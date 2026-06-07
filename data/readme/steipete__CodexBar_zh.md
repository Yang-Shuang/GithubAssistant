# CodexBar 🎚️ — 愿你的 Token 永不耗尽。

> 所有 AI 编码服务的额度限制，尽在菜单栏中。

[![Latest release](https://img.shields.io/github/v/release/steipete/CodexBar?style=flat-square&color=0a0a0c)](https://github.com/steipete/CodexBar/releases/latest)
[![macOS 14+](https://img.shields.io/badge/macOS-14%2B-0a0a0c?style=flat-square)](https://github.com/steipete/CodexBar/releases/latest)
[![Homebrew](https://img.shields.io/badge/brew-steipete%2Ftap%2Fcodexbar-orange?style=flat-square)](https://github.com/steipete/homebrew-tap)
[![AUR](https://img.shields.io/aur/version/codexbar-cli?style=flat-square&color=1793d1)](https://aur.archlinux.org/packages/codexbar-cli)
[![License: MIT](https://img.shields.io/badge/license-MIT-6e5aff?style=flat-square)](LICENSE)
[![Site](https://img.shields.io/badge/site-codexbar.app-16d3b4?style=flat-square)](https://codexbar.app)

<a href="https://codexbar.app"><img src="docs/social.png" alt="CodexBar — every AI coding limit in your menu bar. 40+ providers." width="100%" /></a>

一款适用于 macOS 14+ 的轻量菜单栏应用，让你**始终掌握 AI 编码服务的额度限制**，并显示各服务额度的重置时间。支持 Codex、OpenAI、Claude、Cursor、Gemini、Copilot、Grok、GroqCloud、ElevenLabs、Deepgram、z.ai、MiniMax、Kiro、Vertex AI、Augment、OpenRouter、LLM Proxy、Codebuff、Command Code、AWS Bedrock 以及众多新兴编码服务。每个服务对应一个状态项，或启用“合并图标”模式配合切换器使用。无 Dock 栏图标，界面极简，支持动态菜单栏图标。

<img src="codexbar.png" alt="CodexBar menu popover with provider tiles, usage bars, and reset countdowns" width="520" />

## 核心优势
- **围绕重置周期规划任务。** 针对各服务提供会话、周和月度额度窗口，并显示距离下次重置的倒计时——再也不用纠结是否该开始耗时较长的任务。
- **余额、消费与成本扫描。** 查看信用额度余额、Admin API 支出面板、服务商计费摘要，以及当底层数据源提供足够详细信息时的本地成本扫描。
- **实时状态监控。** 轮询服务状态，在菜单中显示故障徽章（incident badges），并在菜单栏图标上叠加指示器。
- **隐私优先。** 复用现有的服务商会话（OAuth、设备验证流程 Device Flow、API Key、浏览器 Cookie、本地文件），因此不会存储任何密码。

## 安装方式

### 系统要求
- macOS 14+ (Sonoma)

### GitHub Release 版本
下载链接：<https://github.com/steipete/CodexBar/releases>

### Homebrew
```bash
brew install --cask codexbar
```

### CLI 压缩包（macOS / Linux）
Homebrew 公式（目前支持 Linux）：
```bash
brew install steipete/tap/codexbar
```
Arch Linux AUR 包：
```bash
yay -S codexbar-cli
```
或从 GitHub Release 页面下载压缩包：
- macOS: `CodexBarCLI-v<tag>-macos-arm64.tar.gz`, `CodexBarCLI-v<tag>-macos-x86_64.tar.gz`
- Linux: `CodexBarCLI-v<tag>-linux-aarch64.tar.gz`, `CodexBarCLI-v<tag>-linux-x86_64.tar.gz`

### 首次运行
- 打开设置（Settings）→ 服务商（Providers），启用你需要的服务。
- 安装或登录你所依赖的服务商数据源：根据具体服务，支持 CLI、浏览器会话、OAuth/设备验证流程、API Key、本地应用文件或服务商客户端。
- 可选：设置（Settings）→ 服务商（Providers）→ Codex → OpenAI Cookie（自动或手动），以获取仪表盘额外功能。

### 通过 CLI 设置 API Key
服务开关和 API Key 存储在 `~/.codexbar/config.json` 中。你可以编写脚本，使用与“设置 → 服务商”相同的配置列表：

```bash
codexbar config providers
codexbar config enable --provider grok
codexbar config disable --provider cursor
```

对于基于 API Key 的服务，无需打开设置界面即可存储密钥：

```bash
printf '%s' "$ELEVENLABS_API_KEY" | codexbar config set-api-key --provider elevenlabs --stdin
```

`set-api-key` 命令会去除管道输入值的空白字符，以严格的文件权限存储密钥，并默认启用该服务。若只需保存密钥而不启用服务，请使用 `--no-enable`；对于一次性本地脚本且无需担心 Shell 历史记录的情况，可使用 `--api-key <key>`。
完整流程请参阅 [CLI 配置文档](docs/cli-configuration.md)。

## 支持的服务
- [Codex](docs/codex.md) — OAuth API 或本地 Codex CLI，并可选添加 OpenAI Web 仪表盘扩展功能。
- [OpenAI](docs/openai.md) — Admin API Key 用量/成本图表，支持旧版信用额度余额回退机制。
- [Claude](docs/claude.md) — OAuth API、浏览器 Cookie 或 CLI PTY 回退；在可用时显示会话和周度用量。
- [Cursor](docs/cursor.md) — 浏览器 Session Cookie，用于获取计划、用量及计费重置信息。
- [OpenCode](docs/opencode.md) — 浏览器 Cookie，用于工作区订阅用量统计。
- [OpenCode Go](docs/opencode.md) — 浏览器 Cookie，用于 Go 语言额度窗口统计。
- [Alibaba Coding Plan](docs/alibaba-coding-plan.md) — Web Cookie 或 API Key，用于获取编码计划配额。
- [Alibaba Token Plan](docs/alibaba-token-plan.md) — 百炼浏览器/手动 Cookie，用于查询 Token 额度信用。
- [Gemini](docs/gemini.md) — 基于 OAuth 的配额 API，使用 Gemini CLI 凭据（无需浏览器 Cookie）。
- [Antigravity](docs/antigravity.md) — 本地语言服务器探测（实验性）；无需外部验证。
- [Droid](docs/factory.md) — 浏览器 Cookie + WorkOS Token 流程，用于 Factory 用量及计费统计。
- [Copilot](docs/copilot.md) — GitHub 设备验证流程 + Copilot 内部用量 API。
- [z.ai](docs/zai.md) — API Token，用于查询配额及 MCP（Model Context Protocol）额度窗口。
- [Manus](docs/manus.md) — 浏览器 `session_id` 验证，用于信用余额、月度额度和每日刷新追踪。
- [MiniMax](docs/minimax.md) — API Token、Cookie Header 或浏览器 Cookie，用于查询编码计划用量。
- [Kimi](docs/kimi.md) — 验证令牌（来自 `kimi-auth` Cookie 的 JWT），用于周度配额及 5 小时速率限制追踪。
- [Kimi K2 (非官方)](docs/kimi-k2.md) — 旧版 API Key 流程，用于基于信用的用量总计查询。
- [Kilo](docs/kilo.md) — API Token，支持 CLI 验证回退机制，用于 Kilo Pass 用量统计。
- [Kiro](docs/kiro.md) — 基于 CLI 的用量查询；包含月度额度及额外奖励额度。
- [Vertex AI](docs/vertexai.md) — Google Cloud gcloud OAuth，结合本地 Claude 日志追踪 Token 成本。
- [Augment](docs/augment.md) — Augment CLI 或浏览器 Cookie，用于信用额度追踪与用量监控。
- [Amp](docs/amp.md) — 基于浏览器 Cookie 的验证机制，支持 Amp Free 版用量追踪。
- [Ollama](docs/ollama.md) — API Key 访问权限及浏览器 Cookie，用于 Ollama Cloud 额度窗口查询。
- [JetBrains AI](docs/jetbrains.md) — 基于 JetBrains IDE 配置文件的本地 XML 配额数据；支持月度信用额度追踪。
- [Warp](docs/warp.md) — API Token，用于 GraphQL 请求限制及月度额度查询。
- [ElevenLabs](docs/elevenlabs.md) — API Key，用于字符信用额度和语音插槽用量统计。
- [OpenRouter](docs/openrouter.md) — API Token，用于跨多个 AI 服务的基于信用的用量追踪。
- [Windsurf](docs/windsurf.md) — 浏览器 localStorage Session 导入或本地 SQLite 缓存，用于计划用量查询。
- Perplexity — 基于 Perplexity 使用数据的账户信用额度统计。
- [Xiaomi MiMo](docs/mimo.md) — 浏览器 Cookie，用于余额及 Token 计划用量查询。
- [Doubao](docs/doubao.md) — API Key，用于火山引擎 Ark 请求限制探测。
- [Abacus AI](docs/abacus.md) — 浏览器 Cookie 验证，用于 ChatLLM/RouteLLM 算力信用追踪。
- Mistral — 基于浏览器 Cookie 的月度消费统计。
- [DeepSeek](docs/deepseek.md) — API Key，用于信用余额追踪（区分付费与赠送明细）。
- [Moonshot / Kimi API](docs/moonshot.md) — API Key，用于查询月之暗面/Kimi API 账户余额。
- [Venice](docs/venice.md) — API Key，用于 DIEM 或 USD 余额追踪。
- [Codebuff](docs/codebuff.md) — API Token（或 `~/.config/manicode/credentials.json`），用于信用额度及周度速率限制查询。
- [Crof](docs/crof.md) — API Key，用于美元信用余额及请求配额追踪。
- [Command Code](docs/command-code.md) — 浏览器 Cookie，用于获取 Command Code 计费中的月度 USD 额度。
- [StepFun](docs/stepfun.md) — 用户名 + 密码登录，用于查询 Step Plan 速率限制（5 小时及周度窗口）和订阅计划名称。
- [AWS Bedrock](docs/bedrock.md) — AWS Access Key 或命名 AWS Profile（通过 AWS CLI 进行 SSO/角色假设），用于 Cost Explorer 用量统计与月度预算追踪。
- [Grok](docs/grok.md) — Grok CLI 计费 RPC，以及 grok.com 浏览器会话回退机制。
- [GroqCloud](docs/groqcloud.md) — API Key，用于企业级 Prometheus 请求/Token/缓存命中率指标统计。
- [LLM Proxy](docs/llm-proxy.md) — API Key + 基础 URL，用于聚合代理配额统计及服务明细拆解。
- [Deepgram](docs/deepgram.md) — API Key 用量摘要，涵盖语音、Agent、Token 和 TTS（文本转语音）指标。
- 欢迎接入新服务：[服务商开发指南](docs/provider.md)。

## 图标与截图
菜单栏图标是一个微型用量指示器。进度条的具体含义因服务商而异，遇到错误或数据过时可能导致图标变暗或显示故障指示器。

## 功能特性
- 多服务菜单栏，支持按服务独立开关（设置 → 服务商）。
- 针对各服务的专用用量指示器及重置倒计时。
- 可选的 Codex Web 仪表盘扩展功能（剩余代码审查额度、用量明细、信用历史）。
- 为支持 API 的服务（如 OpenAI、Claude Admin API、OpenRouter、z.ai、MiniMax、Mistral 和 AWS Bedrock）提供内联支出与用量图表。
- 支持为 Codex + Claude 配置自定义成本扫描，并复用图表界面展示已支持服务的历史记录。
- 服务商状态轮询，菜单中显示故障徽章，图标上叠加状态指示器。
- “合并图标”模式，将多个服务整合为一个状态项及切换器。
- 显示控制选项：支持自定义服务商图标、标签、进度条样式、重置时间格式，以及最高用量自动选中功能。
- 刷新频率预设（手动、1分钟、2分钟、5分钟、15分钟）。
- 内置 CLI（`codexbar`）用于脚本和 CI 流程（支持 `codexbar cost --provider codex`、`claude` 或 `both` 进行本地成本统计）；提供 macOS 与 Linux 版 CLI 构建包。
- 为已支持的服务提供 WidgetKit 小组件。
- 可选的会话额度通知及周度重置彩纸动画效果。
- 隐私优先：默认本地解析；浏览器 Cookie 需手动授权并复用（不存储密码）。

## 隐私说明
CodexBar 会扫描你的磁盘吗？不会。它不会遍历文件系统；仅在启用相关功能时，读取少量已知位置的数据（浏览器 Cookie/本地存储、服务商配置文件、本地 JSONL 日志）。服务商令牌及账户设置存储在 `~/.codexbar/config.json` 中，并采用严格的文件权限控制。详细讨论与审计记录请参阅 [Issue #12](https://github.com/steipete/CodexBar/issues/12)。

## macOS 权限说明（为何需要）
- **完全磁盘访问权限（可选）**：仅用于读取基于 Web 的服务商所需的 Safari Cookie/本地存储。若未授予此权限，可改用其他受支持的浏览器、手动导入 Cookie/API Key、OAuth 或 CLI/本地数据源（取决于该服务商是否支持）。
- **钥匙串访问（macOS 提示）**：
  - Chromium Cookie 导入需要浏览器的“安全存储”密钥来解密 Cookie。
  - 当 CodexBar 无可用缓存凭据时，Claude OAuth 初始化可能会读取 Claude CLI 的钥匙串条目。
  - 在需要解密浏览器 Cookie、使用缓存 Cookie Header 或处理 OAuth/设备验证流程凭据时，CodexBar 可能会调用钥匙串。
  - **如何阻止这些钥匙串提示？**
    - 打开 **钥匙串访问.app** → 登录钥匙串 → 搜索被提示的条目（对于 Claude OAuth，通常为“Claude Code-credentials”）。
    - 双击该条目 → **访问控制** → 在“始终允许这些应用程序访问”下添加 `CodexBar.app`。
    - 建议仅添加 CodexBar（除非你希望完全开放，否则避免选择“允许所有应用程序”）。
    - 保存后重新打开 CodexBar。
    - 参考截图：![钥匙串访问控制](docs/keychain-allow.png)
  - **如何对浏览器执行相同操作？**
    - 找到浏览器的“安全存储”密钥（例如“Chrome Safe Storage”、“Brave Safe Storage”、“Microsoft Edge Safe Storage”）。
    - 双击该条目 → **访问控制** → 在“始终允许这些应用程序访问”下添加 `CodexBar.app`。
    - 此举可消除 CodexBar 解密该浏览器 Cookie 时的提示。
  - **最终手段——完全禁用钥匙串读取**：如果“始终允许”未生效（例如 macOS 在 Chromium 更新或 `partition_id` 重置后清除了 ACL），请打开 **CodexBar → 设置 → 高级 → 钥匙串访问**，并启用 **禁用钥匙串访问**。此后 CodexBar 将不再调用钥匙串。基于浏览器 Cookie 的服务将被跳过，但通过 CLI 的 Claude/Codex OAuth 仍可正常工作（它读取的是 `~/.codex` / `~/.claude` 配置文件，而非钥匙串）。
- **文件与文件夹提示（文件夹/卷访问）**：CodexBar 会为部分服务商启动 CLI 和本地探测工具。如果这些辅助程序读取项目目录或外接硬盘，macOS 可能会要求 CodexBar 获取该文件夹/卷的权限（例如桌面或外接磁盘）。此行为由辅助程序的当前工作目录触发，而非后台磁盘扫描。
- **我们不会在后台请求的权限**：无需屏幕录制或辅助功能权限；用户触发的辅助操作可能会向 macOS 申请自动化权限以打开终端。不存储任何密码（仅在手动授权时复用浏览器 Cookie）。

## 文档链接
- 服务商概览：[docs/providers.md](docs/providers.md)
- 服务商开发指南：[docs/provider.md](docs/provider.md)
- Issue 标签规范：[docs/ISSUE_LABELING.md](docs/ISSUE_LABELING.md)
- UI 与图标说明：[docs/ui.md](docs/ui.md)
- CLI 参考文档：[docs/cli.md](docs/cli.md)
- 配置说明：[docs/configuration.md](docs/configuration.md)
- CLI 配置详解：[docs/cli-configuration.md](docs/cli-configuration.md)
- 小组件说明：[docs/widgets.md](docs/widgets.md)
- 架构设计：[docs/architecture.md](docs/architecture.md)
- 刷新循环机制：[docs/refresh-loop.md](docs/refresh-loop.md)
- 状态轮询逻辑：[docs/status.md](docs/status.md)
- Sparkle 更新机制：[docs/sparkle.md](docs/sparkle.md)
- 打包说明：[docs/packaging.md](docs/packaging.md)
- 开发指南：[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)
- 发布检查清单：[docs/RELEASING.md](docs/RELEASING.md)
- 更新日志：[CHANGELOG.md](CHANGELOG.md)

## 快速开始（开发者）
- 克隆仓库，在 Xcode 中打开或直接运行脚本。
- 首次启动后，前往“设置 → 服务商”切换所需服务。
- 安装或登录你所依赖的服务商数据源（CLI、浏览器 Cookie、OAuth/设备验证流程、API Key 或本地应用/配置文件）。
- 可选：设置 OpenAI Cookie（自动或手动）以获取 Codex 仪表盘扩展功能。

## 从源码构建
需要 macOS 14+ 及 Swift 6.2+。

```bash
./Scripts/package_app.sh        # builds CodexBar.app in-place
CODEXBAR_SIGNING=adhoc ./Scripts/package_app.sh  # ad-hoc signing (no Apple Developer account)
open CodexBar.app
```

开发调试循环：
```bash
./Scripts/compile_and_run.sh
./Scripts/compile_and_run.sh --test  # also run swift test before packaging/relaunching
make check                           # SwiftFormat + SwiftLint
make docs-list                       # list docs with frontmatter summaries
```

CLI 安装：
```bash
# after installing CodexBar.app in /Applications
./bin/install-codexbar-cli.sh
```

## 相关项目
- ✂️ [Trimmy](https://github.com/steipete/Trimmy) — “粘贴一次，运行一次。”将多行 Shell 代码块展平为单行，方便直接粘贴执行。
- 🧳 [MCPorter](https://mcporter.dev) — TypeScript 工具包与 CLI，用于 Model Context Protocol (MCP) 服务端开发。
- 🧿 [oracle](https://askoracle.dev) — “向先知提问”。在遇到瓶颈时调用 GPT-5 Pro，并附带自定义上下文与文件。

## 寻找 Windows 版本？
- [Win-CodexBar](https://github.com/Finesssee/Win-CodexBar)

## Linux 桌面集成？
- [codexbar-waybar](https://github.com/Marouan-chak/codexbar-waybar) — Waybar 自定义模块 + GTK4 弹出窗口，适用于 Hyprland / Sway 及其他 Wayland 合成器，基于内置 Linux CLI 构建。
- [Codexbar GNOME](https://extensions.gnome.org/extension/9841/codexbar/) — GNOME Shell 扩展，将 CodexBar 用量数据集成至桌面面板。
- [noctalia-codex-usage](https://github.com/rayoplateado/noctalia-codex-usage) — Noctalia/Quickshell 插件，展示 Codex 5小时及周度用量限制，基于内置 Linux CLI 构建。

## 鸣谢
灵感来源于 [ccusage](https://github.com/ryoppippi/ccusage)（MIT），特别是其成本用量追踪功能。

## 许可证
MIT • Peter Steinberger ([steipete](https://twitter.com/steipete))