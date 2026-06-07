<!---
Copyright 2023 The Qwen team, Alibaba Group. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

[中文版](https://github.com/QwenLM/Qwen-Agent/blob/main/README_CN.md) ｜ 英文版

<p align="center">
    <img src="https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/logo_qwen_agent.png" width="400"/>
<p>
<br>

<p align="center">
          💜 <a href="https://chat.qwen.ai/"><b>Qwen Chat</b></a>&nbsp&nbsp | &nbsp&nbsp🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/qwen">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://qwenlm.github.io/">博客</a> &nbsp&nbsp ｜ &nbsp&nbsp📖 <a href="https://qwenlm.github.io/Qwen-Agent/en/">文档</a>

<br>
📊 <a href="https://qwenlm.github.io/Qwen-Agent/en/benchmarks/deepplanning/">基准测试</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png">微信</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp
</p>


Qwen-Agent 是一个基于通义千问（Qwen）的指令遵循、工具使用、规划及记忆能力来开发大语言模型（LLM）应用的框架。它附带了浏览器助手（Browser Assistant）、代码解释器（Code Interpreter）和自定义助手等示例应用。目前，Qwen-Agent 作为 [Qwen Chat](https://chat.qwen.ai/) 的后端运行。

# 更新日志
* 🔥🔥🔥2026年2月16日：开源了 Qwen3.5。使用示例请参考 [Qwen3.5 Agent Demo](./examples/assistant_qwen3.5.py)。
* 2026年1月27日：开源了智能体评估基准测试 [DeepPlanning](https://qwenlm.github.io/Qwen-Agent/en/benchmarks/deepplanning/)，并新增了 Qwen-Agent [文档](https://qwenlm.github.io/Qwen-Agent/en/guide/)。
* 2025年9月23日：新增 [Qwen3-VL 工具调用示例](./examples/cookbook_think_with_images.ipynb)，支持放大、图像搜索和网页搜索等工具。
* 2025年7月23日：新增 [Qwen3-Coder 工具调用示例](./examples/assistant_qwen3_coder.py)；新增了原生 API 工具调用接口支持，例如使用 vLLM 内置的工具调用解析。
* 2025年5月1日：新增 [Qwen3 工具调用示例](./examples/assistant_qwen3.py)，并新增了 [MCP Cookbooks](./examples/)。
* 2025年3月18日：支持 `reasoning_content` 字段；调整了默认的 [函数调用模板](./qwen_agent/llm/fncall_prompts/nous_fncell_prompt.py)，适用于 Qwen2.5 系列通用模型和 QwQ-32B。如需使用旧版模板，请参考 [示例](./examples/function_calling.py) 进行参数传递。
* 2025年3月7日：新增 [QwQ-32B 工具调用示例](./examples/assistant_qwq.py)。支持并行、多步和多轮次工具调用。
* 2024年12月3日：GUI 升级至基于 Gradio 5。注意：GUI 需要 Python 3.10 或更高版本。
* 2024年9月18日：新增 [Qwen2.5-Math 示例](./examples/tir_math.py) 以展示 Qwen2.5-Math 的工具集成推理（Tool-Integrated Reasoning）能力。注意：Python 执行器未进行沙盒隔离，仅用于本地测试，不可用于生产环境。

# 快速开始

## 安装

- 从 PyPI 安装稳定版：
```bash
pip install -U "qwen-agent[gui,rag,code_interpreter,mcp]"
# Or use `pip install -U qwen-agent` for the minimal requirements.
# The optional requirements, specified in double brackets, are:
#   [gui] for Gradio-based GUI support;
#   [rag] for RAG support;
#   [code_interpreter] for Code Interpreter support;
#   [mcp] for MCP support.
```

- 或者，你也可以从源码安装最新开发版：
```bash
git clone https://github.com/QwenLM/Qwen-Agent.git
cd Qwen-Agent
pip install -e ./"[gui,rag,code_interpreter,mcp]"
# Or `pip install -e ./` for minimal requirements.
```

## 准备：模型服务

你可以使用阿里云 [DashScope](https://help.aliyun.com/zh/dashscope/developer-reference/quick-start) 提供的模型服务，也可以使用开源的 Qwen 模型自行部署和使用你的模型服务。

- 如果选择使用 DashScope 提供的模型服务，请确保将环境变量 `DASHSCOPE_API_KEY` 设置为你唯一的 DashScope API 密钥。

- 或者，如果你希望自行部署和使用模型服务，请按照 Qwen2 README 中的说明部署一个兼容 OpenAI API 的服务。具体而言，可参考 [vLLM](https://github.com/QwenLM/Qwen2?tab=readme-ov-file#vllm) 部分进行高吞吐量 GPU 部署，或参考 [Ollama](https://github.com/QwenLM/Qwen2?tab=readme-ov-file#ollama) 部分进行本地 CPU (+GPU) 部署。
对于 QwQ 和 Qwen3 模型，建议**不要**添加 `--enable-auto-tool-choice` 和 `--tool-call-parser hermes` 参数，因为 Qwen-Agent 会自行解析来自 vLLM 的工具输出。
对于 Qwen3-Coder，建议同时启用上述两个参数，使用 vLLM 内置的工具解析功能，并结合 `use_raw_api` 参数 [使用方法](#how-to-pass-llm-parameters-to-the-agent)。

## 开发你自己的 Agent

Qwen-Agent 提供了原子组件（如继承自 `class BaseChatModel` 的 LLM，以及内置 [函数调用](https://github.com/QwenLM/Qwen-Agent/blob/main/examples/function_calling.py) 功能；和继承自 `class BaseTool` 的工具），以及高级组件（如派生自 `class Agent` 的智能体）。

以下示例展示了如何创建一个能够读取 PDF 文件、使用工具并包含自定义工具的 agent：

```py
import pprint
import urllib.parse
import json5
from qwen_agent.agents import Assistant
from qwen_agent.tools.base import BaseTool, register_tool
from qwen_agent.utils.output_beautify import typewriter_print


# Step 1 (Optional): Add a custom tool named `my_image_gen`.
@register_tool('my_image_gen')
class MyImageGen(BaseTool):
    # The `description` tells the agent the functionality of this tool.
    description = 'AI painting (image generation) service, input text description, and return the image URL drawn based on text information.'
    # The `parameters` tell the agent what input parameters the tool has.
    parameters = [{
        'name': 'prompt',
        'type': 'string',
        'description': 'Detailed description of the desired image content, in English',
        'required': True
    }]

    def call(self, params: str, **kwargs) -> str:
        # `params` are the arguments generated by the LLM agent.
        prompt = json5.loads(params)['prompt']
        prompt = urllib.parse.quote(prompt)
        return json5.dumps(
            {'image_url': f'https://image.pollinations.ai/prompt/{prompt}'},
            ensure_ascii=False)


# Step 2: Configure the LLM you are using.
llm_cfg = {
    # Use the model service provided by DashScope:
    'model': 'qwen-max-latest',
    'model_type': 'qwen_dashscope',
    # 'api_key': 'YOUR_DASHSCOPE_API_KEY',
    # It will use the `DASHSCOPE_API_KEY' environment variable if 'api_key' is not set here.

    # Use a model service compatible with the OpenAI API, such as vLLM or Ollama:
    # 'model': 'Qwen2.5-7B-Instruct',
    # 'model_server': 'http://localhost:8000/v1',  # base_url, also known as api_base
    # 'api_key': 'EMPTY',

    # (Optional) LLM hyperparameters for generation:
    'generate_cfg': {
        'top_p': 0.8
    }
}

# Step 3: Create an agent. Here we use the `Assistant` agent as an example, which is capable of using tools and reading files.
system_instruction = '''After receiving the user's request, you should:
- first draw an image and obtain the image url,
- then run code `request.get(image_url)` to download the image,
- and finally select an image operation from the given document to process the image.
Please show the image using `plt.show()`.'''
tools = ['my_image_gen', 'code_interpreter']  # `code_interpreter` is a built-in tool for executing code. For configuration details, please refer to the FAQ.
files = ['./examples/resource/doc.pdf']  # Give the bot a PDF file to read.
bot = Assistant(llm=llm_cfg,
                system_message=system_instruction,
                function_list=tools,
                files=files)

# Step 4: Run the agent as a chatbot.
messages = []  # This stores the chat history.
while True:
    # For example, enter the query "draw a dog and rotate it 90 degrees".
    query = input('\nuser query: ')
    # Append the user query to the chat history.
    messages.append({'role': 'user', 'content': query})
    response = []
    response_plain_text = ''
    print('bot response:')
    for response in bot.run(messages=messages):
        # Streaming output.
        response_plain_text = typewriter_print(response, response_plain_text)
    # Append the bot responses to the chat history.
    messages.extend(response)
```

除了使用内置的 agent 实现（如 `class Assistant`），你还可以通过继承 `class Agent` 来开发自己的 agent 实现。

该框架还提供了便捷的 GUI 界面，支持快速部署 Gradio Demo 用于 Agent。例如在上述情况下，你可以使用以下代码快速启动一个 Gradio Demo：

```py
from qwen_agent.gui import WebUI
WebUI(bot).run()  # bot is the agent defined in the above code, we do not repeat the definition here for saving space.
```
现在你可以在 Web UI 中与 Agent 对话了。更多使用方法请参考 [examples](https://github.com/QwenLM/Qwen-Agent/blob/main/examples) 目录。

# FAQ
## 如何使用代码解释器工具？

我们基于本地 Docker 容器实现了一个代码解释器工具。你可以为你的 agent 启用内置的 `code_interpreter` 工具，使其能够根据特定场景自主编写代码，在隔离的沙盒环境中安全执行，并返回执行结果。

⚠️ **注意**：在使用此工具前，请确保你的本地操作系统已安装并运行 Docker。首次构建容器镜像所需的时间取决于你的网络状况。Docker 的安装与设置说明请参考 [官方文档](https://docs.docker.com/desktop/)。


## 如何使用 MCP？

你可以在开源的 [MCP 服务器网站](https://github.com/modelcontextprotocol/servers) 上选择所需的工具，并配置相关环境变量。

MCP 调用格式示例：
```
{
    "mcpServers": {
        "memory": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-memory"]
        },
        "filesystem": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
        },
        "sqlite" : {
            "command": "uvx",
            "args": [
                "mcp-server-sqlite",
                "--db-path",
                "test.db"
            ]
        }
    }
}
```
更多细节请参考 [MCP 使用示例](./examples/assistant_mcp_sqlite_bot.py)

运行此示例所需的依赖如下：
```
# Node.js (Download and install the latest version from the Node.js official website)
# uv 0.4.18 or higher (Check with uv --version)
# Git (Check with git --version)
# SQLite (Check with sqlite3 --version)

# For macOS users, you can install these components using Homebrew:
brew install uv git sqlite3

# For Windows users, you can install these components using winget:
winget install --id=astral-sh.uv -e
winget install git.git sqlite.sqlite
```
## 是否支持函数调用（即工具调用）？

是的。LLM 类提供了 [函数调用](https://github.com/QwenLM/Qwen-Agent/blob/main/examples/function_calling.py) 功能。此外，部分 Agent 类也是基于函数调用能力构建的，例如 FnCallAgent 和 ReActChat。

当前默认的工具调用模板原生支持**并行函数调用**。

## 如何向 Agent 传递 LLM 参数？
```py
llm_cfg = {
    # The model name being used:
    'model': 'qwen3-32b',
    # The model service being used:
    'model_type': 'qwen_dashscope',
    # If 'api_key' is not set here, it will default to reading the `DASHSCOPE_API_KEY` environment variable:
    'api_key': 'YOUR_DASHSCOPE_API_KEY',

    # Using an OpenAI API compatible model service, such as vLLM or Ollama:
    # 'model': 'qwen3-32b',
    # 'model_server': 'http://localhost:8000/v1',  # base_url, also known as api_base
    # 'api_key': 'EMPTY',

    # (Optional) LLM hyperparameters:
    'generate_cfg': {
        # This parameter will affect the tool-call parsing logic. Default is False:
          # Set to True: when content is `<think>this is the thought</think>this is the answer`
          # Set to False: when response consists of reasoning_content and content
        # 'thought_in_content': True,

        # tool-call template: default is nous (recommended for qwen3):
        # 'fncall_prompt_type': 'nous'

        # Maximum input length, messages will be truncated if they exceed this length, please adjust according to model API:
        # 'max_input_tokens': 58000

        # Parameters that will be passed directly to the model API, such as top_p, enable_thinking, etc., according to the API specifications:
        # 'top_p': 0.8

        # Using the API's native tool call interface
        # 'use_raw_api': True,
    }
}
```

## 如何对涉及百万 token 的超长文档进行问答？

我们已发布 [一种快速的 RAG 解决方案](https://github.com/QwenLM/Qwen-Agent/blob/main/examples/assistant_rag.py)，以及 [一个昂贵但具有竞争力的 agent](https://github.com/QwenLM/Qwen-Agent/blob/main/examples/parallel_doc_qa.py) 用于超长文档问答。它们在两项极具挑战性的基准测试中表现优于原生长上下文模型，且效率更高；在涉及百万 token 上下文的“大海捞针”单针压力测试中也表现完美。技术细节请参阅 [博客](https://qwenlm.github.io/blog/qwen-agent-2405/)。

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/assets/qwen_agent/qwen-agent-2405-blog-long-context-results.png" width="400"/>
<p>

# 应用：BrowserQwen

BrowserQwen 是基于 Qwen-Agent 构建的浏览器助手。详细信息请参阅其 [文档](https://github.com/QwenLM/Qwen-Agent/blob/main/browser_qwen.md)。

# 免责声明

基于 Docker 容器的代码解释器仅挂载了指定的工作目录并实现了基础沙盒隔离，但在生产环境中使用时仍需谨慎。