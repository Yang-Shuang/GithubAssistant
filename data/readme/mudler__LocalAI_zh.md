<h1 align="center">
  <br>
  <img width="300" src="./core/http/static/logo.png"> <br>
<br>
</h1>

<p align="center">
<a href="https://github.com/go-skynet/LocalAI/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/go-skynet/LocalAI?style=for-the-badge" alt="LocalAI stars"/>
</a>
<a href='https://github.com/go-skynet/LocalAI/releases'>
<img src='https://img.shields.io/github/release/go-skynet/LocalAI?&label=Latest&style=for-the-badge'>
</a>
<a href="LICENSE" target="blank">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="LocalAI License"/>
</a>
</p>

<p align="center">
<a href="https://twitter.com/LocalAI_API" target="blank">
<img src="https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white&label=LocalAI_API" alt="Follow LocalAI_API"/>
</a>
<a href="https://discord.gg/uJAeKSAGDy" target="blank">
<img src="https://img.shields.io/badge/dynamic/json?color=blue&label=Discord&style=for-the-badge&query=approximate_member_count&url=https%3A%2F%2Fdiscordapp.com%2Fapi%2Finvites%2FuJAeKSAGDy%3Fwith_counts%3Dtrue&logo=discord" alt="Join LocalAI Discord Community"/>
</a>
</p>

<p align="center">
<a href="https://trendshift.io/repositories/5539" target="_blank"><img src="https://trendshift.io/api/badge/repositories/5539" alt="mudler%2FLocalAI | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

**LocalAI** 是一款开源 AI 引擎。在任何硬件上运行任意模型——大语言模型（LLM）、视觉、语音、图像和视频，无需专用显卡（GPU）即可运行。

**核心精简，非臃肿套件。** 每个后端将业界顶尖引擎（如 llama.cpp、vLLM、whisper.cpp、stable-diffusion、MLX 等）封装为独立的镜像，仅在模型需要时才拉取。你无需安装任何不需要的组件。

- **原生模块化设计**：后端相互独立且按需拉取，因此只需安装模型所需的组件
- **开放可扩展**：加载任意模型，或基于开放接口使用任何语言开发自定义后端
- **开箱即用的 API 兼容**：所有后端均完美兼容 OpenAI、Anthropic 和 ElevenLabs API
- **全模态支持**：大语言模型（LLM）、视觉、语音、图像和视频统一由一个 API 提供服务
- **硬件不限**：全面支持 NVIDIA、AMD、Intel、Apple Silicon、Vulkan，或纯 CPU 环境
- **多用户就绪**：内置 API Key 认证、用户配额及基于角色的访问控制（RBAC）
- **内置 AI Agent**：支持自主调用工具、检索增强生成（RAG）、模型上下文协议（MCP）及技能扩展的智能体
- **隐私优先**：你的数据始终保留在你的基础设施内，绝不外泄

![LocalAI 核心精简，后端（如 llama.cpp、vLLM、MLX、whisper.cpp、stable-diffusion、kokoro、parakeet.cpp 等）作为独立的按需拉取镜像接入](docs/static/images/diagrams/composable-core.png)

由 [Ettore Di Giacinto](https://github.com/mudler) 创建，并由 [LocalAI 团队](#team) 维护。

> [:book: 官方文档](https://localai.io/) | [:speech_balloon: Discord](https://discord.gg/uJAeKSAGDy) | [💻 快速入门](https://localai.io/basics/getting_started/) | [🖼️ 模型库](https://models.localai.io/) | [❓常见问题](https://localai.io/faq/)

## 功能演示

https://github.com/user-attachments/assets/08cbb692-57da-48f7-963d-2e7b43883c18

<details>

<summary>
点击查看更多演示！
</summary>

#### 用户与认证

https://github.com/user-attachments/assets/228fa9ad-81a3-4d43-bfb9-31557e14a36c

#### Agent（智能体）

https://github.com/user-attachments/assets/6270b331-e21d-4087-a540-6290006b381a

#### 用户级使用指标

https://github.com/user-attachments/assets/cbb03379-23b4-4e3d-bd26-d152f057007f

#### 微调与量化

https://github.com/user-attachments/assets/5ba4ace9-d3df-4795-b7d4-b0b404ea71ee

#### WebRTC（实时音视频）

https://github.com/user-attachments/assets/ed88e34c-fed3-4b83-8a67-4716a9feeb7b

</details>

## 快速入门

### macOS

<a href="https://github.com/mudler/LocalAI/releases/latest/download/LocalAI.dmg">
  <img src="https://img.shields.io/badge/Download-macOS-blue?style=for-the-badge&logo=apple&logoColor=white" alt="Download LocalAI for macOS"/>
</a>

> **注意：** 该 DMG 文件未经 Apple 签名。安装后请运行：`sudo xattr -d com.apple.quarantine /Applications/LocalAI.app`。详情请见 [#6268](https://github.com/mudler/LocalAI/issues/6268)。

### 容器部署（Docker、podman 等）

> **提示：** 之前已运行过 LocalAI？使用 `docker start -i local-ai` 即可重启现有容器。

#### 仅 CPU：

```bash
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
```

#### NVIDIA GPU（显卡）：

```bash
# CUDA 13
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-13

# CUDA 12
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-12

# NVIDIA Jetson ARM64（适用于 AGX Orin 及同类设备）
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-nvidia-l4t-arm64

# NVIDIA Jetson ARM64（适用于 DGX Spark）
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-nvidia-l4t-arm64-cuda-13
```

#### AMD GPU（ROCm）：

```bash
docker run -ti --name local-ai -p 8080:8080 --device=/dev/kfd --device=/dev/dri --group-add=video localai/localai:latest-gpu-hipblas
```

#### Intel GPU（oneAPI）：

```bash
docker run -ti --name local-ai -p 8080:8080 --device=/dev/dri/card1 --device=/dev/dri/renderD128 localai/localai:latest-gpu-intel
```

#### Vulkan GPU：

```bash
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest-gpu-vulkan
```

### 加载模型

```bash
# From the model gallery (see available models with `local-ai models list` or at https://models.localai.io)
local-ai run llama-3.2-1b-instruct:q4_k_m
# From Huggingface
local-ai run huggingface://TheBloke/phi-2-GGUF/phi-2.Q8_0.gguf
# From the Ollama OCI registry
local-ai run ollama://gemma:2b
# From a YAML config
local-ai run https://gist.githubusercontent.com/.../phi-2.yaml
# From a standard OCI registry (e.g., Docker Hub)
local-ai run oci://localai/phi-2:latest
```

> **自动后端检测**：LocalAI 会自动识别你的硬件能力并下载对应的后端。如需高级选项，请参阅 [GPU 加速指南](https://localai.io/features/gpu-acceleration/)。

更多详情请查阅[快速入门指南](https://localai.io/basics/getting_started/)。

## 最新动态

- **2026年5月**：**LocalAI 4.3.0** —— `llama.cpp` [默认开启提示词缓存（prompt cache）](https://github.com/mudler/LocalAI/pull/9925)（重复的系统提示处理时间从数分钟缩短至数秒），[后端 OCI 镜像的无密钥 cosign 签名](https://github.com/mudler/LocalAI/pull/9823)，[按 API Key + 用户维度的用量统计](https://github.com/mudler/LocalAI/pull/9920)，分布式 v3 版本新增 [请求级副本路由机制](https://github.com/mudler/LocalAI/pull/9968)。[发布说明](https://github.com/mudler/LocalAI/releases/tag/v4.3.0)
- **2026年5月**：**LocalAI 4.2.0** —— LocalAI 实现视听能力：新增[语音识别](https://github.com/mudler/LocalAI/pull/9500)、[人脸识别 + 防伪造活体检测](https://github.com/mudler/LocalAI/pull/9480)及说话人分离（diarization）。此外还包含[无缝兼容的 Ollama API](https://github.com/mudler/LocalAI/pull/9284)、[视频生成](https://github.com/mudler/LocalAI/pull/9420)，全新设计的 UI 支持多语言国际化（i18n）及管理员自定义品牌配置，vLLM 功能与 llama.cpp 持平，并新增 11 个后端。[发布说明](https://github.com/mudler/LocalAI/releases/tag/v4.2.0)
- **2026年4月**：**LocalAI 4.1.0** —— LocalAI 升级为控制中枢：支持分布式集群模式（具备显存感知智能路由与自动扩缩容）、基于 OIDC 和 API Key 的多用户平台、带预测性分析的用户级配额管理、内置 TRL 微调工具（支持自动导出为 GGUF）、动态量化后端及可视化流水线编辑器。[发布说明](https://github.com/mudler/LocalAI/releases/tag/v4.1.0)
- **2026年3月**：**LocalAI 4.0.0** —— 原生支持 Agent（智能体）编排，上线全新社区中心 [Agenthub](https://agenthub.localai.io)；React UI 全面重构并新增 Canvas 模式；[MCP 应用及客户端侧实现](https://github.com/mudler/LocalAI/pull/8947)支持工具流式传输（tool streaming）；[WebRTC 实时音频](https://github.com/mudler/LocalAI/pull/8790)；[MLX 分布式训练](https://github.com/mudler/LocalAI/pull/8801)。[发布说明](https://github.com/mudler/LocalAI/releases/tag/v4.0.0)
- **2026年2月**：[支持带工具调用的音频到音频实时 API（Realtime API）](https://github.com/mudler/LocalAI/pull/6245)、[ACE-Step 1.5 模型支持](https://github.com/mudler/LocalAI/pull/8396)
- **2026年1月**：**LocalAI 3.10.0** —— 支持 Anthropic API、Open Responses API，新增视频与图像生成（LTX-2）、统一 GPU 后端、工具流式传输（tool streaming）、Moonshine 及 Pocket-TTS。[发布说明](https://github.com/mudler/LocalAI/releases/tag/v3.10.0)
- **2025年12月**：[动态内存资源回收器](https://github.com/mudler/LocalAI/pull/7583)、[LLaMA.cpp 自动多 GPU 模型适配（Automatic multi-GPU model fitting）](https://github.com/mudler/LocalAI/pull/7584)、[Vibevoice 后端](https://github.com/mudler/LocalAI/pull/7494)
- **2025年11月**：[通过 URL 导入模型](https://github.com/mudler/LocalAI/pull/7245)、[多会话与历史记录支持](https://github.com/mudler/LocalAI/pull/7325)
- **2025年10月**：[模型上下文协议（MCP）](https://localai.io/docs/features/mcp/)支持，赋能 Agent 能力
- **2025年9月**：macOS 与 Linux 新版启动器，扩展对 Mac 及 NVIDIA L4T 的后端支持，新增 MLX-Audio、WAN 2.2
- **2025年8月**：MLX、MLX-VLM、Diffusers、llama.cpp 正式支持 Apple Silicon（苹果芯片）
- **2025年7月**：所有后端迁移至主程序之外 —— 实现[轻量级、模块化架构](https://github.com/mudler/LocalAI/releases/tag/v3.2.0)

查看历史动态及完整发布说明，请访问 [GitHub Releases](https://github.com/mudler/LocalAI/releases) 和[新闻动态页面](https://localai.io/basics/news/)。

## 核心功能

- [文本生成](https://localai.io/features/text-generation/)（支持 `llama.cpp`、`transformers`、`vllm` 等，[查看更多](https://localai.io/model-compatibility/)）
- [文本转语音（TTS）](https://localai.io/features/text-to-audio/)
- [语音转文本（STT）](https://localai.io/features/audio-to-text/)
- [图像生成](https://localai.io/features/image-generation)
- [兼容 OpenAI 的 Tools API](https://localai.io/features/openai-functions/)
- [实时 API（Realtime API）](https://localai.io/features/openai-realtime/)（语音到语音）
- [向量嵌入生成（Embeddings）](https://localai.io/features/embeddings/)
- [约束语法（Constrained Grammars）](https://localai.io/features/constrained_grammars/)
- [从 Hugging Face 下载模型](https://localai.io/models/)
- [视觉 API（Vision API）](https://localai.io/features/gpt-vision/)
- [目标检测（Object Detection）](https://localai.io/features/object-detection/)
- [重排序 API（Reranker API）](https://localai.io/features/reranker/)
- [点对点推理（P2P Inferencing）](https://localai.io/features/distribute/)
- [分布式模式](https://localai.io/features/distributed-mode/) —— 基于 PostgreSQL + NATS 的水平扩展
- [模型上下文协议（MCP）](https://localai.io/docs/features/mcp/)
- [内置 Agent（智能体）](https://localai.io/features/agents/) —— 支持工具调用、RAG、技能扩展、SSE 流式传输及 [Agent Hub](https://agenthub.localai.io) 的自主 AI 智能体
- [后端画廊（Backend Gallery）](https://localai.io/backends/) —— 通过 OCI 镜像即时安装/卸载后端
- 语音活动检测（VAD，基于 Silero-VAD）
- 集成 Web UI

## 支持的后端与硬件加速

LocalAI 支持包括 `llama.cpp`、vLLM、transformers、whisper.cpp、diffusers、MLX、MLX-VLM 在内的 **36+ 个后端**。硬件加速全面覆盖 **NVIDIA**（CUDA 12/13）、**AMD**（ROCm）、**Intel**（oneAPI/SYCL）、**Apple Silicon**（Metal）、**Vulkan** 以及 **NVIDIA Jetson**（L4T）。所有后端均可通过 [Backend Gallery](https://localai.io/backends/) 即时安装。

完整列表请查阅[后端与模型兼容性表](https://localai.io/model-compatibility/)及 [GPU 加速指南](https://localai.io/features/gpu-acceleration/)。

## 资源链接

- [官方文档](https://localai.io/)
- [大语言模型微调指南](https://localai.io/docs/advanced/fine-tuning/)
- [源码编译构建](https://localai.io/basics/build/)
- [Kubernetes 部署指南](https://localai.io/basics/getting_started/#run-localai-in-kubernetes)
- [集成与社区项目](https://localai.io/docs/integrations/)
- [安装视频教程](https://www.youtube.com/watch?v=cMVNnlqwfw4)
- [媒体报道与技术博客](https://localai.io/basics/news/#media-blogs-social)
- [示例项目](https://github.com/mudler/LocalAI-examples)

## 团队介绍

LocalAI 由一支精简的核心团队维护，并得到了广大社区贡献者的支持。

- **[Ettore Di Giacinto](https://github.com/mudler)** —— 创始人及项目负责人
- **[Richard Palethorpe](https://github.com/richiejp)** —— 核心维护者

衷心感谢每一位贡献代码、审查 PR、提交 Issue 以及在 [Discord](https://discord.gg/uJAeKSAGDy) 帮助用户的伙伴。LocalAI 是一个社区驱动的项目，没有你们便不会有它的今天。完整名单请见[贡献者列表](https://github.com/mudler/LocalAI/graphs/contributors)。

## 引用说明

如果你在下游项目中使用了本仓库或相关数据，请考虑引用以下内容：

```
@misc{localai,
  author = {Ettore Di Giacinto},
  title = {LocalAI: The free, Open source OpenAI alternative},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/go-skynet/LocalAI}},
```

## 赞助支持

> **你觉得 LocalAI 有用吗？**

通过成为[支持者或赞助商](https://github.com/sponsors/mudler)来支持该项目。你的 Logo 将在此展示并附带官网链接。

衷心感谢慷慨赞助本项目、覆盖持续集成（CI）费用的赞助商，以及我们的[完整赞助名单](https://github.com/sponsors/mudler)：

<p align="center">
  <a href="https://www.spectrocloud.com/" target="blank">
    <img height="200" src="https://github.com/user-attachments/assets/72eab1dd-8b93-4fc0-9ade-84db49f24962">
  </a>
</p>

<details>

<summary>
历史赞助商
</summary>

<p align="center">
  <a href="https://www.premai.io/" target="blank">
    <img height="200" src="https://github.com/mudler/LocalAI/assets/2420543/42e4ca83-661e-4f79-8e46-ae43689683d6"> <br>
  </a>
</p>

</details>

### 个人赞助者

特别感谢所有个人赞助者，完整名单请见 [GitHub](https://github.com/sponsors/mudler) 和 [buy me a coffee](https://buymeacoffee.com/mudler)。特别鸣谢慷慨支持的 [drikster80](https://github.com/drikster80)。谢谢大家！

## ⭐ Star 增长历史

[![LocalAI Star history Chart](https://api.star-history.com/svg?repos=go-skynet/LocalAI&type=Date)](https://star-history.com/#go-skynet/LocalAI&Date)

## 开源协议

LocalAI 是由 [Ettore Di Giacinto](https://github.com/mudler/) 创建、由 [LocalAI 团队](#team) 维护的社区驱动项目。

MIT 协议 —— 作者：Ettore Di Giacinto <mudler@localai.io>

## 致谢

LocalAI 的诞生离不开社区现有优秀软件的支持。在此致以诚挚谢意！

- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- https://github.com/tatsu-lab/stanford_alpaca
- https://github.com/cornelk/llama-go for the initial ideas
- https://github.com/antimatter15/alpaca.cpp
- https://github.com/EdVince/Stable-Diffusion-NCNN
- https://github.com/ggerganov/whisper.cpp
- https://github.com/rhasspy/piper
- [exo](https://github.com/exo-explore/exo) for the MLX distributed auto-parallel sharding implementation

## 贡献者

这是一个社区驱动的项目，特别感谢所有贡献者！
<a href="https://github.com/go-skynet/LocalAI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=go-skynet/LocalAI" />
</a>