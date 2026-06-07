<p align="center">
  <picture>
    <img src="./docs/images/logo.png" alt="WeKnora Logo" height="120"/>
  </picture>
</p>

<p align="center">
  <picture>
    <a href="https://trendshift.io/repositories/15289" target="_blank">
      <img src="https://trendshift.io/api/badge/repositories/15289" alt="Tencent%2FWeKnora | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
    </a>
  </picture>
</p>
<p align="center">
    <a href="https://weknora.weixin.qq.com" target="_blank">
        <img alt="Official Website" src="https://img.shields.io/badge/Official Website-WeKnora-4e6b99">
    </a>
    <a href="https://chatbot.weixin.qq.com" target="_blank">
        <img alt="WeChat Dialog Open Platform" src="https://img.shields.io/badge/WeChat Dialog Open Platform-5ac725">
    </a>
    <a href="https://chromewebstore.google.com/detail/jpemjbopikggjlmikmclgbmkhhopjdgd" target="_blank">
        <img alt="Chrome Extension" src="https://img.shields.io/badge/Chrome Extension-WeKnora-4285F4">
    </a>
    <a href="https://clawhub.ai/lyingbug/weknora" target="_blank">
        <img alt="ClawHub Skill" src="https://img.shields.io/badge/ClawHub Skill-WeKnora-ff6b35">
    </a>
    <a href="https://github.com/Tencent/WeKnora/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-ffffff?labelColor=d4eaf7&color=2e6cc4" alt="License">
    </a>
    <a href="./CHANGELOG.md">
        <img alt="Version" src="https://img.shields.io/badge/version-0.6.0-2e6cc4?labelColor=d4eaf7">
    </a>
</p>

<p align="center">
| <b><a href="./README.md">English</a></b> | <b>简体中文</b> | <a href="./README_JA.md"><b>日本語</b></a> | <a href="./README_KO.md"><b>한국어</b></a> |
</p>

<p align="center">
  <h4 align="center">

  [概述](#-概述) • [架构](#-架构) • [核心功能](#-核心功能) • [快速开始](#-快速开始) • [API 参考](#-api-参考) • [开发者指南](#-开发者指南)
  
  </h4>
</p>

# 💡 WeKnora —— 借助 RAG、智能体与自动 Wiki，将文档转化为鲜活的知识库

## 📌 概述

[**WeKnora**](https://weknora.weixin.qq.com) 是一款开源的、由大语言模型（LLM）驱动的知识框架，专为企业级文档理解、语义检索与自主推理而设计。

它围绕三大核心能力构建：面向日常查询的 **基于 RAG 的快速问答**、能够自主编排检索与 MCP 工具及网页搜索以处理复杂多步任务的 **ReAct 智能体（Agent）**，以及全新的 **Wiki 模式**——在该模式下，智能体会将原始文档提炼为自维护、相互关联的 Markdown 知识库，并附带交互式知识图谱。结合多源数据接入（飞书/Notion/语雀等持续扩展）、20+ LLM 服务商集成、完整的 Langfuse 可观测性、**面向企业级应用的多租户 RBAC**（4 层角色矩阵 + 资源级所有权 + 租户级审计日志）以及完全支持私有化部署的模块化架构，WeKnora 能够将零散的文档转化为可查询、具备推理能力且持续演进的动态知识资产。

该框架支持从飞书、Notion 和语雀自动同步知识库（更多数据源即将上线），兼容 PDF、Word、图片、Excel 等 10+ 种文档格式，并可通过企业微信、飞书、Slack 和 Telegram 等即时通讯（IM）渠道直接提供问答服务。它全面对接 OpenAI、DeepSeek、Qwen（阿里云）、智谱、混元、Gemini、MiniMax、NVIDIA 及 Ollama 等主要大模型服务商。其高度模块化的设计允许自由替换 LLM、向量数据库与存储后端，支持本地化与私有云部署以保障数据主权完整。此外，WeKnora 深度集成 **Langfuse**，提供智能体推理过程、Token 消耗及流水线追踪的全面可观测性。

## ✨ 最新更新

- **v0.6.0** —— 租户 RBAC（4 层角色矩阵 `Owner` / `Admin` / `Contributor` / `Viewer` + 知识库级所有权 + 租户级审计日志）、租户成员管理与多工作区交互体验、自助创建工作区；`weknora` CLI v0.4 GA 正式版支持 `mcp serve`；跨向量存储的知识库检索扇出分发（fan-out）；AES-256-GCM 凭证加密 + docreader gRPC TLS + Token；智谱 Embedder + 华为云 OBS；服务端用户偏好设置；Go 1.26.0。详见 [`docs/RBAC说明.md`](./docs/RBAC说明.md) 与 [`CHANGELOG.md`](./CHANGELOG.md)。
- **v0.5.2** —— Wiki 数据摄入支持至 4 万文档规模的知识库（任务队列 + DLQ）；MCP human-in-the-loop 工具审批；Anthropic / Apache Doris / 腾讯 VectorDB / KS3 / SearXNG 后端适配；自适应三层分块与实时预览；全局 `⌘K` 命令面板；语雀连接器 + 微信小程序；`weknora` CLI 预览版。
- **v0.5.1** —— 知识库批量管理；租户级 IM 渠道总览；会话搜索 + 用户级置顶；统一模型/网页搜索/MCP 设置卡片；单智能体 LLM 超时配置；桌面端租户切换。
- **v0.5.0** —— Wiki 模式 GA：智能体自动生成结构化、相互关联的 Markdown Wiki 页面与知识图谱；UI 内置 Wiki 浏览器与可视化图谱。
- **v0.4.0** —— WeKnora Cloud（托管 LLM + 解析服务）；Chrome 扩展；ClawHub Skill；微信 IM；附件处理；Azure OpenAI / 阿里云 OSS；Notion 连接器；百度+Ollama 网页搜索；VectorStore 管理。
- **v0.3.6** —— ASR（语音识别）；飞书数据源自动同步；OIDC；IM 引用回复上下文 + 基于线程的会话；文档摘要生成；Tavily 搜索；并行工具调用；智能体 `@mention` 作用域限制。
- **v0.3.5** —— Telegram / DingTalk / Mattermost IM；IM 斜杠命令 + QA 队列；建议问题；VLM 自动描述 MCP 工具图片；Novita AI；渠道追踪。
- **v0.3.4** —— WeCom / Feishu / Slack IM；多模态图像支持；NVIDIA 模型 API；Weaviate；AWS S3；AES-256-GCM API Key 加密；内置 MCP 服务；混合搜索优化；`final_answer` 工具。
- **v0.3.3** —— 父子分块（Parent-child chunking）；知识库置顶；兜底回复；用于重排的段落清洗；存储自动创建；Milvus 支持。
- **v0.3.2** —— 知识搜索入口；单源解析器与存储引擎配置；本地存储图像渲染；文档预览；火山云 TOS；Mermaid 渲染；批量会话管理；记忆图谱预览。
- **v0.3.0** —— Shared Space（共享空间）；智能体技能 + 沙箱隔离执行；自定义智能体；数据分析师智能体；思考模式；Bing / Google 网页搜索；API Key 鉴权；Helm Chart；韩语国际化；Qdrant。
- **v0.2.0** —— Agent Mode（ReAct）；多类型知识库（FAQ + 文档）；对话策略配置；DuckDuckGo 网页搜索；MCP 工具集成；支持智能体模式切换的新 UI；MQ 异步任务管理。

## 📱 界面展示

<table>
  <tr>
    <td colspan="2" align="center"><b>💬 智能问答对话</b><br/><img src="./docs/images/qa.png" alt="Intelligent Q&A Conversation" width="100%"></td>
  </tr>
  <tr>
    <td width="50%" align="center"><b>📖 Wiki 浏览器</b><br/><img src="./docs/images/wiki-browser.png" alt="Wiki Browser" width="100%"></td>
    <td width="50%" align="center"><b>🕸️ Wiki 知识图谱</b><br/><img src="./docs/images/wiki-graph.png" alt="Wiki Knowledge Graph" width="100%"></td>
  </tr>
  <tr>
    <td width="50%" align="center"><b>🤖 Agent 模式 · 工具调用流程</b><br/><img src="./docs/images/agent-qa.png" alt="Agent Mode Tool Call Process" width="100%"></td>
    <td width="50%" align="center"><b>⚙️ 对话设置</b><br/><img src="./docs/images/settings.png" alt="Conversation Settings" width="100%"></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><b>🔭 可观测性 · Langfuse 链路追踪</b><br/><img src="./docs/images/langfuse.png" alt="Observability Langfuse Tracing" width="100%"></td>
  </tr>
</table>

## 🏗️ 架构

![weknora-architecture.png](./docs/images/architecture.png)

从文档解析、向量化、检索到 LLM 推理的全链路高度模块化——所有组件均可插拔替换与扩展。支持本地化/私有云部署以保障完整的数据主权，并提供零门槛的 Web UI 助力快速上手。

## 🧩 核心功能

**智能对话**

| 能力 | 说明 |
|------------|---------|
| 智能推理 | ReAct 渐进式多步推理，自主编排知识检索、MCP 工具与网页搜索；支持自定义智能体 |
| 快速问答 | 基于知识库的 RAG 问答，提供精准快速的回答 |
| Wiki 模式 | 由智能体驱动，自动将原始文档生成结构化、相互关联的 Markdown Wiki 页面 |
| 工具调用 | 内置工具、MCP 工具与网页搜索 |
| 对话策略 | 在线 Prompt 编辑、检索阈值调优、多轮上下文感知 |
| 建议问题 | 基于知识库内容自动生成提问建议 |

**知识管理**

| 能力 | 说明 |
|------------|---------|
| 知识库类型 | FAQ / 文档 / Wiki，支持文件夹导入、URL 导入、标签管理与在线入口 |
| 数据源接入 | 自动同步飞书/Notion/语雀（更多数据源即将上线）；增量与全量同步 |
| 文档格式 | PDF / Word / Txt / Markdown / HTML / 图片 / CSV / Excel / PPT / JSON |
| 检索策略 | BM25 稀疏检索 / 稠密检索 / GraphRAG / 父子分块（parent-child chunking）/ 多维索引 |
| 端到端测试 | 全链路可视化，支持召回命中率、BLEU / ROUGE 指标评估 |

**集成与扩展**

| 能力 | 说明 |
|------------|---------|
| LLM | OpenAI / Azure OpenAI / Anthropic (Claude) / DeepSeek / Qwen (阿里云) / 智谱 / 混元 / Doubao (火山引擎) / Gemini / MiniMax / NVIDIA / Novita AI / SiliconFlow / OpenRouter / Ollama |
| Embeddings | Ollama / BGE / GTE / 智谱 / OpenAI 兼容 API |
| 向量数据库 | PostgreSQL (pgvector) / Elasticsearch / Milvus / Weaviate / Qdrant / Apache Doris / 腾讯 VectorDB |
| 对象存储 | 本地 / MinIO / AWS S3 / 火山云 TOS / 阿里云 OSS / 金山云 KS3 / 华为云 OBS |
| IM 渠道 | 企业微信 / 飞书 / Slack / Telegram / 钉钉 / Mattermost / 微信 |
| 网页搜索 | DuckDuckGo / Bing / Google / Tavily / 百度 / Ollama / SearXNG |

**平台能力**

| 能力 | 说明 |
|------------|---------|
| 部署方式 | 本地化 / Docker / Kubernetes (Helm)，支持私有与离线环境 |
| 用户界面 | Web UI / RESTful API / CLI (`weknora`) / Chrome 扩展 / 微信小程序 |
| 访问控制 | 租户 RBAC（4 层角色矩阵 `Owner` / `Admin` / `Contributor` / `Viewer`）、知识库资源级所有权、租户级审计日志、邀请制工作区、自助创建租户、跨租户超级管理员 |
| 安全机制 | API Key 及 MCP/数据源凭证采用 AES-256-GCM 静态加密，支持密钥平滑轮换；应用与 docreader 间 gRPC TLS + Token；防 SSRF 攻击的 HTTP 客户端；智能体技能沙箱隔离 |
| 可观测性 | 集成 Langfuse，覆盖 ReAct 循环、Token 追踪、工具调用及流水线链路 |
| 任务管理 | MQ 异步任务、版本升级时自动数据库迁移 |
| 模型管理 | 集中化配置、知识库级模型选择、多租户内置模型共享、WeKnora Cloud 托管模型与解析服务 |

## 🧩 Chrome 扩展

[**WeKnora Chrome Extension**](https://chromewebstore.google.com/detail/jpemjbopikggjlmikmclgbmkhhopjdgd) 让你能够将网页内容直接捕获至 WeKnora 知识库。在浏览器中选中文本、图片或整个页面，一键保存为知识条目——无需复制粘贴或手动上传文件。

## 📱 微信小程序

[WeKnora 小程序](./miniprogram/README.md) 提供轻量级移动端客户端，支持配置 API 访问权限、选择知识库、导入 URL，并在微信内直接进行知识问答对话。

## 🦞 ClawHub Skill

[**WeKnora ClawHub Skill**](https://clawhub.ai/lyingbug/weknora) 是发布在 ClawHub 平台上的 WeKnora 技能插件。安装后，你可通过智能体实现文档导入（文件 / URL / Markdown）、跨知识库混合搜索（向量 + 关键词）以及知识条目管理——全部通过 WeKnora REST API 驱动。

- **文档导入** —— 上传文件、抓取网页或编写 Markdown 知识
- **混合搜索** —— 在单个或多个知识库中使用向量+关键词进行检索
- **知识管理** —— 以编程方式列出、浏览、编辑和删除知识条目

## ⌨️ 命令行界面（CLI）

`weknora` 是驱动 API 的官方 CLI，适用于终端或 AI Agent。其命令结构遵循 `gh` CLI 的 `<名词> <动词>` 规范；默认输出为人类可读格式，配合 `--json` 参数可切换至稳定的 JSON 信封格式。

```bash
weknora auth login --host https://kb.example.com
weknora kb list
weknora link --kb my-knowledge-base    # 绑定当前目录
weknora doc upload notes.md
weknora chat "summarise the design doc"
```

安装指南与 5 分钟快速上手见 [`cli/README.md`](./cli/README.md)。AI Agent（Claude Code、Cursor、Aider 等）可依赖的交互契约详见 [`cli/AGENTS.md`](./cli/AGENTS.md)。

## 🚀 快速开始

### 🛠 前置条件

- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

### 📦 安装与启动

```bash
git clone https://github.com/Tencent/WeKnora.git
cd WeKnora
cp .env.example .env   # 按需编辑 .env，文件内附有注释说明
docker compose up -d   # 启动核心服务
```

启动完成后，访问 **http://localhost** 即可开始使用。

> 如需使用本地 Ollama 模型，请先运行 `ollama serve > /dev/null 2>&1 &`。

### 🔧 可选服务（Docker Compose Profiles）

添加 `--profile` 参数以启用额外组件。可组合多个 Profile：

| Profile | 说明 | 命令 |
|---------|-------------|---------|
| _(默认)_ | 核心服务 | `docker compose up -d` |
| `full` | 全量功能 | `docker compose --profile full up -d` |
| `neo4j` | 知识图谱 (Neo4j) | `docker compose --profile neo4j up -d` |
| `minio` | 对象存储 (MinIO) | `docker compose --profile minio up -d` |
| `langfuse` | 链路追踪 (Langfuse) | `docker compose --profile langfuse up -d` |

组合使用：`docker compose --profile neo4j --profile minio up -d`

停止服务：`docker compose down`

### 🌐 服务地址

| 服务 | URL |
|---------|-----|
| Web UI | `http://localhost` |
| 后端 API | `http://localhost:8080` |
| Langfuse 追踪 | `http://localhost:3000` |

## MCP Server

必要配置请参考 [MCP 配置指南](./mcp-server/MCP_CONFIG.md)。

## 🔌 使用微信对话开放平台

WeKnora 作为 [微信对话开放平台](https://chatbot.weixin.qq.com) 的核心技术底座，提供更便捷的使用方式：

- **零代码部署**：只需上传知识库即可快速在微信生态内部署智能问答服务，实现“即问即答”体验
- **高效问题管理**：支持高频问题分类管理，配合丰富的数据工具，确保答案准确可靠、易于维护
- **微信生态融合**：通过微信对话开放平台，WeKnora 的智能问答能力可无缝接入微信公众号、小程序等微信场景，提升用户交互体验

## 📘 API 参考

常见问题排查指南：[Troubleshooting FAQ](./docs/QA.md)

详细 API 文档请访问：[API Docs](./docs/api/README.md)

产品规划与即将上线的功能：[Roadmap](./docs/ROADMAP.md)

## 🧭 开发者指南

### ⚡ 快速开发模式（推荐）

如果你需要频繁修改代码，**无需每次重新构建 Docker 镜像！** 使用快速开发模式：

```bash
# 启动基础依赖服务
make dev-start

# 启动后端（新终端窗口）
make dev-app

# 启动前端（新终端窗口）
make dev-frontend
```

**开发优势：**
- ✅ 前端修改自动热重载（无需重启）
- ✅ 后端修改快速重启（5-10 秒，支持 Air 热重载）
- ✅ 免 Docker 镜像构建
- ✅ 支持 IDE 断点调试

**详细文档：** [开发环境快速开始](./docs/开发指南.md)

## 🤝 贡献指南

欢迎提交 [Issues](https://github.com/Tencent/WeKnora/issues) 或 Pull Requests。

**流程：** Fork 仓库 → 创建分支 → 提交更改 → 发起 PR

**规范：** 使用 `gofmt` 格式化代码，遵循 [Conventional Commits](https://www.conventionalcommits.org/)（`feat:` / `fix:` / `docs:` / `test:` / `refactor:`）

## 🔒 安全须知

**重要提示：** 自 v0.1.3 起，WeKnora 已内置登录认证功能以提升系统安全性。针对生产环境部署，我们强烈建议你：

- 将 WeKnora 服务部署在内网或私有网络环境中，而非公网
- 避免将服务直接暴露于公共网络，以防潜在信息泄露
- 为部署环境配置合理的防火墙规则与访问控制策略
- 定期更新至最新版本以获取安全补丁与功能改进

## 👥 贡献者

感谢以下优秀贡献者的付出：

[![Contributors](https://contrib.rocks/image?repo=Tencent/WeKnora)](https://github.com/Tencent/WeKnora/graphs/contributors)

## 📄 许可证

本项目采用 [MIT License](./LICENSE)。
你可自由使用、修改和分发代码，只需保留正确的署名信息。

## 📈 项目统计

<a href="https://www.star-history.com/#Tencent/WeKnora&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Tencent/WeKnora&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Tencent/WeKnora&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Tencent/WeKnora&type=date&legend=top-left" />
 </picture>
</a>