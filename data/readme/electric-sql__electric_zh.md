<p align="center">
  <a href="https://electric-sql.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)"
          srcset="https://raw.githubusercontent.com/electric-sql/meta/main/identity/ElectricSQL-logo-next.svg"
      />
      <source media="(prefers-color-scheme: light)"
          srcset="https://raw.githubusercontent.com/electric-sql/meta/main/identity/ElectricSQL-logo-black.svg"
      />
      <img alt="ElectricSQL logo"
          src="https://raw.githubusercontent.com/electric-sql/meta/main/identity/ElectricSQL-logo-black.svg"
      />
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/electric-sql/electric/actions"><img src="https://github.com/electric-sql/electric/actions/workflows/elixir_tests.yml/badge.svg"></a>
  <a href="https://github.com/electric-sql/electric/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache_2.0-green" alt="License - Apache 2.0"></a>
  <a href="https://electric-sql.com/blog/2025/03/17/electricsql-1.0-released"><img src="https://img.shields.io/badge/status-1.0-green" alt="Status - Beta"></a>
  <a href="https://discord.electric-sql.com"><img src="https://img.shields.io/discord/933657521581858818?color=5969EA&label=discord" alt="Chat - Discord"></a>
  <a href="https://x.com/ElectricSQL" target="_blank"><img src="https://img.shields.io/twitter/follow/ElectricSQL.svg?style=social&label=Follow @ElectricSQL"></a>
</p>

# Electric <!-- omit in toc -->

PostgreSQL 的实时同步引擎。

**目录：**

- [快速链接](#quick-links)
- [什么是 Electric？](#what-is-electric)
- [快速入门](#getting-started)
- [HTTP API 文档](#http-api-docs)
- [Phoenix LiveDashboard](#phoenix-livedashboard)
- [开发 Electric](#developing-electric)
  - [Mac 环境配置](#mac-setup)
- [贡献代码](#contributing)
- [支持](#support)

## 快速链接

- [快速入门](https://electric-sql.com/docs/quickstart)
- [官网](https://electric-sql.com)
- [关于](https://electric-sql.com/about)
- [文档](https://electric-sql.com/docs)
- [演示示例](https://electric-sql.com/demos)（另见 [`./examples` 文件夹](./examples)）

## 什么是 Electric？

同步是现代高性能软件背后的关键要素。从 Figma、Linear 等应用，到基于本地实时数据运行的 AI 智能体，都离不开它。

Electric 是一款 PostgreSQL 同步引擎。它帮你解决同步过程中的复杂难题，包括部分复制（partial replication）、扇出（fan-out）以及数据投递（data delivery）。让你无需自行实现同步逻辑，即可构建出色的软件。

具体来说，Electric 是专为 PostgreSQL 设计的读路径同步引擎。它将数据从 PostgreSQL 同步导出到任意你需要的地方。核心同步协议基于底层的 [HTTP API](https://electric-sql.com/docs/api/http)，并可与 CDN 集成以实现高可扩展的数据投递。

部分复制功能通过 [Shapes](https://electric-sql.com/docs/guides/shapes) 进行管理。同步数据可以直接消费，或通过 [客户端库（client libraries）](https://electric-sql.com/docs/api/clients/typescript) 和 [框架集成（framework integrations）](https://electric-sql.com/docs/api/integrations/react) 使用。

## 快速入门

请参阅[快速入门指南](https://electric-sql.com/docs/quickstart)以快速上手。简而言之，你需要：

1. 拥有一个启用了逻辑复制（logical replication）的 PostgreSQL 数据库；然后
2. 在其前端运行 Electric，并通过 `DATABASE_URL` 进行连接

例如，使用本仓库根目录下的 [Docker Compose](https://docs.docker.com/compose/)：

```sh
docker compose -f .support/docker-compose.yml up
```

随后可通过 [HTTP API](https://electric-sql.com/docs/api/http) 同步 PostgreSQL 中的数据。例如，开始同步整个 `foo` 表：

```sh
curl -i 'http://localhost:3000/v1/shape?table=foo&offset=-1'
```

或者使用客户端或集成方案，例如 React Hook [`useShape`](https://electric-sql.com/docs/api/integrations/react)：

```jsx
import { useShape } from '@electric-sql/react'

function Component() {
  const { data } = useShape({
    url: `http://localhost:3000/v1/shape`,
    params: {
      table: `foo`,
      where: `title LIKE 'foo%'`,
    },
  })

  return JSON.stringify(data)
}
```

更多详情请参阅[快速入门](https://electric-sql.com/docs/quickstart)和[文档](https://electric-sql.com)。

## HTTP API 文档

HTTP API 的定义位于 [website/electric-api.yaml](./website/electric-api.yaml) 中的 [OpenAPI spec](https://swagger.io/specification/)。

## Phoenix LiveDashboard

Electric 提供了一个可选的 [Phoenix LiveDashboard](https://github.com/phoenixframework/phoenix_live_dashboard)，用于实时监控运行中的系统（包括 VM 指标、进程信息、ETS 表等）。

要启用该功能，请设置环境变量 `ELECTRIC_LIVE_DASHBOARD_PORT`：

```sh
ELECTRIC_LIVE_DASHBOARD_PORT=4000
```

仪表盘将可在 `http://localhost:4000`（或你指定的端口）访问。当未设置该变量时，仪表盘不会启动。

> **警告：LiveDashboard 端点完全未进行身份验证。** 任何能访问该端口的人都可以查看内部系统状态。在生产环境中，你**必须**使用防火墙规则、网络策略或其他类似控制手段限制对该端口的访问。切勿将其暴露于公共互联网。

## 开发 Electric

我们使用 [asdf](https://asdf-vm.com/) 来安装 Elixir、Erlang 和 Node.js。版本定义在 [.tool-versions](.tool-versions) 中。

### Mac 环境配置

```sh
brew install asdf
asdf plugin add nodejs
asdf plugin add pnpm
asdf plugin add elixir
asdf plugin add erlang
asdf install
```

你可能需要修改 `bash`/`zsh` 等 shell 的配置文件（rc file），以便将正确的工具加载到你的环境变量中。

### 运行测试

Electric 为 Elixir 和 TypeScript 组件提供了全面的测试套件。

#### 前置条件

安装依赖（如果尚未安装）：

```sh
asdf install
pnpm install
```

然后启动测试用的 PostgreSQL 数据库：

```sh
cd packages/sync-service
mix start_dev
```

这将启动一个 Docker Compose 环境，其中配置的 PostgreSQL 在端口 54321 上启用了逻辑复制。

停止数据库：

```sh
mix stop_dev
```

#### Elixir 测试

**同步服务（Sync Service）：**

```sh
cd packages/sync-service
mix test
```

生成覆盖率报告：

```sh
mix coveralls.html
```

**Elixir 客户端（Elixir Client）：**

```sh
cd packages/elixir-client
mix test
```

#### TypeScript 测试

TypeScript 测试需要同时启动数据库和同步服务。

在另一个终端中，启动同步服务：

```sh
cd packages/sync-service
iex -S mix
```

然后运行测试：

**单个包：**

```sh
cd packages/typescript-client  # 或任意其他 TS 包
pnpm test
```

**所有 TypeScript 包：**

从根目录执行：

```sh
pnpm -r test
```

生成覆盖率报告：

```sh
pnpm coverage
```

## 贡献代码

请参阅以下文档：

- [贡献指南](https://github.com/electric-sql/electric/blob/main/CONTRIBUTING.md)
- [ Contributor License Agreement (CLA)](https://github.com/electric-sql/electric/blob/main/CLA.md)
- [社区行为准则（Code of Conduct）](https://github.com/electric-sql/electric/blob/main/CODE_OF_CONDUCT.md)

## 支持

我们有一个[开放的社区 Discord 频道](https://discord.electric-sql.com)。欢迎前来打招呼，如果你有任何问题或需要帮助让项目运行起来，请随时告诉我们。

如果能在页面顶部☝️给这个项目点个 Star，我们将不胜感激！