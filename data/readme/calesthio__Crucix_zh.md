<div align="center">

# Crucix

**你的专属智能终端。27个数据源。一条命令。零云端。**

## [访问在线站点: crucix.live](https://www.crucix.live/)

[![Live Website](https://img.shields.io/badge/live-crucix.live-00d4ff?style=for-the-badge)](https://www.crucix.live/)
[![Open Demo](https://img.shields.io/badge/open-live%20dashboard-0b1220?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.crucix.live/)

[![Node.js 22+](https://img.shields.io/badge/node-22%2B-brightgreen)](#quick-start)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPLv3-blue.svg)](LICENSE)
[![Dependencies](https://img.shields.io/badge/dependencies-1%20(express)-orange)](#architecture)
[![Sources](https://img.shields.io/badge/OSINT%20sources-27-cyan)](#data-sources-27)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](#docker)

**接入信号网络**

[![Signal Wire](https://img.shields.io/badge/Signal%20Wire-%40crucixmonitor-111111?style=for-the-badge&logo=x&logoColor=white)](https://x.com/crucixmonitor)
[![Ops Room](https://img.shields.io/badge/Ops%20Room-Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/ChVy7SF4)

![Crucix Dashboard](docs/dashboard.png)

<details>
<summary>更多截图</summary>

| 启动序列 | 世界地图 |
|:---:|:---:|
| ![Boot](docs/boot.png) | ![Map](docs/map.png) |

| 3D 地球仪视图 |
|:---:|
| ![Globe](docs/globe.png) |

</details>

</div>

> **在线站点：** [https://www.crucix.live/](https://www.crucix.live/)
> 建议先体验公共演示，然后克隆仓库在本地运行 Crucix。

Crucix 从 27 个开源情报（OSINT）数据源并行获取卫星火情探测、航班追踪、辐射监测、卫星星座跟踪、经济指标、实时市场价格、冲突数据和制裁名单以及社交媒体情绪——每 15 分钟更新一次，并在一个自包含的 Jarvis 风格仪表盘上渲染所有内容。

接入大语言模型（LLM）后，它将成为一个**双向情报助手**——当发生重大变化时向 Telegram 和 Discord 推送多级警报，响应你手机上的 `/brief` 和 `/sweep` 命令，并基于真实的跨领域数据生成可操作的交易建议。就像一位在你熟睡时替你监控世界的分析师。

先在 [https://www.crucix.live/](https://www.crucix.live/) 体验在线演示，当你需要完整的本地部署环境时再克隆仓库。

无需云服务。无遥测数据收集。无订阅费用。只需运行 `node server.mjs`，即可启动。

## Token / 资产警告

> [!WARNING]
> **Crucix 尚未发行任何官方代币、硬币、NFT、空投、预售或其他基于区块链的资产。**
> 使用 Crucix 名称、标志或品牌标识的任何代币或数字资产均与 Crucix 无关，也未获其认可。
> 请勿购买、推广、连接钱包领取、签署交易或发送资金，切勿轻信第三方帖子、私信或网站的相关宣传。

---

## 为什么会有这个项目

世界上大部分实时情报——卫星图像、辐射水平、冲突事件、经济指标、航班追踪、海上活动——都是公开可用的。它们只是分散在数十个政府 API、研究机构和开源数据源中，没人有时间逐一检查。

Crucix 将它们全部整合到一个地方。不设付费墙，不锁定在企业平台内，不需要安全许可。只需开放数据，在你自己的机器上进行聚合和交叉关联，每 15 分钟更新一次。

它旨在帮助任何想了解世界真实动态的人——研究人员、记者、交易员、OSINT 分析师，或者只是那些相信信息获取不应受预算限制的好奇者。

---

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/calesthio/Crucix.git
cd Crucix

# 2. 安装依赖（仅需 Express）
npm install

# 3. 复制环境变量模板并添加你的 API Key（见下文）
cp .env.example .env

# 4. 启动仪表盘
npm run dev
```

> **如果 `npm run dev` 静默失败**（退出且无输出），请直接运行 Node：
> ```bash
> node --trace-warnings server.mjs
> ```
> 这将绕过 npm 的脚本执行器，后者在某些系统上（尤其是 Windows PowerShell）可能会吞掉错误。你也可以运行 `node diag.mjs` 来诊断具体问题——它会检查你的 Node 版本、单独测试每个模块导入，并验证端口可用性。详见 [故障排除](#troubleshooting)。

仪表盘会自动在 `http://localhost:3117` 打开，并开始第一次情报扫描。这次初始扫描会并行查询所有 27 个数据源，通常需要 30–60 秒——在扫描完成并推送首次数据更新之前，仪表盘将显示为空。之后，它将通过 SSE（Server-Sent Events）每 15 分钟自动刷新。无需手动刷新页面。

**要求：** Node.js 22+（使用原生 `fetch`、顶层 `await`、ESM）

### Docker

```bash
git clone https://github.com/calesthio/Crucix.git
cd Crucix
cp .env.example .env    # 添加你的 API Key
docker compose up -d
```

仪表盘地址：`http://localhost:3117`。扫描数据通过卷挂载持久化在 `./runs/` 中。包含健康检查端点。

---

## 你将获得什么

### 实时仪表盘
一个自包含的 Jarvis 风格 HUD，具备：
- **3D WebGL 地球仪**（Globe.gl），带有大气辉光、星空背景和流畅旋转——另附经典平面地图切换功能
- **9 种标记类型**覆盖两种视图：火情探测、航空交通、辐射站点、海上咽喉要道、SDR 接收器、OSINT 事件、健康警报、地理位置新闻、冲突事件
- **动画 3D 飞行走廊弧线**连接航空热点和全球枢纽
- **区域过滤器**（世界、美洲、欧洲、中东、亚太、非洲）——旋转地球仪或缩放平面地图
- **实时市场数据** ——指数、加密货币、能源、大宗商品，通过 Yahoo Finance 提供（无需 API Key）
- **风险仪表盘** —— VIX、高收益利差、供应链压力指数
- **OSINT 信息流** —— 来自 17 个 Telegram 情报频道的英文帖子（可展开）
- **新闻滚动条** —— 合并的 RSS + GDELT 头条 + Telegram 帖子，自动滚动
- **扫描增量（Sweep delta）** —— 实时面板显示自上次扫描以来的变化（新信号、升级、降级及其严重程度）
- **跨源信号** —— 卫星、经济、冲突和社交领域的交叉关联情报
- **核监测** —— Safecast + EPA RadNet 的实时辐射读数
- **太空监测** —— CelesTrak 卫星追踪：近期发射、国际空间站（ISS）、军事星座、Starlink/OneWeb 数量统计
- **可落地的交易思路** —— AI 生成的交易建议（配合 LLM）或基于信号关联的思路（无 LLM 时）

### 性能模式
顶部栏的 `VISUALS FULL` / `VISUALS LITE` 按钮仅更改渲染行为，**不会**移除数据源或减少扫描范围。

切换到 **VISUALS LITE** 后，仪表盘会：
- 禁用装饰性背景效果（如径向/网格覆盖层和扫描线）
- 移除面板和覆盖层上昂贵的模糊/背景滤镜效果
- 停止非关键动画（如图标环闪烁、冲突光环和走廊流动效果）
- 禁用地球仪自动旋转，关闭飞行弧线动画虚线
- 将水平新闻滚动条和 OSINT 信息流转换为静态可滚动列表，而非持续滚动的跑马灯

移动端特定行为：
- 在移动设备上，`VISUALS LITE` 还会强制仪表盘进入**平面地图模式**（如果你当前正在查看地球仪）
- 未来加载时，低功耗模式下将继续以平面地图作为默认视图

该偏好设置保存在浏览器本地存储中，因此界面会记住你上次的选择。

### 自动刷新
服务器每 15 分钟运行一次扫描周期（可配置）。每个周期：
1. 并行查询所有 27 个数据源（约 30 秒）
2. 将原始数据合成仪表盘格式
3. 计算与上次运行的增量差异（变化、升级、降级内容）——在仪表盘的 **Sweep Delta** 面板中可见
4. 生成 LLM 交易建议（如果已配置）
5. 评估突发新闻警报 —— 多级（FLASH / PRIORITY / ROUTINE），具备语义去重功能。若已配置，则发送至 Telegram 和/或 Discord。支持 LLM 评估，或在 LLM 不可用时回退到基于规则的警报系统。
6. 通过 SSE 向所有连接的浏览器推送更新

### Telegram 机器人（双向交互）
Crucix 同时作为交互式 Telegram 机器人运行。除了发送警报外，它还直接响应聊天中的命令：

| Command | 功能 |
|---------|-------------|
| `/status` | 系统健康状态、上次扫描时间、数据源状态、LLM 状态 |
| `/sweep` | 触发手动扫描周期 |
| `/brief` | 最新情报的紧凑文本摘要（趋势、关键指标、顶级 OSINT） |
| `/portfolio` | 投资组合状态（如果已连接 Alpaca） |
| `/alerts` | 带有分级标签的近期警报历史 |
| `/mute` / `/mute 2h` | 静音 1 小时（或自定义时长） |
| `/unmute` | 恢复警报 |
| `/help` | 显示所有可用命令 |

这需要在 `.env` 中配置 `TELEGRAM_BOT_TOKEN` 和 `TELEGRAM_CHAT_ID`。机器人每 5 秒轮询一次消息（可通过 `TELEGRAM_POLL_INTERVAL` 配置）。

### Discord 机器人（双向交互）

Crucix 也支持将 Discord 作为功能完整的机器人，具备斜杠命令和丰富的嵌入警报。它镜像了 Telegram 机器人的功能，并采用 Discord 原生格式。

| Command | 功能 |
|---------|-------------|
| `/status` | 系统健康状态、上次扫描时间、数据源状态、LLM 状态 |
| `/sweep` | 触发手动扫描周期 |
| `/brief` | 最新情报的紧凑文本摘要 |
| `/portfolio` | 投资组合状态（如果已连接 Alpaca） |

警报以丰富的嵌入形式发送，带有彩色侧边栏：红色代表 FLASH，黄色代表 PRIORITY，蓝色代表 ROUTINE。每个嵌入包含信号详情、置信度分数和跨领域关联数据。

**设置需要：** `DISCORD_BOT_TOKEN`、`DISCORD_CHANNEL_ID`，以及可选的 `DISCORD_GUILD_ID` 用于即时注册斜杠命令。详见 [API Key 设置](#api-keys-setup)。

**Webhook 回退方案：** 如果你不想运行完整机器人，可仅设置 `DISCORD_WEBHOOK_URL`。这将启用单向警报（无斜杠命令）且零依赖——无需 `discord.js`。

**可选依赖项：** 完整机器人需要 `discord.js`。通过 `npm install discord.js` 安装。如果未安装，Crucix 会自动回退到仅 Webhook 模式。

### 可选 LLM 层
连接任意 8 个 LLM 提供商以增强分析能力：
- **AI 交易建议** —— 量化分析师生成 5-8 条引用具体数据的可操作建议
- **更智能的警报评估** —— LLM 将信号分类为 FLASH/PRIORITY/ROUTINE 等级，具备跨领域关联和置信度评分功能
- **提供商：** Anthropic Claude、OpenAI、Google Gemini、OpenRouter（统一 API）、OpenAI Codex（ChatGPT 订阅版）、MiniMax、Mistral、Grok
- **优雅降级** —— 当 LLM 不可用时，基于规则的引擎将接管警报评估。LLM 故障绝不会导致扫描周期崩溃。

---

## API Key 设置

在项目根目录将 `.env.example` 复制为 `.env`：

```bash
cp .env.example .env
```

### 最佳体验所需（全部免费）

| Key | 来源 | 获取方式 |
|-----|--------|------------|
| `FRED_API_KEY` | 联邦储备经济数据 (Federal Reserve Economic Data) | [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html) —— 即时，免费 |
| `FIRMS_MAP_KEY` | NASA FIRMS（卫星火情数据） | [firms.modaps.eosdis.nasa.gov](https://firms.modaps.eosdis.nasa.gov/api/area/) —— 即时，免费 |
| `EIA_API_KEY` | 美国能源信息管理局 (US Energy Information Administration) | [api.eia.gov](https://www.eia.gov/opendata/register.php) —— 即时，免费 |

这三个 Key 将解锁最有价值的经济和卫星数据。每个注册过程约需 60 秒。

### 可选（启用额外数据源）

| Key | 来源 | 获取方式 |
|-----|--------|------------|
| `ACLED_EMAIL` + `ACLED_PASSWORD` | 武装冲突事件数据 | [acleddata.com/register](https://acleddata.com/register/) —— 免费，OAuth2 |
| `AISSTREAM_API_KEY` | 海上 AIS 船舶追踪 | [aisstream.io](https://aisstream.io/) —— 免费 |
| `ADSB_API_KEY` | 未过滤的航班追踪 | [RapidAPI](https://rapidapi.com/adsbexchange/api/adsbexchange-com1) —— 约 $10/月 |

### LLM 提供商（可选，用于 AI 增强建议）

将 `LLM_PROVIDER` 设置为以下之一：`anthropic`, `openai`, `gemini`, `codex`, `openrouter`, `minimax`, `mistral`, `grok`

| Provider | Key Required | Default Model |
|----------|-------------|---------------|
| `anthropic` | `LLM_API_KEY` | claude-sonnet-4-6 |
| `openai` | `LLM_API_KEY` | gpt-5.4 |
| `gemini` | `LLM_API_KEY` | gemini-3.1-pro |
| `openrouter` | `LLM_API_KEY` | openrouter/auto |
| `codex` | None (uses `~/.codex/auth.json`) | gpt-5.3-codex |
| `minimax` | `LLM_API_KEY` | MiniMax-M2.5 |
| `mistral` | `LLM_API_KEY` | mistral-large-latest |
| `grok` | `LLM_API_KEY` | grok-4-latest |

对于 Codex，运行 `npx @openai/codex login` 通过你的 ChatGPT 订阅进行身份验证。

### Telegram Bot + Alerts（可选）

| Key | How to Get |
|-----|------------|
| `TELEGRAM_BOT_TOKEN` | 在 Telegram 中通过 [@BotFather](https://t.me/BotFather) 创建 |
| `TELEGRAM_CHAT_ID` | 通过 [@userinfobot](https://t.me/userinfobot) 获取 |
| `TELEGRAM_CHANNELS` | *（可选）* 除内置的 17 个频道外，需额外监控的频道 ID（逗号分隔） |
| `TELEGRAM_POLL_INTERVAL` | *（可选）* 机器人命令轮询间隔（毫秒），默认：5000 |

### Discord Bot + Alerts（可选）

| Key | How to Get |
|-----|------------|
| `DISCORD_BOT_TOKEN` | 在 [Discord Developer Portal](https://discord.com/developers/applications) → Bot → Token 创建 |
| `DISCORD_CHANNEL_ID` | 在 Discord 中右键点击频道（开启开发者模式）→ 复制频道 ID |
| `DISCORD_GUILD_ID` | *（可选）* 右键点击服务器 → 复制服务器 ID。启用即时斜杠命令注册（否则全局命令最多需 1 小时生效） |
| `DISCORD_WEBHOOK_URL` | *（可选）* 频道设置 → 集成 → Webhooks → 新建 Webhook → 复制链接。用于无机器人的纯警报模式 |

**Discord bot setup:**
1. 前往 [Discord Developer Portal](https://discord.com/developers/applications) 并创建新应用
2. 进入 **Bot** → 点击 **Reset Token** → 将令牌复制到 `DISCORD_BOT_TOKEN`
3. 在 **Privileged Gateway Intents** 下，启用 **Message Content Intent**
4. 前往 **OAuth2** → **URL Generator** → 选择 `bot` + `applications.commands` 作用域 → 勾选 `Send Messages` + `Embed Links` 权限
5. 复制生成的 URL 并在浏览器中打开，将机器人邀请到你的服务器
6. 安装依赖项：`npm install discord.js`

Telegram 和 Discord 的警报均可在有无 LLM 的情况下工作。配置 LLM 后，信号评估更丰富且更具上下文感知能力。未配置时，确定性规则引擎将根据严重程度、跨领域关联和信号数量进行评估。

### Without Any Keys

Crucix 即使零 API Key 也能正常运行。18+ 个数据源完全不需要身份验证。需要 Key 的数据源会返回结构化错误，其余扫描照常进行。

---

## Architecture

```
crucix/
├── server.mjs                 # Express 开发服务器（SSE、自动刷新、LLM、机器人命令）
├── crucix.config.mjs          # 配置项，支持环境变量覆盖 + 增量阈值设置
├── diag.mjs                   # 诊断脚本 —— 若服务器启动失败请运行此文件
├── .env.example               # 所有已记录的环境变量模板
├── package.json               # 运行时依赖：express | 可选依赖：discord.js
├── docs/                      # README 引用截图
│
├── apis/
│   ├── briefing.mjs           # 主控编排器 —— 并行运行全部 27 个数据源
│   ├── save-briefing.mjs      # CLI：保存带时间戳的文件 + latest.json
│   ├── BRIEFING_PROMPT.md     # 情报合成协议
│   ├── BRIEFING_TEMPLATE.md   # 简报输出结构
│   ├── utils/
│   │   ├── fetch.mjs          # safeFetch() —— 超时、重试、中止、自动 JSON
│   │   └── env.mjs            # .env 加载器（无 dotenv 依赖）
│   └── sources/               # 27 个自包含数据源模块
│       ├── gdelt.mjs          # 每个文件导出 briefing() → 结构化数据
│       ├── fred.mjs           # 可独立运行：node apis/sources/fred.mjs
│       ├── space.mjs          # CelesTrak 卫星追踪
│       ├── yfinance.mjs       # Yahoo Finance —— 免费实时市场数据
│       └── ...                # 其余 23 个
│
├── dashboard/
│   ├── inject.mjs             # 数据合成 + 独立 HTML 注入
│   └── public/
│       └── jarvis.html        # 自包含 Jarvis HUD
│
├── lib/
│   ├── llm/                   # LLM 抽象层（8 个提供商，原生 fetch，无 SDK）
│   │   ├── provider.mjs       # 基类
│   │   ├── anthropic.mjs      # Claude
│   │   ├── openai.mjs         # GPT
│   │   ├── gemini.mjs         # Gemini
│   │   ├── grok.mjs           # Grok
│   │   ├── openrouter.mjs     # OpenRouter（统一 API）
│   │   ├── codex.mjs          # Codex（ChatGPT 订阅版）
│   │   ├── minimax.mjs        # MiniMax（M2.5，204K 上下文）
│   │   ├── mistral.mjs        # Mistral AI
│   │   ├── ideas.mjs          # LLM 驱动的交易建议生成
│   │   └── index.mjs          # 工厂方法：createLLMProvider()
│   ├── delta/                 # 扫描周期间的变更追踪
│   │   ├── engine.mjs         # 增量计算 —— 语义去重、可配置阈值、严重程度评分
│   │   ├── memory.mjs         # 热内存（3 次运行记录，原子写入）+ 冷存储（每日归档）
│   │   └── index.mjs          # 重新导出
│   └── alerts/
│       ├── telegram.mjs       # 多级警报（FLASH/PRIORITY/ROUTINE） + 双向机器人命令
│       └── discord.mjs        # Discord 机器人（斜杠命令、丰富嵌入） + Webhook 回退
│
└── runs/                      # 运行时数据（已加入 .gitignore）
    ├── latest.json            # 最近一次扫描输出
    └── memory/                # 增量记忆文件（hot.json + cold/YYYY-MM-DD.json）
```

### Design Principles
- **纯 ESM** —— 所有文件均为 `.mjs`，使用显式导入语句
- **最小依赖项** —— Express 是唯一的运行时依赖。`discord.js` 为可选（用于 Discord 机器人）。LLM 提供商使用原生 `fetch()`，无 SDK。
- **并行执行** —— `Promise.allSettled()` 同时触发全部 27 个数据源查询
- **优雅降级** —— 缺失 Key 会产生错误而非崩溃。LLM 故障不会中断扫描周期。
- **各数据源独立运行** —— 运行 `node apis/sources/gdelt.mjs` 即可独立测试任意数据源
- **自包含仪表盘** —— HTML 文件在有无服务器的情况下均可正常工作

---

## Data Sources (27)

### Tier 1: Core OSINT & Geopolitical (11)

| Source | What It Tracks | Auth |
|--------|---------------|------|
| **GDELT** | Global news events, conflict mapping (100+ languages) | None |
| **OpenSky** | Real-time ADS-B flight tracking across 6 hotspot regions | None |
| **NASA FIRMS** | Satellite fire/thermal anomaly detection (3hr latency) | Free key |
| **Maritime/AIS** | Vessel tracking, dark ships, sanctions evasion | Free key |
| **Safecast** | Citizen-science radiation monitoring near 6 nuclear sites | None |
| **ACLED** | Armed conflict events: battles, explosions, protests | Free (OAuth2) |
| **ReliefWeb** | UN humanitarian crisis tracking | None |
| **WHO** | Disease outbreaks and health emergencies | None |
| **OFAC** | US Treasury sanctions (SDN list) | None |
| **OpenSanctions** | Aggregated global sanctions (30+ sources) | Partial |
| **ADS-B Exchange** | Unfiltered flight tracking including military | Paid |

### Tier 2: Economic & Financial (7)

| Source | What It Tracks | Auth |
|--------|---------------|------|
| **FRED** | 22 key indicators: yield curve, CPI, VIX, fed funds, M2 | Free key |
| **US Treasury** | National debt, yields, fiscal data | None |
| **BLS** | CPI, unemployment, nonfarm payrolls, PPI | None |
| **EIA** | WTI/Brent crude, natural gas, inventories | Free key |
| **GSCPI** | NY Fed Global Supply Chain Pressure Index | None |
| **USAspending** | Federal spending and defense contracts | None |
| **UN Comtrade** | Strategic commodity trade flows between major powers | None |

### Tier 3: Weather, Environment, Tech, Social, SIGINT (7)

| Source | What It Tracks | Auth |
|--------|---------------|------|
| **NOAA/NWS** | Active US weather alerts | None |
| **EPA RadNet** | US government radiation monitoring | None |
| **USPTO Patents** | Patent filings in 7 strategic tech areas | None |
| **Bluesky** | Social sentiment on geopolitical/market topics | None |
| **Reddit** | Social sentiment from key subreddits | OAuth |
| **Telegram** | 17 curated OSINT/conflict/finance channels (web scraping, expandable via config) | None |
| **KiwiSDR** | Global HF radio receiver network (~600 receivers) | None |

### Tier 4: Space & Satellites (1)

| Source | What It Tracks | Auth |
|--------|---------------|------|
| **CelesTrak** | Satellite launches, ISS tracking, military constellations, Starlink/OneWeb counts | None |

### Tier 5: Live Market Data (1)

| Source | What It Tracks | Auth |
|--------|---------------|------|
| **Yahoo Finance** | Real-time prices: SPY, QQQ, BTC, Gold, WTI, VIX + 9 more | None |

---

## npm Scripts

| Script | Command | Description |
|--------|---------|-------------|
| `npm run dev` | `node --trace-warnings server.mjs` | Start dashboard with auto-refresh |
| `npm run sweep` | `node apis/briefing.mjs` | Run a single sweep, output JSON to stdout |
| `npm run inject` | `node dashboard/inject.mjs` | Inject latest data into static HTML |
| `npm run brief:save` | `node apis/save-briefing.mjs` | Run sweep + save timestamped JSON |
| `npm run diag` | `node diag.mjs` | Run diagnostics (Node version, imports, port check) |

---

## Configuration

All settings are in `.env` with sensible defaults:

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `3117` | Dashboard server port |
| `REFRESH_INTERVAL_MINUTES` | `15` | Auto-refresh interval |
| `LLM_PROVIDER` | disabled | `anthropic`, `openai`, `gemini`, `codex`, `openrouter`, `minimax`, `mistral`, or `grok` |
| `LLM_API_KEY` | — | API key (not needed for codex) |
| `LLM_MODEL` | per-provider default | Override model selection |
| `TELEGRAM_BOT_TOKEN` | disabled | For Telegram alerts + bot commands |
| `TELEGRAM_CHAT_ID` | — | Your Telegram chat ID |
| `TELEGRAM_CHANNELS` | — | Extra channel IDs to monitor (comma-separated) |
| `TELEGRAM_POLL_INTERVAL` | `5000` | Bot command polling interval (ms) |
| `DISCORD_BOT_TOKEN` | disabled | For Discord alerts + slash commands |
| `DISCORD_CHANNEL_ID` | — | Discord channel for alerts |
| `DISCORD_GUILD_ID` | — | Server ID (instant slash command registration) |
| `DISCORD_WEBHOOK_URL` | — | Webhook URL (alert-only fallback, no bot needed) |

Delta engine thresholds（系统对扫描间变化的敏感度）can be customized in `crucix.config.mjs` under the `delta.thresholds` section. The defaults are tuned to filter out noise while catching meaningful moves.

---

## API Endpoints

When running `npm run dev`:

| Endpoint | Description |
|----------|-------------|
| `GET /` | Jarvis HUD dashboard |
| `GET /api/data` | Current synthesized intelligence data (JSON) |
| `GET /api/health` | Server status, uptime, source count, LLM status |
| `GET /events` | SSE stream for live push updates |

---

## Troubleshooting

### `npm run dev` exits silently (no output, no error)

This is a known issue where npm's script runner can swallow errors, particularly on Windows PowerShell. Try these in order:

**1. Run Node directly (bypasses npm):**
```bash
node --trace-warnings server.mjs
```
This is functionally identical to `npm run dev` but gives you full error output.

**2. Run the diagnostic script:**
```bash
node diag.mjs
```
This tests every import one by one, checks your Node.js version, and verifies port 3117 is available. It will tell you exactly what's failing.

**3. Check if port 3117 is already in use:**

A previous Crucix instance may still be running in the background.

```powershell
# Windows PowerShell
netstat -ano | findstr 3117
taskkill /F /PID <the_PID_from_above>

# Or kill all Node processes
taskkill /F /IM node.exe
```

```bash
# macOS / Linux
lsof -ti:3117 | xargs kill
```

Then try starting again. You can also change the port by setting `PORT=3118` in your `.env` file.

**4. Check Node.js version:**
```bash
node --version
```
Crucix requires Node.js 22 or later. If you have an older version, download the latest LTS from [nodejs.org](https://nodejs.org/).

### Dashboard shows empty panels after first start

This is normal — the first sweep takes 30–60 seconds to query all 27 sources. The dashboard will populate automatically once the sweep completes. Check the terminal for sweep progress logs.

### Some sources show errors

Expected behavior. Sources that require API keys will return structured errors if the key isn't set. The rest of the sweep continues normally. Check the Source Integrity section in the dashboard (or the server logs) to see which sources failed and why. The 3 most impactful free keys to add are `FRED_API_KEY`, `FIRMS_MAP_KEY`, and `EIA_API_KEY`.

OpenSky can also return `HTTP 429` when its public hotspots are queried too aggressively. Crucix does not try to evade that limit. Instead, it surfaces the throttle/error in source health and preserves the most recent non-empty air traffic snapshot from `runs/` so the dashboard flight layer does not suddenly go blank on a throttled sweep.

### Telegram bot not responding to commands

Make sure both `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are set in `.env`. The bot only responds to messages from the configured chat ID (security measure). You should see `[Crucix] Telegram alerts enabled` and `[Crucix] Bot command polling started` in the server logs on startup. If not, double-check your token with `curl https://api.telegram.org/bot<YOUR_TOKEN>/getMe`.

### Discord bot not responding to slash commands

Check these in order:
1. Make sure `DISCORD_BOT_TOKEN` and `DISCORD_CHANNEL_ID` are set in `.env`
2. Verify `discord.js` is installed: `npm ls discord.js`. If missing, run `npm install discord.js`
3. If slash commands don't appear, set `DISCORD_GUILD_ID` — without it, global commands can take up to 1 hour to propagate. Guild-specific commands register instantly
4. Confirm the bot was invited with `bot` + `applications.commands` scopes and has `Send Messages` + `Embed Links` permissions in the target channel
5. Check server logs for `[Discord] Bot logged in as ...` on startup. If you see `[Discord] discord.js not installed`, install it and restart
6. **Webhook-only fallback:** If you just want alerts without slash commands, set `DISCORD_WEBHOOK_URL` instead of the bot token. No `discord.js` needed.

---

## Screenshots

The `docs/` folder contains dashboard screenshots referenced by this README:

| File | Description |
|------|-------------|
| `docs/dashboard.png` | Full dashboard — hero image at the top of this README |
| `docs/boot.png` | Cinematic boot sequence animation |
| `docs/map.png` | D3 world map with marker types and flight arcs |
| `docs/globe.png` | 3D WebGL globe view with atmosphere glow and markers |

To update them: run the dashboard, wait for a sweep to complete, then use your browser's DevTools (`F12` → `Ctrl+Shift+P` → "Capture full size screenshot") or a tool like [LICEcap](https://www.cockos.com/licecap/) for GIFs.

---

## Contributing

Found a bug? Want to add a 28th source? PRs welcome. Each source is a standalone module in `apis/sources/` — just export a `briefing()` function that returns structured data and add it to the orchestrator in `apis/briefing.mjs`.

If you find this useful, a star helps others find it too.

For contribution guidelines, review expectations, and source-add rules, see `CONTRIBUTING.md`. For security reports, see `SECURITY.md`.

## Contact

For partnerships, integrations, or other non-issue inquiries, 你可以通过 `celesthioailabs@gmail.com` 联系我。

For bugs and feature requests, please use GitHub Issues so discussion stays visible and actionable.

---

## Star History

<a href="https://www.star-history.com/?repos=calesthio%2FCrucix&type=date&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=calesthio/Crucix&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=calesthio/Crucix&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/image?repos=calesthio/Crucix&type=date&legend=top-left" />
  </picture>
</a>

---

## License

AGPL-3.0