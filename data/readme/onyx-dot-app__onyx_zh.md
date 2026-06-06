<a name="readme-p"></a>

<h2 align="center">
    <a href="https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme"> <img width="50%" src="https://github.com/onyx-dot-app/onyx/blob/logo/OnyxLogoCropped.jpg?raw=true" /></a>
</h2>

<p align="center">
    <a href="https://discord.gg/TDJ59cGV2X" target="_blank">
        <img src="https://img.shields.io/badge/discord-join-blue.svg?logo=discord&logoColor=white" alt="Discord" />
    </a>
    <a href="https://docs.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme" target="_blank">
        <img src="https://img.shields.io/badge/docs-view-blue" alt="Documentation" />
    </a>
    <a href="https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme" target="_blank">
        <img src="https://img.shields.io/website?url=https://www.onyx.app&up_message=visit&up_color=blue" alt="Documentation" />
    </a>
    <a href="https://github.com/onyx-dot-app/onyx/blob/main/LICENSE" target="_blank">
        <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=blue" alt="License" />
    </a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/12516" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/12516" alt="onyx-dot-app/onyx | Trendshift" style="width: 250px; height: 55px;" />
  </a>
</p>

# Onyx - 开源 AI 平台

**[Onyx](https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)** 是面向大语言模型（LLM）的应用层——提供功能丰富的界面，任何人都可以轻松托管。
Onyx 通过高级能力为 LLM 赋能，包括检索增强生成（RAG）、网页搜索、代码执行、文件创建、深度研究等。

可通过开箱即用的连接器或 MCP 协议连接你的应用，平台内置 50 多种基于索引的连接器。

> [!TIP]
> 一条命令即可部署：
> ```
> curl -fsSL https://onyx.app/install_onyx.sh | bash
> ```

![Onyx Chat Silent Demo](https://github.com/onyx-dot-app/onyx/releases/download/v3.0.0/Onyx.gif)

---

## ⭐ 功能特性

- **🔍 智能体 RAG：** 基于混合索引与 AI 智能体的信息检索，提供业界领先的搜索和问答质量。
  - 📅 基准测试即将发布！
- **🔬 深度研究：** 通过多步骤研究流程，生成详尽的报告。
  - 🏆 截至 2026 年 2 月，位列 [排行榜](https://github.com/onyx-dot-app/onyx_deep_research_bench) 榜首。
- **🤖 自定义智能体：** 构建具有独特指令、知识库和操作能力的 AI 智能体。
- **🌍 网页搜索：** 浏览互联网获取最新资讯。
  - 支持 Serper、Google PSE、Brave、SearXNG 等。
  - 内置自研网络爬虫，并支持 Firecrawl/Exa。
- **📄 工件（Artifacts）：** 生成文档、图表及其他可下载的文件资源。
- **▶️ 操作与 MCP：** 让 Onyx 智能体与外部应用交互，提供灵活的认证选项。
- **💻 代码执行：** 在沙箱中运行代码以分析数据、渲染图表或修改文件。
- **🎙️ 语音模式：** 通过文本转语音和语音转文本与 Onyx 对话。
- **🎨 图像生成：** 根据用户提示词生成图片。

Onyx 支持所有主流大语言模型提供商，包括自托管方案（如 Ollama、LiteLLM、vLLM 等）和闭源商业服务（如 Anthropic、OpenAI、Gemini 等）。

了解更多详情，请参阅我们的[文档](https://docs.onyx.app/welcome?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)！

---

## 🚀 部署模式

> Onyx 支持通过 Docker、Kubernetes、Helm/Terraform 进行部署，并为各大云提供商提供了详细指南。
> 详细的部署指南请查看[此处](https://docs.onyx.app/deployment/overview)。

Onyx 提供两种独立的部署选项：标准版（Standard）和轻量版（Lite）。

#### Onyx 轻量版 (Lite)

轻量版可视为一个精简的聊天界面。它所需的资源更少（内存占用低于 1GB），且架构更简单。
非常适合希望快速体验 Onyx 的用户，或仅关注聊天界面与智能体功能的团队。

#### Onyx 标准版 (Standard)

包含 Onyx 的完整功能集，推荐用于专业用户及大型团队。以下组件未包含在轻量版中：
- 用于 RAG 的向量与关键词索引。
- 后台容器，用于运行作业队列和工作进程，以同步来自连接器的知识数据。
- AI 模型推理服务器，用于运行索引和推理过程中使用的深度学习模型。
- 针对大规模使用场景的性能优化，通过内存缓存（Redis）和对象存储（MinIO）实现。

> [!TIP]  
> **无需部署即可免费体验 Onyx，请访问 [Onyx 云](https://cloud.onyx.app/signup?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)**。

---

## 🏢 企业版 (Enterprise)

Onyx 专为各类团队打造，从个人用户到全球大型跨国企业均可适用：
- 👥 **协作：** 与组织成员共享聊天记录和智能体。
- 🔐 **单点登录（SSO）：** 支持通过 Google OAuth、OIDC 或 SAML 进行认证。通过 SCIM 实现群组同步和用户配置管理。
- 🛡️ **基于角色的访问控制（RBAC）：** 对智能体、操作等敏感资源进行严格的权限管控。
- 📊 **数据分析：** 按团队、大语言模型或智能体维度统计使用数据图表。
- 🕵️ **查询历史：** 审计使用情况，确保组织内安全合规地采用 AI。
- 💻 **自定义代码：** 运行自定义脚本以去除个人身份信息（PII）、拦截敏感查询或执行定制化分析。
- 🎨 **品牌定制（白标）：** 通过自定义名称、图标、横幅等，全面定制 Onyx 的界面外观与风格。

## 📚 许可协议

Onyx 提供两个版本：

- **Onyx 社区版（CE）**：基于 MIT 许可证免费开源，涵盖聊天、RAG、智能体和操作等全部核心功能。
- **Onyx 企业版（EE）**：包含额外的高级功能，主要面向大型组织使用。

有关详细的功能对比，请访问[我们的官网](https://www.onyx.app/pricing?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)。

## 👪 社区

欢迎加入我们在 **[Discord](https://discord.gg/TDJ59cGV2X)** 上的开源社区！

## 💡 贡献指南

想要参与贡献？请查阅[贡献指南](CONTRIBUTING.md)了解更多详情。