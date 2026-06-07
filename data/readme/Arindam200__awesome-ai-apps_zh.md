![Banner](/assets/banner_new.png)

<div align="center">

# Awesome AI Apps [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<a href="https://trendshift.io/repositories/14662" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14662" alt="Arindam200%2Fawesome-ai-apps | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

本仓库是一个全面的合集，包含**80多个实用示例、教程和配方**，用于构建强大的 LLM 驱动应用——涵盖文本智能体、语音助手、RAG 应用以及基于 MCP 的工具。这些项目可作为开发者使用各种 AI 框架和技术栈的指南。

## 📋 目录

- [🎓 课程](#-courses)
- [🚀 精选 AI 应用](#-featured-ai-apps)
  - [🧩 入门级智能体](#-starter-agents)
  - [🪶 基础智能体](#-simple-agents)
  - [🎙️ 语音智能体](#-voice-agents)
  - [🗂️ MCP 智能体](#️-mcp-agents)
  - [🧠 记忆型智能体](#-memory-agents)
  - [📚 RAG 应用](#-rag-applications)
  - [🔬 高级智能体](#-advanced-agents)
- [📺 教程与视频](#-tutorials--videos)
- [🚀 快速开始](#getting-started)
- [🤝 贡献指南](#-contributing)

---

<div align="center">

## 💎 赞助商

<p align="center">
  衷心感谢各位赞助商的慷慨支持！
</p>

<table align="center" cellpadding="10" style="width:100%; border-collapse:collapse;">
  <tr align="center">
    <td width="300" valign="middle" align="center">
      <a href="https://dub.sh/brightdata" target="_blank" title="Visit Bright Data">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/brightdata/logo/light.svg" height="35" style="max-width:180px;" alt="Bright Data - Web Data Platform">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">网页数据平台</span>
        <br>
        <a href="https://dub.sh/brightdata" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit Bright Data website">
        </a>
      </sub>
    </td>
    <td width="300" valign="middle" align="center">
      <a href="https://dub.sh/nebius" target="_blank" title="Visit Nebius Token Factory">
        <img src="./assets/nebius.png" height="36" style="max-width:180px;" alt="Nebius Token Factory">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">AI 推理提供商</span>
        <br>
        <a href="https://dub.sh/nebius" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit Nebius Token Factory">
        </a>
      </sub>
    </td>
    <td width="300" valign="middle" align="center">
      <a href="https://dub.sh/scrapegraphai" target="_blank" title="Visit ScrapeGraphAI on GitHub">
        <img src="https://raw.githubusercontent.com/ScrapeGraphAI/ScrapeGraph-AI/main/docs/assets/scrapegraphai_logo.png" height="44" style="max-width:180px;" alt="ScrapeGraphAI - Web Scraping Library">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">AI 网络爬虫框架</span>
        <br>
        <a href="https://dub.sh/scrapegraphai" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="View ScrapeGraphAI on GitHub">
        </a>
      </sub>
    </td>
  </tr>
  <tr align="center">
    <td width="300" valign="middle" align="center">
      <a href="https://dub.sh/memorilabs" target="_blank" title="Visit Memorilabs">
        <img src="assets/memori.png" height="36" style="max-width:180px;" alt="Memori - SQL Native Memory for AI">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">面向 AI 的 SQL 原生内存</span>
        <br>
        <a href="https://dub.sh/memorilabs" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit Memorilabs website">
        </a>
      </sub>
    </td>
    <td width="300" valign="middle" align="center">
      <a href="https://dub.sh/copilotkit" target="_blank" title="Visit CopilotKit">
        <img src="assets/copilot-kit-logo.svg" height="36" style="max-width:180px;" alt="CopilotKit - Agentic Application Platform">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">智能体应用平台</span>
        <br>
        <a href="https://dub.sh/copilotkit" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit CopilotKit website">
        </a>
      </sub>
    </td>
    <td width="300" valign="middle" align="center">
      <a href="https://dub.sh/scalekitt" target="_blank" title="Visit ScaleKit">
        <img src="assets/scalekit.svg" height="36" style="max-width:180px;" alt="ScaleKit - Auth Stack for AI">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">面向 AI 的身份认证栈</span>
        <br>
        <a href="https://dub.sh/scalekitt" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit ScaleKit website">
        </a>
      </sub>
    </td>
  </tr>
  <tr align="center">
    <td width="200" valign="middle" align="center">
      <a href="https://okahu.ai" target="_blank" title="Visit Okahu">
        <img src="assets/okahu.png" height="36" style="max-width:180px;" alt="Okahu - AI Platform">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">AI 可观测性平台</span>
        <br>
        <a href="https://okahu.ai" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit Okahu website">
        </a>
      </sub>
    </td>
    <td width="200" valign="middle" align="center">
      <a href="https://dub.sh/serpApi" target="_blank" title="Visit SerpApi">
        <img src="assets/serpapi.png" height="36" style="max-width:180px;" alt="SerpApi - Google Search API">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">Google 搜索 API</span>
        <br>
        <a href="https://dub.sh/serpApi" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit SerpApi website">
        </a>
      </sub>
    </td>
    <td width="200" valign="middle" align="center">
      <a href="https://dub.sh/agentfield" target="_blank" title="Visit AgentField">
        <img src="assets/agentfield.png" height="40" style="max-width:180px;" alt="AgentField - Kubernetes for AI Agents">
      </a>
      <br>
      <sub>
        <span style="white-space:nowrap;">面向 AI 智能体的 Kubernetes</span>
        <br>
        <a href="https://dub.sh/agentfield" target="_blank">
          <img src="https://img.shields.io/badge/Visit%20Site-blue?style=flat-square" alt="Visit AgentField website">
        </a>
      </sub>
    </td>
  </tr>

   

</table>

### 💎 成为赞助商

<p align="center">
有兴趣赞助本项目？欢迎随时联系！
<br/>
<a href="https://dub.sh/arindam-linkedin" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<a href="mailto:arindammajumder2020@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
</a>
</p>

</div>

---

## 🎓 课程

### AWS Strands 初学者课程

**全面的 AWS Strands SDK 构建 AI 智能体实战课程：**

- [**AWS Strands 课程**](course/aws_strands) - 完整的 8 课时课程，涵盖从基础概念到生产级模式的全面内容
  - **基础篇**：基础智能体、会话管理、结构化输出
  - **集成篇**：MCP 智能体、人在回路（Human-in-the-Loop）模式
  - **多智能体篇**：编排器智能体、群体智能、图工作流
  - **生产篇**：可观测性、安全护栏与最佳实践

## 🚀 精选 AI 应用

### 🧩 入门级智能体

**用于学习和扩展不同 AI 框架的快速启动智能体。** _19 个项目_

- [Agno HackerNews 分析](starter_ai_agents/agno_starter) - 基于 Agno 的智能体，用于 HackerNews 趋势分析
- [OpenAI SDK 入门](starter_ai_agents/openai_agents_sdk) - OpenAI Agents SDK，附带邮件助手与 haiku 诗人示例
- [LlamaIndex 任务管理器](starter_ai_agents/llamaindex_starter) - 基于 LlamaIndex 的任务辅助智能体
- [CrewAI 研究团队](starter_ai_agents/crewai_starter) - 多智能体研究团队协作示例
- [Letta 入门](starter_ai_agents/letta_starter) - 具备跨会话持久化长期记忆的状态保持型智能体
- [PydanticAI 天气机器人](starter_ai_agents/pydantic_starter) - 实时天气信息查询智能体
- [LangChain 入门](starter_ai_agents/langchain_starter) - 基于 Nebius 的 LangChain 工具调用智能体，使用 `create_tool_calling_agent` + `AgentExecutor`
- [LangGraph 入门](starter_ai_agents/langgraph_starter) - 基于 Nebius 的 LangGraph 预构建 ReAct 智能体（`create_react_agent`），支持自定义工具
- [AWS Strands 智能体入门](starter_ai_agents/aws_strands_starter) - 使用 AWS Strands SDK 的天气报告智能体
- [Mastra 入门](starter_ai_agents/mastra_starter) - TypeScript 优先的智能体，附带由 Nebius Token Factory 支持的自定义工具
- [Camel AI 入门](starter_ai_agents/camel_ai_starter) - 用于对比评估各类 AI 模型的性能基准测试工具
- [DSPy 入门](starter_ai_agents/dspy_starter) - 用于构建和优化 AI 系统的 DSPy 框架
- [Google ADK 入门](starter_ai_agents/google_adk_starter) - Google Agent Development Kit 起始模板
- [Semantic Kernel 入门](starter_ai_agents/semantic_kernel_starter) - Microsoft Semantic Kernel `ChatCompletionAgent`，支持基于插件的工具调用
- [smolagents 入门](starter_ai_agents/smolagents_starter) - Hugging Face smolagents 代码优先的网络搜索智能体
- [AutoGen 入门](starter_ai_agents/autogen_starter) - Microsoft AutoGen `AssistantAgent`，附带由 Nebius Token Factory 支持的自定义工具
- [cagent 入门](starter_ai_agents/cagent_starter) - Docker 开源的可定制多智能体运行时框架
- [Sayna 语音智能体](starter_ai_agents/sayna_starter) - 实时语音基础设施，支持多提供商 STT/TTS（Deepgram、ElevenLabs、Azure、Google）及 WebSocket 流式传输
- [KAOS 入门](starter_ai_agents/kaos_starter) - Kubernetes 原生的多智能体系统，内置 MCP 工具与集群内 LLM

### 🪶 基础智能体

**简单直接、面向日常 AI 应用的实用案例。** _19 个项目_

- [Agno AI 示例](simple_ai_agents/agno_ai_examples) - 从单智能体到多智能体的简易示例，支持网页搜索与知识库
- [金融分析智能体](simple_ai_agents/finance_agent) - 实时股票与市场数据追踪智能体
- [人在回路（HITL）智能体](simple_ai_agents/human_in_the_loop_agent) - 用于安全执行 AI 任务的人机协同操作
- [新闻通讯生成器](simple_ai_agents/newsletter_agent) - 集成 Firecrawl 的 AI 驱动简报构建工具
- [推理演示智能体](simple_ai_agents/reasoning_agent) - 逐步财务逻辑推理演示
- [Agno UI 示例](simple_ai_agents/agno_ui_agent) - 面向网页与金融智能体的交互式界面
- [Mastra 天气机器人](simple_ai_agents/mastra_ai_weather_agent) - 基于 Mastra AI 框架的天气更新服务
- [日历助手](simple_ai_agents/cal_scheduling_agent) - 集成 Cal.com 的日程安排功能
- [智能调度助手](simple_ai_agents/email_to_calendar_scheduler) - AI 驱动的 Gmail 阅读器与 Google Calendar 管理器
- [网页自动化智能体](simple_ai_agents/browser_agent) - 基于 Nebius 与 browser-use 的浏览器自动化智能体
- [Nebius Chat](simple_ai_agents/nebius_chat) - Nebius Token Factory 聊天界面
- [RouteLLM 聊天](simple_ai_agents/llm_router) - 使用 RouteLLM 进行智能模型路由（GPT-4o-mini vs Nebius Llama），以优化成本
- [对话数据库](simple_ai_agents/talk_to_db) - 基于 GibsonAI 与 LangChain 的自然语言数据库查询工具
- [LangChain 基础智能体](simple_ai_agents/langchain_simple_agents) - 基于 Nebius 的事件响应、客服、供应商风险与数据质量智能体，支持类型化输出与安全工具限制
- [智能体发现助手](simple_ai_agents/agent_discovery_agent) - 跨 NANDA、MCP、Virtuals、A2A 和 ERC-8004 注册表查找并对比 AI 智能体
- [LangChain 数据智能体 PoC](simple_ai_agents/langchain_data_agent_poc) - 基于 LangGraph、Nebius 的 NL2SQL 数据智能体，内置只读 SQL 安全限制与 Streamlit 图表展示
- [VoyageCompass 旅行规划师](simple_ai_agents/nebius_travel_planner) - 基于 LangChain 和 Nebius 的旅行规划工具，集成天气、研究、货币换算、预算与打包建议功能

### 🎙️ 语音智能体

**实时语音助手与流式语音处理管道。** _8 个项目_

- [Gradium + Nebius 语音教练](voice_agents/voice-agent-gradium-nebius-langchain) - 结合 Gradium STT/TTS、LangChain 编排与 Nebius 推理的对话式演讲教练
- [医疗客服联络中心](voice_agents/healthcare_contact_center) - 基于 Pipecat 的医疗客服系统，支持预约预订、FAQ 处理与主管升级转接
- [LiveKit + Gemini 实时语音](voice_agents/livekit_gemini_agents) - LiveKit Agents 结合 Google Gemini Live（`gemini` 多模态实时），用于 LiveKit 房间内的低延迟语音对话
- [带网页搜索的 LiveKit 语音智能体](voice_agents/livekit_web_search_agent) - LiveKit + Gemini 实时语音智能体，集成 Olostep 驱动的 `web_search` 工具，提供新鲜且带来源引用的答案
- [LiveKit RSVP 确认智能体](voice_agents/livekit_rsvp_agent) - 外呼语音智能体，自动拨打参会者电话、确认出席状态并更新基于 JSON 的活动数据库
- [Pipecat + Sarvam 语音管道](voice_agents/pipecat_agent) - Pipecat 语音处理管道，集成 Sarvam STT/TTS 与 OpenAI 对话能力；支持通过 Pipecat Runner 使用 WebRTC（浏览器）或 Daily 传输通道
- [极速线索响应语音智能体](voice_layers/speed_to_lead_agent) - 基于 LiveKit 的语音智能体，实时接听入站线索、路由至专家并记录至模拟 CRM
- [VoxCode（Cursor 代码编辑器）](voice_agents/Cursor_code_editor) - 本地化语音工作区，用于代码库摘要与架构问答；集成 Deepgram Voice Agent + Nebius 推理 + Cursor SDK 文件检查/编辑功能

### 🗂️ MCP 智能体

**使用模型上下文协议（MCP）进行外部工具集成的示例。** _13 个项目_

- [Doc-MCP](mcp_ai_agents/doc_mcp) - 语义化 RAG 文档问答系统
- [LangGraph MCP 智能体](mcp_ai_agents/langchain_langgraph_mcp_agent) - 集成 Couchbase 的 LangChain ReAct 智能体
- [GitHub MCP 智能体](mcp_ai_agents/github_mcp_agent) - 通过 MCP 提供仓库洞察与分析功能
- [MCP 入门模板](mcp_ai_agents/mcp_starter) - GitHub 仓库分析器起始模板
- [对话文档助手](mcp_ai_agents/docs_qna_agent) - 基于 MCP 的文档问答智能体
- [数据库 MCP 智能体](mcp_ai_agents/database_mcp_agent) - 用于管理 GibsonAI 数据库项目与架构的对话式 AI 智能体
- [酒店搜索智能体](mcp_ai_agents/hotel_finder_agent) - 集成 MCP 的酒店搜索与预订工具
- [自定义 MCP 服务器](mcp_ai_agents/custom_mcp_server) - 自定义 MCP 服务端实现示例
- [Couchbase MCP 服务器](mcp_ai_agents/couchbase_mcp_server) - 基于 MCP 协议的 Couchbase 数据库集成方案
- [ScaleKit Exa MCP 安全集成](mcp_ai_agents/scalekit-exa-mcp-security) - 结合 Exa 搜索的安全导向型 MCP 集成示例
- [Docker E2B MCP 智能体](mcp_ai_agents/e2b_docker_mcp_agent) - 通过 MCP Gateway 在沙箱化 Docker 环境中安全运行智能体的工具
- [Taskade MCP 智能体](mcp_ai_agents/taskade_mcp_agent) - AI 驱动的工作区管理助手，支持通过 Taskade MCP 管理项目、任务与工作流
- [Telemetry MCP Okahu](mcp_ai_agents/telemetry-mcp-okahu) - 基于托管式 MCP 与 Okahu Cloud 追踪的自愈型 Text-to-SQL 演示

### 🧠 记忆型智能体

**具备高级记忆能力，用于上下文保持与个性化定制的智能体。** _12 个项目_

- [Agno 记忆智能体](memory_agents/agno_memory_agent) - 基于 Agno 且支持持久化记忆能力的智能体
- [arXiv 研究员智能体（集成 Memori）](memory_agents/arxiv_researcher_agent_with_memori) - 结合 OpenAI Agents 与 GibsonAI Memori 的研究助手
- [AWS Strands 记忆智能体（集成 Memori）](memory_agents/aws_strands_agent_with_memori) - 增强 Memori 记忆系统的 AWS Strands 智能体
- [博客写作智能体](memory_agents/blog_writing_agent) - 具备风格一致性记忆的个性化博客撰写助手
- [社交媒体运营智能体](memory_agents/social_media_agent) - 具备品牌语调记忆的社媒自动化助手
- [求职搜索智能体](memory_agents/job_search_agent) - 支持偏好追踪的记忆型求职助手
- [品牌声誉监控器](memory_agents/brand_reputation_monitor) - AI 驱动的品牌声誉监控系统，集成新闻分析与情感追踪
- [产品发布分析智能体](memory_agents/product_launch_agent) - 用于分析竞品动态的竞争性情报工具
- [AI 顾问智能体](memory_agents/ai_consultant_agent/) - 使用 **Memori v3** 作为长期记忆层与 **ExaAI** 进行研究的 AI 咨询助手
- [客服语音智能体](memory_agents/customer_support_voice_agent) - 支持 Memori v3 与 Firecrawl（知识库管理）的语音版客服助手
- [YouTube 趋势分析智能体](memory_agents/youtube_trend_agent) - 结合 Memori、Agno 与 Exa 的 YouTube 频道分析与视频创意推荐工具
- [学习教练智能体](memory_agents/study_coach_agent) - AI 驱动的学习辅导助手，集成 Memori v3 与 LangGraph，支持多步骤理解验证

### 📚 RAG 应用

**面向文档理解与知识库的检索增强生成（RAG）示例。** _12 个项目_

- [Agentic RAG](rag_apps/agentic_rag) - 结合 Agno 与 GPT-5 的智能体化 RAG 实现
- [带网页搜索的 Agentic RAG](rag_apps/agentic_rag_with_web_search) - 结合 CrewAI、Qdrant 与 Exa 的高级 RAG，支持混合搜索能力
- [简历优化器](rag_apps/resume_optimizer) - AI 驱动的简历优化与增强工具
- [LlamaIndex RAG 入门模板](rag_apps/llamaIndex_starter) - LlamaIndex + Nebius RAG 起始模板
- [PDF RAG 分析器](rag_apps/pdf_rag_analyser) - 支持多 PDF 对话与分析的系统
- [Qwen3 RAG 聊天](rag_apps/qwen3_rag) - 基于 Streamlit 构建的 PDF 问答界面
- [代码对话助手](rag_apps/chat_with_code) - 交互式代码探索与文档辅助工具
- [Gemma3 OCR 处理](rag_apps/gemma_ocr/) - 使用 Gemma3 模型的 OCR 文档与图像处理工具
- [Nvidia Nemotron OCR 解析](rag_apps/nvidia_ocr/) - 基于 Nvidia Nemotron-Nano-V2-12b 的文档与图像 OCR 解析器
- [Contextual AI RAG](rag_apps/contextual_ai_rag) - 企业级 RAG，支持托管数据存储与质量评估
- [高级 RAG（含重排序）](rag_apps/advanced_rag_with_reranking) - 生产级 PDF RAG，集成上下文检索、Qdrant 混合搜索、结果重排、流式输出、上传解析与可点击引用功能
- [基础 RAG](rag_apps/simple_rag) - 基于 Nebius 的快速入门基础 RAG 实现
- [WFGY 16 问题地图 LLM 调试器](rag_apps/wfgy_llm_debugger) - 基于 16 模式映射的 LLM 与 RAG 缺陷调试工具

### 🔬 高级智能体

**用于生产级端到端工作流的复杂多智能体管道。** _21 个项目_

- [深度研究 + 写作智能体工作坊](advance_ai_agents/deep_research_writing_agents_nebius_okahu) - 基于 Nebius 的 LangChain MCP 工作坊，集成 Exa 研究、Gemini 图像生成与 Okahu/Monocle 评估可观测性
- [Nebius AutoResearch](advance_ai_agents/nebius-autoresearch-autoresearch-mar30) - NYC 出租车数据分析管道优化器；结合 Nebius Token Factory（实时或批量推理）的迭代代码搜索功能
- [AgentField 金融研究智能体](advance_ai_agents/agentfield_finance_research_agent) - 基于 AgentField 的金融研究助手
- [尽职调查智能体](advance_ai_agents/due_diligence_agent) - 结合 AG2 与 TinyFish 深度网页爬取的多公司尽调管道
- [深度研究员](advance_ai_agents/deep_researcher_agent) - 多阶段研究流程，集成 Agno 与 ScrapeGraph AI
- [候选人分析器](advance_ai_agents/candidate_analyser) - GitHub/LinkedIn 个人资料综合分析工具
- [Cosmos Arena 辩论委员会](advance_ai_agents/cosmos_arena_debate_council) - 基于 LangGraph 与 NVIDIA Cosmos 推理模型（通过 Nebius Token Factory）构建的多智能体辩论系统
- [求职助手](advance_ai_agents/job_finder_agent) - 结合 Bright Data 的 LinkedIn 职位搜索自动化方案
- [AI 趋势分析器](advance_ai_agents/trend_analyzer_agent) - 基于 Google ADK 的 AI 趋势挖掘与分析工具
- [会议演讲摘要生成器](advance_ai_agents/conference_talk_abstract_generator) - 结合 Google ADK 与 Couchbase 的自动化演讲摘要生成系统
- [金融服务智能体](advance_ai_agents/finance_service_agent) - 基于 Agno 的股票数据与预测 FastAPI 服务后端
- [价格监控智能体](advance_ai_agents/price_monitoring_agent) - 基于 CrewAI、Twilio & Nebius 的价格监控与告警工具
- [创业点子验证器](advance_ai_agents/startup_idea_validator_agent) - 用于验证与分析创业构想的 Agentic 工作流
- [会议助手智能体](advance_ai_agents/meeting_assistant_agent) - 自动从对话中提取会议纪要并生成任务清单
- [AI 对冲基金](advance_ai_agents/ai-hedgefund) - 综合财务分析的 Agentic 工作流
- [智能 GTM（市场进入）智能体](advance_ai_agents/smart_gtm_agent) - 市场进入策略与竞品分析助手
- [会议提案生成器（通用型）](advance_ai_agents/conference_agnositc_cfp_generator) - 自动化会议投稿提案生成系统
- [二手车推荐助手](advance_ai_agents/car_finder_agent) - 结合 CrewAI 与 MongoDB 的 AI 驱动二手车推荐系统
- [内容团队智能体](advance_ai_agents/content_team_agent) - SEO 内容优化工作流，集成 Agno & SerpAPI 提升 Google AI Search 排名
- [客服解决智能体](advance_ai_agents/customer_support_resolution_agent) - 基于 LangChain 和 Nebius 的客服助手，支持知识库检索、订单查询与人工工单升级
- [Temporal 智能体示例](advance_ai_agents/temporal_agents/) - 基于 Temporal 框架的 AI 智能体实现示例

## 📺 教程与视频

### 🎓 课程合集

- [**AWS Strands 课程**](https://www.youtube.com/playlist?list=PLMZM1DAlf0Lrc43ZtUXAwYu9DhnqxzRKZ) - 完整的 8 课时课程，讲解如何使用 AWS Strands SDK 构建 AI 智能体

### 🔧 框架教程

- [**使用 MCP 构建应用**](https://www.youtube.com/playlist?list=PLMZM1DAlf0Lolxax4L2HS54Me8gn1gkz4) - 模型上下文协议（Model Context Protocol）教程与示例
- [**开发 AI 智能体**](https://www.youtube.com/playlist?list=PLMZM1DAlf0LqixhAG9BDk4O_FjqnaogK8) - 通用 AI 智能体开发教程
- [**AI 智能体、MCP 及其他...**](https://www.youtube.com/playlist?list=PL2ambAOfYA6-LDz0KpVKu9vJKAqhv0KKI) - 混合教程与项目演示

---

<div align="center">

## 📥 每日获取 AI 洞察！

获取易于理解的每周教程，深入探讨 AI、LLM 及智能体框架。非常适合希望学习、构建并保持技术前沿的开发者。订阅我们的通讯！

[![Subscribe to our Newsletter](https://github.com/user-attachments/assets/990d1947-337b-4e87-a7e6-e619ec19dee6)](https://mranand.substack.com/subscribe)

</div>

---

## 快速开始

### 前置条件

- **Python 3.10+**（较新项目推荐使用 Python 3.11+）
- **Git**：用于克隆仓库
- **包管理器**：`pip` 或 `uv`（推荐，安装速度更快）
- **API Keys**：大多数项目需要配置 API 密钥（详见各子项目的 README）

### 快速启动步骤

1. **克隆仓库**

   ```bash
   git clone https://github.com/Arindam200/awesome-ai-apps.git
   cd awesome-ai-apps
   ```

2. **选择项目并进入目录**

   ```bash
   cd starter_ai_agents/agno_starter  # 示例：从 Agno 入门项目开始
   ```

3. **配置环境变量**

   ```bash
   cp .env.example .env  # 复制示例环境文件
   # 编辑 .env 填入你的 API Keys
   ```

4. **安装依赖**

   ```bash
   # 使用 pip
   pip install -r requirements.txt

   # 或使用 uv（推荐，速度更快）
   uv sync
   # 或
   uv pip install -e .
   ```

5. **运行项目**

   ```bash
   python main.py
   # 或对于 Streamlit 应用
   streamlit run app.py
   ```

## 🤝 贡献指南

我们欢迎社区成员的贡献！你可以通过以下方式提供帮助：

- 🐛 **报告 Bug** 或通过 [GitHub Issues](https://github.com/Arindam200/awesome-ai-apps/issues) 提出改进建议
- 💡 **提交新项目** - 分享你自己的 AI 智能体示例
- 📝 **完善文档** - 帮助项目更易上手
- 🔧 **修复问题** - 贡献代码优化与 Bug 修复

**在贡献前：**

- 请阅读我们的 [贡献指南](CONTRIBUTING.md) 了解详细说明
- 检查现有 Issue 以避免重复提交
- 遵循项目的目录结构与命名规范
- 确保你的项目包含完整的 README.md 说明文档

**重要提示：** 本项目遵循 [贡献者行为准则](CODE_OF_CONDUCT.md)。参与本项目即表示你同意遵守其条款。

## 📜 许可证

本仓库采用 [MIT License](./LICENSE) 开源协议。欢迎自由使用并修改示例代码用于你的项目。

## 👥 核心维护者

本项目由以下成员积极维护：

<p align="center">
  <a href="https://github.com/Arindam200" title="Arindam Majumder">
    <img src="https://avatars.githubusercontent.com/u/109217591?s=128&v=4" width="72" height="72" alt="Arindam Majumder" style="border-radius: 50%;" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/shivaylamba" title="Shivay Lamba">
    <img src="https://avatars.githubusercontent.com/u/19529592?s=128&v=4" width="72" height="72" alt="Shivay Lamba" style="border-radius: 50%;" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/Astrodevil" title="Astrodevil">
    <img src="https://avatars.githubusercontent.com/u/73425223?s=128&v=4" width="72" height="72" alt="Astrodevil" style="border-radius: 50%;" />
  </a>
</p>

<p align="center">
  <sub>
    <a href="https://github.com/Arindam200">Arindam Majumder</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/shivaylamba">Shivay Lamba</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/Astrodevil">Astrodevil</a>
  </sub>
</p>

如有任何疑问、建议或合作意向，欢迎随时联系维护团队。

## 感谢大家的支持！🙏

[![Star History Chart](https://api.star-history.com/svg?repos=Arindam200/awesome-ai-apps&type=Date)](https://www.star-history.com/#Arindam200/awesome-ai-apps&Date)