# Awesome n8n 模板合集

> GitHub 上最大的开源 n8n 自动化模板集合。浏览 280+ 个免费、即插即用的工作流模板，涵盖 Gmail、Telegram、OpenAI、WhatsApp、Slack、Discord、WordPress、Google Sheets 等数十个平台。持续更新中（截至 2026年3月）。

<p align="center">
  <a href="https://trendshift.io/repositories/14621" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/14621" alt="enescingoz%2Fawesome-n8n-templates | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/enescingoz/awesome-n8n-templates?style=social" alt="GitHub Stars" /> <img src="https://img.shields.io/github/forks/enescingoz/awesome-n8n-templates?style=social" alt="GitHub Forks" /> <img src="https://img.shields.io/badge/templates-280+-blue" alt="Templates" /> <img src="https://img.shields.io/badge/license-CC--BY--4.0-blue" alt="License" /> <img src="https://img.shields.io/github/last-commit/enescingoz/awesome-n8n-templates" alt="Last Commit" /> <img src="https://awesome.re/badge.svg" alt="Awesome" />
</p>

---

<p align="center">
  <a href="README-tr.md"><img src="https://img.shields.io/badge/Türkçe-Tıkla-crimson" alt="Türkçe" /></a> | <a href="README.md"><img src="https://img.shields.io/badge/English-Click-yellow" alt="English" /></a> | <a href="README-zh.md"><img src="https://img.shields.io/badge/中文-点击查看-orange" alt="中文" /></a> | <a href="README-de.md"><img src="https://img.shields.io/badge/Deutsch-Klicken-blue" alt="Deutsch" /></a> | <a href="README-fr.md"><img src="https://img.shields.io/badge/Français-Cliquer-green" alt="Français" /></a> | <a href="README-es.md"><img src="https://img.shields.io/badge/Español-Clic-red" alt="Español" /></a> | <a href="README-pt.md"><img src="https://img.shields.io/badge/Português-Clique-brightgreen" alt="Português" /></a> | <a href="README-ja.md"><img src="https://img.shields.io/badge/日本語-クリック-blueviolet" alt="日本語" /></a> | <a href="README-ko.md"><img src="https://img.shields.io/badge/한국어-클릭-ff69b4" alt="한국어" /></a> | <a href="README-hi.md"><img src="https://img.shields.io/badge/हिन्दी-क्लिक-orange" alt="हिन्दी" /></a> | <a href="README-ar.md"><img src="https://img.shields.io/badge/العربية-انقر-green" alt="العربية" /></a> | <a href="README-id.md"><img src="https://img.shields.io/badge/Bahasa_Indonesia-Klik-red" alt="Bahasa Indonesia" /></a> | <a href="README-ru.md"><img src="https://img.shields.io/badge/Русский-Нажмите-blue" alt="Русский" /></a> | <a href="README-it.md"><img src="https://img.shields.io/badge/Italiano-Clicca-brightgreen" alt="Italiano" /></a>
</p>

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="https://img.shields.io/badge/Try_n8n_Free-Start_Automating-orange?style=for-the-badge" alt="Try n8n Free" />
  </a>
</p>

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="/img/n8n.png" alt="n8n automation platform" style="max-height: 300px;" />
  </a>
</p>

---

## 目录

- [快速入门：如何使用这些模板](#quick-start-how-to-use-these-templates)
- [为什么选择 n8n？](#why-n8n)
- [仓库统计](#repository-statistics)
- [免责声明](#disclaimer)
- [分类与模板列表](#categories--template-list)
  - [Gmail 与邮件自动化](#what-n8n-templates-are-available-for-gmail-and-email-automation)
  - [Telegram](#how-can-i-automate-telegram-bots-with-n8n)
  - [Google Drive 与 Google Sheets](#what-are-the-best-n8n-templates-for-google-drive-and-google-sheets)
  - [WordPress](#how-do-i-automate-wordpress-with-n8n)
  - [PDF 与文档处理](#what-n8n-templates-exist-for-pdf-and-document-processing)
  - [Discord](#how-can-i-automate-discord-with-n8n)
  - [数据库与存储](#what-are-the-best-n8n-database-and-storage-automation-templates)
  - [DevOps / 服务器自动化](#what-n8n-templates-are-available-for-devops-and-server-automation)
  - [Airtable](#how-do-i-automate-airtable-with-n8n)
  - [Notion](#what-are-the-best-n8n-templates-for-notion)
  - [Slack](#how-can-i-automate-slack-with-n8n)
  - [OpenAI、大语言模型（LLM）与 AI Agent](#what-n8n-templates-are-available-for-openai-llms-and-ai-agents)
  - [WhatsApp](#how-do-i-build-whatsapp-chatbots-with-n8n)
  - [Instagram、Twitter 与社交媒体](#what-are-the-best-n8n-templates-for-social-media-automation)
  - [其他集成与用例](#what-other-n8n-integration-templates-are-available)
  - [表单与调查](#how-do-i-automate-forms-and-surveys-with-n8n)
  - [AI 研究、RAG（检索增强生成）与数据分析](#what-n8n-templates-exist-for-ai-research-rag-and-data-analysis)
  - [其他](#other)
- [常见问题 (FAQ)](#faq)
- [贡献指南](#contributing)
- [Star 历史](#star-history)
- [贡献者](#contributors)
- [赞助商](#sponsors)

---

## 快速入门：如何使用这些模板

1. **[注册 n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe)**（免费且开源）
2. 从本仓库下载任意 `.json` 模板文件
3. 在 n8n 中，前往 **工作流 → 从文件导入**，选择 JSON 文件
4. 为每个连接的服务配置你的凭据
5. 激活工作流并开始自动化！

---

## 为什么选择 n8n？

[n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) 是一款开源的工作流自动化平台，让你能够将任意服务与数据源连接起来。与闭源替代品不同，n8n 赋予你对数据和基础设施的完全控制权。其核心优势包括：

- **开源且支持自托管** -- 运行在你自己的服务器上，无厂商锁定风险
- **内置 400+ 集成** -- 可连接几乎任何服务或 API
- **可视化工作流编辑器** -- 通过拖拽节点构建自动化流程，无需编写代码
- **AI 原生能力** -- 内置对 OpenAI、Claude、Gemini、LangChain 及向量数据库的支持
- **免费起步** -- n8n Cloud 提供慷慨的免费套餐，或完全免费自托管

无论你是想自动化邮件工作流、构建 AI 聊天机器人、处理文档，还是编排 DevOps 流水线，n8n 都是这些模板运行的坚实基础。

---

## 仓库统计

- **280+ 个自动化模板**，涵盖 18 个分类
- **19,000+ GitHub Stars**，来自自动化社区的支持
- **覆盖平台**：Gmail、Telegram、Google Drive、Google Sheets、WordPress、Discord、Slack、Notion、Airtable、WhatsApp、Instagram、Twitter/X、LinkedIn、Spotify、Pinterest、Todoist、Obsidian 等
- **AI 集成**：OpenAI GPT-4、Anthropic Claude、Google Gemini、DeepSeek R1、Mistral AI、LangChain、Perplexity、Hugging Face 等
- **典型用例**：邮件自动化、AI 聊天机器人、RAG 流水线、文档处理、社交媒体管理、HR 工作流、DevOps 自动化、潜在客户筛选、情感分析、数据提取等
- **数据库支持**：PostgreSQL、MongoDB、SQLite、Supabase、Pinecone、Qdrant、Elasticsearch、Airtable、NocoDB、Baserow

---

## 免责声明

本仓库中的所有自动化模板均来源于网络，仅用于方便访问和分享。这些模板并非由仓库作者创建或拥有。如果你在使用这些模板时遇到任何问题、错误或损失，仓库作者不承担任何责任或义务。所有原始模板的版权均归其各自的创作者所有。

---

## 分类与模板列表

### Gmail 与邮件自动化有哪些 n8n 模板？

本合集包含 9 个适用于 n8n 的邮件自动化模板，涵盖 Gmail、Outlook 和 IMAP。模板范围从利用 OpenAI 进行 AI 驱动的邮件标签分类，到钓鱼检测、自动回复起草以及每日财经新闻推送。非常适合希望简化邮件管理的运营、安全及高管团队。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 使用 AI 节点自动标记 Gmail 收件箱消息 | 利用 AI 自动为传入的 Gmail 消息打标签。工作流会提取邮件内容，建议如“合作”或“咨询”等标签，并自动分配以实现更好的分类管理。 | 运营 | [模板链接](Gmail_and_Email_Automation/Auto-label%20incoming%20Gmail%20messages%20with%20AI%20nodes.json) |
| 使用 OpenAI 和 Gmail API 进行基础自动邮件标签分类 | 结合 OpenAI 与 Gmail API，在收到新邮件时触发工作流，分析内容并自动分配或创建标签。利用 AI 高效归类邮件。 | 运营 | [模板链接](Gmail_and_Email_Automation/Basic%20Automatic%20Gmail%20Email%20Labelling%20with%20OpenAI%20and%20Gmail%20API.json) |
| 使用 OpenAI Assistant 在 Gmail 中起草回复 | 利用 OpenAI 生成 Gmail 回复草稿。在新邮件到达时触发，提取内容并创建建议的回复草稿，以简化响应流程。 | 高管 | [模板链接](Gmail_and_Email_Automation/Compose%20reply%20draft%20in%20Gmail%20with%20OpenAI%20Assistant.json) |
| 使用 ChatGPT 分析与分类可疑邮件内容 | 利用 ChatGPT 分析可疑邮件，进行分类处理，并可生成截图供审核。有助于识别并整理潜在的危险邮件。 | 安全 | [模板链接](Gmail_and_Email_Automation/Analyze%20&%20Sort%20Suspicious%20Email%20Contents%20with%20ChatGPT.json) |
| 使用 ChatGPT Vision 分析可疑邮件内容 | 结合文本与图像分析（ChatGPT Vision）评估可疑邮件。提取截图，分析头部信息与正文内容，并标记钓鱼尝试。 | 安全 | [模板链接](Gmail_and_Email_Automation/Analyze%20Suspicious%20Email%20Contents%20with%20ChatGPT%20Vision.json) |
| 基于 AI 和 IMAP 的简易“人机协同”邮件回复系统 | 实现一个简单的人机协同邮件回复工作流。使用 IMAP 获取邮件，利用 AI 摘要内容，并在发送前起草专业回复供人工审核。 | 客服/支持 | [模板链接](Gmail_and_Email_Automation/A%20Very%20Simple%20_Human%20in%20the%20Loop_%20Email%20Response%20System%20Using%20AI%20and%20IMAP.json) |
| 使用 AI 自动分类 Outlook 邮件 | 利用 AI 模型自动对 Outlook 邮件进行分类。根据内容将消息移动至相应文件夹并分配类别，减少手动整理工作。 | 运营 | [模板链接](Gmail_and_Email_Automation/Auto%20Categorise%20Outlook%20Emails%20with%20AI.json) |
| Microsoft Outlook AI 邮件助手（集成 Monday 与 Airtable 联系人支持） | 一款为 Outlook 打造的 AI 助手，可处理邮件、清洗内容，并根据 Airtable 中的规则分配类别。同时集成 Monday.com 提供联系人支持。 | 运营 | [模板链接](Gmail_and_Email_Automation/Microsoft%20Outlook%20AI%20Email%20Assistant%20with%20contact%20support%20from%20Monday%20and%20Airtable.json) |
| 📈 将 FT.com 每日市场新闻推送至你的 Microsoft Outlook 收件箱 | 从 FT.com 提取财经新闻，并将每日更新自动推送到你的 Outlook 收件箱。自动化内容抓取与邮件投递，助你及时获取市场洞察。 | 高管 | [模板链接](Gmail_and_Email_Automation/📈%20Receive%20Daily%20Market%20News%20from%20FT.com%20to%20your%20Microsoft%20outlook%20inbox.json) |
| 基于 Ollama 的 AI 邮件自动回复器 | 使用 Ollama 本地 AI 对传入邮件进行分类、过滤垃圾邮件，并生成上下文感知的回复草稿。无需外部 API Key。 | 客服/支持 | [模板链接](Gmail_and_Email_Automation/AI%20Email%20Auto-Responder%20with%20Ollama.json) |
| InboxZero Lite - AI 邮件分类器 | 利用 OpenAI gpt-4o-mini 将 Gmail 邮件自动归类为紧急、重要、信息或垃圾邮件。采用轻量级单工作流架构，并集成 Google Sheets 进行日志记录。 | 运营 | [模板链接](Gmail_and_Email_Automation/InboxZero%20Lite%20-%20AI%20Email%20Classifier.json) |
| LeadPilot Lite - AI 冷邮件撰写器 | 利用 OpenAI 根据 Google Sheets 中的潜在客户列表，自动生成个性化冷邮件。为每位目标客户定制标题与正文内容。 | 销售 | [模板链接](Gmail_and_Email_Automation/LeadPilot%20Lite%20-%20AI%20Cold%20Email%20Writer.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 如何使用 n8n 自动化 Telegram 机器人？

探索 18 个适用于 n8n 的 Telegram 自动化模板，包括结合 LangChain 和 OpenAI 的 AI 聊天机器人、支持 55 种语言的语音转文本翻译、PDF 对话功能、图像分析机器人以及 Spotify 集成。这些模板覆盖了 Telegram 在客服、营销和内容审核等场景的应用。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 基于 LangChain 节点与新工具的 Agentic Telegram AI 机器人 | 一款高级 Telegram 机器人，利用 LangChain 和 OpenAI 实现对话式 AI。支持记忆功能、动态工具调用，并处理传入事件，提供丰富且上下文感知的聊天交互体验。 | 客服/支持 | [模板链接](Telegram/Agentic%20Telegram%20AI%20bot%20with%20with%20LangChain%20nodes%20and%20new%20tools.json) |
| AI 驱动的 Telegram 阿拉伯语儿童故事讲述 | 一款 Telegram 机器人，利用 OpenAI 生成并朗读阿拉伯语儿童故事，为年轻用户打造互动式、教育性的阅读体验。 | 客服/支持 | [模板链接](Telegram/AI-Powered%20Children_s%20Arabic%20Storytelling%20on%20Telegram.json) |
| AI 驱动的 Telegram 英语儿童故事讲述（集成 OpenAI） | 利用 OpenAI 创作并朗读英语儿童故事，以互动方式吸引年轻受众。 | 客服/支持 | [模板链接](Telegram/AI-Powered%20Children_s%20English%20Storytelling%20on%20Telegram%20with%20OpenAI.json) |
| 通过 Telegram 实现自动化 AI 图像分析与响应 | 允许用户向 Telegram 发送图片，并自动接收基于 AI 的分析结果与反馈。 | 运营 | [模板链接](Telegram/Automated%20AI%20image%20analysis%20and%20response%20via%20Telegram.json) |
| Angie：具备语音与文本功能的个人 AI 助手 | 一款个人语音/文本助手机器人，利用 AI 回答问题、管理任务，并提供自然的交互体验。 | 客服/支持 | [模板链接](Telegram/Angie,%20Personal%20AI%20Assistant%20with%20Telegram%20Voice%20and%20Text.json) |
| 通过简易 Telegram 机器人对话 OpenAI GPT | 一个极简的 Telegram 机器人，将用户消息转发至 GPT 并返回 AI 生成的回复。是入门 AI 聊天的理想起点。 | 客服/支持 | [模板链接](Telegram/Chat%20with%20OpenAIs%20GPT%20via%20a%20simple%20Telegram%20Bot.json) |
| Telegram AI 机器人助手：现成的语音与文本消息处理模板 | 开箱即用的助手机器人，支持语音和文本输入，利用 AI 在 Telegram 中实现智能对话回复。 | 客服/支持 | [模板链接](Telegram/Telegram%20AI%20bot%20assistant_%20ready-made%20template%20for%20voice%20&%20text%20messages.json) |
| Telegram AI Bot：NeurochainAI 文本与图像生成 | 集成 NeurochainAI API，在 Telegram 内实现文本与图像的生成，支持创意媒体交互。 | 市场/营销 | [模板链接](Telegram/Telegram%20AI%20Bot_%20NeurochainAI%20Text%20&%20Image%20-%20NeurochainAI%20Basic%20API%20Integration.json) |
| 基于 LangChain 节点的 Telegram AI 机器人 | 使用 LangChain 节点在 Telegram 中实现高级 AI 对话与工具调用。 | 客服/支持 | [模板链接](Telegram/Telegram%20AI%20bot%20with%20LangChain%20nodes.json) |
| Telegram AI Chatbot | 适用于 Telegram 的通用型 AI 聊天机器人模板，可根据多种用例进行自定义配置。 | 客服/支持 | [模板链接](Telegram/Telegram%20AI%20Chatbot.json) |
| 集成 Supabase 记忆与 OpenAI Assistant 的 Telegram 机器人 | 为 Telegram 机器人添加基于 Supabase 的长期记忆功能，并结合 OpenAI 实现丰富且上下文感知的对话。 | 客服/支持 | [模板链接](Telegram/Telegram%20Bot%20with%20Supabase%20memory%20and%20OpenAI%20assistant%20integration.json) |
| Telegram PDF 对话 | 允许用户向 Telegram 上传 PDF 文件，并利用 AI 驱动的摘要与问答功能与其内容进行交互。 | 运营 | [模板链接](Telegram/Telegram%20chat%20with%20PDF.json) |
| 🤖 Telegram 文本_音频_图像消息处理 Agent | 多模态 Agent，利用 AI 在 Telegram 聊天中处理文本、音频和图像并生成回复。 | 客服/支持 | [模板链接](Telegram/%F0%9F%A4%96%20Telegram%20Messaging%20Agent%20for%20Text_Audio_Images.json) |
| Telegram 对接 Spotify（集成 OpenAI） | 允许用户在 Telegram 中点播歌曲或歌单，并通过 OpenAI 自动在 Spotify 中创建。 | 市场/营销 | [模板链接](Telegram/Telegram%20to%20Spotify%20with%20OpenAI.json) |
| 每日向 Telegram 推送随机食谱 | 定时工作流，每天抓取一份随机食谱并发布到指定的 Telegram 聊天频道中。 | 市场/营销 | [模板链接](Telegram/Send%20a%20random%20recipe%20once%20a%20day%20to%20Telegram.json) |
| 检测 Telegram 消息中的有毒语言 | 监控 Telegram 聊天频道，利用 AI 审核标记包含攻击性/毒性语言的/messages。 | 安全 | [模板链接](Telegram/Detect%20toxic%20language%20in%20Telegram%20messages.json) |
| 使用 AI 翻译 Telegram 语音消息（支持 55 种语言） | 接收语音消息，进行转录，并将翻译结果发送回超过 50 种语言的频道。 | 客服/支持 | [模板链接](Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json) |
| 通过长期记忆与动态工具路由赋能你的 AI Chatbot | 外部工作流，为 AI 聊天机器人添加长期记忆与动态工具路由能力。 | 客服/支持 | [模板链接](https://n8n.io/workflows/3025-empower-your-ai-chatbot-with-long-term-memory-and-dynamic-tool-routing/) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### Google Drive 与 Google Sheets 有哪些最佳的 n8n 模板？

浏览 13 个适用于 n8n 的 Google Drive 和 Google Sheets 自动化模板。包含企业文档 RAG 聊天机器人、OpenAI 模型微调流水线、自动背景移除、基于 GPT-4 的潜在客户筛选、HR 简历初筛以及文档摘要工作流。非常适合运营、销售、市场及工程团队。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 集成 Google Drive 的 OpenAI 模型自动化端到端微调 | 通过集成 Google Drive 进行数据输入与输出，实现 OpenAI 模型的自动化微调流程，简化自定义 AI 模型的训练。 | 工程 | [模板链接](Google_Drive_and_Google_Sheets/Automated%20End-to-End%20Fine-Tuning%20of%20OpenAI%20Models%20with%20Google%20Drive%20Integration.json) |
| Google Drive 图片自动背景移除 | 自动移除存储在 Google Drive 中的图片背景，为产品目录或营销素材等用途做好准备。 | 市场/营销 | [模板链接](Google_Drive_and_Google_Sheets/Automatic%20Background%20Removal%20for%20Images%20in%20Google%20Drive.json) |
| 构建集成 Google Drive 的 OpenAI Assistant | 演示如何构建可访问并利用 Google Drive 文件的 OpenAI Assistant，使其能够根据文档内容回答问题或执行任务。 | 客服/支持 | [模板链接](Google_Drive_and_Google_Sheets/Build%20an%20OpenAI%20Assistant%20with%20Google%20Drive%20Integration.json) |
| 基于 Google Drive 和 Gemini 的企业文档 RAG Chatbot | 创建一个检索增强生成（RAG）聊天机器人，利用 Google Gemini 回答存储在 Google Drive 中的企业文档相关问题。 | 客服/支持 | [模板链接](Google_Drive_and_Google_Sheets/RAG%20Chatbot%20for%20Company%20Documents%20using%20Google%20Drive%20and%20Gemini.json) |
| RAG_Context-Aware 分块：通过 OpenRouter & Gemini 将 Google Drive 数据导入 Pinecone | 实现针对 Google Drive 文档的上下文感知分块，将其发送至 Pinecone 进行向量存储，并利用 OpenRouter 与 Gemini 执行高级 RAG。 | 工程 | [模板链接](Google_Drive_and_Google_Sheets/RAG_Context-Aware%20Chunking%20_%20Google%20Drive%20to%20Pinecone%20via%20OpenRouter%20&%20Gemini.json) |
| 摘要 Google Drive 中的新文档并将摘要保存至 Google Sheet | 监控 Google Drive 中的新文档，利用 AI 对其内容进行摘要，并将这些摘要保存到 Google Sheet 中以便快速概览与分析。 | 运营 | [模板链接](Google_Drive_and_Google_Sheets/Summarize%20the%20New%20Documents%20from%20Google%20Drive%20and%20Save%20Summary%20in%20Google%20Sheet.json) |
| 从 Google Drive 上传至 Instagram 和 Tiktok | 自动化将媒体文件从 Google Drive 直接上传至 Instagram 和 TikTok，简化社交媒体内容发布流程。 | 市场/营销 | [模板链接](Google_Drive_and_Google_Sheets/Upload%20to%20Instagram%20and%20Tiktok%20from%20Google%20Drive.json) |
| 从 Google Sheets 撰写并发布博客文章 | 允许在 Google Sheets 中编写博客文章，并自动发布到内容管理系统（CMS），简化内容创作与发布流程。 | 市场/营销 | [模板链接](Google_Drive_and_Google_Sheets/Author%20and%20Publish%20Blog%20Posts%20From%20Google%20Sheets.json) |
| 使用 AI 对话 Google Sheet | 允许用户通过自然语言与 Google Sheet 中的数据进行交互和查询，利用 AI 模型降低数据分析门槛。 | 运营 | [模板链接](Google_Drive_and_Google_Sheets/Chat%20with%20a%20Google%20Sheet%20using%20AI.json) |
| 在 Telegram 中通过 Google Sheets 对话你的活动日程 | 将包含活动日程的 Google Sheet 连接到 Telegram，允许用户通过 Telegram 机器人查询个人日程。 | 运营 | [模板链接](Google_Drive_and_Google_Sheets/Chat%20with%20your%20event%20schedule%20from%20Google%20Sheets%20in%20Telegram.json) |
| 通过 OpenAI GPT-4 筛选 Google Sheets 中的新潜在客户 | 利用 OpenAI GPT-4 分析并筛选录入 Google Sheet 的新潜在客户，帮助销售团队优先跟进高价值线索。 | 销售 | [模板链接](Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20Sheets%20via%20OpenAI_s%20GPT-4.json) |
| AI 简历初筛、通知 HR 并保存至 Google Sheet | 利用 AI 自动化求职者简历筛选流程，向 HR 推送合格候选人信息，并将申请人数据自动存入 Google Sheet。 | 人力资源/HR | [模板链接](Google_Drive_and_Google_Sheets/Screen%20Applicants%20With%20AI,%20notify%20HR%20and%20save%20them%20in%20a%20Google%20Sheet.json) |
| 使用 OpenAI GPT-4 摘要 Google Sheets 表单反馈 | 利用 OpenAI GPT-4 对通过 Google Forms 收集并存储在 Google Sheet 中的反馈进行摘要，快速提取调查洞察。 | 市场/营销 | [模板链接](Google_Drive_and_Google_Sheets/Summarize%20Google%20Sheets%20form%20feedback%20via%20OpenAI_s%20GPT-4.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 如何使用 n8n 自动化 WordPress？

本部分提供 6 个适用于 n8n 的 WordPress 自动化模板。利用 AI 自动分类和标记博客文章、生成符合品牌调性的内容、使用 DeepSeek R1 快速创作内容、集成 Supabase 与 OpenAI 嵌入 AI 聊天机器人，或仅凭几个关键词即可撰写完整的博客文章。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 在 WordPress 中使用 AI 自动分类博客文章 | 该工作流利用 AI 自动化 WordPress 博客文章的分类过程，简化内容组织与管理。 | 市场/内容 | [模板链接](WordPress/Auto-Categorize%20blog%20posts%20in%20wordpress%20using%20A.I..json) |
| 在 WordPress 中使用 AI 自动标记博客文章 | 该工作流利用 AI 为 WordPress 博客文章自动生成标签，提升 SEO 效果与内容可发现性。 | 市场/内容 | [模板链接](WordPress/Auto-Tag%20Blog%20Posts%20in%20WordPress%20with%20AI.json) |
| 使用 AI 自动化品牌语调博客创作 | 该工作流利用 AI 自动生成符合特定品牌调性的博客文章，确保内容风格统一。 | 市场/内容 | [模板链接](WordPress/Automate%20Blog%20Creation%20in%20Brand%20Voice%20with%20AI.json) |
| 使用 DeepSeek R1 自动化 WordPress 内容生成器 | 该工作流利用 DeepSeek R1 AI 模型为 WordPress 自动生成内容，实现快速内容创作。 | 市场/内容 | [模板链接](WordPress/Automate%20Content%20Generator%20for%20WordPress%20with%20DeepSeek%20R1.json) |
| WordPress - AI Chatbot 提升用户体验（集成 Supabase 和 OpenAI） | 该工作流通过 Supabase 和 OpenAI 将 AI 聊天机器人嵌入 WordPress，提供智能交互以优化用户体验。 | 客服/市场 | [模板链接](WordPress/WordPress%20-%20AI%20Chatbot%20to%20enhance%20user%20experience%20-%20with%20Supabase%20and%20OpenAI.json) |
| 使用 AI 撰写 WordPress 文章（从几个关键词开始） | 该工作流利用 AI 根据少量关键词生成 WordPress 文章，简化内容创作流程。 | 市场/内容 | [模板链接](WordPress/Write%20a%20WordPress%20post%20with%20AI%20(starting%20from%20a%20few%20keywords).json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### PDF 与文档处理有哪些 n8n 模板？

找到 11 个适用于 n8n 的 PDF 和文档处理模板。这些工作流支持 AI 驱动的 PDF 问答（带来源引用）、多模态视觉 AI 简历解析、通过 LlamaParse 提取发票数据、文档转学习笔记转换、ETL 文本流水线、HTML 转 Markdown 等。支持 Claude、Gemini、MistralAI 和 OpenAI 模型。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 使用 AI 向 PDF 提问 | 该工作流从 Google Drive 获取 PDF，将其分块，利用 OpenAI Embeddings 进行向量嵌入，并支持与文档内容交互对话。 | 客服/知识管理 | [模板链接](PDF_and_Document_Processing/Ask%20questions%20about%20a%20PDF%20using%20AI.json) |
| 使用 MistralAI 和 Qdrant 将文档拆解为学习笔记 | 该工作流在检测到新文件时触发，利用 MistralAI Embeddings 处理文档，并将数据存入 Qdrant 向量库以生成学习笔记。 | 教育/知识管理 | [模板链接](PDF_and_Document_Processing/Breakdown%20Documents%20into%20Study%20Notes%20using%20Templating%20MistralAI%20and%20Qdrant.json) |
| 多模态视觉 AI PDF 简历解析 | 该工作流将候选人简历 PDF 转换为图像，使用视觉语言模型评估人岗匹配度，并包含逻辑以绕过简历中隐藏的 AI Prompt。 | 人力资源/HR | [模板链接](PDF_and_Document_Processing/CV%20Resume%20PDF%20Parsing%20with%20Multimodal%20Vision%20AI.json) |
| 使用 AI 对话 PDF 文档（带来源引用） | 该工作流支持与 PDF 文档交互对话，允许用户提问并获取带有原文引用的答案。 | 客服/知识管理 | [模板链接](PDF_and_Document_Processing/Chat%20with%20PDF%20docs%20using%20AI%20(quoting%20sources).json) |
| 将 URL HTML 转换为 Markdown 格式并提取页面链接 | 该工作流将指定 URL 的 HTML 内容转换为 Markdown 格式，并提取所有页面链接，适用于内容抓取与分析。 | 市场/内容 | [模板链接](PDF_and_Document_Processing/Convert%20URL%20HTML%20to%20Markdown%20Format%20and%20Get%20Page%20Links.json) |
| 文本处理 ETL 流水线 | 该工作流实现用于文本处理的 ETL 流水线，从 Twitter 提取数据，存储至 MongoDB 和 PostgreSQL，并根据情感分析结果向 Slack 发送警报。 | 数据分析/IT | [模板链接](PDF_and_Document_Processing/ETL%20pipeline%20for%20text%20processing.json) |
| 使用 Claude 和 Gemini 直接从 PDF 提取与处理信息 | 该工作流利用 Claude 和 Gemini 等高级 AI 模型直接从 PDF 中提取并处理信息，实现智能文档分析。 | 数据提取/IT | [模板链接](PDF_and_Document_Processing/Extract%20and%20process%20information%20directly%20from%20PDF%20using%20Claude%20and%20Gemini.json) |
| 从简历提取数据并使用 Gotenberg 生成 PDF | 该工作流利用 AI 从简历中提取结构化数据，转换为 HTML，随后使用 Gotenberg 生成排版精美的 PDF。 | 人力资源/HR | [模板链接](PDF_and_Document_Processing/Extract%20data%20from%20resume%20and%20create%20PDF%20with%20Gotenberg.json) |
| 从通过 n8n 表单上传的图片中提取车牌号 | 该工作流利用视觉语言模型，从通过 n8n 表单上传的图片中提取车牌号码，并展示提取结果。 | 运营/物流 | [模板链接](PDF_and_Document_Processing/Extract%20license%20plate%20number%20from%20image%20uploaded%20via%20an%20n8n%20form.json) |
| 使用 Vertex AI (Gemini) 从 PDF 和图片中提取文本至 CSV | 该工作流利用 Vertex AI (Gemini) 从 PDF 和图片中提取文本，根据文件类型路由数据，并将提取结果转换为 CSV 格式。 | 数据提取/IT | [模板链接](PDF_and_Document_Processing/Extract%20text%20from%20PDF%20and%20image%20using%20Vertex%20AI%20(Gemini)%20into%20CSV.json) |
| 使用 LlamaParse 和 OpenAI 提取发票数据 | 该工作流利用 LlamaParse 和 OpenAI 从发票中提取结构化数据，随后通过结构化输出解析器进行深度处理。 | 财务/行政 | [模板链接](PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20LlamaParse%20and%20OpenAI.json) |
| 使用 Cradl AI 结合人工审核与自动训练从 PDF 提取数据 | 利用 Cradl AI 从发票及类似文档中提取结构化数据。在低置信度预测进入系统前标记供人工复核，并在批准修正后自动重新训练模型，同时内置 LLM Guardrails 检测并拒绝幻觉输出。 | 财务/物流/运营 | [模板链接](PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20human-in-the-loop%20validation%20and%20auto-training%20using%20Cradl%20AI.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 如何使用 n8n 自动化 Discord？

本部分包含 3 个适用于 n8n 的 Discord 自动化模板。构建一个 AI 驱动的 Discord 机器人，将消息路由至对应部门；自动翻译并每日发布漫画；或将 YouTube 视频与 AI 生成的摘要直接分享至你的 Discord 服务器。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| Discord AI 驱动机器人 | 该工作流创建一个 AI 驱动的 Discord 机器人，对用户消息进行分类（成功案例、紧急问题、工单），并将其路由至相应部门（客户成功、IT、客服）。 | 客服/支持 | [模板链接](Discord/Discord%20AI-powered%20bot.json) |
| 每日向 Discord 发送翻译后的 Calvin and Hobbes 漫画 | 该工作流自动抓取 Calvin and Hobbes 漫画，将对话翻译成英文和韩文（或其他语言），并发布到 Discord。 | 市场/内容 | [模板链接](Discord/Send%20daily%20translated%20Calvin%20and%20Hobbes%20Comics%20to%20Discord.json) |
| 在 Discord 分享带有 AI 摘要的 YouTube 视频 | 该工作流自动将新发布的 YouTube 视频分享至 Discord，并附带利用字幕数据生成的 AI 内容摘要。 | 市场/营销 | [模板链接](Discord/Share%20YouTube%20Videos%20with%20AI%20Summaries%20on%20Discord.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 数据库与存储有哪些最佳的 n8n 自动化模板？

找到 5 个适用于 n8n 的数据库与存储自动化模板。使用自然语言对话 PostgreSQL、利用 AI 根据 Schema 生成 SQL 查询、从 MongoDB 获取智能电影推荐、管理 Supabase 向量嵌入，或通过 LangChain AI Agent 查询 SQLite 数据库。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 对话 PostgreSQL 数据库 | 该工作流使 AI 助手能够与 PostgreSQL 数据库交互，允许用户使用自然语言查询和检索数据。支持自定义 SQL 查询和 Schema 自省。 | 数据分析 | [模板链接](Database_and_Storage/Chat%20with%20Postgresql%20Database.json) |
| 仅凭 Schema 生成 SQL 查询 - AI 驱动 | 该工作流利用 AI 根据给定的数据库 Schema 自动生成 SQL 查询，降低手动编写查询语句的难度。 | 工程 | [模板链接](Database_and_Storage/Generate%20SQL%20queries%20from%20schema%20only%20-%20AI-powered.json) |
| MongoDB AI Agent - 智能电影推荐 | 该工作流创建一个 AI Agent，通过与 MongoDB 数据库交互提供智能电影推荐，利用聚合管道获取相关电影数据。 | 数据分析 | [模板链接](Database_and_Storage/MongoDB%20AI%20Agent%20-%20Intelligent%20Movie%20Recommendations.json) |
| Supabase 插入、Upsertion 与检索 | 该工作流演示如何对 Supabase 执行插入（Insert）、更新或插入（Upsert）及检索操作，特别适用于处理向量嵌入及相关元数据。 | 工程 | [模板链接](Database_and_Storage/Supabase%20Insertion%20&%20Upsertion%20&%20Retrieval.json) |
| 通过 LangChain AI Agent 对话 SQLite 数据库 | 该工作流允许用户使用 LangChain AI Agent 与 SQLite 数据库交互，实现自然语言查询和数据检索。 | 数据分析 | [模板链接](Database_and_Storage/Talk%20to%20your%20SQLite%20database%20with%20a%20LangChain%20AI%20Agent.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### DevOps 和服务器自动化有哪些 n8n 模板？

本部分包含 2 个适用于 n8n 的 DevOps 与服务器自动化模板。通过 SSH 上的认证 Webhook 触发 Linux 系统更新，或通过 HTTP POST 请求远程控制 Docker Compose 服务。两个模板均使用 SSH 进行安全的服务器管理。

| 标题 | 描述 | 链接 |
|-------|-------------|------|
| 通过 Webhook 更新 Linux 系统 | 通过认证的 POST 请求和 SSH 触发基于 Debian 的服务器的更新与升级操作。 | SSH Tools | [模板链接](devops/linux-update-via-webhook.json) |
| 通过 Webhook 控制 Docker Compose | 通过 n8n + SSH 发送认证的 HTTP POST 请求，在服务器上启动或停止 Docker Compose 服务。 | SSH Tools | [模板链接](devops/docker-compose-controller.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 如何使用 n8n 自动化 Airtable？

浏览 5 个适用于 n8n 的 Airtable 自动化模板。利用 Fireflies 会议转录记录自动化项目管理与跟进、通过 AI Agent 对话 Airtable 数据、集成 Obsidian Notes、使用 AI 驱动简历解析处理求职申请，或连接 HubSpot Chat 与 OpenAI 和 Airtable 以优化客服流程。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 结合 Airtable 与 Fireflies 的项目管理与会议 AI Agent | 该工作流利用 AI Agent 自动化项目管理任务与会议跟进，通过分析 Fireflies 通话转录记录创建 Airtable 任务并通知客户。 | 运营 | [模板链接](Airtable/AI%20Agent%20for%20project%20management%20and%20meetings%20with%20Airtable%20and%20Fireflies.json) |
| 用于对话 Airtable 与分析数据的 AI Agent | 该工作流创建一个可对话 Airtable、分析数据并根据用户需求执行查询的 AI Agent。支持聚合函数计算并生成图表/图片。 | 数据分析 | [模板链接](Airtable/AI%20Agent%20to%20chat%20with%20Airtable%20and%20analyze%20data.json) |
| 通过 AI 和 Obsidian Notes 获取 Airtable 数据 | 该工作流利用 AI Agent 从 Airtable 检索数据，并与 Obsidian Notes 集成，实现在 Obsidian 内无缝访问与组织数据。 | 效率工具 | [模板链接](Airtable/Get%20Airtable%20data%20via%20AI%20and%20Obsidian%20Notes.json) |
| 结合 AI 和 n8n Forms 处理求职申请提交 | 该工作流自动化处理求职申请，利用 AI 从简历（PDF）中提取信息并解析为结构化格式，可选择性存储至 Airtable。 | 人力资源/HR | [模板链接](Airtable/Handling%20Job%20Application%20Submissions%20with%20AI%20and%20n8n%20Forms.json) |
| 结合 OpenAi 和 Airtable 的 Hubspot Chat vAssistant | 该工作流将 OpenAI Assistant 与 HubSpot Chat 及 Airtable 集成，提供自动化回复并管理客户交互。获取聊天消息、利用 AI 处理，并将相关信息存储至 Airtable。 | 销售 | [模板链接](Airtable/vAssistant%20for%20Hubspot%20Chat%20using%20OpenAi%20and%20Airtable.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### Notion 有哪些最佳的 n8n 模板？

探索 10 个适用于 n8n 的 Notion 自动化模板。结合情感分析将 Typeform 正面反馈存入表格、利用 AI 分析 Hugging Face 研究论文、通过 AI Agent 执行竞品调研、自动化 LinkedIn 外联、为 Notion 数据库构建自定义 AI Assistant、创建知识库聊天机器人，并集成 Pinecone 与 Supabase 向量库。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 将正面反馈消息添加至 Notion 表格 | 捕获 Typeform 中的正面反馈，利用 Google Cloud Natural Language 分析情感得分，并将高分评价存入 Notion 表格，同时触发 Slack 通知。 | 客服/支持 | [模板链接](Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20Notion.json) |
| 使用 AI 分析 Hugging Face 论文并存储至 Notion | 自动抓取并分析来自 Hugging Face 的论文，利用 AI 提取关键信息，并将结构化数据存入 Notion 数据库。 | 工程 | [模板链接](Notion/Analyse%20papers%20from%20Hugging%20Face%20with%20AI%20and%20store%20them%20in%20Notion.json) |
| 结合 Exa.ai、Notion 与 AI Agent 自动化竞品调研 | 利用 Exa.ai 构建竞品调研 Agent 寻找相似公司。随后通过互联网搜集公司概况、产品功能与客户评价，最终将报告汇总至 Notion 表格。 | 市场/营销 | [模板链接](Notion/Automate%20Competitor%20Research%20with%20Exa.ai,%20Notion%20and%20AI%20Agents.json) |
| 结合 Notion 与 OpenAI 自动化 LinkedIn 外联 | 自动从 Notion 数据库抓取每日帖子，利用 OpenAI 格式化以适配 LinkedIn 互动风格，并发布至平台。 | 市场/营销 | [模板链接](Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json) |
| Notion AI Assistant Generator | 为特定的 Notion 数据库 Schema 生成自定义 AI Assistant 聊天机器人工作流，允许用户直接对话其 Notion 数据。 | 工程 | [模板链接](Notion/Notion%20AI%20Assistant%20Generator.json) |
| Notion 知识库 AI 助手 | 创建一个可搜索并检索 Notion 知识库信息的 AI Assistant，为用户提供精准问答服务。 | 客服/支持 | [模板链接](Notion/Notion%20knowledge%20base%20AI%20assistant.json) |
| Notion 至 Pinecone 向量库集成 | 将 Notion 与 Pinecone 集成，允许将 Notion 页面转换为向量嵌入并存储于 Pinecone，以支持高级搜索与检索。 | 工程 | [模板链接](Notion/Notion%20to%20Pinecone%20Vector%20Store%20Integration.json) |
| 使用 OpenAI 将 Notion 页面作为向量文档存储至 Supabase | 自动化将 Notion 页面作为向量文档存入 Supabase 数据库，利用 OpenAI 为内容生成 Embeddings。 | 工程 | [模板链接](Notion/Store%20Notion_s%20Pages%20as%20Vector%20Documents%20into%20Supabase%20with%20OpenAI.json) |
| 结合 Gmail、Airtable 和 Softr 将邮件转化为 Notion AI 增强任务（支持多用户） | 将邮件转换为 Notion 中的 AI 增强任务，支持多用户协作。集成 Gmail 作为触发器，Airtable 进行路由分发，Softr 提供用户界面。 | 运营 | [模板链接](Notion/Turn%20Emails%20into%20AI-Enhanced%20Tasks%20in%20Notion%20(Multi-User%20Support)%20with%20Gmail,%20Airtable%20and%20Softr.json) |
| 结合 Supabase 和 Notion 在向量库中 Upsert 海量文档 | 管理大型文档，将其分块生成 Embeddings，并 Upsert 至 Supabase 向量库，Notion 作为文档源。 | 工程 | [模板链接](Notion/Upsert%20huge%20documents%20in%20a%20vector%20store%20with%20Supabase%20and%20Notion.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 如何使用 n8n 自动化 Slack？

探索 9 个适用于 n8n 的 Slack 自动化模板。利用 AI 摘要监控 RSS 订阅源、使用 Google Gemini 构建 Slack Bot、通过 Linear 自动化客服工单系统、结合 Qualys 增强安全运营、丰富 Pipedrive CRM 数据、创建 IT 知识库聊天机器人、跟踪支持问题的情感倾向，以及通过 Venafi Cloud 管理证书。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| 结合 OpenAI、Google Sheets、Jina AI 和 Slack 的 AI 信息监控 | 监控 RSS 订阅源，利用 OpenAI 与 Jina AI 摘要文章并进行分类，随后将格式化通知发送至 Slack，实现 AI 驱动的信息监控。 | 市场/营销 | [模板链接](Slack/AI-Powered%20Information%20Monitoring%20with%20OpenAI,%20Google%20Sheets,%20Jina%20AI%20and%20Slack.json) |
| 使用 Google Gemini 创建 AI Slack Bot | 构建基于 Google Gemini 的 AI Slack Bot，处理 Webhook、集成 AI Agent、管理对话记忆并响应 Slack 消息。 | 工程 | [模板链接](Slack/Creating%20a%20AI%20Slack%20Bot%20with%20Google%20Gemini.json) |
| 结合 Slack 和 Linear 的客服频道与工单系统 | 自动化客服流程：查询带有工单表情的 Slack 消息，判断是否需要新建 Linear 工单，创建或更新工单并通知 Slack。 | 客服/支持 | [模板链接](Slack/Customer%20Support%20Channel%20and%20Ticketing%20System%20with%20Slack%20and%20Linear.json) |
| 结合 Qualys Slack Shortcut Bot 增强安全运营！ | 为 Qualys 创建 Slack 快捷命令机器人以增强安全运营，允许用户直接从 Slack 触发生成报告或启动漏洞扫描等操作。 | 安全 | [模板链接](Slack/Enhance%20Security%20Operations%20with%20the%20Qualys%20Slack%20Shortcut%20Bot!.json) |
| 结合 OpenAI GPT-4o 丰富 Pipedrive 组织数据并通知 Slack | 通过抓取网站内容丰富 Pipedrive 组织数据，利用 OpenAI GPT-4o 生成摘要并作为备注添加至 Pipedrive，随后向指定 Slack 频道发送通知。 | 销售 | [模板链接](Slack/Enrich%20Pipedrive_s%20Organization%20Data%20with%20OpenAI%20GPT-4o%20&%20Notify%20it%20in%20Slack.json) |
| IT Ops AI SlackBot 工作流 - 对话你的知识库 | 为 IT 运维创建 AI SlackBot，允许用户直接与知识库交互以检索信息并获取答案。 | IT | [模板链接](Slack/IT%20Ops%20AI%20SlackBot%20Workflow%20-%20Chat%20with%20your%20knowledge%20base.json) |
| 结合 Linear 和 Slack 跟踪支持问题的情感分析 | 集成 Linear 与 Slack，利用 OpenAI 对 Linear 评论进行情感分析，并将结果通知相关 Slack 频道。 | 客服/支持 | [模板链接](Slack/Sentiment%20Analysis%20Tracking%20on%20Support%20Issues%20with%20Linear%20and%20Slack.json) |
| Slack Slash Commands AI Chat Bot | 实现通过 Slack Slash Commands 调用的 AI 聊天机器人，处理用户命令、与 AI 模型交互并在 Slack 内返回回复。 | IT | [模板链接](Slack/Slack%20slash%20commands%20AI%20Chat%20Bot.json) |
| Venafi Cloud Slack Cert Bot | 提供一款 Slack Bot，用于与 Venafi Cloud 进行证书管理交互，允许用户检查证书状态、接收警报或通过 Slack 请求执行证书操作。 | 安全 | [模板链接](Slack/Venafi%20Cloud%20Slack%20Cert%20Bot.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### OpenAI、LLM 和 AI Agent 有哪些 n8n 模板？

这是最大的分类，包含 17 个适用于 n8n 的 AI 与 LLM 模板。涵盖高级 AI Agent 演示、网页抓取 Agent、股票分析 Crews、客户反馈情感分析、结合 ERPNext 的 AI 潜在客户管理、基于 Strava 的健身指导、HR 候选人初筛、邮件与财报 RAG 流水线、社交媒体放大工具、WooCommerce 客服 Agent、YouTube 视频摘要，以及结合维基百科播客增强等功能。

| 标题 | 描述 | 适用团队 | 链接 |
|---|---|---|---|
| Advanced AI Demo（于 AI Developers #14 研讨会展示） | 高级 AI 能力演示工作流。 | AI/开发 | [模板链接](OpenAI_and_LLMs/Advanced%20AI%20Demo%20(Presented%20at%20AI%20Developers%20%2314%20meetup).json) |
| AI agent chat | 基础型 AI 对话 Agent。 | AI/客服 | [模板链接](OpenAI_and_LLMs/AI%20agent%20chat.json) |
| AI agent that can scrape webpages | 用于网页抓取的 AI Agent。 | AI/数据提取 | [模板链接](OpenAI_and_LLMs/AI%20agent%20that%20can%20scrape%20webpages.json) |
| AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow | 股票分析自动化工作流。 | 金融/AI/数据分析 | [模板链接](OpenAI_and_LLMs/AI%20Crew%20to%20Automate%20Fundamental%20Stock%20Analysis%20-%20Q&A%20Workflow.json) |
| AI Customer feedback sentiment analysis | 客户反馈情感分析。 | 客服/市场/数据分析 | [模板链接](OpenAI_and_LLMs/AI%20Customer%20feedback%20sentiment%20analysis.json) |
| AI Data Extraction with Dynamic Prompts and Airtable | 结合动态 Prompt 与 Airtable 的 AI 数据提取。 | AI/数据提取/数据库 | [模板链接](OpenAI_and_LLMs/AI%20Data%20Extraction%20with%20Dynamic%20Prompts%20and%20Airtable.json) |
| AI Data Extraction with Dynamic Prompts and Baserow | 结合动态 Prompt 与 Baserow 的 AI 数据提取。 | AI/数据提取/数据库 | [模板链接](OpenAI_and_LLMs/AI%20Data%20Extraction%20with%20Dynamic%20Prompts%20and%20Baserow.json) |
| AI-Driven Lead Management and Inquiry Automation with ERPNext & n8n | 潜在客户管理自动化。 | 销售/CRM/AI | [模板链接](OpenAI_and_LLMs/AI-Driven%20Lead%20Management%20and%20Inquiry%20Automation%20with%20ERPNext%20&%20n8n.json) |
| AI Fitness Coach Strava Data Analysis and Personalized Training Insights | 基于 Strava 数据分析的健身指导。 | 健身/AI/数据分析 | [模板链接](OpenAI_and_LLMs/AI%20Fitness%20Coach%20Strava%20Data%20Analysis%20and%20Personalized%20Training%20Insights.json) |
| AI-Powered Candidate Shortlisting Automation for ERPNext | 候选人初筛自动化。 | HR/AI/招聘 | [模板链接](OpenAI_and_LLMs/AI-Powered%20Candidate%20Shortlisting%20Automation%20for%20ERPNext.json) |
| AI-Powered Email Automation for Business: Summarize & Respond with RAG | 结合摘要与回复的邮件自动化。 | 业务自动化/AI/通信 | [模板链接](OpenAI_and_LLMs/AI-Powered%20Email%20Automation%20for%20Business_%20Summarize%20&%20Respond%20with%20RAG.json) |
| AI-Powered RAG Workflow For Stock Earnings Report Analysis | 结合 RAG 的股票财报分析。 | 金融/AI/数据分析 | [模板链接](OpenAI_and_LLMs/AI-Powered%20RAG%20Workflow%20For%20Stock%20Earnings%20Report%20Analysis.json) |
| AI-Powered Social Media Amplifier | 利用 AI 放大社交媒体影响力。 | 市场/AI/社交媒体 | [模板链接](OpenAI_and_LLMs/AI-Powered%20Social%20Media%20Amplifier.json) |
| AI-powered WooCommerce Support-Agent | 为 WooCommerce 商店创建 AI 驱动的客服 Agent。 | 电商/AI/客服 | [模板链接](OpenAI_and_LLMs/AI-powered%20WooCommerce%20Support-Agent.json) |
| AI-Powered YouTube Video Summarization & Analysis | 利用 AI 摘要与分析 YouTube 视频内容。 | 内容创作/AI/数据分析 | [模板链接](OpenAI_and_LLMs/%E2%9A%A1AI-Powered%20YouTube%20Video%20Summarization%20&%20Analysis.json) |
| AI: Ask questions about any data source (using the n8n workflow retriever) | 允许用户通过 n8n 工作流检索器向各类数据源提问。 | AI/数据分析/工作流自动化 | [模板链接](OpenAI_and_LLMs/AI_%20Ask%20questions%20about%20any%20data%20source%20(using%20the%20n8n%20workflow%20retriever).json) |
| AI: Summarize podcast episode and enhance using Wikipedia | 利用 AI 摘要播客节目，并结合维基百科信息增强内容。 | 内容创作/AI/数据分析 | [模板链接](OpenAI_and_LLMs/AI_%20Summarize%20podcast%20episode%20and%20enhance%20using%20Wikipedia.json) |
| AI Blog Writer Pipeline with Ollama | 使用 Ollama 本地 AI 研究主题、创建大纲、撰写完整博客文章并进行编辑。完全在本地运行，无需 API Key。 | 内容创作/AI | [模板链接](OpenAI_and_LLMs/AI%20Blog%20Writer%20Pipeline%20with%20Ollama.json) |
| SupportFlow Lite - Simple AI Customer Support Chatbot | 轻量级 AI 聊天机器人，利用公司信息与 OpenAI gpt-4o-mini 回答客户问题。采用单工作流架构并集成 Google Sheets 知识库，易于部署。 | 客服/AI | [模板链接](OpenAI_and_LLMs/SupportFlow%20Lite%20-%20Simple%20AI%20Customer%20Support%20Chatbot.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 如何使用 n8n 构建 WhatsApp 聊天机器人？

本部分包含 4 个适用于 n8n 的 WhatsApp 自动化模板。利用 AI 和 Apify 自动化销售会议准备、搭建你的第一个 WhatsApp 聊天机器人、结合 OpenAI 打造企业级 RAG 聊天机器人，或设置专业的 AI 消息回复流程。非常适合客服、销售及商务沟通工作流。

| 标题 | 描述 | 适用团队 | 链接 |
|---|---|---|---|
| 利用 AI & APIFY 自动化销售会议准备并发送至 WhatsApp | 该工作流结合 AI 与 Apify 自动化销售会议准备工作，并将相关信息推送至 WhatsApp。 | 销售/AI/自动化 | [模板链接](./WhatsApp/Automate%20Sales%20Meeting%20Prep%20with%20AI%20&%20APIFY%20Sent%20To%20WhatsApp.json) |
| Building Your First WhatsApp Chatbot | 该工作流引导你完成第一个 WhatsApp 聊天机器人的搭建过程。 | 客服/开发 | [模板链接](./WhatsApp/Building%20Your%20First%20WhatsApp%20Chatbot.json) |
| Complete business WhatsApp AI-Powered RAG Chatbot using OpenAI | 该工作流利用 OpenAI 构建完整的业务级 WhatsApp AI 驱动 RAG 聊天机器人。 | 客服/AI/开发 | [模板链接](./WhatsApp/Complete%20business%20WhatsApp%20AI-Powered%20RAG%20Chatbot%20using%20OpenAI.json) |
| Respond to WhatsApp Messages with AI Like a Pro! | 该工作流实现专业的 AI 驱动 WhatsApp 消息回复功能。 | 客服/AI/通信 | [模板链接](./WhatsApp/Respond%20to%20WhatsApp%20Messages%20with%20AI%20Like%20a%20Pro!.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### Instagram、Twitter 和社交媒体有哪些最佳的 n8n 模板？

探索 10 个适用于 n8n 的社交媒体自动化模板，覆盖 Instagram、Twitter/X、Reddit、YouTube、LinkedIn 等平台。包含结合 Manychat 的 AI 驱动 Instagram DM 管理、动态 Twitter Banner、基于趋势的 AI 图像内容生成、推文生成器、YouTube 转 X 发布、Reddit 摘要创建、社媒数据分析及虚拟 AI 网红管理等模板。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| Instagram DM_inbox AI agent. Manychat + Open AI integration | 集成 Manychat 与 OpenAI，创建用于管理 Instagram 私聊的 AI Agent。 | 市场/客服/AI | [模板链接](Instagram_Twitter_Social_Media/AI%20agent%20for%20Instagram%20DM_inbox.%20Manychat%20%2B%20Open%20AI%20integration.json) |
| Create dynamic Twitter profile banner | 自动化创建动态 Twitter 个人主页 Banner。 | 市场/社交媒体 | [模板链接](Instagram_Twitter_Social_Media/Create%20dynamic%20Twitter%20profile%20banner.json) |
| Generate Instagram Content from Top Trends with AI Image Generation | 分析热门趋势并利用 AI 生成相关图像，用于创作 Instagram 内容。 | 市场/AI/内容 | [模板链接](Instagram_Twitter_Social_Media/Generate%20Instagram%20Content%20from%20Top%20Trends%20with%20AI%20Image%20Generation.json) |
| OpenAI-powered tweet generator | 利用 OpenAI 语言模型生成推文。 | 市场/社交媒体/AI | [模板链接](Instagram_Twitter_Social_Media/OpenAI-powered%20tweet%20generator.json) |
| Post New YouTube Videos to X | 自动将新发布的 YouTube 视频发布至 X（原 Twitter）。 | 市场/社交媒体 | [模板链接](Instagram_Twitter_Social_Media/Post%20New%20YouTube%20Videos%20to%20X.json) |
| Reddit AI digest | 利用 AI 生成 Reddit 内容摘要。 | 市场/内容/AI | [模板链接](Instagram_Twitter_Social_Media/Reddit%20AI%20digest.json) |
| Social Media Analysis and Automated Email Generation | 分析社交媒体数据并自动生成邮件报告。 | 市场/数据分析 | [模板链接](Instagram_Twitter_Social_Media/Social%20Media%20Analysis%20and%20Automated%20Email%20Generation.json) |
| Speed Up Social Media Banners With BannerBear.com | 利用 BannerBear.com 自动化创建社交媒体 Banner。 | 市场/设计 | [模板链接](Instagram_Twitter_Social_Media/Speed%20Up%20Social%20Media%20Banners%20With%20BannerBear.com.json) |
| Twitter Virtual AI Influencer | 管理虚拟 AI 网红的 Twitter 账号。 | 市场/AI | [模板链接](Instagram_Twitter_Social_Media/Twitter%20Virtual%20AI%20Influencer.json) |
| Update Twitter banner using HTTP request | 通过 HTTP 请求更新 Twitter Banner。 | 市场/开发 | [模板链接](Instagram_Twitter_Social_Media/Update%20Twitter%20banner%20using%20HTTP%20request.json) |
| AI Social Media Content Generator with Ollama | 使用 Ollama 本地 AI，基于单一主题生成优化后的 Twitter、LinkedIn、Reddit 和 Instagram 帖子，内置质量审查机制。 | 市场/AI/内容 | [模板链接](Instagram_Twitter_Social_Media/AI%20Social%20Media%20Content%20Generator%20with%20Ollama.json) |
| FlowScribe Lite - AI Content Repurposing (4 Platforms) | 利用 OpenAI 将一篇博客文章自动转化为适配 Twitter、LinkedIn、Instagram 和 Facebook 的 4 篇优化社媒帖子。 | 市场/内容 | [模板链接](Instagram_Twitter_Social_Media/FlowScribe%20Lite%20-%20AI%20Content%20Repurposing%204%20Platforms.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 还有哪些其他可用的 n8n 集成模板？

本部分包含 28 个额外的 n8n 集成模板，覆盖广泛的平台与用例。亮点包括 API Schema 提取、结合 AI 的 Pinterest 分析、利用 MITRE ATT&CK 丰富 SIEM 警报、Bitrix24 聊天机器人、GitLab 代码审查（ChatGPT）、LINE 助手集成、Spotify 歌单归档、Zoom 会议 AI Assistant、通过 Apple Shortcuts 调用 Siri AI Agent，以及 Todoist 收件箱整理等。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| API Schema Extractor | 从 Web 服务中提取 API Schema，用于文档编写或系统集成。 | 开发/集成 | [模板链接](Other_Integrations_and_Use_Cases/API%20Schema%20Extractor.json) |
| Analyze feedback and send a message on Mattermost | 分析用户反馈并将通知发送至 Mattermost 频道。 | 客服/通信 | [模板链接](Other_Integrations_and_Use_Cases/Analyze%20feedback%20and%20send%20a%20message%20on%20Mattermost.json) |
| Analyze feedback using AWS Comprehend and send it to a Mattermost channel | 使用 AWS Comprehend 对反馈进行情感分析，并将结果发送至 Mattermost。 | 客服/AI | [模板链接](Other_Integrations_and_Use_Cases/Analyze%20feedback%20using%20AWS%20Comprehend%20and%20send%20it%20to%20a%20Mattermost%20channel.json) |
| Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API | 分析 Pinterest 数据并提供 AI 驱动的内容建议。 | 市场/AI | [模板链接](Other_Integrations_and_Use_Cases/Automate%20Pinterest%20Analysis%20&%20AI-Powered%20Content%20Suggestions%20With%20Pinterest%20API.json) |
| Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n | 结合 MITRE ATT&CK 数据丰富 SIEM 警报，并集成至 Zendesk。 | 安全/IT | [模板链接](Other_Integrations_and_Use_Cases/Automate%20SIEM%20Alert%20Enrichment%20with%20MITRE%20ATT&CK,%20Qdrant%20&%20Zendesk%20in%20n8n.json) |
| Automate Screenshots with URLbox & Analyze them with AI | 截取网页截图并利用 AI 进行分析。 | 开发/市场 | [模板链接](Other_Integrations_and_Use_Cases/Automate%20Screenshots%20with%20URLbox%20&%20Analyze%20them%20with%20AI.json) |
| Automate testimonials in Strapi with n8n | 自动化在 Strapi 中收集与管理用户证言的流程。 | 市场/内容 | [模板链接](Other_Integrations_and_Use_Cases/Automate%20testimonials%20in%20Strapi%20with%20n8n.json) |
| Bitrix24 Chatbot Application Workflow example with Webhook Integration | 结合 Webhook 集成创建 Bitrix24 聊天机器人的示例工作流。 | 商务/通信 | [模板链接](Other_Integrations_and_Use_Cases/Bitrix24%20Chatbot%20Application%20Workflow%20example%20with%20Webhook%20Integration.json) |
| ChatGPT Automatic Code Review in Gitlab MR | 利用 ChatGPT 自动化 GitLab Merge Request 中的代码审查。 | 开发/DevOps | [模板链接](Other_Integrations_and_Use_Cases/ChatGPT%20Automatic%20Code%20Review%20in%20Gitlab%20MR.json) |
| Classify new bugs in Linear with OpenAI_s GPT-4 and move them to the right team | 利用 AI 自动分类并路由至对应团队的 Linear 新 Bug 报告。 | 开发/QA | [模板链接](Other_Integrations_and_Use_Cases/Classify%20new%20bugs%20in%20Linear%20with%20OpenAI_s%20GPT-4%20and%20move%20them%20to%20the%20right%20team.json) |
| Create, update, and get a profile in Humantic AI | 管理 Humantic AI 平台上的用户档案。 | 市场/AI | [模板链接](Other_Integrations_and_Use_Cases/Create,%20update,%20and%20get%20a%20profile%20in%20Humantic%20AI.json) |
| Enhance Customer Chat by Buffering Messages with Twilio and Redis | 结合 Twilio 与 Redis 实现客户聊天消息的缓冲处理。 | 客服/开发 | [模板链接](Other_Integrations_and_Use_Cases/Enhance%20Customer%20Chat%20by%20Buffering%20Messages%20with%20Twilio%20and%20Redis.json) |
| Hacker News Throwback Machine - See What Was Hot on This Day, Every Year! | 展示往年今日在 Hacker News 上热门的内容。 | 开发/社区 | [模板链接](Other_Integrations_and_Use_Cases/Hacker%20News%20Throwback%20Machine%20-%20See%20What%20Was%20Hot%20on%20This%20Day,%20Every%20Year!.json) |
| Handling Appointment Leads and Follow-up With Twilio, Cal.com and AI | 结合 Twilio 与 Cal.com 管理预约线索及后续跟进。 | 销售/客服 | [模板链接](Other_Integrations_and_Use_Cases/Handling%20Appointment%20Leads%20and%20Follow-up%20With%20Twilio,%20Cal.com%20and%20AI.json) |
| Integrating AI with Open-Meteo API for Enhanced Weather Forecasting | 结合 AI 分析增强天气预报能力。 | 数据科学/气象 | [模板链接](Other_Integrations_and_Use_Cases/Integrating%20AI%20with%20Open-Meteo%20API%20for%20Enhanced%20Weather%20Forecasting.json) |
| Introduction to the HTTP Tool | n8n 中 HTTP 工具的基础教程。 | 开发 | [模板链接](Other_Integrations_and_Use_Cases/Introduction%20to%20the%20HTTP%20Tool.json) |
| KB Tool - Confluence Knowledge Base | 集成 Confluence 进行知识库管理。 | 文档/IT | [模板链接](Other_Integrations_and_Use_Cases/KB%20Tool%20-%20Confluence%20Knowledge%20Base.json) |
| Komos Regulated Browser Ops Task Queue | 从 n8n 队列化执行 [Komos](https://www.komos.ai/) 浏览器自动化任务，适用于 CRA、银行或保险门户操作，附带审计就绪的运行元数据。 | 运营/合规 | [模板链接](Other_Integrations_and_Use_Cases/Komos%20Regulated%20Browser%20Ops%20Task%20Queue.json) |
| LINE Assistant with Google Calendar and Gmail Integration | 创建集成 Google Calendar 与 Gmail 的 LINE 助手。 | 效率工具/通信 | [模板链接](Other_Integrations_and_Use_Cases/LINE%20Assistant%20with%20Google%20Calendar%20and%20Gmail%20Integration.json) |
| Monthly Spotify Track Archiving and Playlist Classification | 归档并分类每月的 Spotify 曲目至播放列表。 | 个人/音乐 | [模板链接](Other_Integrations_and_Use_Cases/Monthly%20Spotify%20Track%20Archiving%20and%20Playlist%20Classification.json) |
| Obsidian Notes Read Aloud using AI - Available as a Podcast Feed | 将 Obsidian 笔记转换为音频格式，并提供播客订阅源。 | 效率工具/内容 | [模板链接](Other_Integrations_and_Use_Cases/Obsidian%20Notes%20Read%20Aloud%20using%20AI_%20Available%20as%20a%20Podcast%20Feed.json) |
| Optimize & Update Printify Title and Description Workflow | 自动化优化 Printify 产品标题与描述。 | 电商 | [模板链接](Other_Integrations_and_Use_Cases/Optimize%20&%20Update%20Printify%20Title%20and%20Description%20Workflow.json) |
| Qualify replies from Pipedrive persons with AI | 利用 AI 对来自 Pipedrive 联系人的回复进行筛选与分类。 | 销售/AI | [模板链接](Other_Integrations_and_Use_Cases/Qualify%20replies%20from%20Pipedrive%20persons%20with%20AI.json) |
| Siri AI Agent - Apple Shortcuts powered voice template | 结合 Apple Shortcuts 创建由 Siri 驱动的 AI Agent。 | 个人/效率工具 | [模板链接](Other_Integrations_and_Use_Cases/Siri%20AI%20Agent_%20Apple%20Shortcuts%20powered%20voice%20template.json) |
| Text automations using Apple Shortcuts | 利用 Apple Shortcuts 实现文本自动化。 | 个人/效率工具 | [模板链接](Other_Integrations_and_Use_Cases/Text%20automations%20using%20Apple%20Shortcuts.json) |
| UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports | 创建 UTM 链接、生成二维码，并定时调度 Google Analytics 报告。 | 市场/数据分析 | [模板链接](Other_Integrations_and_Use_Cases/UTM%20Link%20Creator%20&%20QR%20Code%20Generator%20with%20Scheduled%20Google%20Analytics%20Reports.json) |
| Use AI to organize your Todoist Inbox | 利用 AI 自动整理 Todoist 收件箱中的任务。 | 效率工具 | [模板链接](Other_Integrations_and_Use_Cases/Use%20AI%20to%20organize%20your%20Todoist%20Inbox.json) |
| Using External Workflows as Tools in n8n | 演示如何在 n8n 内部将外部工作流作为工具调用。 | 开发 | [模板链接](Other_Integrations_and_Use_Cases/Using%20External%20Workflows%20as%20Tools%20in%20n8n.json) |
| Visualize your SQL Agent queries with OpenAI and Quickchart.io | 结合 OpenAI 与 Quickchart.io 将 SQL Agent 查询结果可视化。 | 数据分析/可视化 | [模板链接](Other_Integrations_and_Use_Cases/Visualize%20your%20SQL%20Agent%20queries%20with%20OpenAI%20and%20Quickchart.io.json) |
| Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call | 结合 Zoom 会议生成邮件摘要、ClickUp 任务并安排后续跟进通话。 | 效率工具/通信 | [模板链接](Other_Integrations_and_Use_Cases/Zoom%20AI%20Meeting%20Assistant%20creates%20mail%20summary,%20ClickUp%20tasks%20and%20follow-up%20call.json) |
| ClientFlow Lite - Client Onboarding Automation | 客户提交表单后自动发送欢迎邮件，并加入 Google Sheets 跟进流水线。轻量级入职工作流。 | 运营/销售 | [模板链接](Other_Integrations_and_Use_Cases/ClientFlow%20Lite%20-%20Client%20Onboarding%20Automation.json) |
| VoiceAgent Lite - Phone Call Logger | 通过 Webhook 将 Vapi.ai 或 Bland.ai 的通话记录日志至 Google Sheets。捕获主叫信息、时长及对话摘要。 | 运营/客服 | [模板链接](Other_Integrations_and_Use_Cases/VoiceAgent%20Lite%20-%20Phone%20Call%20Logger.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 如何使用 n8n 自动化表单与调查？

本部分包含 3 个适用于 n8n 的表单与调查自动化模板。通过 n8n Forms 进行 AI 驱动的对话式访谈、结合 Airtable 管理邮件订阅，或利用 AI 筛选预约请求。这些模板可简化数据收集与潜在客户处理流程。

| 标题 | 描述 | 适用团队 | 链接 |
|-------|-------------|------------|------|
| Conversational Interviews with AI Agents and n8n Forms | 利用 n8n Forms 实现 AI 驱动的对话式访谈，用于交互式数据收集。 | 研究/市场 | [模板链接](Forms_and_Surveys/Conversational%20Interviews%20with%20AI%20Agents%20and%20n8n%20Forms.json) |
| Email Subscription Service with n8n Forms, Airtable and AI | 结合 n8n Forms 管理邮件订阅，将数据存入 Airtable，并利用 AI 进行处理。 | 市场/通信 | [模板链接](Forms_and_Surveys/Email%20Subscription%20Service%20with%20n8n%20Forms,%20Airtable%20and%20AI.json) |
| Qualifying Appointment Requests with AI & n8n Forms | 利用 AI 筛选并处理通过 n8n Forms 提交的预约请求。 | 销售/客服 | [模板链接](Forms_and_Surveys/Qualifying%20Appointment%20Requests%20with%20AI%20&%20n8n%20Forms.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### AI 研究、RAG（检索增强生成）与数据分析有哪些 n8n 模板？

探索 39 个适用于 n8n 的 AI 研究、RAG 与数据分析模板——本合集中的最大分类。涵盖结合 Apify 和 OpenAI 的深度研究 Agent、自主网页爬虫、基于 Qdrant 和 Pinecone 的 RAG Chatbot、TradingView 图表分析、Hugging Face 论文摘要、金融文档助手、SEO 关键词生成、情感分析、视觉回归测试，以及用于异常检测与 KNN 分类的向量数据库分析等。

| 工作流标题 | 描述 | 适用团队 | 模板链接 |
|---|---|---|---|
| Analyze tradingview.com charts with Chrome extension, N8N and OpenAI | 结合 Chrome 扩展、n8n 与 OpenAI 自动化分析 TradingView 图表。 | 数据分析 | [Analyze tradingview.com charts with Chrome extension, N8N and OpenAI.txt](./AI_Research_RAG_and_Data_Analysis/Analyze%20tradingview.com%20charts%20with%20Chrome%20extension,%20N8N%20and%20OpenAI.json) |
| Automated Hugging Face Paper Summary Fetching & Categorization Workflow | 自动化抓取、摘要并分类来自 Hugging Face 的研究论文。 | AI 研究 | [Automated Hugging Face Paper Summary Fetching & Categorization Workflow.json](./AI_Research_RAG_and_Data_Analysis/Automated%20Hugging%20Face%20Paper%20Summary%20Fetching%20&%20Categorization%20Workflow.json) |
| Autonomous AI crawler | 用于数据采集与分析的自主 AI 网页爬虫。 | AI 研究 | [Autonomous AI crawler.json](./AI_Research_RAG_and_Data_Analysis/Autonomous%20AI%20crawler.json) |
| Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearchBuild Your Own Image Search Using AI Object Detection, CDN and ElasticSearch.txt | 结合 AI 目标检测、CDN 与 Elasticsearch 构建图像搜索引擎，实现高效检索。 | AI 研究 | [Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearchBuild Your Own Image Search Using AI Object Detection, CDN and ElasticSearch.json](./AI_Research_RAG_and_Data_Analysis/Build%20Your%20Own%20Image%20Search%20Using%20AI%20Object%20Detection,%20CDN%20and%20ElasticSearchBuild%20Your%20Own%20Image%20Search%20Using%20AI%20Object%20Detection,%20CDN%20and%20ElasticSearch.json) |
| Build a Financial Documents Assistant using Qdrant and Mistral.ai.txt | 结合 Qdrant（向量搜索）与 Mistral.ai（语言处理）构建金融文档 AI 助手。 | 金融/AI 研究 | [Build a Financial Documents Assistant using Qdrant and Mistral.ai.json](./AI_Research_RAG_and_Data_Analysis/Build%20a%20Financial%20Documents%20Assistant%20using%20Qdrant%20and%20Mistral.ai.json) |
| Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.txt | 结合 Qdrant、Mistral.ai 与 OpenAI 构建税务代码查询 AI 助手，提供全面解答。 | 金融/AI 研究 | [Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.json](./AI_Research_RAG_and_Data_Analysis/Build%20a%20Tax%20Code%20Assistant%20with%20Qdrant,%20Mistral.ai%20and%20OpenAI.json) |
| Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI.txt | 构建基于 RAG 的电影推荐聊天机器人，利用 Qdrant 进行检索，OpenAI 生成内容。 | AI 研究/娱乐 | [Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI.json](./AI_Research_RAG_and_Data_Analysis/Building%20RAG%20Chatbot%20for%20Movie%20Recommendations%20with%20Qdrant%20and%20Open%20AI.json) |
| Chat with GitHub API Documentation_ RAG-Powered Chatbot with Pinecone & OpenAI.txt | 结合 Pinecone 与 OpenAI 实现基于 RAG 的 GitHub API 文档对话机器人。 | 开发/AI 研究 | [Chat with GitHub API Documentation_ RAG-Powered Chatbot with Pinecone & OpenAI.json](./AI_Research_RAG_and_Data_Analysis/Chat%20with%20GitHub%20API%20Documentation_%20RAG-Powered%20Chatbot%20with%20Pinecone%20&%20OpenAI.json) |
| Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram.txt | 利用 AI 生成 Google Analytics 数据报告，并通过邮件与 Telegram 发送。 | 数据分析/市场 | [Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram.json](./AI_Research_RAG_and_Data_Analysis/Create%20a%20Google%20Analytics%20Data%20Report%20with%20AI%20and%20sent%20it%20to%20E-Mail%20and%20Telegram.json) |
| Customer Insights with Qdrant, Python and Information Extractor.txt | 结合 Qdrant、Python 与信息提取模块挖掘客户洞察。 | 数据分析/客服 | [Customer Insights with Qdrant, Python and Information Extractor.json](./AI_Research_RAG_and_Data_Analysis/Customer%20Insights%20with%20Qdrant,%20Python%20and%20Information%20Extractor.json) |
| Deduplicate Scraping AI Grants for Eligibility using AI.txt | 利用 AI 自动化去重与资格评估已抓取的 AI 资助数据。 | AI 研究/数据管理 | [Deduplicate Scraping AI Grants for Eligibility using AI.json](./AI_Research_RAG_and_Data_Analysis/Deduplicate%20Scraping%20AI%20Grants%20for%20Eligibility%20using%20AI.json) |
| Enrich Property Inventory Survey with Image Recognition and AI Agent.txt | 结合图像识别与 AI Agent 增强房产盘点调查，实现自动化数据丰富。 | 房地产/AI 研究 | [Enrich Property Inventory Survey with Image Recognition and AI Agent.json](./AI_Research_RAG_and_Data_Analysis/Enrich%20Property%20Inventory%20Survey%20with%20Image%20Recognition%20and%20AI%20Agent.json) |
| Extract insights & analyse YouTube comments via AI Agent chat.txt | 通过 AI Agent 聊天界面提取洞察并分析 YouTube 评论。 | 社交媒体/数据分析 | [Extract insights & analyse YouTube comments via AI Agent chat.json](./AI_Research_RAG_and_Data_Analysis/Extract%20insights%20&%20analyse%20YouTube%20comments%20via%20AI%20Agent%20chat.json) |
| Generate SEO Seed Keywords Using AI.txt | 利用 AI 生成 SEO 种子关键词，优化搜索引擎内容。 | 市场/AI 研究 | [Generate SEO Seed Keywords Using AI.json](./AI_Research_RAG_and_Data_Analysis/Generate%20SEO%20Seed%20Keywords%20Using%20AI.json) |
| Hacker News Job Listing Scraper and Parser.txt | 抓取并解析 Hacker News 上的职位列表，服务于求职者或招聘人员。 | 数据采集/HR | [Hacker News Job Listing Scraper and Parser.json](./AI_Research_RAG_and_Data_Analysis/Hacker%20News%20Job%20Listing%20Scraper%20and%20Parser.json) |
| Hacker News to Video Content.txt | 自动将 Hacker News 文章转换为视频内容。 | 内容创作/媒体 | [Hacker News to Video Content.json](./AI_Research_RAG_and_Data_Analysis/Hacker%20News%20to%20Video%20Content.json) |
| Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3.txt | 结合 n8n、Apify 与 OpenAI 搭建自托管的 AI 深度研究 Agent。 | AI 研究/自动化 | [Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3.json](./AI_Research_RAG_and_Data_Analysis/Host%20Your%20Own%20AI%20Deep%20Research%20Agent%20with%20n8n,%20Apify%20and%20OpenAI%20o3.json) |
| Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini.txt | 结合 Brave 浏览器与 Google Gemini AI 执行智能网页查询与语义重排序。 | AI 研究/数据分析 | [Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini.json](./AI_Research_RAG_and_Data_Analysis/Intelligent%20Web%20Query%20and%20Semantic%20Re-Ranking%20Flow%20using%20Brave%20and%20Google%20Gemini.json) |
| Learn Anything from HN - Get Top Resource Recommendations from Hacker News.txt | 从 Hacker News 提取顶级资源推荐，辅助用户学习任意主题。 | 教育/数据分析 | [Learn Anything from HN - Get Top Resource Recommendations from Hacker News.json](./AI_Research_RAG_and_Data_Analysis/Learn%20Anything%20from%20HN%20-%20Get%20Top%20Resource%20Recommendations%20from%20Hacker%20News.json) |
| Make OpenAI Citation for File Retrieval RAG.txt | 利用 OpenAI 为文件检索 RAG 系统生成引用来源。 | AI 研究/文档 | [Make OpenAI Citation for File Retrieval RAG.json](./AI_Research_RAG_and_Data_Analysis/Make%20OpenAI%20Citation%20for%20File%20Retrieval%20RAG.json) |
| Open Deep Research - AI-Powered Autonomous Research Workflow.txt | 用于执行深度研究的 AI 驱动自主工作流。 | AI 研究/自动化 | [Open Deep Research - AI-Powered Autonomous Research Workflow.json](./AI_Research_RAG_and_Data_Analysis/Open%20Deep%20Research%20-%20AI-Powered%20Autonomous%20Research%20Workflow.json) |
| Query Perplexity AI from your n8n workflows.txt | 将 Perplexity AI 集成至 n8n 工作流，实现高级查询能力。 | AI 研究/自动化 | [Query Perplexity AI from your n8n workflows.json](./AI_Research_RAG_and_Data_Analysis/Query%20Perplexity%20AI%20from%20your%20n8n%20workflows.json) |
| Recipe Recommendations with Qdrant and Mistral.txt | 结合 Qdrant（向量搜索）与 Mistral AI（内容生成）提供食谱推荐。 | 美食/AI 研究 | [Recipe Recommendations with Qdrant and Mistral.json](./AI_Research_RAG_and_Data_Analysis/Recipe%20Recommendations%20with%20Qdrant%20and%20Mistral.json) |
| Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI.txt | 结合本地 Excel 表格与 OpenAI 处理租金支付对账。 | 金融/数据管理 | [Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI.json](./AI_Research_RAG_and_Data_Analysis/Reconcile%20Rent%20Payments%20with%20Local%20Excel%20Spreadsheet%20and%20OpenAI.json) |
| Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI.txt | 使用 DeepSeek 抓取 Trustpilot 评论，并利用 OpenAI 进行情感分析。 | 市场/数据分析 | [Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI.json](./AI_Research_RAG_and_Data_Analysis/Scrape%20Trustpilot%20Reviews%20with%20DeepSeek,%20Analyze%20Sentiment%20with%20OpenAI.json) |
| Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB.txt | 利用 AI 抓取并摘要无 RSS 源的新站文章，将输出保存至 NocoDB。 | 内容策展/数据管理 | [Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB.json](./AI_Research_RAG_and_Data_Analysis/Scrape%20and%20summarize%20posts%20of%20a%20news%20site%20without%20RSS%20feed%20using%20AI%20and%20save%20them%20to%20a%20NocoDB.json) |
| Scrape and summarize webpages with AI.txt | 利用 AI 抓取并摘要网页内容。 | 内容策展/数据分析 | [Scrape and summarize webpages with AI.json](./AI_Research_RAG_and_Data_Analysis/Scrape%20and%20summarize%20webpages%20with%20AI.json) |
| Send Google analytics data to A.I. to analyze then save results in Baserow.txt | 将 Google Analytics 数据发送至 AI 进行分析，并将结果保存至 Baserow。 | 数据分析/市场 | [Send Google analytics data to A.I. to analyze then save results in Baserow.json](./AI_Research_RAG_and_Data_Analysis/Send%20Google%20analytics%20data%20to%20A.I.%20to%20analyze%20then%20save%20results%20in%20Baserow.json) |
| Spot Workplace Discrimination Patterns with AI.txt | 利用 AI 驱动分析识别职场歧视模式。 | HR/AI 研究 | [Spot Workplace Discrimination Patterns with AI.json](./AI_Research_RAG_and_Data_Analysis/Spot%20Workplace%20Discrimination%20Patterns%20with%20AI.json) |
| Summarize SERPBear data with AI (via Openrouter) and save it to Baserow.txt | 利用 AI（通过 Openrouter）摘要 SERPBear 数据，并将洞察保存至 Baserow。 | SEO/数据分析 | [Summarize SERPBear data with AI (via Openrouter) and save it to Baserow.json](./AI_Research_RAG_and_Data_Analysis/Summarize%20SERPBear%20data%20with%20AI%20(via%20Openrouter)%20and%20save%20it%20to%20Baserow.json) |
| Summarize Umami data with AI (via Openrouter) and save it to Baserow.txt | 利用 AI（通过 Openrouter）摘要 Umami 分析数据，并将洞察保存至 Baserow。 | 数据分析/市场 | [Summarize Umami data with AI (via Openrouter) and save it to Baserow.json](./AI_Research_RAG_and_Data_Analysis/Summarize%20Umami%20data%20with%20AI%20(via%20Openrouter)%20and%20save%20it%20to%20Baserow.json) |
| Survey Insights with Qdrant, Python and Information Extractor.txt | 结合 Qdrant、Python 与信息提取器从调查数据中提取与分析洞察。 | 数据分析/市场调研 | [Survey Insights with Qdrant, Python and Information Extractor.json](./AI_Research_RAG_and_Data_Analysis/Survey%20Insights%20with%20Qdrant,%20Python%20and%20Information%20Extractor.json) |
| Ultimate Scraper Workflow for n8n.txt | 适用于 n8n 的综合数据采集工作流，用于从各类来源提取数据。 | 数据采集/自动化 | [Ultimate Scraper Workflow for n8n.json](./AI_Research_RAG_and_Data_Analysis/Ultimate%20Scraper%20Workflow%20for%20n8n.json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [1_3 anomaly][1_2 KNN].txt | 利用向量数据库进行大数据分析，聚焦异常检测与 KNN 分类以辅助 AI Agent。 | AI 研究/数据分析 | [Vector Database as a Big Data Analysis Tool for AI Agents [1_3%20anomaly][1_2%20KNN].json](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[1_3%20anomaly][1_2%20KNN].json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [2_2 KNN].txt | 延续向量数据库的大数据分析应用，聚焦 KNN 分类以辅助 AI Agent。 | AI 研究/数据分析 | [Vector Database as a Big Data Analysis Tool for AI Agents [2_2%20KNN].json](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[2_2%20KNN].json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [2_3 - anomaly].txt | 探索向量数据库的大数据分析应用，聚焦异常检测以辅助 AI Agent。 | AI 研究/数据分析 | [Vector Database as a Big Data Analysis Tool for AI Agents [2_3%20-%20anomaly].json](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[2_3%20-%20anomaly].json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [3_3 - anomaly].txt | 总结向量数据库的大数据分析应用，聚焦异常检测以辅助 AI Agent。 | AI 研究/数据分析 | [Vector Database as a Big Data Analysis Tool for AI Agents [3_3%20-%20anomaly].json](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[3_3%20-%20anomaly].json) |
| Visual Regression Testing with Apify and AI Vision Model.json | 结合 Apify 与 AI 视觉模型执行视觉回归测试，检测 UI 变更。 | QA/AI 研究 | [Visual Regression Testing with Apify and AI Vision Model.json](./AI_Research_RAG_and_Data_Analysis/Visual%20Regression%20Testing%20with%20Apify%20and%20AI%20Vision%20Model.json) |
| SocialPulse Lite - Reddit Trend Monitor.json | 监控 Reddit 子版块的热门话题，并利用 OpenAI 进行分析。将洞察保存至 Google Sheets 以追踪新兴趋势。 | 数据分析/市场 | [Link to Template](AI_Research_RAG_and_Data_Analysis/SocialPulse%20Lite%20-%20Reddit%20Trend%20Monitor.json) |
| DataForge Lite - AI URL Data Extractor.json | POST 任意 URL，利用 OpenAI 提取结构化数据。返回干净的 JSON 输出以便与其他工作流集成。 | 数据提取/AI 研究 | [Link to Template](AI_Research_RAG_and_Data_Analysis/DataForge%20Lite%20-%20AI%20URL%20Data%20Extractor.json) |
| 🔍 Perplexity Research to HTML_ AI-Powered Content Creation.json | 将 Perplexity AI 研究结果转化为 HTML 内容，助力 AI 驱动的内容创作。 | 内容创作/AI 研究 | [🔍%20Perplexity%20Research%20to%20HTML_%20AI-Powered%20Content%20Creation.json](./AI_Research_RAG_and_Data_Analysis/%F0%9F%94%8D%20Perplexity%20Research%20to%20HTML_%20AI-Powered%20Content%20Creation.json) |

> 🚀 **自动化任何工作流。** [创建你的免费 n8n 账号并开始构建 →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### 其他

- `ALL_unique_nodes.txt` -- 完整节点参考列表，列出这些模板中使用的所有唯一 n8n 节点。

---

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="https://img.shields.io/badge/Create_Free_n8n_Account-Start_Automating-orange?style=for-the-badge" alt="Create Free n8n Account" />
  </a>
</p>

## 常见问题 (FAQ)

### 如何从本仓库导入 n8n 模板？

下载你想要使用的任意 `.json` 文件。打开你的 n8n 实例（自托管或 [n8n Cloud](https://n8n.partnerlinks.io/h1pwwf5m4toe)），导航至工作流页面，点击“从文件导入”，选择下载的 JSON 文件即可。工作流将出现在编辑器中等待配置。在激活前，你需要为每个连接的服务添加你自己的凭据。

### n8n 是什么？为什么我应该用它进行自动化？

n8n 是一款免费、开源的工作流自动化平台，内置超过 400 个集成。与 Zapier 或 Make 等 SaaS 替代品不同，n8n 可自托管于你的基础设施上，赋予你对数据的完全控制权。它提供可视化拖拽编辑器、原生 AI 与大语言模型支持，以及活跃的社区。你可以 [免费在 n8n Cloud 平台开始使用](https://n8n.partnerlinks.io/h1pwwf5m4toe)，或部署在自己的服务器上。

### 这些模板可以免费使用吗？

是的，本仓库中的所有模板均可完全免费下载和使用。它们收集自互联网上公开可用的资源，并在此分享以便于访问。n8n 本身是开源且支持免费自托管的。n8n Cloud 平台也提供慷慨的免费套餐，让你无需任何费用即可起步。

### 我可以贡献自己的模板吗？

绝对可以。我们欢迎并鼓励贡献。如果你构建了其他用户可能觉得有用的 n8n 工作流，请提交 Pull Request，将你的模板 JSON 文件放入对应的分类文件夹中。附上清晰的标题和描述。你还可以通过在仓库中创建 Issue 来建议新分类或改进意见。

### 这些模板支持哪些 AI 模型？

这些模板集成了广泛的 AI 模型与提供商，包括 OpenAI GPT-4 和 GPT-4o、Anthropic Claude、Google Gemini 和 Vertex AI、DeepSeek R1、Mistral AI、LangChain、Perplexity AI、NeurochainAI 以及 Hugging Face 模型。许多模板还使用 Pinecone、Qdrant、Supabase 和 Elasticsearch 等向量数据库来构建 RAG（检索增强生成）流水线。

### 这个仓库多久更新一次？

本仓库由社区积极维护并定期更新，随着 n8n 社区新模板的发布不断添加新功能与新分类。你可以 Watch 或 Star 本仓库以获取新增通知。查看页面顶部的 Last Commit Badge 可了解最近更新日期。

---

## 贡献指南

欢迎贡献。如果你有想要分享的 n8n 工作流模板，请提交 Pull Request，将 JSON 文件放入对应的分类文件夹中。对于新分类建议、Bug 报告或一般性改进意见，请创建 Issue。详细规范请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=enescingoz/awesome-n8n-templates&type=Date)](https://star-history.com/#enescingoz/awesome-n8n-templates&Date)

---

## 贡献者

<a href="https://github.com/enescingoz/awesome-n8n-templates/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=enescingoz/awesome-n8n-templates" />
</a>

---

### **赞助商**
- [mahezsh](https://github.com/mahezsh)
- [Dumpling AI](https://github.com/Dumpling-AI)

---

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="https://img.shields.io/badge/Import_280+_Templates-Create_Free_n8n_Account-orange?style=for-the-badge" alt="Import Templates" />
  </a>
</p>

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="/img/n8n.png" alt="n8n automation platform" style="max-height: 300px;" />
  </a>
</p>

---

*最后更新：2026年3月*