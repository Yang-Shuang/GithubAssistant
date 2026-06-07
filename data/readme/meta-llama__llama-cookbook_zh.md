<h1 align="center"> Llama Cookbook </h1>
<p align="center">
	<a href="https://llama.developer.meta.com/join_waitlist?utm_source=llama-cookbook&utm_medium=readme&utm_campaign=main"><img src="https://img.shields.io/badge/Llama_API-Join_Waitlist-brightgreen?logo=meta" /></a>
	<a href="https://llama.developer.meta.com/docs?utm_source=llama-cookbook&utm_medium=readme&utm_campaign=main"><img src="https://img.shields.io/badge/Llama_API-Documentation-4BA9FE?logo=meta" /></a>

</p>
<p align="center">
	<a href="https://github.com/meta-llama/llama-models/blob/main/models/?utm_source=llama-cookbook&utm_medium=readme&utm_campaign=main"><img alt="Llama Model cards" src="https://img.shields.io/badge/Llama_OSS-Model_cards-green?logo=meta" /></a>
	<a href="https://www.llama.com/docs/overview/?utm_source=llama-cookbook&utm_medium=readme&utm_campaign=main"><img alt="Llama Documentation" src="https://img.shields.io/badge/Llama_OSS-Documentation-4BA9FE?logo=meta" /></a>
	<a href="https://huggingface.co/meta-llama"><img alt="Hugging Face meta-llama" src="https://img.shields.io/badge/Hugging_Face-meta--llama-yellow?logo=huggingface" /></a>

</p>
<p align="center">
	<a href="https://github.com/meta-llama/synthetic-data-kit"><img alt="Llama Tools Syntethic Data Kit" src="https://img.shields.io/badge/Llama_Tools-synthetic--data--kit-orange?logo=meta" /></a>
	<a href="https://github.com/meta-llama/llama-prompt-ops"><img alt="Llama Tools Syntethic Data Kit" src="https://img.shields.io/badge/Llama_Tools-llama--prompt--ops-orange?logo=meta" /></a>
</p>
<h2> 使用 Llama 构建的官方指南 </h2>



欢迎进入本官方仓库，它将帮助你快速上手基于 Llama 模型系列进行[推理](https://github.com/meta-llama/llama-cookbook/tree/main/getting-started/inference/)、[微调](https://github.com/meta-llama/llama-cookbook/tree/main/getting-started/finetuning)以及构建[端到端用例](https://github.com/meta-llama/llama-cookbook/tree/main/end-to-end-use-cases)。

本仓库涵盖了社区中最流行的方法、应用场景，以及针对 Llama 文本与视觉模型的最新实践指南（Recipes）。

## 最新 Llama 4 实践指南

* [快速入门](./getting-started/build_with_llama_api.ipynb)：使用 [Llama API](https://bit.ly/llama-api-main)
* 将 [Llama API](https://bit.ly/llama-api-main) 与 [WhatsApp](./end-to-end-use-cases/whatsapp_llama_4_bot/README.md) 集成
* 使用 [Llama 4 Scout](./getting-started/build_with_llama_4.ipynb) 处理 500万（5M）长上下文
* 使用 [Llama 4 Maverick](./end-to-end-use-cases/research_paper_analyzer/README.md) 分析研究论文
* 使用 [Llama 4 Maverick](./end-to-end-use-cases/book-character-mindmap/README.md) 从书籍中生成角色思维导图

## 仓库结构：

- [第三方集成 (3P Integrations)](https://github.com/meta-llama/llama-cookbook/tree/main/3p-integrations): 来自各 Llama 提供商的快速入门指南与端到端用例
- [端到端用例](https://github.com/meta-llama/llama-cookbook/tree/main/end-to-end-use-cases): 顾名思义，涵盖各个领域与应用场景
- [快速入门 (Getting Started)](https://github.com/meta-llama/llama-cookbook/tree/main/getting-started/): 推理、微调及 RAG（检索增强生成）示例参考
- [源码目录 (src)](https://github.com/meta-llama/llama-cookbook/tree/main/src/): 包含原始 `llama-recipes` 库的源代码，以及部分关于微调的常见问题解答。

> Note: 我们近期对仓库进行了重构，[archive-main](https://github.com/meta-llama/llama-cookbook/tree/archive-main) 分支为重构前的代码快照。

## FAQ：

- **问：** `llama-recipes` 发生了什么变化？
  **答：** 我们近期将 `llama-recipes` 更名为 `llama-cookbook`。

- **问：** 我有一些关于微调的问题，有专门的板块解答吗？
  **答：** 请查看此处[的微调常见问题解答](https://github.com/meta-llama/llama-cookbook/tree/main/src/docs/)。

- **问：** 部分链接失效或文件夹缺失：
  **答：** 我们近期对仓库进行了重构，[archive-main](https://github.com/meta-llama/llama-cookbook/tree/archive-main) 分支为重构前的代码快照。

- **问：** 在哪里可以查看最新模型的详细信息？
  **答：** 请访问官方 [Llama 模型网站](https://www.llama.com)。

## Contributing

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，了解我们的行为准则以及向我们提交 Pull Request（PR）的流程。

## License
<!-- markdown-link-check-disable -->
Meta Llama 4 的许可证文件请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE)，可接受使用政策（Acceptable Use Policy）请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama4/USE_POLICY.md)

Meta Llama 3.3 的许可证文件请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE)，可接受使用政策（Acceptable Use Policy）请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/USE_POLICY.md)

Meta Llama 3.2 的许可证文件请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE)，可接受使用政策（Acceptable Use Policy）请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/USE_POLICY.md)

Meta Llama 3.1 的许可证文件请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE)，可接受使用政策（Acceptable Use Policy）请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/USE_POLICY.md)

Meta Llama 3 的许可证文件请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3/LICENSE)，可接受使用政策（Acceptable Use Policy）请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama3/USE_POLICY.md)

Meta Llama 2 的许可证文件请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama2/LICENSE)，可接受使用政策（Acceptable Use Policy）请参见[此处](https://github.com/meta-llama/llama-models/blob/main/models/llama2/USE_POLICY.md)
<!-- markdown-link-check-enable -->