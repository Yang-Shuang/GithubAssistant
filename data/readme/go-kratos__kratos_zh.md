<p align="center"><a href="https://go-kratos.dev/" target="_blank"><img src="https://github.com/go-kratos/kratos/blob/main/docs/images/kratos-large.png?raw=true"></a></p>

<p align="center">
<a href="https://github.com/go-kratos/kratos/actions"><img src="https://github.com/go-kratos/kratos/workflows/Go/badge.svg" alt="Build Status"></a>
<a href="https://pkg.go.dev/github.com/go-kratos/kratos/v3"><img src="https://pkg.go.dev/badge/github.com/go-kratos/kratos/v3" alt="GoDoc"></a>
<a href="https://deepwiki.com/go-kratos/kratos"><img src="https://img.shields.io/badge/DeepWiki-go--kratos%2Fkratos-blue.svg" alt="DeepWiki"></a>
<a href="https://codecov.io/gh/go-kratos/kratos"><img src="https://codecov.io/gh/go-kratos/kratos/master/graph/badge.svg" alt="codeCov"></a>
<a href="https://goreportcard.com/report/github.com/go-kratos/kratos"><img src="https://goreportcard.com/badge/github.com/go-kratos/kratos" alt="Go Report Card"></a>
<a href="https://github.com/go-kratos/kratos/blob/main/LICENSE"><img src="https://img.shields.io/github/license/go-kratos/kratos" alt="License"></a>
<a href="https://github.com/avelino/awesome-go"><img src="https://awesome.re/mentioned-badge.svg" alt="Awesome Go"></a>
<a href="https://discord.gg/BWzJsUJ"><img src="https://img.shields.io/discord/766619759214854164?label=chat&logo=discord" alt="Discord"></a>
</p>

<p align="center">
<a href="https://trendshift.io/repositories/3233" target="_blank"><img src="https://trendshift.io/api/badge/repositories/3233" alt="go-kratos%2Fkratos | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"></a>
<a href="https://www.producthunt.com/posts/go-kratos?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-go-kratos" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=306565&theme=light" alt="Go Kratos - A Go framework for microservices. | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54"></a>
</p>

Translations: [English](README.md) | [简体中文](README_zh.md)

# Kratos

Kratos 是一款用于构建云原生微服务的轻量级 Go 框架。它提供了简洁、明确的传输（transport）、中间件（middleware）、注册中心（registry）、配置管理（configuration）、日志记录（logging）、数据编码（encoding）及代码生成 API，使应用程序能够专注于业务逻辑。

## Features

- 基于 Protobuf 的 API 优先开发，自动生成 HTTP/gRPC 代码。
- 统一的 [传输](https://go-kratos.dev/docs/component/transport/overview) 层，支持 [HTTP](https://go-kratos.dev/docs/component/transport/http) 和 [gRPC](https://go-kratos.dev/docs/component/transport/grpc)。
- 可组合的 [中间件](https://go-kratos.dev/docs/component/middleware/overview)，涵盖服务恢复、日志记录、参数校验、链路追踪、指标监控、身份认证等。
- 即插即用的 [注册中心](https://go-kratos.dev/docs/component/registry)、[配置管理](https://go-kratos.dev/docs/component/config) 和 [数据编码](https://go-kratos.dev/docs/component/encoding) 组件。
- 基于标准库 `log/slog` 的日志系统，并在 contrib 包中提供 OpenTelemetry 扩展支持。
- 统一的数据元（metadata）、错误处理、参数校验、OpenAPI 及代码生成工作流。
- 丰富的 contrib 生态系统，提供注册中心、配置存储、中间件、编码方案及可观测性等可选集成。

## Installation

### Requirements

- [Go](https://go.dev/dl/) 1.25 或更高版本
- [protoc](https://github.com/protocolbuffers/protobuf)
- [protoc-gen-go](https://github.com/protocolbuffers/protobuf-go)

### Install the CLI

```shell
go install github.com/go-kratos/kratos/cmd/kratos/v3@latest
kratos upgrade
```

## Create a Service

```shell
kratos new helloworld
cd helloworld
go mod tidy
kratos run
```

服务启动后，访问 `http://localhost:8000/helloworld/kratos`。

如需生成更完整的服务流程：

```shell
kratos proto add api/helloworld/helloworld.proto
kratos proto client api/helloworld/helloworld.proto
kratos proto server api/helloworld/helloworld.proto -t internal/service
go generate ./...
kratos run
```

## Usage Example

```go
package main

import (
	"github.com/go-kratos/kratos/v3"
	"github.com/go-kratos/kratos/v3/transport/grpc"
	"github.com/go-kratos/kratos/v3/transport/http"
)

func main() {
	httpSrv := http.NewServer(http.Address(":8000"))
	grpcSrv := grpc.NewServer(grpc.Address(":9000"))

	app := kratos.New(
		kratos.Name("helloworld"),
		kratos.Version("v1.0.0"),
		kratos.Server(httpSrv, grpcSrv),
	)
	if err := app.Run(); err != nil {
		panic(err)
	}
}
```

## v3 Migration

Kratos v3 精简了核心依赖，并将以往隐式的行为显式化。在升级生产环境服务前，请查阅 [v2 到 v3 迁移指南](docs/migration/v2-to-v3.md)。

## Further Reading

- [官方文档](https://go-kratos.dev/docs/getting-started/start)
- [示例项目](https://github.com/go-kratos/examples)
- [项目布局规范](https://github.com/go-kratos/kratos-layout)
- [v2 到 v3 迁移指南](docs/migration/v2-to-v3.md)
- [社区贡献指南](https://go-kratos.dev/docs/community/contribution)

## Development

```shell
make test
make lint
```

## Community

- [官方文档](https://go-kratos.dev/en)
- [微信群](https://github.com/go-kratos/kratos/issues/682)
- [Discord 频道](https://discord.gg/BWzJsUJ)
- [讨论区](https://github.com/go-kratos/kratos/discussions)

## Security

如果您发现 Kratos 存在安全漏洞，请联系 go-kratos@googlegroups.com。所有安全报告将在公开前进行保密处理。

## Contributors

感谢为 Kratos 做出贡献的每一位开发者。贡献指南详见 [Kratos 官方文档](https://go-kratos.dev/docs/community/contribution)。

<a href="https://github.com/go-kratos/kratos/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=go-kratos/kratos" alt="Kratos contributors">
</a>

## Acknowledgments

以下项目的设计对 Kratos 产生了影响：

- [go-kit/kit](https://github.com/go-kit/kit)
- [go-micro](https://github.com/asim/go-micro)
- [google/go-cloud](https://github.com/google/go-cloud)
- [go-zero](https://github.com/zeromicro/go-zero)
- [beego](https://github.com/beego/beego)

## License

Kratos 是基于 [MIT license](./LICENSE) 开源的软件。