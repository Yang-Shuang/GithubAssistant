<p align="center">
  <a href="https://vibekanban.com">
    <picture>
      <source srcset="packages/public/vibe-kanban-logo-dark.svg" media="(prefers-color-scheme: dark)">
      <source srcset="packages/public/vibe-kanban-logo.svg" media="(prefers-color-scheme: light)">
      <img src="packages/public/vibe-kanban-logo.svg" alt="Vibe Kanban Logo">
    </picture>
  </a>
</p>

<p align="center">从 Claude Code、Gemini CLI、Codex、Amp 及其他代码代理中获取 10 倍效能...</p>
<p align="center">
  <a href="https://www.npmjs.com/package/vibe-kanban"><img alt="npm" src="https://img.shields.io/npm/v/vibe-kanban?style=flat-square" /></a>
  <a href="https://github.com/BloopAI/vibe-kanban/blob/main/.github/workflows/publish.yml"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/BloopAI/vibe-kanban/.github%2Fworkflows%2Fpublish.yml" /></a>
  <a href="https://deepwiki.com/BloopAI/vibe-kanban"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<h1 align="center">
  <strong>Vibe Kanban 即将停止服务。</strong>
  <a href="https://www.vibekanban.com/blog/shutdown">阅读公告。</a>
</h1>

![](packages/public/vibe-kanban-screenshot-overview.png)

## 项目概述

在软件工程师将大部分时间用于规划与审查代码代理（coding agent）的时代，想要更高效地交付软件，最快的方式就是提升规划和审查的速度。

Vibe Kanban 正是为此而生。你可以使用看板任务（kanban issue）来规划工作，无论是独自进行还是与团队协作。准备就绪后，创建工作区供代码代理执行任务。

- **通过看板任务进行规划** — 在看板板上创建、排序和分配任务
- **在工作区中运行代码代理** — 每个工作区都会为代理提供一个分支、一个终端和一个开发服务器
- **审查差异并提交行内评论** — 直接在界面内向代理发送反馈，无需切换视图
- **预览你的应用** — 内置浏览器支持开发者工具、检查模式和设备模拟
- **在 10+ 种代码代理间切换** — Claude Code、Codex、Gemini CLI、GitHub Copilot、Amp、Cursor、OpenCode、Droid、CCR 和 Qwen Code
- **创建拉取请求并合并** — 使用 AI 生成的描述打开 PR，在 GitHub 上审查后直接合并

![](packages/public/vibe-kanban-screenshot-workspace.png)

一条命令。描述任务、审查差异、完成交付。

```bash
npx vibe-kanban
```


## 安装

确保你已与你常用的代码代理完成身份验证。支持的所有代码代理列表请参阅 [文档](https://vibekanban.com/docs/supported-coding-agents)。然后在终端中运行：

```bash
npx vibe-kanban
```

## 文档

请访问 [官网](https://vibekanban.com/docs) 获取最新文档和用户指南。

## 自托管

想要自行托管 Vibe Kanban Cloud 实例？请参阅我们的 [自托管指南](https://vibekanban.com/docs/self-hosting/deploy-docker)。

## 支持

我们使用 [GitHub Discussions](https://github.com/BloopAI/vibe-kanban/discussions) 收集功能建议。请开启讨论以提交新功能请求。如遇 Bug，请在此仓库创建 Issue。

## 贡献

我们建议先将想法和变更通过 [GitHub Discussions](https://github.com/BloopAI/vibe-kanban/discussions) 或 [Discord](https://discord.gg/AC4nwVtJM3) 与核心团队沟通，以便讨论实现细节及其与现有路线图的一致性。在未与团队讨论提案之前，请勿直接提交 Pull Request（PR）。

## 开发

### 环境要求

- [Rust](https://rustup.rs/)（最新稳定版）
- [Node.js](https://nodejs.org/)（版本 >=20）
- [pnpm](https://pnpm.io/)（版本 >=8）

额外开发工具：
```bash
cargo install cargo-watch
cargo install sqlx-cli
```

安装依赖项：
```bash
pnpm i
```

### 运行开发服务器

```bash
pnpm run dev
```

这将启动后端和 Web 应用。系统将自动从 `dev_assets_seed` 文件夹复制一个空数据库。

### 构建 Web 应用

仅构建 Web 应用：

```bash
cd packages/local-web
pnpm run build
```

### 从源码构建（macOS）

1. 运行 `./local-build.sh`
2. 测试：执行 `cd npx-cli && node bin/cli.js`

### 环境变量

以下环境变量可在构建时或运行时配置：

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `POSTHOG_API_KEY` | Build-time | Empty | PostHog 分析服务 API 密钥（为空则禁用分析功能） |
| `POSTHOG_API_ENDPOINT` | Build-time | Empty | PostHog 分析接口地址（为空则禁用分析功能） |
| `PORT` | Runtime | Auto-assign | **生产环境**：服务器端口。**开发环境**：前端端口（后端使用 PORT+1） |
| `BACKEND_PORT` | Runtime | `0` (auto-assign) | 后端服务器端口（仅限开发模式，覆盖 PORT+1） |
| `FRONTEND_PORT` | Runtime | `3000` | 前端开发服务器端口（仅限开发模式，覆盖 PORT） |
| `HOST` | Runtime | `127.0.0.1` | 后端服务器主机地址 |
| `MCP_HOST` | Runtime | Value of `HOST` | MCP 服务器连接主机（Windows 下当 `HOST=0.0.0.0` 时使用 `127.0.0.1`） |
| `MCP_PORT` | Runtime | Value of `BACKEND_PORT` | MCP 服务器连接端口 |
| `DISABLE_WORKTREE_CLEANUP` | Runtime | Not set | 禁用所有 Git worktree 清理操作，包括孤立和过期的工作区清理（用于调试） |
| `VK_ALLOWED_ORIGINS` | Runtime | Not set | 允许发起后端 API 请求的源地址列表（逗号分隔，例如 `https://my-vibekanban-frontend.com`） |
| `VK_SHARED_API_BASE` | Runtime | Not set | 本地桌面应用使用的远程/云端 API 基础地址 |
| `VK_SHARED_RELAY_API_BASE` | Runtime | Not set | 隧道模式连接使用的中继 API 基础地址 |
| `VK_TUNNEL` | Runtime | Not set | 启用时开启中继隧道模式（需配置中继 API 基础地址） |

**构建时变量**需在运行 `pnpm run build` 时设置。**运行时变量**在应用启动时读取。

#### 通过反向代理或自定义域名自托管

当通过反向代理（如 nginx、Caddy、Traefik）运行 Vibe Kanban，或使用自定义域名时，必须设置 `VK_ALLOWED_ORIGINS` 环境变量。否则浏览器的 Origin 头将无法与后端期望的主机匹配，API 请求将被拒绝并返回 403 Forbidden 错误。

将其设置为前端可访问的完整源地址：

```bash
# Single origin
VK_ALLOWED_ORIGINS=https://vk.example.com

# Multiple origins (comma-separated)
VK_ALLOWED_ORIGINS=https://vk.example.com,https://vk-staging.example.com
```

### 远程部署

当在远程服务器上运行 Vibe Kanban（例如通过 systemctl、Docker 或云托管）时，你可以配置编辑器通过 SSH 打开项目：

1. **通过隧道访问**：使用 Cloudflare Tunnel、ngrok 等工具暴露 Web 界面
2. **在设置中配置远程 SSH**（Settings → Editor Integration）：
   - 将 **Remote SSH Host** 设置为服务器主机名或 IP
   - 将 **Remote SSH User** 设置为你的 SSH 用户名（可选）
3. **前置条件**：
   - 本地机器可访问远程服务器
   - 已配置 SSH 密钥（免密登录）
   - 安装了 VS Code Remote-SSH 扩展

配置完成后，“在 VSCode 中打开”按钮将生成类似 `vscode://vscode-remote/ssh-remote+user@host/path` 的 URL，用于在你的本地编辑器中打开并连接至远程服务器。

详细设置说明请参阅 [文档](https://vibekanban.com/docs/settings/general)。