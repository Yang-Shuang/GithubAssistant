[![Python](https://img.shields.io/pypi/pyversions/gymnasium.svg)](https://badge.fury.io/py/gymnasium)
[![PyPI](https://badge.fury.io/py/gymnasium.svg)](https://badge.fury.io/py/gymnasium)
[![arXiv](https://img.shields.io/badge/arXiv-2407.17032-b31b1b.svg)](https://arxiv.org/abs/2407.17032)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![License](https://img.shields.io/github/license/Farama-Foundation/Gymnasium)](https://github.com/Farama-Foundation/Gymnasium/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p align="center">
    <a href="https://gymnasium.farama.org/" target = "_blank">
    <img src="https://raw.githubusercontent.com/Farama-Foundation/Gymnasium/main/gymnasium-text.png" width="500px" />
</a>

</p>

Gymnasium 是一个开源 Python 库，旨在通过提供学习算法与环境之间通信的标准 API，以及一套符合该标准的环境集合，用于开发和对比强化学习（Reinforcement Learning）算法。它是原 [Gym](https://github.com/openai/gym) 维护团队基于 OpenAI 的 Gym 库分叉出来的版本（OpenAI 已于数年前将维护权移交至外部团队），后续的所有维护工作也将在此继续进行。

文档网站位于 [gymnasium.farama.org](https://gymnasium.farama.org)。此外，我们还有一个公开的 Discord 服务器（用于协调开发工作），欢迎加入：https://discord.gg/bnJ6kubTg6

## Environments

Gymnasium 包含以下环境家族，以及大量第三方环境
* [Classic Control](https://gymnasium.farama.org/environments/classic_control/) - 基于现实世界问题和物理学的经典强化学习环境。
* [Box2D](https://gymnasium.farama.org/environments/box2d/) - 所有环境均围绕物理控制类的玩具游戏展开，采用基于 Box2D 的物理引擎和 PyGame 渲染。
* [Toy Text](https://gymnasium.farama.org/environments/toy_text/) - 专为极致简单而设计，具有较小的离散状态空间和动作空间，易于学习。因此非常适合用于调试强化学习算法的实现。
* [MuJoCo](https://gymnasium.farama.org/environments/mujoco/) - 基于物理引擎的环境，支持多关节控制，复杂度高于 Box2D 环境。
* [Atari](https://ale.farama.org/) - Atari 2600 ROM 模拟器，提供丰富多样的复杂度供智能体（Agent）学习。
* [Third-party](https://gymnasium.farama.org/environments/third_party_environments/) - 已创建大量兼容 Gymnasium API 的环境。请注意软件所针对的版本，如有必要可在 `gymnasium.make` 中使用 `apply_env_compatibility`。

## Installation

安装基础 Gymnasium 库请使用 `pip install gymnasium`。该命令不包含所有环境家族的依赖项（数量庞大，且在部分系统上安装可能存在困难）。你可以为特定家族安装依赖，例如使用 `pip install "gymnasium[atari]"`，或使用 `pip install "gymnasium[all]"` 安装全部依赖。

我们在 Linux 和 macOS 平台上支持并测试 Python 3.10、3.11、3.12、3.13 和 3.14。我们会接受与 Windows 相关的 PR，但不提供官方支持。

## API

Gymnasium API 将环境建模为简单的 Python `env` 类。创建环境实例并与之交互非常简单，以下是一个使用 "CartPole-v1" 环境的示例：

```python
import gymnasium as gym
env = gym.make("CartPole-v1")

observation, info = env.reset(seed=42)
for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()
```

## Notable Related Libraries

请注意，此列表并不完整，仅包含维护者在被询问推荐时最常提及的库。

* [CleanRL](https://github.com/vwxyzjn/cleanrl) 是一个基于 Gymnasium API 的学习库。它专为该领域的新手设计，并提供了非常优秀的参考实现。
* [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) 是 Gymnasium 的多智能体版本，包含多个已实现的环境，例如多智能体 Atari 环境。
* Farama Foundation 还拥有大量其他 [环境](https://farama.org/projects)，由与 Gymnasium 相同的团队维护，并采用 Gymnasium API。

## Environment Versioning

出于可复现性的考虑，Gymnasium 采用严格的版本控制。所有环境名称均以类似 "-v0" 的后缀结尾。当对环境进行修改且可能影响学习结果时，版本号会递增以避免潜在混淆。这些命名规范均继承自 Gym。

## Contributing

我们欢迎社区的贡献！
有关如何开始的详细信息，请参阅我们的 [CONTRIBUTING.md](https://github.com/Farama-Foundation/Gymnasium/blob/main/CONTRIBUTING.md)。

## Support Gymnasium's Development

如果你在经济条件允许的情况下希望支持 Gymnasium 的开发，欢迎加入社区成员一起[向我们捐赠](https://github.com/sponsors/Farama-Foundation)。

## Citation

如需引用 Gymnasium，请使用我们相关的论文（https://arxiv.org/abs/2407.17032），格式如下：

```
@article{towers2024gymnasium,
  title={Gymnasium: A Standard Interface for Reinforcement Learning Environments},
  author={Towers, Mark and Kwiatkowski, Ariel and Terry, Jordan and Balis, John U and De Cola, Gianluca and Deleu, Tristan and Goul{\~a}o, Manuel and Kallinteris, Andreas and Krimmel, Markus and KG, Arjun and others},
  journal={arXiv preprint arXiv:2407.17032},
  year={2024}
}
```