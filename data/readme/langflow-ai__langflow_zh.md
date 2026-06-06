<!-- markdownlint-disable MD030 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./docs/static/img/langflow-logo-color-blue-bg.svg">
  <img src="./docs/static/img/langflow-logo-color-black-solid.svg" alt="Langflow 标志">
</picture>

[![Release Notes](https://img.shields.io/github/release/langflow-ai/langflow?style=flat-square)](https://github.com/langflow-ai/langflow/releases)
[![PyPI - License](https://img.shields.io/badge/license-MIT-orange)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/langflow?style=flat-square)](https://pypistats.org/packages/langflow)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langflow-ai.svg?style=social&label=Follow%20%40Langflow)](https://twitter.com/langflow_ai)
[![YouTube Channel](https://img.shields.io/youtube/channel/subscribers/UCn2bInQrjdDYKEEmbpwblLQ?label=Subscribe)](https://www.youtube.com/@Langflow)
[![Discord Server](https://img.shields.io/discord/1116803230643527710?logo=discord&style=social&label=Join)](https://discord.gg/EqksyE2EX9)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/langflow-ai/langflow)

[Langflow](https://langflow.org) 是一个强大的平台，用于构建和部署由人工智能驱动的代理（agents）和工作流。它为开发者提供了可视化的创作体验以及内置的 API 和 MCP 服务器，将每个工作流转化为可集成到任何框架或技术栈应用中的工具。Langflow 开箱即用，支持所有主流大语言模型（LLM）、向量数据库，并拥有不断增长的 AI 工具库。

## ✨ 核心特性

- **可视化构建界面**，助你快速上手并高效迭代。
- **源码访问权限**，可使用 Python 自定义任意组件。
- **交互式沙盒（Playground）**，提供逐步控制功能，便于即时测试和优化工作流。
- **多代理编排**，支持对话管理与检索。
- **API 部署**或导出为 JSON，方便集成到 Python 应用中。
- **MCP 服务器部署**，将工作流转化为供 MCP 客户端调用的工具。
- **可观测性集成**（LangSmith、LangFuse 等）。
- **企业级安全与可扩展能力**。

## 🖥️ Langflow 桌面版

Langflow 桌面版是上手 Langflow 的最简单方式。所有依赖均已内置，你无需手动管理 Python 环境或安装软件包。支持 Windows 和 macOS 系统。

[📥 下载 Langflow 桌面版](https://www.langflow.org/desktop)

## ⚡️ 快速开始

### 本地安装（推荐）

需要 Python 3.10–3.13 以及 [uv](https://docs.astral.sh/uv/getting-started/installation/)（推荐的包管理器）。

#### 安装

在空目录下运行：
```shell
uv pip install langflow -U
```

已安装最新版本的 Langflow 包。
更多信息，请参阅 [安装并运行 Langflow OSS Python 包](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package)。

#### 启动

要启动 Langflow，请运行：
```shell
uv run langflow run
```

Langflow 将在 http://127.0.0.1:7860 启动。

搞定！你现在可以开始使用 Langflow 进行开发了！🎉

## 📦 其他安装方式

### 从源码运行
如果你已克隆本仓库并希望参与贡献，请在仓库根目录下运行此命令：
```shell
make run_cli
```
更多信息，请参阅 [DEVELOPMENT.md](./DEVELOPMENT.md)。

### Docker
使用默认设置启动 Langflow 容器：
```shell
docker run -p 7860:7860 langflowai/langflow:latest
```
Langflow 可通过 http://localhost:7860/ 访问。
如需配置选项，请参阅 [Docker 部署指南](https://docs.langflow.org/deployment-docker)。

## 🛡️ 安全

有关安全信息，请参阅我们的 [安全策略](./SECURITY.md)。

## 🚀 部署

Langflow 是完全开源的项目，你可将其部署到所有主流云服务提供商。如需了解如何部署 Langflow，请参阅我们的 [Langflow 部署指南](https://docs.langflow.org/deployment-overview)。

## ⭐ 保持更新

在 GitHub 上为 Langflow 点星（Star），以便第一时间获取新版本发布通知。

![Star Langflow](https://github.com/user-attachments/assets/03168b17-a11d-4b2a-b0f7-c1cce69e5a2c)

## 👋 贡献代码

我们欢迎各级开发者参与贡献。如果你想加入，请查阅我们的[贡献指南](./CONTRIBUTING.md)，共同助力 Langflow 的普及与发展。

---

[![Star History Chart](https://api.star-history.com/svg?repos=langflow-ai/langflow&type=Timeline)](https://star-history.com/#langflow-ai/langflow&Date)

## ❤️ 贡献者

[![langflow contributors](https://contrib.rocks/image?repo=langflow-ai/langflow)](https://github.com/langflow-ai/langflow/graphs/contributors)