[![Nightly](https://github.com/vectordotdev/vector/actions/workflows/nightly.yml/badge.svg)](https://github.com/vectordotdev/vector/actions/workflows/nightly.yml)
[![Integration/E2E Test Suite](https://github.com/vectordotdev/vector/actions/workflows/integration.yml/badge.svg)](https://github.com/vectordotdev/vector/actions/workflows/integration.yml/badge.svg?event=merge_group)
[![Component Features](https://github.com/vectordotdev/vector/actions/workflows/component_features.yml/badge.svg)](https://github.com/vectordotdev/vector/actions/workflows/component_features.yml)

<p align="center">
  <img src="website/static/img/diagram.svg" alt="Vector">
</p>

<p align="center">
  <strong>
    <a href="https://vector.dev/docs/setup/quickstart/">快速入门</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://vector.dev/docs/">文档</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://vector.dev/guides/">指南</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://vector.dev/components/">集成</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://chat.vector.dev">社区</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://vector.dev/releases/latest/download/">下载</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://rust-doc.vector.dev/">Rust 模块文档</a>
  </strong>
</p>

## 什么是 Vector？

Vector 是一款高性能的端到端（End-to-end）可观测性数据管道，让你完全掌控自己的可观测性数据。你可以[收集][docs.sources]、[转换][docs.transforms]和[路由][docs.sinks]所有日志与指标数据，将其发送到你今天或明天想要使用的任何供应商平台。Vector 能够在你需要的地方实现显著的成本降低、创新的数据增强以及数据安全，而不是仅仅迁就供应商的便利之处。此外，它是开源的，且性能比该领域的其他替代方案快多达 10 倍。

要开始使用，请阅读我们的[**快速入门指南**][docs.quickstart]或[**安装 Vector**][docs.installation]。

Vector 由 Datadog 的[社区开源工程团队](https://opensource.datadoghq.com/about/#the-community-open-source-engineering-team)维护。

### 核心原则

* **可靠（Reliable）** - 基于 [Rust][urls.rust] 构建，Vector 的首要设计目标是可靠性。
* **端到端（End-to-end）** - 可部署为[代理（Agent）][docs.roles#agent]或[聚合器（Aggregator）][docs.roles#aggregator]。Vector 是一个完整的平台。
* **统一（Unified）** - [日志（Logs）][docs.data-model.log]、[指标（Metrics）][docs.data-model.metric]（Beta 版）和链路追踪（Traces，即将推出）。一款工具满足所有数据需求。

### 使用场景

* 降低整体可观测性成本。
* 在不中断现有工作流的情况下切换供应商。
* 提升数据质量并优化分析洞察。
* 整合代理节点，消除“代理疲劳”。
* 提高整体可观测性的性能与可靠性。

### 社区生态

* **Atlassian**、**T-Mobile**、**Comcast**、**Zendesk**、**Discord**、**Fastly**、**CVS**、**Trivago**、**Tuple**、**豆瓣**、**Visa**、**Mambu**、**Blockfi**、**Claranet**、**Instacart**、**Forcepoint** 等初创公司与企业都在使用 Vector，以及[更多用户][urls.production_users]。
* Vector **每日下载量超过 10 万次**。
* Vector 的最大用户**日处理数据量超过 500TB**。
* Vector 拥有**超过 500 名贡献者**，且仍在持续增长。

## 文档资源

所有用户文档均可在 **[vector.dev/docs](https://vector.dev/docs)** 查阅。

其他资源：

* [**Vector 日历**][urls.vector_calendar]
* **政策规范**：
  * [**行为准则**][urls.vector_code_of_conduct]
  * [**贡献指南**][urls.vector_contributing_policy]
  * [**隐私政策**][urls.vector_privacy_policy]
  * [**发布说明**][urls.vector_releases_policy]
  * [**版本策略**][urls.vector_versioning_policy]
  * [**安全政策**][urls.vector_security_policy]

## 性能对比

### 性能（Performance）

以下性能测试展示了常见协议之间的基线性能表现（正则解析测试除外）。

| 测试项目                                                                                                                   | Vector          | Filebeat | FluentBit       | FluentD   | Logstash  | SplunkUF        | SplunkHF |
| ---------------------------------------------------------------------------------------------------------------------- | --------------- | -------- | --------------- | --------- | --------- | --------------- | -------- |
| [TCP 至黑洞](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/tcp_to_blackhole_performance) | _**86mib/s**_   | n/a      | 64.4mib/s       | 27.7mib/s | 40.6mib/s | n/a             | n/a      |
| [文件至 TCP](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_to_tcp_performance)           | _**76.7mib/s**_ | 7.8mib/s | 35mib/s         | 26.1mib/s | 3.1mib/s  | 40.1mib/s       | 39mib/s  |
| [正则解析](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/regex_parsing_performance)       | 13.2mib/s       | n/a      | _**20.5mib/s**_ | 2.6mib/s  | 4.6mib/s  | n/a             | 7.8mib/s |
| [TCP 至 HTTP](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/tcp_to_http_performance)           | _**26.7mib/s**_ | n/a      | 19.6mib/s       | <1mib/s   | 2.7mib/s  | n/a             | n/a      |
| [TCP 至 TCP](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/tcp_to_tcp_performance)             | 69.9mib/s       | 5mib/s   | 67.1mib/s       | 3.9mib/s  | 10mib/s   | _**70.4mib/s**_ | 7.6mib/s |

欲了解更多性能测试详情，请参阅 [Vector 测试框架][urls.vector_test_harness]。

### 正确性（Correctness）

以下正确性测试并非详尽无遗，但它们展示了质量与细节关注度的根本差异：

| 测试项目                                                                                                                                 | Vector | Filebeat | FluentBit | FluentD | Logstash | Splunk UF | Splunk HF |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------ | -------- | --------- | ------- | -------- | --------- | --------- |
| [磁盘缓冲持久化](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/disk_buffer_persistence_correctness) | **✓**  | ✓        |           |         | ⚠        | ✓         | ✓         |
| [文件轮转（新建）](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_rotate_create_correctness)         | **✓**  | ✓        | ✓         | ✓       | ✓        | ✓         | ✓         |
| [文件轮转（截断复制）](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_rotate_truncate_correctness) | **✓**  |          |           |         |          | ✓         | ✓         |
| [文件截断](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/file_truncate_correctness)                   | **✓**  | ✓        | ✓         | ✓       | ✓        | ✓         | ✓         |
| [进程信号（SIGHUP）](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/sighup_correctness)                         | **✓**  |          |           |         | ⚠        | ✓         | ✓         |
| [JSON（外层包装）](https://github.com/vectordotdev/vector-test-harness/tree/master/cases/wrapped_json_correctness)                     | **✓**  | ✓        | ✓         | ✓       | ✓        | ✓         | ✓         |

欲了解更多正确性测试详情，请参阅 [Vector 测试框架][urls.vector_test_harness]。

### 功能特性（Features）

Vector 是一款端到端、统一且开源的数据平台。

|                     | **Vector** | Beats | Fluentbit | Fluentd | Logstash | Splunk UF | Splunk HF | Telegraf |
| ------------------- | ---------- | ----- | --------- | ------- | -------- | --------- | --------- | -------- |
| **端到端（End-to-end）**      | **✓**      |       |           |         |          |           |           | ✓        |
| 代理节点（Agent）               | **✓**      | ✓     | ✓         |         |          | ✓         |           | ✓        |
| 聚合器（Aggregator）          | **✓**      |       |           | ✓       | ✓        |           | ✓         | ✓        |
| **统一（Unified）**         | **✓**      |       |           |         |          |           |           | ✓        |
| 日志（Logs）                | **✓**      | ✓     | ✓         | ✓       | ✓        | ✓         | ✓         | ✓        |
| 指标（Metrics）             | **✓**      | ⚠     | ⚠         | ⚠       | ⚠        | ⚠         | ⚠         | ✓        |
| 链路追踪（Traces）              | 🚧         |       |           |         |          |           |           |          |
| **开源（Open）**            | **✓**      |       | ✓         | ✓       |          |           |           | ✓        |
| 开放源代码         | **✓**      | ✓     | ✓         | ✓       | ✓        |           |           | ✓        |
| 供应商中立（Vendor-neutral）      | **✓**      |       | ✓         | ✓       |          |           |           | ✓        |
| **可靠性（Reliability）**     | **✓**      |       |           |         |          |           |           |          |
| 内存安全（Memory-safe）         | **✓**      |       |           |         |          |           |           | ✓        |
| 交付保障（Delivery guarantees） | **✓**      |       |           |         |          | ✓         | ✓         |          |
| 多核支持（Multi-core）          | **✓**      | ✓     | ✓         | ✓       | ✓        | ✓         | ✓         | ✓        |

⚠ = 无法互通，指标以结构化日志形式表示

---

<p align="center">
  Developed with ❤️ by <strong><a href="https://datadoghq.com">Datadog</a></strong> - <a href="https://github.com/vectordotdev/vector/security/policy">安全政策</a> - <a href="https://github.com/vectordotdev/vector/blob/master/PRIVACY.md">隐私政策</a>
</p>

[docs.about.concepts]: https://vector.dev/docs/introduction/concepts/
[docs.about.introduction]: https://vector.dev/docs/introduction/
[docs.administration.monitoring]: https://vector.dev/docs/administration/monitoring/
[docs.administration.management]: https://vector.dev/docs/administration/management/
[docs.administration.upgrading]: https://vector.dev/docs/administration/upgrading/
[docs.administration.validating]: https://vector.dev/docs/administration/validating/
[docs.architecture.concurrency-model]: https://vector.dev/docs/architecture/concurrency-model/
[docs.architecture.data-model]: https://vector.dev/docs/architecture/data-model/
[docs.architecture.pipeline-model]: https://vector.dev/docs/architecture/pipeline-model/
[docs.architecture.runtime-model]: https://vector.dev/docs/architecture/runtime-model/
[docs.configuration.sinks]: https://vector.dev/docs/reference/configuration/sinks/
[docs.configuration.sources]: https://vector.dev/docs/reference/configuration/sources/
[docs.configuration.tests]: https://vector.dev/docs/reference/configuration/tests/
[docs.configuration.transforms]: https://vector.dev/docs/reference/configuration/transforms/
[docs.configuration.enrichment_tables]: https://vector.dev/docs/reference/configuration/global-options/#enrichment_tables
[docs.data-model.log]: https://vector.dev/docs/architecture/data-model/log/
[docs.data-model.metric]: https://vector.dev/docs/architecture/data-model/metric/
[docs.deployment.roles]: https://vector.dev/docs/setup/deployment/roles/
[docs.deployment.topologies]: https://vector.dev/docs/setup/deployment/topologies/
[docs.deployment]: https://vector.dev/docs/setup/deployment/
[docs.installation.manual]: https://vector.dev/docs/setup/installation/manual/
[docs.installation.operating_systems]: https://vector.dev/docs/setup/installation/operating-systems/
[docs.installation.package_managers]: https://vector.dev/docs/setup/installation/package-managers/
[docs.installation.platforms]: https://vector.dev/docs/setup/installation/platforms/
[docs.installation]: https://vector.dev/docs/setup/installation/
[docs.architecture.adaptive-request-concurrency]: https://vector.dev/docs/architecture/arc/
[docs.platforms.kubernetes]: https://vector.dev/docs/setup/installation/platforms/kubernetes/
[docs.quickstart]: https://vector.dev/docs/setup/quickstart/
[docs.reference.api]: https://vector.dev/docs/reference/api/
[docs.reference.cli]: https://vector.dev/docs/reference/cli/
[docs.reference.vrl]: https://vector.dev/docs/reference/vrl/
[docs.roles#agent]: https://vector.dev/docs/setup/deployment/roles/#agent
[docs.roles#aggregator]: https://vector.dev/docs/setup/deployment/roles/#aggregator
[docs.setup.installation]: https://vector.dev/docs/setup/installation/
[docs.setup.quickstart]: https://vector.dev/docs/setup/quickstart/
[docs.sinks.aws_cloudwatch_logs]: https://vector.dev/docs/reference/configuration/sinks/aws_cloudwatch_logs/
[docs.sinks.aws_s3]: https://vector.dev/docs/reference/configuration/sinks/aws_s3/
[docs.sinks.clickhouse]: https://vector.dev/docs/reference/configuration/sinks/clickhouse/
[docs.sinks.elasticsearch]: https://vector.dev/docs/reference/configuration/sinks/elasticsearch/
[docs.sinks.gcp_cloud_storage]: https://vector.dev/docs/reference/configuration/sinks/gcp_cloud_storage/
[docs.sinks]: https://vector.dev/docs/reference/configuration/sinks/
[docs.sources.docker_logs]: https://vector.dev/docs/reference/configuration/sources/docker_logs/
[docs.sources.file]: https://vector.dev/docs/reference/configuration/sources/file/
[docs.sources.http]: https://vector.dev/docs/reference/configuration/sources/http/
[docs.sources.journald]: https://vector.dev/docs/reference/configuration/sources/journald/
[docs.sources.kafka]: https://vector.dev/docs/reference/configuration/sources/kafka/
[docs.sources.socket]: https://vector.dev/docs/reference/configuration/sources/socket/
[docs.sources]: https://vector.dev/docs/reference/configuration/sources/
[docs.transforms.dedupe]: https://vector.dev/docs/reference/configuration/transforms/dedupe/
[docs.transforms.filter]: https://vector.dev/docs/reference/configuration/transforms/filter/
[docs.transforms.log_to_metric]: https://vector.dev/docs/reference/configuration/transforms/log_to_metric/
[docs.transforms.lua]: https://vector.dev/docs/reference/configuration/transforms/lua/
[docs.transforms.remap]: https://vector.dev/docs/reference/configuration/transforms/remap/
[docs.transforms]: https://vector.dev/docs/reference/configuration/transforms/
[docs.introduction.architecture]: https://vector.dev/docs/architecture/
[docs.introduction.guarantees]: https://vector.dev/docs/introduction/guarantees/
[docs.introduction.architecture]: https://vector.dev/docs/architecture/
[urls.production_users]: https://github.com/vectordotdev/vector/issues/790
[urls.rust]: https://www.rust-lang.org/
[urls.vector_calendar]: https://calendar.vector.dev
[urls.vector_chat]: https://chat.vector.dev
[urls.vector_code_of_conduct]: https://github.com/vectordotdev/vector/blob/master/CODE_OF_CONDUCT.md
[urls.vector_contributing_policy]: https://github.com/vectordotdev/vector/blob/master/CONTRIBUTING.md
[urls.vector_community]: https://vector.dev/community/
[urls.vector_privacy_policy]: https://github.com/vectordotdev/vector/blob/master/PRIVACY.md
[urls.vector_release_policy]: https://github.com/vectordotdev/vector/blob/master/RELEASING.md
[urls.vector_releases]: https://vector.dev/releases/
[urls.vector_releases_policy]: https://github.com/vectordotdev/vector/blob/master/RELEASES.md
[urls.vector_security_policy]: https://github.com/vectordotdev/vector/security/policy
[urls.vector_test_harness]: https://github.com/vectordotdev/vector-test-harness/
[urls.vector_twitter]: https://twitter.com/vectordotdev
[urls.vector_versioning_policy]: https://github.com/vectordotdev/vector/blob/master/VERSIONING.md
[urls.vote_feature]: https://github.com/vectordotdev/vector/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc+label%3A%22type%3A+feature%22