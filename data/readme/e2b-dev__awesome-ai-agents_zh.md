# 🔮 Awesome AI Agents（精选 AI Agent 资源库）
<p align="center">
	<a href="https://discord.gg/U7KEcGErtQ" target="_blank">
		<img src="https://img.shields.io/static/v1?label=Join&message=%20discord!&color=mediumslateblue">
	</a>
	<a href="https://twitter.com/e2b" target="_blank">
		<img src="https://img.shields.io/twitter/follow/e2b.svg?logo=twitter">
	</a>
</p>

<h3 align="center">
  为你的 AI 应用添加 <a href="https://e2b.dev/docs?ref=awesome-sdks">代码解释器 (Code Interpreter)</a>
</h3>

<h5 align="center">🌟 <a href="https://e2b.dev/ai-agents">在 Web UI 中查看此列表</a></h5>
<h5 align="center">👉 <a href="https://forms.gle/UXQFCogLYrPFvfoUA">在此提交新产品</a></h5>

<img src="assets/landscape-latest.png" width="100%" alt="Chart of AI Agents Landscape" />

欢迎来到我们的 AI Agent 资源库。
我们将列表分为两部分：
- [开源项目](#open-source-projects)
- [闭源项目及公司](#closed-source-projects-and-companies)
  
如需按类别和用例筛选产品，请参阅🌟[此列表的 Web 版本](https://e2b.dev/ai-agents)。🌟

本列表基于我们的最佳认知整理而成，但肯定并不全面。同时推荐查看 <a href="https://github.com/e2b-dev/awesome-sdks-for-ai-agents">Awesome List of SDKs for AI Agents</a>。欢迎讨论和反馈！:heart:

## 有想添加的内容？
请创建 Pull Request 或填写此[表单](https://forms.gle/UXQFCogLYrPFvfoUA)。请保持字母顺序并归入正确的分类。

如需添加与 AI Agent 相关的 SDK、框架和工具，请访问 [Awesome SDKs for AI Agents](https://github.com/e2b-dev/awesome-sdks-for-ai-agents)。本列表仅针对 AI 助手和 Agent。

<!---
## Who's behind this?
This list is made by the team behind [e2b](https://github.com/e2b-dev/e2b). E2b is building AWS for AI agents. We help developers to deploy, test, and monitor AI agents. E2b is agnostic to your tech stack and aims to work with any tooling for building AI agents.
--->

## 探索 E2B —— 为 AI 应用提供代码解释功能
- 查看 [Code Interpreter SDK](https://e2b.dev/docs?ref=awesome-sdk)
- 浏览 [E2B Cookbook](https://github.com/e2b-dev/e2b-cookbook) 中的示例
- 阅读我们的[文档](https://e2b.dev/docs?ref=awesome-sdks)
- 通过 [hello@e2b.dev](mailto:hello@e2b.dev) 或 [Discord](https://discord.gg/35NF4Y8WSE) 联系我们。关注我们在 [X (Twitter)](https://twitter.com/e2b)

# 开源项目

## [Adala](https://github.com/HumanSignal/Adala)
Adala：自主数据（标注）Agent 框架

<details>

![Image](https://github.com/HumanSignal/Adala/raw/master/docs/src/img/logo-dark-mode.png)

### Category
通用、自定义构建、多智能体 (Multi-agent)

### Description

- **可靠 Agent**：基于真实数据构建，确保结果一致且可信。
- **可控输出**：通过灵活的约束定制输出，满足你的需求。
- **专注数据处理**：Agent 在定制化数据标注和处理任务中表现出色。
- **自主学习**：Agent 通过观察和反思进化，而不仅仅是自动化执行。
- **灵活可扩展的运行时**：社区驱动的演进框架，适应多样化需求。
- **易于定制**：无需陡峭的学习曲线即可快速开发应对独特挑战的 Agent。

### Links
- [Documentation](https://humansignal.github.io/Adala/) 
- [Discord](https://discord.gg/QBtgTbXTgU)
- [GitHub](https://github.com/HumanSignal/Adala)
</details>

## [Agent4Rec](https://github.com/LehengTHU/Agent4Rec)
拥有 1,000 个 Agent 的推荐系统模拟器

<details>
<p><img src="https://github.com/LehengTHU/Agent4Rec/raw/master/assets/sandbox.png" alt="Image" /></p>

### Category
通用、自定义构建、多智能体 (Multi-agent)

### Description
- Agent4Rec 是一个推荐系统模拟器，利用 1,000 个由 LLM 赋能的生成式 Agent。
- 这些 Agent 基于 [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/) 数据集初始化，具备多样的社会特征和偏好。
- 每个 Agent 以逐页方式与个性化电影推荐进行交互，并执行观看、评分、评估、退出和访谈等各种操作。

### Links
- [Paper](https://arxiv.org/abs/2310.10108)

</details>

## [AgentForge](https://github.com/DataBassGit/AgentForge)
支持 LLM 无关的 Agent 构建与测试平台

<details>

![Image](https://pbs.twimg.com/profile_images/1667167265060528129/l8S9vtP2_400x400.jpg)

### Category
通用、自定义构建、多智能体 (Multi-agent)

### Description
- 专为快速创建、测试和迭代 AI 驱动的自主 Agent 及认知架构而设计的低代码框架，兼容多种 LLM 模型。
- 轻松构建定制化 Agent 和认知架构。
- 支持 OpenAI、Anthropic Claude 和本地 Oobabooga 等多种 LLM 模型，允许根据特定需求为不同 Agent 灵活运行不同模型。
- 提供可定制的 Agent 记忆管理和实时提示词编辑功能，便于快速开发与测试。
- 采用数据库无关设计确保无缝扩展性，可轻松集成 ChromaDB 等不同数据库以支持各类 AI 项目。

### Links
- [GitHub](https://github.com/DataBassGit/AgentForge)
- [Web](https://www.agentforge.net/)
- [Discord](https://discord.com/invite/ttpXHUtCW6)
- [X](https://twitter.com/AgentForge)

</details>

## [AgentGPT](https://agentgpt.reworkd.ai/)
基于浏览器的 AutoGPT 无代码版本
<details>

![Image](https://raw.githubusercontent.com/reworkd/AgentGPT/main/next/public/banner.png)


### Category
通用

### Description
- 一个无代码平台
- 工作流程：
	- 为 Agent 分配目标
	- 观察其思考过程
	- 制定执行计划
	- 据此采取行动
- 使用 OpenAI Functions（函数调用）
- 支持 gpt-3.5-16k、pinecone 和 pg_vector 数据库
- 技术栈 (Stack)
	- 前端：NextJS + Typescript
	- 后端：FastAPI + Python
	- 数据库：通过 Docker 运行 MySQL，或本地运行 SQLite

<!--
### Features
- Uses OpenAI **functions**
- Supports gpt-3.5-16k, pinecone and pg_vector databases

### Stack
- Frontend: NextJS + Typescript
- Backend: FastAPI + Python
	- DB: MySQL through docker with the option of running SQLite locally
	-->

### Links
- [Documentation](https://docs.reworkd.ai/)
- [Website](https://agentgpt.reworkd.ai/)
- [GitHub](https://github.com/reworkd/AgentGPT)
</details>

<!-- This is a comment that appears only in the raw text -->

## [AgentPilot](https://github.com/jbexta/AgentPilot)
在桌面应用中构建、管理和与 Agent 对话


<details>

![Image](https://github.com/jbexta/AgentPilot/raw/master/docs/demo.png)

### Category
通用

### Description

- 集成于 Open Interpreter 和 MemGPT
- 支持群聊功能



### Links
- [GitHub](https://github.com/jbexta/AgentPilot)
- [X ](https://twitter.com/AgentPilotAI)
- 
  
</details>

## [Agents](https://github.com/aiwaves-cn/agents)

用于构建语言 Agent 的库/框架

<details>

![Image](https://github.com/aiwaves-cn/agents/raw/master/assets/agents-logo.png)

### Category
通用、自定义构建、多智能体 (Multi-agent)

### Description
-   **长短期记忆**：库中的语言 Agent 配备通过 VectorDB + 语义搜索实现的长期记忆，以及由 LLM 维护和更新的短期记忆（工作记忆）。
-   **工具使用**：库中的语言 Agent 可通过 [函数调用](https://platform.openai.com/docs/guides/gpt/function-calling) 使用任何外部工具，开发者可在此处添加定制化工具/API。
-   **网页导航**：库中的语言 Agent 可使用搜索引擎浏览网页并获取有用信息。
-   **多智能体通信**：除单个语言 Agent 外，该库支持构建多智能体系统，其中语言 Agent 可与其他 Agent 及环境进行交互。与大多数使用预定义规则控制 Agent 行动顺序的多智能体框架不同，**Agents** 包含一个 _控制器 (controller)_ 函数，通过 LLM 动态决定哪个 Agent 执行下一步操作，同时考虑之前的动作、环境和当前状态目标。这使得多智能体通信更加灵活。
-   **人机交互**：除让语言 Agent 在环境中相互通信外，我们的框架无缝支持人类用户亲自扮演 Agent 角色并输入自己的操作，与环境中的其他语言 Agent 进行交互。
-   **符号控制**：不同于仅使用简单任务描述来控制整个多智能体系统的现有框架，**Agents** 允许用户使用 **SOP（标准操作流程）** 定义子目标/子任务，从而为语言 Agent 定制细粒度工作流。

### Links
- Author: [AIWaves Inc.](https:github.com/aiwaves-cn)
- [Paper](https://arxiv.org/pdf/2309.07870.pdf)
- [GitHub Repository](https://github.com/aiwaves-cn/agents)
- [Documentation](https://agents-readthedocsio.readthedocs.io/en/latest/index.html)
- [Tweet](https://twitter.com/wangchunshu/status/1702512370785100133)
</details>

## [AgentVerse](https://github.com/OpenBMB/AgentVerse)
任务求解与模拟 Agent 平台
<details>

![Image](https://pbs.twimg.com/card_img/1744672970822615040/m870GGf1?format=jpg&name=medium)

### Category
通用、自定义构建、多智能体 (Multi-agent)

### Description
- 组装多个 Agent 以协作完成复杂任务。
- 允许自定义环境，用于观察或与多个 Agent 进行交互。

### Links
- Paper: [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://arxiv.org/abs/2308.10848)
- [Twitter](https://twitter.com/Agentverse71134)
- [Discord](https://discord.gg/gDAXfjMw)
- [Hugging Face](https://huggingface.co/spaces/AgentVerse/agentVerse)

</details>

## [AI Legion](https://github.com/eumemic/ai-legion)
多智能体 TS 平台，类似 AutoGPT

<details>

![Image](https://res.cloudinary.com/apideck/image/upload/w_1500,f_auto/v1681330426/marketplaces/ckhg56iu1mkpc0b66vj7fsj3o/listings/ai-legion/screenshots/Screenshot_2023-04-12_at_22.13.24_d9kdoj.png)

### Category
多智能体 (Multi-agent)、自定义构建


### Description
- 由 LLM 驱动的自主 Agent 平台
- 一个支持自主 Agent 协作完成任务的框架
- 通过控制台直接消息与 Agent 进行交互

### Links
- Author: [eumemic](https://github.com/eumemic)
- [Website](https://gpt3demo.com/apps/ai-legion)
- [GitHub](https://github.com/eumemic/ai-legion)
- [Twitter](https://twitter.com/dysmemic)
</details>

## [Aider](https://github.com/paul-gauthier/aider)
使用命令行在本地仓库中编辑代码

<details>


![Image](https://repository-images.githubusercontent.com/638629097/1d3d6251-f8be-4d11-bbb1-4e44b7364b74)

### Category
编程、GitHub

### Description
- Aider 是一个命令行工具，让你能够与 GPT-3.5/GPT-4 结对编程，以编辑存储在本地 git 仓库中的代码。
- 你可以启动新项目或与现有仓库协作。你可以在 aider 聊天中让 GPT 修改代码，并在你自己的编辑器中进行更改，两者之间可无缝切换。
- Aider 确保你和 GPT 的修改都能使用合理的提交信息提交到 git。Aider 的独特之处在于它能很好地处理已有的大型代码库。

### Links  
- [Website](https://aider.chat/)
- Author: [Paul Gauthier](https://github.com/paul-gauthier) (Github)
- [Discord Invite](https://discord.com/invite/Tv2uQnR88V)

</details>

## [AIlice](https://github.com/myshell-ai/AIlice)
创建 Agent 调用树以执行你的任务
<details>

![Image](https://github.com/myshell-ai/AIlice/raw/master/AIlice.png)

### Category
通用、个人助手、生产力工具

### Description
- “一个以聊天机器人形式存在的 Agent，独立规划自然语言输入的任务，并动态创建 Agent 调用树来执行任务。
- Agent 之间存在交互机制以确保容错性。
- 可自动构建外部交互模块以实现自我扩展。”

### Links  
- [GitHub](https://github.com/myshell-ai/AIlice)

</details>

## [AutoGen](https://github.com/microsoft/autogen)
具有多样化 Agent 的多智能体框架
<details>

![Image](https://github.com/microsoft/autogen/raw/main/website/static/img/autogen_agentchat.png)

### Category
通用、自定义构建、多智能体 (Multi-agent)

### Description
- 一个用于开发包含多个对话式 Agent 的 LLM（大语言模型）应用程序的框架。
- 这些 Agent 可协作解决问题，并能与人类无缝交互。
- 简化复杂的 LLM 工作流，提升自动化和优化能力。
- 提供覆盖各领域和不同复杂度的多种工作系统。
- 通过简单的性能调优及 API 统一、缓存等实用功能改进 LLM 推理效率。
- 支持高级使用模式，包括错误处理、多配置推理和上下文编程。

### Links
- Paper: [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](https://arxiv.org/pdf/2308.08155.pdf)
- [Discord](https://discord.gg/pAbnFJrkgZ)
- [Twitter thread describing the system](https://twitter.com/pyautogen)


</details>

## [AutoGPT](https://agpt.co/?utm_source=awesome-ai-agents)
尝试让 GPT4 完全自主化的实验性项目

<details>

![Image](https://news.agpt.co/wp-content/uploads/2023/04/Logo_-_Auto_GPT-B-800x363.png)

### Category
通用

### Description
- 一个开源的实验性尝试，旨在让 GPT-4 完全自主化，在 GitHub 上获得超过 140k Star。
- 将 LLM “思考”串联起来，自主实现你设定的任何目标。
- 提供互联网访问以进行搜索和信息收集。
- 支持长短期记忆管理。
- 可执行多种命令，如 Google 搜索、浏览网页、写入文件、执行 Python 文件等。
- 使用 GPT-4 实例进行文本生成。
- 可访问热门网站和平台。
- 使用 GPT-3.5 进行文件存储与摘要总结。
- 支持通过插件扩展功能。
- “类似于 BabyAGI 结合 LangChain 工具。”
- 0.4.0 版本新增特性：
	- 文件读取
	- 命令自定义
	- 增强测试

<!--
### Features added in release 0.4.0
- File reading
- Commands customization
- Enhanced testing
-->

### Links
- [Twitter](https://twitter.com/Auto_GPT/?utm_source=awesome-ai-agents)
- [GitHub](https://github.com/Significant-Gravitas/Auto-GPT/?utm_source=awesome-ai-agents)
- [Facebook](https://www.facebook.com/groups/1330282574368178/?utm_source=awesome-ai-agents)
- [Linkedin](https://www.linkedin.com/company/autogpt/?utm_source=awesome-ai-agents)
- [Discord](https://discord.gg/autogpt/?utm_source=awesome-ai-agents)
- Author: [Significant Gravitas](https://twitter.com/SigGravitas/?utm_source=awesome-ai-agents)
</details>



## [Automata](https://github.com/emrgnt-cmplxty/automata)
根据项目上下文生成代码

<details>


![Image](https://github.com/emrgnt-cmplxty/Automata/assets/68796651/61fe3c33-9b7a-4c1b-9726-a77140476b83)

### Category
编程

### Description
- 模型：GPT 4
- Automata 将你的项目作为上下文，接收任务并无缝执行指令。
- 特性 (Features)
	- Automata 旨在进化为完全自主、自编程的人工智能系统。
	- 设计用于与所有可用的 Agent 平台和 LLM 提供商无缝集成。
	- 利用新颖的代码搜索算法 SymbolRank 及相关工具构建卓越的编码智能。
	- 模块化且完全可配置的设计，最小化对外部依赖的依赖。

### Links
- [GitHub](https://github.com/emrgnt-cmplxty/automata)
- [Docs](https://automata.readthedocs.io/en/latest/)
- Author: [Owen Colegrove](https://twitter.com/ocolegro)
<!--

### Features
- Automata aims to evolve into a fully autonomous, self-programming Artificial Intelligence system.
- It's designed for seamless integration with all available agent platforms and LLM providers.
- Utilizes the novel code search algorithm, SymbolRank, and associated tools to build superior coding intelligence.
- Modular, fully configurable design with minimal reliance on external dependencies.

-->

</details>

## [AutoPR](https://github.com/irgolic/AutoPR)
AI 生成的 Pull Request Agent，用于修复问题

<details>

![Image](https://github.com/irgolic/AutoPR/raw/main/website/static/img/AutoPR_Mark_color.png)

### Category
编程、GitHub

### Description
- 当向 Issue 添加包含 AutoPR 的标签时触发，AutoPR 将：
	- 制定修复计划
	- 编写代码
	- 推送分支
	- 打开 Pull Request

### Links
- [Discord](https://discord.com/invite/ykk7Znt3K6)

</details>

## [Autonomous HR Chatbot](https://github.com/stepanogil/autonomous-hr-chatbot)
使用工具回答人力资源相关查询的 Agent

<details>

![Image](https://github.com/stepanogil/autonomous-hr-chatbot/raw/main/assets/sample_chat.png)

### Category
人力资源、商业智能、生产力工具

### Description
- 一个原型企业应用——由 GPT-3.5 驱动的自主 HR 助手。
- 一个能利用手头工具自主回答人力资源相关查询的 Agent。
- 基于 GPT-3.5 驱动。
- 当前分配给该 Agent 的工具（更多即将推出）：
	- 考勤政策 (Timekeeping Policy)
	- 员工数据 (Employee Data)
	- 计算器 (Calculator)

### Links
- Medium: [Creating a (mostly) Autonomous HR Assistant with ChatGPT and LangChain’s Agents and Tools](https://pub.towardsai.net/creating-a-mostly-autonomous-hr-assistant-with-chatgpt-and-langchains-agents-and-tools-1cdda0aa70ef)
- [GitHub](https://github.com/stepanogil/autonomous-hr-chatbot)
- Author: [Stephen Bonifacio](https://twitter.com/Stepanogil)
- [YouTube demo](https://www.youtube.com/watch?v=id7XRcEIBvg&ab_channel=StephenBonifacio)
- [Blog post](https://pub.towardsai.net/creating-a-mostly-autonomous-hr-assistant-with-chatgpt-and-langchains-agents-and-tools-1cdda0aa70ef)
</details>

## [BabyAGI](https://github.com/yoheinakajima/babyagi)
使用 AI 管理任务的简单框架
<details>

![Image](https://user-images.githubusercontent.com/21254008/235015461-543a897f-70cc-4b63-941a-2ae3c9172b11.png)

### Category
通用

### Description
- 原始 [Task-Driven Autonomous Agent](https://twitter.com/yoheinakajima/status/1640934493489070080?s=20) 的精简版本。
- 根据前序任务结果和预定义目标创建新任务。
- 脚本随后使用 OpenAI 的 NLP 能力基于目标生成新任务。
- 利用 OpenAI GPT-4、pinecone 向量搜索和 LangChainAI 框架。
- 默认模型为 OpenAI GPT3-turbo。
- 系统维护任务列表以管理和优先处理任务。
- 它根据完成结果自主创建新任务并相应地重新排序任务列表，展示了 AI 驱动语言模型的适应性。


### Links
- Paper: [Task-driven Autonomous Agent Utilizing GPT-4, Pinecone, and LangChain for Diverse Applications](https://yoheinakajima.com/task-driven-autonomous-agent-utilizing-gpt-4-pinecone-and-langchain-for-diverse-applications/)
- [Discord](https://discord.com/invite/TMUw26XUcg)
- [Founder's Twitter](https://twitter.com/yoheinakajima)
- [Twitter thread describing the system](https://twitter.com/yoheinakajima/status/1640934493489070080)


</details>


## [BabyBeeAGI](https://yoheinakajima.com/babybeeagi-task-management-and-functionality-expansion-on-top-of-babyagi/)
任务管理与功能扩展的 BabyAGI 衍生版

<details>

![Image](https://yoheinakajima.com/wp-content/uploads/2023/04/image.png)

### Category
通用、生产力工具

### Description
- 原始 BabyAGI 代码的更高级版本。
- - 通过引入更复杂的任务管理提示词，改进了原始框架，允许更全面的信息分析与综合。
- 设计用于在单个任务管理提示词内处理多个功能。
- 基于 GPT-4 架构构建，导致处理速度较慢且偶发错误。
- 提供了一个可进一步扩展和改进的框架，为更复杂的 AI 应用铺平道路。
- BabyAGI 与 BabyBeeAGI 的一个显著区别是任务管理提示词的复杂度。

### Links
- [Tweet](https://twitter.com/yoheinakajima/status/1652732735344246784)
- [GitHub](https://github.com/yoheinakajima/babyagi/blob/main/classic/BabyBeeAGI.py)
- [Replit](https://replit.com/@YoheiNakajima/BabyBeeAGI?v=1)
- Author: [@yoheinakajima](https://twitter.com/yoheinakajima) (Twitter)

</details>


## [BabyCatAGI](https://replit.com/@YoheiNakajima/BabyCatAGI)
BabyCatAGI 是 BabyBeeAGI 的修改版
<details>

![Image](https://pbs.twimg.com/media/FwBwoRracAI99iP?format=jpg&name=medium)

### Category
通用

### Description
- 仅 300 行代码。
- 这是以轻量级方式对原始 BabyAGI 代码的迭代开发。与 BabyAGI 的区别包括：
	- 任务创建 Agent (Task Creation Agent) 仅运行一次
	- 执行 Agent (Execution Agent) 循环处理任务
	- 用于提取相关结果的任务依赖关系
	- 两个工具：搜索工具和文本补全工具
	- “Mini-agent”作为工具使用
	- 搜索工具结合搜索、抓取、分块和提取功能。
	- 合并结果以生成摘要报告


<!--
### How to use
- Fork this into a private Repl
- Add your OpenAI API Key (required) and SerpAPI Key (optional)
- Update the OBJECTIVE variable
- Press "Run" at the top.
-->

### Links
- [Tweet](https://twitter.com/yoheinakajima/status/1657448504112091136)
- [GitHub](https://github.com/yoheinakajima/babyagi/blob/main/classic/BabyCatAGI.py)
- [Replit](https://replit.com/@YoheiNakajima/BabyCatAGI)
- Author: [@yoheinakajima](https://twitter.com/yoheinakajima) (Twitter)

</details>

## [BabyDeerAGI](https://twitter.com/yoheinakajima/status/1666313838868992001)
仅约 350 行代码的 BabyAGI 修改版

<details>

![Image](https://pbs.twimg.com/media/Fx_tr0yaUAYP1Q0?format=jpg&name=medium)

### Category
通用

### Category
通用

### Description
- 特性 (Features)
	- 并行任务（提升速度）
	- 仅支持 3.5-turbo（无需 GPT-4）
	- 用户输入工具
	- 网页搜索工具中的查询重写功能
	- 保存结果


### Links
- [Tweet](https://twitter.com/yoheinakajima/status/1666313838868992001)
- [GitHub](https://github.com/yoheinakajima/babyagi/blob/main/classic/BabyDeerAGI.py)
- [Replit](https://replit.com/@YoheiNakajima/BabyDeerAGI)
- Author: [@yoheinakajima](https://twitter.com/yoheinakajima) (Twitter)

</details>

## [BabyElfAGI](https://twitter.com/yoheinakajima/status/1678443482866933760)
约 895 行代码的 BabyDeerAGI 修改版
<details>

![Image](https://pbs.twimg.com/media/F0sHc04aMAEVn3D?format=jpg&name=medium)

### Category
通用

### Description
- 特性 (Features)
	- Skills 类允许创建新技能
	- “动态任务列表”示例结合向量搜索
	- Beta 版反思 Agent
	- 可读取、编写和审查自身代码


### Links
- [Tweet](https://twitter.com/yoheinakajima/status/1678443482866933760)
- [GitHub](https://github.com/yoheinakajima/babyagi/blob/main/classic/BabyElfAGI/main.py)
- [Replit](https://replit.com/@YoheiNakajima/BabyElfAGI)
- Author: [@yoheinakajima](https://twitter.com/yoheinakajima) (Twitter)

</details>


## [BabyCommandAGI](https://github.com/saten-private/BabyCommandAGI)
测试 CLI 与 LLM 结合的效果
<details>

![Image](https://github.com/saten-private/BabyCommandAGI/raw/main/docs/Architecture.png)

### Category
通用、编程

### Description
- 专为测试 CLI 和 LLM（传统界面而非 GUI）结合效果而设计的 Agent（由 @saten-private 创建）。
- 基于 @yoheinakajima 的 [BabyAGI](https://github.com/yoheinakajima/babyagi) 构建，可执行 Shell 命令。
- 自动编程：仅通过提供反馈即可成功自动创建一个应用。流程详见[此处](https://twitter.com/saten_work/status/1674855573412810753)。
- 自动环境配置：在容器中成功在 Linux 上安装了 Flutter 环境，创建了 Flutter 应用并启动它。流程详见[此处](https://twitter.com/saten_work/status/1667126272072491009)。
- 除环境配置外，似乎还能处理一些通用任务，如 [生成文本（诗歌、代码、脚本、乐曲、邮件和信件）、翻译语言等](https://anyaitools.com/babycommandagi/?utm_source=SocialAutoPoster&utm_medium=Social&utm_campaign=Twitter)。
- 存在破坏环境的風險。请在 Docker 等虚拟环境中运行。
- 推荐使用 GPT-4 或更高版本。

### Links
- [Founder's Twitter](https://twitter.com/saten_work)
- [Twitter thread describing the system](https://twitter.com/saten_work/status/1654571194111393793)

</details>


## [BabyFoxAGI](https://github.com/yoheinakajima/babyagi/tree/main/classic/babyfoxagi)
带有新并行 UI 面板的 BabyAGI 修改版


<details>

![Image](https://pbs.twimg.com/media/F2Vpt4EbIAAa326?format=jpg&name=medium)

### Category
通用

### Description
- BabyElfAGI 的修改版，属于按字母顺序命名的 Baby<animal>AGI 系列修改版。
- 自我改进的任务列表（FOXY 方法）
   	- 通过在末尾存储最终反思，并提取最相关的反思以指导后续运行，BabyAGI 会逐步生成越来越好的任务列表。
- 带有并行任务的创新聊天 UI
  	- 你可以与 BabyAGI 对话！它拥有实验性 UI，将聊天与任务/输出面板分离，允许你并行请求多个任务。
  	- Chat UI 可快速使用单个技能，或使用任务列表串联多个技能。
- 新技能 (New skills)
	- 🎨 DALLE 技能（带提示词辅助）
 	- 🎶 Deezer 音乐播放器
	- 📊 Airtable 搜索（添加你自己的表格/基础 ID）
	- 🔍 初创公司分析师（作为技能的重量级函数调用示例）
- 自带 README


### Links
- [Author's Twitter](https://twitter.com/yoheinakajima)
- [Twitter thread describing the system](https://twitter.com/yoheinakajima/status/16975391768116449)
- [Replit](https://replit.com/@YoheiNakajima)

</details>



## [BambooAI](https://github.com/pgalko/BambooAI)
面向非程序员的数探索与分析工具

<details>

![Image](https://pbs.twimg.com/card_img/1745187734602313730/f-W5kbIU?format=jpg&name=medium)

### Category
数据分析

### Description
- BambooAI 以循环方式运行（直到用户决定结束）。
- 允许混合使用具有不同能力、Token 成本和上下文窗口的模型来处理不同任务。
- 维护之前对话的记忆。
- 利用 Pinecone 向量数据库中的相关上下文动态构建提示词。
- 提供叙述性输出或在必要时提出后续问题。
- 对于代码化响应，将任务分解为步骤列表并构建伪代码算法。
- 基于该算法，使用 Python 进行数据集分析、建模或绘图。
- 调试代码然后执行，如需则自动纠正，并向用户显示输出。
- 对最终答案进行排名，并征求用户反馈。
- 根据排名和用户反馈构建向量数据库知识库。

### Links
- [GitHub](https://github.com/pgalko/BambooAI)
- [Creators's Twitter](https://twitter.com/pgalko)

</details>


## [BeeBot](https://github.com/AutoPackAI/beebot)
面向广泛任务的早期项目

<details>

![Image](https://camo.githubusercontent.com/72231056f7393fa18ee2baa5cedf2688d1fc15478bb6131936e222e5d23ccbb6/68747470733a2f2f65726b6c702e636f6d2f6d6173636f742e706e67)

### Category
通用、生产力工具

### Description
- “BeeBot 目前处于开发中，应被视为早期研究项目。其重点并非用于生产环境。”

	
### Links
- [GitHub](https://github.com/AutoPackAI/beebot)
- [Tweet](https://twitter.com/Douglas_Schon/status/1681094815021187072?s=20)
</details>


## [Blinky](https://github.com/seahyinghang8/blinky)
VSCode 的开源 AI 调试 Agent

<details>

![Banner](https://github.com/seahyinghang8/blinky/raw/master/media/banner.png)

### Category
编程、调试

### Description
- Blinky 是一个用于 VSCode 的开源 AI 调试 Agent，利用 LLM 帮助识别和修复后端代码错误（灵感来自 SWE-agent）。
- Blinky 利用 VSCode API、语言服务器协议 (LSP) 和 print 语句调试技术，对现实世界中的后端系统进行三角定位并解决 Bug。

	
### Links
- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=blinky.blinky)
- [Discord](https://discord.gg/d3AUNHDb)
- [GitHub](https://github.com/seahyinghang8/blinky)
</details>


## [Bloop](https://bloop.ai/)
AI 代码搜索，支持 Rust 和 Typescript

<details>

![Image](https://bloop.ai/_next/static/media/logo_white.b3bdedc0.svg)

### Category
编程

### Description
- 一个由 GPT-4 驱动的语义代码搜索引擎，使用 AI Agent。
- 精确的代码导航。
- 基于堆栈图和范围查询构建。
- 用 Rust 编写的快速代码搜索和正则表达式匹配引擎。
- 允许在 Rust 和 Typescript 中查找代码。
- 支持暂存更改 (stage changes)。
- Agent 使用自然语言、正则表达式和过滤查询同时搜索你的本地和远程仓库。
- Bloop 可通过应用运行（通过 GitHub 易于下载）。

### Links
- [GitHub](https://github.com/BloopAI/bloop)
- ["Getting started" guide](https://bloop.ai/docs/getting-started)
- [Bloop apps](https://github.com/BloopAI/bloop/releases)

</details>

## [BondAI](https://bondai.dev/)
支持 CLI 与 RESTful/WebSocket API 的代码解释器

<details>

![Image](https://bondai.dev/assets/images/bondai-logo-9bec7e27b93b804d375221ff8fb6d336.png)

### Category
编程

### Description
- 一个功能强大的自主 AI Agent，提供易用的 CLI、RESTful/WebSocket API、预构建 Docker 镜像及丰富的集成工具套件。
- 支持所有 GPT-N、Embeddings 和 Dall-E OpenAI 模型。
- 支持 Azure OpenAI Services。
- 易于集成的 SDK，可嵌入任何应用。
- 强大的 **代码解释器 (Code Interpreter)** 功能。
- 通过 Postgres DB 集成实现强大的数据查询能力。
- 预构建 Docker 镜像提供安全的代码生成/执行环境。
- 支持电话应用（通过 BlandAI）。
- 支持股票交易（通过 Alpaca Markets）。
- 集成 Gmail 和 Google Search。
- 易于安装 `pip install bondai`。
- 启动 CLI 只需运行 `bondai`。
- 启动 RESTful/WebSocket API 只需运行 `bondai --server`。

### Links
- [BondAI Homepage/Documentation](https://bondai.dev)
- [Github Repository](https://github.com/krohling/bondai)
- [Docker Image](https://hub.docker.com/r/krohling/bondai)

</details>

## [bumpgen](https://github.com/xeol-io/bumpgen)
保持 npm 依赖项更新的 AI Agent

<details>

![demo](<https://assets-global.website-files.com/65af8f02f12662528cdc93d6/662e6061d42954630a191417_tanstack-ezgif.com-speed%20(1).gif>)

### Category
编程

### Description
- 将依赖管理和升级置于自动驾驶模式。
- bumpgen 将 npm 包的版本 BUMPs（提升）然后 GENerates（生成）破坏性更改的代码修复。
- 支持 gpt-4-turbo。
- 轻松安装 > `npm install -g bumpgen`。
- 轻松启动 > `bumpgen @tanstack/react-query 5.28.14`。

### Links
- [Repo](https://github.com/xeol-io/bumpgen)
- [Docs](https://docs.xeol.io/bumpgen/home)

</details>

## [Cal.ai](https://cal.ai)
基于 Cal.com 构建的开源日程助手

<details>

![Image](https://3620107743-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpmUOqZjfGqNkiPmqgnMv%2Fuploads%2F9Qaq1hlaTcqKfrc9k4OG%2Fimage.png?alt=media&token=1ffe8530-19ff-4aea-b020-a99cdc224ce1)

### Category
生产力工具

### Description
- Cal.ai 可根据自然语言预订会议、总结你的周计划并寻找与他人共处的时间。
- 灵活响应未见过的新任务，例如：“把我倒数第二个会议移到明天早上”。
- 底层使用 GPT-4 和 LangChain Agent Executor。
- [GitHub](https://github.com/calcom/cal.com/tree/main/apps/ai)

### Links
- Authors: [Cal.com core team](https://github.com/calcom/cal.com/graphs/contributors), [Dexter Storey](https://github.com/dexterstorey), [Ted Spare](https://github.com/tedspare)

</details>


## [CAMEL](https://github.com/camel-ai/camel)
用于 Agent “思维”探索的架构

<details>

![Image](https://raw.githubusercontent.com/camel-ai/camel/master/misc/logo.png)

### Category
通用

### Description
- CAMEL 是一个开源库，专为自主和可通信 Agent 的研究而设计。
1) AI 用户 Agent：以完成任务为目标向 AI 助手发出指令。
2) AI 助手 Agent：遵循 AI 用户的指令并返回任务解决方案。
- CAMEL 还有一个致力于研究自主和可通信 Agent 的开源社区。

### Links
- [Web](https://www.camel-ai.org/)
- [Paper - CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society](https://ghli.org/camel.pdf)
- [Colab demo](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing)
- [GitHub](https://github.com/camel-ai/camel)
- [Hugging face datasets](https://huggingface.co/camel-ai)
- [Slack](https://camel-kwr1314.slack.com/join/shared_invite/zt-1vy8u9lbo-ZQmhIAyWSEfSwLCl2r2eKA#/shared-invite/email)
- [Twitter](https://twitter.com/intent/follow?original_referer=https%3A%2F%2F1508613885-atari-embeds.googleusercontent.com%2F&ref_src=twsrc%5Etfw%7Ctwcamp%5Ebuttonembed%7Ctwterm%5Efollow%7Ctwgr%5ECamelAIOrg&screen_name=CamelAIOrg)
- Authors: Guohao Li∗ Hasan Abed Al Kader Hammoud* Hani Itani* Dmitrii Khizbullin, Bernard Ghanem

</details>

## [ChatArena](https://www.chatarena.org/)
用于多智能体交互的聊天工具

<details>

![image](https://github.com/Farama-Foundation/chatarena/raw/main/docs/images/chatarena_architecture.png)

### Category
设计、自定义构建、AI 应用 SDK、多智能体 (Multi-agent)

### Description
- ChatArena（或 Chat Arena）是用于 LLMs 的多 Agent 语言游戏环境。目标是开发 AI 的通信与协作能力。ChatArena 提供：
- 一个用于为多个大语言模型 (LLMs) 构建交互环境的通用框架。 
- 一系列预构建或由社区创建的环境。
- 友好的用户界面，支持 Web UI 和命令行接口。

### Links
- [Web](https://www.chatarena.org/)
- [GitHub](https://github.com/Farama-Foundation/chatarena)
- [X](https://twitter.com/_chatarena)
- [Slack channel](https://chatarena.slack.com/join/shared_invite/zt-1t5fpbiep-CbKucEHdJ5YeDLEpKWxDOg#/shared-invite/email)
  
</details>

## [ChatDev](https://github.com/OpenBMB/ChatDev)
用于软件开发的通信 Agent

<details>

![Image](https://github.com/OpenBMB/ChatDev/raw/main/misc/logo1.png)

### Category
编程、多智能体 (Multi-agent)

### Description
- ChatDev 是一家由众多扮演不同角色的智能 Agent（如 CEO、CPO、CTO、程序员、审查员、测试人员和艺术设计师，每个都有独特图标）驱动虚拟软件公司。
- 这些 Agent 在结构化的组织环境中协作，履行“通过编程颠覆数字世界”的公司使命。他们参与专注于设计、编码、测试和文档的功能研讨会。
- ChatDev 旨在提供一个基于大语言模型的易于访问、模块化和可扩展的平台，以在受控环境中研究集体智能。
- 该框架允许广泛定制，赋能用户定制软件开发流程、定义阶段并在虚拟公司内建立特定角色。
- ChatDev 致力于开源原则，鼓励社区贡献并透明分享进展。

### Links
- [Paper - ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924)
- [Local demo](https://github.com/OpenBMB/ChatDev/blob/main/wiki.md#local-demo)
- [GitHub](https://github.com/OpenBMB/ChatDev)

</details>

## [ChemCrow](https://github.com/ur-whitelab/chemcrow-public)
用于化学相关任务的 LangChain Agent

<details>

![Image](https://github.com/ur-whitelab/chemcrow-public/raw/main/assets/chemcrow_dark_bold.png)

### Category
科学、化学

### Description
- ChemCrow 是一个开源包，用于准确解决推理密集型化学任务。
- 它集成了 13 个专家设计工具以增强 LLM 在化学领域的表现，并展示了自动化化学任务的效能。
- 基于 Langchain 构建。
- 向 LLM 提供工具名称列表、效用描述以及预期的输入/输出细节。然后指示模型在必要时使用提供的工具回答用户提示词。指令建议模型遵循 ReAct 格式——思考 (Thought)、行动 (Action)、行动输入 (Action Input)、观察 (Observation)。一个有趣的观察结果是，尽管基于 LLM 的评估得出结论认为 GPT-4 和 ChemCrow 表现几乎相当，但面向解决方案完整性和化学正确性的专家人类评估显示 ChemCrow 大幅领先于 GPT-4。这表明使用 LLM 评估其在需要深厚专业知识的领域自身性能可能存在潜在问题。缺乏专业知识可能导致 LLM 无法意识到自身的缺陷，从而难以准确判断任务结果的正确性。（来源：[Weng, Lilian. (Jun 2023). LLM-powered Autonomous Agents". Lil’Log. https://lilianweng.github.io/posts/2023-06-23-agent/.](https://lilianweng.github.io/posts/2023-06-23-agent/)）

### Links
- [Paper](https://arxiv.org/abs/2304.05376)
- [GitHub](https://github.com/ur-whitelab/chemcrow-public)
- [HackerNews Discussion](https://news.ycombinator.com/item?id=35607616)

</details>

## [Clippy](https://github.com/ennucore/clippy/)
可规划、编写、调试和测试代码的 Agent

<details>

![Image](https://lev.la/images/clippy.jpg)

### Category
编程

### Description
- Clippy 的目的是为用户生成或协同生成代码。
- 它可以自主规划、编写、调试和测试某些项目。
- 对于更复杂的任务，最佳使用方式是查看其工作成果并向它提供反馈。

### Links
- [GitHub](https://github.com/ennucore/clippy/)
- Author: [Lev Chizhov](http://lev.la/) 

</details>

## [CodeFuse-ChatBot](https://github.com/codefuse-ai/codefuse-chatbot)
服务整个软件开发生命周期的 Agent
<details>

![Image](https://github.com/codefuse-ai/codefuse-chatbot/raw/main/sources/docs_imgs/objective_v4.png)

### Category
编程

### Description
- 一个智能助手，由多 Agent 框架驱动，结合 DevOps 工具包、代码/文档仓库 RAG 等，服务于整个软件开发生命周期。

### Links
- [GitHub](https://github.com/codefuse-ai/codefuse-chatbot)

</details>

## [Cody by ajhous44](https://github.com/ajhous44/cody)
查询和浏览你的代码库

<details>

![Image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
编程

### Description
- 一个 AI 助手，设计用于让你使用自然语言交互式查询你的代码库。
- 通过利用向量嵌入、分块和 OpenAI 的语言模型，Cody 可以高效直观地帮助你导航代码。

### Links
- [GitHub](https://github.com/ajhous44/cody)
- Author: [@ajhous44](https://github.com/ajhous44/) (Github)

</details>

## [Cody by Sourcegraph](https://docs.sourcegraph.com/cody)
编写代码并回答你问题的 Agent

<details>

![Image](https://sourcegraph.com/.assets/img/sourcegraph-mark.svg?v2)

### Category
编程

### Description
来自 Sourcegraph 的 AI 代码助手，通过阅读你的整个代码库和代码图来为你编写代码并回答问题。

### Links
- [GitHub](https://github.com/sourcegraph/sourcegraph/tree/main/client/cody)
- Author: [@sourcegraph](https://twitter.com/sourcegraph) (Twitter)

</details>

## [Continue](https://continue.dev/)
开源软件开发自动驾驶仪

<details>

![Image](https://continue.dev/docs/assets/images/continue-cover-logo-aa135cc83fe8a14af480d1633ed74eb5.png)

### Category
编程

### Description
- 一个开源的软件开发自动驾驶仪——将 ChatGPT 的力量带入 VS Code。
- 特性：
	- 回答编码问题
   	- 使用自然语言编辑代码
   	- 从零生成文件


### Links
- [Website](https://continue.dev/)
- [GitHub](https://github.com/continuedev/continue)
- [Documentation](https://continue.dev/docs/intro)
- [Twitter](https://twitter.com/continuedev)

</details>

## [CrewAI](https://github.com/joaomdmoura/crewai)
用于编排角色扮演 Agent 的框架
<details>

![Image](https://github.com/joaomdmoura/crewAI/raw/main/docs/crewai_logo.png)

### Category
自定义构建、Agent SDK、多智能体 (Multi-agent)

### Description
- 用于编排角色扮演、自主 AI Agent 的前沿框架。
- 通过培养协作智能，CrewAI 赋能 Agent 无缝协作，攻克复杂任务。
- Crew AI 是一个基于 LangChain 的多 Agent 框架，旨在赋能工程师利用 AI Agent 的集体力量。与传统自动化方法相比，Crew AI 引入了协同决策的新方法、增强的创造力以及解决复杂问题的能力。
- Crew AI 的设计哲学倡导通过模块化实现简洁性。其主要组件包括 Agent、工具、任务、流程和团队 (crews)。每个 Agent 都像团队成员一样，拥有特定角色、背景故事、目标和记忆。通过模块化设计，我们将复杂的 AI Agent 世界变得易于访问、管理和更具吸引力。


### Links
- [GitHub](https://github.com/joaomdmoura/crewai)
- [Founder's X](https://twitter.com/joaomdmoura)
- [Blog post: How to use Crew AI](https://crewai.net/posts/how-to-use-crew-ai)
- [Crew AI Wiki with examples and guides](https://github.com/joaomdmoura/CrewAI/wiki)
- [Docs](https://github.com/joaomdmoura/CrewAI/wiki)
- [Discord](https://discord.com/invite/X4JWnZnxPb)

</details>

## [data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper)
从数据到人类可验证研究论文的 AI 驱动研究框架
<details>

<br>
<img src="https://github.com/Technion-Kishony-lab/data-to-paper/assets/65530510/e33bcb52-5f4e-4fd0-8be9-ebd64607c449" width="400" align="center">
<br>
	
### Category
科学、研究、多智能体 (Multi-agent)

### Description
[*data-to-paper*](https://arxiv.org/abs/2404.17605) 是一个框架，旨在系统性地利用 AI 的力量执行完整的端到端科学研究，从原始数据开始，最终产出全面、透明且人类可验证的科研论文。

为此目标，*data-to-paper* 系统地引导交互式的 LLM 和基于规则的 Agent 沿着传统科学路径前进：从带注释的数据出发，创建研究假设，进行文献搜索，编写和调试数据分析代码，解释结果，并最终逐步撰写完整的研究报告。

*data-to-paper* 框架是作为研究项目创建的，旨在理解 LLM 驱动的科学研究的容量与局限性，并开发利用 LLM 加速研究的方法，同时保持甚至增强关键科学价值（如透明度、可追溯性和可验证性），并允许科学家监督和指导该过程 [另见：[living guidelines](https://www.nature.com/articles/d41586-023-03266-1)]。


### Links
- [GitHub](https://github.com/Technion-Kishony-lab/data-to-paper)
- [arXiv preprint](https://arxiv.org/abs/2404.17605)
- [Demo video](https://www.youtube.com/watch?v=Nt_460MmM8k)

</details>


## [Databerry](https://www.databerry.ai/)
（已转型为 Chaindesk）无代码聊天机器人构建工具

<details>

![Image](https://www.chaindesk.ai/_next/image?url=%2Fapp-logo-icon.png&w=256&q=75)

### Category
自定义构建

### Description
- 一个极其简单的无代码平台，用于创建基于你自身数据训练的 AI 聊天机器人。
- 创建新 Agent、选择模型、数据和设置后，即可部署到网站、Slack、Crisp 或 Zapier。
- 免费版本对 Agent 数量有限制。
- 技术栈 (Stack)
	- Next.js
	- Joy UI
	- LangchainJS
	- PostgreSQL
	- Prisma
	- Qdrant
- 特性 (Features)
	- 简化客户支持、新员工入职等流程。
	- 从任何地方加载数据。
	- 无代码：用户友好的界面管理你的数据存储并与数据进行聊天。
	- 用于查询数据的受保护 API 端点。
	- 自动同步数据源（即将推出）。
	- 为每个数据存储自动生成 ChatGPT 插件。

### Links
- [Documentation](https://docs.chaindesk.ai/introduction)
- [Discord](https://discord.com/invite/FSWKj49ckX)
- [GitHub](https://github.com/gmpetrov/databerry)

</details>

## [DemoGPT](https://github.com/melih-unsal/DemoGPT)
生成任何用途新应用的演示版本

<details>

![Image](https://github.com/melih-unsal/DemoGPT/raw/main/assets/banner_small.png)

### Category
自定义构建、通用

### Description
- DemoGPT 利用语言模型 (LLMs) 的力量为应用程序提供快速有效的演示创建功能。
- 自动化原型制作流程，提高效率并节省宝贵时间。
- 理解并处理给定的提示词以生成相关应用。
- 集成 LangChain，通过“转换树” (ToT) 方法迭代解析 LangChain 文档来生成应用代码。
- DemoGPT 的路线图包括基于用户反馈和实际应用的持续更新和改进，致力于完善技术并解决幻觉问题。
- “我们计划引入进一步增强应用生成流程的功能，使其对用户更友好且更高效。”

### Links
- [Github](https://github.com/melih-unsal/DemoGPT)
- [Website](https://www.demogpt.io/)
- [Twitter](https://twitter.com/demo_gpt)
- [Streamlit App](https://demogpt.streamlit.app/)
- [Hugging Face Space](https://huggingface.co/spaces/melihunsal/demogpt)

</details>

## [DevGPT](https://github.com/jina-ai/dev-gpt)
虚拟开发团队

<details>

![Image](https://pbs.twimg.com/profile_images/1684472754597142529/tyM92sRA_400x400.jpg)
### Category
编程、多智能体 (Multi-agent)

### Description
- “告诉你的 AI 团队你想构建什么微服务，他们会为你完成。你的想象力就是极限！！
- 欢迎来到 Dev-GPT，我们利用先进人工智能的力量将你的想法变为现实！我们的自动化开发团队旨在创建量身定制的微服务，使软件开发流程无缝高效。由虚拟产品经理、开发人员 DevOps 组成，确保项目的每个方面从概念到部署都得到全面覆盖。”

### Links
- [Discord](https://discord.com/invite/AWXCCC6G2P)

</details>

## [Devika](https://github.com/stitionai/devika)
Agentic AI 软件工程师

<details>

![Image](https://github.com/stitionai/devika/raw/main/.assets/devika-screenshot.png)
### Category
编程、通用

### Description
- Devika 是一个 Agentic AI 软件工程师，能够理解高层人类指令，将其分解为步骤，研究相关信息，并编写代码以实现给定目标。
- Devika 旨在成为 Cognition AI Devin 的竞争性开源替代品。

### Links
- [GitHub](https://github.com/stitionai/devika)

</details>

## [Devon](https://github.com/entropy-research/Devon)
开源 Devin 替代品

<details>

![Image]()
### Category
编程、通用

### Description
- Entropy research 出品的开源 Devin 替代品。

### Links
- [GitHub](https://github.com/entropy-research/Devon)

</details>

## [DevOpsGPT](https://github.com/kuafuai/DevOpsGPT)
AI 驱动的软件开发自动化解决方案

<details>

![Image](https://github.com/kuafuai/DevOpsGPT/raw/master/docs/files/intro-flow-simple.png)

### Category
编程

### Description
欢迎来到 AI 驱动的软件开发自动化解决方案，简称 DevOpsGPT。我们将 LLM（大语言模型）与 DevOps 工具结合，将自然语言需求转化为可运行的软件。这一创新功能显著提高了开发效率，缩短了开发周期，降低了沟通成本，从而交付更高质量的软件。

### 特性与优势
* 提高开发效率：无需繁琐的需求文档编写和解释。用户可直接与 DevOpsGPT 交互，快速将需求转化为功能性软件。
* 缩短开发周期：自动化的软件开发流程显著减少了交付时间，加速了软件部署和迭代。
* 降低沟通成本：通过准确理解用户需求，DevOpsGPT 最小化了沟通和误解的风险，提高了开发与业务团队之间的协作效率。
* 高质量交付物：DevOpsGPT 生成代码并进行验证，确保交付软件的可靠性和质量。
* [企业版] 现有项目分析：通过 AI 自动分析现有项目信息，在现有项目基础上准确分解和开发所需任务。
* [企业版] 专业模型选择：支持比 GPT 更强大的专业领域语言模型服务以更好地完成需求开发任务，并支持私有化部署。
* [企业版] 支持更多 DevOps 平台：可连接更多 DevOps 平台以实现全流程的开发和部署。

### Links
- [Creator Website](https://www.kuafuai.net/)
- [Demo Video](https://youtu.be/IWUPbGrJQOU)

</details>

## [dotagent](https://github.com/dot-agent/dotagent)
在云端、PC 或移动设备上部署 Agent

<details>

![Image](https://avatars.githubusercontent.com/u/133483033?s=200&v=4)

### Category
自定义构建

### Description
- 一个 Agent 管理系统，通过丰富的开发者工具套件促进健壮 AI 应用和实验性自主 Agent 的创建。
- 支持在云端、PC 或移动设备上部署 Agent，并通过 Python 或纯英语集成扩展功能。
- 借助强大的提示词编译器推进提示工程，对语言模型提供更高程度的控制，显著优化响应生成过程。
- 允许将 Agent 无缝导出为便携式文件以在任何环境中执行，并提供可选的 Agentbox 功能用于沙箱环境中的计算资源管理。

### Links
- [YouTube video](https://www.youtube.com/watch?v=uE_fykl8AVI&ab_channel=FahdMirza)

</details>

## [Eidolon](https://eidolonai.com/)
具有可插拔、模块化组件的多 Agent SDK

<details>

![Image](https://www.eidolonai.com/_astro/default.jKAYXmpI_ZWVg5E.webp)

### Category
自定义构建（Agent 构建框架与平台）、AI 应用 SDK

### Description
- Eidolon 是一个开源 AI Agent SDK。

### Links
- [Web](https://eidolonai.com/)
- [GitHub](https://github.com/eidolon-ai/eidolon)
- [LinkedIn](https://www.linkedin.com/company/august-data/)
- [Dave Brewster - LinkedIn](https://www.linkedin.com/in/dave-brewster-first/)
- [Ravi Ramachandran - LinkedIn](https://www.linkedin.com/in/ravi-nextlevelgtm/)
- [Luke Lalor - LinkedIn](https://www.linkedin.com/in/lukehlalor/)

</details>

## [English Compiler](https://github.com/uilicious/english-compiler)
将 Markdown 规范转换为可运行代码

<details>

![Image](https://github.com/uilicious/english-compiler/raw/main/notes/imgs/EnglishCommand-CLI-help.png)

### Category
编程

### Description
- OC AI 编译器，用于将基于英语的 Markdown 规范转换为功能性代码。
- “我们知道所有伟大的™️项目都始于详尽的功能性规格说明书。这通常是用英语或其许多其他口语变体编写的。
- 那么，如果我们不根据功能规格编写代码，而是直接将其编译为代码呢？
- 迈向一个用纯文本替换几乎所有内容的未来。”

### Links
- [Creator's Twitter](https://twitter.com/picocreator)

</details>

## [evo.ninja](https://evo.ninja/)
根据其任务自适应角色以完成任务的 AI Agent

<details>

![Image](https://camo.githubusercontent.com/3333c49067bddef0b208e36e22cf6ec8066f5be1da1dc327532427a395ed8069/68747470733a2f2f6861636b6d642e696f2f5f75706c6f6164732f4279576a4c4b41686e2e706e67)

### Category
通用、研究、多智能体 (Multi-agent)

### Description
- evo.ninja 的独特之处在于它能根据手头任务实时自适应自身角色。
- Evo 利用预定义的 Agent 角色，这些角色针对特定领域的任务进行了定制。
- 在每次执行循环迭代中，evo 会选择并采用最适合当前任务的 persona（角色）。

### Links
- [Web](https://evo.ninja/)
- [GitHub](https://github.com/polywrap/evo.ninja/)
- [Discord](https://discord.com/invite/r3rwh69cCa)

</details>

## [FastAgency](https://fastagency.ai/latest/)
部署多 Agent 工作流的最快方式

<details>

![Image](https://fastagency.ai/latest/assets/img/logo.svg)

### Category
自定义构建（Agent 构建框架与平台）、AI 应用 SDK、多智能体 (Multi-agent)、支持开源模型

### Description
- “FastAgency 是一个开源框架，旨在加速从原型到生产的多 Agent AI 工作流过渡。
- 对于使用 AutoGen 框架的开发者，FastAgency 使你能够将 Jupyter notebook 原型无缝扩展为功能完备、面向生产的可部署应用。
- 凭借多框架支持、统一的编程接口和强大的 API 集成能力，FastAgency 简化了部署流程，在保持灵活性和性能的同时节省时间和精力。”

### Links
- [Web](https://fastagency.ai/latest/)
- [GitHub](https://github.com/airtai/fastagency)

</details>

## [Flowise](https://flowiseai.com/)
低代码 Agent 构建器

<details>

![Image](https://flowiseai.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-color-high.e60de2f8.png&w=384&q=75)

### Category
自定义构建（Agent 构建框架与平台）

### Description
- Flowise 是一个开源低代码工具，供开发者构建定制的 LLM 编排流程及 AI Agent。

### Links
- [Web](https://flowiseai.com/)
- [GitHub](https://github.com/FlowiseAI/Flowise)
- [X (Twitter)](https://x.com/FlowiseAI)
- [LinkedIn](https://www.linkedin.com/company/flowiseai/)

</details>


## [Friday](https://github.com/amirrezasalimi/friday/)
Node.js AI 开发者助手

<details>

![Image](https://github.com/amirrezasalimi/friday/raw/main/screenshot.png)

### Category
编程

### Description
- 一个能够使用无限提示词生成整个 Node.js 项目的开发者助手。
- 提供用于构建应用基础的核心提示词。
- 允许你添加无限个模块，每个模块都是一个代表应用特定部分的提示词。
- 特性 (Features)
	- Friday 利用 GPT-4 进行 AI 辅助，但已针对 GPT-4-32k 进行测试和优化以获得更快的速度和更好的结果。
	- 你的应用基础需要 2 次请求，你提供的每个模块需要 1 次请求。
	- Friday 在后台使用 esbuild 处理它创建的每个应用。

### Links
- **Author:** [Amirreza Salimi](https://twitter.com/amirsalimiiii)

</details>

## [GeniA](https://github.com/genia-dev/GeniA)
工程化平台 AI 团队成员

<details>

![Image](https://github.com/genia-dev/GeniA/raw/main/media/genia_title.png)

### Category
编程

### Description
- GeniA 能够与你在生产环境中协同工作，在您的开发和云环境（AWS/k8s/Argo/GitHub 等）中代表你执行任务。
- 允许你通过集成自己的工具和 API 来增强平台功能。
- Slack App Bot 集成支持。
- 支持 GPT-3.5 & GPT-4。

### Links
- Authors: [Uri Shamay](https://github.com/cmpxchg16), [Shlomi Shemesh](https://github.com/shlomsh)

</details>

## [Godmode](https://godmode.space/)
受 AutoGPT 和 BabyAGI 启发，拥有出色的 UI

<details>

![Image](https://toolpulse.ai/wp-content/uploads/2023/11/godmode-ai.jpg)

### Category
通用

### Description
- Godmode 是一个受 Auto-GPT 和 BabyAGI 启发的项目，通过精美的 UI 执行各种任务。
- 一个受 AutoGPT 和 BabyAGI 启发的 Web 平台。
- 它能做什么：
	- 在星巴克订购咖啡
	- 进行市场分析
	- 寻找并协商租赁条款
- 支持 GPT-3.5 & GPT-4

### Links
- [GitHub](https://github.com/FOLLGAD/Godmode-GPT)
- Authors: [Emil Ahlbäck](https://twitter.com/emilahlback), [Lonis](https://twitter.com/_Lonis_)
- [Discord](https://discord.com/invite/vSzCcDDwz3)
- [Tweet](https://twitter.com/_Lonis_/status/1646641412182536196)

</details>

## [GPT Discord](https://github.com/Kav-K/GPTDiscord)
用于 Discord 的终极 AI Agent 集成

<details>

![image](https://camo.githubusercontent.com/c02e68bf20c853637e8cfb02c9406bd2b3b20637ea4ed95b7d68819e94a01dfe/68747470733a2f2f692e696d6775722e636f6d2f425A644F52544c2e706e67)

### Category
内容创作、生产力工具、通用、Discord

### Description
- GPT Discord 是一个功能强大的全合一 Discord GPT 界面。
- GPT Discord 支持多模态图像理解、代码解释、高级数据分析、你自己文档的问答、与 Wolfram Alpha 和 Google 联网聊天的 AI 审核、使用 DALL-E 生成图像等大量功能！
- 由 E2B 提供代码执行和环境操作功能。
- ![image](https://camo.githubusercontent.com/6806eb5cd7f4a14e693bc732a304f18c5413a493c92b4b73202ec3205017b9c8/68747470733a2f2f692e696d6775722e636f6d2F547366677455322E706e67)
- 支持的 LLMs/模型提供商：
  - OpenAI 模型

### Links
- [GitHub](https://github.com/Kav-K/GPTDiscord)
- [Kaveen Kumarasinghe - founder of GPT Discord - website](https://kaveenk.com/)
- [Kaveen Kumarasinghe - founder of GPT Discord - LinkedIn](https://www.linkedin.com/in/kaveenk/)

  
</details>

## [GPT Engineer](https://gptengineer.app/)
根据提示词生成整个代码库

<details>

![Image](https://pbs.twimg.com/media/GDA3bYrXYAE5XDQ?format=jpg&name=4096x4096)

### Category
编程

### Description
GPT Engineer 是一个 AI Agent，根据提示词生成整个代码库。
- 模型：GPT 4
- 指定你的项目后，AI Agent 会询问澄清问题，然后构建整个代码库。
- 特性 (Features)
	- 易于适应、扩展和让 Agent 学习你期望的代码风格。它根据提示词生成整个代码库。
	- 你可以通过编辑 identity 文件夹中的文件来指定 AI Agent 的“身份”。
	- 目前，编辑身份和演进主提示词是让 Agent 在项目间记住信息的方式。
	- steps.py 中的每个步骤都会将其与 GPT4 的通信历史存储在 logs 文件夹中，并可以使用 scripts/rerun_edited_message_logs.py 重新运行。


### Links
- [Web](https://gptengineer.app)
- [GitHub](https://github.com/AntonOsika/gpt-engineer)
- [Discord](https://discord.com/invite/8tcDQ89Ej2)
- Author: [Anton Osika](https://twitter.com/antonosika)
- [Twitter review by @Attack](https://twitter.com/Attack/status/1671165869064609792)

</details>

## [GPT Migrate](https://github.com/0xpayne/gpt-migrate)
在框架/语言之间迁移代码库

<details>

![Image](https://opengraph.githubassets.com/678543c5159118a70ea974db32bb95b310a3fbb6ad4296e97d54335031f8df82/joshpxyne/gpt-migrate)

### Category
编程

### Description
GOT Migrate 可轻松将你的代码库从一个框架或语言迁移到另一个。
- 选择不同的 LLMs。
- 允许 GPT Migration 为新代码库生成并运行单元测试的能力。
- 能够选择迁移的源和目标语言。
- 自定义 Agent 工作流（设置 -> 迁移 -> 测试）的能力。
- GPT Migrate 团队正在为 Agent 添加 [基准测试](https://github.com/0xpayne/gpt-migrate#-benchmarks)。

### Links
- [Website](https://gpt-migrate.com/)
- Author: [Josh Payne](https://twitter.com/joshpxyne)
- [Announcement](https://twitter.com/joshpxyne/status/1675254164165910528)


</details>

## [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot)
从零开始编写整个可扩展应用

<details>

![Image](https://techcrunch.com/wp-content/uploads/2023/08/gpt_pilot_logo.png?w=150)

### Category
编程

### Description
GPT Pilot 是一个 AI Agent，在你监督代码编写的同时为你编写整个应用。
- 一个开发工具，在开发人员监督实施的过程中从零开始编写可扩展的应用。
- 一项研究项目，探索如何利用 GPT-4 生成完全可运行、面向生产的可部署应用。
- 主要思想是 AI 可以编写应用的大部分代码（可能是 95%），但剩下的 5% 需要开发人员参与，直到我们实现完全的 AGI。

### Links
- [GitHub](https://github.com/Pythagora-io/gpt-pilot)
- [Discord](https://discord.com/invite/HaqXugmxr9)


</details>


## [GPT Researcher](https://github.com/assafelovic/gpt-researcher)
研究整个互联网任何主题的 Agent

<details>

![Image](https://camo.githubusercontent.com/b3ab3e2b5612657816d64e174672498cd50027b75aa0a795833aee2ddab585b2/68747470733a2f2f636f7772697465722d696d616765732e73332e616d617a6f6e6177732e636f6d2f6172636869746563747572652e706e67)

### Category
研究、科学

### Description
GPT Researcher 是一个基于 GPT 的自主 Agent，对任何给定主题进行在线全面研究。
- 可生成详细、事实准确且无偏见的研究报告。
- 提供自定义选项以聚焦相关资源、大纲和课程。
- 解决了速度和确定性问题，通过并行化 Agent 工作而非同步操作提供更稳定的性能和更快的速度。
- 受 AutoGPT 和 Plan-and-Solve 论文启发。
- 主要思想是运行“规划器”和“执行者”Agent，其中规划器生成研究问题，执行者根据每个生成的研究问题寻找最相关的信息。

### Links
- [Website](https://tavily.com/)
- [Discord](https://discord.com/invite/2pFkc83fRq)
- Author: [Assaf Elovic](https://twitter.com/assaf_elovic)


</details>

## [GPT Runner](https://github.com/nicepkg/gpt-runner)
与你的文件对话的 Agent

<details>

![image](https://repository-images.githubusercontent.com/640476297/30741f73-caac-48bc-b500-1b7d6efde4c4)

### Category
研究、科学

### Description
- 与你选择的文件进行对话，无需嵌入向量，无需向量数据库！
- 它也是一个 AI 提示词故事书。你可以用它与团队管理一些 AI 预设配置。它支持任何 IDE 和语言开发者。我们提供 CLI 来运行 Web 版和 VSCode 扩展，Jetbrains 插件即将推出。
- 隐私优先，所有数据均在本地。
- 同时支持 OpenAI 和 Anthropic (Claude-2)。
- 支持多种语言。

### Links
- [Website](https://github.com/nicepkg/gpt-runner)
- Author: [Jinming Yang](https://github.com/2214962083)


</details>

## [GPTSwarm](https://gptswarm.org/)
语言 Agent 作为可优化图结构

<details>

![image](https://gptswarm.org/images/gptswarm.png)

### Category
自定义构建（Agent 构建框架与平台）、通用、多智能体 (Multi-agent)

### Description
- 🐝 GPTSwarm 是一个基于图的 LLM 驱动 Agent 框架，提供两个高级功能：
  - 让你能够从图中构建 LLM 驱动的 Agent。
  - 启用 Agent 群的自定义和自动自我组织，具备自我改进能力。
- 人们提出了各种人类设计的提示工程技巧来改善基于大语言模型 (LLMs) 的问题解决器，产生了大量不同的代码库。我们通过将 LLM 驱动的 Agent 描述为计算图来统一这些方法。每个节点实现处理多模态数据或查询其他 LLMs 的函数。每条边描述操作和 Agent 之间的信息流。图可以递归组合成更大的复合图，表示跨 Agent 协作的层次结构。我们的新型自动图优化器 (1) 细化节点级 LLM 提示词（节点优化）并 (2) 通过更改图连接性来改进 Agent 编排（边优化）。实验表明，我们的框架可用于高效开发、集成和自动改进各种 LLM Agent。


### Links
- [Web](https://gptswarm.org/)
- [GitHub](https://github.com/metauto-ai/GPTSwarm)
- [Founder's X (Twitter)](https://twitter.com/MingchenZhuge)


</details>


## [IX](https://github.com/kreneskyp/ix)
Agent 构建、调试和部署平台

<details>

![image](https://github.com/kreneskyp/ix/raw/master/ix_350.png)

### Category
自定义构建、多智能体 (Multi-agent)

### Description
IX 是一个用于构建、调试和部署协作 Agent 及认知工作流的平台。
- IX 是一个基于 LangChain 的 Agent 平台，包含构建和部署协同完成任务的 Agent 舰队所需的所有工具。IX 既是编辑器也是运行时。编辑器是一种无代码图风格编辑器，用于设计 Agent、链、工具、检索函数和协作工作流。

- 直观的图风格无代码编辑器。
- 水平扩展的 Agent 工作者集群。
- 多用户、多 Agent 聊天界面。
- 智能输入自动补全 `@mentions` 和 `{file}` 引用。
- 支持 Chroma 和其他向量数据库进行文档搜索。
- 支持 OpenAI API、Anthropic、PaLM 和基于 LLama 的模型。
- 组件库易于扩展。
- 由 LangChain 驱动。

### Links

- [Youtube](https://www.youtube.com/watch?v=hAJ8ectypas&list=PLR8AMvFecu1hyMHFzaehbfFcMcECMafVs)
- [Discord](https://discord.gg/jtrMKxzZZQ)
- [Author's Twitter](https://twitter.com/kreneskyp)

</details>


## [JARVIS](https://github.com/microsoft/JARVIS)
将 LLMs 与机器学习社区连接的系统

<details>

![image](https://github.com/microsoft/JARVIS/raw/main/hugginggpt/assets/intro.png)

### Category
通用

### Description
JARVIS 是一个将 LLMs 与机器学习 (ML) 社区连接的系统。
- 任务规划：使用 ChatGPT 分析用户请求以理解其意图，并将其分解为可能可解决的任务。
- 模型选择：为解决规划出的任务，ChatGPT 根据描述从 Hugging Face 上托管的专家模型中进行选择。
- 任务执行：调用并执行每个选定的模型，并将结果返回给 ChatGPT。
- 响应生成：使用 ChatGPT 整合所有模型的预测并生成响应。

### Links

- [Paper](https://arxiv.org/abs/2303.17580)

</details>

## [Langroid](https://github.com/langroid/langroid)
用于构建 LLM 应用的多 Agent 框架

<details>

![image](https://github.com/langroid/langroid/raw/main/docs/assets/langroid-card-lambda-ossem-rust-1200-630.png)

### Category
通用、自定义构建

### Description


`Langroid` 是一个直观、轻量级、可扩展且原则严谨的 Python 框架，用于轻松构建 LLM 驱动的应用。
你设置 Agent，为它们配备可选组件（LLM、向量存储和方法），分配任务，让它们通过交换消息协作解决问题。
这种多 Agent 范式受 [Actor Framework](https://en.wikipedia.org/wiki/Actor_model) 启发（但你不需要了解任何关于此的知识！）。

`Langroid` 是对 LLM 应用开发的全新视角，在简化开发者体验方面进行了大量思考；它不使用 `Langchain`。

- 兼容大多数商业/远程和本地/开源 LLMs。
- 设置多 Agent、多 LLM 系统：为需要强推理和指令遵循的 Agent 使用更强的 LLMs，将简单任务委托给较弱/本地 LLMs。 
- 支持 OpenAI 函数调用以及称为 `ToolMessage` 的原生等效功能，可与没有内置函数调用的 LLMs 配合使用。只需指定结构为 (嵌套) Pydantic 对象即可。
- 开箱即用：包含用于 RAG（检索增强生成）、缓存、日志/可观测性的向量数据库。
- 提供专用 Agent：`DocChatAgent`、`SQLChatAgent`、`TableChatAgent`（适用于表格数据，如 csv/dataframes）。
- `DocChatAgent` 处理文本、PDF、Docx 文件/URLS，并拥有结合词汇和语义搜索的最先进检索技术。
- 文档：https://langroid.github.io/langroid/
</details>

## [Lemon Agent](https://github.com/felixbrock/lemon-agent)
用于工作流自动化的 Plan-Validate-Solve Agent

<details>

![image](https://pbs.twimg.com/media/F3l2kEsXIAA0Gsm?format=jpg&name=large)

### Category
生产力工具、编程

### Description
Lemon Agent 是一个计划-验证-求解 (PVS) Agent，用于准确、可靠且可重现的工作流自动化。
- 一个独立监督的计划与求解 Agent，专门针对在各种工具（如 GitHub、HubSpot 或 Airtable）上执行读写操作。（ACL 2023 论文 "[Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091)"）。
- **任务分离与人机交互**：Lemon Agent 目前持有规划器 Agent (Planner Agent) 和解码器 Agent (Solver Agent) 以保持专注并提高准确性。我们计划很快添加更多 Agent。此外，Lemon Agent 将在相关的工作流步骤中请求批准以确保预期操作被执行。
- **无限配置选项**：在定义工作流时，Lemon Agent 为你提供无限的配置选项（见此处示例）。例如，你可以告诉 Lemon Agent 在执行工作流步骤前请求权限，或每次模型执行工作流步骤时讲一个 🧔‍♀️ 冷笑话。
- **UI 灵活性**：可在其之上构建任何 UI，或通过内置 CLI 与 Lemon Agent 交互。
- **[即将推出] 模型与框架无关的操作**：Lemon Agent 是一个独立 Agent，但可轻松集成到 LangChain 等框架中并与任何模型配合使用。
- **附加功能**：识别你 Agent 决策能力中的薄弱环节，并通过进一步配置你的 Lemon Agent 工作流向更确定性的行为转变。**（.html 文件，无需额外安装即可运行）**

### Links

- [Discord](https://discord.gg/fWU4rDYSxw)
- [Author's Twitter](https://twitter.com/felixbrockm)

</details>

## [LLM Agents](https://github.com/mpaepper/llm_agents)
用于构建 Agent、使用工具、规划的库

<details>

![image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
编程

### Description
一个极简主义的库，用于构建利用大语言模型通过命令循环和工具集成来自动执行任务的 Agent。
- 在 REPL 环境中执行 Python 代码。
- 在 Google 和 Hacker News 上进行搜索。
- 基于集成工具的输出生成思考、行动、观察和新思考的循环。
- 动态将新信息附加到提示词中以使 Agent 能够做出知情决策。

### Links

- [GitHub](https://github.com/mpaepper/llm_agents)
- [Blog](https://www.paepper.com/blog/posts/intelligent-agents-guided-by-llms/)

</details>

## [LLM Stack](https://llmstack.ai/)
构建 LLM Agent 的无代码平台

<details>

![image](https://llmstack.ai/img/logo-grayscale.svg)

### Category
自定义构建、无代码、Web UI

### Description
- LLM Stack 是一个用于使用你的数据构建 LLM Agent、工作流和应用的无代码平台。
- LLMStack 支持所有主要模型提供商，如 OpenAI、Cohere、Stability AI、Hugging Face 等。轻松使用这些模型来构建强大的应用。
- 借助 LLM Stack，你可以编写任何代码即可构建生成式 AI Agent（如 AI SDR、研究分析师、RPA 自动化等）。将 Agent 连接到你的内部或外部工具，让 Agent 搜索网络或浏览互联网。
- 支持的 LLMs/模型提供商：
  - OpenAI
  - Cohere
  - Stability AI
  - Hugging Face

### Links
- [Web](https://llmstack.ai/)
- [GitHub](https://github.com/trypromptly/LLMStack)
- [Blog](https://llmstack.ai/blog)

</details>

## [Local GPT](https://github.com/PromtEngineer/localGPT)
在不牺牲隐私的情况下与文档对话

<details>

![image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
研究、数据分析、通用

### Description
LocalGPT 是一个开源项目，允许你在不牺牲隐私的情况下与你的文档进行对话。受 privateGPT 启发，允许使用你自己的文档作为信息来源。

- 在你的本地设备上使用 GPT 模型与你的文档聊天。数据不会离开你的设备，100% 私密。
- 由于所有内容都在本地运行，你可以放心数据永远不会离开你的计算机。
- 深入 LocalGPT 的安全本地文档交互世界。
- README 上的大部分描述受原始 privateGPT 启发。
- 模型：Vicuna-7B。
- 使用 InstructorEmbeddings。
- Embeddings 和 LLM 都将在 GPU 上运行。它也支持 CPU（如果你没有 GPU）。
- 基于 Langchain 构建。


### Links

- [GitHub](https://github.com/PromtEngineer/localGPT)
- [Subreddit](https://www.reddit.com/r/LocalGPT/)
- [YouTube - LocalGPT: OFFLINE CHAT FOR YOUR FILES [Installation & Code Walkthrough]](https://www.youtube.com/watch?v=MlyoObdIHyo&ab_channel=PromptEngineering)

</details>


## [Loop GPT](https://github.com/farizrahman4u/loopgpt/tree/main)
作为 Python 包重新实现的 AutoGPT

 <details>

 ![image](https://github.com/farizrahman4u/loopgpt/raw/main/docs/assets/imgs/loopgpt_demo_pic.png?raw=true)

### Category
通用

### Description
Loop GPT 是对流行的 Auto-GPT 项目的重新实现，作为一个规范的 Python 包编写，注重模块化和可扩展性。
- 语言：Python。
- 默认模型：GPT-3.5-turbo（也可使用 GPT-4）。
- 模块化 Auto-GPT 框架。
- “即插即用” API - 可扩展且模块化的“Pythonic”框架，不仅仅是一个命令行工具。
- 特性 (Features)
	- “易于添加新功能、集成和自定义 Agent 能力，全部通过 Python 代码实现，无需讨厌的配置文件！”
	- “最小提示词开销 - 每个 Token 都很重要。我们持续努力以最少的 Token 获得最佳结果。”
	- “人在回路 (Human in the Loop) - 能够通过人类反馈对偏离轨道的 Agent 进行‘纠偏’的能力。”
	- “完整状态序列化 - 可将 Agent 的完整状态（包括其记忆和工具状态）保存到文件或 Python 对象中。无需外部数据库或向量存储（但仍支持它们）！”

<!--
### Features
- "Easy to add new features, integrations and custom agent capabilities, all from python code, no nasty config files!"
- "Minimal prompt overhead - Every token counts. We are continuously working on getting the best results with the least possible number of tokens."
- "Human in the Loop - Ability to "course correct" agents who go astray via human feedback."
- "Full state serialization - can save the complete state of an agent, including memory and the states of its tools to a file or python object. No external databases or vector stores required (but they are still supported)!"

-->
</details>

## [L2MAC](https://github.com/samholt/l2mac)
能够生成大型复杂代码库和整本书的 Agent 框架

<details>

 ![image](https://raw.githubusercontent.com/samholt/L2MAC/master/docs/public/l2mac-icon-white.png)

### Category
多智能体 (Multi-agent)、编程、自定义构建

### Description
L2MAC 是一个多 Agent 生成框架，单个输入提示词即可生成广泛的无界输出，如整个代码库或整本书。
- L2MAC 能够在非常长的生成任务中创建与用户输入提示词完全对齐的近乎无限输出。
- 它在大型代码库任务的最新基准测试中表现出强大的实证性能，并在 HumanEval 编码全球排名中位列前三。由于 L2MAC 可在生成代码时检测无效代码和失败的单元测试并自动纠错。
- 内部持久化完整的文件存储记忆，使 LLM Agent 能够读取文件和写入文件，在多次迭代中创建大型输出。
- 可指示其遵循精确的提示词程序。
- 由于它一次生成输出的一部分，因此允许具有固定上下文 Token 限制的 LLM 被绕过限制。
- 介绍 L2MAC 的论文已在 ICLR 2024 经过同行评审并 recently accepted and published。


### Links  
- [GitHub](https://github.com/samholt/l2mac)
- [Discord](https://discord.gg/z27cxnwdhY)
- [Twitter](https://twitter.com/samianholt)
- [Paper - L2MAC: Large Language Model Automatic Computer for Extensive Code Generation](https://arxiv.org/abs/2310.02003)

</details>


## [Maige](https://maige.app)
GitHub 仓库的自然语言工作流。

<details>

 ![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNrQ3hXkHi0qTI-XThXwx7wA33LcAZZzLp5af6UjY0Vg&s)

### Category
编程、生产力工具、调试、多智能体 (Multi-agent)
	
### Description
- Maige 是一个代码库 Agent，在新 Issue 和 Pull Request 出现时运行。其核心功能是标记、分配和回答问题。
- Maige 可以搜索整个代码库，启动沙箱运行脚本，甚至编写基础代码。

### Links  
- [Web](https://maige.app)
- [GitHub](https://github.com/RubricLab/maige)
- [Video - testing Maige](https://www.youtube.com/watch?v=YN-y-iweZTc&ab_channel=TerezaTizkova)
- [Interview - founder about building Maige](https://e2b.dev/blog/building-open-source-codebase-copilot-with-code-execution-layer)
- [X (Twitter)](https://twitter.com/rubriclabs)
- [Founder's X - Ted Spare](https://twitter.com/tedspare)
</details>

## [Magick](https://www.magickml.com/)
用于创建、部署和变现 Agent 的 AIDE

<details>

 ![image](https://assets-global.website-files.com/6507b4af22875d0b8abf95a7/6507bbdc3085cf26d1e8041e_white-wm-tiny.png)

### Category
编程、Agent SDK、自定义构建
	
### Description
Magick 是一个用于创建、部署、扩展和变现有用 AI Agent 以及提示词链的 AIDE。
- 一套完整的模型无关 AIDE，用于创建、部署、扩展和变现有用的 AI Agent 及提示词链。 
- Magick 允许在 1 小时内构建 BabyAGI。你可以实时观看图执行过程，观察其思考过程并理解流程。
- “自主 Agent 的可视化开发即将到来。我们专门针对认知架构的快速开发和可扩展的事件驱动型自主 Agent 构建了 Magick。”

### Links  
- [Web](https://www.magickml.com/)
- [GitHub](https://github.com/Oneirocom/Magick)
- [X](https://twitter.com/magickml)
- [Discord](https://discord.com/invite/7Xx5DmbJCe)
- [LinkedIn](https://www.linkedin.com/company/magickml/)
- [Founder's LinkedIn - Jesse Alton](https://www.linkedin.com/in/mrmetaverse/)
- [Founder's LinkedIn - Michael Sharpe](https://www.linkedin.com/in/michaelpsharpe/)

</details>

## [MemFree](https://github.com/memfreeme/memfree)
开源混合 AI 搜索引擎

<details>

 ![image](https://raw.githubusercontent.com/memfreeme/memfree/main/frontend/public/og.png)

### Category
开源、AI 搜索、自定义构建

### Description

开源混合 AI 搜索引擎，即时从互联网、书签、笔记和文档中获取准确答案。

- 一键同步并索引 Chrome 书签。
- 支持多种传统搜索引擎作为来源。
- 自托管超快无服务器向量数据库。
- 自托管超快本地嵌入与重排序服务。
- 全代码开源。
- 生产环境一键部署。

### Links  
- [Documentation](https://www.memfree.me/docs)
- [Discord](https://discord.com/invite/7QqyMSTaRq)
- [Twitter](https://twitter.com/ahaapple2023)
- [Website](https://www.memfree.me)

</details>


## [MemGPT](https://github.com/cpacker/MemGPT)
记忆管理系统，为 LLM 提供上下文

<details>

 ![image](https://files.readme.io/da7f719-small-memgpt_logo_circle_nuno.png)

### Category
记忆管理、数据分析
	
### Description
- 一个智能管理系统，用于在 LLMs 中管理不同的记忆层级，以有效提供扩展上下文。LLM 的有限上下文窗口内。 
- 与你的数据聊天——与你本地的文件或 SQL 数据库对话。
- 创建具有自我编辑记忆的永久聊天机器人。

### Links  
- [Paper](https://arxiv.org/abs/2310.08560)
- [Documentation](https://memgpt.readthedocs.io/)
- [Discord](https://discord.gg/9GEQrxmVyE)
- [Hugging Face](https://huggingface.co/MemGPT)

</details>

## [Mentat](https://github.com/biobootloader/mentat)
从命令行协助你完成编码任务

<details>

 ![image](https://assets-global.website-files.com/64bad175c3f1fe8957a06faf/64bef0d57ca34f97c26b2c63_abante-ai-icon_transparent_271.png)

### Category
编程

### Description
Mentat 是一个 AI 工具，直接从你的命令行协助你完成任何编码任务。
与 Copilot 不同，Mentat 协调跨多个位置和文件的编辑操作。与 ChatGPT 不同，Mentat 已经拥有你项目的上下文——无需复制粘贴！

### Links  
- [Website](https://www.mentat.codes/)
- [Youtube](https://www.youtube.com/watch?v=lODjaWclwpY)
- Author: [Bio Bootloader](https://twitter.com/bio_bootloader) (Twitter)
- [Discord Invite](https://discord.com/invite/zbvd9qx9Pb)

</details>


## [MetaGPT](https://github.com/geekan/MetaGPT)
返回 PRD、任务或代码库的 Agent 框架

<details>

 ![image](https://github.com/geekan/MetaGPT/raw/main/docs/resources/MetaGPT-new-log.png)

### Category
多智能体 (Multi-agent)、编程、自定义构建

### Description
MetaGPT 是一个多 Agent 框架，给定一行需求即可返回 PRD、设计、任务或代码库。
- MetaGPT 允许为 GPTs 分配不同角色以形成协作软件实体处理复杂任务。
- 它以单行需求作为输入，输出用户故事/竞争分析/需求/数据结构/API/文档等。
- 内部包含产品经理/架构师/项目经理/工程师。
- 它提供整个软件公司的流程以及精心编排的 SOP（标准操作流程）。Code = SOP(Team) 是核心哲学。
- 关于 LLM 驱动的多 Agent 工作的论文推动了自主 Agent 协作以完成单人无法完成的复杂任务的理念。
- MetaGPT 将高效的人类工作流作为元编程方法纳入基于 LLM 的多 Agent 协作中。


### Links  
- [GitHub](https://github.com/geekan/MetaGPT)
- [Discord](https://discord.com/invite/4WdszVjv)
- [Twitter](https://twitter.com/DeepWisdom2019)
- [Paper - MetaGPT: Meta Programming for Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352)

</details>

## [Mini AGI](https://github.com/muellerberndt/mini-agi)
基于 GPT-3.5 / GPT-4 的通用 Agent

<details>

 ![image](https://github.com/muellerberndt/mini-agi/raw/main/static/mini-agi-cover.png)

### Category
通用

### Description
- MiniAGI 是一个基于 GPT-3.5 / GPT-4 的最小化通用自主 Agent。
- 可分析股票价格、执行网络安全测试、创作艺术并订购披萨。
- MiniAGI 是一个简单的自主 Agent，兼容 GPT-3.5-Turbo 和 GPT-4。
- 它结合了强大的提示词与最小工具集、思维链 (chain-of-thoughts) 以及带摘要功能的短期记忆。
- 具备内心独白和自我批评能力。


### Links
- [GitHub](https://github.com/muellerberndt/mini-agi)

</details>


## [Multiagent Debate](https://github.com/composable-models/llm_multiagent_debate)
多智能体辩论论文的复现实现

<details>

 ![image](https://composable-models.github.io/llm_debate/img/accuracy_small.png)

 ### Category
通用、多智能体 (Multi-agent)

### Description
Multiagent Debate 是论文“Improving Factuality and Reasoning in Language Models through Multiagent Debate”的实现。
- 该论文展示了我们如何将同一语言模型的不同实例视为一个“多 Agent 社会”，其中单个语言模型生成并批评其他语言模型实例的语言生成结果。
- 作者发现，经过此过程后生成的最终答案在事实准确性上更准确，并能更准确地解决推理问题。
- 说明了不同领域中多 Agent 辩论与单 Agent 生成在推理和事实有效性方面的定量差异。


### Links
- [GitHub](https://github.com/composable-models/llm_multiagent_debate)
- [Project page](https://composable-models.github.io/llm_debate/)
- [Paper](https://arxiv.org/abs/2305.14325)

</details>


## [Multi GPT](https://github.com/rumpfmax/Multi-GPT)
实验性多 Agent 系统

<details>

 ![image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
通用

### Description
- 一个开源的实验性尝试，旨在让 GPT-4 完全自主化。
- 多个“专家GPTs”协作执行任务。
- 每个都有长短期记忆并能相互通信。
- 特性 (Features)
	- 设定任务并观看专家们开始工作。
	- 提供互联网访问以进行搜索和信息收集。
	- 长期和短期记忆管理。
	- 使用 GPT-4 实例进行文本生成。
	- 可访问热门网站和平台。
	- 使用 GPT-3.5 进行文件存储与摘要总结。

### Links
- [Demo](https://www.loom.com/share/b6bec93065794eb8a47e2109697afa39)
- Authors: [Max Rumpf](https://twitter.com/md_rumpf) and [Significant Gravitas](https://twitter.com/SigGravitas)

</details>

## [MutahunterAI](https://github.com/codeintegrity-ai/mutahunter)
MutahunterAI：通过开源 AI 加速开发者生产力和代码安全

<details>

![Image](https://avatars.githubusercontent.com/u/152569327?s=48&v=4)

### Category
开发者工具、软件安全、多智能体 (Multi-agent)、通用

### Description
- 使用 Mutahunter 为你的代码库生成单元测试，专门针对代码漏洞。通过精准定位代码弱点，提升开发者生产力。
- 与盲目生成测试用例的 Copilots 不同，Mutahunter 利用我们的变异测试引擎生成专门针对你代码中漏洞的单元测试。
- 特性 (Features)
	- 支持所有主流语言。
	- 可在本地使用或集成到你现有工作流中的任何 CI/CD 运行器中。
	- 你可以使用自己的 LLM API 来保护隐私。

### Links
- [Documentation](https://github.com/codeintegrity-ai/mutahunter?tab=readme-ov-file#mutahunter) 
- [Discord](https://discord.gg/9P5V9qmKJn)
- [GitHub](https://github.com/codeintegrity-ai/mutahunter)
</details>

## [NLSOM](https://github.com/mczhuge/NLSOM)
基于自然语言的心智社会 (Societies of Mind)
<details>

 ![image](https://github.com/mczhuge/NLSOM/raw/main/assets/nlsom.svg)

### Category
科学、多模态、社交、多智能体 (Multi-agent)

### Description
- 基于自然语言的心智社会 - 包含 Agent 的社会和社区概念。
- 一个包含社会和 Agent 社区的概念框架。
- Agent 可以是 LLMs、基于 NN 的专家、API 和角色扮演者。它们全部使用自然语言通信。
- 为了解决任务，这些 Agent 使用协作式“思维风暴” (Mindstorm) 过程进行相互访谈。
- NLSOM 的额外组件可以以模块化方式轻松添加。
- “是什么魔法让我们变得聪明？这个魔法就是没有魔法。智能的力量源于我们巨大的多样性，而非任何单一完美的原则。” — Marvin Minsky, The Society of Mind, p. 308

### Links
- [GitHub](https://github.com/mczhuge/NLSOM)
- [Paper](https://arxiv.org/pdf/2305.17066.pdf)
- [Author's X - Jürgen Schmidhuber](https://twitter.com/SchmidhuberAI)
- [Author's X - Mingchen Zhuge](https://twitter.com/MingchenZhuge)

</details>

## [OpenAgents](https://github.com/xlang-ai/OpenAgents)
多 Agent 通用平台
<details>

 ![image](https://github.com/xlang-ai/OpenAgents/raw/main/pics/openagents_overview.png)

### Category
通用

### Description
OpenAgents 是一个面向野外环境的语言 Agent 开放平台，是研究人员、开发者和普通用户的 ChatGPT Plus 复刻版。
- 以用户为中心：Chat Web UI / 高效 Agent / 在线演示。
- 完全开源：全栈式 / 易于部署。
- 可扩展性：LLMs / 工具 / Agent 方法。

### Links
- [GitHub](https://github.com/xlang-ai/OpenAgents)
- [Paper](https://arxiv.org/abs/2310.10634)
- [Demo](https://chat.xlang.ai/)

</details>


## [OpenAGI](https://github.com/agiresearch/OpenAGI)
研发 Agent 平台

<details>

 ![image](https://github.com/agiresearch/OpenAGI/raw/main/images/illustration.png)

### Category
通用

### Description
OpenAGI 是一个开源 AGI 研发平台，支持基准任务和开放式任务。
- 由 GPT-4、Vicuna、LLaMA 和 Flan-T5 等各种语言模型驱动。
- 支持多模态工具学习和任务解决，如文本、图像、视频和音频。
- 支持将任务分解为线性任务求解计划和非线性任务求解计划。
- 允许基准任务求解和开放式任务求解。
- 提供易于使用的评估协议来评估任务求解能力。
- 提供基于任务反馈的强化学习 (RLTF) 以允许 Agent 持续自我改进。

### Links
- [GitHub](https://github.com/agiresearch/OpenAGI)
- [Paper](https://arxiv.org/abs/2304.04370)
- [Demo](https://www.youtube.com/watch?v=7RaXPPXi0-Y)

</details>

## [OpenDevin](https://github.com/OpenDevin/OpenDevin)
OpenDevin：少写代码，多做事情

<details>

![Image](https://github.com/OpenDevin/OpenDevin/raw/main/logo.png)
### Category
编程、通用

### Description
- OpenDevin 项目源于复制、增强和创新原始 Devin 模型的愿望。
- 通过吸引开源社区参与，我们旨在解决代码 LLMs 在实际场景中面临的挑战，产生显著贡献于社区的成果并为未来进展铺平道路。


### Links
- [GitHub](https://github.com/OpenDevin/OpenDevin)

</details>


## [Open Interpreter](https://openinterpreter.com/)
让 LLMs 执行代码的代码解释器

<details>

 ![image](https://openinterpreter.com/assets/ncu_thumbnail.jpg)

### Category
编程

### Description
Open Interpreter 是一个开源解释器，允许 LLMs 在您的计算机上运行代码以完成任务。
- 本地运行。
- 例如可总结 PDF、可视化数据集、控制你的浏览器。
- 在你的终端中以类似 ChatGPT 的界面工作。

### Links
- [Web](https://openinterpreter.com/)
- [GitHub](https://github.com/KillianLucas/open-interpreter)
- [Author's Twitter](https://twitter.com/hellokillian)

</details>

## [Pezzo](https://www.pezzo.ai/)
提示词管理及其他开发工具包

<details>

 ![image](https://www.pezzo.ai/_next/static/media/Logo.b7e3878b.svg)

### Category
编程

### Description
Pezzo 是一个旨在简化提示词设计、版本管理、发布、协作、故障排除和可观测性的开发工具包。
- “无论你是技术人员还是利益相关者，都可以有效使用 Pezzo。我们不认为 AI 提示词应该在开发者的代码编辑器中设计。除了技术上的问题外，这还会阻碍生产力。”
- 特性 (Features)
	- 集中式提示词管理：在一个地方管理所有 AI 提示词以实现最大可见性和效率。
	- 简化提示词设计、发布与版本控制：轻松创建、编辑、测试和发布提示词。
	- 可观测性：访问详细的提示词执行历史、统计数据和指标（持续时间、提示词成本、完成成本等）以获得更好的洞察。
	- 故障排除：毫不费力地解决你的提示词问题。时间旅行以回溯微调失败的提示词并立即提交修复。
	- 成本透明度：跨所有提示词和 AI 模型获得全面的成本透明度。
	- 简化集成：使用 Pezzo Client 消耗你的 AI 提示词，无论模型提供商如何，减少 90% 的代码开销。

### Links
- [Documentation](https://docs.pezzo.ai/docs/intro.html)
- [GitHub](https://github.com/pezzolabs/pezzo)
</details>

## [Private GPT](https://www.privategpt.io/)
用于私密文档交互的工具

<details>

![image](https://assets-global.website-files.com/6408872e49e0944a088f17c1/640f3c6e8640895f2cbf95ba_logo%20full.svg)

### Category
研究、数据分析

### Description
Private GPT 是一个用于私密与文档交互的工具，无需互联网连接。
- 基于 LangChain、GPT4All、LlamaCpp、Chroma 和 SentenceTransformers 构建。
- 一个测试项目，验证使用 LLMs 和向量嵌入进行完全私问答的可行性，尚未达到生产就绪状态。


### Links
- [GitHub](https://github.com/imartinez/privateGPT)

</details>

## [PromethAI](https://github.com/topoteretes/PromethAI-Backend)
帮助营养和其他目标的 AI Agent

<details>

![image](https://avatars.githubusercontent.com/u/125468716?s=280&v=4)
### Category
生产力工具、通用

### Description
- “个性化 AI 助手，分解问题，提供解决方案，并让你使用 Agent 操作来自动化你的流程。”
- 特性 (Features)
  	- 通过将请求分解为带有选项集（菜系 -> 欧洲）的类别来帮助达到解决方案。
  	- 拥有动态 UX/UI 以避免提示词输入。
  	- 支持语音输入。
  	- 为用户提供查询结果并围绕它们自动化操作。
  	- 记住你过去的偏好并利用它来优化你的选择。
- 技术 (Tech)
	- 由 Langchain、可分解异步提示词 + 向量 DB + Redis 缓存驱动。
 	- App 使用 Flutter + Dart 构建。
    	- 连接到 Zapier NLP。

### Links
- [GitHub](https://github.com/topoteretes/)
- [Website](https://prometh.ai)
- Author: [Vasilije M](https://twitter.com/tricalt)
</details>


## [React Agent](https://reactagent.io/)
开源 React.js 自主 LLM Agent
<details>

![image](https://reactagent.io/logo-dark.png)

### Category
编程

## Description
- 一个实验性自主 Agent。
- 模型：GPT-4。
- 目的：从用户故事中生成和组合 React 组件。
- Stack (技术栈)
	- React
	- TailwindCSS
	- Typescript
	- Radix UI
	- Shandcn UI
	- OpenAI API
- Agent 获取用户故事文本并基于原子设计原则生成和组合多个 React 组件以生成相关屏幕。
- 特性 (Features)
	- 从用户故事中生成 React 组件。
	- 从现有组件组合 React 组件。
	- 使用本地设计系统生成 React 组件。
	- 使用 React, TailwindCSS, Typescript, Radix UI, Shandcn UI。
	- 基于原子设计原则构建。
- 目前仍处于实验阶段，但结果非常有趣，完全开源，正在寻找贡献者！

## Links
- [GitHub](https://github.com/eylonmiz/react-agent)
- [Documentation](https://docs.reactagent.io/)
- Authors: [Eylon Miz and](https://twitter.com/EylonMiz) and [Lee Twito](https://twitter.com/LeeTwito)

</details>

## [Self-operating computer](https://www.hyperwriteai.com/self-operating-computer)
让多模态模型操作计算机

<details>

![image](https://assets-global.website-files.com/63fcd79d410b22ddf397e1b8/654272554402410a71c84ab9_6405c1cabdf9c69f05b1080e_otherside_logo_symbol.webp)

### Category
生产力工具、研究

### Description
- 使用与人类操作员相同的输入和输出，模型查看屏幕并决定一系列鼠标和键盘操作以达到目标。

### Links
- [Web](https://www.hyperwriteai.com/self-operating-computer)
- [GitHub](https://github.com/OthersideAI/self-operating-computer)

</details>

## [Smol developer](https://github.com/smol-ai/developer)
你自己的初级 AI 开发者，通过 E2B UI 部署

<details>

![image](https://smol.ai/logo.png)

### Category
编程

### Description
Smol 是你自己的初级开发人员。[通过 e2b 在几秒内部署](https://app.e2b.dev/agent/smol-developer/?utm_source=awesome-ai-agents)。
- 以人为中心、连贯的完整程序合成。
- 你自己的初级开发者。
- 允许开发、调试和反编译。
- 200 LOC，一半是英语。
- 100k 上下文可总结内容和代码库。
- Markdown 是最好的提示词 DSL。
- 将错误复制粘贴为提示词。
- 将 curl 输出复制粘贴为提示词。
- 通过描述你想要的来编写 CSS 动画。
- GPT4 >>> GPT3.5/Anthropic Claude 用于代码生成。

### Links
- Author: [Swyx](https://twitter.com/swyx)
- [Demo](https://www.youtube.com/watch?v=UCo7YeTy-aE)
- [Twitter](https://twitter.com/SmolModels)
- [Meme](https://smol.ai/)

</details>

## [Stackwise](https://github.com/stackwiseai/stackwise)
编写 Node.js 函数的 VSCode 扩展

<details>

![image](https://pbs.twimg.com/profile_images/1723911660232945664/CtumfUuB_400x400.jpg)

### Category
Agent 工具、编程

### Description
Stackwise 是一个 VS Code 扩展，编写和导入 Node.js 函数，让你无需切换上下文即可编写代码。
- 开源函数集合。
- 解释你想要的功能做什么，AI 会构建它。
- Stackwise 是一个 VS Code 扩展，自动编写和导入 Node.js 函数，让你无需切换上下文即可编写代码。不再需要搜索文档以集成 API 或与 ChatGPT 来回沟通。只需在你的代码中实现纯粹的功能性！

### Links
- [GitHub](https://github.com/stackwiseai/stackwise)
- [X](https://twitter.com/stackwiseai)
- [Founder's X - Wayne](https://twitter.com/merwanehamadi)
- [Founder's X - Silen Naihin](https://twitter.com/silennai)

</details>

## [Superagent](https://www.superagent.sh/)</details>
允许无代码创建 Agent 的工具

<details>

![image](https://api.typedream.com/v0/document/public/b9d688ba-8f34-40e4-a24a-c62b403b402d/2YukgQsvbVkUp7u1HLsrBKCjfrO_superagent_logo_candidate_2_invisible_background_small.png)

### Category
自定义构建、通用、数据分析

### Description
Superagent 不是一个单独的 Agent，而是一个允许无代码创建 Agent 的工具。
- 简化 LLM Agent 到生产环境的配置和部署。
- “SuperAgent 的核心原则之一是使用任何第三方依赖项来构建专有技术。”
- 它提供一系列功能和功能，使开发者更容易构建、管理和将 AI Agent 部署到生产中，包括内置记忆和通过向量 DB 检索文档、强大工具、Webhooks、定时任务等功能。
- 主要有两种类型的 Agent：动作型 Agent (action agents) 和计划执行型 Agent (plan-and-execute agents)。

### Links
- [GitHub](https://github.com/homanp/superagent)
- [Documentation](https://docs.superagent.sh/introduction)
- [Discord](https://discord.com/invite/mhmJUTjW4b)
- Author: [Ismail Pelaseyed](https://twitter.com/pelaseyed)
- [Interview: Discussing agents' tracing, observability, and debugging with Ismail Pelaseyed, the founder of Superagent](https://e2b.dev/blog/discussing-agents-challenges-with-ismail-pelaseyed-the-founder-of-superagent)
- [Blog post: What Ismail from Superagent and other developers predict for the future of AI Agents](https://e2b.dev/blog/ai-agents-in-2024)

</details>


## [SuperAGI](https://superagi.com/)
开发部署 AI Agent 的框架
<details>

![image](https://pbs.twimg.com/profile_images/1678659510041456640/rxUIfulT_400x400.jpg)

### Category
通用

### Description
SuperAGI 是一个开源自主 AI 框架，用于开发部署自主 Agent。
- 一个 AI Agent 框架。
- 开源，但基础设施是闭源的。
- 特性 (Features)
	- 配置、生成和部署自主 AI Agent。
	- 通过工具扩展 Agent 能力。
	- 无缝运行并发 Agent。
	- 图形用户界面 (GUI)。
	- 操作控制台。
	- 多向量数据库。
	- 多模态 Agent。
	- Agent 轨迹微调。
	- 性能遥测。
	- 优化的 Token 使用。
	- Agent 记忆存储。
	- 循环检测启发式算法。
	- 并发 Agent。
	- 资源管理器。


### Links
- [YouTube](https://www.youtube.com/@_superagi)
- [Discord](https://discord.com/invite/dXbRe5BHJC)
- [Subreddit](https://www.reddit.com/r/Super_AGI/)
- [Twitter](https://twitter.com/_superAGI)
- Author: [Ishaan Bhola](https://twitter.com/ishaanbhola)

</details>


## [Suspicion Agent](https://github.com/CR-Gjx/Suspicion-Agent)
关于不完全信息博弈的论文

<details>

![image](https://github.com/CR-Gjx/Suspicion-Agent/raw/main/figures/counterfactual.png)

### Category
通用

### Description
- 使用具备心智理论 (Theory of Mind) 的 GPT-4 玩不完全信息博弈。
- 该论文深入探讨了 GPT-4 的学习知识在不完全信息游戏中的适用性。


### Links
- [GitHub](https://github.com/CR-Gjx/Suspicion-Agent)
- [Paper](https://arxiv.org/abs/2309.17277)
- [Project demo](https://huggingface.co/spaces/cr7-gjx/Suspicion-Agent-Demo)
- [Game data replay](https://huggingface.co/spaces/cr7-gjx/Suspicion-Agent-Data-Visualization)

</details>


## [SWE Agent](https://github.com/princeton-nlp/SWE-agent)
开源 Devin 替代品

<details>

![Image](https://github.com/princeton-nlp/SWE-agent/raw/main/assets/swe-agent-banner.png)
### Category
编程、通用

### Description
- 这个 Devin 替代品在 FULL SWE 基准测试中得分 12.3%。
- ["一个开源 Devin，在 100% 的 SWE Bench 测试集上获得 12.29%，而 Devin 在 25% 的测试集上获得 13.84%！"](https://x.com/danielhanchen/status/1775120334305607781)
- SWE-agent 通过与专用终端交互来工作，允许它：
	- 🔍 打开、滚动和搜索文件。
	- ✍️ 编辑特定行并自动检查语法。
	- 🧪 编写和执行测试。
- 这个定制构建的界面对于良好性能至关重要。简单地将 LM 连接到普通 bash 终端效果不佳。
- ["我们的关键见解是 LMs 需要精心设计的 Agent-计算机接口（类似于人类喜欢好的 UI 设计）。例如，当 LM 弄乱缩进时，我们的编辑器会阻止它并提供反馈。”"](https://x.com/jyangballin/status/1775114448513958134)
- SWE-agent 由普林斯顿 NLP 团队发布。
- SWE-agent 的特殊之处在于它在 SWE-bench 上的表现几乎与 Devin 相当。
- 值得注意的是，性能会根据 Agent 使用的模型[而变化](https://www.swebench.com/)。
- SWE-agent 相比 Devin 的变更和创新包括：
  - SWE Agent 中的代码通过 Docker 在本地执行。
  - 使用“Agent-计算机接口” (ACI) - 限制界面使 LM 更容易使用。仅允许少数命令：运行代码、查找代码、编辑代码和提交更改到 GitHub。
- Agent 编写的任何代码在提交前都会经过语法检查（linter）。如果语法不正确，Agent 会收到反馈并被迫重写代码。
- Agent 一次只能读取 100 行代码，而不是整个文件。这使得语言模型更容易理解代码。


### Links
- [GitHub](https://github.com/princeton-nlp/SWE-agent)
- [Web](https://swe-agent.com/)
- [Demo](https://swe-agent.com/demo)
- [Discord](https://discord.com/invite/AVEFbBn2rH)

</details>


## [Sweep](https://sweep.dev/)
修复问题并编写代码的 Github 助手

<details>

![image](https://avatars.githubusercontent.com/u/127925974?s=200&v=4)

### Category
编程、GitHub

### Description
Sweep 是一个 GitHub 助手，帮助修复小错误和实现小功能。
- 要安装，点击安装按钮。
- 然后添加你想要的仓库，快速创建一个工单（例如编写测试）。
- 在工单前加上 "Sweep:" 并让 Sweep 处理其余部分。

### Links
- [GitHub](https://github.com/sweepai)
- [Discord](https://discord.com/invite/sweep-ai)
- [Interview: Sweep founders share learnings from building an AI coding assistant](https://e2b.dev/blog/sweep-founders-share-learnings-from-building-an-ai-coding-assistant)
- [Tricks for prompting Sweep](https://sweep-ai.notion.site/Tricks-for-prompting-Sweep-3124d090f42e42a6a53618eaa88cdbf1)


</details>

## [Taxy AI](https://github.com/TaxyAI/browser-extension)
Taxy AI 是完整的浏览器自动化方案

<details>

![image](https://github.com/TaxyAI/browser-extension/raw/main/src/assets/img/icon-128.png)

### Category
通用、生产力工具

### Description
- Taxy 使用 GPT-4 控制你的浏览器并代表你执行重复性操作。
- 目前它允许你定义临时指令。
- 未来它将支持保存和计划工作流。
- 目前处于早期阶段，有等待名单。



### Links
- [GitHub](https://github.com/TaxyAI/browser-extension)
- [Waitlist](https://docs.google.com/forms/d/e/1FAIpQLScAFKI1fZ1cXhBmSp2HM93Jvuc8Jvrxh5iSbkKhtwKN-OHoTQ/viewform)

</details>

## [Teenage AGI](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#experiments)
受 BabyAGI 启发的 Agent，可回忆无限记忆
<details>

![image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
通用

### Description
一个受 BabyAGI 启发的 Agent，可以回忆无限记忆，“思考”后再行动，并且在关闭后不会丢失记忆。
- 模型：GPT-4。
- 语言：Python。
- 使用 OpenAI 和 Pinecone 为 AI Agent 提供记忆并允许它在采取行动前“思考”（输出文本）。
- 此外，仅仅关闭 AI 也不会忘记它的记忆，因为它存在于 Pinecone 上且其记忆计数器保存了当前索引。
- 每次用户查询 AI 时发生的过程：
	- AI 向量化查询并将其存储在 Pinecone 向量数据库中。
	- AI 在记忆中查找与当前查询相关的记忆和过去的查询。
	- AI 思考要采取的行动。
	- AI 存储第 3 步中的想法。
	- 基于第 3 步的想法和第 2 步的相关记忆，AI 生成输出。
	- AI 将当前查询及其答案存储在其 Pinecone 向量数据库记忆中。

### Links
- Created by [@sean_pixel](https://twitter.com/sean_pixel)
- Inspired by paper ["Generative Agents: Interactive Simulacra of Human Behavior"](https://arxiv.org/abs/2304.03442)

</details>

## [UFO](https://github.com/microsoft/UFO)
Windows 操作系统上的 UI 聚焦 Agent

<details>

![image](https://github.com/microsoft/UFO/raw/main/assets/ufo_blue.png)

### Category
多智能体 (Multi-agent)、GUI Agent

### Description
- Microsoft 出品的 Agent。
- UFO 是一个 UI 聚焦的双 Agent 框架，通过无缝导航和在单个或跨多个应用程序内操作来满足 Windows OS 上的用户需求。

### Links
- [GitHub](https://github.com/microsoft/UFO)
- [Web]()
- [Paper](https://arxiv.org/abs/2402.07939)

</details>

## [Vanna.AI](https://vanna.ai/)
基于你的架构训练的 Python AI SQL Agent

<details>

![image](https://vanna.ai/img/vanna.svg)
### Category
编程、调试、代码迁移、数据分析

### Description
Vanna 是一个开源的 Python AI SQL Agent，根据你的架构训练后能在几秒内编写复杂 SQL。
- AI 驱动的商业智能助手。
- Vanna 通过检索增强生成 (RAG) 使用 LLMs 帮助你为数据库生成和运行准确的 SQL。
- Vanna 分两步工作——在你的数据上训练 RAG “模型”，然后提问，这将返回可设置为在数据库中自动运行的 SQL 查询。
- Vanna Python 包和各种前端集成均为开源。
- Vanna 的能力与你提供的训练数据相关。更多训练数据意味着对大型和复杂数据集的更高准确性。
- 你的数据库内容永远不会发送到 LLM。元数据存储层仅查看架构、文档和查询。
- 随着你使用 Vanna 的次数增多，我们的模型会不断通过增加训练数据来改进。

### Links
- [Web](https://vanna.ai/)
- [GitHub](https://github.com/vanna-ai/vanna)
- [Discord](https://discord.com/invite/qUZYKHremx)
- [LinkedIn](https://www.linkedin.com/company/vanna-ai/)
- [Docs](https://vanna.ai/docs/)

</details>

## [Voyager](https://voyager.minedojo.org/)
Minecraft 中由 LLM 驱动的终身学习 Agent
<details>

![image](https://voyager.minedojo.org/assets/images/exploration_performance.png)

### Category
通用

### Description
- 一个在 Minecraft 中由 LLM 驱动的具身终身学习 Agent，持续探索世界、获取多样化技能并做出新发现，无需人工干预。
- Voyager 由三个关键组件组成：
	- 1）最大化探索的自动课程表。
	- 2）用于存储和检索复杂行为的不断增长的技能库可执行代码。
	- 3）一种新的迭代提示机制，结合环境反馈、执行错误和自我验证以改进程序。
- Voyager 通过黑盒查询与 GPT-4 交互，绕过了对模型参数微调的需求。


### Links
- [GitHub](https://github.com/MineDojo/Voyager)
- [Paper - Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)
- [YouTube video](https://www.youtube.com/watch?v=uTg39rNMojo)
- [Tweet](https://twitter.com/DrJimFan/status/1662115266933972993)

</details>

## [Web3 GPT](https://w3gpt.ai/)
编写并部署智能合约到 EVM 区块链

<details>

![image](https://pbs.twimg.com/profile_images/1701486001120567296/u84M3Ruo_400x400.jpg)

### Category
区块链、编程、生成应用、智能合约

### Description
- 编写并部署智能合约到 EVM 区块链。
- 连接钱包以手动部署合约，甚至可以从你以前的聊天中部署。
- 通过账户抽象和燃气主账户 (gas master account)，使 Web2/3 用户无需专用 web3 钱包即可与区块链交互。
- 利用 Chat-GPT 与 Web3-GPT 功能进行交互和控制。

### Links
- [Web](https://w3gpt.ai/)
- [GitHub](https://github.com/markeljan/web3gpt?tab=readme-ov-file)
- [Founder's X](https://twitter.com/0xmarkeljan)
- [Founder's LinkedIn](https://www.linkedin.com/in/markeljan/)

</details>

## [“Westworld” simulation](https://theolvs.github.io/westworld/)
多 Agent 环境模拟库
<details>

![image](https://theolvs.github.io/westworld/img/cover_hq_westworld1.jpg)

### Category
通用、多智能体 (Multi-agent)

### Description
一个多 Agent 模拟库，目标是模拟和优化具有多个交互 Agent 的系统和环境。
- 斯坦福和 Google 的研究人员创建了一个交互式沙盒环境，其中包含 25 个生成式 AI Agent 可模拟人类行为。
- 他们在公园散步、在咖啡馆喝咖啡并与同事分享新闻。他们展示了令人惊讶的良好社交能力。
- Westworld 的灵感来自 Unity 软件和 Unity ML Agents，用 Python 改编。
- 语言 (Languages)
	- 该库可通过 pip install westworld 在 PyPi 上获取。
	- [Javascript 版本（开发中）](https://github.com/TheoLvs/westworldjs)。
- 特性 (Features)
	- 轻松创建网格和非网格环境。
	- 对象（Agent、障碍物、收集品、触发器）。
	- 子类化不同对象以创建自定义对象。
	- 生成器在环境中随机生成对象。
	- 所有对象的基本刚体系统。
	- 简单的 Agent 行为（寻路、漫游、随机行走、逃跑、视野范围）。
	- 自动迷宫生成。
	- 图层集成将图像转换为障碍物并吸附到网格。
	- 经典模拟的示例模拟和示例 Agent。
	- 模拟可视化、回放和导出（gif 或视频）。

### Links
- [GitHub](https://github.com/TheoLvs/westworld)
- [Documentation](https://theolvs.github.io/westworld/ )
- [Underlying paper - Generative Agents](https://arxiv.org/abs/2304.03442)
- 模拟数十个 Agent 交互的论文。
- 提出了一种架构，将语言模型扩展到存储和综合 Agent 的经验，使其能够在具有生成式 Agent 的交互式沙盒环境中进行动态行为规划。
</details>

## [WorkGPT](https://github.com/team-openpm/workgpt)
用于调用 API 的 GPT Agent 框架

<details>

![image](https://pbs.twimg.com/card_img/1744902310336118784/AVnD3MC-?format=jpg&name=medium)

### Category
编程

### Description
- WorkGPT 是一个类似于 AutoGPT 或 LangChain 的 Agent 框架。你给它一个指令和一个 API 数组，它将与 AI 来回对话直到其指令完成。
- 例如，指令可以是研究网络、抓取网站或为你订购 Uber。我们支持任何可以用 OpenAPI 文件表示的 API。
- WorkGPT 现在内置了 OpenAI 的新函数调用功能。
	- 以前将 API 串联在一起是可能的（参见 AutoGPT），但速度慢、昂贵且容易出错。
	- [宣布此功能的推文](https://twitter.com/maccaw/status/1669367224694607875)。

### Links
- Author: [Alex MacCaw](https://twitter.com/maccaw)

</details>

## [Wren](https://www.getwren.ai/)
数据库的自然语言接口

<details>

![image](https://cdn.prod.website-files.com/65e9b9dd95692faa9f5bb1c0/65f99924ac1b1f225c356d74_logo.png)

### Category
编程、数据分析、生产力工具

### Description
"WrenAI 是一个 AI 驱动的数据助手，旨在帮助你快速轻松地检索结果和洞察，无需编写 SQL。它也是开源的，这意味着你可以定制并使用它以满足你的特定需求。

我们在开发 WrenAI 时遵循了四个关键原则：

1. 可解释性：我们确保 WrenAI 生成的每个 SQL 查询都准确、简洁且可靠，让你信任它提供的结果。

2. 互操作性：WrenAI 允许你从多个来源查询数据，无论不同的数据格式和方言如何。你可以在各种来源上享受标准接口，节省时间和精力。

3. 交互体验：我们的 AI 助手以对话方式与用户互动，帮助澄清他们的查询并实时优化结果。你可以自然直观地与 WrenAI 交互。

4. 持续学习：WrenAI 从与用户的交互、反馈和查询历史中不断学习。它将新模式、信息和数据结构纳入其 LLM 知识库，确保它随着时间的推移变得更好更准确。”

### Links
- [Web](https://www.getwren.ai/)
- [GitHub](https://github.com/Canner/WrenAI)
- [X (Twitter)](https://x.com/getwrenai)
- [Docs](https://docs.getwren.ai/overview/introduction)
- [Blog](https://blog.getwren.ai/)

</details>

## [XAgent](https://github.com/OpenBMB/XAgent)
实验性 LLM Agent，可解决各种任务

<details>

![image](https://pbs.twimg.com/profile_banners/1713881934991093760/1697456782/1500x500)

### Category
通用、编程

### Description
XAgent 是一个开源实验性大语言模型 (LLM) 驱动的自主 Agent，可自动解决各种任务。
- **涌现与自主**：XAgent 的自主操作超越偏见。
- **安全与运行**：在 Docker 环境中安全执行。
- **免专家知识**：无需依赖单一专家即可有效运行。
- **界面与交互**：通过用户友好的 GUI 或命令行进行交互，同时适应和协作。
- **双循环机制 (Dual-loop Mechanism)**：
  - **外环 (Outer-Loop)**：管理计划和任务优化。
  - **内环 (Inner-Loop)**：分发、基于 ReACT 的执行、反馈。
- **通用语言 - 函数调用 (Universal Language - Function Calling)**：
  - **ToolAgent & ReACT**：为子任务选择最佳动作序列。
- **工具 (Tools)**：
  - 📝 文件编辑器。
  - 📘 Python Notebook。
  - 🌏 Web 浏览器。
  - 🖥️ Shell。
  - 🧩 Rapid API。

### Links
- [Twitter](https://twitter.com/XAgentTeam)
- [GitHub Repository](https://github.com/OpenBMB/XAgent)
- [Discord](https://discord.gg/zncs5aQkWZ)
- [Youtube Demo](https://www.youtube.com/watch?v=QGkpd-tsFPA)

</details>

## [yAgents](https://github.com/yeagerai/yeagerai-agent)
能够设计、编码和调试工具的 Agent

<details>

![image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
编程、自定义构建

### Description
yAgents 是由 Yeager.ai 制作的 Agent-Builder Agent，能够设计、编码和调试其自身的工具。
- 旨在帮助轻松高效地构建、原型制作和部署 AI 驱动的工具和 Agent。
- 基于 LangChain 框架构建，允许任何技术背景的用户创建、改进和部署 AI Agent。
- 配备交互式命令行界面以提供实时反馈和易于导航。
- 具备会话持久记忆以确保跨多个会话的数据保留。
- 通过 pip 快速轻松安装。
- 鼓励贡献以扩展和改进 yAgents。
- 警告 (Warnings)
	- 需要 GPT-4 API 访问权限。
	- 未在 Windows 系统上测试。

### Links
- [GitHub Repository](https://github.com/yeagerai/yeagerai-agent/?utm_source=awesome-ai-agents)
- [Discord](https://discord.com/invite/wKds24jdAX/?utm_source=awesome-ai-agents)
- [License: MIT](https://github.com/yeagerai/yeagerai-agent/blob/main/LICENSE/?utm_source=awesome-ai-agents)

</details>

## [Yourgoal](https://github.com/pj4533/yourgoal/?utm_source=awesome-ai-agents)
Swift 实现的 BabyAGI

<details>

![image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
通用

### Description
- “这是 BabyAGI 的 Swift 移植版，一个 AI 驱动的任务管理系统示例，使用 OpenAI 和 Pinecone API 创建、优先排序和执行任务。该系统背后的主要思想是它根据前序任务结果和预定义目标创建任务。”

### Links
- Author: [PJ Gray](https://twitter.com/pj4533/?utm_source=awesome-ai-agents)
</details>

# 闭源项目及公司

## [Ability AI](https://ability.ai/)
安全、以人为本的自主 AI Agent

<details>

![image](https://ability.ai/assets/images/image01.svg?v=e0c18927)

### Category
通用、生产力工具、商业智能

### Description
- 赋能企业使用安全、以人为本的自主 AI Agent。
- 仍处于早期版本。

### Links
- [Web](https://ability.ai/)

</details>

## [Adept AI](https://www.adept.ai/?utm_source=awesome-ai-agents)
构建智能的机器学习研究与产品实验室

<details>

![image](https://media.licdn.com/dms/image/C4E0BAQHoZ-QBmwsa0g/company-logo_200_200/0/1677107534930/adeptailabs_logo?e=1713398400&v=beta&t=ykMLRWaek147bz9BpCaLCuYFrVorWWT3iaDsrWQa6Do)

### Category
通用

### Description
- 一个通过让人类与计算机创造性地协同工作来构建通用智能的机器学习研究与产品实验室。
- 每个人的 AI 队友。
- “Adept 正在构建一种全新的完成任务的方式。它接受你用自然语言描述的目标，并将其转化为你每天使用的软件上的操作。”
- 处于早期阶段。
- “我们正在构建一个可以与你的计算机上所有内容交互的机器学习模型。”


### Links
- [Twitter](https://www.adept.ai/?utm_source=awesome-ai-agents)
- [Linkedin](https://www.linkedin.com/company/adeptai/?utm_source=awesome-ai-agents)

</details>

## [AGENTS.inc](https://www.agents.inc/)
面向公司/法规、搜索与监控的 Agent

<details>

![image](https://www.agents.inc/wp-content/uploads/2023/08/AGENTS.inc-logo.png)

### Category
数据分析、科学、监控、通用、商业智能、支持开源模型

### Description
- 面向特定任务的 AI Agent：
  - 全球新闻雷达 AI Agent。
  - 公司识别 AI Agent。
  - EU 政策观察 AI Agent。
  - 报告 AI Agent。
  - 科学知识 Agent。
  - 专利分析 Agent。


### Links
- [Web](https://www.agents.inc/)
- [X (Twitter)](https://x.com/agentsdotinc)
- [LinkedIn](https://www.linkedin.com/company/agentsdotinc/)
- [YouTube](https://www.youtube.com/c/agentsdotinc)
- [Facebook](https://www.facebook.com/agentsdotinc)
- [GitHub](https://github.com/agentsinc)

</details>

## [AgentScale](https://agentscale.ai/)
你的助手、邮件撰写者、日历调度员

<details>

![image](https://assets-global.website-files.com/64e879914c784ca827df6d6d/6594ec15997b8276945f35a6_logo_side_white_cropped-p-500.png)

### Category
通用、生产力工具

### Description
AgentScale 是你自己的个人助手、邮件撰写者、日历调度员和互联网冲浪者。
- AgentScale 是你自己的 AI 个人助理。


### Links
- [Web](https://agentscale.ai/)
- [X ](https://twitter.com/agentscale)
- [LInkedin](https://www.linkedin.com/company/agentscale-ai/about/)
- Founder's web: [Jet New](https://jetnew.io/)

</details>


## [Aide by Codestory](https://codestory.ai/)
AI 代码解释器，VSCode 的 AI 驱动修改版

<details>

![image](https://avatars.githubusercontent.com/u/135339264?s=200&v=4)

### Category
编程

### Description
- 仍处于早期阶段，新功能即将推出。
- 现已支持 JS/TS。
- 可分析代码库、识别根本原因、进行修复并自动生成测试以评估 Bug 是否已解决。


### Links
- [Web](https://codestory.ai/)
- [Docs](https://docs.codestory.ai/)
- [Discord](https://discord.com/invite/DNnh6tC9VA)
- [X ](https://twitter.com/codestoryai)
- [Linkedin](https://www.linkedin.com/company/codestory-ai/)

</details>

## [AilaFlow](https://ailaflow.com)
构建 AI Agent 的无代码平台

<details>

![image](https://yt3.googleusercontent.com/TkDmYBaXRvIegqkJoujtXpIlK9X5dMAjiDldAlqSHAUaekbvbYXlOaZq1DsV8neqBUZqlWAc5w=s900-c-k-c0x00ffffff-no-rj)

### Category
自定义构建、生产力工具

### Description
- AilaFlow 是用于构建 AI Agent 的无代码平台。
- 使用模板，通过无代码编辑器根据你的需求进行调整。
- 分类：生产力工具、Agent 构建框架。

### Links
- [AilaFlow - AI Agents No-code Platform](https://ailaflow.com)
- Founder's X account: [b4rtaz](https://twitter.com/b4rtaz)

</details>


## [Airkit.ai](https://www.airkit.ai)
构建、测试和部署 Agent 的平台

<details>

![image](https://airkit.ai/_gatsby/image/4d7db4337bbde82f2bf7ffb0e5046c81/a46b36f8203bc3f33cb41b43956d7bd2/IMG_1847.avif?u=https%3A%2F%2Flive-airkit-ai.pantheonsite.io%2Fapp%2Fuploads%2F2023%2F11%2FIMG_1847.png&a=w%3D480%26h%3D174%26fm%3Davif%26q%3D100&cd=c7e6c2e0828656c0553ba410f22d3684)

### Category
自定义构建

### Description

- 一个基于浏览器的工作室，用于管理提示词、构建工具和测试你的 Agent。
- 内置短期和长期记忆管理。
- 一键部署。通过我们的 Web SDK 嵌入到任何地方。 

### Links
- [Profile of the company](https://www.airkit.ai)
- [Twitter](https://twitter.com/AirkitAI)

</details>

## [Airplane Autopilot](https://www.airplane.dev/autopilot/?utm_source=awesome-ai-agents/)
Airplane 公司的自动驾驶 AI 助手

<details>

![image](https://www.airplane.dev/autopilot/hero/autopilot-logo.png)

### Category
编程、通用

### Description

- 一种面向开发者的构建内部 UI 和工作流的方法。
- 将 API、SQL 查询和脚本转化为整个团队的 App。
- 特性 (Features)
	- Airplane 让你能够将 SQL 查询、JavaScript/Python 代码、HTTP 请求等转化为任务。
	- 允许通过无代码仪表板运行任务。
	- 用于客户支持、值班手册和定时任务的任务。

### Links
- [Profile of the company](https://www.airplane.dev/?utm_source=awesome-ai-agents)
- [Documentation](https://docs.airplane.dev/?utm_source=awesome-ai-agents)
- [Twitter](https://twitter.com/AirplaneDev/?utm_source=awesome-ai-agents)
- [They're building an AI assistant here](https://www.airplane.dev/autopilot/?utm_source=awesome-ai-agents)

</details>


## [Aomni](https://www.aomni.com/?utm_source=awesome-ai-agents)
专为商业智能设计的 AI Agent

<details>

![image](https://www.aomni.com/icons/aomni-logo-black.svg)

### Category
商业智能

### Description
- 将高层研究问题分解为逐步计划并执行。
- 多样化的工具，包括完整的 Web 浏览器。
- 可访问互联网信息而无需 API。
- “我们不使用 AI 生成内容，因为它可能不可靠。相反，我们从可信来源提取相关信息，聚类并将其处理成用户友好的格式。”
- AI 驱动的查询规划器智能路由和执行请求，确保正确性和多样化的源选择。

### Links
- [Discord](https://discord.com/invite/a367ncqEsm/?utm_source=awesome-ai-agents)
- [Interview: David Zhang from Aomni gives his view agents' reliability, debugging and orchestration](https://e2b.dev/blog/david-zhang-from-aomni-gives-his-view-on-ai-agents)

</details>

## [APIDNA](https://apidna.ai/)
用于 API 集成的多 AI Agent。


<details>

![image](https://apidna.ai/wp-content/uploads/2023/12/api-dna-logo.svg)

### Category
生产力工具、多智能体 (Multi-agent)、编程

### Description
- “在 APIDNA，我们将软件公司连接起来以连接世界。我们通过专有的无代码多自主 AI Agent 平台来实现这一目标，解决当今软件开发的主要痛点之一——API 端点的集成。”
- “我们的多个自主 AI Agent 即时集成 API 端点。这简化并加速了软件集成过程，通常只需三个步骤并在几分钟内完成。传统上可能需要数小时、数天、数周甚至数月的任务。”

### Links
- [Web](https://apidna.ai/)
- [LinkedIn](https://www.linkedin.com/company/apidna/)
- [Tim D. - LinkedIn](https://www.linkedin.com/in/timdutta-ai/)

</details>

## [Artisian AI](https://github.com/Artisan-AI)
面向销售、电子邮件、记账等的 Agent

<details>

![image](https://pbs.twimg.com/profile_images/1723059970609225728/WxC0wUQ-_400x400.png)

### Category
多智能体 (Multi-agent)、自定义构建

### Description
- YC 公司。
- “创建第一种类人数字员工，称为 Artisans。”
- Artisans 是经过训练以担任特定角色的先进类人数字员工，与人类团队集成。
- 他们拥有独特的面孔、姓名、记忆和技能，一旦雇佣就会持续改进，适应每家公司的需求。
- 第一个 Artisan Ava 自动化整个外展销售流程，可通过 10 分钟的对话进行设置。Ava 创建 TCPs，使用其超过 270,000,000 个联系人的数据库进行潜在客户开发，制作并发送高度定制化的电子邮件序列，并将会议预约到你的日历中。你可以通过 Slack 与 Ava 交谈来管理所有功能和设置。


### Links
- [GitHub](https://github.com/Artisan-AI)
- [X ](https://twitter.com/GetArtisanAI)
- [LinkedIn](https://www.linkedin.com/company/artisanai/)
- [Founder's X](https://twitter.com/jasparcjack)
- [Founder's LinkedIn](https://www.linkedin.com/in/rupertdodkins/)
- [Article](https://tech.eu/2023/11/17/ai-startup-artisan-raises-23m-to-develop-human-like-digital-workers/)
  
</details>

## [Ask Pandi](https://askpandi.com/ask)
搜索和生成知识的回答引擎

<details>

![image](https://askpandi.com/logo.png)

### Category
生产力工具、研究、通用

### Description
- Pandi 将你的搜索的最后阶段编译为简洁、无干扰的网页。
- 它提供来自顶级网络创作者的多模态答案和引用，无需链接筛选、Cookie 同意或广告。
- 你可以使用互联网作为数据源，创建自己的库，或两者兼用。
- 你还可以在创意模式下使用 Pandi 进行写作或编码。


### Links
- [Web](https://askpandi.com/ask)
- [X (Twitter)](https://twitter.com/ask_pandi)


</details>


## [AskToSell](https://asktosell.com/)
遇见能促成交易的自主 AI 销售 Agent

<details>

![image](https://assets-global.website-files.com/64dc76096a7dfdd761e62e16/64dc9b12f89067d1657f3103_asktosell%20transparent%20logo.svg)

### Category
销售、自定义构建、商业智能、营销

### Description
- 一个部署和管理自主 AI 销售 Agent 以促成小额交易的 Web 平台。
- 自主 Agent 将联系你的潜在客户、进行资格筛选、准备报价、处理异议、谈判并以超人类性能完成交易。
- AskToSell 自动推动你的潜在客户通过管道。AI 销售 Agent 将了解你的产品，联系你的潜在客户，进行资格筛选，准备提案，处理异议，谈判并促成交易。 

### Links
- [Web](https://asktosell.com/)
- [LinkedIn](https://www.linkedin.com/company/asktosell/)
- [Founder's LinkedIn - Laimonas Noreika](https://www.linkedin.com/in/laimonasn/)

</details>

## [AskYourDatabase](https://www.askyourdatabase.com/)
与 SQL 数据库聊天，探索并可视化数据

<details>

![image](https://www.askyourdatabase.com/_next/image?url=%2Flogo-light.png&w=64&q=75)

### Category
商业智能、生产力工具、数据分析

### Description
- “SQL 的 ChatGPT”。
- 无需 SQL，连接你的数据库并通过 ChatGPT 与数据进行聊天。

### Links
- [Web](https://www.askyourdatabase.com/)
- [Discord](https://discord.com/invite/AZ2WnRxTD8)
- [Founder's LinkedIn](https://www.linkedin.com/in/sheldon-niu-a174bb243/)

</details>

## [Athena Intelligence](https://www.athenaintelligence.ai/)
24/7 企业 AI 数据分析师

<details>

![image](https://assets-global.website-files.com/6484b03566311009ccef7599/6602dcd93264ffed31406081_athena_logo_full%201.svg)

### Category
数据分析、商业智能

### Description
-  Athena 是一个 AI 原生分析平台，旨在加速企业团队的 Analytical 工作流。
- 它提供协同和自动驾驶模式，学习用户的工作流以允许自信地自主执行。
- Athena 支持查询数据、生成可视化效果、分析企业数据和固化工作流，使其成为数据驱动决策的强大工具。

### Links
- [Web](https://www.athenaintelligence.ai/)
- [Founder's LinkedIn](https://www.linkedin.com/in/brendongeils/)

</details>

## [Avanzai](https://avanz.ai/)
面向投资组合风险和资产分配的 AI Agent

<details>

![image](https://framerusercontent.com/images/abZ2DpGylwpNlOcvhmiTEHLvU.png?scale-down-to=512)

### Category
编程、数据分析、研究、自定义构建（Agent 构建框架与平台）、金融、多智能体 (Multi-agent)

### Description
-  Avanzai 帮助用户构建自主 AI Agent，这些 Agent 抓取新闻、获取实时数据并编写 Python 代码以帮助他们计算投资组合的风险敞口。
-  用户然后可以部署这些 Agent 全天候工作，节省用户自己执行此任务的时间。

### Links
- [Web](https://avanz.ai/)
- [Founder's X (Twitter)](https://x.com/gmanmalena_)
- [LinkedIn](https://www.linkedin.com/company/avanzai/)

</details>

## [Bardeen](https://www.bardeen.ai/)
自动化重复任务的 AI Agent

<details>

![image](https://media.licdn.com/dms/image/v2/D560BAQEzSXhSE2SQDg/company-logo_200_200/company-logo_200_200/0/1716353067827/bardeen_logo?e=1735776000&v=beta&t=ME3uHoIaMtWAPGQAyBiVFjA4U799mmBj5pjCTjrj5eM)

### Category
生产力工具、销售

### Description
- 自动化重复任务的 AI Agent。

### Links
- [Web](https://www.bardeen.ai/)
- [X (Twitter)](https://x.com/bardeenai)

</details>

## [Beam](https://beam.ai/)
广泛选择的 AI Agent，用于自动化工作流

<details>

![image](https://framerusercontent.com/images/frmJOXg5roLaxUZMpGF6efXw9A.png?scale-down-to=512)

### Category
数据分析、生产力工具、自定义构建（Agent 构建框架与平台）、商业智能、多智能体 (Multi-agent)

### Description
- 端到端流程和工作流自动化，配备智能 AI Agent。
- 在医疗保健、保险、物流、客户服务等众多行业的众多 B2B2C 用例中——Beam 允许企业定制自己的自动化或选择现有的 Agent 模板以最小化执行复杂任务、重复任务和 100% 后台任务所需的时间。

### Links
- [Web](https://beam.ai/)
- [X (Twitter)](https://x.com/join__beam)
- [LinkedIn](https://www.linkedin.com/company/beam-ai/)
- [YouTube](https://www.youtube.com/@beam-ai)

</details>

## [Blackbox AI](https://www.blackbox.ai/)
构建软件的软件

<details>

![image](https://www.blackbox.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FBlackbox-Logo-4x.85cc4976.png&w=384&q=75)

### Category
- 通用、编程、数据分析

### Description
- BLACKBOX.AI 是一个旨在改变我们构建软件方式的编码 LLM。

通过构建 BLACKBOX.AI，我们的目标是：

1. 通过在构建和发布产品方面使工程师快 10 倍来加速公司的创新步伐。

2. 加速全球软件工程师的增长并将工程师数量从约 1 亿增加到 10 亿。


### Links
- [Web](https://www.blackbox.ai/)
- [Blackbox AI Code Interpreter](https://www.runcode.ai/)
- [Blackbox AI Code Interpreter in terminal](https://pypi.org/project/blackboxai/)
- [X (Twitter)](https://x.com/aiblckbx?lang=cs)
- [Facebook](https://www.facebook.com/blckbxai/)
- [Chrome extension](https://chromewebstore.google.com/detail/mcgbeeipkmelnpldkobichboakdfaeon)

Written about Blackbox:
- [BLACKBOX AI vs Codium AI](https://medium.com/@blackbox.ai/blackbox-ai-vs-codium-ai-7016abb93ec0)
- [Blackbox AI: Supercharging Your Coding Workflow](https://www.linkedin.com/pulse/blackbox-ai-supercharging-your-coding-workflow-swarup-mukharjee-5gqbe/)
- [Unveiling the Untold Story of Blackbox.ai: A Revolution in Software Quality Assurance](https://www.linkedin.com/pulse/unveiling-untold-story-blackboxai-revolution-software-yaqoot-kashif-em75f/)

</details>


## [Blobr](https://www.blobr.io/)
连接你所有工具的 AI 商业助手

<details>

![image](https://assets-global.website-files.com/5f1ace21b47b368069989680/65cdd7ab62643c6baa204181_logo-blobr-white.svg)

### Category
数据分析、生产力工具、营销、销售、商业智能

### Description
- Blobr 是一个 AI 助手，使你存储在孤立 SaaS 中的所有业务数据变得有意义。揭示洞察，理解变化和客户模式，无需技术努力。
- Blobr 帮助销售运营、营销运营和增长人员做出更好的决策。
- Blobr 添加了一个连接到你所有 SaaS（Hubspot、Google Analytics、Stripe 等）的智能层。


### Links
- [Web](https://www.blobr.io/)
- [X (Twitter)](https://twitter.com/Blobr_io)
- [Founder's LinkedIn](https://www.linkedin.com/in/alexandre-airvault-aabaa758/)

</details>

## [BrainSoup](https://www.nurgo-software.com/products/brainsoup)
在本地 PC 上构建为你工作的 AI 团队

<details>

![image](https://www.nurgo-software.com/images/BrainSoup/BrainSoupCard512.png)

### Category
通用、生产力工具、数据分析、多智能体 (Multi-agent)、自定义构建

### Description
- 记住、学习并协同工作的定制 AI Agent。
- 本地原生应用，注重隐私和响应速度。
- 你的数据滋养你的 AI Agent 而不会离开你的 PC。
- 多模态：你的 AI Agent 理解文本、语音和图像。
- 反应式：你的 Agent 可以响应用户定义的事件并利用实时数据。
- 自主运行：你的 Agent 可以在无需用户干预的情况下在后台运行。
- 安全协作：AI 可在沙箱环境中读取、写入、执行和共享文件。
- 多 LLM：本地和基于云的 AI 模型可结合使用以获取最佳效果。
- 可玩性和可扩展性：用自定义工具和脚本赋能你的 Agent。

### Links
- [Web](https://www.nurgo-software.com/products/brainsoup)
- [Docs](https://help.nurgo-software.com/collection/148-brainsoup)
- [X](https://twitter.com/Nurgo)
- [Discord](https://discord.gg/xt7PyCnH9S)

</details>

## [broadn](https://www.broadn.io/?utm_source=awesome-ai-agents)
允许用户构建 AI 应用的无代码副驾驶

<details>

![image](https://api.typedream.com/v0/document/public/9727d7a5-4819-4564-beac-0284be31fddc/2aOWIGcm82x5hyT6p1gN9X7cn62_broadn_logo_new.png)

### Category
编程

### Description
- broadn 是一个无代码平台，帮助非技术人员在几分钟内构建 AI 产品。通过 LLM 驱动的对话界面和自动化复杂后端/工作流操作的 Agent 架构，我们比传统无代码工具更快且更灵活。
- 特性 (Features)
	- 对话式界面。
	- LLM/AI 模型连接器（文本、图像模型等）。
	- 创建定制聊天机器人。
	- 渲染 UI 组件。
	- 通过 API 连接外部数据。

### Links
- Authors: [Calin Drimbau](https://twitter.com/calindrimbau) and [Victor Paraschiv](https://twitter.com/vicpara)。
- [Twitter](https://twitter.com/getbroadn)

</details>


## [Butternut AI](https://butternut.ai/)
构建功能完备、准备上线的网站

<details>

![image](https://butternut.ai/_next/image?url=%2Fimages%2Flogo%2Flogo-text.png&w=384&q=75)

### Category
网页设计、设计、编程、营销

### Description
一个在 20 秒内创建功能完备、准备上线的网站工具。
- 用户友好的界面无需编码。
- 完整的 SEO 优化。
- 图片上传：用户可以方便地上传并重新生成自己的图片以无限定制他们的个人资料。
- 资料自定义：用户可以隐藏部分、添加社交媒体链接和共享联系信息，展示他们独特的个性和品牌。
- 即时预览：用户可通过方便放置的预览按钮即时查看其个人资料更改，确保快速评估所需外观。
- 速度快 30%：该应用实现了令人印象深刻的网站生成速度提高 30%，为用户提供快速高效的网站建设体验。

### Links
- [Web](https://butternut.ai/)


</details>

## [B2 AI](https://www.b2.work/)
工作的自动补全 AI 助手

<details>

![image](https://static.vecteezy.com/system/resources/previews/024/246/469/non_2x/advanced-ai-assistant-icon-in-illustration-vector.jpg)

### Category
个人助手、商业智能、生产力工具、数据分析

### Description
- B2 是一个自主 AI 助手，帮助你完成任务。
- 与团队成员分享有用的工作流或安排 AI 驱动的定期工作流。
- 细粒度数据控制以确保公司的数据不会落入错误的人手中。完全可配置的角色访问权限。

### Links
- [Web](https://www.b2.work/)
- [Founder's X - Ethan](https://twitter.com/amazng_wanderer)


</details>

## [ChatHelp](https://chathelp.ai/)
AI 驱动的商业、工作与学习助手

<details>

![image](https://chathelp.ai/wp-content/uploads/chathelp_black.png)

### Category
数据分析、内容创作、生产力工具、研究、营销、销售、商业智能

### Description
- 👉 与私有 AI 知识库聊天——通过拥有你业务和竞争对手、工作或学习所有知识的 AI 助手提高日常工作效率。
- 👉 节省客户支持的时间和金钱。让 AI 24/7 通过网站小部件与潜在客户互动，驱动更多销售！使用你的网站数据和其他文档训练 AI！
- 👉 100+ 独特 AI 工具，满足你所有商业、工作和学习需求。例如 AI 写作助手和 WordPress 自动发帖机。
- 🔜 通过 AI 驱动的反馈、投票和调查小部件更好地了解你的客户！ 

✔️ 支持的文件格式：pdf, doc, docx, ppt, pptx, xls, xlsx, csv, json, epub, mp3, jpg, jpeg, png。
✔️ WordPress 插件。
✔️ YouTube 字幕。
✔️ Yelp 评论分析。
✔️ +175 种语言支持。
✔️ 创建 AI 驱动的网站聊天小部件。
✔️ 创建自定义 AI 驱动的知识库。
🔜 Zapier, Notion, ZenDesk, Hubspot, Trello, Monday.com, Slack, Gmail & Google Doc. 支持。”


### Links
- [Web](https://chathelp.ai/)
- [X (Twitter)](https://twitter.com/ChatHelpAI)
- [LinkedIn](https://www.linkedin.com/company/chathelp/about/)
- [Discord](https://discord.com/invite/BK5QtfKxbB)
- [Facebook](https://www.facebook.com/ChatHelpAI)
- [GitHub](https://github.com/chathelpai)

</details>

## [Claros AI Shopper](https://www.claros.so/)
根据你的品味寻找产品的 AI 购物助手
<details>

![image](https://www.claros.so/logo-circle.png)

### Category
个人助手

### Description
Claros 是一个 AI 个人购物助手，为你发现有趣的产品，并随时间学习你的品味。
- 面向电商 + 所有人的 AI 购物助理。
- Claros 是一个 AI 个人购物助手，为你发现酷且有趣的产品。它还可以随时间学习你的品味以提供最佳结果。


### Links
- [Web](https://www.claros.so/)
- [X](https://twitter.com/so_claros)
- [LinkedIn](https://www.linkedin.com/company/clarosai/)
- [Founder's X - Anish](https://twitter.com/thiteanish)
- - [Founder's X - Ammar Safdari](https://twitter.com/asapdar)

</details>

## [Claygent](https://www.clay.com/learn/claygent)
从网络抓取和总结数据的 Agent

<details>

![image](https://assets-global.website-files.com/61477f2c24a826836f969afe/65b22bf376c1cc60a9e0de93_img-logo-clay.png)

### Category
生产力工具、营销、销售、金融、通用、商业智能

### Description
- Claygent 是一个 AI Web 爬虫，可以搜索和浏览网络以寻找信息，取代你的 SDR 在账户研究上所做的海量手动工作！

### Links
- [Web](https://www.clay.com/learn/claygent)
- [Founder's LinkedIn](https://www.linkedin.com/in/adam-eldefrawy-8623a815a/)

</details>

## [Code Autopilot](https://www.codeautopilot.com/)
你项目的 AI 助手

<details>

![image](https://www.codeautopilot.com/_next/static/media/logo_purple.fa331d81.png)

### Category
编程、多智能体 (Multi-agent)、GitHub

### Description
- GitHub Issue 和 Pull Request 的 AI 助手。在文本描述的指引下，为复杂的 GitHub 项目创建完整功能并修复 Bug。

### Links
- [Web](https://www.codeautopilot.com/)
- [Docs](https://docs.codeautopilot.com/)
- [X](https://twitter.com/code_autopilot)
- [Gustavo Silva - co-founder of Code Autopilot](https://twitter.com/Gsandec)
- [Fábio Zé Domingues - co-founder of Code Autopilot](https://twitter.com/fjrdomingues)
  
</details>


## [Codegen](https://www.codegen.com/)
解决工单、编写测试，提升你的工作流

<details>

![image](https://assets-global.website-files.com/652ef464dd4ef344367c4fd1/652efb93dcbbba956ee773f2_Codegen%20-%20Logo%20-%20Primary%20-%20Dark%20Theme-p-500.png)

### Category
编程

### Description
Codegen 是一个 Agent，允许自动解决工单、编写测试并利用 GPT-4 的力量提升用户的开发工作流。
- 用例：编码、调试、代码迁移等。
- 使用的模型：GPT-4。



### Links
- [Web](https://www.codegen.com/)
- [X ](https://twitter.com/Codegen)
- [Founder's X](https://twitter.com/mathemagic1an)
</details>

## [CodeWP](https://codewp.ai/)
面向 WordPress 网站的 AI Agent
<details>

![image](https://codewp.ai/wp-content/uploads/2023/09/New-Icon.png)

### Category
编程

### Description
通过领域特定的 AI 模式、工具和功能加速 WordPress 开发。

### Links
- [Web](https://codewp.ai/)
- [GitHub](https://github.com/wpai-inc/)
- [X](https://twitter.com/codewp_ai)
- [LinkedIn](https://www.linkedin.com/company/wpai-inc/)
- [James LePage - founder of CodeWP](https://twitter.com/codewp_ai)
  
</details>

## [Codium AI](https://www.codium.ai/)
面向开发者的多功能编码 AI 助手

<details>

![image](https://www.codium.ai/wp-content/uploads/2023/01/codium-logo.svg)

### Category
编程

### Description
- 为忙碌的开发者生成有意义的测试。
- 探索和分析你的代码、文档字符串、注释，并通过与你互动。
- IDE 内直接建议非平凡（以及平凡）的测试：
	- 生成测试用例。
	- 覆盖边缘情况。
	- 最佳实践和可读性代码建议。
	- 提供代码解释。
- 它是免费的。


### Links
- [Twitter](https://twitter.com/CodiumAI)
- [LinkedIn](https://www.linkedin.com/company/codiumai)。
- [YouTube](https://www.youtube.com/@Codium-AI)。
- [Discord](https://discord.com/invite/SgSxuQ65GF)。
- [GitHub](https://github.com/Codium-ai)。


</details>

## [Commit](https://commit.dev)
软件开发者的职业副驾驶和 AI Agent

<details>

![image](https://commit.dev/wp-content/uploads/2021/05/commit-logo.svg)

### Category
编程

### Description
- 全面的求职搜索。
- 基于你的技能、经验和偏好的准确工作推荐。
- AI 驱动的自动申请。

### Links
- CEO: [Greg Gunn](https://www.linkedin.com/in/gunnr)。
- CTO: [Beier Cai](https://www.linkedin.com/in/beiercai)。

</details>


## [Cognosys](https://cognosys.ai)
AutoGPT 或 BabyAGI 的 Web 版本

<details>

![image](https://pbs.twimg.com/profile_banners/1646414136811855873/1704327520/1500x500)

### Category
通用、研究

### Description
- 构建 AI Agent 的友好 UI。

### Links
- Author: [Sully Omarr](https://twitter.com/SullyOmarr)。
- [Interview: About deployment, evaluation, and testing of agents with Sully Omar, the CEO of Cognosys AI](https://e2b.dev/blog/about-deployment-evaluation-and-testing-of-agents-with-sully-omar-the-ceo-of-cognosys-ai)。

</details>

## [ContextQA](https://contextqa.com/)
用于软件测试的 AI Agent

<details>

![image](https://contextqa.com/wp-content/themes/contextQA/assets/images/cqa-logo-with-text.svg)

### Category
编程

### Description
- 面向完整测试覆盖率的 Agentic AI。

### Links
- [Web](https://contextqa.com/)
- [X (Twitter)](https://x.com/ContextQa)。

</details>



## [Cursor](https://www.cursor.so/)
AI 驱动的代码编辑器，拥有类 VSCode UI

<details>

![image](https://cursor.sh/brand/logo.svg)

### Category
编程

### Description
Cursor 是 AI 优先的代码编辑器。在专为与 AI 结对编程而设计的编辑器中更快地构建软件。

### Links
- [Website](https://www.cursor.so/)
- [GitHub (Issue Only)](https://github.com/getcursor/cursor)。
- [Discord](https://discord.com/invite/PJEgRywgRy)。

</details>

## [Cykel](https://www.cykel.ai/)
与任何 UI、网站或 API 交互

<details>

![image](https://pbs.twimg.com/profile_images/1704063452271058944/sZEVZIqG_400x400.png)

### Category
通用、生产力工具


### Description
Cykel 是一个 AI 副驾驶模型，可以根据自然语言命令与任何 UI、网站或 API 交互。
- 用例：通用、个人助手（帮助日常任务）。


### Links
- [Web](https://www.cykel.ai/)
- [X ](https://twitter.com/CykelAI)。
- [LinkedIn](https://www.linkedin.com/company/cykelai)。
- [Founder's X](https://twitter.com/EwanCollinge)。
  
</details>

## [Devin](https://www.cognition-labs.com/introducing-devin)
第一位 AI 软件工程师

<details>

![image](https://assets-global.website-files.com/65cf071d26e52092bc212f6e/65ed4622397bb038560f1ef3_cropped-p-500.png)

### Category
通用、编程


### Description
Devin 目前处于早期阶段，但根据演示，它具有以下能力：
- 可学习如何使用不熟悉的技术。
- 可端到端构建和部署应用。
- 可自主在代码库中查找并修复 Bug。


### Links
- [Blog post](https://www.cognition-labs.com/introducing-devin)。
- [X (Twitter)](https://twitter.com/cognition_labs)。
  
</details>


## [Diagram](https://diagram.com/)
面向所有人的 AI 设计工具，已被 Figma 收购

<details>

![image](https://uploads-ssl.webflow.com/6408bea3de5aef58b7e197d4/6408c50680c7dae0a89901a1_logo.svg)

### Category
设计、内容创作

### Description
- AI 驱动的设计工具，涵盖从文案撰写到根据文本生成唯一图标的各种功能。
- Magic Copy 编写、编辑和重写 Figma 文本层，让你使用真实文案进行设计。
- 在设计时生成图像。
- Magic Rename 智能命名你的图层，让你将更多时间花在真正的设计上。
- Magician 直接在你最喜欢的工具（如 Figma）中工作。
- 可在一个方便的插件中获得所有最新的 AI 设计进展 + 未来的魔法功能。

### Links
- [Web](https://diagram.com/)

</details>

## [Docket AI](https://docketai.net/)
复杂 B2B 销售的 AI 销售工程师

<details>

![image](https://cdn.prod.website-files.com/64b81d5300b4d493cead41a3/66a0a76ea06f179159040503_Docket%20Logo%201.svg)

### Category
销售

### Description
- Docket AI 是你个人的 AI 销售工程师，赋能 AEs 赢得更多订单。
- 它提供即时销售答案、自动 RFP 响应以及来自顶级生产者的洞察。
- 由 Sales Knowledge Lake™ 驱动，Docket 将公司的销售数据与生成式 AI 统一起来。转变销售生产力和胜率。

### Links
- [Web](https://docketai.net/)

</details>

## [Dosu](https://dosu.dev/)
GitHub 仓库的 AI 队友，同时帮助文档编写
<details>

![image](https://avatars.githubusercontent.com/u/146474245?s=200&v=4)

### Category
编程、生产力工具


### Description
- Dosu 是一个生活在你的 GitHub 仓库中的 AI 队友，帮助你回复 Issue、分类 Bug 并构建更好的文档。
- Dosu 在几分钟内用用户的母语回复 Issue。
- Dosu 在处理文档方面是巫师，即使根本没有文档。它不仅会提醒你更新文档并帮你编写它，Dosu 还可以在你编码下一个大功能时坐在副驾驶位，就像你坐在作者旁边一样回答问题。
- Dosu 密切注视开放 Issue，解决你可能错过的 Issue 并弃用不再存在的 Issue。如果不确定甚至会询问你。

### Links
- [Web](https://dosu.dev/)
- [X](https://twitter.com/dosu_ai)。
- [LinkedIn](https://www.linkedin.com/company/dosu-ai/)。
- [Founder's LinkedIn - Devin Stein](https://www.linkedin.com/in/devstein/)。
- [Founder's GitHub - Devin Stein](https://github.com/devstein)。


</details>

## [Dot](https://www.getdot.ai/)
帮助数据分析的虚拟助手
<details>

![image](https://assets-global.website-files.com/644a347ea803e322d9c0feb8/644a36f6d9f2d08386070b0d_fox_avatar_7.jpg)

### Category
数据分析、商业智能

### Description
- Dot 允许你与你的数据仓库（如 Snowflake、BigQuery、RedShift、Postgres...）或语义层（如 Looker、dbt、dotML）进行聊天。
- 即时回答大多数业务问题，24/7 全天候运行，这样数据团队可以专注于深度工作，而不是回答关于仪表板的简单问题。
- 分类：研究、商业智能、数据分析。

### Links
- [Website](https://www.getdot.ai/)
- [Linkedin](https://www.linkedin.com/company/sled-software/)。
- Founder's linkedin - [Rick Radewagen](https://www.linkedin.com/in/radewagen/)。

</details>

## [Duckie AI](https://duckie.ai/)
AI 软件开发伴侣团队（小鸭子 Ducklings）

<details>

![image](https://duckie.ai/images/duckie_logo.png)
### Category
编程、多智能体 (Multi-agent)

### Description
Duckie AI 是一个让工程师管理 AI 软件开发伴侣团队（Ducklings）以完成开发工作的平台。
- Ducklings 与工程师合作完成端到端的功能开发，从设计到实现。
- Ducklings 通过聊天定义目标、提出工程设计并生成代码。
- 成立时间：2023年。
- 地点：旧金山。

### Links
- [Web](https://duckie.ai/)
- [X ](https://twitter.com/duckie_ai)。
- [LInkedin](https://www.linkedin.com/company/duckie-ai/about/)。
- [Discord](https://discord.com/invite/JwQSRj9Wx2)。
- [YCombinator profile](https://www.ycombinator.com/companies/duckie-ai)。

</details>

## [Ellipsis](https://ellipsis.dev/?utm_source=awesome-ai-agents)
（前 BitBuilder）“自动化代码审查和 Bug 修复”

<details>

![image](https://app.ellipsis.dev/images/ellipsis_github_logo_white_bg.png&w=640&q=75)

### Category
编程、GitHub、GitLab

### Description
- 创建 Issue。
- 批准实施方案。
- 审查 Pull Request。
- 特性 (Features)
	- 编写代码。
	- 审查更改。
	- 处理评论。
	- 回答问题。

### Links
- [Docs](https://docs.ellipsis.dev)。
- [Installation](https://www.ellipsis.dev/)。

</details>

## [encode](https://encode.software)
处于早期阶段的完全自主 AI 软件工程师

<details>

![image](https://encode.software/_next/image?url=%2Fslack2.png&w=1920&q=75)

### Category
编程

### Description
- 处于 Alpha 阶段。
- encode 与你和你的团队一起完成工作。
- demo: https://encode.software/demo。
</details>


## [Factory](https://www.factory.ai/)
端到端构建软件的编码机器人 (Droids)

<details>

![image](https://assets-global.website-files.com/644b0c1743a3f6abb4f7f149/659c69f2d6e5ba953d5aed58_t%20(1)-p-500.png)

### Category
编程

### Description
- 处于 Alpha 阶段。
- 它不仅仅是另一个像 GitHub Copilot 或 Codeium 这样的编码副驾驶，而是能够自主端到端构建软件的自主 Agent。

### Links
- [CEO](https://twitter.com/matangrinberg)。

</details>

## [Fine](https://www.fine.dev/)
使用 AI Agent 构建软件

<details>

![image](https://assets-global.website-files.com/6290be8d112ee934eeb6aaf2/64e2150d1d1c34380ec59254_logo%20white%20with%20name.png)

### Category
编程、多智能体 (Multi-agent)、自定义构建

### Description
- 部署、管理和运行作为你虚拟队友的 AI Agent。
- 为团队打造，注重组织记忆和协作。
- 隐私优先，我们不存储你的代码，所有内容均在本地运行。
- 多 Agent 平台：构建你自己的定制 Agent。

### Links
- [Twitter](https://twitter.com/thisisfinedev)。
- [Discord](https://discord.gg/nxW8sA5yqe)。
- [YouTube](https://www.youtube.com/@thisisfinedev)。

</details>

## [Fine Tuner](https://fine-tuner.ai/)
（已转型为 Synthflow）Agent 的无代码平台

<details>

![image](https://1a3c84454236f952546f01b263468144.cdn.bubble.io/f1704473650779x346108115281154240/gray%20logo.svg)

### Category
自定义构建、通用

- 借助 Fine-Tuner，你可以大规模构建复杂定制的 AI Agent，无需任何技术技能或编码。只需提供你的数据和想法，我们将为你提供将其转化为强大 AI 解决方案所需的工具集，能够处理海量数据和用户。利用我们可扩展的平台轻松满足不断增长的需求。
- 将聊天机器人连接到你的应用。

- FineTuner.ai 是一个无代码 AI 平台，使用户无需任何编码即可创建和部署定制 AI Agent 和组件。
通过直观的 UI/UX 和快速 API 部署，FineTuner.ai 简化了 AI 开发，让用户专注于其独特的用例和想法。

4.1. 访问 API 选项卡以获取所需令牌和参数的概述，以便使用 REST API 端点将聊天机器人连接到你的应用。
- Fine-Tuner REST API 提供用于 Fine-Tuner 数据类型的 API 端点，允许通过发送和接收 JSON 远程与 AI 模型交互。
- Fine-Tuner API 的身份验证通过 HTTP Bearer Authentication 执行。
- 前端：Bubble。


### Links
- [Twitter](https://twitter.com/finetuner_ai)。
- [Step-by-step guide](https://fine-tuner.ai/resources?res=1682544317646x963647349155168300)。
- [Author](https://twitter.com/0xAlbert_S3)。
</details>

## [Fixie](https://www.fixie.ai/)
创建 LLM 驱动 AI 应用的平台

<details>

![image](https://pbs.twimg.com/profile_images/1715406291349143552/-wRzF29t_400x400.png)

### Category
自定义构建

### Description
- 构建和管理 LLM 驱动的应用。
- 一个基于云的 PaaS，允许开发者构建将 LLMs 与后端逻辑结合的聪明 Agent，以接口数据、系统和工具。


### Links
- [GitHub](https://github.com/fixie-ai)。
- [Fixie Developer Portal](https://docs.fixie.ai/)。
- [AI.JSX](https://docs.ai-jsx.com/)。
- [Twitter](https://twitter.com/fixieai)。
- [Discord](https://discord.com/invite/MsKAeKF8kU)。

</details>

## [Floode](https://floodehq.com/)
自动化通信事务的执行官 Agent

<details>

![image](https://pbs.twimg.com/profile_images/1670794260579270658/sLUFAGGs_400x400.png)

### Category
生产力工具

### Description
- 跨所有通信和工作工具工作：电子邮件、社交媒体 DM、日历、Notion 等。
- 适应你的工作习惯。
- 询问你的助手：
  - 起草消息。
  - 自动分类。
  - 自动安排。
  - 总结、提取任务和信息。

### Links
- Authors: [Sarah Allali](https://twitter.com/SarahAllali7) and [Nicolas Cabrignac](https://twitter.com/Nicowcbg)。
- [Twitter](https://twitter.com/floodehq)。

</details>

## [GitHub Copilot X](https://github.com/features/preview/copilot-x)
AI 驱动的软件开发者

<details>

![image](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/439603i2263F871BE5D381D/image-size/original?v=v2&px=-1)

### Category
编程、GitHub

### Description
- AI 结对程序员。
- Chat 和终端界面。
- PR 支持。
- 早期采用 OpenAI 的 GPT-4。

### Links
- [Community](https://github.com/orgs/community/discussions/)。
- [Documentation](https://docs.github.com/en)。
- [Twitter](https://twitter.com/GitHubCopilot)。

</details>

## [GitLab Duo](https://about.gitlab.com/gitlab-duo/)
软件开发生命周期每一步的 AI

<details>

![image](https://about.gitlab.com/nuxt-images/solutions/ai/duo-logo.svg)

### Category
编程

### Description
- 面向 #DevSecOps 工作流的 AI 驱动功能套件。
- DevSecOps 平台中集成功能工具箱，帮助整个软件开发环境的团队提高效率。
- GitLab Duo 可以做的示例：
	- 计划细化。
	- 安全风险解决。
	- CI/CD 管道健康。
	- 分析图表。

### Links
- [Twitter](https://twitter.com/gitlab)。

</details>

## [GitWit](https://www.gitwit.dev/)
使用 AI 自动化代码生成。处于 Beta 版本中

<details>

![image](https://framerusercontent.com/images/SmLDF79Mns070VHglJVQyuQ1A.png?scale-down-to=512)

### Category
编程

### Description
- GitWit 使用基于 GPT 的 Agent 生成代码并使用 git 跟踪对文件的更改。
- GitWit 将大型语言模型与现代开发者工具联系在一起。
- 它可以通过单个提示词生成和修改代码库。
- GitWit 主要面向全栈开发者，尤其受到具有学习心态的开发者的喜爱——例如那些正在学习新堆栈或技术的人。
- 处于早期 Beta 阶段，可能需要对你输入的提示词进行一些实验。
- 你可以选择以下代码库：
	- React + NextJS。
	- Python using pip。
	- JavaScript Chrome 扩展程序。
	- AngularJS using npm。
	- 自定义堆栈。

</details>

## [GoCharlie](https://gocharlie.ai/)
多模态内容创作自主 Agent 
<details>

![image](https://gocharlie.ai/wp-content/uploads/2023/08/gocharlie_logo_ai_2x-230x49@2x.png)

### Category
内容创作、通用

### Description
GoCharlie 是一个多模态内容创作自主 Agent。

### Links
- [X ](https://twitter.com/GocharlieAI)。
- [Linkedin](https://www.linkedin.com/company/gocharlieai/)。
- Founders' X accounts:
 	- [Kostas Hatalis](https://twitter.com/kostashatalis)。
  	- [Brennan M. Woodruff](https://twitter.com/BrennanWoodruff)。

</details>


## [Graphlit](https://www.graphlit.com/)
面向使用 AI 构建应用的 API 优先数据平台

<details>

![image](https://pbs.twimg.com/profile_banners/1651090820773335040/1687935300/1500x500)

### Category
编程

### Description
- 基于无服务器云原生平台构建，Graphlit 简化了复杂的数据工作流，包括数据摄取、知识提取、语义搜索、警报和应用集成。

### Links
- [Web](https://www.graphlit.com/)。
- [GitHub](https://github.com/graphlit)。
- [X ](https://twitter.com/graphlit)。
- [Discord](https://discord.com/invite/WjxCHhV8Cz)。
- Founder's LInkedin: [Kirk Marple](https://www.linkedin.com/in/kirkmarple/)。
- Founder's X: [Kirk Marple](https://twitter.com/kirkmarple)。
- [Documentation](https://docs.graphlit.dev/getting-started/readme)。

</details>

## [Grit](https://www.grit.io/)
自动化代码迁移和依赖项升级

<details>

![image](https://framerusercontent.com/images/kBmTJBFuy8F87jwrhcMkN9SRI.png?scale-down-to=512)

### Category
编程

### Description
- Grit 使用机器学习和静态分析自动生成 PR 以清理技术债务。
- 用户可以声明他们希望代码的结构方式，让 Grit 为他们重写。

### Links
- [Linkedin](https://www.linkedin.com/company/getgrit/0)。
- [Twitter](https://twitter.com/gritdotio)。

</details>

## [Gumloop](https://www.gumloop.com/)
使用 AI 自动化任何工作流

<details>

![image](https://www.gumloop.com/images/gumloop_logo.svg)

### Category
生产力工具、数据分析、通用、营销、法律、销售、人力资源、金融、教育


### Description
- （前称 AgentHub）。
- 一个构建和托管 LLM 驱动自动化的平台。
- 用我们不断增长的节点库为工作区注入燃料。
- 通过拖放连接将数据从 A 传递到 Z。无需代码。
- 运行你的工作流。在沙箱中测试。查看结果。准备好后，分享给任何人（或无人）。由你控制。

### Links
- [Web](https://www.gumloop.com/)。
- [X (Twitter)](https://x.com/gumloop_ai)。
- [LinkedIn](https://www.linkedin.com/company/gumloop/)。
- [Discord](https://discord.com/invite/xtbrafmzC7)。
- [Documentation](https://docs.gumloop.com/getting-started/introduction)。
- [YouTube](https://www.youtube.com/@AgentHub_Ai)。
- [Medium blog](https://medium.com/@max_82395)。
- [Templates](https://www.gumloop.com/templates)。

</details>

## [Heights Platform](https://www.heightsplatform.com/)
面向课程创作者、社区建设者和教练的平台

<details>

![image](https://yt3.googleusercontent.com/ytc/AIf8zZRVnjibds6hCRgPhxIuFs2UA7E5wIr9a6Iq69-_sw=s900-c-k-c0x00ffffff-no-rj)

### Category
生产力工具

### Description
- Heights AI Chat 可以编辑你的数字产品、回答支持问题并提供业务增长建议。 
- Heights AI Coach 是你个人的自主教练，帮助你实现独特目标。
    - 你的 AI 教练会向你提问并分析你创建的产品，每周为你提供新任务和推荐。
    - 你与 AI 教练分享的信息永远不会与其他创作者的 AI 教练共享。
    - 提交的任何信息都绝不会用于 AI 语言模型训练数据。

### Links
- [AI Features](https://www.heightsplatform.com/features/ai)。
- [Twitter](https://twitter.com/HeightsPlatform)。

</details>


## [Hex Magic](https://hex.tech/product/magic-ai/)
用数据做惊人之事的 AI 工具

<details>

![image](https://images.ctfassets.net/mmgv7yhaaeds/4UFip8DgC0pJEOXeNppEQS/d97b0b1916c9b298f2480c1c28460015/social-sharing-magic.png)

### Category
编程、数据分析

### Description
- “一套旨在增强数据人员的强大 AI 功能。”
- Hex 可以解释和记录你的代码。
- Hex Magic 功能了解数据库架构、过去的操作和项目执行图，因此它们可以做出更深入、更有洞察力的建议。

你可以在这里查看更多内容并加入等待名单。

### Links
- [Launch post](https://hex.tech/blog/magic-private-beta/)。

</details>

## [Heymoon.ai](https://heymoon.ai/)
让你掌握日历、任务和信息的助手

<details>

![image](https://heymoon.ai/assets/images/image04.png?v=a3b31dce)

### Category
生产力工具

### Description
- 生活个人助理：帮你掌控日历、任务和信息。
- 目前处于 Beta 版本中。

### Links
- [Web](https://heymoon.ai/)。

</details>

## [iMean.AI](https://www.imean.ai/)
自动化浏览器任务的 AI 个人助手

<details>

![image](https://www.imean.ai/icon.svg)

### Category
生产力工具、日常生活、自定义构建（Agent 构建框架与平台）

### Description
- iMean 是第一个公开产品，可确定性端到端自动化浏览器任务。
- 与现有解决方案不同，它们要么停留在中间步骤，要么只输出文本指令，iMean 可以为你自动完成任务并给你真实结果。


### Links
- [Web](https://www.imean.ai/)。
- [X (Twitter)](https://twitter.com/iMeanAI)。
- [LinkedIn](https://www.linkedin.com/company/imean-ai/)。
- [Co-founder's X(Twitter) 1](https://twitter.com/zyonwu)。
- [Co-founder's LinkedIn 1](https://www.linkedin.com/in/zyonwu/)。
- [Co-founder's LinkedIn 2](https://www.linkedin.com/in/yanni-shawn-a6222318b/)。
- [Launch post](https://x.com/zyonwu/status/1747801290368004424?s=20)。

</details>

## [Input](https://useinput.com/)
可协作编码的 AI 队友
<details>

![image](https://useinput.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FlightLogo.196eccc1.png&w=640&q=75)

### Category
编程、多智能体 (Multi-agent)、GitHub

### Description
- 用于编码的 AI 助手（或助手团队）。
- 允许邀请团队成员与你和 AI 协作。
- Agent 自主完成工作并推送到 GitHub。

### Links
- [Web](https://useinput.com/)。
- [X](https://twitter.com/useinputai)。

</details>

## [Instrukt](https://github.com/blob42/Instrukt)
用于与 AI Agent 交互的终端环境

<details>

![image](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)

### Category
编程、自定义构建

### Description
- 使用户能够创建和指导模块化 AI Agent，为问答生成文档索引，并将工具附加到 Agent 以增强功能。
- 通过预定义 Agent 促进编码辅助和对话能力，同时提供在键盘和鼠标友好的终端界面中设计定制 Agent 的选项。
- 通过 Docker 容器为 Agent 提供安全的执行环境，允许安全私密的操作，并集成开发者控制台用于调试和内省。


### Links
- [GitHub](https://github.com/blob42/Instrukt)。

</details>

## [Invicta](https://invictai.io/)
组建你的第一支自主 AI Agent 团队

<details>

![image](https://invictai.io/_next/image?url=%2Fimages%2Finvicta-text-black.svg&w=3840&q=75)

### Category
自定义构建（Agent 构建框架与平台）、多智能体 (Multi-agent)

### Description
- 你的 AI 自动驾驶仪，而不仅仅是副驾驶。
- 同步知识库：Notion、Google Drive、URL、所有文件类型等。
- 自我改进：每次交互和协作都会变得更好。
- LLM 无关。使用来自 OpenAI、Google、Mistral 和 Anthropic 等的最佳 LLMs。
- 在团队所在的地方部署 Agent：Zendesk、Slack、Discord 等。
- 合作 AI 团队：你的 Agent 可以像团队一样协作完成复杂工作流。


### Links
- [Web](https://invictai.io/)。
- [GitHub](https://github.com/Invicta-AI)。
- [X (Twitter)](https://twitter.com/InvictaAI)。
- [LinkedIn](https://www.linkedin.com/company/invicta-ai/)。

</details>


## [Julius](https://julius.ai/)
AI 数据处理、分析和可视化

<details>

![image](https://pbs.twimg.com/profile_images/1704414144798261248/PN4b_sxH_400x400.jpg)

### Category
数据分析

### Description
- 聊天驱动的数据分析和 AI Agent，全部在笔记本界面中。
- 允许通过单个提示词回答关于用户数据的任何问题。
- 一个智能数据分析师工具，以直观、用户友好的方式解释、分析和可视化复杂数据。
- “增强版的 Jupyter Notebooks”。

### Description
- [Docs](https://julius.ai/docs/chat-start-guide)。
- [Use cases](https://julius.ai/use_cases)。
- [Twitter](https://twitter.com/JuliusAI_)。
- Team Twitter profiles: [Matt Brockman](https://twitter.com/badphilosopher), [rahul](https://twitter.com/0interestrates)。

</details>

## [Kadoa](https://www.kadoa.com/)
AI 驱动的网页抓取自动驾驶仪

<details>

![image](https://www.kadoa.com/images/kadoa.svg)

### Category
编程、数据分析

### Description
- 使用 LLMs 动态生成网页爬虫和数据处理步骤，适应网站变化。
- 特性 (Features)
	- 无需编码或浏览器扩展程序。
	- 自主爬取 Agent 高效定位网站上的所需信息。
	- 对网站变化的适应性使其免维护。
	- 将来自多个来源的数据转换为相同结构。
	- 自动处理所有点击和滚动。
	- 支持代理 (Proxies)。
	- 强大的集成能力。

### Links
- [Playground](https://www.kadoa.com/playground)。
- Author: [Adrian Krebs](https://twitter.com/krebs_adrian)。

</details>

## [Juno](https://heyjuno.co/)
AI 主导的用户访谈，获取丰富的人类洞察

<details>

![image](https://framerusercontent.com/images/PobjUKj7qACciStbW7PAArGYXc.png?scale-down-to=512)

### Category
数据分析、研究、商业智能、Web UI

### Description
- 认识 Juno！一个 AI 主导的研究平台，进行研究和收集人类洞察。它是无监督的、多语言且自主的。由资深研究人员训练而成，Juno 赋能每个人进行深入定性研究，无需先前经验。
- LLMs/模型提供商支持：
  - OpenAI

### Links

- [Web](https://heyjuno.co/)。
- [X](https://twitter.com/heyjunoco)。
- [LinkedIn](https://www.linkedin.com/company/heyjunoco/)。
- [Privacy overview](https://twitter.com/heyjunoco)。

</details>

## [Kompas AI](https://kompas.ai/)
选择你的 LLM 并构建定制对话 Agent

<details>

![image](https://pbs.twimg.com/profile_images/1712005262633271296/2c9Vdj2B_400x400.png)

### Category
生产力工具、自定义构建、商业智能

### Description
- Kompas AI 是你团队的先进 AI 助手。
- 旨在协助并提升你的生产力。
- 同时处理多个任务。
- 使用 Microsoft Azure 的 OpenAI Service，Kompas AI 在响应速度上超越 ChatGPT Pro。
- Kompas AI 提供免费试用，允许你使用 Pro 版本 10 天。
- Kompas AI 主要使用 gpt-4-turbo、gpt-4-vision 和 gpt-3.5-turbo 模型，但也支持 Gemini、Claude 2 和其他开源模型等。值得注意的是，Kompas AI 具有更大的上下文窗口，通过利用 gpt-4-turbo 的 128K Token 上下文窗口，它可记住过去对话中多达 512,000 个字符以处理更复杂的任务。
- Kompas AI 优先考虑数据安全。你的文件受到强加密保护，传输中的数据得到保障。未使用的数据会定期从系统中删除。

### Links
- [Web](https://kompas.ai/)。
- [X](https://twitter.com/Kompas_AI)。
- [GitHub](https://github.com/KompasAI)。
- [LinkedIn](https://www.linkedin.com/company/kompas-ai/)。
- [Medium](https://medium.com/@Kompas.ai)。
- [Docs](https://docs.kompas.ai/docs/kompas-ai-intro/service-introduction)。

</details>

## [Kusho](https://kusho.ai/)
面向 API 测试的 AI Agent

<details>

![image](https://media.licdn.com/dms/image/D560BAQFE0UatBCw0_w/company-logo_200_200/0/1702642519517/kusho_logo?e=1714003200&v=beta&t=mihS31C5JOQPva4d17sJvNj_QOS1TS9slFp4VAH16u8)

### Category
编程、生产力工具、调试

### Description
- KushoAI 即时生成并运行 API 测试套件，让你轻松推送代码。 
- 将 API 测试委托给 KushoAI，节省数小时手动工作。今天即可解锁无崩溃发布。

1. 添加你的 Postman 集合链接以即时为每个 API 生成全面的测试套件，节省数小时手动工作。

2. 一键获取 AI 分析的测试结果。

3. 在 CI/CD 管道的任何阶段自动运行相关测试套件。”
- 在你的 Postman 集合上运行。

“在 KushoAI，我们相信技术的使命是赋能人们。我们正在构建针对特定问题训练的 AI Agent，以比以往更快的速度释放价值。”

### Links

- [Web](https://kusho.ai/)。
- [X](https://twitter.com/kushoai)。
- [LinkedIn](https://www.linkedin.com/company/kusho/?originalSubdomain=in)。
- [Blog](https://blog.kusho.ai/)。
- [YouTube](https://www.youtube.com/@KushoAI)。
- [Sourabh Gawande - cofounder at Kusho](https://www.linkedin.com/in/sourabhgawande/)。
- [Abhishek Saikia - cofounder at Kusho](https://www.linkedin.com/in/abhishek1315/)。
  
</details>

## [Kwal](https://www.kwal.ai/)
面向招聘的语音 Agent

<details>

![image](https://static.wixstatic.com/media/d84692_0e36f4d5a7974924a68d537a0c8184f9~mv2.png/v1/fill/w_302,h_166,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/d84692_0e36f4d5a7974924a68d537a0c8184f9~mv2.png)

### Category
生产力工具

### Description
- 

### Links

- [Web](https://www.kwal.ai/)。
- [X (Twitter)](https://x.com/Kwal_AI)。
- [LinkedIn](https://www.linkedin.com/company/kwal/about/)。
  
</details>


## [Lindy](https://www.lindy.ai/)
可帮助日常任务的 AI 助手

<details>

![image](https://assets-global.website-files.com/63e15df811f9df22b231e58f/65473d5a31149f709f0d6c39_Group%201266.svg)

### Category
生产力工具

### Description
- Lindy 仍处于 Beta 版本中。
- 特性 (Features)
	- Lindy 对你的电子邮件进行分类。
	- 她从你的收件箱中学习并自动突出显示最高优先级的邮件。
	- 自动冲突处理。
	- 每日简报。
	- 合同管理。
	- 会议记录。
	- 摘要总结。

### Links
- Author: [Flo Crivello](https://twitter.com/Altimor)。
- 
</details>

## [Lutra AI](https://lutra.ai/)
创建 AI 工作流和应用的平台
<details>

![image](https://media.licdn.com/dms/image/D4D0BAQE_KlQYa63Cbg/company-logo_200_200/0/1701917707502/lutra_ai_logo?e=1713398400&v=beta&t=-c8RMYvjM4j06XsJVx1DUJAJ336S80bWO4CSD_IHQao)

### Category
通用、商业智能、生产力工具、内容创作

### Description
- 一个创建个人 AI 工作流和应用的平台。Lutra 首先与你对话以了解你的目标，然后编写代码生成 AI 工作流。
- 这些 AI 工作流类似于帮助你完成各种任务的专用 Agent。因为这些工作流基于代码构建，Lutra 能够安全可靠地执行它们，确保你的数据始终得到保护。
- 每天获取个性化的新闻通讯，包含符合你兴趣的新闻摘要。
- 让 AI 自动将传入电子邮件分类到你选择的类别中。快速完成任务！
- 收集关于个人及其工作公司的公开信息，以便你在见面时做好准备。


### Links
- [Web](https://lutra.ai/)。
- [LinkedIn](https://www.linkedin.com/company/lutra-ai/)。
- [X](https://twitter.com/Lutra_AI)。
- [Discord](https://discord.com/invite/9ZDFvRXe8V)。
- [Founder's LinkedIn - Vijay Vasudevan](https://www.linkedin.com/in/vijay-vasudevan-a5062434/)。
- [Founder's LinkedIn - Jiquan Ngiam](https://www.linkedin.com/in/jngiam/)。

</details>

## [Magic Loops](https://magicloops.dev/)
轻松实现个人自动化
<details>

![image](https://avatars.githubusercontent.com/u/134019091?s=200&v=4)

### Category
编程、内容创作、生产力工具、自定义构建（Agent 构建框架与平台）、AI 应用 SDK、艺术、营销、销售、金融、通用、个人计算

### Description
- Magic Loops 是自动化（几乎）任何事物的最快方式。通过结合生成式 AI 和代码，我们让任何人（是的，甚至非程序员！）都能轻松设置可重复任务和自动工作流。


### Links
- [Web](https://magicloops.dev/)。
- [GitHub](https://github.com/magicloops)。
- [LinkedIn](https://www.linkedin.com/company/magicloops/)。
- [X (Twitter)](https://twitter.com/magicloopsdev)。
- [Founder's LinkedIn](https://www.linkedin.com/in/adam-williams-0995a949/)。
- [Founder's X (Twitter)](https://twitter.com/jumploops)。

</details>

## [Makedraft](https://makedraft.com/)
使用文本提示生成和编辑 HTML 组件

<details>

![image](https://pbs.twimg.com/profile_images/1719412088492445696/qoVdGYth_400x400.jpg)

### Category
编程、生产力工具、生成应用、设计、内容创作

### Description
- Makedraft 是一个根据你的指令生成前端代码的 AI。然后你可以将 HTML 复制到任何项目中。
- 你可以通过文本提示生成 HTML 模板，或高亮你想更改的代码并指示 AI 进行更改。
- Makedraft 还生成 Javascript，以及 Alpine.js。Vue.js 即将推出。
- Makedraft 将推出一个展示区供人们查看项目。Makedraft 目前处于公开 Beta 阶段且免费使用。Pro 计划即将推出。订阅 Pro 计划的用户的生成项目默认设置为私有。

### Links
- [Web](https://makedraft.com/)。
- [Docs](https://docs.makedraft.com/)。
- [X](https://twitter.com/makedraft)。
- [YouTube](https://www.youtube.com/@makedraft)。
- [Founder's X: David Ma](https://twitter.com/realdavidma)。
- [GitHub](https://github.com/makedraft)。


</details>

## [Manaflow](https://manaflow.ai/)
自动化技术业务工作流

<details>

![image](https://bookface-images.s3.amazonaws.com/logos/5e452772f87fd93353d19538fd8f1c9f3ab9b6eb.png)

### Category
生产力工具、编程、工作流自动化

### Description
- Manaflow 赋能非技术团队自动化需要分析数据、连接 API 并采取行动的重复性工作流。
- 使用英语，你可以训练 Manaflow Agent 同时与多个第三方应用接口、托管自定义 API、进行客户访谈、构建持久化数据仪表板、运行自定义 ML 模型以及执行你的业务操作。

### Links
- [Web](https://manaflow.ai/)。
- [X (Twitter)](https://x.com/manaflowai)。
- [LinkedIn](https://www.linkedin.com/company/manaflow-ai/)。
- [YCombinator](https://www.ycombinator.com/companies/manaflow)。


</details>

## [Minion AI](https://minion.ai/)
GitHub Copilot 创作者出品，处于等待名单阶段
<details>

![image](https://minion.ai/img/minion-1.png)

### Category
通用

### Description
GitHub Copilot 创作者出品，处于等待名单阶段。


### Links
- [Twitter](https://twitter.com/ai_minion)。
- Author: [Alex Graveley](https://twitter.com/alexgraveley)。
</details>


## [MultiOn](https://multion.ai/)
使用 MultiOn 预订航班或订购汉堡
<details>

![image](https://pbs.twimg.com/profile_images/1735699647744864256/jrKJWM78_400x400.jpg)

### Category
生产力工具、通用

### Description
- Agent 运行并控制本地 Google Chrome，允许它像人们使用 Google Chrome 与世界/服务/Web 应用交互一样进行交互。
- Agent 本身可能也在本地运行，目前需要本地 Google Chrome 才能 functioning。
- 我们从演示视频中了解到，他们使用本地代码和 ChatGPT 中的自定义插件来控制 Web 浏览器（例如 Google Chrome）。这种设置使 MultiOn 能够执行诸如订购机票等任务，就像人类直接与浏览器交互一样。
- 用例：
	- 许多很棒的真实用例，例如：
	- 完全自主发送电子邮件。
	- 发布推文。
	- 向特定的人发送带有特定消息的推文回复。
	- 给朋友发 Facebook 消息。
	- 搜索度假租赁并检查即将到来的旅行的价格。
	- 搜索婚礼场地并开始婚礼策划过程。
	- 安排洗车服务。
- 在引入 GPT 函数调用后，MultiOn 可以递归调用自身以生成更多子 Agent。
- 与其调用多个函数或 API，你只需要一个通用函数来与所有服务交互并让它自行调用来并行完成更复杂的任务。

### Links
- [Twitter](https://twitter.com/MultiON_AI)。
- Author: [Div Garg](https://twitter.com/DivGarg9)。
</details>

## [Mutable AI](https://mutable.ai/)
AI 加速软件开发

<details>

![image](https://mutable.ai/Reverse-noMargin1000w-p-500.acf1588e.png)

### Category
编程

### Description
- 特性 (Features)
	- AI 自动补全。
	- 一键生产级代码。
	- 提示驱动开发。
	- 测试生成（即将推出）。

### Links
- [Discord](https://discord.com/invite/zAwadbmuVk)。
- [Twitter](https://twitter.com/mutableai)。
- [GitHub](https://github.com/mutableai/)。

</details>


## [Naut](https://www.naut.ai/)
构建你自己的 Agent。处于早期阶段
<details>

![image](https://pbs.twimg.com/profile_images/1643093020097609730/XmHqIOhJ_400x400.jpg)

### Category
自定义构建、多智能体 (Multi-agent)

### Description
“组建为你工作的 AI Agent 团队。现在开放早期访问。加入等待名单。”


### Links
- [Twitter](https://twitter.com/naut_ai)。
</details>


## [NexusGPT](https://gpt.nexus/)
几分钟内构建 AI Agent，无需编码
<details>

![image](https://pbs.twimg.com/profile_images/1784129822320467968/n_9UYcHR_400x400.jpg)

### Category
构建 AI 产品的技术挑战、构建 AI 产品的商业/营销挑战

### Description
- NexusGPT 使任何人都能在不触碰一行代码的情况下构建、微调和集成自主 AI Agent。
- 在 Nexus 上，你可以创建能够执行你能想象的任何任务的 Agent，并将它们整合到你最关心的地方（从你的网站到你的内部 Slack 频道）。
- 为此，Nexus 提供现有超过 1000 个现成 Agent 的市场以及超过 1500 个可随时添加到你的 Agent 的工具。
- 你还可以添加自定义知识（来自 pdf、pptx、docx、网站、Notion 等）并将其添加到你自己的 Agent 中，使其与你的用例和业务相关。
- 最后，当你准备部署 Agent 时，你可以直接在您的网站、WhatsApp、Slack、Teams 等平台上一键完成。”


### Links
- [Web](https://gpt.nexus/)。
- [X (Twitter)](https://twitter.com/nexus_gpt)。
- [LinkedIn](https://www.linkedin.com/company/nexusgpt/)。

</details>


## [Otherside's AI Assistant - Hyperwrite](https://www.hyperwriteai.com/)
Chrome 扩展程序 - 通用 AI Agent

<details>


![image](https://assets-global.website-files.com/63fcd79d410b22ddf397e1b8/654272554402410a71c84ab9_6405c1cabdf9c69f05b1080e_otherside_logo_symbol.webp)

### Category
生产力工具、通用


### Description
- Hyperwrite 是一个 Chrome 应用，可以控制你的浏览器并代表你完成高级任务。
- AI Agent 像人类一样使用 Web 浏览器。
- “只需描述你想让它做什么，它会自动操作 Chrome 以实现你的目标。”
- 用例示例：预订航班、订购食物、研究复杂主题、管理你的电子邮件。
- 设计用于处理从预订航班到进行深入研究等各种任务。
- 使用示例：
	- 整理 Gmail 收件箱。
	- 预订航班。
	- 在线购物。
	- 寻找招聘候选人。

### Links
- [Launch announcement](https://twitter.com/mattshumer_/status/1673730806865358848)。
- [Google Chrome Extension](https://chrome.google.com/webstore/detail/hyperwrite-ai-writing-com/kljjoeapehcmaphfcjkmbhkinoaopdnd)。
- [Article](https://venturebeat.com/ai/hyperwrite-unveils-breakthrough-ai-agent-that-can-surf-the-web-like-a-human/)。

</details>

## [Phind](https://www.phind.com/)
个人编程和研究 AI 助手

<details>

![image](https://www.phind.com/images/phind_v2.svg)

### Category
编程、研究

### Description
- Phind 是一个 AI 搜索引擎和结对程序员。

### Links
- [Web](https://www.phind.com/)。
- [Discord](https://discord.com/invite/S25yW8TebZ)。
- [X (Twitter)](https://twitter.com/phindsearch)。
- CEO's Twitter: [Michael Royzen](https://twitter.com/MichaelRoyzen)。

</details>

## [Powerdrill AI](https://powerdrill.ai/)
AI Agent 以 10 倍速度完成你的数据工作

<details>

![image](https://media.licdn.com/dms/image/D4E0BAQGwWRCWd6izLg/company-logo_200_200/0/1686636701294?e=1726099200&v=beta&t=oFa1Z8ulQzNuasFcQBdrzZD8L1RJ_vjPhbbl4KXkN7g)

### Category
数据分析、生产力工具、研究、营销、销售、金融

### Description
- Powerdrill 是一个以个人和企业数据集为中心的 AI SaaS 服务。
- 旨在释放你数据的潜力，Powerdrill 使你能够使用自然语言轻松与你的数据集交互，执行从简单问答到深刻 BI 分析的各种任务。
- 通过打破知识获取和数据处理的障碍，Powerdrill 呈指数级提高数据处理效率。

### Links
- [Web](https://powerdrill.ai/)。
- [Twitter](https://x.com/powerdrillai)。
- [Documentation](https://docs.powerdrill.ai/introduction)。

</details>

## [Proficient AI](https://proficientai.com)
用于构建 AI Agent 的交互 API 和 SDKs
<details>

![image](https://www.phind.com/images/phind_v2.svg)

### Category
自定义构建

### Description
- 一个端到端解决方案，只需 3 分钟而非数周即可在你的应用中运行面向用户的 Agent（目前包括 3 个 SDK，含 React）。
- 管理面板和管理 API 中内置的强大工具，包括分析、监控、速率限制、内容审核等。
- 最小化或消除对自定义后端基础设施的需求，让你专注于实现业务逻辑。
- 技术无关的解决方案支持多个 LLM 提供商（目前支持来自 OpenAI 和 Anthropic 的 7 个模型），允许你通过 1 次点击轻松切换模型。
- 开箱即用、高度可定制且美观的 UI 组件，渲染复杂的交互树，并支持高级功能如流式传输。

### Links
- [Documentation](https://docs.proficientai.com)。
- [GitHub](https://github.com/proficientai/js)。
- [Discord](https://discord.gg/DVbwTM8erb)。
</details>

## [Promptly](https://www.trypromptly.com/)
面向企业的生成式 AI

<details>

![image](https://assets-global.website-files.com/64627565e0cbc380d04ed8ae/6488f9eb9992aa1dc3bc1a63_logo.svg)

### Category
自定义构建、无代码、Web UI

### Description
- 构建量身定制的生成式 AI Agent、应用和聊天机器人，以满足你用户的独特需求。
- 无需任何编码经验即可无缝集成你自己的数据和 GPT 驱动模型。
- Promptly 支持所有主要模型提供商，如 OpenAI、Cohere、Stability AI、Hugging Face 等。轻松使用这些模型来构建强大的应用。
- Promptly 提供可嵌入的小部件，你可轻松将其集成到你的网站中。使用这些小部件构建对话式 AI 应用或向你的网站添加聊天机器人。
- 导入你自己的数据并将其连接到 LLM 模型以增强你的生成式 AI 应用和聊天机器人。Promptly 支持各种数据来源，包括 Web URL、Sitemaps、PDFs、音频、PPTs、Google Drive、Notion 导入等。
- LLMs/模型提供商支持：
  - OpenAI。
  - Cohere。
  - Stability AI。
  - Hugging Face。

### Links
- [Web](https://www.trypromptly.com/)。
- [X](https://twitter.com/trypromptly)。
- [GitHub](https://github.com/trypromptly)。
- [Discord](https://discord.com/invite/3JsEzSXspJ)。
- [LinkedIn](https://www.linkedin.com/company/trypromptly/)。
- [YouTube](https://www.youtube.com/@trypromptly)。

</details>

## [Q, ChatGPT for Slack](https://q-bot.suchica.com/)
面向资源不足的中小企业的 Slack AI 劳动力

<details>

![image](https://q-bot.suchica.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FDALLE_2023-01-10_QRobot.86c0521b.png&w=256&q=75)

### Category
通用、个人助手、商业智能、生产力工具

### Description
- Q 在您的工作区中像 ChatGPT 一样运行。
- 安全且可共享，Q 不会存储或学习你的数据。
- 与 ChatGPT 不同，Q 可根据你的输入按需读取各种类型的 URL 和文件。
- 非常适合总结、评估、头脑风暴想法、自我审查、问答等。
- 我们还支持需要身份验证的 URL，例如 Google Workspace Apps。
- 列出你团队特定的规则、指南和模板。


### Links
- [Web](https://q-bot.suchica.com/)。
- [GitHub](https://github.com/hiroshinishio)。
- [LinkedIn](https://www.linkedin.com/company/suchica/)。
- [X](https://twitter.com/QBotGPT)。
- [YouTube](https://www.youtube.com/@q-aibot-2182/videos)。
- [Founder's LinkedIn](https://www.linkedin.com/in/hiroshi-nishio-084595216/)。
- [Founder's X](https://twitter.com/hnishio0105)。
</details>


## [Questflow](https://questflow.ai)
面向无代码自主 AI 工人的市场

<details>

![image](https://www.aitoolsclub.com/content/images/2023/07/Screenshot-2023-07-26-184451.png)

### Category
自定义构建

### Description
- Questflow 是一个面向中小企业连接自主 AI 工人的市场。
- 我们的平台使数字工人能够发现和部署 AI Agent 以实现无缝工作流自动化。
- 通过无代码编辑器，我们赋能数字知识提供者创建、分发和变现 AI 工人。
- 类似于 Upwork，Questflow 提供一个市场，用户可利用 AI Agent 在各种数字工作空间中完成任务。
- 创作者有机会将他们的专业知识转化为 AI Agent，扩大影响力并产生收入。

### Links
- [Twitter](https://twitter.com/questflow)。
- [Telegram](https://t.me/+lAFNg26e5aA5NGNl)。
- [Discord](https://twitter.com/questflow)。

</details>

## [Rebyte](https://rebyte.ai/)
多 AI Agent 构建平台
<details>

![image](https://pbs.twimg.com/profile_images/1700140660702257152/xTLqugBI_400x400.jpg)

### Category
通用、生成应用、自定义构建

### Description
- 一个面向 GenAI 应用构建的多 AI Agent 平台。

### Links
- [Web](https://rebyte.ai/)。
- [X](https://twitter.com/ReByteAI)。
- [Discord](https://discord.com/invite/e4AYNnFg2F)。
- [LinkedIn](https://www.linkedin.com/company/realchar/)。
- [Founder's LinkedIn - Jian cai](https://www.linkedin.com/in/jian-cai-8611094/)。
- - [Founder's LinkedIn - Xiao(Shaun) W.](https://www.linkedin.com/in/shaunwei/)。

</details>

## [Relevance AI](https://relevanceai.com/)
构建你的 AI 劳动力

<details>

![image](https://mintlify.s3-us-west-1.amazonaws.com/relevanceai/images/logo/dark.png)

### Category
内容创作、生产力工具、研究、自定义构建（Agent 构建框架与平台）、营销、销售、通用、多智能体 (Multi-agent)、支持开源模型

### Description
- Relevance AI 是一个快速构建和部署 AI 应用和 Agent 的平台。它是 AI 劳动力的家园。
- AI 劳动力是你雇佣的数字团队，协助你完成琐碎和重复性任务。
- AI 劳动力由配备特定于你的业务操作工具的 Agent 组成，这些工具由领域专家打造。
- 借助 Relevance，你将拥有一个单一平台来创建你的工具、将它们装备给 Agent 并作为多 Agent 系统 (MAS) 部署到你的组织中。
- Relevance 支持 OpenAI、Anthropic、Cohere、PaLM 等。



### Links
- [Web](https://relevanceai.com/)。
- [GitHub](https://github.com/RelevanceAI)。
- [X (Twitter)](https://x.com/RelevanceAI_)。
- [LinkedIn](https://www.linkedin.com/company/relevanceai/)。
- [Jacky Koh - X (Twitter)](https://x.com/JackyGKoh)。
- [Daniel Vassilev - X (Twitter)](https://x.com/thedanvass)。

</details>

## [Saga](https://saga.so/ai)
用于笔记、任务和工具的数字化 AI 助手
<details>

![image](https://uploads-ssl.webflow.com/600abb9dfd0530004ee876c0/62bd6a08f11f1f89bb1d1170_saga-logo.svg)

### Category
生产力工具、内容创作

### Description
- 生成内容。
- 头脑风暴想法。
- 翻译。
- 语法检查。
- [Roadmap](https://sagahq.canny.io/)。

### Links
- [Twitter](https://twitter.com/saga_hq)。
- [Slack](https://sagacommunity.slack.com/join/shared_invite/zt-13m3lrrdt-1x6~l6sLuR8CX~4c3fWwHA#/shared-invite/email)。
- [Discord](https://discord.com/invite/cgz2mUEq7P)。


</details>

## [Second](https://www.second.dev/)
代码的自动化迁移和升级

<details>

![image](https://assets-global.website-files.com/63717dfd25366f06c3ed64cc/645dcdc2d70f00fded6f6c0b_second-logo-white.png)

### Category
编程

### Description
- 迁移框架（如 Angular 到 React）、库（如 Redux 到 React Context）或语言（如 JavaScript 到 TypeScript）。
- 对任意数量、任意大小的应用执行主要版本升级。
- 升级框架（如 Next.js 12 到 13）、库（如 MUI 4 到 5）或语言（如 Python 2 到 3）。
- 目标用户：企业代码库。
- [Roadmap](https://second.canny.io/)。

### Links
- [YCombinator](https://www.ycombinator.com/companies/second)。
- [Twitter](https://twitter.com/SecondDevHQ)。
- [Linkedin](https://www.linkedin.com/company/secondhq/)。
- [Discord](https://discord.com/invite/ZhYUEjsW3Z)。
- Founder: [Eric Rowell](https://twitter.com/ericdrowell)。

</details>

## [Sentius](https://www.sentius.ai/)
AI Agent 操作浏览器为你完成任务

<details>

![image](https://assets-global.website-files.com/65322c702cb29c000a4d7f49/65323973bde43d64e5b01d0f_logo.svg)

### Category
通用、多智能体 (Multi-agent)、支持开源模型

### Description
- 面向企业的自主 Agent。
- Sentius 的高负载自主 Agent 平台在企业安全边界内运行，无论是在云端还是本地部署，并启用企业自主 Agent 的安全创建、部署和管理。
- Sentius 提供集成的无代码开发工具套件，用于在组织内部构建、测试、部署和管理自主 Agent。
- Sentius 为针对你组织特定需求的用例提供强大高效的自主 Agent。

### Links
- [Web](https://www.sentius.ai/)。
- [GitHub](https://github.com/Generative-Assistants/)。
- [LinkedIn](https://www.linkedin.com/company/sentiusai/)。
- [YouTube Demo](https://www.youtube.com/watch?v=amjFOO_v28Q&ab_channel=DanielKornev)。
- [X (Twitter)](https://twitter.com/sentiusai)。
- Team LinkedIn profiles: [1](https://www.linkedin.com/in/eugene-izhikevich/)、[2](https://www.linkedin.com/in/dilyara-zharikova/)、[3](https://www.linkedin.com/in/mikhail-burtsev-85a47b9/)、[4](https://www.linkedin.com/in/danielkornev/)。

</details>

## [ShopPal](https://shoppal.ai)
AI 助手，提升购物体验。

<details>

![image](https://pbs.twimg.com/profile_images/1777239533094150144/a28xyvug_400x400.jpg)

### Category
生产力工具、研究、电商

### Description
- “🛍️ShopPal：你的策展 AI 购物助手🥂💰💳。
- 策展 AI 购物助手，旨在增强和陪伴你的购物体验。
- 为了增强和陪伴你的购物体验，ShopPal 提供总结洞察、定制推荐、视觉比较和最优惠价格，全部为你量身定制！”

### Links
- [Web](https://shoppal.ai)。
  
</details>

## [Spell](https://spell.so/)
带有插件的 AutoGPT Agent
<details>

![image](https://spell.so/_next/static/media/logo.32731dee.svg)

### Category
通用

### Description
- “将你的任务委托给自主 AI Agent。使用由 GPT4 驱动的革命性和直观 AI 工具转变你的日常工作。”
- 访问 Zapier、Wolfram 等 API。
- 打开链接。
- 操作文件。
- 搜索网络。

### Links
- [Author's Twitter](https://twitter.com/rafal_makes)。

</details>

## [Superluminal](https://superluminal.dev)
产品数据仪表板的 AI 副驾驶

<details>

![image](https://superluminal.dev/176fae26858de1966f98.svg)

### Category
编程、数据分析

### Description
- 在几分钟内使用 Superluminal React 组件设置，或直接使用 API 进行自定义解决方案。
- 编写 Python 代码来回答问题并执行任务，类似于 ChatGPT + CodeInterpreter。
- 为安全执行生成的代码提供完全托管的计算基础设施。
- 定制外观和感觉以适合你的产品。
- 全面支持图表、数据透视表和过滤器以及文本答案。
- 启用客户从仪表板上已有的数据中提取更多价值，对高级问题提供有意义的回答。


### Links
- [Twitter](https://twitter.com/getluminal/)。
- [Linkedin](https://www.linkedin.com/company/74930600/)。

</details>

## [TalktoData](https://talktodata.ai/)
数据发现、清理、分析和可视化

<details>

![image](https://talktodata.ai/hubfs/logo-transparant-04-1.svg)

### Category
编程、数据分析

### Description
- 与你的 CSV、Excel、Google Sheets 和 SQL 数据库一起工作的 AI 数据分析师。
- 面向所有数据分析需求的 AI Agent。
- 允许用户生成漂亮的可视化效果、后续问题和优化需求。
- “数据分析的 ChatGPT”。
- 一个永不休眠且随时可用的数据分析师（只需聊一句）。


### Links
- [Web](https://talktodata.ai/)。
- [Twitter](https://twitter.com/TalktoData)。
- [Linkedin](https://www.linkedin.com/company/talktodata/)。
- Team Twitter profiles: [Vinod Varma](https://twitter.com/vinodvarma24)。
</details>

## [Taskade](https://www.taskade.com/)
创建、训练和运行定制 AI Agent

<details>

![image](https://www.taskade.com/static_images/taskade-circle-logo-full-black.png)

### Category
自定义构建、通用、生产力工具

### Description
- 面向自定义任务、自动化和工作流的 AI Agent。
- AI 生成器用于流程图、思维导图、任务管理。 
- AI Chat 助手和媒体问答，支持项目、文档等。
- 定制 AI Agent：使用自定义命令、工具和知识制作 AI Agent 以自动化任务。
- 通过动态 AI Chat 助手与项目和文档互动，提供媒体问答和上下文支持。



### Links
- [Web](https://taskade.com/)。
- [Twitter](https://twitter.com/taskade)。
- [Linkedin](https://www.linkedin.com/company/taskade/)。
- Team Twitter profiles: [John Xie](https://twitter.com/johnxie)。
</details>


## [ThinkChain AI](https://www.thinkchain.ai/)
金融 AI Agent 平台

<details>

![image](https://media.licdn.com/dms/image/D4E0BAQGc0T7tqN-IZQ/company-logo_200_200/0/1688338143903?e=2147483647&v=beta&t=bwM2YckiHgvHaMtmYQjB6XGUT5FNtUbvFNHJvepsGu4)

### Category
金融、数据分析

### Description
- ThinkChain 提供大量且不断增长的先进 AI Agent，例如：
  	- Discover Agent - 可访问搜索和你的知识库以获取知情答案。
  	- Chain of Thought Agent - 将问题分解为独立解决的部分。
  	- Analyst Agent - 创建实时财务分析，从 DCF 到 LBO 等一切。
  	- Auto Agent - 可从头开始创建整个工作流。
- 目前处于早期访问版本中。

### Links
- [Web](https://www.thinkchain.ai/)。
- Founder: [Tony Lewis](https://twitter.com/_tony_lewis)。

</details>

## [Test Driver](https://testdriver.ai/)
GitHub 中的 QA AI Agent

<details>

![image](https://framerusercontent.com/images/in0q3dhCrmymGzApkC4KBzdpcE.png?scale-down-to=512)

### Category
编程、生产力工具、调试、测试

### Description
- “不再编写自动化测试或等待手动测试。
- 指示 @testdriverai 用自然语言测试任何 PR。
- TestDriver 将对你的 PR 进行测试并返回视频和日志记录。”

### Links
- [Web](https://testdriver.ai/)。
- [X (Twitter)](https://twitter.com/sunglassesface)。
- [LinkedIn](https://www.linkedin.com/in/adam-eldefrawy-8623a815a/)。
    
</details>

## [Tusk](https://usetusk.ai/)
推送和测试代码的 AI 工程师

<details>

![image](https://usetusk.ai/tusk-logo.eed7968a.png)

### Category
编程

### Description
- Tusk 是一个 AI 工程师，帮助产品经理快速交付简单的前端更改，让他们的软件工程师专注于更重要的工作。
- 将产品工单分配给 Tusk，让我们的 AI 为你编写、推送和测试代码。
- 用例：编码、调试、代码迁移等。
- Tusk 是一家 [Y-combinator 公司](https://www.ycombinator.com/companies/tusk)。


### Links
- [Web](https://usetusk.ai/)。
- [GitHub](https://github.com/apps/use-tusk)。
- [X ](https://twitter.com/usetusk)。
- [LinkedIn](https://www.linkedin.com/company/usetusk/about/)。
- [Founder's X](https://twitter.com/sohilkshirsagar)。
- [Founder's X 2](https://twitter.com/Marcel7an)。
  
</details>

## [Vortic](https://www.vortic.ai/)
帮助保险销售和理赔的 AI Agent

<details>

![image](https://media.licdn.com/dms/image/D560BAQEG1EZ0w5b_pw/company-logo_200_200/0/1710090819045/vortic_ai_logo?e=2147483647&v=beta&t=cNHAuR0hBAAO_LAhV9iNj0Ha3s8gkQkl1esp3i1RGD4)

### Category
生产力工具、自定义构建（Agent 构建框架与平台）、销售、通用、多智能体 (Multi-agent)、支持开源模型

### Description
- Vortic 希望让企业轻松嵌入具有真正业务成果的 Agent。
- Vortic 旨在通过预建 Agent 提供实时价值实现，其生态系统提供定制工具包。

### Links
- [Web](https://www.vortic.ai/)。
- [Co-founder's LinkedIn 1](https://www.linkedin.com/in/harshnagalla/)。
- [Co-founder's LinkedIn 2](https://www.linkedin.com/in/divyajot-singh-06b78559/)。

</details>


## [v0 by Vercel](https://v0.dev/)
基于 Shadcn UI & Tailwind CSS 获取 React 代码

<details>

![image](https://ph-files.imgix.net/2c7b17e3-7a6d-4872-ab81-471803a924ce.png?auto=format)

### Category
编程

### Description
v0 是 Vercel Labs 的生成式用户界面系统，由 AI 驱动。它基于 Shadcn UI 和 Tailwind CSS 生成复制粘贴友好的 React 代码。
- 目前处于等待名单阶段。
- v0 即时生成自定义组件，你可将其复制并粘贴到你现有的代码库中。
- 基于 NextJS App Router 构建。
- AI 由 Vercel `ai` SDK 驱动。


### Links
- [Web](https://v0.dev/)。
- [X post](https://x.com/rauchg/status/1702353417375826303?s=20)。

</details>

## [Wispy](https://wispy.technicalmagic.ai/)
总结内容、撰写内容、创建测验

<details>

![image](https://wispy.technicalmagic.ai/assets/icon-white.svg)

### Category
研究、内容创作

### Description
Wispy 是一个 Web 浏览 AI 助手，可总结内容、撰写内容、解释事物或为你正在学习的主题创建测验。
- Wispy 仍处于 Beta 版本中。
- 借助 Wispy，你可以在不离开浏览器舒适区的情况下轻松转换网页内容以完美适应你的独特需求。
- Chat-based AI like Llama and GPT-4 不是将 AI 融入你生活的唯一方式。
- 借助 Wispy，超越聊天机器人，拥有一个原生浏览器的 AI 伴侣，让你的浏览更加愉快、高效和 streamlined！


### Links
- [Web](https://wispy.technicalmagic.ai/)。
- [Chrome extension](https://chrome.google.com/webstore/detail/wispy-your-personalized-a/nbljfchpacfegmmmajcneihieeglpofc)。


</details>

## [Wordware](https://www.wordware.ai/)
快速构建更好的语言模型应用。

<details>

![image](https://media.licdn.com/dms/image/D4D0BAQFwJFfvXQ7j4A/company-logo_200_200/0/1693909474889/wordware_logo?e=1714003200&v=beta&t=65DGJQN1bRfjKhVmkWwH393y1_1L7ej8qd6yGYtmdpM)

### Category
自定义构建、支持开源模型

### Description
- Wordware 是你部署 LLM 应用的一站式平台。
- LLMs/模型提供商支持：
  - GPT-3.5。
  - GPT-4 Turbo。
  - GPT-4。
  - GPT-4 Vision。
  - MISTRAL。
  - MIXTRAL。
  - Claude instant。
  - Claude 2。
  - [关于支持模型的 X 帖子](https://x.com/bertie_ai/status/1734539295187214423?s=20)。

### Links

- [Web](https://www.wordware.ai/)。
- [X](https://twitter.com/wordware_ai)。
- [LinkedIn](https://www.linkedin.com/company/wordware/)。
- [Filip Kozera - founder at Wordware](https://www.linkedin.com/in/filipkozera/)。
  
</details>

## [WorkBot](https://workhub.ai/)
你唯一需要的 AI 平台！

<details>

![image](https://workhub.ai/wp-content/uploads/2023/05/workhub-logo-horizontal.png)

### Category
科学、生产力工具、商业智能

### Description
- “一个以隐私为中心的对话式 AI 平台，利用 AI Agent、商业和开源 LLM 支持来集中知识，从而丰富协作并促进顺畅的自动化。
- WorkHub 赋予用户多功能对话机器人和工具的能力，提供洞察、知识和数据驱动的操作。
- 通过无缝集成能力，Workhub 可连接到任何数据库和应用，确保全面的信息访问。”


### Links
- [Web](https://workhub.ai/)。
- [LinkedIn](https://www.linkedin.com/company/workhub-official/)。
- [X (Twitter)](https://x.com/WorkHubOfficiaI)。

</details>

## [Zapier Central](https://zapier.com/central)
与 AI 机器人并肩工作

<details>

![image](https://bot-templates-dbuh9gyx1.vercel.zapier-deployment.com/_next/static/media/logo-color.9fac53e4.svg)

### Category
自定义构建、生产力工具、通用

### Description
- Zapier Central 是一个实验性 AI 工作区，你可以在其中教导机器人跨 6,000+ 应用工作。
- 特性 (Features)：
  - 给你的机器人访问公司真相来源的权限以获取即时答案。
  - 让机器人在 6,000+ 应用中行动。
  - Central 在 Zapier 生态系统上运行，帮助你自动化你已在使用工具。
  - 一次教导你的机器人，然后看着它工作——即使你不在身边。
  - 一切都在一个工作区中。

### Links

- [Web](https://zapier.com/central)。
  
</details>



## :eight_pointed_black_star: 具有沙箱集成或原生支持的 AI 应用与 Agent

### :eight_pointed_black_star: [Superagent](https://www.superagent.sh/)
<details>

Superagent 使用 E2B 作为[代码执行工具](https://x.com/pelaseyed/status/1709592941226831916?s=20)。要尝试将 Superagent 与 E2B 一起使用，请创建一个 Code Interpreter API，然后为你的 Agent 选择它。
</details>

### :eight_pointed_black_star: [OpenAI's Assistants](https://e2b.dev/docs/llm-platforms/openai/)
<details>

你可以为 AI 助手定义操作，E2B 将在沙箱中自动执行它们。这允许你创建具有完全预定义的强大 AI 助手。
要[尝试将 OpenAI Assistants 与 E2B 一起使用](https://e2b.dev/docs/llm-platforms/openai)，你可以按照我们在 [Python](https://e2b.dev/docs/llm-platforms/openai#python) 或 [JavaScript](https://e2b.dev/docs/llm-platforms/openai#java-script) 中的指南操作。 

</details>

### :eight_pointed_black_star: [Langchain Data Analyst](https://python.langchain.com/docs/integrations/tools/e2b_data_analysis)

<details>

E2B 数据分析沙箱[已集成到 Langchain 中](https://python.langchain.com/docs/integrations/tools/e2b_data_analysis)，允许你：
- 运行 Python 代码。
- 通过 matplotlib 生成图表。
- 在运行时动态安装 Python 包。
- 在运行时动态安装系统包。
- 运行 Shell 命令。
- 上传和下载文件。
另请参阅[指南](https://e2b.dev/blog/build-ai-data-analyst-with-langchain-and-e2b)。

</details>

## 想将 E2B 用于你的 AI 产品？
通过 [hello@e2b.dev](mailto:hello@e2b.dev) 或 [Discord](https://discord.gg/35NF4Y8WSE) 联系我们。

我们是开源的，你可以在此处开始使用 E2B [here](https://e2b.dev/docs?ref=awesome-sdks)。

<!-- 
<img src="/assets/footer.png" width="100%" alt="SDKs Repo Visual" />
-->

## 加入社区
- 在 [X ](https://twitter.com/e2b) 关注我们。
- [在 Discord 上联系我们](https://discord.gg/35NF4Y8WSE)。
- 随时通过 [hello@e2b.dev](mailto:hello@e2b.dev) 与我们联系。

<!-- 
<a href="https://discord.gg/U7KEcGErtQ" target="_blank">
	<img src="https://img.shields.io/static/v1?label=Join&message=%20discord!&color=mediumslateblue">
</a>
<a href="https://twitter.com/e2b" target="_blank">
	<img src="https://img.shields.io/twitter/follow/e2b.svg?logo=twitter">
</a>
-->



<!-- More agents to add in the future

- GPTeam https://twitter.com/itstimconnors/status/1672278464362336256
- https://github.com/101dotxyz/GPTeam

- Neurite https://github.com/satellitecomponent/Neurite

- AutoGPT.js https://github.com/zabirauf/AutoGPT.js

- Street Fighter https://github.com/linyiLYi/street-fighter-ai

- GPT RPG https://github.com/dzoba/gptrpg

- Autopilot https://github.com/fjrdomingues/autopilot

- WinGPT - AI assistant for Windows https://news.ycombinator.com/item?id=36472854



-->