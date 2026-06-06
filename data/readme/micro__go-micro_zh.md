# Go Micro [![Go.Dev reference](https://img.shields.io/badge/go.dev-reference-007d9c?logo=go&logoColor=white&style=flat-square)](https://pkg.go.dev/go-micro.dev/v5?tab=doc) [![Go Report Card](https://goreportcard.com/badge/github.com/go-micro/go-micro)](https://goreportcard.com/report/github.com/go-micro/go-micro)

Go Micro 是一个用于构建 AI Agent（智能体）可调用的微服务框架。

使用 Go 编写服务。服务会自动注册、相互发现，并通过 RPC（远程过程调用）和事件进行通信。每个端点都会自动通过 [MCP](https://modelcontextprotocol.io/) 成为 AI 可调用的工具。Agent 负责跨服务的编排协调，因此服务之间无需互相调用。

## Sponsors

<a href="https://go-micro.dev/blog/3"><img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Anthropic_logo.svg" height="26" /></a>
&nbsp;&nbsp;
<a href="https://go-micro.dev/blog/8"><img src="https://www.atlascloud.ai/logo.svg" height="26" /></a>

## Quick Start

安装 CLI：

```bash
# Binary (no Go required)
curl -fsSL https://go-micro.dev/install.sh | sh

# Or with Go
go install go-micro.dev/v5/cmd/micro@v5.25.0
```

根据描述生成服务并启动它们：

```bash
micro run --prompt "a task management system with categories" --provider anthropic
```

AI 会设计架构，你进行审查，随后它生成包含实际业务逻辑的请求处理器（handler），编译并启动它们：

```
Services:
  ● category — Manages task categories
  ● task — Task management with status tracking

Generate? [Y/n]
```

```
Micro

  Dashboard   http://localhost:8080
  API         http://localhost:8080/api/{service}/{method}
  Agent       http://localhost:8080/agent

  Services:
    ● category
    ● task
```

通过 Agent 与你的服务交互：

```bash
micro chat --provider anthropic
> Create a Work category, then add a task called 'Finish report' to it
```

Agent 从注册中心发现服务，将每个端点视为工具，并进行跨服务编排：

```
→ category_Category_Create({"name":"Work","user_id":"user1"})
← {"record":{"id":"f633...","name":"Work"},"success":true}
→ task_Task_Create({"title":"Finish report","category_id":"f633..."})
← {"record":{"id":"a1b2...","title":"Finish report","status":"pending"}}

Created Work category and added 'Finish report' task to it.
```

当你需要现有功能之外的能力时，Agent 会在对话过程中动态生成新服务：

```
> I need to track shipping. Create a shipment for order 123 to London.

  ⚡ generating shipping service...
  ✓ shipping
  → shipping_Shipping_Create({"order_id":"123","destination":"London"})
  ← {"record":{"id":"xyz...","status":"pending"}}

  Created shipment for order 123 going to London.
```

随时手动编辑生成的代码——重新运行会保留你的修改。[阅读更多](https://go-micro.dev/blog/13)。

## Writing Services

底层来看，服务是一个带有方法的结构体。文档注释和 `@example` 标签会自动转换为 AI Agent 的工具描述。

```go
package main

import (
    "go-micro.dev/v5"
)

type Request struct {
    Name string `json:"name"`
}

type Response struct {
    Message string `json:"message"`
}

type Say struct{}

// Hello greets a person by name.
// @example {"name": "Alice"}
func (h *Say) Hello(ctx context.Context, req *Request, rsp *Response) error {
    rsp.Message = "Hello " + req.Name
    return nil
}

func main() {
    service := micro.New("greeter")
    service.Handle(new(Say))
    service.Run()
}
```

运行后即可通过多种方式访问——REST、gRPC、MCP、Agent 测试环境：

```bash
micro run
# Dashboard:   http://localhost:8080
# API:         http://localhost:8080/api/{service}/{method}
# Agent:       http://localhost:8080/agent
# MCP Tools:   http://localhost:8080/mcp/tools
```

你也可以从模板生成服务脚手架：

```bash
micro new helloworld
micro new contacts --template crud
```

## Features

| Category | What | Details |
|----------|------|---------|
| **AI** | MCP gateway | Every endpoint is an AI tool automatically |
| **AI** | 7 LLM providers | Anthropic, OpenAI, Gemini, Groq, Mistral, Together, Atlas Cloud |
| **AI** | Agent orchestration | `micro chat` — LLM calls services as tools |
| **AI** | Service generation | `micro run --prompt` — describe a system, get running services |
| **Discovery** | Service registry | mDNS (default), Consul, etcd |
| **Communication** | RPC client/server | gRPC transport, load balancing, streaming |
| **Messaging** | Pub/sub events | NATS, RabbitMQ, HTTP broker |
| **Storage** | Key-value store | File (bbolt), Postgres, NATS KV |
| **Data** | Typed model layer | CRUD + queries, SQLite/Postgres backends |
| **DX** | Hot reload | `micro run` watches files, rebuilds on change |
| **DX** | Templates | `micro new --template crud/pubsub/api` |
| **Deploy** | One-command deploy | `micro deploy user@server` — SSH + systemd, no Docker |
| **Plugins** | Everything swappable | All abstractions are Go interfaces |

## CLI

| Command | Purpose |
|---------|---------|
| `micro run --prompt "..."` | Generate services from a description and run them |
| `micro chat --provider anthropic` | Talk to services through an LLM |
| `micro new myservice` | Scaffold a service |
| `micro run` | Dev mode: hot reload, gateway, agent playground |
| `micro call service endpoint '{}'` | Call a service from the CLI |
| `micro build` | Compile production binaries |
| `micro deploy user@server` | Deploy via SSH + systemd |

## Multi-Service Projects

同时运行多个服务：

```go
users := micro.New("users", micro.Address(":9001"))
orders := micro.New("orders", micro.Address(":9002"))

users.Handle(new(Users))
orders.Handle(new(Orders))

g := micro.NewGroup(users, orders)
g.Run()
```

或使用 `micro.mu` 配置文件：

```
service users
    path ./users

service orders
    path ./orders
    depends users
```

## Data Model

支持强类型持久化，内置 CRUD 与查询功能：

```go
type User struct {
    ID    string `json:"id" model:"key"`
    Name  string `json:"name"`
    Email string `json:"email" model:"index"`
}

db := service.Model()
db.Register(&User{})
db.Create(ctx, &User{ID: "1", Name: "Alice", Email: "alice@example.com"})

var results []*User
db.List(ctx, &results, model.Where("email", "alice@example.com"))
```

后端存储：内存（默认）、SQLite、PostgreSQL。

## AI Providers

仅需更改一个导入即可切换提供商——全项目接口统一：

| Provider | Default Model |
|----------|---------------|
| Anthropic | `claude-sonnet-4-20250514` |
| OpenAI | `gpt-4o` |
| Google Gemini | `gemini-2.5-flash` |
| Groq | `llama-3.3-70b-versatile` |
| Mistral | `mistral-large-latest` |
| Together AI | `Llama-3.3-70B-Instruct-Turbo` |
| Atlas Cloud | `llama-3.3-70b` |

```go
m := ai.New("anthropic", ai.WithAPIKey(key))
resp, _ := m.Generate(ctx, &ai.Request{Prompt: "hello"})
```

## Examples

- [hello-world](examples/hello-world/) — Basic RPC service
- [multi-service](examples/multi-service/) — Multiple services in one binary
- [mcp](examples/mcp/) — MCP integration with AI agents
- [grpc-interop](examples/grpc-interop/) — Call go-micro from any gRPC client

查看[所有示例](examples/README.md)。

## Docs

- [Getting Started](internal/website/docs/getting-started.md)
- [AI Integration](internal/website/docs/ai-integration.md)
- [MCP & AI Agents](internal/website/docs/mcp.md)
- [Data Model](internal/website/docs/model.md)
- [Deployment](internal/website/docs/deployment.md)
- [Plugins](internal/website/docs/plugins.md)

包文档参考：https://pkg.go.dev/go-micro.dev/v5

## Adopters

- [Sourse](https://sourse.eu) — Earth observation platform with embedded Kubernetes and SaaS built on Go Micro.