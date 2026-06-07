<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100-line minimalist LLM framework" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

English | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow 是一个[仅 100 行代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)的极简主义 LLM 框架。

- **轻量**：仅 100 行代码。零冗余、零依赖、无厂商锁定。
  
- **表达力强**：涵盖你所喜爱的一切功能——（[多](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html)）[智能体 (Agent)](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)、[工作流 (Workflow)](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)、[检索增强生成（RAG）](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) 等。

- **[代理式编程 (Agentic Coding)](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**：让 AI 智能体（例如 Cursor AI）来构建智能体——生产力提升 10 倍！

快速开始使用 Pocket Flow：
- **安装**：运行 `pip install pocketflow`，或直接复制[源代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)（仅 100 行）。
- **学习更多**：查看[视频教程](https://youtu.be/0Zr3NwcvpA0)与[官方文档](https://the-pocket.github.io/PocketFlow/)。
- 🎉 加入我们的 [Discord](https://discord.gg/hUHHE9Sa6T)，与其他使用 Pocket Flow 的开发者交流！
- 🎉 Pocket Flow 现已推出 [TypeScript](https://github.com/The-Pocket/PocketFlow-Typescript)、[Java](https://github.com/The-Pocket/PocketFlow-Java)、[C++](https://github.com/The-Pocket/PocketFlow-CPP)、[Go](https://github.com/The-Pocket/PocketFlow-Go)、[Rust](https://github.com/The-Pocket/PocketFlow-Rust) 和 [PHP](https://github.com/The-Pocket/PocketFlow-PHP) 版本！

## 为什么选择 Pocket Flow？

现有的 LLM 框架过于臃肿……构建一个 LLM 框架你只需要 100 行代码！

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **抽象层**          | **应用特定封装**                                      | **厂商特定封装**                                    | **代码行数**       | **体积大小**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agent, Chain               | 大量 <br><sup><sub>(如问答、摘要)</sub></sup>              | 大量 <br><sup><sub>(如 OpenAI、Pinecone 等)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agent, Chain            | 大量 <br><sup><sub>(如文件读取工具、SerperDev 工具)</sub></sup>         | 大量 <br><sup><sub>(如 OpenAI、Anthropic、Pinecone 等)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agent                      | 部分 <br><sup><sub>(如代码智能体、网页访问工具)</sub></sup>         | 部分 <br><sup><sub>(如 DuckDuckGo、Hugging Face 等)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agent, Graph           | 部分 <br><sup><sub>(如语义搜索)</sub></sup>                     | 部分 <br><sup><sub>(如 PostgresStore、SqliteSaver 等)</sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agent                | 部分 <br><sup><sub>(如工具智能体、聊天智能体)</sub></sup>              | 大量 [可选]<br> (如 OpenAI、Pinecone 等)<sup><sub></sub></sup>        | 7K <br><sup><sub>(仅核心)</sub></sup>    | +26MB <br><sup><sub>(仅核心)</sub></sup>          |
| **PocketFlow** | **图 (Graph)**                    | **无**                                                 | **无**                                                  | **100**       | **+56KB**                  |

</div>

## Pocket Flow 是如何工作的？

这[仅 100 行代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)提炼了 LLM 框架的核心抽象：**图 (Graph)**！
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

基于此，可以轻松实现流行的设计模式，如（[多](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html)）[智能体 (Agent)](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)、[工作流 (Workflow)](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)、[检索增强生成（RAG）](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) 等。
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ 以下是基础教程：

<div align="center">
  
| 名称  | 难度    | 描述  |  
| :-------------:  | :-------------: | :--------------------- |  
| [聊天机器人](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*入门*</sup>  | 具备对话历史的基础聊天机器人 |
| [结构化输出](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*入门*</sup> | 通过提示词从简历中提取结构化数据 |
| [工作流](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*入门*</sup> | 涵盖大纲规划、内容撰写与排版样式的工作流 |
| [智能体 (Agent)](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*入门*</sup>  | 具备网页搜索与问答能力的研究智能体 |
| [检索增强生成（RAG）](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*入门*</sup> | 简化的 RAG 处理流程 |
| [批处理](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*入门*</sup> | 将 Markdown 批量翻译为多语言的处理器 |
| [流式传输](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*入门*</sup> | 支持用户中断的实时 LLM 流式演示 |
| [对话安全护栏](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*入门*</sup> | 仅处理旅行相关查询的旅游顾问聊天机器人 |
| [多数投票](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*入门*</sup> | 通过聚合多次求解结果提升推理准确率 |
| [映射-归约 (Map-Reduce)](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*入门*</sup>  | 使用 Map-Reduce 模式批量处理简历筛选 |
| [命令行人机协同（HITL）](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*入门*</sup>  | 支持人类反馈闭环的 CLI 笑话生成器 |
| [多智能体协作](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*初级*</sup> | 两个智能体异步通信的禁忌词游戏 |
| [监督机制](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*初级*</sup> | 研究智能体表现不稳定？构建监督流程来管控质量 |
| [并行执行](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*初级*</sup> | 展示 3 倍加速效果的并行执行演示 |
| [并行工作流](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*初级*</sup> | 展示 8 倍加速效果的并行图像处理流程 |
| [思维链推理](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*初级*</sup> | 通过思维链（Chain-of-Thought）解决复杂推理问题 |
| [记忆系统](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*初级*</sup> | 具备短期与长期记忆的聊天机器人 |
| [文本转 SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*初级*</sup>  | 通过自动调试循环将自然语言转换为 SQL 查询 |
| [代码生成器](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*初级*</sup> | 生成测试用例、实现方案并迭代优化代码 |
| [模型上下文协议（MCP）](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*初级*</sup> | 使用 MCP 进行数值运算的智能体 |
| [智能体技能路由](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*初级*</sup> | 将请求路由至可复用的 Markdown 技能并在工作流中调用 |
| [智能体间通信（A2A）](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*初级*</sup> | 基于 A2A 协议封装的智能体通信示例 |
| [Streamlit 有限状态机 (FSM)](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*初级*</sup> | 结合 FSM 实现人机协同（HITL）图像生成的 Streamlit 应用 |
| [FastAPI WebSocket](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*初级*</sup> | 通过 WebSocket 实时流式传输 LLM 响应的聊天界面 |
| [FastAPI 后台任务](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*初级*</sup> | 结合后台作业与 SSE（服务端推送事件）实时进度更新的 FastAPI 应用 |
| [语音对话](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*初级*</sup> | 集成 VAD、STT、LLM 和 TTS 的交互式语音聊天应用。 |
| [LLM 裁判评估器](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*初级*</sup> | 用于内容迭代优化的 LLM-as-Judge 评估-优化循环 |
| [辩论机制](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*初级*</sup> | 两名辩手与一名中立裁判进行的对抗式推理演示 |
| [代理式 RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*初级*</sup> | 由智能体驱动、自主决定阅读文档的 RAG 流程 |
| [自愈型 Mermaid 图表](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*初级*</sup> | 自动生成 Mermaid 图表并具备自动错误恢复功能 |
| [心跳监控（嵌套工作流）](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*初级*</sup> | 类似 ClawBot 的常驻周期性监控，采用嵌套工作流实现 |
| [潜在客户挖掘](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*中级*</sup> | 销售漏斗流程：数据抓取、信息丰富、评分与个性化邮件发送 |
| [AI 新闻通讯聚合](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*中级*</sup> | AI 驱动的资讯筛选：搜索、过滤、摘要与排版格式化 |
| [发票数据处理](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★☆★ <sup>*中级*</sup> | 利用视觉模型从 PDF 中提取并验证发票数据 |
| [文档转播客 (NotebookLM)](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*中级*</sup> | 将文档转化为由两位 AI 主持人对谈的播客节目 |
| [深度研究](https://github.com-The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*中级*</sup> | 结合迭代优化的递归式 Map-Reduce 研究流程 |
| [编程智能体](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*高级*</sup> | 集成 6 项工具、记忆系统与补丁子工作流的生产级编程智能体 |

</div>

👀 想看更多面向新手的教程？[创建一个 Issue！](https://github.com/The-Pocket/PocketFlow/issues/new)

## 如何使用 Pocket Flow？

🚀 通过**代理式编程 (Agentic Coding)**——目前最高效的 LLM 应用开发范式：*人类负责设计架构，智能体负责编写代码*！

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ 以下是更复杂的 LLM 应用示例：

<div align="center">
  
| 应用名称     | 难度    | 涉及主题  | 人类设计 | 智能体编码 |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [网站客服机器人](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>将你的网站打造为全天候客服专家</sup></sub> | ★★☆ <br> *中级* | [智能体 (Agent)](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [检索增强生成（RAG）](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [设计文档](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [工作流代码](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [弹丸论破模拟器](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>忘掉图灵测试吧。这是终极 AI 实验！</sup></sub> | ★★★ <br> *高级*   | [工作流 (Workflow)](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [智能体 (Agent)](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [设计文档](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [工作流代码](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [代码库知识构建器](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>人生苦短，别对着别人的代码发呆</sup></sub> |  ★☆★ <br> *中级* | [工作流 (Workflow)](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [设计文档](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [工作流代码](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [用 Cursor 构建 Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>我们即将迎来奇点……</sup></sub> | ★★★ <br> *高级*   | [智能体 (Agent)](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [设计文档](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [工作流代码](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [向 AI Paul Graham 提问](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>万一没被录取，就问问 AI Paul Graham 吧</sup></sub> | ★★☆ <br> *中级*  | [检索增强生成（RAG）](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [映射-归约 (Map Reduce)](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [文本转语音 (TTS)](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [设计文档](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [工作流代码](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [YouTube 视频摘要](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub>像给 5 岁孩子讲故事一样为你讲解 YouTube 视频</sup></sub> | ★☆☆ <br> *初级*   | [映射-归约 (Map Reduce)](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [设计文档](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [工作流代码](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [破冰话术生成器](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub>瞬间破冰，将潜在客户转化为高意向客户</sup></sub> | ★☆☆ <br> *初级*   | [映射-归约 (Map Reduce)](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [网页搜索](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [设计文档](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [工作流代码](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- 想学习**代理式编程 (Agentic Coding)**？

  - 查看[我的 YouTube 频道](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1)，观看上述部分应用的制作视频教程！

  - 想构建自己的 LLM 应用？阅读这篇[文章](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)! 并从[此模板](https://github.com/The-Pocket/PocketFlow-Template-Python)开始吧！