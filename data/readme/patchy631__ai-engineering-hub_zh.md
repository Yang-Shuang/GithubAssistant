<p align="center">
  <a href="https://trendshift.io/repositories/12800">
    <img src="assets/TRENDING-BADGE.png" alt="Trending Badge" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <img src="assets/ai-eng-hub.gif" alt="AI Engineering Hub Banner">
</p>

---

# AI 工程中心 🚀

欢迎来到 **AI 工程中心** —— 你学习与应用 AI 的全面资源库！

## 🌟 为什么选择本仓库？

AI 工程领域发展迅速，要想保持前沿地位，既需要深入的理论理解，也需要丰富的实践经验。在这里，你将找到：
- **93+ 可直接投入生产的项目**（覆盖所有技能水平）
- 关于 **大语言模型 (LLM)、检索增强生成 (RAG) 与智能体 (Agent)** 等的深度教程
- 真实的 **AI 智能体** 应用场景
- 可供你实现、适配和扩展的项目示例

无论你是初学者、实践者还是研究人员，本仓库都为不同技能水平的开发者提供了在 AI 工程领域探索与成功的资源。

---

## 📋 目录

- [入门指南](#-getting-started)
- [订阅通讯](#-stay-updated-with-our-newsletter)
- [按难度分类的项目](#-projects-by-difficulty)
  - [入门项目 (22)](#-beginner-projects)
  - [中级项目 (48)](#-intermediate-projects)
  - [高级项目 (23)](#-advanced-projects)
- [参与贡献](#-contribute-to-the-ai-engineering-hub)
- [开源协议](#-license)

---

## 🎯 入门指南

初次接触 AI 工程？从这里开始：

1. **完全初学者**：查看 [AI 工程学习路线图](./ai-engineering-roadmap)，获取系统化的学习路径
2. **掌握基础**：从 [入门项目](#-beginner-projects) 开始，例如 OCR 应用和基础的 RAG 实现
3. **提升技能**：进阶到 [中级项目](#-intermediate-projects)，学习智能体开发与复杂工作流
4. **精通高级概念**：挑战 [高级项目](#-advanced-projects)，涵盖模型微调与生产级系统

---

## 📬 订阅我们的通讯获取最新动态！

订阅我们的通讯，即可 **免费获取一本数据科学电子书** 📖！书中包含 150+ 节核心课程。第一时间掌握最新教程、行业洞察与独家资源。[立即订阅！](https://join.dailydoseofds.com)

[![Daily Dose of Data Science Newsletter](https://github.com/patchy631/ai-engineering/blob/main/resources/join_ddods.png)](https://join.dailydoseofds.com)

---

## 🎓 按难度分类的项目

### 🟢 入门项目

非常适合初学者上手 AI 工程。这些项目侧重于单一组件与基础实现。

#### OCR 与视觉处理
- [**使用 Llama 进行 LaTeX OCR**](./LaTeX-OCR-with-Llama) - 利用 Llama 3.2 视觉模型将 LaTeX 公式图片转换为代码
- [**Llama OCR**](./llama-ocr) - 基于 Llama 3.2 和 Streamlit 的 100% 本地化 OCR 应用
- [**Gemma-3 OCR**](./gemma3-ocr) - 结合 Gemma-3 实现结构化文本提取的本地 OCR
- [**Qwen 2.5 OCR**](./qwen-2.5VL-ocr) - 使用 Qwen 2.5 VL 模型进行文本提取

#### 对话界面与用户交互 (UI)
- [**使用 DeepSeek 搭建本地 ChatGPT**](./local-chatgpt%20with%20DeepSeek) - 集成 DeepSeek-R1 和 Chainlit 的轻量级 ChatGPT
- [**使用 Llama 搭建本地 ChatGPT**](./local-chatgpt) - 基于 Llama 3.2 视觉模型的 ChatGPT 克隆版
- [**使用 Gemma 3 搭建本地 ChatGPT**](./local-chatgpt%20with%20Gemma%203) - 结合 Gemma 3 的本地对话界面
- [**DeepSeek 思维链 UI**](./deepseek-thinking-ui) - 基于 DeepSeek-R1 实现可见推理过程的 ChatGPT
- [**Qwen3 思维链 UI**](./qwen3-thinking-ui) - 结合 Qwen3:4B 和 Streamlit 的思维可视化界面
- [**GPT-OSS 思维链 UI**](./gpt-oss-thinking-ui) - 支持推理过程可视化的 GPT-OSS
- [**流式 AI 对话机器人**](./streaming-ai-chatbot) - 基于 Motia 框架的实时 AI 流式对话

#### 基础 RAG（检索增强生成）
- [**Simple RAG Workflow**](./simple-rag-workflow) - 结合 LlamaIndex 与 Ollama 的基础 RAG 工作流
- [**Document Chat RAG**](./document-chat-rag) - 使用 Llama 3.3 实现文档对话
- [**Fastest RAG Stack**](./fastest-rag-stack) - 基于 SambaNova、LlamaIndex 与 Qdrant 的高速 RAG
- [**GitHub RAG**](./github-rag) - 本地化 GitHub 仓库问答
- [**ModernBERT RAG**](./modernbert-rag) - 采用 ModernBERT 嵌入向量的 RAG
- [**Llama 4 RAG**](./llama-4-rag) - 基于 Meta Llama 4 的 RAG

#### 多模态与媒体
- [**使用 Janus-Pro 生成图像**](./imagegen-janus-pro) - 使用 DeepSeek Janus-pro 7B 进行本地图像生成
- [**结合 Gemini 的视频 RAG**](./video-rag-gemini) - 借助 Gemini AI 实现视频问答

#### 其他工具
- [**Website to API with FireCrawl**](./Website-to-API-with-FireCrawl) - 将网站转换为 API 接口
- [**AI News Generator**](./ai_news_generator) - 基于 CrewAI 与 Cohere 的新闻自动生成
- [**Siamese Network**](./siamese-network) - 在 MNIST 数据集上进行数字相似度检测

---

### 🟡 中级项目

多组件系统、智能体工作流与进阶功能，适合有一定经验的开发者。

#### AI 智能体与工作流
- [**YouTube Trend Analysis**](./Youtube-trend-analysis) - 结合 CrewAI 与 BrightData 分析 YouTube 趋势
- [**AutoGen Stock Analyst**](./autogen-stock-analyst) - 基于微软 AutoGen 的高级分析师智能体
- [**Agentic RAG**](./agentic_rag) - 集成文档搜索与网页回退的 RAG
- [**Agentic RAG with DeepSeek**](./agentic_rag_deepseek) - 结合 GroundX 的企业级智能体 RAG
- [**Book Writer Flow**](./book-writer-flow) - 基于 CrewAI 的自动化书籍撰写工作流
- [**Content Planner Flow**](./content_planner_flow) - 基于 CrewAI Flow 的内容创作工作流
- [**Brand Monitoring**](./brand-monitoring) - 品牌自动监控体系
- [**Hotel Booking Crew**](./hotel-booking-crew) - 结合 DeepSeek-R1 的多智能体酒店预订系统
- [**Deploy Agentic RAG**](./deploy-agentic-rag) - 基于 LitServe 的私有化智能体 RAG API
- [**Zep Memory Assistant**](./zep-memory-assistant) - 具备拟人记忆能力的 AI 智能体
- [**Agent with MCP Memory**](./agent-with-mcp-memory) - 集成 Graphiti 记忆与 Opik 的智能体
- [**ACP Code**](./acp-code) - 智能体通信协议 (ACP) 演示
- [**Motia Content Creation**](./motia-content-creation) - 社交媒体自动化工作流

#### 语音与音频处理
- [**Real-time Voice Bot**](./real-time-voicebot) - 结合 AssemblyAI 的对话式旅行向导
- [**RAG Voice Agent**](./rag-voice-agent) - 基于 Cartesia 的实时 RAG 语音智能体
- [**Chat with Audios**](./chat-with-audios) - 针对音频文件的 RAG 问答
- [**Audio Analysis Toolkit**](./audio-analysis-toolkit) - 结合 AssemblyAI 的音频分析工具包
- [**Multilingual Meeting Notes**](./multilingual-meeting-notes-generator) - 支持自动语言检测的会议记录生成

#### 高级 RAG（检索增强生成）
- [**RAG with Dockling**](./rag-with-dockling) - 基于 IBM Docling 的 Excel 文档 RAG
- [**Trustworthy RAG**](./trustworthy-rag) - 结合 TLM 处理复杂文档的 RAG
- [**Fastest RAG with Milvus and Groq**](./fastest-rag-milvus-groq) - 检索延迟低于 15ms 的高速方案
- [**Chat with Code**](./chat-with-code) - 基于 Qwen3-Coder 的代码对话助手
- [**RAG SQL Router**](./rag-sql-router) - 集成 RAG 与 SQL 路由的智能体

#### 多模态应用
- [**DeepSeek Multimodal RAG**](./deepseek-multimodal-RAG) - 结合 DeepSeek-Janus-Pro 的多模态 RAG
- [**ColiVara Website RAG**](./Colivara-deepseek-website-RAG) - 面向网站的 MultiModal RAG (ColiVara)
- [**Multimodal RAG with AssemblyAI**](./multimodal-rag-assemblyai) - 音频处理 + 向量数据库 + CrewAI 多模态方案

#### MCP（模型上下文协议）
- [**Cursor Linkup MCP**](./cursor_linkup_mcp) - 集成深度网页搜索的自定义 MCP
- [**EyeLevel MCP RAG**](./eyelevel-mcp-rag) - 面向复杂文档 RAG 的 MCP (EyeLevel)
- [**LlamaIndex MCP**](./llamaindex-mcp) - 基于 LlamaIndex 的本地 MCP 客户端
- [**MCP Agentic RAG**](./mcp-agentic-rag) - 专为 Cursor 打造的 MCP 驱动智能体 RAG
- [**MCP Agentic RAG Firecrawl**](./mcp-agentic-rag-firecrawl) - 结合 Firecrawl 的智能体 RAG
- [**MCP Video RAG**](./mcp-video-rag) - 通过 MCP 调用 Ragie 实现视频 RAG
- [**MCP Voice Agent**](./mcp-voice-agent) - 集成 Firecrawl 与 Supabase 的语音智能体
- [**SDV MCP**](./sdv-mcp) - 合成数据仓库 (SDV) 编排工具
- [**KitOps MCP**](./kitops-mcp) - 基于 KitOps 的机器学习模型管理
- [**Stagehand × MCP-Use**](./stagehand%20x%20mcp-use) - 结合 Stagehand MCP 的网页自动化

#### 模型对比与评估
- [**Evaluation and Observability**](./eval-and-observability) - 使用 CometML Opik 进行端到端 (E2E) RAG 评估
- [**Llama 4 vs DeepSeek-R1**](./llama-4_vs_deepseek-r1) - 基于 RAG 对比 Llama 4 与 DeepSeek-R1
- [**Qwen3 vs DeepSeek-R1**](./qwen3_vs_deepseek-r1) - 结合 Opik 的 Qwen3 与 DeepSeek-R1 模型对比
- [**O3 vs Claude Code**](./o3-vs-claude-code) - 对比 Claude 3.7 和 o3
- [**Sonnet4 vs O4**](./sonnet4-vs-o4) - Sonnet 4 与 O4 代码生成能力对比
- [**Sonnet4 vs Qwen3-Coder**](./sonnet4-vs-qwen3-coder) - Sonnet 4 与 Qwen3-Coder 编程模型对比
- [**Code Model Comparison**](./code-model-comparison) - 前沿大模型代码生成能力对比
- [**GPT-OSS vs Qwen3**](./gpt-oss-vs-qwen3) - GPT-OSS 与 Qwen3 推理能力对比

---

### 🔴 高级项目

复杂系统、模型微调、生产级部署与前沿实现。

#### 模型微调与开发
- [**DeepSeek Fine-tuning**](./DeepSeek-finetuning) - 使用 Unsloth 和 Ollama 微调 DeepSeek
- [**Build Reasoning Model**](./Build-reasoning-model) - 构建类 DeepSeek-R1 推理模型
- [**Attention Is All You Need Implementation**](./attention-is-all-you-need-impl) - 从零实现 Transformer 架构

#### 高级智能体系统
- [**NVIDIA Demo**](./nvidia-demo) - 结合 CrewAI Flows 与 NVIDIA NIM 的文档撰写智能体
- [**Documentation Writer Flow**](./documentation-writer-flow) - 智能体驱动的文档编写工作流
- [**Multi-Agent Deep Researcher**](./Multi-Agent-deep-researcher-mcp-windows-linux) - 基于 MCP 的深度研究智能体（支持 Windows/Linux）
- [**Multiplatform Deep Researcher**](./multiplatform_deep_researcher) - 结合 BrightData 的多平台深度研究系统
- [**Web Browsing Agent**](./web-browsing-agent) - 集成 CrewAI 与 Stagehand 的网页浏览智能体
- [**Paralegal Agent Crew**](./paralegal-agent-crew) - 基于 RAG 的智能法律助理
- [**FireCrawl Agent**](./firecrawl-agent) - 结合网络搜索回退机制的纠偏型 RAG
- [**Context Engineering Workflow**](./context-engineering-workflow) - 集成 TensorLake 与 Zep 的研究助手工作流
- [**Parlant Conversational Agent**](./parlant-conversational-agent) - 合规驱动型对话智能体 (Parlant)
- [**Stock Portfolio Analysis Agent**](./stock-portfolio-analysis-agent) - 结合 React 前端的投资组合分析智能体
- [**Guidelines vs Traditional Prompt**](./guidelines-vs-traditional-prompt) - 结构化指南与传统 Prompt 的对比实验

#### 高级 MCP 与基础设施
- [**MindsDB MCP**](./mindsdb-mcp) - 面向全数据源的统一 MCP (MindsDB)
- [**Financial Analyst DeepSeek**](./financial-analyst-deepseek) - 基于 DeepSeek 的 MCP 财务分析工作流
- [**Graphiti MCP**](./graphiti-mcp) - 结合 Zep Graphiti 的持久化记忆系统
- [**Pixeltable MCP**](./pixeltable-mcp) - 统一多模态数据编排 (Pixeltable)
- [**Ultimate AI Assistant**](./ultimate-ai-assitant-using-mcp) - 支持多 MCP 服务器的终极 AI 助手

#### 生产级系统
- [**GroundX Document Pipeline**](./groundX-doc-pipeline) - 企业级文档处理流水线 (GroundX)
- [**NotebookLM Clone**](./notebook-lm-clone) - 完整复刻 NotebookLM，集成 RAG、引用溯源与播客生成

#### 学习资源
- [**AI Engineering Roadmap**](./ai-engineering-roadmap) - 从 Python 基础到生产级 AI 的完整指南 (AI 工程学习路线图)

---

## 📢 参与贡献！

我们欢迎所有开发者加入！无论你是想添加新教程、优化现有代码，还是报告问题，你的贡献都将推动社区蓬勃发展。参与方式如下：

1. **Fork** 本仓库
2. 为你的贡献创建一个新的分支
3. 提交 **Pull Request** 并描述你所做的改进

查看我们的 [贡献指南](CONTRIBUTING.md) 了解更多详情。

---

## 📜 开源协议

本仓库采用 MIT License 开源协议 - 详情请参阅 [LICENSE](LICENSE) 文件。

---

## 💬 联系我们

如需讨论、提出建议或反馈，欢迎随时 [创建 Issue](https://github.com/patchy631/ai-engineering/issues) 或直接联系！

**祝你编码愉快！** 🎉