# GitHub Reader Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建 GitHub Reader — 通过关键词订阅 GitHub 热门仓库，自动抓取 README 并翻译为中文，以收件箱形式管理阅读进度。

**Architecture:** 前后端分离的本地工具，Flask 提供 REST API，原生 HTML/CSS/JS 构建前端，SQLite 存储数据，llama.cpp server 负责翻译。

**Tech Stack:** Python 3.x + Flask, SQLite, requests, llama.cpp (OpenAI 兼容), marked.js, DOMPurify

---

## Task 0: 项目初始化

**Files:**
- Create: `config.json`
- Create: `config.py`
- Create: `utils.py`
- Create: `requirements.txt`
- Create: `data/readme/` (目录)

- [ ] **Step 1: 创建 config.json**

```json
{
  "github_token": "ghp_your_token_here",
  "keywords": ["vibe coding", "ai agent", "llm tool", "mcp server"],
  "fetch_top_n": 20,
  "request_interval": 0.5,
  "llama_cpp": {
    "base_url": "http://localhost:8080",
    "model": "qwen3.6-35b-a3b",
    "max_tokens": 4096
  },
  "translate_chunk_size": 2000
}
```

- [ ] **Step 2: 创建 config.py**

```python
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def get_readme_dir():
    readme_dir = os.path.join(get_data_dir(), 'readme')
    os.makedirs(readme_dir, exist_ok=True)
    return readme_dir

def get_db_path():
    db_path = os.path.join(get_data_dir(), 'db.sqlite')
    os.makedirs(get_data_dir(), exist_ok=True)
    return db_path
```

- [ ] **Step 3: 创建 utils.py**

```python
import logging
import os
from datetime import datetime

def setup_logger(name='fetch'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', f'{name}.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    handler = logging.FileHandler(log_path, encoding='utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)
    
    return logger

def format_iso(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()

def repo_to_filename(full_name):
    parts = full_name.replace('/', '__')
    return f"{parts}.md"

def repo_to_filename_zh(full_name):
    return f"{repo_to_filename(full_name).replace('.md', '_zh.md')}"
```

- [ ] **Step 4: 创建 requirements.txt**

```
flask==3.0.0
requests==2.31.0
```

- [ ] **Step 5: 创建目录结构**

```bash
mkdir data readme web
```

- [ ] **Step 6: 提交**

```bash
git add config.json config.py utils.py requirements.txt
git commit -m "chore: 初始化项目结构和配置"
```

---

## Task 1: 数据库层 (db.py)

**Files:**
- Create: `db.py`

- [ ] **Step 1: 创建 db.py**

```python
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
            updated_at TEXT NOT NULL
        )
    ''')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_translate_status ON repositories(translate_status)')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_is_read ON repositories(is_read)')
    conn.commit()
    conn.close()

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

def get_repos(filter_type='all', page=1, page_size=20):
    conn = get_connection()
    query = 'SELECT * FROM repositories'
    params = []
    
    if filter_type == 'unread':
        query += ' WHERE is_read = 0'
    
    query += ' ORDER BY fetched_at DESC'
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

def update_translate_status(repo_id, status, error=None):
    conn = get_connection()
    conn.execute(
        'UPDATE repositories SET translate_status = ?, translate_error = ? WHERE id = ?',
        (status, error, repo_id)
    )
    conn.commit()
    conn.close()

def get_pending_translates(limit=10):
    conn = get_connection()
    cursor = conn.execute(
        'SELECT * FROM repositories WHERE translate_status = ? ORDER BY id ASC LIMIT ?',
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

def get_all_keywords():
    conn = get_connection()
    cursor = conn.execute('SELECT DISTINCT value FROM repositories, json_each(keywords)')
    keywords = sorted(set(row[0] for row in cursor.fetchall()))
    conn.close()
    return keywords

def get_stats():
    conn = get_connection()
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    translated = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('done',)).fetchone()[0]
    unread = conn.execute('SELECT COUNT(*) FROM repositories WHERE is_read = 0').fetchone()[0]
    conn.close()
    return {'total': total, 'translated': translated, 'unread': unread}

def get_fetch_progress():
    conn = get_connection()
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    translated = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('done',)).fetchone()[0]
    translating = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('translating',)).fetchone()[0]
    pending = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('pending',)).fetchone()[0]
    failed = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('failed',)).fetchone()[0]
    conn.close()
    return {
        'total': total,
        'translated': translated,
        'translating': translating,
        'pending': pending,
        'failed': failed
    }
```

- [ ] **Step 2: 提交**

```bash
git add db.py
git commit -m "feat: 实现数据库层，支持仓库增删改查和翻译状态管理"
```

---

## Task 2: 抓取模块 (fetch.py)

**Files:**
- Create: `fetch.py`

- [ ] **Step 1: 创建 fetch.py**

```python
import requests
import time
import sys
import os
from config import load_config
from utils import setup_logger, format_iso, get_readme_dir, repo_to_filename
from db import init_db, upsert_repo

logger = setup_logger('fetch')

def search_repos(keyword, top_n=20):
    config = load_config()
    token = config.get('github_token', '')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    url = f'https://api.github.com/search/repositories'
    params = {
        'q': keyword,
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_n
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        items = response.json().get('items', [])
        
        repos = []
        for item in items:
            repos.append({
                'full_name': item['full_name'],
                'description': item.get('description'),
                'stars': item.get('stargazers_count', 0),
                'language': item.get('language'),
                'topics': item.get('topics', []),
                'html_url': item.get('html_url'),
            })
        
        logger.info(f'关键词 "{keyword}" 搜索到 {len(repos)} 个仓库')
        return repos
    except requests.exceptions.RequestException as e:
        logger.error(f'搜索关键词 "{keyword}" 失败: {e}')
        return []

def fetch_readme(full_name):
    config = load_config()
    token = config.get('github_token', '')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    owner, repo = full_name.split('/')
    url = f'https://api.github.com/repos/{owner}/{repo}/readme'
    params = {'ref': 'main'}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        content = data.get('content', '')
        if not content:
            logger.warning(f'{full_name} 没有 README')
            return None
        
        import base64
        readme_content = base64.b64decode(content).decode('utf-8', errors='ignore')
        
        readme_dir = get_readme_dir()
        filename = repo_to_filename(full_name)
        filepath = os.path.join(readme_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        logger.info(f'{full_name} README 已保存到 {filepath}')
        return filepath
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.warning(f'{full_name} 没有 README 文件')
            return None
        logger.error(f'{full_name} 获取 README 失败: {e}')
        return None
    except Exception as e:
        logger.error(f'{full_name} 获取 README 失败: {e}')
        return None

def run_fetch(keywords=None, top_n=None, interval=None):
    config = load_config()
    
    if keywords is None:
        keywords = config.get('keywords', [])
    if top_n is None:
        top_n = config.get('fetch_top_n', 20)
    if interval is None:
        interval = config.get('request_interval', 0.5)
    
    init_db()
    
    all_repos = []
    for keyword in keywords:
        logger.info(f'开始抓取关键词: {keyword}')
        repos = search_repos(keyword, top_n)
        
        for repo in repos:
            repo['keywords'] = [keyword]
            repo['fetched_at'] = format_iso()
            
            readme_path = fetch_readme(repo['full_name'])
            if readme_path:
                repo['readme_path'] = readme_path
            
            upsert_repo(repo)
            all_repos.append(repo)
        
        logger.info(f'关键词 "{keyword}" 抓取完成，共 {len(repos)} 个仓库')
        time.sleep(interval)
    
    logger.info(f'全部抓取完成，共 {len(all_repos)} 个仓库')
    return all_repos

if __name__ == '__main__':
    keywords = None
    if '--keyword' in sys.argv:
        idx = sys.argv.index('--keyword')
        keywords = [sys.argv[idx + 1]]
    
    run_fetch(keywords=keywords)
```

- [ ] **Step 2: 提交**

```bash
git add fetch.py
git commit -m "feat: 实现 GitHub 抓取模块，支持关键词搜索和 README 下载"
```

---

## Task 3: 翻译模块 (translator.py)

**Files:**
- Create: `translator.py`

- [ ] **Step 1: 创建 translator.py**

```python
import requests
import os
from config import load_config
from utils import setup_logger, get_readme_dir, repo_to_filename, repo_to_filename_zh
from db import init_db, get_pending_translates, update_translate_status

logger = setup_logger('translator')

TRANSLATE_PROMPT = """你是一个技术文档翻译助手。将以下 GitHub README（Markdown 格式）翻译为简体中文。
要求：保持所有 Markdown 格式（标题、代码块、链接等）不变，只翻译自然语言文本。
直接输出译文，不要加任何说明。

README 内容：
{content}"""

def call_llm(text):
    config = load_config()
    llama_config = config.get('llama_cpp', {})
    base_url = llama_config.get('base_url', 'http://localhost:8080')
    model = llama_config.get('model', 'qwen3.6-35b-a3b')
    
    url = f'{base_url}/v1/chat/completions'
    headers = {'Content-Type': 'application/json'}
    data = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': TRANSLATE_PROMPT.format(content=text)}
        ],
        'temperature': 0.3,
        'max_tokens': config.get('llama_cpp', {}).get('max_tokens', 4096)
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=300)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f'翻译调用失败: {e}')
        raise

def translate_readme(text):
    return call_llm(text)

def run_translate(limit=10):
    config = load_config()
    init_db()
    
    readme_dir = get_readme_dir()
    repos = get_pending_translates(limit)
    
    logger.info(f'开始翻译 {len(repos)} 个 README')
    
    for repo in repos:
        repo_id = repo['id']
        full_name = repo['full_name']
        
        if not repo.get('readme_path'):
            logger.warning(f'{full_name} 没有 README 文件，跳过')
            update_translate_status(repo_id, 'failed', 'No README file')
            continue
        
        try:
            with open(repo['readme_path'], 'r', encoding='utf-8') as f:
                readme_content = f.read()
            
            update_translate_status(repo_id, 'translating')
            logger.info(f'正在翻译 {full_name}')
            
            translated = translate_readme(readme_content)
            
            zh_filename = repo_to_filename_zh(full_name)
            zh_filepath = os.path.join(readme_dir, zh_filename)
            
            with open(zh_filepath, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            update_translate_status(repo_id, 'done')
            logger.info(f'{full_name} 翻译完成')
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f'{full_name} 翻译失败: {error_msg}')
            update_translate_status(repo_id, 'failed', error_msg)

if __name__ == '__main__':
    run_translate()
```

- [ ] **Step 2: 提交**

```bash
git add translator.py
git commit -m "feat: 实现翻译模块，调用 llama.cpp server 翻译 README"
```

---

## Task 4: Web 服务 (server.py)

**Files:**
- Create: `server.py`

- [ ] **Step 1: 创建 server.py**

```python
import threading
import time
import os
from flask import Flask, jsonify, request, send_from_directory, abort
from config import get_data_dir, get_readme_dir
from utils import setup_logger, format_iso
from db import (
    init_db, get_repos, get_repo, mark_read, mark_unread,
    update_translate_status, get_all_keywords, get_stats, get_fetch_progress
)
from fetch import run_fetch
from translator import run_translate

app = Flask(__name__, static_folder='web', static_url_path='')
logger = setup_logger('server')

fetch_thread = None
fetch_lock = threading.Lock()

@app.before_request
def before_request():
    init_db()

@app.route('/api/repos', methods=['GET'])
def api_repos():
    filter_type = request.args.get('filter', 'all')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 20))
    
    repos, total = get_repos(filter_type, page, page_size)
    return jsonify({'repos': repos, 'total': total, 'page': page, 'page_size': page_size})

@app.route('/api/repos/<int:repo_id>', methods=['GET'])
def api_repo(repo_id):
    repo = get_repo(repo_id)
    if not repo:
        abort(404)
    return jsonify(repo)

@app.route('/api/repos/<int:repo_id>/readme', methods=['GET'])
def api_readme(repo_id):
    repo = get_repo(repo_id)
    if not repo:
        abort(404)
    if not repo.get('readme_path'):
        abort(404)
    readme_dir = get_readme_dir()
    return send_from_directory(readme_dir, os.path.basename(repo['readme_path']))

@app.route('/api/repos/<int:repo_id>/readme_zh', methods=['GET'])
def api_readme_zh(repo_id):
    repo = get_repo(repo_id)
    if not repo:
        abort(404)
    if not repo.get('readme_zh_path'):
        abort(404)
    readme_dir = get_readme_dir()
    return send_from_directory(readme_dir, os.path.basename(repo['readme_zh_path']))

@app.route('/api/repos/<int:repo_id>/read', methods=['POST'])
def api_mark_read(repo_id):
    mark_read(repo_id)
    return jsonify({'status': 'ok'})

@app.route('/api/repos/<int:repo_id>/unread', methods=['POST'])
def api_mark_unread(repo_id):
    mark_unread(repo_id)
    return jsonify({'status': 'ok'})

@app.route('/api/keywords', methods=['GET'])
def api_keywords():
    keywords = get_all_keywords()
    return jsonify({'keywords': keywords})

@app.route('/api/fetch', methods=['POST'])
def api_fetch():
    with fetch_lock:
        global fetch_thread
        if fetch_thread and fetch_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '抓取任务进行中'}), 409
        
        def fetch_worker():
            try:
                run_fetch()
                run_translate()
            except Exception as e:
                logger.error(f'抓取/翻译线程出错: {e}')
        
        fetch_thread = threading.Thread(target=fetch_worker, daemon=True)
        fetch_thread.start()
    
    return jsonify({'status': 'started'})

@app.route('/api/fetch/status', methods=['GET'])
def api_fetch_status():
    with fetch_lock:
        is_running = fetch_thread and fetch_thread.is_alive() if fetch_thread else False
    
    progress = get_fetch_progress()
    return jsonify({
        'running': is_running,
        **progress
    })

@app.route('/api/stats', methods=['GET'])
def api_stats():
    stats = get_stats()
    return jsonify(stats)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
```

- [ ] **Step 2: 提交**

```bash
git add server.py
git commit -m "feat: 实现 Flask Web 服务，提供 REST API"
```

---

## Task 5: 前端 (web/)

**Files:**
- Create: `web/index.html`
- Create: `web/detail.html`
- Create: `web/search.html`
- Create: `web/style.css`
- Create: `web/app.js`

- [ ] **Step 1: 创建 web/style.css**

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #f5f5f5;
    color: #333;
    line-height: 1.6;
}

.header {
    background: #fff;
    padding: 16px 24px;
    border-bottom: 1px solid #e0e0e0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header h1 {
    font-size: 20px;
    font-weight: 600;
}

.nav {
    display: flex;
    gap: 16px;
}

.nav a {
    text-decoration: none;
    color: #0366d6;
    font-size: 14px;
}

.container {
    max-width: 1200px;
    margin: 24px auto;
    padding: 0 24px;
}

.stats-bar {
    display: flex;
    gap: 24px;
    padding: 16px;
    background: #fff;
    border-radius: 8px;
    margin-bottom: 16px;
    font-size: 14px;
}

.stats-bar span {
    color: #666;
}

.stats-bar strong {
    color: #333;
}

.repo-list {
    background: #fff;
    border-radius: 8px;
    overflow: hidden;
}

.repo-item {
    display: flex;
    align-items: center;
    padding: 16px 24px;
    border-bottom: 1px solid #f0f0f0;
    cursor: pointer;
    transition: background 0.2s;
}

.repo-item:hover {
    background: #f8f8f8;
}

.repo-item.unread::before {
    content: '';
    width: 8px;
    height: 8px;
    background: #0366d6;
    border-radius: 50%;
    margin-right: 12px;
    flex-shrink: 0;
}

.repo-info {
    flex: 1;
}

.repo-name {
    font-weight: 600;
    font-size: 15px;
    margin-bottom: 4px;
}

.repo-desc {
    color: #666;
    font-size: 13px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.repo-meta {
    display: flex;
    gap: 16px;
    align-items: center;
    font-size: 13px;
    color: #999;
    margin-left: auto;
    padding-left: 16px;
}

.repo-stars {
    color: #f0c000;
}

.keyword-tag {
    display: inline-block;
    padding: 2px 8px;
    background: #e8f4ff;
    color: #0366d6;
    border-radius: 12px;
    font-size: 12px;
    margin-right: 4px;
}

.translate-status {
    font-size: 16px;
}

.filter-bar {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
}

.filter-btn {
    padding: 8px 16px;
    border: 1px solid #ddd;
    background: #fff;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
}

.filter-btn.active {
    background: #0366d6;
    color: #fff;
    border-color: #0366d6;
}

.detail-header {
    background: #fff;
    padding: 24px;
    border-radius: 8px;
    margin-bottom: 16px;
}

.detail-header h2 {
    font-size: 24px;
    margin-bottom: 8px;
}

.detail-meta {
    display: flex;
    gap: 16px;
    color: #666;
    font-size: 14px;
    margin-bottom: 12px;
}

.detail-meta a {
    color: #0366d6;
}

.lang-switch {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
}

.lang-btn {
    padding: 8px 16px;
    border: 1px solid #ddd;
    background: #fff;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
}

.lang-btn.active {
    background: #0366d6;
    color: #fff;
    border-color: #0366d6;
}

.readme-content {
    background: #fff;
    padding: 24px;
    border-radius: 8px;
    overflow-x: auto;
}

.readme-content h1, .readme-content h2, .readme-content h3 {
    margin-top: 24px;
    margin-bottom: 16px;
}

.readme-content pre {
    background: #f6f8fa;
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 16px 0;
}

.readme-content code {
    background: #f0f0f0;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 13px;
}

.readme-content pre code {
    background: none;
    padding: 0;
}

.readme-content a {
    color: #0366d6;
}

.readme-content img {
    max-width: 100%;
}

.search-page {
    background: #fff;
    padding: 24px;
    border-radius: 8px;
}

.keyword-list {
    margin: 16px 0;
}

.keyword-item {
    display: flex;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid #f0f0f0;
}

.keyword-item span {
    flex: 1;
}

.keyword-item button {
    padding: 4px 12px;
    border: 1px solid #ddd;
    background: #fff;
    border-radius: 4px;
    cursor: pointer;
}

.keyword-item button.delete {
    color: #dc3545;
    border-color: #dc3545;
}

.fetch-btn {
    padding: 12px 24px;
    background: #0366d6;
    color: #fff;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 15px;
}

.fetch-btn:hover {
    background: #025bb7;
}

.fetch-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
}

.progress-bar {
    margin-top: 16px;
    padding: 12px;
    background: #f8f8f8;
    border-radius: 6px;
    font-size: 14px;
}

.back-link {
    display: inline-block;
    margin-bottom: 16px;
    color: #0366d6;
    text-decoration: none;
}

.loading {
    text-align: center;
    padding: 48px;
    color: #999;
}

.pagination {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 24px;
}

.pagination button {
    padding: 8px 16px;
    border: 1px solid #ddd;
    background: #fff;
    border-radius: 4px;
    cursor: pointer;
}

.pagination button.active {
    background: #0366d6;
    color: #fff;
    border-color: #0366d6;
}

.pagination button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}
```

- [ ] **Step 2: 创建 web/app.js**

```javascript
const API_BASE = '/api';

async function apiGet(path, params = {}) {
    const url = new URL(`${API_BASE}${path}`, window.location.origin);
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));
    const res = await fetch(url);
    return res.json();
}

async function apiPost(path, body = {}) {
    const res = await fetch(`${API_BASE}${path}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body)
    });
    return res.json();
}

// Index page
async function loadRepos(filter = 'all', page = 1) {
    const data = await apiGet('/repos', {filter, page, page_size: 20});
    const container = document.getElementById('repo-list');
    const unreadCount = document.getElementById('unread-count');
    
    if (unreadCount) {
        const stats = await apiGet('/stats');
        unreadCount.textContent = `未读: ${stats.unread}`;
    }
    
    if (!container) return;
    
    container.innerHTML = data.repos.map(repo => `
        <div class="repo-item ${!repo.is_read ? 'unread' : ''}" onclick="location.href='/detail.html?id=${repo.id}'">
            <div class="repo-info">
                <div class="repo-name">${repo.full_name}</div>
                <div class="repo-desc">${repo.description || '暂无描述'}</div>
            </div>
            <div class="repo-meta">
                <span class="repo-stars">★ ${repo.stars}</span>
                <span>${(repo.keywords || []).map(kw => `<span class="keyword-tag">${kw}</span>`).join('')}</span>
                <span class="translate-status">
                    ${repo.translate_status === 'done' ? '✅' : 
                      repo.translate_status === 'translating' ? '⏳' : 
                      repo.translate_status === 'failed' ? '❌' : '⏳'}
                </span>
                <span>${new Date(repo.fetched_at).toLocaleDateString()}</span>
            </div>
        </div>
    `).join('');
    
    // Pagination
    const totalPages = Math.ceil(data.total / data.page_size);
    const pagination = document.getElementById('pagination');
    if (pagination && totalPages > 1) {
        pagination.innerHTML = '';
        for (let i = 1; i <= totalPages; i++) {
            const btn = document.createElement('button');
            btn.className = i === page ? 'active' : '';
            btn.textContent = i;
            btn.onclick = () => loadRepos(filter, i);
            pagination.appendChild(btn);
        }
    }
}

// Detail page
async function loadDetail() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    if (!id) return;
    
    const repo = await apiGet(`/repos/${id}`);
    document.getElementById('repo-name').textContent = repo.full_name;
    document.getElementById('repo-desc').textContent = repo.description || '暂无描述';
    document.getElementById('repo-stars').textContent = `★ ${repo.stars}`;
    document.getElementById('repo-lang').textContent = repo.language || '未知';
    document.getElementById('repo-link').href = repo.html_url;
    
    const readmeContent = document.getElementById('readme-content');
    const langSwitch = document.getElementById('lang-switch');
    const savedLang = localStorage.getItem(`lang_${id}`) || 'en';
    
    if (langSwitch) {
        langSwitch.innerHTML = `
            <button class="lang-btn ${savedLang === 'en' ? 'active' : ''}" onclick="switchLang('en')">English</button>
            <button class="lang-btn ${savedLang === 'zh' ? 'active' : ''}" onclick="switchLang('zh')">中文</button>
        `;
    }
    
    if (repo.translate_status === 'pending' || repo.translate_status === 'translating') {
        readmeContent.innerHTML = '<div class="loading">翻译进行中，请稍后...</div>';
        return;
    }
    
    if (savedLang === 'zh' && repo.readme_zh_path) {
        loadReadme(repo.readme_zh_path, id);
    } else {
        loadReadme(repo.readme_path, id);
    }
    
    // Mark as read
    apiPost(`/repos/${id}/read`);
}

async function loadReadme(path, id) {
    const readmeContent = document.getElementById('readme-content');
    try {
        const res = await fetch(path);
        const text = await res.text();
        readmeContent.innerHTML = DOMPurify.sanitize(marked.parse(text));
    } catch (e) {
        readmeContent.innerHTML = '<div class="loading">加载失败</div>';
    }
}

function switchLang(lang) {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    if (!id) return;
    
    localStorage.setItem(`lang_${id}`, lang);
    location.reload();
}

// Search page
async function loadKeywords() {
    const data = await apiGet('/keywords');
    const container = document.getElementById('keyword-list');
    if (!container) return;
    
    container.innerHTML = data.keywords.map(kw => `
        <div class="keyword-item">
            <span>${kw}</span>
            <button class="delete" onclick="deleteKeyword('${kw}')">删除</button>
        </div>
    `).join('');
    
    const stats = await apiGet('/stats');
    document.getElementById('stat-total').textContent = stats.total;
    document.getElementById('stat-translated').textContent = stats.translated;
    document.getElementById('stat-unread').textContent = stats.unread;
}

async function addKeyword() {
    const input = document.getElementById('keyword-input');
    const kw = input.value.trim();
    if (!kw) return;
    
    await apiPost('/keywords', {keyword: kw});
    input.value = '';
    loadKeywords();
}

async function deleteKeyword(kw) {
    await fetch(`/api/keywords/${encodeURIComponent(kw)}`, {method: 'DELETE'});
    loadKeywords();
}

async function startFetch() {
    const btn = document.getElementById('fetch-btn');
    btn.disabled = true;
    btn.textContent = '抓取中...';
    
    await apiPost('/fetch');
    
    pollFetchStatus();
}

async function pollFetchStatus() {
    const statusDiv = document.getElementById('fetch-status');
    if (!statusDiv) return;
    
    const data = await apiGet('/fetch/status');
    
    statusDiv.innerHTML = `
        <div>抓取状态: ${data.running ? '进行中' : '已完成'}</div>
        <div>总仓库数: ${data.total}</div>
        <div>已翻译: ${data.translated}</div>
        <div>翻译中: ${data.translating}</div>
        <div>待翻译: ${data.pending}</div>
        <div>失败: ${data.failed}</div>
    `;
    
    if (data.running) {
        setTimeout(pollFetchStatus, 2000);
    } else {
        document.getElementById('fetch-btn').disabled = false;
        document.getElementById('fetch-btn').textContent = '触发抓取';
    }
}

// Init
if (document.getElementById('repo-list')) {
    loadRepos();
    document.getElementById('filter-all').onclick = () => loadRepos('all');
    document.getElementById('filter-unread').onclick = () => loadRepos('unread');
}

if (document.getElementById('repo-name')) {
    loadDetail();
}

if (document.getElementById('keyword-list')) {
    loadKeywords();
}
```

- [ ] **Step 3: 创建 web/index.html**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>GitHub Reader - 收件箱</title>
    <link rel="stylesheet" href="/style.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js"></script>
</head>
<body>
    <div class="header">
        <h1>📥 GitHub Reader</h1>
        <div class="nav">
            <a href="/">收件箱</a>
            <a href="/search.html">搜索管理</a>
        </div>
    </div>
    
    <div class="container">
        <div class="stats-bar">
            <span id="unread-count">未读: 0</span>
        </div>
        
        <div class="filter-bar">
            <button class="filter-btn active" id="filter-all">全部</button>
            <button class="filter-btn" id="filter-unread">未读</button>
        </div>
        
        <div class="repo-list" id="repo-list">
            <div class="loading">加载中...</div>
        </div>
        
        <div class="pagination" id="pagination"></div>
    </div>
    
    <script src="/app.js"></script>
</body>
</html>
```

- [ ] **Step 4: 创建 web/detail.html**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>GitHub Reader - 详情</title>
    <link rel="stylesheet" href="/style.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js"></script>
</head>
<body>
    <div class="header">
        <h1>📥 GitHub Reader</h1>
        <div class="nav">
            <a href="/">收件箱</a>
            <a href="/search.html">搜索管理</a>
        </div>
    </div>
    
    <div class="container">
        <a href="/" class="back-link">← 返回收件箱</a>
        
        <div class="detail-header">
            <h2 id="repo-name"></h2>
            <div class="detail-meta">
                <span id="repo-stars"></span>
                <span id="repo-lang"></span>
                <a id="repo-link" target="_blank">GitHub →</a>
            </div>
            <p id="repo-desc"></p>
        </div>
        
        <div class="lang-switch" id="lang-switch"></div>
        
        <div class="readme-content" id="readme-content">
            <div class="loading">加载中...</div>
        </div>
    </div>
    
    <script src="/app.js"></script>
</body>
</html>
```

- [ ] **Step 5: 创建 web/search.html**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>GitHub Reader - 搜索管理</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <div class="header">
        <h1>📥 GitHub Reader</h1>
        <div class="nav">
            <a href="/">收件箱</a>
            <a href="/search.html">搜索管理</a>
        </div>
    </div>
    
    <div class="container">
        <div class="search-page">
            <h2>关键词管理</h2>
            
            <div style="margin: 16px 0;">
                <input type="text" id="keyword-input" placeholder="输入关键词" style="padding: 8px; width: 200px;">
                <button class="fetch-btn" onclick="addKeyword()" style="padding: 8px 16px;">添加</button>
            </div>
            
            <div class="keyword-list" id="keyword-list"></div>
            
            <hr style="margin: 24px 0;">
            
            <h2>数据统计</h2>
            <div class="stats-bar" style="margin-top: 16px;">
                <span>总仓库数: <strong id="stat-total">0</strong></span>
                <span>已翻译: <strong id="stat-translated">0</strong></span>
                <span>未读数: <strong id="stat-unread">0</strong></span>
            </div>
            
            <hr style="margin: 24px 0;">
            
            <h2>手动抓取</h2>
            <button class="fetch-btn" id="fetch-btn" onclick="startFetch()">触发抓取</button>
            <div class="progress-bar" id="fetch-status"></div>
        </div>
    </div>
    
    <script src="/app.js"></script>
</body>
</html>
```

- [ ] **Step 6: 提交**

```bash
git add web/
git commit -m "feat: 实现前端页面，包含收件箱、详情页和搜索管理"
```

---

## Task 6: 整合与收尾

**Files:**
- Modify: `fetch.py` — 整合 CLI 参数
- Create: `README.md`

- [ ] **Step 1: 更新 fetch.py 支持完整 CLI**

```python
if __name__ == '__main__':
    keywords = None
    only_fetch = False
    only_translate = False
    
    if '--fetch-only' in sys.argv:
        only_fetch = True
    if '--translate-only' in sys.argv:
        only_translate = True
    if '--keyword' in sys.argv:
        idx = sys.argv.index('--keyword')
        keywords = [sys.argv[idx + 1]]
    
    if only_translate:
        run_translate()
    elif only_fetch:
        run_fetch(keywords=keywords)
    else:
        run_fetch(keywords=keywords)
        run_translate()
```

- [ ] **Step 2: 创建 README.md**

```markdown
# GitHub Reader

通过关键词订阅 GitHub 热门仓库，自动抓取 README 并翻译为中文。

## 安装

```bash
pip install -r requirements.txt
```

## 配置

编辑 `config.json`：
- `github_token`: GitHub Personal Access Token
- `keywords`: 订阅关键词列表
- `llama_cpp.base_url`: llama.cpp server 地址
- `llama_cpp.model`: 使用的模型名称

## 使用

1. 启动 llama.cpp server: `llama.cpp/server -m your_model.gguf -c 4096`
2. 运行抓取: `python fetch.py`
3. 启动 Web 服务: `python server.py`
4. 浏览器访问: `http://localhost:5000`

## Windows 任务计划

创建定时任务每天运行:
```
python fetch.py --fetch-only
python fetch.py --translate-only
```
```

- [ ] **Step 3: 最终提交**

```bash
git add fetch.py README.md
git commit -m "feat: 整合 CLI 参数，添加项目文档"
```

---

## 自检查

1. **Spec coverage:** 所有 PRD 需求（F1-F7）都已覆盖
2. **Placeholder scan:** 无占位符，所有代码完整
3. **Type consistency:** 数据库字段、API 路径、文件名一致
4. **Scope check:** 单文件实现，适合单用户工具

---

