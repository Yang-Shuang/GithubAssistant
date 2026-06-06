<div align="center">

<a href="https://openviking.ai/" target="_blank">
  <picture>
    <img alt="OpenViking" src="docs/images/ov-logo.png" width="200px" height="auto">
  </picture>
</a>

### OpenViking：AI Agent 的上下文数据库

English / [中文](README_CN.md) / [日本語](README_JA.md)

<a href="https://www.openviking.ai">官网</a> · <a href="https://github.com/volcengine/OpenViking">GitHub</a> · <a href="https://github.com/volcengine/OpenViking/issues">Issues</a> · <a href="./docs">文档</a>

[![](https://img.shields.io/github/v/release/volcengine/OpenViking?color=369eff\&labelColor=black\&logo=github\&style=flat-square)](https://github.com/volcengine/OpenViking/releases)
[![](https://img.shields.io/github/stars/volcengine/OpenViking?labelColor\&style=flat-square\&color=ffcb47)](https://github.com/volcengine/OpenViking)
[![](https://img.shields.io/github/issues/volcengine/OpenViking?labelColor=black\&style=flat-square\&color=ff80eb)](https://github.com/volcengine/OpenViking/issues)
[![](https://img.shields.io/github/contributors/volcengine/OpenViking?color=c4f042\&labelColor=black\&style=flat-square)](https://github.com/volcengine/OpenViking/graphs/contributors)
[![](https://img.shields.io/badge/license-AGPLv3-white?labelColor=black\&style=flat-square)](https://github.com/volcengine/OpenViking/blob/main/LICENSE)
[![](https://img.shields.io/github/last-commit/volcengine/OpenViking?color=c4f042\&labelColor=black\&style=flat-square)](https://github.com/volcengine/OpenViking/commits/main)

👋 加入我们的社区

📱 <a href="./docs/en/about/01-about-us.md#lark-group">飞书群</a> · <a href="./docs/en/about/01-about-us.md#wechat-group">微信</a> · <a href="https://discord.com/invite/eHvx8E9XF3">Discord</a> · <a href="https://x.com/openvikingai">X (Twitter)</a>

<a href="https://trendshift.io/repositories/19668" target="_blank"><img src="https://trendshift.io/api/badge/repositories/19668" alt="volcengine%2FOpenViking | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

***

✨ **2026年5月更新**：更新了 OpenViking 在用户记忆、Agent 记忆和知识库问答（QA）场景下的基准测试结果。→ 详见[评测亮点](#evaluation-highlights)。

## 概述

### AI Agent 开发中的挑战

在 AI 时代，数据虽丰富，但高质量的上下文却难以获取。构建 AI Agent 时，开发者常面临以下挑战：

- **上下文碎片化**：记忆散落在代码中，资源存放在向量数据库里，技能也四处分散，难以统一管理。
- **上下文需求激增**：Agent 的长周期任务在每次执行时都会产生大量上下文。简单的截断或压缩会导致信息丢失。
- **检索效果不佳**：传统 RAG 采用扁平化存储，缺乏全局视角，难以理解信息的完整上下文。
- **上下文不可观测**：传统 RAG 的隐式检索链如同黑盒，出错时难以调试。
- **记忆迭代能力有限**：当前的记忆仅是用户交互的记录，缺乏与 Agent 任务相关的记忆管理。

### OpenViking 的解决方案

**OpenViking** 是一款专为 AI Agent 设计的开源**上下文数据库**。

我们旨在为 Agent 定义一种极简的上下文交互范式，让开发者彻底告别上下文管理的繁琐。OpenViking 摒弃了传统 RAG 碎片化的向量存储模式，创新性地采用**“文件系统范式”**，统一结构化地组织 Agent 所需的记忆、资源和技能。

借助 OpenViking，你可以像管理本地文件一样构建 Agent 的“大脑”：

- **文件系统管理范式** → **解决碎片化**：基于文件系统范式，统一管理记忆、资源和技能。
- **分层上下文加载** → **降低 Token 消耗**：采用 L0/L1/L2 三层结构，按需加载，显著节省成本。
- **目录递归检索** → **提升检索效果**：支持原生文件系统检索方式，结合目录定位与语义搜索，实现递归且精准的上下文获取。
- **可视化检索轨迹** → **可观测的上下文**：支持可视化目录检索轨迹，让你清晰观察问题根源并指导检索逻辑优化。
- **自动会话管理** → **上下文自迭代**：自动压缩对话中的内容、资源引用、工具调用等，提取长期记忆，让 Agent 越用越聪明。

## 快速开始

### 前置条件

在开始使用 OpenViking 之前，请确保你的环境满足以下要求：

- **Python 版本**：3.10 或更高
- **Rust 工具链**：Cargo（用于从源码构建 RAGFS 和 CLI 组件）
- **C++ 编译器**：GCC 9+ 或 Clang 11+（用于构建核心扩展）
- **操作系统**：Linux、macOS、Windows
- **网络连接**：需要稳定的网络连接（用于下载依赖和访问模型服务）

### 1. 安装

#### Python 包

```bash
pip install openviking --upgrade --force-reinstall
```

#### Rust CLI（可选）

```bash
npm i -g @openviking/cli
```

或从源码构建：

```bash
cargo install --git https://github.com/volcengine/OpenViking ov_cli
```

### 2. 模型准备

OpenViking 需要以下模型能力支持：

- **视觉语言模型（VLM）**：用于图像和内容理解
- **向量嵌入模型（Embedding）**：用于向量化和语义检索

#### 支持的 VLM 提供商

OpenViking 支持多种 VLM 提供商：

| Provider       | Description              | Setup                                                                                                                                                                                                              |
| -------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `volcengine`   | 火山引擎（Doubao）模型 | [火山引擎控制台](https://console.volcengine.com/ark/region:ark+cn-beijing/overview?briefPage=0\&briefType=introduce\&type=new\&utm_content=OpenViking\&utm_medium=devrel\&utm_source=OWO\&utm_term=OpenViking) |
| `openai`       | OpenAI 官方 API      | [OpenAI 平台](https://platform.openai.com)                                                                                                                                                                     |
| `openai-codex` | Codex VLM                | 使用 `openviking-server init`                                                                                                                                                                                       |
| `kimi`         | Kimi 编程订阅     | 使用 `openviking-server init`                                                                                                                                                                                       |
| `glm`          | GLM 编程计划          | 使用 `openviking-server init`                                                                                                                                                                                       |

#### 各提供商注意事项

<details>
<summary><b>火山引擎（Doubao）</b></summary>

火山引擎支持使用模型名称和 Endpoint ID。为简化配置，建议使用模型名称：

```json
{
  "vlm": {
    "provider": "volcengine",
    "model": "doubao-seed-2-0-pro-260215",
    "api_key": "your-api-key",
    "api_base": "https://ark.cn-beijing.volces.com/api/v3"
  }
}
```

你也可以使用 Endpoint ID（可在[火山引擎 ARK 控制台](https://console.volcengine.com/ark/region:ark+cn-beijing/overview?briefPage=0\&briefType=introduce\&type=new\&utm_content=OpenViking\&utm_medium=devrel\&utm_source=OWO\&utm_term=OpenViking) 中找到）：

```json
{
  "vlm": {
    "provider": "volcengine",
    "model": "ep-20241220174930-xxxxx",
    "api_key": "your-api-key",
    "api_base": "https://ark.cn-beijing.volces.com/api/v3"
  }
}
```

</details>

<details>
<summary><b>OpenAI</b></summary>

使用 OpenAI 官方 API：

```json
{
  "vlm": {
    "provider": "openai",
    "model": "gpt-4o",
    "api_key": "your-api-key",
    "api_base": "https://api.openai.com/v1"
  }
}
```

你也可以使用兼容 OpenAI 协议的自定义 Endpoint：

```json
{
  "vlm": {
    "provider": "openai",
    "model": "gpt-4o",
    "api_key": "your-api-key",
    "api_base": "https://your-custom-endpoint.com/v1"
  }
}
```

</details>

<details>
<summary><b>OpenAI Codex（OAuth）</b></summary>

当你希望 OpenViking 通过你的 ChatGPT/Codex OAuth 会话调用 Codex VLM，而非使用标准 OpenAI API Key 时，请使用此提供商：

```bash
openviking-server init
# choose OpenAI Codex when prompted
openviking-server doctor
```

```json
{
  "vlm": {
    "provider": "openai-codex",
    "model": "gpt-5.3-codex",
    "api_base": "https://chatgpt.com/backend-api/codex",
    "temperature": 0.0,
    "max_retries": 2
  }
}
```

> 💡 **提示**：
>
> - 当启用 Codex OAuth 时，无需配置 `vlm.api_key`
> - OpenViking 将自身的 Codex 认证状态存储在 `~/.openviking/codex_auth.json`
> - `openviking-server doctor` 会验证当前 Codex 认证是否可用

</details>

<details>
<summary><b>Kimi 编程（订阅）</b></summary>

当你希望 OpenViking 直接调用专属的 Kimi 编程订阅 Endpoint 时，请使用此提供商：

```bash
openviking-server init
# choose Kimi Coding when prompted
openviking-server doctor
```

```json
{
  "vlm": {
    "provider": "kimi",
    "model": "kimi-code",
    "api_key": "your-kimi-subscription-api-key",
    "api_base": "https://api.kimi.com/coding",
    "temperature": 0.0,
    "max_retries": 2
  }
}
```

> 💡 **提示**：
>
> - `kimi` 会自动应用推荐的 Kimi 编程默认配置，包括默认的 User-Agent
> - `kimi-code` 和 `kimi-coding` 均可作为提供商名称的别名使用
> - `kimi-code` 会自动映射为 Kimi 上游的编程模型

</details>

<details>
<summary><b>GLM 编程计划（订阅）</b></summary>

当你希望 OpenViking 直接调用智谱 AI（Z.AI）兼容 OpenAI 协议的编程计划 Endpoint 时，请使用此提供商：

```bash
openviking-server init
# choose GLM Coding Plan when prompted
openviking-server doctor
```

```json
{
  "vlm": {
    "provider": "glm",
    "model": "glm-4.6v",
    "api_key": "your-zai-api-key",
    "api_base": "https://api.z.ai/api/coding/paas/v4",
    "temperature": 0.0,
    "max_retries": 2
  }
}
```

> 💡 **提示**：
>
> - `glm`、`zhipu`、`zai`、`z-ai` 和 `z.ai` 均会解析为同一个官方 GLM 提供商
> - 默认 Endpoint 为编程计划专用地址，而非智谱通用 API 地址
> - 多模态解析请使用支持视觉的模型（如 `glm-4.6v` 或 `glm-5v-turbo`）

</details>

### 3. 环境配置

#### 本地模型快速设置（Ollama）

如果你希望通过 [Ollama](https://ollama.ai) 使用本地模型运行 OpenViking，交互式安装向导会自动处理所有配置：

```bash
openviking-server init
```

该向导将执行以下操作：

- 检测并自动安装 Ollama（如需要）
- 根据你的硬件推荐并拉取合适的 Embedding 和 VLM 模型
- 生成开箱即用的 `ov.conf` 配置文件

随时验证配置：

```bash
openviking-server doctor
```

`doctor` 会检查本地前置条件（配置文件、Python 版本、Embedding/VLM 提供商连通性、磁盘空间），无需启动服务器即可运行。

> 对于云 API 提供商（火山引擎、OpenAI、Gemini 等），请继续参考下方的手动配置说明。

#### 服务器配置文件模板

首次推荐的配置流程为：

```bash
openviking-server init
openviking-server doctor
```

如果在 `openviking-server init` 中选择 `OpenAI Codex`，向导会自动导入现有的 Codex 认证或引导你完成登录。

如需手动配置，请创建 `~/.openviking/ov.conf` 文件（复制前请删除注释）：

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "log": {
    "level": "INFO",
    "output": "stdout"                 // Log output: "stdout" or "file"
  },
  "embedding": {
    "dense": {
      "api_base" : "<api-endpoint>",   // API endpoint address
      "api_key"  : "<your-api-key>",   // Model service API Key
      "provider" : "<provider-type>",  // Provider type: "volcengine" or "openai" (currently supported)
      "dimension": 1024,               // Vector dimension
      "model"    : "<model-name>"      // Embedding model name (e.g., doubao-embedding-vision-251215 or text-embedding-3-large)
    },
    "max_concurrent": 10,              // Max concurrent embedding requests (default: 10)
    "text_source": "content_only",     // Text file vectorization source: content_only|summary_first|summary_only
    "max_input_tokens": 4096           // Max estimated raw text tokens sent to embedding
  },
  "vlm": {
    "api_base" : "<api-endpoint>",     // API endpoint address
    "api_key"  : "<your-api-key>",     // Model service API Key (optional for openai-codex)
    "provider" : "<provider-type>",    // Provider type (volcengine, openai, openai-codex, kimi, glm, etc.)
    "model"    : "<model-name>",       // VLM model name (e.g., doubao-seed-2-0-pro-260215 or gpt-4-vision-preview)
    "max_concurrent": 64              // Max concurrent LLM calls for semantic processing (default: 64)
  }
}
```

> **注意**：支持的 Embedding 提供商包括 `volcengine`（Doubao）、`openai`、`azure`、`jina`、`ollama`、`voyage`、`dashscope`、`minimax`、`cohere`、`vikingdb`、`gemini`（需执行 `pip install "google-genai>=1.0.0"`）、`litellm` 和 `local`。VLM 常用提供商包括 `volcengine`、`openai`、`openai-codex`、`kimi` 和 `glm`。

#### 服务器配置示例

👇 展开查看你的模型服务配置示例：

<details>
<summary><b>示例 1：使用火山引擎（Doubao 模型）</b></summary>

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "log": {
    "level": "INFO",
    "output": "stdout"                 // Log output: "stdout" or "file"
  },
  "embedding": {
    "dense": {
      "api_base" : "https://ark.cn-beijing.volces.com/api/v3",
      "api_key"  : "your-volcengine-api-key",
      "provider" : "volcengine",
      "dimension": 1024,
      "model"    : "doubao-embedding-vision-251215"
    },
    "max_concurrent": 10
  },
  "vlm": {
    "api_base" : "https://ark.cn-beijing.volces.com/api/v3",
    "api_key"  : "your-volcengine-api-key",
    "provider" : "volcengine",
    "model"    : "doubao-seed-2-0-pro-260215",
    "max_concurrent": 64
  }
}
```

</details>

<details>
<summary><b>示例 2：使用 OpenAI 模型</b></summary>

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "log": {
    "level": "INFO",
    "output": "stdout"                 // Log output: "stdout" or "file"
  },
  "embedding": {
    "dense": {
      "api_base" : "https://api.openai.com/v1",
      "api_key"  : "your-openai-api-key",
      "provider" : "openai",
      "dimension": 3072,
      "model"    : "text-embedding-3-large"
    },
    "max_concurrent": 10
  },
  "vlm": {
    "api_base" : "https://api.openai.com/v1",
    "api_key"  : "your-openai-api-key",
    "provider" : "openai",
    "model"    : "gpt-4-vision-preview",
    "max_concurrent": 64
  }
}
```

</details>

<details>
<summary><b>示例 3：使用 Google Gemini Embedding</b></summary>

首先安装所需依赖包：

```bash
pip install "google-genai>=1.0.0"
```

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "embedding": {
    "dense": {
      "provider": "gemini",
      "api_key": "your-google-api-key",
      "model": "gemini-embedding-2-preview",
      "dimension": 3072
    },
    "max_concurrent": 10
  },
  "vlm": {
    "api_base" : "https://api.openai.com/v1",
    "api_key"  : "your-openai-api-key",
    "provider" : "openai",
    "model"    : "gpt-4o",
    "max_concurrent": 64
  }
}
```

在 <https://aistudio.google.com/apikey> 获取你的 Google API Key。

</details>

<details>
<summary><b>示例 4：使用火山引擎 Embedding + Codex VLM</b></summary>

运行 `openviking-server init` 并选择 `OpenAI Codex`，随后执行 `openviking-server doctor`。

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "embedding": {
    "dense": {
      "api_base" : "https://ark.cn-beijing.volces.com/api/v3",
      "api_key"  : "your-volcengine-api-key",
      "provider" : "volcengine",
      "dimension": 1024,
      "model"    : "doubao-embedding-vision-251215"
    }
  },
  "vlm": {
    "api_base" : "https://chatgpt.com/backend-api/codex",
    "provider" : "openai-codex",
    "model"    : "gpt-5.3-codex",
    "max_concurrent": 64
  }
}
```

</details>

#### 设置服务器配置文件环境变量

创建配置文件后，请设置环境变量指向该文件（Linux/macOS）：

```bash
export OPENVIKING_CONFIG_FILE=~/.openviking/ov.conf # by default
```

Windows 用户请使用以下任一方式：

PowerShell:

```powershell
$env:OPENVIKING_CONFIG_FILE = "$HOME/.openviking/ov.conf"
```

Command Prompt (cmd.exe):

```bat
set "OPENVIKING_CONFIG_FILE=%USERPROFILE%\.openviking\ov.conf"
```

> 💡 **提示**：你也可以将配置文件放置在其他位置，只需在环境变量中指定正确路径即可。

#### CLI/客户端配置示例

你可以通过 `ov config` 命令交互式初始化 CLI/客户端的配置。如果你有多个 OpenViking 服务器，也可以使用 `ov config switch` 命令切换至其他配置。

👇 展开查看你的 CLI/客户端配置示例：
<details>
<summary><b>示例：访问本地服务器的 ovcli.conf</b></summary>


```json
{
  "url": "http://localhost:1933",
  "timeout": 60.0
}
```

创建配置文件后，请设置环境变量指向该文件（Linux/macOS）：

```bash
export OPENVIKING_CLI_CONFIG_FILE=~/.openviking/ovcli.conf # by default
```

Windows 用户请使用以下任一方式：

PowerShell:

```powershell
$env:OPENVIKING_CLI_CONFIG_FILE = "$HOME/.openviking/ovcli.conf"
```

Command Prompt (cmd.exe):

```bat
set "OPENVIKING_CLI_CONFIG_FILE=%USERPROFILE%\.openviking\ovcli.conf"
```
</details>

### 4. 运行第一个示例

> 📝 **前置条件**：请确保已完成上一步的配置（ov.conf 和 ovcli.conf）。

现在，让我们运行一个完整的示例来体验 OpenViking 的核心功能。

#### 启动服务器

```bash
openviking-server doctor
openviking-server
```

如果你配置了 `provider=openai-codex`，运行 `openviking-server doctor` 即可验证 Codex 认证。

或后台启动：

```bash
nohup openviking-server > /data/log/openviking.log 2>&1 &
```

#### 运行 CLI

```bash
ov status
ov add-resource https://github.com/volcengine/OpenViking # --wait
ov ls viking://resources/
ov tree viking://resources/volcengine -L 2
# wait some time for semantic processing if not --wait
ov find "what is openviking"
ov grep "openviking" --uri viking://resources/volcengine/OpenViking/docs/zh
```

恭喜！你已成功运行 OpenViking 🎉

### VikingBot 快速开始

VikingBot 是一款基于 OpenViking 构建的 AI Agent 框架。使用步骤如下：

```bash
# Option 1: Install VikingBot from PyPI (recommended for most users)
pip install "openviking[bot]"

# Option 2: Install VikingBot from source (for development)
uv pip install -e ".[bot]"

# Start OpenViking server with Bot enabled
openviking-server --with-bot

# In another terminal, start interactive chat
ov chat
```

如果你使用官方 Docker 镜像，`vikingbot` 已内置其中，并默认随 OpenViking 服务器和控制台 UI 一同启动。你可以通过传递 `--without-bot` 参数或设置环境变量 `-e OPENVIKING_WITH_BOT=0` 在运行时禁用它。

***

## 服务端部署详情

在生产环境中，我们建议将 OpenViking 作为独立的 HTTP 服务运行，为你的 AI Agent 提供持久化、高性能的上下文支持。

🚀 **在云端部署 OpenViking**：
为确保最佳的存储性能与数据安全，我们建议在搭载 **veLinux** 操作系统的 **火山引擎云服务器（ECS）** 上进行部署。我们已准备详细的分步指南助你快速上手。

👉 **[查看：服务端部署与 ECS 设置指南](./docs/en/getting-started/03-quickstart-server.md)**

---

## 评测亮点

OpenViking 1.0 已在三个场景下完成评测：长对话用户记忆、Agent 经验记忆和知识库问答（QA）。

### 1. LoCoMo 基准测试中的用户记忆

在 LoCoMo 基准测试中，OpenViking 在多种 Agent 集成场景下提升了长上下文问答准确率，同时降低了延迟和 Token 消耗：

| Integration | Accuracy | Avg. Query Time | Total Input Tokens |
|:-----------:|---------:|----------------:|-------------------:|
| OpenClaw + native memory | 24.20% | 95.14s | 392,559,404 |
| OpenClaw + OpenViking | **82.08%** | 38.8s | 37,423,456 |
| Hermes native memory | 33.38% | 82.4s | 79,228,398 |
| Hermes + OpenViking | **82.86%** | **27.9s** | 52,026,755 |
| Claude Code auto-memory | 57.21% | 49.1s | 353,306,422 |
| Claude Code + OpenViking | **80.32%** | **20.4s** | 129,968,899 |

#### 1.1 关键效率提升

| Agent | Accuracy Improvement | Latency Reduction | Token Reduction |
|:-----:|---------------------:|------------------:|----------------:|
| OpenClaw | 24.20% → 82.08% (+3.39×) | -59.22% | **-91.0%** |
| Hermes | 33.38% → 82.86% (+2.48×) | -66.10% | -34.3% |
| Claude Code | 57.21% → 80.32% (+1.40×) | -58.45% | -63.2% |

### 2. tau2-bench 基准测试中的 Agent 经验记忆

在 tau2-bench 的多轮 Agent 任务中，OpenViking 的经验记忆提升了零售和航空领域的任务成功率：

| Setting | Retail Accuracy | Airline Accuracy |
|:-------:|----------------:|-----------------:|
| LLM without memory | 70.94% | 54.38% |
| LLM + OpenViking experience memory | **77.81%** (+6.87pp) | **66.25%** (+11.87pp) |

### 3. HotpotQA 基准测试中的知识库问答

在 HotpotQA 的多跳 RAG 任务中，将 OpenViking 的检索数量从 top-5 提升至 top-20，可在保持低延迟的同时获得该对比中的最高准确率：

| Method | Retrieval Pattern | Accuracy | Tokens / QA | Latency / QA |
|:------:|:-----------------:|---------:|------------:|-------------:|
| Naive RAG | Vector retrieval | 62.50% | 1,290 | **0.11s** |
| HippoRAG 2 | Vector + knowledge graph | 61.00% | 726 | 20s |
| LightRAG | Vector + knowledge graph | 89.00% | 28,443 | 75s |
| LangChain SQL (Agent) | SQL agent | 78.00% | 4,776 | 132s |
| OpenViking (top-5) | Vector retrieval | 72.75% | 3,154 | 0.22s |
| OpenViking (top-20) | Vector retrieval | **91.00%** | 12,533 | 0.23s |
| Nanobot + OpenViking (Agent) | Vector retrieval + Agent | 87.00% | 71,300 | 61.6s |

#### 3.1 跨 5 个开源数据集的单次 RAG 测试

| Method | Retrieval Pattern | Average Accuracy | Indexing Tokens | Tokens / QA | Retrieval Latency |
|:------:|:-----------------:|-----------------:|----------------:|------------:|------------------:|
| Naive RAG | Vector retrieval | 53.93% | 2,755,356 | 1,435 | **0.13s** |
| PageIndex | Vector + tree structure | 36.75% | 5,609,206 | 710,480 | 84.60s |
| HippoRAG 2 | Vector + knowledge graph | 44.50% | 124,963,618 | **637** | 18.83s |
| LightRAG | Vector + knowledge graph | **76.00%** | 62,705,469 | 27,035 | 9.19s |
| **OpenViking** | **Vector retrieval** | **66.87%** | **8,671,538** | **3,060** | **0.19s** |

> 数据集：FinanceBench、NaturalQuestions、ClapNQ、Qasper 和 SyllabusQA。OpenViking 以极低的检索延迟（0.19s）实现了 66.87% 的平均准确率，且索引成本仅为 LightRAG 的 13.8%。

---

## 学术支持

OpenViking 开源了论文《VikingMem》中所述核心能力的一部分，旨在让 AI Agent 开发者能够直接使用上下文数据库与记忆管理方案。

> **VikingMem: A Memory Base Management System for Stateful LLM-based Applications**
> Jiajie Fu, Junwen Chen, Mengzhao Wang, Aoxiang He, Maojia Sheng, Xiangyu Ke, Yifan Zhu, and Yunjun Gao.
> arXiv:2605.29640, 2026. Accepted by VLDB 2026.
>
> 📄 [在 arXiv 上阅读论文](https://arxiv.org/abs/2605.29640)

## 核心概念

运行完第一个示例后，让我们深入探讨 OpenViking 的设计理念。以下五个核心概念与前述解决方案一一对应，共同构建了一套完整的上下文管理系统：

### 1. 文件系统管理范式 → 解决碎片化

我们不再将上下文视为扁平的文本切片，而是将其统一抽象为虚拟文件系统。无论是记忆、资源还是能力，均映射至 `viking://` 协议下的虚拟目录中，并拥有唯一的 URI。

该范式赋予了 Agent 前所未有的上下文操作能力，使其能够像开发者一样通过标准命令（如 `ls`、`find`）精准、确定性地定位、浏览和操作信息。这将上下文管理从模糊的语义匹配转变为直观的“文件操作”。了解更多：[Viking URI](./docs/en/concepts/04-viking-uri.md) | [Context Types](./docs/en/concepts/02-context-types.md)

```
viking://
├── resources/              # Resources: project docs, repos, web pages, etc.
│   ├── my_project/
│   │   ├── docs/
│   │   │   ├── api/
│   │   │   └── tutorials/
│   │   └── src/
│   └── ...
├── user/                   # User: personal preferences, habits, etc.
│   └── memories/
│       ├── preferences/
│       │   ├── writing_style
│       │   └── coding_habits
│       └── ...
└── agent/                  # Agent: skills, instructions, task memories, etc.
    ├── skills/
    │   ├── search_code
    │   ├── analyze_data
    │   └── ...
    ├── memories/
    └── instructions/
```

### 2. 分层上下文加载 → 降低 Token 消耗

一次性将海量上下文塞入 Prompt 不仅成本高昂，还容易超出模型窗口并引入噪声。OpenViking 在写入时会自动将上下文处理为三个层级：

- **L0（摘要层）**：一句话总结，用于快速检索与识别。
- **L1（概览层）**：包含核心信息与使用场景，供 Agent 在规划阶段进行决策参考。
- **L2（详情层）**：完整原始数据，仅在必要时由 Agent 深度阅读。

了解更多：[Context Layers](./docs/en/concepts/03-context-layers.md)

```
viking://resources/my_project/
├── .abstract               # L0 Layer: Abstract (~100 tokens) - Quick relevance check
├── .overview               # L1 Layer: Overview (~2k tokens) - Understand structure and key points
├── docs/
│   ├── .abstract          # Each directory has corresponding L0/L1 layers
│   ├── .overview
│   ├── api/
│   │   ├── .abstract
│   │   ├── .overview
│   │   ├── auth.md        # L2 Layer: Full content - Load on demand
│   │   └── endpoints.md
│   └── ...
└── src/
    └── ...
```

### 3. 目录递归检索 → 提升检索效果

单一向量检索难以应对复杂的查询意图。OpenViking 设计了一种创新的**目录递归检索策略**，深度融合了多种检索方法：

1. **意图分析**：通过意图解析生成多个检索条件。
2. **初始定位**：利用向量检索快速定位包含初筛切片的高分目录。
3. **精细探索**：在该目录内进行二次检索，并将高分结果更新至候选集。
4. **递归下钻**：若存在子目录，则逐层递归重复上述二次检索步骤。
5. **结果聚合**：最终获取最相关的上下文并返回。

这种“先锁定高分目录，再精细探索内容”的策略不仅找到了语义最匹配的片段，还理解了信息所处的完整上下文，从而提升了检索的全局性与准确性。了解更多：[Retrieval Mechanism](./docs/en/concepts/07-retrieval.md)

### 4. 可视化检索轨迹 → 可观测的上下文

OpenViking 采用分层虚拟文件系统结构组织数据。所有上下文均以统一格式集成，每条记录对应唯一的 URI（如 `viking://` 路径），打破了传统扁平化的黑盒管理模式，层级清晰且易于理解。

检索过程采用目录递归策略。每次检索的目录浏览与文件定位轨迹均完整保留，你可以清晰观察问题根源并指导检索逻辑优化。了解更多：[Retrieval Mechanism](./docs/en/concepts/07-retrieval.md)

### 5. 自动会话管理 → 上下文自迭代

OpenViking 内置了记忆自迭代循环。每次会话结束时，你可主动触发记忆提取机制。系统将异步分析任务执行结果与用户反馈，并自动更新至 User 和 Agent 记忆目录中：

- **用户记忆更新**：同步偏好类记忆，使 Agent 响应更贴合你的需求。
- **Agent 经验积累**：从任务执行经验中提取操作技巧与工具使用心得，辅助后续任务的高效决策。

这使得 Agent 能够通过与世界交互实现“越用越聪明”，完成自我进化。了解更多：[Session Management](./docs/en/concepts/08-session.md)

***

## 进阶阅读

### 文档

如需更多详情，请访问我们的[完整文档](./docs/en/)。

### 社区与团队

详情请见：**[关于我们](./docs/en/about/01-about-us.md)**

### 加入社区

OpenViking 仍处于早期阶段，仍有诸多可优化与探索的空间。我们诚挚邀请每一位热爱 AI Agent 技术的开发者：

- 点亮一颗珍贵的 **Star**，给予我们持续前行的动力。
- 访问我们的 **[官网](https://www.openviking.ai)** 了解我们的理念，并通过 **[文档](https://www.openviking.ai/docs)** 将其应用于你的项目中。感受它带来的改变，并反馈你最真实的体验。
- 加入我们的社区分享见解、解答他人疑问，共同营造开放互助的技术氛围：
  - 📱 **飞书群**：扫码加入 → [查看二维码](./docs/en/about/01-about-us.md#lark-group)
  - 💬 **微信群**：扫码添加助手 → [查看二维码](./docs/en/about/01-about-us.md#wechat-group)
  - 🎮 **Discord**：[加入 Discord 服务器](https://discord.com/invite/eHvx8E9XF3)
  - 🐦 **X (Twitter)**：[关注我们](https://x.com/openvikingai)
- 成为 **贡献者（Contributor）**，无论是提交 Bug 修复还是新增功能，你的每一行代码都将成为 OpenViking 成长的重要基石。

让我们共同定义并构建 AI Agent 上下文管理的未来。旅程已启，期待你的参与！

### Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=volcengine/OpenViking\&type=timeline\&legend=top-left)](https://www.star-history.com/#volcengine/OpenViking\&type=timeline\&legend=top-left)

## 安全与隐私

本项目高度重视安全性。如需报告漏洞或查看支持的版本，请参阅 [SECURITY.md](SECURITY.md)。

## 许可证

OpenViking 项目对不同组件采用不同的许可证：

- **主项目**：AGPLv3 - 详见 [LICENSE](./LICENSE)
- **crates/ov_cli**：Apache 2.0 - 详见 [LICENSE](./crates/LICENSE)
- **examples**：Apache 2.0 - 详见 [LICENSE](./examples/LICENSE)
- **third_party**：遵循第三方项目的原始许可证

<!-- Link Definitions -->