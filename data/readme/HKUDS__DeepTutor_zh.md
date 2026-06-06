<div align="center">

<p align="center"><img src="assets/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="assets/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor：基于智能体的个性化辅导系统

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="Docs — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-BCDCF7"></a>&nbsp;
  <a href="assets/README/README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/HKUDS/DeepTutor?style=flat-square&color=brightgreen)](https://github.com/HKUDS/DeepTutor/releases)
[![arXiv](https://img.shields.io/badge/arXiv-2604.26962-b31b1b?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.26962)

[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/eRsjPgMU4t)
[![Feishu](https://img.shields.io/badge/Feishu-Group-00D4AA?style=flat-square&logo=feishu&logoColor=white)](./Communication.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-07C160?style=flat-square&logo=wechat&logoColor=white)](https://github.com/HKUDS/DeepTutor/issues/78)

[功能特性](#-key-features) · [快速入门](#-get-started) · [探索 DeepTutor](#-explore-deeptutor) · [智能辅导机器人（TutorBot）](#-tutorbot--persistent-autonomous-ai-tutors) · [命令行工具（CLI）](#%EF%B8%8F-deeptutor-cli--agent-native-interface) · [多用户部署](#-multi-user--shared-deployments-with-per-user-workspaces) · [社区生态](#-community--ecosystem)

</div>

---

> 🤝 **我们欢迎任何形式的贡献！** 请在 [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498) 上投票或提出新的路线图项目，并查看我们的 [Contributing Guide](CONTRIBUTING.md) 了解分支策略、编码规范及入门指南。

### 📦 版本发布

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — 稳定性增强与 v1.4.1 优化：解锁 Gemini 2.5+（支持可视化与聊天），修复 ContextVar 认证路由问题 (#485)，强化推理与原生命令标签协议，全面优化流式传输体验，新增可折叠的“最近”侧边栏，以及 Lemonade 本地提供商支持。

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — 安全与稳定性补丁：锁定 TutorBot 工具沙箱，实现按用户资源隔离，为支持视觉的提供商添加多模态图片回退机制，新增用于调用 TutorBot 的 HTTP/SSE API，以及修复 v1.4.0 聊天回归问题。

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — v1.4 正式版：新增自动模式、三层记忆架构、智能体驱动的 Deep Research / Solve / Question，LlamaIndex RAG 重构，Visualize/Animator 合并，以及推理效率标准化、工具 Schema 回退和重启安全的轮次运行时。

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — 三层记忆工作台（L1/L2/L3），所有聊天能力重构为单一智能体引擎，仅使用 LlamaIndex RAG，以及统一的设置与功能界面。

<details>
<summary><b>历史版本（超过两周前）</b></summary>

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — 远程 Docker CORS 恢复，SDK 提供商跨域 `DISABLE_SSL_VERIFY`，更安全的代码块引用，以及可选的 Matrix E2EE 插件。

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — TutorBot Zulip 与 NVIDIA NIM 支持，更安全的推理模型路由、`deeptutor start`、侧边栏提示框及会话存储同步。

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — 可选的多用户部署，含隔离的用户工作区、管理员授权、认证路由及作用域运行时访问。

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — 推理模型/提供商修复，可见的知识索引历史，以及更安全的 Co-Writer 清空/模板编辑。

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — 基于目录的聊天与 TutorBot 模型选择，更安全的 RAG 重新索引、OpenAI Responses Token 限制修复及 Skills 编辑器验证。

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — 更流畅的本地启动设置、更安全的 RAG 查询、清理的本地嵌入认证及设置页深色模式优化。

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — 书籍页面聊天持久化与重建流程、聊天到书籍的引用、增强的语言/推理处理及 RAG 文档提取加固。

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — NVIDIA NIM + Gemini 嵌入支持、统一的空间上下文（聊天历史/Skills/记忆）、会话快照及 RAG 重新索引容错。

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — 透明的嵌入端点 URL、针对无效持久化向量的 RAG 重新索引容错、推理模型输出的内存清理及 Deep Solve 运行时修复。

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — 稳定性：更安全的 RAG 路由与嵌入验证、Docker 持久化、IME 安全输入及 Windows/GBK 鲁棒性。

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — 带重新索引工作流的版本化知识库索引、重建的知识工作区、嵌入自动发现及新适配器、空间中心。

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — 持久化聊天附件（带文件预览抽屉）、附件感知能力流水线及 TutorBot Markdown 导出。

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — 文本/代码/SVG 附件、一键设置向导、Markdown 聊天导出及紧凑的知识库管理 UI。

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — 文档附件（PDF/DOCX/XLSX/PPTX）、推理思考块显示、Soul 模板编辑器及 Co-Writer 保存到笔记本。

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — 用户自定义 Skills 系统、聊天输入性能重构、TutorBot 自动启动、书籍库 UI 及可视化全屏。

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — 分阶段 Token 限制、全入口响应重新生成、RAG 与 Gemma 兼容性修复。

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — 书籍引擎“活书”编译器、多文档 Co-Writer、交互式 HTML 可视化及问题库 @提及。

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — 基于 Schema 的 Channels 标签页、RAG 单流水线整合及外部化聊天提示词。

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — 通用“立即回答”、Co-Writer 滚动同步、统一设置面板及流式传输停止按钮。

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — LaTeX 块数学重构、LLM 诊断探针、Docker + 本地 LLM 指南。

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — 可书签会话、Snow 主题、WebSocket 心跳与自动重连、嵌入注册表重构。

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — 带书签与分类的问题笔记本、Visualize 中的 Mermaid、嵌入不匹配检测、Qwen/vLLM 兼容、LM Studio & llama.cpp 支持及 Glass 主题。

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — 搜索整合（含 SearXNG 回退）、提供商切换修复及前端资源泄漏修复。

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Visualize 功能（Chart.js/SVG）、测验防重复及 o4-mini 模型支持。

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — 带速率限制重试的嵌入进度跟踪、跨平台依赖修复及 MIME 验证修复。

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — 原生 OpenAI/Anthropic SDK（弃用 litellm）、Windows Math Animator 支持、健壮 JSON 解析及完整中文国际化。

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — 热重载设置、MinerU 嵌套输出、WebSocket 修复及 Python 3.11+ 最低要求。

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — 智能体原生架构重写（约 20 万行）：Tools + Capabilities 插件模型、CLI & SDK、TutorBot、Co-Writer、引导式学习及持久化记忆。

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — 会话持久化、增量文档上传、灵活 RAG 流水线导入及完整中文本地化。

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — Docling 支持 RAG-Anything、日志系统优化及 Bug 修复。

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — 统一服务配置、按知识库选择 RAG 流水线、问题生成重构及侧边栏自定义。

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — 多提供商 LLM & 嵌入支持、全新首页、RAG 模块解耦及环境变量重构。

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — 统一 PromptManager 架构、GitHub Actions CI/CD 及 GHCR 预构建 Docker 镜像。

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Docker 部署、Next.js 16 & React 19 升级、WebSocket 安全加固及关键漏洞修复。

</details>

### 📰 新闻

> **[2026.5.22]** 🌐 我们的官方文档站点已在 [**deeptutor.info**](https://deeptutor.info/) 上线 —— 指南、参考手册与功能导览一站式集成。

> **[2026.4.19]** 🎉 我们在 111 天内达到了 2 万星！感谢大家不可思议的支持 —— 我们致力于持续迭代，为每个人提供真正个性化、智能化的辅导体验。

> **[2026.4.10]** 📄 我们的论文现已发布在 arXiv！阅读 [预印本](https://arxiv.org/abs/2604.26962) 了解更多关于 DeepTutor 背后的设计与理念。

> **[2026.4.4]** 好久不见！✨ DeepTutor v1.0.0 终于到来 —— 采用智能体原生架构演进，底层重写、搭载 TutorBot，并在 Apache-2.0 许可证下支持灵活的模式切换。新篇章已开启，我们的故事继续！

> **[2026.2.6]** 🚀 我们仅用 39 天就达到了 1 万星！衷心感谢我们不可思议的社区带来的支持！

> **[2026.1.1]** 新年快乐！加入我们的 [Discord](https://discord.gg/eRsjPgMU4t)、[微信](https://github.com/HKUDS/DeepTutor/issues/78) 或 [讨论区](https://github.com/HKUDS/DeepTutor/discussions) —— 让我们一起塑造 DeepTutor 的未来！

> **[2025.12.29]** DeepTutor 正式发布！


## ✨ 核心功能

**工作界面**

- **对话（Chat）** —— 对话、解题、测验、研究与可视化共享同一会话、知识库和引用历史，让你可以在对话中途无缝升级任务类型而不会丢失上下文。
- **协同写作（Co-Writer）** —— 分屏 Markdown 工作区，任何选中的文本均可重写、扩展或精简，可选择基于你的知识库或网络内容进行 grounding。草稿直接保存至笔记本。
- **书籍引擎（Book Engine）** —— 多智能体流水线将你的资料编译为包含 13 种区块类型的交互式“活书”：测验、闪卡、时间线、概念图、内嵌 GeoGebra 查看器、动画等。页面会进行知识库指纹标记，以便检测内容漂移。

**你的资源库**

- **知识库（Knowledge Bases）** —— 版本化且就绪 RAG 的集合，端到端基于 LlamaIndex。每次（重新）索引均可追踪、可比较且支持回滚。
- **空间（Space）** —— 个人复习图书馆，整合聊天历史、笔记本、问题库及用户自定义 Skills（`SKILL.md`），后者可切换 DeepTutor 的人格设定。
- **三层记忆** —— 仅追加的 L1 轨迹、带引用的 L2 按界面筛选事实、以及跨界面综合的 L3。通过可检查的工作台与记忆图，你可以审计 *DeepTutor* 为何知道它知道的任何内容。

**扩展性与控制权**

- **可组合工具** —— RAG、网络搜索、代码执行、推理、头脑风暴、论文搜索、GeoGebra 分析及聊天辅助（`ask_user`, `web_fetch`, `write_note`, `list_notebook`, `github_query`）。MCP 服务器可与内置功能并行接入。
- **个人智能辅导机器人（TutorBot）** —— 持久化、自主运行的辅导机器人，每个都有独立的工作区、人格（Soul）、Skills 和渠道（Telegram, Discord, Slack, Matrix, Zulip 等）。基于 [nanobot](https://github.com/HKUDS/nanobot) 构建。
- **统一设置** —— 一个草稿/应用工作台，涵盖外观、模型、嵌入、搜索、能力、记忆、MCP 服务器和工具，并共享按次调用的成本追踪。
- **原生智能体 CLI** —— 每项功能、知识库、会话和 TutorBot 均可一键调用；输出对 humans 丰富友好，对 agents 提供结构化 JSON。将 [`SKILL.md`](SKILL.md) 交给任何具备工具调用能力的 LLM，它即可自主驱动 DeepTutor。
- **可选认证** —— 默认关闭；开启后支持多用户部署（bcrypt + JWT）、管理员仪表盘及可选的 PocketBase / OAuth sidecar。

---

## 🚀 快速入门

DeepTutor 提供四种安装路径。它们共享同一工作区布局：设置文件位于启动目录下的 `data/user/settings/`（或显式设置的 `DEEPTUTOR_HOME` / `deeptutor start --home`）。对于完整应用，推荐流程为：**选择工作区目录 → 安装 → `deeptutor init` → `deeptutor start`**。

> ✨ **v1.4.2 已上线。** `pip install -U deeptutor` 将获取最新稳定版。预发布版本（如有）可通过 `pip install --pre -U deeptutor` 启用。

### 方案 1 — 从 PyPI 安装

完整本地 Web 应用 + CLI，无需克隆仓库。需要 **Python 3.11+** 和 PATH 中的 **Node.js 20+** 运行时（打包的 Next.js standalone 服务器由 `deeptutor start` 启动）。

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # 提示配置端口 + LLM 提供商 + 可选嵌入服务
deeptutor start    # 启动后端与前端；保持终端开启
```

`deeptutor init` 会提示配置后端端口（默认 `8001`）、前端端口（默认 `3782`）、LLM 提供商 / 基础 URL / API Key / 模型，以及知识库/RAG 的可选嵌入服务提供商。

运行 `deeptutor start` 后，打开终端打印的前端 URL —— 默认为 [http://127.0.0.1:3782](http://127.0.0.1:3782)。在该终端按 `Ctrl+C` 可停止后端和前端。跳过 `deeptutor init` 进行快速试用也是可以的；应用将以默认端口和空模型设置启动，稍后可在 **Settings → Models** 中配置。

### 方案 2 — 从源码安装

适用于针对代码库进行开发。请使用 **Python 3.11+** 和 **Node.js 22 LTS** 以匹配 CI 与 Docker 环境。

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# 创建虚拟环境（macOS/Linux）。Windows PowerShell：
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# 安装后端 + 前端依赖
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

源码安装在本地 `web/` 目录下以开发模式运行 Next.js；其余部分（配置布局、端口、按 `Ctrl+C` 停止）与方案 1 一致。

<details>
<summary><b>Conda 环境</b>（替代 <code>venv</code>）</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>可选安装扩展依赖</b> — dev / tutorbot / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # 测试/代码检查工具
pip install -e ".[tutorbot]"        # TutorBot 引擎 + 渠道 SDK
pip install -e ".[matrix]"          # Matrix 渠道（不含 E2EE/libolm）
pip install -e ".[matrix-e2e]"      # Matrix E2EE；需 libolm
pip install -e ".[math-animator]"   # Manim 插件；需 LaTeX/ffmpeg/系统库
```

</details>

<details>
<summary><b>前端依赖调整与开发服务器排错</b></summary>

**更改前端依赖：** 运行 `npm install --legacy-peer-deps` 刷新 `web/package-lock.json`，然后提交 `web/package.json` 和 `web/package-lock.json`。

**开发服务器卡死：** 如果 `deeptutor start` 报告存在未响应的前端进程，请停止它打印的 PID。如果没有 Next.js 进程实际在运行，说明锁文件已过期 —— 删除它们并重试：

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### 方案 3 — Docker

一个容器包含完整 Web 应用。镜像位于 GitHub Container Registry：

- `ghcr.io/hkuds/deeptutor:latest` —— 稳定版
- `ghcr.io/hkuds/deeptutor:pre` —— 预发布版（如有）

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **必须同时映射 `3782` 和 `8001`。** `3782` 提供 Web UI；`8001` 是浏览器直接调用的 FastAPI 后端 —— 容器内无代理。跳过 `8001` 映射后页面仍可加载，但 **Settings** 会显示“Backend unreachable”且无法使用。

打开 [http://127.0.0.1:3782](http://127.0.0.1:3782)。容器首次启动时会创建 `/app/data/user/settings/*.json`；请在 Web Settings 页面配置模型提供商。配置、API Key、日志、工作区文件、记忆和知识库均持久化在 `deeptutor-data` 卷中。

- **不同宿主机端口：** 更改每个 `-p host:container` 映射的左侧（例如 `-p 127.0.0.1:8088:3782`）。如果在 `/app/data/user/settings/system.json` 中修改了容器侧端口，重启后需同步更新右侧映射。
- **后台运行：** 添加 `-d`，然后使用 `docker logs -f deeptutor` 跟踪日志，`docker stop deeptutor` 停止，复用名称前执行 `docker rm deeptutor`。`deeptutor-data` 卷会在重启间保留你的设置和工作区。

**远程 Docker / 反向代理：** Web UI 在浏览器中运行，因此浏览器需要能访问的后端 URL。对于远程服务器，打开 **Settings -> Network** 或编辑 `data/user/settings/system.json`：

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` 作为兼容别名被接受，保存时会自动归一化为 `next_public_api_base_external`。CORS 使用前端 **origins**（源），而非 API URL。禁用认证时，DeepTutor 默认允许常规 HTTP/HTTPS 浏览器 origins。启用认证后，需添加精确的前端 origins：

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>连接宿主机上的 Ollama / LM Studio / llama.cpp / vLLM / Lemonade</b></summary>

在 Docker 内部，`localhost` 指的是容器本身而非你的宿主机。要访问运行在宿主机的模型服务，请使用宿主机网关（推荐）：

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

然后在 **Settings → Models** 中，将提供商 Base URL 指向 `host.docker.internal`：

- Ollama LLM：`http://host.docker.internal:11434/v1`
- Ollama embedding：`http://host.docker.internal:11434/api/embed`
- LM Studio：`http://host.docker.internal:1234/v1`
- llama.cpp：`http://host.docker.internal:8080/v1`
- Lemonade：`http://host.docker.internal:13305/api/v1`

Docker Desktop（macOS/Windows）通常无需 `--add-host` 即可解析 `host.docker.internal`。在 Linux 上，该标志是现代 Docker Engine 创建该主机名的可移植方式。

**Linux 替代方案 —— host networking：** 添加 `--network=host` 并移除 `-p` 参数。容器将直接共享宿主机网络，因此打开 [http://127.0.0.1:3782](http://127.0.0.1:3782)（或 `system.json` 中的 `frontend_port`），宿主服务可通过常规 localhost URL（如 `http://127.0.0.1:11434/v1`）访问。注意：host networking 会直接将容器端口暴露给宿主机，可能与现有服务冲突。

</details>

### 方案 4 — 仅 CLI

当你不需要 Web UI 时使用。CLI 专用包需从源码安装，而非 PyPI。

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# 创建虚拟环境（macOS/Linux）。Windows PowerShell：
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` 与完整应用共享相同的 `data/user/settings/` 布局，但跳过后端/前端端口提示，并将嵌入默认设为 **off**（若计划使用 `deeptutor kb …` 或 RAG 工具请选择 `Yes`）。它仍会写入完整的运行时布局（`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`）并提示配置活跃的 LLM 提供商和模型。

<details>
<summary><b>常用命令</b></summary>

```bash
deeptutor chat                                          # 交互式 REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

本地 `deeptutor-cli` 安装不附带 Web 资源或服务器依赖。请保留源码目录 —— 可编辑安装指向它。若后续需要添加 Web 应用，请安装 PyPI 包（方案 1）并从同一工作区运行 `deeptutor init` + `deeptutor start`。

### 配置参考

<details>
<summary><b><code>data/user/settings/</code> 下的配置文件</b> —— JSON/YAML 参考</summary>

`data/user/settings/` 下所有内容均为纯 JSON/YAML。**Settings** 页面是推荐的编辑器。

| 文件 | 用途 |
|:---|:---|
| `model_catalog.json` | LLM、嵌入和搜索提供商配置；API Key；活跃模型 |
| `system.json` | 后端/前端端口、公共 API base、CORS、SSL 验证、附件目录 |
| `auth.json` | 可选认证开关、用户名、密码哈希、Token/Cookie 设置 |
| `integrations.json` | 可选 PocketBase 及 sidecar 集成设置 |
| `interface.json` | UI 语言 / 主题 / 侧边栏偏好 |
| `main.yaml` | 运行时行为默认值与路径注入 |
| `agents.yaml` | 能力/工具的温度参数与 Token 设置 |

项目根目录的 `.env` **不作为**应用配置文件读取。进行最小化模型配置时，打开 **Settings → Models**，添加 LLM 配置（Base URL / API Key / 模型名称）并保存。仅当你计划使用知识库/RAG 功能时才需添加嵌入配置。

</details>

## 📖 探索 DeepTutor

v1.4.0-beta 重构将 DeepTutor 重组为 **五大核心界面** —— Chat、Co-Writer、Book、Knowledge、Space，以及贯穿其下的 **三层记忆（Memory）** 和暴露所有调节选项的统一 **设置（Settings）** 工作台。能力（Solve / Quiz / Research / Visualize）与工具（RAG, web, code, reason, brainstorm, paper search, `ask_user`, `web_fetch`, `write_note`, `list_notebook`, `github_query`）可在顶部自由组合。

### 💬 Chat —— 统一的智能工作区

<div align="center">
<img src="assets/figs/dt-chat.png" alt="Chat Workspace" width="800">
</div>

一个线程，五种模式，任意工具。能力选择器位于输入框中；同一会话、知识库、附件和引用会随你跨模式流转 —— 你可以从随意提问无缝切换至多智能体解题、测验或完整研究报告，而不会丢失上下文。

<details>
<summary><b>各模式功能与底层架构</b></summary>

| 模式 | 功能说明 | 底层架构 |
|:---|:---|:---|
| **Chat** | 灵活对话，支持任意工具；可从 RAG、网络搜索、代码执行、深度推理、头脑风暴、论文搜索、GeoGebra 分析中挑选。 | LlamaIndex 支持的 RAG + 工具注册表 |
| **Solve** | 多步计划 → 调查 → 求解 → 验证，附带精确来源引用。 | 智能体引擎 (`deep_solve`) |
| **Quiz** | 基于你的知识库自动生成并校验问题；为每个问题派生一个跟进聊天输入框。 | 智能体引擎 (`deep_question`) |
| **Research** | 将主题分解为子主题，并行调度 RAG / web / arXiv 智能体，产出带引用的报告并进行迭代追加式修订。 | 重构的 `pipeline.py`（体积缩小约 45%，保留引用与迭代报告） |
| **Visualize** | 生成 SVG 图表、Chart.js 图表、Mermaid 图、交互式 HTML 页面，**或** Manim 视频 / 分镜 —— 分析器会自动选择正确的 `render_type`。 | Visualize 流水线（已合并 Animator） |

</details>

重构随附的 **新增聊天工具**：`ask_user`（在轮次中间提出结构化澄清问题）、`web_fetch`（将特定 URL 拉取至上下文）、`write_note` / `list_notebook`（从聊天界面保存和列出笔记本记录）、以及 `github_query`（Issue/PR/仓库查询）。这些工具与工作流程 **解耦** —— 每种模式均可按轮次选择启用或禁用。

会话还会携带跨轮次的 **累积来源清单**，因此早期 RAG / web 命中产生的引用在后续对话中依然可复用。

### ✍️ Co-Writer —— 多文档 AI 创作空间

<div align="center">
<img src="assets/figs/dt-cowriter.png" alt="Co-Writer" width="800">
</div>

Co-Writer 是分屏 Markdown 工作台（左侧原始编辑器，右侧实时预览），适用于笔记、报告、教程和 AI 辅助草稿。每份文档拥有独立工作区，支持自动保存、Markdown 下载及一键 **Save to Notebook**。

选中任意文本并选择 **Rewrite**、**Expand** 或 **Shorten** —— 每项操作均作为可追踪的智能体编辑执行，可选择从知识库或网络获取依据。Co-Writer 渲染标准 Markdown / CommonMark / GFM（表格、代码、数学公式、流程图、时序图），支持 HTML 标签逃逸语法（`<sub>`, `<sup>`, `<abbr>`, `<mark>`），并附带专为 DeepTutor 产品文档和学习笔记设计的入门模板。

### 📖 Book Engine —— 交互式“活书”

<div align="center">
<img src="assets/figs/dt-book.png" alt="Book Engine" width="800">
</div>

给 DeepTutor 一个主题，指向你的知识库，它便会生成一本结构化、可交互的书籍 —— 不是静态导出物，而是你可以阅读、自测和上下文讨论的活文档。

幕后由多智能体流水线处理繁重工作：提出大纲、从 KB 检索相关来源、综合章节树、规划每页内容并编译每个区块。你始终掌握控制权 —— 审查提案、重新排序章节，并与任意页面对话。

书籍页面由 13 种区块类型组装而成 —— 文本、提示框、测验、闪卡、代码、插图、深度解析、动画、交互演示（现已包含 **GeoGebra 查看器**）、时间线、概念图、章节和用户笔记 —— 每种均渲染专属交互组件。书籍页面会针对源 KB 进行指纹标记；`deeptutor book health` 报告漂移情况，`deeptutor book refresh-fingerprints` 在源文件变更时清除过期页面。

### 📚 Knowledge Bases —— RAG 就绪型文档库

<div align="center">
<img src="assets/figs/dt-kb.png" alt="Knowledge Bases" width="800">
</div>

专为驱动 RAG 的文档集合打造的独立工作区。每个知识库包含四个标签页：

- **Files** —— 浏览上传的来源，内联预览 PDF，查看单文件大小/状态。
- **Add documents** —— 拖入 PDF、Office 文件（DOCX / XLSX / PPTX）、Markdown、纯文本及广泛的代码/数据文件类型。文档会自动路由至对应提取器。
- **Index versions** —— 每次（重新）索引均为可追踪版本。支持回滚至早期索引、比较嵌入模型或检查分块统计，且不丢失之前的构建结果。
- **Settings** —— 选择 KB 的嵌入提供商/模型、分块参数及重排序器。默认值继承自你的全局 LLM 和嵌入配置。

索引功能基于 **LlamaIndex** 端到端实现（v1.4 重构中合并了此前的双流水线），具备重试安全的重新索引、嵌入不匹配检测及损坏持久化向量的容错处理。

### 🌐 Space —— 你的个人学习图书馆

<div align="center">
<img src="assets/figs/dt-space.png" alt="Space" width="800">
</div>

Space 是主动界面的 **阅读/复习** 对应面。Chat / Co-Writer / Book 是你 *生产* 内容的地方，而 Space 是你所有产出物的存放处，支持搜索与回放。

- **Chat History** —— 跨所有模式的所有对话，支持标题重命名、删除和恢复；每个入口均支持删除单轮次记录。
- **Notebooks** —— 将 Chat、Research 和 Co-Writer 的输出保存至分类、颜色编码的笔记本中；每条记录均可链接回原始会话与界面。
- **Question Bank** —— 所有自动生成的测验问题，支持书签收藏并在聊天中使用 @提及以回顾过往表现。
- **Skills** —— 用户自定义的 `SKILL.md` 文件，定义教学人格（名称、描述、触发词、正文）。激活时，Skill 会注入聊天系统提示词 —— 将 DeepTutor 转变为苏格拉底式导师、研究助手或任何你设计的角色。

### 🧠 Memory —— 三层架构

<div align="center">
<img src="assets/figs/dt-memory.png" alt="Memory Workbench" width="800">
</div>

DeepTutor 的记忆现已升级为 **三层流水线**，并在 `/memory` 提供可检查的工作台。旧的 v1 `SUMMARY.md` / `PROFILE.md` 双文件模型已弃用；首次启动时所有数据将迁移至新布局。

<details>
<summary><b>L1 / L2 / L3 —— 角色与磁盘布局</b></summary>

| 层级 | 角色定位 | 存储位置 |
|:---|:---|:---|
| **L1 · 工作区镜像** (LIVE) | 每次交互的仅追加轨迹，按界面、按天记录。实际发生内容的无损记录。 | `trace/<surface>/<YYYY-MM-DD>.jsonl` |
| **L2 · 单界面摘要** (CURATED) | 由聚合器提取的界面专属事实。每条事实均附带指向 L1 轨迹的脚注引用。支持按文档的 **Update / Audit / Dedup** 运行。 | `L2/<surface>.md` |
| **L3 · 跨界面知识** (SYNTHESIS) | 跨界面综合：你的 `profile`、`recent` 时间线、知识 `scope` 及 `preferences`。附带条件限定，每条均受 L2 证据支撑。 | `L3/<recent\|profile\|scope\|preferences>.md` |

</details>

七种界面为流水线提供数据：**chat, notebook, quiz, kb, book, tutorbot, cowriter**。聚合器由 LLM 驱动并异步运行（`POST /memory/runs/start`）—— 你可从工作台触发它，观察 L1 → L2 → L3 的传播过程，并可手动编辑任意层级。

<div align="center">
<img src="assets/figs/dt-memgraph.png" alt="Memory Graph" width="800">
</div>

**记忆图（Memory Graph）**（`/memory/graph`）一次性渲染所有三层：L3 综合位于中心，L2 事实位于中环，L1 轨迹位于外环并按界面分组。悬停任意节点可查看内联预览；点击可锁定高亮并沿 L3 → L2 → L1 引用向内追溯，以便审计 *DeepTutor* “知道”你某些信息的原因。

### ⚙️ Settings —— 统一控制中心

<div align="center">
<img src="assets/figs/dt-settings.png" alt="Settings" width="800">
</div>

设置界面在 v1.4 中完成统一并按关注点拆分，采用草稿/**Apply** 模式，使更改具备原子性且可在保存前撤销：

- **Appearance** —— UI 语言与主题（Cream, Snow, Dark, Glass）。
- **Status** —— LLM、嵌入、搜索和存储后端的实时健康探针。
- **LLM**, **Embedding**, **Search** —— 提供商目录、基础 URL、API Key 及活跃模型选择。活跃模型从目录中选取，确保各界面保持同步。
- **Capabilities** —— Chat、Solve、Quiz、Research、Visualize 和 Co-Writer 的按能力可调参数（分块、LLM 预算、去重与引用策略、最大迭代次数）。由统一的 `emit_capability_result` 信封及共享 `UsageTracker` 支撑，提供按次调用成本展示。
- **Memory** —— 切换聚合器运行、配置频率与预算，并跳转至记忆工作台。
- **MCP servers** —— 注册外部 Model Context Protocol 服务器；其工具将与内置工具一同展示。
- **Tools** —— 检查每项内置工具、参数、状态（已启用/即将推出）及国际化文案。

“Tour”启动器会引导新用户浏览页面，且每项能力均附带标准 `capabilities/prompts/{en,zh}/<name>.yaml`，确保中英文状态下状态消息保持一致。

---

### 🦞 TutorBot —— 持久化、自主 AI 辅导机器人

<div align="center">
<img src="assets/figs/tutorbot-architecture.png" alt="TutorBot Architecture" width="800">
</div>

TutorBot 不是聊天机器人 —— 它是基于 [nanobot](https://github.com/HKUDS/nanobot) 构建的 **持久化、多实例智能体**。每个 TutorBot 运行独立的智能体循环，拥有独立的工作区、记忆和人格。创建一位苏格拉底式数学导师、耐心的写作教练或严谨的研究顾问 —— 全部同时运行，各自随你共同成长。

<div align="center">
<img src="assets/figs/dt-tutorbot.png" alt="TutorBot Agents" width="800">
</div>

- **Soul Templates** —— 通过可编辑的 Soul 文件定义辅导机器人的人格、语气与教学理念。可选择内置原型（苏格拉底式、鼓励型、严谨型）或自定义 —— Soul 将塑造每次回复。
- **Independent Workspace** —— 每个机器人拥有独立目录，包含独立的记忆、会话、Skills 和配置 —— 完全隔离但可访问 DeepTutor 的共享知识层。
- **Proactive Heartbeat** —— 机器人不仅响应，还会主动发起。内置的 Heartbeat 系统支持定期学习检查、复习提醒及计划任务。即使你不主动联系，导师也会准时出现。
- **Full Tool Access** —— 每个机器人均可调用 DeepTutor 完整工具库：RAG 检索、代码执行、网络搜索、学术论文搜索、深度推理和头脑风暴。
- **Skill Learning** —— 通过向工作区添加 Skill 文件教你的机器人新能力。随着你需求的变化，导师的能力也随之进化。
- **Multi-Channel Presence** —— 将机器人接入 Telegram, Discord, Slack, Feishu, WeChat Work, DingTalk, Matrix, QQ, WhatsApp, Email 等渠道。你的导师会在你需要时出现在任何地方。
- **Team & Sub-Agents** —— 在单个机器人内生成后台子智能体或编排多智能体团队，处理复杂、长周期任务。

```bash
deeptutor bot create math-tutor --persona "Socratic math teacher who uses probing questions"
deeptutor bot create writing-coach --persona "Patient, detail-oriented writing mentor"
deeptutor bot list                  # 查看所有活跃导师
```

---

### ⌨️ DeepTutor CLI —— 智能体原生接口

<div align="center">
<img src="assets/figs/cli-architecture.png" alt="DeepTutor CLI Architecture" width="800">
</div>

DeepTutor 完全支持 CLI 原生操作。每项能力、知识库、会话、记忆和 TutorBot 均可一键调用 —— 无需浏览器。CLI 同时服务于人类（丰富的终端渲染）与 AI 智能体（结构化 JSON 输出）。

将项目根目录的 [`SKILL.md`](SKILL.md) 交给任何具备工具调用能力的智能体（[nanobot](https://github.com/HKUDS/nanobot)，或任何带工具访问权限的 LLM），它即可自主配置并运行 DeepTutor。

<details>
<summary><b>示例命令</b> —— 单次执行、REPL、KB 生命周期、JSON 输出、会话恢复</summary>

**一次性执行** —— 直接在终端运行任意能力：

```bash
deeptutor run chat "Explain the Fourier transform" -t rag --kb textbook
deeptutor run deep_solve "Prove that √2 is irrational" -t reason
deeptutor run deep_question "Linear algebra" --config num_questions=5
deeptutor run deep_research "Attention mechanisms in transformers"
deeptutor run visualize "Draw the architecture of a transformer"
```

**交互式 REPL** —— 支持实时模式切换的持久化聊天会话：

```bash
deeptutor chat --capability deep_solve --kb my-kb
# 在 REPL 内使用 /cap, /tool, /kb, /history, /notebook, /config 动态切换
```

**知识库生命周期** —— 完全从终端构建、查询和管理 RAG 就绪型集合：

```bash
deeptutor kb create my-kb --doc textbook.pdf       # 从文档创建
deeptutor kb add my-kb --docs-dir ./papers/         # 添加论文文件夹
deeptutor kb search my-kb "gradient descent"        # 直接搜索
deeptutor kb set-default my-kb                      # 设为所有命令的默认 KB
```

**双输出模式** —— 人类使用丰富渲染，流水线使用结构化 JSON：

```bash
deeptutor run chat "Summarize chapter 3" -f rich    # 彩色格式化输出
deeptutor run chat "Summarize chapter 3" -f json    # 逐行 JSON 事件流
```

**会话连续性** —— 从断点处恢复任意对话：

```bash
deeptutor session list                              # 列出所有会话
deeptutor session open <id>                         # 在 REPL 中恢复
```

</details>

<details>
<summary><b>完整 CLI 命令参考</b></summary>

**顶层命令**

| 命令 | 描述 |
|:---|:---|
| `deeptutor run <capability> <message>` | 单次运行任意能力（`chat`, `deep_solve`, `deep_question`, `deep_research`, `math_animator`, `visualize`） |
| `deeptutor chat` | 交互式 REPL，支持可选的 `--capability`, `--tool`, `--kb`, `--language` |
| `deeptutor serve` | 启动 DeepTutor API 服务器 |

**`deeptutor bot`**

| 命令 | 描述 |
|:---|:---|
| `deeptutor bot list` | 列出所有 TutorBot 实例 |
| `deeptutor bot create <id>` | 创建并启动新机器人（支持 `--name`, `--persona`, `--model`） |
| `deeptutor bot start <id>` | 启动机器人 |
| `deeptutor bot stop <id>` | 停止机器人 |

**`deeptutor kb`**

| 命令 | 描述 |
|:---|:---|
| `deeptutor kb list` | 列出所有知识库 |
| `deeptutor kb info <name>` | 显示知识库详情 |
| `deeptutor kb create <name>` | 从文档创建（支持 `--doc`, `--docs-dir`） |
| `deeptutor kb add <name>` | 增量添加文档 |
| `deeptutor kb search <name> <query>` | 搜索知识库 |
| `deeptutor kb set-default <name>` | 设为默认 KB |
| `deeptutor kb delete <name>` | 删除知识库（支持 `--force`） |

**`deeptutor memory`**

| 命令 | 描述 |
|:---|:---|
| `deeptutor memory show [file]` | 查看记忆（`summary`, `profile` 或 `all`） |
| `deeptutor memory clear [file]` | 清空记忆（支持 `--force`） |

**`deeptutor session`**

| 命令 | 描述 |
|:---|:---|
| `deeptutor session list` | 列出会话（支持 `--limit`） |
| `deeptutor session show <id>` | 查看会话消息 |
| `deeptutor session open <id>` | 在 REPL 中恢复会话 |
| `deeptutor session rename <id>` | 重命名会话（支持 `--title`） |
| `deeptutor session delete <id>` | 删除会话 |

**`deeptutor notebook`**

| 命令 | 描述 |
|:---|:---|
| `deeptutor notebook list` | 列出笔记本 |
| `deeptutor notebook create <name>` | 创建笔记本（支持 `--description`） |
| `deeptutor notebook show <id>` | 查看笔记本记录 |
| `deeptutor notebook add-md <id> <path>` | 导入 Markdown 为记录 |
| `deeptutor notebook replace-md <id> <rec> <path>` | 替换 Markdown 记录 |
| `deeptutor notebook remove-record <id> <rec>` | 移除记录 |

**`deeptutor book`**

| 命令 | 描述 |
|:---|:---|
| `deeptutor book list` | 列出工作区中所有书籍 |
| `deeptutor book health <book_id>` | 检查 KB 漂移与书籍健康状态 |
| `deeptutor book refresh-fingerprints <book_id>` | 刷新 KB 指纹并清除过期页面 |

**`deeptutor config` / `plugin` / `provider`**

| 命令 | 描述 |
|:---|:---|
| `deeptutor config show` | 打印当前配置摘要 |
| `deeptutor plugin list` | 列出已注册的工具和能力 |
| `deeptutor plugin info <name>` | 显示工具或能力详情 |
| `deeptutor provider login <provider>` | 提供商认证（`openai-codex` OAuth 登录；`github-copilot` 验证现有 Copilot 会话） |

</details>

---

### 👥 Multi-User —— 共享部署与按用户隔离工作区

<div align="center">
<img src="assets/figs/dt-multi-user.png" alt="Multi-User" width="800">
</div>

开启认证后，DeepTutor 将转变为多租户部署，提供 **按用户隔离的工作区** 与 **管理员 curated 的资源**。首位注册用户将成为管理员，代表其他所有人配置模型、API Key 和知识库。后续账号由管理员创建（仅限邀请），每个账号拥有独立的作用域聊天历史/记忆/笔记本/知识库，且仅能看到管理员分配给他们的 LLM、KB 和 Skills。

**快速入门（5 步）：**

```bash
# 1. 在 data/user/settings/auth.json 中启用认证：
#    {"enabled": true, "token_expire_hours": 24, "cookie_secure": false}
#    若 Web 与 API 跨域部署，请使用 cookie_secure=true。

# 2. 重启 Web 服务栈。
deeptutor start

# 3. 打开 http://localhost:3782/register 创建首个账号。
#    首次注册是唯一公开的；该用户将成为管理员，随后 /register 端点将自动关闭。

# 4. 以管理员身份访问 /admin/users → "Add user" 配置团队成员。

# 5. 为每个用户点击滑块图标 → 分配 LLM 配置、知识库和 Skills。保存。
#    用户现在可登录并开始使用。
```

**管理员可见内容：**

- **完整 Settings 页面** (`/settings`) —— 管理 LLM / 嵌入 / 搜索提供商、API Key、模型目录及运行时“Apply”。
- **用户管理** (`/admin/users`) —— 创建、提升、降级和删除账号。首个管理员存在后，公共 `/register` 端点将自动关闭；后续账号通过 `POST /api/v1/auth/users`（仅限管理员）创建。
- **授权编辑器** —— 为每个非管理员用户选择可用的模型配置、知识库和 Skills。授权仅携带 **逻辑 ID**；API Key 绝不会跨越授权边界。
- **审计日志** —— 每次授权变更与分配资源访问记录均追加至 `multi-user/_system/audit/usage.jsonl`。

**普通用户获得：**

- **隔离工作区** (`multi-user/<uid>/`) —— 独立的聊天历史（`chat_history.db`）、记忆（`SUMMARY.md` / `PROFILE.md`）、笔记本和个人知识库。默认不共享任何内容。
- **只读访问** 管理员分配的知识库和 Skills，内联展示于自有资源旁并带有“Assigned by admin”标记。
- **精简 Settings 页面** —— 仅显示主题、语言及已授权模型摘要。API Key、基础 URL 和提供商端点绝不会在非管理员请求中返回。
- **作用域 LLM** —— 聊天轮次通过管理员分配的模型路由。若无分配 LLM，轮次将提前拒绝（不会静默回退至管理员的 Key）。

**工作区布局：**

```
multi-user/
├── _system/
│   ├── auth/users.json          # 哈希凭证、角色
│   ├── auth/auth_secret         # JWT 签名密钥（自动生成）
│   ├── grants/<uid>.json        # 按用户资源授权（管理员管理）
│   └── audit/usage.jsonl        # 审计日志
└── <uid>/
    ├── user/
    │   ├── chat_history.db
    │   ├── settings/interface.json
    │   └── workspace/{chat,co-writer,book,...}
    ├── memory/{SUMMARY.md,PROFILE.md}
    └── knowledge_bases/...
```

**配置参考：**

| 设置项 | 是否必需 | 描述 |
|:---|:---|:---|
| `data/user/settings/auth.json: enabled` | 是 | 设为 `true` 启用多用户认证。默认 `false`（单用户模式 —— 所有路径均为管理员）。 |
| `multi-user/_system/auth/auth_secret` | 推荐 | JWT 签名密钥。缺失时首次认证启动自动生成。 |
| `data/user/settings/auth.json: token_expire_hours` | 否 | JWT 有效期；默认 `24`。 |
| `data/user/settings/auth.json: cookie_secure` | HTTPS / 跨域认证 | 需要 `SameSite=None` Cookie 的 HTTPS 部署请设为 `true`。本地 HTTP 保持 `false`。 |
| `data/user/settings/auth.json: username/password_hash` | 否 | 可选的无头单用户引导凭证。使用浏览器注册时留空即可。 |
| `data/user/settings/system.json` | 否 | `deeptutor start` 会从运行时设置推导前端认证标志、公共 API base 和 CORS origins。 |

> ⚠️ **PocketBase 模式（设置了 `integrations.pocketbase_url`）仅限单用户。** 默认 PocketBase schema 在 `users` 上无 `role` 字段（所有登录均解析为 `role=user`，无法创建管理员），且 `sessions` / `messages` / `turns` 查询未按 `user_id` 过滤。多用户部署必须保持 `integrations.pocketbase_url` 为空并使用默认 JSON/SQLite 后端。

> ⚠️ **单进程推荐。** “首用户即管理员”的晋升受进程内 `threading.Lock` 保护。多 Worker 部署应离线配置首个管理员（先启动 `auth.json.enabled=false`，通过引导流程注册管理员，再设 `auth.json.enabled=true`）或将用户存储 backed 由外部系统承担。

## 🌐 社区与生态

DeepTutor 站在优秀开源项目的肩膀上：

| 项目 | 在 DeepTutor 中的角色 |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | 驱动 TutorBot 的超轻量级智能体引擎 |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | RAG 流水线与文档索引骨干 |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | AI 驱动的数学动画生成（用于 Math Animator） |

**来自 HKUDS 生态：**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| 简单快速 RAG | 零代码智能体框架 | 自动化研究 | 超轻量 AI 智能体 |


## 🤝 贡献指南

<div align="center">

我们希望 DeepTutor 能成为献给社区的礼物。🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contributors" />
</a>

</div>

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 了解开发环境搭建、代码规范及 Pull Request 工作流的指南。

## ⭐ Star History

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Star History Rank" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ Star us](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 Report a bug](https://github.com/HKUDS/DeepTutor/issues) · [💬 Discussions](https://github.com/HKUDS/DeepTutor/discussions)

---

Licensed under the [Apache License 2.0](LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Views">
</p>

</div>