<div align="center">

<img src="./assets/logo.svg" alt="OpenSkills" width="420" />

<br/>
<br/>

**面向 AI 编程代理的通用技能加载器**

一个 CLI。适配所有代理。格式与 Claude Code 一致。

[![npm version](https://img.shields.io/npm/v/openskills.svg)](https://www.npmjs.com/package/openskills)
[![npm downloads](https://img.shields.io/npm/dm/openskills.svg)](https://www.npmjs.com/package/openskills)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[快速开始](#-快速启动) · [工作原理](#-工作原理) · [命令](#-命令) · [创建技能](#-创建你自己的技能) · [常见问题](#-faq)

</div>

---

## ✨ 什么是 OpenSkills？

OpenSkills 将 **Anthropic 的技能系统** 带给每一位 AI 编程代理 —— Claude Code、Cursor、Windsurf、Aider、Codex，以及任何能够读取 `AGENTS.md` 的工具。

**把它看作 SKILL.md 的通用安装器。**

---

## 🚀 快速开始

```bash
npx openskills install anthropics/skills
npx openskills sync
```

默认情况下，安装为项目本地（`./.claude/skills`，或使用 `--universal` 时为 `./.agent/skills`）。如需全局安装到 `~/.claude/skills`，请使用 `--global`。

---

## ✅ 为什么选择 OpenSkills

- **与 Claude Code 完全兼容** —— 相同的 Prompt 格式、相同的 Marketplace（市场）、相同的文件夹结构
- **通用性** —— 适用于 Claude Code、Cursor、Windsurf、Aider、Codex 等更多代理
- **渐进式披露（Progressive Disclosure）** —— 仅在需要时加载技能，保持上下文整洁
- **仓库友好型** —— 技能文件位于你的项目中，支持版本控制
- **私有化友好** —— 支持从本地路径或私有 Git 仓库安装

---

## 🧠 工作原理

### Claude Code 系统提示词（技能）

Claude Code 以 **SKILL.md 文件** 的形式提供技能，并在 `<available_skills>` 代码块中暴露它们。当用户请求某项任务时，Claude 会动态加载匹配的技能。

```xml
<available_skills>
<skill>
<name>pdf</name>
<description>Comprehensive PDF manipulation toolkit for extracting text and tables...</description>
<location>plugin</location>
</skill>
</available_skills>
```

### OpenSkills：相同格式，通用加载器

OpenSkills 会在你的 `AGENTS.md` 中生成**完全相同的 `<available_skills>` XML**，并通过以下方式加载技能：

```bash
npx openskills read <skill-name>
```

因此，任何能够读取 `AGENTS.md` 的代理都可以直接使用 Claude Code 的技能，而无需依赖 Claude Code 本身。

### 对比一览

| 方面 | Claude Code | OpenSkills |
|--------|-------------|------------|
| **提示词格式** | `<available_skills>` XML | 相同的 XML | 
| **技能存储位置** | `.claude/skills/` | `.claude/skills/`（默认）| 
| **调用方式** | `Skill("name")` 工具 | `npx openskills read <name>` | 
| **市场/仓库** | Anthropic marketplace | GitHub (anthropics/skills) | 
| **渐进式披露** | ✅ | ✅ |

<details>
<summary><strong>Show the exact AGENTS.md format OpenSkills writes</strong></summary>

```xml
<skills_system priority="1">

## Available Skills

<!-- SKILLS_TABLE_START -->
<usage>
When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively.

How to use skills:
- Invoke: `npx openskills read <skill-name>` (run in your shell)
- The skill content will load with detailed instructions
- Base directory provided in output for resolving bundled resources

Usage notes:
- Only use skills listed in <available_skills> below
- Do not invoke a skill that is already loaded in your context
</usage>

<available_skills>

<skill>
<name>pdf</name>
<description>Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms...</description>
<location>project</location>
</skill>

</available_skills>
<!-- SKILLS_TABLE_END -->

</skills_system>
```

</details>

---

## 🔧 安装技能

### 从 Anthropic Marketplace（市场）

```bash
npx openskills install anthropics/skills
```

### 从任意 GitHub 仓库

```bash
npx openskills install your-org/your-skills
```

### 从本地路径

```bash
npx openskills install ./local-skills/my-skill
```

### 从私有 Git 仓库

```bash
npx openskills install git@github.com:your-org/private-skills.git
```

---

## 🌍 通用模式（多代理环境）

如果你同时使用 Claude Code **和**其他代理，并共用一个 `AGENTS.md`，请安装到 `.agent/skills/` 以避免与 Claude 的插件市场冲突：

```bash
npx openskills install anthropics/skills --universal
```

**优先级顺序（最高优先）：**
1. `./.agent/skills/`
2. `~/.agent/skills/`
3. `./.claude/skills/`
4. `~/.claude/skills/`

---

## 🧰 命令

```bash
npx openskills install <source> [options]  # Install from GitHub, local path, or private repo
npx openskills sync [-y] [-o <path>]       # Update AGENTS.md (or custom output)
npx openskills list                        # Show installed skills
npx openskills read <name>                 # Load skill (for agents)
npx openskills update [name...]            # Update installed skills (default: all)
npx openskills manage                      # Remove skills (interactive)
npx openskills remove <name>               # Remove specific skill
```

### 参数说明

- `--global` — Install globally to `~/.claude/skills` (default: project install)
- `--universal` — Install to `.agent/skills/` instead of `.claude/skills/`
- `-y, --yes` — Skip prompts (useful for CI)
- `-o, --output <path>` — Output file for sync (default: `AGENTS.md`)

---

## 🧬 SKILL.md 格式规范

OpenSkills 采用与 Anthropic 完全一致的格式：

```markdown
---
name: pdf
description: Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms.
---

# PDF Skill Instructions

When the user asks you to work with PDFs, follow these steps:
1. Install dependencies: `pip install pypdf2`
2. Extract text using scripts/extract_text.py
3. Use references/api-docs.md for details
```

技能会**按需加载**，从而保持你的代理上下文整洁且专注。

---

## 🧪 创建你自己的技能

### 最小结构

```
my-skill/
└── SKILL.md
```

### 包含资源文件

```
my-skill/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

安装你自定义的技能：

```bash
npx openskills install ./my-skill
```

### 使用软链接进行本地开发

```bash
git clone git@github.com:your-org/my-skills.git ~/dev/my-skills
mkdir -p .claude/skills
ln -s ~/dev/my-skills/my-skill .claude/skills/my-skill
```

### 编写指南

```bash
npx openskills install anthropics/skills
npx openskills read skill-creator
```

---

## 🔄 更新技能

如果你从 Git 仓库安装了技能，可以随时刷新它们：

```bash
npx openskills update
```

若要更新特定技能，请传入以逗号分隔的列表：

```bash
npx openskills update git-workflow,check-branch-first
```

如果某个技能是在版本追踪功能上线前安装的，只需重新安装一次即可记录其来源。

---

## ✅ 使用技巧

- 你始终可以通过 `npx` 直接运行 OpenSkills；全局安装为可选项。
- 如需读取多个技能，建议使用逗号分隔名称：`npx openskills read foo,bar`.

---

## ❓ 常见问题

### 为什么使用 CLI 而不是 MCP？

**MCP 用于动态工具。** 技能是静态指令与资源的集合。

- 技能只是普通文件 → 无需启动服务器
- 适配所有代理 → 无需依赖 MCP 支持
- 符合 Anthropic 的设计规范 → `SKILL.md` 即为官方标准

MCP 和技能解决的是不同层面的问题。OpenSkills 致力于让技能保持轻量且通用。

---

## 📋 环境要求

- **Node.js** 20.6+
- **Git** (for cloning repositories)

---

## 📜 许可证

Apache 2.0

## 说明

Implements [Anthropic's Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) specification.

**Not affiliated with Anthropic.** Claude, Claude Code, and Agent Skills are trademarks of Anthropic, PBC.