<div align="center">
  <a href="https://casdoor.ai">
    <img src="https://cdn.casbin.org/img/casdoor-logo_1185x256.png" alt="Casdoor" width="500">
  </a>

  <h3>Casdoor：面向 AI 的身份与访问管理（IAM）/ AI MCP 网关</h3>

  <p align="center">
    <strong>一款开源的、以 AI 优先的 IAM / MCP 网关及认证服务器，配备 Web 界面。</strong><br>
    支持 MCP、A2A、OAuth&nbsp;2.0、OIDC（OAuth&nbsp;2.x）、SAML、CAS、LDAP、SCIM、WebAuthn、TOTP、MFA、Face ID、<br>
    Google Workspace、Azure AD 等。
  </p>

  <p align="center">
    <a href="https://casdoor.ai/"><strong>文档与指南：casdoor.ai</strong></a>
  </p>

  <p>
    <a href="https://casdoor.ai/docs/overview">
      <img src="https://img.shields.io/badge/documentation-casdoor.ai%2Fdocs-1890ff?style=flat-square&logo=readthedocs&logoColor=white" alt="Documentation">
    </a>
    <a href="https://github.com/casdoor/casdoor/releases/latest">
      <img src="https://img.shields.io/github/v/release/casdoor/casdoor?style=flat-square&color=blue" alt="GitHub Release">
    </a>
    <a href="https://hub.docker.com/r/casbin/casdoor">
      <img src="https://img.shields.io/docker/pulls/casbin/casdoor?style=flat-square&color=brightgreen" alt="Docker Pulls">
    </a>
    <a href="https://github.com/casdoor/casdoor/actions/workflows/build.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/casdoor/casdoor/build.yml?style=flat-square&label=build" alt="Build Status">
    </a>
    <a href="https://goreportcard.com/report/github.com/casdoor/casdoor">
      <img src="https://img.shields.io/badge/go-report-card-casbin.org-1890ff?style=flat-square" alt="Go Report Card">
    </a>
    <a href="https://github.com/casdoor/casdoor/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/casdoor/casdoor?style=flat-square&color=orange" alt="License">
    </a>
  </p>

  <p>
    <a href="https://github.com/casdoor/casdoor/stargazers">
      <img src="https://img.shields.io/github/stars/casdoor/casdoor?style=flat-square&color=yellow" alt="GitHub Stars">
    </a>
    <a href="https://github.com/casdoor/casdoor/network/members">
      <img src="https://img.shields.io/github/forks/casdoor/casdoor?style=flat-square" alt="GitHub Forks">
    </a>
    <a href="https://github.com/casdoor/casdoor/issues">
      <img src="https://img.shields.io/github/issues/casdoor/casdoor?style=flat-square&color=red" alt="GitHub Issues">
    </a>
    <a href="https://discord.gg/5rPsrAzK7S">
      <img src="https://img.shields.io/discord/1022748306096537660?style=flat-square&logo=discord&label=Discord&color=5865F2" alt="Discord">
    </a>
    <a href="https://crowdin.com/project/casdoor-site">
      <img src="https://badges.crowdin.net/casdoor-site/localized.svg" alt="Crowdin">
    </a>
  </p>

  <p align="center">
    <a href="https://casdoor.ai"><strong>官网</strong></a> ·
    <a href="https://casdoor.ai/docs/overview"><strong>文档中心</strong></a> ·
    <a href="https://door.casdoor.com"><strong>在线演示</strong></a> ·
    <a href="https://discord.gg/5rPsrAzK7S"><strong>Discord 社区</strong></a>
  </p>
</div>

---

## 目录

- [为什么选择 Casdoor](#why-casdoor)
- [在线演示](#live-demos)
- [快速开始](#quick-start)
- [功能特性](#features)
- [技术栈](#technology-stack)
- [文档中心](#documentation)
- [集成生态](#integrations)
- [社区与支持](#community-and-support)
- [贡献指南](#contributing)
- [捐赠支持](#donate)
- [开源协议](#license)

---

<a id="why-casdoor"></a>
## 为什么选择 Casdoor

Casdoor 是一款**以界面优先（UI-first）**的身份提供商与访问管理平台：在一个现代化的 Web 控制台中统一管理用户、组织、应用和身份提供者。授权策略可通过 **[Casbin](https://casbin.org/)**（ACL、RBAC、ABAC 等）进行表达。与以反向代理为核心的认证辅助工具不同，Casdoor 是一款专用的认证服务器，支持广泛的协议，旨在简化自建部署与集成流程——详细文档请访问 **[casdoor.ai](https://casdoor.ai)**。

---

<a id="live-demos"></a>
## 🌐 在线演示

| 环境 | 链接 | 说明 |
|-------------|-----|-------------|
| **只读模式** | [door.casdoor.com](https://door.casdoor.com) | 全球公共演示；**任何修改或写入操作均会失败**（仅支持读取）。 |
| **可写模式** | [demo.casdoor.com](https://demo.casdoor.com) | 测试用完整权限访问；**数据约每 5 分钟重置一次**。 |

默认演示管理员登录信息（如适用）：`admin` / `123` —— 仅限用于演示；请在自行部署时修改凭据。

---

<a id="quick-start"></a>
## 🚀 快速开始

请选择下方一种部署方式。为保持与上游版本行为一致，操作步骤已对齐官方文档。

### 🛠️ 源码部署（默认）

1. 安装依赖：**Go 1.25**（参考 `go.mod`）、**Node.js LTS (20)**、**Yarn 1.x**，以及受支持的数据库。
2. 克隆代码仓库：

```bash
git clone https://github.com/casdoor/casdoor.git
cd casdoor
```

3. 在 `conf/app.conf` 中配置数据库（至少设置 `driverName`、`dataSourceName` 和 `dbName`；若使用 MySQL，请先创建名为 `casdoor` 的数据库）。
4. 构建前端并启动后端：

```bash
cd web
yarn install
yarn build
cd ..
go run main.go
```

5. 访问 [http://localhost:8000](http://localhost:8000)，在全新安装环境下使用 `built-in/admin` / `123` 登录（生产环境请立即修改密码）。

官方指南：[服务器安装](https://casdoor.ai/docs/basic/server-installation)

### 🐳 Docker 部署

使用以下任一官方 Docker 方案：

- **一体化镜像（SQLite 快速试用）**：

```bash
docker run -p 8000:8000 casbin/casdoor-all-in-one
```

- **Docker Compose**（将你的 `conf/app.conf` 与 `docker-compose.yml` 放在同级目录）：

```bash
docker compose up
```

随后访问 [http://localhost:8000](http://localhost:8000)，在全新安装环境下使用 `built-in/admin` / `123` 登录。

官方指南：[Docker 试用](https://casdoor.ai/docs/basic/try-with-docker)

### ☸️ Kubernetes Helm 部署

需具备 Helm v3 及运行中的 Kubernetes 集群：

```bash
helm install casdoor oci://registry-1.docker.io/casbin/casdoor-helm-charts
```

安装完成后，通过集群的 Service 或 Ingress 访问 Casdoor。官方指南涵盖了 Chart 版本说明（含可选的 `--version` 参数）及针对特定集群的配置项。

官方指南：[Helm 试用](https://casdoor.ai/docs/basic/try-with-helm)

---

<a id="features"></a>
## ✨ 功能特性

<table>
<tr>
<td width="50%">

### 🔐 身份认证

- **OAuth 2.0 / OIDC** —— OpenID Connect 与 OAuth 2.x 授权
- **SAML 2.0** —— 企业单点登录（SSO）集成
- **CAS** —— 集中认证服务
- **LDAP** —— 目录服务协议集成
- **WebAuthn / Passkeys（通行密钥）** —— 无密码认证
- **TOTP / MFA** —— 多因素认证
- **Face ID** —— 生物识别认证

</td>
<td width="50%">

### 🏢 企业级功能

- **SCIM 2.0** —— 用户配置与管理
- **RBAC** —— 基于角色的访问控制
- **社交登录** —— 支持 Google、GitHub、Azure AD 等
- **自定义提供商** —— 可扩展的身份提供者
- **用户管理** —— 提供 Web 界面进行管理
- **审计日志** —— 全面的操作记录
- **多租户** —— 完善的组织支持

</td>
</tr>
<tr>
<td width="50%">

### 🤖 AI 与 MCP

- **MCP 网关** —— 支持模型上下文协议（Model Context Protocol）
- **A2A 协议** —— 智能体间通信（Agent-to-Agent）
- **AI 优先设计** —— 专为 AI 应用打造

</td>
<td width="50%">

### 🛠️ 开发者体验

- **RESTful API** —— 完整的 API 覆盖
- **多语言 SDK** —— 支持 Go、Java、Python、Node.js 等
- **Swagger UI** —— 交互式 API 文档
- **Webhook** —— 事件驱动集成
- **可定制界面** —— 支持品牌主题定制

</td>
</tr>
</table>

---

<a id="technology-stack"></a>
## 技术栈

Casdoor 采用**前后端分离**架构构建：

- **前端界面**：JavaScript 与 **React**（[`web/`](https://github.com/casdoor/casdoor/tree/master/web)）
- **API 服务**：**Go** 语言结合 **Beego** 框架，提供 RESTful API（[项目根目录](https://github.com/casdoor/casdoor)）
- **数据存储**：支持主流数据库，包括 **MySQL**、**PostgreSQL** 等（[概览](https://casdoor.ai/docs/overview)）
- **缓存服务**：可选 **Redis**，用于会话或缓存型部署（按需配置）

---

<a id="documentation"></a>
## 📖 文档中心

**所有产品文档、安装指南与教程均托管于 [casdoor.ai/docs/overview](https://casdoor.ai/docs/overview)。** 请从此处开始阅读，随后参考下方分类。

**安装部署**

- [从源码安装](https://casdoor.ai/docs/basic/server-installation)
- [使用 Docker 安装](https://casdoor.ai/docs/basic/try-with-docker)
- [使用 Kubernetes Helm 安装](https://casdoor.ai/docs/basic/try-with-helm)

**接入应用**

- [如何接入 Casdoor](https://casdoor.ai/docs/how-to-connect/overview)

**接口文档**

- [公开 API](https://casdoor.ai/docs/basic/public-api)
- [Swagger UI](https://door.casdoor.com/swagger)（在线 API 调试台）

---

<a id="integrations"></a>
## 🔌 集成生态

Casdoor 支持与主流编程语言及框架无缝集成：

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="40" alt="Go">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="40" alt="Java">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" alt="Python">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" width="40" alt="Node.js">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" width="40" alt="React">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" width="40" alt="Vue">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angularjs/angularjs-original.svg" width="40" alt="Angular">
</p>

查看完整列表：[集成生态](https://casdoor.ai/docs/category/integrations)。

---

<a id="community-and-support"></a>
## 🤝 社区与支持

- **Discord**：[加入我们的社区](https://discord.gg/5rPsrAzK7S)
- **联系我们**：[casdoor.ai/help](https://casdoor.ai/help)
- **问题反馈**：[GitHub Issues](https://github.com/casdoor/casdoor/issues)
- **技术讨论**：[GitHub Discussions](https://github.com/casdoor/casdoor/discussions)

---

<a id="contributing"></a>
## 🌍 贡献指南

如果你有关于 Casdoor 的疑问，可以 **[提交 Issue](https://github.com/casdoor/casdoor/issues)**。我们欢迎所有 Pull Request；**建议在发起较大改动前先创建 Issue**，以便与维护者及社区对齐方案。

贡献前请阅读我们的[贡献指南](https://casdoor.ai/docs/contributing/)。

### 翻译与国际化（i18n）

- 翻译工作流使用 **Crowdin**：[Casdoor 站点翻译页](https://crowdin.com/project/casdoor-site)。
- 前端应用使用 **i18next** 进行国际化。当你在 [`web/`](https://github.com/casdoor/casdoor/tree/master/web) 目录下新增或修改面向用户的文本时，请同步更新 [`web/src/locales/en/data.json`](web/src/locales/en/data.json) 中的英文词条。

---

<a id="donate"></a>
## ❤️ 捐赠支持

如果你觉得 Casdoor 有用，欢迎考虑资助其开发：

<a href="https://opencollective.com/casdoor#sponsor"><img src="https://opencollective.com/casdoor/tiers/sponsor.svg?avatarHeight=74" alt="Sponsors on Open Collective"></a>

<a href="https://opencollective.com/casdoor#backer"><img src="https://opencollective.com/casdoor/tiers/backer.svg?avatarHeight=36" alt="Backers on Open Collective"></a>

---

<a id="license"></a>
## 📄 开源协议

Casdoor 采用 [Apache License 2.0](https://github.com/casdoor/casdoor/blob/master/LICENSE) 开源协议。

---

<div align="center">

[![Made with ❤️](https://img.shields.io/badge/Made_with-%E2%9D%A4%EF%B8%8F-ff6b6b?style=flat-square&logoColor=white)](https://casdoor.ai) [![By Casdoor](https://img.shields.io/badge/by-Casdoor-4ecdc4?style=flat-square)](https://casdoor.ai)

<a href="https://github.com/casdoor/casdoor/stargazers"><img src="https://img.shields.io/github/stars/casdoor/casdoor?style=social&logo=github&label=Star" alt="GitHub Stars"></a>

<sub>© 2026 <a href="https://casdoor.ai">Casdoor</a>。采用 <a href="https://github.com/casdoor/casdoor/blob/master/LICENSE">Apache License 2.0</a> 协议授权。</sub>

</div>