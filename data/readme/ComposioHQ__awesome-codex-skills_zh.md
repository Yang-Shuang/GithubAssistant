<h1 align="center">Awesome Codex Skills</h1>

<p align="center">
<a href="https://dashboard.composio.dev/login?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeCodexSkills">

  <img width="1280" height="640" alt="Composio banner" src="codex_cover_image.png">
</a>
</p>

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome" />
  </a>
  <a href="https://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome" />
  </a>
</p>
<div>
<p align="center">
  <a href="https://twitter.com/composio">
    <img src="https://img.shields.io/badge/Follow on X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X" />
  </a>
  <a href="https://www.linkedin.com/company/composiohq/">
    <img src="https://img.shields.io/badge/Follow on LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" />
  </a>
  <a href="https://discord.com/invite/composio">
    <img src="https://img.shields.io/badge/Join our Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" />
  </a>
  </p>
</div>

一份精心整理的实用 Codex 技能列表，用于自动化跨 Codex CLI 和 API 的工作流。


> **想要不仅能生成文本的技能？** Codex 可以发送邮件、创建 Issue、在 Slack 上发帖，并在 1000+ 款应用中执行实际操作。[查看方法 →](./connect/)

---

## Quickstart: Add Skills to Codex

### Install with the Skill Installer (recommended)

```bash
git clone https://github.com/ComposioHQ/awesome-codex-skills.git
cd awesome-codex-skills
# Install one or more skills into $CODEX_HOME/skills (defaults to ~/.codex/skills)
python skill-installer/scripts/install-skill-from-github.py --repo ComposioHQ/awesome-codex-skills --path meeting-notes-and-actions
```

安装器会获取该技能并将其放置于 `$CODEX_HOME/skills/<skill-name>`。重启 Codex 即可加载新技能。

### Manual install

1. Copy the desired skill folder (e.g., `./spreadsheet-formula-helper`) into `$CODEX_HOME/skills/` (defaults to `~/.codex/skills/`).
2. Restart Codex so it loads the new metadata.
3. In your next session, describe the task or mention the skill name; Codex will trigger matching skills based on their `description` frontmatter.

---

## Contents

- [Bernstein](https://github.com/chernistry/bernstein) - 多智能体编排器，配备 Codex CLI 适配器。在隔离的 git worktrees 中并行运行多个 Codex 智能体，并设置质量门禁。
- [What Are Codex Skills?](#what-are-codex-skills)
- [Skills](#skills)
  - [Development & Code Tools](#development--code-tools)
  - [Productivity & Collaboration](#productivity--collaboration)
  - [Communication & Writing](#communication--writing)
  - [Data & Analysis](#data--analysis)
  - [Meta & Utilities](#meta--utilities)
- [Using Skills in Codex](#using-skills-in-codex)
- [Creating Skills](#creating-skills)
- [Contributing](#contributing)
- [Join the Community](#join-the-community)

## What Are Codex Skills?

Codex skills are modular instruction bundles that tell Codex how to execute a task the way you want it done. Each skill lives in its own folder with a `SKILL.md` that includes metadata (name + description) and step-by-step guidance. Codex reads the metadata to decide when to trigger a skill and loads the body only after it fires, keeping context lean.

## Skills

### Development & Code Tools

- [brooks-lint](https://github.com/hyhmrright/brooks-lint) - AI 代码审查基于六本经典工程书籍——提供带有文献引用的衰退风险诊断、严重性标签以及四种分析模式（PR 审查、架构审计、技术债务、测试质量）。安装：`python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo hyhmrright/brooks-lint --path skills/brooks-lint --name brooks-lint`
- [bringyour-migration-auditor](https://github.com/unitedideas/bringyour-mcp/tree/main/skills/bringyour-migration-auditor) - 审查从 Claude Code 到 Codex harness 的迁移，检查 AGENTS.md/CLAUDE.md 范围、hooks、MCP 配置、技能、密钥和验证说明。安装：`python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo unitedideas/bringyour-mcp --path skills/bringyour-migration-auditor --name bringyour-migration-auditor`
- [codebase-migrate/](./codebase-migrate/) - 以可审查的批次运行大型代码库迁移和多文件重构，并附带 CI 验证。
- [codebase-recon](https://github.com/yujiachen-y/codebase-recon-skill) - 在读取任何代码之前分析 git 历史以理解代码库——通过自动扩展的分析展示热点、Bug 聚集地、巴士因子（bus factor）、开发动量和高风险文件（热点 ∩ Bug 聚集地）。安装：`python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo yujiachen-y/codebase-recon-skill --path skills/codebase-recon --name codebase-recon`
- [create-plan/](./create-plan/) - 快速起草简洁的代码任务执行计划。
- [deploy-pipeline/](./deploy-pipeline/) - 端到端的 Stripe → Supabase → Vercel 发布流水线，包含验证和回滚功能。
- [Emdash Skills](https://github.com/megabytespace/claude-skills) - 14 个类别的自主产品构建操作系统：CF Workers + Hono + Angular + D1 + Stripe。一行提示词即可部署 SaaS，附带 94 份参考文档、18 个智能体以及原生支持 Codex `.agents/skills/`。
- [gh-address-comments/](./gh-address-comments/) - 使用 `gh` 处理当前分支在 GitHub 上的 PR 的审查或 Issue 评论。
- [gh-fix-ci/](./gh-fix-ci/) - 检查失败的 GitHub Actions 检查项，总结失败原因并提出修复方案。
- [mcp-builder/](./mcp-builder/) - 遵循最佳实践并使用评估框架构建和测试 MCP 服务器。
- [pr-review-ci-fix/](./pr-review-ci-fix/) - 通过 Composio CLI 实现自动化的 GitHub/GitLab PR 审查及 CI 自动修复循环。
- [sentry-triage/](./sentry-triage/) - 通过将堆栈帧映射到本地源码来诊断 Sentry 问题——无需复制粘贴。
- [webapp-testing/](./webapp-testing/) - 运行针对性的 Web 应用测试并总结结果。
- [AuraKit](https://github.com/smorky850612/Aurakit) - 全功能技能框架：46 种模式、23 个子智能体、6 层 OWASP 安全机制、10 个生命周期钩子，节省约 55% 的 Token 消耗。安装：`npx @smorky85/aurakit`
- [Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) - 受控的 Codex 技能运行环境，用于分阶段、测试驱动的工作流：将 340+ 个技能路由至需求冻结、计划审批、执行、验证证据和跨会话记忆。
- [polywave](https://github.com/blackwell-systems/polywave-codex) - 具有结构合并安全性的并行智能体协调。Scout 负责分解任务，Wave 智能体在隔离的 worktrees 中实施，文件所有权互不重叠。Claude Code 和 Codex 使用相同协议。

### Productivity & Collaboration

- [connect/](./connect/) - 通过 Composio CLI 将 Codex 连接到 1000+ 款应用以执行实际操作（Slack、GitHub、Notion 等）。
- [connect-apps/](./connect-apps/) - 配置 Composio CLI 连接 Claude，并从终端启动应用工作流。
- [issue-triage/](./issue-triage/) - 对 Linear 或 Jira 的积压任务进行分类，并在终端中运行 Bug 扫描。
- [linear/](./linear/) - 在 Linear 中管理 Issue、项目和团队工作流。
- [meeting-insights-analyzer/](./meeting-insights-analyzer/) - 分析会议记录以提取主题、风险和后续行动项。
- [meeting-notes-and-actions/](./meeting-notes-and-actions/) - 将会议记录转化为包含决策和标记负责人的待办事项的摘要。
- [internal-comms/](./internal-comms/) - 撰写内部公告、更新信息和利益相关者沟通内容。
- [invoice-organizer/](./invoice-organizer/) - 标准化并提取发票数据，用于跟踪和报告。
- [notion-knowledge-capture/](./notion-knowledge-capture/) - 将聊天或笔记转换为带有正确链接的结构化 Notion 页面。
- [notion-meeting-intelligence/](./notion-meeting-intelligence/) - 结合 Notion 上下文与 Codex 研究准备会议材料。
- [notion-research-documentation/](./notion-research-documentation/) - 综合多个 Notion 来源生成简报、对比分析或带引用的报告。
- [notion-spec-to-implementation/](./notion-spec-to-implementation/) - 将 Notion 规范转化为实施计划、任务和进度跟踪。
- [support-ticket-triage/](./support-ticket-triage/) - 对客户支持工单进行分类、定级、规划下一步行动并起草回复。
- [file-organizer/](./file-organizer/) - 整理、重命名和清理文件，保持工作区整洁。
- [paperjsx/](./paperjsx/) - 从结构化 JSON 生成 PPTX 演示文稿、DOCX 文档、XLSX 电子表格以及 PDF 发票/报告/图表。通过 `@paperjsx/mcp-server` 本地运行——无需 API 密钥，无网络请求。
- [skill-share/](./skill-share/) - 在团队成员间共享技能和可复用指令。

### Communication & Writing
- [codex-sms-verification](https://github.com/virtualsms-io/codex-sms-verification) - 外部仓库：通过 VirtualSMS MCP 为 AI 智能体提供真实 SIM 卡短信验证服务。覆盖 145+ 个国家/地区、2000+ 项服务，支持托管（mcp.virtualsms.io）和本地 stdio 传输方式。

- [email-draft-polish/](./email-draft-polish/) - 起草、重写或精简邮件，确保语气和受众匹配。
- [changelog-generator/](./changelog-generator/) - 从提交记录或摘要生成清晰的更新日志。
- [content-research-writer/](./content-research-writer/) - 进行内容研究并撰写带引用来源的文章草稿。
- [diasporic-intelligence](https://github.com/MinistaJazz/diasporic-intelligence) - 外部仓库：具有同意治理谱系的 AI 引用技能，包含归属、溯源、撤销和非冒充边界机制。
- [novel-writing](https://github.com/wgwtest/novel-writing) - 外部仓库：面向公众的 Codex 技能，用于小说规划、章节起草、场景续写和修订。
- [tailored-resume-generator/](./tailored-resume-generator/) - 根据职位描述定制简历，并量化工作影响。
- [unslop](https://github.com/MohamedAbdallah-14/unslop) - 外部仓库：CLI 和 MCP 服务器，用于去除文本中的 AI 写作模式（如三段式排比、过度使用破折号、模糊措辞堆叠及奉承开头）。兼容 Codex、Claude Code、Gemini CLI 和 Cursor。提供五种强度等级以及仅审计模式。

### Data & Analysis

- [spreadsheet-formula-helper/](./spreadsheet-formula-helper/) - 编写和调试电子表格公式、透视表和数组公式。
- [competitive-ads-extractor/](./competitive-ads-extractor/) - 分析竞品广告并提取结构化洞察。
- [datadog-logs/](./datadog-logs/) - 通过 Composio CLI 从终端过滤 Datadog 日志，提供 JSON 友好输出及摘要工作流。
- [developer-growth-analysis/](./developer-growth-analysis/) - 分析 Codex 聊天历史以识别编码模式和学习盲区。
- [lead-research-assistant/](./lead-research-assistant/) - 研究潜在客户并利用企业画像数据丰富记录。
- [domain-name-brainstormer/](./domain-name-brainstormer/) - 根据标准和检查项头脑风暴可用域名。
- [raffle-winner-picker/](./raffle-winner-picker/) - 随机抽取获奖者，并提供便于审计的日志。
- [langsmith-fetch/](./langsmith-fetch/) - 拉取 LangSmith 项目/测试数据以供分析。
- [helium-mcp/](./helium-mcp/) - 通过 MCP 搜索实时新闻（含偏见评分）、获取实时市场数据、ML 期权定价及平衡的新闻合成。

### Meta & Utilities

- [brand-guidelines/](./brand-guidelines/) - 将 OpenAI/Codex 品牌颜色和排版应用于生成内容。
- [agent-deep-links/](./agent-deep-links/) - 为 Codex、Cursor 和 VS Code 构建并验证深度链接，支持 Slack 安全格式及回退指南。
- [canvas-design/](./canvas-design/) - 生成结构化的 Canvas 布局和视觉设计稿。
- [image-enhancer/](./image-enhancer/) - 使用可配置预设放大和优化图像。
- [slack-gif-creator/](./slack-gif-creator/) - 为 Slack 生成带标题和样式的 GIF。
- [theme-factory/](./theme-factory/) - 创建可复用的主题 Token 和调色板。
- [video-downloader/](./video-downloader/) - 下载视频并准备离线审阅版本。
- [template-skill/](./template-skill/) - 用于构建新技能的入门模板。
- [skill-installer/](./skill-installer/) - 辅助脚本，用于从精选列表或 GitHub 路径安装技能。
- [skill-creator/](./skill-creator/) - 指导如何构建高效的 Codex 技能（采用渐进式披露机制）。

## Using Skills in Codex

- Skills live in `$CODEX_HOME/skills` (default `~/.codex/skills`). Each subfolder needs a `SKILL.md` with `name` and `description` frontmatter.
- After installing or updating a skill, restart Codex so it reloads metadata.
- In a session, describe the task naturally; Codex auto-triggers skills whose descriptions match the request. You can also mention a skill by name if you want it considered.
- To verify installation, list installed skills (`ls ~/.codex/skills`) and inspect metadata (`head ~/.codex/skills/<skill>/SKILL.md`).

## Creating Skills

Skill layout:

```
skill-name/
├── SKILL.md          # Required: instructions + YAML frontmatter
├── scripts/          # Optional: helper scripts for deterministic steps
├── references/       # Optional: long-form docs loaded only when needed
└── assets/           # Optional: templates or files used in outputs
```

Basic SKILL.md template:

```markdown
---
name: my-skill-name
description: What the skill does and when Codex should use it.
---

# My Skill Name

Clear instructions and steps for Codex to execute the task.
```

Best practices:

- Keep the `description` exhaustive about when to trigger; keep the body focused on execution steps.
- Use progressive disclosure: put detailed references in `references/` and call them out from `SKILL.md` only when needed.
- Include scripts for repeatable or deterministic operations; mention when Codex should run them.
- Avoid extra docs (README, changelog) inside the skill folder to keep context lean.

## Contributing

PRs welcome. Add real, reusable skills, keep descriptions precise, and include any needed scripts or references. If you add new skills, ensure the `description` clearly states when Codex should trigger and test that metadata fits within context limits.

## Join the Community

- [Join our Discord](https://discord.com/invite/composio) - Chat with other developers building Codex skills.
- [Follow on X](https://twitter.com/composio) - Updates on new skills and features.
Questions? [support@composio.dev](mailto:support@composio.dev)

## Resources

- [Top Codex Skills](https://composio.dev/content/top-codex-skills)

---

<p align="center">
  <b>Join thousands of developers building agents that ship</b>
</p>

<p align="center">
  <a href="https://dashboard.composio.dev/login?utm_source=Github&utm_content=AwesomeCodexSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>