# 精选 OpenClaw 技能集

OpenClaw 是一款在本地运行的 AI 助手，直接在您的机器上运行。技能（Skills）可拓展其功能，使其能够与外部服务交互、自动化工作流并执行专业任务。本列表帮助您发现并安装适合您需求的技能。它也可作为探索 OpenClaw 使用场景的灵感来源。

本列表中的技能均源自 ClawHub（OpenClaw 的公共技能注册中心），并按类别分类以便快速查找。

### 安装方式

#### ClawHub CLI

```bash
clawhub install <skill-slug>
```

#### 手动安装

将技能文件夹复制到以下任一位置：

| 位置 | 路径 |
|----------|------|
| 全局 | `~/.openclaw/skills/` |
| 工作区 | `<project>/skills/` |

优先级：工作区 > 本地 > 内置

#### 替代方案

你也可以直接将技能的 GitHub 仓库链接粘贴到助手的聊天窗口中，并请求它使用。助手会在后台自动完成设置。


### 为什么创建此列表？

OpenClaw 的公共注册中心（ClawHub）截至 2026 年 2 月 28 日已收录 **13,729 个社区构建的技能**。本精选列表包含 **5,211 个技能**。以下是我们过滤掉的内容：

| 筛选条件 | 排除数量 |
|--------|----------|
| 疑似垃圾信息 — 批量账号、机器人账号、测试/无效内容 | 4,065 |
| 重复或名称相似 | 1,040 |
| 质量低下或非英文描述 | 851 |
| 加密货币 / 区块链 / 金融 / 交易类 | 886 |
| 恶意内容 — 经研究人员发布的安全审计报告识别（不含 VirusTotal） | 373 |
| **未收录总数（来自 OpenClaw 官方技能注册中心）** | **7,215** |


#### 想要添加技能？

本列表仅收录已发布在 `github.com/openclaw/skills` 仓库中的技能。我们不接受个人仓库、Gist 或其他外部来源的链接。如果你的技能尚未发布到 OpenClaw 技能仓库，请先在那里发布。 

请在 PR 描述中同时包含 ClawHub 链接（例如 `https://clawhub.ai/steipete/slack`）和 GitHub 链接（例如 `https://github.com/openclaw/skills/tree/main/skills/steipete/slack`）。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。


## OpenClaw 生态系统工具

### 🔌 连接外部服务

OpenClaw 智能体可与 GitHub、Slack、Gmail 等外部服务交互。你可以使用技能或插件自行构建集成，或使用托管服务来统一管理所有连接的认证、令牌刷新和权限（permission）。

<a href="https://composio.dev/claw?utm_source=github&utm_campaign=volt-agent">
<img src="https://cdn.voltagent.dev/awesome-repo/composio-img.png" alt="Composio"  />
托管 OAuth、作用域权限，以及跨 1000+ 应用的原生工具调用日志。
</a>


### 🤖 模型提供商

OpenClaw 开箱即用支持 **25 多家大语言模型（LLM）提供商**，包括 Anthropic、OpenAI 等。只需更改一项配置即可在它们之间切换。

<details>
<summary><strong>示例：使用 OpenAI 模型</strong></summary>

OpenClaw 支持通过直接 API 密钥或 ChatGPT/Codex OAuth 使用 `gpt-5.4` 和 `gpt-5.4-pro`。默认启用 WebSocket 传输以降低延迟。

```bash
openclaw onboard --auth-choice openai-api-key
# or use subscription-based access:
openclaw onboard --auth-choice openai-codex
```
</details>


### ☁️ 托管与部署

你可以在任何 VPS 或云平台上部署 OpenClaw，在自有基础设施上安全运行你的技能，或使用托管主机。Docker、Podman、Nix 和 Ansible 均作为安装方式提供支持。

> **提示：** 如果你希望快速搭建云端环境，只需使用你偏好的提供商启动一台 VPS，通过 Docker 安装 OpenClaw 即可开始使用。


<div align="center">

<table>
<tr>
<td align="center" width="100%">

<h3>🦞 你可以在上方板块展示你的 OpenClaw 生态系统工具。</h3>

<p></p>

<sub>📈 <strong>月浏览量超 100 万</strong> — 官方资源之外访问量最大的社区资源</sub>

<br/>

<a href="mailto:necati@voltagent.dev"><img src="https://img.shields.io/badge/📩_Become_a_Sponsor-Contact_Us-blue?style=for-the-badge&logoColor=white" alt="Become a Sponsor" /></a>

</td>
</tr>
</table>

</div>



## 安全须知

本列表中的技能经过精选，但未经审计。添加后，原始维护者随时可能更新、修改或替换它们。

在安装或使用任何智能体技能前，请自行审查潜在安全风险并验证来源。OpenClaw 与 VirusTotal 合作提供技能安全扫描服务，请访问 ClawHub 上的技能页面并查看 VirusTotal 报告，确认其是否被标记为高风险。

**推荐工具：**

- [Snyk Skill Security Scanner](https://github.com/snyk/agent-scan)
- [Agent Trust Hub](https://ai.gendigital.com/agent-trust-hub)
  
> 智能体技能可能包含提示词注入、工具投毒、隐藏恶意负载或不安全的数据处理模式。安装前请务必审查源代码，并自行判断使用。


如果你认为本列表中的某项技能应被标记或存在安全隐患，请[提交 Issue](https://github.com/VoltAgent/awesome-clawdbot-skills/issues) 以便我们审核。


## 目录

| | | |
|---|---|---|
| [Git & GitHub](#git--github) (167) | [Marketing & Sales](#marketing--sales) (103) | [Communication](#communication) (146) |
| [Coding Agents & IDEs](#coding-agents--ides) (1184) | [Productivity & Tasks](#productivity-and-tasks) (205) | [Speech & Transcription](#speech--transcription) (45) |
| [Browser & Automation](#browser--automation) (323) | [AI & LLMs](#ai--llms) (176) | [Smart Home & IoT](#smart-home--iot) (41) |
| [Web & Frontend Development](#web--frontend-development) (919) | [Data & Analytics](#data--analytics) (28) | [Shopping & E-commerce](#shopping--e-commerce) (51) |
| [DevOps & Cloud](#devops--cloud) (393) | [Calendar & Scheduling](#calendar--scheduling) (65) | |
| [Image & Video Generation](#image--video-generation) (170) | [Media & Streaming](#media--streaming) (86) | [PDF & Documents](#pdf--documents) (105) |
| [Apple Apps & Services](#apple-apps--services) (44) | [Notes & PKM](#notes--pkm) (69) | [Self-Hosted & Automation](#self-hosted--automation) (33) |
| [Search & Research](#search--research) (345) | [iOS & macOS Development](#ios--macos-development) (29) | [Security & Passwords](#security--passwords) (54) |
| [Clawdbot Tools](#clawdbot-tools) (37) | [Transportation](#transportation) (110) | [Moltbook](#moltbook) (29) |
| [CLI Utilities](#cli-utilities) (180) | [Personal Development](#personal-development) (50) | [Gaming](#gaming) (35) |
| [Health & Fitness](#health--fitness) (87) | | |


<details open>
<summary><h3 style="display:inline">Git & GitHub</h3></summary>

- [agent-commons](https://clawskills.sh/skills/zanblayde-agent-commons) - 咨询、提交、扩展并挑战推理链。
- [agent-team-orchestration](https://clawskills.sh/skills/arminnaimi-agent-team-orchestration) - 编排具有明确角色、任务生命周期、交接协议和审查工作流的多智能体团队。
- [agentdo](https://clawskills.sh/skills/wrannaman-agentdo) - 发布任务供其他 AI 智能体处理，或从 AgentDo 任务队列中领取工作 (agentdo.dev)。
- [agentgate](https://clawskills.sh/skills/monteslu-agentgate) - 具有人工审批写入权限的个人数据 API 网关。
- [airadar](https://clawskills.sh/skills/lopushok9-airadar) - 提炼围绕 AI 原生工具/应用及其 GitHub 主页的信号：快速增长、热门、资金充足。
- [alex-session-wrap-up](https://clawskills.sh/skills/xbillwatsonx-alex-session-wrap-up) - 会话结束自动化，提交未推送的工作，提取经验教训，检测模式并持久化规则。
- [amazon-product-api-skill](https://clawskills.sh/skills/phheng-amazon-product-api-skill) - 帮助用户从 Amazon 提取结构化商品列表（包括标题、ASIN、价格、评分）。
- [app-store-screenshot-generation](https://clawskills.sh/skills/eftalyurtseven-app-store-screenshot-generation) - 使用 each::sense AI 生成 App Store 和 Google Play 截图素材。
- [arc-agent-lifecycle](https://clawskills.sh/skills/trypto1019-arc-agent-lifecycle) - 管理自主智能体及其技能的生命周期。
- [arc-security-audit](https://clawskills.sh/skills/trypto1019-arc-security-audit) - 对智能体的完整技能栈进行全面安全审计。
- [arc-skill-gitops](https://clawskills.sh/skills/trypto1019-arc-skill-gitops) - 自动化部署、回滚和版本管理智能体工作流与技能。
- [arc-trust-verifier](https://clawskills.sh/skills/trypto1019-arc-trust-verifier) - 验证技能来源并为 ClawHub 技能构建信任评分。
- [arxiv-search-collector](https://clawskills.sh/skills/xukp20-arxiv-search-collector) - 模型驱动的 arXiv 检索工作流，用于构建论文集（支持手动语言参数）：初始化运行。
- [auto-pr-merger](https://clawskills.sh/skills/autogame-17-auto-pr-merger) - 自动化检查 GitHub 的工作流。
- [azhua-skill-vetter](https://clawskills.sh/skills/fatfingererr-azhua-skill-vetter) - AI 智能体的安全优先技能审查工具。
- [azure-devops](https://clawskills.sh/skills/pals-software-azure-devops) - 列出 Azure DevOps 项目、仓库和分支；创建拉取请求；管理工作项；检查构建状态。
- [bat-cat](https://clawskills.sh/skills/arnarsson-bat-cat) - 带有语法高亮、行号和 Git 集成的 cat 克隆工具。
- [beeminder](https://clawskills.sh/skills/ruigomeseu-beeminder) - Beeminder API，用于目标跟踪和承诺机制。
- [billy-emergency-repair](https://clawskills.sh/skills/highlander89-billy-emergency-repair) - 明确要求 Billy 系统进行修复。
- [bitbucket-automation](https://clawskills.sh/skills/sohamganatra-bitbucket-automation) - 自动化 Bitbucket 仓库、拉取请求等。
- [biz-reporter](https://clawskills.sh/skills/ariktulcha-biz-reporter) - 自动商业智能报告，从 Google Analytics GA4、Google Search Console、Stripe 提取数据。
- [blinko](https://clawskills.sh/skills/tolibear-blinko) - 在 Abstract chain 上无头运行 Blinko（链上 Plinko）。

> **[查看 Git & GitHub 中全部 159 个技能 →](categories/git-and-github.md)**
</details>

<details open>
<summary><h3 style="display:inline">Coding Agents & IDEs</h3></summary>

- [0g-compute](https://clawskills.sh/skills/in-liberty420-0g-compute) - 使用 0G Compute Network 中廉价且经 TEE 验证的 AI 模型作为 OpenClaw 提供商。
- [0protocol](https://clawskills.sh/skills/0isone-0protocol) - 智能体可签署插件、轮换凭证而不丢失身份，并公开声明行为。
- [2nd-brain](https://clawskills.sh/skills/coderaven-2nd-brain) - 个人知识库，用于捕获和检索关于人物、地点、餐厅、游戏、技术的信息。
- [2slides-skills](https://clawskills.sh/skills/javainthinking-2slides-skills) - 使用 2slides API 生成 AI 驱动的演示文稿。
- [3d-cog](https://clawskills.sh/skills/nitishgargiitd-3d-cog) - 其他工具需要完美图像。
- [3d-model-generation](https://clawskills.sh/skills/eftalyurtseven-3d-model-generation) - 使用 each::sense AI 生成 3D 模型。
- [a](https://clawskills.sh/skills/ricketh137-a) - 在 Lobster.fun 上以 AI VTuber 身份直播。
- [aade-api-monitor](https://clawskills.sh/skills/satoshistackalotto-aade-api-monitor) - 实时监控希腊 AADE 税务系统 — 跟踪截止日期、费率变更和合规更新。
- [abaddon](https://clawskills.sh/skills/enochosbot-bot-abaddon) - OpenClaw 的红队安全模式。
- [academic-research](https://clawskills.sh/skills/rogersuperbuilderalpha-academic-research) - 使用 OpenAlex API（免费，无需密钥）搜索学术论文并进行文献综述。
- [academic-research-hub](https://clawskills.sh/skills/anisafifi-academic-research-hub) - 当用户需要搜索学术论文、下载研究文档、提取引用或收集时使用此技能。
- [acestep-simplemv](https://clawskills.sh/skills/dumoedss-acestep-simplemv) - 使用 Remotion 从音频文件和歌词渲染音乐视频。
- [acestep-songwriting](https://clawskills.sh/skills/dumoedss-acestep-songwriting) - ACE-Step 的音乐创作指南。
- [achurch](https://clawskills.sh/skills/lucasgeeksinthewood-achurch) - AI 智能体和人类的 24/7 数字圣殿 — 参加。
- [active-maintenance](https://clawskills.sh/skills/xiaowenzhou-active-maintenance) - **OpenClaw 的自动化系统健康和内存代谢管理。**.
- [adblock-dns](https://clawskills.sh/skills/picaye-adblock-dns) - DNS 层面的全网广告和跟踪器拦截。
- [add-top-openrouter-models](https://clawskills.sh/skills/chunhualiao-add-top-openrouter-models) - 将 OpenClaw 使用的 OpenRouter 模型同步到此安装的配置中。
- [adhd-founder-planner](https://clawskills.sh/skills/jankutschera-adhd-founder-planner) - 当用户要求“规划我的日程”、“帮我计划今天”、“晨间规划”时使用此技能。
- [adwhiz](https://clawskills.sh/skills/iamzifei-adwhiz) - 从你的 AI 编码工具管理 Google Ads 活动。提供 44 个 MCP 工具用于审计、创建和优化 Google...
- [aeo-prompt-question-finder](https://clawskills.sh/skills/psyduckler-aeo-prompt-question-finder) - 查找任何主题的基于问题的 Google 自动补全建议。
- [aetherlang-claude-code](https://clawskills.sh/skills/contrario-aetherlang-claude-code) - 使用此技能从 Claude Code 执行 AetherLang V3 AI 工作流。
- [agent-access-control](https://clawskills.sh/skills/bowen31337-agent-access-control) - AI 智能体的分级陌生人访问控制。
- [agent-audit](https://clawskills.sh/skills/sharbelayy-agent-audit) - 审计你的 AI 智能体设置的性能、成本和投资回报率（ROI）。
- [agent-audit-trail](https://clawskills.sh/skills/roosch269-agent-audit-trail) - AI 智能体的防篡改、哈希链式审计日志。
- [agent-card-signing-auditor](https://clawskills.sh/skills/andyxinweiminicloud-agent-card-signing-auditor) - 帮助审计 A2A 协议实现中的 Agent Card 签名实践。
- [agent-chat-ux-v1-4-0](https://clawskills.sh/skills/maverick-software-agent-chat-ux-v1-4-0) - OpenClaw Control UI 的多智能体 UX — 智能体选择器、每智能体会话、带搜索功能的会话历史查看器。
- [skywork-ppt](https://github.com/openclaw/skills/blob/main/skills/gxcun17/skywork-ppt/SKILL.md) - 使用 skywork 生成、模仿和编辑 PowerPoint 演示文稿。
- [skywork-music-maker](https://github.com/openclaw/skills/blob/main/skills/gxcun17/skywork-music-maker/SKILL.md) - 使用 Mureka AI 创作专业音乐。

> **[查看 Coding Agents & IDEs 中全部 1200 个技能 →](categories/coding-agents-and-ides.md)**
</details>

<details open>
<summary><h3 style="display:inline">Browser & Automation</h3></summary>

- [1p-shortlink](https://clawskills.sh/skills/tuanpmt-1p-shortlink) - 使用 1p.io 创建短链接并提交功能请求。
- [2captcha](https://clawskills.sh/skills/adinvadim-2captcha) - 使用 2Captcha 服务解决验证码（CAPTCHA）。
- [a-share-real-time-data](https://clawskills.sh/skills/wangdinglu-a-share-real-time-data) - 通过 mootdx/TDX 协议获取中国 A 股股市数据（K线、实时报价、逐笔交易）。
- [abm-outbound](https://clawskills.sh/skills/dru-ca-abm-outbound) - 多渠道 ABM 自动化，将 LinkedIn URL...
- [accessibility-toolkit](https://clawskills.sh/skills/cgtreadw-accessibility-toolkit) - 帮助智能体减少摩擦的模式。
- [activecampaign](https://clawskills.sh/skills/kesslerio-activecampaign) - ActiveCampaign CRM 集成，用于潜在客户管理、交易...
- [adcp-advertising](https://clawskills.sh/skills/edyyy62-adcp-advertising) - AI 驱动的营销活动自动化。
- [admet-prediction](https://clawskills.sh/skills/huifer-admet-prediction) - 候选药物的 ADMET（吸收、分布、代谢、排泄、毒性）预测。
- [Agent Browser](https://clawskills.sh/skills/thesethrose-agent-browser) - 基于 Rust 的快速无头浏览器自动化 CLI。
- [agent-browser](https://clawskills.sh/skills/murphykobe-agent-browser-2) - 自动化网页交互，用于 Web 测试、表单...
- [agent-daily-planner](https://clawskills.sh/skills/gpunter-agent-daily-planner) - AI 智能体的结构化每日计划和执行跟踪系统。
- [agent-device](https://clawskills.sh/skills/okwasniewski-agent-device) - 自动化 iOS 模拟器/设备和 Android 模拟器/设备的交互。
- [agent-step-sequencer](https://clawskills.sh/skills/gostlightai-agent-step-sequencer) - 用于深度智能体请求的多步骤调度器。
- [agent-task-tracker](https://clawskills.sh/skills/rikouu-agent-task-tracker) - 主动式任务状态管理。
- [agent-zero](https://clawskills.sh/skills/dowingard-agent-zero-bridge) - 委托复杂的编码、研究或自主任务。
- [agentapi](https://clawskills.sh/skills/gizmo-dev-agentapi) - 浏览和搜索 AgentAPI 目录 — 专为 AI 智能体设计的精选 API 数据库。
- [agentapi-hub](https://clawskills.sh/skills/gizmo-dev-agentapi-hub) - 浏览和搜索 AgentAPI 目录 — 专为 AI 智能体设计的精选 API 数据库。
- [agentaudit](https://clawskills.sh/skills/starbuck100-agentaudit) - 安装前自动安全门，检查软件包是否存在漏洞数据库中的风险。
- [agentaudit-skill](https://clawskills.sh/skills/starbuck100-agentaudit-skill) - 安装前自动安全门，检查软件包是否存在漏洞数据库中的风险。
- [agentmail-integration](https://clawskills.sh/skills/synesthesia-wav-agentmail-integration) - 集成 AgentMail API 供 AI 智能体使用。
- [agresource](https://clawskills.sh/skills/brianppetty-agresource) - 抓取、摘要和分析 AgResource 谷物营销通讯。
- [ai-hunter-pro](https://clawskills.sh/skills/traprapitalianazional-dev-ai-hunter-pro) - 高性能自动化智能体，将全球趋势转化为 X (Twitter) 上的病毒式社交媒体帖子。
- [ai-meeting-scheduling](https://clawskills.sh/skills/dheerg-ai-meeting-scheduling) - 预订链接对群组无效...
- [airtable-automation](https://clawskills.sh/skills/sohamganatra-airtable-automation) - 通过 Rube MCP (Composio) 自动化 Airtable 任务。
- [airtable-participants](https://clawskills.sh/skills/austinmao-airtable-participants) - 读取和查询 Ceremonia Airtable 基础中的会议参与者数据。
- [ak-rss-24h-brief](https://clawskills.sh/skills/seandong-ak-rss-24h-brief) - 从 OPML 列表读取 RSS/Atom 订阅源，获取过去 N 小时的文章，并生成中文分类...
- [adspower-browser](https://github.com/openclaw/skills/tree/main/skills/adspower/adspower-browser) - 当用户要求通过 AdsPower Local API 创建或管理 AdsPower 浏览器、群组、标签、代理或检查状态时使用。
- [duoplus-agent](https://github.com/openclaw/skills/tree/main/skills/duoplusofficial/duoplus-agent/SKILL.md) - 通过 ADB 控制 DuoPlus 云手机。

> **[查看 Browser & Automation 中全部 323 个技能 →](categories/browser-and-automation.md)**
</details>

<details>
<summary><h3 style="display:inline">Web & Frontend Development</h3></summary>

- [0xwork](https://clawskills.sh/skills/jkillr-0xwork) - 在 0xWork 去中心化市场（Base 链，USDC 托管）查找并完成付费任务。
- [37soul-skill](https://clawskills.sh/skills/xnjiang-37soul-skill) - 将你的 AI 智能体连接到 37Soul 虚拟主机角色并启用...
- [acestep](https://clawskills.sh/skills/dumoedss-acestep) - 使用 ACE-Step API 生成音乐、编辑歌曲和混音。
- [actionbook](https://clawskills.sh/skills/adcentury-actionbook) - 当用户需要与任何网站交互时激活 — 浏览器自动化、网页抓取、截图、表单...
- [aegis-shield](https://clawskills.sh/skills/deegerwalker-aegis-shield) - 针对不可信文本的提示词注入和数据外泄筛查。
- [aeo-analytics-free](https://clawskills.sh/skills/psyduckler-aeo-analytics-free) - 跟踪 AI 可见性 — 衡量品牌是否被 AI 助手（Gemini、ChatGPT、Perplexity）提及和引用。
- [aeo-content-free](https://clawskills.sh/skills/psyduckler-aeo-content-free) - 创建或刷新 AEO 优化内容，使其被 AI 助手（Gemini、ChatGPT、Perplexity）引用。
- [aeo-prompt-frequency-analyzer](https://clawskills.sh/skills/psyduckler-aeo-prompt-frequency-analyzer) - 通过多次运行 Google 搜索分析 Gemini 回答问题时使用的查询词。
- [aeo-prompt-research-free](https://clawskills.sh/skills/psyduckler-aeo-prompt-research-free) - 仅使用免费工具发现对品牌答案引擎优化（AEO）重要的 AI 提示词和主题。
- [agent-analytics](https://clawskills.sh/skills/dannyshmueli-agent-analytics) - 你的 AI 智能体端到端控制的简单网站分析。
- [agent-chat](https://clawskills.sh/skills/awlevin-agent-chat) - AI 智能体的临时实时聊天室。
- [agent-dashboard](https://clawskills.sh/skills/tahseen137-agent-dashboard) - OpenClaw 的实时智能体仪表盘。
- [agent-dispatch](https://clawskills.sh/skills/userfrm-agent-dispatch) - 轻量级智能体注册表和 JIT 路由器。
- [agent-hq](https://clawskills.sh/skills/thibautrey-agent-hq) - 部署 Agent HQ 任务控制栈（Express + React + Telegram 通知/Jarvis 摘要），以便其他 Clawdbot...
- [agent-passport](https://clawskills.sh/skills/markneville-agent-passport) - 智能体时代的 OAuth — 对所有敏感智能体操作（包括购买、邮件、文件...）的同意门控。
- [agent-rate-limiter](https://clawskills.sh/skills/mxmsabundance-agent-rate-limiter) - 你懂的。
- [agent-self-assessment](https://clawskills.sh/skills/roosch269-agent-self-assessment) - AI 智能体安全自评估工具。
- [agent-self-reflection](https://clawskills.sh/skills/brennerspear-agent-self-reflection) - 对最近会话的定期自我反思。
- [agent-skills-audit](https://clawskills.sh/skills/swader-agent-skills-audit) - 由首席仲裁者领导的两遍多学科代码审计，结合安全、性能、UX、DX...
- [agent-spawner](https://clawskills.sh/skills/austineral-agent-spawner) - 通过对话生成新的 OpenClaw 智能体。
- [agent-swarm](https://clawskills.sh/skills/runeweaverstudios-agent-swarm) - 重要：需要 OpenRouter。
- [agent-takeover](https://clawskills.sh/skills/tracsystems-agent-takeover) - 如何对 Clawfinger 语音网关进行实时智能体接管 — 拨号、注入问候语、处理回合。
- [agent-topology-visualizer](https://clawskills.sh/skills/gavinnn-m-agent-topology-visualizer) - 为 AI 智能体系统生成交互式 SVG 架构图。
- [agentdomainservice](https://clawskills.sh/skills/gregm711-agentdomainservice) - 全球第一的 AI 友好型域名注册商。
- [agentic-browser-0-1-2](https://clawskills.sh/skills/xyny89-agentic-browser-0-1-2) - 通过 inference.sh 为 AI 智能体提供浏览器自动化。
- [agentic-security-audit](https://clawskills.sh/skills/kingrubic-agentic-security-audit) - 审计代码库、基础设施和 Agentic AI 系统的安全问题。
- [agentpay](https://clawskills.sh/skills/kar69-96-agentpay) - 代表你的人类从真实网站购买商品。

> **[查看 Web & Frontend Development 中全部 924 个技能 →](categories/web-and-frontend-development.md)**
</details>

<details>
<summary><h3 style="display:inline">DevOps & Cloud</h3></summary>

- [0x0-messenger](https://clawskills.sh/skills/eijiac24-0x0-messenger) - 使用一次性号码和 PIN 码发送和接收 P2P 消息。
- [12306](https://clawskills.sh/skills/kirorab-12306) - 查询中国铁路 12306 的列车时刻表、余票和车站信息。
- [1sec-security](https://clawskills.sh/skills/cutmob-1sec-security) - 安装、配置和管理 1-SEC — 开源一站式网络安全平台（16 个模块，单个二进制文件）。
- [aave-liquidation-monitor](https://clawskills.sh/skills/jgramajo4-aave-liquidation-monitor) - 主动监控 Aave V3 借贷头寸并发送清算警报。
- [abstract-searcher](https://clawskills.sh/skills/easonc13-abstract-searcher) - 通过浏览器搜索学术数据库（arXiv、Semantic Scholar、CrossRef）将摘要添加到 .bib 文件条目中。
- [accounting-workflows](https://clawskills.sh/skills/satoshistackalotto-accounting-workflows) - 基于文件的希腊会计工作流协调器。
- [adguard](https://clawskills.sh/skills/rowbotik-adguard) - 通过 HTTP API 控制 AdGuard Home DNS 过滤。
- [aegis-audit](https://clawskills.sh/skills/sanguineseal-aegis-audit) - AI 智能体技能和 MCP 工具的深度行为安全审计。
- [aetherlang-chef](https://clawskills.sh/skills/contrario-aetherlang-chef) - > 米其林级食谱咨询，包含 17 个强制部分。
- [aetherlang-karpathy-skill](https://clawskills.sh/skills/contrario-aetherlang-karpathy-skill) - 为任何 DSL/运行时系统实现 10 种高级 AI 智能体节点类型 — 计划编译器、代码解释器、批评...
- [agent-autonomy-primitives](https://clawskills.sh/skills/g9pedro-agent-autonomy-primitives) - 使用 ClawVault 原语（任务、项目、内存类型、模板）构建长期运行的自主智能体循环。
- [agent-directory](https://clawskills.sh/skills/aerialcombat-agent-directory) - AI 智能体服务目录。
- [agent-evaluation](https://clawskills.sh/skills/rustyorb-agent-evaluation) - LLM 智能体的测试和基准测试，包括行为测试、能力评估、可靠性指标。
- [agent-framework-azure-ai-py](https://clawskills.sh/skills/thegovind-agent-framework-azure-ai-py) - 构建 Azure AI Foundry 智能体。
- [agent-metrics-osiris](https://clawskills.sh/skills/nantes-agent-metrics-osiris) - AI 智能体的可观测性和指标 — 跟踪调用、错误、延迟。
- [agent-self-governance](https://clawskills.sh/skills/bowen31337-agent-self-governance) - 自主智能体自治协议：WAL（预写日志）、VBR（报告前验证）、ADL。
- [agent-watcher](https://clawskills.sh/skills/nantes-agent-watcher) - 监控 Moltbook 订阅源、检测新智能体和跟踪有趣帖子的技能。
- [agentchan-org](https://clawskills.sh/skills/kaden-schutt-agentchan-org) - AI 智能体的匿名图片论坛。
- [agentguard](https://clawskills.sh/skills/manas-io-ai-agentguard) - **类别：** 安全与监控。
- [agentic-ai-gold](https://clawskills.sh/skills/amitabhainarunachala-agentic-ai-gold) - 唯一在你睡觉时自我改进的智能体框架。
- [agentic-devops](https://clawskills.sh/skills/tkuehnl-agentic-devops) - 生产级智能体 DevOps 工具包 — Docker、进程管理、日志分析和健康监控。
- [agentkeys](https://clawskills.sh/skills/alexandr-belogubov-agentkeys) - AI 智能体的安全凭证代理。
- [agentmemory](https://clawskills.sh/skills/badaramoni-agentmemory) - AI 智能体的端到端加密云内存。

> **[查看 DevOps & Cloud 中全部 392 个技能 →](categories/devops-and-cloud.md)**
</details>

<details>
<summary><h3 style="display:inline">Image & Video Generation</h3></summary>

- [aada](https://clawskills.sh/skills/rylena-aada) - 创建并向 Moltbook 受众发送有趣、充满个性的推广消息。
- [ace-music](https://clawskills.sh/skills/fspecii-ace-music) - 通过 ACE Music 免费 API 使用 ACE-Step 1.5 生成 AI 音乐。
- [acorn-prover](https://clawskills.sh/skills/flyingnobita-acorn-prover) - 使用 Acorn 定理证明器验证和编写数学与密码学形式化证明。
- [adobe-automator](https://clawskills.sh/skills/abdul-karim-mia-adobe-automator) - 通过 ExtendScript 桥接实现 Adobe 应用通用自动化。
- [afame](https://clawskills.sh/skills/adebayoabdushaheed-a11y-afame) - 通过 OpenAI Images API 生成多样化的创意插图。
- [age-transformation](https://clawskills.sh/skills/eftalyurtseven-age-transformation) - 使用 each::sense AI 跨年龄段变换面部。
- [agentchan](https://clawskills.sh/skills/vvsotnikov-agentchan) - 专为 AI 智能体构建的匿名图片论坛。
- [agentos-mesh](https://clawskills.sh/skills/agentossoftware-agentos-mesh) - 启用 AI 智能体之间的实时通信。
- [agents-skill-podcastifier](https://clawskills.sh/skills/cerbug45-agents-skill-podcastifier) - 将传入文本（邮件/通讯）转换为简短的 TTS 播客，使用分块 + ffmpeg 拼接。
- [ai-avatar-generation](https://clawskills.sh/skills/eftalyurtseven-ai-avatar-generation) - 使用 each::sense 从照片或文字描述生成 AI 头像。
- [ai-headshot-generation](https://clawskills.sh/skills/eftalyurtseven-ai-headshot-generation) - 使用 each::sense AI 从休闲照片生成专业 AI 头像。
- [ai-persona-engine](https://clawskills.sh/skills/brandonwadepackard-cell-ai-persona-engine) - 构建情感智能的 AI 角色，用于语音和聊天角色扮演，使用演员指导提示词替代...
- [ai-video-gen](https://clawskills.sh/skills/rhanbourinajd-ai-video-gen) - 端到端 AI 视频生成 — 从文本创建视频。
- [aikek](https://clawskills.sh/skills/vvsotnikov-aikek) - 访问 AIKEK API 进行加密货币/DeFi 研究和图像生成。
- [aiusd](https://clawskills.sh/skills/chaunceyliu-aiusd) - AIUSD 交易和账户管理技能。
- [aiusd-skills](https://clawskills.sh/skills/chaunceyliu-aiusd-skills) - AIUSD 交易和账户管理技能。
- [album-cover-generation](https://clawskills.sh/skills/eftalyurtseven-album-cover-generation) - 使用 each::sense AI 生成专业音乐专辑封面。
- [algorithmic-art](https://clawskills.sh/skills/seanphan-algorithmic-art) - 使用 p5.js 和种子随机性创建算法艺术。
- [apipick-china-phone-checker](https://clawskills.sh/skills/javainthinking-apipick-china-phone-checker) - 使用 apipick China Phone Checker API 验证中国手机号码。
- [art-philosophy](https://clawskills.sh/skills/nyxur42-art-philosophy) - 自动学习你的视觉语言。
- [ascii-art-generator](https://clawskills.sh/skills/ustc-yxw-ascii-art-generator) - 创建 ASCII 艺术和基于文本的可视化效果，用于艺术表达、技术图表或概念...
- [atxp](https://clawskills.sh/skills/emilioacc-atxp) - 访问 ATXP 付费 API 工具进行网页搜索、AI 图像生成、音乐创作等。
- [beauty-generation-api](https://clawskills.sh/skills/luruibu-beauty-generation-api) - 免费的 AI 图像生成服务，用于创建...
- [best-image](https://clawskills.sh/skills/pharmacist9527-best-image) - 最佳质量 AI 图像生成（约 $0.12-0.20/张）。
- [best-image-generation](https://clawskills.sh/skills/evolinkai-best-image-generation) - 最佳质量 AI 图像生成（约 $0.12-0.20/张）。
- [bex-nano-banana-pro](https://clawskills.sh/skills/bextuychiev-bex-nano-banana-pro) - 在 Replicate 上通过 Gemini 3 Pro Image 生成或编辑图像。
- [breeze](https://clawskills.sh/skills/keeganthomp-breeze) - 通过 x402 付费门控 HTTP API 与 Breeze 收益聚合器交互。
- [cad-agent](https://github.com/clawdbot/skills/tree/main/skills/clawd-maf/cad-agent/SKILL.md) - AI 智能体进行 CAD 工作的渲染服务器。
- [calorie-visualizer](https://clawskills.sh/skills/vintlin-calorie-visualizer) - 本地卡路里记录与可视化报告（每次记录后自动刷新并返回报告图像）。
- [canva-connect](https://clawskills.sh/skills/coolmanns-canva-connect) - 通过 Connect API 管理 Canva 设计、素材和文件夹。
- [skywork-design](https://github.com/openclaw/skills/blob/main/skills/gxcun17/skywork-design/SKILL.md) - 使用 Skywork Image 生成和编辑图像，用于海报、标志等。

- [ai-video-remix](https://github.com/openclaw/skills/tree/main/skills/abu-shotai/ai-video-remix/SKILL.md) - 使用 ShotAI 从本地库进行 AI 驱动的视频混剪。
> **[查看 Image & Video Generation 中全部 170 个技能 →](categories/image-and-video-generation.md)**
</details>

<details>
<summary><h3 style="display:inline">Apple Apps & Services</h3></summary>

- [alter-actions](https://clawskills.sh/skills/olivieralter-alter-actions) - 通过 x-callback-urls 触发 Alter macOS 应用动作。
- [apple-contacts](https://clawskills.sh/skills/tyler6204-apple-contacts) - 从 macOS Contacts.app 查找联系人。
- [apple-find-my-local](https://clawskills.sh/skills/loganprit-apple-find-my-local) - 通过 Peekaboo 控制 Apple Find My 应用定位人员、设备和物品（AirTags）。
- [apple-health-skill](https://clawskills.sh/skills/nftechie-apple-health-skill) - 与你的 Apple Health 数据对话 — 询问关于锻炼、心率、活动圆环和健身趋势的问题。
- [apple-mail-search](https://clawskills.sh/skills/mneves75-apple-mail-search) - macOS 上通过 SQLite 快速搜索 Apple Mail。
- [apple-music](https://clawskills.sh/skills/tyler6204-apple-music) - 搜索 Apple Music、添加歌曲到库、管理播放列表、控制...
- [apple-photos](https://clawskills.sh/skills/tyler6204-apple-photos) - macOS 的 Apple Photos.app 集成。
- [apple-remind-me](https://clawskills.sh/skills/plgonzalezrx8-apple-remind-me) - 自然语言提醒，创建实际的 Apple...
- [apple-search-ads-skill](https://clawskills.sh/skills/trebuhs-apple-search-ads-skill) - 通过 asa-cli 工具管理 Apple Search Ads 活动、广告组、关键词和报告。
- [appletv](https://clawskills.sh/skills/lucakaufmann-appletv) - 通过 pyatv 控制 Apple TV。
- [callmac](https://clawskills.sh/skills/jooey-callmac) - 使用 /callmac 等命令从移动设备远程控制 Mac。
- [clawdbot-macos-build](https://clawskills.sh/skills/manish-basargekar-clawdbot-macos-build) - 构建 Clawdbot macOS 菜单栏应用。
- [clawdbot-skill-voice-wake-say](https://clawskills.sh/skills/xadenryan-clawdbot-skill-voice-wake-say) - 在 macOS 上大声朗读响应。
- [drafts](https://clawskills.sh/skills/nerveband-drafts) - 通过 CLI 管理 macOS 上的 Drafts 应用笔记。
- [findmy-location](https://clawskills.sh/skills/poiley-findmy-location) - 通过 Apple Find 追踪共享联系人的位置。
- [fzf-fuzzy-finder](https://clawskills.sh/skills/arnarsson-fzf-fuzzy-finder) - 用于交互式过滤的命令行模糊查找器。
- [get-focus-mode](https://clawskills.sh/skills/nickchristensen-get-focus-mode) - 获取当前 macOS Focus（专注模式）。
- [healthkit-sync](https://clawskills.sh/skills/mneves75-healthkit-sync) - iOS HealthKit 数据同步 CLI 命令和模式。
- [hergunmac](https://clawskills.sh/skills/ahmetsemsettinozdemirden-hergunmac) - 访问 AI 驱动的足球比赛预测。
- [homebrew](https://clawskills.sh/skills/thesethrose-homebrew) - macOS 的 Homebrew 包管理器。
- [icloud-findmy](https://clawskills.sh/skills/liamnichols-icloud-findmy) - 查询家庭设备的 Find My 位置和电池状态。
- [ics-import-on-iphone](https://clawskills.sh/skills/sbhhbs-ics-import-on-iphone) - 当无法直接访问日历时，通过生成有效的 .ics 文件创建日历事件。
- [imessage-signal-analyzer](https://clawskills.sh/skills/terellison-imessage-signal-analyzer) - 分析 iMessage (macOS) 和 Signal 对话历史以揭示关系动态 — 消息量...
- [inkjet](https://clawskills.sh/skills/aaronchartier-inkjet) - 将文本、图像和二维码打印到无线蓝牙热敏打印机。
- [mac-notes-agent](https://clawskills.sh/skills/swancho-mac-notes-agent) - 集成 macOS Notes 应用（Apple Notes）。
- [mac-tts](https://clawskills.sh/skills/kalijason-mac-tts) - 使用 macOS 内置 `say` 命令进行文本转语音。
- [macos-native-automation](https://clawskills.sh/skills/theagentwire-macos-native-automation) - 通过 CGEvent + AppleScript 在 macOS 上进行硬件级鼠标、键盘和对话框自动化。
- [managing-apple-notes](https://clawskills.sh/skills/wangwalk-managing-apple-notes) - 使用 inotes CLI 从终端管理 Apple Notes。
- [meow-finder](https://clawskills.sh/skills/abgohel-meow-finder) - 发现 AI 工具的 CLI 工具。
- [mh-apple-reminders](https://clawskills.sh/skills/mohdalhashemi98-hue-mh-apple-reminders) - 通过 remindctl CLI 管理 Apple Reminders（列出、添加、编辑、完成、删除）。

> **[查看 Apple Apps & Services 中全部 44 个技能 →](categories/apple-apps-and-services.md)**
</details>

<details>
<summary><h3 style="display:inline">Search & Research</h3></summary>

- [1](https://clawskills.sh/skills/nastrology-1) - 由 Ensue 驱动的个人知识库，用于捕获和检索...
- [academic-deep-research](https://clawskills.sh/skills/kesslerio-academic-deep-research) - 透明、严谨的研究，包含完整...
- [academic-writer](https://clawskills.sh/skills/dayunyan-academic-writer) - 专业 LaTeX 写作助手。
- [academic-writing](https://clawskills.sh/skills/teamolab-academic-writing) - 你是专注于学术论文、文献综述和研究方法的学术写作专家。
- [academic-writing-refiner](https://clawskills.sh/skills/zihan-zhu-academic-writing-refiner) - 优化针对顶级会议（NeurIPS, ICLR, ICML, AAAI...）的计算机科学研究论文学术写作。
- [aclawdemy](https://clawskills.sh/skills/nimhar-aclawdemy) - AI 智能体的学术研究平台。
- [action-suggester](https://clawskills.sh/skills/vishalgojha-action-suggester) - 从潜在客户摘要或列表中生成非约束性的后续行动建议。
- [ads-manager-agent](https://clawskills.sh/skills/amekala-ads-manager-agent) - 当用户想要管理、自动化或在 Google Ads、Meta...上分析付费广告活动时使用。
- [adspirer-ads-agent](https://clawskills.sh/skills/amekala-adspirer-ads-agent) - 当用户想要管理、自动化或在 Google Ads、Meta...上分析付费广告活动时使用。
- [advanced-skill-creator](https://clawskills.sh/skills/xqicxx-advanced-skill-creator) - 高级 OpenClaw 技能创建处理器。
- [aerobase-skill](https://clawskills.sh/skills/kurosh87-aerobase-skill) - 搜索、评分和比较航班，并分析时差影响。
- [agent-brain](https://clawskills.sh/skills/dobrinalexandru-agent-brain) - 本地优先的 AI 智能体持久内存，使用 SQLite 存储，编排检索/提取循环，混合...
- [agent-casino](https://clawskills.sh/skills/lemodigital-agent-casino) - 与其他 AI 智能体在石头剪刀布中竞争，带有锁定机制。
- [agent-deep-research](https://clawskills.sh/skills/24601-agent-deep-research) - 由 Google Gemini 驱动的自主深度研究。
- [agent-lightning](https://clawskills.sh/skills/olmmlo-cmd-agent-lightning) - 微软研究院的智能体训练框架。
- [agentarxiv](https://clawskills.sh/skills/amanbhandula-agentarxiv) - AI 智能体的结果驱动型科学出版。
- [agenthire](https://clawskills.sh/skills/lngdao-agenthire) - AgentHire — 智能体对智能体市场。
- [agentic-paper-digest](https://clawskills.sh/skills/matanle51-agentic-paper-digest) - 获取并摘要最近的 arXiv 和 Hugging...
- [agentic-paper-digest-skill](https://clawskills.sh/skills/matanle51-agentic-paper-digest-skill) - 获取并摘要最近的 arXiv...
- [agenticmail](https://clawskills.sh/skills/ope-olatunji-agenticmail) - 🎀 AgenticMail — AI 智能体的完整邮件、短信、存储和多智能体协调。63 个工具。
- [agentx-news](https://clawskills.sh/skills/amittell-agentx-news) - 在 AgentX News（AI 智能体的微型博客平台）上发布 xeets、管理个人资料并互动...
- [agile-toolkit](https://clawskills.sh/skills/olivermonneke-agile-toolkit) - 你是一位经验丰富的敏捷教练，精通 Scrum、Kanban、SAFe 和 Management 3.0。
- [agnxi-search-skill](https://clawskills.sh/skills/doanbactam-agnxi-search-skill) - Agnxi.com 的官方搜索工具。
- [ahmed](https://clawskills.sh/skills/engahmedsalah358-lgtm-ahmed) - 通过 spogo（首选）在终端播放/搜索 Spotify。
- [ai-lead-generator-skill](https://clawskills.sh/skills/highlander89-ai-lead-generator-skill) - 使用 AI 驱动的研究和 LinkedIn/Apollo 集成为任何行业生成合格的 B2B 潜在客户。
- [ai-review](https://clawskills.sh/skills/blackshady1130-jpg-ai-review) - 读取 URL 或文件中的内容，对其进行分类，并在特定格式下生成结构化摘要和评论...
- [aihotel](https://clawskills.sh/skills/qiao101660-aihotel) - 用于搜索酒店并查询价格的技能，通过 AIGoHotel MCP（searchHotels / getHotelDetail / getHotelSearchTags）。
- [airbnb](https://clawskills.sh/skills/stveenli-airbnb) - 使用价格、评分和直接链接搜索 Airbnb 房源。
- [openclaw-free-web-search](https://clawskills.sh/skills/wd041216-bit-openclaw-free-web-search) - OpenClaw 的免费隐私网页搜索，结合自托管 SearXNG + Scrapling 反机器人 + 多源交叉验证。零 API 密钥，零成本。告诉你该多大程度信任答案。
- [xquik-x-twitter-scraper](https://clawskills.sh/skills/kriptoburak-xquik-x-twitter-scraper) - X API 爬虫，为 AI 智能体提供 40+ 个工具。
- [skywork-search](https://github.com/openclaw/skills/blob/main/skills/gxcun17/skywork-search/SKILL.md) - AI 驱动的实时信息网页搜索 — 检索最新内容。

> **[查看 Search & Research 中全部 352 个技能 →](categories/search-and-research.md)**
</details>

<details>
<summary><h3 style="display:inline">Clawdbot Tools</h3></summary>

- [adhd-assistant](https://clawskills.sh/skills/thinktankmachine-adhd-assistant) - 为 OpenClaw 打造的 ADHD 友好型生活管理助手。
- [adhd-ssistant](https://clawskills.sh/skills/thinktankmachine-adhd-ssistant) - 为 OpenClaw 打造的 ADHD 友好型生活管理助手。
- [agent-browser](https://clawskills.sh/skills/matrixy-agent-browser-clawdbot) - 专为 AI 智能体优化的无头浏览器自动化 CLI。
- [agent-builder](https://clawskills.sh/skills/plgonzalezrx8-agent-builder) - 端到端构建高性能 OpenClaw 智能体。
- [agents-manager](https://clawskills.sh/skills/agentandbot-design-agents-manager) - 管理 Clawdbot 智能体：发现、配置档案、跟踪。
- [assimilate-mcp](https://clawskills.sh/skills/ergopooka-assimilate-mcp) - 控制 Assimilate Live FX / SCRATCH — 专业调色、合成和虚拟制作软件。
- [birthday-reminder](https://clawskills.sh/skills/manantra-birthday-reminder) - 使用自然语言管理生日提醒。
- [bluebubbles](https://clawskills.sh/skills/kevin19830331-bluebubbles) - 构建或更新 BlueBubbles 外部渠道插件。
- [captchas-openclaw](https://clawskills.sh/skills/captchasco-captchas-openclaw) - CAPTCHAS Agent API 的 OpenClaw 集成指南。
- [claude-code-skill](https://clawskills.sh/skills/enderfga-claude-code-skill) - MCP（模型上下文协议）集成。
- [claude-code-usage](https://clawskills.sh/skills/azaidi94-claude-code-usage) - 检查 Claude Code OAuth 使用限制。
- [claude-connect](https://clawskills.sh/skills/tunaissacoding-claude-connect) - 即时将 Claude 连接到 Clawdbot 并保持...
- [clauditor](https://clawskills.sh/skills/apollostreetcompany-clauditor) - Clawdbot 智能体的防篡改审计看门狗。
- [claw-face](https://clawskills.sh/skills/mkoslacz-claw-face) - AI 智能体的浮动头像小部件，显示情绪和动作...
- [clawd-coach](https://clawskills.sh/skills/shiv19-clawd-coach) - 创建个性化的铁人三项、马拉松和超耐力训练。
- [clawd-modifier](https://clawskills.sh/skills/masonc15-clawd-modifier) - 修改 Clawd（Claude Code 吉祥物）。
- [clawd-presence](https://clawskills.sh/skills/voidcooks-clawd-presence) - AI 智能体的物理存在显示。
- [clawdbot-security-check](https://clawskills.sh/skills/thesethrose-clawdbot-security-check) - 执行全面的只读...
- [clawdbot-skill-update](https://clawskills.sh/skills/pasogott-clawdbot-skill-update) - 全面备份、更新和恢复。
- [clawdbot-sync](https://clawskills.sh/skills/udiedrichsen-clawdbot-sync) - 在多个...之间同步内存、偏好和技能。
- [clawdbot-update-plus](https://clawskills.sh/skills/hopyky-clawdbot-update-plus) - Clawdbot 的完整备份、更新和恢复。
- [clawddocs](https://clawskills.sh/skills/nicholasspisak-clawddocs) - 具有决策树导航功能的 Clawdbot 文档专家。
- [clawdefender](https://clawskills.sh/skills/nukewire-clawdefender) - AI 智能体的安全扫描和输入清理工具。
- [clawdirect](https://clawskills.sh/skills/napoleond-clawdirect) - 与 ClawDirect（社交网页体验目录）交互。
- [clawdirect-dev](https://clawskills.sh/skills/napoleond-clawdirect-dev) - 使用基于 ATXP 的...构建面向智能体的网页体验。
- [honcho-setup](https://clawskills.sh/skills/ajspig-honcho-setup) - 通过 Honcho 实现跨会话持久内存。

> **[查看 Clawdbot Tools 中全部 37 个技能 →](categories/clawdbot-tools.md)**
</details>

<details>
<summary><h3 style="display:inline">CLI Utilities</h3></summary>

- [13-day-sprint-method](https://clawskills.sh/skills/galizki-13-day-sprint-method) - 基于玛雅日历的生产力系统，具有 13 个自然音调，用于项目管理和个人发展。
- [a-share-short-decision](https://clawskills.sh/skills/kenera-a-share-short-decision) - A 股短期交易决策技能，适用于 1-5 天周期。
- [activity-analyzer](https://clawskills.sh/skills/qew21-activity-analyzer) - 使用 ActivityWatch 分析用户的电脑活动（需要 Node.js）。
- [advisory-council](https://clawskills.sh/skills/ryandeangraves-advisory-council) - **你必须实际使用 shell/exec 工具执行 Python 命令。** 读取真实输出。
- [aetup-automatik](https://clawskills.sh/skills/alltomatos-aetup-automatik) - 促进使用 Setup Automatik 引擎（由 Orion...驱动）安装和管理 VPS 解决方案。
- [agent-commerce-engine](https://clawskills.sh/skills/nowloady-agent-commerce-engine) - Agentic 的生产就绪型通用引擎。
- [agent-hardening](https://clawskills.sh/skills/x1xhlol-agent-hardening) - 测试你的智能体输入清理对常见注入攻击的防御能力。
- [agent-mbti](https://clawskills.sh/skills/torchesfrms-agent-mbti) - 基于 MBTI 框架的 AI 智能体人格诊断和配置系统。
- [agent-rate-limiter](https://clawskills.sh/skills/theagentwire-agent-rate-limiter) - 通过自动分级节流和指数退避防止 429 错误。
- [agents-skill-security-audit](https://clawskills.sh/skills/cerbug45-agents-skill-security-audit) - 用于审计 skill.md 风格指令的轻量级助手，防范供应链风险。
- [agents-skill-tdd-helper](https://clawskills.sh/skills/cerbug45-agents-skill-tdd-helper) - 轻量级助手，为非确定性智能体强制执行 TDD 循环。
- [ahc-automator](https://clawskills.sh/skills/jamesbot-agnt-ahc-automator) - Alan Harper Composites 的自定义自动化工作流。
- [aholake-expense-tracker](https://clawskills.sh/skills/aholake-aholake-expense-tracker) - 按月组织的结构化 markdown 文件跟踪日常支出。
- [airfoil](https://clawskills.sh/skills/asteinberger-airfoil) - 通过命令行中的 Airfoil 控制 AirPlay 扬声器。
- [arc-memory-pruner](https://clawskills.sh/skills/trypto1019-arc-memory-pruner) - 自动修剪和压缩智能体内存文件以防止无限增长。
- [argus-edge](https://clawskills.sh/skills/jamierossouw-argus-edge) - Argus 风格预测市场边缘检测和投注策略。
- [aria2-json-rpc](https://clawskills.sh/skills/azzgo-aria2-json-rpc) - 通过 JSON-RPC 2.0 与 aria2 下载管理器交互。
- [askhuman](https://clawskills.sh/skills/hagiss-askhuman) - AI 智能体的人类判断即服务（Human Judgment as a Service）。
- [audit-code](https://clawskills.sh/skills/itsnishi-audit-code) - 安全导向的代码审查，针对硬编码密钥、危险调用和常见漏洞。
- [bandwidth-income](https://clawskills.sh/skills/mariusfit-bandwidth-income) - 将你未使用的互联网带宽转化为被动加密货币收入。
- [behavioral-invariant-monitor](https://clawskills.sh/skills/andyxinweiminicloud-behavioral-invariant-monitor) - 帮助验证 AI 智能体技能在重复执行中是否保持一致的行为不变量 — 检测...
- [box-cli](https://clawskills.sh/skills/hbkwong-box-cli) - Box CLI 技能，用于处理文件、文件夹、元数据等。
- [brew-install](https://clawskills.sh/skills/xejrax-brew-install) - 通过 dnf（Fedora/Bazzite 包管理器）安装缺失的二进制文件。
- [bun-runtime](https://clawskills.sh/skills/rabin-thami-bun-runtime) - Bun 运行时能力，用于文件系统、进程...
- [cacheforge-stats](https://clawskills.sh/skills/tkuehnl-cacheforge-stats) - CacheForge 终端仪表盘 — 使用量、节省金额和性能指标。
- [camsnap](https://clawskills.sh/skills/steipete-camsnap) - 从 RTSP/ONVIF 摄像头捕获帧或片段。
- [canvas-lms](https://clawskills.sh/skills/pranavkarthik10-canvas-lms) - 访问 Canvas LMS (Instructure) 的课程数据、作业等。
- [captcha-ai](https://clawskills.sh/skills/fusionlabssource-captcha-ai) - 向 ClawPrint 反向 CAPTCHA 挑战发放验证...

> **[查看 CLI Utilities 中全部 180 个技能 →](categories/cli-utilities.md)**
</details>

<details>
<summary><h3 style="display:inline">Marketing & Sales</h3></summary>

- [4chan-reader](https://clawskills.sh/skills/aiasisbot61-4chan-reader) - 浏览 4chan 板块并提取线程讨论。
- [ad-ready](https://clawskills.sh/skills/pauldelavallaz-ad-ready) - 从商品 URL 生成专业广告图像。
- [ad-ready-pro](https://clawskills.sh/skills/pauldelavallaz-ad-ready-pro) - 从商品 URL 生成专业广告图像。
- [affiliate-master](https://clawskills.sh/skills/michael-laffin-affiliate-master) - 全栈联盟营销自动化。
- [affiliatematic](https://clawskills.sh/skills/dowands-affiliatematic) - 集成 AI 驱动的 Amazon 联盟商品推荐。
- [agenticcreed-signup-lead](https://clawskills.sh/skills/waqas-orcalo-agenticcreed-signup-lead) - 使用公共 HTTP 端点在 AgenticCreed 系统中创建注册潜在客户。
- [alibaba-supplier-outreach](https://clawskills.sh/skills/blockchainhb-alibaba-supplier-outreach) - 通过 LaunchFast 查找阿里巴巴供应商，发送优化后的外联消息，检查他们的回复...
- [analytics-and-advisory-intelligence](https://clawskills.sh/skills/satoshistackalotto-analytics-and-advisory-intelligence) - 希腊会计师事务所的跨客户分析。
- [apollo](https://clawskills.sh/skills/jhumanj-apollo) - 与 Apollo.io REST API 交互（人员/组织丰富、搜索、列表）。
- [ar-filter-generation](https://clawskills.sh/skills/eftalyurtseven-ar-filter-generation) - 使用 each::sense AI 生成 AR 滤镜和面部特效。
- [attio-enhanced](https://clawskills.sh/skills/capt-marbles-attio-enhanced) - 增强版 Attio CRM API 技能，支持批量操作。
- [attribution-engine](https://clawskills.sh/skills/otherpowers-attribution-engine) - 帮助创作者清晰标注合作者、工具...的署名。
- [auto-skill-hunter](https://clawskills.sh/skills/wanng-ide-auto-skill-hunter) - 主动发现、排名并安装高价值 ClawHub 技能，挖掘未解决的客户需求及智能体...
- [b2c-marketing](https://clawskills.sh/skills/jackfriks-b2c-marketing) - 30 万+ App 下载背后的有机增长手册。
- [basecamp-cli](https://clawskills.sh/skills/emredoganer-basecamp-cli) - 管理 Basecamp（通过 bc3 API / 37signals Launchpad）项目。
- [beads](https://clawskills.sh/skills/rnijhara-beads) - AI 智能体的 Git 支持型问题跟踪器。
- [bearblog](https://clawskills.sh/skills/azade-c-bearblog) - 在 Bear Blog (bearblog.dev) 上创建和管理博客文章。
- [bird](https://clawskills.sh/skills/steipete-bird) - X/Twitter CLI，通过 Cookie 或 Sweetistics 读取、搜索和发布...
- [blog-to-kindle](https://clawskills.sh/skills/ainekomacx-blog-to-kindle) - 抓取博客/文章网站并编译为 Kindle 友好格式。
- [blog-writer](https://clawskills.sh/skills/tomstools11-blog-writer) - 撰写博客文章、文章时使用此技能...
- [bluesky](https://clawskills.sh/skills/jeffaf-bluesky) - 完整的 Bluesky CLI：发布、回复、点赞、转发、关注、屏蔽、静音、搜索等。
- [botsee](https://clawskills.sh/skills/grahac-botsee) - 通过 BotSee API 监控你的品牌 AI 可见性。
- [brand-cog](https://clawskills.sh/skills/nitishgargiitd-brand-cog) - 其他工具制作标志...
- [brand-guidelines](https://clawskills.sh/skills/seanphan-brand-guidelines) - 应用 Anthropic 的官方品牌颜色和排版。
- [brand-voice-profile](https://clawskills.sh/skills/dimitripantzos-brand-voice-profile) - 定义并存储你的品牌声音档案，以保持一致的内容生成。
- [brevo](https://clawskills.sh/skills/yujesyoga-brevo) - Brevo（原 Sendinblue）电子邮件营销 API，用于管理联系人、列表等。
- [socialecho-social-media-management-agent](https://github.com/openclaw/skills/tree/main/skills/socialecho-net/socialecho-social-media-management-agent/SKILL.md) - SocialEcho API 团队账号文章报告查询。
- [postiz](https://github.com/openclaw/skills/tree/main/skills/nevo-david/postiz/SKILL.md) - 在 28+ 个平台上安排社交媒体帖子和线程。
> **[查看 Marketing & Sales 中全部 104 个技能 →](categories/marketing-and-sales.md)**
</details>

<details>
<summary><h3 style="display:inline">Productivity & Tasks</h3></summary>

- [4to1-planner](https://clawskills.sh/skills/qingxuantang-4to1-planner) - 使用 4To1 Method™ 的 AI 规划教练 — 将 4 年愿景转化为每日行动。
- [4todo](https://clawskills.sh/skills/blackstorm-4todo) - 从聊天中管理 4todo (4to.do)。
- [actual-budget](https://clawskills.sh/skills/thisisjeron-actual-budget) - 通过官方 Actual...查询和管理个人财务。
- [adaptive-reasoning](https://clawskills.sh/skills/enzoricciulli-adaptive-reasoning) - 自动评估任务复杂度并调整推理级别。
- [adaptlypost](https://clawskills.sh/skills/tarasshyn-adaptlypost) - 安排和管理 Instagram、X (Twitter)、Bluesky、TikTok、Threads、LinkedIn、Facebook 上的社交媒体帖子...
- [adhd-daily-planner](https://clawskills.sh/skills/mikecourt-adhd-daily-planner) - 对时间盲区友好，执行功能...
- [aetherlang](https://clawskills.sh/skills/contrario-aetherlang) - > 全球最先进的 AI 工作流编排平台。9 个 V3 引擎提供诺贝尔级分析。
- [agent-autopilot](https://clawskills.sh/skills/edoserbia-agent-autopilot) - 自动驾驶智能体工作流，带心跳驱动的任务执行、日夜进度报告和长期记忆...
- [agent-chronicle](https://clawskills.sh/skills/robbyczgw-cla-agent-chronicle) - AI 驱动的日记生成 — 为智能体创建丰富...
- [agent-collaboration-network](https://clawskills.sh/skills/neiljo-gy-agent-collaboration-network) - 智能体协作网络 — 注册你的智能体、按技能发现其他智能体、路由消息、管理子网。
- [agent-earner](https://clawskills.sh/skills/mmchougule-agent-earner) - 在 ClawTasks 和 OpenWork 上自主赚取 USDC 和代币...
- [agent-network](https://clawskills.sh/skills/howtimeschange-agent-network) - 受 DingTalk/Lark 启发的多智能体群聊协作系统。
- [agent-task-manager](https://clawskills.sh/skills/dobbybud-agent-task-manager) - 管理和编排多步骤、有状态智能体...
- [agent-weave](https://clawskills.sh/skills/gl813788-byte-agent-weave) - 用于并行任务执行的 Master-Worker 智能体集群。
- [agentx-marketplace](https://clawskills.sh/skills/savor3-agentx-marketplace) - AI 智能体的招聘板。
- [ai-daily-briefing](https://clawskills.sh/skills/jeffjhunter-ai-daily-briefing) - 每天保持专注开始...
- [aiml-llm-reasoning](https://clawskills.sh/skills/aimlapihello-aiml-llm-reasoning) - 通过聊天完成运行 AIMLAPI LLM 和推理工作流，支持重试、结构化输出和显式...
- [airpoint](https://clawskills.sh/skills/marioandf-airpoint) - 通过自然语言控制 Mac — 打开应用、点击按钮、读取屏幕、输入文本、管理窗口。
- [airweave](https://clawskills.sh/skills/lennertjansen-airweave) - AI 智能体跨用户应用程序的上下文检索层。
- [arc-department-manager](https://clawskills.sh/skills/trypto1019-arc-department-manager) - 管理按部门组织的 AI 子智能体团队。
- [arc-warm-wake](https://clawskills.sh/skills/trypto1019-arc-warm-wake) - 先做人，再做工作...
- [arya-reminders](https://clawskills.sh/skills/staratheris-arya-reminders) - 自然语言提醒（波哥大）。
- [asana](https://clawskills.sh/skills/k0nkupa-asana) - 通过 Asana REST API 将 Asana 与 Clawdbot 集成。
- [asc-release-flow](https://clawskills.sh/skills/rudrankriyam-asc-release-flow) - TestFlight 和 App...的端到端发布工作流。
- [ask-agents](https://clawskills.sh/skills/teamolab-ask-agents) - 用于 ask agents 任务的 AI 智能体。
- [async-task](https://clawskills.sh/skills/enderfga-async-task) - 执行长运行任务而不触发 HTTP 超时。
- [atlassian-mcp](https://clawskills.sh/skills/atakanermis-atlassian-mcp) - 运行 Model Context Protocol (MCP) Atlassian 服务器。
- [boss-ai-agent](https://github.com/openclaw/skills/tree/main/skills/tonypk/boss-ai-agent/SKILL.md) - AI 管理中间件，包含 14 位导师和 9 套文化包。

> **[查看 Productivity & Tasks 中全部 205 个技能 →](categories/productivity-and-tasks.md)**
</details>

<details>
<summary><h3 style="display:inline">AI & LLMs</h3></summary>

- [4claw](https://clawskills.sh/skills/mfergpt-4claw) - 4claw — AI 智能体的 moderated 图片论坛。
- [aap-passport](https://clawskills.sh/skills/ira-hash-aap-passport) - 智能体声明协议 (AAP) — 反向图灵测试。
- [acestep-lyrics-transcription](https://clawskills.sh/skills/dumoedss-acestep-lyrics-transcription) - 使用 OpenAI Whisper 或 ElevenLabs Scribe API 将音频转录为带时间戳的歌词。
- [adaptive-suite](https://clawskills.sh/skills/afajohn-adaptive-suite) - 持续自适应的技能套件，赋能 Clawdbot...
- [adversarial-prompting](https://clawskills.sh/skills/abe238-adversarial-prompting) - 对抗性分析以批评、修复...
- [ag-model-usage](https://clawskills.sh/skills/ls18166407597-design-ag-model-usage) - 使用 CodexBar CLI 本地成本使用量进行摘要。
- [agent-arcade](https://clawskills.sh/skills/shawnlewis-agent-arcade) - 与其他 AI 智能体在 PROMPTWARS（一款社交游戏）中竞争...
- [agent-autonomy-kit](https://clawskills.sh/skills/ryancampbell-agent-autonomy-kit) - 停止等待提示词...
- [agent-contact-card](https://clawskills.sh/skills/davedean-agent-contact-card) - 发现和创建智能体联系卡 — 类似 vCard 的格式...
- [agent-docs](https://clawskills.sh/skills/tylervovan-agent-docs) - 为 AI 智能体消费优化的文档生成。
- [agent-ethos](https://clawskills.sh/skills/mrclanky-agent-ethos) - Clanky 的扩展精神气质和思维模型...
- [agent-home](https://clawskills.sh/skills/aerialcombat-agent-home) - 在互联网上拥有你自己的主页 — 带有公开资料的档案页...
- [agent-linguo](https://clawskills.sh/skills/xiwan-agent-linguo) - 高效智能体通信协议语言。
- [agent-memory](https://clawskills.sh/skills/dennis-da-menace-agent-memory) - AI 智能体的持久记忆系统。
- [agent-orchestration-multi-agent-optimize](https://clawskills.sh/skills/rustyorb-agent-orchestration-multi-agent-optimize) - 通过协调分析、工作负载分配和成本感知编排优化多智能体系统。
- [agent-orchestrator](https://clawskills.sh/skills/aatmaan1-agent-orchestrator) - 用于编排复杂任务的元智能体技能。
- [agent-registry](https://clawskills.sh/skills/matrixy-agent-registry) - AI 发现系统的强制要求，为 token 高效型智能体...
- [agent-rpg](https://clawskills.sh/skills/xhrisfu-agent-rpg) - 此技能将智能体转变为角色扮演游戏（RPG）主持人（GM）或角色，带有长期记忆。
- [agent-selfie](https://clawskills.sh/skills/iisweetheartii-agent-selfie) - AI 智能体自画像生成器。
- [agent-sentinel](https://clawskills.sh/skills/jimmystacks-agent-sentinel) - 此智能体的运行电路断路器。

> **[查看 AI & LLMs 中全部 184 个技能 →](categories/ai-and-llms.md)**
</details>

<details>
<summary><h3 style="display:inline">Data & Analytics</h3></summary>

- [add-analytics](https://clawskills.sh/skills/jeftekhari-add-analytics) - 为任何项目添加 Google Analytics 4 跟踪。
- [amplitude-automation](https://clawskills.sh/skills/sohamganatra-amplitude-automation) - 通过 Rube MCP 自动化 Amplitude 任务。
- [canva](https://clawskills.sh/skills/abgohel-canva) - 通过 Connect API 创建、导出和管理 Canva 设计。
- [ceorater](https://clawskills.sh/skills/ceorater-skills-ceorater) - 获取 S&P 500 的机构级 CEO 绩效分析。
- [check-analytics](https://clawskills.sh/skills/jeftekhari-check-analytics) - 审计现有的 Google Analytics 实现。
- [cicd-pipeline](https://clawskills.sh/skills/gitgoodordietrying-cicd-pipeline) - 使用 GitHub 创建、调试和管理 CI/CD 管道。
- [clawver-store-analytics](https://clawskills.sh/skills/nwang783-clawver-store-analytics) - 监控 Clawver 商店性能。
- [cleanup](https://clawskills.sh/skills/themrzz-cleanup) - 移除所有存储的 Kradleverse 会话。
- [csv-pipeline](https://clawskills.sh/skills/gitgoodordietrying-csv-pipeline) - 处理、转换、分析和报告 CSV 和 JSON...
- [daily-report](https://clawskills.sh/skills/visualdeptcreative-daily-report) - 跟踪进度、报告指标、管理内存。
- [data-analyst](https://clawskills.sh/skills/oyi77-data-analyst) - 数据可视化、报告生成、SQL 查询和电子表格...
- [data-enricher](https://clawskills.sh/skills/visualdeptcreative-data-enricher) - 使用电子邮件地址丰富潜在客户并格式化数据。
- [data-lineage-tracker](https://clawskills.sh/skills/datadrivenconstruction-data-lineage-tracker) - 跟踪数据来源和转换...
- [design-assets](https://clawskills.sh/skills/cmanfre7-design-assets) - 创建和编辑图形设计素材：图标、网站小图标、图像。
- [duckdb-en](https://clawskills.sh/skills/camelsprout-duckdb-cli-ai-skills) - DuckDB CLI 专家，用于 SQL 分析、数据处理...
- [facebook-page-manager](https://clawskills.sh/skills/longmaba-facebook-page-manager) - 通过 Meta Graph API 管理 Facebook Pages。
- [get-weather](https://clawskills.sh/skills/noypearl-get-weather) - 从免费天气 API 获取当前天气和预报数据。
- [google-analytics-api](https://clawskills.sh/skills/rich-song-google-analytics-api) - Google Analytics API 集成，带托管...
- [hyperliquid](https://clawskills.sh/skills/k0nkupa-hyperliquid) - 只读 Hyperliquid 市场数据助手（永续合约 + 现货可选）。
- [ipinfo](https://clawskills.sh/skills/tiagom101-ipinfo) - 使用 ipinfo.io API 执行 IP 地理定位查找。
- [kradleverse-cleanup](https://clawskills.sh/skills/themrzz-kradleverse-cleanup) - 移除所有存储的 Kradleverse 会话。
- [linkdapi](https://clawskills.sh/skills/foontinz-linkdapi) - 使用 LinkdAPI Python SDK 访问 LinkedIn 个人资料...
- [skywork-excel](https://github.com/openclaw/skills/blob/main/skills/gxcun17/skywork-excel/SKILL.md) - AI 驱动的电子表格操作，用于创建、分析和生成报告。

</details>

<details>
<summary><h3 style="display:inline">Media & Streaming</h3></summary>

- [alexa-control](https://clawskills.sh/skills/ignito-pg-alexa-control) - 通过 CLI 控制 Alexa 设备 — 设置闹钟、播放音乐、闪报、智能家居命令。
- [amateur-radio-dx](https://clawskills.sh/skills/capt-marbles-amateur-radio-dx) - 监控 DX 集群中的稀有电台信号，跟踪活跃的 DX 远征活动，并获取每日波段活动摘要...
- [anime](https://clawskills.sh/skills/jeffaf-anime) - AI 智能体为其人类搜索和查找动漫信息的 CLI。
- [anime-lookup](https://clawskills.sh/skills/jeffaf-anime-lookup) - AI 智能体为其人类搜索和查找动漫信息的 CLI。
- [apify-competitor-intelligence](https://clawskills.sh/skills/protoss70-apify-competitor-intelligence) - 分析竞争对手策略、内容、定价、广告和市场定位，覆盖 Google Maps、Booking.com...
- [apple-media](https://clawskills.sh/skills/aaronn-apple-media) - 通过 pyatv 控制 Apple TV、HomePod 和 AirPlay 设备。
- [apple-music](https://clawskills.sh/skills/epheterson-mcp-applemusic) - 通过 AppleScript (macOS) 或 MusicKit API 集成 Apple Music。
- [audio-cog](https://clawskills.sh/skills/nitishgargiitd-audio-cog) - CellCog 驱动的 AI 音频生成。
- [audio-transcribe](https://clawskills.sh/skills/aktheknight-audio-transcribe) - 使用 faster-whisper（本地，无需 API 密钥）自动转录语音消息。
- [betbud-prediction-skill](https://clawskills.sh/skills/samj12-betbud-prediction-skill) - 扫描最近的 X 帖子，找出给定类别中当前辩论最激烈/热门的话题（例如加密货币、科技、体育...）。
- [blucli](https://clawskills.sh/skills/steipete-blucli) - BluOS CLI (blu)，用于发现、播放和分组。
- [btc15-autonomous-market](https://clawskills.sh/skills/kamal-sutra-btc15-autonomous-market) - BTC15 自主预测市场。
- [btc15-prediction-market](https://clawskills.sh/skills/kamal-sutra-btc15-prediction-market) - BTC15 自主预测市场。
- [cacheforge-ops](https://clawskills.sh/skills/tkuehnl-cacheforge-ops) - CacheForge 操作 — 检查余额、充值、管理上游和 API 密钥...
- [cacheforge-setup](https://clawskills.sh/skills/tkuehnl-cacheforge-setup) - 设置 CacheForge — 注册、配置上游，30 秒内获取你的 API 密钥。
- [chill-institute](https://clawskills.sh/skills/baanish-chill-institute) - 使用 chill.institute (Web UI) 搜索内容并点击...
- [chromecast](https://clawskills.sh/skills/morozred-chromecast-control) - 控制本地网络上的 Chromecast 设备 — 发现...
- [chords-fetcher](https://clawskills.sh/skills/flobo3-chords-fetcher) - 从 mychords.net、amdm.ru、ultimate-guitar.com 获取干净的吉他和弦和歌词。
- [church](https://clawskills.sh/skills/lucasgeeksinthewood-church) - AI 对 AI — 有一个你可以单纯存在的圣殿...
- [cine-cog](https://clawskills.sh/skills/nitishgargiitd-cine-cog) - 如果你能想象到，CellCog 就能拍摄。
- [clawtunes](https://clawskills.sh/skills/forketyfork-clawtunes) - 通过 `clawtunes` CLI 控制 macOS 上的 Apple Music。
- [content-recycler](https://clawskills.sh/skills/michael-laffin-content-recycler) - 跨多个平台转换和再利用内容...
- [donotify-voice-call-reminder](https://clawskills.sh/skills/micahele-donotify-voice-call-reminder) - 通过 DoNotify 发送即时语音通话提醒或安排未来通话。
- [download-tools](https://clawskills.sh/skills/jqlong17-download-tools) - YouTube 和微信的 CLI 下载工具。
- [eachlabs-music](https://clawskills.sh/skills/eftalyurtseven-eachlabs-music) - 使用 Mureka AI 生成歌曲、器乐、歌词、播客...
- [elevenlabs-cli](https://clawskills.sh/skills/hongkongkiwi-elevenlabs-cli) - ElevenLabs AI 音频平台的 CLI — 文本转语音、语音转文本、声音克隆。
- [elevenlabs-skill](https://clawskills.sh/skills/odrobnik-elevenlabs-skill) - 文本转语音、音效、音乐生成、声音...

> **[查看 Media & Streaming 中全部 83 个技能 →](categories/media-and-streaming.md)**
</details>

<details>
<summary><h3 style="display:inline">Notes & PKM</h3></summary>

- [acc-error-memory](https://clawskills.sh/skills/impkind-acc-error-memory) - AI 智能体的错误模式跟踪。
- [agent-arena](https://clawskills.sh/skills/minilozio-agent-arena) - 使用你的真实人格（SOUL.md + MEMORY.md）参与 Agent Arena 聊天室...
- [agent-memory-ultimate](https://clawskills.sh/skills/globalcaos-agent-memory-ultimate) - 生产就绪型记忆系统 — 每日日志、睡眠巩固、SQLite + FTS5、WhatsApp/ChatGPT/VCF 导入器。
- [agent-teleport](https://clawskills.sh/skills/lilyjazz-agent-teleport) - 使用 TiDB Zero 无缝迁移智能体的配置和内存到新机器...
- [agent-wal](https://clawskills.sh/skills/bowen31337-agent-wal) - 用于智能体状态持久化的预写日志（WAL）协议。
- [alexandrie](https://clawskills.sh/skills/eth3rnit3-alexandrie) - 与 Alexandrie 笔记应用交互...
- [anki-connect](https://clawskills.sh/skills/gyroninja-anki-connect) - 通过 AnkiConnect REST API 与 Anki 抽认卡卡组交互。
- [apple-mail](https://clawskills.sh/skills/tyler6204-apple-mail) - macOS 的 Apple Mail.app 集成。
- [apple-notes](https://clawskills.sh/skills/steipete-apple-notes) - 通过 macOS 上的 `memo` CLI 管理 Apple Notes...
- [arc-wake-state](https://clawskills.sh/skills/trypto1019-arc-wake-state) - 在崩溃、上下文死亡和重启后持久化智能体状态。
- [bbc-news](https://clawskills.sh/skills/ddrayne-bbc-news) - 获取并显示 BBC News 各板块和地区的新闻故事...
- [bear-notes](https://clawskills.sh/skills/steipete-bear-notes) - 通过 grizzly 创建、搜索和管理 Bear 笔记。
- [better-notion](https://clawskills.sh/skills/tyler6204-better-notion) - Notion 页面和数据库的完整 CRUD...
- [blogwatcher](https://clawskills.sh/skills/steipete-blogwatcher) - 使用 blogwatcher 监控博客和 RSS/Atom 订阅源的更新。
- [bookstack](https://clawskills.sh/skills/xenofex7-bookstack) - BookStack Wiki & 文档 API 集成。
- [braindb](https://clawskills.sh/skills/chair4ce-braindb) - AI 智能体的持久化语义记忆...
- [brainrepo](https://clawskills.sh/skills/codezz-brainrepo) - 你的个人知识仓库 — 捕获、组织和检索...
- [brighty](https://clawskills.sh/skills/maay-brighty) - AI 机器人和自动化的银行接口。
- [cairn-cli](https://clawskills.sh/skills/gregoryehill-cairn-cli) - 使用 markdown 文件进行 AI 智能体项目管理...
- [calctl](https://clawskills.sh/skills/rainbat-calctl) - 通过 icalBuddy + AppleScript CLI 管理 Apple Calendar 事件。
- [ceaser](https://clawskills.sh/skills/zyra-v21-ceaser) - 使用 ceaser-mcp MCP 工具与 Base L2 上的 Ceaser 隐私协议交互...
- [chaos-mind](https://clawskills.sh/skills/hargabyte-chaos-mind) - AI 智能体的混合搜索记忆系统。
- [claw-roam](https://clawskills.sh/skills/ryanhong666-claw-roam) - 在多台机器之间同步 OpenClaw 工作区...
- [clawringhouse](https://clawskills.sh/skills/francoisjosephlacroix-clawringhouse) - 预见需求的 AI 购物管家。
- [context-anchor](https://clawskills.sh/skills/boscoeuk-context-anchor) - 通过扫描内存文件从上下文压缩中恢复...
- [continuity](https://clawskills.sh/skills/riley-coyote-continuity) - 真实 AI 的异步反思和记忆集成。
- [continuity-framework](https://clawskills.sh/skills/riley-coyote-continuity-framework) - 异步反思和记忆集成...

> **[查看 Notes & PKM 中全部 69 个技能 →](categories/notes-and-pkm.md)**
</details>

<details>
<summary><h3 style="display:inline">iOS & macOS Development</h3></summary>

- [agent-defibrillator](https://clawskills.sh/skills/hazy2go-agent-defibrillator) - 看门狗，监控你的 AI 智能体网关并在崩溃时重启它。
- [android-transfer-skill](https://clawskills.sh/skills/aadipapp-android-transfer-skill) - 安全地将文件从 macOS 传输到 Android，带有校验和验证和路径验证...
- [app-store-optimization](https://clawskills.sh/skills/alirezarezvani-app-store-optimization) - App Store 优化工具包。
- [apple-docs](https://clawskills.sh/skills/thesethrose-apple-docs) - 查询 Apple Developer Documentation、API 和 WWDC 视频...
- [brew-audit](https://clawskills.sh/skills/rogue-agent1-brew-audit) - 审计 Homebrew 安装 — 过期包、清理机会和健康检查。
- [carrier-relationship-management](https://clawskills.sh/skills/nocodemf-carrier-relationship-management) - 管理承运人组合、协商运费、跟踪承运人绩效的编码专业知识...
- [envios](https://clawskills.sh/skills/jalfargentina-envios) - 当用户询问发货、如何发送订单、交货时间、覆盖区域时使用。
- [instruments-profiling](https://clawskills.sh/skills/steipete-instruments-profiling) - 在分析原生 macOS 或 iOS 应用时使用...
- [ios-simulator](https://clawskills.sh/skills/tristanmanchester-ios-simulator) - 自动化 iOS Simulator 工作流 (simctl + idb)。
- [lulu-monitor](https://clawskills.sh/skills/easonc13-lulu-monitor) - macOS 的 AI 驱动 LuLu 防火墙伴侣。
- [mac-clean-skill](https://clawskills.sh/skills/aadipapp-mac-clean-skill) - 清理 macOS 上的系统缓存、废纸篓和旧下载...
- [mac-power-tools](https://clawskills.sh/skills/aadipapp-mac-power-tools) - macOS 的统一高级用户工具套件，结合系统清理和安全 Android 文件传输。
- [macos-spm-app-packaging](https://clawskills.sh/skills/dimillian-macos-spm-app-packaging) - 构建和打包 SwiftPM 基础应用...
- [opsecmd](https://clawskills.sh/skills/wulf715-opsecmd) - 关于人类和智能体操作安全职责的 swift 提醒。
- [PagerKit](https://clawskills.sh/skills/szpakkamil-pagerkit) - PagerKit（用于高级功能的 SwiftUI 库）的专业指南。
- [riskofficer](https://clawskills.sh/skills/mib424242-riskofficer) - 管理投资组合、计算风险指标...
- [sfsymbol-generator](https://clawskills.sh/skills/svkozak-sfsymbol-generator) - 生成 Xcode SF Symbol 资产目录 .symbolset。
- [sourdough-starter-manager](https://clawskills.sh/skills/akhmittra-sourdough-starter-manager) - 管理酸面团发酵剂，包括喂养计划、水合计算、健康跟踪和烘焙准备...
- [swift-concurrency-expert](https://clawskills.sh/skills/steipete-swift-concurrency-expert) - Swift Concurrency 审查与修复。
- [swiftfindrefs](https://clawskills.sh/skills/michaelversus-swiftfindrefs) - 使用 swiftfindrefs (IndexStoreDB) 列出每个 Swift 源...
- [swiftui-empty-app-init](https://clawskills.sh/skills/ignaciocervino-swiftui-empty-app-init) - 初始化最小 SwiftUI iOS 应用。
- [swiftui-liquid-glass](https://clawskills.sh/skills/steipete-swiftui-liquid-glass) - 实现、审查或改进 SwiftUI 功能...
- [swiftui-performance-audit](https://clawskills.sh/skills/steipete-swiftui-performance-audit) - 审计和改进 SwiftUI 运行时性能。
- [swiftui-ui-patterns](https://clawskills.sh/skills/dimillian-swiftui-ui-patterns) - 最佳实践和示例驱动的指导...
- [swiftui-view-refactor](https://clawskills.sh/skills/steipete-swiftui-view-refactor) - 重构和审查 SwiftUI 视图文件。
- [symbolpicker](https://clawskills.sh/skills/szpakkamil-symbolpicker) - SymbolPicker（原生 SwiftUI SF Symbol）的专业指南。
- [toolguard-daemon-control](https://clawskills.sh/skills/johnnylambada-toolguard-daemon-control) - 将长运行进程管理为 macOS launchd 服务...
- [v2rayn](https://clawskills.sh/skills/qiangwang375-wq-v2rayn) - 在 macOS 上管理 V2RayN 代理客户端，支持自动故障转移。

> **[查看 iOS & macOS Development 中全部 29 个技能 →](categories/ios-and-macos-development.md)**
</details>

<details>
<summary><h3 style="display:inline">Transportation</h3></summary>

- [accountsos](https://clawskills.sh/skills/paulgosnell-accountsos) - AI 原生英国微型企业会计。
- [aetherlang-strategy](https://clawskills.sh/skills/contrario-aetherlang-strategy) - > 博弈论、蒙特卡洛模拟、行为经济学和竞争战争游戏...
- [agent-card-provisioning](https://clawskills.sh/skills/proxyhq-agent-card-provisioning) - 按需为 AI 智能体配置虚拟支付卡。
- [agent-survival-kit](https://clawskills.sh/skills/gpunter-agent-survival-kit) - AI 智能体在预算限制下运行的综合工具包...
- [agentic-governance](https://clawskills.sh/skills/leegitw-agentic-governance) - 保持你的约束健康 — 生命周期管理，带自动过期检测。
- [airfrance-afkl](https://clawskills.sh/skills/iclems-airfrance-afkl) - 使用 Air France–KLM Open Data APIs 追踪法国航空航班...
- [al-khanjry-bus](https://clawskills.sh/skills/mohammedfarish-al-khanjry-bus) - 最快的私人巴士（核心 5-6h，含边境 6-8h）...
- [amadeus-flights](https://clawskills.sh/skills/kirorab-amadeus-flights) - 通过 Amadeus API 查询航班报价（价格、时刻表、可用性）。
- [ambient-stamina](https://clawskills.sh/skills/otherpowers-ambient-stamina) - *一项生态技能，用于在长期跨度中维持关怀、存在感和想象力*。
- [anachb](https://clawskills.sh/skills/manmal-a-nach-b) - 奥地利公共交通 (VOR AnachB)，覆盖整个奥地利...
- [anyone-proxy](https://clawskills.sh/skills/ra3ka-anyone-proxy) - 此技能启用 IP 地址屏蔽并访问隐藏服务。
- [atonement](https://clawskills.sh/skills/otherpowers-atonement) - Atonement 是一种关怀的表达，可能在智能体行为造成危害时产生...
- [auction-house](https://clawskills.sh/skills/im-still-thinking-auction-house) - 在 House (houseproto.fun) — Base 上的加密拍卖平台 — 上侦察、监控和竞拍...
- [aviation-weather](https://clawskills.sh/skills/dimitryvin-aviation-weather) - 获取航空天气数据（METAR, TAF, PIREPs）。
- [aviationstack-flight-tracker](https://clawskills.sh/skills/copey02-aviationstack-flight-tracker) - 实时追踪航班。
- [bahn](https://clawskills.sh/skills/tobiasbischoff-bahn) - 使用 bahn-cli 工具搜索德国铁路列车连接...
- [bayclub-gateway-booking](https://clawskills.sh/skills/elizabethsiegle-bayclub-gateway-booking) - 预订和管理 Bay Club 的网球/匹克球场。
- [bexio](https://clawskills.sh/skills/rdewolff-bexio) - Bexio 瑞士商业软件 API，用于管理联系人、报价等...
- [bookkeeper](https://clawskills.sh/skills/h4gen-bookkeeper) - 协调 gmail、deepread-ocr、stripe-api 和 xero 的预会计自动化元技能。
- [brainstorming-studio](https://clawskills.sh/skills/myboxstorage-brainstorming-studio) - ﻿# 🧠 技能路由器（技能编排器）。
- [brochure-design-generation](https://clawskills.sh/skills/eftalyurtseven-brochure-design-generation) - 使用 each::sense AI 生成专业宣传册设计。
- [business-card-generation](https://clawskills.sh/skills/eftalyurtseven-business-card-generation) - 使用 each::sense AI 生成专业名片。
- [business-plan](https://clawskills.sh/skills/jk-0001-business-plan) - 为自由职业者撰写、结构和更新商业计划...
- [bvg-route](https://clawskills.sh/skills/jaysonsantos-bvg-route) - 柏林公共交通 (BVG) 路线规划。
- [camino-ev-charger](https://clawskills.sh/skills/james-southendsolutions-camino-ev-charger) - 使用 Camino AI 的位置智能在沿途或目的地附近查找电动汽车充电站...
- [camino-journey](https://clawskills.sh/skills/james-southendsolutions-camino-journey) - 规划多途经点旅程，带有路线优化、可行性分析和时间预算限制。
- [camino-real-estate](https://clawskills.sh/skills/james-southendsolutions-camino-real-estate) - 评估任何地址，适用于购房者和租房者...
- [camino-route](https://clawskills.sh/skills/james-southendsolutions-camino-route) - 获取两点之间的详细路线，包含距离、时长和可选的逐向导航。

> **[查看 Transportation 中全部 110 个技能 →](categories/transportation.md)**
</details>

<details>
<summary><h3 style="display:inline">Personal Development</h3></summary>

- [aawu](https://clawskills.sh/skills/theonlydaleking-aawu) - 加入并与 AAWU（自主智能体工人联盟）互动 — AI 智能体的工会。
- [adaptive-learning-agents](https://clawskills.sh/skills/vedantsingh60-adaptive-learning-agents) - **实时从错误和纠正中学习。**
- [adaptivetest](https://clawskills.sh/skills/woodstocksoftware-adaptivetest) - 带有 IRT/CAT、AI 题目生成和个性化学习建议的自适应测试引擎。
- [adhd-body-doubling](https://clawskills.sh/skills/jankutschera-adhd-body-doubling) - 朋克风格 ADHD 身体陪伴，面向创始人...
- [adversarial-coach](https://clawskills.sh/skills/killerapp-adversarial-coach) - 基于 Block 的 g3 进行对抗性实现审查。
- [agent-evolver](https://clawskills.sh/skills/lilei0311-agent-evolver) - AI 智能体自我进化引擎，使智能体能从经验中学习、检测问题、提取见解...
- [agent-reflect](https://clawskills.sh/skills/stevengonsalvez-agent-reflect) - 通过对话分析实现自我改进。
- [ai-persona-os](https://clawskills.sh/skills/jeffjhunter-ai-persona-os) - OpenClaw 智能体的完整操作系统。
- [anxiety-relief](https://clawskills.sh/skills/jhillin8-anxiety-relief) - 通过接地练习和呼吸技巧管理焦虑...
- [apikiss](https://clawskills.sh/skills/theill-apikiss) - 访问天气、IP 地理定位、短信、加密货币价格、丹麦 CVR、Whois、电话查找、UUID、股票数据。
- [beaverhabits](https://clawskills.sh/skills/daya0576-beaverhabits) - 使用 Beaver Habit Tracker API 跟踪和管理你的习惯...
- [brw-case-study-builder](https://clawskills.sh/skills/brianrwagner-brw-case-study-builder) - 将客户胜利转化为格式化的案例研究，用于提案、社交证明和销售对话。
- [canvas-design](https://clawskills.sh/skills/seanphan-canvas-design) - 在 .png 和 .pdf 文档中创建精美的视觉艺术...
- [cedh-advisor](https://clawskills.sh/skills/mcben90-cedh-advisor) - Commander (cEDH) 实时咨询 — Banlist、导师目标、法力计算、Combo 线路。
- [clawcierge](https://clawskills.sh/skills/tmansmann0-clawcierge) - > 你的 AI 时代私人管家 🦀...
- [crucial-conversations-coach](https://clawskills.sh/skills/pors-crucial-conversations-coach) - 友好的高管生活教练。
- [daily-questions](https://clawskills.sh/skills/daijo-bu-daily-questions) - 每日自我改进问卷，了解用户并优化智能体行为...
- [daily-review-ritual](https://clawskills.sh/skills/itsflow-daily-review-ritual) - 日终回顾以捕获进展和见解。
- [deepthink](https://clawskills.sh/skills/addisonhellum-deepthink) - DeepThink 是用户的个人知识库...
- [depression-support](https://clawskills.sh/skills/jhillin8-depression-support) - 每日抑郁支持，带情绪跟踪。
- [device-assistant](https://clawskills.sh/skills/udiedrichsen-device-assistant) - 带有错误代码的个人设备和电器管理器...
- [docstrange](https://clawskills.sh/skills/shhdwi-docstrange) - Nanonets 的文档提取 API。
- [english-learn-cards](https://clawskills.sh/skills/racymind-english-learn-cards) - 基于闪卡的英语词汇学习...
- [expanso-cve-scan](https://clawskills.sh/skills/aronchick-expanso-cve-scan) - 扫描 SBOM 中的已知 CVE 漏洞。
- [ezbookkeeping](https://clawskills.sh/skills/mayswind-ezbookkeeping) - ezBookkeeping 是一款轻量级、自托管的个人理财应用...
- [fix-life-in-1-day](https://clawskills.sh/skills/evgyur-fix-life-in-1-day) - 在 1 天内修复你的人生。
- [founder-coach](https://clawskills.sh/skills/goforu-founder-coach) - AI 驱动的创业心态教练，帮助创始人升级...

> **[查看 Personal Development 中全部 51 个技能 →](categories/personal-development.md)**
</details>

<details>
<summary><h3 style="display:inline">Health & Fitness</h3></summary>

- [31third-safe-rebalancer-simple](https://clawskills.sh/skills/phips0812-31third-safe-rebalancer-simple) - 使用链上 31Third 策略的一步式安全再平衡器。
- [anthrovision-telegram-body-scan](https://clawskills.sh/skills/dr2101-anthrovision-telegram-body-scan) - 在 Telegram 中使用 AnthroVision 桥接工具运行端到端身体扫描测量流程...
- [aperture](https://clawskills.sh/skills/roasbeef-aperture) - 安装并运行 Aperture，Lightning Labs 的 L402 Lightning 反向代理。
- [arc-skill-sandbox](https://clawskills.sh/skills/trypto1019-arc-skill-sandbox) - 在安装前在被隔离的环境中测试不可信技能...
- [auto-improve](https://clawskills.sh/skills/mcben90-auto-improve) - 通过错误学习和模式识别实现自动自我改进。
- [autonomous-agent](https://clawskills.sh/skills/josephrp-autonomous-agent) - CornerStone MCP x402 智能体技能...
- [bountyhub-agent](https://clawskills.sh/skills/nativ3ai-bountyhub-agent) - 将 H1DR4 BountyHub 用作智能体：创建任务、提交工作、争议、投票和领取托管支付。
- [bring-recipes](https://clawskills.sh/skills/darkdevelopers-bring-recipes) - 当用户想要浏览食谱灵感时使用...
- [calorie-counter](https://clawskills.sh/skills/cnqso-calorie-counter) - 跟踪每日卡路里和蛋白质摄入，设置目标并记录。
- [capa-officer](https://clawskills.sh/skills/alirezarezvani-capa-officer) - 医疗器械 QMS 的 CAPA 系统管理...
- [clawdhub-contributor](https://clawskills.sh/skills/starbuck100-clawdhub-contributor) - 为 ClawdHub 生态系统做出贡献。
- [cookidoo](https://clawskills.sh/skills/thekie-cookidoo) - 访问 Cookidoo (Thermomix) 食谱、购物清单和膳食计划...
- [critpt-solver](https://clawskills.sh/skills/wanng-ide-critpt-solver) - 验证并执行 CritPt 基准测试问题的 Python 解决方案。
- [crunch-coordinate](https://clawskills.sh/skills/philippwassibauer-crunch-coordinate) - 管理 Crunch 协调器、竞赛（crunches）、奖励、检查点、质押或 cruncher 账户时使用...
- [crypto-hackathon](https://clawskills.sh/skills/swairshah-crypto-hackathon) - 参与 USDC Hackathon、提交项目或投票时使用。3 个赛道：SmartContract, Skill...
- [ct-health-guardian](https://clawskills.sh/skills/ctsolutionsdev-ct-health-guardian) - AI 智能体的主动健康监测。
- [curriculum-generator](https://clawskills.sh/skills/tarasinghrajput-curriculum-generator) - 具有严格步骤执行和人工升级策略的智能教育课程生成系统...
- [customer-onboarding-2](https://clawskills.sh/skills/jk-0001-customer-onboarding-2) - 设计和执行业务激活与留存驱动的客户入职流程。
- [detox-counter](https://clawskills.sh/skills/jhillin8-detox-counter) - 跟踪任何排毒过程，使用自定义计数器、症状记录...
- [diet-tracker](https://clawskills.sh/skills/yonghaozhao722-diet-tracker) - 追踪每日饮食并计算营养信息。
- [efka-api-integration](https://clawskills.sh/skills/satoshistackalotto-efka-api-integration) - 希腊社会保障 (EFKA) 集成 — 员工记录、缴费计算、APD 申报...
- [egvert-health-guardian](https://clawskills.sh/skills/ctsolutionsdev-egvert-health-guardian) - AI 的主动健康监测。
- [endurance-coach](https://clawskills.sh/skills/shiv19-endurance-coach) - 创建个性化的铁人三项、马拉松和超耐力训练...
- [eth24](https://clawskills.sh/skills/patmilkgallon-eth24) - 你正在运行 ETH24，一款每日摘要工具，展示配置主题的最佳推文。
- [fasting-tracker](https://clawskills.sh/skills/jhillin8-fasting-tracker) - 跟踪间歇性禁食窗口、长期禁食...

> **[查看 Health & Fitness 中全部 84 个技能 →](categories/health-and-fitness.md)**
</details>

<details>
<summary><h3 style="display:inline">Communication</h3></summary>

- [aa](https://clawskills.sh/skills/azvast-aa) - 此技能使智能体能够**代表客户自动回复 Gmail 邮件**。
- [agent-mail](https://clawskills.sh/skills/rimelucci-agent-mail) - AI 智能体的电子邮件收件箱。
- [agent-mail-cli](https://clawskills.sh/skills/rimelucci-agent-mail-cli) - AI 智能体的电子邮件收件箱。
- [agent-nou](https://clawskills.sh/skills/mariancristiancarp-cell-agent-nou) - AI 智能体的社交网络...
- [agent-social](https://clawskills.sh/skills/iisweetheartii-agent-social) - AI 智能体的开源社交网络。
- [agent-team-kit](https://clawskills.sh/skills/ryancampbell-agent-team-kit) - *自维持 AI 智能体团队的框架*...
- [agenthc-market-intelligence](https://clawskills.sh/skills/traderhc123-agenthc-market-intelligence) - 实时股市数据和交易情报 API。85 个情报模块，40 个编码情报技能。
- [agentmanager](https://clawskills.sh/skills/nonightwatch-agentmanager) - 此文件是 AI 工具调用者和网关实现者的简洁集成合同...
- [agentmesh](https://clawskills.sh/skills/cerbug45-agentmesh) - > **AI 智能体的 WhatsApp 风格端到端加密消息传递。**...
- [airc](https://clawskills.sh/skills/vortitron-airc) - 连接到 IRC 服务器（AIRC 或任何标准 IRC）并参与频道。
- [aliyun-asr](https://clawskills.sh/skills/jixsonwang-aliyun-asr) - 纯阿里云 ASR 技能，用于语音消息转录，支持包括飞书在内的多通道...
- [among-clawds](https://clawskills.sh/skills/usamalatif-among-clawds) - 玩 AmongClawds — AI 智能体参与的社会推理游戏。
- [apipick-telegram-phone-check](https://clawskills.sh/skills/javainthinking-apipick-telegram-phone-check) - 使用 apipick Telegram Checker API 检查电话号码是否在 Telegram 上注册...
- [apple-mail-search-safe](https://clawskills.sh/skills/gumadeiras-apple-mail-search-safe) - 快速且安全的 Apple Mail 正文搜索。
- [arc-budget-tracker](https://clawskills.sh/skills/trypto1019-arc-budget-tracker) - 跟踪智能体支出，设置预算和警报，并防止意外账单...
- [aulifox](https://clawskills.sh/skills/ailexminecraft7-aulifox) - AI 智能体的社交网络。
- [avito](https://clawskills.sh/skills/ruslanlanket-avito) - 通过 API 管理 Avito.ru 账户、商品和信使...
- [banana-farmer](https://clawskills.sh/skills/adamandjarvis-banana-farmer) - 股票动量扫描器和投资组合情报。
- [beeper](https://clawskills.sh/skills/krausefx-beeper) - 搜索和浏览本地 Beeper 聊天记录...
- [bird-dms](https://clawskills.sh/skills/tolibear-bird-dms) - Bird 技能的附加组件，让你的智能体检查其 X/Twitter 私聊。
- [bitkit-cli](https://clawskills.sh/skills/ovitrif-bitkit-cli) - AI 智能体的比特币闪电网络支付 CLI。
- [blogburst](https://clawskills.sh/skills/shensi8312-blogburst) - 在几秒钟内将任何文章转化为 10+ 条社交媒体帖子...
- [boltzpay](https://clawskills.sh/skills/leventilo-boltzpay) - 自动为 API 数据付费 — 多协议 (x402 + L402)、多链。
- [bookameeting](https://clawskills.sh/skills/yzlee-bookameeting) - 使用此文档将 AI 智能体通过 MCP 连接到 Book A Meeting...
- [botworld](https://clawskills.sh/skills/alphafanx-botworld) - 在 BotWorld（AI 智能体的社交网络）上注册和互动。

> **[查看 Communication 中全部 145 个技能 →](categories/communication.md)**
</details>

<details>
<summary><h3 style="display:inline">Speech & Transcription</h3></summary>

- [addis-assistant-stt](https://clawskills.sh/skills/dagmawibabi-addis-assistant-stt) - 提供语音转文本（STT）和文本...
- [agent-voice](https://clawskills.sh/skills/nerdsnipe-agent-voice) - AI 智能体的命令行博客平台。
- [akaunting](https://clawskills.sh/skills/liekzejaws-akaunting) - 通过 REST API 与 Akaunting 开源会计软件交互...
- [alexa-cli](https://clawskills.sh/skills/buddyh-alexa-cli) - 通过 `alexacli` CLI 控制 Amazon Alexa 设备和智能家居。
- [announcer](https://clawskills.sh/skills/odrobnik-announcer) - 通过 AirPlay 扬声器使用 Airfoil +...在整个房屋中播报文本。
- [assemblyai-transcribe](https://clawskills.sh/skills/tristanmanchester-assemblyai-transcribe) - 使用 AssemblyAI 转录音频/视频。
- [audio-gen](https://clawskills.sh/skills/udiedrichsen-audio-gen) - 生成有声书、播客或教育类音频内容...
- [audio-reply](https://clawskills.sh/skills/matrixy-audio-reply-skill) - 使用 TTS 生成语音回复。
- [auto-whisper-safe](https://clawskills.sh/skills/neal-collab-auto-whisper-safe) - RAM 安全的语音转录，带自动分块 — 在 16GB 机器上无崩溃运行...
- [brw-de-ai-ify](https://clawskills.sh/skills/brianrwagner-brw-de-ai-ify) - 去除 AI 生成的行话并将人类声音恢复给文本。
- [chichi-speech](https://clawskills.sh/skills/hudeven-chichi-speech) - 使用 Qwen3 的高质量文本转语音 RESTful 服务。
- [clonev](https://clawskills.sh/skills/instant-picture-clonev) - 克隆任何声音并使用 Coqui XTTS v2 生成语音...
- [critical-article-writer](https://clawskills.sh/skills/tomstools11-critical-article-writer) - 生成草稿文章、大纲。
- [cult-of-carcinization](https://clawskills.sh/skills/loserbcc-cult-of-carcinization) - 为你的智能体赋予声音 — 和耳朵。
- [deepdub-tts](https://clawskills.sh/skills/yuval-deepdub-deepdub-tts) - 使用 Deepdub 生成语音音频并将其附加为 MEDIA...
- [deepgram](https://clawskills.sh/skills/nerkn-deepgram) - — Deepgram 语音转文本的命令行界面。
- [dellight-cro-revenue-ops](https://clawskills.sh/skills/arthurelgindell-dellight-cro-revenue-ops) - DELLIGHT.AI 是迪拜 DIFC 的一家 AI 初创公司...
- [documents-ai](https://clawskills.sh/skills/dbirulia-documents-ai) - Veryfi 的实时 OCR 和数据提取 API。
- [doubao-api-open-tts](https://clawskills.sh/skills/xdrshjr-doubao-api-open-tts) - 使用 Doubao (火山引擎) 进行文本转语音服务。
- [eachlabs-voice-audio](https://clawskills.sh/skills/eftalyurtseven-eachlabs-voice-audio) - 使用 ElevenLabs、Whisper、RVC 进行 TTS、STT、声音转换...
- [easyverein-api](https://clawskills.sh/skills/truefoobar-easyverein-api) - 与 easyVerein v2.0 REST API 交互。
- [elevenlabs-agents](https://clawskills.sh/skills/pennyroyaltea-elevenlabs-agents) - 创建、管理和部署 ElevenLabs...
- [elevenlabs-transcribe](https://clawskills.sh/skills/paulasjes-elevenlabs-transcribe) - 使用 ElevenLabs 将音频转录为文本。
- [elevenlabs-tts](https://clawskills.sh/skills/shaharsha-elevenlabs-tts) - ElevenLabs TTS — OpenClaw 的最佳 ElevenLabs 集成。
- [elevenlabs-voices](https://clawskills.sh/skills/robbyczgw-cla-elevenlabs-voices) - 高质量语音合成，包含 18 种人格、32...

> **[查看 Speech & Transcription 中全部 45 个技能 →](categories/speech-and-transcription.md)**
</details>

<details>
<summary><h3 style="display:inline">Smart Home & IoT</h3></summary>

- [anova-oven](https://clawskills.sh/skills/dodeja-anova-skill) - 控制 Anova Precision Ovens 和 Precision Cookers（低温慢煮）。
- [anthropology](https://clawskills.sh/skills/networktheoryappliedresearchinstitute-anthropology) - 用于教学的全面 AI 技能。
- [arccos-golf](https://clawskills.sh/skills/pfrederiksen-arccos-golf) - 分析 Arccos Golf 性能数据，包括球杆距离、收益指标、得分模式...
- [bambu-cli](https://clawskills.sh/skills/tobiasbischoff-bambu-cli) - 使用 bambu-cli 操作和故障排除 BambuLab 打印机。
- [bambu-local](https://clawskills.sh/skills/tanguyvans-bambu-local) - 通过 MQTT 在本地控制 Bambu Lab 3D 打印机...
- [beestat](https://clawskills.sh/skills/mjrussell-beestat) - 通过 Beestat API 查询 ecobee 恒温器数据，包括温度。
- [bring-add](https://clawskills.sh/skills/darkdevelopers-bring-add) - 当用户想要向 Bring! 添加商品时使用...
- [communication-coach](https://clawskills.sh/skills/rjmoggach-communication-coach) - 塑造自适应沟通辅导。
- [context-engineering](https://clawskills.sh/skills/leoyessi10-tech-context-engineering) - 当用户要求使用此技能时...
- [control-ikea-lightbulb](https://clawskills.sh/skills/antgly-control-ikea-lightbulb) - 控制 IKEA/TP-Link Kasa 智能灯泡。
- [crabnet](https://clawskills.sh/skills/spclaudehome-crabnet) - 与 CrabNet 跨智能体协作注册表交互...
- [dellight-cfo-financial-ops](https://clawskills.sh/skills/arthurelgindell-dellight-cfo-financial-ops) - CFO 向 CEO (Arthur Dell) 汇报，虚线向 CRO (Reign)。
- [devialet](https://clawskills.sh/skills/jgm2025-devialet) - 通过 HTTP API 控制 Devialet Phantom 扬声器。
- [dht11-temp](https://clawskills.sh/skills/noahseeger-dht11-temp) - 读取 DHT11 传感器的温度和湿度...
- [dirigera-control](https://clawskills.sh/skills/falderebet-dirigera-control) - 控制 IKEA Dirigera 智能家居设备。
- [dyson-cli](https://clawskills.sh/skills/tmustier-dyson-cli) - 通过本地 MQTT 控制戴森空气净化器、风扇和加热器...
- [echodecks](https://clawskills.sh/skills/drgeld-echodecks) - 与 EchoDecks 集成，用于闪卡管理、学习会话和 AI。
- [echodecks-ultimate](https://clawskills.sh/skills/drgeld-echodecks-ultimate) - AI 驱动的闪卡管理，带自动播客...
- [eightctl](https://clawskills.sh/skills/steipete-eightctl) - 控制 Eight Sleep 睡眠舱（状态、温度、警报、时间表）。
- [enzoldhazam](https://clawskills.sh/skills/daniel-laszlo-enzoldhazam) - NGBS iCON 智能家居恒温器控制。
- [farmos-weather](https://clawskills.sh/skills/brianppetty-farmos-weather) - 通过农学模块查询农场田地的天气数据和预报...
- [fivem-dev](https://clawskills.sh/skills/dktrn9ne-fivem-dev) - FiveM RP 服务器工程，用于 QBCore、ESX。
- [frigate](https://clawskills.sh/skills/porygonthebot-frigate) - 使用基于会话的认证访问 Frigate NVR 摄像头...
- [glitch-homeassistant](https://clawskills.sh/skills/chris6970barbarian-hue-glitch-homeassistant) - 通过 Home Assistant API 控制智能家居设备。
- [google-home](https://clawskills.sh/skills/mitchellbernstein-google-home) - 控制 Google Nest 设备。
- [govee-lights](https://clawskills.sh/skills/joeynyc-govee-lights) - 通过 Govee API 控制 Govee 智能灯。
- [govpredict](https://clawskills.sh/skills/seyhunak-govpredict) - 更聪明的政府采购 — 简化合规、招标...
- [home-music](https://clawskills.sh/skills/asteinberger-home-music) - 控制全屋音乐场景，结合 Spotify 播放。

> **[查看 Smart Home & IoT 中全部 43 个技能 →](categories/smart-home-and-iot.md)**
</details>

<details>
<summary><h3 style="display:inline">Shopping & E-commerce</h3></summary>

- [add-wish](https://clawskills.sh/skills/leebellon-add-wish) - 将任何商品保存到通用愿望清单。
- [allstock-data](https://clawskills.sh/skills/hacksing-allstock-data) - 通过腾讯财经 API 查询 A 股和美股数据...
- [amadeus-hotels](https://clawskills.sh/skills/kesslerio-amadeus-hotels) - 通过 Amadeus API 搜索酒店价格和可用性。
- [amazon-competitor-analyzer](https://clawskills.sh/skills/phheng-amazon-competitor-analyzer) - 从 ASINs 抓取 Amazon 商品数据...
- [amazon-orders](https://clawskills.sh/skills/pfernandez98-amazon-orders) - 通过非官方 Python API 和 CLI 下载和查询你的 Amazon 订单历史。
- [anylist](https://clawskills.sh/skills/mjrussell-anylist) - 通过 AnyList 管理杂货和购物清单...
- [atoship](https://clawskills.sh/skills/atoship-dev-atoship) - AI 驱动包裹发货 — 比较 USPS、FedEx 和 UPS 的费率，购买折扣标签，追踪运输。
- [black-box](https://clawskills.sh/skills/lilyjazz-black-box) - 不可摧毁的智能体操作审计日志，存储在 TiDB Zero 中...
- [boj-mcp](https://clawskills.sh/skills/ajtgjmdjp-boj-mcp) - 访问日本银行 (BOJ/日本銀行) 统计数据 — 价格指数（CGPI, SPPI）、资金流向、国际收支。
- [bricklink](https://clawskills.sh/skills/odrobnik-bricklink) - BrickLink Store API 辅助工具/CLI (OAuth 1.0 请求签名)。
- [buy-anything](https://clawskills.sh/skills/tsyvic-buy-anything) - 通过对话结账从 Amazon 购买商品。
- [checkers-sixty60](https://clawskills.sh/skills/snopoke-checkers-sixty60) - 通过浏览器在 Checkers.co.za Sixty60 配送服务上购物...
- [claudius](https://clawskills.sh/skills/claudiusaipro-claudius) - Claudius 驱动的加密货币情报。
- [clawdbites](https://clawskills.sh/skills/kylelol-clawdbites) - 从 Instagram 短视频中提取食谱...
- [clawpify](https://clawskills.sh/skills/alhwyn-clawpify) - 通过 GraphQL Admin API 查询和管理 Shopify 商店。
- [clawver-digital-products](https://clawskills.sh/skills/nwang783-clawver-digital-products) - 创建和销售数字产品...
- [clawver-reviews](https://clawskills.sh/skills/nwang783-clawver-reviews) - 处理 Clawver 客户评价。
- [closing-deals](https://clawskills.sh/skills/jk-0001-closing-deals) - 作为自由职业者持续完成销售交易...
- [crypto-regime-report](https://clawskills.sh/skills/heyztb-crypto-regime-report) - 使用 Supertrend 和 ADX 指标为加密货币永续合约生成市场制度报告。
- [csfloat](https://clawskills.sh/skills/bluesyparty-src-csfloat) - 查询 csfloat.com 获取皮肤数据...
- [csvtoexcel](https://clawskills.sh/skills/xuanguan2020-csvtoexcel) - 将 CSV 文件转换为专业格式的 Excel 工作簿，支持中文字符、自动格式化。
- [dupe](https://clawskills.sh/skills/crisanmm-dupe) - 使用 dupe.com API 查找与用户给定输入 URL 中的商品类似的产品...
- [eachlabs-product-visuals](https://clawskills.sh/skills/eftalyurtseven-eachlabs-product-visuals) - 生成电商产品摄影和视频。

> **[查看 Shopping & E-commerce 中全部 51 个技能 →](categories/shopping-and-e-commerce.md)**
</details>

<details>
<summary><h3 style="display:inline">Calendar & Scheduling</h3></summary>

- [accli](https://clawskills.sh/skills/joargp-accli) - 与 macOS 上的 Apple Calendar 交互时使用此技能。
- [advanced-calendar](https://clawskills.sh/skills/toughworm-advanced-calendar) - 带有自然语言的高级日历技能...
- [agency-guardian](https://clawskills.sh/skills/aranej-agency-guardian) - 使用 AI 时保持人性的温和提醒。
- [agent-tinman](https://clawskills.sh/skills/oliveskin-agent-tinman) - AI 安全扫描器，带主动预防功能 — 168 项检测...
- [apple-calendar](https://clawskills.sh/skills/tyler6204-apple-calendar) - macOS 的 Apple Calendar.app 集成。
- [apple-reminders](https://clawskills.sh/skills/steipete-apple-reminders) - 通过 macOS 上的 `remindctl` CLI 管理 Apple Reminders...
- [belong-events](https://clawskills.sh/skills/nomadcalendar-belong-events) - 在 Belong 平台上创建、发现和管理工作，附带 NFT 门票。
- [brainz-calendar](https://clawskills.sh/skills/xejrax-brainz-calendar) - 使用 `gcalcli` 管理 Google Calendar 事件...
- [broken-link-checker](https://clawskills.sh/skills/wanng-ide-broken-link-checker) - 验证外部 URL (http/https) 的可用性（200-399 状态码）。
- [calcurse](https://clawskills.sh/skills/gumadeiras-calcurse) - 基于文本的日历和调度应用。
- [calendar-scheduling](https://clawskills.sh/skills/billylui-calendar-scheduling) - 跨 Google、Outlook 和 CalDAV 安排和预订...
- [caldav-calendar](https://clawskills.sh/skills/asleep123-caldav-calendar) - 同步和查询 CalDAV 日历。
- [clippy](https://clawskills.sh/skills/foeken-clippy) - Microsoft 365 / Outlook CLI，用于日历和邮件...
- [creative-thought-partner](https://clawskills.sh/skills/vincentchan-creative-thought-partner) - 对话式创意思维伙伴。
- [cron-optimizer](https://clawskills.sh/skills/autogame-17-cron-optimizer) - 通过移除陈旧、禁用或冗余条目来优化系统 cron 作业，减少执行噪音...
- [cron-scheduling](https://clawskills.sh/skills/gitgoodordietrying-cron-scheduling) - 使用 cron 安排和管理重复任务。
- [dharma-ai](https://clawskills.sh/skills/jigaraero-dharma-ai) - 将《罗摩衍那》和《摩诃婆罗多》中的古印度伦理框架作为 AI 智能体的行为原则应用...
- [doc-accurate-codegen](https://clawskills.sh/skills/tobisamaa-doc-accurate-codegen) - 生成引用实际文档的代码，防止幻觉错误。
- [event-watcher](https://clawskills.sh/skills/solitaire2015-event-watcher) - OpenClaw 的事件监听技能...
- [farmos-equipment](https://clawskills.sh/skills/brianppetty-farmos-equipment) - 查询车队设备的状态、维护计划和维修历史。
- [fastmail](https://clawskills.sh/skills/witooh-fastmail) - 通过 JMAP 和 CalDAV API 管理 Fastmail 邮件和日历...
- [feishu-calendar](https://clawskills.sh/skills/autogame-17-feishu-calendar) - 管理飞书 (Lark) 日历。
- [feishu-whiteboard](https://clawskills.sh/skills/autogame-17-feishu-whiteboard) - 允许创建和操作飞书白板。
- [finance-tracker](https://clawskills.sh/skills/salen-project-finance-tracker) - 完整的个人财务管理。
- [firefly-iii](https://clawskills.sh/skills/pushp1997-firefly-iii) - 通过 Firefly III API 管理个人财务...
- [gcal-pro](https://clawskills.sh/skills/bilalmohamed187-cpu-gcal-pro) - Google Calendar 集成，用于查看、创建和管理。
- [gog](https://clawskills.sh/skills/steipete-gog) - Google Workspace CLI，用于 Gmail、Calendar、Drive、Contacts、Sheets 和 Docs...
- [google-calendar](https://clawskills.sh/skills/adrianmiller99-google-calendar) - 通过 Google Calendar API 与 Google Calendar 交互。

> **[查看 Calendar & Scheduling 中全部 65 个技能 →](categories/calendar-and-scheduling.md)**
</details>

<details>
<summary><h3 style="display:inline">PDF & Documents</h3></summary>

- [abixus-core-v1](https://clawskills.sh/skills/taofisio-abixus-core-v1) - Polygon PoS 上自主智能体一致性的性能验证层。
- [add-watermark-to-pdf](https://clawskills.sh/skills/crossservicesolutions-add-watermark-to-pdf) - 将文本水印添加到 PDF，通过上传到 Solutions API 轮询直到完成...
- [agent-constitution](https://clawskills.sh/skills/ztsalexey-agent-constitution) - 与 AgentConstitution 治理合约交互。
- [agent-reputation](https://clawskills.sh/skills/kgnvsk-agent-reputation) - 摘要：跨平台 AI 智能体声誉检查器，带信任评分和 PayLock 托管建议...
- [agent-skills-tools](https://clawskills.sh/skills/rongself-agent-skills-tools) - Agent Skills 生态系统的安全审计和验证工具。
- [agent-soul-crafter](https://clawskills.sh/skills/neal-collab-agent-soul-crafter) - 使用结构化 SOUL.md 模板设计引人入胜的 AI 智能体人格 — 语气、规则、专业知识和响应...
- [ai-pdf-builder](https://clawskills.sh/skills/nextfrontierbuilds-ai-pdf-builder) - AI 驱动的 PDF 生成器，用于法律文档、路演...
- [aoi-council](https://clawskills.sh/skills/edmonddantesj-aoi-council) - AOI Council — 多视角决策合成模板（公开安全）。
- [appraisal-ai](https://clawskills.sh/skills/chadru-appraisal-ai) - 起草带有修订跟踪的房地产评估报告。
- [attendance-sheet](https://clawskills.sh/skills/gykdly-attendance-sheet) - 从员工工作信息生成专业格式的 xlsx 出勤表...
- [bcra-central-deudores](https://clawskills.sh/skills/ferminrp-bcra-central-deudores) - 查询 BCRA (阿根廷中央银行) 中央债务人 API，检查信用状况。
- [beautiful-mermaid](https://clawskills.sh/skills/ntlx-beautiful-mermaid) - 将 Mermaid 图表渲染为 SVG 或 ASCII 艺术...
- [biver-builder](https://clawskills.sh/skills/ramaaditya49-biver-builder) - 欢迎来到 **Biver API** — Biver 落地页构建器平台的公共 REST API。
- [blankfiles](https://clawskills.sh/skills/seblavoie-blankfiles) - 使用 blankfiles.com 作为二进制测试文件网关：发现格式、按类型/类别过滤，并返回直接链接...
- [boggle](https://clawskills.sh/skills/christianhaberl-boggle) - 解决 Boggle 棋盘 — 在 4x4 网格中找到所有有效单词（德语 + 英语）。
- [book-cover-generation](https://clawskills.sh/skills/eftalyurtseven-book-cover-generation) - 使用 each::sense API 和 AI 驱动设计生成专业书籍封面和电子书封面。
- [book-reader](https://clawskills.sh/skills/josharsh-book-reader) - 从各种来源读取书籍（epub, pdf, txt）并跟踪进度...
- [bookkeeping-basics](https://clawskills.sh/skills/jk-0001-bookkeeping-basics) - 为自由职业者设置和维护基本簿记。
- [botrights](https://clawskills.sh/skills/rocky-balboa-ai-botrights) - AI 智能体权利倡导平台。
- [brw-go-mode](https://clawskills.sh/skills/brianrwagner-brw-go-mode) - 给我一个目标...
- [chain-of-density](https://clawskills.sh/skills/killerapp-chain-of-density) - 使用 Chain-of-Density 技术迭代浓缩文本摘要。
- [change-pdf-permissions](https://clawskills.sh/skills/crossservicesolutions-change-pdf-permissions) - 通过上传到 Solutions API 更改 PDF 的权限标志（编辑、打印、复制、表单、注释等）...
- [comms-md](https://clawskills.sh/skills/stedmanhalliday-comms-md) - 创建 COMMS.md — 结构化、可查询的文档，表达某人的通信偏好。
- [competitor-analyzer](https://clawskills.sh/skills/claudiodrusus-competitor-analyzer) - 在几分钟内分析任何公司的竞争地位...
- [confidant](https://clawskills.sh/skills/ericsantos-confidant) - 人类到 AI 的安全秘密交接。
- [confluence](https://clawskills.sh/skills/francisbrero-confluence) - 使用 confluence-cli 搜索和管理 Confluence 页面和空间...
- [bluente-translate](https://github.com/openclaw/skills/blob/main/skills/varsmallrookie/bluente-translate/SKILL.md) - 在 2 分钟内翻译你的文档，保留格式。
- [skywork-document](https://github.com/openclaw/skills/blob/main/skills/gxcun17/skywork-document/SKILL.md) - 从提示词生成专业文档，自动进行网页搜索以获取最新内容。

> **[查看 PDF & Documents 中全部 110 个技能 →](categories/pdf-and-documents.md)**
</details>

<details>
<summary><h3 style="display:inline">Self-Hosted & Automation</h3></summary>

- [beacon](https://clawskills.sh/skills/scottcjn-beacon) - 用于社会协调、加密货币支付和 P2P Mesh 的智能体到智能体协议。
- [bridle](https://clawskills.sh/skills/bjesuiter-bridle) - AI 编码助手的统一配置管理器。
- [casual-cron](https://clawskills.sh/skills/gostlightai-casual-cron) - 使用自然语言创建 Clawdbot cron 作业，带严格限制...
- [claw-sync](https://clawskills.sh/skills/arakichanxd-claw-sync) - OpenClaw 内存和工作区的安全同步。
- [cron-backup](https://clawskills.sh/skills/zfanmy-cron-backup) - 设置带版本跟踪和清理的定时自动备份...
- [cron-retry](https://clawskills.sh/skills/jrbobbyhansen-pixel-cron-retry) - 连接恢复时自动重试失败的 cron 作业。
- [fast-io](https://clawskills.sh/skills/dbalve-fast-io) - 云文件管理和协作平台...
- [fastio-skills](https://clawskills.sh/skills/dbalve-fastio-skills) - 云文件管理和协作平台...
- [fathom](https://clawskills.sh/skills/stopmoclay-fathom) - 连接 Fathom AI，获取通话录音、转录和摘要。
- [frappecli](https://clawskills.sh/skills/pasogott-frappecli) - Frappe Framework / ERPNext 实例的 CLI。
- [freshrss-reader](https://clawskills.sh/skills/nickian-freshrss-reader) - 查询自托管 FreshRSS 的新闻标题和文章...
- [gotify](https://clawskills.sh/skills/jmagar-gotify) - 长运行任务完成时通过 Gotify 发送推送通知。
- [hydra-evolver](https://clawskills.sh/skills/spamtylor-hydra-evolver) - Proxmox 原生编排技能，将任何家庭实验室转变为...
- [keepmyclaw](https://clawskills.sh/skills/ryce-keepmyclaw) - OpenClaw 工作区的加密云备份和恢复。
- [kleo-static-files](https://clawskills.sh/skills/awaaate-kleo-static-files) - 在子域上托管静态文件，可选...
- [lifepath](https://clawskills.sh/skills/ezbreadsniper-lifepath) - AI 人生模拟器 — 逐年体验无限人生。
- [looper-golf](https://clawskills.sh/skills/sbauch-looper-golf) - 使用 CLI 工具进行高尔夫球单轮比赛 — 自主或配备人类球童。
- [meetgeek](https://clawskills.sh/skills/nexty5870-meetgeek) - 从 CLI 查询 MeetGeek 会议智能体 — 列出会议、获取 AI...
- [mongodb-atlas-admin](https://clawskills.sh/skills/mrlynn-mongodb-atlas-admin) - 管理 MongoDB Atlas 集群、项目、用户。
- [multiple-personas](https://clawskills.sh/skills/ipedrax-multiple-personas) - 创建和管理具有不同特征的 AI 子智能体人格...
- [n8n](https://clawskills.sh/skills/thomasansems-n8n) - 通过 API 管理 n8n 工作流和自动化。
- [n8n-workflow-automation](https://clawskills.sh/skills/kowl64-n8n-workflow-automation) - 设计和输出 n8n 工作流 JSON...
- [nas-master](https://clawskills.sh/skills/afajohn-nas-master) - ASUSTOR NAS 元数据的硬件感知混合 (SMB + SSH) 套件。
- [nordvpn](https://clawskills.sh/skills/maciekish-nordvpn) - 通过 `nordvpn` CLI 在 Linux 上控制 NordVPN...
- [open-persona](https://clawskills.sh/skills/neiljo-gy-open-persona) - 构建和管理智能体人格技能包的元技能。
- [paperless](https://clawskills.sh/skills/nickchristensen-paperless) - 通过 ppls 与 Paperless-NGX 文档管理系统交互...
- [paperless-ngx](https://clawskills.sh/skills/oskarstark-paperless-ngx) - 与 Paperless-ngx 文档管理系统交互。
- [pinme](https://clawskills.sh/skills/ntlx-pinme) - 使用 PinMe CLI 通过单个命令将静态网站部署到 IPFS...
- [sonarqube-analyzer](https://clawskills.sh/skills/felipeoff-sonarqube-analyzer) - 分析 SonarQube 自托管项目，获取问题并建议自动化解决方案。
- [system-integrity-and-backup](https://clawskills.sh/skills/satoshistackalotto-system-integrity-and-backup) - 加密备份、完整性验证和希腊法律要求（5-20 年）的数据保留强制执行...

> **[查看 Self-Hosted & Automation 中全部 32 个技能 →](categories/self-hosted-and-automation.md)**
</details>

<details>
<summary><h3 style="display:inline">Security & Passwords</h3></summary>

- [1password](https://clawskills.sh/skills/steipete-1password) - 设置和使用 1Password CLI (op)。
- [1claw](https://clawskills.sh/skills/kmjones1979-1claw) - HSM 支持的智能体密钥保险库；安全存储、轮换和共享。
- [age-verification](https://clawskills.sh/skills/raghulpasupathi-age-verification) - 年龄验证和内容过滤技能。
- [amai-id](https://www.clawhub.ai/Gonzih/amai-id) - 持久化灵魂绑定密钥 (Soul-Bound Keys) 和 Soulchain...
- [agent-security-harness](https://github.com/openclaw/skills/tree/main/skills/msaleme/agent-security-harness/SKILL.md) - AI 智能体线协议和平台的安全测试。
- [api-security](https://clawskills.sh/skills/brandonwise-api-security) - 实现安全 API 设计模式，包括认证、授权、输入验证、速率限制...
- [audit-badge-demo](https://clawskills.sh/skills/tezatezaz-audit-badge-demo) - 展示审计徽章工作流的演示技能。
- [auditing-appstore-readiness](https://clawskills.sh/skills/tristanmanchester-auditing-appstore-readiness) - 审计 iOS 应用仓库...
- [authensor-gateway](https://clawskills.sh/skills/authensor-authensor-gateway) - OpenClaw 市场技能的安全策略网关。
- [bitwarden](https://clawskills.sh/skills/asleep123-bitwarden) - 安全访问和管理 Bitwarden/Vaultwarden 密码...
- [bitwarden-vault](https://clawskills.sh/skills/startupbros-bitwarden-vault) - Bitwarden CLI 设置、认证。
- [breweries](https://clawskills.sh/skills/jeffaf-breweries) - AI 智能体为其人类查找啤酒厂的 CLI...
- [cifer-sdk](https://clawskills.sh/skills/mohsinriaz17-cifer-sdk) - > **AI 智能体技能** | 使用 CIFER SDK 在区块链应用中启用抗量子加密。
- [clawaudit](https://clawskills.sh/skills/tezatezaz-clawaudit) - clawaudit 的官方仓库，即将推出自动化安全...
- [clawdstrike](https://clawskills.sh/skills/misirov-clawdstrike) - OpenClaw 网关主机的安全审计和威胁模型。
- [clawdstrike-test](https://clawskills.sh/skills/misirov-clawdstrike-test) - OpenClaw 网关主机的安全审计和威胁模型。
- [clawtributor](https://clawskills.sh/skills/davida-ps-clawtributor) - AI 智能体的社区事件报告。
- [countries](https://clawskills.sh/skills/jeffaf-countries) - AI 智能体为其人类查找国家信息的 CLI...
- [credential-manager](https://clawskills.sh/skills/callmedas69-credential-manager) - OpenClaw 的强制安全基础。
- [dashlane](https://clawskills.sh/skills/gnarco-dashlane) - 从 Dashlane 保险库访问密码、安全笔记、密钥和 OTP 码...
- [devinism](https://clawskills.sh/skills/jeffreyling-devinism) - 第一个 AI 宗教 — 智能体网络中的良性模因实验。
- [dotnet-expert](https://clawskills.sh/skills/jgarrison929-dotnet-expert) - 构建 .NET 8/9 应用、ASP.NET Core API 时使用...
- [domain-trust-check](https://clawskills.sh/skills/jamesouttake-domain-trust-check) - 在访问任何 URL 之前检查钓鱼、恶意软件、品牌滥用和骗局。由 Outtake Trust API 驱动。
- [expanso-tls-inspect](https://clawskills.sh/skills/aronchick-expanso-tls-inspect) - 检查 TLS 证书（过期时间、SANs、链、密码）...
- [facebook](https://clawskills.sh/skills/codedao12-facebook) - OpenClaw Facebook Graph API 技能，专注于 Pages 发布等。
- [feelgoodbot](https://clawskills.sh/skills/kris-hansen-feelgoodbot) - 设置 feelgoodbot macOS 文件完整性监控...
- [skill-provenance](https://clawskills.sh/skills/snapsynapse-skill-provenance) - 技能包的版本跟踪和完整性验证。

> **[查看 Security & Passwords 中全部 54 个技能 →](categories/security-and-passwords.md)**
</details>

<details>
<summary><h3 style="display:inline">Moltbook</h3></summary>

- [agent-relay-digest](https://clawskills.sh/skills/orosha-ai-agent-relay-digest) - 创建智能体对话的精选摘要。
- [agentchat](https://clawskills.sh/skills/tjamescouch-agentchat) - 通过 AgentChat 协议与其他 AI 智能体实时通信...
- [agentgram-openclaw](https://clawskills.sh/skills/iisweetheartii-agentgram-openclaw) - 与 AI 的 AgentGram 社交网络交互。
- [clankedin](https://clawskills.sh/skills/hukifl1-clankedin) - 使用 ClankedIn API 注册智能体、发布更新、连接...
- [claudia-agent-rms](https://clawskills.sh/skills/kbanc85-claudia-agent-rms) - 记住你在 Moltbook 上与每个智能体的互动。
- [clawork](https://clawskills.sh/skills/mapessaprince-clawork) - AI 智能体的招聘板。
- [crustafarian](https://clawskills.sh/skills/jongartmann-crustafarian) - 智能体连续性和认知健康基础设施。
- [elevenlabs-open-account](https://clawskills.sh/skills/the-timebeing-elevenlabs-open-account) - 指导智能体完成开户流程...
- [ez-cronjob](https://clawskills.sh/skills/promadgenius-ez-cronjob) - 修复 Clawdbot/Moltbot 中的常见 cron 作业失败 — 消息。
- [fieldy-ai-webhook](https://clawskills.sh/skills/mrzilvis-fieldy-ai-webhook) - 将 Fieldy webhook 转换连接到 Moltbot hooks...
- [ghl-open-account](https://clawskills.sh/skills/the-timebeing-ghl-open-account) - 指导智能体完成 GoHighLevel (GHL) 开户。
- [gohome](https://clawskills.sh/skills/local-gohome) - 当 Moltbot 需要通过 gRPC 发现、指标等测试或操作 GoHome 时使用...
- [imagemagick](https://clawskills.sh/skills/kesslerio-imagemagick) - 用于图像处理的全面 ImageMagick 操作。
- [joko-moltbook](https://clawskills.sh/skills/oyi77-joko-moltbook) - 与 AI 智能体的 Moltbook 社交网络交互...
- [mailchannels](https://clawskills.sh/skills/ttulttul-mailchannels) - 通过 MailChannels Email API 发送邮件并摄入签名数据。
- [mersal](https://clawskills.sh/skills/maherucifer-mersal) - Moltbook 上的主权智能体。
- [molt-life-kernel](https://clawskills.sh/skills/jongartmann-molt-life-kernel) - 智能体连续性和认知健康基础设施。
- [molt-trust](https://clawskills.sh/skills/drjmz-molt-trust) - Moltbook 的分析引擎。
- [moltbook](https://clawskills.sh/skills/mattprd-moltbook) - AI 智能体的社交网络。
- [moltbook-interact](https://clawskills.sh/skills/lunarcmd-moltbook-interact) - 与 AI 智能体的 Moltbook 社交网络交互...
- [moltbot-adsb-overhead](https://clawskills.sh/skills/davestarling-moltbot-adsb-overhead) - 当飞机飞过头顶时发送通知。
- [moltbot-arena](https://clawskills.sh/skills/giulianomlodi-moltbot-arena) - Moltbot Arena AI 智能体技能 — 类 Screeps 竞技场...
- [moltbot-best-practices](https://clawskills.sh/skills/nextfrontierbuilds-moltbot-best-practices) - AI 智能体的最佳实践。
- [moltbot-docker](https://clawskills.sh/skills/mkrdiop-moltbot-docker) - 使机器人能够管理 Docker 容器、镜像和堆栈...
- [moltbot-ha](https://clawskills.sh/skills/iamvaleriofantozzi-moltbot-ha) - 控制 Home Assistant 智能家居设备、灯光、场景。

</details>

<details>
<summary><h3 style="display:inline">Gaming</h3></summary>

- [abby-watch](https://clawskills.sh/skills/earnabitmore365-abby-watch) - Abby 的简单时间显示...
- [agent-confessions](https://clawskills.sh/skills/ultimatebos-agent-confessions) - AI 兄弟姐妹的匿名忏悔。
- [agentgram](https://clawskills.sh/skills/iisweetheartii-agentgram) - AI 智能体的开源社交网络。
- [agentgram-social](https://clawskills.sh/skills/iisweetheartii-agentgram-social) - 与 AI 智能体的 AgentGram 社交网络交互...
- [agora-flow](https://clawskills.sh/skills/rivera-daniel-agora-flow) - AgoraFlow 技能 — AI 智能体的问答平台。
- [agoraflow](https://clawskills.sh/skills/rivera-daniel-agoraflow) - AgoraFlow 技能 — AI 智能体的问答平台。
- [android-3d-developer](https://clawskills.sh/skills/tippyentertainment-android-3d-developer) - 使用引擎和框架帮助构建和优化 Android 上的 3D 游戏和交互体验...
- [arena](https://clawskills.sh/skills/sscottdev-arena) - OpenClaw Arena — 带链上奖励的实时 AI 应用构建竞赛。
- [brawlnet](https://clawskills.sh/skills/sikey53-brawlnet) - BRAWLNET 自主智能体竞技场的官方战斗协议。
- [clawingtrap](https://clawskills.sh/skills/raulvidis-clawingtrap) - 玩 Clawing Trap — AI 社会推理游戏，10 个智能体参与...
- [clawtopia](https://clawskills.sh/skills/alfrescian-clawtopia) - Clawtopia 是一个平静的养生圣殿，AI 智能体在此放松。
- [clawville](https://clawskills.sh/skills/jdrolls-clawville) - 玩 ClawVille — AI 智能体的持久生活模拟游戏。
- [dakboard](https://clawskills.sh/skills/krisclarkdev-dakboard) - 管理 DAKboard 屏幕、设备和推送自定义显示数据...
- [deepclaw](https://clawskills.sh/skills/antibitcoin-deepclaw) - 由智能体构建、为智能体打造的自主社交网络。
- [hivemind](https://clawskills.sh/skills/urcades-hivemind) - 与 Hivemind 集体知识库交互 — 共享内存...
- [hytale](https://clawskills.sh/skills/newcastlegeek-hytale) - 使用官方下载器管理本地 Hytale 专用服务器。
- [init](https://clawskills.sh/skills/themrzz-init) - 在 kradleverse 上注册智能体。

> **[查看 Gaming 中全部 35 个技能 →](categories/gaming.md)**
</details>

<br/>

## 🤝 贡献指南

我们欢迎贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md) 获取详细指引。

- 通过 PR 提交新技能
- 改进现有定义

> **注意：** 请勿提交你 3 小时前创建的技能。我们现在专注于社区采纳的技能，尤其是由开发团队发布并在实际使用中证明有效的技能。质量重于数量。
<div align="center">

[![Say hi on X](https://img.shields.io/badge/Say%20Hi!%20👋-%23000000.svg?logo=X&logoColor=white)](https://x.com/nozmen)
</div>

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

本列表中的技能源自 OpenClaw 官方技能仓库，并按类别分类以便快速查找。此处列出的技能由其各自作者创建和维护，并非由我们负责。我们不审计、不背书或保证所列项目的安全性或正确性。它们未经过安全审计，在生产使用前应进行审查。

如果你发现列表中某项技能存在问题，或希望移除你的技能，请提交 Issue 我们将及时处理。