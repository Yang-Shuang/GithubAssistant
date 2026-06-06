![nanobot README cover](./images/readme-cover.png)

<div align="center">
  <p>
    <a href="https://nanobot.wiki/docs/latest/getting-started/nanobot-overview">English</a> |
    <a href="https://nanobot.wiki/cn/docs/latest/getting-started/nanobot-overview">简体中文</a> |
    <a href="https://nanobot.wiki/zh-Hant/docs/latest/getting-started/nanobot-overview">繁體中文</a> |
    <a href="https://nanobot.wiki/es/docs/latest/getting-started/nanobot-overview">Español</a> |
    <a href="https://nanobot.wiki/fr/docs/latest/getting-started/nanobot-overview">Français</a> |
    <a href="https://nanobot.wiki/id/docs/latest/getting-started/nanobot-overview">Bahasa Indonesia</a> |
    <a href="https://nanobot.wiki/ja/docs/latest/getting-started/nanobot-overview">日本語</a> |
    <a href="https://nanobot.wiki/ko/docs/latest/getting-started/nanobot-overview">한국어</a> |
    <a href="https://nanobot.wiki/ru/docs/latest/getting-started/nanobot-overview">Русский</a> |
    <a href="https://nanobot.wiki/vi/docs/latest/getting-started/nanobot-overview">Tiếng Việt</a>
  </p>
  <p>
    <a href="https://pypi.org/project/nanobot-ai/"><img src="https://img.shields.io/pypi/v/nanobot-ai" alt="PyPI"></a>
    <a href="https://pepy.tech/project/nanobot-ai"><img src="https://static.pepy.tech/badge/nanobot-ai" alt="Downloads"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue" alt="Python">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <a href="https://github.com/HKUDS/nanobot/graphs/commit-activity" target="_blank">
        <img alt="Commits last month" src="https://img.shields.io/github/commit-activity/m/HKUDS/nanobot?labelColor=%20%2332b583&color=%20%2312b76a"></a>
    <a href="https://github.com/HKUDS/nanobot/issues?q=is%3Aissue%20is%3Aclosed" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3AHKUDS%2Fnanobot%20is%3Aissue%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://twitter.com/intent/follow?screen_name=nanobot_project" target="_blank">
        <img src="https://img.shields.io/twitter/follow/nanobot_project?logo=X&color=%20%23f5f5f5" alt="follow on X(Twitter)"></a>
    <a href="https://nanobot.wiki/docs/latest/getting-started/nanobot-overview"><img src="https://img.shields.io/badge/Docs-nanobot.wiki-blue?style=flat&logo=readthedocs&logoColor=white" alt="Docs"></a>
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
    <a href="https://discord.gg/MnCvHqpUGB"><img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  </p>
</div>

🐈 **nanobot** 是一款开源的超轻量级 Agent 运行时，专为希望完全掌控自身 AI Agent 技术栈的你打造。它提供了一个小巧、易读的代码核心，并配备了支撑长期运行 Agent 所需的实用模块：WebUI、聊天渠道、工具、记忆、MCP、模型路由和部署方案。

## 📢 更新日志

- **2026-06-01** 🚀 发布 **v0.2.1** — **工作台版本 (The Workbench Release)**：将打包的 WebUI 打造为日常 Agent 工作台，提供更清晰的思考/响应时间线、实时文件编辑动态、项目工作区、模型与上下文控制、更稳定的持续目标支持、CLI 应用 + MCP 扩展，以及更广的提供商和渠道覆盖。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.2.1)。
- **2026-05-30** 🔐 更安全的 Matrix 验证、限制媒体下载大小、优化 WebUI 模型时间线显示。
- **2026-05-29** 🧩 扩展注册表、上下文窗口调优、文档提取控制选项。
- **2026-05-28** 🗂️ 项目工作区、访问控制、更稳定的目标执行与流式输出。
- **2026-05-27** ⏱️ Codex 流式传输在长任务中尊重空闲超时设置。
- **2026-05-26** 📡 Telegram Webhook 支持、Kagi 搜索刷新、传输错误提示优化。
- **2026-05-25** 🔌 CLI 应用与 MCP 统一整合、Step Plan 支持、持续目标稳定性提升。
- **2026-05-24** 🧰 MCP 预设模板、更丰富的斜杠命令操作、可配置的 OpenAI 兼容请求参数。
- **2026-05-23** 🖼️ 智谱图像生成支持、延长执行窗口期、优化转录配置结构。
- **2026-05-22** 🛠️ CLI 应用功能上线、新增更多图像提供商、增强网页重定向与编辑安全性。

<details>
<summary>更早更新</summary>

- **2026-05-21** ⚡ Novita 提供商接入、侧边栏响应加速、编码工具与微信回复体验优化。
- **2026-05-20** 📶 Signal 渠道支持、网关启动速度提升、README 多语言链接完善。
- **2026-05-19** 🎨 图像提供商注册表、接入 StepFun 与 Skywork、WebUI 控制功能增强。
- **2026-05-18** 🖌️ Gemini 与 MiniMax 图像生成支持、Ant Ling 集成、实时文件编辑动态显示。
- **2026-05-17** 🌊 WebUI 流式传输更流畅、AutoCompact 修复、CLI 推理缓冲优化。
- **2026-05-16** 🧠 Atomic Chat 提供商接入、目标感知超时机制、执行 URL 处理安全性提升。
- **2026-05-15** 🚀 发布 **v0.2.0** — **`/goal`** 支持跨轮次持续目标，WebUI 内置于发行包中、端到端图像生成、新增 5 个带 `fallback_models` 的提供商，并完成 Agent 循环重构。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.2.0)。
- **2026-05-14** 🎯 **`/goal`** 用于长期目标、可见的多步进度展示、聊天中的长周期任务支持。
- **2026-05-13** 🧠 回答前流式推理输出、自动备份模型切换、插件重连体验优化。
- **2026-05-12** 🎛️ 保存的模型预设与 WebUI 徽章显示、简化插件工具、飞书主题线程提示降噪。
- **2026-05-11** 🖥️ NVIDIA NIM 支持、终端机器人名称与图标配置、流式推理输出与 MiMo 切换清晰度提升。
- **2026-05-09** 🖼️ 图像回放更清晰、设置中支持自定义网络搜索密钥、飞书线程路由优化。
- **2026-05-08** ✨ 内联聊天图片功能、重新设计设置与密钥管理、Dream 记忆模块对齐可见历史记录。
- **2026-05-07** 📜 WebUI 支持本地化斜杠命令面板、局域网登录、HTTP 流式响应保真度提升。
- **2026-05-06** 🧩 可调节的工具提示、语音与插件启动更稳定、定时任务与提醒持久化。
- **2026-05-05** 🛡️ 未知 Telegram 聊天静默拒绝、Dream 记忆清理、自动化摘要内容完善。
- **2026-05-04** 🔐 钉钉外部媒体链接安全性提升、Cron 持久化支持、DeepSeek 体验打磨。
- **2026-05-03** ⚙️ Shell 白名单行为可预测、回复期间隔离聊天会话、交互式重试提示优化。
- **2026-05-02** 🐈 LongCat 支持、Token 大小估算更智能、内置升级指引说明清晰化。
- **2026-05-01** ☁️ 原生 AWS Bedrock 提供商接入、助手交接流程收紧、会话文件作用域隔离。
- **2026-04-30** 💬 飞书线程支持回复与主题路由、WhatsApp 桥接在源编辑后刷新。
- **2026-04-29** 🚀 发布 **v0.1.5.post3** — 飞书/Discord/Slack/Teams 智能线程处理；**DeepSeek-V4** 支持；Hugging Face & Olostep 接入；choices、`/history` 命令与长对话稳定性提升。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.5.post3)。
- **2026-04-28** 🌐 Olostep 网络搜索、Hugging Face 提供商接入、工作区工具中断处理更安全。
- **2026-04-27** 💬 `/history` 命令支持、会话回放上限优化、Discord/Slack 线程交互更流畅。
- **2026-04-26** 🧭 Cron 提醒自然语言化、线程感知重启机制、本地提供商与 Shell 行为安全性提升。
- **2026-04-25** 🧩 `ask_user` 选项支持、macOS LaunchAgent 部署支持、MSTeams 过期引用清理。
- **2026-04-24** 🎥 渠道视频附件支持、DeepSeek 思维控制开关、文档加载速度优化。
- **2026-04-23** 🧵 Discord 线程会话隔离、Telegram 内联按钮支持、结构化工具进度更新。
- **2026-04-22** 🔎 GitHub Copilot GPT-5 / o-series 支持、可配置网页抓取、WebUI 图片上传功能。
- **2026-04-21** 🚀 发布 **v0.1.5.post2** — Windows 与 Python 3.14 支持、Office 文档读取、OpenAI 兼容 API SSE 流式传输，以及跨会话/记忆/渠道的可靠性全面增强。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.5.post2)。
- **2026-04-20** 🎨 Kimi K2.6 支持、Telegram 长消息自动拆分、WebUI 排版与深色模式优化。
- **2026-04-19** 🌐 WebUI i18n 语言切换器、原子化会话写入与自动修复机制。
- **2026-04-18** 🧪 初始 WebUI 聊天功能、设置向导菜单优化、WebSocket 多路复用支持。
- **2026-04-17** 🪟 Windows & Python 3.14 CI 流水线、Dream 行级记忆机制、邮件自循环防护。
- **2026-04-16** 📡 OpenAI 兼容 API SSE 流式传输、Discord 渠道白名单支持。
- **2026-04-15** 🎛️ LM Studio 支持与可选 API Key、MiniMax 思维端点接入、运行时 SelfTool 功能。
- **2026-04-14** 🚀 发布 **v0.1.5.post1** — Dream 技能发现机制、轮次中跟进注入、WebSocket 渠道支持，以及更深入的渠道集成。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.5.post1)。
- **2026-04-13** 🛡️ Agent 轮次加固 — 用户消息早期持久化、自动压缩跳过活跃任务。
- **2026-04-12** 🔒 Lark 全局域名支持、Dream 学习已发现技能、Shell 沙箱收紧。
- **2026-04-11** ⚡ 上下文压缩动态缩减会话；Kagi 网络搜索；QQ & 企业微信全媒体支持。
- **2026-04-10** 📓 多 MCP 服务器支持、飞书流式传输与完成表情符号。
- **2026-04-09** 🔌 WebSocket 渠道、统一跨渠道会话管理、`disabled_skills` 配置项。
- **2026-04-08** 📤 API 文件上传功能、OpenAI 推理自动路由与 Responses 降级策略。
- **2026-04-07** 🧠 Anthropic 自适应思维机制、MCP 资源与提示词暴露为工具调用。
- **2026-04-06** 🛰️ Langfuse 可观测性集成、统一 Whisper 语音转录、邮件附件支持。
- **2026-04-05** 🚀 发布 **v0.1.5** — 更稳健的长任务执行、Dream 两阶段记忆机制、生产级沙箱隔离与编程 Agent SDK。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.5)。
- **2026-04-04** 🚀 Jinja2 响应模板支持、Dream 记忆加固、重试处理逻辑优化。
- **2026-04-03** 🧠 Xiaomi MiMo 提供商接入、思维链推理可见化、Telegram UX 打磨。
- **2026-04-02** 🧱 长任务执行更可靠 — 核心运行时加固。
- **2026-04-01** 🔑 GitHub Copilot 认证恢复；工作区路径限制收紧；OpenRouter Claude 缓存修复。
- **2026-03-31** 🛰️ 微信多模态对齐、Discord/Matrix 体验优化、Python SDK 外观封装、MCP 与工具修复。
- **2026-03-30** 🧩 OpenAI 兼容 API 收紧；可组合的 Agent 生命周期钩子。
- **2026-03-29** 💬 微信语音/打字状态/QR码与媒体容错、修复会话下 OpenAI 兼容 API 支持。
- **2026-03-28** 📚 提供商文档刷新；技能模板文案修正。
- **2026-03-27** 🚀 发布 **v0.1.4.post6** — 架构解耦、移除 litellm、端到端流式传输、微信渠道接入与安全修复。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post6)。
- **2026-03-26** 🏗️ Agent 运行器抽离与生命周期钩子统一；边界流式增量合并优化。
- **2026-03-25** 🌏 StepFun 提供商接入、可配置时区支持、Gemini 思维签名机制。
- **2026-03-24** 🔧 微信兼容性提升、飞书 CardKit 流式传输、测试套件结构重组。
- **2026-03-23** 🔧 插件命令路由重构、WhatsApp/微信媒体支持、统一渠道登录 CLI。
- **2026-03-22** ⚡ 端到端流式传输、微信渠道接入、Anthropic 缓存优化、`/status` 命令上线。
- **2026-03-21** 🔒 使用原生 `openai` + `anthropic` SDK 替换 `litellm`。详情请见 [提交记录](https://github.com/HKUDS/nanobot/commit/3dfdab7)。
- **2026-03-20** 🧙 交互式设置向导 — 选择提供商、模型自动补全，一键就绪。
- **2026-03-19** 💬 Telegram 高负载下更稳定；飞书代码块渲染修复。
- **2026-03-18** 📷 Telegram 支持通过 URL 发送媒体文件、Cron 定时任务显示可读详情。
- **2026-03-17** ✨ 飞书格式美化、Slack 完成后反应提示、自定义端点支持额外请求头、图片处理更稳定。
- **2026-03-16** 🚀 发布 **v0.1.4.post5** — 聚焦体验打磨的更新，可靠性与渠道支持增强，日常使用更省心。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post5)。
- **2026-03-15** 🧩 钉钉富媒体支持、内置技能优化、模型兼容性清理。
- **2026-03-14** 💬 渠道插件化、飞书回复功能、MCP/QQ/媒体处理稳定性提升。
- **2026-03-13** 🌐 多提供商网络搜索、LangSmith 集成、整体可靠性改进。
- **2026-03-12** 🚀 VolcEngine 支持、Telegram 回复上下文传递、`/restart` 命令与记忆模块加固。
- **2026-03-11** 🔌 企业微信接入、Ollama 支持、发现机制优化、工具行为安全性提升。
- **2026-03-10** 🧠 Token 级记忆管理、共享重试机制、网关与 Telegram 交互优化。
- **2026-03-09** 💬 Slack 线程体验打磨、飞书音频兼容性改进。
- **2026-03-08** 🚀 发布 **v0.1.4.post4** — 聚焦稳定性的更新，默认配置更安全、多实例支持更好、MCP 更稳健、渠道与提供商大幅改进。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post4)。
- **2026-03-07** 🚀 Azure OpenAI 提供商接入、WhatsApp 媒体支持、QQ 群聊功能、Telegram/飞书体验优化。
- **2026-03-06** 🪄 轻量级提供商重构、智能媒体处理、记忆与 CLI 兼容性加固。
- **2026-03-05** ⚡️ Telegram 草稿流式传输、MCP SSE 支持、多渠道可靠性修复。
- **2026-03-04** 🛠️ 依赖清理、文件读取安全增强、测试与 Cron 修复第二轮。
- **2026-03-03** 🧠 用户消息合并优化、多模态保存安全性提升、Cron 防护机制加强。
- **2026-03-02** 🛡️ 默认访问控制更安全、Cron 重载更稳定、Matrix 媒体处理优化。
- **2026-03-01** 🌐 Web 代理支持、智能 Cron 提醒、飞书富文本解析改进。
- **2026-02-28** 🚀 发布 **v0.1.4.post3** — 上下文管理更清晰、会话历史加固、Agent 逻辑优化。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post3)。
- **2026-02-27** 🧠 实验性思维模式支持、钉钉媒体消息处理、飞书与 QQ 渠道修复。
- **2026-02-26** 🛡️ 会话注入攻击防护、WhatsApp 去重机制、Windows 路径守卫、Mistral 兼容性适配。
- **2026-02-25** 🧹 新增 Matrix 渠道、会话上下文清理、工作区模板自动同步。
- **2026-02-24** 🚀 发布 **v0.1.4.post2** — 聚焦可靠性的更新，心跳机制重设计、提示词缓存优化、提供商与渠道稳定性加固。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post2)。
- **2026-02-23** 🔧 虚拟工具调用心跳机制、提示词缓存优化、Slack mrkdwn 格式修复。
- **2026-02-22** 🛡️ Slack 线程隔离机制、Discord 打字状态修复、Agent 可靠性提升。
- **2026-02-21** 🎉 发布 **v0.1.4.post1** — 新增提供商、全渠道媒体支持、重大稳定性改进。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post1)。
- **2026-02-20** 🐦 飞书接收用户多模态文件、底层记忆机制更可靠。
- **2026-02-19** ✨ Slack 支持发送文件、Discord 长消息自动拆分、CLI 模式子 Agent 运行。
- **2026-02-18** ⚡️ nanobot 接入 VolcEngine、MCP 自定义认证头支持、Anthropic 提示词缓存机制。
- **2026-02-17** 🎉 发布 **v0.1.4** — MCP 支持、进度流式传输、新增提供商与多渠道改进。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4)。
- **2026-02-16** 🦞 nanobot 集成 [ClawHub](https://clawhub.ai) 技能库 — 搜索并安装公开 Agent 技能。
- **2026-02-15** 🔑 nanobot 支持 OpenAI Codex 提供商，内置 OAuth 登录流程。
- **2026-02-14** 🔌 nanobot 正式支持 MCP！详见 [MCP 章节](#mcp-model-context-protocol)。
- **2026-02-13** 🎉 发布 **v0.1.3.post7** — 包含安全加固与多项改进。**请升级至最新版本以修复安全问题**。详情请见 [发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post7)。
- **2026-02-12** 🧠 记忆系统重设计 — 代码更少、更可靠。欢迎参与 [讨论](https://github.com/HKUDS/nanobot/discussions/566)！
- **2026-02-11** ✨ CLI 体验增强并新增 MiniMax 支持！
- **2026-02-10** 🎉 发布 **v0.1.3.post6** 带来多项改进！查看更新 [说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post6) 与我们的 [路线图](https://github.com/HKUDS/nanobot/discussions/431)。
- **2026-02-09** 💬 新增 Slack、邮件与 QQ 支持 — nanobot 现已支持多平台聊天！
- **2026-02-08** 🔧 Provider 重构 — 接入新 LLM 提供商仅需 2 步！详见 [此处](#providers)。
- **2026-02-07** 🚀 发布 **v0.1.3.post5** 支持 Qwen 并带来多项关键改进！详情见 [此处](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5)。
- **2026-02-06** ✨ 新增 Moonshot/Kimi 提供商、Discord 集成与安全加固升级！
- **2026-02-05** ✨ 新增飞书渠道、DeepSeek 提供商与定时任务支持增强！
- **2026-02-04** 🚀 发布 **v0.1.3.post4** 支持多提供商与 Docker！详情见 [此处](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post4)。
- **2026-02-03** ⚡ 集成 vLLM 实现本地 LLM 支持，优化自然语言任务调度体验！
- **2026-02-02** 🎉 nanobot 正式发布！欢迎体验 🐈 nanobot！

</details>


## 💡 为什么选择 nanobot

- **持久化工作流**：目标、记忆、工具和对话上下文可在长时间运行中保持完整。
- **原生聊天触达**：支持 WebUI、API、Telegram、飞书 (Feishu)、Slack、Discord、Teams 及邮件。
- **模型自由**：兼容 OpenAI API、本地大语言模型、图像生成、网络搜索与降级策略。
- **核心精简**：内置 MCP、记忆、部署和自动化功能，内部结构清晰易读。
- **自主掌控技术栈**：无需依赖臃肿的平台即可进行审查、定制、自托管和扩展。

## 📦 安装指南

> [!IMPORTANT]
> 如果你想要最新的功能与实验性特性，请从源码安装。 
> 
> 如果你追求最稳定的日常使用体验，建议通过 PyPI 或 `uv` 安装。

**从源码安装**

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .
```

**使用 `uv` 安装**

```bash
uv tool install nanobot-ai
```

**从 PyPI 安装**

```bash
pip install nanobot-ai
```

## 🚀 快速开始

**1. 初始化配置**

```bash
nanobot onboard
```

**2. 配置参数** (`~/.nanobot/config.json`)

在你的配置文件中设置以下 **两个部分**（其他选项均有默认值）。请将以下代码块添加或合并到你现有的配置中，而非直接覆盖整个文件。

*设置你的 API Key*（例如 [OpenRouter](https://openrouter.ai/keys) 的密钥，推荐全球用户使用）：

```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  }
}
```

*设置你的模型*（可选指定提供商 — 默认自动检测）：

```json
{
  "agents": {
    "defaults": {
      "provider": "openrouter",
      "model": "anthropic/claude-opus-4-6"
    }
  }
}
```

**3. 开始对话**

```bash
nanobot agent
```


- 想要配置不同的 LLM 提供商、网络搜索、MCP、安全设置或其他参数？详见 [配置文档](./docs/configuration.md)
- 想要在本地运行？可使用 [Atomic Chat](./docs/configuration.md#atomic-chat-local)、[vLLM](./docs/configuration.md#vllm-local-openai-compatible)、[Ollama](./docs/configuration.md#ollama-local) 及其他 [本地提供商方案](./docs/configuration.md#local-providers)。
- 想要在 Telegram、Discord、微信或飞书等聊天应用中运行 nanobot？详见 [聊天应用指南](./docs/chat-apps.md)
- 想要通过 Docker 或 Linux 服务部署？详见 [部署文档](./docs/deployment.md)

## 🌐 WebUI

WebUI **内置于发布的 Wheel 包中** — 无需额外构建步骤。只需启用 WebSocket 渠道并在浏览器中打开即可使用。

<p align="center">
  <img src="images/nanobot_webui.png" alt="nanobot webui preview" width="900">
</p>

**1. 在 `~/.nanobot/config.json` 中启用 WebSocket 渠道**

```json
{ "channels": { "websocket": { "enabled": true } } }
```

**2. 启动网关服务**

```bash
nanobot gateway
```

**3. 打开 WebUI**

在浏览器访问 [`http://127.0.0.1:8765`](http://127.0.0.1:8765)。若要从局域网内的其他设备访问，请参阅 [WebUI 文档 → 局域网访问](./webui/README.md#access-from-another-device-lan)。

> [!TIP]
> 正在开发 WebUI 本身？请查看 [`webui/README.md`](./webui/README.md) 获取 Vite 开发服务器 (HMR) 工作流说明。

## 🏗️ 架构设计

<p align="center">
  <img src="images/nanobot_arch.png" alt="nanobot architecture" width="800">
</p>

🐈 nanobot 通过将一切围绕一个轻量级的 Agent 循环来保持精简：消息从聊天应用进入，LLM 决定何时调用工具，记忆或技能仅在作为上下文需要时才被拉取，而非成为沉重的编排层。这使核心路径保持清晰易读且易于扩展，同时允许你无缝添加渠道、工具、记忆和部署选项，而不会让系统变得臃肿不堪。

## ✨ 功能场景

<table align="center">
  <tr align="center">
    <th><p align="center">📈 全天候实时市场分析</p></th>
    <th><p align="center">🚀 全栈软件工程师</p></th>
    <th><p align="center">📅 智能日常事务管理</p></th>
    <th><p align="center">📚 个人知识助手</p></th>
  </tr>
  <tr>
    <td align="center"><p align="center"><img src="case/search.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/code.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/schedule.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/memory.gif" width="180" height="400"></p></td>
  </tr>
  <tr>
    <td align="center">发现 • 洞察 • 趋势</td>
    <td align="center">开发 • 部署 • 扩展</td>
    <td align="center">排期 • 自动化 • 整理</td>
    <td align="center">学习 • 记忆 • 推理</td>
  </tr>
</table>

## 📚 文档

浏览 [仓库文档](./docs/README.md) 获取最新功能与 GitHub 开发版说明，或访问 [nanobot.wiki](https://nanobot.wiki/docs/latest/getting-started/nanobot-overview) 查阅稳定版发行文档。

- 用你熟悉的聊天应用与 nanobot 对话：[聊天应用指南](./docs/chat-apps.md)
- 配置提供商、网络搜索、MCP 与运行时行为：[配置说明](./docs/configuration.md)
- 将 nanobot 集成到本地工具与自动化流程中：[OpenAI 兼容 API](./docs/openai-api.md) · [Python SDK](./docs/python-sdk.md)
- 使用 Docker 或 Linux 服务运行 nanobot：[部署文档](./docs/deployment.md)

## 🤝 贡献指南 & 路线图

欢迎提交 PR！代码库刻意保持精简且易读。🤗

### 分支策略

| 分支 | 用途 |
|--------|---------|
| `main` | 稳定发行版 — 仅包含 Bug 修复与小幅改进 |
| `nightly` | 实验性特性 — 新功能与破坏性变更 |

**不确定该提交到哪个分支？** 详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

**路线图** — 认领一项任务并 [提交 PR](https://github.com/HKUDS/nanobot/pulls)！

- **多模态交互** — 看得懂、听得见（图像、语音、视频）
- **长期记忆** — 永不遗忘重要上下文信息
- **更优的推理能力** — 支持多步规划与反思机制
- **更多集成场景** — 日历及其他第三方服务接入
- **自我进化** — 从反馈与错误中学习改进

## 联系方式

本项目由 [Xubin Ren](https://github.com/re-bin) 作为个人开源项目发起，并持续使用个人资源以独立维护者身份进行更新，同时受益于开源社区的贡献。如有问题、想法或合作意向，欢迎联系 [xubinrencs@gmail.com](mailto:xubinrencs@gmail.com)。

### 贡献者

<a href="https://github.com/HKUDS/nanobot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/nanobot&max=100&columns=12&updated=20260210" alt="Contributors" />
</a>


## ⭐ Star 历史

<div align="center">
  <a href="https://star-history.com/#HKUDS/nanobot&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" style="border-radius: 15px; box-shadow: 0 0 30px rgba(0, 217, 255, 0.3);" />
    </picture>
  </a>
</div>

<p align="center">
  <em> 感谢你的访问 ✨ nanobot!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.nanobot&style=for-the-badge&color=00d4ff" alt="Views">
</p>