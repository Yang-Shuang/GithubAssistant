<div align="center"><b><a href="README.md">English</a> | <a href="readme_CN.md">简体中文</a> | <a href="readme_JP.md">日本語</a> | <a href="readme_PT_BR.md">Português (Brasil)</a> | <a href="readme_KO.md">한국어</a><br><a href="readme_ES.md">Español</a> | <a href="readme_FR.md">Français</a> | <a href="readme_DE.md">Deutsch</a> | <a href="readme_RU.md">Русский</a> | <a href="readme_AR.md">العربية</a> | <a href="readme_HI.md">हिन्दी</a> | <a href="readme_TR.md">Türkçe</a></b></div>


<h1 align="center" style="border-bottom: none">
    <div>
        <a href="https://www.comet.com/site/products/opik/?from=llm&utm_source=opik&utm_medium=github&utm_content=header_img&utm_campaign=opik"><picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/logo-dark-mode.svg">
            <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/opik-logo.svg">
            <img alt="Comet Opik logo" src="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/opik-logo.svg" width="200" />
        </picture></a>
        <br>
        Opik
    </div>
</h1>
<h2 align="center" style="border-bottom: none">开源的 AI 可观测性、评估与优化工具</h2>
<p align="center">
Opik 帮助你构建、测试和优化生成式 AI 应用，使其从原型到生产环境都能运行得更好。无论是 RAG 聊天机器人、代码助手还是复杂的智能体系统，Opik 都提供全面的追踪（tracing）、评估以及自动化的提示词和工具优化功能，让你摆脱在 AI 开发中的盲目摸索。
</p>

<div align="center">

[![Python SDK](https://img.shields.io/pypi/v/opik)](https://pypi.org/project/opik/)
[![License](https://img.shields.io/github/license/comet-ml/opik)](https://github.com/comet-ml/opik/blob/main/LICENSE)
[![Build](https://github.com/comet-ml/opik/actions/workflows/build_apps.yml/badge.svg)](https://github.com/comet-ml/opik/actions/workflows/build_apps.yml)
<!-- [![Quick Start](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/comet-ml/opik/blob/main/apps/opik-documentation/documentation/docs/cookbook/opik_quickstart.ipynb) -->

</div>

<p align="center">
    <a href="https://www.comet.com/site/products/opik/?from=llm&utm_source=opik&utm_medium=github&utm_content=website_button&utm_campaign=opik"><b>官网</b></a> •
    <a href="https://chat.comet.com"><b>Slack 社区</b></a> •
    <a href="https://x.com/Cometml"><b>Twitter</b></a> •
    <a href="https://www.comet.com/docs/opik/changelog"><b>更新日志</b></a> •
    <a href="https://www.comet.com/docs/opik/?from=llm&utm_source=opik&utm_medium=github&utm_content=docs_button&utm_campaign=opik"><b>文档</b></a>
</p>

<div align="center" style="margin-top: 1em; margin-bottom: 1em;">
<a href="#-what-is-opik">🚀 Opik 是什么？</a> • <a href="#%EF%B8%8F-opik-server-installation">🛠️ Opik 服务端安装</a> • <a href="#-opik-client-sdk">💻 Opik 客户端 SDK</a> • <a href="#-logging-traces-with-integrations">📝 通过集成记录追踪（Logging Traces）</a><br>
<a href="#-llm-as-a-judge-metrics">🧑‍⚖️ “LLM 作为裁判”指标</a> • <a href="#-evaluating-your-llm-application">🔍 评估你的应用</a> • <a href="#-star-us-on-github">⭐ 在 GitHub 上给我们点星（Star）</a> • <a href="#-contributing">🤝 参与贡献</a>
</div>

<br>

[![Opik platform screenshot (thumbnail)](readme-thumbnail-new.png)](https://www.comet.com/signup?from=llm&utm_source=opik&utm_medium=github&utm_content=readme_banner&utm_campaign=opik)

<a id="-what-is-opik"></a>
## 🚀 Opik 是什么？

Opik（由 [Comet](https://www.comet.com?from=llm&utm_source=opik&utm_medium=github&utm_content=what_is_opik_link&utm_campaign=opik) 打造）是一个开源平台，旨在简化 LLM 应用的全生命周期管理。它赋能开发者评估、测试、监控和优化他们的模型与智能体系统。核心功能包括：

- **全面的可观测性（Observability）**：深入追踪 LLM 调用、记录对话日志以及智能体活动。
- **高级评估功能**：强大的提示词评估、“LLM 作为裁判”机制以及实验管理。
- **生产就绪（Production-Ready）**：可扩展的监控仪表盘和用于生产环境的在线评估规则。
- **Opik Agent Optimizer（智能体优化器）**：专用的 SDK 和优化器套件，用于提升提示词和智能体的表现。
- **Opik Guardrails（护栏功能）**：帮助你实施安全且负责任的 AI 实践的功能特性。

<br>

核心能力包括：

- **开发与追踪**：
  - 在开发和生产环境中追踪所有 LLM 调用与详细上下文的追踪日志（[快速开始](https://www.comet.com/docs/opik/quickstart/?from=llm&utm_source=opik&utm_medium=github&utm_content=quickstart_link&utm_campaign=opik)）。
  - 丰富的第三方集成，实现无缝可观测性：轻松对接不断增长的框架列表，原生支持众多主流且流行的框架（包括近期新增的 **Google ADK**、**Autogen** 和 **Flowise AI**）。（[集成概览](https://www.comet.com/docs/opik/integrations/overview/?from=llm&utm_source=opik&utm_medium=github&utm_content=integrations_link&utm_campaign=opik)）
  - 通过 [Python SDK](https://www.comet.com/docs/opik/v1/tracing/annotate_traces/#annotating-traces-and-spans-using-the-sdk?from=llm&utm_source=opik&utm_medium=github&utm_content=sdk_link&utm_campaign=opik) 或 [UI](https://www.comet.com/docs/opik/tracing/annotate_traces/#annotating-traces-through-the-ui?from=llm&utm_source=opik&utm_medium=github&utm_content=ui_link&utm_campaign=opik) 为追踪和跨度（spans）添加反馈评分。
  - 在 [提示词游乐场](https://www.comet.com/docs/opik/prompt_engineering/playground) 中测试不同的提示词与模型。

- **评估与测试**：
  - 利用 [数据集](https://www.comet.com/docs/opik/v1/evaluation/manage_datasets/?from=llm&utm_source=opik&utm_medium=github&utm_content=datasets_link&utm_campaign=opik) 和 [实验](https://www.comet.com/docs/opik/v1/evaluation/evaluate_your_llm/?from=llm&utm_source=opik&utm_medium=github&utm_content=eval_link&utm_campaign=opik) 自动化你的 LLM 应用评估流程。
  - 借助强大的“LLM 作为裁判”指标处理复杂任务，如 [幻觉检测](https://www.comet.com/docs/opik/evaluation/metrics/hallucination/?from=llm&utm_source=opik&utm_medium=github&utm_content=hallucination_link&utm_campaign=opik)、[内容审核](https://www.comet.com/docs/opik/evaluation/metrics/moderation/?from=llm&utm_source=opik&utm_medium=github&utm_content=moderation_link&utm_campaign=opik) 以及 RAG 评估（[答案相关性](https://www.comet.com/docs/opik/evaluation/metrics/answer_relevance/?from=llm&utm_source=opik&utm_medium=github&utm_content=alex_link&utm_campaign=opik)、[上下文精度](https://www.comet.com/docs/opik/evaluation/metrics/context_precision/?from=llm&utm_source=opik&utm_medium=github&utm_content=context_link&utm_campaign=opik)）。
  - 通过我们的 [PyTest 集成](https://www.comet.com/docs/opik/v1/testing/pytest_integration/?from=llm&utm_source=opik&utm_medium=github&utm_content=pytest_link&utm_campaign=opik) 将评估流程接入 CI/CD 流水线。

- **生产监控与优化**：
  - 记录海量生产环境追踪日志：Opik 专为大规模设计（支持每天处理 4000 万+ 条追踪）。
  - 在 [Opik 仪表盘](https://www.comet.com/docs/opik/v1/production/production_monitoring/?from=llm&utm_source=opik&utm_medium=github&utm_content=dashboard_link&utm_campaign=opik) 中监控反馈评分、追踪数量和 Token 使用量随时间的变化。
  - 结合“LLM 作为裁判”指标使用 [在线评估规则](https://www.comet.com/docs/opik/v1/production/rules/?from=llm&utm_source=opik&utm_medium=github&utm_content=dashboard_link&utm_campaign=opik) 快速定位生产环境问题。
  - 利用 **Opik Agent Optimizer** 和 **Opik Guardrails** 持续改进并保障生产环境中 LLM 应用的安全性与稳定性。

> [!TIP]
> 如果你正在寻找 Opik 目前尚未提供的功能，请提交新的[功能请求](https://github.com/comet-ml/opik/issues/new/choose) 🚀

<br>

<a id="%EF%B8%8F-opik-server-installation"></a>
## 🛠️ Opik 服务端安装

在几分钟内让你的 Opik 服务端运行起来。选择最适合你的方案：

### 选项 1：Comet.com Cloud（最简单且推荐）

无需任何配置即可即时访问 Opik。非常适合快速上手和免维护部署。

👉 [创建你的免费 Comet 账户](https://www.comet.com/signup?from=llm&utm_source=opik&utm_medium=github&utm_content=install_create_link&utm_campaign=opik)

### 选项 2：自托管 Opik（完全掌控）

在你的自有环境中部署 Opik。可选择 Docker 用于本地环境，或 Kubernetes 用于可扩展的集群部署。

#### 使用 Docker Compose 自托管（适用于本地开发与测试）

这是启动本地 Opik 实例的最简单方式。请注意新增的 `./opik.sh` 安装脚本：

在 Linux 或 Mac 环境中：

```bash
# Clone the Opik repository
git clone https://github.com/comet-ml/opik.git

# Navigate to the repository
cd opik

# Start the Opik platform
./opik.sh
```

在 Windows 环境中：

```powershell
# Clone the Opik repository
git clone https://github.com/comet-ml/opik.git

# Navigate to the repository
cd opik

# Start the Opik platform
powershell -ExecutionPolicy ByPass -c ".\\opik.ps1"
```

**开发服务配置（Service Profiles）**

Opik 安装脚本现在支持针对不同开发场景的服务配置：

```bash
# Start full Opik suite (default behavior)
./opik.sh

# Start only infrastructure services (databases, caches etc.)
./opik.sh --infra

# Start infrastructure + backend services
./opik.sh --backend

# Enable guardrails with any profile
./opik.sh --guardrails # Guardrails with full Opik suite
./opik.sh --backend --guardrails # Guardrails with infrastructure + backend
```

使用 `--help` 或 `--info` 参数排查问题。Dockerfile 现已确保容器以非 root 用户运行，从而提升安全性。一切就绪后，你可以在浏览器中访问 [localhost:5173](http://localhost:5173)！详细操作请参阅[本地部署指南](https://www.comet.com/docs/opik/self-host/local_deployment?from=llm&utm_source=opik&utm_medium=github&utm_content=self_host_link&utm_campaign=opik)。

#### 使用 Kubernetes & Helm 自托管（适用于可扩展的部署）

对于生产环境或更大规模的自托管部署，Opik 可通过我们的 Helm Chart 安装在 Kubernetes 集群上。点击徽章查看完整的 [Kubernetes 安装指南](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik)。

[![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326ce5.svg?&logo=kubernetes&logoColor=white)](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik)

> [!IMPORTANT]
> **版本 1.7.0 变更**：请查阅[更新日志](https://github.com/comet-ml/opik/blob/main/CHANGELOG.md)以获取重要更新和破坏性变更说明。

<a id="-opik-client-sdk"></a>
## 💻 Opik 客户端 SDK

Opik 提供了一系列客户端库和 REST API，用于与 Opik 服务端交互。其中包括 Python、TypeScript 和 Ruby（通过 OpenTelemetry）的 SDK，可无缝集成到你的工作流中。详细的 API 和 SDK 参考请参阅 [Opik 客户端参考文档](https://www.comet.com/docs/opik/reference/overview?from=llm&utm_source=opik&utm_medium=github&utm_content=reference_link&utm_campaign=opik)。

### Python SDK 快速开始

要开始使用 Python SDK：

安装依赖包：

```bash
# install using pip
pip install opik

# or install with uv
uv pip install opik
```

通过运行 `opik configure` 命令配置 Python SDK，该命令会提示你输入 Opik 服务端地址（自托管实例）或你的 API Key 与工作区名称（Comet.com）：

```bash
opik configure
```

> [!TIP]
> 你也可以在 Python 代码中调用 `opik.configure(use_local=True)`，将 SDK 配置为运行本地自托管环境；或直接提供 API Key 和工作区信息用于 Comet.com。更多配置选项请参阅 [Python SDK 文档](https://www.comet.com/docs/opik/python-sdk-reference/?from=llm&utm_source=opik&utm_medium=github&utm_content=python_sdk_docs_link&utm_campaign=opik)。

你现在已准备好开始使用 [Python SDK](https://www.comet.com/docs/opik/python-sdk-reference/?from=llm&utm_source=opik&utm_medium=github&utm_content=sdk_link2&utm_campaign=opik) 记录追踪日志。

<a id="-logging-traces-with-integrations"></a>
### 📝 通过集成记录追踪（Logging Traces）

记录追踪日志最简单的方式是使用我们的直接集成。Opik 支持广泛的框架，包括近期新增的 **Google ADK**、**Autogen**、**AG2** 和 **Flowise AI**：

| Integration           | Description                                             | Documentation                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ADK                   | 记录 Google Agent Development Kit (ADK) 的追踪日志       | [Documentation](https://www.comet.com/docs/opik/integrations/adk?utm_source=opik&utm_medium=github&utm_content=google_adk_link&utm_campaign=opik)                              |
| AG2                   | 记录 AG2 LLM 调用的追踪日志                             | [Documentation](https://www.comet.com/docs/opik/integrations/ag2?utm_source=opik&utm_medium=github&utm_content=ag2_link&utm_campaign=opik)                                     |
| Agent Spec            | 记录 Agent Spec 调用的追踪日志                          | [Documentation](https://www.comet.com/docs/opik/integrations/agentspec?utm_source=opik&utm_medium=github&utm_content=agentspec_link&utm_campaign=opik)                         |
| AIsuite               | 记录 aisuite LLM 调用的追踪日志                         | [Documentation](https://www.comet.com/docs/opik/integrations/aisuite?utm_source=opik&utm_medium=github&utm_content=aisuite_link&utm_campaign=opik)                             |
| Agno                  | 记录 Agno 智能体编排框架调用的追踪日志                  | [Documentation](https://www.comet.com/docs/opik/integrations/agno?utm_source=opik&utm_medium=github&utm_content=agno_link&utm_campaign=opik)                                   |
| Anthropic             | 记录 Anthropic LLM 调用的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/anthropic?utm_source=opik&utm_medium=github&utm_content=anthropic_link&utm_campaign=opik)                         |
| Autogen               | 记录 Autogen 智能体工作流的追踪日志                     | [Documentation](https://www.comet.com/docs/opik/integrations/autogen?utm_source=opik&utm_medium=github&utm_content=autogen_link&utm_campaign=opik)                             |
| Bedrock               | 记录 Amazon Bedrock LLM 调用的追踪日志                  | [Documentation](https://www.comet.com/docs/opik/integrations/bedrock?utm_source=opik&utm_medium=github&utm_content=bedrock_link&utm_campaign=opik)                             |
| BeeAI (Python)        | 记录 BeeAI Python 智能体框架调用的追踪日志              | [Documentation](https://www.comet.com/docs/opik/integrations/beeai?utm_source=opik&utm_medium=github&utm_content=beeai_link&utm_campaign=opik)                                 |
| BeeAI (TypeScript)    | 记录 BeeAI TypeScript 智能体框架调用的追踪日志          | [Documentation](https://www.comet.com/docs/opik/integrations/beeai-typescript?utm_source=opik&utm_medium=github&utm_content=beeai_typescript_link&utm_campaign=opik)           |
| BytePlus              | 记录 BytePlus LLM 调用的追踪日志                        | [Documentation](https://www.comet.com/docs/opik/integrations/byteplus?utm_source=opik&utm_medium=github&utm_content=byteplus_link&utm_campaign=opik)                           |
| Cloudflare Workers AI | 记录 Cloudflare Workers AI 调用的追踪日志               | [Documentation](https://www.comet.com/docs/opik/integrations/cloudflare-workers-ai?utm_source=opik&utm_medium=github&utm_content=cloudflare_workers_ai_link&utm_campaign=opik) |
| Cohere                | 记录 Cohere LLM 调用的追踪日志                          | [Documentation](https://www.comet.com/docs/opik/integrations/cohere?utm_source=opik&utm_medium=github&utm_content=cohere_link&utm_campaign=opik)                               |
| CrewAI                | 记录 CrewAI 调用的追踪日志                              | [Documentation](https://www.comet.com/docs/opik/integrations/crewai?utm_source=opik&utm_medium=github&utm_content=crewai_link&utm_campaign=opik)                               |
| Cursor                | 记录 Cursor 对话的追踪日志                              | [Documentation](https://www.comet.com/docs/opik/integrations/cursor?utm_source=opik&utm_medium=github&utm_content=cursor_link&utm_campaign=opik)                               |
| DeepSeek              | 记录 DeepSeek LLM 调用的追踪日志                        | [Documentation](https://www.comet.com/docs/opik/integrations/deepseek?utm_source=opik&utm_medium=github&utm_content=deepseek_link&utm_campaign=opik)                           |
| Dify                  | 记录 Dify 智能体运行的追踪日志                          | [Documentation](https://www.comet.com/docs/opik/integrations/dify?utm_source=opik&utm_medium=github&utm_content=dify_link&utm_campaign=opik)                                   |
| DSPY                  | 记录 DSPy 运行的追踪日志                                | [Documentation](https://www.comet.com/docs/opik/integrations/dspy?utm_source=opik&utm_medium=github&utm_content=dspy_link&utm_campaign=opik)                                   |
| Fireworks AI          | 记录 Fireworks AI LLM 调用的追踪日志                    | [Documentation](https://www.comet.com/docs/opik/integrations/fireworks-ai?utm_source=opik&utm_medium=github&utm_content=fireworks_ai_link&utm_campaign=opik)                   |
| Flowise AI            | 记录 Flowise AI 可视化 LLM 构建器的追踪日志             | [Documentation](https://www.comet.com/docs/opik/integrations/flowise?utm_source=opik&utm_medium=github&utm_content=flowise_link&utm_campaign=opik)                             |
| Gemini (Python)       | 记录 Google Gemini LLM 调用的追踪日志                   | [Documentation](https://www.comet.com/docs/opik/integrations/gemini?utm_source=opik&utm_medium=github&utm_content=gemini_link&utm_campaign=opik)                               |
| Gemini (TypeScript)   | 记录 Google Gemini TypeScript SDK 调用的追踪日志        | [Documentation](https://www.comet.com/docs/opik/integrations/gemini-typescript?utm_source=opik&utm_medium=github&utm_content=gemini_typescript_link&utm_campaign=opik)         |
| Groq                  | 记录 Groq LLM 调用的追踪日志                            | [Documentation](https://www.comet.com/docs/opik/integrations/groq?utm_source=opik&utm_medium=github&utm_content=groq_link&utm_campaign=opik)                                   |
| Guardrails            | 记录 Guardrails AI 验证的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/guardrails-ai?utm_source=opik&utm_medium=github&utm_content=guardrails_link&utm_campaign=opik)                    |
| Haystack              | 记录 Haystack 调用的追踪日志                            | [Documentation](https://www.comet.com/docs/opik/integrations/haystack?utm_source=opik&utm_medium=github&utm_content=haystack_link&utm_campaign=opik)                           |
| Harbor                | 记录 Harbor 基准评估测试的追踪日志                      | [Documentation](https://www.comet.com/docs/opik/integrations/harbor?utm_source=opik&utm_medium=github&utm_content=harbor_link&utm_campaign=opik)                               |
| Instructor            | 记录使用 Instructor 发起的 LLM 调用的追踪日志           | [Documentation](https://www.comet.com/docs/opik/integrations/instructor?utm_source=opik&utm_medium=github&utm_content=instructor_link&utm_campaign=opik)                       |
| LangChain (Python)    | 记录 LangChain LLM 调用的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/langchain?utm_source=opik&utm_medium=github&utm_content=langchain_link&utm_campaign=opik)                         |
| LangChain (JS/TS)     | 记录 LangChain JavaScript/TypeScript 调用的追踪日志     | [Documentation](https://www.comet.com/docs/opik/integrations/langchainjs?utm_source=opik&utm_medium=github&utm_content=langchainjs_link&utm_campaign=opik)                     |
| LangGraph             | 记录 LangGraph 执行的追踪日志                           | [Documentation](https://www.comet.com/docs/opik/integrations/langgraph?utm_source=opik&utm_medium=github&utm_content=langgraph_link&utm_campaign=opik)                         |
| Langflow              | 记录 Langflow 可视化 AI 构建器的追踪日志                | [Documentation](https://www.comet.com/docs/opik/integrations/langflow?utm_source=opik&utm_medium=github&utm_content=langflow_link&utm_campaign=opik)                           |
| LiteLLM               | 记录 LiteLLM 模型调用的追踪日志                         | [Documentation](https://www.comet.com/docs/opik/integrations/litellm?utm_source=opik&utm_medium=github&utm_content=litellm_link&utm_campaign=opik)                             |
| LiveKit Agents        | 记录 LiveKit Agents AI 智能体框架调用的追踪日志         | [Documentation](https://www.comet.com/docs/opik/integrations/livekit?utm_source=opik&utm_medium=github&utm_content=livekit_link&utm_campaign=opik)                             |
| LlamaIndex            | 记录 LlamaIndex LLM 调用的追踪日志                      | [Documentation](https://www.comet.com/docs/opik/integrations/llama_index?utm_source=opik&utm_medium=github&utm_content=llama_index_link&utm_campaign=opik)                     |
| Mastra                | 记录 Mastra AI 工作流框架调用的追踪日志                 | [Documentation](https://www.comet.com/docs/opik/integrations/mastra?utm_source=opik&utm_medium=github&utm_content=mastra_link&utm_campaign=opik)                               |
| Microsoft Agent Framework (Python) | 记录 Microsoft Agent Framework 调用的追踪日志 | [Documentation](https://www.comet.com/docs/opik/integrations/microsoft-agent-framework?utm_source=opik&utm_medium=github&utm_content=agent_framework_link&utm_campaign=opik)              |
| Microsoft Agent Framework (.NET) | 记录 Microsoft Agent Framework .NET 调用的追踪日志 | [Documentation](https://www.comet.com/docs/opik/integrations/microsoft-agent-framework-dotnet?utm_source=opik&utm_medium=github&utm_content=agent_framework_dotnet_link&utm_campaign=opik) |
| Mistral AI            | 记录 Mistral AI LLM 调用的追踪日志                      | [Documentation](https://www.comet.com/docs/opik/integrations/mistral?utm_source=opik&utm_medium=github&utm_content=mistral_link&utm_campaign=opik)                             |
| n8n                   | 记录 n8n 工作流执行的追踪日志                           | [Documentation](https://www.comet.com/docs/opik/integrations/n8n?utm_source=opik&utm_medium=github&utm_content=n8n_link&utm_campaign=opik)                                     |
| Novita AI             | 记录 Novita AI LLM 调用的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/novita-ai?utm_source=opik&utm_medium=github&utm_content=novita_ai_link&utm_campaign=opik)                         |
| Ollama                | 记录 Ollama LLM 调用的追踪日志                          | [Documentation](https://www.comet.com/docs/opik/integrations/ollama?utm_source=opik&utm_medium=github&utm_content=ollama_link&utm_campaign=opik)                               |
| OpenAI (Python)       | 记录 OpenAI LLM 调用的追踪日志                          | [Documentation](https://www.comet.com/docs/opik/integrations/openai?utm_source=opik&utm_medium=github&utm_content=openai_link&utm_campaign=opik)                               |
| OpenAI (JS/TS)        | 记录 OpenAI JavaScript/TypeScript 调用的追踪日志        | [Documentation](https://www.comet.com/docs/opik/integrations/openai-typescript?utm_source=opik&utm_medium=github&utm_content=openai_typescript_link&utm_campaign=opik)         |
| OpenAI Agents         | 记录 OpenAI Agents SDK 调用的追踪日志                   | [Documentation](https://www.comet.com/docs/opik/integrations/openai_agents?utm_source=opik&utm_medium=github&utm_content=openai_agents_link&utm_campaign=opik)                 |
| OpenClaw              | 记录 OpenClaw 智能体运行的追踪日志                      | [Documentation](https://www.comet.com/docs/opik/integrations/openclaw?utm_source=opik&utm_medium=github&utm_content=openclaw_link&utm_campaign=opik)                           |
| OpenRouter            | 记录 OpenRouter LLM 调用的追踪日志                      | [Documentation](https://www.comet.com/docs/opik/integrations/openrouter?utm_source=opik&utm_medium=github&utm_content=openrouter_link&utm_campaign=opik)                       |
| OpenTelemetry         | 记录支持 OpenTelemetry 的调用追踪日志                   | [Documentation](https://www.comet.com/docs/opik/tracing/opentelemetry/overview?utm_source=opik&utm_medium=github&utm_content=opentelemetry_link&utm_campaign=opik)             |
| OpenWebUI             | 记录 OpenWebUI 对话的追踪日志                           | [Documentation](https://www.comet.com/docs/opik/integrations/openwebui?utm_source=opik&utm_medium=github&utm_content=openwebui_link&utm_campaign=opik)                         |
| Pipecat               | 记录 Pipecat 实时语音智能体调用的追踪日志               | [Documentation](https://www.comet.com/docs/opik/integrations/pipecat?utm_source=opik&utm_medium=github&utm_content=pipecat_link&utm_campaign=opik)                             |
| Predibase             | 记录 Predibase LLM 调用的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/predibase?utm_source=opik&utm_medium=github&utm_content=predibase_link&utm_campaign=opik)                         |
| Pydantic AI           | 记录 PydanticAI 智能体调用的追踪日志                    | [Documentation](https://www.comet.com/docs/opik/integrations/pydantic-ai?utm_source=opik&utm_medium=github&utm_content=pydantic_ai_link&utm_campaign=opik)                     |
| Ragas                 | 记录 Ragas 评估的追踪日志                               | [Documentation](https://www.comet.com/docs/opik/integrations/ragas?utm_source=opik&utm_medium=github&utm_content=ragas_link&utm_campaign=opik)                                 |
| Semantic Kernel       | 记录 Microsoft Semantic Kernel 调用的追踪日志           | [Documentation](https://www.comet.com/docs/opik/integrations/semantic-kernel?utm_source=opik&utm_medium=github&utm_content=semantic_kernel_link&utm_campaign=opik)             |
| Smolagents            | 记录 Smolagents 智能体的追踪日志                        | [Documentation](https://www.comet.com/docs/opik/integrations/smolagents?utm_source=opik&utm_medium=github&utm_content=smolagents_link&utm_campaign=opik)                       |
| Spring AI             | 记录 Spring AI 框架调用的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/spring-ai?utm_source=opik&utm_medium=github&utm_content=spring_ai_link&utm_campaign=opik)                         |
| Strands Agents        | 记录 Strands 智能体调用的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/strands-agents?utm_source=opik&utm_medium=github&utm_content=strands_agents_link&utm_campaign=opik)               |
| Together AI           | 记录 Together AI LLM 调用的追踪日志                     | [Documentation](https://www.comet.com/docs/opik/integrations/together-ai?utm_source=opik&utm_medium=github&utm_content=together_ai_link&utm_campaign=opik)                     |
| Vercel AI SDK         | 记录 Vercel AI SDK 调用的追踪日志                       | [Documentation](https://www.comet.com/docs/opik/integrations/vercel-ai-sdk?utm_source=opik&utm_medium=github&utm_content=vercel_ai_sdk_link&utm_campaign=opik)                 |
| VoltAgent             | 记录 VoltAgent 智能体框架调用的追踪日志                 | [Documentation](https://www.comet.com/docs/opik/integrations/voltagent?utm_source=opik&utm_medium=github&utm_content=voltagent_link&utm_campaign=opik)                         |
| WatsonX               | 记录 IBM watsonx LLM 调用的追踪日志                     | [Documentation](https://www.comet.com/docs/opik/integrations/watsonx?utm_source=opik&utm_medium=github&utm_content=watsonx_link&utm_campaign=opik)                             |
| xAI Grok              | 记录 xAI Grok LLM 调用的追踪日志                        | [Documentation](https://www.comet.com/docs/opik/integrations/xai-grok?utm_source=opik&utm_medium=github&utm_content=xai_grok_link&utm_campaign=opik)                           |

> [!TIP]
> 如果你使用的框架未在上述列表中，欢迎[提交 Issue](https://github.com/comet-ml/opik/issues) 或通过 PR 贡献集成代码。

如果你没有使用上述任何框架，也可以使用 `track` 函数装饰器来[记录追踪日志](https://www.comet.com/docs/opik/v1/tracing/log_traces/?from=llm&utm_source=opik&utm_medium=github&utm_content=traces_link&utm_campaign=opik)：

```python
import opik

opik.configure(use_local=True) # Run locally

@opik.track
def my_llm_function(user_question: str) -> str:
    # Your LLM code here

    return "Hello"
```

> [!TIP]
> `track` 装饰器可与我们的任何集成配合使用，也可用于追踪嵌套函数调用。

<a id="-llm-as-a-judge-metrics"></a>
### 🧑‍⚖️ “LLM 作为裁判”指标（LLM as a Judge metrics）

Python Opik SDK 内置了多种“LLM 作为裁判”指标，帮助你评估 LLM 应用的表现。更多详情请参阅[指标文档](https://www.comet.com/docs/opik/evaluation/metrics/overview/?from=llm&utm_source=opik&utm_medium=github&utm_content=metrics_2_link&utm_campaign=opik)。

要使用这些指标，只需导入相关模块并调用 `score` 函数：

```python
from opik.evaluation.metrics import Hallucination

metric = Hallucination()
score = metric.score(
    input="What is the capital of France?",
    output="Paris",
    context=["France is a country in Europe."]
)
print(score)
```

Opik 还提供了一系列预构建的启发式（heuristic）指标，并支持你自定义创建自己的指标。更多详情请参阅[指标文档](https://www.comet.com/docs/opik/evaluation/metrics/overview?from=llm&utm_source=opik&utm_medium=github&utm_content=metrics_3_link&utm_campaign=opik)。

<a id="-evaluating-your-llm-application"></a>
### 🔍 评估你的 LLM 应用

Opik 允许你在开发阶段通过 [数据集](https://www.comet.com/docs/opik/v1/evaluation/manage_datasets/?from=llm&utm_source=opik&utm_medium=github&utm_content=datasets_2_link&utm_campaign=opik) 和 [实验](https://www.comet.com/docs/opik/v1/evaluation/evaluate_your_llm/?from=llm&utm_source=opik&utm_medium=github&utm_content=experiments_link&utm_campaign=opik) 评估你的 LLM 应用。Opik 仪表盘提供了针对实验的增强图表以及对大型追踪日志更好的处理能力。你还可以使用我们的 [PyTest 集成](https://www.comet.com/docs/opik/v1/testing/pytest_integration/?from=llm&utm_source=opik&utm_medium=github&utm_content=pytest_2_link&utm_campaign=opik) 将评估流程接入 CI/CD 流水线中运行。

<a id="-star-us-on-github"></a>
## ⭐ 在 GitHub 上给我们点星（Star）

如果你觉得 Opik 有用，请考虑为我们点个 Star！你的支持有助于我们壮大社区并持续改进产品。

[![Star History Chart](https://api.star-history.com/svg?repos=comet-ml/opik&type=Date)](https://github.com/comet-ml/opik)

<a id="-contributing"></a>
## 🤝 参与贡献

你可以通过多种方式为 Opik 做出贡献：

- 提交 [Bug 报告](https://github.com/comet-ml/opik/issues) 和 [功能请求](https://github.com/comet-ml/opik/issues)
- 审阅文档并提交 [Pull Requests](https://github.com/comet-ml/opik/pulls) 以改进内容
- 撰写或分享关于 Opik 的技术文章/演讲，并[告知我们](https://chat.comet.com)
- 为你支持的[热门功能请求](https://github.com/comet-ml/opik/issues?q=is%3Aissue+is%3Aopen+label%3A%22enhancement%22)投票

如需了解如何为 Opik 做出贡献，请参阅我们的[贡献指南](CONTRIBUTING.md)。