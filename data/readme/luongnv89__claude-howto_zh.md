<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.160-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **Language / Ngôn ngữ / 语言 / Мова:** [英语](README.md) | [越南语](vi/README.md) | [中文](zh/README.md) | [乌克兰语](uk/README.md) | [日语](ja/README.md)

# 周末精通 Claude Code

从输入 `claude` 开始，到编排 agent、hook、skill 和 MCP 服务器——通过可视化教程、即拷即用模板和引导式学习路径，全面掌握。

**[15分钟快速上手](#get-started-in-15-minutes)** | **[找到适合你的起点](#not-sure-where-to-start)** | **[浏览功能目录](CATALOG.md)**

---

## 目录

- [痛点所在](#the-problem)
- [本指南如何解决这些问题](#how-claude-how-to-fixes-this)
- [工作原理](#how-it-works)
- [不确定从哪里开始？](#not-sure-where-to-start)
- [15分钟快速上手](#get-started-in-15-minutes)
- [你能用它构建什么？](#what-can-you-build-with-this)
- [常见问题解答 (FAQ)](#faq)
- [贡献指南](#contributing)
- [许可证](#license)

---

## 痛点所在

你安装了 Claude Code。运行了几个 prompt 后，接下来该做什么？

- **官方文档只描述功能——却不教你如何组合它们。** 你知道存在斜杠命令（slash commands），但不知道如何将它们与 hook、记忆和子 agent 串联成真正能节省数小时的工作流。
- **缺乏清晰的学习路径。** 应该先学 MCP 还是 hook？先学 skill 还是 subagent？结果你 skim 了所有内容，却什么都没掌握。
- **示例过于基础。** 一个“hello world”斜杠命令无法帮你构建生产级的代码审查流水线——它需要利用记忆、委派给专业 agent，并自动运行安全扫描。

你只发挥了 Claude Code 10% 的能力——而你甚至不知道还有哪些能力未知。

---

## 本指南如何解决这些问题

这不仅仅是一份功能参考手册。它是一本**结构化、可视化、示例驱动的指导手册**，教你如何使用每个 Claude Code 功能，并提供今天即可复制到项目中的真实世界模板。

| | 官方文档 | 本指南 |
|--|---------------|------------|
| **格式** | 参考文档 | 带 Mermaid 图表的可视化教程 |
| **深度** | 功能描述 | 底层工作原理剖析 |
| **示例** | 基础代码片段 | 即拷即用、生产就绪的模板 |
| **结构** | 按功能分类 | 渐进式学习路径（入门到高级） |
| **上手引导** | 自学导向 | 带时间预估的引导式路线图 |
| **自我评估** | 无 | 交互式测验，帮你定位知识盲区并生成个性化路径 |

### 你将获得：

- **10个教程模块**覆盖所有 Claude Code 功能——从斜杠命令到自定义 agent 团队
- **即拷即用配置**——斜杠命令、CLAUDE.md 模板、hook 脚本、MCP 配置、subagent 定义和完整插件包
- **Mermaid 图表**展示每个功能的内部工作原理，让你理解 *为什么*，而不仅仅是 *怎么做*
- **引导式学习路径**带你从入门者进阶为高级用户（11-13小时）
- **内置自我评估**——直接在 Claude Code 中运行 `/self-assessment` 或 `/lesson-quiz hooks` 来定位知识盲区

**[开始学习路径  ->](LEARNING-ROADMAP.md)**

---

## 工作原理

### 1. 找到你的水平

参加 [自测问卷](LEARNING-ROADMAP.md#%E6%89%BE%E5%88%B0%E4%BD%A0%E7%9A%84%E6%B0%B4%E5%B9%B3) 或在 Claude Code 中运行 `/self-assessment`。根据你的现有知识生成个性化路线图。

### 2. 跟随引导路径

按顺序完成10个模块——每个模块都建立在前一个的基础上。学习时直接将模板复制到你的项目中。

### 3. 将功能组合成工作流

真正的威力在于功能的组合。学习如何将斜杠命令 + 记忆 + subagent + hook 连接成自动化流水线，用于处理代码审查、部署和文档生成。

### 4. 测试你的理解

在每个模块后运行 `/lesson-quiz [topic]`。测验会指出你遗漏的部分，让你快速补齐短板。

**[15分钟快速上手](#get-started-in-15-minutes)**

---

## 开发者信赖之选

- **GitHub Stars**：来自每天使用 Claude Code 的开发者
- **Forks**：来自将本指南适配到自己工作流的团队
- **持续维护**——与每次 Claude Code 发布同步（最新版本：v2.1.160，2026年6月）
- **社区驱动**——由分享真实世界配置的开发者共同贡献

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 不确定从哪里开始？

参加自测或选择你的水平：

| 级别 | 你可以... | 从这里开始 | 耗时 |
|-------|-----------|------------|------|
| **入门** | 启动 Claude Code 并对话 | [斜杠命令](01-slash-commands/) | ~2.5小时 |
| **进阶** | 使用 CLAUDE.md 和自定义命令 | [Skill](03-skills/) | ~3.5小时 |
| **高级** | 配置 MCP 服务器和 hook | [高级功能](09-advanced-features/) | ~5小时 |

**完整学习路径（含全部10个模块）：**

| 顺序 | 模块 | 级别 | 耗时 |
|-------|--------|-------|------|
| 1 | [斜杠命令](01-slash-commands/) | 入门 | 30分钟 |
| 2 | [记忆](02-memory/) | 入门+ | 45分钟 |
| 3 | [检查点](08-checkpoints/) | 进阶 | 45分钟 |
| 4 | [CLI基础](10-cli/) | 入门+ | 30分钟 |
| 5 | [Skill](03-skills/) | 进阶 | 1小时 |
| 6 | [Hook](06-hooks/) | 进阶 | 1小时 |
| 7 | [MCP](05-mcp/) | 进阶+ | 1小时 |
| 8 | [Subagent](04-subagents/) | 进阶+ | 1.5小时 |
| 9 | [高级功能](09-advanced-features/) | 高级 | 2-3小时 |
| 10 | [插件](07-plugins/) | 高级 | 2小时 |

**[完整学习路线图 ->](LEARNING-ROADMAP.md)**

---

## 15分钟快速上手

> **安装说明**：从 v2.1.113 开始，Claude Code 以原生跨平台二进制文件形式发布（macOS/Linux/Windows）。`npm install -g @anthropic-ai/claude-code` 仍然有效——首次使用时会下载原生二进制文件作为可选依赖。自 v2.1.116 起，下载地址为 `https://downloads.claude.ai/claude-code-releases`——企业代理必须将该域名加入白名单。

```bash
# 1. Clone the guide
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. Copy your first slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Try it — in Claude Code, type:
# /optimize

# 4. Ready for more? Set up project memory:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. Install a skill:
cp -r 03-skills/code-review-specialist ~/.claude/skills/
```

需要完整配置？这是**1小时核心设置**：

```bash
# Slash commands (15 min)
cp 01-slash-commands/*.md .claude/commands/

# Project memory (15 min)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Install a skill (15 min)
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Weekend goal: add hooks, subagents, MCP, and plugins
# Follow the learning path for guided setup
```

**[查看完整安装参考](#get-started-in-15-minutes)**

---

## 你能用它构建什么？

| 应用场景 | 组合功能 |
|----------|------------------------|
| **自动化代码审查** | 斜杠命令 + Subagent + 记忆 + MCP |
| **团队入职引导** | 记忆 + 斜杠命令 + 插件 |
| **CI/CD 自动化** | CLI参考 + Hook + 后台任务 |
| **文档生成** | Skill + Subagent + 插件 |
| **安全审计** | Subagent + Skill + Hook（只读模式） |
| **DevOps 流水线** | 插件 + MCP + Hook + 后台任务 |
| **复杂重构** | 检查点 + Planning Mode + Hook |

---

## 常见问题解答 (FAQ)

**这是免费的吗？**
是的。MIT 许可，永久免费。可用于个人项目、公司工作或团队内部——除保留许可证声明外无任何限制。

**会持续维护吗？**
会的。本指南与每次 Claude Code 发布同步更新。当前版本：v2.1.160（2026年6月），兼容 Claude Code 2.1+。

**这与官方文档有什么区别？**
官方文档是功能参考手册。本指南是带图表、生产就绪模板和渐进式学习路径的教程。两者互补——从这里开始学习，需要具体细节时查阅官方文档。

**学完所有内容需要多长时间？**
完整路径需 11-13小时。但你只需 15分钟就能获得即时收益——复制一个斜杠命令模板并试用即可。

**能与 Claude Sonnet / Haiku / Opus 配合使用吗？**
可以。所有模板均兼容 Claude Sonnet 4.6、Claude Opus 4.8 和 Claude Haiku 4.5。

**我可以贡献内容吗？**
当然。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 获取指南。我们欢迎新示例、错误修复、文档改进和社区模板。

**可以离线阅读吗？**
可以。运行 `uv run scripts/build_epub.py` 生成包含所有内容及渲染图表的 EPUB 电子书。

---

## 今日开始精通 Claude Code

你已经安装了 Claude Code。距离 10倍生产力提升的唯一障碍，就是知道如何正确使用它。本指南为你提供结构化路径、可视化讲解和即拷即用模板，助你快速上手。

MIT 许可。永久免费。克隆、Fork、打造属于你的版本。

**[开始学习路径 ->](LEARNING-ROADMAP.md)** | **[浏览功能目录](CATALOG.md)** | **[15分钟快速上手](#get-started-in-15-minutes)**

---

<details>
<summary>快速导航 — 全部功能</summary>

| 功能 | 描述 | 文件夹 |
|---------|-------------|--------|
| **功能目录** | 完整参考手册及安装命令 | [CATALOG.md](CATALOG.md) |
| **斜杠命令** | 用户手动调用的快捷方式 | [01-slash-commands/](01-slash-commands/) |
| **记忆** | 持久化上下文 | [02-memory/](02-memory/) |
| **Skill** | 可复用能力 | [03-skills/](03-skills/) |
| **Subagent** | 专业 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP 协议** | 外部工具访问 | [05-mcp/](05-mcp/) |
| **Hook** | 事件驱动自动化 | [06-hooks/](06-hooks/) |
| **插件** | 捆绑功能包 | [07-plugins/](07-plugins/) |
| **检查点** | 会话快照与回滚 | [08-checkpoints/](08-checkpoints/) |
| **高级功能** | Planning、思考、后台任务 | [09-advanced-features/](09-advanced-features/) |
| **CLI参考** | 命令、参数和选项 | [10-cli/](10-cli/) |
| **博客文章** | 真实世界使用示例 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 调用方式 | 持久性 | 最佳适用场景 |
|---------|-----------|------------|----------|
| **斜杠命令** | 手动 (`/cmd`) | 仅会话内 | 快捷操作 |
| **记忆** | 自动加载 | 跨会话 | 长期学习 |
| **Skill** | 自动触发 | 文件系统 | 自动化工作流 |
| **Subagent** | 自动委派 | 隔离上下文 | 任务分发 |
| **MCP 协议** | 自动查询 | 实时 | 动态数据访问 |
| **Hook** | 事件触发 | 已配置 | 自动化与验证 |
| **插件** | 单条命令 | 全功能覆盖 | 完整解决方案 |
| **检查点** | 手动/自动 | 基于会话 | 安全实验 |
| **Planning Mode** | 手动/自动 | 规划阶段 | 复杂实现 |
| **后台任务** | 手动 | 任务持续期 | 长时间运行操作 |
| **CLI参考** | 终端命令 | 会话/脚本 | 自动化与脚本编写 |

</details>

<details>
<summary>安装快速参考</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints (auto-enabled, configure in settings)
# See 08-checkpoints/README.md

# Advanced Features (configure in settings)
# See 09-advanced-features/config-examples.json

# CLI Reference (no installation needed)
# See 10-cli/README.md for usage examples
```

</details>

<details>
<summary>01. 斜杠命令</summary>

**位置**: [01-slash-commands/](01-slash-commands/)

**是什么**: 用户手动调用的快捷方式，以 Markdown 文件形式存储

**示例**:
- `optimize.md` - 代码优化分析
- `pr.md` - Pull Request 准备
- `generate-api-docs.md` - API 文档生成器

**安装**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**使用**:
```
/optimize
/pr
/generate-api-docs
```

**了解更多**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. 记忆</summary>

**位置**: [02-memory/](02-memory/)

**是什么**: 跨会话持久化上下文

**示例**:
- `project-CLAUDE.md` - 团队级项目规范
- `directory-api-CLAUDE.md` - 目录特定规则
- `personal-CLAUDE.md` - 个人偏好设置

**安装**:
```bash
# Project memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# Directory memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使用**: Claude 自动加载

</details>

<details>
<summary>03. Skill</summary>

**位置**: [03-skills/](03-skills/)

**是什么**: 可复用、自动调用的能力，附带指令和脚本

**示例**:
- `code-review-specialist/` - 包含脚本的综合代码审查
- `brand-voice/` - 品牌语调一致性检查器
- `doc-generator/` - API 文档生成器

**安装**:
```bash
# Personal skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review-specialist /path/to/project/.claude/skills/
```

**使用**: 相关时自动触发

</details>

<details>
<summary>04. Subagent</summary>

**位置**: [04-subagents/](04-subagents/)

**是什么**: 具有隔离上下文和自定义 prompt 的专业 AI 助手

**示例**:
- `code-reviewer.md` - 全面代码质量分析
- `test-engineer.md` - 测试策略与覆盖率
- `documentation-writer.md` - 技术文档编写
- `secure-reviewer.md` - 安全导向审查（只读）
- `implementation-agent.md` - 完整功能实现

**安装**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用**: 主 agent 自动委派

</details>

<details>
<summary>05. MCP 协议</summary>

**位置**: [05-mcp/](05-mcp/)

**是什么**: Model Context Protocol，用于访问外部工具和 API

**示例**:
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件操作
- `multi-mcp.json` - 多 MCP 服务器

**安装**:
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Add MCP server via CLI
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Or add to project .mcp.json manually (see 05-mcp/ for examples)
```

**使用**: 配置完成后，Claude 自动可用 MCP 工具

</details>

<details>
<summary>06. Hook</summary>

**位置**: [06-hooks/](06-hooks/)

**是什么**: 事件驱动的 Shell 命令，在响应 Claude Code 事件时自动执行

**示例**:
- `format-code.sh` - 写入前自动格式化代码
- `pre-commit.sh` - 提交前运行测试
- `security-scan.sh` - 扫描安全问题
- `log-bash.sh` - 记录所有 bash 命令
- `validate-prompt.sh` - 验证用户 prompt
- `notify-team.sh` - 事件发生时发送通知

**安装**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置 hook：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**使用**: Hook 在事件发生时自动执行

**Hook 类型**（5种，29个事件）：
- **Tool Hooks**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **Session Hooks**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **Task Hooks**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **Lifecycle Hooks**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. 插件</summary>

**位置**: [07-plugins/](07-plugins/)

**是什么**: 捆绑的命令、agent、MCP 和 hook 集合

**示例**:
- `pr-review/` - 完整 PR 审查工作流
- `devops-automation/` - 部署与监控
- `documentation/` - 文档生成

**安装**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**使用**: 使用捆绑的斜杠命令和功能

</details>

<details>
<summary>08. 检查点与回滚</summary>

**位置**: [08-checkpoints/](08-checkpoints/)

**是什么**: 保存会话状态并回滚到之前的节点，以探索不同方案

**核心概念**:
- **Checkpoint（检查点）**: 会话状态的快照
- **Rewind（回滚）**: 返回至先前的检查点
- **Branch Point（分支点）**: 从同一检查点探索多种方案

**使用**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose from five options:
# 1. Restore code and conversation
# 2. Restore conversation
# 3. Restore code
# 4. Summarize from here
# 5. Never mind
```

**使用场景**:
- 尝试不同的实现方案
- 从错误中恢复
- 安全实验
- 对比替代方案
- A/B 测试不同设计

</details>

<details>
<summary>09. 高级功能</summary>

**位置**: [09-advanced-features/](09-advanced-features/)

**是什么**: 用于复杂工作流和自动化的进阶能力

**包含**:
- **Planning Mode** — 编码前创建详细实施计划
- **Extended Thinking** — 针对复杂问题的深度推理（通过 `Alt+T` / `Option+T` 切换）
- **Background Tasks** — 运行长时间操作而不阻塞主线程
- **Permission Modes** — `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **Headless Mode** — 在 CI/CD 中运行 Claude Code：`claude -p "Run tests and generate report"`
- **Session Management** — `/resume`, `/rename`, `/fork`, `claude -c`, `claude -r`
- **Configuration** — 在 `~/.claude/settings.json` 中自定义行为

完整配置请参阅 [config-examples.json](09-advanced-features/config-examples.json)。

</details>

<details>
<summary>10. CLI参考</summary>

**位置**: [10-cli/](10-cli/)

**是什么**: Claude Code 完整的命令行界面参考手册

**快速示例**:
```bash
# Interactive mode
claude "explain this project"

# Print mode (non-interactive)
claude -p "review this code"

# Process file content
cat error.log | claude -p "explain this error"

# JSON output for scripts
claude -p --output-format json "list functions"

# Resume session
claude -r "feature-auth" "continue implementation"
```

**使用场景**: CI/CD 流水线集成、脚本自动化、批处理、多会话工作流、自定义 agent 配置

</details>

<details>
<summary>示例工作流</summary>

### 完整代码审查工作流

```markdown
# Uses: Slash Commands + Subagents + Memory + MCP

User: /review-pr

Claude:
1. Loads project memory (coding standards)
2. Fetches PR via GitHub MCP
3. Delegates to code-reviewer subagent
4. Delegates to test-engineer subagent
5. Synthesizes findings
6. Provides comprehensive review
```

### 自动化文档生成

```markdown
# Uses: Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Claude:
1. Loads project memory (doc standards)
2. Detects doc generation request
3. Auto-invokes doc-generator skill
4. Delegates to api-documenter subagent
5. Creates comprehensive docs with examples
```

### DevOps 部署

```markdown
# Uses: Plugins + MCP + Hooks

User: /deploy production

Claude:
1. Runs pre-deploy hook (validates environment)
2. Delegates to deployment-specialist subagent
3. Executes deployment via Kubernetes MCP
4. Monitors progress
5. Runs post-deploy hook (health checks)
6. Reports status
```

</details>

<details>
<summary>目录结构</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review-specialist/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>最佳实践</summary>

### ✅ 推荐做法
- 从简单的斜杠命令开始
- 逐步添加功能
- 使用记忆模块统一团队规范
- 先在本地测试配置
- 记录自定义实现逻辑
- 对项目配置进行版本控制
- 与团队共享插件

### ❌ 避免事项
- 不要创建重复功能
- 不要硬编码凭证
- 不要跳过文档编写
- 不要过度简化复杂任务
- 不要忽视安全最佳实践
- 不要提交敏感数据

</details>

<details>
<summary>故障排除</summary>

### 功能未加载
1. 检查文件位置与命名规范
2. 验证 YAML frontmatter 语法
3. 检查文件权限
4. 核对 Claude Code 版本兼容性

### MCP 连接失败
1. 验证环境变量配置
2. 检查 MCP server 安装状态
3. 测试凭证有效性
4. 排查网络连接问题

### Subagent 未委派
1. 检查工具调用权限
2. 验证 agent 描述是否清晰
3. 评估任务复杂度
4. 独立测试 agent 表现

</details>

<details>
<summary>测试</summary>

本项目包含全面的自动化测试：

- **单元测试**: 使用 pytest（Python 3.10, 3.11, 3.12）
- **代码质量**: Ruff 进行 linting 和格式化检查
- **安全扫描**: Bandit 漏洞检测
- **类型检查**: mypy 静态类型分析
- **构建验证**: EPUB 生成测试
- **覆盖率追踪**: Codecov 集成

```bash
# Install development dependencies
uv pip install -r requirements-dev.txt

# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage report
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run code quality checks
ruff check scripts/
ruff format --check scripts/

# Run security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# Run type checking
mypy scripts/ --ignore-missing-imports
```

测试会在每次推送到 `main`/`develop` 分支及提交 PR 到 `main` 时自动运行。详细信息请参阅 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 生成</summary>

想离线阅读本指南？生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

这将创建 `claude-howto-guide.epub`，包含所有内容及渲染后的 Mermaid 图表。

更多选项请参阅 [scripts/README.md](scripts/README.md)。

</details>

<details>
<summary>贡献指南</summary>

发现 bug 或想贡献示例？我们非常需要你的帮助！

**请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 获取详细指南，内容包括：**
- 贡献类型（示例、文档、功能、bug、反馈）
- 开发环境搭建步骤
- 目录结构与内容添加规范
- 写作指南与最佳实践
- Commit 和 PR 提交流程

**我们的社区准则：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 我们如何相互对待
- [SECURITY.md](SECURITY.md) - 安全政策与漏洞报告流程

### 报告安全问题

如果你发现安全漏洞，请负责任地报告：

1. **使用 GitHub 私有漏洞报告**: https://github.com/luongnv89/claude-howto/security/advisories
2. **或阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细操作指南
3. **切勿**为安全问题公开创建 issue

快速开始：
1. Fork 并克隆仓库
2. 创建描述性分支（`add/feature-name`, `fix/bug`, `docs/improvement`）
3. 按照指南进行修改
4. 提交附带清晰说明的 PR

**需要帮助？** 请创建 issue 或 discussion，我们将指导你完成流程。

</details>

<details>
<summary>附加资源</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 开箱即用的 skill 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 创作者分享的系统化工作流：并行 agent、共享 CLAUDE.md、Planning mode、斜杠命令、subagent 及用于自主长时运行的验证 hook。

</details>

---

## 贡献指南

我们欢迎贡献！请参阅我们的 [贡献指南](CONTRIBUTING.md) 了解如何开始。

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)。可免费使用、修改和分发。唯一要求是保留许可证声明。

---

**最后更新**: 2026年6月2日
**Claude Code 版本**: 2.1.160
**资料来源**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://github.com/anthropics/claude-code/releases
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
**兼容模型**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5