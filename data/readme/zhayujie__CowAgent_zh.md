<p align="center"><img src="https://github.com/user-attachments/assets/eca9a9ec-8534-4615-9e0f-96c5ac1d10a3" alt="CowAgent" width="420" /></p>

<p align="center">
  <a href="https://github.com/zhayujie/CowAgent/releases/latest"><img src="https://img.shields.io/github/v/release/zhayujie/CowAgent" alt="Latest release"></a>
  <a href="https://github.com/zhayujie/CowAgent/blob/master/LICENSE"><img src="https://img.shields.io/github/license/zhayujie/CowAgent" alt="License: MIT"></a>
  <a href="https://github.com/zhayujie/CowAgent"><img src="https://img.shields.io/github/stars/zhayujie/CowAgent?style=flat-square" alt="Stars"></a> <br/>
  [English] | [<a href="docs/zh/README.md">中文</a>] | [<a href="docs/ja/README.md">日本語</a>]
</p>

**CowAgent** 是一款开源的超级 AI 助手，能够主动规划任务、控制你的计算机和外部服务、创建并运行技能（Skills），并通过个人知识库与长期记忆与你共同成长——它是 Agent Harness 工程的参考实现。

CowAgent 轻量、易于部署且高度可扩展。接入任意主流大语言模型（LLM）提供商，即可在个人电脑或服务器上全天候运行，覆盖网页及所有主流即时通讯平台。

<p align="center">
  <a href="https://cowagent.ai/">🌐 Website</a> &nbsp;·&nbsp;
  <a href="https://docs.cowagent.ai/intro/index">📖 Docs</a> &nbsp;·&nbsp;
  <a href="https://docs.cowagent.ai/guide/quick-start">🚀 Quick Start</a> &nbsp;·&nbsp;
  <a href="https://skills.cowagent.ai/">🧩 Skill Hub</a> &nbsp;·&nbsp;
  <a href="https://link-ai.tech/cowagent/create">☁️ Try Online</a>
</p>

<br/>

## 🌟 Highlights

| Capability | Description |
| :--- | :--- |
| [Planning](https://docs.cowagent.ai/intro/architecture) | 将复杂任务拆解为步骤并逐步执行，循环调用工具直至达成目标 |
| [Memory](https://docs.cowagent.ai/memory/index) | 三层架构（上下文 → 日常 → 核心），自动进行 Deep Dream 提炼，采用关键词与向量混合检索 |
| [Knowledge](https://docs.cowagent.ai/knowledge/index) | 自动将结构化知识整理为 Markdown Wiki，构建可演化的知识图谱并支持可视化浏览 |
| [Skills](https://docs.cowagent.ai/skills/index) | 一键安装来自 [Skill Hub](https://skills.cowagent.ai/)、GitHub、ClawHub 的技能；或通过自然语言对话创建自定义技能 |
| [Tools](https://docs.cowagent.ai/tools/index) | 内置文件读写、终端、浏览器、调度器、记忆检索、网页搜索等 10+ 种工具——原生支持 MCP 集成 |
| [Channels](https://docs.cowagent.ai/channels/index) | 接入网页端、微信、飞书、钉钉、企业微信、QQ、公众号、Telegram 和 Slack |
| Multimodal | 原生支持文本、图片、语音与文件——涵盖识别、生成与发送能力 |
| [Models](https://docs.cowagent.ai/models/index) | Claude、GPT、Gemini、DeepSeek、Qwen、GLM、Kimi、MiniMax、Doubao 等——通过网页控制台一键切换提供商 |
| [Deploy](https://docs.cowagent.ai/guide/quick-start) | 一行命令安装，统一网页控制台，支持多种部署模式（本地、Docker、服务器） |

<br/>

## 🏗️ Architecture

<img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/architecture/en/architecture.jpg" alt="CowAgent Architecture" width="750"/>

CowAgent 是一个完整的 **Agent Harness**：消息通过 **Channels（渠道）** 流入；**Agent Core（智能体核心）** 基于记忆、知识库及可用工具与技能进行规划与推理；**Models（模型）** 生成回复，再通过原始渠道发送回去。每一层均解耦且可独立扩展。

详见 [Architecture](https://docs.cowagent.ai/intro/architecture)。

<br/>

## 🚀 Quick Start

一行命令安装脚本会自动处理依赖、配置与启动：

**Linux / macOS:**

```bash
bash <(curl -fsSL https://cdn.link-ai.tech/code/cow/run.sh)
```

**Windows (PowerShell):**

```powershell
irm https://cdn.link-ai.tech/code/cow/run.ps1 | iex
```

**Docker:**

```bash
curl -O https://cdn.link-ai.tech/code/cow/docker-compose.yml
docker compose up -d
```

启动后，访问 `http://localhost:9899` 即可打开 **Web console（网页控制台）**——这是你与智能体对话、配置模型、接入渠道和安装技能的统一入口。

> Deploying on a server? Set `web_host` to `0.0.0.0` in `config.json` to make the console reachable from outside, and set `web_password` to protect it. Don't forget to open port `9899` in your firewall or security group.
> 部署在服务器上？请在 `config.json` 中将 `web_host` 设置为 `0.0.0.0` 以便外部访问，并设置 `web_password` 进行密码保护。别忘了在防火墙或安全组中放行 `9899` 端口。

> 📖 Detailed guides: [Quick Start](https://docs.cowagent.ai/guide/quick-start) · [Install from Source](https://docs.cowagent.ai/guide/manual-install) · [Upgrade](https://docs.cowagent.ai/guide/upgrade)
> 📖 详细指南：[快速开始](https://docs.cowagent.ai/guide/quick-start) · [源码安装](https://docs.cowagent.ai/guide/manual-install) · [版本升级](https://docs.cowagent.ai/guide/upgrade)

安装完成后，可通过 [cow CLI](https://docs.cowagent.ai/cli/index) 管理服务：

```bash
cow start | stop | restart        # service control
cow status | logs                  # status and logs
cow update                         # pull latest code and restart
cow skill install <name>           # install a skill
cow install-browser                # install browser automation
```

<br/>

## 🤖 Models

CowAgent 支持所有主流大语言模型（LLM）提供商。**Chat、Vision、Image Gen、ASR/TTS 和 Embedding** 均可路由至不同的厂商。提供商配置直接在网页控制台中完成，无需手动编辑文件。

| Provider | Featured Models | Chat | Vision | Image Gen | ASR | TTS | Embedding |
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: |
| [Claude](https://docs.cowagent.ai/models/claude) | claude-opus-4-8 | ✅ | ✅ | | | | |
| [OpenAI](https://docs.cowagent.ai/models/openai) | gpt-5.5, o-series | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Gemini](https://docs.cowagent.ai/models/gemini) | gemini-3.5-flash | ✅ | ✅ | ✅ | | | |
| [DeepSeek](https://docs.cowagent.ai/models/deepseek) | deepseek-v4-flash / pro | ✅ | | | | | |
| [Qwen](https://docs.cowagent.ai/models/qwen) | qwen3.7-plus | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [GLM](https://docs.cowagent.ai/models/glm) | glm-5.1, glm-5v-turbo | ✅ | ✅ | | ✅ | | ✅ |
| [Doubao](https://docs.cowagent.ai/models/doubao) | doubao-seed-2.0 series | ✅ | ✅ | ✅ | | | ✅ |
| [Kimi](https://docs.cowagent.ai/models/kimi) | kimi-k2.6 | ✅ | ✅ | | | | |
| [MiniMax](https://docs.cowagent.ai/models/minimax) | MiniMax-M3 | ✅ | ✅ | ✅ | | ✅ | |
| [ERNIE](https://docs.cowagent.ai/models/qianfan) | ernie-5.1 | ✅ | ✅ | | | | |
| [MiMo](https://docs.cowagent.ai/models/mimo) | mimo-v2.5 / pro | ✅ | ✅ | | | ✅ | |
| [LinkAI](https://docs.cowagent.ai/models/linkai) | One key for 100+ models | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Custom](https://docs.cowagent.ai/models/custom) | Local models / third-party proxy | ✅ | | | | | |

> For details on each provider, see the [Models overview](https://docs.cowagent.ai/models/index).
> 各提供商详细配置说明，请参阅 [Models overview（模型总览）](https://docs.cowagent.ai/models/index)。

<br/>

## 💬 Channels

A single Agent instance can serve multiple channels in parallel. Most channels can be onboarded right from the Web console.

| Channel | Text | Image | File | Voice | Group |
| --- | :-: | :-: | :-: | :-: | :-: |
| [Web Console](https://docs.cowagent.ai/channels/web) (default) | ✅ | ✅ | ✅ | ✅ | |
| [Telegram](https://docs.cowagent.ai/channels/telegram) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Slack](https://docs.cowagent.ai/channels/slack) | ✅ | ✅ | ✅ | | ✅ |
| [Discord](https://docs.cowagent.ai/channels/discord) | ✅ | ✅ | ✅ | | ✅ |
| [WeChat](https://docs.cowagent.ai/channels/weixin) | ✅ | ✅ | ✅ | ✅ | |
| [Feishu / Lark](https://docs.cowagent.ai/channels/feishu) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [DingTalk](https://docs.cowagent.ai/channels/dingtalk) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [WeCom Bot](https://docs.cowagent.ai/channels/wecom-bot) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [QQ](https://docs.cowagent.ai/channels/qq) | ✅ | ✅ | ✅ | | ✅ |
| [WeCom App](https://docs.cowagent.ai/channels/wecom) | ✅ | ✅ | ✅ | ✅ | |
| [WeChat Customer Service](https://docs.cowagent.ai/channels/wechat-kf) | ✅ | ✅ | ✅ | ✅ | |
| [WeChat Official Account](https://docs.cowagent.ai/channels/wechatmp) | ✅ | ✅ | | ✅ | |

> See the [Channels overview](https://docs.cowagent.ai/channels/index) for setup details.
> 渠道接入详细步骤，请参阅 [Channels overview（渠道总览）](https://docs.cowagent.ai/channels/index)。

<img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/screenshots/en/web-console-chat.png" alt="CowAgent Web Console" width="800"/>

*The Web console is the default channel and the unified entry point to configure models, channels, skills, memory, and more.*
*网页控制台为默认渠道，也是配置模型、渠道、技能、记忆等的统一入口。*

<br/>

## 🧠 Memory & Knowledge Base

**Long-term memory（长期记忆）** uses a three-tier architecture: conversation context (short-term) → daily memory (mid-term) → MEMORY.md (long-term). A nightly **Deep Dream** pass distills scattered memories into refined long-term entries and a narrative journal. See [Long-term Memory](https://docs.cowagent.ai/memory/index) · [Deep Dream](https://docs.cowagent.ai/memory/deep-dream).

**Personal knowledge base（个人知识库）** complements the time-ordered memory by organizing structured knowledge **by topic**. The Agent automatically curates valuable information from conversations, maintains cross-references and indexes, and the Web console offers an interactive knowledge-graph view. See [Personal Knowledge Base](https://docs.cowagent.ai/knowledge/index).

<table>
  <tr>
    <td width="50%">
      <img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/screenshots/en/web-console-memory.png" alt="Long-term Memory" />
      <p align="center"><em>长期记忆 · 三层架构 + Deep Dream</em></p>
    </td>
    <td width="50%">
      <img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/screenshots/en/web-console-knowledge.png" alt="Personal Knowledge Base" />
      <p align="center"><em>知识库 · 自动整理的 Markdown Wiki</em></p>
    </td>
  </tr>
</table>

<br/>

## 🔧 Tools & Skills

**Tools（工具）** are atomic capabilities the Agent uses to interact with system resources. **Skills（技能）** are higher-level workflows defined by a manifest file that compose multiple tools to accomplish complex tasks.

### Tool System

**Built-in tools（内置工具）** cover file I/O (`read` / `write` / `edit` / `ls`), terminal (`bash`), file sending (`send`), memory retrieval (`memory`), environment variables (`env_config`), web fetching (`web_fetch`), scheduling (`scheduler`), web search (`web_search`), vision (`vision`), and browser automation (`browser`).

**MCP protocol（模型上下文协议）** integrates the open ecosystem of [Model Context Protocol](https://modelcontextprotocol.io) servers. A single `mcp.json` is enough — supports stdio / SSE transports, hot reload, and zero-code integration.

Learn more: [Tools overview](https://docs.cowagent.ai/tools/index) · [MCP integration](https://docs.cowagent.ai/tools/mcp).
了解更多：[工具总览](https://docs.cowagent.ai/tools/index) · [MCP 集成](https://docs.cowagent.ai/tools/mcp)。

### Skills System

- **[Skill Hub（技能中心）]** — open skill marketplace: browse, search, install in one click
- **GitHub / ClawHub / URL and more** — install skills from any source
- **Conversational authoring（对话式开发）** — generate custom skills through dialogue with `skill-creator`; turn any workflow or third-party API into a reusable skill

```bash
/skill list                   # list installed skills
/skill search <keyword>        # search the marketplace
/skill install <name>          # one-click install
```

Learn more: [Skills overview](https://docs.cowagent.ai/skills/index) · [Creating Skills](https://docs.cowagent.ai/skills/create).
了解更多：[技能总览](https://docs.cowagent.ai/skills/index) · [创建技能](https://docs.cowagent.ai/skills/create)。

<br/>

## 🏷 Changelog

> **2026.06.01：** [v2.1.0](https://github.com/zhayujie/CowAgent/releases/tag/2.1.0) —— 新增国际化支持，接入新渠道（Telegram、Discord、Slack、微信客服），CLI 交互升级，精简一行命令安装流程，支持 MCP Streamable HTTP，新增模型（claude-opus-4-8、MiMo）。

> **2026.05.22：** [v2.0.9](https://github.com/zhayujie/CowAgent/releases/tag/2.0.9) —— 模型管理功能，MCP 协议支持，持久化浏览器会话，新增模型（gpt-5.5、gemini-3.5-flash、qwen3.7-max），部署安全加固。

> **2026.05.06：** [v2.0.8](https://github.com/zhayujie/CowAgent/releases/tag/2.0.8) —— 飞书渠道重构（语音支持、流式输出、扫码接入），DeepSeek V4 与百度千帆支持，调度器工具升级。

> **2026.04.22：** [v2.0.7](https://github.com/zhayujie/CowAgent/releases/tag/2.0.7) —— 内置图像生成（GPT Image 2、Nano Banana），新增模型（Kimi K2.6、Claude Opus 4.7、GLM 5.1），记忆与知识库功能增强。

> **2026.04.14：** [v2.0.6](https://github.com/zhayujie/CowAgent/releases/tag/2.0.6) —— 个人知识库上线，Deep Dream 记忆提炼，智能上下文压缩，多会话网页控制台。

> **2026.04.01：** [v2.0.5](https://github.com/zhayujie/CowAgent/releases/tag/2.0.5) —— Cow CLI 命令行工具开源，Skill Hub 开放，浏览器自动化工具，企业微信 Bot 扫码接入。

> **2026.02.03：** [v2.0.0](https://github.com/zhayujie/CowAgent/releases/tag/2.0.0) —— 重大升级：支持多步任务规划、长期记忆与 Skills 框架的超级智能体助手。

Full history: [Release Notes](https://docs.cowagent.ai/releases/overview)
完整更新记录：[Release Notes（版本说明）](https://docs.cowagent.ai/releases/overview)

<br/>

## 🤝 Community & Support

[File an issue](https://github.com/zhayujie/CowAgent/issues) on GitHub, or scan the QR code below to join our WeChat community:
在 GitHub 上[提交 Issue](https://github.com/zhayujie/CowAgent/issues)，或扫描下方二维码加入我们的微信社区：

<img width="130" src="https://img-1317903499.cos.ap-guangzhou.myqcloud.com/docs/open-community.png">

<br/>

## 🔗 Related Projects

- **[Cow Skill Hub（技能中心）]** — open skill marketplace for AI Agents; works with CowAgent, OpenClaw, Claude Code, and more
  —— 面向 AI 智能体的开放技能市场；兼容 CowAgent、OpenClaw、Claude Code 等项目
- **[bot-on-anything]** — lightweight LLM application framework with integrations for Slack, Telegram, Discord, Gmail, and more
  —— 轻量级大语言模型（LLM）应用框架，集成 Slack、Telegram、Discord、Gmail 等渠道
- **[AgentMesh]** — open-source multi-agent framework for solving complex problems through team collaboration
  —— 开源多智能体协作框架，通过团队协同解决复杂问题

<br/>

## 🏢 Enterprise Services

[**LinkAI（https://link-ai.tech/）**](https://link-ai.tech/) is an all-in-one AI Agent platform for enterprises and developers, offering managed hosting and enterprise-grade support for CowAgent:
[**LinkAI**](https://link-ai.tech/) 是面向企业与开发者的全栈 AI 智能体平台，为 CowAgent 提供托管运行与企业级技术支持：

- **🚀 Zero-deployment hosted runtime（免部署托管环境）** — spin up a [CowAgent online assistant](https://link-ai.tech/cowagent/create) in under a minute, no server required
  —— 1分钟内即可启动 [CowAgent 在线助手](https://link-ai.tech/cowagent/create)，无需自备服务器
- **🧠 Agent infrastructure（智能体基础设施）** — unified access to LLMs, knowledge bases, databases, skills, and workflows; plug-and-play building blocks that extend what CowAgent can do
  —— 统一接入大语言模型、知识库、数据库、技能与工作流；提供即插即用模块，扩展 CowAgent 的能力边界
- **🏢 Team & enterprise features（团队与企业功能）** — workspaces, role-based access, audit logs, and private deployment for production use cases
  —— 支持工作区、基于角色的访问控制、审计日志及生产环境私有化部署

For enterprise inquiries: sales@simple-future.tech or [scan the QR code](https://cdn.link-ai.tech/consultant.jpg) to reach our team on WeChat.
企业咨询请联系：sales@simple-future.tech，或[扫描二维码](https://cdn.link-ai.tech/consultant.jpg)通过微信联系我们的团队。

<br/>

## 🛠️ Development & Contributing

All kinds of contributions are welcome — new features, bug fixes, performance improvements, docs, or sharing your own skills on the [Skill Hub（技能中心）](https://skills.cowagent.ai/submit). See [CONTRIBUTING.md](/CONTRIBUTING.md) to get started, then open an Issue to discuss or send a PR directly.
欢迎任何形式的贡献——新功能开发、Bug 修复、性能优化、文档完善，或在 [Skill Hub（技能中心）](https://skills.cowagent.ai/submit) 分享你的自定义技能。请参阅 [CONTRIBUTING.md](/CONTRIBUTING.md) 了解参与方式，随后可提交 Issue 讨论或直接发送 PR。

⭐ Star the project to show your support, and Watch → Custom → Releases to get notified of new versions. PRs and Issues are always welcome.
⭐ 给项目点个 Star 表示支持，并设置 `Watch` → `Custom` → `Releases` 以获取新版本通知。我们随时欢迎提交 PR 和 Issue。

## 🌟 Contributors

![cow contributors](https://contrib.rocks/image?repo=zhayujie/CowAgent&max=1000)

<br/>

## ⚠️ Disclaimer

1. This project is licensed under the [MIT License（麻省理工学院许可证）](/LICENSE) and is intended for technical research and learning. You are responsible for complying with applicable laws and regulations in your jurisdiction; the maintainers assume no liability for any consequences arising from use of this project.
2. **Cost & safety（成本与安全）**：Agent mode consumes substantially more tokens than regular chat — pick models that balance quality and cost. The Agent has access to your local operating system, so only deploy it in trusted environments.
3. CowAgent is a pure open-source project and does not participate in, authorize, or issue any cryptocurrency.

<br/>

## 📌 Project Renaming Notice

This project was previously named `chatgpt-on-wechat` and is now officially **CowAgent**. The old GitHub URL redirects automatically; existing users may optionally run `git remote set-url origin https://github.com/zhayujie/CowAgent.git` to update the local remote.
本项目原名为 `chatgpt-on-wechat`，现已正式更名为 **CowAgent**。旧的 GitHub 链接会自动重定向；现有用户可选择运行 `git remote set-url origin https://github.com/zhayujie/CowAgent.git` 更新本地远程仓库地址。