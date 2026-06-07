<div align="center">

</div>

<h1 align="center">
	🦉 OWL：面向现实世界任务自动化的通用多智能体协作优化劳动力学习（Optimized Workforce Learning）
</h1>

<div align="center">

[![Documentation][docs-image]][docs-url]
[![Discord][discord-image]][discord-url]
[![X][x-image]][x-url]
[![Reddit][reddit-image]][reddit-url]
[![Wechat][wechat-image]][wechat-url]
[![Wechat][owl-image]][owl-url]
[![Hugging Face][huggingface-image]][huggingface-url]
[![Star][star-image]][star-url]
[![Package License][package-license-image]][package-license-url]
[![Citation](https://img.shields.io/badge/Citation-arXiv%3A2505.23885-purple)](https://arxiv.org/abs/2505.23885)

</div>

<hr>

<div align="center">
<h4 align="center">

[中文阅读](https://github.com/camel-ai/owl/tree/main/README_zh.md) |
[社区](https://github.com/camel-ai/owl#community) |
[安装指南](#️-installation) |
[示例](https://github.com/camel-ai/owl/tree/main/owl) |
[论文](https://arxiv.org/abs/2505.23885) |
[引用](https://github.com/camel-ai/owl#citation) |
[贡献指南](https://github.com/camel-ai/owl/graphs/contributors) |
[CAMEL-AI官网](https://www.camel-ai.org/) |

</h4>

<div align="center" style="background-color: #f0f7ff; padding: 10px; border-radius: 5px; margin: 15px 0;">
  <h3 style="color: #1e88e5; margin: 0;">
    🏆 OWL 在 GAIA 基准测试中取得 <span style="color: #d81b60; font-weight: bold; font-size: 1.2em;">69.09</span> 的平均分，并在开源框架中排名 <span style="color: #d81b60; font-weight: bold; font-size: 1.2em;">🏅️ #1</span>！ 🏆
  </h3>
</div>

<div align="center">

🦉 OWL 是一个前沿的多智能体协作框架，基于 [CAMEL-AI 框架](https://github.com/camel-ai/camel) 构建，不断拓展任务自动化的边界。

我们的愿景是彻底变革人工智能智能体（AI Agent）协作解决现实世界任务的方式。通过利用动态的智能体交互，OWL 能够在各个领域中实现更自然、高效且稳健的任务自动化。

如果你认为本项目有用，请考虑引用我们的工作（[引用](#-cite)）。
</div>

![](./assets/owl_architecture.png)

<br>

</div>

<!-- # Key Features -->

# 📋 目录

- [📋 目录](#-table-of-contents)
- [🔥 最新动态](#-news)
- [🎬 演示视频](#-demo-video)
- [✨️ 核心功能](#️-core-features)
- [🛠️ 安装指南](#️-installation)
  - [**前置要求**](#prerequisites)
    - [安装 Python](#install-python)
  - [**安装选项**](#installation-options)
    - [选项 1：使用 uv（推荐）](#option-1-using-uv-recommended)
    - [选项 2：使用 venv 和 pip](#option-2-using-venv-and-pip)
    - [选项 3：使用 conda](#option-3-using-conda)
    - [选项 4：使用 Docker](#option-4-using-docker)
      - [**使用预构建镜像（推荐）**](#using-pre-built-image-recommended)
      - [**本地构建镜像**](#building-image-locally)
      - [**使用便捷脚本**](#using-convenience-scripts)
  - [**设置环境变量**](#setup-environment-variables)
    - [直接在终端中设置](#setting-environment-variables-directly)
    - [替代方案：使用 `.env` 文件](#alternative-using-a-env-file)
    - [**MCP Desktop Commander 配置**](#mcp-desktop-commander-setup)
- [🚀 快速上手](#-quick-start)
  - [基础用法](#basic-usage)
  - [使用不同模型运行](#running-with-different-models)
    - [模型要求](#model-requirements)
      - [支持的模型](#supported-models)
    - [示例任务](#example-tasks)
- [🧰 工具包与功能](#-toolkits-and-capabilities)
  - [模型上下文协议（MCP）](#model-context-protocol-mcp)
    - [**安装 Node.js**](#install-nodejs)
    - [Windows](#windows)
    - [Linux](#linux)
    - [Mac](#mac)
    - [**安装 Playwright MCP 服务**](#install-playwright-mcp-service)
  - [可用工具包](#available-toolkits)
  - [可用工具包](#available-toolkits-1)
    - [多模态工具包（需具备多模态模型能力）](#multimodal-toolkits-require-multimodal-model-capabilities)
    - [文本处理工具包](#text-based-toolkits)
  - [自定义配置](#customizing-your-configuration)
- [🌐 Web 界面](#-web-interface)
  - [启动 Web UI](#starting-the-web-ui)
  - [功能特性](#features)
- [🧪 实验复现](#-experiments)
- [📄 许可证](#-license)
- [🤝 贡献指南](#-contributing)
- [🔥 社区交流](#-community)
- [❓ 常见问题（FAQ）](#-faq)
  - [通用问题](#general-questions)
  - [实验相关问题](#experiment-questions)
- [📚 探索 CAMEL 依赖项](#-exploring-camel-dependency)
  - [访问 CAMEL 源代码](#accessing-camel-source-code)
- [🖊️ 引用](#️-cite)
- [⭐ Star 历史](#-star-history)

# 🔥 最新动态

<div align="center" style="background-color: #e8f5e9; padding: 15px; border-radius: 10px; border: 2px solid #4caf50; margin: 20px 0;">
  <h3 style="color: #2e7d32; margin: 0; font-size: 1.3em;">
    🧩 <b>新功能：社区智能体挑战！</b> 🧩
  </h3>
  <p style="font-size: 1.1em; margin: 10px 0;">
    通过为 AI 智能体设计独特的挑战来展示你的创造力！<br>
    加入我们的社区，看前沿的 AI 如何解决你提出的创新想法。
  </p>
  <p>
    <a href="https://github.com/camel-ai/owl/blob/main/community_challenges.md" style="background-color: #2e7d32; color: white; padding: 8px 15px; text-decoration: none; border-radius: 5px; font-weight: bold;">查看与提交挑战</a>
  </p>
</div>

<!-- <div style="background-color: #e3f2fd; padding: 12px; border-radius: 8px; border-left: 4px solid #1e88e5; margin: 10px 0;">
  <h4 style="color: #1e88e5; margin: 0 0 8px 0;">
    🎉 最新重大更新 - 2025年3月15日
  </h4>
  <p style="margin: 0;">
    <b>显著改进：</b>
    <ul style="margin: 5px 0 0 0; padding-left: 20px;">
      <li>重构基于 Web 的 UI 架构以提升稳定性 🏗️</li>
      <li>优化 OWL Agent 执行机制以获得更好性能 🚀</li>
    </ul>
    <i>立即体验，感受自动化任务中提升的性能表现！</i>
  </p>
</div> -->

- **[2025.09.22]**：激动地宣布 OWL 已被 NeurIPS 2025 接收！🚀 查看最新论文 [此处](https://arxiv.org/abs/2505.23885)。
- **[2025.07.21]**：我们开源了 OWL 项目的训练数据集和模型权重。训练代码即将发布。[huggingface 链接](https://huggingface.co/collections/camel-ai/optimized-workforce-learning-682ef4ab498befb9426e6e27)。
- **[2025.05.27]**：发布了 OWL 技术报告，包含劳动力（框架）和优化劳动力学习（训练方法）的更多细节。[论文](https://arxiv.org/abs/2505.23885)。
- **[2025.05.18]**：开源了 GAIA 基准测试劳动力实验的初始复现代码 [此处](https://github.com/camel-ai/owl/tree/gaia69)。
- **[2025.04.18]**：上传了 OWL 新的 GAIA 基准分数 **69.09%**，在开源框架中排名第 1。查看技术报告 [此处](https://hypnotic-mind-6bd.notion.site/OWL-Optimized-Workforce-Learning-for-General-Multi-Agent-Assistance-in-Real-World-Task-Automation-1d4004aeb21380158749c7f84b20643f)。
- **[2025.03.27]**：集成 SearxNGToolkit，使用 SearxNG 搜索引擎执行网络搜索。
- **[2025.03.26]**：增强 Browser Toolkit，支持 "chrome"、"msedge" 和 "chromium" 通道的多浏览器支持。
- **[2025.03.25]**：支持 Gemini 2.5 Pro，添加示例运行代码
- **[2025.03.21]**：集成 OpenRouter 模型平台，修复 Gemini 工具调用的 bug。
- **[2025.03.20]**：MCP Toolkit 接受 header，支持自动安装 playwright。
- **[2025.03.16]**：支持 Bing 搜索、百度搜索。
- **[2025.03.12]**：SearchToolkit 新增 Bocha 搜索，集成火山引擎模型平台，增强 Azure 和 OpenAI Compatible 模型的结构化输出与工具调用能力。
- **[2025.03.11]**：添加 MCPToolkit、FileWriteToolkit 和 TerminalToolkit，以增强 OWL 智能体的 MCP 工具调用、文件写入能力和终端命令执行功能。
- **[2025.03.09]**：添加了基于 Web 的用户界面，使系统交互更加便捷。
- **[2025.03.07]**：开源了 🦉 OWL 项目的代码库。
- **[2025.03.03]**：OWL 在 GAIA 基准测试中以 58.18 分的成绩位列开源框架第 1 名。

# 🎬 演示视频

https://github.com/user-attachments/assets/2a2a825d-39ea-45c5-9ba1-f9d58efbc372

https://private-user-images.githubusercontent.com/55657767/420212194-e813fc05-136a-485f-8df3-f10d9b4e63ec.mp4

该视频演示了如何在本地安装 OWL，并展示了其作为前沿多智能体协作框架的能力：https://www.youtube.com/watch?v=8XlqVyAZOr8

# ✨️ 核心功能

- **在线搜索** (Online Search)：支持多种搜索引擎（包括维基百科、Google、DuckDuckGo、百度、Bocha 等），用于实时信息检索和知识获取。
- **多模态处理** (Multimodal Processing)：支持处理互联网或本地的视频、图像和音频数据。
- **浏览器自动化** (Browser Automation)：利用 Playwright 框架模拟浏览器交互，包括滚动、点击、输入、下载、导航等。
- **文档解析** (Document Parsing)：从 Word、Excel、PDF 和 PowerPoint 文件中提取内容，并将其转换为文本或 Markdown 格式。
- **代码执行** (Code Execution)：使用解释器编写和执行 Python 代码。
- **内置工具包** (Built-in Toolkits)：提供全面的内置工具包，包括：
  - **模型上下文协议（MCP）** (Model Context Protocol)：标准化 AI 模型与各种工具和数据来源交互的通用协议层
  - **核心工具包** (Core Toolkits)：ArxivToolkit, AudioAnalysisToolkit, CodeExecutionToolkit, DalleToolkit, DataCommonsToolkit, ExcelToolkit, GitHubToolkit, GoogleMapsToolkit, GoogleScholarToolkit, ImageAnalysisToolkit, MathToolkit, NetworkXToolkit, NotionToolkit, OpenAPIToolkit, RedditToolkit, SearchToolkit, SemanticScholarToolkit, SymPyToolkit, VideoAnalysisToolkit, WeatherToolkit, BrowserToolkit 等，用于处理各类专业任务

# 🛠️ 安装指南

## **前置要求**

### 安装 Python

在开始安装 OWL 之前，请确保已安装 Python（支持版本 3.10、3.11 或 3.12）：

> **GAIA 基准测试用户注意**：运行 GAIA 基准评估时，请使用 `gaia58.18` 分支，该分支在 `owl/camel` 目录中包含 CAMEL 框架的定制版本。与标准 CAMEL 安装相比，此版本包含经过专门优化以提升稳定性的增强工具包，特别适用于 GAIA 基准测试。

```bash
# Check if Python is installed
python --version

# If not installed, download and install from https://www.python.org/downloads/
# For macOS users with Homebrew:
brew install python@3.10

# For Ubuntu/Debian:
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip
```

## **安装选项**

OWL 支持多种安装方式，以适应你的工作流程偏好。

### 选项 1：使用 uv（推荐）

```bash
# Clone github repo
git clone https://github.com/camel-ai/owl.git

# Change directory into project directory
cd owl

# Install uv if you don't have it already
pip install uv

# Create a virtual environment and install dependencies
uv venv .venv --python=3.10

# Activate the virtual environment
# For macOS/Linux
source .venv/bin/activate
# For Windows
.venv\Scripts\activate

# Install CAMEL with all dependencies
uv pip install -e .
```

### 选项 2：使用 venv 和 pip

```bash
# Clone github repo
git clone https://github.com/camel-ai/owl.git

# Change directory into project directory
cd owl

# Create a virtual environment
# For Python 3.10 (also works with 3.11, 3.12)
python3.10 -m venv .venv

# Activate the virtual environment
# For macOS/Linux
source .venv/bin/activate
# For Windows
.venv\Scripts\activate

# Install from requirements.txt
pip install -r requirements.txt --use-pep517
```

### 选项 3：使用 conda

```bash
# Clone github repo
git clone https://github.com/camel-ai/owl.git

# Change directory into project directory
cd owl

# Create a conda environment
conda create -n owl python=3.10

# Activate the conda environment
conda activate owl

# Option 1: Install as a package (recommended)
pip install -e .

# Option 2: Install from requirements.txt
pip install -r requirements.txt --use-pep517
```

### 选项 4：使用 Docker

#### **使用预构建镜像（推荐）**

```bash
# This option downloads a ready-to-use image from Docker Hub
# Fastest and recommended for most users
docker compose up -d

# Run OWL inside the container
docker compose exec owl bash
cd .. && source .venv/bin/activate
playwright install-deps
xvfb-python examples/run.py
```

#### **本地构建镜像**

```bash
# For users who need to customize the Docker image or cannot access Docker Hub:
# 1. Open docker-compose.yml
# 2. Comment out the "image: mugglejinx/owl:latest" line
# 3. Uncomment the "build:" section and its nested properties
# 4. Then run:
docker compose up -d --build

# Run OWL inside the container
docker compose exec owl bash
cd .. && source .venv/bin/activate
playwright install-deps
xvfb-python examples/run.py
```

#### **使用便捷脚本**

```bash
# Navigate to container directory
cd .container

# Make the script executable and build the Docker image
chmod +x build_docker.sh
./build_docker.sh

# Run OWL with your question
./run_in_docker.sh "your question"
```

## **设置环境变量**

OWL 需要各种 API 密钥来与不同服务进行交互。

### 直接在终端中设置

你可以在终端中直接设置环境变量：

- **macOS/Linux (Bash/Zsh)**：

  ```bash
  export OPENAI_API_KEY="your-openai-api-key-here"
  # Add other required API keys as needed
  ```

- **Windows (Command Prompt)**：

  ```batch
  set OPENAI_API_KEY=your-openai-api-key-here
  ```

- **Windows (PowerShell)**：
  ```powershell
  $env:OPENAI_API_KEY = "your-openai-api-key-here"
  ```

> **注意**：在终端中直接设置的环境变量仅在当前会话中有效。

### 替代方案：使用 `.env` 文件

如果你更倾向于使用 `.env` 文件，可以执行以下操作：

1. **复制并重命名模板**：

   ```bash
   # For macOS/Linux
   cd owl
   cp .env_template .env

   # For Windows
   cd owl
   copy .env_template .env
   ```

   或者，你也可以手动在 `owl` 目录下创建一个名为 `.env` 的新文件，并将 `.env_template` 的内容复制进去。

2. **配置 API 密钥**：
   用你喜欢的文本编辑器打开 `.env` 文件，并在对应字段中填入你的 API 密钥。

> **注意**：对于最小化示例（`examples/run_mini.py`），你只需配置 LLM API 密钥即可（例如 `OPENAI_API_KEY`）。

### **MCP Desktop Commander 配置**

如果在 Docker 中使用 MCP Desktop Commander，请运行：

```bash
npx -y @wonderwhy-er/desktop-commander setup --force-file-protocol
```

有关更详细的 Docker 使用说明（包括跨平台支持、优化配置和故障排除），请参阅 [DOCKER_README.md](.container/DOCKER_README_en.md)。

# 🚀 快速上手

## 基础用法

安装并配置好环境变量后，即可开始使用 OWL：

```bash
python examples/run.py
```

## 使用不同模型运行

### 模型要求

- **工具调用能力** (Tool Calling)：OWL 需要具备强大工具调用能力的模型来与各类工具包交互。模型必须能够理解工具描述、生成适当的工具调用指令，并处理工具的返回结果。

- **多模态理解** (Multimodal Understanding)：对于涉及网页交互、图像分析或视频处理的任务，需要具备多模态能力的模型来解读视觉内容和上下文信息。

#### 支持的模型

有关配置 AI 模型的详细信息，请参阅我们的 [CAMEL 模型文档](https://docs.camel-ai.org/key_modules/models.html#supported-model-platforms-in-camel)。

> **注意**：为了获得最佳性能，我们强烈建议使用 OpenAI 模型（GPT-4 或更高版本）。我们的实验表明，其他模型在复杂任务和基准测试中可能会导致显著的性能下降，尤其是那些需要高级多模态理解和工具使用的任务。

OWL 支持多种 LLM 后端，但功能可能因模型的工具调用和多模态能力而异。你可以使用以下脚本运行不同模型的版本：

```bash
# Run with Claude model
python examples/run_claude.py

# Run with Qwen model
python examples/run_qwen_zh.py

# Run with Deepseek model
python examples/run_deepseek_zh.py

# Run with other OpenAI-compatible models
python examples/run_openai_compatible_model.py

# Run with Gemini model
python examples/run_gemini.py

# Run with Azure OpenAI
python examples/run_azure_openai.py

# Run with Ollama
python examples/run_ollama.py
```

对于只需配置 LLM API 密钥的简化版本，你可以尝试我们的最小化示例：

```bash
python examples/run_mini.py
```

你可以通过修改 `examples/run.py` 脚本来使用自己的任务运行 OWL 智能体：

```python
# Define your own task
task = "Task description here."

society = construct_society(question)
answer, chat_history, token_count = run_society(society)

print(f"\033[94mAnswer: {answer}\033[0m")
```

如需上传文件，只需在提问时附带文件路径即可：

```python
# Task with a local file (e.g., file path: `tmp/example.docx`)
task = "What is in the given DOCX file? Here is the file path: tmp/example.docx"

society = construct_society(question)
answer, chat_history, token_count = run_society(society)
print(f"\033[94mAnswer: {answer}\033[0m")
```

随后 OWL 将自动调用文档相关工具来处理文件并提取答案。

### 示例任务

以下是一些你可以尝试使用 OWL 执行的任务：

- "查找苹果公司最新的股票价格"
- "分析近期关于气候变化的推文情感倾向"
- "帮我调试这段 Python 代码：[你的代码]"
- "总结这篇研究论文的主要观点：[论文 URL]"
- "为这个数据集创建数据可视化图表：[数据集路径]"

# 🧰 工具包与功能

## 模型上下文协议（MCP） (Model Context Protocol)

OWL 的 MCP 集成为 AI 模型提供了一种标准化的方式来与各种工具和数据来源进行交互：

在使用 MCP 之前，你需要先安装 Node.js。

### **安装 Node.js**

### Windows

下载官方安装包：[Node.js](https://nodejs.org/en)。
安装时勾选 "Add to PATH"（添加到环境变量）选项。

### Linux

```bash
sudo apt update
sudo apt install nodejs npm -y
```

### Mac

```bash
brew install node
```

### **安装 Playwright MCP 服务**

```bash
npm install -g @executeautomation/playwright-mcp-server
npx playwright install-deps
```

尝试我们的综合 MCP 示例：

- `examples/run_mcp.py` - 基础 MCP 功能演示（本地调用，需依赖）
- `examples/run_mcp_sse.py` - 使用 SSE 协议的示例（使用远程服务，无需依赖）

## 可用工具包

> **重要提示**：有效使用工具包需要具备强大工具调用能力的模型。对于多模态工具包（网页、图像、视频），模型还必须具备多模态理解能力。

OWL 支持多种工具包，你可以通过修改脚本中的 `tools` 列表来自定义配置：

```python
# Configure toolkits
tools = [
    *BrowserToolkit(headless=False).get_tools(),  # Browser automation
    *VideoAnalysisToolkit(model=models["video"]).get_tools(),
    *AudioAnalysisToolkit().get_tools(),  # Requires OpenAI Key
    *CodeExecutionToolkit(sandbox="subprocess").get_tools(),
    *ImageAnalysisToolkit(model=models["image"]).get_tools(),
    SearchToolkit().search_duckduckgo,
    SearchToolkit().search_google,  # Comment out if unavailable
    SearchToolkit().search_wiki,
    SearchToolkit().search_bocha,
    SearchToolkit().search_baidu,
    *ExcelToolkit().get_tools(),
    *DocumentProcessingToolkit(model=models["document"]).get_tools(),
    *FileWriteToolkit(output_dir="./").get_tools(),
]
```

## 可用工具包

关键工具包包括：

### 多模态工具包（需具备多模态模型能力）

- **BrowserToolkit**：用于网页交互和导航的浏览器自动化
- **VideoAnalysisToolkit**：视频处理与内容分析
- **ImageAnalysisToolkit**：图像分析与解读

### 文本处理工具包

- **AudioAnalysisToolkit**：音频处理（需 OpenAI API）
- **CodeExecutionToolkit**：Python 代码执行与评估
- **SearchToolkit**：网络搜索（Google、DuckDuckGo、维基百科）
- **DocumentProcessingToolkit**：文档解析（PDF、DOCX 等）

其他专业工具包：ArxivToolkit, GitHubToolkit, GoogleMapsToolkit, MathToolkit, NetworkXToolkit, NotionToolkit, RedditToolkit, WeatherToolkit 等。完整列表请参阅 [CAMEL 工具包文档](https://docs.camel-ai.org/key_modules/tools)。

## 自定义配置

若要自定义可用工具：

```python
# 1. Import toolkits
from camel.toolkits import BrowserToolkit, SearchToolkit, CodeExecutionToolkit

# 2. Configure tools list
tools = [
    *BrowserToolkit(headless=True).get_tools(),
    SearchToolkit().search_wiki,
    *CodeExecutionToolkit(sandbox="subprocess").get_tools(),
]

# 3. Pass to assistant agent
assistant_agent_kwargs = {"model": models["assistant"], "tools": tools}
```

仅选择必要的工具包可以优化性能并减少资源占用。

# 🌐 Web 界面

<div align="center" style="background-color: #f0f7ff; padding: 15px; border-radius: 10px; border: 2px solid #1e88e5; margin: 20px 0;">
  <h3 style="color: #1e88e5; margin: 0;">
    🚀 增强版 Web 界面现已上线！
  </h3>
  <p style="margin: 10px 0;">
    通过最新更新体验提升的系统稳定性和优化后的性能。
    立即通过我们用户友好的界面探索 OWL 的强大功能！
  </p>
</div>

## 启动 Web UI

```bash
# Start the Chinese version
python owl/webapp_zh.py

# Start the English version
python owl/webapp.py

# Start the Japanese version
python owl/webapp_jp.py
```

## 功能特性

- **轻松选择模型**：可在不同模型之间进行选择（OpenAI、Qwen、DeepSeek 等）
- **环境变量管理**：直接从 UI 配置 API 密钥和其他设置
- **交互式聊天界面**：通过用户友好的界面与 OWL 智能体进行对话
- **任务历史记录**：查看交互历史与结果

Web 界面基于 Gradio 构建，并在你的本地机器上运行。除了你配置的模型 API 调用所需的数据外，不会向外部服务器发送任何数据。

# 🧪 实验复现

若要复现 OWL 的 GAIA 基准测试成绩：

我们在 `main` 分支中也提供了增强版 OWL，因此即使不切换分支，你也可以直接受益于升级的工具包和更高的稳定性。
对于原始的 GAIA 专项性能表现，推荐使用我们的 `gaia69` 分支。

运行基准评估时：

1. 切换到 `gaia69` 分支：

   ```bash
   git checkout gaia69
   ```

2. 运行评估脚本：
   ```bash
   python run_gaia_workforce_claude.py
   ```

这将执行与我们在 GAIA 基准测试中取得顶尖排名相同的配置。

# 📄 许可证

源代码采用 Apache 2.0 许可证授权。

# 🤝 贡献指南

我们欢迎社区的贡献！以下是你可以参与的方式：

1. 阅读我们的 [贡献指南](https://github.com/camel-ai/camel/blob/master/CONTRIBUTING.md)
2. 查看 [开放 Issue](https://github.com/camel-ai/camel/issues) 或创建新的 Issue
3. 提交包含你改进内容的 Pull Request

**当前开放贡献的 Issues：**

- [#1915](https://github.com/camel-ai/camel/issues/1915)
- [#2190](https://github.com/camel-ai/camel/issues/2190)
- [#2165](https://github.com/camel-ai/camel/issues/2165)
- [#2121](https://github.com/camel-ai/camel/issues/2121)
- [#1908](https://github.com/camel-ai/camel/issues/1908)
- [#1538](https://github.com/camel-ai/camel/issues/1538)
- [#1481](https://github.com/camel-ai/camel/issues/1481)

若要认领某个 Issue，只需留下评论表明你的兴趣即可。

# 🔥 社区交流

加入我们（[_Discord_](https://discord.camel-ai.org/) 或 [_微信_](https://ghli.org/camel/wechat.png)），共同探索智能体扩展定律的边界。

欢迎加入我们的进一步讨论！

<!-- ![](./assets/community.png) -->
<img src="./assets/community_code.jpeg" width="50%" />

# ❓ 常见问题（FAQ）

## 通用问题

**Q：为什么启动示例脚本后我没有看到本地运行的 Chrome？**

A：如果 OWL 判断任务可以通过非浏览器工具（如搜索或代码执行）完成，则不会启动浏览器。只有当 OWL 判定需要基于浏览器的交互时，才会显示浏览器窗口。

**Q：我应该使用哪个 Python 版本？**

A：OWL 支持 Python 3.10、3.11 和 3.12。

**Q：我如何为项目做出贡献？**

A：请参阅我们的 [贡献指南](#-contributing) 章节，了解如何参与。我们欢迎各种形式的贡献，从代码改进到文档更新均非常欢迎。

## 实验相关问题

**Q：复现角色扮演结果应该使用哪个 CAMEL 版本？**

A：我们在 `gaia58.18` 分支中提供了一个修改版的 CAMEL（`owl/camel`）。请确保在实验中使用该版本的 CAMEL。

**Q：为什么我的实验结果低于报告中的数值？**

A：由于 GAIA 基准测试是在真实世界环境中评估 LLM 智能体，因此引入了大量的随机性。根据用户反馈，复现中最常见的问题之一是智能体因网络原因在某些网页上被阻塞。
我们已上传一个关键词匹配脚本，用于快速过滤这些错误 [此处](https://github.com/camel-ai/owl/blob/gaia58.18/owl/filter_failed_cases.py)。
在真实开放世界环境中评估 LLM 智能体时，你也可以查看此 [技术报告](https://hypnotic-mind-6bd.notion.site/OWL-Optimized-Workforce-Learning-for-General-Multi-Agent-Assistance-in-Real-World-Task-Automation-1d4004aeb21380158749c7f84b20643f?pvs=74) 获取更多信息。

# 📚 探索 CAMEL 依赖项

OWL 构建于 [CAMEL](https://github.com/camel-ai/camel) 框架之上，以下是如何探索 CAMEL 源代码并了解其与 OWL 协同工作方式的方法：

## 访问 CAMEL 源代码

```bash
# Clone the CAMEL repository
git clone https://github.com/camel-ai/camel.git
cd camel
```

# 🖊️ 引用

如果你认为本项目有用，请引用：

```
@misc{hu2025owl,
      title={OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation},
      author={Mengkang Hu and Yuhang Zhou and Wendong Fan and Yuzhou Nie and Bowei Xia and Tao Sun and Ziyu Ye and Zhaoxuan Jin and Yingru Li and Qiguang Chen and Zeyu Zhang and Yifeng Wang and Qianshuo Ye and Bernard Ghanem and Ping Luo and Guohao Li},
      year={2025},
      eprint={2505.23885},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2505.23885},
}
```

# ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=camel-ai/owl&type=Date)](https://star-history.com/#camel-ai/owl&Date)

[docs-image]: https://img.shields.io/badge/Documentation-EB3ECC
[docs-url]: https://camel-ai.github.io/camel/index.html
[star-image]: https://img.shields.io/github/stars/camel-ai/owl?label=stars&logo=github&color=brightgreen
[star-url]: https://github.com/camel-ai/owl/stargazers
[package-license-image]: https://img.shields.io/badge/License-Apache_2.0-blue.svg
[package-license-url]: https://github.com/camel-ai/owl/blob/main/licenses/LICENSE
[colab-url]: https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing
[colab-image]: https://colab.research.google.com/assets/colab-badge.svg
[huggingface-url]: https://huggingface.co/camel-ai
[huggingface-image]: https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-CAMEL--AI-ffc107?color=ffc107&logoColor=white
[discord-url]: https://discord.camel-ai.org/
[discord-image]: https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb
[wechat-url]: https://ghli.org/camel/wechat.png
[wechat-image]: https://img.shields.io/badge/WeChat-CamelAIOrg-brightgreen?logo=wechat&logoColor=white
[x-url]: https://x.com/CamelAIOrg
[x-image]: https://img.shields.io/twitter/follow/CamelAIOrg?style=social
[twitter-image]: https://img.shields.io/twitter/follow/CamelAIOrg?style=social&color=brightgreen&logo=twitter
[reddit-url]: https://www.reddit.com/r/CamelAI/
[reddit-image]: https://img.shields.io/reddit/subreddit-subscribers/CamelAI?style=plastic&logo=reddit&label=r%2FCAMEL&labelColor=white
[ambassador-url]: https://www.camel-ai.org/community
[owl-url]: ./assets/qr_code.jpg
[owl-image]: https://img.shields.io/badge/WeChat-OWLProject-brightgreen?logo=wechat&logoColor=white