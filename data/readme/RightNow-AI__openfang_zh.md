<p align="center">
  <img src="public/assets/openfang-logo.png" width="160" alt="OpenFang Logo" />
</p>

<h1 align="center">OpenFang</h1>
<h3 align="center">智能体操作系统（Agent OS）</h3>

<p align="center">
  用 Rust 构建的开源 Agent OS。13.7万行代码，14个 crate，1,767+ 项测试，零 Clippy 警告。<br/>
  <strong>一个二进制文件。历经实战检验。真正为你工作的智能体。</strong>
</p>

<p align="center">
  <a href="https://openfang.sh/docs">Documentation（文档）</a> &bull;
  <a href="https://openfang.sh/docs/getting-started">Quick Start（快速入门）</a> &bull;
  <a href="https://x.com/openfangg">Twitter / X</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/language-Rust-orange?style=flat-square" alt="Rust" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT" />
  <img src="https://img.shields.io/badge/version-0.6.9-green?style=flat-square" alt="v0.6.9" />
  <img src="https://img.shields.io/badge/tests-2,696%2B%20passing-brightgreen?style=flat-square" alt="Tests" />
  <img src="https://img.shields.io/badge/clippy-0%20warnings-brightgreen?style=flat-square" alt="Clippy" />
  <a href="https://www.buymeacoffee.com/openfang" target="_blank"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" /></a>
</p>

---

> **v0.5.10（2026年4月）**
>
> OpenFang 功能已完整，但仍处于 v1.0 之前的预发布阶段。预期在次版本之间会有细微瑕疵和破坏性更新。我们快速迭代，快速修复。在生产环境中请锁定特定提交记录直到 v1.0。[在此报告问题](https://github.com/RightNow-AI/openfang/issues)

---

## 什么是 OpenFang？

OpenFang 是一个**开源智能体操作系统**。它不是聊天机器人框架，也不是包裹 LLM 的 Python 封装库，更不是“多智能体编排器”。它是一个从头用 Rust 构建的、专为自主智能体设计的完整操作系统。

传统的智能体框架需要你输入指令才会运行。OpenFang 运行**真正为你工作的自主智能体**：按预定计划、全天候运行，负责构建知识图谱、监控目标、生成潜在客户线索、管理你的社交媒体账号，并将结果汇报到你的仪表盘上。

整个系统编译为**单个约 32MB 的二进制文件**。安装一次，一条命令，你的智能体即可上线运行。

```bash
curl -fsSL https://openfang.sh/install | sh
openfang init
openfang start
# Dashboard live at http://localhost:4200
```

<details>
<summary><strong>Windows</strong></summary>

```powershell
irm https://openfang.sh/install.ps1 | iex
openfang init
openfang start
```

</details>

---

## Hands：真正能干活儿的智能体能力包

<p align="center"><em>"传统智能体等你输入指令。Hands 则<strong>为你工作</strong>。”</em></p>

**Hands** 是 OpenFang 的核心创新。它们是预构建的自主能力包，可独立运行、按计划执行，无需你主动提示。这并非聊天机器人。这是一个早上 6 点自动醒来、调研竞争对手、构建知识图谱、对发现内容进行评分，并在你喝完咖啡前将报告发送到 Telegram 的智能体。

每个 Hand 打包了以下内容：
- **HAND.toml**：清单文件，声明工具、设置、依赖项和仪表盘指标。
- **System Prompt**：多阶段操作手册。不是一句话提示词，而是 500+ 字的专业流程指南。
- **SKILL.md**：运行时注入上下文的领域专业知识参考文档。
- **Guardrails（安全护栏）**：敏感操作的审批关卡（例如 Browser Hand 在执行任何购买操作前必须获得批准）。

全部编译进二进制文件中。无需下载、无需 pip install、无需 Docker pull。

### 7 个内置 Hands

| Hand | 实际功能 |
|------|----------|
| **Clip** | 接收 YouTube URL，下载视频，识别精彩片段，剪辑成带字幕和缩略图的竖屏短视频，可选添加 AI 配音，并发布到 Telegram 和 WhatsApp。8 阶段流水线，集成 FFmpeg + yt-dlp + 5 个语音转文本（STT）后端。 |
| **Lead** | 每日运行。发现符合你 ICP（理想客户画像）的潜在客户，通过网络调研丰富其信息，进行 0-100 分评分，与现有数据库去重，并以 CSV/JSON/Markdown 格式交付合格线索。随时间推移自动优化 ICP 模型。 |
| **Collector** | OSINT（开源情报）级智能监控。你提供目标（公司、人物或主题），它持续监控：变更检测、情绪追踪、知识图谱构建，并在关键事件发生时发送紧急警报。 |
| **Predictor** | 超级预测引擎。从多源收集信号，构建校准推理链，输出带置信区间的预测结果，并使用 Brier 分数跟踪自身准确率。具备反共识模式，会刻意与主流观点辩论。 |
| **Researcher** | 深度自主研究员。交叉引用多个来源，使用 CRAAP 标准（时效性、相关性、权威性、准确性、目的性）评估可信度，生成带 APA 格式引用的报告，支持多语言。 |
| **Twitter** | 自主 Twitter/X 账号管理器。以 7 种轮换格式创作内容，定时发布以优化互动率，回复提及消息，跟踪性能指标。设有审批队列，未经你确认绝不自动发帖。 |
| **Browser** | Web 自动化智能体。浏览网站、填写表单、点击按钮、处理多步工作流。使用 Playwright 桥接并支持会话持久化。**强制购买审批关卡**：它绝不会在未获明确授权的情况下花费你的资金。 |

```bash
# Activate the Researcher Hand. It starts working immediately.
openfang hand activate researcher

# Check its progress anytime
openfang hand status researcher

# Activate lead generation on a daily schedule
openfang hand activate lead

# Pause without losing state
openfang hand pause lead

# See all available Hands
openfang hand list
```

**自行开发**。定义包含工具、设置和 System Prompt 的 `HAND.toml`，然后发布到 FangHub。

---

## OpenFang 与竞品对比

<p align="center">
  <img src="public/assets/openfang-vs-claws.png" width="600" alt="OpenFang vs OpenClaw vs ZeroClaw" />
</p>

### 基准测试：实测数据，非营销宣传

所有数据均来源于官方文档和公开仓库，截至 2026年2月。

#### Cold Start Time（冷启动时间，越低越好）

```
ZeroClaw   ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   10 ms
OpenFang   ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  180 ms    ★
LangGraph  █████████████████░░░░░░░░░░░░░░░░░░░░░░░░░  2.5 sec
CrewAI     ████████████████████░░░░░░░░░░░░░░░░░░░░░░  3.0 sec
AutoGen    ██████████████████████████░░░░░░░░░░░░░░░░░  4.0 sec
OpenClaw   █████████████████████████████████████████░░  5.98 sec
```

#### Idle Memory Usage（空闲内存占用，越低越好）

```
ZeroClaw   █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    5 MB
OpenFang   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   40 MB    ★
LangGraph  ██████████████████░░░░░░░░░░░░░░░░░░░░░░░░░  180 MB
CrewAI     ████████████████████░░░░░░░░░░░░░░░░░░░░░░░  200 MB
AutoGen    █████████████████████████░░░░░░░░░░░░░░░░░░  250 MB
OpenClaw   ████████████████████████████████████████░░░░  394 MB
```

#### Install Size（安装体积，越低越好）

```
ZeroClaw   █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  8.8 MB
OpenFang   ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   32 MB    ★
CrewAI     ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  100 MB
LangGraph  ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  150 MB
AutoGen    ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░  200 MB
OpenClaw   ████████████████████████████████████████░░░░  500 MB
```

#### Security Systems（安全系统数量，越高越好）

```
OpenFang   ████████████████████████████████████████████   16      ★
ZeroClaw   ███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░    6
OpenClaw   ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    3
AutoGen    █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    2
LangGraph  █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    2
CrewAI     ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    1
```

#### Channel Adapters（渠道适配器数量，越高越好）

```
OpenFang   ████████████████████████████████████████████   40      ★
ZeroClaw   ███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░   15
OpenClaw   █████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   13
CrewAI     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0
AutoGen    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0
LangGraph  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0
```

#### LLM Providers（LLM 提供商支持数，越高越好）

```
ZeroClaw   ████████████████████████████████████████████   28
OpenFang   ██████████████████████████████████████████░░   27      ★
LangGraph  ██████████████████████░░░░░░░░░░░░░░░░░░░░░   15
CrewAI     ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   10
OpenClaw   ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   10
AutoGen    ███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    8
```

### Feature-by-Feature Comparison（逐功能对比）

| Feature | OpenFang | OpenClaw | ZeroClaw | CrewAI | AutoGen | LangGraph |
|---------|----------|----------|----------|--------|---------|-----------|
| **Language** | **Rust** | TypeScript | **Rust** | Python | Python | Python |
| **Autonomous Hands** | **7 built-in** | None | None | None | None | None |
| **Security Layers** | **16 discrete** | 3 basic | 6 layers | 1 basic | Docker | AES enc. |
| **Agent Sandbox** | **WASM dual-metered** | None | Allowlists | None | Docker | None |
| **Channel Adapters** | **40** | 13 | 15 | 0 | 0 | 0 |
| **Built-in Tools** | **53 + MCP + A2A** | 50+ | 12 | Plugins | MCP | LC tools |
| **Memory** | **SQLite + vector** | File-based | SQLite FTS5 | 4-layer | External | Checkpoints |
| **Desktop App** | **Tauri 2.0** | None | None | None | Studio | None |
| **Audit Trail** | **Merkle hash-chain** | Logs | Logs | Tracing | Logs | Checkpoints |
| **Cold Start** | **<200ms** | ~6s | ~10ms | ~3s | ~4s | ~2.5s |
| **Install Size** | **~32 MB** | ~500 MB | ~8.8 MB | ~100 MB | ~200 MB | ~150 MB |
| **License** | MIT | MIT | MIT | MIT | Apache 2.0 | MIT |

---

## 16 Security Systems：纵深防御体系

OpenFang 并非事后打补丁式地添加安全性。每一层均可独立测试，且不存在单点故障风险。

| # | System | What It Does |
|---|--------|-------------|
| 1 | **WASM Dual-Metered Sandbox** | 工具代码在 WebAssembly 中运行，配备燃料计量（fuel metering）与纪元中断机制。看门狗线程会终止失控代码。 |
| 2 | **Merkle Hash-Chain Audit Trail** | 每个操作都与前一个操作密码学关联。篡改任意一条记录都会导致整条链断裂。 |
| 3 | **Information Flow Taint Tracking** | 标签在运行过程中传播，密钥从源头到终点全程可追溯。 |
| 4 | **Ed25519 Signed Agent Manifests** | 每个智能体的身份和能力集均经过密码学签名验证。 |
| 5 | **SSRF Protection** | 拦截私有 IP、云元数据端点及 DNS 重绑定攻击。 |
| 6 | **Secret Zeroization** | `Zeroizing<String>` 会在 API 密钥不再需要时立即自动擦除内存中的敏感信息。 |
| 7 | **OFP Mutual Authentication** | 基于 HMAC-SHA256 的 nonce 机制，为 P2P 网络提供恒定时间验证。 |
| 8 | **Capability Gates** | 基于角色的访问控制（RBAC）。智能体声明所需工具，内核强制校验执行权限。 |
| 9 | **Security Headers** | 每个响应均包含 CSP、X-Frame-Options、HSTS、X-Content-Type-Options 等标准安全头。 |
| 10 | **Health Endpoint Redaction** | 公开的健康检查仅返回最小化信息，完整诊断需通过身份验证。 |
| 11 | **Subprocess Sandbox** | `env_clear()` + 选择性变量透传。支持跨平台进程树隔离与强制终止。 |
| 12 | **Prompt Injection Scanner** | 检测技能文件中的覆盖尝试、数据外泄模式及 Shell 引用注入攻击。 |
| 13 | **Loop Guard** | 基于 SHA256 的工具调用环路检测，配备熔断机制，可处理乒乓交互模式。 |
| 14 | **Session Repair** | 7 阶段消息历史校验与损坏自动恢复机制。 |
| 15 | **Path Traversal Prevention** | 路径规范化并防止符号链接逃逸。`../` 在此无效。 |
| 16 | **GCRA Rate Limiter** | 成本感知的令牌桶限流器，支持按 IP 追踪与过期清理。 |

---

## Architecture（架构设计）

14 个 Rust crates。137,728 行代码。模块化内核设计。

```
openfang-kernel      Orchestration, workflows, metering, RBAC, scheduler, budget tracking
openfang-runtime     Agent loop, 3 LLM drivers, 53 tools, WASM sandbox, MCP, A2A
openfang-api         140+ REST/WS/SSE endpoints, OpenAI-compatible API, dashboard
openfang-channels    40 messaging adapters with rate limiting, DM/group policies
openfang-memory      SQLite persistence, vector embeddings, canonical sessions, compaction
openfang-types       Core types, taint tracking, Ed25519 manifest signing, model catalog
openfang-skills      60 bundled skills, SKILL.md parser, FangHub marketplace
openfang-hands       7 autonomous Hands, HAND.toml parser, lifecycle management
openfang-extensions  25 MCP templates, AES-256-GCM credential vault, OAuth2 PKCE
openfang-wire        OFP P2P protocol with HMAC-SHA256 mutual authentication
openfang-cli         CLI with daemon management, TUI dashboard, MCP server mode
openfang-desktop     Tauri 2.0 native app (system tray, notifications, global shortcuts)
openfang-migrate     OpenClaw, LangChain, AutoGPT migration engine
xtask                Build automation
```

---

## 40 Channel Adapters（渠道适配器）

将你的智能体连接到用户所在的每一个平台。

**Core：** Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Email (IMAP/SMTP)
**Enterprise：** Microsoft Teams, Mattermost, Google Chat, Webex, Feishu/Lark, Zulip
**Social：** LINE, Viber, Facebook Messenger, Mastodon, Bluesky, Reddit, LinkedIn, Twitch
**Community：** IRC, XMPP, Guilded, Revolt, Keybase, Discourse, Gitter
**Privacy：** Threema, Nostr, Mumble, Nextcloud Talk, Rocket.Chat, Ntfy, Gotify
**Workplace：** Pumble, Flock, Twist, DingTalk, Zalo, Webhooks

每个适配器均支持按渠道覆盖模型、DM/群组策略、速率限制及输出格式定制。

---

## WhatsApp Web Gateway（QR Code）

通过扫描二维码将你的个人 WhatsApp 账号接入 OpenFang，体验与 WhatsApp Web 相同的功能。无需 Meta Business 账号。

### Prerequisites（前置条件）

- **Node.js >= 18** installed ([download](https://nodejs.org/))
- OpenFang installed and initialized

### Setup（配置步骤）

**1. Install the gateway dependencies：**

```bash
cd packages/whatsapp-gateway
npm install
```

**2. Configure `config.toml`：**

```toml
[channels.whatsapp]
mode = "web"
default_agent = "assistant"
```

**3. Set the gateway URL (choose one)：**

Add to your shell profile for persistence:

```bash
# macOS / Linux
echo 'export WHATSAPP_WEB_GATEWAY_URL="http://127.0.0.1:3009"' >> ~/.zshrc
source ~/.zshrc
```

Or set it inline when starting the gateway:

```bash
export WHATSAPP_WEB_GATEWAY_URL="http://127.0.0.1:3009"
```

**4. Start the gateway：**

```bash
node packages/whatsapp-gateway/index.js
```

The gateway listens on port `3009` by default. Override with `WHATSAPP_GATEWAY_PORT`.

**5. Start OpenFang：**

```bash
openfang start
# Dashboard at http://localhost:4200
```

**6. Scan the QR code：**

Open the dashboard → **Channels** → **WhatsApp**. A QR code will appear. Scan it with your phone:

> **WhatsApp** → **Settings** → **Linked Devices** → **Link a Device**

Once scanned, the status changes to `connected` and incoming messages are routed to your configured agent.

### Gateway Environment Variables（网关环境变量）

| Variable | Description | Default |
|----------|-------------|---------|
| `WHATSAPP_WEB_GATEWAY_URL` | OpenFang 连接到的网关 URL | _(empty = disabled)_ |
| `WHATSAPP_GATEWAY_PORT` | 网关监听端口 | `3009` |
| `OPENFANG_URL` | 网关上报的 OpenFang API URL | `http://127.0.0.1:4200` |
| `OPENFANG_DEFAULT_AGENT` | 处理传入消息的 agent | `assistant` |

### Gateway API Endpoints（网关 API 端点）

| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/login/start` | Generate QR code (returns base64 PNG) |
| `GET` | `/login/status` | Connection status (`disconnected`, `qr_ready`, `connected`) |
| `POST` | `/message/send` | Send a message (`{ "to": "5511999999999", "text": "Hello" }`) |
| `GET` | `/health` | Health check |

### Alternative: WhatsApp Cloud API（替代方案）

对于生产级负载，建议使用 [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api) 配合 Meta Business 账号。详见 [Cloud API configuration docs](https://openfang.sh/docs/channels/whatsapp)。



---

## 27 LLM Providers, 123+ Models（支持 27 家提供商，123+ 模型）

3 native drivers (Anthropic, Gemini, OpenAI-compatible) route to 27 providers:

Anthropic, Gemini, OpenAI, Groq, DeepSeek, OpenRouter, Together, Mistral, Fireworks, Cohere, Perplexity, xAI, AI21, Cerebras, SambaNova, HuggingFace, Replicate, Ollama, vLLM, LM Studio, Qwen, MiniMax, Zhipu, Moonshot, Qianfan, Bedrock, and more.

Intelligent routing with task complexity scoring, automatic fallback, cost tracking, and per-model pricing.

---

## Migrate from OpenClaw（从 OpenClaw 迁移）

Already running OpenClaw? One command:

```bash
# Migrate everything: agents, memory, skills, configs.
openfang migrate --from openclaw

# Migrate from a specific path
openfang migrate --from openclaw --path ~/.openclaw

# Dry run first to see what would change
openfang migrate --from openclaw --dry-run
```

The migration engine imports your agents, conversation history, skills, and configuration. OpenFang reads SKILL.md natively and is compatible with the ClawHub marketplace.

---

## OpenAI-Compatible API（OpenAI 兼容 API）

Drop-in replacement. Point your existing tools at OpenFang:

```bash
curl -X POST localhost:4200/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "researcher",
    "messages": [{"role": "user", "content": "Analyze Q4 market trends"}],
    "stream": true
  }'
```

140+ REST/WS/SSE endpoints covering agents, memory, workflows, channels, models, skills, A2A, Hands, and more.

---

## Quick Start（快速入门）

```bash
# 1. Install (macOS/Linux)
curl -fsSL https://openfang.sh/install | sh

# 2. Initialize. Walks you through provider setup.
openfang init

# 3. Start the daemon
openfang start

# 4. Dashboard is live at http://localhost:4200

# 5. Activate a Hand. It starts working for you.
openfang hand activate researcher

# 6. Chat with an agent
openfang chat researcher
> "What are the emerging trends in AI agent frameworks?"

# 7. Spawn a pre-built agent
openfang agent spawn coder
```

<details>
<summary><strong>Windows (PowerShell)</strong></summary>

```powershell
irm https://openfang.sh/install.ps1 | iex
openfang init
openfang start
```

</details>

---

## Development（开发指南）

```bash
# Build the workspace
cargo build --workspace --lib

# Run all tests (1,767+)
cargo test --workspace

# Lint (must be 0 warnings)
cargo clippy --workspace --all-targets -- -D warnings

# Format
cargo fmt --all -- --check
```

---

## Stability Notice（稳定性声明）

OpenFang v0.5.10 is pre-1.0. The architecture is solid, the test suite is comprehensive, and the security model is deep. That said:

- **Breaking changes** may occur between minor versions until v1.0.
- **Some Hands** are more mature than others. Browser and Researcher are the most battle tested.
- **Edge cases** exist. If you find one, [open an issue](https://github.com/RightNow-AI/openfang/issues).
- **Pin to a specific commit** for production deployments until v1.0.

We ship fast and fix fast. The goal is a rock solid v1.0 by mid 2026.

---

## Security（安全报告）

To report a security vulnerability, email **jaber@rightnowai.co**. We take all reports seriously and will respond within 48 hours.

---

## License（许可证）

MIT. Use it however you want.

---

## Links（相关链接）

- [Website & Documentation](https://openfang.sh)
- [Quick Start Guide](https://openfang.sh/docs/getting-started)
- [GitHub](https://github.com/RightNow-AI/openfang)
- [Discord](https://discord.gg/sSJqgNnq6X)
- [Twitter / X](https://x.com/openfangg)

---

## Built by RightNow（RightNow 团队出品）

<p align="center">
  <a href="https://www.rightnowai.co/">
    <img src="public/assets/rightnow-logo.webp" width="60" alt="RightNow Logo" />
  </a>
</p>

<p align="center">
  OpenFang is built and maintained by <a href="https://x.com/Akashi203"><strong>Jaber</strong></a>, Founder of <a href="https://www.rightnowai.co/"><strong>RightNow</strong></a>.
</p>

<p align="center">
  <a href="https://www.rightnowai.co/">Website</a> &bull;
  <a href="https://x.com/Akashi203">Twitter / X</a> &bull;
  <a href="https://www.buymeacoffee.com/openfang" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
</p>

---

<p align="center">
  <strong>Built with Rust. Secured with 16 layers. Agents that actually work for you.</strong>
</p>