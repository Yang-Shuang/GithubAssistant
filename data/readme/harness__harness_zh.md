# Harness
Harness Open Source 是一个开源开发平台，集成了代码托管、自动化 DevOps 流水线、托管式开发环境（Gitspaces）以及制品库的强大功能。

## 概述
Harness Open Source 是一个开源开发平台，集成了代码托管、自动化 DevOps 流水线、Gitspaces 以及制品库的强大功能。


## 本地运行 Harness
> 最新的公开 Docker 镜像可在 [harness/harness](https://hub.docker.com/r/harness/harness) 上找到。

若要自行安装 Harness，只需运行以下命令。容器启动后，你可以在浏览器中访问 http://localhost:3000。

```bash
docker run -d \
  -p 3000:3000 \
  -p 3022:3022 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp/harness:/data \
  --name harness \
  --restart always \
  harness/harness
```
> Harness 镜像使用数据卷来存储数据库和代码仓库。强烈建议使用绑定挂载（bind mount）或命名卷，否则容器停止后所有数据将会丢失。

请参阅 [developer.harness.io](https://developer.harness.io/docs/open-source)，了解如何充分利用 Harness。

## Drone 在哪里？

Harness Open Source 代表了我们对下一代 Drone 的重大投入。Drone 最初仅专注于持续集成（CI），而 Harness 在此基础上增加了源代码托管、开发者环境（Gitspaces）和制品库，为团队提供了一个端到端的开源 DevOps 平台。

我们的目标是让 Harness 在流水线功能上最终与 Drone 完全持平，以便用户能够无缝地从 Drone 迁移到 Harness。

但这需要一定时间，因此我们将 Drone 的当前状态作为功能分支 [drone](https://github.com/harness/harness/tree/drone)（[README](https://github.com/harness/harness/blob/drone/.github/readme.md)）保留下来，以便其继续开发。

至于 Harness，其开发工作主要在 [main](https://github.com/harness/harness/tree/main) 分支上进行。

如需了解更多关于 Harness 的信息，请访问 [developer.harness.io](https://developer.harness.io/)。

如需了解更多关于 Drone 的信息，请访问 [drone.io](https://www.drone.io/)。

## Harness 开源开发指南
### 前置条件

安装最新稳定版的 Node.js 和 Go（版本 1.20 或更高），然后安装以下 Go 程序。请确保将 GOPATH 的 [bin 目录](https://go.dev/doc/gopath_code#GOPATH) 添加到你的 `PATH` 环境变量中。

安装 protobuf：
- 检查是否已安装 protobuf ```protoc --version```
- 如果版本不是 v3.21.11，请运行 ```brew unlink protobuf```
- 获取 v3.21.11 ```curl -s https://raw.githubusercontent.com/Homebrew/homebrew-core/9de8de7a533609ebfded833480c1f7c05a3448cb/Formula/protobuf.rb > /tmp/protobuf.rb```
- 安装它 ```brew install /tmp/protobuf.rb```
- 检查你的版本 ```protoc --version```

安装 protoc-gen-go 和 protoc-gen-go-grpc：

- 安装 protoc-gen-go v1.28.1 ```go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28.1```（注意：这将在 `$GOBIN` 目录下生成二进制文件，请确保 `$GOBIN` 已包含在你的 `$PATH` 中）

- 安装 protoc-gen-go-grpc v1.2.0 ```go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2.0```

```bash
$ make dep
$ make tools
```

### 构建

第一步是构建用户界面相关资源：

```bash
$ pushd web
$ yarn install
$ yarn build
$ popd
```

之后，你可以编译 Harness 的二进制文件：

```bash
$ make build
```

### 运行

本项目支持 Go 所支持的所有操作系统和架构。这意味着你可以在本地机器上构建并运行该系统；本地开发和测试无需依赖 Docker 容器。

要在 `localhost:3000` 启动服务器，只需运行以下命令：

```bash
./gitness server .local.env
```

### 流水线 Docker 配置

Harness 的流水线在 Docker 容器中运行。该应用会自动与你的 Docker 守护进程协商 Docker API 版本，因此它兼容多种 Docker 环境，包括 Docker Desktop、Rancher Desktop、Colima 以及 Linux 原生 Docker。

**Docker Socket 位置**

默认情况下，Harness 期望在 `/var/run/docker.sock` 找到 Docker socket。如果你使用的是其他 Docker 运行时环境，可能需要配置 socket 的位置：

| Runtime | Socket Location | Configuration |
|---------|-----------------|---------------|
| Docker Desktop | `/var/run/docker.sock` | Works by default |
| Rancher Desktop | `~/.rd/docker.sock` | Create symlink or set `GITNESS_DOCKER_HOST` |
| Colima | `~/.colima/default/docker.sock` | Create symlink or set `GITNESS_DOCKER_HOST` |
| Linux (native) | `/var/run/docker.sock` | Works by default |

**方案一：创建软链接（推荐）**
```bash
# For Rancher Desktop
sudo ln -sf ~/.rd/docker.sock /var/run/docker.sock

# For Colima
sudo ln -sf ~/.colima/default/docker.sock /var/run/docker.sock
```

**方案二：设置环境变量**

将其添加到你的 `.local.env` 文件中：
```bash
# For Rancher Desktop
GITNESS_DOCKER_HOST=unix:///Users/<username>/.rd/docker.sock

# For Colima
GITNESS_DOCKER_HOST=unix:///Users/<username>/.colima/default/docker.sock
```

**固定 Docker API 版本**

应用会自动与你的 Docker 守护进程协商 API 版本。如果你需要固定某个特定版本（例如用于兼容性测试），可以设置：
```bash
GITNESS_DOCKER_API_VERSION=1.45
```

### 使用 Swagger 自动生成 UI 使用的 Harness API 客户端
在添加新的 REST API 时，请确保更新 UI 所使用的自动生成的客户端代码。

要重新生成代码，请按以下步骤操作：
- 使用最新的 Harness 二进制文件重新生成 Swagger `./gitness swagger > web/src/services/code/swagger.yaml`
- 进入 `web` 文件夹并运行 `yarn services`

最新的 API 变更现在应已反映在 `web/src/services/code/index.tsx` 中。

# Run Registry Conformance Tests
```
make conformance-test
```
For running conformance tests with existing running service, use:
```
make hot-conformance-test
```

## User Interface

This project includes a full user interface for interacting with the system. When you run the application, you can access the user interface by navigating to `http://localhost:3000` in your browser.

## REST API

This project includes a swagger specification. When you run the application, you can access the swagger specification by navigating to `http://localhost:3000/swagger` in your browser (for raw yaml see `http://localhost:3000/openapi.yaml`).
For registry endpoints, currently swagger is located on different endpoint `http://localhost:3000/registry/swagger/` (for raw json see `http://localhost:3000/registry/swagger.json`). These will be later moved to the main swagger endpoint. 


For testing, it's simplest to just use the cli to create a token (this requires Harness server to run):
```bash
# LOGIN (user: admin, pw: changeit)
$ ./gitness login

# GENERATE PAT (1 YEAR VALIDITY)
$ ./gitness user pat "my-pat-uid" 2592000
```

The command outputs a valid PAT that has been granted full access as the user.
The token can then be send as part of the `Authorization` header with Postman or curl:

```bash
$ curl http://localhost:3000/api/v1/user \
-H "Authorization: Bearer $TOKEN"
```


## CLI
This project includes VERY basic command line tools for development and running the service. Please remember that you must start the server before you can execute commands.

For a full list of supported operations, please see
```bash
$ ./gitness --help
```

## Contributing

Refer to [CONTRIBUTING.md](https://github.com/harness/harness/blob/main/CONTRIBUTING.md)

## License

Apache License 2.0, see [LICENSE](https://github.com/harness/harness/blob/main/LICENSE).