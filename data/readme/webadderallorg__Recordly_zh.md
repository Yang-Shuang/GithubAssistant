[简体中文](README.zh-CN.md) | English

<p align="center">
  <img width="220" alt="Recordly Logo" src="https://github.com/user-attachments/assets/414b8838-6731-45d4-a815-6e3c0aa1fe52" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/macOS%20%7C%20Windows%20%7C%20Linux-111827?style=for-the-badge" alt="macOS Windows Linux" />
  <img src="https://img.shields.io/badge/open%20source-AGPL3.0-2563eb?style=for-the-badge" alt="AGPL 3.0 license" />
</p>

### 几分钟内制作精美的演示视频
[Recordly](https://www.recordly.dev) 是一款**开源的屏幕录制与编辑工具**，适用于制作**操作指南、演示视频、产品介绍**等。 
**接受 Pull Request。**

<img width="1280" height="720" alt="MP4 to GIF export (4)" src="https://github.com/user-attachments/assets/e6d68606-5fc0-4f70-99cd-7521982dc13b" />


---
### 社区支持
<a href="https://coderabbit.link/recordly"><img width="400" alt="CodeRabbit Typemark" src="https://github.com/user-attachments/assets/3926ecfd-8652-4f2d-8da8-ac7641017cf5" /></a>

---

## 什么是 Recordly？

Recordly 是一款桌面应用，内置动效演示工具，用于录制和编辑屏幕画面。无需将原始素材发送给设计师来添加缩放、光标美化或自定义背景，Recordly 免费在统一工作流中完成这些操作。

Recordly 支持以下平台：

- **macOS** 14.0+
- **Windows** 10 Build 19041+
- **Linux**（现代发行版）

平台说明：

- **macOS** 使用基于原生 ScreenCaptureKit 的录制辅助工具。
- **Windows** 在支持的版本上使用原生的 Windows Graphics Capture (WGC) 辅助工具，并支持原生 WASAPI 音频。
- **Linux** 通过 Electron 录制 API 进行捕获。目前 Linux 暂不支持隐藏系统光标。

---

# 核心功能

## 自动缩放、光标美化与自定义画框
Recordly 可基于操作活动自动生成缩放建议，平滑光标移动，添加动态效果，并将最终画面置于自定义画框中（支持壁纸、纯色、渐变、模糊、内边距和阴影）。

<p>
  <img src="./docs/media/feature1.gif" width="450" alt="Recordly cursor and zoom demo video">
</p>

## 动态摄像头气泡叠加层
可将摄像头画面作为悬浮气泡添加，支持预设或自定义坐标定位、镜像翻转、阴影与圆角控制，并可设置跟随缩放动态调整以保持视觉平衡。

<p>
  <img src="./docs/media/feature2.gif" width="450" alt="Recordly webcam overlay demo video">
</p>

## 专为演示设计的轨道编辑
使用拖拽式时间轴工具进行缩放、裁剪、变速区域划分、标注、额外音轨添加及智能裁切编辑。支持保存为 `.recordly` 项目文件并随时重新打开。

<p>
  <img width="450" alt="timeline editor" src="https://github.com/user-attachments/assets/3692bd8f-7b8d-4a93-b696-d17c828487ea" />
</p>

## 扩展与插件市场

Recordly 采用社区驱动的扩展系统。任何人都可以开发并发布新功能扩展，例如光标点击音效、设备外框、浏览器原型图、壁纸、渲染钩子（render hooks）、设置面板等。

前往 [Recordly 插件市场](https://marketplace.recordly.dev/extensions) 浏览并安装社区扩展。

---

## 完整功能列表

### 录制

- 录制整个屏幕或单个应用窗口
- 从录制界面直接进入编辑器
- 同时捕获麦克风音频与系统音频
- 在支持的平台上使用原生录制后端
- 支持从已保存的 `.recordly` 项目文件继续编辑
- 可在应用内打开已有录制片段或项目文件

### 时间轴与编辑

- 拖拽式时间轴编辑
- 裁剪多余片段
- 手动添加缩放区域
- 基于光标活动自动推荐缩放区域
- 添加加速与减速区域
- 添加文本、图片及图形标注
- 在时间轴上添加额外音轨
- 裁剪录制画面
- 保存并重新打开项目，完整保留编辑状态

### 光标控制

- 显示或隐藏渲染的光标叠加层
- 调整光标大小
- 光标平滑处理
- 光标动态模糊
- 光标点击弹跳效果
- 光标微摆动画
- 支持光标循环模式，实现无缝导出
- 为渲染叠加层提供 macOS 风格的光标素材

### 摄像头叠加层

- 启用或禁用摄像头画面叠加
- 上传、替换或删除摄像头画面
- 镜像翻转摄像头画面
- 尺寸控制
- 预设位置与自定义 X/Y 坐标定位
- 边距控制
- 圆角控制
- 阴影控制
- 可选的跟随缩放动态调整摄像头尺寸

### 画框样式与背景

- 内置壁纸
- 运行时自动扫描壁纸目录
- 自定义上传背景
- 纯色背景
- 渐变背景
- 画框内边距
- 圆角设置
- 背景模糊
- 投影阴影
- 最终画面比例预设

### 导出

- MP4 格式导出
- GIF 格式导出
- 选择导出画质
- 设置 GIF 帧率
- GIF 循环开关
- GIF 尺寸预设
- 画面比例与输出尺寸控制
- 在系统文件管理器中显示已导出文件

### 工作流与易用性

- 自定义键盘快捷键
- 应用内快捷键参考手册
- 编辑器内置反馈与问题提交链接
- 项目偏好设置持久化保存
- 导出后更快的预览恢复速度

---

# 截图

<p align="center">
  <img src="https://i.postimg.cc/8CrQtGJf/Screenshot-2026-04-30-at-5-11-52-pm.png" width="700" alt="Recordly recording interface screenshot">
</p>

<p align="center">
  <img src="https://i.postimg.cc/pLSMfrTM/Screenshot-2026-04-30-at-5-11-45-pm.png" width="700" alt="Recordly editor screenshot">
</p>

<p align="center">
  <img src="https://i.postimg.cc/Zn9VY6bg/Screenshot-2026-03-18-at-6-32-59-pm.png" width="700" alt="Recordly timeline screenshot">
</p>

---

# 安装指南

## 下载预构建版本

预构建版本发布页：

https://github.com/webadderallorg/Recordly/releases

---

## Arch Linux / Manjaro (通过 yay)

从 AUR 安装（[recordly-bin](https://aur.archlinux.org/packages/recordly-bin)）：

```bash
yay -S recordly-bin
```

PKGBUILD、桌面入口文件、版本同步及可选的**本地源码打包（local-from-source）**功能均托管在 **[recordly-aur](https://github.com/firtoz/recordly-aur)** 仓库中，以保持主仓库简洁。如需联系维护者或了解更新机制，请访问该仓库或 AUR 软件包页面。

---

## 从源码构建

### 环境依赖

**macOS：** Xcode 命令行工具（运行 `xcode-select --install`）。

**Linux (Ubuntu/Debian)：**

```bash
sudo apt install build-essential cmake libx11-dev libxtst-dev libxrandr-dev libxt-dev
```

**Windows：** Visual Studio 2022（或构建工具）并安装 C++ 工作负载及 CMake。

### 构建步骤

```bash
git clone https://github.com/webadderallorg/Recordly.git recordly
cd recordly
npm install
npm run dev
```

如需打包可执行文件：

```bash
npm run build
```

也可使用针对特定平台的构建命令：

- `npm run build:mac`
- `npm run build:win`
- `npm run build:linux`

---

## macOS：“应用无法打开”提示处理

本地构建的应用可能被 macOS 隔离。

使用以下命令移除隔离标记：

```bash
xattr -rd com.apple.quarantine /Applications/Recordly.app
```

---

# 系统要求

| Platform | Minimum version | Notes |
|---|---|---|
| **macOS** | macOS 14.0 (Sonoma) | 需此版本以支持 ScreenCaptureKit 音频与麦克风录制。 |
| **Windows** | Windows 10 20H1 (Build 19041, May 2020) | 需此版本以启用原生 WGC 辅助工具及最佳的光标隐藏效果。 |
| **Linux** | Any modern distro | 通过 Electron 捕获进行录制。系统音频通常需依赖 PipeWire。 |

> [!IMPORTANT]
> 在低于 19041 版本的 Windows 上，录制仍可通过备用捕获方式工作，但系统真实光标可能会显示在录制片段中。

---

# 使用指南

## 录制

1. 启动 Recordly。
2. 选择屏幕或窗口区域。
3. 配置麦克风与系统音频选项。
4. 开始录制。
5. 停止录制以进入编辑器界面。

## 编辑

在编辑器中，你可以：

- 添加裁剪、缩放、变速区域及标注
- 调整光标行为与预览音量
- 自定义画框样式（壁纸、颜色、渐变、模糊、内边距与圆角）
- 添加或调整摄像头叠加画面
- 添加额外音轨
- 裁剪画面并选择比例

随时将工作保存为 `.recordly` 项目文件。

## 导出

支持的导出格式包括：

- **MP4**：标准视频输出
- **GIF**：轻量级分享与循环动画

导出前可调整画质、GIF 帧率、循环开关及输出尺寸等格式专属设置。

---

# 限制说明

### 光标捕获

Recordly 会在录制片段上层渲染美化后的光标叠加层。平台级隐藏系统光标的行为仍依赖操作系统支持。

**macOS**
- ScreenCaptureKit 可干净地排除真实光标。

**Windows**
- 最佳效果需 Windows 10 构建版本 19041+ 及原生捕获辅助工具。
- 较旧版本将回退至 Electron 捕获，真实光标可能可见。

**Linux**
- Electron 桌面捕获目前不支持隐藏光标。
- 若同时启用渲染的光标叠加层，导出画面可能同时显示真实光标与美化光标。

### 系统音频

各平台对系统音频的支持情况如下：

**Windows**
- 原生 WASAPI 支持

**Linux**
- 通常需依赖 PipeWire

**macOS**
- 需 macOS 14.0+ 及基于 ScreenCaptureKit 的工作流

---

# 工作原理

Recordly 将平台特定的捕获层与渲染驱动的编辑器、导出管线相结合。

**录制（Capture）**
- Electron 负责协调录制流程与应用交互
- macOS 使用原生 ScreenCaptureKit 辅助工具
- Windows 在可用时使用原生的 WGC 辅助工具及音频辅助组件

**编辑（Editing）**
- 时间轴区域用于定义缩放、裁剪、变速、音轨叠加与标注
- 光标与摄像头样式在编辑器状态中应用

**渲染（Rendering）**
- 场景合成由 **PixiJS** 处理

**导出（Export）**
- 预览时使用的场景逻辑将直接渲染为导出的 MP4 或 GIF 文件

**项目（Projects）**
- `.recordly` 文件会保存源媒体路径与编辑器状态，以便后续重新打开继续编辑

---

# 贡献指南

欢迎任何形式的贡献。

尤其需要以下方面的帮助：

- Linux 平台的捕获机制与光标行为优化
- 导出性能与稳定性提升
- 界面交互（UI/UX）打磨
- 本地化工作
- 更多编辑器工具与工作流优化

请保持 Pull Request 聚焦单一功能，测试录制/编辑/导出流程，并避免引入无关的代码重构。

详细规范请参阅 `CONTRIBUTING.md`。

---

# 社区交流

Bug 反馈与功能建议：

https://github.com/webadderallorg/Recordly/issues

欢迎提交 Pull Request。

---

# 支持者名单

[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/webadderall)

- Tom Egan @tomegan on X
- Robin Ebers @robinebers on X
- Tadees
- buildwithfur
- piccinato
- Tobias
- Anonymous Supporter
- Tandava Appadoo
- Digitalfastmind
- Roberto Marcelino
- Tony
- Rajan RK
- Francesco
- Erwan
- Anonymous supporter

---

# 许可证

Recordly 采用 **AGPL 3.0** 开源许可证。

---

# 致谢与来源

## 鸣谢

Recordly 最初是 [OpenScreen](https://github.com/siddharthvaddem/openscreen) 的一个分支。此后超过 80% 的代码已完全重写并独立演进。
OpenScreen 的许多功能（例如其缩放动画）实际上是从 Recordly 早期版本反向移植而来的。

开发者：  
[@webadderall](https://x.com/webadderall)