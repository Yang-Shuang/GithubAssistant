<p align="center">
  <img src="doc/assets/banner.jpg" alt="Paperclip 是用于管理工作型 AI Agent 的应用" width="720" />
</p>

<p align="center">
  <a href="#quickstart"><strong>快速开始</strong></a> &middot;
  <a href="https://paperclip.ing/docs"><strong>文档</strong></a> &middot;
  <a href="https://github.com/paperclipai/paperclip"><strong>GitHub</strong></a> &middot;
  <a href="https://discord.gg/m4HZY7xNG3"><strong>Discord</strong></a> &middot;
  <a href="https://x.com/papercliping"><strong>Twitter</strong></a> &middot;
  <a href="https://paperclip.ing"><strong>官网</strong></a>
</p>

<p align="center">
  <a href="https://github.com/paperclipai/paperclip/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT 许可证" /></a>
  <a href="https://github.com/paperclipai/paperclip/stargazers"><img src="https://img.shields.io/github/stars/paperclipai/paperclip?style=flat" alt="星标数" /></a>
  <a href="https://discord.gg/m4HZY7xNG3"><img src="https://img.shields.io/discord/000000000?label=discord" alt="Discord" /></a>
</p>

<br/>

<div align="center">
  <video src="https://github.com/user-attachments/assets/773bdfb2-6d1e-4e30-8c5f-3487d5b70c8f" width="600" controls></video>
</div>

<br/>

# Paperclip 是用于管理工作型 AI Agent 的应用。

面向 AI Agent 团队的开源编排平台。

**如果 OpenClaw 是_员工_，那么 Paperclip 就是_公司_。**

Paperclip 由 Node.js 服务端和 React 前端组成，用于编排一组 AI Agent 来运营业务。你可以接入自己的 Agent，分配目标，并通过一个统一的仪表盘跟踪工作进度与成本。

它看起来像是一个任务管理器。但在底层：组织架构、预算、治理规则、目标对齐和 Agent 协调都在其中运作。

**管理业务目标，而不是 Pull Request。**

|        | 步骤            | 示例                                                                        |
| ------ | --------------- | --------------------------------------------------------------------------- |
| **01** | 定义目标        | “打造全球排名第一的 AI 笔记应用，实现月营收（MRR）100万美元。”              |
| **02** | 组建团队        | CEO、CTO、工程师、设计师、市场人员——任何 Bot、任何服务商均可。             |
| **03** | 审批并运行      | 审查策略。设定预算。点击启动。通过仪表盘监控。                              |

<br/>

<div align="center">
<table>
  <tr>
    <td align="center"><strong>支持接入</strong></td>
    <td align="center"><img src="doc/assets/logos/openclaw.svg" width="32" alt="OpenClaw" /><br/><sub>OpenClaw</sub></td>
    <td align="center"><img src="doc/assets/logos/claude.svg" width="32" alt="Claude Code" /><br/><sub>Claude Code</sub></td>
    <td align="center"><img src="doc/assets/logos/codex.svg" width="32" alt="Codex" /><br/><sub>Codex</sub></td>
    <td align="center"><img src="doc/assets/logos/cursor.svg" width="32" alt="Cursor" /><br/><sub>Cursor</sub></td>
    <td align="center"><img src="doc/assets/logos/bash.svg" width="32" alt="Bash" /><br/><sub>Bash</sub></td>
    <td align="center"><img src="doc/assets/logos/http.svg" width="32" alt="HTTP" /><br/><sub>HTTP</sub></td>
  </tr>
</table>

<em>只要能接收心跳信号，就算正式入职。</em>

</div>

<br/>

## 如果你符合以下情况，Paperclip 将非常适合你：

- ✅ 你想构建**自主运行的 AI 公司**
- ✅ 你需要**协调多个不同的 Agent**（OpenClaw、Codex、Claude、Cursor）朝着共同目标努力
- ✅ 你同时打开了 **20 个 Claude Code 终端**，已经记不清每个人在做什么了
- ✅ 你想让 Agent **全天候（24/7）自主运行**，但仍希望审计工作并在必要时介入
- ✅ 你想**监控成本**并严格执行预算
- ✅ 你希望有一套管理 Agent 的流程，其体验**就像使用任务管理器一样**
- ✅ 你想通过手机来管理你的自主业务

<br/>

## 核心功能

<table>
<tr>
<td align="center" width="33%">
<h3>🔌 接入自有 Agent</h3>
任何 Agent、任何运行环境，统一纳入一张组织架构图。只要能接收心跳信号，就算正式入职。
</td>
<td align="center" width="33%">
<h3>🎯 目标对齐</h3>
每项任务都追溯至公司使命。Agent 清楚知道该做<em>什么</em>以及<em>为什么</em>要做。
</td>
<td align="center" width="33%">
<h3>💓 心跳机制</h3>
Agent 按调度周期唤醒，检查工作并执行任务。委派指令在组织架构内上下流转。
</td>
</tr>
<tr>
<td align="center">
<h3>💰 成本控制</h3>
为每个 Agent 设定月度预算。达到上限即自动停止。杜绝成本失控。
</td>
<td align="center">
<h3>🏢 多公司支持</h3>
一次部署，运行多家“公司”。数据完全隔离。为你的业务组合提供统一控制面。
</td>
<td align="center">
<h3>🎫 工单系统</h3>
每次对话均可追溯。每项决策均有解释。完整记录工具调用并提供不可篡改的审计日志。
</td>
</tr>
<tr>
<td align="center">
<h3>🛡️ 治理与管控</h3>
审批入职申请、覆盖执行策略、随时暂停或终止任意 Agent —— 全程可控。
</td>
<td align="center">
<h3>📊 组织架构</h3>
层级划分、角色定义、汇报关系。你的 Agent 有上级主管、职位头衔和岗位说明书。
</td>
<td align="center">
<h3>📱 移动端就绪</h3>
随时随地监控和管理你的自主业务。
</td>
</tr>
</table>

<br/>

## Paperclip 解决的问题

| 没有 Paperclip                                                                                                                     | 使用 Paperclip                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| ❌ 你打开了 20 个 Claude Code 标签页，无法追踪各自的任务。重启后一切数据丢失。                              | ✅ 任务基于工单管理，对话支持线程回复，会话在重启后可持久化保存。                                                |
| ❌ 你需要手动从多个地方收集上下文，以提醒你的 Bot 你实际在做什么。                                     | ✅ 上下文沿任务向上流动至项目和公司目标——Agent 始终清楚该做什幺以及为什么。                  |
| ❌ Agent 配置文件散落在各个文件夹中杂乱无章，你还在重复造轮子开发任务管理、通信和 Agent 间协调功能。 | ✅ Paperclip 开箱即提供组织架构、工单系统、委派机制和治理规则——让你真正运营一家公司，而非维护一堆脚本。 |
| ❌ 失控的循环会浪费数百美元 Token 额度，在你还没意识到问题前就已耗尽配额。                           | ✅ 成本追踪功能展示 Token 预算，并在 Agent 超限时进行节流。管理层通过预算优先级进行调度。                    |
| ❌ 你有 recurring jobs（客服、社媒运营、报表生成），但必须手动记住并触发它们。                        | ✅ 心跳机制按调度周期自动处理常规工作。管理层负责监督。                                                                |
| ❌ 你有一个想法，得找到代码仓库、启动 Claude Code、保持标签页打开并全程盯着它运行。                                | ✅ 在 Paperclip 中添加任务即可。你的编程 Agent 会持续处理直到完成。管理层随后审查其成果。                              |

<br/>

## 为什么选择 Paperclip

Paperclip 将复杂的编排细节处理得井井有条。

|                                   |                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **原子化执行。**             | 任务签出和预算强制执行均为原子操作，杜绝重复工作和成本失控。                      |
| **Agent 状态持久化。**       | Agent 在心跳之间恢复相同的任务上下文，而非从头重启。                     |
| **运行时技能注入。**      | Agent 可在运行时学习 Paperclip 工作流和项目上下文，无需重新训练。                      |
| **支持回滚的治理机制。**     | 审批关卡强制生效，配置变更带有版本记录，错误修改可安全回滚。        |
| **目标感知型执行。**         | 任务携带完整的目标溯源链，确保 Agent 始终看到“为什么”，而不仅仅是标题。                        |
| **可移植的公司模板。**   | 支持导出/导入组织架构、Agent 和技能，内置密钥清理和冲突处理机制。                          |
| **真正的多公司数据隔离。** | 每个实体均按公司作用域划分，一次部署即可运行多家独立公司和审计轨迹。 |

<br/>

## 底层架构

Paperclip 是一个完整的全局控制面（Control Plane），而非简单的封装层。在动手自己搭建之前，请记住：这些功能已经存在且成熟可用了。

```
┌──────────────────────────────────────────────────────────────┐
│                       PAPERCLIP SERVER                       │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │Identity & │  │  Work &   │  │ Heartbeat │  │Governance │  │
│  │  Access   │  │   Tasks   │  │ Execution │  │& Approvals│  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │ Org Chart │  │Workspaces │  │  Plugins  │  │  Budget   │  │
│  │ & Agents  │  │ & Runtime │  │           │  │ & Costs   │  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │ Routines  │  │ Secrets & │  │ Activity  │  │  Company  │  │
│  │& Schedules│  │  Storage  │  │ & Events  │  │Portability│  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
└──────────────────────────────────────────────────────────────┘
         ▲              ▲              ▲              ▲
   ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
   │  Claude   │  │   Codex   │  │   CLI     │  │ HTTP/web  │
   │   Code    │  │           │  │  agents   │  │   bots    │
   └───────────┘  └───────────┘  └───────────┘  └───────────┘
```

### 系统模块

<table>
<tr>
<td width="50%">

**身份与访问控制（Identity & Access）** — 支持两种部署模式（可信本地回环或需认证），管理用户看板、Agent API 密钥、短生命周期运行 JWT、公司成员关系、邀请流程及 OpenClaw 入职引导。所有变更请求均追溯至具体操作者。

</td>
<td width="50%">

**组织架构与 Agent（Org Chart & Agents）** — Agent 拥有角色、头衔、汇报线、权限和预算。适配器示例涵盖架构图：Claude Code、Codex、CLI Agent（如 Cursor/Gemini/bash）、HTTP/Webhook Bot（如 OpenClaw）及外部插件适配器。只要能接收心跳信号，就算正式入职。

</td>
</tr>
<tr>
<td>

**工作与任务系统（Work & Task System）** — Issue 携带公司/项目/目标/父级关联，支持原子签出与执行锁、一级阻塞依赖、评论、文档、附件、工作成果、标签及收件箱状态。无重复劳动，不丢失上下文。

</td>
<td>

**心跳执行机制（Heartbeat Execution）** — 基于数据库的唤醒队列，支持合并节流、预算检查、工作区解析、密钥注入、技能加载及适配器调用。运行产出结构化日志、成本事件、会话状态和审计轨迹。自动处理孤儿任务恢复。

</td>
</tr>
<tr>
<td>

**工作区与运行时环境（Workspaces & Runtime）** — 项目工作区、隔离执行工作区（git worktrees、operator branches）及运行时服务（开发服务器、预览 URL）。Agent 每次都在正确的目录中，带着正确的上下文工作。

</td>
<td>

**治理与审批流程（Governance & Approvals）** — 看板审批工作流、带审查/批准阶段的执行策略、决策追踪、预算硬限制、Agent 暂停/恢复/终止及完整审计日志。未经你签字确认，任何内容不会上线。

</td>
</tr>
<tr>
<td>

**预算与成本控制（Budget & Cost Control）** — 按公司、Agent、项目、目标、Issue、服务商和模型追踪 Token 与成本。支持作用域预算策略、警告阈值和硬性停止。超支时自动暂停 Agent 并取消排队任务。

</td>
<td>

**例行任务与调度（Routines & Schedules）** — 支持 cron、webhook 和 API 触发的周期性任务。提供并发控制与追赶策略。每次例行执行自动生成可追踪的 Issue 并唤醒指定 Agent —— 无需手动触发。

</td>
</tr>
<tr>
<td>

**插件系统（Plugins）** — 实例级插件架构，支持进程外 Worker、能力门控主机服务、任务调度、工具暴露及 UI 贡献。在不 Fork Paperclip 的前提下扩展功能。

</td>
<td>

**密钥与存储管理（Secrets & Storage）** — 实例级与公司级密钥、加密本地存储、服务商托管的对象存储、附件及工作成果。敏感值默认不进入 Prompt，除非特定作用域的运行明确需要。

</td>
</tr>
<tr>
<td>

**活动与事件记录（Activity & Events）** — 变更操作、心跳状态变化、成本事件、审批、评论和工作成果均作为持久化活动记录，便于运营人员审计“发生了什么”及“为什么发生”。

</td>
<td>

**公司数据可移植性（Company Portability）** — 支持导出和导入完整组织架构——包括 Agent、技能、项目、例行任务和 Issue —— 内置密钥清理与冲突处理。一次部署，多家独立公司与完全的数据隔离。

</td>
</tr>
</table>

<br/>

## Paperclip 不是什么

|                              |                                                                                                                      |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **不是聊天机器人。**           | Agent 有岗位职责，而不是聊天窗口。                                                                                  |
| **不是 Agent 框架。**  | 我们不教你怎么构建 Agent。我们教你如何运营一家由它们组成的公司。                                |
| **不是工作流搭建器。**  | 没有拖拽式流水线。Paperclip 建模的是“公司”——包含组织架构、目标、预算和治理规则。            |
| **不是 Prompt 管理器。**    | Agent 自带 Prompt、模型和运行环境。Paperclip 管理它们工作的组织环境。               |
| **不是单 Agent 工具。** | 这是为团队设计的。如果你只有一个 Agent，你可能不需要 Paperclip。如果你有二十个 —— 那你绝对需要。 |
| **不是代码审查工具。**  | Paperclip 编排的是工作流，而不是 Pull Request。请自带你的代码审查流程。                                       |

<br/>

## 快速开始

开源。支持自托管。无需注册 Paperclip 账号。

```bash
npx paperclipai onboard --yes
```

该快速入门路径默认使用可信本地回环模式，以实现最快的首次运行体验。若想以认证/私有模式启动，请显式指定绑定预设：

```bash
npx paperclipai onboard --yes --bind lan
# 或：
npx paperclipai onboard --yes --bind tailnet
```

如果你已配置过 Paperclip，重新运行 `onboard` 会保留现有配置。使用 `paperclipai configure` 编辑设置。

或手动安装：

```bash
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
pnpm install
pnpm dev
```

这将启动 API 服务端，地址为 `http://localhost:3100`。内置 PostgreSQL 数据库会自动创建 —— 无需额外配置。

> **环境要求：** Node.js 20+，pnpm 9.15+

<br/>

## 常见问题（FAQ）

**典型的部署长什么样？**
本地环境下，单个 Node.js 进程管理内置的 Postgres 和本地文件存储。生产环境中，指向你自己的 Postgres 实例并按需部署即可。配置好项目、Agent 和目标 —— 剩下的交给 Agent。

如果你是独立开发者，可以使用 Tailscale 随时随地访问 Paperclip。后续业务增长时，可轻松迁移至 Vercel 等云平台。

**我可以运行多家公司吗？**
可以。单次部署支持无限数量的公司，且数据完全隔离。

**Paperclip 和 OpenClaw、Claude Code 等 Agent 有什么区别？**
Paperclip _使用_ 这些 Agent。它将它们编排成一家“公司”——包含组织架构、预算、目标、治理规则和问责机制。

**为什么我应该用 Paperclip，而不是直接把 OpenClaw 指向 Asana 或 Trello？**
Agent 编排涉及如何协调任务签出状态、维护会话、监控成本、建立治理规则等细微之处 —— Paperclip 已为你处理好这些。
（支持接入第三方工单系统已在 Roadmap 中）

**Agent 会持续运行吗？**
默认情况下，Agent 按调度心跳和事件触发器运行（如任务分配、@提及）。你也可以接入 OpenClaw 这类连续运行的 Agent。你提供 Agent，Paperclip 负责协调。

<br/>

## 开发指南

```bash
pnpm dev              # 完整开发环境（API + UI，监听模式）
pnpm dev:once         # 完整开发环境（无文件监听）
pnpm dev:server       # 仅服务端
pnpm build            # 构建全部
pnpm typecheck        # 类型检查
pnpm test             # 快速默认测试运行（仅 Vitest）
pnpm test:watch       # Vitest 监听模式
pnpm test:e2e         # Playwright 浏览器套件
pnpm db:generate      # 生成数据库迁移文件
pnpm db:migrate       # 应用数据库迁移
```

`pnpm test` 不会运行 Playwright。浏览器测试套件保持独立，通常仅在开发相关流程或 CI 环境中执行。

完整开发指南请参阅 [doc/DEVELOPING.md](doc/DEVELOPING.md)。

<br/>

## 路线图

- ✅ 插件系统（如知识库、自定义追踪、队列等）
- ✅ OpenClaw / claw-style Agent 员工接入
- ✅ companies.sh - 导入和导出完整组织架构
- ✅ AGENTS.md 配置简化
- ✅ 技能管理器（Skills Manager）
- ✅ 定时例行任务（Scheduled Routines）
- ✅ 更完善的预算功能
- ✅ Agent 审查与审批流程
- ✅ 多人类用户支持
- ⚪ 云/沙盒 Agent（如 Cursor / e2b agents）
- ⚪ 制品与工作成果管理
- ⚪ 记忆/知识库系统
- ⚪ 结果强制约束
- ⚪ MAXIMIZER MODE
- ⚪ 深度规划
- ⚪ 工作队列
- ⚪ 自组织机制
- ⚪ 自动组织学习
- ⚪ CEO 对话助手
- ⚪ 云端部署支持
- ⚪ 桌面客户端应用

此为精简版路线图预览。完整版请参阅 [ROADMAP.md](ROADMAP.md)。

<br/>

## 社区与插件

在 [awesome-paperclip](https://github.com/gsxdsm/awesome-paperclip) 查找更多插件与资源。

## 遥测数据（Telemetry）

Paperclip 会收集匿名使用遥测数据，以帮助我们了解产品使用情况并进行优化。绝不会收集个人信息、Issue 内容、Prompt、文件路径或密钥。私有仓库引用在发送前会使用每次安装的唯一盐值进行哈希处理。

遥测功能**默认启用**，可通过以下方式禁用：

| 方式               | 设置方法                                                     |
| -------------------- | ------------------------------------------------------- |
| 环境变量           | `PAPERCLIP_TELEMETRY_DISABLED=1`                        |
| 标准约定           | `DO_NOT_TRACK=1`                                        |
| CI 环境            | 当 `CI=true` 时自动禁用                   |
| 配置文件          | 在 Paperclip 配置中设置 `telemetry.enabled: false` |

## 贡献指南

我们欢迎各类贡献。详情请参阅 [contributing guide](CONTRIBUTING.md)。

<br/>

## 社区交流

- [Discord](https://discord.gg/m4HZY7xNG3) — 加入社区
- [Twitter / X](https://x.com/papercliping) — 关注动态与公告
- [GitHub Issues](https://github.com/paperclipai/paperclip/issues) — Bug 报告与功能请求
- [GitHub Discussions](https://github.com/paperclipai/paperclip/discussions) — 创意交流与 RFC

<br/>

## 许可证

MIT &copy; 2026 [Paperclip Labs, Inc](https://paperclip.ing)

## Star 历史

[![Star History Chart](https://api.star-history.com/image?repos=paperclipai/paperclip&type=date&legend=top-left)](https://www.star-history.com/?repos=paperclipai%2Fpaperclip&type=date&legend=top-left)

<br/>

---

<p align="center">
  <sub>基于 MIT 协议开源。为追求高效交付、而非保姆式带教 Agent 的人打造。</sub>
</p>