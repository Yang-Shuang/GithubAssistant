> **注意：** 本仓库包含 Anthropic 为 Claude 实现的 Skills 功能。关于 Agent Skills 标准的信息，请参阅 [agentskills.io](http://agentskills.io)。

[![skills.sh](https://skills.sh/b/anthropics/skills)](https://skills.sh/anthropics/skills)

# Skills
Skills 是由指令、脚本和资源组成的文件夹，Claude 会动态加载这些内容以提升其在特定任务上的表现。Skills 教会 Claude 以可重复的方式完成特定任务，例如按照贵公司的品牌指南创建文档、使用组织特定的工作流分析数据，或自动化处理个人任务。

如需更多信息，请查阅：
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# 关于本仓库

本仓库包含一系列 Skills，用于展示 Claude Skills 系统能够实现的功能。这些 Skills 涵盖了创意应用（艺术、音乐、设计）、技术任务（测试 Web 应用、MCP 服务器生成）以及企业工作流（通信、品牌管理等）。

每个 Skill 都独立存放在自己的文件夹中，并包含一个 `SKILL.md` 文件，其中含有 Claude 使用的指令和元数据。浏览这些 Skills 可以为你创建自己的 Skills 提供灵感，或帮助你了解不同的模式与方法。

本仓库中的许多 Skills 采用开源协议（Apache 2.0）。我们还在 [`skills/docx`](./skills/docx)、[`skills/pdf`](./skills/pdf)、[`skills/pptx`](./skills/pptx) 和 [`skills/xlsx`](./skills/xlsx) 子文件夹中包含了驱动 [Claude 的文档功能](https://www.anthropic.com/news/create-files) 底层能力的文档创建与编辑 Skills。这些属于源码可用（source-available）而非开源，但我们希望向开发者分享它们，作为在生产级 AI 应用中实际使用的复杂 Skills 的参考。

## 免责声明

**这些 Skills 仅用于演示和教育目的。** 虽然 Claude 中可能已提供部分此类功能，但你从 Claude 获取的实现和行为可能与这些 Skills 中展示的内容有所不同。这些 Skills 旨在说明各种模式与可能性。在依赖它们执行关键任务之前，请务必在你自己的环境中进行充分测试。

# 技能集 (Skill Sets)
- [./skills](./skills)：创意与设计、开发与技术支持、企业与通信以及文档类 Skills 示例
- [./spec](./spec)：Agent Skills 规范
- [./template](./template)：Skill 模板

# 在 Claude Code、Claude.ai 和 API 中试用

## Claude Code
你可以在 Claude Code 中运行以下命令，将此仓库注册为 Claude Code 插件市场：
```
/plugin marketplace add anthropics/skills
```

随后，安装特定的 Skills 集：
1. 选择 `Browse and install plugins`
2. 选择 `anthropic-agent-skills`
3. 选择 `document-skills` 或 `example-skills`
4. 选择 `Install now`

或者，通过以下方式直接安装任一插件：
```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

安装插件后，只需提及该 Skill 即可使用。例如，如果你从市场中安装了 `document-skills` 插件，可以要求 Claude Code 执行类似以下操作：“使用 PDF Skill 从 `path/to/some-file.pdf` 中提取表单字段”

## Claude.ai

这些示例 Skills 已对 Claude.ai 的付费计划用户开放。 

若要使用本仓库中的任意 Skill 或上传自定义 Skills，请遵循 [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b) 中的说明。

## Claude API

你可以通过 Claude API 使用 Anthropic 预构建的 Skills，并上传自定义 Skills。更多信息请参阅 [Skills API 快速入门](https://docs.claude.com/en/api/skills-guide#creating-a-skill)。

# 创建基础 Skill

创建 Skills 非常简单——只需一个包含 `SKILL.md` 文件（内含 YAML frontmatter 和指令）的文件夹。你可以使用本仓库中的 **template-skill** 作为起点：

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

frontmatter 仅需包含两个字段：
- `name` - 你 Skill 的唯一标识符（全小写，空格使用连字符）
- `description` - 该 Skill 的功能说明及使用场景

下方的 Markdown 内容包含 Claude 将遵循的指令、示例和指南。更多详情，请参阅 [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)。

# 合作伙伴 Skills

Skills 是教授 Claude 如何更好地使用特定软件的好方法。随着我们收到合作伙伴提供的出色示例 Skills，我们可能会在此处展示其中的一部分：

- **Notion** - [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)