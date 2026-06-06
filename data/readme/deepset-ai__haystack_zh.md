<div align="center">
  <a href="https://haystack.deepset.ai/"><img src="https://raw.githubusercontent.com/deepset-ai/haystack/main/images/banner.png" alt="蓝色横幅，带有 Haystack 标志和文字‘haystack by deepset – 面向生产级 RAG 与 Agent 的开源 AI 框架’，周围环绕着代表搜索、文档、Agent、管道（pipeline）和云系统的抽象图标。"></a>

|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CI/CD   | [![Tests](https://github.com/deepset-ai/haystack/actions/workflows/tests.yml/badge.svg)](https://github.com/deepset-ai/haystack/actions/workflows/tests.yml) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/python/mypy) [![Coverage badge](https://raw.githubusercontent.com/deepset-ai/haystack/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/deepset-ai/haystack/blob/python-coverage-comment-action-data/htmlcov/index.html) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) |
| 文档    | [![Website](https://img.shields.io/website?label=documentation&up_message=online&url=https%3A%2F%2Fdocs.haystack.deepset.ai)](https://docs.haystack.deepset.ai)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 软件包  | [![PyPI](https://img.shields.io/pypi/v/haystack-ai)](https://pypi.org/project/haystack-ai/) ![PyPI - Downloads](https://img.shields.io/pypi/dm/haystack-ai?color=blue&logo=pypi&logoColor=gold) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/haystack-ai?logo=python&logoColor=gold) [![Conda Version](https://img.shields.io/conda/vn/conda-forge/haystack-ai.svg)](https://anaconda.org/conda-forge/haystack-ai) [![GitHub](https://img.shields.io/github/license/deepset-ai/haystack?color=blue)](LICENSE) [![License Compliance](https://github.com/deepset-ai/haystack/actions/workflows/license_compliance.yml/badge.svg)](https://github.com/deepset-ai/haystack/actions/workflows/license_compliance.yml) [![OpenSSF Best Practices](https://www.bestpractices.dev/projects/13067/badge)](https://www.bestpractices.dev/projects/13067)|
| 元数据  | [![Discord](https://img.shields.io/discord/993534733298450452?logo=discord)](https://discord.com/invite/qZxjM4bAHU) [![Twitter Follow](https://img.shields.io/twitter/follow/haystack_ai)](https://twitter.com/haystack_ai)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
</div>

[Haystack](https://haystack.deepset.ai/) 是一个开源的 AI 编排框架，用于使用 Python 构建面向生产环境的大语言模型（LLM）应用。

设计模块化管道（pipeline）和 Agent 工作流，对检索、路由、记忆和生成过程实现明确控制。构建可扩展的 RAG（检索增强生成）系统、多模态应用、语义搜索、问答系统及自主 Agent。所有功能均基于透明架构，让你能够自由实验、深度定制并自信部署。

## 目录

- [安装](#installation)
- [文档](#documentation)
- [功能特性](#features)
- [Haystack Enterprise：支持与平台](#haystack-enterprise-support--platform)
- [遥测数据 (Telemetry)](#telemetry)
- [🖖 社区](#-community)
- [为 Haystack 贡献代码](#contributing-to-haystack)
- [使用 Haystack 的组织](#organizations-using-haystack)


## 安装

通过 `pip` 安装是获取 Haystack 最简单的方式：

```sh
pip install haystack-ai
```

安装夜间构建版本以体验最新功能：
```sh
pip install --pre haystack-ai
```

Haystack 支持多种安装方式，包括 Docker 镜像。如需完整指南，请参阅[文档](https://docs.haystack.deepset.ai/docs/installation)。

## 文档

如果你是初次接触该项目，建议先阅读[“什么是 Haystack？”](https://haystack.deepset.ai/overview/intro)，然后按照[“快速入门指南”](https://haystack.deepset.ai/overview/quick-start)操作，在几分钟内即可构建你的第一个 LLM 应用。继续通过[教程](https://haystack.deepset.ai/tutorials)深入学习。如需更高级的使用场景或寻找灵感，可以浏览[Cookbook（示例库）](https://haystack.deepset.ai/cookbook)中的 Haystack 代码示例。

随时访问[官方文档](https://docs.haystack.deepset.ai/docs/intro)，深入了解 Haystack、它能为你做什么以及背后的技术原理。

## 功能特性

**专为上下文工程打造**  
设计灵活的系统，在信息到达模型之前，对其检索、排序、过滤、组合、结构化和路由进行明确控制。定义管道和工作流，使检索、记忆、工具和生成过程透明且可追溯。

**模型与供应商中立**  
集成 OpenAI、Mistral、Anthropic、Cohere、Hugging Face、Azure OpenAI、AWS Bedrock、本地模型等。无需重写系统即可自由切换模型或基础设施组件。

**模块化与高度可定制**  
使用内置组件进行检索、索引、工具调用、记忆和评估，或自行创建。添加循环、分支和条件逻辑，精确控制上下文在管道和工作流中的流转方式。

**可扩展的生态系统**  
通过统一的接口构建和分享自定义组件，方便社区成员及第三方轻松扩展 Haystack，共同推动开放生态的发展。

> [!TIP]
> 想要将 Haystack 管道部署为 **REST API** 或 **MCP 服务器**吗？[Hayhooks](https://github.com/deepset-ai/hayhooks) 提供了一种简单的方法，让你能够用自定义逻辑包装管道和 Agent，并通过 HTTP 端点或 MCP 暴露它们。它还支持与 OpenAI 兼容的聊天完成端点，并可配合 [open-webui](https://openwebui.com/) 等聊天界面使用。

## Haystack Enterprise：支持与平台

通过 **Haystack Enterprise Starter** 获取 Haystack 团队的专业支持，使用企业级模板加速开发，并借助云及本地环境的部署指南安全扩展。更多详情请参阅[公告文章](https://haystack.deepset.ai/blog/announcing-haystack-enterprise)。

👉 [获取 Haystack Enterprise Starter](https://www.deepset.ai/products-and-services/haystack-enterprise-starter?utm_source=github.com&utm_medium=referral&utm_campaign=haystack_enterprise)

需要为 Haystack 搭建托管的生产环境？**Haystack Enterprise Platform** 内置可观测性、协作、治理和访问控制功能，助你构建、测试、部署和运行 Haystack 管道。它可作为托管云服务或自托管方案提供。

👉 了解更多关于 [Haystack Enterprise Platform](https://www.deepset.ai/products-and-services/haystack-enterprise-platform?utm_campaign=developer-relations&utm_source=haystack&utm_medium=readme) 的信息，或[免费试用](https://www.deepset.ai/haystack-enterprise-platform-trial?utm_campaign=developer-relations&utm_source=haystack&utm_medium=readme)

## 遥测数据 (Telemetry)

Haystack 会收集管道组件的**匿名**使用统计数据。每次初始化这些组件时，我们都会收到事件通知。借此，我们可以了解哪些组件对社区最为重要。

了解更多关于 Haystack 遥测数据的信息或如何退出收集，请参阅[官方文档](https://docs.haystack.deepset.ai/docs/telemetry)。

## 🖖 社区

如果你有功能需求或发现 Bug，欢迎随时在 [GitHub Issues](https://github.com/deepset-ai/haystack/issues) 中提交。我们会定期检查，通常能迅速回复。如果你想讨论某个话题，或寻求如何让 Haystack 适配你项目的通用建议，可以在 [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) 或我们的 [Discord 频道](https://discord.com/invite/VBpFzsgRVF) 发起讨论。我们也会关注 [𝕏 (Twitter)](https://twitter.com/haystack_ai) 和 [Stack Overflow](https://stackoverflow.com/questions/tagged/haystack)。

## 为 Haystack 贡献代码

我们非常欢迎社区的贡献——无论是修复拼写错误，还是添加全新功能！你不必是 Haystack 专家也能提供有价值的改进。如需了解如何开始，请先查阅我们的[贡献者指南](https://github.com/deepset-ai/haystack/blob/main/CONTRIBUTING.md)。

你可以通过以下几种方式为 Haystack 做出贡献：
- 为主项目贡献代码
- 在 [haystack-core-integrations](https://github.com/deepset-ai/haystack-core-integrations) 贡献集成模块
- 为 [haystack/docs-website](https://github.com/deepset-ai/haystack/tree/main/docs-website) 贡献文档

> [!TIP]
> 👉 **[查看所有可参与贡献的 Issue 列表](https://github.com/orgs/deepset-ai/projects/14)**

## 使用 Haystack 的组织

数千个跨行业的团队正在使用 Haystack 构建生产级 AI 系统，其中包括：

- **科技与 AI 基础设施**：[Apple](https://www.apple.com/)、[Meta](https://www.meta.com/about)、[Databricks](https://www.databricks.com/)、[NVIDIA](https://developer.nvidia.com/blog/reducing-development-time-for-intelligent-virtual-assistants-in-contact-centers/)、[Intel](https://github.com/intel/open-domain-question-and-answer#readme)
- **公共部门 AI 项目**：[欧盟委员会](https://commission.europa.eu/index_en)、[德国联邦研究与技术部 (BMFTR)](https://www.deepset.ai/case-studies/german-federal-ministry-research-technology-space-bmftr)、[巴登-符腾堡州 PD](https://www.pd-g.de/)
- **企业与工业 AI 应用**：[Airbus](https://www.deepset.ai/case-studies/airbus)、[汉莎工业解决方案](https://haystack.deepset.ai/blog/lufthansa-user-story)、[Infineon](https://www.infineon.com/)、[LEGO](https://github.com/larsbaunwall/bricky#readme)、[Comcast](https://arxiv.org/html/2405.00801v2)、[Accenture](https://www.accenture.com/)、[TELUS 农业与消费品部门](https://www.telus.com/agcg/en)
- **知识与内容平台**：[Netflix](https://netflix.com)、[ZEIT Online](https://www.deepset.ai/case-studies/zeit-online)、[Rakuten](https://www.rakuten.com/)、[牛津大学出版社](https://corp.oup.com/)、[Manz](https://www.deepset.ai/case-studies/manz)、[YPulse](https://www.deepset.ai/case-studies/ypulse)


你也在使用 Haystack 吗？欢迎提交 PR，或[告诉我们你的故事](https://forms.gle/Mm3G1aEST3GAH2rn8)