<!-- registry-sync: version=11.2.0; skills=1459; stars=37411; updated_at=2026-05-13T13:58:50+00:00 -->
# 🌌 Antigravity Awesome Skills：为 Claude Code、Gemini CLI、Cursor、Copilot 等提供的 1,459+ 智能体技能

> **可安装的 GitHub 库，包含适用于 Claude Code、Cursor、Codex CLI、Gemini CLI、Antigravity 及其他 AI 编程助手的 1,459+ 项智能体技能。**

Antigravity Awesome Skills 是一个可安装的 GitHub 库及 npm 安装器，用于复用 `SKILL.md` 操作手册。它专为 Claude Code、Cursor、Codex CLI、Gemini CLI、Antigravity、Kiro、OpenCode、GitHub Copilot 及其他受益于结构化操作指令的 AI 编程助手设计。与其收集一次性提示词片段，本仓库提供可搜索、可安装的技能目录、套件（Bundles）、工作流（Workflows）、插件安全分发版及实用文档，帮助智能体在更丰富的上下文、更强的约束和更清晰的输出中完成重复性任务。

你可以使用本仓库安装广泛的多工具技能库，从基于角色的套件开始入手，或直接进入用于规划、编码、调试、测试、安全审查、基础设施、产品工作和增长任务的流程驱动执行模式。根目录的 README 刻意作为高信息密度的落地页：了解项目是什么、快速安装、选择正确的工具路径，然后仅在需要时查阅更深入的文档。

**从这里开始：** [给仓库加星](https://github.com/sickn33/antigravity-awesome-skills/stargazers) · [1分钟安装](#installation) · [选择你的工具](#choose-your-tool) · [各工具最佳技能](#best-skills-by-tool) · [📚 浏览 1,459+ 项技能](#browse-1459-skills) · [套件 (Bundles)](docs/users/bundles.md) · [工作流 (Workflows)](docs/users/workflows.md) · [Claude Code 与 Codex 的插件](docs/users/plugins.md)

[![GitHub stars](https://img.shields.io/badge/⭐%2037%2C000%2B%20Stars-gold?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Latest Release](https://img.shields.io/github/v/release/sickn33/antigravity-awesome-skills?display_name=tag&style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/releases/latest)
[![Install with NPX](https://img.shields.io/badge/Install-npx%20antigravity--awesome--skills-black?style=for-the-badge&logo=npm)](#installation)
[![Kiro](https://img.shields.io/badge/Kiro-AWS-orange?style=for-the-badge)](https://kiro.dev)
[![Copilot](https://img.shields.io/badge/Copilot-GitHub-lightblue?style=for-the-badge)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray?style=for-the-badge)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-AI%20IDE-red?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills)

**当前版本：V11.2.0。** 受到超过 3.7 万位 GitHub 加星用户的信赖，本仓库结合了官方与社区技能集合、套件、工作流、安装路径及文档，助你快速从首次安装过渡到日常使用。

## 为什么选择本仓库

- **可安装而不仅是灵感参考**：运行 `npx antigravity-awesome-skills` 将技能放置在你的工具期望的位置。
- **专为主流智能体工作流打造**：适用于 Claude Code、Cursor、Codex CLI、Gemini CLI、Antigravity、Kiro、OpenCode、Copilot 等。
- **覆盖广泛且具备实际效用**：涵盖开发、测试、安全、基础设施、产品及营销领域的 1,459+ 项技能。
- **更快的上手速度**：套件和工作流缩短了从“发现本仓库”到“使用第一项技能”的时间。
- **无论追求广度还是精选都适用**：浏览完整目录、从顶级套件开始，或在安装前比较替代方案。

## 目录

- [为什么选择本仓库](#why-this-repo)
- [安装](#installation)
- [选择你的工具](#choose-your-tool)
- [快速问答 (FAQ)](#quick-faq)
- [各工具最佳技能](#best-skills-by-tool)
- [套件与工作流](#bundles--workflows)
- [浏览 1,459+ 项技能](#browse-1459-skills)
- [故障排除](#troubleshooting)
- [支持本项目](#support-the-project)
- [贡献指南](#contributing)
- [社区](#community)
- [归属与来源](#credits--sources)
- [仓库贡献者](#repo-contributors)
- [加星历史](#star-history)
- [许可证](#license)

## 安装

大多数用户应从完整库安装开始，然后使用套件或工作流来缩小尝试范围。

### 完整库安装

```bash
# Default: ~/.gemini/antigravity/skills (Antigravity global). Use --path for other locations.
npx antigravity-awesome-skills
```

npm 安装器默认使用浅克隆，因此首次运行的安装体积会比完整仓库历史检出更轻量。

### 验证安装

```bash
test -d ~/.gemini/antigravity/skills && echo "Skills installed in ~/.gemini/antigravity/skills"
```

### 运行你的第一项技能

```text
Use @brainstorming to plan a SaaS MVP.
```

### 更倾向于为 Claude Code 或 Codex 使用插件？

- 当你希望获得最广泛的目录并直接控制已安装的技能目录时，请使用完整库安装。
- 当你希望为 Claude Code 或 Codex 获取类似应用商店风格、插件安全分发版时，请走插件路线。
- 阅读 [Claude Code 与 Codex 的插件](docs/users/plugins.md) 以了解完整库安装、插件安装与套件插件的详细对比。

## 选择你的工具

使用同一个仓库，但按照你的宿主工具期望的方式进行安装或调用。

| Tool           | Install                                                                  | First Use                                              |
| -------------- | ------------------------------------------------------------------------ | ------------------------------------------------------ |
| Claude Code    | `npx antigravity-awesome-skills --claude` or Claude plugin marketplace | `>> /brainstorming help me plan a feature`           |
| Cursor         | `npx antigravity-awesome-skills --cursor`                              | `@brainstorming help me plan a feature`              |
| Gemini CLI     | `npx antigravity-awesome-skills --gemini`                              | `Use brainstorming to plan a feature`                |
| Codex CLI      | `npx antigravity-awesome-skills --codex`                               | `Use brainstorming to plan a feature`                |
| Antigravity    | `npx antigravity-awesome-skills --antigravity`                         | `Use @brainstorming to plan a feature`               |
| Kiro CLI       | `npx antigravity-awesome-skills --kiro`                                | `Use brainstorming to plan a feature`                |
| Kiro IDE       | `npx antigravity-awesome-skills --path ~/.kiro/skills`                 | `Use @brainstorming to plan a feature`               |
| GitHub Copilot | _No installer — paste skills or rules manually_                       | `Ask Copilot to use brainstorming to plan a feature` |
| OpenCode       | `npx antigravity-awesome-skills --path .agents/skills --category development,backend --risk safe,none` | `opencode run @brainstorming help me plan a feature` |
| AdaL CLI       | `npx antigravity-awesome-skills --path .adal/skills`                   | `Use brainstorming to plan a feature`                |
| Custom path    | `npx antigravity-awesome-skills --path ./my-skills`                    | Depends on your tool                                   |

如需按宿主工具划分的安装路径详情、提示词示例及设置注意事项，请访问：

- [Claude Code 技能](docs/users/claude-code-skills.md)
- [Cursor 技能](docs/users/cursor-skills.md)
- [Codex CLI 技能](docs/users/codex-cli-skills.md)
- [Gemini CLI 技能](docs/users/gemini-cli-skills.md)
- [AI 智能体技能指南](docs/users/ai-agent-skills.md)

## 快速问答 (FAQ)

### 什么是 Antigravity Awesome Skills？

它是适用于 Claude Code、Cursor、Codex CLI、Gemini CLI、Antigravity 及相关 AI 编程助手的可复用 `SKILL.md` 操作手册的可安装 GitHub 库。该仓库通过安装器 CLI、套件、工作流、生成的目录及文档将这些技能打包，助你快速从发现过渡到日常使用。

### 如何安装？

运行 `npx antigravity-awesome-skills` 进行默认的完整库安装；若希望安装器直接定位已知的技能目录，可使用特定工具的参数，如 `--codex`、`--cursor`、`--gemini`、`--claude` 或 `--antigravity`。

### 我应该使用完整库还是插件？

若希望获得最大的目录范围并直接控制文件系统，请使用完整库。若希望为 Claude Code 或 Codex 获取类似应用商店风格、插件安全分发版，请使用插件。完整说明位于 [Claude Code 与 Codex 的插件](docs/users/plugins.md)。

### 在哪里浏览套件、工作流和完整目录？

从[套件 (Bundles)](docs/users/bundles.md) 开始获取基于角色的推荐，查看[工作流 (Workflows)](docs/users/workflows.md) 获取有序执行手册，查阅 [CATALOG.md](CATALOG.md) 获取完整注册表，或访问托管的 [GitHub Pages 目录](https://sickn33.github.io/antigravity-awesome-skills/) 浏览 Web UI。

## 各工具最佳技能

若想获得比“浏览全部 1,459+ 项技能”更快的答案，请从特定工具的指南开始：

- **[Claude Code 技能](docs/users/claude-code-skills.md)**：安装路径、入门技能、提示词示例及插件应用商店流程。
- **[Cursor 技能](docs/users/cursor-skills.md)**：适用于 `.cursor/skills/` 的入门最佳技能、重度 UI 工作及结对编程流程。
- **[Codex CLI 技能](docs/users/codex-cli-skills.md)**：适用于本地编码循环的规划、实现、调试与审查技能。
- **[Gemini CLI 技能](docs/users/gemini-cli-skills.md)**：研究、智能体系统、集成及工程工作流的入门技术栈。
- **[AI 智能体技能指南](docs/users/ai-agent-skills.md)**：如何评估技能库、在广度与精选间取舍，以及选择正确的起点。

### 通用入门技能

- `@brainstorming`：用于实施前的规划。
- `@test-driven-development`：面向 TDD 的工作。
- `@debugging-strategies`：系统性故障排查。
- `@lint-and-validate`：轻量级质量检查。
- `@security-auditor`：安全导向的审查。
- `@frontend-design`：UI 与交互质量。
- `@api-design-principles`：API 结构与一致性。
- `@create-pr`：将工作打包为整洁的 Pull Request。

### 真实提示词示例

```text
Use @brainstorming to turn this product idea into a concrete MVP plan.
```

```text
Use @security-auditor to review this API endpoint for auth and validation risks.
```

## 套件与工作流

套件帮你选择从哪里开始，工作流帮你按正确顺序执行技能。

### 从套件开始

套件是针对特定角色或目标（如 `Web Wizard`、`Security Engineer` 或 `OSS Maintainer`）精心挑选的推荐技能组合。

- 套件仅为推荐，并非独立安装项。
- 只需安装一次仓库，然后使用 [docs/users/bundles.md](docs/users/bundles.md) 选择起始组合。
- 优秀的入门组合：
  - SaaS MVP：`Essentials` + `Full-Stack Developer` + `QA & Testing`
  - 生产环境加固：`Security Developer` + `DevOps & Cloud` + `Observability & Monitoring`
  - OSS 发布：`Essentials` + `OSS Maintainer`

### 使用工作流进行结果驱动的执行

- 阅读 [docs/users/workflows.md](docs/users/workflows.md) 获取人类可读的操作手册。
- 使用 [data/workflows.json](data/workflows.json) 获取机器可读的工作流元数据。
- 初始工作流包括发布 SaaS MVP、安全审计、AI 智能体系统、QA/浏览器自动化及 DDD 导向的设计工作。

### 运行时需要的活跃技能较少？

如果 Antigravity 因活跃技能过多而触及上下文限制，[docs/users/agent-overload-recovery.md](docs/users/agent-overload-recovery.md) 中的激活指南可仅将你所需的套件或技能 ID 生成到活跃的 Antigravity 目录中。

如果你使用 OpenCode 或其他 `.agents/skills` 宿主，建议一开始就采用精简安装，而不是将整个库复制到上下文敏感的运行时环境中。安装器现已支持 `--risk`、`--category` 和 `--tags` 参数，以便你将已安装的集合保持精简。

## 浏览 1,459+ 项技能

将根仓库作为落地页使用，然后跳转到与你意图匹配的更深层内容。

### 本仓库提供什么

- **技能库**位于 [`skills/`](skills/)
- **安装器 CLI** 由 [`package.json`](package.json) 中的 npm 包驱动
- **生成的目录与元数据**位于 [`CATALOG.md`](CATALOG.md)、`skills_index.json` 和 [`data/`](data/)
- **托管版与本地 Web 应用**位于 [`apps/web-app`](apps/web-app) 及 [GitHub Pages](https://sickn33.github.io/antigravity-awesome-skills/)
- **基于角色的套件**位于 [docs/users/bundles.md](docs/users/bundles.md)
- **执行工作流**位于 [docs/users/workflows.md](docs/users/workflows.md)
- **用户、贡献者与维护者文档**位于 [`docs/`](docs/) 下

### 最佳探索方式

- 在 [`CATALOG.md`](CATALOG.md) 中阅读完整目录。
- 浏览托管版目录：[https://sickn33.github.io/antigravity-awesome-skills/](https://sickn33.github.io/antigravity-awesome-skills/)。
- 如果你是安装后的新用户，请从 [Getting Started](docs/users/getting-started.md) 和 [Usage](docs/users/usage.md) 开始。
- 使用 [Bundles](docs/users/bundles.md) 进行基于角色的发现，使用 [Workflows](docs/users/workflows.md) 进行逐步执行。
- 若关注应用商店安全分发，请使用 [Plugins for Claude Code and Codex](docs/users/plugins.md)。

### 对比替代方案

- **[Antigravity Awesome Skills vs Awesome Claude Skills](docs/users/antigravity-awesome-skills-vs-awesome-claude-skills.md)**：了解广度覆盖与精选列表的权衡。
- **[Best Claude Code skills on GitHub](docs/users/best-claude-code-skills-github.md)**：高意图短名单。
- **[Best Cursor skills on GitHub](docs/users/best-cursor-skills-github.md)**：Cursor 兼容选项及选择标准。

## 故障排除

保持根目录 README 简洁；恢复指南和平台特定说明请使用专用文档。

- 安装后感到困惑，请从[使用指南 (Usage Guide)](docs/users/usage.md) 开始。
- Windows 截断或上下文崩溃循环问题，请参阅 [docs/users/windows-truncation-recovery.md](docs/users/windows-truncation-recovery.md)。
- Linux/macOS 过载或选择性激活问题，请参阅 [docs/users/agent-overload-recovery.md](docs/users/agent-overload-recovery.md)。
- OpenCode 或其他 `.agents/skills` 安装，建议采用精简安装，例如 `npx antigravity-awesome-skills --path .agents/skills --category development,backend --risk safe,none`。
- 插件安装详情、宿主兼容性及应用商店安全分发，请参阅 [docs/users/plugins.md](docs/users/plugins.md)。
- 贡献者期望与规范，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)、[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) 和 [`SECURITY.md`](SECURITY.md)。

## 支持本项目

支持是可选的。该项目对所有人保持免费和开源。

- [在 Buy Me a Coffee 赞助我](https://buymeacoffee.com/sickn33)
- 给仓库加星
- 提交可复现的 Issue
- 贡献文档、修复与技能

---

## 贡献指南

- 在 `skills/<skill-name>/SKILL.md` 下添加新技能。
- 遵循 [`CONTRIBUTING.md`](CONTRIBUTING.md) 中的贡献者指南。
- 使用 [`docs/contributors/skill-template.md`](docs/contributors/skill-template.md) 中的模板。
- 提交 PR 前运行 `npm run validate` 进行验证。
- 保持社区 PR 仅包含源码：不要提交生成的注册表工件，如 `CATALOG.md`、`skills_index.json` 或 `data/*.json`。
- 若你的 PR 修改了 `SKILL.md`，除常规验证和安全扫描外，还需通过 GitHub 上自动化的 `skill-review` 检查。
- 若你的 PR 涉及技能或高风险指导内容，即使自动化检查全部通过，仍需人工逻辑审查。

## 社区

- [Discussions](https://github.com/sickn33/antigravity-awesome-skills/discussions)：用于提问、分享想法、展示作品及获取社区反馈。
- [Issues](https://github.com/sickn33/antigravity-awesome-skills/issues)：用于提交可复现的 Bug 和具体、可执行的改进请求。
- [在 X (原 Twitter) 上关注 @sickn33](https://x.com/sickn33)：获取项目更新与发布通知。
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)：社区期望与管理标准。
- [`SECURITY.md`](SECURITY.md)：安全漏洞报告流程。

## 归属与来源

我们站在巨人的肩膀上。

👉 **[查看完整归属清单](docs/sources/sources.md)**

主要贡献者与来源包括：

- **HackTricks**
- **OWASP**
- **Anthropic / OpenAI / Google**
- **开源社区**

本合集离不开 Claude Code 社区及官方来源的卓越工作：

### 官方来源

- **[anthropics/skills](https://github.com/anthropics/skills)**：Anthropic 官方技能库 - 文档操作（DOCX、PDF、PPTX、XLSX）、品牌指南、内部通信。
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)**：使用 Claude 构建的官方笔记本与配方。
- **[remotion-dev/skills](https://github.com/remotion-dev/skills)**：Remotion 官方技能 - React 视频创作，含 28 个模块化规则。
- **[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)**：Vercel Labs 官方技能 - React 最佳实践、Web 设计规范。
- **[openai/skills](https://github.com/openai/skills)**：OpenAI Codex 技能目录 - 智能体技能、技能创建器、简洁规划。
- **[supabase/agent-skills](https://github.com/supabase/agent-skills)**：Supabase 官方技能 - Postgres 最佳实践。
- **[microsoft/skills](https://github.com/microsoft/skills)**：Microsoft 官方技能 - Azure 云服务、Bot Framework、认知服务，以及 .NET、Python、TypeScript、Go、Rust、Java 的企业级开发模式。
- **[MiniMax-AI/cli](https://github.com/MiniMax-AI/cli)**：MiniMax 官方 CLI - MiniMax 模型与 API 的文本、图像、视频、语音、音乐、视觉及网页搜索工作流。
- **[google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills)**：Gemini 官方技能 - Gemini API、SDK 及模型交互。
- **[apify/agent-skills](https://github.com/apify/agent-skills)**：Apify 官方技能 - 网页抓取、数据提取与自动化。
- **[BuyWhere/buywhere-mcp](https://github.com/BuyWhere/buywhere-mcp)**：BuyWhere 官方 MCP 服务器 — 通过 Model Context Protocol 搜索并比较来自新加坡、东南亚及美国市场的商品。
- **[expo/skills](https://github.com/expo/skills)**：Expo 官方技能 - Expo 项目工作流与 Expo Application Services 指南。
- **[huggingface/skills](https://github.com/huggingface/skills)**：Hugging Face 官方技能 - 模型、Spaces、数据集、推理及更广泛的 Hugging Face 生态系统工作流。
- **[neondatabase/agent-skills](https://github.com/neondatabase/agent-skills)**：Neon 官方技能 - Serverless Postgres 工作流与 Neon 平台指南。
- **[Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)**：Skyvern 官方浏览器自动化技能 — 利用 Vision LLMs 和计算机视觉实现 AI 驱动的浏览器控制，用于导航网站、填写表单及提取结构化数据。
- **[scopeblind/scopeblind-gateway](https://github.com/scopeblind/scopeblind-gateway)**：Scopeblind 官方 MCP 治理工具包 - Cedar 策略编写、影子到强制的发布流程，以及智能体工具调用的签名回执验证指南。

### 社区贡献者

- **[adelaidasofia/ai-brain-starter](https://github.com/adelaidasofia/ai-brain-starter)**：`ingest-youtube` 技能源码 - 使用 yt-dlp 元数据、VTT 清理及 capture-seed 存根将 YouTube 转录稿导入 markdown vault（MIT）。
- **[ejentum/ejentum-mcp](https://github.com/ejentum/ejentum-mcp)**：`ejentum-reasoning-harness` 技能源码 - MCP 认知驾驭模式，用于推理、代码审查、反欺骗检查及记忆漂移分析（MIT）。
- **[luoyuctl/agenttrace](https://github.com/luoyuctl/agenttrace)**：`agenttrace-session-audit` 技能源码 - 本地 AI 编程智能体会话审计，检测成本激增、工具故障、延迟差距、异常、健康门限及会话差异（MIT）。
- **[aomi-labs/skills](https://github.com/aomi-labs/skills)**：`aomi-transact` 技能源码 — Aomi CLI 的自然语言驱动，采用账户抽象优先执行模式，并在 25+ DeFi 应用中实现模拟后签名（MIT）。
- **[rich-elicitation](https://github.com/CyberZenithX/Rich-Elicitation-Skill)**：`rich-elicitation` 技能源码 - 在启动模糊任务前进行多轮澄清提问。
- **[CodeShuX/mockhunter](https://github.com/CodeShuX/mockhunter)**：`mock-hunter` 技能源码 - 基于 Playwright 的实时页面审计，将可见值分类为真实、模拟、LLM 生成、硬编码、损坏或未知（MIT）。
- **[commitshow/production-audit](https://github.com/commitshow/production-audit)**：`production-audit` 技能源码 - 发布应用就绪性审计，涵盖部署健康度、RLS、Webhooks、密钥暴露、权限授权、Stripe 幂等性及移动端 UX。
- **[MohamedAbdallah-14/unslop](https://github.com/MohamedAbdallah-14/unslop)**：`unslop` 技能源码 - CLI 及智能体工具工作流中 AI 生成文本的确定性清理与 LLM 辅助清理（MIT）。
- **[monte-carlo-data/mc-agent-toolkit](https://github.com/monte-carlo-data/mc-agent-toolkit)**：Monte Carlo 数据可观测性技能 — 表健康检查、变更影响评估、监控创建、推送摄入及 dbt 变更的 SQL 验证笔记本。
- **[openclaw/skills](https://github.com/openclaw/skills)**：`daily-gift` 技能源码 - 关系感知的创意礼物生成，含编辑判断、概念选择及多格式渲染。
- **[umutbozdag/agent-skills-manager](https://github.com/umutbozdag/agent-skills-manager)**：`manage-skills` 技能源码 - 跨主流智能体编程工具的技能发现、创建、编辑、切换、复制、移动与删除工作流。
- **[pumanitro/global-chat](https://github.com/pumanitro/global-chat)**：Global Chat Agent Discovery 技能源码 - 跨多个注册表发现 MCP 服务器和 AI 智能体的跨协议能力。
- **[bitjaru/styleseed](https://github.com/bitjaru/styleseed)**：StyleSeed Toss UI/UX 技能合集 - 专业移动端优先 UI 的设置向导、页面与模式生成、设计令牌管理、无障碍审查、UX 审计、反馈状态及微文案指南。
- **[milkomida77/guardian-agent-prompts](https://github.com/milkomida77/guardian-agent-prompts)**：Multi-Agent Task Orchestrator 技能源码 - 经过生产验证的委派模式、防重复机制及协同智能体工作的质量门控。
- **[Elkidogz/technical-change-skill](https://github.com/Elkidogz/technical-change-skill)**：Technical Change Tracker 技能源码 - 结构化 JSON 变更记录、会话交接及可访问 HTML 仪表盘，保障编码连续性。
- **[rmyndharis/antigravity-skills](https://github.com/rmyndharis/antegravity-skills)**：贡献了 300+ 企业级技能及目录生成逻辑。
- **[amartelr/antigravity-workspace-manager](https://github.com/amartelr/antigravity-workspace-manager)**：Workspace Manager CLI，用于在本地开发环境中动态自动预配子集技能。
- **[obra/superpowers](https://github.com/obra/superpowers)**：Jesse Vincent 的原始“Superpowers”。
- **[guanyang/antigravity-skills](https://github.com/guanyang/antigravity-skills)**：Antigravity 核心扩展。
- **[diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase)**：基础设施与后端/前端规范。
- **[ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase)**：React UI 模式与设计系统。
- **[travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)**：Loki Mode 与 Playwright 集成。
- **[Dimillian/Skills](https://github.com/Dimillian/Skills)**：聚焦 Apple 平台、GitHub 工作流、重构及性能的精选 Codex 技能（MIT）。
- **[zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide)**：综合安全套件与指南（~60 项新技能的来源）。
- **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)**：高级工程与产品管理工具包。
- **[karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills)**：Claude Code 的庞大已验证技能列表。
- **[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)**：精选 1000+ 官方与社区智能体技能，来自领先开发团队（MIT）。
- **[zircote/.claude](https://github.com/zircote/.claude)**：已归档的 Claude Code dotfiles/config 仓库，含 Shopify 开发技能参考。
- **[vibeforge1111/vibeship-spawner-skills](https://github.com/vibeforge1111/vibeship-spawner-skills)**：AI 智能体、集成、Maker 工具及其他生产级技能包。
- **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**：CRO、文案撰写、SEO、付费广告及增长营销技能（23 项，MIT）。
- **[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)**：SEO 工作流合集，涵盖技术 SEO、hreflang、站点地图、地理位置、Schema 及程序化 SEO 模式。
- **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**：前端设计品味技能合集，涵盖高级 UI 生成、重设计审计、GSAP 动效、Stitch 设计系统、极简与粗野主义视觉模式及全输出强制。
- **[mrprewsh/seo-aeo-engine](https://github.com/mrprewsh/seo-aeo-engine)**：SEO/AEO 内容增长系统，涵盖关键词研究、内容聚类、落地页、博客结构、Schema、内链及审计工作流。
- **[jonathimer/devmarketing-skills](https://github.com/jonathimer/devmarketing-skills)**：开发者营销技能 — HN 策略、技术教程、文档即营销、Reddit 互动、开发者入职等（33 项，MIT）。
- **[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)**：聚焦 Obsidian 的技能，涵盖 Markdown、Bases、JSON Canvas、CLI 工作流及内容清理。
- **[lewiswigmore/agent-skills](https://github.com/lewiswigmore/agent-skills)**：`vscode-extension-guide-en` 技能源码 - VS Code 扩展开发流程、打包、Marketplace 发布、TreeView 及 Webview 模式。
- **[Silverov/yandex-direct-skill](https://github.com/Silverov/yandex-direct-skill)**：Yandex Direct (API v5) 广告审计技能 — 55 项自动检查、A-F 评分，针对俄罗斯 PPC 市场的活动/广告/关键词分析（MIT）。
- **[vudovn/antigravity-kit](https://github.com/vudovn/antigravity-kit)**：含技能、智能体与工作流的 AI 智能体模板（33 项，MIT）。
- **[affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)**：Anthropic 黑客马拉松冠军的大型 Claude Code 配置与合集（MIT）。
- **[whatiskadudoing/fp-ts-skills](https://github.com/whatiskadudoing/fp-ts-skills)**：TypeScript 实用 fp-ts 技能 – fp-ts-pragmatic, fp-ts-react, fp-ts-errors (v4.4.0)。
- **[warmskull/idea-darwin](https://github.com/warmskull/idea-darwin)**：达尔文式创意演化工作流，用于结构化构思轮次、突变、杂交、批判及谱系追踪。
- **[Slashworks-biz/idea-os](https://github.com/Slashworks-biz/idea-os)**：`idea-os` 技能源码 - 五阶段管道（分诊 -> 澄清 -> 研究 -> PRD -> 规划），将原始创意转化为可构建的 PRD 与执行计划。
- **[webzler/agentMemory](https://github.com/webzler/agentMemory)**：agent-memory-mcp 技能源码。
- **[rafsilva85/credit-optimizer-v5](https://github.com/rafsilva85/credit-optimizer-v5)**：Manus AI 积分优化技能 — 智能模型路由、上下文压缩及智能测试。零质量损失下节省 30-75% 积分，经 53 个场景审计验证。
- **[Wittlesus/cursorrules-pro](https://github.com/Wittlesus/cursorrules-pro)**：8 种框架的专业 .cursorrules 配置 - Next.js、React、Python、Go、Rust 等。兼容 Cursor、Claude Code 与 Windsurf。
- **[nedcodes-ok/rule-porter](https://github.com/nedcodes-ok/rule-porter)**：Cursor (.mdc)、Claude Code (CLAUDE.md)、GitHub Copilot、Windsurf 及遗留 .cursorrules 格式间的双向规则转换器。零依赖。
- **[SSOJet/skills](https://github.com/ssojet/skills)**：面向流行框架与平台的 SSOJet 生产级技能与集成指南 — Node.js、Next.js、React、Java、.NET Core、Go、iOS、Android 等。无缝兼容 SSOJet SAML、OIDC 及企业单点登录流程。兼容 Cursor、Antigravity、Claude Code 与 Windsurf。
- **[MojoAuth/skills](https://github.com/MojoAuth/skills)**：面向 Node.js、Next.js、React、Java、.NET Core、Go、iOS 和 Android 等流行框架的 MojoAuth 生产级指南与示例。
- **[Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper)**：X (Twitter) 数据平台 — 推文搜索、用户查询、粉丝提取、互动指标、抽奖活动、监控、Webhooks、19 项提取工具及 MCP 服务器。
- **[connerlambden/helium-mcp](https://github.com/connerlambden/helium-mcp)**：`helium-mcp` 技能源码 — 新闻情报、媒体偏见分析、市场数据、期权定价及语义模因搜索的 MCP 服务器。
- **[shmlkv/dna-claude-analysis](https://github.com/shmlkv/dna-claude-analysis)**：个人基因组分析工具包 - Python 脚本，按 17 个类别（健康风险、族源、药物基因组学、营养、心理学等）分析原始 DNA 数据，并提供终端风格单页 HTML 可视化。
- **[AlmogBaku/debug-skill](https://github.com/AlmogBaku/debug-skill)**：AI 智能体交互式调试技能 — 通过 `dap` CLI 实现断点、步进、变量检查及堆栈追踪。支持 Python、Go、Node.js/TypeScript、Rust 和 C/C++。
- **[aptratcn/skill-audit](https://github.com/aptratcn/skill-audit)**：安装前安全审计技能，用于在安装前检测恶意、过度授权或可疑的第三方智能体技能（MIT）。
- **[uberSKILLS](https://github.com/uberskillsdev/uberSKILLS)**：通过可视化 AI 辅助工作流设计、测试和部署 Claude Code 智能体技能。
- **[christopherlhammer11-ai/tool-use-guardian](https://github.com/christopherlhammer11-ai/tool-use-guardian)**：Tool Use Guardian 技能源码 — 带重试、恢复及故障分类的工具调用可靠性包装器。
- **[christopherlhammer11-ai/recallmax](https://github.com/christopherlhammer11-ai/recallmax)**：RecallMax 技能源码 - 面向智能体的长上下文记忆、摘要与对话压缩。
- **[tsilverberg/webapp-uat](https://github.com/tsilverberg/webapp-uat)**：完整浏览器 UAT 技能 — Playwright 测试含控制台/网络错误捕获、WCAG 2.2 AA 无障碍检查、i18n 验证、响应式测试及 P0-P3 Bug 分诊。默认只读，兼容 React、Vue、Angular、Ionic、Next.js。
- **[Wolfe-Jam/faf-skills](https://github.com/Wolfe-Jam/faf-skills)**：AI 上下文与项目 DNA 技能 — .faf 格式管理、AI 就绪度评分、双向同步、MCP 服务器构建及冠军级测试（17 项，MIT）。
- **[fullstackcrew-alpha/privacy-mask](https://github.com/fullstackcrew-alpha/privacy-mask)**：面向 AI 编程助手的本地图像隐私掩码。通过 OCR + 47 条正则规则检测并遮蔽截图中的 PII、API 密钥及密钥。Claude Code Hook 集成实现自动掩码。支持 Tesseract 和 RapidOCR。100% 离线（MIT）。
- **[AvdLee/SwiftUI-Agent-Skill](https://github.com/AvdLee/SwiftUI-Agent-Skill)**：面向智能体工作流的 SwiftUI 最佳实践技能（MIT）。
- **[CloudAI-X/threejs-skills](https://github.com/CloudAI-X/threejs-skills)**：聚焦 Three.js 的技能合集，用于 AI 辅助的 3D Web 开发。
- **[K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)**：科学、研究、工程、金融及写作技能套件（MIT）。
- **[NotMyself/claude-win11-speckit-update-skill](https://github.com/NotMyself/claude-win11-speckit-update-skill)**：Claude Code 的归档 Speckit 更新技能（MIT）。
- **[SHADOWPR0/beautiful_prose](https://github.com/SHADOWPR0/beautiful_prose)**：提升文本质量并减少通用输出的写作技能。
- **[SHADOWPR0/security-bluebook-builder](https://github.com/SHADOWPR0/security-bluebook-builder)**：面向智能体工作流的安全文档/蓝皮书构建技能。
- **[SeanZoR/claude-speed-reader](https://github.com/SeanZoR/claude-speed-reader)**：RSVP 风格 Claude 响应速读助手（MIT）。
- **[Shpigford/skills](https://github.com/Shpigford/skills)**：面向常见开发任务的通用智能体技能（MIT）。
- **[ZhangHanDong/makepad-skills](https://github.com/ZhangHanDong/makepad-skills)**：Makepad 应用开发技能与参考（MIT）。
- **[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills)**：面向 Claude Code 的 n8n 工作流构建技能（MIT）。
- **[frmoretto/clarity-gate](https://github.com/frmoreto/clarity-gate)**：标记不确定性并减少 LLM 文档中幻觉确定性的验证协议。
- **[fruitwyatt/puzzle-activity-planner](https://github.com/fruitwyatt/puzzle-activity-planner)**：面向课堂、派对及活动的拼图活动规划技能，含生成器链接工作流。
- **[gokapso/agent-skills](https://github.com/gokapso/agent-skills)**：Kapso/WhatsApp 导向的智能体技能。
- **[huifer/WellAlly-health](https://github.com/huifer/WellAlly-health)**：医疗助手项目，在发布历史中被引用为健康类智能体能力的来源（MIT）。
- **[hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint)**：基于经典软件工程书籍的 AI 代码审查技能，用于设计异味、耦合及架构审查。
- **[hyhmrright/logic-lens](https://github.com/hyhmrright/logic-lens)**：面向 Bug、竞态条件、安全风险及 API 契约问题的形式逻辑检查 AI 代码审查技能。
- **[ibelick/ui-skills](https://github.com/ibelick/ui-skills)**：提升智能体构建界面的 UI 打磨技能（MIT）。
- **[jackjin1997/ClawForge](https://github.com/jackjin1997/ClawForge)**：OpenClaw 的技能、MCP 服务器及智能体工具资源库。
- **[jthack/ffuf_claude_skill](https://github.com/jthack/ffuf_claude_skill)**：Claude 中 Web Fuzzing 工作流的 FFUF 技能。
- **[kubestellar/console](https://github.com/kubestellar/console)**：KubeStellar Console 多集群 Kubernetes 仪表盘，含 `kc-agent` MCP 集成、AI 辅助操作及内置智能体技能。
- **[MetcalfSolutions/Satori](https://github.com/MetcalfSolutions/Satori)**：临床智慧指南伴侣，融合心理学框架与智慧传统，提供结构化反思伙伴。
- **[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)**：上下文工程、多智能体及生产级智能体系统技能合集（MIT）。
- **[robzolkos/skill-rails-upgrade](https://github.com/robzolkos/skill-rails-upgrade)**：面向 AI 辅助迁移的 Rails 升级技能。
- **[sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills)**：Apache 许可的 AI 编程助手智能体技能合集。
- **[scarletkc/vexor](https://github.com/scarletkc/vexor)**：文件与代码语义搜索引擎，在发布历史中被引用。
- **[sstklen/infinite-gratitude](https://github.com/sstklen/infinite-gratitude)**：AI Dojo 系列的多智能体研究技能（MIT）。
- **[wrsmith108/linear-claude-skill](https://github.com/wrsmith108/linear-claude-skill)**：含 MCP 与 GraphQL 工作流的 Linear Issue/Project/Team 管理技能（MIT）。
- **[wrsmith108/varlock-claude-skill](https://github.com/wrsmith108/varlock-claude-skill)**：Claude Code 的安全环境变量管理技能（MIT）。
- **[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)**：面向 Web 演示的前端幻灯片创建技能（MIT）。
- **[zxkane/aws-skills](https://github.com/zxkane/aws-skills)**：聚焦 AWS 的 Claude 智能体技能（MIT）。
- **[UrRhb/agentflow](https://github.com/UrRhb/agentflow)**：看板驱动的 AI 开发管道，用于编排多工作者 Claude Code 工作流，含确定性质量门、对抗性审查、成本追踪及防崩溃执行（MIT）。
- **[AgentPhone-AI/skills](https://github.com/AgentPhone-AI/skills)**：Claude Code 的 AgentPhone 插件 — API 优先的电话智能体工作流，包括电话呼叫、SMS、号码管理、语音智能体设置、流式 Webhooks 及工具调用模式。
- **[uxuiprinciples/agent-skills](https://github.com/uxuiprinciples/agent-skills)**：基于研究的 UX/UI 智能体技能，用于按 168 项原则审计界面、检测反模式及向 AI 编程会话注入 UX 上下文。
- **[voidborne-d/humanize-chinese](https://github.com/voidborne-d/humanize-chinese)**：中文 AI 文本检测与人性化套件，涵盖评分、重写、学术 AIGC 降重及风格转换工作流。
- **[voidborne-d/lambda-lang](https://github.com/voidborne-d/lambda-lang)**：智能体间协调语言，含紧凑原子结构，用于多智能体消息传递、编排及结构化协调日志。
- **[LambdaTest/agent-skills](https://github.com/LambdaTest/agent-skills)**：生产级测试自动化智能体技能 — 46 项技能覆盖 E2E、单元测试、移动端、BDD、视觉及云测试，支持 15+ 种语言（MIT）。
- **[flyingsquirrel0419/squirrel-skill](https://github.com/flyingsquirrel0419/squirrel-skill)**：全周期软件开发技能 — 规划、构建、测试、Lint、修复 Bug 及编写生产级文档。自动检测项目状态并适配其 8 阶段管道。兼容 9 大 AI 编程智能体平台（Apache 2.0）。
- **[CodeShuX/tokenwise](https://github.com/CodeShuX/tokenwise)**：`tokenwise` 技能源码 — Claude Code 的测量驱动型 Haiku/Sonnet/Opus 路由器，含按任务 NDJSON 日志、A/B 测试模式及已验证节省金额报告（MIT）。

### 灵感来源

- **[f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)**：提示词库的灵感来源。
- **[leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts)**：JavaScript 精通系列的灵感来源。

### 其他来源

- **[agent-cards/skill](https://github.com/agent-cards/skill)**：管理 AI 智能体的预付虚拟 Visa 卡。通过 MCP 工具创建卡片、查询余额、查看凭证、关闭卡片及获取支持。

## 仓库贡献者

<a href="https://github.com/sickn33/antigravity-awesome-skills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sickn33/antigravity-awesome-skills" alt="Repository contributors" />
</a>

由 [contrib.rocks](https://contrib.rocks) 生成。 *（图片可能已缓存；请在 GitHub 上[查看实时贡献者](https://github.com/sickn33/antigravity-awesome-skills/graphs/contributors)。）*

我们正式感谢以下贡献者对本仓库做出的卓越贡献！

- [@sck000](https://github.com/sck000)
- [@github-actions[bot]](https://github.com/apps/github-actions)
- [@sickn33](https://github.com/sickn33)
... (列表保持原样，仅翻译引导语)

## 加星历史

<a href="https://www.star-history.com/#sickn33/antigravity-awesome-skills&type=date&legend=top-left">
 <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=sickn33/antigravity-awesome-skills&type=date&legend=top-left" />
</a>

<a href="https://www.star-history.com/sickn33/antigravity-awesome-skills">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=sickn33/antigravity-awesome-skills&style=landscape1&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=sickn33/antigravity-awesome-skills&style=landscape1" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=sickn33/antigravity-awesome-skills&style=landscape1" />
 </picture>
</a>

如果 Antigravity Awesome Skills 对你有所帮助，欢迎 ⭐ 给仓库加星！

<!-- GitHub Topics (for maintainers): claude-code, gemini-cli, codex-cli, antigravity, cursor, github-copilot, opencode, agentic-skills, ai-coding, llm-tools, ai-agents, autonomous-coding, mcp, ai-developer-tools, ai-pair-programming, vibe-coding, skill, skills, SKILL.md, rules.md, CLAUDE.md, GEMINI.md, CURSOR.md -->

## 许可证

原始代码和工具采用 MIT 许可证。详见 [LICENSE](LICENSE)。

原始文档及其他非代码书面内容采用 [CC BY 4.0] 许可，除非上游有更具体的声明。归属及第三方许可详情见 [docs/sources/sources.md](docs/sources/sources.md)。

---