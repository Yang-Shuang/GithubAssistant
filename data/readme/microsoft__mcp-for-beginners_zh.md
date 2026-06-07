![MCP-for-beginners](./images/mcp-beginners.png) 

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/mcp-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/mcp-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/mcp-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

按照以下步骤开始使用这些资源：
1. **Fork 本仓库**：点击 [![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
2. **克隆仓库**：   `git clone https://github.com/microsoft/mcp-for-beginners.git`
3. **加入 [![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG) 社区**


### 🌐 多语言支持

#### 通过 GitHub Action 自动同步（自动化且始终保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./translations/ar/README.md) | [Bengali](./translations/bn/README.md) | [Bulgarian](./translations/bg/README.md) | [Burmese (Myanmar)](./translations/my/README.md) | [Chinese (Simplified)](./translations/zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](./translations/zh-HK/README.md) | [Chinese (Traditional, Macau)](./translations/zh-MO/README.md) | [Chinese (Traditional, Taiwan)](./translations/zh-TW/README.md) | [Croatian](./translations/hr/README.md) | [Czech](./translations/cs/README.md) | [Danish](./translations/da/README.md) | [Dutch](./translations/nl/README.md) | [Estonian](./translations/et/README.md) | [Finnish](./translations/fi/README.md) | [French](./translations/fr/README.md) | [German](./translations/de/README.md) | [Greek](./translations/el/README.md) | [Hebrew](./translations/he/README.md) | [Hindi](./translations/hi/README.md) | [Hungarian](./translations/hu/README.md) | [Indonesian](./translations/id/README.md) | [Italian](./translations/it/README.md) | [Japanese](./translations/ja/README.md) | [Kannada](./translations/kn/README.md) | [Khmer](./translations/km/README.md) | [Korean](./translations/ko/README.md) | [Lithuanian](./translations/lt/README.md) | [Malay](./translations/ms/README.md) | [Malayalam](./translations/ml/README.md) | [Marathi](./translations/mr/README.md) | [Nepali](./translations/ne/README.md) | [Nigerian Pidgin](./translations/pcm/README.md) | [Norwegian](./translations/no/README.md) | [Persian (Farsi)](./translations/fa/README.md) | [Polish](./translations/pl/README.md) | [Portuguese (Brazil)](./translations/pt-BR/README.md) | [Portuguese (Portugal)](./translations/pt-PT/README.md) | [Punjabi (Gurmukhi)](./translations/pa/README.md) | [Romanian](./translations/ro/README.md) | [Russian](./translations/ru/README.md) | [Serbian (Cyrillic)](./translations/sr/README.md) | [Slovak](./translations/sk/README.md) | [Slovenian](./translations/sl/README.md) | [Spanish](./translations/es/README.md) | [Swahili](./translations/sw/README.md) | [Swedish](./translations/sv/README.md) | [Tagalog (Filipino)](./translations/tl/README.md) | [Tamil](./translations/ta/README.md) | [Telugu](./translations/te/README.md) | [Thai](./translations/th/README.md) | [Turkish](./translations/tr/README.md) | [Ukrainian](./translations/uk/README.md) | [Urdu](./translations/ur/README.md) | [Vietnamese](./translations/vi/README.md)

> **更倾向于本地克隆？**
>
> 本仓库包含 50+ 种语言的翻译，这会显著增加下载体积。若需跳过翻译文件进行克隆，请使用稀疏检出（sparse checkout）：
>
> **Bash / macOS / Linux：**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows)：**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 这将为你提供完成课程所需的所有内容，同时大幅加快下载速度。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

# 🚀 Model Context Protocol (MCP) 初学者课程

## **通过 C#、Java、JavaScript、Rust、Python 和 TypeScript 的动手代码示例学习 MCP**

## 🧠 Model Context Protocol（模型上下文协议）课程概览
欢迎来到你的 Model Context Protocol 探索之旅！如果你曾好奇 AI 应用如何与不同的工具和服务进行通信，现在你将发现一种正在重塑开发者构建智能系统方式的优雅解决方案。

可以将 MCP 想象成 AI 应用的“通用翻译器”——就像 USB 接口让你能将任何设备连接到电脑一样，MCP 让 AI 模型能够以标准化的方式连接任意工具或服务。无论你是开发第一个聊天机器人，还是处理复杂的 AI 工作流，掌握 MCP 都将赋予你构建更强大、更灵活应用的能力。

本课程专为你的学习旅程精心打造。我们将从你已经熟悉的概念入手，逐步通过动手实践在你的首选编程语言中积累经验。每一步都配有清晰的解释、实用示例以及充分的鼓励。

当你完成这段旅程时，你将能够自信地搭建自己的 MCP 服务器，将其与主流 AI 平台集成，并深入理解这项技术如何重塑 AI 开发的未来。让我们一起开启这段激动人心的探索吧！

### 官方文档与规范

本课程严格对齐 **MCP Specification 2025-11-25**（最新稳定版本）。MCP 规范采用基于日期的版本号格式（YYYY-MM-DD），以确保协议版本追踪清晰明确。

随着你理解的深入，这些资源会变得越来越有价值，但无需急于一次性读完所有内容！从你最感兴趣的领域开始即可：
- 📘 [MCP Documentation](https://modelcontextprotocol.io/) – 你的首选学习资源，提供循序渐进的教程和用户指南。文档专为初学者编写，配有清晰的示例，你可以按自己的节奏跟随练习。
- 📜 [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25) – 相当于你的综合参考手册。在学习过程中，你会频繁回来查阅具体细节和探索高级功能。
- 📜 [MCP Specification Versioning](https://modelcontextprotocol.io/specification/versioning) – 包含协议版本历史以及 MCP 如何使用基于日期的版本号格式（YYYY-MM-DD）的说明。
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – 在这里你可以找到多种编程语言的 SDK、工具和代码示例。它就像一座实用示例和即插即用组件的宝库。
- 🌐 [MCP Community](https://github.com/orgs/modelcontextprotocol/discussions) – 加入其他学习者和资深开发者的讨论，交流 MCP 相关话题。这是一个充满支持的社区，欢迎提问并自由分享知识。
  
## 学习目标

完成本课程后，你将对自己的新技能充满信心与热情。以下是你将要掌握的能力：

• **理解 MCP 基础**：通过直观的类比和示例，掌握 Model Context Protocol 的定义及其如何革新 AI 应用的协作方式。

• **搭建你的第一个 MCP 服务器**：使用你首选的编程语言创建一个可运行的 MCP 服务器，从简单示例开始，逐步提升技能。

• **将 AI 模型连接到实际工具**：学习如何打通 AI 模型与实际服务之间的桥梁，为你的应用赋予强大的新功能。

• **实施安全最佳实践**：掌握保护 MCP 实现的安全方法，确保你的应用和用户数据安全无忧。

• **自信部署上线**：了解如何将 MCP 项目从开发环境平滑过渡到生产环境，掌握经过实战验证的部署策略。

• **加入 MCP 社区**：成为日益壮大的开发者社群的一员，共同塑造 AI 应用开发的未来。 

## 必备背景知识

在深入 MCP 细节之前，我们先确保你对一些基础概念感到舒适。不用担心你是否是这些领域的专家——我们会在学习过程中逐步讲解所有必要内容！

### 理解协议（基石）

可以将协议想象成对话的规则。当你给朋友打电话时，双方都知道接起时说“你好”，轮流发言，挂断前说“再见”。计算机程序也需要类似的规则才能有效通信。

MCP 是一种协议——一套约定好的规则，帮助 AI 模型和应用与工具及服务进行高效的“对话”。就像人类沟通需要交流规则一样，拥有 MCP 能让 AI 应用之间的交互更加可靠且强大。

### 客户端与服务器关系（程序如何协同工作）

你每天都在使用客户端-服务器架构！当你用网页浏览器（客户端）访问网站时，你正在连接发送页面内容的 Web 服务器。浏览器知道如何请求信息，而服务器知道如何响应。

在 MCP 中，我们也有类似的关系：AI 模型充当请求信息或执行操作的客户端，而 MCP 服务器则提供这些能力。这就像拥有一个 AI 可以随时调用来完成特定任务的“得力助手”（服务器）。

### 为什么标准化很重要（让事物无缝协作）

想象一下，如果每家汽车制造商都使用不同形状的加油枪——那你每辆车都需要一个不同的转接头！标准化意味着就通用方案达成一致，使一切能够无缝协作。

MCP 为 AI 应用提供了这种标准化。不再需要每个 AI 模型都为每种工具编写定制代码，MCP 创建了一种通用的通信方式。这意味着开发者只需构建一次工具，就能让它与多种不同的 AI 系统协同工作。

## 🧭 你的学习路径概览

你的 MCP 学习之旅经过精心设计，旨在逐步建立你的信心与技能。每个阶段都会引入新概念，同时巩固你已学的内容。

### 🌱 基础阶段：理解核心概念（模块 0-2）

这是你冒险的起点！我们将使用熟悉的类比和简单示例为你介绍 MCP 概念。你将了解 MCP 是什么、为什么存在，以及它如何融入更广阔的 AI 开发生态。

• **模块 0 - MCP 简介**：我们将从探索 MCP 的定义及其对现代 AI 应用的重要性开始。你会看到 MCP 在实际场景中的应用案例，并理解它如何解决开发者面临的常见问题。

• **模块 1 - 核心概念详解**：在这里你将学习 MCP 的核心构建块。我们会使用大量类比和可视化示例，确保这些概念自然易懂。

• **模块 2 - MCP 中的安全机制**：安全听起来可能令人望而生畏，但我们会向你展示 MCP 内置的安全特性，并教授从项目伊始就保护应用的实践方法。

### 🔨 构建阶段：创建你的第一个实现（模块 3）

现在真正的乐趣开始了！你将获得动手搭建实际 MCP 服务器和客户端的经验。别担心——我们从简单开始，并引导你完成每一步。

本模块包含多个动手指南，让你使用首选编程语言进行练习。你将创建自己的第一个服务器，编写客户端连接它，甚至集成到 VS Code 等主流开发工具中。

每个指南都提供完整的代码示例、故障排除技巧以及特定设计选择的原理解释。到此阶段结束时，你将拥有值得骄傲的 MCP 实现成果！

### 🚀 进阶阶段：高级概念与实战应用（模块 4-5）

掌握基础后，你已准备好探索更复杂的 MCP 功能。我们将涵盖实用的实施策略、调试技巧以及多模态 AI 集成等高级主题。

你还将学习如何为生产环境扩展你的 MCP 实现，并集成到 Azure 等云平台中。这些模块将为你构建能应对真实世界需求的大型 MCP 方案做好准备。

### 🌟 精通阶段：社区参与与专业化（模块 6-11）

最后阶段专注于加入 MCP 社区并在你感兴趣的领域深耕。你将学习如何为开源 MCP 项目做贡献、实现高级认证模式，以及构建集成数据库的综合解决方案。

特别值得一提的是模块 11——它是一条完整的 13 个实验的动手学习路径，教你使用 PostgreSQL 集成搭建生产级 MCP 服务器。这就像一门集大成之作，将整合你所学的一切！

### 📚 完整课程结构

| 模块 | 主题 | 描述 | 链接 |
|--------|-------|-------------|------|
| **模块 0-3：基础篇** | | | |
| 00 | MCP 简介 | Model Context Protocol 概述及其在 AI 管线中的重要性 | [阅读更多](./00-Introduction/README.md) |
| 01 | 核心概念详解 | 深入探索 MCP 核心概念 | [阅读更多](./01-CoreConcepts/README.md) |
| 02 | MCP 安全机制 | 安全风险与最佳实践 | [阅读更多](./02-Security/README.md) |
| 03 | MCP 入门指南 | 环境配置、基础服务器/客户端、集成方案 | [阅读更多](./03-GettingStarted/README.md) |
| **模块 3：搭建你的第一个服务器与客户端** | | | |
| 3.1 | 首个服务器 | 创建你的第一个 MCP 服务器 | [指南](./03-GettingStarted/01-first-server/README.md) |
| 3.2 | 首个客户端 | 开发基础 MCP 客户端 | [指南](./03-GettingStarted/02-client/README.md) |
| 3.3 | 集成 LLM 的客户端 | 集成大语言模型 | [指南](./03-GettingStarted/03-llm-client/README.md) |
| 3.4 | VS Code 集成 | 在 VS Code 中消费 MCP 服务器 | [指南](./03-GettingStarted/04-vscode/README.md) |
| 3.5 | stdio 服务器 | 使用 stdio 传输协议创建服务器 | [指南](./03-GettingStarted/05-stdio-server/README.md) |
| 3.6 | HTTP 流式传输 | 在 MCP 中实现 HTTP 流式传输 | [指南](./03-GettingStarted/06-http-streaming/README.md) |
| 3.7 | AI Toolkit | 将 AI Toolkit 与 MCP 结合使用 | [指南](./03-GettingStarted/07-aitk/README.md) |
| 3.8 | 测试 | 测试你的 MCP 服务器实现 | [指南](./03-GettingStarted/08-testing/README.md) |
| 3.9 | 部署 | 将 MCP 服务器部署至生产环境 | [指南](./03-GettingStarted/09-deployment/README.md) |
| 3.10 | 高级服务器用法 | 使用高级服务器实现进阶功能与优化架构 | [指南](./03-GettingStarted/10-advanced/README.md) |
| 3.11 | 基础认证 | 从入门开始展示认证机制及 RBAC | [指南](./03-GettingStarted/11-simple-auth/README.md) |
| 3.12 | MCP 宿主环境 | 配置 Claude Desktop、Cursor、Cline 及其他 MCP 宿主 | [指南](./03-GettingStarted/12-mcp-hosts/README.md) |
| 3.13 | MCP Inspector | 使用 Inspector 工具调试和测试 MCP 服务器 | [指南](./03-GettingStarted/13-mcp-inspector/README.md) |
| 3.14 | Sampling（采样） | 使用采样功能与客户端协作 | [指南](./03-GettingStarted/14-sampling/README.md) |
| 3.15 | MCP Apps | 构建 MCP 应用 | [指南](./03-GettingStarted/15-mcp-apps/README.md) |
| **模块 4-5：实战与进阶** | | | |
| 04 | 实际实施 | SDK、调试、测试、可复用提示词模板 | [阅读更多](./04-PracticalImplementation/README.md) |
| 4.1 | 分页处理 | 使用基于游标的分页处理大量结果集 | [指南](./04-PracticalImplementation/pagination/README.md) |
| 05 | MCP 高级主题 | 多模态 AI、扩展方案、企业级应用 | [阅读更多](./05-AdvancedTopics/README.md) |
| 5.1 | Azure 集成 | MCP 与 Azure 的集成方案 | [指南](./05-AdvancedTopics/mcp-integration/README.md) |
| 5.2 | 多模态处理 | 协同多种数据模态的工作方式 | [指南](./05-AdvancedTopics/mcp-multi-modality/README.md) |
| 5.3 | OAuth2 演示 | 实现 OAuth2 认证流程 | [指南](./05-AdvancedTopics/mcp-oauth2-demo/README.md) |
| 5.4 | Root Contexts（根上下文） | 理解并实现根上下文机制 | [指南](./05-AdvancedTopics/mcp-root-contexts/README.md) |
| 5.5 | 路由策略 | MCP 路由策略 | [指南](./05-AdvancedTopics/mcp-routing/README.md) |
| 5.6 | Sampling（采样） | MCP 中的采样技术 | [指南](./05-AdvancedTopics/mcp-sampling/README.md) |
| 5.7 | 扩展方案 | 规模化部署 MCP 实现 | [指南](./05-AdvancedTopics/mcp-scaling/README.md) |
| 5.8 | 安全机制 | 高级安全考量 | [指南](./05-AdvancedTopics/mcp-security/README.md) |
| 5.9 | 网页搜索 | 实现网页搜索能力 | [指南](./05-AdvancedTopics/web-search-mcp/README.md) |
| 5.10 | 实时流式传输 | 构建实时流式功能 | [指南](./05-AdvancedTopics/mcp-realtimestreaming/README.md) |
| 5.11 | 实时搜索 | 实现实时搜索能力 | [指南](./05-AdvancedTopics/mcp-realtimesearch/README.md) |
| 5.12 | Entra ID 认证 | 使用 Microsoft Entra ID 进行身份验证 | [指南](./05-AdvancedTopics/mcp-security-entra/README.md) |
| 5.13 | Foundry 集成 | 与 Azure AI Foundry 集成 | [指南](./05-AdvancedTopics/mcp-foundry-agent-integration/README.md) |
| 5.14 | 上下文工程（Context Engineering） | 高效上下文工程的实用技巧 | [指南](./05-AdvancedTopics/mcp-contextengineering/README.md) |
| 5.15 | MCP 自定义传输 | 自定义 Transport 实现方案 | [指南](./05-AdvancedTopics/mcp-transport/README.md) |
| 5.16 | 协议特性 | 进度通知、取消机制、资源模板 | [指南](./05-AdvancedTopics/mcp-protocol-features/README.md) |
| 5.17 | 对抗性多智能体推理 | 两个智能体使用共享 MCP 工具进行对立辩论，由裁判智能体评估 | [指南](./05-AdvancedTopics/mcp-adversarial-agents/README.md) |
| **模块 6-10：社区与最佳实践** | | | |
| 06 | 社区贡献 | 如何为 MCP 生态贡献力量 | [指南](./06-CommunityContributions/README.md) |
| 07 | 早期采用经验谈 | 真实世界的实施案例分享 | [指南](./07-LessonsfromEarlyAdoption/README.md) |
| 08 | MCP 最佳实践 | 性能优化、容错机制与韧性设计 | [指南](./08-BestPractices/README.md) |
| 09 | MCP 案例研究 | 实际实施示例解析 | [指南](./09-CaseStudy/README.md) |
| 10 | 动手工作坊 | 使用 AI Toolkit 构建 MCP 服务器 | [实验](./10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) |
| **模块 11：MCP 服务器实战实验室** | | | |
| 11 | MCP 服务器数据库集成 | 面向 PostgreSQL 集成的完整 13 个实验学习路径 | [实验](./11-MCPServerHandsOnLabs/README.md) |
| 11.1 | 简介 | 结合数据库集成与零售分析用例的 MCP 概述 | [实验 00](./11-MCPServerHandsOnLabs/00-Introduction/README.md) |
| 11.2 | 核心架构 | 理解 MCP 服务器架构、数据库层与安全模式 | [实验 01](./11-MCPServerHandsOnLabs/01-Architecture/README.md) |
| 11.3 | 安全与多租户 | 行级安全性（RLS）、认证与多租户数据访问 | [实验 02](./11-MCPServerHandsOnLabs/02-Security/README.md) |
| 11.4 | 环境配置 | 搭建开发环境、Docker 及 Azure 资源 | [实验 03](./11-MCPServerHandsOnLabs/03-Setup/README.md) |
| 11.5 | 数据库设计 | PostgreSQL 配置、零售业务模式设计与示例数据 | [实验 04](./11-MCPServerHandsOnLabs/04-Database/README.md) |
| 11.6 | MCP 服务器实现 | 使用 FastMCP 构建集成数据库的服务器 | [实验 05](./11-MCPServerHandsOnLabs/05-MCP-Server/README.md) |
| 11.7 | 工具开发 | 创建数据库查询工具与模式自省功能 | [实验 06](./11-MCPServerHandsOnLabs/06-Tools/README.md) |
| 11.8 | 语义搜索 | 结合 Azure OpenAI 与 pgvector 实现向量嵌入 | [实验 07](./11-MCPServerHandsOnLabs/07-Semantic-Search/README.md) |
| 11.9 | 测试与调试 | 测试策略、调试工具与验证方法 | [实验 08](./11-MCPServerHandsOnLabs/08-Testing/README.md) |
| 11.10 | VS Code 集成 | 配置 VS Code MCP 集成与 AI Chat 使用方式 | [实验 09](./11-MCPServerHandsOnLabs/09-VS-Code/README.md) |
| 11.11 | 部署策略 | Docker 部署、Azure Container Apps 及扩展考量 | [实验 10](./11-MCPServerHandsOnLabs/10-Deployment/README.md) |
| 11.12 | 监控告警 | Application Insights、日志记录与性能监控 | [实验 11](./11-MCPServerHandsOnLabs/11-Monitoring/README.md) |
| 11.13 | 最佳实践 | 性能优化、安全加固与生产环境建议 | [实验 12](./11-MCPServerHandsOnLabs/12-Best-Practices/README.md) |

### 💻 示例代码项目

学习 MCP 最令人兴奋的部分之一，就是看到你的编码能力逐步提升。我们的代码示例设计为从简单开始，随着你理解的深入逐渐增加复杂度。以下是我们引入概念的方式——代码易于理解但能体现真实的 MCP 原理。你将不仅明白这段代码在做什么，还会了解它为何这样设计以及如何融入更大的 MCP 应用中。

#### 基础 MCP 计算器示例

| 语言 | 描述 | 链接 |
|----------|-------------|------|
| C# | MCP 服务器示例 | [查看代码](./03-GettingStarted/samples/csharp/README.md) |
| Java | MCP 计算器 | [查看代码](./03-GettingStarted/samples/java/calculator/README.md) |
| JavaScript | MCP 演示 | [查看代码](./03-GettingStarted/samples/javascript/README.md) |
| Python | MCP 服务器 | [查看代码](./03-GettingStarted/samples/python/mcp_calculator_server.py) |
| TypeScript | MCP 示例 | [查看代码](./03-GettingStarted/samples/typescript/README.md) |
| Rust | MCP 示例 | [查看代码](./03-GettingStarted/samples/rust/README.md) |

#### 高级 MCP 实现方案

| 语言 | 描述 | 链接 |
|----------|-------------|------|
| C# | 高级示例 | [查看代码](./04-PracticalImplementation/samples/csharp/README.md) |
| Java with Spring | Container App 示例 | [查看代码](./04-PracticalImplementation/samples/java/containerapp/README.md) |
| JavaScript | 高级示例 | [查看代码](./04-PracticalImplementation/samples/javascript/README.md) |
| Python | 复杂实现方案 | [查看代码](./04-PracticalImplementation/samples/python/README.md) |
| TypeScript | Container 示例 | [查看代码](./04-PracticalImplementation/samples/typescript/README.md) |


## 🎯 MCP 学习前置要求

为了充分利用本课程，建议你具备以下条件：

- 至少掌握以下语言之一的基础编程知识：C#、Java、JavaScript、Python 或 TypeScript
- 理解客户端-服务器模型与 API 概念
- 熟悉 REST 和 HTTP 基础概念
- （可选）具备 AI/ML 相关背景知识

- 加入我们的社区讨论以获取支持

## 📚 学习指南与资源

本仓库包含多项资源，帮助你高效导航并深入学习：

### 学习指南

我们提供了一份详细的 [学习指南](./study_guide.md)，助你有效利用本仓库。这份可视化课程地图展示了所有主题的关联方式，并提供如何充分利用示例项目的指导。对于喜欢宏观视角的视觉型学习者来说尤其有帮助。

该指南包含：
- 展示所有覆盖主题的课程地图
- 各仓库模块的详细拆解说明
- 示例项目使用建议
- 针对不同技能水平的推荐学习路径
- 补充学习资料以丰富你的学习体验

### 更新日志（Changelog）

我们维护着详细的 [更新日志](./changelog.md)，记录课程材料的所有重要变更，助你随时掌握最新改进与新增内容：
- 新内容添加
- 结构调整
- 功能优化
- 文档更新

## 🛠️ 如何高效使用本课程

本指南中的每个章节均包含以下内容：

1. MCP 概念的清晰解释  
2. 多语言实时代码示例  
3. 用于构建真实 MCP 应用的练习题  
4. 面向进阶学习者的额外资源

### 让我们用 C# 学习 MCP - 教程系列
了解 Model Context Protocol（MCP），这是一个旨在标准化 AI 模型与客户端应用交互的前沿框架。通过这套对初学者友好的课程，我们将带你入门 MCP，并指导你搭建第一个 MCP 服务器。
#### C#：[https://aka.ms/letslearnmcp-csharp](https://aka.ms/letslearnmcp-csharp)
#### Java：[https://aka.ms/letslearnmcp-java](https://aka.ms/letslearnmcp-java)
#### JavaScript：[https://aka.ms/letslearnmcp-javascript](https://aka.ms/letslearnmcp-javascript)
#### Python：[https://aka.ms/letslearnmcp-python](https://aka.ms/letslearnmcp-python)

## 🎓 你的 MCP 之旅由此开始

恭喜！你已经迈出了拓展编程能力、接轨 AI 开发前沿的激动人心的第一步。

### 你已取得的成就

通过阅读本简介，你已经开始构建自己的 MCP 知识体系。你现在已经了解 MCP 是什么、为何重要，以及本课程将如何支持你的学习旅程。这是一项重要的成果，也是你在这一关键技术领域专业能力的起点。

### 前方的冒险

随着你推进各个模块的学习，请记住：每位专家都曾是从零开始的新手。现在看似复杂的概念，在反复练习与应用后将成为你的本能反应。每一步微小的积累都将汇聚成强大的能力，伴随你的整个开发职业生涯。

### 你的支持网络

你正加入一个由热爱 MCP 并乐于助人的学习者与专家组成的社区。无论你是卡在某个编码难题上，还是兴奋于自己的突破进展，这个社区都会全程支持你的学习之旅。

如果你在构建 AI 应用时遇到困难或有任何疑问，欢迎加入讨论区与其他学习者和资深开发者交流。这是一个充满支持的社区，欢迎提问并自由分享知识。

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果你有产品反馈或在构建过程中发现错误，请访问：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

### 准备好开始了吗？

你的 MCP 冒险现在正式开始！从模块 0 入手，开启你的第一次动手实践；或者浏览示例项目，看看你即将构建的内容。请记住——每位专家都始于你现在所在的位置，只要保持耐心并多加练习，你将惊讶于自己能够取得的成就。

欢迎来到 Model Context Protocol 开发的世界。让我们一起打造令人惊叹的作品吧！

## 🤝 为学习社区贡献力量

本课程因像你这样的学习者贡献而日益强大！无论是修复拼写错误、建议更清晰的解释，还是添加新示例，你的贡献都将帮助其他初学者取得成功。

感谢微软价值专业人士 [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) 对代码示例的贡献。

本项目的提交流程旨在保持友好与支持性。大多数贡献需要签署贡献者许可协议（CLA），但自动化工具将引导你顺利完成流程。

## 📜 开源学习

本课程全部内容基于 MIT [许可证](./LICENSE) 发布，意味着你可以自由使用、修改和分享它。这支持了我们让 MCP 知识惠及全球开发者的使命。
## 🤝 贡献指南

本项目欢迎各类贡献与建议。大多数情况下，你需要同意一份
贡献者许可协议（CLA），声明你有权且实际授予我们
使用你贡献内容的权利。详情请访问 <https://cla.opensource.microsoft.com>。

当你提交 Pull Request 时，CLA Bot 将自动判断你是否需要提供 CLA，并相应地装饰 PR（例如：状态检查、评论）。只需遵循机器人提供的指示操作即可。通过我们的 CLA 后，你在所有使用该协议的仓库中仅需执行一次此流程。

本项目已采用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
更多信息请参阅 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或
就其他问题与意见联系 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

---

*准备好开始你的 MCP 之旅了吗？从 [模块 00 - MCP 简介](./00-Introduction/README.md) 开始，迈出你在 Model Context Protocol 开发世界的第一步！*



## 🎒 其他课程
我们的团队还推出了许多其他课程！欢迎查看：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->