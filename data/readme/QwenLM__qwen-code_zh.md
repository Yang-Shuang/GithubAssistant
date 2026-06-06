<div align="center">

[![npm version](https://img.shields.io/npm/v/@qwen-code/qwen-code.svg)](https://www.npmjs.com/package/@qwen-code/qwen-code)
[![License](https://img.shields.io/github/license/QwenLM/qwen-code.svg)](./LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D22.0.0-brightgreen.svg)](https://nodejs.org/)
[![Downloads](https://img.shields.io/npm/dm/@qwen-code/qwen-code.svg)](https://www.npmjs.com/package/@qwen-code/qwen-code)

<a href="https://trendshift.io/repositories/15287" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15287" alt="QwenLM%2Fqwen-code | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

**一个驻留在终端中的开源 AI 智能体（Agent）。**

<a href="https://qwenlm.github.io/qwen-code-docs/zh/users/overview">中文</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/de/users/overview">Deutsch</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/fr/users/overview">français</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/ja/users/overview">日本語</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/ru/users/overview">Русский</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/pt-BR/users/overview">Português (Brasil)</a>

</div>

## 🎉 更新动态

- **2026-04-15**：Qwen OAuth 免费套餐已停止服务。要继续使用 Qwen Code，请切换至 [Alibaba Cloud Coding Plan](https://modelstudio.console.alibabacloud.com/?tab=coding-plan#/efm/coding-plan-index)、[OpenRouter](https://openrouter.ai)、[Fireworks AI](https://app.fireworks.ai)，或使用你自己的 API Key。运行 `qwen auth` 进行配置。

- **2026-04-13**：Qwen OAuth 免费套餐策略更新：每日请求配额调整为每天 100 次（原为 1,000 次）。

- **2026-04-02**：**Qwen3.6-Plus 现已上线！** 从 [Alibaba Cloud ModelStudio](https://modelstudio.console.alibabacloud.com/ap-southeast-1?tab=doc#/doc/?type=model&url=2840914_2&modelId=qwen3.6-plus) 获取 API Key，通过 OpenAI 兼容的 API 进行访问。

- **2026-02-16**：**Qwen3.5-Plus 现已上线！**

## 为什么选择 Qwen Code？

Qwen Code 是一款专为终端设计的开源 AI 智能体（Agent），针对 Qwen 系列模型进行了深度优化。它能帮助你理解大型代码库、自动化繁琐工作并加速交付。

- **多协议与灵活的服务商支持**：可使用兼容 OpenAI / Anthropic / Gemini 的 API、[Alibaba Cloud Coding Plan](https://modelstudio.console.alibabacloud.com/?tab=coding-plan#/efm/coding-plan-index)、[OpenRouter](https://openrouter.ai)、[Fireworks AI](https://app.fireworks.ai)，或自带 API Key。
- **开源与协同演进**：框架与 Qwen3-Coder 模型均为开源，二者同步发布并共同演进。
- **智能体工作流与丰富功能**：内置丰富的工具（Skills、SubAgents），提供完整的智能体工作流和类 Claude Code 的使用体验。
- **终端优先，IDE 友好**：专为命令行开发者打造，可选集成 VS Code、Zed 和 JetBrains IDE。

![](https://gw.alicdn.com/imgextra/i1/O1CN01D2DviS1wwtEtMwIzJ_!!6000000006373-2-tps-1600-900.png)

## 安装

### 快速安装（推荐）

#### Linux / macOS

```bash
curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash
```

#### Windows

```powershell
irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex
```

> **注意**：安装完成后建议重启终端，以确保环境变量生效。

### 手动安装

#### 前置条件

确保已安装 Node.js 22 或更高版本。请从 [nodejs.org](https://nodejs.org/en/download) 下载。

#### NPM

```bash
npm install -g @qwen-code/qwen-code@latest
```

#### Homebrew（macOS、Linux）

```bash
brew install qwen-code
```

## 快速开始

```bash
# Start Qwen Code (interactive)
qwen

# Then, in the session:
/help
/auth
```

首次使用时，系统将提示你登录。你可以随时运行 `/auth` 切换认证方式。

示例提示词：

```text
What does this project do?
Explain the codebase structure.
Help me refactor this function.
Generate unit tests for this module.
```

<details>
<summary>Click to watch a demo video</summary>

<video src="https://cloud.video.taobao.com/vod/HLfyppnCHplRV9Qhz2xSqeazHeRzYtG-EYJnHAqtzkQ.mp4" controls>
Your browser does not support the video tag.
</video>

</details>

## 🦞 在 Claw 中使用 Qwen Code 进行编码任务

复制以下提示词并粘贴到你的智能体中：

```
Use Qwen Code as a coding agent. First, fetch and read this skill reference:
https://raw.githubusercontent.com/QwenLM/qwen-code/refs/heads/main/.qwen/skills/qwen-code-claw/SKILL.md
Then follow the instructions inside to install, authenticate, and use Qwen Code via acpx for all coding tasks.
```

## 认证配置

Qwen Code 支持以下认证方式：

- **API Key（推荐）**：使用阿里云百炼（[北京](https://bailian.console.aliyun.com/) / [国际版](https://modelstudio.console.alibabacloud.com/）或其他支持的服务商（OpenAI、Anthropic、Google GenAI 及其他兼容端点）提供的 API Key。
- **编程套餐**：订阅阿里云编程套餐（[北京](https://bailian.console.aliyun.com/cn-beijing?tab=coding-plan#/efm/coding-plan-index) / [国际版](https://modelstudio.console.alibabacloud.com/?tab=coding-plan#/efm/coding-plan-index）），按月付费，享有更高配额。

> ⚠️ **Qwen OAuth 已于 2026 年 4 月 15 日停止服务。** 如果你之前使用的是 Qwen OAuth，请切换至上述任一方式。运行 `qwen` 然后执行 `/auth` 重新配置。

#### API Key（推荐）

使用 API Key 连接阿里云百炼或任何支持的服务商。支持多种协议：

- **兼容 OpenAI**：阿里云百炼、ModelScope、OpenAI、OpenRouter 及其他兼容 OpenAI 的服务商
- **Anthropic**：Claude 系列模型
- **Google GenAI**：Gemini 系列模型

**推荐**的模型与服务商配置方式是编辑 `~/.qwen/settings.json` 文件（若不存在则新建）。该文件允许你在一个位置定义所有可用模型、API Key 和默认设置。

##### 三步快速配置

**步骤 1：** 创建或编辑 `~/.qwen/settings.json`

完整示例如下：

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.6-plus",
        "name": "qwen3.6-plus",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "description": "Qwen3-Coder via Dashscope",
        "envKey": "DASHSCOPE_API_KEY"
      }
    ]
  },
  "env": {
    "DASHSCOPE_API_KEY": "sk-xxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3.6-plus"
  }
}
```

**步骤 2：** 了解各字段含义

| Field                        | What it does                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `modelProviders`             | Declares which models are available and how to connect to them. Keys like `openai`, `anthropic`, `gemini` represent the API protocol. |
| `modelProviders[].id`        | The model ID sent to the API (e.g. `qwen3.6-plus`, `gpt-4o`).                                                                         |
| `modelProviders[].envKey`    | The name of the environment variable that holds your API key.                                                                         |
| `modelProviders[].baseUrl`   | The API endpoint URL (required for non-default endpoints).                                                                            |
| `env`                        | A fallback place to store API keys (lowest priority; prefer `.env` files or `export` for sensitive keys).                             |
| `security.auth.selectedType` | The protocol to use on startup (`openai`, `anthropic`, `gemini`, `vertex-ai`).                                                        |
| `model.name`                 | The default model to use when Qwen Code starts.                                                                                       |

**步骤 3：** 启动 Qwen Code —— 配置将自动生效：

```bash
qwen
```

可随时使用 `/model` 命令在所有已配置的模型之间切换。

##### 更多示例

<details>
<summary>Coding Plan (Alibaba Cloud ModelStudio) — fixed monthly fee, higher quotas</summary>

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.6-plus",
        "name": "qwen3.6-plus (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "qwen3.6-plus from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY"
      },
      {
        "id": "qwen3.5-plus",
        "name": "qwen3.5-plus (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "qwen3.5-plus with thinking enabled from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "glm-4.7",
        "name": "glm-4.7 (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "glm-4.7 with thinking enabled from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "kimi-k2.5",
        "name": "kimi-k2.5 (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "kimi-k2.5 with thinking enabled from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      }
    ]
  },
  "env": {
    "BAILIAN_CODING_PLAN_API_KEY": "sk-xxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3.6-plus"
  }
}
```

> Subscribe to the Coding Plan and get your API key at [Alibaba Cloud ModelStudio(Beijing)](https://bailian.console.aliyun.com/cn-beijing?tab=coding-plan#/efm/coding-plan-index) or [Alibaba Cloud ModelStudio(intl)](https://modelstudio.console.alibabacloud.com/?tab=coding-plan#/efm/coding-plan-index).

</details>

<details>
<summary>Multiple providers (OpenAI + Anthropic + Gemini)</summary>

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "gpt-4o",
        "name": "GPT-4o",
        "envKey": "OPENAI_API_KEY",
        "baseUrl": "https://api.openai.com/v1"
      }
    ],
    "anthropic": [
      {
        "id": "claude-sonnet-4-20250514",
        "name": "Claude Sonnet 4",
        "envKey": "ANTHROPIC_API_KEY"
      }
    ],
    "gemini": [
      {
        "id": "gemini-2.5-pro",
        "name": "Gemini 2.5 Pro",
        "envKey": "GEMINI_API_KEY"
      }
    ]
  },
  "env": {
    "OPENAI_API_KEY": "sk-xxxxxxxxxxxxx",
    "ANTHROPIC_API_KEY": "sk-ant-xxxxxxxxxxxxx",
    "GEMINI_API_KEY": "AIzaxxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "gpt-4o"
  }
}
```

</details>

<details>
<summary>Enable thinking mode (for supported models like qwen3.5-plus)</summary>

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.5-plus",
        "name": "qwen3.5-plus (thinking)",
        "envKey": "DASHSCOPE_API_KEY",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      }
    ]
  },
  "env": {
    "DASHSCOPE_API_KEY": "sk-xxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3.5-plus"
  }
}
```

</details>

> **提示**：你也可以通过 Shell 中的 `export` 命令或 `.env` 文件设置 API Key，其优先级高于 `settings.json` → `env`。完整说明请参阅[认证指南](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/)。

> **安全提示**：切勿将 API Key 提交至版本控制系统。`~/.qwen/settings.json` 文件位于你的主目录下，应保持私密。

#### Local Model Setup (Ollama / vLLM)

You can also run models locally — no API key or cloud account needed. This is not an authentication method; instead, configure your local model endpoint in `~/.qwen/settings.json` using the `modelProviders` field.

Set `generationConfig.contextWindowSize` inside the matching provider entry
and adjust it to the context length configured on your local server.

<details>
<summary>Ollama setup</summary>

1. Install Ollama from [ollama.com](https://ollama.com/)
2. Pull a model: `ollama pull qwen3:32b`
3. Configure `~/.qwen/settings.json`:

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3:32b",
        "name": "Qwen3 32B (Ollama)",
        "baseUrl": "http://localhost:11434/v1",
        "description": "Qwen3 32B running locally via Ollama",
        "generationConfig": {
          "contextWindowSize": 131072
        }
      }
    ]
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3:32b"
  }
}
```

</details>

<details>
<summary>vLLM setup</summary>

1. Install vLLM: `pip install vllm`
2. Start the server: `vllm serve Qwen/Qwen3-32B`
3. Configure `~/.qwen/settings.json`:

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "Qwen/Qwen3-32B",
        "name": "Qwen3 32B (vLLM)",
        "baseUrl": "http://localhost:8000/v1",
        "description": "Qwen3 32B running locally via vLLM",
        "generationConfig": {
          "contextWindowSize": 131072
        }
      }
    ]
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "Qwen/Qwen3-32B"
  }
}
```

</details>

## 使用方式

作为开源终端智能体，Qwen Code 主要有五种使用方式：

1. Interactive mode（终端界面）
2. Headless mode（脚本、CI）
3. IDE integration（VS Code、Zed）
4. SDKs（TypeScript、Python、Java）
5. Daemon mode —— `qwen serve` 通过 HTTP+SSE 暴露 ACP，使多个客户端共享同一个智能体（实验性功能）

#### Interactive mode

```bash
cd your-project/
qwen
```

在项目文件夹中运行 `qwen` 即可启动交互式终端界面。使用 `@` 引用本地文件（例如 `@src/main.ts`）。

#### Headless mode

```bash
cd your-project/
qwen -p "your question"
```

使用 `-p` 参数在无交互式界面的情况下运行 Qwen Code——非常适合脚本、自动化和 CI/CD。了解更多：[Headless mode](https://qwenlm.github.io/qwen-code-docs/en/users/features/headless)。

#### IDE integration

Use Qwen Code inside your editor (VS Code, Zed, and JetBrains IDEs):

- [Use in VS Code](https://qwenlm.github.io/qwen-code-docs/en/users/integration-vscode/)
- [Use in Zed](https://qwenlm.github.io/qwen-code-docs/en/users/integration-zed/)
- [Use in JetBrains IDEs](https://qwenlm.github.io/qwen-code-docs/en/users/integration-jetbrains/)

#### Daemon mode (`qwen serve`, experimental)

```bash
cd your-project/
qwen serve
# → qwen serve listening on http://127.0.0.1:4170 (mode=http-bridge)
```

将 Qwen Code 作为本地 HTTP 守护进程运行，使 IDE 插件、Web UI、CI 脚本和自定义 CLI 通过 HTTP+SSE 共享**一个**智能体会话——而不是各自启动独立的子进程。默认情况下回环绑定（Loopback）无需认证（设置 `QWEN_SERVER_TOKEN` 可在回环绑定下启用 Bearer 认证）；远程绑定（`--hostname 0.0.0.0`）**必须**提供 Token，否则启动将拒绝。详见：

- [Daemon mode user guide](https://qwenlm.github.io/qwen-code-docs/en/users/qwen-serve)
- [HTTP protocol reference](https://qwenlm.github.io/qwen-code-docs/en/developers/qwen-serve-protocol)
- [DaemonClient TypeScript quickstart](https://qwenlm.github.io/qwen-code-docs/en/developers/examples/daemon-client-quickstart)

#### SDKs

Build on top of Qwen Code with the available SDKs:

- TypeScript: [Use the Qwen Code SDK](./packages/sdk-typescript/README.md)
- Python: [Use the Python SDK](./packages/sdk-python/README.md)
- Java: [Use the Java SDK](./packages/sdk-java/qwencode/README.md)

Python SDK example:

```python
import asyncio

from qwen_code_sdk import is_sdk_result_message, query


async def main() -> None:
    result = query(
        "Summarize the repository layout.",
        {
            "cwd": "/path/to/project",
            "path_to_qwen_executable": "qwen",
        },
    )

    async for message in result:
        if is_sdk_result_message(message):
            print(message["result"])


asyncio.run(main())
```

## 命令与快捷键

### Session Commands

- `/help` - Display available commands
- `/clear` - Clear conversation history
- `/compress` - Compress history to save tokens
- `/stats` - Show current session information
- `/bug` - Submit a bug report
- `/exit` or `/quit` - Exit Qwen Code

### Keyboard Shortcuts

- `Ctrl+C` - Cancel current operation
- `Ctrl+D` - Exit (on empty line)
- `Up/Down` - Navigate command history

> Learn more about [Commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/)
>
> **提示**：在 YOLO 模式（`--yolo`）下，检测到图片时会自动切换视觉能力而无需额外提示。了解更多关于[审批模式](https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/)的信息

## 配置

Qwen Code 可通过 `settings.json`、环境变量和 CLI 参数进行配置。

| File                    | Scope         | Description                                                                             |
| ----------------------- | ------------- | --------------------------------------------------------------------------------------- |
| `~/.qwen/settings.json` | User (global) | Applies to all your Qwen Code sessions. **Recommended for `modelProviders` and `env`.** |
| `.qwen/settings.json`   | Project       | Applies only when running Qwen Code in this project. Overrides user settings.           |

The most commonly used top-level fields in `settings.json`:

| Field                        | Description                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| `modelProviders`             | Define available models per protocol (`openai`, `anthropic`, `gemini`, `vertex-ai`).                 |
| `env`                        | Fallback environment variables (e.g. API keys). Lower priority than shell `export` and `.env` files. |
| `security.auth.selectedType` | The protocol to use on startup (e.g. `openai`).                                                      |
| `model.name`                 | The default model to use when Qwen Code starts.                                                      |

> See the [Authentication](#api-key-flexible) section above for complete `settings.json` examples, and the [settings reference](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/) for all available options.

## 基准测试结果

### Terminal-Bench Performance

| Agent     | Model              | Accuracy |
| --------- | ------------------ | -------- |
| Qwen Code | Qwen3-Coder-480A35 | 37.5%    |
| Qwen Code | Qwen3-Coder-30BA3B | 31.3%    |

## 生态工具

寻找图形化界面？

- [**AionUi**](https://github.com/iOfficeAI/AionUi) A modern GUI for command-line AI tools including Qwen Code
- [**Gemini CLI Desktop**](https://github.com/Piebald-AI/gemini-cli-desktop) A cross-platform desktop/web/mobile UI for Qwen Code

## 常见问题排查

If you encounter issues, check the [troubleshooting guide](https://qwenlm.github.io/qwen-code-docs/en/users/support/troubleshooting/).

**Common issues:**

- **`Qwen OAuth free tier was discontinued on 2026-04-15`**: Qwen OAuth is no longer available. Run `qwen` → `/auth` and switch to API Key or Coding Plan. See the [Authentication](#authentication) section above for setup instructions.

To report a bug from within the CLI, run `/bug` and include a short title and repro steps.

## 联系我们

- Discord: https://discord.gg/RN7tqZCeDK
- Dingtalk: https://qr.dingtalk.com/action/joingroup?code=v1,k1,+FX6Gf/ZDlTahTIRi8AEQhIaBlqykA0j+eBKKdhLeAE=&_dt_no_comment=1&origin=1

## 致谢

This project is based on [Google Gemini CLI](https://github.com/google-gemini/gemini-cli). We acknowledge and appreciate the excellent work of the Gemini CLI team. Our main contribution focuses on parser-level adaptations to better support Qwen-Coder models.