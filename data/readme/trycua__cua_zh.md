<div align="center">
  <a href="https://cua.ai" target="_blank" rel="noopener noreferrer">
    <picture>
      <source media="(prefers-color-scheme: dark)" alt="Cua logo" width="150" srcset="img/logo_white.svg">
      <source media="(prefers-color-scheme: light)" alt="Cua logo" width="150" srcset="img/logo_black.svg">
      <img alt="Cua logo" width="150" src="img/logo_black.svg">
    </picture>
  </a>

  <p align="center">构建、评估与部署能够操控计算机的智能体</p>

  <p align="center">
    <a href="https://cua.ai" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/cua.ai-0ea5e9" alt="cua.ai"></a>
    <a href="https://discord.gg/mVnXXpdE85" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Discord-Join%20Server-10b981?logo=discord&logoColor=white" alt="Discord"></a>
    <a href="https://x.com/trycua" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/twitter/follow/trycua?style=social" alt="Twitter"></a>
    <a href="https://cua.ai/docs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Docs-0ea5e9.svg" alt="Documentation"></a>
    <br>
<a href="https://trendshift.io/repositories/13685" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13685" alt="trycua%2Fcua | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
  </p>

</div>

## 选择适合的路径

<div align="center">
  <table>
    <tr>
      <td colspan="3" align="center">
        <a href="#cua-driver---background-computer-use-on-macos-and-windows-with-linux-pre-release">
          <img src="img/card-cua-driver.png" alt="Cua Driver — The background computer-use agent" width="888">
        </a>
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="#cua---agentic-ui-automation--code-execution">
          <img src="img/card-cua-sandbox.png" alt="Cua &amp; Cua Sandbox" width="280">
        </a>
      </td>
      <td align="center">
        <a href="#cua-bench---benchmarks--rl-environments">
          <img src="img/card-cua-bench.png" alt="Cua Bench" width="280">
        </a>
      </td>
      <td align="center">
        <a href="#lume---macos-virtualization">
          <img src="img/card-cua-lume.png" alt="Lume" width="280">
        </a>
      </td>
    </tr>
  </table>
</div>

---

## Cua Driver —— 在 macOS 和 Windows 上后台运行计算机操作（Linux 预发布版）

在**后台**驱动原生桌面应用 —— 智能体可点击、输入并验证操作，且不会抢占光标或焦点。通过 CLI 和 MCP Server，你可以在 macOS 和 Windows 上使用 Claude Code、Cursor、Codex、OpenClaw 及自定义客户端进行调用。目前 Linux 支持以预发布后端形式提供，平台测试仍在进行中。

**macOS / Linux 预发布版**

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.ps1 | iex
```

完整工具参考、架构说明及可选的智能体技能包（agent skill pack）位于：[`libs/cua-driver/README.md`](libs/cua-driver/README.md)。

---

## Cua —— 适用于任何操作系统的智能体就绪沙箱（Agent-Ready Sandboxes）

构建能够查看屏幕、点击按钮并自主完成任务的智能体。一套 API 即可适配任何虚拟机或容器镜像 —— 无论云端还是本地。

```sh
pip install cua
```

<!-- <img src="img/cua-architecture.png" alt="Cua Architecture" width="100%"> -->

```python
# Requires Python 3.11 or later
from cua import Sandbox, Image

# Same API regardless of OS or runtime
async with Sandbox.ephemeral(Image.linux()) as sb:   # or .macos() .windows() .android()
    result = await sb.shell.run("echo hello")
    screenshot = await sb.screenshot()
    await sb.mouse.click(100, 200)
    await sb.keyboard.type("Hello from Cua!")
    await sb.mobile.gesture((100, 500), (100, 200))  # multi-touch gestures
```

|                    | Linux 容器 | Linux 虚拟机 | macOS | Windows | Android | BYOI (.qcow2, .iso) |
| ------------------ | ---------- | ------------ | ----- | ------- | ------- | ------------------- |
| **云端 (cua.ai)**  | ✅          | ✅            | ✅     | ✅       | ✅       | 🔜 soon             |
| **本地 (QEMU)**    | ✅          | ✅            | ✅     | ✅       | ✅       | ✅                  |

**[快速开始](https://cua.ai/docs/cua/guide/get-started/set-up-sandbox)** | **[示例](https://cua.ai/docs/cua/examples)** | **[API 参考](https://cua.ai/docs/cua/reference/agent-sdk)**

---

## CuaBot —— 为任意智能体提供协同计算机操作环境

<div align="center">
  <img src="img/cuabot-screenshot.png" alt="cuabot screenshot" width="720">
</div>

`cuabot` 为任何编程智能体提供一个无缝的计算机操作沙箱。各个窗口将以原生形式出现在你的桌面上，支持 H.265、共享剪贴板和音频传输。

```bash
npx cuabot                 # Setup onboarding
```

```bash
# Run any agent in a sandbox
cuabot claude              # Claude Code
cuabot openclaw            # OpenClaw in the sandbox

# Run any GUI workflow in a sandbox
cuabot chromium
cuabot --screenshot
cuabot --type "hello"
cuabot --click <x> <y> [button]
```

开箱即用地内置支持 `agent-browser` 和 `agent-device`（iOS、Android）。

<div align="center">

**[快速开始](https://cua.ai/docs/cuabot/guide/getting-started/introduction)** | **[安装指南](https://cua.ai/docs/cuabot/guide/getting-started/installation)** | 首次亮相于 [ClawCon](https://www.claw-con.com/)

<img height="64" alt="cuaXclawdbot_nbg" src="https://github.com/user-attachments/assets/8b92237d-6e9b-4b3a-ae9a-b3560622ec1d" />

</div>

---

## Cua-Bench —— 基准测试与强化学习（RL）环境

在 OSWorld、ScreenSpot、Windows Arena 及自定义任务中评估计算机操作智能体。导出轨迹数据用于模型训练。

<!-- <img src="img/cua-bench-architecture.png" alt="Cua-Bench Architecture" width="100%"> -->

```bash
# Install and create base image
cd cua-bench
uv tool install -e . && cb image create linux-docker

# Run benchmark with agent
cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4
```

**[快速开始](https://cua.ai/docs/cuabench/guide/getting-started/first-steps)** | **[合作伙伴计划](https://cuabench.ai/)** | **[注册表](https://cuabench.ai/registry)** | **[CLI 参考](https://cua.ai/docs/cuabench/reference/cli-reference)**

---

## Lume —— macOS 虚拟化方案

基于 Apple Silicon 芯片，利用 Apple 的 Virtualization.Framework 创建并管理 macOS/Linux 虚拟机，性能接近原生。

<!-- <img src="img/lume-architecture.png" alt="Lume Architecture" width="100%"> -->

```bash
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

**[快速开始](https://cua.ai/docs/lume)** | **[常见问题](https://cua.ai/docs/lume/guide/getting-started/faq)** | **[CLI 参考](https://cua.ai/docs/lume/reference/cli-reference)**

---

## 软件包

| 软件包                                                                        | 描述                                                |
| --------------------------------------------------------------------------- | ---------------------------------------------------- |
| [cuabot](https://docs.trycua.com/cuabot/guide/getting-started/introduction) | 多智能体计算机操作沙箱 CLI 工具                      |
| [cua-agent](https://cua.ai/docs/cua/reference/agent-sdk)                    | 面向计算机操作任务的 AI 智能体框架                   |
| [cua-sandbox](https://cua.ai/docs/cua/reference/sandbox-sdk)                | 用于创建和控制沙箱的 SDK                             |
| [cua-computer-server](https://cua.ai/docs/cua/reference/sandbox-sdk)        | 在沙箱中处理 UI 交互与代码执行的驱动服务             |
| [cua-bench](https://cua.ai/docs/cuabench)                                   | 面向计算机操作的基准测试与强化学习环境               |
| [lume](https://cua.ai/docs/lume)                                            | 适用于 Apple Silicon 的 macOS/Linux 虚拟机管理工具   |
| [lumier](https://cua.ai/docs/lume/guide/advanced/lumier)                    | 兼容 Docker 的 Lume 虚拟机接口                       |

## 资源

- [文档](https://cua.ai/docs) —— 指南、示例与 API 参考
- [博客](https://www.cua.ai/blog) —— 教程、更新与研究动态
- [Discord](https://discord.com/invite/mVnXXpdE85) —— 社区支持与讨论
- [GitHub Issues](https://github.com/trycua/cua/issues) —— Bug 反馈与功能建议

## 贡献指南

我们欢迎任何形式的贡献！详情请参阅我们的[贡献指南](CONTRIBUTING.md)。

## 许可证

MIT 许可证 —— 详见[LICENSE](LICENSE.md)。

第三方组件拥有各自的许可证：

- [Kasm](libs/kasm/LICENSE) (MIT)
- [OmniParser](https://github.com/microsoft/OmniParser/blob/master/LICENSE) (CC-BY-4.0)
- Optional `cua-agent[omni]` includes ultralytics (AGPL-3.0)

## 商标声明

Apple、macOS、Ubuntu、Canonical 和 Microsoft 均为各自所有者的商标。本项目与这些公司无关，也未获得其认可或背书。

---

<div align="center">

[![Stargazers over time](https://starchart.cc/trycua/cua.svg?variant=adaptive)](https://starchart.cc/trycua/cua)

感谢所有 [GitHub Sponsor](https://github.com/sponsors/trycua) 的支持！

<img width="300" alt="coderabbit-cli" src="https://github.com/user-attachments/assets/23a98e38-7897-4043-8ef7-eb990520dccc" />

</div>