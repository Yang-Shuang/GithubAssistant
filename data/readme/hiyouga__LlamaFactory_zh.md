![# LLaMA Factory](assets/logo.png)

[![GitHub Repo stars](https://img.shields.io/github/stars/hiyouga/LLaMA-Factory?style=social)](https://github.com/hiyouga/LLaMA-Factory/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/hiyouga/LLaMA-Factory)](https://github.com/hiyouga/LLaMA-Factory/commits/main)
[![GitHub contributors](https://img.shields.io/github/contributors/hiyouga/LLaMA-Factory?color=orange)](https://github.com/hiyouga/LLaMA-Factory/graphs/contributors)
[![GitHub workflow](https://github.com/hiyouga/LLaMA-Factory/actions/workflows/tests.yml/badge.svg)](https://github.com/hiyouga/LLaMA-Factory/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/llamafactory)](https://pypi.org/project/llamafactory/)
[![Citation](https://img.shields.io/badge/citation-1000+-green)](https://scholar.google.com/scholar?cites=12620864006390196564)
[![Docker Pulls](https://img.shields.io/docker/pulls/hiyouga/llamafactory)](https://hub.docker.com/r/hiyouga/llamafactory/tags)

[![Twitter](https://img.shields.io/twitter/follow/llamafactory_ai)](https://twitter.com/llamafactory_ai)
[![Discord](assets/thirdparty/discord.svg)](https://discord.gg/rKfvV9r9FK)
[![WeChat](https://img.shields.io/badge/WeChat-User%20Group-blue?logo=wechat)](https://github.com/hiyouga/llamafactory-community)
[![Blog](https://img.shields.io/badge/Hugo-Official%20Blog-blue?logo=hugo)](https://blog.llamafactory.net/en/)

[![Open in Colab](assets/thirdparty/colab.svg)](https://colab.research.google.com/drive/1eRTPn37ltBbYsISy9Aw2NuI2Aq5CQrD9?usp=sharing)
[![Open in DSW](assets/thirdparty/dsw.svg)](https://gallery.pai-ml.com/#/preview/deepLearning/nlp/llama_factory)
[![Open in Spaces](https://img.shields.io/badge/🤗-Open%20in%20Spaces-blue)](https://huggingface.co/spaces/hiyouga/LLaMA-Board)
[![Open in Studios](https://img.shields.io/badge/ModelScope-Open%20in%20Studios-blue)](https://modelscope.cn/studios/hiyouga/LLaMA-Board)
[![Open in Novita](https://img.shields.io/badge/Novita-Deploy%20Template-blue)](https://novita.ai/templates-library/105981?sharer=88115474-394e-4bda-968e-b88e123d0c47)

### 被 [Amazon](https://aws.amazon.com/cn/blogs/machine-learning/how-apoidea-group-enhances-visual-information-extraction-from-banking-documents-with-multimodal-models-using-llama-factory-on-amazon-sagemaker-hyperpod/)、[NVIDIA](https://developer.nvidia.com/rtx/ai-toolkit)、[阿里云](https://help.aliyun.com/zh/pai/use-cases/fine-tune-a-llama-3-model-with-llama-factory) 等机构采用

<div align="center" markdown="1">

### 支持者 ❤️

| <div style="text-align: center;"><a href="https://warp.dev/llama-factory"><img alt="Warp sponsorship" width="400" src="assets/sponsors/warp.jpg"></a><br><a href="https://warp.dev/llama-factory" style="font-size:larger;">Warp，面向开发者的智能终端</a><br><a href="https://warp.dev/llama-factory">适用于 MacOS、Linux 和 Windows</a> | <a href="https://serpapi.com"><img alt="SerpAPI sponsorship" width="250" src="assets/sponsors/serpapi.svg"> </a> |
| ---- | ---- |

----

### 通过零代码 [CLI](#快速开始) 和 [Web UI](#使用-llama-board-gui-进行微调) 轻松微调 100+ 大语言模型

![GitHub Trend](https://trendshift.io/api/badge/repositories/4535)

</div>

👋 加入我们的 [微信](https://github.com/hiyouga/llamafactory-community/blob/main/wechat/main.jpg) 和 [NPU](https://github.com/hiyouga/llamafactory-community/blob/main/wechat/npu.jpg) 用户群。

\[ English | [中文](README_zh.md) \]

**微调大语言模型可以如此简单...**

https://github.com/user-attachments/assets/3991a3a8-4276-4d30-9cab-4cb0c4b9b99e

开始本地训练：
- 请参阅 [入门指南](#入门指南)

开始云端训练：
- **Colab（免费）**：https://colab.research.google.com/drive/1eRTPn37ltBbYsISy9Aw2NuI2Aq5CQrD9?usp=sharing
- **PAI-DSW（免费试用）**：https://gallery.pai-ml.com/#/preview/deepLearning/nlp/llama_factory

阅读技术笔记：
- **官方文档（进行中）**：https://llamafactory.readthedocs.io/en/latest/
- **AMD GPU 文档**：https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/llama_factory_llama3.html
- **官方博客**：https://blog.llamafactory.net/en/

> [!NOTE]
> 除上述链接外，其他网站均为未经授权的第三方站点，请谨慎使用。

## 目录

- [功能特性](#功能特性)
- [博客文章](#博客文章)
- [更新日志](#更新日志)
- [支持模型](#支持模型)
- [训练方法](#训练方法)
- [内置数据集](#内置数据集)
- [环境要求](#环境要求)
- [入门指南](#入门指南)
  - [安装](#安装)
  - [数据准备](#数据准备)
  - [快速开始](#快速开始)
  - [使用 LLaMA Board GUI 进行微调](#使用-llama-board-gui-进行微调)
  - [构建 Docker](#构建-docker)
  - [通过 OpenAI 风格 API 和 vLLM 部署](#通过-openai-风格-api-和-vllm-部署)
  - [从 ModelScope Hub 下载](#从-modelscope-hub-下载)
  - [从 Modelers Hub 下载](#从-modelers-hub-下载)
  - [使用 W&B Logger](#使用-wb-logger)
  - [使用 SwanLab Logger](#使用-swanlab-logger)
- [基于 LLaMA Factory 的项目](#基于-llama-factory-的项目)
- [开源协议](#开源协议)
- [引用](#引用)
- [致谢](#致谢)

## 功能特性

- **丰富的模型库**：LLaMA、LLaVA、Mistral、Mixtral-MoE、Qwen3、Qwen3-VL、DeepSeek、Gemma、GLM、Phi 等。
- **全面的训练方法**：（持续）预训练、（多模态）监督微调（SFT）、奖励建模、PPO、DPO、KTO、ORPO 等。
- **可扩展的资源利用**：支持 16-bit 全量微调、冻结微调、LoRA 以及通过 AQLM/AWQ/GPTQ/LLM.int8/HQQ/EETQ 实现的 2/3/4/5/6/8-bit QLoRA。
- **前沿算法集成**：[GaLore](https://github.com/jiaweizzhao/GaLore)、[BAdam](https://github.com/Ledzy/BAdam)、[APOLLO](https://github.com/zhuhanqing/APOLLO)、[Adam-mini](https://github.com/zyushun/Adam-mini)、[Muon](https://github.com/KellerJordan/Muon)、[OFT](https://github.com/huggingface/peft/tree/main/src/peft/tuners/oft)、DoRA、LongLoRA、LLaMA Pro、Mixture-of-Depths、LoRA+、LoftQ 和 PiSSA。
- **实用优化技巧**：[FlashAttention-2](https://github.com/Dao-AILab/flash-attention)、[Unsloth](https://github.com/unslothai/unsloth)、[Liger Kernel](https://github.com/linkedin/Liger-Kernel)、[KTransformers](https://github.com/kvcache-ai/ktransformers/)、RoPE 缩放、NEFTune 和 rsLoRA。
- **广泛的适用任务**：多轮对话、工具调用（Tool Use）、图像理解、视觉定位、视频识别、音频理解等。
- **实验监控支持**：LlamaBoard、TensorBoard、Wandb、MLflow、[SwanLab](https://github.com/SwanHubX/SwanLab) 等。
- **更快的推理速度**：提供 OpenAI 风格 API、Gradio UI 和 CLI，并集成 [vLLM worker](https://github.com/vllm-project/vllm) 或 [SGLang worker](https://github.com/sgl-project/sglang)。

### 紧跟前沿模型的 Day-N 微调支持

| 支持日期 | 模型名称                                                           |
| ------------ | -------------------------------------------------------------------- |
| Day 0        | Qwen3 / Qwen2.5-VL / Gemma 3 / GLM-4.1V / InternLM 3 / MiniCPM-o-2.6 |
| Day 1        | Llama 3 / GLM-4 / Mistral Small / PaliGemma2 / Llama 4               |

## 博客文章

> [!TIP]
> 我们现在拥有 LLaMA Factory 专属博客！
>
> 网站：https://blog.llamafactory.net/en/

- 💡 [KTransformers 微调 × LLaMA Factory：使用 2 张 4090 GPU + CPU 微调万亿参数模型](https://blog.llamafactory.net/en/posts/ktransformers/) (英文)
- 💡 [Easy Dataset × LLaMA Factory：让大语言模型高效学习领域知识](https://buaa-act.feishu.cn/wiki/GVzlwYcRFiR8OLkHbL6cQpYin7g) (英文)
- [基于 LLaMA-Factory 和 EasyR1 的一站式无代码模型强化学习与部署平台](https://aws.amazon.com/cn/blogs/china/building-llm-model-hub-based-on-llamafactory-and-easyr1/) (中文)
- [Apoidea Group 如何利用 LLaMA-Factory 在 Amazon SageMaker HyperPod 上通过多模态模型增强银行文档的视觉信息提取](https://aws.amazon.com/cn/blogs/machine-learning/how-apoidea-group-enhances-visual-information-extraction-from-banking-documents-with-multimodal-models-using-llama-factory-on-amazon-sagemaker-hyperpod/) (英文)

<details><summary>查看所有博客</summary>

- [LLaMA Factory：微调 DeepSeek-R1-Distill-Qwen-7B 模型用于新闻分类](https://gallery.pai-ml.com/#/preview/deepLearning/nlp/llama_factory_deepseek_r1_distill_7b) (中文)
- [基于 SageMaker 和 LLaMA-Factory 的一站式无代码模型微调与部署平台](https://aws.amazon.com/cn/blogs/china/a-one-stop-code-free-model-fine-tuning-deployment-platform-based-on-sagemaker-and-llama-factory/) (中文)
- [LLaMA Factory 多模态微调实践：微调 Qwen2-VL 打造私人导游](https://gallery.pai-ml.com/#/preview/deepLearning/nlp/llama_factory_qwen2vl) (中文)
- [LLaMA Factory：微调 Llama3 用于角色扮演](https://gallery.pai-ml.com/#/preview/deepLearning/nlp/llama_factory) (中文)

</details>

## 更新日志

[25/10/26] 我们支持了基于 [**mcore_adapter**](https://github.com/alibaba/ROLL/tree/main/mcore_adapter) 的 Megatron-core 训练后端。请参阅 [PR #9237](https://github.com/hiyouga/LLaMA-Factory/pull/9237) 获取使用指南。

[25/08/22] 我们支持了 **[OFT](https://arxiv.org/abs/2306.07280)** 和 **[OFTv2](https://arxiv.org/abs/2506.19847)**。请参阅 [examples](examples/README.md) 获取使用指南。

[25/08/20] 我们支持了微调 **[Intern-S1-mini](https://huggingface.co/internlm/Intern-S1-mini)** 模型。请参阅 [PR #8976](https://github.com/hiyouga/LLaMA-Factory/pull/8976) 获取使用指南。

[25/08/06] 我们支持了微调 **[GPT-OSS](https://github.com/openai/gpt-oss)** 模型。请参阅 [PR #8826](https://github.com/hiyouga/LLaMA-Factory/pull/8826) 获取使用指南。

<details><summary>完整更新日志</summary>

[25/07/02] 我们支持了微调 **[GLM-4.1V-9B-Thinking](https://github.com/THUDM/GLM-4.1V-Thinking)** 模型。

[25/04/28] 我们支持了微调 **[Qwen3](https://qwenlm.github.io/blog/qwen3/)** 系列模型。

[25/04/21] 我们支持了 **[Muon](https://github.com/KellerJordan/Muon)** 优化器。请参阅 [examples](examples/README.md) 获取使用指南。感谢 [@tianshijing](https://github.com/tianshijing) 的 PR。

[25/04/16] 我们支持了微调 **[InternVL3](https://huggingface.co/OpenGVLab/InternVL3-8B)** 模型。请参阅 [PR #7258](https://github.com/hiyouga/LLaMA-Factory/pull/7258) 获取使用指南。

[25/04/14] 我们支持了微调 **[GLM-Z1](https://huggingface.co/THUDM/GLM-Z1-9B-0414)** 和 **[Kimi-VL](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct)** 模型。

[25/04/06] 我们支持了微调 **[Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)** 模型。请参阅 [PR #7611](https://github.com/hiyouga/LLaMA-Factory/pull/7611) 获取使用指南。

[25/03/31] 我们支持了微调 **[Qwen2.5 Omni](https://qwenlm.github.io/blog/qwen2.5-omni/)** 模型。请参阅 [PR #7537](https://github.com/hiyouga/LLaMA-Factory/pull/7537) 获取使用指南。

[25/03/15] 我们支持了 **[SGLang](https://github.com/sgl-project/sglang)** 作为推理后端。尝试设置 `infer_backend: sglang` 以加速推理。

[25/03/12] 我们支持了微调 **[Gemma 3](https://huggingface.co/blog/gemma3)** 模型。

[25/02/24] 发布 **[EasyR1](https://github.com/hiyouga/EasyR1)**，一个高效、可扩展且支持多模态的 GRPO 强化学习训练框架。

[25/02/11] 我们支持了在导出模型权重时保存 **[Ollama](https://github.com/ollama/ollama)** modelfile。请参阅 [examples](examples/README.md) 获取使用指南。

[25/02/05] 我们支持了音频理解任务上的 **[Qwen2-Audio](Qwen/Qwen2-Audio-7B-Instruct)** 和 **[MiniCPM-o-2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6)** 微调。

[25/01/31] 我们支持了微调 **[DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)** 和 **[Qwen2.5-VL](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)** 模型。

[25/01/15] 我们支持了 **[APOLLO](https://arxiv.org/abs/2412.05270)** 优化器。请参阅 [examples](examples/README.md) 获取使用指南。

[25/01/14] 我们支持了微调 **[MiniCPM-o-2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6)** 和 **[MiniCPM-V-2.6](https://huggingface.co/openbmb/MiniCPM-V-2_6)** 模型。感谢 [@BUAADreamer](https://github.com/BUAADreamer) 的 PR。

[25/01/14] 我们支持了微调 **[InternLM 3](https://huggingface.co/collections/internlm/)** 系列模型。感谢 [@hhaAndroid](https://github.com/hhaAndroid) 的 PR。

[25/01/10] 我们支持了微调 **[Phi-4](https://huggingface.co/microsoft/phi-4)** 模型。

[24/12/21] 我们支持使用 **[SwanLab](https://github.com/SwanHubX/SwanLab)** 进行实验追踪和可视化。详见 [此章节](#使用-swanlab-logger)。

[24/11/27] 我们支持了微调 **[Skywork-o1](https://huggingface.co/Skywork/Skywork-o1-Open-Llama-3.1-8B)** 模型和 **[OpenO1](https://huggingface.co/datasets/O1-OPEN/OpenO1-SFT)** 数据集。

[24/10/09] 我们支持从 **[Modelers Hub](https://modelers.cn/models)** 下载预训练模型和数据集。详见 [此教程](#从-modelers-hub-下载)。

[24/09/19] 我们支持了微调 **[Qwen2.5](https://qwenlm.github.io/blog/qwen2.5/)** 系列模型。

[24/08/30] 我们支持了微调 **[Qwen2-VL](https://qwenlm.github.io/blog/qwen2-vl/)** 系列模型。感谢 [@simonJJJ](https://github.com/simonJJJ) 的 PR。

[24/08/27] 我们支持了 **[Liger Kernel](https://github.com/linkedin/Liger-Kernel)**。尝试设置 `enable_liger_kernel: true` 以实现高效训练。

[24/08/09] 我们支持了 **[Adam-mini](https://github.com/zyushun/Adam-mini)** 优化器。请参阅 [examples](examples/README.md) 获取使用指南。感谢 [@relic-yuexi](https://github.com/relic-yuexi) 的 PR。

[24/07/04] 我们支持了 [无污染打包训练](https://github.com/MeetKai/functionary/tree/main/functionary/train/packing)。使用 `neat_packing: true` 激活该功能。感谢 [@chuan298](https://github.com/chuan298) 的 PR。

[24/06/16] 我们支持了 **[PiSSA](https://arxiv.org/abs/2404.02948)** 算法。请参阅 [examples](examples/README.md) 获取使用指南。

[24/06/07] 我们支持了微调 **[Qwen2](https://qwenlm.github.io/blog/qwen2/)** 和 **[GLM-4](https://github.com/THUDM/GLM-4)** 模型。

[24/05/26] 我们支持了用于偏好学习的 **[SimPO](https://arxiv.org/abs/2405.14734)** 算法。请参阅 [examples](examples/README.md) 获取使用指南。

[24/05/20] 我们支持了微调 **PaliGemma** 系列模型。请注意，PaliGemma 是预训练模型，你需要使用 `paligemma` 模板对其进行微调以完成对话补全任务。

[24/05/18] 我们支持了用于偏好学习的 **[KTO](https://arxiv.org/abs/2402.01306)** 算法。请参阅 [examples](examples/README.md) 获取使用指南。

[24/05/14] 我们支持了在昇腾 NPU 设备上训练和推理。详见 [安装](#安装) 章节。

[24/04/26] 我们支持了微调 **LLaVA-1.5** 多模态大语言模型。请参阅 [examples](examples/README.md) 获取使用指南。

[24/04/22] 我们提供了一个 **[Colab 笔记本](https://colab.research.google.com/drive/1eRTPn37ltBbYsISy9Aw2NuI2Aq5CQrD9?usp=sharing)**，用于在免费的 T4 GPU 上微调 Llama-3 模型。Hugging Face 上有两个使用 LLaMA Factory 微调的 Llama-3 衍生模型可供下载，详见 [Llama3-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat) 和 [Llama3-Chinese](https://huggingface.co/zhichen/Llama3-Chinese)。

[24/04/21] 我们根据 [AstraMindAI 的实现](https://github.com/astramind-ai/Mixture-of-depths) 支持了 **[Mixture-of-Depths](https://arxiv.org/abs/2404.02258)**。请参阅 [examples](examples/README.md) 获取使用指南。

[24/04/16] 我们支持了 **[BAdam](https://arxiv.org/abs/2404.02827)** 优化器。请参阅 [examples](examples/README.md) 获取使用指南。

[24/04/16] 我们支持了 **[unsloth](https://github.com/unslothai/unsloth)** 的长序列训练（在 24GB 显存下运行 Llama-2-7B-56k）。与 FlashAttention-2 相比，它实现了 **117%** 的速度和 **50%** 的内存节省。更多基准测试详见 [此页面](https://github.com/hiyouga/LLaMA-Factory/wiki/Performance-comparison)。

[24/03/31] 我们支持了 **[ORPO](https://arxiv.org/abs/2403.07691)**。请参阅 [examples](examples/README.md) 获取使用指南。

[24/03/21] 我们的论文 "[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://arxiv.org/abs/2403.13372)" 已收录于 arXiv！

[24/03/20] 我们支持了 **FSDP+QLoRA**，可在 2x24GB GPU 上微调 70B 模型。请参阅 [examples](examples/README.md) 获取使用指南。

[24/03/13] 我们支持了 **[LoRA+](https://arxiv.org/abs/2402.12354)**。请参阅 [examples](examples/README.md) 获取使用指南。

[24/03/07] 我们支持了 **[GaLore](https://arxiv.org/abs/2403.03507)** 优化器。请参阅 [examples](examples/README.md) 获取使用指南。

[24/03/07] 我们集成了 **[vLLM](https://github.com/vllm-project/vllm)** 以实现更快、并行的推理。尝试设置 `infer_backend: vllm` 以享受 **270%** 的推理速度提升。

[24/02/28] 我们支持了基于权重分解的 LoRA（即 **[DoRA](https://arxiv.org/abs/2402.09353)**）。尝试设置 `use_dora: true` 以激活 DoRA 训练。

[24/02/15] 我们支持了 [LLaMA Pro](https://github.com/TencentARC/LLaMA-Pro) 提出的 **块扩展（Block Expansion）** 技术。请参阅 [examples](examples/README.md) 获取使用指南。

[24/02/05] Qwen1.5 (Qwen2 beta version) 系列模型已支持 LLaMA-Factory。详见此 [博客文章](https://qwenlm.github.io/blog/qwen1.5/)。

[24/01/18] 我们支持了大多数模型的 **Agent 微调**，通过 `dataset: glaive_toolcall_en` 数据集微调赋予模型工具调用能力。

[23/12/23] 我们支持了 **[unsloth](https://github.com/unslothai/unsloth)** 的实现以加速 LLaMA、Mistral 和 Yi 模型的 LoRA 微调。尝试设置 `use_unsloth: true` 参数激活 unsloth patch。在我们的基准测试中速度提升了 **170%**，详见 [此页面](https://github.com/hiyouga/LLaMA-Factory/wiki/Performance-comparison)。

[23/12/12] 我们支持了在框架内微调最新的 MoE 模型 **[Mixtral 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)**。硬件要求详见 [此处](#硬件要求)。

[23/12/01] 我们支持从 **[ModelScope Hub](https://modelscope.cn/models)** 下载预训练模型和数据集。详见 [此教程](#从-modelscope-hub-下载)。

[23/10/21] 我们支持了微调技巧 **[NEFTune](https://arxiv.org/abs/2310.05914)**。尝试设置 `neftune_noise_alpha: 5` 参数激活 NEFTune。

[23/09/27] 我们为 LLaMA 模型支持了 [LongLoRA](https://github.com/dvlab-research/LongLoRA) 提出的 **$S^2$-Attn**。尝试设置 `shift_attn: true` 参数启用移位短注意力机制。

[23/09/23] 我们在仓库中集成了 MMLU、C-Eval 和 CMMLU 基准测试工具。请参阅 [examples](examples/README.md) 获取使用指南。

[23/09/10] 我们支持了 **[FlashAttention-2](https://github.com/Dao-AILab/flash-attention)**。如果你使用的是 RTX4090、A100 或 H100 GPU，尝试设置 `flash_attn: fa2` 参数启用 FlashAttention-2。

[23/08/12] 我们支持了 **RoPE Scaling** 以扩展 LLaMA 模型的上下文长度。训练时使用 `rope_scaling: linear` 参数，推理时使用 `rope_scaling: dynamic` 参数进行位置外推。

[23/08/11] 我们支持了指令微调模型的 **[DPO 训练](https://arxiv.org/abs/2305.18290)**。请参阅 [examples](examples/README.md) 获取使用指南。

[23/07/31] 我们支持了 **数据集流式加载**。尝试设置 `streaming: true` 和 `max_steps: 10000` 参数以流式模式加载你的数据集。

[23/07/29] 我们在 Hugging Face 上发布了两款指令微调的 13B 模型。详见这些 Hugging Face 仓库（[LLaMA-2](https://huggingface.co/hiyouga/Llama-2-Chinese-13b-chat) / [Baichuan](https://huggingface.co/hiyouga/Baichuan-13B-sft))。

[23/07/18] 我们开发了用于训练、评估和推理的 **一体化 Web UI**。尝试运行 `train_web.py` 在浏览器中微调模型。感谢 [@KanadeSiina](https://github.com/KanadeSiina) 和 [@codemayq](https://github.com/codemayq) 的开发贡献。

[23/07/09] 我们发布了 **[FastEdit](https://github.com/hiyouga/FastEdit)** ⚡🩹，一个易于使用的包，用于高效编辑大语言模型的事实性知识。如果你感兴趣请跟进 [FastEdit](https://github.com/hiyouga/FastEdit)。

[23/06/29] 我们提供了一个使用指令跟随数据集训练对话模型的 **可复现示例**，详见 [Baichuan-7B-sft](https://huggingface.co/hiyouga/Baichuan-7B-sft)。

[23/06/22] 我们对齐了 [demo API](src/api_demo.py) 与 **[OpenAI's](https://platform.openai.com/docs/api-reference/chat)** 格式，使你能够将微调模型嵌入 **任意基于 ChatGPT 的应用程序**中。

[23/06/03] 我们支持了量化训练和推理（即 **[QLoRA](https://github.com/artidoro/qlora)**）。请参阅 [examples](examples/README.md) 获取使用指南。

</details>

> [!TIP]
> 如果你无法使用最新功能，请拉取最新代码并重新安装 LLaMA-Factory。

## 支持模型

| Model                                                             | Model size                       | Template             |
| ----------------------------------------------------------------- | -------------------------------- | -------------------- |
| [BLOOM/BLOOMZ](https://huggingface.co/bigscience)                 | 560M/1.1B/1.7B/3B/7.1B/176B      | -                    |
| [DeepSeek (LLM/Code/MoE)](https://huggingface.co/deepseek-ai)     | 7B/16B/67B/236B                  | deepseek             |
| [DeepSeek 3-3.2](https://huggingface.co/deepseek-ai)              | 236B/671B                        | deepseek3            |
| [DeepSeek R1 (Distill)](https://huggingface.co/deepseek-ai)       | 1.5B/7B/8B/14B/32B/70B/671B      | deepseekr1           |
| [ERNIE-4.5](https://huggingface.co/baidu)                         | 0.3B/21B/300B                    | ernie_nothink        |
| [Falcon/Falcon H1](https://huggingface.co/tiiuae)                 | 0.5B/1.5B/3B/7B/11B/34B/40B/180B | falcon/falcon_h1     |
| [Gemma/Gemma 2/CodeGemma](https://huggingface.co/google)          | 2B/7B/9B/27B                     | gemma/gemma2         |
| [Gemma 3/Gemma 3n](https://huggingface.co/google)                 | 270M/1B/4B/6B/8B/12B/27B         | gemma3/gemma3n       |
| [GLM-4/GLM-4-0414/GLM-Z1](https://huggingface.co/zai-org)         | 9B/32B                           | glm4/glmz1           |
| [GLM-4.5/GLM-4.5(6)V](https://huggingface.co/zai-org)             | 9B/106B/355B                     | glm4_moe/glm4_5v     |
| [GPT-2](https://huggingface.co/openai-community)                  | 0.1B/0.4B/0.8B/1.5B              | -                    |
| [GPT-OSS](https://huggingface.co/openai)                          | 20B/120B                         | gpt_oss              |
| [Granite 3-4](https://huggingface.co/ibm-granite)                 | 1B/2B/3B/7B/8B                   | granite3/granite4    |
| [Hunyuan/Hunyuan1.5 (MT)](https://huggingface.co/tencent/)        | 0.5B/1.8B/4B/7B/13B              | hunyuan/hunyuan_small|
| [InternLM 2-3](https://huggingface.co/internlm)                   | 7B/8B/20B                        | intern2              |
| [InternVL 2.5-3.5](https://huggingface.co/OpenGVLab)              | 1B/2B/4B/8B/14B/30B/38B/78B/241B | intern_vl            |
| [Intern-S1-mini](https://huggingface.co/internlm/)                | 8B                               | intern_s1            |
| [Kimi-VL](https://huggingface.co/moonshotai)                      | 16B                              | kimi_vl              |
| [Ling 2.0 (mini/flash)](https://huggingface.co/inclusionAI)       | 16B/100B                         | bailing_v2           |
| [LFM 2.5 (VL)](https://huggingface.co/LiquidAI)                   | 1.2B/1.6B                        | lfm2/lfm2_vl         |
| [Llama](https://github.com/facebookresearch/llama)                | 7B/13B/33B/65B                   | -                    |
| [Llama 2](https://huggingface.co/meta-llama)                      | 7B/13B/70B                       | llama2               |
| [Llama 3-3.3](https://huggingface.co/meta-llama)                  | 1B/3B/8B/70B                     | llama3               |
| [Llama 4](https://huggingface.co/meta-llama)                      | 109B/402B                        | llama4               |
| [Llama 3.2 Vision](https://huggingface.co/meta-llama)             | 11B/90B                          | mllama               |
| [LLaVA-1.5](https://huggingface.co/llava-hf)                      | 7B/13B                           | llava                |
| [LLaVA-NeXT](https://huggingface.co/llava-hf)                     | 7B/8B/13B/34B/72B/110B           | llava_next           |
| [LLaVA-NeXT-Video](https://huggingface.co/llava-hf)               | 7B/34B                           | llava_next_video     |
| [MiMo](https://huggingface.co/XiaomiMiMo)                         | 7B/309B                          | mimo/mimo_v2         |
| [MiniCPM 4](https://huggingface.co/openbmb)                       | 0.5B/8B                          | cpm4                 |
| [MiniCPM-o/MiniCPM-V 4.5](https://huggingface.co/openbmb)         | 8B/9B                            | minicpm_o/minicpm_v  |
| [MiniMax-M1/MiniMax-M2](https://huggingface.co/MiniMaxAI/models)  | 229B/456B                        | minimax1/minimax2    |
| [Ministral 3](https://huggingface.co/mistralai)                   | 3B/8B/14B                        | ministral3           |
| [Mistral/Mixtral](https://huggingface.co/mistralai)               | 7B/8x7B/8x22B                    | mistral              |
| [PaliGemma/PaliGemma2](https://huggingface.co/google)             | 3B/10B/28B                       | paligemma            |
| [Phi-3/Phi-3.5](https://huggingface.co/microsoft)                 | 4B/14B                           | phi                  |
| [Phi-3-small](https://huggingface.co/microsoft)                   | 7B                               | phi_small            |
| [Phi-4-mini/Phi-4](https://huggingface.co/microsoft)              | 3.8B/14B                         | phi4_mini/phi4       |
| [Pixtral](https://huggingface.co/mistralai)                       | 12B                              | pixtral              |
| [Qwen2 (Code/Math/MoE/QwQ)](https://huggingface.co/Qwen)          | 0.5B/1.5B/3B/7B/14B/32B/72B/110B | qwen                 |
| [Qwen3 (MoE/Instruct/Thinking/Next)](https://huggingface.co/Qwen) | 0.6B/1.7B/4B/8B/14B/32B/80B/235B | qwen3/qwen3_nothink  |
| [Qwen3.5](https://huggingface.co/Qwen)                            | 0.8B/2B/4B/9B/27B/35B/122B/397B  | qwen3_5/qwen3_5_nothink              |
| [Qwen3.6](https://huggingface.co/Qwen)                            | 27B/35B                          | qwen3_6              |
| [Qwen2-Audio](https://huggingface.co/Qwen)                        | 7B                               | qwen2_audio          |
| [Qwen2.5-Omni](https://huggingface.co/Qwen)                       | 3B/7B                            | qwen2_omni           |
| [Qwen3-Omni](https://huggingface.co/Qwen)                         | 30B                              | qwen3_omni           |
| [Qwen2-VL/Qwen2.5-VL/QVQ](https://huggingface.co/Qwen)            | 2B/3B/7B/32B/72B                 | qwen2_vl             |
| [Qwen3-VL](https://huggingface.co/Qwen)                           | 2B/4B/8B/30B/32B/235B            | qwen3_vl             |
| [Seed (OSS/Coder)](https://huggingface.co/ByteDance-Seed)         | 8B/36B                           | seed_oss/seed_coder  |
| [StarCoder 2](https://huggingface.co/bigcode)                     | 3B/7B/15B                        | -                    |
| [TeleChat 2-2.5](https://huggingface.co/Tele-AI)                  | 3B/7B/35B/115B                   | telechat2            |
| [Yuan 2](https://huggingface.co/IEITYuan)                         | 2B/51B/102B                      | yuan                 |

> [!NOTE]
> 对于 "base" 模型，`template` 参数可选择 `default`、`alpaca`、`vicuna` 等。但对于 "instruct/chat" 模型，请务必使用**对应的模板**。
>
> 如果模型同时提供推理（Thinking）和非推理版本，请使用 `_nothink` 后缀进行区分。例如：`qwen3` 和 `qwen3_nothink`。
>
> 请确保在训练和推理时使用**相同**的模板。
>
> \*: 你需要从 main 分支安装 `transformers` 并设置 `DISABLE_VERSION_CHECK=1` 以跳过版本检查。
>
> \*\*: 你需要安装特定版本的 `transformers` 才能使用对应的模型。

完整支持的模型列表请参阅 [constants.py](src/llamafactory/extras/constants.py)。

你也可以向 [template.py](src/llamafactory/data/template.py) 添加自定义对话模板。

## 训练方法

| Approach               |     Full-tuning    |    Freeze-tuning   |       LoRA         |       QLoRA        |        OFT         |        QOFT        |
| ---------------------- | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| Pre-Training           | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Supervised Fine-Tuning | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Reward Modeling        | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| PPO Training           | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| DPO Training           | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| KTO Training           | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| ORPO Training          | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| SimPO Training         | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |

> [!TIP]
> PPO 的实现细节详见 [此博客](https://newfacade.github.io/notes-on-reinforcement-learning/17-ppo-trl.html)。

## 内置数据集

<details><summary>预训练数据集</summary>

- [Wiki Demo (en)](data/wiki_demo.txt)
- [RefinedWeb (en)](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)
- [RedPajama V2 (en)](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-V2)
- [Wikipedia (en)](https://huggingface.co/datasets/olm/olm-wikipedia-20221220)
- [Wikipedia (zh)](https://huggingface.co/datasets/pleisto/wikipedia-cn-20230720-filtered)
- [Pile (en)](https://huggingface.co/datasets/EleutherAI/pile)
- [SkyPile (zh)](https://huggingface.co/datasets/Skywork/SkyPile-150B)
- [FineWeb (en)](https://huggingface.co/datasets/HuggingFaceFW/fineweb)
- [FineWeb-Edu (en)](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)
- [CCI3-HQ (zh)](https://huggingface.co/datasets/BAAI/CCI3-HQ)
- [CCI3-Data (zh)](https://huggingface.co/datasets/BAAI/CCI3-Data)
- [CCI4.0-M2-Base-v1 (en&zh)](https://huggingface.co/datasets/BAAI/CCI4.0-M2-Base-v1)
- [CCI4.0-M2-CoT-v1 (en&zh)](https://huggingface.co/datasets/BAAI/CCI4.0-M2-CoT-v1)
- [CCI4.0-M2-Extra-v1 (en&zh)](https://huggingface.co/datasets/BAAI/CCI4.0-M2-Extra-v1)
- [The Stack (en)](https://huggingface.co/datasets/bigcode/the-stack)
- [StarCoder (en)](https://huggingface.co/datasets/bigcode/starcoderdata)

</details>

<details><summary>监督微调数据集</summary>

- [Identity (en&zh)](data/identity.json)
- [Stanford Alpaca (en)](https://github.com/tatsu-lab/stanford_alpaca)
- [Stanford Alpaca (zh)](https://github.com/ymcui/Chinese-LLaMA-Alpaca-3)
- [Alpaca GPT4 (en&zh)](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
- [Glaive Function Calling V2 (en&zh)](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2)
- [LIMA (en)](https://huggingface.co/datasets/GAIR/lima)
- [Guanaco Dataset (multilingual)](https://huggingface.co/datasets/JosephusCheung/GuanacoDataset)
- [BELLE 2M (zh)](https://huggingface.co/datasets/BelleGroup/train_2M_CN)
- [BELLE 1M (zh)](https://huggingface.co/datasets/BelleGroup/train_1M_CN)
- [BELLE 0.5M (zh)](https://huggingface.co/datasets/BelleGroup/train_0.5M_CN)
- [BELLE Dialogue 0.4M (zh)](https://huggingface.co/datasets/BelleGroup/generated_chat_0.4M)
- [BELLE School Math 0.25M (zh)](https://huggingface.co/datasets/BelleGroup/school_math_0.25M)
- [BELLE Multiturn Chat 0.8M (zh)](https://huggingface.co/datasets/BelleGroup/multiturn_chat_0.8M)
- [UltraChat (en)](https://github.com/thunlp/UltraChat)
- [OpenPlatypus (en)](https://huggingface.co/datasets/garage-bAInd/Open-Platypus)
- [CodeAlpaca 20k (en)](https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k)
- [Alpaca CoT (multilingual)](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT)
- [OpenOrca (en)](https://huggingface.co/datasets/Open-Orca/OpenOrca)
- [SlimOrca (en)](https://huggingface.co/datasets/Open-Orca/SlimOrca)
- [MathInstruct (en)](https://huggingface.co/datasets/TIGER-Lab/MathInstruct)
- [Firefly 1.1M (zh)](https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M)
- [Wiki QA (en)](https://huggingface.co/datasets/wiki_qa)
- [Web QA (zh)](https://huggingface.co/datasets/suolyer/webqa)
- [WebNovel (zh)](https://huggingface.co/datasets/zxbsmk/webnovel_cn)
- [Nectar (en)](https://huggingface.co/datasets/berkeley-nest/Nectar)
- [deepctrl (en&zh)](https://www.modelscope.cn/datasets/deepctrl/deepctrl-sft-data)
- [Advertise Generating (zh)](https://huggingface.co/datasets/HasturOfficial/adgen)
- [ShareGPT Hyperfiltered (en)](https://huggingface.co/datasets/totally-not-an-llm/sharegpt-hyperfiltered-3k)
- [ShareGPT4 (en&zh)](https://huggingface.co/datasets/shibing624/sharegpt_gpt4)
- [UltraChat 200k (en)](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k)
- [Infinity Instruct (zh)](https://huggingface.co/datasets/BAAI/Infinity-Instruct)
- [AgentInstruct (en)](https://huggingface.co/datasets/THUDM/AgentInstruct)
- [LMSYS Chat 1M (en)](https://huggingface.co/datasets/lmsys/lmsys-chat-1m)
- [Evol Instruct V2 (en)](https://huggingface.co/datasets/WizardLM/WizardLM_evol_instruct_V2_196k)
- [Cosmopedia (en)](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia)
- [STEM (zh)](https://huggingface.co/datasets/hfl/stem_zh_instruction)
- [Ruozhiba (zh)](https://huggingface.co/datasets/hfl/ruozhiba_gpt4_turbo)
- [Neo-sft (zh)](https://huggingface.co/datasets/m-a-p/neo_sft_phase2)
- [Magpie-Pro-300K-Filtered (en)](https://huggingface.co/datasets/Magpie-Align/Magpie-Pro-300K-Filtered)
- [Magpie-ultra-v0.1 (en)](https://huggingface.co/datasets/argilla/magpie-ultra-v0.1)
- [WebInstructSub (en)](https://huggingface.co/datasets/TIGER-Lab/WebInstructSub)
- [OpenO1-SFT (en&zh)](https://huggingface.co/datasets/O1-OPEN/OpenO1-SFT)
- [Open-Thoughts (en)](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k)
- [Open-R1-Math (en)](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k)
- [Chinese-DeepSeek-R1-Distill (zh)](https://huggingface.co/datasets/Congliu/Chinese-DeepSeek-R1-Distill-data-110k-SFT)
- [LLaVA mixed (en&zh)](https://huggingface.co/datasets/BUAADreamer/llava-en-zh-300k)
- [Pokemon-gpt4o-captions (en&zh)](https://huggingface.co/datasets/jugg1024/pokemon-gpt4o-captions)
- [DLR-Web (en)](https://huggingface.co/datasets/Attention1115/DLR-Web)
- [Open Assistant (de)](https://huggingface.co/datasets/mayflowergmbh/oasst_de)
- [Dolly 15k (de)](https://huggingface.co/datasets/mayflowergmbh/dolly-15k_de)
- [Alpaca GPT4 (de)](https://huggingface.co/datasets/mayflowergmbh/alpaca-gpt4_de)
- [OpenSchnabeltier (de)](https://huggingface.co/datasets/mayflowergmbh/openschnabeltier_de)
- [Evol Instruct (de)](https://huggingface.co/datasets/mayflowergmbh/evol-instruct_de)
- [Dolphin (de)](https://huggingface.co/datasets/mayflowergmbh/dolphin_de)
- [Booksum (de)](https://huggingface.co/datasets/mayflowergmbh/booksum_de)
- [Airoboros (de)](https://huggingface.co/datasets/mayflowergmbh/airoboros-3.0_de)
- [Ultrachat (de)](https://huggingface.co/datasets/mayflowergmbh/ultra-chat_de)

</details>

<details><summary>偏好数据集</summary>

- [DPO mixed (en&zh)](https://huggingface.co/datasets/hiyouga/DPO-En-Zh-20k)
- [UltraFeedback (en)](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized)
- [COIG-P (zh)](https://huggingface.co/datasets/m-a-p/COIG-P)
- [RLHF-V (en)](https://huggingface.co/datasets/openbmb/RLHF-V-Dataset)
- [VLFeedback (en)](https://huggingface.co/datasets/Zhihui/VLFeedback)
- [RLAIF-V (en)](https://huggingface.co/datasets/openbmb/RLAIF-V-Dataset)
- [Orca DPO Pairs (en)](https://huggingface.co/datasets/Intel/orca_dpo_pairs)
- [HH-RLHF (en)](https://huggingface.co/datasets/Anthropic/hh-rlhf)
- [Nectar (en)](https://huggingface.co/datasets/berkeley-nest/Nectar)
- [Orca DPO (de)](https://huggingface.co/datasets/mayflowergmbh/intel_orca_dpo_pairs_de)
- [KTO mixed (en)](https://huggingface.co/datasets/argilla/kto-mix-15k)

</details>

部分数据集在使用前需要确认许可，因此我们建议你使用以下命令通过 Hugging Face 账号登录：

```bash
pip install "huggingface_hub<1.0.0"
huggingface-cli login
```

## 环境要求

| Mandatory    | Minimum | Recommend |
| ------------ | ------- | --------- |
| python       | 3.11     | >=3.11   |
| torch        | 2.0.0   | 2.6.0     |
| torchvision  | 0.15.0  | 0.21.0    |
| transformers | 4.49.0  | 4.50.0    |
| datasets     | 2.16.0  | 3.2.0     |
| accelerate   | 0.34.0  | 1.2.1     |
| peft         | 0.14.0  | 0.15.1    |
| trl          | 0.8.6   | 0.9.6     |

| Optional     | Minimum | Recommend |
| ------------ | ------- | --------- |
| CUDA         | 11.6    | 12.2      |
| deepspeed    | 0.10.0  | 0.16.4    |
| bitsandbytes | 0.39.0  | 0.43.1    |
| vllm         | 0.4.3   | 0.8.2     |
| flash-attn   | 2.5.6   | 2.7.2     |

### 硬件要求

\* *估算值*

| Method                              | Bits |   7B  |  14B  |  30B  |   70B  |   `x`B  |
| ----------------------------------- | ---- | ----- | ----- | ----- | ------ | ------- |
| Full (`bf16` or `fp16`)             |  32  | 120GB | 240GB | 600GB | 1200GB | `18x`GB |
| Full (`pure_bf16`)                  |  16  |  60GB | 120GB | 300GB |  600GB |  `8x`GB |
| Freeze/LoRA/GaLore/APOLLO/BAdam/OFT |  16  |  16GB |  32GB |  64GB |  160GB |  `2x`GB |
| QLoRA / QOFT                        |   8  |  10GB |  20GB |  40GB |   80GB |   `x`GB |
| QLoRA / QOFT                        |   4  |   6GB |  12GB |  24GB |   48GB | `x/2`GB |
| QLoRA / QOFT                        |   2  |   4GB |   8GB |  16GB |   24GB | `x/4`GB |

## 入门指南

### 安装

> [!IMPORTANT]
> 必须执行安装步骤。

#### 从源码安装

```bash
git clone --depth 1 https://github.com/hiyouga/LlamaFactory.git
cd LlamaFactory
pip install -e .
pip install -r requirements/metrics.txt
```

可选依赖：`metrics`, `deepspeed`。安装命令：`pip install -e . && pip install -r requirements/metrics.txt -r requirements/deepspeed.txt`

特定功能的额外依赖位于 `examples/requirements/` 中。

#### 从 Docker 镜像运行

```bash
docker run -it --rm --gpus=all --ipc=host hiyouga/llamafactory:latest
```

该镜像基于 Ubuntu 22.04 (x86_64)、CUDA 12.4、Python 3.11、PyTorch 2.6.0 和 Flash-attn 2.7.4 构建。

预构建镜像地址：https://hub.docker.com/r/hiyouga/llamafactory/tags

请参阅 [构建 Docker](#构建-docker) 自行构建镜像。

<details><summary>使用 <b>uv</b> 设置虚拟环境</summary>

使用 [uv](https://github.com/astral-sh/uv) 创建隔离的 Python 环境：

```bash
uv run llamafactory-cli webui
```

</details>

<details><summary>Windows 用户须知</summary>

#### 安装 PyTorch

在 Windows 平台上，你需要手动安装 GPU 版本的 PyTorch。请参阅 [官方网站](https://pytorch.org/get-started/locally/) 并使用以下命令安装支持 CUDA 的 PyTorch：

```bash
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
python -c "import torch; print(torch.cuda.is_available())"
```

如果输出 `True`，则表示已成功安装支持 CUDA 的 PyTorch。

如果遇到 `Can't pickle local object` 错误，请尝试设置 `dataloader_num_workers: 0`。

#### 安装 BitsAndBytes

如果你想在 Windows 平台上启用量化 LoRA（QLoRA），你需要安装预编译版的 `bitsandbytes` 库（支持 CUDA 11.1 至 12.2）。请根据你的 CUDA 版本选择合适的 [发布版](https://github.com/jllllll/bitsandbytes-windows-webui/releases/tag/wheels)。

```bash
pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.2.post2-py3-none-win_amd64.whl
```

#### 安装 Flash Attention-2

要在 Windows 平台上启用 FlashAttention-2，请使用来自 [flash-attention-windows-wheel](https://huggingface.co/lldacing/flash-attention-windows-wheel) 的脚本自行编译并安装。

</details>

<details><summary>昇腾 NPU 用户须知</summary>

若要在昇腾 NPU 设备上安装 LLaMA Factory，请将 Python 升级至 3.10 或更高版本：`pip install -r requirements/npu.txt`。此外，你还需要安装 **Ascend CANN Toolkit and Kernels**。请参阅 [安装教程](https://llamafactory.readthedocs.io/en/latest/advanced/npu_installation.html)。

你也可以下载预构建的 Docker 镜像：

```bash
# Docker Hub
docker pull hiyouga/llamafactory:latest-npu-a2
docker pull hiyouga/llamafactory:latest-npu-a3

# quay.io
docker pull quay.io/ascend/llamafactory:latest-npu-a2
docker pull quay.io/ascend/llamafactory:latest-npu-a3
```

#### 安装 BitsAndBytes

若要在昇腾 NPU 上使用基于 bitsandbytes 的 QLoRA，请遵循以下三个步骤：

1. 手动编译 bitsandbytes：参考 [bitsandbytes 官方文档](https://huggingface.co/docs/bitsandbytes/installation?backend=Ascend+NPU&platform=Ascend+NPU) 完成 NPU 版本的编译与安装。编译需要 cmake >= 3.22.1 和 g++ >= 12.x。

```bash
# 从源码安装 bitsandbytes
# 克隆 bitsandbytes 仓库，昇腾 NPU 后端目前在 multi-backend-refactor 分支上启用
git clone -b multi-backend-refactor https://github.com/bitsandbytes-foundation/bitsandbytes.git
cd bitsandbytes/

# 安装依赖
pip install -r requirements-dev.txt

# 安装编译工具依赖。请注意，此步骤的命令可能因操作系统而异，以下仅供参考
apt-get install -y build-essential cmake

# 编译并安装  
cmake -DCOMPUTE_BACKEND=npu -S .
make
pip install .
```

2. 从 main 分支安装 transformers。

```bash
git clone -b main https://github.com/huggingface/transformers.git
cd transformers
pip install .
```

3. 在配置中设置 `double_quantization: false`。可参考 [示例](examples/train_qlora/qwen3_lora_sft_bnb_npu.yaml)。

</details>

### 数据准备

数据集文件格式详情请参阅 [data/README.md](data/README.md)。你可以使用 HuggingFace / ModelScope / Modelers Hub 上的数据集，加载本地磁盘中的数据，或指定 s3/gcs 云存储路径。

> [!NOTE]
> 请使用自定义数据集时更新 `data/dataset_info.json`。

你还可以使用 **[Easy Dataset](https://github.com/ConardLi/easy-dataset)**、**[DataFlow](https://github.com/OpenDCAI/DataFlow)** 和 **[GraphGen](https://github.com/open-sciencelab/GraphGen)** 创建合成数据用于微调。

### 快速开始

分别使用以下 3 条命令对 Qwen3-4B-Instruct 模型执行 LoRA **微调**、**推理**和**合并**。

```bash
llamafactory-cli train examples/train_lora/qwen3_lora_sft.yaml
llamafactory-cli chat examples/inference/qwen3_lora_sft.yaml
llamafactory-cli export examples/merge_lora/qwen3_lora_sft.yaml
```

高级用法（包括分布式训练）请参阅 [examples/README.md](examples/README.md)。

> [!TIP]
> 使用 `llamafactory-cli help` 查看帮助信息。
>
> 如果遇到任何问题，请先查阅 [常见问题解答 (FAQs)](https://github.com/hiyouga/LLaMA-Factory/issues/4614)。

### 使用 LLaMA Board GUI 进行微调（由 [Gradio](https://github.com/gradio-app/gradio) 驱动）

```bash
llamafactory-cli webui
```

### 构建 Docker

CUDA 用户：

```bash
cd docker/docker-cuda/
docker compose up -d
docker compose exec llamafactory bash
```

昇腾 NPU 用户：

```bash
cd docker/docker-npu/
docker compose up -d
docker compose exec llamafactory bash
```

AMD ROCm 用户：

```bash
cd docker/docker-rocm/
docker compose up -d
docker compose exec llamafactory bash
```

<details><summary>不使用 Docker Compose 构建</summary>

CUDA 用户：

```bash
docker build -f ./docker/docker-cuda/Dockerfile \
    --build-arg PIP_INDEX=https://pypi.org/simple \
    -t llamafactory:latest .

docker run -dit --ipc=host --gpus=all \
    -p 7860:7860 \
    -p 8000:8000 \
    --name llamafactory \
    llamafactory:latest

docker exec -it llamafactory bash
```

昇腾 NPU 用户：

```bash
docker build -f ./docker/docker-npu/Dockerfile \
    --build-arg PIP_INDEX=https://pypi.org/simple \
    -t llamafactory:latest .

docker run -dit --ipc=host \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -p 7860:7860 \
    -p 8000:8000 \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    --name llamafactory \
    llamafactory:latest

docker exec -it llamafactory bash
```

AMD ROCm 用户：

```bash
docker build -f ./docker/docker-rocm/Dockerfile \
    --build-arg PIP_INDEX=https://pypi.org/simple \
    -t llamafactory:latest .

docker run -dit --ipc=host \
    -p 7860:7860 \
    -p 8000:8000 \
    --device /dev/kfd \
    --device /dev/dri \
    --name llamafactory \
    llamafactory:latest

docker exec -it llamafactory bash
```

</details>

<details><summary>使用 Docker 数据卷</summary>

你可以在 Dockerfile 中取消注释 `VOLUME [ "/root/.cache/huggingface", "/app/shared_data", "/app/output" ]` 以启用数据卷。

构建镜像时，请使用 `-v ./hf_cache:/root/.cache/huggingface` 参数将本地目录挂载到容器中。以下数据卷可用：

- `hf_cache`: 使用主机上的 Hugging Face 缓存。
- `shared_data`: 在主机上存储数据集的目录。
- `output`: 将导出目录设置为此位置，以便直接在主机上访问合并后的结果。

</details>

### 通过 OpenAI 风格 API 和 vLLM 部署

```bash
API_PORT=8000 llamafactory-cli api examples/inference/qwen3.yaml infer_backend=vllm vllm_enforce_eager=true
```

> [!TIP]
> API 文档请访问 [此页面](https://platform.openai.com/docs/api-reference/chat/create)。
>
> 示例：[图像理解](scripts/api_example/test_image.py) | [工具调用](scripts/api_example/test_toolcall.py)

### 从 ModelScope Hub 下载

如果你在下载 Hugging Face 模型和数据集时遇到困难，可以使用 ModelScope。

```bash
export USE_MODELSCOPE_HUB=1 # Windows 用户使用 `set USE_MODELSCOPE_HUB=1`
```

通过将 ModelScope Hub 的模型 ID 指定为 `model_name_or_path` 来训练模型。你可以在 [ModelScope Hub](https://modelscope.cn/models) 找到完整的模型 ID 列表，例如：`LLM-Research/Meta-Llama-3-8B-Instruct`。

### 从 Modelers Hub 下载

你也可以使用 Modelers Hub 下载模型和数据集。

```bash
export USE_OPENMIND_HUB=1 # Windows 用户使用 `set USE_OPENMIND_HUB=1`
```

通过将 Modelers Hub 的模型 ID 指定为 `model_name_or_path` 来训练模型。你可以在 [Modelers Hub](https://modelers.cn/models) 找到完整的模型 ID 列表，例如：`TeleAI/TeleChat-7B-pt`。

### 使用 W&B Logger

若要使用 [Weights & Biases](https://wandb.ai) 记录实验结果，你需要在 yaml 文件中添加以下参数。

```yaml
report_to: wandb
run_name: test_run # 可选
```

启动训练任务时，请设置 `WANDB_API_KEY` 为你的 [密钥](https://wandb.ai/authorize) 以登录 W&B 账号。

### 使用 SwanLab Logger

若要使用 [SwanLab](https://github.com/SwanHubX/SwanLab) 记录实验结果，你需要在 yaml 文件中添加以下参数。

```yaml
use_swanlab: true
swanlab_run_name: test_run # 可选
```

启动训练任务时，你可以通过以下方式登录 SwanLab：

1. 在 yaml 文件中添加 `swanlab_api_key=<你的密钥>`，并设置为你的 [API 密钥](https://swanlab.cn/settings)。
2. 设置环境变量 `SWANLAB_API_KEY` 为你的 [API 密钥](https://swanlab.cn/settings)。
3. 使用 `swanlab login` 命令完成登录。

## 基于 LLaMA Factory 的项目

如果你有项目希望收录于此，请通过邮件联系或创建 Pull Request。

<details><summary>点击展开</summary>

1. Wang et al. ESRL: Efficient Sampling-based Reinforcement Learning for Sequence Generation. 2023. [[arxiv]](https://arxiv.org/abs/2308.02223)
1. Yu et al. Open, Closed, or Small Language Models for Text Classification? 2023. [[arxiv]](https://arxiv.org/abs/2308.10092)
1. Wang et al. UbiPhysio: Support Daily Functioning, Fitness, and Rehabilitation with Action Understanding and Feedback in Natural Language. 2023. [[arxiv]](https://arxiv.org/abs/2308.10526)
1. Luceri et al. Leveraging Large Language Models to Detect Influence Campaigns in Social Media. 2023. [[arxiv]](https://arxiv.org/abs/2311.07816)
1. Zhang et al. Alleviating Hallucinations of Large Language Models through Induced Hallucinations. 2023. [[arxiv]](https://arxiv.org/abs/2312.15710)
1. Wang et al. Know Your Needs Better: Towards Structured Understanding of Marketer Demands with Analogical Reasoning Augmented LLMs. KDD 2024. [[arxiv]](https://arxiv.org/abs/2401.04319)
1. Wang et al. CANDLE: Iterative Conceptualization and Instantiation Distillation from Large Language Models for Commonsense Reasoning. ACL 2024. [[arxiv]](https://arxiv.org/abs/2401.07286)
1. Choi et al. FACT-GPT: Fact-Checking Augmentation via Claim Matching with LLMs. 2024. [[arxiv]](https://arxiv.org/abs/2402.05904)
1. Zhang et al. AutoMathText: Autonomous Data Selection with Language Models for Mathematical Texts. 2024. [[arxiv]](https://arxiv.org/abs/2402.07625)
1. Lyu et al. KnowTuning: Knowledge-aware Fine-tuning for Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2402.11176)
1. Yang et al. LaCo: Large Language Model Pruning via Layer Collapse. 2024. [[arxiv]](https://arxiv.org/abs/2402.11187)
1. Bhardwaj et al. Language Models are Homer Simpson! Safety Re-Alignment of Fine-tuned Language Models through Task Arithmetic. 2024. [[arxiv]](https://arxiv.org/abs/2402.11746)
1. Yang et al. Enhancing Empathetic Response Generation by Augmenting LLMs with Small-scale Empathetic Models. 2024. [[arxiv]](https://arxiv.org/abs/2402.11801)
1. Yi et al. Generation Meets Verification: Accelerating Large Language Model Inference with Smart Parallel Auto-Correct Decoding. ACL 2024 Findings. [[arxiv]](https://arxiv.org/abs/2402.11809)
1. Cao et al. Head-wise Shareable Attention for Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2402.11819)
1. Zhang et al. Enhancing Multilingual Capabilities of Large Language Models through Self-Distillation from Resource-Rich Languages. 2024. [[arxiv]](https://arxiv.org/abs/2402.12204)
1. Kim et al. Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2402.14714)
1. Yu et al. KIEval: A Knowledge-grounded Interactive Evaluation Framework for Large Language Models. ACL 2024. [[arxiv]](https://arxiv.org/abs/2402.15043)
1. Huang et al. Key-Point-Driven Data Synthesis with its Enhancement on Mathematical Reasoning. 2024. [[arxiv]](https://arxiv.org/abs/2403.02333)
1. Duan et al. Negating Negatives: Alignment without Human Positive Samples via Distributional Dispreference Optimization. 2024. [[arxiv]](https://arxiv.org/abs/2403.03419)
1. Xie and Schwertfeger. Empowering Robotics with Large Language Models: osmAG Map Comprehension with LLMs. 2024. [[arxiv]](https://arxiv.org/abs/2403.08228)
1. Wu et al. Large Language Models are Parallel Multilingual Learners. 2024. [[arxiv]](https://arxiv.org/abs/2403.09073)
1. Zhang et al. EDT: Improving Large Language Models' Generation by Entropy-based Dynamic Temperature Sampling. 2024. [[arxiv]](https://arxiv.org/abs/2403.14541)
1. Weller et al. FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions. 2024. [[arxiv]](https://arxiv.org/abs/2403.15246)
1. Hongbin Na. CBT-LLM: A Chinese Large Language Model for Cognitive Behavioral Therapy-based Mental Health Question Answering. COLING 2024. [[arxiv]](https://arxiv.org/abs/2403.16008)
1. Zan et al. CodeS: Natural Language to Code Repository via Multi-Layer Sketch. 2024. [[arxiv]](https://arxiv.org/abs/2403.16443)
1. Liu et al. Extensive Self-Contrast Enables Feedback-Free Language Model Alignment. 2024. [[arxiv]](https://arxiv.org/abs/2404.00604)
1. Luo et al. BAdam: A Memory Efficient Full Parameter Training Method for Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2404.02827)
1. Du et al. Chinese Tiny LLM: Pretraining a Chinese-Centric Large Language Model. 2024. [[arxiv]](https://arxiv.org/abs/2404.04167)
1. Ma et al. Parameter Efficient Quasi-Orthogonal Fine-Tuning via Givens Rotation. ICML 2024. [[arxiv]](https://arxiv.org/abs/2404.04316)
1. Liu et al. Dynamic Generation of Personalities with Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2404.07084)
1. Shang et al. How Far Have We Gone in Stripped Binary Code Understanding Using Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2404.09836)
1. Huang et al. LLMTune: Accelerate Database Knob Tuning with Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2404.11581)
1. Deng et al. Text-Tuple-Table: Towards Information Integration in Text-to-Table Generation via Global Tuple Extraction. 2024. [[arxiv]](https://arxiv.org/abs/2404.14215)
1. Acikgoz et al. Hippocrates: An Open-Source Framework for Advancing Large Language Models in Healthcare. 2024. [[arxiv]](https://arxiv.org/abs/2404.16621)
1. Zhang et al. Small Language Models Need Strong Verifiers to Self-Correct Reasoning. ACL 2024 Findings. [[arxiv]](https://arxiv.org/abs/2404.17140)
1. Zhou et al. FREB-TQA: A Fine-Grained Robustness Evaluation Benchmark for Table Question Answering. NAACL 2024. [[arxiv]](https://arxiv.org/abs/2404.18585)
1. Xu et al. Large Language Models for Cyber Security: A Systematic Literature Review. 2024. [[arxiv]](https://arxiv.org/abs/2405.04760)
1. Dammu et al. "They are uncultured": Unveiling Covert Harms and Social Threats in LLM Generated Conversations. 2024. [[arxiv]](https://arxiv.org/abs/2405.05378)
1. Yi et al. A safety realignment framework via subspace-oriented model fusion for large language models. 2024. [[arxiv]](https://arxiv.org/abs/2405.09055)
1. Lou et al. SPO: Multi-Dimensional Preference Sequential Alignment With Implicit Reward Modeling. 2024. [[arxiv]](https://arxiv.org/abs/2405.12739)
1. Zhang et al. Getting More from Less: Large Language Models are Good Spontaneous Multilingual Learners. 2024. [[arxiv]](https://arxiv.org/abs/2405.13816)
1. Zhang et al. TS-Align: A Teacher-Student Collaborative Framework for Scalable Iterative Finetuning of Large Language Models. 2024. [[arxiv]](https://arxiv.org/abs/2405.20215)
1. Zihong Chen. Sentence Segmentation and Sentence Punctuation Based on XunziALLM. 2024. [[paper]](https://aclanthology.org/2024.lt4hala-1.30)
1. Gao et al. The Best of Both Worlds: Toward an Honest and Helpful Large Language Model. 2024. [[arxiv]](https://arxiv.org/abs/2406.00380)
1. Wang and Song. MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with a Multi-task Evaluation Dataset. 2024. [[arxiv]](https://arxiv.org/abs/2406.02106)
1. Hu et al. Computational Limits of Low-Rank Adaptation (LoRA) for Transformer-Based Models. 2024. [[arxiv]](https://arxiv.org/abs/2406.03136)
1. Ge et al. Time Sensitive Knowledge Editing through Efficient Finetuning. ACL 2024. [[arxiv]](https://arxiv.org/abs/2406.04496)
1. Tan et al. Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions. 2024. [[arxiv]](https://arxiv.org/abs/2406.05688)
1. Song et al. Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters. 2024. [[arxiv]](https://arxiv.org/abs/2406.05955)
1. Gu et al. RWKV-CLIP: A Robust Vision-Language Representation Learner. 2024. [[arxiv]](https://arxiv.org/abs/2406.06973)
1. Chen et al. Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees. 2024. [[arxiv]](https://arxiv.org/abs/2406.07115)
1. Zhu et al. Are Large Language Models Good Statisticians?. 2024. [[arxiv]](https://arxiv.org/abs/2406.07815)
1. Li et al. Know the Unknown: An Uncertainty-Sensitive Method for LLM Instruction Tuning. 2024. [[arxiv]](https://arxiv.org/abs/2406.10099)
1. Ding et al. IntentionQA: A Benchmark for Evaluating Purchase Intention Comprehension Abilities of Language Models in E-commerce. 2024. [[arxiv]](https://arxiv.org/abs/2406.10173)
1. He et al. COMMUNITY-CROSS-INSTRUCT: Unsupervised Instruction Generation for Aligning Large Language Models to Online Communities. 2024. [[arxiv]](https://arxiv.org/abs/2406.12074)
1. Lin et al. FVEL: Interactive Formal Verification Environment with Large Language Models via Theorem Proving. 2024. [[arxiv]](https://arxiv.org/abs/2406.14408)
1. Treutlein et al. Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data. 2024. [[arxiv]](https://arxiv.org/abs/2406.14546)
1. Feng et al. SS-Bench: A Benchmark for Social Story Generation and Evaluation. 2024. [[arxiv]](https://arxiv.org/abs/2406.15695)
1. Feng et al. Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement. 2024. [[arxiv]](https://arxiv.org/abs/2406.17233)
1. Liu et al. Large Language Models for Cuffless Blood Pressure Measurement From Wearable Biosignals. 2024. [[arxiv]](https://arxiv.org/abs/2406.18069)
1. Iyer et al. Exploring Very Low-Resource Translation with LLMs: The University of Edinburgh's Submission to AmericasNLP 2024 Translation Task. AmericasNLP 2024. [[paper]](https://aclanthology.org/2024.americasnlp-1.25)
1. Li et al. Calibrating LLMs with Preference Optimization on Thought Trees for Generating Rationale in Science Question Scoring. 2024. [[arxiv]](https://arxiv.org/abs/2406.19949)
1. Yang et al. Financial Knowledge Large Language Model. 2024. [[arxiv]](https://arxiv.org/abs/2407.00365)
1. Lin et al. DogeRM: Equipping Reward Models with Domain Knowledge through Model Merging. 2024. [[arxiv]](https://arxiv.org/abs/2407.01470)
1. Bako et al. Evaluating the Semantic Profiling Abilities of LLMs for Natural Language Utterances in Data Visualization. 2024. [[arxiv]](https://arxiv.org/abs/2407.06129)
1. Huang et al. RoLoRA: Fine-tuning Rotated Outlier-free LLMs for Effective Weight-Activation Quantization. 2024. [[arxiv]](https://arxiv.org/abs/2407.08044)
1. Jiang et al. LLM-Collaboration on Automatic Science Journalism for the General Audience. 2024. [[arxiv]](https://arxiv.org/abs/2407.09756)
1. Inouye et al. Applied Auto-tuning on LoRA Hyperparameters. 2024. [[paper]](https://scholarcommons.scu.edu/cseng_senior/272/)
1. Qi et al. Research on Tibetan Tourism Viewpoints information generation system based on LLM. 2024. [[arxiv]](https://arxiv.org/abs/2407.13561)
1. Xu et al. Course-Correction: Safety Alignment Using Synthetic Preferences. 2024. [[arxiv]](https://arxiv.org/abs/2407.16637)
1. Sun et al. LAMBDA: A Large Model Based Data Agent. 2024. [[arxiv]](https://arxiv.org/abs/2407.17535)
1. Zhu et al. CollectiveSFT: Scaling Large Language Models for Chinese Medical Benchmark with Collective Instructions in Healthcare. 2024. [[arxiv]](https://arxiv.org/abs/2407.19705)
1. Yu et al. Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment. 2024. [[arxiv]](https://arxiv.org/abs/2408.00137)
1. Xie et al. The Power of Personalized Datasets: Advancing Chinese Composition Writing for Elementary School through Targeted Model Fine-Tuning. IALP 2024. [[paper]](https://www.asianlp.sg/conferences/ialp2024/proceedings/papers/IALP2024_P055.pdf)
1. Liu et al. Instruct-Code-Llama: Improving Capabilities of Language Model in Competition Level Code Generation by Online Judge Feedback. ICIC 2024. [[paper]](https://link.springer.com/chapter/10.1007/978-981-97-5669-8_11)
1. Wang et al. Cybernetic Sentinels: Unveiling the Impact of Safety Data Selection on Model Security in Supervised Fine-Tuning. ICIC 2024. [[paper]](https://link.springer.com/chapter/10.1007/978-981-97-5669-8_23)
1. Xia et al. Understanding the Performance and Estimating the Cost of LLM Fine-Tuning. 2024. [[arxiv]](https://arxiv.org/abs/2408.04693)
1. Zeng et al. Perceive, Reflect, and Plan: Designing LLM Agent for Goal-Directed City Navigation without Instructions. 2024. [[arxiv]](https://arxiv.org/abs/2408.04168)
1. Xia et al. Using Pre-trained Language Model for Accurate ESG Prediction. FinNLP 2024. [[paper]](https://aclanthology.org/2024.finnlp-2.1/)
1. Liang et al. I-SHEEP: Self-Alignment of LLM from Scratch through an Iterative Self-Enhancement Paradigm. 2024. [[arxiv]](https://arxiv.org/abs/2408.08072)
1. Bai et al. Aligning Large Language Model with Direct Multi-Preference Optimization for Recommendation. CIKM 2024. [[paper]](https://dl.acm.org/doi/10.1145/3627673.3679611)
1. Zhang et al. CPsyCoun: A Report-based Multi-turn Dialogue Reconstruction and Evaluation Framework for Chinese Psychological Counseling. ACL 2024. [[paper]](https://aclanthology.org/2024.findings-acl.830.pdf)
1. **[StarWhisper](https://github.com/Yu-Yang-Li/StarWhisper)**: 基于 ChatGLM2-6B 和 Qwen-14B 的天文学大语言模型。
1. **[DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM)**: 专注于中国法律领域的大语言模型，基于 Baichuan-13B，具备法律知识检索与推理能力。
1. **[Sunsimiao](https://github.com/X-D-Lab/Sunsimiao)**: 专注于中国医疗领域的大语言模型，基于 Baichuan-7B 和 ChatGLM-6B。
1. **[CareGPT](https://github.com/WangRongsheng/CareGPT)**: 面向中国医疗领域的系列大语言模型，基于 LLaMA2-7B 和 Baichuan-13B。
1. **[MachineMindset](https://github.com/PKU-YuanGroup/Machine-Mindset/)**: MBTI 人格系列大语言模型，能够根据不同数据集和训练方法为任意 LLM 赋予 16 种不同的人格类型。
1. **[Luminia-13B-v3](https://huggingface.co/Nekochu/Luminia-13B-v3)**: 专注于生成 Stable Diffusion 元数据的大语言模型。[[demo]](https://huggingface.co/spaces/Nekochu/Luminia-13B_SD_Prompt)
1. **[Chinese-LLaVA-Med](https://github.com/BUAADreamer/Chinese-LLaVA-Med)**: 专注于中国医疗领域的多模态大语言模型，基于 LLaVA-1.5-7B。
1. **[AutoRE](https://github.com/THUDM/AutoRE)**: 基于大语言模型的文档级关系抽取系统。
1. **[NVIDIA RTX AI Toolkit](https://github.com/NVIDIA/RTX-AI-Toolkit)**: NVIDIA RTX Windows PC 微调 LLM 的 SDK。
1. **[LazyLLM](https://github.com/LazyAGI/LazyLLM)**: 构建多智能体 LLM 应用的简易框架，支持通过 LLaMA Factory 进行模型微调。
1. **[RAG-Retrieval](https://github.com/NLPJCL/RAG-Retrieval)**: RAG 检索模型微调、推理与蒸馏的全流程方案。[[blog]](https://zhuanlan.zhihu.com/p/987727357)
1. **[360-LLaMA-Factory](https://github.com/Qihoo360/360-LLaMA-Factory)**: 修改版库，支持使用 Ring Attention 进行长序列 SFT & DPO。
1. **[Sky-T1](https://novasky-ai.github.io/posts/sky-t1/)**: NovaSky AI 以极低成本微调的类 o1 模型。
1. **[WeClone](https://github.com/xming521/WeClone)**: 一站式数字人克隆解决方案，从聊天记录生成你的数字分身。
1. **[EmoLLM](https://github.com/SmartFlowAI/EmoLLM)**: 关于大语言模型（LLMs）与心理健康的项目。

</details>

## 开源协议

本仓库采用 [Apache-2.0 License](LICENSE) 许可。

使用相应模型权重时，请遵循各模型的许可证：[BLOOM](https://huggingface.co/spaces/bigscience/license) / [DeepSeek](https://github.com/deepseek-ai/DeepSeek-LLM/blob/main/LICENSE-MODEL) / [Falcon](https://huggingface.co/tiiuae/falcon-180B/blob/main/LICENSE.txt) / [Gemma](https://ai.google.dev/gemma/terms) / [GLM-4](https://huggingface.co/THUDM/glm-4-9b/blob/main/LICENSE) / [GPT-2](https://github.com/openai/gpt-2/blob/master/LICENSE) / [Granite](LICENSE) / [InternLM](https://github.com/InternLM/InternLM#license) / [Llama](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) / [Llama 2](https://ai.meta.com/llama/license/) / [Llama 3](https://llama.meta.com/llama3/license/) / [Llama 4](https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE) / [MiniCPM](https://github.com/OpenBMB/MiniCPM/blob/main/MiniCPM%20Model%20License.md) / [Mistral/Mixtral/Pixtral](LICENSE) / [Phi-3/Phi-4](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/LICENSE) / [Qwen](https://github.com/QwenLM/Qwen/blob/main/Tongyi%20Qianwen%20LICENSE%20AGREEMENT) / [StarCoder 2](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) / [TeleChat2](https://huggingface.co/Tele-AI/telechat-7B/blob/main/TeleChat%E6%A8%A1%E5%9E%8B%E7%A4%BE%E5%8C%BA%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE.pdf) / [Yuan 2](https://github.com/IEIT-Yuan/Yuan-2.0/blob/main/LICENSE-Yuan)

## 引用

如果我们的工作对你有帮助，请 kindly 引用：

```bibtex
@inproceedings{zheng2024llamafactory,
  title={LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models},
  author={Yaowei Zheng and Richong Zhang and Junhao Zhang and Yanhan Ye and Zheyan Luo and Zhangchi Feng and Yongqiang Ma},
  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
  address={Bangkok, Thailand},
  publisher={Association for Computational Linguistics},
  year={2024},
  url={http://arxiv.org/abs/2403.13372}
}
```

## 致谢

本仓库受益于 [PEFT](https://github.com/huggingface/peft)、[TRL](https://github.com/huggingface/trl)、[QLoRA](https://github.com/artidoro/qlora) 和 [FastChat](https://github.com/lm-sys/FastChat)。感谢他们的出色工作。

## Star History

![Star History Chart](https://api.star-history.com/svg?repos=hiyouga/LLaMA-Factory&type=Date)