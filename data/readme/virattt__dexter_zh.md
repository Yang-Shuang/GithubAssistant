# Dexter 🤖

Dexter 是一个自主的金融研究智能体（agent），能够在工作中思考、规划并学习。它利用任务规划、自我反思和实时市场数据进行分析。可以把它想象成专为金融研究打造的 Claude Code，但更专注于金融场景。

<img width="665" height="452" alt="Screenshot 2026-04-02 at 4 16 57 PM" src="https://github.com/user-attachments/assets/02418111-5f48-4a66-be5d-dc9bf9806284" />

## 📑 Table of Contents

- [👋 概述](#-overview)
- [✅ 前置条件](#-prerequisites)
- [💻 如何安装](#-how-to-install)
- [🚀 如何运行](#-how-to-run)
- [📊 如何评估](#-how-to-evaluate)
- [🐛 如何调试](#-how-to-debug)
- [📱 如何通过 WhatsApp 使用](#-how-to-use-with-whatsapp)
- [🤝 如何贡献代码](#-how-to-contribute)
- [📄 许可证](#-license)

## ⚠️ 免责声明

本项目仅用于**教育、娱乐和信息参考目的**。不应用于实际交易或投资。

- 不构成财务、投资、税务或法律建议
- 不对准确性、完整性或特定用途的适用性作任何保证
- 输出内容可能存在错误、不完整或已过时
- 创建者和贡献者不对任何财务损失或损害承担任何责任
- 做出投资决策前，请咨询持牌金融顾问
- 过往业绩不代表未来表现

使用本软件即表示你同意仅将其用于学习和信息参考目的，并接受与之相关的所有风险。

## 👋 概述

Dexter 将复杂的金融问题转化为清晰的逐步研究计划。它利用实时市场数据执行这些任务，检查自身工作成果，并不断优化结果，直至得出一个有充分数据支撑的可靠答案。  

**核心功能：**
- **智能任务规划**：自动将复杂查询分解为结构化的研究步骤
- **自主执行**：选择并运行合适的工具来收集金融数据
- **自我验证**：检查自身工作并进行迭代，直到任务完成
- **实时金融数据**：可获取利润表、资产负债表和现金流量表
- **安全特性**：内置循环检测与步骤限制，防止无限执行

[![Twitter Follow](https://img.shields.io/twitter/follow/virattt?style=social)](https://twitter.com/virattt) [![Discord](https://img.shields.io/badge/Discord-Join%20Server-5865F2?style=social&logo=discord)](https://discord.gg/jpGHv2XB6T)

<img width="1042" height="638" alt="Screenshot 2026-02-18 at 12 21 25 PM" src="https://github.com/user-attachments/assets/2a6334f9-863f-4bd2-a56f-923e42f4711e" />


## ✅ 前置条件

- [Bun](https://bun.com) 运行时环境（v1.0 或更高版本）
- OpenAI API 密钥（[点击此处获取](https://platform.openai.com/api-keys)）
- Financial Datasets API 密钥（[点击此处获取](https://financialdatasets.ai)）
- Exa API 密钥（[点击此处获取](https://exa.ai)）- 可选，用于网页搜索

#### Installing Bun

如果你尚未安装 Bun，可以通过 curl 进行安装：

**macOS/Linux:**
```bash
curl -fsSL https://bun.com/install | bash
```

**Windows:**
```bash
powershell -c "irm bun.sh/install.ps1|iex"
```

安装完成后，重启终端并验证 Bun 是否已正确安装：
```bash
bun --version
```

## 💻 如何安装

1. 克隆代码仓库：
```bash
git clone https://github.com/virattt/dexter.git
cd dexter
```

2. 使用 Bun 安装依赖项：
```bash
bun install
```

3. 配置环境变量：
```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your API keys (if using cloud providers)
# OPENAI_API_KEY=your-openai-api-key
# ANTHROPIC_API_KEY=your-anthropic-api-key (optional)
# GOOGLE_API_KEY=your-google-api-key (optional)
# XAI_API_KEY=your-xai-api-key (optional)
# OPENROUTER_API_KEY=your-openrouter-api-key (optional)

# Institutional-grade market data for agents
# FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key

# (Optional) If using Ollama locally
# OLLAMA_BASE_URL=http://127.0.0.1:11434

# Web Search (Exa preferred, Tavily fallback)
# EXASEARCH_API_KEY=your-exa-api-key
# TAVILY_API_KEY=your-tavily-api-key
```

## 🚀 如何运行

以交互模式运行 Dexter：
```bash
bun start
```

或在开发时使用监听（watch）模式：
```bash
bun dev
```

## 📊 如何评估

Dexter 内置了一套评估套件，用于在金融问题数据集上测试智能体的表现。评估过程使用 LangSmith 进行追踪，并采用“大语言模型即裁判（LLM-as-a-judge）”的方法来打分准确性。

**运行全部问题：**
```bash
bun run src/evals/run.ts
```

**随机抽样运行：**
```bash
bun run src/evals/run.ts --sample 10
```

评估运行器会显示实时界面，展示进度、当前问题以及准确率统计。结果将记录到 LangSmith 中以便分析。

## 🐛 如何调试

Dexter 会将所有工具调用记录到暂存区（scratchpad）文件中，以便调试和历史追踪。每次查询都会在 `.dexter/scratchpad/` 目录下生成一个新的 JSONL 文件。

**暂存区位置：**
```
.dexter/scratchpad/
├── 2026-01-30-111400_9a8f10723f79.jsonl
├── 2026-01-30-143022_a1b2c3d4e5f6.jsonl
└── ...
```

每个文件包含按行分隔的 JSON 记录，用于追踪：
- **init**：原始查询内容
- **tool_result**：每次工具调用的参数、原始结果及大语言模型摘要
- **thinking**：智能体的推理步骤

**示例暂存区记录：**
```json
{"type":"tool_result","timestamp":"2026-01-30T11:14:05.123Z","toolName":"get_income_statements","args":{"ticker":"AAPL","period":"annual","limit":5},"result":{...},"llmSummary":"Retrieved 5 years of Apple annual income statements showing revenue growth from $274B to $394B"}
```

这使得你可以轻松检查智能体收集了哪些数据，以及它是如何解读这些结果的。

## 📱 如何通过 WhatsApp 使用

通过将手机与网关（gateway）关联，即可通过 WhatsApp 与 Dexter 聊天。你发送给自身的消息将由 Dexter 处理，并将回复发送回同一会话中。

**快速开始：**
```bash
# Link your WhatsApp account (scan QR code)
bun run gateway:login

# Start the gateway
bun run gateway
```

然后打开 WhatsApp，进入你自己的聊天窗口（给自己发消息），并向 Dexter 提问。

如需详细的设置说明、配置选项和故障排除指南，请参阅 [WhatsApp Gateway README](src/gateway/channels/whatsapp/README.md)。

## 🤝 如何贡献代码

1. Fork（分叉）该仓库
2. 创建功能分支
3. 提交你的更改
4. 推送到该分支
5. 创建拉取请求（Pull Request）

**重要提示**：请保持你的拉取请求精简且聚焦。这将有助于加快审查和合并流程。


## 📄 许可证

本项目采用 MIT License 开源。