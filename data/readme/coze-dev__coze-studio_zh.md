![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/943f576df3424fa98580c2ad18946719~tplv-goo7wpa0wc-image.image)

<div align="center"><p>
<a href="#what-is-coze-studio">Coze Studio</a> •
<a href="#feature-list">功能特性列表</a> •
<a href="#quickstart">快速入门</a> •
<a href="#developer-guide">开发者指南</a>
</p>
<p>
  <img alt="License" src="https://img.shields.io/badge/license-apache2.0-blue.svg">
  <img alt="Go Version" src="https://img.shields.io/badge/go-%3E%3D%201.23.4-blue">
</p>

English | [中文](README.zh_CN.md)

</div>

## What is Coze Studio?

[Coze Studio](https://www.coze.cn/home) 是一款集大成的 AI Agent（智能体）开发工具。它提供最新的大模型与工具、多种开发模式与框架，为开发者打造从开发到部署最便捷的 AI Agent 开发生态环境。 

* **提供 AI Agent 开发所需的全部核心技术**：提示词（prompt）、检索增强生成（RAG）、插件、工作流，让开发者专注于创造 AI 的核心价值。
* **以最低成本实现开箱即用的专业级 AI Agent 开发**：Coze Studio 为开发者提供完整的应用模板与构建框架，助你快速搭建各类 AI Agent，将创意变为现实。

Coze Studio 源自已服务数万家企业与数百万开发者的“扣子（Coze）开放平台”，我们将其核心引擎完全开源。作为一款一站式可视化 AI Agent 开发工具，它让创建、调试和部署 AI Agent 变得前所未有的简单。通过 Coze Studio 的可视化设计与构建工具，开发者可以以无代码或低代码的方式快速创建与调试 Agent、应用和工作流，实现强大的 AI 应用开发与高度定制化的业务逻辑。它是打造定制化低代码 AI 产品的理想选择。Coze Studio 旨在降低 AI Agent 的开发与应用门槛，鼓励社区共建共享，推动 AI 领域的深度探索与实践。

Coze Studio 后端采用 Golang 开发，前端使用 React + TypeScript，整体架构基于微服务设计，并遵循领域驱动设计（DDD）原则构建。我们为开发者提供高性能、高可扩展且易于定制的底层框架，助力应对复杂的业务需求。

## Feature list
| **模块** | **功能特性** |
| --- | --- |
| 模型服务 | 管理模型列表，集成 OpenAI、火山引擎（Volcengine）等服务 |
| 构建 Agent | * 创建、发布与管理 Agent <br> * 支持配置工作流、知识库等资源 |
| 构建应用 | * 创建并发布应用 <br> * 通过工作流构建业务逻辑 |
| 构建工作流 | 创建、修改、发布和删除工作流 |
| 开发资源 | 支持创建与管理以下资源：<br> * 插件<br> * 知识库<br> * 数据库<br> * 提示词（Prompts） |
| API 与 SDK | * 创建会话、发起对话等 OpenAPI <br> * 通过 Chat SDK 将 Agent 或应用集成至自有应用中 |

## Quickstart
了解如何获取并部署 Coze Studio 开源版本，快速搭建项目并体验其功能。

环境要求：

* 安装前请确保您的机器满足以下最低系统配置要求：2核 CPU、4GB 内存
* 预装 Docker 和 Docker Compose，并启动 Docker 服务。

部署步骤：

1. 获取源代码。
   ```Bash
   # Clone code
   git clone https://github.com/coze-dev/coze-studio.git
   ```
2. 部署并启动服务。首次部署和启动 Coze Studio 时，拉取镜像与构建本地镜像可能需要一些时间，请耐心等待。若看到 "Container coze-server Started" 提示，表示 Coze Studio 服务已成功启动。

   ```Bash
   cd coze-studio
   # start service
   # for macOS or Linux
   make web  
   # for windows
   cp ./docker/.env.example ./docker/.env
   docker compose -f ./docker/docker-compose.yml up
   ```

   关于常见的启动失败问题，**请参阅 [FAQ](https://github.com/coze-dev/coze-studio/wiki/9.-FAQ)**。
3.	访问 `http://localhost:8888/sign` 注册账号，输入用户名和密码后点击“Register”按钮完成注册。
4.	在 `http://localhost:8888/admin/#model-management` 配置模型，添加新模型。（镜像版本需大于等于 0.5.0。）
5.	访问 `http://localhost:8888/` 即可使用 Coze Studio。

> [!WARNING]
> 若要在公网环境中部署 Coze Studio，建议在操作前评估安全风险并采取相应的防护措施。潜在的安全风险包括账号注册功能、工作流代码节点中的 Python 执行环境、Coze Server 监听地址配置、SSRF（服务器端请求伪造）以及 API 中存在的某些水平越权问题。更多详情请参阅 [快速入门](https://github.com/coze-dev/coze-studio/wiki/2.-Quickstart#security-risks-in-public-networks)。

## Developer Guide

* **项目配置**：
   * [模型配置](https://github.com/coze-dev/coze-studio/wiki/3.-Model-configuration)：部署 Coze Studio 开源版本前，必须完成模型服务配置。否则在构建 Agent、工作流和应用时将无法选择模型。
   * [插件配置](https://github.com/coze-dev/coze-studio/wiki/4.-Plugin-Configuration)：若要使用插件商店中的官方插件，需先完成插件配置并添加第三方服务的认证密钥（Authentication Keys）。
   * [基础组件配置](https://github.com/coze-dev/coze-studio/wiki/5.-Basic-component-configuration)：了解如何配置图片上传器等基础组件，以便在 Coze Studio 中启用图片上传等功能。
* [API 参考](https://github.com/coze-dev/coze-studio/wiki/6.-API-Reference)：Coze Studio 社区版的 API 与 Chat SDK 采用个人访问令牌（Personal Access Token）进行认证，提供会话与工作流相关的接口。
* [开发规范](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards)：
   * [项目架构](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards#project-architecture)：了解 Coze Studio 开源版本的技术架构与核心组件。
   * [代码开发与测试](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards#code-development-and-testing)：学习如何基于 Coze Studio 开源版本进行二次开发与测试。
   * [问题排查](https://github.com/coze-dev/coze-studio/wiki/7.-Development-Standards#troubleshooting)：掌握查看容器状态与系统日志的方法。

## Using the open-source version of Coze Studio
> 关于如何使用 Coze Studio，请参阅 [扣子开放平台官方文档中心](https://www.coze.cn/open/docs) 获取更多信息。请注意，部分功能（如语气定制）仅限商业版使用。开源版与商业版的差异详见 **功能特性列表**。


* [快速入门](https://www.coze.cn/open/docs/guides/quickstart)：使用 Coze Studio 快速构建 AI 助手 Agent。
* [开发 Agent](https://www.coze.cn/open/docs/guides/agent_overview)：学习如何创建、构建、发布和管理 Agent。你可以利用知识库、插件等功能解决模型幻觉及专业领域知识不足的问题。此外，Coze Studio 提供了丰富的记忆功能，使 Agent 能够在交互过程中基于特定用户的历史对话生成更准确的回复。
* [开发工作流](https://www.coze.cn/open/docs/guides/workflow)：工作流是一套用于实现业务逻辑或完成特定任务的指令集合，它结构化地管理应用或 Agent 的数据流与任务处理流程。Coze Studio 提供可视化画布，你可通过拖拽节点快速构建工作流。
* [插件等资源](https://www.coze.cn/open/docs/guides/plugin)：在 Coze Studio 中，工作流、插件、数据库、知识库和变量统称为资源（Resources）。
* **API 与 SDK**：Coze Studio 支持 [聊天与工作流相关 API](https://github.com/coze-dev/coze-studio/wiki/6.-API-Reference)，你还可以通过 [Chat SDK](https://www.coze.cn/open/docs/developer_guides/web_sdk_overview) 将 Agent 或应用集成到本地业务系统中。
* [实践教程](https://www.coze.cn/open/docs/tutorial/chat_sdk_web_online_customer_service)：学习如何使用 Coze Studio 实现各类 AI 场景，例如通过 Chat SDK 构建基于 Web 的在线客服系统。

## License
本项目采用 Apache 2.0 许可证。详情请参阅 [LICENSE](https://github.com/coze-dev/coze-studio/blob/main/LICENSE-APACHE) 文件。

## Community contributions
我们欢迎社区贡献。关于贡献指南，请参阅 [CONTRIBUTING](https://github.com/coze-dev/coze-studio/blob/main/CONTRIBUTING.md) 和 [行为准则](https://github.com/coze-dev/coze-studio/blob/main/CODE_OF_CONDUCT.md)。期待你的贡献！

## Security and privacy
如果你发现项目存在潜在的安全问题，或认为可能发现了安全漏洞，请通过我们的 [安全中心](https://security.bytedance.com/src) 或 [漏洞报告邮箱](mailto:sec@bytedance.com) 通知字节跳动安全团队。
请**不要**创建公开的 GitHub Issue。

## Join Community

我们致力于打造一个开放、友好的开发者社区。所有对 AI Agent 开发感兴趣的开发者都欢迎加入！

### 🐛 Issue Reports & Feature Requests
为高效追踪并解决问题，同时确保透明与协作，我们建议通过以下方式参与：
- **GitHub Issues**：[提交 Bug 报告或功能请求](https://github.com/coze-dev/coze-studio/issues)
- **Pull Requests**：[贡献代码或改进文档](https://github.com/coze-dev/coze-studio/pulls)

### 💬 Technical Discussion & Communication
加入我们的技术交流群，与其他开发者分享经验，并随时了解项目的最新动态：

**飞书群组**  
使用飞书手机 App 扫描下方二维码即可加入：

![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0a49081e8f3743e8bf3dcdded4bb571a~tplv-goo7wpa0wc-image.image)

**Discord 服务器**  
点击链接加入：[Coze Community](https://discord.gg/sTVN9EVS4B)

**Telegram 群组**  
点击链接加入：Telegram 群组 [Coze](https://t.me/+pP9CkPnomDA0Mjgx)

## Acknowledgments
感谢所有为 Coze Studio 项目做出贡献的开发者与社区成员。特别致谢：

* **[Eino](https://github.com/cloudwego/eino)** 框架团队：为 Coze Studio 的 Agent 与工作流运行时引擎、模型抽象与实现、知识库索引与检索提供强力支持
* **[FlowGram](https://github.com/bytedance/flowgram.ai)** 团队：为 Coze Studio 前端工作流画布编辑器提供高质量的工作流构建引擎
* **[Hertz](https://github.com/cloudwego/hertz)** 团队：高性能、强扩展性的 Go HTTP 微服务框架
* 所有参与测试与反馈的用户