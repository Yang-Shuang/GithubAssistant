# 基于 MCP 的对话机器人

(英文 | [中文](README_zh.md) | [日本語](README_ja.md))

## 简介

👉 [人类：给AI装上摄像头，AI秒知主人三天没洗头【bilibili】](https://www.bilibili.com/video/BV1bpjgzKEhd/)

👉 [亲手打造你的AI女友，新手入门指南【bilibili】](https://www.bilibili.com/video/BV1XnmFYLEJN/)

作为语音交互入口，小智（XiaoZhi）AI 对话机器人依托 Qwen / DeepSeek 等大模型的 AI 能力，并通过 MCP 协议实现多端控制。

<img src="docs/mcp-based-graph.jpg" alt="Control everything via MCP" width="320">

## 版本说明

当前 v2 版本与 v1 分区表（Partition Table）不兼容，因此无法通过 OTA 从 v1 升级至 v2。关于分区表的详细信息，请参阅 [partitions/v2/README.md](partitions/v2/README.md)。

所有运行 v1 版本的硬件均可通过手动烧录固件升级至 v2。

v1 的稳定版本为 1.9.2。你可以通过运行 `git checkout v1` 切换至 v1 分支。v1 分支将持续维护至 2026 年 2 月。

### 已实现的功能

- Wi-Fi / ML307 Cat.1 4G
- 离线语音唤醒 [ESP-SR](https://github.com/espressif/esp-sr)
- 支持两种通信协议（[Websocket](docs/websocket.md) 或 MQTT+UDP）
- 采用 OPUS 音频编解码器
- 基于流式 ASR + LLM + TTS 架构的语音交互
- 说话人识别（Speaker Recognition），可识别当前发言者 [3D Speaker](https://github.com/modelscope/3D-Speaker)
- OLED / LCD 显示屏，支持表情符号显示
- 电量显示与电源管理
- 多语言支持（中文、英文、日文）
- 支持 ESP32-C3、ESP32-S3、ESP32-P4 芯片平台
- 设备端 MCP，用于控制硬件（扬声器、LED、舵机、GPIO 等）
- 云端 MCP，扩展大模型能力（智能家居控制、电脑桌面操作、知识检索、邮件收发等）
- 支持自定义唤醒词、字体、表情符号及聊天背景，并提供在线网页编辑功能（[自定义资源生成器](https://github.com/78/xiaozhi-assets-generator)）

## 硬件支持

### 面包板 DIY 实践

请参阅飞书文档教程：

👉 [《小智 AI 对话机器人百科》](https://ccnphfhqs21z.feishu.cn/wiki/F5krwD16viZoF0kKkvDcrZNYnhb?from=from_copylink)

面包板演示：

![Breadboard Demo](docs/v1/wiring2.jpg)

### 支持 70+ 开源硬件（部分列表）

- <a href="https://oshwhub.com/li-chuang-kai-fa-ban/li-chuang-shi-zhan-pai-esp32-s3-kai-fa-ban" target="_blank" title="立创ESP32-S3开发板">立创ESP32-S3开发板</a>
- <a href="https://github.com/espressif/esp-box" target="_blank" title="乐鑫ESP32-S3-BOX3">乐鑫ESP32-S3-BOX3</a>
- <a href="https://docs.m5stack.com/zh_CN/core/CoreS3" target="_blank" title="M5Stack CoreS3">M5Stack CoreS3</a>
- <a href="https://docs.m5stack.com/en/atom/Atomic%20Echo%20Base" target="_blank" title="AtomS3R + Echo Base">M5Stack AtomS3R + Echo Base</a>
- <a href="https://gf.bilibili.com/item/detail/1108782064" target="_blank" title="妙控按钮 2.4">妙控按钮 2.4</a>
- <a href="https://www.waveshare.net/shop/ESP32-S3-Touch-AMOLED-1.8.htm" target="_blank" title="微雪ESP32-S3-Touch-AMOLED-1.8">微雪ESP32-S3-Touch-AMOLED-1.8</a>
- <a href="https://github.com/Xinyuan-LilyGO/T-Circle-S3" target="_blank" title="LILYGO T-Circle-S3">LILYGO T-Circle-S3</a>
- <a href="https://oshwhub.com/tenclass01/xmini_c3" target="_blank" title="小格Mini C3">小格Mini C3</a>
- <a href="https://oshwhub.com/movecall/cuican-ai-pendant-lights-up-y" target="_blank" title="翠灿AI吊坠">翠灿AI吊坠</a>
- <a href="https://github.com/WMnologo/xingzhi-ai" target="_blank" title="WMnologo-Xingzhi-1.54TFT">WMnologo-Xingzhi-1.54TFT</a>
- <a href="https://www.seeedstudio.com/SenseCAP-Watcher-W1-A-p-5979.html" target="_blank" title="SenseCAP Watcher">SenseCAP Watcher</a>
- <a href="https://www.bilibili.com/video/BV1BHJtz6E2S/" target="_blank" title="ESP-HI低成本机器狗">ESP-HI 低成本机器狗</a>

<div style="display: flex; justify-content: space-between;">
  <a href="docs/v1/lichuang-s3.jpg" target="_blank" title="立创ESP32-S3开发板">
    <img src="docs/v1/lichuang-s3.jpg" width="240" />
  </a>
  <a href="docs/v1/espbox3.jpg" target="_blank" title="乐鑫ESP32-S3-BOX3">
    <img src="docs/v1/espbox3.jpg" width="240" />
  </a>
  <a href="docs/v1/m5cores3.jpg" target="_blank" title="M5Stack CoreS3">
    <img src="docs/v1/m5cores3.jpg" width="240" />
  </a>
  <a href="docs/v1/atoms3r.jpg" target="_blank" title="AtomS3R + Echo Base">
    <img src="docs/v1/atoms3r.jpg" width="240" />
  </a>
  <a href="docs/v1/magiclick.jpg" target="_blank" title="妙控按钮 2.4">
    <img src="docs/v1/magiclick.jpg" width="240" />
  </a>
  <a href="docs/v1/waveshare.jpg" target="_blank" title="微雪ESP32-S3-Touch-AMOLED-1.8">
    <img src="docs/v1/waveshare.jpg" width="240" />
  </a>
  <a href="docs/v1/lilygo-t-circle-s3.jpg" target="_blank" title="LILYGO T-Circle-S3">
    <img src="docs/v1/lilygo-t-circle-s3.jpg" width="240" />
  </a>
  <a href="docs/v1/xmini-c3.jpg" target="_blank" title="小格Mini C3">
    <img src="docs/v1/xmini-c3.jpg" width="240" />
  </a>
  <a href="docs/v1/movecall-cuican-esp32s3.jpg" target="_blank" title="翠灿AI吊坠">
    <img src="docs/v1/movecall-cuican-esp32s3.jpg" width="240" />
  </a>
  <a href="docs/v1/wmnologo_xingzhi_1.54.jpg" target="_blank" title="WMnologo-Xingzhi-1.54TFT">
    <img src="docs/v1/wmnologo_xingzhi_1.54.jpg" width="240" />
  </a>
  <a href="docs/v1/sensecap_watcher.jpg" target="_blank" title="SenseCAP Watcher">
    <img src="docs/v1/sensecap_watcher.jpg" width="240" />
  </a>
  <a href="docs/v1/esp-hi.jpg" target="_blank" title="ESP-HI低成本机器狗">
    <img src="docs/v1/esp-hi.jpg" width="240" />
  </a>
</div>

## 软件与开发

### 固件烧录

对于新手，推荐使用无需配置开发环境即可直接烧录的固件。

该固件默认连接官方 [xiaozhi.me](https://xiaozhi.me) 服务器。个人用户可注册账号免费使用 Qwen 实时模型。

👉 [新手固件烧录指南](https://ccnphfhqs21z.feishu.cn/wiki/Zpz4wXBtdimBrLk25WdcXzxcnNS)

### 开发环境

- Cursor 或 VS Code
- 安装 ESP-IDF 插件，选择 SDK 版本 5.4 或以上
- 推荐使用 Linux 系统，编译速度更快且驱动问题更少
- 本项目采用 Google C++ 代码规范，提交代码时请确保符合规范

### 开发者文档

- [自定义硬件指南](docs/custom-board.md) - 了解如何为小智 AI 创建定制主板
- [MCP 协议物联网控制使用手册](docs/mcp-usage.md) - 学习如何通过 MCP 协议控制物联网设备
- [MCP 协议交互流程](docs/mcp-protocol.md) - 设备端 MCP 协议实现说明
- [MQTT + UDP 混合通信协议文档](docs/mqtt-udp.md)
- [WebSocket 通信协议详细文档](docs/websocket.md)

## 大模型配置

如果你已拥有小智 AI 对话机器人设备并连接至官方服务器，可登录 [xiaozhi.me](https://xiaozhi.me) 控制台进行配置。

👉 [后台操作视频教程（旧版界面）](https://www.bilibili.com/video/BV1jUCUY2EKM/)

## 相关开源项目

如需在个人电脑上部署服务端，请参考以下开源项目：

- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server) Python 服务端
- [joey-zhou/xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java) Java 服务端
- [AnimeAIChat/xiaozhi-server-go](https://github.com/AnimeAIChat/xiaozhi-server-go) Golang 服务端
- [hackers365/xiaozhi-esp32-server-golang](https://github.com/hackers365/xiaozhi-esp32-server-golang) Golang 服务端

其他使用小智通信协议的客户端项目：

- [huangjunsen0406/py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi) Python 客户端
- [TOM88812/xiaozhi-android-client](https://github.com/TOM88812/xiaozhi-android-client) Android 客户端
- [100askTeam/xiaozhi-linux](http://github.com/100askTeam/xiaozhi-linux) 100ask Linux 客户端
- [78/xiaozhi-sf32](https://github.com/78/xiaozhi-sf32) 四川芯科蓝牙芯片固件
- [QuecPython/solution-xiaozhiAI](https://github.com/QuecPython/solution-xiaozhiAI) 移远通信 QuecPython 固件

自定义资源工具：

- [78/xiaozhi-assets-generator](https://github.com/78/xiaozhi-assets-generator) 自定义资源生成器（唤醒词、字体、表情符号、背景）

## 关于本项目

这是一个开源的 ESP32 项目，采用 MIT 许可证发布。任何人都可免费使用，包括商业用途。

我们希望本项目能帮助大家了解 AI 硬件开发，并将快速发展的语言大模型应用于实体硬件设备中。

如果你有任何想法或建议，欢迎提交 Issue 或加入我们的 [Discord](https://discord.gg/C759fGMBcZ) / QQ 群：994694848

## Star 历史

<a href="https://star-history.com/#78/xiaozhi-esp32&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=78/xiaozhi-esp32&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=78/xiaozhi-esp32&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=78/xiaozhi-esp32&type=Date" />
 </picture>
</a>