<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/react-doctor-readme-logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/react-doctor-readme-logo-light.svg">
  <img alt="React Doctor" src="./assets/react-doctor-readme-logo-light.svg" width="134" height="36">
</picture>

[![version](https://img.shields.io/npm/v/react-doctor?style=flat&colorA=000000&colorB=000000)](https://npmjs.com/package/react-doctor)
[![downloads](https://img.shields.io/npm/dt/react-doctor.svg?style=flat&colorA=000000&colorB=000000)](https://npmjs.com/package/react-doctor)

你的 AI 代理（Agent）写出了不够规范的 React 代码？它能帮你精准拦截。

React Doctor 会对你的代码库进行确定性扫描，全面检测状态管理（State）与副作用（Effects）、性能、架构、安全性以及可访问性等方面的潜在问题。

兼容所有 React 框架与库——Next.js、Vite、TanStack、React Native、Expo，应有尽有。

[官网文档 →](https://react.doctor/docs)

## 安装

### 1. 快速开始

在项目根目录运行以下命令即可获取代码审计报告。

```bash
npx react-doctor@latest
```

https://github.com/user-attachments/assets/07cc88d9-9589-44c3-aa73-5d603cb1c570

### 2. 为 AI 代理安装（Agent）

完成审计后，你可以为代码编辑代理安装此功能模块，使其学会识别并修复相关问题。

```bash
npx react-doctor@latest install
```

支持 Claude Code、Cursor、Codex、OpenCode 等多种工具。

### 3. 在 CI（GitHub Actions）中为团队运行

[![GitHub Action](https://img.shields.io/badge/GitHub%20Action-React%20Doctor-000000?style=flat&labelColor=000000&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/react-doctor)

从 Marketplace 引入该可复用 GitHub Action，即可在每次 Pull Request 时进行扫描，提供行内标注，并将结果发布到 Reviewer 常看的地方。

```yaml
name: React Doctor

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

permissions:
  contents: read
  pull-requests: write
  issues: write

concurrency:
  group: react-doctor-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  react-doctor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: millionco/react-doctor@v1
```

`@v1` 始终指向该 Action 最新的 `v1.x` 版本。为了提升 CI 安全性（特别是当工作流拥有 `pull-requests: write` 权限时），建议锁定完整的 Commit SHA，并交由 Dependabot 或 Renovate 自动维护更新：

```yaml
- uses: millionco/react-doctor@b612664043a9be414166e3c6a69b355e39a8dcf4 # v1.1.1
```

[添加 GitHub Action →](https://github.com/marketplace/actions/react-doctor)

### 4. 在 `doctor.config.ts` 中配置规则

在项目根目录创建 `doctor.config.ts`（或 `.js`、`.mjs`、`.cjs`、`.json`、`.jsonc`）文件进行配置。

```ts
// doctor.config.ts
import type { ReactDoctorConfig } from "react-doctor/api";

export default {
  lint: true,
  rules: {
    "react-doctor/no-array-index-as-key": "off",
  },
} satisfies ReactDoctorConfig;
```

更偏好使用 JSON？可使用 `doctor.config.json`：

```jsonc
{
  "$schema": "https://react.doctor/schema/config.json",
  "lint": true,
}
```

## 遥测数据 (Telemetry)

该 CLI 会将崩溃信息、基础运行轨迹及匿名使用统计发送至 [Sentry](https://sentry.io/)，以帮助我们修复 Bug 并优化工作优先级。

我们收集的数据包括：

- **环境信息**：CLI 版本、操作系统平台、Node.js 版本
- **调用信息**：执行的命令、包管理器类型及运行上下文（本地开发 / CI 环境 / AI 编码代理）
- **项目特征**：框架类型、React 版本、TypeScript 使用情况、项目规模（不含文件内容）
- **触发的规则**：仅包含规则名称及触发次数（例如 `react-doctor/no-array-index-as-key`），不包含代码或具体检测结果。
- 反混淆后的 React Doctor CLI 堆栈跟踪信息

如需禁用遥测功能，请运行：`npx react-doctor@latest --no-telemetry`

## 贡献指南

[欢迎提交 Issue！](https://github.com/millionco/react-doctor/issues)

MIT 协议开源