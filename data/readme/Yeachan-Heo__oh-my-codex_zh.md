# oh-my-codex (OMX)

<p align="center">
  <img src="https://yeachan-heo.github.io/oh-my-codex-website/omx-character-nobg.png" alt="oh-my-codex character" width="280">
  <br>
  <em>让工作起步更强劲，随后在任务扩展时由 OMX 提供更优的提示词、工作流与运行时辅助。</em>
</p>

[![npm version](https://img.shields.io/npm/v/oh-my-codex)](https://www.npmjs.com/package/oh-my-codex)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/node-%3E%3D20-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/discord/1452487457085063218?color=5865F2&logo=discord&logoColor=white&label=Discord)](https://discord.gg/sj4exxQ9v)

**官网：** https://yeachan-heo.github.io/oh-my-codex-website/

**文档：** [快速入门](./docs/getting-started.html) · [智能体 (Agents)](./docs/agents.html) · [技能 (Skills)](./docs/skills.html) · [集成 (Integrations)](./docs/integrations.html) · [演示](./DEMO.md) · [OpenClaw 指南](./docs/openclaw-integration.md)

**社区：** [Discord](https://discord.gg/sj4exxQ9v) — oh-my-codex 及相关工具的共享 OMX/community 服务器。

## 官方项目与包

OMX 的官方/原始项目即本仓库 [`Yeachan-Heo/oh-my-codex`](https://github.com/Yeachan-Heo/oh-my-codex)，该项目的官方 npm 包为 [`oh-my-codex`](https://www.npmjs.com/package/oh-my-codex)。安装本项目请使用 `npm install -g oh-my-codex`（或如下方所示与 Codex CLI 配合使用）。

除非本 README 或文档明确说明，否则使用“OMX v2”等名称的第三方项目或分支并非此仓库的官方延续、替代版本或发布线。如有疑虑，请以本仓库和 `oh-my-codex` 包作为官方安装目标为准。

OMX 是 [OpenAI Codex CLI](https://github.com/openai/codex) 的工作流层（workflow layer）。

<table>
<tr>
<td><strong>🚨 注意 — 推荐默认配置仅适用于：macOS 或 Linux + Codex CLI。</strong><br><br><strong>OMX 主要为此路径设计并持续优化。</strong><br><strong>原生 Windows 和 Codex App 并非默认体验，可能出错或行为不一致，且目前获得的支持较少。</strong></td>
</tr>
</table>

它保留 Codex 作为执行引擎，让你更轻松地：
- 默认启动更强的 Codex 会话
- 运行从澄清到完成的统一工作流
- 使用 `$deep-interview`、`$ralplan` 和 `$ultragoal` 调用标准默认工作流
- 将项目指引、计划、日志和状态保存在 `.omx/` 中

## 核心维护者

| 角色 | 姓名 | GitHub |
| --- | --- | --- |
| 创建者与负责人 | Yeachan Heo | [@Yeachan-Heo](https://github.com/Yeachan-Heo) |
| 维护者 | Doyun Ha | [@HaD0Yun](https://github.com/HaD0Yun) |
| 维护者 | Valeriy Pavlovich | [@iqdoctor](https://github.com/iqdoctor) |

## 大使

| 姓名 | GitHub |
| --- | --- |
| Sigrid Jin | [@sigridjineth](https://github.com/sigridjineth) |

## 主要协作者

| 姓名 | GitHub |
| --- | --- |
| Doyun Ha | [@HaD0Yun](https://github.com/HaD0Yun) |
| Junho Yeo | [@junhoyeo](https://github.com/junhoyeo) |
| JiHongKim98 | [@JiHongKim98](https://github.com/JiHongKim98) |
| Lor | [@gobylor](https://github.com/gobylor) |
| HyunjunJeon | [@HyunjunJeon](https://github.com/HyunjunJeon) |

## 推荐的默认流程

如果你希望获得默认的 OMX 体验，请从这里开始：

选择一种安装路径。如果已安装 Codex CLI（Homebrew、npm 或其他支持的方式）：

```bash
codex --version
npm install -g oh-my-codex
omx setup
# 从你希望 Codex 编辑的 git 项目目录执行；选择一个与任务相关的名称
omx --worktree=feat/task --madmax --high
```

如果你尚未安装 Codex CLI，并希望由 npm 管理它：

```bash
npm install -g @openai/codex
npm install -g oh-my-codex
omx setup
```

不要对已有的 Homebrew 管理的 `codex` 二进制文件（如 `/opt/homebrew/bin/codex`）执行合并的 `npm install -g @openai/codex oh-my-codex`；当 `@openai/codex` 尝试创建同名二进制文件时，npm 可能会因 `EEXIST` 报错。OMX 只需在 `PATH` 中有一个可运行且已认证的 `codex` 命令即可，并不要求必须通过 npm 安装 Codex。

在真实的 `oh-my-codex` 版本更新时，全局 npm 安装现在会打印明确的提醒，而不是自动启动 `omx setup`。当你准备好后，手动运行 `omx setup`，或使用 `omx update` 检查 npm 然后执行相同的设置刷新流程。

OMX 还会以限流频率在启动时检查 npm 更新，并在当前会话退出前提示你是否安排更新。设置 `OMX_AUTO_UPDATE=0` 可禁用启动时的检查，或设置 `OMX_AUTO_UPDATE=defer` 可在不提示的情况下安排延迟更新。

**Codex 插件安装说明：** 本仓库还附带了一个官方的 Codex 插件布局 `plugins/oh-my-codex`，其市场元数据位于 `.agents/plugins/marketplace.json`。该插件打包了镜像的技能界面以及用于官方 Codex 生命周期钩子、可选的 MCP 兼容服务器和应用的插件作用域辅助元数据。它仍然**不是** `npm install -g oh-my-codex` 加上 `omx setup` 的替代品：插件作用域的钩子会启动已安装的 `omx` CLI，旧版设置模式安装原生智能体和提示词，而插件设置模式依赖插件发现机制来获取内置技能，同时归档/移除旧的 OMX 管理的提示词和原生智能体 TOML 文件，以防止陈旧的角色文件覆盖插件行为。

然后在 Codex 中正常进行工作：

```text
$deep-interview "clarify the authentication change"
$ralplan "approve the auth plan and review tradeoffs"
$prometheus-strict "stress-test the plan before durable execution"
$ultragoal "turn the approved plan into durable Codex goals"
```

这是主要路径。在将运行时视为就绪之前，请先运行下方的快速冒烟测试：`omx doctor` 会验证安装结构，而 `omx exec` 能证明当前环境下的活跃 Codex 运行时确实能够认证并完成模型调用。让工作起步更强劲，必要时先澄清范围，批准计划，对高风险任务可选地使用 `$prometheus-strict` 进行访谈驱动的强化，然后使用 `$ultragoal` 作为默认的持久化完成包装器。仅当特定的 Ultragoal 故事需要协调的并行工作时，才在该执行路径中使用 `$team`；当你有意想要单一所有者的完成循环而非持久的多目标运行时，请使用 `$ralph`。

## OMX 的适用场景

如果你已经喜欢 Codex 并希望围绕它获得更好的日常运行时体验，请使用 OMX：
- 基于 `$deep-interview` -> `$ralplan` -> `$ultragoal` 构建的标准工作流；当计划需要在执行前进行更严格的访谈/批判/综合时，可使用 `$prometheus-strict` 以及可选的 `.omx/plans/prometheus-strict/` 产物
- 研究边界：使用 `$best-practice-research` 获取普通的预规划官方/上游证据，使用 `$autoresearch` 获取受验证器门禁限制的研究产物，使用 `$autoresearch-goal` 进行目标模式的研究任务，并将任何研究发现输入到 `$ralplan` 中进行架构综合
- 通过 `$ultragoal` 和 `.omx/ultragoal` 产物实现持久的多目标交接，作为规划后的默认完成路径
- 在任务需要时提供专家角色和支持技能
- 通过作用域化的 `AGENTS.md` 提供项目指引
- 在 `.omx/` 下持久化存储计划、日志、记忆和模式跟踪状态

如果你只需要纯 Codex 且不想额外增加工作流层，可能不需要 OMX。

## 快速入门

### 环境要求

- Node.js 20+
- 已安装并验证的 Codex CLI（通过 `codex --version`），且已完成认证（Homebrew 或 npm 均可；如果 Homebrew 已经管理了 `codex`，请勿使用 npm 重新安装 `@openai/codex`）
- 已在将运行 OMX 的同一 Shell/配置文件中配置并可见 Codex 认证信息
- macOS/Linux 上需要 `tmux`（若希望使用推荐的持久化团队运行时）
- 仅限原生 Windows，且仅当你有意使用支持度较低的 Windows 团队路径时才需要 `psmux`

### 一次良好的初始会话

安装后，请检查两个边界：

```bash
omx doctor
codex login status
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"
```

`omx doctor` 会捕获缺失的 OMX 文件、钩子及运行时依赖。真正的冒烟测试能捕获仅在 Codex 发起实际请求时才会出现的认证、配置和提供商/基础 URL 问题。

从 git 项目中按推荐方式启动 OMX：

```bash
omx --worktree=feat/task --madmax --high
```

在带有 `tmux` 的 macOS/Linux 交互式终端中，这默认会在 OMX 管理的分离式 tmux 中启动领导者进程，以便创建和恢复 HUD/运行时窗格。`--worktree` 还会将启动移至独立的 git checkout，这是在配合 `--madmax` 使用时更安全的默认方式。将 `feat/task` 替换为与任务相关的分支名称。

### Madmax 与 Worktree 启动安全

`--madmax` 是 OMX 对 Codex `--dangerously-bypass-approvals-and-sandbox` 的简写。它会移除常规的审批和沙盒护栏（sandbox guardrails），因此仅在可信仓库和环境使用。`--high` 是 `-c model_reasoning_effort="high"` 的简写。

当你在 git 仓库中使用 `--madmax` 时，优先使用 worktree 启动，而不是直接在当前 checkout 中运行。对于可重复或并行的工作，请使用命名的 worktree：

```bash
omx --worktree=feature/auth --madmax --high
```

如果你不在 git 仓库中，请省略 `--worktree`；worktree 启动需要 Git。

对于并行的 `--madmax` 会话，**请勿**将它们全部在同一目录下运行。为每个会话分配独立的命名 worktree：

```bash
omx --worktree=feature/auth --madmax --high
omx --worktree=fix/flaky-tests --madmax --high
```

不带名称的 `--worktree` / `-w` 会在 `../<repo>.omx-worktrees/launch-detached` 创建或重用分离式启动 worktree。带名称的 `--worktree=<name>`、`--worktree <name>` 或 `-w <name>` 会在 `../<repo>.omx-worktrees/` 下创建或重命名启用的 worktree，并检出该分支名。OMX 在启动 Codex 之前会消费 worktree 标志；它不会转发给 Codex 本身。将不带名称的分离形式视为一次性便利：如果在该 worktree 创建后源 checkout 发生推进，后续的无名称启动可能会因 `worktree_target_mismatch` 失败，因为 `launch-detached` 仍指向旧的 HEAD。对于重复性工作请使用命名 worktree，或在重试前移除旧的分离 worktree。
如果目标启动 worktree 已处于脏状态（dirty），OMX 会警告并直接启动，因此在依赖它进行隔离之前，请清理、提交或暂存该 worktree。

对于 `omx team`，工作进程默认已自动使用专用 worktrees；在 `omx team` 上使用 `--worktree` 仅为向后兼容的覆盖选项。

如果你希望一次性启动且无需 OMX tmux/HUD 管理，请使用 `--direct`：

```bash
omx --direct --yolo
```

对于持久化的 Shell/配置文件偏好，设置环境变量策略：

```bash
OMX_LAUNCH_POLICY=direct omx --yolo
```

恢复自动/默认行为：

```bash
unset OMX_LAUNCH_POLICY
```

CLI 策略标志优先于环境变量，且 `--` 之前的最后一个 CLI 策略标志生效：

```bash
OMX_LAUNCH_POLICY=direct omx --tmux --yolo
```

可使用 `OMX_LAUNCH_POLICY=direct|tmux|detached-tmux|auto`。本次迭代仅添加了 CLI 和环境控制；有意未添加配置文件设置。如果你在已有的 tmux 窗格内运行 `--direct`，OMX 不会创建 HUD 分割、启用鼠标模式或包装扩展键处理，但进程仍会在该已打开的终端窗格内运行。

然后尝试标准工作流：

```text
$deep-interview "clarify the authentication change"
$ralplan "approve the safest implementation path"
$ultragoal "turn the approved path into durable Codex goals"
```

当活跃的 Ultragoal 故事需要协调的并行工作时使用 `$team`，或当你希望由单一持久所有者持续推送到完成而无需多目标账本时使用 `$ralph`。

## 简单的思维模型

OMX **并不替代** Codex。

它在周围增加了一个更好的工作层：
- **Codex** 执行实际的智能体（agent）工作
- **OMX 角色关键词** 让常用角色可复用
- **OMX 技能** 让常见工作流可复用
- **.omx/** 存储计划、日志、记忆和运行时状态

大多数用户应将 OMX 视为**更好的任务路由 + 更好的工作流 + 更好的运行时**，而不是一个需要你整天手动操作的命令界面。

## 新手从这里开始

1. 如果已存在 Codex CLI，通过 `codex --version` 验证并使用 `npm install -g oh-my-codex` 安装或更新 OMX；否则若希望 npm 管理 Codex，请先单独安装 `@openai/codex`
2. 在安装或真实的 OMX 版本更新后，当你准备好时自行运行 `omx setup`，或使用 `omx update`（同时让 npm 检查并安装最新构建后再刷新设置）
3. 运行 `omx doctor`
4. 运行实际的执行冒烟测试：`codex login status` 和 `omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"`
5. 从 git 仓库使用命名 worktree 启动，例如 `omx --worktree=feat/task --madmax --high`；如果你运行并行的 `--madmax` 会话，请使用不同的命名 worktree（如 `--worktree=feature/auth`）
6. 当请求或边界尚不明确时使用 `$deep-interview "..."`
7. 使用 `$ralplan "..."` 批准计划并审查权衡取舍
8. 使用 `$ultragoal "..."` 将批准的计划转化为持久化目标和账本检查点

## 推荐工作流

1. `$deep-interview` — 当请求或边界尚模糊时澄清范围。
2. `$ralplan` — 将该澄清后的范围转化为已批准的建筑与实施方案。
3. `$ultragoal` — 将批准的方案持久化为带有 `.omx/ultragoal` 账本检查点（ledger checkpoints）的顺序 Codex 目标。

`$ralplan` 止步于计划产物和持久的共识交接。代码变更需要明确的执行通道（`$ultragoal`、`$team` 或有意的 `$ralph` 回退）；ralplan 不会直接实现代码。

在 Ultragoal 故事内部，仅当该故事受益于协调的并行执行时才使用 `$team`。当你不需要持久的多目标账本时，将 `$ralph` 作为有意的替代完成循环使用。

## 会话内常用界面

| 界面 | 用途 |
| --- | --- |
| `$deep-interview "..."` | 澄清意图、边界和非目标（non-goals） |
| `$ralplan "..."` | 批准实施方案和权衡取舍 |
| `$ultragoal "..."` | 在批准的计划后实现持久的多目标完成 |
| `$ralph "..."` | 持久化的完成与验证循环 |
| `$team "..."` | 当工作量足够大时进行协调的并行执行 |
| `/skills` | 浏览已安装的技能和支持辅助工具 |

## 高级 / 操作者界面

这些很有用，但它们不是主要的入门路径。

### 团队运行时

当你确实需要持久的 tmux/worktree 协调时使用团队运行时，而不是将其作为使用 OMX 的默认方式。在 Codex App 或纯非 tmux 会话中，将 `omx team` 视为 tmux 运行时的 Shell 界面，而非直接在应用内可用的工作流；如果你实际想要团队执行功能，请先从 Shell 启动 OMX CLI。

```bash
omx team 3:executor "fix the failing tests with verification"
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

### 设置、医生检查与 HUD

这些是操作者/支持界面：
- Codex 插件市场安装/发现可能会将插件缓存至 `${CODEX_HOME:-~/.codex}/plugins/cache/$MARKETPLACE_NAME/oh-my-codex/$VERSION/`（本地安装可能使用 `local` 作为版本标识符）；该打包插件包含用于官方 Codex 生命周期钩子、可选的 MCP 兼容服务器和应用的插件作用域辅助元数据（MCP/应用默认禁用），因此它仍与已安装的 `omx` CLI 配对以进行运行时执行
- `omx setup` 安装提示词、技能、AGENTS 脚手架、`.codex/config.toml`，以及（针对旧版安装或没有 `plugin_hooks` 的旧版 Codex）OMX 管理的原生 Codex 钩子 `.codex/hooks.json`
  - 设置刷新会保留 `.codex/hooks.json` 中的非 OMX 钩子条目，仅重写 OMX 管理的包装器
  - `omx setup --merge-agents` 会在保留现有 `AGENTS.md` 指引的同时，在 `<!-- OMX:AGENTS:START -->` / `<!-- OMX:AGENTS:END -->` 之间插入或刷新生成的 OMX 部分；若不使用 `--merge-agents` 或 `--force`，非交互式设置会跳过现有的 `AGENTS.md` 文件
  - `omx uninstall` 会从 `.codex/hooks.json` 中移除 OMX 管理的包装器，但如果用户钩子仍然存在则保留该文件
- `omx update` 会立即检查 npm，安装最新的全球 OMX 构建，然后重新运行相同的交互式设置刷新流程
- 启动时的更新检查默认限流并提示；使用 `OMX_AUTO_UPDATE=0` 禁用它们，或使用 `OMX_AUTO_UPDATE=defer` 安排延迟更新而不提示
- 新鲜的 OMX 管理的 `gpt-5.5` 配置播种现在推荐 `model_context_window = 250000` 和 `model_auto_compact_token_limit = 200000`，但仅在这些键缺失时生效
- `.omx-config.json` 模型/环境变量路由在[模型/环境变量路由参考](./docs/reference/omx-config-schema-routing.md)中记录；请仅编辑你安装的 OMX 版本支持的键
- `omx doctor` 会在出现问题时验证安装；它不能证明活跃的 Codex 配置能够进行认证的模型调用
- `omx hud --watch` 是监控/状态界面，而非主要用户工作流

对于非团队会话，原生 Codex 钩子现在是标准的生命周期界面：
- `plugins/oh-my-codex/hooks/hooks.json` = 插件安装的官方插件作用域钩子注册表
- `.codex/hooks.json` = 为旧版安装和旧版 Codex 保留的遗留/回退原生 Codex 钩子注册表
- `.omx/hooks/*.mjs` = OMX 插件钩子
- `omx tmux-hook` / notify-hook / derived watcher = tmux + 运行时回退路径

请参阅 [Codex 原生钩子映射](./docs/codex-native-hooks.md) 查看当前的原生/回退矩阵。

### 排查虚假绿色就绪状态

绿色的 `omx doctor` 意味着安装和本地运行时布线看起来正常。如果实际执行仍然失败，请检查 Codex 实际使用的环境：

- 从将启动 OMX 的同一 Shell/配置文件运行 `codex login status` 和 `omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"`。
- 在自定义 HOME、配置、容器或服务型 Shell 中，确认活跃的 `~/.codex`（或 `CODEX_HOME`）是包含预期认证和配置的那个。不要假设你的普通用户 `~/.codex` 在那里可见。
- 如果你依赖本地 OpenAI 兼容代理，请确认活跃的 `~/.codex/config.toml` 包含了预期的 `openai_base_url`；否则代理颁发的密钥可能会被发送到默认端点并因 `401 Unauthorized`、`Missing bearer or basic authentication in header` 或 `Incorrect API key provided` 失败。
- 如果 `omx doctor --team` 或恢复报告了陈旧的团队（如 `resume_blocker`）或缺少 tmux 会话，请在重试前清理死掉的运行时状态：

```bash
omx team shutdown <team-name> --force --confirm-issues
omx cancel
omx doctor --team
```

仅在你已确认团队已死亡或有意图放弃时才使用强制的团队关闭。

如果在 OMX 管理的 tmux 会话中 `Shift+Enter` 仍然提交而不是插入换行符，请参阅 [排查执行就绪状态](./docs/troubleshooting.md#shiftenter-submits-instead-of-inserting-a-newline-in-tmux-backed-omx-sessions)。当前的 OMX 已经在其自身的 Codex 启动路径周围启用了 tmux 扩展键转发，因此持续失败通常是 tmux 终端能力/可发现性问题，而非全新的 OMX 功能缺口。

### 探索与 Sparkshell

- `omx explore --prompt "..."` 用于只读仓库查找
- `omx sparkshell <command>` 用于 Shell 原生的检查和受限验证
- 当存在 `omx_wiki/` 时，`omx explore` 可以在回退到更广泛的仓库搜索之前注入 wiki-first 上下文
- 回退边界是明确的：sparkshell-backend 回退会在 stderr 报告，而 spark-model 回退会输出 stderr 元数据并在 stdout 中发出 `## OMX Explore fallback` 通知，以便用户了解成本/行为可能与低成本路径不同
- sparkshell 环境变量覆盖有意保持狭窄：`OMX_SPARKSHELL_BIN` 选择原生旁路路径，`OMX_SPARKSHELL_MODEL` 选择主摘要模型，`OMX_SPARKSHELL_FALLBACK_MODEL` 选择重试模型，`OMX_SPARKSHELL_MODEL_INSTRUCTIONS_FILE` 选择摘要指令，`OMX_SPARKSHELL_SUMMARY_TIMEOUT_MS` 控制本地 API 摘要超时

示例：

```bash
# 仅保留兼容性；对于新查找请使用正常的 Codex 仓库检查
omx explore --prompt "find where team state is written"
omx sparkshell git status
omx sparkshell --tmux-pane %12 --tail-lines 400
```

### Wiki

- `omx wiki` 是用于 Wiki 操作的 CLI-first JSON 界面；`omx_wiki` MCP 仅为显式兼容
- Wiki 数据作为仓库项目知识存储在 `omx_wiki/` 下
- Wiki 优先使用 Markdown 和搜索，而非向量（vector）

示例：

```bash
omx wiki list --json
omx wiki query --input '{"query":"session-start lifecycle"}' --json
omx wiki lint --json
omx wiki refresh --json
```

### 团队模式的平台说明

`omx team` 在带有 `tmux` 的 macOS/Linux 上效果最佳。原生 Windows 是次要路径，如果你希望在 Windows 主机上设置环境，WSL2 通常是更好的选择。在原生 Windows 上，OMX 接受 `psmux` 作为其已使用的现有 tmux 后端路径的 tmux 兼容二进制文件。

| 平台 | 安装方式 |
| --- | --- |
| macOS | `brew install tmux` |
| Ubuntu/Debian | `sudo apt install tmux` |
| Fedora | `sudo dnf install tmux` |
| Arch | `sudo pacman -S tmux` |
| Windows | `winget install psmux` |
| Windows (WSL2) | `sudo apt install tmux` |

## 已知问题

### Intel Mac：启动期间 `syspolicyd` / `trustd` CPU 占用过高

在某些 Intel Mac 上，OMX 启动（尤其是配合 `--madmax --high`）可能会导致 macOS Gatekeeper 在验证大量并发进程启动时引发 `syspolicyd` / `trustd` CPU 使用率飙升。

如果遇到此情况，请尝试：
- `xattr -dr com.apple.quarantine $(which omx)`
- 将你的终端应用添加到 macOS 安全设置中的开发者工具白名单
- 降低并发度（例如，避免使用 `--madmax --high`）

## 文档

- [快速入门](./docs/getting-started.html)
- [演示指南](./DEMO.md)
- [Wiki 功能](./docs/wiki-feature.md)
- [智能体目录](./docs/agents.html)
- [技能参考](./docs/skills.html)
- [Codex 原生钩子映射](./docs/codex-native-hooks.md)
- [GitHub / PR / 包身份流水线](./docs/pipeline/github-pr-package-identity.md)
- [集成](./docs/integrations.html)
- [排查执行就绪状态](./docs/troubleshooting.md)
- [OpenClaw / 通知网关指南](./docs/openclaw-integration.md)
- [贡献指南](./CONTRIBUTING.md)
- [更新日志](./CHANGELOG.md)

## 语言支持

- [English](./README.md)
- [한국어](./docs/readme/README.ko.md)
- [日本語](./docs/readme/README.ja.md)
- [简体中文](./docs/readme/README.zh.md)
- [繁體中文](./docs/readme/README.zh-TW.md)
- [Tiếng Việt](./docs/readme/README.vi.md)
- [Español](./docs/readme/README.es.md)
- [Português](./docs/readme/README.pt.md)
- [Русский](./docs/readme/README.ru.md)
- [Türkçe](./docs/readme/README.tr.md)
- [Deutsch](./docs/readme/README.de.md)
- [Français](./docs/readme/README.fr.md)
- [Italiano](./docs/readme/README.it.md)
- [Ελληνικά](./docs/readme/README.el.md)
- [Polski](./docs/readme/README.pl.md)
- [Українська](./docs/readme/README.uk.md)

## 贡献者

| 角色 | 姓名 | GitHub |
| --- | --- | --- |
| 创建者与负责人 | Yeachan Heo | [@Yeachan-Heo](https://github.com/Yeachan-Heo) |
| 维护者 | Doyun Ha | [@HaD0Yun](https://github.com/HaD0Yun) |
| 维护者 | Valeriy Pavlovich | [@iqdoctor](https://github.com/iqdoctor) |

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=Yeachan-Heo/oh-my-codex&type=date&legend=top-left)](https://www.star-history.com/#Yeachan-Heo/oh-my-codex&type=date&legend=top-left)

## 许可证

MIT