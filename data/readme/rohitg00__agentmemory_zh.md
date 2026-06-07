<p align="center">
  <img src="assets/banner.png" alt="agentmemory — Persistent memory for AI coding agents" width="720" />
</p>

<p align="center">
  <strong>
    你的编程代理能记住一切。无需反复解释。
    基于 <a href="https://github.com/iii-hq/iii">iii engine</a> 构建
  </strong><br/>
  面向 Claude Code、GitHub Copilot CLI、Cursor、Gemini CLI、Codex CLI、Hermes、OpenClaw、pi、OpenCode 以及任何 MCP 客户端的持久化记忆。
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="READMEs/README.zh-CN.md">简体中文</a> |
  <a href="READMEs/README.zh-TW.md">繁體中文</a> |
  <a href="READMEs/README.ja-JP.md">日本語</a> |
  <a href="READMEs/README.ko-KR.md">한국어</a> |
  <a href="READMEs/README.es-ES.md">Español</a> |
  <a href="READMEs/README.tr-TR.md">Türkçe</a> |
  <a href="READMEs/README.ru-RU.md">Русский</a> |
  <a href="READMEs/README.hi-IN.md">हिन्दी</a> |
  <a href="READMEs/README.pt-BR.md">Português</a> |
  <a href="READMEs/README.fr-FR.md">Français</a> |
  <a href="READMEs/README.de-DE.md">Deutsch</a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/25123" target="_blank"><img src="https://trendshift.io/api/badge/repositories/25123" alt="rohitg00/agentmemory | Trendshift" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="https://www.star-history.com/?repos=rohitg00%2Fagentmemory&type=date&legend=top-left">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=rohitg00/agentmemory&type=date&theme=dark&legend=top-left" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=rohitg00/agentmemory&type=date&legend=top-left" />
      <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=rohitg00/agentmemory&type=date&legend=top-left" />
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2"><img src="https://img.shields.io/badge/Viral%20GitHub%20Gist-1.3k%20stars%20%2F%20182%20forks-FF6B35?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a1a" alt="Design doc: 1.3k stars / 182 forks on the gist" /></a>
</p>

<p align="center">
  <em>该 Gist 扩展了 Karpathy 的 LLM Wiki 模式，增加了置信度评分、生命周期管理、知识图谱和混合搜索功能：agentmemory 即为该模式的实现。</em>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@agentmemory/agentmemory"><img src="https://img.shields.io/npm/v/@agentmemory/agentmemory?color=CB3837&label=npm&style=for-the-badge&logo=npm" alt="npm version" /></a>
  <a href="https://www.npmjs.com/package/@agentmemory/agentmemory"><img src="https://img.shields.io/npm/dm/@agentmemory/agentmemory?color=CB3837&label=downloads&style=for-the-badge&logo=npm" alt="npm downloads" /></a>
  <a href="https://github.com/rohitg00/agentmemory/actions"><img src="https://img.shields.io/github/actions/workflow/status/rohitg00/agentmemory/ci.yml?label=tests&style=for-the-badge&logo=github" alt="CI" /></a>
  <a href="https://github.com/rohitg00/agentmemory/blob/main/LICENSE"><img src="https://img.shields.io/github/license/rohitg00/agentmemory?color=blue&style=for-the-badge" alt="License" /></a>
  <a href="https://github.com/rohitg00/agentmemory/stargazers"><img src="https://img.shields.io/github/stars/rohitg00/agentmemory?style=for-the-badge&color=yellow&logo=github" alt="Stars" /></a>
</p>

<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/stat-recall.svg"><img src="assets/tags/stat-recall.svg" alt="95.2% retrieval R@5" height="38" /></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/stat-tokens.svg"><img src="assets/tags/stat-tokens.svg" alt="92% fewer tokens" height="38" /></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/stat-tools.svg"><img src="assets/tags/stat-tools.svg" alt="53 MCP tools" height="38" /></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/stat-hooks.svg"><img src="assets/tags/stat-hooks.svg" alt="12 auto hooks" height="38" /></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/stat-deps.svg"><img src="assets/tags/stat-deps.svg" alt="0 external DBs" height="38" /></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/stat-tests.svg"><img src="assets/tags/stat-tests.svg" alt="1,390+ tests passing" height="38" /></picture>
</p>

<p align="center">
  <img src="assets/demo.gif" alt="agentmemory demo" width="720" />
</p>

<p align="center">
  <a href="#install">安装</a> &bull;
  <a href="#quick-start">快速开始</a> &bull;
  <a href="#benchmarks">基准测试</a> &bull;
  <a href="#vs-competitors">竞品对比</a> &bull;
  <a href="#works-with-every-agent">代理支持</a> &bull;
  <a href="#how-it-works">工作原理</a> &bull;
  <a href="#mcp-server">MCP</a> &bull;
  <a href="#real-time-viewer">实时查看器</a> &bull;
  <a href="#iii-console">iii Console</a> &bull;
  <a href="#powered-by-iii">由 iii 驱动</a> &bull;
  <a href="#configuration">配置</a> &bull;
  <a href="#api">API</a>
</p>

---

## 安装

```bash
npm install -g @agentmemory/agentmemory          # 一次性安装 — PATH 上即可使用裸命令 `agentmemory`
# 如果在 macOS/Linux 系统 Node 安装时遇到 EACCES 错误，请重试：
# sudo npm install -g @agentmemory/agentmemory
agentmemory                                      # 在 :3111 启动记忆服务器
agentmemory demo                                 # 填充示例会话数据并演示检索能力
agentmemory connect claude-code                  # 将 MCP 接入你的代理（也支持：copilot-cli, codex, cursor, gemini-cli...）
npx skills add rohitg00/agentmemory -y           # 安装 8 个原生技能，让你的代理知道何时使用这些工具
```

或通过 `npx` 运行（无需全局安装）：

```bash
npx @agentmemory/agentmemory
```

注意 — npx 会针对每个版本进行缓存。如果你发现裸命令 `npx @agentmemory/agentmemory` 返回的是旧版本，请使用 `npx -y @agentmemory/agentmemory@latest` 强制获取最新版本，或者使用 `rm -rf ~/.npm/_npx`（macOS/Linux；Windows 请删除 `%LOCALAPPDATA%\npm-cache\_npx`）清除一次缓存。从 v0.9.16+ 开始，首次运行 npx 会提示你全局安装以便后续在任何地方都能直接使用裸命令 `agentmemory`。

完整选项见下方的 [快速开始](#quick-start)。特定代理的配置见 [Works with every agent](#works-with-every-agent)。

---

<h2 id="works-with-every-agent"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-agents.svg"><img src="assets/tags/section-agents.svg" alt="Works with every agent" height="32" /></picture></h2>

agentmemory 支持与任何具备 hooks、MCP 或 REST API 的代理配合使用。所有代理共享同一个记忆服务器。

<table>
<tr>
<td align="center" width="12.5%">
<a href="https://claude.com/product/claude-code"><img src="https://github.com/anthropics.png?size=120" alt="Claude Code" width="48" height="48" /></a><br/>
<strong>Claude Code</strong><br/>
<sub>原生插件 + 12个钩子 + MCP</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/openai/codex"><img src="https://github.com/openai.png?size=120" alt="Codex CLI" width="48" height="48" /></a><br/>
<strong>Codex CLI</strong><br/>
<sub>原生插件 + 6个钩子 + MCP</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/features/copilot"><img src="https://github.githubassets.com/images/modules/site/copilot/copilot.png" alt="GitHub Copilot CLI" width="48" height="48" /></a><br/>
<strong>GitHub Copilot CLI</strong><br/>
<sub>MCP + 插件钩子/技能</sub>
</td>
<td align="center" width="12.5%">
<a href="integrations/openclaw/"><img src="https://github.com/openclaw.png?size=120" alt="OpenClaw" width="48" height="48" /></a><br/>
<strong>OpenClaw</strong><br/>
<sub>原生插件 + MCP</sub>
</td>
<td align="center" width="12.5%">
<a href="integrations/hermes/"><img src="https://github.com/NousResearch.png?size=120" alt="Hermes" width="48" height="48" /></a><br/>
<strong>Hermes</strong><br/>
<sub>原生插件 + MCP</sub>
</td>
<td align="center" width="12.5%">
<a href="integrations/pi/"><img src="assets/agents/pi.svg" alt="pi" width="48" height="48" /></a><br/>
<strong>pi</strong><br/>
<sub>原生插件 + MCP</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/tinyhumansai/openhuman"><img src="https://raw.githubusercontent.com/tinyhumansai/openhuman/main/app/src-tauri/icons/128x128.png" alt="OpenHuman" width="48" height="48" /></a><br/>
<strong>OpenHuman</strong><br/>
<sub>原生 Memory trait 后端</sub>
</td>
<td align="center" width="12.5%">
<a href="https://cursor.com"><picture><source media="(prefers-color-scheme: dark)" srcset="https://svgl.app/library/cursor_dark.svg"><img src="https://svgl.app/library/cursor_light.svg" alt="Cursor" width="48" height="48" /></picture></a><br/>
<strong>Cursor</strong><br/>
<sub>MCP 服务器</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/google-gemini/gemini-cli"><img src="https://github.com/google-gemini.png?size=120" alt="Gemini CLI" width="48" height="48" /></a><br/>
<strong>Gemini CLI</strong><br/>
<sub>MCP 服务器</sub>
</td>
</tr>
<tr>
<td align="center" width="12.5%">
<a href="https://github.com/opencode-ai/opencode"><picture><source media="(prefers-color-scheme: dark)" srcset="https://svgl.app/library/opencode-dark.svg"><img src="https://svgl.app/library/opencode.svg" alt="OpenCode" width="48" height="48" /></picture></a><br/>
<strong>OpenCode</strong><br/>
<sub>22个钩子 + MCP + 插件</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/cline/cline"><img src="https://github.com/cline.png?size=120" alt="Cline" width="48" height="48" /></a><br/>
<strong>Cline</strong><br/>
<sub>MCP 服务器</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/block/goose"><img src="https://github.com/block.png?size=120" alt="Goose" width="48" height="48" /></a><br/>
<strong>Goose</strong><br/>
<sub>MCP 服务器</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/Kilo-Org/kilocode"><img src="https://github.com/Kilo-Org.png?size=120" alt="Kilo Code" width="48" height="48" /></a><br/>
<strong>Kilo Code</strong><br/>
<sub>MCP 服务器</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/Aider-AI/aider"><img src="https://github.com/Aider-AI.png?size=120" alt="Aider" width="48" height="48" /></a><br/>
<strong>Aider</strong><br/>
<sub>REST API</sub>
</td>
<td align="center" width="12.5%">
<a href="https://claude.ai/download"><img src="https://github.com/anthropics.png?size=120" alt="Claude Desktop" width="48" height="48" /></a><br/>
<strong>Claude Desktop</strong><br/>
<sub>MCP 服务器</sub>
</td>
<td align="center" width="12.5%">
<a href="https://windsurf.com"><picture><source media="(prefers-color-scheme: dark)" srcset="https://svgl.app/library/windsurf-dark.svg"><img src="https://svgl.app/library/windsurf-light.svg" alt="Windsurf" width="48" height="48" /></picture></a><br/>
<strong>Windsurf</strong><br/>
<sub>MCP 服务器</sub>
</td>
<td align="center" width="12.5%">
<a href="https://github.com/RooCodeInc/Roo-Code"><img src="https://github.com/RooCodeInc.png?size=120" alt="Roo Code" width="48" height="48" /></a><br/>
<strong>Roo Code</strong><br/>
<sub>MCP 服务器</sub>
</td>
</tr>
<tr>
<td align="center" width="12.5%">
<a href="https://www.warp.dev"><img src="https://github.com/warpdotdev.png?size=120" alt="Warp" width="48" height="48" /></a><br/>
<strong>Warp</strong><br/>
<sub>connect + MCP + 技能</sub>
</td>
</tr>
</table>

<p align="center">
  <sub>支持所有使用 **MCP** 或 **HTTP** 的代理。一个服务器，跨代理共享记忆。</sub>
</p>

---

你每次会话都在重复解释同样的架构。你在重新发现同样的 Bug。你在重新教导同样的偏好。内置记忆（CLAUDE.md、.cursorrules）限制在 200 行以内且容易过时。agentmemory 解决了这个问题。它会在后台静默捕获代理所做的操作，将其压缩为可搜索的记忆，并在下次会话开始时注入正确的上下文。只需一条命令。跨代理通用。

**发生了什么改变：** 在第 1 个会话中你设置了 JWT 认证。在第 2 个会话中你需要添加速率限制。此时代理已经知道你的认证使用了 `src/middleware/auth.ts` 中的 jose 中间件，测试覆盖了令牌验证，且你为了 Edge 兼容性选择了 jose 而非 jsonwebtoken。无需反复解释，无需复制粘贴。代理就是 *知道*。

```bash
npx @agentmemory/agentmemory
```

> **v0.9.26 新增** — 热修复：针对缺失索引清单时的首次启动崩溃（[#797](https://github.com/rohitg00/agentmemory/issues/797)），现在改为自我修复而非在 `manifest.v` 上抛出异常。
>
> **v0.9.25** — 修复了十一个破坏性回归问题（跨提供商回退 404、iii-sdk 0.11.2 中的 `triggerVoid` 移除、Markdown 围栏内的 XML 摘要、pi 的 `tool_input/tool_output` 字段不匹配、查看器在 11k+ 节点时的 500 错误、`Promise.all` 下的 agent-sdk 递归保护竞态条件、obsidian-export 缺失 ID 崩溃、iii 运行时自动回退固定版本、import-jsonl 旧会话重新键）。新增：分片 BM25/向量索引持久化及清单提交/回滚（[@Rokurolize](https://github.com/Rokurolize) [#762](https://github.com/rohitg00/agentmemory/issues/762)），智能搜索跟进率诊断（[#771](https://github.com/rohitg00/agentmemory/issues/771））。即插即用升级，无破坏性更改。完整说明见 [CHANGELOG.md](CHANGELOG.md)。

---

<h2 id="benchmarks"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-benchmarks.svg"><img src="assets/tags/section-benchmarks.svg" alt="Benchmarks" height="32" /></picture></h2>

<table>
<tr>
<td width="50%">

### 检索准确率

**coding-agent-life-v1**（内部语料库，沙盒可复现）

| Adapter | P@5 | R@5 | Top-5 hit rate | p50 latency |
|---|---|---|---|---|
| **agentmemory hybrid** | **0.240** | **1.000** | **15 / 15** | 14 ms |
| grep baseline | 0.227 | 0.967 | 15 / 15 | 0 ms |

在此语料库中达到了 **P@5 数学上限**（0.240，见评分卡）的 Top-5 命中率。Hybrid 检索到了所有黄金会话；grep 在多会话时间查询中有 1/2 个黄金样本未命中。提升在于 **召回率 + 时序性**，而非聚合精度 — 该基准测试规模较小且黄金样本稀疏，下方的 LongMemEval-S 区分度更好。完整的按类型细分及修正说明：[`docs/benchmarks/2026-05-20-coding-agent-life-v1.md`](docs/benchmarks/2026-05-20-coding-agent-life-v1.md)。

**LongMemEval-S**（ICLR 2025，500个问题）

| System | R@5 | R@10 | MRR |
|---|---|---|---|
| **agentmemory** | **95.2%** | **98.6%** | **88.2%** |
| BM25-only fallback | 86.2% | 94.6% | 71.5% |

</td>
<td width="50%">

### Token 节省量

| Approach | Tokens/yr | Cost/yr |
|---|---|---|
| Paste full context | 19.5M+ | Impossible (exceeds window) |
| LLM-summarized | ~650K | ~$500 |
| **agentmemory** | **~170K** | **~$10** |
| agentmemory + local embeddings | ~170K | **$0** |

</td>
</tr>
</table>

> 嵌入模型：`all-MiniLM-L6-v2`（本地、免费、无需 API Key）。完整报告：[`benchmark/LONGMEMEVAL.md`](benchmark/LONGMEMEVAL.md), [`benchmark/QUALITY.md`](benchmark/QUALITY.md), [`benchmark/SCALE.md`](benchmark/SCALE.md)。竞品对比：[`benchmark/COMPARISON.md`](benchmark/COMPARISON.md) — agentmemory vs mem0, Letta, Khoj, claude-mem, Hippo。

**本地复现：** [`eval/README.md`](eval/README.md) — 针对 LongMemEval `_s`（公开 500题）+ `coding-agent-life-v1`（内部 15会话语料库）的适配器可插拔测试框架。Grep / vector / agentmemory 适配器并排评分，NDJSON 输出，发布的评分卡位于 [`docs/benchmarks/`](docs/benchmarks/)。

**配合 [codegraph](https://github.com/colbymchenry/codegraph), [Understand Anything](https://github.com/Lum1104/Understand-Anything) 和 [Graphify](https://github.com/safishamsi/graphify) 使用。** 代码图索引、多代理构建流水线以及跨文档/PDF/图片/视频的更广泛知识图谱。agentmemory 记住工作内容；这三个项目点亮其余的上下文层。配方 + 问题路由表：[`docs/recipes/pairings.md`](docs/recipes/pairings.md)。

---

<h2 id="vs-competitors"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-competitors.svg"><img src="assets/tags/section-competitors.svg" alt="vs Competitors" height="32" /></picture></h2>

<table>
<tr>
<th width="20%"></th>
<th width="20%">agentmemory</th>
<th width="20%">mem0 (53K ⭐)</th>
<th width="20%">Letta / MemGPT (22K ⭐)</th>
<th width="20%">Built-in (CLAUDE.md)</th>
</tr>
<tr>
<td><strong>Type</strong></td>
<td>记忆引擎 + MCP 服务器</td>
<td>记忆层 API</td>
<td>完整代理运行时</td>
<td>静态文件</td>
</tr>
<tr>
<td><strong>Retrieval R@5</strong></td>
<td><strong>95.2%</strong></td>
<td>68.5% (LoCoMo)</td>
<td>83.2% (LoCoMo)</td>
<td>N/A (grep)</td>
</tr>
<tr>
<td><strong>Auto-capture</strong></td>
<td>12个钩子（零手动操作）</td>
<td>手动 <code>add()</code> 调用</td>
<td>代理自我编辑</td>
<td>手动编辑</td>
</tr>
<tr>
<td><strong>Search</strong></td>
<td>BM25 + Vector + Graph (RRF融合)</td>
<td>Vector + Graph</td>
<td>Vector (归档)</td>
<td>将所有内容加载到上下文中</td>
</tr>
<tr>
<td><strong>Multi-agent</strong></td>
<td>MCP + REST + 租约(leases) + 信号(signals)</td>
<td>API（无协调机制）</td>
<td>仅限 Letta 运行时内部</td>
<td>每个代理独立文件</td>
</tr>
<tr>
<td><strong>Framework lock-in</strong></td>
<td>无（任何 MCP 客户端均可）</td>
<td>无</td>
<td>高（必须使用 Letta）</td>
<td>每代理格式</td>
</tr>
<tr>
<td><strong>External deps</strong></td>
<td>无 (SQLite + iii-engine)</td>
<td>Qdrant / pgvector</td>
<td>Postgres + vector DB</td>
<td>无</td>
</tr>
<tr>
<td><strong>Memory lifecycle</strong></td>
<td>4级整合 + 衰减 + 自动遗忘</td>
<td>被动提取</td>
<td>代理管理</td>
<td>手动修剪</td>
</tr>
<tr>
<td><strong>Token efficiency</strong></td>
<td>~1,900 tokens/会话 ($10/年)</td>
<td>因集成而异</td>
<td>核心记忆在上下文中</td>
<td>240个观测值下 22K+ tokens</td>
</tr>
<tr>
<td><strong>Real-time viewer</strong></td>
<td>有 (端口 3113)</td>
<td>云端仪表板</td>
<td>云端仪表板</td>
<td>无</td>
</tr>
<tr>
<td><strong>Self-hosted</strong></td>
<td>是（默认）</td>
<td>可选</td>
<td>可选</td>
<td>是</td>
</tr>
</table>

---

<h2 id="quick-start"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-quickstart.svg"><img src="assets/tags/section-quickstart.svg" alt="Quick Start" height="32" /></picture></h2>

兼容性：此版本针对稳定的 `iii-sdk` `^0.11.0` 和 iii-engine v0.11.x。

### 30秒试用

```bash
# Terminal 1: start the server
npx @agentmemory/agentmemory

# Terminal 2: seed sample data and see recall in action
npx @agentmemory/agentmemory demo
```

`demo` 会填充 3 个真实会话（JWT 认证、N+1 查询修复、速率限制）并针对它们运行语义搜索。当你搜索“数据库性能优化”时，你会看到它找到“N+1 查询修复” — 关键词匹配无法做到这一点。

打开 `http://localhost:3113` 观看记忆构建过程。

### 推荐：全局安装

`npx` 会针对每个版本进行缓存。如果你上周运行了 `npx @agentmemory/agentmemory@0.9.14`，那么裸命令 `npx @agentmemory/agentmemory` 可能会从 `~/.npm/_npx/` 提供过时的 0.9.14 版本，而不是最新版本。安装一次后，裸命令 `agentmemory` 即可在任何地方使用：

```bash
npm install -g @agentmemory/agentmemory
# If you hit EACCES on macOS/Linux system Node installs, retry with:
# sudo npm install -g @agentmemory/agentmemory
agentmemory                    # start the server (same as the npx form)
agentmemory stop               # tear it down
agentmemory remove             # uninstall everything we created
agentmemory connect claude-code   # wire one agent
agentmemory doctor             # interactive diagnostics + fix prompts
```

从 v0.9.16 开始，首次运行 npx 会提示你全局安装 — 回答 `Y` 一次即可。如果你跳过此步骤，可回退到以下任一方式获取最新版本：

```bash
npx -y @agentmemory/agentmemory@latest                 # forces latest from npm (cross-platform)
rm -rf ~/.npm/_npx && npx @agentmemory/agentmemory     # macOS/Linux only (POSIX shell)
```

在 Windows / PowerShell 上，等效的缓存清理是 `Remove-Item -Recurse -Force "$env:LOCALAPPDATA\npm-cache\_npx"` — 上述 `npx -y ...@latest` 形式是跨平台选项。

### 会话回放 (Session Replay)

agentmemory 记录的每个会话都是可回放的。打开查看器，选择 **Replay** 标签页，并在时间轴上滑动：提示词、工具调用、工具结果和响应渲染为离散事件，支持播放/暂停、速度控制（0.5×–4×）以及键盘快捷键（空格键切换，方向键步进）。

已经有旧的 Claude Code JSONL 转录文件想要导入？

```bash
# Import everything under the default ~/.claude/projects
npx @agentmemory/agentmemory import-jsonl

# Or import a single file
npx @agentmemory/agentmemory import-jsonl ~/.claude/projects/-my-project/abc123.jsonl
```

导入的会话会与原生的会话一起显示在 Replay 选择器中。底层机制下，每个条目都通过 `mem::replay::load`、`mem::replay::sessions` 和 `mem::replay::import-jsonl` iii 函数进行路由 — 没有旁路服务器。

### 升级 / 维护

当你有意更新本地运行时环境时，请使用维护命令：

```bash
npx @agentmemory/agentmemory upgrade
```

警告：此命令会修改当前工作区/运行时。它可能会更新 JavaScript 依赖项、运行 `cargo install iii-engine --force`，以及拉取 Docker 镜像。

实现细节位于 `src/cli.ts`（参见 `runUpgrade` 函数，约在 `src/cli.ts:544-595` 区域）。

### Claude Code (一个代码块，直接粘贴)

```text
Install agentmemory: run `npx @agentmemory/agentmemory` in a separate terminal to start the memory server. Then run `/plugin marketplace add rohitg00/agentmemory` and `/plugin install agentmemory` — the plugin registers all 12 hooks, 8 skills, AND auto-wires the `@agentmemory/mcp` stdio server via its `.mcp.json`, so you get 53 MCP tools (memory_smart_search, memory_save, memory_sessions, memory_governance_delete, etc.) without any extra config step. Verify with `curl http://localhost:3111/agentmemory/health`. The real-time viewer is at http://localhost:3113.
```

#### Claude Code 无插件安装路径 (MCP-standalone)

如果你直接通过 `~/.claude.json` 将 agentmemory 的 MCP 服务器接入，而不是使用 `/plugin install`，Claude Code 将无法解析 `${CLAUDE_PLUGIN_ROOT}`，且你必须将钩子脚本指向 `~/.claude/settings.json` 中的绝对路径。这些路径通常嵌入了 agentmemory 的版本号（例如 `~/.codex/plugins/cache/agentmemory/agentmemory/0.9.22/scripts/…`），所以下次升级会静默破坏所有钩子 ([#508](https://github.com/rohitg00/agentmemory/issues/508))。

变通方案：

```bash
agentmemory connect claude-code --with-hooks
```

这会将相同的钩子命令合并到 `~/.claude/settings.json` 中，绝对路径解析为当前安装的 `@agentmemory/agentmemory` 包中的捆绑 `plugin/` 目录。升级 agentmemory 后重新运行此命令以刷新路径。同一文件中的用户条目将被保留；仅替换之前的 agentmemory 条目。使用 `/plugin install` 路径仍是推荐的方法。
对于远程或受保护的部署，启动 Claude Code 时设置 `AGENTMEMORY_URL` 和 `AGENTMEMORY_SECRET`。插件会将这两个值传递给其捆绑的 MCP 服务器；当 `AGENTMEMORY_URL` 为空时，MCP shim 会使用 `http://localhost:3111`。

### Codex CLI (Codex 插件平台)

```bash
# 1. start the memory server in a separate terminal
npx @agentmemory/agentmemory

# 2. register the agentmemory marketplace and install the plugin
codex plugin marketplace add rohitg00/agentmemory
codex plugin add agentmemory@agentmemory
```

Codex 插件与 Claude Code 插件来自同一个 `plugin/` 目录。它注册了：

- `@agentmemory/mcp` 作为 MCP 服务器（当 `AGENTMEMORY_URL` 指向正在运行的 agentmemory 服务器时代理所有 53 个工具；当没有服务器可达时回退到本地 7 个工具）
- 6 个生命周期钩子：`SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `Stop`
- 8 个技能：`/recall`, `/remember`, `/session-history`, `/forget`, `/recap`, `/handoff`, `/commit-context`, `/commit-history`

Codex 的钩子引擎将 `CLAUDE_PLUGIN_ROOT` 注入到钩子子进程中（参见 [`codex-rs/hooks/src/engine/discovery.rs`](https://github.com/openai/codex/blob/main/codex-rs/hooks/src/engine/discovery.rs)），因此相同的钩子脚本可以在两个主机上工作而无需重复。Subagent / SessionEnd / Notification / TaskCompleted / PostToolUseFailure 事件仅适用于 Claude Code，不会为 Codex 注册。

#### Codex Desktop：插件钩子目前静默（有变通方案）

`CodexHooks` 和 `PluginHooks` 在 [`codex-rs/features/src/lib.rs`](https://github.com/openai/codex/blob/main/codex-rs/features/src/lib.rs) 中均为稳定且默认启用，但 Codex Desktop 构建目前未分派插件本地的 `hooks.json`（[openai/codex#16430](https://github.com/openai/codex/issues/16430)）。MCP 工具仍然有效；仅缺少生命周期观测。

在修复上线之前，将相同的钩子命令镜像到全局的 `~/.codex/hooks.json`：

```bash
agentmemory connect codex --with-hooks
```

这会在 `~/.codex/hooks.json` 中添加一个幂等块，引用捆绑脚本的绝对路径（无需在用户作用域展开 `${CLAUDE_PLUGIN_ROOT}`）。升级 agentmemory 后重新运行相同的命令以刷新路径。同一文件中的用户条目将被保留；仅替换之前的 agentmemory 条目。

### GitHub Copilot CLI

```bash
# MCP-only wiring
agentmemory connect copilot-cli

# Full hooks/skills plugin from the GitHub subdir
copilot plugin install rohitg00/agentmemory:plugin
```

`agentmemory connect copilot-cli` 将 `mcpServers.agentmemory` 合并到 `~/.copilot/mcp-config.json`（当设置 `COPILOT_HOME` 时为 `$COPILOT_HOME/mcp-config.json`）并保留现有服务器。此适配器是 Windows 安全的，即使其他 `connect` 适配器仍需要手动 Windows 设置也是如此。Copilot 在下次启动或执行 `/mcp` 后拾取 MCP 服务器。当你想要完整的钩子/技能体验时安装插件。

<details>
<summary><b>OpenClaw (粘贴此提示)</b></summary>

```text
Install agentmemory for OpenClaw. Run `npx @agentmemory/agentmemory` in a separate terminal to start the memory server on localhost:3111. Then add this to my OpenClaw MCP config so agentmemory is available with all 53 memory tools:

{
  "mcpServers": {
    "agentmemory": {
      "command": "npx",
      "args": ["-y", "@agentmemory/mcp"],
      "env": {
        "AGENTMEMORY_URL": "http://localhost:3111"
      }
    }
  }
}

Restart OpenClaw. Verify with `curl http://localhost:3111/agentmemory/health`. Open http://localhost:3113 for the real-time viewer. For deeper memory-slot integration, copy `integrations/openclaw` to `~/.openclaw/extensions/agentmemory` and enable `plugins.slots.memory = "agentmemory"` in `~/.openclaw/openclaw.json`.
```

完整指南：[`integrations/openclaw/`](integrations/openclaw/)

</details>

<details>
<summary><b>Hermes Agent (粘贴此提示)</b></summary>

```text
Install agentmemory for Hermes. Run `npx @agentmemory/agentmemory` in a separate terminal to start the memory server on localhost:3111. Then add this to ~/.hermes/config.yaml so Hermes can use agentmemory as an MCP server with all 53 memory tools:

mcp_servers:
  agentmemory:
    command: npx
    args: ["-y", "@agentmemory/mcp"]

memory:
  provider: agentmemory

Verify with `curl http://localhost:3111/agentmemory/health`. Open http://localhost:3113 for the real-time viewer. For deeper 6-hook memory provider integration (pre-LLM context injection, turn capture, MEMORY.md mirroring, system prompt block), copy integrations/hermes from the agentmemory repo to ~/.hermes/plugins/agentmemory.
```

完整指南：[`integrations/hermes/`](integrations/hermes/)

</details>

### 其他代理

启动记忆服务器：`npx @agentmemory/agentmemory`

#### 通过 `npx skills add` 使用原生技能 (50+ 代理)

agentmemory 以 Claude Code 风格的 `<dir>/SKILL.md` 格式提供了 8 个技能（`remember`, `recall`, `recap`, `handoff`, `forget`, `commit-context`, `commit-history`, `session-history`）。[`skills`](https://npmjs.com/package/skills) CLI 由 vercel-labs 开发，可自动将它们安装到调用代理的原生技能目录中（支持 50+ 个代理：Claude Code, Cursor, Cline, Continue, Droid, Warp, Codex, Antigravity, Kiro, OpenCode, Goose, Roo, Trae, Windsurf 等）：

```bash
npx skills add rohitg00/agentmemory -y          # auto-detects the calling agent
npx skills add rohitg00/agentmemory -y -a warp  # explicit agent
npx skills add rohitg00/agentmemory -y -a '*'   # install to every installed agent
```

这**补充了** `agentmemory connect <agent>`：

- `agentmemory connect <agent>` 写入 MCP 服务器配置，使工具可用。
- `npx skills add rohitg00/agentmemory` 安装技能，让代理知道何时调用它们。

对于少数尚未被 skills CLI 覆盖的代理（Zed v1.3.x 及以下），请手动将 8 个 SKILL.md 文件放入代理的原生技能目录下 — 格式在所有地方都通用。

#### 标准 MCP 代码块

agentmemory 条目是 **相同的 MCP 服务器代码块**，适用于所有使用 `mcpServers` 结构的宿主（Cursor, Claude Desktop, Cline, Roo Code, Windsurf, Gemini CLI, OpenClaw）：

```json
"agentmemory": {
  "command": "npx",
  "args": ["-y", "@agentmemory/mcp"],
  "env": {
    "AGENTMEMORY_URL": "${AGENTMEMORY_URL}",
    "AGENTMEMORY_SECRET": "${AGENTMEMORY_SECRET}"
  }
}
```

**将此条目合并到宿主配置文件中的现有 `mcpServers` 对象中** — 不要替换文件。如果文件中已有其他服务器，请在 `mcpServers` 内作为另一个键添加 `agentmemory`。如果完全缺少 `mcpServers`，请将代码块粘贴在 `{ "mcpServers": { ... } }` 内部。`${VAR}` 占位符会在 MCP 服务器启动时从 shell 继承 `AGENTMEMORY_URL` / `AGENTMEMORY_SECRET` — 未设置的变量会传递空字符串，shim 将回退到 `http://localhost:3111`。一个接入条目即可覆盖本地和远程（k8s/反向代理）部署。

| Agent | Config file | Notes |
|---|---|---|
| **Cursor** | `~/.cursor/mcp.json` | Merge into `mcpServers`. One-click deeplink also available on the website. |
| **Claude Desktop** | `claude_desktop_config.json` (Application Support) | Merge into `mcpServers`. Restart Claude Desktop after editing. |
| **Cline / Roo Code / Kilo Code** | Cline MCP settings (Settings UI → MCP Servers → Edit) | Same `mcpServers` block. |
| **Windsurf** | `~/.codeium/windsurf/mcp_config.json` | Same `mcpServers` block. |
| **Gemini CLI** | `~/.gemini/settings.json` | `gemini mcp add agentmemory npx -y @agentmemory/mcp --scope user` (auto-merges). |
| **GitHub Copilot CLI (MCP only)** | `~/.copilot/mcp-config.json` | `agentmemory connect copilot-cli` merges `mcpServers.agentmemory`; Copilot picks it up on next launch or `/mcp`. |
| **GitHub Copilot CLI (full plugin)** | Copilot plugin install | `copilot plugin install rohitg00/agentmemory:plugin` for the plugin from the GitHub subdir. |
| **OpenClaw** | OpenClaw MCP config | Same `mcpServers` block, or use the deeper [memory plugin](integrations/openclaw/). |
| **Codex CLI (MCP only)** | `.codex/config.toml` | TOML shape: `codex mcp add agentmemory -- npx -y @agentmemory/mcp`, or add `[mcp_servers.agentmemory]` manually. |
| **Codex CLI (full plugin)** | Codex plugin marketplace | `codex plugin marketplace add rohitg00/agentmemory` then `codex plugin add agentmemory@agentmemory`. Registers MCP + 6 lifecycle hooks (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PreCompact, Stop) + 8 skills. On Codex Desktop, also run `agentmemory connect codex --with-hooks` until [openai/codex#16430](https://github.com/openai/codex/issues/16430) lands — plugin hooks are currently silent there. |
| **OpenCode (MCP only)** | `opencode.json` | Different shape — top-level `mcp` key, command as array: `{"mcp": {"agentmemory": {"type": "local", "command": ["npx", "-y", "@agentmemory/mcp"], "enabled": true}}}`. |
| **OpenCode (full plugin)** | `plugin/opencode/` | 22 auto-capture hooks covering session lifecycle, messages, tools, errors. Two slash commands (`/recall`, `/remember`). Copy `plugin/opencode/` into your OpenCode workspace and add the plugin entry to `opencode.json`. See [`plugin/opencode/README.md`](plugin/opencode/README.md) for the full hook table + gap analysis. |
| **pi** | `~/.pi/agent/extensions/agentmemory` | Copy [`integrations/pi`](integrations/pi/) and restart pi. |
| **Hermes Agent** | `~/.hermes/config.yaml` | Use the deeper [memory provider plugin](integrations/hermes/) with `memory.provider: agentmemory`. |
| **Qwen Code** | `~/.qwen/settings.json` | `agentmemory connect qwen` writes the standard `mcpServers` block. Hook payload is field-compatible with Claude Code, so the existing 12-hook scripts work without modification — wire them via the `hooks` section in the same `settings.json`. |
| **Antigravity** (replaces Gemini CLI) | `mcp_config.json` (in Antigravity's User dir) | `agentmemory connect antigravity` writes the standard `mcpServers` block. macOS: `~/Library/Application Support/Antigravity/User/`. Linux: `~/.config/Antigravity/User/`. Use after the 2026-06-18 Gemini CLI sunset. |
| **Kiro** | `~/.kiro/settings/mcp.json` | `agentmemory connect kiro` writes the user-level config. Workspace overrides go in `.kiro/settings/mcp.json` next to your code. |
| **Warp** | `~/.warp/.mcp.json` | `agentmemory connect warp` writes the standard `mcpServers` block. Warp also auto-discovers skills from `.claude/skills/` — once the Claude Code plugin is installed the 8 agentmemory skills (`remember`, `recall`, `recap`, `handoff`, `forget`, `commit-context`, `commit-history`, `session-history`) appear natively in Warp's slash-command palette. |
| **Cline (CLI)** | `~/.cline/mcp.json` | `agentmemory connect cline` writes the standard `mcpServers` block. VS Code extension users: paste the same block via Cline Settings → MCP Servers → Edit JSON. |
| **Continue.dev** | `~/.continue/config.yaml` (preferred) or `config.json` (legacy) | `agentmemory connect continue` creates `config.yaml` from scratch when neither exists, or modifies existing `config.json`. **If you already have `config.yaml`** the adapter prints the exact block to paste under `mcpServers:` — it won't silently rewrite your yaml because preserving comments and anchors safely needs a YAML parser the package doesn't ship. Continue uses array form (not object) for `mcpServers`. |
| **Zed** | `~/.config/zed/settings.json` | `agentmemory connect zed` writes under `context_servers` (Zed's key, NOT `mcpServers`). Remote MCP servers can be wired via `{"url": "..."}` instead. |
| **Droid (Factory.ai)** | `~/.factory/mcp.json` | `agentmemory connect droid` writes the standard `mcpServers` block. Project-scoped overrides go in `<repo>/.factory/mcp.json`. The `/mcp` slash command inside droid lists configured servers. |
| **Goose** | Goose MCP settings UI | Same `mcpServers` block — use `goose configure` → Add Extension → MCP. Direct YAML edit at `~/.config/goose/config.yaml` is supported but the schema uses `extensions:` + `cmd` (not `mcpServers:` + `command`). |
| **Aider** | n/a | Talk to the REST API directly: `curl -X POST http://localhost:3111/agentmemory/smart-search -d '{"query": "auth"}'`. |
| **Any agent (32+)** | n/a | `npx skillkit install agentmemory` auto-detects the host and merges. |

**沙盒 MCP 客户端**（Flatpak / Snap / 受限容器）无法访问主机的 `localhost`：同时在 `env` 块中设置 `"AGENTMEMORY_FORCE_PROXY": "1"`，并将 `AGENTMEMORY_URL` 指向沙盒实际可访问的路由（例如你的局域网 IP）。参见 [#234](https://github.com/rohitg00/agentmemory/issues/234) 的诊断指南。

### 编程访问 (Python / Rust / Node)

agentmemory 将其核心操作注册为 iii 函数 (`mem::remember`, `mem::observe`, `mem::context`, `mem::smart-search`, `mem::forget`)。任何具有 iii SDK 的语言都可以直接通过 `ws://localhost:49134` 调用它们 — 无需每种语言都使用单独的 REST 客户端。

```bash
pip install iii-sdk         # Python
cargo add iii-sdk           # Rust
npm  install iii-sdk        # Node
```

```python
from iii import register_worker

iii = register_worker("ws://localhost:49134")
iii.connect()

iii.trigger({
    "function_id": "mem::smart-search",
    "payload": {"project": "demo", "query": "how do tokens refresh"},
})
```

工作示例：[`examples/python/`](examples/python/) (快速入门 + 观测/召回流程)。`:3111` 上的 REST 对于没有 iii 运行时的宿主仍然可用。

### 从源代码构建

```bash
git clone https://github.com/rohitg00/agentmemory.git && cd agentmemory
npm install && npm run build && npm start
```

如果已安装 `iii`，这将使用本地 `iii-engine` 启动 agentmemory；或者如果有 Docker 可用则回退到 Docker Compose。REST、流和查看器默认绑定到 `127.0.0.1`。

手动安装 `iii-engine`。**agentmemory 目前将 `iii-engine` 固定为 `v0.11.2`** — `v0.11.6` 引入了新的通过 `iii worker add` 进行全沙盒化的模型，而 agentmemory 尚未为此重构。一旦重构完成，该限制将解除。如果你已手动迁移到沙盒模式，可使用 `AGENTMEMORY_III_VERSION=<version>` 覆盖。

- **macOS arm64:** `mkdir -p ~/.local/bin && curl -fsSL https://github.com/iii-hq/iii/releases/download/iii/v0.11.2/iii-aarch64-apple-darwin.tar.gz | tar -xz -C ~/.local/bin && chmod +x ~/.local/bin/iii`
- **macOS x64:** 将 `aarch64-apple-darwin` 替换为 `x86_64-apple-darwin`
- **Linux x64:** 替换为 `x86_64-unknown-linux-gnu`
- **Linux arm64:** 替换为 `aarch64-unknown-linux-gnu`
- **Windows:** 从 [iii-hq/iii releases v0.11.2](https://github.com/iii-hq/iii/releases/tag/iii%2Fv0.11.2) 下载 `iii-x86_64-pc-windows-msvc.zip`，解压 `iii.exe`，添加到 PATH

或使用 Docker（捆绑的 `docker-compose.yml` 会拉取 `iiidev/iii:0.11.2`）。完整文档：[iii.dev/docs](https://iii.dev/docs)。

### Windows

agentmemory 可在 Windows 10/11 上运行，但仅 Node.js 包是不够的 — 你还需要作为后台进程的 `iii-engine` 运行时（一个单独的原生二进制文件）。官方上游安装程序是一个 `sh` 脚本，目前还没有 PowerShell 安装程序或 scoop/winget 包，因此 Windows 用户有两条路径：

**选项 A — 预构建的 Windows 二进制文件（推荐）：**

```powershell
# 1. Open https://github.com/iii-hq/iii/releases/tag/iii%2Fv0.11.2 in your browser
#    (we pin to v0.11.2 until agentmemory refactors for the new sandbox
#     model that engine v0.11.6+ requires)
# 2. Download iii-x86_64-pc-windows-msvc.zip
#    (or iii-aarch64-pc-windows-msvc.zip if you're on an ARM machine)
# 3. Extract iii.exe somewhere on PATH, or place it at:
#    %USERPROFILE%\.local\bin\iii.exe
#    (agentmemory checks that location automatically)
# 4. Verify:
iii --version
# Should print: 0.11.2

# 5. Then run agentmemory as usual:
npx -y @agentmemory/agentmemory
```

**选项 B — Docker Desktop：**

```powershell
# 1. Install Docker Desktop for Windows
# 2. Start Docker Desktop and make sure the engine is running
# 3. Run agentmemory — it will auto-start the bundled compose file:
npx -y @agentmemory/agentmemory
```

**选项 C — standalone MCP only (no engine)：**如果你只需要代理的 MCP 工具，不需要 REST API、查看器或定时任务，可以完全跳过引擎：

```powershell
npx -y @agentmemory/agentmemory mcp
# or via the shim package:
npx -y @agentmemory/mcp
```

**Windows 诊断：**如果 `npx @agentmemory/agentmemory` 失败，请重新运行并添加 `--verbose` 以查看实际的引擎 stderr。常见故障模式：

| Symptom | Fix |
|---|---|
| `iii-engine process started` then `did not become ready within 15s` | Engine crashed on startup — re-run with `--verbose`, check stderr |
| `Could not start iii-engine` | Neither `iii.exe` nor Docker is installed. See Option A or B above |
| Port conflict | `netstat -ano \| findstr :3111` to see what's bound, then kill it or use `--port <N>` |
| Docker fallback skipped even though Docker is installed | Make sure Docker Desktop is actually running (system tray icon) |

> 注意：没有 `cargo install iii-engine` — `iii` 未发布到 crates.io。唯一支持的安装方法是上述预构建二进制文件、上游 `sh` 安装脚本（仅限 macOS/Linux）和 Docker 镜像。

---

<h2 id="deploy">Deploy</h2>

托管平台的单键部署模板。每个模板都包含一个自包含的
Dockerfile，从 npm 拉取 `@agentmemory/agentmemory` 并从官方 `iiidev/iii` Docker Hub
镜像中复制 iii 引擎二进制文件 — 不需要预构建的 agentmemory 镜像。持久化存储挂载在 `/data`；首次启动入口点会覆盖
npm 捆绑的 iii 配置（它绑定 `127.0.0.1`），替换为部署优化的配置，该配置绑定 `0.0.0.0` 并使用绝对 `/data` 路径，生成 HMAC 密钥，然后通过
`gosu` 将权限从 `root` 降级到 `node`，最后执行 agentmemory CLI。

<p>
  <a href="https://fly.io/launch?repo=https://github.com/rohitg00/agentmemory&path=deploy/fly"><img src="https://img.shields.io/badge/Deploy%20to-fly.io-8b5cf6?style=for-the-badge&logo=fly.io&logoColor=white" alt="Deploy to fly.io" /></a>
  <a href="https://railway.com/new/template?template=https%3A%2F%2Fgithub.com%2Frohitg00%2Fagentmemory&rootDirectory=deploy%2Frailway"><img src="https://img.shields.io/badge/Deploy%20to-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white" alt="Deploy to Railway" /></a>
</p>

Render 的单键部署按钮要求 `render.yaml` 位于仓库根目录，我们故意保持其干净。请使用 [`deploy/render/`](./deploy/render/README.md) 中记录的 Render Blueprint 流程手动指向仓库中的蓝图。

完整设置详情（HMAC 捕获、查看器 SSH 隧道、轮换、备份）位于 [`deploy/`](./deploy/README.md)：

- [`deploy/fly`](./deploy/fly/README.md) — 单台机器，带有
  `auto_stop_machines = "stop"`；空闲时最便宜。
- [`deploy/railway`](./deploy/railway/README.md) — Hobby 计划固定费用，
  仪表板中的卷。
- [`deploy/render`](./deploy/render/README.md) — Blueprint 流程，
  付费计划上的自动磁盘快照。
- [`deploy/coolify`](./deploy/coolify/README.md) — 在 [Coolify](https://coolify.io/self-hosted) 上通过 VPS
  自托管；相同的 Docker Compose 堆栈，你拥有主机和数据。

仅发布端口 `3111`。位于 `3113` 的查看器保持在容器内的回环绑定 — 每个模板的 README 都记录了访问它的 SSH 隧道模式。

---

<h2 id="why-agentmemory"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-why.svg"><img src="assets/tags/section-why.svg" alt="Why agentmemory" height="32" /></picture></h2>

每个编程代理在会话结束时都会忘记一切。你浪费每次会话的前 5 分钟来重新解释你的技术栈。agentmemory 在后台运行并完全消除了这一点。

```text
Session 1: "Add auth to the API"
  Agent writes code, runs tests, fixes bugs
  agentmemory silently captures every tool use
  Session ends -> observations compressed into structured memory

Session 2: "Now add rate limiting"
  Agent already knows:
    - Auth uses JWT middleware in src/middleware/auth.ts
    - Tests in test/auth.test.ts cover token validation
    - You chose jose over jsonwebtoken for Edge compatibility
  Zero re-explaining. Starts working immediately.
```

### vs built-in agent memory

每个 AI 编程代理都附带内置记忆 — Claude Code 有 `MEMORY.md`，Cursor 有笔记本，Cline 有记忆库。这些就像便利贴一样工作。agentmemory 是便利贴背后的可搜索数据库。

| | Built-in (CLAUDE.md) | agentmemory |
|---|---|---|
| Scale | 200-line cap | Unlimited |
| Search | Loads everything into context | BM25 + vector + graph (top-K only) |
| Token cost | 22K+ at 240 observations | ~1,900 tokens (92% less) |
| Cross-agent | Per-agent files | MCP + REST (any agent) |
| Coordination | None | Leases, signals, actions, routines |
| Observability | Read files manually | Real-time viewer on :3113 |

---

<h2 id="how-it-works"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-how.svg"><img src="assets/tags/section-how.svg" alt="How It Works" height="32" /></picture></h2>

### 记忆管线 (Memory Pipeline)

```text
PostToolUse hook fires
  -> SHA-256 dedup (5min window)
  -> Privacy filter (strip secrets, API keys)
  -> Store raw observation
  -> LLM compress -> structured facts + concepts + narrative
  -> Vector embedding (6 providers + local)
  -> Index in BM25 + vector

Stop / SessionEnd hook fires
  -> Summarize session
  -> Knowledge graph extraction (if GRAPH_EXTRACTION_ENABLED=true)
  -> Slot reflection (if SLOT_REFLECT_ENABLED=true)

SessionStart hook fires
  -> Load project profile (top concepts, files, patterns)
  -> Hybrid search (BM25 + vector + graph)
  -> Token budget (default: 2000 tokens)
  -> Inject into conversation
```

### 4级记忆整合 (4-Tier Memory Consolidation)

灵感来源于人类大脑处理记忆的方式 — 类似于睡眠巩固。

| Tier | What | Analogy |
|------|------|---------|
| **Working** | Raw observations from tool use | Short-term memory |
| **Episodic** | Compressed session summaries | "What happened" |
| **Semantic** | Extracted facts and patterns | "What I know" |
| **Procedural** | Workflows and decision patterns | "How to do it" |

记忆会随时间衰减（艾宾浩斯曲线）。频繁访问的记忆得到加强。过时的记忆会自动驱逐。检测到并解决矛盾。

### 捕获内容 (What Gets Captured)

| Hook | Captures |
|------|----------|
| `SessionStart` | Project path, session ID |
| `UserPromptSubmit` | User prompts (privacy-filtered) |
| `PreToolUse` | File access patterns + enriched context |
| `PostToolUse` | Tool name, input, output |
| `PostToolUseFailure` | Error context |
| `PreCompact` | Re-injects memory before compaction |
| `SubagentStart/Stop` | Sub-agent lifecycle |
| `Stop` | End-of-session summary |
| `SessionEnd` | Session complete marker |

### 关键功能 (Key Capabilities)

| Capability | Description |
|---|---|
| **Automatic capture** | Every tool use recorded via hooks — zero manual effort |
| **Semantic search** | BM25 + vector + knowledge graph with RRF fusion |
| **Memory evolution** | Versioning, supersession, relationship graphs |
| **Auto-forgetting** | TTL expiry, contradiction detection, importance eviction |
| **Privacy first** | API keys, secrets, `<private>` tags stripped before storage |
| **Self-healing** | Circuit breaker, provider fallback chain, health monitoring |
| **Claude bridge** | Bi-directional sync with MEMORY.md |
| **Knowledge graph** | Entity extraction + BFS traversal |
| **Team memory** | Namespaced shared + private across team members |
| **Citation provenance** | Trace any memory back to source observations |
| **Git snapshots** | Version, rollback, and diff memory state |

---

<h2 id="search"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-search.svg"><img src="assets/tags/section-search.svg" alt="Search" height="32" /></picture></h2>

结合三个信号的三重流检索：

| Stream | What it does | When |
|---|---|---|
| **BM25** | Stemmed keyword matching with synonym expansion | Always on |
| **Vector** | Cosine similarity over dense embeddings | Embedding provider configured |
| **Graph** | Knowledge graph traversal via entity matching | Entities detected in query |

使用倒数排名融合 (RRF, k=60) 和会话多样化（每个会话最多 3 个结果）进行融合。

BM25 开箱即用地对希腊语、西里尔字母、希伯来语、阿拉伯语和带重音的拉丁语进行分词。对于中文/日文/韩文记忆，安装可选的分词器 (`npm install @node-rs/jieba tiny-segmenter`) 将 CJK 运行拆分为单词级 token；否则，agentmemory 会软回退到整段分词并在 stderr 上打印一次性提示。

### 嵌入提供商 (Embedding providers)

agentmemory 会自动检测你的提供商。为了获得最佳效果，请安装本地嵌入（免费）：

```bash
npm install @xenova/transformers
```

| Provider | Model | Cost | Notes |
|---|---|---|---|
| **Local (recommended)** | `all-MiniLM-L6-v2` | Free | Offline, +8pp recall over BM25-only |
| Gemini | `gemini-embedding-001` | Free tier | 100+ languages, 768/1536/3072 dims (MRL), 2048-token input. Replaces `text-embedding-004` ([deprecated, shutdown Jan 14, 2026](https://ai.google.dev/gemini-api/docs/deprecations)) |
| OpenAI | `text-embedding-3-small` | $0.02/1M | Highest quality |
| Voyage AI | `voyage-code-3` | Paid | Optimized for code |
| Cohere | `embed-english-v3.0` | Free trial | General purpose |
| OpenRouter | Any model | Varies | Multi-model proxy |

---

<h2 id="mcp-server"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-mcp.svg"><img src="assets/tags/section-mcp.svg" alt="MCP Server" height="32" /></picture></h2>

53 个工具，6 个资源，3 个提示词和 8 个技能 — 面向任何代理的最全面的 MCP 记忆工具箱。

> **MCP shim vs full server：**发布的 `@agentmemory/mcp` 包是一个薄层 (shim)。它仅在通过 `AGENTMEMORY_URL` 能够访问正在运行的 agentmemory 服务器时暴露完整的 53 个工具表面（代理模式）。当没有服务器可达时，shim 会回退到 7 个工具的本地集合 (`memory_save`, `memory_recall`, `memory_smart_search`, `memory_sessions`, `memory_export`, `memory_audit`, `memory_governance_delete`)。`AGENTMEMORY_TOOLS=core|all` 环境变量是一个 *服务器端* 标志 — 在 shim 的 `env` 块中设置它无效。如果你在 Cursor / OpenCode / Gemini CLI 中只看到 7 个工具，请启动 `npx @agentmemory/agentmemory`（或 Docker 堆栈）并设置 `AGENTMEMORY_URL=http://localhost:3111`。

### 53 Tools

<details>
<summary>Core tools (always available)</summary>

| Tool | Description |
|------|-------------|
| `memory_recall` | Search past observations |
| `memory_compress_file` | Compress markdown files while preserving structure |
| `memory_save` | Save an insight, decision, or pattern |
| `memory_patterns` | Detect recurring patterns |
| `memory_smart_search` | Hybrid semantic + keyword search |
| `memory_file_history` | Past observations about specific files |
| `memory_sessions` | List recent sessions |
| `memory_timeline` | Chronological observations |
| `memory_profile` | Project profile (concepts, files, patterns) |
| `memory_export` | Export all memory data |
| `memory_relations` | Query relationship graph |

</details>

<details>
<summary>Extended tools (53 total — set AGENTMEMORY_TOOLS=all)</summary>

| Tool | Description |
|------|-------------|
| `memory_patterns` | Detect recurring patterns |
| `memory_timeline` | Chronological observations |
| `memory_relations` | Query relationship graph |
| `memory_graph_query` | Knowledge graph traversal |
| `memory_consolidate` | Run 4-tier consolidation |
| `memory_claude_bridge_sync` | Sync with MEMORY.md |
| `memory_team_share` | Share with team members |
| `memory_team_feed` | Recent shared items |
| `memory_audit` | Audit trail of operations |
| `memory_governance_delete` | Delete with audit trail |
| `memory_snapshot_create` | Git-versioned snapshot |
| `memory_action_create` | Create work items with dependencies |
| `memory_action_update` | Update action status |
| `memory_frontier` | Unblocked actions ranked by priority |
| `memory_next` | Single most important next action |
| `memory_lease` | Exclusive action leases (multi-agent) |
| `memory_routine_run` | Instantiate workflow routines |
| `memory_signal_send` | Inter-agent messaging |
| `memory_signal_read` | Read messages with receipts |
| `memory_checkpoint` | External condition gates |
| `memory_mesh_sync` | P2P sync between instances |
| `memory_sentinel_create` | Event-driven watchers |
| `memory_sentinel_trigger` | Fire sentinels externally |
| `memory_sketch_create` | Ephemeral action graphs |
| `memory_sketch_promote` | Promote to permanent |
| `memory_crystallize` | Compact action chains |
| `memory_diagnose` | Health checks |
| `memory_heal` | Auto-fix stuck state |
| `memory_facet_tag` | Dimension:value tags |
| `memory_facet_query` | Query by facet tags |
| `memory_verify` | Trace provenance |

</details>

### 6 Resources · 3 Prompts · 4 Skills

| Type | Name | Description |
|------|------|-------------|
| Resource | `agentmemory://status` | Health, session count, memory count |
| Resource | `agentmemory://project/{name}/profile` | Per-project intelligence |
| Resource | `agentmemory://memories/latest` | Latest 10 active memories |
| Resource | `agentmemory://graph/stats` | Knowledge graph statistics |
| Prompt | `recall_context` | Search + return context messages |
| Prompt | `session_handoff` | Handoff data between agents |
| Prompt | `detect_patterns` | Analyze recurring patterns |
| Skill | `/recall` | Search memory |
| Skill | `/remember` | Save to long-term memory |
| Skill | `/session-history` | Recent session summaries |
| Skill | `/forget` | Delete observations/sessions |

### Standalone MCP

在不运行完整服务器的情况下运行 — 适用于任何 MCP 客户端。以下任一方式均可：

```bash
npx -y @agentmemory/agentmemory mcp   # canonical (always available)
npx -y @agentmemory/mcp                # shim package alias
```

或添加到代理的 MCP 配置中：

大多数代理（Cursor, Claude Desktop, Cline, Roo Code, Windsurf, Gemini CLI）：
```json
{
  "mcpServers": {
    "agentmemory": {
      "command": "npx",
      "args": ["-y", "@agentmemory/mcp"],
      "env": {
        "AGENTMEMORY_URL": "http://localhost:3111"
      }
    }
  }
}
```

将 `agentmemory` 条目合并到宿主现有的 `mcpServers` 对象中，而不是替换文件。对于无法访问主机 `localhost` 的沙盒客户端，请在 env 块中添加 `"AGENTMEMORY_FORCE_PROXY": "1"` 并将 `AGENTMEMORY_URL` 设置为沙盒可访问的路由。

OpenCode (`opencode.json`)：
```json
{
  "mcp": {
    "agentmemory": {
      "type": "local",
      "command": ["npx", "-y", "@agentmemory/mcp"],
      "enabled": true
    }
  },
  "plugin": ["./plugins/agentmemory-capture.ts"]
}
```

从仓库复制插件文件：
```bash
mkdir -p ~/.config/opencode/plugins
cp plugin/opencode/agentmemory-capture.ts ~/.config/opencode/plugins/
cp plugin/opencode/commands/*.md ~/.config/opencode/commands/
```

---

<h2 id="real-time-viewer"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-viewer.svg"><img src="assets/tags/section-viewer.svg" alt="Real-Time Viewer" height="32" /></picture></h2>

自动在端口 `3113` 启动。实时观测流、会话浏览器、记忆浏览器、知识图谱可视化和健康仪表板。

```bash
open http://localhost:3113
```

查看器服务器默认绑定到 `127.0.0.1`。REST 提供的 `/agentmemory/viewer` 端点遵循正常的 `AGENTMEMORY_SECRET` bearer-token 规则。CSP 标头使用每个响应脚本 nonce 并禁用内联处理程序属性 (`script-src-attr 'none'`)。

---

<h2 id="iii-console"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-viewer.svg"><img src="assets/tags/section-viewer.svg" alt="iii Console" height="32" /></picture></h2>

`:3113` 处的查看器显示你的代理 **记住了什么**。[iii console](https://iii.dev/docs/console) 显示你的代理 **做了什么** — 每个记忆操作作为 OpenTelemetry 跟踪，每个 KV 条目可编辑，每个函数可调用的，每个流都可连接的。同一记忆的两个窗口：一个产品形状，一个引擎形状。

观看 `memory_smart_search` 触发并查看 BM25 扫描 → 嵌入查找 → RRF 融合 → 重排器作为瀑布图。在 KV 浏览器中编辑卡住的整合计时器。使用调整后的有效负载回放 `PostToolUse` 钩子。固定 WebSocket 流并观看观测数据实时落地。

agentmemory 免费提供此功能，因为每个函数调用和触发都通过 iii — 没有自定义内容，无需额外仪器化。

<p align="center">
  <img src="assets/iii-console/workers.png" alt="iii console Workers page — connected workers including agentmemory instances with live function counts and runtime metadata" width="720" />
  <br/>
  <em>Workers page: every connected worker — including agentmemory itself — with PID, function count, runtime, and last-seen.</em>
</p>

**已安装。** Console 随 `iii` 一起提供 — 无需单独的安装程序。

**与 agentmemory 同时启动：**

```bash
# agentmemory viewer holds port 3113, so run the console on 3114.
# Engine REST (3111), WebSocket (3112), and bridge (49134) defaults match agentmemory.
iii console --port 3114
```

然后打开 `http://localhost:3114`。添加 `--enable-flow` 以获取实验性的架构图页面。

仅在你移动了引擎端点时才覆盖它们：

```bash
iii console --port 3114 \
  --engine-port 3111 \
  --ws-port 3112 \
  --bridge-port 49134
```

**你可以从 Console 做什么：**

| Page | Use it to |
|------|-----------|
| **Workers** | See every connected worker and its live metrics — including the agentmemory worker itself. |
| **Functions** | Invoke any of agentmemory's functions directly with a JSON payload — handy for testing `memory.recall`, `memory.consolidate`, `graph.query` without wiring a client. |
| **Triggers** | Replay HTTP, cron, event, and state triggers — fire the consolidation cron manually, retry an HTTP route, emit a state change. |
| **States** | KV browser with full CRUD — sessions, memory slots, lifecycle timers, embeddings index — edit values in place. |
| **Streams** | Live WebSocket monitor for memory writes, hook events, and observation updates as they flow through iii streams. |
| **Queues** | Durable queue topics + dead-letter management. Replay or drop failed embedding / compression jobs. |
| **Traces** | OpenTelemetry waterfall / flame / service-breakdown views. Filter by `trace_id` to see exactly which functions, DB calls, and embedding requests a single `memory.search` produced. |
| **Logs** | Structured OTEL logs filtered and correlated to trace/span IDs. |
| **Config** | Runtime configuration — see exactly which workers, providers, and ports your engine is running with. |
| **Flow** | (Optional, `--enable-flow`) Interactive architecture graph of every worker, trigger, and stream. |

<p align="center">
  <img src="assets/iii-console/traces-waterfall.png" alt="iii console trace waterfall view showing per-span duration" width="720" />
  <br/>
  <em>Traces: waterfall / flame / service breakdown for every memory operation.</em>
</p>

**跟踪已开启：**

`iii-config.yaml` 随启用了 `iii-observability` worker（`exporter: memory`, `sampling_ratio: 1.0`, metrics + logs）。无需额外配置 — agentmemory 启动的那一刻，每个记忆操作都会发出一个跟踪 span 和一个结构化日志，Console 可以读取。

如果你想导出到 Jaeger/Honeycomb/Grafana Tempo，请将 `exporter: memory` 更改为 `exporter: otlp` 并根据 iii 的可观测性文档设置收集器端点。

> **注意：** Console 本身不强制执行身份验证 — 将其绑定到 `127.0.0.1`（默认值）并永远不要公开暴露它。

---

<h2 id="powered-by-iii"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-architecture.svg"><img src="assets/tags/section-architecture.svg" alt="Powered by iii" height="32" /></picture></h2>

agentmemory **已经是一个正在运行的 [iii](https://iii.dev) 实例**。三个原语 — worker、function、trigger — 组成了运行时；KV 状态、流和 OTEL 跟踪来自 iii-state、iii-stream 和 iii-observability workers，它们随 iii 一起提供。你没有安装 Postgres、Redis、Express、pm2 或 Prometheus，因为 iii 替代了它们。

这意味着多一个命令就可以将 agentmemory 扩展为整个新功能。

### 通过一条命令扩展 agentmemory

```bash
iii worker add iii-pubsub          # fan memory writes out to every connected instance
iii worker add iii-cron            # scheduled consolidation, decay sweeps, snapshot rotation
iii worker add iii-queue           # durable retries for embedding + compression jobs
iii worker add iii-observability   # OTEL traces on every memory op (default on)
iii worker add iii-sandbox         # run recalled code inside an isolated microVM
iii worker add iii-database        # swap in a SQL-backed state adapter
iii worker add mcp                 # generic MCP host alongside the agentmemory MCP
```

每个 `iii worker add` 将新函数和触发器注册到 agentmemory 已经运行的同一引擎中。查看器和 Console 会立即拾取它们 — 无需重新加载，无需新的集成，无需新的容器。

| `iii worker add` | What you get on top of agentmemory |
|---|---|
| [`iii-pubsub`](https://workers.iii.dev/workers/iii-pubsub) | Multi-instance memory: every `remember` fans out, every `search` reads the union |
| [`iii-cron`](https://workers.iii.dev/workers/iii-cron) | Scheduled lifecycle — nightly consolidation, weekly snapshots, decay on a fixed clock |
| [`iii-queue`](https://workers.iii.dev/workers/iii-queue) | Durable retries: failed embedding + compression jobs survive restart, no lost observations |
| [`iii-observability`](https://workers.iii.dev/workers/iii-observability) | OTEL traces, metrics, logs on every function — wired in `iii-config.yaml` from day one |
| [`iii-sandbox`](https://workers.iii.dev/workers/iii-sandbox) | Code that came out of `memory_recall` runs inside a throwaway VM, not your shell |
| [`iii-database`](https://workers.iii.dev/workers/iii-database) | SQL-backed state adapter when you outgrow the in-memory KV defaults |
| [`mcp`](https://workers.iii.dev/workers/mcp) | Stand up extra MCP servers next to agentmemory's, share the same engine |

完整注册表：[workers.iii.dev](https://workers.iii.dev)。那里的每个 worker 都通过 agentmemory 使用的相同原语进行组合 — 而你已经拥有的 agentmemory 就是其中之一。

### iii 替代了什么 (What iii replaces)

| Traditional stack | agentmemory uses |
|---|---|
| Express.js / Fastify | iii HTTP Triggers |
| SQLite / Postgres + pgvector | iii KV State + in-memory vector index |
| SSE / Socket.io | iii Streams (WebSocket) |
| pm2 / systemd | iii engine worker supervision |
| Prometheus / Grafana | iii OTEL + health monitor |
| Custom plugin systems | `iii worker add <name>` |

**174 个源文件 · ~37,800 LOC · 1,390+ 测试 · 258 函数 · 44 KV 作用域** — 全部基于三个原语。没有 `agentmemory plugin install`。插件系统就是 iii 本身。

---

<h2 id="configuration"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-config.svg"><img src="assets/tags/section-config.svg" alt="Configuration" height="32" /></picture></h2>

### LLM 提供商 (LLM Providers)

agentmemory 从你的环境中自动检测。默认情况下，除非你配置了提供商或明确选择加入 Claude 订阅回退，否则不会进行任何 LLM 调用。

| Provider | Config | Notes |
|----------|--------|-------|
| **No-op (default)** | No config needed | LLM-backed compress/summarize is DISABLED. Synthetic BM25 compression + recall still work. See `AGENTMEMORY_ALLOW_AGENT_SDK` below if you used to rely on the Claude-subscription fallback. |
| Anthropic API | `ANTHROPIC_API_KEY` | Per-token billing |
| MiniMax | `MINIMAX_API_KEY` | Anthropic-compatible |
| Gemini | `GEMINI_API_KEY` | Also enables embeddings |
| OpenRouter | `OPENROUTER_API_KEY` | Any model |
| OpenAI API | `OPENAI_API_KEY` | Default `gpt-4o-mini`, override with `OPENAI_MODEL` |
| **Local (Ollama / LM Studio / vLLM / llama.cpp)** | `OPENAI_API_KEY=local` + `OPENAI_BASE_URL=http://localhost:11434/v1` (Ollama) or `http://localhost:1234/v1` (LM Studio) + `OPENAI_MODEL=<your model>` | Anything OpenAI-API-compatible. Zero cost, runs on your hardware. See [Local models](#local-models-ollama-lm-studio-vllm) below. |
| Claude subscription fallback | `AGENTMEMORY_ALLOW_AGENT_SDK=true` | Opt-in only. Spawns `@anthropic-ai/claude-agent-sdk` sessions — used to cause unbounded Stop-hook recursion (#149 follow-up) so it is no longer the default. |

### 本地模型 (Ollama / LM Studio / vLLM)

agentmemory 与任何 OpenAI API 兼容的服务器通信，因此任何暴露 `/v1/chat/completions` 的东西都可以正常工作而无需更改代码。没有付费密钥、没有云、没有限速 — 完全在你的硬件上运行。

**Ollama** (默认端口 `11434`)：

```bash
ollama pull qwen2.5-coder:7b   # or llama3.2:3b, mistral:7b, etc.
ollama serve
```

```env
# ~/.agentmemory/.env
OPENAI_API_KEY=ollama                          # any non-empty string; Ollama ignores it
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_MODEL=qwen2.5-coder:7b
```

**LM Studio** (默认端口 `1234`)：

打开 LM Studio → Local Server 选项卡 → Start Server。从选择器中选择一个聊天模型（Qwen 2.5 Coder, Llama 3.2, DeepSeek 等）。

```env
# ~/.agentmemory/.env
OPENAI_API_KEY=lmstudio                        # any non-empty string; LM Studio ignores it
OPENAI_BASE_URL=http://localhost:1234/v1
OPENAI_MODEL=qwen2.5-coder-7b-instruct         # match the model name from LM Studio
```

**vLLM / llama.cpp / Text Generation Inference：** 相同的形状 — 将 `OPENAI_BASE_URL` 指向你的服务器暴露的任何 URL，设置 `OPENAI_MODEL` 为你的服务器接受的名字。

**记忆工作的模型选择：** 压缩和摘要都是短任务（输入 <2K token，输出 <500 token），其中 7B 指令模型绰绰有余。推荐：

| Model | Size | Why |
|-------|------|-----|
| `qwen2.5-coder:7b` | ~4.7 GB | Best at code-shaped sessions; trained on programming + tool-use traces |
| `llama3.2:3b` | ~2 GB | Smallest sane option — fine for compression, weaker for graph extraction |
| `mistral:7b-instruct` | ~4.4 GB | Good general-purpose baseline if you don't want code-specific |
| `deepseek-r1:7b` | ~4.7 GB | Reasoning-tier quality at 7B; slower but cleaner extractions |

推理类模型（带有 `<think>` 块的 `o1`-style）可能会返回空的 `content` 和一个你的本地服务器可能不显示的 `reasoning` 字段。如果提取结果为空，请先切换到非推理模型。环境变量 `OPENAI_REASONING_EFFORT=none` 也可以禁用 Ollama Cloud 推理模型的思考功能（它们镜像了 OpenAI 的推理模式）。

本地嵌入通过 `@xenova/transformers` 开箱即用 — `EMBEDDING_PROVIDER=local`（默认）为你提供完全在设备上的 BGE-small。无需额外配置。

### 成本感知的模型选择 (Cost-aware model selection)

后台压缩会在每次观测时运行，因此模型选择会显著改变每月的支出。捕获的工作负载数据：635 次请求 / 888K token / 35 小时活跃使用，在三个 OpenRouter 模型上以 2026-05-23 的价格运行。

| Tier | Model | Input / 1M | Output / 1M | Cost for the captured 35h | Notes |
|------|-------|------------|-------------|---------------------------|-------|
| Recommended | `deepseek/deepseek-v4-pro` | $0.435 | $0.87 | ~$0.46 | Solid compression + summarization quality at ~10× lower cost than Sonnet. |
| Recommended | `deepseek/deepseek-chat` | $0.27 | $1.10 | ~$0.40 | Older but still fine for compression-only workloads. |
| Recommended | `qwen/qwen3-coder` | $0.45 | $1.80 | ~$0.55 | Strong code reasoning if your sessions are heavily code-shaped. |
| Premium | `anthropic/claude-sonnet-4.6` | $3.00 | $15.00 | ~$5.02 | High quality but expensive for always-on background work. |
| Premium | `openai/gpt-4o` | $2.50 | $10.00 | ~$4.20 | Similar tier to Sonnet. |
| Avoid | `anthropic/claude-opus-4.6` | $15.00 | $75.00 | ~$25+ | Reasoning-class model; massive overspend for compression. |

当 `OPENROUTER_MODEL` 匹配高级模式时，agentmemory 会打印运行时警告。设置 `AGENTMEMORY_SUPPRESS_COST_WARNING=1` 以在你做出明智选择后静音。

记忆工作的质量与成本权衡：压缩是一个具有相对宽松质量标准的摘要任务（代理重读摘要，而不是用户）。DeepSeek-V4-Pro / Qwen3-Coder 在此任务上的表现与 Sonnet 在舍入误差范围内，而成本约为其十分之一。将高级模型保存为你直接阅读的查询中。

来源：[OpenRouter pricing for Sonnet 4.6](https://openrouter.ai/anthropic/claude-sonnet-4.6/pricing), [DeepSeek V4 Pro](https://openrouter.ai/deepseek/deepseek-v4-pro), [DeepSeek pricing notes](https://api-docs.deepseek.com/quick_start/pricing/)。

### 多代理记忆 (`AGENT_ID` + `AGENTMEMORY_AGENT_SCOPE`)

在多个角色共享一个 agentmemory 服务器的多代理设置中（架构师 / 开发者 / 审查者 / 研究员 / 支持代理），`AGENT_ID` 用角色标签标记每次写入。`AGENTMEMORY_AGENT_SCOPE` 控制召回是否按该标签过滤。

```env
TEAM_ID=company
USER_ID=engineering-team
AGENT_ID=architect
AGENTMEMORY_AGENT_SCOPE=isolated  # optional; default "shared"
```

两种模式：

| Mode | Tag writes | Filter recall | When to use |
|------|------------|---------------|-------------|
| `shared` (default) | yes | no | Cross-agent context with audit trail. Architect can see what developer noted, but every row records who said it. |
| `isolated` | yes | yes | Strict separation. Architect never sees developer's observations / memories / sessions. |

当设置 `AGENT_ID` 时标记的内容：`Session.agentId`, `RawObservation.agentId`, `CompressedObservation.agentId`, `Memory.agentId`。角色从 `api::session::start` → `mem::observe` → `mem::compress` → KV 流动。

隔离模式下过滤的内容：`mem::smart-search`, `/agentmemory/memories`, `/agentmemory/observations`, `/agentmemory/sessions`。每个端点接受 `?agentId=<role>` 以覆盖每次请求，以及 `?agentId=*` 以完全退出环境变量范围。`/memories` 还接受 `?includeOrphans=true` 以显示其 `agentId` 为 undefined 的预 AGENT_ID 记忆。

SDK / REST 层的每次调用覆盖：每个可变端点（`/session/start`, `/remember`）在请求体中接受一个 `agentId` 字段，该字段优于环境变量。适用于将许多角色路由到一个服务器进程的运行环境。

当未设置 `AGENT_ID` 时，记忆保持无作用域（遗留行为，无标签，无过滤器）。

### 端口 (Ports)

agentmemory + iii-engine 默认绑定四个端口。如果重启失败并显示 `port in use`，此表告诉你应该查找哪个进程。

| Port | Process | Purpose | Env override |
|------|---------|---------|--------------|
| `3111` | agentmemory | REST API + MCP HTTP + `/agentmemory/health` + `/agentmemory/livez` | `III_REST_PORT` |
| `3112` | iii-engine | Internal streams worker (consumed by agentmemory + viewer) | `III_STREAMS_PORT` |
| `3113` | agentmemory | Real-time viewer (`http://localhost:3113`) | `AGENTMEMORY_VIEWER_PORT` |
| `49134` | iii-engine | WebSocket — workers register here, OTel telemetry flows over it | `III_ENGINE_URL` (full URL, default `ws://localhost:49134`) |

当崩溃运行后端口保持绑定时清理残留进程：

```bash
# macOS / Linux — find whatever is on each port and kill it
lsof -i :3111,3112,3113,49134
pkill -f agentmemory || true
pkill -f 'iii ' || true

# Windows
netstat -ano | findstr ":3111 :3112 :3113 :49134"
taskkill /F /PID <pid>
```

`agentmemory stop` 在优雅关闭时干净地回收 worker 和引擎 pidfile（#640, #474）。上述手动清理仅用于既没有留下任何 pidfile 的崩溃后情况。

### 配置文件 (Config File)

将 agentmemory 运行时配置放在 `~/.agentmemory/.env` 中，而不是在每个 shell 中导出变量。如果查看器显示类似 `export ANTHROPIC_API_KEY=...` 的设置提示，将其复制到此文件中作为 `ANTHROPIC_API_KEY=...`（不带 `export` 前缀），然后重启 agentmemory。

进程环境变量仍然有效并优先于文件中的值。

在 Windows 上，同一文件位于 `%USERPROFILE%\.agentmemory\.env`：

```powershell
New-Item -ItemType Directory -Force $HOME\.agentmemory
notepad $HOME\.agentmemory\.env
```

要使用 Claude Code Pro/Max 订阅而不是 API Key 进行测试，请明确选择加入：

```env
AGENTMEMORY_ALLOW_AGENT_SDK=true
AGENTMEMORY_AUTO_COMPRESS=true
```

只要配置了 LLM 提供商，整合（图节点、课程、晶体）默认就是开启的。如果你想要无 LLM 操作，请使用 `CONSOLIDATION_ENABLED=false` 明确退出。图形提取是一个单独的标志：

```env
GRAPH_EXTRACTION_ENABLED=true
# CONSOLIDATION_ENABLED=false   # opt out of auto-consolidation
```

### 环境变量 (Environment Variables)

创建 `~/.agentmemory/.env`：

```env
# LLM provider (pick one — default is the no-op provider: no LLM calls)
# ANTHROPIC_API_KEY=sk-ant-...
# ANTHROPIC_BASE_URL=...              # Optional: Anthropic-compatible proxy / Azure
# GEMINI_API_KEY=...
# OPENROUTER_API_KEY=...
# MINIMAX_API_KEY=...
# OPENAI_API_KEY=***                       # NOTE: this same key auto-activates BOTH the
#                                          # OpenAI LLM provider (here) AND the OpenAI
#                                          # embedding provider (further below). Set
#                                          # OPENAI_API_KEY_FOR_LLM=false to scope it
#                                          # to embeddings only.
# OPENAI_BASE_URL=https://api.openai.com   # Optional: override for Azure / vLLM / LM Studio / proxies
#                                          # Azure: https://<resource>.openai.azure.com/openai/deployments/<deployment>
#                                          # Auto-detected from `.openai.azure.com` hostname; uses
#                                          # api-key header + api-version query param.
# OPENAI_API_VERSION=2024-08-01-preview    # Optional: Azure api-version query param
# OPENAI_MODEL=gpt-4o-mini                 # Optional: default model
# OPENAI_TIMEOUT_MS=60000                  # Optional: OpenAI-scoped alias for the outbound fetch
#                                          # timeout. Takes precedence over AGENTMEMORY_LLM_TIMEOUT_MS
#                                          # for back-compat with v0.9.17. New configs should
#                                          # prefer the global AGENTMEMORY_LLM_TIMEOUT_MS below.
# OPENAI_REASONING_EFFORT=none             # Optional: "low" | "medium" | "high" | "none"
#                                          # Honored only by OpenAI's reasoning models (o1, o3,
#                                          # gpt-*-reasoning) and providers that mirror that
#                                          # schema (Ollama Cloud thinking models). Standard
#                                          # chat models reject this field with 400. Set to
#                                          # "none" for thinking models that return reasoning
#                                          # but no content.
# OPENAI_API_KEY_FOR_LLM=false             # Optional: set to false to skip OpenAI auto-detection
#                                          # for LLM (useful if you only want OpenAI for embeddings)
# Opt-in Claude-subscription fallback (spawns @anthropic-ai/claude-agent-sdk);
# leave OFF unless you understand the Stop-hook recursion risk (#149 follow-up):
# AGENTMEMORY_ALLOW_AGENT_SDK=true

# Embedding provider (auto-detected, or override)
# EMBEDDING_PROVIDER=local
# VOYAGE_API_KEY=...
# OPENAI_API_KEY=sk-...
# OPENAI_BASE_URL=https://api.openai.com   # Override for Azure / vLLM / LM Studio / proxies
# OPENAI_EMBEDDING_MODEL=text-embedding-3-small
# OPENAI_EMBEDDING_DIMENSIONS=1536        # Required when the model is not in the known-models table

# Outbound LLM / embedding timeout
# AGENTMEMORY_LLM_TIMEOUT_MS=60000       # Default: 60 000 ms (60 s). Applies to every
                                          # raw-fetch provider (Gemini, OpenRouter, MiniMax,
                                          # OpenAI LLM, OpenAI/Cohere/Voyage/OpenRouter
                                          # embedding). For the OpenAI LLM path, the
                                          # OpenAI-scoped OPENAI_TIMEOUT_MS alias (above)
                                          # takes precedence when set, for back-compat
                                          # with v0.9.17.
                                          # Increase for slow networks or large batch calls;
                                          # decrease to fail-fast on rate-limit holds.

# Search tuning
# BM25_WEIGHT=0.4
# VECTOR_WEIGHT=0.6
# TOKEN_BUDGET=2000

# Auth
# AGENTMEMORY_SECRET=your-secret

# Ports (defaults: 3111 API, 3113 viewer)
# III_REST_PORT=3111

# Features
# AGENTMEMORY_AUTO_COMPRESS=false  # OFF by default (#138). When on,
                                   # every PostToolUse hook calls your
                                   # LLM provider to compress the
                                   # observation — expect significant
                                   # token spend on active sessions.
# AGENTMEMORY_SLOTS=false          # OFF by default. Editable pinned
                                   # memory slots — persona,
                                   # user_preferences, tool_guidelines,
                                   # project_context, guidance,
                                   # pending_items, session_patterns,
                                   # self_notes. Size-limited; agent
                                   # edits via memory_slot_* tools.
                                   # Pinned slots addressable for
                                   # SessionStart injection.
# AGENTMEMORY_REFLECT=false        # OFF by default. Requires SLOTS=on.
                                   # Stop hook fires mem::slot-reflect:
                                   # scans recent observations, auto-
                                   # appends TODOs to pending_items,
                                   # counts patterns in
                                   # session_patterns, records touched
                                   # files in project_context. Fire-
                                   # and-forget; does not block.
# AGENTMEMORY_INJECT_CONTEXT=false # OFF by default (#143). When on:
                                   # - SessionStart may inject ~1-2K
                                   #   chars of project context into
                                   #   the first turn of each session
                                   #   (this is what actually reaches
                                   #   the model — Claude Code treats
                                   #   SessionStart stdout as context)
                                   # - PreToolUse fires /agentmemory/enrich
                                   #   on every file-touching tool call
                                   #   (resource cleanup, not a token
                                   #   fix — PreToolUse stdout is debug
                                   #   log only per Claude Code docs)
                                   # Observations are still captured via
                                   # PostToolUse regardless of this flag.
# GRAPH_EXTRACTION_ENABLED=false
# CONSOLIDATION_ENABLED=false   # on by default when an LLM provider is configured
# LESSON_DECAY_ENABLED=true
# OBSIDIAN_AUTO_EXPORT=false
# AGENTMEMORY_EXPORT_ROOT=~/.agentmemory
# CLAUDE_MEMORY_BRIDGE=false
# SNAPSHOT_ENABLED=false

# Team
# TEAM_ID=
# USER_ID=
# TEAM_MODE=private

# Tool visibility: "core" (8 tools, lean fallback) or "all" (53 tools)
# AGENTMEMORY_TOOLS=core
```

---

<h2 id="api"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-api.svg"><img src="assets/tags/section-api.svg" alt="API" height="32" /></picture></h2>

端口 `3111` 上的 128 个端点。REST API 默认绑定到 `127.0.0.1`。当设置 `AGENTMEMORY_SECRET` 时，受保护的端点需要 `Authorization: Bearer <secret>`，且网格同步端点在两个对等方上都需要 `AGENTMEMORY_SECRET`。

<details>
<summary>Key endpoints</summary>

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/agentmemory/health` | Health check (always public) |
| `POST` | `/agentmemory/session/start` | Start session + get context |
| `POST` | `/agentmemory/session/end` | End session |
| `POST` | `/agentmemory/observe` | Capture observation |
| `POST` | `/agentmemory/smart-search` | Hybrid search |
| `POST` | `/agentmemory/context` | Generate context |
| `POST` | `/agentmemory/remember` | Save to long-term memory |
| `POST` | `/agentmemory/forget` | Delete observations |
| `POST` | `/agentmemory/enrich` | File context + memories + bugs |
| `GET` | `/agentmemory/profile` | Project profile |
| `GET` | `/agentmemory/export` | Export all data |
| `POST` | `/agentmemory/import` | Import from JSON |
| `POST` | `/agentmemory/graph/query` | Knowledge graph query |
| `POST` | `/agentmemory/team/share` | Share with team |
| `GET` | `/agentmemory/audit` | Audit trail |

Full endpoint list: [`src/triggers/api.ts`](src/triggers/api.ts)

</details>

---

<h2 id="development"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-development.svg"><img src="assets/tags/section-development.svg" alt="Development" height="32" /></picture></h2>

```bash
npm run dev               # Hot reload
npm run build             # Production build
npm test                  # 1,390+ tests
npm run test:integration  # API tests (requires running services)
```

**前置条件：** Node.js >= 20，[iii-engine](https://iii.dev/docs) 或 Docker

<h2 id="license"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tags/light/section-license.svg"><img src="assets/tags/section-license.svg" alt="License" height="32" /></picture></h2>

[Apache-2.0](LICENSE)