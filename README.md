# GitHub Reader 📚

> **通过关键词订阅 GitHub 热门仓库，自动抓取 README 并翻译为中文，以收件箱形式管理阅读进度。**

## 💡 解决的问题

### 痛点分析

| 痛点 | 描述 |
|------|------|
| 🔍 **信息过载** | GitHub 每天新增大量仓库，手动搜索关键词、逐个查看效率极低 |
| 🌐 **语言障碍** | 英文 README 阅读速度慢，理解成本高，尤其对非英语母语开发者 |

### 核心价值

- **自动化发现**：关键词订阅 + 自动抓取，告别手动搜索
- **中文阅读体验**：LLM 批量翻译 README 和描述信息
- **收件箱管理**：标记已读/未读、排序筛选、分页浏览
- **完全本地化**：数据存储在本地 SQLite，不依赖云服务

## 👥 目标用户

| 用户类型 | 场景 |
|----------|------|
| **技术追踪者** | 需要持续关注特定领域（如 AI Agent、MCP Server）的开发者 |
| **中文优先读者** | 英文阅读速度较慢，偏好中文技术文档的开发者 |
| **信息收集爱好者** | 定期整理和归档 GitHub 热门项目的研究者 |

## ✨ 功能特性

### 核心功能

- 🔍 **关键词订阅搜索**：支持多关键词分批查询，按星标数降序排列
- 📥 **自动抓取 README**：获取仓库元数据 + README 内容（base64 解码）
- 🌏 **LLM 批量翻译**：调用本地 llama.cpp server 翻译 README 和描述信息
- 📖 **收件箱式浏览**：列表页支持筛选/排序/分页，详情页支持中英文切换
- ⚡ **异步任务管理**：抓取、翻译线程独立运行，可随时中断

### 高级功能

- 🏷️ **Topics 标签云**：动态显示热门话题，字号按频率调整
- 📊 **数据统计面板**：实时统计仓库总数/已读/未读/翻译进度
- 🔧 **数据清理工具**：安全删除低星标仓库（预览模式 + 二次确认）
- 🌐 **Public Viewer**：半独立静态模块，部署到 GitHub Pages 对外分享

## 🏗️ 技术架构

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   Web 前端   │◄──►│   Flask API  │◄──►│   SQLite DB  │
│ (HTML/CSS/JS)│    │ (RESTful)     │    │ (WAL 模式)    │
└─────────────┘    └──────┬───────┘    └─────────────┘
                          │
              ┌───────────▼───────────┐
              │   Python 核心模块      │
              │  • fetch.py (抓取)     │
              │  • translator.py (翻译)│
              │  • db.py (数据操作)    │
              └───────────────────────┘
                          │
              ┌───────────▼───────────┐
              │   llama.cpp server    │
              │   + Qwen3.6-35B-A3B   │
              └───────────────────────┘
```

## 📂 项目结构

```
github-reader/
├── config.json              # 运行时配置（GitHub Token、关键词参数等）
├── keywords.json            # 关键词列表（独立于 config.json）
├── user-config.json         # 个人配置（不提交到 Git，优先读取）
├── config.py                # 配置读取 + 路径工具函数
├── server.py                # Flask Web 服务入口 + REST API
├── fetch.py                 # GitHub 数据抓取模块
├── translator.py            # LLM 翻译模块
├── db.py                    # SQLite 数据库操作层（建表/迁移/CRUD）
├── utils.py                 # 通用工具（日志、路径转换、彩色终端输出）
├── clear.py                 # 数据清理工具（低星标仓库删除）
├── public/                  # Public Viewer（半独立公开模块，纯静态部署）
├── data/                    # 运行时数据目录
│   ├── db.sqlite            # SQLite 数据库文件
│   └── readme/              # README 原始文件和中文译文存储目录
└── web/                     # 前端静态资源（由 Flask static_folder 直接托管）
    ├── index.html           # 收件箱列表页
    ├── detail.html          # README 详情页
    ├── search.html          # 管理控制台页
    ├── style.css            # 全局样式
    └── app.js               # 前端 JS 逻辑（API 封装 + 三页面交互）
```

## 🚀 快速开始

### 前置条件

- Python 3.x
- llama.cpp server（用于翻译功能，可选）

### 安装步骤

1. **克隆项目**

```bash
git clone <repository-url>
cd github-reader
```

2. **配置 GitHub Token**

编辑 `config.json`，填入你的 GitHub Access Token：

```json
{
  "github_token": "ghp_xxxxxxxxxxxxxxxxxxxx"
}
```

3. **设置关键词**

编辑 `keywords.json`，添加你关注的领域：

```json
{
  "keywords": [
    {"key": "vibe coding"},
    {"key": "ai agent"},
    {"key": "mcp server"}
  ]
}
```

4. **启动服务**

```bash
python server.py
```

5. **访问界面**

打开浏览器访问 `http://localhost:5000/`，即可开始使用。

## ⚙️ 配置说明

### config.json — 运行时配置

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `github_token` | string | - | GitHub API Token（提高速率限制） |
| `auto_translate` | boolean | false | 抓取后是否自动翻译 README |
| `llama_cpp.base_url` | string | http://localhost:9898 | llama.cpp server 地址 |
| `llama_cpp.model` | string | Qwen3.6-35B-A3B | 使用的模型名称 |
| `llama_cpp.max_tokens` | integer | 153600 | 最大 token 数（支持长 README） |
| `max_q_length` | integer | 100 | 每批关键词查询串最大长度 |
| `page_size` | integer | 80 | GitHub API per_page，单页抓取数量 |
| `min_stars_stop` | integer | 1800 | stars 低于此值时停止翻页 |
| `clear_limit_count` | integer | 1800 | clear.py 清理阈值（stars < 此值的仓库可被删除） |
| `update_all` | boolean | false | true=全量更新，false=增量模式（跳过已有 README 的仓库） |


## 🛠️ 常用命令

### 启动服务

```bash
# 启动 Web 服务（默认端口 5000，监听所有接口）
python server.py
```

### 手动触发任务

```bash
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

## ❓ 常见问题

### Q: GitHub API 401 错误？

**A:** 检查 `config.json` 中的 `github_token` 是否正确，确认 token 未过期。

### Q: 翻译失败？

**A:** 
- 检查 llama.cpp server 是否正常运行
- 查看 `data/translator.log` 日志
- 确认 `config.json` 中 `base_url` 无末尾斜杠

### Q: README 加载失败？

**A:** 确保仓库有 README 文件，或尝试重新抓取。

## 📄 License

MIT License

---

**GitHub Reader** — 让技术追踪更高效 ✨
