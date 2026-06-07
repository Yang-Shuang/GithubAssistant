<h1 align="center">
    <img src="https://github.com/user-attachments/assets/ec60b0c4-87ba-48f4-981a-c55ed0e8497b" height="100" width="375" alt="banner" /><br>
</h1>


<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nanobrowser)
[![Twitter](https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/nanobrowser_ai)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/NN3ABHggMK)
[<img src="https://deepwiki.com/badge.svg" height="28" alt="Ask DeepWiki">](https://deepwiki.com/nanobrowser/nanobrowser)
[![Sponsor](https://img.shields.io/badge/Sponsor-ff69b4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/alexchenzl)

</div>

## 🌐 Nanobrowser

Nanobrowser 是一款开源的 AI Web 自动化工具，直接在浏览器中运行。作为 OpenAI Operator 的免费替代方案，提供灵活的 LLM（大语言模型）选项与多智能体系统。

⬇️ 免费获取 [Chrome Web Store 上的 Nanobrowser](https://chromewebstore.google.com/detail/nanobrowser/imbddededgmcgfhfpcjmijokokekbkal)

👏 加入社区：[Discord](https://discord.gg/NN3ABHggMK) | [X](https://x.com/nanobrowser_ai)

🌟 喜欢 Nanobrowser？请给我们点个 Star，并帮忙推广！

❤️ 通过[赞助我们](https://github.com/sponsors/alexchenzl)支持该项目——每一份贡献都能帮助 Nanobrowser 保持免费与开源！

<div align="center">
<img src="https://github.com/user-attachments/assets/112c4385-7b03-4b81-a352-4f348093351b" width="600" alt="Nanobrowser Demo GIF" />
<p><em>Nanobrowser 的多智能体系统正在实时分析 HuggingFace，Planner（规划器）在遇到障碍时能进行智能自我修正，并动态指导 Navigator（导航器）调整策略——所有操作均在你的浏览器本地运行。</em></p>
</div>

## 🔥 为什么选择 Nanobrowser？

想要一款强大的 AI 浏览器智能体，却不想承担 OpenAI Operator 每月 $200 的高昂费用？**Nanobrowser** 作为一款 Chrome 扩展插件，在提供顶级 Web 自动化能力的同时，让你完全掌控一切：

- **100% 免费** - 无订阅费或隐藏成本。只需安装并使用你自己的 API Key，按实际用量付费即可。
- **注重隐私** - 所有操作均在你的本地浏览器中运行。你的凭证完全由你掌控，绝不会共享给任何云服务。
- **灵活的 LLM 选项** - 连接你偏好的大语言模型提供商，并可自由为不同智能体分配不同的模型。
- **完全开源** - 你的浏览器自动化逻辑完全透明。无黑盒操作或隐藏进程。

> **注意：** 我们目前支持 OpenAI、Anthropic、Gemini、Ollama、Groq、Cerebras、Llama 以及自定义的 OpenAI 兼容提供商，未来将支持更多提供商。


## 📊 核心功能

- **多智能体系统**：专业 AI 智能体协同完成复杂的 Web 工作流
- **交互式侧边栏**：直观的聊天界面，实时显示任务状态
- **任务自动化**：无缝自动化跨网站的重复性操作
- **后续追问**：针对已完成的任务进行上下文相关的后续提问
- **对话历史**：轻松访问并管理你的 AI 智能体交互记录
- **多模型支持**：连接你偏好的 LLM 提供商，并为不同智能体分配不同的模型


## 🌐 浏览器支持

**官方支持：**
- **Chrome** - 完整支持所有功能
- **Edge** - 完整支持所有功能

**不支持：**
- Firefox、Safari 及其他 Chromium 变种（如 Opera、Arc 等）

> **注意**：虽然 Nanobrowser 可能兼容其他基于 Chromium 的浏览器，但我们建议使用 Chrome 或 Edge 以获得最佳体验并确保完全兼容。


## 🚀 快速开始

1. **从 Chrome Web Store 安装**（稳定版）：
   * 访问 [Nanobrowser Chrome Web Store 页面](https://chromewebstore.google.com/detail/nanobrowser/imbddededgmcgfhfpcjmijokokekbkal)
   * 点击“Add to Chrome”按钮
   * 在弹出的提示中确认安装

> **重要提示**：如需最新功能，请从下方的 [手动安装最新版本](#-manually-install-latest-version) 进行安装，因为 Chrome Web Store 的版本可能因审核流程而延迟。

2. **配置智能体模型**：
   * 点击工具栏中的 Nanobrowser 图标打开侧边栏
   * 点击 `Settings`（设置）图标（右上角）
   * 添加你的 LLM API Key
   * 为不同智能体选择要使用的模型（Navigator、Planner）

## 🔧 手动安装最新版本

如需获取包含最新功能的版本：

1. **下载**
    * 从官方 Github [发布页面](https://github.com/nanobrowser/nanobrowser/releases) 下载最新的 `nanobrowser.zip` 文件。

2. **安装**：
    * 解压 `nanobrowser.zip`。
    * 在 Chrome 中打开 `chrome://extensions/`
    * 启用 `Developer mode`（开发者模式，右上角）
    * 点击 `Load unpacked`（加载已解压的扩展程序，左上角）
    * 选择解压后的 `nanobrowser` 文件夹。

3. **配置智能体模型**
    * 点击工具栏中的 Nanobrowser 图标打开侧边栏
    * 点击 `Settings`（设置）图标（右上角）。
    * 添加你的 LLM API Key。
    * 为不同智能体选择要使用的模型（Navigator、Planner）

4. **升级**：
    * 从发布页面下载最新的 `nanobrowser.zip` 文件。
    * 解压并用新文件替换现有的 Nanobrowser 文件。
    * 在 Chrome 中打开 `chrome://extensions/`，点击 Nanobrowser 卡片上的刷新图标。

## 🛠️ 从源码构建

如果你希望自行编译构建 Nanobrowser，请按照以下步骤操作：

1. **前置条件**：
   * [Node.js](https://nodejs.org/)（v22.12.0 或更高版本）
   * [pnpm](https://pnpm.io/installation)（v9.15.1 或更高版本）

2. **克隆代码库**：
   ```bash
   git clone https://github.com/nanobrowser/nanobrowser.git
   cd nanobrowser
   ```

3. **安装依赖项**：
   ```bash
   pnpm install
   ```

4. **构建扩展插件**：
   ```bash
   pnpm build
   ```

5. **加载扩展插件**：
   * 编译后的扩展文件将位于 `dist` 目录中
   * 按照“手动安装”部分的步骤将其加载到你的浏览器中

6. **开发模式**（可选）：
   ```bash
   pnpm dev
   ```

## 🤖 模型选择指南

Nanobrowser 允许你为每个智能体配置不同的 LLM 模型，以平衡性能与成本。以下是推荐的配置方案：

### 高性能配置
- **Planner**：Claude Sonnet 4
  - 更强的推理与规划能力
- **Navigator**：Claude Haiku 3.5
  - 高效处理网页导航任务
  - 性能与成本的平衡之选

### 高性价比配置
- **Planner**：Claude Haiku 或 GPT-4o
  - 成本较低且表现合理
  - 复杂任务可能需要更多迭代次数
- **Navigator**：Gemini 2.5 Flash 或 GPT-4o-mini
  - 轻量级且节省成本
  - 适合基础导航任务

### 本地模型部署
- **设置选项**：
  - 使用 Ollama 或其他自定义 OpenAI 兼容提供商在本地运行模型
  - 零 API 调用费用，数据完全不出本机，隐私性极佳

- **推荐模型**：
  - **Qwen3-30B-A3B-Instruct-2507**
  - **Falcon3 10B**
  - **Qwen 2.5 Coder 14B**
  - **Mistral Small 24B**
  - [社区最新测试结果](https://gist.github.com/maximus2600/75d60bf3df62986e2254d5166e2524cb) 
  - 欢迎在[Discord](https://discord.gg/NN3ABHggMK)分享你使用其他本地模型的经验

- **提示词工程（Prompt Engineering）**：
  - 本地模型需要更具体、更清晰的提示词
  - 避免使用过于宽泛或模糊的指令
  - 将复杂任务拆解为明确、详细的步骤
  - 提供明确的上下文与约束条件

> **注意**：高性价比配置在输出稳定性上可能稍弱，处理复杂任务时可能需要更多迭代。

> **提示**：欢迎自由尝试你自己的模型组合！如果发现了优秀的搭配方案，请在我们的 [Discord](https://discord.gg/NN3ABHggMK) 分享给社区，帮助他人优化他们的设置。

## 💡 实战演示

只需一句话，你即可完成以下强大任务：

1. **新闻摘要**：
   > "Go to TechCrunch and extract top 10 headlines from the last 24 hours"

2. **GitHub 调研**：
   > "Look for the trending Python repositories on GitHub with most stars"

3. **购物比价**：
   > "Find a portable Bluetooth speaker on Amazon with a water-resistant design, under $50. It should have a minimum battery life of 10 hours"

## 🛠️ 开发路线图

我们正积极开发 Nanobrowser，更多令人兴奋的功能即将上线，欢迎加入！ 

查看我们的详细路线图与 upcoming features：[GitHub Discussions](https://github.com/nanobrowser/nanobrowser/discussions/85)。

## 🤝 贡献指南

**我们需要你的帮助来让 Nanobrowser 变得更好！** 所有类型的贡献都受到欢迎：

* **分享提示词（Prompts）与使用案例** 
   * 加入我们的 [Discord 服务器](https://discord.gg/NN3ABHggMK)。
   * 分享你如何使用 Nanobrowser。帮助我们构建实用的提示词库与实际应用场景。
* **提供反馈** 
   * 试用 Nanobrowser，并在我们的 [Discord 服务器](https://discord.gg/NN3ABHggMK) 中反馈性能表现或提出改进建议。
* **贡献代码**
   * 查看我们的 [CONTRIBUTING.md](CONTRIBUTING.md) 了解项目贡献指南。
   * 提交 Pull Request 以修复 Bug、添加新功能或完善文档。


我们坚信开源的力量与社区协作的价值。加入我们，共同构建 Web 自动化的未来！


## 🔒 安全说明

如果你发现安全漏洞，请**不要**通过 Issues、Pull Requests 或 Discussions 公开披露。

相反，请创建 [GitHub Security Advisory](https://github.com/nanobrowser/nanobrowser/security/advisories/new) 以负责任地报告该漏洞。这能让我们在漏洞被公开前及时修复。

感谢你的帮助，共同维护 Nanobrowser 及其用户的安全！

## 💬 社区

加入我们不断增长的开发者与用户社区：

- [Discord](https://discord.gg/NN3ABHggMK) - 与团队及社区成员交流
- [Twitter](https://x.com/nanobrowser_ai) - 关注最新动态与公告
- [GitHub Discussions](https://github.com/nanobrowser/nanobrowser/discussions) - 分享想法与提问

## 👏 致谢

Nanobrowser 建立在其他优秀的开源项目之上：

- [Browser Use](https://github.com/browser-use/browser-use)
- [Puppeteer](https://github.com/EmergenceAI/Agent-E)
- [Chrome Extension Boilerplate](https://github.com/Jonghakseo/chrome-extension-boilerplate-react-vite)
- [LangChain](https://github.com/langchain-ai/langchainjs)

向它们的创作者与贡献者致以最诚挚的感谢！

## 📄 许可证

本项目采用 Apache License 2.0 开源协议 - 详见 [LICENSE](LICENSE) 文件。

由 Nanobrowser Team 用 ❤️ 打造。 

喜欢 Nanobrowser？请给我们点个 Star 🌟，并加入我们的 [Discord](https://discord.gg/NN3ABHggMK) | [X](https://x.com/nanobrowser_ai)

## ⚠️ 关于衍生项目的免责声明

**我们明确 *不* 认可、支持或参与任何基于此代码库的加密货币、代币、NFT 或其他区块链相关应用项目。**

**此类衍生项目与官方 Nanobrowser 项目及核心维护团队无任何关联，亦不由其维护或背书。**

**对于因使用第三方衍生项目而导致的任何损失、损坏或问题，我们不承担任何责任。用户需自行承担与此类项目交互的风险。**

**我们保留公开声明与任何滥用或误导性使用我们名称、代码库或品牌的行为划清界限的权利。**

我们鼓励开源创新，但恳请社区保持审慎。在使用由独立开发者基于我们的代码库构建的任何软件或服务前，请务必充分了解相关风险。