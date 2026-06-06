<br />
<img src="https://github.com/OpenBB-finance/OpenBB/blob/develop/images/odp-light.svg?raw=true#gh-light-mode-only" alt="Open Data Platform by OpenBB logo" width="600">
<img src="https://github.com/OpenBB-finance/OpenBB/blob/develop/images/odp-dark.svg?raw=true#gh-dark-mode-only" alt="Open Data Platform by OpenBB logo" width="600">
<br />
<br />

[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/openbb_finance.svg?style=social&label=Follow%20%40openbb_finance)](https://x.com/openbb_finance)
[![Discord Shield](https://img.shields.io/discord/831165782750789672)](https://discord.com/invite/xPHTuHCmuV)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/OpenBB-finance/OpenBB)
<a href="https://codespaces.new/OpenBB-finance/OpenBB">
  <img src="https://github.com/codespaces/badge.svg" height="20" />
</a>
<a target="_blank" href="https://colab.research.google.com/github/OpenBB-finance/OpenBB/blob/develop/examples/googleColab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
[![PyPI](https://img.shields.io/pypi/v/openbb?color=blue&label=PyPI%20Package)](https://pypi.org/project/openbb/)

OpenBB 开源数据平台（Open Data Platform，简称 ODP）是一套开源工具集，帮助数据工程师将专有、授权及公开的数据源集成到 AI Copilot 和研究仪表盘等下游应用中。

ODP 作为“一次连接，处处消费”的基础设施层，将数据整合并统一暴露给多个使用场景：量化人员的 Python 环境、分析师使用的 OpenBB Workspace 和 Excel、AI Agent 的 MCP 服务器，以及其他应用的 REST API。

<a href="https://pro.openbb.co">
  <div align="center">
  <img src="https://openbb-cms.directus.app/assets/70b971ef-7a7e-486e-b5ae-1cc602f2162c.png" alt="Logo" width="1000">
  </div>
</a>

快速开始：执行 `pip install openbb`

```python
from openbb import obb
output = obb.equity.price.historical("AAPL")
df = output.to_dataframe()
```

可用的数据集成列表请参见：<https://docs.openbb.co/python/reference>

---

## OpenBB Workspace

虽然开源数据平台提供了底层的数据集成基础，但 **OpenBB Workspace** 为分析师提供了企业级界面，用于可视化数据集并利用 AI Agent。该平台“一次连接，处处消费”的架构实现了两者之间的无缝集成。

你可以通过 <https://pro.openbb.co> 访问 OpenBB Workspace。
<a href="https://pro.openbb.co">
  <div align="center">
  <img src="https://openbb-cms.directus.app/assets/f69b6aaf-0821-4bc8-a43c-715e03a924ef.png" alt="Logo" width="1000">
  </div>
</a>

数据集成：

- 你可以通过[官方文档](https://docs.openbb.co/workspace)或[此开源仓库](https://github.com/OpenBB-finance/backends-for-openbb)了解如何将数据添加到 OpenBB Workspace。

AI Agent 集成：

- 你可以通过[此开源仓库](https://github.com/OpenBB-finance/agents-for-openbb)了解如何将 AI Agent 添加到 OpenBB Workspace。

### 将 ODP 集成到 OpenBB Workspace

在 Python（3.9.21 - 3.12）环境中，只需几条简单命令即可将此库连接到 OpenBB Workspace。

#### 运行 ODP 后端服务

- 安装依赖包。

```sh
pip install "openbb[all]"
```

- 在本地启动 API 服务器。

```sh
openbb-api
```

这将通过 Uvicorn 在 `127.0.0.1:6900` 启动一个 FastAPI 服务。

你可以通过访问 <http://127.0.0.1:6900> 来验证其是否正常运行。

#### 将 ODP 后端集成到 OpenBB Workspace

登录 [OpenBB Workspace](https://pro.openbb.co/)，并按以下步骤操作：

![CleanShot 2025-05-17 at 09 51 56@2x](https://github.com/user-attachments/assets/75cffb4a-5e95-470a-b9d0-6ffd4067e069)

1. 进入“应用（Apps）”选项卡
2. 点击“连接后端（Connect backend）”
3. 填写表单：
   名称：Open Data Platform
   URL：<http://127.0.0.1:6900>
4. 点击“测试（Test）”。你应该会看到“测试成功”以及找到的应用数量。
5. 点击“添加（Add）”。

完成。

---

<!-- TABLE OF CONTENTS -->
<details closed="closed">
  <summary><h2 style="display: inline-block">目录</h2></summary>
  <ol>
    <li><a href="#1-installation">安装</a></li>
    <li><a href="#2-contributing">贡献指南</a></li>
    <li><a href="#3-license">许可证</a></li>
    <li><a href="#4-disclaimer">免责声明</a></li>
    <li><a href="#5-contacts">联系方式</a></li>
    <li><a href="#6-star-history">Star 历史</a></li>
    <li><a href="#7-contributors">贡献者</a></li>
  </ol>
</details>

## 1. 安装

你可以通过运行 `pip install openbb` 从 [PyPI 包](https://pypi.org/project/openbb/)安装 ODP Python 软件包，或直接使用 `git clone https://github.com/OpenBB-finance/OpenBB.git` 克隆仓库。

有关安装过程的更多信息，请参见[OpenBB 官方文档](https://docs.openbb.co/python/installation)。

### ODP CLI（命令行界面）安装

ODP CLI 是一个命令行工具，允许你直接从终端访问 ODP。

你可以通过运行 `pip install openbb-cli` 安装它，或直接克隆仓库：`git clone https://github.com/OpenBB-finance/OpenBB.git`。

有关 CLI 安装的更多信息，请参见[OpenBB 官方文档](https://docs.openbb.co/cli/installation)。

## 2. 贡献指南

参与本项目主要有三种方式。（希望你现在已经给项目点了星标 ⭐️）

### 成为代码贡献者

- 更多详情请查阅[开发者文档](https://docs.openbb.co/python/developer)。

### 提交 GitHub Issue

在创建新 Issue 前，请确保它尚未存在于[现有问题列表](https://github.com/OpenBB-finance/OpenBB/issues)中。

- [报告 Bug](https://github.com/OpenBB-finance/OpenBB/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBug%5D)
- [建议改进](https://github.com/OpenBB-finance/OpenBB/issues/new?assignees=&labels=enhancement&template=enhancement.md&title=%5BIMPROVE%5D)
- [功能请求](https://github.com/OpenBB-finance/OpenBB/issues/new?assignees=&labels=new+feature&template=feature_request.md&title=%5BFR%5D)

### 提供反馈

我们在 [Discord](https://openbb.co/discord) 上最为活跃，但也欢迎通过[任何社交媒体渠道](https://openbb.co/links)向我们提供反馈。

## 3. 许可证

本项目采用 AGPLv3 许可证分发。更多信息请参见
[LICENSE](https://github.com/OpenBB-finance/OpenBB/blob/main/LICENSE)。

## 4. 免责声明

金融工具交易涉及高风险，包括可能损失部分或全部投资金额的风险，且未必适合所有投资者。

在决定交易金融工具前，你应充分了解与金融市场交易相关的风险和成本，仔细考虑你的投资目标、经验水平及风险承受能力，并在必要时寻求专业建议。

开源数据平台（Open Data Platform）中的数据未必完全准确。

对于因你的交易行为或依赖本平台显示的信息而导致的任何损失或损害，OpenBB 及任何数据提供商均不承担责任。

本站、产品或文档中提及的所有第三方名称、标志和品牌均为其各自所有者的商标。除非另有说明，OpenBB 及其产品和服务未得到这些第三方的认可、赞助或关联。

我们使用这些名称、标志和品牌仅用于识别目的，并不暗示任何此类认可、赞助或关联关系。

## 5. 联系方式

如果你有关于平台或 OpenBB 的任何问题，欢迎发送邮件至 `support@openbb.co`

如果你想打个招呼，或有合作意向，欢迎联系 `hello@openbb.co`

我们的所有社交媒体平台：[openbb.co/links](https://openbb.co/links)

## 6. Star 历史

这反映了我们的成长历程，也标志着我们才刚刚开始。

如需查看更多对我们重要的指标，请访问 [openbb.co/open](https://openbb.co/open)。

[![Star History Chart](https://api.star-history.com/svg?repos=openbb-finance/OpenBB&type=Date&theme=dark)](https://api.star-history.com/svg?repos=openbb-finance/OpenBB&type=Date&theme=dark)

## 7. 贡献者

没有你，就没有今天的 OpenBB。如果我们旨在颠覆金融行业，每一份贡献都至关重要。感谢你成为这段旅程的一部分。

<a href="https://github.com/OpenBB-finance/OpenBB/graphs/contributors">
   <img src="https://contributors-img.web.app/image?repo=OpenBB-finance/OpenBB" width="800"/>
</a>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/OpenBB-finance/OpenBB.svg?style=for-the-badge
[contributors-url]: https://github.com/OpenBB-finance/OpenBB/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/OpenBB-finance/OpenBB.svg?style=for-the-badge
[forks-url]: https://github.com/OpenBB-finance/OpenBB/network/members
[stars-shield]: https://img.shields.io/github/stars/OpenBB-finance/OpenBB.svg?style=for-the-badge
[stars-url]: https://github.com/OpenBB-finance/OpenBB/stargazers
[issues-shield]: https://img.shields.io/github/issues/OpenBB-finance/OpenBB.svg?style=for-the-badge&color=blue
[issues-url]: https://github.com/OpenBB-finance/OpenBB/issues
[bugs-open-shield]: https://img.shields.io/github/issues/OpenBB-finance/OpenBB/bug.svg?style=for-the-badge&color=yellow
[bugs-open-url]: https://github.com/OpenBB-finance/OpenBB/issues?q=is%3Aissue+label%3Abug+is%3Aopen
[bugs-closed-shield]: https://img.shields.io/github/issues-closed/OpenBB-finance/OpenBB/bug.svg?style=for-the-badge&color=success
[bugs-closed-url]: https://github.com/OpenBB-finance/OpenBB/issues?q=is%3Aissue+label%3Abug+is%3Aclosed
[license-shield]: https://img.shields.io/github/license/OpenBB-finance/OpenBB.svg?style=for-the-badge
[license-url]: https://github.com/OpenBB-finance/OpenBB/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/DidierRLopes