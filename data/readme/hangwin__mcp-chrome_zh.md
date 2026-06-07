# Chrome MCP Server 🚀

[![Stars](https://img.shields.io/github/stars/hangwin/mcp-chrome)](https://img.shields.io/github/stars/hangwin/mcp-chrome)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8+-blue.svg)](https://www.typescriptlang.org/)
[![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-green.svg)](https://developer.chrome.com/docs/extensions/)
[![Release](https://img.shields.io/github/v/release/hangwin/mcp-chrome.svg)](https://img.shields.io/github/v/release/hangwin/mcp-chrome.svg)

> 🌟 **将你的 Chrome 浏览器变成智能助手** —— 让 AI 接管你的浏览器，将其转变为强大的 AI 控制自动化工具。

**📖 文档**: [英文](README.md) | [中文](README_zh.md)

> 🚧 **项目仍处于早期阶段，正在密集开发中。** 更多功能、稳定性提升及其他优化将陆续推出。

---

## 🎯 什么是 Chrome MCP Server？

Chrome MCP Server 是一款基于 Chrome 扩展的**模型上下文协议（MCP）服务器**。它将你的 Chrome 浏览器功能暴露给 Claude 等 AI 助手，从而实现复杂的浏览器自动化、内容分析和语义搜索。与传统的浏览器自动化工具（如 Playwright）不同，**Chrome MCP Server** 直接调用你日常使用的 Chrome 浏览器，充分利用现有的用户习惯、配置和登录状态，让各大语言模型或聊天机器人接管你的浏览器，真正成为你的日常得力助手。

## ✨ 新功能 (2025/12/30)

- **为 Claude Code 和 Codex 提供的全新可视化编辑器**，详情请见：[VisualEditor](docs/VisualEditor.md)

## ✨ 核心特性

- 😁 **不绑定特定聊天机器人/模型**：让你偏好的任何 LLM、聊天客户端或 Agent 接管并自动化你的浏览器
- ⭐️ **复用原有浏览器环境**：无缝集成你现有的浏览器环境（保留你的配置、登录状态等）
- 💻 **完全本地化**：纯本地运行的 MCP 服务器，保障用户隐私安全
- 🚄 **流式（Streamable）HTTP**：支持流式 HTTP 连接方式
- 🏎 **跨标签页上下文**：支持跨标签页共享上下文信息
- 🧠 **语义搜索**：内置向量数据库，智能发现浏览器标签页内容
- 🔍 **智能内容分析**：基于 AI 的文本提取与相似度匹配
- 🌐 **20+ 项工具**：支持截图、网络监控、交互操作、书签管理、浏览历史等 20 余种功能
- 🚀 **SIMD 加速 AI**：自定义 WebAssembly SIMD 优化，向量运算速度提升 4-8 倍

## 🆚 与同类项目对比

| 对比维度 | 基于 Playwright 的 MCP Server | 基于 Chrome 扩展的 MCP Server |
| --- | --- | --- |
| **资源占用** | ❌ 需启动独立浏览器进程，安装 Playwright 依赖、下载浏览器二进制文件等 | ✅ 无需启动独立进程，直接复用用户已打开的 Chrome 浏览器 |
| **会话状态复用** | ❌ 需重新登录 | ✅ 自动沿用现有登录状态 |
| **浏览器环境** | ❌ 纯净环境，缺乏用户个性化设置 | ✅ 完整保留用户原有环境 |
| **API 调用权限** | ⚠️ 仅限 Playwright API | ✅ 完全支持 Chrome 原生 API |
| **启动速度** | ❌ 需等待浏览器进程启动 | ✅ 仅需激活扩展即可 |
| **响应延迟** | 50-200ms（跨进程通信） | ✅ 更低 |

## 🚀 快速上手

### 前置条件

- Node.js >= 20.0.0 以及 pnpm/npm
- Chrome / Chromium 浏览器

### 安装步骤

1. **从 GitHub 下载最新版 Chrome 扩展**

下载地址：https://github.com/hangwin/mcp-chrome/releases

2. **全局安装 mcp-chrome-bridge**

npm

```bash
npm install -g mcp-chrome-bridge
```

pnpm

```bash
# Method 1: Enable scripts globally (recommended)
pnpm config set enable-pre-post-scripts true
pnpm install -g mcp-chrome-bridge

# Method 2: Manual registration (if postinstall doesn't run)
pnpm install -g mcp-chrome-bridge
mcp-chrome-bridge register
```

> 💡 **注意**：出于安全考虑，pnpm v7+ 默认禁用 `postinstall` 脚本。通过设置 `enable-pre-post-scripts` 可控制是否运行安装前后脚本。若自动注册失败，请手动执行上述命令进行注册。

3. **加载 Chrome 扩展**
   - 打开 Chrome 浏览器并访问 `chrome://extensions/`
   - 开启“开发者模式”
   - 点击“加载已解压的扩展程序”，选择你下载的扩展文件夹路径
   - 点击工具栏中的扩展图标打开插件，然后点击连接以查看 MCP 配置
     <img width="475" alt="Screenshot 2025-06-09 15 52 06" src="https://github.com/user-attachments/assets/241e57b8-c55f-41a4-9188-0367293dc5bc" />

### 配合 MCP 协议客户端使用

#### 使用流式（Streamable）HTTP 连接（👍🏻 推荐）

请将以下配置添加到你的 MCP 客户端配置文件中使用（以 CherryStudio 为例）：

> 💡 推荐使用流式 HTTP 连接方式

```json
{
  "mcpServers": {
    "chrome-mcp-server": {
      "type": "streamableHttp",
      "url": "http://127.0.0.1:12306/mcp"
    }
  }
}
```

#### 使用 STDIO 连接（备选方案）

如果你的客户端仅支持 STDIO 连接方式，请按以下步骤操作：

1. 首先查看刚安装的 npm/pnpm 包路径

```sh
# npm check method
npm list -g mcp-chrome-bridge
# pnpm check method
pnpm list -g mcp-chrome-bridge
```

假设上述命令输出路径为 `/Users/xxx/Library/pnpm/global/5`，则你的最终完整路径应为：`/Users/xxx/Library/pnpm/global/5/node_modules/mcp-chrome-bridge/dist/mcp/mcp-server-stdio.js`

2. 将下方配置中的路径替换为你刚刚获取的实际路径

```json
{
  "mcpServers": {
    "chrome-mcp-stdio": {
      "command": "npx",
      "args": [
        "node",
        "/Users/xxx/Library/pnpm/global/5/node_modules/mcp-chrome-bridge/dist/mcp/mcp-server-stdio.js"
      ]
    }
  }
}
```

eg：config in augment:

<img width="494" alt="截屏2025-06-22 22 11 25" src="https://github.com/user-attachments/assets/48eefc0c-a257-4d3b-8bbe-d7ff716de2bf" />

## 🛠️ 可用工具

完整工具列表请查看：[完整工具列表](docs/TOOLS.md)

<details>
<summary><strong>📊 浏览器管理（6 项）</strong></summary>

- `get_windows_and_tabs` - 列出所有浏览器窗口和标签页
- `chrome_navigate` - 导航至指定 URL 并控制视口大小
- `chrome_switch_tab` - 切换当前活动标签页
- `chrome_close_tabs` - 关闭特定标签页或窗口
- `chrome_go_back_or_forward` - 浏览器前进/后退控制
- `chrome_inject_script` - 向网页注入内容脚本（Content Script）
- `chrome_send_command_to_inject_script` - 向已注入的内容脚本发送指令
</details>

<details>
<summary><strong>📸 截图与视觉（1 项）</strong></summary>

- `chrome_screenshot` - 高级截图功能，支持元素定位、全页截取及自定义尺寸
</details>

<details>
<summary><strong>🌐 网络监控（4 项）</strong></summary>

- `chrome_network_capture_start/stop` - webRequest API 网络抓包
- `chrome_network_debugger_start/stop` - Debugger API（含响应体捕获）
- `chrome_network_request` - 发送自定义 HTTP 请求
</details>

<details>
<summary><strong>🔍 内容分析（4 项）</strong></summary>

- `search_tabs_content` - AI 驱动的跨标签页语义搜索
- `chrome_get_web_content` - 提取页面 HTML/文本内容
- `chrome_get_interactive_elements` - 查找可点击元素
- `chrome_console` - 捕获并获取浏览器标签页的控制台输出
</details>

<details>
<summary><strong>🎯 交互操作（3 项）</strong></summary>

- `chrome_click_element` - 使用 CSS 选择器点击元素
- `chrome_fill_or_select` - 填写表单与下拉选项
- `chrome_keyboard` - 模拟键盘输入与快捷键组合
</details>

<details>
<summary><strong>📚 数据管理（5 项）</strong></summary>

- `chrome_history` - 按时间范围搜索浏览历史
- `chrome_bookmark_search` - 通过关键词查找书签
- `chrome_bookmark_add` - 添加新书签并支持指定文件夹
- `chrome_bookmark_delete` - 删除书签
</details>

## 🧪 使用示例

### AI 协助总结网页内容并自动操控 Excalidraw 绘图

提示词：[excalidraw-prompt](prompt/excalidraw-prompt.md)  
指令：帮我总结当前页面的内容，然后绘制一张图表辅助理解。  
https://www.youtube.com/watch?v=3fBPdUBWVz0

https://github.com/user-attachments/assets/fd17209b-303d-48db-9e5e-3717141df183

### 分析图片内容后，LLM 自动操控 Excalidraw 复刻图像

提示词：[excalidraw-prompt](prompt/excalidraw-prompt.md) | [content-analize](prompt/content-analize.md)  
指令：先分析这张图片的内容，然后结合分析与原图内容将其复刻出来。  
https://www.youtube.com/watch?v=tEPdHZBzbZk

https://github.com/user-attachments/assets/60d12b1a-9b74-40f4-994c-95e8fa1fc8d3

### AI 自动注入脚本并修改网页样式

提示词：[modify-web-prompt](prompt/modify-web.md)  
指令：帮我修改当前页面的样式，并移除广告。  
https://youtu.be/twI6apRKHsk

https://github.com/user-attachments/assets/69cb561c-2e1e-4665-9411-4a3185f9643e

### AI 帮你自动捕获网络请求

查询：我想了解小红书的搜索 API 是什么，以及它的响应结构是怎样的。

https://youtu.be/1hHKr7XKqnQ

https://github.com/user-attachments/assets/dc7e5cab-b9af-4b9a-97ce-18e4837318d9

### AI 协助分析你的浏览历史

查询：帮我分析一下过去一个月的浏览历史记录。

https://youtu.be/jf2UZfrR2Vk

https://github.com/user-attachments/assets/31b2e064-88c6-4adb-96d7-50748b826eae

### 网页对话翻译与总结

查询：翻译并总结当前网页的内容。  
https://youtu.be/FlJKS9UQyC8

https://github.com/user-attachments/assets/aa8ef2a1-2310-47e6-897a-769d85489396

### AI 帮你自动截图（全页截图）

查询：截取 Hugging Face 首页的完整页面。  
https://youtu.be/7ycK6iksWi4

https://github.com/user-attachments/assets/65c6eee2-6366-493d-a3bd-2b27529ff5b3

### AI 帮你自动截图（元素截图）

查询：截取 Hugging Face 首页的 Logo 图标。  
https://youtu.be/ev8VivANIrk

https://github.com/user-attachments/assets/d0cf9785-c2fe-4729-a3c5-7f2b8b96fe0c

### AI 协助管理书签

查询：将当前页面添加到书签，并放入合适的文件夹中。

https://youtu.be/R_83arKmFTo

https://github.com/user-attachments/assets/15a7d04c-0196-4b40-84c2-bafb5c26dfe0

### 自动关闭网页标签

查询：关闭所有与 shadcn 相关的网页标签。

https://youtu.be/2wzUT6eNVg4

https://github.com/user-attachments/assets/83de4008-bb7e-494d-9b0f-98325cfea592

## 🤝 贡献指南

我们非常欢迎你的贡献！详细参与规范请查看 [CONTRIBUTING.md](docs/CONTRIBUTING.md)。

## 🚧 未来规划

我们已为 Chrome MCP Server 的未来开发制定了以下计划：

- [ ] 身份认证（Authentication）
- [ ] 操作录制与回放（Recording and Playback）
- [ ] 工作流自动化（Workflow Automation）
- [ ] 增强浏览器支持（Firefox 扩展）

---

**想参与上述任何功能的开发？** 请查阅我们的[贡献指南](docs/CONTRIBUTING.md)，加入开发者社区！

## 📄 开源协议

本项目采用 MIT 许可证开源，详见 [LICENSE](LICENSE) 文件。

## 📚 更多文档

- [架构设计](docs/ARCHITECTURE.md) - 详细技术架构说明
- [TOOLS API](docs/TOOLS.md) - 完整工具接口文档
- [故障排除](docs/TROUBLESHOOTING.md) - 常见问题解决方案