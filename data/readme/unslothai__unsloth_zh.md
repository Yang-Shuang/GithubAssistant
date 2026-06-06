<h1 align="center" style="margin:0;">
  <a href="https://unsloth.ai/docs"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20logo%20white%20text.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20logo%20black%20text.png">
    <img alt="Unsloth logo" src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20logo%20black%20text.png" height="80" style="max-width:100%;">
  </picture></a>
</h1>
<h3 align="center" style="margin: 0; margin-top: 0;">
Unsloth Studio 允许你在本地运行和训练模型。
</h3>

<p align="center">
  <a href="#-features">功能特性</a> •
  <a href="#-install">快速开始</a> •
  <a href="#-free-notebooks">Notebook（笔记本）</a> •
  <a href="https://unsloth.ai/docs">文档</a>
</p>
<br>
<a href="https://unsloth.ai/docs/new/studio">
<img alt="unsloth studio ui homepage" src="https://github.com/user-attachments/assets/53ae17a9-d975-44ef-9686-efb4ebd0454d" style="max-width: 100%; margin-bottom: 0;"></a>

## ⚡ 快速开始

#### macOS, Linux, WSL:
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```
#### Windows:
```powershell
irm https://unsloth.ai/install.ps1 | iex
```
#### 社区：

- [Discord](https://discord.gg/unsloth)
- [𝕏 (Twitter)](https://x.com/UnslothAI)
- [Reddit](https://reddit.com/r/unsloth)

## ⭐ 功能特性
Unsloth Studio（测试版）支持在 Windows、Linux 和 macOS 上运行并训练文本、[音频](https://unsloth.ai/docs/basics/text-to-speech-tts-fine-tuning)、[嵌入模型(embedding)](https://unsloth.ai/docs/new/embedding-finetuning)、[视觉(vision)](https://unsloth.ai/docs/basics/vision-fine-tuning) 模型。

### 推理 (Inference)
* **搜索、下载和运行模型**：支持 GGUF、LoRA 适配器、safetensors 格式
* **导出模型**：将模型[保存或导出](https://unsloth.ai/docs/new/studio/export)为 GGUF、16位 safetensors 及其他格式。
* **工具调用 (Tool Calling)**：支持[自我修复工具调用](https://unsloth.ai/docs/new/studio/chat#auto-healing-tool-calling)和网页搜索
* **[代码执行](https://unsloth.ai/docs/new/studio/chat#code-execution)**：让 LLM 在 Claude artifacts 和沙箱环境中测试代码
* **[API 推理端点 (Inference Endpoint)](https://unsloth.ai/docs/basics/api)**：使用 Unsloth 在 Claude Code、Codex 工具中部署并运行本地 LLM
* [自动设置推理参数](https://unsloth.ai/docs/new/studio/chat#auto-parameter-tuning)并自定义聊天模板。
* 我们与 [gpt-oss](https://docs.unsloth.ai/new/gpt-oss-how-to-run-and-fine-tune#unsloth-fixes-for-gpt-oss)、[Qwen3](https://www.reddit.com/r/LocalLLaMA/comments/1kaodxu/qwen3_unsloth_dynamic_ggufs_128k_context_bug_fixes/)、[Llama 4](https://github.com/ggml-org/llama.cpp/pull/12889)、[Mistral](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/discussions/18)、[Gemma 1-3](https://news.ycombinator.com/item?id=39671146) 和 [Phi-4](https://unsloth.ai/blog/phi4) 背后的团队直接合作，修复了提升模型准确率的 bug。
* 支持图像、音频、PDF、代码、DOCX 等格式的对话。[连接 API 提供商](https://unsloth.ai/docs/integrations/connections)（OpenAI、Anthropic）或服务器（vLLM、Ollama）。

### 训练 (Training)
* 训练和强化学习(RL) **500+ 个模型**，速度提升高达 **2倍**，显存(VRAM)占用减少达 **70%**，且无精度损失。
* 自定义 Triton 与数学**内核(Kernels)**。查看我们与 [PyTorch](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) 和 [Hugging Face](https://unsloth.ai/docs/new/faster-moe) 的合作成果。
* **数据配方(Data Recipes)**：[自动创建数据集](https://unsloth.ai/docs/new/studio/data-recipe)，支持从 PDF、CSV、DOCX 等格式转换。通过可视化节点工作流编辑数据。
* **[强化学习 (Reinforcement Learning, RL)](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)**：目前最高效的 [RL](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) 库，使用 GRPO、[FP8](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) 等技术可将显存占用降低 **80%**。
* 支持全量微调、强化学习、预训练、4-bit、16-bit 及 FP8 训练。
* **可观测性 (Observability)**：实时监控训练过程，跟踪损失(Loss)和 GPU 使用情况，并可自定义图表。
* [多GPU(Multi-GPU)](https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth) 训练现已支持，近期将有重大改进。

## 📥 安装
Unsloth 支持两种使用方式：通过 **[Unsloth Studio](https://unsloth.ai/docs/new/studio/)**（Web UI）或 **Unsloth Core**（代码版）。两者要求不同。

### Unsloth Studio（Web UI）
Unsloth Studio（测试版）支持在 Windows、Linux、WSL 和 macOS 上运行。

* **CPU：** 目前支持聊天(Chat)和数据配方(Data Recipes)功能
* **NVIDIA：** 训练支持 RTX 30/40/50、Blackwell、DGX Spark、Station 等显卡
* **macOS：** 全面支持训练、MLX 推理和 GGUF 推理。
* **AMD：** 聊天与数据功能可用。训练请使用 [Unsloth Core](#unsloth-core-code-based)。Studio 支持即将推出。
* **多GPU(Multi-GPU)：** 现已提供，重大升级即将到来

#### macOS, Linux, WSL:
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```
使用相同命令进行更新。

#### Windows:
```powershell
irm https://unsloth.ai/install.ps1 | iex
```
使用相同命令进行更新。

#### 启动 (Launch)
```bash
unsloth studio -p 8888
```
如需云端或全局访问，请添加 `-H 0.0.0.0`。默认情况下，Unsloth 仅支持本地访问。

#### Docker
使用我们的 [Docker 镜像](https://hub.docker.com/r/unsloth/unsloth) `unsloth/unsloth` 容器运行：
```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
```

#### 开发者版、Nightly（每日构建）、卸载
查看开发者版、Nightly 版本及卸载等说明，请参阅 [高级安装](#-advanced-installation)。

### Unsloth Core（代码版）
#### Linux, WSL:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv unsloth_env --python 3.13
source unsloth_env/bin/activate
uv pip install unsloth --torch-backend=auto
```
#### Windows:
```powershell
winget install -e --id Python.Python.3.13
winget install --id=astral-sh.uv  -e
uv venv unsloth_env --python 3.13
.\unsloth_env\Scripts\activate
uv pip install unsloth --torch-backend=auto
```
在 Windows 上，仅当你已安装 PyTorch 时才能使用 `pip install unsloth`。请阅读我们的 [Windows 指南](https://unsloth.ai/docs/get-started/install/windows-installation)。你可以使用与 Unsloth Studio 相同的 Docker 镜像。

#### AMD, Intel:
对于 RTX 50x、B200、6000 系列显卡：`uv pip install unsloth --torch-backend=auto`。请阅读我们的指南：[Blackwell](https://unsloth.ai/docs/blog/fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth) 和 [DGX Spark](https://unsloth.ai/docs/blog/fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth)。 <br>
要在 **AMD** 和 **Intel** GPU 上安装 Unsloth，请参阅我们的 [AMD 指南](https://unsloth.ai/docs/get-started/install/amd) 和 [Intel 指南](https://unsloth.ai/docs/get-started/install/intel)。

## 📒 免费 Notebook（笔记本）

使用我们的 Notebook 免费进行训练。你可以通过全新的[免费 Unsloth Studio Notebook](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb)在 Web UI 中免费运行和训练模型。阅读我们的[指南](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide)，添加数据集、运行推理，然后部署你的训练模型。

| **模型** | **免费 Notebook** | **性能提升** | **显存占用减少** |
|-----------|---------|--------|----------|
| **Gemma 4 (E2B)**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_(E2B)-Vision.ipynb)               | 快 1.5 倍 | 降低 50% |
| **Qwen3.5 (4B)**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_(4B)_Vision.ipynb)               | 快 1.5 倍 | 降低 60% |
| **gpt-oss (20B)**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-(20B)-Fine-tuning.ipynb)               | 快 2 倍 | 降低 70% |
| **Qwen3.5 GSPO**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_(4B)_Vision_GRPO.ipynb)               | 快 2 倍 | 降低 70% |
| **gpt-oss (20B): GRPO**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-(20B)-GRPO.ipynb)               | 快 2 倍 | 降低 80% |
| **Qwen3: Advanced GRPO**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(4B)-GRPO.ipynb)               | 快 2 倍 | 降低 70% |
| **embeddinggemma (300M)**    | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/EmbeddingGemma_(300M).ipynb)               | 快 2 倍 | 降低 20% |
| **Mistral Ministral 3 (3B)**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_VL_(3B)_Vision.ipynb)               | 快 1.5 倍 | 降低 60% |
| **Llama 3.1 (8B) Alpaca**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb)               | 快 2 倍 | 降低 70% |
| **Llama 3.2 Conversational**      | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(1B_and_3B)-Conversational.ipynb)               | 快 2 倍 | 降低 70% |
| **Orpheus-TTS (3B)**     | [▶️ 免费开始](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Orpheus_(3B)-TTS.ipynb)               | 快 1.5 倍 | 降低 50% |

- 查看所有 Notebook：[Kaggle](https://github.com/unslothai/notebooks?tab=readme-ov-file#-kaggle-notebooks)、[GRPO](https://unsloth.ai/docs/get-started/unsloth-notebooks#grpo-reasoning-rl-notebooks)、[TTS](https://unsloth.ai/docs/get-started/unsloth-notebooks#text-to-speech-tts-notebooks)、[embedding](https://unsloth.ai/docs/new/embedding-finetuning) 与 [Vision](https://unsloth.ai/docs/get-started/unsloth-notebooks#vision-multimodal-notebooks)
- 查看[所有模型](https://unsloth.ai/docs/get-started/unsloth-model-catalog)和[所有 Notebook](https://unsloth.ai/docs/get-started/unsloth-notebooks)
- 在此查阅 Unsloth 详细文档：[https://unsloth.ai/docs](https://unsloth.ai/docs)

## 🦥 Unsloth 动态
- **连接 (Connections)**：接入任意 API 提供商（OpenAI、Anthropic）或服务器（vLLM、Ollama）。[指南](https://unsloth.ai/docs/integrations/connections)
- **MTP**：在 Unsloth 中运行 Qwen3.6 MTP。MTP 设置会根据你的硬件自动配置。[指南](https://unsloth.ai/docs/models/qwen3.6#mtp-guide)
- **API 推理端点 (Inference Endpoint)**：在 Claude Code、Codex 工具中部署并运行本地 LLM。[指南](https://unsloth.ai/docs/basics/api)
- **Qwen3.6**：现在可在 Unsloth Studio 中训练和运行 Qwen3.6-35B-A3B。[博客](https://unsloth.ai/docs/models/qwen3.6)
- **Gemma 4**：直接在 Unsloth 中运行并训练 Google 的新模型。[博客](https://unsloth.ai/docs/models/gemma-4)
- **推出 Unsloth Studio**：我们全新的用于运行和训练 LLM 的 Web UI。[博客](https://unsloth.ai/docs/new/studio)
- **Qwen3.5** - 现已支持 0.8B、2B、4B、9B、27B、35-A3B、112B-A10B 版本。[指南与 Notebook](https://unsloth.ai/docs/models/qwen3.5/fine-tune)
- **MoE LLM**：训练 MoE 大语言模型速度提升 **12倍**，显存占用减少 **35%** —— DeepSeek、GLM、Qwen 和 gpt-oss。[博客](https://unsloth.ai/docs/new/faster-moe)
- **Embedding 模型**：Unsloth 现已支持快约 1.8~3.3 倍的 embedding 微调。[博客](https://unsloth.ai/docs/new/embedding-finetuning) • [Notebook](https://unsloth.ai/docs/get-started/unsloth-notebooks#embedding-models)
- **长上下文强化学习 (RL)**：通过全新的批处理算法，上下文长度提升达 **7倍**。[博客](https://unsloth.ai/docs/new/grpo-long-context)
- **新型 RoPE 与 MLP Triton 内核(Kernels)及 Padding Free + Packing**：训练速度提升 **3倍**，显存占用减少 **30%**。[博客](https://unsloth.ai/docs/new/3x-faster-training-packing)
- **500K 上下文 (500K Context)**：现在可在 80GB 显存的 GPU 上训练拥有超过 500K 上下文的 20B 模型。[博客](https://unsloth.ai/docs/blog/500k-context-length-fine-tuning)
- **FP8 与视觉强化学习 (Vision RL)**：现在可在消费级显卡上进行 FP8 和 VLM GRPO。[FP8 博客](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) • [视觉 RL](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/vision-reinforcement-learning-vlm-rl)

## 📥 高级安装
以下高级说明适用于 Unsloth Studio。如需 Unsloth Core 的高级安装指南，请[查看我们的文档](https://unsloth.ai/docs/get-started/install/pip-install#advanced-pip-installation)。

#### 开发者版安装：macOS, Linux, WSL:
```bash
git clone https://github.com/unslothai/unsloth
cd unsloth
./install.sh --local
unsloth studio -p 8888
```
随后进行更新：
```bash
cd unsloth && git pull
./install.sh --local
unsloth studio -p 8888
```

#### 开发者版安装：Windows PowerShell:
```powershell
git clone https://github.com/unslothai/unsloth.git
cd unsloth
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
unsloth studio -p 8888
```
随后进行更新：
```bash
cd unsloth && git pull
./install.sh --local
unsloth studio -p 8888
```

#### Nightly（每日构建）：MacOS, Linux, WSL:
```bash
git clone https://github.com/unslothai/unsloth
cd unsloth
git checkout nightly
./install.sh --local
unsloth studio -p 8888
```
随后每次启动运行：
```bash
unsloth studio -p 8888
```

#### Nightly（每日构建）：Windows:
在 Windows Powershell 中运行：
```powershell
git clone https://github.com/unslothai/unsloth.git
cd unsloth
git checkout nightly
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
unsloth studio -p 8888
```
随后每次启动运行：
```bash
unsloth studio -p 8888
```

#### 高级启动选项
安装程序选项可通过环境变量传递。在 macOS、Linux 和 WSL 上，将变量放在管道符 `|` 之后以便 shell 传递给 `sh`；在 Windows 上使用 `$env:` 设置后再通过管道传递给 `iex`。

跳过 PyTorch（仅 GGUF 模式）：
```bash
curl -fsSL https://unsloth.ai/install.sh | UNSLOTH_NO_TORCH=1 sh
```
```powershell
$env:UNSLOTH_NO_TORCH=1; irm https://unsloth.ai/install.ps1 | iex
```

固定 Python 版本：
```bash
curl -fsSL https://unsloth.ai/install.sh | UNSLOTH_PYTHON=3.12 sh
```
```powershell
$env:UNSLOTH_PYTHON='3.12'; irm https://unsloth.ai/install.ps1 | iex
```

通过 `UNSLOTH_STUDIO_HOME` 安装到自定义路径：
```bash
curl -fsSL https://unsloth.ai/install.sh | UNSLOTH_STUDIO_HOME=/abs/path sh
```
```powershell
$env:UNSLOTH_STUDIO_HOME='C:\path'; irm https://unsloth.ai/install.ps1 | iex
```

**限制高核心主机上 Studio 原生 CPU 线程池**：`UNSLOTH_CPU_THREADS=8 unsloth studio -p 8888`。

#### 卸载
完全卸载 Unsloth Studio 的推荐方法是使用与你操作系统匹配的卸载脚本。它会停止正在运行的服务器、移除安装目录、启动器数据目录、桌面快捷方式，以及任何平台特定的条目（macOS `.app` 包 + Mac Launch Services；Windows 开始菜单、`HKCU\Software\Unsloth` 注册表项和用户 `PATH` 条目）：

* **MacOS, WSL, Linux：** `curl -fsSL https://raw.githubusercontent.com/unslothai/unsloth/main/scripts/uninstall.sh | sh`
* **Windows（PowerShell）：** `irm https://raw.githubusercontent.com/unslothai/unsloth/main/scripts/uninstall.ps1 | iex`

如果只想删除安装目录并保留启动器/快捷方式以便稍后重新安装，可改为运行 `rm -rf ~/.unsloth/studio` (Mac/Linux/WSL) 或 `Remove-Item -Recurse -Force "$HOME\.unsloth\studio"` (Windows)。`~/.cache/huggingface` 中的模型缓存不会受此影响。

更多信息，[请参阅我们的文档](https://unsloth.ai/docs/new/studio/install#uninstall)。

#### 删除模型文件

你可以通过模型搜索栏中的 bin 图标删除旧模型文件，或从默认的 Hugging Face 缓存目录中移除对应的缓存文件夹。默认情况下，HF 使用：

* **MacOS, Linux, WSL：** `~/.cache/huggingface/hub/`
* **Windows：** `%USERPROFILE%\.cache\huggingface\hub\`

## 💚 社区与链接
| 类型                                                                                                                                      | 链接                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| <img width="16" src="https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/66e3d80db9971f10a9757c99_Symbol.svg" />  **Discord**                       | [加入 Discord 服务器](https://discord.com/invite/unsloth)                          |
| <img width="15" src="https://redditinc.com/hs-fs/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png" />  **r/unsloth Reddit**                       | [加入 Reddit 社区](https://reddit.com/r/unsloth)                          |
| 📚 **文档与 Wiki**                                                                                                               | [阅读我们的文档](https://unsloth.ai/docs)                                       |
| <img width="13" src="https://upload.wikimedia.org/wikipedia/commons/0/09/X_(formerly_Twitter)_logo_late_2025.svg" />  **Twitter (即 X)** | [在 X 上关注我们](https://twitter.com/unslothai)                                |
| 🔮 **我们的模型**                                                                                                                         | [Unsloth 模型目录](https://unsloth.ai/docs/get-started/unsloth-model-catalog)   |
| ✍️ **博客**                                                                                                                               | [阅读我们的博客](https://unsloth.ai/blog)                                      |

### 引用

你可以通过以下方式引用 Unsloth 仓库：
```bibtex
@software{unsloth,
  author = {Daniel Han, Michael Han and Unsloth team},
  title = {Unsloth},
  url = {https://github.com/unslothai/unsloth},
  year = {2023}
}
```
如果你使用 🦥Unsloth 训练了模型，可以使用这个很酷的贴纸！ <img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/made with unsloth.png" width="200" align="center" />

### 许可证
Unsloth 采用 Apache 2.0 和 AGPL-3.0 双重许可模式。核心 Unsloth 包仍遵循 **[Apache 2.0](https://github.com/unslothai/unsloth?tab=Apache-2.0-1-ov-file)** 许可证，而部分可选组件（如 Unsloth Studio UI）则采用开源许可证 **[AGPL-3.0](https://github.com/unslothai/unsloth?tab=AGPL-3.0-2-ov-file)**。

这种许可结构有助于支持 Unsloth 的持续开发，同时保持项目开源并促进更广泛生态系统的持续发展。

### 致谢
- [llama.cpp 库](https://github.com/ggml-org/llama.cpp)：让用户能够使用 Unsloth 运行和保存模型
- Hugging Face 团队及其库：[transformers](https://github.com/huggingface/transformers) 和 [TRL](https://github.com/huggingface/trl)
- PyTorch 和 [Torch AO](https://github.com/unslothai/unsloth/pull/3391) 团队对项目的贡献
- NVIDIA 对其 [NeMo DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner) 库及所做贡献的支持
- 当然，还有每一位为 Unsloth 做出贡献或使用过它的开发者！