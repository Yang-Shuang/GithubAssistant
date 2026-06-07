<a href="https://www.youtube.com/watch?v=5AWoGo-L16I" target="_blank" rel="noopener noreferrer">
  <img width="1339" height="607" alt="rowboat-github-2" src="https://github.com/user-attachments/assets/fc463b99-01b3-401c-b4a4-044dad480901" />
</a>

<h5 align="center">

<p align="center" style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <a href="https://trendshift.io/repositories/13609" target="blank">
    <img src="https://trendshift.io/api/badge/repositories/13609" alt="rowboatlabs/rowboat | Trendshift" width="250" height="55"/>
  </a>
</p>

<p align="center">
    <a href="https://www.rowboatlabs.com/" target="_blank" rel="noopener">
    <img alt="Website" src="https://img.shields.io/badge/Website-10b981?labelColor=10b981&logo=window&logoColor=white">
  </a>
  <a href="https://discord.gg/wajrgmJQ6b" target="_blank" rel="noopener">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white&labelColor=5865F2">
  </a>
  <a href="https://x.com/intent/user?screen_name=rowboatlabshq" target="_blank" rel="noopener">
    <img alt="Twitter" src="https://img.shields.io/twitter/follow/rowboatlabshq?style=social">
  </a>
  <a href="https://www.ycombinator.com" target="_blank" rel="noopener">
    <img alt="Y Combinator" src="https://img.shields.io/badge/Y%20Combinator-S24-orange">
  </a>
</p>

# Rowboat  
**开源 AI 协作者，将工作转化为知识图谱并自动执行操作**

</h5>

Rowboat 可连接你的邮箱和会议记录，构建长生命周期的知识图谱，并利用这些上下文信息辅助你在本地设备上高效完成工作——全程保持隐私。

你可以尝试以下操作：
- `Build me a deck about our next quarter roadmap` → 基于知识图谱上下文自动生成 PDF 演示文稿
- `Prep me for my meeting with Alex` → 提取过往决策、待办问题和相关讨论，生成精简简报或语音备忘录
- 通过实时笔记追踪人物、公司或话题动态
- 随时可视化、编辑和更新知识图谱（底层仅为 Markdown）
- 录制语音备忘录，自动提取并更新图谱中的关键要点

下载最新版（支持 Mac/Windows/Linux）：[Download](https://www.rowboatlabs.com/downloads)

⭐ 如果你觉得 Rowboat 有用，请给仓库点个 Star。这能帮助更多人发现它。

## Demo
[![Demo](https://github.com/user-attachments/assets/8b9a859b-d4f1-47ca-9d1d-9d26d982e15d)](https://www.youtube.com/watch?v=7xTpciZCfpw)

[观看完整视频](https://www.youtube.com/watch?v=7xTpciZCfpw)

---

## 安装

**下载最新版（支持 Mac/Windows/Linux）：** [Download](https://www.rowboatlabs.com/downloads)

**所有发布版本文件：**   https://github.com/rowboatlabs/rowboat/releases/latest

### Google 服务配置
要连接 Google 服务（Gmail、日历和云端硬盘），请查阅 [Google 服务配置指南]。

### 语音输入
如需启用语音输入和语音笔记（可选），请在 `~/.rowboat/config/deepgram.json` 中添加 Deepgram API Key。

### 语音输出
如需启用语音输出（可选），请在 `~/.rowboat/config/elevenlabs.json` 中添加 ElevenLabs API Key。

### 网页搜索
如需使用 Exa 研究搜索（可选），请在 `~/.rowboat/config/exa-search.json` 中添加 Exa API Key。

### 外部工具
如需启用外部工具（可选），可通过在 `~/.rowboat/config/composio.json` 中添加 API Key，接入任意 MCP Server 或使用 Composio 工具。

所有 API Key 文件均使用以下格式：
```
{
  "apiKey": "<key>"
}
```

## 核心功能

Rowboat 是一款**本地优先的 AI 协作者**，具备以下能力：
- **记忆重要上下文**：自动记住你无需重复说明的信息（人物、项目、决策、承诺等）
- **理解当前语境**：精准识别当下最相关的内容（如会前准备、回复邮件时、撰写文档时）
- **辅助执行操作**：通过起草、总结、规划和生成实际产出物（简报、邮件、文档、PDF 幻灯片）来推动工作

底层架构上，Rowboat 维护着一个与 Obsidian 兼容的纯 Markdown 笔记库（含反向链接）——这是一个透明且可随时查看和编辑的“工作记忆”。

## 集成服务

Rowboat 从你已有的工作流程中自动构建记忆，支持：
- **Gmail**（邮件）
- **Google 日历** 
- **Rowboat 会议记录**或 **Fireflies**

此外，它还通过 Composio.dev 内置了丰富的第三方产品集成库。

## 差异化优势

大多数 AI 工具依赖按需搜索转录文本或文档来重建上下文。

而 Rowboat 维护的是**长期有效的知识**：
- 上下文随时间持续累积
- 关系明确且可随时审查
- 笔记由你直接编辑，而非隐藏在大模型内部
- 所有内容均以纯 Markdown 格式保存在你的本地设备上

最终实现的是持续积累且不断增值的记忆体系，而非每次查询都从零开始检索。

## 使用场景

- **会前准备**：基于过往决策、讨论线程和待解决问题生成材料
- **邮件起草**：结合历史往来与承诺事项进行撰写
- **文档与演示文稿**：基于持续更新的上下文自动生成（含 PDF 幻灯片）
- **跟进管理**：自动记录决策、行动项和负责人，确保事事有回音
- **本地辅助操作**：创建文件、总结为笔记，并使用本地工具执行工作流（所有操作均明确可见且可审核）

## 实时笔记

实时笔记会自动保持更新。在任意笔记中输入 `@rowboat` 即可创建一条。 

- 追踪竞争对手或市场话题（覆盖 X、Reddit 及新闻源）
- 监控特定人物、项目或交易动态（涵盖全网信息或个人通讯记录）
- 持续汇总你关心的任何主题内容

所有内容均自动写回你的本地 Markdown 知识库。运行哪些任务及执行时机完全由你掌控。

## 支持自定义模型

Rowboat 兼容你偏好的任意模型配置：
- **本地模型**：通过 Ollama 或 LM Studio 运行
- **云端托管模型**：支持自带 API Key 或服务提供商
- 随时切换模型，且数据始终保留在你的本地 Markdown 知识库中

## 通过 MCP 扩展工具能力

Rowboat 可通过**模型上下文协议 (MCP)**连接外部工具和服务。
这意味着你可以接入搜索引擎、数据库、CRM、客服工具及自动化流程——或企业内部自有系统。

示例：Exa（网页搜索）、Twitter/X、ElevenLabs（语音合成）、Slack、Linear/Jira、GitHub 等。

## 本地优先设计

- 所有数据均以纯 Markdown 格式存储在本地
- 无私有格式限制，避免厂商锁定
- 你可随时查看、编辑、备份或删除所有内容

---
<div align="center">

[Discord](https://discord.gg/wajrgmJQ6b) · [Twitter](https://x.com/intent/user?screen_name=rowboatlabshq)
</div>