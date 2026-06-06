[![npm version](https://img.shields.io/npm/v/claude-code-templates.svg)](https://www.npmjs.com/package/claude-code-templates)
[![npm downloads](https://img.shields.io/npm/dt/claude-code-templates.svg)](https://www.npmjs.com/package/claude-code-templates)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Sponsored by Z.AI](https://img.shields.io/badge/Sponsored%20by-Z.AI-2563eb?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMiAyMkgyMkwxMiAyWiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+)](https://z.ai/subscribe?ic=8JVLJQFSKB&utm_source=github&utm_medium=badge&utm_campaign=readme)
[![Claude for Open Source](https://img.shields.io/badge/Claude-Open%20Source%20Program-D97757?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIzIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==)](https://claude.com/contact-sales/claude-for-oss)
[![Neon Open Source Program](https://img.shields.io/badge/Neon-Open%20Source%20Program-00E599?style=flat)](https://get.neon.com/4eCjZDz)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-yellow?style=flat&logo=buy-me-a-coffee)](https://buymeacoffee.com/daniavila)
[![GitHub stars](https://img.shields.io/github/stars/davila7/claude-code-templates.svg?style=social&label=Star)](https://github.com/davila7/claude-code-templates)

<p align="center">
  <a href="https://trendshift.io/repositories/15113" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15113" alt="davila7%2Fclaude-code-templates | Trendshift" style="width: 200px; height: 40px;" width="125" height="40"/>
  </a>
  <br />
  <br />
  <a href="https://vercel.com/oss">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge.svg" />
  </a>
  &nbsp;&nbsp;
  <a href="https://get.neon.com/4eCjZDz">
  <img alt="Neon Open Source Program" src="https://img.shields.io/badge/Neon-Open%20Source%20Program-00E599?style=for-the-badge" />
  </a>
  &nbsp;&nbsp;
  <a href="https://claude.com/contact-sales/claude-for-oss">
  <img alt="Claude for Open Source" src="docs/claude-oss-badge.svg" height="48" />
  </a>
</p>

---

> **🧪 新功能：Dashboard** — 前往 **[www.aitmpl.com](https://aitmpl.com)** 探索组件、管理集合库并跟踪安装状态。目前处于 Beta 阶段，欢迎提供反馈！

# Claude Code Templates ([aitmpl.com](https://aitmpl.com))

**Anthropic 旗下 Claude Code 的即用型配置。** 一套全面的 AI Agent（智能体）、自定义命令、设置、Hooks（钩子）、外部集成（MCP）及项目模板集合，旨在提升你的开发工作流。

## 浏览与安装组件和模板

**[浏览所有模板](https://aitmpl.com)** - 交互式网页界面，用于探索和安装 100 多个 Agent、命令、设置、Hooks 和 MCP。

<img width="1049" height="855" alt="Screenshot 2025-08-19 at 08 09 24" src="https://github.com/user-attachments/assets/e3617410-9b1c-4731-87b7-a3858800b737" />

## 🚀 快速安装

```bash
# Install a complete development stack
npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes

# Browse and install interactively
npx claude-code-templates@latest

# Install specific components
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --command performance/optimize-bundle --yes
npx claude-code-templates@latest --setting performance/mcp-timeouts --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

## 你将获得什么

| 组件类型 | 说明 | 示例 |
|-----------|-------------|----------|
| **🤖 Agents（智能体）** | 针对特定领域的 AI 专家 | 安全审计员、React 性能优化器、数据库架构师 |
| **⚡ Commands（命令）** | 自定义斜杠命令 | `/generate-tests`、`/optimize-bundle`、`/check-security` |
| **🔌 MCPs** | 外部服务集成 | GitHub、PostgreSQL、Stripe、AWS、OpenAI |
| **⚙️ Settings（设置）** | Claude Code 配置项 | 超时时间、内存设置、输出风格 |
| **🪝 Hooks（钩子）** | 自动化触发器 | Pre-commit 验证、任务完成后操作 |
| **🎨 Skills（技能）** | 支持渐进式展示的复用能力 | PDF 处理、Excel 自动化、自定义工作流 |

## 🛠️ 附加工具

除了模板目录，Claude Code Templates 还包含强大的开发工具：

### 📊 Claude Code Analytics
通过实时状态检测和性能指标，实时监控你的 AI 驱动开发会话。

```bash
npx claude-code-templates@latest --analytics
```

### 💬 Conversation Monitor  
移动端优化的界面，支持安全远程访问并实时查看 Claude 的响应。

```bash
# Local access
npx claude-code-templates@latest --chats

# Secure remote access via Cloudflare Tunnel
npx claude-code-templates@latest --chats --tunnel
```

### 🔍 Health Check
全面的诊断功能，确保你的 Claude Code 安装配置处于最佳状态。

```bash
npx claude-code-templates@latest --health-check
```

### 🔌 Plugin Dashboard
从统一界面查看应用市场、已安装的插件，并管理权限（permission）。

```bash
npx claude-code-templates@latest --plugins
```

## 📖 文档

**[📚 docs.aitmpl.com](https://docs.aitmpl.com/)** - 所有组件和工具的完整指南、示例及 API 参考。

## 贡献代码

我们欢迎任何形式的贡献！请先**[浏览现有模板](https://aitmpl.com)**了解当前内容，然后查阅我们的 [贡献指南](CONTRIBUTING.md)，添加你自己的 Agent、命令、MCP、设置或 Hooks。

**请在贡献前阅读我们的 [行为准则](CODE_OF_CONDUCT.md)。**

## 致谢与来源

本集合包含来自多个来源的组件：

**科学技能：**
- **[K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)** by K-Dense Inc. - MIT License（涵盖生物学、化学、医学和计算研究的 139 项科学技能）

**Anthropic 官方：**
- **[anthropics/skills](https://github.com/anthropics/skills)** - Official Anthropic skills（共 21 项）
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** - Development guides and examples（共 10 项技能）

**社区技能与 Agent：**
- **[obra/superpowers](https://github.com/obra/superpowers)** by Jesse Obra - MIT License（14 项工作流技能）
- **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** by Alireza Rezvani - MIT License（36 项专业角色技能）
- **[wshobson/agents](https://github.com/wshobson/agents)** by wshobson - MIT License（48 个 Agent）
- **NerdyChefsAI Skills** - Community contribution - MIT License（企业级专业技能）

**命令与工具：**
- **[awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** by hesreallyhim - CC0 1.0 Universal（21 个命令）
- **[awesome-claude-skills](https://github.com/mehdi-lamrani/awesome-claude-skills)** - Apache 2.0（社区技能）
- **move-code-quality-skill** - MIT License
- **cocoindex-claude** - Apache 2.0

所有这些资源均保留其**原始许可证和归属声明**，具体以各自作者的定义为准。
我们尊重并感谢所有原创者对 Claude 生态所做的工作与贡献。

## 📄 许可证

本项目采用 MIT 许可证开源——详见 [LICENSE](LICENSE) 文件。

## 🔗 链接

- **🌐 浏览模板**：[aitmpl.com](https://aitmpl.com)
- **📚 文档**：[docs.aitmpl.com](https://docs.aitmpl.com)
- **💬 社区讨论**：[GitHub Discussions](https://github.com/davila7/claude-code-templates/discussions)
- **🐛 问题反馈**：[GitHub Issues](https://github.com/davila7/claude-code-templates/issues)

## Star 趋势统计
[![Stargazers over time](https://starchart.cc/davila7/claude-code-templates.svg?variant=adaptive)](https://starchart.cc/davila7/claude-code-templates)

---

**⭐ 觉得有用？请给项目点个 Star 支持我们！**

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&slug=daniavila&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/daniavila)