# LLM Wiki

<p align="center">
  <img src="logo.jpg" width="128" height="128" style="border-radius: 22%;" alt="LLM Wiki Logo">
</p>

<p align="center">
  <strong>一个自动构建的个人知识库。</strong><br>
  LLM（大语言模型）会读取你的文档，构建结构化的 Wiki，并保持其内容持续更新。
</p>

<p align="center">
  <a href="#what-is-this">这是什么？</a> •
  <a href="#what-we-changed--added">功能特性</a> •
  <a href="#tech-stack">技术栈</a> •
  <a href="#installation">安装指南</a> •
  <a href="#credits">鸣谢</a> •
  <a href="#license">开源协议</a>
</p>

<p align="center">
  English | <a href="README_CN.md">中文</a> | <a href="README_JA.md">日本語</a> | <a href="README_KO.md">한국어</a>
</p>

---

<p align="center">
  <img src="assets/overview.jpg" width="100%" alt="Overview">
</p>

## 功能特性

- **两步思维链摄入流程** —— LLM 先进行分析，随后生成带有来源可追溯性和增量缓存的 Wiki 页面
- **多模态图像摄入** —— 从 PDF 中提取嵌入图片，使用视觉 LLM 生成事实性描述，在支持灯箱预览和跳转至来源的图片感知搜索结果中展示它们
- **四信号知识图谱** —— 包含直接链接、来源重叠、Adamic-Adar 算法和类型亲和度的相关性模型
- **Louvain 社区发现** —— 自动发现知识簇并计算凝聚力评分
- **图谱洞察（Graph Insights）** —— 一键 Deep Research（深度研究）揭示意外关联与知识盲区
- **向量语义搜索** —— 可选的基于嵌入向量的检索，通过 LanceDB 实现，支持任意 OpenAI 兼容端点
- **持久化摄入队列** —— 串行处理，具备崩溃恢复、取消、重试及进度可视化功能
- **文件夹导入** —— 递归导入文件夹并保留目录结构，将文件夹路径作为 LLM 分类提示词（例如 `"papers > energy"` 有助于内容归类）
- **来源文件夹自动监听** —— 检测 `raw/sources/` 中的外部变更，保持摄入与删除清理操作同步
- **深度研究（Deep Research）** —— LLM 优化搜索主题，通过 Tavily、SerpApi 或 SearXNG 进行多查询网络搜索，自动将结果摄入 Wiki
- **异步审核系统** —— LLM 标记需人工判断的条目，支持预定义操作与预生成搜索查询
- **Chrome 网页剪藏扩展** —— 一键捕获网页并自动摄入知识库
- **本地 HTTP API + MCP 服务器 + AI 智能体技能** —— 内置 `127.0.0.1:19828` JSON API 及打包的 MCP 服务器，支持混合搜索、文件读取、图谱遍历和来源重扫描；提供现成的 [agent skill](https://github.com/nashsu/llm_wiki_skill)，一条命令即可安装至 Claude Code / Codex（`npx skills add …`）

## 这是什么？

LLM Wiki 是一款跨平台桌面应用程序，可将你的文档自动转化为结构清晰、相互关联的知识库。与传统 RAG（每次从头检索并回答）不同，该工具让 LLM **增量构建并维护一个持久化的 Wiki**。知识只需编译一次并保持更新，而非在每次查询时重新推导。

本项目基于 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) —— 一种使用 LLM 构建个人知识库的方法论。我们将其核心思想实现为功能完整的桌面应用程序，并进行了显著增强。

<p align="center">
  <img src="assets/llm_wiki_arch.jpg" width="100%" alt="LLM Wiki Architecture">
</p>

## 鸣谢

基础方法论源自 **Andrej Karpathy** 的 [llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)，该文档描述了使用 LLM 增量构建和维护个人 Wiki 的模式。原始文件是一份抽象的设计模式说明；本项目则是带有大量扩展的具体实现。

## 我们保留的原生设计

核心架构忠实遵循 Karpathy 的设计：

- **三层架构**：Raw Sources（不可变来源） → Wiki（LLM 生成内容） → Schema（规则与配置）
- **三大核心操作**：Ingest（摄入）、Query（查询）、Lint（校验）
- **index.md** 作为内容目录和 LLM 导航入口点
- **log.md** 作为带可解析格式的 chronological 操作记录
- **[[wikilink]]** 语法用于交叉引用
- **YAML frontmatter** 应用于每个 Wiki 页面头部
- **Obsidian 兼容性** —— Wiki 目录可直接作为 Obsidian vault（知识库）使用
- **人类审核，LLM 维护** —— 明确的角色分工

<p align="center">
  <img src="assets/5-obsidian_compatibility.jpg" width="100%" alt="Obsidian Compatibility">
</p>

## 我们修改与新增的内容

### 1. 从命令行到桌面应用程序

原版是一个抽象的模式文档，设计用于复制粘贴给 LLM agent。我们将其构建为**完整的跨平台桌面应用程序**，包含：
- **三栏布局**：知识树 / 文件树（左侧）+ 聊天窗口（中间）+ 预览面板（右侧）
- **图标侧边栏**：用于在 Wiki、Sources、Search、Graph、Lint、Review、Deep Research、Settings 之间切换
- **自定义可调整面板** —— 支持拖拽调整左右面板大小，并设置最小/最大尺寸限制
- **活动面板（Activity Panel）** —— 实时显示处理状态，展示逐文件摄入进度
- **全量状态持久化** —— 对话记录、设置项、审核条目、项目配置在重启后均会保留
- **场景模板** —— Research、Reading、Personal Growth、Business、General —— 每种预设都会自动配置 `purpose.md` 和 `schema.md`

### 2. Purpose.md —— Wiki 的灵魂

原版有 Schema（定义 Wiki 如何工作），但缺少正式记录 **为什么** 创建该 Wiki 的地方。我们新增了 `purpose.md`：
- 定义目标、关键问题、研究范围及不断演进的论点
- LLM 在每次摄入和查询时都会读取它以获取上下文
- LLM 可根据使用模式建议更新内容
- 与 schema 不同 —— schema 是结构规则，purpose 是指向性意图

### 3. 两步思维链摄入流程

原版描述的是单步摄入（LLM 同时阅读和写入）。我们将其拆分为**两次顺序调用的 LLM 请求**，以显著提升质量：

```
Step 1 (Analysis): LLM reads source → structured analysis
  - Key entities, concepts, arguments
  - Connections to existing wiki content
  - Contradictions & tensions with existing knowledge
  - Recommendations for wiki structure

Step 2 (Generation): LLM takes analysis → generates wiki files
  - Source summary with frontmatter (type, title, sources[])
  - Entity pages, concept pages with cross-references
  - Updated index.md, log.md, overview.md
  - Review items for human judgment
  - Search queries for Deep Research
```

除原版外的其他摄入增强：
- **SHA256 增量缓存** —— 摄入前对源文件内容进行哈希计算；未变更的文件会自动跳过，节省 LLM Token 和时间
- **持久化摄入队列** —— 串行处理防止并发调用 LLM；队列持久化到磁盘，应用重启后恢复；失败任务自动重试最多 3 次
- **文件夹导入** —— 递归导入保留目录结构；文件夹路径作为分类上下文传递给 LLM（例如 `"papers > energy"` 有助于内容归类）
- **来源文件夹自动监听** —— 在 `raw/sources/` 中由应用外添加、编辑或删除的文件会被自动捕获，并复用与内部操作相同的摄入/删除生命周期
- **队列可视化** —— Activity Panel 显示进度条，以及待处理/进行中/失败的任务，并提供取消和重试按钮
- **自动向量化（Auto-embedding）** —— 启用向量搜索时，新页面在摄入后会自动生成嵌入向量
- **来源可追溯性** —— 每个生成的 Wiki 页面都在 YAML frontmatter 中包含 `sources: []` 字段，反向链接到贡献该内容的原始源文件
- **overview.md 自动更新** —— 全局摘要页在每次摄入时重新生成，以反映 Wiki 的最新状态
- **保证来源摘要** —— 提供降级机制，确保即使 LLM 遗漏也会始终创建来源摘要页面
- **语言感知生成** —— LLM 会以用户配置的语言（英文或中文）响应
- **渐进式 Sources 视图** —— 大型源文件夹在滚动时渐进渲染，保持大规模源集合的流畅性

### 4. 带相关性模型的知识图谱

<p align="center">
  <img src="assets/3-knowledge_graph.jpg" width="100%" alt="Knowledge Graph">
</p>

原版仅提及用于交叉引用的 `[[wikilinks]]`，并无图谱分析。我们构建了**完整知识图谱可视化与相关性引擎**：

**四信号相关性模型：**
| 信号 | 权重 | 描述 |
|--------|--------|-------------|
| Direct link（直接链接） | ×3.0 | 通过 `[[wikilinks]]` 关联的页面 |
| Source overlap（来源重叠） | ×4.0 | 共享相同原始来源的页面（通过 frontmatter `sources[]`） |
| Adamic-Adar | ×1.5 | 共享共同邻居的页面（按邻居度数加权） |
| Type affinity（类型亲和度） | ×1.0 | 同类别页面的加分项（entity↔entity, concept↔concept） |

**图谱可视化（sigma.js + graphology + ForceAtlas2）：**
- 节点颜色按页面类型或社区划分，大小由链接数缩放（√ 比例缩放）
- 边粗细与颜色对应相关性权重（绿色=强关联，灰色=弱关联）
- 悬停交互：邻居保持可见，非邻居变暗，高亮显示带相关性分数标签的边
- 缩放控制（ZoomIn, ZoomOut, Fit-to-screen）
- 位置缓存防止数据更新时的布局跳变
- 图例根据着色模式在类型统计和社区信息间切换

### 5. Louvain 社区发现算法

原版未包含。使用 **Louvain 算法**（graphology-communities-louvain）自动发现知识簇：

- **自动聚类** —— 基于链接拓扑结构发现自然分组，独立于预定义的页面类型
- **类型 / 社区切换** —— 可在按页面类型着色（entity, concept, source...）与按发现的知識簇着色之间切换
- **凝聚力评分** —— 每个社区根据内部边密度（实际边数 / 可能边数）进行评分；低凝聚力簇（< 0.15）会标记警告
- **12色调色板** —— 集群间保持清晰的视觉区分
- **社区图例** —— 显示顶级节点标签、成员数量及各集群的凝聚力

<p align="center">
  <img src="assets/kg_community.jpg" width="100%" alt="Louvain Community Detection">
</p>

### 6. 图谱洞察 —— 意外关联与知识盲区

原版未包含。系统会**自动分析图谱结构**以呈现可操作的洞察：

**意外关联（Surprising Connections）：**
- 检测非预期关系：跨社区边、跨类型链接、边缘↔中心耦合
- 综合惊喜分数对最值得关注的连接进行排序
- 可忽略 —— 标记为已审核的连接不会再次出现

**知识盲区（Knowledge Gaps）：**
- **孤立页面**（degree ≤ 1）—— 与 Wiki 其余部分极少或完全没有连接的页面
- **稀疏社区**（cohesion < 0.15, ≥ 3 pages）—— 内部交叉引用较弱的知识领域
- **桥梁节点**（连接 3+ clusters）—— 将多个知识领域维系在一起的关键枢纽页面

**交互功能：**
- 点击任意洞察卡片可在图谱中**高亮**对应节点和边；再次点击取消选中
- 知识盲区和桥梁节点带有 **Deep Research 按钮** —— 触发 LLM 优化的研究，使用领域感知主题（读取 `overview.md` + `purpose.md` 获取上下文）
- 研究主题在启动前会显示在**可编辑的确认对话框**中 —— 用户可在此优化主题和搜索查询

<p align="center">
  <img src="assets/kg_insights.jpg" width="100%" alt="Graph Insights">
</p>

### 7. 优化的查询检索管线

原版描述的是简单查询（LLM 读取相关页面）。我们构建了**多阶段检索管线**，支持可选向量搜索与预算控制：

```
Phase 1: Tokenized Search
  - English: word splitting + stop word removal
  - Chinese: CJK bigram tokenization (每个 → [每个, 个…])
  - Title match bonus (+10 score)
  - Searches both wiki/ and raw/sources/

Phase 1.5: Vector Semantic Search (optional)
  - Embedding via any OpenAI-compatible /v1/embeddings endpoint
  - Stored in LanceDB (Rust backend) for fast ANN retrieval
  - Cosine similarity finds semantically related pages even without keyword overlap
  - Results merged into search: boosts existing matches + adds new discoveries

Phase 2: Graph Expansion
  - Top search results used as seed nodes
  - 4-signal relevance model finds related pages
  - 2-hop traversal with decay for deeper connections

Phase 3: Budget Control
  - Configurable context window: 4K → 1M tokens
  - Proportional allocation: 60% wiki pages, 20% chat history, 5% index, 15% system
  - Pages prioritized by combined search + graph relevance score

Phase 4: Context Assembly
  - Numbered pages with full content (not just summaries)
  - System prompt includes: purpose.md, language rules, citation format, index.md
  - LLM instructed to cite pages by number: [1], [2], etc.
```

**向量搜索**完全可选 —— 默认禁用，在 Settings 中启用并独立配置端点、API Key 和模型。禁用时，管线回退到分词搜索 + 图谱扩展。基准测试显示：开启向量搜索后整体召回率从 58.2% 提升至 71.4%。

### 8. 支持持久化的多对话聊天

原版仅有一个查询界面。我们构建了**完整的多对话支持**：

- **独立会话** —— 创建、重命名、删除对话
- **对话侧边栏** —— 快速切换不同主题
- **单会话持久化** —— 每个对话保存至 `.llm-wiki/chats/{id}.json`
- **可配置历史深度** —— 限制作为上下文发送的消息数量（默认：10）
- **引用参考面板** —— 每条回复下方的可折叠区域，显示所用 Wiki 页面，按类型分组并带图标
- **引用持久化** —— 引用页面直接存储在消息数据中，重启后保持稳定
- **重新生成（Regenerate）** —— 一键重新生成最后一条回复（移除最后一对助手+用户消息并重发）
- **保存到 Wiki（Save to Wiki）** —— 将高质量答案归档至 `wiki/queries/`，随后自动摄入以提取实体/概念到知识网络中

### 9. 思维 / 推理过程展示

原版未包含。针对输出 `<think>` 块的 LLM（如 DeepSeek、QwQ 等）：

- **流式思维** —— 生成期间显示滚动 5 行并带透明度渐变的思考内容
- **默认折叠** —— 完成后隐藏思考块，点击可展开
- **视觉分隔** —— 思考内容与主回复使用不同样式区分展示

### 10. KaTeX 数学公式渲染

原版未包含。全视图支持完整 LaTeX 数学：

- **KaTeX 渲染** —— 行内 `$...$` 和块级 `$$...$$` 公式通过 remark-math + rehype-katex 渲染
- **Milkdown math 插件** —— 预览编辑器通过 @milkdown/plugin-math 原生渲染数学
- **自动检测** —— 裸 `\begin{aligned}` 及其他 LaTeX 环境会自动包裹 `$$` 分隔符
- **Unicode 降级方案** —— 100+ 符号映射（α, ∑, →, ≤ 等），用于数学块外的简单行内表示

### 11. 审核系统（异步人机协同）

原版建议用户在摄入期间保持参与。我们新增了**异步审核队列**：

- LLM 在摄入过程中标记需要人工判断的条目
- **预定义操作类型**：Create Page, Deep Research, Skip —— 受限于防止 LLM 幻觉出任意操作
- **摄入时生成搜索查询** —— LLM 为每个审核项预先优化网络搜索查询
- 用户可按需处理审核 —— 不会阻塞摄入流程

### 12. 深度研究（Deep Research）

<p align="center">
  <img src="assets/1-deepresearch.jpg" width="100%" alt="Deep Research">
</p>

原版未包含。当 LLM 识别出知识盲区时：

- **网络搜索** —— 通过 Tavily、SerpApi 或 SearXNG 查找相关来源并完整提取内容（无截断）
- **提供商特定配置** —— Tavily 和 SerpApi 使用独立 API Key；SerpApi 支持选择搜索引擎，而 SearXNG 使用配置的实例 URL 和搜索分类
- **多查询匹配** —— 每个主题多条 LLM 生成的搜索查询，针对搜索引擎优化
- **LLM 优化研究主题** —— 从 Graph Insights 触发时，LLM 读取 `overview.md` + `purpose.md` 生成领域特定主题和查询（而非通用关键词）
- **用户确认对话框** —— 启动前显示可编辑的主题和搜索供审核
- **LLM 综合结果** —— 将发现内容合成为 Wiki 研究页面，并与现有 Wiki 建立交叉引用
- **思维展示** —— `<think>` 块在合成期间作为可折叠部分显示，自动滚动至最新内容
- **自动摄入** —— 研究成果自动处理以提取实体/概念到 Wiki
- **任务队列** —— 支持 3 个并发任务
- **研究面板（Research Panel）** —— 专用侧边栏面板，高度动态调整，实时流式进度显示

### 13. 浏览器扩展（网页剪藏）

<p align="center">
  <img src="assets/4-chrome_extension_webclipper.jpg" width="100%" alt="Chrome Extension Web Clipper">
</p>

原版提及 Obsidian Web Clipper。我们构建了**专用 Chrome 扩展**（Manifest V3）：

- **Mozilla Readability.js** —— 精准提取文章正文（剥离广告、导航、侧边栏）
- **Turndown.js** —— HTML → Markdown 转换，支持表格保留
- **项目选择器** —— 选择剪藏至哪个 Wiki（支持多项目）
- **本地 HTTP API**（端口 19827, tiny_http）—— 扩展 ↔ 应用程序通信
- **自动摄入** —— 剪藏内容自动触发两步摄入管线
- **剪藏监听器** —— 每 3 秒轮询新剪藏，自动处理
- **离线预览** —— 即使应用未运行也能显示提取的内容

### 14. 多格式文档支持

原版聚焦于文本/Markdown。我们支持结构化提取并保留文档语义：

| 格式 | 方法 |
|--------|--------|
| PDF | pdf-extract (Rust) 配合文件缓存 |
| DOCX | docx-rs —— 标题、粗体/斜体、列表、表格 → 结构化 Markdown |
| PPTX | ZIP + XML —— 逐页提取，保留标题/列表结构 |
| XLSX/XLS/ODS | calamine —— 正确识别单元格类型，支持多工作表，输出 Markdown 表格 |
| Images | 原生预览（png, jpg, gif, webp, svg 等） |
| Video/Audio | 内置播放器 |
| Web clips | Readability.js + Turndown.js → 纯净 Markdown |

### 15. 级联清理的文件删除机制

原版无删除机制。我们新增了**智能级联删除**：

- 删除源文件会移除其对应的 Wiki 摘要页
- **三种匹配方法** 查找相关 Wiki 页面：frontmatter `sources[]` 字段、来源摘要页名称、frontmatter 章节引用
- **共享实体保护** —— 链接到多个源的实体/概念页仅从 `sources[]` 数组中移除已删除的源，不会整体删除该页面
- **索引清理** —— 被删页面会从 index.md 中清除
- **Wiki 链接清理** —— 指向已删除页面的死链 `[[wikilinks]]` 会从剩余 Wiki 页中移除

### 16. 可配置上下文窗口

原版未包含。用户可配置 LLM 接收的上下文量：

- **滑块范围从 4K 到 1M Token** —— 适配不同 LLM 能力
- **按比例预算分配** —— 更大的窗口获得成比例的更多 Wiki 内容
- **60/20/5/15 拆分比例** —— Wiki 页面 / 聊天历史 / 索引 / 系统提示词

### 17. 跨平台兼容性

原版是平台无关的（抽象模式）。我们处理了具体的跨平台问题：

- **路径规范化** —— 统一使用 `normalizePath()`，反斜杠 → 正斜杠
- **Unicode 安全字符串处理** —— 基于字符切片而非字节（防止 CJK 文件名导致崩溃）
- **macOS 点击关闭隐藏** —— 关闭窗口仅隐藏窗口（应用后台运行），点击 Dock 图标恢复，Cmd+Q 退出
- **Windows/Linux 关闭确认** —— 退出前弹出确认对话框，防止意外数据丢失
- **Tauri v2** —— macOS、Windows、Linux 原生桌面体验
- **GitHub Actions CI/CD** —— 自动化构建：macOS (ARM + Intel)、Windows (.msi)、Linux (.deb / .AppImage)

### 18. 其他新增功能

- **国际化（i18n）** —— 英文 + 中文界面（react-i18next）
- **设置持久化** —— LLM 提供商、API Key、模型、上下文大小、语言通过 Tauri Store 保存
- **Obsidian 配置** —— 自动生成 `.obsidian/` 目录及推荐设置
- **Markdown 渲染** —— GFM 表格带边框，代码块正确高亮，聊天和预览中处理 Wiki 链接
- **多提供商 LLM 支持** —— OpenAI、Anthropic、Google、Ollama、Custom —— 各提供程序独立流式传输与请求头配置
- **15分钟超时保护** —— 长时间摄入操作不会提前失败
- **dataVersion 信号机制** —— Wiki 内容变更时，图谱和 UI 自动刷新

## 技术栈（Tech Stack）

| 层级 | 技术选型 |
|-------|-----------|
| Desktop | Tauri v2 (Rust backend) |
| Frontend | React 19 + TypeScript + Vite |
| UI | shadcn/ui + Tailwind CSS v4 |
| Editor | Milkdown (基于 ProseMirror 的 WYSIWYG) |
| Graph | sigma.js + graphology + ForceAtlas2 |
| Search | Tokenized search + graph relevance + optional vector (LanceDB) |
| Vector DB | LanceDB (Rust, embedded, optional) |
| PDF | pdf-extract |
| Office | docx-rs + calamine |
| i18n | react-i18next |
| State | Zustand |
| LLM | Streaming fetch (OpenAI, Anthropic, Google, Ollama, Custom) |
| Web Search | Tavily, SerpApi, SearXNG JSON API |

## 安装指南（Installation）

### 预编译二进制文件

从 [Releases](https://github.com/nashsu/llm_wiki/releases) 下载：
- **macOS**: `.dmg` (Apple Silicon + Intel)
- **Windows**: `.msi`
- **Linux**: `.deb` / `.AppImage`

### 从源码构建（Build from Source）

```bash
# Prerequisites: Node.js 20+, Rust 1.70+
git clone https://github.com/nashsu/llm_wiki.git
cd llm_wiki
npm install
npm run tauri dev      # Development
npm run tauri build    # Production build
```

### Chrome 扩展安装（Chrome Extension）

1. 打开 `chrome://extensions`
2. 启用 "Developer mode"
3. 点击 "Load unpacked"
4. 选择 `extension/` 目录

## 快速开始（Quick Start）

1. 启动应用 → 创建新项目（选择模板）
2. 进入 **Settings** → 配置你的 LLM 提供商（API Key + 模型）
3. 可选：在 Settings 中配置 **Web Search** 提供商和来源文件夹自动监听
4. 前往 **Sources** → 导入文档（PDF, DOCX, MD 等）
5. 观察 **Activity Panel** —— LLM 会自动构建 Wiki 页面
6. 使用 **Chat** 查询你的知识库
7. 浏览 **Knowledge Graph** 查看关联关系
8. 检查 **Review** 处理需人工关注的条目
9. 定期运行 **Lint** 维护 Wiki 健康状态

## 本地 HTTP API + MCP 服务器 + AI 智能体技能（Local HTTP API + MCP Server + AI Agent Skill）

LLM Wiki 内置了位于 `http://127.0.0.1:19828` 的本地 HTTP API（Token 保护，仅限 `127.0.0.1`），以便外部工具 —— 包括 **Claude Code**、**Codex** 或任何支持 HTTP 的脚本 —— 能够查询你的 Wiki：

- `GET /api/v1/health` —— 服务器状态（无需认证）
- `GET /api/v1/projects` —— 列出项目
- `GET /api/v1/projects/{id}/files` / `files/content` —— 读取文件和内容
- `POST /api/v1/projects/{id}/search` —— **混合**检索（关键词 + 向量），返回 `mode`, `tokenHits`, `vectorHits`, 以及每条结果的 `vectorScore`
- `GET /api/v1/projects/{id}/graph` —— Wiki 链接图谱
- `POST /api/v1/projects/{id}/sources/rescan` —— 触发后端重扫描

在 **Settings → API + MCP** 中启用 API、生成 Token，并选择是否允许本地未认证访问。

对于支持 MCP 的客户端，LLM Wiki 还在 `mcp-server/` 目录中包含了一个本地 MCP 服务器。使用 `npm run mcp:build` 构建后，**Settings → API + MCP** 会显示可复制的 MCP 客户端配置及适用于你机器的正确本地路径。MCP 工具调用相同的 API 接口，因此智能体客户端可以列出项目、读取文件、执行混合搜索、检查图谱并触发来源重扫描，无需编写自定义 HTTP 胶水代码。

### 一条命令接入你的 AI 智能体

LLM Wiki 的现成 **agent skill** 托管在独立仓库中。安装至 Claude Code / Codex / 任何支持 skills 的运行环境：

```bash
npx skills add https://github.com/nashsu/llm_wiki_skill.git --skill llm_wiki_skill
```

安装后，智能体可通过与你本地运行的应用对话来回答如“我的 LLM Wiki 关于 X 说了什么”、“在我的知识库中搜索 Y”、“展示我 Wiki 图谱中 Z 节点的邻域”以及“重扫描我的 Wiki 来源”等提示词。默认只读模式，并引用 Wiki 页面路径以便你在应用内验证。

- **Skill 仓库**：<https://github.com/nashsu/llm_wiki_skill>
- **触发纪律**：它有意**不**在通用“搜索我的笔记” / “检查我的 Obsidian / Notion / Logseq”时触发 —— 仅当你明确命名 LLM Wiki / `my wiki` / `知识库` 时才激活。

## 项目结构（Project Structure）

```
my-wiki/
├── purpose.md              # Goals, key questions, research scope
├── schema.md               # Wiki structure rules, page types
├── raw/
│   ├── sources/            # Uploaded documents (immutable)
│   └── assets/             # Local images
├── wiki/
│   ├── index.md            # Content catalog
│   ├── log.md              # Operation history
│   ├── overview.md         # Global summary (auto-updated)
│   ├── entities/           # People, organizations, products
│   ├── concepts/           # Theories, methods, techniques
│   ├── sources/            # Source summaries
│   ├── queries/            # Saved chat answers + research
│   ├── synthesis/          # Cross-source analysis
│   └── comparisons/        # Side-by-side comparisons
├── .obsidian/              # Obsidian vault config (auto-generated)
└── .llm-wiki/              # App config, chat history, review items
```

## Star 历史（Star History）

<a href="https://www.star-history.com/?repos=nashsu%2Fllm_wiki&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=nashsu/llm_wiki&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=nashsu/llm_wiki&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=nashsu/llm_wiki&type=date&legend=top-left" />
 </picture>
</a>

## 开源协议（License）

本项目采用 **GNU General Public License v3.0** 许可 —— 详见 [LICENSE](LICENSE)。