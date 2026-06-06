<div align="center">
    <img src="./media/logo_large.webp" alt="Spec Kit Logo" width="200" height="200"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>Build high-quality software faster.</em></h3>
</div>

<p align="center">
    <strong>一个开源工具包，让你能够专注于产品场景和可预期的结果，而不是从零开始进行 vibe coding（氛围编程）。</strong>
</p>

<p align="center">
    <a href="https://github.com/github/spec-kit/releases/latest"><img src="https://img.shields.io/github/v/release/github/spec-kit" alt="Latest Release"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="License"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Documentation"/></a>
</p>

---

## 目录

- [🤔 什么是规范驱动开发？](#-what-is-spec-driven-development)
- [⚡ 快速开始](#-get-started)
- [📽️ 视频概览](#️-video-overview)
- [🌍 社区](#-community)
- [🤖 支持的 AI 编程 Agent 集成](#-supported-ai-coding-agent-integrations)
- [🔧 Specify CLI 参考文档](#-specify-cli-reference)
- [🧩 自定义 Spec Kit：扩展与预设](#-making-spec-kit-your-own-extensions--presets)
- [📚 核心理念](#-core-philosophy)
- [🌟 开发阶段](#-development-phases)
- [🎯 实验目标](#-experimental-goals)
- [🔧 前置条件](#-prerequisites)
- [📖 了解更多](#-learn-more)
- [📋 详细流程](#-detailed-process)
- [💬 支持](#-support)
- [🙏 致谢](#-acknowledgements)
- [📄 许可证](#-license)

## 🤔 什么是规范驱动开发？

规范驱动开发（Spec-Driven Development）**颠覆了传统软件开发模式**。几十年来，代码一直占据核心地位——规范只是我们在开始“真正”编码工作前搭建并丢弃的脚手架。规范驱动开发改变了这一现状：**规范变为可执行的**，直接生成可用的实现，而不仅仅是指导它们。

## ⚡ 快速开始

### 1. 安装 Specify CLI

需要 **[uv](https://docs.astral.sh/uv/)**（[安装 uv](./docs/install/uv.md)）。将 `vX.Y.Z` 替换为 [Releases](https://github.com/github/spec-kit/releases) 中的最新版本号：

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

查看 [安装指南](./docs/installation.md) 以了解其他安装方法、验证方式、升级步骤及故障排除。

### 2. 初始化项目

```bash
specify init my-project --integration copilot
cd my-project
```

### 3. 建立项目原则

在项目中启动你的编程 Agent。大多数 Agent 提供了 `/speckit.*` 斜杠命令；Codex CLI（skills 模式）则使用 `$speckit-*`。

使用 **`/speckit.constitution`** 命令创建项目的治理原则和开发规范，这些内容将指导后续的所有开发工作。

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 4. 创建规范（Spec）

使用 **`/speckit.specify`** 命令描述你想构建的内容。重点在于 **做什么（what）** 和 **为什么做（why）**，而不是技术栈。

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 5. 创建技术实现计划

使用 **`/speckit.plan`** 命令提供你的技术栈和架构选择。

```bash
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 6. 拆解为任务

使用 **`/speckit.tasks`** 从实现计划中生成可执行的任务列表。

```bash
/speckit.tasks
```

### 7. 执行实现

使用 **`/speckit.implement`** 执行所有任务，并按计划构建功能。

```bash
/speckit.implement
```

查看详细步骤说明，请参阅我们的 [综合指南](./spec-driven.md)。

## 📽️ 视频概览

想看看 Spec Kit 的实际效果吗？观看我们的 [视频概览](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)!

[![Spec Kit video header](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🌍 社区

在 [Spec Kit 文档站点](https://github.github.io/spec-kit/) 探索社区贡献的资源：

- [Extensions（扩展）](https://github.github.io/spec-kit/community/extensions.html) — 命令、钩子和功能
- [Presets（预设）](https://github.github.io/spec-kit/community/presets.html) — 模板和术语覆盖配置
- [Walkthroughs（ walkthrough ）](https://github.github.io/spec-kit/community/walkthroughs.html) — 端到端 SDD 场景演示
- [Friends（合作伙伴项目）](https://github.github.io/spec-kit/community/friends.html) — 基于 Spec Kit 扩展或构建的项目

> [!NOTE]
> 社区贡献由各自作者独立创建和维护。安装和使用前请自行审查源代码，风险自负。

想参与贡献？请参阅 [扩展发布指南](extensions/EXTENSION-PUBLISHING-GUIDE.md) 或 [预设发布指南](presets/PUBLISHING.md)。

## 🤖 支持的 AI 编程 Agent 集成

Spec Kit 支持 30+ 种 AI 编程 Agent——包括 CLI 工具和 IDE 内置助手。完整列表、说明及使用详情请参阅 [支持的 AI 编程 Agent 集成](https://github.github.io/spec-kit/reference/integrations.html) 指南。

运行 `specify integration list` 查看当前已安装版本支持的所有集成。

## 可用的斜杠命令（Slash Commands）

运行 `specify init` 后，你的 AI 编程 Agent 将可以使用以下斜杠命令进行结构化开发。对于支持 skills 模式的集成，传递 `--integration <agent> --integration-options="--skills"` 会安装 agent skills 而非斜杠命令提示文件。

#### 核心命令（Core Commands）

规范驱动开发工作流所需的基础命令：

| Command                  | Agent Skill            | Description                                                                |
| ------------------------ | ---------------------- | -------------------------------------------------------------------------- |
| `/speckit.constitution`  | `speckit-constitution` | 创建或更新项目治理原则与开发规范                                           |
| `/speckit.specify`       | `speckit-specify`      | 定义你想构建的内容（需求与用户故事）                                       |
| `/speckit.plan`          | `speckit-plan`         | 使用你选择的技术栈创建技术实现计划                                         |
| `/speckit.tasks`         | `speckit-tasks`        | 生成可执行的任务列表                                                       |
| `/speckit.taskstoissues` | `speckit-taskstoissues`| 将生成的任务列表转换为 GitHub Issues，用于跟踪与执行                       |
| `/speckit.implement`     | `speckit-implement`    | 执行所有任务，按计划构建功能                                               |

#### 可选命令（Optional Commands）

用于增强质量保障和验证的附加命令：

| Command              | Agent Skill            | Description                                                                                                                          |
| -------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/speckit.clarify`   | `speckit-clarify`      | 澄清未明确定义的部分（建议在 `/speckit.plan` 之前使用；原为 `/quizme`）                                                              |
| `/speckit.analyze`   | `speckit-analyze`      | 跨工件一致性与覆盖率分析（在 `/speckit.tasks` 之后、`/speckit.implement` 之前运行）                                                  |
| `/speckit.checklist` | `speckit-checklist`    | 生成自定义质量检查清单，验证需求的完整性、清晰度和一致性（例如“英语单元测试”）                                                       |

## 🔧 Specify CLI 参考文档

如需完整的命令详情、选项和示例，请参阅 [CLI 参考](https://github.github.io/spec-kit/reference/overview.html)。

## 🧩 自定义 Spec Kit：扩展与预设

Spec Kit 可通过两套互补的系统——**扩展（Extensions）** 和 **预设（Presets）**——以及项目级本地覆盖配置来定制你的需求：

| Priority | Component Type                                    | Location                         |
| -------: | ------------------------------------------------- | -------------------------------- |
|      ⬆ 1 | Project-Local Overrides                           | `.specify/templates/overrides/`  |
|        2 | Presets — Customize core & extensions             | `.specify/presets/templates/`    |
|        3 | Extensions — Add new capabilities                 | `.specify/extensions/templates/` |
|      ⬇ 4 | Spec Kit Core — Built-in SDD commands & templates | `.specify/templates/`            |

- **模板（Templates）** 在 **运行时解析** —— Spec Kit 自上而下遍历配置栈，并使用第一个匹配项。
- 项目级本地覆盖（`.specify/templates/overrides/`）允许你为单个项目进行一次性调整，而无需创建完整的预设。
- **扩展/预设命令** 在 **安装时应用** —— 当你运行 `specify extension add` 或 `specify preset add` 时，命令文件会被写入 agent 目录（例如 `.claude/commands/`）。
- 如果多个预设或扩展提供了相同的命令，优先级最高的版本生效。移除后，次高优先级的版本会自动恢复。
- 如果没有覆盖配置或自定义项，Spec Kit 将使用其核心默认值。

### 扩展（Extensions）—— 添加新功能

当你需要超出 Spec Kit 核心功能的能力时，请使用 **扩展**。扩展会引入新命令和模板——例如，添加内置 SDD 命令未涵盖的领域特定工作流、集成外部工具，或增加全新的开发阶段。它们扩展了 *Spec Kit 能做什么*。

```bash
# Search available extensions
specify extension search

# Install an extension
specify extension add <extension-name>
```

例如，扩展可以添加 Jira 集成、实现后代码审查、V-Model 测试追溯性或项目健康诊断功能。

请参阅 [扩展参考](https://github.github.io/spec-kit/reference/extensions.html) 获取完整命令指南。浏览 [社区扩展](https://github.github.io/spec-kit/community/extensions.html) 查看可用内容。

### 预设（Presets）—— 定制现有工作流

当你想改变 *Spec Kit 的工作方式* 而不添加新功能时，请使用 **预设**。预设会覆盖核心功能及已安装扩展中附带的模板和命令——例如，强制执行面向合规的规范格式、使用领域特定术语，或将组织标准应用于计划和任务。它们定制化 Spec Kit 及其扩展生成的工件和指令。

```bash
# Search available presets
specify preset search

# Install a preset
specify preset add <preset-name>
```

例如，预设可以重构规范模板以要求监管追溯性、使工作流适应你使用的方法论（如敏捷、看板、瀑布、Jobs-to-be-Done 或领域驱动设计）、在计划中添加强制安全审查节点、强制执行测试优先的任务排序，或将整个工作流本地化为其他语言。[pirate-speak 演示](https://github.com/mnriem/spec-kit-pirate-speak-preset-demo) 展示了定制能力的深度。多个预设可以按优先级堆叠使用。

请参阅 [预设参考](https://github.github.io/spec-kit/reference/presets.html) 获取完整命令指南，包括解析顺序和优先级堆栈说明。

### 何时使用哪种？

| Goal | Use |
| --- | --- |
| 添加全新命令或工作流 | Extension（扩展） |
| 定制规范、计划或任务的格式 | Preset（预设） |
| 集成外部工具或服务 | Extension（扩展） |
| 强制执行组织或监管标准 | Preset（预设） |
| 分发可复用的领域特定模板 | 两者皆可 —— 使用预设覆盖模板，使用扩展捆绑带新命令的模板 |

## 📚 核心理念

规范驱动开发是一种强调以下内容的结构化流程：

- **意图驱动开发**：在“怎么做（how）”之前，先由规范定义“做什么（what）”
- **丰富的规范创建**：利用护栏机制和组织原则进行规范编写
- **多步迭代优化**：而非通过单次提示词生成代码
- **高度依赖** 先进 AI 模型能力来解析和规范执行

## 🌟 开发阶段

| Phase                                    | Focus                    | Key Activities                                                                                                                                                     |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0-to-1 Development（“Greenfield”）**   | Generate from scratch    | <ul><li>从高层需求开始</li><li>生成规范</li><li>规划实现步骤</li><li>构建生产级应用</li></ul>                                                                      |
| **Creative Exploration**                 | Parallel implementations | <ul><li>探索多样化解决方案</li><li>支持多种技术栈与架构</li><li>实验 UX 模式</li></ul>                                                                            |
| **Iterative Enhancement（“Brownfield”）** | Brownfield modernization | <ul><li>迭代添加功能</li><li>现代化遗留系统</li><li>适配现有流程</li></ul>                                                                                         |

## 🎯 实验目标

我们的研究与实验聚焦于：

### 技术无关性（Technology independence）

- 使用多样化的技术栈创建应用
- 验证假设：规范驱动开发是一种不绑定特定技术、编程语言或框架的流程

### 企业级约束（Enterprise constraints）

- 演示关键业务应用的开发流程
- 整合组织约束（云提供商、技术栈、工程实践）
- 支持企业设计系统与合规要求

### 以用户为中心的开发（User-centric development）

- 为不同用户群体和偏好构建应用
- 支持多种开发方式（从 vibe coding 到 AI-native 开发）

### 创意与迭代流程（Creative & iterative processes）

- 验证并行实现探索的概念
- 提供稳健的迭代功能开发工作流
- 扩展流程以处理升级和现代化任务

## 🔧 前置条件

- **Linux/macOS/Windows**
- [支持的](#-supported-ai-coding-agent-integrations) AI 编程 Agent。
- [uv](https://docs.astral.sh/uv/)（推荐）或 [pipx](https://pipx.pypa.io/) 用于包管理
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

如果你在使用某个 Agent 时遇到问题，请提交 Issue，以便我们优化集成。

## 📖 了解更多

- **[完整规范驱动开发方法论](./spec-driven.md)** - 深入全流程解析
- **[详细 Walkthrough](#-detailed-process)** - 逐步实现指南

---

## 📋 详细流程

<details>
<summary>点击展开详细步骤演示</summary>

你可以使用 Specify CLI 引导项目，这会将所需的工件引入你的环境。运行：

```bash
specify init <project_name>
```

或在当前目录初始化：

```bash
specify init .
# or use the --here flag
specify init --here
# Skip confirmation when the directory already has files
specify init . --force
# or
specify init --here --force
```

![Specify CLI bootstrapping a new project in the terminal](./media/specify_cli.gif)

在交互式终端中，系统会提示你选择正在使用的编程 Agent 集成。在非交互会话（如 CI 或管道运行）中，除非传递 `--integration`，否则 `specify init` 默认使用 GitHub Copilot。你也可以直接在终端主动指定集成：

```bash
specify init <project_name> --integration copilot
specify init <project_name> --integration gemini
specify init <project_name> --integration codex

# Or in current directory:
specify init . --integration copilot
specify init . --integration codex --integration-options="--skills"

# or use --here flag
specify init --here --integration copilot
specify init --here --integration codex --integration-options="--skills"

# Force merge into a non-empty current directory
specify init . --force --integration copilot

# or
specify init --here --force --integration copilot
```

CLI 会检查你是否安装了 Claude Code、Gemini CLI、Cursor CLI、Qwen CLI、opencode、Codex CLI、Qoder CLI、Tabnine CLI、Kiro CLI、Pi、Forge、Goose 或 Mistral Vibe。如果没有安装，或者你希望跳过工具检测直接获取模板，请在命令中添加 `--ignore-agent-tools`：

```bash
specify init <project_name> --integration copilot --ignore-agent-tools
```

### **STEP 1：** 建立项目原则

进入项目文件夹并运行你的编程 Agent。在我们的示例中，使用的是 `claude`。

![Bootstrapping Claude Code environment](./media/bootstrap-claude-code.gif)

如果你能看到 `/speckit.constitution`、`/speckit.specify`、`/speckit.plan`、`/speckit.tasks` 和 `/speckit.implement` 命令可用，说明配置正确。

第一步应使用 `/speckit.constitution` 命令建立项目的治理原则。这有助于确保后续所有开发阶段中决策的一致性：

```text
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements. Include governance for how these principles should guide technical decisions and implementation choices.
```

此步骤会创建或更新 `.specify/memory/constitution.md` 文件，其中包含项目的指导方针。编程 Agent 将在规范、规划和实现阶段引用这些内容。

### **STEP 2：** 创建项目规范

建立项目原则后，你现在可以创建功能规范。使用 `/speckit.specify` 命令，然后提供你想开发的具体需求。

> [!IMPORTANT]
> 尽可能明确地描述 *你要构建什么* 以及 *为什么*。**此时不要关注技术栈**。

示例提示词：

```text
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up. For each task in the UI for a task card,
you should be able to change the current status of the task between the different columns in the Kanban work board.
You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task
card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick
from. There will be no password required. When you click on a user, you go into the main view, which displays the list of
projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns.
You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are
assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly
see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can
delete any comments that you made, but you can't delete comments anybody else made.
```

输入此提示词后，你应该看到 Claude Code 启动规划和规范起草流程。Claude Code 还会触发一些内置脚本来设置仓库。

完成此步骤后，你应该会看到一个新分支（例如 `001-create-taskify`），以及 `specs/001-create-taskify` 目录下的新规范文件。

生成的规范应包含一组用户故事和功能需求，具体格式遵循模板定义。

此时，你的项目文件夹结构应如下所示：

```text
.
├── .specify
│   ├── memory
│   │   └── constitution.md
│   ├── scripts
│   │   └── bash
│   │       ├── check-prerequisites.sh
│   │       ├── common.sh
│   │       ├── create-new-feature.sh
│   │       ├── setup-plan.sh
│   │       └── setup-tasks.sh
│   └── templates
│       ├── plan-template.md
│       ├── spec-template.md
│       └── tasks-template.md
└── specs
    └── 001-create-taskify
        └── spec.md
```

### **STEP 3：** 功能规范澄清（规划前必需）

基础规范创建完成后，你可以继续澄清第一轮尝试中未充分捕获的需求。

你应在**创建技术计划之前**运行结构化澄清工作流，以减少下游返工。

推荐顺序：

1. 使用 `/speckit.clarify`（结构化）——基于覆盖率的顺序提问，并将答案记录在“Clarifications”部分。
2. 如果仍有模糊之处，可选择性地跟进自由形式的细化讨论。

如果你有意跳过澄清步骤（例如进行技术预研或探索性原型开发），请明确说明，以免 Agent 因缺少澄清而阻塞。

示例自由形式细化提示词（如需在 `/speckit.clarify` 之后继续使用）：

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

你还应要求 Claude Code 验证 **Review & Acceptance Checklist**，勾选已满足要求的项，未满足的保持空白。可使用以下提示词：

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

务必将此次与 Claude Code 的交互视为澄清和提问规范的机会——**不要将其首次尝试视为最终结果**。

### **STEP 4：** 生成计划

现在你可以明确指定技术栈和其他技术要求。你可以使用项目模板内置的 `/speckit.plan` 命令，配合类似以下的提示词：

```text
We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use
Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API,
tasks API, and a notifications API.
```

此步骤的输出将包含一系列实现细节文档，你的目录结构大致如下：

```text
.
├── CLAUDE.md
├── .specify
│   ├── memory
│   │   └── constitution.md
│   ├── scripts
│   │   └── bash
│   │       ├── check-prerequisites.sh
│   │       ├── common.sh
│   │       ├── create-new-feature.sh
│   │       ├── setup-plan.sh
│   │       └── setup-tasks.sh
│   └── templates
│       ├── CLAUDE-template.md
│       ├── plan-template.md
│       ├── spec-template.md
│       └── tasks-template.md
└── specs
    └── 001-create-taskify
        ├── contracts
        │   ├── api-spec.json
        │   └── signalr-spec.md
        ├── data-model.md
        ├── plan.md
        ├── quickstart.md
        ├── research.md
        └── spec.md
```

检查 `research.md` 文档，确保根据你的指令使用了正确的技术栈。如果某些组件不合适，你可以要求 Claude Code 进行优化，甚至让它检查你本地安装的框架/平台版本（例如 .NET）。

此外，如果你选择的快速迭代的技术栈（如 .NET Aspire、JS 框架）需要更多细节，可以要求 Claude Code 进行研究，提示词示例：

```text
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

在此过程中，你可能会发现 Claude Code 卡在错误的研究方向上——你可以通过类似提示词引导它回到正轨：

```text
I think we need to break this down into a series of steps. First, identify a list of tasks
that you would need to do during implementation that you're not sure of or would benefit
from further research. Write down a list of those tasks. And then for each one of these tasks,
I want you to spin up a separate research task so that the net results is we are researching
all of those very specific tasks in parallel. What I saw you doing was it looks like you were
researching .NET Aspire in general and I don't think that's gonna do much for us in this case.
That's way too untargeted research. The research needs to help you solve a specific targeted question.
```

> [!NOTE]
> Claude Code 可能会过于积极，添加你未要求的组件。要求它澄清变更的理由和来源。

### **STEP 5：** 让 Claude Code 验证计划

计划就位后，你应该让 Claude Code 通读一遍，确保没有遗漏。可使用类似提示词：

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

这有助于细化实现计划，并帮你避免 Claude Code 在规划周期中可能遗漏的盲点。初步优化完成后，在进入实施阶段前，要求 Claude Code 再次过一遍检查清单。

如果你已安装 [GitHub CLI](https://docs.github.com/en/github-cli/github-cli)，还可以让 Claude Code 从当前分支向 `main` 创建 PR，并附带详细描述，以确保工作被正确跟踪。

> [!NOTE]
> 在让 Agent 实施之前，也值得提示 Claude Code 交叉核对细节，查看是否存在过度设计（记住——它可能过于积极）。如果存在过度设计的组件或决策，可要求 Claude Code 解决。确保 Claude Code 遵循 `.specify/memory/constitution.md` 中的规范，这是制定计划时必须遵守的基础文件。

### **STEP 6：** 使用 `/speckit.tasks` 生成任务拆解

实现计划验证通过后，你现在可以将计划拆解为具体、可执行的任务，并按正确顺序执行。使用 `/speckit.tasks` 命令自动生成详细的任务拆解：

```text
/speckit.tasks
```

此步骤会在你的功能规范目录中创建一个 `tasks.md` 文件，包含以下内容：

- **按用户故事组织的工作项** - 每个用户故事成为一个独立的实现阶段，拥有自己的任务集
- **依赖管理** - 任务排序尊重组件间的依赖关系（例如先模型后服务，先服务后接口）
- **并行执行标记** - 可并行的任务标有 `[P]` 以优化开发工作流
- **文件路径规范** - 每个任务包含实施应发生的确切文件路径
- **测试驱动开发结构** - 如果请求了测试，将包含测试任务并按顺序安排在实现之前编写
- **检查点验证** - 每个用户故事阶段都包含用于验证独立功能的检查点

生成的 `tasks.md` 为 `/speckit.implement` 命令提供了清晰路线图，确保系统化实施、保持代码质量，并支持用户故事的增量交付。

### **STEP 7：** 实现

准备就绪后，使用 `/speckit.implement` 命令执行你的实现计划：

```text
/speckit.implement
```

`/speckit.implement` 命令将：

- 验证所有前置条件是否就位（规范、宪法、计划和任务）
- 解析 `tasks.md` 中的任务拆解
- 按正确顺序执行任务，尊重依赖关系和并行标记
- 遵循你任务计划中定义的 TDD 方法
- 提供进度更新并妥善处理错误

> [!IMPORTANT]
> 编程 Agent 将执行本地 CLI 命令（如 `dotnet`、`npm` 等）——请确保你的机器上已安装所需工具。

实现完成后，测试应用并解决 CLI 日志中可能不可见的任何运行时错误（例如浏览器控制台报错）。你可以将这些错误复制粘贴回你的编程 Agent 进行修复。

</details>

---

## 💬 支持

如需支持，请提交 [GitHub Issue](https://github.com/github/spec-kit/issues/new)。我们欢迎 Bug 报告、功能请求以及关于使用规范驱动开发的提问。

## 🙏 致谢

本项目深受并基于 [John Lam](https://github.com/jflam) 的工作与研究。

## 📄 许可证

本项目采用 MIT 开源许可证条款。完整条款请参阅 [LICENSE](./LICENSE) 文件。