# GitHub Reader — 需求文档 & 任务分解

---

## 一、项目概述

**项目名称**：GitHub Reader  
**目标用户**：开发者本人（单用户本地工具）  
**核心价值**：通过关键词订阅 GitHub 热门仓库，自动抓取 README 并翻译为中文，以收件箱形式管理阅读进度。

---


## 二、需求文档（PRD）

### 2.1 功能模块总览

| 模块 | 说明 |
|------|------|
| 抓取模块 | 通过 GitHub API 按关键词搜索仓库，拉取 README 原文 |
| 翻译模块 | 调用本地 llama.cpp（OpenAI 兼容接口）翻译 README |
| 存储模块 | SQLite 存储仓库元数据，README 文件存本地磁盘 |
| Web 服务 | 本地 Flask 服务，提供 API 和静态页面 |
| 收件箱页面 | 仓库列表，类邮箱收件箱，显示已读/未读状态 |
| 详情页面 | 展示 README，支持英文/中文切换 |
| 搜索页面 | 管理关键词订阅，手动触发一次性抓取 |

---

### 2.2 详细功能需求

#### F1 — 抓取模块

- 支持配置多个关键词（如 `vibe coding`、`ai agent`、`llm tool`）
- 每个关键词按 star 数量降序抓取 Top N 条（默认 20，可配置）
- 字段抓取：仓库全名、描述、star 数、语言、topics、HTML URL、默认分支
- 调用 `/readme` 接口获取 README 原文（base64 解码后存为 `.md` 文件）
- 去重：已存在于数据库的仓库跳过重复写入，但更新 star 数
- 支持 GitHub Personal Access Token（配置文件管理）
- 速率限制友好：请求间隔可配置（默认 0.5s）

#### F2 — 翻译模块

- 调用本地 llama.cpp server（OpenAI 兼容 `/v1/chat/completions` 接口）
- 翻译模型：Qwen3.6-35B-A3B（通过配置文件指定 base_url 和 model name）
- README 可能较长，需分段翻译（按 token 估算，超过阈值则切段）
- 翻译结果存入 SQLite（`readme_zh` 字段），同时写入 `_zh.md` 文件备份
- 翻译状态字段：`pending` / `translating` / `done` / `failed`
- 翻译失败时记录错误信息，支持重试
- 抓取完成后自动批量翻译所有 `pending` 状态条目

#### F3 — 存储模块

**数据库：SQLite（`data/db.sqlite`）**

`repositories` 表：

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PK | 自增主键 |
| full_name | TEXT UNIQUE | owner/repo |
| description | TEXT | 仓库描述 |
| stars | INTEGER | star 数量 |
| language | TEXT | 主语言 |
| topics | TEXT | JSON 数组字符串 |
| html_url | TEXT | GitHub 链接 |
| readme_path | TEXT | 本地 README 原文路径 |
| readme_zh_path | TEXT | 本地中文译文路径 |
| translate_status | TEXT | pending/translating/done/failed |
| translate_error | TEXT | 失败原因 |
| is_read | INTEGER | 0=未读, 1=已读 |
| keywords | TEXT | 来源关键词（JSON 数组） |
| fetched_at | TEXT | 首次抓取时间 ISO8601 |
| updated_at | TEXT | 最后更新时间 |

**文件存储：`data/readme/`**

- 原文：`data/readme/{owner}__{repo}.md`
- 译文：`data/readme/{owner}__{repo}_zh.md`

#### F4 — Web 服务

- Flask 本地服务，默认端口 5000
- 提供 REST API 供前端 JS 调用
- 静态文件服务（`web/` 目录）
- 配置文件：`config.json`

**API 列表：**

| Method | Path | 说明 |
|--------|------|------|
| GET | `/api/repos` | 获取仓库列表，支持分页、筛选已读/未读 |
| GET | `/api/repos/:id` | 获取单个仓库详情 |
| GET | `/api/repos/:id/readme` | 获取 README 原文（markdown） |
| GET | `/api/repos/:id/readme_zh` | 获取 README 中文译文 |
| POST | `/api/repos/:id/read` | 标记已读 |
| POST | `/api/repos/:id/unread` | 标记未读 |
| GET | `/api/keywords` | 获取关键词列表 |
| POST | `/api/fetch` | 触发一次抓取（异步，返回 task_id） |
| GET | `/api/fetch/status` | 查询抓取/翻译进度 |

#### F5 — 收件箱页面（`index.html`）

- 列表展示所有仓库，每行显示：
  - 未读标记（蓝点）
  - 仓库全名（加粗）
  - 描述（截断显示）
  - Star 数
  - 翻译状态图标（⏳待翻译 / ✅已翻译 / ❌失败）
  - 来源关键词标签
  - 抓取时间
- 支持按"未读/全部"筛选
- 点击行进入详情页
- 顶部显示未读数量

#### F6 — 详情页面（`detail.html`）

- 顶部显示仓库名、star 数、描述、GitHub 链接
- README 内容区，Markdown 渲染
- 右上角切换按钮：**英文 / 中文**
  - 默认显示英文原文
  - 点击切换为中文译文
  - 切换状态记录在 localStorage（每个仓库独立记忆）
- 若译文状态为 `pending`/`translating`，显示提示"翻译进行中"
- 进入详情页自动标记已读
- 返回按钮回到收件箱

#### F7 — 搜索/管理页面（`search.html`）

- 关键词管理：增加/删除订阅关键词
- 手动触发抓取按钮，显示实时进度（抓取了多少、翻译了多少）
- 显示数据库统计：总仓库数、已翻译数、未读数

---

### 2.3 配置文件（`config.json`）

```json
{
  "github_token": "ghp_xxx",
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

---

### 2.4 非功能需求

- 所有数据本地存储，不依赖任何云服务
- 启动命令：`python server.py`，浏览器访问 `http://localhost:5000`
- 抓取/翻译脚本：`python fetch.py`，可独立运行，也可通过 Web 页面触发
- Windows 任务计划支持（`fetch.py` 可无头运行，日志输出到 `data/fetch.log`）
- README 超长时分段翻译，保证不超 llama.cpp 上下文限制

---

## 三、任务分解（Task Breakdown）

> 建议使用 opencode + 本地模型按任务逐步完成，每个任务都是独立可验证的。

---

### Phase 0 — 项目初始化

**T0.1** 创建项目目录结构
```
github-reader/
├── config.json
├── server.py
├── fetch.py
├── db.py
├── translator.py
├── data/
│   └── readme/
└── web/
    ├── index.html
    ├── detail.html
    ├── search.html
    └── assets/
        ├── style.css
        └── app.js
```

**T0.2** 创建 `config.json` 模板和配置读取工具函数

**T0.3** 安装依赖（`pip install flask requests`），生成 `requirements.txt`

---

### Phase 1 — 数据库层（`db.py`）

**T1.1** 初始化 SQLite，创建 `repositories` 表（含所有字段）

**T1.2** 实现 `upsert_repo(data)` — 新增或更新仓库记录（以 `full_name` 为唯一键）

**T1.3** 实现 `get_repos(filter, page, page_size)` — 列表查询，支持 `unread`/`all` 筛选

**T1.4** 实现 `get_repo(id)` — 单条查询

**T1.5** 实现 `mark_read(id)` / `mark_unread(id)`

**T1.6** 实现 `update_translate_status(id, status, error=None)`

**验收**：用 Python 脚本手动插入几条测试数据，查询验证正确。

---

### Phase 2 — 抓取模块（`fetch.py` 的抓取部分）

**T2.1** 实现 `search_repos(keyword, top_n)` — 调用 GitHub Search API，返回结构化列表

**T2.2** 实现 `fetch_readme(full_name)` — 调用 `/repos/{owner}/{repo}/readme`，base64 解码，写入本地文件

**T2.3** 实现 `run_fetch(keywords)` — 遍历关键词，调用上述两步，写入数据库，打印进度日志

**T2.4** 添加请求间隔和错误处理（404/403/429 各自处理）

**验收**：运行 `python fetch.py --fetch-only`，数据库有数据，`data/readme/` 有文件。

---

### Phase 3 — 翻译模块（`translator.py`）

**T3.1** 实现 `call_llm(prompt)` — 调用 llama.cpp `/v1/chat/completions` 接口，返回文本

**T3.2** 实现 `split_text(text, chunk_size)` — 按段落切分长文本，保证不截断 Markdown 结构

**T3.3** 实现 `translate_readme(text)` — 调用 `split_text` + `call_llm`，拼接结果，返回完整译文

**T3.4** 实现 `run_translate()` — 查询所有 `pending` 状态仓库，逐个翻译，更新状态，写文件

**T3.5** 翻译 Prompt 设计：
```
你是一个技术文档翻译助手。将以下 GitHub README（Markdown 格式）翻译为简体中文。
要求：保持所有 Markdown 格式（标题、代码块、链接等）不变，只翻译自然语言文本。
直接输出译文，不要加任何说明。
```

**验收**：运行 `python fetch.py --translate-only`，数据库中 `translate_status` 变为 `done`，文件存在。

---

### Phase 4 — Web 服务（`server.py`）

**T4.1** Flask 基础框架，静态文件服务，健康检查接口

**T4.2** 实现 `GET /api/repos` — 分页列表接口

**T4.3** 实现 `GET /api/repos/:id`、`GET /api/repos/:id/readme`、`GET /api/repos/:id/readme_zh`

**T4.4** 实现 `POST /api/repos/:id/read` / `unread`

**T4.5** 实现 `GET /api/keywords`、`POST /api/keywords`、`DELETE /api/keywords/:kw`

**T4.6** 实现 `POST /api/fetch` — 在后台线程中运行 `fetch.py` 逻辑，返回进度

**T4.7** 实现 `GET /api/fetch/status` — 查询当前任务进度

**验收**：用 curl 或浏览器逐一测试所有接口。

---

### Phase 5 — 前端（Web UI）

**T5.1** `index.html` — 收件箱列表页
- 调用 `GET /api/repos` 渲染列表
- 未读/全部切换
- 未读蓝点、翻译状态图标
- 点击跳转详情页

**T5.2** `detail.html` — 详情页
- 调用 `GET /api/repos/:id` 获取元数据
- 调用 `GET /api/repos/:id/readme` 和 `/readme_zh`
- 用 `marked.js` 渲染 Markdown
- 英文/中文切换按钮
- 自动调用标记已读接口

**T5.3** `search.html` — 管理页
- 关键词列表展示和增删
- 触发抓取按钮 + 进度轮询展示
- 统计数字展示（总数/已翻译/未读）

**T5.4** `style.css` — 统一样式
- 收件箱风格（类 Gmail/Outlook）
- 响应式，适合桌面使用
- 深色/浅色主题（可选）

**验收**：完整流程跑通：搜索页触发抓取 → 收件箱出现新条目 → 点进详情看英文 → 切换看中文。

---

### Phase 6 — 收尾

**T6.1** `fetch.py` 整合为完整 CLI：
```
python fetch.py              # 抓取 + 翻译（全流程）
python fetch.py --fetch-only # 只抓取
python fetch.py --translate-only # 只翻译
python fetch.py --keyword "rag pipeline" # 临时添加关键词
```

**T6.2** 日志输出到 `data/fetch.log`，含时间戳

**T6.3** Windows 任务计划配置说明（写入 README）

**T6.4** 项目 README 文档：安装步骤、配置说明、使用方法

---

## 四、技术栈总结

| 层 | 技术 |
|----|------|
| 后端 | Python 3.x + Flask |
| 数据库 | SQLite（标准库 `sqlite3`） |
| HTTP 客户端 | `requests` |
| Markdown 渲染 | 前端 `marked.js`（CDN） |
| 翻译 | llama.cpp server（OpenAI 兼容）+ Qwen3.6-35B-A3B |
| 前端 | 原生 HTML + CSS + JS（无框架） |
| 部署 | 本地运行，`python server.py` |

---

## 五、开发顺序建议

```
T0（初始化）→ T1（DB）→ T2（抓取）→ T3（翻译）→ T4（API）→ T5（前端）→ T6（收尾）
```
