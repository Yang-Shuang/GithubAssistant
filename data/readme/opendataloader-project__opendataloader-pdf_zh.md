# OpenDataLoader PDF

**面向 AI 就绪数据的 PDF 解析器。自动化 PDF 无障碍处理。开源。**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/opendataloader-project/opendataloader-pdf/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/opendataloader-pdf.svg)](https://pypi.org/project/opendataloader-pdf/)
[![npm version](https://img.shields.io/npm/v/@opendataloader/pdf.svg)](https://www.npmjs.com/package/@opendataloader/pdf)
[![Maven Central](https://img.shields.io/maven-central/v/org.opendataloader/opendataloader-pdf-core.svg)](https://search.maven.org/artifact/org.opendataloader/opendataloader-pdf-core)
[![Java](https://img.shields.io/badge/Java-11%2B-blue.svg)](https://github.com/opendataloader-project/opendataloader-pdf#java)

<a href="https://trendshift.io/repositories/21917" target="_blank"><img src="https://trendshift.io/api/badge/repositories/21917" alt="opendataloader-project%2Fopendataloader-pdf | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

🔍 **面向 AI 数据提取的 PDF 解析器** — 从任意 PDF 中提取 Markdown、JSON（含边界框）和 HTML。基准测试排名第一（综合得分 0.907）。确定性本地模式 + AI 混合模式适用于复杂页面。

- **准确率如何？** — 基准测试第一：在包含多栏排版和学术论文的 200 份真实 PDF 中，综合得分 0.907，表格准确率 0.928。提供确定性本地模式与 AI 混合模式以处理复杂页面（[基准测试](#extraction-benchmarks)）
- **支持扫描件与 OCR 吗？** — 支持。混合模式下内置 OCR（支持 80+ 种语言）。即使扫描质量较差，只要达到 300 DPI 以上即可有效识别（[混合模式](#hybrid-mode-1-accuracy-for-complex-pdfs)）
- **表格、公式、图片、图表？** — 支持。复杂/无边框表格、LaTeX 公式以及 AI 生成的图片/图表描述均可通过混合模式处理（[混合模式](#hybrid-mode-1-accuracy-for-complex-pdfs)）
- **如何在 RAG 中使用？** — `pip install opendataloader-pdf`，3 行代码完成转换。输出结构化 Markdown 用于分块（chunking），带边界框的 JSON 用于来源引用，以及 HTML。支持 LangChain 集成。提供 Python、Node.js、Java SDK（[快速入门](#get-started-in-30-seconds) | [LangChain](#langchain-integration)）

♿ **PDF 无障碍自动化** — 批量将未标记的 PDF 自动转换为屏幕阅读器可用的标记型 PDF。首个端到端生成标记型 PDF 的开源工具。

- **存在什么问题？** — 全球范围内的无障碍法规正在严格执行中。手动修复 PDF 成本为每份文档 $50–200，且难以规模化扩展（[相关法规](#pdf-accessibility--pdfua-conversion)）
- **哪些功能是免费的？** — 布局分析 + 自动标记（Apache 2.0）。未标记的 PDF 输入 → 标记型 PDF 输出。无需依赖任何专有 SDK（[自动标记](#auto-tagging)）
- **关于 PDF/UA 合规性？** — 将标记型 PDF 转换为 PDF/UA-1 或 PDF/UA-2 属于企业版附加功能。自动标记生成基础的标记型 PDF；PDF/UA 导出是最终步骤（[工作流](#accessibility-pipeline)）
- **为何值得信赖？** — 与 [Dual Lab](https://duallab.com)（[veraPDF](https://verapdf.org) 开发者）合作开发，基于 [PDF Association](https://pdfa.org) 的规范、最佳实践指南及 [PDF Community](https://pdfa.org/community/) 的专业知识。自动标记遵循 [Well-Tagged PDF 规范](https://pdfa.org/wtpdf/)，并通过 veraPDF 进行验证（[合作详情](https://opendataloader.org/docs/tagged-pdf-collaboration)）

## 30 秒快速入门

**环境要求：**Java 11+ 和 Python 3.10+（[Node.js](https://opendataloader.org/docs/quick-start-nodejs) | [Java](https://opendataloader.org/docs/quick-start-java) 也可用）

> **开始之前：**运行 `java -version`。如果未找到，请从 [Adoptium](https://adoptium.net/) 安装 JDK 11+。

```bash
pip install -U opendataloader-pdf
```

```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

![OpenDataLoader PDF layout analysis — headings, tables, images detected with bounding boxes](https://raw.githubusercontent.com/opendataloader-project/opendataloader-pdf/main/samples/image/example_annotated_pdf.png)

*带标注的 PDF 输出 — 每个元素（标题、段落、表格、图片）均检测出边界框及语义类型。*

## 解决的核心问题

| 痛点 | 解决方案 | 状态 |
|---------|----------|--------|
| **解析时 PDF 结构丢失** — 阅读顺序错误、表格断裂、无元素坐标 | 确定性本地转 Markdown/JSON（含边界框），采用 XY-Cut++ 阅读顺序分析 | 已支持 |
| **复杂表格、扫描件、公式、图表** 需要 AI 级理解能力 | 混合模式将复杂页面路由至 AI 后端（基准测试第一） | 已支持 |
| **人工修复成本高** — 无障碍法规（EAA、ADA、Section 508）要求标记型 PDF。手动修复成本为每份文档 $50–200，且难以扩展 | 自动将未标记 PDF 转换为标记型 PDF（免费，Apache 2.0）。作为 PDF/UA 工作流的基础；完整的 PDF/UA-1/2 导出为企业版功能 | 自动标记：已支持。PDF/UA 导出：企业版 |

## 能力矩阵

| 能力 | 是否支持 | 版本 |
|------------|-----------|------|
| **数据提取** | | |
| 按正确阅读顺序提取文本 | 是 | 免费 |
| 每个元素均提供边界框 | 是 | 免费 |
| 表格提取（简单边框） | 是 | 免费 |
| 表格提取（复杂/无边框） | 是 | 免费（混合模式） |
| 标题层级检测 | 是 | 免费 |
| 列表检测（编号、项目符号、嵌套） | 是 | 免费 |
| 带坐标的图片提取 | 是 | 免费 |
| AI 图表/图片描述生成 | 是 | 免费（混合模式） |
| 扫描件 OCR | 是 | 免费（混合模式） |
| 公式提取（LaTeX） | 是 | 免费（混合模式） |
| 标记型 PDF 结构提取 | 是 | 免费 |
| AI 安全（提示词注入过滤） | 是 | 免费 |
| 页眉/页脚/水印过滤 | 是 | 免费 |
| **无障碍处理** | | |
| 自动标记 → 为未标记 PDF 生成标记型 PDF | 是 | 免费（Apache 2.0） |
| PDF/UA-1、PDF/UA-2 导出 | 💼 可用 | 企业版 |
| 无障碍工作台（可视化编辑器） | 💼 可用 | 企业版 |
| **限制** | | |
| 处理 Word/Excel/PPT | 否 | — |
| 需要 GPU | 否 | — |

## 提取基准测试

**opendataloader-pdf [混合模式]** 在阅读顺序、表格和标题提取准确率上综合排名第一（0.907）。

| Engine | Overall | Reading Order | Table | Heading | Speed (s/page) | License |
|--------|---------|---------------|-------|---------|----------------|---------|
| **opendataloader [hybrid]** | **0.907** | **0.934** | **0.928** | 0.821 | 0.463 | Apache-2.0 |
| nutrient | 0.885 | 0.925 | 0.708 | 0.819 | **0.008** | Commercial |
| docling | 0.882 | 0.898 | 0.887 | **0.824** | 0.762 | MIT |
| marker | 0.861 | 0.890 | 0.808 | 0.796 | 53.932 | GPL-3.0 |
| unstructured [hi_res] | 0.841 | 0.904 | 0.588 | 0.749 | 3.008 | Apache-2.0 |
| edgeparse | 0.837 | 0.894 | 0.717 | 0.706 | 0.036 | Apache-2.0 |
| opendataloader | 0.831 | 0.902 | 0.489 | 0.739 | 0.015 | Apache-2.0 |
| mineru | 0.831 | 0.857 | 0.873 | 0.743 | 5.962 | AGPL-3.0 |
| pymupdf4llm | 0.732 | 0.885 | 0.401 | 0.412 | 0.091 | AGPL-3.0 |
| unstructured | 0.686 | 0.882 | 0.000 | 0.388 | 0.077 | Apache-2.0 |
| markitdown | 0.589 | 0.844 | 0.273 | 0.000 | 0.114 | MIT |
| liteparse | 0.576 | 0.866 | 0.000 | 0.000 | 1.061 | Apache-2.0 |

> 分数已归一化至 [0, 1]。准确率越高越好，耗时越低（速度越快）越好。**加粗** = 最佳表现。[完整基准测试详情](https://github.com/opendataloader-project/opendataloader-bench)

[![Benchmark](https://github.com/opendataloader-project/opendataloader-bench/raw/refs/heads/main/charts/benchmark.png)](https://github.com/opendataloader-project/opendataloader-bench)

[![Quality Breakdown](https://github.com/opendataloader-project/opendataloader-bench/raw/refs/heads/main/charts/benchmark_quality.png)](https://github.com/opendataloader-project/opendataloader-bench)

## 如何选择使用模式？

| 你的文档类型 | 模式 | 安装命令 | 服务端命令 | 客户端命令 |
|---------------|------|---------|----------------|----------------|
| 标准数字 PDF | Fast（默认） | `pip install opendataloader-pdf` | 无需配置 | `opendataloader-pdf file1.pdf file2.pdf folder/` |
| 复杂或嵌套表格 | **Hybrid** | `pip install "opendataloader-pdf[hybrid]"` | `opendataloader-pdf-hybrid --port 5002` | `opendataloader-pdf --hybrid docling-fast file1.pdf file2.pdf folder/` |
| 扫描件/基于图像的 PDF | Hybrid + OCR | `pip install "opendataloader-pdf[hybrid]"` | `opendataloader-pdf-hybrid --port 5002 --force-ocr` | `opendataloader-pdf --hybrid docling-fast file1.pdf file2.pdf folder/` |
| 非英文扫描版 PDF | Hybrid + OCR | `pip install "opendataloader-pdf[hybrid]"` | `opendataloader-pdf-hybrid --port 5002 --force-ocr --ocr-lang "ko,en"` | `opendataloader-pdf --hybrid docling-fast file1.pdf file2.pdf folder/` |
| 数学公式 | Hybrid + formula | `pip install "opendataloader-pdf[hybrid]"` | `opendataloader-pdf-hybrid --enrich-formula` | `opendataloader-pdf --hybrid docling-fast --hybrid-mode full file1.pdf file2.pdf folder/` |
| 需要描述的图表 | Hybrid + picture | `pip install "opendataloader-pdf[hybrid]"` | `opendataloader-pdf-hybrid --enrich-picture-description` | `opendataloader-pdf --hybrid docling-fast --hybrid-mode full file1.pdf file2.pdf folder/` |
| 需无障碍处理的未标记 PDF | Auto-tagging → Tagged PDF | `pip install opendataloader-pdf` | 无需配置 | `opendataloader-pdf --format tagged-pdf file1.pdf file2.pdf folder/` |

## 快速入门

### Python

```bash
pip install -U opendataloader-pdf
```

```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

### Node.js

```bash
npm install @opendataloader/pdf
```

```typescript
import { convert } from '@opendataloader/pdf';

await convert(['file1.pdf', 'file2.pdf', 'folder/'], {
  outputDir: 'output/',
  format: 'markdown,json'
});
```

### Java

```xml
<dependency>
  <groupId>org.opendataloader</groupId>
  <artifactId>opendataloader-pdf-core</artifactId>
</dependency>
```

[Python 快速入门](https://opendataloader.org/docs/quick-start-python) | [Node.js 快速入门](https://opendataloader.org/docs/quick-start-nodejs) | [Java 快速入门](https://opendataloader.org/docs/quick-start-java)

## 混合模式：复杂 PDF 准确率第一

混合模式将快速的本地 Java 处理与 AI 后端相结合。简单页面在本地处理（0.02秒）；复杂页面则路由至 AI 以获取表格准确率提升 90% 以上的效果。

```bash
pip install -U "opendataloader-pdf[hybrid]"
```

**终端 1** — 启动后端服务：

```bash
opendataloader-pdf-hybrid --port 5002
```

**终端 2** — 处理 PDF：

```bash
# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf --hybrid docling-fast file1.pdf file2.pdf folder/
```

**Python：**

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    hybrid="docling-fast"
)
```

### 扫描件 OCR

使用 `--force-ocr` 启动后端以处理无可选文本的基于图像的 PDF：

```bash
opendataloader-pdf-hybrid --port 5002 --force-ocr
```

对于非英文文档，请指定语言：

```bash
opendataloader-pdf-hybrid --port 5002 --force-ocr --ocr-lang "ko,en"
```

支持的语言包括：`en`, `ko`, `ja`, `ch_sim`, `ch_tra`, `de`, `fr`, `ar` 等。

### 公式提取（LaTeX）

从科学类 PDF 中提取数学公式为 LaTeX 格式：

```bash
# Server: enable formula enrichment
opendataloader-pdf-hybrid --enrich-formula

# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf --hybrid docling-fast --hybrid-mode full file1.pdf file2.pdf folder/
```

JSON 输出示例：
```json
{
  "type": "formula",
  "page number": 1,
  "bounding box": [226.2, 144.7, 377.1, 168.7],
  "content": "\\frac{f(x+h) - f(x)}{h}"
}
```

> **注意：**公式和图片描述增强功能需要在客户端使用 `--hybrid-mode full`。

### 图表与图片描述

为图表和图片生成 AI 描述 — 适用于 RAG 搜索和无障碍替代文本（alt text）：

```bash
# Server
opendataloader-pdf-hybrid --enrich-picture-description

# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf --hybrid docling-fast --hybrid-mode full file1.pdf file2.pdf folder/
```

JSON 输出示例：
```json
{
  "type": "picture",
  "page number": 1,
  "bounding box": [72.0, 400.0, 540.0, 650.0],
  "description": "A bar chart showing waste generation by region from 2016 to 2030..."
}
```

> 基于 SmolVLM（2.56亿参数）轻量级视觉模型。支持通过 `--picture-description-prompt` 自定义提示词。

### Hancom Data Loader 集成 —— 即将推出

通过 [Hancom Data Loader](https://sdk.hancom.com/en/services/1?utm_source=github&utm_medium=readme&utm_campaign=opendataloader-pdf) 提供企业级 AI 文档分析 — 基于你所在领域特定文档训练的客户定制模型。支持 30+ 种元素类型（表格、图表、公式、标题、脚注等），基于 VLM 的图片/图表理解，复杂表格提取（合并单元格、嵌套表格），针对扫描文档的 SLA 保障 OCR，以及原生 HWP/HWPX 支持。兼容 PDF、DOCX、XLSX、PPTX、HWP、PNG、JPG。[在线演示](https://livedemo.sdk.hancom.com/en/dataloader?utm_source=github&utm_medium=readme&utm_campaign=opendataloader-pdf)

[混合模式指南](https://opendataloader.org/docs/hybrid-mode)

## 输出格式

| 格式 | 适用场景 |
|--------|----------|
| **JSON** | 带边界框和语义类型的结构化数据 |
| **Markdown** | 干净的文本，适用于 LLM 上下文或 RAG 分块 |
| **HTML** | 支持样式设置的网页展示 |
| **Annotated PDF（标注版）** | 可视化调试 — 查看检测到的结构（[示例](https://opendataloader.org/demo/samples/01030000000000)） |
| **Text（纯文本）** | 基础文本提取 |

可组合使用：`format="json,markdown"`

### JSON 输出示例

```json
{
  "type": "heading",
  "id": 42,
  "level": "Title",
  "page number": 1,
  "bounding box": [72.0, 700.0, 540.0, 730.0],
  "heading level": 1,
  "font": "Helvetica-Bold",
  "font size": 24.0,
  "text color": "[0.0]",
  "content": "Introduction"
}
```

| 字段 | 说明 |
|-------|-------------|
| `type` | 元素类型：heading（标题）、paragraph（段落）、table（表格）、list（列表）、image（图片）、caption（说明）、formula（公式） |
| `id` | 用于交叉引用的唯一标识符 |
| `page number` | 页码索引（从 1 开始） |
| `bounding box` | `[left, bottom, right, top]`，单位为 PDF 点（72pt = 1 inch） |
| `heading level` | 标题层级（1+） |
| `content` | 提取的文本内容 |

[完整 JSON Schema](https://opendataloader.org/docs/reference/json-schema)

## 高级功能

### 标记型 PDF（Tagged PDF）支持

当 PDF 包含结构标签时，OpenDataLoader 会提取作者预期的**精确布局** — 无需猜测，无需启发式算法。标题、列表、表格和阅读顺序均保留自源文件。

> **输出质量取决于标签质量。**并非所有标记型 PDF 都是高质量标注的。对于标签稀疏或不准确的 PDF，默认启发式模式或 `--hybrid docling-fast` 通常能产生更好的结果。

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    use_struct_tree=True           # Use native PDF structure tags
)
```

大多数 PDF 解析器完全忽略结构标签。[了解更多](https://opendataloader.org/docs/tagged-pdf)

### AI 安全：提示词注入防护

PDF 可能包含隐藏的提示词注入攻击。OpenDataLoader 会自动过滤以下内容：

- 隐藏文本（透明或零尺寸字体）
- 页面外内容
- 可疑的不可见图层

如需清理敏感数据（邮箱、URL、电话号码 → 占位符），请显式启用：

```bash
# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf file1.pdf file2.pdf folder/ --sanitize
```

[AI 安全指南](https://opendataloader.org/docs/ai-safety)

### LangChain 集成

```bash
pip install -U langchain-opendataloader-pdf
```

```python
from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader

loader = OpenDataLoaderPDFLoader(
    file_path=["file1.pdf", "file2.pdf", "folder/"],
    format="text"
)
documents = loader.load()
```

[LangChain 文档](https://docs.langchain.com/oss/python/integrations/document_loaders/opendataloader_pdf) | [GitHub](https://github.com/opendataloader-project/langchain-opendataloader-pdf) | [PyPI](https://pypi.org/project/langchain-opendataloader-pdf/)

### 高级选项

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="json,markdown,pdf",
    image_output="embedded",        # "off", "embedded" (Base64), or "external" (default)
    image_format="jpeg",            # "png" or "jpeg"
    use_struct_tree=True,           # Use native PDF structure
)
```

[完整 CLI 选项参考](https://opendataloader.org/docs/reference/cli-options)

## PDF 无障碍与 PDF/UA 转换

**痛点：**数百万现有 PDF 缺乏结构标签，不符合无障碍法规（EAA、ADA/Section 508、韩国数字包容法）。手动修复成本为每份文档 $50–200，且难以扩展。

**OpenDataLoader 的方案：**与 [PDF Association](https://pdfa.org) 和 [Dual Lab](https://duallab.com)（[veraPDF](https://verapdf.org) 开发者，行业标准开源 PDF/A 和 PDF/UA 验证器）合作开发。自动标记遵循 [Well-Tagged PDF 规范](https://pdfa.org/resource/well-tagged-pdf/)，并使用 veraPDF 进行程序化验证 — 针对无障碍标准的自动化合规检查，而非人工审核。目前尚无其他开源工具能端到端生成标记型 PDF — 多数依赖专有 SDK 完成打标签步骤。OpenDataLoader 在 Apache 2.0 许可下实现全流程。（[合作详情](https://opendataloader.org/docs/tagged-pdf-collaboration)）

| 法规 | 截止日期 | 要求 |
|------------|----------|--------|
| **欧洲无障碍法案（EAA）** | 2025年6月28日 | 欧盟范围内所有数字产品需符合无障碍标准 |
| **ADA & Section 508** | 已生效 | 美国联邦机构及公共场所服务 |
| **数字包容法** | 已生效 | 韩国数字服务无障碍合规 |

### 标准与验证

| 方面 | 详情 |
|--------|------|
| **规范** | [Well-Tagged PDF](https://pdfa.org/resource/well-tagged-pdf/)（PDF Association 发布） |
| **验证工具** | [veraPDF](https://verapdf.org) — 行业标准开源 PDF/A & PDF/UA 验证器 |
| **合作开发** | PDF Association + [Dual Lab](https://duallab.com)（veraPDF 开发者）共同开发标记与验证流程 |
| **许可证** | 自动标记 → 生成 Tagged PDF：Apache 2.0（免费）。PDF/UA 导出：企业版 |

### 无障碍工作流

| 步骤 | 功能 | 状态 | 版本 |
|------|---------|--------|------|
| 1. **审计** | 读取现有 PDF 标签，检测未标记的 PDF | 已支持 | 免费 |
| 2. **自动标记 → 生成 Tagged PDF** | 为未标记 PDF 自动生成结构标签 | 已支持 | 免费（Apache 2.0） |
| 3. **导出 PDF/UA** | 转换为符合 PDF/UA-1 或 PDF/UA-2 标准的文件 | 💼 可用 | 企业版 |
| 4. **可视化编辑** | 无障碍工作台 — 审查并修复标签 | 💼 可用 | 企业版 |

> **💼 企业版功能**可按需申请。[联系我们](https://opendataloader.org/contact) 获取试用。

### 自动标记（Auto-Tagging）

将未标记的 PDF 转换为带结构标签（标题、段落、列表、表格、阅读顺序）且支持屏幕阅读器读取的标记型 PDF。

```python
import opendataloader_pdf

# Untagged PDF in → Tagged PDF out
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="tagged-pdf"
)
```

```bash
# CLI
opendataloader-pdf --format tagged-pdf file1.pdf file2.pdf folder/
```

可与其他格式组合使用：`format="json,tagged-pdf"`。

### 端到端合规工作流

```
现有 PDFs（未标记）
    │
    ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌──────────────────┐
│  1. 审计       │───>│  2. 自动标记     │───>│  3. 导出      │───>│  4. 工作台       │
│  (检查标签)   │    │  (→ Tagged PDF)  │    │  (PDF/UA)       │    │  (可视化编辑器) │
└─────────────────┘    └──────────────────┘    └─────────────────┘    └──────────────────┘
        │                       │                       │                      │
        ▼                       ▼                       ▼                      ▼
  use_struct_tree      format="tagged-pdf"        PDF/UA export       Accessibility Studio
  (Available now)      (Available, Apache 2.0)    (Enterprise)        (Enterprise)
```

[PDF 无障碍指南](https://opendataloader.org/docs/accessibility-compliance)

## 路线图

| 功能 | 时间线 | 版本 |
|---------|----------|------|
| **[Hancom Data Loader](https://sdk.hancom.com/en/services/1?utm_source=github&utm_medium=readme&utm_campaign=opendataloader-pdf)** — 企业级 AI 文档分析、客户定制模型、基于 VLM 的图表/图片理解、生产级 OCR | 2026年 Q2-Q3 | 计划中 |
| **结构验证** — 验证 PDF 标签树完整性 | 2026年 Q3 | 计划中 |

[完整路线图](https://opendataloader.org/docs/upcoming-roadmap)

## 常见问题解答 (FAQ)

### 用于 RAG 的最佳 PDF 解析器是什么？
对于 RAG 管道，你需要一个能保留文档结构、维持正确阅读顺序并提供元素坐标以支持引用的解析器。OpenDataLoader 专为该场景设计 — 输出带边界框的结构化 JSON，使用 XY-Cut++ 处理多栏排版，且可在本地运行无需 GPU。在混合模式下，它在基准测试中综合排名第一（0.907）。

### 什么是最好的开源 PDF 解析器？
OpenDataLoader PDF 是唯一结合以下特性的开源解析器：基于规则的确定性提取（无需 GPU）、每个元素均提供边界框、XY-Cut++ 阅读顺序分析、内置 AI 安全过滤器、原生 Tagged PDF 支持，以及用于复杂文档的混合 AI 模式。它在本地 CPU 上运行即可取得综合准确率第一（0.907）。

### 如何从 PDF 中提取表格以供 LLM 使用？
OpenDataLoader 通过边框分析和文本聚类检测表格，并保留行/列结构。对于复杂表格，启用混合模式可将准确率提升 90% 以上（TEDS 分数从 0.489 提升至 0.928）：

```python
# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="json",
    hybrid="docling-fast"           # For complex tables
)
```

### 它与 docling、marker 或 pymupdf4llm 相比如何？
OpenDataLoader [混合模式] 在阅读顺序、表格和标题准确率上综合排名第一（0.907）。主要差异：docling (0.882) 表现强劲但缺乏边界框和 AI 安全过滤器。marker (0.861) 需要 GPU 且速度慢 1000 倍（53.932秒/页）。pymupdf4llm (0.732) 速度快，但表格 (0.401) 和标题 (0.412) 准确率较差。OpenDataLoader 是唯一结合确定性本地提取、每个元素边界框及内置提示词注入防护的解析器。详见 [完整基准测试](https://github.com/opendataloader-project/opendataloader-bench)。

### 我可以在不将数据发送到云端的情况下使用它吗？
可以。OpenDataLoader 100% 在本地运行。无 API 调用，无数据传输 — 你的文档永远不会离开你的环境。混合模式后端也在你本地机器上运行。非常适合法律、医疗和金融类文档。

### 它支持扫描 PDF 的 OCR 吗？
支持，通过混合模式实现。使用 `pip install "opendataloader-pdf[hybrid]"` 安装，启动后端时添加 `--force-ocr`，然后照常处理。支持多种语言（包括韩语、日语、中文、阿拉伯语等），可通过 `--ocr-lang` 指定。

### 它是否兼容韩语、日语或中文文档？
是的。对于数字 PDF，文本提取开箱即用。对于扫描版 PDF，请使用混合模式并添加 `--force-ocr --ocr-lang "ko,en"`（或 `ja`, `ch_sim`, `ch_tra`）。即将推出：[Hancom Data Loader](https://sdk.hancom.com/en/services/1?utm_source=github&utm_medium=readme&utm_campaign=opendataloader-pdf) 集成 — 企业级 AI 文档分析，内置生产级 OCR 和客户定制模型，针对你特定的文档类型和工作流进行优化。

### 它的速度有多快？
本地模式在 CPU 上每秒可处理 60+ 页（0.02秒/页）。混合模式每秒处理 2+ 页（0.46秒/页），且对复杂文档的准确率显著提升。无需 GPU。基准测试环境为 Apple M4。[完整基准测试详情](https://github.com/opendataloader-project/opendataloader-bench)。通过多进程批处理，在 8 核及以上机器上吞吐量可超过每秒 100 页。

### 它是否支持多栏排版？
是的。OpenDataLoader 使用 XY-Cut++ 阅读顺序分析来正确排序跨多栏页面、侧边栏和混合排版的文本。该功能在本地模式和混合模式下均无需任何配置即可生效。

### 什么是混合模式（Hybrid Mode）？
混合模式将快速的本地 Java 处理与 AI 后端相结合。简单页面在本地处理（0.02秒/页）；复杂页面（表格、扫描内容、公式、图表）会自动路由至 AI 后端以获得更高准确率。该后端在你本地机器上运行 — 无需云端支持。详见 [如何选择使用模式？](#which-mode-should-i-use) 和 [混合模式指南](https://opendataloader.org/docs/hybrid-mode)。

### 它是否兼容 LangChain？
是的。安装 `langchain-opendataloader-pdf` 即可获取官方 LangChain 文档加载器集成。详见 [LangChain 文档](https://docs.langchain.com/oss/python/integrations/document_loaders/opendataloader_pdf)。

### 我该如何为 RAG 对 PDF 进行分块（Chunking）？
OpenDataLoader 输出结构化的 Markdown，并保留标题、表格和列表 — 这是语义分块的理想输入。JSON 输出中的每个元素均包含 `type`、`heading level` 和 `page number`，因此你可以按章节或页边界进行分割。对于大多数 RAG 管道：使用 `format="markdown"` 解析文本块，或在需要元素级控制时使用 `format="json"`。建议搭配 LangChain 的 `RecursiveCharacterTextSplitter` 或自定义基于标题的分块器以获得最佳效果。

### 我该如何在 RAG 答案中引用 PDF 来源？
JSON 输出中的每个元素均包含 `bounding box`（PDF 点单位下的 `[left, bottom, right, top]`）和 `page number`。当你的 RAG 管道返回答案时，可将源文本块映射回其边界框，以高亮显示原始 PDF 中的确切位置。这实现了“点击跳转来源”的交互体验 — 用户可直观看到答案出自哪个段落、表格或图表。目前没有其他开源解析器默认提供每个元素的边界框。

### 如何将 PDF 转换为 Markdown 以供 LLM 使用？
```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown"
)
```
OpenDataLoader 在 Markdown 输出中保留标题层级、表格结构和阅读顺序。对于包含无边框表格或扫描页面的复杂文档，请使用混合模式（`hybrid="docling-fast"`）以获得更高准确率。输出内容足够干净，可直接输入 LLM 上下文窗口或 RAG 分块管道。

### 有自动化的 PDF 无障碍修复工具吗？
有的。OpenDataLoader 是首个开源的端到端自动化 PDF 无障碍处理工具。与 [PDF Association](https://pdfa.org) 和 [Dual Lab](https://duallab.com)（veraPDF 开发者）合作开发，自动标记遵循 Well-Tagged PDF 规范并通过 veraPDF 进行程序化验证。布局分析引擎可检测文档结构（标题、表格、列表、阅读顺序）并自动生成无障碍标签。在 Apache 2.0 许可下，自动标记将未标记的 PDF 转换为标记型 PDF — 无需专有 SDK 依赖。使用 `format="tagged-pdf"`（Python/Node.js）或 `--format tagged-pdf`（CLI）。对于需要完整 PDF/UA 合规的组织，企业版附加功能提供 PDF/UA 导出和可视化标签编辑器。这取代了通常每份文档成本 $50–200+ 的手动修复工作流。

### 这真的是第一个开源的 PDF 自动标记工具吗？
是的。现有工具要么依赖专有 SDK 写入结构标签，要么仅输出非 PDF 格式（例如 Docling 输出 Markdown/JSON 但无法生成 Tagged PDF），或需要人工干预。OpenDataLoader 是首个在 Apache 2.0 开源许可下实现布局分析 → 标签生成 → Tagged PDF 输出的工具，且无任何专有依赖。自动标记遵循 PDF Association 的 Well-Tagged PDF 规范，并使用行业标准开源验证器 veraPDF 进行验证。

### 如何将现有 PDF 转换为 PDF/UA？
OpenDataLoader 提供端到端工作流：审计现有 PDF 标签（`use_struct_tree=True`），将未标记的 PDF 自动转换为 Tagged PDF（`format="tagged-pdf"`，Apache 2.0 免费），并导出为 PDF/UA-1 或 PDF/UA-2（企业版附加功能）。自动标记遵循 PDF Association 的 Well-Tagged PDF 规范并通过 veraPDF 验证。自动标记生成基础的 Tagged PDF；PDF/UA 导出是最终步骤。[联系我们](https://opendataloader.org/contact) 获取企业集成支持。

### 如何使我的 PDF 符合 EAA（欧洲无障碍法案）要求？
欧洲无障碍法案要求到 2025 年 6 月 28 日，所有数字产品需具备无障碍特性。OpenDataLoader 支持完整的修复工作流：审计 → 自动标记 → Tagged PDF → PDF/UA 导出。自动标记遵循 PDF Association 的 Well-Tagged PDF 规范并通过 veraPDF 验证，确保输出符合标准。自动标记生成 Tagged PDF 为 Apache 2.0 开源免费。PDF/UA 导出和无障碍工作台为企业版附加功能。详见我们的 [无障碍指南](https://opendataloader.org/docs/accessibility-compliance)。

### OpenDataLoader PDF 是免费的吗？
核心库以 **Apache 2.0** 许可开源 — 商业使用完全免费。这包含所有提取功能（文本、表格、图片、OCR、公式、图表通过混合模式）、AI 安全过滤器、Tagged PDF 支持以及自动标记生成 Tagged PDF。我们致力于保持核心无障碍工作流（布局分析 → 自动标记 → Tagged PDF）免费且开源。企业版附加功能（PDF/UA 导出、无障碍工作台）面向需要端到端合规的组织提供。

### 为什么许可证从 MPL 2.0 改为 Apache 2.0？
MPL 2.0 要求文件级 Copyleft，这通常会在企业采用前触发法务审查。Apache 2.0 是完全宽松的许可协议 — 无 Copleft 义务，更易于集成到商业项目中。如果你使用的是 2.0 之前的版本，它仍受 MPL 2.0 保护，你可继续使用。升级到 2.0+ 意味着你的项目遵循 Apache 2.0 条款，该条款更为宽松 — 无需额外操作或承担附加义务。

## 文档

- [快速入门 (Python)](https://opendataloader.org/docs/quick-start-python)
- [快速入门 (Node.js)](https://opendataloader.org/docs/quick-start-nodejs)
- [快速入门 (Java)](https://opendataloader.org/docs/quick-start-java)
- [JSON Schema 参考](https://opendataloader.org/docs/reference/json-schema)
- [CLI 选项](https://opendataloader.org/docs/reference/cli-options)
- [混合模式指南](https://opendataloader.org/docs/hybrid-mode)
- [标记型 PDF 支持](https://opendataloader.org/docs/tagged-pdf)
- [AI 安全功能](https://opendataloader.org/docs/ai-safety)
- [PDF 无障碍处理](https://opendataloader.org/docs/accessibility-compliance)

## 贡献指南

欢迎贡献代码！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[Apache License 2.0](LICENSE)

> **注意：** 2.0 之前的版本采用 [Mozilla Public License 2.0](https://www.mozilla.org/MPL/2.0/) 许可。

---

**觉得有用？** 请给我们点个 Star，帮助更多人发现 OpenDataLoader。