<p align="center">
    <img src="https://raw.githubusercontent.com/neuml/txtai/master/logo.png"/>
</p>

<p align="center">
    <b>集大成的 AI 框架</b>
</p>

<p align="center">
    <a href="https://github.com/neuml/txtai/releases">
        <img src="https://img.shields.io/github/release/neuml/txtai.svg?style=flat&color=success" alt="Version"/>
    </a>
    <a href="https://github.com/neuml/txtai">
        <img src="https://img.shields.io/github/last-commit/neuml/txtai.svg?style=flat&color=blue" alt="GitHub last commit"/>
    </a>
    <a href="https://github.com/neuml/txtai/issues">
        <img src="https://img.shields.io/github/issues/neuml/txtai.svg?style=flat&color=success" alt="GitHub issues"/>
    </a>
    <a href="https://join.slack.com/t/txtai/shared_invite/zt-37c1zfijp-Y57wMty6YOx_hyIHEQvQJA">
        <img src="https://img.shields.io/badge/slack-join-blue?style=flat&logo=slack&logocolor=white" alt="Join Slack"/>
    </a>
    <a href="https://github.com/neuml/txtai/actions?query=workflow%3Abuild">
        <img src="https://github.com/neuml/txtai/workflows/build/badge.svg" alt="Build Status"/>
    </a>
    <a href="https://coveralls.io/github/neuml/txtai?branch=master">
        <img src="https://img.shields.io/coverallsCoverage/github/neuml/txtai" alt="Coverage Status">
    </a>
</p>

`txtai` 是一个集语义搜索、大语言模型（LLM）编排和语言模型工作流于一体的 AI 框架。

![architecture](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/architecture.png#gh-light-mode-only)
![architecture](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/architecture-dark.png#gh-dark-mode-only)

`txtai` 的核心组件是嵌入数据库（embeddings database），它融合了稀疏与稠密向量索引、图网络以及关系型数据库。

这一基础架构支持向量搜索，并可为大语言模型（LLM）应用提供强大的知识来源。

构建自主智能体、检索增强生成（RAG）流程、多模型工作流等。

`txtai` 功能特性概览：

- 🔎 支持 SQL、对象存储、主题建模、图分析和多模态索引的向量搜索
- 📄 为文本、文档、音频、图像和视频创建嵌入表示
- 💡 由语言模型驱动的流程（Pipeline），支持运行 LLM 提示词、问答、标注、转录、翻译、摘要等任务
- ↪️️ 工作流用于串联流程并聚合业务逻辑。`txtai` 进程可以是简单的微服务，也可以是多模型工作流。
- 🤖 智能体（Agent）能够智能地连接嵌入数据、流程、工作流及其他智能体，自主解决复杂问题
- ⚙️ 提供 Web 和模型上下文协议（Model Context Protocol, MCP）API。支持 [JavaScript](https://github.com/neuml/txtai.js)、[Java](https://github.com/neuml/txtai.java)、[Rust](https://github.com/neuml/txtai.rs) 和 [Go](https://github.com/neuml/txtai.go) 绑定库
- 🔋 开箱即用，内置默认配置助你快速上手
- ☁️ 支持本地运行或通过容器编排进行横向扩展

`txtai` 基于 Python 3.10+、[Hugging Face Transformers](https://github.com/huggingface/transformers)、[Sentence Transformers](https://github.com/UKPLab/sentence-transformers) 和 [FastAPI](https://github.com/tiangolo/fastapi) 构建。本项目遵循 Apache 2.0 开源协议发布。

> [!NOTE]
>
> [NeuML](https://neuml.com) 是 `txtai` 背后的公司，我们围绕自身技术栈提供 AI 咨询服务。[预约会议](https://cal.com/neuml/intro) 或 [发送消息](mailto:info@neuml.com) 了解更多详情。
>
> 我们还正在构建一种简单安全的托管方式，通过 [txtai.cloud](https://txtai.cloud) 运行托管的 `txtai` 应用。

## 为什么选择 txtai？

![why](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/why.png#gh-light-mode-only)
![why](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/why-dark.png#gh-dark-mode-only)

新的向量数据库、LLM 框架及中间的各种工具每天都在涌现。为什么选择使用 `txtai`？

- 🔹 通过 [pip](https://neuml.github.io/txtai/install/) 或 [Docker](https://neuml.github.io/txtai/cloud/) 在几分钟内快速部署运行
```python
# Get started in a couple lines
import txtai

embeddings = txtai.Embeddings()
embeddings.index(["Correct", "Not what we hoped"])
embeddings.search("positive", 1)
#[(0, 0.29862046241760254)]
```
- 🔹 内置 API，便于使用你偏好的编程语言开发应用
```yaml
# app.yml
embeddings:
    path: sentence-transformers/all-MiniLM-L6-v2
```
```bash
CONFIG=app.yml uvicorn "txtai.api:app"
curl -X GET "http://localhost:8000/search?query=positive"
```
- 🔹 支持本地运行——无需将数据发送至分散的远程服务
- 🔹 兼容从微型模型到大型语言模型（LLM）的各类模型
- 🔹 资源占用低——按需安装额外依赖并进行扩展
- 🔹 [通过示例学习](https://neuml.github.io/txtai/examples)——Notebook 涵盖所有可用功能

## 应用场景

以下章节介绍了 `txtai` 的常见应用场景。此外，还提供了一套包含 70 多个 [示例 Notebook 和应用](https://neuml.github.io/txtai/examples) 的综合资源库。

### 语义搜索

构建语义/相似度/向量/神经搜索应用。

![demo](https://raw.githubusercontent.com/neuml/txtai/master/demo.gif)

传统搜索系统依赖关键词查找数据。而语义搜索具备自然语言理解能力，能够识别具有相同含义的结果，而非仅仅匹配相同的关键词。

![search](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/search.png#gh-light-mode-only)
![search](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/search-dark.png#gh-dark-mode-only)

可通过以下示例快速上手：

| Notebook  | Description  |       |
|:----------|:-------------|------:|
| [介绍 txtai](https://github.com/neuml/txtai/blob/master/examples/01_Introducing_txtai.ipynb) [▶️](https://www.youtube.com/watch?v=SIezMnVdmMs) | `txtai` 功能概览 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/01_Introducing_txtai.ipynb) |
| [使用图像进行相似度搜索](https://github.com/neuml/txtai/blob/master/examples/13_Similarity_search_with_images.ipynb) | 将图像和文本嵌入同一空间以实现跨模态检索 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/13_Similarity_search_with_images.ipynb) |
| [构建问答数据库](https://github.com/neuml/txtai/blob/master/examples/34_Build_a_QA_database.ipynb) | 结合语义搜索实现问题匹配 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/34_Build_a_QA_database.ipynb) |
| [语义图谱](https://github.com/neuml/txtai/blob/master/examples/38_Introducing_the_Semantic_Graph.ipynb) | 探索主题、数据关联性及运行网络分析 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/38_Introducing_the_Semantic_Graph.ipynb) |

### LLM 编排

自主智能体、检索增强生成（RAG）、数据对话，以及与大型语言模型（LLM）交互的流程和工作流。

![llm](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/llm.png)

详见下方：

| Notebook  | Description  |       |
|:----------|:-------------|------:|
| [提示词模板与任务链](https://github.com/neuml/txtai/blob/master/examples/44_Prompt_templates_and_task_chains.ipynb) | 构建模型提示词并通过工作流串联任务 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/44_Prompt_templates_and_task_chains.ipynb) |
| [集成 LLM 框架](https://github.com/neuml/txtai/blob/master/examples/53_Integrate_LLM_Frameworks.ipynb) | 整合 llama.cpp、LiteLLM 及自定义生成框架 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/53_Integrate_LLM_Frameworks.ipynb) |
| [使用 LLM 构建知识图谱](https://github.com/neuml/txtai/blob/master/examples/57_Build_knowledge_graphs_with_LLM_driven_entity_extraction.ipynb) | 通过 LLM 驱动的实体抽取技术构建知识图谱 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/57_Build_knowledge_graphs_with_LLM_driven_entity_extraction.ipynb) |
| [用 txtai 解析星空](https://github.com/neuml/txtai/blob/master/examples/72_Parsing_the_stars_with_txtai.ipynb) | 探索已知恒星、行星和星系的宇宙学知识图谱 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/72_Parsing_the_stars_with_txtai.ipynb) |

#### 智能体（Agents）

智能体将嵌入数据、流程、工作流及其他智能体连接起来，自主解决复杂问题。

![agent](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/agent.png)

`txtai` 智能体基于 [smolagents](https://github.com/huggingface/smolagents) 框架构建。它支持 `txtai` 兼容的所有 LLM（通过 Hugging Face、llama.cpp，或通过 LiteLLM 接入 OpenAI / Claude / AWS Bedrock）。同时支持使用 [`agents.md`](https://github.com/agentsmd/agents.md) 和 [`skill.md`](https://agentskills.io/specification) 进行智能体提示词配置。

请查看此[智能体快速入门示例](https://github.com/neuml/txtai/blob/master/examples/agent_quickstart.py)。更多示例如下：

| Notebook  | Description  |       |
|:----------|:-------------|------:|
| [赋予智能体自主权](https://github.com/neuml/txtai/blob/master/examples/69_Granting_autonomy_to_agents.ipynb) | 让智能体根据判断迭代解决问题 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/69_Granting_autonomy_to_agents.ipynb) |
| [TxtAI 获得技能](https://github.com/neuml/txtai/blob/master/examples/83_TxtAI_got_skills.ipynb) | 将 skill.md 文件集成至你的智能体中 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/83_TxtAI_got_skills.ipynb) |
| [智能体工具集](https://github.com/neuml/txtai/blob/master/examples/84_Agent_Tools.ipynb) [▶️](https://www.youtube.com/watch?v=RDNaFXQy3GQ) | 了解 `txtai` 智能体工具箱 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/84_Agent_Tools.ipynb) |
| [使用图谱与智能体分析 LinkedIn 公司帖子](https://github.com/neuml/txtai/blob/master/examples/71_Analyzing_LinkedIn_Company_Posts_with_Graphs_and_Agents.ipynb) | 探索如何利用 AI 提升社交媒体参与度 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/71_Analyzing_LinkedIn_Company_Posts_with_Graphs_and_Agents.ipynb) |

#### 检索增强生成（RAG）

检索增强生成（RAG）通过将知识库作为上下文约束输出，从而降低大语言模型产生幻觉的风险。RAG 常用于实现“与你的数据对话”。

![rag](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/rag.png#gh-light-mode-only)
![rag](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/rag-dark.png#gh-dark-mode-only)

请查看此[RAG 快速入门示例](https://github.com/neuml/txtai/blob/master/examples/rag_quickstart.py)。更多示例如下：

| Notebook  | Description  |       |
|:----------|:-------------|------:|
| [使用 txtai 构建 RAG 流程](https://github.com/neuml/txtai/blob/master/examples/52_Build_RAG_pipelines_with_txtai.ipynb) [▶️](https://www.youtube.com/watch?v=t_OeAc8NVfQ) | RAG 指南，涵盖如何生成引用来源 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/52_Build_RAG_pipelines_with_txtai.ipynb) |
| [RAG 不止于向量搜索](https://github.com/neuml/txtai/blob/master/examples/79_RAG_is_more_than_Vector_Search.ipynb) | 通过网页、SQL 及其他数据源进行上下文检索 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/79_RAG_is_more_than_Vector_Search.ipynb) |
| [结合维基百科与 GPT OSS 的 GraphRAG](https://github.com/neuml/txtai/blob/master/examples/77_GraphRAG_with_Wikipedia_and_GPT_OSS.ipynb) | 基于深度图搜索的 RAG 实现 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/77_GraphRAG_with_Wikipedia_and_GPT_OSS.ipynb) |
| [语音到语音的 RAG](https://github.com/neuml/txtai/blob/master/examples/65_Speech_to_Speech_RAG.ipynb) [▶️](https://www.youtube.com/watch?v=tH8QWwkVMKA) | 结合 RAG 的全流程语音转语音工作流 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/65_Speech_to_Speech_RAG.ipynb) |

### 语言模型工作流

语言模型工作流（亦称语义工作流）将各类语言模型串联起来，以构建智能应用。

![flows](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/flows.png#gh-light-mode-only)
![flows](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/flows-dark.png#gh-dark-mode-only)

尽管大语言模型功能强大，但针对特定任务，许多更小、更专业的模型往往表现更好且速度更快。这包括用于抽取式问答、自动摘要、语音合成（TTS）、转录和翻译的专用模型。

请查看此[工作流快速入门示例](https://github.com/neuml/txtai/blob/master/examples/workflow_quickstart.py)。更多示例如下：

| Notebook  | Description  |       |
|:----------|:-------------|------:|
| [运行流程工作流](https://github.com/neuml/txtai/blob/master/examples/14_Run_pipeline_workflows.ipynb) [▶️](https://www.youtube.com/watch?v=UBMPDCn1gEU) | 简洁而强大的数据处理结构 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/14_Run_pipeline_workflows.ipynb) |
| [构建摘要式文本总结](https://github.com/neuml/txtai/blob/master/examples/09_Building_abstractive_text_summaries.ipynb) | 执行抽象型文本摘要生成 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/09_Building_abstractive_text_summaries.ipynb) |
| [将音频转录为文本](https://github.com/neuml/txtai/blob/master/examples/11_Transcribe_audio_to_text.ipynb) | 把音频文件转换为文字 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/11_Transcribe_audio_to_text.ipynb) |
| [跨语言文本翻译](https://github.com/neuml/txtai/blob/master/examples/12_Translate_text_between_languages.ipynb) | 简化机器翻译与语言检测流程 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/12_Translate_text_between_languages.ipynb) |

## 安装指南

![install](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/install.png#gh-light-mode-only)
![install](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/install-dark.png#gh-dark-mode-only)

最简单的安装方式是通过 pip 和 PyPI：

```
pip install txtai
```

支持 Python 3.10+。建议使用 Python [虚拟环境](https://docs.python.org/3/library/venv.html)。

有关[可选依赖](https://neuml.github.io/txtai/install/#optional-dependencies)、[特定环境前置条件](https://neuml.github.io/txtai/install/#environment-specific-prerequisites)、[从源码安装](https://neuml.github.io/txtai/install/#install-from-source)、[Conda 支持](https://neuml.github.io/txtai/install/#conda)、[轻量级最小化安装](https://neuml.github.io/txtai/install/#minimal-install) 以及如何[使用容器运行](https://neuml.github.io/txtai/cloud) 的详细信息，请参阅详细的[安装说明](https://neuml.github.io/txtai/install)。

## 模型指南

![models](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/models.png)

下表列出了当前推荐的模型。这些模型均支持商业使用，并在速度与性能之间取得了良好平衡。

| Component                                                                     | Model(s)                                                                 |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [嵌入表示](https://neuml.github.io/txtai/embeddings)                        | [all-MiniLM-L6-v2](https://hf.co/sentence-transformers/all-MiniLM-L6-v2) | 
| [图像描述生成](https://neuml.github.io/txtai/pipeline/image/caption)        | [BLIP](https://hf.co/Salesforce/blip-image-captioning-base)              |
| [标签分类 - 零样本](https://neuml.github.io/txtai/pipeline/text/labels)      | [DeBERTa v3 Zeroshot](https://hf.co/MoritzLaurer/deberta-v3-base-zeroshot-v2.0-c) |
| [标签分类 - 固定类别](https://neuml.github.io/txtai/pipeline/text/labels)          | Fine-tune with [training pipeline](https://neuml.github.io/txtai/pipeline/train/trainer)          |
| [大语言模型 (LLM)](https://neuml.github.io/txtai/pipeline/text/llm) | [Gemma 4 31B](https://hf.co/google/gemma-4-31B) |
| [文本摘要](https://neuml.github.io/txtai/pipeline/text/summary)          | [DistilBART](https://hf.co/sshleifer/distilbart-cnn-12-6)                |
| [语音合成 (TTS)](https://neuml.github.io/txtai/pipeline/audio/texttospeech)   | [ESPnet JETS](https://hf.co/NeuML/ljspeech-jets-onnx)                    |
| [音频转录](https://neuml.github.io/txtai/pipeline/audio/transcription)   | [Whisper](https://hf.co/openai/whisper-base)                             | 
| [文本翻译](https://neuml.github.io/txtai/pipeline/text/translation)        | [OPUS Model Series](https://hf.co/Helsinki-NLP)                          |

模型可通过 Hugging Face Hub 的路径或本地目录进行加载。模型路径为可选参数，未指定时将自动加载默认模型。对于无推荐模型的特定任务，`txtai` 将采用 [Hugging Face Tasks](https://hf.co/tasks) 指南中列出的默认模型。

可通过以下链接了解更多：

- [Hugging Face Tasks](https://hf.co/tasks)
- [Hugging Face Model Hub](https://hf.co/models)
- [Embeddings Leaderboard](https://hf.co/spaces/mteb/leaderboard)
- [LLM Leaderboard](https://hf.co/spaces/lmarena-ai/arena-leaderboard)

## 由 txtai 驱动的应用

以下应用由 `txtai` 驱动：

![apps](https://raw.githubusercontent.com/neuml/txtai/master/apps.jpg)

| Application  | Description  |
|:------------ |:-------------|
| [rag](https://github.com/neuml/rag) | 检索增强生成（RAG）应用 |
| [ncoder](https://github.com/neuml/ncoder) | 开源 AI 编程智能体 |
| [paperai](https://github.com/neuml/paperai) | 面向医学与科学论文的 AI 工具 |
| [annotateai](https://github.com/neuml/annotateai) | 利用大语言模型自动标注论文 |

除上述列表外，还有许多基于 `txtai` 构建的[开源项目](https://github.com/neuml/txtai/network/dependents)、已发表的[学术研究](https://scholar.google.com/scholar?q=txtai&hl=en&as_ylo=2022) 以及投入生产环境的闭源商业/专有项目。

## 延伸阅读

![further](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/further.png#gh-light-mode-only)
![further](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/further-ghdark.png#gh-dark-mode-only)

- [介绍 txtai：一款集大成的 AI 框架](https://medium.com/neuml/introducing-txtai-the-all-in-one-ai-framework-0660ecfc39d7)
- [txtai：用于语义搜索与 LLM 工作流的集大成 AI 框架](https://github.com/neuml/papers/blob/master/txtai/txtai.pdf)
- [Hashnode 教程系列](https://neuml.hashnode.dev/series/txtai-tutorial) | [dev.to](https://dev.to/neuml/tutorial-series-on-txtai-ibg)
- [txtai 9.0 更新内容](https://medium.com/neuml/whats-new-in-txtai-9-0-d522bb150afa) | [8.0](https://medium.com/neuml/whats-new-in-txtai-8-0-2d7d0ab4506b) | [7.0](https://medium.com/neuml/whats-new-in-txtai-7-0-855ad6a55440) | [6.0](https://medium.com/neuml/whats-new-in-txtai-6-0-7d93eeedf804) | [5.0](https://medium.com/neuml/whats-new-in-txtai-5-0-e5c75a13b101) | [4.0](https://medium.com/neuml/whats-new-in-txtai-4-0-bbc3a65c3d1c)
- [语义搜索入门](https://medium.com/neuml/getting-started-with-semantic-search-a9fd9d8a48cf) | [工作流](https://medium.com/neuml/getting-started-with-semantic-workflows-2fefda6165d9) | [RAG](https://medium.com/neuml/getting-started-with-rag-9a0cca75f748)
- [大规模运行 txtai](https://medium.com/neuml/running-at-scale-with-txtai-71196cdd99f9)
- [向量搜索与 RAG 全景：基于 txtai 的回顾与分析](https://medium.com/neuml/vector-search-rag-landscape-a-review-with-txtai-a7f37ad0e187)

## 文档

可查阅 `txtai` 的[完整文档](https://neuml.github.io/txtai)，其中包含嵌入表示、流程、工作流和 API 的配置说明，以及涵盖常见问题与故障排除的 FAQ。

## 贡献指南

有意为 `txtai` 贡献代码或文档的朋友，请参阅[此指南](https://github.com/neuml/.github/blob/master/CONTRIBUTING.md)。