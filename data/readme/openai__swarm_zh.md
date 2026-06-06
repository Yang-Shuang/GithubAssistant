![Swarm Logo](assets/logo.png)

# Swarm（实验性，教育用途）

> [!IMPORTANT]
> Swarm 现已由 [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) 取代，后者是 Swarm 的生产就绪版演进版本。Agents SDK 具备关键改进，并将由 OpenAI 团队积极维护。
>
> 我们建议将所有生产用途迁移至 Agents SDK。

## Install（安装）

Requires Python 3.10+ -> 需要 Python 3.10 或更高版本

```shell
pip install git+ssh://git@github.com/openai/swarm.git
```

or -> 或者

```shell
pip install git+https://github.com/openai/swarm.git
```

## Usage（使用示例）

```python
from swarm import Swarm, Agent

client = Swarm()

def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

print(response.messages[-1]["content"])
```

```
Hope glimmers brightly,
New paths converge gracefully,
What can I assist?
```

## Table of Contents（目录）

- [Overview](#overview) -> - [概述](#overview)
- [Examples](#examples) -> - [示例](#examples)
- [Documentation](#documentation) -> - [文档](#documentation)
  - [Running Swarm](#running-swarm) ->   - [运行 Swarm](#running-swarm)
  - [Agents](#agents) ->   - [智能体（Agent）](#agents)
  - [Functions](#functions) ->   - [函数（Functions）](#functions)
  - [Streaming](#streaming) ->   - [流式传输（Streaming）](#streaming)
- [Evaluations](#evaluations) -> - [评估](#evaluations)
- [Utils](#utils) -> - [工具（Utils）](#utils)

# Overview（概述）

Swarm focuses on making agent **coordination** and **execution** lightweight, highly controllable, and easily testable. -> Swarm 专注于使智能体（Agent）的**协调**与**执行**保持轻量、高度可控且易于测试。

It accomplishes this through two primitive abstractions: `Agent`s and **handoffs**. An `Agent` encompasses `instructions` and `tools`, and can at any point choose to hand off a conversation to another `Agent`. -> 它通过两个基础抽象实现这一目标：`Agent` 和**交接（handoff）**。一个 `Agent` 包含 `instructions`（指令）和工具，并可以在任何时候选择将对话交接给另一个 `Agent`。

These primitives are powerful enough to express rich dynamics between tools and networks of agents, allowing you to build scalable, real-world solutions while avoiding a steep learning curve. -> 这些基础概念足以表达工具和智能体网络之间丰富的动态交互，让你能够构建可扩展的、面向现实世界的解决方案，同时避免陡峭的学习曲线。

> [!NOTE]
> Swarm Agents are not related to Assistants in the Assistants API. They are named similarly for convenience, but are otherwise completely unrelated. Swarm is entirely powered by the Chat Completions API and is hence stateless between calls. -> > [!NOTE] Swarm 智能体与 Assistants API 中的助手（Assistants）无关。它们仅因命名相似而便于称呼，但除此之外完全无关。Swarm 完全由 Chat Completions API 驱动，因此在调用之间是无状态的。

## Why Swarm（为什么选择 Swarm）

Swarm explores patterns that are lightweight, scalable, and highly customizable by design. Approaches similar to Swarm are best suited for situations dealing with a large number of independent capabilities and instructions that are difficult to encode into a single prompt. -> Swarm 探索轻量级、可扩展且设计上高度可定制的架构模式。与 Swarm 类似的方法最适合处理大量独立功能和指令的场景，这些内容难以编码到单个提示词（prompt）中。

The Assistants API is a great option for developers looking for fully-hosted threads and built in memory management and retrieval. However, Swarm is an educational resource for developers curious to learn about multi-agent orchestration. Swarm runs (almost) entirely on the client and, much like the Chat Completions API, does not store state between calls. -> Assistants API 是那些寻求完全托管线程及内置记忆管理和检索功能的开发者的绝佳选择。然而，Swarm 旨在作为教育性资源，帮助开发者探索多智能体编排技术。Swarm 几乎完全在客户端运行，与 Chat Completions API 类似，调用之间不会保存状态。

# Examples（示例）

Check out `/examples` for inspiration! Learn more about each one in its README. -> 查看 `/examples` 目录获取灵感！你可以在其 README 中了解每个示例的详细信息。

- [`basic`](examples/basic): Simple examples of fundamentals like setup, function calling, handoffs, and context variables -> - [`basic`](examples/basic)：基础概念（如设置、函数调用、交接和上下文变量）的简单示例
- [`triage_agent`](examples/triage_agent): Simple example of setting up a basic triage step to hand off to the right agent -> - [`triage_agent`](examples/triage_agent)：设置基本分诊步骤以将对话交接给合适智能体的简单示例
- [`weather_agent`](examples/weather_agent): Simple example of function calling -> - [`weather_agent`](examples/weather_agent)：函数调用的简单示例
- [`airline`](examples/airline): A multi-agent setup for handling different customer service requests in an airline context. -> - [`airline`](examples/airline)：用于处理航空公司场景下不同客户服务请求的多智能体设置。
- [`support_bot`](examples/support_bot): A customer service bot which includes a user interface agent and a help center agent with several tools -> - [`support_bot`](examples/support_bot)：包含用户界面智能体和帮助中心智能体的客服机器人，配备多种工具
- [`personal_shopper`](examples/personal_shopper): A personal shopping agent that can help with making sales and refunding orders -> - [`personal_shopper`](examples/personal_shopper)：可协助完成销售与订单退款个人购物智能体

# Documentation（文档）

![Swarm Diagram](assets/swarm_diagram.png)

## Running Swarm（运行 Swarm）

Start by instantiating a Swarm client (which internally just instantiates an `OpenAI` client). -> 首先实例化一个 Swarm 客户端（其内部仅实例化了一个 `OpenAI` 客户端）。

```python
from swarm import Swarm

client = Swarm()
```

### `client.run()`

Swarm's `run()` function is analogous to the `chat.completions.create()` function in the Chat Completions API – it takes `messages` and returns `messages` and saves no state between calls. Importantly, however, it also handles Agent function execution, hand-offs, context variable references, and can take multiple turns before returning to the user. -> Swarm 的 `run()` 函数类似于 Chat Completions API 中的 `chat.completions.create()` 函数——它接收 `messages`（消息）并返回 `messages`，且在调用之间不保存状态。但重要的是，它还负责处理智能体函数执行、交接操作、上下文变量引用，并且可以在返回给用户之前进行多轮交互。

At its core, Swarm's `client.run()` implements the following loop: -> 本质上，Swarm 的 `client.run()` 实现了以下循环：
1. Get a completion from the current Agent -> 1. 获取当前智能体的补全结果
2. Execute tool calls and append results -> 2. 执行工具调用并追加结果
3. Switch Agent if necessary -> 3. 必要时切换智能体
4. Update context variables, if necessary -> 4. 更新上下文变量（如需要）
5. If no new function calls, return -> 5. 若无新函数调用，则返回

#### Arguments（参数）

| Argument              | Type    | Description                                                                                                                                            | Default        |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| **agent**             | `Agent` | The (initial) agent to be called.                                                                                                                      | （必填）     |
| **messages**          | `List`  | A list of message objects, identical to [Chat Completions `messages`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages) | （必填）     |
| **context_variables** | `dict`  | A dictionary of additional context variables, available to functions and Agent instructions                                                            | `{}`           |
| **max_turns**         | `int`   | The maximum number of conversational turns allowed                                                                                                     | `float("inf")` |
| **model_override**    | `str`   | An optional string to override the model being used by an Agent                                                                                        | `None`         |
| **execute_tools**     | `bool`  | If `False`, interrupt execution and immediately returns `tool_calls` message when an Agent tries to call a function                                    | `True`         |
| **stream**            | `bool`  | If `True`, enables streaming responses                                                                                                                 | `False`        |
| **debug**             | `bool`  | If `True`, enables debug logging                                                                                                                       | `False`        |

Once `client.run()` is finished (after potentially multiple calls to agents and tools) it will return a `Response` containing all the relevant updated state. Specifically, the new `messages`, the last `Agent` to be called, and the most up-to-date `context_variables`. You can pass these values (plus new user messages) in to your next execution of `client.run()` to continue the interaction where it left off – much like `chat.completions.create()`. (The `run_demo_loop` function implements an example of a full execution loop in `/swarm/repl/repl.py`.) -> 当 `client.run()` 执行完毕（可能经过多次智能体和工具调用）后，它将返回一个包含所有相关更新状态的 `Response` 对象。具体包括新的 `messages`、最后被调用的 `Agent`，以及最新的 `context_variables`。你可以将这些值（加上新的用户消息）传入下一次 `client.run()` 执行中，以继续之前的交互——这与 `chat.completions.create()` 类似。（`run_demo_loop` 函数在 `/swarm/repl/repl.py` 中提供了一个完整执行循环的示例。）

#### `Response` Fields（`Response` 字段）

| Field                 | Type    | Description                                                                                                                                                                                                                                                                  |
| --------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **messages**          | `List`  | A list of message objects generated during the conversation. Very similar to [Chat Completions `messages`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages), but with a `sender` field indicating which `Agent` the message originated from. |
| **agent**             | `Agent` | The last agent to handle a message.                                                                                                                                                                                                                                          |
| **context_variables** | `dict`  | The same as the input variables, plus any changes.                                                                                                                                                                                                                           |

## Agents（智能体）

An `Agent` simply encapsulates a set of `instructions` with a set of `functions` (plus some additional settings below), and has the capability to hand off execution to another `Agent`. -> `Agent` 仅封装了一组 `instructions`（指令）和一组 `functions`（函数）（以及下方的一些额外设置），并具备将执行权交接给另一个 `Agent` 的能力。

While it's tempting to personify an `Agent` as "someone who does X", it can also be used to represent a very specific workflow or step defined by a set of `instructions` and `functions` (e.g. a set of steps, a complex retrieval, single step of data transformation, etc). This allows `Agent`s to be composed into a network of "agents", "workflows", and "tasks", all represented by the same primitive. -> 虽然很容易将 `Agent` 拟人化为“做某事的人”，但它也可用于表示由一组 `instructions` 和 `functions` 定义的特定工作流或步骤（例如一系列步骤、复杂检索、单步数据转换等）。这使得 `Agent` 可以组合成由相同基础概念表示的“智能体”、“工作流”和“任务”网络。

## `Agent` Fields（`Agent` 字段）

| Field            | Type                     | Description                                                                   | Default                      |
| ---------------- | ------------------------ | ----------------------------------------------------------------------------- | ---------------------------- |
| **name**         | `str`                    | The name of the agent.                                                        | `"Agent"`                    |
| **model**        | `str`                    | The model to be used by the agent.                                            | `"gpt-4o"`                   |
| **instructions** | `str` or `func() -> str` | Instructions for the agent, can be a string or a callable returning a string. | `"You are a helpful agent."` |
| **functions**    | `List`                   | A list of functions that the agent can call.                                  | `[]`                         |
| **tool_choice**  | `str`                    | The tool choice for the agent, if any.                                        | `None`                       |

### Instructions（指令）

`Agent` `instructions` are directly converted into the `system` prompt of a conversation (as the first message). Only the `instructions` of the active `Agent` will be present at any given time (e.g. if there is an `Agent` handoff, the `system` prompt will change, but the chat history will not.) -> `Agent` 的 `instructions` 会直接转换为对话的 `system` 提示词（作为第一条消息）。在任何给定时间，只有当前活跃 `Agent` 的 `instructions` 会出现（例如，发生 `Agent` 交接时，`system` 提示词会更改，但聊天历史不会。）

```python
agent = Agent(
   instructions="You are a helpful agent."
)
```

The `instructions` can either be a regular `str`, or a function that returns a `str`. The function can optionally receive a `context_variables` parameter, which will be populated by the `context_variables` passed into `client.run()`. -> `instructions` 可以是普通的 `str`，也可以是返回 `str` 的函数。该函数可选择接收一个 `context_variables` 参数，它将由传入 `client.run()` 的 `context_variables` 填充。

```python
def instructions(context_variables):
   user_name = context_variables["user_name"]
   return f"Help the user, {user_name}, do whatever they want."

agent = Agent(
   instructions=instructions
)
response = client.run(
   agent=agent,
   messages=[{"role":"user", "content": "Hi!"}],
   context_variables={"user_name":"John"}
)
print(response.messages[-1]["content"])
```

```
Hi John, how can I assist you today?
```

## Functions（函数）

- Swarm `Agent`s can call python functions directly. -> - Swarm `Agent` 可直接调用 Python 函数。
- Function should usually return a `str` (values will be attempted to be cast as a `str`). -> - 函数通常应返回一个 `str`（值将尝试转换为字符串）。
- If a function returns an `Agent`, execution will be transferred to that `Agent`. -> - 如果函数返回一个 `Agent`，执行权将转移至该 `Agent`。
- If a function defines a `context_variables` parameter, it will be populated by the `context_variables` passed into `client.run()`. -> - 如果函数定义了 `context_variables` 参数，它将由传入 `client.run()` 的 `context_variables` 填充。

```python
def greet(context_variables, language):
   user_name = context_variables["user_name"]
   greeting = "Hola" if language.lower() == "spanish" else "Hello"
   print(f"{greeting}, {user_name}!")
   return "Done"

agent = Agent(
   functions=[greet]
)

client.run(
   agent=agent,
   messages=[{"role": "user", "content": "Usa greet() por favor."}],
   context_variables={"user_name": "John"}
)
```

```
Hola, John!
```

- If an `Agent` function call has an error (missing function, wrong argument, error) an error response will be appended to the chat so the `Agent` can recover gracefully. -> - 若 `Agent` 函数调用出错（缺少函数、参数错误等），将追加一条错误响应到聊天中，以便 `Agent` 优雅恢复。
- If multiple functions are called by the `Agent`, they will be executed in that order. -> - 若 `Agent` 调用了多个函数，它们将按照顺序执行。

### Handoffs and Updating Context Variables（交接与更新上下文变量）

An `Agent` can hand off to another `Agent` by returning it in a `function`. -> `Agent` 可以通过在 `function`（函数）中返回另一个 `Agent` 来实现交接。

```python
sales_agent = Agent(name="Sales Agent")

def transfer_to_sales():
   return sales_agent

agent = Agent(functions=[transfer_to_sales])

response = client.run(agent, [{"role":"user", "content":"Transfer me to sales."}])
print(response.agent.name)
```

```
Sales Agent
```

It can also update the `context_variables` by returning a more complete `Result` object. This can also contain a `value` and an `agent`, in case you want a single function to return a value, update the agent, and update the context variables (or any subset of the three). -> 它还可以通过返回更完整的 `Result` 对象来更新 `context_variables`。如果你希望单个函数同时返回值、更改智能体并更新上下文变量（或其中任意组合），该对象也可包含 `value` 和 `agent`。

```python
sales_agent = Agent(name="Sales Agent")

def talk_to_sales():
   print("Hello, World!")
   return Result(
       value="Done",
       agent=sales_agent,
       context_variables={"department": "sales"}
   )

agent = Agent(functions=[talk_to_sales])

response = client.run(
   agent=agent,
   messages=[{"role": "user", "content": "Transfer me to sales"}],
   context_variables={"user_name": "John"}
)
print(response.agent.name)
print(response.context_variables)
```

```
Sales Agent
{'department': 'sales', 'user_name': 'John'}
```

> [!NOTE]
> If an `Agent` calls multiple functions to hand-off to an `Agent`, only the last handoff function will be used. -> > [!NOTE] 若 `Agent` 调用多个函数来交接至另一个 `Agent`，仅最后一个交接函数会被使用。

### Function Schemas（函数架构）

Swarm automatically converts functions into a JSON Schema that is passed into Chat Completions `tools`. -> Swarm 会自动将函数转换为 JSON Schema，并传递给 Chat Completions `tools`。
- Docstrings are turned into the function `description`. -> - 文档字符串（Docstring）会转换为函数的 `description`。
- Parameters without default values are set to `required`. -> - 没有默认值的参数会被设为 `required`。
- Type hints are mapped to the parameter's `type` (and default to `string`). -> - 类型提示将映射到参数的 `type`（默认为 `string`）。
- Per-parameter descriptions are not explicitly supported, but should work similarly if just added in the docstring. (In the future docstring argument parsing may be added.) -> - 不支持显式的逐参数描述，但若仅在文档字符串中添加，效果应类似。（未来可能会添加文档字符串的参数解析功能。）

```python
def greet(name, age: int, location: str = "New York"):
   """Greets the user. Make sure to get their name and age before calling.

   Args:
      name: Name of the user.
      age: Age of the user.
      location: Best place on earth.
   """
   print(f"Hello {name}, glad you are {age} in {location}!")
```

```javascript
{
   "type": "function",
   "function": {
      "name": "greet",
      "description": "Greets the user. Make sure to get their name and age before calling.\n\nArgs:\n   name: Name of the user.\n   age: Age of the user.\n   location: Best place on earth.",
      "parameters": {
         "type": "object",
         "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "location": {"type": "string"}
         },
         "required": ["name", "age"]
      }
   }
}
```

## Streaming（流式传输）

```python
stream = client.run(agent, messages, stream=True)
for chunk in stream:
   print(chunk)
```

Uses the same events as [Chat Completions API streaming](https://platform.openai.com/docs/api-reference/streaming). See `process_and_print_streaming_response` in `/swarm/repl/repl.py` as an example. -> 使用与 [Chat Completions API 流式传输](https://platform.openai.com/docs/api-reference/streaming) 相同的事件。参见 `/swarm/repl/repl.py` 中的 `process_and_print_streaming_response` 作为示例。

Two new event types have been added: -> 新增两种事件类型：
- `{"delim":"start"}` and `{"delim":"end"}`, to signal each time an `Agent` handles a single message (response or function call). This helps identify switches between `Agent`s. -> - `{"delim":"start"}` 和 `{"delim":"end"}`：用于标记每次 `Agent` 处理单条消息（响应或函数调用）的开始与结束。这有助于识别 `Agent` 之间的切换。
- `{"response": Response}` will return a `Response` object at the end of a stream with the aggregated (complete) response, for convenience. -> - `{"response": Response}`：在流结束时返回一个包含聚合（完整）响应的 `Response` 对象，方便使用。

# Evaluations（评估）

Evaluations are crucial to any project, and we encourage developers to bring their own eval suites to test the performance of their swarms. For reference, we have some examples for how to eval swarm in the `airline`, `weather_agent` and `triage_agent` quickstart examples. See the READMEs for more details. -> 评估对于任何项目都至关重要，我们鼓励开发者使用自己的测试套件来验证其 Swarm 的性能。作为参考，我们在 `airline`、`weather_agent` 和 `triage_agent` 快速入门示例中提供了一些如何评估 Swarm 的示例。更多详情请参阅各 README。

# Utils（工具）

Use the `run_demo_loop` to test out your swarm! This will run a REPL on your command line. Supports streaming. -> 使用 `run_demo_loop` 来测试你的 Swarm！它将在命令行中运行一个 REPL。支持流式传输。

```python
from swarm.repl import run_demo_loop
...
run_demo_loop(agent, stream=True)
```

# Core Contributors（核心贡献者）

- Ilan Bigio - [ibigio](https://github.com/ibigio)
- James Hills - [jhills20](https://github.com/jhills20)
- Shyamal Anadkat - [shyamal-anadkat](https://github.com/shyamal-anadkat)
- Charu Jaiswal - [charuj](https://github.com/charuj)
- Colin Jarvis - [colin-openai](https://github.com/colin-openai)
- Katia Gil Guzman - [katia-openai](https://github.com/katia-openai)