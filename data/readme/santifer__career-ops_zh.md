# Career-Ops

[English](README.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [한국어](README.ko-KR.md) | [日本語](README.ja.md) | [Русский](README.ru.md) | [简体中文](README.cn.md) | [繁體中文](README.zh-TW.md)

<p align="center">
  <a href="https://x.com/santifer"><img src="docs/hero-banner.jpg" alt="Career-Ops — Multi-Agent Job Search System" width="800"></a>
</p>

<p align="center">
  <em>我曾花了数月艰难地手动投递简历。于是，我打造了自己希望拥有的求职系统。</em><br>
  企业使用 AI 筛选候选人。<strong>我只是让候选人拥有选择企业的 AI。</strong><br>
  <em>现在它已开源。</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-000?style=flat&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenCode-111827?style=flat&logo=terminal&logoColor=white" alt="OpenCode">
  <img src="https://img.shields.io/badge/Gemini_CLI-4285F4?style=flat&logo=google&logoColor=white" alt="Gemini CLI">
  <img src="https://img.shields.io/badge/Codex_(soon)-6B7280?style=flat&logo=openai&logoColor=white" alt="Codex">
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white" alt="Node.js">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white" alt="Go">
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT">
  <a href="TRADEMARK.md"><img src="https://img.shields.io/badge/Trademark-Policy-blue.svg" alt="Trademark Policy"></a>
  <a href="https://discord.gg/8pRpHETxa4"><img src="https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  <br>
  <img src="https://img.shields.io/badge/EN-blue?style=flat" alt="EN">
  <img src="https://img.shields.io/badge/ES-red?style=flat" alt="ES">
  <img src="https://img.shields.io/badge/DE-grey?style=flat" alt="DE">
  <img src="https://img.shields.io/badge/FR-blue?style=flat" alt="FR">
  <img src="https://img.shields.io/badge/PT--BR-green?style=flat" alt="PT-BR">
  <img src="https://img.shields.io/badge/KO-white?style=flat" alt="KO">
  <img src="https://img.shields.io/badge/JA-red?style=flat" alt="JA">
  <img src="https://img.shields.io/badge/ZH--CN-red?style=flat" alt="ZH-CN">
  <img src="https://img.shields.io/badge/ZH--TW-blue?style=flat" alt="ZH-TW">
</p>

---

<p align="center">
  <img src="docs/demo.gif" alt="Career-Ops Demo" width="800">
</p>

<p align="center"><strong>已评估 740+ 个职位机会 · 生成 100+ 份定制简历 · 成功拿下理想 Offer</strong></p>

<p align="center"><a href="https://discord.gg/8pRpHETxa4"><img src="https://img.shields.io/badge/Join_the_community-Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a></p>

## 这是什么

Career-Ops 将任意 AI 编程命令行工具（CLI）转化为完整的求职指挥中心。不再需要手动在电子表格中跟踪申请进度，你将获得一个由 AI 驱动的自动化流程：

- **评估职位**：使用结构化的 A-F 评分体系（10 个加权维度）进行评估
- **生成定制 PDF**：针对职位描述优化 ATS（应用追踪系统）简历的定制化 PDF
- **自动扫描招聘门户**：自动扫描 Greenhouse、Ashby、Lever 及公司官网等招聘平台
- **批量处理**：通过子代理并行评估 10+ 个职位
- **全链路追踪**：在单一数据源中记录所有状态，并附带完整性校验

> **重要提示：这并非盲目海投工具。** Career-Ops 是一个过滤器——它帮你从数百个机会中筛选出真正值得投入时间的少数职位。系统强烈建议不要申请评分低于 4.0/5 的职位。你的时间很宝贵，招聘官的时间也一样。提交前请务必亲自审核。

Career-Ops 具备智能体（Agent）能力：Claude Code 使用 Playwright 浏览招聘页面，通过推理分析你的 CV（简历）与职位描述的匹配度（而非简单的关键词匹配），并针对每个职位调整你的简历内容。

> **注意：初期的评估结果可能不够理想。** 系统目前还不了解你。请向它提供上下文信息——你的 CV、职业经历、核心优势证明、偏好、擅长领域以及希望避免的方向。你投入的引导越多，它的表现就会越好。这就像带教一名新招聘专员：第一周需要让它熟悉你的背景，之后它就会变得不可或缺。

由一位实际用它评估了 740+ 个职位机会、生成 100+ 份定制简历并成功拿下 Head of Applied AI（应用人工智能负责人）职位的开发者打造。[阅读完整案例研究](https://santifer.io/career-ops-system)。

## 功能特性

| 功能 | 说明 |
|---------|-------------|
| **自动流水线** | 粘贴链接，一键生成完整评估 + PDF + 追踪记录 |
| **六维评估** | 角色摘要、简历匹配度、职级策略、薪酬调研、个性化调整、面试准备（STAR+R） |
| **面试故事库** | 在多次评估中积累 STAR+反思型故事，提炼 5-10 个核心故事以应对各类行为面试题 |
| **谈判话术** | 薪资谈判框架、地域折扣应对策略、竞业 Offer 杠杆技巧 |
| **ATS 简历生成** | 注入关键词的简历，采用 Space Grotesk + DM Sans 排版设计 |
| **招聘门户扫描器** | 预置 45+ 家公司配置（Anthropic, OpenAI, ElevenLabs, Retool, n8n 等）+ 支持跨 Ashby, Greenhouse, Lever, Wellfound 的自定义查询 |
| **批量处理** | 使用 `claude -p` 并行评估 |
| **仪表盘终端界面（TUI）** | 基于终端的用户界面，支持浏览、筛选和排序求职流水线 |
| **人在回路（Human-in-the-Loop）** | AI 负责评估与推荐，你负责决策与执行。系统从不自动提交申请——最终决定权始终在你手中。 |
| **流程完整性** | 自动化合并、去重、状态标准化及健康检查 |

## 快速开始

```bash
# 1. Clone and install
git clone https://github.com/santifer/career-ops.git
cd career-ops && npm install
npx playwright install chromium   # Required for PDF generation

# 2. Check setup
npm run doctor                     # Validates all prerequisites

# 3. Configure
cp config/profile.example.yml config/profile.yml  # Edit with your details
cp templates/portals.example.yml portals.yml       # Customize companies

# 4. Add your CV
# Create cv.md in the project root with your CV in markdown

# 5. Personalize with Claude
claude   # Open Claude Code in this directory

# Then ask Claude to adapt the system to you:
# "Change the archetypes to backend engineering roles"
# "Translate the modes to English"
# "Add these 5 companies to portals.yml"
# "Update my profile with this CV I'm pasting"

# 6. Start using
# Paste a job URL or run /career-ops
```

> **该系统专为让 Claude 自行定制而设计。** 模式（modes）、原型（archetypes）、评分权重、谈判话术——只需让 Claude 修改即可。它读取自身使用的文件，因此清楚知道该编辑哪些内容。

完整设置指南请参阅 [docs/SETUP.md](docs/SETUP.md)。

## Gemini CLI 集成

Career-Ops 原生支持 [Gemini CLI](https://github.com/google-gemini/gemini-cli)——与它支持 Claude Code 和 OpenCode 的方式完全相同。所有 15 个斜杠命令均可用，并沿用相同的 `modes/*.md` 评估逻辑。

### 选项 A — 原生 Gemini CLI（推荐）

```bash
# 1. Install Gemini CLI
npm install -g @google/gemini-cli
# or: npx @google/gemini-cli --version

# 2. Authenticate (free — uses your Google account)
gemini auth

# 3. Run in the career-ops directory
cd career-ops
gemini

# 4. Use slash commands just like Claude Code
/career-ops "Senior AI Engineer at Anthropic..."
/career-ops-evaluate --file ./jds/openai.txt
/career-ops-scan
/career-ops-pdf
/career-ops-tracker
```

`GEMINI.md` 文件将作为上下文自动加载。所有 15 个命令均定义在 `.gemini/commands/*.toml` 中。

### 选项 B — 独立 API 脚本（无需安装 CLI）

```bash
# 1. Get a free API key at https://aistudio.google.com/apikey
cp .env.example .env
# Edit .env → set GEMINI_API_KEY=your_key_here

# 2. Install dependencies
npm install

# 3. Evaluate a job description
node gemini-eval.mjs "We are looking for a Senior AI Engineer..."
node gemini-eval.mjs --file ./jds/my-job.txt
npm run gemini:eval -- "JD text here"
```

> **免费额度：** 两种选项均无需绑定计费方式即可使用。原生 CLI 采用 Google OAuth；API 脚本使用 `gemini-2.0-flash`（15 RPM，每日免费 1M tokens）。

## 使用方法

Career-Ops 是一个包含多种模式的单斜杠命令：

```
/career-ops                → Show all available commands
/career-ops {paste a JD}   → Full auto-pipeline (evaluate + PDF + tracker)
/career-ops scan           → Scan portals for new offers
/career-ops pdf            → Generate ATS-optimized CV
/career-ops batch          → Batch evaluate multiple offers
/career-ops tracker        → View application status
/career-ops apply          → Fill application forms with AI
/career-ops pipeline       → Process pending URLs
/career-ops contacto       → LinkedIn outreach message
/career-ops deep           → Deep company research
/career-ops training       → Evaluate a course/cert
/career-ops project        → Evaluate a portfolio project
```

或者直接粘贴职位链接或描述——Career-Ops 会自动检测并运行完整流水线。

## 工作原理

```
You paste a job URL or description
        │
        ▼
┌──────────────────┐
│  Archetype       │  Classifies: LLMOps / Agentic / PM / SA / FDE / Transformation
│  Detection       │
└────────┬─────────┘
         │
┌────────▼─────────┐
│  A-F Evaluation  │  Match, gaps, comp research, STAR stories
│  (reads cv.md)   │
└────────┬─────────┘
         │
    ┌────┼────┐
    ▼    ▼    ▼
 Report  PDF  Tracker
  .md   .pdf   .tsv
```

## 预配置招聘门户

扫描器内置 **45+ 家公司** 的扫描配置及跨主流招聘网站的 **19 个搜索查询**。复制 `templates/portals.example.yml` 到 `portals.yml` 并添加你自己的配置：

**AI Labs:** Anthropic, OpenAI, Mistral, Cohere, LangChain, Pinecone
**Voice AI:** ElevenLabs, PolyAI, Parloa, Hume AI, Deepgram, Vapi, Bland AI
**AI Platforms:** Retool, Airtable, Vercel, Temporal, Glean, Arize AI
**Contact Center:** Ada, LivePerson, Sierra, Decagon, Talkdesk, Genesys
**Enterprise:** Salesforce, Twilio, Gong, Dialpad
**LLMOps:** Langfuse, Weights & Biases, Lindy, Cognigy, Speechmatics
**Automation:** n8n, Zapier, Make.com
**European:** Factorial, Attio, Tinybird, Clarity AI, Travelperk

**Job boards searched:** Ashby, Greenhouse, Lever, Wellfound, Workable, RemoteFront

## 仪表盘 TUI

内置终端仪表盘支持可视化浏览你的求职流水线：

```bash
cd dashboard
go build -o career-dashboard .
./career-dashboard --path ..
```

功能：6 个筛选标签页、4 种排序模式、分组/平铺视图、懒加载预览、内联状态修改。

## 项目结构

```
career-ops/
├── AGENTS.md                    # Canonical agent instructions (all CLIs)
├── CLAUDE.md                    # Claude Code wrapper (imports AGENTS.md)
├── cv.md                        # Your CV (create this)
├── article-digest.md            # Your proof points (optional)
├── config/
│   └── profile.example.yml      # Template for your profile
├── modes/                       # 14 skill modes
│   ├── _shared.md               # Shared context (customize this)
│   ├── oferta.md                # Single evaluation
│   ├── pdf.md                   # PDF generation
│   ├── scan.md                  # Portal scanner
│   ├── batch.md                 # Batch processing
│   └── ...
├── templates/
│   ├── cv-template.html         # ATS-optimized CV template
│   ├── portals.example.yml      # Scanner config template
│   └── states.yml               # Canonical statuses
├── batch/
│   ├── batch-prompt.md          # Self-contained worker prompt
│   └── batch-runner.sh          # Orchestrator script
├── dashboard/                   # Go TUI pipeline viewer
├── data/                        # Your tracking data (gitignored)
├── reports/                     # Evaluation reports (gitignored)
├── output/                      # Generated PDFs (gitignored)
├── fonts/                       # Space Grotesk + DM Sans
├── docs/                        # Setup, customization, architecture
└── examples/                    # Sample CV, report, proof points
```

## 技术栈

![Claude Code](https://img.shields.io/badge/Claude_Code-000?style=flat&logo=anthropic&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![Bubble Tea](https://img.shields.io/badge/Bubble_Tea-FF75B5?style=flat&logo=go&logoColor=white)

- **智能体引擎**：Claude Code 配合自定义技能与模式
- **PDF 渲染**：Playwright/Puppeteer + HTML 模板
- **扫描器**：Playwright + Greenhouse API + WebSearch
- **仪表盘**：Go + Bubble Tea + Lipgloss（Catppuccin Mocha 主题）
- **数据存储**：Markdown 表格 + YAML 配置 + TSV 批量文件

## 其他开源项目

- **[cv-santiago](https://github.com/santifer/cv-santiago)** -- 个人作品集网站（santifer.io），内置 AI 聊天机器人、LLMOps 仪表盘及案例研究。如果你需要一份配合求职展示的作品集，可 Fork 该项目并自定义为你自己的风格。

## 关于作者

我是 Santiago——应用人工智能负责人，前创业者（创建并出售了一家至今仍以我名字运营的公司）。我开发 Career-Ops 是为了管理自己的求职流程。它奏效了：我用它拿下了目前的职位。

我的作品集及其他开源项目 → [santifer.io](https://santifer.io)

## Star 历史

<a href="https://www.star-history.com/?repos=santifer%2Fcareer-ops&type=timeline&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=santifer/career-ops&type=timeline&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=santifer/career-ops&type=timeline&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=santifer/career-ops&type=timeline&legend=top-left" />
 </picture>
</a>

## 免责声明

**career-ops 是一款本地开源工具——并非托管服务。** 使用本软件即表示你知悉并同意以下事项：

1. **你掌控自己的数据。** 你的 CV、联系方式及个人数据均保留在你自己的设备上，且仅直接发送给你选择的 AI 提供商（Anthropic、OpenAI 等）。我们不会收集、存储或访问任何你的数据。
2. **你掌控 AI 行为。** 默认提示词已明确指示 AI 不得自动提交申请，但 AI 模型的行为可能存在不可预测性。如果你修改了提示词或使用其他模型，风险由你自己承担。**提交前请务必亲自审核 AI 生成的所有内容以确保准确性。**
3. **你需遵守第三方服务条款。** 你必须根据所交互的招聘门户（Greenhouse、Lever、Workday、LinkedIn 等）的服务条款使用本工具。请勿使用该工具向雇主发送垃圾信息或压垮 ATS 系统。
4. **不作任何保证。** 评估结果仅为建议，并非绝对事实。AI 模型可能会虚构技能或经验。作者不对就业结果、申请被拒、账户限制或其他任何后果承担责任。

完整详情请参阅 [LEGAL_DISCLAIMER.md](LEGAL_DISCLAIMER.md)。本软件按 [MIT License](LICENSE) 许可条款提供“原样”分发，不提供任何形式的明示或暗示保证。

## 贡献者

<a href="https://github.com/santifer/career-ops/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=santifer/career-ops" />
</a>

使用 Career-Ops 成功入职？[分享你的故事！](https://github.com/santifer/career-ops/issues/new?template=i-got-hired.yml)

## 许可证与商标

代码采用 [MIT](LICENSE) 许可。"career-ops" 名称及品牌受 [商标政策](TRADEMARK.md) 约束——允许社区自由使用，但商业产品命名与背书需保留权利。

## 联系我

[![Website](https://img.shields.io/badge/santifer.io-000?style=for-the-badge&logo=safari&logoColor=white)](https://santifer.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santifer)
[![X](https://img.shields.io/badge/X-000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/santifer)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/8pRpHETxa4)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hi@santifer.io)