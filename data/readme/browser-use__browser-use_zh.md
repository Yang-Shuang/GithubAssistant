<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/2ccdb752-22fb-41c7-8948-857fc1ad7e24">
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/774a46d5-27a0-490c-b7d0-e65fcbbfa358">
  <img alt="在浅色模式下显示黑色 Browser Use 标志，深色模式下显示白色标志。" src="https://github.com/user-attachments/assets/2ccdb752-22fb-41c7-8948-857fc1ad7e24"  width="full">
</picture>

<div align="center">
    <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/9955dda9-ede3-4971-8ee0-91cbc3850125">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6797d09b-8ac3-4cb9-ba07-b289e080765a">
    <img alt="AI 浏览器智能体。" src="https://github.com/user-attachments/assets/9955dda9-ede3-4971-8ee0-91cbc3850125"  width="400">
    </picture>
</div>

<div align="center">
<a href="https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-downloads"><img src="https://media.browser-use.tools/badges/package" height="48" alt="Browser-Use 包下载统计"></a>
</div>

---

<div align="center">
<a href="#demos"><img src="https://media.browser-use.tools/badges/demos" alt="演示案例"></a>
<img width="16" height="1" alt="">
<a href="https://docs.browser-use.com"><img src="https://media.browser-use.tools/badges/docs" alt="文档"></a>
<img width="16" height="1" alt="">
<a href="https://browser-use.com/posts"><img src="https://media.browser-use.tools/badges/blog" alt="博客"></a>
<img width="16" height="1" alt="">
<a href="https://browsermerch.com"><img src="https://media.browser-use.tools/badges/merch" alt="周边商品"></a>
<img width="100" height="1" alt="">
<a href="https://github.com/browser-use/browser-use"><img src="https://media.browser-use.tools/badges/github" alt="GitHub Stars"></a>
<img width="4" height="1" alt="">
<a href="https://x.com/intent/user?screen_name=browser_use"><img src="https://media.browser-use.tools/badges/twitter" alt="Twitter"></a>
<img width="4" height="1" alt="">
<a href="https://link.browser-use.com/discord"><img src="https://media.browser-use.tools/badges/discord" alt="Discord"></a>
<img width="4" height="1" alt="">
<a href="https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-cloud"><img src="https://media.browser-use.tools/badges/cloud" height="48" alt="Browser-Use 云端服务"></a>
</div>

</br>

🌤️ 想跳过环境配置？直接使用我们的 <b>[云端版](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-skip-setup)</b>，享受更快、可扩展且具备隐身能力的浏览器自动化体验！

# 🤖 LLM（大语言模型）快速入门

1. 引导你常用的编码智能体（Cursor、Claude Code 等）访问 [Agents.md](https://docs.browser-use.com/llms-full.txt)
2. 开始编写提示词并运行吧！

<br/>

# 👋 手动操作快速入门

**1. 创建环境并使用 [uv](https://docs.astral.sh/uv/)（Python>=3.11）安装 Browser-Use：**
```bash
uv init && uv add browser-use && uv sync
# uvx browser-use install  # 如果你未安装 Chromium，请运行此行
```

**2. [可选] 从 [Browser Use Cloud](https://cloud.browser-use.com/new-api-key?utm_source=github&utm_medium=readme-quickstart-api-key) 获取 API 密钥：**
```
# .env
BROWSER_USE_API_KEY=your-key
# GOOGLE_API_KEY=your-key
# ANTHROPIC_API_KEY=your-key
```

**3. 运行你的第一个智能体：**
```python
from browser_use import Agent, Browser, ChatBrowserUse
# from browser_use import ChatGoogle  # ChatGoogle(model='gemini-3-flash-preview')
# from browser_use import ChatAnthropic  # ChatAnthropic(model='claude-sonnet-4-6')
import asyncio

async def main():
    browser = Browser(
        # use_cloud=True,  # 在 Browser Use Cloud 上使用隐身浏览器
    )

    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(),
        # llm=ChatGoogle(model='gemini-3-flash-preview'),
        # llm=ChatAnthropic(model='claude-sonnet-4-6'),
        browser=browser,
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
```

查看[库文档](https://docs.browser-use.com/open-source/introduction)和[云端文档](https://docs.cloud.browser-use.com?utm_source=github&utm_medium=readme-cloud-docs)了解更多！

<br/>

# 开源版与云端版对比

<picture>
  <source media="(prefers-color-scheme: light)" srcset="static/accuracy_by_model_light.png">
  <source media="(prefers-color-scheme: dark)" srcset="static/accuracy_by_model_dark.png">
  <img alt="BU Bench V1 - LLM 成功率" src="static/accuracy_by_model_light.png" width="100%">
</picture>

我们在 100 个真实浏览器任务上对 Browser-Use 进行了基准测试。完整基准测试为开源项目：**[browser-use/benchmark](https://github.com/browser-use/benchmark)**。

**使用开源智能体**
- 你需要使用 [自定义工具](https://docs.browser-use.com/customize/tools/basics) 或进行深度的代码级集成
- 我们建议搭配我们的 [云端浏览器](https://docs.browser-use.com/open-source/customize/browser/remote) 以获得领先的隐身能力、代理轮换和扩展性
- 或者完全在自有机器上自托管开源智能体

**使用 [全托管云端智能体](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-hosted-agent)（推荐）**
- 处理复杂任务时能力更强（见上方图表）
- 起步和扩展的最简单方式
- 提供最佳隐身效果，支持代理轮换与验证码识别
- 支持 1000+ 种集成（Gmail、Slack、Notion 等）
- 持久化文件系统与内存

<br/>

# 演示案例


### 📋 表单填写
#### Task = "用我的简历和信息填写这份求职申请。"
![Job Application Demo](https://github.com/user-attachments/assets/57865ee6-6004-49d5-b2c2-6dff39ec2ba9)
[示例代码 ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/apply_to_job.py)


### 🍎 杂货购物
#### Task = "将这份商品清单添加到我的 Instacart 购物车中。"

https://github.com/user-attachments/assets/a6813fa7-4a7c-40a6-b4aa-382bf88b1850

[示例代码 ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/buy_groceries.py)


### 💻 个人助理
#### Task = "帮我找一下组装定制电脑所需的配件。"

https://github.com/user-attachments/assets/ac34f75c-057a-43ef-ad06-5b2c9d42bf06

[示例代码 ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/pcpartpicker.py)


### 💡查看 [更多示例 ↗](https://docs.browser-use.com/examples)，别忘了给我们点个 Star！

<br/>

# 🚀 模板快速入门

**想更快上手？** 生成一个开箱即用的模板：

```bash
uvx browser-use init --template default
```

这将生成一个 `browser_use_default.py` 文件，内含可运行的示例。可用模板包括：
- `default` - 最小化配置，快速开始
- `advanced` - 包含所有配置选项及详细注释
- `tools` - 自定义工具扩展智能体的示例代码

你也可以指定自定义输出路径：
```bash
uvx browser-use init --template default --output my_agent.py
```

<br/>

# 💻 CLI（命令行界面）

从命令行快速、持久地执行浏览器自动化操作：

```bash
browser-use open https://example.com    # Navigate to URL
browser-use state                       # See clickable elements
browser-use click 5                     # Click element by index
browser-use type "Hello"                # Type text
browser-use screenshot page.png         # Take screenshot
browser-use close                       # Close browser
```

CLI 会在命令执行间保持浏览器运行状态，以便快速迭代。查看所有命令请查阅 [CLI 文档](browser_use/skill_cli/README.md)。

### Claude Code 技能模块

针对 [Claude Code](https://claude.ai/code)，安装该技能以启用 AI 辅助的浏览器自动化：

```bash
mkdir -p ~/.claude/skills/browser-use
curl -o ~/.claude/skills/browser-use/SKILL.md \
  https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md
```

<br/>

## 集成、托管服务、自定义工具、MCP 等功能详见我们的 [文档 ↗](https://docs.browser-use.com)

<br/>

# FAQ（常见问题）

<details>
<summary><b>最佳模型推荐是什么？</b></summary>

我们针对浏览器自动化任务专门优化了 **ChatBrowserUse()**。平均而言，它比其他模型快 3-5 倍完成任务，且准确率处于行业领先水平。

**定价（每百万 Token）：**
- 输入 Token：$0.20
- 缓存输入 Token：$0.02
- 输出 Token：$2.00

其他大语言模型提供商请查阅我们的 [支持的模型文档](https://docs.browser-use.com/supported-models)。
</details>

<details>
<summary><b>我应该将 Browser-Use 的系统提示词与开源预览版模型配合使用吗？</b></summary>

是的。如果你在使用 `ChatBrowserUse(model='browser-use/bu-30b-a3b-preview')` 搭配普通 `Agent(...)`，Browser-Use 仍会为你发送默认的智能体系统提示词。

你**不需要**仅仅因为切换到开源预览版模型就额外添加自定义的“Browser-Use 系统消息”。仅在有意针对你的任务定制默认行为时，才使用 `extend_system_message` 或 `override_system_message`。

如果追求最佳默认速度与准确率，我们仍推荐更新的托管版 `bu-*` 模型。如果使用开源预览版模型，配置方式保持不变，仅需修改 `model=` 的值即可。
</details>

<details>
<summary><b>我可以为智能体使用自定义工具吗？</b></summary>

可以！你可以添加自定义工具来扩展智能体的能力：

```python
from browser_use import Tools

tools = Tools()

@tools.action(description='Description of what this tool does.')
def custom_tool(param: str) -> str:
    return f"Result: {param}"

agent = Agent(
    task="Your task",
    llm=llm,
    browser=browser,
    tools=tools,
)
```

</details>

<details>
<summary><b>可以免费使用吗？</b></summary>

是的！Browser-Use 是开源且免费的。你只需选择一个大语言模型提供商（如 OpenAI、Google、ChatBrowserUse，或使用 Ollama 运行本地模型）。
</details>

<details>
<summary><b>服务条款</b></summary>

本开源库采用 MIT 许可证授权。关于 Browser-Use 的服务与数据政策，请参阅我们的 [服务条款](https://browser-use.com/legal/terms-of-service) 和 [隐私政策](https://browser-use.com/privacy/)。
</details>

<details>
<summary><b>如何处理身份验证（登录）？</b></summary>

请查阅我们的身份验证示例：
- [使用真实的浏览器配置文件](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py) - 复用你现有的 Chrome 配置及已保存的登录信息
- 如需使用带收件箱的临时账号，请选择 AgentMail
- 若要将你的认证配置文件同步至远程浏览器，请运行 `curl -fsSL https://browser-use.com/profile.sh | BROWSER_USE_API_KEY=XXXX sh`（将 XXXX 替换为你的 API 密钥）

这些示例展示了如何无缝维持会话并处理身份验证。
</details>

<details>
<summary><b>如何解决验证码（CAPTCHA）？</b></summary>

处理验证码需要更完善的浏览器指纹伪装和代理支持。请使用 [Browser-Use 云端](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-faq-captcha)，它提供专为规避检测和验证码挑战而设计的隐身浏览器。
</details>

<details>
<summary><b>如何投入生产环境使用？</b></summary>

Chrome 会消耗大量内存，并行运行多个智能体也较难管理。

对于生产环境用途，请使用我们的 [Browser-Use 云端 API](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-faq-production)，它负责处理：
- 可扩展的浏览器基础设施
- 内存管理
- 代理轮换
- 隐身浏览器指纹伪装
- 高性能并行执行
</details>

<br/>

<div align="center">

**告诉你的电脑该做什么，它就能帮你完成。**

<img src="https://github.com/user-attachments/assets/06fa3078-8461-4560-b434-445510c1766f" width="400"/>

[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/intent/user?screen_name=mamagnus00)
&emsp;&emsp;&emsp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/intent/user?screen_name=gregpr07)

</div>

<div align="center"> 由苏黎世和旧金山团队用 ❤️ 打造 </div>