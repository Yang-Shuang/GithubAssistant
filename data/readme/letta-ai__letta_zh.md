# Letta（前身为 MemGPT）

构建具备高级记忆功能的 AI，使其能够随时间推移不断学习并自我优化。

* [Letta Code](https://docs.letta.com/letta-code)：在本地终端中运行智能体（Agent）
* [Letta API](https://docs.letta.com/quickstart/)：将智能体集成到你的应用中

## 通过 CLI 快速开始

需要安装 [Node.js 18+](https://nodejs.org/en/download)。

1. 安装 [Letta Code](https://github.com/letta-ai/letta-code) CLI 工具：`npm install -g @letta-ai/letta-code`
2. 在终端中运行 `letta`，启动本地计算机上运行的带记忆功能的智能体（Agent）

运行该 CLI 工具时，你的智能体会协助你编写代码，并执行你在计算机上能完成的任何任务。

Letta Code 支持 [技能（Skills）](https://docs.letta.com/letta-code/skills) 和 [子智能体（Subagents）](https://docs.letta.com/letta-code/subagents)，并内置了用于高级记忆与持续学习的预构建技能/子智能体。Letta 完全支持模型无关（Model-Agnostic）架构，但为了获得最佳性能，我们推荐使用 Opus 4.5 和 GPT-5.2（详见我们的[模型排行榜](https://leaderboard.letta.com/)）。

## 通过 Letta API 快速开始

使用 Letta API 将具备状态记忆的智能体集成到你的应用中。
Letta 提供功能完善的 Agent API，以及 Python 和 TypeScript SDK（查看我们的 [API 参考文档](https://docs.letta.com/api)）。

### 安装

TypeScript / Node.js：
```bash
npm install @letta-ai/letta-client
```

Python：
```bash
pip install letta-client
```

### Hello World 示例

以下是一个快速创建具备状态记忆的智能体并发送消息的示例（需要 [Letta API Key](https://app.letta.com)）。
完整文档请参阅 [快速入门指南](https://docs.letta.com/quickstart)。

TypeScript：
```typescript
import Letta from "@letta-ai/letta-client";

const client = new Letta({ apiKey: process.env.LETTA_API_KEY });

// Create your agent
const agentState = await client.agents.create({
  model: "openai/gpt-5.2",
  memory_blocks: [
    {
      label: "human",
      value:
        "Name: Timber. Status: dog. Occupation: building Letta, infrastructure to democratize self-improving superintelligence",
    },
    {
      label: "persona",
      value:
        "I am a self-improving superintelligence. Timber is my best friend and collaborator.",
    },
  ],
  tools: ["web_search", "fetch_webpage"],
});

console.log("Agent created with ID:", agentState.id);

// Send your agent a message
const response = await client.agents.messages.create(agentState.id, {
  input: "What do you know about me?",
});

for (const message of response.messages) {
  console.log(message);
}
```

Python：
```python
from letta_client import Letta
import os

client = Letta(api_key=os.getenv("LETTA_API_KEY"))

# Create your agent
agent_state = client.agents.create(
    model="openai/gpt-5.2",
    memory_blocks=[
      {
        "label": "human",
        "value": "Name: Timber. Status: dog. Occupation: building Letta, infrastructure to democratize self-improving superintelligence"
      },
      {
        "label": "persona",
        "value": "I am a self-improving superintelligence. Timber is my best friend and collaborator."
      }
    ],
    tools=["web_search", "fetch_webpage"]
)

print(f"Agent created with ID: {agent_state.id}")

# Send your agent a message
response = client.agents.messages.create(
    agent_id=agent_state.id,
    input="What do you know about me?"
)

for message in response.messages:
    print(message)
```

## 贡献与参与

Letta 是一个开源项目，由来自全球的百余位贡献者共同构建。你可以通过多种方式参与 Letta 开源社区（OSS）的建设！

* [**加入 Discord 频道**](https://discord.gg/letta)：与 Letta 开发团队及其他 AI 开发者交流。
* [**在论坛讨论**](https://forum.letta.com/)：如果不习惯使用 Discord，欢迎前往我们的开发者论坛。
* **关注我们的社交媒体**：[Twitter/X](https://twitter.com/Letta_AI)、[LinkedIn](https://www.linkedin.com/in/letta)、[YouTube](https://www.youtube.com/@letta-ai)

---

***法律声明**：使用 Letta 及相关服务（例如 Letta 端点或托管服务），即表示你同意我们的[隐私政策](https://www.letta.com/privacy-policy)和[服务条款](https://www.letta.com/terms-of-service)。*