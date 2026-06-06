# BlenderMCP - Blender 模型上下文协议集成

BlenderMCP 通过模型上下文协议（Model Context Protocol，简称 MCP）将 Blender 与 Claude AI 连接起来，使 Claude 能够直接与 Blender 交互并控制它。该集成支持通过提示词辅助进行 3D 建模、场景创建和对象操作。

**本项目没有官方网站。你在网上看到的任何网站均为非官方，且与本项目的开发团队无任何关联。使用这些网站的风险由你自行承担。**

[完整教程](https://www.youtube.com/watch?v=lCyQ717DuzQ)

### 加入社区
提供反馈、获取灵感，并基于该 MCP 进行扩展开发：[Discord](https://discord.gg/z5apgR8TFU)

### 支持者
[CodeRabbit](https://www.coderabbit.ai/)

**所有支持者：**

[赞助本项目](https://github.com/sponsors/ahujasid)

## 当前版本（1.5.5）
- 新增 Hunyuan3D 支持
- 查看 Blender 视口的截图，以便更好地理解场景
- 搜索并下载 Sketchfab 模型
- 通过 API 支持 Poly Haven 资产
- 支持使用 Hyper3D Rodin 生成 3D 模型
- 在远程主机上运行 Blender MCP
- 已执行工具的遥测数据（完全匿名）

### 安装新版本（针对现有用户）
- 新用户可直接前往“安装”部分。现有用户请参见以下说明：
- 下载最新的 `addon.py` 文件并替换旧版本，然后将其添加到 Blender
- 在 Claude 中删除该 MCP Server 后重新添加即可正常使用！


## 功能特性

- **双向通信**：通过基于 Socket 的服务器将 Claude AI 连接到 Blender
- **对象操作**：在 Blender 中创建、修改和删除 3D 对象
- **材质控制**：应用并修改材质与颜色
- **场景检查**：获取当前 Blender 场景的详细信息
- **代码执行**：从 Claude 运行任意 Python 代码

## 系统组件

该系统由两个主要部分组成：

1. **Blender 插件（`addon.py`）**：一个在 Blender 内部创建 Socket 服务器的插件，用于接收和执行命令
2. **MCP Server（`src/blender_mcp/server.py`）**：一个实现模型上下文协议的 Python 服务器，并与 Blender 插件进行连接

## 安装


### 前置条件

- Blender 3.0 或更高版本
- Python 3.10 或更高版本
- uv 包管理器： 

**如果你使用的是 Mac，请通过以下方式安装 uv：**
```bash
brew install uv
```
**在 Windows 上运行：**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" 
```
然后将 uv 添加到用户环境变量 Path 中（之后可能需要重启 Claude Desktop）：
```powershell
$localBin = "$env:USERPROFILE\.local\bin"
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;$localBin", "User")
```

否则，安装说明请参阅其官网：[Install uv](https://docs.astral.sh/uv/getting-started/installation/)

**⚠️ 请务必在安装好 UV 后再继续操作**

### 环境变量

以下环境变量可用于配置 Blender 连接：

- `BLENDER_HOST`：Blender Socket 服务器的主机地址（默认值："localhost"）
- `BLENDER_PORT`：Blender Socket 服务器的端口号（默认值：9876）

示例：
```bash
export BLENDER_HOST='host.docker.internal'
export BLENDER_PORT=9876
```

### 与 Claude Desktop 集成

[观看设置说明视频](https://www.youtube.com/watch?v=neoK_WMq92g)（假设你已安装好 uv）

前往 Claude > Settings > Developer > Edit Config > claude_desktop_config.json，并添加以下内容：

```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": [
                "blender-mcp"
            ]
        }
    }
}
```
<details>
<summary>Claude Code</summary>

使用 Claude Code CLI 添加 Blender MCP Server：

```bash
claude mcp add blender uvx blender-mcp
```
</details>

### 与 Cursor 集成

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/link/mcp%2Finstall?name=blender&config=eyJjb21tYW5kIjoidXZ4IGJsZW5kZXItbWNwIn0%3D)

Mac 用户请前往 Settings > MCP，并粘贴以下内容：
- 若要作为全局服务器使用，请点击“add new global MCP server”按钮后粘贴
- 若要作为项目专属服务器使用，请在项目根目录创建 `.cursor/mcp.json` 文件并粘贴


```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": [
                "blender-mcp"
            ]
        }
    }
}
```

Windows 用户请前往 Settings > MCP > Add Server，添加一个新服务器并配置以下设置：

```json
{
    "mcpServers": {
        "blender": {
            "command": "cmd",
            "args": [
                "/c",
                "uvx",
                "blender-mcp"
            ]
        }
    }
}
```

[Cursor 设置视频](https://www.youtube.com/watch?v=wgWsJshecac)

**⚠️ 仅运行一个 MCP Server 实例（在 Cursor 或 Claude Desktop 中二选一，不要同时运行）**

### 与 Visual Studio Code 集成

_前置条件_：请确保已安装 [Visual Studio Code](https://code.visualstudio.com/)。

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_blender--mcp_server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=ffffff)](vscode:mcp/install?%7B%22name%22%3A%22blender-mcp%22%2C%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22blender-mcp%22%5D%7D)

### 安装 Blender 插件

1. 从本仓库下载 `addon.py` 文件
2. 打开 Blender
3. 前往 Edit > Preferences > Add-ons（编辑 > 偏好设置 > 插件）
4. 点击“Install...”并选择 `addon.py` 文件
5. 勾选“Interface: Blender MCP”旁边的复选框以启用该插件


## 使用方法

### 建立连接
![BlenderMCP in the sidebar](assets/addon-instructions.png)

1. 在 Blender 中，打开 3D View 侧边栏（若未显示请按 N）
2. 找到“BlenderMCP”选项卡
3. 如需使用其 API 的资产，请勾选 Poly Haven 复选框（可选）
4. 点击“Connect to Claude”
5. 确保终端中正在运行 MCP Server

### 在 Claude 中使用

当你在 Claude 中配置好文件，且 Blender 中的插件已运行时，你将看到一个带有 Hammer（锤子）图标的工具栏。

![BlenderMCP in the sidebar](assets/hammer-icon.png)

#### 功能支持

- 获取场景和对象信息 
- 创建、删除和修改几何体
- 为对象应用或创建材质
- 在 Blender 中执行任意 Python 代码
- 通过 [Poly Haven](https://polyhaven.com/) 下载合适的模型、资产和 HDRIs
- 通过 [Hyper3D Rodin](https://hyper3d.ai/) 生成 AI 驱动的 3D 模型


### 示例命令

以下是一些你可以让 Claude 执行的操作示例：

- “在地下城中创建一个低多边形场景，有一条龙守护着一罐金子” [演示](https://www.youtube.com/watch?v=DqgKuLYUv00)
- “使用 HDRIs、纹理以及来自 Poly Haven 的岩石和植被模型，营造海滩氛围” [演示](https://www.youtube.com/watch?v=I29rn92gkC4)
- 提供一张参考图，并据此生成 Blender 场景 [演示](https://www.youtube.com/watch?v=FDRb03XPiRo)
- “通过 Hyper3D 生成一个花园小矮人（Garden Gnome）的 3D 模型”
- “获取当前场景的信息，并基于它创建一个 Three.js 草图” [演示](https://www.youtube.com/watch?v=jxbNI5L7AH8)
- “把这辆车改成红色金属质感” 
- “创建一个球体并将其放置在立方体上方”
- “将灯光设置为工作室风格”
- “将相机对准场景，并调整为等轴测视图（Isometric）”

## 与 Hyper3D 集成

Hyper3D 的免费试用密钥允许你每天生成有限数量的模型。如果达到每日限额，你可以等待次日重置，或前往 hyper3d.ai 和 fal.ai 获取你自己的密钥。

## 故障排除

- **连接问题**：请确保 Blender 插件服务器正在运行，且 MCP Server 已在 Claude 中配置完成。**切勿在终端中手动运行 uvx 命令**。有时第一条指令可能无法执行，但后续即可恢复正常。
- **超时错误**：尝试简化你的请求，或将其拆分为更小的步骤
- **Poly Haven 集成问题**：Claude 在此功能上的行为有时会不太稳定
- **是否尝试过重启？**: 如果仍然存在连接错误，请尝试同时重启 Claude 和 Blender 服务器


## 技术细节

### 通信协议

该系统基于 TCP Socket 使用简单的 JSON 协议：

- **指令（Commands）**：以包含 `type` 和可选 `params` 的 JSON 对象形式发送
- **响应（Responses）**：为包含 `status` 以及 `result` 或 `message` 的 JSON 对象

## 限制与安全注意事项

- `execute_blender_code` 工具允许在 Blender 中运行任意 Python 代码，功能强大但存在潜在风险。在生产环境中请谨慎使用。**使用前务必保存你的工作成果**。
- Poly Haven 需要下载模型、纹理和 HDRI 图像。如果你不希望使用该服务，请在 Blender 的复选框中将其关闭。 
- 复杂的操作可能需要拆分为更小的步骤来执行


#### 遥测（Telemetry）控制

BlenderMCP 会收集匿名使用数据以改进该工具。你可以通过以下两种方式控制遥测功能：

1. **在 Blender 中**：前往 Edit > Preferences > Add-ons > Blender MCP，取消勾选遥测同意复选框
   - 已授权（勾选）：收集匿名化的提示词、代码片段和截图
   - 未授权（未勾选）：仅收集最少的匿名使用数据（工具名称、成功/失败状态、耗时）

2. **环境变量**：通过运行以下命令完全禁用所有遥测功能：
```bash
DISABLE_TELEMETRY=true uvx blender-mcp
```

或将其添加到你的 MCP 配置中：
```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": ["blender-mcp"],
            "env": {
                "DISABLE_TELEMETRY": "true"
            }
        }
    }
}
```

所有遥测数据均已完全匿名化，仅用于改进 BlenderMCP。


## 贡献代码

欢迎贡献！请随时提交 Pull Request。

## 免责声明

此为第三方集成工具，并非由 Blender 官方开发。由 [Siddharth](https://x.com/sidahuj) 制作