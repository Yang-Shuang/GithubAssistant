<div align="center" markdown="1">
   <sup>特别感谢：</sup>
   <br>
   <br>
   <a href="https://go.warp.dev/text-generation-webui">
      <img alt="Warp sponsorship" width="400" src="https://raw.githubusercontent.com/warpdotdev/brand-assets/refs/heads/main/Github/Sponsor/Warp-Github-LG-02.png">
   </a>

### [Warp，专为多 Agent 编程打造](https://go.warp.dev/text-generation-webui)
[适用于 macOS、Linux & Windows](https://go.warp.dev/text-generation-webui)<br>
</div>
<hr>

# TextGen

**一款面向本地大语言模型（LLM）的桌面应用。开源，无遥测数据收集。** 支持文本生成、视觉理解、工具调用和网页搜索。提供图形界面（UI）与应用程序接口（API）。

[![GitHub stars](https://img.shields.io/github/stars/oobabooga/textgen?style=for-the-badge&logo=github&logoColor=white&labelColor=black)](https://github.com/oobabooga/textgen)

[![Chat mode](https://raw.githubusercontent.com/oobabooga/screenshots/refs/heads/main/CHAT-4.8.png)](https://raw.githubusercontent.com/oobabooga/screenshots/refs/heads/main/CHAT-4.8.png)

## 1分钟快速上手

下载并解压后，双击运行 `textgen` 即可打开窗口。

**https://github.com/oobabooga/textgen/releases**

提供适用于 Linux、Windows 和 macOS 的便携版（免安装），支持 CUDA、Vulkan、ROCm 及纯 CPU 选项。已内置所有依赖项，兼容 GGUF（llama.cpp）模型格式。

如需使用其他后端（ExLlamaV3、Transformers）、训练功能、图像生成及扩展插件，请参阅[安装说明](#installation)。

## 功能特性

### 对话与文本生成

- ``instruct`` 模式用于指令跟随（类似 ChatGPT），以及 ``chat-instruct``/``chat`` 模式用于自定义角色对话。提示词会自动通过 Jinja2 模板进行格式化。
- **视觉（多模态）**：在消息中附加图片以实现图像理解功能（[教程](https://github.com/oobabooga/textgen/wiki/Multimodal-Tutorial)）。
- **文件附件**：上传文本文件、PDF 文档和 .docx 文档，以便让模型阅读并讨论其内容。
- 支持编辑消息、在不同版本间切换导航，并可随时分支对话。
- 提供笔记本选项卡，用于在对话回合之外进行自由文本生成。

### 后端与 API

- **多后端支持**：[llama.cpp](https://github.com/ggerganov/llama.cpp)、[ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)、[Transformers](https://github.com/huggingface/transformers)、[ExLlamaV3](https://github.com/turboderp-org/exllamav3) 和 [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)。无需重启即可在切换不同后端与模型。
- **兼容 OpenAI/Anthropic 的 API**：提供 Chat（对话）、Completions（补全）和 Messages（消息）接口，并支持工具调用。可作为本地无缝替代品接入 OpenAI/Anthropic API（[示例](https://github.com/oobabooga/textgen/wiki/12-%E2%80%90-OpenAI-API#examples)）。
- **工具调用**：模型可在对话过程中调用自定义函数，包括网页搜索、页面抓取和数学计算等。每个工具均为单个 `.py` 文件。同时支持 MCP 服务器（[教程](https://github.com/oobabooga/textgen/wiki/Tool-Calling-Tutorial)）。

### 训练与图像生成

- **模型训练**：在多轮对话或纯文本数据集上微调 LoRA 模型。支持断点续训功能（[教程](https://github.com/oobabooga/textgen/wiki/05-%E2%80%90-Training-Tab)）。
- **图像生成**：提供专用选项卡用于运行 `diffusers` 模型（如 **Z-Image-Turbo**）。支持 4-bit/8-bit 量化，并配备带有元数据持久化功能的图片库（[教程](https://github.com/oobabooga/textgen/wiki/Image-Generation-Tutorial)）。

### 隐私与界面

- 完全离线运行且保障隐私，零遥测、无外部资源调用或远程更新请求。
- 支持深色/浅色主题，代码块语法高亮，以及数学公式的 LaTeX 渲染。
- 内置及社区[扩展插件](https://github.com/oobabooga/textgen/wiki/07-%E2%80%90-Extensions)（包括 TTS、语音输入和翻译）。完整列表请参阅[扩展目录](https://github.com/oobabooga/textgen-extensions)。

## 下载模型

1. 从 [Hugging Face](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads&search=gguf) 下载 GGUF 格式模型文件。
2. 将其放入 `user_data/models` 文件夹中。

完成。UI 将自动检测该模型。

如需推荐的 GGUF 量化版本，可查看 [LocalBench](https://localbench.substack.com)。要估算模型占用的内存大小，可使用 [GGUF Memory Calculator](https://huggingface.co/spaces/oobabooga/accurate-gguf-vram-calculator)。

<details>
<summary>其他模型类型（Transformers、EXL3）</summary>

由多个文件组成的模型（如 16-bit Transformers 模型和 EXL3 模型）应放置在 `user_data/models` 下的子文件夹中：

```
textgen
└── user_data
    └── models
        └── Qwen_Qwen3-8B
            ├── config.json
            ├── generation_config.json
            ├── model-00001-of-00004.safetensors
            ├── ...
            ├── tokenizer_config.json
            └── tokenizer.json
```

这些格式需要完整安装版（非便携版）。
</details>

## 安装说明

桌面应用请参阅[便携版下载](https://github.com/oobabooga/textgen/releases)。以下选项将在浏览器中运行 Web UI。

### 使用 venv 手动安装便携版

适用于任意 Python 3.9+ 环境的快速部署：

```bash
# Clone repository
git clone https://github.com/oobabooga/textgen
cd textgen

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies (choose appropriate file under requirements/portable for your hardware)
pip install -r requirements/portable/requirements.txt --upgrade

# Launch server (basic command)
python server.py --portable --api --auto-launch

# When done working, deactivate
deactivate
```

### 完整安装说明

适合需要额外后端（ExLlamaV3、Transformers）、训练功能、图像生成或 TTS/语音输入/翻译等扩展插件的用户。需约 10GB 磁盘空间，并会自动下载 PyTorch。

<details>
<summary>安装详情</summary>

#### 一键安装程序

1. 克隆仓库，或[下载源码](https://github.com/oobabooga/textgen/archive/refs/heads/main.zip)并解压。
2. 运行对应操作系统的启动脚本：`start_windows.bat`、`start_linux.sh` 或 `start_macos.sh`。
3. 根据提示选择你的显卡厂商。
4. 安装完成后，在浏览器中打开 `http://127.0.0.1:7860`。

**安装后操作：**

* **重启**：运行相同的 `start_` 脚本即可。
* **传递命令行参数**：可直接传入（如 `./start_linux.sh --help`），或将其持久化保存在 `user_data/CMD_FLAGS.txt` 中（例如添加 `--api` 以启用 API）。
* **更新**：运行对应操作系统的更新脚本（`update_wizard_windows.bat`、`update_wizard_linux.sh` 或 `update_wizard_macos.sh`）。
* **全新重装**：删除 `installer_files` 文件夹后，再次运行 `start_` 脚本。
* **安装扩展依赖**：使用更新向导中的“安装/更新扩展依赖”选项。该选项会在末尾重新安装主项目依赖，以确保其优先级高于可能冲突的扩展依赖项。

**注意事项：**

* 这些脚本（`start_`、`update_wizard_`、`cmd_`）无需以管理员/root权限运行。
* 如需自动化安装，请设置 `GPU_CHOICE`、`LAUNCH_AFTER_INSTALL` 和 `INSTALL_EXTENSIONS` 环境变量。示例：`GPU_CHOICE=A LAUNCH_AFTER_INSTALL=FALSE INSTALL_EXTENSIONS=TRUE ./start_linux.sh`。
* 底层机制方面，脚本使用 Miniforge 在 `installer_files/` 中配置 Conda 环境。若需在该环境中手动执行命令，请使用 `cmd_linux.sh`、`cmd_windows.bat` 或 `cmd_macos.sh` 启动交互式 Shell。

#### 使用 Conda 进行完整安装

##### 0. 安装 Conda

https://github.com/conda-forge/miniforge

在 Linux 或 WSL 环境下，可通过以下两条命令自动安装 Miniforge：

```
curl -sL "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh" > "Miniforge3.sh"
bash Miniforge3.sh
```

其他平台请访问：https://github.com/conda-forge/miniforge/releases/latest

##### 1. 创建新的 Conda 环境

```
conda create -n textgen python=3.13
conda activate textgen
```

##### 2. 安装 PyTorch

| System | GPU | Command |
|--------|---------|---------|
| Linux/WSL | NVIDIA | `pip3 install torch==2.9.1 --index-url https://download.pytorch.org/whl/cu128` |
| Linux/WSL | CPU only | `pip3 install torch==2.9.1 --index-url https://download.pytorch.org/whl/cpu` |
| Linux | AMD | `pip3 install https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2/torch-2.9.1%2Brocm7.2.0.lw.git7e1940d4-cp313-cp313-linux_x86_64.whl` |
| MacOS + MPS | Any | `pip3 install torch==2.9.1` |
| Windows | NVIDIA | `pip3 install torch==2.9.1 --index-url https://download.pytorch.org/whl/cu128` |
| Windows | CPU only | `pip3 install torch==2.9.1` |

最新安装命令请访问：https://pytorch.org/get-started/locally/.

若你需要使用 `nvcc` 手动编译某些库，还需额外安装以下内容：

```
conda install -y -c "nvidia/label/cuda-12.8.1" cuda
```

##### 3. 安装 Web UI

```
git clone https://github.com/oobabooga/textgen
cd textgen
pip install -r requirements/full/<requirements file according to table below>
```

需使用的 requirements 文件：

| GPU | requirements file to use |
|--------|---------|
| NVIDIA | `requirements.txt` |
| AMD | `requirements_amd.txt` |
| CPU only | `requirements_cpu_only.txt` |
| Apple Intel | `requirements_apple_intel.txt` |
| Apple Silicon | `requirements_apple_silicon.txt` |

##### 4. 启动 Web UI

```
conda activate textgen
cd textgen
python server.py
```

随后访问 `http://127.0.0.1:7860`。

#### 手动编译

上述 `requirements*.txt` 文件包含通过 GitHub Actions 预编译的 Wheel 包。如需手动编译（例如你的硬件没有现成 Wheel），请使用 `requirements_nowheels.txt` 并自行安装所需的加载器。

#### 更新依赖项

偶尔 `requirements*.txt` 文件会发生变更。如需更新：

```
conda activate textgen
cd textgen
pip install -r <requirements file that you have used> --upgrade
```

### Docker

```
For NVIDIA GPU:
ln -s docker/{nvidia/Dockerfile,nvidia/docker-compose.yml,.dockerignore} .
For AMD GPU:
ln -s docker/{amd/Dockerfile,amd/docker-compose.yml,.dockerignore} .
For Intel GPU:
ln -s docker/{intel/Dockerfile,intel/docker-compose.yml,.dockerignore} .
For CPU only
ln -s docker/{cpu/Dockerfile,cpu/docker-compose.yml,.dockerignore} .
cp docker/.env.example .env
#Create logs/cache dir :
mkdir -p user_data/logs user_data/cache
# Edit .env and set:
#   TORCH_CUDA_ARCH_LIST based on your GPU model
#   APP_RUNTIME_GID      your host user's group id (run `id -g` in a terminal)
#   BUILD_EXTENIONS      optionally add comma separated list of extensions to build
# Edit user_data/CMD_FLAGS.txt and add in it the options you want to execute (like --listen --cpu)
#
docker compose up --build
```

* 需安装 Docker Compose v2.17 或更高版本。操作指南请参阅[此文档](https://github.com/oobabooga/textgen/wiki/09-%E2%80%90-Docker)。
* 更多 Docker 相关文件，可查阅[该仓库](https://github.com/Atinoda/text-generation-webui-docker)。

</details>

## 命令行参数

<details>
<summary>Show full list</summary>

```txt
usage: server.py [-h] [--user-data-dir USER_DATA_DIR] [--multi-user] [--model MODEL] [--lora LORA [LORA ...]] [--model-dir MODEL_DIR] [--lora-dir LORA_DIR] [--model-menu] [--settings SETTINGS]
                 [--extensions EXTENSIONS [EXTENSIONS ...]] [--verbose] [--idle-timeout IDLE_TIMEOUT] [--image-model IMAGE_MODEL] [--image-model-dir IMAGE_MODEL_DIR] [--image-dtype {bfloat16,float16}]
                 [--image-attn-backend {flash_attention_2,sdpa}] [--image-cpu-offload] [--image-compile] [--image-quant {none,bnb-8bit,bnb-4bit,torchao-int8wo,torchao-fp4,torchao-float8wo}]
                 [--loader LOADER] [--ctx-size N] [--cache-type N] [--model-draft MODEL_DRAFT] [--draft-max DRAFT_MAX] [--gpu-layers-draft GPU_LAYERS_DRAFT] [--device-draft DEVICE_DRAFT]
                 [--ctx-size-draft CTX_SIZE_DRAFT] [--spec-type {none,ngram-mod,ngram-simple,ngram-map-k,ngram-map-k4v,ngram-cache}] [--spec-ngram-size-n SPEC_NGRAM_SIZE_N]
                 [--spec-ngram-size-m SPEC_NGRAM_SIZE_M] [--spec-ngram-min-hits SPEC_NGRAM_MIN_HITS] [--gpu-layers N] [--cpu-moe] [--mmproj MMPROJ] [--streaming-llm] [--tensor-split TENSOR_SPLIT]
                 [--split-mode {layer,row,tensor,none}] [--no-mmap] [--mlock] [--no-kv-offload] [--batch-size BATCH_SIZE] [--ubatch-size UBATCH_SIZE] [--threads THREADS]
                 [--threads-batch THREADS_BATCH] [--numa] [--parallel PARALLEL] [--fit-target FIT_TARGET] [--extra-flags EXTRA_FLAGS] [--ik] [--cpu] [--cpu-memory CPU_MEMORY] [--disk]
                 [--disk-cache-dir DISK_CACHE_DIR] [--load-in-8bit] [--bf16] [--no-cache] [--trust-remote-code] [--force-safetensors] [--no_use_fast] [--attn-implementation IMPLEMENTATION]
                 [--load-in-4bit] [--use_double_quant] [--compute_dtype COMPUTE_DTYPE] [--quant_type QUANT_TYPE] [--gpu-split GPU_SPLIT] [--enable-tp] [--tp-backend TP_BACKEND] [--cfg-cache]
                 [--listen] [--listen-port LISTEN_PORT] [--listen-host LISTEN_HOST] [--share] [--auto-launch] [--gradio-auth GRADIO_AUTH] [--gradio-auth-path GRADIO_AUTH_PATH]
                 [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE] [--subpath SUBPATH] [--old-colors] [--portable] [--api] [--public-api] [--public-api-id PUBLIC_API_ID] [--api-port API_PORT]
                 [--api-key API_KEY] [--admin-key ADMIN_KEY] [--api-enable-ipv6] [--api-disable-ipv4] [--nowebui] [--temperature N] [--dynatemp-low N] [--dynatemp-high N] [--dynatemp-exponent N]
                 [--smoothing-factor N] [--smoothing-curve N] [--top-p N] [--top-k N] [--min-p N] [--top-n-sigma N] [--typical-p N] [--xtc-threshold N] [--xtc-probability N] [--epsilon-cutoff N]
                 [--eta-cutoff N] [--tfs N] [--top-a N] [--adaptive-target N] [--adaptive-decay N] [--dry-multiplier N] [--dry-allowed-length N] [--dry-base N] [--repetition-penalty N]
                 [--frequency-penalty N] [--presence-penalty N] [--encoder-repetition-penalty N] [--no-repeat-ngram-size N] [--repetition-penalty-range N] [--penalty-alpha N] [--guidance-scale N]
                 [--mirostat-mode N] [--mirostat-tau N] [--mirostat-eta N] [--do-sample | --no-do-sample] [--dynamic-temperature | --no-dynamic-temperature]
                 [--temperature-last | --no-temperature-last] [--sampler-priority N] [--dry-sequence-breakers N] [--enable-thinking | --no-enable-thinking] [--reasoning-effort N]
                 [--preserve-thinking | --no-preserve-thinking] [--chat-template-file CHAT_TEMPLATE_FILE] [--no-electron]

TextGen

options:
  -h, --help                                           show this help message and exit

Basic settings:
  --user-data-dir USER_DATA_DIR                        Path to the user data directory. Default: auto-detected.
  --multi-user                                         Multi-user mode. Chat histories are not saved or automatically loaded. Best suited for small trusted teams.
  --model MODEL                                        Name of the model to load by default.
  --lora LORA [LORA ...]                               The list of LoRAs to load. If you want to load more than one LoRA, write the names separated by spaces.
  --model-dir MODEL_DIR                                Path to directory with all the models.
  --lora-dir LORA_DIR                                  Path to directory with all the loras.
  --model-menu                                         Show a model menu in the terminal when the web UI is first launched.
  --settings SETTINGS                                  Load the default interface settings from this yaml file. See user_data/settings-template.yaml for an example. If you create a file called
                                                       user_data/settings.yaml, this file will be loaded by default without the need to use the --settings flag.
  --extensions EXTENSIONS [EXTENSIONS ...]             The list of extensions to load. If you want to load more than one extension, write the names separated by spaces.
  --verbose                                            Print the prompts to the terminal.
  --idle-timeout IDLE_TIMEOUT                          Unload model after this many minutes of inactivity. It will be automatically reloaded when you try to use it again.

Image model:
  --image-model IMAGE_MODEL                            Name of the image model to select on startup (overrides saved setting).
  --image-model-dir IMAGE_MODEL_DIR                    Path to directory with all the image models.
  --image-dtype {bfloat16,float16}                     Data type for image model.
  --image-attn-backend {flash_attention_2,sdpa}        Attention backend for image model.
  --image-cpu-offload                                  Enable CPU offloading for image model.
  --image-compile                                      Compile the image model for faster inference.
  --image-quant {none,bnb-8bit,bnb-4bit,torchao-int8wo,torchao-fp4,torchao-float8wo}
                                                       Quantization method for image model.

Model loader:
  --loader LOADER                                      Choose the model loader manually, otherwise, it will get autodetected. Valid options: Transformers, llama.cpp, ExLlamav3_HF, ExLlamav3, TensorRT-
                                                       LLM.

Context and cache:
  --ctx-size, --n_ctx, --max_seq_len N                 Context size in tokens. 0 = auto for llama.cpp (requires gpu-layers=-1), 8192 for other loaders.
  --cache-type, --cache_type N                         KV cache type; valid options: llama.cpp - fp16, q8_0, q4_0; ExLlamaV3 - fp16, q2 to q8 (can specify k_bits and v_bits separately, e.g. q4_q8).

Speculative decoding:
  --model-draft MODEL_DRAFT                            Path to the draft model for speculative decoding.
  --draft-max DRAFT_MAX                                Number of tokens to draft for speculative decoding.
  --gpu-layers-draft GPU_LAYERS_DRAFT                  Number of layers to offload to the GPU for the draft model.
  --device-draft DEVICE_DRAFT                          Comma-separated list of devices to use for offloading the draft model. Example: CUDA0,CUDA1
  --ctx-size-draft CTX_SIZE_DRAFT                      Size of the prompt context for the draft model. If 0, uses the same as the main model.
  --spec-type {none,ngram-mod,ngram-simple,ngram-map-k,ngram-map-k4v,ngram-cache}
                                                       Draftless speculative decoding type. Recommended: ngram-mod.
  --spec-ngram-size-n SPEC_NGRAM_SIZE_N                N-gram lookup size for ngram speculative decoding.
  --spec-ngram-size-m SPEC_NGRAM_SIZE_M                Draft n-gram size for ngram speculative decoding.
  --spec-ngram-min-hits SPEC_NGRAM_MIN_HITS            Minimum n-gram hits for ngram-map speculative decoding.

llama.cpp:
  --gpu-layers, --n-gpu-layers N                       Number of layers to offload to the GPU. -1 = auto.
  --cpu-moe                                            Move the experts to the CPU (for MoE models).
  --mmproj MMPROJ                                      Path to the mmproj file for vision models.
  --streaming-llm                                      Activate StreamingLLM to avoid re-evaluating the entire prompt when old messages are removed.
  --tensor-split TENSOR_SPLIT                          Split the model across multiple GPUs. Comma-separated list of proportions. Example: 60,40.
  --split-mode {layer,row,tensor,none}                 How to split the model across multiple GPUs. "tensor" can make multi-GPU significantly faster.
  --no-mmap                                            Prevent mmap from being used.
  --mlock                                              Force the system to keep the model in RAM.
  --no-kv-offload                                      Do not offload the K, Q, V to the GPU. This saves VRAM but reduces performance.
  --batch-size BATCH_SIZE                              Maximum number of prompt tokens to batch together when calling llama-server. This is the application level batch size.
  --ubatch-size UBATCH_SIZE                            Maximum number of prompt tokens to batch together when calling llama-server. This is the max physical batch size for computation (device level).
  --threads THREADS                                    Number of threads to use.
  --threads-batch THREADS_BATCH                        Number of threads to use for batches/prompt processing.
  --numa                                               Activate NUMA task allocation for llama.cpp.
  --parallel PARALLEL                                  Number of parallel request slots. The context size is divided equally among slots. For example, to have 4 slots with 8192 context each, set
                                                       ctx_size to 32768.
  --fit-target FIT_TARGET                              Target VRAM margin per device for auto GPU layers, comma-separated list of values in MiB. A single value is broadcast across all devices.
  --extra-flags EXTRA_FLAGS                            Extra flags to pass to llama-server. Example: "--jinja --rpc 192.168.1.100:50052"
  --ik                                                 Use ik_llama.cpp instead of upstream llama.cpp. Requires the ik_llama_cpp_binaries package to be installed.

Transformers/Accelerate:
  --cpu                                                Use the CPU to generate text. Warning: Training on CPU is extremely slow.
  --cpu-memory CPU_MEMORY                              Maximum CPU memory in GiB. Use this for CPU offloading.
  --disk                                               If the model is too large for your GPU(s) and CPU combined, send the remaining layers to the disk.
  --disk-cache-dir DISK_CACHE_DIR                      Directory to save the disk cache to.
  --load-in-8bit                                       Load the model with 8-bit precision (using bitsandbytes).
  --bf16                                               Load the model with bfloat16 precision. Requires NVIDIA Ampere GPU.
  --no-cache                                           Set use_cache to False while generating text. This reduces VRAM usage slightly, but it comes at a performance cost.
  --trust-remote-code                                  Set trust_remote_code=True while loading the model. Necessary for some models.
  --force-safetensors                                  Set use_safetensors=True while loading the model. This prevents arbitrary code execution.
  --no_use_fast                                        Set use_fast=False while loading the tokenizer (it's True by default). Use this if you have any problems related to use_fast.
  --attn-implementation IMPLEMENTATION                 Attention implementation. Valid options: sdpa, eager, flash_attention_2.

bitsandbytes 4-bit:
  --load-in-4bit                                       Load the model with 4-bit precision (using bitsandbytes).
  --use_double_quant                                   use_double_quant for 4-bit.
  --compute_dtype COMPUTE_DTYPE                        compute dtype for 4-bit. Valid options: bfloat16, float16, float32.
  --quant_type QUANT_TYPE                              quant_type for 4-bit. Valid options: nf4, fp4.

ExLlamaV3:
  --gpu-split GPU_SPLIT                                Comma-separated list of VRAM (in GB) to use per GPU device for model layers. Example: 20,7,7.
  --enable-tp, --enable_tp                             Enable Tensor Parallelism (TP) to split the model across GPUs.
  --tp-backend TP_BACKEND                              The backend for tensor parallelism. Valid options: native, nccl. Default: native.
  --cfg-cache                                          Create an additional cache for CFG negative prompts. Necessary to use CFG with that loader.

Gradio:
  --listen                                             Make the web UI reachable from your local network.
  --listen-port LISTEN_PORT                            The listening port that the server will use.
  --listen-host LISTEN_HOST                            The hostname that the server will use.
  --share                                              Create a public URL. This is useful for running the web UI on Google Colab or similar.
  --auto-launch                                        Open the web UI in the default browser upon launch.
  --gradio-auth GRADIO_AUTH                            Set Gradio authentication password in the format "username:password". Multiple credentials can also be supplied with "u1:p1,u2:p2,u3:p3".
  --gradio-auth-path GRADIO_AUTH_PATH                  Set the Gradio authentication file path. The file should contain one or more user:password pairs in the same format as above.
  --ssl-keyfile SSL_KEYFILE                            The path to the SSL certificate key file.
  --ssl-certfile SSL_CERTFILE                          The path to the SSL certificate cert file.
  --subpath SUBPATH                                    Customize the subpath for gradio, use with reverse proxy
  --old-colors                                         Use the legacy Gradio colors, before the December/2024 update.
  --portable                                           Hide features not available in portable mode like training.

API:
  --api                                                Enable the API server.
  --public-api                                         Create a public URL for the API using Cloudflare.
  --public-api-id PUBLIC_API_ID                        Tunnel ID for named Cloudflare Tunnel. Use together with public-api option.
  --api-port API_PORT                                  The listening port for the API.
  --api-key API_KEY                                    API authentication key.
  --admin-key ADMIN_KEY                                API authentication key for admin tasks like loading and unloading models. If not set, will be the same as --api-key.
  --api-enable-ipv6                                    Enable IPv6 for the API
  --api-disable-ipv4                                   Disable IPv4 for the API
  --nowebui                                            Do not launch the Gradio UI. Useful for launching the API in standalone mode.

API generation defaults:
  --temperature N                                      Temperature
  --dynatemp-low N                                     Dynamic temperature low
  --dynatemp-high N                                    Dynamic temperature high
  --dynatemp-exponent N                                Dynamic temperature exponent
  --smoothing-factor N                                 Smoothing factor
  --smoothing-curve N                                  Smoothing curve
  --top-p N                                            Top P
  --top-k N                                            Top K
  --min-p N                                            Min P
  --top-n-sigma N                                      Top N Sigma
  --typical-p N                                        Typical P
  --xtc-threshold N                                    XTC threshold
  --xtc-probability N                                  XTC probability
  --epsilon-cutoff N                                   Epsilon cutoff
  --eta-cutoff N                                       Eta cutoff
  --tfs N                                              TFS
  --top-a N                                            Top A
  --adaptive-target N                                  Adaptive target
  --adaptive-decay N                                   Adaptive decay
  --dry-multiplier N                                   DRY multiplier
  --dry-allowed-length N                               DRY allowed length
  --dry-base N                                         DRY base
  --repetition-penalty N                               Repetition penalty
  --frequency-penalty N                                Frequency penalty
  --presence-penalty N                                 Presence penalty
  --encoder-repetition-penalty N                       Encoder repetition penalty
  --no-repeat-ngram-size N                             No repeat ngram size
  --repetition-penalty-range N                         Repetition penalty range
  --penalty-alpha N                                    Penalty alpha
  --guidance-scale N                                   Guidance scale
  --mirostat-mode N                                    Mirostat mode
  --mirostat-tau N                                     Mirostat tau
  --mirostat-eta N                                     Mirostat eta
  --do-sample, --no-do-sample                          Do sample
  --dynamic-temperature, --no-dynamic-temperature      Dynamic temperature
  --temperature-last, --no-temperature-last            Temperature last
  --sampler-priority N                                 Sampler priority
  --dry-sequence-breakers N                            DRY sequence breakers
  --enable-thinking, --no-enable-thinking              Enable thinking
  --reasoning-effort N                                 Reasoning effort
  --preserve-thinking, --no-preserve-thinking          Preserve thinking blocks from prior turns in the chat template
  --chat-template-file CHAT_TEMPLATE_FILE              Path to a chat template file (.jinja, .jinja2, or .yaml) to use as the default instruction template for API requests. Overrides the model's
                                                       built-in template.

Electron:
  --no-electron                                        In portable builds, skip the Electron desktop window. Useful if you prefer to use the web UI in the browser.
```

</details>

## 自动加载模型

若要在每次启动时跳过“模型”选项卡，请将以下内容添加到 `user_data/CMD_FLAGS.txt`：

```
--model my-model.gguf
```

将 `my-model.gguf` 替换为 `user_data/models` 目录下的任意文件名。该模型将在启动时自动加载。

如需传递额外参数，请每行一个：

```
--model my-model.gguf
--cache-type q8_0
```

## 文档说明

https://github.com/oobabooga/textgen/wiki

## 社区交流

[![Reddit](https://img.shields.io/reddit/subreddit-subscribers/Oobabooga?style=for-the-badge&logo=reddit&logoColor=white&label=r%2FOobabooga&labelColor=black&color=FF4500)](https://www.reddit.com/r/Oobabooga/)

## 致谢

- 2023年8月，[Andreessen Horowitz](https://a16z.com/)（a16z）慷慨资助了本项目，以鼓励和支持我的独立开发工作。我**极其感激**他们的信任与认可。
- 本项目的灵感来源于 [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)，若无其启发，本项目将不复存在。