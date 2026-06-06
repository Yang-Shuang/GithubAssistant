<h1 align="center">Understand Anything</h1>

<p align="center">
  <strong>将任意代码库、知识库或文档转化为可探索、搜索和提问的交互式知识图谱。</strong>
  <br />
  <em>兼容 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等工具。</em>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/23482" target="_blank"><img src="https://trendshift.io/api/badge/repositories/23482" alt="Lum1104%2FUnderstand-Anything | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="READMEs/README.zh-CN.md">简体中文</a> | <a href="READMEs/README.zh-TW.md">繁體中文</a> | <a href="READMEs/README.ja-JP.md">日本語</a> | <a href="READMEs/README.ko-KR.md">한국어</a> | <a href="READMEs/README.es-ES.md">Español</a> | <a href="READMEs/README.tr-TR.md">Türkçe</a> | <a href="READMEs/README.ru-RU.md">Русский</a>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-blue" alt="Quick Start" /></a>
  <a href="https://github.com/Lum1104/Understand-Anything/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="License: MIT" /></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/Claude_Code-8A2BE2" alt="Claude Code" /></a>
  <a href="#codex"><img src="https://img.shields.io/badge/Codex-000000" alt="Codex" /></a>
  <a href="#vs-code--github-copilot"><img src="https://img.shields.io/badge/Copilot-24292e" alt="Copilot" /></a>
  <a href="#copilot-cli"><img src="https://img.shields.io/badge/Copilot_CLI-24292e" alt="Copilot CLI" /></a>
  <a href="#gemini-cli"><img src="https://img.shields.io/badge/Gemini_CLI-4285F4" alt="Gemini CLI" /></a>
  <a href="#opencode"><img src="https://img.shields.io/badge/OpenCode-38bdf8" alt="OpenCode" /></a>
  <a href="#mistral-vibe-cli"><img src="https://img.shields.io/badge/Vibe_CLI-7c3aed" alt="Vibe CLI" /></a>
  <a href="#trae"><img src="https://img.shields.io/badge/Trae-7e22ce" alt="Trae" /></a>
  <a href="https://understand-anything.com"><img src="https://img.shields.io/badge/Homepage-d4a574" alt="Homepage" /></a>
  <a href="https://understand-anything.com/demo/"><img src="https://img.shields.io/badge/Live_Demo-00c853" alt="Live Demo" /></a>
</p>

<p align="center">
  <img src="assets/hero.png" alt="Understand Anything — Turn any codebase into an interactive knowledge graph" width="800" />
</p>

<p align="center">
  <strong>💬 <a href="https://discord.gg/pydat66RY">加入 Discord 社区 &rarr;</a></strong>
  <br />
  <em>提问、分享你的成果，获取社区帮助。</em>
</p>

---

**你刚加入一个新团队。代码库有 20 万行代码，该从何下手？**

Understand Anything 是一款 [Claude Code 插件](https://code.claude.com/docs/en/plugins-reference#plugins-reference)，它通过多智能体（Multi-Agent）流水线分析你的项目，为每个文件、函数、类和依赖项构建知识图谱，并提供交互式仪表盘供你直观探索。告别盲目读代码，开始掌握全局视图。

> **目标不是用图谱展示你的代码库有多复杂——而是让你潜移默化地理解各个模块如何协同工作。**

---

## ✨ 功能特性

> [!NOTE]
> **想跳过阅读？** 试试我们[主页](https://understand-anything.com/)上的[在线演示](https://understand-anything.com/demo/)——一个完全交互式的仪表盘，支持在浏览器中直接拖拽、缩放、搜索和探索。

### 探索结构图谱

将代码库作为交互式知识图谱进行导航——每个文件、函数和类都是可点击、搜索和探索的节点。选择任意节点即可查看清晰易懂的摘要、关系说明及引导式导览。

### 理解业务逻辑

切换到领域视图，查看代码如何映射到真实的业务流程——领域、流程步骤以水平图谱形式呈现。

### 分析知识库

将 `/understand-knowledge` 指向一个 [Karpathy-pattern LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)，即可生成带有社区聚类算法的力导向知识图谱。确定性解析器会从 `index.md` 中提取维基链接和分类，随后 LLM 智能体发现隐式关系、提取实体并提炼核心观点——将你的 Wiki 转化为可导航的思想互联图谱。

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🧭 引导式导览</h3>
      <p>自动生成架构导览，按依赖顺序排列。帮助你按正确顺序熟悉代码库。</p>
    </td>
    <td width="50%" valign="top">
      <h3>🔍 模糊搜索与语义搜索</h3>
      <p>支持按名称或含义查找任意内容。例如搜索“哪些模块处理认证？”，即可在图谱中获得相关结果。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>📊 变更影响分析</h3>
      <p>提交前预览你的修改会影响系统的哪些部分，理解代码库中的连锁反应。</p>
    </td>
    <td width="50%" valign="top">
      <h3>🎭 角色自适应界面</h3>
      <p>仪表盘会根据你的身份（初级开发者、产品经理或高级用户）自动调整信息详细程度。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏗️ 架构分层可视化</h3>
      <p>按架构层自动分组——API、Service、Data、UI、Utility，并配有颜色图例。</p>
    </td>
    <td width="50%" valign="top">
      <h3>📚 语言概念解析</h3>
      <p> wherever they appear 解释 12 种编程模式（泛型、闭包、装饰器等）的上下文含义。</p>
    </td>
  </tr>
</table>

---

## 🚀 快速开始

### 1. 安装插件

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### 2. 分析代码库

```bash
/understand
```

多智能体流水线扫描你的项目，提取每个文件、函数、类和依赖项，随后构建知识图谱并保存至 `.understand-anything/knowledge-graph.json`。

**本地化输出：** 使用 `--language` 参数以你所需的语言生成内容：

```bash
# Generate Chinese content (知识图节点描述和 Dashboard UI)
/understand --language zh

# Supported languages: en (default), zh, zh-TW, ja, ko, ru
```

`--language` 参数影响以下内容：
- 知识图谱中的节点摘要与描述
- 仪表盘界面的标签、按钮和工具提示
- 引导式导览的说明文字

### 3. 探索仪表盘

```bash
/understand-dashboard
```

打开交互式 Web 仪表盘，你的代码库将以图谱形式可视化展示——按架构层着色，支持搜索和点击。选择任意节点即可查看其代码、关系说明及自然语言解释。

### 4. 持续探索与学习

```bash
# Ask anything about the codebase
/understand-chat How does the payment flow work?

# Analyze impact of your current changes
/understand-diff

# Deep-dive into a specific file or function
/understand-explain src/auth/login.ts

# Generate an onboarding guide for new team members
/understand-onboard

# Extract business domain knowledge (domains, flows, steps)
/understand-domain

# Analyze a Karpathy-pattern LLM wiki knowledge base
/understand-knowledge ~/path/to/wiki

# Re-run anytime — incremental by default (only re-analyzes changed files)
/understand

# Auto-update on every commit via a post-commit hook
/understand --auto-update

# Scope to a subdirectory (for huge monorepos)
/understand src/frontend
```

---

## 🌐 多平台安装指南

Understand-Anything 兼容多个 AI 编程平台。

### Claude Code（原生支持）

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### 一键安装（Codex / OpenCode / OpenClaw / Antigravity / Gemini CLI / Pi Agent / Vibe CLI / VS Code Copilot / Hermes / Cline / KIMI CLI / Trae）

**macOS / Linux：**
```bash
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash
# or skip the prompt by passing the platform:
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash -s codex
```

**Windows（PowerShell）：**
```powershell
iwr -useb https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.ps1 | iex
```

安装脚本会将仓库克隆至 `~/.understand-anything/repo`，并为所选平台创建相应的软链接。完成后请重启你的 CLI 或 IDE。

- 支持的 `<platform>` 值：`gemini`, `codex`, `opencode`, `pi`, `openclaw`, `antigravity`, `vibe`, `vscode`, `hermes`, `cline`, `kimi`, `trae`
- 后续更新：`./install.sh --update`
- 卸载：`./install.sh --uninstall <platform>`

### Cursor

克隆此仓库后，Cursor 会通过 `.cursor-plugin/plugin.json` 自动发现该插件。无需手动安装——只需克隆并在 Cursor 中打开即可。

如果未自动识别，可手动安装：打开 **Cursor 设置 → 插件**，将 `https://github.com/Lum1104/Understand-Anything` 粘贴到搜索框中并添加。

### VS Code + GitHub Copilot

使用 GitHub Copilot（v1.108+）的 VS Code 会在克隆此仓库后通过 `.copilot-plugin/plugin.json` 自动发现该插件。无需手动安装——只需克隆并在 VS Code 中打开即可。

如需在所有项目中启用个人技能，请运行上述 `install.sh` 并指定 `vscode` 平台。

### Copilot CLI

```bash
copilot plugin install Lum1104/Understand-Anything:understand-anything-plugin
```

### 平台兼容性

| Platform | Status | Install Method |
|----------|--------|----------------|
| Claude Code | ✅ Native | Plugin marketplace |
| Cursor | ✅ Supported | Auto-discovery |
| VS Code + GitHub Copilot | ✅ Supported | Auto-discovery |
| Copilot CLI | ✅ Supported | Plugin install |
| Codex | ✅ Supported | `install.sh codex` |
| OpenCode | ✅ Supported | `install.sh opencode` |
| OpenClaw | ✅ Supported | `install.sh openclaw` |
| Antigravity | ✅ Supported | `install.sh antigravity` |
| Gemini CLI | ✅ Supported | `install.sh gemini` |
| Pi Agent | ✅ Supported | `install.sh pi` |
| Vibe CLI | ✅ Supported | `install.sh vibe` |
| Hermes | ✅ Supported | `install.sh hermes` |
| Cline | ✅ Supported | `install.sh cline` |
| KIMI CLI | ✅ Supported | `install.sh kimi` |
| Trae | ✅ Supported | `install.sh trae` |

---

## 📦 与团队共享图谱

该图谱本质上是 JSON 文件——**只需提交一次，团队成员即可跳过流水线分析**。非常适合新员工入职、PR（Pull Request）审查以及文档即代码（Docs as Code）工作流。

> **示例：** [GoogleCloudPlatform/microservices-demo (分支)](https://github.com/Lum1104/microservices-demo) —— 包含已提交图谱的 Go/Java/Python/Node 参考项目。

**需提交的内容：** `.understand-anything/` 目录下的所有文件，*排除* `intermediate/` 和 `diff-overlay.json`（这些仅为本地临时文件）。

```gitignore
.understand-anything/intermediate/
.understand-anything/diff-overlay.json
```

**保持图谱更新：** 启用 `/understand --auto-update`——通过提交后钩子（post-commit hook）增量更新图谱，确保每次提交都伴随对应的最新图谱。或可在发布前手动重新运行 `/understand`。

**大型图谱（> 10 MB）：** 使用 **git-lfs** 进行版本控制跟踪。

```bash
git lfs install
git lfs track ".understand-anything/*.json"
git add .gitattributes .understand-anything/
```

---

## 🔧 底层原理

### Tree-sitter + LLM 混合架构

静态分析与大语言模型（LLM）各司其职，发挥各自优势：

- **Tree-sitter（确定性解析）** —— 将源代码解析为抽象语法树，并提取结构事实：导入导出、函数/类定义、调用点、继承关系。在扫描阶段预解析为 `importMap` 后传递给文件分析器，避免重复从源码推导导入项。相同输入必得相同输出，确保每次运行结果一致。同时基于指纹机制实现增量更新的变更检测。
- **LLM（语义理解）** —— 结合解析后的结构与原始源码，生成传统解析器无法提供的信息：自然语言摘要、标签分类、架构分层归属、业务领域映射、引导式导览及编程概念提示。

这种分工使得图谱在结构层面具备可复现性（相同代码始终生成相同的边），同时在语义层面准确捕捉开发意图（文件存在的*目的*，而不仅仅是它导入了什么）。

### 多智能体流水线

`/understand` 命令协调 5 个专用智能体，而 `/understand-domain` 额外增加第 6 个：

| Agent | Role |
|-------|------|
| `project-scanner` | 发现文件、检测编程语言与框架 |
| `file-analyzer` | 提取函数、类、导入项；生成图谱节点与边 |
| `architecture-analyzer` | 识别架构分层 |
| `tour-builder` | 生成引导式学习路径 |
| `graph-reviewer` | 验证图谱完整性与引用一致性（默认内联运行；使用 `--review` 触发完整 LLM 审查） |
| `domain-analyzer` | 提取业务领域、流程及步骤（供 `/understand-domain` 调用） |
| `article-analyzer` | 从 Wiki 文章中提取实体、核心观点与隐式关系（供 `/understand-knowledge` 调用） |

文件分析器并行运行（最多 5 个并发，每批处理 20-30 个文件）。支持增量更新——仅重新分析自上次运行以来发生变更的文件。

---

## 🎥 社区资源

由 **Better Stack** 制作的社区版使用教程。

<p align="center">
  <a href="https://www.youtube.com/watch?v=VmIUXVlt7_I"><img src="https://img.youtube.com/vi/VmIUXVlt7_I/maxresdefault.jpg" alt="Community walkthrough by Better Stack — watch on YouTube" width="480" /></a>
  <br />
  <em><a href="https://www.youtube.com/watch?v=VmIUXVlt7_I">Watch on YouTube &rarr;</a></em>
</p>

制作了视频教程、博客文章或指南？请提交 Issue 或 PR，我们将很乐意在此展示。

---

## 🤝 贡献指南

欢迎贡献代码！以下是入门步骤：

1. Fork 本仓库
2. 创建功能分支（`git checkout -b feature/my-feature`）
3. 运行测试（`pnpm --filter @understand-anything/core test`）
4. 提交更改并打开 Pull Request

对于重大变更，请先提交 Issue 以便讨论方案。

---

<p align="center">
  <strong>告别盲目读代码，开始全面理解项目。</strong>
</p>

## ⭐ Star 历史

<a href="https://www.star-history.com/?repos=Lum1104%2FUnderstand-Anything&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />
 </picture>
</a>

<p align="center">
  <em>感谢所有使用者与贡献者——得知这能为大家节省时间，便是我们坚持开发的动力。</em>
</p>

<p align="center">
  MIT License &copy; <a href="https://github.com/Lum1104">Lum1104</a>
</p>