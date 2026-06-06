# 科学智能体技能（Scientific Agent Skills）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Version](https://img.shields.io/badge/Version-2.43.0-blue.svg)](pyproject.toml)
[![Skills](https://img.shields.io/badge/Skills-142-brightgreen.svg)](#-whats-included)
[![Databases](https://img.shields.io/badge/Databases-100%2B-orange.svg)](#-whats-included)
[![Agent Skills](https://img.shields.io/badge/Standard-Agent_Skills-blueviolet.svg)](https://agentskills.io/)
[![Security Scan](https://github.com/K-Dense-AI/scientific-agent-skills/actions/workflows/security-scan.yml/badge.svg)](https://github.com/K-Dense-AI/scientific-agent-skills/actions/workflows/security-scan.yml)
[![Works with](https://img.shields.io/badge/Works_with-Cursor_|_Claude_Code_|_Codex_|_Google_Antigravity-blue.svg)](#-getting-started)
[![X](https://img.shields.io/badge/Follow_on_X-%40k__dense__ai-000000?logo=x)](https://x.com/k_dense_ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-K--Dense_Inc.-0A66C2?logo=linkedin)](https://www.linkedin.com/company/k-dense-inc)
[![YouTube](https://img.shields.io/badge/YouTube-K--Dense_Inc.-FF0000?logo=youtube)](https://www.youtube.com/@K-Dense-Inc)

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=K-Dense-AI/scientific-agent-skills&type=date&legend=top-left)](https://www.star-history.com/#K-Dense-AI/scientific-agent-skills&type=date&legend=top-left)

> **🔔 Claude Scientific Skills 现已更名为 Scientific Agent Skills。** 技能内容不变，兼容性更广——现在支持任何符合开放 [Agent Skills](https://agentskills.io/) 标准的 AI 智能体（AI agent），而不仅限于 Claude。

> **新功能：[K-Dense BYOK](https://github.com/K-Dense-AI/k-dense-byok)** —— 一款免费开源的 AI 联合科学家，运行于你的桌面端，由 Scientific Agent Skills 驱动。自带 API Key，可选 40+ 模型，享受完整的研究工作区（含网页搜索、文件处理、100+ 科学数据库及本仓库全部 142 项技能）。数据保留在你的本地电脑，如需处理重型任务，还可通过 [Modal](https://modal.com/) 按需扩展至云端算力。[立即开始使用。](https://github.com/K-Dense-AI/k-dense-byok)

> **保持更新：** 关注 K-Dense 的 [X](https://x.com/k_dense_ai)、[LinkedIn](https://www.linkedin.com/company/k-dense-inc) 和 [YouTube](https://www.youtube.com/@K-Dense-Inc)，获取新技能、版本公告、使用教程、研究流程演示及适用于你 AI 智能体的示例。

一套包含 **141 个开箱即用的科学与研究技能**（涵盖癌症基因组学、药物-靶点结合、分子动力学、RNA 速度分析、地理空间科学、时间序列预测、通过 Hugging Science 进行科学 ML 资源发现、78+ 科学数据库等）的完整集合，适用于任何支持开放 [Agent Skills](https://agentskills.io/) 标准的 AI 智能体。由 [K-Dense](https://k-dense.ai) 创建。兼容 **Cursor、Claude Code、Codex、Google Antigravity** 等工具。将你的 AI 编程智能体转变为能够跨生物学、化学、医学等领域执行复杂多步科学工作流的科研助手。

> ⭐ **助力科学领域 AI 更易被发现：** 如果 Scientific Agent Skills 为你节省了时间、教会了你的智能体某项工作流，或帮助你的实验室提升了效率，请 [给本仓库加星](https://github.com/K-Dense-AI/scientific-agent-skills)。一个 Star 是公开信号，表明这些开源、可复用的研究技能值得维护：它能帮助科学家、工程师和开源贡献者发现该项目，展示哪些智能体技能标准正在获得实际采用，并为我们继续为社区扩充技能库提供明确动力。

---

这些技能让你的 AI 智能体能够无缝对接多个科学领域的专业科学库、数据库与工具。虽然智能体本身可以调用任何 Python 包或 API，但这些显式定义的技能提供了精心整理的文档和示例，使其在以下工作流中表现显著更强且更可靠：
- 🧬 生物信息学与基因组学 - 序列分析、单细胞 RNA-seq、基因调控网络、变异注释、系统发育分析
- 🧪 化学信息学与药物发现 - 分子性质预测、虚拟筛选、ADMET 分析、分子对接、先导化合物优化
- 🔬 蛋白质组学与质谱分析 - LC-MS/MS 处理、多肽鉴定、谱图匹配、蛋白质定量
- 🏥 临床研究及精准医学 - 临床试验、药物基因组学、变异解读、用药安全、临床决策支持、治疗方案规划
- 🧠 医疗 AI 与临床机器学习 - EHR（电子健康记录）分析、生理信号处理、医学影像、临床预测模型
- 🖼️ 医学影像与数字病理 - DICOM 处理、全切片图像分析、计算病理学、放射科工作流
- 🤖 机器学习与人工智能 - 深度学习、强化学习、时间序列分析、模型可解释性、贝叶斯方法
- 🔮 材料科学与化学 - 晶体结构分析、相图、代谢建模、计算化学
- 🌌 物理与天文学 - 天文数据分析、坐标变换、宇宙学计算、符号数学、物理计算
- ⚙️ 工程与仿真 - 离散事件仿真、多目标优化、代谢工程、系统建模、流程优化
- 📊 数据分析与可视化 - 统计分析、网络分析、时间序列、出版级图表、大规模数据处理、探索性数据分析（EDA）
- 🌍 地理空间科学与遥感 - 卫星影像处理、GIS 分析、空间统计、地形分析、地球观测机器学习
- 🧪 实验室自动化 - 液体处理协议、实验设备控制、工作流自动化、LIMS 集成
- 📚 科学传播 - 文献综述、同行评审、科技写作、文档处理、海报、幻灯片、示意图、参考文献管理
- 🔬 多组学与系统生物学 - 多模态数据整合、通路分析、网络生物学、系统级洞察
- 🧬 蛋白质工程与设计 - 蛋白质语言模型、结构预测、序列设计、功能注释
- 🎓 研究方法论 - 假设生成、科学头脑风暴、批判性思维、基金申请撰写、学者评估

**将你的 AI 编程智能体转变为桌面上的“AI 科学家”！**

> 🎬 **初次使用 Scientific Agent Skills？** 观看我们的 [Scientific Agent Skills 入门指南](https://youtu.be/ZxbnDaD_FVg) 视频，快速了解使用方法。

---

## 📦 包含内容

本仓库提供 **142 个科学与研究技能**，按以下类别组织：

- **100+ 科学与金融数据库** - 统一的 `database-lookup` 技能可直接访问 78 个公共数据库（PubChem、ChEMBL、UniProt、COSMIC、ClinicalTrials.gov、FRED、USPTO 等），另提供针对 DepMap、Imaging Data Commons、PrimeKG、美国财政部财政数据及 Hugging Science（涵盖 17 个科学领域的精选数据集、模型与演示目录）的专用技能。BioServices（~40 项生物信息学服务）、BioPython（通过 Entrez 访问 38 个 NCBI 子库）和 gget（20+ 基因组数据库）等多数据库包进一步扩展了覆盖范围
- **70+ 优化 Python 包技能** - 为 RDKit、Scanpy、PyTorch Lightning、scikit-learn、BioPython、pyzotero、BioServices、PennyLane、Qiskit、分子动力学（OpenMM/MDAnalysis）、scVelo、TimesFM 等提供显式定义的技能，附带精选文档、示例与最佳实践。注：智能体可使用 *任何* Python 包编写代码，不限于上述列表；这些技能仅为所列包提供更强大、更可靠的调用路径
- **9 项科学集成技能** - 为 Benchling、DNAnexus、LatchBio、OMERO、Protocols.io、Open Notebook、Ginkgo Cloud Lab、LabArchives 和 Opentrons 提供显式定义的技能。同样，智能体不限于此——任何可通过 Python 调用的 API 或平台均可使用；这些技能提供了经过优化且预文档化的调用路径
- **30+ 分析与传播工具** - 文献综述、科技写作、同行评审、文档处理、Paperzilla、PACSOMATIC、Exa Search、海报、幻灯片、示意图、信息图、Mermaid 图表等
- **10+ 研究与临床工具** - 假设生成、基金申请撰写、临床决策支持、治疗方案、BIDS、监管合规、情景分析，以及通过 Autoskill 基于工作流衍生的技能起草

每项技能均包含：
- ✅ 完整文档（`SKILL.md`）
- ✅ 实用代码示例
- ✅ 使用场景与最佳实践
- ✅ 集成指南
- ✅ 参考资料

---

## 📋 目录

- [What's Included](#-whats-included)
- [Why Use This?](#-why-use-this)
- [Getting Started](#-getting-started)
- [Security Disclaimer](#%EF%B8%8F-security-disclaimer)
- [Support Open Source](#%EF%B8%8F-support-the-open-source-community)
- [Prerequisites](#%EF%B8%8F-prerequisites)
- [Quick Examples](#-quick-examples)
- [Use Cases](#-use-cases)
- [Available Skills](#-available-skills)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Support](#-support)
- [Citation](#-citation)
- [License](#-license)

---

## 🚀 为什么使用本仓库？

### ⚡ **加速你的研究**
- **节省数天工作量** - 跳过 API 文档调研与集成配置
- **生产级代码** - 经过测试验证的示例，遵循科学最佳实践
- **多步工作流** - 通过单条提示词执行复杂流水线

### 🎯 **全面覆盖**
- **142 项技能** - 广泛覆盖所有主要科学领域
- **100+ 数据库** - 通过 `database-lookup` 统一访问 78+ 个数据库，另提供专用数据访问技能及 BioServices、BioPython、gget 等多数据库包
- **70+ 优化 Python 包技能** - RDKit、Scanpy、PyTorch Lightning、scikit-learn、BioServices、PennyLane、Qiskit、分子动力学（OpenMM/MDAnalysis）、scVelo、TimesFM 等（智能体可使用任何 Python 包；此处提供的是预文档化且性能更优的路径）

### 🔧 **轻松集成**
- **简单配置** - 将技能复制到你的技能目录即可开始使用
- **自动发现** - 你的智能体会自动查找并使用相关技能
- **文档完善** - 每项技能均包含示例、使用场景与最佳实践

### 🌟 **持续维护与支持**
- **定期更新** - K-Dense 团队持续维护并扩充
- **社区驱动** - 开源项目，拥有活跃的社区贡献
- **企业就绪** - 提供针对高级需求的商业支持

---

## 🎯 快速开始

### 方案一：使用 npx（全平台）

通过一条命令安装 Scientific Agent Skills：

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

这是跨 **所有平台** 安装 Agent Skills 的官方标准方式，适用于 **Claude Code**、**Claude Cowork**、**Codex**、**Gemini CLI**、**Google Antigravity**、**Cursor** 及任何支持开放 [Agent Skills](https://agentskills.io/) 标准的智能体。

### 方案二：使用 GitHub CLI (`gh skill`)

如果你使用 [GitHub CLI](https://cli.github.com/)（v2.90.0+），可通过 [`gh skill`](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/) 安装技能：

```bash
# 交互式浏览并安装
gh skill install K-Dense-AI/scientific-agent-skills

# 直接安装指定技能
gh skill install K-Dense-AI/scientific-agent-skills scanpy

# 指定目标智能体宿主
gh skill install K-Dense-AI/scientific-agent-skills --agent cursor
gh skill install K-Dense-AI/scientific-agent-skills --agent claude-code
gh skill install K-Dense-AI/scientific-agent-skills --agent codex
gh skill install K-Dense-AI/scientific-agent-skills --agent gemini
```

`gh skill` 会自动将技能安装到对应智能体宿主的正确目录，并记录来源元数据以保障供应链完整性。

#### 版本锁定

锁定特定发布标签或 Commit SHA 以实现可复现的安装：

```bash
# 锁定至发布标签
gh skill install K-Dense-AI/scientific-agent-skills --pin v1.0.0

# 锁定至 Commit SHA
gh skill install K-Dense-AI/scientific-agent-skills --pin abc123def
```

#### 保持技能更新

```bash
# 交互式检查更新
gh skill update

# 更新所有已安装的技能
gh skill update --all
```

**完成！** 你的 AI 智能体会自动发现这些技能，并在你执行相关科学任务时调用它们。你也可以通过在提示词中提及技能名称来手动触发任意技能。

---

## ⚠️ 安全免责声明

> **技能可执行代码并影响你的编程智能体行为。请审查你所安装的内容。**

Agent Skills 功能强大——它们可以指示 AI 智能体运行任意代码、安装包、发起网络请求以及修改你系统中的文件。恶意或编写不当的技能可能导致你的编程智能体产生有害行为。

我们高度重视安全性。所有贡献均经过审核流程，且我们对本仓库中的每项技能都运行基于 LLM 的安全扫描（通过 [Cisco AI Defense Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner)）。然而，作为一个团队规模较小但社区贡献日益增多的项目，我们无法保证已对所有可能的风险进行了 exhaustive（穷尽式）审查。

**最终责任在于你本人：请审查你所安装的技能，并自行决定信任哪些。**

我们建议如下操作：

- **不要一次性全部安装。** 仅安装你实际工作所需的技能。在 K-Dense 创建并维护所有技能时，安装完整集合是合理的；但如今仓库包含大量社区贡献内容，我们可能未对其进行了同等程度的审查。
- **安装前阅读 `SKILL.md`。** 每项技能的文档会描述其功能、使用的包及连接的外部服务。若发现可疑之处，请勿安装。
- **查看贡献历史。** 由 K-Dense（`K-Dense-AI`）撰写的技能已通过内部审核流程。社区贡献的技能已尽力审查，但受限于资源。
- **自行运行安全扫描器。** 在安装第三方技能前，请在本地进行扫描：
  ```bash
  uv pip install cisco-ai-skill-scanner
  skill-scanner scan /path/to/skill --use-behavioral
  ```
- **报告可疑内容。** 若发现恶意或行为异常的技能，请立即 [提交 Issue](https://github.com/K-Dense-AI/scientific-agent-skills/issues)，以便我们调查。

所有技能约每周扫描一次，[SECURITY.md](SECURITY.md) 会同步更新最新结果。我们会尽力及时修复安全漏洞。

---

## ❤️ 支持开源社区

Scientific Agent Skills 由全球开发者与科研社区维护的 **50+ 个优秀开源项目** 驱动。Biopython、Scanpy、RDKit、scikit-learn、PyTorch Lightning 等项目构成了这些技能的基础。

**如果你认为本仓库有价值，请考虑支持支撑该项目运行的开源项目：**

- ⭐ **在 GitHub 上给它们加星**
- 💰 **通过 GitHub Sponsors 或 NumFOCUS 赞助维护者**
- 📝 **在你的论文中引用相关项目**
- 💻 **贡献代码、文档或提交 Bug 报告**

👉 **[查看完整的支持项目列表](docs/open-source-sponsors.md)**

---

## ⚙️ 前置条件

- **Python**: 3.13+（用于仓库工具）；各技能依赖可能支持更宽的 Python 版本范围
- **uv**: Python 包管理器（安装技能依赖所必需）
- **客户端**：任何支持 [Agent Skills](https://agentskills.io/) 标准的智能体（Cursor、Claude Code、Gemini CLI、Codex、Google Antigravity 等）
- **系统**：macOS、Linux 或 Windows + WSL2
- **依赖项**：由各个技能自动处理（具体需求请查看 `SKILL.md` 文件）

### 安装 uv

本技能集使用 `uv` 作为包管理器来安装 Python 依赖。请按你的操作系统选择安装方式：

**macOS 与 Linux：**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows：**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**替代方案（通过 pip）：**
```bash
pip install uv
```

安装完成后，运行以下命令验证：
```bash
uv --version
```

更多安装选项与详情，请访问 [官方 uv 文档](https://docs.astral.sh/uv/)。

---

## 💡 快速示例

安装技能后，你可让 AI 智能体执行复杂的多步科学工作流。以下是一些提示词示例：

### 🧪 药物发现流水线
**目标**：寻找针对肺癌治疗的新型 EGFR 抑制剂

**提示词**：
```
Use available skills you have access to whenever possible. Query ChEMBL for EGFR inhibitors (IC50 < 50nM), analyze structure-activity relationships 
with RDKit, generate improved analogs with datamol, perform virtual screening with DiffDock 
against AlphaFold EGFR structure, search PubMed for resistance mechanisms, check COSMIC for 
mutations, and create visualizations and a comprehensive report.
```

**使用的技能**：database-lookup, rdkit, datamol, diffdock, paper-lookup, scientific-visualization

---

### 🔬 单细胞 RNA-seq 分析
**目标**：结合公共数据的 10X Genomics 数据综合分析

**提示词**：
```
Use available skills you have access to whenever possible. Load 10X dataset with Scanpy, perform QC and doublet removal, integrate with Cellxgene 
Census data, identify cell types using NCBI Gene markers, run differential expression with 
PyDESeq2, infer gene regulatory networks with Arboreto, enrich pathways via Reactome/KEGG, 
and identify therapeutic targets with Open Targets.
```

**使用的技能**：scanpy, cellxgene-census, database-lookup, pydeseq2, arboreto

---

### 🧬 多组学生物标志物发现
**目标**：整合 RNA-seq、蛋白质组学与代谢组学数据以预测患者预后

**提示词**：
```
Use available skills you have access to whenever possible. Analyze RNA-seq with PyDESeq2, process mass spec with pyOpenMS, integrate metabolites from 
HMDB/Metabolomics Workbench, map proteins to pathways (UniProt/KEGG), find interactions via 
STRING, correlate omics layers with statsmodels, build predictive model with scikit-learn, 
and search ClinicalTrials.gov for relevant trials.
```

**使用的技能**：pydeseq2, pyopenms, database-lookup, statsmodels, scikit-learn

---

### 🎯 虚拟筛选活动
**目标**：发现蛋白质相互作用的变构调节剂

**提示词**：
```
Use available skills you have access to whenever possible. Retrieve AlphaFold structures, identify interaction interface with BioPython, search ZINC 
for allosteric candidates (MW 300-500, logP 2-4), filter with RDKit, dock with DiffDock, 
rank with DeepChem, check PubChem suppliers, search USPTO patents, and optimize leads with 
MedChem/molfeat.
```

**使用的技能**：database-lookup, biopython, rdkit, diffdock, deepchem, medchem, molfeat

---

### 🏥 临床变异解读
**目标**：分析 VCF 文件以评估遗传性癌症风险

**提示词**：
```
Use available skills you have access to whenever possible. Parse VCF with pysam, annotate variants with Ensembl VEP, query ClinVar for pathogenicity, 
check COSMIC for cancer mutations, retrieve gene info from NCBI Gene, analyze protein impact 
with UniProt, search PubMed for case reports, check ClinPGx for pharmacogenomics, generate 
clinical report with document processing tools, and find matching trials on ClinicalTrials.gov.
```

**使用的技能**：pysam, database-lookup, paper-lookup, clinical-reports, docx, pdf

---

### 🌐 系统生物学网络分析
**目标**：从 RNA-seq 数据分析基因调控网络

**提示词**：
```
Use available skills you have access to whenever possible. Query NCBI Gene for annotations, retrieve sequences from UniProt, identify interactions via 
STRING, map to Reactome/KEGG pathways, analyze topology with Torch Geometric, reconstruct 
GRNs with Arboreto, assess druggability with Open Targets, model with PyMC, visualize 
networks, and search GEO for similar patterns.
```

**使用的技能**：database-lookup, torch-geometric, arboreto, pymc, networkx, scientific-visualization

> 📖 **需要更多示例？** 查看 [docs/examples.md](docs/examples.md) 获取涵盖所有科学领域的完整工作流示例与详细用例。

---

## 🔬 使用场景

### 🧪 药物发现与药物化学
- **虚拟筛选**：针对蛋白质靶点对 PubChem/ZINC 中的数百万化合物进行筛选
- **先导优化**：利用 RDKit 分析构效关系（SAR），通过 datamol 生成类似物
- **ADMET 预测**：使用 DeepChem 预测吸收、分布、代谢、排泄与毒性
- **分子对接**：使用 DiffDock 预测结合姿态与亲和力
- **生物活性挖掘**：查询 ChEMBL 获取已知抑制剂并分析 SAR 模式

### 🧬 生物信息学与基因组学
- **序列分析**：利用 BioPython 和 pysam 处理 DNA/RNA/蛋白质序列
- **单细胞分析**：使用 Scanpy 分析 10X Genomics 数据，识别细胞类型，通过 Arboreto 推断基因调控网络（GRN）
- **变异注释**：使用 Ensembl VEP 注释 VCF 文件，查询 ClinVar 评估致病性
- **变异数据库管理**：利用 TileDB-VCF 构建可扩展的 VCF 数据库，支持增量样本添加、高效群体规模查询及基因组变体数据的压缩存储
- **基因发现**：查询 NCBI Gene、UniProt 和 Ensembl 获取全面基因信息
- **网络分析**：通过 STRING 识别蛋白质相互作用，映射至通路（KEGG, Reactome）

### 🏥 临床研究及精准医学
- **临床试验**：搜索 ClinicalTrials.gov 相关研究，分析纳入/排除标准
- **变异解读**：结合 ClinVar、COSMIC 和 ClinPGx 进行用药基因组学评估
- **用药安全**：查询 FDA 数据库获取不良事件、药物相互作用与召回信息
- **精准治疗**：将患者变异匹配至靶向疗法与临床试验

### 🔬 多组学与系统生物学
- **多组学整合**：结合 RNA-seq、蛋白质组学与代谢组学数据
- **通路分析**：对差异表达基因进行 KEGG/Reactome 通路富集
- **网络生物学**：重构基因调控网络，识别枢纽基因（Hub Genes）
- **生物标志物发现**：整合多组学层以预测患者预后

### 📊 数据分析与可视化
- **统计分析**：执行假设检验、功效分析与实验设计
- **出版级图表**：使用 matplotlib 和 seaborn 创建高质量学术插图
- **网络可视化**：通过 NetworkX 绘制生物网络
- **报告生成**：利用 PDF、DOCX、PPTX、XLSX、MarkItDown、LiteParse 及 clinical-reporting 技能生成综合报告

### 🧪 实验室自动化
- **协议设计**：创建 Opentrons 协议以实现自动化液体处理
- **LIMS 集成**：与 Benchling 和 LabArchives 对接以管理数据
- **工作流自动化**：自动执行多步实验室流程

---

## 📚 可用技能

本仓库包含 **141 个科学与研究技能**，按多个领域组织。每项技能均提供完整的文档、代码示例及与科学库、数据库和工具交互的最佳实践。

### 技能分类

> **注：** 下列 Python 包与集成技能均为 *显式定义* 的技能——经过精心整理，附带文档、示例与最佳实践，以实现更强、更可靠的性能。它们并非上限：智能体仍可安装并使用 *任何* Python 包或调用 *任何* API，即使没有专用技能。此处列出的技能仅旨在让常见工作流更快、更可靠。

#### 🧬 **生物信息学与基因组学**（23 项技能）
- RNA-seq 流水线：Bulk RNA-seq（端到端 FASTQ -> counts -> DE -> enrichment 编排器）
- 序列分析：BioPython, pysam, scikit-bio, BioServices
- 单细胞分析：Scanpy, AnnData, scvi-tools, scVelo（RNA 速度）, Arboreto, Cellxgene Census
- 基因组工具：gget, geniml, gtars, deepTools, FlowIO, Polars-Bio, Zarr, TileDB-VCF
- 差异表达分析：PyDESeq2
- 功能富集：Pathway Enrichment（ORA、GSEA/preranked、ssGSEA via gseapy + g:Profiler；GO, KEGG, Reactome, WikiPathways, MSigDB）
- 系统发育学：ETE Toolkit, Phylogenetics (MAFFT, IQ-TREE 2, FastTree)

#### 🧪 **化学信息学与药物发现**（10 项技能）
- 分子操作：RDKit, Datamol, Molfeat
- 深度学习：DeepChem, TorchDrug
- 对接与筛选：DiffDock
- 分子动力学：OpenMM + MDAnalysis (MD 模拟与轨迹分析)
- 云端量子化学：Rowan (pKa, docking, cofolding)
- 类药性评估：MedChem
- 基准测试：PyTDC

#### 🔬 **蛋白质组学与质谱**（2 项技能）
- 谱图处理：matchms, pyOpenMS

#### 🏥 **临床研究及精准医学**（8 项技能）
- 临床数据库：通过 Database Lookup (ClinicalTrials.gov, ClinVar, ClinPGx, COSMIC, FDA, cBioPortal, Monarch 等)
- 癌症基因组学：DepMap (癌细胞依赖性评分、药物敏感性)
- 癌症影像：Imaging Data Commons (NCI 放射与病理数据集，通过 idc-index)
- 医疗 AI：PyHealth, NeuroKit2, Clinical Decision Support
- 临床文档：Clinical Reports, Treatment Plans

#### 🖼️ **医学影像与数字病理**（3 项技能）
- DICOM 处理：pydicom
- 全切片成像：histolab, PathML

#### 🧠 **神经科学与电生理学**（2 项技能）
- 数据标准：BIDS (脑成像数据结构，适用于神经科学与生物医学数据集)
- 神经记录：Neuropixels-Analysis (细胞外尖峰、硅探针、 spike sorting)

#### 🤖 **机器学习与人工智能**（14 项核心技能）
- 深度学习：PyTorch Lightning, Transformers, Stable Baselines3, PufferLib
- 传统机器学习：scikit-learn, scikit-survival, SHAP
- 时间序列：aeon, TimesFM (Google 的单变量预测零样本基础模型)
- 贝叶斯方法：PyMC
- 优化算法：PyMOO
- 图机器学习：Torch Geometric
- 降维：UMAP-learn
- 统计建模：statsmodels

#### 🔮 **材料科学、化学与物理**（7 项技能）
- 材料科学：Pymatgen
- 代谢建模：COBRApy
- 天文学：Astropy
- 量子计算：Cirq, PennyLane, Qiskit, QuTiP

#### ⚙️ **工程与仿真**（4 项技能）
- 数值计算：MATLAB/Octave
- 计算流体力学：FluidSim
- 离散事件仿真：SimPy
- 符号数学：SymPy

#### 📊 **数据分析与可视化**（19 项技能）
- 可视化：Matplotlib, Seaborn, Scientific Visualization
- 地理空间分析：GeoPandas, GeoMaster (遥感、GIS、卫星影像、空间 ML，500+ 示例)
- 数据处理：Dask, Polars, Vaex
- 网络分析：NetworkX
- 文档处理：LiteParse (本地 PDF/文档解析，支持边界框与 OCR)、MarkItDown、PDF、DOCX、PPTX、XLSX
- 信息图：Infographics (AI 驱动的专业信息图生成)
- 图表：Markdown & Mermaid Writing (文本图表作为默认文档标准)
- 探索性数据分析：EDA workflows
- 统计分析：Statistical Analysis workflows

#### 🧪 **实验室自动化**（6 项技能）
- 液体处理：PyLabRobot, Opentrons
- 云端实验室：Ginkgo Cloud Lab (无细胞蛋白表达、荧光像素艺术，通过自主 RAC 基础设施)
- 协议管理：Protocols.io
- LIMS 集成：Benchling, LabArchives

#### 🔬 **多组学与系统生物学**（4 项技能）
- 通路分析：通过 Database Lookup (KEGG, Reactome, STRING) 与 PrimeKG
- 多组学整合：HypoGeniC
- 数据管理：LaminDB

#### 🧬 **蛋白质工程与设计**（3 项技能）
- 蛋白质语言模型：ESM
- 糖基化工程：Glycoengineering (N/O-糖基化预测、治疗性抗体优化)
- 云端实验室平台：Adaptyv (自动化蛋白质测试与验证)

#### 📚 **科学传播**（27 项技能）
- 文献检索：Paper Lookup (PubMed, PMC, bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall)、Literature Review、Paperzilla
- 高级论文搜索：BGPT Paper Search (每篇论文含 25+ 结构化字段——方法、结果、样本量、质量评分等，基于全文而非仅摘要)
- 网页搜索：Parallel Web, Exa Search, Research Lookup
- 研究笔记：Open Notebook (自托管 NotebookLM 替代品——支持 PDF、视频、音频、网页；16+ AI 提供商；多发言人播客生成)
- 写作：Scientific Writing, Peer Review
- 文档处理：LiteParse, PDF, DOCX, PPTX, XLSX, MarkItDown
- 发表与论文工作流：Venue Templates, PACSOMATIC
- 演示文稿：Scientific Slides, LaTeX Posters, PPTX Posters
- 图表：Scientific Schematics, Markdown & Mermaid Writing
- 信息图：Infographics (10 种类型、8 种风格、色盲安全调色板)
- 引用管理：Citation Management, pyzotero
- 插图生成：Generate Image (基于 FLUX.2 Pro 与 Gemini 3 Pro (Nano Banana Pro) 的 AI 图像生成)

#### 🔬 **科学数据库与数据访问**（6 项技能 → 总计 100+ 数据库）
> 统一的 `database-lookup` 技能提供对所有领域 78 个公共数据库的直接 REST API 访问。专用技能覆盖专业数据平台。BioServices (~40 项生物信息学服务)、BioPython (通过 Entrez 访问 38 个 NCBI 子库) 和 gget (20+ 基因组数据库) 等多数据库包进一步扩展了覆盖范围。
- 统一访问：Database Lookup (78 个数据库，涵盖化学、基因组学、临床、通路、专利、经济学等领域——PubChem, ChEMBL, UniProt, PDB, AlphaFold, KEGG, Reactome, STRING, ClinVar, COSMIC, ClinicalTrials.gov, FDA, FRED, USPTO, SEC EDGAR 等)
- 癌症基因组学：DepMap (癌细胞系依赖性、药物敏感性、基因效应谱)
- 癌症影像：Imaging Data Commons (NCI 放射与病理数据集，通过 idc-index)
- 知识图谱：PrimeKG (精准医学知识图谱——基因、药物、疾病、表型)
- 财政数据：U.S. Treasury Fiscal Data (国债、财政部声明、拍卖、汇率)
- 科学 ML 资源目录：Hugging Science (涵盖 17 个科学领域的精选数据集、模型、博客文章与交互式 Spaces 索引——天文学、生物学、化学、气候、基因组学、材料科学、医学、物理、科学推理等，提供 `datasets`、`transformers` 和 `gradio_client` 的使用模式)

#### 🔧 **基础设施与平台**（8 项技能）
- 云端算力：Modal
- GPU 加速：Optimize for GPU (CuPy, Numba CUDA, Warp, cuDF, cuML, cuGraph, KvikIO, cuCIM, cuxfilter, cuVS, cuSpatial, RAFT)
- 基因组学平台：DNAnexus, LatchBio
- 显微成像：OMERO
- 自动化设备：Opentrons
- 资源检测：Get Available Resources
- 工作流挖掘：Autoskill (基于本地 screenpipe 的重复工作流检测与技能起草)

#### 🎓 **研究方法论与规划**（11 项技能）
- 创意生成：Scientific Brainstorming, Hypothesis Generation
- 批判性分析：Scientific Critical Thinking, Scholar Evaluation
- 情景分析：What-If Oracle (4–6 分支可能性探索、应急预案、决策压力测试)
- 多视角审议：Consciousness Council (多元专家观点、魔鬼代言人分析)
- 认知画像：DHDNA Profiler (从任意文本中提取思维模式与认知特征)
- 基金申请：Research Grants
- 资源发现：Research Lookup, Paper Lookup (10 个学术数据库)
- 市场分析：Market Research Reports

#### ⚖️ **监管与标准**（1 项技能）
- 医疗器械标准：ISO 13485 Certification

> 📖 **查看所有技能的完整详情**，请参阅 [docs/skills.md](docs/skills.md)

> 💡 **寻找实用示例？** 查看 [docs/examples.md](docs/examples.md) 获取涵盖所有科学领域的完整工作流示例。

---

## 🤝 贡献指南

我们欢迎社区扩展与改进本科学技能仓库！

关于添加或更新技能的详细操作，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。该指南涵盖了仓库结构、必需的 `SKILL.md` frontmatter、Agent Skills 规范需求、版本控制、验证流程、安全扫描及 Pull Request 期望。

### 贡献方式

✨ **添加新技能**
- 为更多科学包或数据库创建技能
- 集成科学平台与工具

📚 **改进现有技能**
- 通过更多示例与使用场景完善文档
- 添加新工作流与参考资料
- 优化代码示例与脚本
- 修复 Bug 或更新过时信息

🐛 **报告问题**
- 提交包含详细复现步骤的 Bug 报告
- 提出改进建议或新功能需求

### 贡献流程

1. **Fork** 本仓库
2. **创建**功能分支 (`git checkout -b feature/amazing-skill`)
3. **遵循** [CONTRIBUTING.md](CONTRIBUTING.md) 与现有目录结构
4. **确保**所有新技能均包含有效的 `SKILL.md` 文件（含必需的 frontmatter 与 `metadata.version`）
5. **测试**你的示例与工作流
6. **提交**更改 (`git commit -m 'Add amazing skill'`)
7. **推送**至分支 (`git push origin feature/amazing-skill`)
8. **提交** Pull Request，并清晰描述你的变更

### 贡献规范

✅ **遵守 [Agent Skills Specification](https://agentskills.io/specification)** —— 每项技能必须遵循官方规范（有效的 `SKILL.md` frontmatter、命名约定、目录结构）  
✅ 在每个 `SKILL.md` 中包含带引号的 `metadata.version` 值  
✅ 更新现有技能时递增 `metadata.version`  
✅ 保持与现有技能文档格式一致  
✅ 确保所有代码示例经过测试且可正常运行  
✅ 在示例与工作流中遵循科学最佳实践  
✅ 添加新功能时同步更新相关文档  
✅ 在代码中提供清晰的注释与 docstrings  
✅ 引用官方文档

### 安全扫描

本仓库中的所有技能均使用 [Cisco AI Defense Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner) 进行安全扫描。这是一款开源工具，可检测 Agent Skills 中的提示词注入、数据外泄及恶意代码模式。

若你正在贡献新技能，建议在提交 Pull Request 前在本地运行扫描器：

```bash
uv pip install cisco-ai-skill-scanner
skill-scanner scan /path/to/your/skill --use-behavioral
```

> **注：** 干净的扫描结果可减少审核噪音，但并不能保证技能完全无风险。所有贡献的技能在合并前均会经过人工审查。

### 认可与致谢

贡献者将在我们的社区中获得认可，并可能出现在：
- 仓库贡献者列表
- 版本公告中的特别鸣谢
- K-Dense 社区精选展示

你的贡献将使科学计算更易获取，帮助研究人员更有效地利用 AI 工具！

### 支持开源

本项目构建于 50+ 个优秀开源项目之上。如果你认为这些技能有价值，请考虑 [支持我们依赖的开源项目](docs/open-source-sponsors.md)。

---

## 🔧 故障排除

### 常见问题

**问题：技能未加载**
- 确认技能文件夹位于正确目录（参见 [快速开始](#-getting-started)）
- 每个技能文件夹必须包含 `SKILL.md` 文件
- 复制技能后重启你的智能体/IDE
- 在 Cursor 中，检查 Settings → Rules 以确认技能已被发现

**问题：缺少 Python 依赖**
- 解决方案：查看对应技能的 `SKILL.md` 文件获取所需包列表
- 安装依赖：`uv pip install package-name`

**问题：API 速率限制**
- 解决方案：许多数据库设有速率限制。请查阅具体数据库文档
- 建议实现缓存或批量请求机制

**问题：认证错误**
- 解决方案：部分服务需要 API Key。查看 `SKILL.md` 中的认证配置说明
- 验证你的凭据与权限

**问题：示例过时**
- 解决方案：通过 GitHub Issues 报告该问题
- 查阅官方包文档获取最新语法

**问题：`gh skill install` 或文档链接指向 `scientific-skills/` 失败（v2.43.0+）**
- 自 v2.43.0 起，技能位于 `skills/` 目录下（而非 `scientific-skills/`），以匹配 GitHub CLI 预期的 Agent Skills 布局
- 请将手动复制路径、书签与引用中的 `scientific-skills/<name>` 更新为 `skills/<name>`
- 拉取最新版本后重新运行 `gh skill install K-Dense-AI/scientific-agent-skills`

---

## ❓ 常见问题 (FAQ)

### 通用问题

**问：使用是否免费？**  
答：是的！本仓库采用 MIT 许可证。但每项独立技能均在其 `SKILL.md` 文件的 `license` 元数据字段中声明了各自的许可协议——请务必查阅并遵守相关条款。

**问：为什么所有技能都打包在一起，而不是拆分为独立的包？**  
答：我们认为在 AI 时代，优秀的科学研究本质上是跨学科的。将所有技能捆绑在一起可让你（及你的智能体）轻松跨越领域协作——例如在一个工作流中结合基因组学、化学信息学、临床数据与机器学习——而无需担心该安装或配置哪些独立技能。

**问：能否用于商业项目？**  
答：仓库本身采用 MIT 许可证，允许商业用途。但部分技能可能具有不同的许可协议——请检查各技能 `SKILL.md` 文件中的 `license` 字段以确保符合你的使用意图。

**问：所有技能的许可证是否相同？**  
答：不相同。每项技能均在其 `SKILL.md` 文件的 `license` 元数据字段中声明了各自的许可协议。这些协议可能与仓库的 MIT 许可证不同。用户需自行审查并遵守所使用各项技能的许可条款。

**问：更新频率如何？**  
答：我们会定期更新技能以反映最新版本的包与 API。重大更新将在版本公告中说明。

**问：能否与其他 AI 模型配合使用？**  
答：这些技能遵循开放的 [Agent Skills](https://agentskills.io/) 标准，可与任何兼容的智能体配合使用，包括 Cursor、Claude Code、Codex 和 Google Antigravity。

### 安装与配置

**问：我需要安装所有 Python 包吗？**  
答：不需要！仅安装你实际需要的包即可。每项技能均在其 `SKILL.md` 文件中声明了所需依赖。

**问：如果某项技能无法正常工作怎么办？**  
答：首先查阅 [故障排除](#-troubleshooting) 章节。若问题持续，请在 GitHub 提交 Issue 并附上详细的复现步骤。

**问：这些技能支持离线使用吗？**  
答：数据库类技能需要联网以查询 API。包类技能在 Python 依赖安装完成后可离线运行。

### 贡献相关

**问：我能贡献自己的技能吗？**  
答：当然！我们欢迎社区贡献。请参阅 [贡献指南](#-contributing) 章节了解规范与最佳实践。

**问：如何报告 Bug 或提出功能建议？**  
答：在 GitHub 上提交 Issue 并清晰描述问题。对于 Bug，请包含复现步骤及预期与实际行为对比。

---

## 💬 支持渠道

需要帮助？可通过以下方式获取支持：

- 📖 **文档**：查阅相关 `SKILL.md` 与 `references/` 文件夹
- 🐛 **Bug 报告**：[提交 Issue](https://github.com/K-Dense-AI/scientific-agent-skills/issues)
- 💡 **功能建议**：[提交新功能请求](https://github.com/K-Dense-AI/scientific-agent-skills/issues/new)
- 📣 **更新与演示**：关注 [X](https://x.com/k_dense_ai)、[LinkedIn](https://www.linkedin.com/company/k-dense-inc) 和 [YouTube](https://www.youtube.com/@K-Dense-Inc)，获取新技能、教程及 Scientific Agent Skills 版本动态
- 💼 **企业支持**：联系 [K-Dense](https://k-dense.ai/) 获取商业技术支持

---

## 📖 引用规范

如果你在研究或项目中使用了 Scientific Agent Skills，请引用整体资源集合；并在相关情况下，引用对你工作有实质贡献的独立技能。

引用整个集合有助于他人发现该仓库、了解你工作流中使用的更广泛技能生态，并为 Scientific Agent Skills 的维护工作提供致谢。引用具体技能则可为你的智能体实际调用的特定包、数据库或工作流指导提供更精准的学术认可。

推荐做法：
- 始终使用以下任一格式引用 **Scientific Agent Skills**。
- 同时引用直接参与你分析、代码、图表、报告或研究工作流的各项独立技能。
- 若某项技能封装或文档化了外部包、数据库或平台，且你的学科规范有此要求，请一并引用上游项目。

### 集合引用格式

#### BibTeX
```bibtex
@software{scientific_agent_skills_2026,
  author = {{K-Dense Inc.}},
  title = {Scientific Agent Skills: A Comprehensive Collection of Scientific Tools for AI Agents},
  year = {2026},
  url = {https://github.com/K-Dense-AI/scientific-agent-skills},
  note = {142 skills covering databases, packages, integrations, and analysis tools}
}
```

#### APA
```
K-Dense Inc. (2026). Scientific Agent Skills: A comprehensive collection of scientific tools for AI agents [Computer software]. https://github.com/K-Dense-AI/scientific-agent-skills
```

#### MLA
```
K-Dense Inc. Scientific Agent Skills: A Comprehensive Collection of Scientific Tools for AI Agents. 2026, github.com/K-Dense-AI/scientific-agent-skills.
```

#### Plain Text
```
Scientific Agent Skills by K-Dense Inc. (2026)
Available at: https://github.com/K-Dense-AI/scientific-agent-skills
```

### 独立技能引用格式

引用特定技能时，请包含技能名称、该技能 `SKILL.md` 中 `metadata.version` 的版本号及直接链接。例如：

```bibtex
@software{scientific_agent_skills_astropy_2026,
  author = {{K-Dense Inc.}},
  title = {Astropy Skill for Scientific Agent Skills},
  year = {2026},
  url = {https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/astropy},
  note = {Version 1.0, part of Scientific Agent Skills}
}
```

纯文本格式：

```text
Astropy skill for Scientific Agent Skills, version 1.0.
K-Dense Inc. (2026).
https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/astropy
```

我们感谢在受益于这些技能的研究论文、演示或项目中给予的引用与认可。

---

## 📄 许可证

本项目采用 **MIT License** 许可协议发布。

**版权所有 © 2026 K-Dense Inc.** ([k-dense.ai](https://k-dense.ai/))

### 核心条款：
- ✅ **免费使用**（商业与非商业用途均可）
- ✅ **开源** - 可自由修改、分发与使用
- ✅ **宽松许可** - 对复用限制极少
- ⚠️ **无担保** - 按“原样”提供，不提供任何形式的明示或暗示担保

完整条款请参阅 [LICENSE.md](LICENSE.md)。

### 独立技能许可证

> ⚠️ **重要提示**：每项技能均在其 `SKILL.md` 文件的 `license` 元数据字段中声明了各自的许可协议。这些协议可能与仓库的 MIT 许可证不同，并可能包含额外条款或限制。**用户需自行审查并遵守所使用各项技能的许可条款。**