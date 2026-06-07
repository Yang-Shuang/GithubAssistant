# 复合工程（Compound Engineering）

[![Build Status](https://github.com/EveryInc/compound-engineering-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/EveryInc/compound-engineering-plugin/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/@every-env/compound-plugin)](https://www.npmjs.com/package/@every-env/compound-plugin)

让每一项工程任务都比前一项更轻松的人工智能技能与智能体（agent）。

## 理念

**每一项工程任务都应使后续任务变得更简单，而不是更复杂。**

传统开发会不断累积技术债务。每个功能都会增加复杂度。每次修复 bug 都会留下一些本地知识，导致后来者不得不重新发现。代码库越来越大，上下文（context）越来越难以把握，下一次变更的速度也会变慢。

复合工程颠覆了这一模式。80% 的精力用于规划与审查，20% 用于执行：

- 在编写代码前使用 `/ce-brainstorm` 和 `/ce-plan` 进行充分规划
- 通过 `/ce-code-review` 和 `/ce-doc-review` 进行审查，以发现问题并校准判断力
- 使用 `/ce-compound` 将知识固化以便复用
- 保持高质量代码，让后续变更更轻松

核心不在于流程形式，而在于杠杆效应。充分的头脑风暴能让规划更精准；优秀的规划能缩小执行范围；高质量的审查能捕捉模式而不仅是 bug；好的复合笔记意味着下一个智能体无需从头学习同样的教训。

**了解更多**

- [完整组件参考](plugins/compound-engineering/README.md) - 所有技能与智能体
- [Compound engineering: how Every codes with agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents)
- [The story behind compounding engineering](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)

## 工作流

`/ce-strategy` 位于循环上游——它将产品的目标问题、方法、用户画像、指标和赛道记录为简短持久的锚点，保存在 `STRATEGY.md` 中。当该文件存在时，构思（ideate）与规划会将其作为基础上下文读取，使战略决策直接流向功能构思、优先级排序和规范制定。

核心循环是：头脑风暴需求、规划实现方案、执行计划、审查结果、固化学习成果，然后带着更丰富的上下文重复该过程。

如果你希望智能体在选定一个方向进行头脑风暴前先生成并批判性评估更大的构想，可在循环开始前使用 `/ce-ideate`。它会输出一个排序后的构思产物，而非需求、计划或代码。

| 技能/命令 | 用途 |
|-------|---------|
| `/ce-strategy` | 创建或维护 `STRATEGY.md` ——记录产品的目标问题、方法、用户画像、关键指标和赛道。构思、头脑风暴与规划会读取它作为基础上下文 |
| `/ce-ideate` | 可选的全局构思：生成并批判性评估基于上下文的构想，然后将最有力的一个送入头脑风暴流程 |
| `/ce-brainstorm` | 交互式问答，用于推演功能或问题，并在规划前编写一份篇幅恰当的需求文档 |
| `/ce-plan` | 将功能想法转化为详细的实现计划 |
| `/ce-work` | 通过工作树（worktrees）和任务跟踪执行计划 |
| `/ce-debug` | 系统性复现故障、追踪根本原因并实施修复 |
| `/ce-code-review` | 合并前的多智能体代码审查 |
| `/ce-compound` | 记录学习成果，让后续工作更轻松 |
| `/ce-product-pulse` | 生成单页时间窗口脉冲报告，涵盖使用量、性能、错误及跟进事项。保存至 `docs/pulse-reports/` |

`/ce-product-pulse` 是读取侧的配套工具——它生成一份基于时间窗口的报告，展示用户在指定时间段（如 24h、7d 等）内的实际体验及产品表现。报告保存至 `docs/pulse-reports/`，使历史脉冲记录形成可浏览的用户成果时间线。下一次战略更新与头脑风暴都能获得真实的信号作为锚点。

每个循环都会产生复利效应：头脑风暴让规划更精准，规划为未来计划提供依据，审查发现更多问题，模式得以文档化。

## 快速示例

一个典型循环始于将粗略想法转化为需求文档，随后基于该文档进行规划，再将执行权移交 `/ce-work`：

```text
/ce-brainstorm "make background job retries safer"
/ce-plan docs/brainstorms/background-job-retry-safety-requirements.md
/ce-work
/ce-code-review
/ce-compound
```

针对聚焦的 bug 调查：

```text
/ce-debug "the checkout webhook sometimes creates duplicate invoices"
/ce-code-review
/ce-compound
```

## 入门指南

安装后，在任何项目中运行 `/ce-setup`。它会检查你的环境、安装缺失的工具并引导配置项目设置。

`compound-engineering` 插件目前提供 37 项技能和 51 个智能体。完整清单请参阅[完整组件参考](plugins/compound-engineering/README.md)。

---

## 安装

### Claude Code

```text
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering
```

### Cursor

在 Cursor Agent 聊天中，从插件市场（plugin marketplace）安装：

```text
/add-plugin compound-engineering
```

或在插件市场中搜索 "compound engineering"。

### Codex

分三步操作：注册市场、安装智能体集，然后通过 Codex 的 TUI 安装插件。

1. **向 Codex 注册市场：**

   ```bash
   codex plugin marketplace add EveryInc/compound-engineering-plugin
   ```

2. **安装复合工程智能体**（Codex 的插件规范目前尚未支持注册自定义智能体）：

   ```bash
   bunx @every-env/compound-plugin install compound-engineering --to codex
   ```

3. **通过 Codex 的 TUI 安装插件：** 启动 `codex`，运行 `/plugins`，找到 **Compound Engineering** 市场，选择 **compound-engineering** 插件，并点击 **Install**。安装完成后重启 Codex。Codex 的 CLI 可以注册市场，但目前未暴露从已添加市场中安装插件的子命令——必须使用 `/plugins` TUI 进行安装才能启用 CE 技能。

以上三步缺一不可。市场注册配合 TUI 安装负责处理技能；Bun 步骤则添加审查、研究与工作流智能体，供 `$ce-code-review`、`$ce-plan` 和 `$ce-work` 等技能在 Codex 中调用。若跳过智能体步骤，委派技能时会提示缺少智能体。

对于非默认配置的 Codex 配置文件（profile），请将所有与 Codex 相关的步骤指向相同的 `CODEX_HOME`。以下示例将 CE 安装至 `work` 配置：

```bash
CODEX_HOME="$HOME/.codex/profiles/work" codex plugin marketplace add EveryInc/compound-engineering-plugin
CODEX_HOME="$HOME/.codex/profiles/work" bunx @every-env/compound-plugin install compound-engineering --to codex
CODEX_HOME="$HOME/.codex/profiles/work" codex
```

在 Codex 内部，运行 `/plugins`，选择 **Compound Engineering**，然后安装 **compound-engineering**。市场步骤仅使插件可用；TUI 安装才是激活该配置原生 CE 技能的关键。

若从当前检出目录进行本地开发，可注册当前工作树并使用本地 CLI：

```bash
CODEX_HOME="$HOME/.codex/profiles/work" codex plugin marketplace add "$PWD"
CODEX_HOME="$HOME/.codex/profiles/work" bun run src/index.ts install ./plugins/compound-engineering --to codex
CODEX_HOME="$HOME/.codex/profiles/work" codex
```

> **注意：** 一旦 Codex 的原生插件规范支持自定义智能体，Bun 智能体步骤将不再需要。届时仅通过 TUI 安装即可满足需求。

若你之前使用过纯 Bun 的 Codex 安装方式，在切换前请备份残留的 CE 文件：

```bash
bunx @every-env/compound-plugin cleanup --target codex
```

### GitHub Copilot

针对 **VS Code Copilot Agent Plugins**：

1. 从 VS Code 命令面板运行 `Chat: Install Plugin from Source`
2. 仓库使用 `EveryInc/compound-engineering-plugin`
3. 当 VS Code 显示该仓库中的插件时，选择 `compound-engineering`

针对 **Copilot CLI**，请使用：

在 Copilot CLI 内部：

```text
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering@compound-engineering-plugin
```

在包含 `copilot` 二进制的 shell 中：

```bash
copilot plugin marketplace add EveryInc/compound-engineering-plugin
copilot plugin install compound-engineering@compound-engineering-plugin
```

Copilot CLI 会读取现有的 Claude 兼容插件清单，因此无需单独的 Bun 安装步骤。

若你之前使用过旧的 Bun Copilot 安装方式，在切换至原生插件前请备份残留的 CE 文件：

```bash
bunx @every-env/compound-plugin cleanup --target copilot
```

### Factory Droid

在包含 `droid` 二进制的 shell 中：

```bash
droid plugin marketplace add https://github.com/EveryInc/compound-engineering-plugin
droid plugin install compound-engineering@compound-engineering-plugin
```

Droid 使用 `plugin@marketplace` 格式的插件 ID；此处 `compound-engineering` 为插件名，`compound-engineering-plugin` 为市场名。Droid 会安装现有的 Claude Code 兼容插件并自动转换格式，因此无需 Bun 安装步骤。

若你之前使用过旧的 Bun Droid 安装方式，在切换至原生插件前请备份残留的 CE 文件：

```bash
bunx @every-env/compound-plugin cleanup --target droid
```

### Qwen Code

```bash
qwen extensions install EveryInc/compound-engineering-plugin:compound-engineering
```

Qwen Code 会直接从 GitHub 安装 Claude Code 兼容插件，并在安装过程中转换格式，因此无需 Bun 安装步骤。

若你之前使用过旧的 Bun Qwen 安装方式，在切换至原生扩展前请备份残留的 CE 文件：

```bash
bunx @every-env/compound-plugin cleanup --target qwen
```

### OpenCode、Pi、Gemini 与 Kiro

本仓库包含一个 Bun/TypeScript 安装器，可将复合工程插件转换为适用于 OpenCode、Pi、Gemini CLI 和 Kiro CLI 的格式。

```bash
bunx @every-env/compound-plugin install compound-engineering --to opencode
bunx @every-env/compound-plugin install compound-engineering --to pi
bunx @every-env/compound-plugin install compound-engineering --to gemini
bunx @every-env/compound-plugin install compound-engineering --to kiro
```

**Pi 前置条件。** Pi 未提供原生的子智能体（subagent）基础组件，因此 Pi 安装依赖 [nicobailon/pi-subagents](https://github.com/nicobailon/pi-subagents)（必需），并推荐使用 [edlsh/pi-ask-user](https://github.com/edlsh/pi-ask-user) 以支持更丰富的阻塞式用户提问：

```bash
pi install npm:pi-subagents    # 必需 — 提供技能调度并行智能体时使用的 `subagent` 工具
pi install npm:pi-ask-user     # 推荐 — 提供 `ask_user` 工具；若缺失，技能将回退为聊天中的编号选项
```

若要自动检测自定义安装目标并批量安装：

```bash
bunx @every-env/compound-plugin install compound-engineering --to all
```

自定义安装目标在安装时会运行 CE 遗留清理。如需手动针对特定目标执行清理：

```bash
bunx @every-env/compound-plugin cleanup --target codex
bunx @every-env/compound-plugin cleanup --target opencode
bunx @every-env/compound-plugin cleanup --target pi
bunx @every-env/compound-plugin cleanup --target gemini
bunx @every-env/compound-plugin cleanup --target kiro
bunx @every-env/compound-plugin cleanup --target copilot   # 仅旧版 Bun 安装需要
bunx @every-env/compound-plugin cleanup --target droid     # 仅旧版 Bun 安装需要
bunx @every-env/compound-plugin cleanup --target qwen      # 仅旧版 Bun 安装需要
bunx @every-env/compound-plugin cleanup --target windsurf  # 仅已弃用的遗留安装需要
```

清理操作会将已知的 CE 文件移至目标根目录下的 `compound-engineering/legacy-backup/` 目录中。

---

## 本地开发

```bash
bun install
bun test
bun run release:validate
```

### 从你的本地检出目录运行

适用于活跃开发——对插件源码的修改会立即生效。

**Claude Code** ——添加 shell 别名，使你的本地副本与常规插件并行加载：

```bash
alias cce='claude --plugin-dir ~/Code/compound-engineering-plugin/plugins/compound-engineering'
```

运行 `cce` 替代 `claude` 以测试你的更改。你的生产环境安装保持不变。

**Codex 及其他目标** ——针对检出目录运行本地 CLI：

```bash
# 从仓库根目录执行
bun run src/index.ts install ./plugins/compound-engineering --to codex

# 其他目标遵循相同模式
bun run src/index.ts install ./plugins/compound-engineering --to opencode
```

### 从已推送的分支运行

适用于测试他人或你自己的工作树（worktree）分支，无需切换检出目录。使用 `--branch` 将分支克隆至确定性缓存目录。

> **未推送的本地分支**：若分支仅存在于本地工作树且尚未推送到远程，请直接将 `--plugin-dir` 指向工作树路径（例如 `claude --plugin-dir /path/to/worktree/plugins/compound-engineering`）。

**Claude Code** ——使用 `plugin-path` 获取缓存克隆路径：

```bash
# 从仓库根目录执行
bun run src/index.ts plugin-path compound-engineering --branch feat/new-agents
# 输出：
#   claude --plugin-dir ~/.cache/compound-engineering/branches/compound-engineering-feat~new-agents/plugins/compound-engineering
```

缓存路径是确定性的。重新运行会将检出目录更新至该分支的最新提交。

**Codex、OpenCode 及其他目标** ——向 `install` 传递 `--branch`：

```bash
# 从仓库根目录执行
bun run src/index.ts install compound-engineering --to codex --branch feat/new-agents

# 适用于任意目标
bun run src/index.ts install compound-engineering --to opencode --branch feat/new-agents

# 结合 --also 可同时安装至多个目标
bun run src/index.ts install compound-engineering --to codex --also opencode --branch feat/new-agents
```

两项功能均使用 `COMPOUND_PLUGIN_GITHUB_SOURCE` 环境变量解析仓库地址，默认为 `https://github.com/EveryInc/compound-engineering-plugin`。

### Shell 别名

添加至 `~/.zshrc` 或 `~/.bashrc`。所有别名均调用本地 CLI，因此不依赖 npm 发布。`plugin-path` 仅将路径输出至 stdout，便于与 `$()` 组合使用。

```bash
CE_REPO=~/Code/compound-engineering-plugin

ce-cli() { bun run "$CE_REPO/src/index.ts" "$@"; }

# --- 本地检出（活跃开发）---
alias cce='claude --plugin-dir $CE_REPO/plugins/compound-engineering'

codex-ce() {
  ce-cli install "$CE_REPO/plugins/compound-engineering" --to codex "$@"
}

# --- 已推送分支（测试 PR、工作树工作流）---
ccb() {
  claude --plugin-dir "$(ce-cli plugin-path compound-engineering --branch "$1")" "${@:2}"
}

codex-ceb() {
  ce-cli install compound-engineering --to codex --branch "$1" "${@:2}"
}
```

用法：

```bash
cce                              # 本地检出 + Claude Code
codex-ce                         # 安装本地检出于 Codex
ccb feat/new-agents              # 使用 Claude Code 测试已推送分支
ccb feat/new-agents --verbose    # 额外标志将转发至 claude
codex-ceb feat/new-agents        # 安装已推送分支至 Codex
```

Codex 的安装会将生成的插件技能隔离在 `~/.codex/skills/compound-engineering/` 下，且不会向 `~/.agents` 写入新文件。当安装器能证明旧的 CE 管理的 `.agents/skills` 符号链接指向 CE 的 Codex 管理存储时，它会自动移除这些旧链接，从而防止残留的 Codex 安装覆盖 Copilot 的原生插件安装。

## 故障排除

### Codex 技能正常但审查或研究委派失败

运行智能体安装步骤：

```bash
bunx @every-env/compound-plugin install compound-engineering --to codex
```

原生 Codex 插件安装仅处理技能。Bun 步骤负责安装这些技能所委派的自定义智能体。

### Codex 显示陈旧或重复的 CE 技能

在切换至原生 Codex 插件流程前，请备份旧的 Bun 安装文件：

```bash
bunx @every-env/compound-plugin cleanup --target codex
```

### Copilot、Droid 或 Qwen 加载了陈旧的 CE 技能

在使用原生插件路径前，请备份旧的 Bun 安装文件：

```bash
bunx @every-env/compound-plugin cleanup --target copilot
bunx @every-env/compound-plugin cleanup --target droid
bunx @every-env/compound-plugin cleanup --target qwen
```

## 限制说明

Codex 的原生插件安装目前仅处理技能，不处理自定义智能体。在 Codex 支持其原生插件规范中的智能体之前，文档中记录的 Bun 后续步骤为必需项。

OpenCode、Pi、Gemini 和 Kiro 的安装基于转换器实现，可能会随着目标格式演进而发生变化。

发布版本由自动化流程管理。常规功能 PR 不应手动提升插件或市场清单的版本号。

## 常见问题（FAQ）

### 我需要在 Claude Code 中使用 Bun 吗？

不需要。Claude Code 直接从插件市场安装。Bun 仅用于转换器支持的目标、Codex 当前的智能体后续步骤、本地开发以及清理旧的转换后安装文件。

### 为什么 Codex 需要单独的 Bun 步骤？

Codex 的原生插件流程会从 Codex 插件清单中安装技能，但目前不会安装复合工程技能所委派的自定义审查员、研究员和工作流智能体。Bun 步骤用于填补这一空白。

### 在哪里查看所有可用的技能与智能体？

阅读[复合工程插件 README](plugins/compound-engineering/README.md)。其中列出了当前的技能与智能体清单。

### 发布历史在哪里？

GitHub Releases 是官方的发布说明载体。根目录下的 [`CHANGELOG.md`](CHANGELOG.md) 指向该历史记录。

## 关于贡献（About Contributions）

*关于贡献：* 请别误会，但我并不接受外部项目的贡献。我确实没有足够的精力去审查任何 PR，而且项目挂的是我的名字，我对它可能引发的问题负有全部责任；因此，从我的角度来看，风险与收益极度不对等。此外，我还得考虑其他“利益相关者”的意见，这对于我主要为个人免费开发的工具来说显然不明智。欢迎提交 issue，如果你希望展示修复方案也可以提 PR，但请知悉我不会直接合并它们。相反，我会让 Claude 或 Codex 通过 `gh` 审查提交内容，并独立决定是否以及如何解决。尤其是 bug 报告非常受欢迎。如果这让你感到不适，我深表歉意，但我希望能避免浪费时间与伤感情。我理解这与当前追求社区贡献的开源主流理念不符，但这是我保持开发速度与精神健康的唯一方式。

## 许可证

[MIT](LICENSE)