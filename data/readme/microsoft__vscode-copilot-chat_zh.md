> [!IMPORTANT]
> 本项目已移至主 VS Code 仓库，本仓库现已归档。
>
> 活跃开发继续在此进行：
> https://github.com/microsoft/vscode
>
> 请在 VS Code 仓库中提交 issue 和 pull request（PR）。

---

# GitHub Copilot - 你的自主 AI 结对编程伙伴

**[GitHub Copilot](https://code.visualstudio.com/docs/copilot/overview)** 是一款 AI 结对编程工具，彻底改变了你在 Visual Studio Code（VS Code）中的编码方式。

GitHub Copilot agent（智能体）能够端到端地处理完整的编码任务，自主规划工作、编辑文件、运行命令，并在遇到错误时进行自我修正。你还可以利用内联建议快速获得编码辅助，或使用内联聊天直接在编辑器中进行精确、专注的修改。

**立即注册 [GitHub Copilot Free](https://github.com/settings/copilot?utm_source=vscode-chat-readme&utm_medium=first&utm_campaign=2025mar-em-MSFT-signup)！**

![Working with GitHub Copilot agent mode to make edits to code in your workspace](https://github.com/microsoft/vscode-docs/raw/732b9599e49ee7034744a3e5b0485b7fb4bdf530/docs/copilot/images/getting-started/custom-reviewer-mode.png)


## 获取 GitHub Copilot 访问权限

注册 [GitHub Copilot Free](https://github.com/settings/copilot?utm_source=vscode-chat-readme&utm_medium=second&utm_campaign=2025mar-em-MSFT-signup)，或向企业管理员申请访问权限。

要使用 GitHub Copilot，需要拥有有效的订阅。你可以在 [github.com/features/copilot](https://github.com/features/copilot?utm_source=vscode-chat&utm_medium=readme&utm_campaign=2025mar-em-MSFT-signup) 了解更多关于企业版和个人版的详情。

## 使用自主智能体进行开发

**让 AI 智能体端到端地实现复杂功能。** 向智能体提供一个高层任务，它会将工作分解为多个步骤，编辑多个文件，运行终端命令，并在遇到错误或测试失败时自我修正。智能体擅长 [构建新功能](https://code.visualstudio.com/docs/copilot/agents/overview)、[调试和修复失败的测试](https://code.visualstudio.com/docs/copilot/guides/debug-with-copilot)、重构代码库以及 [通过 pull request（PR）协作](https://code.visualstudio.com/docs/copilot/agents/cloud-agents)。

**从集中视图管理会话。** 并行运行多个 [智能体会话](https://code.visualstudio.com/docs/copilot/chat/chat-sessions) 并在一个地方跟踪它们。监控会话状态，在活跃工作之间切换，查看文件更改，并从中断处继续。

**使用你首选的框架运行智能体。** 可以在 VS Code 本地使用智能体，通过 Copilot CLI 在后台运行，或通过云端（Cloud）使用 Copilot Coding Agent。你还可以与 Claude、Codex 等提供商合作，并在 VS Code 内跨不同智能体类型交接任务，同时保留上下文信息。

![Video showing an agent session building a complete feature in VS Code.](https://github.com/microsoft/vscode-docs/raw/refs/heads/main/docs/copilot/images/overview/agents-intro.gif)

**使用 Plan 智能体在 [构建之前进行规划](https://code.visualstudio.com/docs/copilot/agents/planning)**，它将任务分解为结构化的实施计划并提出澄清问题。当计划准备好后，将其交给实现型智能体执行。你还可以 [将任务委派给云端智能体](https://code.visualstudio.com/docs/copilot/agents/cloud-agents)，它们会创建分支、实现更改并为你团队开启 pull request（PR）以供审查。

## 更多 AI 编码方式

**在输入时接收智能内联建议。** 通过 [幽灵文本建议（Ghost Text）](https://aka.ms/vscode-completions) 和 [下次编辑建议（Next Edit Suggestions）](https://aka.ms/vscode-nes)，帮助你更快地编写代码。Copilot 会预测你接下来的逻辑操作，你可以按 Tab 键接受建议。

![Video showing Copilot next edit suggestions.](https://github.com/microsoft/vscode-docs/raw/refs/heads/main/docs/copilot/images/inline-suggestions/nes-video.gif)

**使用内联聊天进行精准编辑。** 按下 `Ctrl+I`/`Cmd+I` 直接在编辑器中打开聊天提示。描述你的修改需求，Copilot 会就地建议编辑内容，例如重构方法、添加错误处理或解释复杂算法，无需离开编辑器。

![Inline chat in VS Code](https://code.visualstudio.com/assets/docs/copilot/copilot-chat/inline-chat-question-example.png)


## 根据你的工作流定制 AI

**当智能体了解你的项目规范并拥有合适的工具时，效果最佳。** 自定义 Copilot，使其从一开始就生成符合你代码库的代码。

**项目上下文（Project Context）。** 使用 [自定义指令](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) 指定全局或任务特定的上下文和编码规范。

**添加专用功能。** 通过 [智能体技能（Agent Skills）](https://code.visualstudio.com/docs/copilot/customization/agent-skills) 教授 Copilot 专用能力，或通过 [自定义智能体（Custom Agents）](https://code.visualstudio.com/docs/copilot/customization/custom-agents) 定义专业角色。

**连接外部工具和服务。** 通过 [MCP 服务器](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) 的工具和扩展进一步扩展智能体，为 Copilot 提供访问外部数据源、API 或专用工具的网关。

### 支持的语言和框架
GitHub Copilot 适用于任何语言，包括 Java、PHP、Python、JavaScript、Ruby、Go、C# 或 C++。由于它在公共仓库中的代码上进行了训练，因此对大多数流行的语言、库和框架都有效。

### 版本兼容性
由于深度集成 UI，Copilot Chat 的版本与 VS Code 同步发布。因此，每个新版 Copilot Chat 仅兼容最新发布的 VS Code 版本。这意味着如果你使用的是旧版 VS Code，将无法使用最新的 Copilot Chat。

只有最新的 Copilot Chat 版本才会使用 Copilot 服务提供的最新模型，因为即使是微小的模型升级也需要在扩展中进行提示词（Prompt）调整和修复。

### 隐私与预览条款
使用 Copilot Chat 即表示你同意 [GitHub Copilot 聊天预览版条款](https://docs.github.com/en/early-access/copilot/github-copilot-chat-technical-preview-license-terms)。请查阅 [透明度说明（Transparency Note）](https://aka.ms/CopilotChatTransparencyNote)，了解在技术预览期间的使用情况、限制条件以及改进 Copilot Chat 的方法。

请参阅我们的 [隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement) 以了解我们收集的数据、使用方式以及你可用的控制选项。

要获取最新的安全修复，请使用最新版本的 Copilot 扩展和 VS Code。

### 资源与后续步骤
* **[注册 GitHub Copilot Free](https://github.com/settings/copilot?utm_source=vscode-chat-readme&utm_medium=third&utm_campaign=2025mar-em-MSFT-signup)**：在升级到付费计划之前，免费体验 Copilot 的 AI 功能。
   * 如果你在企业环境中使用 Copilot，请查看 [Copilot Business](https://docs.github.com/en/copilot/copilot-business/about-github-copilot-business) 和 [Copilot Enterprise](https://docs.github.com/en/copilot/github-copilot-enterprise/overview/about-github-copilot-enterprise)。
* **[Copilot 快速入门](https://code.visualstudio.com/docs/copilot/getting-started)**：了解 VS Code 中 Copilot 的核心功能。
* **[智能体教程](https://code.visualstudio.com/docs/copilot/agents/agents-tutorial)**：在不同环境中开始使用自主智能体。
* **[YouTube 上的 VS Code](https://www.youtube.com/@code)**：在 VS Code 频道观看最新演示和更新。
* **[常见问题解答（FAQ）](https://code.visualstudio.com/docs/copilot/faq)**：获取关于 VS Code 中 Copilot 的常见问题的答案。
* **[提供反馈](https://github.com/microsoft/vscode-copilot-release/issues)**：发送你的反馈和功能请求，帮助我们改进 GitHub Copilot！

## 数据与遥测（Telemetry）

Visual Studio Code GitHub Copilot 扩展会收集使用情况数据并发送给 Microsoft，以帮助改进我们的产品与服务。阅读我们的 [隐私声明](https://privacy.microsoft.com/privacystatement) 了解更多详情。本扩展尊重 `telemetry.telemetryLevel` 设置，你可以通过 https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting 了解如何禁用遥测报告。

## 商标声明

本项目可能包含项目、产品或服务的商标或徽标。对 Microsoft 商标或徽标的授权使用须遵守并遵循 Microsoft 的《商标与品牌指南》。在本项目的修改版本中使用 Microsoft 商标或徽标不得引起混淆或暗示 Microsoft 赞助。任何第三方商标或徽标的使用均受限于该第三方的政策。

## 许可证

版权所有 (c) Microsoft Corporation。保留所有权利。

根据 [MIT](LICENSE.txt) 许可证授权。