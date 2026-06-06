[![][kong-logo]][kong-url]

![Stars](https://img.shields.io/github/stars/Kong/kong?style=flat-square) ![GitHub commit activity](https://img.shields.io/docker/pulls/_/kong?style=flat-square) [![Build Status][badge-action-image]][badge-action-url] ![Version](https://img.shields.io/github/v/release/Kong/kong?color=green&label=Version&style=flat-square)  ![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square) [![Twitter Follow](https://img.shields.io/twitter/follow/thekonginc?style=social)](https://x.com/thekonginc)


Kong（或 Kong Gateway）是一款云原生、跨平台、可扩展的 **API 𖧹 LLM 𖧹 MCP** 网关，以其高性能和通过插件实现的强大扩展性而闻名。它还提供了先进的 AI 流量管理能力，支持多 LLM、语义安全、MCP 流量安全与分析等功能。

通过提供代理、路由、负载均衡、健康检查、认证（以及[更多功能](#features)），Kong 成为编排微服务或传统 API 流量——以及智能体（Agent）LLM 和 MCP 流量——的中央层，操作简便。

得益于官方 [Kubernetes Ingress Controller](https://github.com/Kong/kubernetes-ingress-controller)，Kong 可原生运行在 Kubernetes 上。

<br />

[![][kong-diagram]][kong-url]

---

[安装](https://konghq.com/install/#kong-community) | [文档](https://docs.konghq.com) | [讨论区](https://github.com/Kong/kong/discussions) | [论坛](https://discuss.konghq.com) | [博客](https://konghq.com/blog) | [构建版本][kong-master-builds] | [AI Gateway](https://konghq.com/products/kong-ai-gateway) | [云托管 Kong](https://konghq.com/kong-konnect/)

---

## 快速入门

如果你更倾向于使用云托管的 Kong，可以[注册免费试用 Kong Konnect](https://konghq.com/products/kong-konnect/register?utm_medium=Referral&utm_source=Github&utm_campaign=kong-gateway&utm_content=konnect-promo-in-gateway&utm_term=get-started)，几分钟内即可上手。否则，请按照以下说明在你自己的基础设施上开始使用 Kong。

让我们通过不到 5 分钟为 API 添加认证来体验一下 Kong。

我们建议通过以下步骤使用 docker-compose 发行版，但如果你更希望以无数据库模式（DB-less Mode）运行 Kong Gateway，也有相应的 [Docker 安装](https://docs.konghq.com/gateway/latest/install/docker/#install-kong-gateway-in-db-less-mode)流程。

无论你在云端、裸金属服务器还是容器环境中运行，都可以在我们的[官方安装页面](https://konghq.com/install/#kong-community)找到所有支持的发行版。

1) 首先，克隆 Docker 仓库并进入 compose 文件夹。
```cmd
  $ git clone https://github.com/Kong/docker-kong
  $ cd docker-kong/compose/
```

2) 使用以下命令启动网关堆栈：
```cmd
  $ KONG_DATABASE=postgres docker-compose --profile database up
```

网关现在可在本地主机的以下端口访问：

- `:8000` - 通过 Kong 向你的服务发送流量
- `:8001` - 使用 Admin API 或 [decK](https://github.com/kong/deck) 配置 Kong
- `:8002` - 访问 Kong 管理 Web UI（[Kong Manager](https://github.com/Kong/kong-manager）），地址为 [localhost:8002](http://localhost:8002)

接下来，请按照[快速入门指南](https://docs.konghq.com/gateway-oss/latest/getting-started/configuring-a-service/)浏览网关功能。

### 开始使用 AI Gateway（LLM 与 MCP）

如果你想开始使用包含 LLM 和 MCP 功能的 Kong AI Gateway，请参阅[官方 AI 文档](https://developer.konghq.com/ai-gateway/)。

## 核心功能

通过将组织中所有服务的常见 API、AI 和 MCP 功能集中管理，Kong Gateway 让工程团队能够更自由地专注于最重要的挑战。

Kong 的主要功能包括：

- 高级路由、负载均衡、健康检查——均可通过 RESTful Admin API 或声明式配置进行自定义。
- 使用 JWT、Basic Auth、OAuth、ACLs 等方法为 API 提供认证和授权。
- 通用 LLM API，支持跨 OpenAI、Anthropic、GCP Gemini、AWS Bedrock、Azure AI、Databricks、Mistral、Huggingface 等多个提供商进行路由。
- MCP 流量治理、安全与可观测性，此外还支持从任何 RESTful API 自动生成 MCP。
- 60 多项 AI 功能，包括 AI 可观测性、语义安全与缓存、语义路由等。
- 代理、SSL/TLS 终止，以及 L4/L7 流量的连接支持。
- 插件用于强制执行流量控制、速率限制、请求/响应转换、日志记录、监控，并提供插件开发者中心。
- 复杂的部署模型，如声明式无数据库部署和混合部署（控制平面/数据平面分离），且无任何厂商锁定。
- 原生 [Ingress Controller](https://github.com/Kong/kubernetes-ingress-controller) 支持，用于服务 Kubernetes。

[![][kong-benefits]][kong-url]

### 插件中心

插件提供了扩展网关使用的高级功能。Kong Inc. 和社区开发的许多插件（如 AWS Lambda、Correlation ID 和 Response Transformer）均在[插件中心](https://docs.konghq.com/hub/)展示。

为插件中心做出贡献，确保你的下一个创新想法得以发布并惠及更广泛的社区！

## 贡献代码

我们 ❤️ Pull Request，并且一直在努力让开发者贡献代码尽可能简单。在使用 Kong Gateway 开始开发之前，请先熟悉以下开发者资源：

- 社区承诺（[COMMUNITY_PLEDGE.md](COMMUNITY_PLEDGE.md)）：关于我们如何与开源社区互动的承诺。
- 贡献者指南（[CONTRIBUTING.md](CONTRIBUTING.md)）：了解如何为 Kong 做出贡献。
- 开发指南（[DEVELOPER.md](DEVELOPER.md)）：设置你的开发环境。
- [行为准则](CODE_OF_CONDUCT.md) 和 [版权说明](COPYRIGHT)

使用[插件开发指南](https://docs.konghq.com/latest/plugin-development/)构建新颖的插件，或在[插件开发工具包 (PDK) 参考文档](https://docs.konghq.com/latest/pdk/)中浏览 Kong 源代码文档的在线版本。开发者可以使用 [Lua](https://docs.konghq.com/gateway/latest/plugin-development/)、[Go](https://docs.konghq.com/gateway-oss/latest/external-plugins/#developing-go-plugins) 或 [JavaScript](https://docs.konghq.com/gateway-oss/latest/external-plugins/#developing-javascript-plugins) 构建插件。

## 版本发布

有关特定版本的详细信息，请参阅[更新日志](CHANGELOG.md)。版本控制遵循 [SemVer 规范](https://semver.org)。

## 加入社区

- 查阅[文档](https://docs.konghq.com/)
- 加入[Kong 讨论区](https://github.com/Kong/kong/discussions)
- 在 Kong Nation 论坛参与 Kong 讨论：[https://discuss.konghq.com/](https://discuss.konghq.com/)
- 加入我们的 [社区 Slack](http://kongcommunity.slack.com/)
- 在我们的[博客](https://konghq.com/blog/)上了解最新动态
- 在 [X (原 Twitter)](https://x.com/thekonginc) 关注我们
- 订阅我们的 [YouTube 频道](https://www.youtube.com/c/KongInc/videos)
- 访问我们的[官网](https://konghq.com/)了解更多

## Konnect Cloud

Kong Inc. 提供多种增强版商业订阅服务。使用 Kong [Konnect Cloud](https://konghq.com/kong-konnect/) 订阅的客户可享受额外的网关功能、商业支持以及 Kong 托管（SaaS）控制平面平台的访问权限。Konnect Cloud 平台功能包括实时分析、服务目录、开发者门户等更多内容！[立即开始](https://konghq.com/products/kong-konnect/register?utm_medium=Referral&utm_source=Github&utm_campaign=kong-gateway&utm_content=konnect-promo-in-gateway&utm_term=get-started)使用 Konnect Cloud。

## 许可证

```
Copyright 2016-2026 Kong Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[kong-url]: https://konghq.com/
[kong-logo]: https://konghq.com/wp-content/uploads/2018/05/kong-logo-github-readme.png
[kong-diagram]: https://assets.prd.mktg.konghq.com/images/2025/09/68cc1bfd-kong-diagram.png?v=2
[kong-benefits]: https://konghq.com/wp-content/uploads/2018/05/kong-benefits-github-readme.png
[kong-master-builds]: https://hub.docker.com/r/kong/kong/tags
[badge-action-url]: https://github.com/Kong/kong/actions
[badge-action-image]: https://github.com/Kong/kong/actions/workflows/build_and_test.yml/badge.svg?branch=master&event=push

[busted]: https://github.com/Olivine-Labs/busted
[luacheck]: https://github.com/mpeterv/luacheck