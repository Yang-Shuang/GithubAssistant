<div align="center">

<img src="assets/mempalace_logo.png" alt="MemPalace" width="240">

# MemPalace

本地优先的 AI 记忆库。逐字存储，可插拔后端，在 LongMemEval 上原始检索率（R@5）达 96.6% —— 零 API 调用。

[![][version-shield]][release-link]
[![][python-shield]][python-link]
[![][license-shield]][license-link]
[![][discord-shield]][discord-link]

</div>

> [!CAUTION]
> **谨防仿冒网站。** MemPalace 没有其他官方网站。唯一的官方来源是此 **[GitHub 仓库](https://github.com/MemPalace/mempalace)**、**[PyPI 软件包](https://pypi.org/project/mempalace/)**，以及 **[mempalaceofficial.com](https://mempalaceofficial.com)** 上的文档。任何其他域名（包括 `.tech`、`.net` 或其他 `.com` 变体）均为仿冒站点，可能会传播恶意软件。详情与时间线：[docs/HISTORY.md](docs/HISTORY.md)。

> [!IMPORTANT]
> **若未配置自动保存钩子（auto-save hooks），Claude Code 会话将在 30 天后过期。** [阅读详情 →](https://github.com/MemPalace/mempalace/discussions/1388)
>
> 需要最短的恢复/设置路径？请使用 [Claude Code 保留设置检查清单](https://mempalaceofficial.com/guide/claude-code-retention.html)。

---

## What it is

MemPalace 将你的对话历史以逐字文本形式存储，并通过语义搜索进行检索。它不会进行摘要、提取或改写。索引是结构化的——人物和项目成为 *翼（wings）*，主题成为 *房间（rooms）*，原始内容存放在 *抽屉（drawers）* 中——因此搜索可以限定范围，而不是在扁平语料库中进行。

检索层是可插拔的。当前默认后端为 ChromaDB；接口定义在 [`mempalace/backends/base.py`](mempalace/backends/base.py) 中，你可以直接替换其他后端而无需修改系统其余部分。

除非你主动选择开启，否则没有任何数据会离开你的本地机器。

架构、概念与数据采集流程：
[mempalaceofficial.com/concepts/the-palace](https://mempalaceofficial.com/concepts/the-palace.html)。

---

## Install

MemPalace 提供 CLI，因此建议在隔离环境中安装，以避免在 Debian/Ubuntu/Homebrew Python 上出现 PEP 668 错误，并防止 mempalace 的依赖项（chromadb、numpy、grpcio 等）与全局 site-packages 中的其他包发生冲突。

我们推荐使用 [`uv`](https://docs.astral.sh/uv/) —— `uv tool install` 会将 `mempalace` CLI 安装到隔离环境中，并添加到你的 PATH：

```bash
uv tool install mempalace
mempalace init ~/projects/myapp
```

[`pipx`](https://pipx.pypa.io/) 操作方式相同，如果你偏好使用它：`pipx install mempalace`。

仅在你明确需要虚拟环境中可调用 `import mempalace` 时，才建议在已激活的 virtualenv 内使用原生 `pip`：

```bash
python -m venv .venv && source .venv/bin/activate
pip install mempalace
```

## Quickstart

```bash
# Mine content into the palace
mempalace mine ~/projects/myapp                    # project files
mempalace mine ~/.claude/projects/ --mode convos   # Claude Code sessions (scope with --wing per project)

# Search
mempalace search "why did we switch to GraphQL"

# Load context for a new session
mempalace wake-up
```

关于 Claude Code、Gemini CLI、MCP 兼容工具及本地模型的配置，请参阅 [mempalaceofficial.com/guide/getting-started](https://mempalaceofficial.com/guide/getting-started.html)。

---

## Benchmarks

以下所有数据均可通过本仓库中的命令复现（详见 `benchmarks/BENCHMARKS.md`）。完整的逐题结果文件已提交至 `benchmarks/results_*`。

**LongMemEval — 检索召回率（R@5，500 道题目）：**

| Mode | R@5 | LLM required |
|---|---|---|
| Raw (semantic search, no heuristics, no LLM) | **96.6%** | None |
| Hybrid v4, held-out 450q (tuned on 50 dev, not seen during training) | **98.4%** | None |
| Hybrid v4 + LLM rerank (full 500) | ≥99% | Any capable model |

原始 96.6% 的指标无需任何 API Key、云服务或 LLM。混合检索管线增加了关键词加权、时间邻近度加权及偏好模式提取；预留测试集得出的 98.4% 是更客观的可泛化指标。

重排序管线使用 LLM 阅读器，从检索出的前 20 个候选会话中挑选最佳结果。它兼容任意具备基本能力的模型——我们已通过 Ollama Cloud 使用 Claude Haiku、Claude Sonnet 和 minimax-m2.7 复现了该结果（无需依赖 Anthropic）。原始检索与重排序之间的性能差距与具体模型无关；我们未将“100%”作为核心指标，因为最后的 0.6% 是通过人工检查特定错误答案得出的，`benchmarks/BENCHMARKS.md` 已将其标记为应试优化。

**其他基准测试（完整结果见 [`benchmarks/BENCHMARKS.md`](benchmarks/BENCHMARKS.md)）：**

| Benchmark | Metric | Score | Notes |
|---|---|---|---|
| LoCoMo (session, top-10, no rerank) | R@10 | 60.3% | 1,986 questions |
| LoCoMo (hybrid v5, top-10, no rerank) | R@10 | 88.9% | Same set |
| ConvoMem (all categories, 250 items) | Avg recall | 92.9% | 50 per category |
| MemBench (ACL 2025, 8,500 items) | R@5 | 80.3% | All categories |

我们刻意未提供与 Mem0、Mastra、Hindsight、Supermemory 或 Zep 的横向对比。这些项目在不同数据划分上使用了不同的评估指标，将检索召回率与端到端问答准确率直接并列并不公平。请参阅各项目官方研究页面获取其公布的数据。

**复现所有结果：**

```bash
git clone https://github.com/MemPalace/mempalace.git
cd mempalace
uv sync --extra dev   # or: pip install -e ".[dev]"
# see benchmarks/README.md for dataset download commands
uv run python benchmarks/longmemeval_bench.py /path/to/longmemeval_s_cleaned.json
```

---

## Knowledge graph

MemPalace 内置了基于本地 SQLite 的时序实体关系图，支持有效期窗口管理——包括添加、查询、失效及时间线功能。使用指南与工具参考：
[mempalaceofficial.com/concepts/knowledge-graph](https://mempalaceofficial.com/concepts/knowledge-graph.html)。

## MCP server

提供 29 个 MCP 工具，涵盖宫殿读写、知识图谱操作、跨翼导航、抽屉管理及 Agent 日记功能。安装指南与完整工具列表：
[mempalaceofficial.com/reference/mcp-tools](https://mempalaceofficial.com/reference/mcp-tools.html)。

## Agents

每位专业 Agent 在宫殿中均拥有独立的“翼”和专属日记。运行时可通过 `mempalace_list_agents` 动态发现——不会增加系统提示词（system prompt）的冗余：
[mempalaceofficial.com/concepts/agents](https://mempalaceofficial.com/concepts/agents.html)。

## Auto-save hooks

提供两个 Claude Code 钩子，分别用于定期保存及上下文压缩前保存：
[mempalaceofficial.com/guide/hooks](https://mempalaceofficial.com/guide/hooks.html)。

若时间紧迫，建议优先参考 [Claude Code 保留设置检查清单](https://mempalaceofficial.com/guide/claude-code-retention.html)：配置钩子、备份现有的 JSONL 转录文件，并使用 `mempalace mine ~/.claude/projects/ --mode convos` 进行数据回填。

若需在钩子生成的文件级分块基础上实现逐条消息的检索，请定期运行 `mempalace sweep <transcript-dir>`——该命令会为每条用户/助手消息存储一个独立的逐字抽屉，支持幂等操作与断点续传（resume-safe）。

---

## Requirements

- Python 3.9+
- A vector-store backend (ChromaDB by default)
- ~300 MB disk for the embedding model. Onboarding (`python -m mempalace.onboarding`) offers `embeddinggemma-300m` (multilingual, 100+ languages, recommended) or `all-MiniLM-L6-v2` (English-only, ~30 MB). See the docstring at [`mempalace/embedding.py`](mempalace/embedding.py) for details and migration notes.

No API key is required for the core benchmark path.

## Docs

- Getting started → [mempalaceofficial.com/guide/getting-started](https://mempalaceofficial.com/guide/getting-started.html)
- CLI reference → [mempalaceofficial.com/reference/cli](https://mempalaceofficial.com/reference/cli.html)
- Python API → [mempalaceofficial.com/reference/python-api](https://mempalaceofficial.com/reference/python-api.html)
- Full benchmark methodology → [benchmarks/BENCHMARKS.md](benchmarks/BENCHMARKS.md)
- Release notes → [CHANGELOG.md](CHANGELOG.md)
- Corrections and public notices → [docs/HISTORY.md](docs/HISTORY.md)

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).

<!-- Link Definitions -->
[version-shield]: https://img.shields.io/badge/version-3.3.6-4dc9f6?style=flat-square&labelColor=0a0e14
[release-link]: https://github.com/MemPalace/mempalace/releases
[python-shield]: https://img.shields.io/badge/python-3.9+-7dd8f8?style=flat-square&labelColor=0a0e14&logo=python&logoColor=7dd8f8
[python-link]: https://www.python.org/
[license-shield]: https://img.shields.io/badge/license-MIT-b0e8ff?style=flat-square&labelColor=0a0e14
[license-link]: https://github.com/MemPalace/mempalace/blob/main/LICENSE
[discord-shield]: https://img.shields.io/badge/discord-join-5865F2?style=flat-square&labelColor=0a0e14&logo=discord&logoColor=5865F2
[discord-link]: https://discord.com/invite/ycTQQCu6kn