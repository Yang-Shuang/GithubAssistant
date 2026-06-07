```markdown
  ██╗  ██╗███████╗ █████╗ ██████╗ ██████╗  ██████╗  ██████╗ ███╗   ███╗
  ██║  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
  ███████║█████╗  ███████║██║  ██║██████╔╝██║   ██║██║   ██║██╔████╔██║
  ██╔══██║██╔══╝  ██╔══██║██║  ██║██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
  ██║  ██║███████╗██║  ██║██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
                  AI 代理的上下文压缩层（Context Compression Layer）
```

<p align="center"><strong>减少 60–95% Token 消耗 · 库 · 代理 · MCP · 6 种算法 · 本地优先 · 可逆压缩</strong></p>

<p align="center">
  <a href="https://github.com/chopratejas/headroom/actions/workflows/ci.yml"><img src="https://github.com/chopratejas/headroom/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://app.codecov.io/gh/chopratejas/headroom"><img src="https://codecov.io/gh/chopratejas/headroom/graph/badge.svg" alt="codecov"></a>
  <a href="https://pypi.org/project/headroom-ai/"><img src="https://img.shields.io/pypi/v/headroom-ai.svg" alt="PyPI"></a>
  <a href="https://www.npmjs.com/package/headroom-ai"><img src="https://img.shields.io/npm/v/headroom-ai.svg" alt="npm"></a>
  <a href="https://huggingface.co/chopratejas/kompress-base"><img src="https://img.shields.io/badge/model-Kompress--base-yellow.svg" alt="Model: Kompress-base"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://headroom-docs.vercel.app/docs"><img src="https://img.shields.io/badge/docs-online-blue.svg" alt="Docs"></a>
</p>

<p align="center">
  <a href="https://headroom-docs.vercel.app/docs">文档</a> ·
  <a href="#get-started-60-seconds">安装</a> ·
  <a href="#proof">效果验证</a> ·
  <a href="#agent-compatibility-matrix">代理兼容</a> ·
  <a href="https://discord.gg/yRmaUNpsPJ">Discord</a> ·
  <a href="llms.txt">llms.txt</a>
</p>

<p align="center"><sub>
  <b>AI 代理 / LLM：</b>在此阅读 <a href="llms.txt"><code>/llms.txt</code></a>，或获取<a href="https://headroom-docs.vercel.app/llms.txt">实时索引</a> / <a href="https://headroom-docs.vercel.app/llms-full.txt">完整文档包</a>。
</sub></p>

---
<a href="https://trendshift.io/repositories/20881" target="_blank"><img src="https://trendshift.io/api/badge/repositories/20881" alt="chopratejas%2Fheadroom | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

> Headroom 会在数据到达 LLM 之前，压缩你的 AI 代理所读取的所有内容——包括工具输出、日志、RAG 分块、文件以及对话历史。答案不变，Token 消耗大幅减少。

<p align="center">
  <img src="HeadroomDemo-Fast.gif" alt="Headroom in action" width="820">
  <br/><sub>实时演示：10,144 → 1,260 Token —— 成功定位相同的 FATAL 错误。</sub>
</p>

## What it does（核心功能）

- **库（Library）** — 在 Python 或 TypeScript 中调用 `compress(messages)`，直接内联到任意应用中
- **代理（Proxy）** — 运行 `headroom proxy --port 8787`，零代码修改，支持任何语言
- **代理封装（Agent wrap）** — 一条命令执行 `headroom wrap claude|codex|cursor|aider|copilot`
- **MCP 服务端** — 为任意 MCP 客户端提供 `headroom_compress`、`headroom_retrieve`、`headroom_stats` 工具
- **跨代理记忆（Cross-agent memory）** — 在 Claude、Codex、Gemini 间共享存储，自动去重
- **`headroom learn`** ——挖掘失败会话，将修正内容写入 `CLAUDE.md` / `AGENTS.md`
- **可逆压缩（Reversible CCR）** — 原始数据永不删除；LLM 可按需检索

## How it works（30 seconds）

```
 Your agent / app
   (Claude Code, Cursor, Codex, LangChain, Agno, Strands, your own code…)
        │   prompts · tool outputs · logs · RAG results · files
        ▼
    ┌────────────────────────────────────────────────────┐
    │  Headroom   (runs locally — your data stays here)  │
    │  ────────────────────────────────────────────────  │
    │  CacheAligner  →  ContentRouter  →  CCR            │
    │                    ├─ SmartCrusher   (JSON)        │
    │                    ├─ CodeCompressor (AST)         │
    │                    └─ Kompress-base  (text, HF)    │
    │                                                    │
    │  Cross-agent memory  ·  headroom learn  ·  MCP     │
    └────────────────────────────────────────────────────┘
        │   compressed prompt  +  retrieval tool
        ▼
 LLM provider  (Anthropic · OpenAI · Bedrock · …)
```

- **ContentRouter** ——检测内容类型，选择对应的压缩器
- **SmartCrusher / CodeCompressor / Kompress-base** ——分别压缩 JSON、AST 或自然语言文本
- **CacheAligner** ——稳定前缀，确保提供商的 KV Cache 真正命中
- **CCR** ——在本地存储原始数据；LLM 如需调用则执行 `headroom_retrieve`

→ [架构设计](https://headroom-docs.vercel.app/docs/architecture) · [CCR 可逆压缩](https://headroom-docs.vercel.app/docs/ccr) · [Kompress-base 模型卡](https://huggingface.co/chopratejas/kompress-base)

## Get started（60 seconds）

```bash
# 1 — Install
pip install "headroom-ai[all]"          # Python
npm install headroom-ai                 # Node / TypeScript

# 2 — Pick your mode
headroom wrap claude                    # wrap a coding agent
headroom proxy --port 8787              # drop-in proxy, zero code changes
# or: from headroom import compress      # inline library

# 3 — See the savings
headroom stats
```

可选扩展模块：`[proxy]`、`[mcp]`、`[ml]`、`[agno]`、`[langchain]`、`[evals]`。需要 **Python 3.10+**。

## Proof（效果验证）

**真实代理工作负载的节省效果：**

| Workload                      | Before | After  | Savings |
|-------------------------------|-------:|-------:|--------:|
| Code search (100 results)     | 17,765 |  1,408 | **92%** |
| SRE incident debugging        | 65,694 |  5,118 | **92%** |
| GitHub issue triage           | 54,174 | 14,761 | **73%** |
| Codebase exploration          | 78,502 | 41,254 | **47%** |

**标准基准测试的准确率保持情况：**

| Benchmark  | Category | N   | Baseline | Headroom | Delta      |
|------------|----------|----:|---------:|---------:|------------|
| GSM8K      | Math     | 100 |    0.870 |    0.870 | **±0.000** |
| TruthfulQA | Factual  | 100 |    0.530 |    0.560 | **+0.030** |
| SQuAD v2   | QA       | 100 |        — |  **97%** | 19% compression |
| BFCL       | Tools    | 100 |        — |  **97%** | 32% compression |

复现命令：`python -m headroom.evals suite --tier 1` · [完整基准测试与方法论](https://headroom-docs.vercel.app/docs/benchmarks)

## Agent compatibility matrix（代理兼容性）

| Agent       | `headroom wrap` | Notes                            |
|-------------|:---------------:|----------------------------------|
| Claude Code | ●               | `--memory` · `--code-graph`      |
| Codex       | ●               | shares memory with Claude        |
| Cursor      | ●               | prints config — paste once       |
| Aider       | ●               | starts proxy + launches          |
| Copilot CLI | ●               | starts proxy + launches          |
| OpenClaw    | ●               | installs as ContextEngine plugin |

任何兼容 OpenAI 的客户端均可通过 `headroom proxy` 使用。原生支持 MCP：运行 `headroom mcp install`。

## When to use · When to skip（适用与不适用场景）

**适合使用的场景：**
- 日常使用 AI 编程代理，且希望在不修改代码的前提下节省 Token
- 跨多个代理工作，并需要共享记忆功能
- 需要可逆压缩——原始数据始终可通过 CCR 检索

**不建议使用的场景：**
- 仅使用单一提供商的原生压缩功能，且不需要跨代理记忆
- 在沙盒环境中工作，且无法运行本地进程

<details>
<summary><b>Integrations — drop Headroom into any stack</b></summary>

| Your setup             | Hook in with                                                     |
|------------------------|------------------------------------------------------------------|
| Any Python app         | `compress(messages, model=…)`                                    |
| Any TypeScript app     | `await compress(messages, { model })`                            |
| Anthropic / OpenAI SDK | `withHeadroom(new Anthropic())` · `withHeadroom(new OpenAI())`   |
| Vercel AI SDK          | `wrapLanguageModel({ model, middleware: headroomMiddleware() })` |
| LiteLLM                | `litellm.callbacks = [HeadroomCallback()]`                       |
| LangChain              | `HeadroomChatModel(your_llm)`                                    |
| Agno                   | `HeadroomAgnoModel(your_model)`                                  |
| Strands                | [Strands guide](https://headroom-docs.vercel.app/docs/strands)  |
| ASGI apps              | `app.add_middleware(CompressionMiddleware)`                      |
| Multi-agent            | `SharedContext().put / .get`                                     |
| MCP clients            | `headroom mcp install`                                           |

</details>

<details>
<summary><b>What's inside（核心组件）</b></summary>

- **SmartCrusher** — 通用 JSON 压缩：支持字典数组、嵌套对象及混合类型。
- **CodeCompressor** — AST 感知压缩，适用于 Python、JS、Go、Rust、Java、C++。
- **Kompress-base** — 我们的 HuggingFace 模型，基于代理交互轨迹训练而成。
- **Image compression** — 通过训练的 ML 路由器实现 40–90% 的图像体积缩减。
- **CacheAligner** ——稳定前缀，确保 Anthropic/OpenAI KV Cache 真正命中。
- **IntelligentContext** ——基于评分与学习到的重要性进行上下文适配。
- **CCR** — 可逆压缩；LLM 可按需检索原始数据。
- **Cross-agent memory** — 共享存储、代理溯源及自动去重。
- **SharedContext** — 跨多代理工作流的压缩上下文传递。
- **`headroom learn`** — 基于插件的失败挖掘机制，支持 Claude、Codex、Gemini。

</details>

<details>
<summary><b>Pipeline internals（流水线内部机制）</b></summary>

Headroom 在 `compress()`、SDK 和代理之间暴露了一套稳定的请求生命周期：

`Setup` → `Pre-Start` → `Post-Start` → `Input Received` → `Input Cached` → `Input Routed` → `Input Compressed` → `Input Remembered` → `Pre-Send` → `Post-Send` → `Response Received`

- **转换组件（Transforms）** 负责实际压缩：CacheAligner、ContentRouter、SmartCrusher、CodeCompressor、Kompress-base、IntelligentContext / RollingWindow。
- **流水线扩展**可通过 `on_pipeline_event(...)` 监听或自定义生命周期阶段。
- **压缩钩子（Hooks）**与标准生命周期并行，作为额外的扩展接口。
- **代理扩展**保留为 ASGI 中间件、路由及启动策略的服务器/应用集成接口。

针对特定提供商和工具的行为逻辑位于 `headroom/providers/` 目录下，以确保核心编排逻辑专注于生命周期、调度顺序与策略管理。

- **CLI/工具模块**：`headroom/providers/claude`、`copilot`、`codex`、`openclaw`
- **提供商运行时模块**：`headroom/providers/claude`、`gemini`，以及 `headroom/providers/registry.py` 中的共享后端/运行时分发逻辑
- **核心文件遵循编排优先原则**：`wrap.py`、`client.py`、`cli/proxy.py` 和 `proxy/server.py` 负责委派提供商特定的环境变量配置、API 目标标准化、后端选择及传输分发。

</details>

## Install（安装）

```bash
pip install "headroom-ai[all]"          # Python, everything
npm install headroom-ai                 # TypeScript / Node
docker pull ghcr.io/chopratejas/headroom:latest
```

可选扩展模块：`[proxy]`、`[mcp]`、`[ml]`（Kompress-base）、`[agno]`、`[langchain]`、`[evals]`。需要 **Python 3.10+**。

使用 `pipx`？请显式指定支持的 Python 解释器：

```bash
pipx install --python python3.13 "headroom-ai[all]"
```

→ [安装指南](https://headroom-docs.vercel.app/docs/installation) ——包含 Docker 标签、持久化服务、PowerShell 及 DevContainer 配置说明。

## headroom learn（失败学习）

<p align="center">
  <img src="headroom_learn.gif" alt="headroom learn in action" width="720">
</p>

**`headroom learn`** ——挖掘失败会话，将修正内容写入 `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`。

## Documentation（文档）

| Start here                                                                    | Go deeper                                                                          |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Quickstart](https://headroom-docs.vercel.app/docs/quickstart)                | [Architecture](https://headroom-docs.vercel.app/docs/architecture)                 |
| [Proxy](https://headroom-docs.vercel.app/docs/proxy)                          | [How compression works](https://headroom-docs.vercel.app/docs/how-compression-works) |
| [MCP tools](https://headroom-docs.vercel.app/docs/mcp)                        | [CCR — reversible compression](https://headroom-docs.vercel.app/docs/ccr)          |
| [Memory](https://headroom-docs.vercel.app/docs/memory)                        | [Cache optimization](https://headroom-docs.vercel.app/docs/cache-optimization)     |
| [Failure learning](https://headroom-docs.vercel.app/docs/failure-learning)    | [Benchmarks](https://headroom-docs.vercel.app/docs/benchmarks)                    |
| [Configuration](https://headroom-docs.vercel.app/docs/configuration)          | [Limitations](https://headroom-docs.vercel.app/docs/limitations)                  |

## Compared to（竞品对比）

Headroom **本地运行**，覆盖**所有**内容类型，兼容各大主流框架，且支持**可逆压缩**。

|                                                                              | Scope                                          | Deploy                             | Local | Reversible |
|------------------------------------------------------------------------------|------------------------------------------------|------------------------------------|:-----:|:----------:|
| **Headroom**                                                                 | All context — tools, RAG, logs, files, history | Proxy · library · middleware · MCP | Yes   | Yes        |
| [RTK](https://github.com/rtk-ai/rtk)                                        | CLI command outputs                            | CLI wrapper                        | Yes   | No         |
| [lean-ctx](https://github.com/yvgude/lean-ctx)                               | CLI commands, MCP tools, editor rules          | CLI wrapper · MCP                  | Yes   | No         |
| [Compresr](https://compresr.ai), [Token Co.](https://thetokencompany.ai)    | Text sent to their API                         | Hosted API call                    | No    | No         |
| OpenAI Compaction                                                            | Conversation history                           | Provider-native                    | No    | No         |

> **致谢。** Headroom 内置了优秀的 [RTK](https://github.com/rtk-ai/rtk) 二进制文件用于 Shell 输出重写——支持 `git show --short`、作用域限定 `ls` 及安装程序摘要。衷心感谢 RTK 团队；他们的工具是我们技术栈中的核心组件，Headroom 会对其下游的所有内容进行压缩。Headroom 也可将 [lean-ctx](https://github.com/yvgude/lean-ctx) 选为 CLI 上下文处理工具；运行 `headroom wrap ...` 前请设置环境变量 `HEADROOM_CONTEXT_TOOL=lean-ctx`。

## Contributing（贡献指南）

```bash
git clone https://github.com/chopratejas/headroom.git && cd headroom
pip install -e ".[dev]" && pytest
```

项目根目录下的 `.devcontainer/` 提供了 DevContainer 配置（默认环境及包含 Qdrant 与 Neo4j 的 `memory-stack`）。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## Community（社区）

- **[Discord](https://discord.gg/yRmaUNpsPJ)** — 提问、反馈与交流实战经验。
- **[Kompress-base on HuggingFace](https://huggingface.co/chopratejas/kompress-base)** ——支撑我们文本压缩的核心模型。

## License（许可证）

Apache 2.0 ——详见 [LICENSE](LICENSE)。
```