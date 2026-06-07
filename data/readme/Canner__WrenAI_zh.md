<div align="center" id="top">
<a href="https://getwren.ai">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./misc/wrenai_logo_white.png">
    <img src="./misc/wrenai_logo.png" width="300px" alt="WrenAI">
  </picture>
</a>

### AI Agent 处理业务数据的开放上下文层（Open Context Layer）

*你的 Agent 并不了解你数据的含义。我们解决这个问题。*

[Docs](https://docs.getwren.ai) · [Discord](https://discord.gg/5DvshJqG8Z) · [Vision](https://www.getwren.ai/post/the-missing-context-layer-for-ai-agents-over-business-data) · [Blog](https://www.getwren.ai/blog)

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/wrenai?label=wrenai)](https://pypi.org/project/wrenai/)
[![GitHub Release](https://img.shields.io/github/v/release/Canner/WrenAI?logo=github&label=release)](https://github.com/Canner/WrenAI/releases)
[![Discord](https://img.shields.io/discord/1227143286951514152?logo=discord&label=Discord)](https://discord.gg/5DvshJqG8Z)
[![Last commit](https://img.shields.io/github/last-commit/Canner/WrenAI)](https://github.com/Canner/WrenAI/commits/main)
[![Follow on X](https://img.shields.io/badge/follow-@getwrenai-blue?logo=x&logoColor=white)](https://x.com/getwrenai)
[![Made by Canner](https://img.shields.io/badge/made_by-Canner-blue)](https://cannerdata.com)
![Stars](https://img.shields.io/github/stars/Canner/WrenAI?style=social)

<a href="https://trendshift.io/repositories/9263" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9263" alt="Canner/WrenAI | Trendshift" width="250" height="55" /></a>

</div>

> 📣 **2026-05-07** — Wren Engine 已合并至本仓库的 [`core/`](./core) 目录下。之前的 `Canner/wren-engine` 仓库已归档。之前的 WrenAI GenBI 应用保留在 [`legacy/v1`](https://github.com/Canner/WrenAI/tree/legacy/v1) 分支（标签 `v1-final`）。[阅读公告 →](https://github.com/Canner/WrenAI/discussions/2205)

<!--
  📺 HERO DEMO (place here)
  ─────────────────────────
  Suggested: a 5–10 second silent loop showing:
    1. Terminal: `wren ask "who are our top 10 customers this quarter?"`
    2. Agent fetches context (memory + MDL) — visible reasoning trace
    3. Final SQL + result table
  Format: .gif (≤2 MB) or .mp4 (autoplay-muted).
  Save under  /assets/wrenai-demo.gif  and use the line below:

  <img src="./assets/wrenai-demo.gif" alt="Wren AI in action" width="820" />
-->

---

## WrenAI 是什么

WrenAI 是一个**开放的上下文层（context layer）**，为你的 Agent 提供数据模式（schema）所不具备的能力：业务语义、示例、记忆、治理机制，以及——即将推出——存在于你的文档、Wiki 和聊天记录中的非结构化企业知识。专为已有的 Agent 框架打造。 

![Wren AI architecture](./misc/wren-ai-architecture.png)

## 为什么 Agent 开发者选择 WrenAI

- **默认开源** —— 核心代码、SDK 和技能包均以 Apache-2.0 许可证开源。
- **专为 AI Agent 构建** —— 技能（Skills）、Agent 架构、上下文检索均为一等公民。以 SDK 形式提供，无缝对接工程师日常使用的 Agent 框架。
- **将正确性作为基础原语** —— 提供丰富的模式检索、dry-plan（执行前验证）验证、带提示的结构化错误、value profiling（值分析）及 eval runner（评估运行器）。Agent 负责编排，执行轨迹融入 Agent 的推理过程。
- **可审查、可复现的上下文** —— 每个定义、示例和映射均可版本化并关联证据。完美兼容 Git 工作流。
- **基于你现有的技术栈之上运行** —— 覆盖数据仓库、转换流水线及已有的语义层。无需维护额外的工具。

## 使用 WrenAI 前后对比

Agent 已无处不在。Claude Code、Cursor、ChatGPT、Aider、LangChain 流水线、Pydantic AI 工作流、内部 Copilot 以及面向客户的应用程序等，都不应被迫从零开始重新发现你的业务逻辑。借助 WrenAI（即“上下文层”），它们可以通过独立且共享的接口进行查询，该接口可供所有 Agent 和人员使用，不再受限于单一厂商的 UI 和架构。

<img width="1445" height="758" alt="before & after" src="https://github.com/user-attachments/assets/d6ef8b73-b844-4e11-9586-b4f7ab6ae9dc" />

## 快速开始

WrenAI 采用**以 Agent 驱动为核心设计**：你只需安装一次技能包，然后交由你的 AI 编程 Agent（如 Claude Code、Openclaw、Hermes、Codex 等）接管后续流程——包括 Python 依赖安装、数据库连接、项目脚手架搭建及首次查询。

### 1. 安装技能包

技能包是工作流指南，用于教导 AI 编程 Agent（如 Claude Code、Openclaw、Hermes、Codex 等）如何为你调用 Wren CLI。

```bash
npx skills add Canner/WrenAI --skill '*'
```

已安装多个 AI 编程 Agent 并希望技能包在所有环境中可用？传入 `--agent '*'`：

```bash
npx skills add Canner/WrenAI --skill '*' --agent '*'
```

或通过安装脚本执行：

```bash
curl -fsSL https://raw.githubusercontent.com/Canner/WrenAI/main/skills/install.sh | bash
```

查看 [Skills reference](https://docs.getwren.ai/oss/reference/skills) 获取已安装的完整技能列表及其功能说明。

### 2. 让 Agent 完成环境配置

在项目目录中打开你的 Agent，并输入：

使用 `/wren-onboarding` 技能来安装和配置 WrenAI。

Agent 将检查你的环境、安装 `wrenai`、创建连接配置文件、生成项目脚手架并执行首次查询——所有步骤在一个流程中完成。

### 3. （可选）丰富项目上下文

完成初始引导后，为你的项目补充模式无法承载的业务上下文：

在 **grill**（单次问答）模式下使用 `/wren-enrich-context` 技能。

提供两种模式：**grill**（一次一个问题，你全程参与把控）或 **auto-pilot**（Agent 读取 `<project>/raw/` 目录并自动提议）。两种模式均会写入 MDL、指令、查询和记忆——所有内容均可审查且兼容 Git。

### 4. 提问与查询

```bash
# Ask any question
"who are our top 10 customers by sales this quarter?"
```

或者直接用自然语言询问你的 Agent——它会利用上下文层解析模式、回忆相似的历史查询，并生成受控的 SQL。

**想在没有自己数据库的情况下体验？** 让 Agent 运行 `/wren-onboarding` 并使用内置的 `jaffle_shop` 示例数据集——流程相同，但几分钟内你就能完成端到端的数据仓库查询。

## 两步走：快速搭建，深度增强

```bash
/wren-onboarding         # 基于你的数据库生成 Wren 项目（Agent 驱动）
/wren-enrich-context     # 单一技能，两种模式：(开发中)
                         #   grill      — 一次一个问题，你全程参与把控
                         #   auto-pilot — Agent 读取 <project>/raw/ 并自动提议
wren ask "..."           # 通过上下文层进行查询
```

起步快，按需深。始终可审查且兼容 Git。

<!--
  📷 OPTIONAL: 2-up screenshot showing grill mode (left) vs auto-pilot mode (right).
  Save under  /assets/two-beats.png
-->

## 包含内容

- **建模定义语言（MDL）** —— 模型、列、关系、视图、立方体、指标、行级/列级访问控制（RLAC / CLAC）
- **引擎** —— 基于 Apache DataFusion，支持 20+ 数据源
- **记忆与示例** —— 基于 LanceDB，支持混合检索，可版本化
- **Agent SDK** —— `wren-langchain`（LangChain / LangGraph）、`wren-pydantic`；提供其他技术栈的参考 Python 集成方案
- **受控执行原语** —— 函数、dry-plan、行限制、访问控制

## 后续计划

- **上下文增强技能** —— `/wren-enrich-context`（grill + auto-pilot 模式）在 MDL、指令、查询和记忆层面的全面加固
- **端到端正确性原语** —— value profiling（值分析）、丰富检索、结构化错误、golden eval runner（黄金评估运行器）
- **原生 Agent 分发** —— 面向主流 Agent 框架的一等公民 SDK；查看 [GitHub Discussions](https://github.com/Canner/WrenAI/discussions) 了解优先级排序
- **完整受控执行** —— 审计日志、速率限制、审批工作流、数据流检查器

<!-- TODO: vision_paper_en.md is currently at .tmp/roadmap-discuss/vision_paper_en.md — move to a published path (e.g. docs/vision-paper.md or repo root) and update this link before publishing. -->
完整路线图与设计说明：请参阅 [vision paper](https://docs.getwren.ai/oss/introduction)。

## 文档

- [Quickstart](https://docs.getwren.ai/oss/get_started/quickstart) —— 从技能安装到首次回答
- [Concepts](https://docs.getwren.ai/oss/concepts/what_is_context) —— 什么是上下文、MDL 是什么、记忆机制如何运作
- [Connect a database](https://docs.getwren.ai/oss/guides/connect/overview) —— Postgres、BigQuery、Snowflake、DuckDB 等
- [Agent SDKs](https://docs.getwren.ai/oss/sdk/overview) —— 今日已发布功能与后续计划

## 社区

- 💬 [Discord](https://discord.gg/5DvshJqG8Z) —— 与团队及其他开发者交流
- 🐙 [GitHub Discussions](https://github.com/Canner/WrenAI/discussions) —— 设计讨论、RFC、深度话题
- 🐦 [Twitter / X](https://x.com/getwrenai) —— 版本更新与简短动态
- 🗞 [Blog](https://www.getwren.ai/blog) —— 愿景分享、复盘总结、深度解析

## 贡献指南

我们公开协作。Issues、PR、连接器开发、SDK 集成、文档修复——均欢迎参与。

- [Contributor guide](./CONTRIBUTING.md)
- [Connector ecosystem program](./docs/contributing-a-connector.md) —— 三级所有权体系：官方、社区认可、社区主导
- [Architecture map](./docs/architecture.md) —— 找到适合你修改的模块位置
- 不知从何开始？尝试 [`good first issue`](https://github.com/Canner/WrenAI/labels/good%20first%20issue) 标签。

<details>
<summary><strong>项目结构</strong> — click to expand</summary>

```
core/
  wren-core/         Rust semantic engine (Apache DataFusion)
  wren-core-base/    Shared manifest types + MDL builder
  wren-core-py/      Python bindings (PyPI: wren-core)
  wren-core-wasm/    WebAssembly build (npm: wren-core-wasm)
  wren/              Python SDK and CLI (PyPI: wrenai)
  wren-mdl/          MDL JSON schema
sdk/
  wren-langchain/    Reference agent SDK integration
skills/              Agent skills for context authoring
docs/                Module documentation
examples/            Example projects
```

</details>

## Contributors

<a href="https://github.com/Canner/WrenAI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Canner/WrenAI" alt="WrenAI contributors" />
</a>

## License

Apache 2.0。详见 [LICENSE](./LICENSE)。

---

<div align="center">

*与我们一起构建上下文层。*

**如果 WrenAI 对你有所帮助，请留下一个 ⭐ ——这能切实帮助我们成长！**

<p><a href="#top">⬆️ Back to top</a></p>

</div>