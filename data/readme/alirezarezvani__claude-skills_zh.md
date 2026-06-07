# Claude Code 技能与插件 —— 适用于所有编程工具的代理（Agent）技能

**338 个生产就绪（production-ready）的 Claude Code 技能、插件及代理技能，覆盖 13 款 AI 编程工具。**

最全面的开源 Claude Code 技能与代理插件库——同样兼容 OpenAI Codex、Gemini CLI、Cursor 及另外 9 款编程代理。提供可复用的专业知识包，涵盖工程（Engineering）、DevOps、营销（含 AEO —— Answer Engine Optimization for LLM citation / 面向大模型引用优化的答案引擎优化）、安全（PreToolUse hooks / PreToolUse 钩子）、合规、高管咨询（含创始人模式 CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE 角色设定 + 21 个 `/cs:*` 斜杠命令）、效率工具（capture/email/reflect）、学术研究栈（litreview/grants/dossier/patent/syllabus/pulse/notebooklm + hybrid router / 混合路由），以及企业级研究运营（clinical-research/research-finance/market-research/product-research，v2.9.0）。

**兼容工具：** Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Hermes Agent[^hermes] · Mistral Vibe[^vibe] · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity

[^hermes]: Hermes Agent 为 **BYO-sync tier**（自带同步层级）：仓库附带预生成的 `.hermes/skills/claude-skills/` 目录树，但你只需在本地运行一次 `python scripts/sync-hermes-skills.py` 即可安装至 `~/.hermes/skills/`。采用相同的 agentskills.io SKILL.md 标准 —— 无需格式转换。
[^vibe]: Mistral Vibe 同样为 **BYO-sync tier**：仓库附带预生成的 `.vibe/skills/claude-skills/` 目录树，在本地运行一次 `./scripts/vibe-install.sh` 即可安装至 `~/.vibe/skills/`。遵循相同的 agentskills.io SKILL.md 标准 —— 无需格式转换。文档：<https://docs.mistral.ai/mistral-vibe/agents-skills>.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-338-brightgreen?style=for-the-badge)](#skills-overview)
[![Agents](https://img.shields.io/badge/Agents-51+-blue?style=for-the-badge)](#agents)
[![Personas](https://img.shields.io/badge/Personas-7-purple?style=for-the-badge)](#personas)
[![Commands](https://img.shields.io/badge/Commands-87+-orange?style=for-the-badge)](#commands)
[![Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=for-the-badge)](https://github.com/alirezarezvani/claude-skills/stargazers)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1?style=for-the-badge)](https://getskillcheck.com)

> **GitHub 星标数超 5,200** —— 最全面的开源 Claude Code 技能与代理插件库。

---

## Claude Code 技能与代理插件是什么？

Claude Code 技能（也称代理技能或编程代理插件）是模块化的指令包，为 AI 编程代理提供开箱即用的领域专业知识。每个技能包含：

- **SKILL.md** —— 结构化指令、工作流与决策框架
- **Python 工具** —— 533 个 CLI 脚本（仅依赖标准库，零 pip 安装）
- **参考文档** —— 676 份模板、清单及领域专属知识文件

**一个仓库，兼容十三款平台。** 原生支持作为 Claude Code 插件、Codex 代理技能、Gemini CLI 技能、Hermes Agent 技能及 Mistral Vibe 技能使用，并可通过 `scripts/convert.sh` 转换适配更多工具。全部 533 个 Python 工具可在任何支持 Python 的环境中运行。

### Skills（技能） vs Agents（代理） vs Personas（角色设定）

| | Skills | Agents | Personas |
|---|---|---|---|
| **目的** | 如何执行任务 | 执行什么任务 | 谁在思考/决策 |
| **范围** | 单一领域 | 单一领域 | 跨领域 |
| **语气** | 中性 | 专业 | 人格化驱动 |
| **示例** | “按以下步骤进行 SEO” | “运行安全审计” | “像初创公司 CTO 一样思考” |

三者协同工作。详见 [Orchestration（编排）](#orchestration) 了解如何组合使用它们。

---

## 快速安装

### Gemini CLI（新增）

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

### Claude Code（推荐）

```bash
# Add the marketplace
/plugin marketplace add alirezarezvani/claude-skills

# Install by domain
/plugin install engineering-skills@claude-code-skills          # 24 core engineering
/plugin install engineering-advanced-skills@claude-code-skills  # 25 POWERFUL-tier
/plugin install product-skills@claude-code-skills               # 12 product skills
/plugin install marketing-skills@claude-code-skills             # 43 marketing skills
/plugin install ra-qm-skills@claude-code-skills                 # 12 regulatory/quality
/plugin install pm-skills@claude-code-skills                    # 6 project management
/plugin install c-level-skills@claude-code-skills               # 28 C-level advisory (full C-suite)
/plugin install business-growth-skills@claude-code-skills       # 4 business & growth
/plugin install finance-skills@claude-code-skills               # 2 finance (analyst + SaaS metrics)

# Or install individual skills
/plugin install skill-security-auditor@claude-code-skills       # Security scanner
/plugin install playwright-pro@claude-code-skills                  # Playwright testing toolkit
/plugin install self-improving-agent@claude-code-skills         # Auto-memory curation
/plugin install content-creator@claude-code-skills              # Single skill
```

### OpenAI Codex

```bash
npx agent-skills-cli add alirezarezvani/claude-skills --agent codex
# Or: git clone + ./scripts/codex-install.sh
```

### OpenClaw

```bash
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```

### 手动安装

```bash
git clone https://github.com/alirezarezvani/claude-skills.git
# Copy any skill folder to ~/.claude/skills/ (Claude Code) or ~/.codex/skills/ (Codex)
```

---

## 多工具支持（新增）

**一条脚本将全部 338 个技能转换为适配 9 款 AI 编程工具的格式：**

| Tool | Format | Install |
|------|--------|---------|
| **Cursor** | `.mdc` rules | `./scripts/install.sh --tool cursor --target .` |
| **Aider** | `CONVENTIONS.md` | `./scripts/install.sh --tool aider --target .` |
| **Kilo Code** | `.kilocode/rules/` | `./scripts/install.sh --tool kilocode --target .` |
| **Windsurf** | `.windsurf/skills/` | `./scripts/install.sh --tool windsurf --target .` |
| **OpenCode** | `.opencode/skills/` | `./scripts/install.sh --tool opencode --target .` |
| **Augment** | `.augment/rules/` | `./scripts/install.sh --tool augment --target .` |
| **Antigravity** | `~/.gemini/antigravity/skills/` | `./scripts/install.sh --tool antigravity` |
| **Hermes Agent** | `~/.hermes/skills/` | `python scripts/sync-hermes-skills.py --verbose` |
| **Mistral Vibe** | `~/.vibe/skills/` | `./scripts/vibe-install.sh` |

**工作原理：**

```bash
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all

# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project

# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force

# 3. Verify
find .cursor/rules -name "*.mdc" | wc -l  # Should show 338
```

**每个工具将获得：**
- ✅ 全部 338 个技能转换为原生格式
- ✅ 附带针对该工具的 README，含安装、验证与更新步骤
- ✅ 按需支持脚本、参考文档及模板
- ✅ 零手动转换工作量

运行 `./scripts/convert.sh --tool all` 可在本地生成针对各工具的适配输出。

---

## 技能概览

**覆盖 16 个领域的 338 项技能：**

| Domain | Skills | Highlights | Details |
|--------|--------|------------|---------|
| **🔧 Engineering — Core** | 51 | Architecture, frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright Pro (test gen, flaky fix, migrations), self-improving agent (auto-memory curation), security suite, a11y audit | [engineering-team/](engineering-team/) |
| **⚡ Engineering — POWERFUL** | 78 | Agent designer, RAG architect, database designer, CI/CD builder, security auditor, MCP builder, AgentHub, Helm charts, Terraform, self-eval, llm-wiki, tc-tracker, autoresearch-agent, **reliability portfolio** (feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect), ship-gate, security-guidance PreToolUse hook, **Matt Pocock skills** (write-a-skill, caveman, grill-me, handoff, grill-with-docs) | [engineering/](engineering/) |
| **🎯 Product** | 17 | Product manager, agile PO, strategist, UX researcher, UI design, landing pages, SaaS scaffolder, analytics, experiment designer, discovery, roadmap communicator, code-to-prd, apple-hig-expert | [product-team/](product-team/) |
| **📣 Marketing** | 46 | 8 pods: Content, SEO + AEO (`aeo` — E-E-A-T audit, citation tracking across 5 LLMs), CRO, Channels, Growth, Intelligence, Sales + context foundation + orchestration router | [marketing-skill/](marketing-skill/) |
| **🚀 Productivity** | 6 | `capture` (brain-dump-to-action), `email` pair (inbox-setup + inbox-triage), `reflect` (journal), `handoff` (Matt Pocock-inspired), `andreessen` (market-first decision mode) | [productivity/](productivity/) |
| **🎨 Marketing (top-level)** | 1 | `landing` — single-file HTML landing-page generator (4 design styles, GSAP patterns, brand palette validator) | [marketing/](marketing/) |
| **🔬 Research (academic)** | 8 | `research` orchestrator (hybrid router + fallback) + 7 specialists: `pulse`, `litreview`, `grants` (NIH), `dossier`, `patent`, `syllabus`, `notebooklm` | [research/](research/) |
| **🧪 Research Operations** ✨v2.9.0 | 5 | Enterprise/cross-functional research: orchestrator + `clinical-research` (study design), `research-finance` (R&D program finance), `market-research` (sizing/survey/segmentation), `product-research` (user research) — each with onboarding + customization + opt-in autoresearch bridge | [research-ops/](research-ops/) |
| **📋 Project Management** | 9 | Senior PM, scrum master, Jira, Confluence, Atlassian admin, templates + bundled Atlassian Remote MCP | [project-management/](project-management/) |
| **🏥 Regulatory & QM** | 18 | ISO 13485, MDR 2017/745, FDA, ISO 27001, GDPR, SOC 2, CAPA, risk management | [ra-qm-team/](ra-qm-team/) |
| **🛡️ Compliance OS** | 9 | Compliance operating system — controls, evidence, audit-readiness workflows | [compliance-os/](compliance-os/) |
| **💼 C-Level Advisory** | 66 | Full C-suite (CEO/CTO/CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE) + founder-mode agents + orchestration + board meetings + culture & collaboration | [c-level-advisor/](c-level-advisor/) |
| **📈 Business & Growth** | 5 | Customer success, sales engineer, revenue ops, contracts & proposals, BizDev toolkit | [business-growth/](business-growth/) |
| **🏭 Business Operations** | 7 | Orchestrator + process-mapper, vendor-management, capacity-planner, internal-comms, knowledge-ops, procurement-optimizer | [business-operations/](business-operations/) |
| **🤝 Commercial** | 8 | Orchestrator + pricing-strategist, deal-desk, partnerships-architect, channel-economics, commercial-policy, rfp-responder, commercial-forecaster | [commercial/](commercial/) |
| **💰 Finance** | 4 | Financial analyst (DCF, budgeting, forecasting), SaaS metrics coach, business investment advisor | [finance/](finance/) |

---

## 角色设定（Personas）

预配置的代理身份，配备精选的技能组合、工作流及独特的沟通风格。角色设定不仅限于“使用这些技能”——它们定义了代理的思考方式、优先级排序与交互逻辑。

| Persona | Domain | Best For |
|---------|--------|----------|
| [**Startup CTO**](agents/personas/startup-cto.md) | Engineering + Strategy | Architecture decisions, tech stack selection, team building, technical due diligence |
| [**Growth Marketer**](agents/personas/growth-marketer.md) | Marketing + Growth | Content-led growth, launch strategy, channel optimization, bootstrapped marketing |
| [**Solo Founder**](agents/personas/solo-founder.md) | Cross-domain | One-person startups, side projects, MVP building, wearing all hats |

**使用方式：**
```bash
# Claude Code
cp agents/personas/startup-cto.md ~/.claude/agents/

# Any tool
./scripts/convert.sh --tool cursor  # Converts personas too
```

详见 [agents/personas/](agents/personas/)。你可通过 [TEMPLATE.md](agents/personas/TEMPLATE.md) 创建自定义角色设定。

---

## 编排（Orchestration）

一套轻量级协议，用于协调跨越领域边界的工作流中的角色设定、技能与代理。无需依赖额外框架。

**四种编排模式：**

| Pattern | What | When |
|---------|------|------|
| **Solo Sprint** | Switch personas across project phases | Side projects, MVPs, solo founders |
| **Domain Deep-Dive** | One persona + multiple stacked skills | Architecture reviews, compliance audits |
| **Multi-Agent Handoff** | Personas review each other's output | High-stakes decisions, launch readiness |
| **Skill Chain** | Sequential skills, no persona needed | Content pipelines, repeatable checklists |

**示例：为期 6 周的产品发布**
```
Week 1-2: startup-cto + aws-solution-architect + senior-frontend → Build
Week 3-4: growth-marketer + launch-strategy + copywriting + seo-audit → Prepare
Week 5-6: solo-founder + email-sequence + analytics-tracking → Ship and iterate
```

详见 [orchestration/ORCHESTRATION.md](orchestration/ORCHESTRATION.md) 获取完整协议与示例。

---

## POWERFUL 层级（高级技能）

25 项具备深度生产级能力的高级技能：

| Skill | What It Does |
|-------|-------------|
| **agent-designer** | Multi-agent orchestration, tool schemas, performance evaluation |
| **agent-workflow-designer** | Sequential, parallel, router, orchestrator, and evaluator patterns |
| **rag-architect** | RAG pipeline builder, chunking optimizer, retrieval evaluator |
| **database-designer** | Schema analyzer, ERD generation, index optimizer, migration generator |
| **database-schema-designer** | Requirements → migrations, types, seed data, RLS policies |
| **migration-architect** | Migration planner, compatibility checker, rollback generator |
| **skill-security-auditor** | 🔒 Security gate — scan skills for malicious code before installation |
| **ci-cd-pipeline-builder** | Analyze stack → generate GitHub Actions / GitLab CI configs |
| **mcp-server-builder** | Build MCP servers from OpenAPI specs |
| **pr-review-expert** | Blast radius analysis, security scan, coverage delta |
| **api-design-reviewer** | REST API linter, breaking change detector, design scorecard |
| **api-test-suite-builder** | Scan API routes → generate complete test suites |
| **dependency-auditor** | Multi-language scanner, license compliance, upgrade planner |
| **release-manager** | Changelog generator, semantic version bumper, readiness checker |
| **observability-designer** | SLO designer, alert optimizer, dashboard generator |
| **performance-profiler** | Node/Python/Go profiling, bundle analysis, load testing |
| **monorepo-navigator** | Turborepo/Nx/pnpm workspace management & impact analysis |
| **changelog-generator** | Conventional commits → structured changelogs |
| **codebase-onboarding** | Auto-generate onboarding docs from codebase analysis |
| **runbook-generator** | Codebase → operational runbooks with commands |
| **git-worktree-manager** | Parallel dev with port isolation, env sync |
| **env-secrets-manager** | .env management, leak detection, rotation workflows |
| **incident-commander** | Incident response playbook, severity classifier, PIR generator |
| **tech-debt-tracker** | Codebase debt scanner, prioritizer, trend dashboard |
| **interview-system-designer** | Interview loop designer, question bank, calibrator |

---

## 🔒 技能安全审计器

v2.0.0 新增 —— 在安装前对任意技能进行安全风险审计：

```bash
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/
```

扫描项包括：命令注入、代码执行、数据外泄、提示词注入（Prompt Injection）、依赖供应链风险及权限提升。返回 **PASS / WARN / FAIL** 状态并附带修复建议。

**零外部依赖。** 可在任何支持 Python 的环境中运行。

---

## 近期增强技能

以下技能已升级至生产级质量：

- `engineering/git-worktree-manager` — worktree lifecycle + cleanup automation scripts
- `engineering/mcp-server-builder` — OpenAPI -> MCP scaffold + manifest validator
- `engineering/changelog-generator` — release note generator + conventional commit linter
- `engineering/ci-cd-pipeline-builder` — stack detector + pipeline generator
- `marketing-skill/prompt-engineer-toolkit` — prompt A/B tester + prompt version/diff manager

每项技能现均附带 `scripts/`、独立提取的 `references/`，以及侧重使用的 `README.md`。

---

## 使用示例

### Architecture Review
```
Using the senior-architect skill, review our microservices architecture
and identify the top 3 scalability risks.
```

### Content Creation
```
Using the content-creator skill, write a blog post about AI-augmented
development. Optimize for SEO targeting "Claude Code tutorial".
```

### Compliance Audit
```
Using the mdr-745-specialist skill, review our technical documentation
for MDR Annex II compliance gaps.
```

---

## Python 分析工具

技能包附带 533 个 CLI 工具（均已验证，仅依赖标准库）：

```bash
# SaaS health check
python3 finance/saas-metrics-coach/scripts/metrics_calculator.py --mrr 80000 --customers 200 --churned 3 --json

# Brand voice analysis
python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py article.txt

# Tech debt scoring
python3 c-level-advisor/cto-advisor/scripts/tech_debt_analyzer.py /path/to/codebase

# RICE prioritization
python3 product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv

# Security audit
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/

# Landing page (TSX + Tailwind)
python3 product-team/landing-page-generator/scripts/landing_page_scaffolder.py config.json --format tsx
```

---

## 相关项目

| Project | Description |
|---------|-------------|
| [**Claude Code Skills & Agents Factory**](https://github.com/alirezarezvani/claude-code-skills-agents-factory) | Methodology for building skills at scale |
| [**Claude Code Tresor**](https://github.com/alirezarezvani/claude-code-tresor) | Productivity toolkit with 60+ prompt templates |
| [**Product Manager Skills**](https://github.com/Digidai/product-manager-skills) | Senior PM agent with 6 knowledge domains, 12 templates, 30+ frameworks — discovery, strategy, delivery, SaaS metrics, career coaching, AI product craft |
| [**toprank**](https://github.com/nowork-studio/toprank) | 9 SEO and Google Ads skills for Claude Code — connects Google Search Console, PageSpeed Insights, and Google Ads API; ships meta tag, schema markup, and keyword bid fixes to source or CMS. MIT, 107 stars |

---

## 常见问题（FAQ）

**How do I install Claude Code plugins?**
添加市场源 `/plugin marketplace add alirezarezvani/claude-skills`，随后使用 `/plugin install <name>@claude-code-skills` 安装任意技能包。

**Do these skills work with OpenAI Codex / Cursor / Windsurf / Aider / Mistral Vibe?**
是的。该库原生兼容 13 款工具：Claude Code、OpenAI Codex、Gemini CLI、OpenClaw、Hermes Agent、Mistral Vibe、Cursor、Aider、Windsurf、Kilo Code、OpenCode、Augment 及 Antigravity。Hermes Agent 与 Mistral Vibe 均遵循相同的 agentskills.io SKILL.md 标准 —— 运行 `python scripts/sync-hermes-skills.py` 或 `./scripts/vibe-install.sh` 即可安装。针对其他工具，请运行 `./scripts/convert.sh --tool all` 后执行 `./scripts/install.sh --tool <name>`。详见 [Multi-Tool Integrations](https://alirezarezvani.github.io/claude-skills/integrations/)。

**Will updating break my installation?**
不会。我们遵循语义化版本控制（Semantic Versioning），并在补丁版本内保持向后兼容。现有脚本参数、插件源路径及 SKILL.md 结构绝不会在补丁版本中更改。详见 [CHANGELOG](CHANGELOG.md) 了解各版本更新说明。

**Are the Python tools dependency-free?**
是的。全部 533 个 Python CLI 工具仅使用标准库 —— 零 pip 安装需求。每个脚本均已验证支持 `--help` 参数运行。

**How do I create my own Claude Code skill?**
每个技能是一个文件夹，内含 `SKILL.md`（含 frontmatter + 指令）、可选的 `scripts/`、`references/` 及 `assets/`。详见 [Skills & Agents Factory](https://github.com/alirezarezvani/claude-code-skills-agents-factory) 获取分步指南。

---

## 贡献指南（Contributing）

我们欢迎所有形式的贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md) 了解规范。

**快速上手建议：**
- 在尚未充分覆盖的领域添加新技能
- 优化现有 Python 工具
- 为脚本补充测试用例
- 为非英语市场翻译技能文档

---

## 许可证（License）

MIT —— 详见 [LICENSE](LICENSE)。

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alirezarezvani/claude-skills&type=Date)](https://star-history.com/#alirezarezvani/claude-skills&Date)

---

**Built by [Alireza Rezvani](https://alirezarezvani.com)** · [Medium](https://alirezarezvani.medium.com) · [Twitter](https://twitter.com/nginitycloud)