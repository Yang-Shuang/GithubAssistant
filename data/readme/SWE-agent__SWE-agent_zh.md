<p align="center">
  <a href="https://swe-agent.com/latest/">
    <img src="assets/swe-agent-banner.png" alt="swe-agent.com" style="height: 7em" />
  </a>
</p>

<p align="center">
<a href="https://swe-agent.com/latest/"><img src="https://img.shields.io/badge/Docs-green?style=for-the-badge&logo=materialformkdocs&logoColor=white" alt="Docs"></a>
<a href="https://swe-bench.slack.com"><img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white" alt="Slack"></a>
<a href="https://arxiv.org/abs/2405.15793"><img src="https://img.shields.io/badge/arxiv-2405.15793-red?style=for-the-badge&logo=arxiv&logoColor=white&labelColor=black" alt="arxiv 2405.15793"></a>
</p>

<p align="center">
  <a href="https://github.com/SWE-agent/mini-swe-agent/">
    <img src="assets/warning.png" alt="mini-swe-agent.com" style="height: 7em" />
  </a>
</p>

> [!warning]
> 我们目前的大部分开发工作都集中在 [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent/) 上，它已取代 SWE-agent。它在保持与 SWE-agent 同等性能的同时，架构更加简洁。有关两者差异的更多详情，请参阅 [FAQ](https://mini-swe-agent.com/latest/faq/)。我们建议今后直接使用 mini-SWE-agent 替代 SWE-agent。


SWE-agent 允许你选择任意的语言模型（例如 GPT-4o 或 Claude Sonnet 4），使其能够自主调用工具来：
[修复真实 GitHub 仓库中的问题](https://swe-agent.com/latest/usage/hello_world)、
[发现网络安全漏洞](https://enigma-agent.com/)，或
[执行任何自定义任务](https://swe-agent.com/latest/usage/coding_challenges)。

* ✅ **开源项目中的顶尖性能**：在 SWE-bench 基准测试中表现优异
* ✅ **自由流畅且易于泛化**：将最大程度的自主权留给语言模型（LM）
* ✅ **可配置且文档齐全**：由单个 `yaml` 文件统一管理
* ✅ **专为研究设计**：架构简单，易于修改和扩展

SWE-agent 由普林斯顿大学和斯坦福大学的研究人员构建并维护。

## 📣 最新动态

* 7月24日：[Mini-SWE-Agent](https://github.com/SWE-agent/mini-swe-agent) 仅用 100 行 Python 代码，就在 SWE-bench verified 上达到 65% 的得分！
* 5月2日：[SWE-agent-LM-32b](https://github.com/SWE-bench/SWE-smith) 在 SWE-bench 上创下开源权重模型的最优成绩（SoTA）
* 2月28日：[SWE-agent 1.0 + Claude 3.7 在 SWE-Bench full 上达到最优成绩](https://x.com/KLieret/status/1895487966409298067)
* 2月25日：[SWE-agent 1.0 + Claude 3.7 在 SWE-bench verified 上达到最优成绩](https://x.com/KLieret/status/1894408819670733158)
* 2月13日：[发布 SWE-agent 1.0：SWE-bench light 最优成绩及大量新功能](https://x.com/KLieret/status/1890048205448220849)
* 12月7日：[专访 SWE-agent & SWE-bench 团队](https://www.youtube.com/watch?v=fcr8WzeEXyk)

## 🚀 快速开始！

👉 在浏览器中体验 SWE-agent：[![Open in GitHub Codespaces](https://img.shields.io/badge/Open_in_GitHub_Codespaces-gray?logo=github)](https://codespaces.new/SWE-agent/SWE-agent) ([更多信息](https://swe-agent.com/latest/installation/codespaces/))

阅读我们的[文档][docs]了解更多：

* [安装指南](https://swe-agent.com/latest/installation/source/)
* [命令行 Hello World](https://swe-agent.com/latest/usage/hello_world/)
* [在 SWE-bench 上进行基准测试](https://swe-agent.com/latest/usage/batch_mode/)
* [常见问题解答 (FAQ)](https://swe-agent.com/latest/faq/)

[docs]: https://swe-agent.com

## SWE-agent 用于进攻性网络安全（EnIGMA） <a name="enigma"></a>

<img src="https://github.com/user-attachments/assets/84599168-11a7-4776-8a49-33dbf0758bb2" height="80px"></img>

[SWE-agent: EnIGMA][enigma] 是一种用于解决进攻性网络安全（Capture The Flag, CTF）挑战的模式。
EnIGMA 在多项网络安全基准测试中均取得了顶尖成绩（详见[排行榜](https://enigma-agent.com/#results)）。
在我们将 EnIGMA 更新至 1.0 版本期间，请使用 [SWE-agent 0.7](https://github.com/SWE-agent/SWE-agent/tree/v0.7)。

[enigma]: https://enigma-agent.com
[SWE-bench]: https://github.com/SWE-bench/SWE-bench
[nyu-ctf]: https://arxiv.org/abs/2406.05590

此外，你可能还会对我们其他的项目感兴趣：


<div align="center">
  <a href="https://github.com/SWE-agent/mini-SWE-agent"><img src="docs/assets/mini_logo_text_below.svg" alt="Mini-SWE-Agent" height="120px"></a>
   &nbsp;&nbsp;
  <a href="https://github.com/SWE-agent/SWE-ReX"><img src="docs/assets/swerex_logo_text_below.svg" alt="SWE-ReX" height="120px"></a>
   &nbsp;&nbsp;
  <a href="https://github.com/SWE-bench/SWE-bench"><img src="docs/assets/swebench_logo_text_below.svg" alt="SWE-bench" height="120px"></a>
  &nbsp;&nbsp;
  <!-- <a href="https://github.com/SWE-agent/SWE-agent"><img src="docs/assets/sweagent_logo_text_below.svg" alt="SWE-agent" height="120px"></a> -->
  <a href="https://github.com/SWE-bench/SWE-smith"><img src="docs/assets/swesmith_logo_text_below.svg" alt="SWE-smith" height="120px"></a>
  &nbsp;&nbsp;
  <a href="https://github.com/SWE-bench/sb-cli"><img src="docs/assets/sbcli_logo_text_below.svg" alt="sb-cli" height="120px"></a>
</div>

## 贡献代码 <a name="contributions"></a>

如果你希望为代码库做出贡献，我们非常欢迎提交 [Issue](https://github.com/SWE-agent/SWE-agent/issues) 和 [Pull Request](https://github.com/SWE-agent/SWE-agent/pulls)！对于较大的代码改动，我们始终建议先在 Issue 中进行讨论。

## 引用与联系方式 <a name="citation"></a>

SWE-agent 是由普林斯顿大学的 John Yang*、Carlos E. Jimenez*、Alexander Wettig、Kilian Lieret、Shunyu Yao、Karthik Narasimhan 和 Ofir Press 发起的学术研究项目。
主要联系人：[John Yang](https://john-b-yang.github.io/)、[Carlos E. Jimenez](http://www.carlosejimenez.com/) 以及 [Kilian Lieret](https://www.lieret.net/)（邮箱：johnby@stanford.edu, carlosej@cs.princeton.edu, kl5675@princeton.edu）。

如果你觉得这项工作对你有帮助，请考虑使用以下格式引用我们：

<details>
<summary> SWE-agent 引用格式</summary>

```bibtex
@inproceedings{yang2024sweagent,
  title={{SWE}-agent: Agent-Computer Interfaces Enable Automated Software Engineering},
  author={John Yang and Carlos E Jimenez and Alexander Wettig and Kilian Lieret and Shunyu Yao and Karthik R Narasimhan and Ofir Press},
  booktitle={The Thirty-eighth Annual Conference on Neural Information Processing Systems},
  year={2024},
  url={https://arxiv.org/abs/2405.15793}
}
```
</details>

如果你使用了 SWE-agent 中的摘要生成器、交互式命令或进攻性网络安全功能，也请考虑引用以下内容：

<details>
<summary>EnIGMA 引用格式</summary>

```bibtex
@misc{abramovich2024enigmaenhancedinteractivegenerative,
      title={EnIGMA: Enhanced Interactive Generative Model Agent for CTF Challenges},
      author={Talor Abramovich and Meet Udeshi and Minghao Shao and Kilian Lieret and Haoran Xi and Kimberly Milner and Sofija Jancheska and John Yang and Carlos E. Jimenez and Farshad Khorrami and Prashanth Krishnamurthy and Brendan Dolan-Gavitt and Muhammad Shafique and Karthik Narasimhan and Ramesh Karri and Ofir Press},
      year={2024},
      eprint={2409.16165},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2409.16165},
}
```
</details>


## 🪪 许可证 <a name="license"></a>
MIT。请查看 `LICENSE` 文件。


<div align="center">

[![Pytest](https://github.com/SWE-agent/SWE-agent/actions/workflows/pytest.yaml/badge.svg)](https://github.com/SWE-agent/SWE-agent/actions/workflows/pytest.yaml)
[![build-docs](https://github.com/SWE-agent/SWE-agent/actions/workflows/build-docs.yaml/badge.svg)](https://github.com/SWE-agent/SWE-agent/actions/workflows/build-docs.yaml)
[![codecov](https://codecov.io/gh/SWE-agent/SWE-agent/graph/badge.svg?token=18XAVDK365)](https://codecov.io/gh/SWE-agent/SWE-agent)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/SWE-agent/SWE-agent/main.svg)](https://results.pre-commit.ci/latest/github/SWE-agent/SWE-agent/main)
[![Markdown links](https://github.com/SWE-agent/SWE-agent/actions/workflows/check-links-periodic.yaml/badge.svg)](https://github.com/SWE-agent/SWE-agent/actions/workflows/check-links-periodic.yaml)

</div>