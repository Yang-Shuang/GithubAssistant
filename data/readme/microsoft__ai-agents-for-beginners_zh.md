# AI Agent 入门课程

![AI Agents for Beginners](./images/repo-thumbnailv2.png)

## 一门教你掌握构建 AI Agent 所需全部知识的课程

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 多语言支持

#### 通过 GitHub Action 支持（自动同步，始终保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./translations/ar/README.md) | [Bengali](./translations/bn/README.md) | [Bulgarian](./translations/bg/README.md) | [Burmese (Myanmar)](./translations/my/README.md) | [Chinese (Simplified)](./translations/zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](./translations/zh-HK/README.md) | [Chinese (Traditional, Macau)](./translations/zh-MO/README.md) | [Chinese (Traditional, Taiwan)](./translations/zh-TW/README.md) | [Croatian](./translations/hr/README.md) | [Czech](./translations/cs/README.md) | [Danish](./translations/da/README.md) | [Dutch](./translations/nl/README.md) | [Estonian](./translations/et/README.md) | [Finnish](./translations/fi/README.md) | [French](./translations/fr/README.md) | [German](./translations/de/README.md) | [Greek](./translations/el/README.md) | [Hebrew](./translations/he/README.md) | [Hindi](./translations/hi/README.md) | [Hungarian](./translations/hu/README.md) | [Indonesian](./translations/id/README.md) | [Italian](./translations/it/README.md) | [Japanese](./translations/ja/README.md) | [Kannada](./translations/kn/README.md) | [Khmer](./translations/km/README.md) | [Korean](./translations/ko/README.md) | [Lithuanian](./translations/lt/README.md) | [Malay](./translations/ms/README.md) | [Malayalam](./translations/ml/README.md) | [Marathi](./translations/mr/README.md) | [Nepali](./translations/ne/README.md) | [Nigerian Pidgin](./translations/pcm/README.md) | [Norwegian](./translations/no/README.md) | [Persian (Farsi)](./translations/fa/README.md) | [Polish](./translations/pl/README.md) | [Portuguese (Brazil)](./translations/pt-BR/README.md) | [Portuguese (Portugal)](./translations/pt-PT/README.md) | [Punjabi (Gurmukhi)](./translations/pa/README.md) | [Romanian](./translations/ro/README.md) | [Russian](./translations/ru/README.md) | [Serbian (Cyrillic)](./translations/sr/README.md) | [Slovak](./translations/sk/README.md) | [Slovenian](./translations/sl/README.md) | [Spanish](./translations/es/README.md) | [Swahili](./translations/sw/README.md) | [Swedish](./translations/sv/README.md) | [Tagalog (Filipino)](./translations/tl/README.md) | [Tamil](./translations/ta/README.md) | [Telugu](./translations/te/README.md) | [Thai](./translations/th/README.md) | [Turkish](./translations/tr/README.md) | [Ukrainian](./translations/uk/README.md) | [Urdu](./translations/ur/README.md) | [Vietnamese](./translations/vi/README.md)

> **更倾向于本地克隆？**
>
> 该仓库包含 50 多种语言的翻译，这会显著增加下载体积。若需不下载翻译内容，请使用稀疏检出（sparse checkout）：
>
> **Bash / macOS / Linux：**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows)：**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 这将为你提供完成课程所需的一切资源，同时大幅加快下载速度。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果你希望支持更多翻译语言，请参阅[此列表](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)。**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 入门指南

本课程包含讲解构建 AI Agent 基础知识的章节。每节课涵盖独立主题，你可以从任意一节开始学习！

本课程支持多语言阅读。请前往[此处查看可用语言列表](#-多语言支持)。 

如果你是首次使用生成式 AI（GenAI）模型进行开发，推荐你先学习我们的[《面向初学者的生成式 AI》](https://aka.ms/genai-beginners)课程，其中包含 21 节关于构建 GenAI 应用的教程。

别忘了[收藏（🌟）此仓库](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)并 [Fork 本仓库](https://github.com/microsoft/ai-agents-for-beginners/fork)以运行代码。

### 结识其他学员，解答你的疑问

如果你在构建 AI Agent 时遇到困难或有任何疑问，欢迎加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 中的专属频道。

### 你需要准备什么 

本课程每节课均包含代码示例，位于 `code_samples` 文件夹中。你可以 [Fork 此仓库](https://github.com/microsoft/ai-agents-for-beginners/fork) 创建自己的副本。  

本练习中的代码示例使用了结合 Azure AI Foundry Agent Service V2 的 Microsoft Agent Framework：

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - 需要 Azure 账户

本课程使用了微软提供的以下 AI Agent 框架与服务：

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

部分代码示例还支持其他兼容 OpenAI 的提供商，例如提供大上下文模型（最高支持 204K token）的 [MiniMax](https://platform.minimaxi.com/)。配置详情请参阅[课程环境设置](./00-course-setup/README.md)。

有关运行本课程代码的更多信息，请前往[课程环境设置](./00-course-setup/README.md)。

## 🙏 想要提供帮助？

如果你有建议或发现了拼写及代码错误？请[提交 Issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) 或 [创建 Pull Request](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)

## 📂 每节课包含的内容

- README 中的文字教程及简短视频
- 使用结合 Azure AI Foundry 的 Microsoft Agent Framework 编写的 Python 代码示例
- 用于继续学习的额外资源链接


## 🗃️ 课程列表

| **课程章节**                                   | **文字与代码**                                    | **视频**                                                  | **拓展学习**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI Agent 简介与应用场景       | [链接](./01-intro-to-ai-agents/README.md)          | [视频](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 探索 AI 智能体框架              | [链接](./02-explore-agentic-frameworks/README.md)  | [视频](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 理解 AI 智能体设计模式     | [链接](./03-agentic-design-patterns/README.md)     | [视频](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 工具调用设计模式                      | [链接](./04-tool-use/README.md)                    | [视频](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 智能体增强检索生成（Agentic RAG）                                  | [链接](./05-agentic-rag/README.md)                 | [视频](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 构建可信的 AI Agent               | [链接](./06-building-trustworthy-agents/README.md) | [视频](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 规划设计模式                      | [链接](./07-planning-design/README.md)             | [视频](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 多智能体设计模式                   | [链接](./08-multi-agent/README.md)                 | [视频](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 元认知设计模式                 | [链接](./09-metacognition/README.md)               | [视频](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 生产环境中的 AI Agent                      | [链接](./10-ai-agents-production/README.md)        | [视频](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 使用智能体协议（MCP、A2A 和 NLWeb） | [链接](./11-agentic-protocols/README.md)           | [视频](https://youtu.be/X-Dh9R3Opn8)                                 | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI Agent 上下文工程            | [链接](./12-context-engineering/README.md)         | [视频](https://youtu.be/F5zqRV7gEag)                                 | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 管理智能体记忆                      | [链接](./13-agent-memory/README.md)     |      [视频](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| 探索 Microsoft Agent Framework                         | [链接](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| 构建计算机操作智能体（CUA）           | [链接](./15-browser-use/README.md)     |                                                            | [链接](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| 部署可扩展的智能体                    | 即将推出                            |                                                            |                                                                                        |
| 创建本地 AI Agent                     | 即将推出                               |                                                            |                                                                                        |
| 保护 AI Agent                           | [链接](./18-securing-ai-agents/README.md)  |                                                            | [链接](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 其他课程

我们的团队还推出了其他课程！欢迎查看：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 社区致谢

感谢 [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) 贡献了展示智能体增强检索生成（Agentic RAG）的重要代码示例。 

## 贡献指南

本项目欢迎各类贡献与建议。大多数贡献需要你同意签署贡献者许可协议（CLA），声明你有权且确实授予我们使用你贡献的权利。详情请访问 <https://cla.opensource.microsoft.com>。

当你提交 Pull Request 时，CLA 机器人将自动判断你是否需要签署协议，并相应地处理 PR（例如状态检查、评论）。只需按照机器人提供的指示操作即可。使用我们 CLA 的所有仓库中你只需执行一次此操作。

本项目已采用[微软开源行为准则](https://opensource.microsoft.com/codeofconduct/)。如需更多信息，请参阅[行为准则常见问题解答](https://opensource.microsoft.com/codeofconduct/faq/)，或就其他问题与意见联系 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 商标声明

本项目可能包含特定项目、产品或服务中的商标或徽标。微软商标或徽标的授权使用须遵守并遵循
[《微软商标与品牌指南》](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。
对本项目的修改版本中不得使用微软商标或徽标，以免造成混淆或暗示微软的赞助关系。使用任何第三方商标或徽标均受该第三方政策约束。

## 获取帮助

如果你在构建 AI 应用时遇到困难或有任何疑问，欢迎加入：

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

如果你有产品反馈或在开发过程中遇到问题，请访问：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)