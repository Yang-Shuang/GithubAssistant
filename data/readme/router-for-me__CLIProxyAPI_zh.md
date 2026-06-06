# CLI Proxy API

English | [中文](README_CN.md) | [日本語](README_JA.md)

一个为 CLI 提供兼容 OpenAI/Gemini/Claude/Codex/Grok API 接口的代理服务器。

现在也支持通过 OAuth 登录使用 OpenAI Codex（GPT 模型）和 Claude Code。

因此，你可以使用本地或多账号的 CLI 访问方式，配合兼容 OpenAI（含 Responses API）/Gemini/Claude 的客户端和 SDK。

## Sponsor

[![https://www.packyapi.com/register?aff=cliproxyapi](./assets/packycode-en.png)](https://www.packyapi.com/register?aff=cliproxyapi)

感谢 PackyCode 对本项目的赞助！

PackyCode 是一家可靠高效的 API 中转服务提供商，提供 Claude Code、Codex、Gemini 等服务的代理中继。

PackyCode 为软件用户提供专属优惠：使用 <a href="https://www.packyapi.com/register?aff=cliproxyapi">此链接</a> 注册，并在充值时输入促销代码“cliproxyapi”，即可享受 9 折优惠。

---

<table>
<tbody>
<tr>
<td width="180"><a href="https://www.aicodemirror.com/register?invitecode=TJNAIF"><img src="./assets/aicodemirror.png" alt="AICodeMirror" width="150"></a></td>
<td>感谢 AICodeMirror 对本项目的赞助！AICodeMirror 为 Claude Code / Codex / Gemini CLI 提供官方高稳定性中继服务，拥有企业级并发处理能力、快速发票开具功能以及全天候专属技术支持。Claude Code / Codex / Gemini 官方渠道价格低至原价的 38% / 2% / 9%，充值还可额外享受折扣！AICodeMirror 为 CLIProxyAPI 用户提供专属福利：通过 <a href="https://www.aicodemirror.com/register?invitecode=TJNAIF">此链接</a> 注册，首充立减 20%，企业客户最高可享 75 折优惠！</td>
</tr>
<tr>
<td width="180"><a href="https://shop.bmoplus.com/?utm_source=github"><img src="./assets/bmoplus.png" alt="BmoPlus" width="150"></a></td>
<td>衷心感谢 BmoPlus 对本项目的赞助！BmoPlus 是一家专为重度 AI 用户和开发者打造的高可靠性 AI 账号提供商。他们提供开箱即用、稳定可靠的 ChatGPT Plus / ChatGPT Pro（全保）/ Claude Pro / Super Grok / Gemini Pro 账号及官方充值服务。通过 <a href="https://shop.bmoplus.com/?utm_source=github">BmoPlus - 高级 AI 账号与充值</a> 注册下单，用户可享受低至<b>官方 GPT 订阅价格 10%（9 折优惠）</b>的惊人费率！</td>
</tr>
<tr>
<td width="180"><a href="https://coder.visioncoder.cn"><img src="./assets/visioncoder.png" alt="VisionCoder" width="150"></a></td>
<td>感谢 <b>VisionCoder</b> 对本项目的支持。<a href="https://coder.visioncoder.cn" target="_blank">VisionCoder 开发者平台</a> 是一家可靠高效的 API 中继服务提供商，提供 Claude Code、Codex、Gemini 等主流 AI 模型的接入服务。它帮助开发者和团队更轻松地集成 AI 能力并提升生产力。<p></p>VisionCoder 还为用户推出限时 <a href="https://coder.visioncoder.cn" target="_blank">Token 套餐</a> 优惠活动：<b>买一送一（购买 1 个月赠送 1 个月）</b>。</td>
</tr>
<tr>
<td width="180"><a href="https://apikey.fun/register?aff=CLIProxyAPI"><img src="./assets/apikey.png" alt="APIKEY.FUN" width="150"></a></td>
<td>感谢 APIKEY.FUN 对本项目的赞助！APIKEY.FUN 是一家专业的企业级 AI 中继平台，致力于为企业和独立开发者提供稳定、高效且低成本的 AI 模型 API 接入服务。平台支持 Claude、OpenAI、Gemini 等热门主流模型，价格低至官方价格的 7%。通过本项目 <a href="https://apikey.fun/register?aff=CLIProxyAPI">专属链接</a> 注册，即可享受<b>永久充值 5% 折扣</b>的特别优惠。</td>
</tr>
</tbody>
</table>

## Overview

- 兼容 OpenAI/Gemini/Claude/Grok 的 CLI 模型 API 端点
- 支持通过 OAuth 登录使用 OpenAI Codex（GPT 模型）
- 支持通过 OAuth 登录使用 Claude Code
- 支持通过 OAuth 登录使用 Grok Build
- 支持带提供商路由的 Amp CLI 及 IDE 扩展
- 支持流式、非流式及 WebSocket 响应（视情况而定）
- 支持函数调用/工具使用
- 支持多模态输入（文本与图像）
- 多账号轮询负载均衡（Gemini、OpenAI、Claude、Grok）
- 简化的 CLI 认证流程（Gemini、OpenAI、Claude、Grok）
- 生成式语言 API Key 支持
- AI Studio Build 多账号负载均衡
- Gemini CLI 多账号负载均衡
- Claude Code 多账号负载均衡
- OpenAI Codex 多账号负载均衡
- Grok Build 多账号负载均衡
- 通过配置支持兼容 OpenAI 的上游提供商（如 OpenRouter）
- 可复用的 Go SDK 用于嵌入代理（详见 `docs/sdk-usage.md`）

## Getting Started

CLIProxyAPI 使用指南：[https://help.router-for.me/](https://help.router-for.me/)

## Management API

详见 [MANAGEMENT_API.md](https://help.router-for.me/management/api)

## Usage Statistics

自 v6.10.0 版本起，CLIProxyAPI 和 [CPAMC](https://github.com/router-for-me/Cli-Proxy-API-Management-Center) 不再内置使用统计功能。如需使用统计数据，请采用以下方案：

### [CPA Usage Keeper](https://github.com/Willxup/cpa-usage-keeper)

面向 CLIProxyAPI 的独立数据持久化与可视化服务，支持定期数据同步、SQLite 存储、聚合 API，并内置用于使用统计的面板。

### [CPA-Manager-Plus](https://github.com/seakee/CPA-Manager-Plus)

完整的 CLIProxyAPI 管理中心，支持请求级监控与成本估算。CPA-Manager 按账号、模型、渠道、延迟、状态和 Token 用量追踪收集的请求；支持通过可编辑的模型价格及一键同步 LiteLLM 价格来估算成本；将事件持久化至 SQLite；并提供 Codex 账号池操作功能，包括批量检查、配额检测、异常账号发现、清理建议以及用于日常多账号维护的一键执行工具。

## SDK Docs

- Usage: [docs/sdk-usage.md](docs/sdk-usage.md)
- Advanced (executors & translators): [docs/sdk-advanced.md](docs/sdk-advanced.md)
- Access: [docs/sdk-access.md](docs/sdk-access.md)
- Watcher: [docs/sdk-watcher.md](docs/sdk-watcher.md)
- Custom Provider Example: `examples/custom-provider`

## Contributing

欢迎贡献代码！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开 Pull Request

## Who is with us?

以下项目基于 CLIProxyAPI 开发：

### [vibeproxy](https://github.com/automazeio/vibeproxy)

原生 macOS 菜单栏应用，用于在 AI 编程工具中使用你的 Claude Code & ChatGPT 订阅——无需 API Key。

### [Subtitle Translator](https://github.com/VjayC/SRT-Subtitle-Translator-Validator)

跨平台桌面与网页应用，通过 CLIProxyAPI 利用现有的 LLM 订阅（Gemini、ChatGPT、Claude 等）翻译和验证 SRT 字幕文件——无需 API Key。

### [CCS (Claude Code Switch)](https://github.com/kaitranntt/ccs)

CLI 包装器，可通过 CLIProxyAPI OAuth 在多个 Claude 账号及替代模型（Gemini、Codex、Antigravity）间即时切换——无需 API Key。

### [Quotio](https://github.com/nguyenphutrong/quotio)

原生 macOS 菜单栏应用，统一整合 Claude、Gemini、OpenAI 和 Antigravity 订阅，提供实时配额追踪与智能自动故障转移功能，适用于 Claude Code、OpenCode、Droid 等 AI 编程工具——无需 API Key。

### [ProxyPilot](https://github.com/Finesssee/ProxyPilot)

Windows 原生的 CLIProxyAPI Fork 版本，内置 TUI（终端用户界面）、系统托盘及多提供商 OAuth 支持，专为 AI 编程工具设计——无需 API Key。

### [Claude Proxy VSCode](https://github.com/uzhao/claude-proxy-vscode)

VSCode 扩展插件，用于快速切换 Claude Code 模型，后端集成 CLIProxyAPI 并自动管理后台生命周期。

### [ZeroLimit](https://github.com/0xtbug/zero-limit)

基于 Tauri + React 构建的 Windows 桌面应用，通过 CLIProxyAPI 监控 AI 编程助手配额。支持跨 Gemini、Claude、OpenAI Codex 和 Antigravity 账号实时追踪使用情况，内置仪表盘、系统托盘集成及一键代理控制——无需 API Key。

### [CPA-XXX Panel](https://github.com/ferretgeek/CPA-X)

轻量级 CLIProxyAPI Web 管理面板，提供健康检查、资源监控、实时日志、自动更新、请求统计与价格显示。支持一键安装及 systemd 服务配置。

### [CLIProxyAPI Tray](https://github.com/kitephp/CLIProxyAPI_Tray)

使用 PowerShell 脚本实现的 Windows 托盘应用，不依赖任何第三方库。主要功能包括：快捷方式自动生成、静默运行、密码管理、频道切换（Main / Plus）以及自动下载与更新。

### [霖君](https://github.com/wangdabaoqq/LinJun)

跨平台桌面应用程序，用于管理 AI 编程助手，支持 macOS、Windows 和 Linux 系统。统一管理 Claude Code、Gemini CLI、OpenAI Codex 等 AI 编程工具，提供本地代理实现多账号配额追踪及一键配置。

### [CLIProxyAPI Dashboard](https://github.com/itsmylife44/cliproxyapi-dashboard)

基于 Next.js、React 和 PostgreSQL 构建的现代 Web 管理面板。支持实时日志流式传输、结构化配置编辑、API Key 管理、Claude/Gemini/Codex OAuth 集成、使用数据分析、容器管理及通过配套插件与 OpenCode 同步配置——无需手动编辑 YAML 文件。

### [All API Hub](https://github.com/qixing-jk/all-api-hub)

浏览器扩展，用于一站式管理 New API 兼容中继站账号。具备余额与用量仪表盘、自动签到、一键导出 Key 至常用应用、页面内 API 可用性测试及频道/模型同步重定向功能。通过 Management API 集成 CLIProxyAPI，支持一键导入提供商并同步配置。

### [Shadow AI](https://github.com/HEUDavid/shadow-ai)

专为受限环境设计的 AI 助手工具。提供无窗口、无痕的隐蔽运行模式，并通过局域网（LAN）实现跨设备 AI 问答交互与控制。本质上是一个“屏幕/音频捕获 + AI 推理 + 低摩擦交付”的自动化协作层，帮助用户在受控设备或受限环境中沉浸式地使用 AI 助手。

### [ProxyPal](https://github.com/buddingnewinsights/proxypal)

跨平台桌面应用（macOS、Windows、Linux），为 CLIProxyAPI 提供原生 GUI 封装。可连接 Claude、ChatGPT、Gemini、GitHub Copilot 及自定义 OpenAI 兼容端点，支持使用统计、请求监控及热门编程工具的自动配置——无需 API Key。

### [CLIProxyAPI Quota Inspector](https://github.com/AllenReder/CLIProxyAPI-Quota-Inspector)

开箱即用的跨平台配额检查工具，支持按账号查看 Codex 5小时/7天配额窗口、基于套餐的排序、状态着色显示及多账号汇总分析。

### [CLIProxy Pool Watch](https://github.com/murasame612/CLIProxyPoolWidget)

原生 macOS SwiftUI 应用，用于监控 CLIProxyAPI 池中的 ChatGPT/Codex 账号配额。通过 Management API 展示账号可用性、Plus 基础容量、5小时与每周配额进度条、套餐权重及恢复预测。

### [Panopticon](https://github.com/eltmon/panopticon-cli)

AI 编程助手的智能体编排工具。将 CLIProxyAPI 作为本地 Sidecar 运行，使其智能体能够通过 ChatGPT 订阅驱动 GPT 模型，并将 Claude Code 指向 Anthropic 兼容端点——无需 OpenAI API Key。

### [Tunnel Agent](https://github.com/Villoh/tunnel-agent)

Windows 桌面 UI，从单一界面管理 CLIProxyAPI 和 Perplexity WebUI Scraper（受 Quotio 和 VibeProxy 启发）。可连接 OAuth 提供商（Claude、Gemini CLI、Codex、Kimi、Antigravity）、自定义 API Key 及 Perplexity 会话账号，随后将任意编程智能体指向本地端点。

> [!NOTE]  
> 如果你开发了基于 CLIProxyAPI 的项目，请提交 Pull Request 将其添加至此列表。

## More choices

以下项目为 CLIProxyAPI 的移植版本或受其启发：

### [9Router](https://github.com/decolua/9router)

受 CLIProxyAPI 启发的 Next.js 实现版本，安装使用简便。从零构建格式转换（OpenAI/Claude/Gemini/Ollama）、带自动故障转移的组合系统、支持指数退避的多账号管理、Next.js Web 面板，并兼容 CLI 工具（Cursor、Claude Code、Cline、RooCode）——无需 API Key。

### [OmniRoute](https://github.com/diegosouzapw/OmniRoute)

永不中断编码。智能路由至免费及低成本 AI 模型，具备自动故障转移功能。
OmniRoute 是多提供商 LLM 的 AI 网关：提供 OpenAI 兼容端点，支持智能路由、负载均衡、重试与降级策略。可添加策略、速率限制、缓存和可观测性，以实现可靠且成本可控的推理服务。

### [Playful Proxy API Panel (PPAP)](https://github.com/daishuge/playful-proxy-api-panel)

一个公开可用的 CLIProxyAPI 兼容 Fork 版本及捆绑管理面板。保留上游风格的使用体验的同时恢复内置使用统计功能，新增缓存命中率、首字节延迟、TPS 追踪及面向 Docker 的自托管安装文档。

### [Codex Switch](https://github.com/9ycrooked/CodexSwitch)

基于 Tauri 2 + Vue 3 构建的工具，用于管理多个 OpenAI Codex 桌面账号。支持在保存的 ChatGPT/Codex 认证配置文件间切换，实时查看 5小时与每周配额使用情况，验证 Token 健康度，查看活跃账号详情，并导入或保存 auth.json 文件而无需手动复制。

> [!NOTE]  
> 如果你开发了 CLIProxyAPI 的移植版本或受其启发的项目，请提交 Pull Request 将其添加至此列表。

## License

本项目采用 MIT 许可证开源——详见 [LICENSE](LICENSE) 文件。