<a href="https://go.novu.co/github?utm_campaign=readme-logo" target="_blank" rel="noopener noreferrer">
  <img alt="Novu Logo" src=".github/assets/novu-logo.svg" width="100%"/>
</a>

<br/>
<br/>
<p align="center">
  <a href="https://www.producthunt.com/products/novu" target="_blank" rel="noopener noreferrer"
>
    <img src="https://img.shields.io/badge/Product%20Hunt-Golden%20Kitty%20Award%202023-yellow" alt="Product Hunt">
  </a>
  <a href="https://news.ycombinator.com/item?id=38419513" target="_blank" rel="noopener noreferrer"
><img src="https://img.shields.io/badge/Hacker%20News-%231-%23FF6600" alt="Hacker News"></a>
  <a href="https://www.npmjs.com/package/@novu/react" target="_blank" rel="noopener noreferrer"
>
    <img src="https://img.shields.io/npm/v/@novu/react" alt="NPM">
  </a>
  <a href="https://www.npmjs.com/package/@novu/js" target="_blank" rel="noopener noreferrer"
>
    <img src="https://img.shields.io/npm/dm/@novu/js" alt="npm downloads">
  </a>
</p>

<h1 align="center">
面向智能体（Agents）与产品的开源通信基础设施
</h1>

<div align="center">
一套统一的 API 和对话模型，将你的 <strong>产品</strong> 和 <strong>智能体</strong> 连接到用户活跃的所有渠道——收件箱、电子邮件、短信、推送通知、聊天应用、Slack、Microsoft Teams、Telegram 等。
</div>

<p align="center">
  <br />
  <a href="https://go.novu.co/github?utm_source=github&utm_medium=readme&utm_campaign=learn-more-link" rel="dofollow"><strong>了解更多 »</strong></a>
  <br />

<br/>
  <a href="https://github.com/novuhq/novu/issues/new?assignees=&labels=type%3A+bug&template=bug_report.yml&title=%F0%9F%90%9B+Bug+Report%3A+" target="_blank" rel="noopener noreferrer"
>报告 Bug</a>
  ·
  <a href="https://docs.novu.co" target="_blank" rel="noopener noreferrer"
>文档</a>
  ·
  <a href="https://go.novu.co/github?utm_campaign=readme_website" target="_blank" rel="noopener noreferrer"
>官网</a>
  ·
  <a href="https://discord.novu.co" target="_blank" rel="noopener noreferrer"
>加入我们的 Discord</a>
  ·
  <a href="https://go.novu.co/changelog" target="_blank" rel="noopener noreferrer"
>更新日志</a>
  ·
  <a href="https://go.novu.co/roadmap" target="_blank" rel="noopener noreferrer"
>路线图</a>
  ·
  <a href="https://twitter.com/novuhq" target="_blank" rel="noopener noreferrer"
>X</a>
  ·
  <a href="https://go.novu.co/contact?utm_source=github&utm_medium=readme&utm_campaign=contact-us-link" target="_blank" rel="noopener noreferrer"
>联系我们</a>

软件正变得越来越具有对话性，用户对交互的期望也随之提升。人们不再满足于那些看一眼就忘的静态、无关紧要的通知，他们希望能够互动、提问并深入探索。与其将单向报告塞进收件箱，用户更期待一个可以自行探索的对话线程：跟进某项指标数据、深挖异常现象，或从上次中断的地方继续对话。正是为了应对这种从“广播式通知”到“有意义对话”的转变，Novu 构建了其通信基础设施。

## ⭐️ 为什么选择 Novu？
 
每个产品和智能体最终都需要与用户沟通，而这些用户已经在使用特定的渠道。Novu 是处理这一通信的开源层，让你无需每次重新从底层构建收件箱流、服务商集成和渠道 Webhook。
 
使用 Novu 有两种方式，它们共享同一套基础：一套统一的 API 和一个标准化的对话模型。
 
- **面向产品的通信基础设施** — 通过一套 API 在收件箱/应用内（Inbox/In-App）、电子邮件、短信、推送通知和聊天应用中发送通知，支持工作流、摘要聚合以及可嵌入的 `<Inbox />` 组件。
- **智能体通信基础设施（ACI）** — 将任何已构建的智能体连接到任意通信渠道：Slack、Microsoft Teams、Telegram、WhatsApp、电子邮件等，全部基于统一的对话模型实现。

## 🚀 快速上手

[创建免费账户](https://go.novu.co/dashboard?utm_source=github&utm_medium=readme&utm_campaign=create-free-account-link) 并跟随仪表板中的指引操作。

## 📚 目录
 
- [为什么选择 Novu？](#️-为什么选择-novu)
- [面向产品的通信基础设施](#-面向产品的通信基础设施)
- [智能体通信基础设施（ACI）](#-智能体通信基础设施aci)
- [快速上手](#-快速上手)
- [可嵌入的收件箱与偏好设置](#可嵌入的收件箱组件)
- [服务提供商 (Providers)](#providers)

## 📬 面向产品的通信基础设施
 
将复杂的多渠道分发转化为单一组件的通知平台。为开发者打造，为增长设计，由开源驱动。
 
Novu 提供统一的 API，通过 **收件箱/应用内、推送通知、电子邮件、短信和聊天应用** 等多个渠道发送通知。你可以自定义工作流、定义按渠道划分的条件，让 Novu 以最高效的方式投递每条通知，无需你自己为每个渠道拼接不同的服务商集成。
 
- 一套 API 覆盖所有消息服务提供商
- 可嵌入的实时 `<Inbox />` 组件
- 支持分支与条件的通知工作流引擎
- 摘要引擎：将多条通知批量合并为单条消息
- 可视化邮件编辑器（No-code email editor）
- 可嵌入的用户偏好设置组件，让用户自主控制自己的通知

## 🤖 智能体通信基础设施（ACI）
 
> **你构建智能体，Novu 赋予它声音。**
 
ACI 是一套完整的解决方案，专为那些需要与用户在真实通信渠道上交互的智能体公司设计。它将你的智能体连接到任意渠道，并通过统一的对话模型屏蔽各平台特有的差异与限制。
 
Novu 负责双向的底层对接：接收来自各渠道的用户消息，将其标准化为统一格式，路由到你的智能体；随后将智能体的回复发回原渠道。你只需集成一次，无需为每个平台单独构建和维护 Webhook 处理器。
 
- **统一的对话模型** — 跨所有渠道保持一致的消息结构，摆脱各平台特有的格式差异和 Webhook 限制
- **双向消息通信** — 通过同一层接收用户消息并发送智能体回复
- **渠道集成** — Slack、Microsoft Teams、Telegram、WhatsApp、电子邮件，以及专为智能体设计的应用内收件箱
- **支持自有智能体** — 兼容你已构建的任何技术栈（无论是 Claude Managed Agents、AI SDK、LangGraph 还是自定义架构）；Novu 不会限制你的智能体逻辑
- **内置最佳实践** — 对话线程管理、表情回应、渠道感知格式化、操作指令，以及统一的集成接口
Novu 负责将智能体连接到世界，它本身并不是智能体。

### 想看看 ACI 的实际效果？
我们构建了 [Novu Connect](https://novu.co/connect) 来展示 ACI 的能力：你可以在不到 2 分钟内将已有的 Claude Managed Agent 集成并作为团队成员接入 Slack、Telegram 或电子邮件。 

立即体验：
```
npx novu@latest connect
```

## 可嵌入的收件箱组件

借助 Novu API 和管理面板，你可以轻松为你的 Web 应用添加实时通知中心，无需自行从头开发。你可以使用我们的 [React](https://docs.novu.co/inbox/react/get-started?utm_source=github&utm_medium=readme&utm_campaign=react-starter-link) 组件，或通过我们的 API 和 SDK 自行构建。React Native、Vue 和 Angular 版本即将推出。

<div align="center">
<img width="4800" height="2700" alt="Novu's Embeddable Inbox components" src="https://github.com/user-attachments/assets/00224c75-7ed0-4e19-b6fd-2a0bdced6258" />

阅读更多有关为你的应用添加 [通知中心收件箱](https://docs.novu.co/inbox/react/get-started?utm_source=github&utm_medium=readme&utm_campaign=read-more-react-link) 的指南。

</div>

## 服务提供商 (Providers)

Novu 提供一套统一的 API，通过简单易用的 API 和 UI 界面管理跨多个渠道的服务商集成。

展开下方各分类浏览支持的提供商列表。

<details>
<summary><strong>💌 电子邮件（Email）</strong> (19 providers)</summary>

| Provider |
| --- |
| [Amazon SES](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/ses) |
| [Braze](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/braze) |
| [Brevo](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/brevo) |
| [Custom SMTP](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/nodemailer) |
| [Email Webhook](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/email-webhook) |
| [Email.js](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/emailjs) |
| [Infobip](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/infobip) |
| [MailerSend](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/mailersend) |
| [Mailgun](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/mailgun) |
| [Mailjet](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/mailjet) |
| [Mailtrap](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/mailtrap) |
| [Mandrill](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/mandrill) |
| [Netcore](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/netcore) |
| [Outlook 365](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/outlook365) |
| [Plunk](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/plunk) |
| [Postmark](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/postmark) |
| [Resend](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/resend) |
| [SendGrid](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/sendgrid) |
| [SparkPost](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/email/sparkpost) |

</details>

<details>
<summary><strong>📞 短信（SMS）</strong> (37 providers)</summary>

| Provider |
| --- |
| [46elks](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/forty-six-elks) |
| [Africa's Talking](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/africas-talking) |
| [Afro SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/afro-sms) |
| [Amazon SNS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/sns) |
| [Azure SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/azure-sms) |
| [Bandwidth](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/bandwidth) |
| [Brevo SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/brevo-sms) |
| [Bulk SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/bulk-sms) |
| [Burst SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/burst-sms) |
| [Clickatell](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/clickatell) |
| [ClickSend](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/clicksend) |
| [CM Telecom](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/cm-telecom) |
| [Eazy SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/eazy-sms) |
| [Firetext](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/firetext) |
| [Generic SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/generic-sms) |
| [Gupshup](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/gupshup) |
| [iMedia](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/imedia) |
| [Infobip](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/infobip) |
| [iSend SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/isend-sms) |
| [iSendPro SMS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/isendpro-sms) |
| [Kannel](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/kannel) |
| [Maqsam](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/maqsam) |
| [MessageBird](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/messagebird) |
| [Mobishastra](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/mobishastra) |
| [Plivo](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/plivo) |
| [RingCentral](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/ring-central) |
| [Sendchamp](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/sendchamp) |
| [SimpleTexting](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/simpletexting) |
| [Sinch](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/sinch) |
| [SMS Central](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/sms-central) |
| [SMS77](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/sms77) |
| [SMSMode](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/smsmode) |
| [Telnyx](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/telnyx) |
| [Termii](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/termii) |
| [Twilio](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/twilio) |
| [Unifonic](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/unifonic) |
| [Vonage](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/sms/nexmo) |

</details>

<details>
<summary><strong>📱 推送通知（Push）</strong> (8 providers)</summary>

| Provider |
| --- |
| [APNS](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/apns) |
| [App.io](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/appio) |
| [Expo](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/expo) |
| [FCM](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/fcm) |
| [OneSignal](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/one-signal) |
| [Push Webhook](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/push-webhook) |
| [Pusher Beams](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/pusher-beams) |
| [Pushpad](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/push/pushpad) |

</details>

<details>
<summary><strong>💬 聊天应用（Chat）</strong> (12 providers)</summary>

| Provider |
| --- |
| [Chat Webhook](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/chat-webhook) |
| [Discord](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/discord) |
| [GetStream](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/getstream) |
| [Grafana OnCall](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/grafana-on-call) |
| [Mattermost](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/mattermost) |
| [Microsoft Teams](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/msTeams) |
| [Rocket.Chat](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/rocket-chat) |
| [Ryver](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/ryver) |
| [Slack](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/slack) |
| [Telegram](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/telegram) |
| [WhatsApp Business](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/whatsapp-business) |
| [Zulip](https://github.com/novuhq/novu/tree/next/packages/providers/src/lib/chat/zulip) |

</details>

<details>
<summary><strong>📥 应用内（In-App）</strong> (1 provider)</summary>

| Provider |
| --- |
| [Novu Inbox](https://docs.novu.co/inbox/react/get-started?utm_source=github&utm_medium=repository&utm_campaign=inbox-channel-link) |

</details>

## 📋 阅读我们的行为准则（Code of Conduct）

在你开始编码和协作之前，请仔细阅读我们的 [行为准则](https://github.com/novuhq/novu/blob/main/CODE_OF_CONDUCT.md)，了解社区参与的标准（你必须遵守的规范）。作为开源社区的一部分，我们以高标准的沟通要求自己和所有贡献者。作为本项目的参与者与贡献者，你同意遵守我们的 [行为准则](https://github.com/novuhq/novu/blob/main/CODE_OF_CONDUCT.md)。

## 💻 需要帮助？

我们非常乐意为你提供支持。如果你在运行或开发本项目时遇到任何报错或问题，欢迎加入我们的 [Discord 服务器](https://discord.novu.co) 寻求帮助。我们开放讨论与项目相关的任何问题。

## 🔗 链接

- [官网首页](https://novu.co?utm_source=github&utm_medium=readme&utm_campaign=main-link)
- [贡献指南](https://github.com/novuhq/novu/blob/main/CONTRIBUTING.md)
- [本地运行 Novu](https://docs.novu.co/community/run-in-local-machine?utm_source=github&utm_medium=readme&utm_campaign=novu-locally-link)

## 🛡️ 许可证

Novu 是一家商业开源公司，这意味着该仓库中的一部分内容需要商业许可证。我们采用“核心开放（Open Core）”模式：核心技术完全开源，遵循 MIT 协议；企业级代码则受商业许可证保护（`/enterprise` 企业版）。企业功能由 Novu 的全职核心团队开发。

以下模块和文件夹采用企业许可证授权：

- 项目根目录下的 `enterprise` 文件夹及其所有子文件夹和模块
- `apps/web/src/ee` 文件夹及其所有子文件夹和模块
- `apps/dashboard/src/ee` 文件夹及其所有子文件夹和模块

## 💪 感谢所有贡献者

感谢你抽出宝贵时间帮助 Novu 成长。继续闪耀吧 🥂

<a href="https://novu.co/contributors?utm_source=github" target="_blank" rel="noopener noreferrer">
  <img src="https://contributors-img.web.app/image?repo=novuhq/novu" alt="Contributors"/>
</a>

精美的头部动画由 [LottieFiles](https://lottiefiles.com/) ❤️ 贡献