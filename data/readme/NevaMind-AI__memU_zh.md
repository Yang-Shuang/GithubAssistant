![MemU Banner](assets/banner.png)

<div align="center">

# memU

### 24/7 全天候主动式记忆，赋能 AI Agent

[![PyPI version](https://badge.fury.io/py/memu-py.svg)](https://badge.fury.io/py/memu-py)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Chat-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/hQZntfGsbJ)
[![Twitter](https://img.shields.io/badge/Twitter-Follow-1DA1F2?logo=x&logoColor=white)](https://x.com/memU_ai)

<a href="https://trendshift.io/repositories/17374" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17374" alt="NevaMind-AI%2FmemU | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

**[English](readme/README_en.md) | [中文](readme/README_zh.md) | [日本語](readme/README_ja.md) | [한국어](readme/README_ko.md) | [Español](readme/README_es.md) | [Français](readme/README_fr.md)**

</div>

---

memU 是一个专为 **全天候主动式 Agent** 构建的记忆框架。
它专为长期运行场景设计，大幅降低了让 Agent 保持在线的 LLM Token 消耗，使持续演进、全天候运行的 Agent 在生产环境中变得切实可行。
memU **持续捕获并理解用户意图**。即使没有发出具体指令，Agent 也能预判你的下一步操作并自主执行。

---

## 🤖 [OpenClaw Alternative](https://github.com/NevaMind-AI/memUBot)

<img width="100%" src="https://github.com/NevaMind-AI/memU/blob/main/assets/memUbot.png" />

**[memU Bot](https://github.com/NevaMind-AI/memUBot)** —— 现已开源。面向企业的 OpenClaw 替代品。一个能记住一切的主动式 AI 助手。

- **开箱即用，上手简单**（一键安装，耗时 < 3 分钟）。
- 构建长期记忆以 **理解用户意图** 并主动行动（24/7 全天候运行）。
- **大幅降低 LLM Token 消耗**（上下文体积缩减至同类方案的约 1/10）。

立即体验：[memu.bot](https://memu.bot) · 源码：[GitHub memUBot](https://github.com/NevaMind-AI/memUBot)

---

## 🗃️ 记忆即文件系统，文件系统即记忆

memU 将 **记忆视为文件系统**——结构清晰、层次分明且可即时访问。

| 文件系统 | memU 记忆系统 |
|-------------|-------------|
| 📁 Folders（文件夹） | 🏷️ Categories（自动组织的主题分类） |
| 📄 Files（文件） | 🧠 Memory Items（提取的事实、偏好与技能） |
| 🔗 Symlinks（软链接） | 🔄 Cross-references（关联记忆相互链接的交叉引用） |
| 📂 Mount points（挂载点） | 📥 Resources（对话、文档、图片等资源） |

**核心优势：**
- **像浏览目录一样导航记忆**——从宽泛分类深入至具体事实
- **即时挂载新知识**——对话和文档瞬间变为可查询的记忆
- **万物互联**——记忆之间相互引用，构建关联的知识图谱
- **持久且便携**——像管理文件一样导出、备份和转移记忆

```
memory/
├── preferences/
│   ├── communication_style.md
│   └── topic_interests.md
├── relationships/
│   ├── contacts/
│   └── interaction_history/
├── knowledge/
│   ├── domain_expertise/
│   └── learned_skills/
└── context/
    ├── recent_conversations/
    └── pending_tasks/
```

就像文件系统将原始字节转化为有序数据，memU 将原始交互转化为**结构化、可搜索的主动式智能**。

---

## ⭐️ Star 本仓库

<img width="100%" src="https://github.com/NevaMind-AI/memU/blob/main/assets/star.gif" />
如果你觉得 memU 有用或有趣，请给我们一个 GitHub Star ⭐️ 支持。

---


## ✨ Core Features（核心特性）

| Capability | Description |
|------------|-------------|
| 🤖 **24/7 Proactive Agent** | 全天候后台持续运行的主动式记忆 Agent |
| 🎯 **User Intention Capture** | 自动理解并跨会话记录用户目标、偏好与上下文 |
| 💰 **Cost Efficient** | 通过缓存洞察避免冗余 LLM 调用，大幅降低长期运行 Token 成本 |
---

## 🔄 How Proactive Memory Works（主动式记忆工作原理）

```bash

cd examples/proactive
python proactive.py

```

---

### Proactive Memory Lifecycle（主动式记忆生命周期）
```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                         USER QUERY                                               │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
                 │                                                           │
                 ▼                                                           ▼
┌────────────────────────────────────────┐         ┌────────────────────────────────────────────────┐
│         🤖 MAIN AGENT                  │         │              🧠 MEMU BOT                        │
│                                        │         │                                                │
│  Handle user queries & execute tasks   │  ◄───►  │  Monitor, memorize & proactive intelligence    │
├────────────────────────────────────────┤         ├────────────────────────────────────────────────┤
│                                        │         │                                                │
│  ┌──────────────────────────────────┐  │         │  ┌──────────────────────────────────────────┐  │
│  │  1. RECEIVE USER INPUT           │  │         │  │  1. MONITOR INPUT/OUTPUT                 │  │
│  │     Parse query, understand      │  │   ───►  │  │     Observe agent interactions           │  │
│  │     context and intent           │  │         │  │     Track conversation flow              │  │
│  └──────────────────────────────────┘  │         │  └──────────────────────────────────────────┘  │
│                 │                      │         │                    │                           │
│                 ▼                      │         │                    ▼                           │
│  ┌──────────────────────────────────┐  │         │  ┌──────────────────────────────────────────┐  │
│  │  2. PLAN & EXECUTE               │  │         │  │  2. MEMORIZE & EXTRACT                   │  │
│  │     Break down tasks             │  │   ◄───  │  │     Store insights, facts, preferences   │  │
│  │     Call tools, retrieve data    │  │  inject │  │     Extract skills & knowledge           │  │
│  │     Generate responses           │  │  memory │  │     Update user profile                  │  │
│  └──────────────────────────────────┘  │         │  └──────────────────────────────────────────┘  │
│                 │                      │         │                    │                           │
│                 ▼                      │         │                    ▼                           │
│  ┌──────────────────────────────────┐  │         │  ┌──────────────────────────────────────────┐  │
│  │  3. RESPOND TO USER              │  │         │  │  3. PREDICT USER INTENT                  │  │
│  │     Deliver answer/result        │  │   ───►  │  │     Anticipate next steps                │  │
│  │     Continue conversation        │  │         │  │     Identify upcoming needs              │  │
│  └──────────────────────────────────┘  │         │  └──────────────────────────────────────────┘  │
│                 │                      │         │                    │                           │
│                 ▼                      │         │                    ▼                           │
│  ┌──────────────────────────────────┐  │         │  ┌──────────────────────────────────────────┐  │
│  │  4. LOOP                         │  │         │  │  4. RUN PROACTIVE TASKS                  │  │
│  │     Wait for next user input     │  │   ◄───  │  │     Pre-fetch relevant context           │  │
│  │     or proactive suggestions     │  │  suggest│  │     Prepare recommendations              │  │
│  └──────────────────────────────────┘  │         │  │     Update todolist autonomously         │  │
│                                        │         │  └──────────────────────────────────────────┘  │
└────────────────────────────────────────┘         └────────────────────────────────────────────────┘
                 │                                                           │
                 └───────────────────────────┬───────────────────────────────┘
                                             ▼
                              ┌──────────────────────────────┐
                              │     CONTINUOUS SYNC LOOP     │
                              │  Agent ◄──► MemU Bot ◄──► DB │
                              └──────────────────────────────┘
```

---

## 🎯 Proactive Use Cases（主动式应用场景）

### 1. **Information Recommendation**（信息推荐）
*Agent monitors interests and proactively surfaces relevant content*
```python
# User has been researching AI topics
MemU tracks: reading history, saved articles, search queries

# When new content arrives:
Agent: "I found 3 new papers on RAG optimization that align with
        your recent research on retrieval systems. One author
        (Dr. Chen) you've cited before published yesterday."

# Proactive behaviors:
- Learns topic preferences from browsing patterns
- Tracks author/source credibility preferences
- Filters noise based on engagement history
- Times recommendations for optimal attention
```

### 2. **Email Management**（邮件管理）
*Agent learns communication patterns and handles routine correspondence*
```python
# MemU observes email patterns over time:
- Response templates for common scenarios
- Priority contacts and urgent keywords
- Scheduling preferences and availability
- Writing style and tone variations

# Proactive email assistance:
Agent: "You have 12 new emails. I've drafted responses for 3 routine
        requests and flagged 2 urgent items from your priority contacts.
        Should I also reschedule tomorrow's meeting based on the
        conflict John mentioned?"

# Autonomous actions:
✓ Draft context-aware replies
✓ Categorize and prioritize inbox
✓ Detect scheduling conflicts
✓ Summarize long threads with key decisions
```

### 3. **Trading & Financial Monitoring**（交易与金融监控）
*Agent tracks market context and user investment behavior*
```python
# MemU learns trading preferences:
- Risk tolerance from historical decisions
- Preferred sectors and asset classes
- Response patterns to market events
- Portfolio rebalancing triggers

# Proactive alerts:
Agent: "NVDA dropped 5% in after-hours trading. Based on your past
        behavior, you typically buy tech dips above 3%. Your current
        allocation allows for $2,000 additional exposure while
        maintaining your 70/30 equity-bond target."

# Continuous monitoring:
- Track price alerts tied to user-defined thresholds
- Correlate news events with portfolio impact
- Learn from executed vs. ignored recommendations
- Anticipate tax-loss harvesting opportunities
```


...

---

## 🗂️ Hierarchical Memory Architecture（分层记忆架构）

MemU 的三层系统同时支持 **被动查询** 与 **主动上下文预加载**：

<img width="100%" alt="structure" src="assets/structure.png" />

| Layer | Reactive Use | Proactive Use |
|-------|--------------|---------------|
| **Resource** | Direct access to original data | Background monitoring for new patterns |
| **Item** | Targeted fact retrieval | Real-time extraction from ongoing interactions |
| **Category** | Summary-level overview | Automatic context assembly for anticipation |

**主动式优势：**
- **Auto-categorization（自动分类）**：新记忆自动按主题归类
- **Pattern Detection（模式检测）**：系统识别 recurring themes（重复出现的主题）
- **Context Prediction（上下文预测）**：预判下一步所需信息

---

## 🚀 Quick Start（快速开始）

### Option 1: Cloud Version（云端版本）

Experience proactive memory instantly: -> 即时体验主动式记忆：

👉 **[memu.so](https://memu.so)** - Hosted service with 7×24 continuous learning -> 托管服务，支持 7×24 小时持续学习

For enterprise deployment with custom proactive workflows, contact **info@nevamind.ai** -> 如需企业级部署及自定义主动工作流，请联系 **info@nevamind.ai**

#### Cloud API (v3)（云端 API）

| Base URL | `https://api.memu.so` |
|----------|----------------------|
| Auth | `Authorization: Bearer YOUR_API_KEY` |

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v3/memory/memorize` | Register continuous learning task -> 注册持续学习任务 |
| `GET` | `/api/v3/memory/memorize/status/{task_id}` | Check real-time processing status -> 查看实时处理状态 |
| `POST` | `/api/v3/memory/categories` | List auto-generated categories -> 列出自动生成的分类 |
| `POST` | `/api/v3/memory/retrieve` | Query memory (supports proactive context loading) -> 查询记忆（支持主动上下文预加载） |

📚 **[Full API Documentation](https://memu.pro/docs#cloud-version)**（完整 API 文档）

---

### Option 2: Self-Hosted（自托管部署）

#### Installation（安装）
```bash
pip install -e .
```

#### Basic Example（基础示例）

> **Requirements**: Python 3.13+ and an OpenAI API key -> **环境要求**：Python 3.13+ 及 OpenAI API Key

**Test Continuous Learning** (in-memory): -> **测试持续学习**（内存模式）：
```bash
export OPENAI_API_KEY=your_api_key
cd tests
python test_inmemory.py
```

**Test with Persistent Storage** (PostgreSQL): -> **测试持久化存储**（PostgreSQL）：
```bash
# Start PostgreSQL with pgvector
docker run -d \
  --name memu-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=memu \
  -p 5432:5432 \
  pgvector/pgvector:pg16

# Run continuous learning test
export OPENAI_API_KEY=your_api_key
cd tests
python test_postgres.py
```

Both examples demonstrate **proactive memory workflows**: -> 两个示例均展示了**主动式记忆工作流**：
1. **Continuous Ingestion**: Process multiple files sequentially -> **持续摄入**：顺序处理多个文件
2. **Auto-Extraction**: Immediate memory creation -> **自动提取**：即时创建记忆项
3. **Proactive Retrieval**: Context-aware memory surfacing -> **主动检索**：感知上下文的记忆召回

See [`tests/test_inmemory.py`](tests/test_inmemory.py) and [`tests/test_postgres.py`](tests/test_postgres.py) for implementation details. -> 实现细节请参见 [`tests/test_inmemory.py`](tests/test_inmemory.py) 和 [`tests/test_postgres.py`](tests/test_postgres.py)。

---

### Custom LLM and Embedding Providers（自定义 LLM 与嵌入模型提供商）

MemU supports custom LLM and embedding providers beyond OpenAI. Configure them via `llm_profiles`: -> memU 支持除 OpenAI 之外的自定义 LLM 和嵌入模型提供商。通过 `llm_profiles` 进行配置：
```python
from memu import MemUService

service = MemUService(
    llm_profiles={
        # Default profile for LLM operations
        "default": {
            "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "api_key": "your_api_key",
            "chat_model": "qwen3-max",
            "client_backend": "sdk"  # "sdk" or "http"
        },
        # Separate profile for embeddings
        "embedding": {
            "base_url": "https://api.voyageai.com/v1",
            "api_key": "your_voyage_api_key",
            "embed_model": "voyage-3.5-lite"
        }
    },
    # ... other configuration
)
```

---

### OpenRouter Integration（OpenRouter 集成）

MemU supports [OpenRouter](https://openrouter.ai) as a model provider, giving you access to multiple LLM providers through a single API. -> memU 支持使用 [OpenRouter](https://openrouter.ai) 作为模型提供商，通过单一 API 即可调用多个 LLM 服务。

#### Configuration（配置）
```python
from memu import MemoryService

service = MemoryService(
    llm_profiles={
        "default": {
            "provider": "openrouter",
            "client_backend": "httpx",
            "base_url": "https://openrouter.ai",
            "api_key": "your_openrouter_api_key",
            "chat_model": "anthropic/claude-3.5-sonnet",  # Any OpenRouter model -> 任意 OpenRouter 模型
            "embed_model": "openai/text-embedding-3-small",  # Embedding model -> 嵌入模型
        },
    },
    database_config={
        "metadata_store": {"provider": "inmemory"},
    },
)
```

#### Environment Variables（环境变量）

| Variable | Description |
|----------|-------------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key from [openrouter.ai/keys](https://openrouter.ai/keys) -> 你的 OpenRouter API Key，可在 [openrouter.ai/keys](https://openrouter.ai/keys) 获取 |

#### Supported Features（支持的功能）

| Feature | Status | Notes |
|---------|--------|-------|
| Chat Completions | Supported | Works with any OpenRouter chat model -> 兼容任意 OpenRouter 对话模型 |
| Embeddings | Supported | Use OpenAI embedding models via OpenRouter -> 通过 OpenRouter 使用 OpenAI 嵌入模型 |
| Vision | Supported | Use vision-capable models (e.g., `openai/gpt-4o`) -> 支持视觉能力模型（如 `openai/gpt-4o`） |

#### Running OpenRouter Tests（运行测试）
```bash
export OPENROUTER_API_KEY=your_api_key

# Full workflow test (memorize + retrieve)
python tests/test_openrouter.py

# Embedding-specific tests
python tests/test_openrouter_embedding.py

# Vision-specific tests
python tests/test_openrouter_vision.py
```

See [`examples/example_4_openrouter_memory.py`](examples/example_4_openrouter_memory.py) for a complete working example. -> 完整可运行示例请参见 [`examples/example_4_openrouter_memory.py`](examples/example_4_openrouter_memory.py)。

---

## 📖 Core APIs（核心 API）

### `memorize()` - Continuous Learning Pipeline（持续学习管道）

Processes inputs in real-time and immediately updates memory: -> 实时处理输入并即时更新记忆：

<img width="100%" alt="memorize" src="assets/memorize.png" />

```python
result = await service.memorize(
    resource_url="path/to/file.json",  # File path or URL -> 文件路径或 URL
    modality="conversation",            # conversation | document | image | video | audio -> 对话 | 文档 | 图片 | 视频 | 音频
    user={"user_id": "123"}             # Optional: scope to a user -> 可选：限定特定用户范围
)

# Returns immediately with extracted memory: -> 立即返回已提取的记忆数据：
{
    "resource": {...},      # Stored resource metadata -> 存储的资源元数据
    "items": [...],         # Extracted memory items (available instantly) -> 提取的记忆项（立即可用）
    "categories": [...]     # Auto-updated category structure -> 自动更新的分类结构
}
```

**Proactive Features:**（主动式特性）
- Zero-delay processing—memories available immediately -> **零延迟处理**——记忆即时可用
- Automatic categorization without manual tagging -> **自动分类**——无需手动打标签
- Cross-reference with existing memories for pattern detection -> **交叉引用**——与现有记忆比对以检测模式

### `retrieve()` - Dual-Mode Intelligence（双模式智能检索）

MemU supports both **proactive context loading** and **reactive querying**: -> memU 同时支持 **主动上下文预加载** 与 **被动查询**：

<img width="100%" alt="retrieve" src="assets/retrieve.png" />

#### RAG-based Retrieval (`method="rag"`)（基于 RAG 的检索）

Fast **proactive context assembly** using embeddings: -> 使用嵌入模型实现快速的 **主动上下文组装**：
- ✅ **Instant context**: Sub-second memory surfacing -> **即时上下文**：亚秒级记忆召回
- ✅ **Background monitoring**: Can run continuously without LLM costs -> **后台监控**：可持续运行且不产生 LLM 调用成本
- ✅ **Similarity scoring**: Identifies most relevant memories automatically -> **相似度评分**：自动识别最相关的记忆

#### LLM-based Retrieval (`method="llm"`)（基于 LLM 的检索）

Deep **anticipatory reasoning** for complex contexts: -> 针对复杂上下文进行深度 **前瞻性推理**：
- ✅ **Intent prediction**: LLM infers what user needs before they ask -> **意图预测**：LLM 在用户提问前推断需求
- ✅ **Query evolution**: Automatically refines search as context develops -> **查询演进**：随上下文演变自动优化搜索策略
- ✅ **Early termination**: Stops when sufficient context is gathered -> **提前终止**：收集到足够上下文后自动停止

#### Comparison（对比）

| Aspect | RAG (Fast Context) | LLM (Deep Reasoning) |
|--------|-------------------|---------------------|
| **Speed** | ⚡ Milliseconds -> 毫秒级 | 🐢 Seconds -> 秒级 |
| **Cost** | 💰 Embedding only -> 仅嵌入计算 | 💰💰 LLM inference -> LLM 推理消耗 |
| **Proactive use** | Continuous monitoring -> 持续监控 | Triggered context loading -> 触发式上下文加载 |
| **Best for** | Real-time suggestions -> 实时建议 | Complex anticipation -> 复杂前瞻场景 |

#### Usage（使用示例）
```python
# Proactive retrieval with context history
result = await service.retrieve(
    queries=[
        {"role": "user", "content": {"text": "What are their preferences?"}},
        {"role": "user", "content": {"text": "Tell me about work habits"}}
    ],
    where={"user_id": "123"},  # Optional: scope filter -> 可选：作用域过滤
    method="rag"  # or "llm" for deeper reasoning -> 或 "llm" 进行深度推理
)

# Returns context-aware results: -> 返回感知上下文的检索结果：
{
    "categories": [...],     # Relevant topic areas (auto-prioritized) -> 相关主题区域（自动排序）
    "items": [...],          # Specific memory facts -> 具体记忆事实
    "resources": [...],      # Original sources for traceability -> 原始来源以便追溯
    "next_step_query": "..." # Predicted follow-up context -> 预测的后续上下文查询建议
}
```

**Proactive Filtering**: Use `where` to scope continuous monitoring: -> **主动过滤**：使用 `where` 限定持续监控范围：
- `where={"user_id": "123"}` - User-specific context -> 特定用户上下文
- `where={"agent_id__in": ["1", "2"]}` - Multi-agent coordination -> 多 Agent 协同
- Omit `where` for global context awareness -> 省略 `where` 则启用全局上下文感知

---

## 💡 Proactive Scenarios（主动式场景示例）

### Example 1: Always-Learning Assistant（示例一：持续学习的助手）

Continuously learns from every interaction without explicit memory commands: -> 无需显式记忆指令，从每次交互中持续学习：
```bash
export OPENAI_API_KEY=your_api_key
python examples/example_1_conversation_memory.py
```

**Proactive Behavior:**（主动行为）
- Automatically extracts preferences from casual mentions -> 自动从闲聊中提取偏好设置
- Builds relationship models from interaction patterns -> 基于交互模式构建关系模型
- Surfaces relevant context in future conversations -> 在后续对话中召回相关上下文
- Adapts communication style based on learned preferences -> 根据学习到的偏好自适应调整沟通风格

**Best for:** Personal AI assistants, customer support that remembers, social chatbots -> **适用场景**：个人 AI 助手、记忆型客服、社交聊天机器人

---

### Example 2: Self-Improving Agent（示例二：自我优化的 Agent）

Learns from execution logs and proactively suggests optimizations: -> 从执行日志中学习并主动建议优化方案：
```bash
export OPENAI_API_KEY=your_api_key
python examples/example_2_skill_extraction.py
```

**Proactive Behavior:**（主动行为）
- Monitors agent actions and outcomes continuously -> 持续监控 Agent 动作与结果
- Identifies patterns in successes and failures -> 识别成功与失败的模式规律
- Auto-generates skill guides from experience -> 基于经验自动生成技能指南
- Proactively suggests strategies for similar future tasks -> 主动为未来类似任务提供策略建议

**Best for:** DevOps automation, agent self-improvement, knowledge capture -> **适用场景**：DevOps 自动化、Agent 自我优化、知识沉淀捕获

---

### Example 3: Multimodal Context Builder（示例三：多模态上下文构建器）

Unifies memory across different input types for comprehensive context: -> 跨输入类型统一记忆，构建全面上下文：
```bash
export OPENAI_API_KEY=your_api_key
python examples/example_3_multimodal_memory.py
```

**Proactive Behavior:**（主动行为）
- Cross-references text, images, and documents automatically -> 自动交叉引用文本、图片与文档
- Builds unified understanding across modalities -> 跨模态构建统一理解
- Surfaces visual context when discussing related topics -> 讨论相关主题时主动呈现视觉上下文
- Anticipates information needs by combining multiple sources -> 结合多源信息预判知识需求

**Best for:** Documentation systems, learning platforms, research assistants -> **适用场景**：文档管理系统、学习平台、科研助手

---

## 📊 Performance（性能表现）

MemU achieves **92.09% average accuracy** on the Locomo benchmark across all reasoning tasks, demonstrating reliable proactive memory operations. -> memU 在 Locomo 基准测试的所有推理任务中取得了 **92.09%** 的平均准确率，充分证明了其主动式记忆操作的可靠性。

<img width="100%" alt="benchmark" src="https://github.com/user-attachments/assets/6fec4884-94e5-4058-ad5c-baac3d7e76d9" />

View detailed experimental data: [memU-experiment](https://github.com/NevaMind-AI/memU-experiment) -> 查看详细实验数据：[memU-experiment](https://github.com/NevaMind-AI/memU-experiment)

---

## 🧩 Ecosystem（生态系统）

| Repository | Description | Proactive Features |
|------------|-------------|-------------------|
| **[memU](https://github.com/NevaMind-AI/memU)** | Core proactive memory engine -> 核心主动式记忆引擎 | 7×24 learning pipeline, auto-categorization -> 全天候学习管道，自动分类 |
| **[memU-server](https://github.com/NevaMind-AI/memU-server)** | Backend with continuous sync -> 支持持续同步的后端服务 | Real-time memory updates, webhook triggers -> 实时记忆更新，Webhook 触发器 |
| **[memU-ui](https://github.com/NevaMind-AI/memU-ui)** | Visual memory dashboard -> 可视化记忆仪表盘 | Live memory evolution monitoring -> 实时监控记忆演化过程 |

**Quick Links:**（快速链接）
- 🚀 [Try MemU Cloud](https://app.memu.so/quick-start)
- 📚 [API Documentation](https://memu.pro/docs)
- 💬 [Discord Community](https://discord.com/invite/hQZntfGsbJ)

---

## 🤝 Partners（合作伙伴）

<div align="center">

<a href="https://github.com/TEN-framework/ten-framework"><img src="https://avatars.githubusercontent.com/u/113095513?s=200&v=4" alt="Ten" height="40" style="margin: 10px;"></a>
<a href="https://openagents.org"><img src="assets/partners/openagents.png" alt="OpenAgents" height="40" style="margin: 10px;"></a>
<a href="https://github.com/milvus-io/milvus"><img src="https://miro.medium.com/v2/resize:fit:2400/1*-VEGyAgcIBD62XtZWavy8w.png" alt="Milvus" height="40" style="margin: 10px;"></a>
<a href="https://xroute.ai/"><img src="assets/partners/xroute.png" alt="xRoute" height="40" style="margin: 10px;"></a>
<a href="https://jaaz.app/"><img src="assets/partners/jazz.png" alt="Jazz" height="40" style="margin: 10px;"></a>
<a href="https://github.com/Buddie-AI/Buddie"><img src="assets/partners/buddie.png" alt="Buddie" height="40" style="margin: 10px;"></a>
<a href="https://github.com/bytebase/bytebase"><img src="assets/partners/bytebase.png" alt="Bytebase" height="40" style="margin: 10px;"></a>
<a href="https://github.com/LazyAGI/LazyLLM"><img src="assets/partners/LazyLLM.png" alt="LazyLLM" height="40" style="margin: 10px;"></a>
<a href="https://clawdchat.ai/"><img src="assets/partners/Clawdchat.png" alt="Clawdchat" height="40" style="margin: 10px;"></a>

</div>

---

## 🤝 How to Contribute（如何贡献）

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated. -> 我们欢迎社区贡献！无论你是修复 Bug、添加新功能还是优化文档，你的帮助都至关重要。

### Getting Started（入门指南）

To start contributing to MemU, you'll need to set up your development environment: -> 要开始为 memU 做贡献，请先配置开发环境：

#### Prerequisites（前置条件）
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (Python package manager) -> Python 包管理器
- Git

#### Setup Development Environment（设置开发环境）
```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/memU.git
cd memU

# 2. Install development dependencies
make install
```

The `make install` command will: -> `make install` 命令将执行以下操作：
- Create a virtual environment using `uv` -> 使用 `uv` 创建虚拟环境
- Install all project dependencies -> 安装所有项目依赖项
- Set up pre-commit hooks for code quality checks -> 配置 pre-commit hook 以进行代码质量检查

#### Running Quality Checks（运行质量检查）

Before submitting your contribution, ensure your code passes all quality checks: -> 提交贡献前，请确保你的代码通过所有质量检查：
```bash
make check
```

The `make check` command runs: -> `make check` 命令会执行以下操作：
- **Lock file verification**: Ensures `pyproject.toml` consistency -> **锁文件验证**：确保 `pyproject.toml` 一致性
- **Pre-commit hooks**: Lints code with Ruff, formats with Black -> **预提交钩子**：使用 Ruff 进行代码检查，使用 Black 格式化
- **Type checking**: Runs `mypy` for static type analysis -> **类型检查**：运行 `mypy` 进行静态类型分析
- **Dependency analysis**: Uses `deptry` to find obsolete dependencies -> **依赖分析**：使用 `deptry` 查找过时依赖

### Contributing Guidelines（贡献指南）

For detailed contribution guidelines, code standards, and development practices, please see [CONTRIBUTING.md](CONTRIBUTING.md). -> 详细的贡献规范、代码标准及开发实践，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

**Quick tips:**（快速提示）
- Create a new branch for each feature or bug fix -> 为每个功能或 Bug 修复创建独立分支
- Write clear commit messages -> 编写清晰的提交信息
- Add tests for new functionality -> 为新功能补充测试用例
- Update documentation as needed -> 按需更新文档
- Run `make check` before pushing -> 推送前务必运行 `make check`

---

## 📄 License（许可证）

[Apache License 2.0](LICENSE.txt)

---

## 🌍 Community（社区）

- **GitHub Issues**: [Report bugs & request features](https://github.com/NevaMind-AI/memU/issues) -> 报告 Bug 与功能请求
- **Discord**: [Join the community](https://discord.com/invite/hQZntfGsbJ) -> 加入社区交流群
- **X (Twitter)**: [Follow @memU_ai](https://x.com/memU_ai) -> 关注官方账号
- **Contact**: info@nevamind.ai

---

<div align="center">

⭐ **Star us on GitHub** to get notified about new releases! -> ⭐️ 在 GitHub 上 Star 我们，第一时间获取新版本更新通知！

</div>