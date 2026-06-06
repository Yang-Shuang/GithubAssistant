# Superpowers

Superpowers 是一套完整的软件开发方法论，专为你的编码代理（coding agents）设计。它基于一套可组合的技能（skills）以及一组初始指令构建而成，确保你的代理能够正确使用这些技能。

## Quickstart

为你的代理赋予 Superpowers：[Claude Code](#claude-code)、[Codex CLI](#codex-cli)、[Codex App](#codex-app)、[Factory Droid](#factory-droid)、[Gemini CLI](#gemini-cli)、[OpenCode](#opencode)、[Cursor](#cursor)、[GitHub Copilot CLI](#github-copilot-cli)。

## How it works

当你启动编码代理时，流程便开始了。一旦它发现你在构建某个项目，它并不会立刻跳进去尝试写代码。相反，它会先退一步，询问你真正想实现的目标是什么。 

从对话中提炼出需求规格后，它会将其拆分为足够短的片段展示给你，以便你阅读和理解。 

你确认设计方案后，代理会制定一份实施计划。这份计划的清晰度足以让一个充满热情但品味不佳、缺乏判断力、对项目背景一无所知且讨厌写测试的初级工程师也能顺利执行。它强调真正的红/绿 TDD（RED-GREEN）、YAGNI（你不会需要它）和 DRY。 

接下来，当你发出“开始”指令后，它会启动 *subagent-driven-development* 流程。代理会逐一处理每个工程任务，检查并审查其工作成果，然后继续推进。Claude 能够自主运行数小时而不偏离你制定的计划，这并不罕见。

系统还有更多细节，但这就是核心机制。由于这些技能会自动触发，你无需进行任何特殊操作。你的编码代理就拥有了 Superpowers。


## Sponsorship

如果 Superpowers 帮助过你实现盈利，并且你愿意支持，我非常感谢你能考虑[赞助我的开源工作](https://github.com/sponsors/obra)。

谢谢！ 

- Jesse


## Installation

不同工具（harness）的安装方式略有差异。如果你同时使用多个，请分别为每个工具单独安装 Superpowers。

### Claude Code

Superpowers 可通过 [官方 Claude 插件市场](https://claude.com/plugins/superpowers) 获取。

#### Official Marketplace

- 从 Anthropic 官方市场安装插件：

  ```bash
  /plugin install superpowers@claude-plugins-official
  ```

#### Superpowers Marketplace

Superpowers 市场提供 Superpowers 及一些其他相关 Claude Code 插件。

- 注册该市场：

  ```bash
  /plugin marketplace add obra/superpowers-marketplace
  ```

- 从此市场安装插件：

  ```bash
  /plugin install superpowers@superpowers-marketplace
  ```

### Codex CLI

Superpowers 可通过 [官方 Codex 插件市场](https://github.com/openai/plugins) 获取。

- 打开插件搜索界面：

  ```bash
  /plugins
  ```

- 搜索 Superpowers：

  ```bash
  superpowers
  ```

- 选择 `Install Plugin`。

### Codex App

Superpowers 可通过 [官方 Codex 插件市场](https://github.com/openai/plugins) 获取。

- 在 Codex 应用中，点击侧边栏的 Plugins。
- 你应该能在 Coding 部分看到 `Superpowers`。
- 点击 `Superpowers` 旁边的 `+` 并按提示操作。

### Factory Droid

- 注册该市场：

  ```bash
  droid plugin marketplace add https://github.com/obra/superpowers
  ```

- 安装插件：

  ```bash
  droid plugin install superpowers@superpowers
  ```

### Gemini CLI

- 安装扩展：

  ```bash
  gemini extensions install https://github.com/obra/superpowers
  ```

- 后续更新：

  ```bash
  gemini extensions update superpowers
  ```

### OpenCode

OpenCode 使用其自身的插件安装机制；即使你已在其他工具中使用过，也请单独为 OpenCode 安装 Superpowers。

- 告知 OpenCode：

  ```
  Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
  ```

- 详细文档：[docs/README.opencode.md](docs/README.opencode.md)

### Cursor

- 在 Cursor Agent 聊天窗口中，从市场安装：

  ```text
  /add-plugin superpowers
  ```

- 或在插件市场中搜索 “superpowers”。

### GitHub Copilot CLI

- 注册该市场：

  ```bash
  copilot plugin marketplace add obra/superpowers-marketplace
  ```

- 安装插件：

  ```bash
  copilot plugin install superpowers@superpowers-marketplace
  ```

## The Basic Workflow

1. **brainstorming** - 在编写代码前激活。通过提问打磨初步想法，探索替代方案，分节展示设计方案以供验证。保存设计文档。

2. **using-git-worktrees** - 在设计审批后激活。在新分支上创建隔离的工作区，运行项目初始化配置，验证干净的测试基线。

3. **writing-plans** - 配合已批准的设计激活。将工作拆分为小块任务（每项约 2-5 分钟）。每个任务都包含精确的文件路径、完整代码和验证步骤。

4. **subagent-driven-development** or **executing-plans** - 配合计划激活。为每个任务分派新的子代理，并进行两阶段审查（先检查是否符合规范，再评估代码质量），或以批次方式执行并设置人工检查点。

5. **test-driven-development** - 在实现阶段激活。严格执行 RED-GREEN-REFACTOR：编写失败的测试，观察其失败，编写最小化代码使其通过，然后提交。删除测试前编写的代码。

6. **requesting-code-review** - 在任务之间激活。对照计划进行审查，按严重程度报告问题。关键问题会阻塞后续进度。

7. **finishing-a-development-branch** - 在任务完成后激活。验证测试，提供选项（merge/PR/keep/discard），并清理工作区。

**代理会在执行任何任务前检查相关技能。** 这是强制性工作流程，而非建议项。

## What's Inside

### Skills Library

**Testing**
- **test-driven-development** - RED-GREEN-REFACTOR 循环（包含测试反模式参考）

**Debugging**
- **systematic-debugging** - 四阶段根因分析流程（包含 root-cause-tracing、defense-in-depth、condition-based-waiting 等技术）
- **verification-before-completion** - 确保问题已真正修复

**Collaboration** 
- **brainstorming** - 苏格拉底式设计打磨
- **writing-plans** - 详细的实施计划
- **executing-plans** - 带检查点的批量执行
- **dispatching-parallel-agents** - 并发子代理工作流
- **requesting-code-review** - 审查前清单
- **receiving-code-review** - 响应反馈
- **using-git-worktrees** - 并行开发分支
- **finishing-a-development-branch** - Merge/PR 决策工作流
- **subagent-driven-development** - 带两阶段审查的快速迭代（先合规，后质量）

**Meta**
- **writing-skills** - 遵循最佳实践创建新技能（包含测试方法论）
- **using-superpowers** - 技能系统简介

## Philosophy

- **Test-Driven Development** - 始终先写测试
- **Systematic over ad-hoc** - 依靠流程而非猜测
- **Complexity reduction** - 以简洁为首要目标
- **Evidence over claims** - 声明成功前务必验证

阅读[原始发布公告](https://blog.fsck.com/2025/10/09/superpowers/)。

## Contributing

Superpowers 的通用贡献流程如下。请注意，我们通常不接受新技能的贡献，且任何技能更新必须能在所有支持的编码代理中正常运行。

1. Fork（克隆）本仓库
2. 切换到 `dev` 分支
3. 为你的工作创建新分支
4. 遵循 `writing-skills` 技能指南来创建和测试新/修改的技能
5. 提交 PR，并确保填写好拉取请求模板。

完整指南请参阅 `skills/writing-skills/SKILL.md`。

## Updating

Superpowers 的更新方式因编码代理而异，但通常会自动进行。

## License

MIT License - 详见 LICENSE 文件

## Community

Superpowers 由 [Jesse Vincent](https://blog.fsck.com) 及 [Prime Radiant](https://primeradiant.com) 团队共同开发。

- **Discord**：[加入我们](https://discord.gg/35wsABTejz) 获取社区支持、提问或分享你使用 Superpowers 构建的项目
- **Issues**：https://github.com/obra/superpowers/issues
- **Release announcements**：[注册](https://primeradiant.com/superpowers/) 以获取新版本通知