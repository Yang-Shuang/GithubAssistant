# FauxPilot

这是一个尝试构建本地托管的 GitHub Copilot 替代方案的项目。它使用 NVIDIA 的 Triton Inference Server，并搭载 FasterTransformer 后端来运行 Salesforce CodeGen 模型。

<p align="right">
  <img width="50%" align="right" src="./img/fauxpilot.png">
</p>

## Prerequisites

你需要准备：

* Docker
* `docker compose` >= 1.28
* 一块计算架构（Compute Capability）>= 6.0 且显存（VRAM）足以运行目标模型的 NVIDIA GPU。
* [`nvidia-docker`](https://github.com/NVIDIA/nvidia-docker)
* `curl` 和 `zstd`，用于下载和解压模型文件。

注意：`setup.sh` 中列出的显存需求是*总和*——如果你拥有多块显卡，可以将模型拆分到这些 GPU 上运行。例如，如果你有双 NVIDIA RTX 3080 显卡，你应该能够将 6B 模型各分一半放在每张卡上成功运行。

## Support and Warranty

开个玩笑（lmao）

好吧，说正经的。我们现在在 [Wiki 页面](https://github.com/moyix/fauxpilot/wiki) 和 [讨论区](https://github.com/moyix/fauxpilot/discussions) 提供了一些基础信息，你可以在那里提问。不过目前仍然没有官方正式支持或保修服务！

## Setup

本节介绍如何安装 FauxPilot 服务端和客户端。

### Setting up a FauxPilot Server

运行安装脚本以选择要使用的模型。该脚本会从 [Huggingface/Moyix](https://huggingface.co/Moyix) 下载 GPT-J 格式的模型，并将其转换为适用于 FasterTransformer 的格式。

详情请参阅 [如何搭建 FauxPilot 服务端](documentation/server.md)。

### Client configuration for FauxPilot

我们提供了几种连接 FauxPilot 服务端的方式。例如，你可以通过 OpenAI API、Copilot 插件或 REST API 来配置客户端。

详情请参阅 [如何配置客户端](documentation/client.md)。

## Terminology
 * API：应用程序编程接口（Application Programming Interface）
 * CC：计算架构能力（Compute Capability）
 * CUDA：统一计算设备架构（Compute Unified Device Architecture）
 * FT：FasterTransformer 框架
 * JSON：JavaScript 对象简谱（JavaScript Object Notation） 
 * gRPC：Google 开发的远程过程调用协议（Remote Procedure Call）
 * GPT-J：基于 Ben Wang 的 Mesh Transformer JAX 训练的 Transformer 模型 
 * REST：表述性状态转移（REpresentational State Transfer）