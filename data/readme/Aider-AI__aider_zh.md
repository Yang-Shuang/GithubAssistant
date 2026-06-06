<p align="center">
    <a href="https://aider.chat/"><img src="https://aider.chat/assets/logo.svg" alt="Aider Logo" width="300"></a>
</p>

<h1 align="center">
在你的终端中进行 AI 结对编程
</h1>


<p align="center">
Aider 让你能够与大型语言模型（LLM）进行结对编程，无论是开启新项目还是在现有代码库上继续开发。 
</p>

<p align="center">
  <img
    src="https://aider.chat/assets/screencast.svg"
    alt="aider screencast"
  >
</p>

<p align="center">
<!--[[[cog
from scripts.homepage import get_badges_md
text = get_badges_md()
cog.out(text)
]]]-->
  <a href="https://github.com/Aider-AI/aider/stargazers"><img alt="GitHub Stars" title="Aider 项目获得的 GitHub 星标总数"
src="https://img.shields.io/github/stars/Aider-AI/aider?style=flat-square&logo=github&color=f1c40f&labelColor=555555"/></a>
  <a href="https://pypi.org/project/aider-chat/"><img alt="PyPI Downloads" title="通过 PyPI pip 安装的总次数"
src="https://img.shields.io/badge/📦%20Installs-6.8M-2ecc71?style=flat-square&labelColor=555555"/></a>
  <img alt="Tokens per week" title="Aider 用户每周处理的 Token 数量"
src="https://img.shields.io/badge/📈%20Tokens%2Fweek-15B-3498db?style=flat-square&labelColor=555555"/>
  <a href="https://openrouter.ai/#options-menu"><img alt="OpenRouter Ranking" title="Aider 在 OpenRouter 平台上的应用排名"
src="https://img.shields.io/badge/🏆%20OpenRouter-Top%2020-9b59b6?style=flat-square&labelColor=555555"/></a>
  <a href="https://aider.chat/HISTORY.html"><img alt="Singularity" title="Aider 上次发布中由 Aider 自身编写的代码占比"
src="https://img.shields.io/badge/🔄%20Singularity-88%25-e74c3c?style=flat-square&labelColor=555555"/></a>
<!--[[[end]]]-->  
</p>

## 功能特性

### [支持云端与本地大语言模型 (LLM)](https://aider.chat/docs/llms.html)

<a href="https://aider.chat/docs/llms.html"><img src="https://aider.chat/assets/icons/brain.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 在配合 Claude 3.7 Sonnet、DeepSeek R1 & Chat V3、OpenAI o1、o3-mini 及 GPT-4o 时效果最佳，但也可连接几乎所有大语言模型（LLM），包括本地部署的模型。

<br>

### [自动映射你的代码库](https://aider.chat/docs/repomap.html)

<a href="https://aider.chat/docs/repomap.html"><img src="https://aider.chat/assets/icons/map-outline.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 会为你的整个代码库生成一张结构地图，这有助于它在大型项目中更好地发挥作用。

<br>

### [支持 100+ 种编程语言](https://aider.chat/docs/languages.html)

<a href="https://aider.chat/docs/languages.html"><img src="https://aider.chat/assets/icons/code-tags.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 兼容大多数主流编程语言：Python、JavaScript、Rust、Ruby、Go、C++、PHP、HTML、CSS，以及数十种其他语言。

<br>

### [集成 Git 版本控制](https://aider.chat/docs/git.html)

<a href="https://aider.chat/docs/git.html"><img src="https://aider.chat/assets/icons/source-branch.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 会自动提交更改并生成合理的提交信息（commit message）。你可以使用熟悉的 Git 工具轻松查看差异、管理以及撤销 AI 的修改。

<br>

### [在集成开发环境 (IDE) 中使用](https://aider.chat/docs/usage/watch.html)

<a href="https://aider.chat/docs/usage/watch.html"><img src="https://aider.chat/assets/icons/monitor.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
在你常用的 IDE 或编辑器中直接使用 Aider。只需在代码中添加注释来提出修改需求，Aider 就会自动开始工作。

<br>

### [支持图片与网页](https://aider.chat/docs/usage/images-urls.html)

<a href="https://aider.chat/docs/usage/images-urls.html"><img src="https://aider.chat/assets/icons/image-multiple.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
在对话中添加图片和网页链接，以提供视觉上下文、截图或参考文档等信息。

<br>

### [语音转代码](https://aider.chat/docs/usage/voice.html)

<a href="https://aider.chat/docs/usage/voice.html"><img src="https://aider.chat/assets/icons/microphone.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
用语音与 Aider 讨论你的代码！通过语音提出新功能需求、测试用例或 Bug 修复请求，让 Aider 自动实现这些更改。

<br>

### [代码检查 (Lint) 与测试](https://aider.chat/docs/usage/lint-test.html)

<a href="https://aider.chat/docs/usage/lint-test.html"><img src="https://aider.chat/assets/icons/check-all.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
每次 Aider 进行修改时，都会自动对你的代码进行 Lint 检查和运行测试。Aider 还能修复你的检查工具和测试套件中发现的问题。

<br>

### [支持网页聊天界面复制/粘贴](https://aider.chat/docs/usage/copypaste.html)

<a href="https://aider.chat/docs/usage/copypaste.html"><img src="https://aider.chat/assets/icons/content-copy.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
通过任何大语言模型（LLM）的网页聊天界面进行协作。Aider 简化了在浏览器中来回复制/粘贴代码上下文和修改内容的流程。

## 快速开始

```bash
python -m pip install aider-install
aider-install

# Change directory into your codebase
cd /to/your/project

# DeepSeek
aider --model deepseek --api-key deepseek=<key>

# Claude 3.7 Sonnet
aider --model sonnet --api-key anthropic=<key>

# o3-mini
aider --model o3-mini --api-key openai=<key>
```

更多详细信息请参阅[安装说明](https://aider.chat/docs/install.html)与[使用文档](https://aider.chat/docs/usage.html)。

## 更多信息

### 文档资料
- [安装指南](https://aider.chat/docs/install.html)
- [使用指南](https://aider.chat/docs/usage.html)
- [教程视频](https://aider.chat/docs/usage/tutorials.html)
- [连接大语言模型 (LLM)](https://aider.chat/docs/llms.html)
- [配置选项](https://aider.chat/docs/config.html)
- [故障排除](https://aider.chat/docs/troubleshooting.html)
- [常见问题解答 (FAQ)](https://aider.chat/docs/faq.html)

### 社区与资源
- [大语言模型排行榜](https://aider.chat/docs/leaderboards/)
- [GitHub 仓库](https://github.com/Aider-AI/aider)
- [Discord 社区](https://discord.gg/Y7X7bhMQFV)
- [更新日志](https://aider.chat/HISTORY.html)
- [官方博客](https://aider.chat/blog/)

## 用户好评

- *“我的生活彻底改变了……Aider……它绝对会颠覆你的认知。”* —— [X 上的 Eric S. Raymond](https://x.com/esrtweet/status/1910809356381413593)
- *“最好的免费开源 AI 编程助手。”* —— [YouTube 上的 IndyDevDan](https://youtu.be/YALpX8oOn78)
- *“迄今为止最棒的 AI 编程助手。”* —— [YouTube 上的 Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
- *“Aider …… 让我的编码生产力轻松翻了好几倍。”* —— [Hacker News 上的 SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
- *“这是一种很酷的工作流……Aider 的交互设计对我来说完美契合。”* —— [Hacker News 上的 qup](https://news.ycombinator.com/item?id=38185326)
- *“真的就像有位资深开发员直接住在了你的 Git 仓库里一样——太不可思议了！”* —— [GitHub 上的 rappster](https://github.com/Aider-AI/aider/issues/124)
- *“多么惊人的工具。简直难以置信。”* —— [GitHub 上的 valyagolev](https://github.com/Aider-AI/aider/issues/6#issue-1722897858)
- *“Aider 真是个令人惊叹的东西！”* —— [GitHub 上的 cgrothaus](https://github.com/Aider-AI/aider/issues/82#issuecomment-1631876700)
- *“比我亲自上手搭建并做出最初几个可用版本的速度快太多了。”* —— [X 上的 Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
- *“感谢 Aider！它真的让人感觉像是看到了编程的未来。”* —— [Hacker News 上的 derwiki](https://news.ycombinator.com/item?id=38205643)
- *“太棒了。它让我能够去做以前觉得超出自己舒适区的事情。”* —— [Discord 上的 Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
- *“这个项目非常出色。”* —— [GitHub 上的 funkytaco](https://github.com/Aider-AI/aider/issues/112#issuecomment-1637429008)
- *“很棒的项目，绝对是我用过最好的 AI 编程助手。”* —— [GitHub 上的 joshuavial](https://github.com/Aider-AI/aider/issues/84)
- *“我真心喜欢使用 Aider……它让软件开发体验变得轻松太多了。”* —— [Discord 上的 principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
- *“我刚刚做完手术恢复中……Aider …… 让我得以继续维持工作效率。”* —— [Reddit 上的 codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
- *“我是 Aider 成瘾者。我在更短的时间内完成了更多工作。”* —— [Discord 上的 dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
- *“Aider……毫无悬念地甩开其他所有工具，根本没有任何可比性。”* —— [Discord 上的 SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
- *“Aider 太棒了，配合 Sonnet 3.5 使用简直令人脑洞大开。”* —— [Discord 上的 Josh Dingus](https://discord.com/channels/1131200896827654144/1133060684540813372/1262374225298198548)
- *“毫无疑问，这是迄今为止最好的 AI 编程助手工具。”* —— [YouTube 上的 IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
- *“[Aider] 彻底改变了我日常的编码工作流。它……能改变你的生活，这简直令人难以置信。”* —— [Discord 上的 maledorak](https://discord.com/channels/1131200896827654144/1131200896827654149/1258453375620747264)
- *“针对现有代码库进行实际开发工作而言，这是最佳 Agent。”* —— [X 上的 Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
- *“我最喜欢的软件之一。在新范式上开辟道路！”* —— [X 上的 Chris Wall](https://x.com/chris65536/status/1905053299251798432)
- *“Aider 对我来说和我的工作是革命性的。”* —— [X 上的 Starry Hope](https://x.com/starryhopeblog/status/1904985812137132056)
- *“试试 Aider！这是体验‘氛围编程’（vibe coding）的最佳方式之一。”* —— [X 上的 Chris Wall](https://x.com/Chris65536/status/1905053418961391929)
- *“我彻底爱上 Aider 了。”* —— [Hacker News 上的 hztar](https://news.ycombinator.com/item?id=44035015)
- *“Aider 绝对是最佳选择。而且它是免费开源的。”* —— [Reddit 上的 AriyaSavakaLurker](https://www.reddit.com/r/ChatGPTCoding/comments/1ik16y6/whats_your_take_on_aider/mbip39n/)
- *“Aider 也是我的最佳拍档。”* —— [Reddit 上的 jzn21](https://www.reddit.com/r/ChatGPTCoding/comments/1heuvuo/aider_vs_cline_vs_windsurf_vs_cursor/m27dcnb/)
- *“试试 Aider，绝对值得。”* —— [Reddit 上的 jorgejhms](https://www.reddit.com/r/ChatGPTCoding/comments/1heuvuo/aider_vs_cline_vs_windsurf_vs_cursor/m27cp99/)
- *“我喜欢 aider :)”* —— [X 上的 Chenwei Cui](https://x.com/ccui42/status/1904965344999145698)
- *“Aider 是 LLM 代码生成中的精准工具……简洁、深思熟虑，能够进行外科手术般的修改……同时让开发者保持控制权。”* —— [X 上的 Reilly Sweetland](https://x.com/rsweetland/status/1904963807237259586)
- *“不敢相信 aider 一次就氛围编程出了跨越服务和 CLI 的、包含 650 行代码的功能特性。”* —— [Discord 上的 autopoietist](https://discord.com/channels/1131200896827654144/1131200896827654149/1355675042259796101)
- *“哦不，秘密藏不住了！没错，Aider 是市面上最好的编码工具。我强烈向任何人推荐它。”* —— [X 上的 Joshua D Vander Hook](https://x.com/jodavaho/status/1911154899057795218)
- *“多亏了 aider，我在过去两天里已经启动并完成三个个人项目”* —— [X 上的 joseph stalzyn](https://x.com/anitaheeder/status/1908338609645904160)
- *“使用 Aider 作为我的主力开发工具已经超过一年了……我真心热爱这个工具，难以用言语表达。”* —— [Discord 上的 koleok](https://discord.com/channels/1131200896827654144/1273248471394291754/1356727448372252783)
- *“Aider …… 是衡量其他工具的基准。”* —— [Hacker News 上的 BeetleB](https://news.ycombinator.com/item?id=43930201)
- *“aider 真的很酷”* —— [X 上的 kache](https://x.com/yacineMTB/status/1911224442430124387)