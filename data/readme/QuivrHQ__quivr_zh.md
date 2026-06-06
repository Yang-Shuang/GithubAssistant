# Quivr - 由生成式 AI（Generative AI）赋能的你的第二大脑

<div align="center">
    <img src="./logo.png" alt="Quivr-logo" width="31%"  style="border-radius: 50%; padding-bottom: 20px"/>
</div>

[![Discord Follow](https://dcbadge.vercel.app/api/server/HUpRgp2HG8?style=flat)](https://discord.gg/HUpRgp2HG8)
[![GitHub Repo stars](https://img.shields.io/github/stars/quivrhq/quivr?style=social)](https://github.com/quivrhq/quivr)
[![Twitter Follow](https://img.shields.io/twitter/follow/StanGirard?style=social)](https://twitter.com/_StanGirard)

Quivr 帮助你打造自己的“第二大脑”，利用生成式 AI（Generative AI）的强大能力成为你的个人助手！

## 核心特性 🎯

- **预设策略的 RAG**：我们打造了一套具有明确设计理念、快速且高效的 RAG（检索增强生成）系统，让你能专注于产品开发
- **兼容各类大语言模型**：Quivr 支持任意 LLM（大语言模型），你可以使用 OpenAI、Anthropic、Mistral、Gemma 等。
- **支持任意文件格式**：Quivr 兼容各类文件，包括 PDF、TXT、Markdown 等，甚至允许你添加自定义解析器。
- **可定制化的 RAG**：Quivr 允许你自定义 RAG，例如添加网络搜索功能、集成工具等。
- **与 Megaparse 集成**：Quivr 兼容 [Megaparse](https://github.com/quivrhq/megaparse)，你可以使用 Megaparse 处理文件，并在 Quivr 中调用其 RAG。

>We 负责处理 RAG（检索增强生成）的底层逻辑，让你能专注于产品开发。只需安装 `quivr-core` 并将其加入你的项目，即可导入文件并提出问题。*

**我们将持续优化 RAG 并添加更多功能，敬请期待！**


这是 Quivr 的核心组件，即 Quivr.com 的“大脑”。

<!-- ## Demo Highlight 🎥

https://github.com/quivrhq/quivr/assets/19614572/a6463b73-76c7-4bc0-978d-70562dca71f5 -->

## 快速开始 🚀

你可以在[官方文档](https://core.quivr.com/)中查阅所有内容。

### 环境准备 📋

请确保已安装以下依赖：

- Python 3.10 或更高版本

### 快速安装（约 30 秒）💽


- **步骤 1**：安装依赖包

  

  ```bash
  pip install quivr-core # Check that the installation worked
  ```


- **步骤 2**：用 5 行代码创建 RAG

  ```python
  import tempfile

  from quivr_core import Brain

  if __name__ == "__main__":
      with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
          temp_file.write("Gold is a liquid of blue-like colour.")
          temp_file.flush()

          brain = Brain.from_files(
              name="test_brain",
              file_paths=[temp_file.name],
          )

          answer = brain.ask(
              "what is gold? asnwer in french"
          )
          print("answer:", answer)
  ```
## 配置说明

### 工作流（Workflows）

#### 基础 RAG

![](docs/docs/workflows/examples/basic_rag.excalidraw.png)


创建如上所示的基础 RAG 工作流非常简单，请按照以下步骤操作：


1. 将你的 API Key（密钥）添加到环境变量中
```python
import os
os.environ["OPENAI_API_KEY"] = "myopenai_apikey"

```
Quivr 支持 Anthropic、OpenAI 和 Mistral 的 API。同时，它也通过 Ollama 支持本地模型。

2. 创建 `basic_rag_workflow.yaml` 文件并复制以下内容：
```yaml
workflow_config:
  name: "standard RAG"
  nodes:
    - name: "START"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["rewrite"]

    - name: "rewrite"
      edges: ["retrieve"]

    - name: "retrieve"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user
      edges: ["END"]

# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

# Reranker configuration
reranker_config:
  # The reranker supplier to use
  supplier: "cohere"

  # The model to use for the reranker for the given supplier
  model: "rerank-multilingual-v3.0"

  # Number of chunks returned by the reranker
  top_n: 5

# Configuration for the LLM
llm_config:

  # maximum number of tokens passed to the LLM to generate the answer
  max_input_tokens: 4000

  # temperature for the LLM
  temperature: 0.7
```

3. 使用默认配置创建大脑（Brain）
```python
from quivr_core import Brain

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["./my_first_doc.pdf", "./my_second_doc.txt"],
                        )

```

4. 启动对话界面
```python
brain.print_info()

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from quivr_core.config import RetrievalConfig

config_file_name = "./basic_rag_workflow.yaml"

retrieval_config = RetrievalConfig.from_yaml(config_file_name)

console = Console()
console.print(Panel.fit("Ask your brain !", style="bold magenta"))

while True:
    # Get user input
    question = Prompt.ask("[bold cyan]Question[/bold cyan]")

    # Check if user wants to exit
    if question.lower() == "exit":
        console.print(Panel("Goodbye!", style="bold yellow"))
        break

    answer = brain.ask(question, retrieval_config=retrieval_config)
    # Print the answer with typing effect
    console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

    console.print("-" * console.width)

brain.print_info()
```

5. 现在你已准备就绪，可以通过修改配置文件来测试不同的检索策略并与你的“大脑”对话！

## 进阶使用

你可以通过添加网络搜索、集成工具等功能进一步扩展 Quivr。更多详情请查阅[官方文档](https://core.quivr.com/)。


## 贡献者名单 ✨

感谢以下这些优秀的贡献者：
<a href="https://github.com/quivrhq/quivr/graphs/contributors">
<img src="https://contrib.rocks/image?repo=quivrhq/quivr" />
</a>

## 参与贡献 🤝

如果你有 Pull Request（PR），请提交，我们会尽快进行审查。查看我们的项目看板[这里](https://github.com/users/StanGirard/projects/5)，了解我们当前的工作重点，并随时将你的新想法带入讨论！

- [Open Issues](https://github.com/quivrhq/quivr/issues)
- [Open Pull Requests](https://github.com/quivrhq/quivr/pulls)
- [Good First Issues](https://github.com/quivrhq/quivr/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)

## 合作伙伴 ❤️

本项目的顺利推进离不开各位合作伙伴的支持。感谢你们的鼎力相助！


<a href="https://ycombinator.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Y_Combinator_logo.svg/1200px-Y_Combinator_logo.svg.png" alt="YCombinator" style="padding: 10px" width="70px">
</a>
<a href="https://www.theodo.fr/">
  <img src="https://avatars.githubusercontent.com/u/332041?s=200&v=4" alt="Theodo" style="padding: 10px" width="70px">
</a>

## 开源许可证 📄

本项目采用 Apache 2.0 许可证进行授权 - 详情请参阅 [LICENSE](LICENSE) 文件。