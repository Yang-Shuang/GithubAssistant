<p align="center">
  <img src="docs/assets/readme-banner.svg" alt="Agent-Lightning 横幅" style="width:600px"/>
</p>

# Agent Lightning⚡

[![Unit Tests](https://github.com/microsoft/agent-lightning/actions/workflows/badge-unit.yml/badge.svg)](https://github.com/microsoft/agent-lightning/actions/workflows/badge-unit.yml)
[![Documentation](https://img.shields.io/badge/GitHub%20Pages-Documentation-blue)](https://microsoft.github.io/agent-lightning/)
[![PyPI version](https://badge.fury.io/py/agentlightning.svg)](https://badge.fury.io/py/agentlightning)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/microsoft/agent-lightning)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/RYk7CdvDR7)

**专为点燃 AI 智能体潜能而打造的终极训练框架。**

加入我们的 [Discord 社区](https://discord.gg/RYk7CdvDR7)，与其他用户和贡献者交流。

## ⚡ 核心特性

- 仅需（几乎）**零代码修改**即可将你的智能体转化为可优化的高效模型！💤
- 支持基于**任意**智能体框架（LangChain、OpenAI Agent SDK、AutoGen、CrewAI、Microsoft Agent Framework 等）进行构建；甚至无需任何框架（直接使用 Python + OpenAI）。随你发挥！🤖
- **选择性**优化多智能体系统中的单个或多个智能体。🎯
- 全面支持强化学习（Reinforcement Learning）、自动提示词优化、监督微调等核心算法。🤗

更多详情请参阅我们的[文档网站](https://microsoft.github.io/agent-lightning/)。

<p align="center">
  <img src="docs/assets/readme-diff.svg" alt="Agent-Lightning Core Quickstart" style="width:100%"/>
</p>

## ⚡ 安装

```bash
pip install agentlightning
```

如需获取最新夜间构建版本（包含前沿功能），可从 Test PyPI 进行安装：

```bash
pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ --pre agentlightning
```

更多详细信息请参阅我们的[安装指南](https://microsoft.github.io/agent-lightning/stable/tutorials/installation/)。

开始使用 Agent Lightning，请查阅我们的[文档](https://microsoft.github.io/agent-lightning/)和[示例代码](./examples)。

## ⚡ 相关文章/博客

- 12/17/2025 [采用轨迹级聚合以实现更快训练](https://agent-lightning.github.io/posts/trajectory_level_aggregation/) Agent Lightning 官方博客。
- 11/4/2025 [使用 Tinker 调优任意 AI 智能体 ✕ Agent Lightning](https://medium.com/@yugez/tuning-any-ai-agent-with-tinker-agent-lightning-part-1-1d8c9a397f0e) Medium。另见[第二部分](https://medium.com/@yugez/tuning-any-ai-agent-with-tinker-agent-lightning-part-2-332c5437f0dc)。
- 10/22/2025 [告别重分词漂移：通过 OpenAI 兼容 API 返回 Token ID 在智能体强化学习中的重要性](https://blog.vllm.ai/2025/10/22/agent-lightning.html) vLLM 官方博客。另见[知乎详解](https://zhuanlan.zhihu.com/p/1965067274642785725)。
- 8/11/2025 [利用强化学习训练 AI 智能体编写与自我修正 SQL](https://medium.com/@yugez/training-ai-agents-to-write-and-self-correct-sql-with-reinforcement-learning-571ed31281ad) Medium。
- 8/5/2025 [Agent Lightning：使用强化学习训练任意 AI 智能体](https://arxiv.org/abs/2508.03680) arXiv 论文。
- 7/26/2025 [我们发现了一种仅需（几乎）零代码改动即可用 RL 训练任意 AI 智能体的方法。](https://www.reddit.com/r/LocalLLaMA/comments/1m9m670/we_discovered_an_approach_to_train_any_ai_agent/) Reddit。
- 6/6/2025 [Agent Lightning - 微软研究院](https://www.microsoft.com/en-us/research/project/agent-lightning/) 项目主页。

## ⚡ 社区项目

- [DeepWerewolf](https://github.com/af-74413592/DeepWerewolf) — 基于 AgentScope 和 Agent Lightning 构建的中国狼人杀游戏智能体强化学习训练案例研究。
- [AgentFlow](https://agentflow.stanford.edu/) — 一个模块化多智能体框架，结合规划器、执行者、验证器和生成器智能体与 Flow-GRPO 算法，用于解决长周期、稀疏奖励任务。
- [Youtu-Agent](https://github.com/TencentCloudADP/Youtu-agent) — Youtu-Agent 让你轻松构建和训练智能体。基于 Agent Lightning 的[修改分支](https://github.com/microsoft/agent-lightning/tree/contrib/youtu-agent-lightning)开发，Youtu-Agent 已验证在数学/代码及搜索能力上最多支持 128 张 GPU 进行强化学习训练，且收敛稳定。另请参阅[相关配方指南](https://github.com/TencentCloudADP/youtu-agent/tree/rl/agl)及其博客文章[*告别折腾你的智能体 RL：Youtu-Agent 如何轻松实现稳定的 128-GPU 扩展*](https://spotted-coconut-df8.notion.site/Stop-Wrestling-with-Your-Agent-RL-How-Youtu-Agent-Achieved-Stable-128-GPU-Scaling-Without-Breaking-2ca5e8f089ba80539a98c582b65e0233)。

## ⚡ 架构设计

Agent Lightning 将底层组件精简至最低限度，让你能专注于核心创意而非基础设施。你的智能体仍可照常运行；你依然可以使用任何偏好的智能体框架；只需嵌入轻量级的 `agl.emit_xxx()` 辅助函数，或让追踪器自动收集每一次提示词输入、工具调用和奖励反馈。这些事件将转化为结构化的 Span（追踪跨度），并流入 LightningStore——一个保持任务、资源与轨迹同步的中心枢纽。

在 Store 的另一端，是你选择或自行编写的算法。该算法读取 Span 数据、从中学习，并发布更新后的资源（如优化后的提示词模板或新的策略权重）。Trainer（训练器）负责串联整个流程：它将数据集流式传输至运行器，在 Store 与算法之间同步资源，并在性能提升时自动更新推理引擎。你可以随时在此处停止迭代，也可以让循环持续运转以不断优化。

无需重写代码，无厂商锁定，仅提供一条从首次运行到稳定优化的清晰路径。

<p align="center">
  <img src="docs/assets/readme-architecture.svg" alt="Agent-lightning Architecture" style="width:100%"/>
</p>

## ⚡ CI 状态

| 工作流 | 状态 |
|----------|--------|
| CPU Tests | [![tests workflow status](https://github.com/microsoft/agent-lightning/actions/workflows/tests.yml/badge.svg)](https://github.com/microsoft/agent-lightning/actions/workflows/tests.yml) |
| Full Tests | [![tests summary workflow status](https://github.com/microsoft/agent-lightning/actions/workflows/badge-unit.yml/badge.svg)](https://github.com/microsoft/agent-lightning/actions/workflows/badge-unit.yml) |
| UI Tests | [![UI Tests](https://github.com/microsoft/agent-lightning/actions/workflows/dashboard.yml/badge.svg)](https://github.com/microsoft/agent-lightning/actions/workflows/dashboard.yml) |
| Examples Integration | [![examples summary workflow status](https://github.com/microsoft/agent-lightning/actions/workflows/badge-examples.yml/badge.svg)](https://github.com/microsoft/agent-lightning/actions/workflows/badge-examples.yml) |
| Latest Dependency Compatibility | [![latest summary workflow status](https://github.com/microsoft/agent-lightning/actions/workflows/badge-latest.yml/badge.svg)](https://github.com/microsoft/agent-lightning/actions/workflows/badge-latest.yml) |
| Legacy Examples Compatibility | [![compat summary workflow status](https://github.com/microsoft/agent-lightning/actions/workflows/badge-compat.yml/badge.svg)](https://github.com/microsoft/agent-lightning/actions/workflows/badge-compat.yml) |

## ⚡ 引用方式

如果你在研究或项目中觉得 Agent Lightning 有用，请引用我们的论文：

```bibtex
@misc{luo2025agentlightningtrainai,
      title={Agent Lightning: Train ANY AI Agents with Reinforcement Learning},
      author={Xufang Luo and Yuge Zhang and Zhiyuan He and Zilong Wang and Siyun Zhao and Dongsheng Li and Luna K. Qiu and Yuqing Yang},
      year={2025},
      eprint={2508.03680},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2508.03680},
}
```

## ⚡ 贡献指南

本项目欢迎各界的贡献与建议。请先阅读[贡献指南](docs/community/contributing.md)，了解推荐的贡献方向、环境配置、分支规范及 Pull Request 要求。大多数贡献需要您签署一份贡献者许可协议（CLA），声明你拥有权利并实际授予我们使用你贡献的权利。详情请访问 https://cla.opensource.microsoft.com。

提交 Pull Request 时，CLA Bot 将自动判断你是否需要签署协议，并相应地更新 PR 状态（例如添加标签或评论）。只需按照机器人提示操作即可。在使用我们 CLA 的所有仓库中，你只需完成一次此流程。

本项目已采用[微软开源行为准则](https://opensource.microsoft.com/codeofconduct/)。如需更多信息，请参阅[行为准则常见问题解答](https://opensource.microsoft.com/codeofconduct/faq/)，或就其他问题与评论联系 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## ⚡ 商标声明

本项目可能包含相关项目、产品或服务的商标或徽标。微软商标或徽标的授权使用须遵循并符合[微软商标与品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。对本项目的修改版本中使用微软商标或徽标不得引起混淆，也不得暗示微软的赞助。任何第三方商标或徽标的使用均受其各自政策约束。

## ⚡ 负责任的人工智能

本项目已通过评估并认证符合微软《负责任的 AI 原则》。团队将持续监控和维护该仓库，及时解决任何严重问题（包括潜在危害）。

## ⚡ 许可证

本项目采用 MIT 许可证。详情请参阅[LICENSE](LICENSE)文件。