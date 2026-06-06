<div align="center">
  <a href="https://pathway.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://pathway.com/logo-light.svg">
      <img src="https://pathway.com/logo-dark.svg">
    </picture>
  </a>
  <br /><br />
  <a href="https://trendshift.io/repositories/10388" target="_blank"><img src="https://trendshift.io/api/badge/repositories/10388" alt="pathwaycom%2Fpathway | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
  <br /><br />
</div>
<p align="center">
        <a href="https://github.com/pathwaycom/pathway/actions/workflows/ubuntu_test.yml">
        <img src="https://github.com/pathwaycom/pathway/actions/workflows/ubuntu_test.yml/badge.svg" alt="ubuntu"/>
        <br>
        <a href="https://github.com/pathwaycom/pathway/actions/workflows/release.yml">
        <img src="https://github.com/pathwaycom/pathway/actions/workflows/release.yml/badge.svg" alt="Last release"/></a>
        <a href="https://badge.fury.io/py/pathway"><img src="https://badge.fury.io/py/pathway.svg" alt="PyPI version" height="18"></a>
        <a href="https://badge.fury.io/py/pathway"><img src="https://static.pepy.tech/badge/pathway" alt="PyPI downloads" height="18"></a>
        <a href="https://github.com/pathwaycom/pathway/blob/main/LICENSE.txt">
        <img src="https://img.shields.io/badge/license-BSL-green" alt="License: BSL"/></a>
      <br>
        <a href="https://discord.gg/pathway">
        <img src="https://img.shields.io/discord/1042405378304004156?logo=discord"
            alt="chat on Discord"></a>
        <a href="https://twitter.com/intent/follow?screen_name=pathway_com">
        <img src="https://img.shields.io/twitter/follow/pathwaycom"
            alt="follow on Twitter"></a>
        <a href="https://linkedin.com/company/pathway">
        <img src="https://img.shields.io/badge/pathway-0077B5?style=social&logo=linkedin" alt="follow on LinkedIn"></a>
      <a href="https://github.com/dylanhogg/awesome-python/blob/main/README.md">
      <img src="https://awesome.re/badge.svg" alt="Awesome Python"></a>
      <a href="https://gurubase.io/g/pathway">
      <img src="https://img.shields.io/badge/Gurubase-Ask%20Pathway%20Guru-006BFF" alt="Pathway Guru"></a>
    <br>
    <a href="#getting-started">快速开始</a> |
    <a href="#deployment">部署</a> |
    <a href="#resources">文档与支持</a> |
    <a href="https://pathway.com/blog/">博客</a> |
    <a href="#license">许可证</a>

  
</p>

# Pathway Live Data Framework<a id="pathway"> 实时数据框架</a>

[Pathway Live Data Framework](https://pathway.com) 是一个用于流处理、实时分析、大语言模型（LLM）管道和检索增强生成（RAG）的 Python ETL 框架。

Pathway Live Data Framework 提供**易于使用的 Python API**，让你能够无缝集成常用的 Python 机器学习库。
Pathway Live Data Framework 的代码兼具通用性与健壮性：**你可以在开发和生产环境中使用它，高效处理批处理和流式数据**。同一套代码可用于本地开发、CI/CD 测试、运行批处理任务、处理流回放以及实时数据流。

Pathway Live Data Framework 由基于差分数据流（Differential Dataflow）的**可扩展 Rust 引擎**驱动，并执行增量计算。
尽管你的代码是用 Python 编写的，但实际由 Rust 引擎运行，从而支持多线程、多进程和分布式计算。
所有管道（Pipeline）均驻留内存中，并可通过 **Docker 和 Kubernetes** 轻松部署。

你可以通过 pip 安装 Pathway Live Data Framework：
```
pip install -U pathway
```

如有任何疑问，欢迎在 [Discord](https://discord.com/invite/pathway) 上联系项目团队和社区。

## 使用场景与模板

准备好看看 Pathway Live Data Framework 能做什么了吗？

[尝试运行我们的简易示例](https://pathway.com/developers/templates)!

这些开箱即用的示例提供 Notebook 和 Docker 两种格式，只需几次点击即可运行。选择一个开始你的 Pathway Live Data Framework 实战之旅吧！

### 事件处理与实时分析管道
凭借统一的批流一体引擎和完整的 Python 兼容性，Pathway Live Data Framework 让数据处理变得尽可能简单。它是各类数据处理管道的理想解决方案，包括：

- [示例：实时 ETL。](https://pathway.com/developers/templates/kafka-etl)
- [示例：带告警的事件驱动管道。](https://pathway.com/developers/templates/realtime-log-monitoring)
- [示例：实时分析。](https://pathway.com/developers/templates/linear_regression_with_kafka)
- [文档：从批处理切换到流处理。](https://pathway.com/developers/user-guide/connecting-to-data/switch-from-batch-to-streaming)



### AI 管道

Pathway Live Data Framework 提供专用的大语言模型工具，用于构建实时 LLM 和 RAG 管道。内置了大多数常用 LLM 服务的封装器（Wrappers）及实用工具，让处理 LLM 和 RAG 管道变得极其简单。查看我们的 [LLM xpack 文档](https://pathway.com/developers/user-guide/llm-xpack/overview)。

不妨尝试一下我们包含 LLM 工具的可运行示例。
你可以在[这里](https://pathway.com/developers/user-guide/llm-xpack/llm-examples)找到这些示例。

  - [模板：实时将非结构化数据转换为 SQL。](https://pathway.com/developers/templates/unstructured-to-structured)
  - [模板：使用 Ollama 和 Mistral AI 构建私有 RAG](https://pathway.com/developers/templates/private-rag-ollama-mistral)
  - [模板：自适应 RAG](https://pathway.com/developers/templates/adaptive-rag)
  - [模板：使用 gpt-4o 的多模态 RAG](https://pathway.com/developers/templates/multimodal-rag)

## 核心特性

- **丰富的连接器**：Pathway Live Data Framework 内置多种连接器，可对接 Kafka、GDrive、PostgreSQL、SharePoint 等外部数据源。其 Airbyte 连接器支持连接 300 多种不同的数据源。如果你需要的连接器不可用，可以使用 Pathway Live Data Framework Python SDK 构建自定义连接器。
- **无状态与有状态转换**：Pathway Live Data Framework 支持 JOIN、窗口化（Windowing）和排序等有状态转换操作。它提供了大量直接由 Rust 实现的转换功能。除了内置转换外，你还可以使用任意 Python 函数或库来处理数据。
- **持久化**：Pathway Live Data Framework 提供持久化功能以保存计算状态。这允许你在更新或崩溃后重新启动管道。你的管道在 Pathway Live Data Framework 中安全无忧！
- **一致性保障**：Pathway Live Data Framework 帮你管理时间逻辑，确保所有计算结果保持一致。特别是，它能处理迟到和乱序数据点，并在有新（或迟到的）数据进入系统时自动更新结果。Pathway Live Data Framework 免费版提供“至少一次”（at least once）一致性保证，企业版则提供“精确一次”（exactly once）一致性保证。
- **可扩展的 Rust 引擎**：借助 Pathway Live Data Framework 的 Rust 引擎，你可以摆脱 Python 常见的性能限制。轻松实现多线程、多进程和分布式计算。
- **大语言模型辅助工具**：Pathway Live Data Framework 提供 LLM 扩展模块，包含集成 LLM 到数据管道所需的所有实用工具（如 LLM 封装器、解析器、嵌入器、分块器），以及内存中的实时向量索引，并集成了 LLamaIndex 和 LangChain。你可以快速构建并部署带有实时文档的 RAG 应用。


## 快速开始<a id="getting-started"></a>

### 安装<a id="installation"></a>

Pathway Live Data Framework 需要 Python 3.10 或更高版本。

你可以通过 `pip` 安装当前版本的 Pathway Live Data Framework：

```
$ pip install -U pathway
```

⚠️ Pathway Live Data Framework 目前支持 MacOS 和 Linux。其他系统的用户建议在虚拟机中运行。


### 示例：实时计算正值之和。<a id="example"></a>

```python
import pathway as pw

# Define the schema of your data (Optional)
class InputSchema(pw.Schema):
  value: int

# Connect to your data using connectors
input_table = pw.io.csv.read(
  "./input/",
  schema=InputSchema
)

#Define your operations on the data
filtered_table = input_table.filter(input_table.value>=0)
result_table = filtered_table.reduce(
  sum_value = pw.reducers.sum(filtered_table.value)
)

# Load your results to external systems
pw.io.jsonlines.write(result_table, "output.jsonl")

# Run the computation
pw.run()
```

你可以在 [Google Colab](https://colab.research.google.com/drive/1aBIJ2HCng-YEUOMrr0qtj0NeZMEyRz55?usp=sharing) 中运行 Pathway Live Data Framework。

你可以在[这里](https://github.com/pathwaycom/pathway/tree/main/examples)找到更多示例。


## 部署<a id="deployment"></a>

### 本地运行<a id="running-pathway-locally"></a>

要使用 Pathway Live Data Framework，只需导入它：

```python
import pathway as pw
```

现在，你可以轻松创建数据处理管道，并让 Pathway Live Data Framework 自动处理数据更新。一旦管道创建完成，你只需一行命令即可在流式数据上启动计算：

```python
pw.run()
```

随后可像运行普通 Python 脚本一样执行你的项目（例如 `main.py`）：`$ python main.py`。
Pathway Live Data Framework 内置监控仪表盘，让你可以实时追踪每个连接器发送的消息数量及系统延迟。仪表盘还集成了日志消息功能。 

<img src="https://d14l3brkh44201.cloudfront.net/pathway-dashboard.png" width="1326" alt="Pathway Live Data Framework dashboard"/>

或者，你也可以使用 `pathway` 命令运行：

```
$ pathway spawn python main.py
```

Pathway Live Data Framework 原生支持多线程。
要以 3 个线程启动你的应用，可执行以下操作：
```
$ pathway spawn --threads 3 python main.py
```

要快速启动一个 Pathway Live Data Framework 项目，可以使用我们的 [cookiecutter 模板](https://github.com/pathwaycom/cookiecutter-pathway)。


### Docker<a id="docker"></a>

你可以轻松使用 Docker 运行 Pathway Live Data Framework。

#### Pathway Live Data Framework 镜像

你可以使用 [Pathway Live Data Framework Docker 镜像](https://hub.docker.com/r/pathwaycom/pathway)，配合以下 Dockerfile：

```dockerfile
FROM pathwaycom/pathway:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-script.py" ]
```

随后可构建并运行该 Docker 镜像：

```console
docker build -t my-pathway-app .
docker run -it --rm --name my-pathway-app my-pathway-app
```

#### 运行单个 Python 脚本

对于单文件项目，编写完整的 `Dockerfile` 可能显得多余。在这种情况下，你可以直接使用 Pathway Live Data Framework Docker 镜像执行 Python 脚本。例如：

```console
docker run -it --rm --name my-pathway-app -v "$PWD":/app pathwaycom/pathway:latest python my-pathway-app.py
```

#### 使用标准 Python Docker 镜像

你也可以使用标准的 Python 镜像，并通过 Dockerfile 安装 Pathway Live Data Framework：

```dockerfile
FROM --platform=linux/x86_64 python:3.10

RUN pip install -U pathway
COPY ./pathway-script.py pathway-script.py

CMD ["python", "-u", "pathway-script.py"]
```

### Kubernetes 与云部署<a id="k8s"></a>

Docker 容器非常适合在云端通过 Kubernetes 进行部署。
如果你希望扩展 Pathway Live Data Framework 应用，可以关注我们的企业版（Enterprise）。
Pathway Live Data Framework 企业版专为端到端数据处理和实时智能分析量身定制。
它通过云端分布式计算实现弹性扩展，并支持带有外部持久化配置的分布式 Kubernetes 部署。

你可以轻松使用 Render 等云服务部署 Pathway Live Data Framework：详见[如何一键部署 Pathway Live Data Framework](https://pathway.com/developers/user-guide/deployment/render-deploy/)。

如有兴趣，欢迎随时[联系我们](mailto:contact@pathway.com)了解更多详情。

## 性能表现<a id="performance"></a>

Pathway Live Data Framework 旨在超越专为流处理和批处理任务设计的先进技术方案，包括 Flink、Spark 和 Kafka Streaming。它还支持以流模式实现许多其他流框架难以直接支持的算法/用户自定义函数（UDFs）（特别是：时间关联、迭代图算法、机器学习例程）。

如果你感兴趣，可以查看[一些可交互的基准测试](https://github.com/pathwaycom/pathway-benchmarks)。

<img src="https://github.com/pathwaycom/pathway-benchmarks/raw/main/images/bm-wordcount-lineplot.png" width="1326" alt="WordCount Graph"/>

## 文档与支持<a id="resources"></a>

Pathway Live Data Framework 的全部文档均可在 [pathway.com/developers/](https://pathway.com/developers/user-guide/introduction/welcome) 查阅，包括 [API 参考文档](https://pathway.com/developers/api-docs/pathway)。

如有任何疑问，欢迎随时在 [GitHub 上提交 Issue](https://github.com/pathwaycom/pathway/issues)、加入我们的 [Discord 社区](https://discord.com/invite/pathway)，或发送邮件至 [contact@pathway.com](mailto:contact@pathway.com)。



## 🤝 重点合作与集成

我们致力于构建前沿的数据处理管道，并共同推广拓展 Python 与流数据处理能力边界的技术方案。
认识这些与我们共同塑造数据工程未来的伙伴：

<div align="center">

| Project | Description |
| ------------ | ----------- |
| [Databento](https://databento.com/blog/option-greeks) | 更简单、更快的市场数据获取方式。 |
| [LangChain](https://docs.langchain.com/oss/python/integrations/vectorstores/pathway) | LangChain 是智能体工程平台。 |
| [LlamaIndex](https://developers.llamaindex.ai/python/examples/retrievers/pathway_retriever/) | 构建上下文感知 AI 智能体的开发者信赖框架。 |
| [MinIO](https://www.min.io/) | MinIO 是一款高性能、S3 兼容的对象存储，采用 GNU AGPLv3 许可证开源。 |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | PaddleOCR 是行业领先的 OCR 与文档 AI 引擎，提供从文本提取到智能文档理解的端到端解决方案。 |
| [Redpanda](https://www.redpanda.com/blog/replace-kafka-redpanda-data-analysis-streaming) | 构建、运营和管理流处理及 AI 应用，无需 Kafka 的复杂性。 |
</div>


## 许可证<a id="license"></a>

Pathway Live Data Framework 采用 [BSL 1.1 许可证](https://github.com/pathwaycom/pathway/blob/main/LICENSE.txt) 分发，允许无限期免费用于非商业用途，以及[大多数商业目的](https://pathway.com/license/)。本仓库中的代码在发布 4 年后将自动转为开源（采用 Apache 2.0 许可证）。部分与本仓库互补的[公开仓库](https://github.com/pathwaycom)（如示例、库、连接器等）采用 MIT 许可证开源。


## 贡献指南<a id="contribution-guidelines"></a>

如果你开发了希望与此仓库集成的库或连接器，建议先以独立的仓库发布，并采用 MIT 或 Apache 2.0 许可证。 

关于 Pathway Live Data Framework 核心功能的相关问题，欢迎提交 Issue。如需进一步交流，请随时加入 Pathway 的 [Discord 社区](https://discord.gg/pathway)。