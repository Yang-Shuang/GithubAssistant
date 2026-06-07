# AIChat：一站式 LLM CLI 工具

[![CI](https://github.com/sigoden/aichat/actions/workflows/ci.yaml/badge.svg)](https://github.com/sigden/aichat/actions/workflows/ci.yaml)
[![Crates](https://img.shields.io/crates/v/aichat.svg)](https://crates.io/crates/aichat)
[![Discord](https://img.shields.io/discord/1226737085453701222?label=Discord)](https://discord.gg/mr3ZZUB9hG)

AIChat 是一款集 Shell 助手、CMD 与 REPL 模式、RAG（检索增强生成）、AI 工具与智能体等功能于一体的全功能 LLM CLI 工具。 

## 安装

### 包管理器

- **Rust 开发者：** `cargo install aichat`
- **Homebrew/Linuxbrew 用户：** `brew install aichat`
- **Pacman 用户**：`pacman -S aichat`
- **Windows Scoop 用户：** `scoop install aichat`
- **Android Termux 用户：** `pkg install aichat`

### 预构建版本

从 [GitHub Releases](https://github.com/sigden/aichat/releases) 下载适用于 macOS、Linux 和 Windows 的预编译二进制文件，解压后将 `aichat` 可执行文件添加到你的 `$PATH` 环境变量中。

## 核心功能

### 多模型支持

通过统一的接口无缝集成超过 20 家主流 LLM 提供商。支持的提供商包括 OpenAI、Claude、Gemini（Google AI Studio）、Ollama、Groq、Azure-OpenAI、VertexAI、Bedrock、Github Models、Mistral、Deepseek、AI21、XAI Grok、Cohere、Perplexity、Cloudflare、OpenRouter、Ernie、Qianwen、Moonshot、ZhipuAI、MiniMax、Deepinfra、VoyageAI，以及任何兼容 OpenAI 的 API 提供商。

### CMD 模式

体验 AIChat 强大的命令行功能（CMD 模式）。

![aichat-cmd](https://github.com/user-attachments/assets/6c58c549-1564-43cf-b772-e1c9fe91d19c)

### REPL 模式

享受交互式 Chat-REPL 体验，支持 Tab 自动补全、多行输入、历史记录搜索、可配置快捷键以及自定义 REPL 提示符等功能。

![aichat-repl](https://github.com/user-attachments/assets/218fab08-cdae-4c3b-bcf8-39b6651f1362)

### Shell 助手

提升你的命令行操作效率。使用自然语言描述任务，让 AIChat 将其转换为精准的 Shell 命令。AIChat 会智能适配你的操作系统和 Shell 环境。

![aichat-execute](https://github.com/user-attachments/assets/0c77e901-0da2-4151-aefc-a2af96bbb004)

### 多样化输入方式

支持多种输入形式，包括标准输入（stdin）、本地文件与目录、远程 URL 等，灵活处理各类数据。

| 输入类型          | CMD                                  | REPL                             |
| ----------------- | ------------------------------------ | -------------------------------- |
| CMD               | `aichat hello`                       |                                  |
| STDIN             | `cat data.txt \| aichat`             |                                  |
| 上次回复          |                                      | `.file %%`                       |
| 本地文件          | `aichat -f image.png -f data.txt`    | `.file image.png data.txt`       |
| 本地目录          | `aichat -f dir/`                     | `.file dir/`                     |
| 远程 URL          | `aichat -f https://example.com`      | `.file https://example.com`      |
| 外部命令          | ```aichat -f '`git diff`'```         | ```.file `git diff` ```          |
| 组合输入          | `aichat -f dir/ -f data.txt explain` | `.file dir/ data.txt -- explain` |

### 角色（Role）

自定义角色以定制 LLM 的行为模式，提升交互效率并增强生产力。

![aichat-role](https://github.com/user-attachments/assets/023df6d2-409c-40bd-ac93-4174fd72f030)

> 角色由提示词（prompt）和模型配置组成。

### 会话（Session）

通过会话功能保持上下文感知的对话，确保交互的连续性。

![aichat-session](https://github.com/user-attachments/assets/56583566-0f43-435f-95b3-730ae55df031)

> 左侧使用了会话（Session），右侧未使用会话。

### 宏（Macro）

将一系列 REPL 命令组合成自定义宏，简化重复性任务的操作流程。

![aichat-macro](https://github.com/user-attachments/assets/23c2a08f-5bd7-4bf3-817c-c484aa74a651)

### RAG（检索增强生成）

将外部文档集成到 LLM 对话中，获取更准确且符合上下文的回复。

![aichat-rag](https://github.com/user-attachments/assets/359f0cb8-ee37-432f-a89f-96a2ebab01f6)

### 函数调用（Function Calling）

通过连接外部工具和数据源，函数调用大幅增强了 LLM 的能力。这解锁了无限可能，使 LLM 能够超越核心能力范围，处理更广泛的任务。

我们创建了新的仓库 [https://github.com/sigoden/llm-functions](https://github.com/sigden/llm-functions)，帮助你充分利用此功能。

#### AI 工具与 MCP

集成外部工具，直接在现有工作流中自动化任务、检索信息并执行操作。

![aichat-tool](https://github.com/user-attachments/assets/7459a111-7258-4ef0-a2dd-624d0f1b4f92)

#### AI 智能体（OpenAI GPTs 的 CLI 版本）

AI 智能体 = 指令（Prompt）+ 工具（函数调用）+ 文档（RAG）。

![aichat-agent](https://github.com/user-attachments/assets/0b7e687d-e642-4e8a-b1c1-d2d9b2da2b6b)

### 本地服务器功能

AIChat 内置轻量级 HTTP 服务器，便于快速部署。

```
$ aichat --serve
Chat Completions API: http://127.0.0.1:8000/v1/chat/completions
Embeddings API:       http://127.0.0.1:8000/v1/embeddings
Rerank API:           http://127.0.0.1:8000/v1/rerank
LLM Playground:       http://127.0.0.1:8000/playground
LLM Arena:            http://127.0.0.1:8000/arena?num=2
```

#### 代理 LLM API

LLM Arena（竞技场）是一个基于 Web 的平台，你可以在其中并排比较不同的 LLM。 

使用 curl 进行测试：

```sh
curl -X POST -H "Content-Type: application/json" -d '{
  "model":"claude:claude-3-5-sonnet-20240620",
  "messages":[{"role":"user","content":"hello"}], 
  "stream":true
}' http://127.0.0.1:8000/v1/chat/completions
```

#### LLM Playground

一个 Web 应用程序，允许你直接在浏览器中与支持的 LLM 进行交互。

![aichat-llm-playground](https://github.com/user-attachments/assets/aab1e124-1274-4452-b703-ef15cda55439)

#### LLM Arena

一个用于并排比较不同 LLM 的 Web 平台。

![aichat-llm-arena](https://github.com/user-attachments/assets/edabba53-a1ef-4817-9153-38542ffbfec6)

## 自定义主题

AIChat 支持自定义深色和浅色主题，可高亮显示回复文本与代码块。

![aichat-themes](https://github.com/sigoden/aichat/assets/4012553/29fa8b79-031e-405d-9caa-70d24fa0acf8)

## 文档

- [Chat-REPL 指南](https://github.com/sigoden/aichat/wiki/Chat-REPL-Guide)
- [命令行使用指南](https://github.com/sigden/aichat/wiki/Command-Line-Guide)
- [角色配置指南](https://github.com/sigden/aichat/wiki/Role-Guide)
- [宏功能指南](https://github.com/sigden/aichat/wiki/Macro-Guide)
- [RAG 使用指南](https://github.com/sigden/aichat/wiki/RAG-Guide)
- [环境变量说明](https://github.com/sigden/aichat/wiki/Environment-Variables)
- [配置指南](https://github.com/sigden/aichat/wiki/Configuration-Guide)
- [自定义主题](https://github.com/sigden/aichat/wiki/Custom-Theme)
- [自定义 REPL 提示符](https://github.com/sigden/aichat/wiki/Custom-REPL-Prompt)
- [常见问题解答 (FAQ)](https://github.com/sigden/aichat/wiki/FAQ)

## 开源协议

Copyright (c) 2023-2025 aichat-developers.

AIChat 遵循双许可协议，你可根据需要选择使用 MIT License 或 Apache License 2.0。

有关详细条款，请参阅 LICENSE-APACHE 和 LICENSE-MIT 文件。