<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/.github/logotype-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="/.github/logotype-light.png">
    <img src="/.github/logotype-dark.png" width="400" alt="Happy">
  </picture>
</div>

<h1 align="center">
适用于 Claude Code 与 Codex 的移动端及网页端客户端
</h1>

<h4 align="center">
随时随地使用 Claude Code 或 Codex，全程端到端加密。
</h4>

<div align="center">
  
[📱 **iOS 应用**](https://apps.apple.com/us/app/happy-claude-code-client/id6748571505) • [🤖 **Android 应用**](https://play.google.com/store/apps/details?id=com.ex3ndr.happy) • [🌐 **网页版**](https://app.happy.engineering) • [🎥 **观看演示**](https://youtu.be/GCS0OG9QMSE) • [📚 **文档**](https://happy.engineering/docs/) • [💬 **Discord**](https://discord.gg/fX9WBAhyfD)

</div>

<img width="5178" height="2364" alt="github" src="/.github/header.png" />


<h3 align="center">
步骤 1：下载应用
</h3>

<div align="center">
<a href="https://apps.apple.com/us/app/happy-claude-code-client/id6748571505"><img width="135" height="39" alt="appstore" src="https://github.com/user-attachments/assets/45e31a11-cf6b-40a2-a083-6dc8d1f01291" /></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://play.google.com/store/apps/details?id=com.ex3ndr.happy"><img width="135" height="39" alt="googleplay" src="https://github.com/user-attachments/assets/acbba639-858f-4c74-85c7-92a4096efbf5" /></a>
</div>

<h3 align="center">
步骤 2：在电脑上安装 CLI
</h3>

```bash
npm install -g happy
```

> 该项目已从 `happy-coder` 包迁移而来。感谢 [@franciscop](https://github.com/franciscop) 捐赠了 `happy` 这个包名！

<h3 align="center">
步骤 3：开始使用 `happy` 替代 `claude` 或 `codex`
</h3>

```bash
# 替代 claude，请使用：
happy claude
# 或者
happy codex
```

## <span id="-how-does-it-work"></span>工作原理

在你的电脑上，运行 `happy`（替代 `claude`）或 `happy codex`（替代 `codex`），即可通过我们的包装器启动 AI。当你想从手机控制你的编程代理时，它会自动以远程模式重启会话。若要切换回电脑端操作，只需按下键盘上的任意键即可。

## <span id="-why-happy-coder"></span>🔥 为什么选择 Happy Coder？

- 📱 **移动端访问 Claude Code 和 Codex** —— 离开办公桌时，随时查看你的 AI 正在构建的内容
- 🔔 **推送通知** —— 当 Claude Code 或 Codex 需要权限确认或遇到错误时，及时收到提醒  
- ⚡ **设备间无缝切换** —— 只需按下一个键，即可在手机和桌面端之间接管控制权
- 🔐 **端到端加密** —— 你的代码永远不会以未加密状态离开你的设备
- 🛠️ **开源** —— 可自行审查代码。无遥测数据（telemetry），无用户追踪

## <span id="-project-components"></span>📦 项目组件

- **[Happy App](https://github.com/slopus/happy/tree/main/packages/happy-app)** - 网页端 UI + 移动端客户端（基于 Expo）
- **[Happy CLI](https://github.com/slopus/happy/tree/main/packages/happy-cli)** - 用于 Claude Code 和 Codex 的命令行界面
- **[Happy Agent](https://github.com/slopus/happy/tree/main/packages/happy-agent)** - 远程代理控制 CLI（创建、发送指令及监控会话）
- **[Happy Server](https://github.com/slopus/happy/tree/main/packages/happy-server)** - 用于加密同步的后端服务器

## <span id="-who-we-are"></span>🏠 关于我们

我们是散落在湾区咖啡馆和极客公寓里的工程师，午休时总忍不住查看你的 AI 编程代理在个人项目上的进展。Happy Coder 的诞生，源于无法在离开键盘时随时瞥一眼你的 AI 编程工具如何打理副业项目的挫败感。我们始终相信：最好的工具源于解决你自己的痛点，并乐于与社区分享。

## <span id="-documentation--contributing"></span>📚 文档与贡献指南

- **[文档网站](https://happy.engineering/docs/)** - 学习如何高效使用 Happy Coder
- **[贡献指南](docs/CONTRIBUTING.md)** - 参与方式、PR（Pull Request）规范及开发环境配置说明
- **[在 GitHub 编辑文档](https://github.com/slopus/slopus.github.io)** - 协助完善我们的文档与指南

## <span id="-license"></span>License

MIT 开源协议 —— 详情请参阅 [LICENSE](LICENSE)。