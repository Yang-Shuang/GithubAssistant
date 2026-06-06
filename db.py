import sqlite3
import json
import os
from config import get_db_path
from utils import format_iso

def get_connection():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def init_db():
    conn = get_connection()
    
    # 检查是否需要迁移（新增的字段）
    cursor = conn.execute("PRAGMA table_info(repositories)")
    columns = [row[1] for row in cursor.fetchall()]
    
    if 'description_zh' not in columns or 'description_translate_status' not in columns:
        # 需要迁移：创建新表 -> 复制数据 -> 删除旧表 -> 创建新表结构
        try:
            conn.execute('DROP TABLE repositories_new')
        except Exception:
            pass
        conn.execute('''
            CREATE TABLE repositories_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT UNIQUE NOT NULL,
                description TEXT,
                stars INTEGER DEFAULT 0,
                language TEXT,
                topics TEXT,
                html_url TEXT,
                readme_path TEXT,
                readme_zh_path TEXT,
                translate_status TEXT DEFAULT 'pending',
                translate_error TEXT,
                is_read INTEGER DEFAULT 0,
                keywords TEXT,
                fetched_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                description_zh TEXT,
                description_translate_status TEXT DEFAULT 'pending'
            )
        ''')
        # 复制所有数据（不含新字段，它们默认为 NULL）
        conn.execute('''
            INSERT INTO repositories_new (id, full_name, description, stars, language, topics, html_url, readme_path, readme_zh_path, translate_status, translate_error, is_read, keywords, fetched_at, updated_at)
            SELECT id, full_name, description, stars, language, topics, html_url, readme_path, readme_zh_path, translate_status, translate_error, is_read, keywords, fetched_at, updated_at
            FROM repositories
        ''')
        conn.execute('DROP TABLE repositories')
        conn.execute('ALTER TABLE repositories_new RENAME TO repositories')
        conn.execute('CREATE INDEX idx_translate_status ON repositories(translate_status)')
        conn.execute('CREATE INDEX idx_is_read ON repositories(is_read)')
    
    else:
        # 表结构已存在，确保表已创建
        conn.execute('''
            CREATE TABLE IF NOT EXISTS repositories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT UNIQUE NOT NULL,
                description TEXT,
                stars INTEGER DEFAULT 0,
                language TEXT,
                topics TEXT,
                html_url TEXT,
                readme_path TEXT,
                readme_zh_path TEXT,
                translate_status TEXT DEFAULT 'pending',
                translate_error TEXT,
                is_read INTEGER DEFAULT 0,
                keywords TEXT,
                fetched_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                description_zh TEXT,
                description_translate_status TEXT DEFAULT 'pending'
            )
        ''')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_translate_status ON repositories(translate_status)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_is_read ON repositories(is_read)')
    
    conn.commit()
    
    # 迁移：将绝对路径转换为相对路径（文件名）
    migrate_paths()
    
    conn.close()


def migrate_paths():
    """将 readme_path/readme_zh_path 从绝对路径迁移为相对路径（文件名）"""
    conn = get_connection()
    cursor = conn.execute('SELECT id, readme_path, readme_zh_path FROM repositories')
    
    for row in cursor:
        repo_id, rp, rzp = row[0], row[1], row[2]
        
        updates = []
        # 已迁移的路径就是纯文件名（不含路径分隔符），跳过
        if rp and ('/' in str(rp) or '\\' in str(rp)):
            updates.append(('readme_path', os.path.basename(str(rp))))
        if rzp and ('/' in str(rzp) or '\\' in str(rzp)):
            updates.append(('readme_zh_path', os.path.basename(str(rzp))))
        
        if updates:
            for field, value in updates:
                conn.execute(f'UPDATE repositories SET {field} = ? WHERE id = ?', (value, repo_id))
    
    conn.commit()


def upsert_repo(data):
    conn = get_connection()
    now = format_iso()
    
    topics_json = json.dumps(data.get('topics', []), ensure_ascii=False) if isinstance(data.get('topics'), list) else None
    keywords_json = json.dumps(data.get('keywords', []), ensure_ascii=False) if isinstance(data.get('keywords'), list) else None
    
    try:
        conn.execute('''
            INSERT INTO repositories (full_name, description, stars, language, topics, html_url, 
                readme_path, readme_zh_path, translate_status, translate_error, is_read, keywords, fetched_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', NULL, 0, ?, ?, ?)
            ON CONFLICT(full_name) DO UPDATE SET
                stars = excluded.stars,
                description = excluded.description,
                language = excluded.language,
                topics = excluded.topics,
                html_url = excluded.html_url,
                updated_at = ?
        ''', (
            data['full_name'],
            data.get('description'),
            data.get('stars', 0),
            data.get('language'),
            topics_json,
            data.get('html_url'),
            data.get('readme_path'),
            data.get('readme_zh_path'),
            keywords_json,
            data.get('fetched_at', format_iso()),
            now,
            now
        ))
    except sqlite3.IntegrityError:
        conn.execute('''
            UPDATE repositories SET
                stars = ?,
                description = ?,
                language = ?,
                topics = ?,
                html_url = ?,
                updated_at = ?
            WHERE full_name = ?
        ''', (
            data.get('stars', 0),
            data.get('description'),
            data.get('language'),
            topics_json,
            data.get('html_url'),
            now,
            data['full_name']
        ))
    
    conn.commit()
    conn.close()

def get_repos(filter_type='all', page=1, page_size=20, sort_by='fetched_at', sort_order='desc'):
    conn = get_connection()
    query = 'SELECT * FROM repositories'
    params = []
    
    if filter_type == 'unread':
        query += ' WHERE is_read = 0'
    elif filter_type == 'read':
        query += ' WHERE is_read = 1'
    
    # 排序字段验证
    allowed_sort_fields = ['fetched_at', 'stars']
    sort_field = sort_by if sort_by in allowed_sort_fields else 'fetched_at'
    sort_dir = 'desc' if sort_order == 'desc' else 'asc'
    
    query += f' ORDER BY {sort_field} {sort_dir}'
    query += ' LIMIT ? OFFSET ?'
    params.extend([page_size, (page - 1) * page_size])
    
    cursor = conn.execute(query, params)
    rows = cursor.fetchall()
    
    repos = []
    for row in rows:
        repo = dict(row)
        repo['topics'] = json.loads(repo['topics']) if repo['topics'] else []
        repo['keywords'] = json.loads(repo['keywords']) if repo['keywords'] else []
        repos.append(repo)
    
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    conn.close()
    
    return repos, total

def get_repo(repo_id):
    conn = get_connection()
    cursor = conn.execute('SELECT * FROM repositories WHERE id = ?', (repo_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return None
    
    repo = dict(row)
    repo['topics'] = json.loads(repo['topics']) if repo['topics'] else []
    repo['keywords'] = json.loads(repo['keywords']) if repo['keywords'] else []
    return repo

def mark_read(repo_id):
    conn = get_connection()
    conn.execute('UPDATE repositories SET is_read = 1 WHERE id = ?', (repo_id,))
    conn.commit()
    conn.close()

def mark_unread(repo_id):
    conn = get_connection()
    conn.execute('UPDATE repositories SET is_read = 0 WHERE id = ?', (repo_id,))
    conn.commit()
    conn.close()

def update_translate_status(repo_id, status, error=None, readme_zh_path=None):
    conn = get_connection()
    if readme_zh_path:
        conn.execute(
            'UPDATE repositories SET translate_status = ?, translate_error = ?, readme_zh_path = ? WHERE id = ?',
            (status, error, readme_zh_path, repo_id)
        )
    else:
        conn.execute(
            'UPDATE repositories SET translate_status = ?, translate_error = ? WHERE id = ?',
            (status, error, repo_id)
        )
    conn.commit()
    conn.close()

def get_pending_translates(limit=10):
    conn = get_connection()
    cursor = conn.execute(
        'SELECT * FROM repositories WHERE translate_status = ? ORDER BY stars DESC NULLS LAST LIMIT ?',
        ('pending', limit)
    )
    rows = cursor.fetchall()
    conn.close()
    
    repos = []
    for row in rows:
        repo = dict(row)
        repo['topics'] = json.loads(repo['topics']) if repo['topics'] else []
        repo['keywords'] = json.loads(repo['keywords']) if repo['keywords'] else []
        repos.append(repo)
    return repos

def get_existing_readme_names():
    """返回已有 README 文件的仓库 full_name 列表"""
    conn = get_connection()
    cursor = conn.execute(
        'SELECT full_name FROM repositories WHERE readme_path IS NOT NULL AND readme_path != ""'
    )
    rows = cursor.fetchall()
    conn.close()
    
    return set(row[0] for row in rows)

def get_all_keywords():
    conn = get_connection()
    cursor = conn.execute('SELECT DISTINCT value FROM repositories, json_each(keywords)')
    keywords = sorted(set(row[0] for row in cursor.fetchall()))
    conn.close()
    return keywords

def get_stats():
    conn = get_connection()
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    translated = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('done',)
    ).fetchone()[0]
    unread = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE is_read = 0'
    ).fetchone()[0]
    
    read_count = total - unread
    max_stars_row = conn.execute('SELECT MAX(stars) FROM repositories').fetchone()[0] or 0
    
    desc_translated = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE description_translate_status = ?', ('done',)
    ).fetchone()[0]
    
    readme_pending = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('pending',)).fetchone()[0]
    
    cursor2 = conn.execute('''SELECT value, COUNT(*) as cnt 
           FROM repositories, json_each(topics) 
           WHERE topics IS NOT NULL AND topics != '[]'
           GROUP BY value 
           ORDER BY cnt DESC, value ASC''')
    
    desc_pending = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE description_translate_status = ?', ('pending',)
    ).fetchone()[0]
    
    conn.close()
    
    return {
        'total': total,
        'read_count': read_count,
        'unread': unread,
        'max_stars': max_stars_row,
        'translated_readme': translated,
        'pending_readme': readme_pending,
        'desc_translated': desc_translated,
        'pending_desc': desc_pending,
    }


def get_all_topics():
    """获取所有不重复的 topics，按出现频率降序排列"""
    conn = get_connection()
    # 统计每个topic出现的次数，按频次降序、名称升序（同频字母序）
    cursor = conn.execute(
        '''SELECT value, COUNT(*) as cnt 
           FROM repositories, json_each(topics) 
           WHERE topics IS NOT NULL AND topics != '[]'
           GROUP BY value 
           ORDER BY cnt DESC, value ASC'''
    )
    rows = cursor.fetchall()
    conn.close()
    
     # 返回带计数的topics列表，按频次降序排列（前端可根据屏幕宽度决定显示数量）
    return [{'name': row[0], 'count': row[1]} for row in rows]


def get_all_topics_list():
    """获取所有不重复的 topics（简单列表格式，兼容旧调用）"""
    conn = get_connection()
    cursor = conn.execute(
        '''SELECT DISTINCT value FROM repositories, json_each(topics) 
           WHERE topics IS NOT NULL AND topics != '[]'
           ORDER BY value'''
    )
    topics = sorted(set(row[0] for row in cursor.fetchall()))
    conn.close()
    return topics[:100]  # 最多返回100个


def get_db_schema():
    """返回数据库表结构信息（字段名、类型、是否必填）"""
    import sqlite3
    
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('PRAGMA table_info(repositories)')
    
    columns_raw = cursor.fetchall()
    columns = []
    for row in columns_raw:
        columns.append({
            'name': row[1],
            'type': row[2] if row[2] else 'TEXT',
            'not_null': bool(row[3]),
            'primary_key': bool(row[5])  # pk column index is 5
        })
    
    conn.close()
    return columns

def get_fetch_progress():
    conn = get_connection()
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    translated = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('done',)).fetchone()[0]
    pending = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('pending',)).fetchone()[0]
    conn.close()
    return {
        'total': total,
        'translated': translated,
        'pending': pending
    }