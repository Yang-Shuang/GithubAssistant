<div align="center">

<pre>
              _        _             _ _            
  ___ ___ ___| |_ __ _| |_ _   _ ___| (_)_ __   ___ 
 / __/ __/ __| __/ _` | __| | | / __| | | '_ \ / _ \
| (_| (__\__ \ || (_| | |_| |_| \__ \ | | | | |  __/
 \___\___|___/\__\__,_|\__|\__,_|___/_|_|_| |_|\___|
                                                     
</pre>

# ccstatusline

**🎨 一款专为 Claude Code CLI 打造的高度可定制状态行格式化工具**
*在终端中显示模型信息、Git 分支、Token 用量及其他指标*

[![npm version](https://img.shields.io/npm/v/ccstatusline.svg)](https://www.npmjs.com/package/ccstatusline)
[![npm downloads](https://img.shields.io/npm/dm/ccstatusline.svg)](https://www.npmjs.com/package/ccstatusline)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/sirmalloc/ccstatusline/blob/main/LICENSE)
[![Node.js Version](https://img.shields.io/node/v/ccstatusline.svg)](https://nodejs.org)
[![install size](https://packagephobia.com/badge?p=ccstatusline)](https://packagephobia.com/result?p=ccstatusline)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/sirmalloc/ccstatusline/graphs/commit-activity)

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![ClaudeLog - A comprehensive knowledge base for Claude](https://claudelog.com/img/claude_log_badge.svg)](https://claudelog.com/)


![Demo](https://raw.githubusercontent.com/sirmalloc/ccstatusline/main/screenshots/demo.gif)

</div>
<br />

## 📚 目录

- [近期更新](#-recent-updates)
- [功能特性](#-features)
- [本地化/多语言](#-localizations)
- [快速开始](#-quick-start)
- [Windows 支持](docs/WINDOWS.md)
- [使用指南](docs/USAGE.md)
- [开发指南](docs/DEVELOPMENT.md)
- [贡献代码](#-contributing)
- [许可证](#-license)
- [相关项目](#-related-projects)

<br />

## 🆕 近期更新

### v2.2.14 - v2.2.19 - 版本锁定、npm 来源证明、用量超限组件与 Git 锁冲突规避

- **📌 支持版本锁定** - 新增对全局安装版本锁定的支持，使 Claude Code 能够持续运行你指定的 ccstatusline 版本。
- **🔐 npm 来源证明** - 发布的包现在使用可信发布来源证明，用户可验证发行版的构建位置，同时避免依赖长期有效的 npm publish token。
- **🔄 从自动更新安装迁移** - 如果你当前使用的是自动更新安装方式，请先通过 TUI 卸载选项进行卸载，然后重新安装以进入版本锁定流程。卸载时你的 ccstatusline 设置会被保留。
- **💸 额外用量组件** - 新增“额外用量利用率”和“剩余可用量”组件，用于显示按月付费的超额使用限制，空值率限制桶将按零用量处理。
- **🔒 Git 锁冲突规避** - Git 辅助命令现在传递 `--no-optional-locks` 参数，使后台状态检查避免创建 `index.lock` 竞争条件。
- **🧱 兼容旧版 Git** - Git 组件已避免使用较新的命令格式，以确保在旧版 Git 安装环境中也能正常工作。
- **⚡ 持久化 Git 缓存** - Git 命令输出现在缓存在 `~/.cache/ccstatusline/git-cache` 下，支持可配置的 TTL 以及 `.git/HEAD`/`.git/index` mtime 检查，以减少重复的子进程调用开销。
- **🧭 安装流程优化** - 全局版本锁定现已设为默认安装选项，安装与迁移流程的提示文案更加清晰。
- **🪟 隐藏辅助进程** - 运行时子进程已设置 `windowsHide`，防止在 Windows 上打开额外的命令行窗口。
- **📏 终端宽度覆盖** - 当自动探测不可用时，可通过 `CCSTATUSLINE_WIDTH` 显式指定终端宽度。

### v2.2.13 - 周度模型用量、语音状态、Hook 优化与文档更新

- **📊 Sonnet/Opus 周度用量组件** - 新增针对 Sonnet 和 Opus API 桶的独立周度用量组件，匹配 Claude Code `/usage` 的模型拆分逻辑。
- **🎤 语音状态组件** - 新增显示 Claude Code 语音输入是否启用的组件，支持图标、文本、单词及可选 Nerd Font 显示模式。
- **📉 紧凑进度条** - 区块计时器、区块重置计时器和周度重置计时器现在支持紧凑的短条形进度显示。
- **🔕 更安静的 Hook 输出** - Hook 处理现在会抑制无操作的 JSON 输出，使非状态更新保持静默。

### v2.2.9 - v2.2.12 - GitLab 支持、重置计时器、上下文/压缩优化与 Git 组件增强

- **🦊 GitLab PR/MR 支持** - `Git Branch` 和 `Git PR/MR` 现已支持 GitHub、GitLab 及兼容的自托管远程仓库，自动根据情况调用 `gh` 或 `glab`。
- **🔄 状态行刷新间隔** - 当 Claude Code >=2.1.97 支持时，已安装的配置可通过 TUI 设置 Claude Code 的 `statusLine.refreshInterval`。
- **🧭 TUI 循环导航** - 菜单/列表导航及移动/重排序模式现在会在首尾项之间循环跳转。
- **📋 克隆组件快捷键** - 在组件编辑器中按 `k` 可复制当前选中的组件，克隆的 Powerline 项目将使用全新的背景色。
- **📊 紧凑进度条显示模式** - 上下文百分比、上下文条形图、会话用量、周度用量、区块计时器及重置计时器组件现在支持紧凑条形变体。
- **⏱️ 用量时间游标** - 会话用量和周度用量进度条可显示当前用量窗口内的已用时间位置。
- **🕒 重置计时器时间戳** - 区块与周度重置计时器组件现在可显示精确的重置时间戳，支持紧凑格式、12/24小时制、IANA 时区及区域设置选择。
- **🪟 上下文窗口组件** - 新增 `Context Window` 组件用于显示模型总上下文窗口大小，使 `Context Length` 专注于当前上下文用量。
- **🔁 压缩计数器组件** - 新增 `Compaction Counter` 组件，用于跟踪会话上下文压缩次数，支持图标/文本/数字格式、可选 Nerd Font 图标及隐藏空值行为。
- **🧮 Git 文件状态组件** - 新增 `Git Staged Files`、`Git Unstaged Files`、`Git Untracked Files` 和 `Git Clean Status`，用于显示文件数量及干净/脏污状态。
- **🏷️ 清晰的上下文百分比标签** - `Context %` 和 `Context % (usable)` 现在在切换已用/剩余模式时，会明确标注渲染值为“已用”或“剩余”。
- **⚡ 更多 Powerline 端点样式** - Powerline 分隔符编辑器现在支持超过三种首尾端点样式。
- **🧠 Thinking Effort 更新** - 新增 `xhigh`，未设置时显示 `default`，未知未来级别标记为 `?`，并跟踪实时状态 JSON 及 `/effort` 命令变更。
- **🧮 更准确的 Token 计数** - 流式重复的 JSONL 条目现已去重，防止 Token 组件对 Claude Code 实时输出进行超额统计。
- **🏷️ 更简洁的模型显示** - Model 组件会剥离如 `(1M context)` 之类的尾部上下文后缀；如需显示总窗口大小请使用 `Context Window`。
- **🧹 更干净的空值组件分隔符** - 手动分隔符现在会在渲染为空值的组件周围自动折叠，避免隐藏型空组件消失时留下悬空分隔符。
- **🧱 更健壮的 Git 辅助逻辑** - Git 组件现在能更防御性地处理缺失或异常的 git 命令输出。

### v2.2.8 - Git 组件、智能选择器搜索与极简模式

- **🔀 新增 Git PR 组件** - 添加 `Git PR` 组件，支持可点击的 PR 链接及当前分支的状态/标题显示（可选）。
- **🧰 Git 组件大幅扩展** - 新增 `Git Status`、`Git Staged`、`Git Unstaged`、`Git Untracked`、`Git Ahead/Behind`、`Git Conflicts`、`Git SHA`、`Git Origin Owner`、`Git Origin Repo`、`Git Origin Owner/Repo`、`Git Upstream Owner`、`Git Upstream Repo`、`Git Upstream Owner/Repo`、`Git Is Fork`、`Git Worktree Mode`、`Git Worktree Name`、`Git Worktree Branch`、`Git Worktree Original Branch` 及 `Custom Symbol`。
- **👤 Claude 账户邮箱组件** - 新增会话级组件，从 `~/.claude.json` 读取已登录的 Claude 账户邮箱（尊重 `CLAUDE_CONFIG_DIR`）。
- **🧼 全局极简模式** - 在 `Global Overrides` 中新增全局开关，强制所有组件进入原始值模式，打造无标签的干净状态行。
- **🔎 智能组件选择器搜索** - 添加/更改组件的选择器现在支持子串、首字母缩写及模糊匹配，结果按相关性排序并实时高亮匹配项。
- **📏 更可靠的终端宽度检测** - Flex 分隔符与右对齐功能在通过包装进程或嵌套 PTY 启动 ccstatusline 时现能更可靠地工作。
- **🎨 Powerline 主题连续性** - 内置的 Powerline 主题现在可在多行状态间无缝延续颜色，而非每行重新开始。

### v2.2.0 - v2.2.6 - 性能、组件、链接与可靠性更新

- **🚀 新增 Token 速度组件** - 添加三个组件：**Input Speed**、**Output Speed** 和 **Total Speed**。
  - 每个速度组件在编辑器中支持 `0-120` 秒的可配置窗口（按 `w` 键）。
  - `0` 禁用窗口模式，使用全会话平均速度。
  - `1-120` 计算所选滑动窗口内的近期速度。
- **🧩 Skills 组件控制增强 (v2.2.1)** - 新增可配置的 Skills 模式（最近/计数/列表）、可选隐藏空值行为，以及按最新优先排序的列表大小限制。
- **🌐 Usage API 代理支持 (v2.2.2)** - Usage 组件现在尊重大写 `HTTPS_PROXY` 环境变量，用于其直连 Anthropic API 的请求。
- **🧠 Thinking Effort 组件新增 (v2.2.4)** - 添加显示当前 Claude Code 思考强度级别的组件。
- **🍎 macOS 用量查询可靠性提升 (v2.2.5)** - 改进 macOS 上加载 Usage API Token 的稳定性。
- **⌨️ Vim Mode 组件新增 (v2.2.5)** - 添加显示当前 vim 模式的组件，支持 ASCII 及可选 Nerd Font 图标显示。
- **🔗 Git 组件链接模式 (v2.2.6)** - `Git Branch` 可渲染可点击的 GitHub 分支链接，`Git Root Dir` 可为 VS Code 和 Cursor 渲染可点击的 IDE 路径链接。
- **🤝 更准确的子代理感知速度报告** - Token 速度计算现在继续包含引用的子代理活动，使显示的速度更能反映实际的并发工作负载。

<br />
<details>
<summary><b>早期更新 (v2.1.10 及更早版本)</b></summary>

### v2.1.0 - v2.1.10 - Usage 组件、链接、新 Git 插入/删除组件与可靠性修复

- **🧩 新增 Usage 组件 (v2.1.0)** - 添加 **Session Usage**、**Weekly Usage**、**Block Reset Timer** 和 **Context Bar** 组件。
- **📊 更准确的计数逻辑 (v2.1.0)** - Usage/上下文组件现在优先使用新的 statusline JSON 指标（若可用），以提供更精确的 Token 与上下文计数。
- **🪟 Windows 空文件 Bug 修复 (v2.1.1)** - 修复了 Windows 下可能意外创建空 `c:\dev\null` 文件的问题。
- **🔗 新增 Link 组件 (v2.1.3)** - 添加支持 OSC8 可点击渲染、预览一致性及原始模式的新 **Link** 组件。
- **➕ 新增 Git Insertions 组件 (v2.1.4)** - 添加专用 Git 组件，仅显示未提交的插入行数（例如 `+42`）。
- **➖ 新增 Git Deletions 组件 (v2.1.4)** - 添加专用 Git 组件，仅显示未提交的删除行数（例如 `-10`）。
- **🧠 Context 格式回退修复 (v2.1.6)** - 当 `context_window_size` 缺失时，上下文组件现在能从模型标识符中的长上下文标签（如 `[1m]` 和 `1M context`）推断出 1M 模型。
- **⏳ 周度重置计时器拆分 (v2.1.7)** - 新增独立的 `Weekly Reset Timer` 组件。
- **⚙️ 自定义配置文件参数 (v2.1.8)** - 添加 `--config <path>` 支持，使 ccstatusline 可从自定义路径加载/保存设置。
- **🔣 Unicode 分隔符十六进制输入升级 (v2.1.9)** - Powerline 分隔符十六进制输入现在支持 4-6 位数字（完整 Unicode 码点最高至 `U+10FFFF`）。
- **🌳 裸仓库 Worktree 检测修复 (v2.1.10)** - `Git Worktree` 现已能正确检测从裸仓库创建的链接 worktrees。

### v2.0.26 - v2.0.29 - 性能、Git 底层优化与工作流改进

- **🧠 Memory Usage 组件 (v2.0.29)** - 新增显示当前系统内存用量的组件（`Mem: used/total`）。
- **⚡ Block Timer 缓存机制 (v2.0.28)** - 缓存区块计时器指标以减少每次渲染时的 JSONL 解析开销，采用按配置哈希的缓存文件及自动 5 小时失效策略。
- **🧱 Git 组件命令重构 (v2.0.28)** - 重构 Git 组件以使用共享的 git 命令辅助函数，并扩展了失败与边界情况的测试覆盖。
- **🪟 Windows UTF-8 管道输出修复 (v2.0.28)** - 为管道状态行渲染设置 Windows UTF-8 代码页。
- **📁 Git Root Dir 组件 (v2.0.27)** - 新增显示仓库根目录名称的 Git 组件。
- **🏷️ Session Name 组件 (v2.0.26)** - 新增从 `/rename` 获取并显示当前 Claude Code 会话名称的组件。
- **🏠 CWD 主目录缩写支持 (v2.0.26)** - 预览与实时渲染中均新增 `~` 缩写选项用于 CWD 显示。
- **🧠 Context 模型后缀修复 (v2.0.26)** - 上下文组件现在能跨所有模型识别 `[1m]` 后缀，而非仅针对单一模型路径。
- **🧭 组件选择器 UX 更新 (v2.0.26)** - 改进组件发现/导航体验，并添加更清晰、安全的清空行行为。
- **⌨️ TUI 编辑器输入修复 (v2.0.26)** - 防止快捷键/输入内容泄漏到组件编辑流程中。
- **📄 仓库文档更新 (v2.0.26)** - 指导文档已从 `CLAUDE.md` 迁移至 `AGENTS.md`（保留符号链接兼容性）。

### v2.0.16 - 为 Current Working Directory 组件添加 Fish 风格路径缩写开关

### v2.0.15 - Block Timer 计算修复
- 修复区块计时器的计算逻辑错误

### v2.0.14 - Context Percentage 组件新增剩余模式切换
- **Remaining Mode** - 现在你可在 TUI 配置时按 `u` 键，在上下文百分比组件的“已用百分比”与“剩余百分比”之间切换。

### v2.0.12 - Custom Text 组件现已支持 Emoji
- **👾 Emoji 支持** - 你现在可将 Emoji 粘贴到自定义文本组件中。还可开启合并选项为组件添加 Emoji 标签，效果如下：
  
![Emoji Support](https://raw.githubusercontent.com/sirmalloc/ccstatusline/main/screenshots/emojiSupport.png)

### v2.0.11 - 无限状态行数
- **🚀 无行数限制** - 可配置任意数量的状态行 - 原有的 3 行限制已移除

### v2.0.10 - Git 更新
- **🌳 Git Worktree 组件** - 在使用 git worktrees 时显示当前活跃的 worktree 名称
- **👻 “无 Git”提示隐藏开关** - Git 组件现在支持在非仓库环境下隐藏“no git”提示（编辑组件时按 `h` 键切换）

### v2.0.8 - Powerline 自动对齐

![Powerline Auto-Alignment](https://raw.githubusercontent.com/sirmalloc/ccstatusline/main/screenshots/autoAlign.png)

- **🎯 组件对齐** - 在 Powerline 模式下跨多行状态行自动对齐组件，打造整洁的列式布局（在 Powerline Setup 中按 `a` 键切换）

### v2.0.7 - Current Working Directory & Session Cost

![Current Working Directory and Session Cost](https://raw.githubusercontent.com/sirmalloc/ccstatusline/main/screenshots/cwdAndSessionCost.png)

- **📁 Current Working Directory** - 显示当前工作目录，支持可配置的段数显示
  - 设置要显示的父级路径段数（例如仅显示最后 2 段：`.../Personal/ccstatusline`）
  - 支持原始值模式以紧凑显示
  - 自动使用省略号截断超长路径
- **💰 Session Cost Widget** - 追踪你的 Claude Code 会话成本（需 Claude Code 1.0.85+）
  - 以 USD 显示总会话成本
  - 支持原始值模式（仅显示 `$X.YZ` 而非 `Cost: $X.YZ`）
  - 实时从 Claude Code 会话数据追踪成本
  - 注意：使用 `/resume` 时成本可能无法正确更新（Claude Code 限制）
- **🐛 Bug Fixes**
  - 修复区块计时器计算，确保跨区块边界的时间跟踪准确
  - 改进组件编辑器稳定性，完善 Ctrl+S 处理逻辑
  - 增强数值输入框中的光标显示

### v2.0.2 - Block Timer Widget

![Block Timer](https://raw.githubusercontent.com/sirmalloc/ccstatusline/main/screenshots/blockTimerSmall.png)

- **⏱️ Block Timer** - 追踪你在 5 小时 Claude Code 区块内的进度
  - 显示当前区块已用时间（例如 "3hr 45m"）
  - 进度条模式显示可视化完成百分比
  - 两种进度条样式：全宽（32字符）或紧凑（16字符）
  - 自动从转录日志时间戳检测区块边界

### v2.0.0 - Powerline Support & Enhanced Themes
- **⚡ Powerline Mode** - 精美的 Powerline 风格状态行，支持箭头分隔符与可定制端点
- **🎨 Built-in Themes** - 多个预配置主题，可直接复制并自定义
- **🌈 Advanced Color Support** - 基础（16色）、256色（支持自定义 ANSI 代码）及真彩色（支持十六进制代码）模式
- **🔗 Widget Merging** - 可合并多个组件，支持带/不带内边距的无缝设计
- **📦 Easy Installation** - 直接使用 `npx` 或 `bunx` 安装 - 无需全局包
- **🔤 Custom Separators** - 添加多个 Powerline 分隔符，使用自定义十六进制代码以支持字体渲染
- **🚀 Auto Font Install** - 在用户授权下自动安装 Powerline 字体

</details>

<br />

## ✨ 功能特性

- **📊 实时指标** - 显示模型名称、Git 分支、Token 用量、各模型周度用量、额外用量限制、语音输入状态、会话时长、压缩次数、区块计时器等
- **🎨 完全可定制** - 自由选择要显示的内容，并为每个元素自定义颜色
- **⚡ Powerline 支持** - 精美的 Powerline 风格渲染，支持箭头分隔符、端点样式与自定义字体
- **📐 多行支持** - 配置多个独立的状态行
- **🖥️ 交互式 TUI** - 内置基于 React/Ink 的配置界面
- **🔎 快速组件选择器** - 按分类添加/更改组件，支持搜索与智能排序匹配
- **⚙️ 全局选项** - 跨所有组件应用一致的格式设置（内边距、分隔符、加粗、极简模式及颜色覆盖）
- **🚀 跨平台兼容** - 完美支持 Bun 和 Node.js
- **🔧 灵活配置** - 通过 `CLAUDE_CONFIG_DIR` 环境变量支持自定义 Claude Code 配置目录
- **📏 智能宽度检测** - 自动适配终端宽度，配合 Flex 分隔符使用效果更佳
- **⚡ 开箱即用** - 提供合理的默认值，无需额外配置即可直接使用

<br />

## 🌐 本地化/多语言

本节中的本地化版本为第三方维护的独立分支。它们不由本仓库维护、审核或背书，使用前请自行审查其代码与发行版。

- 🌏 **中文版 (Chinese):** [ccstatusline-zh](https://github.com/huangguang1999/ccstatusline-zh)

<br />

## 🚀 快速开始

### 无需安装！直接使用 npx 或 bunx：

```bash
# 使用 npm 运行配置 TUI
npx -y ccstatusline@latest

# 或使用 Bun（速度更快）
bunx -y ccstatusline@latest
```

两条命令启动的 TUI 完全相同。在初始设置流程中，如果你希望 Claude Code 始终停留在你正在运行的 ccstatusline 版本上而不是跟随 `@latest`，请选择 **Pinned global install**；TUI 将通过 npm 或 Bun 全局安装该锁定版本，并将锁定的 `ccstatusline` 命令写入 Claude Code 配置。完成锁定安装后，未来可直接运行 `ccstatusline` 启动 TUI。

<br />
<details>
<summary><b>Configure ccstatusline</b></summary>

交互式配置工具提供终端界面，你可在此：
- 配置多个独立的状态行
- 添加/删除/重排状态行组件
- 自定义每个组件的颜色
- 配置 Flex 分隔符行为
- 在 Claude Code 支持的情况下配置状态行刷新间隔
- 编辑自定义文本组件
- 安装/卸载至 Claude Code 设置
- 实时预览你的状态行

> 💡 **提示：** 你的设置会自动保存至 `~/.config/ccstatusline/settings.json`

> 🔧 **自定义 Claude 配置目录：** 如果你的 Claude Code 配置文件位于非标准位置，请设置 `CLAUDE_CONFIG_DIR` 环境变量：
> ```bash
> # Linux/macOS
> export CLAUDE_CONFIG_DIR=/custom/path/to/.claude
> ```

> 🌐 **Usage API 代理：** Usage 组件现在尊重大写 `HTTPS_PROXY` 环境变量，用于其直连 Anthropic API 的请求。

> 🪟 **Windows 支持：** PowerShell 示例、安装说明、字体配置、故障排除、WSL 及 Windows Terminal 设置详见 [docs/WINDOWS.md](docs/WINDOWS.md)。

</details>

<details>
<summary><b>Claude Code settings.json format</b></summary>

当你从 TUI 进行安装时，ccstatusline 会将 `statusLine` 命令对象写入你的 Claude Code 配置：

```json
{
  "statusLine": {
    "type": "command",
    "command": "npx -y ccstatusline@latest",
    "padding": 0,
    "refreshInterval": 10
  }
}
```

仅当你的 Claude Code 版本支持时（>=2.1.97），才会写入 `refreshInterval`。TUI 可将其设置为 `1-60` 秒，或留空输入以移除该字段。

其他支持的命令值包括：
- `bunx -y ccstatusline@latest`
- `ccstatusline`（适用于自管理/全局安装）

对于锁定安装，请使用 `npx -y ccstatusline@latest` 或 `bunx -y ccstatusline@latest` 启动 TUI，然后选择 **Pinned global install**。TUI 会通过全局安装来锁定当前版本，并将 `"command": "ccstatusline"` 写入 `settings.json`；此后你可直接运行 `ccstatusline` 打开 TUI。

</details>

## 🤝 贡献代码

欢迎贡献！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开 Pull Request

## Support

如果 ccstatusline 对你有所帮助，可以考虑请我喝杯咖啡：

<a href="https://www.buymeacoffee.com/sirmalloc" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


## 📄 许可证

[MIT](LICENSE) © Matthew Breedlove


## 👤 作者

**Matthew Breedlove**

- GitHub: [@sirmalloc](https://github.com/sirmalloc)


## 🔗 相关项目

- [tweakcc](https://github.com/Piebald-AI/tweakcc) - 自定义 Claude Code 主题、思考动词等。
- [ccusage](https://github.com/ryoppippi/ccusage) - 追踪并显示 Claude Code 用量指标。
- [codachi](https://github.com/vincent-k2026/codachi) - 一款随上下文窗口增长而成长的 Tamagotchi 风格状态行宠物。
- [AIWatch](https://ai-watch.dev) - 30+ AI API 与应用的实时状态监控；配合自定义命令组件，可在你的状态行中直观展示提供商故障信息。


## 🙏 鸣谢

- 专为与 Anthropic 的 [Claude Code CLI](https://claude.ai/code) 搭配使用而构建
- TUI 界面由 [Ink](https://github.com/vadimdemedes/ink) 驱动
- 为 Claude Code 社区 ❤️ 打造

<br />

## Star History

<a href="https://www.star-history.com/#sirmalloc/ccstatusline&Timeline">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=sirmalloc/ccstatusline&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=sirmalloc/ccstatusline&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=sirmalloc/ccstatusline&type=Timeline" />
 </picture>
</a>

<div align="center">

### 🌟 支持本项目

如果该项目对你有帮助，请给一个 ⭐！

[![GitHub stars](https://img.shields.io/github/stars/sirmalloc/ccstatusline?style=social)](https://github.com/sirmalloc/ccstatusline/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sirmalloc/ccstatusline?style=social)](https://github.com/sirmalloc/ccstatusline/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/sirmalloc/ccstatusline?style=social)](https://github.com/sirmalloc/ccstatusline/watchers)

[![npm version](https://img.shields.io/npm/v/ccstatusline.svg)](https://www.npmjs.com/package/ccstatusline)
[![npm downloads](https://img.shields.io/npm/dm/ccstatusline.svg)](https://www.npmjs.com/package/ccstatusline)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/sirmalloc/ccstatusline/blob/main/LICENSE)
[![Made with Bun](https://img.shields.io/badge/Made%20with-Bun-000000.svg?logo=bun)](https://bun.sh)

[![Issues](https://img.shields.io/github/issues/sirmalloc/ccstatusline)](https://github.com/sirmalloc/ccstatusline/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/sirmalloc/ccstatusline)](https://github.com/sirmalloc/ccstatusline/pulls)
[![Contributors](https://img.shields.io/github/contributors/sirmalloc/ccstatusline)](https://github.com/sirmalloc/ccstatusline/graphs/contributors)

### 💬 联系我们

[报告 Bug](https://github.com/sirmalloc/ccstatusline/issues) · [请求功能](https://github.com/sirmalloc/ccstatusline/issues) · [讨论区](https://github.com/sirmalloc/ccstatusline/discussions)

</div>