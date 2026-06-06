English | [한국어](README.ko.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Português](README.pt.md)

# oh-my-claudecode

[![npm version](https://img.shields.io/npm/v/oh-my-claude-sisyphus?color=cb3837)](https://www.npmjs.com/package/oh-my-claude-sisyphus)
[![npm downloads](https://img.shields.io/npm/dm/oh-my-claude-sisyphus?color=blue)](https://www.npmjs.com/package/oh-my-claude-sisyphus)
[![GitHub stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-claudecode?style=flat&color=yellow)](https://github.com/Yeachan-Heo/oh-my-claudecode/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Sponsor](https://img.shields.io/badge/Sponsor-❤️-red?style=flat&logo=github)](https://github.com/sponsors/Yeachan-Heo)
[![Discord](https://img.shields.io/discord/1452487457085063218?color=5865F2&logo=discord&logoColor=white&label=Discord)](https://discord.gg/PUwSMR9XNk)

> **对于 Codex 用户：** 请查看 [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) —— 为 OpenAI Codex CLI 打造的同等编排体验。

**为 Claude Code 提供多 Agent 编排。零学习成本。**

_无需学习 Claude Code，直接使用 OMC。_

[快速开始](#quick-start) • [文档](https://yeachan-heo.github.io/oh-my-claudecode-website) • [CLI 参考](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#cli-reference) • [工作流](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#workflows) • [迁移指南](docs/MIGRATION.md) • [Discord 社区](https://discord.gg/PUwSMR9XNk)

---

## 核心维护者

| Role | Name | GitHub |
| --- | --- | --- |
| Creator & Lead | Yeachan Heo | [@Yeachan-Heo](https://github.com/Yeachan-Heo) |

## 大使 (Ambassadors)

| Name | GitHub |
| --- | --- |
| Sigrid Jin | [@sigridjineth](https://github.com/sigridjineth) |

## 文档专家 (Document Specialists)

| Name | GitHub |
| --- | --- |
| devswha | [@devswha](https://github.com/devswha) |

## 顶级协作者 (Top Collaborators)

| Name | GitHub | Commits |
| --- | --- | --- |
| JunghwanNA | [@shaun0927](https://github.com/shaun0927) | 65 |
| riftzen-bit | [@riftzen-bit](https://github.com/riftzen-bit) | 52 |
| Seunggwan Song | [@Nathan-Song](https://github.com/Nathan-Song) | 20 |
| BLUE | [@blue-int](https://github.com/blue-int) | 20 |
| Junho Yeo | [@junhoyeo](https://github.com/junhoyeo) | 15 |

## Quick Start（快速开始）

**步骤 1：安装**

应用市场/插件安装（推荐大多数 Claude Code 用户使用）。
这些是 Claude Code 的斜杠命令（slash commands），请**逐条输入**（一次性粘贴两行会失败）：

```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
```

接着执行：

```bash
/plugin install oh-my-claudecode
```

如果你更倾向于使用 npm CLI 或运行时路径，而非应用市场流程：

```bash
npm i -g oh-my-claude-sisyphus@latest
```

> **已知的 npm 警告：** 在使用 CLI 安装时，npm 可能会打印 `deprecated prebuild-install@7.1.3`。
> 该警告目前来源于上游依赖 `better-sqlite3` 的原生插件（`better-sqlite3 -> prebuild-install`）；`prebuild-install@7.1.3` 仍是当前最新发布的版本，因此仓库端暂时无法通过安全的依赖升级或覆盖来消除此警告。该问题已在 [#2913](https://github.com/Yeachan-Heo/oh-my-claudecode/issues/2913) 中记录，且该警告本身并不代表 OMC CLI 安装失败。

**步骤 2：配置**

```bash
# 在 Claude Code / OMC 会话内执行
/setup
/omc-setup

# 从终端直接执行
omc setup
```

如果你通过 `omc --plugin-dir <path>` 或 `claude --plugin-dir <path>` 运行 OMC，请在 `omc setup` 中添加 `--plugin-dir-mode`（或在运行前导出环境变量 `OMC_PLUGIN_ROOT`），以防止安装程序重复创建插件已在运行时提供的技能/Agent。完整的决策矩阵及所有可用参数详见 [REFERENCE.md 中的插件目录参数说明](./docs/REFERENCE.md#plugin-directory-flags)。

**步骤 3：开始构建**

```bash
# 在 Claude Code / OMC 会话内执行
/autopilot "build a REST API for managing tasks"

# 会话内的自然语言快捷方式
autopilot: build a REST API for managing tasks
```

到此为止。其余一切自动完成。

### CLI 命令 vs 会话内技能（In-Session Skills）

OMC 提供两种不同的交互入口：

- **终端 CLI 命令**：安装 npm/运行时路径后，在 Shell 中运行 `omc ...`（或从本地代码检出目录运行）。
- **会话内技能**：在安装插件/配置流程后，在 Claude Code 会话中输入 `/...` 执行。

| Feature | Terminal CLI | In-session skill | Notes |
| --- | --- | --- | --- |
| Setup | `omc setup` | `/setup` or `/omc-setup` | Both are real entrypoints. `/setup` is the easiest plugin-first path. |
| Ask providers | `omc ask codex "review this patch"` | `/ask codex "review this patch"` | Both route through the same advisor flow. |
| Team orchestration | `omc team 2:codex "review auth flow"` | `/team 3:executor "fix all TypeScript errors"` | Both exist, but they are different runtimes: `omc team` launches tmux CLI workers; `/team` runs the in-session native team workflow. |
| Autopilot / Ralph / Ultrawork / Deep Interview | — | `/autopilot ...`, `/ralph ...`, `/ultrawork ...`, `/deep-interview ...` | These are in-session skills. There is no `omc autopilot` / `omc ralph` / `omc ultrawork` CLI subcommand in this repo. |
| Autoresearch | `omc autoresearch` (**hard-deprecated shim**) | `/deep-interview --autoresearch ...` + `/oh-my-claudecode:autoresearch` | Setup stays in deep-interview; execution now belongs to the stateful skill. |

### 不确定从哪里开始？

如果你对产品需求不明确、只有模糊的想法，或希望亲自把控设计细节：

```
/deep-interview "I want to build a task management app"
```

深度访谈（Deep Interview）会在编写任何代码前使用苏格拉底式提问帮你理清思路。它会暴露隐藏假设，并在多个加权维度上评估清晰度，确保你在执行开始前完全清楚自己要构建什么。

## Team 模式（推荐）

从 **v4.1.7** 开始，**Team** 成为 OMC 中标准的编排入口。旧的 `swarm` 关键字/技能已被移除；请直接使用 `team`。

```bash
/team 3:executor "fix all TypeScript errors"
```

当你想要 Claude Code 的会话内原生 Team 工作流时，使用 `/team ...`。当你需要终端启动的 tmux CLI 工作进程（`claude` / `codex` / `gemini` 分屏）时，使用 `omc team ...`。

Team 以分阶段流水线形式运行：

`team-plan → team-prd → team-exec → team-verify → team-fix (循环)`

在 `~/.claude/settings.json` 中启用 Claude Code 原生团队功能：

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

> 如果 Team 功能被禁用，OMC 会发出警告并尽可能回退到非 Team 执行模式。

### tmux CLI 工作进程 — Codex & Gemini (v4.4.0+)

**v4.4.0 移除了 Codex/Gemini MCP 服务器**（`x`, `g` 提供者）。请使用基于 CLI 的 Team 运行时（`omc team ...`）来启动真实的 tmux 工作进程分屏：

```bash
omc team 2:codex "review auth module for security issues"
omc team 2:gemini "redesign UI components for accessibility"
omc team 1:claude "implement the payment flow"
omc team status auth-review
omc team shutdown auth-review
```

`/omc-teams` 仍保留作为遗留兼容技能，现已路由至 `omc team ...`。

若要在单条命令中混合使用 Codex + Gemini，请使用 **`/ccg`** 技能（通过 `/ask codex` + `/ask gemini` 路由，随后由 Claude 综合研判）：

```bash
/ccg Review this PR — architecture (Codex) and UI components (Gemini)
```

| Surface                   | Workers            | Best For                                     |
| ------------------------- | ------------------ | -------------------------------------------- |
| `omc team N:codex "..."`  | N Codex CLI panes  | Code review, security analysis, architecture |
| `omc team N:gemini "..."` | N Gemini CLI panes | UI/UX design, docs, large-context tasks      |
| `omc team N:claude "..."` | N Claude CLI panes | General tasks via Claude CLI in tmux         |
| `/ccg`                    | /ask codex + /ask gemini | Tri-model advisor synthesis           |

工作进程按需启动，任务完成后自动销毁——不会产生空闲资源占用。需要已安装 `codex` / `gemini` CLI 且处于活跃的 tmux 会话中。

原生 Team 工作树（worktrees）功能正在通过可选配置逐步开放。详见 [Native Team Worktree Mode](docs/TEAM-WORKTREE-MODE.md) 了解工作区契约、标准状态根规则、脏工作树保留策略及验证清单。

> **注意：包命名规范** —— 项目品牌名为 **oh-my-claudecode**（仓库、插件、命令），但 npm 发布的包名为 [`oh-my-claude-sisyphus`](https://www.npmjs.com/package/oh-my-claude-sisyphus)。如果你通过 npm/bun 安装或升级 CLI 工具，请使用 `npm i -g oh-my-claude-sisyphus@latest`。

### 更新（Updating）

如果你通过 npm 安装了 OMC，请使用发布的包名进行升级：

```bash
npm i -g oh-my-claude-sisyphus@latest
```

> **包命名说明：** 仓库、插件和命令的品牌名为 **oh-my-claudecode**，但已发布的 npm 包名仍为 `oh-my-claude-sisyphus`。

如果你通过 Claude Code 应用市场/插件流程安装了 OMC，请使用以下方式更新：

```bash
# 1. 更新应用市场克隆版本
/plugin marketplace update omc

# 2. 重新运行配置以刷新设置
/setup
```

如果你是使用本地代码检出或 git worktree 进行开发，请先更新检出目录，然后从该工作树中重新运行配置，以确保活跃运行时与你正在测试的代码保持一致。

> **注意：** 如果未启用应用市场自动更新，你必须在运行 `/setup` 前手动执行 `/plugin marketplace update omc` 以同步最新版本。

如果在更新后遇到问题，请清除旧的插件缓存：

```bash
/omc-doctor
```

<h1 align="center">你的 Claude 现已满血强化。</h1>

<p align="center">
  <img src="assets/omc-character.jpg" alt="oh-my-claudecode" width="400" />
</p>

---

## Why oh-my-claudecode?（为什么选择 OMC？）

- **零配置开箱即用** - 内置智能默认值，无需繁琐设置即可运行
- **Team-first 编排架构** - Team 是标准的多 Agent 协作入口
- **自然语言交互** - 无需记忆命令，直接描述你的需求即可
- **自动并行化** - 复杂任务自动分发至专业 Agent 处理
- **持久执行机制** - 直到任务被验证完成前绝不会放弃
- **成本优化** - 智能模型路由可节省 30%-50% 的 Token 消耗
- **经验学习** - 自动提取并复用已验证的问题解决模式
- **实时可视化** - HUD（状态栏）清晰展示底层执行动态

---

## Features（功能特性）

### Orchestration Modes（编排模式）

针对不同使用场景提供多种策略——从 Team 驱动编排到 Token 高效的代码重构。[了解更多 →](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#execution-modes)

| Mode                    | What it is                                                                              | Use For                                                |
| ----------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Team (recommended)**  | Canonical staged pipeline (`team-plan → team-prd → team-exec → team-verify → team-fix`) | Coordinated Claude agents on a shared task list        |
| **omc team (CLI)**      | tmux CLI workers — real `claude`/`codex`/`gemini` processes in split-panes              | Codex/Gemini CLI tasks; on-demand spawn, die when done |
| **ccg**                 | Tri-model advisors via `/ask codex` + `/ask gemini`, Claude synthesizes                   | Mixed backend+UI work needing both Codex and Gemini    |
| **Autopilot**           | Autonomous execution (single lead agent)                                                | End-to-end feature work with minimal ceremony          |
| **Ultrawork**           | Maximum parallelism (non-team)                                                          | Burst parallel fixes/refactors where Team isn't needed |
| **Ralph**               | Persistent mode with verify/fix loops                                                   | Tasks that must complete fully (no silent partials)    |
| **Pipeline**            | Sequential, staged processing                                                           | Multi-step transformations with strict ordering        |
| **Ultrapilot (legacy)** | Deprecated compatibility mode (autopilot pipeline alias)                                | Existing workflows and older docs                      |

### Intelligent Orchestration（智能编排）

- **19 个专业 Agent**（含分级变体），覆盖架构、研究、设计、测试与数据科学领域
- **智能模型路由** - 简单任务使用 Haiku，复杂推理调用 Opus
- **自动委派机制** - 每次都能精准匹配最合适的 Agent 处理对应工作

### Developer Experience（开发者体验）

- **魔法关键字** - `ralph`, `ulw`, `ralplan`；Team 通过 `/team` 保持显式控制
- **HUD 状态栏** - 实时显示编排指标与执行进度
  - 如果你直接通过 `claude --plugin-dir <path>`（绕过 `omc` 包装器）启动 Claude Code，请在 Shell 中导出 `OMC_PLUGIN_ROOT=<path>`，以确保 HUD 资源包能正确解析到插件加载器所在的检出目录。详见 [REFERENCE.md 中的插件目录参数说明](./docs/REFERENCE.md#plugin-directory-flags)。
- **技能学习（Skill Learning）** - 从会话中提取可复用模式
- **分析与成本追踪** - 全面了解所有会话的 Token 使用情况

### Contributing（贡献指南）

想要为 OMC 贡献力量？请查阅 [CONTRIBUTING.md](./CONTRIBUTING.md)，其中包含完整的开发者指南，涵盖如何 Fork、配置本地开发环境、链接为活跃插件、运行测试及提交 PR 等步骤。

### Custom Skills（自定义技能）

一次学习，永久复用。OMC 会将宝贵的调试经验提取为可移植的技能文件，并在相关场景下自动注入上下文。

| | Project Scope | User Scope |
|---|---|---|
| **Path** | `.omc/skills/` | `~/.omc/skills/` |
| **Shared with** | Team (commit the skill file to keep it across worktrees) | All your projects |
| **Priority** | Higher (overrides user) | Lower (fallback) |

```yaml
# .omc/skills/fix-proxy-crash.md
---
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
---
Wrap handler at server.py:42 in try/except ClientDisconnectedError...
```

**管理技能：** `/skill list | add | remove | edit | search`
**Skillify（技能化）：** `/skillify` 提取可复用模式并设置严格的质量门禁
**自动注入（Auto-inject）：** 匹配的技能会自动加载至上下文——无需手动调用

项目级技能存储在 `.omc/skills/` 中，建议通过 Git 提交以便在多个工作树间共享。如果你在已链接的 git worktree 内创建它们但未提交，当该工作树被移除时这些文件也会消失。

[完整功能列表 →](docs/REFERENCE.md)

---

## In-session shortcuts（会话内快捷方式）

以下快捷方式**仅在 Claude Code / OMC 会话内部运行**，并非终端 CLI 命令。如需使用 Shell 命令，请参见上文提供的 `omc ...` 形式。Team 模式需显式调用：在会话中使用 `/team ...`，或在 Shell 中使用 `omc team ...`，不要依赖裸关键字触发器。

| In-session form        | Kind                  | Effect                              | Example                                        |
| ---------------------- | --------------------- | ----------------------------------- | ---------------------------------------------- |
| `/team`                | Slash skill           | Canonical Team orchestration        | `/team 3:executor "fix all TypeScript errors"` |
| `/ccg`                 | Slash skill           | `/ask codex` + `/ask gemini` synthesis | `/ccg review this PR`                       |
| `/autopilot` / `autopilot` | Skill / prompt trigger | Full autonomous execution       | `/autopilot "build a todo app"`                |
| `/ralph` / `ralph`     | Skill / prompt trigger | Persistence mode                   | `/ralph "refactor auth"`                       |
| `/ultrawork` / `ulw`   | Skill / prompt trigger | Maximum parallelism                | `/ultrawork "fix all errors"`                  |
| `/ralplan` / `ralplan` | Skill / prompt trigger | Iterative planning consensus       | `/ralplan "plan this feature"`                 |
| `/deep-interview`      | Slash skill           | Socratic requirements clarification | `/deep-interview "vague idea"`                 |
| `deepsearch`           | Prompt trigger        | Codebase-focused search routing     | `deepsearch for auth middleware`               |
| `ultrathink`           | Prompt trigger        | Deep reasoning mode                 | `ultrathink about this architecture`           |
| `cancelomc`, `stopomc` | Prompt trigger        | Stop active OMC modes               | `stopomc`                                      |

**注意事项：**

- **ralph 包含 ultrawork**：激活 ralph 模式时，会自动启用 ultrawork 的并行执行机制。
- `swarm` 兼容别名已移除；请将现有提示词迁移至 `/team` 语法。
- `plan this` / `plan the` 关键字触发器已移除；请使用 `ralplan` 或显式的 `/oh-my-claudecode:plan`。

## Utilities（实用工具）

### Provider Advisor (`omc ask` / `/ask`)

运行本地提供者 CLI，并在 `.omc/artifacts/ask/` 下保存 Markdown 格式的执行产物。

```bash
# Terminal CLI
omc ask claude "review this migration plan"
omc ask codex --prompt "identify architecture risks"
omc ask gemini --prompt "propose UI polish ideas"
omc ask claude --agent-prompt executor --prompt "draft implementation steps"

# Inside a Claude Code / OMC session
/ask claude "review this migration plan"
/ask codex "identify architecture risks"
```

标准环境变量：

- `OMC_ASK_ADVISOR_SCRIPT`
- `OMC_ASK_ORIGINAL_TASK`

阶段 1 别名 `OMX_ASK_ADVISOR_SCRIPT` 和 `OMX_ASK_ORIGINAL_TASK` 仍被接受，但会输出弃用警告。

### Autoresearch（状态化技能）

`omc autoresearch` 现已标记为 **硬弃用垫片**。权威工作流如下：

```bash
/deep-interview --autoresearch improve startup performance
/oh-my-claudecode:autoresearch
```

- `deep-interview --autoresearch` 负责生成/配置任务目标与评估器
- `autoresearch` 执行有界、单任务的闭环状态循环
- 每次迭代均记录评估 JSON 及 Markdown 决策日志
- 未通过的迭代会自动继续重试
- 严格停止条件由显式的最大运行时间上限控制

### Rate Limit Wait（速率限制等待）

在 API 速率限制重置后自动恢复 Claude Code 会话。

```bash
omc wait          # 检查状态并获取操作指引
omc wait --start  # 启用自动恢复守护进程
omc wait --stop   # 禁用守护进程
```

**依赖：** tmux（用于会话检测）

### Monitoring & Observability（监控与可观测性）

使用 HUD 进行实时可观测，并通过当前会话/回放产物进行事后检查：

- HUD 预设配置：执行 `/oh-my-claudecode:hud setup`，然后使用支持的前置配置如 `"omcHud": { "preset": "focused" }`
- 会话摘要文件：`.omc/sessions/*.json`
- 回放日志：`.omc/state/agent-replay-*.jsonl`
- 实时 HUD 渲染：运行 `omc hud`

### Notification Tags（通知标签 - Telegram/Discord/Slack）

你可以配置在停止回调发送会话摘要时，@提及哪些用户。

```bash
# Set/replace tag list
omc config-stop-callback telegram --enable --token <bot_token> --chat <chat_id> --tag-list "@alice,bob"
omc config-stop-callback discord --enable --webhook <url> --tag-list "@here,123456789012345678,role:987654321098765432"
omc config-stop-callback slack --enable --webhook <url> --tag-list "<!here>,<@U1234567890>"

# Incremental updates
omc config-stop-callback telegram --add-tag charlie
omc config-stop-callback discord --remove-tag @here
omc config-stop-callback discord --clear-tags
```

标签行为说明：

- Telegram: `alice` 会自动转换为 `@alice`
- Discord: 支持 `@here`, `@everyone`, 数字用户 ID, 以及 `role:<id>`
- Slack: 支持 `<@MEMBER_ID>`, `<!channel>`, `<!here>`, `<!everyone>`, `<!subteam^GROUP_ID>`
- `file` 回调类型忽略标签选项

### OpenClaw Integration（OpenClaw 集成）

将 Claude Code 会话事件转发至 [OpenClaw](https://openclaw.ai/) 网关，以便通过你的 OpenClaw Agent 实现自动化响应与工作流。

**快速配置（推荐）：**

```bash
/oh-my-claudecode:configure-notifications
# → 当提示时输入 "openclaw" → 选择 "OpenClaw Gateway"
```

**手动配置：** 创建 `~/.claude/omc_config.openclaw.json`：

```json
{
  "enabled": true,
  "gateways": {
    "my-gateway": {
      "url": "https://your-gateway.example.com/wake",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" },
      "method": "POST",
      "timeout": 10000
    }
  },
  "hooks": {
    "session-start": { "gateway": "my-gateway", "instruction": "Session started for {{projectName}}", "enabled": true },
    "stop":          { "gateway": "my-gateway", "instruction": "Session stopping for {{projectName}}", "enabled": true }
  }
}
```

**环境变量：**

| Variable | Description |
|----------|-------------|
| `OMC_OPENCLAW=1` | Enable OpenClaw |
| `OMC_OPENCLAW_DEBUG=1` | Enable debug logging |
| `OMC_OPENCLAW_CONFIG=/path/to/config.json` | Override config file path |

**支持的 Hook 事件（bridge.ts 中激活 6 个）：**

| Event | Trigger | Key template variables |
|-------|---------|----------------------|
| `session-start` | Session begins | `{{sessionId}}`, `{{projectName}}`, `{{projectPath}}` |
| `stop` | Claude response completes | `{{sessionId}}`, `{{projectName}}` |
| `keyword-detector` | Every prompt submission | `{{prompt}}`, `{{sessionId}}` |
| `ask-user-question` | Claude requests user input | `{{question}}`, `{{sessionId}}` |
| `pre-tool-use` | Before tool invocation (high frequency) | `{{toolName}}`, `{{sessionId}}` |
| `post-tool-use` | After tool invocation (high frequency) | `{{toolName}}`, `{{sessionId}}` |

**回复通道环境变量：**

| Variable | Description |
|----------|-------------|
| `OPENCLAW_REPLY_CHANNEL` | Reply channel (e.g. `discord`) |
| `OPENCLAW_REPLY_TARGET` | Channel ID |
| `OPENCLAW_REPLY_THREAD` | Thread ID |

参考网关实现请查看 `scripts/openclaw-gateway-demo.mjs`，该示例展示了如何通过 ClawdBot 将 OpenClaw 负载中继至 Discord。

---

## Documentation（文档）

- **[完整功能参考](docs/REFERENCE.md)** - 全部特性详细文档
- **[CLI 命令参考](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#cli-reference)** - 所有 `omc` 命令、参数与工具说明
- **[通知配置指南](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#notifications)** - Discord, Telegram, Slack 及 Webhook 设置教程
- **[推荐工作流](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#workflows)** - 经过实战检验的技能链，覆盖常见开发任务
- **[更新日志](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#release-notes)** - 各版本新增功能与修复记录
- **[官方网站](https://yeachan-heo.github.io/oh-my-claudecode-website)** - 交互式指南与示例演示
- **[迁移指南](docs/MIGRATION.md)** - 从 v2.x 升级至最新版本的操作指引
- **[架构说明](docs/ARCHITECTURE.md)** - 底层运行机制详解
- **[性能监控](docs/PERFORMANCE-MONITORING.md)** - Agent 追踪、调试与优化方案
- **[安全指南](SECURITY.md)** - 企业级部署与安全加固建议

---

## Requirements（环境要求）

- [Claude Code](https://docs.anthropic.com/claude-code) CLI
- Claude Max/Pro 订阅 **或** Anthropic API Key

### Platform & tmux（平台与终端复用器）

OMC 的 `omc team` 及速率限制检测等功能依赖 **tmux**：

| Platform       | tmux provider                                            | Install                |
| -------------- | -------------------------------------------------------- | ---------------------- |
| macOS          | [tmux](https://github.com/tmux/tmux)                    | `brew install tmux`    |
| Ubuntu/Debian  | tmux                                                     | `sudo apt install tmux`|
| Fedora         | tmux                                                     | `sudo dnf install tmux`|
| Arch           | tmux                                                     | `sudo pacman -S tmux`  |
| Windows        | [psmux](https://github.com/marlocarlo/psmux) (native)   | `winget install psmux` |
| Windows (WSL2) | tmux (inside WSL)                                        | `sudo apt install tmux`|

> **Windows 用户：** [psmux](https://github.com/marlocarlo/psmux) 提供原生 Windows 版 `tmux` 二进制文件，兼容 76 个 tmux 命令。无需依赖 WSL。

### Optional: Multi-AI Orchestration（可选：多 AI 编排）

OMC 可选择性地编排外部 AI 提供商以进行交叉验证与设计一致性检查。**这些并非必需**——OMC 在完全无额外配置的情况下即可独立运行。

| Provider                                                  | Install                             | What it enables                                  |
| --------------------------------------------------------- | ----------------------------------- | ------------------------------------------------ |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `npm install -g @google/gemini-cli` | Design review, UI consistency (1M token context) |
| [Codex CLI](https://github.com/openai/codex)              | `npm install -g @openai/codex`      | Architecture validation, code review cross-check |

**成本说明：** 3 份 Pro 订阅（Claude + Gemini + ChatGPT）即可覆盖全部功能，月费约 $60。

---

## License（许可证）

MIT

---

<div align="center">

**灵感来源：** [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) • [claude-hud](https://github.com/ryanjoachim/claude-hud) • [Superpowers](https://github.com/obra/superpowers) • [everything-claude-code](https://github.com/affaan-m/everything-claude-code) • [Ouroboros](https://github.com/Q00/ouroboros)

**零学习成本。极致效能。**

</div>

<!-- OMC:FEATURED-CONTRIBUTORS:START -->
## Featured by OmC Contributors（OmC 贡献者推荐）

来自 OMC 历史贡献者的顶级个人非 Fork、未归档仓库（GitHub 星标数 100+）。

- [@Yeachan-Heo](https://github.com/Yeachan-Heo) — [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) (⭐ 32k)
- [@junhoyeo](https://github.com/junhoyeo) — [tokscale](https://github.com/junhoyeo/tokscale) (⭐ 2.3k)
- [@psmux](https://github.com/psmux) — [psmux](https://github.com/psmux/psmux) (⭐ 1.6k)
- [@BowTiedSwan](https://github.com/BowTiedSwan) — [buildflow](https://github.com/BowTiedSwan/buildflow) (⭐ 291)
- [@alohays](https://github.com/alohays) — [awesome-visual-representation-learning-with-transformers](https://github.com/alohays/awesome-visual-representation-learning-with-transformers) (⭐ 268)
- [@jcwleo](https://github.com/jcwleo) — [random-network-distillation-pytorch](https://github.com/jcwleo/random-network-distillation-pytorch) (⭐ 261)
- [@emgeee](https://github.com/emgeee) — [mean-tutorial](https://github.com/emgeee/mean-tutorial) (⭐ 200)
- [@shaun0927](https://github.com/shaun0927) — [openchrome](https://github.com/shaun0927/openchrome) (⭐ 186)
- [@MeroZemory](https://github.com/MeroZemory) — [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp) (⭐ 182)
- [@anduinnn](https://github.com/anduinnn) — [HiFiNi-Auto-CheckIn](https://github.com/anduinnn/HiFiNi-Auto-CheckIn) (⭐ 171)
- [@HaD0Yun](https://github.com/HaD0Yun) — [Gopeak-godot-mcp](https://github.com/HaD0Yun/Gopeak-godot-mcp) (⭐ 148)
- [@Znuff](https://github.com/Znuff) — [consolas-powerline](https://github.com/Znuff/consolas-powerline) (⭐ 146)

<!-- OMC:FEATURED-CONTRIBUTORS:END -->

## Star History（星标历史）

[![Star History Chart](https://api.star-history.com/svg?repos=Yeachan-Heo/oh-my-claudecode&type=date&legend=top-left)](https://www.star-history.com/#Yeachan-Heo/oh-my-claudecode&type=date&legend=top-left)

## 💖 Support This Project（支持本项目）

如果 Oh-My-ClaudeCode 提升了你的开发工作流，请考虑成为赞助者：

[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor-❤️-red?style=for-the-badge&logo=github)](https://github.com/sponsors/Yeachan-Heo)

### Why sponsor?（为什么选择赞助？）

- 保持项目持续活跃开发
- 获得赞助者优先技术支持
- 参与产品路线图与功能规划决策
- 助力维护免费且开源的开发者工具

### Other ways to help（其他支持方式）

- ⭐ Star 本仓库
- 🐛 提交 Bug 报告
- 💡 提出新功能建议
- 📝 贡献代码