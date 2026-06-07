<div align="center">
  <img src="public/logo.svg" alt="CloudCLI UI" width="64" height="64">
  <h1>Cloud CLI（又名 Claude Code UI）</h1>
  <p>A desktop and mobile UI for <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://docs.cursor.com/en/cli/overview">Cursor CLI</a>, <a href="https://developers.openai.com/codex">Codex</a>, and <a href="https://geminicli.com/">Gemini-CLI</a>.<br>Use it locally or remotely to view your active projects and sessions from everywhere.</p>
</div>

<p align="center">
  <a href="https://cloudcli.ai">CloudCLI Cloud</a> · <a href="https://cloudcli.ai/docs">文档</a> · <a href="https://discord.gg/buxwujPNRE">Discord</a> · <a href="https://github.com/siteboon/claudecodeui/issues">问题反馈</a> · <a href="CONTRIBUTING.md">参与贡献</a>
</p>

<p align="center">
  <a href="https://cloudcli.ai"><img src="https://img.shields.io/badge/☁️_CloudCLI_Cloud-Try_Now-0066FF?style=for-the-badge" alt="CloudCLI Cloud"></a>
  <a href="https://discord.gg/buxwujPNRE"><img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord"></a>
  <br><br>
  <a href="https://trendshift.io/repositories/15586" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15586" alt="siteboon%2Fclaudecodeui | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<div align="right"><i><b>英文（English）</b> · <a href="./README.ru.md">Русский</a> · <a href="./README.de.md">Deutsch</a> · <a href="./README.ko.md">한국어</a> · <a href="./README.zh-CN.md">中文</a> · <a href="./README.ja.md">日本語</a> · <a href="./README.tr.md">Türkçe</a></i></div>

---

## 截图（Screenshots）

<div align="center">
  
<table>
<tr>
<td align="center">
<h3>桌面视图</h3>
<img src="public/screenshots/desktop-main.png" alt="Desktop Interface" width="400">
<br>
<em>显示项目概览和聊天功能的主界面</em>
</td>
<td align="center">
<h3>移动端体验</h3>
<img src="public/screenshots/mobile-chat.png" alt="Mobile Interface" width="250">
<br>
<em>支持触控导航的响应式移动端设计</em>
</td>
</tr>
<tr>
<td align="center" colspan="2">
<h3>CLI 选择</h3>
<img src="public/screenshots/cli-selection.png" alt="CLI Selection" width="400">
<br>
<em>在 Claude Code、Gemini、Cursor CLI 和 Codex 之间进行选择</em>
</td>
</tr>
</table>



</div>

## 功能特性（Features）

- **响应式设计** — 完美适配桌面端、平板和移动端，让你也能通过手机使用 Agent（智能体） 
- **交互式聊天界面** — 内置聊天功能，与 Agent 无缝沟通
- **集成 Shell 终端** — 通过内置 Shell 直接访问 Agent 的 CLI（命令行接口）
- **文件管理器** — 交互式文件树，支持语法高亮和实时编辑
- **Git 管理** — 查看、暂存并提交更改。还支持切换分支 
- **会话管理** — 恢复对话，管理多个会话并追踪历史记录
- **插件系统** — 通过自定义插件扩展 CloudCLI 功能——添加新标签页、后端服务和集成。[构建你自己的插件 →](https://github.com/cloudcli-ai/cloudcli-plugin-starter)
- **TaskMaster AI 集成** *（可选）* — 借助 AI 驱动的任务规划、PRD（产品需求文档）解析和工作流自动化，实现高级项目管理
- **模型兼容性** — 兼容 Claude、GPT 和 Gemini 系列模型（完整支持列表见 [`public/modelConstants.js`](public/modelConstants.js)）


## 快速开始（Quick Start）

### CloudCLI Cloud（推荐）

最快捷的入门方式——无需本地配置。获取完全托管的容器化开发环境，可通过网页、移动应用、API 或你喜欢的 IDE 访问。

**[开始使用 CloudCLI Cloud](https://cloudcli.ai)**


### 自托管（开源）（Self-Hosted (Open source)）

#### npm

通过 **npx** 即时体验 CloudCLI UI（需要 **Node.js** v22+ 或更高版本）：

```
npx @cloudcli-ai/cloudcli
```

如需长期使用，可全局安装：

```
npm install -g @cloudcli-ai/cloudcli
cloudcli
```

打开 `http://localhost:3001` —— 系统会自动发现你现有的所有会话。

访问 **[文档 →](https://cloudcli.ai/docs)** 查看完整配置选项、PM2 部署、远程服务器设置等更多内容。

#### Docker 沙箱（实验性）（Docker Sandboxes (Experimental)）

在具有虚拟机监控程序级隔离的独立沙箱中运行 Agent。默认启动 Claude Code。需要安装 [`sbx` CLI](https://docs.docker.com/ai/sandboxes/get-started/)。

```
npx @cloudcli-ai/cloudcli@latest sandbox ~/my-project
```

支持 Claude Code、Codex 和 Gemini CLI。设置与高级选项请参阅沙箱文档 [`docker/`](docker/)。


---

## 哪种方案适合你？（Which option is right for you?）

CloudCLI UI 是驱动 CloudCLI Cloud 的开源界面层。你可以将其自托管在自己的机器上，或在 Docker 沙箱中运行以实现隔离，也可以直接使用 CloudCLI Cloud 获取完全托管的环境。

| | Self-Hosted (npm) | Self-Hosted (Docker Sandbox) *(Experimental)* | CloudCLI Cloud |
|---|---|---|---|
| **适用场景**（Best for） | 在本地机器上运行 Agent 会话 | 通过 Web/移动端 IDE 隔离运行 Agent | 希望将 Agent 部署在云端的团队 |
| **访问方式**（How you access it） | 浏览器访问 `[你的IP]:端口` | 浏览器访问 `localhost:端口` | 浏览器、任意 IDE、REST API、n8n |
| **配置要求**（Setup） | `npx @cloudcli-ai/cloudcli` | `npx @cloudcli-ai/cloudcli@latest sandbox ~/project` | 无需配置 |
| **隔离级别**（Isolation） | 运行于宿主机 | 虚拟机监控程序级沙箱（微虚拟机 / microVM） | 完整云端隔离 |
| **设备需保持开机**（Machine needs to stay on） | 是 | 是 | 否 |
| **移动端访问**（Mobile access） | 局域网内任意浏览器 | 局域网内任意浏览器 | 任意设备，原生应用开发中 |
| **支持的 Agent**（Agents supported） | Claude Code, Cursor CLI, Codex, Gemini CLI | Claude Code, Codex, Gemini CLI | Claude Code, Cursor CLI, Codex, Gemini CLI |
| **文件管理器与 Git**（File explorer and Git） | 支持 | 支持 | 支持 |
| **MCP 配置**（MCP configuration） | 同步自 `~/.claude` | 通过界面管理 | 通过界面管理 |
| **REST API**（REST API） | 支持 | 支持 | 支持 |
| **团队协作共享**（Team sharing） | 不支持 | 不支持 | 支持 |
| **平台费用**（Platform cost） | 免费，开源 | 免费，开源 | 起价 $7/月 |

> **注意**：所有方案均使用你自己的 AI 订阅（如 Claude、Cursor 等）——CloudCLI 仅提供运行环境，不包含 AI 服务。

---

## 安全与工具配置（Security & Tools Configuration）

**🔒 重要提示**：所有 Claude Code 工具默认均为**禁用状态**。此举可防止潜在的危险操作自动执行。

### 启用工具（Enabling Tools）

如需使用 Claude Code 的全部功能，需手动启用相关工具：

1. **打开工具设置** - 点击侧边栏的齿轮图标
2. **按需启用** - 仅开启你需要的工具
3. **应用设置** - 你的偏好将保存在本地

<div align="center">

![Tools Settings Modal](public/screenshots/tools-modal.png)
*工具设置界面 —— 仅开启所需功能*

</div>

**推荐做法**：先启用基础工具，后续按需添加。你随时可以在此处调整这些设置。

---

## 插件系统（Plugins）

CloudCLI 提供了一套插件系统，允许你添加带有独立前端界面和可选 Node.js 后端的自定义标签页。你可以直接在 **设置 > 插件** 中从 Git 仓库安装插件，或自行开发。

### 可用插件（Available Plugins）

| Plugin | Description |
|---|---|
| **[Project Stats](https://github.com/cloudcli-ai/cloudcli-plugin-starter)** | 显示当前项目的文件数量、代码行数、文件类型分布、最大文件及最近修改的文件 |
| **[Web Terminal](https://github.com/cloudcli-ai/cloudcli-plugin-terminal)** | 支持多标签页的完整 xterm.js 终端 |
| **[CloudCLI Scheduler](https://github.com/grostim/cloudcli-cron)** | 创建工作区级别的定时提示词，并通过本地 CLI（如 Codex、Claude Code 或 Gemini CLI）执行 |

### 自行开发（Build Your Own）

**[插件 starter 模板 →](https://github.com/cloudcli-ai/cloudcli-plugin-starter)** —— Fork 此仓库即可创建你自己的插件。其中包含一个完整示例，涵盖前端渲染、实时上下文更新以及与后端服务器的 RPC 通信。

**[插件文档 →](https://cloudcli.ai/docs/plugin-overview)** —— 关于插件 API、清单格式、安全模型等的完整指南。

---
## 常见问题（FAQ）

<details>
<summary>这与 Claude Code Remote Control（远程控制台）有什么区别？</summary>

Claude Code Remote Control 允许你向已在本地终端运行的会话发送消息。你的设备必须保持开机，终端需持续打开，且若约 10 分钟无网络连接，会话将会超时断开。

CloudCLI UI 和 CloudCLI Cloud 是对 Claude Code 的扩展，而非独立并列的工具——你的 MCP 服务器、权限、设置与会话均与 Claude Code 原生使用的一致。不会重复生成或单独管理任何内容。

具体体现在以下方面：

- **管理所有会话，而非仅限一个** —— CloudCLI UI 会自动发现你 `~/.claude` 文件夹中的所有会话。Remote Control 仅暴露当前活跃的一个会话以适配 Claude 移动端应用。
- **你的设置即生效** —— 在 CloudCLI UI 中修改的 MCP 服务器、工具权限和项目配置会直接写入你的 Claude Code 配置文件中并立即生效，反之亦然。
- **支持更多 Agent** —— 兼容 Claude Code、Cursor CLI、Codex 和 Gemini CLI，不仅限于 Claude Code。
- **完整界面，而非仅聊天窗口** —— 内置文件管理器、Git 集成、MCP 管理和 Shell 终端等功能。
- **CloudCLI Cloud 运行在云端** —— 合上笔记本，Agent 依然持续运行。无需专人看守终端，也无需保持设备开机。

</details>

<details>
<summary>我需要单独购买 AI 订阅吗？</summary>

是的。CloudCLI 仅提供运行环境，不提供 AI 服务。你需要自备 Claude、Cursor、Codex 或 Gemini 的订阅账号。在此基础上，CloudCLI Cloud 托管环境的起价为 $7/月。

</details>

<details>
<summary>我能在手机上使用 CloudCLI UI 吗？</summary>

可以。自托管方案下，在你的机器上运行服务器，并在局域网内任意浏览器中访问 `[你的IP]:端口` 即可。使用 CloudCLI Cloud 时，可在任意设备上直接打开——无需配置 VPN、端口转发或额外设置。原生移动端应用也在开发中。

</details>

<details>
<summary>我在界面中的更改会影响本地 Claude Code 的设置吗？</summary>

是的，针对自托管方案。CloudCLI UI 与 Claude Code 原生配置共享同一个 `~/.claude` 文件。通过界面添加的 MCP 服务器会立即同步至 Claude Code，反之亦然。

</details>

---

## 社区与支持（Community & Support）

- **[文档](https://cloudcli.ai/docs)** —— 安装、配置、功能说明与故障排除
- **[Discord](https://discord.gg/buxwujPNRE)** —— 获取帮助并与其他用户交流
- **[GitHub Issues](https://github.com/siteboon/claudecodeui/issues)** —— 提交 Bug 报告和功能建议
- **[贡献指南](CONTRIBUTING.md)** —— 如何参与项目开发

## 许可证（License）

GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later) — see [LICENSE](LICENSE) for the full text, including additional terms under Section 7.

本项目基于 AGPL-3.0-or-later 许可证开源免费使用、修改和分发。若你修改了本软件并将其作为网络服务运行，则必须向该服务的用户提供你的修改版源代码。

CloudCLI UI - (https://cloudcli.ai)。

## 致谢（Acknowledgments）

### 核心技术栈（Built With）
- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** - Anthropic 官方 CLI
- **[Cursor CLI](https://docs.cursor.com/en/cli/overview)** - Cursor 官方 CLI
- **[Codex](https://developers.openai.com/codex)** - OpenAI Codex
- **[Gemini-CLI](https://geminicli.com/)** - Google Gemini CLI
- **[React](https://react.dev/)** - 用户界面库
- **[Vite](https://vitejs.dev/)** - 快速构建工具与开发服务器
- **[Tailwind CSS](https://tailwindcss.com/)** - 实用优先的 CSS 框架
- **[CodeMirror](https://codemirror.net/)** - 高级代码编辑器
- **[TaskMaster AI](https://github.com/eyaltoledano/claude-task-master)** *（可选）* - AI 驱动的项目管理与任务规划


### 赞助商（Sponsors）
- [Siteboon - AI 驱动的网站建设工具](https://siteboon.ai)
---

<div align="center">
  <strong>专为 Claude Code、Cursor 和 Codex 社区精心打造。</strong>
</div>