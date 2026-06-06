<p align="center">
  <a href="https://github.com/mem0ai/mem0">
    <img src="docs/images/banner-sm.png" width="800px" alt="Mem0 - 个性化 AI 的记忆层">
  </a>
</p>
<p align="center" style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <a href="https://trendshift.io/repositories/11194" target="blank">
    <img src="https://trendshift.io/api/badge/repositories/11194" alt="mem0ai%2Fmem0 | Trendshift" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <a href="https://mem0.ai">了解更多</a>
  ·
  <a href="https://mem0.dev/DiG">加入 Discord</a>
  ·
  <a href="https://mem0.dev/demo">在线演示</a>
</p>

<p align="center">
  <a href="https://mem0.dev/DiG">
    <img src="https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white" alt="Mem0 Discord">
  </a>
  <a href="https://pepy.tech/project/mem0ai">
    <img src="https://img.shields.io/pypi/dm/mem0ai" alt="Mem0 PyPI - Downloads">
  </a>
  <a href="https://github.com/mem0ai/mem0">
    <img src="https://img.shields.io/github/commit-activity/m/mem0ai/mem0?style=flat-square" alt="GitHub commit activity">
  </a>
  <a href="https://pypi.org/project/mem0ai" target="blank">
    <img src="https://img.shields.io/pypi/v/mem0ai?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://www.npmjs.com/package/mem0ai" target="blank">
    <img src="https://img.shields.io/npm/v/mem0ai" alt="Npm package">
  </a>
  <a href="https://www.ycombinator.com/companies/mem0">
    <img src="https://img.shields.io/badge/Y%20Combinator-S24-orange?style=flat-square" alt="Y Combinator S24">
  </a>
</p>

<p align="center">
  <a href="https://mem0.ai/research"><strong>📄 Benchmarking Mem0's token-efficient memory algorithm →</strong></a>
</p>

## 全新记忆算法（2026年4月）

| Benchmark | Old | New  | Tokens  | Latency p50  |
| --- | --- | --- | --- | --- |
| **LoCoMo** | 71.4 | **91.6** | 7.0K  | 0.88s  |
| **LongMemEval** | 67.8 | **94.8** | 6.8K  | 1.09s  |
| **BEAM (1M)** | — | **64.1** | 6.7K  | 1.00s  |
| **BEAM (10M)** | — | **48.6** | 6.9K  | 1.05s  |

所有基准测试均在相同的生产级模型栈上运行。采用单次检索（一次调用，无智能体循环）。

**主要变更：**
- **仅支持新增的单次提取** —— 仅需一次 LLM 调用，无需 UPDATE/DELETE。记忆持续累积，不会覆盖旧内容。
- **Agent（智能体）生成的事实享有同等优先级** —— 当智能体确认某项操作时，该信息现在会以相同权重进行存储。
- **实体链接** —— 提取、嵌入并跨记忆关联实体，以提升检索效果。
- **多信号检索** —— 语义、BM25 关键词和实体匹配并行打分并融合结果。
- **时间推理** —— 具备时间感知能力的检索，可根据查询内容（当前状态、过去事件或未来计划）精准排序对应时间点的数据实例。

升级说明请参阅 [迁移指南](https://docs.mem0.ai/migration/oss-v2-to-v3)。[评估框架](https://github.com/mem0ai/memory-benchmarks) 已开源，任何人都可复现上述数据。

## 研究亮点
- **LoCoMo 得分 91.6** —— 较旧算法提升 20 分
- **LongMemEval 得分 94.8** —— 提升 27 分，助手记忆召回率提升 53.6%
- **BEAM (1M) 得分 64.1** —— 在百万 Token 规模下实现生产级记忆评估
- [阅读完整论文](https://mem0.ai/research)

# 简介

[Mem0](https://mem0.ai)（"mem-zero"）为 AI 助手和智能体提供了一层智能化的记忆层（Memory Layer），从而实现个性化的 AI 交互体验。它能记住用户偏好、适应个体需求并持续学习——非常适合客服聊天机器人、AI 助手及自主系统。

### 核心功能与应用场景

**核心能力：**
- **多级记忆**：无缝保留用户、会话和智能体状态，并提供自适应个性化服务
- **开发者友好**：直观的 API、跨平台 SDK 以及全托管云服务选项

**应用场景：**
- **AI 助手**：保持上下文连贯的丰富对话体验
- **客服支持**：回顾历史工单与用户记录，提供定制化帮助
- **医疗健康**：追踪患者偏好与病史，实现个性化护理
- **生产力工具与游戏**：基于用户行为自适应调整工作流与环境

## 🚀 快速入门 <a name="quickstart"></a>

### 以智能体身份注册

AI 智能体可在五秒内生成可用的 Mem0 API Key —— 无需邮箱、无需控制面板、无需短信验证码。全程仅需四条命令：

```bash
# 1. Install
npm install -g @mem0/cli      # or: pip install mem0-cli

# 2. Sign up as an agent (replace `claude-code` with your name)
mem0 init --agent --agent-caller claude-code

# 3. Add a memory
mem0 add "I am using mem0"

# 4. Search
mem0 search "am I using mem0"
```

人类用户稍后可通过 `mem0 init --email <邮箱地址>` 认领该账户 —— 使用相同的 Key，记忆数据完整保留。完整指南：[以智能体身份注册](https://docs.mem0.ai/platform/agent-signup)。

| | Library | Self-Hosted Server | Cloud Platform |
|---|---------|-------------------|----------------|
| **适用场景** | 测试、原型开发 | 团队自建基础设施 | 零运维生产环境 |
| **安装方式** | `pip install mem0ai` | `docker compose up` | 前往 [app.mem0.ai](https://app.mem0.ai?utm_source=oss&utm_medium=readme) 注册 |
| **控制面板** | -- | [支持](https://docs.mem0.ai/open-source/setup) | 支持 |
| **认证与 API Key** | -- | 支持 | 支持 |
| **高级功能** | -- | 预览版 | 全部包含 |

仅做测试？使用本地库。为团队构建？选择自托管服务。希望零运维？直接使用云平台。

### 本地库（pip / npm）

```bash
pip install mem0ai
```

如需增强混合搜索功能（支持 BM25 关键词匹配与实体提取），请安装带 NLP 支持的版本：

```bash
pip install mem0ai[nlp]
python -m spacy download en_core_web_sm
```

通过 npm 安装 SDK：

```bash
npm install mem0ai
```

### 自托管服务

> **注意**：自托管版本默认开启认证。若从旧版（无认证）升级？请设置 `ADMIN_API_KEY`，通过向导注册管理员账号，或仅在本地开发时配置 `AUTH_DISABLED=true`。详见 [升级说明](https://docs.mem0.ai/open-source/setup#upgrade-notes)。

```bash
# Recommended: one command — start the stack, create an admin, issue the first API key.
cd server && make bootstrap

# Manual: start the stack and finish setup via the browser wizard.
cd server && docker compose up -d    # http://localhost:3000
```

详细配置请参阅 [自托管文档](https://docs.mem0.ai/open-source/overview)。

### 云平台

1. 在 [Mem0 平台](https://app.mem0.ai?utm_source=oss&utm_medium=readme) 注册账号
2. 通过 SDK 或 API Key 集成记忆层
3. 正在使用托管的 Qdrant 向量？请参阅 [平台迁移指南](https://docs.mem0.ai/migration/oss-to-platform) 将其导入 Mem0 平台。

### 命令行工具（CLI）

在终端中管理记忆数据：

```bash
npm install -g @mem0/cli   # or: pip install mem0-cli

mem0 init
mem0 add "Prefers dark mode and vim keybindings" --user-id alice
mem0 search "What does Alice prefer?" --user-id alice
```

完整命令参考请参阅 [CLI 文档](https://docs.mem0.ai/platform/cli)。

### 智能体技能（Agent Skills）

教你的 AI 编程助手（Claude Code、Codex、Cursor、Windsurf、OpenCode、OpenClaw，以及任何支持技能标准的工具）如何使用 Mem0 进行开发。分为两类：

**参考类技能 —— 始终启用**（将 SDK 知识加载至助手上下文）：

```bash
npx skills add https://github.com/mem0ai/mem0 --skill mem0
npx skills add https://github.com/mem0ai/mem0 --skill mem0-cli
npx skills add https://github.com/mem0ai/mem0 --skill mem0-vercel-ai-sdk
```

**流水线类技能 —— 按需运行**（在现有仓库中执行端到端工作流）：

```bash
npx skills add https://github.com/mem0ai/mem0 --skill mem0-integrate
npx skills add https://github.com/mem0ai/mem0 --skill mem0-test-integration
```

使用 `/mem0-integrate` 通过测试优先流水线将 Mem0 接入现有仓库，随后运行 `/mem0-test-integration` 进行验证。完整说明请参阅 [技能目录](./skills/) 或 [Mem0 辅助编程指南](https://docs.mem0.ai/vibecoding)。

### 基础用法

Mem0 需要依赖大语言模型（LLM）运行，默认使用 OpenAI 的 `gpt-5-mini`。同时它支持多种 LLM；详情请参阅我们的 [支持的 LLM 文档](https://docs.mem0.ai/components/llms/overview)。

Mem0 默认使用 OpenAI 的 `text-embedding-3-small` 作为嵌入模型（Embedding Model）。为获得最佳混合搜索效果（语义 + 关键词 + 实体加权），建议至少使用 [Qwen 600M](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct) 或同等水平的嵌入模型。配置详情请参阅 [支持的嵌入模型](https://docs.mem0.ai/components/embedders/overview)。

第一步是初始化记忆实例：

```python
from openai import OpenAI
from mem0 import Memory

openai_client = OpenAI()
memory = Memory()

def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    # Retrieve relevant memories
    relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])

    # Generate Assistant response
    system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
    response = openai_client.chat.completions.create(model="gpt-5-mini", messages=messages)
    assistant_response = response.choices[0].message.content

    # Create new memories from the conversation
    messages.append({"role": "assistant", "content": assistant_response})
    memory.add(messages, user_id=user_id)

    return assistant_response

def main():
    print("Chat with AI (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        print(f"AI: {chat_with_memories(user_input)}")

if __name__ == "__main__":
    main()
```

详细集成步骤请参阅 [快速入门](https://docs.mem0.ai/quickstart) 和 [API 参考](https://docs.mem0.ai/api-reference)。

## 🔗 集成与演示

- **支持记忆的 ChatGPT**：由 Mem0 驱动的个性化对话（[在线演示](https://mem0.dev/demo)）
- **浏览器扩展**：在 ChatGPT、Perplexity 和 Claude 间同步记忆数据（[Chrome 插件](https://chromewebstore.google.com/detail/onihkkbipkfeijkadecaafbgagkhglop?utm_source=item-share-cb)）
- **Langgraph 支持**：使用 Langgraph + Mem0 构建客服机器人（[指南](https://docs.mem0.ai/integrations/langgraph)）
- **CrewAI 集成**：利用 Mem0 定制 CrewAI 输出结果（[示例](https://docs.mem0.ai/integrations/crewai)）

## 📚 文档与支持

- 完整文档：https://docs.mem0.ai
- 社区交流：[Discord](https://mem0.dev/DiG) · [X（原 Twitter）](https://x.com/mem0ai)
- 商务联系：founders@mem0.ai

## 引用

我们现已发表可供引用的学术论文：

```bibtex
@article{mem0,
  title={Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory},
  author={Chhikara, Prateek and Khant, Dev and Aryan, Saket and Singh, Taranjeet and Yadav, Deshraj},
  journal={arXiv preprint arXiv:2504.19413},
  year={2025}
}
```

## ⚖️ 许可证

Apache 2.0 —— 详见 [LICENSE](https://github.com/mem0ai/mem0/blob/main/LICENSE) 文件。