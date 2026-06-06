[![PyPI version](https://img.shields.io/pypi/v/ansible-core.svg)](https://pypi.org/project/ansible-core)
[![Docs badge](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://docs.ansible.com/ansible/latest/)
[![Chat badge](https://img.shields.io/badge/chat-Matrix-brightgreen.svg)](https://docs.ansible.com/ansible/devel/community/communication.html#real-time-chat)
[![Ansible forum](https://img.shields.io/badge/forum-Ansible-orange.svg)](https://docs.ansible.com/ansible/devel/community/communication.html#forum)
[![Build Status](https://dev.azure.com/ansible/ansible/_apis/build/status/CI?branchName=devel)](https://dev.azure.com/ansible/ansible/_build/latest?definitionId=20&branchName=devel)
[![Ansible Code of Conduct](https://img.shields.io/badge/code%20of%20conduct-Ansible-silver.svg)](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
[![Repository License](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)][copying]
[![Ansible CII Best Practices certification](https://bestpractices.coreinfrastructure.org/projects/2372/badge)](https://bestpractices.coreinfrastructure.org/projects/2372)

# Ansible

Ansible 是一个极其简洁的 IT 自动化工具。它负责配置管理、应用部署、云资源供应、临时任务执行、网络自动化以及多节点编排。借助负载均衡器，Ansible 让零停机滚动更新等复杂变更变得轻而易举。更多信息请访问 Ansible [官网](https://ansible.com/)。

## 设计原则

* 提供极其简单的安装配置流程，学习曲线平缓。
* 快速且并行地管理多台主机。
* 避免使用自定义代理或开放额外端口，通过利用现有的 `SSH` 守护进程实现无代理（agentless）架构。
* 使用一种既便于机器解析又符合人类阅读习惯的语言来描述基础设施。
* 注重安全性，并支持内容易于审计、审查和重写。
* 即时管理新远程主机，无需预先引导安装任何软件。
* 允许使用任意动态语言（不仅限于 Python）进行模块开发。
* 支持非 root 权限用户运行。
* 致力于成为有史以来最易用的 IT 自动化工具。

## 使用 Ansible

你可以通过 `pip` 或包管理器安装已发布的 Ansible 版本。有关在多种平台上安装 Ansible 的详细信息，请参阅我们的[安装指南](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)。

高级用户和开发者可以直接运行包含最新功能与修复的 `devel` 分支。尽管该分支相对稳定，但在运行时你更有可能遇到破坏性更新（breaking changes）。如果你打算运行 `devel` 分支，我们建议你积极参与 Ansible 社区。

## 交流

加入 Ansible 论坛提问、获取帮助并与社区互动。

* [获取帮助](https://forum.ansible.com/c/help/6)：寻找解答或分享你的 Ansible 知识以帮助他人。使用标签过滤和订阅帖子，例如：
  * 带有 [ansible](https://forum.ansible.com/tag/ansible) 标签的帖子
  * 带有 [ansible-core](https://forum.ansible.com/tag/ansible-core) 标签的帖子
  * 带有 [playbook](https://forum.ansible.com/tag/playbook) 标签的帖子
* [社交空间](https://forum.ansible.com/c/chat/4)：结识并与其他爱好者交流。
* [新闻与公告](https://forum.ansible.com/c/news/5)：跟踪项目范围的公告，包括社交活动。
* [Bullhorn 通讯](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn)：获取版本发布公告和重要变更通知。

如需更多联系方式，请参阅[与 Ansible 社区交流](https://docs.ansible.com/ansible/devel/community/communication.html)。

## 参与贡献

* 查阅[贡献者指南](https://github.com/ansible/ansible/blob/devel/.github/CONTRIBUTING.md)。
* 阅读[社区信息](https://docs.ansible.com/ansible/devel/community)，了解参与项目及与项目互动的各种方式，包括如何提交 bug 报告和代码。
* 通过向 `devel` 分支发起 Pull Request（PR）来提交代码更新建议。
* 在进行较大范围的修改前请先与我们沟通，以避免重复劳动。这不仅能让大家了解进展，也能在我们需要某些变更时节省时间精力。

## 编码规范

我们的[开发者指南](https://docs.ansible.com/ansible/devel/dev_guide/)中详细记录了编码规范。我们特别建议你查阅以下内容：

* [将你的模块贡献给 Ansible](https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_checklist.html)
* [惯例、技巧与常见陷阱](https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_best_practices.html)

## 分支说明

* `devel` 分支对应当前正在积极开发中的版本。
* `stable-2.X` 分支对应稳定发布版。
* 如需提交 PR，请基于 `devel` 创建分支并配置[开发环境](https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_general.html#common-environment-setup)。
* 有关活跃分支的详细信息，请参阅 [Ansible 版本与维护](https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html) 页面。

## 路线图

根据团队与社区反馈，将为大版本或小版本（例如 2.7、2.8）发布初始路线图。[Ansible 路线图](https://docs.ansible.com/ansible/devel/roadmap/)页面详细说明了计划内容以及如何参与路线图的制定。

## 作者

Ansible 由 [Michael DeHaan](https://github.com/mpdehaan) 创建，并得到了超过 5000 名用户的贡献（且人数仍在增长）。感谢大家！

本项目绝大部分由人类亲手编码实现。

[Ansible](https://www.ansible.com) 由 [Red Hat, Inc.](https://www.redhat.com) 赞助。

## 许可证

GNU 通用公共许可证 v3.0 或更高版本

完整文本请参阅 [COPYING]。

[copying]: https://github.com/ansible/ansible/blob/devel/COPYING