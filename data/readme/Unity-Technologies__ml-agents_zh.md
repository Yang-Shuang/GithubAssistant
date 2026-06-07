# Unity ML-Agents 工具包

[![docs badge](https://img.shields.io/badge/docs-reference-blue.svg)](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest)

[![license badge](https://img.shields.io/badge/license-Apache--2.0-green.svg)](https://github.com/Unity-Technologies/ml-agents/blob/release/4.0.0/LICENSE.md)

([最新发行版](https://github.com/Unity-Technologies/ml-agents/releases/tag/latest_release)) ([所有发行版](https://github.com/Unity-Technologies/ml-agents/releases))

**Unity 机器学习代理工具包**（ML-Agents）是一个开源项目，允许游戏和仿真环境用于训练智能体。我们提供了基于最新算法的实现（底层采用 PyTorch），使游戏开发者及爱好者能够轻松为 2D、3D 以及 VR/AR 游戏训练智能体。研究人员也可使用提供的易用 Python API，通过强化学习（Reinforcement Learning）、模仿学习、神经进化或其他方法训练代理（Agent）。这些经过训练的代理可用于多种用途，包括控制 NPC 行为（适用于多智能体及对抗等多种场景）、自动化测试游戏构建版本以及评估发布前的不同游戏设计方案。该工具包对游戏开发者和人工智能研究人员均具有双重价值，因为它提供了一个集中平台，使人工智能领域的最新进展能够在 Unity 丰富的环境中进行评估，并进一步惠及更广泛的研究界与游戏开发者社区。

## 功能特性
- 17 个以上的 [示例 Unity 环境](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Learning-Environment-Examples.html)
- 支持多种环境配置与训练场景
- 灵活的 Unity SDK，可集成至你的游戏或自定义 Unity 场景中
- 支持通过多种深度强化学习算法（如 PPO、SAC、MA-POCA、自我对战）训练单智能体、多智能体协作及多智能体对抗场景。
- 支持通过两种模仿学习算法（BC 和 GAIL）从演示中学习。
- 快速轻松地添加你自己的 [自定义训练算法](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Python-Custom-Trainer-Plugin.html)及/或组件。
- 可为复杂任务轻松定义课程学习（Curriculum Learning）场景
- 利用环境随机化训练鲁棒的智能体
- 通过按需决策（On Demand Decision Making）实现灵活的代理控制
- 使用多个并发的 Unity 环境实例进行训练
- 利用 [推理引擎（Inference Engine）](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Inference-Engine.html) 提供原生跨平台支持
- 通过 Python [控制 Unity 环境](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Python-LLAPI.html)
- 将 Unity 学习环境包装为 [gym](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Python-Gym-API.html) 环境
- 将 Unity 学习环境包装为 [PettingZoo](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Python-PettingZoo-API.html) 环境

## 发行版与文档

> **⚠️ 文档迁移通知**
> 我们已将 [Unity Package 文档](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest) 作为**主要开发者文档**，并**弃用**了 [web docs](https://unity-technologies.github.io/ml-agents/) 的维护。请使用 Unity Package 文档获取最新信息。

下表展示了我们的最新版本，包括正在积极开发中且可能不稳定的 `develop` 分支。以下是一些实用指南：

- [版本说明页面](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Versioning.html) 概述了我们如何管理 GitHub 发行版以及各 ML-Agents 组件的版本控制流程。
- [发布记录页面](https://github.com/Unity-Technologies/ml-agents/releases) 包含版本间变更的详细信息。
- [迁移指南页面](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Migrating.html) 详细说明如何从早期版本的 ML-Agents 工具包进行升级。
- `com.unity.ml-agents` 软件包已针对 Unity 2020.1 及更高版本进行[验证](https://docs.unity3d.com/2020.1/Documentation/Manual/pack-safe.html)。经过验证的软件包发行版编号为 1.0.x。

| **版本** | **发布日期** | **源码** | **文档** | **下载** | **Python 软件包** | **Unity 软件包** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Release 23 | August 28, 2025 | **[源码](https://github.com/Unity-Technologies/ml-agents/tree/release_23)** | [文档](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/index.html) | **[下载](https://github.com/Unity-Technologies/ml-agents/archive/release_23.zip)** | [1.1.0](https://pypi.org/project/mlagents/1.1.0/) | 4.0.0 |
| develop（不稳定） | -- | [源码](https://github.com/Unity-Technologies/ml-agents/tree/develop) | [文档](https://github.com/Unity-Technologies/ml-agents/tree/develop/com.unity.ml-agents/Documentation~/index.md) | [下载](https://github.com/Unity-Technologies/ml-agents/archive/develop.zip) | -- | -- |

如果你是一名对将 Unity 作为人工智能平台进行讨论感兴趣的研究人员，请参阅我们的[关于 Unity 和 ML-Agents 工具包的参考论文预印本](https://arxiv.org/abs/1809.02627)。

如果你使用 Unity 或 ML-Agents 工具包进行研究，请引用以下论文作为参考文献：

```
@article{juliani2020,
  title={Unity: A general platform for intelligent agents},
  author={Juliani, Arthur and Berges, Vincent-Pierre and Teng, Ervin and Cohen, Andrew and Harper, Jonathan and Elion, Chris and Goy, Chris and Gao, Yuan and Henry, Hunter and Mattar, Marwan and Lange, Danny},
  journal={arXiv preprint arXiv:1809.02627},
  url={https://arxiv.org/pdf/1809.02627.pdf},
  year={2020}
}
```

此外，如果你在研究中使用 MA-POCA 训练器，请引用以下论文作为参考文献：

```
@article{cohen2022,
  title={On the Use and Misuse of Absorbing States in Multi-agent Reinforcement Learning},
  author={Cohen, Andrew and Teng, Ervin and Berges, Vincent-Pierre and Dong, Ruo-Ping and Henry, Hunter and Mattar, Marwan and Zook, Alexander and Ganguly, Sujoy},
  journal={RL in Games Workshop AAAI 2022},
  url={http://aaai-rlg.mlanctot.info/papers/AAAI22-RLG_paper_32.pdf},
  year={2022}
}
```

## 其他资源

* [Unity 讨论区](https://discussions.unity.com/tag/ml-agents)
* [CodeMonkeyUnity 制作的 ML-Agents 教程](https://www.youtube.com/playlist?list=PLzDRvYVwl53vehwiN_odYJkPBzcqFw110)
* [Huggingface 提供的 ML-Agents 入门指南](https://huggingface.co/learn/deep-rl-course/en/unit5/introduction)
* [社区创建的 ML-Agents 项目](https://discussions.unity.com/t/post-your-ml-agents-project/816756)
* [Huggingface 上的 ML-Agents 模型](https://huggingface.co/models?library=ml-agents)
* [博客文章](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/Blog-posts.html)
* [Discord 社区频道](https://discord.com/channels/489222168727519232/1202574086115557446)

## 社区与反馈

ML-Agents 工具包是一个开源项目，我们鼓励并欢迎各方贡献。如果你希望参与贡献，请务必查阅我们的 [贡献指南](https://docs.unity3d.com/Packages/com.unity.ml-agents@latest/index.html?subfolder=/manual/CONTRIBUTING.html) 和 [行为准则](https://github.com/Unity-Technologies/ml-agents/blob/release/4.0.0/CODE_OF_CONDUCT.md)。

如果遇到 ML-Agents 工具包的安装与设置问题，或想讨论如何最佳地配置/训练你的智能体，请在 [Unity ML-Agents 讨论论坛](https://discussions.unity.com/tag/ml-agents) 创建新帖子。请务必提供尽可能多的详细信息，以便他人有效协助你。如果使用 ML-Agents 工具包时遇到其他问题或有特定功能需求，请 [提交 GitHub Issue](https://github.com/Unity-Technologies/ml-agents/issues)。

请通过回复 [此讨论帖](https://discussions.unity.com/t/help-shape-the-future-of-ml-agents/1661019) 告知我们你希望随 ML-Agents Unity 软件包一同提供的示例内容。

## 隐私政策

为了提升 Unity ML-Agents 工具包的开发体验，我们添加了编辑器内分析功能。请参阅 [Unity 隐私政策](https://unity3d.com/legal/privacy-policy) 中的“Unity 被动收集的信息”部分。