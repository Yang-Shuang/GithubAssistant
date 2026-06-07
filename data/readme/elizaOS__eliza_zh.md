<div align="center">
  <img src="packages/shared/assets/banners/elizaos_banner.svg" alt="elizaOS" width="100%" />
  <h1>elizaOS</h1>
  <p><strong>一个用于构建自主 AI 智能体的开源框架。</strong></p>
</div>

## ✨ 什么是 Eliza？

elizaOS 是一个一体化、可扩展的平台，用于构建和部署由 AI 驱动的应用。无论你是要创建复杂的聊天机器人、用于业务流程自动化的自主智能体（autonomous agents），还是智能游戏 NPC，Eliza 都能为你提供快速上手并高效扩展所需的全部工具。

它结合了模块化架构、强大的 CLI 和丰富的 Web 界面，让你完全掌控智能体的开发、部署与管理生命周期。

完整指南与 API 参考请访问官方 **[文档](https://docs.elizaos.ai/)**。

## 🚀 核心特性

- 🔌 **丰富的连接性**：开箱即用的 Discord、Telegram、Farcaster 等连接器。
- 🧠 **模型无关（Model Agnostic）**：支持所有主流模型，包括 OpenAI、Gemini、Anthropic、Llama 和 Grok。
- 🖥️ **现代化 Web UI**：专业的仪表盘，用于实时管理智能体、群组及对话。
- 🤖 **多智能体架构（Multi-Agent Architecture）**：专为创建和编排专业智能体群组而设计。
- 📄 **文档处理**：轻松导入文档，让智能体检索信息并基于你的数据回答问题（RAG）。
- 🛠️ **高度可扩展**：通过强大的插件系统构建你自己的功能。
- 📦 **开箱即用（It Just Works）**：从第一天起即可无缝安装与开发。

> **寻找插件？** 浏览公共插件目录 **[plugins.elizacloud.ai](https://plugins.elizacloud.ai)**。社区注册表条目维护在此 monorepo 的 [`packages/registry`](packages/registry) 下，带有 `elizaos` 关键词的 npm 包无需注册表条目即可被发现。

## 框架、项目与应用插件

elizaOS 是一个框架及其上层构建包。明确你正在使用的层级，有助于避免项目、插件和应用入口相互混淆。

**框架（Framework）**：即运行时环境，包含 `@elizaos/core`、智能体循环（agent loop）、插件模型（actions, providers, services）、消息/内存/状态原语，以及模型无关的 LLM 层。如果你的代码依赖 `@elizaos/core`，说明你正在使用框架。

**项目（Project）**：基于框架构建的可部署产品工作区。一个生成的项目拥有自己的品牌应用外壳（app shell），通常位于该项目工作区的 `apps/app` 目录下。

**应用插件（App Plugin）**：一种运行时插件，同时为 Eliza 提供应用界面入口。官方应用插件位于 [`plugins/app-*`](plugins) 下，npm 包名如 `@elizaos/plugin-companion`，通过包名加载。它们是插件，而非顶层仓库应用。

目录树中的分层同样清晰可见：

```
packages/        ← framework and shared packages
  core/          # @elizaos/core — runtime, types, agent loop
  agent/         # @elizaos/agent — AgentRuntime + plugin loader
  app-core/      # API + dashboard host
  elizaos/       # the `elizaos` CLI
  prompts/       # shared prompt scaffolding
  ui/            # shared React component library
  examples/      # standalone examples (chat, discord, mcp, ...)
  benchmarks/    # evaluation suites (gaia, swe_bench, tau-bench, ...)

plugins/         ← runtime plugins and app plugins
  app-companion/ app-browser/ app-documents/ app-phone/
  app-task-coordinator/ app-training/ plugin-form/ ...
  plugin-discord/ plugin-openai/ plugin-sql/ ...

packages/elizaos/templates/   ← CLI scaffolds + min-project / min-plugin for APP/PLUGIN create
```

*插件（Plugin）* 处于两者之间：它具备框架结构（向运行时注册 actions/providers/services），但打包和消费方式如同产品。社区插件通过 npm 元数据发现，并通过仓库内的 [`packages/registry`](packages/registry) 目录进行策展管理。

## 选择你的起点

| 你想实现…                                                  | 从这里开始                                    |
| ------------------------------------------------------------- | --------------------------------------------- |
| 5 分钟内体验一个智能体                                     | [CLI 快速入门](#cli-quick-start)           |
| 在你的 TypeScript 代码中直接使用运行时（无需 CLI，无需 UI） | [独立使用](#standalone-usage)         |
| 构建新的可部署产品                                | [创建新项目](#create-a-new-project) |
| 构建运行时插件（action / provider / service）          | [创建新插件](#create-a-new-plugin)   |
| 查看他人的实现方式                                         | [示例](#examples)                         |
| 评估或基准测试一个智能体                                | [基准测试](#benchmarks)                     |
| 阅读文档                                                 | [docs.elizaos.ai](https://docs.elizaos.ai/)   |

## CLI 快速入门

**前置条件：** [Node.js v24+](https://nodejs.org/)、[bun](https://bun.sh/docs/installation)。在 Windows 上，请使用 [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual)。

```bash
bun add -g elizaos
elizaos create my-first-agent --template project
cd my-first-agent
# add OPENAI_API_KEY=... to .env (or your provider's key)
bun install
bun run dev
```

生成的项目会暴露你日常使用的运行时脚本：`bun run dev`、`bun run build`、`bun run test`、`bun run typecheck`、`bun run lint`、`bun run verify`。`elizaos` CLI 本身刻意保持精简——它的职责是脚手架生成（`elizaos create`）和模板升级（`elizaos upgrade`）。如需查看可用模板列表，请运行 `elizaos info`。

完整参考：`elizaos --help` 或 `elizaos <command> --help`。

## 本地模拟栈（Mock Stack）

一条命令即可启动包含模拟数据（Hetzner + control-plane + cloud-api with `MOCK_REDIS` + PGlite，以及 cloud-frontend）的完整本地云栈：

```bash
bun run cloud:mock          # boot with existing PGlite data
bun run cloud:mock:fresh    # wipe PGlite + re-run migrations first
```

端口会自动分配并在启动横幅中打印；日志流式输出至 `./.logs/<service>.log`。向 `bun scripts/cloud/mock-stack-up.mjs` 传递 `--help` 可查看所有参数（跳过特定服务、固定端口等）。按 Ctrl+C 会按逆序安全关闭整个栈。

## 独立使用（Standalone Usage）

直接使用 `@elizaos/core` ——无需 CLI，无需仪表盘，仅在代码中引入运行时。

```bash
git clone --filter=blob:none https://github.com/elizaos/eliza.git
cd eliza
bun install

# Interactive REPL against a real agent
OPENAI_API_KEY=your_key bun run packages/examples/chat/chat.ts
```

[`packages/examples/`](packages/examples) 中几乎每个入口都有可运行的示例，共计 30+ 个。每个示例都拥有独立的 README 并可独立运行。这是最快了解框架独立运作方式的方法。详见下方 [示例](#examples)。

> **关于部分克隆（Partial Clone）**：`--filter=blob:none` 会保留完整的提交历史，但按需拉取文件内容——体积缩小约 10 倍。`git log`、分支操作和 `git checkout` 均可正常使用；首次使用 `git blame` 或 `git log -p` 时会触发按需拉取。如需后续升级：执行 `git config --unset remote.origin.partialclonefilter && git fetch --refetch`。对于一次性 CI 任务，使用 `--depth=1 --single-branch` 体积更小。

## 创建新项目

项目是基于运行时构建的独立产品工作区：包含品牌应用外壳、本地 eliza 检出代码、插件选择、平台配置及部署脚本。提供两种路径：

**1. CLI 脚手架（推荐）**

```bash
elizaos create my-app --template project
cd my-app
bun install
bun run dev
```

项目模板会搭建完整的工作区，包含本地 eliza 检出代码、默认插件（`plugin-sql`、`plugin-elizacloud`、`plugin-local-ai`、`plugin-ollama`）以及一个 Vite + React UI，你可立即编辑。

**2. 直接复制模板**。[`packages/elizaos/templates/min-project/`](packages/elizaos/templates/min-project) 是最小的应用结构——包含 Vite + React UI、一个带单个 action 的运行时 `Plugin`、`package.json` 中的 `elizaos.app` 元数据块，以及 vitest 冒烟测试。阅读 [`packages/elizaos/templates/min-project/SCAFFOLD.md`](packages/elizaos/templates/min-project/SCAFFOLD.md) 了解需替换的占位符及验证契约。

如需查看官方应用插件参考，请浏览 [`plugins/app-*`](plugins)。按复杂度递增的几个起点：

- [`app-companion`](plugins/plugin-companion) — 以聊天为主、带自定义 React UI 的助手。
- [`app-browser`](plugins/app-browser) — 智能体驱动的浏览器自动化。
- [`app-documents`](plugins/plugin-documents) — 基于用户文档的 RAG（支持全局/所有者私有/用户私有/智能体私有作用域）。
- [`app-phone`](plugins/plugin-phone) — 语音与电话交互入口。
- [`plugin-form`](plugins/plugin-form) — 表单驱动的数据收集。
- [`app-task-coordinator`](plugins/plugin-task-coordinator) — 多智能体编排。
- [`app-training`](plugins/plugin-training) — 轨迹捕获 + 原生提示词优化。

## 创建新插件

*插件（Plugin）* 通过 actions、providers 或 services 扩展运行时，无需 UI。

```bash
elizaos create my-plugin -t plugin
cd my-plugin
bun install
bun run build
```

或直接复制 [`packages/elizaos/templates/min-plugin/`](packages/elizaos/templates/min-plugin)。详见 [`packages/elizaos/templates/min-plugin/SCAFFOLD.md`](packages/elizaos/templates/min-plugin/SCAFFOLD.md) 中的契约说明。

当类型检查、代码规范检查和测试均通过后，使用 `elizaos` 关键词发布至 npm。如需申请策展收录，请在 [`packages/registry/entries/third-party`](packages/registry/entries/third-party) 添加条目并发起 Pull Request。

## 示例（Examples）

[`packages/examples/`](packages/examples) — 30+ 个可运行参考项目，涵盖连接器、集成方案、托管目标及游戏玩法。每个子目录均可独立构建，且拥有独立的 README。

| 分类             | 示例                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 对话交互       | [`chat`](packages/examples/chat)、[`discord`](packages/examples/discord)、[`telegram`](packages/examples/telegram)、[`farcaster`](packages/examples/farcaster)、[`farcaster-miniapp`](packages/examples/farcaster-miniapp)、[`twitter-xai`](packages/examples/twitter-xai)、[`bluesky`](packages/examples/bluesky) |
| Web 框架       | [`next`](packages/examples/next)、[`react`](packages/examples/react)、[`html`](packages/examples/html)、[`browser-extension`](packages/examples/browser-extension)、[`rest-api`](packages/examples/rest-api)                                                                                                       |
| 托管 / Serverless | [`vercel`](packages/examples/vercel)、[`cloudflare`](packages/examples/cloudflare)、[`gcp`](packages/examples/gcp)、[`aws`](packages/examples/aws)、[`supabase`](packages/examples/supabase)、[`convex`](packages/examples/convex)                                                                                 |
| 协议            | [`mcp`](packages/examples/mcp)、[`a2a`](packages/examples/a2a)                                                                                                                                                                                                                                                     |
| 链上 / 交易   | [`polymarket`](packages/examples/polymarket)、[`trader`](packages/examples/trader)、[`lp-manager`](packages/examples/lp-manager)                                                                                                                                                                                   |
| 趣味 / 游戏          | [`tic-tac-toe`](packages/examples/tic-tac-toe)、[`text-adventure`](packages/examples/text-adventure)、[`game-of-life`](packages/examples/game-of-life)、[`roblox`](packages/examples/roblox)、[`elizagotchi`](packages/examples/elizagotchi)                                                                       |
| 其他                | [`autonomous`](packages/examples/autonomous)、[`avatar`](packages/examples/avatar)、[`code`](packages/examples/code)、[`form`](packages/examples/form)、[`moltbook`](packages/examples/moltbook)、[`_plugin`](packages/examples/_plugin)                                                                           |

## 基准测试（Benchmarks）

[`packages/benchmarks/`](packages/benchmarks) — 30+ 个评估套件，用于衡量智能体能力。每个套件位于独立子目录中，拥有专属的测试运行器与 README。

| 分类           | 基准测试                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通用智能体      | [`gaia`](packages/benchmarks/gaia)、[`agentbench`](packages/benchmarks/agentbench)、[`tau-bench`](packages/benchmarks/tau-bench)、[`gauntlet`](packages/benchmarks/gauntlet)、[`realm`](packages/benchmarks/realm)、[`trust`](packages/benchmarks/trust)、[`experience`](packages/benchmarks/experience)                     |
| 编程             | [`swe_bench`](packages/benchmarks/swe_bench)、[`bfcl`](packages/benchmarks/bfcl)、[`mint`](packages/benchmarks/mint)                                                                                                                                                                                                         |
| OS / 桌面       | [`OSWorld`](packages/benchmarks/OSWorld)、[`terminal-bench`](packages/benchmarks/terminal-bench)                                                                                                                                                                                                                             |
| Web                | [`mind2web`](packages/benchmarks/mind2web)、[`webshop`](packages/benchmarks/webshop)                                                                                                                                                                                                                                         |
| 链上 / 交易   | [`HyperliquidBench`](packages/benchmarks/HyperliquidBench)、[`solana`](packages/benchmarks/solana)、[`evm`](packages/benchmarks/evm)、[`vending-bench`](packages/benchmarks/vending-bench)                                                                                                                                   |
| 语音 / 多模态 | [`voicebench`](packages/benchmarks/voicebench)                                                                                                                                                                                                                                                                               |
| 专项测试        | [`adhdbench`](packages/benchmarks/adhdbench)、[`clawbench`](packages/benchmarks/clawbench)、[`openclaw-benchmark`](packages/benchmarks/openclaw-benchmark)、[`woobench`](packages/benchmarks/woobench)、[`rlm-bench`](packages/benchmarks/rlm-bench)、[`social-alpha`](packages/benchmarks/social-alpha)                     |
| elizaOS 专属   | [`app-eval`](packages/benchmarks/app-eval)、[`configbench`](packages/benchmarks/configbench)、[`context-bench`](packages/benchmarks/context-bench)、[`framework`](packages/benchmarks/framework)、[`orchestrator`](packages/benchmarks/orchestrator)、[`orchestrator_lifecycle`](packages/benchmarks/orchestrator_lifecycle) |

编排驱动的基准测试运行手册位于 [`packages/benchmarks/ORCHESTRATOR_SUBAGENT_BENCHMARK_RUNBOOK.md`](packages/benchmarks/ORCHESTRATOR_SUBAGENT_BENCHMARK_RUNBOOK.md)。允许基准测试驱动 Eliza 智能体的适配器位于 [`packages/benchmarks/eliza-adapter`](packages/benchmarks/eliza-adapter)。综合结果查看器位于 [`packages/benchmarks/viewer`](packages/benchmarks/viewer)。

## 在 Monorepo 中工作

```bash
bun install            # workspace install
bun run dev            # API + Vite UI for apps/app
bun run build          # turbo build across the workspace
bun run lint           # turbo lint across the workspace
bun run test           # full test suite (packages/scripts/run-all-tests.mjs)
```

核心框架包说明：

- **[`@elizaos/core`](packages/core)** — 运行时、类型定义、智能体循环。该框架的起点与终点所在包。
- **[`@elizaos/agent`](packages/agent)** — `AgentRuntime`、插件加载器、默认插件映射表。
- **[`@elizaos/app-core`](packages/app-core)** — 运行智能体的 Express API + 仪表盘宿主服务。
- **[`elizaos`](packages/elizaos)** — `elizaos` CLI：提供 `create`、`info`、`upgrade`、`version` 命令。
- **[`@elizaos/prompts`](packages/prompts)** — 共享提示词脚手架。
- **[`@elizaos/ui`](packages/ui)** — 共享 React 组件库。
- **[`plugins/`](plugins)** — 连接器与能力模块（Telegram、Discord、Farcaster、Twitter/X、浏览器、视频、TEE 等）。

## 贡献指南

欢迎贡献代码。在提交非 trivial 的 PR 前，请先创建 Issue 进行讨论。

- [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md)
- [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md)

## License

MIT — 详见 [LICENSE](LICENSE)。

## Contributors

<a href="https://github.com/elizaos/eliza/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=elizaos/eliza" alt="Eliza project contributors" />
</a>