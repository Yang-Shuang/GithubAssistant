<!--BEGIN_BANNER_IMAGE-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/.github/banner_dark.png">
  <source media="(prefers-color-scheme: light)" srcset="/.github/banner_light.png">
  <img style="width:100%;" alt="The LiveKit icon, the name of the repository and some sample code in the background." src="https://raw.githubusercontent.com/livekit/agents/main/.github/banner_light.png">
</picture>

<!--END_BANNER_IMAGE-->
<br />

![PyPI - Version](https://img.shields.io/pypi/v/livekit-agents)
[![PyPI Downloads](https://static.pepy.tech/badge/livekit-agents/month)](https://pepy.tech/projects/livekit-agents)
[![Slack community](https://img.shields.io/endpoint?url=https%3A%2F%2Flivekit.io%2Fbadges%2Fslack)](https://livekit.io/join-slack)
[![Twitter Follow](https://img.shields.io/twitter/follow/livekit)](https://twitter.com/livekit)
[![Ask DeepWiki for understanding the codebase](https://deepwiki.com/badge.svg)](https://deepwiki.com/livekit/agents)
[![License](https://img.shields.io/github/license/livekit/livekit)](https://github.com/livekit/livekit/blob/master/LICENSE)

<br />

正在寻找 JS/TS 库？请查看 [AgentsJS](https://github.com/livekit/agents-js)

## 什么是 Agents？

<!--BEGIN_DESCRIPTION-->

Agent 框架专为构建在服务器上运行的实时、可编程参与者而设计。你可以使用它来创建具备视觉、听觉和理解能力的对话式多模态语音代理（Agent）。

<!--END_DESCRIPTION-->

## 功能特性

- **灵活的集成**：提供丰富的生态系统，让你自由组合最适合场景的 STT、LLM、TTS 和 Realtime API。
- **集成的任务调度**：内置任务调度和分发机制，通过 [dispatch APIs](https://docs.livekit.io/agents/build/dispatch/) 将终端用户与代理连接起来。
- **丰富的 WebRTC 客户端支持**：基于 LiveKit 开源 SDK 生态系统构建客户端应用，全面支持各大主流平台。
- **电话集成**：无缝对接 LiveKit [电话栈](https://docs.livekit.io/sip/)，让你的代理能够拨打或接听电话。
- **与客户端交换数据**：使用 [RPCs](https://docs.livekit.io/home/client/data/rpc/) 和其他 [Data APIs](https://docs.livekit.io/home/client/data/) 与客户端无缝交换数据。
- **语义轮次检测**：采用 Transformer 模型检测用户发言是否结束，有效减少打断。
- **支持 MCP**：原生支持 MCP（Model Context Protocol）。仅需一行代码即可集成 MCP 服务器提供的工具。
- **内置测试框架**：编写测试用例并使用评估器（judges）确保代理按预期运行。
- **开源**：完全开源，允许你将整个技术栈部署在自己的服务器上，其中包括 [LiveKit server](https://github.com/livekit/livekit) 这一广泛使用的 WebRTC 媒体服务器。

## 安装

要安装核心 Agents 库以及常用模型提供商的插件：

```bash
pip install "livekit-agents[openai,silero,deepgram,cartesia,turn-detector]"
```

## 文档与指南

框架及其使用方法的完整文档请参见 [此处](https://docs.livekit.io/agents/)

### 配合 AI 编程代理开发

如果你正在使用 AI 编程助手来基于 LiveKit Agents 进行开发，我们推荐以下配置以获得最佳效果：

1. **安装 [LiveKit Docs MCP server](https://docs.livekit.io/mcp)** —— 让你的编程代理能够访问最新的 LiveKit 文档、跨仓库的代码搜索功能以及可运行的示例。

2. **安装 [LiveKit Agent Skill](https://github.com/livekit/agent-skills)** —— 为你的编程代理提供架构指导和构建语音 AI 应用的最佳实践，包括工作流设计、任务交接（handoffs）、任务分配和测试模式等。

   ```shell
   npx skills add livekit/agent-skills --skill livekit-agents
   ```

Agent Skill 与 MCP server 配合效果最佳：Skill 教会你的代理*如何着手*使用 LiveKit 进行开发，而 MCP server 则提供实现正确功能所需的*当前 API 详情*。

## 核心概念

- **Agent**：基于 LLM 的应用程序，具有明确的指令定义。
- **AgentSession**：管理终端用户交互的代理容器。
- **entrypoint（入口点）**：交互式会话的起点，类似于 Web 服务器中的请求处理器。
- **AgentServer**：负责协调任务调度并为用户会话启动代理的主进程。

## 使用示例

### 基础语音代理

---

```python
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    RunContext,
    cli,
    function_tool,
    inference,
)
from livekit.plugins import silero


@function_tool
async def lookup_weather(
    context: RunContext,
    location: str,
):
    """Used to look up weather information."""

    return {"weather": "sunny", "temperature": 70}


server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    session = AgentSession(
        vad=silero.VAD.load(),
        # any combination of STT, LLM, TTS, or realtime API can be used
        # this example shows LiveKit Inference, a unified API to access different models via LiveKit Cloud
        # to use model provider keys directly, replace with the following:
        # from livekit.plugins import deepgram, openai, cartesia
        # stt=deepgram.STT(model="nova-3"),
        # llm=openai.LLM(model="gpt-4.1-mini"),
        # tts=cartesia.TTS(model="sonic-3", voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc"),
        stt=inference.STT("deepgram/nova-3", language="multi"),
        llm=inference.LLM("openai/gpt-4.1-mini"),
        tts=inference.TTS("cartesia/sonic-3", voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc"),
    )

    agent = Agent(
        instructions="You are a friendly voice assistant built by LiveKit.",
        tools=[lookup_weather],
    )

    await session.start(agent=agent, room=ctx.room)
    await session.generate_reply(instructions="greet the user and ask about their day")


if __name__ == "__main__":
    cli.run_app(server)
```

运行此示例需要配置以下环境变量：

- LIVEKIT_URL
- LIVEKIT_API_KEY
- LIVEKIT_API_SECRET

### 多代理交接

---

此处代码已简化。完整示例请参见 [multi_agent.py](examples/voice_agents/multi_agent.py)

```python
...
class IntroAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=f"You are a story teller. Your goal is to gather a few pieces of information from the user to make the story personalized and engaging."
            "Ask the user for their name and where they are from"
        )

    async def on_enter(self):
        self.session.generate_reply(instructions="greet the user and gather information")

    @function_tool
    async def information_gathered(
        self,
        context: RunContext,
        name: str,
        location: str,
    ):
        """Called when the user has provided the information needed to make the story personalized and engaging.

        Args:
            name: The name of the user
            location: The location of the user
        """

        context.userdata.name = name
        context.userdata.location = location

        story_agent = StoryAgent(name, location)
        return story_agent, "Let's start the story!"


class StoryAgent(Agent):
    def __init__(self, name: str, location: str) -> None:
        super().__init__(
            instructions=f"You are a storyteller. Use the user's information in order to make the story personalized."
            f"The user's name is {name}, from {location}",
            # override the default model, switching to Realtime API from standard LLMs
            llm=openai.realtime.RealtimeModel(voice="echo"),
            chat_ctx=chat_ctx,
        )

    async def on_enter(self):
        self.session.generate_reply()


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    userdata = StoryData()
    session = AgentSession[StoryData](
        vad=silero.VAD.load(),
        stt="deepgram/nova-3",
        llm="openai/gpt-4.1-mini",
        tts="cartesia/sonic-3:9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
        userdata=userdata,
    )

    await session.start(
        agent=IntroAgent(),
        room=ctx.room,
    )
...
```

### 测试

自动化测试对于构建可靠的代理至关重要，尤其是考虑到 LLM 行为的不确定性。LiveKit Agents 提供了原生的测试集成，帮助你创建稳定可靠的 Agent。

```python
@pytest.mark.asyncio
async def test_no_availability() -> None:
    llm = google.LLM()
    async with AgentSession(llm=llm) as sess:
        await sess.start(MyAgent())
        result = await sess.run(
            user_input="Hello, I need to place an order."
        )
        result.expect.skip_next_event_if(type="message", role="assistant")
        result.expect.next_event().is_function_call(name="start_order")
        result.expect.next_event().is_function_call_output()
        await (
            result.expect.next_event()
            .is_message(role="assistant")
            .judge(llm, intent="assistant should be asking the user what they would like")
        )

```

## 示例项目

更多示例和详细的设置说明，请查看 [examples 目录](examples/)。如需更多示例，可访问 [python-agents-examples](https://github.com/livekit-examples/python-agents-examples) 仓库。

<table>
<tr>
<td width="50%">
<h3>🎙️ 基础代理</h3>
<p>专为语音对话优化的入门级代理。</p>
<p>
<a href="examples/voice_agents/basic_agent.py">代码</a>
</p>
</td>
<td width="50%">
<h3>🔄 多用户按住说话</h3>
<p>通过按住说话（Push-to-Talk）响应房间内的多个用户。</p>
<p>
<a href="examples/voice_agents/push_to_talk.py">代码</a>
</p>
</td>
</tr>

<tr>
<td width="50%">
<h3>🎵 背景环境音</h3>
<p>添加背景氛围音与思考音效，提升真实感。</p>
<p>
<a href="examples/voice_agents/background_audio.py">代码</a>
</p>
</td>
<td width="50%">
<h3>🛠️ 动态工具创建</h3>
<p>动态生成函数工具（Function Tools）。</p>
<p>
<a href="examples/voice_agents/dynamic_tool_creation.py">代码</a>
</p>
</td>
</tr>

<tr>
<td width="50%">
<h3>☎️ 外呼代理</h3>
<p>支持主动拨打电话的代理。</p>
<p>
<a href="https://github.com/livekit-examples/outbound-caller-python">代码</a>
</p>
</td>
<td width="50%">
<h3>📋 结构化输出</h3>
<p>利用 LLM 的结构化输出来引导 TTS 的语气。</p>
<p>
<a href="examples/voice_agents/structured_output.py">代码</a>
</p>
</td>
</tr>

<tr>
<td width="50%">
<h3>🔌 MCP 支持</h3>
<p>使用来自 MCP 服务器的工具。</p>
<p>
<a href="examples/voice_agents/mcp">代码</a>
</p>
</td>
<td width="50%">
<h3>💬 纯文本代理</h3>
跳过语音功能，直接使用相同代码实现纯文本集成。</p>
<p>
<a href="examples/other/text_only.py">代码</a>
</p>
</td>
</tr>

<tr>
<td width="50%">
<h3>📝 多用户语音转写</h3>
<p>生成房间内所有用户的实时转写文本。</p>
<p>
<a href="examples/other/transcription/multi-user-transcriber.py">代码</a>
</p>
</td>
<td width="50%">
<h3>🎥 视频虚拟形象</h3>
<p>集成 Tavus、Bithuman、LemonSlice 等 AI 数字人服务。</p>
<p>
<a href="examples/avatar_agents/">代码</a>
</p>
</td>
</tr>

<tr>
<td width="50%">
<h3>🍽️ 餐厅点餐与预订</h3>
<p>完整示例：处理餐厅电话订餐的代理。</p>
<p>
<a href="examples/voice_agents/restaurant_agent.py">代码</a>
</p>
</td>
<td width="50%">
<h3>👁️ Gemini Live 视觉识别</h3>
<p>完整示例（含 iOS App）：具备视觉能力的 Gemini Live 代理。</p>
<p>
<a href="https://github.com/livekit-examples/vision-demo">代码</a>
</p>
</td>
</tr>

</table>

## 运行你的代理

### 在终端中测试

```shell
python myagent.py console
```

以终端模式运行你的代理，启用本地音频输入和输出以便进行测试。此模式无需外部服务器或依赖项，非常适合快速验证行为逻辑。

### 配合 LiveKit 客户端开发

```shell
python myagent.py dev
```

启动代理服务器并在文件更改时启用热重载。此模式下每个进程可高效托管多个并发代理。

代理将连接至 LiveKit Cloud 或你的自建服务器。请设置以下环境变量：
- LIVEKIT_URL
- LIVEKIT_API_KEY
- LIVEKIT_API_SECRET

你可以使用任何 LiveKit 客户端 SDK 或电话集成进行连接。要快速上手，可尝试 [Agents Playground](https://agents-playground.livekit.io/)。

### 生产环境运行

```shell
python myagent.py start
```

以生产环境优化配置运行代理。

## 贡献指南

Agent 框架正处于快速演进的活跃开发阶段。我们欢迎并感谢任何形式的贡献，包括反馈、Bug 修复、新功能、新插件与工具或更完善的文档。你可以在本仓库提交 Issue、发起 PR，或在 [LiveKit 社区](https://docs.livekit.io/intro/community/) 与我们交流。

### 开发环境配置

本项目使用 [uv](https://docs.astral.sh/uv/) 进行包管理。安装开发依赖：

```shell
uv sync --all-extras --dev
```

### 示例项目

本项目在 [`examples`](examples/) 目录中包含大量示例。运行前，请创建 `examples/.env` 文件并填入 LiveKit Server 及所需模型提供商的凭证（参考 `examples/.env.example`），然后执行：

```shell
uv run examples/voice_agents/basic_agent.py dev
```

更多信息请参阅 [examples README](examples/README.md)。

### 测试

单元测试位于 `tests` 目录中，可通过以下命令运行：

```shell
uv run pytest tests/test_tools.py
```

各插件的集成测试需要相应的 API 凭证，并由项目维护者提交 PR 时在 GitHub CI 中自动运行。详情请参见 [tests workflow](.github/workflows/tests.yml)。

### 代码格式化

本项目使用 [ruff](https://github.com/astral-sh/ruff) 进行格式化和代码检查：

```shell
uv run ruff format
uv run ruff check --fix
```

### 文档生成

使用 [pdoc](https://github.com/pdoc3/pdoc) 在本地生成文档：

```shell
uv sync --all-extras --group docs
uv run --active pdoc --skip-errors --html --output-dir=docs livekit
```

<!--BEGIN_REPO_NAV-->
<br/><table>
<thead><tr><th colspan="2">LiveKit 生态系统</th></tr></thead>
<tbody>
<tr><td>Agents SDKs</td><td><b>Python</b> · <a href="https://github.com/livekit/agents-js">Node.js</a></td></tr><tr></tr>
<tr><td>LiveKit SDKs</td><td><a href="https://github.com/livekit/client-sdk-js">Browser</a> · <a href="https://github.com/livekit/client-sdk-swift">Swift</a> · <a href="https://github.com/livekit/client-sdk-android">Android</a> · <a href="https://github.com/livekit/client-sdk-flutter">Flutter</a> · <a href="https://github.com/livekit/client-sdk-react-native">React Native</a> · <a href="https://github.com/livekit/rust-sdks">Rust</a> · <a href="https://github.com/livekit/node-sdks">Node.js</a> · <a href="https://github.com/livekit/python-sdks">Python</a> · <a href="https://github.com/livekit/client-sdk-unity">Unity</a> · <a href="https://github.com/livekit/client-sdk-unity-web">Unity (WebGL)</a> · <a href="https://github.com/livekit/client-sdk-esp32">ESP32</a> · <a href="https://github.com/livekit/client-sdk-cpp">C++</a></td></tr><tr></tr>
<tr><td>Starter Apps</td><td><a href="https://github.com/livekit-examples/agent-starter-python">Python Agent</a> · <a href="https://github.com/livekit-examples/agent-starter-node">TypeScript Agent</a> · <a href="https://github.com/livekit-examples/agent-starter-react">React App</a> · <a href="https://github.com/livekit-examples/agent-starter-swift">SwiftUI App</a> · <a href="https://github.com/livekit-examples/agent-starter-android">Android App</a> · <a href="https://github.com/livekit-examples/agent-starter-flutter">Flutter App</a> · <a href="https://github.com/livekit-examples/agent-starter-react-native">React Native App</a> · <a href="https://github.com/livekit-examples/agent-starter-embed">Web Embed</a></td></tr><tr></tr>
<tr><td>UI Components</td><td><a href="https://github.com/livekit/components-js">React</a> · <a href="https://github.com/livekit/components-android">Android Compose</a> · <a href="https://github.com/livekit/components-swift">SwiftUI</a> · <a href="https://github.com/livekit/components-flutter">Flutter</a></td></tr><tr></tr>
<tr><td>Server APIs</td><td><a href="https://github.com/livekit/node-sdks">Node.js</a> · <a href="https://github.com/livekit/server-sdk-go">Golang</a> · <a href="https://github.com/livekit/server-sdk-ruby">Ruby</a> · <a href="https://github.com/livekit/server-sdk-kotlin">Java/Kotlin</a> · <a href="https://github.com/livekit/python-sdks">Python</a> · <a href="https://github.com/livekit/rust-sdks">Rust</a> · <a href="https://github.com/agence104/livekit-server-sdk-php">PHP (community)</a> · <a href="https://github.com/pabloFuente/livekit-server-sdk-dotnet">.NET (community)</a></td></tr><tr></tr>
<tr><td>Resources</td><td><a href="https://docs.livekit.io">Docs</a> · <a href="https://docs.livekit.io/mcp">Docs MCP Server</a> · <a href="https://github.com/livekit/livekit-cli">CLI</a> · <a href="https://cloud.livekit.io">LiveKit Cloud</a></td></tr><tr></tr>
<tr><td>LiveKit Server OSS</td><td><a href="https://github.com/livekit/livekit">LiveKit server</a> · <a href="https://github.com/livekit/egress">Egress</a> · <a href="https://github.com/livekit/ingress">Ingress</a> · <a href="https://github.com/livekit/sip">SIP</a></td></tr><tr></tr>
<tr><td>Community</td><td><a href="https://community.livekit.io">Developer Community</a> · <a href="https://livekit.io/join-slack">Slack</a> · <a href="https://x.com/livekit">X</a> · <a href="https://www.youtube.com/@livekit_io">YouTube</a></td></tr>
</tbody>
</table>
<!--END_REPO_NAV-->