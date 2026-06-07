<p align="center">
  <img src="assets/logo-text.png" alt="LEANN Logo" width="400">
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/15049" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15049" alt="yichuan-w/LEANN | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg" alt="Python Versions">
  <img src="https://github.com/yichuan-w/LEANN/actions/workflows/build-and-publish.yml/badge.svg" alt="CI Status">
  <img src="https://img.shields.io/badge/Platform-Ubuntu%20%26%20Arch%20%26%20WSL%20%7C%20macOS%20(ARM64%2FIntel)%20%7C%20Windows-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/MCP-Native%20Integration-blue" alt="MCP Integration">
  <a href="https://join.slack.com/t/leann-e2u9779/shared_invite/zt-3ol2ww9ic-Eg_kB8omwe6xmYVd0epr4Q">
    <img src="https://img.shields.io/badge/Slack-Join-4A154B?logo=slack&logoColor=white" alt="Join Slack">
  </a>

</p>

<div align="center">
  <a href="https://forms.gle/rDbZf864gMNxhpTq8">
    <img src="https://img.shields.io/badge/📣_Community_Survey-Help_Shape_v0.4-007ec6?style=for-the-badge&logo=google-forms&logoColor=white" alt="Take Survey">
  </a>
  <p>
    我们严格遵循 <b>零遥测（zero telemetry）</b> 原则。本问卷是你告诉我们是否希望下一步支持 <br>
    <b>GPU 加速</b> 或 <b>更多集成平台</b> 的唯一方式。<br>
    👉 <a href="https://forms.gle/rDbZf864gMNxhpTq8"><b>点击此处投票（约2分钟）</b></a>
  </p>
</div>

<div align="center">
  <h3>💬 加入我们的 Slack 社区！</h3>
  <p>
    我们非常欢迎你来加入 LEANN 社区！<br>
    👉 <a href="https://join.slack.com/t/leann-e2u9779/shared_invite/zt-3ol2ww9ic-Eg_kB8omwe6xmYVd0epr4Q"><b>加入 LEANN Slack</b></a><br>
    如果邀请链接已过期或你遇到加入问题，请 <a href="https://github.com/yichuan-w/LEANN/issues">提交 Issue</a>，我们会协助你完成加入！
  </p>
</div>

<h2 align="center" tabindex="-1" class="heading-element" dir="auto">
    全球最小的向量索引。用 LEANN 实现万物 RAG（检索增强生成）！
</h2>

LEANN 是一款创新的向量数据库，致力于让个人 AI 走向大众化。它将你的笔记本电脑转变为一个强大的 RAG 系统，能够索引并搜索数百万份文档，同时相比传统方案**节省 97% 的存储空间**，且**不损失任何精度**。

LEANN 通过 *基于图的 selective recomputation（选择性重计算）* 与 *高度数保持剪枝（high-degree preserving pruning）* 技术实现这一目标。它按需计算 embedding（嵌入向量），而非全部存储。 [图示 Fig →](#️-architecture--how-it-works) | [论文 →](https://arxiv.org/abs/2506.08276)

**准备好万物 RAG 了吗？** 将你的笔记本电脑转变为一个个人 AI 助手，它可以对你的 **[文件系统](#-personal-data-manager-process-any-documents-pdf-txt-md)**、**[邮件](#-your-personal-email-secretary-rag-on-apple-mail)**、**[浏览器历史](#-time-machine-for-the-web-rag-your-entire-browser-history)**、**[聊天记录](#-wechat-detective-unlock-your-golden-memories)**（[微信](#-wechat-detective-unlock-your-golden-memories)、[iMessage](#-imessage-history-your-personal-conversation-archive)）、**[Agent 记忆](#-chatgpt-chat-history-your-personal-ai-conversation-archive)**（[ChatGPT](#-chatgpt-chat-history-your-personal-ai-conversation-archive)、[Claude](#-claude-chat-history-your-personal-ai-conversation-archive)）、**[实时数据](#mcp-integration-rag-on-live-data-from-any-platform)**（[Slack](#slack-messages-search-your-team-conversations)、[Twitter](#-twitter-bookmarks-your-personal-tweet-library)）、**[代码库](#-claude-code-integration-transform-your-development-workflow)**\*，或外部知识库（即 6000 万份文档）进行语义搜索——全部在本地运行，零云端成本，完全隐私。

\* Claude Code 目前仅支持基础的 `grep` 风格关键词搜索。**LEANN** 是一个开箱即用的 **语义搜索 MCP 服务，与 Claude Code 完全兼容**，在不改变你工作流的前提下解锁智能检索能力。🔥 查看 [简易设置指南 →](packages/leann-mcp/README.md)

## 为什么选择 LEANN？

<p align="center">
  <img src="assets/effects.png" alt="LEANN vs Traditional Vector DB Storage Comparison" width="70%">
</p>

> **数据说明一切：** 仅需 6GB 即可索引 6000 万个文本分块，而传统方案需要 201GB。从邮件到浏览器历史，全部轻松容纳在你的笔记本中。[查看下方不同应用的详细基准测试 ↓](#-storage-comparison)

🔒 **隐私安全：** 你的数据永远不会离开本地电脑。无需 OpenAI，无需云端，没有“服务条款”的束缚。

🪶 **轻量高效：** 基于图的重计算技术消除了沉重的 embedding 存储负担，配合智能图剪枝与 CSR（压缩稀疏行）格式，将图的存储开销降至最低。始终更省空间、更少内存占用！

📦 **便携迁移：** 以极低成本在设备间（甚至与他人共享）转移你的整个知识库——你的个人 AI 记忆随行随走。

📈 **高可扩展性：** 轻松处理会让传统向量数据库崩溃的杂乱个人数据，从容管理不断增长的个人化数据和 Agent 生成的记忆！

✨ **零精度损失：** 在使用 97% 更少存储空间的同时，保持与重型方案同等质量的搜索效果。

## 安装指南

### 📦 前置条件：安装 uv

如果你还没有安装 [uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)，请先完成安装。通常你可以使用以下命令安装：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🚀 快速安装

克隆仓库以获取所有示例并体验精彩应用，

```bash
git clone https://github.com/yichuan-w/LEANN.git leann
cd leann
```

然后从 [PyPI](https://pypi.org/project/leann/) 安装 LEANN 即可立即运行：

```bash
uv venv
source .venv/bin/activate
uv pip install leann

# CPU-only (Linux): use the `cpu` extra (e.g. `leann[cpu]`)
```

<!--
> Low-resource? See "Low-resource setups" in the [Configuration Guide](docs/configuration-guide.md#low-resource-setups). -->

<details>
<summary>
<strong>🔧 从源码构建（推荐用于开发）</strong>
</summary>



```bash
git clone https://github.com/yichuan-w/LEANN.git leann
cd leann
git submodule update --init --recursive
```

**macOS:**

注意：DiskANN 需要 MacOS 13.3 或更高版本。

```bash
brew install libomp boost protobuf zeromq pkgconf
uv sync --extra diskann
```

**Linux (Ubuntu/Debian):**

注意：在 Ubuntu 20.04 上，你可能需要构建更新版本的 Abseil 并固定 Protobuf（例如 v3.20.x）以编译 DiskANN。请参阅 [Issue #30](https://github.com/yichuan-w/LEANN/issues/30) 获取逐步指南。

你可以手动安装 [Intel oneAPI MKL](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html) 来替代 `libmkl-full-dev` 用于 DiskANN。你也可以使用 `libopenblas-dev` 仅构建 HNSW，只需在下方命令中移除 `--extra diskann` 即可。

```bash
sudo apt-get update && sudo apt-get install -y \
  libomp-dev libboost-all-dev protobuf-compiler libzmq3-dev \
  pkg-config libabsl-dev libaio-dev libprotobuf-dev \
  libmkl-full-dev

uv sync --extra diskann
```

**Linux (Arch Linux):**

```bash
sudo pacman -Syu && sudo pacman -S --needed base-devel cmake pkgconf git gcc \
  boost boost-libs protobuf abseil-cpp libaio zeromq

# For MKL in DiskANN
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/paru-bin.git
cd paru-bin && makepkg -si
paru -S intel-oneapi-mkl intel-oneapi-compiler
source /opt/intel/oneapi/setvars.sh

uv sync --extra diskann
```

**Linux (RHEL / CentOS Stream / Oracle / Rocky / AlmaLinux):**

详见 [Issue #50](https://github.com/yichuan-w/LEANN/issues/50)。

```bash
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y libomp-devel boost-devel protobuf-compiler protobuf-devel \
  abseil-cpp-devel libaio-devel zeromq-devel pkgconf-pkg-config

# For MKL in DiskANN
sudo dnf install -y intel-oneapi-mkl intel-oneapi-mkl-devel \
  intel-oneapi-openmp || sudo dnf install -y intel-oneapi-compiler
source /opt/intel/oneapi/setvars.sh

uv sync --extra diskann
```

**Windows:**

需要 [Visual Studio 2022 Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)（包含 **C++ desktop development** 工作负载）以及 [vcpkg](https://github.com/microsoft/vcpkg)。

```powershell
# Install toolchain (if not already present)
choco install cmake swig pkgconfiglite nuget.commandline -y

# Install C++ dependencies via vcpkg
vcpkg install zeromq:x64-windows openblas:x64-windows lapack:x64-windows `
  boost-program-options:x64-windows protobuf:x64-windows

# Set environment variables (adjust VCPKG_ROOT to your vcpkg path)
$env:CMAKE_PREFIX_PATH = "$env:VCPKG_ROOT\installed\x64-windows"
$env:PKG_CONFIG_PATH = "$env:VCPKG_ROOT\installed\x64-windows\lib\pkgconfig"
$env:PKG_CONFIG_EXECUTABLE = "C:\ProgramData\chocolatey\bin\pkg-config.exe"
$env:OPENBLAS_LIB = "$env:VCPKG_ROOT\installed\x64-windows\lib\openblas.lib"
$env:PATH += ";$env:VCPKG_ROOT\installed\x64-windows\bin"
$env:PATH += ";$env:VCPKG_ROOT\installed\x64-windows\tools\protobuf"

uv sync --extra diskann
```

</details>


## 快速开始

我们的声明式 API 让 RAG（检索增强生成）像编写配置文件一样简单。

查看 [demo.ipynb](demo.ipynb) 或 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yichuan-w/LEANN/blob/main/demo.ipynb)

```python
from leann import LeannBuilder, LeannSearcher, LeannChat
from pathlib import Path
INDEX_PATH = str(Path("./").resolve() / "demo.leann")

# Build an index
builder = LeannBuilder(backend_name="hnsw")
builder.add_text("LEANN saves 97% storage compared to traditional vector databases.")
builder.add_text("Tung Tung Tung Sahur called—they need their banana‑crocodile hybrid back")
builder.build_index(INDEX_PATH)

# Search
searcher = LeannSearcher(INDEX_PATH)
results = searcher.search("fantastical AI-generated creatures", top_k=1)

# Chat with your data
chat = LeannChat(INDEX_PATH, llm_config={"type": "hf", "model": "Qwen/Qwen3-0.6B"})
response = chat.ask("How much storage does LEANN save?", top_k=1)
```

## 万物皆可 RAG！

LEANN 支持对多种数据源进行 RAG，包括文档（`.pdf`、`.txt`、`.md`）、Apple Mail、Google 搜索历史、微信、ChatGPT 对话、Claude 对话、iMessage 对话，以及**通过 MCP（模型上下文协议）服务器获取的任何平台的实时数据**——涵盖 Slack、Twitter 等。

### 生成模型设置

#### LLM 后端

LEANN 支持多种大语言模型提供商用于文本生成（HuggingFace、Ollama、Anthropic 及任意兼容 OpenAI API 的服务）。

<details>
<summary><strong>🔑 OpenAI API 设置（默认）</strong></summary>

将你的 OpenAI API Key 设置为环境变量：

```bash
export OPENAI_API_KEY="your-api-key-here"
```

使用 CLI 时请确保添加 `--llm openai` 参数。
你也可以通过 `--llm-model <model-name>` 参数指定模型名称。

</details>

<details>
<summary><strong>🛠️ 支持的 LLM & Embedding 提供商（基于 OpenAI 兼容性）</strong></summary>

得益于 OpenAI API 格式的广泛采用，LEANN 开箱即用兼容海量 LLM 和 embedding 服务提供商。只需设置 `OPENAI_BASE_URL` 和 `OPENAI_API_KEY` 环境变量即可连接到你偏好的服务。

```sh
export OPENAI_API_KEY="xxx"
export OPENAI_BASE_URL="http://localhost:1234/v1" # base url of the provider
```

在 CLI 界面中使用 OpenAI 兼容端点时：

若用于文本生成，请确保使用 `--llm openai` 参数并通过 `--llm-model <model-name>` 指定模型名称。

若用于 embedding，请使用 `--embedding-mode openai` 参数并通过 `--embedding-model <MODEL>` 指定模型名称。

-----


以下是常用提供商的 Base URL 列表供你快速上手：

### 🖥️ 本地推理引擎（推荐以保障完全隐私）

| Provider         | Sample Base URL             |
| ---------------- | --------------------------- |
| **Ollama** | `http://localhost:11434/v1` |
| **LM Studio** | `http://localhost:1234/v1`  |
| **vLLM** | `http://localhost:8000/v1`  |
| **llama.cpp** | `http://localhost:8080/v1`  |
| **SGLang** | `http://localhost:30000/v1` |
| **LiteLLM** | `http://localhost:4000`     |

-----

### ☁️ 云端提供商

> **🚨 隐私提示：** 在选择云端提供商前，请仔细审查其隐私与数据保留政策。根据其条款，你的数据可能被用于其自身目的（包括但不限于人工审核和模型训练），若处理不当可能导致严重后果。


| Provider         | Base URL                                                   |
| ---------------- | ---------------------------------------------------------- |
| **OpenAI** | `https://api.openai.com/v1`                                |
| **OpenRouter** | `https://openrouter.ai/api/v1`                             |
| **Gemini** | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| **x.AI (Grok)** | `https://api.x.ai/v1`                                      |
| **Groq AI** | `https://api.groq.com/openai/v1`                           |
| **DeepSeek** | `https://api.deepseek.com/v1`                              |
| **SiliconFlow** | `https://api.siliconflow.cn/v1`                            |
| **Zhipu (BigModel)** | `https://open.bigmodel.cn/api/paas/v4/`                |
| **Mistral AI** | `https://api.mistral.ai/v1`                                |
| **Anthropic** | `https://api.anthropic.com/v1`                             |
| **Jina AI** (Embeddings) | `https://api.jina.ai/v1`                         |

> **💡 提示：分离 Embedding 提供商**
>
> 若希望 embedding 使用另一家提供商（例如 Jina AI），而 LLM 使用其他服务，请使用 `--embedding-api-base` 和 `--embedding-api-key`：
> ```bash
> leann build my-index --docs ./docs \
>   --embedding-mode openai \
>   --embedding-model jina-embeddings-v3 \
>   --embedding-api-base https://api.jina.ai/v1 \
>   --embedding-api-key $JINA_API_KEY
> ```

如果你的提供商不在此列表中，别担心！查看其文档寻找 OpenAI 兼容端点——很可能它也是兼容的！

</details>

<details>
<summary><strong>🔧 Ollama 设置（推荐以保障完全隐私）</strong></summary>

**macOS:**

首先，[下载 macOS 版 Ollama](https://ollama.com/download/mac)。

```bash
# Pull a lightweight model (recommended for consumer hardware)
ollama pull llama3.2:1b
```

**Linux:**

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service manually
ollama serve &

# Pull a lightweight model (recommended for consumer hardware)
ollama pull llama3.2:1b
```

</details>


## ⭐ 灵活配置

LEANN 提供灵活的参数，涵盖 embedding 模型、搜索策略与数据处理，以满足你的特定需求。

📚 **需要配置最佳实践？** 查看我们的 [Configuration Guide](docs/configuration-guide.md) 获取详细的优化建议、模型选择指南，以及解决慢速 embedding 或低质量检索等常见问题的方案。

<details>
<summary><strong>📋 点击展开：通用参数（适用于所有示例）</strong></summary>

所有 RAG 示例共享以下通用参数。**交互模式**在所有示例中均可用——只需不传 `--query` 即可启动连续问答会话，你可以提出多个问题。输入 'quit' 退出。

```bash
# Environment Variables (GPU Device Selection)
LEANN_EMBEDDING_DEVICE       # GPU for embedding model (e.g., cuda:0, cuda:1, cpu)
LEANN_LLM_DEVICE             # GPU for HFChat LLM (e.g., cuda:1, or "cuda" for multi-GPU auto)

# Core Parameters (General preprocessing for all examples)
--index-dir DIR              # Directory to store the index (default: current directory)
--query "YOUR QUESTION"      # Single query mode. Omit for interactive chat (type 'quit' to exit), and now you can play with your index interactively
--max-items N                # Limit data preprocessing (default: -1, process all data)
--force-rebuild              # Force rebuild index even if it exists

# Embedding Parameters
--embedding-model MODEL      # e.g., facebook/contriever, text-embedding-3-small, mlx-community/Qwen3-Embedding-0.6B-8bit or nomic-embed-text
--embedding-mode MODE        # sentence-transformers, openai, mlx, or ollama

# LLM Parameters (Text generation models)
--llm TYPE                   # LLM backend: openai, ollama, hf, or anthropic (default: openai)
--llm-model MODEL            # Model name (default: gpt-4o) e.g., gpt-4o-mini, llama3.2:1b, Qwen/Qwen2.5-1.5B-Instruct
--thinking-budget LEVEL      # Thinking budget for reasoning models: low/medium/high (supported by o3, o3-mini, GPT-Oss:20b, and other reasoning models)

# Search Parameters
--top-k N                    # Number of results to retrieve (default: 20)
--search-complexity N        # Search complexity for graph traversal (default: 32)

# Chunking Parameters
--chunk-size N               # Size of text chunks (default varies by source: 256 for most, 192 for WeChat)
--chunk-overlap N            # Overlap between chunks (default varies: 25-128 depending on source)

# Index Building Parameters
--backend-name NAME          # Backend to use: hnsw or diskann (default: hnsw)
--graph-degree N             # Graph degree for index construction (default: 32)
--build-complexity N         # Build complexity for index construction (default: 64)
--compact / --no-compact     # Use compact storage (default: true). Must be `no-compact` for `no-recompute` build.
--recompute / --no-recompute # Enable/disable embedding recomputation (default: enabled). Should not do a `no-recompute` search in a `recompute` build.
```

</details>

### 📄 个人数据管理器：处理任意文档（`.pdf`, `.txt`, `.md`)！

直接针对你的个人 PDF、文档及包含文件的目录提问！

<p align="center">
  <img src="videos/paper_clear.gif" alt="LEANN Document Search Demo" width="600">
</p>

以下示例询问关于总结我们论文的问题（使用 `data/` 中的默认数据，该目录包含多样化数据源：两篇论文、《傲慢与偏见》以及一份华为的 LLM 中文技术报告），这是此处**最容易运行的示例**：

```bash
source .venv/bin/activate # Don't forget to activate the virtual environment
python -m apps.document_rag --query "What are the main techniques LEANN explores?"
```

<details>
<summary><strong>📋 点击展开：文档专用参数</strong></summary>

#### Parameters
```bash
--data-dir DIR           # Directory containing documents to process (default: data)
--file-types .ext .ext   # Filter by specific file types (optional - all LlamaIndex supported types if omitted)
```

#### Example Commands
```bash
# Process all documents with larger chunks for academic papers
python -m apps.document_rag --data-dir "~/Documents/Papers" --chunk-size 1024

# Filter only markdown and Python files with smaller chunks
python -m apps.document_rag --data-dir "./docs" --chunk-size 256 --file-types .md .py

# Enable AST-aware chunking for code files
python -m apps.document_rag --enable-code-chunking --data-dir "./my_project"

# Or use the specialized code RAG for better code understanding
python -m apps.code_rag --repo-dir "./my_codebase" --query "How does authentication work?"
```

</details>

### 🎨 ColQwen：基于视觉语言模型的多模态 PDF 检索

使用 ColQwen2/ColPali 模型，通过文本与视觉理解双重能力搜索 PDF。非常适合研究论文、技术文档以及任何包含复杂排版、图表或示意图的 PDF。

> **🍎 Mac 用户：** ColQwen 针对 Apple Silicon 进行了优化，支持 MPS 加速以实现更快的推理！

```bash
# Build index from PDFs
python -m apps.colqwen_rag build --pdfs ./my_papers/ --index research_papers

# Search with text queries
python -m apps.colqwen_rag search research_papers "How does attention mechanism work?"

# Interactive Q&A
python -m apps.colqwen_rag ask research_papers --interactive
```

<details>
<summary><strong>📋 点击展开：ColQwen 设置与使用</strong></summary>

#### Prerequisites
```bash
# Install dependencies
uv pip install colpali_engine pdf2image pillow matplotlib qwen_vl_utils einops seaborn
brew install poppler  # macOS only, for PDF processing
```

#### Build Index
```bash
python -m apps.colqwen_rag build \
  --pdfs ./pdf_directory/ \
  --index my_index \
  --model colqwen2  # or colpali
```

#### Search
```bash
python -m apps.colqwen_rag search my_index "your question here" --top-k 5
```

#### Models
- **ColQwen2** (`colqwen2`): 最新视觉语言模型，性能更优
- **ColPali** (`colpali`): 经过验证的多模态检索器

详细用法请参阅 [ColQwen Guide](docs/COLQWEN_GUIDE.md)。

</details>

### 📧 你的个人邮件秘书：对 Apple Mail 进行 RAG！

> **注意：** 以下示例目前仅支持 macOS。Windows 支持即将推出。


<p align="center">
  <img src="videos/mail_clear.gif" alt="LEANN Email Search Demo" width="600">
</p>

在运行以下示例前，你需要在系统偏好设置 → 隐私与安全性 → 完全磁盘访问权限中，为你的终端/VS Code 授予完全磁盘访问权限。

```bash
python -m apps.email_rag --query "What's the food I ordered by DoorDash or Uber Eats mostly?"
```
**780K 邮件分块 → 78MB 存储空间。** 终于像搜索 Google 一样搜索你的邮件了。

<details>
<summary><strong>📋 点击展开：邮件专用参数</strong></summary>

#### Parameters
```bash
--mail-path PATH         # Path to specific mail directory (auto-detects if omitted)
--include-html          # Include HTML content in processing (useful for newsletters)
```

#### Example Commands
```bash
# Search work emails from a specific account
python -m apps.email_rag --mail-path "~/Library/Mail/V10/WORK_ACCOUNT"

# Find all receipts and order confirmations (includes HTML)
python -m apps.email_rag --query "receipt order confirmation invoice" --include-html
```

</details>

<details>
<summary><strong>📋 点击展开：可尝试的示例查询</strong></summary>

索引构建完成后，你可以提问如：
- “找出我老板关于截止日期的邮件”
- “John 对项目时间线说了什么？”
- “显示与我差旅费用相关的邮件”
</details>

### 🔍 网页时光机：RAG 你的整个 Chrome 浏览器历史！

<p align="center">
  <img src="videos/google_clear.gif" alt="LEANN Browser History Search Demo" width="600">
</p>

```bash
python -m apps.browser_rag --query "Tell me my browser history about machine learning?"
```
**38K 浏览器记录 → 6MB 存储空间。** 你的浏览历史就是你的个人搜索引擎。

<details>
<summary><strong>📋 点击展开：浏览器专用参数</strong></summary>

#### Parameters
```bash
--chrome-profile PATH    # Path to Chrome profile directory (auto-detects if omitted)
```

#### Example Commands
```bash
# Search academic research from your browsing history
python -m apps.browser_rag --query "arxiv papers machine learning transformer architecture"

# Track competitor analysis across work profile
python -m apps.browser_rag --chrome-profile "~/Library/Application Support/Google/Chrome/Work Profile" --max-items 5000
```

</details>

<details>
<summary><strong>📋 点击展开：如何查找你的 Chrome 配置文件</strong></summary>

默认 Chrome 配置文件路径针对典型 macOS 设置配置。如需查找你特定的 Chrome 配置文件：

1. 打开终端
2. 运行：`ls ~/Library/Application\ Support/Google/Chrome/`
3. 寻找类似 "Default"、"Profile 1"、"Profile 2" 等文件夹
4. 使用完整路径作为 `--chrome-profile` 参数

**常见 Chrome 配置文件位置：**
- macOS: `~/Library/Application Support/Google/Chrome/Default`
- Linux: `~/.config/google-chrome/Default`

</details>

<details>
<summary><strong>💬 点击展开：可尝试的示例查询</strong></summary>

索引构建完成后，你可以提问如：

- “我浏览过哪些关于机器学习的网站？”
- “找出我关于编程的搜索历史”
- “我最近看了哪些 YouTube 视频？”
- “显示我去过的与旅行规划相关的网站”

</details>

### 💬 微信侦探：解锁你的黄金记忆！

<p align="center">
  <img src="videos/wechat_clear.gif" alt="LEANN WeChat Search Demo" width="600">
</p>

```bash
python -m apps.wechat_rag --query "Show me all group chats about weekend plans"
```
**400K 条消息 → 64MB 存储空间** 用任意语言搜索多年的聊天记录。


<details>
<summary><strong>🔧 点击展开：安装要求</strong></summary>

首先，你需要安装 [WeChat exporter](https://github.com/sunnyyoung/WeChatTweak-CLI)，

```bash
brew install sunnyyoung/repo/wechattweak-cli
```

或手动安装（如果 Homebrew 有问题）：

```bash
sudo packages/wechat-exporter/wechattweak-cli install
```

**故障排除：**
- **安装问题**：查看 [WeChatTweak-CLI Issues 页面](https://github.com/sunnyyoung/WeChatTweak-CLI/issues/41)
- **导出错误**：如果遇到以下错误，请尝试重启微信
  ```bash
  Failed to export WeChat data. Please ensure WeChat is running and WeChatTweak is installed.
  Failed to find or export WeChat data. Exiting.
  ```
</details>

<details>
<summary><strong>📋 点击展开：微信专用参数</strong></summary>

#### Parameters
```bash
--export-dir DIR         # Directory to store exported WeChat data (default: wechat_export_direct)
--force-export          # Force re-export even if data exists
```

#### Example Commands
```bash
# Search for travel plans discussed in group chats
python -m apps.wechat_rag --query "travel plans" --max-items 10000

# Re-export and search recent chats (useful after new messages)
python -m apps.wechat_rag --force-export --query "work schedule"
```

</details>

<details>
<summary><strong>💬 点击展开：可尝试的示例查询</strong></summary>

索引构建完成后，你可以提问如：

- “我想买魔术师约翰逊的球衣，给我一些对应聊天记录?” (Chinese: Show me chat records about buying Magic Johnson's jersey)

</details>

### 🤖 ChatGPT 对话历史：你的个人 AI 对话档案！

将你的 ChatGPT 对话转变为可搜索的知识库！搜索所有关于编程、研究、头脑风暴等的 ChatGPT 讨论。

```bash
python -m apps.chatgpt_rag --export-path chatgpt_export.html --query "How do I create a list in Python?"
```

**解锁你的 AI 对话历史。** 再也不必丢失有价值的 ChatGPT 讨论见解。

<details>
<summary><strong>📋 点击展开：如何导出 ChatGPT 数据</strong></summary>

**逐步导出流程：**

1. **登录 ChatGPT**
2. **点击右上角个人头像图标**
3. **导航至 Settings → Data Controls**
4. **在 Export Data 下点击 "Export"**
5. **确认导出请求**
6. **通过邮件链接下载 ZIP 文件（有效期24小时）**
7. **解压或直接使用 LEANN 处理**

**支持的格式：**
- ChatGPT 导出的 `.html` 文件
- ChatGPT 的 `.zip` 压缩包
- 包含多个导出文件的目录

</details>

<details>
<summary><strong>📋 点击展开：ChatGPT 专用参数</strong></summary>

#### Parameters
```bash
--export-path PATH           # Path to ChatGPT export file (.html/.zip) or directory (default: ./chatgpt_export)
--separate-messages         # Process each message separately instead of concatenated conversations
--chunk-size N              # Text chunk size (default: 512)
--chunk-overlap N           # Overlap between chunks (default: 128)
```

#### Example Commands
```bash
# Basic usage with HTML export
python -m apps.chatgpt_rag --export-path conversations.html

# Process ZIP archive from ChatGPT
python -m apps.chatgpt_rag --export-path chatgpt_export.zip

# Search with specific query
python -m apps.chatgpt_rag --export-path chatgpt_data.html --query "Python programming help"

# Process individual messages for fine-grained search
python -m apps.chatgpt_rag --separate-messages --export-path chatgpt_export.html

# Process directory containing multiple exports
python -m apps.chatgpt_rag --export-path ./chatgpt_exports/ --max-items 1000
```

</details>

<details>
<summary><strong>💡 点击展开：可尝试的示例查询</strong></summary>

索引你的 ChatGPT 对话后，你可以使用以下查询进行搜索：
- “我让 ChatGPT 帮我解决过哪些 Python 编程问题？”
- “显示关于机器学习算法的对话”
- “找出关于 Web 开发框架的讨论”
- “ChatGPT 给过我什么编码建议？”
- “搜索关于调试技术的对话”
- “查找 ChatGPT 推荐的学习资源”

</details>

### 🤖 Claude 对话历史：你的个人 AI 对话档案！

将你的 Claude 对话转变为可搜索的知识库！搜索所有关于编程、研究、头脑风暴等的 Claude 讨论。

```bash
python -m apps.claude_rag --export-path claude_export.json --query "What did I ask about Python dictionaries?"
```

**解锁你的 AI 对话历史。** 再也不必丢失有价值的 Claude 讨论见解。

<details>
<summary><strong>📋 点击展开：如何导出 Claude 数据</strong></summary>

**逐步导出流程：**

1. **在浏览器中打开 Claude**
2. **导航至 Settings（寻找齿轮图标或设置菜单）**
3. **在账户设置中找到 Export/Download 选项**
4. **下载对话数据（通常为 JSON 格式）**
5. **将文件放置在你的项目目录中**

*注意：Claude 导出方法可能因你使用的界面而异。请查阅 Claude 帮助文档获取最新导出说明。*

**支持的格式：**
- `.json` 文件（推荐）
- 包含 JSON 数据的 `.zip` 压缩包
- 包含多个导出文件的目录

</details>

<details>
<summary><strong>📋 点击展开：Claude 专用参数</strong></summary>

#### Parameters
```bash
--export-path PATH           # Path to Claude export file (.json/.zip) or directory (default: ./claude_export)
--separate-messages         # Process each message separately instead of concatenated conversations
--chunk-size N              # Text chunk size (default: 512)
--chunk-overlap N           # Overlap between chunks (default: 128)
```

#### Example Commands
```bash
# Basic usage with JSON export
python -m apps.claude_rag --export-path my_claude_conversations.json

# Process ZIP archive from Claude
python -m apps.claude_rag --export-path claude_export.zip

# Search with specific query
python -m apps.claude_rag --export-path claude_data.json --query "machine learning advice"

# Process individual messages for fine-grained search
python -m apps.claude_rag --separate-messages --export-path claude_export.json

# Process directory containing multiple exports
python -m apps.claude_rag --export-path ./claude_exports/ --max-items 1000
```

</details>

<details>
<summary><strong>💡 点击展开：可尝试的示例查询</strong></summary>

索引你的 Claude 对话后，你可以使用以下查询进行搜索：
- “我让 Claude 帮我解决过哪些 Python 编程问题？”
- “显示关于机器学习算法的对话”
- “找出关于软件架构模式的讨论”
- “Claude 给过我什么调试建议？”
- “搜索关于数据结构的话题”
- “查找 Claude 推荐的学习资源”

</details>

### 💬 iMessage 历史：你的个人对话档案！

将你的 iMessage 对话转变为可搜索的知识库！搜索所有短信、群聊以及与朋友、家人和同事的对话。

```bash
python -m apps.imessage_rag --query "What did we discuss about the weekend plans?"
```

**解锁你的消息历史。** 再也不必丢失重要的对话、共享链接或来自 iMessage 历史的难忘时刻。

<details>
<summary><strong>📋 点击展开：如何访问 iMessage 数据</strong></summary>

**iMessage 数据存储位置：**

iMessage 对话存储在你 Mac 上的 SQLite 数据库中，路径为：
```
~/Library/Messages/chat.db
```

**重要设置要求：**

1. **授予完全磁盘访问权限** 给你的终端或 IDE：
   - 打开 **系统偏好设置 → 安全性与隐私 → 隐私**
   - 左侧栏选择 **完全磁盘访问权限**
   - 点击 **+** 按钮并添加你的终端应用（Terminal, iTerm2）或 IDE（VS Code 等）
   - 授予权限后重启终端/IDE

2. **替代方案：使用备份数据库**
   - 如果你有 Time Machine 备份或手动复制的数据库副本
   - 使用 `--db-path` 指定自定义路径

**支持的格式：**
- 直接访问 `~/Library/Messages/chat.db`（默认）
- 通过 `--db-path` 指定自定义路径
- 支持数据库备份副本

</details>

<details>
<summary><strong>📋 点击展开：iMessage 专用参数</strong></summary>

#### Parameters
```bash
--db-path PATH                    # Path to chat.db file (default: ~/Library/Messages/chat.db)
--concatenate-conversations       # Group messages by conversation (default: True)
--no-concatenate-conversations    # Process each message individually
--chunk-size N                    # Text chunk size (default: 1000)
--chunk-overlap N                 # Overlap between chunks (default: 200)
```

#### Example Commands
```bash
# Basic usage (requires Full Disk Access)
python -m apps.imessage_rag

# Search with specific query
python -m apps.imessage_rag --query "family dinner plans"

# Use custom database path
python -m apps.imessage_rag --db-path /path/to/backup/chat.db

# Process individual messages instead of conversations
python -m apps.imessage_rag --no-concatenate-conversations

# Limit processing for testing
python -m apps.imessage_rag --max-items 100 --query "weekend"
```

</details>

<details>
<summary><strong>💡 点击展开：可尝试的示例查询</strong></summary>

索引你的 iMessage 对话后，你可以使用以下查询进行搜索：
- “我们讨论过哪些度假计划？”
- “找出关于餐厅推荐的消息”
- “显示我与 John 关于项目的对话”
- “搜索共享的技术类链接”
- “找出群聊中关于周末活动的讨论”
- “妈妈说过什么关于家庭聚会的事？”

</details>

### MCP 集成：对任何平台的实时数据进行 RAG

通过模型上下文协议（MCP）连接实时数据源。LEANN 现在支持通过标准化的 MCP 服务器，对 Slack、Twitter 等平台进行实时 RAG。

**核心优势：**
- **实时数据访问**：无需手动导出即可获取实时数据
- **标准化协议**：使用任意兼容 MCP 的服务器
- **易于扩展**：仅需少量代码即可添加新平台
- **安全访问**：MCP 服务器负责处理身份验证

#### 💬 Slack 消息：搜索你的团队对话

将你的 Slack 工作区转变为可搜索的知识库！在所有频道中查找讨论、决策与共享知识。

```bash
# Test MCP server connection
python -m apps.slack_rag --mcp-server "slack-mcp-server" --test-connection

# Index and search Slack messages
python -m apps.slack_rag \
  --mcp-server "slack-mcp-server" \
  --workspace-name "my-team" \
  --channels general dev-team random \
  --query "What did we decide about the product launch?"
```

**📖 完整设置指南：** 详细设置说明、常见故障排除（如“users cache is not ready yet”）及高级配置选项，请参阅我们的 [**Slack Setup Guide**](docs/slack-setup-guide.md)。

**快速设置：**
1. 安装 Slack MCP 服务器（例如 `npm install -g slack-mcp-server`）
2. 创建 Slack App 并获取 API 凭证（详见上方指南）
3. 设置环境变量：
   ```bash
   export SLACK_BOT_TOKEN="xoxb-your-bot-token"
   export SLACK_APP_TOKEN="xapp-your-app-token"  # Optional
   ```
4. 使用 `--test-connection` 参数测试连接

**参数：**
- `--mcp-server`: 启动 Slack MCP 服务器的命令
- `--workspace-name`: Slack 工作区名称用于组织分类
- `--channels`: 指定要索引的频道（可选）
- `--concatenate-conversations`: 按频道分组消息（默认: true）
- `--max-messages-per-channel`: 限制每频道的消息数（默认: 100）
- `--max-retries`: 缓存同步问题的最大重试次数（默认: 5）
- `--retry-delay`: 重试之间的初始延迟秒数（默认: 2.0）

#### 🐦 Twitter Bookmarks：你的个人推文库

搜索你的 Twitter Bookmarks！找回你保存以备日后阅读的完美文章、Thread 或见解。

```bash
# Test MCP server connection
python -m apps.twitter_rag --mcp-server "twitter-mcp-server" --test-connection

# Index and search Twitter bookmarks
python -m apps.twitter_rag \
  --mcp-server "twitter-mcp-server" \
  --max-bookmarks 1000 \
  --query "What AI articles did I bookmark about machine learning?"
```

**设置要求：**
1. 安装 Twitter MCP 服务器（例如 `npm install -g twitter-mcp-server`）
2. 获取 Twitter API 凭证：
   - 在 [developer.twitter.com](https://developer.twitter.com) 申请 Twitter Developer Account
   - 在 Twitter Developer Portal 创建新 App
   - 生成具有“读取”权限的 API Keys 和 Access Tokens
   - 如需访问 Bookmarks，可能需要 Twitter API v2 及相应作用域
   ```bash
   export TWITTER_API_KEY="your-api-key"
   export TWITTER_API_SECRET="your-api-secret"
   export TWITTER_ACCESS_TOKEN="your-access-token"
   export TWITTER_ACCESS_TOKEN_SECRET="your-access-token-secret"
   ```
3. 使用 `--test-connection` 参数测试连接

**参数：**
- `--mcp-server`: 启动 Twitter MCP 服务器的命令
- `--username`: 按用户名过滤 Bookmarks（可选）
- `--max-bookmarks`: 获取的最大 Bookmarks 数量（默认: 1000）
- `--no-tweet-content`: 排除推文内容，仅保留元数据
- `--no-metadata`: 排除互动元数据

</details>

<details>
<summary><strong>💡 点击展开：可尝试的示例查询</strong></summary>

**Slack 查询：**
- “团队讨论过哪些关于项目截止日期的内容？”
- “找出关于新功能发布的消息”
- “显示关于预算规划的对话”
- “dev-team 频道中做出了什么决策？”

**Twitter 查询：**
- “我上个月 Bookmark 了哪些 AI 文章？”
- “找出关于机器学习技术的推文”
- “显示我保存的关于创业建议的 Thread”
- “我保存过哪些 Python 教程？”

</details>
<summary><strong>🔧 在 CLI 命令中使用 MCP</strong></summary>

**想将 MCP 数据与常规 LEANN CLI 结合使用？** 你可以将 MCP 应用与 CLI 命令组合：

```bash
# Step 1: Use MCP app to fetch and index data
python -m apps.slack_rag --mcp-server "slack-mcp-server" --workspace-name "my-team"

# Step 2: The data is now indexed and available via CLI
leann search slack_messages "project deadline"
leann ask slack_messages "What decisions were made about the product launch?"

# Same for Twitter bookmarks
python -m apps.twitter_rag --mcp-server "twitter-mcp-server"
leann search twitter_bookmarks "machine learning articles"
```

**MCP vs 手动导出：**
- **MCP**: 实时数据，自动更新，需要服务器设置
- **手动导出**: 一次性设置，支持离线使用，需手动导出数据

</details>

<details>
<summary><strong>🔧 添加新的 MCP 平台</strong></summary>

想添加对其他平台的支持？LEANN 的 MCP 集成设计为易于扩展：

1. **查找或创建** 你平台的 MCP 服务器
2. **创建 Reader 类**，遵循 `apps/slack_data/slack_mcp_reader.py` 的模式
3. **创建 RAG 应用**，遵循 `apps/slack_rag.py` 的模式
4. **测试并贡献** 回社区！

**值得探索的热门 MCP 服务器：**
- GitHub 仓库与 Issues
- Discord 消息
- Notion 页面
- Google Drive 文档
- MCP 生态中的更多平台！

</details>

### 🚀 Claude Code 集成：重塑你的开发工作流！

<details>
<summary><strong>AST‑Aware 代码分块</strong></summary>

LEANN 具备智能的代码分块功能，可保留 Python、Java、C# 和 TypeScript 的语义边界（函数、类、方法），相比基于文本的分块能显著提升代码理解能力。

📖 阅读 [AST Chunking Guide →](docs/ast_chunking_guide.md)

</details>

**代码辅助的未来已来。** 通过 LEANN 对 Claude Code 的原生 MCP 集成，重塑你的开发工作流。索引整个代码库并在 IDE 中直接获取智能代码辅助。

**核心特性：**
- 🔍 **语义代码搜索**：覆盖整个项目，完全本地索引且轻量级
- 🧠 **AST 感知分块**：保留代码结构（函数、类）
- 📚 **上下文感知辅助**：助力调试与开发
- 🚀 **零配置设置**：自动检测编程语言

```bash
# Install LEANN globally for MCP integration
uv tool install leann-core --with leann
claude mcp add --scope user leann-server -- leann_mcp
# Setup is automatic - just start using Claude Code!
```
尝试我们完全自主的 Agentic Pipeline，支持自动查询重写、语义搜索规划等功能：

![LEANN MCP Integration](assets/mcp_leann.png)

**🔥 准备好为你的编码能力超频了吗？** [完整设置指南 →](packages/leann-mcp/README.md)

## 命令行界面 (CLI)

LEANN 包含强大的 CLI，用于文档处理与搜索。非常适合快速文档索引与交互式对话。

### 安装

如果你已按照“快速开始”操作，`leann` 已在你的虚拟环境中安装：
```bash
source .venv/bin/activate
leann --help
```

**若要使其全局可用：**
```bash
# Install the LEANN CLI globally using uv tool
uv tool install leann-core --with leann


# Now you can use leann from anywhere without activating venv
leann --help
```

> **注意**：Claude Code 集成需要全局安装。`leann_mcp` 服务器依赖于全局可用的 `leann` 命令。



### 使用示例

```bash
# build from a specific directory, and my_docs is the index name(Here you can also build from multiple dict or multiple files)
leann build my-docs --docs ./your_documents

# Search your documents
leann search my-docs "machine learning concepts"

# Interactive chat with your documents
leann ask my-docs --interactive

# Ask a single question (non-interactive)
leann ask my-docs "Where are prompts configured?"

# Detect file changes since last build/watch checkpoint
leann watch my-docs

# List all your indexes
leann list

# Remove an index
leann remove my-docs
```

**核心 CLI 特性：**
- 自动检测文档格式（PDF, TXT, MD, DOCX, PPTX + 代码文件）
- **🧠 AST 感知分块**：适用于 Python、Java、C#, TypeScript 文件
- 智能文本分块与重叠处理，适用于其他所有内容
- **📂 基于 Merkle 树快照的文件变更检测**（`leann watch`）
- 多 LLM 提供商支持（Ollama, OpenAI, HuggingFace）
- 索引存储于 `.leann/indexes/`（项目本地路径）
- 支持高级搜索参数

<details>
<summary><strong>📋 点击展开：完整 CLI 参考</strong></summary>

你可以通过 `leann --help`，或 `leann build --help`、`leann search --help`、`leann watch --help`、`leann ask --help`、`leann list --help`、`leann remove --help` 获取完整 CLI 参考。

**Build Command:**
```bash
leann build INDEX_NAME --docs DIRECTORY|FILE [DIRECTORY|FILE ...] [OPTIONS]

Options:
  --backend {hnsw,diskann}     Backend to use (default: hnsw)
  --embedding-model MODEL      Embedding model (default: facebook/contriever)
  --graph-degree N             Graph degree (default: 32)
  --complexity N               Build complexity (default: 64)
  --force                      Force rebuild existing index
  --compact / --no-compact     Use compact storage (default: true). Must be `no-compact` for `no-recompute` build.
  --recompute / --no-recompute Enable recomputation (default: true)
```

**Search Command:**
```bash
leann search INDEX_NAME QUERY [OPTIONS]

Options:
  --top-k N                     Number of results (default: 5)
  --complexity N                Search complexity (default: 64)
  --recompute / --no-recompute  Enable/disable embedding recomputation (default: enabled). Should not do a `no-recompute` search in a `recompute` build.
  --pruning-strategy {global,local,proportional}
```

**Watch Command:**
```bash
leann watch INDEX_NAME

# Compares the current file system state against the last checkpoint (Merkle tree snapshot)
# and reports which files have been added, removed, or modified, along with their chunk IDs.
#
# - Automatically saves a new checkpoint after detecting changes
# - Each subsequent run compares against the most recent checkpoint
# - File change detection uses SHA-256 content hashing via a Merkle tree
#
# Example output:
#   === Changes since last checkpoint ===
#   modified (1):
#     - /path/to/file.py
#       chunks: 42, 43, 44
```

**Ask Command:**
```bash
leann ask INDEX_NAME [OPTIONS]

Options:
  --llm {ollama,openai,hf,anthropic}    LLM provider (default: ollama)
  --model MODEL                         Model name (default: qwen3:8b)
  --interactive                         Interactive chat mode
  --top-k N                             Retrieval count (default: 20)
```

**List Command:**
```bash
leann list

# Lists all indexes across all projects with status indicators:
# ✅ - Index is complete and ready to use
# ❌ - Index is incomplete or corrupted
# 📁 - CLI-created index (in .leann/indexes/)
# 📄 - App-created index (*.leann.meta.json files)
```

**Remove Command:**
```bash
leann remove INDEX_NAME [OPTIONS]

Options:
  --force, -f    Force removal without confirmation

# Smart removal: automatically finds and safely removes indexes
# - Shows all matching indexes across projects
# - Requires confirmation for cross-project removal
# - Interactive selection when multiple matches found
# - Supports both CLI and app-created indexes
```

</details>

## 🚀 高级功能

### 🎯 元数据过滤 (Metadata Filtering)

LEANN 支持简单的元数据过滤系统，以实现更复杂的用例，如按日期/类型过滤文档、按文件扩展名搜索代码，以及基于自定义标准的内容管理。

```python
# Add metadata during indexing
builder.add_text(
    "def authenticate_user(token): ...",
    metadata={"file_extension": ".py", "lines_of_code": 25}
)

# Search with filters
results = searcher.search(
    query="authentication function",
    metadata_filters={
        "file_extension": {"==": ".py"},
        "lines_of_code": {"<": 100}
    }
)
```

**支持的运算符**: `==`, `!=`, `<`, `<=`, `>`, `>=`, `in`, `not_in`, `contains`, `starts_with`, `ends_with`, `is_true`, `is_false`

📖 **[完整元数据过滤指南 →](docs/metadata_filtering.md)**

### 🔍 Grep 搜索 (Grep Search)

若需要精确文本匹配而非语义搜索，请使用 `use_grep` 参数：

```python
# Exact text search
results = searcher.search("banana‑crocodile", use_grep=True, top_k=1)
```

**适用场景**：查找特定代码模式、错误消息、函数名或需要精确匹配的短语（无需语义相似度）。

📖 **[完整 Grep 搜索指南 →](docs/grep_search.md)**

## 🏗️ 架构与工作原理 (Architecture & How It Works)

<p align="center">
  <img src="assets/arch.png" alt="LEANN Architecture" width="800">
</p>

**核心魔法：** 大多数向量数据库存储每一个 embedding（成本高）。LEANN 仅存储剪枝后的图结构（成本低），并在需要时快速重新计算 embedding。

**核心技术：**
- **基于图的 selective recomputation（选择性重计算）**：仅对搜索路径上的节点计算 embedding
- **High-degree preserving pruning（高度数保持剪枝）**：保留重要的“枢纽”节点，移除冗余连接
- **Dynamic batching（动态批处理）**：高效批量计算 embedding 以充分利用 GPU
- **Two-level search（两级搜索）**：智能图遍历，优先探索潜力节点

**后端支持：**
- **HNSW**（默认）：适用于大多数数据集，通过完全重计算实现最大存储节省
- **DiskANN**：高级选项，提供卓越的搜索性能，使用基于 PQ 的图遍历与实时重排序，在速度与精度间取得最佳平衡

## 基准测试 (Benchmarks)

**[DiskANN vs HNSW 性能对比 →](benchmarks/diskann_vs_hnsw_speed_comparison.py)** - 比较两种后端的搜索性能

**[简单示例：LEANN vs FAISS 对比 →](benchmarks/compare_faiss_vs_leann.py)** - 直观展示存储节省效果

### 📊 存储空间对比 (Storage Comparison)

| System | DPR (2.1M) | Wiki (60M) | Chat (400K) | Email (780K) | Browser (38K) |
|--------|-------------|------------|-------------|--------------|---------------|
| Traditional vector database (e.g., FAISS) | 3.8 GB      | 201 GB     | 1.8 GB     | 2.4 GB      | 130 MB        |
| LEANN  | 324 MB      | 6 GB       | 64 MB       | 79 MB       | 6.4 MB        |
| Savings| 91%         | 97%        | 97%         | 97%         | 95%           |



## 复现我们的结果 (Reproduce Our Results)

```bash
uv run benchmarks/run_evaluation.py    # Will auto-download evaluation data and run benchmarks
uv run benchmarks/run_evaluation.py benchmarks/data/indices/rpj_wiki/rpj_wiki --num-queries 2000    # After downloading data, you can run the benchmark with our biggest index
```

评估脚本会在首次运行时自动下载数据。最后三项结果使用部分个人数据进行测试，你可以用自己的数据复现它们！

## 🔬 论文 (Paper)

如果你认为 Leann 有用，请引用：

**[LEANN: A Low-Storage Vector Index](https://arxiv.org/abs/2506.08276)**

```bibtex
@misc{wang2025leannlowstoragevectorindex,
      title={LEANN: A Low-Storage Vector Index},
      author={Yichuan Wang and Shu Liu and Zhifei Li and Yongji Wu and Ziming Mao and Yilong Zhao and Xiao Yan and Zhiying Xu and Yang Zhou and Ion Stoica and Sewon Min and Matei Zaharia and Joseph E. Gonzalez},
      year={2025},
      eprint={2506.08276},
      archivePrefix={arXiv},
      primaryClass={cs.DB},
      url={https://arxiv.org/abs/2506.08276},
}
```

## ✨ [详细功能 →](docs/features.md)

## 🤝 [贡献指南 →](docs/CONTRIBUTING.md)


## ❓ [常见问题 →](docs/faq.md)


## 📈 [路线图 →](docs/roadmap.md)

## 📄 许可证 (License)

MIT License - 详见 [LICENSE](LICENSE)。

## 🙏 致谢 (Acknowledgments)

核心贡献者：[Yichuan Wang](https://yichuan-w.github.io/) & [Zhifei Li](https://github.com/andylizf)。

活跃贡献者：[Gabriel Dehan](https://github.com/gabriel-dehan), [Aakash Suresh](https://github.com/ASuresh0524)


我们欢迎更多贡献者！随时提交 Issue 或 PR。

本工作由 [**Berkeley Sky Computing Lab**](https://sky.cs.berkeley.edu/) 完成。

## Star History (Star 历史)

[![Star History Chart](https://api.star-history.com/svg?repos=yichuan-w/LEANN&type=Date)](https://www.star-history.com/#yichuan-w/LEANN&Date)
<p align="center">
  <strong>⭐ 如果 Leann 对你的研究或应用有帮助，请在 GitHub 上 Star 我们！</strong>
</p>

<p align="center">
  Made with ❤️ by the Leann team
</p>

## 🤖 使用 AI 探索 LEANN

LEANN 已收录于 [DeepWiki](https://deepwiki.com/yichuan-w/LEANN)，你可以使用 Deep Research 向 LLM 提问，以探索代码库并获取新功能开发帮助。