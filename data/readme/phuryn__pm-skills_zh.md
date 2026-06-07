![GitHub stars](https://img.shields.io/github/stars/phuryn/pm-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/CONTRIBUTING.md)
[![Companion: pm-skills](https://img.shields.io/badge/companion-pm--brain-blue)](https://github.com/phuryn/pm-brain)

# PM Skills Marketplace：助力更优产品决策的 AI 操作系统

> 涵盖 8 个插件、共 65 项 PM（产品经理）技能与 36 条链式工作流。支持 Claude Code、Cowork 等工具。覆盖从需求发现、战略规划、执行落地到发布推广与增长的全流程。 

![Plugin overview](.docs/images/plugins-overview.webp)

专为 Claude Code 和 Cowork 设计。技能（Skills）兼容其他 AI 助手。

## Start Here

有新想法？ → `/discover`  
需要战略指引？ → `/strategy`  
正在撰写 PRD？ → `/write-prd`  
规划发布计划？ → `/plan-launch`  
定义核心指标？ → `/north-star`

如果本项目对你有帮助，请给仓库点个 ⭐。

## Why PM Skills Marketplace?

通用 AI 只给你文本。PM Skills Marketplace 给你结构化工作流。

每项技能都内置了经过验证的 PM 框架（如需求发现、假设映射、优先级排序、战略规划），并引导你一步步完成。你将日常工作中融入 Teresa Torres、Marty Cagan 和 Alberto Savoia 的方法论严谨性，而不是让好书束之高阁。

结果：做出更好的产品决策，而不仅仅是更快地生成文档。

## How It Works (Skills, Commands, Plugins)

**技能（Skills）**是市场的基础构建块。每项技能为 Claude 提供领域知识、分析框架或针对特定 PM 任务的引导式工作流。部分技能也可作为可复用的基础模块，供多个命令共享。 

当与对话内容相关时，技能会自动加载——无需显式调用。如有需要（例如优先使用技能而非通用知识），你可以通过 `/plugin-name:skill-name` 或 `/skill-name` **强制加载技能**（Claude 会自动添加前缀）。

**命令（Commands）**是由用户触发的链式工作流，通过 `/command-name` 调用。它们将一项或多项技能串联成端到端的流程。例如，`/discover` 将四项技能串联起来：`brainstorm-ideas` → `identify-assumptions` → `prioritize-assumptions` → `brainstorm-experiments`。

**插件（Plugins）**将相关的技能和命令分组为可安装的程序包。每个插件覆盖一个 PM 领域——需求发现、战略规划、执行落地等。安装该市场即一次性获得全部 8 个插件。

![How skills work](.docs/images/how-skills-work.webp)

命令调用技能。部分技能服务于多个命令。部分技能（如 `prioritization-frameworks` 或 `opportunity-solution-tree`）是独立参考模块，Claude 在相关场景下随时调用——无需触发特定命令。

命令设计为可无缝衔接，契合 PM 工作流。任何命令执行完毕后，都会推荐相关的下一步命令——只需跟随提示即可。

## Installation

### Claude Cowork (recommended for non-developers)

1. Open **Customize** (bottom-left)
2. Go to **Browse plugins** → **Personal** → **+**
3. Select **Add marketplace from GitHub**
4. Enter: `phuryn/pm-skills`

All 8 plugins install automatically. You get both commands (`/discover`, `/strategy`, etc.) and skills.

![在 Claude Cowork 中安装 PM Skills](.docs/images/pm-skills-install.gif)

### Claude Code (CLI)

```bash
# Step 1: Add the marketplace
claude plugin marketplace add phuryn/pm-skills

# Step 2: Install individual plugins
claude plugin install pm-toolkit@pm-skills
claude plugin install pm-product-strategy@pm-skills
claude plugin install pm-product-discovery@pm-skills 
claude plugin install pm-market-research@pm-skills 
claude plugin install pm-data-analytics@pm-skills
claude plugin install pm-marketing-growth@pm-skills
claude plugin install pm-go-to-market@pm-skills
claude plugin install pm-execution@pm-skills
```

### Other AI assistants (skills only)

The `skills/*/SKILL.md` files follow the universal skill format and work with any tool that reads it. Commands (`/slash-commands`) are Claude-specific.

| Tool | How to use | What works |
|------|-----------|------------|
| **Gemini CLI** | Copy skill folders to `.gemini/skills/` | 仅技能 |
| **OpenCode** | Copy skill folders to `.opencode/skills/` | 仅技能 |
| **Cursor** | Copy skill folders to `.cursor/skills/` | 仅技能 |
| **Codex CLI** | Copy skill folders to `.codex/skills/` | 仅技能 |
| **Kiro** | Copy skill folders to `.kiro/skills/` | 仅技能 |

```bash
# Example: copy all skills for OpenCode (project-level)
for plugin in pm-*/; do
  mkdir -p .opencode/skills/
  cp -r "$plugin/skills/"* .opencode/skills/ 2>/dev/null
done

# Example: copy all skills for Gemini CLI (global)
for plugin in pm-*/; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## Available Plugins

<details>
<summary><strong>1. pm-product-discovery</strong> —— 创意构思、实验设计、假设验证、OST（机会解决方案树）、用户访谈（13项技能，5个命令）</summary>

**Skills (13):**

- ``brainstorm-ideas-existing`` —— 针对现有产品的多视角创意构思（产品经理、设计师、工程师）
- ``brainstorm-ideas-new`` —— 新产品初期探索的创意构思
- ``brainstorm-experiments-existing`` —— 设计实验以验证现有产品的假设
- ``brainstorm-experiments-new`` —— 为新产品设计精益创业原型（Alberto Savoia）
- ``identify-assumptions-existing`` —— 识别价值、可用性、可行性与实现性方面的风险假设
- ``identify-assumptions-new`` —— 识别包括上市策略、战略和团队在内的 8 大风险类别中的风险假设
- ``prioritize-assumptions`` —— 使用影响×风险矩阵对假设进行优先级排序，并提供实验建议
- ``prioritize-features`` —— 基于影响力、工作量、风险和战略对齐度对功能需求池进行优先级排序
- ``analyze-feature-requests`` —— 按主题和战略契合度分析并分类客户的功能请求
- ``opportunity-solution-tree`` —— 构建机会解决方案树（Teresa Torres）—— 结果 → 机会 → 方案 → 实验
- ``interview-script`` —— 创建结构化用户访谈脚本，包含 JTBD 探询问题
- ``summarize-interview`` —— 将访谈记录总结为 JTBD、满意度信号和待办事项
- ``metrics-dashboard`` —— 设计产品指标仪表盘，含北极星指标、输入指标与告警阈值

**Commands (5):**

- `/discover` —— 完整需求发现周期：创意构思 → 假设映射 → 优先级排序 → 实验设计
- `/brainstorm` —— 多视角创意构思（`ideas|experiments` × `existing|new`）
- `/triage-requests` —— 分析并批量处理功能请求的优先级
- `/interview` —— 准备访谈脚本或总结记录（`prep|summarize`）
- `/setup-metrics` —— 设计产品指标仪表盘

**Examples:**

Skills:
- `我们 AI 写作助手想法的最高风险假设是什么？`
- `帮我为提升用户激活率构建机会解决方案树`
- `对来自企业客户的这 12 个功能请求进行优先级排序 [附带 CSV]`

Commands:
- `/discover 面向远程团队的 AI 驱动会议摘要工具`
- `/brainstorm experiments existing — 我们需要降低入职流程中的流失率`
- `/interview prep — 我们正就采购流程访谈企业买家`

</details>

<details>
<summary><strong>2. pm-product-strategy</strong> —— 愿景、商业模式、定价、竞争格局（12项技能，5个命令）</summary>

产品战略、愿景、商业模式、定价与宏观环境分析。涵盖从愿景塑造到竞品扫描的完整战略工具箱。

**Skills (12):**

- ``product-strategy`` —— 全面的 9 部分产品战略画布（愿景 → 护城河）
- ``startup-canvas`` —— 创业画布：结合产品战略（9部分）+ 商业模式——新产品替代 BMC 和 Lean Canvas 的选择
- ``product-vision`` —— 打造鼓舞人心、可实现且富有情感共鸣的产品愿景
- ``value-proposition`` —— 6 部分 JTBD 价值主张（谁、为什么、之前如何、怎么做、之后怎样、替代方案）
- ``lean-canvas`` —— 面向初创企业和新产品的精益商业模式画布
- ``business-model`` —— 包含全部 9 个模块的商业模式画布
- ``monetization-strategy`` —— 构思 3–5 种变现策略并提供验证实验建议
- ``pricing-strategy`` —— 定价模型、竞品分析、支付意愿与价格弹性
- ``swot-analysis`` —— SWOT 分析与可执行建议
- ``pestle-analysis`` —— 宏观环境：政治、经济、社会、技术、法律、环境
- ``porters-five-forces`` —— 竞争力量分析（同业竞争、供应商、买家、替代品、新进入者）
- ``ansoff-matrix`` —— 跨市场与产品的增长战略映射

**Commands (5):**

- `/strategy` —— 创建完整的 9 部分产品战略画布
- `/business-model` —— 探索商业模式（`lean|full|startup|value-prop|all`）
- `/value-proposition` —— 使用 6 部分 JTBD 模板设计价值主张
- `/market-scan` —— 宏观环境分析：整合 SWOT + PESTLE + Porter's + Ansoff
- `/pricing` —— 设计定价策略，含竞品分析与实验

**Examples:**

Skills:
- `对比我的平台型初创企业该用 Lean Canvas、Business Model Canvas 还是 Startup Canvas？`
- `为非母语英语用户设计 AI 写作助手的价值主张`
- `对项目管理 SaaS 市场运行 Porter's Five Forces 分析`

Commands:
- `/strategy 面向代理机构的 B2B 项目管理工具`
- `/business-model startup — 面向非母语者的 AI 写作工具`
- `/value-proposition 面向企业客户的 SaaS 入职工具`

</details>

<details>
<summary><strong>3. pm-execution</strong> —— PRD、OKR、路线图、Sprint、回顾会、发布说明、干系人管理（15项技能，10个命令）</summary>

日常产品管理：PRD、OKR、路线图、迭代周期、回顾会、发布说明、事前验尸、干系人管理、用户故事与优先级框架。

**Skills (15):**

- ``create-prd`` —— 全面的 8 部分 PRD 模板
- ``brainstorm-okrs`` —— 与公司目标对齐的团队级 OKR
- ``outcome-roadmap`` —— 将功能列表转化为以结果为导向的路线图
- ``sprint-plan`` —— Sprint 规划：含容量估算、故事选择与风险识别
- ``retro`` —— 结构化的 Sprint 回顾会引导
- ``release-notes`` —— 基于工单、PRD 或更新日志生成面向用户的发布说明
- ``pre-mortem`` —— 风险分析，按 Tigers/Paper Tigers/Elephants 分类
- ``stakeholder-map`` —— Power × Interest 网格与定制化沟通计划
- ``summarize-meeting`` —— 会议记录 → 决策 + 待办事项
- ``user-stories`` —— 遵循 3C 原则和 INVEST 标准的用户故事
- ``job-stories`` —— Job Stories：当 [情境]，我想 [动机]，以便 [结果]
- ``wwas`` —— 产品需求项以 Why-What-Acceptance 格式呈现
- ``test-scenarios`` —— 测试场景：正常路径、边界情况、错误处理
- ``dummy-dataset`` —— 逼真的模拟数据集（CSV、JSON、SQL 或 Python）
- ``prioritization-frameworks`` —— 9 种优先级框架参考指南（Opportunity Score, ICE, RICE, MoSCoW, Kano 等）

**Commands (10):**

- `/write-prd` —— 基于功能想法或问题陈述创建 PRD
- `/plan-okrs` —— 构思团队级 OKR
- `/transform-roadmap` —— 将基于功能的路线图转化为以结果为导向
- `/sprint` —— Sprint 生命周期（`plan|retro|release`）
- `/pre-mortem` —— 对 PRD 或发布计划进行事前验尸风险分析
- `/meeting-notes` —— 将会议记录总结为结构化笔记
- `/stakeholder-map` —— 映射干系人并制定沟通计划
- `/write-stories` —— 将功能拆解为需求项（`user|job|wwa`）
- `/test-scenarios` —— 根据用户故事生成测试场景
- `/generate-data` —— 创建逼真的模拟数据集

**Examples:**

Skills:
- `50 个条目的需求池该用哪种优先级框架？`
- `为平台迁移项目映射我们的干系人`
- `Opportunity Score、ICE 和 RICE 有什么区别？`

Commands:
- `/write-prd 减少通知疲劳的智能通知系统`
- `/sprint retro — 这是我们上次迭代的记录`
- `/write-stories job — 将“团队仪表盘”功能拆解为 Job Stories`

</details>

<details>
<summary><strong>4. pm-market-research</strong> —— 用户画像、细分、旅程地图、市场规模估算、竞品分析（7项技能，3个命令）</summary>

用户研究与竞品分析：用户画像、市场细分、旅程地图、市场规模估算、竞品分析与反馈分析。

**Skills (7):**

- ``user-personas`` ———— 基于研究数据创建精炼的用户画像
- ``market-segments`` —— 识别 3–5 个客户细分群体，含人口统计、JTBD 与产品契合度
- ``user-segmentation`` —— 根据行为、JTBD 和需求对反馈数据进行用户分群
- ``customer-journey-map`` ———— 端到端旅程地图：含阶段、触点、情绪与痛点
- ``market-sizing`` —— TAM、SAM、SOM 估算（自上而下与自下而上结合）
- ``competitor-analysis`` —— 竞品优势、劣势与差异化机会分析
- ``sentiment-analysis`` ———— 用户反馈的情感分析与主题提取

**Commands (3):**

- `/research-users` —— 构建画像、细分用户并映射客户旅程
- `/competitive-analysis` —— 分析竞争格局
- `/analyze-feedback` —— 基于用户反馈进行情感分析与分群洞察

**Examples:**

Skills:
- `估算美国市场 AI 代码审查工具的 TAM/SAM/SOM`
- `为我们的电商结账流程创建客户旅程地图`
- `按行为和需求对这批问卷受访者进行细分 [附带 CSV]`

Commands:
- `/research-users 我们拥有健身应用 12 位用户的访谈数据`
- `/competitive-analysis 设计工具领域的 Figma 竞品`
- `/analyze-feedback 这是 Q4 的 200 条 NPS 反馈 [附带文件]`

</details>

<details>
<summary><strong>5. pm-data-analytics</strong> —— SQL 生成、同期群分析、A/B 测试分析（3项技能，3个命令）</summary>

面向产品经理的数据分析：SQL 查询生成、同期群分析与 A/B 测试分析。

**Skills (3):**

- ``sql-queries`` ———— 将自然语言转换为 SQL（BigQuery, PostgreSQL, MySQL）
- ``cohort-analysis`` —— 按同期群划分留存曲线、功能采用率与参与度趋势
- ``ab-test-analysis`` —— 统计显著性、样本量验证，以及上线/延长/终止建议

**Commands (3):**

- `/write-query` —— 将自然语言转换为 SQL 查询
- `/analyze-cohorts` ———— 用户参与度的同期群分析
- `/analyze-test` —— A/B 测试结果分析

**Examples:**

Skills:
- `95% 置信度下，2% MDE 需要多大的样本量？`
- `订阅类应用应追踪哪些留存指标？`

Commands:
- `/write-query 展示 2025 年 Q4 各国月活用户数（BigQuery）`
- `/analyze-test 这是我们结账流程 A/B 测试的结果 [附带 CSV]`
- `/analyze-cohorts 1 月与 2 月注册用户的周留存率对比`

</details>

<details>
<summary><strong>6. pm-go-to-market</strong> —— 滩头市场、ICP、信息传达、增长飞轮、GTM 策略、竞争作战卡（6项技能，3个命令）</summary>

上市策略：滩头市场细分、理想客户画像（ICP）、信息传达、增长飞轮、GTM 动作与竞品作战卡。

**Skills (6):**

- ``gtm-strategy`` ———— 完整 GTM 战略：渠道、信息传达、成功指标与发布计划
- ``beachhead-segment`` —— 识别首个滩头市场细分
- ``ideal-customer-profile`` —— ICP（含人口统计、行为特征、JTBD 与需求）
- ``growth-loops`` ———— 设计可持续增长飞轮
- ``gtm-motions`` ———— 评估 GTM 动作与工具（产品驱动、销售驱动等）
- ``competitive-battlecard`` —— 面向销售的竞品作战卡，含异议处理与获胜策略

**Commands (3):**

- `/plan-launch` —— 从滩头市场到发布计划的完整 GTM 战略
- `/growth-strategy` ———— 设计增长飞轮并评估 GTM 动作
- `/battlecard` —— 创建竞品作战卡

**Examples:**

Skills:
- `开发者效率工具的最佳滩头市场细分是什么？`
- `为带有免费层的 B2B SaaS 设计增长飞轮`
- `定义我们 AI HR 筛选平台的 ICP`

Commands:
- `/plan-launch 面向中型工程团队的 AI 代码审查工具`
- `/battlecard 我们的 CRM vs Salesforce（针对中小企业市场）`
- `/growth-strategy 连接自由职业者与初创公司的双边市场`

</details>

<details>
<summary><strong>7. pm-marketing-growth</strong> —— 营销创意、定位、价值主张、命名、北极星指标（5项技能，2个命令）</summary>

产品营销与增长：营销创意、产品定位、价值主张陈述、产品命名与北极星指标。

**Skills (5):**

- ``marketing-ideas`` ———— 具有渠道与传达策略的创意且高性价比的营销点子
- ``positioning-ideas`` —— 区别于竞品的产品定位
- ``value-prop-statements`` —— 面向营销、销售与入职流程的价值主张陈述
- ``product-name`` ———— 结合品牌价值观与目标受众的产品命名构思
- ``north-star-metric`` —— 北极星指标 + 输入指标，含业务游戏分类

**Commands (2):**

- `/market-product` —— 构思营销创意、定位、价值主张与产品名
- `/north-star` ———— 定义你的北极星指标及支撑性输入指标

**Examples:**

Skills:
- `构思 5 个能区别于 Notion 的定位角度`
- `双边市场的最佳北极星指标是什么？`
- `为销售团队的 Pitch Deck 生成价值主张陈述`

Commands:
- `/market-product 面向电商经理的 B2B 分析仪表盘`
- `/north-star 连接自由职业者与客户的双边市场`

</details>

<details>
<summary><strong>8. pm-toolkit</strong> —— 简历审查、法律文档、校对（4项技能，5个命令）</summary>

核心产品工作之外的 PM 实用工具：简历审查、法律文档与文本校对。

**Skills (4):**

- ``review-resume`` ———— PM 简历审查与定制，遵循 10 大最佳实践（XYZ+S 公式、关键词、结构）
- ``draft-nda`` ———— NDA 起草，含符合司法管辖区的条款
- ``privacy-policy`` —— GDPR/CCPA 合规隐私政策起草
- ``grammar-check`` —— 语法、逻辑与行文流畅度检查及针对性修复

**Commands (5):**

- `/review-resume` —— 全面的 PM 简历审查
- `/tailor-resume` ———— 将简历定制到特定职位描述
- `/draft-nda` ———— 起草 NDA
- `/privacy-policy` —— 起草隐私政策
- `/proofread` ———— 检查语法、逻辑与行文流畅度

**Examples:**

Skills:
- `按最佳实践审查我的 PM 简历 [附带 PDF]`
- `检查这篇产品公告的语法与清晰度`

Commands:
- `/review-resume [附上你的 PM 简历]`
- `/tailor-resume [附上简历 + 粘贴职位描述]`
- `/proofread 这是我们 Q1 投资者更新报告的草稿`

</details>

---

## About

该市场随产品实践与 AI 能力不断演进。

精选技能基于以下作者的工作：

- Teresa Torres — [*Continuous Discovery Habits*](https://www.amazon.com/Continuous-Discovery-Habits-Discover-Products/dp/1736633309/)
- Marty Cagan — [*INSPIRED*](https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507/) 与 [*TRANSFORMED*](https://www.amazon.com/dp/1119697336/)
- Alberto Savoia — [*The Right It*](https://www.amazon.com/Right-Many-Ideas-Yours-Succeed/dp/0062884654)
- Dan Olsen — [*The Lean Product Playbook*](https://www.amazon.com/dp/1118960874/)
- Roger L. Martin — [*Playing to Win*](https://www.amazon.com/Playing-Win-Expanded-Bonus-Articles/dp/B0F25SDYWV/)
- Ash Maurya — [*Running Lean*](https://www.amazon.com/dp/B004J4XGN6/)
- Strategyzer — [*Business Model Generation*](https://www.amazon.com/dp/0470876417/) 与 [*Value Proposition Design*](https://www.amazon.com/dp/1118968050/)
- Christina Wodtke — [*Radical Focus*](https://www.amazon.com/Radical-Focus-Achieving-Important-Objectives/dp/0996006052)
- Anthony W. Ulwick — [*Jobs to Be Done*](https://jobs-to-be-done-book.com/)
- Alistair Croll & Benjamin Yoskovitz — [*Lean Analytics*](https://www.amazon.com/Lean-Analytics-Better-Startup-Faster/dp/1449335675/)
- Sean Ellis — [*Hacking Growth*](https://www.amazon.com/Hacking-Growth-Fastest-Growing-Companies-Breakout/dp/045149721X/)
- Maja Voje — [*Go-To-Market Strategist*](https://gtmstrategist.com/)

由 Paweł Huryn 从 [The Product Compass Newsletter](https://www.productcompass.pm) 精选整理。

## Compose with PM Brain

![PM Brain composes with PM Skills](.docs/images/pm-brain-pm-skills.webp)

[PM Brain](https://github.com/phuryn/pm-brain) 是产品经理的第二大脑。纯 Markdown 文件存放在电脑文件夹中。Claude 在回答前读取它们，回答后写入，每周五自动清理。无需向量数据库，无需云端，无需 Agent 记忆技巧。

## Contributing

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## Known Issue on Windows

如果你的 Cowork 运行不稳定且无法启动虚拟机（见 [claude-code/issues/27010]），请尝试：

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -Command `"if ((Get-Service CoworkVMService).Status -ne 'Running') { Start-Service CoworkVMService }`""

$trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 1) -Once -At (Get-Date)

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "CoworkVMServiceMonitor" `
  -Action $action `
  -Trigger $trigger `
  -Settings $settings `
  -RunLevel Highest `
  -User "SYSTEM"
```

此方法可解决 Windows 上 90% 的问题。
剩余 10%：打开 `services.msc`，手动启动 “Claude” 服务。

## License

MIT —— 详见 [LICENSE](LICENSE)。