<div align="center">

# Botpress Cloud

[![Discord](https://img.shields.io/badge/Join_Community-white?color=7289da&label=Discord&labelColor=6a7ec1&logo=discord&logoColor=FFF)](https://discord.gg/botpress)
[![YouTube Subscribe](https://img.shields.io/badge/YouTube-red?logo=youtube&logoColor=white)](https://www.youtube.com/c/botpress)
[![Documentation](https://img.shields.io/badge/Documentation-blue?logo=typescript&logoColor=white)](https://docs.botpress.cloud)
[![@botpress/sdk](https://img.shields.io/badge/@botpress%2fsdk-black?logo=npm)](https://www.npmjs.com/package/@botpress/sdk)
[![@botpress/cli](https://img.shields.io/badge/@botpress%2fcli-black?logo=npm)](https://www.npmjs.com/package/@botpress/cli)

[Botpress](https://botpress.com) 是构建由 OpenAI 驱动的**下一代聊天机器人**和助手的终极平台。以闪电般的速度为你的项目或业务开始打造令人惊叹的助手。

[快速入门](#本仓库内容) •
[云平台](https://app.botpress.cloud) •
[文档](https://botpress.com/docs) •
[集成](#集成integrations) •
[插件](#插件plugins)

<img src="https://user-images.githubusercontent.com/10071388/248040379-8aee1b03-c483-4040-8ee0-741554310e88.png" width="800">
  
</div>

## 本仓库内容 (This Repository)

该仓库包含以下内容：

- **[集成（Integrations）](#集成integrations)** – 由 Botpress 维护的在 [Botpress Hub](https://app.botpress.cloud/hub) 上的所有公开集成
- **[开发工具（Devtools）](#开发工具devtools)** – 所有 Botpress Cloud 开发工具（CLI、SDK、API 客户端）
- **[机器人（Bots）](#机器人bots)** - 仅使用 SDK 和 CLI 构建的“代码即机器人”示例
- **[插件（Plugins）](#插件plugins)** – [Botpress Studio](https://studio.botpress.cloud) 上的所有插件 **（即将上线）**

## 贡献指南 (Contributing)

我们非常欢迎社区的贡献！

我们欢迎针对本仓库中任何代码的 Pull Request（PR）和 Issue。更多详情请参阅[本仓库内容](#本仓库内容)部分。

对于与 Botpress Cloud 相关的 Bug 或功能建议，你可以在本仓库创建 Issue，但请注意：在 [Discord](https://discord.gg/botpress) 上与我们交流通常会获得更快的响应！

有关本地部署版 Botpress v12 的任何问题，请参阅 [Botpress v12 仓库](https://github.com/botpress/v12)。

## 集成 (Integrations)

[`/integrations`](./integrations) 文件夹包含我们所有的公开及开源集成。我们邀请社区成员为我们现有的集成分担贡献，或将你自己的集成发布到 [Botpress Hub](https://app.botpress.cloud/hub)。

### 集成开发 (Integration Development)

要开发一个集成，首先安装 [Botpress CLI](https://www.npmjs.com/package/@botpress/cli)：

```sh
npm install -g @botpress/cli # for npm
yarn global add @botpress/cli # for yarn
pnpm install -g @botpress/cli # for pnpm
```

然后，在你选择的目录中创建一个新的集成：

```sh
bp init
```

该命令将根据提供的模板之一生成一个集成。

_此步骤可以在你选择的任意目录和 Git 仓库中执行。创建集成时，无需 Fork 本仓库。_

随后可修改你的集成定义与实现代码，它们分别位于 `integration.definition.ts` 和 `src/index.ts` 文件中。

有关如何开发集成的更多信息，请参阅[文档](https://botpress.com/docs/for-developers/sdk/integration/getting-started)。

### 集成部署 (Integration Deployment)

要测试你的集成，可以使用 Botpress CLI 将其当前版本部署到你的工作区：

```sh
bp deploy
```

这会将你集成的当前版本部署到你的工作区，并使其对所有机器人可用。如果该版本已部署，则会被更新；否则将创建新版本。

默认情况下，所有集成仅对你所在的工作区私有。当你准备好向社区分享你的版本时，可以通过运行以下命令将其设为公开：

```sh
bp deploy --visibility public
```

这将使你的集成在 [Botpress Hub](https://app.botpress.cloud/hub) 上对所有 Botpress 用户可用。一旦你的某个集成版本设为公开，将无法再次更新。

## 机器人 (Bots)

[`/bots`](./bots) 文件夹包含仅使用客户端、SDK 和 CLI 构建的“代码即机器人”示例。

**这不推荐作为构建机器人的方式**，也绝不能替代 Botpress Studio。

不过，对于希望以更具编程化方式构建机器人的高级开发者来说，它可能很有用。

Botpress 团队内部也在使用该方式，因为 Studio 和 SDK 均基于相同的底层基础组件。

## 插件 (Plugins)

即将上线。

## 开发工具 (Devtools)

| **包（Package）**                                                          | **描述**                                         | **文档**                                                               | **代码**               |
| -------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------- | ---------------------- |
| [`@botpress/cli`](https://www.npmjs.com/package/@botpress/cli)             | 构建、部署和管理机器人、集成与插件               | [文档](https://www.botpress.com/docs/for-developers/sdk/cli-reference) | [代码](./packages/cli) |
| [`@botpress/client`](https://www.npmjs.com/package/@botpress/client)       | 用于调用 Botpress API 的类型安全客户端           | [文档]()                                                               | [代码]()               |
| [`@botpress/sdk`](https://www.npmjs.com/package/@botpress/sdk)             | 用于构建集成的 SDK                               | [文档]()                                                               | [代码]()               |

## 本地开发 (Local Development)

### 前置条件 (Prerequisites)

开发环境需安装以下工具：

- [`git`](https://git-scm.com/): Git 是一款免费开源的分布式版本控制系统。
- [`node`](https://nodejs.org/en/): Node.js® 是基于 Chrome 的 V8 JavaScript 引擎构建的 JavaScript 运行时环境。
- [`pnpm`](https://pnpm.io/): PNPM 是一款快速且节省磁盘空间的包管理器。

#### Windows 专属前置条件

- [适用于 Visual Studio 2015-2022 的 Microsoft Visual C++ 可再发行组件包](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist#visual-studio-2015-2017-2019-and-2022)

### 从源码构建 (Building from sources)

```sh
# Clone the repository
git clone https://github.com/botpress/botpress.git
cd botpress

# Install dependencies
pnpm install

# Build all packages
pnpm run build

# Run Checks
pnpm run check
```

## 许可证 (Licensing)

本仓库中的所有软件包均为开源软件，并遵循 [MIT 许可证](LICENSE)。在此仓库贡献代码即表示你同意将你的代码也以此许可证发布。

让我们一起构建聊天机器人开发的未来！ 🤖🚀