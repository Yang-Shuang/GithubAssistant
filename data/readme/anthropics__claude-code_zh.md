# Claude Code

![](https://img.shields.io/badge/Node.js-18%2B-brightgreen?style=flat-square) [![npm]](https://www.npmjs.com/package/@anthropic-ai/claude-code)

[npm]: https://img.shields.io/npm/v/@anthropic-ai/claude-code.svg?style=flat-square

Claude Code 是一款集成于终端的智能体编程工具，它能理解你的代码库，并通过自然语言指令执行常规任务、解释复杂代码及处理 Git 工作流，从而助你更高效地编写代码。你可以在终端或 IDE 中使用它，也可在 GitHub 上 @claude。

**更多详情请参阅[官方文档](https://code.claude.com/docs/en/overview)**。

<img src="./demo.gif" />

## 快速开始
> [!NOTE]
> 通过 npm 安装的方式已弃用。请使用下方推荐的任一方法。

如需更多安装选项、卸载步骤及故障排除指南，请参阅[设置文档](https://code.claude.com/docs/en/setup)。

1. 安装 Claude Code：

    **MacOS/Linux（推荐）：**
    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Homebrew（MacOS/Linux）：**
    ```bash
    brew install --cask claude-code
    ```

    **Windows（推荐）：**
    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

    **WinGet（Windows）：**
    ```powershell
    winget install Anthropic.ClaudeCode
    ```

    **NPM（已弃用）：**
    ```bash
    npm install -g @anthropic-ai/claude-code
    ```

2. 进入你的项目目录并运行 `claude`。

## 插件

本仓库包含多个 Claude Code 插件，通过自定义命令和智能体扩展了功能。有关可用插件的详细文档，请参阅[插件目录](./plugins/README.md)。

## 报告问题

我们非常重视你的反馈。你可以在 Claude Code 内部直接使用 `/bug` 命令报告问题，或者提交一个 [GitHub Issue](https://github.com/anthropics/claude-code/issues)。

## 加入 Discord

加入 [Claude 开发者 Discord](https://anthropic.com/discord)，与其他使用 Claude Code 的开发者建立联系。在这里获取帮助、分享反馈，并与社区讨论你的项目。

## 数据收集、使用与保留

当你使用 Claude Code 时，我们会收集反馈信息，其中包括使用情况数据（例如代码接受或拒绝记录）、相关的对话数据，以及通过 `/bug` 命令提交的用户反馈。

### 我们如何使用你的数据

请参阅我们的[数据使用政策](https://code.claude.com/docs/en/data-usage)。

### 隐私保障措施

我们已实施多项措施以保护你的数据，包括对敏感信息设置有限的保留期、限制访问用户会话数据，以及明确禁止将反馈用于模型训练。

完整详情请查阅我们的[商业服务条款](https://www.anthropic.com/legal/commercial-terms)和[隐私政策](https://www.anthropic.com/legal/privacy)。