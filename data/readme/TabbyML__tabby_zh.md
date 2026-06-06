<div align="center">
  
# 🐾 Tabby

[📚 Docs](https://tabby.tabbyml.com/docs/welcome/) • [💬 Slack](https://links.tabbyml.com/join-slack) • [🗺️ Roadmap](https://tabby.tabbyml.com/docs/roadmap/)

[![latest release](https://shields.io/github/v/release/TabbyML/tabby)](https://github.com/TabbyML/tabby/releases/latest)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![Docker pulls](https://img.shields.io/docker/pulls/tabbyml/tabby)](https://hub.docker.com/r/tabbyml/tabby)
[![codecov](https://codecov.io/gh/TabbyML/tabby/graph/badge.svg?token=WYVVH8MKK3)](https://codecov.io/gh/TabbyML/tabby)

[English](/README.md) |
[简体中文](/README-zh.md) |
[日本語](/README-ja.md)

</div>

Tabby 是一款自托管的 AI 编程助手，提供开源且支持本地部署的方案，作为 GitHub Copilot 的替代选择。它具备以下核心特性：
* 独立运行（Self-contained），无需依赖数据库管理系统（DBMS）或云服务。
* 提供 OpenAPI 接口，易于集成到现有基础设施中（例如云 IDE）。
* 支持消费级 GPU。

<p align="center">
  <a target="_blank" href="https://tabby.tabbyml.com"><img alt="Open Live Demo" src="https://img.shields.io/badge/OPEN_LIVE_DEMO-blue?logo=xcode&style=for-the-badge&logoColor=green"></a>
</p>

<p align="center">
  <img alt="Demo" src="https://user.githubusercontent.com/388154/230440226-9bc01d05-9f57-478b-b04d-81184eba14ca.gif">
</p>

## 🔥 最新动态
* **12/12/2025** 通过将 GitHub Issue 关联到 [Pochi](https://github.com/TabbyML/pochi) 任务，并直接从侧边栏创建 PR（附带 CI/Lint/Test 结果详情），让你的 Issue 得到实现！[vscode@0.20.0](https://github.com/TabbyML/pochi/releases/tag/vscode%400.20.0)。
* **07/02/2025** [v0.30](https://github.com/TabbyML/tabby/releases/tag/v0.30.0) 支持将 GitLab 合并请求（Merge Request）作为上下文进行索引！ 
* **05/25/2025** 💡 有兴趣加入 [Agent](https://links.tabbyml.com/pochi-github-readme) 私密预览吗？在 [X](https://x.com/getpochi) 上私信获取早期候补名单资格！🎫
* **05/20/2025** 通过 [v0.29](https://github.com/TabbyML/tabby/releases/tag/v0.29.0) 中的 REST API，使用你自己的文档📃来增强 Tabby！ 🎉
* **05/01/2025** [v0.28](https://github.com/TabbyML/tabby/releases/tag/v0.28.0) 将回答引擎（Answer Engine）的消息转换为持久化、可共享的页面
* **03/31/2025** 发布 [v0.27](https://github.com/TabbyML/tabby/releases/tag/v0.27.0)，聊天侧边板中的 `@` 菜单功能更加丰富。


<details>
  <summary>归档更新</summary>

* **02/05/2025** Tabby [v0.24.0](https://github.com/TabbyML/tabby/releases/tag/v0.24.0) 带来 LDAP 认证功能以及更完善的后台任务通知！✨
* **02/04/2025** [VS Code 1.20.0](https://marketplace.visualstudio.com/items/TabbyML.vscode-tabby/changelog) 升级！支持通过 @提及文件将其添加为聊天上下文，并可通过新增的右键选项进行内联编辑！
* **01/10/2025** Tabby [v0.23.0](https://github.com/TabbyML/tabby/releases/tag/v0.23.0) 带来更优的代码浏览器体验和聊天侧边板改进！
* **12/24/2024** Tabby [v0.22.0](https://github.com/TabbyML/tabby/releases/tag/v0.22.0) 引入**通知中心（Notification Box）**！
* **12/06/2024** Llamafile 部署集成与增强的回答引擎（Answer Engine）用户体验即将登陆 Tabby [v0.21.0](https://github.com/TabbyML/tabby/releases/tag/v0.21.0)！🚀
* **11/10/2024** 通过 Tabby [v0.20.0](https://github.com/TabbyML/tabby/releases/tag/v0.20.0)，回答引擎（Answer Engine）现已支持切换不同的后端聊天模型！
* **10/30/2024** Tabby [v0.19.0](https://github.com/TabbyML/tabby/releases/tag/v0.19.0) 在主页面展示最近共享的对话线程，提升查找效率。 
* **07/09/2024** 🎉 宣布 [Tabby 集成 Codestral](https://tabby.tabbyml.com/blog/2024/07/09/tabby-codestral/)！
* **07/05/2024** Tabby [v0.13.0](https://github.com/TabbyML/tabby/releases/tag/v0.13.0) 推出***回答引擎（Answer Engine）***，这是专为内部工程团队打造的核心知识引擎。它能无缝集成开发团队的内部数据，提供准确可靠的解答以赋能开发者。
* **06/13/2024** [VS Code 1.7](https://marketplace.visualstudio.com/items/TabbyML.vscode-tabby/changelog) 带来重要里程碑式的多功能聊天体验，贯穿你的整个编码过程。快来体验最新的**侧边栏聊天（chat in side-panel）**和**通过聊天命令进行编辑（editing via chat command）**功能吧！
* **06/10/2024** 最新博客文章发布，探讨 Tabby 中[增强的代码上下文理解能力](https://tabby.tabbyml.com/blog/2024/06/11/rank-fusion-in-tabby-code-completion/)！
* **06/06/2024** Tabby [v0.12.0](https://github.com/TabbyML/tabby/releases/tag/v0.12.0) 发布，带来🔗**无缝集成**（GitLab SSO、自托管 GitHub/GitLab 等）、⚙️**灵活配置**（HTTP API 集成）以及 🌐**功能扩展**（代码浏览器中的仓库上下文）！ 
* **05/22/2024** Tabby [VS Code 1.6](https://marketplace.visualstudio.com/items?itemName=TabbyML.vscode-tabby) 支持内联补码的**多选项（multiple choices）**，以及**自动生成提交信息（commit messages）**🐱💻！
* **05/11/2024** [v0.11.0](https://github.com/TabbyML/tabby/releases/tag/v0.11.0) 带来重大企业级升级，包括 📊**存储用量统计**、🔗**GitHub & GitLab** 集成、📋**活动（Activities）**页面，以及备受期待的 🤖**Ask Tabby** 功能！
* **04/22/2024** [v0.10.0](https://github.com/TabbyML/tabby/releases/tag/v0.10.0) 发布，新增最新的**报表（Reports）**标签页，提供团队维度的 Tabby 使用分析。
* **04/19/2024** 📣 Tabby 现已集成[本地相关代码片段](https://github.com/TabbyML/tabby/pull/1844)（来自本地 LSP 的声明及最近修改的代码）以用于代码补全！
* **04/17/2024** CodeGemma 和 CodeQwen 模型系列现已加入[官方注册表](https://tabby.tabbyml.com/docs/models/)！
* **03/20/2024** 发布 [v0.9](https://github.com/TabbyML/tabby/releases/tag/v0.9.1)，主打功能完善的管理员界面（Admin UI）。
* **12/23/2023** 借助 SkyPilot 的 [SkyServe](https://skypilot.readthedocs.io/en/latest/serving/sky-serve.html)，轻松[将 Tabby 部署到任意云平台](https://tabby.tabbyml.com/docs/installation/skypilot/) 🛫。
* **12/15/2023** 发布 [v0.7.0](https://github.com/TabbyML/tabby/releases/tag/v0.7.0)，新增团队管理与安全访问控制！
* **10/15/2023** [v0.3.0](https://github.com/TabbyML/tabby/releases/tag/v0.3.0) 默认启用了基于 RAG（检索增强生成）的代码补全功能🎉！查看[博客文章](https://tabby.tabbyml.com/blog/2023/10/16/repository-context-for-code-completion/)了解 Tabby 如何利用仓库级上下文变得更智能！
* **11/27/2023** 发布 [v0.6.0](https://github.com/TabbyML/tabby/releases/tag/v0.6.0)！
* **11/09/2023** 发布 [v0.5.5](https://github.com/TabbyML/tabby/releases/tag/v0.5.5)！伴随界面重构与性能提升。
* **10/24/2023** ⛳️ Tabby IDE 插件在 [VS Code / Vim / IntelliJ](https://tabby.tabbyml.com/docs/extensions) 上迎来重大更新！
* **10/04/2023** 查看[模型目录](https://tabby.tabbyml.com/docs/models/)，了解 Tabby 支持的最新模型。
* **09/18/2023** Apple M1/M2 Metal 推理支持已登陆 [v0.1.1](https://github.com/TabbyML/tabby/releases/tag/v0.1.1)！
* **08/31/2023** Tabby 首个稳定版本 [v0.0.1](https://github.com/TabbyML/tabby/releases/tag/v0.0.1) 发布 🥳。
* **08/28/2023** 提供对 [CodeLlama 7B](https://github.com/TabbyML/tabby/issues/370) 的实验性支持。
* **08/24/2023** Tabby 现已上架 [JetBrains 插件市场](https://plugins.jetbrains.com/plugin/22379-tabby)!

</details>

## 👋 快速开始

你可以在[这里](https://tabby.tabbyml.com/docs/getting-started)查阅我们的文档。
- 📚 [安装指南](https://tabby.tabbyml.com/docs/installation/)
- 💻 [IDE/编辑器扩展](https://tabby.tabbyml.com/docs/extensions/)
- ⚙️ [配置说明](https://tabby.tabbyml.com/docs/configuration)

### 1 分钟运行 Tabby
启动 Tabby 服务器最简单的方法是使用以下 Docker 命令：

```bash
docker run -it \
  --gpus all -p 8080:8080 -v $HOME/.tabby:/data \
  tabbyml/tabby \
  serve --model StarCoder-1B --device cuda --chat-model Qwen2-1.5B-Instruct
```
如需更多选项（例如推理类型、并行度等），请参阅[文档页面](https://tabbyml.github.io/tabby)。

## 🤝 贡献指南

完整指南请参见 [CONTRIBUTING.md](https://github.com/TabbyML/tabby/blob/main/CONTRIBUTING.md)；

### 获取代码

```bash
git clone --recurse-submodules https://github.com/TabbyML/tabby
cd tabby
```

如果你已经克隆了仓库，可以运行 `git submodule update --recursive --init` 命令来获取所有子模块。

### 编译构建

1. 按照本[教程](https://www.rust-lang.org/learn/get-started)配置 Rust 开发环境。

2. 安装所需的依赖项：
```bash
# For MacOS
brew install protobuf

# For Ubuntu / Debian
apt install protobuf-compiler libopenblas-dev
```

3. 安装常用工具：
```bash
# For Ubuntu
apt install make sqlite3 graphviz
```

4. 现在，运行 `cargo build` 命令即可编译 Tabby。

### 开始开发！
... 别忘了提交 [Pull Request](https://github.com/TabbyML/tabby/compare)

## 🌍 社区
- 🎤 [Twitter / X](https://twitter.com/Tabby_ML) - 关注 TabbyML，探索一切可能 
- 📚 [LinkedIn](https://www.linkedin.com/company/tabbyml/) - 获取社区最新动态 
- 💌 [Newsletter](https://newsletter.tabbyml.com/archive) - 订阅以解锁 Tabby 的深度洞察与独家资讯

### 🔆 活跃度

![Git Repository Activity](https://repobeats.axiom.co/api/embed/e4ef0fbd12e586ef9ea7d72d1fb4f5c5b88d78d5.svg "Repobeats analytics image")

### 🌟 星标历史

[![Star History Chart](https://api.star-history.com/svg?repos=tabbyml/tabby&type=Date)](https://star-history.com/#tabbyml/tabby&Date)