<h1 align="center">请前往<a href="https://opcode.sh/">Opcode</a>查看，这是 Devika 的第二代版本。新版本即将发布！</h1>

---

<p align="center">
  <img src=".assets/devika-avatar.png" alt="Devika Logo" width="250">
</p>

<h1 align="center">🚀 Devika - 代理型 AI 软件工程师 👩‍💻</h1>

![devika screenshot](.assets/devika-screenshot.png)

> [!IMPORTANT]  
> 本项目目前处于非常早期的开发/实验阶段。当前有许多功能尚未实现或存在缺陷。欢迎贡献代码以帮助推进项目进展！

## Table of Contents

- [About](#about)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [How to use](#how-to-use)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Help and Support](#help-and-support)
- [License](#license)

## About

Devika 是一款先进的 AI 软件工程师，能够理解高级人类指令，将其分解为具体步骤，研究相关信息，并编写代码以实现给定目标。Devika 利用大语言模型、规划与推理算法以及网页浏览能力来智能地开发软件。

Devika 旨在通过提供一位只需极少人工指导即可承担复杂编码任务的 AI 结对编程伙伴，彻底革新我们的软件开发方式。无论你是需要创建新功能、修复 Bug，还是从零开始开发整个项目，Devika 都能为你提供协助。

> [!NOTE]
> Devika 的架构参考了 Cognition AI 开发的 [Devin](https://www.cognition-labs.com/introducing-devin)。本项目旨在成为 Devin 的开源替代方案，并怀揣一个“极其宏大”的目标：在 [SWE-bench](https://www.swebench.com/) 基准测试中达到与 Devin 相同的分数……甚至最终超越它？

## Demos

https://github.com/stitionai/devika/assets/26198477/cfed6945-d53b-4189-9fbe-669690204206

## Key Features

- 🤖 支持通过 [Ollama](https://ollama.com) 使用 **Claude 3**、**GPT-4**、**Gemini**、**Mistral**、**Groq** 以及**本地 LLM**。为获得最佳性能：建议使用 **Claude 3** 系列模型。
- 🧠 先进的 AI 规划与推理能力
- 🔍 基于上下文的关键词提取，实现精准研究
- 🌐 无缝网页浏览与信息收集
- 💻 支持多编程语言代码编写
- 📊 动态智能体状态追踪与可视化
- 💬 通过聊天界面进行自然语言交互
- 📂 基于项目的组织与管理
- 🔌 可扩展架构，便于添加新功能与集成

## System Architecture

详细文档请参阅 [**README.md**](docs/architecture)。


## Getting Started

### Requirements
```
Version's requirements
  - Python >= 3.10 and < 3.12
  - NodeJs >= 18
  - bun
```

- 安装 uv（Python 包管理器）[下载地址](https://github.com/astral-sh/uv)
- 安装 bun（JavaScript 运行时）[下载地址](https://bun.sh/docs/installation)
- 如需使用 Ollama，请参考 [Ollama 设置指南](docs/Installation/ollama.md)（可选：若不使用本地模型可跳过此步）
- 对于 API 模型，请通过 UI 中的设置页面配置相应的 API 密钥。


### Installation

要安装 Devika，请按以下步骤操作：

1. 克隆 Devika 代码仓库：
   ```bash
   git clone https://github.com/stitionai/devika.git
   ```
2. 进入项目目录：
   ```bash
   cd devika
   ```
3. 创建虚拟环境并安装所需依赖（可使用任意虚拟环境管理器）：
   ```bash
   uv venv
   
   # On macOS and Linux.
   source .venv/bin/activate

   # On Windows.
   .venv\Scripts\activate

   uv pip install -r requirements.txt
   ```
4. 安装 Playwright 以启用浏览器功能：
   ```bash
   playwright install --with-deps # installs browsers in playwright (and their deps) if required
   ```
5. 启动 Devika 服务器：
   ```bash
   python devika.py
   ```
6. 若一切正常，你将看到以下输出：
   ```bash
   root: INFO   : Devika is up and running!
   ```
7. 接下来配置前端，打开新终端并进入 `ui` 目录：
   ```bash
   cd ui/
   bun install
   bun run start
   ```
8. 在浏览器中访问 `http://127.0.0.1:3001` 即可使用 Devika Web 界面。

### how to use

要开始使用 Devika，请按以下步骤操作：

1. 在浏览器中打开 Devika Web 界面。
2. 创建项目：点击“Select Project”（选择项目），然后点击“New Project”（新建项目）。
3. 为项目选择搜索引擎和模型配置。
4. 在聊天界面中，输入高级目标或任务描述供 Devika 处理。
5. Devika 将处理你的请求，将其分解为步骤并开始执行任务。
6. 监控 Devika 的进度，查看生成的代码，并根据需要提供额外指导或反馈。
7. Devika 完成任务后，审查生成的代码和项目文件。
8. 通过提供进一步指令或修改意见，迭代并完善项目。

## Configuration

正常运行 Devika 需要特定的配置设置和 API 密钥：

首次运行 Devika 时，它会在根目录为你创建一个 `config.toml` 文件。你可以通过 UI 中的设置页面配置以下选项：

- **API KEYS**
   - `BING`: 用于网页搜索功能的 Bing 搜索 API 密钥。
   - `GOOGLE_SEARCH`: 用于网页搜索功能的 Google 搜索 API 密钥。
   - `GOOGLE_SEARCH_ENGINE_ID`: 使用 Google 进行网页搜索的搜索引擎 ID。
   - `OPENAI`: 用于访问 GPT 模型的 OpenAI API 密钥。
   - `GEMINI`: 用于访问 Gemini 模型的 Gemini API 密钥。
   - `CLAUDE`: 用于访问 Claude 模型的 Anthropic API 密钥。
   - `MISTRAL`: 用于访问 Mistral 模型的 Mistral API 密钥。
   - `GROQ`: 用于访问 Groq 模型的 Groq API 密钥。
   - `NETLIFY`: 用于部署和管理 Web 项目的 Netlify API 密钥。

- **API_ENDPOINTS**
   - `BING`: 用于网页搜索的 Bing API 端点。
   - `GOOGLE`: 用于网页搜索的 Google API 端点。
   - `OLLAMA`: 用于访问本地 LLM 的 Ollama API 端点。
   - `OPENAI`: 用于访问 OpenAI 模型的 OpenAI API 端点。

请妥善保管你的 API 密钥，切勿公开分享。如需设置 Bing 和 Google 搜索 API 密钥，请参阅 [搜索引擎设置指南](docs/Installation/search_engine.md)。


## Contributing

我们欢迎各方贡献以增强 Devika 的功能并提升其性能。如需参与贡献，请查看 [`CONTRIBUTING.md`](CONTRIBUTING.md) 文件中的详细步骤。

## Help and Support

如果你有任何问题、反馈或建议，欢迎随时联系我们。你可以在 [Issue 追踪器](https://github.com/stitionai/devika/issues) 中提交问题，或加入 [讨论区](https://github.com/stitionai/devika/discussions) 参与一般性交流。

我们还设有 Devika 社区 Discord 服务器，你可以在这里与其他用户建立联系、分享经验、提问并协作开发项目。要加入 Devika 社区 Discord 服务器，[点击此处](https://discord.gg/CYRp43878y)。

## License

Devika 基于 [MIT 许可证](https://opensource.org/licenses/MIT) 发布。更多信息请参阅 `LICENSE` 文件。

## Star History

<div align="center">
<a href="https://star-history.com/#stitionai/devika&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=stitionai/devika&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=stitionai/devika&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=stitionai/devika&type=Date" />
 </picture>
</a>
</div>

---

我们希望 Devika 能成为你软件开发旅程中的得力助手。如果你有任何问题、反馈或建议，欢迎随时联系我们。祝使用 Devika 编码愉快！