<div align="center">
  <img src="src-tauri/icons/icon.png" alt="opcode Logo" width="120" height="120">

  <h1>opcode</h1>
  
  <p>
    <strong>Claude Code 的强大图形界面应用与工具包</strong>
  </p>
  <p>
    <strong>创建自定义智能体、管理交互式 Claude Code 会话、运行安全的后台智能体，以及更多功能。</strong>
  </p>
  
  <p>
    <a href="#features"><img src="https://img.shields.io/badge/Features-✨-blue?style=for-the-badge" alt="Features"></a>
    <a href="#installation"><img src="https://img.shields.io/badge/Install-🚀-green?style=for-the-badge" alt="Installation"></a>
    <a href="#usage"><img src="https://img.shields.io/badge/Usage-📖-purple?style=for-the-badge" alt="Usage"></a>
    <a href="#development"><img src="https://img.shields.io/badge/Develop-🛠️-orange?style=for-the-badge" alt="Development"></a>
    <a href="https://discord.com/invite/KYwhHVzUsY"><img src="https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  </p>
</div>

![457013521-6133a738-d0cb-4d3e-8746-c6768c82672c](https://github.com/user-attachments/assets/a028de9e-d881-44d8-bae5-7326ab3558b9)



https://github.com/user-attachments/assets/6bceea0f-60b6-4c3e-a745-b891de00b8d0



> [!TIP]
> **⭐ 给仓库点星并关注 X (原 Twitter) 上的 [@getAsterisk](https://x.com/getAsterisk)，即可抢先体验 `asteria-swe-v0`**。

> [!NOTE]
> 本项目与 Anthropic 无关，未获其认可或赞助。Claude 是 Anthropic, PBC. 的商标。这是一个使用 Claude 的独立开发者项目。

## 🌟 概述

**opcode** 是一款强大的桌面应用程序，彻底改变了你与 Claude Code 的交互方式。基于 Tauri 2 构建，它提供了一个美观的图形界面（GUI），用于管理你的 Claude Code 会话、创建自定义智能体、跟踪使用情况等。

可以将 opcode 视为你驾驭 Claude Code 的指挥中心——它弥合了命令行工具与可视化体验之间的差距，让 AI 辅助开发更加直观高效。

## 📋 目录

- [🌟 概述](#-概述)
- [✨ 功能特性](#-功能特性)
  - [🗂️ 项目与会话管理](#️-项目与会话管理)
  - [🤖 CC Agents](#-cc-agents)
  
  - [📊 使用分析仪表盘](#-使用分析仪表盘)
  - [🔌 MCP 服务器管理](#-mcp-服务器管理)
  - [⏰ 时间线与检查点](#-时间线与检查点)
  - [📝 CLAUDE.md 管理](#-claudemd-管理)
- [📖 使用方法](#-使用方法)
  - [快速开始](#快速开始)
  - [管理项目](#管理项目)
  - [创建智能体](#创建智能体)
  - [跟踪使用情况](#跟踪使用情况)
  - [使用 MCP 服务器](#使用-mcp-服务器)
- [🚀 安装指南](#-安装指南)
- [🔨 从源码构建](#-从源码构建)
- [🛠️ 开发指南](#️-开发指南)
- [🔒 安全性](#-安全性)
- [🤝 贡献指南](#-贡献指南)
- [📄 许可证](#-许可证)
- [🙏 鸣谢](#-鸣谢)

## ✨ 功能特性

### 🗂️ **项目与会话管理**
- **可视化项目浏览器**：浏览位于 `~/.claude/projects/` 的所有 Claude Code 项目
- **会话历史**：查看并恢复过往的编码会话，保留完整上下文
- **智能搜索**：通过内置搜索快速查找项目和会话
- **会话洞察**：一目了然地查看首条消息、时间戳和会话元数据

### 🤖 **CC Agents**
- **自定义 AI 智能体**：使用自定义系统提示词和行为创建专用智能体
- **智能体库**：为不同任务构建专属智能体集合
- **后台执行**：在独立进程中运行智能体，实现非阻塞操作
- **执行历史**：通过详细日志和性能指标跟踪所有智能体运行情况

### 📊 **使用分析仪表盘**
- **成本追踪**：实时监控你的 Claude API 使用情况与费用
- **Token 分析**：按模型、项目和时间段进行详细拆解
- **可视化图表**：美观的图表展示使用趋势和模式
- **导出数据**：导出使用数据以便财务核算与分析

### 🔌 **MCP 服务器管理**
- **服务器注册表**：通过中央界面管理模型上下文协议（Model Context Protocol）服务器
- **便捷配置**：通过界面添加服务器或从现有配置中导入
- **连接测试**：使用前验证服务器连通性
- **Claude Desktop 导入**：从 Claude Desktop 导入服务器配置

### ⏰ **时间线与检查点**
- **会话版本控制**：在编码会话的任何节点创建检查点
- **可视化时间线**：通过分支时间线浏览你的会话历史
- **即时恢复**：一键跳转回任意检查点
- **分叉会话**：从现有检查点创建新分支
- **差异查看器**：清晰查看检查点之间的具体变更

### 📝 **CLAUDE.md 管理**
- **内置编辑器**：在应用内直接编辑 CLAUDE.md 文件
- **实时预览**：实时查看 Markdown 渲染效果
- **项目扫描器**：自动查找项目中所有的 CLAUDE.md 文件
- **语法高亮**：完整的 Markdown 支持与语法高亮

## 📖 使用方法

### 快速开始

1. **启动 opcode**：安装完成后打开应用程序
2. **欢迎界面**：选择 CC Agents 或 Projects
3. **首次设置**：opcode 将自动检测你的 `~/.claude` 目录

### 管理项目

```
Projects → Select Project → View Sessions → Resume or Start New
```

- 点击任意项目查看其会话
- 每个会话显示首条消息和时间戳
- 直接恢复会话或开始新的会话

### 创建智能体

```
CC Agents → Create Agent → Configure → Execute
```

1. **设计你的智能体**：设置名称、图标和系统提示词
2. **配置模型**：在可用的 Claude 模型中选择
3. **设置权限（permission）**：配置文件读写和网络访问权限
4. **执行任务**：在任何项目上运行你的智能体

### 跟踪使用情况

```
Menu → Usage Dashboard → View Analytics
```

- 按模型、项目和日期监控费用
- 导出数据生成报告
- 设置使用量警报（即将推出）

### 使用 MCP 服务器

```
Menu → MCP Manager → Add Server → Configure
```

- 手动添加或通过 JSON 导入服务器
- 从 Claude Desktop 配置中导入
- 使用前测试连接

## 🚀 安装指南

### 前置条件

- **Claude Code CLI**：从 [Claude 官方网站](https://claude.ai/code) 安装

### 发布版可执行文件即将上线

## 🔨 从源码构建

### 前置条件

在从源码构建 opcode 之前，请确保已安装以下内容：

#### 系统要求

- **操作系统（Operating System）**：Windows 10/11、macOS 11+ 或 Linux（Ubuntu 20.04+）
- **内存（RAM）**：最低 4GB（推荐 8GB）
- **存储空间**：至少预留 1GB 可用空间

#### 必需工具

1. **Rust** (1.70.0 或更高版本)
   ```bash
   # Install via rustup
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

2. **Bun** (最新版本)
   ```bash
   # Install bun
   curl -fsSL https://bun.sh/install | bash
   ```

3. **Git**
   ```bash
   # Usually pre-installed, but if not:
   # Ubuntu/Debian: sudo apt install git
   # macOS: brew install git
   # Windows: Download from https://git-scm.com
   ```

4. **Claude Code CLI**
   - 从 [Claude 官方网站](https://claude.ai/code) 下载并安装
   - 确保 `claude` 已添加到你的 PATH 环境变量中

#### 平台特定依赖项

**Linux (Ubuntu/Debian)**
```bash
# Install system dependencies
sudo apt update
sudo apt install -y \
  libwebkit2gtk-4.1-dev \
  libgtk-3-dev \
  libayatana-appindicator3-dev \
  librsvg2-dev \
  patchelf \
  build-essential \
  curl \
  wget \
  file \
  libssl-dev \
  libxdo-dev \
  libsoup-3.0-dev \
  libjavascriptcoregtk-4.1-dev
```

**macOS**
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Install additional dependencies via Homebrew (optional)
brew install pkg-config
```

**Windows**
- 安装 [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- 安装 [WebView2](https://developer.microsoft.com/microsoft-edge/webview2/)（Windows 11 通常已预装）

### 构建步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/getAsterisk/opcode.git
   cd opcode
   ```

2. **安装前端依赖项**
   ```bash
   bun install
   ```

3. **构建应用程序**
   
   **开发模式（支持热重载）**
   ```bash
   bun run tauri dev
   ```
   
   **生产环境构建**
   ```bash
   # Build the application
   bun run tauri build
   
   # The built executable will be in:
   # - Linux: src-tauri/target/release/
   # - macOS: src-tauri/target/release/
   # - Windows: src-tauri/target/release/
   ```

4. **平台特定构建选项**
   
   **调试模式（编译更快，二进制文件体积较大）**
   ```bash
   bun run tauri build --debug
   ```
   
   **macOS 通用二进制文件（Intel + Apple Silicon）**
   ```bash
   bun run tauri build --target universal-apple-darwin
   ```

### 故障排除

#### 常见问题

1. **"cargo not found" 错误**
   - 确保已安装 Rust 且 `~/.cargo/bin` 已在你的 PATH 中
   - 运行 `source ~/.cargo/env` 或重启终端

2. **Linux: "webkit2gtk not found" 错误**
   - 安装上述列出的 webkit2gtk 开发包
   - 在较新的 Ubuntu 版本上，你可能需要 `libwebkit2gtk-4.0-dev`

3. **Windows: "MSVC not found" 错误**
   - 安装包含 C++ 支持组件的 Visual Studio Build Tools
   - 安装完成后重启终端

4. **"claude command not found" 错误**
   - 确保已安装 Claude Code CLI 且已在 PATH 中
   - 使用 `claude --version` 测试

5. **构建失败提示 "out of memory"**
   - 尝试减少并行编译任务数：`cargo build -j 2`
   - 关闭其他应用程序以释放内存（RAM）

#### 验证你的构建

构建完成后，你可以直接运行可执行文件来验证应用是否正常工作：

```bash
# Run the built executable directly
# Linux/macOS
./src-tauri/target/release/opcode

# Windows
./src-tauri/target/release/opcode.exe
```

### 构建产物

构建过程会生成以下产物：

- **可执行文件**：主程序 opcode
- **安装包**（使用 `tauri build` 时）：
  - `.deb` 包（Linux）
  - `.AppImage`（Linux）
  - `.dmg` 安装器（macOS）
  - `.msi` 安装器（Windows）
  - `.exe` 安装器（Windows）

所有产物均位于 `src-tauri/target/release/` 目录下。

## 🛠️ 开发指南

### 技术栈

- **前端**：React 18 + TypeScript + Vite 6
- **后端**：Rust (Tauri 2)
- **UI 框架**：Tailwind CSS v4 + shadcn/ui
- **数据库**：SQLite（通过 rusqlite）
- **包管理器**：Bun

### 项目结构

```
opcode/
├── src/                   # React frontend
│   ├── components/        # UI components
│   ├── lib/               # API client & utilities
│   └── assets/            # Static assets
├── src-tauri/             # Rust backend
│   ├── src/
│   │   ├── commands/      # Tauri command handlers
│   │   ├── checkpoint/    # Timeline management
│   │   └── process/       # Process management
│   └── tests/             # Rust test suite
└── public/                # Public assets
```

### 开发命令

```bash
# Start development server
bun run tauri dev

# Run frontend only
bun run dev

# Type checking
bunx tsc --noEmit

# Run Rust tests
cd src-tauri && cargo test

# Format code
cd src-tauri && cargo fmt
```

## 🔒 安全性

opcode 高度重视你的隐私与安全：

1. **进程隔离（Process Isolation）**：智能体在独立进程中运行
2. **权限控制**：按智能体配置文件和网络访问权限
3. **本地存储**：所有数据仅保留在你的设备上
4. **无遥测（No Telemetry）**：不收集或追踪任何数据
5. **开源透明**：通过完全公开的源代码实现透明度

## 🤝 贡献指南

我们欢迎你的贡献！详情请参阅我们的 [贡献指南](CONTRIBUTING.md)。

### 可贡献方向

- 🐛 Bug 修复与改进
- ✨ 新功能与增强
- 📚 文档优化
- 🎨 UI/UX 体验提升
- 🧪 测试覆盖率扩展
- 🌐 国际化支持

## 📄 许可证

本项目采用 AGPL 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 🙏 鸣谢

- 基于 [Tauri](https://tauri.app/) 构建 —— 用于开发安全桌面应用的可靠框架
- [Claude](https://claude.ai) by Anthropic

---

<div align="center">
  <p>
    <strong>Made with ❤️ by the <a href="https://asterisk.so/">Asterisk</a></strong>
  </p>
  <p>
    <a href="https://github.com/getAsterisk/opcode/issues">Report Bug</a>
    ·
    <a href="https://github.com/getAsterisk/opcode/issues">Request Feature</a>
  </p>
</div>


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=getAsterisk/opcode&type=Date)](https://www.star-history.com/#getAsterisk/opcode&Date)