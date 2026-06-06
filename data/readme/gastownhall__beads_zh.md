# bd - Beads

**基于 [Dolt](https://github.com/dolthub/dolt) 构建的分布式图结构问题追踪器，专为 AI Agent（智能体）设计。**

**支持平台：** macOS、Linux、Windows、FreeBSD

[![License](https://img.shields.io/github/license/gastownhall/beads)](LICENSE)
[![Go Report Card](https://goreportcard.com/badge/github.com/steveyegge/beads)](https://goreportcard.com/report/github.com/steveyegge/beads)
[![Release](https://img.shields.io/github/v/release/gastownhall/beads)](https://github.com/gastownhall/beads/releases)
[![npm version](https://img.shields.io/npm/v/@beads/bd)](https://www.npmjs.com/package/@beads/bd)
[![PyPI](https://img.shields.io/pypi/v/beads-mcp)](https://pypi.org/project/beads-mcp/)

**文档：** https://gastownhall.github.io/beads/

Beads 为编码 Agent（智能体）提供持久化、结构化的记忆存储。它用依赖感知的图结构替代了杂乱的 Markdown 计划，使 Agent 能够处理长周期任务而不会丢失上下文。

## ⚡ Quick Start

```bash
# Install beads CLI (system-wide - don't clone this repo into your project)
curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh | bash

# Initialize in YOUR project
cd your-project
bd init

# Optional: refresh or install richer instructions for your agent
bd setup codex    # Codex CLI - installs skill, AGENTS.md guidance, and hooks
bd setup claude   # Claude Code - installs hooks/settings
bd setup factory  # Factory.ai Droid - creates/updates AGENTS.md
```

**注意：** Beads 是一款一次性安装、随处可用的 CLI 工具。你无需将此仓库克隆到你的项目中。

运行 ``bd init`` 默认会创建或更新 ``AGENTS.md``，以便 Agent 发现 beads 工作流；同时也会安装项目相关的 Claude/Codex 集成配置（除非传入 ``--skip-agents`` 或 ``--stealth`` 参数）。使用 ``bd setup --list`` 可查看支持的集成方式，包括 ``bd setup codex``、``bd setup factory``、``bd setup claude``、``bd setup mux``、``bd setup cursor`` 等。详见 [Agent and IDE setup](docs/SETUP.md)。

手动复制粘贴仅适用于不受 ``bd setup`` 支持的 Agent、无法重新运行 ``bd init``/``bd setup`` 的现有项目，或自定义指令文件。在这些情况下，请运行 ``bd onboard`` 并将输出的代码片段粘贴到你的 Agent 读取的配置文件中。

如果你的 Agent 未被 ``bd setup`` 覆盖，请在 ``AGENTS.md`` 中添加以下最小化配置：

```markdown
This project uses bd (beads) for issue tracking.

- Run `bd prime` for workflow context and command guidance.
- Use `bd ready`, `bd show <id>`, `bd update <id> --claim`, and `bd close <id>`.
- Use `bd remember "insight"` for persistent project memory; do not create MEMORY.md files.
- Do not use markdown TODO lists for task tracking.
```

## 🛠 Features

* **[Dolt](https://github.com/dolthub/dolt)-Powered：** 版本控制的 SQL 数据库，支持单元格级合并、原生分支功能，并通过 Dolt remotes 内置同步。
* **Agent-Optimized：** JSON 输出格式、依赖关系追踪以及自动就绪任务检测。
* **Zero Conflict：** 基于哈希的 ID（如 ``bd-a1b2``）可防止多 Agent/多分支工作流中的合并冲突。
* **Compaction：** 语义化的“记忆衰减”机制，自动总结已关闭的旧任务以节省上下文窗口。
* **Messaging：** 支持线程化（``--thread``）、临时生命周期及任务委派的消息 Issue 类型。
* **Graph Links：** 提供 ``relates_to``、``duplicates``、``supersedes`` 和 ``replies_to`` 等关系类型，构建知识图谱。

## 📖 Essential Commands

| Command | Action |
| --- | --- |
| `bd ready` | 列出无阻塞项的任务。 |
| `bd create "Title" -p 0` | 创建 P0 级任务。 |
| `bd update <id> --claim` | 原子化认领任务（同时设置负责人及状态为进行中）。 |
| `bd dep add <child> <parent>` | 链接任务（阻塞、关联、父子关系）。 |
| `bd show <id>` | 查看任务详情及操作审计日志。 |
| `bd prime` | 输出 Agent 工作流上下文及持久化记忆。 |
| `bd remember "insight"` | 存储项目记忆，供后续 ``bd prime`` 注入使用。 |

## 🔗 Hierarchy & Workflow

Beads 支持用于 Epic（史诗/大型需求）的层级 ID：

* `bd-a3f8` (Epic)
* `bd-a3f8.1` (Task)
* `bd-a3f8.1.1` (Sub-task)

**隐身模式：**运行 ``bd init --stealth`` 可在本地使用 Beads 而不将文件提交到主仓库。非常适合在共享项目中进行个人开发。详见下方的 [无 Git 用法](#-git-free-usage)。

**贡献者与维护者：**在使用开源项目时：

* **Contributors（Fork 仓库）：**运行 ``bd init --contributor`` 将规划类 Issue 路由到独立仓库（例如 ``~/.beads-planning``）。可将实验性工作与 PR 分离。
* **Maintainers（拥有写入权限）：**Beads 会通过 SSH URL 或带凭据的 HTTPS 自动检测维护者角色。仅在使用 GitHub HTTPS 但无凭据且你拥有写入权限时，才需要手动执行 ``git config beads.role maintainer``。

## 📦 Installation

```bash
brew install beads           # macOS / Linux (recommended)
npm install -g @beads/bd     # Node.js users
```

**其他安装方式：**[安装脚本](docs/INSTALLING.md#quick-install-script-all-platforms) | [go install](docs/INSTALLING.md#a-note-on-go-install-capability) | [源码编译](docs/INSTALLING.md#build-dependencies-contributors-only) | [Windows 11](docs/INSTALLING.md#windows-11) | [Arch AUR](docs/INSTALLING.md#linux)

**系统要求：**macOS、Linux、Windows 或 FreeBSD。完整安装指南请见 [docs/INSTALLING.md](docs/INSTALLING.md)。

### Security And Verification

在信任任何下载的二进制文件之前，请对照发布版中的 ``checksums.txt`` 验证其校验和。

安装脚本会在安装前自动验证发布版的校验和。对于手动安装，请在首次运行前自行完成此验证步骤。

在 macOS 上，``scripts/install.sh`` 默认会保留下载文件的签名。本地临时重新签名需显式启用：设置 ``BEADS_INSTALL_RESIGN_MACOS=1``。

Windows 杀毒软件误报处理指南及验证流程，请见 [docs/ANTIVIRUS.md](docs/ANTIVIRUS.md)。

## 💾 Storage Modes

Beads 使用 [Dolt](https://github.com/dolthub/dolt) 作为底层数据库。提供两种运行模式：

### Embedded Mode (default)

```bash
bd init
```

Dolt 以进程内方式运行，无需外部服务器。数据存储在 ``.beads/embeddeddolt/`` 目录中。仅支持单写入者（强制文件锁）。这是大多数用户推荐使用的模式。

当 Git 仓库配置了 ``origin`` 远程地址时，``bd init`` 会自动配置一个名为 ``origin`` 的 Dolt 远程端点。跨机器同步请使用 ``bd dolt push`` 和 ``bd dolt pull`` 操作 ``refs/dolt/data``；而 ``.beads/issues.jsonl`` 仅作为导出文件供查看或交换使用，并非唯一数据源或完整的数据库备份。

### Server Mode

```bash
bd init --server
```

连接外部 ``dolt sql-server``。数据存储在 ``.beads/dolt/`` 目录中。支持多并发写入者。可通过命令行参数或环境变量配置连接信息：

| Flag | Env Var | Default |
|------|---------|---------|
| `--server-host` | `BEADS_DOLT_SERVER_HOST` | `127.0.0.1` |
| `--server-port` | `BEADS_DOLT_SERVER_PORT` | `3307` |
| `--server-socket` | `BEADS_DOLT_SERVER_SOCKET` | (none; uses TCP) |
| `--server-user` | `BEADS_DOLT_SERVER_USER` | `root` |
| | `BEADS_DOLT_PASSWORD` | (none) |

**Unix 域套接字：**使用 ``--server-socket`` 可通过 Unix 套接字而非 TCP 进行连接。这能避免多项目并发时的端口冲突，在沙盒环境（如 Claude Code）中尤为实用，因为文件级访问控制比网络白名单更简单。Dolt 服务器需通过 ``dolt sql-server --socket <path>`` 启动。套接字模式下暂不支持自动启动。

### Backup & Migration

使用 ``bd backup`` 备份数据库并在不同模式间迁移：

```bash
# Set up a backup destination and push
bd backup init /path/to/backup
bd backup sync

# Restore into a new project (any mode)
bd init           # or bd init --server
bd backup restore --force /path/to/backup
```

完整迁移指南请见 [docs/DOLT.md](docs/DOLT.md#migrating-between-backends)。

``bd export`` 和 ``.beads/issues.jsonl`` 仅为 Issue 表的导出文件。它们适用于审查、迁移及互操作，但不会捕获 Dolt 分支、提交历史、工作集状态或非 Issue 表数据。如需可恢复的数据库备份，请使用 ``bd backup`` 或手动执行 Dolt 备份。

## 🌐 Community Tools

详见 [docs/COMMUNITY_TOOLS.md](docs/COMMUNITY_TOOLS.md)，获取精心整理的社区构建 UI、扩展及集成列表，涵盖终端界面、Web UI、编辑器插件和原生应用。

## 🚀 Git-Free Usage

Beads 可在无 Git 的环境下运行。Dolt 数据库作为存储后端，Git 集成（钩子、仓库发现、身份标识）为可选项。

```bash
# Initialize without git
export BEADS_DIR=/path/to/your/project/.beads
bd init --quiet --stealth

# All core commands work with zero git calls
bd create "Fix auth bug" -p 1 -t bug
bd ready --json
bd update bd-a1b2 --claim
bd prime
bd close bd-a1b2 "Fixed"
```

设置 ``BEADS_DIR`` 可指定 ``.beads/`` 数据库目录的位置，从而绕过 Git 仓库自动发现功能。``--stealth`` 会在配置中设置 `no-git-ops: true`，禁用所有 Git 钩子安装及 Git 操作。

该模式适用于以下场景：
- **非 Git VCS**（如 Sapling、Jujutsu、Piper）——无需 ``.git/`` 目录
- **单体仓库** ——将 ``BEADS_DIR`` 指向特定子目录即可
- **CI/CD** ——实现隔离的任务追踪，避免影响整个仓库
- **评估与测试** ——在 ``/tmp`` 等临时目录中快速创建实验性数据库

如需在无 Git 环境下使用守护进程模式，请运行 ``bd daemon start --local``（详见 [PR #433](https://github.com/gastownhall/beads/pull/433)）。

## 📝 Documentation

* [文档站点](https://gastownhall.github.io/beads/)（按版本归档）| [安装指南](docs/INSTALLING.md) | [同步概念](docs/SYNC_CONCEPTS.md) | [Agent 工作流](AGENT_INSTRUCTIONS.md) | [Copilot CLI 集成](docs/COPILOT_CLI_INTEGRATION.md) | [Copilot VS Code MCP](docs/COPILOT_INTEGRATION.md) | [技术文章](ARTICLES.md) | [受保护分支同步模式](docs/PROTECTED_BRANCHES.md) | [故障排除](docs/TROUBLESHOOTING.md) | [常见问题](docs/FAQ.md)
* [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/gastownhall/beads)