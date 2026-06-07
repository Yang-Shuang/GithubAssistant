<div align="center">

<img width="full" alt="Superset" src="apps/marketing/public/images/readme-hero.png" />

### 专为 AI 代理打造的代码编辑器

[![GitHub stars](https://img.shields.io/github/stars/superset-sh/superset?style=flat&logo=github)](https://github.com/superset-sh/superset/stargazers)
[![GitHub release](https://img.shields.io/github/v/release/superset-sh/superset?style=flat&logo=github)](https://github.com/superset-sh/superset/releases)
[![License](https://img.shields.io/github/license/superset-sh/superset?style=flat)](LICENSE.md)
[![Twitter](https://img.shields.io/badge/@superset__sh-555?logo=x)](https://x.com/superset_sh)
[![Discord](https://img.shields.io/badge/Discord-555?logo=discord)](https://discord.gg/cZeD9WYcV7)

<br />

并行编排 Claude Code、Codex 等 AI 代理集群。<br />
兼容任意 CLI 代理。专为本地 worktree（工作树）开发模式构建。

<br />

[**下载 macOS 版本**](https://github.com/superset-sh/superset/releases/latest) &nbsp;&bull;&nbsp; [文档](https://docs.superset.sh) &nbsp;&bull;&nbsp; [更新日志](https://github.com/superset-sh/superset/releases) &nbsp;&bull;&nbsp; [Discord](https://discord.gg/cZeD9WYcV7)

<br />


</div>

## 零切换成本，代码编写效率提升 10 倍

Superset 在隔离的 Git worktree（工作树）中编排基于 CLI 的代码代理，内置终端、审查及编辑器打开工作流。

- **同时运行多个代理**，无需承担上下文切换开销
- **隔离每个任务**至独立的 git worktree，避免代理间相互干扰
- **集中监控所有代理**，并在需要人工干预时及时通知你
- 使用内置的差异查看器和编辑器**快速审查与编辑变更内容**
- **一键将任意工作区移交至编辑器或终端**，随时调用

减少等待，加速交付。

## 功能特性

| 功能特性 | 说明 |
|:--------|:------------|
| **并行执行** | 在本地机器上同时运行 10 个以上的代码代理 |
| **worktree 隔离** | 每个任务拥有独立的分支和工作目录 |
| **代理监控** | 跟踪代理状态，并在变更就绪时接收通知 |
| **内置差异查看器** | 无需离开应用即可检查并编辑代理的修改内容 |
| **工作区预设** | 自动化环境变量配置、依赖安装等流程 |
| **通用兼容性** | 兼容任何可在终端运行的 CLI 代理 |
| **快速上下文切换** | 根据任务需求随时跳转，响应人工干预 |
| **IDE 集成** | 一键将任意工作区打开到你偏爱的编辑器中 |

## 支持的代理

Superset 兼容所有基于 CLI 的代码代理，包括：

| 代理名称 | 支持状态 |
|:------|:-------|
| <img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/amp.svg" /> &nbsp;[Amp Code](https://ampcode.com/) | 完全支持 |
| <img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/claude.svg" /> &nbsp;[Claude Code](https://github.com/anthropics/claude-code) | 完全支持 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="packages/ui/src/assets/icons/preset-icons/codex-white.svg" /><img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/codex.svg" /></picture> &nbsp;[OpenAI Codex CLI](https://github.com/openai/codex) | 完全支持 |
| <img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/cursor.svg" /> &nbsp;[Cursor Agent](https://docs.cursor.com/agent) | 完全支持 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="packages/ui/src/assets/icons/preset-icons/droid-white.svg" /><img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/droid.svg" /></picture> &nbsp;[Droid](https://www.factory.ai/) | 完全支持 |
| <img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/gemini.svg" /> &nbsp;[Gemini CLI](https://github.com/google-gemini/gemini-cli) | 完全支持 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="packages/ui/src/assets/icons/preset-icons/copilot-white.svg" /><img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/copilot.svg" /></picture> &nbsp;[GitHub Copilot](https://github.com/features/copilot) | 完全支持 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="packages/ui/src/assets/icons/preset-icons/mastracode-white.svg" /><img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/mastracode.svg" /></picture> &nbsp;[Mastra Code](https://mastra.ai/) | 完全支持 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="packages/ui/src/assets/icons/preset-icons/opencode-white.svg" /><img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/opencode.svg" /></picture> &nbsp;[OpenCode](https://github.com/opencode-ai/opencode) | 完全支持 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="packages/ui/src/assets/icons/preset-icons/pi-white.svg" /><img height="16" align="top" src="packages/ui/src/assets/icons/preset-icons/pi.svg" /></picture> &nbsp;[Pi](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent) | 完全支持 |
| 其他任意 CLI 代理 | 无需配置即可使用 |

只要能在终端运行，Superset 就能调度它。

## 系统要求

| 要求 | 说明 |
|:------------|:--------|
| **操作系统** | macOS（Windows/Linux 尚未测试） |
| **运行环境** | [Bun](https://bun.sh/) v1.0+ |
| **版本控制** | Git 2.20+ |
| **GitHub CLI** | [gh](https://cli.github.com/) |
| **Caddy** | [caddy](https://caddyserver.com/docs/install)（用于开发服务器） |

## 安装

**[下载 Superset macOS 版](https://github.com/superset-sh/superset/releases/latest)**

Windows 和 Linux 版本尚未提供。

## 本地开发

想要修改 Superset 源码或贡献 PR？只需一条命令即可启动本地开发环境：

```bash
git clone https://github.com/superset-sh/superset.git
cd superset
./.superset/setup.local.sh
bun run dev
```

无需 Neon 账号或第三方凭据——`setup.local.sh` 会通过 Docker 启动本地 Postgres + Electric 服务栈，并预置开发账号。点击 **“以开发者身份登录”**（或使用 `admin@local.test` / `supersetdev`）即可登录。

前置依赖：`bun`、`docker`、`jq`、`caddy`（执行 `brew install jq caddy && caddy trust`）。

完整指南请参阅 [**DEVELOPMENT.md**](./DEVELOPMENT.md) ——了解安装脚本的作用、针对真实服务的配置方法、常用命令、故障排除及桌面应用构建流程。贡献规范详见 [**CONTRIBUTING.md**](./CONTRIBUTING.md)。

## 键盘快捷键

所有快捷键均可通过 **设置 > 键盘快捷键** (`⌘/`) 进行自定义。详见[完整文档](https://docs.superset.sh/keyboard-shortcuts)。

### 工作区导航

| 快捷键 | 操作 |
|:---------|:-------|
| `⌘1-9` | 切换至工作区 1-9 |
| `⌘⌥↑/↓` | 上一个/下一个工作区 |
| `⌘N` | 新建工作区 |
| `⌘⇧N` | 快速创建工作区 |
| `⌘⇧O` | 打开项目 |

### 终端

| 快捷键 | 操作 |
|:---------|:-------|
| `⌘T` | 新建标签页 |
| `⌘W` | 关闭窗格/终端 |
| `⌘D` | 向右分屏 |
| `⌘⇧D` | 向下分屏 |
| `⌘K` | 清屏 |
| `⌘F` | 在终端中查找 |
| `⌘⌥←/→` | 上一个/下一个标签页 |
| `Ctrl+1-9` | 打开预设 1-9 |

### 布局

| 快捷键 | 操作 |
|:---------|:-------|
| `⌘B` | 切换工作区侧边栏 |
| `⌘L` | 切换变更面板 |
| `⌘O` | 在外部应用中打开 |
| `⌘⇧C` | 复制路径 |

## 配置

在 `.superset/config.json` 中配置工作区的初始化与清理流程。详见[完整文档](https://docs.superset.sh/setup-teardown-scripts)。

```json
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}
```

| 选项 | 类型 | 说明 |
|:-------|:-----|:------------|
| `setup` | `string[]` | 创建工作区时执行的命令 |
| `teardown` | `string[]` | 删除工作区时执行的命令 |

### 示例初始化脚本

```bash
#!/bin/bash
# .superset/setup.sh

# Copy environment variables
cp ../.env .env

# Install dependencies
bun install

# Run any other setup tasks
echo "Workspace ready!"
```

脚本可访问以下环境变量：
- `SUPERSET_WORKSPACE_NAME` — 工作区名称
- `SUPERSET_ROOT_PATH` — 主仓库路径

## Mastra 依赖说明

本仓库直接引用已发布的上游 `mastracode` 和 `@mastra/*` 软件包。除非遇到特定于该仓库的阻塞性问题，否则请勿添加自定义 tarball 覆盖文件。

## 技术栈

<p>
  <a href="https://www.electronjs.org/"><img src="https://img.shields.io/badge/Electron-191970?logo=Electron&logoColor=white" alt="Electron" /></a>
  <a href="https://reactjs.org/"><img src="https://img.shields.io/badge/React-%2320232a.svg?logo=react&logoColor=%2361DAFB" alt="React" /></a>
  <a href="https://tailwindcss.com/"><img src="https://img.shields.io/badge/Tailwindcss-%2338B2AC.svg?logo=tailwind-css&logoColor=white" alt="TailwindCSS" /></a>
  <a href="https://bun.sh/"><img src="https://img.shields.io/badge/Bun-000000?logo=bun&logoColor=white" alt="Bun" /></a>
  <a href="https://turbo.build/"><img src="https://img.shields.io/badge/Turborepo-EF4444?logo=turborepo&logoColor=white" alt="Turborepo" /></a>
  <a href="https://vitejs.dev/"><img src="https://img.shields.io/badge/Vite-%23646CFF.svg?logo=vite&logoColor=white" alt="Vite" /></a>
  <a href="https://biomejs.dev/"><img src="https://img.shields.io/badge/Biome-339AF0?logo=biome&logoColor=white" alt="Biome" /></a>
  <a href="https://orm.drizzle.team/"><img src="https://img.shields.io/badge/Drizzle%20ORM-FFE873?logo=drizzle&logoColor=black" alt="Drizzle ORM" /></a>
  <a href="https://neon.tech/"><img src="https://img.shields.io/badge/Neon-00E9CA?logo=neon&logoColor=white" alt="Neon" /></a>
  <a href="https://trpc.io/"><img src="https://img.shields.io/badge/tRPC-2596BE?logo=trpc&logoColor=white" alt="tRPC" /></a>
</p>

## 默认隐私优先

- **源码公开** —— 完整源代码托管于 GitHub，采用 Elastic License 2.0 (ELv2) 协议。
- **连接显式可控** —— 由你自主选择需要连接的代理、服务提供商及集成工具。

## 贡献指南

我们欢迎任何形式的贡献！如果你有任何能让 Superset 变得更好的建议：

1. Fork 本仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 发起 Pull Request

你也可以[提交 Issue](https://github.com/superset-sh/superset/issues) 来报告 Bug 或提出功能需求。

详细贡献指南及行为准则请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

<a href="https://github.com/superset-sh/superset/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=superset-sh/superset" />
</a>

## 社区加入

加入 Superset 社区以获取帮助、分享反馈并与其他用户建立联系：

- **[Discord](https://discord.gg/cZeD9WYcV7)** — 与团队和社区成员交流
- **[Twitter](https://x.com/superset_sh)** — 关注最新动态与公告
- **[GitHub Issues](https://github.com/superset-sh/superset/issues)** — 报告 Bug 和请求功能
- **[GitHub Discussions](https://github.com/superset-sh/superset/discussions)** — 提问与分享想法

### 团队成员

[![Avi Twitter](https://img.shields.io/badge/Avi-@avimakesrobots-555?logo=x)](https://x.com/avimakesrobots)
[![Kiet Twitter](https://img.shields.io/badge/Kiet-@flyakiet-555?logo=x)](https://x.com/flyakiet)
[![Satya Twitter](https://img.shields.io/badge/Satya-@saddle__paddle-555?logo=x)](https://x.com/saddle_paddle)

## 开源协议

本项目采用 Elastic License 2.0 (ELv2) 协议分发。更多信息请参阅 [LICENSE.md](LICENSE.md)。