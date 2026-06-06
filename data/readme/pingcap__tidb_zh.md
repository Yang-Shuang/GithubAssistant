<div align="center">
<a href='https://www.pingcap.com/?utm_source=github&utm_medium=tidb'>
<img src="docs/tidb-logo.png" alt="TiDB, a distributed SQL database" height=100></img>
</a>

---

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/pingcap/tidb/blob/master/LICENSE)
[![Language](https://img.shields.io/badge/Language-Go-blue.svg)](https://golang.org/)

[![Build Status](https://prow.tidb.net/badge.svg?jobs=merged-tidb-build)](https://prow.tidb.net/?repo=pingcap%2Ftidb&type=postsubmit&job=merged-tidb-build)
[![Go Report Card](https://goreportcard.com/badge/github.com/pingcap/tidb)](https://goreportcard.com/report/github.com/pingcap/tidb)
[![GitHub release](https://img.shields.io/github/tag/pingcap/tidb.svg?label=release)](https://github.com/pingcap/tidb/releases)
</div>

# TiDB

TiDB（发音 /’taɪdiːbi:/，“Ti” 代表钛 Titanium）是一款开源、云原生分布式 SQL 数据库，专为高可用性、水平与垂直扩展能力、强一致性及高性能而设计。

- [核心特性](#key-features)
- [快速入门](#quick-start)
- [需要帮助？](#need-help)
- [架构](#architecture)
- [贡献代码](#contributing)
- [许可证](#license)
- [参见](#see-also)
- [鸣谢](#acknowledgments)

## 核心特性

- **[分布式事务](https://www.pingcap.com/blog/distributed-transactions-tidb?utm_source=github&utm_medium=tidb)**: TiDB 采用两阶段提交协议（Two-Phase Commit）以确保遵循 ACID 原则，提供强一致性保证。事务可跨多个节点执行，TiDB 的分布式特性确保了即使在网络分区或节点故障的情况下数据依然正确无误。

- **[水平与垂直扩展能力](https://docs.pingcap.com/tidb/stable/scale-tidb-using-tiup?utm_source=github&utm_medium=tidb)**: TiDB 支持通过增加节点进行横向扩展，或通过提升现有节点资源进行纵向扩展，且全程无需停机。TiDB 的计算与存储分离架构使你能根据需求独立调整两者，兼顾灵活性与业务增长。

- **[高可用性](https://docs.pingcap.com/tidbcloud/high-availability-with-multi-az?utm_source=github&utm_medium=tidb)**: 内置的 Raft 共识协议确保了系统的可靠性并实现自动故障转移。数据以多副本形式存储，事务仅在写入多数派副本后才提交，从而保证强一致性和高可用性，即使部分副本发生故障也是如此。你可以根据不同的容灾级别配置副本的地理分布。

- **[混合事务/分析处理（HTAP）](https://www.pingcap.com/blog/htap-demystified-defining-modern-data-architecture-tidb?utm_source=github&utm_medium=tidb)**: TiDB 提供两种存储引擎：基于行存储的 TiKV 和基于列存储的 TiFlash。TiFlash 通过 Multi-Raft Learner 协议从 TiKV 实时复制数据，确保行存与列存之间的数据一致性。TiDB Server 负责协调跨 TiKV 和 TiFlash 的查询执行，以优化性能。

- **[云原生](https://www.pingcap.com/cloud-native?utm_source=github&utm_medium=tidb)**: TiDB 可部署在公有云、本地数据中心或 Kubernetes 环境中。[TiDB Operator](https://docs.pingcap.com/tidb-in-kubernetes/stable/tidb-operator-overview/?utm_source=github&utm_medium=tidb) 帮助你在 Kubernetes 上管理 TiDB，自动化集群运维；而 [TiDB Cloud](https://tidbcloud.com/?utm_source=github&utm_medium=tidb) 提供全托管服务，实现轻松且经济的部署，用户只需点击几次即可完成集群搭建。

- **[MySQL 兼容性](https://docs.pingcap.com/tidb/stable/mysql-compatibility?utm_source=github&utm_medium=tidb)**: TiDB 兼容 MySQL 8.0，使你能够继续使用熟悉的协议、框架和工具。你可以在不修改代码或仅需极小改动的情况下将应用迁移至 TiDB。此外，TiDB 还提供了一套[数据迁移工具](https://docs.pingcap.com/tidb/stable/ecosystem-tool-user-guide?utm_source=github&utm_medium=tidb)，帮助你轻松地将应用数据迁入 TiDB。

- **[开源承诺](https://www.pingcap.com/blog/open-source-is-in-our-dna-reaffirming-tidb-commitment?utm_source=github&utm_medium=tidb)**: 开源是 TiDB 的核心基因。所有源代码均在 GitHub 上以 Apache 2.0 许可证开放，涵盖企业级功能。我们坚信开源能够带来透明、创新与协作。我们积极鼓励社区贡献，共同构建一个充满活力且包容的生态系统，重申我们对开放开发和人人可及的承诺。

## 快速入门

1. 启动 TiDB 集群。

    - **在本地沙盒环境**。要启动本地测试集群，请参阅 [TiDB 快速入门指南](https://docs.pingcap.com/tidb/stable/quick-start-with-tidb#deploy-a-local-test-cluster?utm_source=github&utm_medium=tidb)。

    - **在 Kubernetes 上**。你可以使用 TiDB Operator 轻松将 TiDB 部署到自建 Kubernetes 环境或公有云 Kubernetes 服务中。更多详情请参见 [Kubernetes 上的 TiDB 快速入门指南](https://docs.pingcap.com/tidb-in-kubernetes/stable/get-started?utm_source=github&utm_medium=tidb)。

    - **使用 TiDB Cloud（推荐）**。TiDB Cloud 提供全托管版 TiDB，包含免费套餐且无需绑定信用卡，让你能在几秒内获取免费集群并轻松上手：[注册 TiDB Cloud](https://tidbcloud.com/free-trial?utm_source=github&utm_medium=tidb)。

2. 了解 TiDB SQL：要探索 TiDB 的 SQL 能力，请参阅 [TiDB SQL 文档](https://docs.pingcap.com/tidb/stable/sql-statement-overview?utm_source=github&utm_medium=tidb)。

3. 使用 MySQL 驱动或 ORM 框架来 [基于 TiDB 构建应用](https://docs.pingcap.com/tidbcloud/dev-guide-overview?utm_source=github&utm_medium=tidb)。

4. 探索核心功能，例如[数据迁移](https://docs.pingcap.com/tidbcloud/tidb-cloud-migration-overview?utm_source=github&utm_medium=tidb)、[变更数据捕获（Changefeed）](https://docs.pingcap.com/tidbcloud/changefeed-overview?utm_source=github&utm_medium=tidb)、[向量搜索](https://docs.pingcap.com/tidbcloud/vector-search-overview?utm_source=github&utm_medium=tidb)、[HTAP](https://docs.pingcap.com/tidbcloud/tidb-cloud-htap-quickstart?utm_source=github&utm_medium=tidb)、[容灾备份](https://docs.pingcap.com/tidb/stable/dr-solution-introduction?utm_source=github&utm_medium=tidb) 等。


## 需要帮助？

- 你可以通过我们的社区平台与 TiDB 用户交流、提问、寻找答案或帮助他人：[Discord](https://discord.gg/KVRZBR2DrG?utm_source=github), Slack（[英文](https://slack.tidb.io/invite?team=tidb-community&channel=everyone&ref=pingcap-tidb), [日文](https://slack.tidb.io/invite?team=tidb-community&channel=tidb-japan&ref=github-tidb）, [Stack Overflow](https://stackoverflow.com/questions/tagged/tidb), [TiDB 中文论坛](https://asktug.com), X [@PingCAP](https://twitter.com/PingCAP)

- 如需提交 Bug、建议改进或请求新功能，请使用 [GitHub Issues](https://github.com/pingcap/tidb/issues) 或在 [GitHub Discussions](https://github.com/orgs/pingcap/discussions) 参与讨论。

- 排查 TiDB 问题时，请参阅[故障排除文档](https://docs.pingcap.com/tidb/stable/tidb-troubleshooting-map?utm_source=github&utm_medium=tidb)。

## 架构

![TiDB 架构](./docs/tidb-architecture.png)

在我们的 [官方文档](https://docs.pingcap.com/tidb/stable/tidb-architecture?utm_source=github&utm_medium=tidb) 中了解更多关于 TiDB 架构的详细信息。

## 贡献代码

TiDB 建立在开源承诺之上，我们欢迎所有人的贡献。无论你是想改进文档、修复 Bug 还是开发新功能，我们都邀请你共同塑造 TiDB 的未来。

- 请参阅我们的 [贡献者指南](https://github.com/pingcap/community/blob/master/contributors/README.md#how-to-contribute) 和 [TiDB 开发指南](https://pingcap.github.io/tidb-dev-guide/index.html) 开始你的旅程。

- 如果你想寻找可参与的问题，可以尝试查看 [适合新手的问题 (good first issues)](https://github.com/pingcap/tidb/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) 或 [需要帮助的问题 (help wanted issues)](https://github.com/pingcap/tidb/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)。

- [贡献地图 (contribution map)](https://github.com/pingcap/tidb-map/blob/master/maps/contribution-map.md#a-map-that-guides-what-and-how-contributors-can-contribute) 列出了所有你可以参与的贡献方向。

- [社区仓库 (community repository)](https://github.com/pingcap/community) 包含了你所需的其他所有内容。

- 别忘了填写并提交这份 [表单](https://forms.pingcap.com/f/tidb-contribution-swag)，领取你的贡献纪念品（swag）。


<a href="https://next.ossinsight.io/widgets/official/compose-recent-active-contributors?repo_id=41986369&limit=30" target="_blank" style="display: block" align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-recent-active-contributors/thumbnail.png?repo_id=41986369&limit=30&image_size=auto&color_scheme=dark" width="655" height="auto">
    <img alt="Active Contributors of pingcap/tidb - Last 28 days" src="https://next.ossinsight.io/widgets/official/compose-recent-active-contributors/thumbnail.png?repo_id=41986369&limit=30&image_size=auto&color_scheme=light" width="655" height="auto">
  </picture>
</a>

## 许可证

TiDB 采用 Apache 2.0 许可证。详情请参阅 [LICENSE](./LICENSE) 文件。

## 参见

- [TiDB 在线沙盒](https://play.tidbcloud.com/?utm_source=github&utm_medium=tidb_readme)
- TiDB 客户案例：[TiDB Customers](https://www.pingcap.com/customers/?utm_source=github&utm_medium=tidb), [TiDB 事例記事](https://pingcap.co.jp/case-study/?utm_source=github&utm_medium=tidb), [TiDB 中文用户案例](https://cn.pingcap.com/case/?utm_source=github&utm_medium=tidb)
- [TiDB 用户文档](https://docs.pingcap.com/tidb/stable?utm_source=github&utm_medium=tidb)
- [TiDB 设计文档](/docs/design)
- [TiDB 发行说明](https://docs.pingcap.com/tidb/dev/release-notes?utm_source=github&utm_medium=tidb)
- [TiDB 博客](https://www.pingcap.com/blog/?utm_source=github&utm_medium=tidb)
- [TiDB 路线图](roadmap.md)

## 鸣谢

- 感谢 [cznic](https://github.com/cznic) 提供了多款优秀的开源工具。
- 感谢 [GolevelDB](https://github.com/syndtr/goleveldb), [BoltDB](https://github.com/boltdb/bolt), 和 [RocksDB](https://github.com/facebook/rocksdb) 提供的强大存储引擎支持。