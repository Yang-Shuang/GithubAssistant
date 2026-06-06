<p align="center"><code>npm i -g @openai/codex</code><br />或 <code>brew install --cask codex</code></p>
<p align="center"><strong>Codex CLI</strong> 是 OpenAI 推出的一款在本地计算机上运行的编程智能体（coding agent）。
<p align="center">
  <img src="https://github.com/openai/codex/blob/main/.github/codex-cli-splash.png" alt="Codex CLI splash" width="80%" />
</p>
</br>
如果你希望在代码编辑器（如 VS Code、Cursor、Windsurf）中使用 Codex，<a href="https://developers.openai.com/codex/ide">请安装至你的集成开发环境。</a>
</br>如果你想要桌面应用体验，可运行 <code>codex app</code> 或访问 <a href="https://chatgpt.com/codex?app-landing-page=true">Codex 应用页面</a>。
</br>如果你正在寻找 OpenAI 的<em>云端智能体</em><strong>Codex Web</strong>，请访问 <a href="https://chatgpt.com/codex">chatgpt.com/codex</a>。</p>

---

## 快速开始

### 安装与运行 Codex CLI

使用你偏好的包管理器进行全局安装：

```shell
# Install using npm
npm install -g @openai/codex
```

```shell
# Install using Homebrew
brew install --cask codex
```

然后只需运行 `codex` 即可开始使用。

<details>
<summary>你也可以前往<a href="https://github.com/openai/codex/releases/latest">最新的 GitHub 发布页面</a>，下载适用于你平台的对应二进制文件。</summary>

每个 GitHub 发布版本都包含多个可执行文件，但在实际使用中，你可能只需要以下其中一个：

- macOS
  - Apple Silicon/arm64: `codex-aarch64-apple-darwin.tar.gz`
  - x86_64（较旧的 Mac 硬件）：`codex-x86_64-apple-darwin.tar.gz`
- Linux
  - x86_64: `codex-x86_64-unknown-linux-musl.tar.gz`
  - arm64: `codex-aarch64-unknown-linux-musl.tar.gz`

每个压缩包内仅包含一个文件，其名称中已内置平台信息（例如 `codex-x86_64-unknown-linux-musl`），因此解压后你可能需要将其重命名为 `codex`。

</details>

### 搭配 ChatGPT 套餐使用 Codex

运行 `codex` 并选择 **使用 ChatGPT 登录**。我们建议你登录 ChatGPT 账号，以便在 Plus、Pro、Business、Edu 或 Enterprise 套餐内使用 Codex。[详细了解你的 ChatGPT 套餐包含哪些内容](https://help.openai.com/en/articles/11369540-codex-in-chatgpt)。

你也可以通过 API Key 使用 Codex，但这需要[额外配置](https://developers.openai.com/codex/auth#sign-in-with-an-api-key)。

## 文档

- [**Codex Documentation（官方文档）**](https://developers.openai.com/codex)
- [**Contributing（贡献指南）**](./docs/contributing.md)
- [**Installing & building（安装与构建）**](./docs/install.md)
- [**Open source fund（开源基金）**](./docs/open-source-fund.md)

本仓库遵循 [Apache-2.0 License（许可证）](LICENSE)。