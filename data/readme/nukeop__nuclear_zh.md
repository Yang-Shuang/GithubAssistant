<p align="center">
  <picture>
    <source alt="Nuclear Music Player"  srcset="packages/docs/.gitbook/assets/readme-banner.png">
    <img alt="Nuclear Music Player"  srcset="packages/docs/.gitbook/assets/readme-banner.png">
  </picture>


</p>

<div align="center">

# Nuclear 

</div>

<div align="center">

  Nuclear 是一款免费、开源的音乐播放器，无广告且无数据追踪。搜索任意歌曲或艺术家，创建播放列表并开始聆听。<br>
  支持在 Windows、macOS 和 Linux 系统上运行。
  
</div>

## 截图

<p align="center">
  <img src="packages/docs/.gitbook/assets/dashboard-main.png" alt="Nuclear Music Player - Dashboard" width="100%">
</p>

Nuclear 内置了多种主题：

<p align="center">
  <img src="packages/docs/.gitbook/assets/dashboard-green.png" alt="Green theme" width="32%">
  <img src="packages/docs/.gitbook/assets/dashboard-aqua.png" alt="Aqua theme" width="32%">
  <img src="packages/docs/.gitbook/assets/dashboard-mint.png" alt="Mint theme" width="32%">
</p>
<p align="center">
  <img src="packages/docs/.gitbook/assets/dashboard-orange.png" alt="Orange theme" width="32%">
  <img src="packages/docs/.gitbook/assets/dashboard-red.png" alt="Red theme" width="32%">
  <img src="packages/docs/.gitbook/assets/dashboard-violet.png" alt="Violet theme" width="32%">
</p>

| | |
|:---:|:---:|
| ![Search artists](packages/docs/.gitbook/assets/search-artists.png) | ![Search albums](packages/docs/.gitbook/assets/search-albums.png) |
| 艺术家搜索 | 专辑搜索 |
| ![Playlists](packages/docs/.gitbook/assets/playlists.png) | ![Plugin store](packages/docs/.gitbook/assets/plugin-store.png) |
| 播放列表 | 插件商店 |
| ![Installed plugins](packages/docs/.gitbook/assets/installed-plugins.png) | ![Preferences](packages/docs/.gitbook/assets/preferences.png) |
| 已安装的插件 | 偏好设置 |
| ![What's new](packages/docs/.gitbook/assets/whats-new.png) | ![Log viewer](packages/docs/.gitbook/assets/log-viewer.png) |
| 更新内容 | 日志查看器 |

## 下载

请前往[发布页面](https://github.com/nukeop/nuclear/releases)获取适用于你平台的最新版本。

| Platform | Formats |
|----------|---------|
| Windows | `.exe` installer, `.msi` |
| macOS | `.dmg` (Apple Silicon and Intel) |
| Linux | `.AppImage`, `.deb`, `.rpm`, `.flatpak` |

## 功能特性

- 搜索音乐并从任意音源流式播放
- 浏览艺术家页面，查看简介、作品列表及相似歌手
- 浏览专辑页面，查看曲目列表
- 队列管理支持随机播放、循环播放及拖拽排序
- 收藏功能（支持专辑、艺术家和歌曲）
- 播放列表（支持创建、导入、导出，以及从各平台导入）
- 强大的插件系统，内置插件商店
- 主题（内置及自定义 CSS 主题）
- MCP 服务器允许你的 AI Agent 驱动播放器操作
- 自动更新
- 键盘快捷键
- 支持多语言本地化

## 插件

Nuclear 现已拥有强大的插件系统！所有功能均重新设计为可由插件驱动。

插件可提供音频流源、元数据、播放列表、仪表盘内容等。你可以从内置的插件商店浏览并安装插件，或使用 [@nuclearplayer/plugin-sdk](https://www.npmjs.com/package/@nuclearplayer/plugin-sdk) 自行开发。

## MCP

你可以在「设置」→「集成（Integrations）」中启用 MCP 服务器。

随后将其添加到 **Claude Code：**

```bash
claude mcp add nuclear --transport http http://127.0.0.1:8800/mcp
```

**Codex CLI：**

```bash
codex mcp add nuclear --url http://127.0.0.1:8800/mcp
```

**OpenCode：**

```json
{
  "mcp": {
    "nuclear": {
      "type": "remote",
      "url": "http://127.0.0.1:8800/mcp"
    }
  }
}
```

**Claude Desktop / Cursor / Windsurf：**

```json
{
  "mcpServers": {
    "nuclear": {
      "url": "http://127.0.0.1:8800/mcp"
    }
  }
}
```

该 MCP 服务设计为支持自动发现，但你可以加载以下技能文件让你的 AI 快速熟悉操作流程：[Nuclear MCP Skill](./packages/docs/public/skills/nuclear-mcp.zip)

## 开发指南

Nuclear 是一个由 Turborepo 管理的 pnpm Monorepo。主应用基于 Tauri（Rust + React）构建。

### 前置条件

- Node.js >= 22
- pnpm >= 9
- Rust（稳定版）
- 平台特定的 Tauri 依赖项（[详见 Tauri 文档](https://v2.tauri.app/start/prerequisites/)）

### 快速开始

```bash
git clone https://github.com/nukeop/nuclear.git
cd nuclear
pnpm install
pnpm dev
```

### 常用命令

```bash
pnpm dev            # Run the player in dev mode
pnpm dev:remote     # Same, but binds Vite to 0.0.0.0 so you can open the remote control UI from other devices on your LAN
pnpm build          # Build all packages
pnpm test           # Run all tests
pnpm lint           # Lint all packages
pnpm type-check     # TypeScript checks
pnpm storybook      # Run Storybook
```

## 社区交流

- [Discord](https://discord.gg/JqPjKxE)
- [Mastodon](https://fosstodon.org/@nuclearplayer)
- [Discussions](https://github.com/nukeop/nuclear/discussions)

## 许可证

AGPL-3.0。详见 [LICENSE](LICENSE)。