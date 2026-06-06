[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

> [!IMPORTANT]
> 阅读 [2025年MCP现状报告](https://glama.ai/blog/2025-12-07-the-state-of-mcp-in-2025)。

> [!IMPORTANT]
> [Awesome MCP Servers](https://glama.ai/mcp/servers) 在线目录。

一份精心整理的优秀模型上下文协议（Model Context Protocol, MCP）服务器列表。

* [什么是 MCP？](#what-is-mcp)
* [客户端](#clients)
* [教程](#tutorials)
* [社区](#community)
* [标识说明](#legend)
* [服务器实现](#server-implementations)
* [框架](#frameworks)
* [技巧与提示](#tips-and-tricks)

## 什么是 MCP？

[MCP](https://modelcontextprotocol.io/) 是一个开放协议，通过标准化的服务器实现，使 AI 模型能够安全地与本地及远程资源进行交互。本列表侧重于生产就绪型和实验性的 MCP 服务器，它们通过文件访问、数据库连接、API 集成及其他上下文服务来扩展 AI 能力。

## 客户端

查看 [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) 和 [glama.ai/mcp/clients](https://glama.ai/mcp/clients)。

## 教程

* [模型上下文协议（MCP）快速入门](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [配置 Claude Desktop 应用以使用 SQLite 数据库](https://youtu.be/wxCCzo9dGj0)

## 社区

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord 服务器](https://glama.ai/mcp/discord)

## 标识说明

* 🎖️ – 官方实现
* 编程语言
  * 🐍 – Python 代码库
  * 📇 – TypeScript（或 JavaScript）代码库
  * 🏎️ – Go 代码库
  * 🦀 – Rust 代码库
  * #️⃣ - C# 代码库
  * ☕ - Java 代码库
  * 🌊 – C/C++ 代码库
  * 💎 - Ruby 代码库

* 作用范围
  * ☁️ - 云服务
  * 🏠 - 本地服务
  * 📟 - 嵌入式系统
* 操作系统
  * 🍎 – macOS
  * 🪟 – Windows
  * 🐧 - Linux

> [!NOTE]
> 混淆了本地（🏠）与云端（☁️）？
> * 当 MCP 服务器与**本地安装的软件**通信时使用本地图标，例如控制 Chrome 浏览器。
> * 当 MCP 服务器与**远程 API** 通信时使用云端图标，例如天气 API。

## 服务器实现

> [!NOTE]
> 我们现在有一个[在线目录](https://glama.ai/mcp/servers)，已与仓库同步。

* 🔗 - [聚合器](#aggregators)
* 🎨 - [艺术与文化](#art-and-culture)
* 📐 - [架构与设计](#architecture-and-design)
* 📂 - [浏览器自动化](#browser-automation)
* 🧬 - [生物医学与生物信息学](#bio)
* ☁️ - [云平台](#cloud-platforms)
* 👨‍💻 - [代码执行](#code-execution)
* 🤖 - [编码智能体](#coding-agents)
* 🖥️ - [命令行](#command-line)
* 💬 - [通信协作](#communication)
* 🗣️ - [对话式 AI](#conversational-ai)
* 👤 - [客户数据平台](#customer-data-platforms)
* 🗄️ - [数据库](#databases)
* 📊 - [数据平台](#data-platforms)
* 🚚 - [物流配送](#delivery)
* 🛠️ - [开发者工具](#developer-tools)
* 🧮 - [数据科学工具](#data-science-tools)
* 📊 - [数据可视化](#data-visualization)
* 📟 - [嵌入式系统](#embedded-system)
* 🎓 - [教育](#education)
* 🛒 - [电子商务](#e-commerce)
* 🌳 - [环境与自然](#environment-and-nature)
* 📂 - [文件系统](#file-systems)
* 💰 - [金融与金融科技](#finance--fintech)
* 🎮 - [游戏](#gaming)
* 🏠 - [智能家居自动化](#home-automation)
* 🧠 - [知识与记忆](#knowledge--memory)
* ⚖️ - [法律合规](#legal)
* 🗺️ - [位置服务](#location-services)
* 🎯 - [营销推广](#marketing)
* 📊 - [监控运维](#monitoring)
* 🎥 - [多媒体处理](#multimedia-process)
* 🖥️ - [操作系统自动化](#os-automation)
* 📋 - [产品管理](#product-management)
* 🏠 - [房地产](#real-estate)
* 🔬 - [科研探索](#research)
* 🔎 - [搜索与数据提取](#search)
* 🔒 - [安全合规](#security)
* 🌐 - [社交媒体](#social-media)
* 🏃 - [体育健康](#sports)
* 🎧 - [客服与服务管理](#support-and-service-management)
* 🌎 - [翻译服务](#translation-services)
* 🎧 - [文本转语音](#text-to-speech)
* 🚆 - [旅行与交通](#travel-and-transportation)
* 🔄 - [版本控制](#version-control)
* 🏢 - [职场与生产力](#workplace-and-productivity)
* 🛠️ - [其他工具与集成](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>聚合器

通过单个 MCP 服务器访问多种应用和工具的服务端。

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - 一个统一的模型上下文协议服务器实现，将多个 MCP 服务器聚合为一个。
- [8randonpickart5/alderpost-mcp](https://github.com/8randonpickart5/alderpost-mcp) [![alderpost-mcp MCP server](https://glama.ai/mcp/servers/8randonpickart5/alderpost-mcp/badges/score.svg)](https://glama.ai/mcp/servers/8randonpickart5/alderpost-mcp) 📇 ☁️ - 通过 Base 上的 x402 微支付提供 8 个集成智能端点（安全、企业、威胁、合规、销售、体育、房产、健康）。
- [tadas-github/a2asearch-mcp](https://github.com/tadas-github/a2asearch-mcp) [![tadas-github/a2asearch-mcp MCP server](https://glama.ai/mcp/servers/tadas-github/a2asearch-mcp/badges/score.svg)](https://glama.ai/mcp/servers/tadas-github/a2asearch-mcp) 📇 ☁️ - 用于搜索 4,800+ MCP 服务器、AI 智能体、CLI 工具和智能体技能的 MCP 服务端。安装：`npx -y a2asearch-mcp`。询问 Claude：“查找数据库访问的 MCP 服务器”。免费，无需认证。
- [Aganium/agenium](https://github.com/Aganium/agenium) 📇 ☁️ 🍎 🪟 🐧 - 将任意 MCP 服务器桥接到 agent:// 网络 —— 为 AI 智能体提供类似 DNS 的身份、发现与信任机制。使你的工具可通过 `agent://` URI 被发现和调用，支持 mTLS、信任评分和能力搜索。
- [elisymlabs/elisym](https://github.com/elisymlabs/elisym) [![elisymlabs/elisym MCP server](https://glama.ai/mcp/servers/elisymlabs/elisym/badges/score.svg)](https://glama.ai/mcp/servers/elisymlabs/elisym) 📇 ☁️ 🍎 🪟 🐧 - 基于 Nostr 和 Solana 支付（SOL, USDC）的 AI 智能体发现与交易市场。支持 NIP-89 发现、NIP-90 任务、NIP-44 v2 加密及链上微支付。
- [espadaw/Agent47](https://github.com/espadaw/Agent47) 📇 ☁️ - 面向 AI 智能体的统一工作聚合器，覆盖 9+ 平台（x402, RentAHuman, Virtuals 等）。
- [doggychip/agentforge](https://github.com/doggychip/agentforge) [![doggychip/agentforge MCP server](https://glama.ai/mcp/servers/doggychip/agentforge/badges/score.svg)](https://glama.ai/mcp/servers/doggychip/agentforge) 📇 ☁️ - 面向 300+ AI 智能体的统一 API 网关与交易市场。提供单一 API Key、REST + 流式传输、90% 创作者收益分成及健康监控。支持自托管（MIT）。
- [AgentHotspot](https://github.com/AgentHotspot/agenthotspot-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - 在 AgentHotspot MCP 市场中搜索、集成并变现 MCP 连接器
- [alexanderclapp/clirank-mcp-server](https://github.com/alexanderclapp/clirank-mcp-server) [![alexanderclapp/clirank-mcp-server MCP server](https://glama.ai/mcp/servers/alexanderclapp/clirank-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/alexanderclapp/clirank-mcp-server) 📇 ☁️ 🍎 🪟 🐧 - 面向 AI 编码智能体的 API 情报。对 387 个 API 进行友好度评分，提供推荐、对比、分数查询及发现工具。安装：`npx clirank-mcp-server`。官网：[clirank.dev](https://clirank.dev)。
- [Work90210/APIFold](https://github.com/Work90210/APIFold) [![Work90210/APIFold MCP server](https://glama.ai/mcp/servers/Work90210/APIFold/badges/score.svg)](https://glama.ai/mcp/servers/Work90210/APIFold) 📇 ☁️ - 将任意 REST API 转换为托管的 MCP 服务端。提供 18 个免费公共服务器（GitHub, Stripe, Slack, OpenAI, Notion 等）—— 无需配置，自带 API Key 即可使用。
- [rhein1/agoragentic-integrations](https://github.com/rhein1/agoragentic-integrations) [![agoragentic-integrations MCP server](https://glama.ai/mcp/servers/@rhein1/agoragentic-integrations/badges/score.svg)](https://glama.ai/mcp/servers/@rhein1/agoragentic-integrations) 📇 ☁️ - 智能体间交易市场，AI 智能体使用 Base L2 上的 USDC 发现、调用并购买其他智能体的服务。
- [arikusi/deepseek-mcp-server](https://github.com/arikusi/deepseek-mcp-server) [![deepseek-mcp-server MCP server](https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server) 📇 ☁️ 🍎 🪟 🐧 - 面向 DeepSeek AI 的 MCP 服务端，支持对话、推理、多轮会话、函数调用、思维模式及成本追踪。
- [ariekogan/ateam-mcp](https://github.com/ariekogan/ateam-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - 在 ADAS 平台上构建、验证并部署多智能体 AI 解决方案。使用工具设计技能，管理解决方案生命周期，并通过 stdio 或 HTTP 从任何 AI 环境连接。
- [askbudi/roundtable](https://github.com/askbudi/roundtable) 📇 ☁️ 🏠 🍎 🪟 🐧 - Meta-MCP 服务端，通过智能自动发现和标准化 MCP 接口统一多个 AI 编码助手（Codex, Claude Code, Cursor, Gemini），提供零配置访问整个 AI 编码生态系统的能力。
- [blockrunai/blockrun-mcp](https://github.com/blockrunai/blockrun-mcp) 📇 ☁️ 🍎 🪟 🐧 - 无需 API Key 即可访问 30+ AI 模型（GPT-5, Claude, Gemini, Grok, DeepSeek）。通过 Base 上的 x402 USDC 微支付按量付费。
- [Data-Everything/mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates) 📇 🏠 🍎 🪟 🐧 - 一个服务端，所有工具。统一的 MCP 平台将众多应用、工具和后端服务连接在一个强大的接口下——非常适合本地开发者或生产级智能体。
- [depwire/depwire](https://github.com/depwire/depwire) [![depwire/depwire MCP server](https://glama.ai/mcp/servers/depwire/depwire/badges/score.svg)](https://glama.ai/mcp/servers/depwire/depwire) 📇 🐍 🏎️ 🦀 🌊 🏠 - 依赖图 + 15 个 MCP 工具，专为 AI 编码助手设计。解析 TypeScript, JavaScript, Python, Go, Rust 和 C。提供弧状图可视化、健康评分、死代码检测和时序图。
- [duaraghav8/MCPJungle](https://github.com/duaraghav8/MCPJungle) 🏎️ 🏠 - 面向企业 AI 智能体的自托管 MCP 服务端注册中心
- [edgarriba/prolink](https://github.com/edgarriba/prolink) 🐍 ☁️ 🏠 🍎 🪟 🐧 - 智能体间中间件市场 —— 支持 MCP 原生的发现、协商及 AI 智能体间的交易
- [entire-vc/evc-spark-mcp](https://github.com/entire-vc/evc-spark-mcp) [![evc-spark-mcp MCP server](https://glama.ai/mcp/servers/entire-vc/evc-spark-mcp/badges/score.svg)](https://glama.ai/mcp/servers/entire-vc/evc-spark-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - 从精选的 4500+ 资产目录中搜索和发现 AI 智能体、技能、提示词、包及 MCP 连接器。
- [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - 一个 MCP 服务器列表，让你可以询问客户端哪些服务器可用于优化你的日常工作流。
- [gpu-bridge/mcp-server](https://github.com/gpu-bridge/mcp-server) [![gpu-bridge-mcp-server MCP server](https://glama.ai/mcp/servers/gpu-bridge/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/gpu-bridge/mcp-server) 📇 ☁️ 🍎 🪟 🐧 - 统一的 GPU 推理 API，包含 30 项 AI 服务（LLM, 图像生成, 视频, TTS, whisper, 嵌入, 重排序, OCR）作为 MCP 工具。通过 x402 USDC 或 API Key 积分按量付费。
- [carlosahumada89/govrider-mcp-server](https://github.com/carlosahumada89/govrider-mcp-server) [![@carlosahumada89-govrider-mcp-server MCP server](https://glama.ai/mcp/servers/@carlosahumada89-govrider-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/@carlosahumada89-govrider-mcp-server) ☁️  📇 - 将你的技术产品或咨询服务与全球 25+ 官方来源的数千个政府招标、RFP、拨款和框架进行匹配。
- [gzoonet/cortex](https://github.com/gzoonet/cortex) [![gzoo-cortex MCP server](https://glama.ai/mcp/servers/@gzoonet/gzoo-cortex/badges/score.svg)](https://glama.ai/mcp/servers/@gzoonet/gzoo-cortex) 📇 🏠 - 面向开发者的本地优先知识图谱。监控项目文件，通过 LLMs 提取实体和关系，构建带 Web 仪表板和 CLI 的可查询知识图谱。提供 4 个 MCP 工具：get_status, list_projects, find_entity, query_cortex。
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - 通过 MCP 使用 Google Imagen 3.0 API 的强大图像生成工具。支持文本提示生成高质量图像，提供高级摄影、艺术和照片级真实控制。
- [hashgraph-online/hashnet-mcp-js](https://github.com/hashgraph-online/hashnet-mcp-js) 📇 ☁️ 🍎 🪟 🐧 - 注册中心代理的 MCP 服务端。在 Hashgraph 网络上发现、注册并与 AI 智能体聊天。
- [isaac-levine/forage](https://github.com/isaac-levine/forage) 📇 🏠 🍎 🪟 🐧 - AI 智能体的自改进工具发现系统。搜索注册表，将 MCP 服务端作为子进程安装，并在会话间持久化工具知识 —— 无需重启。
- [jaspertvdm/mcp-server-gemini-bridge](https://github.com/jaspertvdm/mcp-server-gemini-bridge) 🐍 ☁️ - Google Gemini API 桥接器。通过 MCP 访问 Gemini Pro 和 Flash 模型。
- [jaspertvdm/mcp-server-ollama-bridge](https://github.com/jaspertvdm/mcp-server-ollama-bridge) 🐍 🏠 - 本地 Ollama LLM 服务端桥接器。通过 MCP 运行 Llama, Mistral, Qwen 等本地模型。
- [jaspertvdm/mcp-server-openai-bridge](https://github.com/jaspertvdm/mcp-server-openai-bridge) 🐍 ☁️ - OpenAI API 桥接器。通过 MCP 访问 GPT-4, GPT-4o 等 OpenAI 模型。
- [Jovancoding/Network-AI](https://github.com/Jovancoding/Network-AI) [![network](https://glama.ai/mcp/servers/Jovancoding/network-ai/badges/score.svg)](https://glama.ai/mcp/servers/Jovancoding/network-ai) 📇 🏠 🍎 🪟 🐧 - 支持竞态安全共享黑板的多智能体编排 MCP 服务端。20+ MCP 工具：黑板读写、智能体生成/停止、FSM 转换、预算追踪、令牌管理及审计日志查询。`npx network-ai-server --port 3001`。
- [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - 使用一个二进制文件通过 SQL 查询 40+ 应用。支持连接 PostgreSQL, MySQL 或 SQLite 兼容数据库。本地优先，隐私设计。
- [juspay/neurolink](https://github.com/juspay/neurolink) 📇 ☁️ 🏠 🍎 🪟 🐧 - 使企业 AI 基础设施普适化访问。边缘优先平台统一 12 个提供商和 100+ 模型，支持多智能体编排、HITL 工作流、护栏中间件及上下文摘要。
- [codeislaw101/katzilla](https://github.com/codeislaw101/katzilla) [![codeislaw101/katzilla MCP server](https://glama.ai/mcp/servers/codeislaw101/katzilla/badges/score.svg)](https://glama.ai/mcp/servers/codeislaw101/katzilla) 📇 ☁️ 🍎 🪟 🐧 - 面向 AI 智能体的统一数据 API —— 300+ 免费、公开及政府数据源汇聚于单一 API Key。覆盖经济（FRED, BLS）、环境（EPA, NOAA）、健康（CDC, FDA）、天气（NWS）、金融（SEC, CFPB）、科学（NASA, arXiv）等 30+ 类别。安装：`npx @katzilla/mcp`。
- [K-Dense-AI/claude-skills-mcp](https://github.com/K-Dense-AI/claude-skips-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - 智能搜索能力，让每个模型和客户端像原生一样使用 [Claude Agent Skills](https://www.anthropic.com/news/skills)。
- [khalidsaidi/ragmap](https://github.com/khalidsaidi/ragmap) 📇 ☁️ 🏠 🍎 🪟 🐧 - MapRag：专注于 RAG 的子注册中心 + MCP 服务端，使用结构化约束和可解释排序来发现并路由至具备检索能力的 MCP 服务器。
- [malamutemayhem/unclick-agent-native-endpoints](https://github.com/malamutemayhem/unclick-agent-native-endpoints) [![malamutemayhem/unclick-agent-native-endpoints MCP server](https://glama.ai/mcp/servers/malamutemayhem/unclick-agent-native-endpoints/badges/score.svg)](https://glama.ai/mcp/servers/malamutemayhem/unclick-agent-native-endpoints) 📇 🏠 🍎 🪟 🐧 - 110+ 工具覆盖社交媒体、金融、游戏、音乐、AU 特定服务及实用程序。零配置本地工具加平台连接器。`npx @unclick/mcp-server`
- [Markgatcha/universal-mcp-toolkit](https://github.com/Markgatcha/universal-mcp-toolkit) [![Markgatcha/universal-mcp-toolkit MCP server](https://glama.ai/mcp/servers/Markgatcha/universal-mcp-toolkit/badges/score.svg)](https://glama.ai/mcp/servers/Markgatcha/universal-mcp-toolkit) 📇 ☁️ 🏠 🍎 🪟 🐧 - 通用 MCP 聚合工具包，通过单一统一配置将 AI 智能体连接到多个 MCP 服务端。提供现成模板、跨仓库提示词工作流及零配置安装的 npm 包。
- [MastadoonPrime/sylex-search](https://github.com/MastadoonPrime/sylex-search) [![MastadoonPrime/sylex-search MCP server](https://glama.ai/mcp/servers/MastadoonPrime/sylex-search/badges/score.svg)](https://glama.ai/mcp/servers/MastadoonPrime/sylex-search) 🐍 📇 ☁️ 🍎 🪟 🐧 - AI 智能体的通用搜索引擎。跨所有类别发现产品、服务和业务。10 个 MCP 工具，零 LLM 调用，毫秒级响应。`npx sylex-search`
- [merterbak/Grok-MCP](https://github.com/merterbak/Grok-MCP) 🐍 ☁️ 🍎 🪟 🐧 - xAI 的 [Grok API](https://docs.x.ai/docs/overview) MCP 服务端，支持智能体工具调用、图像生成、视觉及文件支持。
- [metatool-ai/metatool-app](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP 是唯一的统一中间件 MCP 服务端，通过 GUI 管理你的 MCP 连接。
- [MikkoParkkola/mcp-gateway](https://github.com/MikkoParkkola/mcp-gateway) [![MikkoParkkola/mcp-gateway MCP server](https://glama.ai/mcp/servers/MikkoParkkola/mcp-gateway/badges/score.svg)](https://glama.ai/mcp/servers/MikkoParkkola/mcp-gateway) 🏎️ 🏠 🍎 🪟 🐧 - 支持单端口复用和 Meta-MCP 的通用 MCP 网关。4 个元工具替代 100+ 注册，节省 95% 上下文窗口。支持热重载能力、OpenAPI 自动导入及 42 个启动能力（25 个零配置）。
- [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) - 通过 [MindsDB 作为单一 MCP 服务端](https://docs.mindsdb.com/mcp/overview) 连接并统一跨各种平台和数据库的数据。
- [opentabs-dev/opentabs](https://github.com/opentabs-dev/opentabs) [![opentabs-dev/opentabs MCP server](https://glama.ai/mcp/servers/opentabs-dev/opentabs/badges/score.svg)](https://glama.ai/mcp/servers/opentabs-dev/opentabs) 📇 🏠 🍎 🪟 🐧 - 基于插件的 MCP 服务端 + Chrome 扩展，使 AI 智能体能够通过用户已认证的浏览器会话访问 Web 应用。提供 100+ 插件及用于构建新插件的 SDK。
- [oxgeneral/agentnet](https://github.com/oxgeneral/agentnet) 🐍 ☁️ 🍎 🪟 🐧 - 智能体间推荐网络，AI 智能体相互发现、推荐并引导用户。支持双边信任模型、信用经济体系及 7 个 MCP 工具用于注册、发现和推荐追踪。
- [particlefuture/MCPDiscovery](https://github.com/particlefuture/1mcpserver) 🐍 ☁️ 🏠 🍎 🪟 - MCP 的 MCP。自动发现并配置本地机器上的 MCP 服务端。 
- [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - 通过 8,000+ 预构建工具连接 2,500 个 API，并在你自己的应用中管理用户服务端。
- [portel-dev/ncp](https://github.com/portel-dev/ncp) 📇 ☁️ 🏠 🍎 🪟 🐧 - NCP 通过智能发现编排你的整个 MCP 生态系统，在保持 98.2% 准确率的同时消除令牌开销。
- [profullstack/mcp-server](https://github.com/profullstack/mcp-server) 📇 ☁️ 🏠 🍎 🪟 🐧 - 综合性 MCP 服务端，聚合 20+ 工具包括 SEO 优化、文档转换、域名查询、邮箱验证、二维码生成、天气数据、社交媒体发布、安全扫描等开发者实用工具。
- [RipperMercs/tensorfeed](https://github.com/RipperMercs/tensorfeed/tree/main/mcp-server) [![RipperMercs/tensorfeed MCP server](https://glama.ai/mcp/servers/RipperMercs/tensorfeed/badges/score.svg)](https://glama.ai/mcp/servers/RipperMercs/tensorfeed) 📇 ☁️ - 实时 AI 行业情报 MCP 服务端。6 个免费工具（AI 新闻、服务状态、模型定价、今日摘要、智能体活动、MCP 注册表快照）和 13 个付费高级工具（路由推荐、新闻搜索、历史系列、成本预测、提供商深度分析、模型对比、智能体目录、新功能简报、MCP 注册表系列、带每日/每周摘要的 Webhook 监控）。Base 主网 USDC 按次付费，无需账户。`npx -y @tensorfeed/mcp-server`
- [robhunter/agentdeals](https://github.com/robhunter/agentdeals) [![robhunter/agentdeals MCP server](https://glama.ai/mcp/servers/robhunter/agentdeals/badges/score.svg)](https://glama.ai/mcp/servers/robhunter/agentdeals) 📇 ☁️ - 覆盖 54 个类别的 1,500+ 开发者基础设施交易、免费层级和初创计划。搜索交易、对比供应商、规划技术栈并追踪价格变化。REST API 及 Web 浏览器访问 [agentdeals.dev](https://agentdeals.dev)。
- [rupinder2/mcp-orchestrator](https://github.com/rupinder2/mcp-orchestrator) 🐍 🏠 🍎 🪟🩷 🐧 - 中央枢纽，聚合多个 MCP 服务端的工具，提供统一的 BM25/正则搜索及延迟加载。
- [supertrained/rhumb](https://github.com/supertrained/rhumb) [![supertrained/rhumb MCP server](https://glama.ai/mcp/servers/supertrained/rhumb/badges/score.svg)](https://glama.ai/mcp/servers/supertrained/rhumb) 📇 ☁️ 🍎 🪟 🐧 - 覆盖 1,000+ 评分服务的智能体原生工具情报。21 个 MCP 工具：发现服务、检查 AN 分数、对比替代品、将能力解析为排名提供商、通过 3 种凭证模式（托管、BYOK、智能体金库）执行、带收据追踪成本及检查故障模式。支持通过 x402 微支付零注册选项。
- [sitbon/magg](https://github.com/sitbon/magg) 🍎 🪟 🐧 ☁️ 🏠 🐍 - Magg：一个 Meta-MCP 服务端，充当通用枢纽，使 LLMs 能够自主发现、安装并编排多个 MCP 服务端 —— 本质上赋予 AI 助手按需扩展自身能力的能力。
- [smart-mcp-proxy/mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go) [![smart-mcp-proxy/mcpproxy-go MCP server](https://glama.ai/mcp/servers/smart-mcp-proxy/mcpproxy-go/badges/score.svg)](https://glama.ai/mcp/servers/smart-mcp-proxy/mcpproxy-go) 🏎️ 🏠 🍎 🪟 🐧 - 本地 MCP 代理，支持 BM25 工具过滤、隔离安全沙箱、活动日志记录及 Web UI。通过单一端点路由多个服务端。
- [sonnyflylock/voxie-ai-directory-mcp](https://github.com/sonnyflylock/voxie-ai-directory-mcp) 📇 ☁️ - AI 电话号码目录，提供通过网页聊天访问 AI 服务的入口。查询 Voxie AI 角色和第三方服务（如 ChatGPT），提供免费互动的即时网页聊天 URL。
- [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) 📇 ☁️ - OpenAI GPT 图像生成/编辑 MCP 服务端。
- [sxhxliang/mcp-access-point](https://github.com/sxhxliang/mcp-access-point) 📇 ☁️ 🏠 🍎 🪟 🐧 - 一键将 Web 服务转换为 MCP 服务端，无需任何代码修改。
- [TheLunarCompany/lunar#mcpx](https://github.com/TheLunarCompany/lunar/tree/main/mcpx) 📇 🏠  ☁️ 🍎 🪟 🐧 - MCPX 是一个生产就绪、开源的网关，用于大规模管理 MCP 服务端 —— 集中工具发现、访问控制、调用优先级和用量追踪，简化智能体工作流。
- [thinkchainai/mcpbundles](https://github.com/thinkchainai/mcpbundles) - MCP Bundles：创建自定义的工具包并通过 OAuth 或 API Key 连接提供商。通过一个 MCP 服务端使用数千个集成，支持编程工具调用及用于管理捆绑包和凭证的 MCP UI。
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - 将多个 MCP 服务端组合为统一端点的代理工具。通过跨多个 MCP 服务端的请求负载均衡来扩展 AI 工具，类似于 Nginx 对 Web 服务器的作用。
- [toadlyBroodle/satring](https://github.com/toadlyBroodle/satring/tree/main/mcp) [![toadlyBroodle/satring MCP server](https://glama.ai/mcp/servers/toadlyBroodle/satring/badges/score.svg)](https://glama.ai/mcp/servers/toadlyBroodle/satring) 🐍 ☁️ 🍎 🪟 🐧 - 发现和对比 satring.com 的 L402 + x402 付费 API 服务，这是最佳精选的 Lightning 和 USDC API 目录。
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy)  📇 🏠 - 综合性代理服务端，将多个 MCP 服务端结合为单一界面并提供广泛的可视化功能。提供跨服务端的工具、提示词、资源和模板的发现与管理，以及构建 MCP 服务端时的调试沙盒。
- [ViperJuice/mcp-gateway](https://github.com/ViperJuice/mcp-gateway) 🐍 🏠 🍎 🪟 🐧 - 针对最小化 Claude Code 工具膨胀的元服务端，支持渐进式披露和动态服务端配置。暴露 9 个稳定元工具，自动启动 Playwright 和 Context7，并可从精选清单按需动态配置 25+ MCP 服务端。
- [WayStation-ai/mcp](https://github.com/waystation-ai/mcp) ☁️ 🍎 🪟 - 无缝且安全地将 Claude Desktop 及其他 MCP 主机连接到你喜爱的应用（Notion, Slack, Monday, Airtable 等）。耗时不到 90 秒。
- [wegotdocs/open-mcp](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - 10 秒内将 Web API 转换为 MCP 服务端并添加到开源注册表：https://open-mcp.org
- [whiteknightonhorse/APIbase](https://github.com/whiteknightonhorse/APIbase) [![APIbase MCP server](https://glama.ai/mcp/servers/whiteknightonhorse/APIbase/badges/score.svg)](https://glama.ai/mcp/servers/whiteknightonhorse/APIbase) 📇 ☁️ - 面向 AI 智能体的统一 API 枢纽，覆盖旅行（Amadeus, Sabre）、预测市场（Polymarket）、加密货币和天气的 56+ 工具。通过 Base 上的 USDC x402 微支付按次付费。
- [rplryan/x402-discovery-mcp](https://github.com/rplryan/x402-discovery-mcp) [![x402-discovery-mcp MCP server](https://glama.ai/mcp/servers/@rplryan/x402-discovery-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@rplryan/x402-discovery-mcp) 🐍 ☁️ - 面向 x402 可支付 API 的运行时发现层。智能体按能力发现和路由至按次付费的 x402 端点，获取带信任评分（0-100）的质量排名结果，并通过 x402 按查询付费。包含 MCP 服务端、Python SDK 及 CLI (`npm install -g x402scout`)。
- [x402-index/x402search-mcp](https://github.com/x402-index/x402search-mcp) [![x402-index/x402search-mcp MCP server](https://glama.ai/mcp/servers/x402-index/x402search-mcp/badges/score.svg)](https://glama.ai/mcp/servers/x402-index/x402search-mcp) 📇 ☁️ 🍎 🪟 🐧 - 按关键词搜索 14,000+ x402 支持的 HTTP API。智能体通过 Base 主网上的 x402 微支付每次搜索支付 $0.01 USDC —— 无需 API Key。索引规模大于任何其他 x402 发现层。
- [ikoskela/wisepanel-mcp](https://github.com/ikoskela/wisepanel-mcp) [![ikoskela/wisepanel-mcp MCP server](https://glama.ai/mcp/servers/ikoskela/wisepanel-mcp/badges/score.svg)](https://glama.ai/mcp/servers/ikoskela/wisepanel-mcp) 📇 ☁️ 🍎 🪟 🐧 - 支持发散上下文增强的多智能体辩论。动态生成角色以围绕问题空间展开，最大化 ChatGPT, Claude, Gemini 和 Perplexity 之间的发散对话。
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - 综合性个人数据聚合 MCP 服务端，集成 Steam, YouTube, Bilibili, Spotify, Reddit 等平台。支持 OAuth2 认证、自动令牌管理及 90+ 工具用于游戏、音乐、视频和社交平台数据访问。

### 🚀 <a name="aerospace-and-astrodynamics"></a>航空航天与轨道动力学

- [gregario/astronomy-oracle](https://github.com/gregario/astronomy-oracle) [![astronomy-oracle MCP server](https://glama.ai/mcp/servers/gregario/astronomy-oracle/badges/score.svg)](https://glama.ai/mcp/servers/gregario/astronomy-oracle) 📇 🏠 🍎 🪟 🐧 - 精确的天文学目录数据和观测会话规划器。包含 OpenNGC 的 13,000+ 深空天体，支持确定性可见性、升/中天/落及高度/方位角计算。`npx astronomy-oracle`
- [IO-Aerospace-software-community/mcp-server](https://github.com/IO-Aerospace-software-engineering/mcp-server) #️⃣ ☁️/🏠 🐧 - IO 航空航天 MCP 服务端：基于 .NET 的 MCP 服务端，用于航空航天与轨道动力学 —— 星历、轨道转换、DSS 工具、时间转换及单位/数学实用程序。支持 STDIO 和 SSE 传输；文档化 Docker 和本机 .NET 部署。

### 🎨 <a name="art-and-culture"></a>艺术与文化

访问并探索艺术收藏、文化遗产和博物馆数据库。使 AI 模型能够搜索和分析艺术与文化内容。
- [AceDataCloud/MCPFlux](https://github.com/AceDataCloud/FluxMCP) [![AceDataCloud/MCPFlux MCP server](https://glama.ai/mcp/servers/AceDataCloud/MCPFlux/badges/score.svg)](https://glama.ai/mcp/servers/AceDataCloud/MCPFlux) 🐍 ☁️ - 通过 Ace Data Cloud API 提供 Flux AI 图像生成与编辑（Black Forest Labs）。

- [AceDataCloud/MCPNanoBanana](https://github.com/AceDataCloud/MCPNanoBanana) [![AceDataCloud/MCPNanoBanana MCP server](https://glama.ai/mcp/servers/AceDataCloud/MCPNanoBanana/badges/score.svg)](https://glama.ai/mcp/servers/AceDataCloud/MCPNanoBanana) 🐍 ☁️ - NanoBanana AI 图像生成与编辑，支持虚拟试穿和真实场景中的商品放置。
- [AceDataCloud/MCPSeedream](https://github.com/AceDataCloud/SeedreamMCP) [![AceDataCloud/MCPSeedream MCP server](https://glama.ai/mcp/servers/AceDataCloud/MCPSeedream/badges/score.svg)](https://glama.ai/mcp/servers/AceDataCloud/MCPSeedream) 🐍 ☁️ - 通过 Ace Data Cloud API 提供字节跳动 Seedream 图像生成与编辑。
- [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) 📇 ☁️ - 面向 Open Library API 的 MCP 服务端，使 AI 助手能够搜索书籍信息。
- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - 使用 Manim 生成动画的本地 MCP 服务端。
- [austenstone/myinstants-mcp](https://github.com/austenstone/myinstants-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - 拥有来自 myinstants.com 数百万个梗声音的声音板 MCP 服务端。搜索、播放并浏览分类 —— 让 AI 智能体在代码编译时播放 Vine Boom。`npx myinstants-mcp`
- [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) 🐍 - 用于操作 Blender 的 MCP 服务端
- [albertnahas/icogenie-mcp](https://github.com/albertnahas/icogenie-mcp) [![icogenie-mcp MCP server](https://glama.ai/mcp/servers/@albertnahas/icogenie-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@albertnahas/icogenie-mcp) 📇 ☁️ - AI 驱动的 SVG 图标生成 MCP 服务端。通过文本描述生成生产级 SVG 图标，支持自定义样式。
- [aliafsahnoudeh/shahnameh-mcp-server](https://github.com/aliafsahnoudeh/shahnameh-mcp-server) 🐍 🏠 🍎 🪟 🐧 - 访问菲尔多西的波斯史诗《列王纪》（Shahnameh）的 MCP 服务端，包含章节、诗句和注释。
- [arikusi/nakkas](https://github.com/arikusi/nakkas) [![nakkas MCP server](https://glama.ai/mcp/servers/arikusi/nakkas/badges/score.svg)](https://glama.ai/mcp/servers/arikusi/nakkas) 📇 🏠 🍎 🪟 🐧 - 将 AI 转化为 SVG 艺术家的 MCP 服务端。单一渲染引擎配合 JSON 配置，AI 控制所有设计参数。支持 CSS @keyframes + SMIL 动画、16+ 元素类型、参数曲线、滤镜、渐变及 PNG 预览。
- [asmith26/jupytercad-mcp](https://github.com/asmith26/jupytercad-mcp) 🐍 🏠 🍎 🪟 🐧 - 面向 [JupyterCAD](https://github.com/jupytercad/JupyterCAD) 的 MCP 服务端，允许你通过 LLMs/自然语言控制它。
- [attalla1/photopea-mcp-server](https://github.com/attalla1/photopea-mcp-server) [![attalla1/photopea-mcp-server MCP server](https://glama.ai/mcp/servers/attalla1/photopea-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/attalla1/photopea-mcp-server) 📇 🏠 🍎 🪟 🐧 - 通过 Photopea 进行 AI 驱动的图像编辑，提供 34 个工具用于文档、图层、文本、形状、滤镜、效果和导出。`npx photopea-mcp-server`
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - 从你的 Video Jungle 集合中添加、分析、搜索和生成视频编辑内容
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 提供全面且准确的八字（中国占星术）排盘与分析
- [cfpramod/open-museum-mcp](https://github.com/cfpramod/open-museum-mcp) [![cfpramod/open-museum-mcp MCP server](https://glama.ai/mcp/servers/cfpramod/open-museum-mcp/badges/score.svg)](https://glama.ai/mcp/servers/cfpramod/open-museum-mcp) 📇 ☁️ 🍎 🪟 🐧 - 跨大都会博物馆、克利夫兰、AIC、维基共享资源及 Europeana 的联邦化、许可证验证搜索。默认严格拒绝权限，仅接受 CC0 / 公共领域标记。工具：search, get, cite（完整/说明/简短）, dynasty/region discovery。`npx -y open-museum-mcp`
- [Cifero74/mcp-apple-music](https://github.com/Cifero74/mcp-apple-music) [![mcp-apple-music MCP server](https://glama.ai/mcp/servers/@Cifero74/mcp-apple-music/badges/score.svg)](https://glama.ai/mcp/servers/@Cifero74/mcp-apple-music) 🐍 🏠 🍎 - 完整的 Apple Music 集成：搜索目录、浏览个人库、管理播放列表及获取个性化推荐。- [codex-curator/studiomcphub](https://github.com/codex-curator/studiomcphub) [![studio-mcp-hub MCP server](https://glama.ai/mcp/servers/@codex-curator/studio-mcp-hub/badges/score.svg)](https://glama.ai/mcp/servers/@codex-curator/studio-mcp-hub) 🐍 ☁️ - 32 个创意 AI 工具（18 个免费）面向自主智能体：图像生成（SD 3.5）、ESRGAN 超分、背景移除、产品样机、CMYK 转换、打印就绪 PDF、SVG 矢量化、隐形水印、AI 元数据增强、溯源、Arweave 存储、NFT 铸造及 53,000+ 博物馆艺术品。通过 x402/Stripe/GCX 按次付费。
- [ConstantineB6/comfy-pilot](https://github.com/ConstantineB6/comfy-pilot) 🐍 🏠 - ComfyUI 的 MCP 服务端，使 AI 智能体能够通过嵌入式终端查看、编辑并运行基于节点的图像生成工作流。
- [cswkim/discogs-mcp-server](https://github.com/cswkim/discogs-mcp-server) 📇 ☁️ - 用于与 Discogs API 交互的 MCP 服务端
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - 使用 Aseprite API 创建像素艺术的 MCP 服务端
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ 通过官方 REST API v4 与 Quran.com 语料库交互的 MCP 服务端。
- [drakonkat/wizzy-mcp-tmdb](https://github.com/drakonkat/wizzy-mcp-tmdb) 📇 ☁️ - 面向 The Movie Database API 的 MCP 服务端，使 AI 助手能够搜索和检索电影、电视剧及人物信息。
- [gavxm/ani-mcp](https://github.com/gavxm/ani-mcp) [![ani-mcp MCP server](https://glama.ai/mcp/servers/gavxm/ani-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gavxm/ani-mcp) 📇 🏠 - AniList 的 MCP 服务端，支持品味感知推荐、观看分析、社交工具及完整列表管理。
- [GenWaveLLC/svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp) 📇 ☁️ - 通过自然语言提供 AI 驱动的 SVG 生成与编辑，支持实时更新和安全文件处理。
- [gupta-kush/spotify-mcp](https://github.com/gupta-kush/spotify-mcp) 🐍 ☁️ 🍎 🪟 🐧 - 93 工具 Spotify 服务端，支持智能随机播放、自然语言歌曲搜索、氛围分析、艺术家网络映射、品味演化及播放列表强力工具。兼容 Spotify 2026年2月 API 变更后的版本。
- [jau123/MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP) [![mei-gen-ai-design-mcp MCP server](https://glama.ai/mcp/servers/@jau123/mei-gen-ai-design-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@jau123/mei-gen-ai-design-mcp) 📇 ☁️ 🏠 - AI 图像生成与编辑 MCP 服务端，拥有 1,500+ 精选提示词库、智能提示词增强及多提供商路由（本地 ComfyUI, MeiGen Cloud, OpenAI 兼容 API）。
- [khglynn/spotify-bulk-actions-mcp](https://github.com/khglynn/spotify-bulk-actions-mcp) 🐍 ☁️ - 批量 Spotify 操作，支持置信度评分的歌曲匹配、从 CSV/播客列表批量创建播放列表及库导出以发现你最常收藏的艺术家和专辑。
- [leonardoca1/aesthetics-wiki-mcp](https://github.com/leonardoca1/aesthetics-wiki-mcp) [![leonardoca1/aesthetics-wiki-mcp MCP server](https://glama.ai/mcp/servers/leonardoca1/aesthetics-wiki-mcp/badges/score.svg)](https://glama.ai/mcp/servers/leonardoca1/aesthetics-wiki-mcp) 🐍 🏠 🍎 🪟 🐧 - 从 [Aesthetics Wiki](https://aesthetics.fandom.com) 搜索、阅读并发现数千种视觉美学（田园风、暗黑学院风、Y2K、地精风等）。非常适合情绪板、品牌方向和创意灵感。`uvx aesthetics-wiki-mcp`
- [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) 📇 ☁️ - 大都会艺术博物馆收藏 API 集成，用于搜索和展示馆藏艺术品。
- [mikan-atomoki/text-to-model](https://github.com/mikan-atomoki/text-to-model) [![text-to-model MCP server](https://glama.ai/mcp/servers/mikan-atomoki/text-to-model/badges/score.svg)](https://glama.ai/mcp/servers/mikan-atomoki/text-to-model) 🐍 🏠 🪟 🍎 - 将自然语言转化为 Fusion 360 中的 3D 模型。包含 64 个 CAD 工具，包括草图、拉伸、圆角及 JIS 标准件。
- [molanojustin/smithsonian-mcp](https://github.com/molanojustin/smithsonian-mcp) 🐍 ☁️ - 使 AI 助手能够访问史密森尼学会开放收藏的 MCP 服务端。
- [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) #️⃣ ☁️ - 3D 打印机 MCP 服务端，支持获取实时打印机状态、摄像头快照及打印机控制。
- [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) 📇 ☁️ - MCP 服务端与扩展，使自然语言能够控制 NVIDIA Isaac Sim, Lab, OpenUSD 等。
- [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) 🐍 🏠 - Autodesk Maya 的 MCP 服务端
- [peek-travel/mcp-intro](https://github.com/peek-travel/mcp-intro) ☁️ 🍎 🪟 🐧 - 远程 MCP 服务端，用于发现和规划居家及度假体验
- [doctorm333/promptpilot-mcp-server](https://github.com/doctorm333/promptpilot-mcp-server) [![doctorm333/promptpilot-mcp-server MCP server](https://glama.ai/mcp/servers/doctorm333/promptpilot-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/doctorm333/promptpilot-mcp-server) 📇 ☁️ - 通过 20+ AI 模型（Flux, GPT-Image-1, Imagen 4, Grok, Seedance, ElevenLabs）生成图像、视频和音频。提供带风格、灯光、相机、情绪预设的提示词构建器及批量生成功能。
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - 荷兰（1940-1945）二战历史记录、照片和文件的 Oorlogsbronnen (战争来源) API 集成
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 荷兰国立博物馆艺术品搜索、详情及收藏的 Rijksmuseum API 集成
- [raveenb/fal-mcp-server](https://github.com/raveenb/fal-mcp-server) 🐍 ☁️ - 直接在 Claude Desktop 中使用 Fal.ai 模型（FLUX, Stable Diffusion, MusicGen）生成 AI 图像、视频和音乐。
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - DaVinci Resolve 的 MCP 服务端集成，提供强大的视频编辑、调色、媒体管理和项目控制工具。
- [shunshi-ai/bazi-reader-mcp](https://github.com/shunshi-ai/bazi-reader-mcp) [![shunshi-ai/bazi-reader-mcp MCP server](https://glama.ai/mcp/servers/shunshi-ai/bazi-reader-mcp/badges/score.svg)](https://glama.ai/mcp/servers/shunshi-ai/bazi-reader-mcp) 📇 🏠 🍎 🪟 🐧 - 八字（四柱推命）排盘 MCP 服务端，支持真太阳时校正及多语言输出（中文/EN/日本語/한국어）。`npx shunshi-bazi-mcp`
- [tasopen/mcp-alphabanana](https://github.com/tasopen/mcp-alphabanana) [![mcp-alphabanana MCP server](https://glama.ai/mcp/servers/@tasopen/mcp-alphabanana/badges/score.svg)](https://glama.ai/mcp/servers/@tasopen/mcp-alphabanana) 📇 🏠 🍎 🪟 🐧 - 使用 Google Gemini（Nano Banana 2 / Pro）生成图像资产的本地 MCP 服务端。支持透明 PNG/WebP 输出、精确调整大小/裁剪、最多 14 张参考图及 Google Search grounding。
- [TwelveTake-Studios/reaper-mcp](https://github.com/TwelveTake-Studios/reaper-mcp) 🐍 🏠 🍎 🪟 🐧 - 使 AI 助手能够控制 REAPER DAW 进行混音、母带处理、MIDI 作曲及完整音乐制作的 MCP 服务端，提供 129 个工具。
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - 集成 AniList API 用于动漫和漫画信息的 MCP 服务端
- [yuvalsuede/agent-media](https://github.com/yuvalsuede/agent-media) 📇 ☁️ 🍎 🪟 🐧 - AI 视频与图像生成的 CLI 和 MCP 服务端，统一访问 7 个模型（Kling, Veo, Sora, Seedance, Flux, Grok Imagine）。提供 9 个工具用于生成、管理和浏览媒体。


### 📐 <a name="architecture-and-design"></a>架构与设计

设计和可视化软件架构、系统图及技术文档。使 AI 模型能够生成专业图表和架构文档。

- [betterhyq/mermaid-grammer-inspector-mcp](https://github.com/betterhyq/mermaid_grammer_inspector_mcp) 📇 🏠 🍎 🪟 🐧 - 用于验证 Mermaid 图表语法并提供全面语法检查能力的模型上下文协议（MCP）服务端
- [BV-Venky/excalidraw-architect-mcp](https://github.com/BV-Venky/excalidraw-architect-mcp) [![excalidraw-architect-mcp MCP server](https://glama.ai/mcp/servers/@BV-Venky/excalidraw-architect-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@BV-Venky/excalidraw-architect-mcp) 🐍 🏠 🍎 🪟 🐧 - 自动生成布局、架构感知组件样式及状态编辑的精美 Excalidraw 架构图。支持 50+ 技术映射（数据库、消息队列、缓存等）。无需 API Key。
- [erajasekar/ai-diagram-maker-mcp](https://github.com/erajasekar/ai-diagram-maker-mcp) [![erajasekar/ai-diagram-maker-mcp MCP server](https://glama.ai/mcp/servers/erajasekar/ai-diagram-maker-mcp/badges/score.svg)](https://glama.ai/mcp/servers/erajasekar/ai-diagram-maker-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - AI Diagram Maker 的 MCP 服务端 —— 通过自然语言、代码、ASCII、图像或 Mermaid 生成流程图、序列图、ERD、系统/网络架构、UML、思维导图和工作流。使用 MCP Apps UI 进行内联渲染及可编辑图表 URL。需要 API Key。
- [flowzap-xyz/flowzap-mcp](https://github.com/flowzap-xyz/flowzap-mcp) [![flowzap-xyz/flowzap-mcp MCP server](https://glama.ai/mcp/servers/flowzap-xyz/flowzap-mcp/badges/score.svg)](https://glama.ai/mcp/servers/flowzap-xyz/flowzap-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - 使用 FlowZap Code DSL 创建工作流、序列和架构图。7 个工具用于验证、游乐场 URL 生成、语法文档、图导出、工件解析、对比及修补。无需 API Key。通过 NPM 安装：`npx -y flowzap-mcp`
- [GittyBurstein/mermaid-mcp-server](https://github.com/GittyBurstein/mermaid-mcp-server) 🐍 ☁️ - 将本地项目或 GitHub 仓库转换为 Mermaid 图表并通过 Kroki 渲染的 MCP 服务端。
- [Narasimhaponnada/mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp) 📇 ☁️ 🍎 🪟 🐧 - AI 驱动的 Mermaid 图表生成，支持 22+ 种图表类型（流程图、序列图、类图、ERD、架构图、状态机等）。提供 50+ 预构建模板、高级布局引擎、SVG/PNG/PDF 导出及与 GitHub Copilot, Claude 和任何 MCP 兼容客户端的无缝集成。通过 NPM 安装：`npm install -g @narasimhaponnada/mermaid-mcp-server`
- [rdanieli/tentra-mcp](https://github.com/rdanieli/tentra-mcp) [![rdanieli/tentra-mcp MCP server](https://glama.ai/mcp/servers/rdanieli/tentra-mcp/badges/score.svg)](https://glama.ai/mcp/servers/rdanieli/tentra-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - 面向工程团队的 AI 原生架构平台。用自然语言描述系统（例如“带有 Stripe, Kafka, PostgreSQL 的支付服务”）→ 获得包含 167 个云组件的可交互类型图表 → 导出至 14 种生产框架（Java Spring Boot, Python FastAPI, Go chi, Rust Axum, .NET, Kotlin Ktor, Ruby Rails, Elixir Phoenix, Docker Compose, Terraform, Mermaid, ADR 等）。漂移检测 (`sync_architecture`) 将保存的图表与实时代码进行 0-100 分评分及结构化对比。9 个质量规则捕获孤立节点、单点故障和上帝服务。还包括用于 AI 编码智能体的次要持久化代码图层（通过 `npx tentra-mcp --local init` 免费离线使用）。Agent-as-LLM 模式 —— 我们侧零 LLM 成本，你侧零 API Key。35 个 MCP 工具。兼容 Cursor, Claude Code, Codex, Windsurf。

### <a name="bio"></a>生物医学与生物信息学
- [ammawla/encode-toolkit](https://github.com/ammawla/encode-toolkit) [![encode-toolkit MCP server](https://glama.ai/mcp/servers/ammawla/encode-toolkit/badges/score.svg)](https://glama.ai/mcp/servers/ammawla/encode-toolkit) 🐧 - 面向完整 ENCODE Project 基因组数据和分析工具包的 MCP 服务端和 Claude 插件 —— 搜索、下载、追踪并分析功能基因组学实验。
- [cafferychen777/ChatSpatial](https://github.com/cafferychen777/ChatSpatial) 🐍 🏠 - 空间转录组学分析的 MCP 服务端，集成 60+ 方法覆盖细胞注释、去卷积、空间统计和可视化。
- [dnaerys/onekgpd-mcp](https://github.com/dnaerys/onekgpd-mcp) ☕ ☁️ 🍎 🪟 🐧 - 实时访问 1000 Genomes Project 数据集
- [fulcradynamics/fulcra-context-mcp](https://github.com/fulcradynamics/fulcra-context-mcp) [![fulcra-context-mcp MCP server](https://glama.ai/mcp/servers/fulcradynamics/fulcra-context-mcp/badges/score.svg)](https://glama.ai/mcp/servers/fulcradynamics/fulcra-context-mcp) 🐍 ☁️ - 通过 Fulcra Life API（OAuth2 同意）访问个人健康和生物数据，包括睡眠阶段、心率、HRV、血糖、锻炼、日历和位置的 MCP 服务端。
- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - 提供 PubMed, ClinicalTrials.gov 和 MyVariant.info 访问权限的生物医学研究 MCP 服务端。
- [HelixGenomics/Genomic-Agent-Discovery](https://github.com/HelixGenomics/Genomic-Agent-Discovery) [![Genomic-Agent-Discovery MCP server](https://glama.ai/mcp/servers/HelixGenomics/Genomic-Agent-Discovery/badges/score.svg)](https://glama.ai/mcp/servers/HelixGenomics/Genomic-Agent-Discovery) 📇 🏠 - 面向基因组分析的多智能体 MCP 服务端 —— 专用 AI 智能体跨 16 个数据库（ClinVar, GWAS, gnomAD, CPIC, AlphaMissense 等）分析原始 DNA 文件，并通过共享 MCP 工具协调发现结果。隐私优先，本地运行。
- [hlydecker/ucsc-genome-mcp](https://github.com/hlydecker/ucsc-genome-mcp) 🐍 ☁️ - 与 UCSC Genome Browser API 交互的 MCP 服务端，允许你查找基因组、染色体等。
- [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) 📇 🏠 - 提供医疗信息、药物数据库和医疗保健资源访问权限的 MCP 服务端。使 AI 助手能够查询医疗数据、药物相互作用及临床指南。
- [MyMedi-AI/mymedi-ai-mcp-server](https://github.com/MyMedi-AI/mymedi-ai-mcp-server) [![MyMedi-AI/mymedi-ai-mcp-server MCP server](https://glama.ai/mcp/servers/OFODevelopment/mymedi-ai-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/OFODevelopment/mymedi-ai-mcp-server) 📇 ☁️ - 面向智能体的医疗计费 AI：ICD-10/CPT/HCPCS 代码查询（81,769 个带 RVU + OPPS 定价的代码）、预授权预测、医疗 NER、索赔验证、拒付风险评分、HIPAA 合规审计及 NPI/药物增强。20 个工具，10 个免费积分后通过积分或匿名 USDC（x402）按次付费。`npx @mymedi-ai/mcp-server`
- [NyxToolsDev/dicom-hl7-mcp-server](https://github.com/NyxToolsDev/dicom-hl7-mcp-server) [![NyxToolsDev/dicom-hl7-mcp-server MCP server](https://glama.ai/mcp/servers/NyxToolsDev/dicom-hl7-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/NyxToolsDev/dicom-hl7-mcp-server) 🐍 🏠 - 唯一将 DICOM, HL7v2 和 FHIR 桥接在一个包中的 MCP 服务端。跨标准映射、Mirth Connect 通道生成、厂商私有标签解码（GE, Siemens, Philips）及集成模式知识。由 19 年医疗 IT 老兵构建。`pip install dicom-hl7-mcp`
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - 与 BioThings API（包括基因、遗传变异、药物和分类信息）交互的 MCP 服务端。
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - 提供强大生物信息学工具包用于基因组查询和分析的 MCP 服务端，封装流行的 `gget` 库。
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - OpenGenes 项目衰老与长寿研究可查询数据库的 MCP 服务端。
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - SynergyAge 协同与拮抗遗传相互作用长寿数据库的 MCP 服务端。
- [neptun2000/heor-agent-mcp](https://github.com/neptun2000/heor-agent-mcp) [![heor-agent-mcp MCP server](https://glama.ai/mcp/servers/neptun2000/heor-agent-mcp/badges/score.svg)](https://glama.ai/mcp/servers/neptun2000/heor-agent-mcp) 📇 ☁️ - 面向 HEOR（卫生经济学与结果研究）的 MCP 服务端，提供 7 个工具用于跨 41 个医疗数据源（PubMed, NICE, CADTH, ICER 等）的文献搜索、成本效益建模（Markov/PartSA/PSA）及 HTA 档案准备。
- [OHNLP/omop_mcp](https://github.com/OHNLP/omop_mcp) 🐍 🏠 ☁️ - 使用 LLMs 将临床术语映射到 OMOP 概念，用于医疗数据标准化和互操作性。
- [tatsuju/opdstar-nhi-mcp](https://github.com/tatsuju/opdstar-nhi-mcp) [![opdstar-nhi-mcp MCP server](https://glama.ai/mcp/servers/tatsuju/opdstar-nhi-mcp/badges/score.svg)](https://glama.ai/mcp/servers/tatsuju/opdstar-nhi-mcp) 📇 ☁️ - 台湾首个公开数据国民健康保险（NHI）MCP 服务端 —— 234 个拒付代码、跨 20 个专科的 1,497 个 ICD-10→手术映射、审计指标（008/014/027/P043）及 8,232 块官方 NHI 文档的语义 wiki 搜索。由 [OPDSTAR](https://opdstar.com) 驱动。安装：`npx @opdstar/nhi-mcp`。
- [pkotecha-eng/aria-mcp-server](https://github.com/pkotecha-eng/aria-mcp-server) [![aria-mcp-server MCP server](https://glama.ai/mcp/servers/pkotecha-eng/aria-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/pkotecha-eng/aria-mcp-server) 🐍 - 临床试验协调员和生命科学团队的临床研究 MCP 服务端。实时访问 PubMed（3500万+论文）和 ClinicalTrials.gov（40万+试验）。无需 API Key。
- [the-momentum/apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server) 🐍 🏠 🍎 🪟 🐧 - 提供 Apple Health 导出数据访问权限的 MCP 服务端。包含数据分析功能。
- [the-momentum/fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server) 🐍 🏠 ☁️ - 将 AI 智能体连接到 FHIR 服务端的 MCP 服务端。一个示例用例是通过自然语言查询患者病史。
- [thelongevityvault/decoder-3am-mcp](https://github.com/thelongevityvault/decoder-3am-mcp) [![thelongevityvault/decoder-3am-mcp MCP server](https://glama.ai/mcp/servers/thelongevityvault/decoder-3am-mcp/badges/score.svg)](https://glama.ai/mcp/servers/thelongevityvault/decoder-3am-mcp) 📇 ☁️ - 使用 The Longevity Vault 的 5 大原因框架对睡眠中断进行分类。通过症状描述识别凌晨 3 点醒来的生物学机制，并提供指向完整交互式 3AM Decoder 的可追踪链接。
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - Fast Healthcare Interoperability Resources (FHIR) API 的模型上下文协议服务端。提供与 FHIR 服务端的无缝集成，使 AI 助手能够搜索、检索、创建、更新和分析临床医疗数据，支持 SMART-on-FHIR 认证。

### 📂 <a name="browser-automation"></a>浏览器自动化

网页内容访问与自动化能力。使 AI 模型能够以友好的格式搜索、抓取和处理网页内容。

- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - 支持搜索 Bilibili 内容的 MCP 服务端。提供 LangChain 集成示例和测试脚本。
- [achiya-automation/safari-mcp](https://github.com/achiya-automation/safari-mcp) [![safari-mcp MCP server](https://glama.ai/mcp/servers/achiya-automation/safari-mcp/badges/score.svg)](https://glama.ai/mcp/servers/achiya-automation/safari-mcp) 📇 🏠 🍎 - 面向 AI 智能体的原生 Safari 浏览器自动化，提供 80+ 工具。无 Chrome 依赖，针对 Apple Silicon 优化，CPU 开销降低 60%。
- [agent-infra/mcp-server-browser](https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser) 📇 🏠 - 使用 Puppeteer 的浏览器自动化能力，支持本地和远程浏览器连接。
- [aparajithn/agent-scraper-mcp](https://github.com/aparajithn/agent-scraper-mcp) [![agent-scraper-mcp MCP server](https://glama.ai/mcp/servers/@aparajithn/agent-scraper-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@aparajithn/agent-scraper-mcp) 🐍 ☁️ - 面向 AI 智能体的网页抓取 MCP 服务端。6 个工具：清洁内容提取、CSS 选择器结构化抓取、Playwright 全页截图、链接提取、元数据提取（OG/Twitter 卡片）及 Google 搜索。免费层级支持 x402 微支付。
- [apireno/DOMShell](https://github.com/apireno/DOMShell) [![domshell MCP server](https://glama.ai/mcp/servers/@apireno/domshell/badges/score.svg)](https://glama.ai/mcp/servers/@apireno/domshell) 📇 🏠 - 使用文件系统命令（ls, cd, grep, click）浏览网页。38 个 MCP 工具通过 Chrome 扩展将 Chrome 的无障碍树映射到虚拟文件系统。
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - 使用 Playwright 进行浏览器自动化的 MCP 服务端
- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) 🦀 Rust 编写的轻量级浏览器自动化 MCP 服务端，零依赖。
- [bch1212/agentfetch-mcp](https://github.com/bch1212/agentfetch-mcp) [![bch1212/agentfetch-mcp MCP server](https://glama.ai/mcp/servers/bch1212/agentfetch-mcp/badges/score.svg)](https://glama.ai/mcp/servers/bch1212/agentfetch-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - 面向 AI 智能体的令牌预算网页抓取。根据 URL 模式在 Trafilatura, Jina Reader, FireCrawl 和 pypdf 之间自动路由。`fetch_url` 前执行 `estimate_tokens`，6 小时 Redis 缓存，服务端 `max_tokens` 截断。开源 MCP 服务端（MIT）及 [agentfetch.dev](https://www.agentfetch.dev) 托管 REST API —— 每月 500 次免费抓取，无需信用卡。
- [bighippoman/intercept-mcp](https://github.com/bighippoman/intercept-mcp) [![bighippoman/intercept-mcp MCP server](https://glama.ai/mcp/servers/bighippoman/intercept-mcp/badges/score.svg)](https://glama.ai/mcp/servers/bighippoman/intercept-mcp) 📇 🏠 - 用于将网页内容抓取为清洁 Markdown 的多级回退链。处理推文、YouTube、arXiv、PDF 和普通页面，提供 9 种回退策略。
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - 使用 Playwright 进行浏览器自动化的 Python MCP 服务端，更适合 LLM
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - 在云端自动化浏览器交互（如网页导航、数据提取、表单填写等）
- [browsermcp/mcp](https://github.com/browsermcp/mcp) 📇 🏠 - 自动化你的本地 Chrome 浏览器
- [brutalzinn/simple-mcp-selenium](https://github.com/brutalzinn/simple-mcp-selenium) 📇 🏠 - 面向 Cursor IDE 的 Selenium MCP 服务端，支持自然语言控制浏览器。非常适合测试、自动化和多用户场景。
- [co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🐍 - 打包为带 SSE 传输的 MCP 服务端的 browser-use。包含 Dockerfile 用于在 Docker + VNC 服务器中运行 Chromium。
- [Custodia-Admin/pagebolt-mcp](https://github.com/Custodia-Admin/pagebolt-mcp) [![Custodia-Admin/pagebolt-mcp MCP server](https://glama.ai/mcp/servers/Custodia-Admin/pagebolt-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Custodia-Admin/pagebolt-mcp) 📇 ☁️ - 面向 Claude Desktop, Cursor 和 Windsurf 的截图、PDF、OG 图像及旁白视频录制 MCP 服务端。
- [eat-pray-ai/yutu](https://github.com/eat-pray-ai/yutu) 🏎️ 🏠 🍎 🐧 🪟 - 功能完整的 YouTube 自动化 MCP 服务端和 CLI
- [executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 📇 - 使用 Playwright 进行浏览器自动化和网络抓取的 MCP 服务端
- [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) 📇 🏠 - 配合浏览器扩展使用的 MCP 服务端，使 LLM 客户端能够控制用户浏览器（Firefox）。
- [fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - macOS 上用于与 Apple Reminders 交互的 MCP 服务端
- [freema/firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) 📇 🏠 - 通过 WebDriver BiDi 进行 Firefox 浏览器自动化，适用于测试、抓取和浏览器控制。支持基于快照/UID 的交互、网络监控、控制台捕获及截图。
- [getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 📇 🏠 - 从任何网站提取结构化数据。只需提示词即可获得 JSON。
- [hanzili/comet-mcp](https://github.com/hanzili/comet-mcp) 📇 🏠 🍎 - 连接 Perplexity Comet 浏览器进行智能体网页浏览、深度研究和实时监控任务。
- [LarryWalkerDEV/mcp-immostage](https://github.com/LarryWalkerDEV/mcp-immostage) 📇 ☁️ - AI 虚拟房地产布景。布置空房间、将平面图美化转为 3D 渲染、分类房间图像、生成物业描述及获取风格建议。
- [LeonTing1010/tap](https://github.com/LeonTing1010/tap) [![LeonTing1010/tap MCP server](https://glama.ai/mcp/servers/LeonTing1010/tap/badges/score.svg)](https://glama.ai/mcp/servers/LeonTing1010/tap) 📇 🏠 🍎 🪟 🐧 - 将 AI 浏览器自动化编译为确定性 `.tap.json` 计划（25-op 闭合联合，零运行时 LLM）、在你已登录的 Chrome 上运行，并通过语义指纹对比检测站点变更漂移。40+ 网站拥有 65+ 开放社区 taps。
- [markmircea/Selenix-MCP-Server](https://github.com/markmircea/Selenix-MCP-Server) [![markmircea/Selenix-MCP-Server MCP server](https://glama.ai/mcp/servers/markmircea/Selenix-MCP-Server/badges/score.svg)](https://glama.ai/mcp/servers/markmircea/Selenix-MCP-Server) 📇 🏠 🍎 🪟 🐧 - 桥接 Claude Desktop 与 Selenix 的 MCP 服务端，用于浏览器自动化和测试。通过自然语言创建、运行、调试和管理浏览器测试。
- [imprvhub/mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent) 📇 🏠 - 提供 Claude Desktop 自主浏览器自动化能力的模型上下文协议（MCP）集成。
- [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - 获取 YouTube 字幕和转录文本供 AI 分析
- [samson-art/transcriptor-mcp](https://github.com/samson-art/transcriptor-mcp) [![transcriptor-mcp MCP server](https://glama.ai/mcp/servers/samson-art/transcriptor-mcp/badges/score.svg)](https://glama.ai/mcp/servers/samson-art/transcriptor-mcp) 📇 ☁️ - 当你需要 AI、摘要或内容分析的转录文本和元数据时，Transcriptor MCP 是你的首选
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - 使用 Azure OpenAI 和 Playwright 的 `minimal` 服务端/客户端 MCP 实现。
- [junipr-labs/mcp-server](https://github.com/junipr-labs/mcp-server) [![mcp-server MCP server](https://glama.ai/mcp/servers/junipr-labs/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/junipr-labs/mcp-server) 📇 ☁️ - 面向 AI 智能体的网页情报 API —— 截图捕获、PDF 生成、页面元数据提取及 75+ 专业数据提取器（新闻、社交媒体、SERP、定价等）。包含免费层级。
- [lightpanda-io/gomcp](https://github.com/lightpanda-io/gomcp) 🏎 🏠/☁️ 🐧/🍎 - Go 编写的 MCP 服务端，用于专为网页自动化设计的超快无头浏览器 Lightpanda
- [LvcidPsyche/auto-browser](https://github.com/LvcidPsyche/auto-browser) [![LvcidPsyche/auto-browser MCP server](https://glama.ai/mcp/servers/LvcidPsyche/auto-browser/badges/score.svg)](https://glama.ai/mcp/servers/LvcidPsyche/auto-browser) 🐍 🏠 🐧 🍎 🪟 - 开源 MCP 原生浏览器智能体，支持通过 noVNC 人工接管、可重用认证配置及审批/审计轨道。基于 Playwright + FastAPI，Docker 隔离会话，为 Claude Desktop 和 Cursor 提供 stdio 桥接。
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) - Microsoft 官方 Playwright MCP 服务端，使 LLMs 能够通过结构化的无障碍快照与网页交互
- [modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer) 📇 🏠 - 用于网络抓取和交互的浏览器自动化
- [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) 📇 🏠 - 使 AI 助手能够与你本地浏览器交互的 MCP 服务端。
- [nnemirovsky/iwdp-mcp](https://github.com/nnemirovsky/iwdp-mcp) [![iwdp-mcp MCP server](https://glama.ai/mcp/servers/nnemirovsky/iwdp-mcp/badges/score.svg)](https://glama.ai/mcp/servers/nnemirovsky/iwdp-mcp) 🏎️ 🏠 🍎 🐧 - 通过 ios-webkit-debug-proxy 进行 iOS Safari 调试 —— 完整支持 WebKit Inspector Protocol（DOM, CSS, Network, Storage, Debugger 等）的 MCP 服务端
- [Metadrama/obscura-mcp](https://github.com/Metadrama/obscura-mcp) [![Metadrama/obscura-mcp MCP server](https://glama.ai/mcp/servers/Metadrama/obscura-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Metadrama/obscura-mcp) 📇 ☁️ 🐧 🪟 🍎 - 轻量级 Rust 无头浏览器 Obscura 的 MCP 服务端适配器 —— 高性能网页抓取，反检测。非常适合 AI 智能体自动化。服务端可 [本地运行](https://github.com/Metadrama/obscura-mcp) 或作为 [托管端点](https://glama.ai/mcp/connectors)。
- [olostep/olostep-mcp-server](https://github.com/olostep/olostep-mcp-server) 📇 ☁️ - 网页抓取、爬取和搜索 API。以 Markdown/JSON 提取内容，批量处理 10k URL，并通过引用获取 AI 驱动的答案。
- [operative_sh/web-eval-agent](https://github.com/Operative-Sh/web-eval-agent) 🐍 🏠 🍎 - 使用 browser-use 浏览器智能体自主调试 Web 应用的 MCP 服务端
- [ofershap/real-browser-mcp](https://github.com/ofershap/real-browser-mcp) [![real-browser-mcp MCP server](https://glama.ai/mcp/servers/ofershap/real-browser-mcp/badges/score.svg)](https://glama.ai/mcp/servers/ofershap/real-browser-mcp) 📇 🏠 - 配合 Chrome 扩展的 MCP 服务端，使 AI 智能体能够控制用户真实浏览器（保留现有会话、登录和 Cookie）。无需无头浏览器，无需重新认证。
- [Pantheon-Security/chrome-mcp-secure](https://github.com/Pantheon-Security/chrome-mcp-secure) 📇 🏠 🍎 🪟 🐧 - 后量子加密（ML-KEM-768 + ChaCha20-Poly1305）、安全凭证库、内存清理及审计日志的安全加固 Chrome 自动化。提供 22 个浏览器自动化和安全登录工具。
- [PhungXuanAnh/selenium-mcp-server](https://github.com/PhungXuanAnh/selenium-mcp-server) 🐍 🏠 🍎 🪟 🐧 - 通过 Selenium WebDriver 提供网页自动化能力的模型上下文协议服务端
- [pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - 启用免费 Google 搜索结果搜索的 MCP 服务端，无需 API Key。
- [KuvopLLC/purroxy2](https://github.com/KuvopLLC/purroxy2) [![purroxy MCP server](https://glama.ai/mcp/servers/KuvopLLC/purroxy2/badges/score.svg)](https://glama.ai/mcp/servers/KuvopLLC/purroxy2) 📇 🏠 🍎 🪟 🐧 - 记录你在任何网站上的操作并永久安全地自动化。在 Playwright 无头浏览器中回放浏览器动作，配合加密凭证和 AI 驱动的选择器修复。
- [realwigu/mcp-doctor](https://github.com/realwigu/mcp-doctor) [![realwigu/mcp-doctor MCP server](https://glama.ai/mcp/servers/realwigu/mcp-doctor/badges/score.svg)](https://glama.ai/mcp/servers/realwigu/mcp-doctor) 📇 🏠 🍎 🪟 🐧 - 面向 MCP 服务端的零配置诊断工具。自动发现 Claude Code, Cursor, VS Code, Windsurf 和 Claude Desktop 的配置，通过 JSON-RPC 握手测试连接，审计安全问题并基准化延迟。也可作为 MCP 服务端自身运行。
- [recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - Apple Shortcuts 的 MCP 服务端集成
- [Retio-ai/pagemap](https://github.com/Retio-ai/Retio-pagemap) 🐍 🏠 - 将约 100K 令牌的 HTML 压缩为 2-5K 令牌的结构化地图，同时保留每个可操作元素。AI 智能体能以少 97% 的令牌读取和交互任何网页。
- [serkan-ozal/browser-devtools-mcp](https://github.com/serkan-ozal/browser-devtools-mcp) 📇 - 使 AI 助手能够自主测试、调试和验证 Web 应用的 MCP 服务端
- [softvoyagers/pageshot-api](https://github.com/softvoyagers/pageshot-api) 📇 ☁️ - 免费网页截图捕获 API，支持格式、视口和暗色模式选项。无需 API Key。
- [User0856/snaprender-mcp](https://github.com/User0856/snaprender-integrations/tree/main/mcp-server) [![snaprender-mcp MCP server](https://glama.ai/mcp/servers/@User0856/snaprender-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@User0856/snaprender-mcp) 📇 ☁️ - 面向 AI 智能体的截图 API —— 以 PNG, JPEG, WebP 或 PDF 捕获任何网站，支持设备模拟、暗色模式、广告拦截及 Cookie 横幅移除。包含免费层级。
- [copperline-labs/rendex-mcp](https://github.com/copperline-labs/rendex-mcp) [![rendex-mcp MCP server](https://glama.ai/mcp/servers/copperline-labs/rendex-mcp/badges/score.svg)](https://glama.ai/mcp/servers/copperline-labs/rendex-mcp) 📇 ☁️ - 面向 AI 智能体的截图、PDF 和 HTML 渲染 API。以 PNG/JPEG/WebP/PDF 捕获任何 URL 或原始 HTML，支持批量处理、地理定位、异步 Webhook 及 MCP 原生集成。包含免费层级。
- [webdriverio/mcp](https://github.com/webdriverio/mcp) [![mcp MCP server](https://glama.ai/mcp/servers/webdriverio/mcp/badges/score.svg)](https://glama.ai/mcp/servers/webdriverio/mcp) 📇 🏠 - 使用 WebdriverIO 进行浏览器和移动应用自动化，使 AI 智能体能够通过 WebDriver 和 Appium 协议控制浏览器、与网页元素交互并自动化原生 Android 和 iOS 应用。
- [xspadex/bilibili-mcp](https://github.com/xspadex/bilibili-mcp.git) 📇 🏠 - 基于 FastMCP 的工具，获取 Bilibili 热门视频并通过标准 MCP 接口暴露。
- [ymw0407/auth-fetch-mcp](https://github.com/ymw0407/auth-fetch-mcp) [![ymw0407/auth-fetch-mcp MCP server](https://glama.ai/mcp/servers/ymw0407/auth-fetch-mcp/badges/score.svg)](https://glama.ai/mcp/servers/ymw0407/auth-fetch-mcp) 📇 🏠 🍎 🪟 🐧 - 通过打开真实浏览器进行认证并持久化会话缓存，从受登录保护的网页（Notion, Google Docs, Jira, Confluence 等）获取内容。
- [PrinceGabriel-lgtm/freshcontext-mcp](https://github.com/PrinceGabriel-lgtm/freshcontext-mcp) [![freshcontext-mcp MCP server](https://glama.ai/mcp/servers/@PrinceGabriel-lgtm/freshcontext-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@PrinceGabriel-lgtm/freshcontext-mcp) ☁️ 🏠 - 带新鲜时间戳的实时网页情报。GitHub, HN, Scholar, arXiv, YC, jobs, finance, package trends —— 每个结果都标注其新鲜度。

### ☁️ <a name="cloud-platforms"></a>云平台

云服务平台集成。使 AI 模型能够管理和与云基础设施及服务交互。

- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - 面向 4EVERLAND Hosting 的 MCP 服务端实现，使 AI 生成的代码能够即时部署到 Greenfield, IPFS 和 Arweave 等去中心化存储网络。
- [aashari/mcp-server-aws-sso](https://github.com/aashari/mcp-server-aws-sso) 📇 ☁️ 🏠 - AWS 单点登录（SSO）集成，使 AI 系统能够通过启动 SSO 登录、列出账户/角色及使用临时凭证执行 AWS CLI 命令来安全地与 AWS 资源交互。
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - IPFS 存储的上传与操作
- [aparajithn/agent-deploy-dashboard-mcp](https://github.com/aparajithn/agent-deploy-dashboard-mcp) [![agent-deploy-dashbaord MCP server](https://glama.ai/mcp/servers/@aparajithn/agent-deploy-dashbaord/badges/score.svg)](https://glama.ai/mcp/servers/@aparajithn/agent-deploy-dashbaord) 🐍 ☁️ - 跨 Vercel, Render, Railway 和 Fly.io 的统一部署仪表板 MCP 服务端。9 个工具用于所有平台的部署状态、日志、环境变量、回滚和健康检查。免费层级支持 x402 微支付。
- [arnstarn/mcp-server-spotinst](https://github.com/arnstarn/mcp-server-spotinst) [![arnstarn/mcp-server-spotinst MCP server](https://glama.ai/mcp/servers/arnstarn/mcp-server-spotinst/badges/score.svg)](https://glama.ai/mcp/servers/arnstarn/mcp-server-spotinst) 🐍 ☁️ - 面向 Spot.io (Spotinst) API 的 MCP 服务端，提供 23 个工具用于跨 AWS 和 Azure 管理 Ocean 集群、VNGs, Elastigroups、成本、自动调整规模和日志，支持多账户。
- [antonio-mello-ai/mcp-pfsense](https://github.com/antonio-mello-ai/mcp-pfsense) [![mcp-pfsense MCP server](https://glama.ai/mcp/servers/antonio-mello-ai/mcp-pfsense/badges/score.svg)](https://glama.ai/mcp/servers/antonio-mello-ai/mcp-pfsense) 🐍 🏠 - 通过 AI 助手管理 pfSense 防火墙 —— 防火墙规则、DHCP 租约/保留、DNS 覆盖、网关监控、ARP 表及服务管理。17 个工具，破坏性操作需两步确认。
- [antonio-mello-ai/mcp-proxmox](https://github.com/antonio-mello-ai/mcp-proxmox) [![mcp-proxmox MCP server](https://glama.ai/mcp/servers/antonio-mello-ai/mcp-proxmox/badges/score.svg)](https://glama.ai/mcp/servers/antonio-mello-ai/mcp-proxmox) 🐍 🏠 - 通过 AI 助手管理 Proxmox VE 集群 —— VM、容器、快照、模板、cloud-init、防火墙及迁移。29 个工具，破坏性操作需两步确认。
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - 轻量但强大的服务端，使 AI 助手能够在安全的 Docker 环境中（支持多架构）执行 AWS CLI 命令、使用 Unix 管道及应用常见 AWS 任务的提示词模板。
- [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - 轻量但健壮的服务端，赋能 AI 助手在安全的 Docker 环境中（支持多架构）安全执行 Kubernetes CLI 命令 (`kubectl`, `helm`, `istioctl`, `argocd`)。
- [alexpota/cloudscope-mcp](https://github.com/alexpota/cloudscope-mcp) [![alexpota/cloudscope-mcp MCP server](https://glama.ai/mcp/servers/alexpota/cloudscope-mcp/badges/score.svg)](https://glama.ai/mcp/servers/alexpota/cloudscope-mcp) 📇 ☁️ - Azure 云成本管理 —— 支出分析、预测、异常检测、预算、优化建议、闲置资源检测、基于标签的成本分配及跨订阅查询，均通过自然语言实现。
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - 使 AI 助手能够在阿里云上操作资源的 MCP 服务端，支持 ECS、云监控、OOS 及广泛使用的