# lark-cli

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/go-%3E%3D1.23-blue.svg)](https://go.dev/)
[![npm version](https://img.shields.io/npm/v/@larksuite/cli.svg)](https://www.npmjs.com/package/@larksuite/cli)

[中文版](./README.zh.md) | [English](./README.md)

由 larksuite 团队维护的官方 [Lark/飞书](https://www.larksuite.com/) CLI 工具——专为人类与 AI Agent 打造。涵盖即时通讯、文档、多维表格、电子表格、幻灯片、日历、邮件、任务、会议、Markdown 等核心业务领域，提供 200+ 命令及 26 个 AI Agent [技能](./skills/)。

[安装](#安装与快速入门) · [AI Agent 技能](#agent-技能) · [身份验证](#身份验证) · [命令系统](#三层命令系统) · [高级用法](#高级用法) · [安全警告](#安全与风险警告（使用前必读）) · [贡献指南](#贡献指南)

## 为什么选择 lark-cli？

- **Agent 原生设计** — 开箱即用的 24 个结构化 [技能](./skills/)，兼容主流 AI 工具——Agent 可零配置操作 Lark
- **覆盖广泛** — 18 个业务领域，精选 200+ 命令，26 个 AI Agent [技能](./skills/)
- **AI 友好且优化** — 每条命令均经真实 Agent 测试，参数精简、默认值智能、输出结构化，最大化 Agent 调用成功率
- **开源无门槛** — MIT 协议，开箱即用，仅需 `npm install`
- **3 分钟快速上手** — 一键创建应用、交互式登录，从安装到首次 API 调用仅需 3 步
- **安全可控** — 输入注入防护、终端输出清洗、操作系统原生密钥链凭据存储
- **三层架构** — 快捷指令（人类与 AI 友好）→ API 命令（平台同步）→ 原始 API（全覆盖），按需选择粒度

## 功能特性

| 类别      | 能力                                                                                                                      |
| ------------- |-----------------------------------------------------------------------------------------------------------------------------------|
| 📅 日历   | 查看、创建和更新日程，邀请参会人，查找会议室，回复会议邀请，查询空闲/忙碌状态及时间建议     |
| 💬 即时通讯  | 发送/回复消息，创建和管理群聊，查看聊天记录与线程，搜索消息，下载媒体文件                  |
| 📄 文档       | 创建、读取、更新和搜索文档，读写媒体内容与白板                                                        |
| 📁 云盘      | 上传和下载文件，搜索文档与知识库，管理评论                                                                    |
| 📝 Markdown   | 创建、获取、修改和覆盖云盘原生的 `.md` 文件                                                                      |
| 📊 多维表格       | 创建和管理数据表、字段、记录、视图、仪表盘、工作流、表单、角色与权限、数据聚合与分析 |
| 📈 电子表格     | 创建、读取、写入、追加、查找和导出表格数据                                                                    |
| 🖼️ 幻灯片     | 创建和管理演示文稿，读取内容，添加或删除幻灯片                                              |
| ✅ 任务      | 创建、查询、更新和完成任务；管理任务列表、子任务、评论与提醒                                      |
| 📚 知识库       | 创建和管理知识空间、节点和文档                                                                          |
| 👤 通讯录    | 按姓名/邮箱/手机号搜索用户，获取用户资料                                                                               |
| 📧 邮件       | 浏览、搜索、阅读邮件，发送、回复、转发，管理草稿，订阅新邮件通知                                                  |
| 🎥 会议   | 搜索会议记录，查询会议纪要素材与录音录像                                                            |
| 🕐 考勤打卡 | 查询个人考勤打卡记录                                                                                        |
| ✍️ 审批   | 查询审批任务，通过/拒绝/转交任务，取消和抄送实例                                                      |
| 🎯 OKR        | 查询、创建、更新目标与关键结果；管理对齐关系、指标与进度。                                  |
| 📋 项目管理    | Meegle — 通过独立 [meegle-cli](https://github.com/larksuite/meegle-cli)（需单独安装）管理工作项、日程和数据 |
| 🔗 应用       | 开发、部署 HTML、网页和应用程序                                                                                  |

## 安装与快速入门

### 前置要求

开始前，请确保你已具备：

- Node.js (`npm`/`npx`)
- Go `v1.23`+ 和 Python 3（仅用于从源码构建）

### 快速入门（人类用户）

> **AI 助手注意：** 如果你是协助用户安装的 AI Agent，请直接跳转至 [快速入门（AI Agent）](#quick-start-ai-agent)，其中包含你需要完成的所有步骤。

#### 安装

选择以下任一方式：

**方案 1 — 通过 npm 安装（推荐）：**

```bash
npx @larksuite/cli@latest install
```

**方案 2 — 从源码构建：**

需要 Go `v1.23`+ 和 Python 3。

```bash
git clone https://github.com/larksuite/cli.git
cd cli
make install

# 安装 CLI SKILL（必需）
npx skills add larksuite/cli -y -g
```

#### 配置与使用

```bash
# 1. 配置应用凭据（一次性，交互式引导设置）
lark-cli config init

# 2. 登录（--recommend 推荐自动选择常用权限范围）
lark-cli auth login --recommend

# 3. 开始使用
lark-cli calendar +agenda
```

## 快速入门（AI Agent）

> 以下步骤面向 AI Agent。部分步骤需要用户在浏览器中完成操作。

**步骤 1 — 安装**

```bash
npx @larksuite/cli@latest install
```

**步骤 2 — 配置应用凭据**

> 请在后台运行此命令。它将输出一条授权链接——提取该链接并发送给你（用户）。用户在浏览器完成设置后，命令将自动退出。

```bash
lark-cli config init --new
```

**步骤 3 — 登录**

> 同上：在后台运行，提取授权链接并发送给你（用户）。

```bash
lark-cli auth login --recommend
```

**步骤 4 — 验证**

```bash
lark-cli auth status
```

## Agent 技能

| Skill                           | 描述                                                                                                    |
| ------------------------------- |----------------------------------------------------------------------------------------------------------------|
| `lark-shared`                   | 应用配置、身份验证登录、身份切换、权限范围管理、安全规则（其他所有技能自动加载） |
| `lark-calendar`                 | 日历日程（创建/更新）、议程视图、空闲/忙碌查询、时间建议、查找会议室、回复会议邀请  |
| `lark-im`                       | 发送/回复消息，群聊管理，消息搜索，上传/下载图片与文件，表情回应          |
| `lark-doc`                      | 创建、读取、更新、搜索文档（基于 Markdown）                                                        |
| `lark-drive`                    | 上传、下载文件，管理权限与评论                                                          |
| `lark-markdown`                 | 创建、获取、修改和覆盖云盘原生 Markdown 文件                                                |
| `lark-sheets`                   | 创建、读取、写入、追加、查找、导出电子表格                                                         |
| `lark-slides`                   | 创建和管理演示文稿，读取内容，添加或删除幻灯片                          |
| `lark-base`                     | 数据表、字段、记录、视图、仪表盘、数据聚合与分析                                       |
| `lark-task`                     | 任务、任务列表、子任务、提醒、成员分配                                                      |
| `lark-mail`                     | 浏览、搜索、阅读邮件，发送、回复、转发，草稿管理，订阅新邮件通知                            |
| `lark-contact`                  | 按姓名/邮箱/手机号搜索用户，获取用户资料                                                            |
| `lark-wiki`                     | 知识空间、节点、文档                                                                             |
| `lark-event`                    | 实时事件订阅（WebSocket），正则路由与 Agent 友好格式                               |
| `lark-vc`                       | 搜索会议记录，查询会议纪要（摘要、待办事项、逐字稿）                                     |
| `lark-whiteboard`               | 白板/图表 DSL 渲染                                                                                 |
| `lark-minutes`                  | 纪要元数据与 AI 素材（摘要、待办事项、章节）；上传音视频创建纪要，下载媒体 |
| `lark-openapi-explorer`         | 从官方文档探索底层 API                                                                     |
| `lark-skill-maker`              | 自定义技能创建框架                                                                                |
| `lark-attendance`               | 查询个人考勤打卡记录                                                                     |
| `lark-approval`                 | 查询审批任务，通过/拒绝/转交任务，取消和抄送实例                                   |
| `lark-workflow-meeting-summary` | 工作流：会议纪要聚合与结构化报告                                                      |
| `lark-workflow-standup-report`  | 工作流：议程与待办事项摘要                                                                                |
| `lark-okr`                      | 查询、创建、更新 OKR；管理目标与关键结果、对齐关系和指标。                         |

## 身份验证

| Command       | 描述                                                    |
| ------------- | -------------------------------------------------------------- |
| `auth login`  | OAuth 交互式选择或通过 CLI 参数指定权限范围进行登录 |
| `auth logout` | 退出登录并清除已存储的凭据                         |
| `auth status` | 显示当前登录状态与已授予的权限范围                   |
| `auth check`  | 验证特定权限（返回 0 = 正常，1 = 缺失）            |
| `auth scopes` | 列出应用所有可用的权限范围                          |
| `auth list`   | 列出所有已认证的用户                                   |

```bash
# 交互式登录（TUI 引导选择域名与权限级别）
lark-cli auth login

# 按域名过滤
lark-cli auth login --domain calendar,task

# 推荐自动授权范围
lark-cli auth login --recommend

# 精确指定权限
lark-cli auth login --scope "calendar:calendar:read"

# Agent 模式：立即返回验证链接，非阻塞
lark-cli auth login --domain calendar --no-wait
# 稍后恢复轮询
lark-cli auth login --device-code <DEVICE_CODE>

# 身份切换：以用户或机器人身份执行命令
lark-cli calendar +agenda --as user
lark-cli im +messages-send --as bot --chat-id "oc_xxx" --text "Hello"
```

## 三层命令系统

CLI 提供三个粒度的操作层级，覆盖从快捷操作到完全自定义 API 调用的所有场景：

### 1. 快捷指令 (Shortcuts)

以 `+` 为前缀，专为人类和 AI 设计，具备智能默认值、表格输出及试运行预览功能。

```bash
lark-cli calendar +agenda
lark-cli im +messages-send --chat-id "oc_xxx" --text "Hello"
lark-cli docs +create --api-version v2 --doc-format markdown --content $'<title>Weekly Report</title>\n# Progress\n- Completed feature X'
```

运行 `lark-cli <service> --help` 查看所有快捷指令。

### 2. API 命令 (API Commands)

基于飞书开放平台（Lark OAPI）元数据自动生成，经评估与质量门禁筛选——100+ 命令与平台端点 1:1 映射。

```bash
lark-cli calendar calendars list
lark-cli calendar events instance_view --params '{"calendar_id":"primary","start_time":"1700000000","end_time":"1700086400"}'
```

### 3. 原始 API 调用 (Raw API Calls)

直接调用飞书开放平台的任意接口，覆盖 2500+ API。

```bash
lark-cli api GET /open-apis/calendar/v4/calendars
lark-cli api POST /open-apis/im/v1/messages --params '{"receive_id_type":"chat_id"}' --data '{"receive_id":"oc_xxx","msg_type":"text","content":"{\"text\":\"Hello\"}"}'
```

## 高级用法

### 输出格式 (Output Formats)

```bash
--format json      # 完整 JSON 响应（默认）
--format pretty    # 人类友好的格式化输出
--format table     # 可读性表格
--format ndjson    # 逐行分隔的 JSON（用于管道传输）
--format csv       # 逗号分隔值
```

### 分页处理 (Pagination)

```bash
--page-all                  # 自动遍历所有页面
--page-limit 5              # 最多 5 页
--page-delay 500            # 请求间隔 500ms
```

### 试运行模式 (Dry Run)

对可能产生副作用的命令，建议先使用 `--dry-run` 预览请求：

```bash
lark-cli im +messages-send --chat-id oc_xxx --text "hello" --dry-run
```

### Schema 探查 (Schema Introspection)

使用 schema 检查任意 API 方法的参数、请求体、响应结构、支持的主体身份及权限范围：

```bash
lark-cli schema
lark-cli schema calendar.events.instance_view
lark-cli schema im.messages.delete
```

## 安全与风险警告（使用前必读）

本工具可由 AI Agent 调用，用于自动化操作飞书开放平台，因此存在模型幻觉、不可预测的执行行为以及提示词注入等固有风险。在你授权 Lark/飞书权限后，AI Agent 将在授权范围内以你的用户身份进行操作，可能导致敏感数据泄露或未经授权的操作等高后果风险。请谨慎使用。

为降低上述风险，本工具在多个层级启用了默认安全保护机制。但这些风险依然存在。我们强烈建议你**不要主动修改任何默认安全设置**；一旦相关限制被放宽，风险将显著增加，且你需要自行承担相应后果。

建议使用集成此工具的 Lark/飞书机器人作为私人对话助手。请勿将其添加至群聊或允许其他用户与其交互，以避免权限滥用或数据泄露。

请充分理解所有使用风险。**使用本工具即视为你自愿承担所有相关责任。**

## 星标历史

[![Star History Chart](https://api.star-history.com/svg?repos=larksuite/cli&type=Date)](https://star-history.com/#larksuite/cli&Date)

## 贡献指南

欢迎社区贡献！如果你发现 Bug 或有功能建议，请提交 [Issue](https://github.com/larksuite/cli/issues) 或 [Pull Request](https://github.com/larksuite/cli/pulls)。

对于重大变更，我们建议你首先通过 Issue 与我们讨论。

在提交 PR 前，请参阅 [AGENTS.md](./AGENTS.md)，其中包含贡献者与 AI Agent 使用的本地构建、测试及 PR 检查清单。

## 许可证

本项目采用 **MIT License** 开源协议。
运行时，本工具会调用飞书开放平台 API。使用这些 API 需遵守以下协议与隐私政策：

- [飞书用户服务协议](https://www.feishu.cn/terms)
- [飞书隐私政策](https://www.feishu.cn/privacy)
- [飞书开放平台应用服务商安全管理规范](https://open.feishu.cn/document/uAjLw4CM/uMzNwEjLzcDMx4yM3ATM/management-practice/app-service-provider-security-management-specifications)
- [Lark User Terms of Service](https://www.larksuite.com/user-terms-of-service)
- [Lark Privacy Policy](https://www.larksuite.com/privacy-policy)