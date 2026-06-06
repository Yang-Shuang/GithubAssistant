# ![PandasAI](assets/logo.png)

[![Release](https://img.shields.io/pypi/v/pandasai?label=Release&style=flat-square)](https://pypi.org/project/pandasai/)
[![CI](https://github.com/sinaptik-ai/pandas-ai/actions/workflows/ci-core.yml/badge.svg)](https://github.com/sinaptik-ai/pandas-ai/actions/workflows/ci-core.yml/badge.svg)
[![CD](https://github.com/sinaptik-ai/pandas-ai/actions/workflows/cd.yml/badge.svg)](https://github.com/sinaptik-ai/pandas-ai/actions/workflows/cd.yml/badge.svg)
[![Coverage](https://codecov.io/gh/sinaptik-ai/pandas-ai/branch/main/graph/badge.svg)](https://codecov.io/gh/sinaptik-ai/pandas-ai)
[![Discord](https://dcbadge.vercel.app/api/server/kF7FqH2FwS?style=flat&compact=true)](https://discord.gg/KYKj9F2FRH)
[![Downloads](https://static.pepy.tech/badge/pandasai)](https://pepy.tech/project/pandasai) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZnO-njhL7TBOYPZaqvMvGtsjckZKrv2E?usp=sharing)

PandasAI 是一个 Python 库，让你能够用自然语言轻松地向数据提问。它帮助非技术用户以更直观的方式与数据进行交互，同时帮助技术用户在处理数据时节省时间和精力。

# 🔧 快速开始

你可以在[这里](https://docs.pandas-ai.com/)找到 PandasAI 的完整文档。


## 📚 使用指南

### Python 环境要求

Python version `3.8+ <=3.11`

### 📦 安装

你可以通过 pip 或 poetry 安装 PandasAI 库。

使用 pip：

```bash
pip install pandasai
pip install pandasai-litellm
```

使用 poetry：

```bash
poetry add pandasai
poetry add pandasai-litellm
```

### 💻 使用示例

#### 提问

```python
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM

# Initialize LiteLLM with your OpenAI model
llm = LiteLLM(model="gpt-4.1-mini", api_key="YOUR_OPENAI_API_KEY")

# Configure PandasAI to use this LLM
pai.config.set({
    "llm": llm
})

# Load your data
df = pai.read_csv("data/companies.csv")

response = df.chat("What is the average revenue by region?")
print(response)
```

---

或者你可以提出更复杂的问题：

```python
df.chat(
    "What is the total sales for the top 3 countries by sales?"
)
```

```
The total sales for the top 3 countries by sales is 16500.
```

#### 可视化图表

你也可以让 PandasAI 为你生成图表：

```python
df.chat(
    "Plot the histogram of countries showing for each one the gdp. Use different colors for each bar",
)
```

![Chart](assets/histogram-chart.png?raw=true)

#### 使用多个 DataFrame

你还可以向 PandasAI 传入多个 DataFrame，并询问它们之间的关联问题。

```python
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM

# Initialize LiteLLM with your OpenAI model
llm = LiteLLM(model="gpt-4.1-mini", api_key="YOUR_OPENAI_API_KEY")

# Configure PandasAI to use this LLM
pai.config.set({
    "llm": llm
})

employees_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    'Department': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

salaries_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Salary': [5000, 6000, 4500, 7000, 5500]
}

employees_df = pai.DataFrame(employees_data)
salaries_df = pai.DataFrame(salaries_data)


pai.chat("Who gets paid the most?", employees_df, salaries_df)
```

```
Olivia gets paid the most.
```

#### Docker 沙箱环境

你可以在 Docker 沙箱环境中运行 PandasAI，提供一个安全、隔离的环境来执行代码，从而降低恶意攻击的风险。

##### Python 环境要求

```bash
pip install "pandasai-docker"
```

##### 使用示例

```python
import pandasai as pai
from pandasai_docker import DockerSandbox
from pandasai_litellm.litellm import LiteLLM

# Initialize LiteLLM with your OpenAI model
llm = LiteLLM(model="gpt-4.1-mini", api_key="YOUR_OPENAI_API_KEY")

# Configure PandasAI to use this LLM
pai.config.set({
    "llm": llm
})

# Initialize the sandbox
sandbox = DockerSandbox()
sandbox.start()

employees_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    'Department': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

salaries_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Salary': [5000, 6000, 4500, 7000, 5500]
}

employees_df = pai.DataFrame(employees_data)
salaries_df = pai.DataFrame(salaries_data)

pai.chat("Who gets paid the most?", employees_df, salaries_df, sandbox=sandbox)

# Don't forget to stop the sandbox when done
sandbox.stop()
```

```
Olivia gets paid the most.
```

你可以在 [examples](examples) 目录中找到更多示例。

## 📜 许可证

PandasAI 基于 MIT 开源协议发布，但本仓库的 `pandasai/ee` 目录除外，其[许可证请参见此处](https://github.com/sinaptik-ai/pandas-ai/blob/main/ee/LICENSE)。

如果你对托管版 PandasAI Cloud 或企业级私有化部署方案感兴趣，请[联系我们](https://pandas-ai.com)。

## 资源链接

- [官方文档](https://docs.pandas-ai.com/)：获取全面的使用指南
- [示例代码](examples)：包含示例笔记本（Notebooks）
- [Discord](https://discord.gg/KYKj9F2FRH)：与社区成员及 PandasAI 团队交流讨论

## 🤝 贡献指南

欢迎贡献代码！请查看现有的待办 Issue，并随时提交 Pull Request。
更多详细信息，请参阅[贡献指南](CONTRIBUTING.md)。

### 感谢所有贡献者！

[![Contributors](https://contrib.rocks/image?repo=sinaptik-ai/pandas-ai)](https://github.com/sinaptik-ai/pandas-ai/graphs/contributors)