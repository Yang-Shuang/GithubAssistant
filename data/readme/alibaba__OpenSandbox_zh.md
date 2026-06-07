<div align="center">
  <img src="docs/assets/logo.svg" alt="OpenSandbox logo" width="150" />

  <h1>OpenSandbox</h1>

  <p align="center">
    <a href="https://trendshift.io/repositories/21828" target="_blank">
      <img src="https://trendshift.io/api/badge/repositories/21828" alt="alibaba%2FOpenSandbox | Trendshift" style="width: 320px; height: 70px;" width="320" height="70" />
    </a>
  </p>

<p align="center">
  <a href="https://github.com/alibaba/OpenSandbox">
    <img src="https://img.shields.io/github/stars/alibaba/OpenSandbox.svg?style=social" alt="GitHub stars" />
  </a>
  <a href="https://deepwiki.com/alibaba/OpenSandbox">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0.html">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="license" />
  </a>
  <a href="https://www.bestpractices.dev/projects/12588">
    <img src="https://www.bestpractices.dev/projects/12588/badge" alt="OpenSSF Best Practices" />
  </a>
  <a href="https://badge.fury.io/py/opensandbox">
    <img src="https://badge.fury.io/py/opensandbox.svg" alt="PyPI version" />
  </a>
  <a href="https://badge.fury.io/js/@alibaba-group%2Fopensandbox">
    <img src="https://badge.fury.io/js/@alibaba-group%2Fopensandbox.svg" alt="npm version" />
  </a>
  <a href="https://landscape.cncf.io/?item=orchestration-management--scheduling-orchestration--opensandbox">
    <img src="https://img.shields.io/badge/CNCF-Landscape-0C66E4" alt="CNCF Landscape" />
  </a>
  <a href="https://qr.dingtalk.com/action/joingroup?code=v1,k1,A4Bgl5q1I1eNU/r33D18YFNrMY108aFF38V+r19RJOM=&_dt_no_comment=1&origin=11">
    <img src="https://img.shields.io/badge/DingTalk-Join-0089FF?logo=dingtalk&logoColor=white" alt="DingTalk" />
  </a>
  <a href="https://github.com/alibaba/OpenSandbox/actions">
    <img src="https://github.com/alibaba/OpenSandbox/actions/workflows/real-e2e.yml/badge.svg?branch=main" alt="E2E Status" />
  </a>
  <a href="https://github.com/alibaba/OpenSandbox/actions">
    <img src="https://github.com/alibaba/OpenSandbox/actions/workflows/kubernetes-nightly-build.yml/badge.svg?branch=main" alt="E2E Status" />
  </a>
</p>

  <hr />
</div>

[英文文档](https://open-sandbox.ai/) | [中文文档](https://open-sandbox.ai/zh/)

OpenSandbox 是一款面向 AI 应用的**通用沙箱平台**，提供多语言 SDK、统一的沙箱 API 以及 Docker/Kubernetes 运行时，适用于编码智能体（Coding Agents）、GUI 智能体、智能体评估、AI 代码执行和强化学习（RL）训练等场景。

OpenSandbox 现已收录于 [CNCF Landscape](https://landscape.cncf.io/?item=orchestration-management--scheduling-orchestration--opensandbox)。

## 功能特性

- **多语言 SDK**：提供 Python、Java/Kotlin、JavaScript/TypeScript、C#/.NET、Go 的沙箱 SDK。
- **沙箱协议（Protocol）**：定义了沙箱生命周期管理 API 和沙箱执行 API，以便你扩展自定义的沙箱运行时。
- **沙箱运行时（Runtime）**：内置生命周期管理，支持 Docker 和[高性能 Kubernetes 运行时](./kubernetes)，同时满足本地运行与大规模分布式调度需求。
- **沙箱环境（Environments）**：内置命令、文件系统和代码解释器实现。示例涵盖编码智能体（如 Claude Code）、浏览器自动化（Chrome、Playwright）以及桌面环境（VNC、VS Code）。
- **网络策略**：统一的[入口网关（Ingress Gateway）](components/ingress)，支持多种路由策略，并提供每沙箱级别的[出口控制（egress controls）](components/egress)。
- **强隔离性**：支持 gVisor、Kata Containers 和 Firecracker microVM 等安全容器运行时，以增强沙箱工作负载与宿主机之间的隔离。详见[安全容器运行指南](docs/secure-container.md)。

## SDKs

Python:

```bash
pip install opensandbox
```

Java/Kotlin (Gradle Kotlin DSL):

```kotlin
dependencies {
    implementation("com.alibaba.opensandbox:sandbox:{latest_version}")
}
```

Java/Kotlin (Maven):

```xml
<dependency>
    <groupId>com.alibaba.opensandbox</groupId>
    <artifactId>sandbox</artifactId>
    <version>{latest_version}</version>
</dependency>
```

JavaScript/TypeScript:

```bash
npm install @alibaba-group/opensandbox
```

C#/.NET:

```bash
dotnet add package Alibaba.OpenSandbox
```

Go:

```bash
go get github.com/alibaba/OpenSandbox/sdks/sandbox/go
```

## CLI

OpenSandbox 还提供 `osb`，一款用于常见沙箱工作流的终端 CLI：创建沙箱、运行命令、传输文件、检查诊断信息以及管理运行时出口策略。

安装:

```bash
pip install opensandbox-cli
# or
uv tool install opensandbox-cli
```

快速开始:

```bash
osb config init
osb config set connection.domain localhost:8080
osb config set connection.protocol http
osb config set connection.api_key <your-api-key>
osb sandbox create --image python:3.12 --timeout 30m -o json
osb command run <sandbox-id> -o raw -- python -c "print(1 + 1)"
```

完整命令参考请参见 [CLI README](cli/README.md)。

## MCP

OpenSandbox MCP Server 向支持 MCP 的客户端（如 Claude Code 和 Cursor）暴露沙箱创建、命令执行及文本文件操作接口。

安装与运行:

```bash
pip install opensandbox-mcp
opensandbox-mcp --domain localhost:8080 --protocol http
```

最小化 stdio 配置:

```json
{
  "mcpServers": {
    "opensandbox": {
      "command": "opensandbox-mcp",
      "args": ["--domain", "localhost:8080", "--protocol", "http"]
    }
  }
}
```

特定客户端的配置请参见 [MCP README](sdks/mcp/sandbox/python/README.md)。

## 入门指南

环境要求:

- Docker（本地运行必需）
- Python 3.10+（示例与本地运行时必需）

### 安装并配置沙箱服务端

```bash
uvx opensandbox-server init-config ~/.sandbox.toml --example docker

uvx opensandbox-server

# Show help
# uvx opensandbox-server -h
```

### 创建代码解释器并执行命令/代码

安装 Code Interpreter SDK

```bash
uv pip install opensandbox-code-interpreter
```

创建沙箱并执行命令和代码。

```python
import asyncio
from datetime import timedelta

from code_interpreter import CodeInterpreter, SupportedLanguage
from opensandbox import Sandbox
from opensandbox.models import WriteEntry

async def main() -> None:
    # 1. Create a sandbox
    sandbox = await Sandbox.create(
        "opensandbox/code-interpreter:v1.0.2",
        entrypoint=["/opt/opensandbox/code-interpreter.sh"],
        env={"PYTHON_VERSION": "3.11"},
        timeout=timedelta(minutes=10),
    )

    async with sandbox:

        # 2. Execute a shell command
        execution = await sandbox.commands.run("echo 'Hello OpenSandbox!'")
        print(execution.logs.stdout[0].text)

        # 3. Write a file
        await sandbox.files.write_files([
            WriteEntry(path="/tmp/hello.txt", data="Hello World", mode=644)
        ])

        # 4. Read a file
        content = await sandbox.files.read_file("/tmp/hello.txt")
        print(f"Content: {content}") # Content: Hello World

        # 5. Create a code interpreter
        interpreter = await CodeInterpreter.create(sandbox)

        # 6. Execute Python code (single-run, pass language directly)
        result = await interpreter.codes.run(
              """
                  import sys
                  print(sys.version)
                  result = 2 + 2
                  result
              """,
              language=SupportedLanguage.PYTHON,
        )

        print(result.result[0].text) # 4
        print(result.logs.stdout[0].text) # 3.11.14

    # 7. Cleanup the sandbox
    await sandbox.kill()

if __name__ == "__main__":
    asyncio.run(main())
```

### 更多示例

OpenSandbox 提供了涵盖 SDK 使用、智能体集成、浏览器自动化及训练工作负载的示例。所有示例代码均位于 `examples/` 目录下。

#### 🎯 基础示例

- **[code-interpreter](examples/code-interpreter/README.md)** - 沙箱内端到端的代码解释器（Code Interpreter）SDK 工作流。
- **[aio-sandbox](examples/aio-sandbox/README.md)** - 使用 OpenSandbox SDK 的一体化沙箱环境搭建。
- **[agent-sandbox](examples/agent-sandbox/README.md)** - 结合 [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) 在 Kubernetes 上运行 OpenSandbox 工作负载的集成示例。
- **存储卷（Volumes）** — [Docker PVC / 命名卷](examples/docker-pvc-volume-mount/README.md)、[Docker OSSFS](examples/docker-ossfs-volume-mount/README.md)、[Kubernetes PVC](examples/kubernetes-pvc-volume-mount/README.md)：持久化与共享存储模式。

#### 🤖 编码智能体集成

- **CLI 工具** — [Claude Code](examples/claude-code/README.md)、[Gemini CLI](examples/gemini-cli/README.md)、[OpenAI Codex CLI](examples/codex-cli/README.md)、[Qwen Code](examples/qwen-code/README.md)、[Kimi CLI](examples/kimi-cli/README.md)：在 OpenSandbox 内部运行各厂商的 CLI。
- **[langgraph](examples/langgraph/README.md)** - 支持回退重试机制的 LangGraph 状态机工作流，用于创建/运行沙箱任务。
- **[google-adk](examples/google-adk/README.md)** - 使用 OpenSandbox 工具进行文件读写和命令执行的 Google ADK 智能体示例。
- **[openclaw](examples/openclaw/README.md)** - 在沙箱内启动 OpenClaw Gateway。

#### 🌐 浏览器与桌面环境

- **[chrome](examples/chrome/README.md)** - 支持 VNC 和 DevTools 访问的 Chromium 沙箱，用于自动化与调试。
- **[playwright](examples/playwright/README.md)** - Playwright + Chromium 无头抓取与测试示例。
- **[desktop](examples/desktop/README.md)** - 沙箱内完整的桌面环境，支持 VNC 访问。
- **[vscode](examples/vscode/README.md)** - 在沙箱内运行 code-server（VS Code Web）以实现远程开发。

#### 🧠 机器学习与训练

- **[rl-training](examples/rl-training/README.md)** - 沙箱内运行 DQN CartPole 训练，支持检查点保存与摘要输出。

更多详情请参阅 [examples](examples/README.md) 及各示例目录下的 README 文件。

## 项目结构

| Directory | Description                                                      |
|-----------|------------------------------------------------------------------|
| [`sdks/`](sdks/) | 多语言 SDK（Python、Java/Kotlin、TypeScript/JavaScript、C#/.NET） |
| [`specs/`](specs/README.md) | OpenAPI 规范与生命周期规范                                      |
| [`server/`](server/README.md) | Python FastAPI 沙箱生命周期服务端                                |
| [`cli/`](cli/README.md) | OpenSandbox 命令行界面                                           |
| [`kubernetes/`](kubernetes/README.md) | Kubernetes 部署与示例                                            |
| [`components/execd/`](components/execd/README.md) | 沙箱执行守护进程（命令与文件操作）                               |
| [`components/ingress/`](components/ingress/README.md) | 沙箱流量入口代理                                                 |
| [`components/egress/`](components/egress/README.md) | 沙箱网络出口控制                                                 |
| [`sandboxes/`](sandboxes/) | 运行时沙箱实现                                                   |
| [`examples/`](examples/README.md) | 集成示例与用例                                                   |
| [`oseps/`](oseps/README.md) | OpenSandbox 增强提案                                             |
| [`docs/`](docs/) | 架构与设计文档                                                   |
| [`tests/`](tests/) | 跨组件端到端测试                                                 |
| [`scripts/`](scripts/) | 开发与维护脚本                                                   |

详细架构说明请参见 [docs/architecture.md](docs/architecture.md)。

## 相关文档

- [docs/architecture.md](docs/architecture.md) – 整体架构与设计理念
- [docs/release-verification.md](docs/release-verification.md) - 发布签名与制品验证
- [oseps/README.md](oseps/README.md) – OpenSandbox 增强提案
- SDK
  - 沙箱基础 SDK（[Java/Kotlin SDK](sdks/sandbox/kotlin/README.md)、[Python SDK](sdks/sandbox/python/README.md)、[JavaScript/TypeScript SDK](sdks/sandbox/javascript/README.md)、[C#/.NET SDK](sdks/sandbox/csharp/README.md)）、[Go SDK](sdks/sandbox/go/README.md) - 包含沙箱生命周期、命令执行、文件操作
  - 代码解释器 SDK（[Java/Kotlin SDK](sdks/code-interpreter/kotlin/README.md)、[Python SDK](sdks/code-interpreter/python/README.md)、[JavaScript/TypeScript SDK](sdks/code-interpreter/javascript/README.md)、[C#/.NET SDK](sdks/code-interpreter/csharp/README.md)）- 代码解释器功能
- [cli/README.md](cli/README.md) - OpenSandbox CLI 安装与命令参考
- [sdks/mcp/sandbox/python/README.md](sdks/mcp/sandbox/python/README.md) - MCP Server 安装与客户端配置
- [specs/README.md](specs/README.md) - 沙箱生命周期 API 和沙箱执行 API 的 OpenAPI 定义
- [server/README.md](server/README.md) - 沙箱服务端启动与配置；支持 Docker 和 Kubernetes 运行时
- [ROADMAP.md](ROADMAP.md) - 轻量级项目路线图与规划流程

## 许可证

本项目基于 [Apache 2.0 License](LICENSE) 开源。

## 路线图

当前项目路线图、规划范围及路线图项的管理方式，请参见 [ROADMAP.md](ROADMAP.md)。

## 联系方式与讨论

- **Issues**：通过 GitHub Issues 提交 Bug、功能请求或设计讨论
- **钉钉（DingTalk）**：加入 [OpenSandbox 技术交流群](https://qr.dingtalk.com/action/joingroup?code=v1,k1,A4Bgl5q1I1eNU/r33D18YFNrMY108aFF38V+r19RJOM=&_dt_no_comment=1&origin=11)

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=alibaba/OpenSandbox&type=date&legend=top-left)](https://www.star-history.com/#alibaba/OpenSandbox&type=date&legend=top-left)