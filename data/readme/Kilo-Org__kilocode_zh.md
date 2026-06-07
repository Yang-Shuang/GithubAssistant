<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code"><img src="https://raster.shields.io/badge/VS_Code_Marketplace-007ACC?style=flat&logo=visualstudiocode&logoColor=white" alt="VS Code Marketplace" height="20"></a>
  <a href="https://x.com/kilocode"><img src="https://raster.shields.io/badge/kilocode-000000?style=flat&logo=x&logoColor=white" alt="X (Twitter)" height="20"></a>
  <a href="https://blog.kilo.ai"><img src="https://raster.shields.io/badge/Blog-555?style=flat&logo=substack&logoColor=white" alt="Substack Blog" height="20"></a>
  <a href="https://kilo.ai/discord"><img src="https://raster.shields.io/badge/Join%20Discord-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord" height="20"></a>
  <a href="https://www.reddit.com/r/kilocode/"><img src="https://raster.shields.io/badge/Join%20r%2Fkilocode-D84315?style=flat&logo=reddit&logoColor=white" alt="Reddit" height="20"></a>
</p>

<p align="center">
  <a href="https://kilo.ai"><img width="250" alt="kilo-code-logo" src="https://github.com/user-attachments/assets/bdb0c174-b9fd-40ad-a47b-f3aab9b54e8d" /></a>
</p>

<p align="center">
  <strong>Kilo 是一款集大成的智能体（Agent）工程平台。</strong><br>
  借助最受欢迎的开源编码智能体，构建、交付与迭代更快速。
</p>

<p align="center">
  <img width="100%" alt="Kilo Code running inside VS Code" src="https://kilo.ai/_next/image?url=%2Fscreenshots%2Fvs-code%2Fvs-code-home-page-screenshot.png&w=3840&q=75">
</p>

<p align="center">
  <a href="https://kilo.ai">官网</a> ·
  <a href="https://kilo.ai/install">安装</a> ·
  <a href="https://kilo.ai/landing/vs-code">IDE</a> ·
  <a href="https://kilo.ai/cli">CLI</a> ·
  <a href="https://kilo.ai/docs">文档</a> ·
  <a href="https://kilo.ai/leaderboard">模型</a> ·
  <a href="https://kilo.ai/gateway">Gateway</a> ·
  <a href="https://kilo.ai/pricing">定价</a> ·
  <a href="https://kilo.ai/pricing/kilo-pass">Kilo Pass</a>
</p>

<p align="center">
  支持 500+ 模型。一款开源智能体，覆盖 <a href="https://kilo.ai/install">VS Code</a>、<a href="https://kilo.ai/features/jetbrains-native">JetBrains</a>、<a href="https://kilo.ai/cli">CLI</a>、<a href="https://kilo.ai/slack">Slack</a> 与 <a href="https://kilo.ai/cloud">Cloud</a>。
</p>

- ✨ 使用自然语言生成代码
- ✅ 自动检查自身工作成果
- 🧪 执行终端命令
- 🌐 自动化浏览器操作
- ⚡ 行内智能代码补全建议
- 🤖 搭载最新 AI 模型
- 🎁 可选使用 API Key

## Quick Links

- [VS Code Marketplace](https://kilo.ai/vscode-marketplace?utm_source=Readme)（下载）
- 安装 CLI：`npm install -g @kilocode/cli`
- [Kilo.ai 官方主页](https://kilo.ai)（了解更多）

## Key Features

- **代码生成：** Kilo 支持使用自然语言生成代码。
- **行内自动补全：** 在输入时获取由 AI 驱动的智能代码补全建议。
- **任务自动化：** Kilo 可自动化重复性编码任务，节省时间。
- **自动重构：** Kilo 能高效地重构并优化现有代码。
- **MCP Server Marketplace**：Kilo 可轻松查找并使用 MCP 服务器，以扩展智能体功能。
- **多模式（Multi Mode）**：使用 Architect、Coder 和 Debugger 进行规划、编码与调试，并可创建自定义模式。

## Get Started in Visual Studio Code

1. 从 [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code) 安装 Kilo Code 扩展。
2. 创建账户以访问 500 多款前沿 AI 模型（包括 GPT-5.5、Claude Opus 4.7、Claude Sonnet 4.6 和 Gemini 3.1 Pro Preview），定价透明且与官方供应商费率完全一致。
3. 开始使用适配你工作流的 AI 进行编码。观看我们的快速入门指南，了解 Kilo 的实际操作：

<a href="https://youtu.be/pqGfYXgrhig"><img src="https://img.youtube.com/vi/pqGfYXgrhig/maxresdefault.jpg" alt="Watch the video" width="640" height="360"></a>

## Get Started with the CLI

```bash
# npm
npm install -g @kilocode/cli

# Or run directly with npx
npx @kilocode/cli
```

然后在任意项目目录中运行 `kilo` 即可开始。

<!-- kilocode_change start -->

### npm Install Note: Hidden `.kilo` File

在某些系统和 npm 版本中，安装 `@kilocode/cli` 可能会在安装 `kilo` 命令的目录附近（例如全局 npm bin 目录）生成一个隐藏的 `.kilo` 文件。该文件是 npm 生成的启动器辅助文件，并非项目数据。

- **存在原因**：npm 在配置 CLI 可执行文件时可能会生成此类辅助文件。
- **大小说明**：文件大小因平台、npm 版本和安装模式（符号链接或复制启动器）而异，因此无法保证固定大小。
- **安全性**：保留该文件是安全的。请勿手动编辑它。请使用包管理器的卸载命令（`npm uninstall -g @kilocode/cli`）来干净地移除安装残留。
<!-- kilocode_change end -->

### Install from GitHub Releases (Optional)

请前往 [Releases 页面](https://github.com/Kilo-Org/kilocode/releases) 下载最新的二进制文件或源代码，并参考以下快速指南：

- `kilo-<os>-<arch>.zip` 是适用于你操作系统和 CPU 架构的 CLI 二进制文件（Windows 和 macOS）。Linux 用户请使用 `kilo-linux-<arch>.tar.gz`。
- `darwin` 代表 macOS。
- `x64` 为标准的 64 位 Intel/AMD CPU。
- `x64-baseline` 是为较老的 x64 CPU（不支持 AVX 指令集）提供的兼容版本构建。
- `arm64` 为基于 ARM 架构的 Linux/macOS。
- `musl` 是为 Alpine/精简版 Docker（无 glibc）提供的静态链接 Linux 构建版本。Alpine/精简版 Docker 用户应优先选择匹配的 \*-musl 资源文件。
- `kilo-vscode-*.vsix` 是 VS Code 扩展包，并非 CLI 二进制文件。
- `Source code`（源代码）发布版用于从源码构建，不适用于常规安装。

对于大多数用户：

- **Windows（多数电脑）**：`kilo-windows-x64.zip`
- **macOS Apple Silicon**：`kilo-darwin-arm64.zip`
- **macOS Intel**：`kilo-darwin-x64.zip`
- **Linux x64**：`kilo-linux-x64.tar.gz`
- **ARM 架构 Linux**：`kilo-linux-arm64.tar.gz`

### Autonomous Mode (CI/CD)

在运行 `kilo run` 时添加 `--auto` 参数，即可启用完全自主的运行模式，无需用户交互。此功能非常适合 CI/CD 流水线及自动化工作流：

```bash
kilo run --auto "run tests and fix any failures"
```

**重要提示：** `--auto` 参数会禁用所有权限（permission）确认提示，允许智能体无需审批即可执行任何操作。请仅在 CI/CD 流水线等可信环境中使用此功能。

## Contributing

我们欢迎开发者、文档撰写者及技术爱好者做出贡献！
如需开始贡献，请阅读我们的 [Contributing Guide](/CONTRIBUTING.md)。其中包含环境配置、代码规范、贡献类型及如何提交 Pull Request 的详细说明。

有关 VS Code 扩展和 CLI 的发布流程，请参阅 [RELEASING.md](RELEASING.md)。

有关 JetBrains 插件的发布流程，请参阅 [packages/kilo-jetbrains/RELEASING.md](packages/kilo-jetbrains/RELEASING.md)。

## Code of Conduct

我们的社区建立在尊重、包容与协作的基础上。请查阅我们的 [Code of Conduct](/CODE_OF_CONDUCT.md)，了解所有贡献者及社区成员需遵守的规范。

## License

本项目采用 MIT 许可证开源。
你可自由使用、修改和分发此代码（包括商业用途），只需保留正确的署名及许可证声明即可。详见 [License](/LICENSE)。

## FAQ

<details>
<summary>Kilo CLI 源自何处？</summary>

Kilo CLI 是 [OpenCode](https://github.com/anomalyco/opencode) 的分支版本，经过增强以适配 Kilo 智能体工程平台。

</details>