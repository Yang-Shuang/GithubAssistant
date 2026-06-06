# GraphRAG

👉 [微软研究博客文章](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/) <br/>
👉 [阅读文档](https://microsoft.github.io/graphrag) <br/>
👉 [GraphRAG 论文 (ArXiv)](https://arxiv.org/pdf/2404.16130)

<div align="left">
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/graphrag">
  </a>
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/issues">
    <img alt="GitHub Issues" src="https://img.shields.io/github/issues/microsoft/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/discussions">
    <img alt="GitHub Discussions" src="https://img.shields.io/github/discussions/microsoft/graphrag">
  </a>
</div>

## 概述

GraphRAG 项目是一套数据处理管道与转换工具套件，旨在利用大语言模型（LLM）的能力，从非结构化文本中提取有意义、结构化的数据。

如需了解更多关于 GraphRAG 的信息，以及它如何增强你的大语言模型（LLM）对你私有数据进行推理的能力，请访问<a href="https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/" target="_blank">微软研究博客文章</a>。

## 快速入门

要开始使用 GraphRAG 系统，我们建议先尝试[命令行快速入门指南](https://microsoft.github.io/graphrag/get_started/)。

## 项目指引

本仓库展示了一种利用知识图谱记忆结构来增强大语言模型（LLM）输出效果的方法论。请注意，提供的代码仅作为演示用途，并非微软官方正式支持的产品/服务。

⚠️ *警告：GraphRAG 索引构建可能涉及较高的资源消耗与成本，请仔细阅读所有文档以了解相关流程与费用，建议从小规模数据开始尝试。*

## 进阶指南

- 了解我们的贡献规范，请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md)
- 开始开发 _GraphRAG_，请参阅 [DEVELOPING.md](./DEVELOPING.md)
- 加入讨论并在 [GitHub Discussions 标签页](https://github.com/microsoft/graphrag/discussions) 提供反馈！

## Prompt 调优 (Prompt Tuning)

开箱即用地直接使用你的数据运行 _GraphRAG_ 可能无法获得最佳效果。我们强烈建议按照文档中的[提示词调优指南](https://microsoft.github.io/graphrag/prompt_tuning/overview/)对你的 prompt 进行微调。

## 版本管理

关于本项目的版本迭代策略，请参阅[重大变更说明](./breaking-changes.md)。

*在次版本更新之间，请始终运行 `graphrag init --root [path] --force` 以确保你拥有最新的配置格式。若想在主版本更新时避免重新索引历史数据集，请运行提供的迁移笔记本（notebook）。请注意，此操作将覆盖你的现有配置和 prompt，如有必要请先进行备份。*

## 负责任 AI 常见问题解答 (FAQ)

请参阅 [RAI_TRANSPARENCY.md](./RAI_TRANSPARENCY.md)

- [GraphRAG 是什么？](./RAI_TRANSPARENCY.md#what-is-graphrag)
- [GraphRAG 能做什么？](./RAI_TRANSPARENCY.md#what-can-graphrag-do)
- [GraphRAG 的预期用途有哪些？](./RAI_TRANSPARENCY.md#what-are-graphrags-intended-uses)
- [GraphRAG 是如何进行评估的？使用了哪些性能指标？](./RAI_TRANSPARENCY.md#how-was-graphrag-evaluated-what-metrics-are-used-to-measure-performance)
- [GraphRAG 存在哪些局限性？用户在使用系统时如何最大限度地降低这些局限性的影响？](./RAI_TRANSPARENCY.md#what-are-the-limitations-of-graphrag-how-can-users-minimize-the-impact-of-graphrags-limitations-when-using-the-system)
- [哪些操作因素和设置能够确保有效且负责任地使用 GraphRAG？](./RAI_TRANSPARENCY.md#what-operational-factors-and-settings-allow-for-effective-and-responsible-use-of-graphrag)

## 商标声明

本项目可能包含其他项目、产品或服务的商标或徽标。对微软商标或徽标的授权使用须遵循并符合[微软商标与品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。在本项目的修改版本中使用微软商标或徽标不得引起混淆，也不得暗示微软的赞助关系。任何第三方商标或徽标的使用均受该第三方政策的约束。

## 隐私政策

[微软隐私声明](https://privacy.microsoft.com/en-us/privacystatement)