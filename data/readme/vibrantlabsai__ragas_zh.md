<h1 align="center">
  <img style="vertical-align:middle" height="200"
  src="https://raw.githubusercontent.com/vibrantlabsai/ragas/main/docs/_static/imgs/logo.png">
</h1>
<p align="center">
  <i>为你的大语言模型（LLM）应用评估注入强大动力 🚀</i>
</p>

<p align="center">
    <a href="https://github.com/vibrantlabsai/ragas/releases">
        <img alt="Latest release" src="https://img.shields.io/github/release/vibrantlabsai/ragas.svg">
    </a>
    <a href="https://www.python.org/">
        <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?color=purple">
    </a>
    <a href="https://github.com/vibrantlabsai/ragas/blob/master/LICENSE">
        <img alt="License Apache-2.0" src="https://img.shields.io/github/license/vibrantlabsai/ragas.svg?color=green">
    </a>
    <a href="https://pypi.org/project/ragas/">
        <img alt="Ragas Downloads per month" src="https://static.pepy.tech/badge/ragas/month">
    </a>
    <a href="https://discord.gg/5djav8GGNZ">
        <img alt="Join Ragas community on Discord" src="https://img.shields.io/discord/1119637219561451644">
    </a>
    <a target="_blank" href="https://deepwiki.com/vibrantlabsai/ragas">
      <img 
        src="https://devin.ai/assets/deepwiki-badge.png" 
        alt="Ask DeepWiki.com" 
        height="20" 
      />
    </a>
</p>

<h4 align="center">
    <p>
        <a href="https://docs.ragas.io/">文档</a> |
        <a href="#fire-quickstart">快速入门</a> |
        <a href="https://discord.gg/5djav8GGNZ">加入 Discord</a> |
        <a href="https://blog.ragas.io/">博客</a> |
        <a href="https://newsletter.ragas.io/">通讯</a> |
        <a href="https://www.ragas.io/careers">招聘</a>
    <p>
</h4>

面向大语言模型（LLM）应用的目标指标、智能测试生成与数据驱动洞察

Ragas 是你评估和优化大型语言模型（LLM）应用的终极工具包。告别耗时且主观的评估方式，拥抱数据驱动、高效的工作流。还没有准备好测试数据集？我们也提供与生产环境对齐的测试集生成功能。

## 核心特性

- 🎯 **客观指标**：结合基于大语言模型和传统指标，精准评估你的 LLM 应用。
- 🧪 **测试数据生成**：自动生成覆盖广泛场景的全面测试数据集。
- 🔗 **无缝集成**：与 LangChain 等主流大语言模型框架及主要可观测性工具完美兼容。
- 📊 **构建反馈闭环**：利用生产数据持续优化你的 LLM 应用。

## :shield: 安装

PyPI：

```bash
pip install ragas
```

或者，从源码安装：

```bash
pip install git+https://github.com/vibrantlabsai/ragas
```

## :fire: 快速入门

### 克隆完整示例项目

最快的上手方式是使用 `ragas quickstart` 命令：

```bash
# List available templates
ragas quickstart

# Create a RAG evaluation project
ragas quickstart rag_eval

# Specify where you want to create it.
ragas quickstart rag_eval -o ./my-project
```

可用模板：
- `rag_eval` - 评估检索增强生成（RAG）系统

即将推出：
- `agent_evals` - 评估 AI Agent
- `benchmark_llm` - 基准测试与对比大语言模型
- `prompt_evals` - 评估提示词（Prompt）变体
- `workflow_eval` - 评估复杂工作流

### 评估你的大语言模型应用

`ragas` 内置了针对常见评估任务的指标。例如，Aspect Critique（维度评估）使用 `DiscreteMetric` 来评估输出的任意方面：

```python
import asyncio
from openai import AsyncOpenAI
from ragas.metrics import DiscreteMetric
from ragas.llms import llm_factory

# Setup your LLM
client = AsyncOpenAI()
llm = llm_factory("gpt-4o", client=client)

# Create a custom aspect evaluator
metric = DiscreteMetric(
    name="summary_accuracy",
    allowed_values=["accurate", "inaccurate"],
    prompt="""Evaluate if the summary is accurate and captures key information.

Response: {response}

Answer with only 'accurate' or 'inaccurate'."""
)

# Score your application's output
async def main():
    score = await metric.ascore(
        llm=llm,
        response="The summary of the text is..."
    )
    print(f"Score: {score.value}")  # 'accurate' or 'inaccurate'
    print(f"Reason: {score.reason}")


if __name__ == "__main__":
    asyncio.run(main())
```

> **注意**：请确保已设置环境变量 `OPENAI_API_KEY`。

查看完整的[快速入门指南](https://docs.ragas.io/en/latest/getstarted/quickstart)

## 想借助评估工具优化你的 AI 应用吗？

过去两年中，我们见证并协助了许多 AI 应用通过评估实现优化。如果你希望借助评估工具来改进和扩展你的 AI 应用，

🔗 预约[一个时段](https://cal.com/team/vibrantlabs/app)或直接联系我们：[founders@vibrantlabs.com](mailto:founders@vibrantlabs.com)。

## 🫂 社区

如果你想更深入地参与 Ragas 社区，欢迎加入我们的 [Discord 服务器](https://discord.gg/5qGUJ6mh7C)。这是一个充满活力的社区，我们在这里热烈探讨大语言模型、检索技术、生产环境部署等话题。

## 贡献者

```yml
+----------------------------------------------------------------------------+
|     +----------------------------------------------------------------+     |
|     | Developers: Those who built with `ragas`.                      |     |
|     | (You have `import ragas` somewhere in your project)            |     |
|     |     +----------------------------------------------------+     |     |
|     |     | Contributors: Those who make `ragas` better.       |     |     |
|     |     | (You make PR to this repo)                         |     |     |
|     |     +----------------------------------------------------+     |     |
|     +----------------------------------------------------------------+     |
+----------------------------------------------------------------------------+
```

我们欢迎社区成员的贡献！无论是修复 Bug、添加新功能还是改进文档，你的每一份投入都弥足珍贵。

1. Fork（复刻）该仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 🔍 开放数据收集（Analytics）

在 Ragas，我们坚信透明化。我们仅收集最小化、匿名的使用数据，以改进产品并指导开发工作。

✅ 不收集任何个人或公司身份信息

✅ 开源的数据收集 [代码](./src/ragas/_analytics.py)

✅ 公开可查的聚合 [数据](https://github.com/vibrantlabsai/ragas/issues/49)

如需退出跟踪，请将环境变量 `RAGAS_DO_NOT_TRACK` 设置为 `true`。

### 引用我们

```
@misc{ragas2024,
  author       = {VibrantLabs},
  title        = {Ragas: Supercharge Your LLM Application Evaluations},
  year         = {2024},
  howpublished = {\url{https://github.com/vibrantlabsai/ragas}},
}
```