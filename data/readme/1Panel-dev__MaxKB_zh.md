<p align="center"><img src= "https://github.com/1Panel-dev/maxkb/assets/52996290/c0694996-0eed-40d8-b369-322bf2a380bf" alt="MaxKB" width="300" /></p>
<h3 align="center">构建企业级智能体的开源平台</h3>
<h3 align="center">强大易用的企业级智能体平台</h3>
<p align="center"><a href="https://trendshift.io/repositories/9113" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9113" alt="1Panel-dev%2FMaxKB | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a></p>
<p align="center">
  <a href="https://www.gnu.org/licenses/gpl-3.0.html#license-text"><img src="https://img.shields.io/github/license/1Panel-dev/maxkb?color=%231890FF" alt="License: GPL v3"></a>
  <a href="https://github.com/1Panel-dev/maxkb/releases/latest"><img src="https://img.shields.io/github/v/release/1Panel-dev/maxkb" alt="Latest release"></a>
  <a href="https://github.com/1Panel-dev/maxkb"><img src="https://img.shields.io/github/stars/1Panel-dev/maxkb?color=%231890FF&style=flat-square" alt="Stars"></a>    
  <a href="https://hub.docker.com/r/1panel/maxkb"><img src="https://img.shields.io/docker/pulls/1panel/maxkb?label=downloads" alt="Download"></a><br/>
 [<a href="/README_CN.md">中文(简体)</a>] | [<a href="/README.md">English</a>] 
</p>
<hr/>

MaxKB（全称 Max Knowledge Brain）是一款构建企业级智能体的开源平台。MaxKB 集成了 RAG（检索增强生成）流水线，支持强大的工作流引擎，并提供先进的 MCP 工具调用能力。MaxKB 广泛应用于智能客服、企业内部知识库、学术研究及教育等场景。

- **RAG Pipeline**：支持直接上传文档或自动爬取在线文档，具备文本自动分块与向量化功能。这能有效降低大模型的幻觉问题，提供更优质的智能问答交互体验。
- **Agentic Workflow**：内置强大的工作流引擎、函数库及 MCP 工具调用功能，支持对 AI 流程进行编排，满足复杂业务场景的需求。
- **Seamless Integration**：支持零代码快速接入第三方业务系统，为现有系统快速赋予智能问答能力，提升用户满意度。
- **Model-Agnostic**：兼容多种大语言模型（LLM），包括私有化部署模型（如 DeepSeek、Llama、Qwen 等）和公有云模型（如 OpenAI、Claude、Gemini、MiniMax 等）。
- **Multi Modal**：原生支持文本、图片、音频和视频的输入与输出。

## Quick start

执行以下命令，使用 Docker 启动 MaxKB 容器：

```bash
docker run -d --name=maxkb --restart=always -p 8080:8080 -v ~/.maxkb:/opt/maxkb 1panel/maxkb
```

通过浏览器访问 MaxKB Web 界面 `http://your_server_ip:8080`，默认管理员账号信息如下：

- username: admin
- password: MaxKB@123..

中国用户如遇到 Docker 镜像 Pull 失败问题，请参照该 [离线安装文档](https://maxkb.cn/docs/v2/installation/offline_installtion/) 进行安装。

## Screenshots

<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/eb285512-a66a-4752-8941-c65ed1592238" alt="MaxKB Demo1"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/f732f1f5-472c-4fd2-93c1-a277eda83d04" alt="MaxKB Demo2"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/c927474a-9a23-4830-822f-5db26025c9b2" alt="MaxKB Demo3"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/e6268996-a46d-4e58-9f30-31139df78ad2" alt="MaxKB Demo4"   /></td>
  </tr>
</table>

## Technical stack

- Frontend：[Vue.js](https://vuejs.org/)
- Backend：[Python / Django](https://www.djangoproject.com/)
- LLM Framework：[LangChain](https://www.langchain.com/)
- Database：[PostgreSQL + pgvector](https://www.postgresql.org/)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=1Panel-dev/MaxKB&type=Date)](https://star-history.com/#1Panel-dev/MaxKB&Date)

## License

本软件依据 GNU 通用公共许可证第 3 版（GPLv3，以下简称“本协议”）授权；除非符合本协议规定，否则不得使用此文件。您可以在以下网址获取许可证副本：

<https://www.gnu.org/licenses/gpl-3.0.html>

除非适用法律要求或书面同意，否则按“原样”分发基于本协议许可的软件，不附带任何形式的明示或暗示担保或条件。详见许可证关于权限和限制的特定条款。