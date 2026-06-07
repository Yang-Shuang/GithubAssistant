<h4 align="center">
  <img src="docs/_static/logo.png" alt="RA-Agent logo" style="width:70%; ">
  
  <a href="https://rdagent.azurewebsites.net" target="_blank">🖥️ 在线演示</a> |
  <a href="https://rdagent.azurewebsites.net/factor_loop" target="_blank">🎥 演示视频</a> <a href="https://www.youtube.com/watch?v=JJ4JYO3HscM&list=PLALmKB0_N3_i52fhUmPQiL4jsO354uopR" target="_blank">▶️YouTube</a>   |
  <a href="https://rdagent.readthedocs.io/en/latest/index.html" target="_blank">📖 文档</a> |
  <a href="https://aka.ms/RD-Agent-Tech-Report" target="_blank">📄 技术报告</a> |
  <a href="#-paperwork-list"> 📃 论文 </a>
</h3>


[![CI](https://github.com/microsoft/RD-Agent/actions/workflows/ci.yml/badge.svg)](https://github.com/microsoft/RD-Agent/actions/workflows/ci.yml)
[![CodeQL](https://github.com/microsoft/RD-Agent/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/microsoft/RD-Agent/actions/workflows/github-code-scanning/codeql)
[![Dependabot Updates](https://github.com/microsoft/RD-Agent/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/microsoft/RD-Agent/actions/workflows/dependabot/dependabot-updates)
[![Lint PR Title](https://github.com/microsoft/RD-Agent/actions/workflows/pr.yml/badge.svg)](https://github.com/microsoft/RD-Agent/actions/workflows/pr.yml)
[![Release.yml](https://github.com/microsoft/RD-Agent/actions/workflows/release.yml/badge.svg)](https://github.com/microsoft/RD-Agent/actions/workflows/release.yml)
[![Platform](https://img.shields.io/badge/platform-Linux-blue)](https://pypi.org/project/rdagent/#files)
[![PyPI](https://img.shields.io/pypi/v/rdagent)](https://pypi.org/project/rdagent/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rdagent)](https://pypi.org/project/rdagent/)
[![Release](https://img.shields.io/github/v/release/microsoft/RD-Agent)](https://github.com/microsoft/RD-Agent/releases)
[![GitHub](https://img.shields.io/github/license/microsoft/RD-Agent)](https://github.com/microsoft/RD-Agent/blob/main/LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Chat](https://img.shields.io/badge/chat-discord-blue)](https://discord.gg/ybQ97B6Jjy)
[![Documentation Status](https://readthedocs.org/projects/rdagent/badge/?version=latest)](https://rdagent.readthedocs.io/en/latest/?badge=latest)
[![Readthedocs Preview](https://github.com/microsoft/RD-Agent/actions/workflows/readthedocs-preview.yml/badge.svg)](https://github.com/microsoft/RD-Agent/actions/workflows/readthedocs-preview.yml) <!-- this badge is too long, please place it in the last one to make it pretty --> 
[![arXiv](https://img.shields.io/badge/arXiv-2505.14738-00ff00.svg)](https://arxiv.org/abs/2505.14738)


# 📰 新闻
| 🗞️ 动态        | 📝 说明                 |
| --            | ------      |
| ICML 2026 接收通知 | 我们很高兴地宣布，论文 [FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents](https://arxiv.org/abs/2603.01712) 已被 ICML 2026 接收。FT-Agent 的实现代码位于 [LLM fine-tuning guide](rdagent/app/finetune/llm/README.md)。 |
| ACL 2026 Findings 接收通知 | 我们很高兴地宣布，论文 [Reasoning as Gradient](https://arxiv.org/abs/2603.01692) 已被 ACL 2026 Findings 接收。执行轨迹数据位于 [Gome GPT-5 Traces](https://huggingface.co/datasets/amstrongzyf/Gome-GPT5-Traces)。 |
| Web UI 发布 | 我们发布了新的前端界面，可通过 `rdagent server_ui` 构建和运行，支持实时交互与轨迹查看（目前暂不支持 `data_science` 场景）。 |
| NeurIPS 2025 接收通知 | 我们很高兴地宣布，论文 [R&D-Agent-Quant](https://arxiv.org/abs/2505.15155) 已被 NeurIPS 2025 接收。 | 
| [技术报告发布](#overall-technical-report) | 整体框架说明及 MLE-bench 上的实验结果 | 
| [R&D-Agent-Quant 发布](#deep-application-in-diverse-scenarios) | 将 R&D-Agent 应用于量化交易领域 | 
| MLE-Bench 结果公布 | R&D-Agent 目前在 MLE-bench 上作为表现最佳的[机器学习工程智能体](#-the-best-machine-learning-engineering-agent)。 |
| 支持 LiteLLM 后端 | 我们现已全面支持 **[LiteLLM](https://github.com/BerriAI/litellm)** 作为默认后端，用于集成多个 LLM 提供商。 |
| 通用数据科学智能体 | [Data Science Agent](https://rdagent.readthedocs.io/en/latest/scens/data_science.html) |
| Kaggle 场景发布 | 我们发布了 **[Kaggle Agent](https://rdagent.readthedocs.io/en/latest/scens/data_science.html)**，欢迎体验新功能！                  |
| 官方微信群发布  | 我们创建了官方微信群，欢迎加入！（🗪[二维码](https://github.com/microsoft/RD-Agent/issues/880)） |
| 官方 Discord 频道发布  | 我们在 Discord 上推出了首个聊天频道（🗪[![Chat](https://img.shields.io/badge/chat-discord-blue)](https://discord.gg/ybQ97B6Jjy)）。 |
| 首次发布 | **R&D-Agent** 在 GitHub 正式发布。 |



# 🏆 表现最佳的机器学习工程智能体！

[MLE-bench](https://github.com/openai/mle-bench) 是一个综合基准测试，用于评估 AI 智能体在机器学习工程任务中的性能。该基准利用来自 75 个 Kaggle 竞赛的数据集，为 AI 系统在真实 ML 工程场景中的能力提供了强有力的评估。

R&D-Agent 目前在 MLE-bench 上表现最佳：

| Agent | Low == Lite (%) | Medium (%) | High (%) | All (%) |
|---------|--------|-----------|---------|----------|
| R&D-Agent o3(R)+GPT-4.1(D) | 51.52 ± 6.9 | 19.3 ± 5.5 | 26.67 ± 0 | 30.22 ± 1.5 |
| R&D-Agent o1-preview | 48.18 ± 2.49 | 8.95 ± 2.36 | 18.67 ± 2.98 | 22.4 ± 1.1 |
| AIDE o1-preview | 34.3 ± 2.4 | 8.8 ± 1.1 | 10.0 ± 1.9 | 16.9 ± 1.1 |

**说明：**
- **O3(R)+GPT-4.1(D)**：此版本旨在通过无缝集成研究智能体（Research Agent, o3）与开发智能体（Development Agent, GPT-4.1），降低平均循环时间，并利用成本效益更高的后端 LLM 组合。
- **AIDE o1-preview**：代表 MLE-bench 原始论文中报告的此前最佳公开结果。
- R&D-Agent o1-preview 的平均值和标准差基于 5 个随机种子独立运行；R&D-Agent o3(R)+GPT-4.1(D) 基于 6 个随机种子。
- 根据 MLE-Bench，这 75 场竞赛按复杂度分为三个等级：**Low==Lite**（假设经验丰富的 ML 工程师可在 2 小时内产出合理方案，不含模型训练时间）；**Medium**（耗时 2 至 10 小时）；**High**（耗时超过 10 小时）。

你可以在线查看上述结果的详细运行记录。
- [R&D-Agent o1-preview 详细运行记录](https://aka.ms/RD-Agent_MLE-Bench_O1-preview)
- [R&D-Agent o3(R)+GPT-4.1(D) 详细运行记录](https://aka.ms/RD-Agent_MLE-Bench_O3_GPT41)

在 MLE-bench 上运行 R&D-Agent，请参阅 **[MLE-bench 指南：通过 MLE-bench 运行 ML 工程](https://rdagent.readthedocs.io/en/latest/scens/data_science.html)**。

# 🥇 首个以数据为中心的量化多智能体框架！

面向量化金融的 R&D-Agent（简称 **RD-Agent(Q)**）是首个以数据为中心的多智能体框架，旨在通过协同因子-模型联合优化，实现量化策略的全栈研发自动化。

![image](https://github.com/user-attachments/assets/3198bc10-47ba-4ee0-8a8e-46d5ce44f45d)

在真实股票市场的广泛实验中表明，RD-Agent(Q) 在成本低于 $10 的情况下，其年化收益率（ARR）比基准因子库高出约 2 倍，同时使用的因子数量减少了 70% 以上。它还在更小的资源预算下超越了最先进的深度时间序列模型。其交替的因子-模型优化机制进一步实现了预测精度与策略稳健性之间的优异平衡。

你可以通过[论文](https://arxiv.org/abs/2505.15155)了解更多关于 **RD-Agent(Q)** 的细节，并通过[文档](https://rdagent.readthedocs.io/en/latest/scens/quant_agent_fin.html)进行复现。

# 数据科学智能体预览
查看我们的演示视频，了解正在开发中的数据科学智能体的当前进展：

https://github.com/user-attachments/assets/3eccbecb-34a4-4c81-bce4-d3f8862f7305

# 🌟 简介
<div align="center">
      <img src="docs/_static/scen.png" alt="Our focused scenario" style="width:80%; ">
</div>

R&D-Agent 旨在自动化工业研发流程中最关键且最具价值的环节，我们首先聚焦于数据驱动场景，以简化模型与数据的开发。在方法论上，我们确立了一个包含两个核心组件的框架：'R'（Research）负责提出新想法，'D'（Development）负责将其实现。我们相信，研发过程的自动化演进将带来具有重大工业价值的解决方案。


<!-- Tag Cloud -->
研发是一个高度通用的场景。R&D-Agent 的出现可以成为你的：
- 💰 **自动量化工厂**（[🎥演示视频](https://rdagent.azurewebsites.net/factor_loop)|[▶️YouTube](https://www.youtube.com/watch?v=X4DK2QZKaKY&t=6s)）
- 🤖 **数据挖掘智能体：** 迭代提出数据与模型，并通过从数据中学习知识来加以实现（[🎥演示视频 1](https://rdagent.azurewebsites.net/model_loop)|[▶️YouTube](https://www.youtube.com/watch?v=dm0dWL49Bc0&t=104s)）（[🎥演示视频 2](https://rdagent.azurewebsites.net/dmm)|[▶️YouTube](https://www.youtube.com/watch?v=VIaSTZuoZg4)）。
- 🦾 **研究副驾驶：** 自动阅读研究论文（[🎥演示视频](https://rdagent.azurewebsites.net/report_model)|[▶️YouTube](https://www.youtube.com/watch?v=BiA2SfdKQ7o)）/ 财务报告（[🎥演示视频](https://rdagent.azurewebsites.net/report_factor)|[▶️YouTube](https://www.youtube.com/watch?v=ECLTXVcSx-c)），并实现模型结构或构建数据集。
- 🤖 **Kaggle 智能体：** 自动进行模型调参与特征工程（[🎥演示视频即将发布]()）并将其应用于竞赛中取得更好成绩。
- 🧪 **FT-Agent：** 面向基准驱动的领域自适应的自主 LLM 微调。详见 [LLM fine-tuning guide](rdagent/app/finetune/llm/README.md)。
- ...

你可以点击上述链接查看演示。我们正持续向项目中添加更多方法与场景，以增强你的研发流程并提升生产力。 

此外，你可以在我们的 **[🖥️ 在线演示](https://rdagent.azurewebsites.net/)** 中查看更多示例。

<div align="center">
    <a href="https://rdagent.azurewebsites.net/" target="_blank">
        <img src="docs/_static/demo.png" alt="Watch the demo" width="80%">
    </a>
</div>


# ⚡ 快速开始

### RD-Agent 目前仅支持 Linux。

你可以通过运行以下命令体验上述演示：

### 🐳 Docker 安装。
用户在尝试大多数场景前必须确保已安装 Docker。请参阅[官方 🐳Docker 页面](https://docs.docker.com/engine/install/)获取安装指南。
请确保当前用户无需使用 `sudo` 即可执行 Docker 命令。你可以通过运行 `docker run hello-world` 进行验证。

### 🐍 创建 Conda 环境
- 使用 Python（我们的 CI 已充分测试 3.10 和 3.11）创建新的 conda 环境：
  ```sh
  conda create -n rdagent python=3.10
  ```
- 激活环境：
  ```sh
  conda activate rdagent
  ```

### 🛠️ 安装 R&D-Agent

#### 面向用户
- 你可以直接从 PyPI 安装 R&D-Agent 包：
  ```sh
  pip install rdagent
  ```

#### 面向开发者
- 如果你想尝试最新版本或为 RD-Agent 做出贡献，可以从源码安装并遵循开发环境配置指南：
  ```sh
  git clone https://github.com/microsoft/RD-Agent
  cd RD-Agent
  make dev
  ```

更多细节请参阅[开发环境设置](https://rdagent.readthedocs.io/en/latest/development.html)。

### 💊 健康检查
- rdagent 提供了一项健康检查功能，目前主要检测两项内容：
  - Docker 安装是否成功。
  - [rdagent ui](https://github.com/microsoft/RD-Agent?tab=readme-ov-file#%EF%B8%8F-monitor-the-application-results) 使用的默认端口是否被占用。
  ```sh
  rdagent health_check --no-check-env
  ```


### ⚙️ 配置
- 演示功能需要以下能力支持：
  - ChatCompletion（对话补全）
  - json_mode（JSON 模式输出）
  - embedding query（嵌入查询）

  你可以通过以下方式设置你的聊天模型和嵌入模型：

  > **🔥 注意**：我们现已提供对 **DeepSeek** 模型的实验性支持！你可以使用 DeepSeek 官方 API 进行高性价比和高性能推理。请参阅下方的 DeepSeek 配置示例。

- **使用 LiteLLM（默认）**：我们现已支持将 LiteLLM 作为后端，用于集成多个 LLM 提供商。你可以通过多种方式配置：

  **选项 1：为两个模型统一设置 API Base**

  *配置示例：`OpenAI` 设置 :*

  ```bash
  cat << EOF  > .env
  # Set to any model supported by LiteLLM.
  CHAT_MODEL=gpt-4o 
  EMBEDDING_MODEL=text-embedding-3-small
  # Configure unified API base
  OPENAI_API_BASE=<your_unified_api_base>
  OPENAI_API_KEY=<replace_with_your_openai_api_key>
  ```

  *配置示例：`Azure OpenAI` 设置 :*

  > 使用此配置前，请提前确认你的 `Azure OpenAI API key` 支持 `嵌入模型（embedding models）`。

  ```bash
  cat << EOF  > .env
  EMBEDDING_MODEL=azure/<Model deployment supporting embedding>
  CHAT_MODEL=azure/<your deployment name>
  AZURE_API_KEY=<replace_with_your_openai_api_key>
  AZURE_API_BASE=<your_unified_api_base>
  AZURE_API_VERSION=<azure api version>
  ```

  **选项 2：为聊天和嵌入模型分别设置 API Base**
  ```bash
  cat << EOF  > .env
  # Set to any model supported by LiteLLM.
  # Configure separate API bases for chat and embedding
  
  # CHAT MODEL:
  CHAT_MODEL=gpt-4o 
  OPENAI_API_BASE=<your_chat_api_base>
  OPENAI_API_KEY=<replace_with_your_openai_api_key>

  # EMBEDDING MODEL:
  # TAKE siliconflow as an example, you can use other providers.
  # Note: embedding requires litellm_proxy prefix
  EMBEDDING_MODEL=litellm_proxy/BAAI/bge-large-en-v1.5
  LITELLM_PROXY_API_KEY=<replace_with_your_siliconflow_api_key>
  LITELLM_PROXY_API_BASE=https://api.siliconflow.cn/v1
  ```

  *配置示例：`DeepSeek` 设置 :*

  > 由于许多用户在配置 DeepSeek 时遇到错误，这里提供一个完整可用的 DeepSeek 设置示例：
  ```bash
  cat << EOF  > .env
  # CHAT MODEL: Using DeepSeek Official API
  CHAT_MODEL=deepseek/deepseek-chat 
  DEEPSEEK_API_KEY=<replace_with_your_deepseek_api_key>

  # EMBEDDING MODEL: Using SiliconFlow for embedding since deepseek has no embedding model.
  # Note: embedding requires litellm_proxy prefix
  EMBEDDING_MODEL=litellm_proxy/BAAI/bge-m3
  LITELLM_PROXY_API_KEY=<replace_with_your_siliconflow_api_key>
  LITELLM_PROXY_API_BASE=https://api.siliconflow.cn/v1
  ```

  注意：如果你使用的是会在回复中包含思维过程（如 `\<think>` 标签）的推理模型，你需要设置以下环境变量：
  ```bash
  REASONING_THINK_RM=True
  ```

  如果你仅直接使用 `OpenAI API` 或 `Azure OpenAI`，也可以使用已弃用的后端。有关此弃用设置的更多配置信息，请参阅[文档](https://rdagent.readthedocs.io/en/latest/installation_and_configuration.html)。 



- 如果你的环境配置已完成，请执行以下命令检查配置是否有效。这一步是必要的。

  ```bash
  rdagent health_check
  ```

### 🚀 运行应用

**[🖥️ 在线演示](https://rdagent.azurewebsites.net/)** 由以下命令实现（每项代表一个演示，你可以根据需要选择）：

- 运行 **自动量化交易 & 迭代因子模型联合演化**： [Qlib](http://github.com/microsoft/qlib) 自循环因子与模型提议及实现应用
  ```sh
  rdagent fin_quant
  ```

- 运行 **自动量化交易 & 迭代因子演化**： [Qlib](http://github.com/microsoft/qlib) 自循环因子提议及实现应用
  ```sh
  rdagent fin_factor
  ```

- 运行 **自动量化交易 & 迭代模型演化**：[Qlib](http://github.com/microsoft/qlib) 自循环模型提议及实现应用
  ```sh
  rdagent fin_model
  ```

- 运行 **自动量化交易 & 从财务报告中提取因子**：基于财务报告运行 [Qlib](http://github.com/microsoft/qlib) 的因子提取与实现应用
  ```sh
  # 1. 通常，你可以使用以下命令运行此场景：
  rdagent fin_factor_report --report-folder=<Your financial reports folder path>

  # 2. 具体而言，你需要先准备一些财务报告。你可以参考此具体示例：
  wget https://github.com/SunsetWolf/rdagent_resource/releases/download/reports/all_reports.zip
  unzip all_reports.zip -d git_ignore_folder/reports
  rdagent fin_factor_report --report-folder=git_ignore_folder/reports
  ```

- 运行 **自动模型研发 & 研究副驾驶**：模型提取与实现应用
  ```sh
  # 1. 通常，你可以使用以下命令运行你自己的论文/报告：
  rdagent general_model <Your paper URL>

  # 2. 具体而言，你可以这样做。更多细节及其他论文示例请使用 `rdagent general_model -h` 查看：
  rdagent general_model  "https://arxiv.org/pdf/2210.09789"
  ```

- 运行 **自动医疗预测模型演化**：医疗自循环模型提议及实现应用

  ```bash
  # 通常，你可以使用以下命令运行数据科学程序：
  rdagent data_science --competition <your competition name>

  # 具体而言，你需要创建一个用于存放竞赛文件的文件夹（例如竞赛说明文件、竞赛数据集等），并在环境中配置该文件夹的路径。此外，在下载竞赛说明时需要使用 chromedriver，你可以参考此具体示例操作：

  # 1. 下载数据集并解压到目标文件夹。
  wget https://github.com/SunsetWolf/rdagent_resource/releases/download/ds_data/arf-12-hours-prediction-task.zip
  unzip arf-12-hours-prediction-task.zip -d ./git_ignore_folder/ds_data/

  # 2. 在 `.env` 文件中配置环境变量
  dotenv set DS_LOCAL_DATA_PATH "$(pwd)/git_ignore_folder/ds_data"
  dotenv set DS_CODER_ON_WHOLE_PIPELINE True
  dotenv set DS_IF_USING_MLE_DATA False
  dotenv set DS_SAMPLE_DATA_BY_LLM False
  dotenv set DS_SCEN rdagent.scenarios.data_science.scen.DataScienceScen

  # 3. 运行应用
  rdagent data_science --competition arf-12-hours-prediction-task
  ```

  **注意：** 有关数据集的更多信息，请参阅[文档](https://rdagent.readthedocs.io/en/latest/scens/data_science.html)。

- 运行 **自动 Kaggle 模型调参与特征工程**：自循环模型提议与特征工程实现应用 <br />
  > 以 **tabular-playground-series-dec-2021** 为例。 <br />
  > 1. 在 [Kaggle](https://www.kaggle.com/) 网站注册并登录。 <br />
  > 2. 配置 Kaggle API。 <br />
  > (1) 点击头像（通常在页面右上角）-> `Settings` -> `Create New Token`，将下载名为 `kaggle.json` 的文件。 <br />
  > (2) 将 `kaggle.json` 移动到 `~/.config/kaggle/` 目录下。 <br />
  > (3) 修改 kaggle.json 文件的权限。参考命令：`chmod 600 ~/.config/kaggle/kaggle.json` <br />
  > 3. 加入竞赛：在[竞赛详情页](https://www.kaggle.com/competitions/tabular-playground-series-dec-2021/data)底部点击 `Join the competition` -> `I Understand and Accept`。
  ```bash
  # 通常，你可以使用以下命令运行 Kaggle 竞赛程序：
  rdagent data_science --competition <your competition name>

  # 1. 在 `.env` 文件中配置环境变量
  mkdir -p ./git_ignore_folder/ds_data
  dotenv set DS_LOCAL_DATA_PATH "$(pwd)/git_ignore_folder/ds_data"
  dotenv set DS_CODER_ON_WHOLE_PIPELINE True
  dotenv set DS_IF_USING_MLE_DATA True
  dotenv set DS_SAMPLE_DATA_BY_LLM True
  dotenv set DS_SCEN rdagent.scenarios.data_science.scen.KaggleScen

  # 2. 运行应用
  rdagent data_science --competition tabular-playground-series-dec-2021
  ```

- 运行 **FT-Agent 自主 LLM 微调**：一个 ICML 2026 的 LLM 微调场景，用于基准驱动的数据处理、训练、评估及反馈引导优化。
  ```bash
  # 查看完整设置、基准说明、数据集备注及示例：
  # rdagent/app/finetune/llm/README.md
  # 运行前请配置 FT_TARGET_BENCHMARK 和 FT_BENCHMARK_DESCRIPTION。
  rdagent llm_finetune --base-model Qwen/Qwen2.5-7B-Instruct
  ```

### 🖥️ 监控应用结果
#### Streamlit UI

使用 Streamlit UI 查看运行日志，尤其适用于 `data_science` 场景。

```sh
rdagent ui --port 19899 --log-dir <your log folder like "log/"> --data-science
```

关于 `data_science` 参数：如果你想查看数据科学场景的日志，请将 `data_science` 参数设置为 `True`；否则请设置为 `False`。

#### Web UI

我们还为通过 `server_ui` 启动的 Flask 后端提供了一个独立的 Web 前端（位于 `web/` 目录）。

**注意：** 此 Web UI 与 `rdagent ui` 不同。当前的 Web UI 暂不支持 `data_science` 场景。对于 `data_science` 场景，请继续使用 `rdagent ui --data-science`。

```sh
cd web
npm install
```

要为 Flask 后端构建前端并将静态资源生成到 `server_ui` 使用的默认目录中：

```sh
cd web
npm run build:flask
```

默认情况下，`server_ui` 从 `./git_ignore_folder/static` 提供静态文件。如果你需要不同的位置，请在启动后端前设置环境变量 `UI_STATIC_PATH`。

启动 Flask 后端，并同时提供构建好的前端与实时 API：

```sh
rdagent server_ui --port 19899
```

之后，在浏览器中打开 `http://127.0.0.1:19899`。

#### 通用注意事项

上述示例中使用了端口 `19899`。在启动任一 UI 前，请检查该端口是否已被占用。如果是，请更改为其他可用端口。

你可以通过运行以下命令检查端口占用情况：

```sh
rdagent health_check --no-check-env --no-check-docker
```

# 🏭 场景

我们将 R&D-Agent 应用到了多个具有高价值的工业数据驱动场景中。


## 🎯 目标：面向数据驱动研发的智能体

在本项目中，我们旨在构建一个能够自动化数据驱动研发（Data-Driven R\&D）的智能体，它能够：
+ 📄 阅读真实世界材料（报告、论文等）并**提取**关键公式、感兴趣的 **特征（features）** 和 **模型（models）** 的描述，这些是数据驱动研发的关键组件。
+ 🛠️ **实现** 提取出的公式（例如特征、因子和模型），将其转化为可运行的代码。
   + 鉴于 LLM 一次性实现的局限性，我们为智能体构建了一个演进流程，使其通过从反馈和知识中学习来不断提升性能。
+ 💡 基于当前知识和观察提出**新想法**。

<!-- ![Data-Centric R&D Overview](docs/_static/overview.png) -->

## 📈 场景/演示

在数据驱动场景的两个核心领域（模型实现与数据构建）中，我们的系统旨在扮演两个主要角色：🦾 副驾驶（Copilot）和 🤖 智能体（Agent）。 
- 🦾 副驾驶遵循人类指令以自动化重复性任务。 
- 🤖 智能体具有更高的自主性，会主动提出未来能获得更好结果的新想法。

支持的场景如下表所示：

| 场景/目标 | 模型实现                   | 数据构建                                                                      |
| --              | --                                     | --                                                                                 |
| **💹 金融**      | 🤖 [迭代提议与演化](https://rdagent.azurewebsites.net/model_loop)[▶️YouTube](https://www.youtube.com/watch?v=dm0dWL49Bc0&t=104s) |  🤖 [迭代提议与演化](https://rdagent.azurewebsites.net/factor_loop) [▶️YouTube](https://www.youtube.com/watch?v=X4DK2QZKaKY&t=6s) <br/>   🦾 [自动阅读报告并实现](https://rdagent.azurewebsites.net/report_factor)[▶️YouTube](https://www.youtube.com/watch?v=ECLTXVcSx-c)  |
| **🩺 医疗**      | 🤖 [迭代提议与演化](https://rdagent.azurewebsites.net/dmm)[▶️YouTube](https://www.youtube.com/watch?v=VIaSTZuoZg4) | -                                                                                  |
| **🏭 通用**      | 🦾 [自动阅读论文并实现](https://rdagent.azurewebsites.net/report_model)[▶️YouTube](https://www.youtube.com/watch?v=BiA2SfdKQ7o) <br/> 🤖 自动 Kaggle 模型调参   | 🤖 自动 Kaggle 特征工程 |

- **[路线图](https://rdagent.readthedocs.io/en/latest/scens/data_science.html#roadmap)**：目前，我们正致力于为 Kaggle 场景添加新功能。

不同场景的入口和配置各不相同。请查阅各场景文档中的详细设置教程。

此处展示了 [成功探索案例](https://github.com/SunsetWolf/rdagent_resource/releases/download/demo_traces/demo_traces.zip)（其中 5 个轨迹展示在 **[🖥️ 在线演示](https://rdagent.azurewebsites.net/)**）。你可以下载并使用文档中的[此命令](https://github.com/microsoft/RD-Agent?tab=readme-ov-file#%EF%B8%8F-monitor-the-application-results)查看执行轨迹。

更多场景细节请参阅 **[📖 readthedocs_scen](https://rdagent.readthedocs.io/en/latest/scens/catalog.html)**。

# ⚙️ 框架

<div align="center">
    <img src="docs/_static/Framework-RDAgent.png" alt="Framework-RDAgent" width="85%">
</div>


在数据科学领域自动化研发流程是一个极具价值但尚未被充分探索的工业方向。我们提出了一个旨在推动这一重要研究领域的框架。

该框架内的研究问题可分为三大类：
| 研究领域 | 论文/工作列表 |
|--------------------|-----------------|
| **评估研发能力** | [基准测试](#benchmark) |
| **想法提出：** 探索新想法或优化现有想法 | [研究](#research) |
| **实现想法的能力：** 执行并落地想法 | [开发](#development) |

我们相信，提供高质量解决方案的关键在于演进研发能力。智能体应像人类专家一样学习，持续提升其研发技能。

更多文档请参阅 **[📖 readthedocs](https://rdagent.readthedocs.io/)**。

# 📃 论文/工作列表

## 总体技术报告
- [R&D-Agent: An LLM-Agent Framework Towards Autonomous Data Science](https://arxiv.org/abs/2505.14738)
```BibTeX
@misc{yang2025rdagentllmagentframeworkautonomous,
      title={R&D-Agent: An LLM-Agent Framework Towards Autonomous Data Science}, 
      author={Xu Yang and Xiao Yang and Shikai Fang and Yifei Zhang and Jian Wang and Bowen Xian and Qizheng Li and Jingyuan Li and Minrui Xu and Yuante Li and Haoran Pan and Yuge Zhang and Weiqing Liu and Yelong Shen and Weizhu Chen and Jiang Bian},
      year={2025},
      eprint={2505.14738},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2505.14738}, 
}
```
![image](https://github.com/user-attachments/assets/28b0488d-a546-4fef-8dc5-563ed64a9b4d)

## 📊 基准测试 (Benchmark)
- [Towards Data-Centric Automatic R&D](https://arxiv.org/abs/2404.11276)
```BibTeX
@misc{chen2024datacentric,
    title={Towards Data-Centric Automatic R&D},
    author={Haotian Chen and Xinjie Shen and Zeqi Ye and Wenjun Feng and Haoxue Wang and Xiao Yang and Xu Yang and Weiqing Liu and Jiang Bian},
    year={2024},
    eprint={2404.11276},
    archivePrefix={arXiv},
    primaryClass={cs.AI}
}
```
![image](https://github.com/user-attachments/assets/494f55d3-de9e-4e73-ba3d-a787e8f9e841)

## 🔍 研究 (Research)

在数据挖掘专家的日常研发过程中，他们会提出假设（例如 RNN 等模型结构可以捕捉时间序列数据中的模式），设计实验（例如金融数据包含时间序列，我们可以在该场景中验证此假设），将实验实现为代码（例如 PyTorch 模型结构），然后执行代码获取反馈（例如指标、损失曲线等）。专家从反馈中学习并在下一次迭代中改进。

基于上述原则，我们建立了一个基本方法框架，持续提出假设、进行验证并从真实实践中获取反馈。这是首个支持链接到真实世界验证的科学研究自动化框架。

更多细节请参阅我们的 **[🖥️ 在线演示页面](https://rdagent.azurewebsites.net)**。

## 🛠️ 开发 (Development)

- [Collaborative Evolving Strategy for Automatic Data-Centric Development](https://arxiv.org/abs/2407.18690)
```BibTeX
@misc{yang2024collaborative,
    title={Collaborative Evolving Strategy for Automatic Data-Centric Development},
    author={Xu Yang and Haotian Chen and Wenjun Feng and Haoxue Wang and Zeqi Ye and Xinjie Shen and Xiao Yang and Shizhao Sun and Weiqing Liu and Jiang Bian},
    year={2024},
    eprint={2407.18690},
    archivePrefix={arXiv},
    primaryClass={cs.AI}
}
```
![image](https://github.com/user-attachments/assets/75d9769b-0edd-4caf-9d45-57d1e577054b)

## 多场景深度应用 (Deep Application in Diverse Scenarios)

- [FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents](https://arxiv.org/abs/2603.01712)

```BibTeX
@misc{li2026ftdojo,
  title={FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents},
  author={Qizheng Li and Yifei Zhang and Xiao Yang and Xu Yang and Zhuo Wang and Weiqing Liu and Jiang Bian},
  year={2026},
  eprint={2603.01712},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2603.01712}
}
```

FT-Agent（本文提出的自主 LLM 微调场景）可通过 [LLM fine-tuning guide](rdagent/app/finetune/llm/README.md) 获取。

- [R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)
```BibTeX
@misc{li2025rdagentquantmultiagentframeworkdatacentric,
      title={R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization}, 
      author={Yuante Li and Xu Yang and Xiao Yang and Minrui Xu and Xisen Wang and Weiqing Liu and Jiang Bian},
      year={2025},
      eprint={2505.15155},
      archivePrefix={arXiv},
      primaryClass={q-fin.CP},
      url={https://arxiv.org/abs/2505.15155}, 
}
```
![image](https://github.com/user-attachments/assets/3186f67a-c2f8-4b6b-8bb9-a9b959c13866)

- [Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search](https://arxiv.org/abs/2603.01692)

```BibTeX
@article{zhang2026reasoning,
  title={Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search},
  author={Zhang, Yifei and Yang, Xu and Yang, Xiao and Xian, Bowen and Li, Qizheng and Fang, Shikai and Li, Jingyuan and Wang, Jian and Xu, Mingrui and Liu, Weiqing and others},
  journal={arXiv preprint arXiv:2603.01692},
  year={2026}
}
```

你可以在 [Gome GPT-5 Traces](https://huggingface.co/datasets/amstrongzyf/Gome-GPT5-Traces) 在线查看详细执行轨迹。

# 🤝 贡献指南 (Contributing)

我们欢迎对 R&D-Agent 的贡献与建议。有关如何参与的更多细节，请参阅 [贡献指南](CONTRIBUTING.md)。

在提交 Pull Request 之前，请确保你的代码能通过自动 CI 检查。

## 📝 指导原则
本项目欢迎贡献与建议。
参与本项目的开发既简单又有意义。无论是解决 Issue、修复 Bug、完善文档还是纠正拼写错误，每一份贡献都弥足珍贵并有助于提升 R&D-Agent。

要开始参与，你可以浏览 Issues 列表，或通过运行命令 `grep -r "TODO:"` 在代码库中搜索 `TODO:` 注释。

<img src="https://img.shields.io/github/contributors-anon/microsoft/RD-Agent"/>

<a href="https://github.com/microsoft/RD-Agent/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=microsoft/RD-Agent&max=100&columns=15" />
</a>

在我们将 R&D-Agent 作为开源项目发布到 GitHub 之前，它一直是我们团队内部的内部项目。不幸的是，当我们移除部分机密代码时，内部提交历史未能保留。因此，我们团队成员（包括 Haotian Chen, Wenjun Feng, Haoxue Wang, Zeqi Ye, Xinjie Shen 和 Jinhui Li）的部分贡献未包含在公开提交记录中。

# ⚖️ 法律声明
<p style="line-height: 1; font-style: italic;">RD-agent 按“原样”提供，不提供任何形式的明示或暗示保证，包括但不限于适销性、特定用途适用性及不侵权的保证。RD-agent 旨在促进金融行业的研发流程，并非为任何金融投资或建议而准备的即用型产品。用户应独立评估和测试 RD-agent 在特定使用场景中的风险，确保负责任地使用 AI 技术（包括但不限于开发和整合风险缓解措施），并遵守所有适用司法管辖区的所有适用法律与法规。RD-agent 不提供财务意见，也不代表微软的观点，其设计目的并非取代合格金融专业人士在制定、评估和审批金融产品时的角色。RD-agent 的输入和输出归用户所有，用户在合同、侵权、监管、过失、产品责任或其他任何法律责任理论下，因使用 RD-Agent 及其任何输入/输出而产生的全部责任均由用户自行承担。</p>