<div align="center">
  <img src="./images/9router.png?1" alt="9Router Dashboard" width="800"/>
  
  # 9Router - 免费 AI 路由与令牌（Token）节省工具
  
  **持续编码，永不中断。通过 RTK + 自动回退至免费及低价 AI 模型，节省 20-40% 的 Token。**
  
  **连接所有 AI 编程工具（Claude Code、Cursor、Antigravity、Copilot、Codex、Gemini、OpenCode、Cline、OpenClaw...）至 40+ AI 服务商与 100+ 模型。**
  
  [![npm](https://img.shields.io/npm/v/9router.svg)](https://www.npmjs.com/package/9router)
  [![Downloads](https://img.shields.io/npm/dm/9router.svg)](https://www.npmjs.com/package/9router)
  [![Docker Pulls](https://img.shields.io/docker/pulls/decolua/9router.svg?logo=docker&label=Docker%20pulls)](https://hub.docker.com/r/decolua/9router)
  [![GHCR](https://img.shields.io/badge/GHCR-decolua%2F9router-blue?logo=github)](https://github.com/decolua/9router/pkgs/container/9router)
  [![License](https://img.shields.io/npm/l/9router.svg)](https://github.com/decolua/9router/blob/main/LICENSE)

  <a href="https://trendshift.io/repositories/22628" target="_blank"><img src="https://trendshift.io/api/badge/repositories/22628" alt="decolua%2F9router | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
  
  [🚀 快速入门](#-quick-start) • [💡 核心功能](#-key-features) • [📖 设置指南](#-setup-guide) • [🌐 官网](https://9router.com)

  [🇻🇳 Tiếng Việt](./i18n/README.vi.md) • [🇨🇳 中文](./i18n/README.zh-CN.md) • [🇯🇵 日本語](./i18n/README.ja-JP.md)
</div>

---

## 🤔 为什么选择 9Router？

**停止浪费金钱、Token 和触发限额：**

- ❌ 每月订阅额度未用完即过期
- ❌ 编码中途遇到速率限制（Rate Limits）
- ❌ 工具输出（git diff、grep、ls...）快速消耗 Token
- ❌ 昂贵的 API 费用（每个服务商 $20-$50/月）
- ❌ 手动在不同服务商之间切换

**9Router 解决这些问题：**

- ✅ **RTK 令牌节省器** - 自动压缩 tool_result 内容，每次请求节省 20-40% Token
- ✅ **最大化订阅价值** - 跟踪额度，在重置前用尽每一分配额
- ✅ **自动回退（Fallback）** - 订阅版 → 低价版 → 免费版，零停机时间
- ✅ **多账号支持** - 按服务商轮询使用多个账号
- ✅ **通用兼容** - 完美适配 Claude Code、Codex、Cursor、Cline 及任意 CLI 工具

---

## 🔄 工作原理

```
┌─────────────┐
│   你的 CLI    │  (Claude Code, Codex, OpenClaw, Cursor, Cline...)
│   工具       │
└──────┬──────┘
       │ http://localhost:20128/v1
       ↓
┌─────────────────────────────────────────────┐
│           9Router（智能路由）               │
│  • RTK 令牌节省器 (削减 tool_result Token)  │
│  • 格式转换 (OpenAI ↔ Claude)              │
│  • 额度跟踪                               │
│  • Token 自动刷新                         │
└──────┬──────────────────────────────────────┘
       │
       ├─→ [第一级：订阅版] Claude Code, Codex, GitHub Copilot
       │   ↓ 配额耗尽
       ├─→ [第二级：低价版] GLM ($0.6/1M), MiniMax ($0.2/1M)
       │   ↓ 预算限制
       └─→ [第三级：免费版] Kiro, OpenCode Free, Vertex ($300 额度)

结果：持续编码，成本最低 + RTK 节省 20-40% Token
```

---

## ⚡ 快速入门

**1. 全局安装：**

```bash
npm install -g 9router
9router
```

🎉 控制面板将在 `http://localhost:20128` 打开

**2. 连接一个免费服务商（无需注册）：**

控制面板 → Providers → 连接 **Kiro AI**（免费无限 Claude）或 **OpenCode Free**（免认证）→ 完成！

**3. 在你的 CLI 工具中使用：**

```
Claude Code/Codex/OpenClaw/Cursor/Cline Settings:
  Endpoint: http://localhost:20128/v1
  API Key: [从控制面板复制]
  Model: kr/claude-sonnet-4.5
```

**就是这样！** 开始使用免费 AI 模型进行编码。

**替代方案：从源码运行（本仓库）：**

本仓库包为私有 (`9router-app`)，因此源码/Docker 执行是预期的本地开发路径。

```bash
cp .env.example .env
npm install
PORT=20128 NEXT_PUBLIC_BASE_URL=http://localhost:20128 npm run dev
```

生产模式：

```bash
npm run build
PORT=20128 HOSTNAME=0.0.0.0 NEXT_PUBLIC_BASE_URL=http://localhost:20128 npm run start
```

默认访问地址：
- 控制面板：`http://localhost:20128/dashboard`
- OpenAI 兼容 API：`http://localhost:20128/v1`

---

## 📹 视频教程

<div align="center">

<table>
  <tr>
    <td align="center" width="320">
      <a href="https://www.youtube.com/watch?v=raEyZPg5xE0">
        <img src="https://img.youtube.com/vi/raEyZPg5xE0/maxresdefault.jpg" alt="9Router Setup Tutorial" width="300"/>
      </a><br/>
      <b>🇺🇸 英文</b><br/>
      <sub>9Router + Claude Code 免费配置指南<br/>by <a href="https://www.youtube.com/@BuildAIWithHamid">Build AI With Hamid</a></sub>
    </td>
    <td align="center" width="320">
      <a href="https://www.youtube.com/watch?v=X69n5Lm06Yw">
        <img src="https://img.youtube.com/vi/X69n5Lm06Yw/maxresdefault.jpg" alt="Tiết kiệm chi phí LLM với 9Router" width="300"/>
      </a><br/>
      <b>🇻🇳 越南语</b><br/>
      <sub>使用 9Router 降低 OpenClaw LLM 成本<br/>by <a href="https://www.youtube.com/c/M%C3%ACAIblog">Mì AI</a></sub>
    </td>
    <td align="center" width="320">
      <a href="https://www.youtube.com/watch?v=o3qYCyjrFYg">
        <img src="https://img.youtube.com/vi/o3qYCyjrFYg/maxresdefault.jpg" alt="Claude Code FREE Forever" width="300"/>
      </a><br/>
      <b>🇺🇸 英文</b><br/>
      <sub>Claude Code 永久免费 — 无限模型<br/>by <a href="https://www.youtube.com/@BuildAIWithHamid">Build AI With Hamid</a></sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="320">
      <a href="https://www.youtube.com/watch?v=Ttpc26m39Dw">
        <img src="https://img.youtube.com/vi/Ttpc26m39Dw/maxresdefault.jpg" alt="Claude CLI Free Setup" width="300"/>
      </a><br/>
      <b>🇺🇸 英文</b><br/>
      <sub>Claude CLI 免费配置指南 🚀<br/>by <a href="https://www.youtube.com/@CodeVerseSoban">CodeVerse Soban</a></sub>
    </td>
    <td align="center" width="320">
      <a href="https://www.youtube.com/watch?v=G-5A_D5Pm6Y">
        <img src="https://img.youtube.com/vi/G-5A_D5Pm6Y/maxresdefault.jpg" alt="Cài đặt OpenClaw Free A-Z" width="300"/>
      </a><br/>
      <b>🇻🇳 越南语</b><br/>
      <sub>OpenClaw 免费从零到一配置 + 9Router<br/>by <a href="https://www.youtube.com/@maigia">Mai Gia</a></sub>
    </td>
    <td align="center" width="320">
      <a href="https://www.youtube.com/watch?v=JXmg8_gccgE">
        <img src="https://img.youtube.com/vi/JXmg8_gccgE/maxresdefault.jpg" alt="FREE OpenClaw with Claude Opus" width="300"/>
      </a><br/>
      <b>🇺🇸 英文</b><br/>
      <sub>免费使用 OpenClaw + Claude Opus 4.6<br/>by <a href="https://www.youtube.com/@BuildAIWithHamid">Build AI With Hamid</a></sub>
    </td>
  </tr>
</table>

</div>

> 🎬 **制作了关于 9Router 的视频？** 提交 [Pull Request](https://github.com/decolua/9router/pulls) 将你的视频添加到此部分，我们会合并！

---

## 🛠️ 支持的 CLI 工具

9Router 与所有主流 AI 编程工具无缝协作：

<div align="center">
  <table>
    <tr>
      <td align="center" width="120">
        <img src="./public/providers/claude.png" width="60" alt="Claude Code"/><br/>
        <b>Claude-Code</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/openclaw.png" width="60" alt="OpenClaw"/><br/>
        <b>OpenClaw</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/codex.png" width="60" alt="Codex"/><br/>
        <b>Codex</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/opencode.png" width="60" alt="OpenCode"/><br/>
        <b>OpenCode</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/cursor.png" width="60" alt="Cursor"/><br/>
        <b>Cursor</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/antigravity.png" width="60" alt="Antigravity"/><br/>
        <b>Antigravity</b>
      </td>
    </tr>
    <tr>
      <td align="center" width="120">
        <img src="./public/providers/cline.png" width="60" alt="Cline"/><br/>
        <b>Cline</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/continue.png" width="60" alt="Continue"/><br/>
        <b>Continue</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/droid.png" width="60" alt="Droid"/><br/>
        <b>Droid</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/roo.png" width="60" alt="Roo"/><br/>
        <b>Roo</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/copilot.png" width="60" alt="Copilot"/><br/>
        <b>Copilot</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/kilocode.png" width="60" alt="Kilo Code"/><br/>
        <b>Kilo Code</b>
      </td>
    </tr>
  </table>
</div>

---

## 🌐 支持的服务商

### 🔐 OAuth 服务商

<div align="center">
  <table>
    <tr>
      <td align="center" width="120">
        <img src="./public/providers/claude.png" width="60" alt="Claude Code"/><br/>
        <b>Claude-Code</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/antigravity.png" width="60" alt="Antigravity"/><br/>
        <b>Antigravity</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/codex.png" width="60" alt="Codex"/><br/>
        <b>Codex</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/github.png" width="60" alt="GitHub"/><br/>
        <b>GitHub</b>
      </td>
      <td align="center" width="120">
        <img src="./public/providers/cursor.png" width="60" alt="Cursor"/><br/>
        <b>Cursor</b>
      </td>
    </tr>
  </table>
</div>

### 🆓 免费服务商

<div align="center">
  <table>
    <tr>
      <td align="center" width="150">
        <img src="./public/providers/kiro.png" width="70" alt="Kiro"/><br/>
        <b>Kiro AI</b><br/>
        <sub>Claude 4.5 + GLM-5 + MiniMax<br/>无限免费</sub>
      </td>
      <td align="center" width="150">
        <img src="./public/providers/opencode.png" width="70" alt="OpenCode Free"/><br/>
        <b>OpenCode Free</b><br/>
        <sub>免认证 • 自动获取模型<br/>无限免费</sub>
      </td>
      <td align="center" width="150">
        <img src="./public/providers/gemini.png" width="70" alt="Vertex AI"/><br/>
        <b>Vertex AI</b><br/>
        <sub>Gemini 3 Pro + GLM-5 + DeepSeek<br/>新用户赠 $300 额度</sub>
      </td>
    </tr>
  </table>
</div>

> **注意：** iFlow、Qwen 和 Gemini CLI 的免费层已于 2026 年下线。请改用 Kiro / OpenCode Free / Vertex。

### 🔑 API Key 服务商（40+）

<div align="center">
  <table>
    <tr>
      <td align="center" width="100">
        <img src="./public/providers/openrouter.png" width="50" alt="OpenRouter"/><br/>
        <sub>OpenRouter</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/glm.png" width="50" alt="GLM"/><br/>
        <sub>GLM</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/kimi.png" width="50" alt="Kimi"/><br/>
        <sub>Kimi</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/minimax.png" width="50" alt="MiniMax"/><br/>
        <sub>MiniMax</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/openai.png" width="50" alt="OpenAI"/><br/>
        <sub>OpenAI</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/anthropic.png" width="50" alt="Anthropic"/><br/>
        <sub>Anthropic</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="100">
        <img src="./public/providers/gemini.png" width="50" alt="Gemini"/><br/>
        <sub>Gemini</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/deepseek.png" width="50" alt="DeepSeek"/><br/>
        <sub>DeepSeek</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/groq.png" width="50" alt="Groq"/><br/>
        <sub>Groq</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/xai.png" width="50" alt="xAI"/><br/>
        <sub>xAI</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/mistral.png" width="50" alt="Mistral"/><br/>
        <sub>Mistral</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/perplexity.png" width="50" alt="Perplexity"/><br/>
        <sub>Perplexity</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="100">
        <img src="./public/providers/together.png" width="50" alt="Together"/><br/>
        <sub>Together AI</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/fireworks.png" width="50" alt="Fireworks"/><br/>
        <sub>Fireworks</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/cerebras.png" width="50" alt="Cerebras"/><br/>
        <sub>Cerebras</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/cohere.png" width="50" alt="Cohere"/><br/>
        <sub>Cohere</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/nvidia.png" width="50" alt="NVIDIA"/><br/>
        <sub>NVIDIA</sub>
      </td>
      <td align="center" width="100">
        <img src="./public/providers/siliconflow.png" width="50" alt="SiliconFlow"/><br/>
        <sub>SiliconFlow</sub>
      </td>
    </tr>
  </table>
  <p><i>...以及包括 Nebius、Chutes、Hyperbolic 和自定义 OpenAI/Anthropic 兼容端点在内的 20+ 个服务商</i></p>
</div>

---

## 💡 核心功能

| 功能 | 作用 | 为什么重要 |
|---------|--------------|----------------|
| 🚀 **RTK 令牌节省器** ([RTK](https://github.com/rtk-ai/rtk) ⭐40K) | 在发送给 LLM 前压缩工具输出（`git diff`、`grep`、`ls`、`tree`...） | 每次请求节省 **20-40% 输入 Token** |
| 🪨 **原始人模式** ([Caveman](https://github.com/JuliusBrussee/caveman) ⭐52K) | 注入原始人风格提示词 → LLM 回复更精简，保留技术实质内容 | 节省 **高达 65% 输出 Token** |
| 🎯 **智能三级回退机制** | 自动路由：订阅版 → 低价版 → 免费版 | 持续编码不中断，零停机时间 |
| 📊 **实时额度跟踪** | 动态显示 Token 数量 + 重置倒计时 | 最大化订阅价值 |
| 🔄 **格式转换** | OpenAI ↔ Claude ↔ Gemini ↔ Cursor ↔ Kiro ↔ Vertex | 兼容任意 CLI 工具 |
| 👥 **多账号支持** | 每个服务商配置多个账号 | 负载均衡 + 冗余保障 |
| 🔄 **Token 自动刷新** | OAuth Token 自动续期 | 无需手动重新登录 |
| 🎨 **自定义组合（Combos）** | 创建无限模型组合 | 按需定制回退策略 |
| 📝 **请求日志记录** | 调试模式，完整记录请求/响应 | 轻松排查问题 |
| 💾 **云端同步** | 跨设备同步配置 | 随时随地保持相同设置 |
| 📊 **使用分析** | 跟踪 Token、成本及长期趋势 | 优化支出结构 |
| 🌐 **任意部署** | 本地主机、VPS、Docker、Cloudflare Workers | 灵活的部署选项 |

<details>
<summary><b>📖 功能详情</b></summary>

### 🚀 RTK 令牌节省器

工具输出（`git diff`、`grep`、`find`、`ls`、`tree`、日志转储...）通常会消耗你提示词预算的 30-50%。RTK 会检测这些内容，并在请求到达 LLM **之前**应用智能无损压缩：

- **过滤器：** `git-diff`、`git-status`、`grep`、`find`、`ls`、`tree`、`dedup-log`、`smart-truncate`、`read-numbered`、`search-list`
- **自动检测：** 无需配置 — RTK 会查看每个 `tool_result` 的前 1KB，并自动选择正确的过滤器。
- **安全设计：** 如果某个过滤器失败、抛出异常或导致输出变大，RTK 会静默保留原始文本。错误绝不会破坏你的请求。
- **通用兼容：** 跨所有格式工作（OpenAI、Claude、Gemini、Cursor、Kiro、OpenAI Responses），因为它在**任何格式转换之前**运行。
- **默认开启：** 可在控制面板 → Endpoint 设置中随时切换。

```
未启用 RTK：向 LLM 发送 47K Token
启用 RTK：   向 LLM 发送 28K Token（节省 40% · 上下文相同 · 答案一致）
```

### 🎯 智能三级回退机制

创建带有自动回退的组合：

```
组合: "my-coding-stack"
  1. cc/claude-opus-4-6        (你的订阅)
  2. glm/glm-4.7               (低价备用, $0.6/1M)
  3. if/kimi-k2-thinking       (免费回退)

→ 配额耗尽或出错时自动切换
```

### 📊 实时额度跟踪

- 各服务商的 Token 消耗情况
- 重置倒计时（5小时、每日、每周）
- 付费层成本估算
- 月度支出报告

### 🔄 格式转换

无缝转换不同格式：
- **OpenAI** ↔ **Claude** ↔ **Gemini** ↔ **Cursor** ↔ **Kiro** ↔ **Vertex** ↔ **Antigravity** ↔ **Ollama** ↔ **OpenAI Responses**
- 你的 CLI 工具发送 OpenAI 格式 → 9Router 转换 → 服务商接收原生格式
- 兼容任何支持自定义 OpenAI 端点的工具

### 👥 多账号支持

- 为每个服务商添加多个账号
- 自动轮询或基于优先级的路由
- 当某个账号达到额限时，回退至下一个账号

### 🔄 Token 自动刷新

- OAuth Token 在过期前自动刷新
- 无需手动重新认证
- 所有服务商体验无缝衔接

### 🎨 自定义组合（Combos）

- 创建无限模型组合
- 混合订阅、低价和免费层
- 为组合命名以便快速访问
- 通过云端同步跨设备共享组合

### 📝 请求日志记录

- 启用调试模式获取完整请求/响应日志
- 跟踪 API 调用、头部信息和负载数据
- 排查集成问题
- 导出日志进行分析

### 💾 云端同步

- 跨设备同步服务商、组合和设置
- 后台自动同步
- 安全加密存储
- 随时随地访问你的配置

#### 云运行时说明

- 生产环境优先使用服务端云变量：
  - `BASE_URL`（内部回调 URL，用于同步调度器）
  - `CLOUD_URL`（云端同步端点基础地址）
- `NEXT_PUBLIC_BASE_URL` 和 `NEXT_PUBLIC_CLOUD_URL` 仍为兼容 UI 而保留，但服务端运行时现在优先使用 `BASE_URL`/`CLOUD_URL`。
- 云同步请求现已采用超时 + 快速失败机制，避免在云 DNS/网络不可用时导致界面卡死。

### 📊 使用分析

- 跟踪各服务商和模型的 Token 使用情况
- 成本估算与支出趋势
- 月度报告与洞察
- 优化你的 AI 支出

> **💡 重要提示 - 理解控制面板中的“成本”：**
> 
> “使用分析”中显示的“成本”**仅用于跟踪和对比**。 
> 9Router 本身**从不向你收取任何费用**。你只需直接支付给服务商（如果使用付费服务）。
> 
> **示例：** 如果你的面板显示“总成本 $290”，而你正在使用 iFlow 模型，这代表 
> 如果你直接使用付费 API 本应支付的费用。你的实际支出 = **$0**（iFlow 为免费无限）。
> 
> 请将其视为一个“节省追踪器”，展示你通过使用免费模型或路由至 9Router 所节省的金额！

### 🌐 任意部署

- 💻 **本地主机** - 默认选项，支持离线运行
- ☁️ **VPS/云端** - 跨设备共享使用
- 🐳 **Docker** - 一键命令部署
- 🚀 **Cloudflare Workers** - 全球边缘网络

</details>

---

## 💰 价格一览

| 层级 | 服务商 | 费用 | 额度重置 | 适用场景 |
|------|----------|------|-------------|----------|
| **🚀 令牌节省器** | **RTK (内置)** | **免费** | 始终开启 | **每次请求节省 20-40% Token** |
| **💳 订阅版** | Claude Code (Pro/Max) | $20-$200/月 | 5小时 + 每周 | 已订阅用户 |
| | Codex (Plus/Pro) | $20-$200/月 | 5小时 + 每周 | OpenAI 用户 |
| | GitHub Copilot | $10-$19/月 | 每月重置 | GitHub 用户 |
| | Cursor IDE | $20/月 | 每月重置 | Cursor 用户 |
| **💰 低价版** | GLM-5.1 / GLM-4.7 | $0.6/1M | 每日上午 10 点 | 预算备用方案 |
| | MiniMax M2.7 | $0.2/1M | 5小时滚动重置 | 最经济选项 |
| | Kimi K2.5 | $9/月固定 | 每月 10M Token | 成本可预测 |
| **🆓 免费版** | Kiro AI | $0 | 无限 | Claude 4.5 + GLM-5 + MiniMax 免费 |
| | OpenCode Free | $0 | 无限 | 免认证，自动获取模型 |
| | Vertex AI | $300 额度 | 新 GCP 账号赠送 | Gemini 3 Pro + DeepSeek + GLM-5 |

**💡 进阶技巧：** RTK + Kiro AI + OpenCode Free 组合 = **$0 成本 + 20-40% Token 节省**！

---

### 📊 理解 9Router 的成本与计费

**9Router 计费现实：**

✅ **9Router 软件本身永久免费**（开源，从不收费）  
✅ **面板“显示的费用” = 仅用于展示/跟踪**（非实际账单）  
✅ **你直接支付给服务商**（订阅费或 API 费用）  
✅ **免费服务商保持免费**（iFlow、Kiro、Qwen = $0 无限）  
❌ **9Router 从不发送发票或扣款**

**费用显示工作原理：**

面板展示的是**估算成本**，假设你直接使用付费 API。这**不是计费** - 它是一个对比工具，用于直观展示你的节省金额。

**示例场景：**
```
面板显示：
• 总请求数: 1,662
• 总 Token: 47M
• 显示费用: $290

实际情况：
• 服务商: iFlow (免费无限)
• 实际支付: $0.00
• $290 的含义: 你通过使用免费模型节省的金额！
```

**付费规则：**
- **订阅服务商**（Claude Code、Codex）：直接通过其官网支付
- **低价服务商**（GLM、MiniMax）：直接支付给它们，9Router 仅负责路由请求
- **免费服务商**（iFlow、Kiro、Qwen）：真正永久免费，无隐藏收费
- **9Router**：永远不收取任何费用

---

## 🎯 使用场景

### 场景 1：“我有 Claude Pro 订阅”

**问题：** 额度未用完即过期，重度编码时遇到速率限制

**解决方案：**
```
组合: "maximize-claude"
  1. cc/claude-opus-4-7        (充分利用订阅)
  2. glm/glm-5.1               (配额耗尽时的低价备用)
  3. kr/claude-sonnet-4.5      (免费紧急回退)

月度成本: $20 (订阅) + ~$5 (备用) = 总计 $25
对比: $20 + 频繁触发限制 = 体验极差
```

### 场景 2：“我想要零成本”

**问题：** 无法承担订阅费用，但需要可靠的 AI 编程辅助

**解决方案：**
```
组合: "free-forever"
  1. kr/claude-sonnet-4.5      (Claude 4.5 免费无限)
  2. kr/glm-5                  (通过 Kiro 使用 GLM-5 免费版)
  3. oc/<auto>                 (OpenCode Free，免认证)

月度成本: $0
质量：生产级模型 + RTK 节省 20-40% Token
```

### 场景 3：“我需要 7x24 小时编码，不能中断”

**问题：** 赶截止日期，无法承受停机时间

**解决方案：**
```
组合: "always-on"
  1. cc/claude-opus-4-7        (最佳质量)
  2. cx/gpt-5.5                (第二订阅)
  3. glm/glm-5.1               (低价，每日重置)
  4. minimax/MiniMax-M2.7      (最便宜，5小时重置)
  5. kr/claude-sonnet-4.5      (免费无限)

结果：5层回退机制 = 零停机时间
月度成本: $20-$200 (订阅) + $10-$20 (备用)
```

### 场景 4：“我想在 OpenClaw 中使用免费 AI”

**问题：** 需要在聊天应用中获取 AI 助手（WhatsApp、Telegram、Slack...），且完全免费

**解决方案：**
```
组合: "openclaw-free"
  1. kr/claude-sonnet-4.5      (Claude 4.5 免费版)
  2. kr/glm-5                  (GLM-5 免费版)
  3. kr/MiniMax-M2.5           (MiniMax 免费版)

月度成本: $0
接入方式：WhatsApp、Telegram、Slack、Discord、iMessage、Signal...
```

---

## ❓ 常见问题解答

<details>
<summary><b>📊 为什么我的面板显示高额费用？</b></summary>

面板会跟踪你的 Token 使用情况，并展示**估算成本**，假设你直接使用付费 API。这**不是实际账单** - 它只是一个参考指标，用于说明你通过使用免费模型或现有订阅通过 9Router 所节省的金额。

**示例：**
- **面板显示：** “总费用 $290”
- **实际情况：** 你正在使用 iFlow（免费无限）
- **你的实际支出：** **$0.00**
- **$290 的含义：** 你通过使用免费模型替代付费 API所**节省的金额**！

费用显示是一个“节省追踪器”，帮助你理解使用模式并发现优化机会。

</details>

<details>
<summary><b>💳 我会被 9Router 扣款吗？</b></summary>

**不会。** 9Router 是免费开源软件，运行在你自己的计算机上。它从不向你收取任何费用。

**你只需支付：**
- ✅ **订阅服务商**（Claude Code $20/月、Codex $20-$200/月）→ 直接在其官网支付
- ✅ **低价服务商**（GLM、MiniMax）→ 直接支付给它们，9Router 仅路由你的请求
- ❌ **9Router 本身** → **永远不收取任何费用**

9Router 是一个本地代理/路由器。它没有你的信用卡信息，无法发送发票，也没有计费系统。它是完全免费的软件。

</details>

<details>
<summary><b>🆓 免费服务商真的是无限使用吗？</b></summary>

**是的！** 当前的免费服务商（Kiro、OpenCode Free、Vertex）确实是真正免费的，**无任何隐藏收费**。

这些是由相应公司提供的免费服务：
- **Kiro AI**：通过 AWS Builder ID / Google / GitHub OAuth 提供无限免费的 Claude 4.5 + GLM-5 + MiniMax
- **OpenCode Free**：免认证透传代理，模型自动从 `opencode.ai/zen/v1/models` 获取
- **Vertex AI**：新 Google Cloud 账号赠送 $300 免费额度（90天有效）

9Router 只是将你的请求路由至它们 - 没有“陷阱”或未来计费。它们是真正的免费服务，而 9Router 通过回退支持让它们更易用。

**已下线的免费层（不再推荐）：**
- ❌ **iFlow**：曾为免费无限，现已改为付费（2026年）
- ❌ **Qwen Code**：阿里已于 2026-04-15 下线其免费 OAuth 层
- ❌ **Gemini CLI**：仍可运行，但与非 CLI 工具（Claude、Codex、Cursor...）混用可能导致封号 — 仅建议单独使用 Gemini CLI

</details>

<details>
<summary><b>💰 如何最小化我的实际 AI 成本？</b></summary>

**免费优先策略：**

1. **从 100% 免费组合开始：**
   ```
   1. gc/gemini-3-flash (Google 每月赠送 180K)
   2. if/kimi-k2-thinking (iFlow 无限免费)
   3. qw/qwen3-coder-plus (Qwen 无限免费)
   ```
   **成本：$0/月**

2. **仅在需要时添加低价备用：**
   ```
   4. glm/glm-4.7 ($0.6/1M Token)
   ```
   **额外成本：仅为你实际使用的部分付费**

3. **最后使用订阅服务商：**
   - 仅在你已有订阅的情况下使用
   - 9Router 通过额度跟踪帮你最大化其价值

**结果：** 大多数用户仅使用免费层即可实现 $0/月运行！

</details>

<details>
<summary><b>📈 如果我的用量突然激增怎么办？</b></summary>

9Router 的智能回退机制可防止意外扣款：

**场景：** 你正在进行编码冲刺，快速消耗完配额

**未使用 9Router：**
- ❌ 触发速率限制 → 工作停止 → 体验极差
- ❌ 或：不小心产生巨额 API 账单

**使用 9Router：**
- ✅ 订阅版达到限额 → 自动回退至低价层
- ✅ 低价层费用过高 → 自动回退至免费层
- ✅ 持续编码不中断 → 成本可预测

**完全由你掌控：** 在控制面板中为每个服务商设置支出上限，9Router 会严格遵守。

</details>

---

## 📖 设置指南

<details>
<summary><b>🔐 订阅服务商（最大化价值）</b></summary>

### Claude Code (Pro/Max)

```bash
控制面板 → Providers → 连接 Claude Code
→ OAuth 登录 → Token 自动刷新
→ 5小时 + 每周额度跟踪

模型：
  cc/claude-opus-4-7
  cc/claude-opus-4-6
  cc/claude-sonnet-4-6
  cc/claude-haiku-4-5-20251001
```

**💡 进阶技巧：** Opus 用于复杂任务，Sonnet 用于快速响应。9Router 会按模型跟踪额度！

### OpenAI Codex (Plus/Pro)

```bash
控制面板 → Providers → 连接 Codex
→ OAuth 登录（端口 1455）
→ 5小时 + 每周重置

模型：
  cx/gpt-5.5
  cx/gpt-5.4
  cx/gpt-5.3-codex
  cx/gpt-5.2-codex
```

### GitHub Copilot

```bash
控制面板 → Providers → 连接 GitHub
→ GitHub OAuth 授权
→ 每月重置（每月1日）

模型：
  gh/gpt-5.4
  gh/claude-opus-4.7
  gh/claude-sonnet-4.6
  gh/gemini-3.1-pro-preview
  gh/grok-code-fast-1
```

### Cursor IDE

```bash
控制面板 → Providers → 连接 Cursor
→ OAuth 登录
→ 月度订阅

模型：
  cu/claude-4.6-opus-max
  cu/claude-4.5-sonnet-thinking
  cu/gpt-5.3-codex
```

</details>

<details>
<summary><b>💰 低价服务商（备用）</b></summary>

### GLM-5.1 / GLM-4.7 (每日重置, $0.6/1M)

1. 注册：[智谱 AI](https://open.bigmodel.cn/)
2. 从 Coding Plan 获取 API Key
3. 控制面板 → 添加 API Key：
   - 服务商: `glm`
   - API Key: `your-key`

**使用：** `glm/glm-5.1`, `glm/glm-5`, `glm/glm-4.7`

**💡 进阶技巧：** Coding Plan 提供 3倍额度，成本仅为 1/7！每日上午 10:00 重置。

### MiniMax M2.7 (5小时重置, $0.20/1M)

1. 注册：[MiniMax](https://www.minimax.io/)
2. 获取 API Key
3. 控制面板 → 添加 API Key

**使用：** `minimax/MiniMax-M2.7`, `minimax/MiniMax-M2.5`

**💡 进阶技巧：** 长上下文（1M Token）最经济的选择！

### Kimi K2.5 ($9/月固定)

1. 订阅：[Moonshot AI](https://platform.moonshot.ai/)
2. 获取 API Key
3. 控制面板 → 添加 API Key

**使用：** `kimi/kimi-k2.5`, `kimi/kimi-k2.5-thinking`

**💡 进阶技巧：** $9/月固定费用，10M Token = 实际成本仅 $0.90/1M！

</details>

<details>
<summary><b>🆓 免费服务商（推荐）</b></summary>

### Kiro AI (Claude 4.5 + GLM-5 + MiniMax 免费)

```bash
控制面板 → 连接 Kiro
→ AWS Builder ID, AWS IAM Identity Center, Google 或 GitHub
→ 无限使用

模型：
  kr/claude-sonnet-4.5
  kr/claude-haiku-4.5
  kr/glm-5
  kr/MiniMax-M2.5
  kr/qwen3-coder-next
  kr/deepseek-3.2
```

**💡 进阶技巧：** Claude 最佳免费方案。无需 API Key，无需付款，完全无限。

### OpenCode Free (免认证, 自动获取模型)

```bash
控制面板 → 连接 OpenCode Free
→ 无需登录（透传代理）
→ 模型自动从 opencode.ai/zen/v1/models 获取
```

**💡 进阶技巧：** 配置最快的方案。只需连接即可开始编码。

### Vertex AI (新 GCP 账号赠 $300 额度)

```bash
控制面板 → 连接 Vertex AI
→ 上传 Google Cloud Service Account JSON
→ 在你的 GCP 项目中启用 Vertex AI API

模型：
  vertex/gemini-3.1-pro-preview
  vertex/gemini-3-flash-preview
  vertex/gemini-2.5-flash

Vertex Partner (Anthropic / DeepSeek / GLM / Qwen via Vertex):
  vertex-partner/glm-5-maas
  vertex-partner/deepseek-v3.2-maas
  vertex-partner/qwen3-next-80b-a3b-thinking-maas
```

**💡 进阶技巧：** 新 Google Cloud 账号赠送 $300 额度，有效期 90 天。足够日常编码使用。

</details>

<details>
<summary><b>🎨 创建组合（Combos）</b></summary>

### 示例 1：最大化订阅 → 低价备用

```
控制面板 → Combos → 新建

名称: premium-coding
模型：
  1. cc/claude-opus-4-7 (订阅主用)
  2. glm/glm-5.1 (低价备用, $0.6/1M)
  3. minimax/MiniMax-M2.7 (最便宜回退, $0.20/1M)

CLI 中使用: premium-coding

月度成本示例（100M Token）：
  80M 通过 Claude (订阅): 额外费用 $0
  15M 通过 GLM: $9
  5M 通过 MiniMax: $1
  总计: $10 + 你的订阅费
```

### 示例 2：纯免费（零成本）

```
名称: free-combo
模型：
  1. kr/claude-sonnet-4.5 (Claude 4.5 免费无限)
  2. kr/glm-5 (通过 Kiro 使用 GLM-5 免费版)
  3. vertex/gemini-3.1-pro-preview ($300 免费额度)

成本：永久 $0 (+ RTK 节省 20-40% Token)!
```

</details>

<details>
<summary><b>🔧 CLI 集成</b></summary>

### Cursor IDE

```
设置 → Models → Advanced:
  OpenAI API Base URL: http://localhost:20128/v1
  OpenAI API Key: [来自 9router 控制面板]
  Model: cc/claude-opus-4-7
```

或使用组合：`premium-coding`

### Claude Code

编辑 `~/.claude/config.json`：

```json
{
  "anthropic_api_base": "http://localhost:20128/v1",
  "anthropic_api_key": "your-9router-api-key"
}
```

### Codex CLI

```bash
export OPENAI_BASE_URL="http://localhost:20128"
export OPENAI_API_KEY="your-9router-api-key"

codex "your prompt"
```

### OpenClaw

**选项 1 — 控制面板（推荐）：**

```
控制面板 → CLI Tools → OpenClaw → 选择模型 → Apply
```

**选项 2 — 手动编辑：** `~/.openclaw/openclaw.json`：

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "9router/kr/claude-sonnet-4.5"
      }
    }
  },
  "models": {
    "providers": {
      "9router": {
        "baseUrl": "http://127.0.0.1:20128/v1",
        "apiKey": "sk_9router",
        "api": "openai-completions",
        "models": [
          {
            "id": "kr/claude-sonnet-4.5",
            "name": "Claude Sonnet 4.5 (Kiro Free)"
          }
        ]
      }
    }
  }
}
```

> **注意：** OpenClaw 仅支持本地运行的 9Router。请使用 `127.0.0.1` 替代 `localhost` 以避免 IPv6 解析问题。

### Cline / Continue / RooCode

```
Provider: OpenAI Compatible
Base URL: http://localhost:20128/v1
API Key: [来自控制面板]
Model: cc/claude-opus-4-7
```

</details>

<details>
<summary><b>🚀 部署指南</b></summary>

### VPS 部署

```bash
# 克隆并安装
git clone https://github.com/decolua/9router.git
cd 9router
npm install
npm run build

# 配置环境变量
export JWT_SECRET="your-secure-secret-change-this"
export INITIAL_PASSWORD="your-password"
export DATA_DIR="/var/lib/9router"
export PORT="20128"
export HOSTNAME="0.0.0.0"
export NODE_ENV="production"
export NEXT_PUBLIC_BASE_URL="http://localhost:20128"
export NEXT_PUBLIC_CLOUD_URL="https://9router.com"
export API_KEY_SECRET="endpoint-proxy-api-key-secret"
export MACHINE_ID_SALT="endpoint-proxy-salt"

# 启动服务
npm run start

# 或使用 PM2 守护进程管理
npm install -g pm2
pm2 start npm --name 9router -- start
pm2 save
pm2 startup
```

### Docker

已发布镜像（多平台 `linux/amd64` + `linux/arm64`）：
- Docker Hub: [`decolua/9router`](https://hub.docker.com/r/decolua/9router)
- GHCR: [`ghcr.io/decolua/9router`](https://github.com/decolua/9router/pkgs/container/9router)

**快速启动（使用发布镜像）：**

```bash
docker run -d \
  --name 9router \
  -p 20128:20128 \
  -v "$HOME/.9router:/app/data" \
  -e DATA_DIR=/app/data \
  decolua/9router:latest
```

→ 访问 http://localhost:20128

**从源码构建（开发环境）：**

```bash
git clone https://github.com/decolua/9router.git
cd 9router/app
docker build -t 9router .
docker run -d --name 9router -p 20128:20128 \
  -v "$HOME/.9router:/app/data" -e DATA_DIR=/app/data 9router
```

**容器默认值：**
- `PORT=20128`
- `HOSTNAME=0.0.0.0`

**常用命令：**

```bash
docker logs -f 9router
docker restart 9router
docker stop 9router && docker rm 9router
docker pull decolua/9router:latest   # 更新至最新版
```

**数据持久化：** 宿主机 `$HOME/.9router/db/data.sqlite` ↔ 容器内 `/app/data/db/data.sqlite`。

### 环境变量说明

| 变量 | 默认值 | 描述 |
|----------|---------|-------------|
| `JWT_SECRET` | 自动生成 (`~/.9router/jwt-secret`) | JWT 签名密钥，用于控制面板认证 Cookie（跨实例共享时请覆盖） |
| `INITIAL_PASSWORD` | `123456` | 无已保存哈希时的首次登录密码 |
| `DATA_DIR` | `~/.9router` | 主应用数据存储位置 (SQLite 位于 `$DATA_DIR/db/data.sqlite`) |
| `PORT` | 框架默认值 | 服务端口（示例中为 `20128`） |
| `HOSTNAME` | 框架默认值 | 绑定主机地址（Docker 默认为 `0.0.0.0`） |
| `NODE_ENV` | 运行时默认值 | 部署时设置为 `production` |
| `BASE_URL` | `http://localhost:20128` | 服务端内部基础 URL，用于云端同步任务 |
| `CLOUD_URL` | `https://9router.com` | 服务端云端同步端点基础 URL |
| `NEXT_PUBLIC_BASE_URL` | `http://localhost:3000` | 向后兼容/公开基础 URL（服务端运行时优先使用 `BASE_URL`） |
| `NEXT_PUBLIC_CLOUD_URL` | `https://9router.com` | 向后兼容/公开云 URL（服务端运行时优先使用 `CLOUD_URL`） |
| `API_KEY_SECRET` | `endpoint-proxy-api-key-secret` | 生成 API Key 的 HMAC 密钥 |
| `MACHINE_ID_SALT` | `endpoint-proxy-salt` | 用于稳定机器 ID 哈希的盐值 |
| `ENABLE_REQUEST_LOGS` | `false` | 启用请求/响应日志，存储于 `logs/` 目录下 |
| `AUTH_COOKIE_SECURE` | `false` | 强制设置 `Secure` 认证 Cookie（HTTPS 反向代理后设为 `true`） |
| `REQUIRE_API_KEY` | `false` | 对 `/v1/*` 路由强制执行 Bearer API Key（面向公网部署推荐开启） |
| `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, `NO_PROXY` | 空 | 上游服务商调用的可选出站代理配置 |

注意事项：
- 小写代理变量同样受支持：`http_proxy`, `https_proxy`, `all_proxy`, `no_proxy`。
- `.env` 不会打包进 Docker 镜像（`.dockerignore`）；请使用 `--env-file` 或 `-e` 注入运行时配置。
- Windows 环境下可使用 `APPDATA` 解析本地存储路径。
- `INSTANCE_NAME` 出现在旧版文档/环境变量模板中，但当前运行时未使用。

### 运行时文件与存储

- 主应用状态：`${DATA_DIR}/db/data.sqlite`（SQLite — 服务商、组合、别名、密钥、设置、使用历史）
- 自动备份：`${DATA_DIR}/db/backups/`
- 可选请求/转换器日志：当 `ENABLE_REQUEST_LOGS=true` 时生成于 `<repo>/logs/...`
- `${DATA_DIR}` 和 `~/.9router` 在 Docker 容器中解析为同一位置 — 构建时会创建符号链接 `/root/.9router -> /app/data`。

</details>

---

## 📊 可用模型列表

<details>
<summary><b>查看所有可用模型</b></summary>

**Claude Code (`cc/`)** - Pro/Max:
- `cc/claude-opus-4-7`
- `cc/claude-opus-4-6`
- `cc/claude-sonnet-4-6`
- `cc/claude-sonnet-4.5-20250929`
- `cc/claude-haiku-4-5-20251001`

**Codex (`cx/`)** - Plus/Pro:
- `cx/gpt-5.5`
- `cx/gpt-5.4`
- `cx/gpt-5.3-codex`
- `cx/gpt-5.2-codex`
- `cx/gpt-5.1-codex-max`

**GitHub Copilot (`gh/`)**:
- `gh/gpt-5.4`
- `gh/claude-opus-4.7`
- `gh/claude-sonnet-4.6`
- `gh/gemini-3.1-pro-preview`
- `gh/grok-code-fast-1`

**Cursor (`cu/`)** - 订阅版:
- `cu/claude-4.6-opus-max`
- `cu/claude-4.5-sonnet-thinking`
- `cu/gpt-5.3-codex`
- `cu/kimi-k2.5`

**GLM (`glm/`)** - $0.6/1M:
- `glm/glm-5.1`
- `glm/glm-5`
- `glm/glm-4.7`

**MiniMax (`minimax/`)** - $0.2/1M:
- `minimax/MiniMax-M2.7`
- `minimax/MiniMax-M2.5`

**Kimi (`kimi/`)** - $9/月固定:
- `kimi/kimi-k2.5`
- `kimi/kimi-k2.5-thinking`

**Kiro (`kr/`)** - 免费无限:
- `kr/claude-sonnet-4.5`
- `kr/claude-haiku-4.5`
- `kr/glm-5`
- `kr/MiniMax-M2.5`
- `kr/qwen3-coder-next`
- `kr/deepseek-3.2`

**OpenCode Free (`oc/`)** - 免费免认证:
- 自动从 `opencode.ai/zen/v1/models` 获取

**Vertex AI (`vertex/`)** - $300 免费额度:
- `vertex/gemini-3.1-pro-preview`
- `vertex/gemini-3-flash-preview`
- `vertex/gemini-2.5-flash`
- `vertex-partner/glm-5-maas`
- `vertex-partner/deepseek-v3.2-maas`

</details>

---

## 🐛 故障排除

**"Language model did not provide messages"**
- 服务商配额耗尽 → 检查控制面板额度跟踪器
- 解决方案：使用组合回退或切换至更低价层

**速率限制（Rate limiting）**
- 订阅配额用尽 → 回退至 GLM/MiniMax
- 添加组合：`cc/claude-opus-4-7 → glm/glm-5.1 → kr/claude-sonnet-4.5`

**OAuth Token 过期**
- 9Router 会自动刷新
- 若问题持续：控制面板 → Provider → 重新连接

**费用过高**
- 在控制面板 → Endpoint 设置中启用 RTK（默认开启，节省 20-40% Token）
- 检查面板使用统计
- 将主模型切换至 GLM/MiniMax
- 对非关键任务使用免费层（Kiro、OpenCode Free、Vertex）

**控制面板打开错误端口**
- 设置 `PORT=20128` 和 `NEXT_PUBLIC_BASE_URL=http://localhost:20128`

**首次登录失败**
- 检查 `.env` 中的 `INITIAL_PASSWORD`
- 若未设置，默认回退密码为 `123456`

**`logs/` 下无请求日志**
- 设置 `ENABLE_REQUEST_LOGS=true`

---

## 🛠️ 技术栈

- **运行环境**: Node.js 20+
- **框架**: Next.js 16
- **UI**: React 19 + Tailwind CSS 4
- **数据库**: SQLite (better-sqlite3 / node:sqlite / sql.js 回退)
- **流式传输**: Server-Sent Events (SSE)
- **认证**: OAuth 2.0 (PKCE) + JWT + API Keys

---

## 📝 API 参考

### Chat Completions

```bash
POST http://localhost:20128/v1/chat/completions
Authorization: Bearer your-api-key
Content-Type: application/json

{
  "model": "cc/claude-opus-4-6",
  "messages": [
    {"role": "user", "content": "Write a function to..."}
  ],
  "stream": true
}
```

### List Models

```bash
GET http://localhost:20128/v1/models
Authorization: Bearer your-api-key

→ 返回所有模型 + 组合（OpenAI 格式）
```

## 📧 支持渠道

- **官网**: [9router.com](https://9router.com)
- **GitHub**: [github.com/decolua/9router](https://github.com/decolua/9router)
- **Issues**: [github.com/decolua/9router/issues](https://github.com/decolua/9router/issues)

---

## 👥 贡献者

感谢所有帮助完善 9Router 的贡献者！

[![Contributors](https://contrib.rocks/image?repo=decolua/9router&max=150&columns=15&anon=1&v=20260309)](https://github.com/decolua/9router/graphs/contributors)

---

## 📊 Star 趋势图

[![Star Chart](https://starchart.cc/decolua/9router.svg?variant=adaptive)](https://starchart.cc/decolua/9router)



## 🔀 Forks

**[OmniRoute](https://github.com/diegosouzapw/OmniRoute)** — 基于 TypeScript 的 9Router 全功能分支。新增 36+ 服务商、4级自动回退、多模态 API（图像、嵌入、音频、TTS）、熔断器、语义缓存、LLM 评估及优化后的控制面板。包含 368+ 单元测试。可通过 npm 和 Docker 获取。

---

## 🙏 致谢

站在巨人的肩膀上构建：

- **[CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)** — 启发本 JavaScript 端口的原始 Go 实现。
- **[RTK](https://github.com/rtk-ai/rtk)** ![Stars](https://img.shields.io/github/stars/rtk-ai/rtk?style=flat&color=yellow) — Rust 令牌节省器。9Router 将其压缩管道移植至 JS → **每次请求减少 20-40% 输入 Token**。
- **[Caveman](https://github.com/JuliusBrussee/caveman)** ![Stars](https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat&color=yellow) by **[@JuliusBrussee](https://github.com/JuliusBrussee)** — 病毒式传播的 *"为什么用很多 token，少一点也能搞定"*。9Router 适配其提示词逻辑 → **减少 65% 输出 Token**。

衷心感谢这些作者的工作 —— 没有他们的贡献，9Router 的令牌节省功能将不复存在。去 GitHub 给他们 ⭐ Star 吧！

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)。

---

<div align="center">
  <sub>为 24/7 编码的开发者 ❤️ 构建</sub>
</div>