![](blog/images/claude-code-router-img.png)

[![](https://img.shields.io/badge/%F0%9F%87%A8%F0%9F%87%B3-%E4%B8%AD%E6%96%87%E7%89%88-ff0000?style=flat)](README_zh.md)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white)](https://discord.gg/rdftVMaUcS)
[![](https://img.shields.io/github/license/musistudio/claude-code-router)](https://github.com/musistudio/claude-code-router/blob/main/LICENSE)

<hr>

![](blog/images/sponsors/glm-en.jpg)
> 本项目由 Z.ai 赞助，感谢其提供的 GLM CODING PLAN 支持。

> GLM CODING PLAN 是一款专为 AI 编程设计的订阅服务，月费低至 $10。它提供旗舰级 GLM-4.7 及（仅 Pro 用户可用的）GLM-5 模型，支持 Claude Code、Cline、Roo Code 等 10+ 款主流 AI 编程工具，为开发者带来顶级、快速且稳定的编码体验。

> 领取 GLM CODING PLAN 9折优惠：https://z.ai/subscribe?ic=8JVLJQFSKB  

> [从 CLI 工具风格视角看 Agent 工具的渐进式披露](/blog/en/progressive-disclosure-of-agent-tools-from-the-perspective-of-cli-tool-style.md)

> 一款强大的工具，可将 Claude Code 请求路由至不同模型，并自定义任何请求。

![](blog/images/claude-code.png)

## ✨ 功能特性

- **模型路由（Model Routing）**：根据需求将请求路由到不同的模型（例如后台任务、思考模式、长上下文）。
- **多提供商支持**：支持 OpenRouter、DeepSeek、Ollama、Gemini、火山引擎（Volcengine）和 SiliconFlow 等多种模型提供商。
- **请求/响应转换（Request/Response Transformation）**：使用转换器自定义不同提供商的请求和响应载荷。
- **动态切换模型**：在 Claude Code 中通过 `/model` 命令实时切换模型。
- **CLI 模型管理**：通过终端直接使用 `ccr model` 管理模型和提供商。
- **GitHub Actions 集成**：在 GitHub 工作流中触发 Claude Code 任务。
- **插件系统**：通过自定义转换器扩展功能。

## 🚀 快速开始

### 1. 安装

首先，确保已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code/quickstart)：

```shell
npm install -g @anthropic-ai/claude-code
```

然后，安装 Claude Code Router：

```shell
npm install -g @musistudio/claude-code-router
```

### 2. 配置

创建并配置你的 `~/.claude-code-router/config.json` 文件。更多详情可参考 `config.example.json`。

`config.json` 文件包含以下几个关键部分：

- **`PROXY_URL`**（可选）：可为 API 请求设置代理，例如：`"PROXY_URL": "http://127.0.0.1:7890"`。
- **`LOG`**（可选）：可通过设置为 `true` 启用日志记录。设为 `false` 时不生成日志文件，默认为 `true`。
- **`LOG_LEVEL`**（可选）：设置日志级别。可用选项包括：`"fatal"`、`"error"`、`"warn"`、`"info"`、`"debug"`、`"trace"`，默认为 `"debug"`。
- **日志系统**：Claude Code Router 使用两套独立的日志记录系统：
  - **服务端日志**：HTTP 请求、API 调用及服务器事件使用 pino 记录在 `~/.claude-code-router/logs/` 目录下，文件名格式为 `ccr-*.log`。
  - **应用层日志**：路由决策和业务逻辑事件记录在 `~/.claude-code-router/claude-code-router.log` 中。
- **`APIKEY`**（可选）：可设置密钥用于请求认证。启用后，客户端必须在 `Authorization` 头（如 `Bearer your-secret-key`）或 `x-api-key` 头中提供该密钥。示例：`"APIKEY": "your-secret-key"`。
- **`HOST`**（可选）：可设置服务器主机地址。若未设置 `APIKEY`，出于安全考虑主机将强制设为 `127.0.0.1` 以防止未经授权的访问。示例：`"HOST": "0.0.0.0"`。
- **`NON_INTERACTIVE_MODE`**（可选）：设为 `true` 时，启用与 GitHub Actions、Docker 容器或其他 CI/CD 系统等非交互式环境的兼容性。此设置会自动配置合适的环境变量（如 `CI=true`、`FORCE_COLOR=0` 等），并调整 stdin 处理逻辑以防止进程在自动化环境中挂起。示例：`"NON_INTERACTIVE_MODE": true`。

- **`Providers`**：用于配置不同的模型提供商。
- **`Router`**：用于设置路由规则。`default` 指定默认模型，若未配置其他路由则所有请求均使用此模型。
- **`API_TIMEOUT_MS`**：指定 API 调用的超时时间（毫秒）。

#### 环境变量插值（Environment Variable Interpolation）

Claude Code Router 支持环境变量插值，以便安全地管理 API 密钥。你可以在 `config.json` 中使用 `$VAR_NAME` 或 `${VAR_NAME}` 语法引用环境变量：

```json
{
  "OPENAI_API_KEY": "$OPENAI_API_KEY",
  "GEMINI_API_KEY": "${GEMINI_API_KEY}",
  "Providers": [
    {
      "name": "openai",
      "api_base_url": "https://api.openai.com/v1/chat/completions",
      "api_key": "$OPENAI_API_KEY",
      "models": ["gpt-5", "gpt-5-mini"]
    }
  ]
}
```

这允许你将敏感的 API 密钥保存在环境变量中，而非硬编码在配置文件里。插值功能支持递归处理嵌套对象和数组。

以下是一个完整示例：

```json
{
  "APIKEY": "your-secret-key",
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "API_TIMEOUT_MS": 600000,
  "NON_INTERACTIVE_MODE": false,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-xxx",
      "models": [
        "google/gemini-2.5-pro-preview",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking"
      ],
      "transformer": {
        "use": ["openrouter"]
      }
    },
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"],
      "transformer": {
        "use": ["deepseek"],
        "deepseek-chat": {
          "use": ["tooluse"]
        }
      }
    },
    {
      "name": "ollama",
      "api_base_url": "http://localhost:11434/v1/chat/completions",
      "api_key": "ollama",
      "models": ["qwen2.5-coder:latest"]
    },
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/models/",
      "api_key": "sk-xxx",
      "models": ["gemini-2.5-flash", "gemini-2.5-pro"],
      "transformer": {
        "use": ["gemini"]
      }
    },
    {
      "name": "volcengine",
      "api_base_url": "https://ark.cn-beijing.volces.com/api/v3/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-v3-250324", "deepseek-r1-250528"],
      "transformer": {
        "use": ["deepseek"]
      }
    },
    {
      "name": "modelscope",
      "api_base_url": "https://api-inference.modelscope.cn/v1/chat/completions",
      "api_key": "",
      "models": ["Qwen/Qwen3-Coder-480B-A35B-Instruct", "Qwen/Qwen3-235B-A22B-Thinking-2507"],
      "transformer": {
        "use": [
          [
            "maxtoken",
            {
              "max_tokens": 65536
            }
          ],
          "enhancetool"
        ],
        "Qwen/Qwen3-235B-A22B-Thinking-2507": {
          "use": ["reasoning"]
        }
      }
    },
    {
      "name": "dashscope",
      "api_base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
      "api_key": "",
      "models": ["qwen3-coder-plus"],
      "transformer": {
        "use": [
          [
            "maxtoken",
            {
              "max_tokens": 65536
            }
          ],
          "enhancetool"
        ]
      }
    },
    {
      "name": "aihubmix",
      "api_base_url": "https://aihubmix.com/v1/chat/completions",
      "api_key": "sk-",
      "models": [
        "Z/glm-4.5",
        "claude-opus-4-20250514",
        "gemini-2.5-pro"
      ]
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "ollama,qwen2.5-coder:latest",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "openrouter,google/gemini-2.5-pro-preview",
    "longContextThreshold": 60000,
    "webSearch": "gemini,gemini-2.5-flash"
  }
}
```

### 3. 使用路由器运行 Claude Code

通过路由器启动 Claude Code：

```shell
ccr code
```

> **注意**：修改配置文件后，需重启服务以使更改生效：
>
> ```shell
> ccr restart
> ```

### 4. UI 模式

为了更直观的体验，你可以使用 UI 模式来管理配置：

```shell
ccr ui
```

这将打开一个基于 Web 的界面，方便你查看和编辑 `config.json` 文件。

![UI](/blog/images/ui.png)

### 5. CLI 模型管理

对于偏好终端工作流的用户，可使用交互式 CLI 模型选择器：

```shell
ccr model
```
![](blog/images/models.gif)

该命令提供以下交互功能：

- **查看当前配置**：
- **查看所有已配置的模型**（默认、后台、思考、长上下文、网页搜索、图像）
- **切换模型**：快速更改每种路由类型使用的模型
- **添加新模型**：将模型添加到现有提供商
- **创建新提供商**：设置完整的提供商配置，包括：
   - 提供商名称与 API 端点
   - API 密钥
   - 可用模型列表
   - 转换器配置（支持）：
     - 多转换器组合（如 openrouter、deepseek、gemini 等）
     - 转换器选项（例如使用 maxtoken 设置自定义限制）
     - 提供商专属路由（例如 OpenRouter 的提供商偏好设置）

CLI 工具会验证所有输入并提供友好的提示，引导你完成配置过程。无需手动编辑 JSON 文件即可轻松管理复杂配置。

### 6. 预设管理（Presets Management）

预设功能允许你轻松保存、共享和复用配置。你可以将当前配置导出为预设，并从文件或 URL 安装预设。

```shell
# 将当前配置导出为预设
ccr preset export my-preset

# 带元数据导出
ccr preset export my-preset --description "My OpenAI config" --author "Your Name" --tags "openai,production"

# 从本地目录安装预设
ccr preset install /path/to/preset

# 列出所有已安装的预设
ccr preset list

# 查看预设信息
ccr preset info my-preset

# 删除预设
ccr preset delete my-preset
```

**预设特性：**
- **导出**：将当前配置保存为预设目录（包含 `manifest.json`）
- **安装**：从本地目录安装预设
- **敏感数据处理**：导出时会自动清理 API 密钥等敏感数据（标记为 `{{field}}` 占位符）
- **动态配置**：预设可包含输入模式，用于在安装过程中收集必要信息
- **版本控制**：每个预设均包含版本元数据以跟踪更新

**预设文件结构：**
```
~/.claude-code-router/presets/
├── my-preset/
│   └── manifest.json    # 包含配置和元数据
```

### 7. activate 命令（环境变量配置）

`activate` 命令允许你在 Shell 中全局设置环境变量，使你能够直接使用 `claude` 命令或将 Claude Code Router 与基于 Agent SDK 构建的应用集成。

要激活环境变量，请运行：

```shell
eval "$(ccr activate)"
```

该命令会以 Shell 友好的格式输出必要的环境变量，并在当前会话中设置。激活后你可以：

- **直接使用 `claude` 命令**：无需使用 `ccr code` 即可运行 `claude` 命令。`claude` 命令会自动将请求路由至 Claude Code Router。
- **与 Agent SDK 应用集成**：使用 Anthropic Agent SDK 构建的应用将自动使用已配置的路由器和模型。

`activate` 命令会设置以下环境变量：

- **`ANTHROPIC_AUTH_TOKEN`**：配置文件中的 API 密钥
- **`ANTHROPIC_BASE_URL`**：本地路由器端点（默认：`http://127.0.0.1:3456`）
- **`NO_PROXY`**：设为 `127.0.0.1` 以防止代理干扰
- **`DISABLE_TELEMETRY`**：禁用遥测功能
- **`DISABLE_COST_WARNINGS`**：禁用费用警告
- **`API_TIMEOUT_MS`**：配置文件中的 API 超时时间

> **注意**：在使用激活的环境变量前，请确保 Claude Code Router 服务正在运行（执行 `ccr start`）。环境变量仅对当前 Shell 会话有效。若要使其持久生效，可将 `eval "$(ccr activate)"` 添加到你的 Shell 配置文件中（例如 `~/.zshrc` 或 `~/.bashrc`）。

#### 提供商 (Providers)

`Providers` 数组用于定义你要使用的不同模型提供商。每个提供商对象需包含：

- **`name`**：提供商的唯一名称。
- **`api_base_url`**：聊天补全的完整 API 端点地址。
- **`api_key`**：该提供商的 API 密钥。
- **`models`**：该提供商可用的模型名称列表。
- **`transformer`**（可选）：指定用于处理请求和响应的转换器。

#### 转换器 (Transformers)

转换器允许你修改请求和响应载荷，以确保与不同提供商 API 的兼容性。

- **全局转换器**：将转换器应用于某提供商下的所有模型。在此示例中，`openrouter` 转换器应用于 `openrouter` 提供商下的所有模型。
  ```json
  {
    "name": "openrouter",
    "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
    "api_key": "sk-xxx",
    "models": [
      "google/gemini-2.5-pro-preview",
      "anthropic/claude-sonnet-4",
      "anthropic/claude-3.5-sonnet"
    ],
    "transformer": { "use": ["openrouter"] }
  }
  ```
- **模型专属转换器**：将转换器应用于特定模型。在此示例中，`deepseek` 转换器应用于所有模型，而额外的 `tooluse` 转换器仅应用于 `deepseek-chat` 模型。

  ```json
  {
    "name": "deepseek",
    "api_base_url": "https://api.deepseek.com/chat/completions",
    "api_key": "sk-xxx",
    "models": ["deepseek-chat", "deepseek-reasoner"],
    "transformer": {
      "use": ["deepseek"],
      "deepseek-chat": { "use": ["tooluse"] }
    }
  }
  ```

- **向转换器传递选项**：部分转换器（如 `maxtoken`）接受配置选项。要传递选项，请使用嵌套数组，其中第一个元素为转换器名称，第二个为选项对象。
  ```json
  {
    "name": "siliconflow",
    "api_base_url": "https://api.siliconflow.cn/v1/chat/completions",
    "api_key": "sk-xxx",
    "models": ["moonshotai/Kimi-K2-Instruct"],
    "transformer": {
      "use": [
        [
          "maxtoken",
          {
            "max_tokens": 16384
          }
        ]
      ]
    }
  }
  ```

**内置可用转换器：**

- **`Anthropic`**：若仅使用此转换器，将保留原始请求和响应参数（可用于直接连接至 Anthropic 端点）。
- **`deepseek`**：适配 DeepSeek API 的请求/响应。
- **`gemini`**：适配 Gemini API 的请求/响应。
- **`openrouter`**：适配 OpenRouter API 的请求/响应。它还接受一个 `provider` 路由参数，用于指定 OpenRouter 应使用的底层提供商。更多详情请参阅 [OpenRouter 文档](https://openrouter.ai/docs/features/provider-routing)。示例如下：
  ```json
    "transformer": {
      "use": ["openrouter"],
      "moonshotai/kimi-k2": {
        "use": [
          [
            "openrouter",
            {
              "provider": {
                "only": ["moonshotai/fp8"]
              }
            }
          ]
        ]
      }
    }
  ```
- **`groq`**：适配 Groq API 的请求/响应。
- **`maxtoken`**：设置特定的 `max_tokens` 值。
- **`tooluse`**：通过 `tool_choice` 优化特定模型的工具调用。
- **`gemini-cli`**（实验性）：通过 Gemini CLI 对 Gemini 的非官方支持 [gemini-cli.js](https://gist.github.com/musistudio/1c13a65f35916a7ab690649d3df8d1cd)。
- **`reasoning`**：用于处理 `reasoning_content` 字段。
- **`sampling`**：用于处理采样信息字段，如 `temperature`、`top_p`、`top_k` 和 `repetition_penalty`。
- **`enhancetool`**：为 LLM 返回的工具调用参数增加一层容错处理（这将导致工具调用信息不再流式传输）。
- **`cleancache`**：清除请求中的 `cache_control` 字段。
- **`vertex-gemini`**：使用 Vertex 认证处理 Gemini API。
- **`chutes-glm`**：通过 Chutes 对 GLM 4.5 模型的非官方支持 [chutes-glm-transformer.js](https://gist.github.com/vitobotta/2be3f33722e05e8d4f9d2b0138b8c863)。
- **`qwen-cli`**（实验性）：通过 Qwen CLI 对 qwen3-coder-plus 模型的非官方支持 [qwen-cli.js](https://gist.github.com/musistudio/f5a67841ced39912fd99e42200d5ca8b)。
- **`rovo-cli`**（实验性）：通过 Atlassian Rovo Dev CLI 对 gpt-5 的非官方支持 [rovo-cli.js](https://gist.github.com/SaseQ/c2a20a38b11276537ec5332d1f7a5e53)。

**自定义转换器：**

你也可以创建自己的转换器，并通过 `config.json` 中的 `transformers` 字段加载它们。

```json
{
  "transformers": [
    {
      "path": "/User/xxx/.claude-code-router/plugins/gemini-cli.js",
      "options": {
        "project": "xxx"
      }
    }
  ]
}
```

#### 路由器 (Router)

`Router` 对象用于定义不同场景下使用的模型：

- **`default`**：通用任务的默认模型。
- **`background`**：后台任务使用的模型（可使用较小的本地模型以节省成本）。
- **`think`**：用于重度推理任务的模型，例如计划模式。
- **`longContext`**：处理长上下文（如 > 60K token）的模型。
- **`longContextThreshold`**（可选）：触发长上下文模型的 Token 数量阈值，默认为 60000。
- **`webSearch`**：用于处理网页搜索任务，需模型本身支持该功能。若使用 OpenRouter，需在模型名称后添加 `:online` 后缀。
- **`image`**（测试版）：用于处理图像相关任务（由 CCR 内置 Agent 支持）。若模型不支持工具调用，需将 `config.forceUseImageAgent` 属性设为 `true`。

- **你还可以通过 `/model` 命令在 Claude Code 中动态切换模型：**
  `/model provider_name,model_name`
  示例：`/model openrouter,anthropic/claude-3.5-sonnet`

#### 自定义路由器 (Custom Router)

对于更高级的路由逻辑，你可以在 `config.json` 中通过 `CUSTOM_ROUTER_PATH` 指定自定义路由器脚本。这允许你实现超出默认场景的复杂路由规则。

在 `config.json` 中：

```json
{
  "CUSTOM_ROUTER_PATH": "/User/xxx/.claude-code-router/custom-router.js"
}
```

自定义路由器文件必须是一个导出 `async` 函数的 JavaScript 模块。该函数接收请求对象和配置对象作为参数，并应返回提供商和模型名称的字符串（例如 `"provider_name,model_name"`），或返回 `null` 以回退到默认路由器。

以下是一个基于 `custom-router.example.js` 的 `custom-router.js` 示例：

```javascript
// /User/xxx/.claude-code-router/custom-router.js

/**
 * A custom router function to determine which model to use based on the request.
 *
 * @param {object} req - The request object from Claude Code, containing the request body.
 * @param {object} config - The application's config object.
 * @returns {Promise<string|null>} - A promise that resolves to the "provider,model_name" string, or null to use the default router.
 */
module.exports = async function router(req, config) {
  const userMessage = req.body.messages.find((m) => m.role === "user")?.content;

  if (userMessage && userMessage.includes("explain this code")) {
    // Use a powerful model for code explanation
    return "openrouter,anthropic/claude-3.5-sonnet";
  }

  // Fallback to the default router configuration
  return null;
};
```

##### 子代理路由 (Subagent Routing)

对于子代理内部的路由，必须在子代理提示词的**开头**包含 `<CCR-SUBAGENT-MODEL>provider,model</CCR-SUBAGENT-MODEL>`，以指定特定的提供商和模型。这允许你将特定子代理任务定向到指定的模型。

**示例：**

```
<CCR-SUBAGENT-MODEL>openrouter,anthropic/claude-3.5-sonnet</CCR-SUBAGENT-MODEL>
Please help me analyze this code snippet for potential optimizations...
```

## 状态栏（测试版）
为了更好地监控运行时 Claude Code Router 的状态，v1.0.40 版本内置了状态栏工具，你可以在 UI 中启用它。
![statusline-config.png](/blog/images/statusline-config.png)

效果如下：
![statusline](/blog/images/statusline.png)

## 🤖 GitHub Actions

将 Claude Code Router 集成到你的 CI/CD 流水线中。完成 [Claude Code Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions) 设置后，修改你的 `.github/workflows/claude.yaml` 以使用路由器：

```yaml
name: Claude Code

on:
  issue_comment:
    types: [created]
  # ... other triggers

jobs:
  claude:
    if: |
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
      # ... other conditions
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: read
      issues: read
      id-token: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - name: Prepare Environment
        run: |
          curl -fsSL https://bun.sh/install | bash
          mkdir -p $HOME/.claude-code-router
          cat << 'EOF' > $HOME/.claude-code-router/config.json
          {
            "log": true,
            "NON_INTERACTIVE_MODE": true,
            "OPENAI_API_KEY": "${{ secrets.OPENAI_API_KEY }}",
            "OPENAI_BASE_URL": "https://api.deepseek.com",
            "OPENAI_MODEL": "deepseek-chat"
          }
          EOF
        shell: bash

      - name: Start Claude Code Router
        run: |
          nohup ~/.bun/bin/bunx @musistudio/claude-code-router@1.0.8 start &
        shell: bash

      - name: Run Claude Code
        id: claude
        uses: anthropics/claude-code-action@beta
        env:
          ANTHROPIC_BASE_URL: http://localhost:3456
        with:
          anthropic_api_key: "any-string-is-ok"
```

> **注意**：在 GitHub Actions 或其他自动化环境中运行时，请确保配置中设置 `"NON_INTERACTIVE_MODE": true`，以防止因 stdin 处理问题导致进程挂起。

此设置可实现有趣的自动化操作，例如在低峰期运行任务以降低 API 成本。

## 📝 延伸阅读

- [项目动机与工作原理](blog/en/project-motivation-and-how-it-works.md)
- [也许我们可以用路由器做更多事](blog/en/maybe-we-can-do-more-with-the-route.md)
- [GLM-4.6 支持推理与交错思考](blog/en/glm-4.6-supports-reasoning.md)

## ❤️ 支持与赞助

如果你觉得这个项目有帮助，请考虑赞助其开发。非常感谢你的支持！

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F31GN2GM)

[Paypal](https://paypal.me/musistudio1999)

<table>
  <tr>
    <td><img src="/blog/images/alipay.jpg" width="200" alt="Alipay" /></td>
    <td><img src="/blog/images/wechat.jpg" width="200" alt="WeChat Pay" /></td>
  </tr>
</table>

### 我们的赞助商

衷心感谢所有慷慨支持的赞助商！


- [AIHubmix](https://aihubmix.com/)
- [BurnCloud](https://ai.burncloud.com)
- [302.AI](https://share.302.ai/ZGVF9w)
- [Z智谱](https://www.bigmodel.cn/claude-code?ic=FPF9IVAGFJ)
- @Simon Leischnig
- [@duanshuaimin](https://github.com/duanshuaimin)
- [@vrgitadmin](https://github.com/vrgitadmin)
- @\*o
- [@ceilwoo](https://github.com/ceilwoo)
- @\*说
- @\*更
- @K\*g
- @R\*R
- [@bobleer](https://github.com/bobleer)
- @\*苗
- @\*划
- [@Clarence-pan](https://github.com/Clarence-pan)
- [@carter003](https://github.com/carter003)
- @S\*r
- @\*晖
- @\*敏
- @Z\*z
- @\*然
- [@cluic](https://github.com/cluic)
- @\*苗
- [@PromptExpert](https://github.com/PromptExpert)
- @\*应
- [@yusnake](https://github.com/yusnake)
- @\*飞
- @董\*
- @\*汀
- @\*涯
- @\*:-）
- @\*\*磊
- @\*琢
- @\*成
- @Z\*o
- @\*琨
- [@congzhangzh](https://github.com/congzhangzh)
- @\*\_
- @Z\*m
- @*鑫
- @c\*y
- @\*昕
- [@witsice](https://github.com/witsice)
- @b\*g
- @\*亿
- @\*辉
- @JACK
- @\*光
- @W\*l
- [@kesku](https://github.com/kesku)
- [@biguncle](https://github.com/biguncle)
- @二吉吉
- @a\*g
- @\*林
- @\*咸
- @\*明
- @S\*y
- @f\*o
- @\*智
- @F\*t
- @r\*c
- [@qierkang](http://github.com/qierkang)
- @\*军
- [@snrise-z](http://github.com/snrise-z)
- @\*王
- [@greatheart1000](http://github.com/greatheart1000)
- @\*王
- @zcutlip
- [@Peng-YM](http://github.com/Peng-YM)
- @\*更
- @\*.
- @F\*t
- @\*政
- @\*铭
- @\*叶
- @七\*o
- @\*青
- @\*\*晨
- @\*远
- @\*霄
- @\*\*吉
- @\*\*飞
- @\*\*驰
- @x\*g
- @\*\*东
- @\*落
- @哆\*k
- @\*涛
- [@苗大](https://github.com/WitMiao)
- @\*呢
- @\d*u
- @crizcraig
- s\*s
- \*火
- \*勤
- \*\*锟
- \*涛
- \*\*明
- \*知
- \*语
- \*瓜


(若你的名字被隐藏，请通过主页邮箱联系我，以便更新为你的 GitHub 用户名。)