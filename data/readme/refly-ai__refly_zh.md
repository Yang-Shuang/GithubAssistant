# Refly —— 基于 Vibe 工作流的智能体技能构建器
<p align="right">
  <a href="README.md"><u>English</u></a> · <a href="README_CN.md"><u>中文</u></a>
</p>
<p align="center">
  <a href="https://github.com/refly-ai/refly">
    <img src="https://img.shields.io/github/stars/refly-ai/refly?style=flat&colorA=080f12&colorB=1fa669&logo=github" alt="GitHub stars">
  </a>
  <a href="https://refly.ai/workspace">
    <img src="https://img.shields.io/badge/refly.ai-007bff?style=flat&colorA=080f12&colorB=007bff&logo=google-chrome&logoColor=white" alt="Website">
  </a>
  <a href="https://www.youtube.com/@refly-ai">
    <img src="https://img.shields.io/badge/YouTube-Refly%20AI-FF0000?style=flat&colorA=080f12&colorB=FF0000&logo=youtube&logoColor=white" alt="YouTube">
  </a>
  <a href="https://discord.com/invite/YVuYFjFvRC">
    <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2FYVuYFjFvRC%3Fwith_counts%3Dtrue&query=%24.approximate_member_count&suffix=%20members&logo=discord&logoColor=white&label=%20&color=7389D8&labelColor=6A7EC2" alt="Discord">
  </a>
  <a href="https://github.com/refly-ai/refly-skills">
    <img src="https://img.shields.io/badge/refly--skills-Repo-2ea043?style=flat&colorA=080f12&logo=github" alt="Refly Skills">
  </a><br>
  <a href="https://docs.refly.ai/">
    <img src="https://img.shields.io/badge/docs.refly.ai-Docs-2ea043?style=flat&colorA=080f12&logo=readthedocs" alt="Docs">
  </a>
  <a href="https://deepwiki.com/refly-ai/refly">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-ReflyAI%20License-2ea043?style=flat&colorA=080f12" alt="License">
  </a>
  <a href="https://x.com/reflyai">
    <img src="https://img.shields.io/badge/%40reflyai-black?style=flat&logo=x&labelColor=%23101419&color=%232d2e30" alt="X (formerly Twitter) Follow">
  </a>
</p>


[Lovable API 集成](#use-case-1-api-integration) · [飞书/Lark Webhook](#use-case-2-webhook-for-lark-feishu) · [Claude Code 技能支持](#use-case-3-skills-for-claude-code) · [构建 Clawdbot](#use-case-4-build-clawdbot)

技能（Skills）不是提示词，而是持久化的基础设施。

Refly 是首个开源的、用于构建稳定、原子化且支持版本控制的智能体技能的平台。 

<a href="https://refly.ai/workspace"><u>立即体验</u></a> 

---
## Refly Skills

**Refly 技能**是 Refly 官方可执行技能注册中心。

- ⚡ **即点即用**：在 Refly 中一键运行技能
- 🧩 **可复用基础设施**：版本化技能，而非一次性提示词
- 🔌 **随处分发**：将技能导出至 Claude Code 或部署为 API
- 🌍 **社区驱动**：导入、Fork 并发布你自己的技能

浏览注册中心：<a href="https://github.com/refly-ai/refly-skills"><u>Refly Skills 仓库</u></a> 

技能是确定性的智能体能力——可在不同工作流、团队和运行环境中复用。

**简而言之**：Refly 将企业标准作业程序（SOP）编译为可执行的智能体技能。3 分钟构建，随处分发。

---
## 快速开始

### 部署 Refly

- 📘 **[自托管部署指南](https://docs.refly.ai/community-version/self-deploy/)**  
  *（推荐开发者使用）*：在自有服务器上通过 Docker 逐步部署 Refly 的详细教程。

- 🔌 **[API 参考文档](https://github.com/refly-ai/refly/tree/main/docs/en/guide/api)**  
  完整的 API 文档，助你快速将 Refly 集成到你的应用中。

> [!TIP]
> 想立即体验？直接打开托管工作区：<a href="https://refly.ai/workspace"><u>Refly 在线工作区</u></a> 

### 下一步做什么？

部署完成后，请根据你的使用场景选择路径：

| 我的目标 | 开始路径 | 耗时 |
|-------------|-----------|------|
| 🔧 **构建第一个工作流** | [创建工作流](#create-your-first-workflow) | 约 5 分钟 |
| 🔌 **通过 API 调用工作流** | [API 集成](#use-case-1-api-integration) | 约 10 分钟 |
| 💬 **接入飞书/Lark** | [Webhook 配置](#use-case-2-webhook-for-lark-feishu) | 约 15 分钟 |
| 🤖 **导出至 Claude Code** | [技能导出](#use-case-3-skills-for-claude-code) | 约 15 分钟 |
| 🦞 **构建 Clawdbot** | [构建 Clawdbot](#use-case-4-build-clawdbot) | 约 20 分钟 |
---


## 为什么选择 Refly？

大多数 AI 智能体在生产环境中失败，是因为它们依赖于“Vibe 编码”的脚本和脆弱、黑盒化的逻辑。随着生态系统向 Claude Code、AutoGen 和 MCP 等智能体框架演进，瓶颈已不再是 LLM（大语言模型），而是缺乏标准化且可靠的执行动作。

Refly 填补了原始 API 与智能体之间的鸿沟。我们允许你将杂乱的业务逻辑编码为结构化的、支持版本控制的智能体技能（Agent Skills），任何智能体均可 100% 可靠地调用它们。

**停止硬编码工具**。在 Refly 的可视化 IDE 中一次性构建模块化技能，并将其作为 MCP 服务器、标准 API 或可移植 SDK 部署到任意智能体框架。<a href="https://refly.ai/workspace"><u>立即体验</u></a> 

---

## 核心能力

### 🎯 基于 Vibe 构建（AI Copilot 驱动）

用自然语言描述你的业务逻辑，Refly 的模型原生 DSL 会将你的意图编译为高性能技能。

- **意图驱动构建**：只需描述一次工作需求，Refly 即可将其转化为确定性、可复用且可组合的技能。
- **规模化高效执行**：专为 LLM 优化的精简 DSL，确保快速运行并显著降低 Token 消耗。
- **3 分钟部署上线**：从静态企业 SOP 到生产级智能体技能，仅需不到 3 分钟。

### ⚡ 可控执行（可干预运行时）

打破 AI 执行的“黑盒”状态，采用专为确定性可靠性设计的有状态运行时。

- **可干预运行时**：在运行过程中暂停、审计并重新引导智能体逻辑，确保 100% 的操作合规性。
- **确定性保障**：强制执行严格的业务规则，最大限度减少幻觉并支持故障恢复。

### 🚀 生产级交付（统一智能体技术栈）

将 MCP 集成、工具、模型和可复用技能统一至单一执行层。

- **全场景交付**：导出为 Lovable API、Slack 或飞书 Webhook，或作为 Claude Code 和 Cursor 的原生工具。
- **稳定调度**：通过托管执行机制，按预定计划可靠地运行工作流。

### 🏛️ 资产化治理（技能注册中心）

将脆弱的脚本转化为企业内受控、可共享的基础设施。

- **集中式技能注册中心**：安全地管理、版本控制和共享智能体能力。
- **团队工作区协作**：内置版本控制与审计日志，支持多人协同开发。

---

## 生态系统

Refly 旨在成为连接你现有企业工具链与下一代智能体运行时的通用桥梁。

### 工具与协议（输入端）

零摩擦地将自有数据与逻辑接入 Refly。

- **3000+ 原生工具**：无缝集成 Stripe、Slack、Salesforce、GitHub 等。

完整的支持模型与工具提供商列表见 [provider-catalog.json](./config/provider-catalog.json)。

<img width="3840" height="1254" alt="part supported tools integrations in refly" src="https://github.com/user-attachments/assets/954f43bd-356d-48c4-a3b9-1c0f2e781a43" />


- **支持 MCP**：完全兼容模型上下文协议（Model Context Protocol）服务器
- **私有技能连接器**：对接你的数据库、脚本与内部系统

### 智能体运行时与平台（输出端）

将确定性技能导出至任意工作发生的环境。

<img width="2688" height="1512" alt="deterministic skills can be exported to cursor, claude code and etc." src="https://github.com/user-attachments/assets/23e7a204-4dce-432f-b8bc-65839061d086" />



- **AI 编程工具**：原生支持 Claude Code 和 Cursor（即将上线）
- **应用构建器**：通过有状态 API 为 Lovable 或自定义前端赋能
- **自动化枢纽**：作为 Slack、飞书/Lark 或 Microsoft Teams 的 Webhook 部署
- **智能体框架**：兼容 AutoGen、Manus、LangChain 及自定义 Python 技术栈

---
## 为什么团队选择 Refly

### 面向开发者：从 Vibe 到生产环境

当前的智能体工具主要分为两类：

- **工作流构建器**（如 n8n、Dify）：擅长编排，但工作流脆弱、仅支持触发式“黑盒”操作且难以复用。
- **智能体框架**（如 LangChain）：基础原语强大，但需要大量工程开发、手动编写样板代码且维护成本高。
Refly 消除了手动配置的摩擦成本，为你提供从“Vibe”想法到可用智能体工具的最快路径。通过采用我们的精简 DSL，你既能享受 GUI 的便捷，又能获得代码级的精确度。

| 维度 | 传统自动化工具 <br><sub>(n8n, Dify)</sub> | 代码优先 SDK <br><sub>(LangChain)</sub> | **Refly 技能** |
| :--- | :--- | :--- | :--- |
| **交互深度** | 仅支持触发 <br><sub>黑盒模式</sub> | 编程式调用 <br><sub>依赖代码变更</sub> | **可干预运行时**<br><sub>运行中动态引导逻辑</sub> |
| **构建方式** | 手动接线与配置 JSON | 手写 Python/TS 样板代码 | **AI Copilot 驱动**<br><sub>描述意图 → 自动生成技能</sub> |
| **故障恢复** | 失败即从头重启 | 调试 → 重新部署 → 重跑 | **热修复（Hot-fix）**<br><sub>执行中直接修复工作流</sub> |
| **可移植性** | 跨环境复用困难 | 绑定特定框架 | **随处导出**<br><sub>支持 Claude Code、Cursor、Manus 等</sub> |
| **部署形态** | 功能受限的工具节点 | 自定义微服务 | **生产就绪**<br><sub>有状态且经过验证的 API</sub> |

### 面向企业：可扩展的技能治理

像 n8n 这样的工作流工具擅长基础连接，LangChain 等框架提供强大原语——但它们都无法为企业级智能体基础设施提供所需的受控、生产就绪的能力层。

Refly 充当智能体技能构建器，提供部署全企业 AI 所需的安全治理与可靠性基础设施。

| 企业需求 | 传统工具 <br><sub>工作流优先</sub> | SDK <br><sub>代码优先</sub> | **Refly（技能操作系统）** |
| :--- | :--- | :--- | :--- |
| **治理与复用** | 模板复制后<br><sub>需按实例重新配置</sub> | 无原生注册中心<br><sub>难以共享逻辑</sub> | **集中式技能注册中心**<br><sub>版本化、可共享的能力资产</sub> |
| **运行可靠性** | 基于触发器<br><sub>恢复能力有限</sub> | 需自定义处理逻辑 | **有状态运行时**<br><sub>内置验证与故障恢复机制</sub> |
| **SOP 执行一致性** | 工作流易随副本漂移<br><sub>难以保持一致</sub> | 依赖人工<br><sub>工程纪律约束</sub> | **企业级 SOP 确定性技能**<br><sub>受控执行，杜绝偏差</sub> |
| **部署架构** | 绑定特定实例的工作流 | 代码需手动维护<br><sub>按团队隔离</sub> | **本地优先，支持私有化部署**<br><sub>开源基础设施</sub> |
| **总体拥有成本（TCO）** | 开销随<br><sub>工作流复杂度增长</sub> | 高昂的工程<br><sub>维护成本</sub> | **极简 DSL**<br><sub>大幅降低 Token 消耗</sub> |

---

## 创建你的第一个工作流

> [!NOTE]
> 本节假设你已完成[自托管部署](https://docs.refly.ai/community-version/self-deploy/)，并可通过 `http://localhost:5700` 访问 Refly。

**步骤 1：注册与登录**

1. 在浏览器中打开 `http://localhost:5700`
2. 使用邮箱和密码完成注册
3. 配置你的首个模型提供商：
   - 点击右上角账户图标 → 设置（Settings）
   - 添加提供商（如 OpenAI、Anthropic）
   - 添加你的首个对话模型
   - 将其设为默认模型

> 📖 图文详细设置指南：[自托管部署指南](https://docs.refly.ai/community-version/self-deploy/#start-using-refly)

**步骤 2：创建工作流**

1. 在首页点击 **“新建工作流”**（New Workflow）
2. 选择模板或从零开始：
   - **空白画布**：使用可视化节点进行构建
   - **Vibe 模式**：用自然语言描述你的工作流

**示例 - 产品调研工作流**：
```text
1. Add "Web Search" node - searches for product information
2. Add "LLM" node - analyzes search results
3. Add "Output" node - formats the report
4. Connect the nodes
5. Click "Save"
```

> [!TIP]
> 若追求最快上手，建议从 Vibe 模式开始并基于模板迭代。

**步骤 3：测试工作流**

1. 点击“运行”（Run）按钮
2. 输入测试数据（例如产品 URL）
3. 实时查看执行结果
4. 若出现异常，请检查日志

---

## 使用场景

### 场景一：API 集成

**目标**：通过 REST API 在你的应用中调用工作流

**获取 API 凭证**

1. 进入“设置”（Settings）→ “API Keys”
2. 点击“生成新密钥”
3. 复制你的 API 密钥（请妥善保管！）

**发起首次 API 调用**
```bash
curl -X POST https://your-refly-instance.com/api/v1/workflows/{WORKFLOW_ID}/execute \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "product_url": "https://example.com/product"
    }
  }'
```

**响应示例**：
```json
{
  "execution_id": "exec_abc123",
  "status": "running"
}
```

**查询执行状态**
```bash
curl https://your-refly-instance.com/api/v1/executions/{execution_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

📖 **完整 API 文档**：[API 参考手册](https://github.com/refly-ai/refly/tree/main/docs/en/guide/api)




### 场景二：飞书/Lark Webhook

**目标**：当有人在飞书中发送消息时触发工作流

**前置条件**

- 拥有管理员权限的飞书（Lark）空间
- 已在 Refly 中创建工作流

**配置步骤**

1. **在 Refly 中操作**：
   - 打开你的工作流
   - 点击“设置”（Settings）→ “触发器”（Triggers）
   - 启用“Webhook 触发器”
   - 复制 Webhook URL

2. **在飞书/Lark 中操作**：
   - 访问 [api.feishu.com/apps](https://open.feishu.cn/app)
   - 创建“自定义应用”
   - 进入“事件订阅”（Event Subscriptions）
   - 将 Refly Webhook URL 粘贴至“请求地址”（Request URL）
   - 点击“添加事件”，选择“接收消息”（Receive Message）
   - 进入“版本管理与发布”，发布应用
     
3. **测试**：
   - 在飞书中搜索你的机器人并发送消息（例如 `analyze report.pdf`）
   - 工作流将自动执行，并通过 Webhook 返回结果


> ⚠️ **注意**：详细的飞书集成指南即将上线。当前请参考[API 参考手册](https://github.com/refly-ai/refly/tree/main/docs/en/guide/api)进行 Webhook 配置。


### 场景三：Claude Code 技能支持

**目标**：将你的 Refly 工作流发布为 Claude Code 技能

**快速开始**

1. **安装 Refly CLI**
```bash
npm install -g @powerformer/refly-cli
```

2. **安装技能**
```bash
# Via Refly CLI
refly skill install <skill-id>

#Via npx
npx skills add refly-ai/<skill-name>
```

3. **发布技能**
```bash
refly skill publish <skill-id>
```

该技能现已在 Claude Code、Cursor 及支持 MCP 的工作流中可用。智能体可直接将其作为工具调用！


📖 **文档**：<a href="https://github.com/refly-ai/refly-skills"><u>Refly 技能仓库</u></a> 

### 场景四：构建 Clawdbot

📖 **教程**：<a href="https://powerformer.feishu.cn/wiki/Gz4swMzn0izknZki3g4coSgvnNe"><u>Clawdbot 构建指南</u></a> 

***

## 社区与支持

- 🌟 **[在 GitHub 上 Star](https://github.com/refly-ai/refly)**：你的支持是我们持续开发的动力！
- 💬 **[加入 Discord](https://discord.com/invite/YVuYFjFvRC)**：参与社区交流
- 🐦 **[关注 Twitter](https://x.com/reflyai)**：获取最新动态
- 📖 **[官方文档](https://docs.refly.ai)**：完整指南与教程
- 🐛 **[提交 Issue](https://github.com/refly-ai/refly/issues)**：报告 Bug 或提出功能建议

---

## 加入我们

加入我们的社区以获取帮助、分享经验并与其他 Refly 用户交流：<a href="https://docs.refly.ai/community/contact-us"><u>Refly 社区</u></a>

---

## 贡献指南

欢迎贡献代码，请参阅我们的[贡献指南](CONTRIBUTING.md)。同时，也请考虑在社交媒体、活动和会议上分享 Refly，支持我们的项目。

> 我们正在寻找贡献者协助将 Refly 翻译为中文或英文以外的其他语言。如有兴趣，请参阅[贡献指南](CONTRIBUTING.md)了解详情。

---

## ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=refly-ai/refly&type=Date)](https://star-history.com/#refly-ai/refly&Date)

## 📜 许可证

本仓库采用 [ReflyAI 开源许可证](LICENSE) 授权，该协议基于 Apache 2.0 许可证并附加了部分限制条款。