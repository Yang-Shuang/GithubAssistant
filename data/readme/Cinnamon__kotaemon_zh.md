<div align="center">

# kotaemon

一个开源、简洁且可定制的基于文档对话的 RAG UI。兼顾最终用户与开发者体验构建。

![Preview](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/preview-graph.png)

<a href="https://trendshift.io/repositories/11607" target="_blank"><img src="https://trendshift.io/api/badge/repositories/11607" alt="Cinnamon%2Fkotaemon | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[在线演示 #1](https://huggingface.co/spaces/cin-model/kotaemon) |
[在线演示 #2](https://huggingface.co/spaces/cin-model/kotaemon-demo) |
[在线安装](https://cinnamon.github.io/kotaemon/online_install/) |
[Colab 笔记本 (本地 RAG)](https://colab.research.google.com/drive/1eTfieec_UOowNizTJA1NjawBJH9y_1nn)

[用户指南](https://cinnamon.github.io/kotaemon/) |
[开发者指南](https://cinnamon.github.io/kotaemon/development/) |
[反馈建议](https://github.com/Cinnamon/kotaemon/issues) |
[联系我们](mailto:kotaemon.support@cinnamon.is)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-31013/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<a href="https://github.com/Cinnamon/kotaemon/pkgs/container/kotaemon" target="_blank">
<img src="https://img.shields.io/badge/docker_pull-kotaemon:latest-brightgreen" alt="docker pull ghcr.io/cinnamon/kotaemon:latest"></a>
![download](https://img.shields.io/github/downloads/Cinnamon/kotaemon/total.svg?label=downloads&color=blue)
<a href='https://huggingface.co/spaces/cin-model/kotaemon-demo'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue'></a>
<a href="https://hellogithub.com/en/repository/d3141471a0244d5798bc654982b263eb" target="_blank"><img src="https://abroad.hellogithub.com/v1/widgets/recommend.svg?rid=d3141471a0244d5798bc654982b263eb&claim_uid=RLiD9UZ1rEHNaMf&theme=small" alt="Featured｜HelloGitHub" /></a>

</div>

<!-- start-intro -->

## 简介

本项目为希望基于文档进行问答（QA）的最终用户，以及希望构建自有 RAG 流水线的开发者提供了一个功能完善的 RAG UI。
<br>

```yml
+----------------------------------------------------------------------------+
| End users: Those who use apps built with `kotaemon`.                       |
| (You use an app like the one in the demo above)                            |
|     +----------------------------------------------------------------+     |
|     | Developers: Those who built with `kotaemon`.                   |     |
|     | (You have `import kotaemon` somewhere in your project)         |     |
|     |     +----------------------------------------------------+     |     |
|     |     | Contributors: Those who make `kotaemon` better.    |     |     |
|     |     | (You make PR to this repo)                         |     |     |
|     |     +----------------------------------------------------+     |     |
|     +----------------------------------------------------------------+     |
+----------------------------------------------------------------------------+
```

### 面向最终用户

- **简洁美观的 UI**：专为基于 RAG 的 QA 设计的友好界面。
- **支持多种 LLM**：兼容主流 LLM API 提供商（OpenAI、AzureOpenAI、Cohere 等）及本地大语言模型（通过 `ollama` 和 `llama-cpp-python`）。
- **快速上手安装**：提供简便脚本助你迅速开始。

### 面向开发者

- **RAG 流水线框架**：提供工具以构建基于 RAG 的文档 QA 流水线。
- **可定制 UI**：通过内置 <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a> 界面直观展示你的 RAG 流水线运行效果。
- **Gradio 主题**：如果你使用 Gradio 进行开发，可查看我们的主题：[kotaemon-gradio-theme](https://github.com/lone17/kotaemon-gradio-theme)。

## 核心功能

- **托管你自己的文档问答（RAG）Web UI**：支持多用户登录，在私有/公共集合中组织文件，协作分享你喜欢的对话。

- **管理你的 LLM 与 Embedding 模型**：同时支持本地大语言模型及主流 API 提供商（OpenAI、Azure、Ollama、Groq）。

- **混合 RAG 流水线**：提供合理的默认 RAG 流水线，采用混合（全文检索 + 向量检索）检索器与重排序机制，确保最佳检索质量。

- **多模态问答支持**：支持对包含图表的多个文档进行问答。支持多模态文档解析（可在 UI 中选择配置）。

- **高级引用与文档预览**：系统默认提供详细引用以确保 LLM 答案的准确性。你可以在内置浏览器 PDF 查看器中直接查看引用内容（含相关度分数）并高亮显示。当检索流水线返回的相关度较低时，会发出警告提示。

- **支持复杂推理方法**：使用问题分解回答复杂/多跳问题。支持基于 `ReAct`、`ReWOO` 及其他 Agent 的推理方式。

- **可配置的设置界面**：你可以在 UI 上调整检索与生成过程的大部分关键参数（包括提示词）。

- **高度可扩展**：基于 Gradio 构建，你可以自由定制或添加任何 UI 元素。同时，我们致力于支持多种文档索引与检索策略。`GraphRAG` 索引流水线已作为示例提供。

![Preview](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/preview.png)

## 安装指南

> 如果你不是开发者，只是希望使用本应用，请查阅我们的 [用户指南](https://cinnamon.github.io/kotaemon/)。从[最新版本发布页](https://github.com/Cinnamon/kotaemon/releases/latest)下载 `.zip` 文件即可获取最新功能与 Bug 修复。

### 系统要求

1. [Python](https://www.python.org/downloads/) >= 3.10
2. [Docker](https://www.docker.com/）：可选，若你选择[使用 Docker 安装](#with-docker-recommended)
3. [Unstructured](https://docs.unstructured.io/open-source/installation/full-installation#full-installation)：若需处理 `.pdf`、`.html`、`.mhtml` 和 `.xlsx` 以外的文件类型。具体安装步骤因操作系统而异，请访问链接并按说明操作。

### 使用 Docker（推荐）

1. 我们支持 `lite`（轻量版）与 `full`（完整版）两种 Docker 镜像。`full` 版本会额外安装 `unstructured` 相关依赖包，从而支持更多文件格式（`.doc`, `.docx` 等），但代价是镜像体积更大。对大多数用户而言，`lite` 版本已足够满足日常需求。

   - 使用 `full` 版本：

     ```shell
     docker run \
     -e GRADIO_SERVER_NAME=0.0.0.0 \
     -e GRADIO_SERVER_PORT=7860 \
     -v ./ktem_app_data:/app/ktem_app_data \
     -p 7860:7860 -it --rm \
     ghcr.io/cinnamon/kotaemon:main-full
     ```

   - 使用内置 **Ollama** 的 `full` 版本进行 _本地/私有 RAG_：

     ```shell
     # 将镜像名称更改为
     docker run <...> ghcr.io/cinnamon/kotaemon:main-ollama
     ```

   - 使用 `lite` 版本：

   ```shell
    # 将镜像名称更改为
    docker run <...> ghcr.io/cinnamon/kotaemon:main-lite
   ```

2. 我们目前支持并测试了两个平台：`linux/amd64` 和 `linux/arm64`（适用于新款 Mac）。你可以通过在 `docker run` 命令中传递 `--platform` 参数来指定平台。例如：

   ```shell
   # 以 linux/arm64 平台运行 Docker
   docker run \
   -e GRADIO_SERVER_NAME=0.0.0.0 \
   -e GRADIO_SERVER_PORT=7860 \
   -v ./ktem_app_data:/app/ktem_app_data \
   -p 7860:7860 -it --rm \
   --platform linux/arm64 \
   ghcr.io/cinnamon/kotaemon:main-lite
   ```

3. 配置完成后，访问 `http://localhost:7860/` 即可进入 Web UI。

4. 我们使用 [GHCR](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) 存储 Docker 镜像，所有镜像均可在[此处](https://github.com/Cinnamon/kotaemon/pkgs/container/kotaemon)查看。

### 不使用 Docker

1. 克隆仓库：

   ```shell
   git clone https://github.com/Cinnamon/kotaemon
   cd kotaemon
   ```

2. 配置环境：

- **选项 1：使用 [uv](https://docs.astral.sh/uv/getting-started/installation/)（推荐）**

  ```shell
  uv sync --python 3.10
  source .venv/bin/activate
  ```

- **选项 2：使用 conda**

  ```shell
  conda create -n kotaemon python=3.10
  conda activate kotaemon

  pip install -e "libs/kotaemon[all]"
  pip install -e "libs/ktem"
  ```

3. 在项目根目录创建 `.env` 文件。可参考 `.env.example` 模板进行配置。

   `.env` 文件主要用于在应用启动前预配置模型的场景（例如部署到 HF Hub）。该文件仅在首次运行时用于初始化数据库，后续运行将不再读取此文件。

4. （可选）若要启用浏览器内 `PDF_JS` 查看器，请下载 [PDF_JS_DIST](https://github.com/mozilla/pdf.js/releases/download/v4.0.379/pdfjs-4.0.379-dist.zip) 并将其解压至 `libs/ktem/ktem/assets/prebuilt`。

   <img src="https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/pdf-viewer-setup.png" alt="pdf-setup" width="300">

5. 启动 Web 服务器：

   ```shell
   python app.py
   ```

   - 应用将在你的浏览器中自动打开。
   - 默认用户名和密码均为 `admin`。你可直接通过 UI 创建额外用户。

   ![Chat tab](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/chat-tab.png)

6. 检查 `Resources`（资源）选项卡以及 `LLMs and Embeddings`，确保你的 `.env` 文件中的 `api_key` 已正确配置。若未设置，可在此处直接填写。

### 配置 GraphRAG

> [!NOTE]
> Microsoft 官方 GraphRAG 索引仅支持 OpenAI 或 Ollama API。
> 我们建议大多数用户使用 NanoGraphRAG 实现，以便与 Kotaemon 进行无缝集成。

<details>

<summary>配置 Nano GRAPHRAG</summary>

- 安装 nano-GraphRAG：`pip install nano-graphrag`
- `nano-graphrag` 安装可能引发版本冲突，详见[此 Issue](https://github.com/Cinnamon/kotaemon/issues/440)
  - 快速修复方法：`pip uninstall hnswlib chroma-hnswlib && pip install chroma-hnswlib`
- 设置环境变量 `USE_NANO_GRAPHRAG=true` 启动 Kotaemon。
- 在资源设置中配置默认的 LLM 与 Embedding 模型，系统会自动从 NanoGraphRAG 识别并加载。

</details>

<details>

<summary>配置 LIGHTRAG</summary>

- 安装 LightRAG：`pip install git+https://github.com/HKUDS/LightRAG.git`
- `LightRAG` 安装可能引发版本冲突，详见[此 Issue](https://github.com/Cinnamon/kotaemon/issues/440)
  - 快速修复方法：`pip uninstall hnswlib chroma-hnswlib && pip install chroma-hnswlib`
- 设置环境变量 `USE_LIGHTRAG=true` 启动 Kotaemon。
- 在资源设置中配置默认的 LLM 与 Embedding 模型，系统会自动从 LightRAG 识别并加载。

</details>

<details>

<summary>配置 MS GRAPHRAG</summary>

- **非 Docker 安装**：若不使用 Docker，请通过以下命令安装 GraphRAG：

  ```shell
  pip install "graphrag<=0.3.6" future
  ```

- **设置 API KEY**：若要使用 GraphRAG 检索功能，请确保已配置 `GRAPHRAG_API_KEY` 环境变量。你可以直接在终端中 export，或将其添加到 `.env` 文件中。
- **使用本地模型与自定义配置**：若希望将 GraphRAG 与本地模型（如 `Ollama`）配合使用，或自定义默认 LLM 及其他参数，请将环境变量 `USE_CUSTOMIZED_GRAPHRAG_SETTING` 设为 true。随后在 `settings.yaml.example` 文件中调整你的配置即可。

</details>

### 配置本地模型（用于本地/私有 RAG）

详见 [Local model setup](docs/local_model.md)。

### 配置多模态文档解析（OCR、表格解析、图表提取）

目前支持以下选项：

- [Azure Document Intelligence (API)](https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence)
- [Adobe PDF Extract (API)](https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/)
- [Docling (本地，开源)](https://github.com/DS4SD/docling) – 详见 [integrations/docling.md](./docs/integrations/docling.md) 获取 Kotaemon 专属配置说明。
- [PaddleOCR (本地，开源)](https://github.com/PADDLEPADDLE/PADDLEOCR) – 详见 [integrations/paddle_ocr.md](./docs/integrations/paddle_ocr.md) 获取 Kotaemon 专属配置说明。

在 `Settings -> Retrieval Settings -> File loader` 中选择对应的解析器即可。

### 自定义你的应用

- 默认情况下，所有应用数据均存储在 `./ktem_app_data` 文件夹中。你可通过备份或复制该文件夹将安装迁移至新机器。

- 针对高级用户或特定使用场景，你可自定义以下文件：

  - `flowsettings.py`
  - `.env`

#### `flowsettings.py`

该文件包含应用的核心配置。你可以参考示例 [此处](flowsettings.py) 作为起点进行修改。

<details>

<summary>关键配置项</summary>

```python
# setup your preferred document store (with full-text search capabilities)
KH_DOCSTORE=(Elasticsearch | LanceDB | SimpleFileDocumentStore)

# setup your preferred vectorstore (for vector-based search)
KH_VECTORSTORE=(ChromaDB | LanceDB | InMemory | Milvus | Qdrant)

# Enable / disable multimodal QA
KH_REASONINGS_USE_MULTIMODAL=True

# Setup your new reasoning pipeline or modify existing one.
KH_REASONINGS = [
    "ktem.reasoning.simple.FullQAPipeline",
    "ktem.reasoning.simple.FullDecomposeQAPipeline",
    "ktem.reasoning.react.ReactAgentPipeline",
    "ktem.reasoning.rewoo.RewooAgentPipeline",
]
```

</details>

#### `.env`

该文件提供了另一种配置模型与凭证的方式。

<details>

<summary>通过 .env 文件配置模型</summary>

- 你也可通过应用目录下的 `.env` 文件配置模型连接信息。若未找到该文件，可手动创建。

- 目前支持以下提供商：

  - **OpenAI**

    在 `.env` 文件中设置 `OPENAI_API_KEY` 变量并填入你的 OpenAI API Key，即可启用 OpenAI 模型访问权限。其他参数可根据实际需求修改，默认配置通常已能满足大多数场景。

    ```shell
    OPENAI_API_BASE=https://api.openai.com/v1
    OPENAI_API_KEY=<your OpenAI API key here>
    OPENAI_CHAT_MODEL=gpt-3.5-turbo
    OPENAI_EMBEDDINGS_MODEL=text-embedding-ada-002
    ```

  - **Azure OpenAI**

    对于通过 Azure 平台使用的 OpenAI 模型，你需要提供 Azure 端点地址与 API Key。根据你在 Azure 上的部署配置，可能还需要指定 Chat 模型和 Embedding 模型的部署名称（Deployment Name）。

    ```shell
    AZURE_OPENAI_ENDPOINT=
    AZURE_OPENAI_API_KEY=
    OPENAI_API_VERSION=2024-02-15-preview
    AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-35-turbo
    AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=text-embedding-ada-002
    ```

  - **本地模型**

    - 使用 `ollama` OpenAI 兼容服务端：

      - 安装 [ollama](https://github.com/ollama/ollama) 并启动服务。

      - 拉取你的模型，例如：

        ```shell
        ollama pull llama3.1:8b
        ollama pull nomic-embed-text
        ```

      - 在 Web UI 中设置模型名称并将其设为默认值：

        ![Models](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/models.png)

    - 使用 `GGUF` 格式配合 `llama-cpp-python`

      你可从 [Hugging Face Hub](https://huggingface.co/models) 搜索并下载适用于本地运行的 LLM。目前支持的模型格式如下：

      - GGUF

        请选择体积小于设备可用内存的模型（建议预留约 2 GB）。例如，若你的总内存为 16 GB，可用内存为 12 GB，则应选择占用不超过 10 GB 的模型。通常更大的模型能生成更好的结果，但也会消耗更多推理时间。

        以下是一些推荐模型及其内存占用参考：

      - [Qwen1.5-1.8B-Chat-GGUF](https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat-GGUF/resolve/main/qwen1_5-1_8b-chat-q8_0.gguf?download=true)：约 2 GB

        在 Web UI 中添加新的 LlamaCpp 模型并填入对应名称即可。

  </details>

### 添加自定义 RAG 流水线

#### 自定义推理流水线

1. 查看默认流水线实现代码 [此处](libs/ktem/ktem/reasoning/simple.py)。你可快速调整默认 QA 流水线的行为逻辑。
2. 在 `libs/ktem/ktem/reasoning/` 目录下新增 `.py` 文件，并在 `flowssettings` 中注册即可在 UI 上启用。

#### 自定义索引流水线

- 参考示例实现：`libs/ktem/ktem/index/file/graph`

> （更多说明正在完善中）。

<!-- end-intro -->

## 引用

引用本项目时请使用以下格式：

```BibTeX
@misc{kotaemon2024,
    title = {Kotaemon - An open-source RAG-based tool for chatting with any content.},
    author = {The Kotaemon Team},
    year = {2024},
    howpublished = {\url{https://github.com/Cinnamon/kotaemon}},
}
```

## 星标历史

<a href="https://star-history.com/#Cinnamon/kotaemon&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Cinnamon/kotaemon&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Cinnamon/kotaemon&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Cinnamon/kotaemon&type=Date" />
 </picture>
</a>

## 贡献指南

由于本项目正处于快速迭代阶段，我们非常重视你的反馈与贡献。请查阅我们的 [贡献指南](https://github.com/Cinnamon/kotaemon/blob/main/CONTRIBUTING.md) 开始参与开发。感谢所有贡献者的付出！

<a href="https://github.com/Cinnamon/kotaemon/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Cinnamon/kotaemon" />
</a>