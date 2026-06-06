# 🗂️ LlamaIndex 🦙

[![PyPI - Downloads](https://img.shields.io/pypi/dm/llama-index)](https://pypi.org/project/llama-index/)
[![Build](https://github.com/run-llama/llama_index/actions/workflows/build_package.yml/badge.svg)](https://github.com/run-llama/llama_index/actions/workflows/build_package.yml)
[![GitHub contributors](https://img.shields.io/github/contributors/jerryjliu/llama_index)](https://github.com/jerryjliu/llama_index/graphs/contributors)
[![Discord](https://img.shields.io/discord/1059199217496772688)](https://discord.gg/dGcwcsnxhU)
[![Twitter](https://img.shields.io/twitter/follow/llama_index)](https://x.com/llama_index)
[![Reddit](https://img.shields.io/reddit/subreddit-subscribers/LlamaIndex?style=plastic&logo=reddit&label=r%2FLlamaIndex&labelColor=white)](https://www.reddit.com/r/LlamaIndex/)
[![Ask AI](https://img.shields.io/badge/Phorm-Ask_AI-%23F2777A.svg?&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNSIgaGVpZ2h0PSI0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxwYXRoIGQ9Ik00LjQzIDEuODgyYTEuNDQgMS40NCAwIDAgMS0uMDk4LjQyNmMtLjA1LjEyMy0uMTE1LjIzLS4xOTIuMzIyLS4wNzUuMDktLjE2LjE2NS0uMjU1LjIyNmExLjM1MyAxLjM1MyAwIDAgMS0uNTk1LjIxMmMtLjA5OS4wMTItLjE5Mi4wMTQtLjI3OS4wMDZsLTEuNTkzLS4xNHYtLjQwNmgxLjY1OGMuMDkuMDAxLjE3LS4xNjkuMjQ2LS4xOTFhLjYwMy42MDMgMCAwIDAgLjItLjEwNi41MjkuNTI5IDAgMCAwIC4xMzgtLjE3LjY1NC42NTQgMCAwIDAgLjA2NS0uMjRsLjAyOC0uMzJhLjkzLjkzIDAgMCAwLS4wMzYtLjI0OS41NjcuNTY3IDAgMCAwLS4xMDMtLjIuNTAyLjUwMiAwIDAgMC0uMTY4LS4xMzguNjA4LjYwOCAwIDAgMC0uMjQtLjA2N0wyLjQzNy43MjkgMS42MjUuNjcxYS4zMjIuMzIyIDAgMCAwLS4yMzIuMDU4LjM3NS4zNzUgMCAwIDAtLjExNi4yMzJsLS4xMTYgMS40NS0uMDU4LjY5Ny0uMDU4Ljc1NEwuNzA1IDRsLS4zNTctLjA3OUwuNjAyLjkwNkMuNjE3LjcyNi42NjMuNTc0LjczOS40NTRhLjk1OC45NTggMCAwIDEgLjI3NC0uMjg1Ljk3MS45NzEgMCAwIDEgLjMzNy0uMTRjLjExOS0uMDI2LjIyNy0uMDM0LjMyNS0uMDI2TDMuMjMyLjE2Yy4xNTkuMDE0LjMzNi4wMy40NTkuMDgyYTEuMTczIDEuMTczIDAgMCAxIC41NDUuNDQ3Yy4wNi4wOTQuMTA5LjE5Mi4xNDQuMjkzYTEuMzkyIDEuMzkyIDAgMCAxIC4wNzguNThsLS4wMjkuMzJaIiBmaWxsPSIjRjI3NzdBIi8+CiAgPHBhdGggZD0iTTQuMDgyIDIuMDA3YTEuNDU1IDEuNDU1IDAgMCAxLS4wOTguNDI3Yy0uMDUuMTI0LS4xMTQuMjMyLS4xOTIuMzI0YTEuMTMgMS4xMyAwIDAgMS0uMjU0LjIyNyAxLjM1MyAxLjM1MyAwIDAgMS0uNTk1LjIxNGMtLjEuMDEyLS4xOTMuMDE0LS4yOC4wMDZsLTEuNTYtLjEwOC4wMzQtLjQwNi4wMy0uMzQ4IDEuNTU5LjE1NGMuMDkgMCAuMTczLS4wMS4yNDgtLjAzM2EuNjAzLjYwMyAwIDAgMCAuMi0uMTA2LjUzMi41MzIgMCAwIDAgLjEzOS0uMTcyLjY2LjY2IDAgMCAwIC4wNjQtLjI0MWwuMDI5LS4zMjFhLjk0Ljk0IDAgMCAwLS4wMzYtLjI1LjU3LjU3IDAgMCAwLS4xMDMtLjIwMi41MDIuNTAyIDAgMCAwLS4xNjgtLjEzOC42MDUuNjA1IDAgMCAwLS4yNC0uMDY3TDEuMjczLjgyN2MtLjA5NC0uMDA4LS4xNjguMDEtLjIyMS4wNTUtLjA1My4wNDUtLjA4NC4xMTQtLjA5Mi4yMDZMLjcwNSA0IDAgMy45MzhsLjI1NS0yLjkxMUExLjAxIDEuMDEgMCAwIDEgLjM5My41NzIuOTYyLjk2MiAwIDAgMSAuNjY2LjI4NmEuOTcuOTcgMCAwIDEgLjMzOC0uMTRDMS4xMjIuMTIgMS4yMy4xMSAxLjMyOC4xMTlsMS41OTMuMTRjLjE2LjAxNC4zLjA0Ny40MjMuMWExLjE3IDEuMTcgMCAwIDEgLjU0NS40NDhjLjA2MS4wOTUuMTA5LjE5My4xNDQuMjk1YTEuNDA2IDEuNDA2IDAgMCAxIC4wNzcuNTgzbC0uMDI4LjMyMloiIGZpbGw9IndoaXRlIi8+CiAgPHBhdGggZD0iTTQuMDgyIDIuMDA3YTEuNDU1IDEuNDU1IDAgMCAxLS4wOTguNDI3Yy0uMDUuMTI0LS4xMTQuMjMyLS4xOTIuMzI0YTEuMTMgMS4xMyAwIDAgMS0uMjU0LjIyNyAxLjM1MyAxLjM1MyAwIDAgMS0uNTk1LjIxNGMtLjEuMDEyLS4xOTMuMDE0LS4yOC4wMDZsLTEuNTYtLjEwOC4wMzQtLjQwNi4wMy0uMzQ4IDEuNTU5LjE1NGMuMDkgMCAuMTczLS4wMS4yNDgtLjAzM2EuNjAzLjYwMyAwIDAgMCAuMi0uMTA2LjUzMi41MzIgMCAwIDAgLjEzOS0uMTcyLjY2LjY2IDAgMCAwIC4wNjQtLjI0MWwuMDI5LS4zMjFhLjk0Ljk0IDAgMCAwLS4wMzYtLjI1LjU3LjU3IDAgMCAwLS4xMDMtLjIwMi41MDIuNTAyIDAgMCAwLS4xNjgtLjEzOC42MDUuNjA1IDAgMCAwLS4yNC0uMDY3TDEuMjczLjgyN2MtLjA5NC0uMDA4LS4xNjguMDEtLjIyMS4wNTUtLjA1My4wNDUtLjA4NC4xMTQtLjA5Mi4yMDZMLjcwNSA0IDAgMy45MzhsLjI1NS0yLjkxMUExLjAxIDEuMDEgMCAwIDEgLjM5My41NzIuOTYyLjk2MiAwIDAgMSAuNjY2LjI4NmEuOTcuOTcgMCAwIDEgLjMzOC0uMTRDMS4xMjIuMTIgMS4yMy4xMSAxLjMyOC4xMTlsMS41OTMuMTRjLjE2LjAxNC4zLjA0Ny40MjMuMWExLjE3IDEuMTcgMCAwIDEgLjU0NS40NDhjLjA2MS4wOTUuMTA5LjE5My4xNDQuMjk1YTEuNDA2IDEuNDA2IDAgMCAxIC4wNzcuNTgzbC0uMDI4LjMyMloiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=)](https://www.phorm.ai/query?projectId=c5863b56-6703-4a5d-87b6-7e6031bf16b6)

LlamaIndex OSS（由 [LlamaIndex](https://llamaindex.ai?utm_medium=li_github&utm_source=github&utm_campaign=2026--) 提供）是一个用于构建智能体应用（Agentic Applications）的开源框架。**[Parse](https://cloud.llamaindex.ai?utm_medium=li_github&utm_source=github&utm_campaign=2026--)** 是我们面向企业的 OCR、解析、提取、索引等功能的平台。你可以将此框架与 LlamaParse 配合使用，也可以单独运行它；注册及产品链接请参见下方的 [LlamaParse](#llamacloud-document-agent-platform)。

> ### 📚 **文档：**
>
> - [LlamaParse](https://developers.llamaindex.ai/python/cloud/llamaparse/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)
> - [LlamaIndex OSS](https://developers.llamaindex.ai/python/framework/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)
> - [LlamaAgents](https://developers.llamaindex.ai/python/llamaagents/overview/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)

使用 LlamaIndex 进行开发通常涉及核心库（LlamaIndex Core）以及你选择的一组集成（或插件）。在 Python 中开始使用 LlamaIndex 有两种方式：

1. **入门版**：[`llama-index`](https://pypi.org/project/llama-index/)。一个包含 LlamaIndex 核心库及精选集成的基础 Python 包。

2. **自定义版**：[`llama-index-core`](https://pypi.org/project/llama-index-core/)。安装 LlamaIndex 核心库，并根据你的应用需求在 [LlamaHub](https://llamahub.ai/)
   上添加所需的集成包。目前有超过 300 个与核心无缝协作的集成包，让你能够使用偏好的大语言模型（LLM）、嵌入模型和向量存储提供商进行开发。

LlamaIndex 的 Python 库采用命名空间设计：导入语句中包含 `core` 表示使用的是核心包；而不包含 `core` 的语句则表示使用的是集成包。

```python
# typical pattern
from llama_index.core.xxx import ClassABC  # core submodule xxx
from llama_index.xxx.yyy import (
    SubclassABC,
)  # integration yyy for submodule xxx

# concrete example
from llama_index.core.llms import LLM
from llama_index.llms.openai import OpenAI
```

### LlamaParse（文档智能体平台）

**LlamaParse** 是一个独立平台，专注于文档智能体和智能体 OCR。它包含 **Parse**（解析）、**LlamaAgents**（已部署的文档智能体）、**Extract**（结构化提取）和 **Index**（数据摄入与 RAG）。你可以将其与 LlamaIndex 框架配合使用，或单独运行。

- **[注册 LlamaParse](https://cloud.llamaindex.ai?utm_medium=li_github&utm_source=github&utm_campaign=2026--)** —— 创建账户并获取你的 API 密钥。
- **Parse** —— 智能体 OCR 与文档解析（支持 130 多种格式）。[文档](https://developers.llamaindex.ai/python/cloud/llamaparse/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)
- **Extract** —— 从文档中提取结构化数据。[文档](https://developers.llamaindex.ai/python/cloud/llamaextract/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)
- **Index** —— 数据摄入、索引构建与 RAG（检索增强生成）流水线。[文档](https://developers.llamaindex.ai/python/cloud/llamacloud/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)
- **Split** —— 将大型文档拆分为子类别。[文档](https://developers.llamaindex.ai/python/cloud/split/getting_started/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)
- **Agents** —— 使用 `Workflows` 和智能体构建器搭建端到端的文档智能体。[文档](https://developers.llamaindex.ai/python/llamaagents/overview/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)

### 重要链接

[文档](https://developers.llamaindex.ai/python/framework/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)

[X（原 Twitter）](https://x.com/llama_index)

[LinkedIn](https://www.linkedin.com/company/llamaindex/)

[Reddit](https://www.reddit.com/r/LlamaIndex/)

[Discord](https://discord.gg/dGcwcsnxhU)

## 🚀 概述

**注意**：本 README 的更新频率不如文档高。请查阅上方的文档以获取最新内容！

### 背景

- 大语言模型（LLM）在知识生成与推理方面是一项卓越的技术。它们基于海量公开数据进行了预训练。
- 我们该如何最好地利用私有数据来增强 LLM？

我们需要一套全面的工具包来帮助完成针对 LLM 的数据增强工作。

### 解决方案

这正是 **LlamaIndex** 的用武之地。LlamaIndex 是一个“数据框架”，旨在帮助你构建 LLM 应用。它提供以下功能：

- 提供**数据连接器**，用于摄入你现有的数据源和数据格式（API、PDF、文档、SQL 等）。
- 提供**数据结构化**方法（索引、图谱），以便轻松将数据与 LLM 配合使用。
- 提供针对数据的**高级检索/查询接口**：输入任意 LLM 提示词，即可返回检索到的上下文及知识增强后的输出。
- 支持与外部应用框架轻松集成（例如 LangChain、Flask、Docker、ChatGPT 或其他工具）。

LlamaIndex 为新手用户和高级用户提供不同层次的工具体验。我们的上层 API 允许新手用户在短短 5 行代码内完成数据的摄入与查询。而下层 API 则让高级用户可以自定义并扩展任意模块（数据连接器、索引、检索器、查询引擎、重排序模块等），以满足特定需求。

## 💡 贡献指南

有兴趣参与贡献吗？我们欢迎并鼓励对 LlamaIndex 核心库的贡献，以及基于核心构建的集成开发！更多详情请参阅我们的 [贡献指南](CONTRIBUTING.md)。

新集成需与现有的 LlamaIndex 框架组件有实质性的结合。LlamaIndex 维护者保留根据具体情况决定是否接受某些集成的权利。

## 📄 文档

完整文档请查阅 [此处](https://developers.llamaindex.ai/python/framework/?utm_medium=li_github&utm_source=github&utm_campaign=2026--)

欢迎浏览以获取最新的教程、操作指南、参考文档及其他资源！

## 💻 示例用法

```sh
# custom selection of integrations to work with core
pip install llama-index-core
pip install llama-index-llms-openai
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
```

示例位于 `docs/examples` 文件夹中。索引文件位于 `indices` 文件夹（详见下方的索引列表）。

使用 OpenAI 构建简单的向量存储索引：

```python
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("YOUR_DATA_DIRECTORY").load_data()
index = VectorStoreIndex.from_documents(documents)
```

使用非 OpenAI 的 LLM（例如通过 Ollama 托管的大语言模型）构建简单的向量存储索引：

```python
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from transformers import AutoTokenizer

# set the LLM
Settings.llm = Ollama(
    model="llama-3.1:latest",
    request_timeout=360.0,
)

# set tokenizer to match LLM
Settings.tokenizer = AutoTokenizer.from_pretrained(
    "meta-llama/Llama-3.1-8B-Instruct"
)

# set the embed model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

documents = SimpleDirectoryReader("YOUR_DATA_DIRECTORY").load_data()
index = VectorStoreIndex.from_documents(
    documents,
)
```

进行查询：

```python
query_engine = index.as_query_engine()
query_engine.query("YOUR_QUESTION")
```

默认情况下，数据存储在内存中。
若要持久化到磁盘（位于 `./storage` 目录下）：

```python
index.storage_context.persist()
```

从磁盘重新加载：

```python
from llama_index.core import StorageContext, load_index_from_storage

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)
```

## 关于构建资产验证的说明

默认情况下，`llama-index-core` 包含一个 `_static` 文件夹，其中预置了 nltk 和 tiktoken 缓存（随包安装一同提供）。这确保了你在运行时受磁盘访问权限限制的环境中也能轻松运行 `llama-index`。

为验证这些文件的安全性与有效性，我们使用了 GitHub 的 `attest-build-provenance` Action。该 Action 会校验 `_static` 文件夹中的文件是否与 `llama-index-core/llama_index/core/_static` 目录下的文件一致。

你可以通过运行以下脚本进行验证（请将路径指向你的已安装包）：

```bash
#!/bin/bash
STATIC_DIR="venv/lib/python3.13/site-packages/llama_index/core/_static"
REPO="run-llama/llama_index"

find "$STATIC_DIR" -type f | while read -r file; do
    echo "Verifying: $file"
    gh attestation verify "$file" -R "$REPO" || echo "Failed to verify: $file"
done
```

## 📖 引用方式

如果你在论文中使用了 LlamaIndex，请引用以下内容：

```
@software{Liu_LlamaIndex_2022,
author = {Liu, Jerry},
doi = {10.5281/zenodo.1234},
month = {11},
title = {{LlamaIndex}},
url = {https://github.com/jerryjliu/llama_index},
year = {2022}
}
```