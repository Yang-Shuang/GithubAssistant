<p align="center">
  <img src="ironclaw.png?v=2" alt="IronClaw" width="200"/>
</p>

<h1 align="center">IronClaw</h1>

<p align="center">
  <strong>你的安全个人 AI 助手，始终与你同在</strong>
</p>

<p align="center">
  <a href="#license"><img src="https://img.shields.io/badge/license-MIT%20OR%20Apache%202.0-blue.svg" alt="License: MIT OR Apache-2.0" /></a>
  <a href="https://t.me/ironclawAI"><img src="https://img.shields.io/badge/Telegram-%40ironclawAI-26A5E4?style=flat&logo=telegram&logoColor=white" alt="Telegram: @ironclawAI" /></a>
  <a href="https://www.reddit.com/r/ironclawAI/"><img src="https://img.shields.io/badge/Reddit-r%2FironclawAI-FF4500?style=flat&logo=reddit&logoColor=white" alt="Reddit: r/ironclawAI" /></a>
  <a href="https://gitcgr.com/nearai/ironclaw">
    <img src="https://gitcgr.com/badge/nearai/ironclaw.svg" alt="gitcgr" />
  </a>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.ru.md">Русский</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <a href="#philosophy">理念</a> •
  <a href="#features">功能特性</a> •
  <a href="#installation">安装</a> •
  <a href="#configuration">配置</a> •
  <a href="#security">安全机制</a> •
  <a href="#architecture">架构设计</a>
</p>

---

## 理念

IronClaw 基于一个简单的原则：**你的 AI 助手应该为你服务，而不是与你作对**。

在 AI 系统的数据处理方式日益不透明且往往与企业利益绑定的今天，IronClaw 采取了不同的方法：

- **数据完全归属你** - 所有信息均本地存储、加密处理，始终由你掌控
- **设计即透明** - 开源可审计，无隐藏遥测或数据采集行为
- **能力自我扩展** - 随时按需构建新工具，无需等待厂商更新
- **纵深防御体系** - 多层安全机制有效防范提示词注入（Prompt Injection）与数据泄露

IronClaw 是真正值得你将个人生活与职业事务托付的 AI 助手。

## 功能特性

### 安全优先

- **WASM 沙箱** - 不受信任的工具在隔离的 WebAssembly 容器中运行，并采用基于能力的权限控制
- **凭证保护** - 密钥永远不会暴露给工具；仅在宿主机边界注入，并配备泄露检测机制
- **提示词注入防御** - 模式检测、内容清洗与策略执行
- **端点白名单** - HTTP 请求仅允许访问明确批准的宿主和路径

### 始终可用

- **多通道支持** - 支持 REPL、HTTP Webhook、WASM 通道（Telegram、Slack）及网页网关
- **Docker 沙箱** - 隔离的容器执行环境，采用单任务令牌与编排器/工作器模式
- **网页网关** - 提供浏览器界面，支持实时 SSE/WebSocket 流式传输
- **例行任务（Routines）** - 基于定时计划、事件触发器和 Webhook 处理程序实现后台自动化
- **心跳系统** - 主动在后台执行监控与维护任务
- **并行任务** - 使用隔离上下文并发处理多个请求
- **自我修复** - 自动检测并恢复卡住的进程

### 能力自扩展

- **动态工具构建** - 描述你的需求，IronClaw 会将其编译为 WASM 工具
- **MCP 协议支持** - 连接模型上下文协议（Model Context Protocol）服务器以扩展功能
- **插件化架构** - 无需重启即可直接加载新的 WASM 工具与通道

### 持久记忆

- **混合搜索** - 结合全文检索与向量检索，采用倒数排名融合（Reciprocal Rank Fusion）算法
- **工作区文件系统** - 基于路径的灵活存储方案，用于保存笔记、日志和上下文信息
- **身份配置文件** - 跨会话保持统一的性格设定与偏好配置

## 安装

### 前置要求

- Rust 1.92+
- PostgreSQL 15+（需安装 [pgvector](https://github.com/pgvector/pgvector) 扩展）
- NEAR AI 账号（认证通过设置向导完成）
- `libclang` 及可用的 C 语言工具链（若从源码编译微信语音/SILK 路径）

## 下载或编译

访问 [发布页面](https://github.com/nearai/ironclaw/releases/)查看最新更新。

<details>
  <summary>通过 Windows 安装程序安装（Windows）</summary>

下载[Windows 安装程序](https://github.com/nearai/ironclaw/releases/latest/download/ironclaw-x86_64-pc-windows-msvc.msi)并运行它。

</details>

<details>
  <summary>通过 PowerShell 脚本安装（Windows）</summary>

```sh
irm https://github.com/nearai/ironclaw/releases/latest/download/ironclaw-installer.ps1 | iex
```

</details>

<details>
  <summary>通过 Shell 脚本安装（macOS、Linux、Windows/WSL）</summary>

```sh
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/nearai/ironclaw/releases/latest/download/ironclaw-installer.sh | sh
```
</details>

<details>
  <summary>通过 Homebrew 安装（macOS/Linux）</summary>

```sh
brew install ironclaw
```

</details>

<details>
  <summary>编译源码（Windows、Linux、macOS）</summary>

使用 `cargo` 进行安装，请确保你的计算机已安装 [Rust](https://rustup.rs)。

```bash
# Clone the repository
git clone https://github.com/nearai/ironclaw.git
cd ironclaw

# Build
cargo build --release

# Run tests
cargo test
```

对于**完整发布版本**（修改通道源码后），请先运行 `./scripts/build-all.sh` 重新编译通道。

> **可选：** 微信语音笔记（audio/silk）需要独立的 `ironclaw-silk-decoder` 辅助工具才能进行转录。默认工作区构建会排除该组件，因为 `silk-codec` 依赖 `bindgen`/`libclang`。请通过 `./crates/ironclaw_silk_decoder/build.sh` 单独编译它（需要 libclang + C 语言工具链），并将生成的二进制文件放入 `$PATH`、与 `ironclaw` 二进制文件同级，或通过环境变量 `IRONCLAW_SILK_DECODER` 指定路径。若无此组件，语音消息仍可接收——但将以原始 `audio/silk` 数据块形式呈现。

</details>

### 数据库配置

```bash
# Create database
createdb ironclaw

# Enable pgvector
psql ironclaw -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

## 配置

运行设置向导以配置 IronClaw：

```bash
ironclaw onboard
```

向导将处理数据库连接、NEAR AI 认证（通过浏览器 OAuth）以及密钥加密（使用系统钥匙串）。配置信息会持久化保存到已连接的数据库中；引导变量（例如 `DATABASE_URL`、`LLM_BACKEND`）会写入 `~/.ironclaw/.env`，以便在数据库连接前即可生效。

### 替代 LLM 提供商

IronClaw 默认使用 NEAR AI，但开箱即用地支持众多 LLM 提供商。
内置提供商包括 **Anthropic**、**OpenAI**、**GitHub Copilot**、**Google Gemini**、**MiniMax**、**Mistral** 以及 **Ollama**（本地）。同时支持 OpenAI 兼容服务，如 **OpenRouter**（300+ 模型）、**Together AI**、**Fireworks AI** 及自托管服务器（**vLLM**、**LiteLLM**）。

在向导中选择你的提供商，或直接设置环境变量：

```env
# Example: MiniMax (built-in, 204K context)
LLM_BACKEND=minimax
MINIMAX_API_KEY=...

# Example: OpenAI-compatible endpoint
LLM_BACKEND=openai_compatible
LLM_BASE_URL=https://openrouter.ai/api/v1
LLM_API_KEY=sk-or-...
LLM_MODEL=anthropic/claude-sonnet-4
```

请参阅 [docs/capabilities/llm-providers.md](docs/capabilities/llm-providers.md) 获取完整的提供商指南。

## 安全机制

IronClaw 采用纵深防御体系来保护你的数据并防止滥用。

### WASM 沙箱

所有不受信任的工具均在隔离的 WebAssembly 容器中运行：

- **基于能力的权限控制** - 显式授权 HTTP、密钥访问及工具调用
- **端点白名单** - HTTP 请求仅允许访问批准的宿主/路径
- **凭证注入** - 密钥仅在宿主机边界注入，绝不暴露给 WASM 代码
- **泄露检测** - 扫描请求与响应中的密钥外泄尝试
- **速率限制** - 按工具设置请求上限以防滥用
- **资源限制** - 约束内存、CPU 及执行时间

```
WASM ──► Allowlist ──► Leak Scan ──► Credential ──► Execute ──► Leak Scan ──► WASM
         Validator     (request)     Injector       Request     (response)
```

### 提示词注入防御

外部内容需经过多层安全过滤：

- 基于模式的注入尝试检测
- 内容清洗与转义处理
- 带有严重程度等级（拦截/警告/审查/清洗）的策略规则
- 工具输出包装，确保安全注入 LLM 上下文

### 数据保护

- 所有数据均本地存储于你的 PostgreSQL 数据库中
- 密钥采用 AES-256-GCM 加密
- 无遥测、数据分析或数据共享行为
- 完整记录所有工具执行操作的审计日志

## 架构设计

```
┌────────────────────────────────────────────────────────────────┐
│                          Channels                              │
│  ┌──────┐  ┌──────┐   ┌─────────────┐  ┌─────────────┐         │
│  │ REPL │  │ HTTP │   │WASM Channels│  │ Web Gateway │         │
│  └──┬───┘  └──┬───┘   └──────┬──────┘  │ (SSE + WS)  │         │
│     │         │              │         └──────┬──────┘         │
│     └─────────┴──────────────┴────────────────┘                │
│                              │                                 │
│                    ┌─────────▼─────────┐                       │
│                    │    Agent Loop     │  Intent routing       │
│                    └────┬──────────┬───┘                       │
│                         │          │                           │
│              ┌──────────▼────┐  ┌──▼───────────────┐           │
│              │  Scheduler    │  │ Routines Engine  │           │
│              │(parallel jobs)│  │(cron, event, wh) │           │
│              └──────┬────────┘  └────────┬─────────┘           │
│                     │                    │                     │
│       ┌─────────────┼────────────────────┘                     │
│       │             │                                          │
│   ┌───▼─────┐  ┌────▼────────────────┐                         │
│   │ Local   │  │    Orchestrator     │                         │
│   │Workers  │  │  ┌───────────────┐  │                         │
│   │(in-proc)│  │  │ Docker Sandbox│  │                         │
│   └───┬─────┘  │  │   Containers  │  │                         │
│       │        │  │ ┌───────────┐ │  │                         │
│       │        │  │ │Worker / CC│ │  │                         │
│       │        │  │ └───────────┘ │  │                         │
│       │        │  └───────────────┘  │                         │
│       │        └─────────┬───────────┘                         │
│       └──────────────────┤                                     │
│                          │                                     │
│              ┌───────────▼──────────┐                          │
│              │    Tool Registry     │                          │
│              │  Built-in, MCP, WASM │                          │
│              └──────────────────────┘                          │
└────────────────────────────────────────────────────────────────┘
```

### 核心组件

| Component | Purpose |
|-----------|---------|
| **Agent Loop** | 主要消息处理与任务协调 |
| **Router** | 分类用户意图（命令、查询、任务） |
| **Scheduler** | 管理带优先级的并行任务执行 |
| **Worker** | 结合 LLM 推理与工具调用执行任务 |
| **Orchestrator** | 容器生命周期管理、LLM 代理转发及单任务认证 |
| **Web Gateway** | 提供浏览器界面（聊天、记忆、任务、日志、扩展、例行任务） |
| **Routines Engine** | 定时（cron）与响应式（事件、webhook）后台任务引擎 |
| **Workspace** | 支持混合搜索的持久化记忆模块 |
| **Safety Layer** | 提示词注入防御与内容清洗层 |

## 使用方式

Engine v2 目前为可选功能。若想启用新引擎替代传统的 Agent Loop，请在启动 IronClaw 时添加 `ENGINE_V2=true`。详情请参阅 [docs/internal/engine-v2-architecture.md#enabling-engine-v2](docs/internal/engine-v2-architecture.md#enabling-engine-v2)。

```bash
# First-time setup (configures database, auth, etc.)
ironclaw onboard

# Start interactive REPL
cargo run

# Start interactive REPL with engine v2
ENGINE_V2=true cargo run

# Engine v2 with debug logging
ENGINE_V2=true RUST_LOG=ironclaw=debug cargo run
```

## 开发指南

```bash
# Format code
cargo fmt

# Lint
cargo clippy --all --benches --tests --examples --all-features

# Run tests
createdb ironclaw_test
cargo test

# Run specific test
cargo test test_name
```

- **通道（Channels）**：请参阅 [docs/channels/overview.mdx](docs/channels/overview.mdx) 了解 Telegram、Discord 及其他通道的配置方法。
- **修改通道源码**：在运行 `cargo build` 前，请先执行 `./channels-src/telegram/build.sh` 以确保更新后的 WASM 文件被正确打包。

## OpenClaw 传承

IronClaw 是受 [OpenClaw](https://github.com/openclaw/openclaw) 启发的 Rust 语言重新实现版本。完整的特性对照矩阵请参阅 [FEATURE_PARITY.md](FEATURE_PARITY.md)。

主要差异：

- **Rust 与 TypeScript** - 原生性能、内存安全、单一可执行文件
- **WASM 沙箱与 Docker** - 轻量级架构，基于能力的权限控制
- **PostgreSQL 与 SQLite** - 面向生产环境的持久化存储方案
- **安全优先设计** - 多层防御机制，强化凭证保护

## 许可证

本项目采用以下任一许可证：

- Apache License, Version 2.0（[LICENSE-APACHE](LICENSE-APACHE)）
- MIT License（[LICENSE-MIT](LICENSE-MIT)）

你可自由选择适用其中一项。