# 🦌 DeerFlow - 2.0

English | [中文](./README_zh.md) | [日本語](./README_ja.md) | [Français](./README_fr.md) | [Русский](./README_ru.md)

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](./backend/pyproject.toml)
[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](./Makefile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<a href="https://trendshift.io/repositories/14699" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14699" alt="bytedance%2Fdeer-flow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
> 2026年2月28日，DeerFlow在发布 2.0 版本后荣登 GitHub Trending 🏆 #1。感谢我们了不起的社区——是你们让这一切成为可能！💪🔥

DeerFlow（**D**eep **E**xploration and **E**fficient **R**esearch **F**low）是一个开源的**超级代理运行底座（Super Agent Harness）**，通过编排**子代理、记忆模块和沙盒环境**来实现几乎任何任务——由**可扩展技能（Skills）**驱动。

https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

> [!NOTE]
> **DeerFlow 2.0 是完全重写版本。** 它与 v1 没有任何共享代码。如果你正在寻找原始的 Deep Research 框架，它仍在 [`1.x` 分支](https://github.com/bytedance/deer-flow/tree/main-1.x) 上维护——那里依然欢迎贡献。活跃开发已移至 2.0。

## 官方网站

[<img width="2880" height="1600" alt="image" src="https://github.com/user-attachments/assets/a598c49f-3b2f-41ea-a052-05e21349188a" />](https://deerflow.tech)

访问我们的[**官方网站**](https://deerflow.tech)了解更多并查看**真实演示**。

## 字节跳动火山引擎编程计划

<img width="4808" height="2400" alt="英文方舟" src="https://github.com/user-attachments/assets/2ecc7b9d-50be-4185-b1f7-5542d222fb2d" />

- 我们强烈建议使用 Doubao-Seed-2.0-Code、DeepSeek v3.2 和 Kimi 2.5 来运行 DeerFlow
- [了解更多](https://www.byteplus.com/en/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)
- [中国大陆地区的开发者请点击这里](https://www.volcengine.com/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

## InfoQuest

DeerFlow 新集成了 BytePlus 独立研发的智能搜索与爬虫工具集——[InfoQuest（支持免费在线体验）](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)。

<a href="https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest" target="_blank">
  <img
    src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/hubseh7bsbps/20251208-160108.png"   alt="InfoQuest_banner"
  />
</a>

---

## 目录

- [🦌 DeerFlow - 2.0](#-deerflow---20)
  - [官方网站](#官方网站)
  - [字节跳动火山引擎编程计划](#字节跳动火山引擎编程计划)
  - [InfoQuest](#infoquest)
  - [目录](#目录)
  - [一键配置代理](#一键配置代理)
  - [快速开始](#快速开始)
    - [配置](#配置)
    - [运行应用](#运行应用)
      - [部署资源规划](#部署资源规划)
      - [方案 1：Docker（推荐）](#方案-1docker推荐)
      - [方案 2：本地开发](#方案-2本地开发)
    - [高级功能](#高级功能)
      - [沙盒模式](#沙盒模式)
      - [MCP Server](#mcp-server)
      - [IM 消息通道](#im-消息通道)
      - [LangSmith 追踪](#langsmith-追踪)
      - [Langfuse 追踪](#langfuse-追踪)
      - [同时使用两个提供商](#同时使用两个提供商)
  - [从深度研究到超级代理运行底座](#从深度研究到超级代理运行底座)
  - [核心功能](#核心功能)
    - [技能与工具](#技能与工具)
      - [Claude Code 集成](#claude-code-集成)
    - [子代理](#子代理)
    - [沙盒与文件系统](#沙盒与文件系统)
    - [上下文工程](#上下文工程)
    - [长期记忆](#长期记忆)
  - [推荐模型](#推荐模型)
  - [嵌入式 Python 客户端](#嵌入式-python-客户端)
  - [文档](#文档)
  - [⚠️ 安全须知](#️-安全须知)
    - [不当部署可能引入安全风险](#不当部署可能引入安全风险)
    - [安全建议](#安全建议)
  - [贡献指南](#贡献指南)
  - [许可证](#许可证)
  - [致谢](#致谢)
    - [核心作者](#核心作者)
  - [Star 历史](#star-历史)

## 一键配置代理

如果你使用 Claude Code、Codex、Cursor、Windsurf 或其他编码助手，只需一句话即可将设置说明交给它：

```text
Help me clone DeerFlow if needed, then bootstrap it for local development by following https://raw.githubusercontent.com/bytedance/deer-flow/main/Install.md
```

该提示旨在用于编码助手。它会指示助手在需要时克隆仓库，在有 Docker 时选择 Docker，并在停止前执行确切的下一条命令以及你仍需提供的任何缺失配置。

## 快速开始

### 配置

1. **克隆 DeerFlow 仓库**

   ```bash
   git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
   ```

2. **运行设置向导**

   在项目根目录（`deer-flow/`）下，运行：

   ```bash
   make setup
   ```

   这将启动一个交互式向导，引导你选择 LLM 提供商、可选的网页搜索功能，以及沙盒模式、bash 访问权限和文件写入工具等执行/安全偏好。它会生成一份精简的 `config.yaml` 并将你的密钥写入 `.env`。大约需要2分钟。

   该向导还允许你配置可选的网页搜索提供商，或暂时跳过。

   随时运行 `make doctor` 验证环境并获取可操作的修复提示。

   > **高级/手动配置**：如果你更喜欢直接编辑 `config.yaml`，请运行 `make config` 以复制完整模板。参见 `config.example.yaml` 获取完整参考文档，包括基于 CLI 的提供商（Codex CLI、Claude Code OAuth）、OpenRouter、Responses API 等。

   <details>
   <summary>手动模型配置示例</summary>

   ```yaml
   models:
     - name: gpt-4o
       display_name: GPT-4o
       use: langchain_openai:ChatOpenAI
       model: gpt-4o
       api_key: $OPENAI_API_KEY

     - name: openrouter-gemini-2.5-flash
       display_name: Gemini 2.5 Flash (OpenRouter)
       use: langchain_openai:ChatOpenAI
       model: google/gemini-2.5-flash-preview
       api_key: $OPENROUTER_API_KEY
       base_url: https://openrouter.ai/api/v1

     - name: gpt-5-responses
       display_name: GPT-5 (Responses API)
       use: langchain_openai:ChatOpenAI
       model: gpt-5
       api_key: $OPENAI_API_KEY
       use_responses_api: true
       output_version: responses/v1

     - name: qwen3-32b-vllm
       display_name: Qwen3 32B (vLLM)
       use: deerflow.models.vllm_provider:VllmChatModel
       model: Qwen/Qwen3-32B
       api_key: $VLLM_API_KEY
       base_url: http://localhost:8000/v1
       supports_thinking: true
       when_thinking_enabled:
         extra_body:
           chat_template_kwargs:
             enable_thinking: true
   ```

   OpenRouter 及类似的 OpenAI 兼容网关应使用 `langchain_openai:ChatOpenAI` 配合 `base_url` 进行配置。如果你偏好特定提供商的环境变量名，请显式将 `api_key` 指向该变量（例如 `api_key: $OPENROUTER_API_KEY`）。

   若要通过 `/v1/responses` 路由 OpenAI 模型，继续使用 `langchain_openai:ChatOpenAI` 并设置 `use_responses_api: true` 与 `output_version: responses/v1`。

   对于 vLLM 0.19.0，使用 `deerflow.models.vllm_provider:VllmChatModel`。对于 Qwen 风格的推理模型，DeerFlow 通过 `extra_body.chat_template_kwargs.enable_thinking` 切换推理功能，并在多轮工具调用对话中保留 vLLM 的非标准 `reasoning` 字段。旧的 `thinking` 配置会自动标准化以保证向后兼容。推理模型可能还需要服务器以 `--reasoning-parser ...` 启动。如果你的本地 vLLM 部署接受任何非空的 API Key，你仍可将 `VLLM_API_KEY` 设置为占位符值。

   CLI 支持的提供商示例：

   ```yaml
   models:
     - name: gpt-5.4
       display_name: GPT-5.4 (Codex CLI)
       use: deerflow.models.openai_codex_provider:CodexChatModel
       model: gpt-5.4
       supports_thinking: true
       supports_reasoning_effort: true

     - name: claude-sonnet-4.6
       display_name: Claude Sonnet 4.6 (Claude Code OAuth)
       use: deerflow.models.claude_provider:ClaudeChatModel
       model: claude-sonnet-4-6
       max_tokens: 4096
       supports_thinking: true
   ```

   - Codex CLI 读取 `~/.codex/auth.json`
   - Claude Code 接受 `CLAUDE_CODE_OAUTH_TOKEN`、`ANTHROPIC_AUTH_TOKEN`、`CLAUDE_CODE_CREDENTIALS_PATH` 或 `~/.claude/.credentials.json`
   - ACP 代理条目独立于模型提供商——如果你配置了 `acp_agents.codex`，请将其指向如 `npx -y @zed-industries/codex-acp` 的 Codex ACP 适配器
   - 在 macOS 上，如需可显式导出 Claude Code 认证：

   ```bash
   eval "$(python3 scripts/export_claude_code_oauth.py --print-export)"
   ```

   API Key 也可手动设置在 `.env`（推荐）或导出到 Shell：

   ```bash
   OPENAI_API_KEY=your-openai-api-key
   TAVILY_API_KEY=your-tavily-api-key
   ```

   </details>

### 运行应用

#### 部署资源规划

下表可作为选择 DeerFlow 运行方式的实用起点：

| 部署目标 | 起步配置 | 推荐配置 | 说明 |
|---------|-----------|------------|-------|
| 本地评估 / `make dev` | 4 vCPU, 8 GB RAM, 20 GB 空闲 SSD | 8 vCPU, 16 GB RAM | 适合单个开发者或单次轻量级会话（使用托管模型 API）。`2 vCPU / 4 GB` 通常不够。 |
| Docker 开发 / `make docker-start` | 4 vCPU, 8 GB RAM, 25 GB 空闲 SSD | 8 vCPU, 16 GB RAM | 镜像构建、绑定挂载和沙盒容器需要比纯本地开发更多的资源余量。 |
| 长期运行服务器 / `make up` | 8 vCPU, 16 GB RAM, 40 GB 空闲 SSD | 16 vCPU, 32 GB RAM | 适合共享使用、多代理运行、报告生成或更重的沙盒负载。 |

- 这些数值仅涵盖 DeerFlow 自身。如果你还托管本地 LLM，请单独评估该服务的资源需求。
- Linux + Docker 是持久化服务器的推荐部署目标。macOS 和 Windows 最好作为开发或测试环境使用。
- 如果 CPU 或内存持续满载，请先减少并发运行数，再考虑升级到下一档资源配置。

#### 方案 1：Docker（推荐）

**开发模式**（热重载、源码挂载）：

```bash
make docker-init    # 拉取沙盒镜像（仅首次或镜像更新时执行）
make docker-start   # 启动服务（自动从 config.yaml 检测沙盒模式）
```

当 `config.yaml` 使用 provisioner 模式（`sandbox.use: deerflow.community.aio_sandbox:AioSandboxProvider` 且包含 `provisioner_url`）时，`make docker-start` 才会启动 `provisioner`。

Docker 构建默认使用上游 `uv` 注册表。如果在受限网络中需要更快的镜像源，请在运行 `make docker-init` 或 `make docker-start` 前导出环境变量：
`UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple` 和 `NPM_REGISTRY=https://registry.npmmirror.com`。

后端进程会在下次访问配置时自动读取 `config.yaml` 的更改，因此在开发过程中模型元数据更新无需手动重启。

> [!TIP]
> 在 Linux 上，如果基于 Docker 的命令因 `permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock` 失败，请将你的用户添加到 `docker` 组并重新登录后再试。详见 [CONTRIBUTING.md](CONTRIBUTING.md#linux-docker-daemon-permission-denied) 中的完整修复步骤。

**生产模式**（本地构建镜像、挂载运行时配置和数据）：

```bash
make up     # 构建镜像并启动所有生产服务
make down   # 停止并移除容器
```

访问地址：http://localhost:2026

统一的 nginx 端点默认同域，且不发送浏览器 CORS 头。如果你运行的是跨域或端口转发后的浏览器客户端，请将 `GATEWAY_CORS_ORIGINS` 设置为逗号分隔的精确源（如 `http://localhost:3000`）；Gateway 随后会应用 CORS 白名单并匹配 CSRF 源检查。

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 获取详细的 Docker 开发指南。

#### 方案 2：本地开发

如果你偏好在本地运行服务：

前置条件：首先完成上述“配置”步骤（`make setup`）。`make dev` 需要项目根目录下存在有效的 `config.yaml`。设置 `DEER_FLOW_PROJECT_ROOT` 可显式定义该根目录，或设置 `DEER_FLOW_CONFIG_PATH` 指向特定配置文件。运行时状态默认位于项目根目录下的 `.deer-flow`，可通过 `DEER_FLOW_HOME` 移动；技能默认位于项目根目录下的 `skills/`，可通过 `DEER_FLOW_SKILLS_PATH` 移动。启动前请运行 `make doctor` 验证你的环境。
在 Windows 上，请通过 Git Bash 运行本地开发流程。不支持原生的 `cmd.exe` 和 PowerShell shell，也不保证 WSL 可用，因为部分脚本依赖 Git for Windows 的工具（如 `cygpath`）。

1. **检查前置条件**：
   ```bash
   make check  # 验证 Node.js 22+、pnpm、uv、nginx
   ```

2. **安装依赖**：
   ```bash
   make install  # 安装后端 + 前端依赖 + pre-commit hooks
   ```

3. **（可选）预拉取沙盒镜像**：
   ```bash
   # 如果使用基于 Docker/容器的沙盒，推荐执行
   make setup-sandbox
   ```

4. **（可选）加载示例记忆数据供本地预览**：
   ```bash
   python scripts/load_memory_sample.py
   ```
   这会将示例文件复制到默认本地运行时记忆文件中，以便审查者立即测试 `Settings > Memory`。
   详见 [backend/docs/MEMORY_SETTINGS_REVIEW.md](backend/docs/MEMORY_SETTINGS_REVIEW.md) 获取最短预览流程说明。

5. **启动服务**：
   ```bash
   make dev
   ```

6. **访问地址**：http://localhost:2026

#### 启动模式

DeerFlow 在 Gateway API 内部运行代理运行时。开发模式启用热重载；生产模式使用预构建的前端。

| | **本地前台** | **本地守护进程** | **Docker 开发** | **Docker 生产** |
|---|---|---|---|---|
| **Dev** | `./scripts/serve.sh --dev`<br/>`make dev` | `./scripts/serve.sh --dev --daemon`<br/>`make dev-daemon` | `./scripts/docker.sh start`<br/>`make docker-start` | — |
| **Prod** | `./scripts/serve.sh --prod`<br/>`make start` | `./scripts/serve.sh --prod --daemon`<br/>`make start-daemon` | — | `./scripts/deploy.sh`<br/>`make up` |

| 操作 | 本地 | Docker 开发 | Docker 生产 |
|---|---|---|---|
| **停止** | `./scripts/serve.sh --stop`<br/>`make stop` | `./scripts/docker.sh stop`<br/>`make docker-stop` | `./scripts/deploy.sh down`<br/>`make down` |
| **重启** | `./scripts/serve.sh --restart [flags]` | `./scripts/docker.sh restart` | — |

Gateway 负责管理 `/api/langgraph/*` 路由，并在 nginx 后端将其翻译为原生 `/api/*` 路由。

#### Docker 生产部署

`deploy.sh` 支持分别构建和启动：

```bash
# 一步完成（构建 + 启动）
deploy.sh

# 两步完成（先构建一次，稍后启动）
deploy.sh build              # 构建所有镜像
deploy.sh start              # 启动预构建的镜像

# 停止服务
deploy.sh down
```

### 高级功能

#### 沙盒模式

DeerFlow 支持多种沙盒执行模式：
- **本地执行**（直接在宿主机上运行沙盒代码）
- **Docker 执行**（在隔离的 Docker 容器中运行沙盒代码）
- **Kubernetes + Docker 执行**（通过 provisioner 服务在 Kubernetes Pod 中运行沙盒代码）

对于 Docker 开发，服务启动遵循 `config.yaml` 中的沙盒模式。在本地/Docker 模式下，不会启动 `provisioner`。

详见 [沙盒配置指南](backend/docs/CONFIGURATION.md#sandbox) 配置你偏好的模式。

#### MCP Server

DeerFlow 支持可配置的 MCP Server 和技能以扩展其能力。
对于 HTTP/SSE MCP Server，支持 OAuth Token 流程（`client_credentials`、`refresh_token`）。
详见 [MCP Server 指南](backend/docs/MCP_SERVER.md) 获取详细说明。

#### IM 消息通道

DeerFlow 支持接收来自即时通讯应用的任务。配置后通道会自动启动——无需任何公共 IP。

| 通道 | 传输方式 | 难度 |
|---------|-----------|------------|
| Telegram | Bot API（长轮询） | 简单 |
| Slack | Socket Mode | 中等 |
| Feishu / Lark | WebSocket | 中等 |
| WeChat | Tencent iLink（长轮询） | 中等 |
| WeCom | WebSocket | 中等 |
| DingTalk | Stream Push (WebSocket) | 中等 |

**`config.yaml` 中的配置：**

```yaml
channels:
  # LangGraph-compatible Gateway API base URL (default: http://localhost:8001/api)
  langgraph_url: http://localhost:8001/api
  # Gateway API URL (default: http://localhost:8001)
  gateway_url: http://localhost:8001

  # Optional: global session defaults for all mobile channels
  session:
    assistant_id: lead_agent  # or a custom agent name; custom agents are routed via lead_agent + agent_name
    config:
      recursion_limit: 100
    context:
      thinking_enabled: true
      is_plan_mode: false
      subagent_enabled: false

  feishu:
    enabled: true
    app_id: $FEISHU_APP_ID
    app_secret: $FEISHU_APP_SECRET
    # domain: https://open.feishu.cn       # China (default)
    # domain: https://open.larksuite.com   # International

  wecom:
    enabled: true
    bot_id: $WECOM_BOT_ID
    bot_secret: $WECOM_BOT_SECRET

  slack:
    enabled: true
    bot_token: $SLACK_BOT_TOKEN     # xoxb-...
    app_token: $SLACK_APP_TOKEN     # xapp-... (Socket Mode)
    allowed_users: []               # empty = allow all

  telegram:
    enabled: true
    bot_token: $TELEGRAM_BOT_TOKEN
    allowed_users: []               # empty = allow all

  wechat:
    enabled: false
    bot_token: $WECHAT_BOT_TOKEN
    ilink_bot_id: $WECHAT_ILINK_BOT_ID
    qrcode_login_enabled: true      # optional: allow first-time QR bootstrap when bot_token is absent
    allowed_users: []               # empty = allow all
    polling_timeout: 35
    state_dir: ./.deer-flow/wechat/state
    max_inbound_image_bytes: 20971520
    max_outbound_image_bytes: 20971520
    max_inbound_file_bytes: 52428800
    max_outbound_file_bytes: 52428800

    # Optional: per-channel / per-user session settings
    session:
      assistant_id: mobile-agent  # custom agent names are also supported here
      context:
        thinking_enabled: false
      users:
        "123456789":
          assistant_id: vip-agent
          config:
            recursion_limit: 150
          context:
            thinking_enabled: true
            subagent_enabled: true

  dingtalk:
    enabled: true
    client_id: $DINGTALK_CLIENT_ID             # Client ID of your DingTalk application
    client_secret: $DINGTALK_CLIENT_SECRET     # Client Secret of your DingTalk application
    allowed_users: []                          # empty = allow all
    card_template_id: ""                       # Optional: AI Card template ID for streaming typewriter effect
```

说明：
- `assistant_id: lead_agent` 直接调用默认的 LangGraph 助手。
- 如果 `assistant_id` 设置为自定义代理名，DeerFlow 仍通过 `lead_agent` 路由并注入该值作为 `agent_name`，从而使自定义代理的 SOUL/配置在 IM 通道中生效。
- IM 通道工作者在内部调用 Gateway 的兼容 LangGraph API，并自动附加进程本地内部认证及创建线程和运行所需的 CSRF cookie/header 对。

在你的 `.env` 文件中设置相应的 API Key：

```bash
# Telegram
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ

# Slack
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...

# Feishu / Lark
FEISHU_APP_ID=cli_xxxx
FEISHU_APP_SECRET=your_app_secret

# WeChat iLink
WECHAT_BOT_TOKEN=your_ilink_bot_token
WECHAT_ILINK_BOT_ID=your_ilink_bot_id

# WeCom
WECOM_BOT_ID=your_bot_id
WECOM_BOT_SECRET=your_bot_secret

# DingTalk
DINGTALK_CLIENT_ID=your_client_id
DINGTALK_CLIENT_SECRET=your_client_secret
```

**Telegram 设置**

1. 与 [@BotFather](https://t.me/BotFather) 聊天，发送 `/newbot`，并复制 HTTP API Token。
2. 在 `.env` 中设置 `TELEGRAM_BOT_TOKEN` 并在 `config.yaml` 中启用该通道。

**Slack 设置**

1. 在 [api.slack.com/apps](https://api.slack.com/apps) 创建 Slack App → Create New App → From scratch。
2. 在 **OAuth & Permissions** 下，添加 Bot Token Scopes：`app_mentions:read`, `chat:write`, `im:history`, `im:read`, `im:write`, `files:write`。
3. 启用 **Socket Mode** → 生成应用级 Token（`xapp-…`），权限包含 `connections:write`。
4. 在 **Event Subscriptions** 下，订阅 bot 事件：`app_mention`, `message.im`。
5. 在 `.env` 中设置 `SLACK_BOT_TOKEN` 和 `SLACK_APP_TOKEN` 并在 `config.yaml` 中启用该通道。

**Feishu / Lark 设置**

1. 在 [飞书开放平台](https://open.feishu.cn/) 创建应用 → 启用 **机器人** 能力。
2. 添加权限：`im:message`, `im:message.p2p_msg:readonly`, `im:resource`。
3. 在 **Events** 下，订阅 `im.message.receive_v1` 并选择 **长连接（Long Connection）** 模式。
4. 复制 App ID 和 App Secret。在 `.env` 中设置 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET` 并在 `config.yaml` 中启用该通道。

**WeChat 设置**

1. 在 `config.yaml` 中启用 `wechat` 通道。
2. 可在 `.env` 中设置 `WECHAT_BOT_TOKEN`，或设置 `qrcode_login_enabled: true` 进行首次 QR 码引导绑定。
3. 当缺少 `bot_token` 且启用了 QR 引导时，观察后端日志中 iLink 返回的 QR 内容并完成绑定流程。
4. QR 流程成功后，DeerFlow 会将获取到的 Token 持久化保存到 `state_dir` 以便后续重启使用。
5. 对于 Docker Compose 部署，请将 `state_dir` 放在持久卷上，以确保 `get_updates_buf` 游标和已保存的认证状态在重启后保留。

**WeCom 设置**

1. 在 WeCom AI Bot 平台创建机器人并获取 `bot_id` 和 `bot_secret`。
2. 在 `config.yaml` 中启用 `channels.wecom` 并填入 `bot_id` / `bot_secret`。
3. 在 `.env` 中设置 `WECOM_BOT_ID` 和 `WECOM_BOT_SECRET`。
4. 确保后端依赖包含 `wecom-aibot-python-sdk`。该通道使用 WebSocket 长连接，无需公共回调 URL。
5. 当前集成支持接收文本、图片和文件消息。代理生成的最终图片/文件也会发送回 WeCom 会话。

**DingTalk 设置**

1. 在 [钉钉开发者后台](https://open.dingtalk.com/) 创建应用并启用 **机器人（Robot）** 能力。
2. 在机器人配置页面将消息接收模式设置为 **Stream Mode**。
3. 复制 `Client ID` 和 `Client Secret`，在 `.env` 中设置 `DINGTALK_CLIENT_ID` 和 `DINGTALK_CLIENT_SECRET`，并在 `config.yaml` 中启用该通道。
4. *（可选）* 要启用的流式 AI 卡片回复（打字机效果），需在 [钉钉卡片平台](https://open.dingtalk.com/document/dingstart/typewriter-effect-streaming-ai-card) 创建 **AI Card** 模板，然后在 `config.yaml` 中设置 `card_template_id` 为模板 ID。你还需要申请 `Card.Streaming.Write` 和 `Card.Instance.Write` 权限。

当 DeerFlow 在 Docker Compose 中运行时，IM 通道会在 `gateway` 容器内执行。此时请勿将 `channels.langgraph_url` 或 `channels.gateway_url` 指向 `localhost`；请使用容器服务名（如 `http://gateway:8001/api` 和 `http://gateway:8001`），或设置环境变量 `DEER_FLOW_CHANNELS_LANGGRAPH_URL` 与 `DEER_FLOW_CHANNELS_GATEWAY_URL`。

**命令**

通道连接后，你可以直接在聊天中与 DeerFlow 交互：

| 命令 | 说明 |
|---------|-------------|
| `/new` | 开始新对话 |
| `/status` | 显示当前线程信息 |
| `/models` | 列出可用模型 |
| `/memory` | 查看记忆 |
| `/help` | 显示帮助 |

> 不带命令前缀的消息将被视为普通聊天——DeerFlow 会创建线程并以对话方式回复。

#### LangSmith 追踪

DeerFlow 内置 [LangSmith](https://smith.langchain.com) 集成用于可观测性。启用后，所有 LLM 调用、代理运行和工具执行都会被追踪并在 LangSmith 仪表板中可见。

将以下内容添加到你的 `.env` 文件：

```bash
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=lsv2_pt_xxxxxxxxxxxxxxxx
LANGSMITH_PROJECT=xxx
```

#### Langfuse 追踪

DeerFlow 也支持 [Langfuse](https://langfuse.com) 用于兼容 LangChain 的运行可观测性。

将以下内容添加到你的 `.env` 文件：

```bash
LANGFUSE_TRACING=true
LANGFUSE_PUBLIC_KEY=pk-lf-xxxxxxxxxxxxxxxx
LANGFUSE_SECRET_KEY=sk-lf-xxxxxxxxxxxxxxxx
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

如果你使用的是自托管的 Langfuse 实例，请将 `LANGFUSE_BASE_URL` 设置为你的部署 URL。

#### 同时使用两个提供商

如果同时启用了 LangSmith 和 Langfuse，DeerFlow 会附加双追踪回调并将相同的模型活动报告给两个系统。

如果显式启用了某个提供商但缺少必要凭据，或其回调初始化失败，DeerFlow 会在创建模型期间初始化追踪时快速失败（fails fast），并在错误消息中指明导致失败的提供商。

对于 Docker 部署，追踪功能默认禁用。在 `.env` 中设置 `LANGSMITH_TRACING=true` 和 `LANGSMITH_API_KEY` 即可启用。

## 从深度研究到超级代理运行底座

DeerFlow 最初是一个深度研究框架——而社区将其推向了更远的地方。自发布以来，开发者们用它构建了远超研究的场景：搭建数据管道、生成幻灯片、创建仪表盘、自动化内容工作流。这些是我们从未预料到的用法。

这告诉我们一个重要事实：DeerFlow 不仅仅是一个研究工具。它是一个**运行底座（Harness）**——一个赋予代理实际完成工作的基础设施的运行环境。

于是我们从头重构了它。

DeerFlow 2.0 不再是一个需要你自行拼装的框架。它是一个超级代理运行底座——开箱即用，完全可扩展。基于 LangGraph 和 LangChain 构建，内置了代理所需的一切：文件系统、记忆模块、技能体系、沙盒感知执行环境，以及规划任务和生成子代理的能力。

直接使用即可。或者拆散它，打造属于你自己的版本。

## 核心功能

### 技能与工具

技能是让 DeerFlow 能够*几乎做任何事*的关键。

标准 Agent Skill 是一个结构化的能力模块——一个定义工作流、最佳实践和辅助资源引用的 Markdown 文件。DeerFlow 内置了研究、报告生成、幻灯片制作、网页创建、图像和视频生成等技能。但真正的力量在于可扩展性：添加你自己的技能，替换内置的，或将它们组合成复合工作流。

技能采用渐进式加载——仅在任务需要时加载，而非一次性全部载入。这保持了上下文窗口的精简，使 DeerFlow 即使在令牌敏感的模型下也能良好运行。

当你通过 Gateway 安装 `.skill` 归档文件时，DeerFlow 会接受标准的可选 frontmatter 元数据（如 `version`、`author`、`compatibility`），而不是拒绝其他方面有效的外部技能。

工具遵循相同的设计哲学。DeerFlow 自带核心工具集——网页搜索、网页抓取、文件操作、bash 执行——并支持通过 MCP Server 和 Python 函数添加自定义工具。随意替换或添加任何内容。

Gateway 生成的后续建议现在会在解析 JSON 数组响应前，规范化纯字符串模型输出与块/列表样式的富文本内容，因此特定提供商的内容包装器不会静默丢弃建议。

```
# Paths inside the sandbox container
/mnt/skills/public
├── research/SKILL.md
├── report-generation/SKILL.md
├── slide-creation/SKILL.md
├── web-page/SKILL.md
└── image-generation/SKILL.md

/mnt/skills/custom
└── your-custom-skill/SKILL.md      ← yours
```

#### Claude Code 集成

`claude-to-deerflow` 技能允许你直接从 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 与正在运行的 DeerFlow 实例交互。发送研究任务、检查状态、管理线程——无需离开终端。

**安装技能**：

```bash
npx skills add https://github.com/bytedance/deer-flow --skill claude-to-deerflow
```

然后确保 DeerFlow 正在运行（默认在 `http://localhost:2026`），并在 Claude Code 中使用 `/claude-to-deerflow` 命令。

**你可以做什么**：
- 向 DeerFlow 发送消息并获取流式响应
- 选择执行模式：flash（快速）、standard、pro（规划）、ultra（子代理）
- 检查 DeerFlow 健康状态，列出模型/技能/代理
- 管理线程和对话历史
- 上传文件进行分析

**环境变量**（可选，用于自定义端点）：

```bash
DEERFLOW_URL=http://localhost:2026            # Unified proxy base URL
DEERFLOW_GATEWAY_URL=http://localhost:2026    # Gateway API
DEERFLOW_LANGGRAPH_URL=http://localhost:2026/api/langgraph  # LangGraph API
```

详见 [`skills/public/claude-to-deerflow/SKILL.md`](skills/public/claude-to-deerflow/SKILL.md) 获取完整 API 参考。

### 子代理

复杂任务很少能单次完成。DeerFlow 会将其拆解。

主代理可以动态生成子代理——每个子代理拥有独立的上下文范围、工具集和终止条件。子代理在可能时并行运行，返回结构化结果，由主代理综合所有内容输出连贯结果。当启用令牌用量追踪时，已完成的子代理用量将追溯归因到分发步骤。

这就是 DeerFlow 处理耗时数分钟至数小时任务的方式：一个研究任务可能会发散出十几个子代理，各自探索不同方向，然后收敛为单一报告——或网站——或带有生成视觉效果的幻灯片。一套底座，多方协作。

### 沙盒与文件系统

DeerFlow 不只是*谈论*做事。它拥有自己的计算机。

每个任务都获得独立的执行环境及完整的文件系统视图——技能、工作区、上传文件、输出结果。代理可以读取、写入和编辑文件。它可以查看图片，并在安全配置下执行 Shell 命令。

使用 `AioSandboxProvider` 时，Shell 执行在隔离容器内进行。使用 `LocalSandboxProvider` 时，文件工具仍映射到宿主机上的每线程目录，但默认禁用宿主 `bash`，因为它不是安全的隔离边界。仅在对完全可信的本地工作流启用宿主 bash。

这就是拥有工具访问权限的聊天机器人与拥有实际执行环境的代理之间的区别。

```
# Paths inside the sandbox container
/mnt/user-data/
├── uploads/          ← your files
├── workspace/        ← agents' working directory
└── outputs/          ← final deliverables
```

### 上下文工程

**隔离的子代理上下文**：每个子代理在独立的上下文中运行。这意味着子代理无法看到主代理或其他子代理的上下文。这确保了子代理能够专注于当前任务，而不受主代理或其他子代理上下文的干扰。

**摘要压缩**：在一个会话内，DeerFlow 会积极管理上下文——对已完成的子任务进行摘要、将中间结果卸载到文件系统、压缩不再立即相关的内容。这使得它能够在长周期多步骤任务中保持敏锐，而不会撑爆上下文窗口。

**严格工具调用恢复**：当提供商或中间件中断工具调用循环时，DeerFlow 现在会在强制停止的助手消息上剥离提供商级别的原生工具调用元数据，并在下一次模型调用前为悬空调用注入占位符结果。这确保了严格验证 `tool_call_id` 序列的 OpenAI 兼容推理模型不会因格式错误的历史记录而失败。

### 长期记忆

大多数代理在对话结束的瞬间就会忘记一切。DeerFlow 会记住。

跨会话中，DeerFlow 建立对你个人档案、偏好和积累知识的持久记忆。你使用得越多，它越了解你——你的写作风格、技术栈、 recurring workflows。记忆存储在本地并完全由你控制。

记忆更新现在在应用时跳过重复的事实条目，因此重复的偏好和上下文不会跨会话无限累积。

## 推荐模型

DeerFlow 与模型无关——它适用于任何实现 OpenAI 兼容 API 的 LLM。话虽如此，它在支持以下特性的模型上表现最佳：

- **长上下文窗口**（100k+ tokens）用于深度研究和多步骤任务
- **推理能力**用于自适应规划和复杂分解
- **多模态输入**用于图像理解和视频解析
- **强大的工具使用**用于可靠的功能调用和结构化输出

## 嵌入式 Python 客户端

DeerFlow 可作为嵌入式 Python 库使用，无需运行完整的 HTTP 服务。`DeerFlowClient` 提供对代理和 Gateway 所有功能的直接进程内访问，返回与 HTTP Gateway API 相同的响应模式。HTTP Gateway 还暴露 `DELETE /api/threads/{thread_id}` 以在 LangGraph 线程本身被删除后移除 DeerFlow 管理的本地线程数据：

```python
from deerflow.client import DeerFlowClient

client = DeerFlowClient()

# Chat
response = client.chat("Analyze this paper for me", thread_id="my-thread")

# Streaming (LangGraph SSE protocol: values, messages-tuple, end)
for event in client.stream("hello"):
    if event.type == "messages-tuple" and event.data.get("type") == "ai":
        print(event.data["content"])

# Configuration & management — returns Gateway-aligned dicts
models = client.list_models()        # {"models": [...]}
skills = client.list_skills()        # {"skills": [...]}
client.update_skill("web-search", enabled=True)
client.upload_files("thread-1", ["./report.pdf"])  # {"success": True, "files": [...]}
```

所有返回字典的方法均在 CI 中通过 `TestGatewayConformance` 对照 Gateway Pydantic 响应模型进行验证，确保嵌入式客户端与 HTTP API 模式保持同步。详见 `backend/packages/harness/deerflow/client.py` 获取完整 API 文档。

## 文档

- [贡献指南](CONTRIBUTING.md) - 开发环境设置与工作流
- [配置指南](backend/docs/CONFIGURATION.md) - 安装与配置说明
- [架构概览](backend/CLAUDE.md) - 技术架构详情
- [后端架构](backend/README.md) - 后端架构与 API 参考

## ⚠️ 安全须知

### 不当部署可能引入安全风险

DeerFlow 具备包括**系统命令执行、资源操作和业务逻辑调用**在内的高权限关键功能，默认设计为**部署在本地可信环境中（仅通过 127.0.0.1 回环接口访问）**。如果你在未采取严格安全措施的情况下将代理部署在不信任的环境中——例如局域网、公共云服务器或其他多端点可访问环境——可能引入安全风险，包括：

- **未授权非法调用**：代理功能可能被未经授权的第叁方或恶意互联网扫描器发现，触发批量未授权请求以执行系统命令和文件读写等高危操作，可能导致严重的安全后果。
- **合规与法律风险**：如果代理被非法调用于进行网络攻击、数据窃取或其他违法活动，可能引发法律责任和合规风险。

### 安全建议

**注意：我们强烈建议在本地可信网络环境中部署 DeerFlow。** 如果你需要跨设备或跨网络部署，必须实施严格的安全措施，例如：

- **IP 白名单**：使用 `iptables`，或部署带有访问控制列表（ACL）的硬件防火墙/交换机，以**配置 IP 白名单规则**并拒绝所有其他 IP 地址的访问。
- **认证网关**：配置反向代理（如 nginx）并**启用强预认证**，拦截任何未认证的访问。
- **网络隔离**：尽可能将代理和可信设备置于**专用的同一 VLAN 中**，与其他网络设备隔离。
- **保持更新**：持续关注 DeerFlow 的安全功能更新。

## 贡献指南

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 获取开发环境设置、工作流和规范说明。

回归测试覆盖包括 `backend/tests/` 中的 Docker 沙盒模式检测和 provisioner kubeconfig-path 处理测试。
Gateway 工件服务现在强制对活跃 Web 内容类型（`text/html`, `application/xhtml+xml`, `image/svg+xml`）以附件形式下载而非内联渲染，降低了生成工件的 XSS 风险。

## 许可证

本项目为开源项目，遵循 [MIT License](./LICENSE)。

## 致谢

DeerFlow 建立在开源社区的卓越工作之上。我们深深感谢所有使 DeerFlow 成为可能的项目和贡献者。诚然，我们站在巨人的肩膀上。

我们要向以下项目致以诚挚的谢意，感谢它们宝贵的贡献：

- **[LangChain](https://github.com/langchain-ai/langchain)**：其卓越的框架驱动了我们的 LLM 交互与链式调用，实现了无缝集成与功能扩展。
- **[LangGraph](https://github.com/langchain-ai/langgraph)**：其在多代理编排方面的创新方法对实现 DeerFlow 的复杂工作流起到了关键作用。

这些项目彰显了开源协作的转变力量，我们自豪地构建于它们的基础之上。

### 核心作者

衷心感谢 `DeerFlow` 的核心作者们，你们的远见、热情与奉献使该项目得以诞生：

- **[Daniel Walnut](https://github.com/hetaoBackend/)**
- **[Henry Li](https://github.com/magiccube/)**

你们坚定不移的承诺与专业知识是 DeerFlow 成功的核心驱动力。很荣幸能与你共同引领这段旅程。

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=bytedance/deer-flow&type=Date)](https://star-history.com/#bytedance/deer-flow&Date)