<p align="center">
  <a href="https://opencode.ai">
    <picture>
      <source srcset="packages/console/app/src/asset/logo-ornate-dark.svg" media="(prefers-color-scheme: dark)">
      <source srcset="packages/console/app/src/asset/logo-ornate-light.svg" media="(prefers-color-scheme: light)">
      <img src="packages/console/app/src/asset/logo-ornate-light.svg" alt="OpenCode 标志">
    </picture>
  </a>
</p>
<p align="center">开源的 AI 编程智能体。</p>
<p align="center">
  <a href="https://opencode.ai/discord"><img alt="Discord" src="https://img.shields.io/discord/1391832426048651334?style=flat-square&label=discord" /></a>
  <a href="https://www.npmjs.com/package/opencode-ai"><img alt="npm" src="https://img.shields.io/npm/v/opencode-ai?style=flat-square" /></a>
  <a href="https://github.com/anomalyco/opencode/actions/workflows/publish.yml"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/anomalyco/opencode/publish.yml?style=flat-square&branch=dev" /></a>
</p>

<p align="center">
  <a href="README.md">英语</a> |
  <a href="README.zh.md">简体中文</a> |
  <a href="README.zht.md">繁体中文</a> |
  <a href="README.ko.md">韩语</a> |
  <a href="README.de.md">德语</a> |
  <a href="README.es.md">西班牙语</a> |
  <a href="README.fr.md">法语</a> |
  <a href="README.it.md">意大利语</a> |
  <a href="README.da.md">丹麦语</a> |
  <a href="README.ja.md">日语</a> |
  <a href="README.pl.md">波兰语</a> |
  <a href="README.ru.md">俄语</a> |
  <a href="README.bs.md">波斯尼亚语</a> |
  <a href="README.ar.md">阿拉伯语</a> |
  <a href="README.no.md">挪威语</a> |
  <a href="README.br.md">葡萄牙语（巴西）</a> |
  <a href="README.th.md">泰语</a> |
  <a href="README.tr.md">土耳其语</a> |
  <a href="README.uk.md">乌克兰语</a> |
  <a href="README.bn.md">孟加拉语</a> |
  <a href="README.gr.md">希腊语</a> |
  <a href="README.vi.md">越南语</a>
</p>

[![OpenCode 终端界面](packages/web/src/assets/lander/screenshot.png)](https://opencode.ai)

---

### 安装

```bash
# YOLO
curl -fsSL https://opencode.ai/install | bash

# Package managers
npm i -g opencode-ai@latest        # or bun/pnpm/yarn
scoop install opencode             # Windows
choco install opencode             # Windows
brew install anomalyco/tap/opencode # macOS and Linux (recommended, always up to date)
brew install opencode              # macOS and Linux (official brew formula, updated less)
sudo pacman -S opencode            # Arch Linux (Stable)
paru -S opencode-bin               # Arch Linux (Latest from AUR)
mise use -g opencode               # Any OS
nix run nixpkgs#opencode           # or github:anomalyco/opencode for latest dev branch
```

> [!TIP]
> 安装前请移除 0.1.x 之前的旧版本。

### 桌面应用（测试版）

OpenCode 也提供桌面应用程序。你可以直接从[发布页面](https://github.com/anomalyco/opencode/releases)或[opencode.ai/download](https://opencode.ai/download)下载。

| Platform              | Download                           |
| --------------------- | ---------------------------------- |
| macOS (Apple Silicon) | `opencode-desktop-mac-arm64.dmg`   |
| macOS (Intel)         | `opencode-desktop-mac-x64.dmg`     |
| Windows               | `opencode-desktop-windows-x64.exe` |
| Linux                 | `.deb`, `.rpm`, or `.AppImage`     |

```bash
# macOS (Homebrew)
brew install --cask opencode-desktop
# Windows (Scoop)
scoop bucket add extras; scoop install extras/opencode-desktop
```

#### 安装目录

安装脚本将按以下优先级顺序确定安装路径：

1. `$OPENCODE_INSTALL_DIR` - 自定义安装目录
2. `$XDG_BIN_DIR` - 符合 XDG 基础目录规范的路径
3. `$HOME/bin` - 标准用户二进制文件目录（若存在或可创建）
4. `$HOME/.opencode/bin` - 默认回退路径

```bash
# Examples
OPENCODE_INSTALL_DIR=/usr/local/bin curl -fsSL https://opencode.ai/install | bash
XDG_BIN_DIR=$HOME/.local/bin curl -fsSL https://opencode.ai/install | bash
```

### 智能体（agent）

OpenCode 内置了两个 agent，你可以通过 `Tab` 键在它们之间切换。

- **build** - 默认 agent，拥有完整权限，适用于开发工作
- **plan** - 只读 agent，用于分析和代码探索
  - 默认拒绝文件编辑操作
  - 执行 bash 命令前会请求权限（permission）
  - 非常适合探索陌生代码库或规划变更

此外还内置了一个 **general** 子 agent，用于复杂搜索和多步任务。该 agent 主要在内部使用，你也可以在消息中通过 `@general` 调用它。

了解更多关于 [agent](https://opencode.ai/docs/agents) 的信息。

### 文档

如需了解如何配置 OpenCode，[**请查阅我们的官方文档**](https://opencode.ai/docs)。

### 贡献指南

如果你有兴趣为 OpenCode 做出贡献，请在提交 Pull Request（PR）之前阅读我们的[贡献指南](./CONTRIBUTING.md)。

### 关于以 OpenCode 命名的项目说明

如果你正在开发与 OpenCode 相关且名称中包含 “opencode”（例如 “opencode-dashboard” 或 “opencode-mobile”）的项目，请在你的 README 中添加说明，明确指出该项目并非由 OpenCode 团队构建，与我们也无任何关联。

---

**加入我们的社区** [Discord](https://discord.gg/opencode) | [X.com](https://x.com/opencode)