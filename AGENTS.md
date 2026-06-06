# AGENTS.md

## 项目概述

**GitHub Reader** — 通过关键词订阅 GitHub 热门仓库，自动抓取 README 并翻译为中文，以收件箱形式管理阅读进度。

- **目标用户**：开发者本人（单用户本地工具）
- **核心价值**：本地化、自动化、中文阅读体验

## 技术栈

| 层 | 技术 |
|----|------|
| 后端 | Python 3.x + Flask |
| 数据库 | SQLite（标准库 sqlite3，WAL 模式） |
| HTTP 客户端 | requests |
| Markdown 渲染 | marked.js（CDN）+ DOMPurify（CDN） |
| 翻译引擎 | llama.cpp server（OpenAI 兼容接口） + Qwen3.6-35B-A3B |
| 前端 | 原生 HTML + CSS + JS（无框架，无构建工具） |

## 项目结构

```
github-reader/
├── config.json              # 运行时配置（GitHub Token、关键词参数、翻译服务设置等）
├── keywords.json            # 关键词列表（独立于 config.json）
├── config.py                # 配置读取 + 路径工具函数
├── server.py                # Flask Web 服务入口 + REST API
├── fetch.py                 # GitHub 数据抓取模块
├── translator.py            # LLM 翻译模块
├── db.py                    # SQLite 数据库操作层（建表/迁移/CRUD）
├── utils.py                 # 通用工具（日志、路径转换、彩色终端输出）
├── clear.py                 # 数据清理工具（低星标仓库删除）
├── public/                  # Public Viewer（半独立公开模块，纯静态部署）
├── data/
│   ├── db.sqlite            # SQLite 数据库文件
│   └── readme/              # README 原始文件和中文译文存储目录
│       └── {owner}__{repo}.md / {owner}__{repo}_zh.md
└── web/                     # 前端静态资源（由 Flask static_folder 直接托管）
    ├── index.html           # 收件箱列表页
    ├── detail.html          # README 详情页
    ├── search.html          # 管理控制台页
    ├── style.css            # 全局样式
    └── app.js               # 前端 JS 逻辑（API 封装 + 三页面交互）
```

## 文件说明

### 后端 Python 模块

#### `config.py` — 配置读取与路径工具

| 函数 | 说明 |
|------|------|
| `load_config()` | 加载 `config.json`，返回配置字典 |
| `get_data_dir()` | 返回 `data/` 目录绝对路径 |
| `get_readme_dir()` | 返回 `data/readme/` 目录（自动创建） |
| `get_db_path()` | 返回 `data/db.sqlite` 路径（自动创建 data 目录） |
| `load_keywords()` | 从 `keywords.json` 加载关键词 key 数组 |

#### `server.py` — Flask Web 服务 + REST API

**三类路由：**

1. **HTML 页面路由**：`/` → index.html、`/detail.html`、`/search.html`
2. **RESTful API 路由**（详见下方 API 接口表）
3. **异步任务管理**：抓取和翻译通过 `threading.Thread(daemon=True)` 执行，使用全局锁 `fetch_lock` 保证线程安全

**核心辅助函数：**
- `make_relative_path(abs_path)` — 将数据库中的绝对路径转换为相对文件名（前端可访问）

#### `fetch.py` — GitHub 数据抓取模块

| 函数 | 说明 |
|------|------|
| `search_repos(keyword, top_n)` | 调用 GitHub Search API，按关键词搜索热门仓库（返回去重后的 repo 列表） |
| `fetch_readme(full_name)` | 通过 GitHub API 获取 README 内容（base64 解码），自动尝试默认分支 → main/master/develop fallback，保存到本地 `data/readme/{owner}__{repo}.md` |
| `fetch_repos_with_pagination(query, page_size, min_stars_stop)` | 分页搜索：按 stars 降序翻页，遇到任意仓库 stars < min_stars_stop 时提前停止 |
| `build_keyword_batches(keywords, max_q_length)` | 将关键词分批（每批用 OR 拼接），遵守 GitHub Search API q 参数长度限制（≤100）和操作符数量限制（最多 6 个关键词/批） |
| `run_fetch()` | 主流程：加载关键词 → 分批构建查询串 → 逐批搜索 + 获取 README → upsert_repo() 入库。支持中断标志 `fetch_stop`，每批/每个 repo 前检查 |

**抓取策略要点：**
- 增量模式（`update_all=false`）：跳过已有 README 文件的仓库
- 任务级去重：全局 `processed_repos: set[str]`，同一批次内不重复处理
- 分支回退：先获取默认分支 → fallback main/master/develop

#### `translator.py` — LLM 翻译模块

| 函数 | 说明 |
|------|------|
| `call_llm(text, max_retries=3)` | 调用本地 llama.cpp server（OpenAI 兼容 `/v1/chat/completions`），支持 3 次重试 + 指数退避，自动检测推理模型使用 reasoning_content |
| `translate_readme(text)` | 封装 README 翻译请求，使用预定义 `TRANSLATE_PROMPT` 提示词 |
| `translate_description(description)` | 封装 Description 翻译请求（复用 TRANSLATE_PROMPT） |
| `translate_single_repo(repo_id)` | 单仓库翻译流程：读取本地 README → LLM 调用 → 保存 `_zh.md` → 更新数据库状态 |
| `run_translate(limit, force=False)` | 批量 README 翻译：按 `translate_status='pending'` + stars DESC 查询，逐条翻译。支持中断标志 `readme_translate_stop` |
| `translate_description_single(repo_id)` | 单条 Description 翻译 |
| `run_translate_descriptions()` | 批量 Description 翻译：按 `description_translate_status='pending'` + stars DESC 查询 |

**提示词设计（TRANSLATE_PROMPT）：**
- 中文内容 >80% 时直接返回原文，不做修改
- 保留产品名、命令行命令、配置字段名、代码块、技术术语缩写不翻译
- Markdown 格式结构不变，语言风格简洁自然

#### `db.py` — SQLite 数据库操作层

详见下方「数据库结构」章节。核心函数：

| 函数 | 说明 |
|------|------|
| `get_connection()` | 获取数据库连接（WAL 模式 + Row factory） |
| `init_db()` | 建表 + 自动迁移检测 + 路径迁移 |
| `upsert_repo(data)` | 幂等写入：`INSERT ON CONFLICT(full_name) DO UPDATE`，已存在仅更新 stars/description/language/topics/html_url/updated_at |
| `get_repos(filter, page, page_size, sort_by, sort_order)` | 分页查询 + JSON 字段自动解析（topics、keywords） |
| `get_repo(repo_id)` | 获取单条记录，JSON 字段自动解析 |
| `mark_read()` / `mark_unread()` | 切换 is_read 状态 |
| `update_translate_status()` | 更新翻译状态 + 可选同时更新 readme_zh_path |
| `get_pending_translates(limit)` | 查询待 README 翻译记录（translate_status='pending'，按 stars DESC） |
| `get_existing_readme_names()` | 返回已有 README 文件的仓库 full_name 集合 |
| `get_all_keywords()` | 使用 json_each() 提取所有关键词（去重排序） |
| `get_stats()` | 统计信息：总数/已读/未读/最高星标/README翻译进度/Description翻译进度 |
| `get_fetch_progress()` | 抓取进度统计 |

#### `utils.py` — 通用工具函数

| 函数/类 | 说明 |
|---------|------|
| `setup_logger(name)` | 创建日志记录器：文件输出（`data/{name}.log`）+ 终端彩色输出 |
| `format_iso(dt=None)` | ISO 8601 时间格式化 |
| `repo_to_filename(full_name)` | `owner/repo` → `{owner}__{repo}.md` |
| `repo_to_filename_zh(full_name)` | 追加 `_zh.md` 后缀 |
| `ColorFormatter` | ANSI 终端彩色日志（INFO=绿色、WARNING=黄色、ERROR=红色） |
| `log_done()` / `log_stop()` / `log_skip()` | 进度/中断/跳过的高亮日志输出 |

#### `clear.py` — 数据清理工具

- **用途**：删除 stars < `clear_limit_count`（默认 1800）的仓库记录及相关 README 文件
- **安全设计**：默认预览模式，需显式传入 `--execute` + 二次确认才执行删除
- **用法**：`python clear.py --execute`

### 前端模块

#### `web/index.html` — 收件箱列表页

- 顶部导航栏（收件箱 / 管理）
- 未读计数统计、筛选按钮组（全部/已读/未读）、排序按钮组（最新抓取/最早抓取/最多星标）
- 仓库列表容器、分页容器

#### `web/detail.html` — README 详情页

- 返回链接、仓库信息区（名称、描述、Description中文译文、星标、语言、GitHub 链接）
- 语言切换按钮（English / 中文，localStorage 持久化）
- 操作按钮组：翻译/重新翻译、标记已读/未读
- README Markdown 渲染内容区

#### `web/search.html` — 管理控制台页

- 数据统计卡片（总数/已读/未读/最高星标/README翻译完成&待翻译/Description翻译完成&待翻译）
- Topics 标签云（按频率动态调整字号和透明度，目标约 10 行展示）
- 任务控制按钮组：抓取 / Description翻译 / README翻译 + 对应的停止按钮
- 数据库结构说明表

#### `web/style.css` — 全局样式

- Flexbox 响应式布局
- 组件：列表项、详情页、按钮（filter-btn/fetch-btn）、分页、标签云等
- `.active` 类用于高亮选中状态，`.read` / `.unread` 区分已读/未读样式

#### `web/app.js` — 前端 JavaScript 逻辑

| 功能区域 | 核心函数 |
|----------|----------|
| API 封装 | `apiGet()`、`apiPost()` |
| Toast 通知 | `showToast()`、`showFetchToast()`、`showTranslateToast()`、`showStopToast()` |
| 列表页 | `loadRepos()`（分页+筛选+排序）、`updateActiveButtons()`、分页渲染（含省略号） |
| 详情页 | `loadDetail()`（加载仓库详情 + Description中文译文）、`loadReadme()`（marked.js 渲染 + DOMPurify  sanitization）、`switchLang()`、`startTranslate()`、`pollTranslateStatus()`、`toggleReadStatus()` |
| 管理页 | `loadSearchStats()`、`loadTopics()`（动态标签云尺寸计算）、`loadDbSchema()`、任务控制函数（`startFetch()` / `stopFetch()` / `startTranslateReadmes()` / `stopTranslateReadmes()` / `startTranslateDescriptions()` / `stopTranslateDescriptions()`） |
| 轮询通用 | `pollTaskUntilDone()` — 通用轮询直到任务完成，自动恢复按钮状态并刷新统计 |

#### `public/` — Public Viewer（半独立公开模块）

**定位**：依赖主项目生成的数据文件，纯静态页面部署到 GitHub Pages，无需后端服务。用于将抓取结果以只读形式对外分享。

```
public/
├── index.html          # 列表页
├── detail.html         # README 详情页  
├── style.css           # 独立样式（与 web/ 不共用）
├── app.js              # 前端逻辑
└── data/
    ├── repos.json      # 主项目导出的仓库数据（JSON 格式）
    └── readmes/        # README 文件目录（引用自 data/readme/）
```

**功能说明：**

| 页面 | 功能 |
|------|------|
| `index.html` | 仓库列表页，支持按抓取时间/星标数排序，本地 JSON 分页展示 |
| `detail.html` | README 详情页，侧边栏显示仓库信息 + Tab 切换中英文译文 |

**数据依赖：**
- 读取 `data/repos.json`（主项目生成）获取仓库元数据
- 读取 `data/readmes/{owner}__{repo}.md` / `_zh.md` 作为 README 原文/译文
- 详情页根据文件是否存在自动显示对应语言 Tab，仅有一种语言时禁用切换

---

### 配置文件

#### `config.json` — 运行时配置

```json
{
  "github_token": "ghp_xxx",           // GitHub API Token（提高速率限制）
  "keywords": ["vibe coding", ...],      // （已迁移到 keywords.json，保留兼容）
  "fetch_top_n": 20,                     // （已迁移，被 page_size 替代）
  "request_interval": 0.5,               // （已迁移，批次间隔由 fetch.py 内部逻辑控制）
  "auto_translate": false,               // 抓取后是否自动翻译 README（默认 false）
  "llama_cpp": {                         // llama.cpp server 配置
    "base_url": "http://localhost:9898", // OpenAI 兼容接口地址
    "model": "Qwen3.6-35B-A3B",          // 模型名称
    "max_tokens": 153600                  // 最大 token 数
  },
  "translate_chunk_size": 20000,         // （保留字段）
  "max_q_length": 100,                   // 每批关键词查询串最大长度
  "page_size": 80,                       // GitHub API per_page，单页抓取数量
  "min_stars_stop": 1800,                // stars 低于此值时停止翻页
  "clear_limit_count": 1800,             // clear.py 清理阈值（stars < 此值的仓库可被删除）
  "update_all": false                    // true=全量更新，false=增量模式（跳过已有 README 的仓库）
}
```

#### `keywords.json` — 关键词列表

独立于 config.json，格式：
```json
{
  "keywords": [
    {"key": "vibe coding", ...},
    {"key": "ai agent", ...}
  ]
}
```

---

## API 接口

### HTML 页面路由

| Path | 说明 |
|------|------|
| `/` | 收件箱列表页 |
| `/detail.html?id={id}` | README 详情页 |
| `/search.html` | 管理控制台页 |

### RESTful API

| Method | Path | 说明 |
|--------|------|------|
| GET | `/api/repos` | 获取仓库列表（参数：filter=all/read/unread, page, page_size=20, sort_by=fetched_at/stars, sort_order=desc/asc） |
| GET | `/api/repos/:id` | 获取单个仓库详情 |
| GET | `/api/repos/:id/readme` | 获取 README 原文（直接返回 .md 文件内容） |
| GET | `/api/repos/:id/readme_zh` | 获取 README 中文译文 |
| POST | `/api/repos/:id/read` | 标记已读 |
| POST | `/api/repos/:id/unread` | 标记未读 |
| POST | `/api/repos/:id/translate` | 手动触发单条 README 翻译 |
| GET | `/api/keywords` | 获取所有关键词列表（去重排序） |
| POST | `/api/fetch` | 触发抓取任务（异步，返回 started/busy） |
| GET | `/api/fetch/status` | 查询抓取进度（running + total/translating/pending） |
| POST | `/api/fetch/stop` | 停止正在进行的抓取任务 |
| GET | `/api/translate/status` | 查询 README 翻译状态（running） |
| POST | `/api/readme/translate` | 批量触发 README 翻译（异步，force=true） |
| POST | `/api/translate/stop` | 停止正在进行的 README 翻译 |
| GET | `/api/stats` | 获取基础统计信息 |
| GET | `/api/stats/detailed` | 获取详细统计数据（管理页用） |
| GET | `/api/topics` | 获取所有 topics 及频次统计 |
| GET | `/api/db/schema` | 获取数据库表结构信息 |
| POST | `/api/description/translate` | 批量触发 Description 翻译（异步） |
| GET | `/api/description/translate/status` | 查询 Description 翻译进度（running + total + done + current_repo） |
| POST | `/api/description/translate/stop` | 停止正在进行的 Description 翻译 |
| GET | `/api/logs?type={fetch\|translate}&lines=50` | 获取日志内容（最近 N 行，HTML 转义） |

---

## 数据库结构

### 表：repositories

```sql
CREATE TABLE repositories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT UNIQUE NOT NULL,       -- 仓库全称，如 "owner/repo"
    description TEXT,                      -- 仓库描述（英文原文）
    stars INTEGER DEFAULT 0,               -- 星标数量
    language TEXT,                         -- 编程语言
    topics TEXT,                           -- 话题标签，JSON 数组字符串
    html_url TEXT,                         -- GitHub 页面 URL
    readme_path TEXT,                      -- README 本地文件名（相对路径），如 "owner__repo.md"
    readme_zh_path TEXT,                   -- README 中文译文本地文件名，如 "owner__repo_zh.md"
    translate_status TEXT DEFAULT 'pending', -- 翻译状态：'pending' | 'done' | 'error'
    translate_error TEXT,                  -- 翻译错误信息（失败时记录）
    is_read INTEGER DEFAULT 0,             -- 是否已读：0=未读，1=已读
    keywords TEXT,                         -- 触发抓取的关键词，JSON 数组字符串
    fetched_at TEXT NOT NULL,              -- 抓取时间（ISO 8601）
    updated_at TEXT NOT NULL,              -- 最后更新时间（ISO 8601）
    description_zh TEXT,                   -- Description 中文译文
    description_translate_status TEXT DEFAULT 'pending'  -- Description 翻译状态：'pending' | 'done' | 'error'
);

-- 索引
CREATE INDEX idx_translate_status ON repositories(translate_status);
CREATE INDEX idx_is_read ON repositories(is_read);
```

### 字段详细说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | INTEGER PK | 自增主键 |
| `full_name` | TEXT UNIQUE NOT NULL | 仓库全称，格式 `{owner}/{repo}`，唯一约束 |
| `description` | TEXT | 仓库描述文字（英文原文） |
| `stars` | INTEGER DEFAULT 0 | 星标数量 |
| `language` | TEXT | 编程语言（可能为 null） |
| `topics` | TEXT | JSON 数组字符串，如 `["ai", "coding-agent"]`，null/空数组表示无标签 |
| `html_url` | TEXT | GitHub HTML 页面 URL |
| `readme_path` | TEXT | README 本地存储文件名（仅文件名，不含路径），格式 `{owner}__{repo}.md` |
| `readme_zh_path` | TEXT | README 中文译文本地文件名，格式 `{owner}__{repo}_zh.md` |
| `translate_status` | TEXT DEFAULT 'pending' | README 翻译状态：`'pending'`(待翻译) / `'done'`(已完成) / `'error'`(失败) |
| `translate_error` | TEXT | 翻译失败时的错误信息 |
| `is_read` | INTEGER DEFAULT 0 | 阅读状态：`0`=未读，`1`=已读 |
| `keywords` | TEXT | JSON 数组字符串，记录触发该仓库抓取的关键词 |
| `fetched_at` | TEXT NOT NULL | 抓取时间（ISO 8601 格式） |
| `updated_at` | TEXT NOT NULL | 最后更新时间（每次 upsert 时更新） |
| `description_zh` | TEXT | Description 中文译文（翻译完成后写入） |
| `description_translate_status` | TEXT DEFAULT 'pending' | Description 翻译状态：`'pending'` / `'done'` / `'error'` |

### 数据库迁移机制

- **启动时自动检测**：`init_db()` 检查新字段是否存在，缺失则执行"建新表 → 复制旧数据 → 删旧表 → 重命名"流程
- **路径迁移**：`migrate_paths()` 将历史绝对路径转换为纯文件名（不含 `/` 或 `\`）

---

## 常用命令

### 启动服务

```bash
# 启动 Web 服务（默认端口 5000，监听所有接口）
python server.py

# 手动触发抓取 + 翻译
python fetch.py

# 只抓取
python fetch.py --fetch-only

# 只翻译 README
python fetch.py --translate-only

# 临时添加关键词
python fetch.py --keyword "your keyword"
```

### 数据清理

```bash
# 预览模式（默认，仅显示即将删除的记录）
python clear.py

# 执行删除操作（需二次确认）
python clear.py --execute
```

### 访问地址

- Web 界面：`http://localhost:5000/` — 收件箱列表页
- README 详情：`http://localhost:5000/detail.html?id={id}`
- 管理控制台：`http://localhost:5000/search.html`

---

## 配置说明

编辑 `config.json`（关键词已迁移至 `keywords.json`）：

```json
{
  "github_token": "ghp_your_token_here",
  "auto_translate": false,
  "llama_cpp": {
    "base_url": "http://localhost:9898",
    "model": "Qwen3.6-35B-A3B",
    "max_tokens": 153600
  },
  "max_q_length": 100,
  "page_size": 80,
  "min_stars_stop": 1800,
  "clear_limit_count": 1800,
  "update_all": false
}
```

---

## 开发规范

### 代码风格

- Python：遵循 PEP 8，4 空格缩进
- 前端：原生 HTML/CSS/JS，无框架、无构建工具
- 注释：只写必要注释，避免冗余

### 数据库

- SQLite WAL 模式（`PRAGMA journal_mode=WAL`）
- 所有操作通过 `db.py` 函数封装，禁止直接 SQL
- JSON 字段存储为 TEXT，读取时自动解析

### Git 提交

- 中文提交信息，格式：`type: 简要描述`
- 类型：feat, fix, docs, chore, refactor

---

## 注意事项

1. **GitHub API 速率限制**：有 token 每分钟 5000 次，注意控制请求频率和批次间隔
2. **llama.cpp server**：不支持并发，翻译时避免其他请求干扰
3. **README 超长**：当前不分段翻译，如超时可考虑分段处理
4. **数据本地存储**：所有数据保存在本地，不依赖云服务
5. **手动标记已读**：进入详情页不会自动标记，需手动点击按钮

---

## 工程规范

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:

- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.
