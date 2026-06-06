<div align="center">

# Pathway AI Pipelines

<a href="https://trendshift.io/repositories/4400" target="_blank"><img src="https://trendshift.io/api/badge/repositories/4400" alt="pathwaycom%2Fllm-app | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
[![chat on Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/pathway)
[![follow on X](  https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/intent/follow?screen_name=pathway_com)
</div>

Pathway Live Data Framework 的 **AI Pipelines** 允许你快速将提供**高准确率 RAG（检索增强生成）和大规模 AI 企业搜索**的应用投入生产环境，并充分利用数据源中最新的知识。它提供了开箱即用的 **LLM（大语言模型）应用模板**。你可以在本地机器上测试它们，并部署到云端（GCP、AWS、Azure、Render 等）或本地服务器。

这些应用能够与你的**文件系统、Google Drive、Sharepoint、S3、Kafka、PostgreSQL 以及实时数据 API** 等数据源连接并同步（包括所有新增、删除和更新的数据）。它们无需额外的基础设施依赖或单独配置。内置了**数据索引功能**，支持向量搜索、混合搜索和全文检索——全部在内存中完成，并配备缓存机制。


## Application Templates

本仓库提供的应用模板可处理高达**数百万页文档**的数据。部分模板针对简洁性进行了优化，另一些则专注于极高的准确率。请选择最适合你的那一款。你可以直接使用它，也可以修改流水线中的某些步骤——例如，如果你想添加新的数据源，或将向量索引改为混合索引，仅需一行代码即可实现。 

| 应用（模板）                                                                           | 描述                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``[`问答型 RAG 应用`](templates/question_answering_rag/)``    | 基础端到端 RAG 应用。一个问答流水线，使用你指定的 GPT 模型对实时连接的数据源（文件、Google Drive、Sharepoint 等）中的文档（PDF、DOCX 等）进行查询并返回答案。你也可以尝试 [演示 REST 接口](https://pathway.com/solutions/rag-pipelines#try-it-out)。              |
| ``[`实时文档索引（向量存储 / 检索器）`](templates/document_indexing/)``     | 面向 RAG 的实时文档索引流水线，充当向量存储服务。它对来自连接数据源的文件进行实时索引。可与任何前端配合使用，或作为 [Langchain](https://pathway.com/blog/langchain-integration) 或 [Llamaindex](https://pathway.com/blog/llamaindex-pathway) 应用的检索后端集成。你也可以尝试 [演示 REST 接口](https://pathway.com/solutions/ai-contract-management#try-it-out)。         |
| ``[`基于 GPT4o 的多模态 RAG 流水线`](templates/multimodal_rag/)`` | 在解析阶段使用 GPT-4o 进行多模态 RAG，对来自连接数据源的文件、Google Drive、Sharepoint 等中的 PDF 及其他文档建立索引。非常适合从文件夹的非结构化财务文档（包括图表和表格）中提取信息，并在文档变更或新增时自动更新结果。|
| ``[`非结构化到 SQL 流水线 + SQL 问答`](templates/unstructured_to_sql_on_the_fly/)`` | RAG 示例应用，连接非结构化财务数据源（如财务报告 PDF），将数据结构化为 SQL 并加载至 PostgreSQL 表中。它还通过 LLM 将用户的自然语言查询转换为 SQL，并在 PostgreSQL 表上执行查询以回答这些财务文档相关问题。 |
| ``[`自适应 RAG 应用`](templates/adaptive_rag/)`` | 采用 Pathway 开发的 Adaptive RAG 技术的 RAG 应用，可在保持准确率的同时，将 Token 成本降低多达 4 倍。 |
| ``[`基于 Mistral 和 Ollama 的私有 RAG 应用`](templates/private_rag/)`` | 使用 Pathway Live Data Framework、Mistral 和 Ollama 构建的 `question_answering_rag` RAG 流水线的完全私有（本地）版本。 |
| ``[`幻灯片 AI 搜索应用`](templates/slides_ai_search/)``                                        | 用于检索幻灯片的索引流水线。它对 PowerPoint 和 PDF 进行多模态处理，并维护你幻灯片的实时索引。|


## How do these AI Pipelines work?

这些应用可以作为 **Docker 容器**运行，并暴露一个 **HTTP API** 用于连接前端。为了便于快速测试和演示，部分应用模板还包含可选的 Streamlit UI，可直接与该 API 交互。 

这些应用依赖 [Pathway Live Data framework](https://github.com/pathwaycom/pathway) 进行数据源同步和 API 请求服务（Pathway 是一个内置 Rust 引擎的独立 Python 库）。它为你提供了**简洁统一的后端、Embedding、检索与 LLM 技术栈逻辑**。你无需为 Gen AI 应用集成和维护单独的模块：~~向量数据库（如 Pinecone/Weaviate/Qdrant）+ 缓存（如 Redis）+ API 框架（如 FastAPI）~~。Pathway 默认采用的**内置向量索引**基于极速的 [usearch](https://github.com/unum-cloud/usearch) 库，而**混合全文索引**则使用了 [Tantivy](https://github.com/quickwit-oss/tantivy) 库。开箱即用，一切就绪。

## Getting started

本仓库中的每个 [应用模板](templates/) 都包含一个 `README.md`，其中附有运行说明。

你还可以访问 Pathway 官网查看[更多开箱即用的代码模板](https://pathway.com/developers/templates/)。


## Some visual highlights

**多模态 RAG 实时提取与整理**：轻松从 PDF、文档等文件中提取并整理表格和图表数据，全程实时更新：

![Effortlessly extract and organize table and chart data from PDFs, docs, and more with multimodal RAG - in real-time](https://github.com/pathwaycom/llm-app/blob/main/templates/multimodal_rag/gpt4o_with_pathway_comparison.gif)

（查看 ``[`基于 GPT4o 的多模态 RAG 流水线`](templates/multimodal_rag/)`` 以了解完整流水线的运行情况。你也可以参考 ``[`非结构化到 SQL 流水线`](templates/unstructured_to_sql_on_the_fly/)``，该示例同样适用于非多模态模型。）


**自动化实时知识挖掘与告警**：

![Automated real-time knowledge mining and alerting](templates/drive_alert/drive_alert_demo.gif)

（查看 [`Google Drive 答案变更告警`](https://github.com/pathwaycom/llm-app/tree/main/templates/drive_alert) 应用示例。）


### Do-it-Yourself Videos

▶️ [使用 Pathway Live Data Framework 构建 LLM 应用入门](https://www.youtube.com/watch?v=kcrJSk00duw) - 作者：[Jan Chorowski](https://scholar.google.com/citations?user=Yc94070AAAAJ)

▶️ [11 分钟搭建一个真实的 LLM 应用](https://www.youtube.com/watch?v=k1XGo7ts4tI) - 作者：[Pau Labarta Bajo](https://substack.com/@paulabartabajo)


## Troubleshooting

如需反馈或报告 Bug，请在我们的 [Issue Tracker](https://github.com/pathwaycom/pathway/issues) 上提交 Issue。

## Contributing

非常欢迎任何人参与本项目，无论是文档完善、功能开发、Bug 修复、代码清理、测试还是代码审查。如果你是第一次向 GitHub 项目贡献代码，可以参考这份 [入门指南](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)。 

如果你计划进行需要较多工作的贡献，欢迎在 [Pathway Discord 服务器](https://discord.com/invite/pathway)（`#get-help` 频道）留言告知你的计划！

## Supported and maintained by

<p align="center">
  <a href="https://github.com/pathwaycom/"><img src="https://pathway.com/logo-light.svg" alt="Pathway"/></a>
</p>
<p align="center">
  <a href="https://pathway.com/solutions/llm-app">
    <img src="https://img.shields.io/badge/See%20Pathway's%20offering%20for%20AI%20applications-0000FF" alt="See Pathway's offering for AI applications"/>
  </a>
</p>