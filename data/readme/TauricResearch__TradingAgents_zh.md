<p align="center">
  <img src="assets/TauricResearch.png" style="width: 60%; height: auto;">
</p>

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2412.20138" target="_blank"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2412.20138-B31B1B?logo=arxiv"/></a>
  <a href="https://discord.com/invite/hk9PGKShPK" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-TradingResearch-7289da?logo=discord&logoColor=white&color=7289da"/></a>
  <a href="./assets/wechat.png" target="_blank"><img alt="WeChat" src="https://img.shields.io/badge/WeChat-TauricResearch-brightgreen?logo=wechat&logoColor=white"/></a>
  <a href="https://x.com/TauricResearch" target="_blank"><img alt="X Follow" src="https://img.shields.io/badge/X-TauricResearch-white?logo=x&logoColor=white"/></a>
  <br>
  <a href="https://github.com/TauricResearch/" target="_blank"><img alt="Community" src="https://img.shields.io/badge/Join_GitHub_Community-TauricResearch-14C290?logo=discourse"/></a>
</div>

<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=de">Deutsch</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=es">Español</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=fr">français</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ja">日本語</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ko">한국어</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=pt">Português</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ru">Русский</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=zh">中文</a>
</div>

---

# TradingAgents：基于多智能体大语言模型的金融交易框架

## 更新日志
- [2026-05] 发布 **TradingAgents v0.2.5**，新增接地气的情绪分析师（Sentiment Analyst）、支持 GPT-5.5 等模型、Qwen/GLM/MiniMax 双区域支持、`TRADINGAGENTS_*` 环境变量配置及 API Key 自动检测、远程 Ollama 支持、非美股 Alpha 基准测试，以及 Ticker 路径遍历加固。完整列表请参见 [CHANGELOG.md](CHANGELOG.md)。
- [2026-04] 发布 **TradingAgents v0.2.4**，新增结构化输出智能体（研究经理、交易员、投资组合经理）、LangGraph 断点续跑支持、持久化决策日志、DeepSeek/Qwen/GLM/Azure 提供商支持、Docker 部署及 Windows UTF-8 编码修复。
- [2026-03] 发布 **TradingAgents v0.2.3**，新增多语言支持、GPT-5.4 系列模型、统一模型目录、回测日期保真度提升及代理（Proxy）支持。
- [2026-03] 发布 **TradingAgents v0.2.2**，新增 GPT-5.4/Gemini 3.1/Claude 4.6 模型覆盖、五级评分体系、OpenAI Responses API、Anthropic 算力控制及跨平台稳定性优化。
- [2026-02] 发布 **TradingAgents v0.2.0**，新增多提供商 LLM 支持（GPT-5.x, Gemini 3.x, Claude 4.x, Grok 4.x）并重构系统架构。
- [2026-01] 发布 **Trading-R1** [技术报告](https://arxiv.org/abs/2509.11420)，[Terminal](https://github.com/TauricResearch/Trading-R1) 预计即将上线。

<div align="center">
<a href="https://www.star-history.com/#TauricResearch/TradingAgents&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" />
   <img alt="TradingAgents Star History" src="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" style="width: 80%; height: auto;" />
 </picture>
</a>
</div>

> 🎉 **TradingAgents** 正式发布！我们收到了大量关于该项目的咨询，在此感谢社区的热情关注。
>
> 因此我们决定将框架完全开源。期待与你共同打造具有影响力的项目！

<div align="center">

🚀 [TradingAgents](#tradingagents-framework) | ⚡ [安装与 CLI](#installation-and-cli) | 🎬 [演示视频](https://www.youtube.com/watch?v=90gr5lwjIho) | 📦 [包调用示例](#tradingagents-package) | 🤝 [贡献指南](#contributing) | 📄 [引用格式](#citation)

</div>

## TradingAgents 框架介绍

TradingAgents 是一个多智能体交易框架，模拟了真实交易公司的运作机制。通过部署由大语言模型（LLM）驱动的专业智能体：从基本面分析师、情绪专家和技术分析师，到交易员和风险管理团队，平台协同评估市场状况并辅助交易决策。此外，这些智能体会进行动态讨论，以锁定最优策略。

<p align="center">
  <img src="assets/schema.png" style="width: 100%; height: auto;">
</p>

> TradingAgents 框架专为研究目的设计。实际交易表现可能受多种因素影响（包括选用的基础语言模型、模型温度参数、交易周期、数据质量及其他非确定性因素）。[本项目不构成任何金融、投资或交易建议。](https://tauric.ai/disclaimer/)

我们的框架将复杂的交易任务拆解为专业化的角色分工：

### 分析师团队 (Analyst Team)
- **基本面分析师**：评估公司财务与绩效指标，识别内在价值与潜在风险信号（red flags）。
- **情绪分析师**：整合新闻标题、StockTwits 和 Reddit 讨论，生成综合情绪读数以把握短期市场情绪。
- **新闻分析师**：监控全球新闻与宏观经济指标，解读重大事件对市场状况的影响。
- **技术分析师**：利用技术指标（如 MACD 和 RSI）检测交易模式并预测价格走势。

<p align="center">
  <img src="assets/analyst.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

### 研究员团队 (Researcher Team)
- 由多头和空头研究员组成，对分析师团队提供的见解进行批判性评估。通过结构化辩论，平衡潜在收益与固有风险。

<p align="center">
  <img src="assets/researcher.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### 交易员智能体 (Trader Agent)
- 综合分析师和研究员的报告以做出明智的交易决策，确定交易的时机与规模。

<p align="center">
  <img src="assets/trader.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### 风险管理与投资组合经理 (Risk Management and Portfolio Manager)
- 通过评估市场波动性、流动性及其他风险因素，持续监控投资组合风险。风险管理团队负责评估和调整交易策略，并向投资组合经理提供评估报告以做出最终决策。
- 投资组合经理负责审批/拒绝交易提案。若获批准，订单将发送至模拟交易所并执行。

<p align="center">
  <img src="assets/risk.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

## 安装与 CLI 使用

### 安装步骤

克隆 TradingAgents：
```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
```

使用你喜欢的环境管理工具创建虚拟环境：
```bash
conda create -n tradingagents python=3.13
conda activate tradingagents
```

安装包及其依赖项：
```bash
pip install .
```

### Docker 部署

或者，通过 Docker 运行：
```bash
cp .env.example .env  # 添加你的 API Keys
docker compose run --rm tradingagents
```

使用本地 Ollama 模型：
```bash
docker compose --profile ollama run --rm tradingagents-ollama
```

### 所需 API Key

TradingAgents 支持多个 LLM 提供商。请为你选择的提供商设置对应的 API Key：

```bash
export OPENAI_API_KEY=...          # OpenAI (GPT)
export GOOGLE_API_KEY=...          # Google (Gemini)
export ANTHROPIC_API_KEY=...       # Anthropic (Claude)
export XAI_API_KEY=...             # xAI (Grok)
export DEEPSEEK_API_KEY=...        # DeepSeek
export DASHSCOPE_API_KEY=...       # Qwen — 国际版 (dashscope-intl.aliyuncs.com)
export DASHSCOPE_CN_API_KEY=...    # Qwen — 国内版 (dashscope.aliyuncs.com)
export ZHIPU_API_KEY=...           # GLM via Z.AI (国际版)
export ZHIPU_CN_API_KEY=...        # GLM via BigModel (国内版, open.bigmodel.cn)
export MINIMAX_API_KEY=...         # MiniMax — 全球版 (api.minimax.io, M2.x, 204K ctx)
export MINIMAX_CN_API_KEY=...      # MiniMax — 国内版 (api.minimaxi.com, M2.x, 204K ctx)
export OPENROUTER_API_KEY=...      # OpenRouter
export ALPHA_VANTAGE_API_KEY=...   # Alpha Vantage
```

对于企业级提供商（如 Azure OpenAI、AWS Bedrock），复制 `.env.enterprise.example` 至 `.env.enterprise` 并填入你的凭证。

对于本地模型，在配置中设置 `llm_provider: "ollama"`。默认端点为 `http://localhost:11434/v1`；可通过环境变量 `OLLAMA_BASE_URL` 指向远程 `ollama-serve`。使用 `ollama pull <name>` 拉取模型，并在 CLI 中选择“Custom model ID”以启用未预置的模型。

或者，复制 `.env.example` 至 `.env` 并填入你的密钥：
```bash
cp .env.example .env
```

### CLI 使用指南

启动交互式命令行界面：
```bash
tradingagents          # 已安装的命令
python -m cli.main     # 备选方案：直接从源码运行
```
你将看到一个交互界面，可在此选择目标 Ticker、分析日期、LLM 提供商、研究深度等参数。

### 市场与 Ticker 支持

TradingAgents 支持 Yahoo Finance 覆盖的所有市场，使用带交易所后缀的 Ticker 格式。公司身份识别与 Alpha 基准会根据所选市场自动解析：

- 美股：`AAPL`, `SPY`
- 港股：`0700.HK` · 东京：`7203.T` · 伦敦：`AZN.L`
- 印度：`RELIANCE.NS`, `.BO` · 加拿大：`.TO` · 澳大利亚：`.AX`
- A股：沪市 `.SS`，深市 `.SZ`（例如贵州茅台 `600519.SS`）
- 加密货币：`BTC-USD`, `ETH-USD`

<p align="center">
  <img src="assets/cli/cli_init.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

界面会实时显示加载结果，方便你跟踪智能体的运行进度。

<p align="center">
  <img src="assets/cli/cli_news.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

<p align="center">
  <img src="assets/cli/cli_transaction.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

## TradingAgents 包调用示例

### 实现细节

我们使用 LangGraph 构建了 TradingAgents，以确保灵活性和模块化。该框架支持多个 LLM 提供商：OpenAI、Google、Anthropic、xAI、DeepSeek、Qwen（阿里云 DashScope，国际与中国节点）、GLM（智谱）、MiniMax（全球+中国）、OpenRouter、Ollama（本地模型）以及 Azure OpenAI（企业级）。

### Python 调用示例

若要在代码中使用 TradingAgents，可导入 `tradingagents` 模块并初始化 `TradingAgentsGraph()` 对象。`.propagate()` 函数将返回交易决策。你可以运行 `main.py`，以下为快速使用示例：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# forward propagate
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

你也可通过修改默认配置来自定义 LLM 选择、辩论轮次等参数：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"        # openai, google, anthropic, xai, deepseek, qwen, qwen-cn, glm, glm-cn, minimax, minimax-cn, openrouter, ollama, azure
config["deep_think_llm"] = "gpt-5.5"     # 复杂推理模型
config["quick_think_llm"] = "gpt-5.4-mini" # 快速任务模型
config["max_debate_rounds"] = 2

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

所有配置选项详见 `tradingagents/default_config.py`。

## 状态持久化与断点恢复

TradingAgents 会在多次运行间持久化两类状态：

### 决策日志 (Decision log)

决策日志默认开启。每次完整运行结束后，其决策结果会自动追加至 `~/.tragingagents/memory/trading_memory.md`。下次针对同一 Ticker 运行时，TradingAgents 会获取已实现的收益率（原始收益及相对于 SPY 的 Alpha），生成一段反思摘要，并将最近同 Ticker 的决策记录与近期的跨 Ticker 经验注入投资组合经理的 Prompt 中，使每次分析都能继承历史的有效经验与教训。

可通过环境变量 `TRADINGAGENTS_MEMORY_LOG_PATH` 覆盖日志路径。

### 断点续跑 (Checkpoint resume)

通过添加 `--checkpoint` 参数可启用此功能（默认关闭）。启用后，LangGraph 会在每个节点执行完毕后保存状态快照；若运行崩溃或中断，下次启动将从最后一个成功步骤继续，而非从头开始。在日志中，恢复运行会显示 `Resuming from step N for <TICKER> on <date>`，全新运行则显示 `Starting fresh`。任务成功后会自动清理检查点文件。

每个 Ticker 的 SQLite 数据库位于 `~/.tradingagents/cache/checkpoints/<TICKER>.db`（可通过环境变量 `TRADINGAGENTS_CACHE_DIR` 覆盖基础路径）。使用 `--clear-checkpoints` 可在运行前重置所有快照。

```bash
tradingagents analyze --checkpoint           # 本次运行启用断点续跑
tradingagents analyze --clear-checkpoints    # 运行前清空所有快照
```

```python
config = DEFAULT_CONFIG.copy()
config["checkpoint_enabled"] = True
ta = TradingAgentsGraph(config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
```

## 可复现性说明

TradingAgents 由大语言模型驱动，因此针对同一 Ticker 和日期的两次运行结果可能不同。这是基于语言模型构建的研究工具的预期行为，并非缺陷。差异主要来源于以下几个方面：

**语言模型采样的非确定性**：即使在固定温度参数下，各提供商也无法保证多次调用的输出字节完全一致。推理模型（默认的 GPT-5.x 系列及任何思考模式模型）波动最大，因为其内部推理过程本身也是基于采样生成的。

**实时数据动态变化**：新闻、StockTwits 和 Reddit 的内容会随时间推移而更新。因此，即使针对相同的历史交易日期，本周的运行输入与上周也会不同。虽然分析日期已固定以锁定价格和技术指标窗口，但社交媒体与新闻源仍反映的是“当前”状态。

为降低结果波动，你可尝试调低采样温度参数。在配置中设置 `temperature`（或 `.env` 中的 `TRADINGAGENTS_TEMPERATURE`）；较低的值会使支持该参数的模型输出更稳定。推理模型通常忽略温度参数，因此若追求更高的可复现性，建议搭配非推理模型使用，例如 `gpt-4.1`。

```python
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"
config["deep_think_llm"] = "gpt-4.1"      # 非推理模型会严格遵循温度参数
config["quick_think_llm"] = "gpt-4.1"
config["temperature"] = 0.0
```

**已消除的变量来源**：分析对象的公司身份会在任何智能体运行前通过 Ticker 确定性解析；市场分析师的数据快照会严格锚定精确的价格与指标数值。早期反馈中提到的“不同公司”或跨次运行价格虚报问题，已通过上述两项机制解决。

回测结果不保证与任何公开文献数据完全一致。收益率表现取决于模型选择、温度参数、日期范围、数据质量及上述采样特性。请将本框架视为研究多智能体分析架构的科研脚手架，而非具有固定可复现收益的交易策略。

## 贡献指南 (Contributing)

欢迎提交贡献：包括 Bug 修复、文档完善及功能建议；过往贡献者将在每次发布的 [`CHANGELOG.md`](CHANGELOG.md) 中署名致谢。

## 引用格式 (Citation)

如果你发现 *TradingAgents* 对你的研究有所帮助，请引用我们的工作 :)

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework}, 
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138}, 
}
```