<div align="center"><a name="readme-top"></a>

[![][image-banner]][vercel-link]

# LobeHub

LobeHub 是工作与生活的终极空间：<br/>
发现、构建并与与你共同成长的 Agent 队友协作。<br/>
我们正在打造全球最大的“人类-Agent”协同演进（Co-evolution）网络。

**English** · [简体中文](./README.zh-CN.md) · [官方网站][official-site] · [更新日志][changelog] · [文档][docs] · [博客][blog] · [反馈][github-issues-link]

<!-- SHIELD GROUP -->

[![][github-release-shield]][github-release-link]
[![][docker-release-shield]][docker-release-link]
[![][vercel-shield]][vercel-link]
[![][discord-shield]][discord-link]<br/>
[![][codecov-shield]][codecov-link]
[![][github-action-test-shield]][github-action-test-link]
[![][github-action-release-shield]][github-action-release-link]
[![][github-releasedate-shield]][github-releasedate-link]<br/>
[![][github-contributors-shield]][github-contributors-link]
[![][github-forks-shield]][github-forks-link]
[![][github-stars-shield]][github-stars-link]
[![][github-issues-shield]][github-issues-link]
[![][github-license-shield]][github-license-link]<br>
[![][sponsor-shield]][sponsor-link]

**分享 LobeHub 仓库**

[![][share-x-shield]][share-x-link]
[![][share-telegram-shield]][share-telegram-link]
[![][share-whatsapp-shield]][share-whatsapp-link]
[![][share-reddit-shield]][share-reddit-link]
[![][share-weibo-shield]][share-weibo-link]
[![][share-mastodon-shield]][share-mastodon-link]
[![][share-linkedin-shield]][share-linkedin-link]

<sup>与你共同成长的 Agent 队友</sup>

[![][github-trending-shield]][github-trending-url]

[![](https://vercel.com/oss/program-badge.svg)](https://vercel.com/oss)

</div>

<details>
<summary><kbd>目录</kbd></summary>

#### 目录

- [👋🏻 快速开始与加入社区](#-getting-started--join-our-community)
- [✨ 功能特性](#-features)
  - [创建：以 Agent 为工作单元](#create-agents-as-the-unit-of-work)
  - [协作：扩展新型协作网络](#collaborate-scale-new-forms-of-collaboration-networks)
  - [进化：人类与 Agent 的协同演进](#evolve-co-evolution-of-humans-and-agents)
  - [MCP 插件一键安装](#mcp-plugin-one-click-installation)
  - [MCP 市场（Marketplace）](#mcp-marketplace)
  - [桌面客户端](#desktop-app)
  - [智能联网搜索](#smart-internet-search)
  - [思维链（Chain of Thought）](#chain-of-thought)
  - [对话分支（Branching Conversations）](#branching-conversations)
  - [Artifacts 支持](#artifacts-support)
  - [文件上传 / 知识库](#file-upload-knowledge-base)
  - [多模型服务商支持](#multi-model-service-provider-support)
  - [本地大语言模型（LLM）支持](#local-large-language-model-llm-support)
  - [视觉识别能力](#model-visual-recognition)
  - [TTS & STT 语音对话](#tts--stt-voice-conversation)
  - [文生图功能](#text-to-image-generation)
  - [插件系统（Function Calling）](#plugin-system-function-calling)
  - [Agent 市场（GPTs）](#agent-market-gpts)
  - [支持本地 / 远程数据库](#support-local--remote-database)
  - [支持多用户管理](#support-multi-user-management)
  - [渐进式 Web 应用（PWA）](#progressive-web-app-pwa)
  - [移动端适配](#mobile-device-adaptation)
  - [自定义主题](#custom-themes)
  - [`*` 更多特性](#-whats-more)
- [🛳 私有化部署（Self Hosting）](#-self-hosting)
  - [`A` 使用 Vercel、Zeabur、Sealos 或阿里云部署](#a-deploying-with-vercel-zeabur--sealos-or-alibaba-cloud)
  - [`B` 使用 Docker 部署](#b-deploying-with-docker)
  - [环境变量配置](#environment-variable)
- [📦 生态组件](#-ecosystem)
- [🧩 插件开发](#-plugins)
- [⌨️ 本地开发](#️-local-development)
- [🤝 贡献指南](#-contributing)
- [❤️ 赞助支持](#️-sponsor)
- [🔗 更多产品](#-more-products)

####

<br/>

</details>

<https://github.com/user-attachments/assets/6710ad97-03d0-4175-bd75-adff9b55eca2>

## 👋🏻 快速开始与加入社区

我们是一群 e/acc（加速主义）设计工程师，致力于为 AIGC 提供现代化的设计组件与工具。通过采用自举（Bootstrapping）开发模式，我们希望为开发者与用户打造更加开放、透明且友好的产品生态。

无论是普通用户还是专业开发者，LobeHub 都将是你的 AI Agent 游乐场。请注意，LobeHub 目前处于积极开发阶段，欢迎随时提交遇到的任何 [问题][issues-link]。

| [![](https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1065874&theme=light&t=1769347414733)](https://www.producthunt.com/products/lobehub?embed=true&utm_source=badge-featured&utm_medium=badge&utm_campaign=badge-lobehub) | 我们已上线 Product Hunt！很高兴能将 LobeHub 带给世界。如果你相信人类与 Agent 协同演进的未来，请支持我们的旅程。 |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![][discord-shield-badge]][discord-link]                                                                                                                                                                                                         | 加入我们的 Discord 社区！在这里你可以与开发者及其他热情的 LobeHub 用户建立联系。                                                    |

> \[!IMPORTANT]
>
> **给我们点 Star**，你将第一时间收到 GitHub 上的所有版本更新通知 ⭐️

[![][image-star]][github-stars-link]

<details>
  <summary><kbd>Star 历史</kbd></summary>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=lobehub%2Flobehub&theme=dark&type=Date">
    <img width="100%" src="https://api.star-history.com/svg?repos=lobehub%2Flobehub&type=Date">
  </picture>
</details>

## ✨ 功能特性

今天的 AI Agent 大多是一次性、任务驱动的工具。它们缺乏上下文感知能力，彼此孤立存在，且需要在不同窗口和模型间手动交接。尽管部分工具具备记忆功能，但往往局限于全局、浅层且缺乏个性化。在这种模式下，你被迫在碎片化的对话中切换，难以形成结构化的生产力。

**LobeHub 将彻底改变这一切。**

LobeHub 是一个工作与生活方式空间，用于发现、构建并与与你共同成长的 Agent 队友协作。在 LobeHub 中，我们将 **Agent 视为工作单元**，提供人类与 Agent 协同演进的基础设施。

![](https://hub-apac-1.lobeobjects.space/blog/assets/2204cde2228fb3f583f3f2c090bc49fb.webp)

### 创建：以 Agent 为工作单元

构建个性化 AI 团队始于 **Agent 构建器**。你只需描述一次需求，即可立即启动 Agent 配置并应用自动设置，实现开箱即用。

- **统一智能**：无缝接入任意模型与模态——一切尽在你的掌控之中。
- **万种技能**：通过超过 10,000 个工具和兼容 MCP 的插件库，让你的 Agent 连接你日常使用的各项技能。

[![][back-to-top]](#readme-top)

<div align="right">

[![][back-to-top]](#readme-top)

</div>

![](https://hub-apac-1.lobeobjects.space/blog/assets/771ff3d30b9ef93e65e55021cc43d356.webp)

### 协作：扩展新型协作网络

LobeHub 引入 **Agent 群组**功能，让你能够像对待真实队友一样与 Agent 协同工作。系统会根据任务自动组装合适的 Agent，实现并行协作与迭代优化。

- **页面（Pages）**：在共享上下文中，于同一位置撰写并打磨内容。
- **调度（Schedule）**：设置定时运行计划，让 Agent 在你不在时也能准时完成任务。
- **项目（Project）**：按项目组织工作，保持一切井井有条且易于追踪。
- **工作区（Workspace）**：团队与 Agent 协作的共享空间，确保清晰的权责划分与全局可见性。

[![][back-to-top]](#readme-top)

<div align="right">

[![][back-to-top]](#readme-top)

</div>

![](https://hub-apac-1.lobeobjects.space/blog/assets/fe98eae9fcb6acc47c8e1fb69bdb4b50.webp)

### 进化：人类与 Agent 的协同演进

最好的 AI 是深刻理解你的那一个。LobeHub 具备 **个人记忆（Personal Memory）** 功能，能够精准理解你的需求。

- **持续学习**：Agent 会从你的工作习惯中学习，自适应行为并在恰当时机发挥作用。
- **白盒记忆**：我们崇尚透明化。Agent 使用结构化、可编辑的记忆机制，让你完全掌控其记住的内容。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

<details>
<summary>更多功能特性</summary>

![][image-feat-mcp]

### MCP 插件一键安装

**无缝连接你的 AI 与世界**

通过启用流畅、安全且动态的外部交互，释放你 AI 的全部潜力。LobeHub 的 MCP（Model Context Protocol）插件系统打破了你的 AI 与数字生态之间的壁垒，实现前所未有的连通性与功能扩展。

将对话转化为强大的工作流：连接数据库、API、文件系统及其他服务。体验真正理解并与你的世界互动的自由 AI。

[![][back-to-top]](#readme-top)

![][image-feat-mcp-market]

### MCP 市场（Marketplace）

**发现、连接与扩展**

浏览不断增长的 MCP 插件库，轻松扩展 AI 能力并优化工作流。访问 [lobehub.com/mcp](https://lobehub.com/mcp) 探索 MCP 市场，这里汇集了精心筛选的集成方案，全面提升你的 AI 处理各类工具与服务的能力。

从效率工具到开发环境，发现延伸 AI 影响力与效能的新方式。加入社区，找到最适合你需求的完美插件。

[![][back-to-top]](#readme-top)

![][image-feat-desktop]

### 桌面客户端

**极致性能，零干扰体验**

在不受浏览器限制的环境下享受完整的 LobeHub 体验——全面、专注且随时待命。我们的桌面应用为你的 AI 交互提供专属环境，确保最佳性能与最小干扰。

获得更快的响应速度、更优的资源管理以及更稳定的连接体验。桌面端专为追求极致性能的 AI 工具用户打造。

[![][back-to-top]](#readme-top)

![][image-feat-web-search]

### 智能联网搜索

**按需获取在线知识**

借助实时互联网访问能力，让你的 AI 紧跟世界脉搏——新闻、数据、趋势等一应俱全。随时掌握最新资讯，确保你的 AI 提供准确且最新的回答。

在不离开对话的情况下访问实时信息、验证事实并探索时事。你的 AI 将成为通往全球知识的门户，始终全面且最新。

[![][back-to-top]](#readme-top)

[![][image-feat-cot]][docs-feat-cot]

### [思维链（Chain of Thought）][docs-feat-cot]

以前所未有的方式体验 AI 推理过程。通过我们创新的思维链（CoT）可视化功能，观察复杂问题如何一步步展开。这一突破性功能为 AI 的决策过程提供了前所未有的透明度，让你实时见证结论是如何得出的。

通过将复杂的推理拆解为清晰、逻辑严密的步骤，你可以更好地理解并验证 AI 的解题思路。无论你是用于调试学习，还是单纯对 AI 推理感兴趣，思维链可视化都将抽象的思考转化为引人入胜的交互式体验。

[![][back-to-top]](#readme-top)

[![][image-feat-branch]][docs-feat-branch]

### [对话分支（Branching Conversations）][docs-feat-branch]

引入更自然、灵活的 AI 聊天方式。通过对话分支功能，你的讨论可以像人类交流一样向多个方向延伸。你可以从任意消息创建新的对话分支，在探索不同路径的同时保留原始上下文。

提供两种强大模式供你选择：

- **延续模式**：无缝扩展当前讨论，同时保持有价值的上下文信息
- **独立模式**：基于任意历史消息开启全新话题

这一开创性功能将线性对话转化为动态的树状结构，支持对想法进行更深度的探索与更高效的互动。

[![][back-to-top]](#readme-top)

[![][image-feat-artifacts]][docs-feat-artifacts]

### [Artifacts 支持][docs-feat-artifacts]

体验 Claude Artifacts 的强大能力，现已集成至 LobeHub。这一革命性功能拓展了人机交互的边界，实现多样化内容格式的实时创建与可视化展示。

以前所未有的灵活性进行创作与预览：

- 生成并渲染动态 SVG 图形
- 构建并实时呈现交互式 HTML 页面
- 输出多种格式的专业文档

[![][back-to-top]](#readme-top)

[![][image-feat-knowledgebase]][docs-feat-knowledgebase]

### [文件上传 / 知识库][docs-feat-knowledgebase]

LobeHub 支持文件上传与知识库功能。你可以上传各类文件，包括文档、图片、音频和视频，并创建专属知识库，方便用户管理与检索文件。此外，在对话中也可直接调用文件与知识库内容，带来更丰富的交互体验。

<https://github.com/user-attachments/assets/faa8cf67-e743-4590-8bf6-ebf6ccc34175>

> \[!TIP]
>
> 了解更多详情：[📘 LobeHub 知识库上线——从此每一步都算数](https://lobehub.com/blog/knowledge-base)

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-privoder]][docs-feat-provider]

### [多模型服务商支持][docs-feat-provider]

在 LobeHub 的持续演进中，我们深刻认识到多样化模型服务商对满足社区需求的重要性。因此，我们在提供 AI 对话服务时，不再局限于单一厂商，而是全面扩展了对多家模型服务商的支持，为你提供更丰富、更多元的对话选择。

通过这种方式，LobeHub 能够更灵活地适配不同用户的需求，同时也为开发者提供了更广阔的选择空间。

#### 已支持的模型服务商

我们已实现对以下模型服务商的支持：

<!-- PROVIDER LIST -->

<details><summary><kbd>查看更多服务商 (+-10)</kbd></summary>

</details>

> 📊 总计支持服务商数: [<kbd>**0**</kbd>](https://lobechat.com/discover/providers)

 <!-- PROVIDER LIST -->

同时，我们正计划支持更多模型服务商。如果你希望 LobeHub 接入你偏好的服务商，欢迎随时加入我们的 [💬 社区讨论](https://github.com/lobehub/lobehub/discussions/1284)。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-local]][docs-feat-local]

### [本地大语言模型（LLM）支持][docs-feat-local]

为满足用户的特定需求，LobeHub 还支持基于 [Ollama](https://ollama.ai) 的本地模型运行能力，允许你灵活使用自有或第三方开源模型。

> \[!TIP]
>
> 了解更多关于 [📘 LobeHub 中使用 Ollama][docs-usage-ollama] 的详情。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-vision]][docs-feat-vision]

### [视觉识别能力][docs-feat-vision]

LobeHub 现已支持 OpenAI 最新的 [`gpt-4-vision`](https://platform.openai.com/docs/guides/vision) 模型，具备多模态视觉感知能力。你可以轻松上传或拖拽图片至对话框，Agent 将识别图像内容并基于此展开智能对话，打造更聪明、更多元的聊天场景。

该功能开启了全新的交互方式，让交流突破纯文本限制，融入丰富的视觉元素。无论是日常分享照片，还是特定行业的图纸解读，Agent 都能为你提供出色的对话体验。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-tts]][docs-feat-tts]

### [TTS & STT 语音对话][docs-feat-tts]

LobeHub 支持文本转语音（TTS）与语音转文本（STT）技术，使应用能够将文字消息转化为清晰的语音输出，让你能够像与真人交谈一样与我们的对话 Agent 互动。你可以从多种音色中选择与 Agent 搭配的声音。

此外，TTS 为偏好听觉学习或希望在忙碌时接收信息的用户提供了极佳解决方案。在 LobeHub 中，我们精心筛选了多款高品质语音选项（OpenAI Audio、Microsoft Edge Speech），以满足不同地区与文化背景用户的需求。你可以根据个人喜好或特定场景选择最合适的音色，获得个性化的沟通体验。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-t2i]][docs-feat-t2i]

### [文生图功能][docs-feat-t2i]

依托最新的文生图技术，LobeHub 现允许你在与 Agent 的对话中直接调用图像生成工具。借助 [`DALL-E 3`](https://openai.com/dall-e-3)、[`MidJourney`](https://www.midjourney.com/) 和 [`Pollinations`](https://pollinations.ai/) 等 AI 工具的底层能力，Agent 现已能将你的创意转化为可视化图像。

这为你提供了一种更私密、更具沉浸感的创作流程，让视觉叙事无缝融入你与 Agent 的个人对话中。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-plugin]][docs-feat-plugin]

### [插件系统（Function Calling）][docs-feat-plugin]

LobeHub 的插件生态是其核心功能的重要延伸，大幅提升了 LobeHub 助手的实用性与灵活性。

<video controls src="https://github.com/lobehub/lobehub/assets/28616219/f29475a3-f346-4196-a435-41a6373ab9e2" muted="false"></video>

通过利用插件，LobeHub 助手能够获取并处理实时信息，例如搜索网络资讯并向用户提供即时相关的新闻。

此外，这些插件不仅限于新闻聚合，还可扩展至其他实用功能，如快速检索文档、生成图像、从 Bilibili、Steam 等平台获取数据，以及与各类第三方服务进行交互。

> \[!TIP]
>
> 了解更多关于 [📘 插件使用指南][docs-usage-plugin] 的详情。

<!-- PLUGIN LIST -->

| 最新提交                                                                                                             | 描述                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [购物工具](https://lobechat.com/discover/plugin/ShoppingTools)<br/><sup>由 **shoppingtools** 于 **2026-01-12** 提交</sup> | 在 eBay & AliExpress 上搜索商品，查找促销活动与优惠券。获取提示词示例。<br/>`shopping` `e-bay` `ali-express` `coupons`       |
| [SEO 助手](https://lobechat.com/discover/plugin/seo_assistant)<br/><sup>由 **webfx** 于 **2026-01-12** 提交</sup>          | SEO 助手可生成搜索引擎关键词信息，辅助内容创作。<br/>`seo` `keyword`                   |
| [视频字幕](https://lobechat.com/discover/plugin/VideoCaptions)<br/><sup>由 **maila** 于 **2025-12-13** 提交</sup>         | 将 YouTube 链接转换为转录文本，支持提问、创建章节及内容摘要。<br/>`video-to-text` `youtube` |
| [WeatherGPT](https://lobechat.com/discover/plugin/WeatherGPT)<br/><sup>由 **steven-tey** 于 **2025-12-13** 提交</sup>           | 获取指定位置的实时天气信息。<br/>`weather`                                                                          |

> 📊 总计插件数: [<kbd>**40**</kbd>](https://lobechat.com/discover/plugins)

 <!-- PLUGIN LIST -->

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-agent]][docs-feat-agent]

### [Agent 市场（GPTs）][docs-feat-agent]

在 LobeHub Agent 市场中，创作者可以发现一个充满活力与创新精神的社区，汇聚了众多精心设计的 Agent。这些 Agent 不仅在工作场景中发挥重要作用，也为学习过程提供了极大便利。我们的市场不仅是展示平台，更是协作空间。在这里，每个人都可以贡献智慧并分享自己开发的 Agent。

> \[!TIP]
>
> 通过 [🤖/🏪 提交 Agent][submit-agents-link]，你可以轻松将你的创作发布至本平台。
> 重要的是，LobeHub 已建立了一套完善的自动化国际化（i18n）工作流，
> 能够无缝地将你的 Agent 翻译为多语言版本。
> 这意味着无论用户使用何种语言，都能无障碍地体验你的 Agent。

> \[!IMPORTANT]
>
> 我们欢迎所有用户加入这一不断成长的生态，并参与 Agent 的迭代与优化。
> 让我们共同创造更多有趣、实用且创新的 Agent，进一步丰富 Agent 供给的多样性与实用性。

<!-- AGENT LIST -->

| 最新提交                                                                                                                                                                 | 描述                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [海龟汤主持人](https://lobechat.com/discover/assistant/lateral-thinking-puzzle)<br/><sup>由 **[CSY2022](https://github.com/CSY2022)** 于 **2025-06-19** 提交</sup>              | 海龟汤主持人需提供场景、完整故事（事件真相）及关键点（猜对的必要条件）。<br/>`turtle-soup` `reasoning` `interaction` `puzzle` `role-playing` |
| [学术写作助手](https://lobechat.com/discover/assistant/academic-writing-assistant)<br/><sup>由 **[swarfte](https://github.com/swarfte)** 于 **2025-06-17** 提交</sup> | 学术论文写作与正式文档撰写专家<br/>`academic-writing` `research` `formal-style`                                                                                                      |
| [美食评论家🍟](https://lobechat.com/discover/assistant/food-reviewer)<br/><sup>由 **[renhai-lab](https://github.com/renhai-lab)** 于 **2025-06-17** 提交</sup>                | 美食评测专家<br/>`gourmet` `review` `writing`                                                                                                                                                                    |
| [Minecraft 资深开发者](https://lobechat.com/discover/assistant/java-development)<br/><sup>由 **[iamyuuk](https://github.com/iamyuuk)** 于 **2025-06-17** 提交</sup>           | Java 高级开发与 Minecraft 模组、服务器插件开发专家<br/>`development` `programming` `minecraft` `java`                                                                                   |

> 📊 总计 Agent 数: [<kbd>**505**</kbd> ](https://lobechat.com/discover/assistants)

 <!-- AGENT LIST -->

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-database]][docs-feat-database]

### [支持本地 / 远程数据库][docs-feat-database]

LobeHub 同时支持服务端与本地数据库的使用。根据你的需求，你可以选择合适的部署方案：

- **本地数据库**：适合希望对数据拥有更高控制权及注重隐私保护的用户。LobeHub 采用 CRDT（无冲突复制数据类型）技术实现多设备同步。这是一项实验性功能，旨在提供无缝的数据同步体验。
- **服务端数据库**：适合追求便捷使用体验的用户。LobeHub 支持 PostgreSQL 作为服务端数据库。有关配置服务端数据库的详细文档，请访问 [配置服务端数据库](https://lobehub.com/docs/self-hosting/advanced/server-database)。

无论选择哪种数据库方案，LobeHub 都能为你提供卓越的使用体验。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-auth]][docs-feat-auth]

### [支持多用户管理][docs-feat-auth]

LobeHub 支持多用户管理，并提供灵活的用户认证解决方案：

- **Better Auth**：LobeHub 集成了 `Better Auth`，这是一款现代且灵活的认证库，支持多种认证方式，包括 OAuth、邮箱登录、凭证登录、魔法链接等。借助 `Better Auth`，你可以轻松实现用户注册、登录、会话管理、社交登录、多因素认证（MFA）等功能，确保用户数据的安全与隐私。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-pwa]][docs-feat-pwa]

### [渐进式 Web 应用（PWA）][docs-feat-pwa]

我们深刻理解在多设备环境下为用户提供无缝体验的重要性。
因此，我们采用了渐进式 Web 应用（[PWA](https://support.google.com/chrome/answer/9658361)）技术，
这是一种现代 Web 技术标准，将 Web 应用提升至接近原生应用的体验级别。

通过 PWA，LobeHub 可在桌面与移动设备上提供高度优化的用户体验，同时保持高性能特性。
在视觉与交互手感上，我们也进行了精心设计，确保其与原生应用难以区分，
提供流畅的动画、响应式布局，并适配不同设备的屏幕分辨率。

> \[!NOTE]
>
> 如果你不熟悉 PWA 的安装流程，可按照以下步骤将 LobeHub 添加为桌面应用（同样适用于移动设备）：
>
> - 在电脑上启动 Chrome 或 Edge 浏览器。
> - 访问 LobeHub 网页。
> - 点击地址栏右上角的 <kbd>安装</kbd> 图标。
> - 按照屏幕提示完成 PWA 安装。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-mobile]][docs-feat-mobile]

### [移动端适配][docs-feat-mobile]

我们针对移动设备进行了系列优化设计，以提升你的移动端使用体验。目前我们正在持续迭代移动端交互体验，力求实现更流畅、更直观的操作。如果你有任何建议或想法，欢迎通过 GitHub Issues 或 Pull Requests 向我们反馈。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[![][image-feat-theme]][docs-feat-theme]

### [自定义主题][docs-feat-theme]

作为一款面向设计与工程的应用，LobeHub 高度重视用户的个性化体验，
因此引入了灵活多样的主题模式，包括日间使用的亮色模式与夜间使用的暗色模式。
除了切换主题模式外，我们还提供了丰富的色彩定制选项，允许用户根据个人偏好调整应用的主题配色。
无论是偏爱沉稳的深蓝色、活泼的蜜桃粉，还是专业的灰白色，你都能在 LobeHub 中找到适合自己的风格。

> \[!TIP]
>
> 默认配置可智能识别你的系统颜色模式并自动切换主题，确保与操作系统保持视觉一致。
> 对于喜欢手动控制细节的用户，LobeHub 也提供了直观的设置选项，并在对话场景中提供气泡模式与文档模式两种选择。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

### `*` 更多特性

除上述功能外，LobeHub 还拥有更扎实的基础技术底座：

- [x] 💨 **快速部署**：使用 Vercel 平台或 Docker 镜像，只需一键即可完成部署，全程无需复杂配置，1分钟内即可完成。
- [x] 🌐 **自定义域名**：如果你拥有自己的域名，可将其绑定至平台，随时随地通过专属链接访问对话助手。
- [x] 🔒 **隐私保护**：所有数据均存储于用户本地浏览器中，切实保障你的隐私安全。
- [x] 💎 **精致 UI 设计**：精心打磨的界面提供优雅的外观与流畅的交互。支持亮暗主题切换且完美适配移动端。PWA 支持提供更接近原生的体验。
- [x] 🗣️ **丝滑对话体验**：响应迅速，确保对话过程行云流水。全面支持 Markdown 渲染，包括代码高亮、LaTex 公式、Mermaid 流程图等。

</details>

> ✨ LobeHub 持续演进中，更多功能即将上线。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## 🛳 私有化部署（Self Hosting）

LobeHub 提供基于 Vercel、阿里云及 [Docker 镜像][docker-release-link] 的私有化版本。无需任何前置知识，几分钟内即可部署你自己的聊天机器人。

> \[!TIP]
>
> 了解更多关于 [📘 构建你的专属 LobeHub][docs-self-hosting] 的详情。

### `A` 使用 Vercel、Zeabur、Sealos 或阿里云部署

“如果你希望在 Vercel、Zeabur 或阿里云上自行部署此服务，可按照以下步骤操作：

- 准备你的 [OpenAI API Key](https://platform.openai.com/account/api-keys)。
- 点击下方按钮开始部署：直接使用 GitHub 账号登录，并记得在环境变量部分填写 `OPENAI_API_KEY`（必填）。
- 部署完成后即可开始使用。
- 绑定自定义域名（可选）：部分地区 Vercel 分配的域名 DNS 存在污染；绑定自定义域名可实现直连。

<div align="center">

|           使用 Vercel 部署            |                     使用 Zeabur 部署                      |                     使用 Sealos 部署                      |                       使用 RepoCloud 部署                       |                         使用阿里云部署                         |
| :-------------------------------------: | :---------------------------------------------------------: | :---------------------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------------------------: |
| [![][deploy-button-image]][deploy-link] | [![][deploy-on-zeabur-button-image]][deploy-on-zeabur-link] | [![][deploy-on-sealos-button-image]][deploy-on-sealos-link] | [![][deploy-on-repocloud-button-image]][deploy-on-repocloud-link] | [![][deploy-on-alibaba-cloud-button-image]][deploy-on-alibaba-cloud-link] |

</div>

#### 关于 Fork（分叉）操作

Fork 后，请仅保留上游同步动作，并在你的 GitHub 仓库中禁用其他所有 Actions。

#### 保持更新

如果你已按照 README 中的一键部署步骤完成了私有化部署，可能会遇到持续提示“有可用更新”的情况。这是因为 Vercel 默认会创建一个新项目而非 Fork 本仓库，导致无法准确检测上游更新。

> \[!TIP]
>
> 我们建议你使用以下步骤重新部署：[📘 自动同步最新版本][docs-upstream-sync]

<br/>

### `B` 使用 Docker 部署

[![][docker-release-shield]][docker-release-link]
[![][docker-size-shield]][docker-size-link]
[![][docker-pulls-shield]][docker-pulls-link]

我们提供 Docker 镜像，方便你在私有设备上部署 LobeHub 服务。使用以下命令启动 LobeHub 服务：

1. 创建用于存储数据的文件夹

```fish
$ mkdir lobehub-db && cd lobehub-db
```

2. 初始化 LobeHub 基础设施

```fish
bash <(curl -fsSL https://lobe.li/setup.sh)
```

3. 启动 LobeHub 服务

```fish
docker compose up -d
```

> \[!NOTE]
>
> 有关使用 Docker 部署的详细操作说明，请参阅 [📘 Docker 部署指南][docs-docker]

<br/>

### 环境变量配置

本项目提供了一些通过环境变量设置的额外配置项：

| 环境变量             | 是否必填 | 描述                                                                                                                                                               | 示例                                                                                                              |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `OPENAI_API_KEY`     | 是       | 你在 OpenAI 账户页面申请的 API Key                                                                                                                  | `sk-xxxxxx...xxxxxx`                                                                                                 |
| `OPENAI_PROXY_URL`   | 否       | 如果你手动配置了 OpenAI 接口代理，可使用此项覆盖默认的 OpenAI API 请求基础地址                             | `https://api.chatanywhere.cn` 或 `https://aihubmix.com/v1` <br/>默认值为<br/>`https://api.openai.com/v1` |
| `OPENAI_MODEL_LIST`  | 否       | 用于控制模型列表。使用 `+` 添加模型，`-` 隐藏模型，`model_name=display_name` 自定义显示名称，多个配置用逗号分隔。 | `qwen-7b-chat,+glm-6b,-gpt-3.5-turbo`                                                                                |

> \[!NOTE]
>
> 完整的环境变量列表请参阅 [📘 环境变量][docs-env-var]

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## 📦 生态组件

| NPM                               | 仓库                                | 描述                                                                                           | 版本                                    |
| --------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [@lobehub/ui][lobe-ui-link]       | [lobehub/lobe-ui][lobe-ui-github]       | 专为构建 AIGC Web 应用而设计的开源 UI 组件库。                         | [![][lobe-ui-shield]][lobe-ui-link]       |
| [@lobehub/icons][lobe-icons-link] | [lobehub/lobe-icons][lobe-icons-github] | 热门 AI / LLM 模型品牌 SVG Logo 与图标合集。                                            | [![][lobe-icons-shield]][lobe-icons-link] |
| [@lobehub/tts][lobe-tts-link]     | [lobehub/lobe-tts][lobe-tts-github]     | 高质量且可靠的 TTS/STT React Hooks 库                                                   | [![][lobe-tts-shield]][lobe-tts-link]     |
| [@lobehub/lint][lobe-lint-link]   | [lobehub/lobe-lint][lobe-lint-github]   | LobeHub 的 ESlint、Stylelint、Commitlint、Prettier、Remark 及 Semantic Release 配置。 | [![][lobe-lint-shield]][lobe-lint-link]   |

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## 🧩 插件开发

插件为扩展 LobeHub 的 [Function Calling][docs-function-call] 能力提供了途径。它们可用于引入新的函数调用，甚至全新的消息结果渲染方式。如果你对插件开发感兴趣，请参阅 Wiki 中的 [📘 插件开发指南][docs-plugin-dev]。

- [lobe-chat-plugins][lobe-chat-plugins]: LobeHub 的插件索引仓库。通过读取此仓库的 index.json 文件，向用户展示可用的 LobeHub 插件列表。
- [chat-plugin-template][chat-plugin-template]: LobeHub 插件开发的模板项目。
- [@lobehub/chat-plugin-sdk][chat-plugin-sdk]: LobeHub 插件 SDK，协助你为 LobeHub 打造卓越的聊天插件。
- [@lobehub/chat-plugins-gateway][chat-plugins-gateway]: LobeHub 插件网关后端服务，为插件提供统一接入点。该服务部署于 Vercel。核心 API `POST /api/v1/runner` 已作为边缘函数（Edge Function）发布。

> \[!NOTE]
>
> 插件系统目前正处于重大开发阶段。你可通过以下 Issue 了解更多进展：
>
> - [x] [**插件第一阶段**](https://github.com/lobehub/lobehub/issues/73): 实现插件与主程序分离，将插件拆分为独立仓库维护，并实现动态加载机制。
> - [x] [**插件第二阶段**](https://github.com/lobehub/lobehub/issues/97): 提升插件使用的安全性与稳定性，更精准地呈现异常状态，优化架构可维护性并对开发者更加友好。
> - [x] [**插件第三阶段**](https://github.com/lobehub/lobehub/issues/149): 提供更高级、更全面的自定义能力，支持插件认证机制并提供示例代码。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## ⌨️ 本地开发

你可以使用 GitHub Codespaces 进行在线开发：

[![][codespaces-shield]][codespaces-link]

或克隆至本地进行开发：

```fish
$ git clone https://github.com/lobehub/lobehub.git
$ cd lobehub
$ pnpm install
$ pnpm dev          # 全栈启动（Next.js + Vite SPA）
$ bun run dev:spa   # 仅前端 SPA（端口 9876）
```

> **调试代理**：运行 `dev:spa` 后，终端会打印一个代理 URL，例如
> `https://app.lobehub.com/_dangerous_local_dev_proxy?debug-host=http%3A%2F%2Flocalhost%3A9876`。
> 打开该链接即可在本地开发环境中对接生产后端并启用 HMR（热更新）。

如需了解更多细节，欢迎查阅我们的 [📘 开发指南][docs-dev-guide]。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## 🤝 贡献指南

我们热烈欢迎各种类型的代码与文档贡献；如果你有兴趣参与代码贡献，请随时查看 GitHub 上的 [Issues][github-issues-link] 和 [Projects][github-project-link]，直接上手展示你的实力。

> \[!TIP]
>
> 我们正在打造一个技术驱动的社区，促进知识互动与思想交流，最终实现相互启发与协同创新。
>
> 帮助我们让 LobeHub 变得更好。欢迎直接向我们提供产品设计反馈、用户体验讨论。
>
> **核心维护者**：[@arvinxx](https://github.com/arvinxx) [@canisminor1990](https://github.com/canisminor1990)

[![][pr-welcome-shield]][pr-welcome-link]
[![][submit-agents-shield]][submit-agents-link]
[![][submit-plugin-shield]][submit-plugin-link]

<a href="https://github.com/lobehub/lobehub/graphs/contributors" target="_blank">
  <table>
    <tr>
      <th colspan="2">
        <br><img src="https://contrib.rocks/image?repo=lobehub/lobehub"><br><br>
      </th>
    </tr>
    <tr>
      <td>
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?activity=active&period=past_28_days&owner_id=131470832&repo_ids=643445235&image_size=2x3&color_scheme=dark">
          <img src="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?activity=active&period=past_28_days&owner_id=131470832&repo_ids=643445235&image_size=2x3&color_scheme=light">
        </picture>
      </td>
      <td rowspan="2">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-org-participants-growth/thumbnail.png?activity=active&period=past_28_days&owner_id=131470832&repo_ids=643445235&image_size=4x7&color_scheme=dark">
          <img src="https://next.ossinsight.io/widgets/official/compose-org-participants-growth/thumbnail.png?activity=active&period=past_28_days&owner_id=131470832&repo_ids=643445235&image_size=4x7&color_scheme=light">
        </picture>
      </td>
    </tr>
    <tr>
      <td>
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?activity=new&period=past_28_days&owner_id=131470832&repo_ids=643445235&image_size=2x3&color_scheme=dark">
          <img src="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?activity=new&period=past_28_days&owner_id=131470832&repo_ids=643445235&image_size=2x3&color_scheme=light">
        </picture>
      </td>
    </tr>
  </table>
</a>

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## ❤️ 赞助支持

每一份贡献都弥足珍贵，你的单次捐赠将在我们的支持银河中熠熠生辉！你是划破夜空的流星，为我们的旅程带来迅速而明亮的影响。感谢你对我们使命的信任——你的慷慨将指引我们前行，每一次闪耀都是前进的动力。

<a href="https://opencollective.com/lobehub" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/lobehub/.github/blob/main/static/sponsor-dark.png?raw=true">
    <img  src="https://github.com/lobehub/.github/blob/main/static/sponsor-light.png?raw=true">
  </picture>
</a>

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## 🔗 更多产品

- **[🅰️ Lobe SD Theme][lobe-theme]：** Stable Diffusion WebUI 的现代主题，界面精致、高度可定制且内置提效功能。
- **[⛵️ Lobe Midjourney WebUI][lobe-midjourney-webui]：** Midjourney 的 WebUI 客户端，利用 AI 快速从文本提示词生成丰富多元的图片，激发创意并提升沟通效率。
- **[🌏 Lobe i18n][lobe-i18n] :** 由 ChatGPT 驱动的国际化（i18n）翻译自动化流程工具。支持大文件自动拆分、增量更新及 OpenAI 模型/API 代理/温度等自定义选项。
- **[💌 Lobe Commit][lobe-commit]:** 基于 Langchain/ChatGPT 生成 Gitmoji 风格提交信息的 CLI 工具。

<div align="right">

[![][back-to-top]](#readme-top)

</div>

---

<details><summary><h4>📝 许可证</h4></summary>

[![][fossa-license-shield]][fossa-license-link]

</details>

Copyright © 2026 [LobeHub][profile-link]. <br />
本项目采用 [LobeHub Community License](./LICENSE) 许可。

<!-- LINK GROUP -->

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square
[blog]: https://lobehub.com/blog
[changelog]: https://lobehub.com/changelog
[chat-plugin-sdk]: https://github.com/lobehub/chat-plugin-sdk
[chat-plugin-template]: https://github.com/lobehub/chat-plugin-template
[chat-plugins-gateway]: https://github.com/lobehub/chat-plugins-gateway
[codecov-link]: https://codecov.io/gh/lobehub/lobehub
[codecov-shield]: https://img.shields.io/codecov/c/github/lobehub/lobehub?labelColor=black&style=flat-square&logo=codecov&logoColor=white
[codespaces-link]: https://codespaces.new/lobehub/lobehub
[codespaces-shield]: https://github.com/codespaces/badge.svg
[deploy-button-image]: https://vercel.com/button
[deploy-link]: https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Flobehub%2Flobehub&env=OPENAI_API_KEY&envDescription=Find%20your%20OpenAI%20API%20Key%20by%20click%20the%20right%20Learn%20More%20button.&envLink=https%3A%2F%2Fplatform.openai.com%2Faccount%2Fapi-keys&project-name=lobehub&repository-name=lobehub
[deploy-on-alibaba-cloud-button-image]: https://service-info-public.oss-cn-hangzhou.aliyuncs.com/computenest-en.svg
[deploy-on-alibaba-cloud-link]: https://computenest.console.aliyun.com/service/instance/create/default?type=user&ServiceName=LobeHub%E7%A4%BE%E5%8C%86%E7%89%88
[deploy-on-repocloud-button-image]: https://d16t0pc4846x52.cloudfront.net/deploylobe.svg
[deploy-on-repocloud-link]: https://repocloud.io/details/?app_id=248
[deploy-on-sealos-button-image]: https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg
[deploy-on-sealos-link]: https://template.usw.sealos.io/deploy?templateName=lobehub-db
[deploy-on-zeabur-button-image]: https://zeabur.com/button.svg
[deploy-on-zeabur-link]: https://zeabur.com/templates/VZGGTI
[discord-link]: https://discord.gg/AYFPHvv2jT
[discord-shield]: https://img.shields.io/discord/1127171173982154893?color=5865F2&label=discord&labelColor=black&logo=discord&logoColor=white&style=flat-square
[discord-shield-badge]: https://img.shields.io/discord/1127171173982154893?color=5865F2&label=discord&labelColor=black&logo=discord&logoColor=white&style=for-the-badge
[docker-pulls-link]: https://hub.docker.com/r/lobehub/lobehub
[docker-pulls-shield]: https://img.shields.io/docker/pulls/lobehub/lobehub?color=45cc11&labelColor=black&style=flat-square&sort=semver
[docker-release-link]: https://hub.docker.com/r/lobehub/lobehub
[docker-release-shield]: https://img.shields.io/docker/v/lobehub/lobehub?color=369eff&label=docker&labelColor=black&logo=docker&logoColor=white&style=flat-square&sort=semver
[docker-size-link]: https://hub.docker.com/r/lobehub/lobehub
[docker-size-shield]: https://img.shields.io/docker/image-size/lobehub/lobehub?color=369eff&labelColor=black&style=flat-square&sort=semver
[docs]: https://lobehub.com/docs/usage/start
[docs-dev-guide]: https://lobehub.com/docs/development/start
[docs-docker]: https://lobehub.com/docs/self-hosting/server-database/docker-compose
[docs-env-var]: https://lobehub.com/docs/self-hosting/environment-variables
[docs-feat-agent]: https://lobehub.com/docs/usage/features/agent-market
[docs-feat-artifacts]: https://lobehub.com/docs/usage/features/artifacts
[docs-feat-auth]: https://lobehub.com/docs/usage/features/auth
[docs-feat-branch]: https://lobehub.com/docs/usage/features/branching-conversations
[docs-feat-cot]: https://lobehub.com/docs/usage/features/cot
[docs-feat-database]: https://lobehub.com/docs/usage/features/database
[docs-feat-knowledgebase]: https://lobehub.com/blog/knowledge-base
[docs-feat-local]: https://lobehub.com/docs/usage/features/local-llm
[docs-feat-mobile]: https://lobehub.com/docs/usage/features/mobile
[docs-feat-plugin]: https://lobehub.com/docs/usage/features/plugin-system
[docs-feat-provider]: https://lobehub.com/docs/usage/features/multi-ai-providers
[docs-feat-pwa]: https://lobehub.com/docs/usage/features/pwa
[docs-feat-t2i]: https://lobehub.com/docs/usage/features/text-to-image
[docs-feat-theme]: https://lobehub.com/docs/usage/features/theme
[docs-feat-tts]: https://lobehub.com/docs/usage/features/tts
[docs-feat-vision]: https://lobehub.com/docs/usage/features/vision
[docs-function-call]: https://lobehub.com/blog/openai-function-call
[docs-plugin-dev]: https://lobehub.com/docs/usage/plugins/development
[docs-self-hosting]: https://lobehub.com/docs/self-hosting/start
[docs-upstream-sync]: https://lobehub.com/docs/self-hosting/advanced/upstream-sync
[docs-usage-ollama]: https://lobehub.com/docs/usage/providers/ollama
[docs-usage-plugin]: https://lobehub.com/docs/usage/plugins/basic
[fossa-license-link]: https://app.fossa.com/projects/git%2Bgithub.com%2Flobehub%2Flobehub
[fossa-license-shield]: https://app.fossa.com/api/projects/git%2Bgithub.com%2Flobehub%2Flobehub.svg?type=large
[github-action-release-link]: https://github.com/actions/workflows/lobehub/lobehub/release.yml
[github-action-release-shield]: https://img.shields.io/github/actions/workflow/status/lobehub/lobehub/release.yml?label=release&labelColor=black&logo=githubactions&logoColor=white&style=flat-square
[github-action-test-link]: https://github.com/actions/workflows/lobehub/lobehub/test.yml
[github-action-test-shield]: https://img.shields.io/github/actions/workflow/status/lobehub/lobehub/test.yml?label=test&labelColor=black&logo=githubactions&logoColor=white&style=flat-square
[github-contributors-link]: https://github.com/lobehub/lobehub/graphs/contributors
[github-contributors-shield]: https://img.shields.io/github/contributors/lobehub/lobehub?color=c4f042&labelColor=black&style=flat-square
[github-forks-link]: https://github.com/lobehub/lobehub/network/members
[github-forks-shield]: https://img.shields.io/github/forks/lobehub/lobehub?color=8ae8ff&labelColor=black&style=flat-square
[github-issues-link]: https://github.com/lobehub/lobehub/issues
[github-issues-shield]: https://img.shields.io/github/issues/lobehub/lobehub?color=ff80eb&labelColor=black&style=flat-square
[github-license-link]: https://github.com/lobehub/lobehub/blob/main/LICENSE
[github-license-shield]: https://img.shields.io/badge/license-apache%202.0-white?labelColor=black&style=flat-square
[github-project-link]: https://github.com/lobehub/lobehub/projects
[github-release-link]: https://github.com/lobehub/lobehub/releases
[github-release-shield]: https://img.shields.io/github/v/release/lobehub/lobehub?color=369eff&labelColor=black&logo=github&style=flat-square
[github-releasedate-link]: https://github.com/lobehub/lobehub/releases
[github-releasedate-shield]: https://img.shields.io/github/release-date/lobehub/lobehub?labelColor=black&style=flat-square
[github-stars-link]: https://github.com/lobehub/lobehub/stargazers
[github-stars-shield]: https://img.shields.io/github/stars/lobehub/lobehub?color=ffcb47&labelColor=black&style=flat-square
[github-trending-shield]: https://trendshift.io/api/badge/repositories/2256
[github-trending-url]: https://trendshift.io/repositories/2256
[image-banner]: https://github.com/user-attachments/assets/0fe626a3-0ddc-4f67-b595-3c5b3f1701e0
[image-feat-agent]: https://github.com/user-attachments/assets/b3ab6e35-4fbc-468d-af10-e3e0c687350f
[image-feat-artifacts]: https://github.com/user-attachments/assets/7f95fad6-b210-4e6e-84a0-7f39e96f3a00
[image-feat-auth]: https://github.com/user-attachments/assets/80bb232e-19d1-4f97-98d6-e291f3585e6d
[image-feat-branch]: https://github.com/user-attachments/assets/92f72082-02bd-4835-9c54-b089aad7fd41
[image-feat-cot]: https://github.com/user-attachments/assets/f74f1139-d115-4e9c-8c43-040a53797a5e
[image-feat-database]: https://github.com/user-attachments/assets/f1697c8b-d1fb-4dac-ba05-153c6295d91d
[image-feat-desktop]: https://github.com/user-attachments/assets/a7bac8d3-ea96-4000-bb39-fadc9b610f96
[image-feat-knowledgebase]: https://github.com/user-attachments/assets/7da7a3b2-92fd-4630-9f4e-8560c74955ae
[image-feat-local]: https://github.com/user-attachments/assets/1239da50-d832-4632-a7ef-bd754c0f3850
[image-feat-mcp]: https://github.com/user-attachments/assets/1be85d36-3975-4413-931f-27e05e440995
[image-feat-mcp-market]: https://github.com/user-attachments/assets/bb114f9f-24c5-4000-a984-c10d187da5a0
[image-feat-mobile]: https://github.com/user-attachments/assets/32cf43c4-96bd-4a4c-bfb6-59acde6fe380
[image-feat-plugin]: https://github.com/user-attachments/assets/66a891ac-01b6-4e3f-b978-2eb07b489b1b
[image-feat-privoder]: https://github.com/user-attachments/assets/e553e407-42de-4919-977d-7dbfcf44a821
[image-feat-pwa]: https://github.com/user-attachments/assets/9647f70f-b71b-43b6-9564-7cdd12d1c24d
[image-feat-t2i]: https://github.com/user-attachments/assets/708274a7-2458-494b-a6ec-b73dfa1fa7c2
[image-feat-theme]: https://github.com/user-attachments/assets/b47c39f1-806f-492b-8fcb-b0fa973937c1
[image-feat-tts]: https://github.com/user-attachments/assets/50189597-2cc3-4002-b4c8-756a52ad5c0a
[image-feat-vision]: https://github.com/user-attachments/assets/18574a1f-46c2-4cbc-af2c-35a86e128a07
[image-feat-web-search]: https://github.com/user-attachments/assets/cfdc48ac-b5f8-4a00-acee-db8f2eba09ad
[image-star]: https://github.com/user-attachments/assets/3216e25b-186f-4a54-9cb4-2f124aec0471
[issues-link]: https://img.shields.io/github/issues/lobehub/lobehub.svg?style=flat
[lobe-chat-plugins]: https://github.com/lobehub/lobe-chat-plugins
[lobe-commit]: https://github.com/lobehub/lobe-commit/tree/master/packages/lobe-commit
[lobe-i18n]: https://github.com/lobehub/lobe-commit/tree/master/packages/lobe-i18n
[lobe-icons-github]: https://github.com/lobehub/lobe-icons
[lobe-icons-link]: https://www.npmjs.com/package/@lobehub/icons
[lobe-icons-shield]: https://img.shields.io/npm/v/@lobehub/icons?color=369eff&labelColor=black&logo=npm&logoColor=white&style=flat-square
[lobe-lint-github]: https://github.com/lobehub/lobe-lint
[lobe-lint-link]: https://www.npmjs.com/package/@lobehub/lint
[lobe-lint-shield]: https://img.shields.io/npm/v/@lobehub/lint?color=369eff&labelColor=black&logo=npm&logoColor=white&style=flat-square
[lobe-midjourney-webui]: https://github.com/lobehub/lobe-midjourney-webui
[lobe-theme]: https://github.com/lobehub/sd-webui-lobe-theme
[lobe-tts-github]: https://github.com/lobehub/lobe-tts
[lobe-tts-link]: https://www.npmjs.com/package/@lobehub/tts
[lobe-tts-shield]: https://img.shields.io/npm/v/@lobehub/tts?color=369eff&labelColor=black&logo=npm&logoColor=white&style=flat-square
[lobe-ui-github]: https://github.com/lobehub/lobe-ui
[lobe-ui-link]: https://www.npmjs.com/package/@lobehub/ui
[lobe-ui-shield]: https://img.shields.io/npm/v/@lobehub/ui?color=369eff&labelColor=black&logo=npm&logoColor=white&style=flat-square
[official-site]: https://lobehub.com
[pr-welcome-link]: https://github.com/lobehub/lobehub/pulls
[pr-welcome-shield]: https://img.shields.io/badge/🤯_pr_welcome-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge
[profile-link]: https://github.com/lobehub
[share-linkedin-link]: https://linkedin.com/feed
[share-linkedin-shield]: https://img.shields.io/badge/-share%20on%20linkedin-black?labelColor=black&logo=linkedin&logoColor=white&style=flat-square
[share-mastodon-link]: https://mastodon.social/share?text=Check%20this%20GitHub%20repository%20out%20%F0%9F%A4%AF%20LobeHub%20-%20An%20open-source,%20extensible%20%28Function%20Calling%29,%20high-performance%20chatbot%20framework.%20It%20supports%20one-click%20free%20deployment%20of%20your%20private%20ChatGPT%2FLLM%20web%20application.%20https://github.com/lobehub/lobehub%20#chatbot%20#chatGPT%20#openAI
[share-mastodon-shield]: https://img.shields.io/badge/-share%20on%20mastodon-black?labelColor=black&logo=mastodon&logoColor=white&style=flat-square
[share-reddit-link]: https://www.reddit.com/submit?title=Check%20this%20GitHub%20repository%20out%20%F0%9F%A4%AF%20LobeHub%20-%20An%20open-source%2C%20extensible%20%28Function%20Calling%29%2C%20high-performance%20chatbot%20framework.%20It%20supports%20one-click%20free%20deployment%20of%20your%20private%20ChatGPT%2FLLM%20web%20application.%20%23chatbot%20%23chatGPT%20%23openAI&url=https%3A%2F%2Fgithub.com%2Flobehub%2Flobehub
[share-reddit-shield]: https://img.shields.io/badge/-share%20on%20reddit-black?labelColor=black&logo=reddit&logoColor=white&style=flat-square
[share-telegram-link]: https://t.me/share/url"?text=Check%20this%20GitHub%20repository%20out%20%F0%9F%A4%AF%20LobeHub%20-%20An%20open-source%2C%20extensible%20%28Function%20Calling%29,%20high-performance%20chatbot%20framework.%20It%20supports%20one-click%20free%20deployment%20of%20your%20private%20ChatGPT%2FLLM%20web%20application.%20%23chatbot%20%23chatGPT%20%23openAI&url=https%3A%2F%2Fgithub.com%2Flobehub%2Flobehub
[share-telegram-shield]: https://img.shields.io/badge/-share%20on%20telegram-black?labelColor=black&logo=telegram&logoColor=white&style=flat-square
[share-weibo-link]: http://service.weibo.com/share/share.php?sharesource=weibo&title=Check%20this%20GitHub%20repository%20out%20%F0%9F%A4%AF%20LobeHub%20-%20An%20open-source,%20extensible%20%28Function%20Calling%29,%20high-performance%20chatbot%20framework.%20It%20supports%20one-click%20free%20deployment%20of%20your%20private%20ChatGPT%2FLLM%20web%20application.%20%23chatbot%20%23chatGPT%20%23openAI&url=https%3A%2F%2Fgithub.com%2Flobehub%2Flobehub
[share-weibo-shield]: https://img.shields.io/badge/-share%20on%20weibo-black?labelColor=black&logo=sinaweibo&logoColor=white&style=flat-square
[share-whatsapp-link]: https://api.whatsapp.com/send?text=Check%20this%20GitHub%20repository%20out%20%F0%9F%A4%AF%20LobeHub%20-%20An%20open-source,%20extensible%20%28Function%20Calling%29,%20high-performance%20chatbot%20framework.%20It%20supports%20one-click%20free%20deployment%20of%20your%20private%20ChatGPT%2FLLM%20web%20application.%20https%3A%2F%2Fgithub.com%2Flobehub%2Flobehub%20%23chatbot%20%23chatGPT%20%23openAI
[share-whatsapp-shield]: https://img.shields.io/badge/-share%20on%20whatsapp-black?labelColor=black&logo=whatsapp&logoColor=white&style=flat-square
[share-x-link]: https://x.com/intent/tweet?hashtags=chatbot%2CchatGPT%2CopenAI&text=Check%20this%20GitHub%20repository%20out%20%F0%9F%A4%AF%20LobeHub%20-%20An%20open-source,%20extensible%20%28Function%20Calling%29,%20high-performance%20chatbot%20framework.%20It%20supports%20one-click%20free%20deployment%20of%20your%20private%20ChatGPT%2FLLM%20web%20application.&url=https%3A%2F%2Fgithub.com%2Flobehub%2Flobehub
[share-x-shield]: https://img.shields.io/badge/-share%20on%20x-black?labelColor=black&logo=x&logoColor=white&style=flat-square
[sponsor-link]: https://opencollective.com/lobehub 'Become ❤️ LobeHub Sponsor'
[sponsor-shield]: https://img.shields.io/badge/-Sponsor%20LobeHub-f04f88?logo=opencollective&logoColor=white&style=flat-square
[submit-agents-link]: https://github.com/lobehub/lobe-chat-agents
[submit-agents-shield]: https://img.shields.io/badge/🤖/🏪_submit_agent-%E2%86%92-c4f042?labelColor=black&style=for-the-badge
[submit-plugin-link]: https://github.com/lobehub/lobe-chat-plugins
[submit-plugin-shield]: https://img.shields.io/badge/🧩/🏪_submit_plugin-%E2%86%92-95f3d9?labelColor=black&style=for-the-badge
[vercel-link]: https://app.lobehub.com
[vercel-shield]: https://img.shields.io/badge/vercel-online-55b467?labelColor=black&logo=vercel&style=flat-square