<div align="center">

# GET SHIT DONE

**English** · [Português](README.pt-BR.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md)

**一个面向 Claude Code、OpenCode、Gemini CLI、Kilo、Codex、Copilot、Cursor、Windsurf 等工具的轻量级元提示（meta-prompting）、上下文工程与规范驱动开发系统。**

**解决上下文腐烂（context rot）问题——即随着你的 AI 填满其上下文窗口而发生的质量退化现象。**

[![npm version](https://img.shields.io/npm/v/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![npm downloads](https://img.shields.io/npm/dm/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![Tests](https://img.shields.io/github/actions/workflow/status/gsd-build/get-shit-done/test.yml?branch=main&style=for-the-badge&logo=github&label=Tests)](https://github.com/gsd-build/get-shit-done/actions/workflows/test.yml)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/mYgfVNfA2r)
[![X (Twitter)](https://img.shields.io/badge/X-@gsd__foundation-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/gsd_foundation)
[![$GSD Token](https://img.shields.io/badge/$GSD-Dexscreener-1C1C1C?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgZmlsbD0iIzAwRkYwMCIvPjwvc3ZnPgo=&logoColor=00FF00)](https://dexscreener.com/solana/dwudwjvan7bzkw9zwlbyv6kspdlvhwzrqy6ebk8xzxkv)
[![GitHub stars](https://img.shields.io/github/stars/gsd-build/get-shit-done?style=for-the-badge&logo=github&color=181717)](https://github.com/gsd-build/get-shit-done)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

<br>

```bash
npx get-shit-done-cc@latest
```

**支持 Mac、Windows 和 Linux。**

<br>

![GSD Install](assets/terminal.svg)

<br>

*"如果你清楚自己想要什么，它就能为你构建出来。绝不废话。"*

*"我用过 SpecKit、OpenSpec 和 Taskmaster——这个工具给我的效果最好。"*

*"迄今为止对我使用 Claude Code 最强大的补充。没有过度设计，真的就是能干活。"*

<br>

**被亚马逊、Google、Shopify 和 Webflow 的工程师所信赖。**

</div>

---

> [!IMPORTANT]
> **重新回到 GSD？**
>
> 运行 `/gsd-map-codebase` 重新索引你的代码库，然后执行 `/gsd-new-project` 重建 GSD 的规划上下文。你的代码没有问题——GSD 只是需要重建其上下文。有关新增内容，请参阅 [CHANGELOG](CHANGELOG.md)。

---

## 我为什么构建这个工具

我是独立开发者。我不写代码——由 Claude Code 代劳。

市面上已有其他规范驱动工具，但它们都是为 50 人规模的工程团队设计的——冲刺仪式、故事点、利益相关者同步、Jira 工作流。我不是那样的人。我是一个试图持续构建优秀作品的创意工作者。

所以我构建了 GSD。复杂性隐藏在系统内部，而非你的工作流中。幕后：上下文工程、XML 提示词格式化、子代理编排（subagent orchestration）、状态管理。你看到的：几个能直接生效的命令。

该系统为 Claude 提供了完成工作并验证它所需的一切。我信任这套工作流。它只是干得漂亮。

— **TÂCHES**

---

## 它是如何工作的

核心循环由六个命令组成。每个命令只做一件事。

### 1. 初始化

```bash
/gsd-new-project
```

提问 → 调研 → 需求 → 路线图。你审核通过后，即可开始构建。

> **已有代码？** 请先运行 `/gsd-map-codebase`。它会分析你的技术栈、架构和约定，以便 `/gsd-new-project` 提出正确的问题。

### 2. 讨论

```bash
/gsd-discuss-phase 1
```

你的路线图每个阶段只有一句话。这不足以按照你*想象*的方式将其构建出来。讨论环节会在任何规划开始前捕获你的决策：布局、API 形态、错误处理、数据结构——以及该特定阶段存在的所有模糊地带。

输出结果将直接用于调研和规划。跳过它，获得合理默认值；使用它，实现你的构想。

### 3. 规划

```bash
/gsd-plan-phase 1
```

调研 → 规划 → 验证，循环进行直到规划通过。每个规划的规模都足够小，可以在全新的上下文窗口中执行。

### 4. 执行

```bash
/gsd-execute-phase 1
```

规划以并行波次运行。每个执行器获得一个全新的 200k token 上下文。每个任务都有自己独立的原子提交。随时离开，回来时面对的是已完成的工作和干净的 Git 历史。

你的主上下文窗口始终保持在 30%–40%。实际工作由子代理完成。

### 5. 验证

```bash
/gsd-verify-work 1
```

逐步检查已构建的内容。任何损坏的部分都会生成诊断修复计划——随时准备重新执行。你无需手动调试；只需再次运行执行命令即可。

### 6. 重复 → 交付

```bash
/gsd-ship 1
/gsd-complete-milestone
/gsd-new-milestone
```

循环执行讨论 → 规划 → 执行 → 验证 → 交付，直到里程碑完成。然后归档、打标签，并从头开始下一个。

---

## 快速上手

```bash
npx get-shit-done-cc@latest
```

安装程序会提示你选择运行环境（Claude Code、OpenCode、Gemini CLI、Kilo、Codex、Copilot、Cursor、Windsurf 等），以及是全局还是本地安装。

```bash
claude --dangerously-skip-permissions
```

GSD 专为无缝自动化而设计。跳过权限正是其预期运行方式。

使用 `--profile=core`（六个核心循环技能）、`--profile=standard`（核心 + 阶段管理）或默认完整安装来仅安装你需要的技能。配置文件可组合：`--profile=core,audit`。`--minimal` 是 `--profile=core` 的别名。请参阅 **[docs/USER-GUIDE.md](docs/USER-GUIDE.md)** 获取完整指南、所有 15 种运行环境的非交互式安装标志以及权限配置说明。有关配置文件模型和运行环境表面控制，请参阅 [ADR-0011](docs/adr/0011-skill-surface-budget-module.md)。

---

## 命令

核心循环：

| Command | What it does |
|---------|--------------|
| `/gsd-new-project` | 提问 → 调研 → 需求 → 路线图 |
| `/gsd-discuss-phase [N]` | 在规划前捕获实施决策 |
| `/gsd-plan-phase [N]` | 调研 + 规划 + 验证 |
| `/gsd-execute-phase <N>` | 以并行波次执行规划 |
| `/gsd-verify-work [N]` | 手动验收测试 |
| `/gsd-ship [N]` | 基于已验证的阶段工作创建 PR |
| `/gsd-progress --next` | 自动检测并运行下一步 |
| `/gsd-complete-milestone` | 归档里程碑并标记发布版本 |
| `/gsd-new-milestone` | 开始下一个版本 |
| `/gsd:surface` | 在运行时启用/禁用技能集群，无需重新安装 |

对于临时任务、自主模式、代码库分析、取证及完整命令集——请参阅 **[docs/COMMANDS.md](docs/COMMANDS.md)**。

---

## 为什么它能生效

大多数 AI 编程设置都存在三个误区：

**1. 上下文膨胀。** 随着会话增长，质量会下降。GSD 通过在全新的子代理上下文中执行繁重工作来保持你的主上下文整洁。调研、规划和执行人员各自从头开始，仅加载所需内容。

**2. 缺乏共享记忆。** GSD 维护跨越会话边界持久化的结构化工件：`PROJECT.md`（愿景）、`REQUIREMENTS.md`（范围）、`ROADMAP.md`（目标方向）、`STATE.md`（当前位置与决策）、`CONTEXT.md`（各阶段实施决策）。每次新会话都会加载这些文件，清楚当前状态。

**3. 缺乏验证。** “能运行”的代码不等于“能用”的代码。GSD 的验证步骤会引导你检查已构建内容，通过专用调试代理诊断失败原因，并在你宣布阶段完成前生成修复计划。

有关多代理编排和上下文工程的具体工作原理，请参阅 **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**。

---

## 配置

设置位于 `.planning/config.json`。可在 `/gsd-new-project` 期间进行配置，或通过 `/gsd-settings` 更新。

关键调节项：

| Setting | What it controls |
|---------|-----------------|
| `mode` | `interactive`（确认每一步）或 `yolo`（自动批准） |
| Model profiles | `quality` / `balanced` / `budget` ——控制每个代理使用的模型 |
| `workflow.research` / `plan_check` / `verifier` | 切换增加 token 和时间的质量代理开关 |
| `parallelization.enabled` | 同时运行独立规划 |

可选的结构审查：将 `code_quality.fallow.enabled` 设置为 `true`，以在 `/gsd-code-review` 中添加一个 fallow 预检步骤。GSD 会写入 `.planning/phases/<phase>/FALLOW.json`，并在 `REVIEW.md` 中展示 `Structural Findings (fallow)` 部分。使用 `npm install -D fallow@^2.70.0`（或通过 `cargo install fallow` 全局安装）进行安装；请注意，Rust 二进制文件的 JSON Schema 必须与文档化的 v2.70+ 契约匹配——旧版本可能会产生静默的零结果输出。

完整配置参考（所有设置、Git 分支策略、各运行环境模型覆盖、工作流配置继承、代理技能注入）请参阅 **[docs/CONFIGURATION.md](docs/CONFIGURATION.md)**。

---

## 文档

| Doc | What's in it |
|-----|-------------|
| [用户指南](docs/USER-GUIDE.md) | 端到端指南、安装选项、所有运行环境标志、配置参考 |
| [命令集](docs/COMMANDS.md) | 包含标志和示例的完整命令列表 |
| [配置说明](docs/CONFIGURATION.md) | 完整配置 Schema、模型配置、Git 分支策略 |
| [架构设计](docs/ARCHITECTURE.md) | 多代理编排工作原理 |
| [CLI 工具](docs/CLI-TOOLS.md) | `gsd-sdk query` 及编程式 SDK 调度接口 |
| [功能列表](docs/FEATURES.md) | 完整功能索引 |
| [更新日志](CHANGELOG.md) | 各版本变更内容 |

---

## 故障排除

**命令不显示？** 安装后请重启你的运行环境。GSD 会安装到 `~/.claude/skills/gsd-*/`（Claude Code）、`~/.codex/skills/gsd-*/`（Codex）或对应环境的等效路径中。

**出错了？** 重新运行安装程序——它是幂等的：
```bash
npx get-shit-done-cc@latest
```

**容器或 Docker？** 在安装前设置 `CLAUDE_CONFIG_DIR` 以避免波浪号展开问题：
```bash
CLAUDE_CONFIG_DIR=/home/youruser/.claude npx get-shit-done-cc --global
```

完整的故障排除和卸载说明请参阅 **[docs/USER-GUIDE.md](docs/USER-GUIDE.md#troubleshooting)**。

---

## 社区

| Project | Platform |
|---------|----------|
| [gsd-opencode](https://github.com/rokicool/gsd-opencode) | 原始 OpenCode 移植版 |
| [Discord](https://discord.gg/mYgfVNfA2r) | 社区支持 |

---

## Star History

<a href="https://star-history.com/#gsd-build/get-shit-done&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=gsd-build/get-shit-done&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=gsd-build/get-shit-done&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=gsd-build/get-shit-done&type=Date" />
 </picture>
</a>

---

## 许可证

采用 MIT 许可证。详见 [LICENSE](LICENSE)。

---

<div align="center">

**Claude Code 功能强大。GSD 使其可靠。**

</div>