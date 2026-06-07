<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

## 🌍 其他语言版本

[English](README.md) • [العربية](docs/ar-SA/README.md) • [বাংলা](docs/bn-BD/README.md) • [Deutsch](docs/de-DE/README.md) • [Español](docs/es-ES/README.md) • [فارسی](docs/fa-IR/README.md) • [Français](docs/fr-FR/README.md) • [हिन्दी](docs/hi-IN/README.md) • [Bahasa Indonesia](docs/id-ID/README.md) • [Italiano](docs/it-IT/README.md) • [日本語](docs/ja-JP/README.md) • [한국어](docs/ko-KR/README.md) • [Polski](docs/pl-PL/README.md) • [Português](docs/pt-BR/README.md) • [Română](docs/ro-RO/README.md) • [Русский](docs/ru-RU/README.md) • [Slovenščina](docs/sl-SI/README.md) • [ไทย](docs/th-TH/README.md) • [Türkçe](docs/tr-TR/README.md) • [Українська](docs/uk-UA/README.md) • [Tiếng Việt](docs/vi-VN/README.md) • [简体中文](docs/zh-CN/README.md) • [繁體中文](docs/zh-TW/README.md)

<div align="center">

# Apache Doris

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![GitHub release](https://img.shields.io/github/release/apache/doris.svg)](https://github.com/apache/doris/releases)
[![OSSRank](https://shields.io/endpoint?url=https://ossrank.com/shield/516)](https://ossrank.com/p/516)
[![Commit activity](https://img.shields.io/github/commit-activity/m/apache/doris)](https://github.com/apache/doris/commits/master/)
[![EN doc](https://img.shields.io/badge/Docs-English-blue.svg)](https://doris.apache.org/docs/gettingStarted/what-is-apache-doris)
[![CN doc](https://img.shields.io/badge/文档-中文版-blue.svg)](https://doris.apache.org/zh-CN/docs/gettingStarted/what-is-apache-doris)

<div>

[![Official Website](<https://img.shields.io/badge/-Visit%20the%20Official%20Website%20%E2%86%92-rgb(15,214,106)?style=for-the-badge>)](https://doris.apache.org/)
[![Quick Download](<https://img.shields.io/badge/-Quick%20%20Download%20%E2%86%92-rgb(66,56,255)?style=for-the-badge>)](https://doris.apache.org/download)


</div>


<div>
    <a href="https://twitter.com/doris_apache"><img src="https://img.shields.io/badge/- @Doris_Apache -424549?style=social&logo=x" height=25></a>
    &nbsp;
    <a href="https://github.com/apache/doris/discussions"><img src="https://img.shields.io/badge/- Discussion -red?style=social&logo=discourse" height=25></a>
    &nbsp;
    <a href="https://doris.apache.org/slack" height=25></a>
    &nbsp;
    <a href="https://medium.com/@ApacheDoris"><img src="https://img.shields.io/badge/-Medium-red?style=social&logo=medium" height=25></a>

</div>

</div>

---

<p align="center">

  <a href="https://trendshift.io/repositories/1156" target="_blank"><img src="https://trendshift.io/api/badge/repositories/1156" alt="apache%2Fdoris | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</p>




Apache Doris 是一款基于 MPP（大规模并行处理）架构构建的易用、高性能且支持实时分析的关系型数据库，以其极致的速度和易用性而闻名。在海量数据下，它仅需亚秒级响应时间即可返回查询结果，不仅支持高并发点查场景，还能胜任高吞吐量的复杂分析任务。

所有这一切使得 Apache Doris 成为报表分析、即席查询（Ad-Hoc Query）、统一数据仓库以及数据湖查询加速等场景的理想工具。基于 Apache Doris，用户可以构建多种应用，如用户行为分析、AB Test 平台、日志检索与分析、用户画像分析及订单分析等。

🎉 查看 🔗[所有版本](https://doris.apache.org/docs/releasenotes/all-release)，其中按时间顺序汇总了过去一年发布的 Apache Doris 版本信息。

👀 探索 🔗[官方网站](https://doris.apache.org/)，详细了解 Apache Doris 的核心功能、技术博客及用户案例。

## 📈 使用场景

如下图所示，经过各类数据集成与处理后，数据源通常存储于实时数仓 Apache Doris 以及离线数据湖或数据仓库（如 Apache Hive、Apache Iceberg 或 Apache Hudi）中。

<br />

<img src="https://cdn.selectdb.com/static/What_is_Apache_Doris_3_a61692c2ce.png" />

<br />


Apache Doris 广泛应用于以下场景：

- **实时数据分析**：
  
  - **实时报表与决策**：Doris 为内外企业提供实时更新的数据报表和仪表盘，支持自动化流程中的实时决策。
  
  - **即席分析（Ad-Hoc）**：Doris 提供多维数据分析能力，使业务能够进行快速智能分析与临时查询，帮助用户迅速从复杂数据中挖掘洞察。
  
  - **用户画像与行为分析**：Doris 可深入分析用户的参与、留存和转化等行为，同时支持人群洞察与圈选等场景下的行为分析。

- **湖仓一体分析**：
  
  - **湖仓查询加速**：凭借高效的查询引擎，Doris 显著加速湖仓数据的查询速度。
  
  - **联邦分析**：Doris 支持跨多个数据源的联邦查询，简化系统架构并打破数据孤岛。
  
  - **实时数据处理**：Doris 结合实时数据流与批处理计算能力，满足高并发、低延迟的复杂业务需求。

- **基于 SQL 的可观测性**：
  
  - **日志与事件分析**：Doris 支持对分布式系统中的日志和事件进行实时或批量分析，帮助快速定位问题并优化性能。


## 整体架构

Apache Doris 采用 MySQL 协议，高度兼容 MySQL 语法，并支持标准 SQL。用户可以通过多种客户端工具访问 Apache Doris，并能与 BI 工具无缝集成。

### 存算一体架构

Apache Doris 的存算一体架构精简且易于维护。如下图所示，它仅由两类进程组成：

- **前端节点（FE）：** 主要负责处理用户请求、查询解析与规划、元数据管理及节点管理任务。

- **后端节点（BE）：** 主要负责数据存储和查询执行。数据被划分为分片，并在 BE 节点间以多副本形式存储。

![Apache Doris 整体架构](https://cdn.selectdb.com/static/What_is_Apache_Doris_adb26397e2.png)

<br />

在生产环境中，可部署多个 FE 节点以实现容灾。每个 FE 节点均维护元数据的完整副本。FE 节点分为三种角色：

| 角色      | 功能                                                     |
| --------- | ------------------------------------------------------------ |
| Master（主节点）    | 负责元数据的读写操作。当 Master 发生元数据变更时，会通过 BDB JE 协议同步至 Follower 或 Observer 节点。 |
| Follower（跟随者节点）  | 负责读取元数据。若 Master 节点故障，可从 Follower 节点中选举产生新的 Master。 |
| Observer（观察者节点）  | 负责读取元数据，主要用于提升查询并发量。不参与集群主节点选举。 |

FE 和 BE 进程均支持水平扩展，单个集群可支撑数百台机器及数十 PB 的存储容量。FE 与 BE 进程采用一致性协议保障服务的高可用性与数据的高可靠性。存算一体架构高度集成，显著降低了分布式系统的运维复杂度。


## Apache Doris 核心特性

- **高可用性**：在 Apache Doris 中，元数据与数据均通过多副本存储，并通过多数派协议同步数据日志。只要多数节点完成写入即视为成功，即使部分节点故障也能保证集群持续可用。Apache Doris 支持同城及异地容灾，可实现双主/主从模式。当部分节点发生故障时，集群可自动隔离异常节点，避免影响整体可用性。

- **高兼容性**：Apache Doris 高度兼容 MySQL 协议与标准 SQL 语法，覆盖绝大多数 MySQL 和 Hive 函数。这种高兼容性使得用户能够无缝迁移并集成现有应用与工具。Doris 全面支持 MySQL 生态，允许用户使用 MySQL Client 等工具连接操作，极大便利了运维管理。同时，它完美适配各类 BI 报表工具及数据同步传输工具的 MySQL 协议兼容要求，确保数据分析与数据传输流程的高效稳定。

- **实时数仓**：基于 Apache Doris 可构建实时数仓服务。Doris 提供秒级数据摄入能力，可在数秒内捕获上游在线事务型数据库的增量变更并同步至 Doris。依托向量化引擎、MPP 架构与 Pipeline（流水线）执行引擎，Doris 实现亚秒级查询响应，从而打造高性能、低延迟的实时数仓平台。

- **统一湖仓**：Apache Doris 可基于数据湖或关系型数据库等外部数据源构建统一的湖仓一体架构。Doris 的统一湖仓方案实现了数据湖与数仓之间的无缝集成与自由数据流转，帮助用户直接利用数仓能力解决数据湖中的分析难题，同时充分发挥数据湖的数据管理能力以提升数据价值。

- **灵活建模**：Apache Doris 提供多种建表模型，如宽表模型、预聚合模型、星型/雪花模型等。在数据导入阶段，可通过 Flink 或 Spark 等计算引擎将数据扁平化为宽表写入 Doris；也可直接将数据导入 Doris，并通过视图、物化视图（Materialized Views）或实时多表 Join 进行数据建模操作。

## 技术概览

Doris 提供高效的 SQL 接口，并完全兼容 MySQL 协议。其查询引擎基于 MPP 架构设计，能够高效执行复杂分析查询，实现低延迟的实时查询。通过列式存储技术进行数据编码与压缩，显著优化了查询性能与存储空间利用率。

### 交互接口

Apache Doris 采用 MySQL 协议，支持标准 SQL，并高度兼容 MySQL 语法。用户可通过多种客户端工具访问 Apache Doris，并能与 BI 工具无缝集成，包括但不限于 Smartbi、DataEase、FineBI、Tableau、Power BI 和 Apache Superset。任何支持 MySQL 协议的 BI 工具均可将 Apache Doris 作为数据源使用。

### 存储引擎

Apache Doris 采用列式存储引擎，按列对数据进行编码、压缩与读取。这实现了极高的数据压缩率，大幅减少不必要的 I/O 扫描，从而更高效地利用 CPU 和 IO 资源。

Apache Doris 支持多种索引结构以最大限度减少数据扫描：

- **排序复合键索引（Sorted Compound Key Index）**：用户最多可指定三列构成复合排序键。这能有效裁剪数据，更好地支撑高并发报表场景。

- **最小/最大索引（Min/Max Index）**：在数值类型的等值与范围查询中实现高效的数据过滤。

- **BloomFilter 索引**：在高基数列的等值过滤与数据裁剪方面效果显著。

- **倒排索引（Inverted Index）**：支持对任意字段进行快速检索。

Apache Doris 支持多种数据模型，并针对不同场景进行了优化：

- **明细模型（Duplicate Key Model）**：专为事实表的明细数据存储需求设计。

- **主键模型（Primary Key Model / Unique Key Model）**：保证键值唯一；相同键的数据会被覆盖，从而实现行级数据更新。

- **聚合模型（Aggregate Key Model）**：对相同键的值列进行合并，通过预聚合显著提升查询性能。

Apache Doris 还支持强一致性的单表物化视图与异步刷新的多表物化视图。单表物化视图由系统自动刷新与维护，无需人工干预；多表物化视图可通过集群内调度或外部调度工具定期刷新，降低了数据建模的复杂度。

### 🔍 查询引擎

Apache Doris 拥有基于 MPP 架构的查询引擎，支持节点间及节点内的并行执行。它支持分布式 Shuffle Join（洗牌连接）处理大表关联，更好地应对复杂查询场景。

<br />

![Query Engine](https://cdn.selectdb.com/static/What_is_Apache_Doris_1_c6f5ba2af9.png)

<br />

Apache Doris 的查询引擎全面向量化，所有内存结构均以列式布局存储。这大幅减少了虚函数调用，提高了缓存命中率，并高效利用 SIMD（单指令多数据流）指令集。在宽表聚合场景下，Doris 的性能比非向量化引擎高出 5~10 倍。

<br />

![Doris query engine](https://cdn.selectdb.com/static/What_is_Apache_Doris_2_29cf58cc6b.png)

<br />

Apache Doris 采用自适应查询执行技术，根据运行时统计信息动态调整执行计划。例如，它可以生成运行时过滤器（Runtime Filter）并下推至探测端（Probe Side）。具体而言，它将过滤器下推至探测端最底层的扫描节点，大幅减少待处理数据量，从而提升 Join 性能。Apache Doris 的运行时过滤器支持 In、Min/Max 及 BloomFilter。

Apache Doris 采用 Pipeline（流水线）执行引擎，将查询拆分为多个子任务进行并行计算，充分发挥多核 CPU 的性能优势。同时，通过限制查询线程数量解决了线程爆炸问题。Pipeline 执行引擎减少了数据拷贝与共享开销，优化了排序和聚合操作，从而显著提升查询效率与吞吐量。

在优化器方面，Apache Doris 采用基于成本的优化器（CBO）、基于规则的优化器（RBO）与基于历史的优化器（HBO）相结合的混合优化策略。RBO 支持常量折叠、子查询重写、谓词下推等；CBO 支持 Join 重排序等优化；HBO 则根据历史查询信息推荐最优执行计划。这些多重优化措施确保 Doris 能够针对各类查询枚举出高性能的执行计划。


## 🎆 为什么选择 Apache Doris？

- 🎯 **易于使用**：仅含两个进程，无其他依赖；支持在线集群扩容与副本自动恢复；兼容 MySQL 协议并使用标准 SQL。

- 🚀 **高性能**：凭借列式存储引擎、现代 MPP 架构、向量化查询引擎、预聚合物化视图及数据索引，实现低延迟、高吞吐量极限性能。

- 🖥️ **单一系统统一支撑**：单个系统即可同时支持实时数据服务、交互式数据分析与离线数据处理场景。

- ⚛️ **联邦查询**：支持对 Hive、Iceberg、Hudi 等数据湖以及 MySQL、Elasticsearch 等数据库进行联邦查询。

- ⏩ **丰富的数据导入方式**：支持从 HDFS/S3 批量导入，以及通过 MySQL Binlog/Kafka 流式导入；支持通过 HTTP 接口微批写入及 JDBC Insert 实时写入。

- 🚙 **丰富的生态集成**：Spark 可通过 Spark-Doris-Connector 读写 Doris；Flink-Doris-Connector 使 Flink CDC 能够向 Doris 实现 Exactly-once（精确一次）数据写入；提供 DBT Doris Adapter，支持使用 DBT 转换 Doris 中的数据。

## 🙌 贡献者

**Apache Doris 已于 2022 年 6 月成功从 Apache 孵化器毕业，成为 Apache 顶级项目。** 

我们衷心感谢 🔗[社区贡献者](https://github.com/apache/doris/graphs/contributors) 对 Apache Doris 的付出。

[![contrib graph](https://contrib.rocks/image?repo=apache/doris)](https://github.com/apache/doris/graphs/contributors)

## 👨‍👩‍👧‍👦 用户

Apache Doris 在中国及全球拥有广泛的用户群体。截至目前，**全球已有数千家企业在生产环境中使用 Apache Doris。** 市值或估值排名前 50 的中国互联网公司中，超过 80% 已长期采用 Apache Doris，包括百度、美团、小米、京东、字节跳动、腾讯、网易、快手、新浪、360、米哈游及贝壳找房等。它也在金融、能源、制造、电信等传统行业广泛应用。

Apache Doris 用户列表：🔗[用户名单](https://doris.apache.org/users)

在 Apache Doris 官网添加贵公司 Logo：🔗[申请加入](https://github.com/apache/doris/discussions/27683)
 
## 👣 快速开始

### 📚 文档

所有文档：🔗[查看文档](https://doris.apache.org/docs/gettingStarted/what-is-apache-doris)  

### ⬇️ 下载 

所有发布版与二进制版本：🔗[前往下载](https://doris.apache.org/download) 

### 🗄️ 编译

查看编译指南：🔗[编译教程](https://doris.apache.org/community/source-install/compilation-with-docker)

### 📮 安装

查看安装与部署指南：🔗[安装部署](https://doris.apache.org/docs/install/preparation/env-checking) 

## 🧩 组件

### 📝 Doris Connector

Doris 提供 Spark/Flink Connector，支持通过该组件读取存储在 Doris 中的数据，同时也支持向 Doris 写入数据。

🔗[apache/doris-flink-connector](https://github.com/apache/doris-flink-connector)

🔗[apache/doris-spark-connector](https://github.com/apache/doris-spark-connector)


## 🌈 社区与支持

### 📤 订阅邮件列表

邮件列表是 Apache 社区最认可的沟通方式。查看如何 🔗[订阅邮件列表](https://doris.apache.org/community/subscribe-mail-list)

### 🙋 提交 Issue 或 Pull Request

如遇任何问题，欢迎随时提交 🔗[GitHub Issue](https://github.com/apache/doris/issues)，或在 🔗[GitHub Discussion](https://github.com/apache/doris/discussions) 中发帖讨论，并通过提交 🔗[Pull Request](https://github.com/apache/doris/pulls) 进行修复。

### 🍻 如何贡献

我们欢迎你的建议、反馈（包括批评意见）与代码贡献。查看 🔗[如何贡献](https://doris.apache.org/community/how-to-contribute/) 及 🔗[代码提交指南](https://doris.apache.org/community/how-to-contribute/pull-request/)

### ⌨️ Doris 改进提案（DSIP）

🔗[Doris 改进提案 (DSIP)](https://cwiki.apache.org/confluence/display/DORIS/Doris+Improvement+Proposals) 可视为**所有重大功能更新或改进的设计文档集合**。

### 🔑 后端 C++ 编码规范
🔗 [后端 C++ 编码规范](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=240883637) 需严格遵守，这将有助于我们实现更高的代码质量。

## 💬 联系我们

请通过以下邮件列表与我们联系。

| 名称                                                                          | 范围                           |                                                                 |                                                                     |                                                                              |
|:------------------------------------------------------------------------------|:--------------------------------|:----------------------------------------------------------------|:--------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [dev@doris.apache.org](mailto:dev@doris.apache.org)     | 开发相关讨论 | [订阅](mailto:dev-subscribe@doris.apache.org)   | [退订](mailto:dev-unsubscribe@doris.apache.org)   | [归档](http://mail-archives.apache.org/mod_mbox/doris-dev/)   |

## 🧰 相关链接

* Apache Doris 官方网站 - [访问站点](https://doris.apache.org)
* 开发者邮件列表 - <dev@doris.apache.org>。发送邮件至 <dev-subscribe@doris.apache.org>，并按回复指引完成订阅。
* Slack 频道 - [加入 Slack](https://doris.apache.org/slack)
* Twitter - [关注 @doris_apache](https://twitter.com/doris_apache)


## 📜 许可证

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

> **注意**
> 部分第三方依赖的许可证与 Apache 2.0 许可证不兼容。因此，你需要禁用某些 Doris 功能以符合 Apache 2.0 许可证要求。详细信息请参阅 `thirdparty/LICENSE.txt`