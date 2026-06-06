<p align="center">
  <a href="https://grafana.com/oss/k6/">
    <picture>
      <img src="assets/logo.svg" alt="Grafana k6" width="210" height="210" /><br>
    </picture>
    <br>
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/grafana-labs-dark-theme.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/grafana-labs.svg">
      <img src="assets/grafana-labs.svg" alt="Grafana Labs" width="210" />
    </picture>
    <br>
  </a>
</p>

<h3 align="center">像做单元测试一样进行性能测试</h3>
<p align="center">面向 DevOps 时代开发者与测试人员的现代化负载测试（load testing）工具。</p>

<p align="center">
  <a href="https://github.com/grafana/k6/releases"><img src="https://img.shields.io/github/release/grafana/k6.svg" alt="Github release"></a>
  <a href="https://github.com/grafana/k6/actions/workflows/all.yml"><img src="https://github.com/grafana/k6/actions/workflows/build.yml/badge.svg" alt="Build status"></a>
  <a href="https://goreportcard.com/report/github.com/grafana/k6"><img src="https://goreportcard.com/badge/github.com/grafana/k6" alt="Go Report Card"></a>
 <a href="https://codecov.io/gh/grafana/k6"><img src="https://img.shields.io/codecov/c/github/grafana/k6/master.svg" alt="Codecov branch"></a>
  <br>
  <a href="https://twitter.com/k6_io"><img src="https://img.shields.io/badge/twitter-@k6_io-55acee.svg" alt="@k6_io on Twitter"></a>
</p>
<p align="center">
    <a href="https://github.com/grafana/k6/releases">下载</a> ·
    <a href="https://grafana.com/docs/k6/latest/">文档</a> ·
    <a href="https://community.grafana.com/c/grafana-k6/70">社区论坛</a> ·
    <a href="https://github.com/orgs/grafana/projects/443/views/1">公共路线图</a>
</p>

<br/>
<img src="assets/github-hr.png" alt="---" />
<br/>

**k6** 是一款现代化的负载测试工具，基于我们在性能与测试行业多年的经验打造。它旨在提供强大的功能、良好的扩展性以及完整的功能集。其核心设计目标是提供**极致的开发者体验**。

它的核心特性包括：

- **可配置的负载生成。** 即使是配置较低的机器也能模拟大量流量。
- **测试即代码（Tests as Code）。** 复用脚本、模块化逻辑、版本控制，并将测试集成到你的 CI/CD 流程中。
- **功能完善的 API。** 脚本 API 内置丰富特性，助你轻松模拟真实的应用流量。
- **内嵌 JavaScript 引擎。** 兼具 Go 语言的性能与 JavaScript 的编程熟悉感。
- **多协议支持**。涵盖 HTTP、WebSockets、gRPC、浏览器（Browser）等更多协议。
- **庞大的扩展生态。** 你可以根据需求自行扩展 k6。已有许多开发者将他们的扩展分享给了社区！[探索](https://grafana.com/docs/k6/latest/extensions/explore)可用的扩展插件。
- **灵活的指标存储与可视化**。支持汇总统计或细粒度指标，并可导出到你选择的任意服务中。
- **与 Grafana Cloud 原生集成**。[SaaS 解决方案](https://grafana.com/products/cloud/k6/)，涵盖测试执行、指标关联分析、数据洞察等更多功能。

这就是 21 世纪负载测试应有的模样。

## 示例脚本


```js
import http from "k6/http";
import { check, sleep } from "k6";

// Test configuration
export const options = {
  thresholds: {
    // Assert that 99% of requests finish within 3000ms.
    http_req_duration: ["p(99) < 3000"],
  },
  // Ramp the number of virtual users up and down
  stages: [
    { duration: "30s", target: 15 },
    { duration: "1m", target: 15 },
    { duration: "20s", target: 0 },
  ],
};

// Simulated user behavior
export default function () {
  let res = http.get("https://quickpizza.grafana.com");
  // Validate response status
  check(res, { "status was 200": (r) => r.status == 200 });
  sleep(1);
}
```

你可以通过命令行（CLI）运行此类脚本，或在 CI 环境中执行，甚至跨 Kubernetes 集群进行分布式测试。

> [!NOTE]
> 不想写代码？
> 
> 没问题！试试 [k6 Studio](https://github.com/grafana/k6-studio)，这是一款桌面应用程序，可帮你直接生成 k6 脚本，无需触碰任何代码！

## 文档指南

官方文档涵盖了使用 k6 的所有方面。部分重点内容包括：

- [快速入门](https://grafana.com/docs/k6/latest/)。安装、运行测试并查看结果。
- [HTTP 请求](https://grafana.com/docs/k6/latest/using-k6/http-requests/)。让你的虚拟用户执行各类 HTTP 方法。此外，还可查看其他[协议支持](https://grafana.com/docs/k6/latest/using-k6/protocols/)。
- [阈值（Thresholds）](https://grafana.com/docs/k6/latest/using-k6/thresholds/)。为测试设定目标，并将你的服务等级协议（SLO）代码化。
- [配置选项（Options）](https://grafana.com/docs/k6/latest/using-k6/k6-options/)。自定义负载参数、持续时间、TLS 证书等，以及更多设置。
- [场景（Scenarios）](https://grafana.com/docs/k6/latest/using-k6/scenarios/)。选择你的负载建模方式：开放模型、封闭模型、恒定 RPS、固定迭代次数等。
- [结果输出（Results Output）](https://grafana.com/docs/k6/latest/results-output/)。分析、过滤并导出你的测试结果。
- [JavaScript API](https://grafana.com/docs/k6/latest/javascript-api/)。所有 k6 模块的参考文档与使用示例。
- [扩展插件（Extensions）](https://grafana.com/docs/k6/latest/extensions/)。通过扩展支持新协议与新用例。

这些链接仅触及皮毛！如果你需要更底层的概念解析，可以阅读关于[测试类型](https://grafana.com/docs/k6/latest/testing-guides/test-types/)、[测试策略](https://grafana.com/docs/k6/latest/testing-guides/)的文章，或浏览丰富的官方博客文章。

## 产品路线图

我们的团队致力于持续改进，力求提供最佳的用户体验（UX）。[公共路线图](https://github.com/orgs/grafana/projects/443/views/1)涵盖了以用户为导向的功能、UX 优化以及 JavaScript 支持等我们重点关注的方向。请注意，时间表和优先级可能会调整，但我们认为分享产品愿景至关重要。

我们希望它能清晰展示我们未来的开发计划。欢迎通过 GitHub 提供反馈、修正与建议，使其对社区更加全面、易读且富有价值。

值得一提的是，我们将[点赞（大拇指向上）](https://github.com/grafana/k6/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc)视为衡量社区需求的重要指标之一。如果你认为某项功能很重要，请为它点一个赞。

## 贡献代码

如果你想为 k6 贡献代码或协助开发，请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。在开始编码之前，建议先与 k6 维护者讨论你的计划与实现细节——尤其是涉及重大变更和新功能时。你可以在解决该问题的 [GitHub Issue](https://github.com/grafana/k6/issues) 中进行沟通（如果尚未创建，请新建一个）。

> **注意：** 如需披露安全漏洞，请参阅 [SECURITY.md](https://github.com/grafana/k6?tab=security-ov-file)。

## 获取支持

如需寻求帮助、报告 Bug、建议新功能或与他人讨论 k6，请参阅 [SUPPORT.md](SUPPORT.md)。

## 开源协议

k6 基于 [AGPL-3.0 许可证](https://github.com/grafana/k6/blob/master/LICENSE.md) 发布。