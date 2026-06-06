<h1 align="center">GPT4All</h1>

<p align="center">
  现已支持 DeepSeek R1 蒸馏模型
</p>

<p align="center">
  <a href="https://www.nomic.ai/gpt4all">官网</a> &bull; <a href="https://docs.gpt4all.io">文档</a> &bull; <a href="https://discord.gg/mGZE39AS3e">Discord</a> &bull; <a href="https://www.youtube.com/watch?v=gQcZDXRVJok">YouTube 教程</a>
</p>

<p align="center">
  GPT4All 可在日常台式机和笔记本电脑上私有化运行大型语言模型（LLM）。
</p>
<p align="center">
  无需调用 API 或依赖 GPU——**你**只需下载应用程序即可 <a href="https://docs.gpt4all.io/gpt4all_desktop/quickstart.html#quickstart">开始使用</a>。
</p>

<p align="center">
  查看<a href="https://www.nomic.ai/blog/tag/gpt4all">我们的博客</a>了解最新动态。
</p>
<p align="center">
  <a href="https://nomic.ai/gpt4all/#newsletter-form">订阅新闻通讯</a>
</p>

https://github.com/nomic-ai/gpt4all/assets/70534565/513a0f15-4964-4109-89e4-4f9a9011f311

<p align="center">
GPT4All 得以实现，离不开我们的算力合作伙伴 <a href="https://www.paperspace.com/">Paperspace</a>。
</p>

## Download Links

<p>
  &mdash; <a href="https://gpt4all.io/installers/gpt4all-installer-win64.exe">
    <img src="gpt4all-bindings/python/docs/assets/windows.png" style="height: 1em; width: auto" /> Windows 安装程序
  </a> &mdash;
</p>
<p>
  &mdash; <a href="https://gpt4all.io/installers/gpt4all-installer-win64-arm.exe">
    <img src="gpt4all-bindings/python/docs/assets/windows.png" style="height: 1em; width: auto" /> Windows ARM 安装程序
  </a> &mdash;
</p>
<p>
  &mdash; <a href="https://gpt4all.io/installers/gpt4all-installer-darwin.dmg">
    <img src="gpt4all-bindings/python/docs/assets/mac.png" style="height: 1em; width: auto" /> macOS 安装程序
  </a> &mdash;
</p>
<p>
  &mdash; <a href="https://gpt4all.io/installers/gpt4all-installer-linux.run">
    <img src="gpt4all-bindings/python/docs/assets/ubuntu.svg" style="height: 1em; width: auto" /> Ubuntu 安装程序
  </a> &mdash;
</p>
<p>
Windows 和 Linux 版本需要 Intel Core i3 第二代或更高，或 AMD Bulldozer 架构及更高性能的处理器。
</p>
<p>
Windows ARM 版本支持高通骁龙（Qualcomm Snapdragon）以及微软 SQ1/SQ2 处理器。
</p>
<p>
Linux 版本仅支持 x86-64 架构（不支持 ARM）。
</p>
<p>
macOS 版本要求系统为 Monterey 12.6 或更高版本。在 Apple Silicon M 系列处理器上可获得最佳性能。
</p>

详见完整的 [System Requirements](gpt4all-chat/system_requirements.md) 以获取更多信息。

<br/>
<br/>
<p>
  <a href='https://flathub.org/apps/io.gpt4all.gpt4all'>
    <img style="height: 2em; width: auto" alt='Get it on Flathub' src='https://flathub.org/api/badge'><br/>
    Flathub（社区维护）
  </a>
</p>

## Install GPT4All Python

`gpt4all` 提供了基于 [`llama.cpp`](https://github.com/ggerganov/llama.cpp) 实现的 Python 客户端，让你能够轻松调用大型语言模型。 

Nomic 积极为 [`llama.cpp`](https://github.com/ggerganov/llama.cpp) 等开源软件做出贡献，致力于让 LLM 技术惠及大众并实现高效运行 **for all**。

```bash
pip install gpt4all
```

```python
from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
with model.chat_session():
    print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))
```


## Integrations

:parrot::link: [Langchain](https://python.langchain.com/v0.2/docs/integrations/providers/gpt4all/)
:card_file_box: [Weaviate Vector Database](https://github.com/weaviate/weaviate) - [module docs](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/text2vec-gpt4all)
:telescope: [OpenLIT (OTel-native Monitoring)](https://github.com/openlit/openlit) - [Docs](https://docs.openlit.io/latest/integrations/gpt4all)

## Release History
- **July 2nd, 2024**: V3.0.0 Release
    - Fresh redesign of the chat application UI
    - Improved user workflow for LocalDocs
    - Expanded access to more model architectures
- **October 19th, 2023**: GGUF Support Launches with Support for:
    - Mistral 7b base model, an updated model gallery on our website, several new local code models including Rift Coder v1.5
    - [Nomic Vulkan](https://blog.nomic.ai/posts/gpt4all-gpu-inference-with-vulkan) support for Q4\_0 and Q4\_1 quantizations in GGUF.
    - Offline build support for running old versions of the GPT4All Local LLM Chat Client.
- **September 18th, 2023**: [Nomic Vulkan](https://blog.nomic.ai/posts/gpt4all-gpu-inference-with-vulkan) launches supporting local LLM inference on NVIDIA and AMD GPUs.
- **July 2023**: Stable support for LocalDocs, a feature that allows you to privately and locally chat with your data.
- **June 28th, 2023**: [Docker-based API server] launches allowing inference of local LLMs from an OpenAI-compatible HTTP endpoint.

[Docker-based API server]: https://github.com/nomic-ai/gpt4all/tree/cef74c2be20f5b697055d5b8b506861c7b997fab/gpt4all-api

## Contributing
GPT4All welcomes contributions, involvement, and discussion from the open source community!
Please see CONTRIBUTING.md and follow the issues, bug reports, and PR markdown templates.

Check project discord, with project owners, or through existing issues/PRs to avoid duplicate work.
Please make sure to tag all of the above with relevant project identifiers or your contribution could potentially get lost.
Example tags: `backend`, `bindings`, `python-bindings`, `documentation`, etc.

## Citation

If you utilize this repository, models or data in a downstream project, please consider citing it with:
```
@misc{gpt4all,
  author = {Yuvanesh Anand and Zach Nussbaum and Brandon Duderstadt and Benjamin Schmidt and Andriy Mulyar},
  title = {GPT4All: Training an Assistant-style Chatbot with Large Scale Data Distillation from GPT-3.5-Turbo},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/nomic-ai/gpt4all}},
}
```