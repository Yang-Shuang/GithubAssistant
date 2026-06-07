<div align="center">

![Hindsight Banner](./hindsight-docs/static/img/hindsight-github-banner.png)

[文档](https://hindsight.vectorize.io) • [论文](https://arxiv.org/abs/2512.12818) • [示例教程](https://hindsight.vectorize.io/cookbook) • [Hindsight Cloud](https://ui.hindsight.vectorize.io/signup)

[![CI](https://github.com/vectorize-io/hindsight/actions/workflows/release.yml/badge.svg)](https://github.com/vectorize-io/hindsight/actions/workflows/release.yml)
[![Slack Community](https://img.shields.io/badge/Slack-Join%20Community-4A154B?logo=slack)](https://join.slack.com/t/hindsight-space/shared_invite/zt-3nhbm4w29-LeSJ5Ixi6j8PdiYOCPlOgg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![gitcgr](https://gitcgr.com/badge/vectorize-io/hindsight.svg)](https://gitcgr.com/vectorize-io/hindsight)
![PyPI - Downloads](https://img.shields.io/pypi/dm/hindsight-api?label=PyPI)
![NPM Downloads](https://img.shields.io/npm/dm/%40vectorize-io%2Fhindsight-client?logoColor=orange&label=NPM&color=blue&link=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40vectorize-io%2Fhindsight-client)
<br/>

<a href="https://trendshift.io/repositories/15603" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15603" alt="vectorize-io%2Fhindsight | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

---

## 什么是 Hindsight？

Hindsight™ 是一个智能体记忆系统，旨在构建能够随时间推移不断学习的更智能的智能体。大多数智能体记忆系统侧重于回忆对话历史，而 Hindsight 专注于让智能体真正学习，而不仅仅是记住信息。


<video src="https://github.com/user-attachments/assets/923b798d-3581-4897-bb62-9cfa5a931682" controls></video>

它克服了 RAG（检索增强生成）和知识图谱等替代技术的局限性，并在长期记忆任务中实现了业界领先的性能。

## 记忆性能与准确性

根据基准测试表现，Hindsight 是目前测试过的最准确的智能体记忆系统。它在广泛用于评估各类对话式 AI 场景下记忆系统性能的 LongMemEval 基准测试中取得了业界领先的成绩。截至 2026 年 1 月，Hindsight 及其他智能体记忆解决方案的当前报告性能如下所示：

![Overview](./hindsight-docs/static/img/hindsight-benchmarks.png)

Hindsight 的基准测试数据已由弗吉尼亚理工大学桑格尼人工智能与数据分析中心（Sanghani Center for Artificial Intelligence and Data Analytics）及《华盛顿邮报》的研究合作者独立复现。其他分数由软件供应商自行报告。

Hindsight 已在多家财富 500 强企业投入生产环境使用，并被越来越多的 AI 初创公司采用。 

## 将 Hindsight 集成到你的 AI 智能体中

与现有智能体配合使用 Hindsight 的最简单方式是使用 LLM Wrapper（大语言模型封装器）。你只需两行代码即可为智能体添加记忆功能。这会将你当前的 LLM 客户端替换为 Hindsight 封装器，此后在进行 LLM 调用时，记忆将自动存储和检索。

如果你需要更精细地控制智能体存储和检索记忆的时机与方式，也可以通过 SDK 或直接向 HTTP 接口发送请求来集成一个简单的 API。

![Hindsight Banner](./hindsight-docs/static/img/migration-code.png)

---

> 🤖 **正在使用编码智能体？** 安装 Hindsight 文档技能，以便在编写代码时即时访问文档：
> ```bash
> npx skills add https://github.com/vectorize-io/hindsight --skill hindsight-docs
> ```
> 兼容 Claude Code、Cursor 及其他 AI 编程助手。

---


## 快速开始

### Docker（推荐）

```bash
export OPENAI_API_KEY=sk-xxx

docker run -it --pull always --name hindsight --restart unless-stopped -p 8888:8888 -p 9999:9999 \
  -e HINDSIGHT_API_LLM_API_KEY=$OPENAI_API_KEY \
  -v $HOME/.hindsight-docker:/home/hindsight/.pg0 \
  ghcr.io/vectorize-io/hindsight:latest
```

>API: http://localhost:8888
>UI: http://localhost:9999

你可以通过设置环境变量 `HINDSIGHT_API_LLM_PROVIDER` 来修改大语言模型提供商。支持的有效选项包括 `openai`、`anthropic`、`gemini`、`groq`、`ollama`、`lmstudio` 和 `minimax`。有关支持的模型，请参阅文档中的[详细列表](https://hindsight.vectorize.io/developer/models)。



### Docker（外部 PostgreSQL）

```bash
export OPENAI_API_KEY=sk-xxx
export HINDSIGHT_DB_PASSWORD=choose-a-password
cd docker/docker-compose
docker compose up 
```

> Oracle AI Database 也支持企业级部署，且功能完全对等。详情请参阅[存储文档](https://hindsight.vectorize.io/developer/storage)。


>API: http://localhost:8888
>UI: http://localhost:9999

### Client（客户端）

```bash
pip install hindsight-client -U
# or
npm install @vectorize-io/hindsight-client
```

#### Python

```python
from hindsight_client import Hindsight

client = Hindsight(base_url="http://localhost:8888")

# Retain: Store information
client.retain(bank_id="my-bank", content="Alice works at Google as a software engineer")

# Recall: Search memories
client.recall(bank_id="my-bank", query="What does Alice do?")

# Reflect: Generate disposition-aware response
client.reflect(bank_id="my-bank", query="Tell me about Alice")
```

#### Node.js / TypeScript

```bash
npm install @vectorize-io/hindsight-client
```

```javascript
const { HindsightClient } = require('@vectorize-io/hindsight-client');

const main = async () => {
  const client = new HindsightClient({ baseUrl: 'http://localhost:8888' });

  await client.retain('my-bank', 'Alice loves hiking in Yosemite');

  const results = await client.recall('my-bank', 'What does Alice like?');
  console.log(results);
}

main();
```


### Python Embedded（无需服务器）

```bash
pip install hindsight-all -U
```

```python
import os
from hindsight import HindsightServer, HindsightClient

with HindsightServer(
    llm_provider="openai",
    llm_model="gpt-5-mini", 
    llm_api_key=os.environ["OPENAI_API_KEY"]
) as server:
    client = HindsightClient(base_url=server.url)
    client.retain(bank_id="my-bank", content="Alice works at Google")
    results = client.recall(bank_id="my-bank", query="Where does Alice work?")
```


---

## 应用场景


Hindsight 专为支持对话式 AI 智能体以及旨在自主执行任务的智能体而构建。Hindsight 的理想应用场景是那些需要结合这些功能的智能体，例如“AI 员工”：它们需要处理开放式任务、根据用户反馈调整行为，并学习执行复杂任务以实现自动化工作，其水平可媲美人类。Hindsight 也可用于使用 n8n 及其他类似工具构建的简单 AI 工作流，但对于此类应用来说可能略显冗余。

### 用户级记忆与聊天历史

你可以使用 Hindsight 实现的一个较简单用例是：通过存储和检索与特定用户相关的记忆，为 AI 聊天机器人及其他对话式智能体提供个性化服务。

该用例的需求通常如下所示：

![Per-User Memories](./hindsight-docs/static/img/per-user-memory-requirements.png)

<video src="https://github.com/user-attachments/assets/4805e8e1-e7d1-47c6-a4f8-2344a5ec8906" controls></video>

在 Hindsight 中满足这些需求非常直接。当通过 `retain`（存储）操作将新的用户输入和工具调用摄入系统时，可以使用自定义元数据（metadata）来丰富新记忆。元数据提供了一种便捷的方式，用于隔离那些需要限制在特定用户范围内的记忆。将这些输入 `retain` 操作后，在检索相关记忆时，可以对生成的原始记忆和心智模型进行过滤。 

![Per-User Memories](./hindsight-docs/static/img/per-user-memory-howto.png)

---

## 架构与运行机制

![Overview](./hindsight-docs/static/img/hindsight-overview.webp)

大多数智能体记忆实现依赖于基础的向量搜索（vector search），有时也会使用知识图谱。Hindsight 采用仿生数据结构来组织智能体记忆，其运作方式更贴近人类记忆机制：

- **World（世界）：** 关于客观世界的事实（例如“炉子会烫”）
- **Experiences（经历）：** 智能体自身的经历（例如“我碰了炉子，真的很疼”）
- **Mental Models（心智模型）：** 通过对原始记忆和经历进行反思而形成的对智能体所处世界的认知理解。

Hindsight 中的记忆存储在库（即 memory banks / 记忆库）中。当记忆被添加到 Hindsight 时，它们会被推入世界事实或经历记忆路径。随后，它们将被表示为实体、关系和时间序列的组合，并采用稀疏/稠密向量表示法，以辅助后续的检索。

Hindsight 提供三种简单的方法与系统交互：

- **Retain（存储）：** 向 Hindsight 提供你希望它记住的信息
- **Recall（检索）：** 从 Hindsight 中检索记忆
- **Reflect（反思）：** 对记忆和经历进行反思，从而基于现有记忆生成新的观察结果与见解。

### Retain（存储）

`retain` 操作用于将新记忆推入 Hindsight。它指示系统 _保留_ 你作为输入传递的信息。

```python
from hindsight_client import Hindsight

client = Hindsight(base_url="http://localhost:8888")

# Simple
client.retain(
    bank_id="my-bank",
    content="Alice works at Google as a software engineer"
)

# With context and timestamp
client.retain(
    bank_id="my-bank",
    content="Alice got promoted to senior engineer",
    context="career update",
    timestamp="2025-06-15T10:00:00Z"
)
```

在底层，`retain` 操作会使用大语言模型提取关键事实、时间数据、实体和关系。随后通过标准化流程，将提取的数据转换为规范化的实体、时间序列、搜索索引以及元数据。这些表示方式为 `recall`（检索）和 `reflect`（反思）操作中的准确记忆检索创建了路径。 

![Retain Operation](hindsight-docs/static/img/retain-operation.webp)

### Recall（检索）

`recall` 操作用于检索记忆。这些记忆可以来自任意类型的记忆库（世界、经历等）。

```python
from hindsight_client import Hindsight

client = Hindsight(base_url="http://localhost:8888")

# Simple
client.recall(bank_id="my-bank", query="What does Alice do?")

# Temporal
client.recall(bank_id="my-bank", query="What happened in June?")
```

`recall` 并行执行四种检索策略：
- **Semantic（语义）：** 向量相似度匹配
- **Keyword（关键词）：** BM25 精确匹配
- **Graph（图谱）：** 实体/时间/因果链接
- **Temporal（时间）：** 时间范围过滤

![Retain Operation](hindsight-docs/static/img/recall-operation.webp)

检索得到的独立结果会被合并，然后使用互反排名融合（reciprocal rank fusion）和交叉编码器重排序模型（cross-encoder reranking model）按相关性进行排序。

最终输出会根据需要进行裁剪，以符合令牌（token）限制。

### Reflect（反思）

`reflect` 操作用于对现有记忆进行更深入的分析。这使得智能体能够建立记忆之间的新关联，并构建对其所处世界的更透彻理解。

例如，`reflect` 操作可用于支持以下用例：

- **AI 项目经理**反思项目中需要缓解哪些风险。
- **销售智能体**反思为何某些外联消息获得了回复，而另一些没有。
- **客服智能体**反思客户提出但未被当前产品文档解答的问题机会点。

`reflect` 操作也可用于处理需要深度思考的按需问答或分析任务。

```python
from hindsight_client import Hindsight

client = Hindsight(base_url="http://localhost:8888")

client.reflect(bank_id="my-bank", query="What should I know about Alice?")
```

![Retain Operation](hindsight-docs/static/img/reflect-operation.webp)

---

## 资源

**文档：** 
- [https://hindsight.vectorize.io](https://hindsight.vectorize.io)

**客户端 SDK/API：**
- [Python](http://hindsight.vectorize.io/sdks/python)
- [Node.js](http://hindsight.vectorize.io/sdks/nodejs)
- [REST API](https://hindsight.vectorize.io/api-reference)
- [CLI](https://hindsight.vectorize.io/sdks/cli)

**社区与支持：**
- [Slack](https://join.slack.com/t/hindsight-space/shared_invite/zt-3nhbm4w29-LeSJ5Ixi6j8PdiYOCPlOgg)
- [GitHub Issues](https://github.com/vectorize-io/hindsight/issues)

---
## Star 历史趋势

[![Star History Chart](https://api.star-history.com/svg?repos=vectorize-io/hindsight&type=date&legend=top-left)](https://www.star-history.com/#vectorize-io/hindsight&type=date&legend=top-left)
---

## 贡献指南

请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 开源协议

MIT — 详见 [LICENSE](./LICENSE)

---

由 [Vectorize.io](https://vectorize.io) 构建

<img src="https://umami-pixel.chris-latimer.workers.dev/?id=a8b043e6-6964-454d-80df-69b69d3f0d50&host=github.com&url=/vectorize-io/hindsight" width="1" height="1" alt="" />