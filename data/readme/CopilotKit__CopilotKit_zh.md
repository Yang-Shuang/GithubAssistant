<div align=center>

<img width="120" height="120" alt="FavIcon" src="https://github.com/user-attachments/assets/779de607-2b8d-4751-872b-1243e97c7d18" />

# CopilotKit

<div align=center>

[Docs](https://docs.copilotkit.ai/?ref=github_readme) ·
[Examples](https://www.copilotkit.ai/examples) ·
[Enterprise Intelligence Platform](https://go.copilotkit.ai/enterprise-intelligence-platform) ·
[Discord](https://discord.gg/6dffbvGU3D?ref=github_readme)

</div>

构建具备生成式 UI、共享状态以及人在回路（Human-in-the-Loop）工作流的 **Agent 原生应用**。

</div>

[![CopilotKit](https://github.com/user-attachments/assets/aeb56c28-c766-44a5-810c-5d999bb6a32a)](https://go.copilotkit.ai/copilotkit-docs)

<div align="center" style="display:flex;justify-content:start;gap:16px;height:20px;margin: 0;">
  <a href="https://www.npmjs.com/package/@copilotkit/react-core" target="_blank">
    <img src="https://img.shields.io/npm/v/%40copilotkit%2Freact-core?logo=npm&logoColor=%23FFFFFF&label=Version&color=%236963ff" alt="NPM">
  </a>

  <a href="https://github.com/copilotkit/copilotkit/blob/main/LICENSE" target="_blank">
    <img src="assets/license-badge.svg" alt="License: MIT" height="20">
  </a>

  <a href="https://discord.gg/6dffbvGU3D" target="_blank">
    <img src="https://img.shields.io/discord/1122926057641742418?logo=discord&logoColor=%23FFFFFF&label=Discord&color=%236963ff" alt="Discord">
  </a>
  </div>
  <br/>
  <div>
    <a href="https://www.producthunt.com/posts/copilotkit" target="_blank">
  </a>

<div />
  <div align="center">
      <a href="https://trendshift.io/repositories/5730" target="_blank"><img src="https://trendshift.io/api/badge/repositories/5730" alt="CopilotKit%2FCopilotKit | Trendshift"                         style="width: 250px; height: 55px;" width="250" height="55"/>
    </a>
    <a href="https://www.producthunt.com/posts/copilotkit" target="_blank">
      <img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=428778&theme=light&period=daily">
    </a>

  </div>

---

## CopilotKit 是什么？

CopilotKit 是构建全栈 Agent 应用、生成式 UI（Generative UI）及聊天应用的顶级 SDK。

我们是 **[AG-UI 协议](https://github.com/ag-ui-protocol/ag-ui)** 背后的公司，该协议已被 Google、LangChain、AWS、Microsoft、Mastra、PydanticAI 等广泛采用！

https://github.com/user-attachments/assets/72b7b4f3-b6e7-460c-a932-5746fe3c8db3

<div align="center">1 分钟内为你的应用接入 AI</div>

**核心特性：**

- **聊天界面（Chat UI）** – 基于 React 的聊天组件，支持消息流式传输、工具调用及 Agent 响应。
- **后端工具渲染** – 使 Agent 能够调用返回 UI 组件的后端工具，并在客户端直接渲染。
- **生成式 UI（Generative UI）** – 允许 Agent 根据用户意图和自身状态，在运行时动态生成并更新 UI 组件。
- **共享状态（Shared State）** – 一个同步的状态层，Agent 与 UI 组件均可实时读写。
- **人在回路（Human-in-the-Loop）** – 允许 Agent 在执行过程中暂停，以请求用户输入、确认或修改后再继续。

https://github.com/user-attachments/assets/55bf6714-62a7-4d5d-9232-07747cc0763b

## 快速开始

### 新建项目：

```bash
npx copilotkit@latest create -f <framework>
```

### 现有项目：

```bash
npx copilotkit@latest init
```

https://github.com/user-attachments/assets/7372b27b-8def-40fb-a11d-1f6585f556ad

安装后你将获得：

- **已安装 CopilotKit** – 核心包已在你的应用中完整配置
- **Provider 已配置** – 上下文、状态和 Hooks 就绪，可直接使用
- **Agent 与 UI 已连接** – Agent 可流式传输操作并立即渲染 UI
- **具备部署条件** – 你的应用已准备好进行部署

[查看完整入门指南 →](https://docs.copilotkit.ai/langgraph/quickstart)

## 工作原理：

CopilotKit 将你的 UI、Agent 和工具连接到一个统一的交互循环中。

![CopilotKit Diagram — Motion x2 6 sec version](https://github.com/user-attachments/assets/6f175d86-bd22-4c26-a13a-6013654ed542)

从而实现：

- 向用户请求输入的 Agent
- 渲染 UI 的工具
- 跨步骤和会话的状态化工作流

## ⭐️ useAgent Hook

`useAgent` Hook 是 `useCoAgent` 的完整超集，直接基于 AG-UI 构建，让你对 Agent 连接拥有更多控制权。

```ts
// 编程式访问并控制你的 Agents
const { agent } = useAgent({ agentId: "my_agent" });

// 渲染和更新 Agent 的状态
return <div>
  <h1>{agent.state.city}</h1>
  <button onClick={() => agent.setState({ city: "NYC" })}>
    Set City
  </button>
</div>
```

查看 [useAgent 文档](https://go.copilotkit.ai/useagent-docs) 了解更多。

https://github.com/user-attachments/assets/67928406-8abc-49a1-a851-98018b52174f

## 生成式 UI（Generative UI）

生成式 UI 是 CopilotKit 的核心模式之一，允许 Agent 在工作流中动态渲染 UI。

https://github.com/user-attachments/assets/3cfacac0-4ffd-457a-96f9-d7951e4ab7b6

### 三种类型对比

<img width="708" height="311" alt="image" src="https://github.com/user-attachments/assets/962f49c2-31ea-43c5-b2a3-7cdde114705a" />

#### 探索更多：

- [静态（AG-UI 协议）](https://docs.copilotkit.ai/ag-ui-protocol)
- [声明式（A2UI）](https://docs.copilotkit.ai/generative-ui/specs/a2ui#using-a2ui-with-copilotkit)
- [开放式（MCP Apps & Open JSON）](https://docs.copilotkit.ai/generative-ui/specs/mcp-apps)

[生成式 UI 教学仓库 →](https://github.com/CopilotKit/CopilotKit/tree/main/examples/showcases/generative-ui)

## 🖥️ AG-UI：Agent–用户交互协议

将 Agent 工作流连接到面向用户的应用，在代理技术栈中拥有深度合作伙伴关系及原生集成（包括 LangGraph、CrewAI 等）。

[![AG-UI](https://github.com/user-attachments/assets/a625237a-cfc1-45fc-8d0c-637316b81291)](https://go.copilotkit.ai/ag-ui)

---

```
npx create-ag-ui-app my-agent-app
```

  <a href="https://github.com/ag-ui-protocol/ag-ui" target="_blank">
   Learn more in the AG-UI README →
  </a>

## 🤝 社区

- [更新日志](https://docs.copilotkit.ai/whats-new)
<h3>有疑问或需要帮助？</h3>
  <a href="https://discord.gg/6dffbvGU3D?ref=github_readme" target="_blank">
   加入我们的 Discord →
  </a> </br>
    <a href="https://docs.copilotkit.ai/?ref=github_readme" target="_blank">
  阅读文档 →
  </a> </br>
    <a href="https://cloud.copilotkit.ai?ref=github_readme" target="_blank">
   试用 Copilot Cloud →
  </a>
<h3>关注最新更新！**</h3>
  <a href="https://www.linkedin.com/company/copilotkit/" target="_blank">
   在 LinkedIn 上关注我们 →
  </a> </br>
    <a href="https://x.com/copilotkit" target="_blank">
   在 X (Twitter) 上关注我们 →
  </a>

## 🙋🏽‍♂️ 贡献指南

感谢你为 CopilotKit 贡献代码！💜

我们珍视每一份贡献，无论是编写代码、完善文档、创建演示应用，还是仅仅向他人推荐。

以下是一些帮助你入门的实用资源：

- **代码贡献**，请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md)。
- **文档相关贡献**，请查看[文档贡献指南](https://docs.copilotkit.ai/contributing/docs-contributions?ref=github_readme)。

- **想参与但不知从何入手？** [加入我们的 Discord](https://discord.gg/6dffbvGU3D) 并告诉我们你的想法！

## 安装为 Claude Code 插件

CopilotKit monorepo 同时也是一个 Claude Code 插件——安装后即可使用全部 9 项技能（3 个包元技能 + 6 个生命周期旅程技能）。

将仓库添加为 Claude Code 市场源：

```bash
claude plugin marketplace add https://github.com/CopilotKit/CopilotKit
claude plugin install copilotkit
```

技能文件从仓库根目录的 `skills/<slug>/SKILL.md` 自动发现。三个包元技能（`runtime`、`react-core`、`a2ui-renderer`）是 `packages/<pkg>/skills/<pkg>/` 下源文件的**自动生成镜像**——请勿直接编辑镜像文件。如需更新内容，请修改 `packages/*/skills/` 下的源文件并运行：

```bash
pnpm sync:plugin-skills
```

Lefthook 预提交检查（`pnpm check:plugin-skills`）会拒绝导致镜像与源文件不一致的提交。插件版本固定于 `packages/runtime/package.json`，并由同一脚本保持同步。

### 技能清单

| Slug                     | Type      | Source                                         |
| ------------------------ | --------- | ---------------------------------------------- |
| `runtime`                | core      | `packages/runtime/skills/runtime/`             |
| `react-core`             | framework | `packages/react-core/skills/react-core/`       |
| `a2ui-renderer`          | framework | `packages/a2ui-renderer/skills/a2ui-renderer/` |
| `0-to-working-chat`      | lifecycle | `skills/0-to-working-chat/`                    |
| `spa-without-runtime`    | lifecycle | `skills/spa-without-runtime/`                  |
| `go-to-production`       | lifecycle | `skills/go-to-production/`                     |
| `scale-to-multi-agent`   | lifecycle | `skills/scale-to-multi-agent/`                 |
| `v1-to-v2-migration`     | lifecycle | `skills/v1-to-v2-migration/`                   |
| `debug-and-troubleshoot` | lifecycle | `skills/debug-and-troubleshoot/`               |

## 📄 许可证

本仓库源代码遵循 [MIT 许可证](https://github.com/CopilotKit/CopilotKit/blob/main/LICENSE) 开源。