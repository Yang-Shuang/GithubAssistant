<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec">
    <picture>
      <source srcset="assets/openspec_bg.png">
      <img src="assets/openspec_bg.png" alt="OpenSpec logo">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://www.npmjs.com/package/@fission-ai/openspec"><img alt="npm version" src="https://img.shields.io/npm/v/@fission-ai/openspec?style=flat-square" /></a>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" /></a>
  <a href="https://discord.gg/YctCnvvshC"><img alt="Discord" src="https://img.shields.io/discord/1411657095639601154?style=flat-square&logo=discord&logoColor=white&label=Discord&suffix=%20online" /></a>
</p>

<details>
<summary><strong>最深受喜爱的规范框架。</strong></summary>

[![Stars](https://img.shields.io/github/stars/Fission-AI/OpenSpec?style=flat-square&label=Stars)](https://github.com/Fission-AI/OpenSpec/stargazers)
[![Downloads](https://img.shields.io/npm/dm/@fission-ai/openspec?style=flat-square&label=Downloads/mo)](https://www.npmjs.com/package/@fission-ai/openspec)
[![Contributors](https://img.shields.io/github/contributors/Fission-AI/OpenSpec?style=flat-square&label=Contributors)](https://github.com/Fission-AI/OpenSpec/graphs/contributors)

</details>
<p></p>
我们的核心理念：

```text
→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
→ scalable from personal projects to enterprises
```

> [!TIP]
> **全新工作流现已上线！** 我们已基于新的制品（artifact）引导式工作流重构了 OpenSpec。
>
> 运行 `/opsx:propose "你的想法"` 即可开始使用。 → [在此了解更多](docs/opsx.md)

<p align="center">
  关注 <a href="https://x.com/0xTab">@0xTab on X</a> 获取更新 · 加入 <a href="https://discord.gg/YctCnvvshC">OpenSpec Discord</a> 社区寻求帮助与提问。
</p>

<!-- TODO: Add GIF demo of /opsx:propose → /opsx:archive workflow -->

## 实际运行效果

```text
You: /opsx:propose add-dark-mode
AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md — why we're doing this, what's changing
     ✓ specs/       — requirements and scenarios
     ✓ design.md    — technical approach
     ✓ tasks.md     — implementation checklist
     Ready for implementation!

You: /opsx:apply
AI:  Implementing tasks...
     ✓ 1.1 Add theme context provider
     ✓ 1.2 Create toggle component
     ✓ 2.1 Add CSS variables
     ✓ 2.2 Wire up localStorage
     All tasks complete!

You: /opsx:archive
AI:  Archived to openspec/changes/archive/2025-01-23-add-dark-mode/
     Specs updated. Ready for the next feature.
```

<details>
<summary><strong>OpenSpec Dashboard</strong></summary>

<p align="center">
  <img src="assets/openspec_dashboard.png" alt="OpenSpec dashboard preview" width="90%">
</p>

</details>

## 快速上手

**需要 Node.js 20.19.0 或更高版本。**

全局安装 OpenSpec：

```bash
npm install -g @fission-ai/openspec@latest
```

然后进入你的项目目录并初始化：

```bash
cd your-project
openspec init
```

现在告诉你的 AI：`/opsx:propose <你想构建的内容>`

如需使用扩展工作流（`/opsx:new`、`/opsx:continue`、`/opsx:ff`、`/opsx:verify`、`/opsx:bulk-archive`、`/opsx:onboard`），请通过 `openspec config profile` 进行选择，并使用 `openspec update` 应用配置。

> [!NOTE]
> 不确定你的工具是否受支持？[查看完整列表](docs/supported-tools.md)——我们已支持 25+ 款工具并持续增加。
>
> 同样兼容 pnpm、yarn、bun 和 nix。[查看安装选项](docs/installation.md)。

## 文档索引

→ **[快速入门](docs/getting-started.md)**：初始步骤<br>
→ **[工作流](docs/workflows.md)**：组合与模式<br>
→ **[命令](docs/commands.md)**：斜杠命令与技能（skills）<br>
→ **[命令行工具 (CLI)](docs/cli.md)**：终端参考手册<br>
→ **[支持的工具](docs/supported-tools.md)**：工具集成与安装路径<br>
→ **[核心概念](docs/concepts.md)**：整体架构解析<br>
→ **[多语言支持](docs/multi-language.md)**<br>
→ **[自定义配置](docs/customization.md)**：打造专属工作流


## 社区规范包

第三方规范包通过独立仓库分发——这些提供了预设的工作流，用于将 OpenSpec 与其他工具集成，类似于 [github/spec-kit 的社区扩展目录](https://github.com/github/spec-kit/tree/main/extensions) 处理工具集成的方式。

→ **在自定义文档中[浏览目录](docs/customization.md#community-schemas)**


## 为什么选择 OpenSpec？

AI 编程助手功能强大，但当需求仅存在于聊天记录中时，其输出往往不可预测。OpenSpec 引入了一个轻量级的规范层（spec layer），确保你在编写任何代码前就明确要构建什么。

- **先对齐再开发** —— 人类与 AI 在写代码前先对需求达成一致
- **保持条理清晰** —— 每次变更拥有独立文件夹，包含提案、规范、设计与任务清单
- **灵活协作** —— 随时更新任意制品（artifact），无需遵循僵化的阶段门禁
- **自由选用工具** —— 通过斜杠命令兼容 20+ 款 AI 助手

### 横向对比

**与 [Spec Kit](https://github.com/github/spec-kit)（GitHub）对比** —— 功能全面但较为臃肿。阶段门禁严格，依赖大量 Markdown 和 Python 环境配置。OpenSpec 更轻量，支持自由迭代。

**与 [Kiro](https://kiro.dev)（AWS）对比** —— 功能强大，但会绑定其专属 IDE 且仅支持 Claude 模型。OpenSpec 可无缝对接你已有的工具链。

**与“无规范”对比** —— 缺乏规范的 AI 编程意味着模糊的提示词和不可预测的结果。OpenSpec 在无需繁琐流程的前提下，带来可预期的产出。

## 更新 OpenSpec

**升级软件包**

```bash
npm install -g @fission-ai/openspec@latest
```

**刷新 Agent 指令**

在每个项目目录下运行此命令以重新生成 AI 引导说明，并确保最新的斜杠命令已生效：

```bash
openspec update
```

## 使用建议

**模型选择**：OpenSpec 在基于高推理能力（high-reasoning）的模型上表现最佳。我们推荐在规划与实现阶段均使用 Codex 5.5 和 Opus 4.7。

**上下文管理 (Context Hygiene)**：OpenSpec 需要干净的上下文窗口以获得最佳效果。开始实现前请清理上下文，并在整个会话期间保持良好的上下文管理规范。

## 参与贡献

**小型修复** —— 错误修复、错别字更正及微小改进可直接提交 PR。

**大型变更** —— 如需新增功能、重大重构或架构调整，请先提交 OpenSpec 变更提案，以便我们在实施前对齐目标与意图。

撰写提案时请牢记 OpenSpec 的核心理念：我们服务于使用不同编程 Agent、模型和用例的广泛用户群体。所有变更都应确保普适性。

**欢迎使用 AI 生成代码** —— 前提是必须经过测试与验证。包含 AI 生成代码的 PR 需注明所使用的编程 Agent 及模型（例如：“由 Claude Code 配合 claude-opus-4-5-20251101 生成”）。

### 开发指南

- 安装依赖：`pnpm install`
- 构建项目：`pnpm run build`
- 运行测试：`pnpm test`
- 本地调试 CLI：`pnpm run dev` 或 `pnpm run dev:cli`
- 遵循规范提交（单行格式）：`type(scope): subject`

## 其他说明

<details>
<summary><strong>遥测数据</strong></summary>

OpenSpec 会收集匿名的使用统计数据。

我们仅收集命令名称与版本号以了解使用模式。不采集参数、路径、内容或个人身份信息（PII）。在 CI 环境中默认自动禁用。

**退出选项：**设置环境变量 `OPENSPEC_TELEMETRY=0` 或 `DO_NOT_TRACK=1`

</details>

<details>
<summary><strong>维护者与顾问</strong></summary>

核心维护者及项目指导顾问名单详见 [MAINTAINERS.md](MAINTAINERS.md)。

</details>



## 开源协议

MIT