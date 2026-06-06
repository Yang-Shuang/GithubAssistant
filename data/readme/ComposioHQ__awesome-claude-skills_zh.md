<h1 align="center">精选 Claude Skills（技能）合集</h1>

<p align="center">
<a href="https://dashboard.composio.dev/login?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeSkills">
  <img width="1280" height="640" alt="Composio banner" src="https://github.com/user-attachments/assets/e91255af-e4ba-4d71-b1a8-bd081e8a234a">
</a>


</p>

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome" />
  </a>
  <a href="https://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square" alt="License: Apache-2.0" />
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

一份全面且精心策划的列表，收录了 1000+ 个面向生产环境、实用高效的 Claude Skills（技能）与插件。它们不仅能用于提升 Claude.ai 和 Claude Code 的生产力，还广泛适用于 Codex、Cursor、Gemini CLI、Antigravity 等代码智能体及其他场景。


> **想要超越单纯文本生成的技能？** Claude 可以发送邮件、创建 Issue（工单）、在 Slack 发帖，并在 1000+ 款应用中执行实际操作。[查看方法 →](./connect/)

---

## 快速上手：将 Claude 连接到 500+ 款应用

**connect-apps** 插件让 Claude 能够执行真实操作——发送邮件、创建 Issue（工单）、在 Slack 发帖。它负责处理身份验证，并在底层通过 Composio 连接 500+ 款应用。

### 1. 安装插件

```bash
claude --plugin-dir ./connect-apps-plugin
```

### 2. 运行初始化

```
/connect-apps:setup
```

当提示时粘贴你的 API Key。（在 [dashboard.composio.dev](https://dashboard.comcomposio.dev/login?utm_source=Github&utm_content=AwesomeSkills) 获取免费密钥）

### 3. 重启并试用

```bash
exit
claude
```

> **想要超越单纯文本生成的技能？** Claude 可以发送邮件、创建 Issue（工单）、在 Slack 发帖，并在 1000+ 款应用中执行实际操作。[查看方法 →](./connect/)

如果你收到该邮件，说明 Claude 已成功连接至 500+ 款应用。

**[查看所有支持的应用 →](https://composio.dev/toolkits)**

---

## 目录

- [什么是 Claude Skills？](#what-are-claude-skills)
- [Skills（技能）](#skills)
  - [文档处理](#document-processing)
  - [开发与代码工具](#development--code-tools)
  - [数据与分析](#data--analysis)
  - [商业与营销](#business--marketing)
  - [沟通与写作](#communication--writing)
  - [创意与媒体](#creative--media)
  - [效率与组织](#productivity--organization)
  - [协作与项目管理](#collaboration--project-management)
  - [安全与系统](#security--systems)
  - [通过 Composio 实现应用自动化](#app-automation-via-composio)
- [快速开始](#getting-started)
- [创建 Skills](#creating-skills)
- [贡献指南](#contributing)
- [资源链接](#resources)
- [许可证](#license)

## 什么是 Claude Skills？

Claude Skills（技能）是可复用的指令包，用于教 AI 智能体如何处理特定类别的任务。每个 Skill 都是一个文件夹，包含一个带有 YAML frontmatter（名称、描述）和 Markdown 说明的 `SKILL.md` 文件，并可选择性地附带脚本、参考文档及资源素材。Anthropic 于 2025 年 10 月推出了该格式，并于同年 12 月将其发布为 [开放标准](https://github.com/anthropics/skills)；目前它已得到 Claude Code、Claude.ai、Claude API、OpenAI Codex、Cursor、Gemini CLI、Antigravity 和 Windsurf 的支持。

Skill 采用渐进式加载机制。在会话开始时，智能体仅能看到每个 Skill 的名称和描述——大约每个 Skill 占用 100 tokens。完整的 `SKILL.md` 正文（通常低于 5,000 tokens）仅在智能体判断该 Skill 与当前任务相关时才会加载。`scripts/` 和 `references/` 中的辅助文件则按需加载。这正是单个智能体能够托管数百个 Skill 而不会撑爆上下文窗口的原因所在。

Skill 不是 MCP Server，也不是 Tool（工具）。MCP 定义了智能体如何连接外部系统——包括身份验证、传输协议和工具发现机制；Tool 是智能体调用的独立函数。Skill 则定义了工作流——在智能体获取所需连接和工具后，具体该做什么、按什么顺序做、以及遵循哪些安全护栏（guardrails）。在生产环境中，这三层架构协同运行：MCP 负责接入，Tool 负责执行动作，Skill 负责规范行为逻辑。

## Skills（技能）

### 文档处理

- [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - 创建、编辑、分析 Word 文档，支持修订模式、批注和格式调整。
- [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) - 提取文本、表格、元数据，合并及注释 PDF 文件。
- [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) - 读取、生成并调整幻灯片、版式和模板。
- [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) - 电子表格操作：公式、图表和数据转换。
- [Markdown to EPUB Converter](https://github.com/smerchek/claude-epub-skill) - 将 Markdown 文档和对话摘要转换为专业的 EPUB 电子书格式。*By [@smerchek](https://github.com/smerchek)*
- [Master Claude for Legal](https://github.com/sboghossian/master-claude-for-legal) - 面向法律团队的技能包。包含 NDA（保密协议）审查、多方版本比对、引用验证、会议简报，以及周五通讯状态综合模式等。附带 10 份参考文档（特权、验证、长文档、业务领域）和 3 套律所模板。基于 Anthropic 公开的“法律团队”网络研讨会数据集构建。*By [@sboghossian](https://github.com/sboghossian)*

### 开发与代码工具

- [artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) - 一套用于创建复杂多组件 claude.ai HTML 工件的工具集，采用现代前端技术（React、Tailwind CSS、shadcn/ui）。
- [aws-skills](https://github.com/zxkane/aws-skills) - AWS 开发技能，遵循 CDK 最佳实践、成本优化 MCP Server，以及无服务器/事件驱动架构模式。
- [building-blog](https://github.com/BuildShipGrowRepeat/nextjs-sanity-blog-skill) - 通过 40 个问题问卷、一页纸计划和 20 章节规范，为 Next.js + Sanity 站点添加 SEO 优先且支持 i18n（国际化）的博客功能。内置通过 Gemini 3 Pro Image (Nano Banana Pro) 生成 AI Hero 图片的生成器。*By [@BuildShipGrowRepeat](https://github.com/BuildShipGrowRepeat)*
- [Changelog Generator](./changelog-generator/) - 自动从 Git 提交记录中生成面向用户的更新日志，通过分析历史记录将技术 Commit 转化为客户友好的发布说明。
- [Chrome Relay](https://chrome-relay.kushalsm.com/) - 通过本地 CLI 桥接驱动用户已打开的 Chrome 会话——包括 Cookie、SSO（单点登录）、扩展程序和 localhost。是 Playwright Browser Automation 的真实 Chrome 替代方案；通过 `npx skills add chrome-relay` + [Chrome Web Store 插件](https://chromewebstore.google.com/detail/chrome-relay/cpdiapbifblhlcpnmlmfpgfjlacebokb) 安装。无需远程中继，无需 Playwright 夹具，无需 MCP Server。
- [Claude Code Terminal Title](https://github.com/bluzername/claude-code-terminal-title) - 为每个 Claud-Code 终端窗口分配动态标题，描述当前正在进行的工作，让你不再迷失于各个窗口的任务状态。
- [Connect](./connect/) - 将 Claude 连接到任意应用。发送邮件、创建 Issue（工单）、发布消息、更新数据库——在 Gmail、Slack、GitHub、Notion 及 1000+ 服务中执行真实操作。
- [D3.js Visualization](https://github.com/chrisvoncsefalvay/claude-d3js-skill) - 教 Claude 生成 D3 图表和交互式数据可视化效果。*By [@chrisvoncsefalvay](https://github.com/chrisvoncsefalvay)*
- [FFUF Web Fuzzing](https://github.com/jthack/ffuf_claude_skill) - 集成 ffuf 网页模糊测试工具，让 Claude 能够运行 fuzzing（模糊测试）任务并分析漏洞结果。*By [@jthack](https://github.com/jthack)*
- [finishing-a-development-branch](https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch) - 通过提供清晰选项和处理选定工作流，指导开发工作的收尾完成。
- [Full-Page Screenshot](https://github.com/LewisLiu007/full-page-screenshot) - 通过 Chrome DevTools Protocol 捕获网页全屏截图，零依赖。*By [@LewisLiu007](https://github.com/LewisLiu007)*
- [great_cto](https://github.com/avelikiy/great_cto) - Claude Code 插件：包含 7 个专业化子智能体（技术主管、高级开发、QA 工程师、安全官、DevOps、L3 支持、项目审计员），编排完整的 SDLC（软件开发生命周期）流水线——架构设计、TDD（测试驱动开发）、12 维度代码审查、QA、安全审计、部署。自动检测 11 种项目架构类型，内置 13 项合规框架（GDPR/PCI-DSS/HIPAA/SOC2/ISO 27001），具备从每次事故中学习并自我优化的知识层。*By [@avelikiy](https://github.com/avelikiy)*
- [iOS Simulator](https://github.com/conorluddy/ios-simulator-skill) - 使 Claude 能够与 iOS 模拟器交互，用于测试和调试 iOS 应用。*By [@conorluddy](https://github.com/conorluddy)*
- [jules](https://github.com/sanjay3290/ai-skills/tree/main/skills/jules) - 将编码任务委派给 Google Jules AI 智能体，用于 GitHub 仓库的异步 Bug 修复、文档编写、测试及功能实现。*By [@sanjay3290](https://github.com/sanjay3290)*
- [LangSmith Fetch](./langsmith-fetch/) - 通过自动获取和分析 LangSmith Studio 中的执行轨迹来调试 LangChain 和 LangGraph 智能体。这是面向 Claude Code 的首款 AI 可观测性技能。*By [@OthmanAdi](https://github.com/OthmanAdi)*
- [lean-ctx](https://github.com/yvgude/lean-ctx) - MCP Server 与上下文运行时，专为 AI 编码智能体设计：支持会话缓存、AST（抽象语法树）感知压缩，以及 90+ Shell 模式以减少 Token 消耗。支持 Claude Code、Cursor、Copilot 等集成。使用 `lean-ctx init --agent claude-code` 安装 Claude Code 技能；文档见 [leanctx.com](https://leanctx.com)。*By [@yvgude](https://github.com/yvgude)*
- [MCP Builder](./mcp-builder/) - 指导创建高质量的 MCP（模型上下文协议）Server，用于通过 Python 或 TypeScript 将外部 API 和服务集成到 LLM 中。
- [move-code-quality-skill](https://github.com/1NickPappas/move-code-quality-skill) - 对照官方 Move Book 代码质量检查清单，分析 Move 语言包是否符合 Move 2024 Edition 规范及最佳实践。
- [OpenWeb](https://github.com/openweb-org/openweb) - Agent（智能体）原生的网站访问方式。调用与网站相同的 API（JSON 输入，JSON 输出），按请求自动解析身份验证（Cookie、JWT、CSRF、签名）。已内置支持 90+ 站点。*By [@openweb-org](https://github.com/openweb-org)*
- [overkill](https://github.com/santiago-vargas-de-kruijf/claude-overkill) - 展示被讨论方案的先进、极致替代方案——高级数据结构、分布式系统算法、小众框架、设计模式及前沿工具，每项均在校准过的复杂度量表上排名，并附带学习链接和适用场景说明。*By [@santiago-vargas-de-kruijf](https://github.com/santiago-vargas-de-kruijf)*
- [Playwright Browser Automation](https://github.com/lackeyjb/playwright-skill) - 由模型调用的 Playwright 自动化方案，用于测试和验证 Web 应用。*By [@lackeyjb](https://github.com/lackeyjb)*
- [prompt-engineering](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/customaize-agent/skills/prompt-engineering) - 教授知名的提示词工程技巧与模式，包括 Anthropic 最佳实践及智能体说服原则。
- [pypict-claude-skill](https://github.com/omkamal/pypict-claude-skill) - 使用 PICT（成对独立组合测试）为需求或代码设计全面的测试用例，生成具有成对覆盖率的优化测试套件。
- [reddit-fetch](https://github.com/ykdojo/claude-code-tips/tree/main/skills/reddit-fetch) - 当 WebFetch 被阻止或返回 403 错误时，通过 Gemini CLI 抓取 Reddit 内容。
- [Septim Agents Pack](https://septimlabs.com/tools/agents?utm_source=awesome-claude-skills&utm_medium=awesome-list&utm_campaign=oss-backlink) - 10 个具名 Claude Code 子智能体（Atlas, Luca, Canon, Ember, Tally, Nova, Ward, Mira, Juno, Pip），覆盖规划、架构、品牌、营销、财务、设计、法律、客户支持、研究和协调。放入 `.claude/agents/` 即可使用。*By [@septimlabs-code](https://github.com/septimlabs-code)*
- [Skill Creator](./skill-creator/) - 提供创建高效 Claude Skills（技能）的指导，通过专业知识、工作流和工具集成来扩展能力。
- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) - 在几分钟内将任意文档网站自动转换为 Claude AI 技能。*By [@yusufkaraaslan](https://github.com/yusufkaraaslan)*
- [software-architecture](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd/skills/software-architecture) - 实现包括 Clean Architecture（整洁架构）、SOLID 原则及全面软件设计最佳实践在内的设计模式。
- [subagent-driven-development](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/sadd/skills/subagent-driven-development) - 为独立任务分派独立的子智能体，并在迭代间设置代码审查检查点，以实现快速且受控的开发流程。
- [test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) - 在实现任何功能或修复 Bug 时、编写实现代码前使用此技能。
- [using-git-worktrees](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/) - 创建隔离的 Git worktree（工作树），具备智能目录选择与安全验证功能。
- [Webapp Testing](./webapp-testing/) - 使用 Playwright 测试本地 Web 应用，用于验证前端功能、调试 UI 行为及捕获截图。

### 数据与分析

- [CSV Data Summarizer](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) - 自动分析 CSV 文件并生成包含可视化图表的综合洞察报告，无需用户提示即可执行。*By [@coffeefuelbump](https://github.com/coffeefuelbump)*
- [deep-research](https://github.com/sanjay3290/ai-skills/tree/main/skills/deep-research) - 使用 Gemini Deep Research Agent 执行自主多步研究，适用于市场分析、竞争格局梳理及文献综述。*By [@sanjay3290](https://github.com/sanjay3290)*
- [postgres](https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres) - 对 PostgreSQL 数据库执行安全的只读 SQL 查询，支持多连接及纵深防御安全机制。*By [@sanjay3290](https://github.com/sanjay3290)*
- [recursive-research](https://github.com/Anjos2/recursive-research) - 跨任意领域（科学、技术、商业、艺术、人文）进行博士级递归研究，采用来源分级、WDM + Munger 逆向思维实现自主决策，并支持磁盘断点续传以应对上下文压缩。*By [@Anjos2](https://github.com/Anjos2)*
- [root-cause-tracing](https://github.com/obra/superpowers/tree/main/skills/root-cause-tracing) - 当错误发生在执行深处且需要回溯查找原始触发器时使用此技能。

### 商业与营销

- [Brand Build Skills](https://github.com/rampstackco/claude-skills) - 涵盖完整网站生命周期的 59 项技能库：品牌、设计、内容、SEO（搜索引擎优化）、开发、运维、增长及研究。支持多技术栈，内置基于 Ahrefs MCP 的 SEO 审计套件。附带元技能用于编写你自己的技能。*By [@rampstackco](https://github.com/rampstackco)*
- [Brand Guidelines](./brand-guidelines/) - 将 Anthropic 官方品牌色彩与排版应用于工件中，确保视觉身份一致性与专业设计标准。
- [Competitive Ads Extractor](./competitive-ads-extractor/) - 从广告库中提取并分析竞争对手的广告内容，以理解引发共鸣的信息传递与创意策略。
- [Domain Name Brainstormer](./domain-name-brainstormer/) - 生成创意域名建议，并在多个 TLD（顶级域名）下检查可用性，包括 .com、.io、.dev 和 .ai 后缀。
- [Internal Comms](./internal-comms/) - 协助撰写内部通讯，包括 3P 更新、公司通讯简报、FAQ、状态报告及项目进度更新，支持自定义企业格式。
- [Lead Research Assistant](./lead-research-assistant/) - 通过分析你的产品、搜索目标公司及提供可执行的触达策略来识别并筛选高质量潜在客户（Leads）。

### 沟通与写作

- [article-extractor](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/article-extractor) - 从网页提取完整文章正文及元数据。
- [brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming) - 通过结构化提问和替代方案探索，将粗糙的想法转化为成熟的设计方案。
- [Content Research Writer](./content-research-writer/) - 协助撰写高质量内容，包括开展研究、添加引用、优化开头钩子（hooks）并提供逐节反馈。
- [family-history-research](https://github.com/emaynard/claude-family-history-research-skill) - 提供家族历史与谱系学研究项目的规划辅助。
- [Meeting Insights Analyzer](./meeting-insights-analyzer/) - 分析会议转录文本以揭示行为模式，包括回避冲突倾向、发言比例、填充词使用及领导风格。
- [NotebookLM Integration](https://github.com/PleasePrompto/notebooklm-skill) - 让 Claude Code 直接与 NotebookLM 对话，基于上传文档生成有据可查的答案。*By [@PleasePrompto](https://github.com/PleasePrompto)*
- [Twitter Algorithm Optimizer](./twitter-algorithm-optimizer/) - 利用 Twitter 开源算法洞察分析与优化推文以获取最大曝光度。重写并编辑推文以提升互动率与可见性。

### 创意与媒体

- [anydesign](https://github.com/uxKero/anydesign) - 分析任意图片、URL 或 Figma 文件，生成结构化的 `design.md`（含完整设计系统、组件清单及重构笔记）——可无缝迁移至 v0、Lovable、Cursor 或任何 AI 构建器。*By [@uxKero](https://github.com/uxKero)*
- [Canvas Design](./canvas-design/) - 运用设计理念与美学原则，在 PNG 和 PDF 文档中创作精美的视觉艺术作品（海报、设计与静态插图）。
- [imagen](https://github.com/sanjay3290/ai-skills/tree/main/skills/imagen) - 使用 Google Gemini 图像生成 API 创建图片，适用于 UI 原型图、图标、插画及视觉素材。*By [@sanjay3290](https://github.com/sanjay3290)*
- [Image Enhancer](./image-enhancer/) - 通过提升分辨率、清晰度和锐度来改善图片与截图质量，适用于专业演示文稿与技术文档。
- [Slack GIF Creator](./slack-gif-creator/) - 为 Slack 创建优化的动态 GIF，包含尺寸约束校验器及可组合的动画基元（primitives）。
- [Theme Factory](./theme-factory/) - 将专业的字体与色彩主题应用于工件中（包括幻灯片、文档、报告及 HTML 落地页），内置 10 套预设主题。
- [Video Downloader](./video-downloader/) - 从 YouTube 等平台下载视频，支持离线观看、编辑或归档，兼容多种格式与画质选项。
- [youtube-transcript](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript) - 抓取 YouTube 视频字幕并准备摘要。
- [swiftui-design-skill](https://github.com/wholiver/swiftui-design-skill) - SwiftUI 前端设计 skill —— 反 AI Slop（粗制滥造）六条铁律、设计方向顾问、品牌资产协议、五维评审。支持 Claude Code / Cursor / Codex / OpenCode 等全部 AI agent 平台。 *By [@wholiver](https://github.com/wholiver)*
- [Pixelbin-Media-Generation](https://github.com/anandpareek-hub/pixelbin-claude-skill) - 使用 85+ API 组合生成与编辑图片/视频，并构建视觉吸引力强的网站页面

### 效率与组织

- [File Organizer](./file-organizer/) - 通过理解上下文、查找重复文件及建议更优组织结构来智能整理文件与文件夹。
- [Invoice Organizer](./invoice-organizer/) - 自动整理发票与收据以用于税务申报，通过读取文件、提取信息并统一重命名实现自动化。
- [kaizen](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/kaizen/skills/kaizen) - 应用持续改进方法论（基于日本 Kaizen 哲学与精益方法），结合多种分析视角。
- [n8n-skills](https://github.com/haunchen/n8n-skills) - 使 AI 助手能够直接理解并操作 n8n 工作流。
- [Raffle Winner Picker](./raffle-winner-picker/) - 从列表、电子表格或 Google Sheets 中随机抽取中奖者，适用于抽奖活动，采用密码学安全随机算法。
- [solo-skills](https://github.com/rockscy/solo-skills) - 面向独立创始人和 Indie Dev（个人开发者）的 7 项双语（EN+中文）技能：发布推文、客户邮件、决策框架及事后复盘（Postmortems）。每项技能均包含明确的“何时不使用”部分。
- [Tailored Resume Generator](./tailored-resume-generator/) - 分析职位描述并生成定制化简历，突出相关经验、技能与成就，以最大化面试机会。
- [ship-learn-next](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/ship-learn-next) - 帮助迭代确定下一步构建方向或学习重点的技能，基于反馈循环机制运行。
- [tapestry](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/tapestry) - 将相关文档相互链接并总结为知识网络。

### 协作与项目管理

- [git-pushing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/git-pushing) - 自动化 Git 操作及仓库交互流程。
- [google-workspace-skills](https://github.com/sanjay3290/ai-skills/tree/main/skills) - Google Workspace 集成套件：涵盖 Gmail、Calendar（日历）、Chat、Docs、Sheets、Slides 和 Drive，支持跨平台 OAuth。*By [@sanjay3290](https://github.com/sanjay3290)*
- [mercury-mcp](https://www.teamoffsite.ai/proton/docs/skill) - Mercury (Proton) MCP 工具速查表。向智能体队友发送消息、管理线程、创建任务及在协作团队间调度自动化流程。*By [Mercury](https://mercury.build)*
- [outline](https://github.com/sanjay3290/ai-skills/tree/main/skills/outline) - 搜索、阅读、创建及管理 Outline Wiki 实例（云端或自托管）中的文档。*By [@sanjay3290](https://github.com/sanjay3290)*
- [review-implementing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/review-implementing) - 评估代码实施方案并与规范对齐。
- [test-fixing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/test-fixing) - 检测失败的测试用例并提出补丁或修复方案。

### 安全与系统

- [computer-forensics](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/computer-forensics) - 数字取证分析与调查技术。
- [file-deletion](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/file-deletion) - 安全的文件删除与数据擦除方法。
- [metadata-extraction](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/metadata-extraction) - 提取并分析文件元数据以用于取证目的。
- [threat-hunting-with-sigma-rules](https://github.com/jthack/threat-hunting-with-sigma-rules-skill) - 使用 Sigma 检测规则进行威胁狩猎与安全事件分析。

### 辅助技术

- [ASD-AuDHD-PAI-Skills](https://github.com/emory/ASD-AuDHD-PAI-Skills) - 全新技能集，首项技能 [pda-reframing](https://github.com/emory/ASD-AuDHD-PAI-Skills/blob/main/Skills/pda-reframing/SKILL.md) 可重构请求或决策以克服自闭症谱系障碍中的持续性需求回避（PDA）症状，或帮助患有 ADHD（注意力缺陷多动障碍）且难以启动任务的人群对齐目标。

### 通过 Composio 实现应用自动化

基于 [Rube MCP (Composio)](https://composio.dev) 的 78 款 SaaS 应用预置工作流技能。每项技能均包含工具序列、参数指导、已知陷阱及快速参考表——全部使用从 Composio API 发现的实际工具标识符（tool slugs）。

**CRM 与销售**
- [Close Automation](./close-automation/) - 自动化 Close CRM：线索、联系人、商机、活动及销售漏斗。
- [HubSpot Automation](./hubspot-automation/) - 自动化 HubSpot CRM：联系人、交易、公司、工单及邮件互动数据。
- [Pipedrive Automation](./pipedrive-automation/) - 自动化 Pipedrive：交易、联系人、组织、活动及销售漏斗。
- [Salesforce Automation](./salesforce-automation/) - 自动化 Salesforce：对象、记录、SOQL 查询及批量操作。
- [Zoho CRM Automation](./zoho-crm-automation/) - 自动化 Zoho CRM：线索、联系人、交易、账户及模块。

**项目管理**
- [Asana Automation](./asana-automation/) - 自动化 Asana：任务、项目、区块、分配人及工作区。
- [Basecamp Automation](./basecamp-automation/) - 自动化 Basecamp：待办清单、消息、人员、群组及项目。
- [ClickUp Automation](./clickup-automation/) - 自动化 ClickUp：任务、列表、空间、目标及时间追踪。
- [Jira Automation](./jira-automation/) - 自动化 Jira：Issue（工单）、项目、看板、Sprint 及 JQL 查询。
- [Linear Automation](./linear-automation/) - 自动化 Linear：Issue（工单）、项目、周期、团队及工作流。
- [Monday Automation](./monday-automation/) - 自动化 Monday.com：看板、项目项、列、群组及工作区。
- [Notion Automation](./notion-automation/) - 自动化 Notion：页面、数据库、区块、评论及搜索功能。
- [Todoist Automation](./todoist-automation/) - 自动化 Todoist：任务、项目、区块、标签及过滤器。
- [Trello Automation](./trello-automation/) - 自动化 Trello：看板、卡片、列表、成员及检查清单。
- [Wrike Automation](./wrike-automation/) - 自动化 Wrike：任务、文件夹、项目、评论及工作流。

**沟通**
- [Discord Automation](./discord-automation/) - 自动化 Discord：消息、频道、服务器、角色及表情反应。
- [Intercom Automation](./intercom-automation/) - 自动化 Intercom：对话、联系人、公司、工单及知识库文章。
- [Microsoft Teams Automation](./microsoft-teams-automation/) - 自动化 Teams：消息、频道、团队、聊天及会议。
- [Slack Automation](./slack-automation/) - 自动化 Slack：消息、频道、搜索、表情反应、线程及日程安排。
- [Telegram Automation](./telegram-automation/) - 自动化 Telegram：消息、会话、媒体、群组及机器人。
- [WhatsApp Automation](./whatsapp-automation/) - 自动化 WhatsApp：消息、媒体、模板、群组及商业资料。

**电子邮件**
- [Gmail Automation](./gmail-automation/) - 自动化 Gmail：发送/回复、搜索、标签、草稿及附件管理。
- [Outlook Automation](./outlook-automation/) - 自动化 Outlook：邮件、文件夹、联系人及日历集成。
- [Postmark Automation](./postmark-automation/) - 自动化 Postmark：事务性邮件、模板、服务器及投递统计。
- [SendGrid Automation](./sendgrid-automation/) - 自动化 SendGrid：邮件、模板、联系人、列表及活动统计。

**代码与 DevOps**
- [Bitbucket Automation](./bitbucket-automation/) - 自动化 Bitbucket：仓库、PR（合并请求）、分支、Issue（工单）及工作区。
- [CircleCI Automation](./circleci-automation/) - 自动化 CircleCI：流水线、工作流、任务及项目配置。
- [Datadog Automation](./datadog-automation/) - 自动化 Datadog：监控器、仪表盘、指标、事故及告警。
- [GitHub Automation](./github-automation/) - 自动化 GitHub：Issue（工单）、PR、仓库、分支、Actions 及代码搜索。
- [GitLab Automation](./gitlab-automation/) - 自动化 GitLab：Issue（工单）、MR、项目、流水线及分支管理。
- [PagerDuty Automation](./pagerduty-automation/) - 自动化 PagerDuty：事故、服务、排班表、升级策略及值班安排。
- [Render Automation](./render-automation/) - 自动化 Render：服务、部署及项目管理。
- [Sentry Automation](./sentry-automation/) - 自动化 Sentry：Issue（工单）、事件、项目、版本发布及告警。
- [Supabase Automation](./supabase-automation/) - 自动化 Supabase：SQL 查询、表结构、边缘函数及存储管理。
- [Vercel Automation](./vercel-automation/) - 自动化 Vercel：部署、项目、域名、环境变量及日志查看。

**存储与文件**
- [Box Automation](./box-automation/) - 自动化 Box：文件、文件夹、搜索、分享、协作及电子签名请求。
- [Dropbox Automation](./dropbox-automation/) - 自动化 Dropbox：文件、文件夹、搜索、分享及批量操作。
- [Google Drive Automation](./google-drive-automation/) - 自动化 Google Drive：上传、下载、搜索、共享及文件整理。
- [OneDrive Automation](./one-drive-automation/) - 自动化 OneDrive：文件、文件夹、搜索、共享、权限管理及版本控制。

**电子表格与数据库**
- [Airtable Automation](./airtable-automation/) - 自动化 Airtable：记录、表、工作区、视图及字段管理。
- [Coda Automation](./coda-automation/) - 自动化 Coda：文档、表格、行、公式及自动化规则。
- [Google Sheets Automation](./googlesheets-automation/) - 自动化 Google Sheets：单元格读写、格式设置、公式及批量操作。

**日历与日程安排**
- [Cal.com Automation](./cal-com-automation/) - 自动化 Cal.com：事件类型、预约、可用性及日程调度。
- [Calendly Automation](./calendly-automation/) - 自动化 Calendly：活动、参与者、事件类型、邀请链接及可用性管理。
- [Google Calendar Automation](./google-calendar-automation/) - 自动化 Google Calendar：事件、参会者、空闲/忙碌状态及重复日程。
- [Outlook Calendar Automation](./outlook-calendar-automation/) - 自动化 Outlook Calendar：事件、参会者、提醒及重复日程安排。

**社交媒体**
- [Instagram Automation](./instagram-automation/) - 自动化 Instagram：帖子、快拍、评论、媒体素材及商业洞察数据。
- [LinkedIn Automation](./linkedin-automation/) - 自动化 LinkedIn：帖子、个人主页、公司页、图片及评论管理。
- [Reddit Automation](./reddit-automation/) - 自动化 Reddit：帖子、评论、子版块、投票及内容审核。
- [TikTok Automation](./tiktok-automation/) - 自动化 TikTok：视频上传、查询及创作者账号管理。
- [Twitter Automation](./twitter-automation/) - 自动化 Twitter/X：推文、搜索、用户、列表及互动数据。
- [YouTube Automation](./youtube-automation/) - 自动化 YouTube：视频、频道、播放列表、评论及订阅管理。

**营销与邮件营销**
- [ActiveCampaign Automation](./activecampaign-automation/) - 自动化 ActiveCampaign：联系人、交易、活动、列表及自动化流程。
- [Brevo Automation](./brevo-automation/) - 自动化 Brevo：联系人、电子邮件活动、事务性邮件及订阅者列表。
- [ConvertKit Automation](./convertkit-automation/) - 自动化 ConvertKit (Kit)：订阅者、标签、序列、广播及表单。
- [Klaviyo Automation](./klaviyo-automation/) - 自动化 Klaviyo：用户档案、列表、细分、活动及事件追踪。
- [Mailchimp Automation](./mailchimp-automation/) - 自动化 Mailchimp：受众、活动、模板、细分及报告生成。

**支持与客服**
- [Freshdesk Automation](./freshdesk-automation/) - 自动化 Freshdesk：工单、联系人、客服人员、群组及快捷回复。
- [Freshservice Automation](./freshservice-automation/) - 自动化 Freshservice：工单、资产、变更、问题及服务目录管理。
- [Help Scout Automation](./helpdesk-automation/) - 自动化 Help Scout：对话、客户、邮箱及标签分类。
- [Zendesk Automation](./zendesk-automation/) - 自动化 Zendesk：工单、用户、组织、搜索功能及宏命令（Macros）。

**电子商务与支付**
- [Shopify Automation](./shopify-automation/) - 自动化 Shopify：商品、订单、客户、库存及 GraphQL 查询。
- [Square Automation](./square-automation/) - 自动化 Square：支付、客户、目录、订单及门店管理。
- [Stripe Automation](./stripe-automation/) - 自动化 Stripe：扣款、客户、商品、订阅及退款处理。

**设计与协作**
- [Canva Automation](./canva-automation/) - 自动化 Canva：设计稿、模板、素材库、文件夹及品牌套件管理。
- [Confluence Automation](./confluence-automation/) - 自动化 Confluence：页面、空间、搜索（CQL）、标签及版本控制。
- [DocuSign Automation](./docusign-automation/) - 自动化 DocuSign：信封、模板、电子签名及文档管理流程。
- [Figma Automation](./figma-automation/) - 自动化 Figma：文件、组件、评论、项目及团队管理。
- [Miro Automation](./miro-automation/) - 自动化 Miro：画板、便利贴、图形、连接线及项目项管理。
- [Webflow Automation](./webflow-automation/) - 自动化 Webflow：CMS 集合、内容项、站点发布及资产管理。

**分析与数据**
- [Amplitude Automation](./amplitude-automation/) - 自动化 Amplitude：事件、用户群（Cohorts）、属性及分析查询。
- [Google Analytics Automation](./google-analytics-automation/) - 自动化 Google Analytics：报表、维度、指标及账户管理。
- [Mixpanel Automation](./mixpanel-automation/) - 自动化 Mixpanel：事件、漏斗、用户群、注释及 JQL 查询。
- [PostHog Automation](./posthog-automation/) - 自动化 PostHog：事件、用户、功能标志（Feature Flags）、洞察数据及注释。
- [Segment Automation](./segment-automation/) - 自动化 Segment：数据源、目的地、追踪代码及仓库连接管理。

**人力资源与员工管理**
- [BambooHR Automation](./bamboohr-automation/) - 自动化 BambooHR：员工档案、休假申请、报表及目录管理。

**自动化平台**
- [Make Automation](./make-automation/) - 自动化 Make (Integromat)：场景（Scenarios）、连接及执行任务管理。

**Zoom 与会议**
- [Zoom Automation](./zoom-automation/) - 自动化 Zoom：会议、录制文件、参会者、网络研讨会及报表生成。

## 快速开始

### 在 Claude.ai 中使用 Skills

1. 点击聊天界面中的技能图标（🧩）。
2. 从市场添加 Skills，或上传自定义技能包。
3. Claude 会根据你的任务自动激活相关 Skill。

### 在 Claude Code 中使用 Skills

1. 将技能放入 `~/.config/claude-code/skills/`：
   ```bash
   mkdir -p ~/.config/claude-code/skills/
   cp -r skill-name ~/.config/claude-code/skills/
   ```

2. 验证技能元数据：
   ```bash
   head ~/.config/claude-code/skills/skill-name/SKILL.md
   ```

3. 启动 Claude Code：
   ```bash
   claude
   ```

4. Skill 将自动加载，并在相关时激活。

### 通过 API 使用 Skills

使用 Claude Skills API 以编程方式加载和管理技能：

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    skills=["skill-id-here"],
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

详见 [Skills API 文档](https://docs.claude.com/en/api/skills-guide)。

## 创建 Skills（技能）

### Skill 结构

每个 Skill 都是一个包含 `SKILL.md` 文件的文件夹，其中带有 YAML frontmatter：

```
skill-name/
├── SKILL.md          # 必填：技能说明与元数据
├── scripts/          # 可选：辅助脚本
├── templates/        # 可选：文档模板
└── resources/        # 可选：参考文件
```

### 基础 Skill 模板

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it.
---

# My Skill Name

Detailed description of the skill's purpose and capabilities.

## When to Use This Skill

- Use case 1
- Use case 2
- Use case 3

## Instructions

[Detailed instructions for Claude on how to execute this skill]

## Examples

[Real-world examples showing the skill in action]
```

### Skill 最佳实践

- 聚焦具体、可重复的任务场景
- 包含清晰的示例与边界情况处理说明
- 为 Claude 编写指令，而非最终用户
- 在 Claude.ai、Claude Code 和 API 中交叉测试
- 记录前置条件与依赖项
- 提供错误处理指导

## 贡献指南

我们欢迎你的贡献！请阅读我们的 [贡献指南](CONTRIBUTING.md)，了解以下详情：

- 如何提交新技能
- 技能质量标准
- Pull Request 流程
- 行为准则（Code of Conduct）

### 快速贡献步骤

1. 确保你的 Skill 基于真实使用场景
2. 检查现有 Skills 中是否已有重复项
3. 遵循 Skill 结构模板进行编写
4. 跨平台测试你的技能包
5. 提交附带清晰说明的 Pull Request

## 资源链接

### 官方文档

- [Claude Skills Overview](https://www.anthropic.com/news/skills) - 官方公告与功能介绍
- [Skills User Guide](https://support.claude.com/en/articles/12512180-using-skills-in-claude) - Claude 中如何使用技能
- [Creating Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) - 技能开发指南
- [Skills API Documentation](https://docs.claude.com/en/api/skills-guide) - API 集成指南
- [Agent Skills Blog Post](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - 工程深度解析

### 社区资源

- [Anthropic Skills Repository](https://github.com/anthropics/skills) - 官方示例技能库
- [Claude Community](https://community.anthropic.com) - 与其他用户讨论技能使用心得
- [Skills Marketplace](https://claude.ai/marketplace) - 发现并分享社区技能

### 灵感与用例参考

- [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code) - 50 种使用 Claude Code 的方式
- [Notion Skills](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0) - Notion 集成技能示例
- [Top Claude Skills](https://composio.dev/content/top-claude-skills)


## 加入社区

- [加入我们的 Discord](https://discord.com/invite/composio) - 与其他构建 Claude Skills 的开发者交流
- [在 Twitter/X 上关注](https://x.com/composio) - 获取最新技能与功能更新
- 有疑问？请发送邮件至 [support@composio.dev](mailto:support@composio.dev)

---

<p align="center">
  <b>加入 20,000+ 位开发者，共同构建可落地的智能体应用</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>

## 许可证

本仓库采用 Apache License 2.0 开源协议。

各个独立技能可能拥有不同的许可证——请查阅每个 Skill 文件夹内的具体许可信息。

---

**注意**：Claude Skills 兼容 Claude.ai、Claude Code 及 Claude API。一旦你创建了一个 Skill，它即可在所有平台上无缝迁移，让你在使用 Claude 的每个环境中保持工作流一致。

- [AgentsKB](https://agentskb.com) - 用研究驱动的答案升级你的 AI。我们已完成调研，确保你的 AI 首次调用即给出正确答案。