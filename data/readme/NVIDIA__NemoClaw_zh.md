<!--
  SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
  SPDX-License-Identifier: Apache-2.0
-->

# NVIDIA NemoClaw：OpenShell 中沙盒化 AI Agent 的参考栈

[![License](https://img.shields.io/badge/License-Apache_2.0-blue)](https://github.com/NVIDIA/NemoClaw/blob/main/LICENSE)
[![Security Policy](https://img.shields.io/badge/Security-Report%20a%20Vulnerability-red)](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md)
[![Discord](https://img.shields.io/badge/Discord-Join-7289da)](https://discord.gg/XFpfPv9Uvx)

NVIDIA NemoClaw 是一个开源参考栈，旨在通过 [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) 沙盒更安全地运行始终在线的 AI Agent。
它通过单个 CLI 提供引导式入门、加固 blueprint（蓝图）、路由推理、网络策略以及生命周期管理。

**支持的 Agent：**

- [OpenClaw](https://openclaw.ai)（默认）
- [Hermes](https://get-hermes.ai/)

有关功能、架构、安全控制及完整功能列表，请参阅 [NemoClaw 文档](https://docs.nvidia.com/nemoclaw/latest/)。

## 开始使用

安装前请查阅 [前置条件](https://docs.nvidia.com/nemoclaw/latest/get-started/prerequisites.html)。
若使用 Hermes，请在运行安装程序前设置 `NEMOCLAW_AGENT=hermes`，或在安装后使用 `nemohermes` 别名。

| Agent | 指南 |
|-------|------|
| OpenClaw（默认） | [使用 OpenClaw 快速入门](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html) |
| Hermes | [使用 Hermes 快速入门](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart-hermes.html) |

## 文档

有关 NemoClaw 的更多信息，请参阅官方文档网站中的以下页面。

| 页面 | 说明 |
|------|------|
| [概述](https://docs.nvidia.com/nemoclaw/latest/about/overview.html) | NemoClaw 的功能及其整体架构协同方式。 |
| [架构概览](https://docs.nvidia.com/nemoclaw/latest/about/how-it-works.html) | Plugin、blueprint（蓝图）、沙盒生命周期及防护层的高级概述。 |
| [生态系统](https://docs.nvidia.com/nemoclaw/latest/about/ecosystem.html) | OpenClaw、OpenShell 与 NemoClaw 如何构成完整技术栈，以及何时应使用 NemoClaw 而非单独使用 OpenShell。 |
| [架构详情](https://docs.nvidia.com/nemoclaw/latest/reference/architecture.html) | Plugin 结构、blueprint（蓝图）生命周期、沙盒环境及主机端状态的详细说明。 |
| [前置条件](https://docs.nvidia.com/nemoclaw/latest/get-started/prerequisites.html) | 硬件、软件、支持的平台，以及各平台特定的预配置步骤。 |
| [推理选项](https://docs.nvidia.com/nemoclaw/latest/inference/inference-options.html) | 支持的提供商、验证机制及路由推理配置。 |
| [网络策略](https://docs.nvidia.com/nemoclaw/latest/reference/network-policies.html) | 基线规则、操作员审批流程及出站流量控制。 |
| [自定义网络策略](https://docs.nvidia.com/nemoclaw/latest/network-policy/customize-network-policy.html) | 静态与动态策略变更、预设配置。 |
| [安全最佳实践](https://docs.nvidia.com/nemoclaw/latest/security/best-practices.html) | 控制措施参考、风险框架及沙盒安全态势配置文件。 |
| [沙盒加固](https://docs.nvidia.com/nemoclaw/latest/deployment/sandbox-hardening.html) | 容器安全措施、能力剥离（capabilities drops）及进程限制。 |
| [CLI 命令](https://docs.nvidia.com/nemoclaw/latest/reference/commands.html) | NemoClaw CLI 完整命令参考。 |
| [故障排除](https://docs.nvidia.com/nemoclaw/latest/reference/troubleshooting.html) | 常见问题及解决步骤。 |

## 社区

- [Discord](https://discord.gg/XFpfPv9Uvx)
- [GitHub Discussions](https://github.com/NVIDIA/NemoClaw/discussions)
- [GitHub Issues](https://github.com/NVIDIA/NemoClaw/issues)

## 参与贡献

我们欢迎社区贡献。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解开发环境配置、编码规范及 PR（Pull Request）提交流程。

## 安全

NVIDIA 高度重视安全问题。
若发现 NemoClaw 存在漏洞，**请勿提交公开 Issue。**
请使用 [SECURITY.md](SECURITY.md) 中描述的私有报告渠道之一：

- 通过 [NVIDIA 漏洞披露计划](https://www.nvidia.com/en-us/security/report-vulnerability/) 提交报告。
- 使用 [NVIDIA PGP 密钥](https://www.nvidia.com/en-us/security/pgp-key) 加密后发送邮件至 [psirt@nvidia.com](mailto:psirt@nvidia.com)。
- 使用 [GitHub 私有漏洞报告功能](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configuring-private-vulnerability-reporting-for-a-repository) 直接在此仓库中提交报告。

如需查看安全公告及 PSIRT（产品安全应急响应团队）政策，请访问 [NVIDIA 产品安全](https://www.nvidia.com/en-us/security/) 门户。

## 声明与免责声明

本软件会自动检索、访问或交互外部材料。所检索的材料不随本软件一同分发，且仅受独立条款、条件与许可证的约束。你需自行负责查找、审查并遵守所有适用的条款、条件与许可证，同时验证所检索材料的安全性、完整性及是否适用于你的具体使用场景。本软件按“原样”提供，不提供任何形式的明示或暗示担保。作者不对任何检索材料作出任何保证或声明，亦不对其因使用或无法使用本软件及任何检索材料而导致的任何损失、损害、责任或法律后果承担任何责任。使用本软件及检索材料的风险由你自行承担。

## 许可证

Apache 2.0。详见 [LICENSE](LICENSE)。