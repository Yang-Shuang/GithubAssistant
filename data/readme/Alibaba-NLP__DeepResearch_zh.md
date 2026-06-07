<div align="center">
  <picture>
      <img src="./assets/logo.png" width="100%">
  </picture>
</div>

<hr>

<div align="center" style="line-height: 1;">

[![MODELS](https://img.shields.io/badge/Models-5EDDD2?style=for-the-badge&logo=huggingface&logoColor=ffffff&labelColor)](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B)
[![GITHUB](https://img.shields.io/badge/Github-24292F?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Alibaba-NLP/DeepResearch)
[![Blog](https://img.shields.io/badge/Blog-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/)
[![Paper](https://img.shields.io/badge/Paper-red?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/pdf/2510.24701)

</div>
<p align="center">
<p align="center">
🤗 <a href="https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B" target="_blank">HuggingFace</a> ｜
<img src="./assets/tongyi.png" width="14px" style="display:inline;"> <a href="https://modelscope.cn/models/iic/Tongyi-DeepResearch-30B-A3B" target="_blank">ModelScope</a> | 💬 <a href="./assets/wechat_new.jpg">WeChat(微信)</a> | 📰 <a href="https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/">Blog</a> | 📑 <a href="https://arxiv.org/pdf/2510.24701">Paper</a>

<p align="center">
<a href="https://trendshift.io/repositories/14895" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14895" alt="Alibaba-NLP%2FDeepResearch | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

👏 欢迎通过我们的 **[<img src="./assets/tongyi.png" width="14px" style="display:inline;"> Modelscope 在线演示](https://www.modelscope.cn/studios/jialongwu/Tongyi-DeepResearch)**、**[🤗 Huggingface 在线演示](https://huggingface.co/spaces/Alibaba-NLP/Tongyi-DeepResearch)** 或 <img src="./WebAgent/assets/aliyun.png" width="14px" style="display:inline;"> **[百炼服务](https://bailian.console.aliyun.com/?spm=a2ty02.31808181.d_app-market.1.6c4974a1tFmoFc&tab=app#/app/app-market/deep-search/)** 体验 Tongyi DeepResearch！

> [!NOTE]
> 该演示仅用于快速探索。由于模型延迟和工具 QPS 限制，响应时间可能会有所波动或偶尔失败。如需稳定体验，建议本地部署；如需生产级服务，请访问 <img src="./WebAgent/assets/aliyun.png" width="14px" style="display:inline;"> [百炼](https://bailian.console.aliyun.com/?spm=a2ty02.31808181.d_app-market.1.6c4974a1tFmoFc&tab=app#/app/app-market/deep-search/) 并按指引完成配置。

# Introduction (简介)

我们推出 <img src="./assets/tongyi.png" width="14px" style="display:inline;"> **Tongyi DeepResearch**，这是一款智能体大语言模型（Agentic LLM），总参数量为 305 亿，每次推理仅激活 33 亿参数。该模型由通义实验室研发，专为**长视野、深度信息检索**任务设计。Tongyi DeepResearch 在多项智能体搜索基准测试中展现出领先性能，包括 Humanity's Last Exam、BrowseComp、BrowseComp-ZH、WebWalkerQA、xbench-DeepSearch、FRAMES 和 SimpleQA。

> Tongyi DeepResearch 基于我们此前在 <img src="./assets/tongyi.png" width="14px" style="display:inline;"> [WebAgent](./WebAgent/) 项目上的研究成果构建。

更多详情请参阅我们的 📰&nbsp;<a href="https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/">技术博客</a>。

<p align="center">
  <img width="100%" src="./assets/performance.png">
</p>

## Features (核心特性)

- ⚙️ **全自动合成数据生成流水线**：我们设计了一套高度可扩展的数据合成流水线，实现完全自动化，赋能智能体预训练、监督微调（SFT）和强化学习。
- 🔄 **基于智能体数据的大规模持续预训练**：利用多样化的高质量智能体交互数据扩展模型能力，保持知识时效性，并增强推理性能。
- 🔁 **端到端强化学习**：我们采用严格遵循在线策略（On-Policy RL）的强化学习方法，基于定制的 Group Relative Policy Optimization 框架，结合 token 级策略梯度、留一法优势估计以及负样本选择性过滤，以稳定非平稳环境下的训练过程。
- 🤖 **智能体推理范式兼容**：在推理阶段，Tongyi DeepResearch 支持两种推理范式：ReAct（用于严谨评估模型核心内在能力）和基于 IterResearch 的“Heavy”模式（采用测试时扩展策略以释放模型最大性能上限）。

# Model Download (模型下载)

你可通过以下链接直接下载模型。

|            Model            |                                                                           Download Links                                                                           | Model Size | Context Length |
| :-------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------: | :------------: |
| Tongyi-DeepResearch-30B-A3B | [🤗 HuggingFace](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B)<br> [🤖 ModelScope](https://modelscope.cn/models/iic/Tongyi-DeepResearch-30B-A3B) |  30B-A3B   |      128K      |

# News (最新动态)

[2025/09/20]🚀 Tongyi-DeepResearch-30B-A3B 现已上线 [OpenRouter](https://openrouter.ai/alibaba/tongyi-deepresearch-30b-a3b)！请查阅[快速入门指南](https://github.com/Alibaba-NLP/DeepResearch?tab=readme-ov-file#6-you-can-use-openrouters-api-to-call-our-model)。

[2025/09/17]🔥 我们已发布 **Tongyi-DeepResearch-30B-A3B**。

# Deep Research Benchmark Results (深度研究基准测试结果)
<p align="center">
  <img width="100%" src="./assets/benchmark.png">
</p>

## Quick Start (快速入门)

本指南将介绍如何配置环境并运行位于 `[inference](./inference/)` 文件夹中的推理脚本。

### 1. Environment Setup (环境配置)
- 推荐 Python 版本：**3.10.0**（使用其他版本可能导致依赖问题）。
- 强烈建议使用 `conda` 或 `virtualenv` 创建隔离环境。

```bash
# Example with Conda
conda create -n react_infer_env python=3.10.0
conda activate react_infer_env
```

### 2. Installation (安装依赖)

安装所需依赖项：
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration and Prepare Evaluation Data (环境配置与准备评估数据)

#### Environment Configuration (环境配置)

通过复制示例环境变量文件来配置你的 API Key 和设置：

```bash
# Copy the example environment file
cp .env.example .env
```

编辑 `.env` 文件，填入你实际的 API Key 和配置值：

- **SERPER_KEY_ID**：前往 [Serper.dev](https://serper.dev/) 获取密钥，用于网页搜索和 Google Scholar
- **JINA_API_KEYS**：前往 [Jina.ai](https://jina.ai/) 获取密钥，用于网页阅读/解析
- **API_KEY/API_BASE**：来自 [OpenAI](https://platform.openai.com/) 的兼容 OpenAI 接口，用于页面摘要生成
- **DASHSCOPE_API_KEY**：前往 [Dashscope](https://dashscope.aliyun.com/) 获取密钥，用于文件解析
- **SANDBOX_FUSION_ENDPOINT**：Python 解释器沙箱端点地址（详见 [SandboxFusion](https://github.com/bytedance/SandboxFusion)）
- **MODEL_PATH**：模型权重路径
- **DATASET**：评估数据集名称/路径
- **OUTPUT_PATH**：结果保存目录

> **注意**：`.env` 文件已加入 `.gitignore`，因此你的密钥不会被提交到仓库中。

#### Prepare Evaluation Data (准备评估数据)

系统支持两种输入文件格式：**JSON** 和 **JSONL**。

**支持的格式说明：**

**选项 1：JSONL 格式（推荐）**
- 创建扩展名为 `.jsonl` 的数据文件（例如 `my_questions.jsonl`）
- 每一行必须是包含 `question` 和 `answer` 键的有效 JSON 对象：
  ```json
  {"question": "What is the capital of France?", "answer": "Paris"}
  {"question": "Explain quantum computing", "answer": ""}
  ```

**选项 2：JSON 格式**
- 创建扩展名为 `.json` 的数据文件（例如 `my_questions.json`）
- 文件必须包含一个对象数组，每个对象均具有 `question` 和 `answer` 键：
  ```json
  [
    { "question": "What is the capital of France?", "answer": "Paris" },
    { "question": "Explain quantum computing", "answer": "" }
  ]
  ```

**重要提示：** `answer` 字段包含用于评估的**真实答案/参考标准**。系统会针对问题生成自己的回答，这些参考答案将在基准测试期间用于自动评判生成回答的质量。

#### File References for Document Processing (文档处理中的文件引用说明)：

- 若使用 `_file_parser_`（文件解析）工具，请**在 `question` 字段前添加文件名**
- 将引用的文件放置在 `eval_data/file_corpus/` 目录下
- 示例：`{"question": "(Uploaded 1 file: ['report.pdf'])\n\nWhat are the key findings?", "answer": "..."}`

#### File Organization (目录结构)：
```
project_root/
├── eval_data/
│   ├── my_questions.jsonl          # Your evaluation data
│   └── file_corpus/                # Referenced documents
│       ├── report.pdf
│       └── data.xlsx
```

### 4. Configure the Inference Script (配置推理脚本)

- 打开 `run_react_infer.sh`，并根据注释提示修改以下变量：
  - `MODEL_PATH` - 本地或远程模型权重路径。
  - `DATASET` - 评估文件的完整路径，例如 `eval_data/my_questions.jsonl` 或 `/path/to/my_questions.json`。
  - `OUTPUT_PATH` - 保存预测结果的路径，例如 `./outputs`。
- 根据你启用的工具（检索、计算器、网页搜索等），提供所需的 `API_KEY`、`BASE_URL` 或其他凭证。每个密钥在 Bash 脚本中均有行内说明。

### 5. Run the Inference Script (运行推理脚本)

```bash
bash run_react_infer.sh
```
---

完成上述步骤后，你即可完全准备好环境、配置数据集并运行模型。如需更多详情，请查阅各脚本中的行内注释或提交 Issue。

### 6. You can use OpenRouter's API to call our model (使用 OpenRouter API 调用我们的模型)

Tongyi-DeepResearch-30B-A3B 现已在 [OpenRouter](https://openrouter.ai/alibaba/tongyi-deepresearch-30b-a3b) 上线。你无需任何 GPU 即可运行推理。

你需要修改文件 `[inference/react_agent.py](https://github.com/Alibaba-NLP/DeepResearch/blob/main/inference/react_agent.py)` 中的以下内容：

- 在 `call_server` 函数中：将 API Key 和 URL 设置为你 OpenRouter 账号的对应值。
- 将模型名称更改为 `alibaba/tongyi-deepresearch-30b-a3b`。
- 按照第 **88–90** 行注释中的说明调整内容拼接方式。

## Benchmark Evaluation (基准评估)

我们为多种数据集提供了基准评估脚本。更多详情请参阅 [evaluation scripts](./evaluation/) 目录。

## FAQ (常见问题)

更多详情请参阅 [FAQ](./FAQ.md)。

## Deep Research Agent Family (深度研究智能体家族)

<p align="center">
  <img width="100%" src="./assets/family17.png">
</p>

Tongyi DeepResearch 还拥有庞大的深度研究智能体家族。你可在以下论文中找到更多信息：

[1] [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/pdf/2501.07572) (ACL 2025)<br>
[2] [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/pdf/2505.22648) (NeurIPS 2025)<br>
[3] [WebSailor: Navigating Super-human Reasoning for Web Agent](https://arxiv.org/pdf/2507.02592)<br>
[4] [WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization](https://arxiv.org/pdf/2507.15061)<br>
[5] [WebWatcher: Breaking New Frontier of Vision-Language Deep Research Agent](https://arxiv.org/pdf/2508.05748)<br>
[6] [WebResearcher: Unleashing unbounded reasoning capability in Long-Horizon Agents](https://arxiv.org/pdf/2509.13309)<br>
[7] [ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/pdf/2509.13313)<br>
[8] [WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research](https://arxiv.org/pdf/2509.13312)<br>
[9] [WebSailor-V2: Bridging the Chasm to Proprietary Agents via Synthetic Data and Scalable Reinforcement Learning](https://arxiv.org/pdf/2509.13305)<br>
[10] [Scaling Agents via Continual Pre-training](https://arxiv.org/pdf/2509.13310)<br>
[11] [Towards General Agentic Intelligence via Environment Scaling](https://arxiv.org/pdf/2509.13311)<br>
[12] [AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/pdf/2510.24699)<br>
[13] [WebLeaper: Empowering Efficient, Info-Rich Seeking for Web Agents](https://arxiv.org/pdf/2510.24697)<br>
[14] [BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents](https://arxiv.org/pdf/2510.23458)<br>
[15] [Repurposing Synthetic Data for Fine-grained Search Agent Supervision](https://arxiv.org/pdf/2510.24694)<br>
[16] [ParallelMuse: Agentic Parallel Thinking for Deep Information Seeking](https://arxiv.org/pdf/2510.24698)<br>
[17] [AgentFrontier: Expanding the Capability Frontier of LLM Agents with ZPD-Guided Data Synthesis](https://arxiv.org/pdf/2510.24695)<br>
[18] [Nested Browser-Use Learning for Agentic Information Seeking](https://arxiv.org/pdf/2512.23647)<br>

## 🌟 Misc (其他信息)

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Alibaba-NLP/DeepResearch&type=Date)](https://www.star-history.com/#Alibaba-NLP/DeepResearch&Date)

</div>

## 🚩 Talent Recruitment (人才招聘)

🔥🔥🔥 我们正在招聘！研究实习生岗位开放（工作地点：杭州、北京、上海）

📚 **研究方向**：网页智能体、搜索智能体、Agent RL、多智能体强化学习、Agentic RAG

☎️ **联系方式**：[yongjiang.jy@alibaba-inc.com]()

## Contact Information (联系信息)

如有任何交流事宜，请联系 Yong Jiang（yongjiang.jy@alibaba-inc.com）。

## Citation (引用)

```bibtex
@article{tongyidr,
  title={Tongyi DeepResearch Technical Report},
  author={Team, Tongyi DeepResearch and Li, Baixuan and Zhang, Bo and Zhang, Dingchu and Huang, Fei and Li, Guangyu and Chen, Guoxin and Yin, Huifeng and Wu, Jialong and Zhou, Jingren and others},
  journal={arXiv preprint arXiv:2510.24701},
  year={2025}
}
```