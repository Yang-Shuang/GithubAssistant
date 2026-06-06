<p align="center">
  <img src="./resources/aionui-banner-1.png" alt="AionUi - Cowork with AI Agents" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/iOfficeAI/AionUi?style=flat-square&color=32CD32" alt="Version">
  &nbsp;
  <img src="https://img.shields.io/badge/license-Apache--2.0-32CD32?style=flat-square&logo=apache&logoColor=white" alt="License">
  &nbsp;
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-6C757D?style=flat-square&logo=linux&logoColor=white" alt="Platform">
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/15423" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15423" alt="GitHub Trending" height="80">
  </a>
</p>

---

<p align="center">
  <strong>A free, open-source, Cowork app with AI Agents</strong><br>
  <em>Built-in Agent | Zero Setup | Any API Key | Multi-Agents | Remote Access | Cross-Platform | 24/7 Automation</em>
</p>

<p align="center">
  <a href="https://github.com/iOfficeAI/AionUi/releases">
    <img src="https://img.shields.io/badge/⬇️%20Download%20Now-Latest%20Release-32CD32?style=for-the-badge&logo=github&logoColor=white" alt="Download Latest Release" height="50">
  </a>
</p>

<p align="center">
  <strong>English</strong> | <a href="./docs/readme/readme_ch.md">简体中文</a> | <a href="./docs/readme/readme_tw.md">繁體中文</a> | <a href="./docs/readme/readme_jp.md">日本語</a> | <a href="./docs/readme/readme_ko.md">한국어</a> | <a href="./docs/readme/readme_es.md">Español</a> | <a href="./docs/readme/readme_pt.md">Português</a> | <a href="./docs/readme/readme_tr.md">Türkçe</a> | <a href="./docs/readme/readme_ru.md">Русский</a> | <a href="./docs/readme/readme_uk.md">Українська</a> | <a href="https://www.aionui.com" target="_blank">Official Website</a>
</p>

<p align="center">
  <strong>💬 Community:</strong> <a href="https://discord.gg/2QAwJn7Egx" target="_blank">Discord (English)</a> | <a href="./resources/wx-9.png" target="_blank">微信 (中文群)</a> | <a href="https://twitter.com/AionUI" target="_blank">Twitter</a>
</p>

---

## 📋 快速导航

<p align="center">

[实战体验](#-cowork-in-action) ·
[为何选择 AionUi？](#-why-choose-aionui-over-claude-cowork) ·
[快速开始](#-quick-start) ·
[社区支持](#-community--support)

</p>

---

## 协作（Cowork）—— AI Agent 与你并肩工作

**AionUi 不仅仅是一个聊天客户端。** 它是一个协作平台，让 AI Agent 在您的电脑上与您并肩工作——读取文件、编写代码、浏览网页并自动化任务。您可以看到 Agent 所做的每一步操作，并且始终掌控全局。

|                                 | 传统 AI 聊天客户端          | **AionUi (Cowork)**                                                                                                           |
| :------------------------------ | :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| AI 能否操作你的文件             | 有限或无                    | **是 —— 内置 Agent，拥有完整文件访问权限**                                                                                    |
| AI 能否执行多步任务             | 有限                        | **是 —— 在你批准下自主运行**                                                                                                  |
| 手机远程访问                    | 罕见                        | **WebUI + Telegram / Lark / DingTalk / WeChat / WeCom**                                                                       |
| 定时自动化                      | 无                          | **Cron —— 24/7 无人值守**                                                                                                    |
| 同时使用多个 AI Agent           | 无                          | **Claude Code, Codex, Qwen Code, Kiro, Hermes Agent, Snow CLI, Cursor Agent 及 16+ 更多 —— 自动检测，统一界面** |
| 价格                            | 免费 / 付费                 | **免费且开源**                                                                                                                |

<p align="center">
  <img src="./resources/offica-ai BANNER-function.png" alt="AionUi Cowork Platform" width="800">
</p>

---

## 内置 Agent —— 安装即用，零配置

AionUi 自带完整的 AI Agent 引擎。与那些需要你单独安装 CLI Agent 的工具不同，**AionUi 在安装后即可立即使用**。

- **无需安装 CLI 工具** —— Agent 引擎已内置
- **无需复杂设置** —— 用 Google 账号登录或粘贴任意 API Key 即可
- **完整的 Agent 能力** —— 文件读写、网页搜索、图像生成、MCP（Model Context Protocol）工具调用
- **开箱即用的助手** —— 20 款内置专业助手（协作、PPT 创作、Word 创作、Excel 创作、Morph PPT 3D、Pitch Deck 制作、仪表盘制作、学术论文写作、财务模型构建等），随时可用

<p align="center">
  <img src="./resources/homepage.png" alt="Built-in Agents" width="800">
</p>

### **办公助手 —— PPT、Word & Excel**

这些功能与 App 实际交付的内容一致：**Morph PPT** 预设以及 **`pptx` / `docx` / `xlsx` 技能**（详见仓库中的 `assistant/` 预设和 `skills/`）。需要文档/表格输出？AionUi 内置的 **[OfficeCLI](https://github.com/iOfficeAI/OfficeCli)** 可帮助 PPT (Morph)、Word (`.docx`) 和 Excel (`.xlsx/.xlsm/.csv`) 更快、更可靠地从请求转化为成品。
这三种助手类型对应文件工作流，最终输出结果可直接编辑并复用。

#### **PPT 助手**

> **输出：** 可编辑的 Morph PPT (`.pptx`)
> 支持连贯故事节奏的幻灯片间 Morph 动画过渡；由 [OfficeCLI](https://github.com/iOfficeAI/OfficeCli) 驱动。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="./resources/morph-ppt-balanced.gif" alt="Morph PPT — slide-to-slide transitions (OfficeCLI)" width="390">
    </td>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-assistant-ppt.gif" alt="PPT assistant — screen recording" width="390">
    </td>
  </tr>
</table>

#### **Word 助手**

> **输出：** 可编辑的 Word (`.docx`)
> 通过 `docx` 技能实现论文/学术写作及生产级文档编辑；由 [OfficeCLI](https://github.com/iOfficeAI/OfficeCli) 驱动。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-generate-academic-paper.gif" alt="Generate academic paper demo" width="390">
    </td>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-assistant-write-paper.gif" alt="Paper writing assistant demo" width="390">
    </td>
  </tr>
</table>

#### **Excel 助手**

> **输出：** 可用的 Excel (`.xlsx/.xlsm/.csv`)
> 通过 `xlsx` 生成/刷新电子表格，支持数据分析、自动排版和图表制作；由 [OfficeCLI](https://github.com/iOfficeAI/OfficeCli) 驱动。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-generate-excel.gif" alt="Excel generation demo" width="390">
    </td>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-assistant-excel.gif" alt="Excel assistant demo" width="390">
    </td>
  </tr>
</table>

---

## 多 Agent 模式 —— 已有 CLI Agent？直接接入

如果你已经在使用 Claude Code、Codex、Hermes Agent 或 OpenClaw，AionUi 会自动检测它们，并让你与所有这些 Agent（包括内置 Agent）一起协作。

**支持的 Agent：** 内置 Agent (零配置) • Claude Code • Codex • Qwen Code • Goose AI • OpenClaw • Augment Code • CodeBuddy • Kimi CLI • OpenCode • Factory Droid • GitHub Copilot • Qoder CLI • Mistral Vibe • Nanobot • Aion CLI (aionrs，AionUi 捆绑的基于 Rust 的后端服务) • Snow CLI • Kiro • Hermes Agent • Cursor Agent 等

<p align="center">
  <img src="./resources/multi-agent支持openclaw.gif" alt="Multi-Agent Cowork" width="800">
</p>

- **自动检测** —— 自动识别已安装的 CLI 工具
- **统一界面** —— 一个协作平台管理所有 AI Agent
- **并行会话** —— 同时运行多个 Agent，各自拥有独立的上下文
- **MCP 统一管理** —— 一次性配置 MCP（Model Context Protocol）工具，自动同步至所有 Agent —— 无需逐个配置
- **YOLO 模式** (自动批准所有 Agent 操作) / **全自动模式** —— 一键绕过权限提示；所有 Agent 均支持全自动模式以实现无人值守执行

### 团队模式（Team Mode）—— 协同多 Agent 协作

将多个 AI Agent 作为有组织的团队运行：**Leader** Agent 接收你的指令，将其拆分为子任务，并通过内置的 Team MCP Server 委派给 **Teammate** Agent。队友并行执行任务，通过异步邮箱共享结果，并写入共享的任务看板。

<p align="center">
  <img src="./resources/AionUi_team.gif" alt="Team Mode overview" width="800">
</p>

- **并行多 Agent 执行** —— Leader 将任务拆分为子任务并委派给并行运行的 Teammate Agent；每个 Teammate 通过 ACP（Agent Communication Protocol，AionUi 的多 Agent 协调层）、Gemini 或 Aionrs 使用各自的模型
- **Leader 编排** —— Leader 分配、跟踪并汇总结果；支持的后端包括 Claude Code、Codex、Hermes Agent、Gemini、Snow CLI 和 Aion CLI
- **团队隔离工作区** —— 所有 Agent 共享同一文件夹；每个 Agent 拥有独立的权限对话框，侧边栏徽标显示待审批项

<details>
<summary><strong>🔍 查看团队模式详情 ▶️</strong></summary>

<br>

- **共享工作区** —— 所有 Agent 读写同一个文件夹；文件面板在整个过程中保持可见
- **支持的后端** —— Claude Code、Codex、Gemini、Snow CLI、Aion CLI (aionrs)；其他带有 `mcpCapabilities.stdio` 的 ACP 后端自动支持
- **动态扩缩容** —— 团队运行期间可随时添加或移除 Teammate；静默 Agent 会自动标记为失败，并支持一键移除
- **细粒度权限** —— 每个 Agent 拥有独立的权限确认对话框；侧边栏徽标显示待审批项
- **文件共享** —— Leader 可将文件附件传递给 Teammate

</details>

---

## 任意 API Key，完整协作能力

其他 AI App 只给你一个带 API Key 的聊天框。**AionUi 给你的是一个完整的协作 Agent。**

| 你的 API Key                            | 你将获得的功能                                |
| :-------------------------------------- | :------------------------------------------ |
| Gemini API Key (或 Google 登录 —— 免费) | 由 Gemini 驱动的协作 Agent                  |
| OpenAI API Key                          | 由 GPT 驱动的协作 Agent                     |
| Anthropic API Key                       | 由 Claude 驱动的协作 Agent                  |
| AWS Bedrock 凭证                        | 通过 Aion CLI (aionrs) 调用的 Bedrock Agent   |
| Ollama / LM Studio (本地)               | 本地模型协作 Agent                          |
| NewAPI Gateway                          | 统一接入 20+ 个模型                         |

无论底层由哪个模型驱动，你都拥有相同的能力 —— 文件读写、网页搜索、图像生成、工具调用。AionUi 支持 **20+ AI 平台**，涵盖云服务和本地部署。

<p align="center">
  <img src="./resources/llm_newapi.png" alt="Multi-Model Support" width="800">
</p>

<details>
<summary><strong>🔍 查看所有 20+ 支持平台 ▶️</strong></summary>

<br>

**全面的平台支持：**

- **官方平台** —— Gemini, Gemini (Vertex AI), Anthropic (Claude), OpenAI
- **云服务商** —— AWS Bedrock, New API (统一 AI 模型网关)
- **国内平台** —— Dashscope (通义千问), Zhipu (智谱), Moonshot (Kimi), Qianfan (百度), Hunyuan (腾讯), Lingyi (零一万物), ModelScope, InfiniAI, Ctyun, StepFun
- **国际平台** —— DeepSeek, MiniMax, OpenRouter, SiliconFlow, xAI, Ark (火山引擎), Poe
- **本地模型** —— Ollama, LM Studio（通过自定义平台配置本地 API 端点）

AionUi 还支持 [NewAPI](https://github.com/QuantumNous/new-api) 网关服务 —— 一个聚合和分发各类 LLM 的统一 AI 模型中心。在同一界面中灵活切换不同模型，满足各种任务需求。

</details>

---

## 可扩展的助手与技能

_具备 20 款内置专业助手的可扩展系统，采用三层技能架构。创建并管理你自己的助手和技能。_

- **创建自定义助手** —— 定义带有自定义规则和能力的专属助手
- **三层技能体系** —— Builtin 技能（随 AionUi 自带）、Custom 技能（你自己创建的）和 Extension 技能（由第三方扩展贡献）；通过聊天头部的技能指示器按会话启用/禁用
- **逐会话控制** —— 聊天头部显示当前会话的活跃技能；可按需搜索或排除特定技能

<p align="center">
  <img src="./resources/assitants.png" alt="AI Assistants & Skills Ecosystem" width="800">
</p>

AionUi 支持三种技能层级：**内置** 技能（随应用自带）、**自定义** 技能（用户定义）和 **扩展** 技能（从 Extension SDK 加载）。

<details>
<summary><strong>🔍 查看助手详情与自定义技能 ▶️</strong></summary>

<br>

AionUi 内置了 **20 款专业助手**，具备预定义能力，可通过自定义技能进行扩展：

- **🤝 Cowork** —— 自主任务执行（文件操作、文档处理、工作流规划）
- **📊 PPT Creator / Morph PPT / Morph PPT 3D** —— 生成并制作带 Morph 过渡的动画 PPTX 演示文稿
- **📐 Pitch Deck Creator** —— 面向投资人的商业计划页生成
- **📊 Dashboard Creator** —— 数据仪表盘生成
- **📝 Word Creator** —— 生产级 Word (`.docx`) 文档生成
- **📗 Excel Creator** —— 带数据分析、图表和自动排版的电子表格生成
- **🎓 Academic Paper Writer** —— 结构化学术论文写作
- **💰 Financial Model Creator** —— 财务模型与预测
- **⭐ Star Office Helper** —— 办公效率助手
- **📄 PDF to PPT** —— PDF 转 PPT
- **🎮 3D Game** —— 单文件 3D 游戏生成
- **🎨 UI/UX Pro Max** —— 专业 UI/UX 设计（57 种风格，95 套配色）
- **📋 Planning with Files** —— 基于文件的复杂任务规划（类 Manus 持久化 Markdown 规划）
- **🧭 HUMAN 3.0 Coach** —— 个人成长教练
- **📣 Social Job Publisher** —— 招聘发布与分发
- **🦞 moltbook** —— 零部署 AI Agent 社交网络
- **📈 Beautiful Mermaid** —— 流程图、时序图等
- **🔧 OpenClaw Setup** —— OpenClaw 集成设置向导
- **📖 Story Roleplay** —— 沉浸式故事角色扮演（支持角色卡与世界设定，兼容 SillyTavern）

**自定义技能**：在 `skills/` 目录下创建技能，可为助手启用或禁用技能以扩展 AI 能力。技能来源分为三类：builtin（随 AionUi 自带）、custom（你自己创建的）和 Extension（通过 Extension SDK 贡献）。内置技能包括 `pptx`, `docx`, `pdf`, `xlsx`, `mermaid` 等。

> 💡 每个助手均由一个 Markdown 文件定义。查看 `assistant/` 目录获取示例。

</details>

---

## 随时随地进行协作（Cowork）

_你的 24/7 AI 助理 —— 在任何设备、任何地点访问 AionUi。_

- **WebUI 模式** —— 通过手机、平板或任意电脑的浏览器访问。支持局域网、跨网段及服务器部署。支持扫码或密码登录。
- **聊天平台集成**
  - **Telegram** —— 直接在 Telegram 中与你的 AI Agent 协作
  - **Lark (飞书)** —— 通过飞书机器人实现企业级协同办公
  - **DingTalk (钉钉)** —— AI 卡片流式输出，自动降级兼容
  - **WeChat (微信)** —— 个人微信号集成
  - **WeCom (企业微信)** —— 团队协作用的企业微信机器人
  - **Slack** 及更多平台即将上线

> **设置方法：** AionUi 设置 → WebUI 设置 → Channel，配置 Bot Token。

<p align="center">
  <img src="./resources/webui-remote.gif" alt="WebUI remote access demo" width="800">
</p>

<p align="center"><em>远程控制 &amp; 监控你的 Agent —— Claude, Gemini, Codex。通过浏览器或手机使用，体验与 Claude Code Remote 一致。</em></p>

> [远程互联网访问教程](https://github.com/iOfficeAI/AionUi/wiki/Remote-Internet-Access-Guide-Chinese)

## ✨ 实战体验

### **定时任务 —— 协作自动驾驶**

_配置一次，AI Agent 按时间表自动运行 —— 真正实现 24/7 无人值守操作。_

- **自然语言指令** —— 像聊天一样告诉 Agent 该做什么
- **三种调度模式** —— 标准 Cron 表达式（支持时区）、固定间隔（每 N 分钟/小时）或一次性触发
- **Agent 自主创建任务** —— 在对话过程中，Agent 可自主创建定时任务
- **使用场景：** 定时数据聚合、报告生成、文件整理、提醒通知

<p align="center">
  <img src="./resources/alart-task.png" alt="Scheduled Tasks" width="800">
</p>

<details>
<summary><strong>🔍 查看定时任务详情 ▶️</strong></summary>

<br>

**调度模式：**

- `Cron expression` —— 标准 5 字段 Cron，支持时区（例如 `0 9 * * 1`, `Asia/Shanghai`）
- `Every N minutes/hours` —— 固定间隔，例如每 30 分钟执行一次
- `One-time` —— 在指定时间触发一次后自动禁用

**执行模式：**

- `Continue in existing conversation` —— 追加到绑定的对话中，使 AI 保留完整的上下文历史
- `Create new conversation each time` —— 每次触发时开启新会话，适合独立的周期性报告

**其他能力：**

- **绑定对话** —— 每个定时任务均绑定到一个对话，保持上下文和历史连贯
- **自动执行** —— 任务在预定时间自动运行，并向对话发送消息
- **便捷管理** —— 随时创建、修改、启用/禁用、删除和查看定时任务
- **防休眠机制** —— AionUi 会在任务运行时自动防止系统休眠，并在唤醒后检测遗漏的触发器
- **高级配置** —— 每个任务可独立设置模型、工作区目录和推理强度

**实际案例：**

- 每日天气报告生成
- 每周销售数据聚合
- 月度备份文件整理
- 自定义提醒通知

</details>

---

### **预览面板 —— 即时查看 AI 生成结果**

_支持 10+ 种格式：PDF、Word、Excel、PPT、代码、Markdown、图片、HTML、Diff —— 无需切换应用即可查看全部内容。_

- **即时预览** —— Agent 生成文件后，立即查看结果，无需切换应用
- **实时追踪 + 可编辑** —— 自动跟踪文件变更；支持 Markdown、代码、HTML 的在线编辑
- **多标签页支持** —— 同时打开多个文件，每个文件独立标签页展示
- **版本历史** —— 查看并恢复文件的历史版本（基于 Git）

<p align="center">
  <img src="./resources/preview.gif" alt="Preview Panel" width="800">
</p>

<details>
<summary><strong>🔍 查看完整格式列表 ▶️</strong></summary>

<br>

**支持的预览格式：**

- **文档类** —— PDF, Word (`.doc`, `.docx`, `.odt`), Excel (`.xls`, `.xlsx`, `.ods`, `.csv`), PowerPoint (`.ppt`, `.pptx`, `.odp`)
- **代码类** —— JavaScript, TypeScript, Python, Java, Go, Rust, C/C++, CSS, JSON, XML, YAML, Shell 脚本，以及 30+ 种编程语言
- **标记语言** —— Markdown (`.md`, `.markdown`), HTML (`.html`, `.htm`)
- **图片类** —— PNG, JPG, JPEG, GIF, SVG, WebP, BMP, ICO, TIFF, AVIF
- **其他** —— Diff 文件 (`.diff`, `.patch`)

</details>

---

### **智能文件管理 —— 自动化文件操作**

_批量重命名、自动整理、智能分类、文件合并 —— 协作 Agent 替你搞定。_

<p align="center">
  <img src="./resources/aionui sort file 2.gif" alt="Smart File Management" width="800">
</p>

<details>
<summary><strong>🔍 查看文件管理功能详情 ▶️</strong></summary>

<br>

- **自动整理** —— 智能识别内容并自动分类，保持文件夹整洁有序
- **高效批量处理** —— 一键重命名、合并文件，告别繁琐的手工操作
- **自动化执行** —— AI Agent 可独立执行文件读写操作，自动完成任务流程

**使用场景：**

- 按文件类型整理杂乱的下载文件夹
- 为照片批量重命名为有意义的名称
- 将多个文档合并为一个
- 根据内容自动分类文件

</details>

---

### **Excel 数据处理 —— AI 驱动分析**

_深度分析 Excel 数据，自动美化报表并生成洞察 —— 全部由 AI Agent 驱动。_

<p align="center">
  <img src="./resources/generate_xlsx.gif" alt="Excel Processing" width="800">
</p>

<details>
<summary><strong>🔍 查看 Excel 处理功能 ▶️</strong></summary>

<br>

- **智能分析** —— AI 自动识别数据模式并生成洞察报告
- **自动排版美化** —— 一键为 Excel 报表应用专业级样式与格式
- **数据转换重组** —— 使用自然语言指令进行数据清洗、合并与结构重构
- **报表自动生成** —— 从原始数据快速生成综合分析报告

**使用场景：**

- 分析销售数据并生成月度总结报告
- 清理杂乱 Excel 文件并统一格式
- 智能合并多个电子表格
- 创建数据可视化图表

</details>

---

### **AI 图像生成与编辑**

_智能图像生成、编辑与识别，由 Gemini 驱动_

<p align="center">
  <img src="./resources/Image_Generation.gif" alt="AI Image Generation" width="800">
</p>

<details>
<summary><strong>🔍 查看图像生成功能 ▶️</strong></summary>

<br>

- **文生图** —— 根据自然语言描述生成图像
- **图像编辑** —— 修改与增强现有图片
- **图像识别** —— 分析与描述图片内容
- **批量处理** —— 一次性生成多张图像

</details>

> [图像生成模型配置指南](https://github.com/iOfficeAI/AionUi/wiki/AionUi-Image-Generation-Tool-Model-Configuration-Guide)

---

### **文档生成 —— PPT、Word、Markdown**

_借助 AI Agent 自动生成专业级文档 —— 演示文稿、报告等。_

<p align="center">
  <img src="./resources/file_generation_preview.png" alt="Document Generation" width="800">
</p>

<details>
<summary><strong>🔍 查看文档生成功能 ▶️</strong></summary>

<br>

- **PPTX 生成器** —— 根据大纲或主题创建专业演示文稿
- **Word 文档** —— 生成结构规范、排版精美的 Word 文档
- **Markdown 文件** —— 创建并格式化 Markdown 技术文档
- **PDF 转换** —— 在不同文档格式间自由转换

**使用场景：**

- 生成季度业务汇报 PPT
- 编写技术文档与说明书
- PDF 转可编辑格式
- 自动排版学术论文

</details>

### **个性化界面定制**

_自定义专属 CSS 代码，让你的界面完全符合个人偏好_

<p align="center">
  <img src="./resources/css with skin.gif" alt="CSS Customization" width="800">
</p>

- ✅ **高度可定制** —— 通过 CSS 代码自由调整界面颜色、样式与布局，打造专属使用体验

---

### **多任务并行处理**

_同时打开多个对话，任务互不干扰，独立记忆空间，效率翻倍_

<p align="center">
  <img src="./resources/multichat-side-by-side.gif" alt="Multi-Task Parallel" width="800">
</p>

- ✅ **上下文隔离** —— 每个对话保持独立的上下文与历史记录
- ✅ **并行执行** —— 同时运行多个任务，互不干扰
- ✅ **智能管理** —— 通过视觉指示器轻松切换不同对话

---

## 🤔 为何选择 AionUi 而非 Claude Cowork？

<details>
<summary><strong>点击查看详细对比</strong></summary>

<br>

AionUi 是一款 **免费开源的多 AI Agent 桌面端**。与仅支持 macOS 且绑定 Claude 的 Claude Cowork 相比，AionUi 是其全模型、跨平台的增强版。

| 维度         | Claude Cowork       | AionUi                                                                    |
| :----------- | :------------------ | :------------------------------------------------------------------------ |
| 操作系统     | 仅限 macOS          | macOS / Windows / Linux                                                   |
| 模型支持     | 仅 Claude           | Gemini, Claude, DeepSeek, OpenAI, Ollama, ...                             |
| 交互方式     | 桌面 GUI            | 桌面 GUI + WebUI + Telegram / Lark / DingTalk / WeChat / WeCom          |
| 自动化能力   | 仅限手动操作        | Cron 定时任务 —— 24/7 无人值守                                            |
| 成本         | $100/月             | 免费且开源                                                                |

深度 AI 办公场景支持：

- **文件管理**：智能整理本地文件夹，一键批量重命名。
- **数据处理**：深度分析并自动美化 Excel 报表。
- **文档生成**：自动生成排版精美的 PPT、Word 和 Markdown 文档。
- **即时预览**：内置 10+ 种格式预览面板，AI 协作结果实时可见。

</details>

---

## 快速 Q&A

<details>
<summary><strong>问：我需要先安装 Gemini CLI 或 Claude Code 吗？</strong></summary>
A: <strong>不需要。</strong> AionUi 内置了 AI Agent，安装后即可立即使用。只需通过 Google 登录或输入任意 API Key 即可开始。如果你还安装了如 Claude Code 或 Gemini CLI 等 CLI 工具，AionUi 会自动检测并集成它们，从而提供更强大的能力。
</details>

<details>
<summary><strong>问：我可以用 AionUi 做什么？</strong></summary>
A: AionUi 是你的 <strong>私人协作工作区。</strong> 内置 Agent 可以批量整理文件夹、处理 Excel 数据、生成文档、搜索网页并创建图像。通过多 Agent 模式，你还可以通过同一界面调用 Claude Code、Codex 等强大的 CLI Agent。
</details>

<details>
<summary><strong>问：它是免费的吗？</strong></summary>
A: AionUi 完全免费且开源。你可以使用 Google 账号免费体验 Gemini，或使用任意你偏好的服务商提供的 API Key。
</details>

<details>
<summary><strong>问：我可以在服务器（无头模式）上运行 AionUi 吗？</strong></summary>
A: 可以 —— AionUi WebUI 模式可作为独立的 HTTP 服务器运行。详见上方的 WebUI 部分获取设置说明。
</details>

<details>
<summary><strong>问：我的数据安全吗？</strong></summary>
A: 所有数据均本地存储在 SQLite 数据库中，不会上传至任何云端或第三方服务器。
</details>

---

## 看看大家如何使用 AionUi

<p align="center">
  <a href="https://www.youtube.com/watch?v=vWxE6VO9TKo" target="_blank">
    <img src="https://img.youtube.com/vi/vWxE6VO9TKo/maxresdefault.jpg" alt="Hermes + Aion UI is Insane (FREE)!" width="400">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.youtube.com/watch?v=RgSLdOhICZw" target="_blank">
    <img src="https://img.youtube.com/vi/RgSLdOhICZw/maxresdefault.jpg" alt="OpenClaw + Aion UI is Insane (FREE!)" width="400">
  </a>
</p>
<p align="center">
  <em>Julian Goldie SEO —— Hermes + Aion UI 太疯狂了（免费！）· 2.7万次观看</em> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>Julian Goldie SEO —— OpenClaw + Aion UI 太疯狂了（免费！）· 1.1万次观看</em>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=yUU5E-U5B3M" target="_blank">
    <img src="https://img.youtube.com/vi/yUU5E-U5B3M/maxresdefault.jpg" alt="WorldofAI Review" width="400">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.youtube.com/watch?v=enQnkKfth10" target="_blank">
    <img src="https://img.youtube.com/vi/enQnkKfth10/maxresdefault.jpg" alt="Julian Goldie SEO Review" width="400">
  </a>
</p>
<p align="center">
  <em>WorldofAI (20万订阅者)</em> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>Julian Goldie SEO (38.4万订阅者)</em>
</p>

### 社区文章

- [开源免费协作工具，全模型接入+自主文件操作](https://mp.weixin.qq.com/s/F3f-CCsVPaK3lK00jXhOOg) — 开源AI项目落地
- [让普通人像用APP一样使用Claude Code](https://mp.weixin.qq.com/s/TsMojSbkUUFvsd-HQCazZg) — 懒猫爱钓鱼
- [5500 Stars：开源如何打破Anthropic的AI工具护城河](https://mp.weixin.qq.com/s/saEk49cYV6MqBgw19Lw6Gw) — AI硅基时刻

> **制作了关于 AionUi 的视频？** [在 X (Twitter) 上告诉我们](https://x.com/AionUi)，我们将在此展示！

---

## 🚀 快速开始

### 系统要求

- **macOS**: 10.15 或更高版本
- **Windows**: Windows 10 或更高版本
- **Linux**: Ubuntu 18.04+ / Debian 10+ / Fedora 32+
- **内存**: 建议 4GB+
- **存储**: 至少 500MB 可用空间

### 安装

<p>
  <a href="https://github.com/iOfficeAI/AionUi/releases">
    <img src="https://img.shields.io/badge/Download-Latest%20Release-32CD32?style=for-the-badge&logo=github&logoColor=white" alt="Download Latest Release" height="50">
  </a>
</p>

点击上方按钮前往 Releases 页面，下载对应平台的安装包（macOS / Windows / Linux）。

```bash
# 或者通过 Homebrew 安装 (macOS)
brew install aionui
```

### 3 步上手

1. **安装** AionUi
2. **登录** Google 账号或输入任意 API Key
3. **开始协作** —— 内置 AI Agent 已准备就绪

### 📖 详细指南

<details>
<summary><strong>📖 展开查看完整使用指南</strong></summary>

<br>

**🚀 快速入门**

- [📖 完整安装指南](https://github.com/iOfficeAI/AionUi/wiki/Getting-Started) —— 从下载到配置的详细步骤
- [⚙️ LLM 配置指南](https://github.com/iOfficeAI/AionUi/wiki/LLM-Configuration) —— 多平台 AI 模型配置说明
- [🤖 多 Agent 模式设置](https://github.com/iOfficeAI/AionUi/wiki/ACP-Setup) —— 集成终端 AI Agent
- [🔌 MCP 工具配置](https://github.com/iOfficeAI/AionUi/wiki/MCP-Configuration-Guide) —— 模型上下文协议服务器设置
- [🌐 WebUI 配置指南](https://github.com/iOfficeAI/AionUi/wiki/WebUI-Configuration-Guide) —— 完整的 WebUI 设置与配置教程

**🎯 使用场景**

- [📁 文件管理](https://github.com/iOfficeAI/AionUi/wiki/file-management) —— 智能文件整理
- [📊 Excel 处理](https://github.com/iOfficeAI/AionUi/wiki/excel-processing) —— AI 驱动的数据处理
- [🎨 图像生成](https://github.com/iOfficeAI/AionUi/wiki/AionUi-Image-Generation-Tool-Model-Configuration-Guide) —— AI 图像创作
- [📚 更多使用场景](https://github.com/iOfficeAI/AionUi/wiki/Use-Cases-Overview)

**❓ 支持与帮助**

- [❓ 常见问题 (FAQ)](https://github.com/iOfficeAI/AionUi/wiki/FAQ) —— 问题解答与故障排除
- [🔧 配置与使用教程](https://github.com/iOfficeAI/AionUi/wiki/Configuration-Guides) —— 完整的配置文档

</details>

---

## 💬 社区与支持

**你的想法很重要！** 我们珍视每一条建议与反馈。

<p align="center">
  <a href="https://x.com/AionUi" target="_blank">
    <img src="./resources/contactus-x.png" alt="Contact Us on X" width="600">
  </a>
</p>

- [GitHub Discussions](https://github.com/iOfficeAI/AionUi/discussions) —— 分享想法与交流技巧
- [报告问题 (Issues)](https://github.com/iOfficeAI/AionUi/issues) —— Bug 反馈与功能请求
- [版本更新 (Releases)](https://github.com/iOfficeAI/AionUi/releases) —— 获取最新版本
- [Discord 社区](https://discord.gg/2QAwJn7Egx) —— 英文社区交流
- [微信群](./resources/wx-9.png) —— 中文社区交流

### 贡献代码 (Contributing)

请在提交 PR 前阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 发起 Pull Request

### 开发环境搭建

技术栈：Electron · Vite · React · Bun

```bash
bun install        # 安装依赖
bun run dev        # 启动开发服务器
bun run test       # 运行单元测试
```

---

## License

本项目采用 [Apache-2.0](LICENSE) 许可证。

---

## Contributors

<p align="center">
  <a href="https://github.com/iOfficeAI/AionUi/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=iOfficeAI/AionUi&max=100" alt="Contributors" />
  </a>
</p>

## Star History

<p align="center">
  <a href="https://www.star-history.com/#iOfficeAI/aionui&Date" target="_blank">
    <img src="https://api.star-history.com/svg?repos=iOfficeAI/aionui&type=Date" alt="Star History" width="600">
  </a>
</p>

<div align="center">

**如果你喜欢它，请给我们一个 Star**

[报告 Bug](https://github.com/iOfficeAI/AionUi/issues) · [请求功能](https://github.com/iOfficeAI/AionUi/issues)

</div>

<sub><a href="https://linux.do/">LINUX DO - A New Ideal Community</a></sub>