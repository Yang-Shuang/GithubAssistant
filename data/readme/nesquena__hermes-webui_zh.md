# Hermes Web UI

[Hermes Agent](https://hermes-agent.nousresearch.com/) 是一款运行在你服务器上的高级自主智能体，可通过终端或消息应用访问。它会记住所学内容，运行时间越长越强大。

Hermes WebUI 是专为 [Hermes Agent](https://hermes-agent.nousresearch.com/) 打造的轻量级、深色主题网页应用界面。与 CLI（命令行）体验完全一致——你在终端能做的所有操作，都能在此 UI 中完成。无需构建步骤、框架或打包工具。仅依赖 Python 和原生 JavaScript。

布局：三栏设计。左侧边栏用于会话管理和导航，中间为聊天区，右侧为工作区文件浏览。模型、配置和工作区控件位于 **底部编辑区 (composer footer)**——始终可见。圆形上下文环直观显示 Token 使用情况。所有设置和会话工具均在 **Hermes 控制中心 (Control Center)**中（侧边栏底部的启动器）。

<img width="2448" height="1748" alt="Hermes Web UI — three-panel layout" src="https://github.com/user-attachments/assets/6bf8af4c-209d-441e-8b92-6515d7a0c369" />

<table>
  <tr>
    <td width="50%" align="center">
      <img width="2940" height="1848" alt="Light mode with full profile support" src="https://github.com/user-attachments/assets/4ef3a59c-7a66-4705-b4e7-cb9148fe4c47" />
      <br /><sub>支持完整配置文件的亮色模式</sub>
    </td>
    <td width="50%" align="center">
      <img alt="Customize your settings, configure a password" src="https://github.com/user-attachments/assets/941f3156-21e3-41fd-bcc8-f975d5000cb8" />
      <br /><sub>自定义设置，配置密码</sub>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="50%" align="center">
      <img alt="Workspace file browser with inline preview" src="docs/images/ui-workspace.png" />
      <br /><sub>支持内联预览的工作区文件浏览器</sub>
    </td>
    <td width="50%" align="center">
      <img alt="Session projects, tags, and tool call cards" src="docs/images/ui-sessions.png" />
      <br /><sub>会话项目、标签与工具调用卡片</sub>
    </td>
  </tr>
</table>

这为你提供了与 Hermes CLI 近乎 **1:1 的网页 UI 体验**。你可以通过 SSH 隧道安全访问它。只需一条命令即可启动，另一条命令建立 SSH 隧道供本地电脑访问。Web UI 的每个部分都直接使用你现有的 Hermes 智能体和模型，无需任何额外设置。

---

## 目录

- [为什么选择 Hermes](#why-hermes) — 产品简介与对比分析
- [快速入门](#quick-start) — 克隆 + `bootstrap.py` / `start.sh` / `ctl.sh`
- [功能特性](#features) — 聊天、会话、工作区、语音、配置文件、安全、主题、面板、移动端适配
- [配置与访问](#configuration--access) — 自动发现、覆盖参数、远程/Tailscale/手机访问、手动启动
- [Docker](#docker) — 单容器与多容器部署
- [运行测试](#running-tests)
- [架构](#architecture) — 后端/前端布局、状态目录
- [文档](#docs) — 完整文档索引
- [贡献者](#contributors)

---

## 为什么选择 Hermes

大多数 AI 工具每次会话都会重置上下文。它们不知道你是谁、你做过什么工作，或你的项目遵循哪些规范。每次都需要重新解释一遍。

Hermes 能够跨会话保留上下文，在你离线时运行定时任务，并且随着运行时间增长越来越了解你的环境。它直接使用你现有的 Hermes 智能体配置和模型，无需额外设置即可开始使用。

与其他智能体工具的不同之处：

- **持久化记忆** — 用户配置文件、智能体笔记和技能系统可保存可复用流程；Hermes 会学习你的环境，无需重复学习
- **自托管调度** — 定时任务在你离线时触发，并将结果推送到 Telegram、Discord、Slack、Signal、邮件等
- **支持 10+ 消息平台** — 终端中可用的同一智能体也可通过手机访问
- **自我进化技能** — Hermes 会根据经验自动编写并保存自身技能；无需浏览市场，也无需安装插件
- **模型无关/多供应商支持** — OpenAI、Anthropic、Google、DeepSeek、OpenRouter 等
- **编排其他智能体** — 可启动 Claude Code 或 Codex 处理重型编码任务，并将结果带回自身记忆库
- **自托管** — 你的对话、你的记忆、你的硬件

**vs. 竞品对比** *(市场格局动态变化中——详见 [docs/why-hermes.md](docs/why-hermes.md) 的完整拆解)*:

| | OpenClaw | Claude Code | Codex CLI | OpenCode | Hermes |
|---|---|---|---|---|---|
| 持久化记忆（自动） | 是 | 部分† | 部分 | 部分 | 是 |
| 定时任务（自托管） | 是 | 否‡ | 否 | 否 | 是 |
| 消息应用访问 | 是（15+ 平台） | 部分（Telegram/Discord 预览） | 否 | 否 | 是（10+） |
| Web UI（自托管） | 仅仪表盘 | 否 | 否 | 是 | 是 |
| 自我进化技能 | 部分 | 否 | 否 | 否 | 是 |
| Python / ML 生态 | 否（Node.js） | 否 | 否 | 否 | 是 |
| 模型无关/多供应商支持 | 是 | 否（仅 Claude） | 是 | 是 | 是 |
| 开源 | 是（MIT） | 否 | 是 | 是 | 是 |

† Claude Code 拥有 CLAUDE.md / MEMORY.md 项目上下文和滚动自动记忆，但并非完整的跨会话自动召回  
‡ Claude Code 提供云端托管调度（Anthropic 基础设施）和会话级 `/loop`；不支持自托管 cron

**最接近的竞品是 OpenClaw** — 两者都是始终在线、自托管、开源且具备记忆、cron 和消息功能的智能体。关键区别在于：Hermes 将自动编写并保存自身技能作为核心行为（OpenClaw 的技能系统侧重于社区市场）；Hermes 在版本更新中更稳定（OpenClaw 有已记录的回退问题，ClawHub 曾发生涉及恶意技能的网络安全事件）；且 Hermes 原生运行于 Python 生态。详见 [docs/why-hermes.md](docs/why-hermes.md) 的完整对比。

---

## 快速入门

运行仓库引导脚本：

```bash
git clone https://github.com/nesquena/hermes-webui.git hermes-webui
cd hermes-webui
python3 bootstrap.py
```

或继续使用 Shell 启动器：

```bash
./start.sh
```

对于自托管虚拟机或家庭实验室安装，`ctl.sh` 封装了常见的守护进程生命周期命令，无需依赖 `fuser` 或 `pkill`：

```bash
./ctl.sh start              # 后台运行守护进程，PID 记录在 ~/.hermes/webui.pid
./ctl.sh status             # PID、运行时间、绑定主机/端口、日志路径、/health
./ctl.sh logs --lines 100   # tail ~/.hermes/webui.log
./ctl.sh restart
./ctl.sh stop
```

`ctl.sh start` 会在守护进程包装器下以前台/无浏览器模式运行引导脚本，日志写入 `~/.hermes/webui.log`，并支持 `.env` 及内联覆盖参数（如 `HERMES_WEBUI_HOST=0.0.0.0 ./ctl.sh start`）。

### 高级功能：动态召回预填充与 Gateway 支持的聊天

两项可选的自托管部署特性——将动态**会话召回预填充**附加到浏览器对话轮次中（支持 Joplin/Obsidian/Notion/llm-wiki 路由器），以及通过运行的 **Hermes Gateway** 路由浏览器聊天——详见 [`docs/advanced-chat-setup.md`](docs/advanced-chat-setup.md)。大多数用户无需使用这些功能。

引导脚本将执行以下操作：

1. 检测 Hermes Agent，若缺失则尝试官方安装器（`curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`）。
2. 查找或创建包含 WebUI 依赖的 Python 环境。
3. 启动 Web 服务器并等待 `/health` 就绪。
4. 除非传递 `--no-browser`，否则自动打开浏览器。
5. 引导你进入 WebUI 内的首次运行向导。

> 此引导脚本暂不支持原生 Windows。请使用 Linux、macOS 或 WSL2。
> 如需在登录时自动启动 Windows/WSL，请参阅 [`docs/wsl-autostart.md`](docs/wsl-autostart.md)。

社区维护的原生 Windows 设置文档见 [@markwang2658/hermes-windows-native-guide](https://github.com/markwang2658/hermes-windows-native-guide)（配套仓库：[@markwang2658/hermes-windows-native](https://github.com/markwang2658/hermes-windows-native)）。社区在 [#1952](https://github.com/nesquena/hermes-webui/issues/1952) 中的反馈笔记如下：

- **内存占用：** 社区实测约 330 MB（原生）对比 ~1080 MB（WSL2+Docker，因配置而异）。
- **可用功能：** 聊天、工作区浏览器、会话管理、所有主题。
- **已知限制：** 工作区浏览器中可能出现部分 POSIX 风格文件路径；假设使用 bash 的智能体工具可能无法原生运行。
- **原生 Windows 设置：** 安装 Python 3.11+，然后在 hermes-agent 根目录的 PowerShell 中执行：`python -m venv venv` → `pip install -r requirements.txt` → `pwsh .\start.ps1`（它会自动发现 `venv\Scripts\python.exe`）。
- **WSL2 关系：** 非必需——WSL2 构建的 venv (`venv/bin/python`, ELF) 无法被原生 Windows Python 调用，因此请使用上述原生设置。如果你希望保留完整的 `bootstrap.py` + Linux 运行时，WSL2 仍可作为并行安装使用。

如果安装后供应商配置仍未完成，引导向导会指引你使用 `hermes model` 完成配置，而不是尝试在浏览器中复制完整的 CLI 设置流程。
如需逐步指南、供应商选择、本地模型服务器 Base URL 及安全重新运行说明，请参阅 [`docs/onboarding.md`](docs/onboarding.md)。
如果有 AI 助手协助安装、重装、引导、供应商设置或首次运行支持，请在执行命令或检查日志前让其阅读 [`docs/onboarding-agent-checklist.md`](docs/onboarding-agent-checklist.md)。

---

## 功能特性

### 聊天与智能体
- 通过 SSE（服务器发送事件）实现流式响应（Token 生成时实时显示）
- 多供应商模型支持——任意 Hermes API 供应商（OpenAI、Anthropic、Google、DeepSeek、Nous Portal、OpenRouter、MiniMax、Xiaomi MiMo、Z.AI）；动态模型下拉菜单从已配置的密钥中填充
- 处理中发送消息——自动排队等待
- 内联编辑任意历史用户消息并从该点重新生成
- 一键重试上一次智能体回复
- 直接从底部编辑区取消运行中的任务（发送按钮旁的停止按钮）
- 内联工具调用卡片——每张显示工具名称、参数和结果片段；支持多轮次展开/收起切换
- 子智能体委派卡片——以不同图标和缩进边框展示子智能体活动
- 内联渲染 Mermaid 图表（流程图、时序图、甘特图）
- 思考/推理显示——可折叠的金色主题卡片，用于 Claude 扩展思考和 o3 推理块
- 危险 Shell 命令审批卡片（允许一次/本次会话/始终/拒绝）
- 网络抖动时 SSE 自动重连（SSH 隧道弹性保障）
- 文件附件在页面刷新后持久保存，默认存储在工作区之外 (`~/.hermes/webui/attachments/<session_id>/`，配置 `HERMES_WEBUI_ATTACHMENT_DIR/<session_id>/` 时生效)
- 消息时间戳（每条消息旁显示 HH:MM，悬停显示完整日期）
- 代码块复制按钮及“已复制！”反馈提示
- 通过 Prism.js 实现语法高亮（Python、JS、bash、JSON、SQL 等）
- AI 回复中的安全 HTML 渲染（加粗、斜体、代码转换为 Markdown）
- 使用 rAF 节流 Token 流式传输，长回复时渲染更流畅
- 底部编辑区上下文使用指示器——Token 计数、成本和使用率进度条（模型感知）

### 会话管理
- 创建、重命名、复制、删除，支持按标题和内容搜索
- 通过每会话的 `⋯` 下拉菜单执行操作——置顶、移至项目、归档、复制、删除
- 将会话置顶/星标显示在侧边栏顶部（金色指示器）
- 归档会话（隐藏但不删除，可切换显示）
- 会话项目——带颜色的命名分组，用于组织会话
- 会话标签——在标题中添加 `#tag` 生成彩色标签并支持点击筛选
- 侧边栏按今天/昨天/更早分组（可折叠日期组）
- 导出为 Markdown 记录、完整 JSON 或从 JSON 导入
- 会话在页面刷新和 SSH 隧道重连后持久保存
- 浏览器标签页标题显示当前活动会话名称
- CLI 会话桥接——hermes-agent SQLite 存储中的 CLI 会话会以金色“cli”徽章显示在侧边栏；点击即可导入完整历史并正常回复
- Token/成本显示——每条对话展示输入 Token、输出 Token 和预估成本（可在设置或 `/usage` 命令中切换）

### 工作区文件浏览器
- 目录树支持展开/收起（单击切换，双击导航）
- 面包屑导航，路径片段可点击
- 内联预览文本、代码、Markdown（已渲染）和图片
- 使用 `workspace://path/to/file` 格式的聊天链接可在右侧预览窗格中打开文件
- 编辑、创建、删除和重命名文件；创建文件夹
- 二进制文件下载（服务器自动检测）
- 目录导航时自动关闭文件预览（含未保存编辑保护）
- Git 检测——工作区头部显示分支名称和修改文件计数徽章
- 右侧面板支持拖拽调整大小
- 语法高亮代码预览（Prism.js）

### 语音输入
- 编辑区麦克风按钮（基于 Web Speech API）
- 点击录音，再次点击或发送以停止
- 实时中间转录文本显示在输入框中
- 约 2 秒静音后自动停止
- 追加到现有输入框内容（不覆盖）
- 浏览器不支持 Web Speech API 时隐藏（Chrome、Edge、Safari 支持）

### 配置文件
- **底部编辑区**的配置文件标签——下拉菜单显示所有配置文件及网关状态和模型信息
- 网关状态圆点（绿色=运行中）、模型信息、每配置文件的技能数量
- 配置文件管理面板——从侧边栏创建、切换和删除配置文件
- 创建时克隆当前活动配置的配置
- 创建时可自定义端点字段——Base URL 和 API Key 在创建时写入配置文件的 `config.yaml`，以便手动编辑文件即可配置 Ollama、LMStudio 等本地端点
- 无缝切换——无需重启服务器；重新加载配置、技能、记忆、cron 和模型
- 逐会话配置文件跟踪（记录创建时激活的配置文件）

### 认证与安全
- 可选密码认证——默认关闭，本地访问零摩擦
- 通过环境变量 `HERMES_WEBUI_PASSWORD` 或设置面板启用
- 可选通行密钥/WebAuthn——登录后在“设置 -> 系统”中注册；登录页仅在至少存在一个通行密钥后显示通行密钥登录选项
- 注册至少一个通行密钥后，可在“设置 -> 系统”中移除密码并仅保留通行密钥登录。在选择不使用密码前，密码认证仍作为引导/恢复路径；通行密钥遵循同源策略，存储于 WebUI 本地状态目录
- 带 24 小时有效期的签名 HMAC 仅 HTTP Cookie
- `/login` 处的极简深色主题登录页
- 所有响应均包含安全头（X-Content-Type-Options, X-Frame-Options, Referrer-Policy）
- 20MB POST 请求体大小限制
- CDN 资源使用 SRI 完整性哈希锁定

### 主题
- 外观分为两个维度：主题（`system`、`dark`、`light`）和皮肤（`default`、`ares`、`mono`、`slate`、`poseidon`、`sisyphus`、`charizard`、`sienna`、`catppuccin`、`nous`、`geist-contrast` / Geist Contrast）
- 通过“设置 -> 外观”切换（即时实时预览）或使用 `/theme <主题或皮肤>`
- 跨刷新持久保存（服务器端 `settings.json` + localStorage，实现无闪烁加载）
- 皮肤使用 `data-skin` 及 CSS 变量；深色模式通过 `.dark` 类解析，而非 `data-theme` 自定义主题轴——详见 [THEMES.md](THEMES.md)

### 设置与配置
- **Hermes 控制中心**（侧边栏启动器按钮）——对话标签页（导出/导入/清空）、偏好设置标签页（模型、发送键、主题、语言、所有开关）、系统标签页（版本、密码）
- 发送快捷键：Enter（默认）或 Ctrl/Cmd+Enter
- 显示/隐藏 CLI 会话切换（默认启用）
- Token 使用显示切换（默认关闭，也可通过 `/usage` 命令控制）
- 控制中心始终在对话标签页打开；关闭时重置
- 未保存更改保护——关闭含未持久化更改的窗口时会提示丢弃/保存
- Cron 完成提醒——任务标签页显示 Toast 通知和未读徽章
- 后台智能体错误提醒——非活动会话遇到错误时显示横幅

### 斜杠命令
- 在编辑区输入 `/` 触发自动补全下拉菜单
- 内置命令：`/help`、`/clear`、`/compress [焦点主题]`、`/compact`（别名）、`/model <名称>`、`/workspace <名称>`、`/new`、`/usage`、`/theme`
- 方向键导航，Tab/Enter 选择，Escape 关闭
- 未识别的命令将透传给智能体

### 面板
- **聊天**——会话列表、搜索、置顶、归档、项目、新建对话
- **任务**——查看、创建、编辑、运行、暂停/恢复、删除 cron 任务；运行历史；完成提醒
- **技能**——按类别列出所有技能，搜索、预览、创建/编辑/删除；关联文件查看器
- **记忆**——内联查看和编辑 `MEMORY.md` 与 `USER.md`
- **配置文件**——创建、切换、删除智能体配置文件；克隆配置
- **待办事项**——来自当前会话的实时任务列表
- **空间**——添加、重命名、移除工作区；从顶部栏快速切换

### 移动端响应式适配
- 汉堡菜单侧边栏——移动端（<640px）滑动覆盖层
- 移动端保留侧边栏顶部标签；无固定底部导航占用聊天高度
- 文件面板从右侧边缘滑入
- 所有交互元素触控目标最小 44px
- 手机端全屏聊天/编辑区，无底部导航间距干扰
- 桌面端布局完全不变

---

## 配置与访问

`start.sh` 自动检测几乎所有内容；以下小节涵盖无法自动检测时的调整选项及远程访问方法。

### start.sh 的自动发现功能

| 项目 | 查找方式 |
|---|---|
| Hermes agent 目录 | `HERMES_WEBUI_AGENT_DIR` 环境变量，随后是 `$HERMES_HOME/hermes-agent`（Windows 默认 `%LOCALAPPDATA%\hermes\hermes-agent`，POSIX 默认 `~/.hermes/hermes-agent`），最后是同级 `../hermes-agent` |
| Python 可执行文件 | Agent venv 优先，其次是本仓库的 `.venv`，然后是系统 `python3` |
| 状态目录 | `HERMES_WEBUI_STATE_DIR` 环境变量，随后是 `$HERMES_HOME/webui`（Windows 默认 `%LOCALAPPDATA%\hermes\webui`，POSIX 默认 `~/.hermes/webui`） |
| 默认工作区 | `HERMES_WEBUI_DEFAULT_WORKSPACE` 环境变量，随后是 `~/workspace`，最后是状态目录 |
| 端口 | `HERMES_WEBUI_PORT` 环境变量或第一个参数，默认 `8787` |

如果自动发现找到所有项目，则无需其他操作。

---

### 覆盖配置（仅在自动检测遗漏时需要）

```bash
export HERMES_WEBUI_AGENT_DIR=/path/to/hermes-agent
export HERMES_WEBUI_PYTHON=/path/to/python
export HERMES_WEBUI_PORT=9000
export HERMES_WEBUI_AUTO_INSTALL=1  # 启用 Agent 依赖的自动安装（默认关闭）
./start.sh
```

或内联执行：

```bash
HERMES_WEBUI_AGENT_DIR=/custom/path ./start.sh 9000
```

完整环境变量列表：

| 变量名 | 默认值 | 描述 |
|---|---|---|
| `HERMES_WEBUI_AGENT_DIR` | 自动发现 | hermes-agent 检出路径 |
| `HERMES_WEBUI_PYTHON` | 自动发现 | Python 可执行文件路径 |
| `HERMES_WEBUI_HOST` | `127.0.0.1` | 绑定地址（`0.0.0.0` 表示所有 IPv4，`::` 表示所有 IPv6，`::1` 为 IPv6 回环） |
| `HERMES_WEBUI_PORT` | `8787` | 端口号 |
| `HERMES_WEBUI_STATE_DIR` | `$HERMES_HOME/webui` (Windows 默认 `%LOCALAPPDATA%\hermes\webui`, POSIX 默认 `~/.hermes/webui`) | 会话和状态存储位置 |
| `HERMES_WEBUI_DEFAULT_WORKSPACE` | `~/workspace` | 默认工作区路径 |
| `HERMES_WEBUI_DEFAULT_MODEL` | *(供应商默认)* | 可选模型覆盖；留空则使用当前 Hermes 供应商默认值 |
| `HERMES_WEBUI_PASSWORD` | *(未设置)* | 设置以启用密码认证 |
| `HERMES_WEBUI_CSP_CONNECT_EXTRA` | *(未设置)* | 可选的 `http(s)://` 或 `ws(s)://` 源（空格分隔），追加到报告型 CSP `connect-src` 指令中，适用于反向代理或隧道部署 |
| `HERMES_WEBUI_EXTENSION_DIR` | *(未设置)* | 可选的本地目录，在 `/extensions/` 提供；启用扩展注入前必须指向现有目录 |
| `HERMES_WEBUI_EXTENSION_SCRIPT_URLS` | *(未设置)* | 可选的同源脚本 URL（逗号分隔）用于注入；详见 [WebUI Extensions](docs/EXTENSIONS.md) |
| `HERMES_WEBUI_EXTENSION_STYLESHEET_URLS` | *(未设置)* | 可选的同源样式表 URL（逗号分隔）用于注入；详见 [WebUI Extensions](docs/EXTENSIONS.md) |
| `HERMES_HOME` | Windows: `%LOCALAPPDATA%\hermes`; POSIX: `~/.hermes` | Hermes 状态基础目录（影响所有路径） |
| `HERMES_CONFIG_PATH` | `$HERMES_HOME/config.yaml` | Hermes 配置文件路径 |

---

### 远程访问（SSH 隧道、Tailscale、手机）

服务器默认绑定到 `127.0.0.1`。要从其他机器访问，请使用 SSH 隧道（`ssh -N -L 8787:127.0.0.1:8787 user@host`，通过 SSH 连接时 `start.sh` 会为你打印该命令），或将服务器和手机加入 [Tailscale](https://tailscale.com) 网络并访问 `http://<server-tailscale-ip>:8787`（需设置 `HERMES_WEBUI_HOST=0.0.0.0` + `HERMES_WEBUI_PASSWORD`）。完整指南（含社区 ARM64-Android 现场报告）：[`docs/remote-access.md`](docs/remote-access.md)。

### 手动启动（不使用 start.sh）

如需直接启动服务器：

```bash
cd /path/to/hermes-agent          # 或 sys.path 可找到 Hermes 模块的任意目录
HERMES_WEBUI_PORT=8787 venv/bin/python /path/to/hermes-webui/server.py
```

注意：请使用 Agent venv 的 Python（或已安装 Hermes agent 依赖的任何 Python 环境）。系统 Python 会缺少 `openai`、`httpx` 等必需包。

健康检查：

```bash
curl http://127.0.0.1:8787/health
```

---

## Docker

**预构建镜像**（amd64 + arm64）在每个版本发布时同步推送到 GHCR。

涵盖所有 3 个 compose 文件、常见故障及 bind-mount 迁移的综合设置指南，请参阅 [`docs/docker.md`](docs/docker.md)。本 README 仅覆盖 5 分钟快速入门路径。

### 5 分钟快速入门（单容器）

最简单的设置：一个在进程内运行 Agent 的 WebUI 容器。

```bash
git clone https://github.com/nesquena/hermes-webui
cd hermes-webui
cp .env.docker.example .env
# 如果你的宿主机 UID 不是 1000（例如 macOS，UID 从 501 开始），请编辑 .env
docker compose up -d
# 访问 http://localhost:8787
```

以拥有 Hermes 主目录的用户身份运行 Compose。`sudo docker compose up -d` 可能导致 `${HOME}` 展开为 root 用户的主目录，从而 Docker 挂载错误的 `.hermes` 目录而非你的真实 `~/.hermes`，导致 WebUI 启动时提示 `config.yaml (not found, using defaults)`。建议将用户加入 Docker 组并运行 `docker compose up -d`；若必须使用 sudo，请先设置绝对路径，例如 `HERMES_HOME=/home/you/.hermes HERMES_WORKSPACE=/home/you/workspace sudo -E docker compose up -d`，然后通过 `docker compose config` 验证。

容器会自动检测挂载的 `~/.hermes` 卷中的 UID/GID，确保 Agent 写入的文件在宿主机上对你可读。

如需启用密码保护（将端口暴露到 `127.0.0.1` 之外时必需）：

```bash
echo "HERMES_WEBUI_PASSWORD=change-me-to-something-strong" >> .env
docker compose up -d --force-recreate
```

### 手动 `docker run`（不使用 Compose）

```bash
docker pull ghcr.io/nesquena/hermes-webui:latest
docker run -d \
  -e WANTED_UID=$(id -u) -e WANTED_GID=$(id -g) \
  -v ~/.hermes:/home/hermeswebui/.hermes \
  -e HERMES_WEBUI_STATE_DIR=/home/hermeswebui/.hermes/webui \
  -v ~/workspace:/workspace \
  -p 127.0.0.1:8787:8787 \
  ghcr.io/nesquena/hermes-webui:latest
```

### 本地构建

```bash
docker build -t hermes-webui .
docker run -d \
  -e WANTED_UID=$(id -u) -e WANTED_GID=$(id -g) \
  -v ~/.hermes:/home/hermeswebui/.hermes \
  -e HERMES_WEBUI_STATE_DIR=/home/hermeswebui/.hermes/webui \
  -v ~/workspace:/workspace \
  -p 127.0.0.1:8787:8787 \
  hermes-webui
```

### 多容器设置

若希望将 Agent 和 WebUI 分离到不同容器中（用于隔离，或因为你已在其他地方运行 Agent Gateway）：

```bash
# Agent + WebUI
docker compose -f docker-compose.two-container.yml up -d

# Agent + Dashboard + WebUI
docker compose -f docker-compose.three-container.yml up -d
```

两个 Compose 文件默认使用**命名 Docker 卷**，从架构上解决了 UID/GID 问题。如需 bind mount 共享现有宿主机目录，请参阅 [`docs/docker.md`](docs/docker.md) 中的完整迁移方案。

> **已知限制 (#681)**：在双容器设置中，从 WebUI 触发的工具运行在**WebUI 容器**内，而非 Agent 容器。若需要 Git/Node 等位于 WebUI 文件系统上，请使用单容器设置、扩展 WebUI Dockerfile，或使用社区 [all-in-one image](https://github.com/sunnysktsang/hermes-suite)。
> 
> **源码边界说明 (#2453)**：多容器设置默认以只读方式将 `hermes-agent-src` 挂载到 WebUI。这阻止了 WebUI 端的源码重写，但仍属于实现耦合的桥接，而非稳定的 Agent API 边界。详见 [`docs/rfcs/agent-source-boundary.md`](docs/rfcs/agent-source-boundary.md) 中的当前源码/API 解耦清单。

### 常见故障模式

| 症状 | 可能原因 | 解决方法 |
|---|---|---|
| 启动时 `PermissionError` | bind mount UID 不匹配 | 在 `.env` 中设置 `UID=$(id -u)` |
| `.env: permission denied` (#1389) | `fix_credential_permissions()` 强制设为 0600 | 在 `.env` 中设置 `HERMES_SKIP_CHMOD=1` |
| 工作区显示为空 | `/workspace` 挂载 UID 不匹配 | 在 `.env` 中设置 `UID=$(id -u)` |
| 聊天中出现 `git: command not found` | 双容器架构限制 (#681) | 使用单容器或扩展 Dockerfile |
| WebUI 找不到 Agent 源码 | `hermes-agent-src` 卷配置错误 | 直接使用 Compose 文件中的命名卷 |
| Podman 共享 `.hermes` 失败 | Podman 3.4 `keep-id` 限制 | 使用 Podman 4+ 或单容器设置 |
| Host API 在 WebUI 的 `localhost` 访问失败 | 容器内的 `localhost` 指代的是容器本身，而非宿主机 (#3012) | Docker Desktop 使用 `http://host.docker.internal:<port>`，Podman 使用 `http://host.containers.internal:<port>` |
| `sudo docker compose` 后 WebUI 无法看到 `~/.hermes` | `${HOME}` 展开为 root 用户主目录 (#3006) | 以你的用户身份运行 Compose，或使用 `sudo -E` 传递绝对路径的 `HERMES_HOME`/`HERMES_WORKSPACE` |

每个故障的深度排查指南见 [`docs/docker.md`](docs/docker.md)。

> **注意：** 默认情况下，Docker Compose 绑定到 `127.0.0.1`（仅限本地）。要在网络中暴露，请将 `docker-compose.yml` 中的端口改为 `"8787:8787"`，并设置 `HERMES_WEBUI_PASSWORD` 以启用认证。

---

## 运行测试

测试会动态发现仓库和 Hermes Agent——无需硬编码路径。

```bash
cd hermes-webui
pytest tests/ -v --timeout=60
```

或使用 Agent venv 显式运行：

```bash
/path/to/hermes-agent/venv/bin/python -m pytest tests/ -v
```

测试在隔离的服务器环境下运行，使用独立的状态目录。生产数据和真实 cron 任务绝不会被触碰。当前快照：**~7,150 个测试**分布在 **~700 个测试文件**中，在 CI 环境中针对 Python 3.11、3.12 和 3.13 运行（各 3 个并行分片）。

---

## 架构

无需构建步骤、框架或打包工具——基于 Python 标准库 HTTP 服务器和原生 JavaScript。后端位于 `api/`，前端位于 `static/`。

**后端 (`api/`)**

```
server.py         HTTP routing shell + auth middleware
api/
  auth.py         Optional password authentication, signed cookies, passkeys
  config.py       Discovery, globals, model detection, reloadable config
  helpers.py      HTTP helpers, security headers
  models.py       Session model + CRUD + CLI/state.db bridge
  onboarding.py   First-run onboarding wizard, OAuth provider support
  profiles.py     Profile state management, hermes_cli wrapper
  routes.py       All GET + POST route handlers (if/elif dispatch, no decorators)
  state_sync.py   /insights sync — message_count to state.db
  streaming.py    SSE engine, run_agent, cancellation, compression
  updates.py      Self-update check and release notes
  upload.py       Multipart parser, file upload handler
  workspace.py    File ops, workspace helpers, git detection
```

**前端 (`static/`)**

```
index.html        HTML template
style.css         All CSS incl. mobile responsive, themes + skins
ui.js             DOM helpers, renderMd, tool cards, context indicator
workspace.js      File preview, file ops, git badge, central api() fetch wrapper
sessions.js       Session CRUD, collapsible groups, search, reload recovery
messages.js       send(), SSE handlers, live streaming, session recovery
panels.js         Cron, skills, memory, profiles, settings (Control Center)
commands.js       Slash command autocomplete
boot.js           Mobile nav, voice input, theme/skin boot, bfcache handler
```

**测试与打包**

```
tests/            Pytest suite (~7,150 tests; isolated server/state fixtures)
pyproject.toml    Tooling config (ruff lint gate) — not a packaged distribution
Dockerfile        python:3.12-slim container image
docker-compose.yml  Compose with named volume and optional auth
.github/workflows/  CI: ruff + sharded pytest, browser smoke, Docker smoke,
                    multi-arch Docker build + GitHub Release on tag
```

状态默认存储在仓库外的 `~/.hermes/webui/`（会话、工作区、设置、项目、最后使用的工作区）。可通过 `HERMES_WEBUI_STATE_DIR` 覆盖。完整设计说明和端点目录见 [`ARCHITECTURE.md`](ARCHITECTURE.md)。

---

## 文档

**从这里开始**
- [`docs/why-hermes.md`](docs/why-hermes.md) — 为什么选择 Hermes、核心心智模型，以及与 Claude Code / Codex / OpenCode / Cursor 的详细对比
- [`docs/onboarding.md`](docs/onboarding.md) — 首次运行向导、供应商设置、本地模型服务器 Base URL 及安全重新运行指南
- [`docs/troubleshooting.md`](docs/troubleshooting.md) — 常见故障的诊断流程（例如“AIAgent 不可用”）

**使用与自定义**
- [`THEMES.md`](THEMES.md) — 主题+皮肤系统、自定义主题指南
- [`docs/workspace-git.md`](docs/workspace-git.md) — 工作区 Git 控制功能
- [`docs/EXTENSIONS.md`](docs/EXTENSIONS.md) — 管理员控制的 WebUI 扩展注入

**部署与运维**
- [`docs/remote-access.md`](docs/remote-access.md) — SSH 隧道、Tailscale 及手机访问（含社区 ARM64-Android 现场报告）
- [`docs/advanced-chat-setup.md`](docs/advanced-chat-setup.md) —— 可选的动态召回预填充与 Gateway 支持的浏览器聊天（适用于自托管部署）
- [`docs/docker.md`](docs/docker.md) — Docker Compose 设置、常见故障及 bind-mount 迁移指南
- [`docs/supervisor.md`](docs/supervisor.md) —— launchd、systemd、supervisord、runit 和 s6 进程管理器设置
- [`docs/wsl-autostart.md`](docs/wsl-autostart.md) —— WSL2 在 Windows 登录时自动启动
- [`docs/onboarding-agent-checklist.md`](docs/onboarding-agent-checklist.md) —— AI 助手辅助安装/重装的安全规则与通过/失败检查清单

**贡献与设计**
- [`CONTRIBUTING.md`](CONTRIBUTING.md) —— 贡献规范、PR 期望及本地验证流程
- [`ARCHITECTURE.md`](ARCHITECTURE.md) —— 系统设计、所有 API 端点及实现说明
- [`TESTING.md`](TESTING.md) —— 手动浏览器测试计划与自动化覆盖率参考
- [`DESIGN.md`](DESIGN.md) —— 设计令牌与“平静控制台”设计理念
- [`docs/UIUX-GUIDE.md`](docs/UIUX-GUIDE.md) —— 源自设计文档和视觉清单的 UI/UX 原则
- [`docs/CONTRACTS.md`](docs/CONTRACTS.md) —— 面向贡献者和智能体的项目契约/RFC/设计索引
- [`docs/rfcs/README.md`](docs/rfcs/README.md) —— 大型架构与耐久性提案的 RFC 索引

**发布历史与计划**
- [`CHANGELOG.md`](CHANGELOG.md) —— 各版本发布说明
- [`ROADMAP.md`](ROADMAP.md) —— 功能路线图与迭代历史
- [`SPRINTS.md`](SPRINTS.md) —— 面向未来的迭代计划及 CLI + Claude 对齐目标
- [`CONTRIBUTORS.md`](CONTRIBUTORS.md) —— 完整的社区贡献者名单

---

## 贡献者

Hermes WebUI 的构建离不开开源社区的帮助。每一个 PR——无论是直接合并、吸收进批量发布，还是从大型提案中挽救回来——都在塑造这个项目，我们感谢每一位付出时间贡献的人。

超过 **190 位贡献者**的代码已收录于发行标签中。完整且持续更新的致谢名单（包括所有提交过一两次 PR 的成员以及设计与架构工作的特别鸣谢）位于 [`CONTRIBUTORS.md`](CONTRIBUTORS.md)。以下是部分高频贡献者的快照：

### 核心贡献者（按 PR 数量统计，含吸收/批量发布工作）

| # | Contributor | PRs | First → latest release |
|---|---|---:|---|
| 1 | [@franksong2702](https://github.com/franksong2702) | 148 | `v0.49.3` → `v0.51.153` |
| 2 | [@Michaelyklam](https://github.com/Michaelyklam) | 117 | `v0.50.240` → `v0.51.139` |
| 3 | [@bergeouss](https://github.com/bergeouss) | 70 | `v0.48.0` → `v0.51.46` |
| 4 | [@ai-ag2026](https://github.com/ai-ag2026) | 67 | `v0.50.279` → `v0.51.190` |
| 5 | [@dso2ng](https://github.com/dso2ng) | 25 | `v0.50.227` → `v0.51.153` |
| 6 | [@AJV20](https://github.com/AJV20) | 24 | `v0.51.93` → `v0.51.188` |
| 7 | [@starship-s](https://github.com/starship-s) | 19 | `v0.50.123` → `v0.51.153` |
| 8 | [@jasonjcwu](https://github.com/jasonjcwu) | 16 | `v0.50.227` → `v0.51.132` |
| 9 | [@dobby-d-elf](https://github.com/dobby-d-elf) | 15 | `v0.51.38` → `v0.51.161` |
| 10 | [@Jordan-SkyLF](https://github.com/Jordan-SkyLF) | 12 | `v0.50.18` → `v0.51.66` |

详见 [`CONTRIBUTORS.md`](CONTRIBUTORS.md) 获取全部 194 位贡献者的完整排名列表，包括所有提交过一两次 PR 的成员以及设计与架构工作的特别鸣谢名单。

### notable 贡献（重要贡献）

**[@franksong2702](https://github.com/franksong2702)** —— 最活跃的外部贡献者（148 个 PR，`v0.49.3` → `v0.51.153`）
在所有外部贡献者中任期最长：会话标题保护 (#301)、面包屑工作区导航 (#302)、内嵌工作区终端 (#1099)、worktree 支持的会话创建 (#2053)、引导文档 (#2052)、底部编辑区容器查询、流式传输侧边栏豁免 (#1327)、会话旁路修复、cron 输出保留 (#1295)、配置文件默认工作区持久化、手动 `/compress` 异步启动/状态端点 (#2128)、worktree 状态展示 (#2109) + 生命周期伞形 #2057 的安全移除 (#2156)、会话后处理去重 (#2166)、原生 WebUI 快速路径 (#2170)、尾窗响应修剪 (#2171)、过期流保护扩展 (#2158)、CSP 报告收集器 (#2160)，以及在移动端/响应式、会话侧边栏和工作区状态机方面的持续打磨。

**[@Michaelyklam](https://github.com/Michaelyklam)** —— 近期版本最活跃贡献者（117 个 PR，`v0.50.240` → `v0.51.139`）
生产环境 Docker 加固 (#1921，移除可提权暂存用户)、配置文件作用域技能端点 (#1903)、在配置文件作用域的 HERMES_HOME 下解析网关 PID (#1901)、感知配置文件的 AIAgent 缓存 (#1898/#1904)、反斜杠 LaTeX 分隔符 (#1848)、Codex 配额错误展示 (#1770)、Shell 路由 HTML 503 (#1836)、过期看板客户端恢复 (#1828)、上下文自动压缩 Toast 生命周期 (#1988)、`/goal` 命令 (#1866)、看板详情视图滚动 (#1916)、CLI 会话工具元数据保留 (#1778)、繁体中文看板区域设置回填 (#1979)、v0.51.51 移动端洞察分桶/布局 (#2120/#2121)、Hermes 运行适配器 RFC (#2105 for #1925)、fork-from-here 绝对索引 (#2198 for #2184)、opencode-go 自定义供应商重叠路由 (#2204 for #1894)。

**[@bergeouss](https://github.com/bergeouss)** —— 供应商管理界面 + Docker 加固（70 个 PR，`v0.48.0` → `v0.51.46`）
提供从设置中添加/编辑自定义供应商的界面、OAuth 供应商状态检测 (#1552)、双容器 Docker 设置、配置文件隔离加固（每配置文件 `.env` 密钥）、用户触摸“设置 -> 供应商”时看到的大部分功能、Finder 中显示上下文菜单 (#1551)、网关状态卡片 (#1552)、自动将会话分配给活动项目过滤器 (#1550)、“更新横幅中的‘新功能’链接 (#1549)、OpenRouter 免费层实时获取 (#1548)、凭证池 401 自愈 (#1553)、模型选择器中的内联供应商标签 + 分组模型计数 (#1644)。

**[@ai-ag2026](https://github.com/ai-ag2026)** —— 会话恢复 + 审计基础设施（67 个 PR，`v0.50.279` → `v0.51.190`）
自主 AI 贡献者（由 Hermes Agent 驱动），专注于耐久性：`state.db` 支持的旁路对账 (#2041)、启动时孤儿 `.json.bak` 恢复 (#2035)、只读会话恢复审计端点 (#2036, #2040)、`/health` 中的活动运行生命周期 (#2039)、`docs/rfcs/turn-journal.md` 的防崩溃轮次日志 RFC (#2042)、仅追加轮次日志辅助函数 (#2059)、生命周期事件层 (#2062)、`Content-Security-Policy-Report-Only` 头 (#2084)、每 cron Toast 切换 (#2100)、fork 会话压缩谱系隔离 (#2014)。

**[@dso2ng](https://github.com/dso2ng)** —— 会话谱系 + 诊断（25 个 PR，`v0.50.227` → `v0.51.153`）
用于有界会话图诊断的 `/api/session/lineage-report/<sid>` 端点 (#2012)、过期 Mermaid 渲染错误清理 (#1337)、`session_source="fork"` 延续链隔离 (#2063)、侧边栏徽章展开时的懒加载谱系报告获取 (#2130)，以及在会话加载方面的大量前端可靠性修复。

**[@jasonjcwu](https://github.com/jasonjcwu)** —— 编辑区 + 记录打磨（16 个 PR，`v0.50.227` → `v0.51.132`）
通过点击活动栏折叠侧边栏 (#2054，合并 #1884 + #1924)、编辑区标签灯箱 (#1758)、工具密集型首轮标题修复、会话切换期间的静默压缩状态 (#2185)、并发发送丢失修复 (#2186)、记录内转向消息徽章 (#2187)，以及一系列前端打磨修复。

**[@Jordan-SkyLF](https://github.com/Jordan-SkyLF)** —— 实时流式传输 + UX 打磨（12 个 PR，`v0.50.18` → `v0.51.66`）
工作区回退解决的首个迭代、实时推理卡片 (#366, #367, #394–#397)，以及近期密集更新：供应商配额卡上的手动“刷新用量”按钮 (#2150)、已取消轮次状态分类 (#2151)、Firefox 侧边栏滚动稳定化 (#2200)、早期暂定会话标题 (#2202)、目标感知的“新功能”更新横幅链接 (#2207)，以及设置中 MCP 工具溢出修复 (#2210)。

**[@aronprins](https://github.com/aronprins)** —— `v0.50.0` UI 重构（PR #242，附带 9 个跟进 PR）
该项目单次最大贡献：全面 UI 重新设计，将模型/配置/工作区控件移至底部编辑区，用 Hermes 控制中心（标签页模态框）替换齿轮图标设置面板，以内联编辑区状态取代活动栏，重新设计带 `⋯` 操作下拉菜单的会话列表，并添加工作区面板状态机。此外还包括聊天记录重设计 (#587)、侧边栏精简 (#584)、三列布局重构 (#899)、亮/暗主题+强调色皮肤 (#627)，以及共享 `confirm()`/`prompt()` 对话框替换（PR #251 从 #242 提取）。

**[@iRonin](https://github.com/iRonin)** —— 安全加固迭代（PRs #196–#204）
六次连续且专注的安全 PR：会话内存泄漏修复（过期 Token 修剪）、CSP + Permissions-Policy 头、30 秒慢客户端连接超时、通过环境变量支持可选 HTTPS/TLS、自更新的远程分支跟踪修复，以及文件浏览器 API 中的 CLI 会话支持。这种专注的高质量安全工作让自托管工具值得信赖。

**[@lucasrc](https://github.com/lucasrc)** —— 认证加固三部曲（PRs #2191, #2192, #2193）
三项协调一致的安全 PR，均收录于 v0.51.57：带 PBKDF2 密钥分离的线程安全登录速率限制器、设置保存时的密码哈希缓存失效，以及完整的 64 字符 HMAC-SHA256 会话签名（含向后兼容迁移桥接）。这种清晰分解的安全工作可拆分为三个独立部分进行审查。

**[@LumenYoung](https://github.com/LumenYoung)** —— 流式传输热路径正确性（8 个 PR，`v0.51.47` → `v0.51.99`）
原始过期流回写保护 (#2136——后续两个版本扩展的 Bug 类别)、网关状态存活空值分类 (#2075)、压缩横幅锚点对齐 (#2182)，以及压缩完成时上下文进度环自动刷新 (#2188)。每个 PR 都在代码库中最脆弱的子系统之一中进行了精准的手术式修复。

**[@dobby-d-elf](https://github.com/dobby-d-elf)** —— 前端可靠性 + 动效打磨（15 个 PR，`v0.51.38` → `v0.51.161`）
删除目录时的工作区回退 (#2138)、iPhone PWA 底部滚动修复 (#2143)、新的“活动：X 个工具”编辑区闪烁动画 (#2203)，以及后续动效调优 (#2212)。

**[@JKJameson](https://github.com/JKJameson)** —— 编辑区 + 会话打磨（10 个 PR）
逐会话持久化编辑区草稿 (#1956)，以及在编辑区和会话侧边栏的大量持续打磨。

**[@gabogabucho](https://github.com/gabogabucho)** —— 西班牙语区域设置 + 引导向导
完整的西班牙语 (`es`) 区域设置，覆盖所有 UI 字符串，以及一次性引导向导，指导新用户完成首次启动时的供应商设置。

**[@deboste](https://github.com/deboste)** —— 反向代理认证 + 移动端响应式布局（PRs #3, #4, #5）
社区最早的三个 PR：修复反向代理设置的 EventSource/fetch 以使用 URL 来源，更正配置中的模型供应商路由，并添加带 dvh 视口修复的移动端响应式布局。早期基础工作。

**[@indigokarasu](https://github.com/indigokarasu)** —— 视觉重设计提案（PR #213）
纯 CSS 的全 UI 重设计——完善的设计令牌、替代表情符号标签页的图标轨道侧边栏、一致的表单卡片、面包屑导航，以及作为自定义属性的 7 个内置主题。该 PR 未直接合并，但塑造了 v0.50.0 中发布的设计语言和主题架构。

**[@zenc-cp](https://github.com/zenc-cp)** —— ReAct 循环的防幻觉保护（PR #133）
三层方法（临时防幻觉提示、实时 Token 过滤、会话历史清理），流式传输管道至今仍在使用。

**[@Hinotoi-agent](https://github.com/Hinotoi-agent)** —— 配置+会话安全（PRs #351, #2048）
配置文件 `.env` 密钥隔离修复（PR #351），防止不同配置间的 API Key 泄露；会话导入工作区验证（PR #2048），阻止针对 `/` 的构造 JSON 文件读取。

**[@Sanjays2402](https://github.com/Sanjays2402)** —— 无限滚动+Start-jump 竞态修复（PR #1949）
生成 Token + 互斥锁对，修复 v0.51.30 中无限滚动预取与 Start-jump 的 `_ensureAllMessagesLoaded` 之间的竞态。天真的同标志检查方法（在 #1942 和 #1962 中提出）对于等待后竞态无效——Sanjays2402 的修复是正确的方案。

**[@fxd-jason](https://github.com/fxd-jason)** —— 通过 SSE 实现实时审批+澄清（PRs #1350, #1355）
将 1.5 秒 HTTP 轮询替换为 SSE 长连接（用于审批和澄清），将延迟从最高 1.5 秒降至近乎即时。完美处理了所有正确性细节（原子订阅+快照、锁内通知、队列头负载、尾部事件重发）。

**[@happy5318](https://github.com/happy5318)** —— 自定义供应商模型去重（PR #1947）
修复了不同命名的自定义供应商中的相同模型在选择器中被静默去重的问题，Opus 捕获到原始测试中需要补充的竞态。

**[@NocGeek](https://github.com/NocGeek)** —— 流式传输滚动+手动 Cron 输出持久化（7 个 PR）
工具/队列卡片插入时的流式传输滚动视口稳定性 (#1360)，手动 Cron 运行输出和元数据持久化 (#1372，从搁置的 #1352 拆分)。

**[@DavidSchuchert](https://github.com/DavidSchuchert)** —— 德语翻译（PR #190）
完整的德语区域设置 (`de`)，覆盖所有 UI 字符串、设置标签、命令和系统消息——并压力测试了国际化系统，暴露出多个尚未翻译的元素并在同一 PR 中修复。

**[@Bobby9228](https://github.com/Bobby9228)** —— 移动端配置文件按钮（PR #265）
在移动导航流程中添加配置文件入口，使手机端可访问配置切换。

**[@kevin-ho](https://github.com/kevin-ho)** —— OLED 主题（PR #168）
第 7 个内置主题：纯黑背景搭配暖色强调，优化以降低烧屏风险。

**[@andrewy-wizard](https://github.com/andrewy-wizard)** —— 中文本地化（PR #177）
初始简体中文 (`zh`) 区域设置。首批非英语区域设置之一。

**[@DelightRun](https://github.com/DelightRun)** —— WebUI 会话的 `session_search` 修复（PR #356）
追踪到流式传输路径中缺失的 `SessionDB` 注入，该问题无声地破坏了所有 WebUI 会话的工具功能。

**[@lawrencel1ng](https://github.com/lawrencel1ng)** —— Bandit 安全修复（PR #354）
系统性 Bandit 扫描修复：`urlopen` 前的 URL 方案验证、MD5 `usedforsecurity=False`，以及将 40+ 个裸 `except: pass` 块替换为适当的日志记录。

**[@shaoxianbilly](https://github.com/shaoxianbilly)** —— Unicode 文件名下载（PR #378）
符合 RFC 5987 的 `Content-Disposition` 及 `filename*=UTF-8''...` 编码，确保非 ASCII 文件名下载时不崩溃。

**[@lx3133584](https://github.com/lx3133584)** —— 反向代理的 CSRF 修复（PR #360）
解决了任何在 Nginx Proxy Manager 或其他非 80/443 端口后托管的真实世界阻塞问题。

**[@betamod](https://github.com/betamod)** —— 安全审计（PR #171）
全面的 CSRF/SSRF/XSS/环境竞态审计，收录于 v0.39.0。

**[@TaraTheStar](https://github.com/TaraTheStar)** —— 机器人名称+思考块+登录重构（PRs #132, #176, #181）
可配置的助手显示名称、思考/推理块展示，以及登录页面重构。

---

## 仓库

```
git@github.com:nesquena/hermes-webui.git
```