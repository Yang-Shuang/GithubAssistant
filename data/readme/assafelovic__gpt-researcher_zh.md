<div align="center" id="top">

<img src="https://github.com/assafelovic/gpt-researcher/assets/13554167/20af8286-b386-44a5-9a83-3be1365139c3" alt="Logo" width="80">

####

[![Website](https://img.shields.io/badge/Official%20Website-gptr.dev-teal?style=for-the-badge&logo=world&logoColor=white&color=0891b2)](https://gptr.dev)
[![Documentation](https://img.shields.io/badge/Documentation-DOCS-f472b6?logo=googledocs&logoColor=white&style=for-the-badge)](https://docs.gptr.dev)
[![Discord](https://img.shields.io/discord/1127851779011391548?logo=discord&logoColor=white&label=Discord&color=34b76a&style=for-the-badge)](https://discord.gg/QgZXvJAccX)


[![PyPI version](https://img.shields.io/pypi/v/gpt-researcher?logo=pypi&logoColor=white&style=flat)](https://badge.fury.io/py/gpt-researcher)
![GitHub Release](https://img.shields.io/github/v/release/assafelovic/gpt-researcher?style=flat&logo=github)
[![Open In Colab](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=grey&color=yellow&label=%20&style=flat&logoSize=40)](https://colab.research.google.com/github/assafelovic/gpt-researcher/blob/master/docs/docs/examples/pip-run.ipynb)
[![Docker Image Version](https://img.shields.io/docker/v/elestio/gpt-researcher/latest?arch=amd64&style=flat&logo=docker&logoColor=white&color=1D63ED)](https://hub.docker.com/r/gptresearcher/gpt-researcher)
[![Skill](https://img.shields.io/badge/Claude%20Skill-skills.sh-blueviolet?style=flat&logo=anthropic&logoColor=white)](https://skills.sh/assafelovic/gpt-researcher/gpt-researcher)
[![Twitter Follow](https://img.shields.io/twitter/follow/assaf_elovic?style=social)](https://twitter.com/assaf_elovic)

[English](README.md) | [中文](README-zh_CN.md) | [日本語](README-ja_JP.md) | [한국어](README-ko_KR.md)

</div>

# 🔎 GPT Researcher

**GPT Researcher 是首款开源的深度研究智能体，适用于针对任何给定任务的 Web 端和本地研究。** 

该智能体能够生成详细、客观且带有引用来源的研究报告。GPT Researcher 提供全套自定义选项，用于创建量身定制的领域特定研究智能体。受近期 [Plan-and-Solve](https://arxiv.org/abs/2305.04091) 和 [RAG](https://arxiv.org/abs/2005.11401) 论文的启发，GPT Researcher 通过并行化的智能体工作流提供稳定性能并提升速度，从而解决信息错误、响应延迟、确定性及可靠性等问题。

**我们的使命是通过人工智能为个人和组织提供准确、客观且基于事实的信息。**

## Why GPT Researcher?

- 手动研究得出客观结论可能需要数周时间，耗费大量资源与精力。
- 使用过时信息训练的 LLM（大语言模型）容易产生幻觉，难以胜任当前的研究任务。
- 现有 LLM 存在 Token 数量限制，不足以生成长篇研究报告。
- 现有服务中的网络数据来源有限，容易导致信息错误且分析浅显。
- 选择性使用网络来源可能会在研究任务中引入偏见。

## Demo
<a href="https://www.youtube.com/watch?v=f60rlc_QCxE" target="_blank" rel="noopener">
  <img src="https://github.com/user-attachments/assets/ac2ec55f-b487-4b3f-ae6f-b8743ad296e4" alt="Demo video" width="800" target="_blank" />
</a>

## Install as Claude Skill

将 GPT Researcher 作为 [Claude Skill](https://skills.sh/assafelovic/gpt-researcher/gpt-researcher) 安装，以扩展 Claude 的深度研究能力：

```bash
npx skills add assafelovic/gpt-researcher
```

安装完成后，Claude 即可在你的对话中直接调用 GPT Researcher 的深度研究能力。

## Architecture

核心思想是利用“规划（planner）”和“执行（execution）”智能体。规划器负责生成研究问题，而执行智能体则收集相关信息。随后，发布模块将所有发现汇总成一份综合报告。

<div align="center">
<img align="center" height="600" src="https://github.com/assafelovic/gpt-researcher/assets/13554167/4ac896fd-63ab-4b77-9688-ff62aafcc527">
</div>

步骤：
* 根据研究查询创建特定任务的智能体。
* 生成一系列问题，共同形成对该任务的客观观点。
* 使用爬虫智能体为每个问题收集信息。
* 对每个资源进行摘要并追踪来源。
* 筛选并汇总摘要，生成最终研究报告。

## Tutorials
 - [How it Works](https://docs.gptr.dev/blog/building-gpt-researcher)
 - [How to Install](https://www.loom.com/share/04ebffb6ed2a4520a27c3e3addcdde20?sid=da1848e8-b1f1-42d1-93c3-5b0b9c3b24ea)
 - [Live Demo](https://www.loom.com/share/6a3385db4e8747a1913dd85a7834846f?sid=a740fd5b-2aa3-457e-8fb7-86976f59f9b8)

## Features

- 📝 使用网络和本地文档生成详细研究报告。
- 🖼️ 智能抓取并过滤报告配图。
- 🍌 **AI-generated inline images**：使用 Google Gemini（Nano Banana）生成视觉插图。
- 📜 生成超过 2,000 字的详细报告。
- 🌐 聚合 20 多个数据源以得出客观结论。
- 🖥️ 提供轻量级（HTML/CSS/JS）和生产就绪版（NextJS + Tailwind）前端。
- 🔍 支持 JavaScript 的网页抓取。
- 📂 在研究过程中保持记忆与上下文连贯。
- 📄 将报告导出为 PDF、Word 及其他格式。

## 📖 Documentation

请参阅 [Documentation](https://docs.gptr.dev/docs/gpt-researcher/getting-started) 获取：
- 安装与设置指南
- 配置与自定义选项
- 操作示例
- 完整 API 参考

## ⚙️ Getting Started

### Installation

1. 安装 Python 3.11 或更高版本。[指南](https://www.tutorialsteacher.com/python/install-python)。
2. 克隆项目并进入目录：

    ```bash
    git clone https://github.com/assafelovic/gpt-researcher.git
    cd gpt-researcher
    ```

3. 通过导出环境变量或将其存储在 `.env` 文件中来设置 API Key。

    ```bash
    export OPENAI_API_KEY={Your OpenAI API Key here}
    export TAVILY_API_KEY={Your Tavily API Key here}
    ```

    （可选）如需增强追踪与可观测性，还可设置：
    
    ```bash
    # export LANGCHAIN_TRACING_V2=true
    # export LANGCHAIN_API_KEY={Your LangChain API Key here}
    ```

    对于自定义的 OpenAI 兼容 API（例如本地模型或其他提供商），还可设置：
    
    ```bash
    export OPENAI_BASE_URL={Your custom API base URL here}
    ```

4. 安装依赖并启动服务：

    ```bash
    pip install -r requirements.txt
    python -m uvicorn main:app --reload
    ```

访问 [http://localhost:8000](http://localhost:8000) 即可开始使用。

其他部署方案（如 Poetry 或虚拟环境），请参阅 [Getting Started page](https://docs.gptr.dev/docs/gpt-researcher/getting-started)。

## Run as PIP package
```bash
pip install gpt-researcher

```
### Example Usage:
```python
...
from gpt_researcher import GPTResearcher

query = "why is Nvidia stock going up?"
researcher = GPTResearcher(query=query)
# Conduct research on the given query
research_result = await researcher.conduct_research()
# Write the report
report = await researcher.write_report()
...
```

**更多示例与配置，请参阅 [PIP documentation](https://docs.gptr.dev/docs/gpt-researcher/gptr/pip-package) 页面。**

### 🔧 MCP Client
GPT Researcher 支持 MCP（模型上下文协议）集成，可连接 GitHub 仓库、数据库及自定义 API 等专业数据源。这使得研究能够结合网络搜索与特定数据源进行。

```bash
export RETRIEVER=tavily,mcp  # Enable hybrid web + MCP research
```

```python
from gpt_researcher import GPTResearcher
import asyncio
import os

async def mcp_research_example():
    # Enable MCP with web search
    os.environ["RETRIEVER"] = "tavily,mcp"
    
    researcher = GPTResearcher(
        query="What are the top open source web research agents?",
        mcp_configs=[
            {
                "name": "github",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-github"],
                "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")}
            }
        ]
    )
    
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return report
```

> 如需全面的 MCP 文档与高级示例，请访问 [MCP Integration Guide](https://docs.gptr.dev/docs/gpt-researcher/retrievers/mcp-configs)。

## 🍌 Inline Image Generation

GPT Researcher 可利用 Google 的 Gemini 模型（Nano Banana）自动在研究报告中生成并嵌入 AI 绘制的插图。

```bash
# Enable in your .env file
IMAGE_GENERATION_ENABLED=true
GOOGLE_API_KEY=your_google_api_key
IMAGE_GENERATION_MODEL=models/gemini-2.5-flash-image
```

启用后，系统将：
1. 分析你的研究上下文以识别可视化机会
2. 在研究阶段预生成 2-3 张相关图片
3. 在撰写报告时将其内联嵌入

生成的图片采用暗色模式样式，与 GPT Researcher UI 保持一致，并带有专业信息图表美学风格及青色点缀。

[了解更多关于 Image Generation](https://docs.gptr.dev/docs/gpt-researcher/gptr/image_generation) 的内容。

## ✨ Deep Research

GPT Researcher 现已内置深度研究（Deep Research）功能——一种先进的递归研究工作流，以智能体的深度和广度探索主题。该功能采用树状探索模式，在保持对研究主题全面视角的同时深入子话题。

- 🌳 支持配置深度与宽度的树状探索
- ⚡️ 并发处理以加速结果生成
- 🤝 跨研究分支的智能上下文管理
- ⏱️ 每次深度研究约耗时 ~5 分钟
- 💰 每次研究成本约 $0.4（使用 `o3-mini` 并设置 "high" 推理强度）

[了解更多关于 Deep Research](https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research) 的内容。

## Run with Docker

> **Step 1** - [Install Docker](https://docs.gptr.dev/docs/gpt-researcher/getting-started/getting-started-with-docker)

> **Step 2** - 克隆 `.env.example` 文件，将你的 API Key 添加到克隆的文件中，并将文件保存为 `.env`

> **Step 3** - 在 docker-compose 文件中，注释掉你不想通过 Docker 运行的服务。

```bash
docker-compose up --build
```

如果上述命令无效，请尝试去掉连字符运行：
```bash
docker compose up --build
```

> **Step 4** - **默认情况下**，如果你未在 docker-compose 文件中取消注释任何内容，此流程将启动两个进程：
 - localhost:8000 上运行的 Python 服务器<br>
 - localhost:3000 上运行的 React 应用<br>

在任何浏览器中访问 localhost:3000 并开始研究吧！


## 📄 Research on Local Documents

你可以指示 GPT Researcher 基于你的本地文档执行研究任务。目前支持的文件格式包括：PDF、纯文本、CSV、Excel、Markdown、PowerPoint 和 Word 文档。

步骤 1：添加环境变量 `DOC_PATH`，指向你存放文档的文件夹路径。

```bash
export DOC_PATH="./my-docs"
```

步骤 2： 
 - 如果你在 localhost:8000 运行前端应用，只需从“Report Source”下拉菜单中选择“My Documents”。
 - 如果你使用 [PIP package](https://docs.tavily.com/guides/gpt-researcher/gpt-researcher#pip-package) 运行 GPT Researcher，在实例化 `GPTResearcher` 类时将 `report_source` 参数设置为 "local"（[代码示例在此](https://docs.gptr.dev/docs/gpt-researcher/context/tailored-research)）。


## 🤖 MCP Server

我们将 MCP 服务器迁移到了独立仓库：[gptr-mcp](https://github.com/assafelovic/gptr-mcp)。

GPT Researcher MCP Server 使 Claude 等 AI 应用能够开展深度研究。虽然 LLM 应用可通过 MCP 访问网络搜索工具，但 GPT Researcher MCP 能提供更深入、更可靠的研究结果。

功能：
- 为 AI 助手提供深度研究能力
- 优化上下文使用，获取高质量信息
- 为 LLM 提供推理更全面的结果
- Claude Desktop 集成支持

如需详细的安装与使用说明，请访问 [official repository](https://github.com/assafelovic/gptr-mcp)。


## 👪 Multi-Agent Assistant
随着人工智能从提示词工程和 RAG 向多智能体系统演进，我们很高兴推出基于 [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/) 和 [AG2](https://github.com/ag2ai/ag2) 构建的多智能体助手。

通过采用多智能体框架，研究过程的深度与质量可得到显著提升，这得益于多个具备专项技能的智能体的协同工作。受近期 [STORM](https://arxiv.org/abs/2402.14207) 论文的启发，本项目展示了一个 AI 智能体团队如何协作开展给定主题的研究，涵盖从规划到发布的完整流程。

平均每次运行可生成一份 5-6 页的研究报告，支持 PDF、Docx 和 Markdown 等多种格式。

可在 [此处](https://github.com/assafelovic/gpt-researcher/tree/master/multi_agents) 查看，或前往我们的文档获取关于 [LangGraph](https://docs.gptr.dev/docs/gpt-researcher/multi_agents/langgraph) 和 [AG2](https://docs.gptr.dev/docs/gpt-researcher/multi_agents/ag2) 的更多信息。

## 🔍 Observability

GPT Researcher 支持 **LangSmith** 以增强追踪与可观测性，使调试和优化复杂的多智能体工作流更加便捷。

启用追踪步骤：
1. 设置以下环境变量：
   ```bash
   export LANGCHAIN_TRACING_V2=true
   export LANGCHAIN_API_KEY=your_api_key
   export LANGCHAIN_PROJECT="gpt-researcher"
   ```
2. 像往常一样运行你的研究任务。所有基于 LangGraph 的智能体交互将在你的 LangSmith 仪表板中自动被追踪和可视化。

## 🖥️ Frontend Applications

GPT-Researcher 现已推出增强型前端，以改善用户体验并简化研究工作流。该前端提供：

- 用于输入研究查询的直观界面
- 研究任务的实时进度跟踪
- 研究成果的交互式展示
- 可自定义的设置选项以满足个性化研究需求

目前提供两种部署方案：
1. 由 FastAPI 托管的轻量级静态前端
2. 功能丰富的 NextJS 应用，支持高级功能

如需详细设置说明及更多关于前端功能的介绍，请访问我们的 [documentation page](https://docs.gptr.dev/docs/gpt-researcher/frontend/introduction)。

## 🚀 Contributing
我们非常欢迎贡献！如果你有兴趣参与，请查看 [contributing](https://github.com/assafelovic/gpt-researcher/blob/master/CONTRIBUTING.md) 指南。

欢迎查阅我们的 [roadmap](https://trello.com/b/3O7KBePw/gpt-researcher-roadmap) 页面，并希望通过 [Discord community](https://discord.gg/QgZXvJAccX) 与我们取得联系，加入我们的使命。
<a href="https://github.com/assafelovic/gpt-researcher/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=assafelovic/gpt-researcher&max=1000" />
</a>
## ✉️ Support / Contact us
- [Community Discord](https://discord.gg/spBgZmm3Xe)
- Author Email: assaf.elovic@gmail.com

## 🛡 Disclaimer

本项目 GPT Researcher 为实验性应用，按“原样”提供，不提供任何明示或暗示的担保。我们在 Apache 2 许可证下分享代码用于学术交流目的。本文内容不构成学术建议，亦非推荐在学术论文或研究中使用的意见。

我们对客观研究声明的看法：
1. GPT Researcher 的主要目标是减少错误和偏见事实。如何实现？我们认为抓取的数据源越多，出现错误数据的可能性就越低。通过针对每项研究抓取多个网站并选择出现频率最高的信息，它们全部出错的可能性极低。
2. 我们的目标并非消除偏见，而是尽可能减少它。**作为社区成员，我们致力于探索最有效的人机/LLM 交互方式。**
3. 在研究中，人们也往往倾向于带有偏见，因为大多数人对自己研究的主题已有既定观点。该工具会抓取大量观点，并均衡地解释有偏见的人可能从未阅读过的多元视角。

---

<p align="center">
<a href="https://star-history.com/#assafelovic/gpt-researcher">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=assafelovic/gpt-researcher&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=assafelovic/gpt-researcher&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=assafelovic/gpt-researcher&type=Date" />
  </picture>
</a>
</p>


<p align="right">
  <a href="#top">⬆️ Back to Top</a>
</p>