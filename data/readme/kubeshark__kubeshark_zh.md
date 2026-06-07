<p align="center">
  <img src="https://raw.githubusercontent.com/kubeshark/assets/master/svg/kubeshark-logo.svg" alt="Kubeshark" height="120px"/>
</p>

<p align="center">
    <a href="https://github.com/kubeshark/kubeshark/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/kubeshark/kubeshark?logo=GitHub&style=flat-square"></a>
    <a href="https://hub.docker.com/r/kubeshark/worker"><img alt="Docker pulls" src="https://img.shields.io/docker/pulls/kubeshark/worker?color=%23099cec&logo=Docker&style=flat-square"></a>
    <a href="https://discord.gg/WkvRGMUcx7"><img alt="Discord" src="https://img.shields.io/discord/1042559155224973352?logo=Discord&style=flat-square&label=discord"></a>
    <a href="https://join.slack.com/t/kubeshark/shared_invite/zt-3jdcdgxdv-1qNkhBh9c6CFoE7bSPkpBQ"><img alt="Slack" src="https://img.shields.io/badge/slack-join_chat-green?logo=Slack&style=flat-square"></a>
</p>

<p align="center"><b>面向 SRE 与 AI Agent 的网络可观测性（Network Observability）</b></p>

<p align="center">
  <a href="https://demo.kubeshark.com/">在线演示</a> · <a href="https://docs.kubeshark.com">文档</a>
</p>

---

Kubeshark 基于 eBPF（扩展伯克利包过滤）在内核层面索引集群范围的网路流量，通过结合网络、API 和 Kubernetes 语义，即时响应任何查询。

**你可以做什么：**

- **下载回溯性 PCAP 文件** —— 按节点、时间、工作负载和 IP 过滤集群范围的抓包数据。支持长期存储 PCAP，便于后续排查。
- **可视化网络数据** —— 通过实时仪表盘，结合 API、Kubernetes 或网络语义探索匹配的流量。
- **明文查看加密流量** —— 利用 eBPF 自动解密 TLS/mTLS 流量，无需密钥管理或 Sidecar（旁路容器）。
- **集成 AI 助手** —— 连接你常用的 AI 助手（如 Claude、Copilot），将网络数据融入事件响应和根因分析（Root Cause Analysis）等 AI 驱动的工作流。

![Kubeshark](https://github.com/kubeshark/assets/raw/master/png/stream.png)

---

## 快速上手

```bash
helm repo add kubeshark https://helm.kubeshark.com
helm install kubeshark kubeshark/kubeshark
kubectl port-forward svc/kubushark-front 8899:80
```

在浏览器中打开 `http://localhost:8899`。你已经开始捕获流量了。

> 生产环境使用时，我们建议使用 [Ingress Controller](https://docs.kubeshark.com/en/ingress) 替代端口转发。

**通过 MCP 连接 AI Agent：**

```bash
brew install kubeshark
claude mcp add kubeshark -- kubeshark mcp
```

[查看 MCP 配置指南 →](https://docs.kubeshark.com/en/mcp)

---

### 面向 AI Agent 的网络数据

Kubeshark 通过 [MCP](https://docs.kubeshark.com/en/mcp) 暴露集群范围的网路数据，使 AI Agent 能够通过自然语言查询流量、调查 API 调用并执行根因分析。

> *“为什么下午 2:15 的结账流程失败了？”*
> *“哪些服务的错误率超过 1%？”*
> *“展示所有节点间路径的 TCP 重传率”*
> *“追踪请求 abc123 在所有服务中的流转路径”*

兼容 Claude Code、Cursor 以及任何支持 MCP 的 AI 工具。

![MCP Demo](https://github.com/kubeshark/assets/raw/master/gif/mcp-demo.gif)

[查看 MCP 配置指南 →](https://docs.kubeshark.com/en/mcp)

### AI 技能

开源且可复用的技能模块，在 Kubeshark MCP 工具之上为 AI Agent 提供特定领域的 workflow（工作流）：

| Skill | Description |
|-------|-------------|
| **[网络 RCA](skills/network-rca/)** | 回溯性根因分析 —— 快照、流量拆解、PCAP 提取、趋势对比 |
| **[KFL](skills/kfl/)** | KFL（Kubeshark Filter Language）专家 —— 编写、调试和优化流量过滤规则 |

作为 Claude Code 插件安装：

```
/plugin marketplace add kubeshark/kubeshark
/plugin install kubeshark
```

或直接克隆并使用 —— 技能会根据对话上下文自动触发。

[查看 AI 技能文档 →](https://docs.kubeshark.com/en/mcp/skills)

---

### 结合 API、Kubernetes 与网络语义进行查询

Kubeshark 根据协议规范解析集群范围的网路流量并进行索引，支持 HTTP、gRPC、Redis、Kafka、DNS 等协议。单个 [KFL 查询](https://docs.kubeshark.com/en/v2/kfl2)即可融合这三层语义 —— Kubernetes 身份标识、API 上下文和网络属性，精准定位你所需的流量。无需任何代码插桩（instrumentation）。

![KFL query combining API, Kubernetes, and network semantics](https://github.com/kubeshark/assets/raw/master/png/kfl-semantics.png)

[KFL 参考文档 →](https://docs.kubeshark.com/en/v2/kfl2) · [流量索引机制 →](https://docs.kubeshark.com/en/v2/l7_api_dissection)

### 工作负载依赖拓扑图

可视化展示工作负载间的通信方式，呈现集群范围内的依赖关系、流量规模及协议使用情况。

![Service Map](https://github.com/kubeshark/assets/raw/master/png/servicemap.png)

[了解更多 →](https://docs.kubeshark.com/en/v2/service_map)

### 流量留存与 PCAP 导出

捕获并长期留存集群范围的原始网络流量（含已解密的 TLS）。可按时间范围、节点、工作负载和 IP 下载 PCAP 文件，直接用于 Wireshark 或任何兼容 PCAP 的工具。将快照存储至云存储（S3、Azure Blob、GCS）以实现长期保留及跨集群共享。

![Traffic Retention](https://github.com/kubeshark/assets/raw/master/png/snapshots-list.png)

[快照使用指南 →](https://docs.kubeshark.com/en/v2/traffic_snapshots) · [云存储配置 →](https://docs.kubeshark.com/en/snapshots_cloud_storage)

---

## 功能特性

| Feature | Description |
|---------|-------------|
| [**流量快照（Traffic Snapshots）**](https://docs.kubeshark.com/en/v2/traffic_snapshots) | 时间点快照，支持云存储（S3、Azure Blob、GCS），提供 PCAP 导出供 Wireshark 使用 |
| [**流量索引（Traffic Indexing）**](https://docs.kubeshark.com/en/v2/l7_api_dissection) | 实时与延迟 L7 层索引，支持请求/响应匹配及完整 Payload 提取 |
| [**协议支持（Protocol Support）**](https://docs.kubeshark.com/en/protocols) | HTTP、gRPC、GraphQL、Redis、Kafka、DNS 等 |
| [**TLS 解密（TLS Decryption）**](https://docs.kubeshark.com/en/encrypted_traffic) | 基于 eBPF 的解密，无需密钥管理，已包含在快照中 |
| [**AI 集成（AI Integration）**](https://docs.kubeshark.com/en/mcp) | MCP Server + 开源 AI 技能，支持网络 RCA 与流量过滤 |
| [**KFL 查询语言（KFL Query Language）**](https://docs.kubeshark.com/en/v2/kfl2) | 基于 CEL 的查询语言，融合 Kubernetes、API 和网络语义 |
| [**100% 本地部署（On-Premises）**](https://docs.kubeshark.com/en/air_gapped) | 支持物理隔离环境（Air-gapped），无外部依赖 |

---

## 安装方式

| Method | Command |
|--------|---------|
| Helm | `helm repo add kubeshark https://helm.kubeshark.com && helm install kubeshark kubeshark/kubeshark` |
| Homebrew | `brew install kubeshark && kubeshark tap` |
| 二进制文件 | [下载](https://github.com/kubeshark/kubeshark/releases/latest) |

[查看安装指南 →](https://docs.kubeshark.com/en/install)

---

## 贡献代码

我们欢迎社区贡献。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[Apache-2.0](LICENSE)