# 描述信息中文翻译 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在仓库列表页展示描述信息的中文翻译，支持批量翻译所有未翻译的描述，可随时中断。

**Architecture:** 在 `repositories` 表新增 `description_zh` 和 `description_translate_status` 字段，复用现有 `translator.py` 的 `call_llm()` 和 `TRANSLATE_PROMPT`，通过异步线程批量翻译，前端轮询进度。

**Tech Stack:** Python 3.x + Flask, SQLite, 原生 HTML/CSS/JS

---

### Task 1: 数据库迁移 — 新增字段

**Files:**
- Modify: `db.py:14-38` — `init_db()` 函数

在 `init_db()` 中新增两个字段。由于 SQLite 不支持对已有表 `ALTER TABLE ADD COLUMN IF NOT EXISTS`，需要在 `init_db()` 中检查字段是否存在，不存在则迁移表。

- [ ] **Step 1: 修改 db.py 新增字段和迁移逻辑**

将 `db.py` 的 `init_db()` 函数替换为以下实现：

```python
def init_db():
    conn = get_connection()
    
    # 检查是否需要迁移（新增的字段）
    cursor = conn.execute("PRAGMA table_info(repositories)")
    columns = [row[1] for row in cursor.fetchall()]
    
    if 'description_zh' not in columns or 'description_translate_status' not in columns:
        # 需要迁移：创建新表 -> 复制数据 -> 删除旧表 -> 创建新表结构
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
            INSERT INTO repositories_new
            SELECT id, full_name, description, stars, language, topics, html_url,
                   readme_path, readme_zh_path, translate_status, translate_error,
                   is_read, keywords, fetched_at, updated_at
            FROM repositories
        ''')
        conn.execute('DROP TABLE repositories')
        conn.execute('DROP INDEX idx_translate_status')
        conn.execute('DROP INDEX idx_is_read')
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
    conn.close()
```

- [ ] **Step 2: 修改 upsert_repo() 适配新字段**

将 `db.py` 的 `upsert_repo()` 函数替换为：

```python
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
```

（此函数本身不需要改动，因为 `upsert_repo()` 只更新抓取时的字段，不更新翻译字段）

- [ ] **Step 3: 验证数据库迁移**

运行：
```bash
cd E:\Projects\htmlSpace\GithubAssistant
python -c "from db import init_db; init_db(); print('OK')"
```

预期输出：`OK`

---

### Task 2: 后端翻译模块 — translator.py

**Files:**
- Modify: `translator.py` — 新增函数和全局标志

- [ ] **Step 1: 在 translator.py 顶部添加全局中断标志**

在 `logger = setup_logger('translator')` 下方添加：

```python
description_translate_stop = False
```

- [ ] **Step 2: 新增 translate_description() 函数**

在 `translate_readme()` 函数之后添加：

```python
def translate_description(description):
    """翻译仓库描述信息为中文，复用 TRANSLATE_PROMPT"""
    return call_llm(description)
```

- [ ] **Step 3: 新增 translate_description_single() 函数**

在 `run_translate()` 函数之后添加：

```python
def translate_description_single(repo_id):
    """翻译单条仓库描述的中文"""
    init_db()
    
    repo = get_repo(repo_id)
    if not repo:
        logger.error(f'仓库 {repo_id} 不存在')
        return False
    
    full_name = repo['full_name']
    description = repo.get('description')
    
    if not description:
        logger.warning(f'{full_name} 没有描述信息，跳过')
        update_translate_status(repo_id, 'failed', 'No description')
        return False
    
    try:
        update_translate_status(repo_id, 'translating')
        logger.info(f'正在翻译 {full_name} 的描述')
        
        translated = translate_description(description)
        
        conn = get_connection()
        conn.execute(
            'UPDATE repositories SET description_zh = ?, description_translate_status = ? WHERE id = ?',
            (translated, 'done', repo_id)
        )
        conn.commit()
        conn.close()
        
        logger.info(f'{full_name} 描述翻译完成')
        return True
        
    except Exception as e:
        error_msg = str(e)
        logger.error(f'{full_name} 描述翻译失败: {error_msg}')
        conn = get_connection()
        conn.execute(
            'UPDATE repositories SET description_translate_status = ?, translate_error = ? WHERE id = ?',
            ('failed', error_msg, repo_id)
        )
        conn.commit()
        conn.close()
        return False
```

- [ ] **Step 4: 新增 run_translate_descriptions() 函数**

在 `translate_description_single()` 之后添加：

```python
def run_translate_descriptions():
    """批量翻译所有待翻译的仓库描述"""
    global description_translate_stop
    
    init_db()
    
    conn = get_connection()
    cursor = conn.execute(
        'SELECT * FROM repositories WHERE description_translate_status = ? AND description IS NOT NULL AND LENGTH(description) > 0 ORDER BY id ASC',
        ('pending',)
    )
    rows = cursor.fetchall()
    conn.close()
    
    repos = []
    for row in rows:
        repo = dict(row)
        repo['topics'] = json.loads(repo['topics']) if repo['topics'] else []
        repo['keywords'] = json.loads(repo['keywords']) if repo['keywords'] else []
        repos.append(repo)
    
    logger.info(f'开始翻译 {len(repos)} 个仓库描述')
    
    total = len(repos)
    done = 0
    failed = 0
    
    for repo in repos:
        if description_translate_stop:
            logger.info(f'描述翻译被中断，已翻译 {done}/{total}')
            return {'total': total, 'done': done, 'failed': failed, 'stopped': True}
        
        repo_id = repo['id']
        full_name = repo['full_name']
        
        try:
            update_translate_status(repo_id, 'translating')
            logger.info(f'正在翻译 {full_name} 的描述')
            
            description = repo.get('description')
            translated = translate_description(description)
            
            conn = get_connection()
            conn.execute(
                'UPDATE repositories SET description_zh = ?, description_translate_status = ? WHERE id = ?',
                (translated, 'done', repo_id)
            )
            conn.commit()
            conn.close()
            
            done += 1
            logger.info(f'{full_name} 描述翻译完成')
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f'{full_name} 描述翻译失败: {error_msg}')
            conn = get_connection()
            conn.execute(
                'UPDATE repositories SET description_translate_status = ?, translate_error = ? WHERE id = ?',
                ('failed', error_msg, repo_id)
            )
            conn.commit()
            conn.close()
            failed += 1
    
    logger.info(f'描述翻译完成: 成功 {done}, 失败 {failed}')
    return {'total': total, 'done': done, 'failed': failed, 'stopped': False}
```

- [ ] **Step 5: 验证 translator.py 语法**

运行：
```bash
python -c "import ast; ast.parse(open('translator.py').read()); print('Syntax OK')"
```

---

### Task 3: 后端 API 路由 — server.py

**Files:**
- Modify: `server.py` — 新增导入和路由

- [ ] **Step 1: 修改导入语句**

将 `server.py` 第 12 行的导入：
```python
from translator import run_translate, translate_single_repo
```

改为：
```python
from translator import run_translate, translate_single_repo, run_translate_descriptions
```

- [ ] **Step 2: 添加全局中断标志引用**

在 `fetch_lock = threading.Lock()` 下方添加：
```python
description_translate_thread = None
```

- [ ] **Step 3: 新增三个 API 路由**

在 `api_stats()` 函数之后、`if __name__ == '__main__':` 之前添加：

```python
@app.route('/api/description/translate', methods=['POST'])
def api_description_translate():
    global description_translate_thread
    import translator
    
    with fetch_lock:
        if description_translate_thread and description_translate_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '翻译任务进行中'}), 409
        
        def translate_worker():
            try:
                run_translate_descriptions()
            except Exception as e:
                logger.error(f'描述翻译线程出错: {e}')
        
        description_translate_thread = threading.Thread(target=translate_worker, daemon=True)
        description_translate_thread.start()
    
    return jsonify({'status': 'started'})

@app.route('/api/description/translate/status', methods=['GET'])
def api_description_translate_status():
    global description_translate_thread
    
    with fetch_lock:
        is_running = description_translate_thread and description_translate_thread.is_alive() if description_translate_thread else False
    
    conn = get_connection()
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    desc_done = conn.execute('SELECT COUNT(*) FROM repositories WHERE description_translate_status = ?', ('done',)).fetchone()[0]
    desc_failed = conn.execute('SELECT COUNT(*) FROM repositories WHERE description_translate_status = ?', ('failed',)).fetchone()[0]
    conn.close()
    
    return jsonify({
        'running': is_running,
        'total': total,
        'done': desc_done,
        'failed': desc_failed
    })

@app.route('/api/description/translate/stop', methods=['POST'])
def api_description_translate_stop():
    import translator
    translator.description_translate_stop = True
    return jsonify({'status': 'stopped'})
```

- [ ] **Step 4: 修改 api_repos() 确保返回新字段**

`api_repos()` 函数本身不需要改动，因为 `get_repos()` 返回完整行数据，新字段会自动包含在结果中。但需要确认 `make_relative_path()` 不影响新字段（它只处理 `readme_path` 和 `readme_zh_path`）。

- [ ] **Step 5: 验证 server.py 语法**

运行：
```bash
python -c "import ast; ast.parse(open('server.py').read()); print('Syntax OK')"
```

---

### Task 4: 前端列表页 — index.html

**Files:**
- Modify: `web/index.html`

- [ ] **Step 1: 在 stats-bar 中新增翻译按钮和进度区域**

将 `.stats-bar` 部分替换为：

```html
<div class="stats-bar">
    <span id="unread-count">未读: 0</span>
    <div class="desc-translate-actions" id="desc-translate-actions" style="display: none;">
        <button class="filter-btn" id="translate-desc-btn">翻译全部</button>
        <button class="filter-btn" id="stop-translate-btn" style="display: none; background: #dc3545; color: #fff; border-color: #dc3545;">停止</button>
        <span id="desc-translate-progress" style="margin-left: 12px; font-size: 13px; color: #666;"></span>
    </div>
</div>
```

- [ ] **Step 2: 验证 HTML 结构**

确保 HTML 标签闭合正确。

---

### Task 5: 前端列表渲染 — app.js

**Files:**
- Modify: `web/app.js` — 修改列表渲染和新增翻译函数

- [ ] **Step 1: 修改 loadRepos() 中的列表渲染**

将第 32-49 行的列表渲染代码替换为：

```javascript
container.innerHTML = data.repos.map(repo => `
    <div class="repo-item ${repo.is_read ? 'read' : 'unread'}" data-id="${repo.id}">
        <div class="repo-info">
            <div class="repo-name">${repo.full_name}</div>
            <div class="repo-desc">${repo.description || '暂无描述'}</div>
            ${repo.description_zh ? `<div class="repo-desc-zh">${repo.description_zh}</div>` : ''}
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
```

- [ ] **Step 2: 在 loadRepos() 中显示/隐藏翻译按钮**

在 `loadRepos()` 函数的 `container.innerHTML = ...` 之后、分页代码之前，添加：

```javascript
// 显示翻译按钮（如果有未翻译的描述）
const hasPending = data.repos.some(r => r.description && !r.description_zh);
const descActions = document.getElementById('desc-translate-actions');
if (descActions) {
    descActions.style.display = hasPending ? 'flex' : 'none';
}
```

- [ ] **Step 3: 新增 startTranslateDescriptions() 函数**

在 `pollTranslateStatus(id)` 函数之后添加：

```javascript
async function startTranslateDescriptions() {
    const btn = document.getElementById('translate-desc-btn');
    const stopBtn = document.getElementById('stop-translate-btn');
    const progress = document.getElementById('desc-translate-progress');
    
    btn.disabled = true;
    btn.style.display = 'none';
    stopBtn.style.display = 'inline-block';
    progress.textContent = '翻译进行中...';
    
    try {
        await apiPost('/description/translate');
        pollDescriptionTranslateStatus();
    } catch (e) {
        progress.textContent = '操作失败';
        btn.disabled = false;
        btn.style.display = 'inline-block';
        stopBtn.style.display = 'none';
    }
}

async function pollDescriptionTranslateStatus() {
    const btn = document.getElementById('translate-desc-btn');
    const stopBtn = document.getElementById('stop-translate-btn');
    const progress = document.getElementById('desc-translate-progress');
    
    const data = await apiGet('/description/translate/status');
    
    if (data.running) {
        progress.textContent = `翻译中: ${data.done}/${data.total}`;
        setTimeout(() => pollDescriptionTranslateStatus(), 2000);
    } else {
        progress.textContent = `翻译完成: ${data.done}/${data.total}, 失败 ${data.failed}`;
        btn.style.display = 'none';
        stopBtn.style.display = 'none';
        
        // 刷新列表
        const filterBtn = document.querySelector('.filter-btn.active');
        const filter = filterBtn ? (filterBtn.id === 'filter-read' ? 'read' : filterBtn.id === 'filter-unread' ? 'unread' : 'all') : 'all';
        loadRepos(filter, 1, 'fetched_at', 'desc');
    }
}

// 停止翻译
async function stopTranslateDescriptions() {
    const btn = document.getElementById('translate-desc-btn');
    const stopBtn = document.getElementById('stop-translate-btn');
    const progress = document.getElementById('desc-translate-progress');
    
    try {
        await apiPost('/description/translate/stop');
        progress.textContent = '已停止';
        btn.style.display = 'none';
        stopBtn.style.display = 'none';
        
        // 刷新列表
        const filterBtn = document.querySelector('.filter-btn.active');
        const filter = filterBtn ? (filterBtn.id === 'filter-read' ? 'read' : filterBtn.id === 'filter-unread' ? 'unread' : 'all') : 'all';
        loadRepos(filter, 1, 'fetched_at', 'desc');
    } catch (e) {
        progress.textContent = '停止失败';
    }
}
```

- [ ] **Step 4: 添加按钮事件绑定**

在文件末尾的 `if (document.getElementById('repo-list'))` 块中，添加：

```javascript
document.getElementById('translate-desc-btn').onclick = startTranslateDescriptions;
document.getElementById('stop-translate-btn').onclick = stopTranslateDescriptions;
```

- [ ] **Step 5: 验证 app.js 语法**

运行（在浏览器控制台或通过 Node.js 检查）：
```bash
node -c web/app.js
```

---

### Task 6: 前端样式 — style.css

**Files:**
- Modify: `web/style.css`

- [ ] **Step 1: 新增 .repo-desc-zh 样式**

在 `.repo-desc` 样式之后添加：

```css
.repo-desc-zh {
    color: #888;
    font-size: 12px;
    margin-top: 2px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

- [ ] **Step 2: 新增翻译按钮容器样式**

在 `.stats-bar` 样式之后添加：

```css
.desc-translate-actions {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-left: auto;
}
```

---

### Task 7: 集成测试

- [ ] **Step 1: 启动服务验证**

运行：
```bash
cd E:\Projects\htmlSpace\GithubAssistant
python server.py
```

访问 `http://localhost:5000/`，确认：
1. 列表页正常显示
2. 有未翻译描述的仓库显示"翻译全部"按钮
3. 点击"翻译全部"后按钮变为"停止"，进度条显示进度
4. 点击"停止"后翻译中断
5. 翻译完成后中文描述显示在英文描述下方

- [ ] **Step 2: 验证 API 接口**

```bash
# 触发翻译
curl -X POST http://localhost:5000/api/description/translate

# 查询状态
curl http://localhost:5000/api/description/translate/status

# 停止翻译
curl -X POST http://localhost:5000/api/description/translate/stop
```

---

## 影响文件清单

| 文件 | 变更类型 | 说明 |
|------|---------|------|
| `db.py` | 修改 | 新增字段迁移逻辑 |
| `translator.py` | 修改 | 新增 3 个函数 + 1 个全局标志 |
| `server.py` | 修改 | 新增 3 个 API 路由 |
| `web/index.html` | 修改 | 新增翻译按钮和进度区域 |
| `web/app.js` | 修改 | 修改列表渲染 + 新增 3 个函数 |
| `web/style.css` | 修改 | 新增 2 个样式类 |
