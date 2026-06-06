# AI Agent 营销技能集

一套专注于营销任务的 AI Agent 技能集合。专为希望借助 AI 编程助手进行转化优化、文案撰写、SEO、数据分析和增长工程的技术型营销人员与创始人打造。兼容 Claude Code、OpenAI Codex、Cursor、Windsurf，以及支持 [Agent Skills 规范](https://agentskills.io) 的任何 Agent。

由 [Corey Haines](https://corey.co?ref=marketingskills) 开发。需要实操指导？请查看 [Conversion Factory](https://conversionfactory.co?ref=marketingskills) —— Corey 的转化优化、落地页与增长策略代理机构。想深入了解营销知识？订阅 [Swipe Files](https://swipefiles.com?ref=marketingskills)。想要一个能运用这些技能自主担任你 CMO（首席营销官）的 AI Agent？试试 [Magister](https://magistermarketing.com?ref=marketingskills)。

刚接触终端和编程助手？不妨阅读配套指南 [Coding for Marketers](https://codingformarketers.com?ref=marketingskills)。

**欢迎贡献！** 发现改进技能的方法，或有新技能想添加？[提交 PR](#contributing)。
遇到问题或有任何疑问？[提交 Issue](https://github.com/coreyhaines31/marketingskills/issues) —— 我们很乐意提供帮助。

## 什么是技能（Skills）？

技能是 Markdown 文件，为 AI Agent 提供特定任务的专业知识与工作流。将其添加到项目后，你的 Agent 能识别你正在进行的营销任务，并自动应用相应的框架与最佳实践。

## 技能的协作机制

技能之间相互引用，并基于共享上下文进行扩展。`product-marketing`（产品营销）是基础技能——其他所有技能在执行任何操作前，都会先读取该文件以了解你的产品、受众与市场定位。

```
                            ┌──────────────────────────────────────┐
                            │          product-marketing           │
                            │    (read by all other skills first)  │
                            └──────────────────┬───────────────────┘
                                               │
    ┌──────────────┬─────────────┬─────────────┼─────────────┬──────────────┬──────────────┐
    ▼              ▼             ▼             ▼             ▼              ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│  SEO &   │ │   CRO    │ │Content & │ │  Paid &    │ │ Growth & │ │  Sales &    │ │ Strategy  │
│ Content  │ │          │ │   Copy   │ │Measurement │ │Retention │ │    GTM      │ │           │
├──────────┤ ├──────────┤ ├──────────┤ ├────────────┤ ├──────────┤ ├─────────────┤ ├───────────┤
│seo-audit │ │cro       │ │copywritng│ │ads         │ │referrals │ │revops       │ │mktg-ideas │
│ai-seo    │ │signup    │ │copy-edit │ │ad-creative │ │free-tools│ │sales-enable │ │mktg-psych │
│site-arch │ │onboarding│ │cold-email│ │ab-testing  │ │churn-    │ │launch       │ │customer-  │
│programm  │ │popups    │ │emails    │ │analytics   │ │ prevent  │ │pricing      │ │ research  │
│schema    │ │paywalls  │ │social    │ │            │ │community │ │competitors  │ │           │
│content   │ │          │ │video     │ │            │ │lead-magnt│ │comp-profile │ │           │
│aso       │ │          │ │image     │ │            │ │co-mktg   │ │directory    │ │           │
│          │ │          │ │sms       │ │            │ │          │ │prospecting  │ │           │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └─────┬──────┘ └────┬─────┘ └──────┬──────┘ └─────┬─────┘
     │            │            │              │             │              │              │
     └────────────┴─────┬──────┴──────────────┴─────────────┴──────────────┴──────────────┘
                        │
         Skills cross-reference each other:
           copywriting ↔ cro ↔ ab-testing
           revops ↔ sales-enablement ↔ cold-email
           seo-audit ↔ schema ↔ ai-seo
           customer-research → copywriting, cro, competitors
```

完整依赖关系图请参阅各技能的 **相关技能（Related Skills）** 章节。

## 可用技能

<!-- SKILLS:START -->
| 技能名称 | 说明 |
|-------|-------------|
| [ab-testing](skills/ab-testing/) | 当用户希望规划、设计或实施 A/B 测试，或构建增长实验体系时适用... |
| [ad-creative](skills/ad-creative/) | 当用户需要生成、迭代或规模化制作广告素材（标题、描述、主文案或完整广告）时适用... |
| [ads](skills/ads/) | 当用户希望获得 Google Ads、Meta (Facebook/Instagram)、LinkedIn、Twitter/X 等平台的付费广告投放帮助时适用... |
| [ai-seo](skills/ai-seo/) | 当用户希望对内容进行 AI 搜索引擎优化，争取被 LLM 引用或出现在 AI 生成答案中时适用... |
| [analytics](skills/analytics/) | 当用户希望搭建、改进或审计数据分析追踪与测量体系。当用户提及“分析”、“数据追踪”等关键词时也适用... |
| [aso](skills/aso/) | 当用户希望对应用商店（App Store/Google Play）页面进行审计或优化。当用户提及“ASO”时适用... |
| [churn-prevention](skills/churn-prevention/) | 当用户希望降低流失率、设计取消订阅流程、设置挽留优惠、挽回失败支付，或...时适用... |
| [co-marketing](skills/co-marketing/) | 当用户希望寻找联合营销伙伴、策划联名活动，或 brainstorming 合作机会时。适用场景包括... |
| [cold-email](skills/cold-email/) | 撰写能带来回复的 B2B 冷邮件及跟进序列。当用户希望编写冷启动外联邮件、...时适用... |
| [community-marketing](skills/community-marketing/) | 构建并利用在线社区推动产品增长与品牌忠诚度。当用户希望创建社群、运营私域流量或...时适用... |
| [competitor-profiling](skills/competitor-profiling/) | 当用户希望通过竞争对手的网址调研、画像构建或深度分析其业务时。当用户提及“竞品分析”时也适用... |
| [competitors](skills/competitors/) | 当用户希望创建用于 SEO 和销售赋能的竞品对比页或替代方案页面时。当用户需要制作“vs...”或 alternatives 页面时也适用... |
| [content-strategy](skills/content-strategy/) | 当用户希望规划内容策略、决定创作方向，或确定选题范围时。也适用于内容日历制定与...场景... |
| [copy-editing](skills/copy-editing/) | 当用户需要编辑、审阅或优化现有营销文案，或更新过时内容时。也适用于校对、润色及...场景... |
| [copywriting](skills/copywriting/) | 当用户希望撰写、重写或优化任意页面的营销文案（包括首页、落地页、产品页等）时适用... |
| [cro](skills/cro/) | 当用户希望对任何营销页面或表单进行优化以提升转化率，包括首页、注册页、支付页等...时适用... |
| [customer-research](skills/customer-research/) | 当用户希望开展、分析或综合客户调研数据。当用户提及“用户研究”、“访谈”、“反馈分析”时也适用... |
| [directory-submissions](skills/directory-submissions/) | 当用户希望将产品提交至初创企业、SaaS、AI、Agent、MCP 或无代码平台的目录及评测网站，以获取曝光与流量时适用... |
| [emails](skills/emails/) | 当用户希望创建或优化邮件序列、滴灌营销（Drip Campaign）、自动化邮件流或生命周期邮件策略时适用... |
| [free-tools](skills/free-tools/) | 当用户希望规划、评估或开发用于营销目的的免费工具，以获取线索、提升 SEO 权重或增强品牌粘性时适用... |
| [image](skills/image/) | 当用户需要为营销活动创建、生成、编辑或优化图片（如博客头图、社交媒体配图、产品截图等）时适用... |
| [launch](skills/launch/) | 当用户希望规划产品发布、功能公告或版本更新策略时。也适用于制定上市（Go-to-Market）计划与...场景... |
| [lead-magnets](skills/lead-magnets/) | 当用户希望创建、规划或优化用于邮件收集或线索获取的诱饵内容（Lead Magnet）。也适用于设计白皮书、模板等...场景... |
| [marketing-ideas](skills/marketing-ideas/) | 当用户需要为其 SaaS 或软件产品寻找营销灵感、创意或策略时。也适用于突破增长瓶颈与...场景... |
| [marketing-plan](skills/marketing-plan/) | 当用户需要为客户、顾问公司或自有产品制定全面的营销策略计划时。也适用于年度规划、预算分配与...场景... |
| [marketing-psychology](skills/marketing-psychology/) | 当用户希望将心理学原理、思维模型或行为科学应用于营销活动。也适用于设计高转化文案、定价策略及...场景... |
| [onboarding](skills/onboarding/) | 当用户希望优化注册后的引导流程、提升新用户激活率、打磨首次使用体验或缩短价值实现时间（Time-to-Value）时适用... |
| [paywalls](skills/paywalls/) | 当用户希望创建或优化应用内付费墙、升级界面、追加销售弹窗或功能权限门控（Feature Gates）时适用... |
| [popups](skills/popups/) | 当用户需要为提升转化而创建或优化弹窗、模态框、覆盖层、侧边栏或横幅广告时。也适用于设置触发条件与...场景... |
| [pricing](skills/pricing/) | 当用户需要定价决策支持、套餐设计（Packaging）或变现策略规划时。也适用于分析竞品定价模型与...场景... |
| [product-marketing](skills/product-marketing/) | 当用户希望创建或更新产品营销上下文文档（Product Marketing Context）。也适用于定义目标受众、价值主张与...场景... |
| [programmatic-seo](skills/programmatic-seo/) | 当用户希望通过模板和数据批量生成以 SEO 为导向的页面时。也适用于自动化内容生产与...场景... |
| [prospecting](skills/prospecting/) | 当用户希望寻找、筛选并建立潜在客户名单以进行外联触达时，适用于 B2B SaaS、通用 B2B 或...垂直领域... |
| [referrals](skills/referrals/) | 当用户希望创建、优化或分析推荐计划、联盟营销（Affiliate）或口碑传播策略时适用... |
| [revops](skills/revops/) | 当用户需要营收运营支持、线索生命周期管理，或优化从市场到销售的交接流程时适用... |
| [sales-enablement](skills/sales-enablement/) | 当用户希望制作销售物料（如演示文稿、单页简介、异议处理指南）或编写产品演示脚本时。也适用于赋能销售团队与...场景... |
| [schema](skills/schema/) | 当用户希望添加、修复或优化网站上的 Schema 标记与结构化数据时。也适用于提升搜索引擎结果展示（富摘要）与...场景... |
| [seo-audit](skills/seo-audit/) | 当用户希望对网站的 SEO 问题进行审计、审查或诊断时。也适用于技术 SEO 检查、页面优化建议与...场景... |
| [signup](skills/signup/) | 当用户希望优化注册、账号创建或试用激活流程时。也适用于减少表单摩擦、提升填写完成率与...场景... |
| [site-architecture](skills/site-architecture/) | 当用户需要规划、绘制或重构网站的页面层级、导航结构、URL 架构或内部链接策略时适用... |
| [sms](skills/sms/) | 当用户希望规划、构建或优化短信（SMS）与多媒体消息（MMS）营销，包括欢迎流程、弃购提醒、促销通知等时适用... |
| [social](skills/social/) | 当用户需要帮助创建、排期或优化社交媒体内容（如 LinkedIn、Twitter/X、Instagram、小红书等）时适用... |
| [video](skills/video/) | 当用户希望使用 AI 工具或自动化框架创建、生成或制作视频内容时。也适用于短视频脚本撰写与...场景... |
<!-- SKILLS:END -->

## 安装指南

### 方式一：CLI 命令行安装（推荐）

使用 [npx skills](https://github.com/vercel-labs/skills) 直接安装技能：

```bash
# Install all skills
npx skills add coreyhaines31/marketingskills

# Install specific skills
npx skills add coreyhaines31/marketingskills --skill cro copywriting

# List available skills
npx skills add coreyhaines31/marketingskills --list
```

该命令会自动将技能安装至你的 `.agents/skills/` 目录（并为兼容 Claude Code，在 `.claude/skills/` 中创建软链接）。

### 方式二：Claude Code 插件系统

通过 Claude Code 内置的插件系统进行安装：

```bash
# Add the marketplace
/plugin marketplace add coreyhaines31/marketingskills

# Install all marketing skills
/plugin install marketing-skills
```

### 方式三：克隆并复制

克隆整个仓库并将技能文件夹复制到项目目录：

```bash
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

### 方式四：Git Submodule（子模块）

将其添加为子模块，便于后续更新：

```bash
git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills
```

之后通过引用 `.agents/marketingskills/skills/` 目录下的技能即可。

### 方式五：Fork 并自定义

1. Fork（复刻）本仓库
2. 根据你的具体需求定制技能
3. 将你的 Fork 版本克隆到项目中

### 方式六：SkillKit（多 Agent 兼容）

使用 [SkillKit](https://github.com/rohitg00/skillkit) 在多个 AI Agent（如 Claude Code、Cursor、Copilot 等）间统一安装技能：

```bash
# Install all skills
npx skillkit install coreyhaines31/marketingskills

# Install specific skills
npx skillkit install coreyhaines31/marketingskills --skill cro copywriting

# List available skills
npx skillkit install coreyhaines31/marketingskills --list
```

## 从 v1.x 升级至 v2.0

v2.0 重命名了 17 个技能，并将 `page-cro` 与 `form-cro` 合并为单一的 `cro` 技能。如果你已安装过 v1.x 版本，升级后你的安装目录中会保留**旧的文件夹**。新技能会与旧版并存（例如同时出现 `skills/page-cro/` 和 `skills/cro/`）。建议清理旧文件：

```bash
# From the directory where you installed the skills (e.g., .agents/skills/ or .claude/skills/)
rm -rf page-cro form-cro \
       ab-test-setup analytics-tracking aso-audit competitor-alternatives \
       email-sequence free-tool-strategy launch-strategy onboarding-cro \
       paid-ads paywall-upgrade-cro popup-cro pricing-strategy \
       product-marketing-context referral-program schema-markup \
       signup-flow-cro social-content
```

随后可通过你习惯的方式重新安装 v2.0 技能（例如执行 `npx skills add coreyhaines31/marketingskills`）。

### 迁移产品营销上下文文件

在 v2.0 中，上下文文件已从 `.claude/` 移至 `.agents/`，且文件名从 `product-marketing-context.md` 更改为 `product-marketing.md`。请迁移你现有的上下文文件：

```bash
mkdir -p .agents
# v2.0 file (or pre-v2.0 file with new name)
mv .claude/product-marketing.md .agents/product-marketing.md 2>/dev/null
# pre-v2.0 file with legacy name
mv .claude/product-marketing-context.md .agents/product-marketing.md 2>/dev/null
```

技能仍会将 `.claude/` 目录及旧的 `product-marketing-context.md` 文件名作为回退（Fallback）选项进行检查。因此，即使不迁移也不会影响现有功能。

### 完整重命名对照表

| 旧名称 | 新名称 |
|-----|-----|
| `ab-test-setup` | `ab-testing` |
| `analytics-tracking` | `analytics` |
| `aso-audit` | `aso` |
| `competitor-alternatives` | `competitors` |
| `email-sequence` | `emails` |
| `form-cro` | merged into `cro` |
| `free-tool-strategy` | `free-tools` |
| `launch-strategy` | `launch` |
| `onboarding-cro` | `onboarding` |
| `page-cro` | `cro` |
| `paid-ads` | `ads` |
| `paywall-upgrade-cro` | `paywalls` |
| `popup-cro` | `popups` |
| `pricing-strategy` | `pricing` |
| `product-marketing-context` | `product-marketing` |
| `referral-program` | `referrals` |
| `schema-markup` | `schema` |
| `signup-flow-cro` | `signup` |
| `social-content` | `social` |

## 使用方法

安装完成后，只需向你的 Agent 下达营销任务指令即可：

```
"Help me optimize this landing page for conversions"
→ Uses cro skill

"Write homepage copy for my SaaS"
→ Uses copywriting skill

"Set up GA4 tracking for signups"
→ Uses analytics skill

"Create a 5-email welcome sequence"
→ Uses emails skill
```

你也可以直接调用特定技能：

```
/cro
/emails
/seo-audit
```

## 技能分类

### 转化优化（Conversion Optimization）
- `cro` - 页面与表单优化
- `signup` - 注册流程设计
- `onboarding` - 注册后激活引导
- `popups` - 弹窗与覆盖层组件
- `paywalls` - 应用内付费墙

### 内容与文案（Content & Copy）
- `copywriting` - 营销页面文案撰写
- `copy-editing` - 现有文案编辑与润色
- `cold-email` - B2B 冷启动外联邮件及序列设计
- `emails` - 自动化邮件流策略
- `social` - 社交媒体内容创作
- `image` - AI 图像生成、设计与优化

### SEO 与发现（SEO & Discovery）
- `seo-audit` - 技术与站内 SEO 审计
- `ai-seo` - AI 搜索引擎优化（AEO, GEO, LLMO）
- `programmatic-seo` - 规模化页面批量生成
- `site-architecture` - 页面层级、导航与 URL 结构规划
- `competitors` - 竞品对比页与替代方案页面
- `schema` - 结构化数据标记

### 付费投放与分发（Paid & Distribution）
- `ads` - Google、Meta、LinkedIn 广告战役策划
- `ad-creative` - 批量生成与迭代广告素材
- `social` - 社交媒体排期与策略规划

### 数据测量与测试（Measurement & Testing）
- `analytics` - 事件追踪搭建
- `ab-testing` - 实验设计与分析

### 用户留存（Retention）
- `churn-prevention` - 取消流程设计、挽留优惠设置、账单催收与支付挽回

### 增长工程（Growth Engineering）
- `co-marketing` - 合作伙伴挖掘与联名活动策划
- `free-tools` - 营销工具与计算器开发
- `referrals` - 推荐计划与联盟营销体系搭建

### 策略与变现（Strategy & Monetization）
- `marketing-ideas` - SaaS 营销灵感库（140+ 创意）
- `marketing-psychology` - 思维模型与行为心理学应用
- `launch` - 产品发布与功能公告策略
- `pricing` - 定价、套餐设计与变现策略

### 销售与营收运营（Sales & RevOps）
- `revops` - 线索生命周期管理、评分、路由分配与销售协同流程优化
- `sales-enablement` - 销售物料制作、演示文稿、异议处理指南与脚本编写

## 贡献指南

发现可改进的技能？或有新技能建议？欢迎提交 PR 和 Issue！

添加或优化技能的详细规范，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE) - 你可自由使用本项目内容。