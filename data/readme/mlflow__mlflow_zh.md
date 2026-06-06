<h1 align="center" style="border-bottom: none">
    <a href="https://mlflow.org/">
        <img alt="MLflow logo" src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/assets/logo.svg" width="200" />
    </a>
</h1>
<h2 align="center" style="border-bottom: none">面向智能体（Agents）、大语言模型与机器学习模型的开源 AI 工程平台</h2>

MLflow 是目前最大的面向智能体、大语言模型（LLM）和机器学习模型的开源 **AI 工程平台**。MLflow 使各类团队能够 [调试](https://mlflow.org/llm-tracing)、[评估](https://mlflow.org/llm-evaluation)、[监控](https://mlflow.org/ai-monitoring) 并 [优化](https://mlflow.org/prompt-optimization) 生产级 AI 应用，同时有效控制成本并管理对模型与数据的访问权限。凭借每月超过 **6000 万次下载量**，全球数以千计的组织每天都在使用 MLflow 自信地将 AI 部署到生产环境中。

MLflow 为智能体和 LLM 应用提供了全面的功能集，包括生产级 [可观测性（Observability）](https://mlflow.org/docs/latest/genai/tracing)、[评估（Evaluation）](https://mlflow.org/docs/latest/genai/eval-monitor)、[提示词管理（Prompt Management）](https://mlflow.org/docs/latest/genai/prompt-registry)、[提示词优化（Prompt Optimization）](https://mlflow.org/prompt-optimization) 以及用于管理成本和模型访问的 [AI Gateway](https://mlflow.org/docs/latest/genai/governance/ai-gateway)。了解更多请访问 [面向 LLM 和智能体的 MLflow](https://mlflow.org/docs/latest/genai)。

<div align="center">

[![Python SDK](https://img.shields.io/pypi/v/mlflow)](https://pypi.org/project/mlflow/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/mlflow)](https://pepy.tech/projects/mlflow)
[![License](https://img.shields.io/github/license/mlflow/mlflow)](https://github.com/mlflow/mlflow/blob/master/LICENSE.txt)
<a href="https://twitter.com/intent/follow?screen_name=mlflow" target="_blank">
<img src="https://img.shields.io/twitter/follow/mlflow?logo=X&color=%20%23f5f5f5"
      alt="follow on X(Twitter)"></a>
<a href="https://www.linkedin.com/company/mlflow-org/" target="_blank">
<img src="https://custom-icon-badges.demolab.com/badge/LinkedIn-0A66C2?logo=linkedin-white&logoColor=fff"
      alt="follow on LinkedIn"></a>
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/mlflow/mlflow)

</div>

<div align="center">
   <div>
      <a href="https://mlflow.org/"><strong>官网</strong></a> ·
      <a href="https://demo.mlflow.org/"><strong>在线试用</strong></a> ·
      <a href="https://mlflow.org/docs/latest"><strong>文档</strong></a> ·
      <a href="https://mlflow.org/blog"><strong>动态</strong></a> ·
      <a href="https://lu.ma/mlflow?k=c"><strong>活动</strong></a>
   </div>
</div>

<br>

## 三步快速上手

几分钟内从零搭建完整的 LLMOps 全栈流程。无需复杂配置或大规模代码修改。[快速开始 →](https://mlflow.org/docs/latest/genai/tracing/quickstart/)

**1. 启动 MLflow 服务**

```bash
uvx mlflow server
```

**2. 启用日志记录**

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.openai.autolog()
```

**3. 运行你的代码**

```python
from openai import OpenAI

client = OpenAI()
client.responses.create(
    model="gpt-5.4-mini",
    input="Hello!",
)
```

在 `http://localhost:5000` 的 MLflow 界面中探索追踪（Traces）和指标数据。

## 大语言模型与智能体

MLflow 提供构建、调试、评估和部署生产级 LLM 应用及 AI 智能体所需的一切工具。支持 Python、TypeScript/JavaScript、Java 以及任何其他编程语言。MLflow 还原生集成了 [OpenTelemetry](https://opentelemetry.io/) 和 MCP。

<table>
  <tr>
    <td width="50%">
    <img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/assets/readme-tracing.png" alt="Observability" width=100%>
    <div align="center">
        <br>
        <a href="https://mlflow.org/docs/latest/genai/tracing/"><strong>可观测性</strong></a>
        <br><br>
        <div>Capture complete traces of your LLM applications and agents for deep behavioral insights. Built on OpenTelemetry, supporting any LLM provider and agent framework. Monitor production quality, costs, and safety.</div><br>
        <a href="https://mlflow.org/docs/latest/genai/tracing/quickstart/">Getting Started →</a>
        <br>
        <a href="https://demo.mlflow.org/#/experiments/1/traces?startTimeLabel=CUSTOM&startTime=2026-04-17T16%3A47%3A15.258Z&endTime=2026-04-24T21%3A20%3A50.781Z">Try Demo →</a>
        <br><br>
    </div>
    </td>
    <td width="50%">
    <img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/assets/readme-llm-eval.png" alt="Evaluation" width=100%>
    <div align="center">
        <br>
        <a href="https://mlflow.org/docs/latest/genai/eval-monitor/"><strong>评估</strong></a>
        <br><br>
        <div>Run systematic evaluations, track quality metrics over time, and catch regressions before they reach production. Choose from 50+ built-in metrics and LLM judges, or define your own.</div><br>
        <a href="https://mlflow.org/docs/latest/genai/eval-monitor/">Getting Started →</a>
        <br>
        <a href="https://demo.mlflow.org/#/experiments/1/runs/d690ad8bb7a546c5a74b79691bb32b27/evaluations">Try Demo →</a>
        <br><br>
    </div>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/assets/readme-prompt.png" alt="Prompts & Optimization" width=100%>
    <div align="center">
        <br>
        <a href="https://mlflow.org/docs/latest/genai/prompt-registry/"><strong>提示词与优化</strong></a>
        <br><br>
        <div>Version, test, and deploy prompts with full lineage tracking. <a href="https://mlflow.org/prompt-optimization">Automatically optimize prompts</a> with state-of-the-art algorithms to improve performance.</div><br>
        <a href="https://mlflow.org/docs/latest/genai/prompt-registry/create-and-edit-prompts/">Getting Started →</a>
        <br>
        <a href="https://demo.mlflow.org/#/experiments/1/prompts/mlflow-demo.prompts.code-reviewer?promptVersion=4">Try Demo →</a>
        <br><br>
    </div>
    </td>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/assets/readme-gateway.png" alt="AI Gateway" width=100%>
    <div align="center">
        <br>
        <a href="https://mlflow.org/docs/latest/genai/governance/ai-gateway/"><strong>AI Gateway</strong></a>
        <br><br>
        <div>Unified API gateway for all LLM providers. Route requests, manage rate limits, handle fallbacks, and control costs through an OpenAI-compatible interface with built-in credential management, guardrails and traffic splitting for A/B testing.</div><br>
        <a href="https://mlflow.org/docs/latest/genai/governance/ai-gateway/quickstart/">Getting Started →</a>
        <br><br>
    </div>
    </td>
  </tr>
</table>

## 模型训练

针对机器学习和深度学习模型的开发生命周期，MLflow 提供了一套完整的工具：

- [**实验追踪（Experiment Tracking）**](https://mlflow.org/docs/latest/ml/tracking/) — 跨实验跟踪模型、参数、指标和评估结果
- [**模型评估（Model Evaluation）**](https://mlflow.org/docs/latest/ml/evaluation/) — 与实验追踪集成的自动化评估工具
- [**模型注册表（Model Registry）**](https://mlflow.org/docs/latest/ml/model-registry/) — 协作管理机器学习模型的全生命周期
- [**部署（Deployment）**](https://mlflow.org/docs/latest/ml/deployment/) — 将模型部署到批处理和实时推理环境，支持 Docker、Kubernetes、Azure ML、AWS SageMaker 等

了解更多请访问 [面向模型训练的 MLflow](https://mlflow.org/docs/latest/ml)。

## 集成支持

MLflow 支持所有智能体框架、LLM 提供商、工具和编程语言。我们为超过 60 个框架提供一行代码自动追踪功能。查看 [完整集成列表](https://mlflow.org/docs/latest/genai/tracing/integrations/)。

### OpenTelemetry

<table>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/app-instrumentation/opentelemetry"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/opentelemetry-logo-only.png" height="40"><br><sub><b>OpenTelemetry</b></sub></a></td>
  </tr>
</table>

### 智能体框架（Python）

<table>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langchain"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/langchain-logo-only.png" height="40"><br><sub><b>LangChain</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langgraph"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/langgraph-logo-only.png" height="40"><br><sub><b>LangGraph</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/openai-agent"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/openai-logo-only.png" height="40"><br><sub><b>OpenAI Agent</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/dspy"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/dspy-logo.png" height="40"><br><sub><b>DSPy</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/pydantic_ai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/pydantic-ai-logo-only.png" height="40"><br><sub><b>PydanticAI</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/google-adk"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/google-adk-logo.png" height="40"><br><sub><b>Google ADK</b></sub></a></td>
  </tr>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/microsoft-agent-framework"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/microsoft-agent-framework-logo.png" height="40"><br><sub><b>Microsoft Agent</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/crewai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/crewai-logo.svg" height="40"><br><sub><b>CrewAI</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/llama_index"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/llamaindex-logo.svg" height="40"><br><sub><b>LlamaIndex</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/autogen"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/autogen-logo.png" height="40"><br><sub><b>AutoGen</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/strands"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/strands-logo.png" height="40"><br><sub><b>Strands</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/livekit"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/livekit-logo.png" height="40"><br><sub><b>LiveKit Agents</b></sub></a></td>
  </tr>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/agno"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/agno-logo.png" height="40"><br><sub><b>Agno</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/bedrock-agentcore"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/bedrock-logo.png" height="40"><br><sub><b>Bedrock AgentCore</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/smolagents"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/smolagents-logo.png" height="40"><br><sub><b>Smolagents</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/semantic_kernel"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/semantic-kernel-logo.png" height="40"><br><sub><b>Semantic Kernel</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/deepagent"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/deepagent-logo.svg" height="40"><br><sub><b>DeepAgent</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/ag2"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/ag2-logo.png" height="40"><br><sub><b>AG2</b></sub></a></td>
  </tr>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/haystack"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/haystack-logo.png" height="40"><br><sub><b>Haystack</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/koog"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/koog.png" height="40"><br><sub><b>Koog</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/txtai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/txtai-logo.png" height="40"><br><sub><b>txtai</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/pipecat"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/pipecat.png" height="40"><br><sub><b>Pipecat</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/watsonx-orchestrate"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/watsonx-orchestrate.png" height="40"><br><sub><b>Watsonx</b></sub></a></td>
  </tr>
</table>

### 智能体框架（TypeScript）

<table>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langchain"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/langchain-logo-only.png" height="40"><br><sub><b>LangChain</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langgraph"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/langgraph-logo-only.png" height="40"><br><sub><b>LangGraph</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/vercelai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/vercel-logo.svg" height="40"><br><sub><b>Vercel AI SDK</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/mastra"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/mastra-logo.png" height="40"><br><sub><b>Mastra</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/voltagent"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/voltagent-logo.png" height="40"><br><sub><b>VoltAgent</b></sub></a></td>
  </tr>
</table>

### 智能体框架（Java）

<table>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/spring-ai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/spring-ai-logo.png" height="40"><br><sub><b>Spring AI</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/quarkus-langchain4j"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/langchain4j.svg" height="40"><br><sub><b>Quarkus LangChain4j</b></sub></a></td>
  </tr>
</table>

### LLM 提供商

<table>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/openai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/openai-logo-only.png" height="40"><br><sub><b>OpenAI</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/anthropic"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/anthropic-logo.png" height="40"><br><sub><b>Anthropic</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/databricks"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/databricks-logo.png" height="40"><br><sub><b>Databricks</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/gemini"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/google-gemini-logo.svg" height="40"><br><sub><b>Gemini</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/bedrock"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/bedrock-logo.png" height="40"><br><sub><b>Amazon Bedrock</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/litellm"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/litellm-logo.png" height="40"><br><sub><b>LiteLLM</b></sub></a></td>
  </tr>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/mistral"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/mistral-ai-logo.svg" height="40"><br><sub><b>Mistral</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/xai-grok"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/grok-logo.png" height="40"><br><sub><b>xAI / Grok</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/ollama"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/ollama-logo.png" height="40"><br><sub><b>Ollama</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/groq"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/groq-logo.svg" height="40"><br><sub><b>Groq</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/deepseek"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/deepseek-logo.png" height="40"><br><sub><b>DeepSeek</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/qwen"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/qwen-logo.jpg" height="40"><br><sub><b>Qwen</b></sub></a></td>
  </tr>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/moonshot"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/kimi-logo.png" height="40"><br><sub><b>Moonshot AI</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/cohere"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/cohere-logo.png" height="40"><br><sub><b>Cohere</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/byteplus"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/byteplus-logo.png" height="40"><br><sub><b>BytePlus</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/novitaai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/novitaai-logo.jpg" height="40"><br><sub><b>Novita AI</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/fireworksai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/fireworks-ai-logo.png" height="40"><br><sub><b>FireworksAI</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/togetherai"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/together-ai-logo.png" height="40"><br><sub><b>Together AI</b></sub></a></td>
  </tr>
</table>

### AI Gateway / 网关

<table>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/databricks-ai-gateway"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/databricks-logo.png" height="40"><br><sub><b>Databricks</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/litellm-proxy"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/litellm-logo.png" height="40"><br><sub><b>LiteLLM Proxy</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/vercel-ai-gateway"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/vercel-logo.svg" height="40"><br><sub><b>Vercel AI Gateway</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/openrouter"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/openrouter-logo.png" height="40"><br><sub><b>OpenRouter</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/portkey"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/portkey-logo.png" height="40"><br><sub><b>Portkey</b></sub></a></td>
  </tr>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/helicone"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/helicone-logo.png" height="40"><br><sub><b>Helicone</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/kong"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/kong-logo.png" height="40"><br><sub><b>Kong AI Gateway</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/pydantic-ai-gateway"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/pydantic-ai-logo-only.png" height="40"><br><sub><b>PydanticAI Gateway</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/truefoundry"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/truefoundry-logo.png" height="40"><br><sub><b>TrueFoundry</b></sub></a></td>
  </tr>
</table>

### 工具与无代码平台

<table>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/instructor"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/instructor-logo.svg" height="40"><br><sub><b>Instructor</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/claude_code"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/claude-code-logo.png" height="40"><br><sub><b>Claude Code</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/opencode"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/opencode-logo.png" height="40"><br><sub><b>Opencode</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langfuse"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/langfuse-logo.png" height="40"><br><sub><b>Langfuse</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/arize"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/arize-phoenix-logo.png" height="40"><br><sub><b>Arize / Phoenix</b></sub></a></td>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/goose"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/goose-logo.png" height="40"><br><sub><b>Goose</b></sub></a></td>
  </tr>
  <tr>
    <td align="center" width="110"><a href="https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langflow"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/langflow.svg" height="40"><br><sub><b>Langflow</b></sub></a></td>
  </tr>
</table>

## 部署与托管 MLflow

MLflow 可在多种环境中使用，包括本地环境、内部集群、云平台以及托管服务。作为开源平台，MLflow **不绑定任何特定供应商** —— 无论你是构建 AI 智能体、LLM 应用还是机器学习模型，都能获得 MLflow 的核心能力支持。

<table>
  <tr>
    <td align="center" width="130"><a href="https://docs.databricks.com/aws/en/mlflow3/genai/"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/databricks-logo.png" height="40"><br><sub><b>Databricks</b></sub></a></td>
    <td align="center" width="130"><a href="https://aws.amazon.com/sagemaker-ai/experiments/"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/amazon-sagemaker-logo.png" height="40"><br><sub><b>Amazon SageMaker</b></sub></a></td>
    <td align="center" width="130"><a href="https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow?view=azureml-api-2"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/azure-ml-logo.png" height="40"><br><sub><b>Azure ML</b></sub></a></td>
    <td align="center" width="130"><a href="https://nebius.com/services/managed-mlflow"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/nebius-logo.png" height="40"><br><sub><b>Nebius</b></sub></a></td>
    <td align="center" width="130"><a href="https://mlflow.org/docs/latest/ml/tracking/"><img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/docs/static/images/logos/kubernetes-logo.png" height="40"><br><sub><b>Self-Hosted</b></sub></a></td>
  </tr>
</table>

## 💭 支持与帮助

- 如需使用 MLflow 的帮助或提问（例如“如何实现 X？”），请访问 [官方文档](https://mlflow.org/docs/latest)。
- 在文档页面中，你可以向我们的 AI 驱动聊天机器人提问。点击右下角的 **“Ask AI”** 按钮即可。
- 加入 [线上活动](https://lu.ma/mlflow?k=c)，如办公时间交流和线下聚会。
- 如需报告 Bug、提交文档问题或提出功能建议，请 [创建 GitHub Issue](https://github.com/mlflow/mlflow/issues/new/choose)。
- 如需获取版本更新公告及其他讨论信息，欢迎订阅我们的邮件列表（mlflow-users@googlegroups.com）或在 [Slack](https://mlflow.org/slack) 上加入我们。

## 🤝 贡献指南

我们非常欢迎对 MLflow 的贡献！

- 提交 [Bug 报告](https://github.com/mlflow/mlflow/issues/new?template=bug_report_template.yaml) 和 [功能请求](https://github.com/mlflow/mlflow/issues/new?template=feature_request_template.yaml)
- 参与 [适合新手的任务](https://github.com/mlflow/mlflow/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) 和 [寻求协助的任务](https://github.com/mlflow/mlflow/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
- 撰写关于 MLflow 的文章并分享你的使用经验

请查阅我们的 [贡献指南](CONTRIBUTING.md) 以了解更多如何为 MLflow 做出贡献。

## ⭐️ Star History

<a href="https://star-history.com/#mlflow/mlflow&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mlflow/mlflow&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mlflow/mlflow&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=mlflow/mlflow&type=Date" />
 </picture>
</a>

## ✏️ 引用说明

如果你在研究中使用了 MLflow，请使用 [GitHub 仓库页面](https://github.com/mlflow/mlflow) 顶部的 "Cite this repository" 按钮进行引用。该功能将为你提供包括 APA 和 BibTeX 在内的多种标准引用格式。

## 👥 核心维护成员

MLflow 目前由以下核心成员负责维护，同时得到了数百位才华横溢的社区成员的显著贡献支持：

- [Ben Wilson](https://github.com/BenWilson2)
- [Corey Zumar](https://github.com/dbczumar)
- [Daniel Lok](https://github.com/daniellok-db)
- [Gabriel Fu](https://github.com/gabrielfu)
- [Harutaka Kawamura](https://github.com/harupy)
- [Joel Robin P](https://github.com/joelrobin18)
- [Matt Prahl](https://github.com/mprahl)
- [Pat Sukprasert](https://github.com/PattaraS)
- [Serena Ruan](https://github.com/serena-ruan)
- [Tomu Hirata](https://github.com/TomeHirata)
- [Weichen Xu](https://github.com/WeichenXu123)
- [Yuki Watanabe](https://github.com/B-Step62)