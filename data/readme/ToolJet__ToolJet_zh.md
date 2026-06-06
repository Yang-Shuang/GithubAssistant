ToolJet 是一个**开源低代码（low-code）框架**，旨在以最小的工程投入构建和部署内部工具。ToolJet 的拖拽式前端生成器让你能够在几分钟内创建复杂、响应式的界面。此外，你还可以集成各种数据源，包括 PostgreSQL、MongoDB 和 Elasticsearch 等数据库；支持 OpenAPI 规范和 OAuth2 认证的 API 端点；Stripe、Slack、Google Sheets、Airtable 和 Notion 等 SaaS 工具；以及 S3、GCS 和 Minio 等对象存储服务，用于读取和写入数据。

 :star: 如果你觉得 ToolJet 有用，请在 GitHub 上给我们点个 Star！你的支持将帮助我们持续创新并交付令人兴奋的功能。

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/tooljet/tooljet-ce)
![Number of GitHub contributors](https://img.shields.io/github/contributors/tooljet/tooljet)
[![Number of GitHub issues that are open](https://img.shields.io/github/issues/ToolJet/ToolJet)](https://github.com/ToolJet/ToolJet/issues)
[![Number of GitHub stars](https://img.shields.io/github/stars/ToolJet/ToolJet)](https://github.com/ToolJet/ToolJet/stargazers)
![Number of GitHub closed issues](https://img.shields.io/github/issues-closed/tooljet/tooljet)
![Number of GitHub pull requests that are open](https://img.shields.io/github/issues-pr-raw/tooljet/tooljet)
![GitHub release; latest by date](https://img.shields.io/github/v/release/tooljet/tooljet)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/tooljet/tooljet)
[![GitHub license which is AGPL license](https://img.shields.io/github/license/ToolJet/ToolJet)](https://github.com/ToolJet/ToolJet)
[![Follow us on X, formerly Twitter](https://img.shields.io/twitter/follow/ToolJet?style=social)](https://twitter.com/ToolJet)

<p align="center">
    <img src="https://user.githubusercontent.com/7828962/211444352-4d6d2e4a-13c9-4980-9e16-4aed4af9811b.png" alt="Tooljet dashboard showing inventory and orders"/>
</p>

<p align="center">
    <img src="https://github.com/ToolJet/ToolJet/assets/25361949/0e711f3a-edb7-496b-8833-107de3826933"/>
</p>

## 所有功能

- **可视化应用构建器：**内置 45 多种响应式组件，包括表格、图表、列表、表单和进度条。
- **ToolJet 数据库：**内置无代码（no-code）数据库。
- **多页面支持：**构建包含多个页面的应用。
- **多人协作编辑：**允许多名开发者同时构建应用。
- **50+ 数据源：**集成外部数据库、云存储和 API。
- **桌面端与移动端：**自定义布局宽度以适配不同屏幕尺寸。
- **自托管（self-host）：**支持 Docker、Kubernetes、AWS EC2、Google Cloud Run 等部署方式。
- **团队协作：**在画布任意位置添加评论，并 @ 团队成员。
- **通过插件扩展：**使用我们的 [命令行工具](https://www.npmjs.com/package/@tooljet/cli) 轻松创建新的连接器。
- **版本控制：**通过结构化的发布周期管理多个应用版本。
- **运行 JS 与 Python 代码：**执行自定义的 JavaScript 和 Python 片段。
- **细粒度访问控制：**在组和应用级别设置权限（permission）。
- **低代码开发：**在构建器中几乎任何地方都可以使用 JS 代码，例如通过 `status === 'success' ? 'green' : 'red'` 根据状态设置文本颜色。
- **无代码查询编辑器：**所有支持的数据源均提供查询编辑器（Query Editor）。
- **数据关联与转换：**使用 JavaScript 或 Python 代码转换查询结果。
- **安全可靠：**所有凭据（credentials）均通过 `aes-256-gcm` 进行安全加密。
- **数据隐私保护：**ToolJet 仅作为代理使用，不存储任何数据。
- **单点登录（SSO）：**支持多种 SSO 提供商。

<hr>

## 快速入门
使用 ToolJet 最简单的方式是注册一个 [ToolJet Cloud](https://tooljet.com) 账号。ToolJet Cloud 提供托管解决方案。如果你想自托管（self-host）ToolJet，请参阅[部署文档](https://docs.tooljet.com/docs/setup/)。

### 使用 Docker 体验
想在本机快速跑一下 ToolJet？你可以在终端中运行以下命令，立即启动并运行 ToolJet。


```bash
docker run \
  --name tooljet \
  --restart unless-stopped \
  -p 80:80 \
  --platform linux/amd64 \
  -v tooljet_data:/var/lib/postgresql/13/main \
  tooljet/try:ee-lts-latest
```

*对于升级 ToolJet 版本的用户，我们建议选择 LTS（长期支持）版本而非最新版。LTS 版本通过生产环境 Bug 修复、安全补丁和性能优化确保稳定性。*

## 教程与示例

[时间追踪应用](https://docs.tooljet.com/docs/#quickstart-guide)<br>
[使用低代码构建你自己的 CMS](https://blog.tooljet.com/build-cms-using-lowcode-and-mongodb/)<br>
[AWS S3 浏览器](https://blog.tooljet.com/build-an-aws-s3-broswer-with-tooljet/)

## 文档
官方文档位于 https://docs.tooljet.com。

- [快速开始](https://docs.tooljet.com)<br>
- [数据源参考](https://docs.tooljet.com/docs/data-sources/airtable/)<br>
- [组件参考](https://docs.tooljet.com/docs/widgets/button)

## 自托管部署
你可以使用 ToolJet Cloud 获得完全托管的解决方案。如果你想自托管（self-host）ToolJet，我们提供了在 Kubernetes、AWS EC2、Docker 等平台上部署 ToolJet 指南。

| 平台/提供商      | 文档链接                                                                                         |
| :-------------   | :--------------------------------------------------------------------------------------------- |
| Digital Ocean    | [Link](https://docs.tooljet.com/docs/setup/digitalocean)                                         |
| Docker           | [Link](https://docs.tooljet.com/docs/setup/docker)                                               |
| AWS EC2          | [Link](https://docs.tooljet.com/docs/setup/ec2)                                                  |
| AWS ECS          | [Link](https://docs.tooljet.com/docs/setup/ecs)                                                  |
| OpenShift        | [Link](https://docs.tooljet.com/docs/setup/openshift)                                            |
| Helm             | [Link](https://docs.tooljet.com/docs/setup/helm)                                                 |
| AWS EKS (Kubernetes) | [Link](https://docs.tooljet.com/docs/setup/kubernetes)                                       |
| GCP GKE (Kubernetes) | [Link](https://docs.tooljet.com/docs/setup/kubernetes-gke)                                   |
| Azure AKS (Kubernetes) | [Link](https://docs.tooljet.com/docs/setup/kubernetes-aks)                                 |
| Azure Container  | [Link](https://docs.tooljet.com/docs/setup/azure-container)                                      |
| Google Cloud Run | [Link](https://docs.tooljet.com/docs/setup/google-cloud-run)                                     |
| Deploying ToolJet client | [Link](https://docs.tooljet.com/docs/setup/client)                                       |
| Deploying ToolJet on a Subpath   | [Link](https://docs.tooljet.com/docs/setup/tooljet-subpath/)                                 |

## 市场平台 
ToolJet 现已上架 AWS 和 Azure 市场，让你比以往更轻松地访问和部署我们的应用构建平台。

你可以在这里找到 AWS 市场上的 ToolJet：[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-fxjto27jkpqfg?sr=0-1&ref_=beagle&applicationId=AWSMPContessa)，并在此探索 Azure 市场的无缝集成体验：[Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/tooljetsolutioninc1679496832216.tooljet?tab=Overview)。

## 社区支持
如需一般性帮助，请参阅官方 [文档](https://docs.tooljet.com/docs/)。如需更多帮助，你可以通过以下渠道提问：

- [Slack](https://tooljet.com/slack) - 与社区及团队交流讨论。
- [GitHub Issues](https://github.com/ToolJet/ToolJet/issues) - 提交 Bug 报告和功能请求。
- [𝕏 (Twitter)](https://twitter.com/ToolJet) - 快速获取产品更新动态。

## 路线图
查看我们的 [路线图](https://github.com/orgs/ToolJet/projects/15)，了解近期发布的功能以及未来的开发计划。

## 分支模型
我们采用 git-flow 分支模型。基础分支为 `develop`。如需稳定版本，请使用 `main` 分支或标记为 v1.x.x 的标签（tags）。

## 贡献指南
请阅读我们的 [贡献指南](CONTRIBUTING.md)，了解 ToolJet 的开发流程、如何提交 Bug 修复与改进建议，以及构建和测试代码变更的步骤。<br>

## Contributors
<a href="https://github.com/tooljet/tooljet/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tooljet/tooljet&max=400&columns=20" />
  <img src="https://us-central1-tooljet-hub.cloudfunctions.net/github" width="0" height="0" />
</a>

## License
ToolJet © 2023, ToolJet Solutions Inc - 根据 GNU Affero General Public License v3.0（AGPL）开源协议发布。