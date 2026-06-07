# nature-skills
大家好，我是上海交通大学博士生袁一哲，目前主要从事医疗 AI 相关的研究与创业实践，计划落地浦东张江！有病理专病或者泛癌万人以上队列的朋友，正在创业的伙伴亦或者欣赏我的投资人等等可以添加我的个人微信，务必备注来意。感谢大家持续关注 nature-skill。如果你有任何需求，欢迎提交 issue；如果我们认为该需求有意义且可行，也会尽量推进实现。我们同样欢迎 PR，但请务必按照 README 后面说明的格式提交，以便我们更高效地审核与合并。
<table>
  <tr>
    <td align="center">
      <b>个人微信</b><br>
      <img width="400" alt="个人微信" src="https://github.com/user-attachments/assets/9e2931fb-748b-418e-97ab-0515d191633d" />
    </td>
    <td align="center">
      <b>个人介绍</b><br>
      <img width="400" alt="个人介绍" src="https://github.com/user-attachments/assets/ef355bb8-7189-49a1-bfe0-b1c7dcc7e04e" />
    </td>
  </tr>
</table>

---

## Installation

`nature-skills` 是一个以 `SKILL.md` 为核心的可复用指令包（Skill）仓库。
每个 `skills/nature-*` 目录是一个可安装单元。请复制整个文件夹，而不仅仅是 `SKILL.md`，因为许多技能依赖 `references/`、`static/`、静态资源、脚本或 README 上下文。当你手动安装技能时，`skills/_shared/` 目录（多个技能共用的支持内容）应保留在 `nature-*` 文件夹旁边。

### 1. Codex

**Codex 插件市场安装**

本仓库在 `plugins/nature-skills/` 提供了 Codex 插件打包文件，因此 Codex 用户可以直接从插件市场安装完整的 Nature Skills 套件，而无需手动复制每个技能文件夹。

CLI 安装：

```bash
codex plugin marketplace add https://github.com/Yuan1z0825/nature-skills --ref main
codex plugin add nature-skills@nature-skills
```

Codex 桌面版用户可将同一仓库添加为自定义插件市场：

- Marketplace 源地址：`https://github.com/Yuan1z0825/nature-skills.git`
- 分支/版本（Branch/ref）：`main`
- 插件名称：`nature-skills`

安装完成后，所有 `nature-*` 技能均可通过插件作为完整套件使用，同时包含较新路由型（router-style）技能所需的共享支持目录。如果技能未立即显示，请刷新插件页面或启动新的 Codex 会话。

**手动本地安装技能**

Codex 也可以直接使用这些文件夹作为本地技能。

**克隆仓库**

```bash
git clone https://github.com/Yuan1z0825/nature-skills.git
cd nature-skills
```

**安装单个技能**

```bash
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
cp -R skills/nature-reader ~/.codex/skills/
```

即使某些技能不使用 `_shared`，复制它也是无害的，这能避免 `nature-reader`、`nature-writing`、`nature-polishing` 和 `nature-paper2ppt` 等技能出现相对路径引用断裂的问题。

**安装所有当前技能**

```bash
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
for d in skills/nature-*; do
  cp -R "$d" ~/.codex/skills/
done
```

**拉取新更改后的更新方法**

```bash
git pull
cp -R skills/_shared ~/.codex/skills/
for d in skills/nature-*; do
  cp -R "$d" ~/.codex/skills/
done
```

**完成**

- 重启 Codex 以加载新添加的技能。
- 然后自然地进行提问，例如：`Translate this paper into a full markdown reader.` 或 `Make this paper into a Chinese journal-club PPT.`

如果你更倾向于不使用终端，也可以手动将 `skills/nature-*` 文件夹复制到 `~/.codex/skills/`；记得只需复制一次 `skills/_shared/`。如需详细操作指南，请参阅 [`install.md`](install.md)。

### 2. Claude Code

Claude Code 无法直接读取 Codex 技能文件夹。推荐在 Claude Code 中配置一个轻量级的子代理（subagent）或斜杠命令（slash-command）包装器，指向该仓库的稳定克隆版本，以便 `references/`、`static/`、静态资源、脚本和 `skills/_shared/` 等支持文件保持可用。

```bash
mkdir -p ~/ai-skills
cd ~/ai-skills
git clone https://github.com/Yuan1z0825/nature-skills.git
```

创建用户级子代理包装器：

```bash
mkdir -p ~/.claude/agents
cat > ~/.claude/agents/nature-reader.md <<'EOF'
---
name: nature-reader
description: Full-paper bilingual, figure-aware, source-grounded Markdown reader for journal or conference papers. Use proactively when the user asks to translate an entire paper or generate a complete markdown reader.
---

When invoked, first read `~/ai-skills/nature-skills/skills/nature-reader/SKILL.md`.
Treat that file as the governing workflow.
If the skill references supporting files, read only the specific files you need from
`~/ai-skills/nature-skills/skills/nature-reader/` and
`~/ai-skills/nature-skills/skills/_shared/`.
Do not replace the skill with a generic paper-summary response.
EOF
```

之后，启动新的 Claude Code 会话或打开 `/agents`，自然或显式地调用它：

```text
Use the nature-reader subagent to turn this PDF into a full markdown reader.
```

如果你更倾向于使用命令而非子代理，可以在 `.claude/commands/` 或 `~/.claude/commands/` 下创建项目级或用户级命令，指示 Claude Code 读取克隆仓库中的真实 `SKILL.md`。

官方 Claude Code 文档：

- [Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)

### 3. Other agents or manual use

如果你的代理支持可复用的提示词文件、系统提示词或代理配置文件，则最小可移植单元即为技能目录本身：

```text
skills/
├── _shared/              # keep this when a skill references ../_shared
└── nature-<topic>/
    ├── README.md
    ├── SKILL.md
    ├── manifest.yaml     # present for router-style skills
    ├── static/           # present for router-style skills
    └── references/...
```

在这种情况下：

1. 将整个技能目录复制到你的提示词库或项目中。
2. 保留 `SKILL.md`、`manifest.yaml`、`static/`、`references/`、脚本、静态资源以及任何所需的 `skills/_shared/` 文件。
3. 如有需要，调整 frontmatter 和正文以适配目标代理的原生格式。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Yuan1z0825/nature-skills&type=Date&cache_bust=2026-06-01T10)](https://star-history.com/#Yuan1z0825/nature-skills&Date)


## Skill index

| Skill | Status | Purpose | Trigger keywords |
|-------|--------|---------|-----------------|
| [`nature-figure`](skills/nature-figure/README.md) | Stable | Nature/high-impact Python or R figure workflow with bundled figures4papers demos | "Nature figure", "publication plot", "scientific figure", "figures4papers" |
| [`nature-polishing`](skills/nature-polishing/README.md) | Stable | Academic prose polishing to *Nature* style | "Nature style", "polish", "academic writing" |
| [`nature-writing`](skills/nature-writing/README.md) | Draft | Nature-style manuscript section drafting and argument restructuring | "Nature writing", "write abstract", "write introduction", "manuscript draft" |
| [`nature-reviewer`](skills/nature-reviewer/README.md) | Draft | Nature-style reviewer assessment with 3 referee reports and a cross-review synthesis | "Nature reviewer", "pre-submission review", "reviewer report", "peer-review critique", "审稿人视角评估" |
| [`nature-citation`](skills/nature-citation/README.md) | Beta | Strict Nature / CNS-family citation retrieval with ENW, RIS, and Zotero RDF export | "Nature citation", "CNS citation", "text citation", "supporting references", "Zotero RDF" |
| [`nature-data`](skills/nature-data/README.md) | Draft | Nature Data Availability statements, repository plans, and FAIR checks | "Data Availability", "repository", "FAIR metadata", "data availability statement" |
| [`nature-reader`](skills/nature-reader/README.md) | Beta | Full-paper bilingual Markdown reader with source anchors and figure grounding | "nature reader", "full markdown", "paper md", "原文对照", "图文对应", "全文翻译" |
| [`nature-response`](skills/nature-response/README.md) | Beta | Point-by-point reviewer response letters with comment triage, action mapping, and risk checks | "response to reviewers", "rebuttal letter", "major revision", "审稿意见回复" |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README.md) | Beta | Chinese PPTX decks from scientific papers | "paper PPT", "journal club", "paper to slides", "paper presentation" |
| [`nature-academic-search`](skills/nature-academic-search/README.md) | Beta | Multi-source literature search, citation verification, and reference management | "search papers", "find articles", "academic search", "literature search", "verify DOI" |

> **Adding a new skill?** Follow the [contribution guide](#adding-a-new-skill) at the bottom of this file.

---

## nature-figure

**What it does** — Generates multi-panel matplotlib figures that match *Nature* journal
visual standards: correct typography, semantic colour palette, editable SVG output,
and non-redundant panel information architecture.

**Example output gallery** — Five dense, simulated *Nature*-style result figures are
included in the [`nature-figure` gallery](skills/nature-figure/README.md#example-output-gallery):
material/mechanism, spatial imaging, in vivo efficacy, single-cell systems and
perturbation validation.

**Chart-type atlas** — The [`nature-figure` chart atlas](skills/nature-figure/README.md#chart-type-atlas)
classifies 10 supported chart families, including bar, line, heatmap, scatter/bubble,
radar/polar, distribution, forest/interval, area/stacked, image-plate and network/matrix
layouts.

| ![Material design and physical validation](skills/nature-figure/assets/gallery/fig1-material-mechanism-rich.png) | ![Spatial imaging and uptake](skills/nature-figure/assets/gallery/fig2-spatial-imaging-rich.png) | ![In vivo efficacy and tolerability](skills/nature-figure/assets/gallery/fig3-in-vivo-efficacy-rich.png) | ![Single-cell systems figure](skills/nature-figure/assets/gallery/fig4-single-cell-systems-rich.png) | ![Perturbation validation](skills/nature-figure/assets/gallery/fig5-validation-perturbation-rich.png) |
|---|---|---|---|---|

**Built from** — Production scripts from papers published in *Nature Machine Intelligence*
and top ML/bioinformatics venues ([figures4papers](https://github.com/ChenLiu-1996/figures4papers)).
The figures4papers demo scripts and preview assets are bundled inside
`skills/nature-figure/assets/figures4papers/`, with a routing guide at
`skills/nature-figure/references/demos.md`.

**Key rules enforced**

- Three mandatory rcParams must always appear first:
  ```python
  plt.rcParams['font.family'] = 'sans-serif'
  plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
  plt.rcParams['svg.fonttype'] = 'none'   # text stays as <text> nodes, not paths
  ```
- Primary output is always `.svg`; `.png` at 300 dpi is a secondary raster preview.
- Multi-panel figures follow a three-level information hierarchy: **overview → deviation → relationship**. No two panels may answer the same scientific question.

**Reference files**

```
skills/nature-figure/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
└── references/
    ├── api.md            PALETTE, helper signatures, validation rules
    ├── design-theory.md  Typography, layout, export policy, anti-redundancy rules
    ├── common-patterns.md Ultra-wide panels, legend axes, print-safe bars
    ├── tutorials.md      End-to-end walkthroughs (bars, trends, heatmaps)
    ├── chart-types.md    Radar, 3D sphere, scatter, fill_between, log-scale
    └── demos.md          Bundled figures4papers scripts and preview routing
```

**Supported chart types** — Stacked bar, grouped bar, horizontal ablation bar, trend/line,
sequential heatmap, diverging z-score heatmap, bubble scatter, radar/polar, 3D sphere
illustration, fill-between area, log-scale bar, GridSpec multi-panel.

---

## nature-polishing

**What it does** — Transforms academic draft text (including Chinese → English translation)
into prose matching *Nature* journal conventions: ≤ 30-word sentences, section-aware
tense and hedging, precise vocabulary, correct citation practice, and British English.

**Built from** — A graduate-level scientific English writing course, Academic Phrasebank,
and close reading of curated *Nature* and *Nature Communications* research articles
across materials, energy systems, construction decarbonization and machine learning.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Sentence length | Every sentence ≤ 30 words; count individually; last sentence most likely to fail |
| Hedging calibration | Match claim strength to evidence: *demonstrate* → *suggest* → *may reflect* |
| Section tense | Results = past tense + quantitative detail; Discussion = hedging + mechanism |
| Citation integrity | Cite only sources personally read and verified; four attribution types |
| Overclaim detection | Flag absolutes, unwarranted causation, scope expansion, unverified "first" claims |
| British English | signalling, colour, analyse, programme, modelling, behaviour |

**12-step polishing workflow**

Sentence split → Section ID → Hourglass check → Tense audit → Sentence edit →
Vocabulary upgrade → Template check → Citation audit → House style → Overclaim →
Proofreading → Plain-text output

**Reference files**

```
skills/nature-polishing/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
└── references/
    ├── latex-layout.md
    ├── published-article-patterns.md
    ├── phrasebank-playbook.md
    ├── section-moves.md
    ├── style-guardrails.md
    └── writing-strategy.md
```

---

## nature-writing

**What it does** — Drafts or rebuilds manuscript sections from author-provided
claims, results, figures, notes, or Chinese drafts. It is for argument construction:
abstracts, introductions, Results narratives, Discussions, Conclusions, titles and
full manuscript outlines, method sections, experiment sections and reviewer-facing
self-review.

**Built from** — Close reading of curated *Nature* and *Nature Communications*
articles, especially how published papers move from field-scale stakes to a narrow
gap, then to evidence, interpretation and bounded implication. It also integrates
open research-writing notes for paragraph flow, section logic and adversarial
paper review.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Evidence first | Do not invent data, mechanisms, references, statistics, novelty or limitations |
| Abstract | Context/problem → gap → approach → key result → implication → boundary |
| Introduction | Field scale → bottleneck → prior attempts → unresolved gap → present study |
| Method | Module motivation → module design → forward process → technical advantage |
| Results | Build an evidence ladder, not a chronological lab diary |
| Experiments | Tie claims to baselines, ablations, metrics, stress tests and readable tables |
| Discussion | Explain meaning, relation to prior work, constraints and future use |
| Review | Run claim-evidence and rejection-risk checks before submission |
| Chinese notes | Translate intent and argument, not clause order |

**Reference files**

```
skills/nature-writing/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
├── agents/
│   └── openai.yaml
└── references/
    ├── abstract.md
    ├── article-architecture.md
    ├── chinese-author-workflow.md
    ├── conclusion.md
    ├── experiments.md
    ├── introduction.md
    ├── method.md
    ├── paper-review.md
    ├── paragraph-flow.md
    ├── related-work.md
    └── examples/
```

---

## nature-reviewer

**What it does** — Simulates a Nature-style pre-submission reviewer assessment
from the referee perspective. It returns three reviewer reports plus a
cross-review synthesis, focusing on novelty, significance, technical soundness,
presentation, and likely editorial risk.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Reviewer role | Assess as external referees, not as an author rebuttal writer |
| Evidence grounding | Use only the manuscript/material supplied by the user and the local reviewer source basis |
| Multi-reviewer output | Produce three distinct reviewer reports plus a synthesis |
| Editorial relevance | Separate novelty, significance, technical confidence, presentation, and decision risk |
| Boundaries | Do not invent experiments, citations, journal policy, or manuscript content |

**Reference files**

```text
skills/nature-reviewer/
├── README.md
├── SKILL.md
└── references/
    ├── source-basis.md
    ├── reviewer-workflow.md
    ├── review-axes.md
    ├── report-structure.md
    ├── role-boundaries.md
    └── qa-checklist.md
```

---

## nature-citation

**What it does** — Converts manuscript text or standalone claims into strict Nature / CNS-family
citation candidates, then exports one reference-manager-ready file in `ENW`, `RIS`, or Zotero
`RDF`. It can also generate an HTML screening page for year filtering, citation selection, and
format-specific download.

**Built from** — Crossref metadata retrieval, DOI record export, and journal-family filtering logic
for Nature Portfolio, the AAAS Science family, and Cell Press.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Scope filtering | Restrict to Nature Portfolio, Science family, Cell Press, or flagship-only journals |
| Segmentation | Split long text into citable claim units with stable segment IDs |
| Search discipline | Translate Chinese claims into English scientific concepts; prefer precision over volume |
| Support grading | Distinguish strong, partial, background, limiting, and metadata-only support |
| Export integrity | Do not fabricate DOI, pages, volume, issue, or journal metadata |
| Download options | Support one-file export in `ENW`, `RIS`, or Zotero `RDF` |

**Reference files**

```text
skills/nature-citation/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
├── references/
│   ├── journal-scope.md
│   ├── ris-endnote.md
│   ├── script-usage.md
│   └── search-strategy.md
└── scripts/
    └── nature_citation.py
```

**Example workflow** — Segment a paragraph, search in-scope citations, review candidates in the
HTML browser, then download only the selected records as `ENW`, `RIS`, or Zotero `RDF`.

---

## nature-data

**What it does** — Prepares and audits Data Availability statements, repository plans,
dataset citations, and FAIR metadata checks for Nature-family and Springer Nature
submissions. It is bilingual-aware: Chinese author notes such as "data availability statement",
"request from corresponding author", "raw data", "restricted data", and "public database" are converted into precise
submission-ready English with Chinese action notes.

**Built from** — Springer Nature research data policy, Nature Portfolio reporting standards,
Scientific Data repository and citation practice, the FAIR Guiding Principles, and DataCite
metadata conventions.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Data Availability | Map every result-supporting dataset to a durable access route |
| Repository strategy | Prefer mandated or discipline-specific repositories with persistent identifiers |
| Restricted data | State the restriction reason, controller, review route, and access conditions |
| Dataset citations | Cite public datasets with DataCite-style creator, title, repository, year, and identifier metadata |
| FAIR metadata | Check identifiers, licence, README/data dictionary, provenance, version, and reuse conditions |
| Chinese alignment | Translate intent rather than literal wording; flag vague "reasonable request" phrasing |

**Reference files**

```
skills/nature-data/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
├── agents/
│   └── openai.yaml
└── references/
    ├── chinese-author-alignment.md
    ├── fair-metadata-checklist.md
    ├── policy-principles.md
    ├── repository-and-identifiers.md
    ├── source-basis.md
    └── statement-patterns.md
```

---

## nature-response

**What it does** — Drafts, audits, and revises point-by-point reviewer response
letters for Nature-family and high-impact journal manuscript revisions. It treats the
response letter as an editor-facing verification document: every reviewer concern is assigned
a stable ID, classified, mapped to an action, and tied to manuscript evidence, a revision
location, or an unresolved author-input flag.

**Built from** — Nature editorial process guidance, Nature-family revision-package
instructions, Springer Nature rebuttal advice, and transparent peer-review considerations.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Completeness | Every reviewer comment receives an ID and a response, cross-reference, or unresolved flag |
| Action mapping | Each reply maps to a concrete manuscript action such as `ACCEPT_TEXT`, `ACCEPT_ANALYSIS`, `SOFTEN_CLAIM`, or `AUTHOR_INPUT_NEEDED` |
| Traceability | Claimed changes must cite a section, page, line, figure, table, supplement, citation, or visible placeholder |
| Factuality | Do not invent experiments, analyses, citations, line numbers, figure panels, editor instructions, or manuscript changes |
| Tone | Use cooperative, evidence-forward language; disagree only with scientific or scope-based reasoning |
| Chinese alignment | Convert Chinese author notes into English response prose plus Chinese confirmation items when needed |

**Reference files**

```
skills/nature-response/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
├── references/
│   ├── action-mapping.md
│   ├── chinese-author-alignment.md
│   ├── comment-taxonomy.md
│   ├── difficult-cases.md
│   ├── intake-and-routing.md
│   ├── qa-checklist.md
│   ├── response-structure.md
│   ├── source-basis.md
│   └── tone-and-stance.md
├── tests/
    ├── conflicting-reviewers.md
    ├── defensive-draft-audit.md
    ├── evaluation-summary.md
    ├── impossible-experiment.md
    ├── major-revision-missing-evidence.md
    ├── minor-revision.md
    └── rubric.md
└── examples/
    ├── conflicting-reviewers.md
    ├── major-revision-with-missing-evidence.md
    └── minor-revision.md
```

---

## nature-paper2ppt

**What it does** — Turns a scientific paper, preprint, PDF, article text, abstract,
figure legends, or reading notes into a concise Chinese `.pptx` presentation for journal
club, group meeting, lab meeting, paper sharing, or thesis seminar.

The skill identifies the paper type and central argument, selects only figures and tables
that support the evidence chain, writes Chinese slide titles, bullets, captions, takeaways
and speaker notes, creates the actual PPTX deck, and runs lightweight package QA.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Narrative | Use the paper's scientific argument as the slide spine, not the manuscript section order |
| Paper type | Classify the paper before choosing claim-first, problem-to-solution, workflow-to-validation, or evidence-map logic |
| Figures | Use figures as evidence; crop or split dense panels rather than shrinking them into unreadable slots |
| Output | Build a real `.pptx` as the primary deliverable, with Chinese text and speaker notes |
| QA | Reopen or inspect the PPTX package, record slide count, embedded media, notes, and any rendering limits |
| Integrity | Do not fabricate results, methods, numbers, datasets, mechanisms, or figure details |

**Reference files**

```
skills/nature-paper2ppt/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
└── references/
    ├── design-and-layout.md
    ├── figure-assets.md
    └── self-review.md
```

---

## nature-academic-search

**What it does** — Provides a multi-source academic search and reference-management
workflow backed by a local MCP server. It searches PubMed, CrossRef and arXiv in
parallel, fetches records by DOI, PMID or arXiv ID, formats citations, looks up MeSH
terms, verifies bibliographic identifiers, and supports `.nbib`, `.ris`, `.bib` and
`.enw` reference-file workflows.

**Built from** — A unified MCP server with source adapters for PubMed E-utilities,
CrossRef REST metadata and arXiv Atom metadata, plus reusable workflow notes for
source-tier routing, search strategy, citation parsing, deduplication, RIS/BibTeX
field mapping and reference-file conversion.

**Setup note** — For Claude Code MCP use, run
`bash skills/nature-academic-search/install.sh your-email@example.com`, restart Claude Code,
and optionally set `NCBI_API_KEY` for higher PubMed rate limits. For plain prompt use,
copy the whole `skills/nature-academic-search/` directory like the other skills.

**Key rules enforced**

| Domain | Core rule |
|--------|-----------|
| Source routing | Start with structured API-backed sources: PubMed for biomedical searches, CrossRef for DOI and cross-disciplinary metadata, and arXiv for preprints |
| Fallback discipline | Escalate from T1 sources to limited APIs or scraped/manual sources only when needed, and warn when results may be incomplete |
| Deduplication | Merge multi-source hits by DOI, PMID, arXiv ID and normalized title rather than counting duplicate records as separate evidence |
| Citation verification | Resolve DOI, PMID and arXiv IDs before citation formatting; expose missing or failed metadata instead of filling fields by guesswork |
| MeSH strategy | Use MeSH lookup for biomedical PubMed queries when the task needs recall, controlled vocabulary or systematic search structure |
| File integrity | Preserve bibliographic fields when converting `.nbib`, `.ris`, `.bib` and `.enw`; do not fabricate volume, issue, pages, DOI or PMID values |

**MCP tools**

| Tool | Purpose |
|------|---------|
| `search_papers` | Search CrossRef, PubMed and arXiv with optional source selection and per-source result limits |
| `get_paper_by_id` | Fetch paper metadata by DOI, PMID or arXiv ID with automatic ID-type detection |
| `get_citation` | Generate formatted citations in styles such as APA, Nature, IEEE, Vancouver, Chicago and MLA |
| `lookup_mesh` | Query PubMed MeSH descriptors for biomedical search-term expansion |

**Reference files**

```text
skills/nature-academic-search/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
├── install.sh
├── config/
│   ├── mcp-snippet.json
│   ├── settings-snippet.json
│   └── triggers-academic-search.toml
├── mcp-server/
│   ├── academic_search_server.py
│   ├── sources/
│   ├── tests/
│   └── utils/
├── references/
│   ├── citation-parser.md
│   ├── dedup-engine.md
│   ├── ris-bibtex-format.md
│   ├── search-strategy.md
│   ├── source-tiers.md
│   └── workflows/
└── scripts/
    ├── converters.py
    ├── format-converter.py
    └── preflight.py
```

**Example workflow** — Search the same topic across PubMed, CrossRef and arXiv, merge
and deduplicate candidate papers, verify key identifiers, look up MeSH terms for the
biomedical subset, then export or convert the selected references for Zotero, EndNote
or BibTeX.

---

## Shared design principles

All skills in this collection adhere to the following:

1. **Primary sources only** — rules are grounded in published *Nature* content or official
   journal guidelines, not general style preference.
2. **Explicit over implicit** — every rule is stated with a rationale, not just asserted.
3. **Section-aware** — academic writing and figures both require context-sensitivity;
   each skill applies different logic depending on which part of a paper is being handled.
4. **Output-first** — every skill returns something immediately usable: copy-paste prose,
   a `.svg` file, a `.pptx` deck, or a concrete recommendation. No intermediate planning documents.
5. **Extensible by design** — each skill is self-contained in its own directory; adding a
   new skill requires no changes to existing ones.

---

## Adding a new skill

To add a skill to this collection:

**1. Create a directory**
```
skills/nature-<topic>/
```

**2. Minimum required files**

| File | Required | Purpose |
|------|----------|---------|
| `SKILL.md` | Yes | Frontmatter (`name`, `description`) + rules + workflow; loaded by the agent after triggering |
| `README.md` | Yes | Human-readable reference in full English |
| `references/*.md` | Recommended for complex skills | Modular rule files (api, design theory, tutorials, chart types, …) |

**3. SKILL.md frontmatter template**
```yaml
---
name: nature-<topic>
description: >-
  One-sentence description of what the skill does and when to trigger it.
  Include the output format and the primary use case.
---
```

**4. Update this index**

Add a row to the [Skill index](#skill-index) table above:
```markdown
| [`nature-<topic>`](skills/nature-<topic>/README.md) | Draft / Stable | One-line purpose | trigger keywords |
```

**5. Status labels**

| Label | Meaning |
|-------|---------|
| `Draft` | Rules defined; not yet tested on real examples |
| `Beta` | Tested on examples; edge cases may remain |
| `Stable` | Validated on real academic content; rules are settled |

---

## Candidate skills (not yet built)

The following are documented gaps. Contributions welcome.

| Candidate | Scope | Priority |
|-----------|-------|----------|
| `nature-stats` | Statistical reporting conventions for *Nature* (effect sizes, confidence intervals, p-value formatting, sample size statements) | High |
| `nature-methods` | Deep-dive Methods writing assistant — reproducibility checklist, forbidden phrases, ethical approval templates, supplementary organisation | Medium |
| `nature-cover` | Cover letter drafting — hook paragraph, significance framing, fit-to-journal argument, ≤ 500-word limit | Medium |


## ☕ 如果内容对你有帮助，欢迎随缘支持一下

---

<div align="center">

| 微信赞赏 | 来自粉丝的小感动 |
| --- | --- |
| <img width="320" alt="微信赞赏" src="https://github.com/user-attachments/assets/83c101e7-2370-46e9-a840-cb506df98cf4" /> | <img width="320" alt="粉丝的鼓励" src="https://github.com/user-attachments/assets/0484300a-95e8-4cb3-ad73-478ba9bd19d6" /> |

</div>

### 💬 想说的话
 
项目会长期免费维护，大家正常使用就好。  
很多朋友还是学生党，所以完全不需要有任何“必须打赏”的压力。

如果这些内容刚好帮你节省了一些时间、解决了一点问题，  
又恰好想请作者喝杯咖啡，那我会非常开心 ☕  

你的支持会用于：

- 持续更新内容
- 服务器与工具费用
- 熬夜写文档时的续命奶茶（认真）

无论是否赞赏，都非常感谢你的关注与支持 ❤️