# GitHub Reader 管理页面改造设计

## 项目概述

重新设计 `search.html`（管理页），删除关键词管理和日志显示功能，改为数据统计 + 操作控制 + 数据库结构说明的布局。同时增强后端：彩色日志、进度展示、全任务支持停止中断。

---

## 一、前端改造

### 1.1 search.html 页面重构

**删除内容：**
- 关键词输入框和删除按钮（`#keyword-input`, `#keyword-list`）
- 日志显示区域（`#log-container`, `#log-title`, `#log-content`）
- 相关API调用：`addKeyword()`, `deleteKeyword()`

**新增布局结构：**

```html
<div class="search-page">
    <!-- 数据统计区 -->
    <div class="stats-section">...</div>
    
    <!-- Topics标签云 -->
    <div class="topics-cloud">...</div>
    
    <!-- 操作按钮组（6个平铺） -->
    <div class="action-buttons">...</div>
    
    <!-- 数据库结构说明 -->
    <div class="db-schema-section">...</div>
</div>
```

### 1.2 数据统计区

展示7项指标，分两行排列：

| 第一行 | 仓库总数 | 已读数 | 未读数 | 最高星标 |
|--------|---------|-------|-------|---------|
| 第二行 | README翻译完成数 | Description翻译完成数 | 待翻译数 |

每个指标卡片样式：白色背景 + 圆角 + 浅灰边框，数值加粗大字体（24px），标签小字灰色。

### 1.3 Topics标签云

- 从 `GET /api/topics` 接口获取所有不重复的topics
- 展示为可点击的标签列表，每个标签带背景色和圆角
- 点击某个topic时跳转到收件页并筛选该topic（可选功能）

### 1.4 操作按钮组

6个按钮平铺一行，分两组样式：

| 类型 | 按钮 | 颜色 | 对应API |
|------|------|------|---------|
| 抓取 | [开始抓取] | #0d6efd (蓝) | POST /api/fetch |
| 抓取 | [停止抓取] | #dc3545 (红,隐藏) | POST /api/fetch/stop |
| README翻译 | [翻译README] | #198754 (绿) | POST /api/readme/translate |
| README翻译 | [停止翻译README] | #dc3545 (红,隐藏) | POST /api/translate/stop |
| Description翻译 | [翻译Description] | #0d6efd (蓝) | POST /api/description/translate |
| Description翻译 | [停止...] | #dc3545 (红,hidden) | POST /api/description/translate/stop |

按钮样式：padding 8px 16px，圆角6px，hover效果。运行中时显示隐藏对应停止按钮并禁用开始按钮。

### 1.5 数据库结构说明区

以可折叠面板展示 `repositories` 表的每个字段：
- 每行：`字段名` (类型, 必填/可选) — 用途说明
- 示例值用代码块显示

---

## 二、后端API改造

### 2.1 新增接口

| Method | Path | 返回内容 |
|--------|------|---------|
| GET | `/api/stats/detailed` | `{ total, read_count, unread_count, max_stars, readme_translated, desc_translated, pending_translate }` |
| GET | `/api/topics` | `[topic1, topic2, ...]` 所有不重复的topics列表 |
| GET | `/api/db/schema` | `[{ table: 'repositories', columns: [{ name, type, not_null, description }] }]` |
| POST | `/api/fetch/stop` | `{ status: 'stopped' }` — 停止抓取任务 |

### 2.2 server.py 改动

- 新增上述4个API路由
- `fetch_stop_thread` 全局变量替代现有的简单 `None` 判断，支持真正的中断信号传递

---

## 三、日志系统改造

### 3.1 utils.py — 彩色Logger扩展

```python
class ColorFormatter(logging.Formatter):
    COLORS = {
        'INFO': '\033[92m',      # 绿色 - 成功/正常
        'WARNING': '\033[93m',   # 黄色 - 警告
        'ERROR': '\033[91m',     # 红色 - 错误
        'PROGRESS': '\033[94m',  # 蓝色 - 进度信息（自定义级别）
    }
    
    def format(self, record):
        if record.levelname in self.COLORS:
            color = self.COLORS[record.levelname]
            msg = super().format(record)
            return f"{color}{msg}\033[0m"  # ANSI重置码
        return super().format(record)
```

**进度日志格式（重要）：**每次完成一项操作后换行输出：
```
✅ [已完成: 15/42 | 剩余: 27 | 总数: 42]
```

### 3.2 fetch.py — 抓取进度 + 中断支持

```python
# 全局中断标志
fetch_stop = False

def run_fetch():
    global fetch_stop, total_repos_fetched
    
    init_db()
    
    # ... 分批循环 ...
    for repo in repos:
        if fetch_stop:
            logger.info(f'抓取被中断，已完成 {total_repos_fetched}/{len(all_repos)}')
            return all_repos
        
        readme_path = fetch_readme(repo['full_name'])
        upsert_repo(repo)
        
        # 进度日志（重要）
        total_repos_fetched += 1
        logger.progress(f'[{total_repos_fetched}/{len(all_repos)}] {repo["full_name"]} README {"已保存" if readme_path else "无"}')
    
    return all_repos

def stop_fetch():
    global fetch_stop
    fetch_stop = True
```

### 3.3 translator.py — README翻译中断支持

```python
# 已有 description_translate_stop，补充：
readme_translate_stop = False

def run_translate(limit=10):
    # ... existing code ...
    
    for repo in repos:
        if readme_translate_stop:
            logger.info(f'README翻译被中断，已完成 {done}/{len(repos)}')
            break
        
        # 翻译逻辑...
        
        done += 1
        logger.progress(f'[已翻译: {done}/{len(repos)} | 剩余: {len(repos) - done}] {repo["full_name"]}')

def stop_readme_translate():
    global readme_translate_stop
    readme_translate_stop = True
```

---

## 四、数据库结构说明数据源

`/api/db/schema` 通过查询 SQLite 的 `PRAGMA table_info(repositories)` 获取：

```python
@app.route('/api/db/schema')
def api_db_schema():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.execute('PRAGMA table_info(repositories)')
    columns = [{'name': row[1], 'type': row[2], 'not_null': bool(row[3])} for row in cursor.fetchall()]
    
    # 添加字段说明（硬编码映射，因为schema不包含语义信息）
    descriptions = {
        'id': '自增主键',
        'full_name': '仓库全称 (owner/repo)',
        'description': '仓库描述文字',
        ...
    }
    
    conn.close()
    return jsonify({'table': 'repositories', 'columns': columns, 'descriptions': descriptions})
```

---

## 五、CSS样式增强

### 5.1 stats-section（统计区）
- Grid布局：4列 × 2行
- 每个卡片：白色背景 `#fff`，圆角8px，内边距16px，浅灰边框 `#e0e0e0`
- 数值：字体32px，加粗，颜色 `#0d6efd`（主题蓝）

### 5.2 topics-cloud（标签云）
- Flex-wrap布局，自动换行
- 每个标签：背景色 `#e8f4fd`，圆角12px，padding 6px 12px，字号13px

### 5.3 action-buttons（操作按钮组）
- Grid布局：3列 × 2行
- 蓝色按钮：`#0d6efd`，hover `#0b5ed7`
- 红色停止按钮：`#dc3545`，hover `#bb2d3b`

### 5.4 db-schema-section（数据库结构）
- 表格样式：表头背景 `#f8f9fa`，斑马纹行，圆角6px
- 字段名等宽字体，类型用斜体灰色显示

---

## 六、文件改动清单

| 文件 | 改动内容 |
|------|---------|
| `web/search.html` | **完全重写**：删除关键词/日志区块，新增统计+按钮+数据库结构区 |
| `web/app.js` | 重写搜索页逻辑：加载统计数据、topics、操作按钮事件；删除关键词相关函数 |
| `web/style.css` | 新增 `.stats-section`, `.topics-cloud`, `.action-buttons`, `.db-schema-section` 样式类 |
| `server.py` | 新增4个API路由（detailed stats, topics, db schema, fetch stop）+ 停止线程管理 |
| `db.py` | 扩展 `get_stats()` 返回更多指标；新增 `get_all_topics()`, `get_db_schema()` |
| `utils.py` | 新增 `ColorFormatter` 类，支持ANSI彩色输出 + PROGRESS级别 |
| `fetch.py` | 新增 `fetch_stop` 全局变量 + 中断检查 + 进度日志 |
| `translator.py` | 新增 `readme_translate_stop` 全局变量 + 中断检查 + 进度日志 |

---

## 七、技术决策

1. **停止机制**：采用"当前任务完成后退出"策略，而非强制终止线程。这样不会丢失数据，且实现简单可靠。
2. **数据库结构说明**：通过 `PRAGMA table_info()` 动态获取字段信息 + 硬编码语义描述（因为SQLite schema不包含注释）。
3. **彩色日志**：仅终端输出使用ANSI颜色，文件日志保持纯文本格式（避免日志分析工具解析失败）。
4. **Topics数据源**：从现有 `topics` JSON数组中提取去重值，无需新增数据库字段。
