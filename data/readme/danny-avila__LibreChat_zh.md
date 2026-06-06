<p align="center">
  <a href="https://librechat.ai">
    <img src="client/public/assets/logo.svg" height="256">
  </a>
  <h1 align="center">
    <a href="https://librechat.ai">LibreChat</a>
  </h1>
</p>

<p align="center">
  <strong>English</strong> ·
  <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <a href="https://discord.librechat.ai"> 
    <img
      src="https://img.shields.io/discord/1086345563026489514?label=&logo=discord&style=for-the-badge&logoWidth=20&logoColor=white&labelColor=000000&color=blueviolet">
  </a>
  <a href="https://www.youtube.com/@LibreChat"> 
    <img
      src="https://img.shields.io/badge/YOUTUBE-red.svg?style=for-the-badge&logo=youtube&logoColor=white&labelColor=000000&logoWidth=20">
  </a>
  <a href="https://docs.librechat.ai"> 
    <img
      src="https://img.shields.io/badge/DOCS-blue.svg?style=for-the-badge&logo=read-the-docs&logoColor=white&labelColor=000000&logoWidth=20">
  </a>
  <a aria-label="Sponsors" href="https://github.com/sponsors/danny-avila">
    <img
      src="https://img.shields.io/badge/SPONSORS-brightgreen.svg?style=for-the-badge&logo=github-sponsors&logoColor=white&labelColor=000000&logoWidth=20">
  </a>
</p>

<p align="center">
<a href="https://railway.com/deploy/librechat-official?referralCode=HI9hWz&utm_medium=integration&utm_source=readme&utm_campaign=librechat">
  <img src="https://railway.com/button.svg" alt="Deploy on Railway" height="30">
</a>
<a href="https://zeabur.com/templates/0X2ZY8">
  <img src="https://zeabur.com/button.svg" alt="Deploy on Zeabur" height="30"/>
</a>
<a href="https://template.cloud.sealos.io/deploy?templateName=librechat">
  <img src="https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg" alt="Deploy on Sealos" height="30">
</a>
</p>

<p align="center">
  <a href="https://www.librechat.ai/docs/translation">
    <img 
      src="https://img.shields.io/badge/dynamic/json.svg?style=for-the-badge&color=2096F3&label=locize&query=%24.translatedPercentage&url=https://api.locize.app/badgedata/4cb2598b-ed4d-469c-9b04-2ed531a8cb45&suffix=%+translated" 
      alt="Translation Progress">
  </a>
</p>


# ✨ 功能特性

- 🖥️ **界面与体验**：受 ChatGPT 启发，并进行了增强的设计与功能优化

- 🤖 **AI 模型选择**：  
  - Anthropic (Claude)、AWS Bedrock、OpenAI、Azure OpenAI、Google、Vertex AI、OpenAI Responses API（含 Azure）
  - [自定义端点](https://www.librechat.ai/docs/quick_start/custom_endpoints)：LibreChat 支持使用任何兼容 OpenAI 的 API，无需代理即可直接调用
  - 兼容 [本地与远程 AI 服务提供商](https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints)：
    - Ollama、groq、Cohere、Mistral AI、Apple MLX、koboldcpp、together.ai、
    - OpenRouter、Helicone、Perplexity、ShuttleAI、Deepseek、Qwen 等

- 🔧 **[代码解释器 API](https://www.librechat.ai/docs/features/code_interpreter)**： 
  - 安全沙箱执行：支持 Python、Node.js (JS/TS)、Go、C/C++、Java、PHP、Rust 和 Fortran
  - 无缝文件处理：直接上传、处理和下载文件
  - 无隐私顾虑：完全隔离且安全的执行环境

- 🔦 **智能体与工具集成**：  
  - **[LibreChat 智能体 (Agents)](https://www.librechat.ai/docs/features/agents)**：
    - 零代码自定义助手：构建专业化的 AI 驱动辅助工具
    - 智能体市场：发现并部署社区开发的智能体
    - 协作共享：与特定用户和群组分享智能体
    - 灵活可扩展：支持使用 MCP Servers、工具、文件搜索、代码执行等功能
    - [技能 (Skills)](https://www.librechat.ai/docs/features/skills)：创建可复用的 `SKILL.md` 指令包，用于手动触发、自动触发或常驻模式的智能体工作流
    - [子智能体 (Subagents)](https://www.librechat.ai/docs/features/subagents)：将专注任务委派给独立的子智能体运行实例，并拥有独立上下文窗口
    - 兼容自定义端点、OpenAI、Azure、Anthropic、AWS Bedrock、Google、Vertex AI、Responses API 等
    - [模型上下文协议 (MCP)](https://modelcontextprotocol.io/clients#librechat) 支持用于工具调用

- 🔍 **网页搜索**：  
  - 搜索互联网并检索相关信息，以增强你的 AI 对话上下文
  - 整合搜索引擎、内容抓取器和结果重排器，以获得最佳搜索结果
  - **可自定义的 Jina 重排序**：配置自定义 Jina API URL 以使用重排序服务
  - **[了解更多 →](https://www.librechat.ai/docs/features/web_search)**

- 🪄 **基于代码工件的生成式界面 (Generative UI with Code Artifacts)**：  
  - [代码工件 (Code Artifacts)](https://youtu.be/GfTj7O4gmd0?si=WJbdnemZpJzBrJo3) 允许直接在聊天中创建 React、HTML 和 Mermaid 图表

- 🎨 **图像生成与编辑**
  - 使用 [GPT-Image-1](https://www.librechat.ai/docs/features/image_gen#1--openai-image-tools-recommended) 进行文生图和图生图
  - 使用 [DALL-E (3/2)](https://www.librechat.ai/docs/features/image_gen#2--dalle-legacy)、[Stable Diffusion](https://www.librechat.ai/docs/features/image_gen#3--stable-diffusion-local)、[Flux](https://www.librechat.ai/docs/features/image_gen#4--flux) 或任意 [MCP server](https://www.librechat.ai/docs/features/image_gen#5--model-context-protocol-mcp) 进行文生图
  - 根据提示词生成精美图像，或通过单条指令优化现有图片

- 💾 **预设与上下文管理**：  
  - 创建、保存并分享自定义预设  
  - 在对话过程中随时切换 AI 端点和预设
  - 支持编辑、重新提交消息，并通过对话分支功能继续对话
  - 创建提示词并与特定用户和群组分享
  - [消息与对话分叉 (Fork)](https://www.librechat.ai/docs/features/fork)：实现更高级的上下文控制

- 💬 **多模态与文件交互**：  
  - 使用 Claude 3、GPT-4.5、GPT-4o、o1、Llama-Vision 和 Gemini 📸 上传并分析图像
  - 使用自定义端点、OpenAI、Azure、Anthropic、AWS Bedrock & Google 🗃️ 进行文件对话

- 🌎 **多语言界面**：
  - English, 中文 (简体), 中文 (繁體), العربية, Deutsch, Español, Français, Italiano
  - Polski, Português (PT), Português (BR), Русский, 日本語, Svenska, 한국어, Tiếng Việt
  - Türkçe, Nederlands, עברית, Català, Čeština, Dansk, Eesti, فارسی
  - Suomi, Magyar, Հայերեն, Bahasa Indonesia, ქართული, Latviešu, ไทย, ئۇيغۇرچە

- 🧠 **推理界面 (Reasoning UI)**：  
  - 为 DeepSeek-R1 等思维链（Chain-of-Thought）/推理型 AI 模型提供动态推理界面展示

- 🎨 **可定制界面**：  
  - 支持自定义下拉菜单与界面布局，兼顾高级用户与新用户的需求

- 🌊 **[断点续传流 (Resumable Streams)](https://www.librechat.ai/docs/features/resumable_streams)**：  
  - 永不丢失回复：若连接中断，AI 回复将自动重新连接并继续生成
  - 多标签页与多设备同步：可在多个标签页中打开同一对话，或跨设备接续使用
  - 生产级就绪：支持从单机部署到基于 Redis 的水平扩展集群

- 🗣️ **语音与音频**：  
  - 通过语音转文字（STT）和文字转语音（TTS）实现免提对话
  - 自动发送并播放音频消息
  - 支持 OpenAI、Azure OpenAI 及 ElevenLabs

- 📥 **对话导入与导出**：  
  - 从 LibreChat、ChatGPT、Chatbot UI 导入对话记录
  - 将对话导出为截图、Markdown、纯文本或 JSON 格式

- 🔍 **搜索与发现**：  
  - 支持全局搜索所有消息/对话记录

- 👥 **多用户与安全访问**：
  - 支持多用户管理与安全认证，兼容 OAuth2、LDAP 及邮箱登录
  - 内置内容审核功能与 Token 消耗管理工具

- ⚙️ **配置与部署**：  
  - 支持配置代理、反向代理、Docker 及多种部署选项
  - 使用 [结合 CloudFront 的 S3 存储](https://www.librechat.ai/docs/configuration/cdn/cloudfront) 获取稳定的媒体链接、边缘分发、签名 Cookie 及安全下载功能
  - 支持完全本地化部署或云端托管

- 📖 **开源与社区**：  
  - 完全开源，公开开发过程
  - 由社区驱动的开发、支持与反馈机制

[如需全面了解我们的功能，请查阅文档](https://docs.librechat.ai/) 📚

## 🪶 一站式 AI 对话体验：LibreChat

LibreChat 是一款自托管的 AI 对话平台，将各大主流 AI 提供商整合于一个注重隐私的统一界面中。

除基础聊天外，LibreChat 还提供 AI 智能体、模型上下文协议（MCP）支持、代码工件（Artifacts）、代码解释器、自定义操作、对话搜索以及企业级多用户认证功能。

项目完全开源且持续活跃开发，专为重视自身 AI 基础设施控制权的用户打造。

---

## 🌐 资源链接

**GitHub 仓库：**
  - **RAG API：** [github.com/danny-avila/rag_api](https://github.com/danny-avila/rag_api)
  - **官网代码库：** [github.com/LibreChat-AI/librechat.ai](https://github.com/LibreChat-AI/librechat.ai)

**其他资源：**
  - **官方网站：** [librechat.ai](https://librechat.ai)
  - **官方文档：** [librechat.ai/docs](https://librechat.ai/docs)
  - **官方博客：** [librechat.ai/blog](https://librechat.ai/blog)

---

## 📝 更新日志

请访问发布页面与更新日志以获取最新动态：
- [Releases](https://github.com/danny-avila/LibreChat/releases)
- [Changelog](https://www.librechat.ai/changelog) 

**⚠️ 升级前请务必查阅[更新日志](https://www.librechat.ai/changelog)，了解是否存在破坏性变更（Breaking Changes）。**

---

## ⭐ Star 历史

<p align="center">
  <a href="https://star-history.com/#danny-avila/LibreChat&Date">
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=danny-avila/LibreChat&type=Date&theme=dark" onerror="this.src='https://api.star-history.com/svg?repos=danny-avila/LibreChat&type=Date'" />
  </a>
</p>
<p align="center">
  <a href="https://trendshift.io/repositories/4685" target="_blank" style="padding: 10px;">
    <img src="https://trendshift.io/api/badge/repositories/4685" alt="danny-avila%2FLibreChat | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  <a href="https://runacap.com/ross-index/q1-24/" target="_blank" rel="noopener" style="margin-left: 20px;">
    <img style="width: 260px; height: 56px" src="https://runacap.com/wp-content/uploads/2024/04/ROSS_badge_white_Q1_2024.svg" alt="ROSS Index - Fastest Growing Open-Source Startups in Q1 2024 | Runa Capital" width="260" height="56"/>
  </a>
</p>

---

## ✨ 贡献指南

欢迎提交贡献、建议、Bug 报告及修复方案！

如需新增功能、组件或扩展，请先创建 Issue 进行讨论，再提交 Pull Request (PR)。

如果你希望协助将 LibreChat 翻译成本地语言，我们非常欢迎你的参与！优化翻译不仅能让全球用户更便捷地使用 LibreChat，也能提升整体用户体验。请查阅我们的[翻译指南](https://www.librechat.ai/docs/translation)。

---

## 💖 本项目的当前状态离不开所有贡献者的支持

<a href="https://github.com/danny-avila/LibreChat/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=danny-avila/LibreChat" />
</a>

---

## 🎉 特别鸣谢

感谢 [Locize](https://locize.com) 提供的翻译管理工具，助力 LibreChat 实现多语言支持。

<p align="center">
  <a href="https://locize.com" target="_blank" rel="noopener noreferrer">
    <img src="https://github.com/user-attachments/assets/d6b70894-6064-475e-bb65-92a9e23e0077" alt="Locize Logo" height="50">
  </a>
</p>