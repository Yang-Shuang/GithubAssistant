<p align="center">
<a href="https://langbot.app">
<img width="130" src="res/logo-blue.png" alt="LangBot"/>
</a>

<div align="center">

<a href="https://www.producthunt.com/products/langbot?utm_source=badge-follow&utm_medium=badge&utm_source=badge-langbot" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/follow.svg?product_id=1077185&theme=light" alt="LangBot - Production&#0045;grade&#0032;IM&#0032;bot&#0032;made&#0032;easy&#0046; | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

<h3>面向生产环境的 AI 智能体即时通讯机器人构建平台。</h3>
<h4>快速构建、调试并将 AI 机器人部署至 Slack、Discord、Telegram、微信等平台。</h4>

English / [简体中文](README_CN.md) / [繁體中文](README_TW.md) / [日本語](README_JP.md) / [Español](README_ES.md) / [Français](README_FR.md) / [한국어](README_KO.md) / [Русский](README_RU.md) / [Tiếng Việt](README_VI.md)

[![Discord](https://img.shields.io/discord/1335141740050649118?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb)](https://discord.gg/wdNEHETs87)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/langbot-app/LangBot)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/langbot-app/LangBot)](https://github.com/langbot-app/LangBot/releases/latest)
<img src="https://img.shields.io/badge/python-3.10 ~ 3.13 -blue.svg" alt="python">
[![GitHub stars](https://img.shields.io/github/stars/langbot-app/LangBot?style=social)](https://github.com/langbot-app/LangBot/stargazers)

<a href="https://langbot.app">官网</a> ｜
<a href="https://link.langbot.app/en/docs/features">功能特性</a> ｜
<a href="https://link.langbot.app/en/docs/guide">文档</a> ｜
<a href="https://link.langbot.app/en/docs/api">API</a> ｜
<a href="https://space.langbot.app/cloud">云端服务</a> ｜
<a href="https://space.langbot.app">插件市场</a> ｜
<a href="https://langbot.featurebase.app/roadmap">路线图</a>

</div>

</p>

---

## 什么是 LangBot？

LangBot 是一个**开源的生产级平台**，用于构建基于 AI 的即时通讯机器人。它将大语言模型（LLM）接入任意聊天平台，使你能够创建具备对话、任务执行及工作流集成能力的智能体。

### 核心能力

- **AI 对话与智能体** —— 支持多轮对话、工具调用、多模态处理及流式输出。内置 RAG（检索增强生成）知识库，并深度集成 [Dify](https://dify.ai)、[Coze](https://coze.com)、[n8n](https://n8n.io)、[Langflow](https://langflow.org)。
- **全平台即时通讯支持** —— 一套代码适配 Discord、Telegram、Slack、LINE、QQ、微信、企业微信、飞书、钉钉、KOOK。
- **生产级就绪** —— 提供权限控制、限流机制、敏感词过滤、全面监控与异常处理，深受企业信赖。
- **插件生态系统** —— 拥有数百款插件，采用事件驱动架构，支持组件扩展及 [MCP 协议](https://modelcontextprotocol.io/)。
- **Web 管理面板** —— 通过直观的浏览器界面配置、管理和监控你的机器人，无需编辑 YAML 文件。
- **多流水线架构** —— 针对不同场景部署独立机器人，配备完善的监控与异常处理机制。

[→ 了解更多功能特性](https://link.langbot.app/en/docs/features)

📍 实战指南：[5分钟部署跨平台 AI 机器人](https://blog.langbot.app/en/blog/deploy-ai-bot-in-5-minutes/)、[将 DeepSeek 接入微信、Discord 和 Telegram](https://blog.langbot.app/en/blog/connect-deepseek-to-wechat/)、[在 Discord、Telegram 和 Slack 中运行 Dify Agent](https://blog.langbot.app/en/blog/dify-agent-discord-telegram-slack/)，以及 [构建基于 n8n 的聊天机器人](https://blog.langbot.app/en/blog/n8n-multi-platform-ai-chatbot/)。

---

## 快速开始

### ☁️ LangBot 云端服务（推荐）

**[LangBot 云端服务](https://space.langbot.app/cloud)** —— 零部署，开箱即用。

### 一行命令启动

```bash
uvx langbot
```

> 需要安装 [uv](https://docs.astral.sh/uv/getting-started/installation/)。访问 http://localhost:5300 —— 完成部署。

### Docker Compose 部署

```bash
git clone https://github.com/langbot-app/LangBot
cd LangBot/docker
docker compose up -d
```

### 一键云部署

[![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/en-US/templates/ZKTBDH)
[![Deploy on Railway](https://railway.com/button.svg)](https://railway.app/template/yRrAyL?referralCode=vogKPF)

**更多部署方式：** [Docker](https://link.langbot.app/en/docs/docker) · [手动部署](https://link.langbot.app/en/docs/manual-deploy) · [宝塔面板](https://link.langbot.app/en/docs/bt-panel) · [Kubernetes](./docker/README_K8S.md)

---

## 支持的平台

| 平台 | 状态 | 说明 |
|----------|--------|-------|
| Discord | ✅ | 官方支持 |
| Telegram | ✅ | 官方支持 |
| Slack | ✅ | 官方支持 |
| LINE | ✅ | 官方支持 |
| QQ | ✅ | 个人号与官方 API（频道、私聊、群聊） |
| WeCom | ✅ | 企业微信、外部客服、AI 机器人 |
| WeChat | ✅ | 个人号与公众号 |
| Lark | ✅ | 官方支持 |
| DingTalk | ✅ | 官方支持 |
| KOOK | ✅ | 官方支持 |
| Satori | ✅ |  |
| Email | ✅ | Matrix, Satori |
| Matrix | ✅ | 支持 Signal、WhatsApp、Messenger、iMessage、Mattermost、Google Chat、IRC、XMPP、Zulip 等多种桥接平台 |

---

## 支持的 LLM 与集成服务

| 提供商                                                                                                          | 类型         | 状态 |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | ------ |
| [OpenAI](https://platform.openai.com/)                                                                            | LLM          | ✅     |
| [Anthropic](https://www.anthropic.com/)                                                                           | LLM          | ✅     |
| [DeepSeek](https://www.deepseek.com/)                                                                             | LLM          | ✅     |
| [Google Gemini](https://aistudio.google.com/prompts/new_chat)                                                     | LLM          | ✅     |
| [xAI](https://x.ai/)                                                                                              | LLM          | ✅     |
| [Moonshot](https://www.moonshot.cn/)                                                                              | LLM          | ✅     |
| [Zhipu AI](https://open.bigmodel.cn/)                                                                             | LLM          | ✅     |
| [Ollama](https://ollama.com/)                                                                                     | 本地大模型    | ✅     |
| [LM Studio](https://lmstudio.ai/)                                                                                 | 本地大模型    | ✅     |
| [Dify](https://dify.ai)                                                                                           | LLMOps       | ✅     |
| [MCP](https://modelcontextprotocol.io/)                                                                           | 协议         | ✅     |
| [SiliconFlow](https://siliconflow.cn/)                                                                            | API 网关      | ✅     |
| [Aliyun Bailian](https://bailian.console.aliyun.com/)                                                             | API 网关      | ✅     |
| [Volc Engine Ark](https://console.volcengine.com/ark/region:ark+cn-beijing/model?vendor=Bytedance&view=LIST_VIEW) | API 网关      | ✅     |
| [ModelScope](https://modelscope.cn/docs/model-service/API-Inference/intro)                                        | API 网关      | ✅     |
| [GiteeAI](https://ai.gitee.com/)                                                                                  | API 网关      | ✅     |
| [CompShare](https://www.compshare.cn/?ytag=GPU_YY-gh_langbot)                                                     | GPU 算力平台   | ✅     |
| [PPIO](https://ppinfra.com/user/register?invited_by=QJKFYD&utm_source=github_langbot)                             | GPU 算力平台   | ✅     |
| [ShengSuanYun](https://www.shengsuanyun.com/?from=CH_KYIPP758)                                                    | GPU 算力平台   | ✅     |
| [接口 AI](https://jiekou.ai/)                                                                                     | API 网关      | ✅     |
| [302.AI](https://share.302.ai/SuTG99)                                                                             | API 网关      | ✅     |
| [Qiniu](https://www.qiniu.com/ai/agent)                                                                           | API 网关      | ✅     |

[→ 查看所有集成服务](https://link.langbot.app/en/docs/features)

---

## 为什么选择 LangBot？

| 使用场景                    | LangBot 如何提供帮助                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| **客户支持**        | 部署 AI 智能体至 Slack/Discord/Telegram，利用知识库自动回答问题 |
| **内部工具**          | 将 n8n/Dify 工作流接入企业微信/钉钉，实现业务流程自动化              |
| **社区管理**    | 借助 AI 内容过滤与互动功能，高效管理 QQ/Discord 群组               |
| **全平台覆盖** | 一个机器人覆盖所有平台。通过统一仪表盘集中管理                                     |

---

## 在线演示

**立即体验：** https://demo.langbot.dev/

- 邮箱：`demo@langbot.app`
- 密码：`langbot123456`

_注：此为公开测试环境，请勿输入敏感信息。_

---

## 社区交流

[![Discord](https://img.shields.io/discord/1335141740050649118?logo=discord&label=Discord)](https://discord.gg/wdNEHETs87)

- [加入 Discord 社区](https://discord.gg/wdNEHETs87)

---

## ⭐ Star 历史记录

[![Star History Chart](https://api.star-history.com/svg?repos=langbot-app/LangBot&type=Date)](https://star-history.com/#langbot-app/LangBot&Date)

---

## 贡献者

感谢所有帮助 LangBot 变得更好的[贡献者](https://github.com/langbot-app/LangBot/graphs/contributors)：

<a href="https://github.com/langbot-app/LangBot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=langbot-app/LangBot" />
</a>