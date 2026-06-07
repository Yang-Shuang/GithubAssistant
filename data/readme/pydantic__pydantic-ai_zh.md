<div align="center">
  <a href="https://ai.pydantic.dev/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://pydantic.dev/docs/ai/img/pydantic-ai-dark.svg">
      <img src="https://pydantic.dev/docs/ai/img/pydantic-ai-light.svg" alt="Pydantic AI">
    </picture>
  </a>
</div>
<div align="center">
  <h3>生成式 AI（GenAI）Agent 框架，采用 Pydantic 风格</h3>
</div>
<div align="center">
  <a href="https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml/badge.svg?event=push" alt="CI"></a>
  <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/pydantic/pydantic-ai"><img src="https://coverage-badge.samuelcolvin.workers.dev/pydantic/pydantic-ai.svg" alt="Coverage"></a>
  <a href="https://pypi.python.org/pypi/pydantic-ai"><img src="https://img.shields.io/pypi/v/pydantic-ai.svg" alt="PyPI"></a>
  <a href="https://github.com/pydantic/pydantic-ai"><img src="https://img.shields.io/pypi/pyversions/pydantic-ai.svg" alt="versions"></a>
  <a href="https://github.com/pydantic/pydantic-ai/blob/main/LICENSE"><img src="https://img.shields.io/github/license/pydantic/pydantic-ai.svg?v" alt="license"></a>
  <a href="https://logfire.pydantic.dev/docs/join-slack/"><img src="https://img.shields.io/badge/Slack-Join%20Slack-4A154B?logo=slack" alt="Join Slack" /></a>
</div>

---

**文档**: [ai.pydantic.dev](https://ai.pydantic.dev/)

---

### <em>Pydantic AI 是一个 Python Agent（智能体）框架，旨在帮助你快速、自信且无痛苦地构建基于生成式 AI 的生产级应用与工作流。</em>


FastAPI 通过提供创新且符合人体工程学的设计，彻底改变了 Web 开发。它建立在 [Pydantic Validation](https://docs.pydantic.dev)（数据校验）和现代 Python 特性（如类型提示）的基础之上。

尽管几乎所有的 Python Agent 框架和 LLM（大语言模型）库都使用了 Pydantic Validation，但当我们开始在 [Pydantic Logfire](https://pydantic.dev/logfire) 中集成 LLM 时，却找不到能带来同样流畅体验的解决方案。

我们构建 Pydantic AI 只有一个简单的目标：将那种 FastAPI 般的开发体验带到 GenAI（生成式 AI）应用与 Agent 开发中。

## 为什么选择 Pydantic AI

1. **由 Pydantic 团队打造**：
[Pydantic Validation](https://docs.pydantic.dev/latest/)（数据校验）是 OpenAI SDK、Google ADK、Anthropic SDK、LangChain、LlamaIndex、AutoGPT、Transformers、CrewAI、Instructor 等众多库的底层校验层。_既然可以直接使用源头，何必舍近求远呢？_ :smiley:

2. **模型无关性**：
支持几乎所有 [模型](https://ai.pydantic.dev/models/overview) 和提供商：OpenAI、Anthropic、Gemini、DeepSeek、Grok、Cohere、Mistral 以及 Perplexity；Azure AI Foundry、Amazon Bedrock、Google Cloud、Ollama、LiteLLM、Groq、OpenRouter、Together AI、Fireworks AI、Cerebras、Hugging Face、GitHub、Heroku、Vercel、Nebius、OVHcloud、Alibaba Cloud 和 SambaNova。如果你常用的模型或提供商未列出，也可以轻松实现 [自定义模型](https://ai.pydantic.dev/models/overview#custom-models)。

3. **无缝可观测性**：
与我们的通用 OpenTelemetry（OTel）可观测平台 [Pydantic Logfire](https://pydantic.dev/logfire) 深度[集成](https://ai.pydantic.dev/logfire)，提供实时调试、基于评估的性能监控，以及行为追踪和成本跟踪。如果你已经拥有支持 OTel 的可观测性平台，也可以[直接使用它](https://ai.pydantic.dev/logfire#alternative-observability-backends)。

4. **完全类型安全**：
旨在为你的 IDE 或 AI 编程 Agent 提供尽可能多的上下文以支持自动补全和[静态类型检查](https://ai.pydantic.dev/agents#static-type-checking)，将整类错误从运行时提前到编写时解决，带来类似 Rust “只要编译通过就能运行”的体验。

5. **强大的评估功能**：
使你能够系统地测试和[评估](https://ai.pydantic.dev/evals)所构建 Agent 系统的性能与准确性，并在 Pydantic Logfire 中长期监控其表现。

6. **为扩展而设计**：
通过可组合的 [能力（Capabilities）](https://ai.pydantic.dev/capabilities) 构建 Agent，将工具、钩子、指令和模型设置打包为可复用单元。可使用内置的 [Web 搜索](https://ai.pydantic.dev/capabilities#provider-adaptive-tools)、[思考](https://ai.pydantic.dev/capabilities#thinking) 和 [MCP](https://ai.pydantic.dev/capabilities#provider-adaptive-tools) 能力，从 [Pydantic AI Harness](https://ai.pydantic.dev/harness/overview) 能力库中挑选，构建自己的，或安装[第三方能力包](https://ai.pydantic.dev/extensibility)。完全使用 [YAML/JSON](https://ai.pydantic.dev/agent-spec) 定义 Agent —— 无需编写代码。

7. **支持 MCP、A2A 与 UI**：
集成 [模型上下文协议（MCP）](https://ai.pydantic.dev/mcp/overview)、[Agent-to-Agent (A2A)](https://ai.pydantic.dev/a2a) 以及各种 [UI 事件流](https://ai.pydantic.dev/ui/overview) 标准，让你的 Agent 能够访问外部工具和数据，与其他 Agent 互操作，并通过基于事件的流式通信构建交互式应用。

8. **人在回路（Human-in-the-Loop）工具审批**：
轻松标记某些工具调用[需要人工批准](https://ai.pydantic.dev/deferred-tools#human-in-the-loop-tool-approval)后才能执行，这可以基于工具参数、对话历史或用户偏好进行动态判断。

9. **持久化执行**：
使你能够构建 [持久化 Agent](https://ai.pydantic.dev/durable_execution/overview/)，在遭遇临时 API 故障、应用错误或重启时保留进度，并以生产级可靠性处理长耗时、异步及人在回路的工作流。

10. **流式输出**：
提供[流式传输](https://ai.pydantic.dev/output#streamed-results)结构化输出的能力，支持实时验证，确保你能即时获取生成的数据。

11. **图（Graph）支持**：
提供使用类型提示定义 [图结构](https://ai.pydantic.dev/graph) 的强大方式，适用于标准控制流容易退化为“面条代码”的复杂应用。

但说实话，再长的列表也不如[亲自试一试](#next-steps)来得有说服力！看看它能否打动你吧！

## Hello World 示例

以下是 Pydantic AI 的最小化示例：

```python
from pydantic_ai import Agent

# Define a very simple agent including the model to use, you can also set the model when running the agent.
agent = Agent(
    'anthropic:claude-sonnet-4-6',
    # Register static instructions using a keyword argument to the agent.
    # For more complex dynamically-generated instructions, see the example below.
    instructions='Be concise, reply with one sentence.',
)

# Run the agent synchronously, conducting a conversation with the LLM.
result = agent.run_sync('Where does "hello world" come from?')
print(result.output)
"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""
```

_(This example is complete, it can be run "as is", assuming you've [installed the `pydantic_ai` package](https://ai.pydantic.dev/install))_

交互过程将非常简短：Pydantic AI 会将指令和用户提示发送给 LLM，模型随后返回文本响应。

目前看起来还不太有趣，但你可以轻松添加 [工具](https://ai.pydantic.dev/tools)、[动态指令](https://ai.pydantic.dev/agents#instructions)、[结构化输出](https://ai.pydantic.dev/output) 或可组合的 [能力（Capabilities）](https://ai.pydantic.dev/capabilities)，以构建更强大的 Agent。

以下是添加了 [思考](https://ai.pydantic.dev/capabilities#thinking) 和 [Web 搜索](https://ai.pydantic.dev/capabilities#provider-adaptive-tools) 能力的同一 Agent：

```python
from pydantic_ai import Agent
from pydantic_ai.capabilities import Thinking, WebSearch

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    instructions='Be concise, reply with one sentence.',
    capabilities=[Thinking(), WebSearch()],
)

result = agent.run_sync('What was the mass of the largest meteorite found this year?')
print(result.output)
```

## 工具与依赖注入示例

下面是一个使用 Pydantic AI 为银行构建客服 Agent 的简洁示例：

**(Better documented example [in the docs](https://ai.pydantic.dev/#tools-dependency-injection-example))**

```python
from dataclasses import dataclass

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

from bank_database import DatabaseConn


# SupportDependencies is used to pass data, connections, and logic into the model that will be needed when running
# instructions and tool functions. Dependency injection provides a type-safe way to customise the behavior of your agents.
@dataclass
class SupportDependencies:
    customer_id: int
    db: DatabaseConn


# This Pydantic model defines the structure of the output returned by the agent.
class SupportOutput(BaseModel):
    support_advice: str = Field(description='Advice returned to the customer')
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description='Risk level of query', ge=0, le=10)


# This agent will act as first-tier support in a bank.
# Agents are generic in the type of dependencies they accept and the type of output they return.
# In this case, the support agent has type `Agent[SupportDependencies, SupportOutput]`.
support_agent = Agent(
    'openai:gpt-5.2',
    deps_type=SupportDependencies,
    # The response from the agent will be guaranteed to be a SupportOutput,
    # if validation fails the agent is prompted to try again.
    output_type=SupportOutput,
    instructions=(
        'You are a support agent in our bank, give the '
        'customer support and judge the risk level of their query.'
    ),
)


# Dynamic instructions can make use of dependency injection.
# Dependencies are carried via the `RunContext` argument, which is parameterized with the `deps_type` from above.
# If the type annotation here is wrong, static type checkers will catch it.
@support_agent.instructions
async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
    customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
    return f"The customer's name is {customer_name!r}"


# The `tool` decorator let you register functions which the LLM may call while responding to a user.
# Again, dependencies are carried via `RunContext`, any other arguments become the tool schema passed to the LLM.
# Pydantic is used to validate these arguments, and errors are passed back to the LLM so it can retry.
@support_agent.tool
async def customer_balance(
        ctx: RunContext[SupportDependencies], include_pending: bool
) -> float:
    """Returns the customer's current account balance."""
    # The docstring of a tool is also passed to the LLM as the description of the tool.
    # Parameter descriptions are extracted from the docstring and added to the parameter schema sent to the LLM.
    balance = await ctx.deps.db.customer_balance(
        id=ctx.deps.customer_id,
        include_pending=include_pending,
    )
    return balance


...  # In a real use case, you'd add more tools and a longer system prompt


async def main():
    deps = SupportDependencies(customer_id=123, db=DatabaseConn())
    # Run the agent asynchronously, conducting a conversation with the LLM until a final response is reached.
    # Even in this fairly simple case, the agent will exchange multiple messages with the LLM as tools are called to retrieve an output.
    result = await support_agent.run('What is my balance?', deps=deps)
    # The `result.output` will be validated with Pydantic to guarantee it is a `SupportOutput`. Since the agent is generic,
    # it'll also be typed as a `SupportOutput` to aid with static type checking.
    print(result.output)
    """
    support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1
    """

    result = await support_agent.run('I just lost my card!', deps=deps)
    print(result.output)
    """
    support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8
    """
```

## 下一步

想要亲自试用 Pydantic AI，请 [安装它](https://ai.pydantic.dev/install) 并按照 [示例中的说明](https://ai.pydantic.dev/examples/setup) 操作。

阅读 [文档](https://ai.pydantic.dev/agents/) 以了解如何使用 Pydantic AI 构建应用。

查阅 [API 参考手册](https://ai.pydantic.dev/api/agent/) 以熟悉 Pydantic AI 的接口。

如有任何疑问，欢迎加入 [Slack](https://logfire.pydantic.dev/docs/join-slack/) 或在 [GitHub](https://github.com/pydantic/pydantic-ai/issues) 提交 Issue。