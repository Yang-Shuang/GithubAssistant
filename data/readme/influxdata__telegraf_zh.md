# ![tiger](assets/TelegrafTigerSmall.png "tiger") Telegraf

[![GoDoc](https://img.shields.io/badge/doc-reference-00ADD8.svg?logo=go)](https://godoc.org/github.com/influxdata/telegraf)
[![Docker pulls](https://img.shields.io/docker/pulls/library/telegraf.svg)](https://hub.docker.com/_/telegraf/)
[![Go Report Card](https://goreportcard.com/badge/github.com/influxdata/telegraf)](https://goreportcard.com/report/github.com/influxdata/telegraf)
[![Circle CI](https://circleci.com/gh/influxdata/telegraf.svg?style=svg)](https://circleci.com/gh/influxdata/telegraf)

Telegraf 是一款用于收集、处理、聚合和写入指标（metrics）、日志及其他任意数据的代理程序。

* 提供包含 300 多个插件的综合套件，广泛涵盖系统监控、云服务及消息传递等功能
* 支持集成用户自定义代码，以高效地收集、转换和传输数据
* 编译为独立的静态二进制文件，无任何外部依赖，确保部署流程简洁顺畅
* 采用 TOML 格式进行配置，提供直观且无歧义的配置体验
* 由超过 1,200 名贡献者组成的多元化社区共同开发

用户可以从广泛的主题中选择插件，包括但不限于：

* 设备类：[OPC UA][], [Modbus][]
* 日志类：[File][], [Tail][], [Directory Monitor][]
* 消息传递类：[AMQP][], [Kafka][], [MQTT][]
* 监控类：[OpenTelemetry][], [Prometheus][]
* 网络类：[Cisco TelemetryMDT][], [gNMI][]
* 系统监控：[CPU][], [Memory][], [Disk][], [Network][], [SMART][], [Docker][], [Nvidia SMI][] 等
* 通用类：[Exec][], [HTTP][], [HTTP Listener][], [SNMP][], [SQL][]
* Windows 专用：[Event Log][], [Management Instrumentation][], [Performance Counters][]

## 🔨 安装

如需获取 Telegraf 的二进制文件、Docker 镜像、RPM 与 DEB 安装包及其他构建版本，请参阅[安装指南](/docs/INSTALL_GUIDE.md)。

有关版本管理及发布周期的详细信息，请参见[发行说明文档](/docs/RELEASES.md)。

## 💻 使用方法

用户需定义一个包含所需插件和设置的 TOML 配置文件，然后将其传递给 Telegraf。Telegraf 代理程序将按设定的时间间隔从输入（inputs）收集数据，并按刷新间隔（flush interval）将数据发送至输出端（outputs）。

如需基础操作指南，请参见[快速入门](/docs/QUICK_START.md)。

## 📖 文档

如需查阅完整文档（包括教程、参考手册及其他资料），请从[/docs 目录](/docs/README.md)开始。

此外，每个插件均附有独立的 README 文件，其中包含配置、使用以及部分调试或故障排除的详细说明。请前往[/plugins 目录](/plugins/)查看具体插件文档。

以下是一些常用文档：

* [更新日志](/CHANGELOG.md)
* [配置说明](/docs/CONFIGURATION.md)
* [常见问题解答](/docs/FAQ.md)
* [发行版本](https://github.com/influxdata/telegraf/releases)
* [安全策略](/SECURITY.md)

## ❤️ 贡献代码

[![Contribute](https://img.shields.io/badge/contribute-to_telegraf-blue.svg?logo=influxdb)](https://github.com/influxdata/telegraf/blob/master/CONTRIBUTING.md)

我们非常感谢超过 1,200 名社区贡献者的支持！Telegraf 中包含的许多插件最初均由社区成员贡献。如果你有兴趣参与贡献，请查阅我们的[贡献指南](CONTRIBUTING.md)。此外，如果你对我们的工程团队有任何问题或建议，欢迎加入我们的[社区 Slack](https://influxdata.com/slack) 或[社区论坛](https://community.influxdata.com/)。

如果你是 Telegraf 和 InfluxDB 的新用户，还可以免费注册[InfluxDB 大学](https://www.influxdata.com/university/)的课程以了解更多内容。

## ℹ️ 技术支持

[![Slack](https://img.shields.io/badge/slack-join_chat-blue.svg?logo=slack)](https://www.influxdata.com/slack)
[![Forums](https://img.shields.io/badge/discourse-join_forums-blue.svg?logo=discourse)](https://community.influxdata.com/)

如果你对我们的工程团队有任何问题或建议，请使用[社区 Slack](https://influxdata.com/slack) 或[社区论坛](https://community.influxdata.com/)。GitHub Issue 仅用于报告实际错误或提交功能请求。

## 📜 许可证

[![MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/influxdata/telegraf/blob/master/LICENSE)

[OPC UA]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/opcua
[Modbus]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/modbus
[File]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/file
[Tail]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/tail
[Directory Monitor]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/directory_monitor
[AMQP]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/amqp_consumer
[Kafka]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/kafka_consumer
[MQTT]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/mqtt_consumer
[OpenTelemetry]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/opentelemetry
[Prometheus]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/prometheus
[Cisco TelemetryMDT]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/cisco_telemetry_mdt
[gNMI]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/gnmi
[CPU]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/cpu
[Memory]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/mem
[Disk]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/disk
[Network]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/net
[SMART]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/smartctl
[Docker]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/docker
[Nvidia SMI]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/nvidia_smi
[Exec]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/exec
[HTTP]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/http
[HTTP Listener]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/http_listener_v2
[SNMP]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/snmp
[SQL]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/sql
[Event Log]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/win_eventlog
[Management Instrumentation]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/win_wmi
[Performance Counters]: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/win_perf_counters