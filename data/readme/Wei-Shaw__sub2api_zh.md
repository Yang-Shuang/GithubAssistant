# Sub2API

<div align="center">

[![Go](https://img.shields.io/badge/Go-1.25.7-00ADD8.svg)](https://golang.org/)
[![Vue](https://img.shields.io/badge/Vue-3.4+-4FC08D.svg)](https://vuejs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791.svg)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7+-DC382D.svg)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)

<a href="https://trendshift.io/repositories/21823" target="_blank"><img src="https://trendshift.io/api/badge/repositories/21823" alt="Wei-Shaw%2Fsub2api | Trendshift" width="250" height="55"/></a>

**面向订阅配额分配的 AI API 网关平台**

English | [中文](README_CN.md) | [日本語](README_JA.md)

</div>

> **Sub2API 官方仅使用 `sub2api.org` 和 `pincc.ai` 两个域名。其他使用 Sub2API 名称的网站可能为第三方部署或服务，与本仓库无关。请自行核实并谨慎判断。**

---

## 在线演示

在线试用 Sub2API：**[https://demo.sub2api.org/](https://demo.sub2api.org/)**

演示账号（共享演示环境；自托管安装不会自动创建此账号）：

| 邮箱 | 密码 |
|-------|----------|
| admin@sub2api.org | admin123 |

## 项目概述

Sub2API 是一款面向订阅配额分配的 AI API 网关平台。用户可通过平台生成的 API Key（应用程序接口密钥）访问上游 AI 服务，平台负责处理身份验证、计费、负载均衡及请求转发。

## 核心功能

- **多账号管理** - 支持多种类型的上游账号（OAuth、API Key）
- **API Key 分发** - 为用户生成并管理 API Key
- **精准计费** - Token（词元）级用量追踪与成本计算
- **智能调度** - 支持粘性会话的智能账号选择策略
- **并发控制** - 支持按用户和按账号的并发限制
- **速率限制** - 可配置请求频率与 Token 消耗速率限制
- **内置支付系统** - 支持 EasyPay、支付宝、微信支付及 Stripe，实现用户自助充值，无需额外部署第三方支付服务（[配置指南](docs/PAYMENT.md)）
- **管理后台** - 提供用于监控与管理的 Web 界面
- **外部系统集成** - 通过 iframe 嵌入外部系统（如工单系统），扩展管理后台功能

## ❤️ 赞助支持

> [希望出现在这里？](mailto:support@pincc.ai)

<table>
<tr>
<td width="180" align="center" valign="middle"><a href="https://shop.pincc.ai/"><img src="assets/partners/logos/pincc-logo.png" alt="pincc" width="150"></a></td>
<td valign="middle"><b><a href="https://shop.pincc.ai/">PinCC</a></b> 是官方基于 Sub2API 构建的代理（Relay）服务，提供 Claude Code、Codex、Gemini 等热门模型的稳定访问通道——开箱即用，无需自行部署或维护。</td>
</tr>

<tr>
<td width="180"><a href="https://www.packyapi.com/register?aff=sub2api"><img src="assets/partners/logos/packycode.png" alt="PackyCode" width="150"></a></td>
<td>感谢 PackyCode 对本项目的赞助！PackyCode 是一家可靠高效的 API 代理服务提供商，提供 Claude Code、Codex、Gemini 等热门模型的代理支持。我们的软件用户可享受专属优惠：使用 <a href="https://www.packyapi.com/register?aff=sub2api">此链接</a> 注册，并在首次充值时输入促销码 "sub2api" 即可享受 10% 折扣。</td>
</tr>

<tr>
<td width="180"><a href="https://ctok.ai"><img src="assets/partners/logos/ctok.png" alt="CTok" width="150"></a></td>
<td>感谢 CTok.ai 对本项目的赞助！CTok.ai 致力于构建一站式 AI 编程工具服务平台。我们提供专业 Claude Code 套餐及技术支持社区，支持 Google Gemini 和 OpenAI Codex。通过精心设计的方案与专业的技术社区，我们为开发者提供可靠的服务保障与持续的技术支持，让 AI 辅助编程真正成为生产力工具。点击 <a href="https://ctok.ai">此处</a> 注册！</td>
</tr>

<tr>
<td width="180"><a href="https://aigocode.com/invite/SUB2API"><img src="assets/partners/logos/aigocode.png" alt="AIGoCode" width="150"></a></td>
<td>感谢 AIGoCode 对本项目的赞助！AIGoCode 是一个整合 Claude Code、Codex 及最新 Gemini 模型的一体化平台，为你提供稳定、高效且极具性价比的 AI 编程服务。平台提供灵活的订阅方案，账号零封禁风险，直连无需翻墙，响应速度极快。我们为 sub2api 用户准备了专属福利：通过 <a href="https://aigocode.com/invite/SUB2API">此链接</a> 注册，首次充值即可额外获得 10% 的赠金！</td>
</tr>

<tr>
<td width="180"><a href="https://apikey.fun/register?aff=SUB2API"><img src="assets/partners/logos/apikey-fun.png" alt="APIKEY.FUN" width="150"></a></td>
<td>感谢 APIKEY.FUN 对本项目的赞助！<a href="https://apikey.fun/register?aff=SUB2API">APIKEY.FUN</a> 是 sub2api 开源项目的核心贡献者之一，致力于提供开放、稳定且高性价比的 AI API 访问服务。平台支持 Claude、OpenAI、Gemini 等热门模型的 API 代理，价格低至原价的 7%。通过专属链接注册：<a href="https://apikey.fun/register?aff=SUB2API">APIKEY</a> 即可享受所有充值永久 5% 折扣。</td>
</tr>

<tr>
<td width="180"><a href="https://code.silkapi.com/register?aff=SUB2API"><img src="assets/partners/logos/silkapi.png" alt="silkapi" width="150"></a></td>
<td>感谢 SilkAPI 对本项目的赞助！<a href="https://code.silkapi.com/register?aff=SUB2API">SilkAPI</a> 是一款基于 Sub2API 构建的代理服务，专注于提供高速稳定的 Codex API 代理。</td>
</tr>

<tr>
<td width="180"><a href="https://ylscode.com/"><img src="assets/partners/logos/ylscode.png" alt="ylscode" width="150"></a></td>
<td>感谢 YLS Code 对本项目的赞助！<a href="https://ylscode.com/">YLS Code</a> 致力于构建安全的企业级 Coding Agent 生产力服务，提供稳定快速的 Codex / Claude / Gemini 订阅服务及按需付费 API 选项。立即注册即可领取限时 3 天 Codex 试用赠金！</td>
</tr>

<tr>
<td width="180"><a href="https://www.aicodemirror.com/register?invitecode=KMVZQM"><img src="assets/partners/logos/AICodeMirror.jpg" alt="AICodeMirror" width="150"></a></td>
<td>感谢 AICodeMirror 对本项目的赞助！AICodeMirror 提供 Claude Code / Codex / Gemini CLI 的官方高稳定性代理服务，具备企业级并发能力、快速开票及 24/7 专属技术支持。Claude Code / Codex / Gemini 官方渠道价格分别为原价的 38% / 2% / 9%，充值另有额外折扣！我们为 sub2api 用户提供专属福利：通过 <a href="https://www.aicodemirror.com/register?invitecode=KMVZQM">此链接</a> 注册，首次充值享 20% 折扣；企业客户最高可享 25% 优惠！</td>
</tr>

<tr>
<td width="180"><a href="https://shop.bmoplus.com/?utm_source=github"><img src="assets/partners/logos/bmoplus.jpg" alt="bmoplus" width="150"></a></td>
<td>特别感谢 BmoPlus 对本项目的赞助！BmoPlus 是专为重度 AI 用户与开发者打造的高可靠性 AI 账号提供商。他们提供开箱即用、稳定可靠的 ChatGPT Plus / ChatGPT Pro（全保修）/ Claude Pro / Super Grok / Gemini Pro 官方充值服务。通过 <a href="https://shop.bmoplus.com/?utm_source=github">BmoPlus - 高端 AI 账号与充值</a> 注册下单，用户可解锁令人惊叹的 GPT 订阅原价 10% 费率（90% OFF）。</td>
</tr>

<tr>
<td width="180"><a href="https://bestproxy.com/?keyword=a2e8iuol"><img src="assets/partners/logos/bestproxy.png" alt="bestproxy" width="150"></a></td>
<td>感谢 Bestproxy 对本项目的赞助！<a href="https://bestproxy.com/?keyword=a2e8iuol">Bestproxy</a> 提供高纯度住宅 IP，支持每账号独享单 IP。通过结合真实家庭网络与指纹隔离技术，实现链接环境隔离，有效降低基于关联的风控概率。</td>
</tr>

<tr>
<td width="180"><a href="https://pateway.ai/?ch=1tsfr51"><img src="assets/partners/logos/pateway.png" alt="pateway" width="150"></a></td>
<td>感谢 PatewayAI 对本项目的赞助！<a href="https://pateway.ai/?ch=1tsfr51">PatewayAI</a> 是一款专为重度 AI 开发者打造的高端 API 代理，提供 100% 源自官方供应商的完整 Claude 和 Codex 系列服务，支持透明的 Token 级计费。企业版计划包含高并发、专属管理、合同签署及发票开具功能。立即注册领取 $3 体验金，充值低至 6 折，推荐奖励最高可达 $150。</td>
</tr>

<tr>
<td width="180"><a href="https://api.pptoken.org/register?promo=SUB2API"><img src="assets/partners/logos/pptoken.png" alt="pptoken" width="150"></a></td>
<td>感谢 PPToken.org 对本项目的赞助！<a href="https://api.pptoken.org/register?promo=SUB2API">PPToken.org</a> 专注于 GPT 模型 API 代理服务，支持 Codex、Claude Code、OpenAI 兼容客户端及 Gemini CLI 集成。充值比例 1:1（¥1 = $1 额度）；GPT 模型起步倍率为 0.16x，整体成本约为官方定价的 2.2%，首 Token 延迟约 1 秒——非常适合寻求低成本、高速访问 GPT 模型能力的开发者。技术支持：7×24 小时真人响应（无机器人），在群内发送 @tech 即可 10 分钟内获得回复。赞助福利：通过 <a href="https://api.pptoken.org/register?promo=SUB2API">专属注册链接</a> 注册并输入促销码 `SUB2API` 的前 200 名用户，可领取免费的 Codex / Claude Code 体验额度——无需最低消费，无需绑定银行卡。</td>
</tr>

<tr>
<td width="180"><a href="https://runapi.co/register?aff=fu2E"><img src="assets/partners/logos/runapi.png" alt="RunAPI" width="150"></a></td>
<td>感谢 RunAPI 对本项目的赞助！<a href="https://runapi.co/register?aff=fu2E">RunAPI</a> 是一款高效稳定的 API 平台及 OpenRouter 替代方案。只需一个 API Key，即可访问包括 OpenAI、Claude、Gemini、DeepSeek 和 Grok 在内的 150+ 热门模型，价格低至原价的 10%。系统高度稳定，无缝兼容 Claude Code 与 OpenClaw 等工具。</td>
</tr>

<tr>
<td width="180"><a href="https://unity2.ai/register?source=sub2api"><img src="assets/partners/logos/unity2.png" alt="unity2" width="150"></a></td>
<td>感谢 Unity2 对本项目的赞助！<a href="https://unity2.ai/register?source=sub2api">Unity2</a> 是一款面向个人、团队及企业的高性能 AI 模型 API 代理，日处理 Token 量超 30B，并发能力达 5000 RPM。一个 API Key 即可在 Claude Code、Codex、OpenAI 模型、IDE 插件及 Agent 工作流中通用，支持余额计费、订阅捆绑、企业开票及一对一专属支持。<a href="https://unity2.ai/register?source=sub2api">注册</a> 领取 $2 余额，加入官方群再领 $10——最高可获得 $12 免费额度。</td>
</tr>

<tr>
<td width="180"><a href="https://veilx.io/#/hello/SJRBRVDV"><img src="assets/partners/logos/veilx.png" alt="veilx" width="150"></a></td>
<td>感谢 Veilx 对本项目的赞助！<a href="https://veilx.io/#/hello/SJRBRVDV">Veilx</a> CDN 专为大规模 AI API 流量设计，针对 OpenAI、Claude、Gemini 等跨平台代理及调用链进行深度优化，覆盖对话、图像生成、Embedding 及流式输出等场景——在高并发下实现更低延迟与更高稳定性。同时提供中国大陆三网回程优化线路，是全球化 AI 代理平台、海外 AI SaaS 及跨境高并发部署的理想选择。</td>
</tr>

</table>

## 生态项目

扩展或集成 Sub2API 的社区项目：

| 项目 | 描述 | 功能特性 |
|---------|-------------|----------|
| ~~[Sub2ApiPay](https://github.com/touwaeriol/sub2apipay)~~ | ~~自助支付系统~~ | **已内置** — 支付功能现已集成至 Sub2API，无需单独部署。详见 [支付配置指南](docs/PAYMENT.md) |
| [sub2api-mobile](https://github.com/ckken/sub2api-mobile) | 移动端管理控制台 | 跨平台应用（iOS/Android/Web），支持用户管理、账号管理、监控看板及多后端切换；基于 Expo + React Native 构建 |

## 技术栈

| 组件 | 技术 |
|-----------|------------|
| 后端 | Go 1.25.7, Gin, Ent |
| 前端 | Vue 3.4+, Vite 5+, TailwindCSS |
| 数据库 | PostgreSQL 15+ |
| 缓存与队列 | Redis 7+ |

---

## Nginx 反向代理注意事项

当使用 Nginx 作为 Sub2API（或 CRS）的反向代理，并结合 Codex CLI 使用时，请在 Nginx 配置文件的 `http` 块中添加以下内容：

```nginx
underscores_in_headers on;
```

Nginx 默认会丢弃包含下划线的请求头（如 `session_id`），这会导致多账号环境下的粘性会话路由失效。

---

## 部署指南

### 方式一：脚本安装（推荐）

一键安装脚本，从 GitHub Releases 下载预编译二进制文件。

#### 前置条件

- Linux 服务器（amd64 或 arm64）
- PostgreSQL 15+（已安装并运行）
- Redis 7+（已安装并运行）
- Root 权限

#### 安装步骤

```bash
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

脚本将执行以下操作：
1. 检测系统架构
2. 下载最新版本
3. 将二进制文件安装至 `/opt/sub2api`
4. 创建 systemd 服务
5. 配置系统用户及权限

#### 安装后操作

```bash
# 1. 启动服务
sudo systemctl start sub2api

# 2. 设置开机自启
sudo systemctl enable sub2api

# 3. 在浏览器中打开安装向导
# http://YOUR_SERVER_IP:8080
```

安装向导将引导你完成：
- 数据库配置
- Redis 配置
- 管理员账号创建

#### 升级

你可以直接在 **管理后台** 点击左上角的 **检查更新** 按钮进行升级。

Web 界面将自动执行以下操作：
- 自动检测新版本
- 一键下载并应用更新
- 支持必要时回滚

#### 常用命令

```bash
# 查看状态
sudo systemctl status sub2api

# 查看日志
sudo journalctl -u sub2api -f

# 重启服务
sudo systemctl restart sub2api

# 卸载
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash -s -- uninstall -y
```

---

### 方式二：Docker Compose（推荐）

使用 Docker Compose 部署，包含 PostgreSQL 和 Redis 容器。

#### 前置条件

- Docker 20.10+
- Docker Compose v2+

#### 快速启动（一键部署）

使用自动化部署脚本轻松完成设置：

```bash
# 创建部署目录
mkdir -p sub2api-deploy && cd sub2api-deploy

# 下载并运行部署准备脚本
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash

# 启动服务
docker compose up -d

# 查看日志
docker compose logs -f sub2api
```

**脚本执行内容：**
- 下载 `docker-compose.local.yml`（保存为 `docker-compose.yml`）和 `.env.example`
- 生成安全凭证（JWT_SECRET、TOTP_ENCRYPTION_KEY、POSTGRES_PASSWORD）
- 创建包含自动生成密钥的 `.env` 文件
- 创建数据目录（使用本地目录以便备份/迁移）
- 显示生成的凭证供你参考

#### 手动部署

如果你偏好手动设置：

```bash
# 1. 克隆仓库
git clone https://github.com/Wei-Shaw/sub2api.git
cd sub2api/deploy

# 2. 复制环境配置
cp .env.example .env

# 3. 编辑配置（生成安全密码）
nano .env
```

**`.env` 中必需的配置：**

```bash
# PostgreSQL 密码（必填）
POSTGRES_PASSWORD=your_secure_password_here

# JWT Secret（推荐 - 重启后保持用户登录状态）
JWT_SECRET=your_jwt_secret_here

# TOTP 加密密钥（推荐 - 重启后保留两步验证数据）
TOTP_ENCRYPTION_KEY=your_totp_key_here

# 可选：管理员账号
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=your_admin_password

# 可选：自定义端口
SERVER_PORT=8080
```

**生成安全密钥：**
```bash
# 生成 JWT_SECRET
openssl rand -hex 32

# 生成 TOTP_ENCRYPTION_KEY
openssl rand -hex 32

# 生成 POSTGRES_PASSWORD
openssl rand -hex 32
```

```bash
# 4. 创建数据目录（本地版本）
mkdir -p data postgres_data redis_data

# 5. 启动所有服务
# 方案 A：本地目录版本（推荐 - 便于迁移）
docker compose -f docker-compose.local.yml up -d

# 方案 B：命名卷版本（简单设置）
docker compose up -d

# 6. 检查状态
docker compose -f docker-compose.local.yml ps

# 7. 查看日志
docker compose -f docker-compose.local.yml logs -f sub2api
```

#### 部署版本对比

| 版本 | 数据存储方式 | 迁移难度 | 适用场景 |
|---------|-------------|-----------|----------|
| **docker-compose.local.yml** | 本地目录 | ✅ 简单（打包整个目录） | 生产环境、频繁备份 |
| **docker-compose.yml** | Docker 命名卷 | ⚠️ 需使用 docker 命令操作 | 简易测试/开发 |

**建议：** 使用 `docker-compose.local.yml`（脚本默认部署版本）以便更轻松地管理数据。

#### 访问地址

在浏览器中打开 `http://YOUR_SERVER_IP:8080`。

如果管理员密码为自动生成，可在日志中查找：
```bash
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```

#### 升级

```bash
# 拉取最新镜像并重建容器
docker compose -f docker-compose.local.yml pull
docker compose -f docker-compose.local.yml up -d
```

#### 轻松迁移（本地目录版本）

使用 `docker-compose.local.yml` 时，可轻松迁移至新服务器：

```bash
# 在源服务器上执行
docker compose -f docker-compose.local.yml down
cd ..
tar czf sub2api-complete.tar.gz sub2api-deploy/

# 传输至新服务器
scp sub2api-complete.tar.gz user@new-server:/path/

# 在新服务器上执行
tar xzf sub2api-complete.tar.gz
cd sub2api-deploy/
docker compose -f docker-compose.local.yml up -d
```

#### 常用命令

```bash
# 停止所有服务
docker compose -f docker-compose.local.yml down

# 重启
docker compose -f docker-compose.local.yml restart

# 查看所有日志
docker compose -f docker-compose.local.yml logs -f

# 删除所有数据（谨慎操作！）
docker compose -f docker-compose.local.yml down
rm -rf data/ postgres_data/ redis_data/
```

---

### 方式三：源码编译

从源代码构建并运行，适用于开发或自定义需求。

#### 前置条件

- Go 1.21+
- Node.js 18+
- PostgreSQL 15+
- Redis 7+

#### 构建步骤

```bash
# 1. 克隆仓库
git clone https://github.com/Wei-Shaw/sub2api.git
cd sub2api

# 2. 安装 pnpm（如尚未安装）
npm install -g pnpm

# 3. 构建前端
cd frontend
pnpm install
pnpm run build
# 输出将位于 ../backend/internal/web/dist/

# 4. 使用嵌入的前端构建后端
cd ../backend
go build -tags embed -o sub2api ./cmd/server

# 5. 创建配置文件
cp ../deploy/config.example.yaml ./config.yaml

# 6. 编辑配置
nano config.yaml
```

> **注意：** `-tags embed` 标志会将前端嵌入至二进制文件中。若未添加此标志，编译出的程序将无法提供前端 UI。

**`config.yaml` 中的关键配置：**

```yaml
server:
  host: "0.0.0.0"
  port: 8080
  mode: "release"

database:
  host: "localhost"
  port: 5432
  user: "postgres"
  password: "your_password"
  dbname: "sub2api"

redis:
  host: "localhost"
  port: 6379
  password: ""

jwt:
  secret: "change-this-to-a-secure-random-string"
  expire_hour: 24

default:
  user_concurrency: 5
  user_balance: 0
  api_key_prefix: "sk-"
  rate_multiplier: 1.0
```

### Sora 状态（暂时不可用）

> ⚠️ 由于上游集成与媒体传输的技术问题，Sora 相关功能目前暂时不可用。
> 现阶段请勿在生产环境中依赖 Sora。
> 现有的 `gateway.sora_*` 配置键已保留，待问题解决前可能不会生效。

`config.yaml` 中还提供其他安全相关选项：

- `cors.allowed_origins` 用于 CORS 白名单设置
- `security.url_allowlist` 用于上游/计费/CRS 主机地址白名单
- `security.url_allowlist.enabled` 禁用 URL 验证（请谨慎使用）
- `security.url_allowlist.allow_insecure_http` 在禁用验证时允许 HTTP 协议 URL
- `security.url_allowlist.allow_private_hosts` 允许私有/本地 IP 地址
- `security.response_headers.enabled` 启用可配置响应头过滤（关闭时使用默认白名单）
- `security.csp` 控制 Content-Security-Policy 响应头
- `billing.circuit_breaker` 在计费错误时触发熔断机制
- `server.trusted_proxies` 启用 X-Forwarded-For 解析
- `turnstile.required` 在 release 模式下要求验证 Turnstile

**⚠️ 安全警告：HTTP URL 配置**

当 `security.url_allowlist.enabled=false` 时，系统默认仅执行最低限度的 URL 验证，**拒绝 HTTP 协议 URL**，仅允许 HTTPS。若要允许 HTTP 协议 URL（例如用于开发或内部测试），你必须显式设置：

```yaml
security:
  url_allowlist:
    enabled: false                # 禁用白名单检查
    allow_insecure_http: true     # 允许 HTTP URL（⚠️ 不安全）
```

**或通过环境变量配置：**

```bash
SECURITY_URL_ALLOWLIST_ENABLED=false
SECURITY_URL_ALLOWLIST_ALLOW_INSECURE_HTTP=true
```

**允许 HTTP 的风险：**
- API Key 与数据将以**明文形式传输**（易被拦截）
- 易受 **中间人攻击（MITM）**
- **不适合生产环境**

**适用场景：**
- ✅ 使用本地服务器的开发/测试（http://localhost）
- ✅ 内部网络且端点可信的环境
- ✅ 获取 HTTPS 证书前测试账号连通性
- ❌ 生产环境（仅使用 HTTPS）

**未配置此选项时的典型报错：**
```
Invalid base URL: invalid url scheme: http
```

若你禁用了 URL 验证或响应头过滤，请加固你的网络层：
- 对上游域名/IP 实施出口白名单策略
- 拦截私有/回环/链路本地地址段
- 强制仅允许 TLS 出站流量
- 在代理层剥离敏感的上游响应头

```bash
# 6. 运行程序
./sub2api
```

#### 开发模式

```bash
# 后端（支持热重载）
cd backend
go run ./cmd/server

# 前端（支持热重载）
cd frontend
pnpm run dev
```

#### 代码生成

编辑 `backend/ent/schema` 后，需重新生成 Ent + Wire：

```bash
cd backend
go generate ./ent
go generate ./cmd/server
```

---

## 简易模式 (Simple Mode)

简易模式专为希望快速上手且无需完整 SaaS 功能的个人开发者或内部团队设计。

- **启用方式**：设置环境变量 `RUN_MODE=simple`
- **功能差异**：隐藏 SaaS 相关功能，并跳过计费流程
- **安全提示**：在生产环境中运行前，你还需设置 `SIMPLE_MODE_CONFIRM=true` 以允许启动

---

## Antigravity（反重力）支持

Sub2API 支持 [Antigravity](https://antigravity.so/) 账号。授权后，可为 Claude 和 Gemini 模型提供专用端点。

### 专用端点

| 端点 | 模型 |
|----------|-------|
| `/antigravity/v1/messages` | Claude 系列模型 |
| `/antigravity/v1beta/` | Gemini 系列模型 |

### Claude Code 配置

```bash
export ANTHROPIC_BASE_URL="http://localhost:8080/antigravity"
export ANTHROPIC_AUTH_TOKEN="sk-xxx"
```

### 混合调度模式

Antigravity 账号支持可选的 **混合调度**。启用后，通用端点 `/v1/messages` 和 `/v1beta/` 也将把请求路由至 Antigravity 账号。

> **⚠️ 警告**：Anthropic Claude 与 Antigravity Claude **不可在同一对话上下文中混用**。请使用分组功能将它们隔离。

### 已知问题

在 Claude Code 中，Plan Mode（规划模式）无法自动退出。（通常在使用原生 Claude API 时，规划完成后 Claude Code 会弹出选项供用户批准或拒绝计划。）

**临时解决方案**：按 `Shift + Tab` 手动退出 Plan Mode，随后输入你的回复以批准或拒绝该计划。

---

## 项目结构

```
sub2api/
├── backend/                  # Go backend service
│   ├── cmd/server/           # Application entry
│   ├── internal/             # Internal modules
│   │   ├── config/           # Configuration
│   │   ├── model/            # Data models
│   │   ├── service/          # Business logic
│   │   ├── handler/          # HTTP handlers
│   │   └── gateway/          # API gateway core
│   └── resources/            # Static resources
│
├── frontend/                 # Vue 3 frontend
│   └── src/
│       ├── api/              # API calls
│       ├── stores/           # State management
│       ├── views/            # Page components
│       └── components/       # Reusable components
│
└── deploy/                   # Deployment files
    ├── docker-compose.yml    # Docker Compose configuration
    ├── .env.example          # Environment variables for Docker Compose
    ├── config.example.yaml   # Full config file for binary deployment
    └── install.sh            # One-click installation script
```

## 免责声明

> **使用前请仔细阅读：**
>
> :rotating_light: **服务条款风险**：使用本项目可能违反 Anthropic 的服务条款（Terms of Service）。使用前请务必仔细阅读 Anthropic 的用户协议。因使用本项目而产生的所有风险均由用户自行承担。
>
> :book: **免责声明**：本项目仅用于技术学习与研究目的。作者不对因使用本项目导致的账号封禁、服务中断或其他任何损失承担任何责任。

---

## Star History

<a href="https://star-history.com/#Wei-Shaw/sub2api&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Wei-Shaw/sub2api&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Wei-Shaw/sub2api&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Wei-Shaw/sub2api&type=Date" />
 </picture>
</a>

---

## 许可证

本项目采用 [GNU Lesser General Public License v3.0](LICENSE)（或更高版本）许可。

Copyright (c) 2026 Wesley Liddick

---

<div align="center">

**如果你觉得这个项目有用，请给它一个 Star！**

</div>