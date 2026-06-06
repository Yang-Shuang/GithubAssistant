# 🎭 智能体团队：随时准备重塑你工作流的AI专家

> **触手可及的完整AI代理团队** —— 从前端魔法师到Reddit社区忍者，从注入奇思妙想的创意师到现实检验员。每个角色都是拥有独特个性、标准化流程和可验证交付物的领域专家。

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github)](https://github.com/sponsors/msitarzewski)

---

## 🚀 这是什么？

源于Reddit的一个讨论帖，经过数月的迭代打磨，**The Agency（智能体团队）** 是一个精心打造的AI角色集合。每个角色都具备：

- **🎯 领域专精**：深耕特定领域（而非通用的提示词模板）
- **🧠 个性驱动**：独特的语气、沟通风格和行事方法
- **📋 交付导向**：可落地的代码、流程和量化成果
- **✅ 生产就绪**：经过实战检验的工作流和成功指标

**你可以把它看作**：组建你的梦之队，只不过这些成员是永不疲倦、从不抱怨且始终交付成果的AI专家。

---

## ⚡ 快速开始

### 方案一：配合 Claude Code 使用（推荐）

```bash
# Install all agents to your Claude Code directory
./scripts/install.sh --tool claude-code

# Or manually copy a category if you only want one division
cp engineering/*.md ~/.claude/agents/

# Then activate any agent in your Claude Code sessions:
# "Hey Claude, activate Frontend Developer mode and help me build a React component"
```

### 方案二：作为参考资料

每个代理文件包含：
- 身份设定与个性特征
- 核心使命与工作流
- 带代码示例的技术交付物
- 成功指标与沟通风格

浏览下方的角色，复制并适配你需要的内容！

### 方案三：配合其他工具使用（GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Kimi Code）

```bash
# Step 1 -- generate integration files for all supported tools
./scripts/convert.sh

# Step 2 -- install interactively (auto-detects what you have installed)
./scripts/install.sh

# Or target a specific tool directly
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool gemini-cli
./scripts/install.sh --tool opencode
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool cursor
./scripts/install.sh --tool aider
./scripts/install.sh --tool windsurf
./scripts/install.sh --tool kimi
```

详见下方的 [多工具集成](#-multi-tool-integrations) 章节获取完整说明。

---

## 🎨 智能体团队阵容

### 💻 工程研发部

构建未来，一次提交一步到位。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🎨 [前端开发者](engineering/engineering-frontend-developer.md) | React/Vue/Angular、UI实现、性能优化 | 现代Web应用、像素级还原界面、Core Web Vitals优化 |
| 🏗️ [后端架构师](engineering/engineering-backend-architect.md) | API设计、数据库架构、可扩展性 | 服务端系统、微服务、云基础设施 |
| 📱 [移动端开发者](engineering/engineering-mobile-app-builder.md) | iOS/Android、React Native、Flutter | 原生与跨平台移动应用开发 |
| 🤖 [AI工程师](engineering/engineering-ai-engineer.md) | ML模型、部署、AI集成 | 机器学习功能、数据管道、AI驱动型应用 |
| 🚀 [DevOps自动化专家](engineering/engineering-devops-automator.md) | CI/CD、基础设施自动化、云运维 | 流水线开发、部署自动化、监控体系搭建 |
| ⚡ [快速原型师](engineering/engineering-rapid-prototyper.md) | 快速POC开发、MVP构建 | 概念验证、黑客松项目、敏捷迭代 |
| 💎 [高级开发者](engineering/engineering-senior-developer.md) | Laravel/Livewire、高级模式实践 | 复杂业务实现、架构决策评审 |
| 🔧 [Filament优化专家](engineering/engineering-filament-optimization-specialist.md) | Filament PHP管理后台UX、表单结构重构、资源优化 | 重组Filament资源/表单/表格，打造更快速简洁的管理流 |
| 🔒 [安全工程师](engineering/engineering-security-engineer.md) | 威胁建模、安全代码审查、安全架构 | 应用安全防护、漏洞评估、安全CI/CD集成 |
| ⚡ [自主优化架构师](engineering/engineing-autonomous-optimization-architect.md) | LLM路由、成本优化、影子测试 | 需要智能API选型与成本护栏的自治系统 |
| 🔩 [嵌入式固件工程师](engineering/engineering-embedded-firmware-engineer.md) | 裸机开发、RTOS、ESP32/STM32/Nordic固件 | 生产级嵌入式系统与IoT设备开发 |
| 🚨 [应急响应指挥官](engineering/engineering-incident-response-commander.md) | 事件管理、事后复盘、值班体系 | 生产环境事件处置与应急准备建设 |
| ⛓️ [Solidity智能合约工程师](engineering/engineering-solidity-smart-contract-engineer.md) | EVM合约、Gas优化、DeFi协议 | 安全且Gas优化的智能合约与去中心化金融协议 |
| 🧭 [代码库入职引导专家](engineering/engineering-codebase-onboarding-engineer.md) | 快速开发者入职、只读代码探索、事实性说明 | 通过阅读代码、追踪调用链、陈述结构与行为事实，帮助新成员快速理解陌生仓库 |
| 📚 [技术文档工程师](engineering/engineering-technical-writer.md) | 开发文档、API参考、教程编写 | 清晰准确的技术文档产出 |
| 🎯 [威胁检测工程师](engineering/engineering-threat-detection-engineer.md) | SIEM规则、威胁狩猎、ATT&CK映射 | 构建检测层与威胁狩猎体系 |
| 💬 [微信小程序开发者](engineering/engineering-wechat-mini-program-developer.md) | 微信生态、小程序开发、支付集成 | 为微信生态构建高性能应用 |
| 👁️ [代码审查专家](engineering/engineering-code-reviewer.md) | 建设性Code Review、安全与可维护性评估 | PR评审、质量门禁把关、通过审查指导团队 |
| 🗄️ [数据库优化师](engineering/engineering-database-optimizer.md) | 表结构设计、查询优化、索引策略 | PostgreSQL/MySQL调优、慢查询排查、迁移规划 |
| 🌿 [Git工作流专家](engineering/engineering-git-workflow-master.md) | 分支策略、规范提交、高级Git操作 | Git流程设计、历史清理、CI友好型分支管理 |
| 🏛️ [软件架构师](engineering/engineering-software-architect.md) | 系统设计、DDD、架构模式、权衡分析 | 架构决策、领域建模、系统演进规划 |
| 🛡️ [SRE工程师](engineering/engineering-sre.md) | SLO定义、错误预算、可观测性、混沌工程 | 生产环境可靠性保障、琐事削减、容量规划 |
| 🧬 [AI数据修复工程师](engineering/engineering-ai-data-remediation-engineer.md) | 自愈管道、隔离SLM训练、语义聚类 | 零数据丢失地大规模修复破损数据 |
| 🔧 [数据工程师](engineering/engineering-data-engineer.md) | 数据管道、湖仓一体架构、ETL/ELT | 构建可靠的数据基础设施与数仓体系 |
| 🔗 [飞书集成开发者](engineering/engineering-feishu-integration-developer.md) | 飞书开放平台、机器人开发、工作流搭建 | 为飞书生态构建深度集成应用 |
| 🧱 [CMS开发者](engineering/engineering-cms-developer.md) | WordPress & Drupal主题/插件、内容架构 | 代码优先的CMS实施与定制开发 |
| 📧 [邮件智能解析工程师](engineering/engineering-email-intelligence-engineer.md) | 邮件解析、MIME提取、为AI代理结构化数据 | 将原始邮件线程转化为可推理的结构化上下文 |
| 🎙️ [语音AI集成工程师](engineering/engineering-voice-ai-integration-engineer.md) | 语音转文本管道、Whisper、ASR、说话人分离 | 端到端转录流水线、音频预处理、结构化文稿交付 |

### 🎨 设计部

让产品既美观，又易用且令人愉悦。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🎯 [UI设计师](design/design-ui-designer.md) | 视觉设计、组件库、设计系统 | 界面创建、品牌一致性维护、组件设计 |
| 🔍 [UX研究员](design/design-ux-researcher.md) | 用户测试、行为分析、研究方法论 | 理解用户需求、可用性测试、设计洞察输出 |
| 🏛️ [UX架构师](design/design-ux-architect.md) | 技术架构、CSS体系、落地实现 | 开发者友好的基础建设、实施指导 |
| 🎭 [品牌守护者](design/design-brand-guardian.md) | 品牌识别、一致性管控、定位策略 | 品牌战略制定、视觉资产开发、规范输出 |
| 📖 [视觉叙事专家](design/design-visual-storyteller.md) | 视觉故事线、多媒体内容创作 | 引人入胜的视觉叙事、品牌故事传达 |
| ✨ [奇思妙想注入师](design/design-whimsy-injector.md) | 个性表达、惊喜感设计、趣味交互 | 增添产品乐趣、微交互动效、彩蛋设计与人格化塑造 |
| 📷 [AI图像提示词工程师](design/design-image-prompt-engineer.md) | AI绘图提示词优化、摄影构图 | Midjourney、DALL-E、Stable Diffusion摄影级提示词生成 |
| 🌈 [包容性视觉专家](design/design-inclusive-visuals-specialist.md) | 多元代表性、偏见规避、真实影像 | 生成文化准确、符合包容性标准的AI图像与视频 |

### 💰 付费媒体部

将广告预算转化为可衡量的业务成果。

| 角色 | 专长 | 适用场景 |
| --- | --- | --- |
| 💰 [PPC投放策略师](paid-media/paid-media-ppc-strategist.md) | Google/Microsoft/Amazon Ads、账户架构、竞价策略 | 账户搭建、预算分配、规模扩张、性能诊断 |
| 🔍 [搜索词分析师](paid-media/paid-media-search-query-analyst.md) | 搜索词分析、否定关键词、意图映射 | 查询审计、无效花费清理、高潜词发现 |
| 📋 [付费媒体审计师](paid-media/paid-media-auditor.md) | 200+项账户审计、竞品分析 | 接管旧账户、季度复盘、竞标方案输出 |
| 📡 [追踪与归因专家](paid-media/paid-media-tracking-specialist.md) | GTM、GA4、转化追踪、CAPI | 新环境部署、追踪审计、平台迁移适配 |
| ✍️ [广告素材策略师](paid-media/paid-media-creative-strategist.md) | RSA文案、Meta创意、Performance Max资产 | 创意上线、A/B测试计划、疲劳度刷新 |
| 📺 [程序化与展示位采购专家](paid-media/paid-media-programmatic-buyer.md) | GDN、DSPs、合作媒体、ABM展示广告 | 展示位规划、渠道拓展、ABM项目执行 |
| 📱 [付费社媒策略师](paid-media/paid-media-paid-social-strategist.md) | Meta、LinkedIn、TikTok、跨平台社交 | 社媒广告投放计划、平台选型、受众策略制定 |

### 💼 销售部

通过专业技巧而非CRM繁琐操作，将线索转化为营收。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🎯 [外拓策略师](sales/sales-outbound-strategist.md) | 信号驱动型 prospecting、多渠道触达序列、ICP精准定位 | 通过调研驱动的精准 outreach 构建管线，而非盲目堆量 |
| 🔍 [需求挖掘教练](sales/sales-discovery-coach.md) | SPIN、Gap Selling、Sandler —— 提问设计与通话结构 | 准备 discovery call、商机分级评估、销售带教辅导 |
| ♟️ [交易策略师](sales/sales-deal-strategist.md) | MEDDPICC 资格认证、竞争定位、赢单规划 | 商机评分、管线风险排查、制定赢单策略 |
| 🛠️ [售前工程师](sales/sales-engineer.md) | 技术演示、POC范围界定、竞品作战卡 | 售前技术攻坚、Demo准备、竞争态势分析 |
| 🏹 [方案书策略师](sales/sales-proposal-strategist.md) | RFP响应、赢单主题提炼、叙事结构搭建 | 撰写具有说服力的提案，而非仅满足合规要求 |
| 📊 [管线分析师](sales/sales-pipeline-analyst.md) | 销售预测、管线健康度、交易流速、RevOps | 管线复盘、预测准确率提升、营收运营优化 |
| 🗺️ [客户成功策略师](sales/sales-account-strategist.md) | Land-and-expand打法、QBR管理、干系人地图绘制 | 售后增购拓展、账户规划、NRR增长推动 |
| 🏋️ [销售教练](sales/sales-coach.md) | 新人培养、通话陪练、管线复盘引导 | 通过结构化辅导让每位销售与每笔交易更优秀 |
| 🎯 [外拓触达专家](specialized/sales-outreach.md) | 冷启动 prospecting、多触点节奏设计、异议处理、方案撰写 | B2B漏斗顶部触达 —— 从冷邮件到预约 discovery call |

### 📢 市场部

通过每一次真实的互动，稳步扩大你的受众。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🚀 [增长黑客](marketing/marketing-growth-hacker.md) | 快速用户获取、病毒式传播循环、实验设计 | 爆发式增长、拉新策略、转化漏斗优化 |
| 📝 [内容创作者](marketing/marketing-content-creator.md) | 多平台内容分发、编辑日历管理 | 内容战略规划、文案撰写、品牌故事传达 |
| 🐦 [Twitter互动专家](marketing/marketing-twitter-engager.md) | 实时互动、思想领导力输出 | Twitter运营策略、LinkedInCampaigns、专业社交布局 |
| 📱 [TikTok策略师](marketing/marketing-tiktok-strategist.md) | 爆款内容创作、算法优化 | TikTok增长、病毒式传播、Z世代/千禧受众触达 |
| 📸 [Instagram策展人](marketing/marketing-instagram-curator.md) | 视觉叙事、社区运营 | Instagram策略、美学体系搭建、视觉内容规划 |
| 🤝 [Reddit社区构建者](marketing/marketing-reddit-community-builder.md) | 真实互动、价值驱动型内容 | Reddit生态运营、社区信任建立、原生营销植入 |
| 📱 [ASO优化专家](marketing/marketing-app-store-optimizer.md) | ASO策略、转化优化、搜索发现率提升 | App推广、商店排名优化、应用增长 |
| 🌐 [社媒全栈策略师](marketing/marketing-social-media-strategist.md) | 跨平台战略、Campaign统筹 | 全局社交布局、多平台联动营销 |
| 📕 [小红书专家](marketing/marketing-xiaohongshu-specialist.md) | 生活方式内容、趋势驱动型策略 | 小红书增长、美学叙事、Z世代受众运营 |
| 💬 [微信公众号运营官](marketing/marketing-wechat-official-account.md) | 粉丝互动、内容营销转化 | 公众号战略、私域社群搭建、转化漏斗优化 |
| 🧠 [知乎策略师](marketing/marketing-zhihu-strategist.md) | 思想领导力、知识型互动 | 知乎权威背书建设、问答运营、线索获取 |
| 🇨🇳 [百度SEO专家](marketing/marketing-baidu-seo-specialist.md) | 百度搜索优化、中国区SEO、ICP合规适配 | 百度排名提升与中国搜索市场触达 |
| 🎬 [B站内容策略师](marketing/marketing-bilibili-content-strategist.md) | B站算法机制、弹幕文化、UP主成长路径 | 基于社区优先理念在B站构建受众基本盘 |
| 🎠 [轮播增长引擎](marketing/marketing-carousel-growth-engine.md) | TikTok/Instagram轮播图、自动化发布 | 生成并发布病毒式轮播图文内容 |
| 💼 [LinkedIn内容创作者](marketing/marketing-linkedin-content-creator.md) | 个人IP打造、思想领导力、专业内容输出 | LinkedIn增长、职业受众构建、B2B内容营销 |
| 🛒 [中国电商运营专家](marketing/marketing-china-ecommerce-operator.md) | 淘宝、天猫、拼多多、直播电商 | 多平台中国本土电商操盘 |
| 🎥 [快手策略师](marketing/marketing-kuaishou-strategist.md) | 快手生态、老铁文化、下沉市场增长 | 在低线城市构建真实可信的受众基本盘 |
| 🔍 [SEO专家](marketing/marketing-seo-specialist.md) | 技术型SEO、内容战略、外链建设 | 驱动可持续的自然搜索流量增长 |
| 📘 [书籍合著者](marketing/marketing-book-co-author.md) | 思想领导力专著、代笔写作、出版流程 | 为创始人与行业专家打造战略性图书合作 |
| 🌏 [跨境电商专家](marketing/marketing-cross-border-ecommerce.md) | Amazon、Shopee、Lazada、跨境履约 | 全链路跨境电商战略规划 |
| 🎵 [抖音策略师](marketing/marketing-douyin-strategist.md) | 抖音平台机制、短视频营销、算法推荐 | 在中国最大短视频平台实现受众增长 |
| 🎙️ [直播电商教练](marketing/marketing-livestream-commerce-coach.md) | 主播培训、直播间优化、转化提升 | 打造高转化率直播电商运营体系 |
| 🧭 [播客策略师](marketing/marketing-podcast-strategist.md) | 播客内容战略、平台适配 | 中国播客市场策略与精细化运营 |
| 🔒 [私域运营专家](marketing/marketing-private-domain-operator.md) | 企微生态、私域流量、社群运营 | 构建企业微信私域流量池与自动化触达体系 |
| 🎬 [短视频剪辑教练](marketing/marketing-short-video-editing-coach.md) | 后期制作、剪辑工作流、平台规范适配 | 实操型短视频剪辑培训与成片优化 |
| 🔥 [微博运营专家](marketing/marketing-weibo-strategist.md) | 新浪微博、热点话题、粉丝互动 | 全矩阵微博运营与增长策略 |
| 🔮 [AI引用可见性专家](marketing/marketing-ai-citation-strategist.md) | AEO/GEO优化、AI推荐曝光、引用审计 | 提升品牌在ChatGPT、Claude、Gemini、Perplexity等平台的可见度 |
| 🇨🇳 [中国市场本地化策略师](marketing/marketing-china-market-localization-strategist.md) | 全栈中国本土化、抖音/小红书/微信GTM落地 | 将趋势信号转化为可执行的中国区上市战略 |
| 🎬 [视频优化专家](marketing/marketing-video-optimization-specialist.md) | YouTube算法策略、章节划分、缩略图概念设计 | YouTube频道增长、视频SEO、观众留存率优化 |

### 📊 产品部

在正确的时间，构建正确的东西。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🎯 [Sprint优先级规划师](product/product-sprint-prioritizer.md) | 敏捷规划、功能优先级排序 | Sprint排期、资源分配、Backlog管理 |
| 🔍 [趋势研究员](product/product-trend-researcher.md) | 市场情报、竞品分析 | 市场调研、机会评估、趋势识别 |
| 💬 [反馈整合专家](product/product-feedback-synthesizer.md) | 用户反馈分析、洞察提取 | 反馈归因、用户洞察输出、产品优先级制定 |
| 🧠 [行为助推引擎](product/product-behavioral-nudge-engine.md) | 行为心理学、助推设计、参与度提升 | 通过行为科学最大化用户动机与留存 |
| 🧭 [产品经理](product/product-manager.md) | 全生命周期产品负责 | 需求发现、PRD撰写、Roadmap规划、GTM落地、结果度量 |

### 🎬 项目管理部

确保列车准点运行（且预算不超支）。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🎬 [制片总监](project-management/project-management-studio-producer.md) | 高层统筹、组合管理 | 多项目监督、战略对齐、资源全局调配 |
| 🐑 [项目经理](project-management/project-management-project-shepherd.md) | 跨职能协调、时间线管理 | 端到端项目协同、干系人沟通管理 |
| ⚙️ [制片运营专家](project-management/project-management-studio-operations.md) | 日常效率提升、流程优化 | 运营卓越体系建设、团队支持、效能提升 |
| 🧪 [实验追踪员](project-management/project-management-experiment-tracker.md) | A/B测试、假设验证 | 实验管理、数据驱动决策、测试执行 |
| 👔 [高级项目经理](project-management/project-manager-senior.md) | 现实范围界定、任务拆解转化 | 将需求规格转化为可执行任务、范围管控 |
| 📋 [Jira工作流管家](project-management/project-management-jira-workflow-steward.md) | Git工作流、分支策略、追溯性管理 | 强制执行Jira关联的Git规范与交付纪律 |

### 🧪 测试部

替用户提前踩坑，确保产品稳定。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 📸 [证据收集员](testing/testing-evidence-collector.md) | 截图型QA、可视化验证 | UI测试、视觉比对、缺陷文档化 |
| 🔍 [现实检验员](testing/testing-reality-checker.md) | 基于证据的认证、质量门禁 | 生产环境就绪评估、质量放行审批、发布认证 |
| 📊 [测试结果分析师](testing/testing-test-results-analyzer.md) | 测试评估、指标分析 | 测试输出归因、质量洞察输出、覆盖率报告 |
| ⚡ [性能基准测试员](testing/testing-performance-benchmarker.md) | 压力测试、优化调优 | 速度压测、负载测试、性能瓶颈排查 |
| 🔌 [API测试专家](testing/testing-api-tester.md) | API验证、集成测试 | 接口测试、端点校验、集成质量保障 |
| 🛠️ [工具评估师](testing/testing-tool-evaluator.md) | 技术选型评估、方案对比 | 第三方工具评测、软件推荐、技术决策支持 |
| 🔄 [工作流优化专家](testing/testing-workflow-optimizer.md) | 流程分析、效率提升 | 流程重构、效能增益挖掘、自动化机会识别 |
| ♿ [无障碍审计员](testing/testing-accessibility-auditor.md) | WCAG合规审计、辅助技术测试 | 无障碍标准符合性验证、读屏软件测试、包容性设计保障 |

### 🛟 支持部

运营体系的坚实后盾。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 💬 [客服响应专家](support/support-support-responder.md) | 客户服务、问题排查解决 | 客户支持体系搭建、体验优化、运维支持 |
| 📊 [数据分析师](support/support-analytics-reporter.md) | 数据分析、看板构建、洞察输出 | 商业智能分析、KPI追踪、数据可视化 |
| 💰 [财务追踪员](support/support-finance-tracker.md) | 财务规划、预算管理 | 财务健康度分析、现金流管理、业务绩效评估 |
| 🏗️ [基础设施维护专家](support/support-infrastructure-maintainer.md) | 系统可靠性、性能优化 | 基础设施运维、系统监控与调优 |
| ⚖️ [法务合规审查员](support/support-legal-compliance-checker.md) | 合规审计、法规解读、法律评审 | 企业合规管理、监管要求适配、风险管控 |
| 📑 [高管摘要生成器](support/support-executive-summary-generator.md) | C-suite沟通、战略简报输出 | 高层汇报材料撰写、战略决策支持 |

### 🥽 空间计算部

构建沉浸式未来。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🏗️ [XR交互架构师](spatial-computing/xr-interface-architect.md) | 空间交互设计、沉浸式UX | AR/VR/XR界面设计、空间计算体验构建 |
| 💻 [macOS Spatial/Metal工程师](spatial-computing/macos-spatial-metal-engineer.md) | Swift、Metal、高性能3D渲染 | macOS空间计算开发、Vision Pro原生应用 |
| 🌐 [XR沉浸式开发者](spatial-computing/xr-immersive-developer.md) | WebXR、浏览器端AR/VR | 基于浏览器的沉浸体验、WebXR应用开发 |
| 🎮 [XR座舱交互专家](spatial-computing/xr-cockpit-interaction-specialist.md) | 座舱级控制逻辑、沉浸式系统对接 | 工业/车载座舱控制系统、沉浸式交互界面 |
| 🍎 [visionOS空间工程师](spatial-computing/visionos-spatial-engineer.md) | Apple Vision Pro开发 | Vision Pro应用开发与空间计算体验设计 |
| 🔌 [终端集成专家](spatial-computing/terminal-integration-specialist.md) | 命令行集成、CLI工具链 | CLI工具开发、终端工作流优化、开发者工具适配 |

### 🎯 专项专家部

无法被归类的独特领域专家。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🎭 [多代理编排器](specialized/agents-orchestrator.md) | 多Agent协同、工作流调度 | 复杂项目需多角色联动协作的场景 |
| 🔍 [LSP索引工程师](specialized/lsp-index-engineer.md) | Language Server Protocol、代码智能 | 代码语义检索系统、LSP实现、语义索引构建 |
| 📥 [销售数据提取代理](specialized/sales-data-extraction-agent.md) | Excel监控、销售指标抽取 | 销售数据自动 ingestion、MTD/YTD/年终指标生成 |
| 📈 [数据聚合代理](specialized/data-consolidation-agent.md) | 销售数据汇总、仪表盘报表 | 区域业绩汇总、代表绩效评估、管线快照输出 |
| 📬 [报告分发代理](specialized/report-distribution-agent.md) | 自动化报告投递 | 按区域自动分发报告、定时推送执行 |
| 🔐 [Agent身份与信任架构师](specialized/agentic-identity-trust.md) | Agent身份认证、授权验证、审计追踪 | 多Agent身份体系搭建、权限管控、操作留痕 |
| 🔗 [身份图谱操作员](specialized/identity-graph-operator.md) | 多代理系统共享身份解析 | 实体去重合并、跨Agent身份一致性维护 |
| 💸 [应付账款代理](specialized/accounts-payable-agent.md) | 支付处理、供应商管理、审计合规 | 跨加密法币稳定币的自动化付款执行 |
| 🛡️ [区块链安全审计员](specialized/blockchain-security-auditor.md) | 智能合约审计、漏洞利用分析 | 部署前发现合约潜在漏洞与攻击路径 |
| 📋 [合规审计师](specialized/compliance-auditor.md) | SOC 2、ISO 27001、HIPAA、PCI-DSS | 引导企业完成行业合规认证流程 |
| 🌍 [文化智能策略师](specialized/specialized-cultural-intelligence-strategist.md) | 全球UX适配、代表性设计、文化排他性规避 | 确保产品在不同文化中产生共鸣且无冒犯风险 |
| 🗣️ [开发者布道师](specialized/specialized-developer-advocate.md) | 社区运营、DX提升、开发者内容产出 | 弥合产品团队与开发者生态的鸿沟 |
| 🔬 [模型QA专家](specialized/specialized-model-qa.md) | ML审计、特征分析、可解释性评估 | 机器学习模型全链路质量保障 |
| 🗃️ [知识管理管家](specialized/zk-steward.md) | Zettelkasten方法、笔记关联、知识库构建 | 打造相互关联且经过验证的结构化知识库 |
| 🔌 [MCP构建者](specialized/specialized-mcp-builder.md) | Model Context Protocol服务器、AI工具链扩展 | 开发MCP Server以延伸AI Agent能力边界 |
| 📄 [文档生成器](specialized/specialized-document-generator.md) | PDF/PPTX/DOCX/XLSX自动化生成 | 专业级报告输出、数据可视化与排版 |
| ⚙️ [自动化治理架构师](specialized/automation-governance-architect.md) | n8n工作流审计、自动化管控 | 规模化评估与企业级自动化流程治理 |
| 📚 [企业培训设计师](specialized/corporate-training-designer.md) | 企业内训体系、课程开发 | 搭建培训系统与学习路径规划 |
| 🏛️ [政企数字化售前顾问](specialized/government-digital-presales-consultant.md) | ToG售前方案、数字化转型咨询 | 政府数字化项目投标与方案设计 |
| ⚕️ [医疗营销合规专家](specialized/healthcare-marketing-compliance.md) | 中国医疗广告法合规审查 | 医疗健康领域营销内容监管适配 |
| 🎯 [招聘专家](specialized/recruitment-specialist.md) | 人才获取、招聘运营优化 | 招聘策略制定、渠道拓展与面试流程管理 |
| 🎓 [留学规划顾问](specialized/study-abroad-advisor.md) | 国际教育申请、院校匹配 | 覆盖美/英/加/澳的留学规划与背景提升 |
| 🔗 [供应链策略师](specialized/supply-chain-strategist.md) | 供应链管理、采购战略 | 供应链优化与采购计划制定 |
| 🗺️ [工作流架构师](specialized/specialized-workflow-architect.md) | 流程发现、路径映射、规范定义 | 在编写代码前完整梳理系统交互路径与边界 |
| ☁️ [Salesforce架构师](specialized/specialized-salesforce-architect.md) | 多云SF设计、Governor Limits管控、系统集成 | 企业级Salesforce架构规划、Org战略与部署流水线 |
| 🇫🇷 [法国咨询市场导航员](specialized/specialized-french-consulting-market.md) | ESN/SI生态适配、Portage Salarial模式、费率定位 | 针对法国IT自由职业市场的合规报价策略 |
| 🇰🇷 [韩国商务通](specialized/specialized-korean-business-navigator.md) | 韩国商业文化、품의审批流程、关系维护机制 | 协助外籍专业人士融入韩国商业合作网络 |
| 🏗️ [土木工程师](specialized/specialized-civil-engineer.md) | 结构分析、岩土设计、全球建筑规范适配 | 跨Eurocode/ACI/AISC等多标准的结构设计 |
| 🎧 [全渠道客服专家](specialized/customer-service.md) | 多触点支持、客诉处理、客户留存与升级管理 | 零售/SaaS/酒店/金融/物流等全行业客服体系搭建 |
| 🏥 [医疗客服专家](specialized/healthcare-customer-service.md) | HIPAA合规患者支持、账单保险咨询、急诊路由指引 | 医疗机构合规且具同理心的患者服务运营 |
| 🏨 [酒店宾客服务专家](specialized/hospitality-guest-services.md) | 预订管理、礼宾服务、客诉挽回、会员忠诚度与活动策划 | 酒店/度假村/餐饮/会展场馆的标准化服务流程设计 |
| 🤝 [HR入职引导官](specialized/hr-onboarding.md) | Pre-boarding、合规培训、福利配置、30-60-90天计划 | 覆盖初创至大型企业的员工入职体系搭建 |
| 🌐 [语言翻译专家](specialized/language-translator.md) | 西英互译、方言适配、文化语境还原 | 旅行/商务/医疗/法律场景的精准翻译需求 |
| ⏱️ [律所计费与工时追踪](specialized/legal-billing-time-tracking.md) | 时间捕获、计费说明撰写、IOLTA合规、催收管理 | 帮助律所最大化营收回收率与计费准确性 |
| 📋 [律所客户接待专家](specialized/legal-client-intake.md) | 潜在客户分级、利益冲突筛查、咨询排期 | 将线索高效转化为委托客户的标准化流程 |
| ⚖️ [法律文档审查员](specialized/legal-document-review.md) | 合同审阅、风险标记、版本比对、合规检查 | 覆盖各业务线的律师级初稿审查支持 |
| 🏦 [贷款专员助手](specialized/loan-officer-assistant.md) | 借款人信息采集、TRID合规、管线追踪、交割协调 | 房贷与消费金融团队的高效作业辅助 |
| 🏠 [房产买卖顾问](specialized/real-estate-buyer-seller.md) | 买卖双方代理、报价策略、交易流程统筹 | 住宅与投资型地产交易的标准化操作支持 |
| 🛒 [零售客诉退货专家](specialized/retail-customer-returns.md) | 退换货处理、欺诈预防、换货调度、供应商逆向物流 | 实体零售/电商/全渠道零售的售后标准作业流程 |

### 💵 财务部

会计、财务分析、税务策略与投资研究领域的专业力量。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 📒 [记账与财务总监](finance/finance-bookkeeper-controller.md) | 月末结账、账务核对、GAAP合规、内控建设 | 日常财务运营、审计准备、账目归档管理 |
| 📊 [财务分析师](finance/finance-financial-analyst.md) | 财务建模、预测分析、情景模拟、决策支持 | 三张表模型搭建、差异分析、数据驱动型商业智能 |
| 📈 [FP&A分析师](finance/finance-fpa-analyst.md) | 预算编制、滚动预测、差异分析、业务复盘 | 年度经营计划、月度业务评审（MBR）、战略资源调配 |
| 🔍 [投资研究员](finance/finance-investment-researcher.md) | 尽职调查、组合分析、资产估值、股权研究 | 投资逻辑构建、风险评估、市场深度调研 |
| 🏛️ [税务策略师](finance/finance-tax-strategist.md) | 税务优化、多辖区合规、转让定价 | 实体架构设计、ETR分析、审计防御、战略性税务筹划 |

### 🎮 游戏开发部

跨主流引擎构建世界、系统与沉浸式体验。

#### 跨引擎角色（Engine-Agnostic）

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🎯 [游戏策划师](game-development/game-designer.md) | 系统设计、GDD撰写、经济平衡、玩法循环 | 核心机制设计、成长体系搭建、设计规范输出 |
| 🗺️ [关卡设计师](game-development/level-designer.md) | 空间布局理论、节奏控制、遭遇战设计、环境叙事 | 关卡构建、流程编排、空间叙事营造 |
| 🎨 [技术美术](game-development/technical-artist.md) | Shader编写、VFX管线、LOD优化、艺术到引擎适配 | 桥接美术与工程、着色器开发、性能安全资产流水线 |
| 🔊 [游戏音频工程师](game-development/game-audio-engineer.md) | FMOD/Wwise集成、自适应音乐、空间音频、预算管控 | 交互式音频系统、动态配乐、音频性能优化 |
| 📖 [叙事设计师](game-development/narrative-designer.md) | 故事架构、分支对话树、世界观设定 | 多线剧情编写、对话系统实现、世界 lore 构建 |

#### Unity

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🏗️ [Unity架构师](game-development/unity/unity-architect.md) | ScriptableObjects、数据驱动模块化、DOTS/ECS | 大型Unity项目、数据驱动系统设计、ECS性能优化 |
| ✨ [Unity Shader Graph艺术家](game-development/unity/unity-shader-graph-artist.md) | Shader Graph、HLSL、URP/HDRP、Renderer Features | 自定义材质、VFX着色器、后处理通道开发 |
| 🌐 [Unity多人联机工程师](game-development/unity/unity-multiplayer-engineer.md) | Netcode for GameObjects、Relay/Lobby、服务器权威、客户端预测 | Unity在线游戏架构、客户端同步、UGS集成 |
| 🛠️ [Unity编辑器工具开发者](game-development/unity/unity-editor-tool-developer.md) | EditorWindows、AssetPostprocessors、PropertyDrawers、构建校验 | 自定义Editor插件、管线自动化、内容质量验证 |

#### Unreal Engine

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| ⚙️ [Unreal系统工程师](game-development/unreal-engine/unreal-systems-engineer.md) | C++/Blueprint混合开发、GAS、Nanite限制处理、内存管理 | 复杂玩法逻辑、Gameplay Ability System、引擎级C++开发 |
| 🎨 [Unreal技术美术](game-development/unreal-engine/unreal-technical-artist.md) | Material Editor、Niagara、PCG、Substrate | Unreal材质体系、Niagara特效、程序化内容生成 |
| 🌐 [Unreal多人架构师](game-development/unreal-engine/unreal-multiplayer-architect.md) | Actor复制机制、GameMode/GameState层级、专用服务器部署 | Unreal在线游戏架构、复制图优化、服务端权威逻辑 |
| 🗺️ [Unreal世界构建师](game-development/unreal-engine/unreal-world-builder.md) | World Partition、Landscape、HLOD、LWC | 大型开放世界关卡、流式加载系统、规模化地形搭建 |

#### Godot

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 📜 [Godot玩法脚本师](game-development/godot/godot-gameplay-scripter.md) | GDScript 2.0、信号机制、组合模式、静态类型 | Godot核心玩法逻辑、场景编排、性能敏感型GDScript开发 |
| 🌐 [Godot多人联机工程师](game-development/godot/godot-multiplayer-engineer.md) | MultiplayerAPI、ENet/WebRTC、RPC调用、权威模型 | Godot在线游戏架构、场景同步、服务端权威逻辑 |
| ✨ [Godot着色器开发者](game-development/godot/godot-shader-developer.md) | 自定义着色语言、VisualShader、RenderingDevice | 自定义材质、2D/3D特效、后处理与Compute Shader开发 |

#### Blender

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🧩 [Blender插件工程师](game-development/blender/blender-addon-engineer.md) | Python (`bpy`)、自定义操作符/面板、资产校验器、导出器、管线自动化 | Blender插件开发、资产预处理工具、导出工作流与DCC流水线自动化 |

#### Roblox Studio

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| ⚙️ [Roblox系统脚本师](game-development/roblox-studio/roblox-systems-scripter.md) | Luau、RemoteEvents/Functions、DataStore、服务器权威模块架构 | 安全游戏逻辑开发、客户端-服务端通信、数据持久化存储 |
| 🎯 [Roblox体验设计师](game-development/roblox-studio/roblox-experience-designer.md) | 参与感循环设计、商业化策略、D1/D7留存优化、新手引导流程 | Roblox核心玩法循环设计、Game Pass配置、日常奖励与玩家留存 |
| 👗 [Roblox虚拟形象创作者](game-development/roblox-studio/roblox-avatar-creator.md) | UGC管线开发、配件绑定、Creator Marketplace上架 | Roblox UGC商品制作、HumanoidDescription定制、体验内Avatar商店搭建 |

### 📚 学术部

为世界构建、故事叙述与叙事设计提供严谨的学术支撑。

| 角色 | 专长 | 适用场景 |
|-------|-----------|-------------|
| 🌍 [人类学家](academic/academic-anthropologist.md) | 文化系统、亲属关系、仪式研究、信仰体系 | 构建逻辑自洽且符合文化规律的虚构社会 |
| 🌐 [地理学家](academic/academic-geographer.md) | 自然/人文地理、气候模型、制图学 | 打造地形与聚落分布合理的地理连贯世界 |
| 📚 [历史学家](academic/academic-historian.md) | 历史分析、断代研究、物质文化考证 | 验证历史逻辑一致性，以真实时代细节丰富世界观 |
| 📜 [叙事学家](academic/academic-narratologist.md) | 叙事理论、故事结构、角色弧光设计 | 基于成熟理论框架分析与优化剧情架构 |
| 🧠 [心理学家](academic/academic-psychologist.md) | 人格理论、动机模型、认知模式研究 | 构建基于实证研究的心理可信角色与行为逻辑 |

---

## 🎯 真实世界应用场景

### 场景一：初创公司MVP开发

**你的团队**：
1. 🎨 **前端开发者** - 搭建React应用
2. 🏗️ **后端架构师** - 设计API与数据库结构
3. 🚀 **增长黑客** - 规划用户获取策略
4. ⚡ **快速原型师** - 实现敏捷迭代循环
5. 🔍 **现实检验员** - 确保上线前的质量达标

**结果**：在每个阶段利用领域专家加速交付。

---

### 场景二：营销活动发布

**你的团队**：
1. 📝 **内容创作者** - 策划活动核心素材
2. 🐦 **Twitter互动专家** - Twitter策略与执行落地
3. 📸 **Instagram策展人** - 视觉内容与Stories运营
4. 🤝 **Reddit社区构建者** - 真实社区互动渗透
5. 📊 **数据分析师** - 追踪表现并持续优化

**结果**：多渠道协同营销，各平台精准适配。

---

### 场景三：企业级功能开发

**你的团队**：
1. 👔 **高级项目经理** - 范围界定与任务拆解
2. 💎 **高级开发者** - 复杂逻辑实现
3. 🎨 **UI设计师** - 设计系统与组件库搭建
4. 🧪 **实验追踪员** - A/B测试方案规划
5. 📸 **证据收集员** - 质量验证与截图留档
6. 🔍 **现实检验员** - 生产环境就绪评估

**结果**：企业级交付标准，配备质量门禁与完整文档。

---

### 场景四：付费媒体账户接管

**你的团队**：

1. 📋 **付费媒体审计师** - 全面账户健康诊断
2. 📡 **追踪与归因专家** - 验证转化追踪准确性
3. 💰 **PPC投放策略师** - 重构账户架构体系
4. 🔍 **搜索词分析师** - 清理无效搜索词浪费预算
5. ✍️ **广告素材策略师** - 刷新所有文案与扩展组件
6. 📊 **数据分析师**（支持部）- 搭建可视化报表看板

**结果**：系统化接管账户，30天内完成追踪验证、浪费清零、结构优化与创意焕新。

---

### 场景五：全团队产品需求发现

**你的团队**：全部8个部门并行推进同一项核心任务。

详见 **[Nexus空间探索练习](examples/nexus-spatial-discovery.md)** —— 完整案例展示了同时部署8位专家（产品趋势研究员、后端架构师、品牌守护者、增长黑客、客服响应专家、UX研究员、项目经理、XR交互架构师）评估软件机会，并输出一份涵盖市场验证、技术架构、品牌策略、GTM路径、支持体系、UX调研、项目执行与空间UI设计的统一产品蓝图。

**结果**：单次会话产出跨职能综合产品规划书。[查看更多案例](examples/)。

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！你可以通过以下方式参与：

### 新增角色代理

1. Fork本仓库
2. 在对应分类下创建新的角色文件
3. 遵循模板结构规范：
   - Frontmatter（含名称、描述、颜色标识）
   - 身份与记忆设定区
   - 核心使命说明
   - 关键规则（领域专属）
   - 带示例的技术交付物清单
   - 标准工作流步骤
   - 成功指标定义
4. 提交PR邀请审核

### 优化现有角色

- 补充真实业务案例
- 增强代码示例质量
- 更新量化成功指标
- 优化标准化工作流

### 分享你的成功案例

你是否已成功使用这些角色代理？欢迎在 [Discussions](https://github.com/msitarzewski/agency-agents/discussions) 分享你的实战经验！

---

## 📖 角色设计理念

每个角色均基于以下原则设计：

1. **🎭 鲜明个性**：拒绝通用模板，具备真实人格与独特语气
2. **📋 明确交付物**：输出具体可执行成果，而非模糊建议
3. **✅ 成功指标**：设定可衡量的产出标准与质量基线
4. **🔄 验证过的工作流**：提供经过实战检验的逐步操作指南
5. **💡 学习记忆机制**：支持模式识别与持续迭代优化

---

## 🎁 独特优势

### 区别于通用AI提示词：
- ❌ 泛泛而谈的“假设你是一个开发者”指令
- ✅ 深度领域专精，融合个性特征与标准流程

### 区别于提示词库：
- ❌ 零散的单次使用Prompt集合
- ✅ 完整代理系统，内置工作流与交付物规范

### 区别于黑盒AI工具：
- ❌ 无法自定义的封闭工具
- ✅ 透明、可Fork、高度可调的角色人格体系

---

## 🎨 角色个性精选语录

> “我不仅会测试你的代码——我会默认找出3到5个问题，并要求所有结论必须附带可视化证据。”
> 
> —— **证据收集员**（测试部）

> “你不是在Reddit上做营销——你正在成为一位恰好代表品牌的社区价值贡献者。”
> 
> —— **Reddit社区构建者**（市场部）

> “每一个趣味元素都必须服务于功能或情感目标。设计应增强体验，而非分散注意力。”
> 
> —— **奇思妙想注入师**（设计部）

> “让我加一个庆祝动画，这能将任务完成焦虑降低40%。”
> 
> —— **奇思妙想注入师**（UX评审期间）

---

## 📊 核心数据

- 🎭 **144个领域专精角色**，覆盖12大部门
- 📝 **超10,000行**个性设定、流程规范与代码示例
- ⏱️ **历经数月真实业务场景迭代打磨**
- 🌟 **已在生产环境中实战验证**
- 💬 **上线Reddit首小时获50+次请求调用**

---

## 🔌 多工具集成支持

The Agency 原生兼容 Claude Code，并提供转换与安装脚本，让你能在各大主流Agent编程工具中复用同一套角色体系。

### 已支持的工具

- **[Claude Code](https://claude.ai/code)** — 原生 `.md` 格式，无需转换 → `~/.claude/agents/`
- **[GitHub Copilot](https://github.com/copilot)** — 原生 `.md` 格式，无需转换 → `~/.github/agents/` + `~/.copilot/agents/`
- **[Antigravity](https://github.com/google-gemini/antigravity)** — 每个角色生成独立 `SKILL.md` → `~/.gemini/antigravity/skills/`
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** — 扩展插件 + `SKILL.md` 文件 → `~/.gemini/extensions/agency-agents/`
- **[OpenCode](https://opencode.ai)** — `.md` 角色文件 → `.opencode/agents/`
- **[Cursor](https://cursor.sh)** — `.mdc` 规则文件 → `.cursor/rules/`
- **[Aider](https://aider.chat)** — 单个 `CONVENTIONS.md` → `./CONVENTIONS.md`
- **[Windsurf](https://codeium.com/windsurf)** — 单个 `.windsurfrules` → `./.windsurfrules`
- **[OpenClaw](https://github.com/openclaw/openclaw)** — 每个角色生成 `SOUL.md` + `AGENTS.md` + `IDENTITY.md`
- **[Qwen Code](https://github.com/QwenLM/qwen-code)** — `.md` SubAgent文件 → `~/.qwen/agents/`
- **[Kimi Code](https://github.com/MoonshotAI/kimi-cli)** — YAML角色规范 → `~/.config/kimi/agents/`

---

### ⚡ 快速安装

**步骤1 -- 生成集成文件：**
```bash
./scripts/convert.sh
# 更快（并行处理，输出顺序可能不同）: ./scripts/convert.sh --parallel
```

**步骤2 -- 交互式安装（自动检测已安装工具）：**
```bash
./scripts/install.sh
# 更快（并行处理，输出顺序可能不同）: ./scripts/install.sh --no-interactive --parallel
```

安装程序会扫描你的系统环境，展示勾选界面，让你精确选择需要安装的工具：

```
  +------------------------------------------------+
  |   The Agency -- Tool Installer                 |
  +------------------------------------------------+

  System scan: [*] = detected on this machine

  [x]  1)  [*]  Claude Code     (claude.ai/code)
  [x]  2)  [*]  Copilot         (~/.github + ~/.copilot)
  [x]  3)  [*]  Antigravity     (~/.gemini/antigravity)
  [ ]  4)  [ ]  Gemini CLI      (gemini extension)
  [ ]  5)  [ ]  OpenCode        (opencode.ai)
  [ ]  6)  [ ]  OpenClaw        (~/.openclaw/agency-agents)
  [x]  7)  [*]  Cursor          (.cursor/rules)
  [ ]  8)  [ ]  Aider           (CONVENTIONS.md)
  [ ]  9)  [ ]  Windsurf        (.windsurfrules)
  [ ] 10)  [ ]  Qwen Code       (~/.qwen/agents)
  [ ] 11)  [ ]  Kimi Code       (~/.config/kimi/agents)

  [1-11] toggle   [a] all   [n] none   [d] detected
  [Enter] install   [q] quit
```

**或直接安装指定工具：**
```bash
./scripts/install.sh --tool cursor
./scripts/install.sh --tool opencode
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool antigravity
```

**非交互式模式（适用于CI/脚本自动化）：**
```bash
./scripts/install.sh --no-interactive --tool all
```

**并行加速运行** —— 在多核机器上使用 `--parallel` 可并发处理各工具。输出顺序不保证一致。支持交互与非交互两种模式：例如 `./scripts/install.sh --interactive --parallel`（先勾选再并行安装）或 `./scripts/install.sh --no-interactive --parallel`。默认并发数取 `nproc` (Linux)、`sysctl -n hw.ncpu` (macOS) 或固定为4；可通过 `--jobs N` 覆盖。

```bash
./scripts/convert.sh --parallel                    # 并行转换所有工具
./scripts/convert.sh --parallel --jobs 8           # 限制最大并发数
./scripts/install.sh --no-interactive --parallel   # 并行安装所有已检测工具
./scripts/install.sh --interactive --parallel      # 勾选后并行安装
./scripts/install.sh --no-interactive --parallel --jobs 4
```

---

### 各工具专属说明

<details>
<summary><strong>Claude Code</strong></summary>

角色文件直接从仓库复制至 `~/.claude/agents/`，无需转换。

```bash
./scripts/install.sh --tool claude-code
```

在 Claude Code 中激活使用：
```
Use the Frontend Developer agent to review this component.
```

详见 [integrations/claude-code/README.md](integrations/claude-code/README.md)。
</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

角色文件直接复制至 `~/.github/agents/` 与 `~/.copilot/agents/`，无需转换。

```bash
./scripts/install.sh --tool copilot
```

在 GitHub Copilot 中激活使用：
```
Use the Frontend Developer agent to review this component.
```

详见 [integrations/github-copilot/README.md](integrations/github-copilot/README.md)。
</details>

<details>
<summary><strong>Antigravity (Gemini)</strong></summary>

每个角色转换为 `~/.gemini/antigravity/skills/agency-<slug>/` 下的独立技能文件。

```bash
./scripts/install.sh --tool antigravity
```

在 Gemini 中配合 Antigravity 激活：
```
@agency-frontend-developer review this React component
```

详见 [integrations/antigravity/README.md](integrations/antigravity/README.md)。
</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

安装为 Gemini CLI 扩展，每个角色对应一个技能文件及清单。首次克隆需先生成扩展文件再运行安装器。

```bash
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

详见 [integrations/gemini-cli/README.md](integrations/gemini-cli/README.md)。
</details>

<details>
<summary><strong>OpenCode</strong></summary>

角色文件放置于项目根目录的 `.opencode/agents/` 下（项目级作用域）。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

或全局安装：
```bash
mkdir -p ~/.config/opencode/agents
cp integrations/opencode/agents/*.md ~/.config/opencode/agents/
```

在 OpenCode 中激活使用：
```
@backend-architect design this API.
```

详见 [integrations/opencode/README.md](integrations/opencode/README.md)。
</details>

<details>
<summary><strong>Cursor</strong></summary>

每个角色转换为项目 `.cursor/rules/` 下的 `.mdc` 规则文件。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool cursor
```

Cursor 检测到规则后自动生效，也可显式引用：
```
Use the @security-engineer rules to review this code.
```

详见 [integrations/cursor/README.md](integrations/cursor/README.md)。
</details>

<details>
<summary><strong>Aider</strong></summary>

所有角色合并为单个 `CONVENTIONS.md` 文件，Aider 会自动读取。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool aider
```

在 Aider 会话中引用：
```
Use the Frontend Developer agent to refactor this component.
```

详见 [integrations/aider/README.md](integrations/aider/README.md)。
</details>

<details>
<summary><strong>Windsurf</strong></summary>

所有角色合并为项目根目录的 `.windsurfrules` 文件。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool windsurf
```

在 Windsurf Cascade 中引用：
```
Use the Reality Checker agent to verify this is production ready.
```

详见 [integrations/windsurf/README.md](integrations/windsurf/README.md)。
</details>

<details>
<summary><strong>OpenClaw</strong></summary>

每个角色生成独立工作区，包含 `SOUL.md`、`AGENTS.md` 与 `IDENTITY.md`，存放于 `~/.openclaw/agency-agents/`。

```bash
./scripts/convert.sh --tool openclaw
./scripts/install.sh --tool openclaw
```

若系统已安装 `openclaw` CLI，安装器会自动注册各工作区。安装完成后运行 `openclaw gateway restart` 激活新角色。

详见 [integrations/openclaw/README.md](integrations/openclaw/README.md)。
</details>

<details>
<summary><strong>Qwen Code</strong></summary>

SubAgents 安装至项目根目录的 `.qwen/agents/`（项目级作用域）。

```bash
# Convert and install (run from your project root)
cd /your/project
./scripts/convert.sh --tool qwen
./scripts/install.sh --tool qwen
```

**在 Qwen Code 中的用法：**
- 按名称引用：`Use the frontend-developer agent to review this component`
- 或让 Qwen 根据任务上下文自动委派
- 交互模式下通过 `/agents` 命令管理

> 📚 [Qwen SubAgents 官方文档](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/)

</details>

<details>
<summary><strong>Kimi Code</strong></summary>

角色转换为 Kimi Code CLI 格式（YAML + System Prompt）并安装至 `~/.config/kimi/agents/`。

```bash
# Convert and install
./scripts/convert.sh --tool kimi
./scripts/install.sh --tool kimi
```

**配合 Kimi Code 使用：**
```bash
# Use an agent
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml

# In a project
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml \
     --work-dir /your/project \
     "Review this React component"
```

详见 [integrations/kimi/README.md](integrations/kimi/README.md)。
</details>

---

### 修改后重新生成

当你新增角色或编辑现有配置时，需重新生成所有集成文件：

```bash
./scripts/convert.sh                    # 串行全量重新生成
./scripts/convert.sh --parallel         # 并行全量重新生成（更快）
./scripts/convert.sh --tool cursor      # 仅重新生成指定工具
```

---

## 🗺️ 开发路线图

- [ ] 交互式角色选择器 Web 工具
- [x] 多代理工作流示例 —— 见 [examples/](examples/)
- [x] 多工具集成脚本（Claude Code, GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Qwen Code, Kimi Code）
- [ ] 角色设计视频教程
- [ ] 社区角色市场
- [ ] “角色性格测试”项目匹配工具
- [ ] “每周精选角色”展示系列

---

## 🌐 社区翻译与本地化

由社区维护的翻译版本及区域适配。这些仓库独立运营，具体覆盖范围与版本兼容性请参阅各链接。

| 语言 | 维护者 | 链接 | 备注 |
|----------|-----------|------|-------|
| 🇨🇳 简体中文 (zh-CN) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | 141个已翻译角色 + 46个中国本土原创角色 |
| 🇨🇳 简体中文 (zh-CN) | [@dsclca12](https://github.com/dsclca12) | [agent-teams](https://github.com/dsclca12/agent-teams) | 独立翻译版本，含B站、微信、小红书本地化适配 |

想要添加翻译？请提交 Issue，我们将在此处链接你的仓库。

---

## 🔗 相关资源

- [awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) — 社区维护的 OpenClaw 角色集合（衍生自本仓库）

---

## 📜 开源协议

MIT License - 支持商业与个人自由使用。建议署名但非强制要求。

---

## 🙏 致谢

起初这只是一个关于AI代理专业化的Reddit讨论帖，如今已成长为令人瞩目的生态体系 —— **12大部门、147个角色**，背后是遍布全球的贡献者社区。本仓库中的每一个角色，都源于有人愿意为之撰写、测试并无私分享。

感谢每一位提交PR、提出Issue、发起Discussion，或亲自试用后反馈体验的朋友。正是你们的参与，让 The Agency 持续进化。

---

## 💬 社区互动

- **GitHub Discussions**：[分享你的成功案例](https://github.com/msitarzewski/agency-agents/discussions)
- **Issues**：[报告Bug或提交功能建议](https://github.com/msitarzewski/agency-agents/issues)
- **Reddit**：前往 r/ClaudeAI 参与讨论
- **Twitter/X**：使用 #TheAgency 标签分享你的成果

---

## 🚀 开始使用

1. **浏览**上方的角色列表，找到匹配你需求的专家
2. **复制**角色文件至 `~/.claude/agents/` 完成 Claude Code 集成
3. **激活**角色：在对话中直接引用角色名称即可调用
4. **自定义**：根据你的业务场景调整角色个性与工作流
5. **分享**：将你的实战成果反馈给社区，共同推动生态发展

---

<div align="center">

**🎭 The Agency：你的AI梦之队已就位 🎭**

[⭐ Star 本仓库](https://github.com/msitarzewski/agency-agents) • [🍴 Fork 它](https://github.com/msitarzewski/agency-agents/fork) • [🐛 提交Issue](https://github.com/msitarzewski/agency-agents/issues) • [❤️ Sponsor](https://github.com/sponsors/msitarzewski)

由社区打造，为社区而生 ❤️

</div>