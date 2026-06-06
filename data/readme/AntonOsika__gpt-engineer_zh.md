# gpt-engineer

[![GitHub Repo stars](https://img.shields.io/github/stars/gpt-engineer-org/gpt-engineer?style=social)](https://github.com/gpt-engineer-org/gpt-engineer)
[![Discord Follow](https://dcbadge.vercel.app/api/server/8tcDQ89Ej2?style=flat)](https://discord.gg/8tcDQ89Ej2)
[![License](https://img.shields.io/github/license/gpt-engineer-org/gpt-engineer)](https://github.com/gpt-engineer-org/gpt-engineer/blob/main/LICENSE)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/gpt-engineer-org/gpt-engineer)](https://github.com/gpt-engineer-org/gpt-engineer/issues)
![GitHub Release](https://img.shields.io/github/v/release/gpt-engineer-org/gpt-engineer)
[![Twitter Follow](https://img.shields.io/twitter/follow/antonosika?style=social)](https://twitter.com/antonosika)

经典的代码生成实验平台！

如果你正在寻找一个更具主见、托管式的演进版本，请查看 gptengineer.app。

如果你正在寻找一款维护良好且易于二次开发的 CLI 工具，请查看 aider。


gpt-engineer 让你能够：
- 用自然语言描述软件需求
- 坐享其成，看着 AI 编写并执行代码
- 让 AI 实现功能改进

## Getting Started

### Install gpt-engineer

For **stable** release:

- `python -m pip install gpt-engineer`

For **development**:
- `git clone https://github.com/gpt-engineer-org/gpt-engineer.git`
- `cd gpt-engineer`
- `poetry install`
- `poetry shell` to activate the virtual environment

我们目前积极支持 Python 3.10 - 3.12。支持 Python 3.8 - 3.9 的最后一个版本是 [0.2.6](https://pypi.org/project/gpt-engineer/0.2.6/)。

### Setup API key

Choose **one** of:
- Export env variable (you can add this to .bashrc so that you don't have to do it each time you start the terminal)
    - `export OPENAI_API_KEY=[your api key]`
- .env file:
    - Create a copy of `.env.template` named `.env`
    - Add your OPENAI_API_KEY in .env
- Custom model:
    - See [docs](https://gpt-engineer.readthedocs.io/en/latest/open_models.html), supports local model, azure, etc.

如需在 Windows 上使用，请查看 [Windows README](./WINDOWS_README.md)。

**Other ways to run:**
- Use Docker ([instructions](docker/README.md))
- Do everything in your browser:
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/gpt-engineer-org/gpt-engineer/codespaces)

### Create new code (default usage)
- Create an empty folder for your project anywhere on your computer
- Create a file called `prompt` (no extension) inside your new folder and fill it with instructions
- Run `gpte <project_dir>` with a relative path to your folder
  - For example: `gpte projects/my-new-project` from the gpt-engineer directory root with your new folder in `projects/`

### Improve existing code
- Locate a folder with code which you want to improve anywhere on your computer
- Create a file called `prompt` (no extension) inside your new folder and fill it with instructions for how you want to improve the code
- Run `gpte <project_dir> -i` with a relative path to your folder
  - For example: `gpte projects/my-old-project -i` from the gpt-engineer directory root with your folder in `projects/`

### Benchmark custom agents
- gpt-engineer installs the binary 'bench', which gives you a simple interface for benchmarking your own agent implementations against popular public datasets.
- The easiest way to get started with benchmarking is by checking out the [template](https://github.com/gpt-engineer-org/gpte-bench-template) repo, which contains detailed instructions and an agent template.
- Currently supported benchmark:
  - [APPS](https://github.com/hendrycks/apps)
  - [MBPP](https://github.com/google-research/google-research/tree/master/mbpp)

社区已开展多项基准测试相关工作，详情可观看[此 Loom 视频](https://www.loom.com/share/206805143fbb4302b5455a5329eaab17?sid=f689608f-8e49-44f7-b55f-4c81e9dc93e6)。

### Research
我们的部分社区成员已撰写了若干可进一步深入的研究简报。如果你感兴趣，请参阅[此文档](https://docs.google.com/document/d/1qmOj2DvdPc6syIAm8iISZFpfik26BYw7ZziD5c-9G0E/edit?usp=sharing)。

## Terms
运行 gpt-engineer 即表示你同意我们的 [terms](https://github.com/gpt-engineer-org/gpt-engineer/blob/main/TERMS_OF_USE.md)。


## Relation to gptengineer.app (GPT Engineer)
[gptengineer.app](https://gptengineer.app/) 是一个用于自动生成 Web 应用的商业项目。
它为非技术用户提供了一套图形界面（UI），并连接至由 git 管理的代码库。
gptengineer.app 团队正在积极支持开源社区。


## Features

### Pre Prompts (前置提示词)
你可以通过用自己的版本覆盖 `preprompts` 文件夹来指定 AI Agent 的“身份”。可通过 `--use-custom-preprompts` 参数实现。

编辑 `preprompts` 是让 Agent 在不同项目间保持记忆的方法。

### Vision (视觉支持)

默认情况下，gpt-engineer 通过 `prompt` 文件接收文本输入。它也支持为具备视觉能力的模型传入图像输入。这可用于添加 UX 或架构图作为 GPT Engineer 的额外上下文信息。你可以通过指定 `—-image_directory` 参数来设定图像目录，并在第二个 CLI 参数中设置具备视觉能力的模型来实现。

例如：`gpte projects/example-vision gpt-4-vision-preview --prompt_file prompt/text --image_directory prompt/images -i`

### Open source, local and alternative models (开源、本地及替代模型)

默认情况下，gpt-engineer 支持通过 OpenAI API 或 Azure OpenAI API 调用 OpenAI 模型，以及 Anthropic 的模型。

经过少量额外配置后，你也可以使用如 WizardCoder 等开源模型。示例说明请参阅 [documentation](https://gpt-engineer.readthedocs.io/en/latest/open_models.html)。

## Mission

gpt-engineer 社区的使命是**维护编码 Agent 构建者可使用的工具，并促进开源社区的合作**。

如果你有兴趣为此做出贡献，我们非常欢迎你的加入。

若想了解我们的更宏大愿景，请查看 [roadmap](https://github.com/gpt-engineer-org/gpt-engineer/blob/main/ROADMAP.md)，并加入
[discord](https://discord.gg/8tcDQ89Ej2)
了解如何为其 [contribute](.github/CONTRIBUTING.md)。

gpt-engineer 由长期贡献者组成的委员会进行 [governed](https://github.com/gpt-engineer-org/gpt-engineer/blob/main/GOVERNANCE.md)。如果你定期做出贡献，并希望参与塑造 gpt-engineer 的未来，我们将考虑将你纳入该委员会。

## Significant contributors
<ul style="list-style-type: none; padding: 0; display: flex; flex-wrap: wrap;"> <li style="margin-right: 10px; margin-bottom: 10px;"> <a href="https://github.com/ATheorell"> <img src="https://avatars.githubusercontent.com/u/143704446?s=64&v=4" alt="@ATheorell" width="32" height="32" style="border-radius: 50%;"> @ATheorell </a> </li> <li style="margin-right: 10px; margin-bottom: 10px;"> <a href="https://github.com/similato87"> <img src="https://avatars.githubusercontent.com/u/71301573?s=64&v=4" alt="@similato87" width="32" height="32" style="border-radius: 50%;"> @similato87 </a> </li> <li style="margin-right: 10px; margin-bottom: 10px;"> <a href="https://github.com/TheoMcCabe"> <img src="https://avatars.githubusercontent.com/u/9841960?s=64&v=4" alt="@TheoMcCabe" width="32" height="32" style="border-radius: 50%;"> @TheoMcCabe </a> </li> <li style="margin-right: 10px; margin-bottom: 10px;"> <a href="https://github.com/captivus"> <img src="https://avatars.githubusercontent.com/u/366332?s=64&v=4" alt="@captivus" width="32" height="32" style="border-radius: 50%;"> @captivus </a> </li> </ul>


## Example



https://github.com/gpt-engineer-org/gpt-engineer/assets/4467025/40d0a9a8-82d0-4432-9376-136df0d57c99