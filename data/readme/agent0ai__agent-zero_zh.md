<div align="center">

<img src="docs/res/a0-vector-graphics/horizontal_banner.svg" alt="Agent Zero Banner" width="100%"/>

# Agent Zero
### 为你的 AI 智能体打造的完整 Linux 系统。

Agent Zero 是一个开源、动态且有机生长的智能体框架。一个 Docker 容器即可交付完整的 Linux 系统，内置桌面环境与插件中心，智能体可通过技能（Skills）进行扩展。

[![Website](https://img.shields.io/badge/Website-agent--zero.ai-0A192F?style=for-the-badge&logo=vercel&logoColor=white)](https://agent-zero.ai)
[![Docs](https://img.shields.io/badge/Docs-Read%20the%20guides-1F6FEB?style=for-the-badge&logo=readthedocs&logoColor=white)](./docs/)
[![Discord](https://img.shields.io/badge/Discord-Join%20us-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsors-Thank%20you-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/agent0ai)

[Install](#how-to-install) |
[What's Different](#what-makes-agent-zero-different) |
[A0 CLI](#a0-cli-connector-extend-onto-your-host-machine) |
[Docs](#documentation)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/agent0ai/agent-zero)
[Ask ChatGPT](https://chatgpt.com/?q=Analyze%20this%3A%20https%3A%2F%2Fgithub.com%2Fagent0ai%2Fagent-zero) |
[Ask Claude](https://claude.ai/new?q=Analyze%20this%3A%20https%3A%2F%2Fgithub.com%2Fagent0ai%2Fagent-zero)


</div>

<div align="center">
<a href="https://www.youtube.com/watch?v=k78HX_RA9Q0&t=19s">
<img src="docs/res/thumbnail-install.webp" alt="Agent Zero Installation Guide" width="100%"/>
</a>
</div>

# 是什么让 Agent Zero 与众不同

## 如何安装

### macOS / Linux

```bash
curl -fsSL https://bash.agent-zero.ai | bash
```

### Windows PowerShell

```powershell
irm https://ps.agent-zero.ai | iex
```

### 已安装 Docker？直接运行以下命令

```bash
docker run -p 80:80 -v a0_usr:/a0/usr agent0ai/agent-zero
```

打开 Web UI，配置你的大语言模型（LLM）提供商，然后开始处理具体任务。完整安装与引导流程请参阅[安装指南](./docs/setup/installation.md)。

## Canvas 中的真实 Linux 桌面

<img alt="Agent Zero driving Blender in its built-in XFCE desktop" src="docs/res/usage/webui/agentzero-xfce-computer.gif" />
<br>

Agent Zero 在右侧的 Canvas（画布）中打开它自己的 Linux 桌面。这不是远程虚拟机，也不是共享剪贴板，而是在容器中运行的真实 XFCE 桌面会话。

这意味着智能体可以驱动*真实的桌面软件*：打开 Blender 建模、进入终端窗口、可视化文件管理，或运行没有 API 的图形界面工具。

你可以实时查看每一个操作，并且随时可以介入，因为你的鼠标和键盘与智能体共享同一个桌面。

完整步骤、提示词示例以及桌面模式与浏览器模式的差异说明，请参阅[桌面指南](./docs/guides/desktop.md)。

## 原生浏览器与 DOM 标注功能

<img alt="Annotating a webpage element in the Agent Zero browser" src="docs/res/usage/browser/annotation.gif" />
<br>

Agent Zero 内置了浏览器，并可在 Canvas 中提供可选的实时视图。智能体可以打开网页、阅读内容、点击、输入、上传文件和截图——这些是常规操作。不寻常的是它的**标注模式（Annotate mode）**。

标注模式可将任意网页转化为交互式指令界面。点击元素即可：

- **修改它** - “将此按钮改为蓝色并圆角”将作为 JS 指令由智能体执行并验证。
- **检查它** - 提取 DOM、样式、父级链和框架提示到对话中。
- **提取/复用它** - 看到别人网站上的卡片、首屏或组件很喜欢？直接捕获它，让智能体在你的项目技术栈中重新实现。
- **评论它** - 在 UI 审查期间留下可操作的注释并固定在元素上；智能体会读取这些注释并完成修复。

Docker 浏览器是默认的实时视图。浏览器历史记录会保存关键步骤的截图，因此旧对话仍能展示智能体当时的所见内容。该浏览器还支持在 Docker 内部安装 Chrome 扩展，并且通过 A0 CLI Connector（连接器）的**自带浏览器（Bring Your Own Browser）**功能，可以让智能体直接驱动你本机上的 Chrome/Edge/Chromium。

截图、设置、主机浏览器配置及故障排除请参阅[浏览器指南](./docs/guides/browser.md)。

## 文档协同编辑

### 支持实时协同的 Markdown 编辑器

<img alt="Agent Zero writing a TODO plan in the Canvas markdown editor" src="docs/res/usage/webui/markdown-editor.gif" />
<br>

Canvas 内置了功能丰富的 Markdown 编辑器，专为真正的协同工作设计。让智能体“在已打开的文档中，于 `TODO.md` 编写执行 X 的计划”，你会看到文件逐个字符地出现在编辑器中，而你可以同时在另一处继续输入。

这不是预览面板。它是一个真正的编辑器，包含工具栏、格式化按钮、表格和可编辑的源码视图——旨在让智能体的修改与你的输入成为同一文档中同等优先级的操作。

适用于计划、待办事项、会议纪要、RFC 文档、项目交接，或任何希望交付物以*纯文本形式存在*而非被困在聊天滚动记录中的场景。

### LibreOffice 集成

已接入 LibreOffice Writer、Calc 和 Impress，你可以手动输入，同时让 Agent Zero 实时创建、更新、保存并验证相同的文件。

为符合开放文档格式（Open Document Format, ODF）标准，Agent Zero 桌面环境将 ODT、ODS 和 ODP 二进制格式视为一等公民。

使用桌面工具栏即可创建和编辑 Writer 文档、电子表格及演示文稿。

## 插件中心 - 100+ 社区插件

<img alt="Agent Zero Plugin Hub showing community plugins" src="docs/res/usage/plugins/plugin-hub-browse.png" />
<br>

Agent Zero 专为扩展而设计，而非仅仅用于配置。内置的**插件中心（Plugin Hub）**提供不断增长的社区插件目录——目前已超过 100 个，涵盖：

- **开发框架**：如 [BMAD Method](https://github.com/bmad-code-org/bmad-method)（包含 20 个专业智能体的完整软件开发生命周期）和 [Agent Skills](https://github.com/addyosmani/agent-skills)。
- **记忆系统** - 替代型记忆后端、智能整合策略、向量检索插件等。
- **工具与集成**：嵌入式终端、自定义浏览器、部署辅助工具、API 客户端等。
- **界面扩展**：聊天重命名控件、侧边栏调整、主题包、自定义 Canvas 面板等。
- **工作流插件**：调度器、多智能体编排、项目自动化等。

在 Web UI 中一键安装，或发布你自己的插件到索引仓库。结合 `prompts/` 中的自定义提示词、`tools/` 中的自定义工具、MCP 服务器、A2A 连接器以及项目级配置，Agent Zero 为你提供了广阔的扩展空间，可按需塑造智能体。

请参阅[技能指南](./docs/guides/skills.md)、[创建小型插件](./docs/guides/create-plugin.md)教程以及[MCP 配置](./docs/guides/mcp-setup.md)指南。

## 使用你的 OpenAI Codex 计划

<img alt="OAuth LLM plans in Agent Zero" src="docs/res/codex-screenshot.png" />
<br>

Agent Zero 通过全新的 OAuth 流程连接至你的 OpenAI Codex 计划。使用账号登录，选择支持 Codex 的提供商，让 Agent Zero 直接使用你已有的计划。点击“连接”，在 OpenAI 页面输入设备代码，选择模型即可配置完成。

这是 Agent Zero 迈向账号绑定大语言模型（LLM）计划的第一步。更多集成即将推出，包括通过额外用量（Extra Usage）接入的 Gemini CLI 和 Claude Code。

## A0 CLI 连接器：扩展至宿主机

<img alt="A0 CLI driving the host browser through a Google Cloud VM creation flow" src="docs/res/usage/a0-cli/host-browser.gif" />
<br>

**A0 CLI 连接器（A0 CLI Connector）**并非独立的 CLI 智能体。它连接到正在运行的 Agent Zero 实例，并为该实例提供与宿主机终端原生的桥接——这样同一个智能体（携带所有记忆、项目和技能）也能在 Docker 容器外的真实文件上工作。

请在希望 Agent Zero 工作的机器上安装连接器，**不要**安装在 Agent Zero 容器内部。

### macOS / Linux

```bash
curl -LsSf https://cli.agent-zero.ai/install.sh | sh
```

### Windows PowerShell

```powershell
irm https://cli.agent-zero.ai/install.ps1 | iex
```

然后运行 `a0`，将你的终端连接到现有的 Agent Zero 实例。它通常会自动发现本地实例，或者你可以将其指向托管在其他位置（如 VPS 或隧道）的远程 URL。

如果你符合以下情况，此功能尤其有用：

- 偏好命令行工作流；
- 希望 Agent Zero 在现有的本地代码库中工作；
- 在远程服务器上运行 Agent Zero；
- 既需要 Docker 隔离环境，又希望显式、受控地访问宿主机端的工作。

完整配置请参阅[A0 CLI 连接器指南](https://www.agent-zero.ai/p/docs/a0-cli-connector/)（或[仓库内指南](./docs/guides/a0-cli-connector.md)）。

## 项目、技能、智能体配置文件与模型预设

**项目（Projects）**：隔离工作区、指令、记忆、密钥、知识库、代码库和模型预设。将公开或私有 Git 仓库克隆至项目中，即可为智能体提供专属该项目的上下文。

**技能（Skills）**：可由 Agent Zero 按需加载，或在聊天输入框中固定，以便特定流程保持激活状态。

**智能体配置文件（Agent Profiles）**：改变当前对话的整体工作风格。

**模型预设（Model Presets）**：为模型配置命名的快捷方式，便于快速切换轻量、均衡、低成本、本地或高性能的模型选项。

## 多智能体协作

每个智能体均可创建从属智能体以分解任务。上级智能体分配任务并接收报告；子智能体保持自身上下文专注，完成后返回结果。

这使得 Agent Zero 在研究、软件工程、数据分析、插件开发等领域非常有用，尤其适用于需要多个专业视角而非单一臃肿上下文的任务。

## 设计透明且易于扩展

几乎没有任何隐藏内容。提示词存放在 `prompts/`，工具位于 `tools/` 或插件中，内置行为均可查看、修改、替换或扩展。

Agent Zero 支持插件、MCP、A2A、自定义工具与提示词、项目级配置、基于环境的部署设置，以及专为实时保持智能体工作可读性而设计的 Web UI。

## 快速上手尝试

- **标注你喜欢的界面**：“在浏览器中打开这个模板网站。我要标注首屏区域——用我的项目技术栈（React + Tailwind）重新实现它。”
- **协同编辑表格**：“创建一个可编辑的 ODS 预算模型，包含假设条件和月度预测。”
- **驱动桌面应用**：“使用 Linux 桌面打开 Blender，为我创建一个简单的 3D Logo。”
- **审查 Web 界面**：“在浏览器中打开我的本地应用。我会用注释标注页面；然后实现请求的 UI 修复。”
- **创建专家智能体**：“为财务分析创建一个智能体配置文件，要求推理谨慎、假设清晰，并以表格优先交付成果。”
- **恢复工作区**：“显示最近的时光机快照，并解释在回滚之前发生了什么变更。”

## Agent Zero 与 Space Agent

Agent Zero 是开源框架及基于 Linux 的智能体工作台。

[Space Agent](https://github.com/agent0ai/space-agent) 是我们面向“智能体形态工作区”的最新产品方向：一个智能体可在浏览器内重塑的 Space，提供实时演示、桌面应用，以及为你或团队运行真实服务器的路径。

<p align="left">
  <a href="https://www.youtube.com/watch?v=CNRHxEZ8yqs"><img src="https://github.com/agent0ai/space-agent/raw/main/.github/thumbnail.webp" alt="Watch Space Agent on YouTube" width="560" /></a>
</p>

如果你需要搭配完整 Linux 系统的智能体的强大能力与深度自定义功能，请从这里开始使用 Agent Zero。如果你追求更易于个人、团队、桌面或自托管使用的精致 Space 体验，可探索 [Space Agent](https://github.com/agent0ai/space-agent)。


## 时光机（由 Space Agent 驱动）

“时光机”功能为 Agent Zero 管理的 `/a0/usr` 工作区提供快照历史、差异检查、时间旅行与回滚。它专为可恢复的智能体工作设计：查看变更内容、对比文件、检查历史状态，并在需要时回滚。你也可以在 Space Agent 中体验此功能（见上方链接）。

<img alt="Time Travel" src="docs/res/time-travel.png" />

它并非 Git 或备份的替代品。它是为智能体活跃创建和编辑文件的工作区提供的一项实用安全层。

## 实际应用场景

- **软件工程**：检查代码库、进行范围限定修改、运行测试、解释权衡取舍，并保留可恢复的文件变更历史。
- **宿主机开发**：通过 `a0` 连接，让 Agent Zero 在真实的本地代码库中工作，或通过 Web UI 的 Git 项目功能克隆它们。
- **设计灵感与界面迭代**：浏览网页、标注你喜欢的元素，并将组件提取到你的技术栈中。
- **财务分析与图表制作**：收集数据、关联事件、创建电子表格并生成可编辑的图表。
- **办公交付物**：在文档、表格和演示文稿中进行协同，而非将结果困于聊天文本中。
- **网页与移动端测试（QA）**：浏览应用、标注界面问题、安装浏览器扩展，并将视觉注释转化为可执行的修复方案。
- **API 集成**：粘贴 API 代码片段，让智能体构建可用示例，并保存该模式供未来复用。
- **客户端/项目隔离**：按项目分离记忆、密钥、指令、文件和模型选择。
- **定时任务操作**：使用项目级上下文和凭据运行定期检查和监控任务。

## 安全规范

Agent Zero 的强大之处在于它能够调用真实环境。

- 始终在 Docker 或其他隔离环境中运行。
- 除非你清楚相关风险，否则不要挂载整个主目录（home directory）。
- 仅对受信任的机器和工作区授予 A0 CLI 读写权限及远程代码执行权限。
- 将凭据存储在项目密钥或设置中，切勿放在提示词或公开文件里。
- 审查涉及账户、资金、生产系统或个人数据的操作。
- 为重要工作区保留备份。

## 文档索引

| 我想了解... | 从这里开始 |
| --- | --- |
| 安装或更新 Agent Zero | [安装指南](./docs/setup/installation.md) |
| 熟悉界面与基础工作流 | [快速入门](./docs/quickstart.md) |
| 浏览、标注及使用浏览器截图 | [浏览器指南](./docs/guides/browser.md) |
| 使用 Linux 桌面与 LibreOffice | [桌面指南](./docs/guides/desktop.md) |
| 将 Agent Zero 连接至宿主机文件与终端 | [A0 CLI 连接器](https://www.agent-zero.ai/p/docs/a0-cli-connector/) |
| 使用项目与 Git 工作区 | [项目指南](./docs/guides/projects.md) |
| 创建小型插件 | [创建小型插件](./docs/guides/create-plugin.md) |
| 添加或移除活跃技能 | [技能指南](./docs/guides/skills.md) |
| 创建或切换智能体配置文件 | [智能体配置文件](./docs/guides/agent-profiles.md) |
| 创建或切换模型预设 | [模型预设](./docs/guides/model-presets.md) |
| 管理与筛选记忆 | [记忆指南](./docs/guides/memory.md) |
| 掌握日常聊天控件 | [使用指南](./docs/guides/usage.md) |
| 配置 MCP 或外部工具 | [MCP 配置](./docs/guides/mcp-setup.md) |
| 理解架构与底层原理 | [Agent Zero DeepWiki](https://deepwiki.com/agent0ai/agent-zero) |
| 构建高级扩展功能 | [扩展开发](./docs/developer/extensions.md) |
| 参与项目贡献 | [贡献指南](./docs/guides/contribution.md) |
| 排查常见问题 | [故障排除](./docs/guides/troubleshooting.md) |

## 与我们共建

Agent Zero 专为希望理解并塑造自身工具的人打造。

你可以通过完善文档、创建技能、发布插件、测试模型/提供商配置、报告漏洞、分享工作流或贡献核心改进来提供帮助。从[贡献指南](./docs/guides/contribution.md)开始，浏览[插件中心](https://www.agent-zero.ai/p/docs/plugins/#plugin-hub)，或在 Discord 提出你的想法。

## 社区与支持

- [Discord](https://discord.gg/B8KZKNsPpj) 用于实时讨论与求助。
- [Skool Community](https://www.skool.com/agent-zero) 用于社区学习。
- [YouTube](https://www.youtube.com/@AgentZeroFW) 观看演示与教程。
- [X](https://x.com/Agent0ai)、[LinkedIn](https://www.linkedin.com/company/109758317) 和 [Warpcast](https://warpcast.com/agent-zero) 获取最新动态。
- [GitHub Issues](https://github.com/agent0ai/agent-zero/issues) 提交漏洞报告与功能建议。