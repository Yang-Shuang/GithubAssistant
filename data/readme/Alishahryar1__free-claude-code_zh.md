<div align="center">

# 🤖 Free Claude Code

通过你自己的 Anthropic 兼容代理，使用 Claude Code CLI、VS Code、JetBrains ACP 或聊天机器人。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.14](https://img.shields.io/badge/python-3.14-3776ab.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=for-the-badge)](https://github.com/astral-sh/uv)
[![Tested with Pytest](https://img.shields.io/badge/testing-Pytest-00c0ff.svg?style=for-the-badge)](https://github.com/Alishahryar1/free-claude-code/actions/workflows/tests.yml)
[![Type checking: Ty](https://img.shields.io/badge/type%20checking-ty-ffcc00.svg?style=for-the-badge)](https://pypi.org/project/ty/)
[![Code style: Ruff](https://img.shields.io/badge/code%20formatting-ruff-f5a623.svg?style=for-the-badge)](https://github.com/astral-sh/ruff)
[![Logging: Loguru](https://img.shields.io/badge/logging-loguru-4ecdc4.svg?style=for-the-badge)](https://github.com/Delgan/loguru)

Free Claude Code 将来自 Claude Code 的 Anthropic Messages API 流量路由到任意提供商（Provider）。它保持 Claude Code 客户端协议稳定，同时让你可以选择免费、付费或本地模型。

[快速开始](#quick-start) · [提供商配置](#choose-a-provider) · [连接 Claude Code](#connect-claude-code) · [可选集成](#optional-integrations) · [开发指南](#development)

</div>

<div align="center">
  <img src="assets/pic.png" alt="Free Claude Code in action" width="700">
</div>

<a id="model-picker"></a>

<div align="center">
  <img src="assets/cc-model-picker.png" alt="Claude Code model picker showing gateway models" width="700">
</div>

## ⭐ Star 历史

<div align="center">
  <a href="https://star-history.com/#Alishahryar1/free-claude-code&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Alishahryar1/free-claude-code&type=Date&theme=dark">
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Alishahryar1/free-claude-code&type=Date">
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Alishahryar1/free-claude-code&type=Date" width="700">
    </picture>
  </a>
</div>

## ✨ 核心功能

- 无缝替换 Claude Code 的 Anthropic API 调用代理。
- 支持 17 个提供商后端：NVIDIA NIM、OpenRouter、Google AI Studio (Gemini)、DeepSeek、Mistral La Plateforme、Mistral Codestral、OpenCode Zen、OpenCode Go、Wafer、Kimi、Cerebras Inference、Groq、Fireworks AI、Z.ai、LM Studio、llama.cpp 和 Ollama。
- 按模型路由：将 Opus、Sonnet、Haiku 及回退流量发送到不同的提供商。
- 通过代理的 `/v1/models` 端点原生支持 Claude Code `/model` 选择器（Claude Code 需开启网关模型发现功能；详见 [Model Picker](#model-picker)）。
- 支持流式传输（Streaming）、工具调用、思考/推理块处理及本地请求优化。
- 可选的 Discord 或 Telegram 机器人包装器，用于远程编程会话。
- 通过 VS Code 扩展实现用量统计（可选）。
- 支持通过本地 Whisper 或 NVIDIA NIM 进行语音笔记转录（可选）。
- 提供位于 `/admin` 的本地 **管理界面（Admin UI）**，用于编辑受管代理配置、验证更改并检查提供商状态（仅限回环访问）。

## 🚀 快速开始

### 1. 安装/更新代理

macOS/Linux:

```bash
curl -fsSL "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh?raw=1" | sh
```

Windows PowerShell:

```powershell
irm "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1?raw=1" | iex
```

请查看 [scripts/install.sh](https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh) 和 [scripts/install.ps1](https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1) 中的安装脚本。重新运行这些命令即可更新到最新版本。

### 2. 启动代理

```bash
fcc-server
```

启动后，Uvicorn 会打印代理绑定地址，应用日志会显示管理界面 URL：

```text
INFO:     Admin UI: http://127.0.0.1:8082/admin (local-only)
```

许多终端支持点击链接。如果端口不是默认的 `8082`，请使用你配置的 `PORT`。

### 3. 打开管理界面并配置 NVIDIA NIM

从终端输出中复制 **管理界面（Admin UI）** URL 并在浏览器中打开。

需要 NVIDIA NIM API 密钥吗？请参阅下方的 **[NVIDIA NIM 提供商](#nvidia-nim-provider)** 章节，然后返回此处继续操作。

<div align="center">
  <img src="assets/admin-page.png" alt="Local admin UI for proxy settings" width="700">
</div>

将你的 NVIDIA NIM API 密钥粘贴到 `NVIDIA_NIM_API_KEY` 字段中，然后点击 **Validate（验证）** 和 **Apply（应用）**。

默认模型已设置为 `nvidia_nim/nvidia/nemotron-3-super-120b-a12b`。你稍后可在同一管理界面中更改它。

### 4. 运行 Claude Code

```bash
fcc-claude
```

`fcc-claude` 每次启动时都会读取当前配置的端口和认证令牌，设置 Claude Code 环境变量（包括用于自动压缩的 190k token 的 `CLAUDE_CODE_AUTO_COMPACT_WINDOW`），然后启动真实的 `claude` 命令。

## ⚙️ 选择提供商

选择一个提供商，在管理界面中输入其密钥或本地 URL，并将 `MODEL` 设置为带提供商前缀的模型标识符（slug）。`MODEL` 为回退默认值。`MODEL_OPUS`、`MODEL_SONNET` 和 `MODEL_HAIKU` 可覆盖 Claude Code 不同模型层级的路由策略。

<a id="nvidia-nim-provider"></a>

### 1. [NVIDIA NIM](https://build.nvidia.com/)

在 [build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys) 获取密钥。

在管理界面中，将其粘贴到 `NVIDIA_NIM_API_KEY`。默认 `MODEL` 为 `nvidia_nim/nvidia/nemotron-3-super-120b-a12b`。

常用示例：
- `nvidia_nim/nvidia/nemotron-3-super-120b-a12b`
- `nvidia_nim/z-ai/glm5.1`
- `nvidia_nim/moonshotai/kimi-k2.5`
- `nvidia_nim/minimaxai/minimax-m2.5`

在 [build.nvidia.com](https://build.nvidia.com/explore/discover) 浏览模型。

### 2. [OpenRouter](https://openrouter.ai/)

在 [openrouter.ai/keys](https://openrouter.ai/keys) 获取密钥。

在管理界面中，将其粘贴到 `OPENROUTER_API_KEY`，然后设置 `MODEL` 为 OpenRouter 标识符如 `open_router/openrouter/free`。

浏览[所有模型](https://openrouter.ai/models)或[免费模型](https://openrouter.ai/collections/free-models)。

### 3. [Google AI Studio (Gemini)](https://aistudio.google.com/)

在 [Google AI Studio](https://aistudio.google.com/apikey) 获取 Gemini API 密钥（参见 Google 的[Gemini OpenAI 兼容文档](https://ai.google.dev/gemini-api/docs/openai)）。

在管理界面中，将其粘贴到 `GEMINI_API_KEY`，然后设置 `MODEL` 为 Gemini 模型标识符如 `gemini/models/gemini-3.1-flash-lite`。

Gemini API 在 `https://generativelanguage.googleapis.com/v1beta/openai/` 提供 OpenAI 兼容端点。免费层配额按模型计算；除非你的账户区域另有说明，否则提示词可能被用于改进 Google 的产品（英国/瑞士/欧洲经济区/欧盟除外）——详见 Google 条款。

常用示例：
- `gemini/models/gemini-3.1-flash-lite`

### 4. [DeepSeek](https://platform.deepseek.com/)

在 [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys) 获取密钥。

在管理界面中，将其粘贴到 `DEEPSEEK_API_KEY`，然后设置 `MODEL` 为 DeepSeek 标识符如 `deepseek/deepseek-chat`。

此提供商使用 DeepSeek 的 Anthropic 兼容端点，而非 OpenAI chat-completions 端点。

### 5. [Mistral La Plateforme](https://console.mistral.ai/)

[Mistral](https://mistral.ai) 在 `https://api.mistral.ai/v1` 托管了 OpenAI 兼容的 Chat Completions API。在 [console.mistral.ai](https://console.mistral.ai/) 上激活 **Experiment** 计划以获取免费层 API 访问权限（有速率限制；升级可提高配额）。

在管理界面中，将你的 API 密钥粘贴到 `MISTRAL_API_KEY`，然后设置 `MODEL` 为 Mistral 模型标识符如 `mistral/devstral-small-latest` 或 `mistral/mistral-small-latest`。

常用示例：
- `mistral/devstral-small-latest`
- `mistral/mistral-small-latest`

在 [Mistral 文档](https://docs.mistral.ai/) 浏览模型。

### 6. [Mistral Codestral](https://console.mistral.ai/)

Mistral 的 **Codestral** 网关使用与 La Plateforme **不同的 API 密钥**：配置 `CODESTRAL_API_KEY`，然后使用 `mistral_codestral/` 前缀进行路由。默认上游为 **`https://codestral.mistral.ai/v1`**（OpenAI 兼容 Chat Completions；请求格式与 `mistral` 提供商相同）。参见 Mistral 的[编程/FIM 领域文档](https://docs.mistral.ai/mistral-vibe/using-fim-api)；精选的[免费 LLM API 列表](https://github.com/cheahjs/free-llm-api-resources#mistral-codestral)总结了典型的 Codestral 访问条款。

常用示例：
- `mistral_codestral/codestral-latest`

### 7. [OpenCode Zen](https://opencode.ai/)

在 [opencode.ai/auth](https://opencode.ai/auth) 获取 API 密钥。

在管理界面中，将其粘贴到 `OPENCODE_API_KEY`，然后设置 `MODEL` 为 OpenCode Zen 模型标识符如 `opencode/gpt-5.3-codex`。相同的 `OPENCODE_API_KEY` 也用于下方的 **OpenCode Go**；在那里请使用 `opencode_go/` 前缀的标识符。

OpenCode Zen 是一个精选模型网关，通过单个 API 密钥和位于 `https://opencode.ai/zen/v1` 的 OpenAI 兼容端点提供对 Anthropic、OpenAI、Google、DeepSeek 等模型的访问。

常用示例：
- `opencode/gpt-5.3-codex`
- `opencode/claude-sonnet-4`
- `opencode/deepseek-v4-flash-free` (免费)
- `opencode/gemini-3-flash`
- `opencode/big-pickle` (免费)
- `opencode/glm-5.1`

在 [opencode.ai](https://opencode.ai) 浏览可用模型。

### 8. [OpenCode Go](https://opencode.ai/)

在 [opencode.ai/auth](https://opencode.ai/auth) 获取 API 密钥（与 OpenCode Zen 相同）。

在管理界面中，使用 `OPENCODE_API_KEY`，然后设置 `MODEL` 为 OpenCode Go 模型标识符如 `opencode_go/minimax-m2.7`。

OpenCode Go 是带有独立精选目录的订阅网关，在 `https://opencode.ai/zen/go/v1` 提供 OpenAI 兼容端点。它与 Zen **共享相同的 OpenCode API 密钥**；仅标识符前缀（`opencode_go/` vs `opencode/`）和上游路径不同。

常用示例：
- `opencode_go/minimax-m2.7`

在 [opencode.ai](https://opencode.ai) 浏览可用模型。

### 9. [Wafer](https://wafer.ai/)

从 [wafer.ai](https://wafer.ai) 获取密钥。在管理界面中，将其粘贴到 `WAFER_API_KEY`，然后设置 `MODEL` 为 Wafer Pass 模型如 `wafer/DeepSeek-V4-Pro`。

常用示例：
- `wafer/DeepSeek-V4-Pro`
- `wafer/MiniMax-M2.7`
- `wafer/Qwen3.5-397B-A17B`
- `wafer/GLM-5.1`

此提供商使用位于 `https://pass.wafer.ai/v1/messages` 的 Wafer Anthropic 兼容端点。

### 10. [Kimi](https://platform.moonshot.ai/)

在 [platform.moonshot.ai/console/api-keys](https://platform.moonshot.ai/console/api-keys) 获取密钥。

在管理界面中，将其粘贴到 `KIMI_API_KEY`，然后设置 `MODEL` 为 Kimi 标识符如 `kimi/kimi-k2.5`。

此提供商调用 Kimi 的 **Anthropic 兼容** Messages API（`https://api.moonshot.ai/anthropic/v1/messages`; 模型发现使用 OpenAI 兼容 `GET https://api.moonshot.ai/v1/models`）。它**不是** OpenAI Chat Completions 路径。

在 [platform.moonshot.ai](https://platform.moonshot.ai) 浏览模型。

### 11. [Cerebras Inference](https://inference-docs.cerebras.ai/quickstart)

在 [Cerebras Cloud Console](https://cloud.cerebras.ai) 注册并创建 API 密钥（参见[快速入门](https://inference-docs.cerebras.ai/quickstart)）。

在管理界面中，设置 `CEREBRAS_API_KEY`，然后使用 `MODEL` 如 `cerebras/llama3.1-8b` 或 `cerebras/gpt-oss-120b`（ID 来自[列出模型](https://inference-docs.cerebras.ai/api-reference/models/list-models)）。

Cerebras 在 `https://api.cerebras.ai/v1` 暴露了 OpenAI 兼容 API（[OpenAI 兼容性说明](https://inference-docs.cerebras.ai/resources/openai)）。非标准请求字段在使用 OpenAI 客户端时应放入 `extra_body`；详见同一页面。对于推理模型和参数，参见[推理功能](https://inference-docs.cerebras.ai/capabilities/reasoning)。当启用 Claude 风格思考时，本代理通过 `reasoning_content` 遵循其他 OpenAI 兼容适配器的思考实现。

### 12. [Groq](https://console.groq.com/)

在 [console.groq.com/keys](https://console.groq.com/keys) 获取 API 密钥。

在管理界面中，将其粘贴到 `GROQ_API_KEY`，然后设置 `MODEL` 为 Groq OpenAI 兼容模型标识符如 `groq/llama-3.3-70b-versatile`。

Groq 通过 `https://api.groq.com/openai/v1` 路由（[OpenAI 兼容 Chat Completions](https://console.groq.com/docs/openai)）。部分请求字段会导致 HTTP 400；此适配器会剥离已知不支持的请求格式（记录在 Groq 的兼容性说明中）。

重度推理模型暴露了额外参数，详见[Groq 推理文档](https://console.groq.com/docs/reasoning)。当启用 Claude 风格思考时，本发行版通过 `reasoning_content` delta 镜像其他 OpenAI 兼容适配器的思考功能；你可在需要时通过请求 `extra_body` 调整高级参数。

在 [console.groq.com/docs/models](https://console.groq.com/docs/models) 浏览模型。

### 13. [Fireworks AI](https://fireworks.ai/)

在 [fireworks.ai/account/api-keys](https://fireworks.ai/account/api-keys) 获取 API 密钥。

在管理界面中，将其粘贴到 `FIREWORKS_API_KEY`，然后设置 `MODEL` 为 Fireworks 模型标识符如 `fireworks/accounts/fireworks/models/llama-v3p3-70b-instruct`。

Fireworks 在 `https://api.fireworks.ai/inference/v1/messages` 暴露了**Anthropic 兼容** Messages API（此处不使用 Chat Completions）。当允许时，供应商特定的 JSON 键仍可从请求 `extra_body` 合并。

在 [fireworks.ai/models](https://fireworks.ai/models) 浏览模型。

### 14. [Z.ai](https://z.ai/)

在 [Z.ai/manage-apikey/apikey-list](https://z.ai/manage-apikey/apikey-list) 获取 API 密钥。

在管理界面中，将其粘贴到 `ZAI_API_KEY`，然后设置 `MODEL` 为 Z.ai 模型标识符如 `zai/glm-5.1`。

此提供商调用 Z.ai 的 **Anthropic 兼容** Messages API（`https://api.z.ai/api/anthropic/v1/messages`）。前 OpenAI Coding Plan 基础端点（`https://api.z.ai/api/coding/paas/v4`）**未**被本网关使用。

常用示例：
- `zai/glm-5.1`
- `zai/glm-5-turbo`

在 [Z.ai](https://z.ai) 浏览模型。

### 15. [LM Studio](https://lmstudio.ai/)

启动 LM Studio 的本地服务器并加载模型。在管理界面中，保留或更新 `LM_STUDIO_BASE_URL`，然后设置 `MODEL` 为 LM Studio 显示的模型标识符（带 `lmstudio/` 前缀）。

优先选择支持工具调用的模型以适配 Claude Code 工作流。

### 16. [llama.cpp](https://github.com/ggml-org/llama.cpp)

启动带有 Anthropic 兼容 `/v1/messages` 端点且上下文足够大的 `llama-server`，以满足 Claude Code 请求需求。

在管理界面中，保留或更新 `LLAMACPP_BASE_URL`，然后设置 `MODEL` 为本地模型标识符（带 `llamacpp/` 前缀）。

对于本地编程模型，上下文大小至关重要。如果 llama.cpp 对常规 Claude Code 请求返回 HTTP 400，请增加 `--ctx-size` 并验证模型/服务器构建是否支持所请求的功能。

### 17. [Ollama](https://ollama.com/)

运行 Ollama 并拉取模型：

```bash
ollama pull llama3.1
ollama serve
```

在管理界面中，保留或更新 `OLLAMA_BASE_URL`，然后设置 `MODEL` 为与 `ollama list` 显示的标签相同的标识符（带 `ollama/` 前缀）。

`OLLAMA_BASE_URL` 是 Ollama 服务器根目录；请勿追加 `/v1`。示例模型标识符包括 `ollama/llama3.1` 和 `ollama/llama3.1:8b`。

### 18. 按模型层级混合提供商

每个模型层级都可以通过设置管理界面中的 `MODEL_OPUS`、`MODEL_SONNET` 和 `MODEL_HAIKU` 来使用不同的提供商。将某个层级留空则继承 `MODEL`。

例如，你可以将 Opus 路由到 `nvidia_nim/moonshotai/kimi-k2.6`，Sonnet 到 `open_router/openrouter/free`，Haiku 到 `lmstudio/qwen3.5-coder`，并将回退 `MODEL` 保持在 `zai/glm-5.1`。

## 🔗 连接 Claude Code

### 1. Claude Code CLI

终端使用推荐安装好的启动器：

```bash
fcc-claude
```

工作时请保持 `fcc-server` 运行。管理界面用于管理代理配置，在运行时设置更改时重启服务器，且 `fcc-claude` 每次启动都会读取当前由管理界面管理的端口和认证令牌。它还会将 `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 设置为 `190000` 以启用自动压缩。

### 2. VS Code Extension

打开设置，搜索 `claude-code.environmentVariables`，选择 **Edit in settings.json**，并添加：

```json
"claudeCode.environmentVariables": [
  { "name": "ANTHROPIC_BASE_URL", "value": "http://localhost:8082" },
  { "name": "ANTHROPIC_AUTH_TOKEN", "value": "freecc" },
  { "name": "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY", "value": "1" },
  { "name": "CLAUDE_CODE_AUTO_COMPACT_WINDOW", "value": "190000" }
]
```

重新加载扩展。如果扩展显示登录界面，请选择 Anthropic Console 路径一次；环境变量生效后，本地代理仍会处理模型流量。

### 3. JetBrains ACP

编辑已安装的 Claude ACP 配置：

- Windows: `C:\Users\%USERNAME%\AppData\Roaming\JetBrains\acp-agents\installed.json`
- Linux/macOS: `~/.jetbrains/acp.json`

为 `acp.registry.claude-acp` 设置环境变量：

```json
"env": {
  "ANTHROPIC_BASE_URL": "http://localhost:8082",
  "ANTHROPIC_AUTH_TOKEN": "freecc",
  "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1",
  "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "190000"
}
```

修改文件后重启 IDE。

## 🔌 可选集成

对于以下所有集成，仅在 `/admin` 的 **管理界面（Admin UI）** 中更改**受管代理配置**：编辑字段，点击 **Validate（验证）**，然后 **Apply（应用）**。页脚会显示受管配置的存储位置；本 README 不介绍手动编辑该文件的步骤。

### 1. Discord 和 Telegram 机器人

机器人包装器支持远程运行 Claude Code 会话、流式传输进度、基于回复的对话分支，并支持停止或清除任务。

**Discord**
1. 在 [Discord Developer Portal](https://discord.com/developers/applications) 创建机器人。
2. 启用 **Message Content Intent**。
3. 邀请机器人并赋予读取消息、发送消息和查看历史记录的权限。
4. 复制机器人令牌（Bot Token）以及机器人应回复的频道 ID（或 IDs）。

**Telegram**
1. 通过 [@BotFather](https://t.me/BotFather) 创建机器人并复制令牌。
2. 从 [@userinfobot](https://t.me/userinfobot) 获取你的数字用户 ID，以便仅允许你使用此机器人。

**在管理界面中配置**
1. `fcc-server` 运行时，打开终端输出中的 **管理界面（Admin UI）** URL。
2. 在侧边栏中选择 **Messaging**。
3. 将 **Messaging Platform** 设置为 **discord** 或 **telegram**。
4. Discord 粘贴 **Discord Bot Token** 和 **Allowed Discord Channels**；Telegram 粘贴 **Telegram Bot Token** 和 **Allowed Telegram User ID**。
5. 设置 **Allowed Directory** 为运行代理的机器上的绝对路径（机器人可使用的根工作区）。
6. 点击 **Validate**，然后 **Apply**。如果界面提示需要重启服务器则执行。

<div align="center">
  <img src="assets/admin-messaging.png" alt="Admin UI Messaging view with bot and voice settings" width="700">
</div>

<p align="center"><em>管理界面 → Messaging（平台、机器人和语音）</em></p>

**常用命令**
- `/stop` 取消任务；回复特定任务消息仅停止该分支。
- `/clear` 重置会话；回复以清除单个分支。
- `/stats` 显示会话状态。

### 2. 语音笔记（Voice Notes）

在 [Free Claude Code 安装](#1-fast-install)基础上添加匹配的可选依赖后，Discord 和 Telegram 即可使用语音笔记功能。

macOS/Linux:

```bash
# NVIDIA NIM 转录 (Riva gRPC)
curl -fsSL "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh?raw=1" | sh -s -- --voice-nim

# 本地 Whisper (CPU 或 CUDA)
curl -fsSL "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh?raw=1" | sh -s -- --voice-local

# 双后端
curl -fsSL "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh?raw=1" | sh -s -- --voice-all

# 带 CUDA 的本地 Whisper
curl -fsSL "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh?raw=1" | sh -s -- --voice-local --torch-backend cu130
```

Windows PowerShell:

```powershell
# NVIDIA NIM 转录 (Riva gRPC)
& ([scriptblock]::Create((irm "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1?raw=1"))) -VoiceNim

# 本地 Whisper (CPU 或 CUDA)
& ([scriptblock]::Create((irm "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1?raw=1"))) -VoiceLocal

# 双后端
& ([scriptblock]::Create((irm "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1?raw=1"))) -VoiceAll

# 带 CUDA 的本地 Whisper
& ([scriptblock]::Create((irm "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1?raw=1"))) -VoiceLocal -TorchBackend cu130
```

重新安装后重启 `fcc-server`。

在 **管理界面** 中，打开 **Messaging** 并滚动到 **Voice**。开启 **Voice Notes**，选择 **Whisper Device**（`cpu`、`cuda` 或 `nvidia_nim`），设置 **Whisper Model**，并在你的环境需要时输入 **Hugging Face Token**。对于 **nvidia_nim** 转录，需安装 `voice` 扩展包并在 **Providers** 视图中设置 **NVIDIA NIM API Key**。上图展示了同一视图中的 **Voice** 模块。

## 🔍 工作原理

<div align="center">
  <img src="assets/how-it-works.svg" alt="Free Claude Code request flow architecture" width="900">
</div>

图表源码：[`assets/how-it-works.mmd`](assets/how-it-works.mmd)。

关键组件：
- FastAPI 暴露了 Anthropic 兼容的路由，如 `/v1/messages`、`/v1/messages/count_tokens` 和 `/v1/models`。
- 模型路由将 Claude 模型名称解析为 `MODEL_OPUS`、`MODEL_SONNET`、`MODEL_HAIKU` 或 `MODEL`。
- NIM、OpenCode Zen 和 OpenCode Go 使用 OpenAI 聊天流式传输，并将其转换为 Anthropic SSE。
- Wafer、OpenRouter、DeepSeek、Kimi、Fireworks AI、Z.ai、LM Studio、llama.cpp 和 Ollama 在适用时使用 Anthropic Messages 风格的传输协议（带有特定提供商的 quirks 和模型列表 URL）。
- 代理将思考块、工具调用、令牌使用元数据和提供商错误规范化为 Claude Code 期望的格式。
- 请求优化会在本地直接响应 Claude Code 的简单探测，从而节省延迟和配额。

## 💻 开发指南

### 1. 项目结构

```text
free-claude-code/
├── server.py              # ASGI 入口点
├── api/                   # FastAPI 路由、服务层、路由逻辑与优化
├── core/                  # 共享 Anthropic 协议辅助函数和 SSE 工具
├── providers/             # 提供商传输层、注册表与限流
├── messaging/             # Discord/Telegram 适配器、会话管理与语音功能
├── cli/                   # 包入口点与 Claude 进程管理
├── config/                # 设置、提供商目录与日志配置
└── tests/                 # 单元测试与契约测试
```

### 2. 从源码运行

如果你正在开发或希望直接从代码库运行，请使用此路径：

```bash
git clone https://github.com/Alishahryar1/free-claude-code.git
cd free-claude-code
uv run uvicorn server:app --host 0.0.0.0 --port 8082
```

### 3. 命令

```bash
uv run ruff format
uv run ruff check
uv run ty check
uv run pytest
```

在推送前按顺序运行它们。CI 会强制执行相同的检查。

### 4. 包脚本

`pyproject.toml` 安装了以下命令：
- `fcc-server`: 启动代理，使用配置的 host 和 port。
- `fcc-init`: 为 `~/.fcc/.env` 提供可选的高级脚手架；常规配置推荐使用 **管理界面**。
- `fcc-claude`: 启动 Claude Code，传入配置的本地代理 URL、认证令牌、模型发现标志以及用于自动压缩的 190k `CLAUDE_CODE_AUTO_COMPACT_WINDOW`。
- `free-claude-code`: `fcc-server` 的兼容性别名。

### 5. 扩展开发

- 添加 OpenAI 兼容提供商：继承 `OpenAIChatTransport`。
- 添加 Anthropic Messages 提供商：继承 `AnthropicMessagesTransport`。
- 在 `config.provider_catalog` 中注册提供商元数据，并在 `providers.registry` 中进行工厂接线。
- 添加消息平台：在 `messaging/` 中实现 `MessagingPlatform` 接口。

## 🤝 贡献指南

- [`.env.example`](.env.example) 列出了环境变量键名作为只读参考；请使用 **管理界面** 更改受管代理配置。
- 在 [Issues](https://github.com/Alishahryar1/free-claude-code/issues) 报告 Bug 和功能请求。提交 Bug 时请务必包含所有模型映射、问题发生时的当前模型以及具体的错误字符串。
- 保持变更小巧，并用聚焦的测试覆盖。
- 不要提交 Docker 集成相关的 PR。
- 不要仅为了修改 README 而提交 PR；请为此单独开一个 Issue。
- 在提交 Pull Request 前运行完整的检查序列。
- Python 3.14 正式版已恢复 `except X, Y` 语法（3.14 alpha 版本未包含）。在提交 PR 前请留意此点。

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.