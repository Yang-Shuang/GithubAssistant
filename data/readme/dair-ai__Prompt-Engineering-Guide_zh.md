# 提示工程指南

<h5 align="center">
  赞助方&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://serpapi.com/"><img src="https://cdn.rawgit.com/standard/standard/master/docs/logos/serpapi.png" height=35 valign="middle"></a>
</h5>

提示工程是一门相对新兴的学科，旨在开发和优化提示词（prompts），以便在各种应用和研究课题中高效地使用语言模型（LM）。掌握提示工程技术有助于更好地理解大型语言模型（LLM）的能力与局限性。研究人员利用提示工程来提升 LLM 在问答、算术推理等各类常见及复杂任务中的表现。开发者则利用它来设计稳健且高效的提示技巧，以对接 LLM 及其他工具。

鉴于业界对基于 LLM 开发的高度关注，我们编写了这本最新的提示工程指南，其中收录了所有与 LLM 提示工程相关的最新论文、学习教程、讲座视频、参考资料及工具。

🌐 [提示工程指南（网页版）](https://www.promptingguide.ai/)

🎉 我们很高兴在 DAIR.AI Academy 下推出全新的提示工程、RAG 和 AI Agents 课程。[立即加入](https://academy.dair.ai/pricing)!

这些课程旨在补充本指南，提供更注重实践的学习方式，帮助你深入了解提示工程、上下文工程（context engineering）及 AI Agents。 

使用优惠码 `PROMPTING20` 可额外享受 8 折优惠。

祝你提示愉快！

---
## 公告/更新

- 🎓 我们在 DAIR.AI Academy 现提供自定进度的提示工程课程。[立即加入](https://academy.dair.ai/pricing)! 
- 🎓 新增 LLM 提示工程课程！[在此报名](https://academy.dair.ai/courses/introduction-prompt-engineering)!
- 💼 我们现在提供多项 [服务](https://www.promptingguide.ai/services)，如企业培训、咨询和讲座。
- 🌐 现已支持 13 种语言！欢迎更多翻译贡献。
- 👩‍🎓 我们在 2024 年 1 月突破了 300 万学习者！
- 🎉 我们已在此推出指南的全新网页版 [here](https://www.promptingguide.ai/)
- 🔥 我们在 2023 年 2 月 21 日登上 Hacker News 榜首。
- 🎉 首期提示工程讲座视频已上线 [此处](https://youtu.be/dOxUroR57xs)

[加入我们的 Discord](https://discord.gg/YbMT8k6GfX)

[在 Twitter 上关注我们](https://twitter.com/dair_ai)

[订阅我们的 YouTube 频道](https://www.youtube.com/channel/UCyna_OxOWL7IEuOwb7WhmxQ)

[订阅我们的 Newsletter](https://nlpnews.substack.com/)

---

## 指南
你也可以在我们新网站上找到最新的指南：[https://www.promptingguide.ai/](https://www.promptingguide.ai/)。

- [提示工程 - 简介](https://www.promptingguide.ai/introduction)
  - [提示工程 - LLM 设置](https://www.promptingguide.ai/introduction/settings)
  - [提示工程 - 提示基础](https://www.promptingguide.ai/introduction/basics)
  - [提示工程 - 提示元素](https://www.promptingguide.ai/introduction/elements)
  - [提示工程 - 设计提示的通用技巧](https://www.promptingguide.ai/introduction/tips)
  - [提示工程 - 提示示例](https://www.promptingguide.ai/introduction/examples)
- [提示工程 - 技术方法](https://www.promptingguide.ai/techniques)
  - [提示工程 - 零样本提示（Zero-Shot）](https://www.promptingguide.ai/techniques/zeroshot)
  - [提示工程 - 少样本提示（Few-Shot）](https://www.promptingguide.ai/techniques/fewshot)
  - [提示工程 - 思维链提示（Chain-of-Thought）](https://www.promptingguide.ai/techniques/cot)
  - [提示工程 - 自洽性提示（Self-Consistency）](https://www.promptingguide.ai/techniques/consistency)
  - [提示工程 - 知识生成提示（Generate Knowledge Prompting）](https://www.promptingguide.ai/techniques/knowledge)
  - [提示工程 - 提示词串联（Prompt Chaining）](https://www.promptingguide.ai/techniques/prompt_chaining)
  - [提示工程 - 思维树（Tree of Thoughts, ToT）](https://www.promptingguide.ai/techniques/tot)
  - [提示工程 - 检索增强生成（RAG）](https://www.promptingguide.ai/techniques/rag)
  - [提示工程 - 自动推理与工具使用（ART）](https://www.promptingguide.ai/techniques/art)
  - [提示工程 - 自动提示词工程师（APE）](https://www.promptingguide.ai/techniques/ape)
  - [提示工程 - 主动提示（Active-Prompt）](https://www.promptingguide.ai/techniques/activeprompt)
  - [提示工程 - 定向刺激提示（DSP）](https://www.promptingguide.ai/techniques/dsp)
  - [提示工程 - 程序辅助语言模型（PAL）](https://www.promptingguide.ai/techniques/pal)
  - [提示工程 - ReAct 提示](https://www.promptingguide.ai/techniques/react)
  - [提示工程 - 多模态思维链提示](https://www.promptingguide.ai/techniques/multimodalcot)
  - [提示工程 - 图提示（Graph Prompting）](https://www.promptingguide.ai/techniques/graph)
- [提示工程 - 应用场景](https://www.promptingguide.ai/applications)
  - [提示工程 - 函数调用（Function Calling）](https://www.promptingguide.ai/applications/function_calling)
  - [提示工程 - 生成数据](https://www.promptingguide.ai/applications/generating)
  - [提示工程 - 为 RAG 生成合成数据集](https://www.promptingguide.ai/applications/synthetic_rag)
  - [提示工程 - 应对生成数据集的多样性](https://www.promptingguide.ai/applications/generating_textbooks)
  - [提示工程 - 生成代码](https://www.promptingguide.ai/applications/coding)
  - [提示工程 - 毕业生职位分类案例研究](https://www.promptingguide.ai/applications/workplace_casestudy)
- [提示工程 - 提示词中心（Prompt Hub）](https://www.promptingguide.ai/prompts)
  - [提示工程 - 分类](https://www.promptingguide.ai/prompts/classification)
  - [提示工程 - 编程](https://www.promptingguide.ai/prompts/coding)
  - [提示工程 - 创意生成](https://www.promptingguide.ai/prompts/creativity)
  - [提示工程 - 评估](https://www.promptingguide.ai/prompts/evaluation)
  - [提示工程 - 信息抽取](https://www.promptingguide.ai/prompts/information-extraction)
  - [提示工程 - 图像生成](https://www.promptingguide.ai/prompts/image-generation)
  - [提示工程 - 数学](https://www.promptingguide.ai/prompts/mathematics)
  - [提示工程 - 问答](https://www.promptingguide.ai/prompts/question-answering)
  - [提示工程 - 推理](https://www.promptingguide.ai/prompts/reasoning)
  - [提示工程 - 文本摘要](https://www.promptingguide.ai/prompts/text-summarization)
  - [提示工程 - 真实性](https://www.promptingguide.ai/prompts/truthfulness)
  - [提示工程 - 对抗性提示（Adversarial Prompting）](https://www.promptingguide.ai/prompts/adversarial-prompting)
- [提示工程 - 模型支持](https://www.promptingguide.ai/models)
  - [提示工程 - ChatGPT](https://www.promptingguide.ai/models/chatgpt)
  - [提示工程 - Code Llama](https://www.promptingguide.ai/models/code-llama)
  - [提示工程 - Flan](https://www.promptingguide.ai/models/flan)
  - [提示工程 - Gemini](https://www.promptingguide.ai/models/gemini)
  - [提示工程 - GPT-4](https://www.promptingguide.ai/models/gpt-4)
  - [提示工程 - LLaMA](https://www.promptingguide.ai/models/llama)
  - [提示工程 - Mistral 7B](https://www.promptingguide.ai/models/mistral-7b)
  - [提示工程 - Mixtral](https://www.promptingguide.ai/models/mixtral)
  - [提示工程 - OLMo](https://www.promptingguide.ai/models/olmo)
  - [提示工程 - Phi-2](https://www.promptingguide.ai/models/phi-2)
  - [提示工程 - 模型合集](https://www.promptingguide.ai/models/collection)
- [提示工程 - 风险与滥用防范](https://www.promptingguide.ai/risks)
  - [提示工程 - 对抗性提示](https://www.promptingguide.ai/risks/adversarial)
  - [提示工程 - 事实准确性](https://www.promptingguide.ai/risks/factuality)
  - [提示工程 - 偏见问题](https://www.promptingguide.ai/risks/biases)
- [提示工程 - 论文精选](https://www.promptingguide.ai/papers)
  - [提示工程 - 综述类](https://www.promptingguide.ai/papers#overviews)
  - [提示工程 - 方法类](https://www.promptingguide.ai/papers#approaches)
  - [提示工程 - 应用类](https://www.promptingguide.ai/papers#applications)
  - [提示工程 - 合集类](https://www.promptingguide.ai/papers#collections)
- [提示工程 - 工具推荐](https://www.promptingguide.ai/tools)
- [提示工程 - Notebook 示例](https://www.promptingguide.ai/notebooks)
- [提示工程 - 数据集](https://www.promptingguide.ai/datasets)
- [提示工程 - 延伸阅读](https://www.promptingguide.ai/readings)


---
## 讲座视频

我们发布了一小时长的讲座视频，全面概述了提示技巧、应用及工具。
- [视频讲座](https://youtu.be/dOxUroR57xs)
- [含代码的 Notebook](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-lecture.ipynb)
- [演示文稿（Slides）](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/lecture/Prompt-Engineering-Lecture-Elvis.pdf)

---
## 本地运行指南

要在本地运行本指南（例如用于检查新翻译的正确性），你需要：

1. 安装 Node.js（版本需 >=18.0.0）
2. 若系统中未安装 `pnpm`，请进行安装。详细操作请参阅 [此处](https://pnpm.io/installation)。
3. 安装依赖项：运行命令 `pnpm i next react react-dom nextra nextra-theme-docs`
4. 启动指南服务：运行 `pnpm dev`
5. 在浏览器中访问 `http://localhost:3000/` 查看指南

---
## 媒体报道

我们的内容曾亮相于以下媒体：
- Wall Street Journal - [ChatGPT Can Give Great Answers. But Only If You Know How to Ask the Right Question](https://www.wsj.com/articles/chatgpt-ask-the-right-question-12d0f035)
- Forbes - [Mom, Dad, I Want To Be A Prompt Engineer](https://www.forbes.com/sites/craigsmith/2023/04/05/mom-dad-i-want-to-be-a-prompt-engineer/?sh=7f1213159c8e)
- Markettechpost - [Best Free Prompt Engineering Resources (2023)](https://www.marktechpost.com/2023/04/04/best-free-prompt-engineering-resources-2023/)


---
如果你在您的工作或研究中使用本指南，请按以下格式引用我们：

```
@article{Saravia_Prompt_Engineering_Guide_2022,
author = {Saravia, Elvis},
journal = {https://github.com/dair-ai/Prompt-Engineering-Guide},
month = {12},
title = {{Prompt Engineering Guide}},
year = {2022}
}
```

## 许可证

[MIT License](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/LICENSE.md)


如果你觉得内容有所遗漏，欢迎随时提交 Pull Request。我们始终欢迎反馈与建议，直接创建 Issue 即可！