# Agent2Agent (A2A) 协议

[![PyPI - Version](https://img.shields.io/pypi/v/a2a-sdk)](https://pypi.org/project/a2a-sdk)
[![Apache License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
<a href="https://codewiki.google/github.com/a2aproject/a2a">
  <img src="https://www.gstatic.com/_/boq-sdlc-agents-ui/_/r/Mvosg4klCA4.svg" alt="Ask Code Wiki" height="20">
</a>

<div style="text-align: left;">
  <details>
    <summary>🌐 Language</summary>
    <div>
      <div style="text-align: center;">
        <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=en">English</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=zh-CN">简体中文</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=zh-TW">繁體中文</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ja">日本語</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ko">한국어</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=hi">हिन्दी</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=th">ไทย</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=fr">Français</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=de">Deutsch</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=es">Español</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=it">Italiano</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ru">Русский</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=pt">Português</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=nl">Nederlands</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=pl">Polski</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ar">العربية</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=fa">فارسی</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=tr">Türkçe</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=vi">Tiếng Việt</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=id">Bahasa Indonesia</a>
        | <a href="https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=as">অসমীয়া</a>
      </div>
    </div>
  </details>
</div>

<!-- markdownlint-disable MD041 -->
<div style="text-align: center;">
  <div class="centered-logo-text-group">
    <img src="docs/assets/a2a-logo-black.svg" alt="Agent2Agent Protocol Logo" width="100">
    <h1>Agent2Agent (A2A) 协议</h1>
  </div>
</div>

**一个开放协议，旨在实现不透明智能体应用之间的通信与互操作。**

Agent2Agent (A2A) 协议旨在解决人工智能领域的一个关键挑战：使由不同公司基于多种框架构建、运行在独立服务器上的生成式 AI（GenAI）智能体，能够作为真正的“智能体”而非仅仅是工具进行有效通信与协作。A2A 致力于提供一套通用的智能体语言，从而培育一个更加互联、强大且富有创新精神的 AI 生态系统。

借助 A2A，智能体可以实现：

- 发现彼此的能力（capabilities）。
- 协商交互模式（如文本、表单、媒体）。
- 安全地协作处理长周期任务。
- 在不暴露内部状态、记忆或工具的情况下运行。

## DeepLearning.AI 课程

[![A2A DeepLearning.AI](https://img.youtube.com/vi/4gYm0Rp7VHc/maxresdefault.jpg)](https://goo.gle/dlai-a2a)

加入这门由 Google Cloud 和 IBM Research 联合打造、[Holt Skinner](https://github.com/holtskinner)、[Ivan Nardini](https://github.com/inardini) 与 [Sandi Besen](https://github.com/sandijean90) 主讲的关于 [A2A: The Agent2Agent Protocol](https://goo.gle/dlai-a2a) 的短期课程。

**你将学到：**

- **使智能体符合 A2A 标准：** 将使用 Google ADK、LangGraph 或 BeeAI 等框架构建的智能体暴露为 A2A 服务器。
- **连接智能体：** 从零开始创建 A2A 客户端，或使用集成工具连接到符合 A2A 标准的智能体。
- **编排工作流：** 构建由符合 A2A 标准的智能体组成的顺序和层级工作流。
- **多智能体系统：** 使用不同框架构建医疗领域的多智能体系统，并了解 A2A 如何实现协作。
- **A2A 与 MCP：** 学习 A2A 如何通过使智能体相互协作来补充 MCP（模型上下文协议）。

## 为什么选择 A2A？

随着 AI 智能体日益普及，其互操作能力对于构建复杂的多功能应用至关重要。A2A 旨在：

- **打破信息孤岛：** 连接跨不同生态系统的智能体。
- **实现复杂协作：** 允许专业智能体协同处理单个智能体无法独立完成的复杂任务。
- **推动开放标准：** 培育社区驱动的智能体通信方式，鼓励创新与广泛采用。
- **保持不透明性（隐私保护）：** 允许智能体在无需共享内部记忆、专有逻辑或特定工具实现的情况下进行协作，从而提升安全性并保护知识产权。

### 核心特性

- **标准化通信：** 基于 HTTP(S) 的 JSON-RPC 2.0。
- **智能体发现：** 通过包含能力与连接信息的“智能体卡片（Agent Card）”进行发现。
- **灵活交互：** 支持同步请求/响应、流式传输（SSE）以及异步推送通知。
- **丰富的数据交换：** 处理文本、文件及结构化 JSON 数据。
- **企业级就绪：** 专为安全性、身份认证与可观测性设计。

## 快速开始

- 📚 **探索文档：** 访问 [Agent2Agent 协议官方文档站点](https://a2a-protocol.org)，获取完整概览、协议规范全文、教程与指南。
- 📝 **查看规范：** [A2A 协议规范](https://a2a-protocol.org/latest/specification/)
- 使用以下 SDK：
    - [🐍 A2A Python SDK](https://github.com/a2aproject/a2a-python) `pip install a2a-sdk`
    - [🐿️ A2A Go SDK](https://github.com/a2aproject/a2a-go) `go get github.com/a2aproject/a2a-go`
    - [🧑‍💻 A2A JS SDK](https://github.com/a2aproject/a2a-js) `npm install @a2a-js/sdk`
    - [☕️ A2A Java SDK](https://github.com/a2aproject/a2a-java) using maven
    - [🔷 A2A .NET SDK](https://github.com/a2aproject/a2a-dotnet) using [NuGet](https://www.nuget.org/packages/A2A) `dotnet add package A2A`
    - [🦀 A2A Rust SDK](https://github.com/a2aproject/a2a-rs) `cargo add a2a-lf`
- 🎬 使用我们的 [示例](https://github.com/a2aproject/a2a-samples) 查看 A2A 的实际运行效果

## 贡献指南

我们欢迎社区贡献者共同完善和演进 A2A 协议！

- **问题与讨论：** 加入我们的 [GitHub Discussions](https://github.com/a2aproject/A2A/discussions)。
- **问题与建议：** 通过 [GitHub Issues](https://github.com/a2aproject/A2A/issues) 提交问题或改进建议。
- **贡献指南：** 请参阅我们的 [CONTRIBUTING.md](CONTRIBUTING.md)，了解具体的参与方式。
- **私密反馈：** 使用此 [Google 表单](https://goo.gle/a2a-feedback)。
- **合作伙伴计划：** Google Cloud 客户可通过此 [表单](https://goo.gle/a2a-partner) 加入我们的合作伙伴计划。

## 后续规划

### 协议增强

- **智能体发现：**
    - 正式在 `AgentCard` 中集成授权方案及可选凭据的规范。
- **智能体协作：**
    - 探索引入 `QuerySkill()` 方法，用于动态检查未支持或未预期的技能（skills）。
- **任务生命周期与用户体验：**
    - 支持在任务内部进行动态的 UI/UX 协商（例如：智能体在对话中途添加音频或视频功能）。
- **客户端方法与传输层：**
    - 探索将支持范围扩展至客户端发起的方法（超越任务管理范畴）；提升流式传输的可靠性与推送通知机制。

## 关于

A2A 协议是 Linux 基金会旗下的开源项目，由 Google 贡献。该项目采用 [Apache License 2.0](LICENSE) 许可，并欢迎社区贡献者参与开发。