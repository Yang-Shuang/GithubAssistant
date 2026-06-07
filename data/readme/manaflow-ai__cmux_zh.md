<h1 align="center">cmux</h1>
<p align="center">基于 Ghostty 的 macOS 终端，为 AI 编程代理提供垂直标签页和通知功能</p>

<p align="center">
  <a href="https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg">
    <img src="./docs/assets/macos-badge.png" alt="Download cmux for macOS" width="180" />
  </a>
</p>

<p align="center">
  English | <a href="README.ja.md">日本語</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.zh-TW.md">繁體中文</a> | <a href="README.ko.md">한국어</a> | <a href="README.de.md">Deutsch</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.it.md">Italiano</a> | <a href="README.da.md">Dansk</a> | <a href="README.pl.md">Polski</a> | <a href="README.ru.md">Русский</a> | <a href="README.bs.md">Bosanski</a> | <a href="README.ar.md">العربية</a> | <a href="README.no.md">Norsk</a> | <a href="README.pt-BR.md">Português (Brasil)</a> | <a href="README.th.md">ไทย</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.km.md">ភាសាខ្មែរ</a> | <a href="README.uk.md">Українська</a>
</p>

<p align="center">
  <a href="https://x.com/manaflowai"><img src="https://img.shields.io/badge/@manaflow-555?logo=x" alt="X / Twitter" /></a>
  <a href="https://discord.gg/xsgFEVrWCZ"><img src="https://img.shields.io/badge/Discord-555?logo=discord" alt="Discord" /></a>
  <a href="https://github.com/manaflow-ai/cmux"><img src="https://img.shields.io/github/stars/manaflow-ai/cmux?style=flat&logo=github&label=stars&color=4c71f2" alt="GitHub stars" /></a>
</p>

<p align="center">
  <img src="./docs/assets/main-first-image.png" alt="cmux screenshot" width="900" />
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=i-WxO5YUTOs">▶ Demo video</a> · <a href="https://cmux.com/blog/zen-of-cmux">The Zen of cmux</a>
</p>

## Features

<table>
<tr>
<td width="40%" valign="middle">
<h3>通知光环 (Notification rings)</h3>
当编程代理需要你的注意时，窗格会显示蓝色光环，标签页也会高亮。
</td>
<td width="60%">
<img src="./docs/assets/notification-rings.png" alt="Notification rings" width="100%" />
</td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>通知面板 (Notification panel)</h3>
在一个地方查看所有待处理的通知，快速跳转到最新的未读消息。
</td>
<td width="60%">
<img src="./docs/assets/sidebar-notification-badge.png" alt="Sidebar notification badge" width="100%" />
</td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>内置浏览器 (In-app browser)</h3>
通过从 <a href="https://github.com/vercel-labs/agent-browser">agent-browser</a> 移植的可脚本化 API，在终端旁分屏显示浏览器。
</td>
<td width="60%">
<img src="./docs/assets/built-in-browser.png" alt="Built-in browser" width="100%" />
</td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>垂直与水平标签页 (Vertical + horizontal tabs)</h3>
侧边栏显示 Git 分支、关联的 PR 状态/编号、工作目录、监听端口以及最新的通知文本。支持水平和垂直分屏。
</td>
<td width="60%">
<img src="./docs/assets/vertical-horizontal-tabs-and-splits.png" alt="Vertical tabs and split panes" width="100%" />
</td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>SSH (SSH)</h3>
<code>cmux ssh user@remote</code> 为远程机器创建工作区。浏览器窗格会通过远程网络路由，因此访问 localhost 即可正常工作。将图片拖入远程会话可通过 scp 上传。
</td>
<td width="60%">
<img src="./docs/assets/ssh.png" alt="cmux SSH" width="100%" />
</td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>Claude Code 团队模式 (Claude Code Teams)</h3>
<code>cmux claude-teams</code> 通过一条命令运行 Claude Code 的队友模式。队友会以原生分屏形式启动，并附带侧边栏元数据和通知功能。无需使用 tmux。
</td>
<td width="60%">
<img src="./docs/assets/claude-code-teams.png" alt="Claude Code Teams" width="100%" />
</td>
</tr>
</table>

- **浏览器导入** — 从 Chrome、Firefox、Arc 等 20 多种浏览器中导入 Cookie、历史记录和会话，使浏览器窗格启动时即可自动登录。
- **自定义命令** — 在 [`cmux.json`](https://cmux.com/docs/custom-commands) 中定义项目特定操作，并通过命令面板启动。
- **可脚本化** — 提供 CLI 和 Socket API，用于创建工作区、分屏窗格、发送按键以及自动化浏览器操作。
- **原生 macOS 应用** — 使用 Swift 和 AppKit 构建（非 Electron）。启动速度快，内存占用低。
- **兼容 Ghostty** — 读取你现有的 `~/.config/ghostty/config` 配置来加载主题、字体和颜色。
- **GPU 加速渲染** — 基于 libghostty 实现流畅的界面渲染。

## Install

### DMG（推荐）

<a href="https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg">
  <img src="./docs/assets/macos-badge.png" alt="Download cmux for macOS" width="180" />
</a>

打开 `.dmg` 文件，将 cmux 拖入“应用程序”文件夹。cmux 通过 Sparkle 自动更新，因此只需下载一次即可。

### Homebrew

```bash
brew tap manaflow-ai/cmux
brew install --cask cmux
```

To update later:

```bash
brew upgrade --cask cmux
```

首次启动时，macOS 可能会要求你确认打开来自已识别开发者的应用。点击 **Open** 继续。

## Why cmux?

我同时运行大量的 Claude Code 和 Codex 会话。我之前使用 Ghostty 配合多个分屏窗格，并依赖 macOS 原生通知来知晓代理何时需要我的介入。但 Claude Code 的通知内容始终只是“Claude is waiting for your input”，没有任何上下文信息。当打开的标签页过多时，我甚至无法再看清标题内容。

我尝试过几款代码编排工具，但它们大多是 Electron/Tauri 应用，性能问题让我很困扰。而且我更偏爱终端，因为 GUI 编排工具会将你锁定在它们的工作流中。因此，我用 Swift/AppKit 将 cmux 打造为一款原生 macOS 应用。它使用 libghostty 进行终端渲染，并读取你现有的 Ghostty 配置来加载主题、字体和颜色。

主要新增功能是侧边栏和通知系统。侧边栏提供垂直标签页，显示每个工作区的 Git 分支、关联的 PR 状态/编号、工作目录、监听端口以及最新的通知文本。通知系统可捕获终端序列（OSC 9/99/777），并提供 CLI (`cmux notify`) 供你接入 Claude Code、OpenCode 等代理的钩子 (hook)。当代理处于等待状态时，其窗格会显示蓝色光环，侧边栏中的标签页也会高亮，这样我就能轻松分辨出哪个分屏或标签页需要我的处理。按 `Cmd+Shift+U` 可跳转到最新的未读通知。

内置浏览器采用了从 [agent-browser](https://github.com/vercel-labs/agent-browser) 移植的可脚本化 API。代理可以快照无障碍树、获取元素引用、点击、填写表单并执行 JS。你可以将浏览器窗格与终端并列分屏，让 Claude Code 直接与你的开发服务器交互。

所有功能均可通过 CLI 和 Socket API 进行脚本化控制——创建工作区/标签页、分屏窗格、发送按键以及在浏览器中打开 URL。

## The Zen of cmux

cmux 并不规定开发者该如何使用工具。它只是一个带有 CLI 的终端和浏览器，其余完全由你决定。

cmux 是一个基础组件 (primitive)，而非完整的解决方案。它为你提供终端、浏览器、通知、工作区、分屏、标签页以及控制所有这些功能的 CLI。cmux 不会强迫你采用某种特定的方式来使用编程代理。你用这些基础组件构建出什么，就属于你。

最优秀的开发者历来都在自己打造工具。目前还没有人完全掌握与 AI 协作的最佳方式，那些正在开发封闭产品的团队也尚未找到答案。最贴近自身代码库的开发者将率先摸索出最优解。

向百万开发者提供可组合的基础组件，他们将共同以比任何产品团队自上而下设计更快的速度，找到最高效的工作流。

## Documentation

有关如何配置 cmux 的更多信息，[请访问我们的文档](https://cmux.com/docs/getting-started?utm_source=readme)。

## Keyboard Shortcuts

### Workspaces (工作区)

| Shortcut | Action |
|----------|--------|
| ⌘ N | New workspace（新建工作区） |
| ⌘ 1–8 | Jump to workspace 1–8（跳转至工作区 1–8） |
| ⌘ 9 | Jump to last workspace（跳转至最近使用的工作区） |
| ⌃ ⌘ ] | Next workspace（下一个工作区） |
| ⌃ ⌘ [ | Previous workspace（上一个工作区） |
| ⌘ ⇧ W | Close workspace（关闭工作区） |
| ⌘ ⇧ R | Rename workspace（重命名工作区） |
| ⌥ ⌘ E | Edit workspace description（编辑工作区描述） |
| ⌘ B | Toggle sidebar（切换侧边栏） |
| ⌥ ⌘ B | Toggle right sidebar（切换右侧边栏） |
| ⌘ ⇧ E | Toggle right sidebar focus（聚焦/取消聚焦右侧边栏） |

### Surfaces (界面)

| Shortcut | Action |
|----------|--------|
| ⌘ T | New surface（新建界面） |
| ⌘ ⇧ ] | Next surface（下一个界面） |
| ⌘ ⇧ [ | Previous surface（上一个界面） |
| ⌃ Tab | Next surface（下一个界面） |
| ⌃ ⇧ Tab | Previous surface（上一个界面） |
| ⌃ 1–8 | Jump to surface 1–8（跳转至界面 1–8） |
| ⌃ 9 | Jump to last surface（跳转至最近使用的界面） |
| ⌘ W | Close surface（关闭界面） |

### Split Panes (分屏窗格)

| Shortcut | Action |
|----------|--------|
| ⌘ D | Split right（向右分屏） |
| ⌘ ⇧ D | Split down（向下分屏） |
| ⌥ ⌘ ← → ↑ ↓ | Focus pane directionally（按方向聚焦窗格） |
| ⌘ ⇧ H | Flash focused panel（闪烁高亮当前聚焦的窗格） |

### Browser (浏览器)

Browser developer-tool shortcuts follow Safari defaults and are customizable in `Settings → Keyboard Shortcuts`.
Command palette navigation shortcuts, including ⌃ P, are also customizable and can be cleared so the keypress reaches the active terminal.

| Shortcut | Action |
|----------|--------|
| ⌘ ⇧ L | Open browser in split（在分屏中打开浏览器） |
| ⌘ L | Focus address bar（聚焦地址栏） |
| ⌘ [ | Back（后退） |
| ⌘ ] | Forward（前进） |
| ⌘ R | Reload page（刷新页面） |
| ⌥ ⌘ I | Toggle Developer Tools (Safari default)（切换开发者工具，Safari 默认快捷键） |
| ⌥ ⌘ C | Show JavaScript Console (Safari default)（显示 JavaScript 控制台，Safari 默认快捷键） |

### Notifications (通知)

| Shortcut | Action |
|----------|--------|
| ⌘ I | Show notifications panel（显示通知面板） |
| ⌘ ⇧ U | Jump to latest unread（跳转至最新未读消息） |
| ⌥ ⌘ U | Toggle current item unread state（切换当前项的未读状态） |
| ⌃ ⌘ U | Mark current item as oldest unread and jump to next latest unread（将当前项标记为最旧未读，并跳转至下一个最新未读） |

### Find (查找)

| Shortcut | Action |
|----------|--------|
| ⌘ F | Find（查找） |
| ⌘ ⇧ F | Find in directory（在目录中查找） |
| ⌘ G / ⌥ ⌘ G | Find next / previous（查找下一个/上一个） |
| ⌥ ⌘ ⇧ F | Hide find bar（隐藏查找栏） |
| ⌘ E | Use selection for find（使用选中文本进行查找） |

### Terminal (终端)

| Shortcut | Action |
|----------|--------|
| ⌘ K | Clear scrollback（清除滚动历史） |
| ⌘ C | Copy (with selection)（复制，含选中内容） |
| ⌘ V | Paste（粘贴） |
| ⌘ + / ⌘ - | Increase / decrease font size（增大/减小字体大小） |
| ⌘ 0 | Reset font size（重置字体大小） |

### Window (窗口)

| Shortcut | Action |
|----------|--------|
| ⌘ ⇧ N | New window（新建窗口） |
| ⌘ ⇧ O | Reopen previous session（重新打开上次会话） |
| ⌘ , | Settings（设置） |
| ⌘ ⇧ , | Reload configuration（重载配置） |
| ⌘ Q | Quit（退出） |

## Nightly Builds

[Download cmux NIGHTLY](https://github.com/manaflow-ai/cmux/releases/download/nightly/cmux-nightly-macos.dmg)

cmux NIGHTLY 是一个独立的应用程序，拥有独立的 Bundle ID，因此可与稳定版并行运行。它自动从最新的 `main` 分支构建，并通过专属的 Sparkle 通道进行自动更新。

请在 [GitHub Issues](https://github.com/manaflow-ai/cmux/issues) 或 Discord 的 [#nightly-bugs on Discord](https://discord.gg/xsgFEVrWCZ) 频道反馈夜间版 Bug。

## Session restore (会话恢复)

Quitting cmux saves the current session. On relaunch, cmux restores app-owned
state:
- Window/workspace/pane layout（窗口/工作区/窗格布局）
- Working directories（工作目录）
- Terminal scrollback (best effort)（终端滚动历史，尽力保留）
- Browser URL and navigation history（浏览器网址与导航历史）

cmux does not checkpoint arbitrary live process state. tmux, vim, shells, and
unsupported terminal apps reopen as normal terminals.

Supported agent sessions can resume when hooks have saved a native session ID.
Install hooks after installing the agent CLI so its binary is on `PATH`:

```bash
cmux hooks setup
cmux hooks setup codex
cmux hooks setup --agent opencode
```

`cmux hooks setup` installs supported agents it can find and prints a summary
for skipped agents. Supported resume integrations include Claude Code, Codex,
Grok, OpenCode, Pi, Amp, Cursor CLI, Gemini, Rovo Dev, Copilot, CodeBuddy,
Factory, and Qoder. Claude Code is handled by the cmux Claude wrapper when Claude
integration is enabled in Settings.

Advanced users and integrations can attach a custom resume command to the
current terminal surface. This is useful for tools with their own durable state,
such as tmux sessions or custom agent CLIs:

```bash
cmux surface resume set --kind tmux --checkpoint work --shell "tmux attach -t work"
cmux surface resume show --json
cmux surface resume clear --checkpoint work
```

The binding stays attached to the cmux surface. Public CLI or socket-created
bindings are stored for inspection and manual restore unless you approve a
signed command prefix for automatic restore. Approved prefixes are also bound to
the working directory and exact environment values, when present. Review or edit
approvals in **Settings > Terminal > Resume Commands**. cmux only auto-runs
resume bindings it marks trusted, such as live process-detected tmux bindings or
user-approved prefixes. Sensitive environment keys such as tokens, passwords,
secrets, and API keys are dropped before a resume binding is stored.

To keep restored agent terminals idle instead of automatically running their resume commands,
turn off **Settings > Terminal > Resume Agent Sessions on Reopen** or set this in
`~/.config/cmux/cmux.json`:

```json
{
  "terminal": {
    "autoResumeAgentSessions": false
  }
}
```

This only disables automatic agent resume commands. cmux still restores the saved layout,
working directories, scrollback, and browser history.

If you need to reapply the last saved snapshot manually, use:
- `File > Reopen Previous Session`
- `⌘ ⇧ O`
- `cmux restore-session`

Under the hood, cmux writes a versioned snapshot under
`~/Library/Application Support/cmux/` and agent hooks write session mappings
under `~/.cmuxterm/`. On restore, cmux rebuilds the layout first, then runs the
supported agent's native resume command when automatic agent resume is enabled.

Read the full guide at <https://cmux.com/docs/session-restore>.

## Star History (星标历史)

<a href="https://star-history.com/#manaflow-ai/cmux&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=manaflow-ai/cmux&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=manaflow-ai/cmux&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=manaflow-ai/cmux&type=Date" width="600" />
 </picture>
</a>

## Contributing (参与贡献)

Ways to get involved:

- Follow us on X for updates [@manaflowai](https://x.com/manaflowai), [@lawrencecchen](https://x.com/lawrencecchen), and [@austinywang](https://x.com/austinywang)
- Join the conversation on [Discord](https://discord.gg/xsgFEVrWCZ)
- Create and participate in [GitHub issues](https://github.com/manaflow-ai/cmux/issues) and [discussions](https://github.com/manaflow-ai/cmux/discussions)
- Let us know what you're building with cmux

## Community (社区)

- [Discord](https://discord.gg/xsgFEVrWCZ)
- [GitHub](https://github.com/manaflow-ai/cmux)
- [X / Twitter](https://twitter.com/manaflowai)
- [YouTube](https://www.youtube.com/channel/UCAa89_j-TWkrXfk9A3CbASw)
- [LinkedIn](https://www.linkedin.com/company/manaflow-ai/)
- [Reddit](https://www.reddit.com/r/cmux/)

## Founder's Edition (创始人版)

cmux is free, open source, and always will be. If you'd like to support development and get early access to what's coming next:

**[Get Founder's Edition](https://buy.stripe.com/3cI00j2Ld0it5OU33r5EY0q)**

- **Prioritized feature requests/bug fixes**（优先处理功能请求/Bug 修复）
- **Early access: cmux AI that gives you context on every workspace, tab and panel**（抢先体验：cmux AI，为每个工作区、标签页和窗格提供上下文信息）
- **Early access: iOS app with terminals synced between desktop and phone**（抢先体验：iOS 应用，桌面与手机终端同步）
- **Early access: Cloud VMs**（抢先体验：云端虚拟机 (Cloud VMs)）
- **Early access: Voice mode**（抢先体验：语音模式）
- **My personal iMessage/WhatsApp**（我的个人 iMessage/WhatsApp 联系方式）

## License

cmux is open source under [GPL-3.0-or-later](LICENSE).

If your organization cannot comply with GPL, a commercial license is available. Contact [founders@manaflow.com](mailto:founders@manaflow.com) for details.