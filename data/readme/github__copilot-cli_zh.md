# GitHub Copilot CLI

GitHub Copilot 的强大功能，现已进入你的终端。

GitHub Copilot CLI 将基于 AI 的编码辅助直接带入命令行，让你能够通过自然语言对话来构建、调试和理解代码。它采用与 GitHub Copilot 编程智能体相同的底层架构（agentic harness），在深度集成你现有 GitHub 工作流的同时提供智能辅助。

请参阅[我们的官方文档](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)获取更多信息。

![Image of the splash screen for the Copilot CLI](https://github.com/user-attachments/assets/f40aa23d-09dd-499e-9457-1d57d3368887)


## 🚀 简介与概览

我们将 GitHub Copilot 编程智能体的强大功能直接带入你的终端。借助 GitHub Copilot CLI，你可以本地化地与理解你代码和 GitHub 上下文的 AI 智能体同步协作。

- **原生终端开发：**直接在命令行中协同 Copilot 编程智能体工作——无需切换上下文。
- **开箱即用的 GitHub 集成：**使用自然语言访问你的仓库、Issue 和 Pull Request，全部通过你现有的 GitHub 账户进行身份验证。
- **智能体能力：**与 AI 协作者共同构建、编辑、调试和重构代码，该智能体能够规划并执行复杂任务。
- **基于 MCP 的扩展性：**充分利用其默认内置 GitHub MCP Server，且支持自定义 MCP Server 以扩展功能的特性。
- **完全掌控：**在执行前预览每一项操作——未经你明确批准，不会执行任何操作。

我们仍处于早期阶段，但通过你的反馈，我们正在快速迭代，致力于将 GitHub Copilot CLI 打造为终端中最佳的辅助工具。

## 📦 入门指南

### 支持的平台

- **Linux**
- **macOS**
- **Windows**

### 前置条件

- (在 Windows 上) **PowerShell** v6 或更高版本
- **活跃的 Copilot 订阅**。请参阅 [Copilot 计划](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=install-copilot-cli&ref_page=docs)。

如果你通过所在组织或企业使用 GitHub Copilot，且组织管理员或企业管理员在设置中禁用了该功能，则无法使用 GitHub Copilot CLI。请参阅[在你的组织中管理 GitHub Copilot 的策略和功能](http://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization)获取更多信息。

### 安装

使用安装脚本进行安装（适用于 macOS 和 Linux）：

```bash
curl -fsSL https://gh.io/copilot-install | bash
```

或

```bash
wget -qO- https://gh.io/copilot-install | bash
```

添加 `| sudo bash` 以 root 权限运行，并将其安装到 `/usr/local/bin`。

设置 `PREFIX` 可将工具安装至 `$PREFIX/bin/` 目录。默认为：root 用户下为 `/usr/local`，非 root 用户下为 `$HOME/.local`。

设置 `VERSION` 可指定安装的版本。默认安装最新版本。

例如，将版本 `v0.0.369` 安装到自定义目录：

```bash
curl -fsSL https://gh.io/copilot-install | VERSION="v0.0.369" PREFIX="$HOME/custom" bash
```

使用 [Homebrew](https://formulae.brew.sh/cask/copilot-cli) 进行安装（适用于 macOS 和 Linux）：

```bash
brew install copilot-cli
```

```bash
brew install copilot-cli@prerelease
```


使用 [WinGet](https://github.com/microsoft/winget-cli) 进行安装（适用于 Windows）：

```bash
winget install GitHub.Copilot
```

```bash
winget install GitHub.Copilot.Prerelease
```


使用 [npm](https://www.npmjs.com/package/@github/copilot) 进行安装（适用于 macOS、Linux 和 Windows）：

```bash
npm install -g @github/copilot
```

```bash
npm install -g @github/copilot@prerelease
```


### 启动 CLI

```bash
copilot
```

首次启动时，你会看到我们可爱的动态横幅！若想再次显示该横幅，可在使用 `copilot` 命令时添加 `--banner` 标志。

如果你尚未登录 GitHub，系统将提示你使用 `/login` 斜杠命令。输入该命令并按照屏幕指示完成身份验证即可。

#### 通过个人访问令牌（PAT）进行认证

你也可以使用启用了“Copilot Requests”权限的细粒度 PAT 进行身份验证。

1. 访问 https://github.com/settings/personal-access-tokens/new
2. 在“Permissions（权限）”下，点击“add permissions”，然后选择“Copilot Requests”
3. 生成你的令牌
4. 通过环境变量 `GH_TOKEN` 或 `GITHUB_TOKEN`（按优先级顺序）将令牌添加到你的环境中

### 使用 CLI

在包含你要处理的代码的文件夹中启动 `copilot`。

默认情况下，`copilot` 使用 Claude Sonnet 4.5。运行 `/model` 斜杠命令可选择其他可用模型，包括 Claude Sonnet 4 和 GPT-5。

### 实验模式

实验模式可让你访问仍在开发中的新功能。你可以通过以下方式激活实验模式：

- 使用 `--experimental` 标志启动：`copilot --experimental`
- 在 CLI 内使用 `/experimental` 斜杠命令

激活后，该设置会持久化保存至你的配置文件中，因此后续启动时不再需要添加 `--experimental` 标志。

#### 实验性功能

- **自动执行模式（Autopilot）：**这是一种新模式（按 `Shift+Tab` 切换模式），旨在让智能体持续工作直至任务完成。

每次向 GitHub Copilot CLI 提交提示词，都会消耗你每月的高级请求配额一次。关于高级请求的详细信息，请参阅[关于高级请求](https://docs.github.com/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests)。

有关如何使用 GitHub Copilot CLI 的更多信息，请参阅[我们的官方文档](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)。

## 🔧 配置 LSP Server

GitHub Copilot CLI 支持语言服务器协议（LSP）以增强代码智能分析功能。该功能提供诸如“转到定义”、悬停提示和诊断等智能代码辅助。

### 安装语言服务器

Copilot CLI 未内置 LSP Server，你需要单独安装它们。例如，配置 TypeScript 支持：

```bash
npm install -g typescript-language-server
```

对于其他语言，请安装对应的 LSP Server，并按照下方示例进行配置。

### 配置 LSP Server

LSP Server 通过专用的配置文件进行管理。你可以在用户级别或仓库级别进行配置：

**用户级配置**（适用于所有项目）：
编辑 `~/.copilot/lsp-config.json`

**仓库级配置**（适用于特定项目）：
在仓库根目录创建 `.github/lsp.json`

示例配置：

```json
{
  "lspServers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "fileExtensions": {
        ".ts": "typescript",
        ".tsx": "typescript"
      }
    }
  }
}
```

### 查看 LSP Server 状态

在交互式会话中使用 `/lsp` 命令检查已配置的 LSP Server，或直接查看你的配置文件。

更多信息请参阅[更新日志](./changelog.md)。

## 📢 反馈与参与

很高兴你能在 Copilot CLI 的早期阶段加入我们。

我们正处于快速迭代期，更新将十分频繁——请保持客户端为最新版本以获取最新功能与修复！

你的见解至关重要！欢迎在此仓库提交 Issue、加入 Discussions，或在 CLI 中运行 `/feedback` 参与保密反馈调查！