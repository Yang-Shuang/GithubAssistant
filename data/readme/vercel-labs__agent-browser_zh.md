# agent-browser

面向 AI Agent 的浏览器自动化 CLI。快速的原生 Rust CLI。

[![skills.sh](https://skills.sh/b/vercel-labs/agent-browser)](https://skills.sh/vercel-labs/agent-browser)

## 安装

### 全局安装（推荐）

安装原生 Rust 二进制文件：

```bash
npm install -g agent-browser
agent-browser install  # 从 Chrome for Testing 下载 Chrome（仅首次运行需要）
```

### 项目安装（本地依赖）

适用于希望在 `package.json` 中锁定版本的项目：

```bash
npm install agent-browser
agent-browser install
```

然后通过 `package.json` 脚本调用，或直接执行 `agent-browser`。

### Homebrew (macOS)

```bash
brew install agent-browser
agent-browser install  # 从 Chrome for Testing 下载 Chrome（仅首次运行需要）
```

### Cargo (Rust)

```bash
cargo install agent-browser
agent-browser install  # 从 Chrome for Testing 下载 Chrome（仅首次运行需要）
```

### 从源码构建

需要 Node.js 24+、pnpm 11+ 和 Rust。

```bash
git clone https://github.com/vercel-labs/agent-browser
cd agent-browser
pnpm install
pnpm build
pnpm build:native   # 需要 Rust (https://rustup.rs)
pnpm link --global  # 使 agent-browser 全局可用
agent-browser install
```

### Linux 依赖

在 Linux 上，安装系统级依赖：

```bash
agent-browser install --with-deps
```

### 更新版本

升级到最新版本：

```bash
agent-browser upgrade
```

自动检测你的安装方式（npm、Homebrew 或 Cargo）并运行相应的更新命令。

### 环境要求

- **Chrome** - 运行 `agent-browser install` 从 [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/)（Google 官方自动化渠道）下载 Chrome。系统会自动检测现有的 Chrome、Brave、Playwright 和 Puppeteer 安装。守护进程无需 Playwright 或 Node.js。
- **Node.js 24+ 和 pnpm 11+** - 仅从源码构建时需要。
- **Rust** - 仅从源码构建时需要（见上方“从源码构建”）。

## 快速入门

```bash
agent-browser open example.com
agent-browser snapshot                    # 获取带引用标识符的无障碍树
agent-browser click @e2                   # 通过快照中的 ref 点击元素
agent-browser fill @e3 "test@example.com" # 通过 ref 填充输入框
agent-browser get text @e1                # 通过 ref 获取文本
agent-browser screenshot page.png
agent-browser close
```

无头（Headless）Chromium 截图默认隐藏原生滚动条以确保输出图像一致。启动时传入 `--hide-scrollbars false` 可保留原生滚动条可见。

### 传统选择器（同样支持）

```bash
agent-browser click "#submit"
agent-browser fill "#email" "test@example.com"
agent-browser find role button click --name "Submit"
```

## 命令

### 核心命令

```bash
agent-browser open                    # 启动浏览器（不导航）；停留在 about:blank
agent-browser open <url>              # 启动并导航到 URL（别名：goto, navigate）
agent-browser click <sel>             # 点击元素 (--new-tab 在新标签页中打开)
agent-browser dblclick <sel>          # 双击元素
agent-browser focus <sel>             # 聚焦元素
agent-browser type <sel> <text>       # 向元素输入文本
agent-browser fill <sel> <text>       # 清空并填充
agent-browser press <key>             # 按键 (Enter, Tab, Control+a) (别名：key)
agent-browser keyboard type <text>    # 使用真实击键输入（无需选择器，作用于当前焦点）
agent-browser keyboard inserttext <text>  # 插入文本且不触发按键事件（无需选择器）
agent-browser keydown <key>           # 按住按键
agent-browser keyup <key>             # 释放按键
agent-browser hover <sel>             # 悬停元素
agent-browser select <sel> <val>      # 选择下拉菜单选项
agent-browser check <sel>             # 勾选复选框
agent-browser uncheck <sel>           # 取消勾选复选框
agent-browser scroll <dir> [px]       # 滚动 (up/down/left/right, --selector <sel>)
agent-browser scrollintoview <sel>    # 将元素滚动到视图中（别名：scrollinto）
agent-browser drag <src> <tgt>        # 拖拽并放下
agent-browser upload <sel> <files>    # 上传文件
agent-browser screenshot [path]       # 截图 (--full 为全页截图，无 path 时保存到临时目录)
agent-browser screenshot --annotate   # 带编号元素标签的标注截图
agent-browser screenshot --screenshot-dir ./shots    # 保存到自定义目录
agent-browser screenshot --screenshot-format jpeg --screenshot-quality 80
agent-browser pdf <path>              # 保存为 PDF
agent-browser snapshot                # 带引用标识符的无障碍树（最适合 AI）
agent-browser eval <js>               # 执行 JavaScript (-b 用于 base64, --stdin 用于管道输入)
agent-browser connect <port>          # 通过 CDP 连接浏览器
agent-browser stream enable [--port <port>]  # 启动运行时 WebSocket 流式传输
agent-browser stream status           # 显示运行时流式传输状态和绑定端口
agent-browser stream disable          # 停止运行时 WebSocket 流式传输
agent-browser close                   # 关闭浏览器（别名：quit, exit）
agent-browser close --all             # 关闭所有活跃会话
agent-browser chat "<instruction>"    # AI 对话：自然语言控制浏览器（单次执行）
agent-browser chat                    # AI 对话：交互式 REPL 模式
```

### 获取信息

```bash
agent-browser get text <sel>          # 获取文本内容
agent-browser get html <sel>          # 获取 innerHTML
agent-browser get value <sel>         # 获取输入值
agent-browser get attr <sel> <attr>   # 获取属性
agent-browser get title               # 获取页面标题
agent-browser get url                 # 获取当前 URL
agent-browser get cdp-url             # 获取 CDP WebSocket URL（用于 DevTools、调试）
agent-browser get count <sel>         # 匹配元素计数
agent-browser get box <sel>           # 获取边界框坐标
agent-browser get styles <sel>        # 获取计算样式
```

### 检查状态

```bash
agent-browser is visible <sel>        # 检查是否可见
agent-browser is enabled <sel>        # 检查是否启用
agent-browser is checked <sel>        # 检查是否已勾选
```

### 查找元素（语义定位器）

```bash
agent-browser find role <role> <action> [value]       # 通过 ARIA role
agent-browser find text <text> <action>               # 通过文本内容
agent-browser find label <label> <action> [value]     # 通过标签
agent-browser find placeholder <ph> <action> [value]  # 通过占位符
agent-browser find alt <text> <action>                # 通过替代文本 (alt)
agent-browser find title <text> <action>              # 通过 title 属性
agent-browser find testid <id> <action> [value]       # 通过 data-testid
agent-browser find first <sel> <action> [value]       # 第一个匹配项
agent-browser find last <sel> <action> [value]        # 最后一个匹配项
agent-browser find nth <n> <sel> <action> [value]     # 第 N 个匹配项
```

**操作（Actions）：** `click`, `fill`, `type`, `hover`, `focus`, `check`, `uncheck`, `text`

**选项：** `--name <name>`（通过无障碍名称过滤 role）、`--exact`（要求精确文本匹配）

**示例：**

```bash
agent-browser find role button click --name "Submit"
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "test@test.com"
agent-browser find first ".item" click
agent-browser find nth 2 "a" text
```

### 等待

```bash
agent-browser wait <selector>         # 等待元素可见
agent-browser wait <ms>               # 等待指定时间（毫秒）
agent-browser wait --text "Welcome"   # 等待文本出现（子串匹配）
agent-browser wait --url "**/dash"    # 等待 URL 模式匹配
agent-browser wait --load networkidle # 等待加载状态为网络空闲
agent-browser wait --fn "window.ready === true"  # 等待 JS 条件满足

# 等待文本/元素消失
agent-browser wait --fn "!document.body.innerText.includes('Loading...')"
agent-browser wait "#spinner" --state hidden
```

**加载状态：** `load`, `domcontentloaded`, `networkidle`

### 批量执行

在单次调用中执行多条命令。命令可以作为带引号的参数传递，或通过 stdin 以 JSON 形式管道输入。这避免了在多步骤工作流中每条命令都产生进程启动开销。

```bash
# 参数模式：每个带引号的参数是一条完整命令
agent-browser batch "open https://example.com" "snapshot -i" "screenshot"

# 配合 --bail 在首次出错时停止
agent-browser batch --bail "open https://example.com" "click @e1" "screenshot"

# stdin 模式：通过管道输入 JSON 格式的命令
echo '[
  ["open", "https://example.com"],
  ["snapshot", "-i"],
  ["click", "@e1"],
  ["screenshot", "result.png"]
]' | agent-browser batch --json
```

### 剪贴板

```bash
agent-browser clipboard read                      # 从剪贴板读取文本
agent-browser clipboard write "Hello, World!"     # 向剪贴板写入文本
agent-browser clipboard copy                      # 复制当前选区 (Ctrl+C)
agent-browser clipboard paste                     # 粘贴剪贴板内容 (Ctrl+V)
```

### 鼠标控制

```bash
agent-browser mouse move <x> <y>      # 移动鼠标
agent-browser mouse down [button]     # 按下按钮（left/right/middle）
agent-browser mouse up [button]       # 释放按钮
agent-browser mouse wheel <dy> [dx]   # 滚轮滚动
```

### 浏览器设置

```bash
agent-browser set viewport <w> <h> [scale]  # 设置视口尺寸（scale 用于视网膜屏，例如 2）
agent-browser set device <name>       # 模拟设备 ("iPhone 14")
agent-browser set geo <lat> <lng>     # 设置地理位置
agent-browser set offline [on|off]    # 切换离线模式
agent-browser set headers <json>      # 额外 HTTP 请求头
agent-browser set credentials <u> <p> # HTTP 基本认证
agent-browser set media [dark|light]  # 模拟配色方案
```

### Cookie 与存储

```bash
agent-browser cookies                 # 获取所有 cookie
agent-browser cookies set <name> <val> # 设置 cookie
agent-browser cookies set --curl <file> # 从 Copy-as-cURL 导出、JSON 数组或裸 Cookie 请求头导入（自动检测）
agent-browser cookies clear           # 清除 cookie

agent-browser storage local           # 获取所有 localStorage
agent-browser storage local <key>     # 获取指定键
agent-browser storage local set <k> <v>  # 设置值
agent-browser storage local clear     # 清空全部

agent-browser storage session         # sessionStorage 同上操作
```

### 网络

```bash
agent-browser network route <url>              # 拦截请求
agent-browser network route <url> --abort      # 阻止请求
agent-browser network route <url> --body <json>  # 模拟响应体
agent-browser network route '*' --abort --resource-type script  # 仅阻止脚本资源
agent-browser network unroute [url]            # 移除路由规则
agent-browser network requests                 # 查看已跟踪的请求
agent-browser network requests --filter api    # 按名称过滤请求
agent-browser network requests --type xhr,fetch  # 按资源类型过滤
agent-browser network requests --method POST   # 按 HTTP 方法过滤
agent-browser network requests --status 2xx    # 按状态码过滤（200, 2xx, 400-499）
agent-browser network request <requestId>      # 查看完整请求/响应详情
agent-browser network har start                # 开始 HAR 录制
agent-browser network har stop [output.har]    # 停止并保存 HAR（省略路径则保存到临时目录）
```

### 标签页与窗口

```bash
agent-browser tab                              # 列出标签页（显示 `tabId` 和可选的 label）
agent-browser tab new [url]                    # 新建标签页（可选附带 URL）
agent-browser tab new --label docs [url]       # 新建带用户指定 label 的标签页
agent-browser tab <t<N>|label>                 # 通过 id 或 label 切换到标签页
agent-browser tab close [t<N>|label]           # 关闭标签页（默认为当前活跃标签）
agent-browser window new                       # 新建窗口
```

标签页 ID 是稳定的字符串，格式为 `t1`、`t2`、`t3`。它们在会话期间永远不会被重用，因此脚本和 Agent 可以在其他标签页打开或关闭后继续引用同一个标签页。不支持使用位置整数（如 `tab 2`）；必须使用 `t` 前缀以将句柄与索引区分开，并沿用元素 ref 的 `@e1` 命名惯例。

你还可以分配一个易记的 label（如 `docs`、`app`、`admin`），并与 id 互换使用。label 永远不会自动生成，导航时也不会被重写——它们由你自定义且保持不变：

```bash
agent-browser tab new --label docs https://docs.example.com
agent-browser tab docs               # 切换到 docs 标签页
agent-browser snapshot               # 为 docs 填充 refs
agent-browser click @e3              # 点击操作使用 docs 的 refs
agent-browser tab close docs         # 通过 label 关闭
```

### 框架（Frames）

```bash
agent-browser frame <sel>             # 切换到 iframe
agent-browser frame main              # 返回主框架
```

### 对话框

```bash
agent-browser dialog accept [text]    # 接受（可选附带提示文本）
agent-browser dialog dismiss          # 取消/关闭
agent-browser dialog status           # 检查当前是否有打开的对话框
```

默认情况下，`alert` 和 `beforeunload` 对话框会被自动接受，以免阻塞 Agent。`confirm` 和 `prompt` 对话框仍需显式处理。使用 `--no-auto-dialog`（或设置 `AGENT_BROWSER_NO_AUTO_DIALOG=1`）可禁用自动处理。

当存在待处理的 JavaScript 对话框时，所有命令响应中都会包含一个 `warning` 字段，其中带有对话框类型和消息。

### 差异对比 (Diff)

```bash
agent-browser diff snapshot                              # 比较当前快照与上次快照
agent-browser diff snapshot --baseline before.txt        # 比较当前快照与保存的快照文件
agent-browser diff snapshot --selector "#main" --compact # 限定范围的快照差异对比
agent-browser diff screenshot --baseline before.png      # 视觉像素级差异对比（基于基准图）
agent-browser diff screenshot --baseline b.png -o d.png  # 将差异图像保存到自定义路径
agent-browser diff screenshot --baseline b.png -t 0.2    # 调整颜色阈值 (0-1)
agent-browser diff url https://v1.com https://v2.com     # 比较两个 URL（快照差异对比）
agent-browser diff url https://v1.com https://v2.com --screenshot  # 同时生成视觉差异图
agent-browser diff url https://v1.com https://v2.com --wait-until networkidle  # 自定义等待策略
agent-browser diff url https://v1.com https://v2.com --selector "#main"  # 限定到特定元素范围
```

### 调试 (Debug)

```bash
agent-browser trace start             # 开始录制 Trace
agent-browser trace stop [path]       # 停止并保存 Trace
agent-browser profiler start          # 启动 Chrome DevTools 性能分析
agent-browser profiler stop [path]    # 停止并保存性能数据 (.json)
agent-browser console                 # 查看控制台消息 (log, error, warn, info)
agent-browser console --json          # JSON 格式输出，包含原始 CDP 参数以便程序化访问
agent-browser console --clear         # 清空控制台
agent-browser errors                  # 查看页面错误（未捕获的 JavaScript 异常）
agent-browser errors --clear          # 清除错误记录
agent-browser highlight <sel>         # 高亮显示元素
agent-browser inspect                 # 为当前活跃页面打开 Chrome DevTools
agent-browser state save <path>       # 保存认证状态
agent-browser state load <path>       # 加载认证状态
agent-browser state list              # 列出已保存的状态文件
agent-browser state show <file>       # 显示状态摘要
agent-browser state rename <old> <new> # 重命名状态文件
agent-browser state clear [name]      # 清除会话的指定状态
agent-browser state clear --all       # 清除所有已保存的状态
agent-browser state clean --older-than <days>  # 删除超过 N 天的旧状态
```

### 导航

```bash
agent-browser back                    # 后退
agent-browser forward                 # 前进
agent-browser reload                  # 刷新页面
agent-browser pushstate <url>         # SPA 客户端侧导航；自动检测 window.next.router.push，
                                      # 否则回退到 history.pushState + popstate
```

### 预导航配置 (Pre-navigation setup)

某些流程（SSR 调试、受保护源域的认证 cookie、初始化脚本）需要在*首次导航前*设置状态。使用 `open` 不带 URL 启动浏览器，然后配置 cookies / 路由 / 初始化脚本，最后再执行导航。`batch` 可将这些操作合并为一次 CLI 调用：

```bash
agent-browser batch \
  '["open"]' \
  '["network","route","*","--abort","--resource-type","script"]' \
  '["cookies","set","--curl","cookies.curl","--domain","localhost"]' \
  '["navigate","http://localhost:3000/target"]'
```

不使用 `batch` 时，相同流程需要三条命令，虽然它们会复用同一个守护进程（速度快），但并非单次调用完成。

### React / Web Vitals

agent-browser 内置了对 React 深度探查和通用 Web Vitals 指标的一流支持。React 相关命令需要在启动时安装 React DevTools hook；Web Vitals 和 pushstate 则与框架无关。

```bash
agent-browser open --enable react-devtools <url>   # 启动并安装 React hook
agent-browser react tree                           # 完整组件树
agent-browser react inspect <fiberId>              # props, hooks, state, source
agent-browser react renders start                  # 开始记录 Fiber 渲染
agent-browser react renders stop [--json]          # 停止并打印性能分析 (--json 输出原始数据)
agent-browser react suspense [--only-dynamic] [--json]  # Suspense 边界 + 分类器
                                                         # --only-dynamic 隐藏“静态”列表
agent-browser vitals [url] [--json]                # LCP/CLS/TTFB/FCP/INP + 水合摘要
```

每个 `react ...` 子命令都要求在启动时传递了 `--enable react-devtools`（React DevTools `installHook.js` 已嵌入二进制文件中）。否则这些命令会报错：`React DevTools hook not installed - relaunch with --enable react-devtools`。

适用于任何 React 应用——Next.js、Remix、Vite+React、CRA、TanStack Start、React Native Web 等。`vitals` 和 `pushstate` 与框架无关。默认情况下 `vitals` 会打印摘要；传入 `--json` 可获取完整的结构化数据负载。

### 初始化脚本 (Init scripts)

```bash
agent-browser open --init-script <path>           # 在首次导航前注册页面初始化脚本
                                                  # （可重复使用；也支持 AGENT_BROWSER_INIT_SCRIPTS 环境变量）
agent-browser addinitscript <js>                  # 运行时注册（返回标识符）
agent-browser removeinitscript <identifier>       # 移除之前注册的初始化脚本
```

### 安装与诊断 (Setup)

```bash
agent-browser install                 # 从 Chrome for Testing 下载 Chrome（Google 官方自动化渠道）
agent-browser install --with-deps     # 同时安装系统依赖（Linux）
agent-browser upgrade                 # 升级到最新版本
agent-browser doctor                  # 诊断环境并自动清理残留的守护进程文件
agent-browser doctor --fix            # 同时执行破坏性修复（重装 Chrome、清除旧状态等）
agent-browser doctor --offline --quick  # 跳过网络探测和实时启动测试
```

`doctor` 会检查你的环境、Chrome 安装情况、守护进程状态、配置文件、加密密钥、Provider、网络连通性，并运行一次真实的无头浏览器启动测试。残留的 socket/pid 辅助文件会被自动清理。输出结果也支持 `--json` 格式以便 Agent 解析。

### Skills (技能)

```bash
agent-browser skills                  # 列出可用技能
agent-browser skills list             # 同上
agent-browser skills get <name>       # 输出技能的完整内容
agent-browser skills get <name> --full  # 包含引用和模板
agent-browser skills get --all        # 输出所有技能
agent-browser skills path [name]      # 打印技能目录路径
```

提供与已安装 CLI 版本严格匹配的内嵌技能内容。AI Agent 可借此获取最新指令，而非依赖可能过时的缓存副本。设置 `AGENT_BROWSER_SKILLS_DIR` 可覆盖技能目录路径。

## 认证 (Authentication)

agent-browser 提供了多种持久化登录会话的方式，让你无需每次运行都重新认证。

### 快速概览

| 方式 | 适用场景 | 标志 / 环境变量 |
|----------|----------|------------|
| **Chrome Profile 复用** | 零配置复用现有 Chrome 登录状态（cookies、会话） | `--profile <name>` / `AGENT_BROWSER_PROFILE` |
| **持久化 Profile** | 跨重启保留完整的浏览器状态（cookies、IndexedDB、Service Workers、缓存） | `--profile <path>` / `AGENT_BROWSER_PROFILE` |
| **会话持久化 (Session Persistence)** | 按名称自动保存/恢复 cookies + localStorage | `--session-name <name>` / `AGENT_BROWSER_SESSION_NAME` |
| **从浏览器导入认证** | 抓取已登录 Chrome 会话的认证状态 | `--auto-connect` + `state save` |
| **状态文件 (State file)** | 启动时加载之前保存的状态 JSON | `--state <path>` / `AGENT_BROWSER_STATE` |
| **认证保险箱 (Auth vault)** | 本地存储凭证（加密），按名称登录 | `auth save` / `auth login` |

### 从浏览器导入认证

如果你已经在 Chrome 中登录了某个网站，可以抓取该认证状态并复用：

```bash
# 1. 启动启用远程调试的 Chrome
#    macOS:
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222
#    或使用 --auto-connect 自动发现已运行的 Chrome

# 2. 连接并保存认证状态
agent-browser --auto-connect state save ./my-auth.json

# 3. 在后续会话中使用保存的认证
agent-browser --state ./my-auth.json open https://app.example.com/dashboard

# 4. 或使用 --session-name 实现自动持久化
agent-browser --session-name myapp state load ./my-auth.json
# 此后，--session-name myapp 会自动保存/恢复该状态
```

> **安全提示：**
> - `--remote-debugging-port` 会在 localhost 上暴露完整的浏览器控制权。任何本地进程均可连接。仅在可信机器上使用，并在完成后关闭 Chrome。
> - 状态文件包含明文会话令牌。请将其加入 `.gitignore` 并在不再需要时删除。如需静态加密（Encryption at rest），设置 `AGENT_BROWSER_ENCRYPTION_KEY`（详见 [State Encryption](#state-encryption)）。

有关登录流程、OAuth、双因素认证 (2FA)、基于 Cookie 的认证和认证保险箱的完整详情，请参阅 [Authentication](docs/src/app/sessions/page.mdx) 文档。

## 会话 (Sessions)

运行多个隔离的浏览器实例：

```bash
# 不同会话
agent-browser --session agent1 open site-a.com
agent-browser --session agent2 open site-b.com

# 或通过环境变量
AGENT_BROWSER_SESSION=agent1 agent-browser click "#btn"

# 列出活跃会话
agent-browser session list
# 输出:
# Active sessions:
# -> default
#    agent1

# 显示当前会话
agent-browser session
```

每个会话拥有独立的：

- 浏览器实例
- Cookie 和存储数据
- 导航历史
- 认证状态

## Chrome Profile 复用

使用现有登录状态的最快方式：向 `--profile` 传递一个 Chrome profile 名称：

```bash
# 列出可用的 Chrome profiles
agent-browser profiles

# 复用默认 Chrome profile 的登录状态
agent-browser --profile Default open https://gmail.com

# 使用命名 profile（按显示名称或目录名）
agent-browser --profile "Work" open https://app.example.com

# 或通过环境变量
AGENT_BROWSER_PROFILE=Default agent-browser open https://gmail.com
```

这会将你的 Chrome profile 复制到临时目录（只读快照，不会修改原始 profile），使浏览器启动时携带你现有的 cookies 和会话。

> **注意：** 在 Windows 上，如果使用 `--profile <name>` 时 Chrome 正在运行，请先关闭 Chrome，因为部分 profile 文件可能被锁定。

## 持久化 Profiles (Persistent Profiles)

对于需要跨浏览器重启保留状态的自定义 profile 目录，向 `--profile` 传递路径：

```bash
# 使用持久化 profile 目录
agent-browser --profile ~/.myapp-profile open myapp.com

# 登录一次后，认证会话可重复使用
agent-browser --profile ~/.myapp-profile open myapp.com/dashboard

# 或通过环境变量
AGENT_BROWSER_PROFILE=~/.myapp-profile agent-browser open myapp.com
```

该 profile 目录会存储：

- Cookies 和 localStorage
- IndexedDB 数据
- Service Workers
- 浏览器缓存
- 登录会话

**提示：** 为不同项目使用不同的 profile 路径，以保持其浏览器状态隔离。

## 会话持久化 (Session Persistence)

或者，使用 `--session-name` 自动在浏览器重启间保存和恢复 cookies 与 localStorage：

```bash
# 为 "twitter" 会话自动保存/加载状态
agent-browser --session-name twitter open twitter.com

# 登录一次后，状态会自动持久化
# 状态文件存储在 ~/.agent-browser/sessions/

# 或通过环境变量
export AGENT_BROWSER_SESSION_NAME=twitter
agent-browser open twitter.com
```

### 状态加密 (State Encryption)

使用 AES-256-GCM 对静态保存的会话数据进行加密：

```bash
# 生成密钥: openssl rand -hex 32
export AGENT_BROWSER_ENCRYPTION_KEY=<64-char-hex-key>

# 状态文件现在会自动加密
agent-browser --session-name secure open example.com
```

| 变量                          | 描述                                        |
| --------------------------------- | -------------------------------------------------- |
| `AGENT_BROWSER_SESSION_NAME`      | 自动保存/加载的状态持久化名称              |
| `AGENT_BROWSER_ENCRYPTION_KEY`    | AES-256-GCM 加密的 64 位十六进制密钥         |
| `AGENT_BROWSER_STATE_EXPIRE_DAYS` | 自动删除超过 N 天的状态（默认：30） |

## 安全 (Security)

agent-browser 包含用于安全部署 AI Agent 的安全功能。所有功能均为可选开启，现有工作流在未显式启用前不受影响：

- **认证保险箱 (Authentication Vault)**：本地存储凭证（始终加密），按名称引用。LLM 永远不会看到密码。`auth login` 会导航至页面并等待登录表单选择器出现（兼容 SPA，超时时间遵循默认操作超时）。若未设置 `AGENT_BROWSER_ENCRYPTION_KEY`，会在 `~/.agent-browser/.encryption-key` 自动生成密钥：`echo "pass" | agent-browser auth save github --url https://github.com/login --username user --password-stdin` 然后执行 `agent-browser auth login github`
- **内容边界标记 (Content Boundary Markers)**：用分隔符包裹页面输出，使 LLM 能够区分工具输出与不受信的内容：`--content-boundaries`
- **域名白名单 (Domain Allowlist)**：限制导航至受信任的域名（通配符如 `*.example.com` 也匹配裸域）：`--allowed-domains "example.com,*.example.com"`。对非白名单域的静态资源请求（脚本、图片、fetch）及 WebSocket/EventSource 连接也会被拦截。请包含目标页面依赖的任何 CDN 域名（例如 `*.cdn.example.com`）。
- **操作策略 (Action Policy)**：通过静态策略文件限制破坏性操作：`--action-policy ./policy.json`
- **操作确认 (Action Confirmation)**：对敏感操作类别要求显式审批：`--confirm-actions eval,download`
- **输出长度限制 (Output Length Limits)**：防止上下文溢出：`--max-output 50000`

| 变量                            | 描述                              |
| ----------------------------------- | ---------------------------------------- |
| `AGENT_BROWSER_CONTENT_BOUNDARIES`  | 用边界标记包裹页面输出     |
| `AGENT_BROWSER_MAX_OUTPUT`          | 页面输出的最大字符数           |
| `AGENT_BROWSER_ALLOWED_DOMAINS`     | 逗号分隔的允许域名模式  |
| `AGENT_BROWSER_ACTION_POLICY`       | 操作策略 JSON 文件路径          |
| `AGENT_BROWSER_CONFIRM_ACTIONS`     | 需要确认的操作类别 |
| `AGENT_BROWSER_CONFIRM_INTERACTIVE` | 启用交互式确认提示  |

详见 [Security documentation](https://agent-browser.dev/security)。

## 快照选项 (Snapshot Options)

`snapshot` 命令支持过滤以减小输出体积：

```bash
agent-browser snapshot                    # 完整无障碍树
agent-browser snapshot -i                 # 仅交互元素（按钮、输入框、链接）
agent-browser snapshot -i --urls          # 带链接 URL 的交互元素
agent-browser snapshot -c                 # 紧凑模式（移除空的结构性元素）
agent-browser snapshot -d 3               # 限制深度为 3 层
agent-browser snapshot -s "#main"         # 限定到 CSS 选择器范围
agent-browser snapshot -i -c -d 5         # 组合选项
```

| 选项                 | 描述                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| `-i, --interactive`    | 仅显示交互元素（按钮、链接、输入框）                 |
| `-u, --urls`           | 包含链接元素的 href URL                                     |
| `-c, --compact`        | 移除空的结构性元素                                        |
| `-d, --depth <n>`      | 限制树深度                                                        |
| `-s, --selector <sel>` | 限定到 CSS 选择器范围                                                   |

## 标注截图 (Annotated Screenshots)

`--annotate` 标志会在截图中的交互元素上叠加编号标签。每个标签 `[N]` 对应 ref `@eN`，因此相同的 refs 可同时用于视觉和基于文本的工作流。

CDP 支持的浏览器路径（Chrome/Lightpanda）支持标注截图。Safari/WebDriver 后端暂不支持 `--annotate`。

```bash
agent-browser screenshot --annotate
# -> Screenshot saved to /tmp/screenshot-2026-02-17T12-00-00-abc123.png
#    [1] @e1 button "Submit"
#    [2] @e2 link "Home"
#    [3] @e3 textbox "Email"
```

生成标注截图后，refs 会被缓存，你可以立即与元素交互：

```bash
agent-browser screenshot --annotate ./page.png
agent-browser click @e2     # 点击标号为 [2] 的 "Home" 链接
```

这对于能够推理视觉布局的多模态 AI 模型非常有用，例如处理未标注的图标按钮、Canvas 元素或文本无障碍树无法捕获的视觉状态。

## 选项 (Options)

| Option | Description |
|--------|-------------|
| `--session <name>` | 使用隔离会话（或使用 `AGENT_BROWSER_SESSION` 环境变量） |
| `--session-name <name>` | 自动保存/恢复会话状态（或使用 `AGENT_BROWSER_SESSION_NAME` 环境变量） |
| `--profile <name\|path>` | Chrome profile 名称或持久化目录路径（或使用 `AGENT_BROWSER_PROFILE` 环境变量） |
| `--state <path>` | 从 JSON 文件加载存储状态（或使用 `AGENT_BROWSER_STATE` 环境变量） |
| `--headers <json>` | 设置作用域为 URL 源 (origin) 的 HTTP 请求头 |
| `--executable-path <path>` | 自定义浏览器可执行文件（或使用 `AGENT_BROWSER_EXECUTABLE_PATH` 环境变量） |
| `--extension <path>` | 加载浏览器扩展（可重复使用；或使用 `AGENT_BROWSER_EXTENSIONS` 环境变量） |
| `--init-script <path>` | 在首次导航前注册页面初始化脚本（可重复使用；或使用 `AGENT_BROWSER_INIT_SCRIPTS` 环境变量） |
| `--enable <feature>` | 内置初始化脚本：`react-devtools`（可重复或逗号分隔；或使用 `AGENT_BROWSER_ENABLE` 环境变量） |
| `--args <args>` | 浏览器启动参数，逗号或换行分隔（或使用 `AGENT_BROWSER_ARGS` 环境变量） |
| `--user-agent <ua>` | 自定义 User-Agent 字符串（或使用 `AGENT_BROWSER_USER_AGENT` 环境变量） |
| `--proxy <url>` | 代理服务器 URL（可选包含认证信息；或使用 `AGENT_BROWSER_PROXY` 环境变量） |
| `--proxy-bypass <hosts>` | 绕过代理的主机列表（或使用 `AGENT_BROWSER_PROXY_BYPASS` 环境变量） |
| `--ignore-https-errors` | 忽略 HTTPS 证书错误（对自签名证书很有用） |
| `--allow-file-access` | 允许 file:// URL 访问本地文件（仅 Chromium） |
| `--hide-scrollbars <bool>` | 在无头 Chromium 截图中隐藏原生滚动条，默认启用（或使用 `AGENT_BROWSER_HIDE_SCROLLBARS` 环境变量） |
| `-p, --provider <name>` | 云浏览器 Provider（或使用 `AGENT_BROWSER_PROVIDER` 环境变量） |
| `--device <name>` | iOS 设备名称，例如 "iPhone 15 Pro"（或使用 `AGENT_BROWSER_IOS_DEVICE` 环境变量） |
| `--json` | JSON 格式输出（适用于 Agent） |
| `--annotate` | 带编号元素标签的标注截图（或使用 `AGENT_BROWSER_ANNOTATE` 环境变量） |
| `--screenshot-dir <path>` | 默认截图输出目录（或使用 `AGENT_BROWSER_SCREENSHOT_DIR` 环境变量） |
| `--screenshot-quality <n>` | JPEG 质量 0-100（或使用 `AGENT_BROWSER_SCREENSHOT_QUALITY` 环境变量） |
| `--screenshot-format <fmt>` | 截图格式：`png`, `jpeg`（或使用 `AGENT_BROWSER_SCREENSHOT_FORMAT` 环境变量） |
| `--headed` | 显示浏览器窗口（非无头模式）（或使用 `AGENT_BROWSER_HEADED` 环境变量） |
| `--cdp <port\|url>` | 通过 Chrome DevTools Protocol 连接（端口或 WebSocket URL） |
| `--auto-connect` | 自动发现并连接到正在运行的 Chrome（或使用 `AGENT_BROWSER_AUTO_CONNECT` 环境变量） |
| `--color-scheme <scheme>` | 配色方案：`dark`, `light`, `no-preference`（或使用 `AGENT_BROWSER_COLOR_SCHEME` 环境变量） |
| `--download-path <path>` | 默认下载目录（或使用 `AGENT_BROWSER_DOWNLOAD_PATH` 环境变量） |
| `--content-boundaries` | 用边界标记包裹页面输出以保障 LLM 安全（或使用 `AGENT_BROWSER_CONTENT_BOUNDARIES` 环境变量） |
| `--max-output <chars>` | 将页面输出截断至 N 个字符（或使用 `AGENT_BROWSER_MAX_OUTPUT` 环境变量） |
| `--allowed-domains <list>` | 逗号分隔的允许域名模式（或使用 `AGENT_BROWSER_ALLOWED_DOMAINS` 环境变量） |
| `--action-policy <path>` | 操作策略 JSON 文件路径（或使用 `AGENT_BROWSER_ACTION_POLICY` 环境变量） |
| `--confirm-actions <list>` | 需要确认的操作类别（或使用 `AGENT_BROWSER_CONFIRM_ACTIONS` 环境变量） |
| `--confirm-interactive` | 交互式确认提示；若 stdin 非 TTY 则自动拒绝（或使用 `AGENT_BROWSER_CONFIRM_INTERACTIVE` 环境变量） |
| `--engine <name>` | 浏览器引擎：`chrome`（默认）, `lightpanda`（或使用 `AGENT_BROWSER_ENGINE` 环境变量） |
| `--no-auto-dialog` | 禁用 `alert`/`beforeunload` 对话框的自动关闭（或使用 `AGENT_BROWSER_NO_AUTO_DIALOG` 环境变量） |
| `--model <name>` | chat 命令使用的 AI 模型（或使用 `AI_GATEWAY_MODEL` 环境变量） |
| `-v`, `--verbose` | 显示工具命令及其原始输出（chat 模式） |
| `-q`, `--quiet` | 仅显示 AI 文本响应，隐藏工具调用（chat 模式） |
| `--config <path>` | 使用自定义配置文件（或使用 `AGENT_BROWSER_CONFIG` 环境变量） |
| `--debug` | 调试输出 |

## 可观测性仪表盘 (Observability Dashboard)

通过本地 Web 仪表盘实时监控 agent-browser 会话，展示实时视口和命令活动流。

```bash
# 启动仪表盘服务器（后台运行在端口 4848）
agent-browser dashboard start
agent-browser dashboard start --port 8080   # 自定义端口

# 所有会话都会自动显示在仪表盘中
agent-browser open example.com

# 停止仪表盘
agent-browser dashboard stop
```

仪表盘作为独立后台进程运行在端口 4848，与浏览器会话无关。即使没有活跃会话，它也会保持可用状态。可通过 `http://localhost:4848` 或代理/转发 URL（如 `https://dashboard.agent-browser.localhost` 或 Coder 工作区 URL）访问。浏览器保持在仪表盘源域；特定于会话的标签页、状态和流流量会在内部进行代理，因此无需暴露会话端口。

仪表盘显示：
- **实时视口**：来自浏览器的实时 JPEG 帧
- **活动流 (Activity feed)**：按时间顺序排列的命令/结果流，带计时器和可展开详情
- **控制台输出**：浏览器控制台消息（log, warn, error）
- **会话创建**：通过 UI 使用本地引擎（Chrome、Lightpanda）或云 Provider（AgentCore、Browserbase、Browserless、Browser Use、Kernel）创建新会话
- **AI Chat**：直接在仪表盘中与 AI 助手对话（需要配置 Vercel AI Gateway）

### AI Chat (仪表盘)

仪表盘包含一个可选的 AI 聊天面板，由 Vercel AI Gateway 驱动。CLI 中也提供了相同的功能，可通过 `chat` 命令直接使用。设置以下环境变量以启用 AI 聊天：

```bash
export AI_GATEWAY_API_KEY=gw_your_key_here
export AI_GATEWAY_MODEL=anthropic/claude-sonnet-4.6           # 可选，此为默认值
export AI_GATEWAY_URL=https://ai-gateway.vercel.sh           # 可选，此为默认值
```

**CLI 用法：**

```bash
agent-browser chat "open google.com and search for cats"     # 单次执行
agent-browser chat                                           # 交互式 REPL
agent-browser -q chat "summarize this page"                  # 静默模式（仅文本）
agent-browser -v chat "fill in the login form"               # 详细模式（显示命令输出）
agent-browser --model openai/gpt-4o chat "take a screenshot" # 覆盖模型
```

`chat` 命令将自然语言指令翻译为 agent-browser 命令，执行它们并流式传输 AI 响应。在交互模式下，输入 `quit` 退出。使用 `--json` 可获取适合 Agent 消费的结构化输出。

**仪表盘用法：**

聊天标签页始终可见于仪表盘中。当设置了 `AI_GATEWAY_API_KEY` 时，Rust 服务器会将请求代理到网关，并使用 Vercel AI SDK 的 UI Message Stream 协议流式返回响应。若未设置密钥，发送消息时会显示内联错误提示。

## 配置 (Configuration)

创建 `agent-browser.json` 文件以设置持久化默认值，避免在每个命令中重复传递标志位。

**位置（优先级从低到高）：**

1. `~/.agent-browser/config.json`: 用户级默认值
2. `./agent-browser.json`: 项目级覆盖配置（工作目录下）
3. `AGENT_BROWSER_*` 环境变量会覆盖配置文件中的值
4. CLI 标志位拥有最高优先级

**示例 `agent-browser.json`：**

```json
{
  "headed": true,
  "proxy": "http://localhost:8080",
  "profile": "./browser-data",
  "userAgent": "my-agent/1.0",
  "hideScrollbars": false,
  "ignoreHttpsErrors": true
}
```

使用 `--config <path>` 或 `AGENT_BROWSER_CONFIG` 加载特定配置文件，而非默认配置：

```bash
agent-browser --config ./ci-config.json open example.com
AGENT_BROWSER_CONFIG=./ci-config.json agent-browser open example.com
```

上表中的所有选项均可在配置文件中通过 camelCase 键名设置（例如 `--executable-path` 变为 `"executablePath"`，`--proxy-bypass` 变为 `"proxyBypass"`）。未知键会被忽略以保持向前兼容。

提供了 [JSON Schema](agent-browser.schema.json) 用于 IDE 自动补全和验证。在配置文件中添加 `$schema` 键即可启用：

```json
{
  "$schema": "https://agent-browser.dev/schema.json",
  "headed": true
}
```

布尔标志位接受可选的 `true`/`false` 值以覆盖配置设置。例如，`--headed false` 会禁用配置中的 `"headed": true`。单独的 `--headed` 等价于 `--headed true`。

自动发现的缺失配置文件会被静默忽略。如果 `--config <path>` 指向一个不存在或无效的文件，agent-browser 会报错退出。用户和项目配置中的扩展（Extensions）是合并（拼接）而非替换的。

> **提示：** 如果你的项目级 `agent-browser.json` 包含环境特定值（路径、代理），建议将其加入 `.gitignore`。

## 默认超时 (Default Timeout)

标准操作（点击、等待、填充等）的默认超时时间为 25 秒。这故意设置为低于 CLI 的 30 秒 IPC 读取超时，以便守护进程返回正确的错误信息，而不是让 CLI 因 EAGAIN 超时而中断。

通过环境变量覆盖默认超时：

```bash
# 为慢速页面设置更长的超时（毫秒）
export AGENT_BROWSER_DEFAULT_TIMEOUT=45000
```

> **注意：** 将其设置为超过 30000（30秒）可能导致 EAGAIN 错误，因为 CLI 的读取超时会先于守护进程响应而触发。CLI 会自动重试瞬时错误，但响应时间会增加。

| 变量                        | 描述                              |
| ------------------------------- | ---------------------------------------- |
| `AGENT_BROWSER_DEFAULT_TIMEOUT` | 默认操作超时（毫秒），默认值：25000 |

## 选择器 (Selectors)

### Refs（推荐用于 AI）

Refs 提供从快照中进行确定性元素选择的功能：

```bash
# 1. 获取带 refs 的快照
agent-browser snapshot
# 输出:
# - heading "Example Domain" [ref=e1] [level=1]
# - button "Submit" [ref=e2]
# - textbox "Email" [ref=e3]
# - link "Learn more" [ref=e4]

# 2. 使用 refs 进行交互
agent-browser click @e2                   # 点击按钮
agent-browser fill @e3 "test@example.com" # 填充输入框
agent-browser get text @e1                # 获取标题文本
agent-browser hover @e4                   # 悬停链接
```

**为什么使用 Refs？**

- **确定性 (Deterministic)**：Ref 精确指向快照中的特定元素
- **快速 (Fast)**：无需重新查询 DOM
- **对 AI 友好 (AI-friendly)**：快照 + ref 工作流最适合 LLM

### CSS 选择器

```bash
agent-browser click "#id"
agent-browser click ".class"
agent-browser click "div > button"
```

### 文本与 XPath

```bash
agent-browser click "text=Submit"
agent-browser click "xpath=//button"
```

### 语义定位器 (Semantic Locators)

```bash
agent-browser find role button click --name "Submit"
agent-browser find label "Email" fill "test@test.com"
```

## Agent 模式 (Agent Mode)

使用 `--json` 获取机器可读的输出：

```bash
agent-browser snapshot --json
# 返回: {"success":true,"data":{"snapshot":"...","refs":{"e1":{"role":"heading","name":"Title"},...}}}

agent-browser get text @e1 --json
agent-browser is visible @e2 --json
```

### AI 工作流最佳实践 (Optimal AI Workflow)

```bash
# 1. 导航并获取快照
agent-browser open example.com
agent-browser snapshot -i --json   # AI 解析树和 refs

# 2. AI 从快照中识别目标 refs
# 3. 使用 refs 执行操作
agent-browser click @e2
agent-browser fill @e3 "input text"

# 4. 若页面发生变化，获取新快照
agent-browser snapshot -i --json
```

### 命令链式调用 (Command Chaining)

命令可以通过 `&&` 在单次 shell 调用中链式执行。浏览器通过后台守护进程保持持久化，因此链式调用是安全的且更高效：

```bash
# 打开、等待加载完成并截图，一次调用完成
agent-browser open example.com && agent-browser wait --load networkidle && agent-browser snapshot -i

# 链式多次交互
agent-browser fill @e1 "user@example.com" && agent-browser fill @e2 "pass" && agent-browser click @e3

# 导航并截图
agent-browser open example.com && agent-browser wait --load networkidle && agent-browser screenshot page.png
```

当你不需要中间输出时使用 `&&`。当需要先解析输出时（例如先获取快照以发现 refs，再进行交互），请分开运行命令。

## 有头模式 (Headed Mode)

显示浏览器窗口以便调试：

```bash
agent-browser open example.com --headed
```

这会打开一个可见的浏览器窗口，而不是在无头模式下运行。

> **注意：** 浏览器扩展在有头和无头模式下均可工作（Chrome 的 `--headless=new`）。

## 认证会话 (Authenticated Sessions)

使用 `--headers` 为特定源设置 HTTP 请求头，无需登录流程即可实现认证：

```bash
# 请求头仅作用域于 api.example.com
agent-browser open api.example.com --headers '{"Authorization": "Bearer <token>"}'

# 对 api.example.com 的请求会包含认证头
agent-browser snapshot -i --json
agent-browser click @e2

# 导航到其他域名时——不会发送请求头（安全！）
agent-browser open other-site.com
```

这适用于：

- **跳过登录流程** - 通过请求头而非 UI 进行认证
- **切换用户** - 使用不同的认证令牌启动新会话
- **API 测试** - 直接访问受保护的端点
- **安全性** - 请求头作用域于源，不会泄露到其他域名

要为多个源设置请求头，请在每个 `open` 命令中配合使用 `--headers`：

```bash
agent-browser open api.example.com --headers '{"Authorization": "Bearer token1"}'
agent-browser open api.acme.com --headers '{"Authorization": "Bearer token2"}'
```

若要为所有域名设置全局请求头，请使用 `set headers`：

```bash
agent-browser set headers '{"X-Custom-Header": "value"}'
```

## 自定义浏览器可执行文件 (Custom Browser Executable)

使用自定义浏览器可执行文件替代内置的 Chromium。适用于以下场景：

- **Serverless 部署**：使用轻量级 Chromium 构建（如 `@sparticuz/chromium`，约 50MB vs ~684MB）
- **系统浏览器**：使用已安装的 Chrome/Chromium
- **自定义构建**：使用修改过的浏览器版本

### CLI 用法

```bash
# 通过标志位
agent-browser --executable-path /path/to/chromium open example.com

# 通过环境变量
AGENT_BROWSER_EXECUTABLE_PATH=/path/to/chromium agent-browser open example.com
```

### Serverless (Vercel)

在瞬态 Vercel Sandbox microVM 中运行 agent-browser + Chrome。无需外部服务器：

```typescript
import { Sandbox } from "@vercel/sandbox";

const sandbox = await Sandbox.create({ runtime: "node24" });
await sandbox.runCommand("agent-browser", ["open", "https://example.com"]);
const result = await sandbox.runCommand("agent-browser", ["screenshot", "--json"]);
await sandbox.stop();
```

参见 [environments example](examples/environments/) 获取包含 UI 和部署到 Vercel 按钮的完整演示。

### Serverless (AWS Lambda)

```typescript
import chromium from '@sparticuz/chromium';
import { execSync } from 'child_process';

export async function handler() {
  const executablePath = await chromium.executablePath();
  const result = execSync(
    `AGENT_BROWSER_EXECUTABLE_PATH=${executablePath} agent-browser open https://example.com && agent-browser snapshot -i --json`,
    { encoding: 'utf-8' }
  );
  return JSON.parse(result);
}
```

## 本地文件 (Local Files)

使用 `file://` URL 打开并与本地文件（PDF、HTML 等）交互：

```bash
# 启用文件访问（JavaScript 访问本地文件必需）
agent-browser --allow-file-access open file:///path/to/document.pdf
agent-browser --allow-file-access open file:///path/to/page.html

# 截取本地 PDF 的截图
agent-browser --allow-file-access open file:///Users/me/report.pdf
agent-browser screenshot report.png
```

`--allow-file-access` 标志会添加 Chromium 参数（`--allow-file-access-from-files`, `--allow-file-access`），允许 `file://` URL：

- 加载并渲染本地文件
- 通过 JavaScript (XHR, fetch) 访问其他本地文件
- 加载本地资源（图片、脚本、样式表）

**注意：** 此标志仅对 Chromium 有效。出于安全考虑，默认处于禁用状态。

## CDP 模式 (CDP Mode)

通过 Chrome DevTools Protocol 连接到现有浏览器：

```bash
# 启动 Chrome: google-chrome --remote-debugging-port=9222

# 连接一次后，后续命令无需再带 --cdp
agent-browser connect 9222
agent-browser snapshot
agent-browser tab
agent-browser close

# 或在每条命令中传递 --cdp
agent-browser --cdp 9222 snapshot

# 通过 WebSocket URL 连接到远程浏览器
agent-browser --cdp "wss://your-browser-service.com/cdp?token=..." snapshot
```

`--cdp` 标志接受以下任一参数：

- 端口号（例如 `9222`），用于本地连接 `http://localhost:{port}`
- 完整的 WebSocket URL（例如 `wss://...` 或 `ws://...`），用于远程浏览器服务

这支持控制：

- Electron 应用
- 启用远程调试的 Chrome/Chromium 实例
- WebView2 应用
- 任何暴露 CDP 端点的浏览器

### 自动连接 (Auto-Connect)

使用 `--auto-connect` 自动发现并连接到正在运行的 Chrome 实例，无需指定端口：

```bash
# 自动发现启用远程调试的 Chrome
agent-browser --auto-connect open example.com
agent-browser --auto-connect snapshot

# 或通过环境变量
AGENT_BROWSER_AUTO_CONNECT=1 agent-browser snapshot
```

自动连接通过以下方式发现 Chrome：

1. 从默认用户数据目录读取 Chrome 的 `DevToolsActivePort` 文件
2. 回退到探测常见调试端口（9222, 9229）
3. 若基于 HTTP 的发现（`/json/version`, `/json/list`）失败，则回退到直接 WebSocket 连接

这在以下场景非常有用：

- Chrome 144+ 通过 `chrome://inspect/#remote-debugging` 启用了远程调试（使用动态端口）
- 你希望零配置连接到现有浏览器
- 不想追踪 Chrome 正在使用的具体端口

## 流式传输 (Streaming / Browser Preview)

通过 WebSocket 流式传输浏览器视口，用于实时预览或“协同浏览”（人类可在一旁观看并与 AI Agent 交互）。

### 流式传输 (Streaming)

每个会话都会自动在 OS 分配的端口上启动一个 WebSocket 流服务器。使用 `stream status` 查看绑定端口和连接状态：

```bash
agent-browser stream status
```

若要绑定到特定端口，设置 `AGENT_BROWSER_STREAM_PORT`：

```bash
AGENT_BROWSER_STREAM_PORT=9223 agent-browser open example.com
```

你也可以在运行时通过 `stream enable`、`stream disable` 和 `stream status` 管理流式传输：

```bash
agent-browser stream enable --port 9223   # 在特定端口重新启用
agent-browser stream disable              # 停止该会话的流式传输
```

WebSocket 服务器负责流式传输浏览器视口并接受输入事件。

### WebSocket 协议 (Protocol)

连接到 `ws://localhost:9223` 以接收帧并发送输入：

**接收帧：**

```json
{
  "type": "frame",
  "data": "<base64-encoded-jpeg>",
  "metadata": {
    "deviceWidth": 1280,
    "deviceHeight": 720,
    "pageScaleFactor": 1,
    "offsetTop": 0,
    "scrollOffsetX": 0,
    "scrollOffsetY": 0
  }
}
```

**发送鼠标事件：**

```json
{
  "type": "input_mouse",
  "eventType": "mousePressed",
  "x": 100,
  "y": 200,
  "button": "left",
  "clickCount": 1
}
```

**发送键盘事件：**

```json
{
  "type": "input_keyboard",
  "eventType": "keyDown",
  "key": "Enter",
  "code": "Enter"
}
```

**发送触摸事件：**

```json
{
  "type": "input_touch",
  "eventType": "touchStart",
  "touchPoints": [{ "x": 100, "y": 200 }]
}
```

## 架构 (Architecture)

agent-browser 采用客户端-守护进程架构：

1. **Rust CLI** - 解析命令，与守护进程通信
2. **Rust Daemon** - 纯 Rust 实现的守护进程，直接使用 CDP，无需 Node.js

守护进程会在首次执行命令时自动启动，并在命令间保持持久化以实现快速后续操作。若要设置闲置超时后自动关闭守护进程，请设置 `AGENT_BROWSER_IDLE_TIMEOUT_MS`（毫秒值）。启用后，若在指定时间内未收到新命令，守护进程将关闭浏览器并退出。

**浏览器引擎：** 默认使用 Chrome（来自 Chrome for Testing）。通过 `--engine` 标志可在 `chrome` 和 `lightpanda` 之间切换。支持的浏览器：Chromium/Chrome（通过 CDP）和 Safari（通过 iOS 的 WebDriver）。

## 平台 (Platforms)

| Platform    | Binary      |
| ----------- | ----------- |
| macOS ARM64 | Native Rust |
| macOS x64   | Native Rust |
| Linux ARM64 | Native Rust |
| Linux x64   | Native Rust |
| Windows x64 | Native Rust |

## 与 AI Agent 配合使用 (Usage with AI Agents)

### 直接告知 Agent (Just ask the agent)

最简单的方法是直接告诉你的 Agent 如何使用它：

```
Use agent-browser to test the login flow. Run agent-browser --help to see available commands.
```

`--help` 输出非常全面，大多数 Agent 都能据此自行理解。

### AI 编程助手 (推荐) (AI Coding Assistants - recommended)

将技能添加到你的 AI 编程助手中以获取更丰富的上下文：

```bash
npx skills add vercel-labs/agent-browser
```

这适用于 Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot、Goose、OpenCode 和 Windsurf。技能会从仓库中拉取，因此会自动保持更新。请勿从 `node_modules` 复制 `SKILL.md`，否则内容会过时。

### Claude Code

作为 Claude Code 技能安装：

```bash
npx skills add vercel-labs/agent-browser
```

这会在 `.claude/skills/agent-browser/SKILL.md` 添加一个轻量级发现存根（Stub）。该存故意保持极简——它在运行时将 Claude Code 指向 `agent-browser skills get core` 以加载实际的工作流内容。这样指令始终与已安装的 CLI 版本匹配，避免在发布间隙过时。

### AGENTS.md / CLAUDE.md

为了获得更一致的结果，请将其添加到你的项目或全局说明文件中：

```markdown
## Browser Automation

Use `agent-browser` for web automation. Run `agent-browser --help` for all commands.

Core workflow:

1. `agent-browser open <url>` - Navigate to page
2. `agent-browser snapshot -i` - Get interactive elements with refs (@e1, @e2)
3. `agent-browser click @e1` / `fill @e2 "text"` - Interact using refs
4. Re-snapshot after page changes
```

## 集成 (Integrations)

### iOS Simulator

控制 iOS 模拟器中的真实 Mobile Safari，用于真实的移动端网页测试。需要 macOS 和 Xcode。

**设置：**

```bash
# 安装 Appium 和 XCUITest driver
npm install -g appium
appium driver install xcuitest
```

**用法：**

```bash
# 列出可用的 iOS 模拟器
agent-browser device list

# 在特定设备上启动 Safari
agent-browser -p ios --device "iPhone 16 Pro" open https://example.com

# 与桌面端相同的命令
agent-browser -p ios snapshot -i
agent-browser -p ios tap @e1
agent-browser -p ios fill @e2 "text"
agent-browser -p ios screenshot mobile.png

# 移动端专属命令
agent-browser -p ios swipe up
agent-browser -p ios swipe down 500

# 关闭会话
agent-browser -p ios close
```

或使用环境变量：

```bash
export AGENT_BROWSER_PROVIDER=ios
export AGENT_BROWSER_IOS_DEVICE="iPhone 16 Pro"
agent-browser open https://example.com
```

| Variable                   | Description                                     |
| -------------------------- | ----------------------------------------------- |
| `AGENT_BROWSER_PROVIDER`   | 设置为 `ios` 以启用 iOS 模式                 |
| `AGENT_BROWSER_IOS_DEVICE` | 设备名称（例如 "iPhone 16 Pro", "iPad Pro"） |
| `AGENT_BROWSER_IOS_UDID`   | 设备 UDID（替代设备名称）        |

**支持的设备：** Xcode 中所有可用的 iOS 模拟器（iPhone、iPad），以及真实 iOS 设备。

**注意：** iOS Provider 会启动模拟器、启动 Appium 并控制 Safari。首次启动约需 30-60 秒；后续命令速度很快。

#### 真机支持 (Real Device Support)

Appium 也支持通过 USB 连接的真实 iOS 设备。这需要额外的单次设置：

**1. 获取你的设备 UDID：**

```bash
xcrun xctrace list devices
# 或
system_profiler SPUSBDataType | grep -A 5 "iPhone\|iPad"
```

**2. 签名 WebDriverAgent（一次性）：**

```bash
# 打开 WebDriverAgent Xcode 项目
cd ~/.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent
open WebDriverAgent.xcodeproj
```

在 Xcode 中：

- 选择 `WebDriverAgentRunner` target
- 进入 Signing & Capabilities
- 选择你的 Team（需要 Apple Developer 账号，免费层级即可）
- 让 Xcode 自动管理签名

**3. 与 agent-browser 配合使用：**

```bash
# 通过 USB 连接设备后：
agent-browser -p ios --device "<DEVICE_UDID>" open https://example.com

# 或使用唯一设备名称
agent-browser -p ios --device "John's iPhone" open https://example.com
```

**真机注意事项：**

- 首次运行会将 WebDriverAgent 安装到设备上（可能需要点击 Trust 提示）
- 设备必须已解锁并通过 USB 连接
- 初始连接速度略慢于模拟器
- 针对真实 Safari 的性能和行为进行测试

### Browserless

[Browserless](https://browserless.io) 提供带有 Sessions API 的云浏览器基础设施。当在无法运行本地浏览器的环境中使用 agent-browser 时，可使用它。

要启用 Browserless，请使用 `-p` 标志：

```bash
export BROWSERLESS_API_KEY="your-api-token"
agent-browser -p browserless open https://example.com
```

或在 CI/脚本中使用环境变量：

```bash
export AGENT_BROWSER_PROVIDER=browserless
export BROWSERLESS_API_KEY="your-api-token"
agent-browser open https://example.com
```

可选的环境变量配置：

| Variable                   | Description                                      | Default                                 |
| -------------------------- | ------------------------------------------------ | --------------------------------------- |
| `BROWSERLESS_API_URL`      | 基础 API URL（用于自定义区域或自托管） | `https://production-sfo.browserless.io` |
| `BROWSERLESS_BROWSER_TYPE` | 要使用的浏览器类型 (chromium or chrome)      | chromium                                |
| `BROWSERLESS_TTL`          | 会话 TTL，单位毫秒                      | `300000`                                |
| `BROWSERLESS_STEALTH`      | 启用隐身模式 (`true`/`false`)             | `true`                                  |

启用后，agent-browser 会连接到 Browserless 云会话而非启动本地浏览器。所有命令用法完全相同。

你的 API Token 可在 [Browserless Dashboard](https://browserless.io) 获取。

### Browserbase

[Browserbase](https://browserbase.com) 提供远程浏览器基础设施，简化 Agentic Browsing Agent 的部署。当在无法运行本地浏览器的环境中使用 agent-browser CLI 时，可使用它。

要启用 Browserbase，请使用 `-p` 标志：

```bash
export BROWSERBASE_API_KEY="your-api-key"
agent-browser -p browserbase open https://example.com
```

或在 CI/脚本中使用环境变量：

```bash
export AGENT_BROWSER_PROVIDER=browserbase
export BROWSERBASE_API_KEY="your-api-key"
agent-browser open https://example.com
```

启用后，agent-browser 会连接到 Browserbase 会话而非启动本地浏览器。所有命令用法完全相同。

你的 API Key 可在 [Browserbase Dashboard](https://browserbase.com/overview) 获取。

### Browser Use

[Browser Use](https://browser-use.com) 为 AI Agent 提供云浏览器基础设施。当在无法运行本地浏览器的环境中使用 agent-browser（Serverless、CI/CD 等）时，可使用它。

要启用 Browser Use，请使用 `-p` 标志：

```bash
export BROWSER_USE_API_KEY="your-api-key"
agent-browser -p browseruse open https://example.com
```

或在 CI/脚本中使用环境变量：

```bash
export AGENT_BROWSER_PROVIDER=browseruse
export BROWSER_USE_API_KEY="your-api-key"
agent-browser open https://example.com
```

启用后，agent-browser 会连接到 Browser Use 云会话而非启动本地浏览器。所有命令用法完全相同。

你的 API Key 可在 [Browser Use Cloud Dashboard](https://cloud.browser-use.com/settings?tab=api-keys) 获取。提供免费额度用于起步，后续采用按量付费定价。

### Kernel

[Kernel](https://www.kernel.sh) 为 AI Agent 提供云浏览器基础设施，支持隐身模式和持久化 Profile 等功能。

要启用 Kernel，请使用 `-p` 标志：

```bash
export KERNEL_API_KEY="your-api-key"
agent-browser -p kernel open https://example.com
```

或在 CI/脚本中使用环境变量：

```bash
export AGENT_BROWSER_PROVIDER=kernel
export KERNEL_API_KEY="your-api-key"
agent-browser open https://example.com
```

可选的环境变量配置：

| Variable                 | Description                                                                      | Default |
| ------------------------ | -------------------------------------------------------------------------------- | ------- |
| `KERNEL_HEADLESS`        | 在无头模式下运行浏览器 (`true`/`false`)                                    | `true`  |
| `KERNEL_STEALTH`         | 启用隐身模式以避免被检测为机器人 (`true`/`false`)                      | `false` |
| `KERNEL_TIMEOUT_SECONDS` | 会话超时时间，单位秒                                                       | `300`   |
| `KERNEL_PROFILE_NAME`    | 浏览器 Profile 名称用于持久化 cookies/登录（若不存在则自动创建） | (none)  |

启用后，agent-browser 会连接到 Kernel 云会话而非启动本地浏览器。所有命令用法完全相同。

**Profile 持久化：** 当设置了 `KERNEL_PROFILE_NAME` 时，如果该 Profile 尚不存在会自动创建。Cookies、登录信息和会话数据会在浏览器会话结束时自动保存回该 Profile，以便在未来会话中复用。

你的 API Key 可在 [Kernel Dashboard](https://dashboard.onkernel.com) 获取。

### AgentCore

[AWS Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 提供带有 SigV4 认证的云浏览器会话。

要启用 AgentCore，请使用 `-p` 标志：

```bash
agent-browser -p agentcore open https://example.com
```

或在 CI/脚本中使用环境变量：

```bash
export AGENT_BROWSER_PROVIDER=agentcore
agent-browser open https://example.com
```

凭证会自动从环境变量（`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`）或 AWS CLI（`aws configure export-credentials`，支持 SSO、Profiles 和 IAM Roles）中解析。

可选的环境变量配置：

| Variable                   | Description                                                          | Default          |
| -------------------------- | -------------------------------------------------------------------- | ---------------- |
| `AGENTCORE_REGION`         | AgentCore 端点的 AWS Region                                | `us-east-1`      |
| `AGENTCORE_BROWSER_ID`     | 浏览器标识符                                                   | `aws.browser.v1` |
| `AGENTCORE_PROFILE_ID`     | 用于持久化状态（cookies, localStorage）的浏览器 Profile         | (none)           |
| `AGENTCORE_SESSION_TIMEOUT`| 会话超时时间，单位秒                                           | `3600`           |
| `AWS_PROFILE`              | 用于凭证解析的 AWS CLI Profile                            | `default`        |

**浏览器 Profiles：** 当设置了 `AGENTCORE_PROFILE_ID` 时，浏览器状态（cookies, localStorage）会在跨会话时自动持久化。

启用后，agent-browser 会连接到 AgentCore 云浏览器会话而非启动本地浏览器。所有命令用法完全相同。

## License

Apache-2.0