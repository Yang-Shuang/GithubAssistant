# Claudian

![GitHub stars](https://img.shields.io/github/stars/YishenTu/claudian?style=social)
![GitHub release](https://img.shields.io/github/v/release/YishenTu/claudian)
![License](https://img.shields.io/github/license/YishenTu/claudian)

![Preview](Preview.png)

一款将 AI 编程代理（如 Claude Code、Codex、Opencode、Pi 等更多即将支持的工具）嵌入 Obsidian Vault（工作区）的插件。你的 Vault 将成为代理的工作目录——文件读写、搜索、Bash 终端执行以及多步工作流均可开箱即用。

## 功能与使用

通过左侧功能区图标或命令面板打开聊天侧边栏。选中文本并使用快捷键进行行内编辑。其交互方式与你熟悉的编程代理（Claude Code、Codex、Opencode、Pi）一致——与代理对话，它即可在 Vault 中读取、写入、编辑和搜索文件。

**行内编辑（Inline Edit）** —— 选中文本或光标所在位置后按快捷键，即可直接在笔记中进行编辑，并支持单词级差异预览。

**斜杠命令与技能（Skills）** —— 输入 `/` 或 `$` 调用可复用的提示词模板，或使用用户级和 Vault 级的技能。

**`@提及（@mention）`** —— 输入 `@` 可提及代理需要处理的任何对象，包括 Vault 文件、子代理、MCP 服务器或外部目录中的文件。

**规划模式（Plan Mode）** —— 通过 `Shift+Tab` 切换。代理会在执行前先进行探索与设计，随后提交计划供你审批。

**指令模式（Instruction Mode, `#`）** —— 从聊天输入框添加经过优化的自定义指令。

**MCP 服务器（MCP Servers）** —— 通过模型上下文协议（Model Context Protocol，支持 stdio、SSE、HTTP）连接外部工具。Claude 在应用内管理 Vault 的 MCP；Codex 使用其自身由 CLI 管理的 MCP 配置。

**多标签页与对话（Multi-Tab & Conversations）** —— 支持多个聊天标签页、对话历史、分支复制、恢复以及紧凑模式。

## 环境要求

- **Claude 提供商**：已安装 [Claude Code CLI](https://code.claude.com/docs/en/overview)（推荐原生安装）。需 Claude 订阅/API 或兼容的第三方提供商（如 [Openrouter](https://openrouter.ai/docs/guides/guides/claude-code-integration)、[Kimi](https://platform.moonshot.ai/docs/guide/agent-support) 等）。
- **可选提供商**：[Codex CLI](https://github.com/openai/codex)、[Opencode](https://opencode.ai/)、[Pi](https://github.com/earendil-works/pi)。
- Obsidian v1.7.2+
- 仅限桌面端（macOS、Linux、Windows）

## 安装方式

### 通过 Obsidian 社区插件商店安装（推荐）

1. 打开 Obsidian → 设置 → 第三方插件 → 浏览
2. 搜索“Claudian”并点击安装
3. 启用该插件

或直接通过[社区插件页面](https://community.obsidian.md/plugins/realclaudian)安装。

### 从 GitHub Releases 下载

1. 从[最新版本页面](https://github.com/YishenTu/claudian/releases/latest)下载 `main.js`、`manifest.json` 和 `styles.css`
2. 在你的 Vault 插件文件夹中创建一个名为 `claudian` 的目录：
   ```
   /path/to/vault/.obsidian/plugins/claudian/
   ```
3. 将下载的文件复制到该 `claudian` 目录中
4. 在 Obsidian 中启用插件：
   - 设置 → 第三方插件 → 启用“Claudian”

### 从源码安装（开发用途）

1. 将此仓库克隆至你的 Vault 插件目录：
   ```bash
   cd /path/to/vault/.obsidian/plugins
   git clone https://github.com/YishenTu/claudian.git
   cd claudian
   ```

2. 安装依赖并构建项目：
   ```bash
   npm install
   npm run build
   ```

3. 在 Obsidian 中启用插件：
   - 设置 → 第三方插件 → 启用“Claudian”

### 开发调试

```bash
# Watch mode
npm run dev

# Production build
npm run build
```

## 隐私与数据使用

- **发送至 API**：你的输入内容、附加文件、图片以及工具调用输出。默认使用 Anthropic（Claude）、OpenAI（Codex）或你在 Opencode/Pi 中配置的提供商；可通过提供商设置和环境变量进行配置。
- **本地存储**：Claudian 设置与会话元数据保存在 `vault/.claudian/`；Claude 提供商文件保存在 `vault/.claude/`；对话记录分别位于 `~/.claude/projects/`（Claude）、`~/.codex/sessions/`（Codex）以及 `.pi/agent/sessions/` 或 `~/.pi/agent/sessions/`（Pi）。
- **环境变量**：提供商的子进程会继承 Obsidian 的环境变量，以及你在 Claudian 中配置的任何额外变量。这对于 CLI 认证、代理设置、证书加载和 PATH 路径解析是必需的。
- **设备特定路径**：各设备的 CLI 路径使用存储在浏览器本地存储中的不透明本地密钥，而非你的系统主机名。
- **后台活动**：Claudian 不会运行遥测信标。UI 轮询计时器仅读取本地 Obsidian/编辑器选择状态。网络活动仅限于明确的提供商运行时任务、已配置的 MCP 端点，以及响应请求所需的提供商 SDK/CLI 调用。

## 故障排除

### Claude CLI not found

如果遇到 `spawn claude ENOENT` 或 `Claude CLI not found` 错误，说明插件无法自动检测你的 Claude 安装路径。在使用 Node 版本管理器（nvm、fnm、volta）时较常见。

**解决方法**：先将该设置留空，以便 Claudian 自动检测 Claude Code。如果自动检测失败，请找到你的 CLI 路径并在“设置 → 高级 → Claude CLI 路径”中手动配置。

| Platform | Command | Example Path |
|----------|---------|--------------|
| macOS/Linux | `which claude` | `/Users/你/.volta/bin/claude` |
| Windows (native) | `where.exe claude` | `C:\Users\你\AppData\Local\Claude\claude.exe` |
| Windows (npm) | `npm root -g` | `{root}\@anthropic-ai\claude-code\cli-wrapper.cjs` |

> **Note**: On Windows, avoid `.cmd` and `.ps1` wrappers. Use `claude.exe` for native installs, or `cli-wrapper.cjs` for package-manager installs. `cli.js` is only a legacy fallback for older Claude Code npm packages.
> 
> > **注意**：在 Windows 上，请避免使用 `.cmd` 和 `.ps1` 包装器。原生安装请使用 `claude.exe`，包管理器安装请使用 `cli-wrapper.cjs`。`cli.js` 仅作为旧版 Claude Code npm 包的遗留回退选项。

**Alternative**: Add your Node.js bin directory to PATH in Settings → Environment → Custom variables.
> **替代方案**：在“设置 → 环境 → 自定义变量”中，将你的 Node.js `bin` 目录添加到 PATH 环境变量中。

### npm CLI and Node.js not in same directory

如果使用通过 npm 安装的 CLI，请检查 `claude` 和 `node` 是否位于同一目录：
```bash
dirname $(which claude)
dirname $(which node)
```

如果路径不同，Obsidian 等图形界面应用可能无法找到 Node.js。

**Solutions**:
1. Install native binary (recommended)
2. Add Node.js path to Settings → Environment: `PATH=/path/to/node/bin`
> **解决方法**：
> 1. 安装原生二进制文件（推荐）
> 2. 在“设置 → 环境”中添加 Node.js 路径：`PATH=/path/to/node/bin`

### Other providers

Codex、Opencode 和 Pi 的支持已上线，但部分功能可能尚未完善，且仍需在不同平台和安装方式下进行更多测试。如果你有功能建议或遇到任何 Bug，请[提交 GitHub Issue](https://github.com/YishenTu/claudian/issues)。

## 项目架构

```
src/
├── main.ts                      # Plugin entry point
├── app/                         # Shared defaults and plugin-level storage
├── core/                        # Provider-neutral runtime, registry, and type contracts
│   ├── runtime/                 # ChatRuntime interface and approval types
│   ├── providers/               # Provider registry and workspace services
│   ├── auxiliary/               # Shared provider auxiliary services
│   ├── bootstrap/               # Plugin bootstrap wiring
│   ├── security/                # Approval utilities
│   └── ...                      # commands, mcp, prompt, storage, tools, types
├── providers/
│   ├── claude/                  # Claude SDK adaptor, prompt encoding, storage, MCP, plugins
│   ├── codex/                   # Codex app-server adaptor, JSON-RPC transport, JSONL history
│   ├── opencode/                # Opencode adaptor
│   ├── pi/                      # Pi RPC adaptor, model discovery, JSONL history
│   └── acp/                     # Agent Client Protocol shared transport
├── features/
│   ├── chat/                    # Sidebar chat: tabs, controllers, renderers
│   ├── inline-edit/             # Inline edit modal and provider-backed edit services
│   └── settings/                # Settings shell with provider tabs
├── shared/                      # Reusable UI components and modals
├── i18n/                        # Internationalization (10 locales)
├── types/                       # Shared ambient types
├── utils/                       # Cross-cutting utilities
└── style/                       # Modular CSS
```

## 开发路线图

- [x] 支持 Opus 和 Sonnet 模型（百万 token）
- [x] Codex provider integration
- [x] Opencode support
- [x] Pi provider support
- [ ] More to come!

## 许可证

本项目基于 [MIT License](LICENSE) 许可。

## Star History

<a href="https://www.star-history.com/?repos=YishenTu%2Fclaudian&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=YishenTu/claudian&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=YishenTu/claudian&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=YishenTu/claudian&type=date&legend=top-left" />
 </picture>
</a>

## 鸣谢

- [Obsidian](https://obsidian.md)：提供插件 API
- [Anthropic](https://anthropic.com)：提供 Claude 及 [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)
- [OpenAI](https://openai.com)：提供 [Codex](https://github.com/openai/codex)
- [Opencode](https://opencode.ai/) 
- [Pi](https://github.com/earendil-works/pi)