## Void 现已弃用。
Void 已正式停止维护，且不再接受任何贡献。
感谢所有通过编写代码或提供社区支持做出贡献的伙伴。Void 仍保持开源，并且在你 fork（分叉）VS Code 时，它依然是极佳的参考项目之一。


## 下载

如需查看更新的 Void 分叉版本列表，请参阅 [Void Forks](http://github.com/voideditor/void-forks/)。

如需下载旧版 Void，请参阅 [Releases（发行版本）](https://github.com/voideditor/void/releases)。

## 分叉（Fork）VS Code

如果你正在 fork VS Code，可能仍需要参考 Void 的设计逻辑。请查阅我们的 [代码库指南（Codebase Guide）](https://github.com/voideditor/void/blob/main/VOID_CODEBASE_GUIDE.md) 和 [如何贡献（How to Contribute）](https://github.com/voideditor/void/blob/main/HOW_TO_CONTRIBUTE.md)。

- 我们集成了 React + Tailwind。这在原生 VS Code 中无法直接实现，因此我们需要扩展构建流水线（build pipeline），以编译 React 并自行处理 [Tailwind 作用域化](https://github.com/andrewpareles/scope-tailwind)。

- 你可以直接复用我们的 GitHub Actions 工作流，用于打包、签名和自动更新 Void。由于 VS Code 的构建流水线是私有的，自行实现这一流程通常非常困难。

- 我们的 AI 服务提供者（AI provider）代码完全从零构建，从而支持自动补全（中间填充/FIM）及其他自定义响应。我们公开了常见 `<thinking>` 标签、工具调用标签等的语法解析器。你可以自由参考我们在架构层面使用 IPC（进程间通信）并满足 CSP（内容安全策略）的实现方式。

- 使用我们自定义的服务来编辑文件。`EditCodeService` 允许你将代码差异（diff）以流式形式实时展示，甚至支持逐 token（词元）渲染。`VoidModelService` 则支持在后台编辑文件，并将操作系统层面的文件与你的文本缓冲区进行同步。

- 我们所做的一切均为 100% 开源。请参阅 [仓库列表（repos）](https://github.com/orgs/voideditor/repositories)，以全面了解构成 Void 的所有项目仓库。



# 欢迎使用 Void。

<div align="center">
	<img
		src="./src/vs/workbench/browser/parts/editor/media/slice_of_void.png"
	 	alt="Void Welcome"
		width="300"
	 	height="300"
	/>
</div>

在你的代码库上使用 AI Agent（智能体），通过检查点记录并可视化变更，同时支持在本地运行任意模型或使用自建托管服务。Void 会直接将消息发送至服务提供商，不会留存你的任何数据。

本仓库包含 Void 桌面版应用的完整源代码。如果你是新用户，欢迎加入！

- 🧭 [官网](https://voideditor.com)

- 🚙 [路线图](https://github.com/orgs/voideditor/projects/2)

- 🔨 [参与贡献](https://github.com/voideditor/void/blob/main/HOW_TO_CONTRIBUTE.md)




## 参考资料

Void 是 [vscode](https://github.com/microsoft/vscode) 仓库的一个分叉版本。如需了解我们的代码库结构，请参阅 [VOID_CODEBASE_GUIDE（代码库指南）](https://github.com/voideditor/void/blob/main/VOID_CODEBASE_GUIDE.md)。

如需了解如何开发你自己的 Void 版本，请参阅 [HOW_TO_CONTRIBUTE（贡献指南）](https://github.com/voideditor/void/blob/main/HOW_TO_CONTRIBUTE.md) 以及 [void-builder](https://github.com/voideditor/void-builder)。



## 获取帮助
你随时可以通过我们的 [Discord 服务器](https://discord.gg/RSNjgaugJs) 联系我们，或发送邮件至 hello@voideditor.com。