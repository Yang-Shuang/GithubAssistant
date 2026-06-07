# Agent Skills（智能体技能）

[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/MKPE9g8aUy)

一种为 AI 智能体赋予新能力与专业知识的标准化方案。

## 什么是 Agent Skills？

Agent Skills 是一种轻量级、开放的标准格式，用于通过专业知识（specialized knowledge）和工作流来扩展 AI 智能体的能力。

其核心是一个包含 `SKILL.md` 文件的文件夹。该文件至少包含元数据（`name` 和 `description`）以及指示智能体如何执行特定任务的说明。技能还可以打包脚本、参考资料、模板和其他资源。

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## 为什么需要 Agent Skills？

智能体的能力日益增强，但通常缺乏可靠执行实际任务所需的上下文（context）。Agent Skills 通过将流程性知识和公司、团队及用户特定的上下文打包成可移植的、支持版本控制的文件夹来解决这一问题，智能体可按需加载这些文件夹。这为智能体提供了：

- **领域专业知识**：将专门知识——从法律审查流程到数据分析流水线再到演示文稿排版——捕获为可复用的指令和资源。
- **可重复的工作流**：将多步骤任务转化为一致且可审计的流程。
- **跨产品复用**：一次构建技能，即可在任何兼容该标准的智能体中使用。

## Agent Skills 如何工作？

智能体通过**渐进式加载（progressive disclosure）**机制分三个阶段加载技能：

1. **发现（Discovery）**：启动时，智能体仅加载每个可用技能的名称和描述，足以判断其是否相关即可。
2. **激活（Activation）**：当任务匹配某个技能的描述时，智能体会将完整的 `SKILL.md` 说明读取并加入上下文。
3. **执行（Execution）**：智能体按照指令操作，并根据需要选择性地执行打包的代码或加载引用的文件。

完整的说明仅在任务需要时才会加载，因此智能体可以保留大量技能，同时仅占用极小的上下文空间（context footprint）。

## 在哪里可以使用 Agent Skills？

众多 AI 工具和智能体客户端（agentic clients）均已支持 Agent Skills —— 请参阅 [Client Showcase](https://agentskills.io/clients) 探索部分示例！

## 快速入门

- **[Documentation](https://agentskills.io)** — 指南与教程
- **[Specification](https://agentskills.io/specification)** — 格式细节
- **[Example Skills](https://github.com/anthropics/skills)** — 探索更多可能性
- **[Discord](https://discord.gg/MKPE9g8aUy)** — 分享你的构建成果！

## 开放开发

Agent Skills 格式最初由 [Anthropic](https://www.anthropic.com/) 开发，现已作为开放标准发布，并被越来越多的智能体产品所采用。该标准向更广泛的生态系统开放贡献 —— 请参阅 [`CONTRIBUTING.md`](CONTRIBUTING.md) 了解如何参与。

## 许可证

本仓库中的代码采用 [Apache 2.0](LICENSE) 许可证授权。文档采用 [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) 许可证授权。详细信息请参阅各独立目录下的说明文件。