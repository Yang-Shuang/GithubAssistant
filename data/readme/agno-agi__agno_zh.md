<div align="center" id="top">
  <a href="https://agno.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-dark.svg">
      <source media="(prefers-colors-scheme: light)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg">
      <img src="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg" alt="Agno">
    </picture>
  </a>
</div>

<p align="center">
  构建、运行和管理 Agent 平台。<br/>
</p>

## 简介

Agno 是一个用于构建 Agent 平台的 SDK。

- 使用任意 Agent 框架构建智能体。
- 以生产级服务运行它们，支持链路追踪、任务调度和基于角色的访问控制（RBAC）。
- 通过单一管控面板进行统一管理。

Agno 让你完全掌控自己的 Agent 技术栈。自主管理你的数据、上下文、工具、权限（permission）、记忆以及人工审核流程。将平台部署在你的云端，并通过美观的界面进行管理。

<img width="3192" height="2038" alt="demo-os" src="https://github.com/user-attachments/assets/6d21e6bc-111f-4b81-ba29-6550fead89b2" />

## 你可以构建什么

Agno 能让任何 Agent 落地运行，以下是一些示例：

- [Coda →](https://docs.agno.com/tutorials/coda/overview) 常驻 Slack、与团队协同工作的代码助手。
- [Dash →](https://docs.agno.com/tutorials/dash/overview) 具备自学习能力的数据 Agent，答案基于 6 层上下文进行事实锚定（grounding）。
- [Scout →](https://docs.agno.com/tutorials/scout/overview) 能够穿梭于 Slack 和 Google Drive 之间检索信息并回答问题的上下文 Agent。
- [自动优化 Agent 平台 →](https://docs.agno.com/tutorials/starter/overview) 构建带有自我迭代循环的专属 Agent 平台。

## 快速上手

- [阅读文档](https://docs.agno.com)
- [用 20 行代码构建你的第一个 Agent。](https://docs.agno.com/first-agent)
- [使用 Claude Code 完全托管，构建一个自动优化的 Agent 平台。](https://docs.agno.com/tutorials/starter/overview)

## 核心特性

- [生产级 API](https://docs.agno.com/runtime/serve-as-api)。提供 50+ 个端点，支持 SSE 和 WebSocket，助你在此基础上构建产品。
- [存储管理](https://docs.agno.com/runtime/storage)。将会话、记忆、知识库和链路追踪数据存储在自有数据库中。
- [100+ 集成工具](https://docs.agno.com/tools/toolkits/overview)。使用预构建的工具包，轻松对接 100 多种外部工具。
- [上下文提供者](https://docs.agno.com/runtime/context)。实时获取来自 Slack、Drive、Wiki、MCP 及自定义数据源的信息。
- [人工审批](https://docs.agno.com/runtime/human-approval)：暂停运行等待用户确认，拦截需要管理员批准的工具调用。
- [可观测性](https://docs.agno.com/runtime/observability)：开箱即用，通过 OpenTelemetry 链路追踪、运行历史记录和审计日志实现全面监控。
- [安全性](https://docs.agno.com/runtime/security-and-auth)：开箱即用，提供基于 JWT 的 RBAC（基于角色的访问控制）以及多用户、多租户隔离能力。
- [交互接口](https://docs.agno.com/runtime/interfaces)。通过 Slack、Telegram、WhatsApp、Discord、AG-UI 和 A2A 暴露你的 Agent。
- [定时调度](https://docs.agno.com/runtime/scheduling)。基于 Cron 的定时任务和后台作业，无需依赖外部基础设施。
- [随处部署](https://docs.agno.com/runtime/deploy)。支持在任何容器化云平台上运行，如 Docker、Railway、AWS、GCP 等。

## 搭配编码 Agent 使用

提供两种方案：

1. 将 Agno 文档添加为索引源。在 Cursor 中：Settings → Indexing & Docs → 添加 `https://docs.agno.com/llms-full.txt`。该方案同样适用于 VS Code、Windsurf 等同类工具。
2. 将 Agno 文档添加为 MCP Server（模型上下文协议服务器）。将你常用的编码 Agent 指向 `https://docs.agno.com/mcp`。

完整指南请参见 [此处](https://docs.agno.com/coding-agents)。

## 社区

- [X (原 Twitter)](https://x.com/AgnoAgi)：关注获取版本更新与演示视频
- [通讯订阅](https://www.agno.com/the-agno-loop-newsletter)：每月推送最新功能动态

## 参与贡献

请参阅[贡献指南](https://github.com/agno-agi/agno/blob/main/CONTRIBUTING.md)。

## 遥测数据

Agno 会记录所使用的模型提供商信息，以便优先进行功能更新。可通过设置环境变量 `AGNO_TELEMETRY=false` 关闭此功能。

<p align="right"><a href="#top">↑ 回到顶部</a></p>