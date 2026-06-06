# MetaGPT：多智能体框架

<p align="center">
<a href=""><img src="docs/resources/MetaGPT-new-log.png" alt="MetaGPT logo: Enable GPT to work in a software company, collaborating to tackle more complex tasks." width="150px"></a>
</p>

<p align="center">
[ <b>En</b> |
<a href="docs/README_CN.md">中</a> |
<a href="docs/README_FR.md">Fr</a> |
<a href="docs/README_JA.md">日</a> ]
<b>为 GPT 分配不同角色，组建协作实体以应对复杂任务。</b>
</p>

<p align="center">
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
<a href="https://discord.gg/DYn29wFk9z"><img src="https://img.shields.io/badge/Join-Discord-gGnrXvVz7a?logo=discord" alt="Discord Follow"></a>
<a href="https://twitter.com/MetaGPT_"><img src="https://img.shields.io/twitter/follow/MetaGPT?style=social" alt="Twitter Follow"></a>
</p>

<h4 align="center">
    
</h4>

## 更新动态

🚀 2025年3月10日：🎉 [mgx.dev](https://mgx.dev/) 荣登 @ProductHunt 本周最佳产品榜首！🏆

🚀 2025年3月4日：🎉 [mgx.dev](https://mgx.dev/) 荣登 @ProductHunt 今日最佳产品榜首！🏆

🚀 2025年2月19日：今天我们正式推出自然语言编程产品：[MGX (MetaGPT X)](https://mgx.dev/) —— 全球首个 AI Agent 开发团队。更多详情见 [Twitter](https://x.com/MetaGPT_/status/1892199535130329356)。

🚀 2025年2月17日：我们发布了两篇论文：[SPO](https://arxiv.org/pdf/2502.06855) 和 [AOT](https://arxiv.org/pdf/2502.12018)，请查看 [代码](examples)!

🚀 2025年1月22日：我们的论文 [AFlow: Automating Agentic Workflow Generation](https://openreview.net/forum?id=z5uVAKwmjf) 被 ICLR 2025 接收，将以**口头报告（前 1.8%）**形式展示，在基于 LLM 的 Agent 类别中**排名第 2**。

👉👉 [更早的动态](docs/NEWS.md) 

## 软件公司作为多智能体系统

1. MetaGPT 以**一行需求**作为输入，输出**用户故事 / 竞品分析 / 需求文档 / 数据结构 / API 接口 / 项目文档等**。
2. 内部架构上，MetaGPT 包含**产品经理 / 架构师 / 项目经理 / 工程师**等角色。它提供了完整的软件公司工作流程及精心编排的标准作业程序（SOP）。
   1. `Code = SOP(Team)` 是我们的核心理念。我们将 SOP 具象化，并应用于由 LLM 组成的团队中。

![A software company consists of LLM-based roles](docs/resources/software_company_cd.jpeg)

<p align="center">软件公司多智能体示意图（逐步实现中）</p>

## 快速上手

### 安装

> 请确保你的系统已安装 Python 3.9 或更高版本，但低于 3.12。可通过 `python --version` 进行检查。  
> 你也可以使用 conda 进行环境管理：`conda create -n metagpt python=3.9 && conda activate metagpt`

```bash
pip install --upgrade metagpt
# or `pip install --upgrade git+https://github.com/geekan/MetaGPT.git`
# or `git clone https://github.com/geekan/MetaGPT && cd MetaGPT && pip install --upgrade -e .`
```

**正式使用前，请安装 [Node.js](https://nodejs.org/en/download) 和 [pnpm](https://pnpm.io/installation#using-npm)。**

详细安装指南请参考 [CLI 安装](https://docs.deepwisdom.ai/main/en/guide/get_started/installation.html#install-stable-version) 或 [Docker 安装](https://docs.deepwisdom.ai/main/en/guide/get_started/installation.html#install-with-docker)。

### 配置

你可以通过运行以下命令初始化 MetaGPT 的配置，也可以手动创建 `~/.metagpt/config2.yaml` 文件：
```bash
# Check https://docs.deepwisdom.ai/main/en/guide/get_started/configuration.html for more details
metagpt --init-config  # it will create ~/.metagpt/config2.yaml, just modify it to your needs
```

你可以根据 [示例](https://github.com/geekan/MetaGPT/blob/main/config/config2.example.yaml) 和 [文档](https://docs.deepwisdom.ai/main/en/guide/get_started/configuration.html) 配置 `~/.metagpt/config2.yaml`：

```yaml
llm:
  api_type: "openai"  # or azure / ollama / groq etc. Check LLMType for more options
  model: "gpt-4-turbo"  # or gpt-3.5-turbo
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
```

### 使用方式

安装完成后，你可以通过 CLI 使用 MetaGPT：

```bash
metagpt "Create a 2048 game"  # this will create a repo in ./workspace
```

也可以将其作为 Python 库进行调用：

```python
from metagpt.software_company import generate_repo
from metagpt.utils.project_repo import ProjectRepo

repo: ProjectRepo = generate_repo("Create a 2048 game")  # or ProjectRepo("<path>")
print(repo)  # it will print the repo structure with files
```

你也可以使用 [数据解释器（Data Interpreter）](https://github.com/geekan/MetaGPT/tree/main/examples/di) 来编写代码：

```python
import asyncio
from metagpt.roles.di.data_interpreter import DataInterpreter

async def main():
    di = DataInterpreter()
    await di.run("Run data analysis on sklearn Iris dataset, include a plot")

asyncio.run(main())  # or await main() in a jupyter notebook setting
```


### 快速体验与演示视频
- 在 [MetaGPT Huggingface Space](https://huggingface.co/spaces/deepwisdom/MetaGPT-SoftwareCompany) 在线试用
- [Matthew Berman：如何通过一条提示词安装 MetaGPT 并构建初创公司？](https://youtu.be/uT75J_KG_aY)
- [官方演示视频](https://github.com/geekan/MetaGPT/assets/2707039/5e8c1062-8c35-440f-bb20-2b0320f8d27d)

https://github.com/user-attachments/assets/888cb169-78c3-4a42-9d62-9d90ed3928c9

## 教程与文档

- 🗒 [在线文档](https://docs.deepwisdom.ai/main/en/)
- 💻 [使用指南](https://docs.deepwisdom.ai/main/en/guide/get_started/quickstart.html)  
- 🔎 [MetaGPT 能做什么？](https://docs.deepwisdom.ai/main/en/guide/get_started/introduction.html)
- 🛠 如何构建你自己的智能体（Agent）？ 
  - [MetaGPT 使用与开发指南 | Agent 101](https://docs.deepwisdom.ai/main/en/guide/tutorials/agent_101.html)
  - [MetaGPT 使用与开发指南 | Multi-Agent 101](https://docs.deepwisdom.ai/main/en/guide/tutorials/multi_agent_101.html)
- 🧑‍💻 贡献指南
  - [开发路线图](docs/ROADMAP.md)
- 🔖 应用场景 / 用例
  - [数据解释器（Data Interpreter）](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/intro.html)
  - [多智能体辩论（Debate）](https://docs.deepwisdom.ai/main/en/guide/use_cases/multi_agent/debate.html)
  - [研究员（Researcher）](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/researcher.html)
  - [票据助手（Receipt Assistant）](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/receipt_assistant.html)
- ❓ [常见问题解答（FAQs）](https://docs.deepwisdom.ai/main/en/guide/faq.html)

## 支持与反馈

### 加入 Discord 社区

📢 欢迎加入我们的 [Discord 频道](https://discord.gg/ZRHeExS6xv)! 期待与你交流！🎉

### 贡献者登记

📝 [填写表单](https://airtable.com/appInfdG0eJ9J4NNL/pagK3Fh1sGclBvVkV/form) 成为项目贡献者。我们非常期待你的加入！

### 联系方式

如果你对该项目有任何问题或建议，欢迎随时联系我们。非常感谢你的支持！

- **邮箱：** alexanderwu@deepwisdom.ai
- **GitHub Issue：** 如需更多技术交流，也可在我们的 [GitHub 仓库](https://github.com/geekan/metagpt/issues) 中提交新的 issue。

我们将在 2-3 个工作日内回复所有问题。

## 引用

关注 [@MetaGPT_](https://twitter.com/MetaGPT_) 以获取最新研发动态。 

在发表论文引用 [MetaGPT](https://openreview.net/forum?id=VtmBAGCN7o) 时，请使用以下 BibTeX 条目：   

```bibtex
@inproceedings{hong2024metagpt,
      title={Meta{GPT}: Meta Programming for A Multi-Agent Collaborative Framework},
      author={Sirui Hong and Mingchen Zhuge and Jonathan Chen and Xiawu Zheng and Yuheng Cheng and Jinlin Wang and Ceyao Zhang and Zili Wang and Steven Ka Shing Yau and Zijuan Lin and Liyang Zhou and Chenyu Ran and Lingfeng Xiao and Chenglin Wu and J{\"u}rgen Schmidhuber},
      booktitle={The Twelfth International Conference on Learning Representations},
      year={2024},
      url={https://openreview.net/forum?id=VtmBAGCN7o}
}
```

如需了解更多相关工作，请参阅 [学术成果列表](docs/ACADEMIC_WORK.md)。