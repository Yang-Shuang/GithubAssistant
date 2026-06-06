<div align="center">
  <p>
      <img width="800" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/Banner.png" alt="Star-history">
  </p>



<h3>全球领先的 OCR 工具包与文档 AI 引擎</h3>

English | [简体中文](./readme/README_cn.md) | [繁體中文](./readme/README_tcn.md) | [日本語](./readme/README_ja.md) | [한국어](./readme/README_ko.md) | [Français](./readme/README_fr.md) | [Русский](./readme/README_ru.md) | [Español](./readme/README_es.md) | [العربية](./readme/README_ar.md)

<!-- icon -->

[![PyPI Downloads](https://static.pepy.tech/badge/paddleocr)](https://pepy.tech/projects/paddleocr)
[![Used by](https://img.shields.io/badge/Used%20by-6k%2B%20repositories-blue)](https://github.com/PaddlePaddle/PaddleOCR/network/dependents)
![python](https://img.shields.io/badge/python-3.8~3.12-aff.svg)
![os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg)
![hardware](https://img.shields.io/badge/hardware-cpu%2C%20gpu%2C%20xpu%2C%20npu-yellow.svg)

[![AI Studio](https://img.shields.io/badge/PaddleOCR-_Offiical_Website-1927BA?logo=data:image/png;base64,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&labelColor=white)](https://www.paddleocr.com)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/PaddlePaddle/PaddleOCR)
[![License](https://img.shields.io/badge/license-Apache_2.0-green)](../LICENSE)

</div>






**PaddleOCR 以行业领先的精度，将 PDF 文档和图像转换为结构化的、可直接用于大语言模型（LLM）的数据（JSON/Markdown）。凭借超过 7 万颗星标，并获 Dify、RAGFlow 和 Cherry Studio 等顶级项目信赖，PaddleOCR 已成为构建智能 RAG（检索增强生成）与 Agent（智能体）应用的基石。**


## 🚀 核心特性

### 📄 智能文档解析（面向 LLM）
> *将杂乱的视觉信息转化为大语言模型时代所需的结构化数据。*

* **领先的文档视觉语言模型（VLM）**：搭载行业领先的轻量级文档解析模型 PaddleOCR-VL-1.6 (0.9B)。在 OmniDocBench v1.6 上准确率达 96.3%，在文本、公式和表格识别方面表现领先，并在古籍、生僻字、印章及图表理解能力上有显著提升，支持输出 **Markdown** 和 **JSON** 格式的结构化结果。
* **结构感知转换**：基于 PP-StructureV3 技术，无缝将复杂 PDF 和图像转换为 **Markdown** 或 **JSON**。与 PaddleOCR-VL 系列模型相比，它提供更细粒度的坐标信息（如表格单元格坐标、文本框坐标等）。
* **生产级效率**：以极小的资源占用实现商用级精度。在公开基准测试中超越众多闭源方案，同时兼顾边缘端与云端部署的资源效率。

### 🔍 通用文本识别（场景 OCR）
> *全球高速、多语言文字检测的行业标杆。*

* **支持 100+ 种语言**：原生支持庞大的全球语种库。**PP-OCRv5** 单模型优雅处理中英日混排及拼音等多语言混合文档。
* **全面掌握复杂场景元素**：除标准文本识别外，广泛支持身份证、街景、书籍、工业零件等多样环境下的自然场景文字检测（Text Spotting）。
* **性能飞跃**：PP-OCRv5 较上一代准确率提升 **13%**，同时延续 PaddleOCR 著名的“极致效率”特性。

<div align="center">
  <p>
      <img width="100%" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/Arch.jpg" alt="PaddleOCR Architecture">
  </p>
</div>

### 🛠️ 以开发者为中心的生态系统
* **无缝集成**：AI Agent 生态的首选——深度集成 **Dify、RAGFlow、Pathway 和 Cherry Studio**。
* **大模型数据飞轮**：提供完整的高质量数据集构建流水线，为大型语言模型微调提供可持续的“数据引擎”。
* **一键部署**：支持多种硬件后端（NVIDIA GPU、Intel CPU、昆仑芯 XPU 及各类 AI 加速卡）。


## 📣 近期更新

### 🔥 2026.05.28：PaddleOCR 3.6.0 发布
- PaddleOCR-VL-1.6 亮点：

    - **全新 SOTA 精度**：在 OmniDocBench v1.6 上突破 96.3%，同时在 v1.5 和 Real5-OmniDocBench 上刷新纪录，文本、公式及表格识别能力全面领先开源与闭源方案。
    - **综合能力升级**：在表格、古籍及生僻字识别方面显著提升，印章检测与图表理解在多场景下表现优异。
    - **无缝迁移**：模型架构与 PaddleOCR-VL-1.5 完全一致，实现零成本适配——即插即用。
    - **立即体验**：可在 [HuggingFace](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6) 或[官方网站](https://www.paddleocr.com) 获取。

<details>
<summary><strong>2026.04.21：PaddleOCR 3.5.0 发布</strong></summary>

* **灵活的推理后端**：无缝切换 Paddle 静态图、动态图或 Transformers。PaddleOCR 现已深度融入 Hugging Face 生态，20 款主流模型均支持以 Transformers 作为推理后端。
* **办公文档转 Markdown**：将 Word、Excel、PowerPoint 等常见办公格式转换为 Markdown。
* **解析结果导出 DOCX**：`PaddleOCR-VL` 系列、`PP-StructureV3` 和 `PP-DocTranslation` 现已支持将解析结果导出为 DOCX，方便在 Microsoft Word 中查看与编辑。
* **官方浏览器推理 SDK**：发布 `PaddleOCR.js`，支持直接在浏览器中运行 `PP-OCRv5`。

</details>

<details>
<summary><strong>2026.01.29：PaddleOCR 3.4.0 发布</strong></summary>

* PaddleOCR-VL-1.5（SOTA 0.9B VLM）：我们的最新旗舰文档解析模型现已上线！
    * **OmniDocBench 准确率达 94.5%**：超越顶级通用大模型及专用文档解析器。
    * **真实世界鲁棒性**：首次引入 **PP-DocLayoutV3** 算法进行不规则形状定位，攻克倾斜、弯曲、扫描、光照、屏幕截图等 5 类高难度场景。
    * **能力扩展**：新增支持**印章识别**、**文字检测（Text Spotting）**，语种覆盖扩至 **111 种**（含藏文、孟加拉语）。
    * **长文档处理 mastery**：支持跨页表格自动合并与层级标题识别。
    * **立即体验**：可在 [HuggingFace](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5) 或[官方网站](https://www.paddleocr.com) 获取。

</details>

<details>
<summary><strong>2025.10.16：PaddleOCR 3.3.0 发布</strong></summary>

- 发布 PaddleOCR-VL：
    - **模型介绍**：
        - **PaddleOCR-VL** 是一款面向文档解析的 SOTA 且资源高效的模型。其核心组件为 PaddleOCR-VL-0.9B，这是一个紧凑而强大的视觉语言模型（VLM），融合了 NaViT 风格的动态分辨率视觉编码器与 ERNIE-4.5-0.3B 语言模型，以实现精准的要素识别。**该创新模型高效支持 109 种语言，在文本、表格、公式及图表等复杂元素识别上表现卓越，同时保持极低的资源消耗**。通过广泛公开基准测试与内部评估验证，PaddleOCR-VL 在页面级文档解析和要素级识别上均取得 SOTA 性能。其显著优于现有方案，具备媲美顶级 VLM 的竞争力，且推理速度极快，非常适合实际场景部署。模型已发布至 [HuggingFace](https://huggingface.co/PaddlePaddle/PaddleOCR-VL)，欢迎下载试用！更多介绍详见 [PaddleOCR-VL](https://www.paddleocr.ai/latest/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html)。

    - **核心特性**：
        - **紧凑强大的 VLM 架构**：我们提出了一种专为资源高效推理设计的新型视觉语言模型，在要素识别上表现优异。通过融合 NaViT 风格动态高分辨率视觉编码器与轻量级 ERNIE-4.5-0.3B 语言模型，显著提升模型的识别能力与解码效率。该集成在保证高精度的同时大幅降低计算需求，非常适合高效实用的文档处理应用。
        - **SOTA 文档解析性能**：PaddleOCR-VL 在页面级文档解析和要素级识别上均达到行业领先水平。显著优于传统流水线方案，并在文档解析任务中展现出与顶级视觉语言模型（VLM）相抗衡的竞争力。其在文本、表格、公式及图表等复杂元素识别上表现突出，适用于手写体、历史文献等多种挑战性内容类型，具备极强的通用性。
        - **多语言支持**：PaddleOCR-VL 支持 109 种语言，覆盖全球主要语种（含中、英、日、拉丁文、韩文等），以及俄语（西里尔字母）、阿拉伯语、印地语（天城体）、泰语等不同书写系统的语言。广泛的语种覆盖大幅提升了系统在多语言及全球化文档处理场景中的适用性。

- 发布 PP-OCRv5 多语言识别模型：
    - 提升拉丁文系的识别精度与覆盖率；新增西里尔字母、阿拉伯文、天城文、泰卢固文、泰米尔文等语种支持，全面覆盖 109 种语言。该模型参数量仅 2M，部分模型准确率较上一代提升超 40%。

</details>


<details>
<summary><strong>2025.08.21：PaddleOCR 3.2.0 发布</strong></summary>

- **重大模型更新：**
    - 引入英、泰、希腊语 PP-OCRv5 识别模型的训练、推理与部署。**PP-OCRv5 英文模型在英文场景下较主模型提升 11%，泰语和希腊语识别准确率达 82.68% 和 89.28%。**

- **部署能力升级：**
    - **全面支持 PaddlePaddle 框架版本 3.1.0 与 3.1.1。**
    - **PP-OCRv5 C++ 本地部署方案全面升级，现已同时支持 Linux 和 Windows，特性与精度同 Python 实现保持一致。**
    - **高性能推理新增 CUDA 12 支持，用户可选择 Paddle Inference 或 ONNX Runtime 作为推理后端。**
    - **高稳定服务化部署方案已完全开源，允许用户按需自定义 Docker 镜像与 SDK。**
    - 该方案同样支持通过手动构造 HTTP 请求进行调用，便于使用任意编程语言开发客户端代码。

- **基准测试支持：**
    - **全流水线现均支持细粒度压测，可测量端到端推理耗时及各层/模块延迟数据，辅助性能分析。[参见此处](docs/version3.x/pipeline_usage/instructions/benchmark.en.md)了解如何配置与使用基准测试功能。**
    - **文档已更新主流硬件常用配置的关键指标（如推理延迟、显存占用），为用户提供部署参考。**

- **缺陷修复：**
    - 修复模型训练期间日志保存失败的问题。
    - 升级公式模型的数据增强组件以适配新版 albumentations，并修复多进程场景下使用 tokenizers 包时的死锁警告。
    - 修复 PP-StructureV3 配置文件中的开关行为（如 `use_chart_parsing`）与其他流水线不一致的问题。

- **其他优化：**
    - **分离核心与可选依赖。基础文本识别仅需最小化核心依赖；文档解析与信息提取的额外依赖可按需安装。**
    - **Windows 平台新增 NVIDIA RTX 50 系列显卡支持，用户可参考[安装指南](docs/version3.x/installation.en.md)获取对应 PaddlePaddle 框架版本。**
    - **PP-OCR 系列模型现已支持返回单字坐标。**
    - 新增 AIStudio、ModelScope 等模型下载源，允许用户指定模型下载地址。
    - 新增 PP-Chart2Table 模块，支持图表转表格功能。
    - 优化文档描述以提升易用性。
</details>


[历史日志](https://paddlepaddle.github.io/PaddleOCR/latest/en/update/update.html)


## 🚀 快速开始

### 步骤 1：在线体验
PaddleOCR 官方网站提供交互式**体验中心**与 **API**——无需本地配置，一键即可体验。

👉 [访问官方网站](https://www.paddleocr.com)

### 步骤 2：本地部署
如需本地使用，请根据您的实际需求参考以下文档：

- **PP-OCR 系列**：参见 [PP-OCR 文档](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/OCR.html)
- **PaddleOCR-VL 系列**：参见 [PaddleOCR-VL 文档](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html)
- **PP-StructureV3**：参见 [PP-StructureV3 文档](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html)
- **更多能力**：参见 [更多功能文档](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/pipeline_overview.html)


## 🧩 更多功能

- 将模型转换为 ONNX 格式：[获取 ONNX 模型](https://paddlepaddle.github.io/PaddleOCR/latest/en/version3.x/inference_deployment/others/obtaining_onnx_models.html)。
- 使用 OpenVINO、ONNX Runtime、TensorRT 等引擎加速推理，或使用 ONNX 格式模型进行推理：[高性能推理](https://paddlepaddle.github.io/PaddleOCR/latest/en/version3.x/inference_deployment/local_inference/high_performance_inference.html)。
- 使用多 GPU 和多进程加速推理：[流水线并行推理](https://paddlepaddle.github.io/PaddleOCR/latest/en/version3.x/pipeline_usage/instructions/parallel_inference.html)。
- 将 PaddleOCR 集成至 C++、C#、Java 等语言编写的应用中：[Serving](https://paddlepaddle.github.io/PaddleOCR/latest/en/version3.x/inference_deployment/serving/serving.html)。

## 🔄 效果预览

### PP-OCRv5

<div align="center">
  <p>
       <img width="100%" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/PP-OCRv5_demo.gif" alt="PP-OCRv5 Demo">
  </p>
</div>



### PP-StructureV3

<div align="center">
  <p>
      <img width="100%" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/PP-StructureV3_demo.gif" alt="PP-StructureV3 Demo">
  </p>
</div>

### PaddleOCR-VL

<div align="center">
  <p>
      <img width="100%" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/PaddleOCR-VL_demo.gif" alt="PP-StructureV3 Demo">
  </p>
</div>


## ✨ 持续关注

⭐ **给本仓库点亮 Star，第一时间获取激动人心的更新与新功能发布，包括强大的 OCR 与文档解析能力！** ⭐

<div align="center">
  <p>
       <img width="1200" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/star_paddleocr2.en.gif" alt="Star-Project">
  </p>
</div>


## 👩‍👩‍👧‍👦 社区交流

<div align="center">

| PaddlePaddle 微信公众号 | 加入技术交流群 |
| :---: | :---: |
| <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/refs/heads/main/images/paddleocr/README/qrcode_for_paddlepaddle_official_account.jpg" width="150"> | <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/refs/heads/main/images/paddleocr/README/qr_code_for_the_questionnaire.jpg" width="150"> |
</div>


## 😃 基于 PaddleOCR 的优秀项目
PaddleOCR 的今天离不开其令人惊叹的社区！💗 衷心感谢所有长期合作伙伴、新晋协作者以及每一位为 PaddleOCR 倾注热情的开发者——无论我们是否在此一一列举。您的支持是我们前行的动力！

<div align="center">

| 项目名称 | 描述 |
| ------------ | ----------- |
| [Dify](https://github.com/langgenius/dify) <a href="https://github.com/langgenius/dify"><img src="https://img.shields.io/github/stars/langgenius/dify"></a>|面向 Agent 工作流开发的开箱即用平台。|
| [RAGFlow](https://github.com/infiniflow/ragflow) <a href="https://github.com/infiniflow/ragflow"><img src="https://img.shields.io/github/stars/infiniflow/ragflow"></a>|基于深度文档理解的 RAG 引擎。|
| [pathway](https://github.com/pathwaycom/pathway) <a href="https://github.com/pathwaycom/pathway"><img src="https://img.shields.io/github/stars/pathwaycom/pathway"></a>|用于流处理、实时分析、LLM 流水线与 RAG 的 Python ETL 框架。|
| [MinerU](https://github.com/opendatalab/MinerU) <a href="https://github.com/opendatalab/MinerU"><img src="https://img.shields.io/github/stars/opendatalab/MinerU"></a>|多类型文档转 Markdown 转换工具|
| [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) <a href="https://github.com/hiroi-sora/Umi-OCR"><img src="https://img.shields.io/github/stars/hiroi-sora/Umi-OCR"></a>|免费、开源的批量离线 OCR 软件。|
| [cherry-studio](https://github.com/CherryHQ/cherry-studio) <a href="https://github.com/CherryHQ/cherry-studio"><img src="https://img.shields.io/github/stars/CherryHQ/cherry-studio"></a>|支持多 LLM 提供商的桌面客户端。|
| [haystack](https://github.com/deepset-ai/haystack)<a href="https://github.com/deepset-ai/haystack"><img src="https://img.shields.io/github/stars/deepset-ai/haystack"></a> |用于构建可定制、生产就绪的 LLM 应用的 AI 编排框架。|
| [OmniParser](https://github.com/microsoft/OmniParser)<a href="https://github.com/microsoft/OmniParser"><img src="https://img.shields.io/github/stars/microsoft/OmniParser"></a> |基于纯视觉 GUI Agent 的屏幕解析工具。|
| [QAnything](https://github.com/netease-youdao/QAnything)<a href="https://github.com/netease-youdao/QAnything"><img src="https://img.shields.io/github/stars/netease-youdao/QAnything"></a> |基于任意内容的问答系统。|
| [了解更多项目](./awesome_projects.md) | [更多基于 PaddleOCR 的项目](./awesome_projects.md)|
</div>

## 👩‍👩‍👧‍👦 贡献者

<div align="center">
<a href="https://github.com/PaddlePaddle/PaddleOCR/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PaddlePaddle/PaddleOCR&max=400&columns=20"  width="800"/>
</a>
</div>

## 🌟 Star 趋势

<div align="center">
  <p>
      <img width="800" src="https://api.star-history.com/svg?repos=PaddlePaddle/PaddleOCR&type=Date" alt="Star-history">
  </p>
</div>


## 📄 许可证
本项目基于 [Apache 2.0 license](LICENSE) 开源。

## 🎓 引用格式

```bibtex
@misc{cui2025paddleocr30technicalreport,
      title={PaddleOCR 3.0 Technical Report}, 
      author={Cheng Cui and Ting Sun and Manhui Lin and Tingquan Gao and Yubo Zhang and Jiaxuan Liu and Xueqing Wang and Zelun Zhang and Changda Zhou and Hongen Liu and Yue Zhang and Wenyu Lv and Kui Huang and Yichao Zhang and Jing Zhang and Jun Zhang and Yi Liu and Dianhai Yu and Yanjun Ma},
      year={2025},
      eprint={2507.05595},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2507.05595}, 
}

@misc{cui2025paddleocrvlboostingmultilingualdocument,
      title={PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model}, 
      author={Cheng Cui and Ting Sun and Suyin Liang and Tingquan Gao and Zelun Zhang and Jiaxuan Liu and Xueqing Wang and Changda Zhou and Hongen Liu and Manhui Lin and Yue Zhang and Yubo Zhang and Handong Zheng and Jing Zhang and Jun Zhang and Yi Liu and Dianhai Yu and Yanjun Ma},
      year={2025},
      eprint={2510.14528},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2510.14528}, 
}

@misc{cui2026paddleocrvl15multitask09bvlm,
      title={PaddleOCR-VL-1.5: Towards a Multi-Task 0.9B VLM for Robust In-the-Wild Document Parsing}, 
      author={Cheng Cui and Ting Sun and Suyin Liang and Tingquan Gao and Zelun Zhang and Jiaxuan Liu and Xueqing Wang and Changda Zhou and Hongen Liu and Manhui Lin and Yue Zhang and Yubo Zhang and Yi Liu and Dianhai Yu and Yanjun Ma},
      year={2026},
      eprint={2601.21957},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2601.21957}, 
}

@misc{zhang2026paddleocrvl16expandingfrontierdocument,
      title={PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training}, 
      author={Zelun Zhang and Hongen Liu and Suyin Liang and Yubo Zhang and Yiqing Xiang and Jiaxuan Liu and Ting Sun and Manhui Lin and Yue Zhang and Changda Zhou and Tingquan Gao and Cheng Cui and Yi Liu and Dianhai Yu and Yanjun Ma},
      year={2026},
      eprint={2606.03264},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2606.03264}, 
}
```