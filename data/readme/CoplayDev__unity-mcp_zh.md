<img width="676" height="380" alt="MCP for Unity" src="docs/images/logo.png" />

| [English](README.md) | [简体中文](docs/i18n/README-zh.md) |
|----------------------|---------------------------------|

#### 由 [Aura](https://www.tryaura.dev/) 自豪赞助并维护 —— 专为 Unreal & Unity 打造的 AI 助手。
##### 别忘了关注 [Godot AI](https://github.com/hi-godot/godot-ai)，这是 MCP for Unity 团队推出的全新开源 MCP/AI 项目。

[![Docs](https://img.shields.io/badge/Docs-unity--mcp-4f46e5)](https://coplaydev.github.io/unity-mcp/)
[![Discord](https://img.shields.io/badge/discord-join-red.svg?logo=discord&logoColor=white)](https://discord.gg/y4p8KfzrN4)
[![](https://img.shields.io/badge/Website-Visit-purple)](https://www.coplay.dev/?ref=unity-mcp)
[![](https://img.shields.io/badge/Unity-000000?style=flat&logo=unity&logoColor=blue 'Unity')](https://unity.com/releases/editor/archive)
[![python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![](https://badge.mcpx.dev?status=on 'MCP Enabled')](https://modelcontextprotocol.io/introduction)
[![](https://img.shields.io/badge/License-MIT-red.svg 'MIT License')](https://opensource.org/licenses/MIT)

**使用大语言模型（LLM）构建你的 Unity 应用。** MCP for Unity 通过 [模型上下文协议（Model Context Protocol）](https://modelcontextprotocol.io/introduction) 将 AI 助手——包括 Claude、Codex、VS Code、本地 LLM 等——与你的 Unity Editor 连接起来。让你的 LLM 掌握管理资源、控制场景、编辑脚本、运行测试以及自动化工作流的工具。

<img alt="MCP for Unity building a scene" src="docs/images/building_scene.gif">

---

## 阅读文档

### **→ [coplaydev.github.io/unity-mcp](https://coplaydev.github.io/unity-mcp/)**

---

## 安装

在 Unity 中：**窗口 → 包管理器 → + → 从 Git URL 添加**，粘贴：

```text
https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main
```

Beta 频道请使用 `#beta`。Asset Store 和 OpenUPM 的安装路径详见 [安装指南](https://coplaydev.github.io/unity-mcp/getting-started/install)。

然后打开 **窗口 → MCP for Unity → 配置所有已检测到的客户端**。完成！现在可以尝试一个提示词：

> 在当前场景中创建一个红色、蓝色和黄色的立方体。

完整教程：[你的第一个提示词](https://coplaydev.github.io/unity-mcp/getting-started/first-prompt)。

---

<!-- recent-updates:start -->
<details>
<summary><strong>最近更新</strong></summary>

* **[v9.7.0](https://github.com/CoplayDev/unity-mcp/releases/tag/v9.7.0)** (2026-05-22)
* **[v9.6.8](https://github.com/CoplayDev/unity-mcp/releases/tag/v9.6.8)** (2026-04-27)
* **[v9.6.6](https://github.com/CoplayDev/unity-mcp/releases/tag/v9.6.6)** (2026-04-07)
* **[v9.6.5](https://github.com/CoplayDev/unity-mcp/releases/tag/v9.6.5)** (2026-04-03)
* **[v9.6.4](https://github.com/CoplayDev/unity-mcp/releases/tag/v9.6.4)** (2026-03-31)

完整历史记录：[发布说明](https://coplaydev.github.io/unity-mcp/releases)。

</details>
<!-- recent-updates:end -->

---

## 社区交流

- [Discord](https://discord.gg/y4p8KfzrN4) —— 与维护者及其他贡献者聊天交流
- [Issues](https://github.com/CoplayDev/unity-mcp/issues) —— 提交 Bug 报告和功能请求
- [Discussions](https://github.com/CoplayDev/unity-mcp/discussions) —— 探讨设计思路与更广泛的问题
- 安全相关：请参阅 [SECURITY.md](SECURITY.md) 进行私密报告

## 贡献指南

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。请基于 `beta` 分支进行开发，而非 `main`。完整的开发环境配置、测试及发布流程详见 [贡献指南](https://coplaydev.github.io/unity-mcp/contributing/dev-setup) 文档。

## 高级功能

- **多实例 Unity** —— [多实例路由](https://coplaydev.github.io/unity-mcp/guides/multi-instance)
- **工具组（vfx / 动画 / UI / 测试等）** —— [工具组配置](https://coplaydev.github.io/unity-mcp/guides/tool-groups)
- **Roslyn 脚本验证** —— [Roslyn 验证指南](https://coplaydev.github.io/unity-mcp/guides/roslyn)
- **带身份验证的远程托管服务器** —— [远程服务器认证](https://coplaydev.github.io/unity-mcp/guides/remote-server-auth)

## 星标历史

[![Star History Chart](https://api.star-history.com/svg?repos=CoplayDev/unity-mcp&type=Date)](https://www.star-history.com/#CoplayDev/unity-mcp&Date)

## 引用说明

如果 MCP for Unity 对你的研究有所帮助，请引用本项目。

```bibtex
@inproceedings{wu2025mcpunity,
  author    = {Wu, Shutong and Barnett, Justin P.},
  title     = {{MCP-Unity}: {Protocol-Driven} Framework for Interactive {3D} Authoring},
  year      = {2025},
  isbn      = {9798400721366},
  publisher = {Association for Computing Machinery},
  address   = {New York, NY, USA},
  url       = {https://doi.org/10.1145/3757376.3771417},
  doi       = {10.1145/3757376.3771417},
  series    = {SA Technical Communications '25}
}
```

## Aura 的 Unity AI 工具

Aura 提供两款面向 Unity 的 AI 工具：
- **MCP for Unity** 基于 MIT 许可证免费开源。
- **Aura for Unity** 是专为游戏开发者打造的高级 Unity/Unreal AI 助手。

## 免责声明

本项目是一款面向 Unity Editor 的免费开源工具，与 Unity Technologies 无关。

---

**许可证：** MIT —— 详见 [LICENSE](LICENSE)。