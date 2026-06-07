<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/pai-logo-v7.png">
  <source media="(prefers-color-scheme: light)" srcset="./images/pai-logo-v7.png">
  <img alt="PAI Logo" src="./images/pai-logo-v7.png" width="300">
</picture>

<br/>
<br/>

# Personal AI Infrastructure

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=24&pause=1000&color=60A5FA&center=true&vCenter=true&width=600&lines=Everyone+needs+access+to+the+best+AI.;AI+should+magnify+everyone.;Your+Life+Operating+System.)](https://github.com/danielmiessler/Personal_AI_Infrastructure)

<br/>

<!-- Social Proof -->
![Stars](https://img.shields.io/github/stars/danielmiessler/Personal_AI_Infrastructure?style=social)
![Forks](https://img.shields.io/github/forks/danielmiessler/Personal_AI_Infrastructure?style=social)
![Watchers](https://img.shields.io/github/watchers/danielmiessler/Personal_AI_Infrastructure?style=social)

<!-- Project Health -->
![Release](https://img.shields.io/github/v/release/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=github&color=8B5CF6)
![Last Commit](https://img.shields.io/github/last-commit/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=git&color=22C55E)
![Open Issues](https://img.shields.io/github/issues/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=github&color=F97316)
![Open PRs](https://img.shields.io/github/issues-pr/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=github&color=EC4899)
![License](https://img.shields.io/github/license/danielmiessler/Personal_AI_Infrastructure?style=flat&color=60A5FA)

<!-- Metrics -->
![Discussions](https://img.shields.io/github/discussions/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=github&label=Discussions&color=EAB308)
![Commit Activity](https://img.shields.io/github/commit-activity/m/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=git&label=Commits%2Fmo&color=F59E0B)
![Repo Size](https://img.shields.io/github/repo-size/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=database&label=Repo%20Size&color=D97706)

<!-- Content -->
[![Get Started](https://img.shields.io/badge/🚀_Get_Started-Install-22C55E?style=flat)](#-installation)
[![Release v5.0.0](https://img.shields.io/badge/📦_Release-v5.0.0-8B5CF6?style=flat)](Releases/v5.0.0/)
[![Algorithm v6.3.0](https://img.shields.io/badge/Algorithm-v6.3.0-D97706?style=flat)](Releases/v5.0.0/.claude/PAI/ALGORITHM/v6.3.0.md)
[![Pulse](https://img.shields.io/badge/Pulse-included-3B82F6?style=flat)](Releases/v5.0.0/.claude/PAI/PULSE/)
[![Contributors](https://img.shields.io/github/contributors/danielmiessler/Personal_AI_Infrastructure?style=flat&logo=githubsponsors&logoColor=white&label=Contributors&color=EC4899)](https://github.com/danielmiessler/Personal_AI_Infrastructure/graphs/contributors)

<!-- Tech Stack -->
[![Built with Claude](https://img.shields.io/badge/Built_with-Claude-D4A574?style=flat&logo=anthropic&logoColor=white)](https://claude.ai)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Bun](https://img.shields.io/badge/Bun-000000?style=flat&logo=bun&logoColor=white)](https://bun.sh)
[![Community](https://img.shields.io/badge/Community-5865F2?style=flat&logo=discord&logoColor=white)](https://danielmiessler.com/upgrade)

<br/>

**概述：** [PAI 是什么](#what-pai-is) · [核心原则](#principles) · [功能特性](#features)

**快速开始：** [安装指南](#-installation) · [版本发布](Releases/) · [技能包](Packs/)

**资源文档：** [常见问题](#-faq) · [发展路线图](#-roadmap) · [社区交流](#-community) · [贡献指南](#-contributing)

<br/>

[![PAI Overview Video](https://img.youtube.com/vi/Le0DLrn7ta0/maxresdefault.jpg)](https://youtu.be/Le0DLrn7ta0)

**[观看完整 PAI 演示视频](https://youtu.be/Le0DLrn7ta0)** | **[阅读：真正的物联网（The Real Internet of Things）](https://danielmiessler.com/blog/the-real-internet-of-things)**

---

</div>

> [!IMPORTANT]
> **PAI v5.0.0 — 生活操作系统** —— PAI 历史上最大的版本更新。PAI 不再仅仅是“AI 脚手架”，而是一个完整的**生活操作系统（Life Operating System）**，包含统一的 **Pulse** 守护进程（位于 `localhost:31337` 的生活仪表盘）、**DA**（数字助手）身份层、**Algorithm v6.3.0**（当前状态 → 理想状态，七阶段流程，基于分类器的模式与等级划分）、**ISA** 基础原语（通用的“理想状态”描述）、45 项技能、171 个工作流、37 个钩子（hooks），以及通过隔离区实现的结构性隐私保护。
>
> **[v5.0.0 发布说明 →](Releases/v5.0.0/README.md)** | **[所有版本 →](Releases/)**
>
> **一键安装：** `curl -sSL https://ourpai.ai/install.sh | bash`
>
> 从 v4.x 升级？这是一个全新的系统，而非补丁。请先阅读[迁移指南](Releases/v5.0.0/README.md#migration-guide-from-v4x)。

<div align="center">

# AI 应该放大每个人的能力——而不仅仅是那前 1%。

</div>

## PAI 是什么

PAI 是一个生活操作系统（Life Operating System）。它记录你是谁、你在意什么以及你的目标所在，然后通过了解你的 AI 助你达成目标。系统由三层架构叠加而成：

- **PAI** —— 操作系统本身。包含技能、记忆、算法、你的 Telos（终极目标）和身份文件。
- **Pulse** —— 位于 `localhost:31337` 的生活仪表盘。在这里你可以直观地查看自己的状态、目标和进度。
- **DA** —— 你的数字助手（Digital Assistant）。与你对话的声音与人格化界面。

该系统首先为个人用户设计，但相同的架构同样适用于团队、公司或任何希望明确自身定位并朝目标迈进的组织实体。

---

## 核心原则

### 以人为本，技术为辅

PAI 将人置于核心位置，而非工具本身。技术的存在是为了改善人们的生活，而不是反过来。每一项设计决策都始于同一个问题：这能为运行它的用户带来什么价值？

### 生活操作系统，而非代理工具箱

PAI 记录你在意的事物——目标、工作、人际关系、健康、财务等——并帮助你在所有这些领域追求理想状态。它会编写代码、运行代理（agents）并完成人们通常认为属于 AI 工具的工作，但这些只是服务于更大目标的**能力**。核心始终是你的生活，而不是工具本身。

### 以“理想状态”驱动一切

AI 面临的最大未解难题是：没有人能真正定义某项任务的“好”或“完成”究竟意味着什么。PAI 围绕“理想状态（Ideal State）”这一概念构建——特别是从当前状态到理想状态的过渡过程，并将其贯穿系统的每一层。

其核心表达形式是 **ISA**（理想状态产物，Ideal State Artifact）。ISA 类似于软件领域的产品需求文档（PRD），它定义了“完成”的模样，以便你朝着目标构建。区别在于 ISA 具有通用性——适用于任何创造性任务，从设计、艺术、哲学到工程与战略。系统会将理想状态拆解为离散的 **ISC**（理想状态标准，Ideal State Criteria），这些标准既填充文档内容，也作为验证项使用。这就是 PAI 在任何类型工作中向理想状态逼近的方法论。

### 单一数字助手将是所有人接入 AI 的界面

我在 2016 年的文章 [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things) 中曾论述过这一点，如今我比当时更加确信。发展轨迹非常清晰：聊天机器人 → 代理（agents）→ 助手（assistants）。我们都在构建相同的东西，而终点是每人一个 DA。

TRIOT 包含四个核心思想，也是 PAI 的基石：

- **数字助手** —— 每人一个 DA，作为你接入所有 AI 的主要界面
- **万物皆 API** —— 每个产品、服务、人与地点都变得可寻址（addressable）
- **DA 动态生成你的界面** —— 告别传统应用和仪表盘；DA 按需即时组装所需的一切
- **由你定义理想状态，AI 助你达成** —— 整个系统始终指向你的 Telos

这正是 PAI 所追求的方向。

---

## 功能特性

### 优先使用纯文本而非封闭存储

强烈倾向使用纯文本和 Markdown。PAI 尽可能避免使用 SQLite、Postgres 等不透明（opaque）的数据库。所有内容都应保持透明且可解析——供你本人、你的 DA、`rg` 或其他任何工具读取。如果你无法用 `cat` 直接查看它，我们就不需要它。

### 上下文脚手架 > 模型本身

大多数人在使用 AI 时犯的错误是：未能提供全局视角的上下文。PAI 本质上是一个为智能模型提供正确上下文的系统——关于你本人、你想达成的目标、以及可用的工具——从而使它们真正帮助你实现理想状态。模型的重要性远低于围绕它的上下文设计。

### “良药苦口”式的工程实践

上下文脚手架的反面：随着模型能力增强，它们对具体指令的依赖会减少。我们持续审计 PAI 以移除那些在提供正确上下文和工具后显得过于冗长或教条的指导语。系统会随着模型的变大而变得更精简。

### 文件系统即上下文，无需 RAG

自 2025 年 6 月起，PAI 已完全避免使用 RAG（检索增强生成）。结合带交叉引用的富文本与 ripgrep 等快速搜索工具，我们获得了人们通常期望从 RAG 中获得的一切功能——同时避免了嵌入计算的复杂性、检索的不稳定性以及保真度损失。你的文件系统就是索引。

### 复利式记忆系统

基于纯文本的记忆体系，记录你做过的事、学到的知识以及值得保留的内容，并将其作为输入反馈给未来的工作流。包含三个层级（WORK、KNOWLEDGE、LEARNING）以及跨人、公司、思想与研究的类型化图谱。

### 自我改进循环

PAI 会捕获关于“什么做得好/不好”的信号——显式评分、情感分析、验证结果、满意度等，并利用这些信号进行自我优化。执行工作的系统同时也是变得更好的系统。

### Algorithm（算法）

一套定制算法，驱动从当前状态到理想状态的过渡过程。它基于科学方法构建了一个七阶段循环，并以 Deutsch 提出的“难以变动的解释”作为衡量“好”的标准。它是 PAI 的引力中心——所有非琐碎任务都会经过它的处理。

### 技能即确定性执行单元

一套偏向确定性代码执行的技能系统。层级结构为：代码 → 用于运行代码的 CLI → 调用该 CLI 的工作流 → 负责在工作流间路由的 SKILL.md。技能是容器；SKILL.md 是入口；实际工作尽可能使用真实代码。Prompt 包裹代码，而非代码包裹 Prompt。

### 思考类技能

一套丰富的自定义思考技能库——包括第一性原理、委员会辩论、红队测试、根因分析、系统思维、迭代深度探索、孔径振荡等——Algorithm 会从中调用以提升整个系统的决策质量。

---

## 🚀 安装指南

> [!CAUTION]
> **项目处于活跃开发阶段** —— PAI 正在快速演进。请预期会有破坏性变更、结构重组和频繁更新。

### 使用你的 AI 进行安装与运行

我们非常推崇基于 AI 的 PAI 安装与修改方式。成功安装后，将你的 AI 指向系统本身——升级版本、添加技能、修改钩子（hooks）、调整设置或修复任何故障。你的 AI 在初期能为你做最重要的事情是：将你现有的自定义上下文——笔记、项目状态、偏好设置、身份、历史记录等——全部导入 `PAI/USER/` 目录，使 PAI 从第一天起就认识你。告诉你的 DA：“帮我迁移我的上下文到 PAI/USER/。”该系统专为 AI 操作而设计；请充分依赖它。

### 一键安装（推荐）

```bash
curl -sSL https://ourpai.ai/install.sh | bash
```

就这么简单。安装向导会自动处理 Bun、Git 和 Claude Code 的验证、ElevenLabs API Key（可选）、DA 身份设置、语音选择、Pulse launchd 注册以及最终校验。在覆盖任何内容前，现有的 `~/.claude/` 目录会自动备份至 `~/.claude.backup-{TIMESTAMP}`。

**希望先审查脚本？** [在此阅读安装脚本](https://ourpai.ai/install.sh) 后再执行管道命令。

### 手动安装（克隆 + 运行）

```bash
git clone https://github.com/danielmiessler/Personal_AI_Infrastructure.git
cd Personal_AI_Infrastructure/Releases/v5.0.0
cp -R .claude ~/
cd ~/.claude && ./install.sh
```

**安装向导将执行以下操作：**
- 验证 Bun、Git 和 Claude Code 是否已安装
- 提示输入 ElevenLabs API Key（可跳过——语音功能将回退到桌面通知）
- 启动 DA 身份设置向导（名称 + 语音 + 人格）
- 将 Pulse 注册为 launchd 服务 (`com.pai.pulse`)
- 运行系统校验

### 安装后操作

```bash
open http://localhost:31337    # 打开生活仪表盘
```

然后在 Claude Code 中运行 `/interview`。你的 DA 将引导你完成以下步骤：

1. **阶段 1 — TELOS：** 使命、目标、信念、智慧、挑战、书籍、心智模型、叙事框架
2. **阶段 2 — IDEAL_STATE：** 对你而言，成功是什么样子？
3. **阶段 3 — Preferences：** 工具、规范、工作风格
4. **阶段 4 — Identity：** DA 人格最终调优

这是最重要的步骤。**如果没有 TELOS，你的 DA 将缺乏优化的基准。**

### 从 v4.x 升级

> [!IMPORTANT]
> v5.0.0 是一个全新的系统，而非补丁。安装前请阅读 **[完整迁移指南](Releases/v5.0.0/README.md#migration-guide-from-v4x)**。

快速路径：

```bash
# 1. 备份现有安装
cp -R ~/.claude ~/.claude.backup-$(date +%Y%m%d)

# 2. 安装 v5.0.0（使用上方一键命令）或通过手动克隆安装
curl -sSL https://ourpai.ai/install.sh | bash

# 3. 打开生活仪表盘并运行访谈流程
open http://localhost:31337
```

如果你在 v4.x 中有个人内容（笔记、项目状态、自定义规则），请告诉你的 DA：“帮我迁移旧内容到 PAI/USER/ 结构中。” **Migrate** 技能会从 `.md`/`.markdown`/`.txt`、Obsidian、Notion、Apple Notes 等来源摄入数据，根据 v5 分类体系（TELOS, KNOWLEDGE, PROJECTS, FEED 等）对每个片段进行分类，并附带溯源信息提交。

**升级后检查清单：**
- [ ] Pulse 运行正常：`curl -s http://localhost:31337/api/pulse/health | jq`
- [ ] 语音通知测试：`curl -s -X POST http://localhost:31337/notify -H "Content-Type: application/json" -d '{"message": "Hello from your DA"}'`
- [ ] 仪表盘渲染正常：`open http://localhost:31337`
- [ ] `PAI/USER/DA_IDENTITY.md` 中已填充 DA 身份信息
- [ ] `PAI/USER/TELOS/` 下已捕获 TELOS 数据

---

## 📦 PAI 技能包（Packs）

技能包是独立、可 AI 安装的附加能力，你可以将其添加到任何 AI 编码工具中而无需安装完整的 PAI。每个技能包都是一个自包含的 Prompt，你的 DA 可以读取并执行——将 DA 指向该包目录并说“安装这个”，其余工作由它自动完成。

**[浏览所有技能包 →](Packs/)**

---

## ❓ 常见问题（FAQ）

### PAI 与直接使用 Claude Code 有什么区别？

PAI 原生构建于 Claude Code 之上，并且我们有意保持这种架构关系。选择 Claude Code 是因为其钩子系统、上下文管理和代理式架构是个人 AI 基础设施的最佳基础。

PAI 不是 Claude Code 的替代品——它是叠加在其之上的层，使 Claude Code *成为你的*：

- **持久化记忆** —— 你的 DA 会记住过去的会话、决策和学习内容
- **自定义技能** —— 针对你高频操作场景的专业能力
- **专属上下文** —— 目标、联系人、偏好设置等均可直接调用，无需重复说明
- **智能路由** —— 输入“研究一下”，系统会自动触发合适的工作流
- **自我改进** —— 系统会根据学习到的内容自动调整自身

可以这样理解：Claude Code 是引擎，PAI 是让这辆车成为 *你的* 车的所有其他部件。

### PAI 与 Claude Code 内置功能有什么区别？

Claude Code 提供了强大的基础原语——钩子（hooks）、斜杠命令、MCP 服务器、上下文文件等。它们是独立的构建模块。

PAI 是基于这些原语构建的完整系统。它将一切串联起来：你的目标决定技能配置，技能生成记忆内容，记忆优化后续响应。PAI 将 Claude Code 的积木整合成了一个连贯的个人 AI 平台。

### PAI 是否仅适用于 Claude Code？

PAI 是 Claude Code 原生架构。我们相信 Claude Code 的钩子系统、上下文管理和代理能力使其成为个人 AI 基础设施的最佳平台，PAI 的设计正是为了充分利用这些特性。

话虽如此，PAI 的核心概念（技能、记忆、算法）具有通用性，且代码基于 TypeScript 和 Bash——因此欢迎社区成员将其适配到其他平台。

### 这与 Fabric 有什么区别？

[Fabric](https://github.com/danielmiessler/fabric) 是一套针对特定任务的 AI Prompt（模式）集合。它侧重于 *该问 AI 什么*。

PAI 是 *你的 DA 如何运作* 的基础设施——包含记忆、技能、路由、上下文和自我改进机制。两者互补。许多 PAI 用户会将 Fabric 的 Prompt 集成到自己的技能中。

### 如果我不小心搞坏了系统怎么办？

恢复流程非常直接：

- **先备份** —— 任何升级前执行：`cp -r ~/.claude ~/.claude-backup-$(date +%Y%m%d)`
- **USER/ 目录安全** —— `USER/` 中的自定义内容永远不会被安装程序或升级覆盖
- **配置合并而非覆盖** —— 安装程序仅更新身份和版本字段；你的钩子、状态栏和自定义配置均会保留
- **基于 Git 的版本控制** —— 全程使用版本管理，需要时随时回滚
- **历史记录保留** —— DA 的记忆不会因操作失误而丢失
- **DA 可协助修复** —— 既然它参与了构建，自然也能帮你修复问题
- **重新安装** —— 再次运行安装程序；它会检测现有安装并智能合并

---

## 🎯 发展路线图

| 功能 | 描述 |
|---------|-------------|
| **本地模型支持** | 使用本地模型（Ollama、llama.cpp）运行 PAI，实现隐私保护与成本可控 |
| **细粒度模型路由** | 根据任务复杂度将不同请求分发至不同的模型 |
| **远程访问** | 随时随地通过移动端、Web 或其他设备访问你的 PAI |
| **外拨语音通话** | 支持主动发起电话的语音能力 |
| **外部通知系统** | 针对 Email、Discord、Telegram、Slack 的健壮通知机制 |

---

## 🌐 社区交流

**GitHub Discussions：** [加入讨论](https://github.com/danielmiessler/Personal_AI_Infrastructure/discussions)

**Community Discord：** PAI 与其他 AI 项目一同在 [社区 Discord](https://danielmiessler.com/upgrade) 中交流探讨

**Twitter/X：** [@danielmiessler](https://twitter.com/danielmiessler)

**博客：** [danielmiessler.com](https://danielmiessler.com)

### Star 增长历史

<a href="https://star-history.com/#danielmiessler/Personal_AI_Infrastructure&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=danielmiessler/Personal_AI_Infrastructure&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=danielmiessler/Personal_AI_Infrastructure&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=danielmiessler/Personal_AI_Infrastructure&type=Date" />
 </picture>
</a>

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！请查看我们的 [GitHub Issues](https://github.com/danielmiessler/Personal_AI_Infrastructure/issues) 获取待办任务。

1. **Fork 本仓库**
2. **进行修改** —— Bug 修复、新增技能、文档优化等
3. **充分测试** —— 在干净环境中安装以验证功能
4. **提交 PR** —— 附带示例代码与测试结果证明

---

## 📜 开源协议

MIT License - 详见 [LICENSE](LICENSE)。

---

## 🙏 致谢

**Anthropic 及 Claude Code 团队** —— 首要感谢。你们正在以超越任何人的速度推动 AI 向前发展。Claude Code 是使这一切成为可能的基石。

**[IndyDevDan](https://www.youtube.com/@indydevdan)** —— 提供了关于元提示（meta-prompting）和自定义代理的优秀视频，启发了 PAI 的部分设计。

### 贡献者

**[fayerman-source](https://github.com/fayerman-source)** —— 负责 Google Cloud TTS 提供商集成及 Linux 音频支持。

**Matt Espinoza** —— 为 PAI 2.3 版本提供了大量测试、创意与反馈，并参与了路线图规划。

---

## 💜 支持本项目

<div align="center">

<a href="https://github.com/sponsors/danielmiessler"><img src="https://img.shields.io/badge/Sponsor-❤️-EA4AAA?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="Sponsor"></a>

**PAI 将永远免费且开源。如果你认为它有价值，可以 [赞助本项目](https://github.com/sponsors/danielmiessler)。**

</div>

---

## 📚 延伸阅读

- [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things) —— PAI 背后的愿景
- [AI's Predictable Path: 7 Components](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024) —— AI 发展路径的可视化解析
- [Building a Personal AI Infrastructure](https://danielmiessler.com/blog/personal-ai-infrastructure) —— PAI 完整演示与示例

---

<details>
<summary><strong>📜 更新历史</strong></summary>

<br/>

**v5.0.0 (2026-04-30) — 生活操作系统（Life Operating System）**
- **Pulse** —— 统一守护进程（端口 31337）：语音、钩子、可观测性、定时任务、生活仪表盘（22 个路由）、Wiki API，可选 Telegram/iMessage 桥接。取代了所有之前的独立服务。
- **DA** —— 数字助手身份层。PRINCIPAL_IDENTITY + DA_IDENTITY 配对，在会话启动时加载。`/interview` 引导你为 DA 命名、选择语音并捕获 TELOS。
- **Algorithm v6.3.0** —— 七阶段循环（OBSERVE → THINK → PLAN → BUILD → EXECUTE → VERIFY → LEARN）。基于 Sonnet 的模式分类器会为每个 Prompt 选择 MINIMAL/NATIVE/ALGORITHM 模式及等级（E1–E5）。支持闭卷思考能力、语音阶段播报。验证机制包含实时探针、承诺边界处的顾问调用，以及 E4/E5 级别的跨厂商审计。
- **ISA** —— 理想状态产物原语。单文档结构，含十二个章节（Problem → Vision → Out of Scope → Principles → Constraints → Goal → Criteria → Test Strategy → Features → Decisions → Changelog → Verification），五种身份映射（描述、测试框架、构建验证、完成条件、系统记录）。由 **ISA 技能**（Scaffold, Interview, CheckCompleteness, Reconcile, Seed, Append）管理，附带十二个覆盖 E1–E5 的参考示例。
- **隔离区 + 发布工具链** —— 隐私具备结构性保障。`containment-zones.ts` 声明每个目录的隐私区域；`ContainmentGuard` PreToolUse 钩子阻止跨区数据泄露；每次公开发布均经过 12 道安全关卡检查；两阶段发布流程（stage → publish）永不自动级联执行。
- **Memory v7.6** —— 按用途结构化：WORK（活跃任务 ISA）、KNOWLEDGE（类型化图谱：People, Companies, Ideas, Research, Blogs）、LEARNING（元模式）、RELATIONSHIP（DA-Principal 笔记）、OBSERVABILITY（每次工具调用 + 钩子触发 + 满意度信号）、STATE（会话注册表）。
- **45 项公开技能、171 个工作流、37 个钩子** —— 技能为自激活的可组合领域单元；钩子在 SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStop, PreCompact, SessionEnd 等节点触发。
- **一键安装器** —— `curl -sSL https://ourpai.ai/install.sh | bash`。自动备份现有 `~/.claude/`，运行 DA 身份向导，注册 Pulse 为 launchd 服务并校验。
- [完整发布说明 + 迁移指南](Releases/v5.0.0/README.md)

**v4.0.3 (2026-03-01) — 社区 PR 补丁**
- Inference.ts 中 JSON 数组解析修复
- CONTEXT_ROUTING.md 移除 29 个失效引用
- WorldThreatModelHarness PAI_DIR 可移植性优化
- v2.5/v3.0 升级用户的上下文迁移支持
- [发布说明](Releases/v4.0.3/README.md)

**v4.0.2 (2026-03-01) — Bug 修复补丁**
- 13 项精准修复：Linux 兼容性、安装程序、状态栏、钩子逻辑
- 跨平台 OAuth Token 提取、GNU coreutils tr 命令兼容
- Inference 守卫优化（约节省 15s）、血缘追踪、死代码清理
- [发布说明](Releases/v4.0.2/README.md)

**v4.0.1 (2026-02-28) — 升级路径与偏好设置**
- 新增带备份、合并及升级后检查清单的升级文档
- 状态栏与安装程序支持配置温度单位（华氏/摄氏）
- FAQ 修复：移除过时的 Python 引用，优化恢复指导说明
- [发布说明](Releases/v4.0.1/README.md)

**v4.0.0 (2026-02-27) — 精简与强化（Lean and Mean）**
- 38 个扁平技能目录 → 12 级层级分类（顶层目录减少 68%）
- 移除废弃系统：Components/, DocRebuild, RebuildSkill
- CLAUDE.md 模板系统，配合 BuildCLAUDE.ts + SessionStart 钩子
- Algorithm v3.5.0（较 v1.4.0 升级）
- 全面安全清理（清洗 33+ 个文件）
- 更新所有版本引用、修复 Electron 崩溃问题
- 63 项技能，21 个钩子，180 个工作流，14 个代理
- [发布说明](Releases/v4.0.0/README.md)

**v3.0.0 (2026-02-15) — 算法成熟（The Algorithm Matures）**
- Algorithm v1.4.0：新增约束提取与构建漂移预防机制
- 持久化 PRD 支持与并行循环执行
- 完整安装程序含 GUI 向导
- 新增 10 项技能、代理团队/蜂群模式、语音人格系统
- 38 项技能，20 个钩子，162 个工作流
- [发布说明](Releases/v3.0/README.md)

**v2.5.0 (2026-01-30) — 深度思考，快速执行（Think Deeper, Execute Faster）**
- 双阶段能力选择：THINK 阶段钩子提示与 ISC 验证对齐
- 思考工具配套 Justify-Exclusion 机制：Council、RedTeam、FirstPrinciples 等采用“排除法”而非“勾选法”
- 默认并行执行：独立任务通过并发代理生成实现并行运行
- 28 项技能，17 个钩子，356 个工作流
- [发布说明](Releases/v2.5/README.md)

**v2.4.0 (2026-01-23) — 算法上线（The Algorithm）**
- 通用问题解决系统，支持 ISC（理想状态标准）追踪
- 29 项技能，15 个钩子，331 个工作流
- 引入“惊喜感”作为核心结果指标
- 增强安全机制：强制 AllowList 策略
- [发布说明](Releases/v2.4/README.md)

**v2.3.0 (2026-01-15) — 完整版本回归（Full Releases Return）**
- 完整的 `.claude/` 目录版本发布，支持持续学习机制
- 显式与隐式评分捕获系统
- 增强型钩子系统：新增 14 个生产级钩子
- 状态栏集成学习信号显示
- [发布说明](Releases/v2.3/README.md)

**v2.1.1 (2026-01-09) — MEMORY 系统迁移**
- 历史管理系统合并至核心，升级为 MEMORY System

**v2.1.0 (2025-12-31) — 模块化架构（Modular Architecture）**
- 源代码采用真实文件组织，替代内嵌 Markdown

**v2.0.0 (2025-12-28) — PAI v2 发布**
- 模块化架构，支持独立技能扩展
- Claude Code 原生设计

</details>

---

<div align="center">

**由 [Daniel Miessler](https://danielmiessler.com) 与 PAI 社区 ❤️ 打造**

*Augment yourself.*

</div>