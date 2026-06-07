![Pinpoint](web/psd/logo.png)

[![Maven](https://img.shields.io/github/actions/workflow/status/pinpoint-apm/pinpoint/maven.yml?branch=master&label=build&logo=github)](https://github.com/pinpoint-apm/pinpoint/actions?query=workflow%3AMaven)
[![codecov](https://codecov.io/gh/pinpoint-apm/pinpoint/branch/master/graph/badge.svg)](https://codecov.io/gh/pinpoint-apm/pinpoint)

## 最新版本 (2026/05/21)

我们很高兴地宣布 Pinpoint v3.1.0 正式发布。
请访问 (https://github.com/pinpoint-apm/pinpoint/releases/tag/v3.1.0) 查看完整发布说明。

当前稳定版本为 [v3.1.0](https://github.com/pinpoint-apm/pinpoint/releases/tag/v3.1.0)。

## 在线演示

欢迎通过我们的[演示环境](http://223.130.142.103:8080/main/ApiGateway@SPRING_BOOT/5m?inbound=1&outbound=4&wasOnly=false&bidirectional=false)快速体验 Pinpoint！

## PHP、Python 支持

Pinpoint 同样支持使用 PHP 和 Python 编写的应用程序。[请查看我们的 Agent 仓库](https://github.com/pinpoint-apm/pinpoint-c-agent)。

## 关于 Pinpoint

**Pinpoint** 是一款面向大规模分布式系统的 APM（Application Performance Management，应用性能管理）工具，主要使用 Java / [PHP](https://github.com/pinpoint-apm/pinpoint-c-agent)/[PYTHON]((https://github.com/pinpoint-apm/pinpoint-c-agent)) 编写。
受 [Dapper](http://research.google.com/pubs/pub36356.html "Google Dapper") 启发，
Pinpoint 提供了一套解决方案，通过追踪分布式应用间的事务（Transaction）流转，帮助你分析系统的整体架构以及内部组件的相互连接关系。

如果你有以下需求，强烈建议试用 **Pinpoint**：

* 一目了然地掌握你的 *[应用拓扑结构](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview)*
* 对应用程序进行 *实时（Real-Time）监控*
* 获得每个事务的 *代码级可见性（code-level visibility）*
* 实现 APM Agent 的 *零代码侵入式安装*
* 对性能的影响极小（资源消耗仅增加约 3%）

## 快速开始
 * [快速入门指南](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart)：用于简单测试运行 Pinpoint
 * [安装指南](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/installation)：获取详细操作说明。

## 部署到 Kubernetes
 * [pinpoint-kubernetes](https://github.com/pinpoint-apm/pinpoint-kubernetes) 
 
## 功能概览
现代服务通常由众多不同的组件构成，它们不仅相互通信，还会向外部服务发起 API 调用。而每个事务的具体执行过程往往是一个“黑盒”。Pinpoint 会追踪这些组件间的事务流转，提供清晰的视图以帮助你快速定位问题区域和潜在瓶颈。<br/>
如需更详细的引导，请观看我们的 *[Pinpoint 入门介绍](https://pinpoint-apm.gitbook.io/pinpoint/#want-a-quick-tour)* 视频。

* **ServerMap（服务器拓扑图）** - 通过可视化组件间的互联关系，轻松掌握任意分布式系统的架构。点击节点可查看该组件的详细信息，如当前状态和事务计数。
  ![Server Map](doc/images/ss_server-map.png)

* **Realtime Active Thread Chart（实时活跃线程图表）** - 实时监控应用程序内部的活跃线程情况。
* **Request/Response Scatter Chart（请求/响应散点图）** - 可视化展示随时间变化的请求数量和响应模式，以便发现潜在问题。你可以通过**在图表上拖拽**来选中特定事务以查看详细信息。

  ![Call Stack](doc/images/ss_call-stack.png)

* **CallStack（调用栈）** - 在分布式环境中提供每个事务的代码级可见性，在一个视图中即可定位瓶颈和故障点。

  ![Call Stack](doc/images/ss_call-stack.png)

* **Inspector（检查器）** - 查看应用程序的更多详细信息，如 CPU 使用率、内存/垃圾回收情况、TPS 以及 JVM 参数等。

  ![Inspector](doc/images/ss_inspector.png)

* **URI-metric**
  ![URI-Metric](doc/images/ss-uri-metric.png)

* **Infrastructure（基础设施指标）**
  ![Infrastructure](doc/images/ss-Infrastructure-metric.png)

* **Error-Analysis（错误分析）**
  ![Error-Analysis 1](doc/images/ss_error-analysis1.png)
  ![Error-Analysis 2](doc/images/ss_error-analysis3.gif)

## 支持的模块
* JDK 8+
* [Tomcat](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/tomcat), [Jetty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jetty), [JBoss EAP](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jboss), [Websphere](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/websphere), [Vertx](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/vertx), [Weblogic](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/weblogic), [Undertow](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow), [Akka HTTP](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/akka-http)
* [Spring](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring), [Spring Boot](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-boot) ([Embedded Tomcat](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/tomcat), [Jetty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jetty), [Undertow](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow), [Reactor Netty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor-netty)), [Spring WebFlux](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-webflux), [Spring TX](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-tx), [Spring Cloud Sleuth](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-cloud-sleuth), [RestTemplate](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/resttemplate), [Ktor](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/ktor)
* Apache HttpClient [3](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/httpclient3) / [4](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/httpclient4) / [5](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/httpclient5), [JDK HttpConnector](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jdk-http), [JDK HttpClient](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jdk-httpclient), [GoogleHttpClient](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/google-httpclient), [OkHttpClient](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/okhttp), [NingAsyncHttpClient](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/ning-asynchttpclient), [Netty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/netty)
* [Thrift](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/thrift), [DUBBO](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/apache-dubbo), [GRPC](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/grpc), [Apache CXF](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/cxf)
* [ActiveMQ](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/activemq-client), [RabbitMQ](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rabbitmq), [Kafka](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/kafka), [RocketMQ](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rocketmq), [Pulsar](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/pulsar), [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)
* [MySQL](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/mysql-jdbc), [Oracle](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/oracle-jdbc), [MSSQL](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/mssql-jdbc), [JTDS](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jtds), [CUBRID](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/cubrid-jdbc), [POSTGRESQL](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/postgresql-jdbc), [MariaDB](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/mariadb-jdbc), [Informix](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/informix-jdbc), [DB2](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/db2-jdbc), [ClickHouse](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/clickhouse-jdbc), [Dameng](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/dameng-jdbc), [Spring Data R2DBC](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-data-r2dbc)
* [Arcus](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/arcus), [Memcached](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/arcus), Redis([Jedis](https://github.com/pinpoint-apm/pinpoint/blob/master/agent-module/plugins/redis), [Lettuce](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-lettuce), [Redisson](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-redisson)), [CASSANDRA](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/cassandra), [MongoDB](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/mongodb), [Hbase](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/hbase), [Elasticsearch](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/elasticsearch)
* [iBATIS](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/ibatis), [MyBatis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/mybatis)
* [DBCP](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/dbcp), [DBCP2](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/dbcp2), [HIKARICP](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/hikaricp), [DRUID](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/druid)
* [Gson](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/gson), [Jackson](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jackson), [Json Lib](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/json-lib), [Fastjson](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/fastjson)
* [log4j](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/log4j), [Logback](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/logback), [log4j2](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/log4j2)
* [Hystrix](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/hystrix), [Resilience4j](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/resilience4j), [RxJava](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rxjava), [Reactor](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor)
* [AWS SDK S3](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/aws-sdk-s3), [OpenWhisk](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/openwhisk), [Kotlin Coroutines](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/kotlin-coroutines)

## 兼容性说明

运行 Pinpoint 所需的 Java 版本：
<!-- <compatibilityJava.md> -->
| Pinpoint 版本 | Agent | Collector | Web | Batch | 
|------------------|-------|-----------|-----|-------|
| 2.0.x            | 6-13  | 8         | 8   | 8     |
| 2.1.x            | 6-14  | 8         | 8   | 8     |
| 2.2.x            | 7-14  | 8         | 8   | 8     |
| 2.3.x            | 7-17  | 8         | 8   | 8     |
| 2.4.x            | 7-18  | 11        | 11  | 11    |
| 2.5.x            | 8-19  | 11        | 11  | 11    |
| 3.0.x            | 8-21  | 17        | 17  | 17    |
| 3.1.x            | 8-25  | 17        | 17  | 17    |

<!-- </compatibilityJava.md> -->
HBase 兼容性表：
<!-- <compatibilityHbase.md> -->
| Pinpoint 版本 | HBase 1.x | HBase 2.x                                                                                                             |
|------------------|-----------|-----------------------------------------------------------------------------------------------------------------------|
| 2.0.x - 2.2.x    | yes       | [可选](https://pinpoint-apm.gitbook.io/pinpoint/documents/hbase-upgrade#do-you-like-to-use-hbase-2x-for-pinpoint) |
| 2.3.x - 2.5.x    | yes       | [hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/2.3.x/hbase2-module)                                    |
| 3.0.x            | no        | yes                                                                                                                   |
| 3.1.x            | no        | yes                                                                                                                   |

<!-- </compatibilityHbase.md> -->
Agent - Collector 兼容性表：
<!-- <compatibilityPinpoint.md> -->

| Agent 版本 | Collector 2.x.x | Collector 3.0.x | Collector 3.1.x |
|---------------|-----------------|-----------------|-----------------|
| 2.x.x         | yes             | yes             | yes             |
| 3.0.x         | no              | yes             | yes             |
| 3.1.x         | no              | no              | yes             |

<!-- </compatibilityPinpoint.md> -->
Pinot 兼容性表：
<!-- <compatibilityPinot.md> -->
| Pinpoint 版本 | Pinot 0.11.0 | Pinot 0.12.0 | Pinot 1.0.0 | [Pinot 1.2.0](https://github.com/pinpoint-apm/pinpoint/issues/11613) | Pinot 1.3.0 |
|------------------|--------------|--------------|-------------|----------------------------------------------------------------------|-------------|
| 2.5.x            | yes          | yes          | yes         | yes                                                                  | yes         |
| 3.0.x            | no           | no           | yes         | yes                                                                  | yes         |
| 3.1.x            | no           | no           | no          | no                                                                    | yes         |
<!-- </compatibilityPinot.md> -->

## 社区交流

[GitHub Issues](https://github.com/pinpoint-apm/pinpoint/issues)   
[Gitter 频道](https://gitter.im/naver/pinpoint)  

我们现已建立中文社区，欢迎加入！

<details>
  <summary> 👆 点击展开
</summary>

QQ 群1: 897594820 | QQ 群2: 812507584 | QQ 群3: 882020485| DING 群 : 21981598
:----------------: |:----------------: | :-----------: | :-----------: 
![QQ Group1](doc/images/NAVERPinpoint.png) | ![QQ Group2](doc/images/NAVERPinpoint2.png)| ![QQ Group3](doc/images/NAVERPinpoint3.png)| ![DING Group](doc/images/NaverPinpoint交流群-DING.jpg)

</details>

## 许可证
Pinpoint 遵循 Apache License, Version 2.0 开源协议。
完整许可条款请参阅 [LICENSE](LICENSE)。

```
Copyright 2018 NAVER Corp.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```