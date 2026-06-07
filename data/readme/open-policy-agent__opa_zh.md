# ![logo](./logo/logo-144x144.png) Open Policy Agent

[![Build Status](https://github.com/open-policy-agent/opa/workflows/Post%20Merge/badge.svg)](https://github.com/open-policy-agent/opa/actions) [![Go Report Card](https://goreportcard.com/badge/github.com/open-policy-agent/opa)](https://goreportcard.com/report/github.com/open-policy-agent/opa) [![CII Best Practices](https://www.bestpractices.dev/projects/1768/badge)](https://www.bestpractices.dev/en/projects/1768/passing) [![Netlify Status](https://api.netlify.com/api/v1/badges/4a0a092a-8741-4826-a28f-826d4a576cab/deploy-status)](https://app.netlify.com/sites/openpolicyagent/deploys)

Open Policy Agent（OPA）是一个开源的、通用的策略引擎，能够在整个技术栈中实现统一的、上下文感知的策略执行。

OPA 很荣幸成为 [Cloud Native Computing Foundation](https://www.cncf.io/)（CNCF）的毕业项目。详情请参阅 CNCF 发布的[公告](https://www.cncf.io/announcements/2021/02/04/cloud-native-computing-foundation-announces-open-policy-agent-graduation/)。

## 开始使用 OPA

- 使用 [Rego Playground](https://play.openpolicyagent.org) 编写你的第一条 Rego 策略，或用它与他人分享作品以获取反馈和支持。如果不确定从哪里开始，可以查看[访问控制示例](https://play.openpolicyagent.org/?example-group=access-control)。
- 安装 [VS Code extension](https://marketplace.visualstudio.com/items?itemName=tsandall.opa) 以在本地快速上手，支持实时诊断、调试和格式化。请参阅[编辑器与 IDE 支持](https://www.openpolicyagent.org/docs/editor-and-ide-support)了解其他支持的编辑器。
- 访问 [OPA Documentation](https://www.openpolicyagent.org/docs)，学习 Rego 语言以及如何部署和集成 OPA。
- 查看生态目录中 [Learning Rego](https://www.openpolicyagent.org/ecosystem/by-feature/learning-rego) 部分的学习资源。
- 按照[运行 OPA](https://www.openpolicyagent.org/docs/latest/#running-opa) 指南在本地开始使用 OPA CLI。
- 查看 [Docker Hub](https://hub.docker.com/r/openpolicyagent/opa/tags/) 获取容器镜像，或访问 [GitHub releases](https://github.com/open-policy-agent/opa/releases) 下载二进制文件。
- 浏览 [OPA Roadmap](https://github.com/orgs/open-policy-agent/projects/10)，了解 OPA 正在进行和计划中的功能概览。

## 交流或获取支持？

- 加入 [OPA Slack](https://slack.openpolicyagent.org) 与其他用户和维护者交流。请参阅 `#help` 频道获取技术支持。
- 查看[社区讨论区](https://github.com/orgs/open-policy-agent/discussions)提问。
- 访问[支持](https://www.openpolicyagent.org/support)页面了解商业支持选项。

## 想了解其他人如何使用 OPA？

- 浏览 [OPA Ecosystem Directory](https://www.openpolicyagent.org/ecosystem) 中的社区项目——别忘了[列出你自己的项目](https://github.com/open-policy-agent/opa/tree/main/docs#opa-ecosystem)！
- 查看 [ADOPTERS.md](./ADOPTERS.md) 文件获取生产环境采用者列表。你的组织是否在生产环境中使用了 OPA？请提交 PR 将你的组织添加到列表中，并附上简短的 OPA 使用案例描述，以支持 OPA 项目！

## 如何集成 OPA？

- 查看高级 [Go SDK](https://www.openpolicyagent.org/docs/integration#integrating-with-the-go-sdk) 或低级 Go API
  [![GoDoc](https://pkg.go.dev/badge/github.com/open-policy-agent/opa?utm_source=godoc)](https://pkg.go.dev/github.com/open-policy-agent/opa/rego?utm_source=godoc)
  将 OPA 与用 Go 编写服务集成。
- 查阅 [REST API](https://www.openpolicyagent.org/docs/rest-api.html)
  参考文档，将 OPA 与其他语言编写的服务集成。
- 查看[集成文档](https://www.openpolicyagent.org/docs/integration)了解更多选项。

## 如何为 OPA 做贡献？

- 阅读 [Contributing Guide](https://www.openpolicyagent.org/docs/contributing)，了解如何做出你的第一次贡献。
- 在 Slack 中使用 [#contributors](https://openpolicyagent.slack.com/?redir=%2Farchives%2FC02L1TLPN59%3Fname%3DC02L1TLPN59) 频道与其他贡献者和维护者交流。
- 提交 [GitHub Issue](https://github.com/open-policy-agent/opa/issues) 以请求新功能或报告 Bug。

## OPA 是如何工作的？

OPA 为你提供了一门高级声明式语言，用于在整个技术栈中编写和执行策略。

使用 OPA，你可以定义_规则_来规范系统的行为方式。这些规则旨在回答以下问题：
- 用户 X 是否可以对资源 Z 执行操作 Y？
- 工作负载 W 应该部署到哪些集群？
- 在创建资源 R 之前必须设置哪些标签？

你将服务与 OPA 集成，这样就不必_硬编码_这些策略决策。当需要做出策略决策时，服务通过执行_查询_来与 OPA 交互。

当你向 OPA 查询策略决策时，OPA 会评估你提供的规则和_数据_以生成答案。该策略决策将作为查询结果返回。

例如，在一个简单的 API 授权用例中：
- 你编写允许（或拒绝）访问服务 API 的规则。
- 你的服务在收到 API 请求时向 OPA 发起查询。
- OPA 将允许（或拒绝）的决策返回给你的服务。
- 你的服务_执行_这些决策，相应地接受或拒绝请求。

有关如何将 OPA 与 [Kubernetes](https://www.openpolicyagent.org/docs/kubernetes)、[Terraform](https://www.openpolicyagent.org/docs/terraform)、[Docker](https://www.openpolicyagent.org/docs/docker-authorization)、[SSH](https://www.openpolicyagent.org/docs/ssh-and-sudo-authorization) 等系统集成的具体示例，请参阅 [openpolicyagent.org](https://www.openpolicyagent.org)。

## 演示文稿与演讲视频

- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon EU 2026：[video](https://www.youtube.com/watch?v=TENlj4r6IXk)
- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon NA 2025：[video](https://www.youtube.com/watch?v=tDBYMF2XXLA)
- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon EU 2025：[video](https://www.youtube.com/watch?v=XtA-NKoJDaI)
- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon NA 2024：[video](https://www.youtube.com/watch?v=QuotLxFb2f4)
- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon EU 2024：[video](https://www.youtube.com/watch?v=hENwFyrtm1g)
- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon NA 2023：[video](https://www.youtube.com/watch?v=wJkjsvVpj_Q)
- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon EU 2023：[video](https://www.youtube.com/watch?v=6RNp3m_THw4)
- 使用 WASM & OPA 在难以触及的地方执行策略 @ CN Wasm Day EU 2023：[video](https://www.youtube.com/watch?v=BdeBhukLwt4)
- OPA 维护者演讲 @ Kubecon NA 2022：[video](https://www.youtube.com/watch?v=RMiovzGGCfI)
- Open Policy Agent (OPA) 简介与深度解析 @ Kubecon EU 2022：[video](https://www.youtube.com/watch?v=MhyQxIp1H58)
- Open Policy Agent 简介 @ KubeCon EU 2021：[Video](https://www.youtube.com/watch?v=2CgeiWkliaw)
- 使用 Open Policy Agent 满足不断变化的策略要求 @ KubeCon NA 2020：[video](https://www.youtube.com/watch?v=zVuM7F_BTyc)
- 在应用生命周期中通过 Open Policy Agent 实施策略 @ CloudNativeCon 2019：[video](https://www.youtube.com/watch?v=cXfsaE6RKfc)
- Open Policy Agent 简介 @ CloudNativeCon EU 2018：[video](https://youtu.be/XEHeexPpgrA), [slides](https://www.slideshare.net/slideshow/opa-the-cloud-native-policy-engine/96644504)
- Rego 深度解析 @ CloudNativeCon EU 2018：[video](https://youtu.be/4mBJSIhs2xQ), [slides](https://www.slideshare.net/slideshow/rego-deep-dive/96644608)
- Netflix 如何在云环境中解决授权问题 @ CloudNativeCon US 2017：[video](https://www.youtube.com/watch?v=R6tUNpRpdnY), [slides](https://www.slideshare.net/slideshow/how-netflix-is-solving-authorization-across-their-cloud/84384095)。
- Kubernetes Federation 中的基于策略的资源放置 @ LinuxCon Beijing 2017：[slides](https://www.slideshare.net/slideshow/policybased-resource-placement-across-hybrid-cloud/83876901), [screencast](https://www.youtube.com/watch?v=hRz13baBhfg&feature=youtu.be)
- 在 Kubernetes 中执行定制策略 @ KubeCon US 2017：[video](https://www.youtube.com/watch?v=llDI8VvkUj8), [slides](https://www.slideshare.net/slideshow/enforcing-bespoke-policies-in-kubernetes/83877237)
- Istio Mixer：使用自定义适配器执行策略 @ CloudNativeCon US 2017：[video](https://www.youtube.com/watch?v=czZLXUqzd24), [slides](https://www.slideshare.net/slideshow/istios-mixer-policy-enforcement-with-custom-adapters-cloud-nativecon-17/83877455)

## 安全性

该项目已由 Cure53 完成第三方安全审计，完整报告请参见[此处](SECURITY_AUDIT.pdf)。

请通过电子邮件向 [open-policy-agent-security](mailto:open-policy-agent-security@googlegroups.com) 报告漏洞。我们将发送确认邮件以告知已收到报告，并在问题调查完成后发送后续消息进行跟进。