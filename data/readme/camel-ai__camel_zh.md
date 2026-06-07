<div align="center">
  <a href="https://www.camel-ai.org/">
    <img src="docs/images/banner.png" alt="Banner">
  </a>
</div>

</br>

<div align="center">

[![Documentation][docs-image]][docs-url]
[![Discord][discord-image]][discord-url]
[![X][x-image]][x-url]
[![Reddit][reddit-image]][reddit-url]
[![Wechat][wechat-image]][wechat-url]
[![Hugging Face][huggingface-image]][huggingface-url]
[![Star][star-image]][star-url]
[![Package License][package-license-image]][package-license-url]
[![PyPI Download][package-download-image]][package-download-url]
[![][join-us-image]][join-us]

<a href="https://trendshift.io/repositories/649" target="_blank"><img src="https://trendshift.io/api/badge/repositories/649" alt="camel-ai/camel | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[English](README.md) |
[简体中文](README.zh.md) |
[日本語](README.ja.md)

</div>


<hr>

<div align="center">
<h4 align="center">

[社区](https://github.com/camel-ai/camel#community) |
[安装](https://github.com/camel-ai/camel#installation) |
[示例](https://github.com/camel-ai/camel/tree/HEAD/examples) |
[论文](https://arxiv.org/abs/2303.17760) |
[引用](https://github.com/camel-ai/camel#citation) |
[贡献指南](https://github.com/camel-ai/camel#contributing-to-camel-) |
[CAMEL-AI](https://www.camel-ai.org/)

</h4>

<p style="line-height: 1.5; text-align: center;"> 🐫 CAMEL 是一个开源社区，致力于探索智能体（Agent）的扩展定律。我们相信，大规模研究这些智能体能为理解其行为、能力与潜在风险提供宝贵见解。为便利该领域的研究，我们实现并支持多种类型的智能体、任务、提示词（prompt）、模型及模拟环境。</p>


<br>


加入我们（[*Discord*](https://discord.camel-ai.org/) 或 [*WeChat*](https://ghli.org/camel/wechat.png)），共同拓展智能体扩展定律的研究边界。

🌟 在 GitHub 上为 CAMEL 点星，第一时间获取新版本通知。

</div>

<div align="center">
    <img src="docs/images/stars.gif" alt="Star">
  </a>
</div>

<br>

[![][image-join-us]][join-us]

<details>
<summary><kbd>目录</kbd></summary>

<br/>

- [CAMEL 框架设计原则](#camel-framework-design-principles)
- [为什么选择 CAMEL 进行研究？](#why-use-camel-for-your-research)
- [使用 CAMEL 能构建什么？](#what-can-you-build-with-camel)
  - [数据生成](#1-data-generation)
  - [任务自动化](#2-task-automation)
  - [世界模拟](#3-world-simulation)
- [快速开始](#quick-start)
  - [从 ChatAgent 起步](#starting-with-chatagent)
  - [寻求帮助](#seeking-help)
- [技术栈](#tech-stack)
- [研究项目](#research)
- [合成数据集](#synthetic-datasets)
- [实战指南（用例）](#cookbooks-usecases)
  - [基础概念](#1-basic-concepts)
  - [高级功能](#2-advanced-features)
  - [模型训练与数据生成](#3-model-training--data-generation)
  - [多智能体系统与应用程序](#4-multi-agent-systems--applications)
  - [数据处理](#5-data-processing)
- [真实世界用例](#real-world-usecases)
- [🧱 基于 CAMEL 构建的项目（现实产品与研究）](#-built-with-camel-real-world-producs--research)
  - [研究项目](#research-projects)
  - [产品项目](#product-projects)
- [🗓️ 社区活动](#️-events)
- [贡献代码](#contributing-to-camel)
- [社区与联系](#community--contact)
- [引用文献](#citation)
- [鸣谢](#acknowledgment)
- [许可证](#license)

####

<br/>

</details>


## CAMEL 框架设计原则

<h3>🧬 可演进性（Evolvability）</h3 >

该框架使多智能体系统能够通过生成数据并与环境交互来持续演进。这种演进可通过带有可验证奖励的强化学习或监督学习驱动。

<h3>📈 可扩展性（Scalability）</h3>

框架旨在支持包含数百万个智能体的系统，确保大规模下的高效协调、通信与资源管理。

<h3>💾 状态保持（Statefulness）</h3>

智能体具备状态记忆能力，使其能够与环境进行多步交互，高效应对复杂任务。

<h3>📖 代码即提示词（Code-as-Prompt）</h3>

每一行代码和注释都是给智能体的提示词（prompt）。代码应清晰易读，确保人类与智能体均能有效理解。

<br>

## 为什么选择 CAMEL 进行研究？

我们是一个由社区驱动的研究集体，拥有超过 100 名研究人员致力于推进多智能体系统的前沿研究。全球研究人员基于以下原因选择 CAMEL 开展研究工作：

<table style="width: 100%;">
  <tr>
    <td align="left"></td>
    <td align="left"></td>
    <td align="left"></td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">大规模智能体系统</td>
    <td align="left">模拟多达 100 万个智能体，研究复杂多智能体环境中的涌现行为与扩展定律。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">动态通信</td>
    <td align="left">支持智能体间的实时交互，促进无缝协作以应对复杂任务。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">状态记忆</td>
    <td align="left">赋予智能体保留并利用历史上下文的能力，在长期交互中提升决策水平。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">多基准测试支持</td>
    <td align="left">利用标准化基准严格评估智能体性能，确保可复现性与可靠对比。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">多种智能体类型支持</td>
    <td align="left">兼容各类智能体角色、任务、模型与环境，支持跨学科实验与多样化研究应用。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">数据生成与工具集成</td>
    <td align="left">自动化创建大规模结构化数据集，并无缝集成多种工具，简化合成数据生成与研究流程。</td>
  </tr>
</table>

<br>

## 使用 CAMEL 能构建什么？


### 1. 数据生成

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/datagen/cot_datagen.py">
    <img src="docs/images/cot.png" alt="CoT Data Generation">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/datagen/self_instruct">
    <img src="docs/images/self_instruct.png" alt="Self-Instruct Data Generation">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/datagen/source2synth">
    <img src="docs/images/source2synth.png" alt="Source2Synth Data Generation">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/datagen/self_improving_cot.py">
    <img src="docs/images/self_improving.png" alt="Self-Improving Data Generation">
  </a>
</div>

### 2. 任务自动化

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/societies/role_playing.py">
    <img src="docs/images/role_playing.png" alt="Role Playing">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/societies/workforce">
    <img src="docs/images/workforce.png" alt="Workforce">
  </a>
</div>

<div align="center">
  <a href="https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_rag">
    <img src="docs/images/rag_pipeline.png" alt="RAG Pipeline">
  </a>
</div>


### 3. 世界模拟

<div align="center">
  <a href="https://github.com/camel-ai/oasis">
    <img src="docs/images/oasis_case.png" alt="Oasis Case">
  </a>
</div>

<br>

## 快速开始

得益于 PyPI 上的可用包，安装 CAMEL 非常简单。只需打开终端并运行：

```bash
pip install camel-ai
```

### 从 ChatAgent 起步

本示例演示如何使用 CAMEL 框架创建 `ChatAgent` 并使用 DuckDuckGo 执行搜索查询。

1. **安装工具包：**

  ```bash
  pip install 'camel-ai[web_tools]'
  ```

2. **配置你的 OpenAI API 密钥：**

  ```bash
  export OPENAI_API_KEY='your_openai_api_key'
  ```

   或者，使用 `.env` 文件：

   ```bash
   cp .env.example .env
   # then edit .env and add your keys
   ```

3. **运行以下 Python 代码：**

  ```python
  from camel.models import ModelFactory
  from camel.types import ModelPlatformType, ModelType
  from camel.agents import ChatAgent
  from camel.toolkits import SearchToolkit

  model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O,
    model_config_dict={"temperature": 0.0},
  )

  search_tool = SearchToolkit().search_duckduckgo

  agent = ChatAgent(model=model, tools=[search_tool])

  response_1 = agent.step("What is CAMEL-AI?")
  print(response_1.msgs[0].content)
  # CAMEL-AI is the first LLM (Large Language Model) multi-agent framework
  # and an open-source community focused on finding the scaling laws of agents.
  # ...

  response_2 = agent.step("What is the Github link to CAMEL framework?")
  print(response_2.msgs[0].content)
  # The GitHub link to the CAMEL framework is
  # [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel).
  ```

4. **（可选）启用模型请求/响应日志：**

  ```bash
  export CAMEL_MODEL_LOG_ENABLED=true
  export CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED=true
  export CAMEL_LOG_DIR=camel_logs
  ```

  - `CAMEL_MODEL_LOG_ENABLED`：启用请求/响应的 JSON 日志记录。
  - `CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED`：控制是否在 `request.model_config_dict` 下记录 `model_config_dict`。若未设置，则默认与 `CAMEL_MODEL_LOG_ENABLED` 保持一致。
  - `CAMEL_LOG_DIR`：生成日志文件的目录（默认为 `camel_logs`）。
  - 日志以 UTF-8 格式的 JSON 写入，多语言文本（如中文、日文、阿拉伯文）将保留原样，避免 Unicode 转义噪声。


更多详细安装说明与配置选项，请查阅[安装文档](https://github.com/camel-ai/camel/blob/master/docs/get_started/installation.md)。

运行后，你可以通过 [docs.camel-ai.org](https://docs.camel-ai.org) 探索 CAMEL 技术栈与实战指南（Cookbooks），构建强大的多智能体系统。

我们提供了一个 [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing) 演示，展示两个 ChatGPT 智能体分别扮演 Python 程序员和股票交易员，协作开发股市交易机器人的对话过程。

探索不同类型的智能体、角色及其应用场景。

- **[创建你的第一个智能体](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agent)**
- **[创建你的第一个智能体社会](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agents_society)**
- **[批评家智能体（Critic Agents）](https://docs.camel-ai.org/cookbooks/advanced_features/critic_agents_and_tree_search)**

### 寻求帮助

如果你在配置 CAMEL 时遇到任何问题，请前往 [CAMEL Discord](https://discord.camel-ai.org/) 联系我们。

<br>

## 技术栈

<div align="center">
  <a href="https://docs.camel-ai.org">
    <img src="https://camel-ai.github.io/camel_asset/graphics/techstack.png" alt="TechStack">
  </a>
</div>

### 核心模块
构建、运行和增强 CAMEL-AI 智能体与社会的核心组件及工具。

| 模块 | 描述 |
|:---|:---|
| **[智能体（Agents）](https://docs.camel-ai.org/key_modules/agents)** | 自主运行的核心架构与行为逻辑。 |
| **[智能体社会（Agent Societies）](https://docs.camel-ai.org/key_modules/society)** | 构建与管理多智能体系统及协作的组件。 |
| **[数据生成（Data Generation）](https://docs.camel-ai.org/key_modules/datagen)** | 合成数据创建与增强的工具与方法。 |
| **[模型（Models）](https://docs.camel-ai.org/key_modules/models)** | 用于赋予智能体智能性的模型架构与定制选项。 |
| **[工具（Tools）](https://docs.camel-ai.org/key_modules/tools)** | 集成专用工具以执行特定智能体任务。 |
| **[记忆（Memory）](https://docs.camel-ai.org/key_modules/memory)** | 用于管理智能体状态的记忆存储与检索机制。 |
| **[存储（Storage）](https://docs.camel-ai.org/key_modules/storages)** | 用于持久化保存智能体数据与状态的解决方案。 |
| **[基准测试（Benchmarks）](https://github.com/camel-ai/camel/tree/master/camel/benchmarks)** | 性能评估与测试框架。 |
| **[解释器（Interpreters）](https://docs.camel-ai.org/key_modules/interpreters)** | 代码与命令的解析能力。 |
| **[数据加载器（Data Loaders）](https://docs.camel-ai.org/key_modules/loaders)** | 数据摄入与预处理工具。 |
| **[检索器（Retrievers）](https://docs.camel-ai.org/key_modules/retrievers)** | 知识检索与 RAG 组件。 |
| **[运行时（Runtime）](https://github.com/camel-ai/camel/tree/master/camel/runtime)** | 执行环境与进程管理。 |
| **[人在回路（Human-in-the-Loop）](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_human_in_loop_and_tool_approval)** | 用于人工监督与干预的交互组件。 |
---

## 研究项目

我们相信，大规模研究这些智能体能为理解其行为、能力与潜在风险提供宝贵见解。

**探索我们的研究项目：**

<div align="center">
  <a href="https://github.com/camel-ai/owl">
    <img src="docs/images/owl.png" alt="OWL">
  </a>
</div>

<div align="center">
  <a href="https://oasis.camel-ai.org/">
    <img src="docs/images/oasis.png" alt="OASIS">
  </a>
</div>

<div align="center">
  <a href="https://crab.camel-ai.org/">
    <img src="docs/images/crab.png" alt="CRAB">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/loong">
    <img src="docs/images/loong.png" alt="Loong">
  </a>
</div>

<div align="center">
  <a href="https://agent-trust.camel-ai.org/">
    <img src="docs/images/agent_trust.png" alt="Agent Trust">
  </a>
</div>

<div align="center">
  <a href="https://emos-project.github.io/">
    <img src="docs/images/emos.png" alt="Emos">
  </a>
</div>

>### 与我们共同研究
>
>我们诚挚邀请你使用 CAMEL 开展具有影响力的研究工作。
>
>严谨的研究需要时间与资源投入。作为一个拥有 100+ 名研究人员驱动的开源社区，我们正致力于探索多智能体系统的前沿研究。欢迎加入我们的正在进行的项目，或与我们一起测试新想法，[请通过邮件联系我们](mailto:camel-ai@eigent.ai) 获取更多信息。
>
><div align="center">
>    <img src="docs/images/partners.png" alt="Partners">
></div>

<br>

## 合成数据集

### 1. 支持多种大语言模型（LLM）作为后端

更多详情请参阅我们的 [模型文档](https://docs.camel-ai.org/key_modules/models#)。

> **数据集（托管于 Hugging Face）**

| Dataset        | Chat format                                                                                         | Instruction format                                                                                               | Chat format (translated)                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **AI Society** | [Chat format](https://huggingface.co/datasets/camel-ai/ai_society/blob/main/ai_society_chat.tar.gz) | [Instruction format](https://huggingface.co/datasets/camel-ai/ai_society/blob/main/ai_society_instructions.json) | [Chat format (translated)](https://huggingface.co/datasets/camel-ai/ai_society_translated) |
| **Code**       | [Chat format](https://huggingface.co/datasets/camel-ai/code/blob/main/code_chat.tar.gz)             | [Instruction format](https://huggingface.co/datasets/camel-ai/code/blob/main/code_instructions.json)             | x                                                                                          |
| **Math**       | [Chat format](https://huggingface.co/datasets/camel-ai/math)                                        | x                                                                                                                | x                                                                                          |
| **Physics**    | [Chat format](https://huggingface.co/datasets/camel-ai/physics)                                     | x                                                                                                                | x                                                                                          |
| **Chemistry**  | [Chat format](https://huggingface.co/datasets/camel-ai/chemistry)                                   | x                                                                                                                | x                                                                                          |
| **Biology**    | [Chat format](https://huggingface.co/datasets/camel-ai/biology)                                     | x                                                                                                                | x                                                                                          |

### 2. 指令与任务可视化

| Dataset          | Instructions                                                                                                         | Tasks                                                                                                         |
|------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **AI Society**   | [Instructions](https://atlas.nomic.ai/map/3a559a06-87d0-4476-a879-962656242452/db961915-b254-48e8-8e5c-917f827b74c6) | [Tasks](https://atlas.nomic.ai/map/cb96f41b-a6fd-4fe4-ac40-08e101714483/ae06156c-a572-46e9-8345-ebe18586d02b) |
| **Code**         | [Instructions](https://atlas.nomic.ai/map/902d6ccb-0bbb-4294-83a8-1c7d2dae03c8/ace2e146-e49f-41db-a1f4-25a2c4be2457) | [Tasks](https://atlas.nomic.ai/map/efc38617-9180-490a-8630-43a05b35d22d/2576addf-a133-45d5-89a9-6b067b6652dd) |
| **Misalignment** | [Instructions](https://atlas.nomic.ai/map/5c491035-a26e-4a05-9593-82ffb2c3ab40/2bd98896-894e-4807-9ed8-a203ccb14d5e) | [Tasks](https://atlas.nomic.ai/map/abc357dd-9c04-4913-9541-63e259d7ac1f/825139a4-af66-427c-9d0e-f36b5492ab3f) |

<br>

## 实战指南（用例）
关于在 CAMEL-AI 智能体与社会中实现特定功能的实用指南与教程。

### 1. 基础概念
| Cookbook | Description |
|:---|:---|
| **[创建你的第一个智能体](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agent)** | 构建你第一个智能体的分步指南。 |
| **[创建你的第一个智能体社会](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agents_society)** | 学习如何构建协作型智能体社会。 |
| **[消息处理指南](https://docs.camel-ai.org/cookbooks/basic_concepts/agents_message)** | 智能体消息处理的最佳实践。 |

### 2. 高级功能
| Cookbook | Description |
|:---|:---|
| **[工具集成指南](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_tools)** | 集成工具以增强功能。 |
| **[记忆系统指南](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_memory)** | 在智能体中实现记忆系统。 |
| **[RAG 指南](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_rag)** | 检索增强生成（Retrieval-Augmented Generation）实战配方。 |
| **[Graph RAG 指南](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_graph_rag)** | 结合知识图谱与 RAG 技术。 |
| **[使用 AgentOps 追踪 CAMEL 智能体](https://docs.camel-ai.org/cookbooks/advanced_features/agents_tracking)** | 用于运营中追踪与管理智能体的工具。 |

### 3. 模型训练与数据生成
| Cookbook | Description |
|:---|:---|
| **[使用 CAMEL 进行数据生成并与 Unsloth 微调](https://docs.camel-ai.org/cookbooks/data_generation/sft_data_generation_and_unsloth_finetuning_Qwen2_5_7B)** | 学习如何使用 CAMEL 生成数据，并通过 Unsloth 高效微调模型。 |
| **[真实函数调用与 Hermes 格式的数据生成](https://docs.camel-ai.org/cookbooks/data_generation/data_gen_with_real_function_calls_and_hermes_format)** | 探索使用真实函数调用和 Hermes 格式生成数据的方法。 |
| **[CoT 数据生成并上传至 Huggingface](https://docs.camel-ai.org/cookbooks/data_generation/distill_math_reasoning_data_from_deepseek_r1)** | 了解如何使用 CAMEL 生成思维链（CoT）数据，并无缝上传至 Huggingface。 |
| **[使用 CAMEL 和 Unsloth 进行 CoT 数据生成与 Qwen SFT](https://docs.camel-ai.org/cookbooks/data_generation/cot_data_gen_sft_qwen_unsolth_upload_huggingface)** | 发现如何使用 CAMEL 生成 CoT 数据，结合 Unsloth 对 Qwen 进行 SFT，并无缝上传数据与模型至 Huggingface。 |

### 4. 多智能体系统与应用程序
| Cookbook | Description |
|:---|:---|
| **[角色扮演爬虫用于报告与知识图谱生成](https://docs.camel-ai.org/cookbooks/applications/roleplaying_scraper)** | 创建用于数据爬取和报告的扮演型智能体。 |
| **[使用 Workforce 组建黑客松评审委员会](https://docs.camel-ai.org/cookbooks/multi_agent_society/workforce_judge_committee)** | 构建协作评审的智能体团队。 |
| **[动态知识图谱角色扮演：具备时间感知能力的多智能体系统](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_dkg)** | 使用多智能体系统为金融应用构建动态、具时间感知的知识图谱。该系统处理财报、新闻与研究论文，帮助交易员分析数据、识别关系并挖掘市场洞察。系统还利用多样化且可选的节点去重技术确保数据完整性，并为金融决策优化图结构。 |
| **[使用 Agentic RAG 构建 Discord 客服机器人](https://docs.camel-ai.org/cookbooks/applications/customer_service_Discord_bot_using_SambaNova_with_agentic_RAG)** | 学习如何使用 Agentic RAG 为 Discord 构建健壮的客服机器人。 |
| **[使用本地模型与 Agentic RAG 构建 Discord 客服机器人](https://docs.camel-ai.org/cookbooks/applications/customer_service_Discord_bot_using_local_model_with_agentic_RAG)** | 学习如何使用支持本地部署的 Agentic RAG 为 Discord 构建健壮的客服机器人。 |

### 5. 数据处理
| Cookbook | Description |
|:---|:---|
| **[视频分析](https://docs.camel-ai.org/cookbooks/data_processing/video_analysis)** | 智能体在视频数据分析中的应用技术。 |
| **[使用 Firecrawl 从网站提取数据的三种方式](https://docs.camel-ai.org/cookbooks/data_processing/ingest_data_from_websites_with_Firecrawl)** | 探索使用 Firecrawl 提取和处理网站数据的三种方法。 |
| **[创建可处理 PDF 的智能体](https://docs.camel-ai.org/cookbooks/data_processing/agent_with_chunkr_for_pdf_parsing)** | 学习如何使用 Chunkr 和 Mistral AI 创建能与你本地 PDF 文件交互的 AI 智能体。 |

<br>

## 真实世界用例

展示 CAMEL 多智能体框架如何在基础设施自动化、生产力工作流、检索增强对话、智能文档/视频分析及协作研究中创造真实业务价值的用例。

### 1. 基础设施自动化

| Usecase                                                      | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **[ACI MCP](https://github.com/camel-ai/camel/tree/master/examples/usecases/aci_mcp)** | 展示 CAMEL 多智能体框架如何在基础设施自动化、生产力工作流、检索增强对话、智能文档/视频分析及协作研究中创造真实业务价值。 |
| **[Cloudflare MCP CAMEL](https://github.com/camel-ai/camel/tree/master/examples/usecases/cloudfare_mcp_camel)** | 智能代理动态管理 Cloudflare 资源，实现可扩展且高效的云安全与性能调优。 |

### 2. 生产力与商业工作流

| Usecase                                                      | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **[Airbnb MCP](https://github.com/camel-ai/camel/tree/master/examples/usecases/airbnb_mcp)** | 协调智能体以优化和管理 Airbnb 房源及房东运营。 |
| **[PPTX Toolkit Usecase](https://github.com/camel-ai/camel/tree/master/examples/usecases/pptx_toolkit_usecase)** | 分析 PowerPoint 文档并通过多智能体协作提取结构化洞察。 |

### 3. 检索增强型多智能体对话

| Usecase                                                      | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **[与 GitHub 对话](https://github.com/camel-ai/camel/tree/master/examples/usecases/chat_with_github)** | 通过利用 RAG 工作流的 CAMEL 智能体查询和理解 GitHub 代码库，加速开发者入职和代码导航。 |
| **[与 YouTube 对话](https://github.com/camel-ai/camel/tree/master/examples/usecases/chat_with_youtube)** | 对话式智能体提取并总结视频字幕，实现更快的内容理解与再利用。 |

### 4. 视频与文档智能分析

| Usecase                                                      | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **[YouTube OCR](https://github.com/camel-ai/camel/tree/master/examples/usecases/youtube_ocr)** | 智能体对视频截图执行 OCR，总结视觉内容，支持媒体监控与合规审查。 |
| **[Mistral OCR](https://github.com/camel-ai/camel/tree/master/examples/usecases/mistral_OCR)** | CAMEL 智能体结合 Mistral 使用 OCR 分析文档，减少文档理解工作流中的手动操作。 |

### 5. 研究与协作

| Usecase                                                      | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **[多智能体研究助手](https://github.com/camel-ai/camel/tree/master/examples/usecases/multi_agent_research_assistant)** | 模拟研究团队智能体协作进行文献综述，提升探索性分析与报告的工作效率。 |

<br>

## 🧱 基于 CAMEL 构建的项目（现实产品与研究）
<div align="left">
  <a href="https://www.camel-ai.org/">
    <img src="docs/images/built_with_CAMEL.png" alt="Built with CAMEL" height="40px">
  </a>
</div>

### 研究项目

| Name | Description |
|:---|:---|
| **[ChatDev](https://github.com/OpenBMB/ChatDev/tree/main/camel)** | 用于软件开发的通信智能体 |
| **[Paper2Poster](https://github.com/Paper2Poster/Paper2Poster)** | 从科学论文自动生成多模态海报 |
| **[Paper2Video](https://github.com/showlab/Paper2Video)** | 从科学论文自动生成视频 |

### 产品项目

| Name | Description |
|:---|:---|
| **[Eigent](https://www.eigent.ai/)** | 全球首个多智能体劳动力平台 |


## 🗓️ 社区活动

我们积极参与以下社区活动：

- 🎙️ **社区会议** — 每周与 CAMEL 团队进行的虚拟同步会议
- 🏆 **竞赛** — 由 CAMEL 举办的黑客马拉松、赏金任务与编程挑战
- 🤝 **志愿活动** — 代码贡献、文档编写与导师指导
- 🌍 **大使计划** — 在你的大学或本地技术社群中代表 CAMEL

>想主办或参与 CAMEL 活动？加入我们的 [Discord](https://discord.com/invite/CNcNpquyDc) 或成为 [大使计划](https://www.camel-ai.org/ambassador) 的一员。



## 贡献代码

>对于希望贡献代码的开发者，我们非常感谢你参与我们的开源项目。请在开始协作前查阅我们的[贡献指南](https://github.com/camel-ai/camel/blob/master/CONTRIBUTING.md)。🚀
>
>我们也欢迎你在社交媒体、活动现场或会议上分享 CAMEL，助力社区发展。你的支持至关重要！

## Contributors

<a href="https://github.com/camel-ai/camel/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=camel-ai/camel" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

<br>

## 鸣谢

特别感谢 [Nomic AI](https://home.nomic.ai/) 为我们提供了对其数据集探索工具（Atlas）的扩展访问权限。

同时感谢 Haya Hammoud 为本项目设计了初始 Logo。

我们借鉴了其他优秀研究中的创新思路，供你构建、对比和定制自己的智能体。如果你使用了以下模块，请引用原始文献：
- `TaskCreationAgent` 和 `TaskPrioritizationAgent` 源自 *Nakajima et al.*：[Task-Driven Autonomous Agent](https://yoheinakajima.com/task-driven-autonomous-agent-utilizing-gpt-4-pinecone-and-langchain-for-diverse-applications/)。

- `PersonaHub` 源自 *Tao Ge et al.*：[Scaling Synthetic Data Creation with 1,000,000,000 Personas](https://arxiv.org/pdf/2406.20094)。[[示例](https://github.com/camel-ai/camel/blob/master/examples/personas/personas_generation.py)]

- `Self-Instruct` 源自 *Yizhong Wang et al.*：[SELF-INSTRUCT: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/pdf/2212.10560)。[[示例](https://github.com/camel-ai/camel/blob/master/examples/datagen/self_instruct/self_instruct.py)]

## 许可证

源代码采用 Apache 2.0 许可证。

## 引用文献
```
@inproceedings{li2023camel,
  title={CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society},
  author={Li, Guohao and Hammoud, Hasan Abed Al Kader and Itani, Hani and Khizbullin, Dmitrii and Ghanem, Bernard},
  booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
  year={2023}
}
```

引用示例：
```
We use the CAMEL framework \cite{li2023camel} to develop the agents used in our experiments.
```

## 社区与联系

如需更多信息，请联系 camel-ai@eigent.ai

- **GitHub Issues：** 报告 Bug、提交功能请求并跟踪开发进度。[提交 Issue](https://github.com/camel-ai/camel/issues)

- **Discord：** 获取实时支持、与社区交流并保持最新动态。[加入我们](https://discord.camel-ai.org/)

- **X（Twitter）：** 关注更新、AI 见解及重要公告。[关注我们](https://x.com/CamelAIOrg)

- **大使计划：** 推广 CAMEL-AI，主办活动并贡献内容。[了解更多](https://www.camel-ai.org/community)

- **微信社区：** 扫描下方二维码加入我们的微信社群。

  <div align="center">
    <img src="misc/wechat.jpeg" alt="WeChat QR Code" width="200">
  </div>


<br>

[docs-image]: https://img.shields.io/badge/Documentation-EB3ECC
[docs-url]: https://camel-ai.github.io/camel/index
[star-image]: https://img.shields.io/github/stars/camel-ai/camel?label=stars&logo=github&color=brightgreen
[star-url]: https://github.com/camel-ai/camel/stargazers
[package-license-image]: https://img.shields.io/badge/License-Apache_2.0-blue.svg
[package-license-url]: https://github.com/camel-ai/camel/blob/master/licenses/LICENSE
[package-download-image]: https://img.shields.io/pypi/dm/camel-ai

[colab-url]: https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing
[colab-image]: https://colab.research.google.com/assets/colab-badge.svg
[huggingface-url]: https://huggingface.co/camel-ai
[huggingface-image]: https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-CAMEL--AI-ffc107?color=ffc107&logoColor=white
[discord-url]: https://discord.camel-ai.org/
[discord-image]: https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb
[wechat-url]: https://ghli.org/camel/wechat.png
[wechat-image]: https://img.shields.io/badge/WeChat-CamelAIOrg-brightgreen?logo=wechat&logoColor=white
[x-url]: https://x.com/CamelAIOrg
[x-image]: https://img.shields.io/twitter/follow/CamelAIOrg?style=social
[twitter-image]: https://img.shields.io/twitter/follow/CamelAIOrg?style=social&color=brightgreen&logo=twitter
[reddit-url]: https://www.reddit.com/r/CamelAI/
[reddit-image]: https://img.shields.io/reddit/subreddit-subscribers/CamelAI?style=plastic&logo=reddit&label=r%2FCAMEL&labelColor=white
[ambassador-url]: https://www.camel-ai.org/community
[package-download-url]: https://pypi.org/project/camel-ai
[join-us]:https://eigent-ai.notion.site/eigent-ai-careers
[join-us-image]:https://img.shields.io/badge/Join%20Us-yellow?style=plastic
[image-join-us]: https://camel-ai.github.io/camel_asset/graphics/join_us.png