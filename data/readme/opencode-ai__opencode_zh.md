# 已归档：项目已迁移

该仓库已停止维护，仅为保留历史版本而归档。

该项目已由原作者与 Charm 团队以 [Crush][crush] 的名称继续开发。

请持续关注 [Crush][crush] 获取最新进展。

[crush]: https://github.com/charmbracelet/crush


# ⌬ OpenCode

<p align="center"><img src="https://github.com/user-attachments/assets/9ae61ef6-70e5-4876-bc45-5bcb4e52c714" width="800"></p>

> **⚠️ 早期开发说明：** 本项目处于早期开发阶段，尚未达到生产环境使用标准。功能可能随时变更、破坏或存在不完整之处。请自行承担使用风险。

一款面向开发者的强大终端 AI 助手，直接在终端中提供智能编码辅助。

## 概述

OpenCode 是一款基于 Go 语言的 CLI 应用程序，将 AI 辅助功能带入你的终端。它提供了一个 TUI（Terminal User Interface，终端用户界面），用于与各种 AI 模型交互，以协助编码、调试等任务。

<p>如需快速了解视频演示，请查看
<a href="https://www.youtube.com/watch?v=P8luPmEa1QI"><img width="25" src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg"> OpenCode + Gemini 2.5 Pro: BYE Claude Code! I'm SWITCHING To the FASTEST AI Coder!</a></p>

<a href="https://www.youtube.com/watch?v=P8luPmEa1QI"><img width="550" src="https://i3.ytimg.com/vi/P8luPmEa1QI/maxresdefault.jpg"></a><p>

## 功能特性

- **交互式 TUI**：基于 [Bubble Tea](https://github.com/charmbracelet/bubbletea) 构建，提供流畅的终端体验
- **多模型支持**：兼容 OpenAI、Anthropic Claude、Google Gemini、AWS Bedrock、Groq、Azure OpenAI 及 OpenRouter
- **会话管理**：保存并管理多个对话会话
- **工具集成**：支持 AI 执行命令、搜索文件及修改代码
- **类 Vim 编辑器**：内置文本输入与编辑功能
- **持久化存储**：使用 SQLite 数据库保存对话与会话记录
- **LSP 集成**：支持语言服务器协议（Language Server Protocol），提供代码智能提示
- **文件变更追踪**：在会话中实时跟踪并可视化文件更改
- **外部编辑器支持**：可调用你偏好的编辑器来编写消息
- **自定义命令命名参数**：通过多个命名占位符创建强大的自定义命令

## 安装方式

### 使用安装脚本

```bash
# 安装最新版本
curl -fsSL https://raw.githubusercontent.com/opencode-ai/opencode/refs/heads/main/install | bash

# 安装指定版本
curl -fsSL https://raw.githubusercontent.com/opencode-ai/opencode/refs/heads/main/install | VERSION=0.1.0 bash
```

### 使用 Homebrew（macOS 和 Linux）

```bash
brew install opencode-ai/tap/opencode
```

### 使用 AUR（Arch Linux）

```bash
# 使用 yay
yay -S opencode-ai-bin

# 使用 paru
paru -S opencode-ai-bin
```

### 使用 Go

```bash
go install github.com/opencode-ai/opencode@latest
```

## 配置

OpenCode 将在以下位置查找配置文件：

- `$HOME/.opencode.json`
- `$XDG_CONFIG_HOME/opencode/.opencode.json`
- `./.opencode.json`（本地目录）

### 自动压缩功能

OpenCode 内置了自动压缩（autoCompact）功能，当对话接近模型上下文窗口限制时，会自动对你的对话进行摘要总结。启用后（默认开启），该功能将：

- 实时监控会话中的 Token 使用情况
- 当使用量达到模型上下文窗口的 95% 时自动触发摘要生成
- 基于摘要创建新会话，让你在不丢失上下文的情况下继续工作
- 有效避免长对话中常见的“超出上下文”错误

你可以在配置文件中启用或禁用此功能：

```json
{
  "autoCompact": true // default is true
}
```

### 环境变量

你可以通过环境变量来配置 OpenCode：

| 环境变量                 | 用途                                                                     |
| ------------------------ | ------------------------------------------------------------------------ |
| `ANTHROPIC_API_KEY`      | Claude 模型 API 密钥                                                     |
| `OPENAI_API_KEY`         | OpenAI 模型 API 密钥                                                     |
| `GEMINI_API_KEY`         | Google Gemini 模型 API 密钥                                              |
| `GITHUB_TOKEN`           | GitHub Copilot 模型 Token（详见 [使用 GitHub Copilot](#使用-github-copilot)） |
| `VERTEXAI_PROJECT`       | Google Cloud VertexAI (Gemini)                                           |
| `VERTEXAI_LOCATION`      | Google Cloud VertexAI (Gemini)                                           |
| `GROQ_API_KEY`           | Groq 模型 API 密钥                                                       |
| `AWS_ACCESS_KEY_ID`      | AWS Bedrock (Claude) Access Key                                          |
| `AWS_SECRET_ACCESS_KEY`  | AWS Bedrock (Claude) Secret Key                                          |
| `AWS_REGION`             | AWS Bedrock (Claude) Region                                              |
| `AZURE_OPENAI_ENDPOINT`  | Azure OpenAI 模型端点                                                    |
| `AZURE_OPENAI_API_KEY`   | Azure OpenAI 模型 API 密钥（使用 Entra ID 时可选）                       |
| `AZURE_OPENAI_API_VERSION` | Azure OpenAI 模型 API 版本                                             |
| `LOCAL_ENDPOINT`         | 自托管模型端点                                                           |
| `SHELL`                  | 默认使用的 Shell（若配置文件中未指定）                                   |

### Shell 配置

OpenCode 允许你配置 `bash` 工具使用的 Shell。默认情况下，它使用 `SHELL` 环境变量指定的 Shell；若未设置，则回退至 `/bin/bash`。

你可以在配置文件中覆盖此设置：

```json
{
  "shell": {
    "path": "/bin/zsh",
    "args": ["-l"]
  }
}
```

如果你希望使用与系统默认不同的 Shell，或需要向 Shell 传递特定参数（如 `-l`），这将非常有用。

### 配置文件结构

```json
{
  "data": {
    "directory": ".opencode"
  },
  "providers": {
    "openai": {
      "apiKey": "your-api-key",
      "disabled": false
    },
    "anthropic": {
      "apiKey": "your-api-key",
      "disabled": false
    },
    "copilot": {
      "disabled": false
    },
    "groq": {
      "apiKey": "your-api-key",
      "disabled": false
    },
    "openrouter": {
      "apiKey": "your-api-key",
      "disabled": false
    }
  },
  "agents": {
    "coder": {
      "model": "claude-3.7-sonnet",
      "maxTokens": 5000
    },
    "task": {
      "model": "claude-3.7-sonnet",
      "maxTokens": 5000
    },
    "title": {
      "model": "claude-3.7-sonnet",
      "maxTokens": 80
    }
  },
  "shell": {
    "path": "/bin/bash",
    "args": ["-l"]
  },
  "mcpServers": {
    "example": {
      "type": "stdio",
      "command": "path/to/mcp-server",
      "env": [],
      "args": []
    }
  },
  "lsp": {
    "go": {
      "disabled": false,
      "command": "gopls"
    }
  },
  "debug": false,
  "debugLSP": false,
  "autoCompact": true
}
```

## 支持的 AI 模型

OpenCode 支持来自不同提供商的多种 AI 模型：

### OpenAI

- GPT-4.1 family (gpt-4.1, gpt-4.1-mini, gpt-4.1-nano)
- GPT-4.5 Preview
- GPT-4o family (gpt-4o, gpt-4o-mini)
- O1 family (o1, o1-pro, o1-mini)
- O3 family (o3, o3-mini)
- O4 Mini

### Anthropic

- Claude 4 Sonnet
- Claude 4 Opus
- Claude 3.5 Sonnet
- Claude 3.5 Haiku
- Claude 3.7 Sonnet
- Claude 3 Haiku
- Claude 3 Opus

### GitHub Copilot

- GPT-3.5 Turbo
- GPT-4
- GPT-4o
- GPT-4o Mini
- GPT-4.1
- Claude 3.5 Sonnet
- Claude 3.7 Sonnet
- Claude 3.7 Sonnet Thinking
- Claude Sonnet 4
- O1
- O3 Mini
- O4 Mini
- Gemini 2.0 Flash
- Gemini 2.5 Pro

### Google

- Gemini 2.5
- Gemini 2.5 Flash
- Gemini 2.0 Flash
- Gemini 2.0 Flash Lite

### AWS Bedrock

- Claude 3.7 Sonnet

### Groq

- Llama 4 Maverick (17b-128e-instruct)
- Llama 4 Scout (17b-16e-instruct)
- QWEN QWQ-32b
- Deepseek R1 distill Llama 70b
- Llama 3.3 70b Versatile

### Azure OpenAI

- GPT-4.1 family (gpt-4.1, gpt-4.1-mini, gpt-4.1-nano)
- GPT-4.5 Preview
- GPT-4o family (gpt-4o, gpt-4o-mini)
- O1 family (o1, o1-mini)
- O3 family (o3, o3-mini)
- O4 Mini

### Google Cloud VertexAI

- Gemini 2.5
- Gemini 2.5 Flash

## 使用方法

```bash
# 启动 OpenCode
opencode

# 以调试日志模式启动
opencode -d

# 指定工作目录启动
opencode -c /path/to/project
```

## 非交互式提示模式

你可以通过将提示词直接作为命令行参数传递，以非交互模式运行 OpenCode。这适用于脚本编写、自动化任务，或当你需要快速获得答案而无需启动完整 TUI 时。

```bash
# 执行单次提示并打印 AI 回复到终端
opencode -p "Explain the use of context in Go"

# 以 JSON 格式获取响应
opencode -p "Explain the use of context in Go" -f json

# 静默模式运行（不显示加载动画，适用于脚本）
opencode -p "Explain the use of context in Go" -q
```

在此模式下，OpenCode 会处理你的提示词，将结果打印到标准输出，然后退出。会话期间所有权限请求均自动批准。

默认情况下，模型在处理查询时会显示加载动画（旋转图标）。你可以使用 `-q` 或 `--quiet` 标志禁用此动画，这在从脚本或自动化工作流中运行 OpenCode 时特别有用。

### 输出格式

OpenCode 在非交互模式下支持以下输出格式：

| Format | Description                     |
| ------ | ------------------------------- |
| `text` | 纯文本输出（默认）              |
| `json` | JSON 对象包裹的输出             |

输出格式在代码中实现为强类型的 `OutputFormat`，确保在处理输出时具备类型安全与验证机制。

## 命令行参数

| Flag              | Short | Description                                         |
| ----------------- | ----- | --------------------------------------------------- |
| `--help`          | `-h`  | 显示帮助信息                                        |
| `--debug`         | `-d`  | 启用调试模式                                        |
| `--cwd`           | `-c`  | 设置当前工作目录                                    |
| `--prompt`        | `-p`  | 在非交互模式下执行单次提示                          |
| `--output-format` | `-f`  | 非交互模式的输出格式（text, json）                  |
| `--quiet`         | `-q`  | 隐藏非交互模式下的加载动画                          |

## 键盘快捷键

### 全局快捷键

| Shortcut | Action                                                  |
| -------- | ------------------------------------------------------- |
| `Ctrl+C` | 退出应用                                                |
| `Ctrl+?` | 切换帮助对话框                                          |
| `?`      | 切换帮助对话框（非编辑模式下）                          |
| `Ctrl+L` | 查看日志                                                |
| `Ctrl+A` | 切换会话                                                |
| `Ctrl+K` | 打开命令对话框                                          |
| `Ctrl+O` | 切换模型选择对话框                                      |
| `Esc`    | 关闭当前覆盖层/对话框，或返回上一级模式                 |

### 聊天页面快捷键

| Shortcut | Action                                  |
| -------- | --------------------------------------- |
| `Ctrl+N` | 创建新会话                              |
| `Ctrl+X` | 取消当前操作/生成                       |
| `i`      | 聚焦编辑器（非写作模式下）              |
| `Esc`    | 退出写作模式并聚焦消息区                |

### 编辑器快捷键

| Shortcut            | Action                                    |
| ------------------- | ----------------------------------------- |
| `Ctrl+S`            | 发送消息（当编辑器获得焦点时）            |
| `Enter` or `Ctrl+S` | 发送消息（当编辑器未获得焦点时）          |
| `Ctrl+E`            | 打开外部编辑器                            |
| `Esc`               | 失去编辑器焦点并聚焦消息区                |

### 会话对话框快捷键

| Shortcut   | Action           |
| ---------- | ---------------- |
| `↑` or `k` | 上一个会话       |
| `↓` or `j` | 下一个会话       |
| `Enter`    | 选中当前会话     |
| `Esc`      | 关闭对话框       |

### 模型选择对话框快捷键

| Shortcut   | Action            |
| ---------- | ----------------- |
| `↑` or `k` | 上移              |
| `↓` or `j` | 下移              |
| `←` or `h` | 上一个提供商      |
| `→` or `l` | 下一个提供商      |
| `Esc`      | 关闭对话框        |

### 权限确认对话框快捷键

| Shortcut                | Action                       |
| ----------------------- | ---------------------------- |
| `←` or `left`           | 向左切换选项                 |
| `→` or `right` or `tab` | 向右切换选项                 |
| `Enter` or `space`      | 确认选择                     |
| `a`                     | 允许权限                     |
| `A`                     | 允许本次会话的权限           |
| `d`                     | 拒绝权限                     |

### 日志页面快捷键

| Shortcut           | Action              |
| ------------------ | ------------------- |
| `Backspace` or `q` | 返回聊天页面        |

## AI 助手工具

OpenCode 的 AI 助手可调用多种工具来协助编码任务：

### 文件与代码工具

| Tool          | Description                 | Parameters                                                                               |
| ------------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| `glob`        | 按模式查找文件              | `pattern`（必填），`path`（可选）                                                        |
| `grep`        | 搜索文件内容                | `pattern`（必填），`path`（可选），`include`（可选），`literal_text`（可选）             |
| `ls`          | 列出目录内容                | `path`（可选），`ignore`（可选，包含模式的数组）                                         |
| `view`        | 查看文件内容                | `file_path`（必填），`offset`（可选），`limit`（可选）                                   |
| `write`       | 写入文件                    | `file_path`（必填），`content`（必填）                                                   |
| `edit`        | 编辑文件                    | 各种文件编辑相关参数                                                                     |
| `patch`       | 对文件应用补丁              | `file_path`（必填），`diff`（必填）                                                      |
| `diagnostics` | 获取诊断信息                | `file_path`（可选）                                                                      |

### 其他工具

| Tool          | Description                            | Parameters                                                                                |
| ------------- | -------------------------------------- | ----------------------------------------------------------------------------------------- |
| `bash`        | 执行 Shell 命令                        | `command`（必填），`timeout`（可选）                                                      |
| `fetch`       | 从 URL 获取数据                        | `url`（必填），`format`（必填），`timeout`（可选）                                        |
| `sourcegraph` | 在公开代码仓库中搜索                   | `query`（必填），`count`（可选），`context_window`（可选），`timeout`（可选）             |
| `agent`       | 运行由 AI agent 执行子任务             | `prompt`（必填）                                                                          |

## 架构设计

OpenCode 采用模块化架构构建：

- **cmd**：基于 Cobra 的命令行接口
- **internal/app**：核心应用服务
- **internal/config**：配置管理
- **internal/db**：数据库操作与迁移
- **internal/llm**：LLM 提供商集成与工具调用
- **internal/tui**：终端 UI 组件与布局
- **internal/logging**：日志基础设施
- **internal/message**：消息处理
- **internal/session**：会话管理
- **internal/lsp**：语言服务器协议（LSP）集成

## 自定义命令

OpenCode 支持用户创建的自定义命令，用于快速向 AI 助手发送预设提示词。

### 创建自定义命令

自定义命令是预定义的提示词，以 Markdown 文件的形式存储在以下三个位置之一：

1. **用户命令**（前缀为 `user:`）：

   ```
   $XDG_CONFIG_HOME/opencode/commands/
   ```

   （通常在 Linux/macOS 上为 `~/.config/opencode/commands/`）

   或

   ```
   $HOME/.opencode/commands/
   ```

2. **项目命令**（前缀为 `project:`）：

   ```
   <PROJECT DIR>/.opencode/commands/
   ```

这些目录中的每个 `.md` 文件都会成为一个自定义命令。文件名（不含扩展名）即为该命令的 ID。

例如，在 `~/.config/opencode/commands/prime-context.md` 创建文件并写入以下内容：

```markdown
RUN git ls-files
READ README.md
```

这将创建一个名为 `user:prime-context` 的命令。

### 命令参数

OpenCode 支持在自定义命令中使用命名参数，占位符格式为 `$NAME`（NAME 由大写字母、数字和下划线组成，且必须以字母开头）。

例如：

```markdown
# Fetch Context for Issue $ISSUE_NUMBER

RUN gh issue view $ISSUE_NUMBER --json title,body,comments
RUN git grep --author="$AUTHOR_NAME" -n .
RUN grep -R "$SEARCH_PATTERN" $DIRECTORY
```

运行带参数的命令时，OpenCode 会提示你为每个唯一的占位符输入值。命名参数具有以下优势：

- 清晰标识每个参数的含义
- 支持重复使用同一参数
- 便于管理包含多个输入的复杂命令

### 组织命令

你可以通过子目录来组织命令：

```
~/.config/opencode/commands/git/commit.md
```

这将创建一个 ID 为 `user:git:commit` 的命令。

### 使用自定义命令

1. 按 `Ctrl+K` 打开命令对话框
2. 选择你的自定义命令（前缀为 `user:` 或 `project:`）
3. 按 `Enter` 执行命令

命令文件的内容将作为消息发送给 AI 助手。

### 内置命令

OpenCode 自带以下内置命令：

| Command            | Description                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| Initialize Project | 创建或更新 OpenCode.md 记忆文件，写入项目特定信息                                                     |
| Compact Session    | 手动触发当前会话的摘要生成，并基于摘要创建新会话                                                      |

## MCP（模型上下文协议）

OpenCode 实现了模型上下文协议（MCP），通过外部工具扩展其功能。MCP 为 AI 助手与外部服务及工具的交互提供了标准化方式。

### MCP 特性

- **外部工具集成**：通过标准化协议连接外部工具与服务
- **工具发现**：自动从 MCP 服务器发现可用工具
- **多种连接类型**：
  - **Stdio**：通过标准输入/输出与工具通信
  - **SSE**：通过服务器发送事件（Server-Sent Events）与工具通信
- **安全性**：内置权限系统，控制对 MCP 工具的访问

### 配置 MCP 服务器

MCP 服务器在配置文件的 `mcpServers` 部分中定义：

```json
{
  "mcpServers": {
    "example": {
      "type": "stdio",
      "command": "path/to/mcp-server",
      "env": [],
      "args": []
    },
    "web-example": {
      "type": "sse",
      "url": "https://example.com/mcp",
      "headers": {
        "Authorization": "Bearer token"
      }
    }
  }
}
```

### MCP 工具使用

配置完成后，MCP 工具将自动对 AI 助手可用（与内置工具并列）。它们遵循与其他工具相同的权限模型，执行前需获得用户批准。

## LSP（语言服务器协议）

OpenCode 集成了语言服务器协议（LSP），以跨多种编程语言提供代码智能功能。

### LSP 特性

- **多语言支持**：连接不同编程语言的服务器
- **诊断信息**：接收错误检查与代码规范提示
- **文件监听**：自动将文件变更通知给语言服务器

### 配置 LSP

语言服务器在配置文件的 `lsp` 部分中定义：

```json
{
  "lsp": {
    "go": {
      "disabled": false,
      "command": "gopls"
    },
    "typescript": {
      "disabled": false,
      "command": "typescript-language-server",
      "args": ["--stdio"]
    }
  }
}
```

### LSP 与 AI 的集成

AI 助手可通过 `diagnostics`（诊断）工具访问 LSP 功能，从而实现：

- 检查代码中的错误
- 根据诊断结果提供修复建议

尽管 LSP 客户端实现支持完整的 LSP 协议（包括补全、悬停提示、定义跳转等），但目前仅向 AI 助手开放了诊断功能。

## 使用 GitHub Copilot

_Copilot 支持目前处于实验阶段。_

### 前置要求
- 在 GitHub 设置中启用 [IDE 中的 Copilot 聊天功能](https://github.com/settings/copilot)
- 满足以下任一条件：
  - VSCode GitHub Copilot chat extension（扩展）
  - GitHub `gh` CLI
  - Neovim GitHub Copilot plugin (`copilot.vim` or `copilot.lua`)
  - 具有 Copilot 权限的 GitHub Token

如果使用上述插件或 CLI 工具，请确保使用该工具登录你的 GitHub 账号。这将在以下位置之一生成一个 GitHub Token：
- ~/.config/github-copilot/[hosts,apps].json
- $XDG_CONFIG_HOME/github-copilot/[hosts,apps].json

如果使用显式的 GitHub Token，你可以设置 `$GITHUB_TOKEN` 环境变量，或将其添加到 `opencode.json` 配置文件的 `providers.copilot.apiKey` 字段中。

## 使用自托管模型服务

OpenCode 还支持加载和使用来自自托管（类 OpenAI）服务的模型。这对于想要试用自定义模型的开发者来说非常有用。

### 配置自托管服务

你可以通过设置 `LOCAL_ENDPOINT` 环境变量来使用自托管模型。这将使 OpenCode 加载并使用指定端点上的模型。

```bash
LOCAL_ENDPOINT=http://localhost:1235/v1
```

### 配置自托管模型

你也可以在配置文件的 `agents` 部分配置自托管模型：

```json
{
  "agents": {
    "coder": {
      "model": "local.granite-3.3-2b-instruct@q8_0",
      "reasoningEffort": "high"
    }
  }
}
```

## 开发指南

### 环境要求

- Go 1.24.0 或更高版本

### 从源码构建

```bash
# 克隆仓库
git clone https://github.com/opencode-ai/opencode.git
cd opencode

# 编译
go build -o opencode

# 运行
./opencode
```

## 鸣谢

OpenCode 衷心感谢以下关键个人的贡献与支持：

- [@isaacphi](https://github.com/isaacphi) —— 提供 [mcp-language-server](https://github.com/isaacphi/mcp-language-server) 项目，为本项目的 LSP 客户端实现奠定了基础
- [@adamdottv](https://github.com/adamdottv) —— 负责整体设计方向与 UI/UX 架构

特别感谢更广泛的开源社区，正是你们提供的工具与库让本项目得以实现。

## 许可证

OpenCode 采用 MIT 许可证发布。详情请参阅 [LICENSE](LICENSE) 文件。

## 贡献指南

欢迎贡献代码！你可以通过以下方式参与：

1. Fork 本仓库
2. 创建功能分支（`git checkout -b feature/amazing-feature`）
3. 提交你的更改（`git commit -m 'Add some amazing feature'`）
4. 推送到分支（`git push origin feature/amazing-feature`）
5. 发起 Pull Request

请确保在提交前更新相关测试，并遵循现有的代码风格规范。