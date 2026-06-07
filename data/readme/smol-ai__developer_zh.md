# 🐣 smol developer

<a href="https://app.e2b.dev/agent/smol-developer" target="_blank" rel="noopener noreferrer">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://app.e2b.dev/api/badge_light">
  <img alt="Deploy agent on e2b button" src="https://app.e2b.dev/api/badge"/>
</picture>
</a>
<a href="https://github.com/modal-labs/devlooper"><img src="https://github.com/smol-ai/developer/assets/6764957/6af16d37-2494-4722-b3a2-6fc91c005451"></img>
</a>
<a href="https://twitter.com/morph_labs/status/1689321673151979536"><img src="https://avatars.githubusercontent.com/u/136536927?s=40&v=4" alt="Morph"></img> Morph
</a>

***以人为本且连贯的完整程序合成*** 也就是你专属的个人初级开发者（junior developer）

> [构建那个能构建事物的工具！](https://twitter.com/swyx/status/1657578738345979905) 为每位开发者在任何场景下提供一位 `smol dev`

这是一个“初级开发者”智能体（即 `smol dev`），它可以：

1. 在你提供产品规格说明后，为你搭建整个代码库
2. 为你提供基础构建模块，让你在自己的应用中集成一位 smol dev。

与制作和维护特定、僵化的一次性脚手架（如 `create-react-app` 或 `create-nextjs-app`）不同，它本质上是一个或帮助你创建 [`create-anything-app`](https://news.ycombinator.com/item?id=35942352) 的工具，你可以与你的 smol dev 紧密协作，快速迭代开发脚手架提示词。

在 [v0 版本成功发布](https://twitter.com/swyx/status/1657578738345979905)后，smol developer 被重写为**更加精简（smol-ler）**的版本，并支持作为库直接导入使用！

## 基本用法

### Git 仓库模式

```bash
# install
git clone https://github.com/smol-ai/developer.git
cd developer
poetry install # install dependencies. pip install poetry if you need

# run
python main.py "a HTML/JS/CSS Tic Tac Toe Game" # defaults to gpt-4-0613
# python main.py "a HTML/JS/CSS Tic Tac Toe Game" --model=gpt-3.5-turbo-0613

# other cli flags
python main.py --prompt prompt.md # for longer prompts, move them into a markdown file
python main.py --prompt prompt.md --debug True # for debugging
```

<details>
  <summary>
此模式允许你以“人在回路”（human-in-the-loop）的方式开发应用，遵循 smol developer 的原始版本设计。
  </summary>


<p align="center">
  <img height=200 src="https://pbs.twimg.com/media/FwEzVCcaMAE7t4h?format=jpg&name=large" />
</p>

*使用提示词进行工程化开发，而非传统的提示词工程（prompt engineering）*

`prompt.md` 中的演示示例展示了 AI 赋能但依然坚定以开发者为中心的工作流的潜力：

- 你编写一个基础提示词，描述想要构建的应用
- `main.py` 生成代码
- 你运行或阅读生成的代码
- 你可以：
  - 随着发现提示词中未明确指定的部分，直接在提示词中添加内容
  - 手动运行代码并排查错误
  - *将报错信息粘贴到提示词中*，就像提交 GitHub Issue 一样
  - 如需额外帮助，可使用 `debugger.py`，它会读取整个代码库以提供具体的代码修改建议

循环此过程直到满意为止。请注意，AI 仅在它真正创造价值时才被使用——一旦它妨碍你的工作，只需轻松接管代码库即可，无需顾虑（*我们也可以让 smol-dev 接管现有代码库并自动生成其提示词……但这属于“未来方向”*）

</details>

通过这种方式，你可以直接利用克隆的该仓库本身来原型设计或开发你的应用。

### 库模式

这是 smol developer v1 的新特性！你可以将 `smol developer` 集成到自己的项目中！

```bash
pip install smol_dev
```

在此模式下，你基本上可以将 `main.py` 的内容视为我们的“文档”，了解如何在你自己的应用中调用这些函数和提示词：

```python
from smol_dev.prompts import plan, specify_file_paths, generate_code_sync

prompt = "a HTML/JS/CSS Tic Tac Toe Game"

shared_deps = plan(prompt) # returns a long string representing the coding plan

# do something with the shared_deps plan if you wish, for example ask for user confirmation/edits and iterate in a loop

file_paths = specify_file_paths(prompt, shared_deps) # returns an array of strings representing the filenames it needs to write based on your prompt and shared_deps. Relies on OpenAI's new Function Calling API to guarantee JSON.

# do something with the filepaths if you wish, for example display a plan

# loop through file_paths array and generate code for each file
for file_path in file_paths:
    code = generate_code_sync(prompt, shared_deps, file_path) # generates the source code of each file

    # do something with the source code of the file, eg. write to disk or display in UI
    # there is also an async `generate_code()` version of this
```

### API 模式（通过 [Agent Protocol](https://github.com/e2b-dev/agent-protocol)）
启动服务器请运行：
```bash
poetry run api
```
或
```bash
python smol_dev/api.py
```

随后可通过以下命令调用 API：

要**创建任务**，请运行：
```bash
curl --request POST \
  --url http://localhost:8000/agent/tasks \
  --header 'Content-Type: application/json' \
  --data '{
	"input": "Write simple script in Python. It should write '\''Hello world!'\'' to hi.txt"
}'
```

你将收到如下响应：
```json
{"input":"Write simple script in Python. It should write 'Hello world!' to hi.txt","task_id":"d2c4e543-ae08-4a97-9ac5-5f9a4459cb19","artifacts":[]}
```

随后要**执行任务的单步操作**，复制上一步请求返回的 `task_id` 并运行：

```bash
curl --request POST \
  --url http://localhost:8000/agent/tasks/<task-id>/steps
```

或者你可以使用 [Python 客户端库](https://github.com/e2b-dev/agent-protocol/tree/main/agent_client/python)：

```python
from agent_protocol_client import AgentApi, ApiClient, TaskRequestBody

...

prompt = "Write simple script in Python. It should write 'Hello world!' to hi.txt"

async with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = AgentApi(api_client)
    task_request_body = TaskRequestBody(input=prompt)

    task = await api_instance.create_agent_task(
        task_request_body=task_request_body
    )
    task_id = task.task_id
    response = await api_instance.execute_agent_task_step(task_id=task_id)

...

```

## 示例/提示词画廊

- [6 分钟视频演示](https://youtu.be/UCo7YeTy-aE) - （抱歉音频加速了，当时为了适配 Twitter 做了优化，效果不太好）
  - 这是最初的 smol developer 演示：从提示词到完整的 Chrome 扩展程序（请求并存储 API Key、生成弹窗窗口、读取和传输页面内容，并使用 Anthropic Claude 对任意网站进行有用总结；根据输入长度自动切换模型至最高支持 100k token 的版本）
  - 提示词位于 [prompt.md](https://github.com/smol-ai/developer/blob/main/prompt.md)，输出目录为 [/exampleChromeExtension](https://github.com/smol-ai/developer/tree/main/examples/exampleChromeExtension)
- `smol-plugin` - 用于 ChatGPT 插件的提示词（[推文](https://twitter.com/ultrasoundchad/status/1659366507409985536?s=20), [Fork](https://github.com/gmchad/smol-plugin)）

  <img src="https://github.com/smol-ai/developer/assets/6764957/6ffaac3b-5d90-460a-a590-c8a8c004bd36" height=200 />

- [从提示词到宝可梦应用](https://twitter.com/RobertCaracaus/status/1659312419485761536?s=20)

  <img src="https://github.com/smol-ai/developer/assets/6764957/15fa189a-3f52-4618-ac8e-2a77b6500264" height=200 />

- [政治竞选 CRM 程序示例](https://github.com/smol-ai/developer/pull/22/files)
- [使用 GPT-4 创建 VSCode 扩展的经验教训](https://bit.kevinslin.com/p/leveraging-gpt-4-to-automate-the)（也在 [HN](https://news.ycombinator.com/item?id=36071342) 上发布）
- [7 分钟视频：Smol AI Developer - 用单个提示词构建完整代码库](https://www.youtube.com/watch?v=DzRoYc2UGKI) 展示了如何从提示词生成一个功能完整的 OpenAI CLI Python 应用

  <img src="https://github.com/smol-ai/developer/assets/6764957/e80058f1-ea9c-42dd-87ff-004b61f08f2e" height=200 />

- [12 分钟视频：SMOL AI - 一键开发大规模应用](https://www.youtube.com/watch?v=zsxyqz6SYp8) 该演示在 40 分钟内、花费约 9 美元，搭建了一个结构相当复杂的 React/Node/MongoDB 全栈应用

  <img src="https://github.com/smol-ai/developer/assets/6764957/c51f9f8c-021d-446a-b44d-7a6f48e64550" height=200 />

我正在积极寻找更多示例，欢迎提交你的 Pull Request！
抱歉目前示例较少，我知道这让人沮丧，但我当时确实没料到会有这么多人关注 lol

## 主要 Forks / 替代方案

欢迎提交其他实现方式，以及在替代技术栈上的部署策略！

- **JS/TS**：https://github.com/PicoCreator/smol-dev-js 纯 JavaScript 变体，允许通过提示词实现更精细的增量修改（如果你不想走完整的“规格转代码”流程），并且可以实时嵌入任何项目中使用（好坏参半）
- **C#/Dotnet**：https://github.com/colhountech/smol-ai-dotnet 使用 C#！
- **Golang**：https://github.com/tmc/smol-dev-go 使用 Go 语言编写
- https://github.com/gmchad/smol-plugin 通过指定 Markdown API，自动生成 @openai 插件（smol-developer 风格）
- 你的 Fork 版本在此！


### 创新与见解

> 如需更详细的文章、见解和反思，请订阅 https://latent.space/

- **Markdown 足矣** - Markdown 是提示词进行完整程序合成的完美载体，因为它可以轻松混合英文和代码（无论是 `variable_names` 还是完整的 \`\`\` 代码块）
  - 事实证明，你可以在提示词中用代码指定其他提示词，GPT-4 会严格按字面意思执行。
- **复制粘贴编程**
  - 只需将 `curl` 的输入和输出粘贴进去，就能教会程序如何围绕新 API（Anthropic 的 API 在 GPT3 知识截止日期之后）进行编码。
  - 将报错信息粘贴到提示词中，并模糊地指示程序如何处理。这感觉有点像“日志驱动编程”。
- **通过 `cat` 整个代码库进行调试**：将报错信息连同完整代码库一起丢给 AI，获取具体的修复建议——这非常令人愉悦！
- **保持完整程序连贯性的技巧** - 我们选择的示例用例 Chrome 扩展程序在文件间存在大量间接依赖。任何跨依赖关系的幻觉都会导致整个程序报错。
  - 我们通过增加一个中间步骤来解决：要求 GPT 预先梳理 `shared_dependencies.md`，然后在生成每个文件时强制使用该文件。这基本上意味着让 GPT 能够“自言自语”……
  - ……但这还不够完美。`shared_dependencies.md` 有时无法全面理解文件间的强依赖关系。因此我们直接在提示词中指定了特定的 `name`。起初感觉有点“脏”，但确实有效，归根结底这只是清晰无歧义的沟通方式。
  - 请参阅 `prompt.md` 获取当前最佳（SOTA）的 smol-dev 提示词技巧。
- **降低不熟悉 API 的使用门槛**
  - 我们从未真正学过 CSS 动画，但现在只需说想要一个“带有红白糖果条纹的生动 CSS 动画加载指示器”，它就能实现。
  - Chrome Extension Manifest v3 也是如此——文档简直是一团糟，但幸运的是我们现在不必阅读它们也能快速完成基础功能。
  - Anthropic 的文档（非常糟糕）缺少关于返回签名的说明。所以直接 curl 请求并把结果丢进提示词里就行了 lol。
- **Modal 足矣** - 我们选择 Modal 解决了四个问题：
  - 解决开发和生产环境中的 Python 依赖地狱问题
  - 支持并行代码生成
  - 提供从本地开发到云端托管端点的简单升级路径（未来）
  - 具备容错机制的 OpenAI API 调用，支持重试/退避策略及附加存储功能（未来使用）

> 如需更详细的文章、见解和反思，请订阅 https://latent.space/

### 注意事项 / 局限性

我们当时正在开发一个 Chrome 扩展程序，需要生成图片，因此添加了一些用例特定的代码来跳过销毁/重新生成步骤，这部分尚未决定如何通用化。

我们目前无法使用 GPT4-32k，但如果可以的话，我们会尝试将整个 API/SDK 文档注入上下文。

目前的反馈循环非常慢（根据 `time` 命令统计，即使通过 Modal 进行并行化，GPT-4 生成一个程序也需要约 2-4 分钟，偶尔还会更高），但可以肯定的是随着时间的推移速度会下降（详见下方的“未来方向”）。


## 未来方向

可尝试的方向/欢迎提交 Issue 讨论和 Pull Request：

- **为每个生成的文件指定独立的 `.md` 文件**，并在其中添加进一步的提示词以微调输出。
  - 例如类似 `popup.html.md` 和 `content_script.js.md` 这样的结构。
- **为现有代码库自动生成 `prompt.md`** - 编写脚本读取代码库并生成描述性的、要点式的提示词来还原它。
  - 目前由 `smol pm` 完成，但效果还不够好——在实现“能自我生成的 quine smol developer”之前，非常需要有人进行专注的打磨和优化 lol。
- **自动安装自身依赖的能力**
  - 这会涉及到对执行环境的依赖，众所周知这是导致依赖混乱的根源。如何避免？Dockerize？Nix？还是 [Web Container](https://twitter.com/litbid/status/1658154530385670150)？
  - Modal 提供了一个有趣的思路：生成能够“调用 Modal”的函数，这也能解决依赖问题（见推文链接）。
- **自我修复** - 通过运行代码本身，并将报错信息作为重新提示词的依据。
  - 但由于从 Chrome 扩展环境获取错误信息比较困难，我们暂未尝试此方案。
- **使用 Anthropic 作为编码层**
  - 你可以运行 `modal run anthropic.py --prompt prompt.md --outputdir=anthropic` 进行尝试。
  - 但目前效果不佳，因为 Anthropic 在遵循指令生成文件代码方面表现不够理想。
- **创建自主运行此代码的 Agent（循环执行/监听提示词文件）**，每次都在新的 Git 分支上重新生成代码。
  - 代码可以在 5 个并行的 Git 分支上同时生成，检查输出只需切换分支即可。