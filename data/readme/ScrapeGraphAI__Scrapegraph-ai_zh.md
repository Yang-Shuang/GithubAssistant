## 🚀 **正在寻找一种更快、更简单的规模化抓取方式（仅需 5 行代码）？** 请访问我们的增强版：[**ScrapeGraphAI.com**](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&ut#m_content=top_banner)！🚀

---

# 🕷️ ScrapeGraphAI：你只需抓取一次

<p align="center">
  <a href="https://scrapegraphai.com">
    <img src="media/banner.png" alt="ScrapeGraphAI" style="width: 100%;">
  </a>
</p>

[English](README.md) | [中文](docs/chinese.md) | [日本語](docs/japanese.md)
| [한국어](docs/korean.md)
| [Русский](docs/russian.md) | [Türkçe](docs/turkish.md)
| [Deutsch](docs/german.md)
| [Español](docs/spanish.md)
| [français](docs/french.md)
| [Português](docs/portuguese.md)
| [Italiano](docs/italian.md)

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/scrapegraphai?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/scrapegraphai)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![](https://dcbadge.vercel.app/api/server/gkxQDAjfeX)](https://discord.gg/gkxQDAjfeX)

<p align="center">
<a href="https://trendshift.io/repositories/15078" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15078" alt="ScrapeGraphAI%2FScrapegraph-ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<p align="center">

[ScrapeGraphAI](https://scrapegraphai.com) 是一个使用大语言模型 (LLM) 和直接图逻辑的 Python *网页抓取*库，用于为网站和本地文档（XML、HTML、JSON、Markdown 等）创建数据抓取流水线。

只需告诉它你想提取哪些信息，该库就会为你完成工作！

## 🚀 集成支持
ScrapeGraphAI 提供了与流行框架和工具的无缝集成，以增强你的抓取能力。无论你是使用 Python 或 Node.js 进行开发、使用大语言模型框架，还是在无代码平台上工作，我们都提供了全面的集成选项来满足你的需求。

<p align="center">
  <img src="https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/sgai-hero.png" alt="ScrapeGraphAI Hero" style="width: 100%;">
</p>

你可以在以下[链接](https://scrapegraphai.com)找到更多信息。

**集成支持**：
- **API**：[文档](https://docs.scrapegraphai.com/introduction)
- **SDK**：[Python](https://docs.scrapegraphai.com/sdks/python)、[Node](https://docs.scrapegraphai.com/sdks/javascript)
- **大语言模型框架**：[Langchain](https://docs.scrapegraphai.com/integrations/langchain)、[Llama Index](https://docs.scrapegraphai.com/integrations/llamaindex)、[Crew.ai](https://docs.scrapegraphai.com/integrations/crewai)、[Agno](https://docs.scrapegraphai.com/integrations/agno)、[CamelAI](https://github.com/camel-ai/camel)
- **低代码框架**：[Pipedream](https://pipedream.com/apps/scrapegraphai)、[Bubble](https://bubble.io/plugin/scrapegraphai-1745408893195x213542371433906180)、[Zapier](https://zapier.com/apps/scrapegraphai/integrations)、[n8n](http://localhost:5001/dashboard)、[Dify](https://dify.ai)、[Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
- **MCP 服务器**： [链接](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)

## 🚀 快速安装

ScrapeGraphAI 的官方参考页面位于 PyPI：[pypi](https://pypi.org/project/scrapegraphai/)。

```bash
pip install scrapegraphai

# IMPORTANT (for fetching websites content)
playwright install
```

**注意**：建议在虚拟环境中安装该库，以避免与其他库发生冲突 🐱


## 💻 使用方法
有多种标准的抓取流水线可用于从网站（或本地文件）中提取信息。

其中最常用的是 `SmartScraperGraph`，它根据用户提示词和源 URL 从单个页面提取信息。

```python
from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract useful information from the webpage, including a description of what the company does, founders and social media links",
    source="https://scrapegraphai.com/",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> 对于 OpenAI 及其他模型，你只需更改 llm 配置即可！
> ```python
>graph_config = {
>    "llm": {
>        "api_key": "YOUR_OPENAI_API_KEY",
>        "model": "openai/gpt-4o-mini",
>    },
>    "verbose": True,
>    "headless": False,
>}
>```


输出结果将是一个如下所示的字典：

```python
{
    "description": "ScrapeGraphAI transforms websites into clean, organized data for AI agents and data analytics. It offers an AI-powered API for effortless and cost-effective data extraction.",
    "founders": [
        {
            "name": "",
            "role": "Founder & Technical Lead",
            "linkedin": "https://www.linkedin.com/in/perinim/"
        },
        {
            "name": "Marco Vinciguerra",
            "role": "Founder & Software Engineer",
            "linkedin": "https://www.linkedin.com/in/marco-vinciguerra-7ba365242/"
        },
        {
            "name": "Lorenzo Padoan",
            "role": "Founder & Product Engineer",
            "linkedin": "https://www.linkedin.com/in/lorenzo-padoan-4521a2154/"
        }
    ],
    "social_media_links": {
        "linkedin": "https://www.linkedin.com/company/101881123",
        "twitter": "https://x.com/scrapegraphai",
        "github": "https://github.com/ScrapeGraphAI/Scrapegraph-ai"
    }
}
```
还有其他流水线可用于从多个页面提取信息、生成 Python 脚本，甚至生成音频文件。

| Pipeline Name           | Description                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| SmartScraperGraph       | 单页抓取器，仅需用户提示词和输入源。                                                                           |
| SearchGraph             | 多页抓取器，从搜索引擎的前 n 条搜索结果中提取信息。                                                              |
| SpeechGraph             | 单页抓取器，从网站提取信息并生成音频文件。                                                                       |
| ScriptCreatorGraph      | 单页抓取器，从网站提取信息并生成 Python 脚本。                                                                   |
| SmartScraperMultiGraph  | 多页抓取器，根据单个提示词和源列表从多个页面提取信息。                                                           |
| ScriptCreatorMultiGraph | 多页抓取器，生成用于从多个页面和源提取信息的 Python 脚本。                                                       |

上述每种流水线均提供 Multi（多版本）。它支持并行调用大语言模型。

你可以通过 API 使用不同的**大语言模型 (LLM)**，例如 **OpenAI**、**Groq**、**Azure**、**Gemini**、**MiniMax** 等，或者通过 **Ollama** 使用本地模型。

如果你打算使用本地模型，请确保已安装 [Ollama](https://ollama.com/)，并使用 **ollama pull** 命令下载所需模型。


## 📖 文档

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing)

ScrapeGraphAI 的官方文档请参见[此处](https://docs.scrapegraphai.com/introduction)。

## 🤝 贡献指南

欢迎随时提交贡献，并加入我们的 Discord 服务器与我们讨论改进建议！

请参阅[贡献指南](https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/CONTRIBUTING.md)。

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/uJN7TYcpNa)
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/scrapegraphai/)
[![My Skills](https://skillicons.dev/icons?i=twitter)](https://twitter.com/scrapegraphai)

## 🔗 ScrapeGraph API 与 SDK
如果你正在寻找将 ScrapeGraph 快速集成到系统中的解决方案，请查看我们强大的 API [这里！](https://dashboard.scrapegraphai.com/login)

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://dashboard.scrapegraphai.com/login)

我们提供 Python 和 Node.js 的 SDK，方便你轻松集成到项目中。请参见下方：

| SDK       | Language | GitHub Link                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| Python SDK | Python   | [scrapegraph-py](https://docs.scrapegraphai.com/sdks/python) |
| Node.js SDK | Node.js  | [scrapegraph-js](https://docs.scrapegraphai.com/sdks/javascript) |

官方 API 文档请参见[此处](https://docs.scrapegraphai.com/introduction)。

## 📈 使用统计 (Telemetry)
我们收集匿名使用指标，以提升包的质量和用户体验。这些数据有助于我们确定改进优先级并确保兼容性。如果你希望退出数据收集，请设置环境变量 `SCRAPEGRAPHAI_TELEMETRY_ENABLED=false`。更多信息请参阅[此处文档](https://docs.scrapegraphai.com/introduction)。

## ❤️ 贡献者
[![Contributors](https://contrib.rocks/image?repo=ScrapeGraphAI/Scrapegraph-ai)](https://github.com/ScrapeGraphAI/Scrapegraph-ai/graphs/contributors)

## 🎓 引用规范
如果你在我们的研究工作中使用了该库，请使用以下引用格式：
```text
  @misc{scrapegraph-ai,
    author = {Lorenzo Padoan, Marco Vinciguerra},
    title = {Scrapegraph-ai},
    year = {2024},
    url = {https://github.com/ScrapeGraphAI/Scrapegraph-ai},
    note = {A Python library for scraping leveraging large language models}
  }
```
## 作者

|                    | Contact Info         |
|--------------------|----------------------|
| Marco Vinciguerra  | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/)    |
| Lorenzo Padoan     | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)  |

## 📜 许可证

ScrapeGraphAI 采用 MIT 许可证。更多信息请参阅 [LICENSE](https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/LICENSE) 文件。

## 致谢

- 感谢所有项目贡献者及开源社区的支持。
- ScrapeGraphAI 仅应用于数据探索和研究目的。我们不对任何滥用该库的行为承担责任。

由 [ScrapeGraph AI](https://scrapegraphai.com) 用 ❤️ 制作

[Scarf tracking](https://static.scarf.sh/a.png?x-pxid=102d4b8c-cd6a-4b9e-9a16-d6d141b9212d)