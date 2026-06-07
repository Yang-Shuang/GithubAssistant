<p align="center">
  <img src="assets/valuecell.png" style="width: 100%; height: auto;">
</p>

<div align="center" style="line-height: 2;">
    <a href="https://www.python.org/downloads" target="_blank">
        <img src="https://img.shields.io/badge/python-3.12+-blue.svg"
            alt="Python version"></a>
    <a href="LICENSE" target="_blank">
        <img src="https://img.shields.io/badge/license-Apache2.0-red.svg"
            alt="License: Apache2.0"></a>  
    <br>
    <a href="https://discord.com/invite/84Kex3GGAh" target="_blank">
        <img src="https://img.shields.io/discord/1399603591471435907?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
    <a href="https://twitter.com/intent/follow?screen_name=valuecell" target="_blank">
        <img src="https://img.shields.io/twitter/follow/valuecell?logo=X&color=%20%23f5f5f5"
            alt="follow on X(Twitter)"></a>
    <a href="https://www.linkedin.com/company/valuecell/" target="_blank">
        <img src="https://custom-icon-badges.demolab.com/badge/LinkedIn-0A66C2?logo=linkedin-white&logoColor=fff"
            alt="follow on LinkedIn"></a>
    <a href="https://www.facebook.com/people/ValueCell/61581410516790/" target="_blank">
        <img src="https://custom-icon-badges.demolab.com/badge/Facebook-1877F2?logo=facebook-white&logoColor=fff"
            alt="follow on Facebook"></a>
    <a href="https://www.youtube.com/watch?v=C3tfHyGY9YE" target="_blank">
        <img src="https://img.shields.io/badge/Watch%20on-YouTube-red?logo=youtube"
            alt="Watch on YouTube"></a>
</div>

<div align="center">
  <a href="README.md" style="color: gray;">English</a>
  <a href="README.zh.md" style="color: auto;">中文（简体）</a>
  <a href="README.zh_Hant.md" style="color: auto;">中文（繁體）</a>
  <a href="README.ja.md" style="color: auto;">日本語</a>
</div>


# ValueCell

## 我们的产品已上线 🔥🔥🔥

 **ValueCell 现已提供 A 股深度研究、市场分析功能，无需部署——直接访问 [valuecell.ai](https://valuecell.ai) 即可体验。**

## 项目简介

ValueCell 是一个由社区驱动的金融应用多智能体（Agent）平台。我们的使命是打造全球最大的去中心化金融智能体社区。

它提供了一支顶尖的投资智能体团队，协助你进行选股、研究、跟踪乃至交易。

该系统将所有敏感信息存储在你的本地设备上，确保核心数据安全。

欢迎加入我们的 Discord 社区，分享你的反馈和遇到的问题，并邀请更多开发者共同贡献代码 🔥🔥🔥

>注意：ValueCell 团队成员绝不会主动联系社区参与者。本项目仅用于技术交流。投资有风险，入市需谨慎。⚠️

# 截图预览

[![Watch the video](https://img.youtube.com/vi/C3tfHyGY9YE/maxresdefault.jpg)](https://www.youtube.com/watch?v=C3tfHyGY9YE)


<p align="center">
  <img src="assets/product/AutoTradingAgent.png" style="width: 100%; height: auto;">
</p>

<p align="center">
  <img src="assets/product/Model_Configuration.png" style="width: 100%; height: auto;">
</p>


# 核心功能

<p align="center">
  <img src="assets/architecture.png" style="width: 100%; height: auto;">
</p>


## 多智能体系统（Multi-Agent System）
- **深度研究智能体（DeepResearch Agent）**：自动检索并分析基础文档，生成准确的数据洞察与可解释的摘要
- **策略智能体（Strategy Agent）**：支持多种加密货币资产及多策略智能交易，自动执行你的投资策略
- **新闻检索智能体（News Retrieval Agent）**：支持个性化定时新闻推送，实时跟踪关键信息
- **其他功能**：更多智能体正在规划中……

## 灵活的集成能力
- **支持多种大语言模型提供商（LLM）**：兼容 OpenRouter、SiliconFlow、Azure、类 OpenAI API、Google、OpenAI 和 DeepSeek
- **丰富的市场数据**：覆盖美股、加密货币、港股、A股等全球主流市场
- **兼容多智能体框架**：支持通过 LangChain 和基于 A2A 协议的 Agno 进行研发集成
- **交易所直连**：实时路由对接 OKX 与 Binance，内置风控护栏机制

# 快速上手

## 新用户指南

如需快速开始，请前往 GitHub 的 [Releases 页面](https://github.com/ValueCell-ai/valuecell/releases) 下载适用于 macOS 或 Windows 的最新 ValueCell 客户端。

安装完成后，首次使用 ValueCell 前请配置你偏好的模型提供商。具体操作请参考应用内指引或相关文档。

### 实盘交易（Live Trading）

- **配置 AI 模型**：通过 Web 界面添加你的 AI 模型 API Key
- **配置交易所**：设置 Binance / HyperLiquid / OKX / Coinbase 等平台的 API 凭证
- **创建策略**：结合 AI 模型与交易所接口，定制个性化交易策略
- **监控与控制**：启动或停止交易智能体，并实时监控表现
- **注意**：目前仅支持合约交易（现货已实现为 1倍杠杆合约），请确保你的合约账户余额充足

#### 支持的交易所

| 交易所 | 说明 | 状态 |
| --- | --- | --- |
| **Binance** | 仅支持国际版网站 [binance.com](binance.com)，不支持美国站。使用 USDT-M 永续合约（USDT 本位合约）。请确保期货账户有充足的 USDT 余额。交易对格式：`BTC/USDT`。注意：请确保持续性合约账户余额不为 0。申请 API 时，请在搜索引擎搜索 `My IP` 添加 IP 白名单 | ✅ 已测试 |
| **Hyperliquid** | 仅支持 USDC 作为保证金货币。采用主钱包地址 + API 钱包私钥进行身份验证（通过 [API 选项卡](https://app.hyperliquid.xyz/API) 申请）。市价单会自动转换为 IOC 限价单。交易对格式需手动调整为 `SYMBOL/USDC`（例如 `WIF/USDC`）。配置时需提供主钱包地址 + API 钱包私钥。单笔最低交易量为 10U | ✅ 已测试 |
| **OKX** | 需要 API Key、Secret 和 Passphrase（OKX 账户密码）进行身份验证。支持 USDT 本位合约。交易对格式：`BTC/USDT` | ✅ 已测试 |
| Coinbase | 支持 USDT 本位合约。暂不支持国际版（Coinbase International） | 🟡 部分测试 |
| Gate.io | 支持 USDT 本位合约。需提供 API Key 和 Secret | 🟡 部分测试 |
| MEXC | 支持 USDT 本位合约。需提供 API Key 和 Secret | 🟡 部分测试 |
| Blockchain | 支持 USDT 本位合约。需提供 API Key、Secret | 🟡 部分测试 |

**图例说明**：
- ✅ **已测试（Tested）**：已在生产环境中完成全面测试与验证
- 🟡 **部分测试（Partially Tested）**：代码实现已完成，但尚未完全测试，可能需要调试
- **推荐优先使用**：已全面测试的交易所（Binance、Hyperliquid、OKX）

### 注意事项
- 目前仅支持杠杆交易，请确保你的永续合约（Perps）账户余额充足。
- 请务必妥善保管你的 API 密钥，以免资金损失。应用会将密钥存储在你的本地设备上，不会通过互联网发送给任何第三方。
- 为保障账户安全，请定期重置你的 API 密钥。 

---

**注意**：运行应用前，请确保所有依赖项已安装且环境变量配置正确。如果距离上次更新已有较长时间，你可以删除本地数据存储并重新开始：
- LanceDB 目录（存储于系统应用目录，与 `.env` 路径相同）：
  - macOS: `~/Library/Application Support/ValueCell/lancedb`
  - Linux: `~/.config/valuecell/lancedb`
  - Windows: `%APPDATA%\\ValueCell\\lancedb`
- 知识库目录（存储于系统应用目录，与 `.env` 路径相同）：
  - macOS: `~/Library/Application Support/ValueCell/.knowledge`
  - Linux: `~/.config/valuecell/.knowledge`
  - Windows: `%APPDATA%\\ValueCell\\.knowledge`
- SQLite 数据库文件（存储于系统应用目录，与 `.env` 路径相同）：
  - macOS: `~/Library/Application Support/ValueCell/valuecell.db`
  - Linux: `~/.config/valuecell/valuecell.db`
  - Windows: `%APPDATA%\\ValueCell\\valuecell.db`


## 开发者指南

我们诚挚邀请所有开发者加入我们的 Discord 讨论组，我们将定期分享社区路线图及即将推出的贡献者福利计划。

详细的开发流程与规范如下：[CONTRIBUTING.md](.github/CONTRIBUTING.md)

ValueCell 是一款基于 Python 的应用程序，配备完整的 Web 界面，支持多平台部署。请按照以下配置快速上手。

## 克隆仓库

   ```bash
   git clone https://github.com/ValueCell-ai/valuecell.git
   cd valuecell
   ```

## 运行应用

启动完整的应用程序（包含前端、后端及智能体）：

### Linux / Macos
```bash
bash start.sh
```

### Windows (PowerShell)
```powershell
.\start.ps1
```

### 访问界面

- **Web 界面**：在浏览器中访问 [http://localhost:1420](http://localhost:1420)
- **日志（Logs）**：直接在终端查看应用日志，获取后端服务及各智能体的详细运行信息

### 后续步骤

应用启动后，你可以通过 Web 界面探索并体验 ValueCell 的各项功能与能力。

### 配置说明

更详细的配置信息请参阅 [CONFIGURATION_GUIDE](./docs/CONFIGURATION_GUIDE.md)

# 路线图

## 🤖 智能体能力增强
### 交易功能
- **加密货币**：支持 OKX、Binance 和 Hyperliquid 交易所，更多交易所正在规划接入中……
- **证券**：逐步支持 AI 证券交易

### 市场拓展
- **欧洲市场**：新增对富时指数（FTSE）、德意志交易所指数（DAX）、法国 CAC 40 及其他欧洲交易所的支持
- **亚洲市场**：扩展覆盖至日经指数及新兴亚洲市场
- **商品市场**：原油、黄金、白银、农产品分析
- **外汇市场**：主要货币对及交叉盘分析

### 资产多元化
- **固定收益**：国债、公司债及收益率分析智能体
- **衍生品**：期权、期货及复杂金融工具
- **另类投资**：私募股权、对冲基金与风险投资分析

### 高级通知与推送类型
- **实时警报**：价格波动、成交量激增及技术面突破提醒
- **定时报告**：每日/每周/每月投资组合总结
- **事件驱动通知**：财报发布、分红公告、监管政策变更提醒
- **自定义触发器**：用户定义的条件与阈值
- **多渠道推送**：集成 Discord 和 Webhook

## ⚙️ 产品配置与个性化
### 多平台支持
- **桌面端支持**：逐步完善桌面客户端功能与能力
- **数据库热更新**：逐步支持兼容性升级

### 国际化（i18n）
- **多语言支持**：英语、中文（简体/繁体）、日语、韩语、西班牙语、法语
- **本地化市场数据**：符合区域习惯的金融术语与格式
- **文化适配**：时区设置、日期格式及货币偏好
- **智能体人格本地化**：符合当地文化的沟通风格

### 令牌与身份验证管理
- **API Key 管理**：第三方 API Key 的安全存储与定期轮换机制
- **OAuth 集成**：支持主流金融数据提供商的 OAuth 认证

### 用户偏好与自定义设置
- **投资画像**：风险承受能力、投资期限及策略偏好配置
- **界面定制（UI/UX）**：深色/浅色模式、仪表盘布局及组件偏好设置
- **智能体行为**：沟通频率、分析深度与报告风格设定
- **投资组合管理**：自定义基准指数、绩效指标及资产配置目标

### 记忆与学习系统
- **对话历史**：跨会话持久化保存聊天记录
- **用户学习模型**：基于用户行为提供自适应推荐
- **市场记忆库**：保留历史上下文与模式识别能力
- **偏好演化机制**：随时间动态调整推荐策略

## 🔧 ValueCell SDK 开发
### 核心 SDK 功能
- **Python SDK**：提供全面的智能体集成与自定义库
- **WebSocket 支持**：实现实时数据流传输与双向通信

### 智能体集成框架
- **插件架构**：轻松接入第三方智能体与工具
- **智能体注册中心（Registry）**：社区贡献型智能体的应用市场

### 开发者工具与文档
- **交互式 API 浏览器**：提供 Swagger/OpenAPI 文档及在线测试功能
- **代码示例**：涵盖多种编程语言的参考实现
- **测试框架**：包含单元测试、集成测试及模拟数据生成器

# 许可证（LICENSE）

本项目采用 **Apache License 2.0** 开源协议——详情请参阅 [LICENSE](./LICENSE) 文件。

> 📌 注意：Apache 2.0 协议**仅适用于 ValueCell 团队及贡献者编写的原始代码**。第三方组件（如 API、小部件、库等）受其各自许可证和条款约束——详见下文。

## 第三方组件与许可说明

ValueCell 集成了外部服务并嵌入了第三方小部件。其使用**不受 Apache 2.0 协议覆盖**，作为用户或开发者，你有责任遵守其相关条款。

| 组件 | 类型 | 许可证/条款 |
|---------|------|-----------------|
| **TradingView 高级图表** | 嵌入式 iframe 小部件 | [免费高级图表协议](https://www.tradingview.com/chart-embedding/)（专有） |
| **交易所 API**（Binance、OKX、Hyperliquid 等） | REST / WebSocket 接口 | 各交易所的服务条款（ToS），例如 [Binance API 条款](https://www.binance.com/en/terms) |
| **大语言模型提供商（LLM）**（OpenAI、Azure、Google、DeepSeek 等） | 推理 API | 各提供商专属服务条款（ToS），例如 [OpenAI 使用条款](https://openai.com/policies/terms-of-use) |

# Star 历史

<div align="center">
<a href="https://www.star-history.com/#ValueCell-ai/valuecell&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ValueCell-ai/valuecell&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ValueCell-ai/valuecell&type=Date" />
   <img alt="TradingAgents Star History" src="https://api.star-history.com/svg?repos=ValueCell-ai/valuecell&type=Date" style="width: 80%; height: auto;" />
 </picture>
</a>
</div>

<div align="center">