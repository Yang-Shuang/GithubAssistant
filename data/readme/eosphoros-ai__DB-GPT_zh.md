# <img src="./assets/LOGO_SMALL.png" alt="Logo" style="vertical-align: middle; height: 24px;" /> DB-GPT：开源智能体 AI 数据助手

<p align="left">
  <img src="./assets/dbgpt_vision.png" width="100%" />
</p>

<div align="center">
  <p>
    <a href="https://github.com/eosphoros-ai/DB-GPT">
        <img alt="stars" src="https://img.shields.io/github/stars/eosphoros-ai/db-gpt?style=social" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT">
        <img alt="forks" src="https://img.shields.io/github/forks/eosphoros-ai/db-gpt?style=social" />
    </a>
    <a href="http://dbgpt.cn/">
      <img alt="Official Website" src="https://img.shields.io/badge/官方%20网站-DB--GPT-blue?style=flat&labelColor=3366CC" />
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img alt="License: MIT" src="https://img.shields.io/github/license/eosphoros-ai/db-gpt?style=flat&labelColor=009966&color=009933" />
    </a>
     <a href="https://github.com/eosphoros-ai/DB-GPT/releases">
      <img alt="Release Notes" src="https://img.shields.io/github/v/release/eosphoros-ai/db-gpt?style=flat&labelColor=FF9933&color=FF6633" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT/issues">
      <img alt="Open Issues" src="https://img.shields.io/github/issues-raw/eosphoros-ai/db-gpt?style=flat&labelColor=666666&color=333333" />
    </a>
    <a href="https://x.com/DBGPT_AI">
      <img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/DBGPT_AI" />
    </a>
    <a href="https://medium.com/@dbgpt0506">
      <img alt="Medium Follow" src="https://badgen.net/badge/Medium/DB-GPT/333333?icon=medium&labelColor=666666" />
    </a>
    <a href="https://space.bilibili.com/3537113070963392">
      <img alt="Bilibili Space" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.bilibili.com%2Fx%2Frelation%2Fstat%3Fvmid%3D3537113070963392&query=data.follower&style=flat&logo=bilibili&logoColor=white&label=Bilibili%20Fans&labelColor=F37697&color=6495ED" />
    </a>
    <a href="https://join.slack.com/t/slack-inu2564/shared_invite/zt-29rcnyw2b-N~ubOD9kFc7b7MDOAM1otA">
      <img alt="Slack" src="https://img.shields.io/badge/Slack-Join%20us-5d6b98?style=flat&logo=slack&labelColor=7d89b0" />
    </a>
    <a href="https://codespaces.new/eosphoros-ai/DB-GPT">
      <img alt="Open in GitHub Codespaces" src="https://github.com/codespaces/badge.svg" />
    </a>
  </p>


[![English](https://img.shields.io/badge/English-d9d9d9?style=flat-square)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-d9d9d9?style=flat-square)](README.zh.md)
[![日本語](https://img.shields.io/badge/日本語-d9d9d9?style=flat-square)](README.ja.md) 

[**文档**](http://docs.dbgpt.cn/docs/overview/) | [**联系我们**](https://github.com/eosphoros-ai/DB-GPT/blob/main/README.zh.md#%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC) | [**社区**](https://github.com/eosphoros-ai/community) | [**论文**](https://arxiv.org/pdf/2312.17449.pdf)

</div>

> **一款开源的 AI 数据助手，可连接你的数据，编写 SQL 和代码，在沙箱环境中运行技能（skills），并将分析转化为报告、洞察与行动。**

![welcome_page](https://github.com/user-attachments/assets/ff9beb32-7db5-487a-bd81-d4489d853ea5)

## 什么是 DB-GPT？

DB-GPT 是一款面向下一代 **AI + 数据**产品的开源**智能体（Agentic）AI 数据助手**。

它帮助用户和团队：
- 连接**数据库、CSV / Excel 文件、数仓与知识库**
- 使用自然语言提问，让 AI **自主编写 SQL**
- 运行基于 Python 和代码的分析工作流
- 加载并执行可复用的领域任务技能（skills）
- 生成图表、仪表盘、HTML 报告与分析摘要
- 在沙箱环境中安全地执行任务

DB-GPT 同时也是一个用于构建 **AI 原生数据智能体、工作流与应用**的平台，支持 Agent、AWEL、RAG 与多模型。

## 为什么选择 DB-GPT？

### 1. 智能体数据分析
规划任务、拆解步骤、调用工具，端到端完成分析工作流。
![csv_data_analysis_demo_en](https://github.com/user-attachments/assets/4921fa40-20f7-4a9c-b908-c0b4e7caa9d6)

### 2. 自主 SQL + 代码执行
生成 SQL 与代码以查询数据、清洗数据集、计算指标并输出结果。
![agentic_write_code](https://github.com/user-attachments/assets/aeebc2b8-6c50-4ebb-96fd-07b860faa044)
![sql_query](https://github.com/user-attachments/assets/da45de20-3768-4f0d-ab20-e939ddf21361)

### 3. 多源数据访问
跨结构化与非结构化数据源工作，包括数据库、电子表格、文档与知识库。

![datasource](./assets/datasources.png)

### 4. 技能驱动的可扩展性
将领域知识、分析方法与执行流程打包为可复用的技能（skills）。





![import_github_skill](https://github.com/user-attachments/assets/39f39c36-a014-4a2e-8e14-b3af3f1d2f1c)

### 5. 沙箱执行
在隔离环境中运行代码与工具，确保分析与操作更安全、更可靠。
![sandbox](https://github.com/user-attachments/assets/bfbd78e0-15e2-42ac-876f-5b91847aadc1)



## 你能用 DB-GPT 做什么

- **分析 CSV / Excel 文件**并生成可视化报告
- **连接数据库**并生成数据画像（Profiling）报告
- 使用自然语言提出业务问题，让 AI **自动编写 SQL**
- 结合代码、图表与叙述性摘要进行**财务报表分析**
- 创建并复用 **SQL 分析技能**与领域工作流
- 在单一智能体工作流中组合**代码、SQL、检索与工具**
- 为你的团队或产品构建下一代 **AI + 数据助手**

## 产品工作流

### 探索数据
在一个工作区中连接文件、数据库和知识库。

### 规划与执行
让 AI 推理任务，编写 SQL 与代码，并逐步执行。

### 使用技能
加载可复用的技能，实现可重复的业务分析流程。

### 生成报告
输出图表、仪表盘、HTML 报告及可直接用于决策的结果。


## 快速入门

只需几分钟即可运行 DB-GPT（macOS & Linux）：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh | bash
```

或直接指定配置与 API Key：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh \
  | OPENAI_API_KEY=sk-xxx bash -s -- --profile openai
```

通过 Moonshot API 使用 Kimi 2.5：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh \
  | MOONSHOT_API_KEY=sk-xxx bash -s -- --profile kimi
```

通过 OpenAI 兼容 API 使用 MiniMax：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh \
  | MINIMAX_API_KEY=sk-xxx bash -s -- --profile minimax
```

已拥有本地 DB-GPT 代码库？可复用现有仓库，无需重新克隆 `~/.dbgpt/DB-GPT`：

```bash
OPENAI_API_KEY=sk-xxx \
  bash scripts/install/install.sh --profile openai --repo-dir "$(pwd)" --yes
```

或使用 Kimi 2.5 复用本地仓库：

```bash
MOONSHOT_API_KEY=sk-xxx \
  bash scripts/install/install.sh --profile kimi --repo-dir "$(pwd)" --yes
```

或使用 MiniMax 复用本地仓库：

```bash
MINIMAX_API_KEY=sk-xxx \
  bash scripts/install/install.sh --profile minimax --repo-dir "$(pwd)" --yes
```

安装完成后，使用生成的配置启动服务：

```bash
cd ~/.dbgpt/DB-GPT && uv run dbgpt start webserver --profile <profile>
```

然后访问 [http://localhost:5670](http://localhost:5670)。

> **想先查看脚本内容？**
> ```bash
> curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh -o install.sh
> less install.sh
> bash install.sh --profile openai
> ```

### 通过 PyPI 安装

从 PyPI 安装 DB-GPT 并一键启动，无需拉取源码。

> **前置条件：** Python **3.10+** 以及 [uv](https://docs.astral.sh/uv/getting-started/installation/)（推荐）或 pip。

**1. 安装**

```bash
# 推荐使用 uv
uv pip install dbgpt-app

# 或使用 pip
pip install dbgpt-app
```

默认安装包含核心框架（CLI、FastAPI、Agent）、OpenAI 兼容 LLM 支持、DashScope / 通义千问支持、RAG 文档解析与 ChromaDB 向量数据库。

**2. 启动**

```bash
dbgpt start
```

首次运行时，交互式安装向导将引导你选择 LLM 提供商并输入 API Key。完成后，Web 服务将自动启动。

**3. 打开 Web UI**

访问 [http://localhost:5670](http://localhost:5670) —— 一切就绪！🎉

### 进阶安装指南

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

如需使用 Docker、本地 GPU 模型（vLLM、llama.cpp）或手动源码部署，请参阅完整文档：

- [**安装指南**](http://docs.dbgpt.cn/docs/installation)
  - [Docker](http://docs.dbgpt.cn/docs/installation/docker)
  - [源码编译](http://docs.dbgpt.cn/docs/installation/sourcecode)
- [**快速上手**](http://docs.dbgpt.cn/docs/quickstart)
- [**应用开发**](http://docs.dbgpt.cn/docs/operation_manual)
  - [开发指南](http://docs.dbgpt.cn/docs/cookbook/app/data_analysis_app_develop)
  - [应用使用](http://docs.dbgpt.cn/docs/application/app_usage)
  - [AWEL 流程使用](http://docs.dbgpt.cn/docs/application/awel_flow_usage)
- [**调试指南**](http://docs.dbgpt.cn/docs/operation_manual/advanced_tutorial/debugging)
- [**高级用法**](http://docs.dbgpt.cn/docs/application/advanced_tutorial/cli)
  - [SMMF](http://docs.dbgpt.cn/docs/application/advanced_tutorial/smmf)
  - [微调（Finetune）](http://docs.dbgpt.cn/docs/application/fine_tuning_manual/dbgpt_hub)
  - [AWEL](http://docs.dbgpt.cn/docs/awel/tutorial)


## 核心能力

### 智能体分析（Agentic Analysis）
- 任务规划
- 逐步执行
- 工具调用
- 迭代推理

### SQL + 代码执行
- 自然语言转 SQL
- 基于 Python 的数据分析与转换
- 指标计算
- 图表生成

### 多源数据访问
- 关系型数据库
- CSV / Excel
- 文档
- 知识库
- 混合数据源工作流

### 技能与智能体（Skills & Agents）
- 可复用技能
- 领域工作流
- 智能体编排
- 自定义执行流程

### 报告与决策支持
- 数据库画像报告
- 财务分析报告
- 可视化图表与仪表盘
- 摘要与业务洞察

### 安全执行
- 沙箱代码执行
- 受控工具调用
- 可复现的输出与产物

#### Text2SQL 微调（Finetune）

  |     LLM     |  支持状态  | 
  |:-----------:|:-----------:|
  |    LLaMA    |      ✅     |
  |   LLaMA-2   |      ✅     | 
  |    BLOOM    |      ✅     | 
  |   BLOOMZ    |      ✅     | 
  |   Falcon    |      ✅     | 
  |  Baichuan   |      ✅     | 
  |  Baichuan2  |      ✅     | 
  |  InternLM   |      ✅     |
  |    Qwen     |      ✅     | 
  |   XVERSE    |      ✅     | 
  |  ChatGLM2   |      ✅     |

[了解更多 Text2SQL 微调信息](https://github.com/eosphoros-ai/DB-GPT-Hub)

### 支持的模型（Supported Models）

<table>
      <thead>
        <tr>
          <th>提供商</th>
          <th>支持状态</th>
          <th>模型</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td align="center" valign="middle">DeepSeek</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1-0528">DeepSeek-R1-0528</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V3-0324">DeepSeek-V3-0324</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1">DeepSeek-R1</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V3">DeepSeek-V3</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B">DeepSeek-R1-Distill-Llama-70B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B">DeepSeek-R1-Distill-Qwen-32B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct">DeepSeek-Coder-V2-Instruct</a><br/>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Qwen</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen3-235B-A22B">Qwen3-235B-A22B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen3-30B-A3B">Qwen3-30B-A3B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen3-32B">Qwen3-32B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/QwQ-32B">QwQ-32B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct">Qwen2.5-Coder-32B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct">Qwen2.5-Coder-14B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-72B-Instruct">Qwen2.5-72B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-32B-Instruct">Qwen2.5-32B-Instruct</a><br/>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">GLM</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/THUDM/GLM-Z1-32B-0414">GLM-Z1-32B-0414</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/THUDM/GLM-4-32B-0414">GLM-4-32B-0414</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/THUDM/glm-4-9b-chat">Glm-4-9b-chat</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Llama</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct">Meta-Llama-3.1-405B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct">Meta-Llama-3.1-70B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct">Meta-Llama-3.1-8B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct">Meta-Llama-3-70B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct">Meta-Llama-3-8B-Instruct</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Gemma</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-2-27b-it">gemma-2-27b-it</a><br>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-2-9b-it">gemma-2-9b-it</a><br>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-7b-it">gemma-7b-it</a><br>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-2b-it">gemma-2b-it</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Yi</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-1.5-34B-Chat">Yi-1.5-34B-Chat</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-1.5-9B-Chat">Yi-1.5-9B-Chat</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-1.5-6B-Chat">Yi-1.5-6B-Chat</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-34B-Chat">Yi-34B-Chat</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Starling</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/Nexusflow/Starling-LM-7B-beta">Starling-LM-7B-beta</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">SOLAR</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0">SOLAR-10.7B</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Mixtral</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1">Mixtral-8x7B</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Phi</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3">Phi-3</a>
          </td>
        </tr>
      </tbody>
    </table>

  - [更多支持的 LLM](http://docs.dbgpt.site/docs/modules/smmf)

### 隐私与安全（Privacy and Security）

我们通过私有模型部署、代理脱敏与沙箱执行机制，全面保障数据隐私与执行安全。

### 数据源（Data Sources）
- [数据源配置文档](http://docs.dbgpt.cn/docs/modules/connections)

## 愿景（Vision）

我们相信数据产品的未来不止于仪表盘。

下一代 **AI + 数据**产品将具备以下特征：
- **智能体驱动（Agentic）**
- **多源融合（Multi-source）**
- **技能化扩展（Skill-driven）**
- **沙箱隔离执行（Sandboxed）**
- 能够编写 **SQL 与代码**
- 将分析直接转化为**报告、决策与行动**

DB-GPT 致力于帮助开发者与企业构建这一未来。


## 参与贡献

- 如需查看详细的贡献指南，请参考 [如何参与贡献](https://github.com/eosphoros-ai/DB-GPT/blob/main/CONTRIBUTING.md)

### 贡献者墙
<a href="https://github.com/eosphoros-ai/DB-GPT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=eosphoros-ai/DB-GPT&max=200" />
</a>


## 许可证（Licence）
MIT License (MIT)

## 免责声明（DISCKAIMER）
- [免责声明详情](./DISCKAIMER.md)

## 引用（Citation）
如果你想了解 DB-GPT 的整体架构，请引用 <a href="https://arxiv.org/abs/2312.17449" target="_blank">论文</a> 与 <a href="https://arxiv.org/abs/2404.10209" target="_blank">论文</a>

如果你想了解如何使用 DB-GPT 进行 Agent 开发，请引用 <a href="https://arxiv.org/abs/2412.13520" target="_blank">论文</a>
```bibtex
@article{xue2023dbgpt,
      title={DB-GPT: Empowering Database Interactions with Private Large Language Models}, 
      author={Siqiao Xue and Caigao Jiang and Wenhui Shi and Fangyin Cheng and Keting Chen and Hongjun Yang and Zhiping Zhang and Jianshan He and Hongyang Zhang and Ganglin Wei and Wang Zhao and Fan Zhou and Danrui Qi and Hong Yi and Shaodong Liu and Faqiang Chen},
      year={2023},
      journal={arXiv preprint arXiv:2312.17449},
      url={https://arxiv.org/abs/2312.17449}
}
@misc{huang2024romasrolebasedmultiagentdatabase,
      title={ROMAS: A Role-Based Multi-Agent System for Database monitoring and Planning}, 
      author={Yi Huang and Fangyin Cheng and Fan Zhou and Jiahui Li and Jian Gong and Hongjun Yang and Zhidong Fan and Caigao Jiang and Siqiao Xue and Faqiang Chen},
      year={2024},
      eprint={2412.13520},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2412.13520}, 
}
@inproceedings{xue2024demonstration,
      title={Demonstration of DB-GPT: Next Generation Data Interaction System Empowered by Large Language Models}, 
      author={Siqiao Xue and Danrui Qi and Caigao Jiang and Wenhui Shi and Fangyin Cheng and Keting Chen and Hongjun Yang and Zhiping Zhang and Jianshan He and Hongyang Zhang and Ganglin Wei and Wang Zhao and Fan Zhou and Hong Yi and Shaodong Liu and Hongjun Yang and Faqiang Chen},
      year={2024},
      booktitle = "Proceedings of the VLDB Endowment",
      url={https://arxiv.org/abs/2404.10209}
}
```


## 联系方式（Contact Information）
感谢所有为 DB-GPT 做出贡献的人！你的想法、代码、评论，以及在活动或社交平台上的分享，都能让 DB-GPT 变得更好。
我们正在建设社区，如果你有任何关于社区建设的建议，欢迎随时联系我们。  

- [Github Issues](https://github.com/eosphoros-ai/DB-GPT/issues) ⭐️：如需了解使用 GB-DPT 的常见问题，请参阅 CONTRIBUTING.md。  
- [Github Discussions](https://github.com/orgs/eosphoros-ai/discussions) ⭐️：分享你的使用经验或独特应用。  
- [Twitter](https://x.com/DBGPT_AI) ⭐️：欢迎随时与我们交流。  


[![Star History Chart](https://api.star-history.com/svg?repos=csunny/DB-GPT&type=Date)](https://star-history.com/#csunny/DB-GPT)