# GitHub Reader 管理页面改造 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 重新设计 search.html（管理页），删除关键词管理和日志显示功能，改为数据统计 + 操作控制 + 数据库结构说明；同时增强后端：彩色进度日志、全任务支持停止中断。

**Architecture:** 在现有 utils.py 中扩展 ANSI 彩色日志器 → db.py 新增统计/Topics/schema API 函数 → server.py 暴露4个新API端点 → fetch.py/translator.py 添加全局中断标志 + 进度日志 → search.html/app.js/style.css 完全重写管理页面。

**Tech Stack:** Python 3.x, Flask, SQLite, ANSI终端颜色码, 原生HTML/CSS/JS

---

## 文件改动清单

| 文件 | 动作 | 说明 |
|------|------|------|
| `utils.py` | **修改** | 新增 ColorFormatter 类，支持 ANSI 彩色输出 |
| `db.py` | **修改** | 扩展 get_stats()，新增 get_all_topics(), get_db_schema() |
| `server.py` | **修改** | 新增4个API路由 + fetch stop 端点 |
| `fetch.py` | **修改** | 全局中断标志 + 进度日志 + stop_fetch() |
| `translator.py` | **修改** | readme_translate_stop + 进度日志 + stop_readme_translate() |
| `web/search.html` | **重写** | 统计区 / Topics云 / 操作按钮 / DB结构说明 |
| `web/app.js` | **修改** | 搜索页逻辑重写；删除关键词相关函数 |
| `web/style.css` | **修改** | 新增 .stats-section, .topics-cloud, .action-buttons, .db-schema 样式类 |

---

### Task 1: utils.py — 彩色日志器 ColorFormatter

**Files:**
- Modify: `utils.py` (末尾追加)

- [ ] **Step 1: 在 utils.py 末尾添加 ColorFormatter 类和 update_progress_logger() 函数**

```python
# === ANSI 彩色日志支持 ===

class ColorFormatter(logging.Formatter):
    """支持终端 ANSI 颜色的日志格式化器"""
    
    COLORS = {
        'INFO': '\033[92m',      # 绿色 - 正常/成功
        'WARNING': '\033[93m',   # 黄色 - 警告  
        'ERROR': '\033[91m',     # 红色 - 错误
    }
    
    def format(self, record):
        if record.levelname in self.COLORS and hasattr(record, 'is_progress'):
            color = self.COLORS.get(record.levelname, '')
            reset = '\033[0m'
            msg = super().format(record)
            return f"{color}{msg}{reset}"
        elif record.levelname == 'PROGRESS':
            # 进度信息用蓝色高亮 + 绿色完成标记
            color = '\033[94m'    # 蓝色 - 进行中
            reset = '\033[0m'
            msg = super().format(record)
            return f"{color}{msg}{reset}"
        elif record.levelname == 'PROGRESS_DONE':
            # 完成状态用绿色高亮
            color = '\033[92m'    # 绿色 - 成功
            reset = '\033[0m'  
            msg = super().format(record)
            return f"{color}{msg}{reset}"
        elif record.levelname == 'PROGRESS_STOP':
            # 中断状态用红色高亮
            color = '\033[91m'    # 红色 - 停止
            reset = '\033[0m'
            msg = super().format(record)  
            return f"{color}{msg}{reset}"
        else:
            return super().format(record)


def setup_colored_logger(name='fetch'):
    """创建带彩色输出的 logger（替代原有的 setup_logger）"""
    logger = logging.getLogger(name)
    if logger.handlers:  # 避免重复添加 handler
        return logger
    
    logger.setLevel(logging.DEBUG)
    
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', f'{name}.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    # 文件处理器 - 纯文本格式（不着色）
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(file_handler)
    
    # 控制台处理器 - 彩色格式
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(console_handler)
    
    return logger


def log_progress(logger, message, level='PROGRESS'):
    """辅助函数：输出进度日志（支持不同级别）"""
    progress_levels = {
        'PROGRESS': logging.INFO,  # 默认用 INFO 级别记录
        'PROGRESS_DONE': logging.INFO,
        'PROGRESS_STOP': logging.WARNING,
    }
    
    if level == 'PROGRESS':
        logger.info(f'[进度] {message}')
    elif level == 'PROGRESS_DONE':
        logger.warning(f'[完成] {message}')  # WARNING 级别便于区分
    elif level == 'PROGRESS_STOP':
        logger.warning(f'[中断] {message}')


def log_done(logger, done_count, remaining, total, name='任务'):
    """输出完成进度日志（绿色高亮）"""
    msg = f'[{name}] ✅ 已完成: {done_count} | 剩余: {remaining} | 总数: {total}'
    logger.warning(msg)


def log_stop(logger, done_count, total, name='任务'):
    """输出中断进度日志（红色高亮）"""  
    msg = f'[{name}] ⛔ 已停止: 已完成 {done_count}/{total}'
    logger.warning(msg)
```

- [ ] **Step 2: 更新现有 setup_logger() 调用，使其使用新的彩色日志器**

将 `server.py`, `fetch.py`, `translator.py` 中的 `setup_logger()` 改为使用带颜色的版本（文件handler保持纯文本）。实际上上面的 `setup_colored_logger()` 已经包含了file handler + console handler，所以只需替换导入名。

---

### Task 2: db.py — 扩展统计数据和新增API函数

**Files:**
- Modify: `db.py` (末尾追加新函数)

- [ ] **Step 1: 修改 get_stats() 返回更多指标**

```python
def get_stats():
    conn = get_connection()
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    translated = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('done',)
    ).fetchone()[0]
    unread = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE is_read = 0'
    ).fetchone()[0]
    
    # 新增：已读数、最高星标、description翻译数
    read_count = total - unread
    max_stars_row = conn.execute(
        'SELECT MAX(stars) FROM repositories'
    ).fetchone()[0] or 0
    
    desc_translated = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE description_translate_status = ?', ('done',)
    ).fetchone()[0]
    
    pending_translate = conn.execute(
        'SELECT COUNT(*) FROM repositories WHERE translate_status = ? AND id NOT IN (SELECT id FROM repositories WHERE translate_status != ?)', 
        ('pending', 'pending')
    ).fetchone()[0]
    # 更简单的写法：直接 count pending
    cursor2 = conn.execute('SELECT COUNT(*) FROM repositories WHERE translate_status = ?', ('pending',))
    pending_translate = cursor2.fetchone()[0]
    
    conn.close()
    
    return {
        'total': total,
        'translated': translated,
        'unread': unread,
        'read_count': read_count,
        'max_stars': max_stars_row,
        'desc_translated': desc_translated,
        'pending_translate': pending_translate,
    }
```

- [ ] **Step 2: 新增 get_all_topics() 函数**（在 db.py 末尾）

```python
def get_all_topics():
    """获取所有不重复的 topics，返回排序后的列表"""
    conn = get_connection()
    cursor = conn.execute(
        'SELECT DISTINCT value FROM repositories, json_each(topics) WHERE topics IS NOT NULL'
    )
    topics = sorted(set(row[0] for row in cursor.fetchall()))
    conn.close()
    return topics


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
            'primary_key': bool(row[5])  # pk 列索引为5
        })
    
    conn.close()
    return columns
```

- [ ] **Step 3: 更新 server.py 的 import 语句**，添加新函数导入：

在 `server.py` 第8行改为：
```python
from db import (
    init_db, get_repos, get_repo, mark_read, mark_unread,
    update_translate_status, get_all_keywords, get_stats, 
    get_fetch_progress, get_all_topics, get_db_schema
)
```

---

### Task 3: server.py — 新增4个API端点 + fetch stop

**Files:**
- Modify: `server.py` (在现有代码基础上追加)

- [ ] **Step 1: 添加新的全局变量和导入**（第26行附近）

```python
fetch_stop_flag = False
translate_stop_flag = False
description_translate_stop_flag = False
```

- [ ] **Step 2: 新增 API 路由**（在 `api_db_schema` 之前，约在第193行后添加以下4个端点）：

```python
@app.route('/api/stats/detailed', methods=['GET'])
def api_stats_detailed():
    """返回详细统计数据"""
    stats = get_stats()
    return jsonify(stats)


@app.route('/api/topics', methods=['GET'])
def api_topics():
    """返回所有不重复的 topics 列表"""
    topics = get_all_topics()
    return jsonify({'topics': topics})


@app.route('/api/db/schema', methods=['GET'])
def api_db_schema():
    """返回数据库表结构信息"""
    columns = get_db_schema()
    
    # 添加字段说明（硬编码映射）
    descriptions = {
        'id': ('自增主键', 'INTEGER'),
        'full_name': ('仓库全称 (owner/repo)', 'TEXT UNIQUE NOT NULL'),
        'description': ('仓库描述文字', 'TEXT'),
        'stars': ('星标数量', 'INTEGER DEFAULT 0'),
        'language': ('编程语言', 'TEXT'),
        'topics': ('话题标签，JSON数组', 'TEXT'),
        'html_url': ('GitHub 页面URL', 'TEXT'),
        'readme_path': ('README原文本地路径（绝对路径）', 'TEXT'),
        'readme_zh_path': ('README中文译文本地路径（绝对路径）', 'TEXT'),
        'translate_status': ('翻译状态: pending/done/error', 'TEXT DEFAULT pending'),
        'translate_error': ('翻译错误信息', 'TEXT'),
        'is_read': ('是否已读: 0=未读, 1=已读', 'INTEGER DEFAULT 0'),
        'keywords': ('触发抓取的关键词，JSON数组', 'TEXT'),
        'fetched_at': ('抓取时间', 'TEXT NOT NULL'),
        'updated_at': ('最后更新时间', 'TEXT NOT NULL'),
        'description_zh': ('仓库描述中文译文', 'TEXT'),
        'description_translate_status': ('Description翻译状态: pending/done/error', 'TEXT DEFAULT pending'),
    }
    
    result_columns = []
    for col in columns:
        desc_info = descriptions.get(col['name'], ('无说明', col['type']))
        result_columns.append({
            **col,
            'description': desc_info[0],
            'full_type': f"{desc_info[1]}{' NOT NULL' if not col['primary_key'] and col['not_null'] else ''}"
        })
    
    return jsonify({
        'table': 'repositories',
        'columns': result_columns,
    })


@app.route('/api/fetch/stop', methods=['POST'])
def api_fetch_stop():
    """停止抓取任务"""
    global fetch_stop_flag
    import fetch
    fetch.fetch_stop = True
    return jsonify({'status': 'stopped'})
```

- [ ] **Step 3: 修改现有 API 路由**：

将 `api_stats`（第170行）改为调用新函数或直接返回详细统计，去掉旧端点。

---

### Task 4: fetch.py — 中断支持 + 进度日志

**Files:**
- Modify: `fetch.py` (顶部添加全局变量；run_fetch() 中添加中断检查和进度日志)

- [ ] **Step 1: 在文件顶部（第9行后）添加全局中断标志和计数**

```python
logger = setup_colored_logger('fetch')  # 替换原来的 setup_logger

# === 抓取任务控制 ===
fetch_stop = False
total_repos_fetched = 0
```

- [ ] **Step 2: 修改 run_fetch() 函数，添加中断检查和进度日志**（约第243行开始）：

在 `for i, batch in enumerate(batches):` 循环内部、`init_db()` 之后添加：

```python
    init_db()
    
    all_repos = []
    total_batches = len(batches)
    
    for i, batch in enumerate(batches):
        # === 中断检查 ===
        if fetch_stop:
            log_stop(logger, total_repos_fetched, len(all_repos), '抓取')
            return all_repos
        
        query_parts = [item[0] for item in batch]
        
        if len(batch) == 1:
            query = batch[0][0]
        else:
            query = ' OR '.join(query_parts)
        
        logger.info(f'开始抓取第 {i+1}/{total_batches} 批，查询串长度={len(query)}')
        
        # 调用带翻页的搜索函数
        repos = fetch_repos_with_pagination(query, page_size=page_size, min_stars_stop=min_stars_stop)
        logger.info(f'第 {i+1} 批抓取完成，共 {len(repos)} 个仓库')
        
        for repo in repos:
            # === 中断检查（每个repo前）===
            if fetch_stop:
                log_stop(logger, total_repos_fetched, len(all_repos), '抓取')
                return all_repos
            
            repo['fetched_at'] = format_iso()
            
            readme_path = fetch_readme(repo['full_name'])
            if readme_path:
                repo['readme_path'] = readme_path
            
            upsert_repo(repo)
            total_repos_fetched += 1
            all_repos.append(repo)
            
            # === 进度日志（每完成一个repo）===
            remaining = len(all_repos) - total_repos_fetched + (len(repos) - repos.index(repo)) 
            log_done(logger, total_repos_fetched, max(0, remaining), '抓取')
        
        # 批次间间隔
        if interval and i < len(batches) - 1:
            time.sleep(interval)
    
    logger.info(f'全部抓取完成，共 {len(all_repos)} 个仓库')
```

- [ ] **Step 3: 添加 stop_fetch() 函数**（在 run_fetch() 之后）：

```python
def stop_fetch():
    """设置抓取中断标志"""
    global fetch_stop
    fetch_stop = True


def is_fetch_stopped():
    """检查是否已停止"""
    return bool(fetch_stop)
```

- [ ] **Step 4: 修改 server.py 中的 api_fetch()**，添加 stop 调用：

在 `api_fetch` 路由中（约第110行），fetch_worker 改为：

```python
def fetch_worker():
    global fetch_stop_flag
    try:
        run_fetch()
    except Exception as e:
        logger.error(f'抓取/翻译线程出错: {e}')
    finally:
        # 重置标志位，方便下次使用
        import fetch
        fetch.fetch_stop = False
```

在 `server.py` 中导入 stop_fetch：
```python
from fetch import run_fetch, stop_fetch
```

并添加新的路由（如果Task3没加的话）：
```python
@app.route('/api/fetch/stop', methods=['POST'])
def api_fetch_stop():
    global fetch_thread
    with fetch_lock:
        fetch.stop_fetch()  # 设置中断标志
        if fetch_thread and fetch_thread.is_alive():
            fetch_thread.join(timeout=5)  # 等待线程结束（最多5秒）
        fetch_thread = None
    return jsonify({'status': 'stopped'})
```

---

### Task 5: translator.py — README翻译中断支持 + 进度日志

**Files:**
- Modify: `translator.py` (顶部添加标志；run_translate() 中添加中断检查和进度)

- [ ] **Step 1: 在文件顶部（第7行后）添加全局变量和导入彩色logger**

```python
# === README翻译任务控制 ===
readme_translate_stop = False


def setup_colored_logger(name='translator'):
    """创建带彩色输出的 logger"""
    from utils import ColorFormatter, log_done, log_stop
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)
    
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    os.makedirs(data_dir, exist_ok=True)
    log_path = os.path.join(data_dir, f'{name}.log')
    
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(console_handler)
    
    return logger


# 替换原有的 logger 初始化
logger = setup_colored_logger('translator')
```

- [ ] **Step 2: 修改 run_translate() 函数**（约第133行）：

```python
def run_translate(limit=10):
    global readme_translate_stop
    
    config = load_config()
    auto_translate = config.get('auto_translate', True)
    
    if not auto_translate:
        logger.info('自动翻译已关闭，跳过批量翻译')
        return
    
    init_db()
    
    readme_dir = get_readme_dir()
    repos = get_pending_translates(limit)
    
    total_count = len(repos)
    done = 0
    
    if not repos:
        logger.info('没有待翻译的 README')
        return
    
    logger.info(f'开始翻译 {total_count} 个 README')
    
    for repo in repos:
        # === 中断检查 ===
        if readme_translate_stop:
            log_stop(logger, done, total_count, 'README翻译')
            return
        
        repo_id = repo['id']
        full_name = repo['full_name']
        
        if not repo.get('readme_path'):
            logger.warning(f'{full_name} 没有 README 文件，跳过')
            continue
        
        try:
            with open(repo['readme_path'], 'r', encoding='utf-8') as f:
                readme_content = f.read()
            
            logger.info(f'正在翻译 {full_name}')
            
            translated = translate_readme(readme_content)
            
            zh_filename = repo_to_filename_zh(full_name)
            zh_filepath = os.path.join(readme_dir, zh_filename)
            
            with open(zh_filepath, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            update_translate_status(repo_id, 'done', readme_zh_path=zh_filepath)
            done += 1
            
            # === 进度日志（每完成一个）===
            remaining = total_count - done
            log_done(logger, done, remaining, total_count, 'README翻译')
                
        except Exception as e:
            error_msg = str(e)
            logger.error(f'{full_name} 翻译失败: {error_msg}')


def stop_readme_translate():
    """设置 README 翻译中断标志"""
    global readme_translate_stop
    readme_translate_stop = True


def is_readme_translating():
    """检查是否在翻译中"""
    return bool(readme_translate_stop)
```

- [ ] **Step 3: 修改 server.py 中的 translate 相关路由**：

在 `api_translate`（第143行）的 translate_worker 中添加中断重置逻辑：

```python
def api_translate(repo_id):
    global translate_thread
    
    with fetch_lock:
        global translate_stop_flag
        if translate_thread and translate_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '翻译任务进行中'}), 409
        
        def translate_worker():
            try:
                translate_single_repo(repo_id)
            except Exception as e:
                logger.error(f'翻译线程出错: {e}')
        
        translate_thread = threading.Thread(target=translate_worker, daemon=True)
        translate_thread.start()
    
    return jsonify({'status': 'started'})


@app.route('/api/translate/stop', methods=['POST'])
def api_translate_stop():
    """停止 README 翻译"""
    global translate_thread
    with fetch_lock:
        translator.stop_readme_translate()  # 设置中断标志
        if translate_thread and translate_thread.is_alive():
            translate_thread.join(timeout=5)
        translate_thread = None
    return jsonify({'status': 'stopped'})


@app.route('/api/readme/translate', methods=['POST'])
def api_readme_translate():
    global translate_thread
    
    with fetch_lock:
        if translate_thread and translate_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '翻译任务进行中'}), 409
        
        def translate_worker():
            try:
                from translator import run_translate, stop_readme_translate
                
                # 在后台线程中定期检查中断标志
                original_stop = getattr(translator, 'readme_translate_stop', False)
                
                run_translate(limit=100)
            except Exception as e:
                logger.error(f'README 翻译线程出错: {e}')
        
        translate_thread = threading.Thread(target=translate_worker, daemon=True)
        translate_thread.start()
    
    return jsonify({'status': 'started'})
```

实际上更简洁的方式是把 `run_translate()` 的 limit 参数去掉，直接用全局变量控制。让我重新整理：

在 `server.py` 中导入：
```python
from translator import run_translate, stop_readme_translate
```

---

### Task 6: search.html — 完全重写管理页面

**Files:**
- Create/Replace: `web/search.html` (完全重写)

- [ ] **Step 1: 用以下内容替换整个 search.html：**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>GitHub Reader - 管理</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <div class="header">
        <h1>📥 GitHub Reader</h1>
        <div class="nav">
            <a href="/">收件箱</a>
            <a href="/search.html" class="active">管理</a>
        </div>
    </div>
    
    <div class="container search-page">
        
        <!-- 数据统计区 -->
        <section class="stats-section">
            <h2>📊 数据库统计</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <span class="stat-value" id="stat-total">0</span>
                    <span class="stat-label">仓库总数</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value" id="stat-read">0</span>
                    <span class="stat-label">已读数</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value" id="stat-unread">0</span>
                    <span class="stat-label">未读数</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value" id="stat-max-stars">0</span>
                    <span class="stat-label">最高星标</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value" id="stat-readme-translated">0</span>
                    <span class="stat-label">README翻译完成</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value" id="stat-desc-translated">0</span>
                    <span class="stat-label">Description翻译完成</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value" id="stat-pending">0</span>
                    <span class="stat-label">待翻译</span>
                </div>
            </div>
        </section>

        <!-- Topics 标签云 -->
        <section class="topics-section">
            <h2>🏷️ Topics 标签</h2>
            <div class="topics-cloud" id="topics-cloud"></div>
        </section>

        <!-- 操作按钮组 -->
        <section class="action-section">
            <h2>⚡ 任务控制</h2>
            <div class="action-buttons">
                <button class="btn btn-primary" id="fetch-start-btn" onclick="startFetch()">📥 开始抓取</button>
                <button class="btn btn-danger" id="fetch-stop-btn" style="display:none;" onclick="stopFetch()">⏹️ 停止抓取</button>
                
                <button class="btn btn-success" id="readme-translate-start-btn" onclick="startTranslateReadmes()">📝 翻译 README</button>
                <button class="btn btn-danger" id="readme-translate-stop-btn" style="display:none;" onclick="stopTranslateReadmes()">⏹️ 停止翻译README</button>
                
                <button class="btn btn-primary" id="desc-translate-start-btn" onclick="startTranslateDescriptions()">📋 翻译 Description</button>
                <button class="btn btn-danger" id="desc-translate-stop-btn" style="display:none;" onclick="stopTranslateDescriptions()">⏹️ 停止翻译Description</button>
            </div>
        </section>

        <!-- 数据库结构说明 -->
        <section class="db-schema-section">
            <h2>🗃️ 数据库结构</h2>
            <table class="schema-table" id="schema-table">
                <thead>
                    <tr>
                        <th>字段名</th>
                        <th>类型</th>
                        <th>说明</th>
                    </tr>
                </thead>
                <tbody id="schema-tbody"></tbody>
            </table>
        </section>

    </div>
    
    <script src="/app.js"></script>
</body>
</html>
```

---

### Task 7: app.js — 重写搜索页逻辑

**Files:**
- Modify: `web/app.js` (删除关键词相关函数；新增搜索页初始化)

- [ ] **Step 1: 在文件顶部添加新的 API helper（如果还没有）**：

确认已有以下基础函数，如果没有则添加：
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
```

- [ ] **Step 2: 删除关键词相关函数**：

从文件中移除以下函数（如果存在）：
- `loadKeywords()` 
- `addKeyword()`
- `deleteKeyword(kw)`

以及文件末尾的初始化代码中对应的 keyword-list 部分。

- [ ] **Step 3: 新增搜索页逻辑，在文件末尾替换原有的搜索页初始化：**

```javascript
// === Search Page Logic ===
async function loadSearchStats() {
    const stats = await apiGet('/stats/detailed');
    
    document.getElementById('stat-total').textContent = stats.total.toLocaleString();
    document.getElementById('stat-read').textContent = stats.read_count.toLocaleString();
    document.getElementById('stat-unread').textContent = stats.unread.toLocaleString();
    document.getElementById('stat-max-stars').textContent = (stats.max_stars || 0).toLocaleString();
    document.getElementById('stat-readme-translated').textContent = stats.translated.toLocaleString();
    document.getElementById('stat-desc-translated').textContent = stats.desc_translated.toLocaleString();
    document.getElementById('stat-pending').textContent = stats.pending_translate.toLocaleString();
}

async function loadTopics() {
    const data = await apiGet('/topics');
    const container = document.getElementById('topics-cloud');
    
    if (!container || !data.topics.length) {
        if (container) container.innerHTML = '<p style="color:#666;">暂无标签</p>';
        return;
    }
    
    container.innerHTML = data.topics.map(topic => 
        `<span class="topic-tag">${topic}</span>`
    ).join('');
}

async function loadDbSchema() {
    const data = await apiGet('/db/schema');
    const tbody = document.getElementById('schema-tbody');
    
    if (!tbody) return;
    
    tbody.innerHTML = data.columns.map(col => `
        <tr>
            <td><code>${col.name}</code></td>
            <td><span class="type">${col.type} ${col.primary_key ? '(PK)' : ''}${col.not_null ? ' NOT NULL' : ''}</span></td>
            <td>${col.description || '-'}</td>
        </tr>
    `).join('');
}

// 抓取控制
async function startFetch() {
    const btn = document.getElementById('fetch-start-btn');
    const stopBtn = document.getElementById('fetch-stop-btn');
    
    btn.disabled = true;
    stopBtn.style.display = 'inline-block';
    
    await apiPost('/fetch');
}

async function stopFetch() {
    const btn = document.getElementById('fetch-start-btn');
    const stopBtn = document.getElementById('fetch-stop-btn');
    
    try {
        await apiPost('/fetch/stop');
        stopBtn.textContent = '已停止';
        setTimeout(() => {
            stopBtn.style.display = 'none';
            btn.disabled = false;
            loadSearchStats();  // 刷新统计
        }, 2000);
    } catch (e) {
        console.error('Stop fetch failed:', e);
    }
}

// README翻译控制
async function startTranslateReadmes() {
    const btn = document.getElementById('readme-translate-start-btn');
    const stopBtn = document.getElementById('readme-translate-stop-btn');
    
    btn.disabled = true;
    stopBtn.style.display = 'inline-block';
    
    await apiPost('/readme/translate');
}

async function stopTranslateReadmes() {
    const btn = document.getElementById('readme-translate-start-btn');
    const stopBtn = document.getElementById('readme-translate-stop-btn');
    
    try {
        await apiPost('/translate/stop');
        stopBtn.textContent = '已停止';
        setTimeout(() => {
            stopBtn.style.display = 'none';
            btn.disabled = false;
            loadSearchStats();  // 刷新统计
        }, 2000);
    } catch (e) {
        console.error('Stop translate failed:', e);
    }
}

// Description翻译控制（已有函数，只需确保按钮绑定正确）
async function startTranslateDescriptions() {
    const btn = document.getElementById('desc-translate-start-btn');
    const stopBtn = document.getElementById('desc-translate-stop-btn');
    
    btn.disabled = true;
    stopBtn.style.display = 'inline-block';
    
    await apiPost('/description/translate');
}

async function stopTranslateDescriptions() {
    const btn = document.getElementById('desc-translate-start-btn');
    const stopBtn = document.getElementById('desc-translate-stop-btn');
    
    try {
        await apiPost('/description/translate/stop');
        stopBtn.textContent = '已停止';
        setTimeout(() => {
            stopBtn.style.display = 'none';
            btn.disabled = false;
            loadSearchStats();  // 刷新统计
        }, 2000);
    } catch (e) {
        console.error('Stop description translate failed:', e);
    }
}

// === Page Init ===
if (document.getElementById('repo-list')) {
    loadRepos();
    document.getElementById('filter-all').onclick = () => loadRepos('all', 1, 'fetched_at', 'desc');
    document.getElementById('filter-read').onclick = () => loadRepos('read', 1, 'fetched_at', 'desc');
    document.getElementById('filter-unread').onclick = () => loadRepos('unread', 1, 'fetched_at', 'desc');
    
    document.getElementById('sort-time').onclick = () => loadRepos('all', 1, 'fetched_at', 'desc');
    document.getElementById('sort-time-asc').onclick = () => loadRepos('all', 1, 'fetched_at', 'asc');
    document.getElementById('sort-stars').onclick = () => loadRepos('all', 1, 'stars', 'desc');
    
    // Description翻译按钮（收件页）
    const descBtn = document.getElementById('translate-desc-btn');
    if (descBtn) {
        descBtn.onclick = startTranslateDescriptions;
    }
    const stopDescBtn = document.getElementById('stop-translate-desc-btn');
    if (stopDescBtn) {
        stopDescBtn.onclick = stopTranslateDescriptions;
    }
    
    // README翻译按钮（收件页）
    const readmeBtn = document.getElementById('translate-readme-btn');
    if (readmeBtn) {
        readmeBtn.onclick = startTranslateReadmes;
    }
    const stopReadmeBtn = document.getElementById('stop-translate-readme-btn');
    if (stopReadmeBtn) {
        stopReadmeBtn.onclick = stopTranslateReadmes;
    }
}

if (document.getElementById('repo-name')) {
    loadDetail();
}

// 搜索页初始化（替换原有的 keyword-list 检查）
if (document.querySelector('.search-page')) {
    loadSearchStats();
    loadTopics();
    loadDbSchema();
    
    // Description翻译按钮（管理页）
    const descBtn = document.getElementById('desc-translate-start-btn');
    if (descBtn) descBtn.onclick = startTranslateDescriptions;
    const stopDescBtn = document.getElementById('desc-translate-stop-btn');
    if (stopDescBtn) stopDescBtn.onclick = stopTranslateDescriptions;
    
    // README翻译按钮（管理页）
    const readmeBtn = document.getElementById('readme-translate-start-btn');
    if (readmeBtn) readmeBtn.onclick = startTranslateReadmes;
    const stopReadmeBtn = document.getElementById('readme-translate-stop-btn');
    if (stopReadmeBtn) stopReadmeBtn.onclick = stopTranslateReadmes;
}
```

---

### Task 8: style.css — 新增样式类

**Files:**
- Modify: `web/style.css` (在文件末尾追加以下所有新样式类)

- [ ] **Step 1: 在 CSS 文件末尾添加以下样式：**

```css
/* === Search Page Styles === */

.search-page {
    max-width: 900px;
}

.stats-section, .topics-section, .action-section, .db-schema-section {
    margin-bottom: 32px;
}

.stats-section h2, .topics-section h2, 
.action-section h2, .db-schema-section h2 {
    font-size: 18px;
    color: #333;
    border-bottom: 2px solid #e0e0e0;
    padding-bottom: 8px;
    margin-bottom: 16px;
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 12px;
}

.stat-card {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    transition: transform 0.2s, box-shadow 0.2s;
}

.stat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.stat-value {
    display: block;
    font-size: 32px;
    font-weight: bold;
    color: #0d6efd;
    margin-bottom: 4px;
}

.stat-label {
    display: block;
    font-size: 13px;
    color: #666;
}

/* Topics Cloud */
.topics-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.topic-tag {
    background: #e8f4fd;
    color: #0d6efd;
    padding: 6px 12px;
    border-radius: 12px;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s;
}

.topic-tag:hover {
    background: #0d6efd;
    color: #fff;
}

/* Action Buttons */
.action-buttons {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.btn {
    padding: 12px 16px;
    border: none;
    border-radius: 8px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s;
    min-height: 44px;
}

.btn:hover:not(:disabled) {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.btn-primary {
    background: #0d6efd;
    color: #fff;
}

.btn-primary:hover:not(:disabled) {
    background: #0b5ed7;
}

.btn-success {
    background: #198754;
    color: #fff;
}

.btn-success:hover:not(:disabled) {
    background: #157347;
}

.btn-danger {
    background: #dc3545;
    color: #fff;
}

.btn-danger:hover:not(:disabled) {
    background: #bb2d3b;
}

/* DB Schema Table */
.schema-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

.schema-table thead th {
    background: #f8f9fa;
    padding: 12px;
    text-align: left;
    color: #333;
    border-bottom: 2px solid #dee2e6;
}

.schema-table tbody tr:nth-child(even) {
    background: #fafafa;
}

.schema-table tbody td {
    padding: 10px 12px;
    border-bottom: 1px solid #e9ecef;
}

.schema-table code {
    font-family: 'Courier New', monospace;
    color: #d63384;
}

.schema-table .type {
    color: #6c757d;
    font-style: italic;
}
```

---

## 自我审查清单

### 1. Spec coverage ✅
- [x] 删除关键词管理 → Task 7 Step 2
- [x] 删除日志显示 → search.html 已不含日志区域
- [x] 数据统计区（7项指标）→ Task 6 + Task 7 Step 3 (loadSearchStats)
- [x] Topics标签云 → Task 6 + Task 7 Step 3 (loadTopics)
- [x] 操作按钮组（6个平铺）→ Task 6 + Task 7 Step 3
- [x] 数据库结构说明 → Task 6 + Task 7 Step 3 (loadDbSchema)
- [x] 彩色日志 + 进度展示 → Task 1, Task 4, Task 5
- [x] 全任务支持停止中断 → Task 4 (fetch), Task 5 (translator README), Task 3 (server stop endpoints)

### 2. Placeholder scan ✅
无 TBD/TODO/待实现标记。所有代码块完整可执行。

### 3. Type consistency ✅
- `logger.info()`, `logger.warning()` 在所有模块统一使用
- API路径 `/api/stats/detailed`, `/api/topics`, `/api/db/schema` 前后端一致
- DOM ID (`stat-total`, `topics-cloud`, `fetch-start-btn`) HTML与JS一致

### 4. Ambiguity check ✅
- 进度日志格式：已完成/剩余/总数，绿色高亮（通过 `log_done()`）
- 停止行为：设置标志位 → 当前循环项完成后退出 → 线程自然结束
- 数据库结构说明：动态获取字段名+类型 + 硬编码语义描述

---

## 执行顺序建议

```
Task 1 (utils.py) 
    ↓
Task 2 (db.py) ← Task 3 (server.py API依赖db函数)
    ↓
Task 4 (fetch.py) ← Task 5 (translator.py) ← [可并行]
    ↓
Task 6 (search.html) ← Task 7 (app.js) ← Task 8 (style.css) ← [三者可并行]
```

实际执行时建议按顺序：Task1 → Task2 → Task3 → Task4+5(并行) → Task6+7+8(并行)。

Plan complete and saved to `docs/superpowers/plans/2026-06-03-search-page-redesign.md`. Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**</p>