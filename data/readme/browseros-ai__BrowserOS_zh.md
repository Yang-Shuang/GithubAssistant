<div align="center">
<img width="693" height="379" alt="github-banner" src="https://github.com/user-attachments/assets/1e37941c-4dbc-4662-9c8c-3bbe9971301d" />

<br></br>
[![Discord](https://img.shields.io/badge/Discord-Join%20us-blue)](https://discord.gg/YKwjt5vuKr)
[![Slack](https://img.shields.io/badge/Slack-Join%20us-4A154B?logo=slack&logoColor=white)](https://dub.sh/browserOS-slack)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/Docs-docs.browseros.com-blue)](https://docs.browseros.com)
<br></br>
<a href="https://files.browseros.com/download/BrowserOS.dmg">
  <img src="https://img.shields.io/badge/Download-macOS-black?style=flat&logo=apple&logoColor=white" alt="Download for macOS (beta)" />
</a>
<a href="https://files.browseros.com/download/BrowserOS_installer.exe">
  <img src="https://img.shields.io/badge/Download-Windows-0078D4?style=flat&logo=windows&logoColor=white" alt="Download for Windows (beta)" />
</a>
<a href="https://files.browseros.com/download/BrowserOS.AppImage">
  <img src="https://img.shields.io/badge/Download-Linux-FCC624?style=flat&logo=linux&logoColor=black" alt="Download for Linux (beta)" />
</a>
<a href="https://cdn.browseros.com/download/BrowserOS.deb">
  <img src="https://img.shields.io/badge/Download-Debian-D70A53?style=flat&logo=debian&logoColor=white" alt="Download Debian package" />
</a>
<br /><br />

创始人 —— [@nv_sonti](https://x.com/intent/user?screen_name=nv_sonti) 和 [@ThatNithin](https://x.com/intent/user?screen_name=ThatNithin)：

[![Twitter Follow](https://img.shields.io/twitter/follow/nv_sonti?style=social)](https://x.com/intent/user?screen_name=nv_sonti)
&emsp;&emsp;&emsp;
[![Twitter Follow](https://img.shields.io/twitter/follow/ThatNithin?style=social)](https://x.com/intent/user?screen_name=ThatNithin)

</div>

BrowserOS 是一个开源的 Chromium 分支，原生运行 AI Agent（智能体）。**它是 ChatGPT Atlas、Perplexity Comet 和 Dia 的隐私优先替代方案。**

使用你自己的 API Key，或通过 Ollama 运行本地模型。你的数据绝不会离开本地设备。

> **[文档](https://docs.browseros.com)** · **[Discord](https://discord.gg/YKwjt5vuKr)** · **[Slack](https://dub.sh/browserOS-slack)** · **[Twitter](https://x.com/browserOS_ai)** · **[功能建议](https://github.com/browseros-ai/BrowserOS/issues/99)**

## 快速开始

1. **下载并安装** BrowserOS —— [macOS](https://files.browseros.com/download/BrowserOS.dmg) · [Windows](https://files.browseros.com/download/BrowserOS_installer.exe) · [Linux (AppImage)](https://files.browseros.com/download/BrowserOS.AppImage) · [Linux (Debian)](https://cdn.browseros.com/download/BrowserOS.deb)
2. **导入你的 Chrome 数据**（可选）—— 书签、密码和扩展均会一并迁移
3. **连接你的 AI 服务提供商** —— 通过 OAuth 连接 Claude、OpenAI、Gemini、ChatGPT Pro，或通过 Ollama/LM Studio 使用本地模型

## 功能特性

| 功能 | 说明 | 文档 |
|---------|-------------|------|
| **AI Agent** | 提供 50+ 浏览器自动化工具 —— 通过自然语言进行导航、点击、输入和提取数据 | [指南](https://docs.browseros.com/getting-started) |
| **MCP Server** | 从 Claude Code、Gemini CLI 或任何 MCP 客户端控制浏览器 | [设置](https://docs.browseros.com/features/use-with-claude-code) |
| **Workflows（工作流）** | 使用可视化图构建器创建可重复的浏览器自动化流程 | [文档](https://docs.browseros.com/features/workflows) |
| **Cowork** | 将浏览器自动化与本地文件操作相结合 —— 搜索网页并将报告保存到文件夹中 | [文档](https://docs.browseros.com/features/cowork) |
| **Scheduled Tasks（定时任务）** | 让 Agent 自动运行 —— 支持每日、每小时或每隔几分钟执行一次 | [文档](https://docs.browseros.com/features/scheduled-tasks) |
| **Memory（记忆）** | 跨对话持久化记忆 —— 你的助手会随时间推移记住上下文信息 | [文档](https://docs.browseros.com/features/memory) |
| **SOUL.md** | 在单个 Markdown 文件中定义 AI 的性格与指令 | [文档](https://docs.browseros.com/features/soul-md) |
| **LLM Hub（大模型中心）** | 在任何页面上并排比较 Claude、ChatGPT 和 Gemini 的回复 | [文档](https://docs.browseros.com/features/llm-chat-hub) |
| **40+ App Integrations（应用集成）** | 通过 MCP 连接 Gmail、Slack、GitHub、Linear、Notion、Figma、Salesforce 等更多应用 | [文档](https://docs.browseros.com/features/connect-apps) |
| **Vertical Tabs（垂直标签页）** | 侧栏标签页管理 —— 即使打开 100+ 个标签页也能保持井井有条 | [文档](https://docs.browseros.com/features/vertical-tabs) |
| **Ad Blocking（广告拦截）** | 支持 uBlock Origin + Manifest V2 —— [提供比 Chrome 多 10 倍的保护](https://docs.browseros.com/features/ad-blocking) | [文档](https://docs.browseros.com/features/ad-blocking) |
| **Cloud Sync（云同步）** | 跨设备同步浏览器配置与 Agent 历史记录 | [文档](https://docs.browseros.com/features/sync) |
| **Skills（技能）** | 自定义指令集，塑造你的 AI 助手的行为方式 | [文档](https://docs.browseros.com/features/skills) |
| **Smart Nudges（智能提示）** | 上下文相关的建议，在恰当时机推荐连接应用或使用功能 | [文档](https://docs.browseros.com/features/smart-nudges) |

## 演示

### BrowserOS Agent 实际运行效果
[![BrowserOS agent in action](docs/videos/browserOS-agent-in-action.gif)](https://www.youtube.com/watch?v=SoSFev5R5dI)
<br/><br/>

### 安装 [BrowserOS as MCP](https://docs.browseros.com/features/use-with-claude-code) 并通过 `claude-code` 控制它

https://github.com/user-attachments/assets/c725d6df-1a0d-40eb-a125-ea009bf664dc

<br/><br/>

### 使用 BrowserOS 进行对话

https://github.com/user-attachments/assets/726803c5-8e36-420e-8694-c63a2607beca

<br/><br/>

### 使用 BrowserOS 抓取数据

https://github.com/user-attachments/assets/9f038216-bc24-4555-abf1-af2adcb7ebc0

<br/><br/>

## 安装 `browseros-cli`

通过终端或像 Claude Code 这样的 AI 编程 Agent，使用 `browseros-cli` 启动和控制 BrowserOS。

**macOS / Linux：**

```bash
curl -fsSL https://cdn.browseros.com/cli/install.sh | bash
```

**Windows：**

```powershell
irm https://cdn.browseros.com/cli/install.ps1 | iex
```

安装完成后，运行 `browseros-cli init` 将 CLI 连接到正在运行的 BrowserOS 实例。

## LLM（大语言模型）提供商

BrowserOS 兼容任意 LLM。你可以自带 API Key、使用 OAuth，或在本地运行模型。

| 提供商 | 类型 | 认证方式 |
|----------|------|------|
| Kimi K2.5 | 云端（默认） | 内置 |
| ChatGPT Pro/Plus | 云端 | [OAuth](https://docs.browseros.com/features/chatgpt) |
| GitHub Copilot | 云端 | [OAuth](https://docs.browseros.com/features/github-copilot) |
| Qwen Code | 云端 | [OAuth](https://docs.browseros.com/features/qwen-code) |
| Claude (Anthropic) | 云端 | API Key |
| GPT-4o / o3 (OpenAI) | 云端 | API Key |
| Gemini (Google) | 云端 | API Key |
| Azure OpenAI | 云端 | API Key |
| AWS Bedrock | 云端 | IAM 凭证 |
| OpenRouter | 云端 | API Key |
| Ollama | 本地 | [设置](https://docs.browseros.com/features/ollama) |
| LM Studio | 本地 | [设置](https://docs.browseros.com/features/lm-studio) |

## 功能对比

| | BrowserOS | Chrome | Brave | Dia | Comet | Atlas |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 开源 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| AI Agent（智能体） | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |
| MCP Server | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 可视化工作流 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Cowork（文件+浏览器） | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 定时任务 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 自带 API Key | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 本地模型（Ollama） | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 隐私优先（本地优先） | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 广告拦截（MV2） | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |

**详细对比：**
- [BrowserOS vs Chrome DevTools MCP](https://docs.browseros.com/comparisons/chrome-devtools-mcp) —— 面向开发者的浏览器自动化功能对比
- [BrowserOS vs Claude Cowork](https://docs.browseros.com/comparisons/claude-cowork) —— 利用 AI 高效完成实际工作
- [BrowserOS vs OpenClaw](https://docs.browseros.com/comparisons/openclaw) —— 日常 AI 辅助工具

## 架构设计

BrowserOS 是一个 Monorepo（单体仓库），包含两个主要子系统：**浏览器**（Chromium 分支）和 **Agent 平台**（基于 TypeScript/Go）。

```
BrowserOS/
├── packages/browseros/              # Chromium fork + build system (Python)
│   ├── chromium_patches/            # Patches applied to Chromium source
│   ├── build/                       # Build CLI and modules
│   └── resources/                   # Icons, entitlements, signing
│
├── packages/browseros-agent/        # Agent platform (TypeScript/Go)
│   ├── apps/
│   │   ├── server/                  # MCP server + AI agent loop (Bun)
│   │   ├── agent/                   # Browser extension UI (WXT + React)
│   │   ├── cli/                     # CLI tool (Go)
│   │   ├── eval/                    # Benchmark framework
│   │   └── controller-ext/          # Chrome API bridge extension
│   │
│   └── packages/
│       ├── agent-sdk/               # Node.js SDK (npm: @browseros-ai/agent-sdk)
│       ├── cdp-protocol/            # CDP type bindings
│       └── shared/                  # Shared constants
```

| 包名 | 功能说明 |
|---------|-------------|
| [`packages/browseros`](packages/browseros/) | Chromium 分支 —— 补丁、构建系统、代码签名 |
| [`apps/server`](packages/browseros-agent/apps/server/) | Bun 服务器，提供 50+ MCP 工具并运行 AI Agent 循环 |
| [`apps/agent`](packages/browseros-agent/apps/agent/) | 浏览器扩展 —— 新标签页、侧栏对话、引导流程、设置 |
| [`apps/cli`](packages/browseros-agent/apps/cli/) | Go CLI —— 从终端或 AI 编程 Agent 控制 BrowserOS |
| [`apps/eval`](packages/browseros-agent/apps/eval/) | 基准测试框架 —— WebVoyager、Mind2Web 评估 |
| [`agent-sdk`](packages/browseros-agent/packages/agent-sdk/) | Node.js SDK，用于通过自然语言进行浏览器自动化 |
| [`cdp-protocol`](packages/browseros-agent/packages/cdp-protocol/) | 类型安全的 Chrome DevTools Protocol 绑定 |

## 贡献指南

我们非常欢迎你的帮助，共同让 BrowserOS 变得更好！详情请参阅我们的[贡献指南](CONTRIBUTING.md)。

- [报告问题](https://github.com/browseros-ai/BrowserOS/issues)
- [建议功能](https://github.com/browseros-ai/BrowserOS/issues/99)
- [加入 Discord](https://discord.gg/YKwjt5vuKr) · [加入 Slack](https://dub.sh/browserOS-slack)
- [关注 Twitter](https://x.com/browserOS_ai)

**Agent 开发**（TypeScript/Go）—— 请参阅 [agent monorepo README](packages/browseros-agent/README.md) 获取设置说明。

**浏览器开发**（C++/Python）—— 需要约 100GB 磁盘空间。请参阅 [`packages/browseros`](packages/browseros/) 获取构建说明。

## 鸣谢

- [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium) —— BrowserOS 使用了部分补丁以增强隐私保护。感谢该项目背后的每一位贡献者！
- [The Chromium Project](https://www.chromium.org/) —— 作为 BrowserOS 的核心基础，使其得以存在。

## 引用

如果你在研究或项目中使用了 BrowserOS，请引用：

```bibtex
@software{browseros2025,
  author = {Nithin Sonti and Nikhil Sonti and {BrowserOS-team}},
  title = {BrowserOS: The open-source Agentic browser},
  url = {https://github.com/browseros-ai/BrowserOS},
  year = {2025},
  publisher = {GitHub},
  license = {AGPL-3.0},
}
```

## 许可证

BrowserOS 基于 [AGPL-3.0 许可证](LICENSE) 开源。

Copyright &copy; 2026 Felafax, Inc.

## Star 数量（支持者）

感谢所有支持我们的朋友！

[![Star History Chart](https://api.star-history.com/svg?repos=browseros-ai/BrowserOS&type=Date)](https://www.star-history.com/#browseros-ai/BrowserOS&Date)

<p align="center">
Built with ❤️ from San Francisco
</p>