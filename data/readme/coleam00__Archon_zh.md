<p align="center">
  <img src="assets/logo.png" alt="Archon" width="160" />
</p>

<h1 align="center">Archon</h1>

<p align="center">
  面向 AI 编程的首款开源编排构建器。让 AI 编程变得确定且可重复。
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/13964" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13964" alt="coleam00%2FArchon | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" /></a>
  <a href="https://github.com/coleam00/Archon/actions/workflows/test.yml"><img src="https://github.com/coleam00/Archon/actions/workflows/test.yml/badge.svg" alt="CI" /></a>
  <a href="https://archon.diy/docs/"><img src="https://img.shields.io/badge/docs-archon.diy-blue" alt="Docs" /></a>
</p>

---

Archon 是一款面向 AI 编程智能体的工作流引擎。将你的开发流程定义为 YAML 工作流——规划、实现、验证、代码审查、PR 创建等，并在所有项目中可靠地运行它们。

正如 Dockerfile 改变了基础设施管理，GitHub Actions 重塑了 CI/CD——Archon 则为 AI 编程工作流带来了同样的变革。可以把它想象成面向软件开发的 n8n。

## 为什么选择 Archon？

当你要求 AI 智能体“修复这个 Bug”时，结果往往取决于模型当时的心情。它可能会跳过规划步骤，可能忘记运行测试，也可能写出不符合你模板要求的 PR 描述。每次运行的结果都各不相同。

Archon 解决了这个问题。将你的开发流程编码为工作流。工作流定义了阶段、验证门禁和产物。AI 负责在每个步骤中提供智能，但整体结构是确定的且由你掌控。

- **可重复** - 相同的工作流、相同的执行顺序、每次运行皆如此。规划、实现、验证、审查、创建 PR。
- **隔离性** - 每次工作流运行都会获得独立的 `git worktree`。可同时并行运行 5 个修复任务，互不冲突。
- **即发即走（异步执行）** - 启动工作流后去处理其他事务。回来时即可看到已完成且带有审查意见的 PR。
- **可组合** - 将确定性节点（bash 脚本、测试、git 操作）与 AI 节点（规划、代码生成、审查）混合使用。AI 仅在真正产生价值的环节运行。
- **可移植** - 在 `.archon/workflows/` 中定义一次工作流，提交到仓库即可。无论是通过 CLI、Web UI、Slack、Telegram 还是 GitHub，效果完全一致。

## 实际效果示例

以下是一个 Archon 工作流的示例：它会进行规划，循环实现直到测试通过，获取你的批准，然后创建 PR：

```yaml
# .archon/workflows/build-feature.yaml
nodes:
  - id: plan
    prompt: "Explore the codebase and create an implementation plan"

  - id: implement
    depends_on: [plan]
    loop:                                      # AI loop - iterate until done
      prompt: "Read the plan. Implement the next task. Run validation."
      until: ALL_TASKS_COMPLETE
      fresh_context: true                      # Fresh session each iteration

  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"                   # Deterministic - no AI

  - id: review
    depends_on: [run-tests]
    prompt: "Review all changes against the plan. Fix any issues."

  - id: approve
    depends_on: [review]
    loop:                                      # Human approval gate
      prompt: "Present the changes for review. Address any feedback."
      until: APPROVED
      interactive: true                        # Pauses and waits for human input

  - id: create-pr
    depends_on: [approve]
    prompt: "Push changes and create a pull request"
```

告诉你的编程智能体你想要什么，Archon 负责处理其余部分：

```
You: Use archon to add dark mode to the settings page

Agent: I'll run the archon-idea-to-pr workflow for this.
       → Creating isolated worktree on branch archon/task-dark-mode...
       → Planning...
       → Implementing (task 1/4)...
       → Implementing (task 2/4)...
       → Tests failing - iterating...
       → Tests passing after 2 iterations
       → Code review complete - 0 issues
       → PR ready: https://github.com/you/project/pull/47
```

## 历史版本

寻找最初基于 Python 的 Archon（任务管理 + RAG）？它已完整保留在 [`archive/v1-task-management-rag`](https://github.com/coleam00/Archon/tree/archive/v1-task-management-rag) 分支中。

## 快速开始

> **大多数用户应从[完整安装](#完整安装-5分钟)开始**——它将引导你配置凭据，将 Archon 技能安装到你的项目中，并提供 Web 仪表盘。
>
> **已经配置好 Claude Code，只需要 CLI？** 请直接跳转至[快速安装](#快速安装-30秒)。

### 完整安装（约 5 分钟）

克隆仓库并使用引导式设置向导。这将配置凭据、平台集成，并将 Archon 技能复制到你的目标项目中。

<details>
<summary><b>前置条件</b> - Bun、Claude Code 和 GitHub CLI</summary>

**Bun** - [bun.sh](https://bun.sh)

```bash
# macOS/Linux
curl -fsSL https://bun.sh/install | bash

# Windows (PowerShell)
irm bun.sh/install.ps1 | iex
```

**GitHub CLI** - [cli.github.com](https://cli.github.com/)

```bash
# macOS
brew install gh

# Windows (via winget)
winget install GitHub.cli

# Linux (Debian/Ubuntu)
sudo apt install gh
```

**Claude Code** - [claude.ai/code](https://claude.ai/code)

```bash
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

</details>

```bash
git clone https://github.com/coleam00/Archon
cd Archon
bun install
claude
```

然后输入：**"Set up Archon"**

设置向导将引导你完成所有步骤：CLI 安装、身份验证、平台选择，并将 Archon 技能复制到你的目标仓库。

### 快速安装（约 30 秒）

已经配置好 Claude Code？直接安装独立的 CLI 二进制文件并跳过向导。

**macOS / Linux**
```bash
curl -fsSL https://archon.diy/install | bash
```

**Windows (PowerShell)**
```powershell
irm https://archon.diy/install.ps1 | iex
```

**Homebrew**
```bash
brew install coleam00/archon/archon
```

> **编译后的二进制文件需要设置 `CLAUDE_BIN_PATH`。** 快速安装版未内置 Claude Code。请单独安装它，然后让 Archon 指向该路径：
>
> ```bash
> # macOS / Linux / WSL
> curl -fsSL https://claude.ai/install.sh | bash
> export CLAUDE_BIN_PATH="$HOME/.local/bin/claude"
>
> # Windows (PowerShell)
> irm https://claude.ai/install.ps1 | iex
> $env:CLAUDE_BIN_PATH = "$env:USERPROFILE\.local\bin\claude.exe"
> ```
>
> 或在 `~/.archon/config.yaml` 中设置 `assistants.claude.claudeBinaryPath`。Docker 镜像已预装 Claude Code。详情请参阅 [AI 智能体 → 二进制路径配置](https://archon.diy/getting-started/ai-assistants/#binary-path-configuration-compiled-binaries-only)。

### 开始使用 Archon

完成任一安装路径后，进入你的项目并开始工作：

```bash
cd /path/to/your/project
claude
```

```
Use archon to fix issue #42
```

```
What archon workflows do I have? When would I use each one?
```

编程智能体会为你处理工作流选择、分支命名和 worktree 隔离。首次使用时，项目会自动注册。

> **重要提示：** 请始终在目标仓库中运行 Claude Code，而不是在 Archon 仓库中。设置向导已将 Archon 技能复制到你的项目中，以便直接调用。

## Web UI

Archon 内置了 Web 仪表盘，用于与编程智能体对话、运行工作流和监控活动。二进制安装版：运行 `archon serve` 即可一键下载并启动 Web UI。源码部署：让你的编程智能体从 Archon 仓库启动前端，或自己在仓库根目录运行 `bun run dev`。

在聊天侧边栏的“项目”旁点击 **+** 即可注册项目——输入 GitHub URL 或本地路径。然后开始对话、调用工作流，并实时查看进度。

**核心页面：**
- **聊天（Chat）** - 支持实时流式输出和工具调用可视化的对话界面
- **仪表盘（Dashboard）** - 监控运行中工作流的控制中心，可按项目、状态和日期筛选历史记录
- **工作流编辑器（Workflow Builder）** - 支持拖拽操作的可视化编辑器，用于创建包含循环节点的工作流图（DAG）
- **工作流执行（Workflow Execution）** - 任意运行中或已完成工作流的逐步进度视图

**监控中心：** 侧边栏显示来自**所有平台**的对话——不仅限于 Web。从 CLI 启动的工作流、Slack 或 Telegram 的消息、GitHub Issue 交互等，全部汇聚于一处。

完整文档请参阅 [Web UI 指南](https://archon.diy/adapters/web/)。

## 你可以自动化什么？

Archon 预置了针对常见开发任务的工作流：

| Workflow | 功能说明 |
|----------|-------------|
| `archon-assist` | **通用问答、调试与探索** - 搭载完整工具链的 Claude Code 智能体 |
| `archon-fix-github-issue` | **分类 Issue → 调查/规划 → 实现 → 验证 → 创建 PR → 智能审查 → 自动修复** |
| `archon-create-issue` | **分类问题 → 收集上下文 → 调查 → 创建 GitHub Issue** |
| `archon-issue-review-full` | **全面修复 + 多智能体完整审查流水线**（针对 GitHub Issues） |
| `archon-piv-loop` | **引导式 Plan-Implement-Validate 循环**，迭代间包含人工审查 |
| `archon-idea-to-pr` | **功能创意 → 规划 → 实现 → 验证 → PR → 5 路并行审查 → 自动修复** |
| `archon-plan-to-pr` | **执行现有计划 → 实现 → 验证 → PR → 审查 → 自动修复** |
| `archon-feature-development` | **根据计划实现功能 → 验证 → 创建 PR** |
| `archon-adversarial-dev` | **使用对抗式开发从 scratch 构建完整应用** |
| `archon-smart-pr-review` | **分类 PR 复杂度 → 运行定向审查智能体 → 汇总结果** |
| `archon-comprehensive-pr-review` | **多智能体 PR 审查（5 个并行审查者）**，含自动修复功能 |
| `archon-validate-pr` | **全面 PR 验证测试**，同时覆盖 main 和 feature 分支 |
| `archon-architect` | **架构扫描、复杂度降低、代码库健康度提升** |
| `archon-refactor-safely` | **安全重构**，含类型检查钩子与行为验证 |
| `archon-interactive-prd` | **通过引导式对话创建 PRD（产品需求文档）** |
| `archon-ralph-dag` | **PRD 实现循环** - 遍历用户故事直至完成 |
| `archon-workflow-builder` | **为你的项目生成新的 Archon 工作流 YAML** |
| `archon-remotion-generate` | **使用 AI 生成或修改 Remotion 视频组合** |
| `archon-resolve-conflicts` | **检测合并冲突 → 分析两侧代码 → 解决冲突 → 验证 → 提交** |

Archon 内置了 19 个默认工作流——运行 `archon workflow list`，或描述你的需求，路由模块会自动匹配最合适的工作流。

**或者自定义工作流。** 默认工作流是很好的起点——从 `.archon/workflows/defaults/` 复制一个并进行修改。工作流是位于 `.archon/workflows/` 的 YAML 文件，命令是位于 `.archon/commands/` 的 Markdown 文件。仓库中同名的文件会覆盖内置的默认配置。提交它们即可——你的团队将运行相同的流程。

详情请参阅 [创建工作流](https://archon.diy/guides/authoring-workflows/) 和 [创建命令](https://archon.diy/guides/authoring-commands/)。

## 接入平台

Web UI 和 CLI 开箱即用。可选择接入聊天平台以实现远程访问：

| Platform | 配置耗时 | 指南 |
|----------|-----------|-------|
| **Telegram** | 约 5 分钟 | [Telegram 指南](https://archon.diy/adapters/telegram/) |
| **Slack** | 约 15 分钟 | [Slack 指南](https://archon.diy/adapters/slack/) |
| **GitHub Webhooks** | 约 15 分钟 | [GitHub 指南](https://archon.diy/adapters/github/) |
| **Discord** | 约 5 分钟 | [Discord 指南](https://archon.diy/adapters/community/discord/) |

## 架构设计

```
┌─────────────────────────────────────────────────────────┐
│  Platform Adapters (Web UI, CLI, Telegram, Slack,       │
│                    Discord, GitHub)                     │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                     Orchestrator                        │
│          (Message Routing & Context Management)         │
└─────────────┬───────────────────────────┬───────────────┘
              │                           │
      ┌───────┴────────┐          ┌───────┴────────┐
      │                │          │                │
      ▼                ▼          ▼                ▼
┌───────────┐  ┌────────────┐  ┌──────────────────────────┐
│  Command  │  │  Workflow  │  │    AI Assistant Clients  │
│  Handler  │  │  Executor  │  │   (Claude / Codex / Pi)  │
│  (Slash)  │  │  (YAML)    │  │                          │
└───────────┘  └────────────┘  └──────────────────────────┘
      │              │                      │
      └──────────────┴──────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│             SQLite / PostgreSQL (12 Tables)             │
│  Codebases • Conversations • Sessions • Workflow Runs   │
│   Isolation Environments • Messages • Workflow Events   │
│    Users • User Identities • Workflow Node Sessions     │
│         Codebase Env Vars • User GitHub Tokens          │
└─────────────────────────────────────────────────────────┘
```

## 文档

完整文档请访问 **[archon.diy/docs](https://archon.diy/docs/)**。

| Topic | Description |
|-------|-------------|
| [Getting Started](https://archon.diy/getting-started/overview/) | 安装指南（Web UI 或 CLI） |
| [The Book of Archon](https://archon.diy/book/) | 10 章叙事式教程 |
| [CLI Reference](https://archon.diy/reference/cli/) | 完整 CLI 参考手册 |
| [Authoring Workflows](https://archon.diy/guides/authoring-workflows/) | 创建自定义 YAML 工作流 |
| [Authoring Commands](https://archon.diy/guides/authoring-commands/) | 创建可复用的 AI 命令 |
| [Configuration](https://archon.diy/reference/configuration/) | 所有配置选项、环境变量与 YAML 设置 |
| [AI Assistants](https://archon.diy/getting-started/ai-assistants/) | Claude、Codex 和 Pi 的详细配置 |
| [Deployment](https://archon.diy/deployment/) | Docker、VPS 及生产环境部署 |
| [Architecture](https://archon.diy/reference/architecture/) | 系统设计原理与内部机制 |
| [Troubleshooting](https://archon.diy/reference/troubleshooting/) | 常见问题与解决方案 |

**面向 AI 工具：** 将你的 LLM 指向 [`/llms.txt`](https://archon.diy/llms.txt) 获取所有文档索引，[`/llms-full.txt`](https://archon.diy/llms-full.txt) 获取单文件完整文档，或 [`/llms-small.txt`](https://archon.diy/llms-small.txt) 获取精简版。

## 遥测（Telemetry）

Archon 会发送少量匿名事件，以便维护者了解哪些工作流被实际使用、在哪些平台上运行以及执行是否成功——从而合理分配开发优先级。**绝不收集任何个人隐私信息（PII）。** 事件包括：`archon_started`（每次 CLI 调用或服务器启动时触发一次）、`workflow_invoked`（每次工作流启动）和 `workflow_completed` / `workflow_failed`（每次运行结果）。

**收集内容（仅限分类数据）：**
- **工作流名称** —— 对于*内置*（由 Archon 编写）的工作流显示真实名称；对你自定义的工作流统一标记为 `"custom"`，确保私有名称绝不会离开你的本地机器。
- **运行形态与结果** —— 平台（`cli`/`web`/`slack`/…）、提供商 ID（在 `workflow_invoked` 时包含模型 ID）、节点数量、使用的节点类型、成功/失败状态、耗时，以及分类错误原因（绝不包含原始错误文本）。
- **机器环境** —— 操作系统、架构、Archon 版本、运行环境、是否为二进制构建版，以及是否处于 CI 环境中。
- 存储在 `~/.archon/telemetry-id` 的随机安装 UUID。仅此而已。

**不收集的内容：** 你的代码、提示词（prompts）、消息内容、自定义工作流名称、工作流描述、git 远程仓库地址、文件路径、用户名、令牌（tokens）、AI 输出结果、错误文本、IP 地址、地理位置——全部不会收集。

**退出监控：** 在环境变量中设置以下任意一项即可：

```bash
ARCHON_TELEMETRY_DISABLED=1
DO_NOT_TRACK=1        # de facto standard honored by Astro, Bun, Prisma, Nuxt, etc.
POSTHOG_API_KEY=off   # off | 0 | false | disabled | "" all disable
```

CI 环境（`CI=true`）会自动禁用——在 GitHub Actions、CircleCI 等中运行测试用例的 Fork 仓库不会发送事件。

**查看当前状态：** 运行 `archon telemetry status` 可查看遥测是否启用、未启用的原因（如有）、安装 UUID 及活跃主机。运行 `archon telemetry reset` 可轮换安装 UUID。`archon doctor` 的检查清单中也会显示当前状态。

通过设置 `POSTHOG_API_KEY` 和 `POSTHOG_HOST`，可自行托管 PostHog 或使用其他项目实例。

## 贡献指南

欢迎贡献代码！请查看开放的 [Issues](https://github.com/coleam00/Archon/issues) 了解可参与的任务。

提交 Pull Request 前，请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## Star History

[![Star History Chart](https://api.star-history.com/chart?repos=coleam00/Archon&type=date&legend=top-left)](https://www.star-history.com/?repos=coleam00%2FArchon&type=date&legend=top-left)

## License

[MIT](LICENSE)