# 12-Factor Agent：构建可靠 LLM 应用的原则

<div align="center">
<a href="https://www.apache.org/licenses/LICENSE-2.0">
        <img src="https://img.shields.io/badge/Code-Apache%202.0-blue.svg" alt="Code License: Apache 2.0"></a>
<a href="https://creativecommons.org/licenses/by-sa/4.0/">
        <img src="https://img.shields.io/badge/Content-CC%20BY--SA%204.0-lightgrey.svg" alt="Content License: CC BY-SA 4.0"></a>
<a href="https://humanlayer.dev/discord">
    <img src="https://img.shields.io/badge/chat-discord-5865F2" alt="Discord Server"></a>
<a href="https://www.youtube.com/watch?v=8kMaTybvDUw">
    <img src="https://img.shields.io/badge/aidotengineer-conf_talk_(17m)-white" alt="YouTube
Deep Dive"></a>
<a href="https://www.youtube.com/watch?v=yxJDyQ8v6P0">
    <img src="https://img.shields.io/badge/youtube-deep_dive-crimson" alt="YouTube
Deep Dive"></a>
    
</div>

<p></p>

*秉承《十二要素应用》（12 Factor Apps）的精神。本项目的源代码公开于 https://github.com/humanlayer/12-factor-agents，欢迎提供反馈与贡献。让我们一起摸索出最佳实践！*

> [!TIP]
> 错过了 AI Engineer World's Fair？[在这里观看演讲](https://www.youtube.com/watch?v=8kMaTybvDUw)
>
> 寻找上下文工程相关内容？[直接跳转至要素 3](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)
>
> 想为 `npx/uvx create-12-factor-agent` 做出贡献？查看 [讨论帖](https://github.com/humanlayer/12-factor-agents/discussions/61)


<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=2acad99a-c2d9-48df-86f5-9ca8061b7bf9" />

<a href="#visual-nav"><img width="907" alt="Screenshot 2025-04-03 at 2 49 07 PM" src="https://github.com/user-attachments/assets/23286ad8-7bef-4902-b371-88ff6a22e998" /></a>


你好，我是 Dex。我[折腾][https://youtu.be/8bIHcttkOTE] 人工智能智能体（AI Agents）已经[有一段时间了][https://humanlayer.dev] 。 

**我尝试过市面上所有的 Agent 框架**，从开箱即用的 CrewAI/LangChain，到极简的 SmolAgents，再到号称“生产级”的 LangGraph、Griptape 等。 

**我和许多非常优秀的创始人聊过**，无论是否出自 Y Combinator 孵化器，他们都在用 AI 构建令人印象深刻的项目。其中大多数人都是自己从头搭建技术栈。我在面向客户的生产级 Agent 产品中很少看到直接使用现成框架的情况。

**令我惊讶的是**，市面上大多数自称“AI Agents”的产品其实并不具备真正的自主性。它们大多由确定性代码组成，仅在关键节点嵌入 LLM 步骤，以带来真正的神奇体验。

优秀的 Agent 至少不会遵循[“给你提示词，给你一堆工具，循环直到达成目标”][https://www.anthropic.com/engineering/building-effective-agents#agents] 的模式。相反，它们主要由软件逻辑构成。 

因此，我着手回答以下问题：

> ### **我们应遵循哪些原则来构建足够可靠、可交付给生产环境客户的 LLM 驱动软件？**

欢迎来到 12-Factor Agent。正如自戴利以来历任芝加哥市长都在城市主要机场反复宣传的那样：很高兴你来到这里。

*特别感谢 [@iantbutler01](https://github.com/iantbutler01)、[@tnm](https://github.com/tnm)、[@hellovai](https://www.github.com/hellovai)、[@stantonk](https://www.istantonk)、[@balanceiskey](https://www.balanceiskey)、[@AdjectiveAllison](https://www.AdjectiveAllison)、[@pfbyjy](https://www.pfbyjy)、[@a-churchill](https://www.a-churchill)，以及旧金山 MLOps 社区为本指南提供的早期反馈。*

## 精简版：十二要素

即使 LLM [持续以指数级变得更强大][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md#what-if-llms-get-smarter]，仍有一些核心工程技巧能让 LLM 驱动的软件更可靠、更易扩展且更易于维护。

- [我们如何走到这一步：软件简史][https://github.com/humanlayer/12-factor-agents/blob/main/content/brief-history-of-software.md]
- [要素 1：自然语言到工具调用][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-01-natural-language-to-tool-calls.md]
- [要素 2：掌控你的提示词（Prompts）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md]
- [要素 3：掌控你的上下文窗口（Context Window）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md]
- [要素 4：工具即结构化输出][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-04-tools-are-structured-outputs.md]
- [要素 5：统一执行状态与业务状态][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md]
- [要素 6：通过简单 API 实现启动/暂停/恢复][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md]
- [要素 7：通过工具调用联系人类（人工介入）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md]
- [要素 8：掌控你的控制流（Control Flow）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md]
- [要素 9：将错误信息紧凑化至上下文窗口][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-09-compact-errors.md]
- [要素 10：小型、专注的 Agent][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md]
- [要素 11：随处触发，在用户所在处提供服务][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md]
- [要素 12：让你的 Agent 成为无状态归约器（Stateless Reducer）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-12-stateless-reducer.md]

### 可视化导航

|    |    |    |
|----|----|-----|
|[![factor 1](https://github.com/humanlayer/12-factor-agents/blob/main/img/110-natural-language-tool-calls.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-01-natural-language-to-tool-calls.md) | [![factor 2](https://github.com/humanlayer/12-factor-agents/blob/main/img/120-own-your-prompts.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md) | [![factor 3](https://github.com/humanlayer/12-factor-agents/blob/main/img/130-own-your-context-building.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md) |
|[![factor 4](https://github.com/humanlayer/12-factor-agents/blob/main/img/140-tools-are-just-structured-outputs.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-04-tools-are-structured-outputs.md) | [![factor 5](https://github.com/humanlayer/12-factor-agents/blob/main/img/150-unify-state.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md) | [![factor 6](https://github.com/humanlayer/12-factor-agents/blob/main/img/160-pause-resume-with-simple-apis.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md) |
| [![factor 7](https://github.com/humanlayer/12-factor-agents/blob/main/img/170-contact-humans-with-tools.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md) | [![factor 8](https://github.com/humanlayer/12-factor-agents/blob/main/img/180-control-flow.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md) | [![factor 9](https://github.com/humanlayer/12-factor-agents/blob/main/img/190-factor-9-errors-static.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-09-compact-errors.md) |
| [![factor 10](https://github.com/humanlayer/12-factor-agents/blob/main/img/1a0-small-focused-agents.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md) | [![factor 11](https://github.com/humanlayer/12-factor-agents/blob/main/img/1b0-trigger-from-anywhere.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md) | [![factor 12](https://github.com/humanlayer/12-factor-agents/blob/main/img/1c0-stateless-reducer.png)](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-12-stateless-reducer.md) |

## 我们如何走到这一步

若想深入了解我的 Agent 探索历程及本文的由来，请查阅《[软件简史][https://github.com/humanlayer/12-factor-agents/blob/main/content/brief-history-of-software.md]》。此处为简要总结：

### Agent 的承诺

我们将频繁提到有向图（Directed Graphs, DG）及其无环好友 DAG。我首先要指出的是……好吧……软件本质上就是一个有向图。我们过去习惯用流程图来表示程序，自有其道理。

![010-software-dag](https://github.com/humanlayer/12-factor-agents/blob/main/img/010-software-dag.png)

### 从代码到 DAGs

大约 20 年前，DAG 编排器开始流行。我们谈论的是经典之作如 [Airflow][https://airflow.apache.org/]、[Prefect][https://www.prefect.io/]，以及一些先驱和较新的工具如 ([dagster][https://dagster.io/], [ingest][https://www.inngest.com/], [windmill][https://www.windmill.dev/])。它们遵循相同的图模式，并额外提供了可观测性、模块化、重试机制和管理功能等优势。

![015-dag-orchestrators](https://github.com/humanlayer/12-factor-agents/blob/main/img/015-dag-orchestrators.png)

### Agent 的愿景

我不是第一个[说出这话的人][https://youtu.be/Dc99-zTMyMg?si=bcT0hIwWij2mR-40&t=73]，但当我开始学习 Agent 时，最大的收获是：你可以扔掉那个固定的 DAG。与其让软件工程师编写每一个步骤和边界情况，不如给 Agent 一个目标以及一组状态转换规则：

![025-agent-dag](https://github.com/humanlayer/12-factor-agents/blob/main/img/025-agent-dag.png)

然后让 LLM 实时做出决策来探索路径。

![026-agent-dag-lines](https://github.com/humanlayer/12-factor-agents/blob/main/img/026-agent-dag-lines.png)

这里的愿景是：你只需编写更少的软件，将图的“边”交给 LLM，让它自行推导节点。你可以从错误中恢复，减少代码量，甚至可能发现 LLM 能找出解决问题的新颖方案。


### Agent 作为循环

正如我们稍后所见，事实证明这并不完全奏效。

让我们深入一步——使用 Agent 时，你会遇到这样一个由以下步骤组成的循环：

1. LLM 确定工作流的下一步，输出结构化 JSON（即“工具调用”）
2. 确定性代码执行该工具调用
3. 结果被追加到上下文窗口中 
4. 重复上述过程，直到下一步判定为“完成”

```python
initial_event = {"message": "..."}
context = [initial_event]
while True:
  next_step = await llm.determine_next_step(context)
  context.append(next_step)

  if (next_step.intent === "done"):
    return next_step.final_answer

  result = await execute_step(next_step)
  context.append(result)
```

我们的初始上下文只是一个起始事件（可能是用户消息、定时任务触发或 Webhook 等），我们让 LLM 选择下一步（工具）或判定已完成。

以下是一个多步骤示例：

[![027-agent-loop-animation](https://github.com/humanlayer/12-factor-agents/blob/main/img/027-agent-loop-animation.gif)](https://github.com/user-attachments/assets/3beb0966-fdb1-4c12-a47f-ed4e8240f8fd)

<details>
<summary><a href="https://github.com/humanlayer/12-factor-agents/blob/main/img/027-agent-loop-animation.gif">GIF 版本</a></summary>

![027-agent-loop-animation](https://github.com/humanlayer/12-factor-agents/blob/main/img/027-agent-loop-animation.gif)

</details>

## 为什么是 12-Factor Agent？

归根结底，这种方法的效果并未达到我们的预期。

在构建 HumanLayer 的过程中，我至少与 100 位 SaaS 开发者（多为技术创始人）交流过，他们希望让自己的现有产品更具 Agent 特性。通常的演进路径如下：

1. 决定要构建一个 Agent
2. 进行产品设计、UX 映射、明确要解决的问题
3. 为了快速推进，直接引入某个 $FRAMEWORK *开始搭建*
4. 达到 70-80% 的质量基准 
5. 意识到对于大多数面向客户的功能而言，80% 并不够好
6. 发现跨越 80% 的瓶颈需要逆向工程框架、提示词、流程等
7. 从零开始重来

<details>
<summary>随机免责声明</summary>

**声明**：我不确定放在哪里最合适，但这里似乎可以：**这绝非为了贬低市面上众多的框架，或是那些极其聪明的框架开发者**。它们催生了令人惊叹的成果，并加速了 AI 生态的发展。 

我希望本文的一个成果是，Agent 框架的构建者能从我和其他人的经历中吸取经验，打造出更优秀的框架。

尤其是对于那些希望快速推进但需要深度控制权的产品构建者而言。

**声明 2**：我不会在这里讨论 MCP。我相信你能看出它的位置。

**声明 3**：我主要使用 TypeScript，[出于某些原因][https://www.linkedin.com/posts/dexterihorthy_llms-typescript-aiagents-activity-7290858296679313408-Lh9e?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA4oHTkByAiD-wZjnGsMBUL_JT6nyyhOh30]，但这套方法论在 Python 或你偏好的任何其他语言中同样适用。 


好了，言归正传...

</details>

### 优秀 LLM 应用的设计模式

在翻阅了数百个 AI 库并与数十位创始人合作后，我的直觉是：

1. 存在一些核心要素能让 Agent 变得出色
2. 盲目押注某个框架并构建本质上属于全新重写（greenfield rewrite）的项目可能适得其反
3. 确实存在一些让 Agent 出色的核心原则，如果你引入一个框架，你很可能已经获取了其中大部分/全部
4. **但是**，我发现开发者将高质量 AI 软件交付给客户的最快路径是：提取 Agent 构建中的小型、模块化概念，并将其融入他们现有的产品中
5. 即使没有 AI 背景，大多数熟练的软件工程师也能定义和应用这些来自 Agent 的模块化概念

> #### 我发现开发者将优秀 AI 软件交付给客户的最快路径是：提取 Agent 构建中的小型、模块化概念，并融入他们现有的产品


## 十二要素（再次列出）


- [我们如何走到这一步：软件简史][https://github.com/humanlayer/12-factor-agents/blob/main/content/brief-history-of-software.md]
- [要素 1：自然语言到工具调用][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-01-natural-language-to-tool-calls.md]
- [要素 2：掌控你的提示词（Prompts）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md]
- [要素 3：掌控你的上下文窗口（Context Window）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md]
- [要素 4：工具即结构化输出][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-04-tools-are-structured-outputs.md]
- [要素 5：统一执行状态与业务状态][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md]
- [要素 6：通过简单 API 实现启动/暂停/恢复][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md]
- [要素 7：通过工具调用联系人类（人工介入）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md]
- [要素 8：掌控你的控制流（Control Flow）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md]
- [要素 9：将错误信息紧凑化至上下文窗口][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-09-compact-errors.md]
- [要素 10：小型、专注的 Agent][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md]
- [要素 11：随处触发，在用户所在处提供服务][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md]
- [要素 12：让你的 Agent 成为无状态归约器（Stateless Reducer）][https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-12-stateless-reducer.md]

## 荣誉提名 / 其他建议

- [要素 13：预取所有可能需要的上下文][https://github.com/humanlayer/12-factor-agents/blob/main/content/appendix-13-pre-fetch.md]

## 相关资源

- 在此为本指南做出贡献 [here](https://github.com/humanlayer/12-factor-agents)
- 我在 2025 年 3 月的《Tool Use》播客节目中详细讨论了其中的许多内容 [I talked about a lot of this on an episode of the Tool Use podcast][https://youtu.be/8bIHcttkOTE]
- 我会在 [The Outer Loop][https://theouterloop.substack.com] 上撰写一些相关内容
- 我与 [@hellovai][https://github.com/hellovai] 一起举办关于[最大化 LLM 性能的网络研讨会][https://github.com/hellovai/ai-that-works/tree/main]
- 我们使用此方法论在 [got-agents/agents][https://github.com/got-agents/agents] 下构建开源 Agent
- 我们无视了自己的所有建议，并构建了一个[用于在 Kubernetes 中运行分布式 Agent 的框架][https://github.com/humanlayer/kubechain]
- 本指南的其他链接：
  - [12 Factor Apps][https://12factor.net]
  - [Building Effective Agents (Anthropic)][https://www.anthropic.com/engineering/building-effective-agents#agents]
  - [Prompts are Functions][https://thedataexchange.media/baml-revolution-in-ai-engineering/ ]
  - [Library patterns: Why frameworks are evil][https://tomasp.net/blog/2015/library-frameworks/]
  - [The Wrong Abstraction][https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction]
  - [Mailcrew Agent][https://github.com/dexhorthy/mailcrew]
  - [Mailcrew Demo Video][https://www.youtube.com/watch?v=f_cKnoPC_Oo]
  - [Chainlit Demo][https://x.com/chainlit_io/status/1858613325921480922]
  - [TypeScript for LLMs][https://www.linkedin.com/posts/dexterihorthy_llms-typescript-aiagents-activity-7290858296679313408-Lh9e]
  - [Schema Aligned Parsing][https://www.boundaryml.com/blog/schema-aligned-parsing]
  - [Function Calling vs Structured Outputs vs JSON Mode][https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode]
  - [BAML on GitHub][https://github.com/boundaryml/baml]
  - [OpenAI JSON vs Function Calling][https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/]
  - [Outer Loop Agents][https://theouterloop.substack.com/p/openais-realtime-api-is-a-step-towards]
  - [Airflow][https://airflow.apache.org/]
  - [Prefect][https://www.prefect.io/]
  - [Dagster][https://dagster.io/]
  - [Inngest][https://www.inngest.com/]
  - [Windmill][https://www.windmill.dev/]
  - [The AI Agent Index (MIT)][https://aiagentindex.mit.edu/]
  - [NotebookLM on Finding Model Capability Boundaries][https://open.substack.com/pub/swyx/p/notebooklm?selection=08e1187c-cfee-4c63-93c9-71216640a5f8]

## 贡献者

感谢所有为 12-Factor Agent 做出贡献的人！

[<img src="https://avatars.githubusercontent.com/u/3730605?v=4&s=80" width="80px" alt="dexhorthy" />](https://github.com/dexhorthy) [<img src="https://avatars.githubusercontent.com/u/50557586?v=4&s=80" width="80px" alt="Sypherd" />](https://github.com/Sypherd) [<img src="https://avatars.githubusercontent.com/u/66259401?v=4&s=80" width="80px" alt="tofaramususa" />](https://github.com/tofaramususa) [<img src="https://avatars.githubusercontent.com/u/18105223?v=4&s=80" width="80px" alt="a-churchill" />](https://github.com/a-churchill) [<img src="https://avatars.githubusercontent.com/u/4084885?v=4&s=80" width="80px" alt="Elijas" />](https://github.com/Elijas) [<img src="https://avatars.githubusercontent.com/u/39267118?v=4&s=80" width="80px" alt="hugolmn" />](https://github.com/hugolmn) [<img src="https://avatars.githubusercontent.com/u/1882972?v=4&s=80" width="80px" alt="jeremypeters" />](https://github.com/jeremypeters)

[<img src="https://avatars.githubusercontent.com/u/380402?v=4&s=80" width="80px" alt="kndl" />](https://github.com/kndl) [<img src="https://avatars.githubusercontent.com/u/16674643?v=4&s=80" width="80px" alt="maciejkos" />](https://github.com/maciejkos) [<img src="https://avatars.githubusercontent.com/u/85041180?v=4&s=80" width="80px" alt="pfbyjy" />](https://github.com/pfbyjy) [<img src="https://avatars.githubusercontent.com/u/36044389?v=4&s=80" width="80px" alt="0xRaduan" />](https://github.com/0xRaduan) [<img src="https://avatars.githubusercontent.com/u/7169731?v=4&s=80" width="80px" alt="zyuanlim" />](https://github.com/zyuanlim) [<img src="https://avatars.githubusercontent.com/u/15862501?v=4&s=80" width="80px" alt="lombardo-chcg" />](https://github.com/lombardo-chcg) [<img src="https://avatars.githubusercontent.com/u/160066852?v=4&s=80" width="80px" alt="sahanatvessel" />](https://github.com/sahanatvessel)
 
## 许可证

所有内容与图片均采用 <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0 License</a> 许可。

代码采用 <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a> 授权。