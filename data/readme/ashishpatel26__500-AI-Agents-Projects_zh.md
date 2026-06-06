# 🌟 500+ AI 智能体项目/用例

[![500-AI-Agents-Projects - UseCase](https://img.shields.io/badge/500--AI--Agents--Projects-UseCase-2ea44f?logo=https%3A%2F%2Fstatic-00.iconduck.com%2Fassets.00%2Frobot-emoji-2048x2044-kay057lt.png&logoColor=2ea44f)](https://github.com/ashishpatel26/500-AI-Agents-Projects)

![img](images/AIAgentUseCase.jpg)

这是一份精选的跨行业 AI 智能体用例合集，展示了实际应用场景并链接了可落地的开源项目。探索 AI 智能体如何变革医疗、金融、教育等行业！🤖✨

---

## 📋 目录

- [简介](#introduction)
- [行业用例](#-industry-usecase-mindmap)
- [用例总表](#use-case-table)
- [按框架分类的用例](#framework-wise-usecases)
  - [CrewAI 用例](#framework-name-crewai)
  - [Autogen 用例](#framework-name-autogen)
  - [Agno 用例](#framework-name-agno)
  - [Langgraph 用例](#framework-name-langgraph)
- [参与贡献](#contributing)
- [许可证](#license)

---

## 🧠 简介

人工智能（AI）智能体正在彻底改变各行各业的运作方式。从个性化学习到金融交易机器人，AI 智能体带来了效率、创新与可扩展性。本仓库提供：

- 按行业分类的 AI 智能体应用列表。
- 详细用例说明及对应的开源项目落地链接。

无论你是开发者、研究人员还是商业爱好者，这里都是你获取 AI 智能体灵感与学习资源的绝佳指南。

---

## 🏭 行业用例思维导图

![](images/industry_usecase1.png)

---

## 🧩 用例总表

| 用例 | 行业 | 描述 | GitHub 代码仓库 |
| ------------------------------------------- | ---------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **HIA (健康洞察智能体)**       | 医疗         | 分析医学报告并提供健康建议。    | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/harshhh28/hia.git)                                                                             |
| **AI 健康助手**               | 医疗       | 利用患者数据诊断和监测疾病。      | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/ahmadvh/AI-Agents-for-Medical-Diagnostics.git)                                                 |
| **自动化交易机器人**             | 金融          | 结合实时市场分析自动执行股票交易。  | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MingyuJ666/Stockagent.git)                                                                     |
| **虚拟 AI 导师**                  | 教育        | 提供面向用户的个性化教育服务。       | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/hqanhh/EduGPT.git)                                                                             |
| **全天候 AI 客服机器人**                   | 客户服务 | 全天候处理客户咨询。               | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/NirDiamant/GenAI_Agents/blob/main/all_agents_tutorials/customer_support_agent_langgraph.ipynb) |
| **商品推荐智能体**      | 零售           | 根据用户偏好和历史记录推荐商品。 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/microsoft/RecAI)                                                                               |
| **自动驾驶配送智能体**       | 交通运输   | 优化路线并自主完成包裹配送。     | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/sled-group/driVLMe)                                                                            |
| **工厂流程监控智能体**  | 制造业    | 监控生产线并确保质量控制。   | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/yuchenxia/llm4ias)                                                                             |
| **房产定价智能体**            | 房地产      | 分析市场趋势以确定房产价格。     | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/AleksNeStu/ai-real-estate-assistant)                                                           |
| **智慧农业助手**           | 农业      | 提供作物健康状况分析及产量预测建议。  | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/mohammed97ashraf/LLM_Agri_Bot)                                                                 |
| **能源需求预测智能体**   | 能源行业           | 预测能源消耗以优化电网管理。       | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/yecchen/MIRAI)                                                                                 |
| **内容个性化智能体**     | 娱乐业    | 根据偏好推荐个性化媒体内容。      | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/crosleythomas/MirrorGPT)                                                                       |
| **法律文档审查助手**   | 法律行业            | 自动化文档审查并高亮关键条款。    | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/firica/legalai)                                                                                |
| **招聘推荐智能体**  | 人力资源  | 为职位空缺推荐最匹配的候选人。           | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/sentient-engineering/jobber)                                                                   |
| **虚拟旅行助手**          | 酒店与旅游      | 根据偏好规划旅行行程。           | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/nirbar1985/ai-travel-agent)                                                                    |
| **AI 游戏陪伴智能体**           | 游戏行业           | 通过实时辅助提升玩家体验。    | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/onjas-buidl/LLM-agent-game)                                                                    |
| **实时威胁检测智能体**  | 网络安全    | 识别潜在威胁并缓解攻击。      | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/NVISOsecurity/cyber-security-llm-agents)                                                       |
| **电商个人购物助手** | 电子商务       | 帮助顾客找到心仪的商品。             | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/Hoanganhvu123/ShoppingGPT)                                                                     |
| **物流优化智能体**      | 供应链     | 规划高效配送路线并管理库存。   | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/microsoft/OptiGuide)                                                                           |
| **Vibe Hacking 智能体**                | 网络安全    | 基于多智能体的自动化红队测试服务。   | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/PurpleAILAB/Decepticon) |
| **MediSuite-Ai-Agent**  | 医疗保险  | 一款医疗 AI 智能体，助力自动化医院/保险理赔流程。 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MahmoudRabea13/MediSuite-Ai-Agent)                                         | 
| **Lina-Egyptian-Medical-Chatbot**  | 医疗保险  | （同上） | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MahmoudRabea13/MediSuite-Ai-Agent)                                         |

## 🛠️ 按框架分类的用例

---

### **框架名称：CrewAI**

| 用例                         | 行业/领域                | 描述                                                                                  | GitHub                                                                                                                                              |
| -------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📧 邮件自动回复流程     | 🗣️ 通信        | 根据预设条件自动化邮件回复，提升沟通效率。  | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/email_auto_responder_flow) |
| 📝 会议助手流程        | 🛠️ 生产力         | 协助组织和管理会议，包括日程安排和议程准备。    | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/meeting_assistant_flow) |
| 🔄 自我评估循环流程     | 👥 人力资源      | 促进组织内部的自我评估流程，辅助绩效考核。 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/self_evaluation_loop_flow) |
| 📈 潜在客户评分流程               | 💼 销售                | 评估并打分潜在线索，以优先推进销售策略。             | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/lead-score-flow) |
| 📊 营销策略生成器  | 📢 营销            | 通过分析市场趋势和受众数据来制定营销策略。                  | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/marketing_strategy) |
| 📝 招聘启事生成器         | 🧑‍💼 招聘          | 分析职位需求创建招聘启事，辅助招聘流程。         | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/job-posting) |
| 🔄 招聘工作流          | 🧑‍💼 招聘          | 通过自动化招聘各环节任务来简化招聘流程。          | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/recruitment) |
| 🔍 人岗匹配            | 🧑‍💼 招聘          | 将候选人简历与合适岗位进行匹配，提升招聘效率。      | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/match_profile_to_positions) |
| 📸 Instagram 帖子生成器      | 📱 社交媒体         | 自动生成并排期 Instagram 帖子，简化社媒管理。 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/instagram_post)             |
| 🌐 落地页生成器        | 💻 Web开发      | 自动化网站落地页的创建，辅助前端开发任务。    | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator)     |
| 🎮 游戏构建 Crew             | 🎮 游戏开发     | 通过自动化部分游戏创建环节来辅助游戏开发。          | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/game-builder-crew)          |
| 💹 股票分析工具           | 💰 金融              | 提供股市数据分析工具，辅助财务决策。       | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis)             |
| 🗺️ 行程规划师                  | ✈️ 旅行               | 协助规划行程，整理路线和出行细节。             | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner)               |
| 🎁 惊喜旅行规划师         | ✈️ 旅行               | 根据用户偏好选择目的地和活动，策划惊喜之旅。     | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/surprise_trip)              |
| 📚 使用流程写一本书       | ✍️ 创意写作     | 为作者提供结构化工作流和写作辅助，助力书籍创作。   | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/write_a_book_with_flows) |
| 🎬 剧本作家             | ✍️ 创意写作     | 提供模板和脚本开发指导，辅助剧本创作。       | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/screenplay_writer)          |
| ✅ Markdown 验证器            | 📄 文档        | 验证 Markdown 文件以确保格式规范并符合标准。             | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/markdown_validator)         |
| 🧠 Meta Quest 知识库          | 📚 知识管理 | 管理和组织与 Meta Quest 相关的知识，便于信息检索。   | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/meta_quest_knowledge)       |
| 🤖 NVIDIA 模型集成     | 🤖 AI集成       | 将 NVIDIA AI 模型集成到工作流中，增强计算能力。            | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/nvidia_models) |
| 🗂️ 会前准备            | 🛠️ 生产力         | 协助整理会议材料和设置议程，做好会前准备。               | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/prep-for-a-meeting)         |
| 🛠️ 启动模板               | 🛠️ 开发          | 提供新项目的基础模板，简化环境搭建流程。                | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/starter_template)           |
| 🔗 CrewAI + LangGraph 集成 | 🤖 AI集成       | 演示 CrewAI 与 LangGraph 的集成，实现更强大的工作流自动化。      | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/CrewAI-LangGraph)           |


### **框架名称：Autogen**

> **代码生成、执行与调试**

| 用例                                                                                | 行业/领域                | 描述                                                                       | Notebook                                                                                                                                                                   |
| --------------------------------------------------------------------------------------- | ----------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🤖 自动化任务解决（含代码生成、执行与调试）                   | 💻 软件开发 | 演示通过自动生成、执行和调试代码来自动完成任务。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_auto_feedback_from_code_execution) |
| 🧑‍💻 检索增强智能体的自动化代码生成与问答 | 💻 软件开发 | 使用检索增强方法生成代码并回答问题。           | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat)                      |
| 🧠 基于 Qdrant 的自动化代码生成与问答         | 💻 软件开发 | 利用 Qdrant 增强检索增强智能体的性能。               | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat_qdrant)               |

> **多智能体协作（3个以上 Agent）**

| 用例                                                                 | 行业/领域                    | 描述                                                         | Notebook                                                                                                                                                            |
| :----------------------------------------------------------------------- | :-------------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 🤝 群聊自动化任务解决（3名成员，1名经理）           | 🤝 协作            | 演示通过多智能体协作进行群组任务解决。      | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat)                  |
| 📊 群聊自动化数据可视化（3名成员，1名经理）     | 📊 数据分析            | 利用多智能体协作创建数据可视化图表。       | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_vis)              |
| 🧩 群聊自动化复杂任务解决（6名成员，1名经理）   | 🤝 协作            | 通过更大规模的智能体群组协同解决复杂任务。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_research)         |
| 🧑‍💻 结合编程与规划智能体的自动化任务解决              | 🛠️ 规划与开发 | 融合编程和规划智能体以高效解决问题。  | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_planning.ipynb)             |
| 📐 基于图结构预定义转移路径的自动化任务解决     | 🤝 协作            | 利用图中预定义的转移路径来解决问题。      | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/docs/notebooks/agentchat_groupchat_finite_state_machine) |
| 🧠 通过 SocietyOfMindAgent 运行群聊作为内心独白 | 🧠 认知科学       | 模拟利用群聊进行问题解决的“内心独白”机制。    | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_society_of_mind)            |
| 🔧 使用自定义发言选择函数运行群聊           | 🤝 协作            | 在群聊中实现自定义的发言人选择逻辑。  | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_customized)       |

> **顺序多智能体对话**

| 用例                                                                           | 行业/领域               | 描述                                                                      | Notebook                                                                                                                                                        |
| :--------------------------------------------------------------------------------- | :--------------------- | :------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 🔄 由单一 Agent 发起的顺序对话解决多项任务       | 🔄 工作流自动化 | 通过单个发起 Agent 实现顺序任务的自动化解决。                | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_multi_task_chats)       |
| ⏳ 异步顺序对话解决多项任务（单一 Agent 发起） | 🔄 工作流自动化 | 处理由单个 Agent 发起的序列对话中的异步任务。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_multi_task_async_chats) |
| 🤝 由不同 Agent 发起的顺序对话解决多项任务     | 🔄 工作流自动化 | 通过不同 Agent 依次发起对话来推进顺序任务的解决。  | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchats_sequential_chats)      |

> **嵌套对话**

| 用例                                                                       | 行业/领域                     | 描述                                                                                                          | Notebook                                                                                                                                                         |
| :----------------------------------------------------------------------------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 🧠 使用嵌套对话解决复杂任务                                     | 🧠 问题解决           | 利用嵌套对话结构处理层级化与复杂问题。                                                        | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat)              |
| 🔄 通过嵌套对话序列解决复杂任务                       | 🧠 问题解决           | 演示使用嵌套对话进行顺序任务的解决。                                                             | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_sequential_chats) |
| 🏭 OptiGuide 嵌套对话解决供应链优化问题 | 🏭 供应链优化 | 展示如何使用嵌套对话、代码智能体与防护智能体协同解决供应链优化问题。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat_optiguide)    |
| ♟️ 嵌套对话与工具使用的交互式象棋游戏                       | 🎮 游戏                    | 探索利用嵌套对话结合集成工具进行交互式下棋。                             | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_chats_chess)      |

> **应用**

| 用例                                                                                           | 行业/领域                     | 描述                                                                                       | Notebook                                                                                                                                                      |
| :------------------------------------------------------------------------------------------------- | :--------------------------- | :------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔄 基于新数据的自动化持续学习                                                      | 📊 机器学习          | 从新数据输入中持续学习，实现自适应 AI。                                         | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_stream.ipynb)         |
| 🏭 OptiGuide - 编程、工具调用、安全防护与问答（供应链优化） | 🏭 供应链优化 | 展示结合代码生成、工具使用与安全机制的供应链优化解决方案。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat_optiguide) |
| 🤖 AutoAnny - 基于 Autogen 构建的 Discord 机器人                                                    | 💬 通讯工具       | 展示使用 Autogen 开发 Discord 机器人的完整流程。                | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/tree/main/samples/apps/auto-anny)                 |

> **工具**

| 用例                                                               | 行业/领域                       | 描述                                                                                  | Notebook                                                                                                                                                                         |
| :--------------------------------------------------------------------- | :----------------------------- | :------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🌐 Web 搜索：解决需网络信息的任务                          | 🔍 信息检索       | 通过网络搜索获取完成任务所需的信息。                        | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_web_info.ipynb)                          |
| 🔧 将提供的工具作为函数调用                                     | 🛠️ 工具集成          | 演示如何在 Autogen 中将预置工具作为可调用函数使用。                 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_function_call_currency_calculator)       |
| 🔗 通过同步与异步函数调用使用工具                       | 🛠️ 工具集成          | 演示在 Autogen 工作流中同步和异步调用工具的用法。                | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_function_call_async)                     |
| 🧩 结合 Langchain 工具的任务解决             | 🔍 语言处理         | 在 Autogen 中利用 Langchain 提供的工具进行任务求解。                                   | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_langchain.ipynb)                         |
| 📚 RAG：结合检索增强生成的群聊               | 🤝 协作               | 启用支持检索增强生成（RAG）的群聊，促进信息共享。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_RAG)                           |
| ⚙️ 函数内省：在对话中动态更新/移除函数  | 🔧 开发工具           | 允许 Autogen 智能体在对话过程中动态修改自身功能。            | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_inception_function.ipynb)                |
| 🔊 结合 Whisper 的智能体对话                                             | 🎙️ 音频处理          | 演示 AI 智能体利用 Whisper 进行语音转录和翻译的能力。          | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_video_transcript_translate_with_whisper) |
| 📏 通过 Guidance 约束响应内容                                  | 💡 自然语言处理 | 展示如何使用 Guidance 限制智能体生成的回复范围。                        | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_guidance.ipynb)                          |
| 🌍 使用智能体浏览网页                                          | 🌐 信息检索       | 说明如何配置智能体以浏览和检索网络信息。            | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_surfer.ipynb)                            |
| 📊 SQL：使用 Spider 基准将自然语言转为 SQL 查询      | 💾 数据库管理         | 利用 Spider 基准测试将自然语言输入转换为 SQL 查询。                | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_sql_spider.ipynb)                        |
| 🕸️ 结合 Apify 的网页抓取                                           | 🌐 数据采集              | 演示使用 Autogen 配合 Apify 进行网页数据抓取的技术。                                | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_webscraping_with_apify)                  |
| 🕷️ 网页爬取：使用 Spider API 抓取整个域名                 | 🌐 数据采集              | 说明如何借助 Spider API 实现全站域名爬虫。                                   | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_webcrawling_with_spider)                 |
| 💻 分步编写软件应用（配合专用函数） | 💻 软件开发        | 使用精心设计的函数逐步构建应用程序。                         | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_function_call_code_writing.ipynb)        |

> **人类参与开发**

| 用例                                                         | 行业/领域                | 描述                                                                                       | Notebook                                                                                                                                                      |
| :--------------------------------------------------------------- | :---------------------- | :------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 💬 ChatGPT 风格的简单示例                               | 🧠 对话式 AI    | 演示类似 ChatGPT 的简易交互示例。                             | [![Example](https://img.shields.io/badge/View-Example-blue?logo=openai)](https://github.com/microsoft/autogen/blob/0.2/samples/simple_chat.py)                     |
| 🤖 代码生成、执行、调试与人类反馈集成 | 💻 软件开发 | 展示在流程中融入人类反馈的代码生成、执行与调试能力。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_human_feedback.ipynb) |
| 👥 结合 GPT-4 + 多用户协作的自动化任务解决      | 🤝 协作        | 支持多名人类用户与 GPT-4 协同完成复杂任务。                          | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_two_users.ipynb)      |
| 🔄 支持异步人类输入的智能体对话                            | 🧠 对话式 AI    | 在智能体对话过程中支持非同步的人类反馈与干预。                                     | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/Async_human_input.ipynb)        |

> **智能体教学与学习**

| 用例                                                             | 行业/领域                    | 描述                                                                              | Notebook                                                                                                                                                                |
| :------------------------------------------------------------------- | :-------------------------- | :--------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📘 通过自动化对话教授新技能并复用                | 🎓 教育与培训     | 演示如何向智能体传授新技能，并在自动化对话中实现能力复用。  | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_teaching)                       |
| 🧠 教授智能体新事实、用户偏好与非编程技能 | 🎓 教育与培训     | 展示如何向智能体注入新知识、用户偏好及非代码类技能。            | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_teachability)                   |
| 🤖 通过 GPTAssistantAgent 增强 OpenAI 助手                 | 💻 AI助手开发 | 演示如何利用 GPTAssistantAgent 扩展 OpenAI 助手的底层能力。      | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_teachable_oai_assistants.ipynb) |
| 🔄 Agent Optimizer：以智能体方式训练模型                   | 🛠️ 优化           | 讲解如何使用 Agent Optimizer 高效地以自主化方式训练智能体。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentoptimizer.ipynb)           |

> **结合 OpenAI 助手的循环多智能体对话**

| 用例                                                  | 行业/领域                 | 描述                                                                   | Notebook                                                                                                                                                                     |
| :-------------------------------------------------------- | :----------------------- | :---------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🌟 AutoGen 中调用 OpenAI Assistant 的 Hello-World 示例      | 🤖 对话式 AI     | 使用 AutoGen 与 OpenAI Assistant 进行基础交互的入门示例。              | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_twoagents_basic.ipynb) |
| 🔧 结合函数调用的 OpenAI Assistant 对话         | 🔧 开发工具     | 演示如何在对话中通过函数调用与 OpenAI Assistant 交互。         | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_function_call.ipynb)   |
| 🧠 结合代码解释器的 OpenAI Assistant 对话       | 💻 软件开发  | 演示将 OpenAI Assistant 作为代码解释器嵌入对话流程。      | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_code_interpreter.ipynb)          |
| 🔍 结合检索增强的 OpenAI Assistant 对话 | 📚 信息检索 | 启用支持检索增强技术的 OpenAI Assistant 对话。              | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_retrieval.ipynb)       |
| 🤝 群聊中的 OpenAI Assistant                       | 🤝 协作         | 展示 OpenAI Assistant 如何与其他智能体在群聊中协同工作。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_groupchat.ipynb)       |
| 🛠️ 基于 GPTAssistantAgent 的多智能体工具调用         | 🔧 开发工具     | 讲解如何利用 GPTAssistantAgent 实现多智能体环境下的统一工具调度。             | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/gpt_assistant_agent_function_call.ipynb)       |

> **非 OpenAI 模型**

| 用例                                          | 行业/领域  | 描述                                                       | Notebook                                                                                                                                                              |
| :------------------------------------------------ | :-------- | :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ♟️ 结合非 OpenAI 模型的交互式象棋游戏 | 🎮 游戏 | 探索使用非 OpenAI 模型实现的对话式下棋功能。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_chats_chess_altmodels) |

> **多模态智能体**

| 用例                                       | 行业/领域            | 描述                                                                       | Notebook                                                                                                                                                       |
| :--------------------------------------------- | :------------------ | :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 🎨 结合 DALLE 与 GPT-4V 的多模态对话 | 🖼️ 多媒体 AI  | 融合 DALLE 图像生成与 GPT-4V 视觉理解能力，实现多模态交互。                     | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_dalle_and_gpt4v.ipynb) |
| 🖌️ 结合 Llava 的多模态对话          | 📷 图像处理 | 利用 Llava 模型启用支持图像理解的多模态智能体对话。     | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_lmm_llava.ipynb)       |
| 🖼️ 结合 GPT-4V 的多模态对话         | 🖼️ 多媒体 AI  | 借助 GPT-4V 实现视觉感知与多模态智能体的交互能力。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_lmm_gpt-4v.ipynb)      |

> **长上下文处理**

| 用例                                 | 行业/领域         | 描述                                                                        | Notebook                                                                                                                                                    |
| :--------------------------------------- | :--------------- | :--------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📜 将长上下文处理能力作为核心特性 | 🧠 AI能力 | 演示在 AI 工作流中高效处理超长上下文的实用技术。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_transform_messages) |

> **评估与测试**

| 用例                                                                             | 行业/领域                  | 描述                                                                                  | Notebook                                                                                                                                               |
| :----------------------------------------------------------------------------------- | :------------------------ | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📊 AgentEval：用于评估 LLM 应用效能的多智能体系统 | 📈 性能评估 | 引入 AgentEval 框架，用于全面评估和测试基于大语言模型的应用表现。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agenteval_cq_math.ipynb) |

> **自动化构建智能体**

| 用例                                                      | 行业/领域          | 描述                                                                           | Notebook                                                                                                                                                     |
| :------------------------------------------------------------ | :---------------- | :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🏗️ 使用 AgentBuilder 自动构建多智能体系统 | 🤖 AI开发 | 讲解如何利用 AgentBuilder 工具自动化搭建多智能体架构。  | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/autobuild_basic.ipynb)         |
| 📚 从智能体库自动构建多智能体系统  | 🤖 AI开发 | 展示如何借助预定义的智能体库快速组合并构建多智能体系统。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/autobuild_agent_library.ipynb) |

> **可观测性**

| 用例                                                          | 行业/领域                  | 描述                                                                          | Notebook                                                                                                                                                |
| :---------------------------------------------------------------- | :------------------------ | :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 📊 使用 AgentOps 追踪 LLM 调用、工具使用、动作与错误 | 📈 监控与分析 | 演示如何通过 AgentOps 实时监控 LLM 交互记录、工具调用情况及异常报错。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentops.ipynb) |

> **推理优化**

| 用例                                                               | 行业/领域           | 描述                                                                                | Notebook                                                                                                                                                                     |
| :--------------------------------------------------------------------- | :----------------- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔗 API 统一接口                                                     | 🔧 API管理  | 讲解如何统一管理 API 调用，并提供配套文档与代码示例。                      | [![Documentation](https://img.shields.io/badge/View-Documentation-blue?logo=readthedocs)](https://microsoft.github.io/autogen/docs/Use-Cases/enhanced_inference/#api-unification) |
| ⚙️ 高效管理 API 配置的实用函数 | 🔧 API管理  | 演示用于优化和集中管理 API 配置参数的工具函数。              | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/topics/llm_configuration)                                |
| 💰 成本核算                                                    | 📈 成本管理 | 介绍追踪 Token 消耗量并预估 LLM 交互成本的实用方法。     | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_cost_token_tracking.ipynb)           |
| ⚡ 代码生成专项优化                                        | 📊 优化    | 展示提升 LLM 代码生成质量的高性价比调优技巧。 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/oai_completion.ipynb)                          |
| 📐 数学问题专项优化                                                   | 📊 优化    | 讲解针对数学推理场景的 LLM 性能调优策略。         | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/oai_chatgpt_gpt4.ipynb)                        |

### **框架名称：Agno**

> **用例**

| 用例                           | 行业/领域                                         | 描述                                                                                                                                                                                                                                         | Notebook                                                                                                                                                                                                       |
| :--------------------------------- | :----------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🤖 Agno 支持智能体                   | 💻 软件开发 / AI / 框架支持 | Agno Support Agent 为开发者提供实时解答、原理解释与代码示例，全面辅助 Agno 框架的使用。                                                                                                                    | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/agno_support_agent.py)         |
| 🎥 YouTube 视频分析 Agent                   | 📺 媒体与内容                               | 智能分析 YouTube 视频，自动生成详细摘要、时间戳、主题划分及内容拆解。                                                                                                      | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/youtube_agent.py)              |
| 📊 金融分析 Agent                   | 💼 金融                                       | 高级 AI 市场分析师，提供实时股市洞察、机构研报解读、深度财务分析及行业趋势。支持针对 AAPL、TSLA、NVDA 等标的的深度提示词分析。     | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/thinking_finance_agent.py)     |
| 📚 学习伙伴                   | 🎓 教育                                     | 协助用户查找学习资料、解答疑问并生成个性化复习计划。                                                                                                                                                      | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/study_partner.py)              |
| 🛍️ 购物助手 Agent        | 🏬 电子商务                                    | 商品推荐智能体，根据用户偏好从 Amazon、Flipkart 等可信平台匹配并推荐合适商品。                                                                                                         | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/shopping_partner.py)           |
| 🎓 学术研究智能体          | 🧠 教育 / 科研                          | AI 学术助手，执行高级文献检索、分析最新论文、跨学科综合研究结果，并生成带规范引用的结构化学术报告。                                | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/research_agent_exa.py)         |
| 🧠 新闻调研智能体                  | 🗞️ 媒体与新闻                          | 结合网络搜索与专业写作能力的调研 Agent，执行深度调查并输出类似 NYT 风格的报道。                                                                                                    | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/research_agent.py)             |
| 🍳 菜谱生成器                  | 🍽️ 餐饮与美食                             | AI 食谱推荐智能体，根据食材库存、口味偏好及时间限制提供个性化烹饪方案。                                                                                                               | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/recipe_creator.py)             |
| 🗞️ 金融分析 Agent                 | 💼 金融                                       | 强大的财务分析智能体，整合实时行情、机构观点、公司基本面与市场新闻。适用于苹果、特斯拉、英伟达及半导体/汽车等板块的深度剖析。                 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/finance_agent.py)              |
| 🧠 金融推理智能体       | 📈 金融                                       | 基于 Claude-3.5 Sonnet 的智能体，结合推理工具与 Yahoo Finance 数据对 NVDA 等股票进行深度逻辑分析。                                                                                                                                  | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/reasoning_finance_agent.py)    |
| 🤖 README 生成器 Agent          | 💻 软件开发                                  | 基于仓库元数据自动生成高质量 GitHub README 文档的智能体。                                                                                                                                                                   | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/readme_generator.py)           |
| 🎬 电影推荐智能体      | 🎥 娱乐                                 | 结合 Exa 与 GPT-4o，分析题材、主题与最新评分，提供个性化观影指南。                                                                                                              | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/movie_recommedation.py)        |
| 🔍 媒体趋势分析智能体      | 📰 媒体与新闻                                  | 利用 AI Agent 结合网络爬虫技术，深度挖掘数字平台上的新兴趋势、热点模式及关键意见领袖。                                                                                                                                    | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/media_trend_analysis_agent.py) |
| ⚖️ 法律文档分析智能体 | 🏛️ 法律科技                                  | AI Agent，支持解析 PDF URL 中的法律文书，结合向量知识库与 GPT-4o 提供专业法律见解。                                                                                                   | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/legal_consultant.py)           |
| 🤔 DeepKnowledge                   | 🧠 科研                                      | 该智能体通过迭代检索知识库，将复杂问题拆解为子问题并综合生成全面答案。内置 Agno 文档演示模块，专为深度推理与探索设计。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/deep_knowledge.py)             |
| 📚 书籍推荐智能体       | 🧠 出版与媒体                            | 结合文学数据、读者偏好、书评及发行信息，提供个性化书单的智能助手。                                                                                                                | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/book_recommendation.py)        |
| 🏠 MCP Airbnb 智能体                | 🛎️ 酒店与旅游                                 | 基于 MCP 协议与 Llama 4 构建 AI Agent，支持按工作空间 proximity、交通配套等条件筛选 Airbnb 房源。                                                                                                                               | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/airbnb_mcp.py)                 |
| 🤖 Assist 智能体                   | 🧠 AI框架                                  | 基于 GPT-4o 构建，结合混合搜索与内置知识库，精准解答关于 Agno 框架的技术问题。                                                                                                                                    | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/agno_assist.py)                |

### **框架名称：Langgraph**

> **用例**

| 用例                              | 行业/领域                      | 描述                                                  | Notebook                                                     |
| :------------------------------------ | :---------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 🤖 聊天机器人仿真评估       | 💻 / 💬 AI / 质量保证    | 模拟真实用户交互以评估聊天机器人的鲁棒性与可靠性。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation.ipynb) |
| 🧠 基于提示词的信息收集 | 🧠 AI / 研发 | 演示如何设计 LangGraph 工作流，利用提示工程高效采集信息并管理数据流转。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/chatbots/information-gather-prompting.ipynb) |
| 🧠 代码助手 (LangGraph版)       | 💻 软件开发        | 演示构建具备容错能力的代码助手。涵盖代码生成、错误校验与迭代优化全流程。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/code_assistant/langgraph_code_assistant.ipynb) |
| 🧑‍💼 客服智能体             | 🧑‍💼 客户服务     | 演示构建基于图的客服 Agent，自动处理客户咨询并优化服务体验。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/customer-support/customer-support.ipynb) |
| 🔁 带重试机制的数据提取             | 🧠 AI / 数据抽取        | 演示在 LangGraph 中实现容错与自动重试逻辑，保障数据抽取的稳定性。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/extraction/retries.ipynb) |
| 🧠 多智能体工作流                | 🧠 AI / 流程编排 | 演示使用 Agent Supervisor 构建多智能体系统，实现任务分发与协同通信。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/agent_supervisor.ipynb) |
| 🧠 层级化智能体团队            | 🧠 AI / 流程编排 | 演示构建顶层调度 Agent 与底层专业子 Agent 的层级架构。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/hierarchical_agent_teams.ipynb) |
| 🤝 多智能体协作           | 🧠 AI / 流程编排 | 演示多个专业 Agent 协同完成复杂任务的架构设计。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/multi-agent-collaboration.ipynb) |
| 🧠 规划与执行智能体 (Plan-and-Execute)              | 🧠 AI / 流程编排 | 演示构建先生成多步计划再逐步执行的 Agent，支持动态调整策略。灵感源自 Plan-and-Solve 论文与 Baby-AGI。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb) |
| 🧠 SQL 查询智能体 | 🧠 AI / 数据库交互 | 演示构建可理解并操作 SQL 数据库的 Agent。自动获取表结构、生成查询语句、校验错误并返回结果。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/sql-agent.ipynb) |
| 🧠 反思型智能体 (Reflection Agent) | 🧠 AI / 流程编排 | 演示构建具备自我审查与修正能力的 Agent，提升生成内容的质量。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflection/reflection.ipynb)|
| 🧠 反射型智能体 (Reflexion Agent) | 🧠 AI / 流程编排 | 演示构建能反思自身行为与结果，通过迭代优化提升复杂决策准确率的 Agent。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflexion/reflexion.ipynb)|
| **LangGraph 智能体 RAG**           |                               |                                                              |                                                              |
| 🧠 **自适应 RAG (Adaptive RAG)**           | 🧠 AI / 信息检索 | 演示构建根据查询复杂度动态调整检索策略的 RAG 系统。 | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_adaptive_rag.ipynb) |
| 🧠 **本地自适应 RAG (Adaptive RAG Local)**   | 🧠 AI / 信息检索 | 聚焦于离线环境下的自适应 RAG，适用于数据隐私要求高或网络受限场景。                                           | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_adaptive_rag_local.ipynb) |
| 🤖 **智能体 RAG (Agentic RAG)**            | 🤖 AI / 智能代理    | 学习构建由 Agent 主导检索策略的 RAG，在生成回答前自主判断最佳召回路径。                                                                          | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_agentic_rag.ipynb) |
| 🤖 **本地智能体 RAG (Agentic RAG Local)**    | 🤖 AI / 智能代理    | 将 Agentic RAG 扩展至本地环境，支持使用私有模型与数据源进行离线检索生成。                                                                                                     | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_agentic_rag_local.ipynb) |
| 🧠 **校正型 RAG (CRAG)**  | 🧠 AI / 信息检索 | 实现 CRAG 架构，在将文档送入生成器前进行质量评估与过滤修正。                                                                                            | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_crag.ipynb) |
| 🧠 **本地校正型 RAG (CRAG Local)** | 🧠 AI / 信息检索 | 聚焦于利用本地资源实现离线文档评估与修正的 CRAG 架构。                                                                                                | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_crag_local.ipynb)       |
| 🧠 **自检索 RAG (Self-RAG)**               | 🧠 AI / 信息检索 | 实现 Self-RAG，让系统在生成过程中自我评估并按需追加检索，显著提升回答准确性。                                                              | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_self_rag.ipynb)                       |
| 🧠 **本地自检索 RAG (Self-RAG Local)**       | 🧠 AI / 信息检索 | 演示在本地环境下实现 Self-RAG，支持离线自我反思与数据召回。                                                                                                     | [![AI Agent Code - Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_self_rag_local.ipynb)         |

---

## 🤝 参与贡献

欢迎提交代码！🎉 你可以通过以下方式提供帮助：

1. Fork 本仓库。
2. 添加新的用例或优化现有内容。
3. 提交 Pull Request。

更多细节请查阅我们的 [贡献指南](CONTRIBUTING.md)。

---

## Star 历史统计

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="
      https://api.star-history.com/svg?repos=ashishpatel26/500-AI-Agents-Projects&type=date&legend=top-left
    "
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="
      https://api.star-history.com/svg?repos=ashishpatel26/500-AI-Agents-Projects&type=date&legend=top-left
    "
  />
  <img
    alt="Star History Chart"
    src="https://api.star-history.com/svg?repos=ashishpatel26/500-AI-Agents-Projects&type=date&legend=top-left"
  />
</picture>

---

## 📜 许可证

本仓库采用 MIT License。详见 [LICENSE](LICENSE) 文件获取完整条款。

---

## 🚀 一起构建！

欢迎将此仓库分享给你的社交网络，如果觉得有用请点亮 ⭐ Star。让我们携手打造最全面的 AI 智能体用例资源库！