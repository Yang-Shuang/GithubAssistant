<p align="center">
  <b>English</b> | <a href="README_zh.md">中文</a> | <a href="README_ja.md">日本語</a> | <a href="README_ko.md">한국어</a> | <a href="README_ar.md">العربية</a>
</p>

<p align="center">
  <img src="assets/icon.png" width="120" alt="Vibe-Trading Logo"/>
</p>

<h1 align="center">Vibe-Trading：你的个人交易代理</h1>

<p align="center">
  <b>一条命令为你的代理赋予全面的交易能力</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=flat" alt="FastAPI">
  <img src="https://img.shields.io/badge/Frontend-React%2019-61DAFB?style=flat&logo=react&logoColor=white" alt="React">
  <a href="https://pypi.org/project/vibe-trading-ai/"><img src="https://img.shields.io/pypi/v/vibe-trading-ai?style=flat&logo=pypi&logoColor=white" alt="PyPI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=flat" alt="License"></a>
  <br>
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat-square&logo=feishu&logoColor=white" alt="Feishu"></a>
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat-square&logo=wechat&logoColor=white" alt="WeChat"></a>
  <a href="https://discord.gg/2vDYc2w5"><img src="https://img.shields.io/badge/Discord-Join-7289DA?style=flat-square&logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <a href="#官网">官网</a> &nbsp;&middot;&nbsp;
  <a href="#文档">文档</a> &nbsp;&middot;&nbsp;
  <a href="#-news">动态</a> &nbsp;&middot;&nbsp;
  <a href="#-key-features">功能特性</a> &nbsp;&middot;&nbsp;
  <a href="#-shadow-account">影子账户</a> &nbsp;&middot;&nbsp;
  <a href="#-demo">演示</a> &nbsp;&middot;&nbsp;
  <a href="#-quick-start">快速开始</a> &nbsp;&middot;&nbsp;
  <a href="#-examples">示例</a> &nbsp;&middot;&nbsp;
  <a href="#-api-server">API / MCP</a> &nbsp;&middot;&nbsp;
  <a href="#-roadmap">路线图</a> &nbsp;&middot;&nbsp;
  <a href="#-contributing">贡献指南</a>
</p>

<p align="center">
  <a href="#-quick-start"><img src="assets/pip-install.svg" height="45" alt="pip install vibe-trading-ai"></a>
</p>

---

## 📰 动态

- **2026-06-02** 🔌 **六大新增券商连接器（Tiger / Longbridge / Alpaca / OKX / Binance / Futu）**：以连接器为核心的交易层在原有 IBKR（本地）和 Robinhood（MCP）基础上，新增了直连 SDK 传输通道。每个连接器均暴露只读账户/持仓/订单/行情/历史数据 **以及仿真账户下单功能** —— 你可以在这些券商的仿真账户中测试策略。其中五个（Tiger、Alpaca、OKX、Binance、Futu）还遵循与 Robinhood 相同的安全模型，支持基于授权指令的门控下单：用户提交的指令范围（标的池/订单规模/敞口/杠杆/每日上限）、文件系统紧急停止开关、失败关闭型盘前风控门以及完整的审计账本。**Longbridge 仅支持仿真+只读**（其 API 未暴露运行时仿真/实盘的区分标识）。所有仿真与实盘的区分均由各券商的结构化守卫保障——账户 ID 格式、主机隔离、演示标志或交易环境。新增 `trading_place_order` / `trading_cancel_order` 工具；指令范围中增加了港股和 A 股资产类别。实验性功能，请自行评估风险后使用。
- **2026-06-01** 🚀 **v0.1.9 发布**（`pip install -U vibe-trading-ai`）：汇总了自 0.1.8 以来的所有更新。以连接器为核心的券商配置档案（IBKR 本地只读 TWS / IB Gateway + Robinhood Agentic Trading，后者基于 OAuth、授权指令、订单守卫、审计账本和即时熔断）。Research Goal 支持在 CLI / REST / MCP / Web 中跨运行时执行。蜂群(Swarm)增强——实时对账 + MCP keepalive、操作员配置的 Worker MCP 工具、严格的 Alpha 基准随机对照组，以及新增的 `retry_run` 用于重启失败/过期的任务（**现已拥有 36 个 MCP 工具**）。重构了 `agent/cli/` 包并刷新终端 UI，引入 `mootdx` 免 Token A 股加载器，并对回测/代理循环/会话进行了鲁棒性增强。`--version` 现在始终与已安装包匹配，修复了 0.1.8 的版本漂移问题（[#156](https://github.com/HKUDS/Vibe-Trading/issues/156)）。
- **2026-05-31** 🔌 **以连接器为核心的券商架构（IBKR + Robinhood）**：交易访问现在从可选的连接器配置档案开始，而非分散的券商/实盘入口。`vibe-trading connector list/use/check/account/positions/orders/quote/history` 与 MCP `trading_*` 工具共享同一选定配置，仿真/实盘作为连接器的属性存在。IBKR 可通过本地只读 TWS / IB Gateway 配置档案直接使用，而官方 IBKR 远程 MCP 路径已预置为 OAuth `mcp.read` 探针，等待稳定的读取工具名称上线。Robinhood Agentic Trading 仍作为基于 OAuth、授权指令、订单守卫、审计账本和即时熔断的受限实盘 MCP 连接器存在。
<details>
<summary>早期动态</summary>

- **2026-05-30** 🧰 **鲁棒性增强 —— 回测、代理循环、会话**：LLM 生成的信号引擎在实例化前现在会通过预飞行接口验证，捕获循环自导入、缺失的 `generate()`、非默认化的 `__init__` 参数以及错误的返回类型，并提供可操作的 JSON 错误而非原始堆栈跟踪（[#149](https://github.com/HKUDS/Vibe-Trading/pull/149)）；后续更新将源码级 AST 验证错误路由到相同的干净 JSON 信封中。代理循环不再将所有 50 次迭代全部消耗为无输出的 `failed` 状态——它在达到迭代预算的 80% 时镜像蜂群 Worker 的收尾提示，并在最后一次迭代时丢弃工具定义以强制输出最终文本答案（[#148](https://github.com/HKUDS/Vibe-Trading/pull/148)），且该逻辑被限制仅在运行中途触发，以免覆盖 Research Goal 上下文。会话消息写入现在对每次追加执行 `flush + fsync`，确保昂贵的 AI 响应能存活于写入中断的崩溃中；读取路径会跳过损坏的 JSONL 行（记录前 200 字符用于恢复），而不是直接让 `/messages` 端点返回 500 错误（[#147](https://github.com/HKUDS/Vibe-Trading/pull/147)）。Web 编辑器也修复了 IME Enter 键处理问题，避免在词组输入确认时意外提交（[#146](https://github.com/HKUDS/Vibe-Trading/pull/146)）。
- **2026-05-29** 🔐 **Robinhood Agentic Trading 支持（可选、受限自主性）**：新增对 Robinhood Agentic Trading 的支持（远程 MCP，OAuth）。默认关闭且仅只读；代理仅在用户提交的指令范围内行动（标的/订单规模/敞口/杠杆/每日上限），配备文件系统级即时停止开关、抢先平仓、指令自动过期、完整审计账本和持久化自主运行器。无托管、无交易场所——券商持有资金并执行交易，我们仅转发意图。实验性功能，请自行评估风险后使用。
- **2026-05-28** 🧪 **蜂群安全 + 严格 Alpha 门控 + Worker MCP**：当上游任务失败时，蜂群 DAG 会阻断下游任务（[#145](https://github.com/HKUDS/Vibe-Trading/pull/145)）。新增的 `run_bench_strict()` 增加了同标的池随机对照组 + OOS 划分，用于捕获仅跟踪市场 Beta 的因素（[#143](https://github.com/HKUDS/Vibe-Trading/pull/143)，感谢 @Soli22de）。蜂群 Worker 现在可以调用操作员配置的外部 MCP 服务器，并固定了信任边界（[#142](https://github.com/HKUDS/Vibe-Trading/pull/142)，感谢 @shadowinlife）。
- **2026-05-27** 📊 **mootdx A 股数据源 + 输出优化**：新增的 `mootdx` 加载器使用原生通达信 TCP 协议处理 A 股 OHLCV（无需认证、无 IP 限流，支持日线+分钟线及 25 页回卷分页），在降级链中位于 tushare 和 akshare 之间（[#107](https://github.com/HKUDS/Vibe-Trading/issues/107)）。CCXT 加载器现在读取 `HTTP_PROXY/HTTPS_PROXY/ALL_PROXY`，使受限网络下的 Binance/OKX 公共数据可用（[#126](https://github.com/HKUDS/Vibe-Trading/pull/126)，感谢 @ruok808）。最终答案渲染也去除了 CLI 和 Web 中丑陋的全角 `---` 水平分隔线：系统提示词现在引导代理使用 Markdown 表格和 `##` 标题，CLI 渲染器作为纵深防御剥离独立 HR，聊天气泡隐藏任何漏网的 `<hr>`（[#139](https://github.com/HKUDS/Vibe-Trading/issues/139)，感谢 @sdwxm188）。
- **2026-05-26** ✅ **Research Goal 生命周期闭环**：Goal 模式现在表现得像真正的任务执行器：Web UI 创建 Goal 会创建或绑定会话并立即发送启动轮次；活跃的 Goals 可在 Web/API/CLI/MCP 中继续、编辑、取消和完成；代理从当前 Goal 快照（标准、证据、声明、待办事项）推进，而非仅依赖原始提示词。已完成但仍活跃的目标现在进入审计/状态更新流程，而不是静默停止，并在后端、CLI、MCP 和前端事件上覆盖了回归测试。

- **2026-05-25** 🧼 **更清爽的聊天 UI + 编辑器工作流**：Web UI 使聊天聚焦于下一步操作：上传、蜂群和研究目标模式现在位于编辑器 `+` 菜单后，而非浮动面板。活跃上下文作为紧凑标签显示在输入框上方，目标详情仅在需要时内联展开。UI 还弃用了旧的自定义 i18n 层，改为直接使用英文文案；将完整报告卡片限制为符合报告标准的高质量任务；并加固了本地开发启动/状态报告以支持可靠的浏览器冒烟测试。
- **2026-05-24** 🎯 **Research Goal 运行时**：在后端、CLI、API/MCP、SSE 和 Web UI 中新增了会话级 Research Goal 层。Goals 持久化存储声明、验收标准、证据行、预算和完成策略；代理工具可创建 Goals 并附加证据；`/goal` 为 CLI 提供直接入口；REST/MCP 暴露目标快照和证据写入；SSE 保持聊天客户端实时刷新。后续审计修复锁定了已验证证据，通过代理工具拦截了实盘交易风险层级，将 CLI 创建的 Goals 接入后续轮次，在会话删除时清理目标账本，启用了全量回放，并修复了跨会话的前端竞态问题。
- **2026-05-23** 🖥️ **交互式 CLI 刷新**：终端入口现在展示更大的 Vibe-Trading Banner、更清爽的提示符分隔线、上一轮摘要、运行后耗时以及类 Claude Code 风格的实时活动轨道，用于代理工作。工具调用、网页/数据抓取、Shell 风格操作、Markdown 答案和管道表格以更易读的转录格式渲染；而管道或非 TTY 运行仍保持纯文本输出以适配自动化。生成的 CLI 截图现在被视为本地工件而非提交的文档文件，使仓库更轻量。
- **2026-05-22** 🧭 **蜂群恢复 + MCP keepalive**：蜂群状态现在在每次读取时从实时任务文件中对账，因此 API/MCP/SSE/列表视图可恢复崩溃或过期的运行，而非显示永久 `running` 快照。`run_swarm` 在轮询期间发送 MCP 进度心跳，并为断连后重连的客户端固定了首帧 `swarm_started run_id=<id>`；Worker 现在通过 LLM 流式传输、数据抓取和工具执行进行心跳。过期运行清理器使用每任务阈值并从任务状态推导终端状态，`SwarmTool` 不再因等待预算耗尽而取消仍在运行的团队，MCP 客户端可调用 `reap_stale_runs()` 进行显式清理。今日的 DX 增强还刷新了提供商默认模型，并使 CI 语法检查与新 `agent/cli/` 包对齐。22 项新回归测试覆盖水合、终端恢复、过期清理、keepalive 节奏、环境变量解析和心跳布线；完整的蜂群/MCP 套件通过 169 项，跳过 4 项。
- **2026-05-21** 🧱 **CLI 包重构**：`agent/cli.py`（3216 LOC）拆分为 `agent/cli/` 包——交互式入口、斜杠路由器、Rich 组件，以及保留所有子命令并重新导出每个公共符号的 `_legacy.py` 垫片，确保 `cli.cmd_*` / `cli._INIT_ENV_PATH` / `cli.Confirm` 继续可用。新增 FastAPI 中间件在浏览器直接访问 `/runs/{id}` 或 `/correlation` 时提供 SPA shell；Vite 开发代理也应用了相同的缩小策略。版本通过 `cli/_version.py` 统一（`--version` 与 Banner 不再漂移），`python -m cli` 通过 `__main__.py` 恢复，聊天门控已收紧，使 `chat --help` / `chat extra` 能正确路由到 legacy argparse 而非被 REPL 吞没。
- **2026-05-20** 🔬 **Hypothesis Registry CLI**：补全了仅在后端发布的 Hypothesis Registry（2026-05-16）的 CLI 侧功能。`vibe-trading hypothesis list` 输出 Rich 表格或 JSON（支持 `--status` 过滤、`--limit`）；`show <id>` 渲染包含链接运行卡片的详情面板；`invalidate <id> --note "..."` 将状态翻转为 `rejected`，若省略 `--note` 则保留先前的失效注释。兼容现有的 `VIBE_TRADING_HYPOTHESES_PATH` 环境变量覆盖，并新增每次调用的 `--path`。22 项新测试覆盖布线、JSON 输出、状态过滤、限制、缺失 ID 错误和注释持久化。
- **2026-05-19** ✨ **实时工具反馈 + 优雅取消**：长时间运行的工具（回测、大型 PDF、蜂群 Worker）不再看起来像卡死。每次工具调用现在都会发出 3 秒心跳及结构化分阶段进度——`run_backtest` 显示阶段标记（`validate` / `simulate` / `finalize`），`read_document` 在 PDF 上逐页跳动或在 Excel 上逐表跳动，`read_url` 标记 `fetch` / `parse`。CLI Rich Live 仪表板渲染 Unicode 旋转器、ASCII 进度条、ETA，并堆叠最多 3 个按名称键名的并行工具；前端聊天搭载新的 `ToolProgressIndicator`，采用 rAF 合并渲染、ARIA `role="status"` + 隐藏的 `<progress>` 供屏幕阅读器使用，并在已知总量时显示确定性 `ProgressRing` SVG。CLI 运行期间首次按下 `Ctrl+C` 现在调用 `agent.cancel()` 进行优雅退出（当前步骤完成，追踪干净关闭）；2 秒内第二次按下的强制退出。在此过程中提取了可复用原语：`ProgressBar.tsx` 和 `lib/tools.ts`（共享工具名称 i18n）。
- **2026-05-18** 🧹 **清理增强 + 三项潜在 Bug 修复**：`CompositeEngine` 不再将裸中国期货代码如 `RB2410` 错误路由到 `GlobalFuturesEngine`——`_is_china_futures` 移至共享的 `_market_hooks` 模块，配备大小写标准化产品表和防非 CN 交易所守卫，并新增 9 项回归用例。会话 FTS5 索引现在持久化时间戳，使跨会话搜索可按日期排序；同一路径还修复了每次重新插入都会导致全表扫描的 `started_at` 问题。Vite 开发模式代理新增了缺失的 `/alpha` 入口，使 AlphaZoo 页面在 `npm run dev` 下可解析。`tests/test_e2e_harness_v2.py`（真实 LLM e2e 套件）现在受 `VIBE_TRADING_RUN_LIVE_E2E=1` 门控保护，CI 不再因环境变量键的存在而改变形态。Ruff `per-file-ignores` 已为因子动物园添加（3783 → 0 F401 噪音），前端 tsconfig 启用了 `noUnusedLocals` / `noUnusedParameters` 作为回归守卫，并从 `gtja191` alphas 中删除了 76 行未使用的 `vw = vwap(...)` 样板代码。净减少 **-918 LOC**。
- **2026-05-17** 🧬 **Alpha Zoo v1 (0.1.8)**：4 个动物园共 452 个预构建量化 Alpha —— `qlib158`（Microsoft Qlib，Apache-2 署名），`alpha101`（Kakushadze 101 Formulaic Alphas，基于 arXiv:1601.00991 的论文重写），`gtja191`（国泰君安 2014 短期因子报告），以及 `academic`（Fama-French 5 + Carhart 价格基准代理）。一行 CLI 即可在你的标的池上测试任意动物园：`vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025`。附带 AST 纯度门控、前视守卫测试、`pytest-socket` 网络熔断开关、每动物园 LICENSE.md，以及面向社区 PR 的 DCO（开发者证书来源）工作流。Alpha Library 自动渲染于 [vibetrading.wiki/alpha-library/](https://vibetrading.wiki/alpha-library/) + 研究实验室文章 [191 个 GTJA Alpha 中哪些在 2026 年仍然有效？](https://vibetrading.wiki/research-lab/posts/alpha-191-in-2026.html)。
- **2026-05-16** 🧪 **Research spine 更新**：新增后端 Hypothesis Registry，包含 `create_hypothesis`、`update_hypothesis`、`link_backtest` 和 `search_hypotheses`；外部内容读取器现在附加仅警告的 `security_warnings`；Shadow Account 扫描现在使用确定性 OHLCV 特征评估替代旧的日历阶段存根。
- **2026-05-15** 🪪 运行详情页现在在指标和工件旁展示 Trust Layer 运行卡片，补全了 2026-05-12 提交的 `run_card.json` 的 UI 侧功能。`PersistentMemory.add()` 也在长度、空/纯空白名称以及 C0/C1 控制字节方面进行了加固（来自 #108/#109/#110 分诊）（[#112](https://github.com/HKUDS/Vibe-Trading/pull/112)，感谢 @Teerapat-Vatpitak）。
- **2026-05-14** 🌐 公共 Wiki 现已上线于 [vibetrading.wiki](https://vibetrading.wiki/)，通过 Cloudflare Pages 部署了文档、教程、研究实验室和 Alpha Library 板块。持久化记忆现在也可通过 CLI 检查：`vibe-trading memory list/show/search/forget`（[#102](https://github.com/HKUDS/Vibe-Trading/pull/102)，感谢 @Teerapat-Vatpitak），且记忆分词/Slug 现已支持泰语、阿拉伯语、希伯来语和西里尔文文本（[#104](https://github.com/HKUDS/Vibe-Trading/pull/104)）。
- **2026-05-13** 🧭 蜂群运行现在使用抓取的市场数据和更清爽的持久化报告为 Worker 提供上下文支撑（[#93](https://github.com/HKUDS/Vibe-Trading/pull/93), [#84](https://github.com/HKUDS/Vibe-Trading/pull/84)）。
- **2026-05-12** 🧾 回测现在在工件旁输出 `run_card.json` 和 `run_card.md`，以支持可复现的研究运行。
- **2026-05-11** 🧭 **记忆 Slug、蜂群记账与 CLI 预飞行检查**：持久化记忆在生成文件 Slug 时现在保留 CJK 字符，防止中文/日文/韩文笔记出现静默文件名冲突（[#95](https://github.com/HKUDS/Vibe-Trading/pull/95)，感谢 @voidborne-d）。蜂群运行总数现在优先使用提供商报告的 Token 用量，并保留现有的估算降级方案（[#94](https://github.com/HKUDS/Vibe-Trading/pull/94)，感谢 @Teerapat-Vatpitak），CLI 运行 UI 新增了常见环境问题的启动预飞行检查（[#96](https://github.com/HKUDS/Vibe-Trading/pull/96)，感谢 @ykykj）。
- **2026-05-10** 🧱 **回归护栏 + 运行元数据**：记忆召回现在将下划线视为 Token 边界，因此蛇形命名保存的记忆如 `mcp_wiring_test` 可匹配自然语言查询 "mcp wiring"（[#87](https://github.com/HKUDS/Vibe-Trading/pull/87)，感谢 @hp083625）。MCP 服务器新增了覆盖 initialize → `tools/list` → `tools/call` 的子进程冒烟测试，以防护首次调用死锁路径（[#86](https://github.com/HKUDS/Vibe-Trading/pull/86)），同时针对 Windows 路径敏感测试、API 尽力异常处理、回测 `run_dir` 允许根验证以及 SwarmRun 提供商/模型元数据落地了低风险加固（[#88](https://github.com/HKUDS/Vibe-Trading/pull/88), [#90](https://github.com/HKUDS/Vibe-Trading/pull/90), [#91](https://github.com/HKUDS/Vibe-Trading/pull/91), [#92](https://github.com/HKUDS/Vibe-Trading/pull/92)，感谢 @Teerapat-Vatpitak）。
- **2026-05-09** 🛡️ **API 路径加固 + MCP 服务器稳定性**：API 运行/会话路由现在在查找前验证路径 ID，拒绝包含换行符的畸形参数，并在认证/安全回归套件中固定行为（[#80](https://github.com/HKUDS/Vibe-Trading/pull/80)，感谢 @SJoon99）。MCP 服务器现在在主线程服务 `tools/call` 前预热工具注册表，避免懒加载工具发现导致的首次调用死锁（[#85](https://github.com/HKUDS/Vibe-Trading/pull/85)，感谢 @Teerapat-Vatpitak）。Vite 开发代理现在也尊重 `VITE_API_URL` 用于非默认后端目标（[#82](https://github.com/HKUDS/Vibe-Trading/pull/82)，感谢 @voidborne-d）。
- **2026-05-08** 🧾 **Tushare 财报字段在过滤器中**：A 股日度回测现在可通过 `fundamental_fields` 请求 PIT（Point-in-Time）安全的财务报表字段，使信号引擎能在公告/披露日期后筛选 `income_total_revenue`、`income_n_income`、`balancesheet_total_hldr_eqy_exc_min_int`、`fina_indicator_roe` 等带表前缀的列（[#76](https://github.com/HKUDS/Vibe-Trading/pull/76)，感谢 @mrbob-git）。后续加固使显式财报字段请求在 Tushare 增强无法运行时快速失败，而不是静默降级到原始价格柱（[#77](https://github.com/HKUDS/Vibe-Trading/pull/77)）。
- **2026-05-07** 📈 **Tushare 基本面 + 社区分诊**：新增面向基本面研究工作流的 PIT `TushareFundamentalProvider` 合约，并附带项目 `TUSHARE_TOKEN` 环境变量路径的回归覆盖（[#74](https://github.com/HKUDS/Vibe-Trading/pull/74)）。社区分诊还澄清了 Vibe-Trading 目前将快速迭代聚焦于单一 UI 语言，在已捆绑 DuckDuckGo 驱动的 `web_search` 时避免添加冗余搜索依赖，并将非官方托管部署视为不适合存放 API Key 或数据源 Token 的不受信任位置。
- **2026-05-06** 🚀 **v0.1.7 发布**（[Release notes](https://github.com/HKUDS/Vibe-Trading/releases/tag/v0.1.7), `pip install -U vibe-trading-ai`）：安全边界加固现已发布至 PyPI 和 ClawHub，涵盖更安全的 API/读取/上传/文件/URL/生成代码/Shell 工具/Docker 默认配置，同时保持 localhost CLI/Web UI 工作流低摩擦。本周期还包括 Web UI 设置、相关性热力图、OpenAI Codex OAuth、A 股预 ST 过滤、交互式 CLI UX、蜂群预设检查、股息分析、开发工作流打磨以及审计过的前端构建依赖底线。感谢 0.1.7 的贡献者及 lemi9090 (S2W) 的协同安全验证。
- **2026-05-05** 🛡️ **安全边界后续**：补全了围绕显式 CORS 起源、设置凭证指示器、网页 URL 读取和 Shadow Account 代码生成的剩余安全边界加固，并为每个路径添加了回归测试。正常的 localhost CLI/Web UI 工作流保持不变；远程部署应继续使用 `API_AUTH_KEY` 和显式可信来源。
- **2026-05-04** 🖥️ **交互式 CLI UX + CI 清理**：交互模式现在拥有实时底部状态栏，显示提供商/模型、会话时长、上次运行延迟和累计工具调用统计，并通过 `prompt_toolkit` 支持箭头键导航提示符历史和光标编辑（[#69](https://github.com/HKUDS/Vibe-Trading/pull/69)）。若不可用 `prompt_toolkit` 或 TTY，CLI 仍会回退到 Rich 提示符。CI 路径期望现已与加固的文件导入沙盒和跨平台 `/tmp` 解析对齐，使 main 分支恢复绿色（[`bb67dc7`](https://github.com/HKUDS/Vibe-Trading/commit/bb67dc7cfcc11553c57d8962bee56381dca43758)）。
- **2026-05-03** 🛡️ **安全加固补丁**：收紧了非本地部署的默认 API 认证，保护敏感的运行/会话/蜂群读取，限制上传和本地文件读取边界，按入口点门控 Shell 工具，在导入前验证生成的策略加载，并默认以非 root 用户运行 Docker 镜像且仅发布 localhost 端口。本地 CLI 和 localhost Web UI 工作流保持低摩擦；远程 API/Web 部署应设置 `API_AUTH_KEY`。
- **2026-05-02** 🧭 **股息分析 + 更清晰的路线图**：新增 `dividend-analysis` 技能用于收益股、派息可持续性、股息增长、股东收益率、除息机制和收益率陷阱检查，并由捆绑技能的回归测试固定。公共路线图现在聚焦于 upcoming work：Research Autopilot、Data Bridge、Options Lab、Portfolio Studio、Alpha Zoo、Research Delivery、Trust Layer 和社区分享。
- **2026-05-01** 🔥 **相关性热力图 + OpenAI Codex OAuth + A 股预 ST 过滤**：新增的相关性仪表板/API 计算滚动回报相关性并渲染 ECharts 热力图用于组合和标的分析（[#64](https://github.com/HKUDS/Vibe-Trading/pull/64)）。OpenAI Codex 提供商支持现在通过 `vibe-trading provider login openai-codex` 使用 ChatGPT OAuth，附带设置元数据和适配器回归测试（[#65](https://github.com/HKUDS/Vibe-Trading/pull/65)）。新增并加固了 `ashare-pre-st-filter` 技能用于 A 股 ST/*ST 风险筛查，包括新浪处罚相关性过滤以防止证券账户提及膨胀 E2 计数（[#63](https://github.com/HKUDS/Vibe-Trading/pull/63)）。
- **2026-04-30** ⚙️ **Web UI 设置 + CLI 验证加固**：新增 LLM 提供商/模型、基础 URL、推理力度和数据源凭证的设置页面，由本地/受认证的设置 API 和数据驱动的提供商元数据支持（[#57](https://github.com/HKUDS/Vibe-Trading/pull/57)）。同时加固了 `python -m backtest.validation <run_dir>`，使缺失、空白、畸形、不存在和非目录输入在验证开始前以清晰的操作员提示失败（[#60](https://github.com/HKUDS/Vibe-Trading/pull/60)）。
- **2026-04-28** 🚀 **v0.1.6 发布**（`pip install -U vibe-trading-ai`）：修复了 `pip install` / `uv tool install` 后 `vibe-trading --swarm-presets` 返回空的问题（[#55](https://github.com/HKUDS/Vibe-Trading/issues/55)）——预设 YAML 现已捆绑至 `src.swarm` 包内并由 6 项回归套件固定。此外 AKShare 加载器现在正确路由 ETF（`510300.SH`）和外汇（`USDCNH`）到正确的端点，并加固了注册表降级方案。汇总了 v0.1.5 以来的所有更新：基准对比面板、`/upload` 流式传输+大小限制、Futu 加载器（HK + A 股）、vnpy 导出技能、安全加固、前端懒加载（688KB → 262KB）。
- **2026-04-27** 📊 **基准面板 + 上传安全**：回测输出现在附带基准对比面板（Ticker / 基准回报 / 超额回报 / 信息比率），并支持通过 yfinance 解析 SPY、CSI 300 等（[#48](https://github.com/HKUDS/Vibe-Trading/issues/48)）。此外 `/upload` 以 1 MB 块流式传输请求体并在超过 `MAX_UPLOAD_SIZE` 时中止，将内存占用限制在畸形客户端下（[#53](https://github.com/HKUDS/Vibe-Trading/pull/53)）——由 4 用例回归套件固定。
- **2026-04-22** 🛡️ **加固 + 新集成**：`safe_path` + journal/shadow 工具沙盒中强制执行路径包含，`MANIFEST.in` 在 sdist 中包含 `.env.example` / tests / Docker 文件，路由级懒加载将前端初始包从 688KB 缩小至 262KB。此外新增 Futu HK & A 股股票数据加载器（[#47](https://github.com/HKUDS/Vibe-Trading/pull/47)）和 vnpy CtaTemplate 导出技能（[#46](https://github.com/HKUDS/Vibe-Trading/pull/46)）。
- **2026-04-21** 🛡️ **工作区 + 文档**：相对 `run_dir` 现在归一化为活跃运行目录（[#43](https://github.com/HKUDS/Vibe-Trading/pull/43)）。README 使用示例（[#45](https://github.com/HKUDS/Vibe-Trading/pull/45)）。
- **2026-04-20** 🔌 **推理 + Swarm**：`reasoning_content` 在所有 `ChatOpenAI` 路径中保留——Kimi / DeepSeek / Qwen 思维链端到端工作（[#39](https://github.com/HKUDS/Vibe-Trading/issues/39)）。Swarm 流式传输 + 干净 Ctrl+C（[#42](https://github.com/HKUDS/Vibe-Trading/issues/42)）。
- **2026-04-19** 📦 **v0.1.5**：发布至 PyPI & ClawHub。`python-multipart` CVE 底线提升，新增 5 个 MCP 工具（`analyze_trade_journal` + 4 个 shadow-account 工具），修复 `pattern_recognition` → `pattern` 注册表，Docker 依赖对齐，SKILL manifest 同步（22 MCP tools / 71 skills）。
- **2026-04-18** 👥 **Shadow Account**：从券商日志提取你的策略规则 → 跨市场回测影子账户 → 8 部分 HTML/PDF 报告精确展示你漏掉的机会（规则违规、提前退出、错过信号、反事实交易）。新增 4 个工具，1 个技能，共 32 个工具。Trade Journal + Shadow Account 示例现已上线 Web UI 欢迎屏。
- **2026-04-17** 📊 **Trade Journal Analyzer + Universal File Reader**：上传券商导出文件（同花顺/东财/富途/generic CSV） → 自动交易画像（持仓天数、胜率、盈亏比、回撤）+ 4 项偏差诊断（处置效应、过度交易、追涨杀跌、锚定效应）。`read_document` 现在通过统一调用分发 PDF、Word、Excel、PowerPoint、图片（OCR）和 40+ 文本格式。
- **2026-04-16** 🧠 **Agent Harness**：跨会话持久化记忆、FTS5 会话搜索、自进化技能（完整 CRUD）、5 层上下文压缩、读写工具批处理。27 个工具，107 项新测试。
- **2026-04-15** 🤖 **Z.ai + MiniMax**：Z.ai 提供商（[#35](https://github.com/HKUDS/Vibe-Trading/pull/35)），MiniMax 温度修复+模型更新（[#33](https://github.com/HKUDS/Vibe-Trading/pull/33)）。13 个提供商。
- **2026-04-14** 🔧 **MCP 稳定性**：修复了 stdio 传输下回测工具的 `Connection closed` 错误（[#32](https://github.com/HKUDS/Vibe-Trading/pull/32)）。
- **2026-04-13** 🌐 **跨市场组合回测**：新增 `CompositeEngine` 支持混合市场投资组合（如 A 股+加密货币）的回测，共享资金池并按市场规则执行。同时修复了蜂群模板变量降级和前端超时问题。
- **2026-04-12** 🌍 **多平台导出**：一条命令将策略导出至 TradingView (Pine Script v6)、TDX（通达信/同花顺/东方财富）和 MetaTrader 5 (MQL5)。
- **2026-04-11** 🛡️ **可靠性 & DX**：`vibe-trading init` .env 引导（[#19](https://github.com/HKUDS/Vibe-Trading/pull/19)）、预飞行检查、运行时数据源降级、加固回测引擎。多语言 README（[#21](https://github.com/HKUDS/Vibe-Trading/pull/21)）。
- **2026-04-10** 📦 **v0.1.4**：Docker 修复（[#8](https://github.com/HKUDS/Vibe-Trading/issues/8)），`web_search` MCP 工具，12 LLM 提供商，`akshare`/`ccxt` 依赖。发布至 PyPI 和 ClawHub。
- **2026-04-09** 📊 **回测 Wave 2**：ChinaFutures、GlobalFutures、Forex、Options v2 引擎。蒙特卡洛、Bootstrap CI、Walk-Forward 验证。
- **2026-04-08** 🔧 **多市场回测** 支持按市场规则、Pine Script v6 导出，5 个数据源自动降级。

</details>

---

## ✨ 核心功能

<div align="center">
<table align="center" width="94%" style="width:94%; margin-left:auto; margin-right:auto;">
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-self-improving-trading-agent.png" height="130" alt="Self-improving trading agent"/><br>
      <h3>🔍 自进化交易代理</h3>
      <div align="left">
        • 自然语言市场研究<br>
        • 策略草稿与文件/网页分析<br>
        • 记忆驱动的工作流
      </div>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-multi-agent-trading-teams.png" height="130" alt="Multi-agent trading teams"/><br>
      <h3>🐝 多智能体交易协作组</h3>
      <div align="left">
        • 投资、量化、加密与风控团队<br>
        • 流式进度与持久化报告<br>
        • Worker 由抓取的市场数据提供上下文支撑
      </div>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-cross-market-data-backtesting.png" height="130" alt="Cross-market data and backtesting"/><br>
      <h3>📊 跨市场数据与回测</h3>
      <div align="left">
        • A/HK/US 股票、加密货币、期货和外汇<br>
        • 数据降级与组合回测<br>
        • PIT 数据、验证与运行卡片
      </div>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-shadow-account.png" height="130" alt="Shadow Account"/><br>
      <h3>👥 影子账户 (Shadow Account)</h3>
      <div align="left">
        • 券商日志行为诊断<br>
        • 基于规则的影子账户对比<br>
        • 可导出的审计报告与策略代码
      </div>
    </td>
  </tr>
</table>
</div>

## 💡 Vibe-Trading 是什么？

Vibe-Trading 是一个开源研究工作台，用于将金融问题转化为可运行的分析。它将自然语言提示词连接到市场数据加载器、策略生成、回测引擎、报告、导出和持久化研究记忆。

它专为研究、模拟和回测设计——当你选择时，也可通过你自行授权的券商（例如 Robinhood Agentic Trading）进行自主交易。它不持有资金，也绝不会在你设定的限制之外进行交易，且你可随时瞬间停止它。

---

## ✨ 你能做什么

| 任务 | 输出 |
|------|--------|
| **提出交易问题** | 使用工具、数据、文档和可复用会话上下文进行市场研究。 |
| **回测策略想法** | 策略代码、指标、基准对比、验证工件和运行卡片。 |
| **复盘你的交易** | 券商日志解析、行为诊断、规则提取与影子账户对比。 |
| **优化重复性研究** | 持久化记忆和可编辑技能将实用流程转化为可复用工作流。 |
| **运行分析师团队** | 针对投资、量化、加密、宏观和风险工作流的多智能体研究评审。 |
| **交付可用工件** | 报告、TradingView Pine Script、TDX、MetaTrader 5、MCP 工具及后续研究会话。 |
| **测试预构建 Alpha 动物园** | 一行命令在你的标的池上对 452 个 Alpha（Qlib 158 + Kakushadze 101 + GTJA 191 + FF5 + Carhart）进行 IC + 存活/反转/失效分类。 |

---

## ⚡ 快速示例

```bash
pip install vibe-trading-ai

# 自然语言研究
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report"

# 测试预构建 Alpha 动物园（一行）
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

```bash
vibe-trading --upload trades_export.csv
vibe-trading run -p "Analyze my trading behavior, extract my shadow strategy, and compare it with my actual trades"
```

---

## 👥 影子账户 (Shadow Account)

影子账户从你自己的交易记录开始，而非通用策略模板。

上传券商导出文件，让代理总结你的行为，然后将实际交易路径与基于规则的影子策略进行对比。

| 步骤 | 代理输出 |
|------|--------------|
| **1. 读取日志** | 解析来自同花顺、东方财富、富途和通用 CSV 格式的券商导出文件。 |
| **2. 画像你的行为** | 持仓天数、胜率、盈亏比、回撤、处置效应、过度交易、追涨杀跌和锚定检查。 |
| **3. 提取规则** | 将重复的入场/出场转化为明确的策略画像，而非模糊总结。 |
| **4. 运行影子** | 回测提取的规则，高亮规则违规、提前退出、错过信号及替代交易路径。 |
| **5. 交付报告** | 生成可检查、归档或在后续会话中优化的 HTML/PDF 报告。 |

```bash
vibe-trading --upload trades_export.csv
vibe-trading run -p "Analyze my trading behavior, extract my shadow strategy, and compare it with my actual trades"
```

---

## 🧪 研究工作流

大多数运行遵循相同的路径：路由请求、加载正确的市场上下文、执行工具、验证输出，并保持工件可检查。

| 层级 | 发生什么 |
|-------|--------------|
| **Plan** | 选择相关的金融技能、工具、数据源和蜂群预设（如有必要）。 |
| **Ground** | 通过可用加载器获取 A 股、HK/US 股票、加密货币、期货、外汇、文档或网页上下文。 |
| **Execute** | 生成可测试的策略代码，运行工具，并使用匹配的回测引擎或分析工作流。 |
| **Validate** | 添加指标、基准对比、蒙特卡洛、Bootstrap、Walk-Forward、运行卡片和警告（如适用）。 |
| **Deliver** | 返回报告、工件、工具追踪以及 TradingView、TDX、MetaTrader 5、MCP 客户端或后续会话的导出文件。 |

---

## 🔩 详细功能

详细清单折叠在下方以保持主 README 的可扫描性。当你需要检查可用构建块时再展开它们。

<details>
<summary><b>金融技能库</b> <sub>8 大类共 77 项技能</sub></summary>

- 📊 77 个专业化金融技能，分为 8 个类别
- 🌐 从传统市场到加密 & DeFi 的完整覆盖
- 🔬 涵盖数据获取到量化研究的综合能力

| 类别 | 数量 | 示例 |
|----------|--------|----------|
| Data Source | 7 | `data-routing`, `tushare`, `yfinance`, `okx-market`, `akshare`, `mootdx`, `ccxt` |
| Strategy | 17 | `strategy-generate`, `cross-market-strategy`, `technical-basic`, `candlestick`, `ichimoku`, `elliott-wave`, `smc`, `multi-factor`, `ml-strategy` |
| Analysis | 17 | `factor-research`, `macro-analysis`, `global-macro`, `valuation-model`, `earnings-forecast`, `credit-analysis`, `dividend-analysis` |
| Asset Class | 9 | `options-strategy`, `options-advanced`, `convertible-bond`, `etf-analysis`, `asset-allocation`, `sector-rotation` |
| Crypto | 7 | `perp-funding-basis`, `liquidation-heatmap`, `stablecoin-flow`, `defi-yield`, `onchain-analysis` |
| Flow | 7 | `hk-connect-flow`, `us-etf-flow`, `edgar-sec-filings`, `financial-statement`, `adr-hshare` |
| Tool | 11 | `backtest-diagnose`, `report-generate`, `pine-script`, `doc-reader`, `web-reader`, `vnpy-export`, `alpha-zoo` |
| Risk Analysis | 1 | `ashare-pre-st-filter` |

</details>

<details>
<summary><b>预设交易团队</b> <sub>29 个蜂群预设</sub></summary>

- 🏢 29 套开箱即用的代理团队
- ⚡ 预配置的金融工作流
- 🎯 投资、交易与风险管理预设

| 预设 | 工作流 |
|--------|----------|
| `investment_committee` | 牛熊辩论 → 风控评审 → PM 最终决策 |
| `global_equities_desk` | A 股 + HK/US + 加密研究员 → 全球策略师 |
| `crypto_trading_desk` | 资金费率/基差 + 清算 + 资金流 → 风险经理 |
| `earnings_research_desk` | 基本面 + 修正 + 期权 → 财报策略师 |
| `macro_rates_fx_desk` | 利率 + FX + 商品 → 宏观 PM |
| `quant_strategy_desk` | 筛选 + 因子研究 → 回测 → 风控审计 |
| `technical_analysis_panel` | 经典 TA + Ichimoku + 谐波 + Elliott + SMC → 共识 |
| `risk_committee` | 回撤 + 尾部风险 + 制度评审 → 签字放行 |
| `global_allocation_commit` | A 股 + 加密 + HK/US → 跨市场配置 |

<sub>另有 20+ 专业预设 —— 运行 vibe-trading --swarm-presets 探索全部。

</sub>

</details>

<details>
<summary><b>Alpha Zoo</b> <sub>4 个动物园共 452 个预构建量化 Alpha</sub></summary>

- 🧬 452 个横截面 Alpha，在操作员层禁止前视
- 📈 IC + IR + 存活/反转/失效分类在一行 CLI 命令中完成
- 🔬 AST 纯度门控 + 300 行前视哨兵测试 + `pytest-socket` 网络熔断开关
- 📦 Qlib Apache-2 署名；每动物园 `LICENSE.md` 声明公式为数学内容
- 🤝 DCO（开发者证书来源）签核工作流面向社区 PR

| Zoo | 数量 | 来源 | 许可证 |
|-----|-------|--------|---------|
| **qlib158** | 154 | Microsoft Qlib `Alpha158` (Apache-2.0, commit-pinned) | Apache-2.0 |
| **alpha101** | 101 | Kakushadze (2015), "101 Formulaic Alphas", arXiv:1601.00991 | 公式属于数学内容 |
| **gtja191** | 191 | Guotai Junan (2014), "191 Short-period Trading Alpha Factors" | 公式属于数学内容 |
| **academic** | 6 | Fama-French 5 + Carhart momentum (价格基准代理) | 公共学术文献 |

运行 `vibe-trading alpha list` 浏览，`vibe-trading alpha show <id>` 查看公式+来源，`vibe-trading alpha bench --zoo X --universe Y --period Z` 对整动物园打分。

</details>

## 🎬 演示

<div align="center">
<table>
<tr>
<td width="50%">

https://github.com/user-attachments/assets/4e4dcb80-7358-4b9a-92f0-1e29612e6e86

</td>
<td width="50%">

https://github.com/user-attachments/assets/3754a414-c3ee-464f-b1e8-78e1a74fbd30

</td>
</tr>
<tr>
<td colspan="2" align="center"><sub>☝️ 自然语言回测 & 多智能体蜂群辩论 —— Web UI + CLI</sub></td>
</tr>
</table>
</div>

---

## 🚀 快速开始

### 一行安装 (PyPI)

```bash
pip install vibe-trading-ai
```

然后运行首次研究任务：

```bash
vibe-trading init
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024 and summarize return and drawdown"
```

> **包名与命令：** PyPI 包名为 `vibe-trading-ai`。安装后你将获得三个命令：
>
> | 命令 | 用途 |
> |---------|---------|
> | `vibe-trading` | 交互式 CLI / TUI |
> | `vibe-trading serve` | 启动 FastAPI Web 服务器 |
> | `vibe-trading-mcp` | 启动 MCP 服务器（用于 Claude Desktop、OpenClaw、Cursor 等） |

```bash
vibe-trading init              # 交互式 .env 设置
vibe-trading                   # 启动 CLI
vibe-trading serve --port 8899 # 启动 Web UI
vibe-trading-mcp               # 启动 MCP 服务器 (stdio)
```

### 或选择一条路径

| 路径 | 适用场景 | 耗时 |
|------|----------|------|
| **A. Docker** | 立即试用，零本地配置 | 2 分钟 |
| **B. 本地安装** | 开发、完整 CLI 访问 | 5 分钟 |
| **C. MCP 插件** | 接入你现有的代理 | 3 分钟 |
| **D. ClawHub** | 一条命令，无需克隆仓库 | 1 分钟 |

### 前置条件

- 来自任何支持提供商的 **LLM API Key** —— 或使用 **Ollama** 本地运行（无需 Key）
- Path B 需要 **Python 3.11+**
- Path A 需要 **Docker**
- OpenAI Codex 也可通过 ChatGPT OAuth 使用：设置 `LANGCHAIN_PROVIDER=openai-codex`，然后运行 `vibe-trading provider login openai-codex`。此方式不使用 `OPENAI_API_KEY`。

> **支持的 LLM 提供商：** OpenRouter、OpenAI、DeepSeek、Gemini、Groq、DashScope/Qwen、Zhipu、Moonshot/Kimi、MiniMax、Xiaomi MIMO、Z.ai、Ollama（本地）。配置详见 `.env.example`。

> **提示：** 得益于自动降级机制，所有市场均可在无 API Key 的情况下工作。yfinance (HK/US)、OKX (crypto)、mootdx (A 股，直连 TCP，无 IP 限流) 和 AKShare (A 股、美股、港股、期货、外汇) 均为免费数据源。Tushare Token 为可选项 —— mootdx 是首选的免 Token A 股降级方案，AKShare 作为更广泛的备份。

### Path A: Docker（零配置）

```bash
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading
cp agent/.env.example agent/.env
# 编辑 agent/.env —— 取消注释你的 LLM 提供商并设置 API Key
docker compose up --build
```

打开 `http://localhost:8899`。后端 + 前端在单个容器中运行。

Docker 默认将后端发布在 `127.0.0.1:8899`，并以非 root 容器用户运行应用。如果你有意将 API 暴露给本机以外的网络，请设置强密码的 `API_AUTH_KEY`，并在客户端发送 `Authorization: Bearer <key>`。

### Path B: 本地安装

```bash
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading
python -m venv .venv

# 激活虚拟环境
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\Activate.ps1       # Windows PowerShell

pip install -e .
cp agent/.env.example agent/.env   # 编辑 —— 设置你的 LLM 提供商 API Key
vibe-trading                       # 启动交互式 TUI
```

<details>
<summary><b>启动 Web UI（可选）</b></summary>

```bash
# Terminal 1: API server
vibe-trading serve --port 8899

# Terminal 2: Frontend dev server
cd frontend && npm install && npm run dev
```

打开 `http://localhost:5899`。前端将 API 请求代理至 `localhost:8899`。

**生产模式（单服务器）：**

```bash
cd frontend && npm run build && cd ..
vibe-trading serve --port 8899     # FastAPI 以静态文件形式提供 dist/
```

</details>

### Path C: MCP 插件

详见下方 [MCP Plugin](#-mcp-plugin) 章节。

### Path D: ClawHub（一条命令）

```bash
npx clawhub@latest install vibe-trading --force
```

技能 + MCP 配置将下载至你代理的技能目录中。详见 [ClawHub install](#-mcp-plugin)。

---

## 🧠 环境变量

复制 `agent/.env.example` 到 `agent/.env` 并取消注释你想要使用的提供商区块。每个提供商需要 3-4 个变量：

| Variable | Required | Description |
|----------|:--------:|-------------|
| `LANGCHAIN_PROVIDER` | Yes | 提供商名称 (`openrouter`, `deepseek`, `groq`, `ollama` 等) |
| `<PROVIDER>_API_KEY` | Yes* | API Key (`OPENROUTER_API_KEY`, `DEEPSEEK_API_KEY` 等) |
| `<PROVIDER>_BASE_URL` | Yes | API 端点 URL |
| `LANGCHAIN_MODEL_NAME` | Yes | 模型名称 (e.g. `deepseek-v4-pro`) |
| `TUSHARE_TOKEN` | No | A 股数据用的 Tushare Pro Token（降级至 AKShare） |
| `TIMEOUT_SECONDS` | No | LLM 调用超时，默认 120s |
| `API_AUTH_KEY` | Recommended for network deployments | 当 API 可从非本地客户端访问时所需的 Bearer Token |
| `VIBE_TRADING_ENABLE_SHELL_TOOLS` | No | 在远程 API/MCP-SSE 风格部署中显式启用 Shell 工具 |
| `VIBE_TRADING_ALLOWED_FILE_ROOTS` | No | 文档和券商日志导入的额外逗号分隔根目录 |
| `VIBE_TRADING_ALLOWED_RUN_ROOTS` | No | 生成代码运行目录的额外逗号分隔根目录 |

<sub>* Ollama 不需要 API Key。OpenAI Codex 使用 ChatGPT OAuth 并通过 `oauth-cli-kit` 存储 Token，而非存放在 `agent/.env`。</sub>

**免费数据（无需 Key）：** A 股通过 AKShare、HK/US 股票通过 yfinance、加密货币通过 OKX、100+ 加密交易所通过 CCXT。系统会自动为每个市场选择最佳可用源。

### 🎯 推荐模型

Vibe-Trading 是一个重度依赖工具的代理 —— 技能、回测、记忆和蜂群均流经工具调用。模型选择直接决定代理是*使用*其工具，还是从训练数据中编造答案。

| Tier | Examples | When to use |
|------|----------|-------------|
| **Best** | `anthropic/claude-opus-4.7`, `anthropic/claude-sonnet-4.6`, `openai/gpt-5.5-pro`, `google/gemini-3.5-flash` | 复杂蜂群（3+ 代理）、长研究会话、论文级分析 |
| **Sweet spot** (default) | `deepseek-v4-pro`, `deepseek/deepseek-v4-pro`, `x-ai/grok-4.20`, `z-ai/glm-5.1`, `moonshotai/kimi-k2.6`, `qwen/qwen3-max-thinking` | 日常主力 —— 可靠的工具调用，成本约为前者的 1/10 |
| **Avoid for agent use** | `*-nano`, `*-flash-lite`, `*-coder-next`, small / distilled variants | 工具调用不可靠 —— 代理会看似“从记忆中回答”，而非加载技能或运行回测 |

默认 `agent/.env.example` 附带 DeepSeek 官方 API + `deepseek-v4-pro`；OpenRouter 用户可使用 `deepseek/deepseek-v4-pro`。

---

## 🖥 CLI 参考

交互式 TUI (`vibe-trading`) 现在使用终端原生转录格式：启动 Banner、提示符规则、上一轮摘要、实时活动轨道、Markdown/表格渲染和运行耗时均保留在 CLI 中。非交互调用如 `vibe-trading run`、管道输入和 `--json` 仍保持脚本友好。

```bash
vibe-trading               # 交互式 TUI
vibe-trading run -p "..."  # 单次运行
vibe-trading serve         # API server
vibe-trading alpha list    # 浏览 452 个预构建 Alpha；支持 show / bench / compare / export-manifest 子命令
```

<details>
<summary><b>TUI 内的斜杠命令</b></summary>

| Command | Description |
|---------|-------------|
| `/help` | 显示所有命令 |
| `/skills` | 列出全部 77 项金融技能 |
| `/swarm` | 列出 29 个蜂群团队预设 |
| `/swarm run <preset> [vars_json]` | 运行蜂群团队并实时流式传输 |
| `/swarm list` | 蜂群运行历史 |
| `/swarm show <run_id>` | 蜂群运行详情 |
| `/swarm cancel <run_id>` | 取消运行的蜂群 |
| `/list` | 最近运行记录 |
| `/show <run_id>` | 运行详情 + 指标 |
| `/code <run_id>` | 生成的策略代码 |
| `/pine <run_id>` | 导出指标 (TradingView + TDX + MT5) |
| `/trace <run_id>` | 完整执行回放 |
| `/continue <run_id> <prompt>` | 使用新指令继续运行 |
| `/sessions` | 列出聊天会话 |
| `/settings` | 显示运行时配置 |
| `/clear` | 清屏 |
| `/quit` | 退出 |

</details>

<details>
<summary><b>单次运行 & 参数</b></summary>

```bash
vibe-trading run -p "Backtest BTC-USDT MACD strategy, last 30 days"
vibe-trading run -p "Analyze AAPL momentum" --json
vibe-trading run -f strategy.txt
echo "Backtest 000001.SZ RSI" | vibe-trading run
```

```bash
vibe-trading -p "your prompt"
vibe-trading --skills
vibe-trading --swarm-presets
vibe-trading --swarm-run investment_committee '{"topic":"BTC outlook"}'
vibe-trading --list
vibe-trading --show <run_id>
vibe-trading --code <run_id>
vibe-trading --pine <run_id>           # 导出指标 (TradingView + TDX + MT5)
vibe-trading --trace <run_id>
vibe-trading --continue <run_id> "refine the strategy"
vibe-trading --upload report.pdf
```

```bash
vibe-trading alpha list --zoo gtja191 --limit 10
vibe-trading alpha show gtja191_171
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

</details>

---

## 💡 示例

### 策略与回测

```bash
# 美股均线交叉
vibe-trading run -p "Backtest a 20/50-day moving average crossover on AAPL for the past year, show Sharpe ratio and max drawdown"

# 加密货币 RSI 均值回归
vibe-trading run -p "Test RSI(14) mean-reversion on BTC-USDT: buy below 30, sell above 70, last 6 months"

# A 股多因子策略
vibe-trading run -p "Backtest a momentum + value + quality multi-factor strategy on CSI 300 constituents over 2 years"

# 回测后导出至 TradingView / TDX / MetaTrader 5
vibe-trading --pine <run_id>
```

**测试预构建 Alpha 动物园（一行）：**
```bash
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

**浏览目录并检查单个 Alpha：**
```bash
vibe-trading alpha list --zoo gtja191 --theme reversal --limit 10
vibe-trading alpha show gtja191_171
```

**从动物园组合多因子信号（Python）：**
```python
from src.skills.multi_factor.zoo_signal_engine import ZooSignalEngine
engine = ZooSignalEngine.from_zoo(["gtja191_171", "gtja191_111", "gtja191_163"])
panel = ...  # your wide OHLCV panel
signal = engine.compute_signal(panel)
```

### 市场研究

```bash
# 股票深度调研
vibe-trading run -p "Research NVDA: earnings trend, analyst consensus, option flow, and key risks for next quarter"

# 宏观分析
vibe-trading run -p "Analyze the current Fed rate path, USD strength, and impact on EM equities and gold"

# 加密货币链上数据
vibe-trading run -p "Deep dive BTC on-chain: whale flows, exchange balances, miner activity, and funding rates"
```

### 蜂群工作流

```bash
# 股票牛熊辩论
vibe-trading --swarm-run investment_committee '{"topic": "Is TSLA a buy at current levels?"}'

# 量化策略：从筛选到回测
vibe-trading --swarm-run quant_strategy_desk '{"universe": "S&P 500", "horizon": "3 months"}'

# 加密团队：资金费率 + 清算 + 资金流 → 风险经理
vibe-trading --swarm-run crypto_trading_desk '{"asset": "ETH-USDT", "timeframe": "1w"}'

# 全球宏观投资组合配置
vibe-trading --swarm-run macro_rates_fx_desk '{"focus": "Fed pivot impact on EM bonds"}'
```

### 跨会话记忆

```bash
# 一次性保存你的偏好
vibe-trading run -p "Remember: I prefer RSI-based strategies, max 10% drawdown, hold period 5–20 days"

# 代理将在后续会话中自动回忆这些偏好
vibe-trading run -p "Build a crypto strategy that fits my risk profile"
```

### 上传与分析文档

```bash
# 分析券商导出文件或财报
vibe-trading --upload trades_export.csv
vibe-trading run -p "Profile my trading behavior and identify any biases"

vibe-trading --upload NVDA_Q1_earnings.pdf
vibe-trading run -p "Summarize the key risks and beats/misses from this earnings report"
```

---

## 🌐 API 服务器

```bash
vibe-trading serve --port 8899
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/runs` | 列出运行记录 |
| `GET` | `/runs/{run_id}` | 运行详情 |
| `GET` | `/runs/{run_id}/pine` | 多平台指标导出 |
| `POST` | `/sessions` | 创建会话 |
| `POST` | `/sessions/{id}/messages` | 发送消息 |
| `GET` | `/sessions/{id}/events` | SSE 事件流 |
| `POST` | `/upload` | 上传 PDF/文件 |
| `GET` | `/swarm/presets` | 列出蜂群预设 |
| `POST` | `/swarm/runs` | 启动蜂群运行 |
| `GET` | `/swarm/runs/{id}/events` | 蜂群 SSE 流 |
| `GET` | `/alpha/list` | 列出 Alpha（按 Zoo/主题/标的池过滤） |
| `GET` | `/alpha/{alpha_id}` | Alpha 元数据 + 源代码 |
| `POST` | `/alpha/bench` | 启动基准任务（返回 `job_id`） |
| `GET` | `/alpha/bench/{job_id}/stream` | SSE 进度流 |
| `GET` | `/settings/llm` | 读取 Web UI LLM 设置 |
| `PUT` | `/settings/llm` | 更新本地 LLM 设置 |
| `GET` | `/settings/data-sources` | 读取本地数据源设置 |
| `PUT` | `/settings/data-sources` | 更新本地数据源设置 |

交互式文档：`http://localhost:8899/docs`

### 安全默认配置

对于 localhost 开发，`vibe-trading serve` 保持浏览器工作流简单。对于任何非本地客户端，敏感 API 端点需要 `API_AUTH_KEY`；对 JSON/上传请求使用 `Authorization: Bearer <key>`。浏览器 EventSource 流由 Web UI 处理，你只需在设置中输入一次相同的 Key。

Shell 工具仅向本地 CLI 和受信任的 localhost 工作流开放，除非你显式设置 `VIBE_TRADING_ENABLE_SHELL_TOOLS=1`，否则不会暴露给远程 API 会话。文档和日志读取器默认仅限于上传/导入根目录；请将文件放置于 `agent/uploads`、`agent/runs`、`./uploads`、`./data`、`~/.vibe-trading/uploads` 或 `~/.vibe-trading/imports`，或通过 `VIBE_TRADING_ALLOWED_FILE_ROOTS` 添加专用目录。

### Web UI 设置

Web UI 设置页面允许本地用户更新 LLM 提供商/模型、基础 URL、生成参数、推理力度以及可选的市场数据凭证（如 Tushare Token）。设置持久化至 `agent/.env`；提供商默认值从 `agent/src/providers/llm_providers.json` 加载。

设置读取无副作用：`GET /settings/llm` 和 `GET /settings/data-sources` 永远不会创建 `agent/.env`，且仅返回项目相对路径。设置读写可能暴露凭证状态或更新凭证/运行时环境，因此在配置时需要 `API_AUTH_KEY`。若 dev 模式下未设置 `API_AUTH_KEY`，则仅接受来自回环客户端的设置访问。

---

## 🔌 MCP 插件

Vibe-Trading 向任何兼容 MCP 的客户端暴露 36 个 MCP 工具。作为 stdio 子进程运行 —— 无需服务器配置。核心研究工具对 HK/US/crypto 零 API Key 即可工作；交易连接器工具使用选定的连接器配置档案，`run_swarm` 需要 LLM Key。

<details>
<summary><b>Claude Desktop</b></summary>

添加至 `claude_desktop_config.json`：

```json
{
  "mcpServers": {
    "vibe-trading": {
      "command": "vibe-trading-mcp"
    }
  }
}
```

</details>

<details>
<summary><b>OpenClaw</b></summary>

添加至 `~/.openclaw/config.yaml`：

```yaml
skills:
  - name: vibe-trading
    command: vibe-trading-mcp
```

进行首次仅研究冒烟测试时，请先确认工具发现并运行市场数据或回测请求，然后再选择交易连接器配置档案。核心研究工具可在无券商凭证的情况下运行；仅在你有意选择并检查连接器配置档案后，才应使用由连接器驱动的 `trading_*` 工具。`run_swarm` 需要 LLM Key。

</details>

<details>
<summary><b>Cursor / Windsurf / 其他 MCP 客户端</b></summary>

```bash
vibe-trading-mcp                  # stdio (默认)
vibe-trading-mcp --transport sse  # SSE 用于 Web 客户端
```

</details>

**暴露的 MCP 工具（36个）：** `list_skills`, `load_skill`, `start_research_goal`, `get_research_goal`, `add_goal_evidence`, `update_research_goal_status`, `backtest`, `factor_analysis`, `analyze_options`, `pattern_recognition`, `read_url`, `read_document`, `web_search`, `write_file`, `read_file`, `list_swarm_presets`, `run_swarm`, `get_market_data`, `get_swarm_status`, `get_run_result`, `list_runs`, `reap_stale_runs`, `retry_run`, `analyze_trade_journal`, `extract_shadow_strategy`, `run_shadow_backtest`, `render_shadow_report`, `scan_shadow_signals`, `trading_connections`, `trading_select_connection`, `trading_check`, `trading_account`, `trading_positions`, `trading_orders`, `trading_quote`, `trading_history`.

### SWARM 外部 MCP 工具

`run_swarm` Worker 可调用来自外部 MCP 服务器的操作员批准工具。在 `VIBE_TRADING_SWARM_AGENT_CONFIG`、`~/.vibe-trading/swarm-agent.json` 或降级路径 `~/.vibe-trading/agent.json` 中配置服务器端白名单；然后在蜂群预设中使用本地 MCP 包装器名称列出远程工具，例如 `mcp_internal_kb_search`。调用者提供的 `variables` 仅保留为模板数据，无法注入 MCP URL、命令、环境变量或白名单覆盖项。

<details>
<summary><b>从 ClawHub 安装（一条命令）</b></summary>

```bash
npx clawhub@latest install vibe-trading --force
```

> `--force` 是必需的，因为技能引用了外部 API，这会触发 VirusTotal 的自动扫描。代码完全开源且安全可检查。

这将把技能 + MCP 配置下载至你代理的技能目录中。无需克隆仓库。

在 ClawHub 浏览：[clawhub.ai/skills/vibe-trading](https://clawhub.ai/skills/vibe-trading)

</details>

<details>
<summary><b>OpenSpace —— 自进化技能</b></summary>

全部 77 项金融技能已发布至 [open-space.cloud](https://open-space.cloud)，并通过 OpenSpace 的自进化引擎自主演进。

要与 OpenSpace 配合使用，请将两个 MCP 服务器添加至你的代理配置：

```json
{
  "mcpServers": {
    "openspace": {
      "command": "openspace-mcp",
      "toolTimeout": 600,
      "env": {
        "OPENSPACE_HOST_SKILL_DIRS": "/path/to/vibe-trading/agent/src/skills",
        "OPENSPACE_WORKSPACE": "/path/to/OpenSpace"
      }
    },
    "vibe-trading": {
      "command": "vibe-trading-mcp"
    }
  }
}
```

OpenSpace 将自动发现全部 77 项技能，启用自动修复、自动改进和社区分享。在任何连接 OpenSpace 的代理中通过 `search_skills("finance backtest")` 搜索 Vibe-Trading 技能。

</details>

---

## 🔌 从外部 MCP 服务器加载工具（MCP 客户端模式）

> **这与上方的 MCP 插件方向相反。**
> MCP 插件允许*其他代理*调用 Vibe-Trading 的工具。
> 本节让 *内置的* Vibe-Trading 代理调用 *你的* 外部 MCP 服务器的工具。

### 快速开始

创建 `~/.vibe-trading/agent.json`：

```json
{
  "mcpServers": {
    "my-server": {
      "command": "uvx",
      "args": ["my-mcp-server"]
    }
  }
}
```

运行任意 CLI 命令 —— 普通外部服务器的工具将在本地工具之后自动注入代理注册表：

```bash
vibe-trading run "use my-server to do X"
```

### 官方 IBKR MCP 只读探针

Vibe-Trading 可以只读模式直接连接至 Interactive Brokers 的官方远程 MCP 端点。将此添加至 `~/.vibe-trading/agent.json`：

```json
{
  "mcpServers": {
    "ibkr": {
      "type": "streamableHttp",
      "url": "https://api.ibkr.com/v1/api/mcp",
      "auth": {
        "type": "oauth",
        "scopes": ["mcp.read"],
        "clientName": "Vibe-Trading",
        "cacheDir": "~/.vibe-trading/live/ibkr/oauth"
      },
      "enabledTools": ["*"]
    }
  }
}
```

然后启动浏览器 OAuth 流程：

```bash
vibe-trading connector authorize ibkr-live-official-mcp-readonly
```

通配符仅接受用于 IBKR 的 `mcp.read` 探针。授权此配置档案确认了对 IBKR 官方只读范围的访问；通用的 `trading_account` 和 `trading_positions` 调用在 Vibe-Trading 能安全映射稳定的读取工具名称之前保持禁用。添加 `mcp.write` 的配置必须固定显式工具白名单，并仍通过实盘订单守卫。

如果 IBKR 颁发预注册 OAuth 客户端，请在 `auth` 内添加 `clientId` 和 `clientSecret`。

### 交易连接器：最快路径

对于无法等待 IBKR OAuth 客户端审批的用户，连接至本地 TWS 或 IB Gateway 会话。凭证保留在 IBKR 桌面应用内部；Vibe-Trading 仅连接至 `127.0.0.1` 并将其作为连接器配置档案暴露。

安装可选 SDK：

```bash
pip install "vibe-trading-ai[ibkr]"
```

打开 TWS 仿真交易或 IB Gateway 仿真，启用 API Socket 客户端，然后运行：

```bash
vibe-trading connector list
vibe-trading connector use ibkr-paper-local
vibe-trading connector configure ibkr-paper-local --yes
vibe-trading connector check
vibe-trading connector account
vibe-trading connector positions
vibe-trading connector orders
vibe-trading connector quote AAPL
vibe-trading connector history AAPL --duration "30 D" --bar-size "1 day"
```

默认本地端口：

| App | Paper | Live read-only |
|-----|-------|----------------|
| TWS | `7497` | `7496` |
| IB Gateway | `4002` | `4001` |

代理暴露的连接器范围工具名为 `trading_connections`、`trading_select_connection`、`trading_check`、`trading_account`、`trading_positions`、`trading_orders`、`trading_quote` 和 `trading_history`。实盘券商原始 MCP 工具不直接注册为 `mcp_<broker>_*`。未注册任何 IBKR 下单工具。

### 配置参考

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `type` | string | inferred for stdio; required for HTTP | 对 stdio 省略，或对基于 URL 的服务器设置为 `sse` / `streamableHttp`。 |
| `command` | string | required for stdio | 用于启动 stdio 服务器的可执行文件。不适用于 `sse` / `streamableHttp` 服务器。 |
| `args` | array | `[]` | 仅适用于 stdio 服务器的命令行参数。 |
| `env` | object | `{}` | 仅适用于 stdio 服务器的额外环境变量，合并至子进程环境。 |
| `url` | string | required for `sse` / `streamableHttp` | 远程 SSE / streamable HTTP 端点 URL。不用于 stdio 服务器。 |
| `headers` | object | `{}` | 仅适用于 `sse` / `streamableHttp` 服务器的额外 HTTP 头。 |
| `toolTimeout` | number | `30` | 每个工具调用超时（秒） |
| `enabledTools` | array | `["*"]` | 工具白名单。使用 `["*"]` 暴露服务器的全部工具 |

配置文件位置：`~/.vibe-trading/agent.json` (JSON 或 YAML)。

对于基于 URL 的传输，`type` 为必填项。代理不再根据 URL 后缀猜测 SSE 和 streamable HTTP。

### 会话级覆盖（API）

通过 API 创建会话时，你可以在 `session.config` 内传递 `mcpServers` 以仅扩展或覆盖该会话的全局配置：

```json
{
  "config": {
    "mcpServers": {
      "research-server": {
        "command": "uvx",
        "args": ["research-mcp"],
        "enabledTools": ["search", "fetch"]
      }
    }
  }
}
```

### 工具命名

普通远程工具以稳定名称暴露：`mcp_<server>_<tool>`。实盘券商 MCP 服务器保留在 `trading_*` 连接器表面之后。

如果两个服务器名称产生相同的 ASCII 安全本地前缀（例如 `foo-bar` 和 `foo_bar` 均变为 `foo_bar`），将在服务器段级别附加确定性哈希后缀以保持名称唯一。操作员将收到警告：

```
WARNING: Configured MCP server 'foo-bar' collides with another server after local name
normalization. Using local tool prefix 'mcp_foo_bar_<hash>_<tool>' to keep generated
tool names unique. Rename the server in agent config if you want a different prefix.
```

### v1 限制

| Limit | Detail |
|-------|--------|
| Transport | stdio, SSE, and streamable HTTP |
| Execution | serial only — MCP tools never enter the parallel readonly path |
| Surfaces | tools only (resources and prompts excluded in v1) |
| Hot reload | not supported — restart the process to pick up config changes |
| Swarm path | MCP tools are not available inside Swarm worker registries in v1 |

---

## 📁 项目结构

<details>
<summary><b>点击展开</b></summary>

```
Vibe-Trading/
├── agent/                          # Backend (Python)
│   ├── cli/                        # CLI package — interactive TUI + subcommands
│   ├── api_server.py               # FastAPI server — runs, sessions, upload, swarm, SSE
│   ├── mcp_server.py               # MCP server — 36 tools for OpenClaw / Claude Desktop
│   │
│   ├── src/
│   │   ├── agent/                  # ReAct agent core
│   │   │   ├── loop.py             #   5-layer compression + read/write tool batching
│   │   │   ├── context.py          #   system prompt + auto-recall from persistent memory
│   │   │   ├── skills.py           #   skill loader (77 bundled + user-created via CRUD)
│   │   │   ├── tools.py            #   tool base class + registry
│   │   │   ├── memory.py           #   lightweight workspace state per run
│   │   │   ├── frontmatter.py      #   shared YAML frontmatter parser
│   │   │   └── trace.py            #   execution trace writer
│   │   │
│   │   ├── memory/                 # Cross-session persistent memory
│   │   │   └── persistent.py       #   file-based memory (~/.vibe-trading/memory/)
│   │   │
│   │   ├── tools/                  # 31 auto-discovered agent tools
│   │   │   ├── backtest_tool.py    #   run backtests
│   │   │   ├── remember_tool.py    #   cross-session memory (save/recall/forget)
│   │   │   ├── skill_writer_tool.py #  skill CRUD (save/patch/delete/file)
│   │   │   ├── session_search_tool.py # FTS5 cross-session search
│   │   │   ├── swarm_tool.py       #   launch swarm teams
│   │   │   ├── web_search_tool.py  #   DuckDuckGo web search
│   │   │   └── ...                 #   bash, file I/O, factor analysis, options, alpha browser + bench, etc.
│   │   │
│   │   ├── factors/                # Alpha Zoo — 452 alphas across 4 zoos
│   │   │   ├── base.py             #   19 operators (rank/scale/ts_*/delta/decay_linear/safe_div/vwap)
│   │   │   ├── registry.py         #   AST-only metadata load + lazy compute + sanity gates
│   │   │   ├── bench_runner.py     #   IC + alive/reversed/dead categorisation
│   │   │   └── zoo/                #   qlib158 (154) + alpha101 (101) + gtja191 (191) + academic (6)
│   │   │
│   │   ├── api/                    # FastAPI route modules
│   │   │   └── alpha_routes.py     #   /alpha/list, /alpha/{id}, /alpha/bench, SSE stream
│   │   │
│   │   ├── skills/                 # 77 finance skills in 8 categories (SKILL.md each)
│   │   ├── swarm/                  # Swarm DAG execution engine
│   │   │   └── presets/            #   29 swarm preset YAML definitions
│   │   ├── session/                # Multi-turn chat + FTS5 session search
│   │   └── providers/              # LLM provider abstraction
│   │
│   └── backtest/                   # Backtest engines
│       ├── engines/                #   7 engines + composite cross-market engine + options_portfolio
│       ├── loaders/                #   7 sources: tushare, okx, yfinance, akshare, mootdx, ccxt, futu
│   │   │   ├── base.py             #   DataLoader Protocol
│   │   │   └── registry.py         #   Registry + auto-fallback chains
│       └── optimizers/             #   MVO, equal vol, max div, risk parity
│
├── frontend/                       # Web UI (React 19 + Vite + TypeScript)
│   └── src/
│       ├── pages/                  #   Home, Agent, AlphaZoo, RunDetail, Compare, Correlation, Settings
│       ├── components/             #   chat, charts, layout
│       └── stores/                 #   Zustand state management
│
├── Dockerfile                      # Multi-stage build
├── docker-compose.yml              # One-command deploy
├── pyproject.toml                  # Package config + CLI entrypoint
├── tools/                          # Repo-level CI helpers
│   └── ci_grep_gates.sh            # rejects yaml.load / trademark / per-stock-data leaks
└── LICENSE                         # MIT
```

</details>

---

## 🏛 生态系统

Vibe-Trading 是 **[HKUDS](https://github.com/HKUDS)** 代理生态系统的组成部分：

<table>
  <tr>
    <td align="center" width="20%">
      <a href="https://github.com/HKUDS/nanobot"><b>NanoBot</b></a><br>
      <sub>超轻量个人 AI 助手</sub>
    </td>
    <td align="center" width="20%">
      <a href="https://github.com/HKUDS/AI-Trader"><b>AI-Trader</b></a><br>
      <sub>Agent-Native 信号与跟单交易平台</sub>
    </td>
    <td align="center" width="20%">
      <a href="https://github.com/HKUDS/CLI-Anything"><b>CLI-Anything</b></a><br>
      <sub>让所有软件具备 Agent-Native 能力</sub>
    </td>
    <td align="center" width="20%">
      <a href="https://github.com/HKUDS/OpenSpace"><b>OpenSpace</b></a><br>
      <sub>自进化 AI 代理技能</sub>
    </td>
    <td align="center" width="20%">
      <a href="https://github.com/HKUDS/ClawTeam"><b>ClawTeam</b></a><br>
      <sub>Agent Swarm Intelligence</sub>
    </td>
  </tr>
</table>

---

## 🗺 路线图

> 我们分阶段发布。工作开始时项目会移至 [Issues](https://github.com/HKUDS/Vibe-Trading/issues)。

| Phase | Feature | Status |
|-------|---------|--------|
| **Trust Layer** | 可复现的运行卡片已生成并在运行详情页展示；v1 增加工具追踪和引用 | v0 Shipped |
| **Hypothesis Registry** | 持久化研究假设，含生命周期状态、数据源、技能、运行卡片链接及失效注释 | Backend MVP Shipped |
| **Research Autopilot** | 手动优先的研究循环：假设 → 确定性回测 → 证据报告 | Next |
| **Data Bridge** | Bring-your-own data：本地 CSV/Parquet/SQL 连接器与模式映射 | Planned |
| **Options Lab** | Vol surface、Greeks 仪表板、收益曲线/情景探索器 | Planned |
| **Portfolio Studio** | Risk x-ray、约束条件、换手率感知优化器、再平衡注释 | Planned |
| **Alpha Zoo** | 452 个预构建 Alpha（Qlib 158 + Kakushadze 101 + GTJA 191 + FF5 + Carhart），支持一键基准测试、代理集成与 Web UI | **Shipped 0.1.8** |
| **Research Delivery** | 定时简报发送至 Slack / Telegram / 邮件类渠道 | Planned |
| **Community** | 可共享的技能、预设和策略卡片 | Exploring |

---

## Contributing

欢迎贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md) 获取指南。

**Good first issues** 已标记为 [`good first issue`](https://github.com/HKUDS/Vibe-Trading/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) —— 挑选一个并开始吧。

想贡献更大内容？查看上方的 [路线图](#-roadmap) 并在开始前开 Issue 讨论。

---

## Contributors

感谢所有为 Vibe-Trading 做出贡献的人！

近期 v0.1.9 周期贡献者与致谢：

- @toanalien — session JSONL 崩溃加固 (#147)、迭代预算内优雅代理循环退出 (#148)、LLM 生成信号引擎的预飞行验证 (#149) 以及跨浏览器完整报告链接 (#150)
- @ai7eam-dev — 跨市场相关性时间戳对齐 (#158) 与会话运行状态指示器 + 蜂群重试 (#159 → #160)
- @shadowinlife — SSE/HTTP 远程 MCP 服务器 (#125) 与操作员配置的蜂群 Worker 外部 MCP 工具 (#142)
- @DoubleSky123 — 可配置 SSE 空闲超时 (#157)
- @ArthurXi — Web 编辑器中的 IME Enter 提交处理 (#146)
- @omcdecor-cyber — 上游任务失败时的蜂群 DAG 门控 (#145)
- @Soli22de — 强制随机对照的严格 Alpha 基准模式 (#143)
- @ruok808 — CCXT 加载器中的代理环境变量支持 (#126)
- @faizack — 远程 Ollama 基础 URL 归一化 (#129)
- @fightZy — 代理会话历史加载修复 (#136)
- @lcwSeven — Alpha 列表端点中的短标的池名称 (#137)
- @Teerapat-Vatpitak — 解决 .env-source 日志记录 (#124)
- @warren618 / Haozhe Wu — 以连接器为核心的券商配置档案、Robinhood Agentic Trading 通道、Research Goal 运行时、蜂群对账 + retry_run、agent/cli 重构、mootdx 加载器及发布集成

<a href="https://github.com/HKUDS/Vibe-Trading/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/Vibe-Trading" />
</a>

---

## Disclaimer

Vibe-Trading 是研究与交易软件。它不是投资建议，不持有资金，也不运行任何交易场所。通过你明确授权的券商通道（例如 Robinhood Agentic Trading）进行的交易仅在你设定的限制内发生，且你可随时停止该通道。此券商交易功能为实验性，未经我们针对真实券商账户验证 —— 请自行评估风险后使用。过往业绩不保证未来结果。

## License

MIT License — see [LICENSE](LICENSE)

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=HKUDS/Vibe-Trading&type=Date)](https://star-history.com/#HKUDS/Vibe-Trading&Date)

<p align="center">
  ⭐ 如果 <b>Vibe-Trading</b> 对你的研究有帮助，一个 Star 能帮助更多人找到它。
</p>

---

<p align="center">
  感谢访问 <b>Vibe-Trading</b> ✨
</p>
<p align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.Vibe-Trading&style=flat" alt="visitors"/>
</p>