![Huginn](https://raw.github.com/huginn/huginn/master/media/huginn-logo.png "Your agents are standing by.")

-----

## Huginn 是什么？

Huginn 是一个用于构建智能体（Agent）的系统，这些智能体可以为你在线执行自动化任务。它们能够浏览网页、监控事件，并代表你采取操作。Huginn 的 Agent 会创建和消费（处理）事件，并通过有向图将它们传递下去。你可以把它看作是在你自己的服务器上运行的、可自由定制的 IFTTT 或 Zapier。你始终清楚谁掌握着你的数据。没错，就是你。

![the origin of the name](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/the-name.png)

#### 你可以使用 Huginn 实现以下功能：

* 追踪天气，并在明天有雨（或雪）时收到邮件提醒（“别忘了带伞！”）
* 列出你关注的关键词，当它们在 Twitter 上的出现频率发生变化时接收邮件。（例如，想了解机器学习领域发生了什么有趣的事？Huginn 会监控 Twitter 上关于“machine learning”的讨论，并在话题热度飙升时通知你。）
* 监控机票或购物优惠信息
* 在 Twitter 上关注你的项目名，当有人提及它们时获取更新
* 抓取网站内容，并在网页发生变化时接收邮件通知
* 连接 HipChat、FTP、IMAP、Jabber、JIRA、MQTT、nextbus、Pushbullet、Pushover、RSS、Bash、Slack、StubHub、翻译 API、Twilio、Twitter 和微博等（仅列举部分）
* 在每天特定时间发送包含你关注内容的摘要邮件
* 追踪高频事件的数量，并在其突然飙升时立即发送短信通知（例如“san francisco emergency”关键词）
* 发送和接收 WebHooks
* 运行自定义的 JavaScript 函数
* 随时间追踪你的位置信息
* 创建亚马逊机械工（Amazon Mechanical Turk）工作流，作为 Agent 的输入或输出（该智能体名为“HumanTaskAgent”）。例如：“每天询问 5 个人要一张有趣的猫照片；将结果发给另外 5 人进行评分；将评分最高的照片发给 5 人征集有趣配文；最后再交给 5 人评选最佳配文；最终，将最佳配文的照片发布到我的博客上。”

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/huginn/huginn?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Changelog #199](https://img.shields.io/badge/changelog-%23199-lightgrey.svg)](https://changelog.com/podcast/199)

欢迎加入我们的 [Gitter 频道](https://gitter.im/huginn/huginn) 讨论项目。

### 加入我们！

想要为 Huginn 贡献力量吗？我们非常欢迎任何形式的贡献！你可以改进用户界面、[添加新的 Agent](https://github.com/huginn/huginn/wiki/Creating-a-new-agent)、编写[文档和教程](https://github.com/huginn/huginn/wiki)，或者尝试解决[标记为“需要帮助”的 Issue](https://github.com/huginn/huginn/issues?direction=desc&labels=help+wanted&page=1&sort=created&state=open)。请 Fork 项目、补充测试用例，然后提交 Pull Request！

有绝妙的主意但暂时不想亲自参与开发？欢迎前往我们的[官方“推荐智能体”讨论帖](https://github.com/huginn/huginn/issues/353)告诉我们！

## 示例演示

请观看 [Huginn 入门录屏教程](http://vimeo.com/61976251)!

接下来是一些示例截图。下方附有操作指南，助你快速上手。

![Example list of agents](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/your-agents.png)

![Event flow diagram](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/diagram.png)

![Detecting peaks in Twitter](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/peaks.png)

![Logging your location over time](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/my-locations.png)

![Making a new agent](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/new-agent.png)

## 快速开始

### Docker

体验 Huginn 最快、最简单的方式是使用官方 Docker 镜像。请查看[相关文档](https://github.com/huginn/huginn/blob/master/doc/docker/install.md)。

### 本地安装

如果你只是想先体验一下，可以直接 Fork 本仓库，然后执行以下步骤：

* 运行 `git remote add upstream https://github.com/huginn/huginn.git` 将主仓库添加为 Fork 的远程源。
* 复制 `.env.example` 到 `.env`（执行 `cp .env.example .env`）并编辑 `.env`，至少更新 `APP_SECRET_TOKEN` 变量。
* 确保已安装 MySQL 或 PostgreSQL。（在 Mac 上，使用 [Homebrew](http://brew.sh/) 是最简单的方式。如果你打算使用 PostgreSQL，需要在后续所有命令前加上 `DATABASE_ADAPTER=postgresql`。）
* 运行 `bundle` 安装依赖项。
* 依次运行 `bundle exec rake db:create`、`bundle exec rake db:migrate`，然后执行 `bundle exec rake db:seed`，以创建一个包含示例 Agent 的数据库。
* 运行 `bundle exec foreman start`，访问 [http://localhost:3000/][localhost]，并使用用户名 `admin` 和密码 `password` 登录。
* 配置一些 Agent！
* 阅读[维基文档][wiki]获取使用示例，并学习如何创建新的 Agent。
* 定期运行 `git fetch upstream`，然后执行 `git checkout master && git merge upstream/master` 以合并 Huginn 的最新版本。

**注意**：默认情况下，邮件消息会在 Rails 的 `development`（开发）环境中被拦截捕获，这正是你刚才搭建的环境。你可以在 [http://localhost:3000/letter_opener](http://localhost:3000/letter_opener) 查看它们。如果你想在本地运行 Huginn 时通过 SMTP 发送真实邮件，请在 `.env` 文件中将 `SEND_EMAIL_IN_DEVELOPMENT` 设置为 `true`。

如果需要更详细的指导，请参阅[新手设置指南][novice-setup-guide]。

[localhost]: http://localhost:3000/
[wiki]: https://github.com/huginn/huginn/wiki
[novice-setup-guide]: https://github.com/huginn/huginn/wiki/Novice-setup-guide

### 本地开发

所有 Agent 都配有测试用例（specs）！此外还有验收测试，用于在无头浏览器中模拟运行 Huginn。

* 安装 Google Chrome 和 ChromeDriver 以支持本地功能测试
* 或使用 [`docker/test/README.md`](docker/test/README.md) 中基于 Docker 的测试环境
* 运行 `bundle exec rspec` 执行全部测试用例
* 运行 `bundle exec rspec path/to/specific/test_spec.rb` 执行特定测试用例
* 了解更多关于 Rails 的 RSpec 信息请[点击这里](https://github.com/rspec/rspec-rails)。

## 使用外部 Agent Gems

Huginn 的智能体现在可以编写为外部 Gems，并通过 `ADDITIONAL_GEMS` 环境变量添加到你的 Huginn 安装中。更多信息请查看 `.env.example` 中的 `Additional Agent gems` 部分。

如果你想编写自己的 Huginn Agent Gem，请参阅 [huginn_agent](https://github.com/huginn/huginn_agent)。

我们的总体思路是：鼓励将复杂且特定用途的智能体编写为独立 Gem，同时继续在核心仓库中新增通用型智能体。

## 部署指南

请参阅[Huginn 维基文档](https://github.com/huginn/huginn/wiki#deploying-huginn)获取针对不同服务商的详细部署策略。

### Heroku

在 Heroku 上体验 Huginn：[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)（部署需要几分钟。等待期间请阅读[文档](https://github.com/huginn/huginn/blob/master/doc/heroku/install.md)，启动后务必点击“View it”！）Huginn 在 Heroku 上仅支持付费订阅计划运行。若非测试用途，我们强烈建议使用 Heroku 的 1GB 付费套餐或我们的 Docker 容器。

### OpenShift

#### OpenShift Online

在 OpenShift Online 上体验 Huginn

使用 `mysql` 或 `postgres` 创建新应用：
```bash
oc new-app -f https://raw.githubusercontent.com/huginn/huginn/master/openshift/templates/huginn-mysql.json
```
或
```bash
oc new-app -f https://raw.githubusercontent.com/huginn/huginn/master/openshift/templates/huginn-postgresql.json
```
**注意**：你也可以通过 Web 控制台导入任意 JSON 文件，路径为“添加至项目（Add to Project）”->“导入 YAML/JSON”。

如果你使用的是 Starter 套餐，请务必按照[指南](https://docs.openshift.com/online/getting_started/beyond_the_basics.html#btb-creating-a-new-application-from-source-code)操作以移除任何现有应用。

这些模板适用于 v3 版本安装或当前的 v4 Online 环境。

### 在任何服务器上手动安装

请查看[安装指南](https://github.com/huginn/huginn/blob/master/doc/manual/README.md)。

### 可选配置

#### 私有开发环境设置

请参阅维基上的[私有开发说明](https://github.com/huginn/huginn/wiki/Private-development-instructions)。

#### 启用 WeatherAgent

要使用 WeatherAgent，你需要获取[Pirate Weather 的天气数据 API Key](https://pirate-weather.apiable.io/products/weather-data)。注册后，请在种子数据生成的 WeatherAgent 中将 `api_key: your-key` 的值修改为你的密钥。

#### 禁用 SSL

我们默认你的部署将运行在 SSL 之上。这是一个非常好的建议！但如果确实需要关闭，你可能需要编辑 `config/initializers/devise.rb`，修改包含 `config.rememberable_options = { :secure => true }` 的那一行。同时，你还需要编辑 `config/environments/production.rb`，并将 `config.force_ssl` 的值进行修改（通常设为 false）。

## 许可证

Huginn 基于 MIT 许可证提供。

Huginn 最初由 [@cantino](https://github.com/cantino) 于 2013 年创建。此后，众多开发者的无私奉献使其发展成为今天的样子。

[![CI](https://github.com/huginn/huginn/actions/workflows/ci.yml/badge.svg)](https://github.com/huginn/huginn/actions/workflows/ci.yml) [![Coverage Status](https://coveralls.io/repos/huginn/huginn/badge.svg)](https://coveralls.io/r/huginn/huginn)