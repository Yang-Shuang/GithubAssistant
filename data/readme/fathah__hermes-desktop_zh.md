<img width="100%" alt="HERMES DESKTOP" src="previews/header.webp" />

<br/>
<p align="center">
  <a href="https://hermes-agent.nousresearch.com/docs/"><img src="https://img.shields.io/badge/Docs-hermes--agent.nousresearch.com-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://t.me/hermes_agent_desktop"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="https://github.com/fathah/hermes-desktop/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://hermesagents.cc/"><img src="https://img.shields.io/badge/Download-Releases-FF6600?style=for-the-badge" alt="Releases"></a>
<a href="https://github.com/fathah/hermes-desktop/stargazers">
  <img src="https://img.shields.io/github/stars/fathah/hermes-desktop?style=for-the-badge&color=FFD700&label=Stars" alt="Stars">
</a>
  <a href="https://github.com/fathah/hermes-desktop/releases/">
  <img src="https://img.shields.io/github/downloads/fathah/hermes-desktop/total?style=for-the-badge&color=00B496&label=Total%20Downloads" alt="Downloads">
</a>
</p>

> **本项目正在积极开发中。** 功能可能会发生变化，部分设置可能会被破坏。如果你遇到问题或有想法，请[提交 Issue](https://github.com/fathah/hermes-desktop/issues)。欢迎贡献！

## Languages

- English: `README.md`
- 简体中文: `README.zh-CN.md`
- 日本語: `README.ja-JP.md`
- 🌎 Español (LATAM): `README.es-LATAM.md`

Hermes Desktop 是一款原生桌面应用，用于安装、配置并与 [Hermes Agent](https://github.com/NousResearch/hermes-agent)（一款具备工具调用能力、跨平台消息支持和闭环学习机制的自进化 AI 助手）进行对话。

无需手动管理 CLI，该应用在一个界面中引导你完成安装、提供商配置和日常使用。它采用官方 Hermes 安装脚本，将 Hermes 存储在 `~/.hermes` 目录下，并提供用于聊天、会话、配置文件（Profile）、记忆库、技能、工具、定时任务、消息网关等的图形化界面（GUI）。

## Install

<a href="https://hermesagents.cc/"><img width="380" alt="Download Now" src="previews/download.webp" /></a>

### Windows

> **Windows 用户：** 安装包未进行代码签名。首次启动时 Windows SmartScreen 会发出警告——点击“更多信息”→“仍要运行”。

> **WSL 用户：** 如果安装程序卡在 `Switching to root user to install dependencies...`，说明 Playwright 正在等待一个没有 TTY 可供读取的 sudo 密码。请为本次安装授予免密 sudo 权限，完成后恢复原设置：
>
> ```bash
> echo "$USER ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/hermes-install
> # …re-run the installer; once it finishes:
> sudo rm /etc/sudoers.d/hermes-install
> ```
>
> Tracked in [#109](https://github.com/fathah/hermes-desktop/issues/109).

### Fedora (RPM)

```bash
sudo dnf install ./hermes-desktop-<version>.rpm
```

> **Fedora 用户：** `.rpm` 包未进行 GPG 签名。如果你的系统强制要求验证签名，请在安装命令后追加 `--nogpgcheck`。`.rpm` 构建版不支持自动更新（受限于 `electron-updater`）；请重新安装新的 `.rpm` 文件以完成更新。

## Preview

<table>
<tr>
<td width="50%" align="center"><b>Chat</b><br/><img width="100%" alt="Chat" src="previews/chat.png" /></td>
<td width="50%" align="center"><b>Profiles</b><br/><img width="100%" alt="Profiles" src="previews/profiles.png" /></td>
</tr>
<tr>
<td width="50%" align="center"><b>Models</b><br/><img width="100%" alt="Models" src="previews/models.png" /></td>
<td width="50%" align="center"><b>Providers</b><br/><img width="100%" alt="Providers" src="previews/providers.png" /></td>
</tr>
<tr>
<td width="50%" align="center"><b>Tools</b><br/><img width="100%" alt="Tools" src="previews/tools.png" /></td>
<td width="50%" align="center"><b>Skills</b><br/><img width="100%" alt="Skills" src="previews/skills.png" /></td>
</tr>
<tr>
<td width="50%" align="center"><b>Schedules</b><br/><img width="100%" alt="Schedules" src="previews/schedules.png" /></td>
<td width="50%" align="center"><b>Gateway</b><br/><img width="100%" alt="Gateway" src="previews/gateway.png" /></td>
</tr>
<tr>
<td width="50%" align="center"><b>Persona</b><br/><img width="100%" alt="Persona" src="previews/persona.png" /></td>
<td width="50%" align="center"><b>Kanban</b><br/><img width="100%" alt="Kanban" src="previews/kanban.png" /></td>
</tr>
<tr>
<td width="50%" align="center"><b>Office</b><br/><img width="100%" alt="Office" src="previews/office.png" /></td>
<td width="50%" align="center"><b>Settings</b><br/><img width="100%" alt="Settings" src="previews/settings.png" /></td>
</tr>
</table>

## Features

- **引导式首次运行安装**：带有进度跟踪和依赖解析的 Hermes Agent 安装流程
- **本地或远程后端**：可在 `127.0.0.1:8642` 上本地运行 Hermes，或通过 URL + API Key 将桌面应用连接到远程 Hermes API 服务器
- **多提供商支持**：OpenRouter、Anthropic、OpenAI、Google (Gemini)、xAI (Grok)、Nous Portal、Qwen、MiniMax、Hugging Face、Groq，以及本地 OpenAI 兼容端点（LM Studio、Atomic Chat、Ollama、vLLM、llama.cpp）
- **流式聊天界面**：支持 SSE 流传输、工具进度指示器、Markdown 渲染和语法高亮
- **Token 用量追踪**：在聊天底部实时显示提示词/补全 Token 计数与费用，并提供 `/usage` 斜杠命令
- **22 个斜杠命令**：`/new`、`/clear`、`/fast`、`/web`、`/image`、`/browse`、`/code`、`/shell`、`/usage`、`/help`、`/tools`、`/skills`、`/model`、`/memory`、`/persona`、`/version`、`/compact`、`/compress`、`/undo`、`/retry`、`/debug`、`/status` 等
- **会话管理**：支持全文搜索（SQLite FTS5）、按日期分组的历史记录，以及跨对话的恢复与搜索功能
- **配置文件切换**：创建、删除并在具有独立配置的 Hermes 环境之间切换
- **14 套工具集**：Web、浏览器、终端、文件、代码执行、视觉、图像生成、TTS、技能、记忆、会话搜索、澄清、委托、MoA 和任务规划
- **记忆系统**：查看/编辑记忆条目、用户配置文件记忆、容量追踪，以及可发现（Discoverable）的记忆提供商（Honcho、Hindsight、Mem0、RetainDB、Supermemory、ByteRover）
- **人格编辑器**：编辑并重置代理的 SOUL.md 人格设定
- **已保存模型**：跨提供商管理模型配置的增删改查（CRUD）功能
- **定时任务**：内置 Cron 作业构建器（支持分钟、每小时、每天、每周、自定义 cron），提供 15 种投递目标
- **16 个消息网关**：Telegram、Discord、Slack、WhatsApp、Signal、Matrix、Mattermost、电子邮件（IMAP/SMTP）、短信（Twilio/Vonage）、iMessage（BlueBubbles）、钉钉、飞书/Lark、企业微信、微信（iLink Bot）、Webhooks、Home Assistant
- **Hermes Office (Claw3d)**：带有开发服务器和适配器管理的可视化 3D 界面
- **备份、导入与调试转储**：通过设置界面进行完整数据备份/恢复及系统诊断
- **日志查看器**：直接从设置屏幕查看网关和代理日志
- **自动更新器**：通过 electron-updater 检查并安装更新
- **国际化就绪（i18n）**：内置国际化框架，已提供覆盖所有界面的英文本地化文件，随时准备接受社区翻译
- **测试套件**：使用 Vitest 对 SSE 解析器、IPC 处理器、预加载 API 表面、安装程序工具及常量验证进行测试

## How It Works

首次启动时，应用将执行以下操作：

1. 询问你希望本地运行 Hermes 还是连接到**远程** Hermes API 服务器。
2. **本地模式：**检查 `~/.hermes` 中是否已安装 Hermes；若未安装，则运行官方安装脚本并自动解析依赖（Git、uv、Python 3.11+）。
3. **远程模式：**提示输入远程 API URL 和 API Key，验证连接后跳过本地安装。
4. 提示选择 API 提供商或本地模型端点。
5. 通过 Hermes 配置文件保存提供商配置和 API Key。
6. 设置完成后启动主工作区。

在本地模式下，聊天请求通过 `http://127.0.0.1:8642` 进行 SSE 流传输。在远程模式下，应用使用相同的流协议与你配置的远程 URL 通信。桌面应用会实时解析数据流，并在接收时渲染工具进度、Markdown 内容和 Token 用量。

## Screens

| Screen        | Description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| **Chat**      | Streaming conversation UI with slash commands, tool progress, and token tracking      |
| **Sessions**  | Browse, search, and resume past conversations                                         |
| **Agents**    | Create, delete, and switch between Hermes profiles                                    |
| **Skills**    | Browse, install, and manage bundled and installed skills                              |
| **Models**    | Manage saved model configurations per provider                                        |
| **Memory**    | View/edit memory entries, user profile, and configure memory providers                |
| **Soul**      | Edit the active profile's persona (SOUL.md)                                           |
| **Tools**     | Enable or disable individual toolsets                                                 |
| **Schedules** | Create and manage cron jobs with delivery targets                                     |
| **Gateway**   | Configure and control messaging platform integrations                                 |
| **Office**    | Claw3d visual interface setup and management                                          |
| **Settings**  | Provider config, credential pools, backup/import, log viewer, network settings, theme |

## Supported Providers

### LLM Providers

| Provider            | Notes                                    |
| ------------------- | ---------------------------------------- |
| **OpenRouter**      | 200+ models via single API (recommended) |
| **Anthropic**       | Direct Claude access                     |
| **OpenAI**          | Direct GPT access                        |
| **Google (Gemini)** | Google AI Studio                         |
| **xAI (Grok)**      | Grok models                              |
| **Nous Portal**     | Free tier available                      |
| **Qwen**            | QwenAI models                            |
| **MiniMax**         | Global and China endpoints               |
| **Hugging Face**    | 20+ open models via HF Inference         |
| **Groq**            | Fast inference (voice/STT)               |
| **Local/Custom**    | Any OpenAI-compatible endpoint           |

Local presets are included for LM Studio, Atomic Chat, Ollama, vLLM, and llama.cpp.

### Messaging Platforms

Telegram, Discord, Slack, WhatsApp, Signal, Matrix/Element, Mattermost, Email (IMAP/SMTP), SMS (Twilio & Vonage), iMessage (BlueBubbles), DingTalk, Feishu/Lark, WeCom, WeChat (iLink Bot), Webhooks, and Home Assistant.

### Tool Integrations

Exa Search, Parallel API, Tavily, Firecrawl, FAL.ai (image generation), Honcho, Browserbase, Weights & Biases, and Tinker.

## Development

### Prerequisites

- Node.js and npm
- A Unix-like shell environment for the Hermes installer
- Network access for downloading Hermes during first-run install

### Install dependencies

```bash
npm install
```

### Start the app in development

```bash
npm run dev
```

### Run checks

```bash
npm run lint
npm run typecheck
```

### Run tests

```bash
npm run test
npm run test:watch
```

### Build the desktop app

```bash
npm run build
```

Platform packaging:

```bash
npm run build:mac
npm run build:win
npm run build:linux
npm run build:rpm    # Fedora/RHEL .rpm only
```

## First-Time Setup

When the app opens for the first time, it will either detect an existing Hermes installation or offer to install it for you.

Supported setup paths in the UI:

- `OpenRouter`
- `Anthropic`
- `OpenAI`
- `Local LLM` via an OpenAI-compatible base URL

Local presets are included for:

- LM Studio
- Atomic Chat
- Ollama
- vLLM
- llama.cpp

Hermes files are managed in:

- `~/.hermes`
- `~/.hermes/.env`
- `~/.hermes/config.yaml`
- `~/.hermes/hermes-agent`
- `~/.hermes/profiles/` — named profile directories
- `~/.hermes/state.db` — session history database
- `~/.hermes/cron/jobs.json` — scheduled tasks

## Tech Stack

- **Electron** 39 — cross-platform desktop shell
- **React** 19 — UI framework
- **TypeScript** 5.9 — type safety across main and renderer processes
- **Tailwind CSS** 4 — utility-first styling
- **Vite** 7 + electron-vite — fast dev server and build tooling
- **better-sqlite3** — local session storage with FTS5 full-text search
- **i18next** — internationalization framework
- **Vitest** — test runner

## Notes

- The desktop app depends on the upstream Hermes Agent project for agent behavior and tool execution.
- The built-in installer runs the official Hermes install script with `--skip-setup`, then completes provider configuration in the GUI.
- Local model providers do not require an API key, but the compatible server must already be running.
- Alternative npm registry routes are supported for environments with restricted network access.

## Contributing

Contributions are welcome! Check out the [Contributing Guide](CONTRIBUTING.md) to get started. If you're not sure where to begin, take a look at the [open issues](https://github.com/NousResearch/hermes-desktop/issues). Found a bug or have a feature request? [File an issue](https://github.com/NousResearch/hermes-desktop/issues/new).

## Related Project

For the core agent, docs, and CLI workflows, see the main Hermes Agent repository:

- https://github.com/NousResearch/hermes-agent