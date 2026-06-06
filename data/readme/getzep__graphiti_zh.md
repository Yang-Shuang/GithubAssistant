<p align="center">
  <a href="https://www.getzep.com/">
    <img src="https://github.com/user-attachments/assets/119c5682-9654-4257-8922-56b7cb8ffd73" width="150" alt="Zep Logo">
  </a>
</p>

<h1 align="center">
Graphiti
</h1>
<h2 align="center">为 AI Agent 构建时序上下文图</h2>

<div align="center">

[![Lint](https://github.com/getzep/Graphiti/actions/workflows/lint.yml/badge.svg?style=flat)](https://github.com/getzep/Graphiti/actions/workflows/lint.yml)
[![Unit Tests](https://github.com/getzep/Graphiti/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/getzep/Graphiti/actions/workflows/unit_tests.yml)
[![MyPy Check](https://github.com/getzep/Graphiti/actions/workflows/typecheck.yml/badge.svg)](https://github.com/getzep/Graphiti/actions/workflows/typecheck.yml)

[![GitHub Repo stars](https://img.shields.io/github/stars/getzep/graphiti)](https://github.com/getzep/graphiti/stargazers)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white)](https://discord.com/invite/W8Kw6bsgXQ)
[![arXiv](https://img.shields.io/badge/arXiv-2501.13956-b31b1b.svg?style=flat)](https://arxiv.org/abs/2501.13956)
[![Release](https://img.shields.io/github/v/release/getzep/graphiti?style=flat&label=Release&color=limegreen)](https://github.com/getzep/graphiti/releases)

</div>
<div align="center">

<a href="https://trendshift.io/repositories/12986" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12986" alt="getzep%2Fgraphiti | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

> [!NOTE]
> **我们正在招聘！** 构建能够驱动可靠、个性化、快速生产级 AI Agent 的上下文图。
> 加入我们——我们正招聘工程师和开发者关系（Developer Relations）人员。[查看开放职位](https://www.getzep.com/careers/)。

⭐ *帮助我们触达更多开发者，壮大 Graphiti 社区。给本项目点个 Star！*

&nbsp;

> [!TIP]
> 看看全新的 [Graphiti MCP Server](mcp_server/README.md)！为 Claude、Cursor 及其他 MCP 客户端提供强大的基于上下文图的记忆功能，具备时间感知能力。

Graphiti 是一个用于构建和查询 AI Agent **时序上下文图（Temporal Context Graph）**的框架。与静态知识图谱不同，
Graphiti 的上下文图会追踪事实随时间的变化、保留数据来源的可追溯性（provenance），并支持预设与自学习本体论（ontology）——专为在动态现实数据中运行的 Agent 而设计。

与传统检索增强生成（RAG, Retrieval-Augmented Generation）方法不同，Graphiti 持续将用户交互、
结构化与非结构化的企业数据以及外部信息整合到一个连贯且可查询的图中。该框架支持增量数据更新、高效检索和精确的历史查询，无需重新计算整个图，使其非常适合开发交互式、具备上下文感知能力的 AI 应用。

使用 Graphiti 可以：

- 构建随每次交互而演进的上下文图——追踪当前为真与过去为真的事实。
- 为 Agent 提供丰富、结构化的上下文，而非扁平的文档分块或原始聊天记录。
- 跨时间、语义和关系进行查询，结合混合检索（语义 + 关键词 + 图谱遍历）。

&nbsp;

<p align="center">
    <img src="images/graphiti-graph-intro.gif" alt="Graphiti temporal walkthrough" width="700px">
</p>

&nbsp;

## 什么是上下文图？

一个 **上下文图** 是由实体、关系和事实组成的时序图谱——例如 *"Kendra 喜欢 Adidas 鞋（截至 2026 年 3 月）"*。与传统知识图谱不同，上下文图中的每个事实都有一个有效时间窗口：它何时变为真，以及何时（如果有的话）被取代。实体会随时间演进并更新摘要。所有内容均可追溯至 **事件（Episodes）**——即生成这些数据的原始数据流。

Graphiti 的独特之处在于其能够自主从非结构化与结构化数据中构建上下文图，在保持完整时序历史的同时处理动态变化的关系。

一个上下文图包含：

| Component | What it stores |
|-----------|---------------|
| **Entities**（节点） | 人物、产品、策略、概念等——附带随时间演进的摘要 |
| **Facts / Relationships**（边） | 三元组（Entity → Relationship → Entity），带有有效时间窗口 |
| **Episodes**（溯源） | 原始数据摄入时的状态——即真相流。每个派生事实均可追溯至此 |
| **Custom Types**（本体论） | 通过 Pydantic 模型定义的开发者级实体和边类型 |

## Graphiti 与 Zep

Graphiti 是 [Zep](https://www.getzep.com) AI Agent 上下文基础设施核心的开源时序上下文图引擎。Zep 负责大规模管理上下文图，提供
受控、低延迟的上下文检索与组装服务，适用于生产级 Agent 部署。

借助 Graphiti，我们已证明 Zep 是 [Agent 记忆领域的最新技术](https://blog.getzep.com/state-of-the-art-agent-memory/)。

阅读我们的论文：[Zep：一种面向 Agent 记忆的时序知识图谱架构](https://arxiv.org/abs/2501.13956)。

我们很高兴将 Graphiti 开源，相信其作为上下文图引擎的潜力远不止于记忆应用。

<p align="center">
    <a href="https://arxiv.org/abs/2501.13956"><img src="images/arxiv-screenshot.png" alt="Zep: A Temporal Knowledge Graph Architecture for Agent Memory" width="700px"></a>
</p>

## Zep 与 Graphiti 对比

| Aspect | Zep | Graphiti |
|--------|-----|---------|
| **定位** | AI Agent 托管式上下文图基础设施 | 开源时序上下文图引擎 |
| **上下文图** | 管理海量用户/实体级上下文图，具备治理功能 | 构建和查询单个上下文图 |
| **用户与对话管理** | 内置用户、线程及消息存储 | 需自行实现 |
| **检索与性能** | 预配置的生产就绪型检索，大规模下亚毫秒（sub-200ms）延迟 | 需自定义实现；性能取决于你的部署环境 |
| **开发者工具** | 提供图谱可视化、调试日志、API 日志的仪表盘；Python、TypeScript 和 Go SDK | 需自行构建工具 |
| **企业级功能** | SLA、技术支持、安全保证 | 自托管管理 |
| **部署方式** | 全托管或部署于你的云环境 | 仅支持自建/本地部署 |

### 如何选择

**选择 Zep**：如果你需要一个开箱即用、具备企业级安全保障，且内置安全、性能与技术支持的平台。

**选择 Graphiti**：如果你需要灵活的开源核心组件，并且有能力自行构建和运维周边系统。

## 为什么选择 Graphiti？

传统的 RAG 方法通常依赖批处理和静态数据摘要处理，面对频繁变化的数据时效率低下。Graphiti 通过以下方式解决这些挑战：

- **时序事实管理**：事实具有有效时间窗口。当信息变更时，旧事实会被标记为失效而非直接删除。你可以查询当前为真的内容，或任意历史时刻的状态。
- **事件与溯源（Episodes & Provenance）**：每个实体和关系均可追溯至生成它的原始数据（事件）。提供从派生事实到源数据的完整血缘链路。
- **预设与自学习本体论**：可通过 Pydantic 模型预先定义实体和边类型（预设），或让结构从你的数据中自然浮现（自学习）。从简单开始，随模式出现而演进。
- **增量图构建**：新数据即时集成，无需批处理重新计算。随着事件摄入，图谱实时演进。
- **混合检索**：结合语义向量、关键词（BM25）和图谱遍历技术，实现低延迟、高精确度的查询，不依赖 LLM 摘要生成。
- **可扩展性**：通过并行处理和可插拔图后端高效管理大规模数据集，适用于企业级工作负载。

<p align="center">
    <img src="/images/graphiti-intro-slides-stock-2.gif" alt="Graphiti structured + unstructured demo" width="700px">
</p>

## Graphiti 与 GraphRAG 对比

| Aspect | GraphRAG | Graphiti |
|--------|----------|---------|
| **主要用途** | 静态文档摘要生成 | Agent 的动态演进上下文管理 |
| **数据处理方式** | 面向批处理 | 持续增量更新 |
| **知识结构** | 实体聚类与社区摘要 | 时序上下文图——含有效时间窗口的实体、事实、事件及社区 |
| **检索方法** | 顺序式 LLM 摘要生成 | 混合语义、关键词与基于图谱的搜索 |
| **适应性** | 低 | 高 |
| **时序处理** | 基础的时间戳追踪 | 显式的双时间轴（bi-temporal）追踪，自动失效事实 |
| **矛盾处理** | LLM 驱动的摘要判断 | 自动标记事实失效，同时保留完整时序历史 |
| **查询延迟** | 数秒至数十秒 | 通常低于 1 秒 |
| **自定义实体类型** | 不支持 | 支持，可通过 Pydantic 模型定制 |
| **可扩展性** | 中等 | 高，针对大规模数据集优化 |

Graphiti 专为应对动态且频繁更新的数据集挑战而设计，特别适合需要实时交互和精确历史查询的应用场景。

## 安装要求：

- Python 3.10 或更高版本
- Neo4j 5.26 / FalkorDB 1.1.2 / Kuzu 0.11.2 / Amazon Neptune Database Cluster 或 Neptune Analytics Graph + Amazon OpenSearch Serverless 集合（用作全文检索后端）
- OpenAI API Key（Graphiti 默认使用 OpenAI 进行 LLM 推理与嵌入向量生成）

> [!IMPORTANT]
> Graphiti 在配合支持结构化输出（Structured Output）的 LLM 服务时效果最佳（如 OpenAI 和 Gemini）。
> 使用其他服务可能导致输出模式错误及数据摄入失败。在使用较小模型时此问题尤为突出。

可选：

- Google Gemini、Anthropic 或 Groq API Key（用于替代 LLM 提供商）

> [!TIP]
> 安装 Neo4j 最简单的方式是通过 [Neo4j Desktop](https://neo4j.com/download/)。它提供用户友好的界面来管理 Neo4j 实例和数据库。
> 或者，你可以通过 Docker 在本地部署 FalkorDB 并立即开始快速入门示例：
> ```bash
> docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
> ```

```bash
pip install graphiti-core
```

or

```bash
uv add graphiti-core
```

### Installing with FalkorDB Support

如果你计划将 FalkorDB 用作图数据库后端，请安装包含 FalkorDB 扩展的版本：

```bash
pip install graphiti-core[falkordb]

# or with uv
uv add graphiti-core[falkordb]
```

### Installing with Kuzu Support

如果你计划将 Kuzu 用作图数据库后端，请安装包含 Kuzu 扩展的版本：

```bash
pip install graphiti-core[kuzu]

# or with uv
uv add graphiti-core[kuzu]
```

### Installing with Amazon Neptune Support

如果你计划将 Amazon Neptune 用作图数据库后端，请安装包含 Amazon Neptune 扩展的版本：

```bash
pip install graphiti-core[neptune]

# or with uv
uv add graphiti-core[neptune]
```

### You can also install optional LLM providers as extras:

你也可以将可选的 LLM 提供商作为额外依赖安装：

```bash
# Install with Anthropic support
pip install graphiti-core[anthropic]

# Install with Groq support
pip install graphiti-core[groq]

# Install with Google Gemini support
pip install graphiti-core[google-genai]

# Install with multiple providers
pip install graphiti-core[anthropic,groq,google-genai]

# Install with FalkorDB and LLM providers
pip install graphiti-core[falkordb,anthropic,google-genai]

# Install with Amazon Neptune
pip install graphiti-core[neptune]
```

## 默认低并发；LLM 提供商 429 限流错误

Graphiti 的数据摄入管道（ingestion pipelines）设计用于高并发场景。默认情况下，并发数设置较低以避免触发 LLM
提供商的 429 Rate Limit Errors（速率限制错误）。如果你发现 Graphiti 运行较慢，请按照下文描述提高并发配置。

并发量由 `SEMAPHORE_LIMIT` 环境变量控制。默认情况下，`SEMAPHORE_LIMIT` 设置为 `10`
个并发操作，以帮助防止来自 LLM 提供商的 `429` 限流错误。如果你遇到此类错误，请尝试降低此值。

如果你的 LLM 提供商允许更高的吞吐量，你可以增加 `SEMAPHORE_LIMIT` 以提升事件摄入性能。

## Quick Start

> [!IMPORTANT]
> Graphiti 默认使用 OpenAI 进行 LLM 推理与嵌入向量生成。请确保你的环境变量中已设置 `OPENAI_API_KEY`。
> 我们也支持 Anthropic 和 Groq 的 LLM 推理。其他 LLM 提供商可通过兼容 OpenAI API 的方式接入。

完整可运行的示例请参阅 examples 目录中的 [快速入门示例](examples/quickstart/README.md)。该示例演示了：

1. 连接 Neo4j、Amazon Neptune、FalkorDB 或 Kuzu 数据库
2. 初始化 Graphiti 索引与约束条件
3. 向图中添加事件（包括文本和结构化 JSON）
4. 使用混合搜索查询关系（边）
5. 基于图距离对搜索结果进行重排序
6. 使用预定义搜索配方查询节点

该示例配有完整文档，清晰解释了各项功能，并包含详细的 README 以提供设置说明和后续步骤。

### Running with Docker Compose

你可以通过 Docker Compose 快速启动所需服务：

- **Neo4j Docker：**

  ```bash
  docker compose up
  ```

  This will start the Neo4j Docker service and related components.

- **FalkorDB Docker：**

  ```bash
  docker compose --profile falkordb up
  ```

  This will start the FalkorDB Docker service and related components.

## MCP Server

`mcp_server` 目录包含 Graphiti 的模型上下文协议（MCP）服务器实现。该服务器允许 AI 助手通过 MCP 协议与 Graphiti 的上下文图功能进行交互。

MCP 服务器的主要特性包括：

- 事件管理（添加、检索、删除）
- 实体管理与关系处理
- 语义与混合搜索能力
- 用于组织相关数据的群组管理
- 图谱维护操作

该 MCP 服务器可配合 Neo4j 通过 Docker 部署，便于将 Graphiti 集成到你的 AI 助手工作流中。

详细设置说明和使用示例请参阅 [MCP server README](mcp_server/README.md)。

## REST Service

`server` 目录包含用于与 Graphiti API 交互的 API 服务，基于 FastAPI 构建。

更多信息请参阅 [server README](server/README.md)。

## Optional Environment Variables

除了 Neo4j 和 OpenAI 兼容的凭据外，Graphiti 还提供了一些可选的环境变量。
如果你使用我们支持的模型（如 Anthropic 或 Voyage），必须设置相应必要的环境变量。

### Database Configuration

数据库名称直接在驱动构造函数中配置：

- **Neo4j**：数据库名默认为 `neo4j`（在 Neo4jDriver 中硬编码）
- **FalkorDB**：数据库名默认为 `default_db`（在 FalkorDriver 中硬编码）

自 v0.17.0 起，如需自定义数据库配置，可实例化一个数据库驱动并通过 `graph_driver` 参数传递给 Graphiti 构造函数。

#### Neo4j with Custom Database Name

```python
from graphiti_core import Graphiti
from graphiti_core.driver.neo4j_driver import Neo4jDriver

# Create a Neo4j driver with custom database name
driver = Neo4jDriver(
    uri="bolt://localhost:7687",
    user="neo4j",
    password="password",
    database="my_custom_database"  # Custom database name
)

# Pass the driver to Graphiti
graphiti = Graphiti(graph_driver=driver)
```

#### FalkorDB with Custom Database Name

```python
from graphiti_core import Graphiti
from graphiti_core.driver.falkordb_driver import FalkorDriver

# Create a FalkorDB driver with custom database name
driver = FalkorDriver(
    host="localhost",
    port=6379,
    username="falkor_user",  # Optional
    password="falkor_password",  # Optional
    database="my_custom_graph"  # Custom database name
)

# Pass the driver to Graphiti
graphiti = Graphiti(graph_driver=driver)
```

#### Kuzu

```python
from graphiti_core import Graphiti
from graphiti_core.driver.kuzu_driver import KuzuDriver

# Create a Kuzu driver
driver = KuzuDriver(db="/tmp/graphiti.kuzu")

# Pass the driver to Graphiti
graphiti = Graphiti(graph_driver=driver)
```

#### Amazon Neptune

```python
from graphiti_core import Graphiti
from graphiti_core.driver.neptune_driver import NeptuneDriver

# Create a Neptune driver
driver = NeptuneDriver(
    host='<NEPTUNE_ENDPOINT>',
    aoss_host='<AMAZON_OPENSEARCH_SERVERLESS_HOST>',
    port=8182,      # Optional, defaults to 8182
    aoss_port=443,  # Optional, defaults to 443
)

# Pass the driver to Graphiti
graphiti = Graphiti(graph_driver=driver)
```

Contributing a new graph backend? See [Adding a graph driver](CONTRIBUTING.md#adding-a-graph-driver).

## Using Graphiti with Azure OpenAI

Graphiti 支持通过 Azure 的 OpenAI v1 API 兼容层，使用 Azure OpenAI 进行 LLM 推理和嵌入向量生成。

### Quick Start

```python
from openai import AsyncOpenAI
from graphiti_core import Graphiti
from graphiti_core.llm_client.azure_openai_client import AzureOpenAILLMClient
from graphiti_core.llm_client.config import LLMConfig
from graphiti_core.embedder.azure_openai import AzureOpenAIEmbedderClient

# Initialize Azure OpenAI client using the standard OpenAI client
# with Azure's v1 API endpoint
azure_client = AsyncOpenAI(
    base_url="https://your-resource-name.openai.azure.com/openai/v1/",
    api_key="your-api-key",
)

# Create LLM and Embedder clients
llm_client = AzureOpenAILLMClient(
    azure_client=azure_client,
    config=LLMConfig(model="gpt-5-mini", small_model="gpt-5-mini")  # Your Azure deployment name
)
embedder_client = AzureOpenAIEmbedderClient(
    azure_client=azure_client,
    model="text-embedding-3-small"  # Your Azure embedding deployment name
)

# Initialize Graphiti with Azure OpenAI clients
graphiti = Graphiti(
    "bolt://localhost:7687",
    "neo4j",
    "password",
    llm_client=llm_client,
    embedder=embedder_client,
)

# Now you can use Graphiti with Azure OpenAI
```

**Key Points：**

- 使用标准 `AsyncOpenAI` 客户端配合 Azure 的 v1 API 端点格式：
  `https://your-resource-name.openai.azure.com/openai/v1/`
- 部署名称（例如 `gpt-5-mini`、`text-embedding-3-small`）应与你的 Azure OpenAI 实际部署名称保持一致
- 完整可运行示例请参阅 `examples/azure-openai/`

请确保将占位符值替换为你实际的 Azure OpenAI 凭据和部署名称。

## Using Graphiti with Google Gemini

Graphiti 支持使用 Google 的 Gemini 模型进行 LLM 推理、嵌入向量生成以及交叉编码/重排序。要使用 Gemini，
你需要配置 LLM 客户端、嵌入器及交叉编码器，并传入你的 Google API Key。

安装 Graphiti：

```bash
uv add "graphiti-core[google-genai]"

# or

pip install "graphiti-core[google-genai]"
```

```python
from graphiti_core import Graphiti
from graphiti_core.llm_client.gemini_client import GeminiClient, LLMConfig
from graphiti_core.embedder.gemini import GeminiEmbedder, GeminiEmbedderConfig
from graphiti_core.cross_encoder.gemini_reranker_client import GeminiRerankerClient

# Google API key configuration
api_key = "<your-google-api-key>"

# Initialize Graphiti with Gemini clients
graphiti = Graphiti(
    "bolt://localhost:7687",
    "neo4j",
    "password",
    llm_client=GeminiClient(
        config=LLMConfig(
            api_key=api_key,
            model="gemini-2.0-flash"
        )
    ),
    embedder=GeminiEmbedder(
        config=GeminiEmbedderConfig(
            api_key=api_key,
            embedding_model="embedding-001"
        )
    ),
    cross_encoder=GeminiRerankerClient(
        config=LLMConfig(
            api_key=api_key,
            model="gemini-2.5-flash-lite"
        )
    )
)

# Now you can use Graphiti with Google Gemini for all components
```

Gemini 重排序器默认使用 `gemini-2.5-flash-lite` 模型，该模型针对成本效益和低延迟分类任务进行了优化。它采用与 OpenAI 重排序器相同的布尔分类方法，利用 Gemini 的对数概率（log probabilities）功能对段落相关性进行排名。

## Using Graphiti with Ollama (Local LLM)

Graphiti 支持通过 Ollama 的 OpenAI 兼容 API 运行本地 LLM 和嵌入模型。这非常适合注重隐私的应用场景，或希望避免 API 费用的情况。

**注意：** 对于 Ollama 及其他兼容 OpenAI API 的提供商（如 LM Studio），请使用 `OpenAIGenericClient`（而非 `OpenAIClient`）。`OpenAIGenericClient` 针对本地模型进行了优化，默认最大 token 限制更高（16K vs 8K）并完整支持结构化输出。

安装模型：

```bash
ollama pull deepseek-r1:7b # LLM
ollama pull nomic-embed-text # embeddings
```

```python
from graphiti_core import Graphiti
from graphiti_core.llm_client.config import LLMConfig
from graphiti_core.llm_client.openai_generic_client import OpenAIGenericClient
from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig
from graphiti_core.cross_encoder.openai_reranker_client import OpenAIRerankerClient

# Configure Ollama LLM client
llm_config = LLMConfig(
    api_key="ollama",  # Ollama doesn't require a real API key, but some placeholder is needed
    model="deepseek-r1:7b",
    small_model="deepseek-r1:7b",
    base_url="http://localhost:11434/v1",  # Ollama's OpenAI-compatible endpoint
)

llm_client = OpenAIGenericClient(config=llm_config)

# Initialize Graphiti with Ollama clients
graphiti = Graphiti(
    "bolt://localhost:7687",
    "neo4j",
    "password",
    llm_client=llm_client,
    embedder=OpenAIEmbedder(
        config=OpenAIEmbedderConfig(
            api_key="ollama",  # Placeholder API key
            embedding_model="nomic-embed-text",
            embedding_dim=768,
            base_url="http://localhost:11434/v1",
        )
    ),
    cross_encoder=OpenAIRerankerClient(client=llm_client, config=llm_config),
)

# Now you can use Graphiti with local Ollama models
```

请确保已运行 `ollama serve` 并已拉取你打算使用的模型。

## Documentation

- [指南与 API 文档](https://help.getzep.com/graphiti)。
- [快速入门](https://help.getzep.com/graphiti/graphiti/quick-start)
- [使用 LangChain 的 LangGraph 和 Graphiti 构建 Agent](https://help.getzep.com/graphiti/integrations/lang-graph-agent)

## Telemetry

Graphiti 会收集匿名使用统计数据，以帮助我们了解框架的使用情况并为所有人进行改进。我们坚信透明度至关重要，以下是我们收集的具体内容及原因。

### What We Collect

当你初始化 Graphiti 实例时，我们会收集：

- **Anonymous identifier**：本地存储在 `~/.cache/graphiti/telemetry_anon_id` 中的随机生成 UUID
- **System information**：操作系统、Python 版本和系统架构
- **Graphiti version**：你使用的版本号
- **Configuration choices**：
  - LLM provider type（OpenAI, Azure, Anthropic 等）
  - Database backend（Neo4j, FalkorDB, Kuzu, Amazon Neptune Database 或 Neptune Analytics）
  - Embedder provider（OpenAI, Azure, Voyage 等）

### What We Don't Collect

我们致力于保护你的隐私。我们 **绝不会** 收集：

- Personal information or identifiers
- API keys or credentials
- Your actual data, queries, or graph content
- IP addresses or hostnames
- File paths or system-specific information
- Any content from your episodes, nodes, or edges

### Why We Collect This Data

这些信息帮助我们：

- Understand which configurations are most popular to prioritize support and testing
- Identify which LLM and database providers to focus development efforts on
- Track adoption patterns to guide our roadmap
- Ensure compatibility across different Python versions and operating systems

通过分享这些匿名信息，你可以帮助社区中的每个人更好地使用 Graphiti。

### View the Telemetry Code

遥测代码 [可在以下位置查看](graphiti_core/telemetry/telemetry.py)。

### How to Disable Telemetry

遥测功能为 **默认开启（opt-out）**，可随时禁用。要禁用遥测收集：

**Option 1: Environment Variable**

```bash
export GRAPHITI_TELEMETRY_ENABLED=false
```

**Option 2: Set in your shell profile**

```bash
# For bash users (~/.bashrc or ~/.bash_profile)
echo 'export GRAPHITI_TELEMETRY_ENABLED=false' >> ~/.bashrc

# For zsh users (~/.zshrc)
echo 'export GRAPHITI_TELEMETRY_ENABLED=false' >> ~/.zshrc
```

**Option 3: Set for a specific Python session**

```python
import os

os.environ['GRAPHITI_TELEMETRY_ENABLED'] = 'false'

# Then initialize Graphiti as usual
from graphiti_core import Graphiti

graphiti = Graphiti(...)
```

Telemetry is automatically disabled during test runs (when `pytest` is detected).

### Technical Details

- Telemetry uses PostHog for anonymous analytics collection
- All telemetry operations are designed to fail silently - they will never interrupt your application or affect Graphiti
  functionality
- The anonymous ID is stored locally and is not tied to any personal information

## Contributing

我们鼓励并感谢任何形式的贡献，无论是代码、文档、处理 GitHub Issue，还是在 Graphiti Discord 频道回答问题。有关代码贡献的详细规范，请参阅 [CONTRIBUTING](CONTRIBUTING.md)。

## Support

加入 [Zep Discord 服务器](https://discord.com/invite/W8Kw6bsgXQ) 并前往 **#Graphiti** 频道！