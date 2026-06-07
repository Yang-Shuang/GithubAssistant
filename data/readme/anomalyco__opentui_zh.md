# OpenTUI

<div align="center">
    <a href="https://www.npmjs.com/package/@opentui/core"><img alt="npm" src="https://img.shields.io/npm/v/@opentui/core?style=flat-square" /></a>
    <a href="https://github.com/anomalyco/opentui/actions/workflows/build-core.yml"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/anomalyco/opentui/build-core.yml?style=flat-square&branch=main" /></a>
    <a href="https://github.com/msmps/awesome-opentui"><img alt="awesome opentui list" src="https://awesome.re/badge-flat.svg" /></a>
</div>

OpenTUI 是一个使用 Zig 编写的原生终端 UI 核心，并提供 TypeScript 绑定。该原生核心暴露了 C ABI（应用程序二进制接口），因此可被任何语言调用。OpenTUI 目前正为 [OpenCode](https://opencode.ai) 提供生产环境支持，未来也将支撑 [terminal.shop](https://terminal.shop)。它是一个可扩展的核心框架，注重正确性、稳定性和高性能。它提供基于组件的架构和灵活的布局能力，帮助你构建复杂的终端应用程序。

文档：https://opentui.com/docs/getting-started

使用 [bun](https://bun.sh) 和 [create-tui](https://github.com/msmps/create-tui) 快速开始：

```bash
bun create tui
```

此仓库包含以下软件包：

- [`@opentui/core`](packages/core) - OpenTUI 原生 Zig 核心的 TypeScript 绑定，提供命令式 API 及所有基础组件。
- [`@opentui/three`](packages/three) - 用于 OpenTUI 的 Three.js WebGPU 渲染器。
- [`@opentui/solid`](packages/solid) - 用于 OpenTUI 的 SolidJS 协调器（Reconciler）。
- [`@opentui/react`](packages/react) - 用于 OpenTUI 的 React 协调器。
- [`@opentui/examples`](packages/examples) - 示例浏览器及独立可执行文件的构建版本。

## 安装

注意：构建软件包前，请确保你的系统已安装 [Zig](https://ziglang.org/learn/getting-started/)。

### TypeScript / JavaScript

```bash
bun install @opentui/core
```

## AI Agent 技能

让你的 AI 编程助手掌握 OpenTUI 的 API 与使用模式。

**通过 [`npx skills`](https://skills.sh) 进行通用安装：**

```bash
npx skills add anomalyco/opentui --skill opentui
```

全局安装以适用于所有项目：

```bash
npx skills add anomalyco/opentui --skill opentui -g
```

OpenCode 使用相同的安装命令，无需额外安装程序。

## 尝试示例

你无需克隆仓库即可快速体验 OpenTUI 示例：

**适用于 macOS、Linux、WSL、Git Bash：**

```bash
curl -fsSL https://raw.githubusercontent.com/anomalyco/opentui/main/packages/examples/install.sh | sh
```

**适用于 Windows（PowerShell / CMD）：**

请直接从 [GitHub Releases 页面](https://github.com/anomalyco/opentui/releases/latest) 下载最新版本。

## 运行示例（从仓库根目录）

### TypeScript 示例

```bash
bun install
cd packages/examples
bun run dev
```

## 开发指南

请参阅 [开发指南](packages/core/docs/development.md)，了解构建、测试、调试及本地开发链接的方法。

### 文档资源

- [网站文档](https://opentui.com/docs/getting-started) - 使用指南与 API 参考手册
- [开发指南](packages/core/docs/development.md) - 构建、测试及本地开发链接说明
- [快速入门](packages/core/docs/getting-started.md) - API 与使用教程
- [环境变量](packages/core/docs/env-vars.md) - 配置选项说明

## 项目展示

欢迎在 [awesome-opentui](https://github.com/msmps/awesome-opentui) 列表中展示你的作品。该列表精选了基于 OpenTUI 构建的优秀资源与终端用户界面（TUI）项目。