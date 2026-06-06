<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="docs/images/crewai_logo.png" width="600px" alt="Open source Multi-AI Agent orchestration framework">
  </a>
</p>
<p align="center" style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <a href="https://trendshift.io/repositories/11239" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/11239" alt="crewAIInc%2FcrewAI | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <a href="https://crewai.com">官网</a>
  ·
  <a href="https://docs.crewai.com">文档</a>
  ·
  <a href="https://app.crewai.com">开始免费试用 Cloud</a>
  ·
  <a href="https://blog.crewai.com">博客</a>
  ·
  <a href="https://community.crewai.com">社区论坛</a>
</p>

<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="https://img.shields.io/github/stars/crewAIInc/crewAI" alt="GitHub Repo stars">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/network/members">
    <img src="https://img.shields.io/github/forks/crewAIInc/crewAI" alt="GitHub forks">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/issues">
    <img src="https://img.shields.io/github/issues/crewAIInc/crewAI" alt="GitHub issues">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/pulls">
    <img src="https://img.shields.io/github/issues-pr/crewAIInc/crewAI" alt="GitHub pull requests">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  </a>
</p>

<p align="center">
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/v/crewai" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/dm/crewai" alt="PyPI downloads">
  </a>
  <a href="https://twitter.com/crewAIInc">
    <img src="https://img.shields.io/twitter/follow/crewAIInc?style=social" alt="Twitter Follow">
  </a>
</p>

### 快速且灵活的多智能体自动化框架

> CrewAI 是一个轻量、极速的 Python 框架，完全从零构建——**独立于 LangChain 或其他智能体（Agent）框架**。它为开发者提供了高层级的简洁性与低层级的精确控制，非常适合创建面向各种场景的自主 AI 智能体。

- **CrewAI Crews（团队）**：优化自主性与协同智能。
- **CrewAI Flows（工作流）**：**企业与生产级架构**，用于构建和部署多智能体系统。提供细粒度的事件驱动控制、单次大语言模型调用以实现精确的任务编排，并原生支持 Crews。

通过 [learn.crewai.com](https://learn.crewai.com) 上的社区课程，已有超过 10 万名开发者获得认证，CrewAI 正迅速成为企业级 AI 自动化的标准选择。

# CrewAI AMP 套件

CrewAI AMP 套件是一套专为需要安全、可扩展且易于管理的智能体驱动自动化而设计的综合方案。

你可以免费试用该套件的一部分：[Crew Control Plane](https://app.crewai.com)

## Crew Control Plane（控制平面）核心功能：

- **追踪与可观测性**：实时监控和跟踪你的 AI 智能体与工作流，包括指标、日志和链路追踪。
- **统一控制平面**：集中管理平台，用于管理、监控和扩展你的 AI 智能体与工作流。
- **无缝集成**：轻松连接现有企业系统、数据源和云基础设施。
- **高级安全性**：内置强大的安全与合规措施，确保部署与管理的安全。
- **可操作洞察**：实时分析与报告，优化性能与决策制定。
- **全天候支持**：专属企业级技术支持，确保不间断运行并快速解决问题。
- **本地与云部署选项**：根据你的安全与合规需求，选择将 CrewAI AMP 部署在本地或云端。

CrewAI AMP 专为寻求强大、可靠解决方案的企业设计，旨在将复杂的业务流程转化为高效、智能的自动化系统。

## 目录

- [使用 AI 进行开发](#build-with-ai)
- [为什么选择 CrewAI？](#why-crewai)
- [快速开始](#getting-started)
- [核心功能](#key-features)
- [理解 Flows 与 Crews](#understanding-flows-and-crews)
- [CrewAI 对比 LangGraph](#how-crewai-compares)
- [示例](#examples)
  - [快速教程](#quick-tutorial)
  - [编写职位描述](#write-job-descriptions)
  - [旅行规划器](#trip-planner)
  - [股票分析](#stock-analysis)
  - [结合使用 Crews 与 Flows](#using-crews-and-flows-together)
- [将你的 Crew 连接到模型](#connecting-your-crew-to-a-model)
- [与其他框架的对比](#how-crewai-compares)
- [常见问题解答（FAQ）](#frequently-asked-questions-faq)
- [贡献指南](#contribution)
- [遥测数据（Telemetry）](#telemetry)
- [许可证](#license)

## 使用 AI 进行开发

正在使用 AI 编程智能体？一条命令即可教会它 CrewAI 的最佳实践：

**Claude Code：**
```shell
/plugin marketplace add crewAIInc/skills
/plugin install crewai-skills@crewai-plugins
/reload-plugins
```
当你提出相关 CrewAI 问题时，将自动激活以下四项技能：

| 技能 | 触发时机 |
|-------|--------------|
| `getting-started` | 搭建新项目脚手架，在 `LLM.call()` / `Agent` / `Crew` / `Flow` 间做出选择，配置 `crew.py` / `main.py` |
| `design-agent` | 配置智能体 —— 角色、目标、背景故事、工具、大语言模型、记忆机制、安全护栏（guardrails） |
| `design-task` | 编写任务描述、依赖关系、结构化输出（`output_pydantic`, `output_json`）、人工审核流程 |
| `ask-docs` | 查询实时 [CrewAI 文档 MCP 服务器](https://docs.crewai.com/mcp) 以获取最新的 API 详情 |

**Cursor、Codex、Windsurf 及其他工具（[skills.sh](https://skills.sh/crewaiinc/skills)）：**
```shell
npx skills add crewaiinc/skills
```

这将安装官方的 [CrewAI Skills](https://github.com/crewAIInc/skills) ——一套结构化指令，用于指导编程智能体如何搭建 Flows、配置 Crews、设计智能体与任务，并遵循 CrewAI 规范。

## 为什么选择 CrewAI？

<div align="center" style="margin-bottom: 30px;">
  <img src="docs/images/asset.png" alt="CrewAI Logo" width="100%">
</div>

CrewAI 释放了多智能体自动化的真正潜力，在速度、灵活性与控制力方面提供业界领先的组合，支持 AI Agent 团队（Crews）或事件驱动工作流（Flows）：

- **独立框架**：完全从零构建，不依赖 LangChain 或其他智能体框架。
- **高性能**：针对速度与资源占用进行优化，实现更快的执行效率。
- **灵活的底层自定义**：在高层与低层均享有完全的自由度——从整体工作流和系统架构，到细粒度的智能体行为、内部提示词及执行逻辑均可定制。
- **适用于所有场景**：已验证在简单任务与复杂的真实企业级场景中均表现出色。
- **活跃的社区**：拥有超过 **10 万名认证开发者**的快速成长型社区，提供全面的支持与资源。

CrewAI 赋能开发者与企业自信地构建智能自动化系统，在简洁性、灵活性与性能之间取得完美平衡。

## 快速开始

按照本教程设置并运行你的第一个 CrewAI 智能体。

[![CrewAI Getting Started Tutorial](https://img.youtube.com/vi/-kSOTtYzgEw/hqdefault.jpg)](https://www.youtube.com/watch?v=-kSOTtYzgEw "CrewAI Getting Started Tutorial")

###

学习资源

通过我们的综合课程学习 CrewAI：

- [使用 CrewAI 构建多智能体系统](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - 掌握多智能体系统的核心基础
- [实践多智能体与高级用例](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/) - 深入探索高级实现方案

### 理解 Flows 与 Crews

CrewAI 提供两种强大且互补的方法，无缝协作以构建复杂的 AI 应用：

1. **Crews（智能体团队）**：具备真正自主性与行动权的 AI 智能体团队，通过基于角色的协作共同完成复杂任务。Crews 支持以下特性：
   - 智能体间自然、自主的决策机制
   - 动态的任务委派与协作
   - 具有明确目标与专业能力的专属角色
   - 灵活的问题解决策略

2. **Flows（工作流）**：面向生产环境的事件驱动型工作流，提供对复杂自动化的精确控制。Flows 提供以下特性：
   - 针对真实场景执行路径的细粒度控制
   - 任务间安全且一致的状态管理
   - 智能体与生产级 Python 代码的无缝集成
   - 支持复杂业务逻辑的条件分支

当结合使用 Crews 和 Flows 时，CrewAI 的真正威力得以展现。这种协同效应让你能够：
- 构建复杂的、生产级应用
- 在自主性与精确控制间取得平衡
- 应对复杂的真实场景
- 保持清晰且易于维护的代码结构

### 安装与入门

按照以下步骤快速上手 CrewAI：

### 1. 安装依赖项

确保你的系统已安装 Python >=3.10 且 <3.14。CrewAI 使用 [UV](https://docs.astral.sh/uv/) 进行依赖管理与包处理，提供无缝的安装与执行体验。

首先，安装 CrewAI：

```shell
uv pip install crewai
```

若想同时安装 `crewai` 包及其可选功能（包含智能体所需的额外工具），可使用以下命令：

```shell
uv pip install 'crewai[tools]'
```

上述命令将安装基础包，并添加需要更多依赖才能正常运行的附加组件。

### 依赖项故障排除

如果在安装或使用过程中遇到问题，可参考以下常见解决方案：

#### 常见问题

1. **ModuleNotFoundError: No module named 'tiktoken'**（未找到模块）
   - 显式安装 tiktoken：`uv pip install 'crewai[embeddings]'`
   - 若使用 embedchain 或其他工具：`uv pip install 'crewai[tools]'`

2. **tiktoken 构建 wheel 失败**
   - 确保已安装 Rust 编译器（参考上述步骤）
   - Windows 用户：请确认已安装 Visual C++ Build Tools
   - 尝试升级 pip：`uv pip install --upgrade pip`
   - 若问题依旧，请使用预编译的 wheel 包：`uv pip install tiktoken --prefer-binary`

### 2. 使用 YAML 配置创建你的 Crew

要创建新的 CrewAI 项目，请运行以下 CLI（命令行界面）命令：

```shell
crewai create crew <project_name>
```

该命令将创建一个包含以下结构的新项目文件夹：

```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

你现在可以通过编辑 `src/my_project` 文件夹中的文件来开发你的 Crew。其中，`main.py` 是项目入口点，`crew.py` 用于定义 Crew，`agents.yaml` 用于定义智能体，`tasks.yaml` 用于定义任务。

#### 自定义项目配置：

- 修改 `src/my_project/config/agents.yaml` 以定义你的智能体。
- 修改 `src/my_project/config/tasks.yaml` 以定义你的任务。
- 修改 `src/my_project/crew.py` 添加你自己的逻辑、工具和特定参数。
- 修改 `src/my_project/main.py` 为智能体和任务添加自定义输入。
- 将环境变量添加到 `.env` 文件中。

#### 顺序执行流程的简单 Crew 示例：

实例化你的 Crew：

```shell
crewai create crew latest-ai-development
```

根据实际需求修改文件内容：

**agents.yaml**

```yaml
# src/my_project/config/agents.yaml
researcher:
  role: >
    {topic} 高级数据研究员
  goal: >
    挖掘 {topic} 领域的尖端技术进展
  backstory: >
    你是一位经验丰富的研究员，擅长发掘 {topic} 领域的最新动态。以能够找到最相关的信息并以清晰简洁的方式呈现而闻名。

reporting_analyst:
  role: >
    {topic} 报告分析师
  goal: >
    基于 {topic} 的数据分析与研究结果创建详细报告
  backstory: >
    你是一位注重细节的分析师，以敏锐的观察力著称。擅长将复杂数据转化为清晰简洁的报告，使他人易于理解并据此采取行动。
```

**tasks.yaml**

````yaml
# src/my_project/config/tasks.yaml
research_task:
  description: >
    对 {topic} 进行彻底的研究
    确保找到任何有趣且相关的信息，注意当前年份为 2025 年。
  expected_output: >
    一份包含 10 个要点的列表，列出关于 {topic} 的最相关信息
  agent: researcher

reporting_task:
  description: >
    审查你获取的上下文信息，并将每个主题扩展为报告中的完整章节。
    确保报告内容详实，包含所有相关细节。
  expected_output: >
    一份完整的报告，涵盖主要主题，每个主题均有完整的详细信息章节。
    格式化为 Markdown，但不使用 '```' 代码块包裹。
  agent: reporting_analyst
  output_file: report.md
````

**crew.py**

```python
# src/my_project/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopmentCrew():
	"""LatestAiDevelopment crew"""
	agents: List[BaseAgent]
	tasks: List[Task]

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			tools=[SerperDevTool()]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the LatestAiDevelopment crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
```

**main.py**

```python
#!/usr/bin/env python
# src/my_project/main.py
import sys
from latest_ai_development.crew import LatestAiDevelopmentCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI Agents'
    }
    LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
```

### 3. 运行你的 Crew

在运行 Crew 之前，请确保在 `.env` 文件中已设置以下环境变量：

- [OpenAI API 密钥](https://platform.openai.com/account/api-keys)（或其他大语言模型 API 密钥）：`OPENAI_API_KEY=sk-...`
- [Serper.dev](https://serper.dev/) API 密钥：`SERPER_API_KEY=YOUR_KEY_HERE`

使用 CLI 命令锁定并安装依赖项。首先，进入你的项目目录：

```shell
cd my_project
crewai install (Optional)
```

要在项目中运行 Crew，请在根目录下执行以下命令：

```bash
crewai run
```

或

```bash
python src/my_project/main.py
```

如果因 Poetry 使用问题导致错误，请运行以下命令更新你的 crewai 包：

```bash
crewai update
```

你将在控制台看到输出结果，并且项目根目录下会生成包含完整最终报告的 `report.md` 文件。

除了顺序执行流程外，你还可以使用分层（hierarchical）流程。该流程会自动为定义的 Crew 分配一名管理者，通过委派和结果验证来妥善协调任务的规划与执行。[在此了解更多关于流程的信息](https://docs.crewai.com/core-concepts/Processes/)。

## 核心功能

CrewAI 作为一个轻量、独立的高性能多 AI 智能体框架脱颖而出，提供简洁性、灵活性与精确控制——摆脱其他智能体框架的复杂性与限制。

- **独立且轻量**：完全独立于 LangChain 等其他框架，执行速度更快，资源占用更低。
- **灵活且精准**：通过直观的 [Crews](https://docs.crewai.com/concepts/crews) 或精确的 [Flows](https://docs.crewai.com/concepts/flows) 轻松编排自主智能体，完美契合你的需求。
- **无缝集成**： effortlessly（轻松）结合 Crews（自主性）与 Flows（精准控制），创建复杂的真实世界自动化系统。
- **深度自定义**：从高层工作流到底层内部提示词和智能体行为，定制每一个环节。
- **可靠性能**：在简单任务与企业级复杂自动化中均保持一致的优异表现。
- **活跃社区**：拥有完善的文档支持与超过 10 万名认证开发者，提供卓越的技术支持与指导。

选择 CrewAI，轻松构建强大、灵活且面向生产环境的 AI 自动化系统。

## 示例

你可以在 [CrewAI-examples 仓库](https://github.com/crewAIInc/crewAI-examples?tab=readme-ov-file) 中测试不同的真实 AI Crew 案例：

- [落地页生成器](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator)
- [在执行过程中引入人工输入](https://docs.crewai.com/how-to/Human-Input-on-Execution)
- [旅行规划器](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner)
- [股票分析](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis)

### 快速教程

[![CrewAI Tutorial](https://img.youtube.com/vi/tnejrr-0a94/maxresdefault.jpg)](https://www.youtube.com/watch?v=tnejrr-0a94 "CrewAI Tutorial")

### 编写职位描述

[查看此示例的代码](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/job-posting) 或观看下方视频：

[![Jobs postings](https://img.youtube.com/vi/u98wEMz-9to/maxresdefault.jpg)](https://www.youtube.com/watch?v=u98wEMz-9to "Jobs postings")

### 旅行规划器

[查看此示例的代码](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner) 或观看下方视频：

[![Trip Planner](https://img.youtube.com/vi/xis7rWp-hjs/maxresdefault.jpg)](https://www.youtube.com/watch?v=xis7rWp-hjs "Trip Planner")

### 股票分析

[查看此示例的代码](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis) 或观看下方视频：

[![Stock Analysis](https://img.youtube.com/vi/e0Uj4yWdaAg/maxresdefault.jpg)](https://www.youtube.com/watch?v=e0Uj4yWdaAg "Stock Analysis")

### 结合使用 Crews 与 Flows

当将 Crews 与 Flows 结合使用时，CrewAI 的真正威力得以充分展现。
CrewAI Flows 支持使用 `or_` 和 `and_` 等逻辑运算符组合多个条件。这些运算符可与 `@start`、`@listen` 或 `@router` 装饰器配合使用，以创建复杂的触发条件。

- `or_`：当满足任一指定条件时触发。
- `and_`：当所有指定条件均被满足时触发。

以下示例展示了如何在 Flows 中编排多个 Crews：

```python
from crewai.flow.flow import Flow, listen, start, router, or_
from crewai import Crew, Agent, Task, Process
from pydantic import BaseModel

# Define structured state for precise control
class MarketState(BaseModel):
    sentiment: str = "neutral"
    confidence: float = 0.0
    recommendations: list = []

class AdvancedAnalysisFlow(Flow[MarketState]):
    @start()
    def fetch_market_data(self):
        # Demonstrate low-level control with structured state
        self.state.sentiment = "analyzing"
        return {"sector": "tech", "timeframe": "1W"}  # These parameters match the task description template

    @listen(fetch_market_data)
    def analyze_with_crew(self, market_data):
        # Show crew agency through specialized roles
        analyst = Agent(
            role="Senior Market Analyst",
            goal="Conduct deep market analysis with expert insight",
            backstory="You're a veteran analyst known for identifying subtle market patterns"
        )
        researcher = Agent(
            role="Data Researcher",
            goal="Gather and validate supporting market data",
            backstory="You excel at finding and correlating multiple data sources"
        )

        analysis_task = Task(
            description="Analyze {sector} sector data for the past {timeframe}",
            expected_output="Detailed market analysis with confidence score",
            agent=analyst
        )
        research_task = Task(
            description="Find supporting data to validate the analysis",
            expected_output="Corroborating evidence and potential contradictions",
            agent=researcher
        )

        # Demonstrate crew autonomy
        analysis_crew = Crew(
            agents=[analyst, researcher],
            tasks=[analysis_task, research_task],
            process=Process.sequential,
            verbose=True
        )
        return analysis_crew.kickoff(inputs=market_data)  # Pass market_data as named inputs

    @router(analyze_with_crew)
    def determine_next_steps(self):
        # Show flow control with conditional routing
        if self.state.confidence > 0.8:
            return "high_confidence"
        elif self.state.confidence > 0.5:
            return "medium_confidence"
        return "low_confidence"

    @listen("high_confidence")
    def execute_strategy(self):
        # Demonstrate complex decision making
        strategy_crew = Crew(
            agents=[
                Agent(role="Strategy Expert",
                      goal="Develop optimal market strategy")
            ],
            tasks=[
                Task(description="Create detailed strategy based on analysis",
                     expected_output="Step-by-step action plan")
            ]
        )
        return strategy_crew.kickoff()

    @listen(or_("medium_confidence", "low_confidence"))
    def request_additional_analysis(self):
        self.state.recommendations.append("Gather more data")
        return "Additional analysis required"
```

本示例演示了如何：

1. 使用 Python 代码进行基础数据操作
2. 将 Crews 创建并作为工作流中的步骤执行
3. 使用 Flows 装饰器管理操作流程顺序
4. 根据 Crew 结果实现条件分支逻辑

## 将你的 Crew 连接到模型

CrewAI 支持通过多种连接选项使用不同的 LLM。默认情况下，智能体在查询模型时将使用 OpenAI API。不过还有其他方式可以让智能体连接到模型。例如，你可以通过 Ollama 工具配置智能体使用本地模型。

有关配置智能体连接模型的详细信息，请参阅 [将 CrewAI 连接到 LLMs](https://docs.crewai.com/how-to/LLM-Connections/) 页面。

## 与其他框架的对比

**CrewAI 的优势**：CrewAI 通过独特的 Crews 和 Flows 架构，将自主智能体智能与精确的工作流控制相结合。该框架在高层编排与底层自定义方面均表现出色，能够以细粒度控制构建复杂的、生产级系统。

- **LangGraph**：虽然 LangGraph 为构建智能体工作流提供了基础，但其方法需要大量的样板代码和复杂的状态管理模式。该框架与 LangChain 的深度耦合在实现自定义智能体行为或与外部系统集成时可能限制灵活性。

_P.S. CrewAI 相比 LangGraph 展现出显著的性能优势，在某些场景（如 QA 任务示例）中执行速度快达 5.76 倍（[查看对比](https://github.com/crewAIInc/crewAI-examples/tree/main/Notebooks/CrewAI%20Flows%20%26%20Langgraph/QA%20Agent)），在某些编程任务中也以更快的完成时间获得了更高的评估分数（[详细分析](https://github.com/crewAIInc/crewAI-examples/blob/main/Notebooks/CrewAI%20Flows%20%26%20Langgraph/Coding%20Assistant/coding_assistant_eval.ipynb)）。_

- **Autogen**：虽然 Autogen 擅长创建能够协同工作的对话型智能体，但它缺乏内置的流程概念。在 Autogen 中，编排智能体的交互需要额外的编程工作，随着任务规模的增长，这可能会变得复杂且繁琐。
- **ChatDev**：ChatDev 将流程概念引入 AI 智能体领域，但其实现方式较为僵化。ChatDev 的自定义能力有限，且未针对生产环境进行优化，这可能会在实际应用中限制可扩展性与灵活性。

## 贡献指南

CrewAI 是开源项目，我们欢迎社区贡献。如果你希望参与贡献，请：

- Fork（克隆）本仓库。
- 为你的新功能创建分支。
- 添加你的功能或改进内容。
- 提交 Pull Request。
- 感谢你的贡献！

### 安装依赖项

```bash
uv lock
uv sync
```

### 虚拟环境

```bash
uv venv
```

### 预提交钩子（Pre-commit hooks）

```bash
pre-commit install
```

### 运行测试

```bash
uv run pytest .
```

### 运行静态类型检查

```bash
uvx mypy src
```

### 打包构建

```bash
uv build
```

### 本地安装

```bash
uv pip install dist/*.tar.gz
```

## 遥测数据（Telemetry）

CrewAI 使用匿名遥测技术收集使用数据，主要目的是帮助我们集中精力优化最常用功能、集成与工具。

需要明确的是，除非满足特定条件，否则**不会收集**任何关于提示词、任务描述、智能体背景故事或目标、工具使用情况、API 调用及响应、智能体处理的数据、以及密钥和环境变量的数据。当启用 `share_crew` 功能时，为了提供更深入的洞察，会收集包括任务描述、智能体背景故事或目标及其他特定属性在内的详细数据，同时严格尊重用户隐私。用户可以通过设置环境变量 `OTEL_SDK_DISABLED=true` 来禁用遥测功能。

收集的遥测数据包括：

- CrewAI 版本
  - 了解最新版本的活跃用户数量
- Python 版本
  - 决定优先支持哪些版本
- 操作系统类型及基本信息（如 CPU 核心数、macOS/Windows/Linux）
  - 以便聚焦重点系统并开发相关特性
- Crew 中的智能体与任务数量
  - 确保内部测试用例与实际使用场景一致，并向开发者普及最佳实践
- 使用的 Crew 流程类型
  - 明确优化方向
- 智能体是否启用记忆或委派功能
  - 评估功能改进价值或是否需要下线
- 任务执行方式（并行还是顺序）
  - 决定是否需要加强并行执行支持
- 使用的语言模型
  - 优化主流模型的兼容性与支持
- Crew 中智能体的角色分布
  - 了解高层使用场景，以便构建更好的工具、集成与示例
- 可用的工具名称
  - 了解哪些公开工具使用频率最高，以便优先进行优化

用户可通过在 Crews 中将 `share_crew` 属性设置为 `True` 选择加入更详细的遥测数据共享。启用 `share_crew` 将收集包括任务 `goal`、`backstory`、`context` 和 `output` 在内的详细执行数据，从而在尊重用户意愿的前提下提供更深度的使用洞察。

## 许可证

CrewAI 基于 [MIT 许可证](https://github.com/crewAIInc/crewAI/blob/main/LICENSE) 发布。

## 常见问题解答（FAQ）

### 通用问题
- [CrewAI 到底是什么？](#q-what-exactly-is-crewai)
- [如何安装 CrewAI？](#q-how-do-i-install-crewai)
- [CrewAI 是否依赖 LangChain？](#q-does-crewai-depend-on-langchain)
- [CrewAI 是开源的吗？](#q-is-crewai-open-source)
- [CrewAI 会收集用户数据吗？](#q-does-crewai-collect-data-from-users)

### 功能与能力
- [CrewAI 能处理复杂用例吗？](#q-can-crewai-handle-complex-use-cases)
- [我可以在本地 AI 模型上使用 CrewAI 吗？](#q-can-i-use-crewai-with-local-ai-models)
- [Crews 与 Flows 有什么区别？](#q-what-makes-crews-different-from-flows)
- [CrewAI 相比 LangChain 有哪些优势？](#q-how-is-crewai-better-than-langchain)
- [CrewAI 支持微调或训练自定义模型吗？](#q-does-crewai-support-fine-tuning-or-training-custom-models)

### 资源与社区
- [在哪里可以找到真实的 CrewAI 示例？](#q-where-can-i-find-real-world-crewai-examples)
- [我如何为 CrewAI 做出贡献？](#q-how-can-i-contribute-to-crewai)

### 企业级功能
- [CrewAI AMP 提供了哪些额外功能？](#q-what-additional-features-does-crewai-amp-offer)
- [CrewAI AMP 支持云端和本地部署吗？](#q-is-crewai-amp-available-for-cloud-and-on-premise-deployments)
- [我可以免费试用 CrewAI AMP 吗？](#q-can-i-try-crewai-amp-for-free)

### Q：CrewAI 到底是什么？
A：CrewAI 是一个独立、轻量且快速的 Python 框架，专为编排自主 AI 智能体而设计。与 LangChain 等框架不同，CrewAI 不依赖外部组件，因此更加轻量、快速且简洁。

### Q：如何安装 CrewAI？
A：使用命令安装 CrewAI：

```shell
uv pip install crewai
```

如需额外工具，请使用：

```shell
uv pip install 'crewai[tools]'
```

### Q：CrewAI 是否依赖 LangChain？
A：不依赖。CrewAI 完全从零构建，没有任何对 LangChain 或其他智能体框架的依赖。这确保了轻量、快速且灵活的体验。

### Q：CrewAI 能处理复杂用例吗？
A：可以。CrewAI 在简单任务和复杂的真实场景中均表现出色，提供从内部提示词到高级工作流编排的高层与底层深度自定义选项。

### Q：我可以在本地 AI 模型上使用 CrewAI 吗？
A：完全可以！CrewAI 支持多种语言模型，包括本地模型。Ollama 和 LM Studio 等工具可实现无缝集成。详见 [LLM 连接文档](https://docs.crewai.com/how-to/LLM-Connections/)。

### Q：Crews 与 Flows 有什么区别？
A：Crews 提供自主的智能体协作，适合需要灵活决策和动态交互的任务。Flows 提供精确的事件驱动控制，适合管理详细的执行路径和安全的状态管理。你可以无缝结合两者以实现最佳效果。

### Q：CrewAI 相比 LangChain 有哪些优势？
A：CrewAI 提供更简单直观的 API、更快的执行速度、更稳定一致的结果、完善的文档以及活跃的社区——有效解决了 LangChain 常见的批评与局限性。

### Q：CrewAI 是开源的吗？
A：是的，CrewAI 是开源项目，并积极鼓励社区贡献与协作。

### Q：CrewAI 会收集用户数据吗？
A：CrewAI 仅收集匿名遥测数据用于改进产品。除非用户明确启用，否则绝不会收集提示词、任务或 API 响应等敏感数据。

### Q：在哪里可以找到真实的 CrewAI 示例？
A：请查看 [CrewAI-examples 仓库](https://github.com/crewAIInc/crewAI-examples)，其中包含旅行规划器、股票分析和职位描述等实用案例。

### Q：我如何为 CrewAI 做出贡献？
A：我们热烈欢迎贡献！Fork 本仓库，创建你的分支，实现更改并提交 Pull Request。详见 README 中的“贡献指南”部分以获取详细说明。

### Q：CrewAI AMP 提供了哪些额外功能？
A：CrewAI AMP 提供高级功能，包括统一控制平面、实时可观测性、安全集成、高级安全性、可操作洞察以及专属的 24/7 企业支持。

### Q：CrewAI AMP 支持云端和本地部署吗？
A：是的，CrewAI AMP 同时支持云服务和本地部署选项，帮助企业满足特定的安全与合规要求。

### Q：我可以免费试用 CrewAI AMP 吗？
A：可以，你可以免费访问 [Crew Control Plane](https://app.crewai.com) 体验部分 CrewAI AMP 套件功能。

### Q：CrewAI 支持微调或训练自定义模型吗？
A：是的，CrewAI 可集成经过自定义训练或微调的模型，让你能够利用领域特定知识提升智能体的表现与准确性。

### Q：CrewAI 智能体能否与外部工具和 API 交互？
A：完全可以！CrewAI 智能体可以轻松集成外部工具、API 和数据库，使其能够充分利用现实世界的数据和资源。

### Q：CrewAI 是否适用于生产环境？
A：是的，CrewAI 明确按照生产级标准设计，确保企业部署的可靠性、稳定性和可扩展性。

### Q：CrewAI 的可扩展性如何？
A：CrewAI 具有高度可扩展性，支持从简单自动化到涉及大量智能体和复杂任务的大型企业工作流。

### Q：CrewAI 提供调试和监控工具吗？
A：是的，CrewAI AMP 包含高级调试、链路追踪和实时可观测性功能，简化你的自动化系统管理与故障排查。

### Q：CrewAI 支持哪些编程语言？
A：CrewAI 主要基于 Python，但通过其灵活的 API 集成能力，可轻松与任何编程语言编写的服务和 API 进行交互。

### Q：CrewAI 是否提供面向初学者的教育资源？
A：是的，CrewAI 通过 learn.crewai.com 提供丰富的初学者教程、课程和文档，支持不同技能水平的开发者。

### Q：CrewAI 能否自动化“人在回路”（Human-in-the-loop）工作流？
A：可以，CrewAI 完全支持人在回路的工作流模式，允许人类专家与 AI 智能体无缝协作，从而提升决策质量。