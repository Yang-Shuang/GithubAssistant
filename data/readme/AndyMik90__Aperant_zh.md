# Aperant（原名 Auto Claude）

**为你自主规划、构建和验证软件的自主多代理编码框架。**

![Aperant Kanban Board](.github/assets/Auto-Claude-Kanban.png)

[![License](https://img.shields.io/badge/license-AGPL--3.0-green?style=flat-square)](./agpl-3.0.txt)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/KCXaPBr4Dj)
[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@AndreMikalsen)
[![CI](https://img.shields.io/github/actions/workflow/status/AndyMik90/Auto-Claude/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/AndyMik90/Auto-Claude/actions)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/hesreallyhim/awesome-claude-code)

---

## 下载

### 稳定版发布

<!-- STABLE_VERSION_BADGE -->
[![Stable](https://img.shields.io/badge/stable-2.7.6-blue?style=flat-square)](https://github.com/AndyMik90/Auto-Claude/releases/tag/v2.7.6)
<!-- STABLE_VERSION_BADGE_END -->

<!-- STABLE_DOWNLOADS -->
| 平台 | 下载 |
|----------|----------|
| **Windows** | [Auto-Claude-2.7.6-win32-x64.exe](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.6/Auto-Claude-2.7.6-win32-x64.exe) |
| **macOS (Apple Silicon)** | [Auto-Claude-2.7.6-darwin-arm64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.6/Auto-Claude-2.7.6-darwin-arm64.dmg) |
| **macOS (Intel)** | [Auto-Claude-2.7.6-darwin-x64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.6/Auto-Claude-2.7.6-darwin-x64.dmg) |
| **Linux** | [Auto-Claude-2.7.6-linux-x86_64.AppImage](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.6/Auto-Claude-2.7.6-linux-x86_64.AppImage) |
| **Linux (Debian)** | [Auto-Claude-2.7.6-linux-amd64.deb](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.6/Auto-Claude-2.7.6-linux-amd64.deb) |
| **Linux (Flatpak)** | [Auto-Claude-2.7.6-linux-x86_64.flatpak](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.6/Auto-Claude-2.7.6-linux-x86_64.flatpak) |
<!-- STABLE_DOWNLOADS_END -->

### 测试版（Beta）发布

> ⚠️ Beta 版本可能包含 Bug 和破坏性更改。[查看所有发布版本](https://github.com/AndyMik90/Auto-Claude/releases)

<!-- BETA_VERSION_BADGE -->
[![Beta](https://img.shields.io/badge/beta-2.8.0--beta.6-orange?style=flat-square)](https://github.com/AndyMik90/Auto-Claude/releases/tag/v2.8.0-beta.6)
<!-- BETA_VERSION_BADGE_END -->

<!-- BETA_DOWNLOADS -->
| 平台 | 下载 |
|----------|----------|
| **Windows** | [Aperant-2.8.0-beta.5-win32-x64.exe](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.8.0-beta.5/Aperant-2.8.0-beta.5-win32-x64.exe) |
| **macOS (Apple Silicon)** | [Aperant-2.8.0-beta.5-darwin-arm64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.8.0-beta.5/Aperant-2.8.0-beta.5-darwin-arm64.dmg) |
| **macOS (Intel)** | [Aperant-2.8.0-beta.5-darwin-x64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.8.0-beta.5/Aperant-2.8.0-beta.5-darwin-x64.dmg) |
| **Linux** | [Aperant-2.8.0-beta.5-linux-x86_64.AppImage](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.8.0-beta.5/Aperant-2.8.0-beta.5-linux-x86_64.AppImage) |
| **Linux (Debian)** | [Aperant-2.8.0-beta.5-linux-amd64.deb](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.8.0-beta.5/Aperant-2.8.0-beta.5-linux-amd64.deb) |
| **Linux (Flatpak)** | [Aperant-2.8.0-beta.5-linux-x86_64.flatpak](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.8.0-beta.5/Aperant-2.8.0-beta.5-linux-x86_64.flatpak) |
<!-- BETA_DOWNLOADS_END -->

> 所有发布版本均包含 SHA256 校验和及 VirusTotal 扫描结果，以供安全验证。

---

## 环境要求

- **Claude Pro/Max 订阅** - [在此获取](https://claude.ai/upgrade)
- **Claude Code CLI** - `npm install -g @anthropic-ai/claude-code`
- **Git 仓库** - 你的项目必须已初始化为 Git 仓库

---

## 快速开始

1. **下载并安装**适用于你平台的客户端应用
2. **打开你的项目** - 选择一个 Git 仓库文件夹
3. **连接 Claude** - 应用将引导你完成 OAuth 设置
4. **创建任务** - 描述你想构建的内容
5. **观看运行过程** - 代理将自主进行规划、编码和验证

---

## 功能特性

| 功能 | 说明 |
|---------|-------------|
| **自主任务** | 描述你的目标；代理负责规划、实现和验证 |
| **并行执行** | 最多支持 12 个代理终端，同时运行多个构建任务 |
| **隔离工作区** | 所有更改均在 Git worktree 中进行；你的主分支保持安全 |
| **自验证质量保证（QA）** | 内置质量检查循环，在审查前自动发现问题 |
| **AI 驱动合并** | 集成回主分支时自动解决冲突 |
| **记忆层** | 代理可在跨会话中保留洞察信息，实现更智能的构建 |
| **GitHub/GitLab 集成** | 导入 Issue、使用 AI 调查问题并创建合并请求（Merge Request） |
| **Linear 集成** | 与 Linear 同步任务，以便团队跟踪进度 |
| **跨平台支持** | 提供适用于 Windows、macOS 和 Linux 的原生桌面应用 |
| **自动更新** - 新版本发布时，应用会自动更新 |

---

## 界面说明

### 看板（Kanban）界面
可视化任务管理，覆盖从规划到完成的全流程。创建任务并实时监控代理进度。

### 代理终端
搭载 AI 的终端，支持一键注入任务上下文。可启动多个代理进行并行工作。

![Agent Terminals](.github/assets/Auto-Claude-Agents-terminals.png)

### 路线图（Roadmap）
借助 AI 辅助功能规划，结合竞品分析与目标受众定位。

![Roadmap](.github/assets/Auto-Claude-roadmap.png)

### 其他功能特性
- **洞察（Insights）** - 用于探索代码库的聊天界面
- **构思（Ideation）** - 发现改进建议、性能问题与安全漏洞
- **更新日志（Changelog）** - 根据已完成的任务自动生成发布说明

---

## 项目结构

```
Aperant/
├── apps/
│   └── desktop/     # Electron desktop application (TypeScript AI agent layer + UI)
├── guides/          # Additional documentation
└── scripts/         # Build utilities
```

---

## 开发指南

想要从源码构建或参与贡献？请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 获取完整的开发环境配置指南。

如需针对 Linux 的特定构建（Flatpak、AppImage），请参阅 [guides/linux.md](guides/linux.md)。

---

## 安全机制

Aperant 采用三层安全模型：

1. **操作系统沙箱（OS Sandbox）** - Bash 命令在隔离环境中运行
2. **文件系统限制** - 操作仅限于项目目录范围内
3. **动态命令白名单** - 仅允许经过批准的项目命令（基于检测到的项目技术栈）

所有发布版本均满足以下安全标准：
- 发布前经 VirusTotal 扫描
- 附带 SHA256 校验和以供验证
- 在适用情况下进行代码签名（如 macOS）

---

## 可用脚本

| 命令 | 说明 |
|---------|-------------|
| `npm run install:all` | 安装所有依赖项 |
| `npm start` | 构建并运行桌面应用 |
| `npm run dev` | 以开发模式运行（支持热重载） |
| `npm run package` | 打包当前平台版本 |
| `npm run package:mac` | 打包 macOS 版本 |
| `npm run package:win` | 打包 Windows 版本 |
| `npm run package:linux` | 打包 Linux 版本 |
| `npm run package:flatpak` | 打包为 Flatpak 格式（详见 [guides/linux.md](guides/linux.md)） |
| `npm run lint` | 运行代码检查工具 |
| `npm test` | 运行前端测试 |

---

## 贡献指南

我们欢迎你的贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解：
- 开发环境配置指南
- 代码风格规范
- 测试要求
- 拉取请求（Pull Request）流程

---

## 社区交流

- **Discord** - [加入我们的社区](https://discord.gg/KCXaPBr4Dj)
- **Issue 反馈** - [报告 Bug 或请求新功能](https://github.com/AndyMik90/Auto-Claude/issues)
- **讨论区** - [提问与交流](https://github.com/AndyMik90/Auto-Claude/discussions)

---

## 开源协议

**AGPL-3.0** - GNU Affero 通用公共许可证第三版（GNU Affero General Public License v3.0）

Aperant 可免费使用。如果你修改并分发它，或将其作为服务运行，你的代码也必须根据 AGPL-3.0 开源。

针对闭源商用场景提供商业授权许可。

---

## 星标历史

[![GitHub Repo stars](https://img.shields.io/github/stars/AndyMik90/Auto-Claude?style=social)](https://github.com/AndyMik90/Auto-Claude/stargazers)

[![Star History Chart](https://api.star-history.com/svg?repos=AndyMik90/Auto-Claude&type=Date)](https://star-history.com/#AndyMik90/Auto-Claude&Date)