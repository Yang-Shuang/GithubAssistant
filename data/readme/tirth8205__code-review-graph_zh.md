<h1 align="center">code-review-graph</h1>

<p align="center">
  <strong>停止浪费 Token。开始更智能地进行代码审查。</strong>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.ja-JP.md">日本語</a> |
  <a href="README.ko-KR.md">한국어</a> |
  <a href="README.hi-IN.md">हिन्दी</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/code-review-graph/"><img src="https://img.shields.io/pypi/v/code-review-graph?style=flat-square&color=blue" alt="PyPI"></a>
  <a href="https://pepy.tech/project/code-review-graph"><img src="https://img.shields.io/pepy/dt/code-review-graph?style=flat-square" alt="Downloads"></a>
  <a href="https://github.com/tirth8205/code-review-graph/stargazers"><img src="https://img.shields.io/github/stars/tirth8205/code-review-graph?style=flat-square" alt="Stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT Licence"></a>
  <a href="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml"><img src="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square" alt="Python 3.10+"></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-compatible-green.svg?style=flat-square" alt="MCP"></a>
  <a href="https://code-review-graph.com"><img src="https://img.shields.io/badge/website-code--review--graph.com-blue?style=flat-square" alt="Website"></a>
  <a href="https://discord.gg/3p58KXqGFN"><img src="https://img.shields.io/badge/discord-join-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord"></a>
</p>

<br>

AI 编程工具在审查任务中可能会反复重读代码库的很大一部分。`code-review-graph` 解决了这个问题。它使用 [Tree-sitter](https://tree-sitter.github.io/tree-sitter/) 构建代码的结构化映射，增量跟踪变更，并通过 [MCP](https://modelcontextprotocol.io/) 为你的 AI 助手提供精确上下文，使其仅读取关键内容。

<p align="center">
  <img src="diagrams/diagram1_before_vs_after.png" alt="The Token Problem: 38x to 528x token reduction across 6 real repositories" width="85%" />
</p>

---

## 快速开始 (Quick Start)

```bash
pip install code-review-graph                     # or: pipx install code-review-graph
code-review-graph install          # auto-detects and configures all supported platforms
code-review-graph build            # parse your codebase
```

一条命令即可完成全部配置。`install` 会自动检测你已安装的 AI 编程工具，为每个工具写入正确的 MCP 配置，在支持的情况下安装平台原生钩子（hooks）或技能（skills），并将图感知指令注入到平台规则中。它会自动检测你是通过 `uvx` 还是 `pip`/`pipx` 安装的，并生成相应的配置。安装完成后请重启编辑器/工具。

<p align="center">
  <img src="diagrams/diagram8_supported_platforms.png" alt="One Install, Every Platform: auto-detects Codex, Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, Gemini CLI, Qwen, Qoder, Kiro, and GitHub Copilot" width="85%" />
</p>

若要针对特定平台：

```bash
code-review-graph install --platform codex       # configure only Codex
code-review-graph install --platform cursor      # configure only Cursor
code-review-graph install --platform claude-code  # configure only Claude Code
code-review-graph install --platform gemini-cli   # configure only Gemini CLI
code-review-graph install --platform kiro         # configure only Kiro
code-review-graph install --platform copilot      # configure only GitHub Copilot (VS Code)
code-review-graph install --platform copilot-cli  # configure only GitHub Copilot CLI
```

需要 Python 3.10+。为获得最佳体验，建议安装 [uv](https://docs.astral.sh/uv/)（如果可用，MCP 配置将使用 `uvx`，否则回退到直接使用 `code-review-graph` 命令）。

然后打开你的项目并询问 AI 助手：

```
Build the code review graph for this project
```

对于包含 500 个文件的项目，初始构建耗时约 10 秒。之后，监听模式（watch mode）和受支持的钩子可以自动保持图结构的更新。


## 工作原理 (How It Works)

<p align="center">
  <img src="diagrams/diagram7_mcp_integration_flow.png" alt="How your AI assistant uses the graph: User asks for review, AI checks MCP tools, graph returns blast radius and risk scores, AI reads only what matters" width="80%" />
</p>

你的代码库通过 Tree-sitter 被解析为抽象语法树（AST），存储为由节点（函数、类、导入项）和边（调用、继承、测试覆盖）组成的图结构，然后在审查时进行查询，以计算 AI 助手需要读取的最小文件集。

<p align="center">
  <img src="diagrams/diagram2_architecture_pipeline.png" alt="Architecture pipeline: Repository to Tree-sitter Parser to SQLite Graph to Blast Radius to Minimal Review Set" width="100%" />
</p>

### 爆炸半径（Blast-radius）分析

当某个文件发生变更时，图结构会追踪所有可能受影响的调用方、依赖项和测试用例。这就是变更的“爆炸半径”。你的 AI 助手仅读取这些文件，而无需扫描整个项目。

<p align="center">
  <img src="diagrams/diagram3_blast_radius.png" alt="Blast radius visualization showing how a change to login() propagates to callers, dependents, and tests" width="70%" />
</p>

### 增量更新耗时 < 2 秒

当启用钩子或监听模式时，文件保存和受支持的提交钩子会触发增量更新。图结构会对变更文件进行差异比对，通过 SHA-256 哈希检查查找其依赖项，并仅重新解析发生变更的部分。一个包含 2,900 个文件的项目可在不到 2 秒内完成重新索引。

<p align="center">
  <img src="diagrams/diagram4_incremental_update.png" alt="Incremental update flow: supported hook or watch update triggers diff, finds dependents, re-parses only 5 files while 2,910 are skipped" width="90%" />
</p>

### 解决单体仓库（Monorepo）难题

大型单体仓库是 Token 浪费最严重的地方。图结构能过滤掉无关噪音 —— 从审查上下文中排除 27,700+ 个文件，实际仅读取约 15 个文件。

<p align="center">
  <img src="diagrams/diagram6_monorepo_funnel.png" alt="code-review-graph repo: 208,821 source tokens funnel down to ~2,495 token graph responses — 93x fewer tokens per question" width="80%" />
</p>

### 广泛的语言支持与 Jupyter Notebook

<p align="center">
  <img src="diagrams/diagram9_language_coverage.png" alt="Language coverage organized by category: Web, Backend, Systems, Mobile, Scripting, Config, plus Jupyter and Databricks notebook support" width="90%" />
</p>

解析器支持覆盖当前解析范围内的函数、类、导入项、调用点、继承和测试检测，在可用时使用 Tree-sitter，并在需要时提供针对性回退方案。目前支持 Python、JavaScript/TypeScript/TSX、Go、Rust、Java、C/C++、C#、Ruby、Kotlin、Swift、PHP、Scala、Solidity、Dart、R、Perl、Lua/Luau、Objective-C、Shell 脚本、Elixir、Zig、PowerShell、Julia、ReScript、GDScript、Nix、Verilog/SystemVerilog、SQL、Vue/Svelte SFCs、通过 TypeScript 解析器处理的 Astro 文件、Jupyter/Databricks Notebook（`.ipynb`）以及 Perl XS 文件（`.xs`）。

---

## 基准测试 (Benchmarks)

<p align="center">
  <img src="diagrams/diagram5_benchmark_board.png" alt="Benchmarks across 6 real repositories: 38x to 528x token reduction, 100% impact recall, 0.71 average F1" width="85%" />
</p>

所有数据均基于针对 6 个真实开源仓库（共 13 次提交）的自动化评估运行器得出。每个配置都固定了上游 SHA，Leiden 社区检测算法使用固定随机种子，且 CPU 上的嵌入向量是确定性的 —— 因此在不同机器上运行的两次结果完全一致。完整的复现步骤及预期输出位于 [`docs/REPRODUCING.md`](docs/REPRODUCING.md)。

<details>
<summary><strong>Token 效率：每次提问减少 38x – 528x Token（全文库 vs 图查询）</strong></summary>
<br>

对于典型的 Agent 提问（如 `"how does authentication work"`、`"what is the main entry point"` 等），图结构会返回约 2,000–3,500 个 Token 的精准搜索结果及邻居边，而不是强制 Agent 读取每个源文件。下表数据基于 `code_review_graph/token_benchmark.py` 中定义的 5 个示例问题的平均值。

| Repo | Snapshot SHA | naive_corpus_tokens | avg graph_tokens | Reduction |
|------|---|-----------------:|----------------:|----------:|
| fastapi | `0227991a` | 951,071 | 2,169 | **528.4x** |
| code-review-graph | `84bde354` | 208,821 | 2,495 | **93.0x** |
| gin | `5c00df8a` | 166,868 | 1,990 | **91.8x** |
| flask | `a29f88ce` | 125,022 | 1,986 | **71.4x** |
| express | `b4ab7d65` | 135,955 | 3,465 | **40.6x** |
| httpx | `b55d4635` | 89,492 | 2,438 | **38.0x** |

6 个仓库的范围：**38x – 528x**（每次提问的中位数减少约 82x）。

形式化的 `eval/benchmarks/token_efficiency.py` 基准测试衡量的是另一种场景 —— 完整的 `get_review_context()` JSON 与仅包含提交变更文件内容的对比，因此对于小提交的比率低于 1。这是因为审查上下文响应携带了影响半径边及源代码片段，其大小超过了单个文件的微小差异。这并非 Bug；两个基准测试回答的是不同的问题。完整方法论见 [`docs/REPRODUCING.md`](docs/REPRODUCING.md)。

自 v2.3.4 起，审查和影响工具会附加一个紧凑的 `context_savings` 估算值，以便 MCP 客户端查看每次调用大约节省了多少上下文。在 v2.3.5 中，CLI 将其作为上方显示的带框 `Token Savings` 面板展示（见“用法”部分的“节省 Token 面板”），并新增 `--verify` 参数以与 OpenAI 的 `cl100k_base` 分词器进行交叉验证。[`docs/REPRODUCING.md`](docs/REPRODUCING.md) 中的校准数据显示，在 222 个示例文件的整体统计中，该估算值与实际 GPT-4 Token 的差异约为 ~1%。

</details>

<details>
<summary><strong>影响准确性：召回率 100%，平均 F1 分数 0.71</strong></summary>
<br>

爆炸半径分析在全部 13 次评估提交中均达到 100% 的召回率。在某些情况下会出现过度预测，这是一种保守权衡：标记过多文件比漏掉损坏的依赖项更安全。

| Repo | Commits | Avg F1 | Avg Precision | Recall |
|------|--------:|-------:|--------------:|-------:|
| httpx | 2 | 0.864 | 0.786 | 1.0 |
| fastapi | 2 | 0.834 | 0.750 | 1.0 |
| code-review-graph | 2 | 0.734 | 0.584 | 1.0 |
| express | 2 | 0.667 | 0.500 | 1.0 |
| flask | 2 | 0.628 | 0.481 | 1.0 |
| gin | 3 | 0.609 | 0.439 | 1.0 |
| **Average** | **13** | **0.714** | **0.578** | **1.000** |

</details>

<details>
<summary><strong>构建性能</strong></summary>
<br>

| Repo | Files | Nodes | Edges | Flow Detection | Search Latency |
|------|------:|------:|------:|---------------:|---------------:|
| express | 141 | 1,910 | 17,553 | 106ms | 0.7ms |
| fastapi | 1,122 | 6,285 | 27,117 | 128ms | 1.5ms |
| flask | 83 | 1,446 | 7,974 | 95ms | 0.7ms |
| gin | 99 | 1,286 | 16,762 | 111ms | 0.5ms |
| httpx | 60 | 1,253 | 7,896 | 96ms | 0.4ms |

</details>

<details>
<summary><strong>局限性与已知弱点</strong></summary>
<br>

- **小型单文件变更：** 对于琐碎的编辑，图上下文可能比直接读取文件消耗更多 Token（参见上方 express 的结果）。开销来自于启用多文件分析所需的结构化元数据。
- **搜索质量 (MRR 0.35)：** 关键词搜索在大多数查询中能于前 4 个结果中找到正确答案，但排序仍需改进。Express 的查询因模块模式命名返回了 0 次命中。
- **流程检测（召回率 33%）：仅在 Python 仓库（fastapi, httpx）中可靠检测到入口点**，因为这些框架的模式被识别出来。JavaScript 和 Go 的流程检测仍需改进。
- **精确度与召回率的权衡：** 影响分析故意保持保守。它会标记 *可能* 受影响的文件，这意味着在大型依赖图中会出现一些误报。

</details>

---

## 功能特性 (Features)

| Feature | Details |
|---------|---------|
| **增量更新** | 仅重新解析变更的文件。后续更新可在不到 2 秒内完成。 |
| **广泛的语言与 Notebook 支持** | Python、JavaScript/TypeScript/TSX、Go、Rust、Java、C/C++、C#、Ruby、Kotlin、Swift、PHP、Scala、Solidity、Dart、R、Perl、Lua/Luau、Objective-C、Shell 脚本、Elixir、Zig、PowerShell、Julia、ReScript、GDScript、Nix、Verilog/SystemVerilog、SQL、Vue/Svelte SFCs、通过 TypeScript 解析器处理的 Astro 文件、Jupyter/Databricks (.ipynb)、Perl XS (.xs) |
| **爆炸半径分析** | 显示哪些函数、类和文件可能受变更影响 |
| **自动更新钩子** | 钩子和监听模式可在文件保存和受支持的提交钩子时更新图结构 |
| **语义搜索** | 可选的向量嵌入，支持 sentence-transformers、Google Gemini、MiniMax 或任何 OpenAI 兼容端点（真实 OpenAI、Azure、new-api、LiteLLM、vLLM、LocalAI） |
| **交互式可视化** | D3.js 力导向图，支持搜索、社区图例切换和按度缩放节点 |
| **枢纽与桥梁检测** | 通过介数中心性（betweenness centrality）查找连接最密集的节点及架构瓶颈 |
| **意外耦合评分** | 检测非预期的耦合：跨社区、跨语言、边缘到枢纽的边 |
| **知识缺口分析** | 识别孤立节点、未测试的热区、稀疏社区和结构弱点 |
| **建议问题** | 基于图分析（桥梁、枢纽、异常）自动生成审查问题 |
| **边置信度** | 三级置信度评分（EXTRACTED/INFERRED/AMBIGUOUS），边附带浮点分数 |
| **图遍历** | 支持从任意节点进行自由形式的 BFS/DFS 探索，可配置深度和 Token 预算 |
| **导出格式** | GraphML (Gephi/yEd)、Neo4j Cypher、带 wikilinks 的 Obsidian vault、SVG 静态图 |
| **图差异对比** | 比较不同时间的图快照：新增/删除的节点、边和社区变化 |
| **Token 基准测试** | 测量原始全文库 Token 与图查询 Token，提供每次提问的比例 |
| **估算上下文节省** | 在相关 MCP/CLI 审查输出上附加紧凑的 `context_savings` 元数据，标记为估算值且仅保留三个小字段 |
| **记忆循环 (Memory loop)** | 将问答结果持久化为 Markdown 以便重新摄入，使图结构随查询不断成长 |
| **社区自动拆分** | 过大的社区（>25% 的图）通过 Leiden 算法递归拆分 |
| **执行流程** | 从入口点追踪调用链，按加权关键性排序 |
| **社区检测** | 使用 Leiden 算法聚类相关代码，针对大图进行分辨率缩放 |
| **架构概览** | 自动生成带耦合警告的架构图 |
| **风险评分审查** | `detect_changes` 将差异映射到受影响的函数、流程和测试缺口 |
| **重构工具** | 重命名预览、框架感知的死代码检测、社区驱动的建议 |
| **Wiki 生成** | 基于社区结构自动生成 Markdown Wiki |
| **多仓库注册表** | 注册多个仓库，跨所有仓库进行搜索 |
| **多仓库守护进程 (Daemon)** | `crg-daemon` 以子进程方式监听多个仓库，具备健康检查与自动重启功能 |
| **MCP Prompts** | 5 个工作流模板：review、architecture、debug、onboard、pre-merge |
| **全文搜索** | 基于 FTS5 的混合搜索，结合关键词与向量相似度 |
| **本地存储** | SQLite 文件位于 `.code-review-graph/`。核心图存储无需外部数据库或云服务。 |
| **监听模式 (Watch mode)** | 在开发过程中持续更新图结构 |

---

## 用法 (Usage)

<details>
<summary><strong>斜杠命令</strong></summary>
<br>

| Command | Description |
|---------|-------------|
| `/code-review-graph:build-graph` | 构建或重建代码图 |
| `/code-review-graph:review-delta` | 审查自上次提交以来的变更 |
| `/code-review-graph:review-pr` | 完整的 PR 审查，含爆炸半径分析 |

</details>

<details>
<summary><strong>CLI 参考</strong></summary>
<br>

```bash
code-review-graph install          # Auto-detect and configure all platforms
code-review-graph install --platform <name>  # Target a specific platform
code-review-graph build            # Parse entire codebase
code-review-graph update           # Incremental update (changed files only)
code-review-graph status           # Graph statistics
code-review-graph watch            # Auto-update on file changes
code-review-graph visualize        # Generate interactive HTML graph
code-review-graph visualize --format graphml   # Export as GraphML
code-review-graph visualize --format svg       # Export as SVG
code-review-graph visualize --format obsidian  # Export as Obsidian vault
code-review-graph visualize --format cypher    # Export as Neo4j Cypher
code-review-graph wiki             # Generate markdown wiki from communities
code-review-graph detect-changes --brief         # Risk panel + token savings (read-only)
code-review-graph update --brief                 # Refresh graph + same panel
code-review-graph detect-changes --brief --verify  # Cross-check vs tiktoken
code-review-graph register <path>  # Register repo in multi-repo registry
code-review-graph unregister <id>  # Remove repo from registry
code-review-graph repos            # List registered repositories
code-review-graph daemon start     # Start multi-repo watch daemon
code-review-graph daemon stop      # Stop the daemon
code-review-graph daemon status    # Show daemon status and repos
code-review-graph eval             # Run evaluation benchmarks
code-review-graph serve            # Start MCP server
```

</details>

<details>
<summary><strong>节省 Token 面板：<code>detect-changes --brief</code> vs <code>update --brief</code></strong></summary>
<br>

两个命令都会打印相同的紧凑面板，显示图结构为你节省了多少 Token（相比直接将变更文件交给 Agent）。它们的**唯一区别**在于：是否先刷新图结构。

```text
┌─────────────────────── Token Savings ────────────────────────┐
│ Full context would be:     12,921 tokens                     │
│ Graph context used:           762 tokens                     │
│ Saved:                     12,159 tokens (~94%)              │
│ Breakdown: Functions 244 · Tests 191 · Risk 244 · Other 83   │
└──────────────────────────────────────────────────────────────┘
```

| Command | What it does | When to use |
|---|---|---|
| `detect-changes --brief` | **只读。** 查看当前变更，查询**现有**图结构，打印面板。约需 1 秒。 | 大多数情况 —— 钩子（或 `crg-daemon`）会在后台保持图结构新鲜，因此这通常已足够。 |
| `update --brief` | **先将你的变更文件重新解析到图中**，然后打印相同的面板。约需 5 秒。 | 执行 rebase、处理大型变更集后，或任何你怀疑图结构已过时的时候。 |

两者最终都会输出**相同的面板**，因为它们都在末尾调用了相同的 `analyze_changes()` 步骤。区别在于运行该分析前图结构本身是否已刷新。

向任一命令添加 `--verify` 参数，即可将显示的数值与 OpenAI 的 `cl100k_base` 分词器（GPT-4 系列）进行交叉验证。需要执行 `pip install tiktoken`。在典型变更集上，估算值与实际 Token 的差异保持在 ~1% 以内 —— 校准数据见 [`docs/REPRODUCING.md`](docs/REPRODUCING.md)。

相同的 `context_savings` 元数据也会自动附加到 `get_impact_radius`、`get_review_context`、`detect_changes` 和 `get_architecture_overview` MCP 工具的 JSON 响应中，因此 AI Agent 可以在聊天界面中将节省情况展示给用户，无需额外提示。

</details>

<details>
<summary><strong>多仓库守护进程 (Daemon)</strong></summary>
<br>

如果你的编辑器不支持钩子（例如 Cursor、OpenCode），或者你只是希望图结构在后台保持新鲜而无需任何编辑器集成，那么守护进程非常适合你。它会监听你的仓库文件变更并自动重建图 —— 无需手动执行 `build` 或 `update` 命令。

该守护进程已包含在 `code-review-graph` 中 —— 无需单独安装。

**快速设置：**

```bash
# 1. 注册你要监听的仓库
crg-daemon add ~/project-a --alias proj-a
crg-daemon add ~/project-b

# 2. 启动守护进程（后台运行）
crg-daemon start

# 3. 完成 —— 图结构会自动保持更新
crg-daemon status                 # check daemon and per-repo watcher status
crg-daemon logs --repo proj-a -f  # tail logs for a specific repo
crg-daemon stop                   # stop daemon and all watcher processes
```

也可通过 `code-review-graph daemon start|stop|status|...` 使用。

底层机制上，`crg-daemon add` 会写入位于 `~/.code-review-graph/watch.toml` 的 TOML 配置文件。你也可以直接编辑此文件：

```toml
[[repos]]
path = "/home/user/project-a"
alias = "proj-a"

[[repos]]
path = "/home/user/project-b"
alias = "project-b"
```

守护进程会监控此配置文件的变更，并在添加或移除仓库时自动启动/停止监听进程。每 30 秒执行一次健康检查以重启死掉的监听器。无需外部依赖。

完整配置参考及所有可用选项见 [docs/COMMANDS.md](docs/COMMANDS.md#standalone-daemon-cli-crg-daemon)。

</details>

<details>
<summary><strong>30 个 MCP 工具</strong></summary>
<br>

图结构构建完成后，你的 AI 助手会自动使用这些工具。

| Tool | Description |
|------|-------------|
| `build_or_update_graph_tool` | 构建或增量更新图结构 |
| `run_postprocess_tool` | 重新运行流程检测、社区检测和 FTS 索引 |
| `get_minimal_context_tool` | 超紧凑上下文（约 100 Token）—— 请优先调用此项 |
| `get_impact_radius_tool` | 变更文件的爆炸半径 |
| `get_review_context_tool` | 经 Token 优化的审查上下文，含结构摘要 |
| `query_graph_tool` | 调用方、被调函数、测试、导入项、继承查询 |
| `traverse_graph_tool` | 从任意节点进行 BFS/DFS 遍历，支持 Token 预算 |
| `semantic_search_nodes_tool` | 按名称或含义搜索代码实体 |
| `embed_graph_tool` | 计算向量嵌入以用于语义搜索 |
| `list_graph_stats_tool` | 图大小与健康状态 |
| `get_docs_section_tool` | 检索文档章节 |
| `find_large_functions_tool` | 查找超过行数阈值的函数/类 |
| `list_flows_tool` | 按关键性排序列出执行流程 |
| `get_flow_tool` | 获取单个执行流程的详情 |
| `get_affected_flows_tool` | 查找受变更文件影响的流程 |
| `list_communities_tool` | 列出检测到的代码社区 |
| `get_community_tool` | 获取单个社区的详情 |
| `get_architecture_overview_tool` | 基于社区结构的架构概览 |
| `detect_changes_tool` | 用于代码审查的风险评分变更影响分析 |
| `get_hub_nodes_tool` | 查找连接最密集的节点（架构热区） |
| `get_bridge_nodes_tool` | 通过介数中心性查找瓶颈 |
| `get_knowledge_gaps_tool` | 识别结构弱点与未测试的热区 |
| `get_surprising_connections_tool` | 检测非预期的跨社区耦合 |
| `get_suggested_questions_tool` | 基于分析结果自动生成审查问题 |
| `refactor_tool` | 重命名预览、死代码检测、建议 |
| `apply_refactor_tool` | 应用之前预览的重构操作 |
| `generate_wiki_tool` | 基于社区生成 Markdown Wiki |
| `get_wiki_page_tool` | 检索特定 Wiki 页面 |
| `list_repos_tool` | 列出已注册的仓库 |
| `cross_repo_search_tool` | 跨所有注册仓库进行搜索 |

**MCP Prompts**（5 个工作流模板）：
`review_changes`, `architecture_map`, `debug_issue`, `onboard_developer`, `pre_merge_check`

</details>

<details>
<summary><strong>配置</strong></summary>
<br>

若要从索引中排除特定路径，请在你的仓库根目录创建 `.code-review-graphignore` 文件：

```
generated/**
*.generated.ts
vendor/**
node_modules/**
```

注意：在 git 仓库中，仅索引已跟踪的文件（`git ls-files`），因此被 gitignore 忽略的文件会自动跳过。使用 `.code-review-graphignore` 可排除已跟踪的文件，或在无法使用 git 时生效。

可选依赖分组：

```bash
pip install code-review-graph[embeddings]          # Local vector embeddings (sentence-transformers)
pip install code-review-graph[google-embeddings]   # Google Gemini embeddings
pip install code-review-graph[communities]         # Community detection (igraph)
pip install code-review-graph[enrichment]          # Python call-resolution enrichment (Jedi)
pip install code-review-graph[eval]                # Evaluation benchmarks (matplotlib)
pip install code-review-graph[wiki]                # Wiki generation with LLM summaries (ollama)
pip install code-review-graph[all]                 # All optional dependencies
```

### 环境变量

| Variable | Description | Default |
|----------|-------------|---------|
| `CRG_GIT_TIMEOUT` | Git 操作的超时时间（秒） | `30` |
| `CRG_DATA_DIR` | 覆盖图数据库和生成图工件的目录 | - |
| `CRG_EMBEDDING_MODEL` | 向量嵌入的默认模型 | `all-MiniLM-L6-v2` |
| `CRG_ACCEPT_CLOUD_EMBEDDINGS` | 在明确确认后抑制云嵌入出站警告 | - |
| `CRG_ALLOW_REMOTE_CODE` | 允许需要 `trust_remote_code=True` 的 HuggingFace 模型 | `0` |
| `CRG_MAX_IMPACT_NODES` | 影响分析中包含的最大节点数 | `500` |
| `CRG_MAX_IMPACT_DEPTH` | 爆炸半径分析的搜索深度 | `2` |
| `CRG_MAX_BFS_DEPTH` | 图遍历的最大深度 | `15` |
| `CRG_MAX_CHANGED_FUNCS` | 单次变更报告中分析的最大变更函数数 | `500` |
| `CRG_MAX_TRANSITIVE_FRONTIER` | 传递调用方/被调函数扩展的最大前沿大小 | `50` |
| `CRG_TOOL_TIMEOUT` | MCP 工具的可选超时时间（秒）（`0` 表示禁用超时） | `0` |
| `CRG_RECURSE_SUBMODULES` | 设置为 `1`、`true` 或 `yes` 时，在文件收集中包含 git 子模块 | - |
| `CRG_TOOLS` | 提供 MCP 服务时要暴露的 MCP 工具逗号分隔白名单 | - |
| `GOOGLE_API_KEY` | Google Gemini 嵌入的 API Key | - |
| `MINIMAX_API_KEY` | MiniMax 嵌入的 API Key | - |
| `CRG_OPENAI_BASE_URL` | OpenAI 兼容嵌入端点 | - |
| `CRG_OPENAI_API_KEY` | OpenAI 兼容嵌入的 API Key | - |
| `CRG_OPENAI_MODEL` | OpenAI 兼容嵌入的模型名称 | - |
| `CRG_OPENAI_DIMENSION` | 固定嵌入维度（v3 模型支持降维） | - |
| `NO_COLOR` | 若设置，则禁用终端中的 ANSI 颜色 | - |
| `CRG_SERIAL_PARSE` | 若为 `1`，则禁用并行解析（用于调试） | - |

OpenAI 兼容嵌入（真实 OpenAI、Azure 或任何自托管网关如 new-api / LiteLLM / vLLM / LocalAI / Ollama openai 模式）无需额外安装 —— 只需设置环境变量并将 `provider="openai"` 传递给 `embed_graph`：

```bash
export CRG_OPENAI_BASE_URL=http://127.0.0.1:3000/v1     # or https://api.openai.com/v1
export CRG_OPENAI_API_KEY=sk-...
export CRG_OPENAI_MODEL=text-embedding-3-small          # whatever your gateway serves
# optional:
export CRG_OPENAI_DIMENSION=1536                        # pin dim (v3 models support reduction)
export CRG_OPENAI_BATCH_SIZE=100                        # lower for gateways with tight limits
                                                        # (e.g. Qwen text-embedding-v4 caps at 10)
```

当基础 URL 指向本地主机（`127.0.0.1`、`localhost`、`0.0.0.0`、`::1`）时，会自动跳过云出站警告。

> **模型选择建议。** 避免使用 `-preview` / `-beta` / `-exp` 模型 ID（例如 `google/gemini-embedding-2-preview`）用于任何你计划长期保留的场景 —— 预览模型的权重可能发生变化（不同维度 → 需要完全重新嵌入），或在不通知的情况下被弃用。优先选择稳定的 GA 版本，如 `text-embedding-3-small` / `text-embedding-3-large`（OpenAI）、`Qwen/Qwen3-Embedding-8B`（通过自托管 vLLM / LocalAI）或 `gemini-embedding-001`（通过原生 Gemini 提供商，需使用 `GOOGLE_API_KEY` 而非 OpenAI 兼容路径）。
>
> 另请注意：`code-review-graph` 当前仅嵌入**函数签名**（每个节点约 ~10 Token，例如 `"parse_file function (path: str) returns Tree"`。对于 headline 质量依赖于长上下文主体理解的模型（如 Gemini 2 或 Qwen3-8B 在其 MTEB-code SOTA 分数下），在此输入长度下与较小模型的差距会显著缩小。主体/文档字符串嵌入已列为后续增强功能待办事项。

#### 工具过滤 (Tool Filtering)

CRG 默认暴露 30 个 MCP 工具。在 Token 受限的环境中，你可以使用 `--tools` 或 `CRG_TOOLS` 环境变量将服务器限制为子集工具：

```bash
# Via CLI flag
code-review-graph serve --tools query_graph_tool,semantic_search_nodes_tool,detect_changes_tool

# Via environment variable
CRG_TOOLS=query_graph_tool,semantic_search_nodes_tool code-review-graph serve
```

CLI 标志优先于环境变量。当两者均未设置时，所有工具均可用。这对于 MCP 客户端配置特别有用：

```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "code-review-graph",
      "args": ["serve", "--tools", "query_graph_tool,semantic_search_nodes_tool,detect_changes_tool,get_review_context_tool"]
    }
  }
}
```

</details>

---

## 故障排除 (Troubleshooting)

### `pip` / `pipx` 无法下载 `hatchling`（或出现 `Errno 9` / `Bad file descriptor`）

从**源码树**安装（例如 `pipx install .`）需要 **PyPI** 上的构建依赖项（例如 `hatchling`）。如果在连接警告后看到 `Could not find a version that satisfies the requirement hatchling`，说明该**终端**中的 Python/pip 可能无法向 `pypi.org` 打开 HTTPS 客户端（有时在集成编辑器终端中出现；VPN、防火墙或代理情况下系统级较少见）。

**解决方案：**

1. 改用 **macOS Terminal.app**（或 iTerm）运行相同命令，然后重试 `pipx install .` 或 `pipx install "git+https://..."`。
2. 使用 **[uv](https://docs.astral.sh/uv/)** 从签出的代码库安装 CLI（在许多情况下使用与 `pip` 不同的下载机制）：

   ```bash
   cd /path/to/code-review-graph
   uv tool install . --force
   ```

3. 对于**克隆版开发环境**且无需全局安装，可使用 `uv sync` 和 `uv run code-review-graph …`（或在 `uv sync` 后激活 `.venv`）。

**诊断（可选）：** `python3 scripts/diagnose_pypi_connectivity.py` —— 如果输出 `FAILED`，说明是环境/网络问题，而非本仓库中的包名错误。

### Windows 配置问题（无效 JSON / 连接关闭）
如果你正在使用 Windows，并通过 Claude Code 连接时遇到 `Invalid JSON: EOF while parsing` 或 `MCP error -32000: Connection closed`，请勿在配置中使用 `cmd /c` 包装器。

确保 `fastmcp` 已更新至至少 `3.2.4+`。然后，将你的 `~/.claude.json` 配置为直接执行 `.exe` 并通过配置传递 UTF-8 环境变量：

```json
"code-review-graph": {
  "command": "C:\\path\\to\\your\\venv\\Scripts\\code-review-graph.exe",
  "args": ["serve", "--repo", "C:\\path\\to\\your\\project"],
  "env": { "PYTHONUTF8": "1" }
}
```

## 贡献 (Contributing)

```bash
git clone https://github.com/tirth8205/code-review-graph.git
cd code-review-graph
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

<details>
<summary><strong>添加新语言支持</strong></summary>
<br>

编辑 `code_review_graph/parser.py`，将你的文件扩展名添加到 `EXTENSION_TO_LANGUAGE` 中，并在 `_CLASS_TYPES`、`_FUNCTION_TYPES`、`_IMPORT_TYPES` 和 `_CALL_TYPES` 中添加节点类型映射。包含测试用例并发起 PR。

</details>

## 许可协议 (Licence)

MIT。详见 [LICENSE](LICENSE)。

<p align="center">
<br>
<a href="https://code-review-graph.com">code-review-graph.com</a><br><br>
<code>pip install code-review-graph && code-review-graph install</code><br>
<sub>Works with Codex, Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, Gemini CLI, Qwen, Qoder, Kiro, GitHub Copilot, and GitHub Copilot CLI</sub>
</p>