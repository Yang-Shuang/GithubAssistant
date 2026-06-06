<div align="center">

<div style="margin: 20px 0;">
  <img src="./assets/logo.png" width="120" height="120" alt="LightRAG Logo" style="border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 217, 255, 0.3);">
</div>

# 🚀 LightRAG：简单高效的检索增强生成（Retrieval-Augmented Generation）

<div align="center">
    <a href="https://trendshift.io/repositories/13043" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13043" alt="HKUDS%2FLightRAG | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>
<p>
</p>
<div align="center">
  <div style="width: 100%; height: 2px; margin: 20px 0; background: linear-gradient(90deg, transparent, #00d9ff, transparent);"></div>
</div>

<div align="center">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 25px; text-align: center;">
    <p>
      <a href='https://github.com/HKUDS/LightRAG'><img src='https://img.shields.io/badge/🔥项目主页-00d9ff?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a2e'></a>
      <a href='https://arxiv.org/abs/2410.05779'><img src='https://img.shields.io/badge/📄arXiv-2410.05779-ff6b6b?style=for-the-badge&logo=arxiv&logoColor=white&labelColor=1a1a2e'></a>
      <a href="https://github.com/HKUDS/LightRAG/stargazers"><img src='https://img.shields.io/github/stars/HKUDS/LightRAG?color=00d9ff&style=for-the-badge&logo=star&logoColor=white&labelColor=1a1a2e' /></a>
    </p>
    <p>
      <img src="https://img.shields.io/badge/🐍Python-3.10-4ecdc4?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a2e">
      <a href="https://pypi.org/project/lightrag-hku/"><img src="https://img.shields.io/pypi/v/lightrag-hku.svg?style=for-the-badge&logo=pypi&logoColor=white&labelColor=1a1a2e&color=ff6b6b"></a>
    </p>
    <p>
      <a href="https://discord.gg/yF2MmDJyGJ"><img src="https://img.shields.io/badge/💬Discord-社区-7289da?style=for-the-badge&logo=discord&logoColor=white&labelColor=1a1a2e"></a>
      <a href="https://github.com/HKUDS/LightRAG/issues/285"><img src="https://img.shields.io/badge/💬微信群-07c160?style=for-the-badge&logo=wechat&logoColor=white&labelColor=1a1a2e"></a>
    </p>
    <p>
      <a href="README-zh.md"><img src="https://img.shields.io/badge/🇨🇳中文版-1a1a2e?style=for-the-badge"></a>
      <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸English-1a1a2e?style=for-the-badge"></a>
    </p>
    <p>
      <a href="https://pepy.tech/projects/lightrag-hku"><img src="https://static.pepy.tech/personalized-badge/lightrag-hku?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads"></a>
    </p>
  </div>
</div>

</div>

<div align="center" style="margin: 30px 0;">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">
</div>

<div align="center" style="margin: 30px 0;">
    <img src="./README.assets/b2aaf634151b4706892693ffb43d9093.png" width="800" alt="LightRAG Diagram">
</div>

---

<div align="center">
  <table>
    <tr>
      <td style="vertical-align: middle;">
        <img src="./assets/LiteWrite.png"
             width="56"
             height="56"
             alt="LiteWrite"
             style="border-radius: 12px;" />
      </td>
      <td style="vertical-align: middle; padding-left: 12px;">
        <a href="https://litewrite.ai">
          <img src="https://img.shields.io/badge/🚀%20LiteWrite-AI%20Native%20LaTeX%20Editor-ff6b6b?style=for-the-badge&logoColor=white&labelColor=1a1a2e">
        </a>
      </td>
    </tr>
  </table>
</div>

---

## 🎉 更新动态
- [2026.05]🎯[新功能]: **将 RagAnything 合并至 LightRAG**🎉。通过 **MinerU / Docling** 服务实现多模态内容解析与提取。
- [2026.05]🎯[新功能]: 新增四种可选文本分块策略：`Fix`、`Recursive`、`Vector` 和 `Paragraph`。
- [2026.05]🎯[新功能]: **按角色配置 LLM**，支持 4 种独立角色：EXTRACT（提取）、QUERY（查询）、KEYWORDS（关键词）和 VLM，可分别设置独立的 LLM。
- [2026.03]🎯[新功能]: 集成 **OpenSearch** 作为统一的存储后端，全面支持 LightRAG 的四种存储方案。
- [2026.03]🎯[新功能]: 引入交互式安装向导。支持通过 Docker 本地部署 Embedding、重排序（Reranker）及存储后端服务。
- [2025.11]🎯[新功能]: 集成 **RAGAS 用于评估** 和 **Langfuse 用于追踪**。更新 API 以在返回查询结果的同时提供检索上下文，支持上下文精度指标计算。
- [2025.10]🎯[可扩展性增强]: 消除处理瓶颈，支持**高效处理大规模数据集**。
- [2025.09]🎯[新功能]: 提升对 **Qwen3-30B-A3B** 等开源 LLM 的知识图谱提取准确率。
- [2025.08]🎯[新功能]: 正式支持 **Reranker（重排序模型）**，显著提升混合查询性能（已设为默认查询模式）。
- [2025.08]🎯[新功能]: 新增**文档删除功能**，并自动重新生成知识图谱以确保最佳查询效果。
- [2025.06]🎯[新版本发布] 团队发布了 [RAG-Anything](https://github.com/HKUDS/RAG-Anything) —— 一个**全栈多模态 RAG** 系统，可无缝处理文本、图像、表格和公式。
- [2025.06]🎯[新功能] LightRAG 现已通过集成 [RAG-Anything](https://github.com/HKUDS/RAG-Anything) 支持全面的多模态数据处理，实现跨 PDF、图片、Office 文档、表格和公式的无缝文档解析与 RAG 能力。详情请参阅新增的[多模态章节](https://github.com/HKUDS/LightRAG/?tab=readme-ov-file#multimodal-document-processing-rag-anything-integration)。
- [2025.03]🎯[新功能] LightRAG 现已支持引用功能，可实现规范的来源标注并增强文档可追溯性。
- [2025.02]🎯[新功能] 你现在可以使用 MongoDB 作为一体化存储方案，实现统一的数据管理。
- [2025.02]🎯[新版本发布] 团队发布了 [VideoRAG](https://github.com/HKUDS/VideoRAG) —— 专为理解超长上下文视频设计的 RAG 系统。
- [2025.01]🎯[新版本发布] 团队发布了 [MiniRAG](https://github.com/HKUDS/MiniRAG)，利用小模型让 RAG 更简单。
- [2025.01]🎯你现在可以使用 PostgreSQL 作为一体化存储方案进行数据管理。
- [2024.11]🎯[新资源] LearnOpenCV 现已发布 LightRAG 综合指南：[LearnOpenCV](https://learnopencv.com/lightrag)。—— 深入教程与最佳实践。感谢博客作者的杰出贡献！
- [2024.11]🎯[新功能] 推出 LightRAG WebUI —— 一个直观的基于 Web 的界面，允许你通过可视化面板插入、查询和探索 LightRAG 知识图谱。
- [2024.11]🎯[新功能] 你现在可以 [使用 Neo4J 进行存储](https://github.com/HKUDS/LightRAG?tab=readme-ov-file#using-neo4j-for-storage)，启用图数据库支持。
- [2024.10]🎯[新功能] 我们添加了 [LightRAG 介绍视频](https://youtu.be/oageL-1I0GE) 的链接 —— 详细演示 LightRAG 的核心能力。感谢作者的杰出贡献！
- [2024.10]🎯[新渠道] 我们创建了 [Discord 频道](https://discord.gg/yF2MmDJyGJ)!💬 欢迎加入我们的社区进行分享、讨论与合作！🎉🎉

<details>
  <summary style="font-size: 1.4em; font-weight: bold; cursor: pointer; display: list-item;">
    算法流程图
  </summary>

![LightRAG Indexing Flowchart](https://learnopencv.com/wp-content/uploads/2024/11/LightRAG-VectorDB-Json-KV-Store-Indexing-Flowchart-scaled.jpg)
*图 1：LightRAG 索引流程图 - Img Caption : [Source](https://learnopencv.com/lightrag/)*
![LightRAG Retrieval and Querying Flowchart](https://learnopencv.com/wp-content/uploads/2024/11/LightRAG-Querying-Flowchart-Dual-Level-Retrieval-Generation-Knowledge-Graphs-scaled.jpg)
*图 2：LightRAG 检索与查询流程图 - Img Caption : [Source](https://learnopencv.com/lightrag/)*

</details>

## 安装部署

**💡 使用 uv 进行包管理**：本项目使用 [uv](https://docs.astral.sh/uv/) 进行快速可靠的 Python 包管理。请先安装 uv：`curl -LsSf https://astral.sh/uv/install.sh | sh` (Unix/macOS) 或 `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"` (Windows)

> **注意**：你也可以使用 pip，但推荐使用 uv 以获得更好的性能和更可靠的依赖管理。
>
> **📦 离线部署**：针对离线或物理隔离环境，请参阅 [离线部署指南](./docs/OfflineDeployment.md)，了解如何预装所有依赖项和缓存文件。

### 安装 LightRAG 服务端

LightRAG 服务端旨在提供 Web UI 和 API 支持。Web UI 便于文档索引、知识图谱探索以及简单的 RAG 查询接口。LightRAG 服务端还提供与 Ollama 兼容的接口，旨在将 LightRAG 模拟为 Ollama 聊天模型，从而使 AI 聊天机器人（如 Open WebUI）能够轻松调用 LightRAG。

* 从 PyPI 安装

```bash
### 使用 uv 作为工具安装 LightRAG Server（推荐）
uv tool install "lightrag-hku[api]"

### 或使用 pip 安装
# python -m venv .venv
# source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install "lightrag-hku[api]"

### 构建前端资源
cd lightrag_webui
bun install --frozen-lockfile
bun run build
cd ..

# 配置环境变量文件
# 通过从 GitHub 仓库根目录下载，或从本地源码检出中复制来获取 env.example 文件。
cp env.example .env  # 在 .env 中更新你的 LLM 和 Embedding 配置
# 启动服务端
lightrag-server
```

* 从源码安装

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG

# 初始化开发环境（推荐）
make dev
source .venv/bin/activate  # 激活虚拟环境 (Linux/macOS)
# Windows: .venv\Scripts\activate

# make dev 会安装测试工具链及完整离线栈
# （API、存储后端及服务提供商集成），然后构建前端。
# 启动服务端前请运行 make env-base 或复制 env.example 至 .env。

# uv 等效手动步骤
# 注意：uv sync 会自动在 .venv/ 中创建虚拟环境
uv sync --extra test --extra offline
source .venv/bin/activate  # 激活虚拟环境 (Linux/macOS)
# Windows: .venv\Scripts\activate

### 或使用 pip 配合虚拟环境
# python -m venv .venv
# source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install -e ".[test,offline]"

# 构建前端资源
cd lightrag_webui
bun install --frozen-lockfile
bun run build
cd ..

# 配置环境变量文件
make env-base  # 或：cp env.example .env 并手动更新
# 启动 API-WebUI 服务端
lightrag-server
```

* 使用 Docker Compose 启动 LightRAG 服务端

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG
cp env.example .env  # 在 .env 中更新你的 LLM 和 Embedding 配置
# 修改 .env 中的 LLM 和 Embedding 设置
docker compose up
```

> 历史版本的 LightRAG Docker 镜像可在此查看：[LightRAG Docker Images]( https://github.com/HKUDS/LightRAG/pkgs/container/lightrag)
>
> GitHub Actions 发布的官方 GHCR 镜像已通过 Sigstore Cosign（使用 GitHub OIDC）签名。验证命令请参阅 [docs/DockerDeployment.md](./docs/DockerDeployment.md#verify-official-ghcr-images-with-cosign)。

### 通过安装向导创建 .env 文件

无需手动编辑 `env.example`，可使用交互式安装向导生成配置好的 `.env` 及（在需要时）`docker-compose.final.yml`：

```bash
make env-base           # 必需的第一步：LLM、Embedding、Reranker
make env-storage        # 可选：存储后端与数据库服务
make env-server         # 可选：服务端端口、认证与 SSL
make env-base-rewrite   # 可选：强制重新生成向导管理的 Compose 服务块
make env-storage-rewrite # 可选：强制重新生成向导管理的 Compose 服务块
make env-security-check # 可选：审计当前 .env 的安全风险
```

所有目标的完整说明请参阅 [docs/InteractiveSetup.md](./docs/InteractiveSetup.md)。
安装向导仅更新配置；在部署前请单独运行 `make env-security-check` 以审计当前 `.env` 的安全风险。
默认情况下，重新运行安装向导会保留未更改的 Compose 服务块；仅在需要基于内置模板重建这些受管块时才使用带 `-rewrite` 后缀的目标。

### 安装 LightRAG 核心库

* 从源码安装（推荐）

```bash
cd LightRAG
# 注意：uv sync 会自动在 .venv/ 中创建虚拟环境
uv sync
source .venv/bin/activate  # 激活虚拟环境 (Linux/macOS)
# Windows: .venv\Scripts\activate

# 或使用：pip install -e .
```

* 从 PyPI 安装

```bash
uv pip install lightrag-hku
# 或：pip install lightrag-hku
```

## 快速开始

### LightRAG 的 LLM 与技术栈要求

LightRAG 对大语言模型（LLM）的能力要求显著高于传统 RAG，因为它需要 LLM 执行从文档中提取实体与关系的任务。配置合适的 Embedding 和 Reranker 模型对于提升查询性能也至关重要。

- **LLM 选型建议**：
  - 建议使用参数量至少为 320 亿的 LLM。
  - 上下文长度应至少为 32KB，推荐 64KB。
  - 在文档索引阶段不建议使用推理模型（reasoning models）。
  - 在查询阶段，建议选择比索引阶段能力更强的模型，以获得更好的查询效果。
- **Embedding 模型**：
  - 高性能的 Embedding 模型是 RAG 的核心基础。
  - 推荐使用主流的多语言 Embedding 模型，例如：`BAAI/bge-m3` 和 `text-embedding-3-large`。
  - **重要提示**：必须在文档索引前确定 Embedding 模型，并在查询阶段使用相同的模型。对于某些存储方案（如 PostgreSQL），向量维度需在初始建表时定义。因此，更换 Embedding 模型时，需删除现有的向量相关数据表，以便 LightRAG 以新维度重新创建它们。
- **Reranker 模型配置**：
  - 配置 Reranker 模型可显著提升 LightRAG 的检索性能。
  - 启用 Reranker 后，建议将“混合模式（mix mode）”设置为默认查询方式。
  - 推荐使用主流 Reranker 模型，例如：`BAAI/bge-reranker-v2-m3` 或 Jina 等服务提供的模型。

### LightRAG 服务端快速开始

LightRAG 服务端旨在提供 Web UI 和 API 支持。该服务提供了全面的知识图谱可视化功能，支持多种引力布局、节点查询、子图过滤等。有关 LightRAG 服务端的更多信息，请参阅 [LightRAG Server](./docs/LightRAG-API-Server.md)。

![iShot_2025-03-23_12.40.08](./README.assets/iShot_2025-03-23_12.40.08.png)


### LightRAG 核心库快速开始

要开始使用 LightRAG 核心库，请参考 `examples` 文件夹中的示例代码。此外，我们还提供了 [视频演示](https://www.youtube.com/watch?v=g21royNJ4fw) 以指导你完成本地部署流程。如果你已拥有 OpenAI API Key，可直接运行演示：

```bash
### 请在项目目录下运行演示代码
cd LightRAG
### 提供你的 OpenAI API-KEY
export OPENAI_API_KEY="sk-...your_opeai_key..."
### 下载示例文档 "A Christmas Carol"（查尔斯·狄更斯）
curl https://raw.githubusercontent.com/gusye1234/nano-graphrag/main/tests/mock_data.txt > ./book.txt
### 运行演示代码
python examples/lightrag_openai_demo.py
```

流式响应实现示例请参阅 `examples/lightrag_openai_compatible_demo.py`。执行前请确保已按需求修改示例代码中的 LLM 和 Embedding 配置。

**注意 1**：运行演示程序时请注意，不同的测试脚本可能使用不同的 Embedding 模型。如果你切换了 Embedding 模型，必须清空数据目录（`./dickens`）；否则程序可能会报错。若想保留 LLM 缓存，可在清空数据目录的同时保留 `kv_store_llm_response_cache.json` 文件。

**注意 2**：仅官方支持 `lightrag_openai_demo.py` 和 `lightrag_openai_compatible_demo.py` 示例代码。其他示例文件为社区贡献，未经过完整测试与优化。

## 使用 LightRAG 核心库进行开发

完整的 Core API 参考文档（包括初始化参数、`QueryParam`、LLM/Embedding 提供商示例（OpenAI, Ollama, Azure, Gemini, HuggingFace, LlamaIndex）、Reranker 注入、插入操作、实体/关系管理以及删除/合并）请参阅 **[docs/ProgramingWithCore.md](./docs/ProgramingWithCore.md)**。

> ⚠️ **如果你希望将 LightRAG 集成到你的项目中，我们推荐使用 LightRAG 服务端提供的 REST API**。LightRAG 核心库通常用于嵌入式应用，或供希望进行研究评估的开发者使用。

### 高级功能

LightRAG 提供额外的高级能力，包括 Token 用量追踪、知识图谱数据导出、LLM 缓存管理、Langfuse 可观测性集成以及基于 RAGAS 的评估。请参阅 **[docs/AdvancedFeatures.md](./docs/AdvancedFeatures.md)**。

### 多模态文档处理

LightRAG 服务端内置了针对 PDF、Office 文档、图片、表格和公式的多模态文档流水线。解析工作由外部 MinerU 或 Docling 服务处理，而多模态索引则在 LightRAG 流水线的内部运行。详细配置请参阅 **[docs/AdvancedFeatures.md](./docs/AdvancedFeatures.md)**。

## 复现论文结果

LightRAG 在农业、计算机科学、法律及混合领域均显著优于 NaiveRAG、RQ-RAG、HyDE 和 GraphRAG。完整的评估方法、提示词模板及复现步骤请参阅 **[docs/Reproduce.md](./docs/Reproduce.md)**。

**整体性能对比表**

||**农业**||**计算机科学**||**法律**||**混合领域**||
|----------------------|---------------|------------|------|------------|---------|------------|-------|------------|
||NaiveRAG|**LightRAG**|NaiveRAG|**LightRAG**|NaiveRAG|**LightRAG**|NaiveRAG|**LightRAG**|
|**全面性**|32.4%|**67.6%**|38.4%|**61.6%**|16.4%|**83.6%**|38.8%|**61.2%**|
|**多样性**|23.6%|**76.4%**|38.0%|**62.0%**|13.6%|**86.4%**|32.4%|**67.6%**|
|**赋能度**|32.4%|**67.6%**|38.8%|**61.2%**|16.4%|**83.6%**|42.8%|**57.2%**|
|**综合评分**|32.4%|**67.6%**|38.8%|**61.2%**|15.2%|**84.8%**|40.0%|**60.0%**|
||RQ-RAG|**LightRAG**|RQ-RAG|**LightRAG**|RQ-RAG|**LightRAG**|RQ-RAG|**LightRAG**|
|**全面性**|31.6%|**68.4%**|38.8%|**61.2%**|15.2%|**84.8%**|39.2%|**60.8%**|
|**多样性**|29.2%|**70.8%**|39.2%|**60.8%**|11.6%|**88.4%**|30.8%|**69.2%**|
|**赋能度**|31.6%|**68.4%**|36.4%|**63.6%**|15.2%|**84.8%**|42.4%|**57.6%**|
|**综合评分**|32.4%|**67.6%**|38.0%|**62.0%**|14.4%|**85.6%**|40.0%|**60.0%**|
||HyDE|**LightRAG**|HyDE|**LightRAG**|HyDE|**LightRAG**|HyDE|**LightRAG**|
|**全面性**|26.0%|**74.0%**|41.6%|**58.4%**|26.8%|**73.2%**|40.4%|**59.6%**|
|**多样性**|24.0%|**76.0%**|38.8%|**61.2%**|20.0%|**80.0%**|32.4%|**67.6%**|
|**赋能度**|25.2%|**74.8%**|40.8%|**59.2%**|26.0%|**74.0%**|46.0%|**54.0%**|
|**综合评分**|24.8%|**75.2%**|41.6%|**58.4%**|26.4%|**73.6%**|42.4%|**57.6%**|
||GraphRAG|**LightRAG**|GraphRAG|**LightRAG**|GraphRAG|**LightRAG**|GraphRAG|**LightRAG**|
|**全面性**|45.6%|**54.4%**|48.4%|**51.6%**|48.4%|**51.6%**|**50.4%**|49.6%|
|**多样性**|22.8%|**77.2%**|40.8%|**59.2%**|26.4%|**73.6%**|36.0%|**64.0%**|
|**赋能度**|41.2%|**58.8%**|45.2%|**54.8%**|43.6%|**56.4%**|**50.8%**|49.2%|
|**综合评分**|45.2%|**54.8%**|48.0%|**52.0%**|47.2%|**52.8%**|**50.4%**|49.6%|


## 🔗 相关项目

*生态与扩展*

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/HKUDS/RAG-Anything">
          <div style="width: 100px; height: 100px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 217, 255, 0.05) 100%); border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2); display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
            <span style="font-size: 32px;">📸</span>
          </div>
          <b>RAG-Anything</b><br>
          <sub>多模态 RAG</sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/HKUDS/VideoRAG">
          <div style="width: 100px; height: 100px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 217, 255, 0.05) 100%); border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2); display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
            <span style="font-size: 32px;">🎥</span>
          </div>
          <b>VideoRAG</b><br>
          <sub>超长上下文视频 RAG</sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/HKUDS/MiniRAG">
          <div style="width: 100px; height: 100px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 217, 255, 0.05) 100%); border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2); display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
            <span style="font-size: 32px;">✨</span>
          </div>
          <b>MiniRAG</b><br>
          <sub>极简 RAG</sub>
        </a>
      </td>
    </tr>
  </table>
</div>

---

## ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=HKUDS/LightRAG&type=Date)](https://star-history.com/#HKUDS/LightRAG&Date)

## 🤝 贡献指南

<div align="center">
  我们欢迎所有形式的贡献 —— Bug 修复、新功能、文档改进等。<br>
  请在提交 Pull Request 前阅读我们的 <a href=".github/CONTRIBUTING.md"><strong>贡献指南</strong></a>。
</div>

<br>

<div align="center">
  感谢所有贡献者的宝贵付出。
</div>

<div align="center">
  <a href="https://github.com/HKUDS/LightRAG/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=HKUDS/LightRAG" style="border-radius: 15px; box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);" />
  </a>
</div>


## 📖 引用

```python
@article{guo2024lightrag,
title={LightRAG: Simple and Fast Retrieval-Augmented Generation},
author={Zirui Guo and Lianghao Xia and Yanhua Yu and Tu Ao and Chao Huang},
year={2024},
eprint={2410.05779},
archivePrefix={arXiv},
primaryClass={cs.IR}
}
```

---

<div align="center" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 30px; margin: 30px 0;">
  <div>
    <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="500">
  </div>
  <div style="margin-top: 20px;">
    <a href="https://github.com/HKUDS/LightRAG" style="text-decoration: none;">
      <img src="https://img.shields.io/badge/⭐%20在%GitHub%上%Star-1a1a2e?style=for-the-badge&logo=github&logoColor=white">
    </a>
    <a href="https://github.com/HKUDS/LightRAG/issues" style="text-decoration: none;">
      <img src="https://img.shields.io/badge/🐛%20报告问题-ff6b6b?style=for-the-badge&logo=github&logoColor=white">
    </a>
    <a href="https://github.com/HKUDS/LightRAG/discussions" style="text-decoration: none;">
      <img src="https://img.shields.io/badge/💬%20讨论区-4ecdc4?style=for-the-badge&logo=github&logoColor=white">
    </a>
  </div>
</div>

<div align="center">
  <div style="width: 100%; max-width: 600px; margin: 20px auto; padding: 20px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 217, 255, 0.05) 100%); border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2);">
    <div style="display: flex; justify-content: center; align-items: center; gap: 15px;">
      <span style="font-size: 24px;">⭐</span>
      <span style="color: #00d9ff; font-size: 18px;">感谢访问 LightRAG！</span>
      <span style="font-size: 24px;">⭐</span>
    </div>
  </div>
</div>