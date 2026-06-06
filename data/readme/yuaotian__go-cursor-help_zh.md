# 🚀 Cursor 免费试用重置工具

<div align="center">

[![Release](https://img.shields.io/github/v/release/yuaotian/go-cursor-help?style=flat-square&logo=github&color=blue)](https://github.com/yuaotian/go-cursor-help/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square&logo=bookstack)](https://github.com/yuaotian/go-cursor-help/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/yuaotian/go-cursor-help?style=flat-square&logo=github)](https://github.com/yuaotian/go-cursor-help/stargazers)

[🌟 英文版](README.md) | [🌏 中文版](README_CN.md) | [🌏 日文版](README_JP.md)

<img src="/img/cursor.png" alt="Cursor Logo" width="120"/>

</div>

---

<div align="center">

<!-- 公告区域：展示 Codex 官方 API 套餐与购买入口 -->

## 📢 Codex 官方 API 套餐指南

| 套餐 | 每日限额 | 每周限额 | 每月限额 | 价格 |
|:---|:---:|:---:|:---:|---:|
| 周卡（86元促销） | 50 | 200 | - | $6 |
| 15天标准套餐 | 100 | 300 | 500 | $30 |
| 30天稳定套餐 | 200 | 500 | 1000 | $55 |
| 30天高级套餐 | 400 | 1000 | 2000 | $90 |

### 促销说明

- 专注于稳定与安心，而非昂贵。
- 直连官方 Codex API。
- 一个 Pro 账号对应一个住宅宽带 IP。
- 真金白银购买，非低质共享资源。
- 自测近半个月，整体体验优秀且稳定（已优化缓存）。
- 周卡价格：【$6】。单次使用成本约 `$6/200=$0.03`；每日限额 50，每周限额 200，倍率 1。
- 支持 GPT 模型系列，以及图像生成模型（`image-2`）。

**一个邮箱地址仅限购买一张周卡！**

**请勿尝试越狱、成人内容或逆向工程滥用。后端 AI 审计已启用，将直接拒绝。**

📢 **PS：如需更高额度、定制按需付费套餐或有特殊需求，请直接联系我。**

周卡订单页：https://pay.ldxp.cn/item/oq0epw

商店主页（更多套餐）：https://pay.ldxp.cn/shop/yuaotian

---
</div>

> ⚠️ **重要提示**
> 
> 该工具目前支持：
> - ✅ Windows：最新 2.x.x 版本（已支持）
> - ✅ Mac/Linux：最新 2.x.x 版本（已支持，欢迎反馈）
>
> 使用前请检查你的 Cursor 版本。

---

### 🚀 一键解决方案

<details open>
<summary><b>全球用户</b></summary>

**macOS**

```bash
curl -fsSL https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_mac_id_modifier.sh -o ./cursor_mac_id_modifier.sh && sudo bash ./cursor_mac_id_modifier.sh && rm ./cursor_mac_id_modifier.sh
```

**Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_linux_id_modifier.sh | sudo bash 
```

> **注意：** 脚本会尝试通过检查常见路径（`/usr/bin`、`/usr/local/bin`、`$HOME/.local/bin`、`/opt/cursor`、`/snap/bin`）、使用 `which cursor` 命令以及在 `/usr`、`/opt` 和 `$HOME/.local` 中搜索来定位你的 Cursor 安装位置。如果 Cursor 安装在其他位置或通过这些方法未找到，脚本可能会失败。请确保 Cursor 可通过上述标准路径之一或方法访问。

**Windows**

```powershell
irm https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1 | iex
```

**提示（Windows）：** 如果你怀疑缓存了旧版脚本（镜像/代理缓存），可追加时间戳查询参数以绕过缓存：

```powershell
irm "https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1?$(Get-Date -Format yyyyMMddHHmmss)" | iex
```



</details>


<details open>
<summary><b>中国用户（推荐）</b></summary>

**macOS**

```bash
curl -fsSL https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_mac_id_modifier.sh -o ./cursor_mac_id_modifier.sh && sudo bash ./cursor_mac_id_modifier.sh && rm ./cursor_mac_id_modifier.sh
```

**Linux**

```bash
curl -fsSL https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_linux_id_modifier.sh | sudo bash
```

**Windows**

```powershell
irm https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1 | iex
```

**提示（Windows）：** 如果镜像缓存了旧内容，可在 URL 末尾追加 `?$(Get-Date -Format yyyyMMddHHmmss)`：

```powershell
irm "https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1?$(Get-Date -Format yyyyMMddHHmmss)" | iex
```

</details>


<div align="center">
<img src="img/run_success.png" alt="Run Success" width="600"/>
</div>

<details open>
<summary><b>Windows 终端运行与配置</b></summary>

#### 如何在 Windows 中打开管理员终端：

##### 方法 1：使用 Win + X 快捷键
```md
1. 按下 Win + X 组合键
2. 从菜单中选择以下选项之一：
   - “Windows PowerShell (管理员)”
   - “Windows Terminal (管理员)”
   - “终端 (管理员)”
   （具体选项可能因 Windows 版本而异）
```

##### 方法 2：使用 Win + R 运行命令
```md
1. 按下 Win + R 组合键
2. 在“运行”对话框中输入 powershell 或 pwsh
3. 按 Ctrl + Shift + Enter 以管理员身份运行
   或在打开的窗口中键入：Start-Process pwsh -Verb RunAs
4. 在管理员终端中输入重置脚本：

irm https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1 | iex
```

增强版命令：
```powershell
irm https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1 | iex
```

##### 方法 3：使用搜索
>![Search PowerShell](img/pwsh_1.png)
>在搜索框中输入 pwsh，右键选择“以管理员身份运行”
>![Run as Administrator](img/pwsh_2.png)

在管理员终端中输入重置脚本：
```powershell
irm https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1 | iex
```

增强版命令：
```powershell
irm https://wget.la/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1 | iex
```

### 🔧 PowerShell 安装指南 

如果你的系统中未安装 PowerShell，可通过以下任一方式进行安装：

#### 方法 1：通过 Winget 安装（推荐）

1. 打开命令提示符或 PowerShell
2. 运行以下命令：
```powershell
winget install --id Microsoft.PowerShell --source winget
```

#### 方法 2：手动安装

1. 下载适合你系统的安装包：
   - [PowerShell-7.4.6-win-x64.msi](https://github.com/PowerShell/PowerShell/releases/download/v7.4.6/PowerShell-7.4.6-win-x64.msi)（64 位系统）
   - [PowerShell-7.4.6-win-x86.msi](https://github.com/PowerShell/PowerShell/releases/download/v7.4.6/PowerShell-7.4.6-win-x86.msi)（32 位系统）
   - [PowerShell-7.4.6-win-arm64.msi](https://github.com/PowerShell/PowerShell/releases/download/v7.4.6/PowerShell-7.4.6-win-arm64.msi)（ARM64 系统）

2. 双击下载的安装包并按照提示完成安装

> 💡 如遇任何问题，请参阅 [Microsoft 官方安装指南](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows)

</details>

#### Windows 安装特性:

- 🔍 自动检测并使用 PowerShell 7（如果可用）
- 🛡️ 通过 UAC 提示请求管理员权限
- 📝 若未找到 PS7，则回退至 Windows PowerShell
- 💡 若提权失败，提供手动操作指引

完成！该脚本将：

1. ✨ 自动安装工具
2. 🔄 立即重置你的 Cursor 试用期

### 📦 手动安装

> 从 [releases](https://github.com/yuaotian/go-cursor-help/releases/latest) 下载适合你系统的文件

<details>
<summary>Windows 安装包</summary>

- 64位：`cursor-id-modifier_windows_x64.exe`
- 32位：`cursor-id-modifier_windows_x86.exe`
</details>

<details>
<summary>macOS 安装包</summary>

- Intel：`cursor-id-modifier_darwin_x64_intel`
- M1/M2：`cursor-id-modifier_darwin_arm64_apple_silicon`
</details>

<details>
<summary>Linux 安装包</summary>

- 64位：`cursor-id-modifier_linux_x64`
- 32位：`cursor-id-modifier_linux_x86`
- ARM64：`cursor-id-modifier_linux_arm64`
</details>

### 🔧 技术细节

<details>
<summary><b>配置文件</b></summary>

程序会修改位于以下路径的 Cursor `storage.json` 配置文件：

- Windows：`%APPDATA%\Cursor\User\globalStorage\storage.json`
- macOS：`~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- Linux：`~/.config/Cursor/User/globalStorage/storage.json`
</details>

<details>
<summary><b>修改字段</b></summary>

该工具会为以下项生成全新的唯一标识符：

- `telemetry.machineId`
- `telemetry.macMachineId`
- `telemetry.devDeviceId`
- `telemetry.sqmId`
</details>

<details>
<summary><b>手动禁用自动更新</b></summary>

Windows 用户可手动禁用自动更新功能：

1. 关闭所有 Cursor 进程
2. 删除目录：`C:\Users\username\AppData\Local\cursor-updater`
3. 创建同名文件：`cursor-updater`（无扩展名）

macOS/Linux 用户可在系统中查找类似的 `cursor-updater` 目录并执行相同操作。

</details>

<details>
<summary><b>安全特性</b></summary>

- ✅ 安全的进程终止机制
- ✅ 原子化文件操作
- ✅ 错误处理与恢复机制
</details>

<details>
<summary><b>注册表修改说明</b></summary>

> ⚠️ **重要：该工具会修改 Windows 注册表**

#### 修改的注册表项
- 路径：`Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography`
- 键名：`MachineGuid`

#### 潜在影响
修改此注册表键可能影响：
- Windows 系统的唯一设备标识
- 部分软件的设备识别与授权状态
- 基于硬件标识的系统功能

#### 安全措施
1. 自动备份
   - 修改前会自动备份原始值
   - 备份位置：`%APPDATA%\Cursor\User\globalStorage\backups`
   - 备份文件格式：`MachineGuid.backup_YYYYMMDD_HHMMSS`

2. 手动恢复步骤
   - 打开注册表编辑器（regedit）
   - 导航至：`Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography`
   - 右键点击 `MachineGuid`
   - 选择“修改”
   - 粘贴备份文件中的值

#### 重要注意事项
- 修改前请验证备份文件是否存在
- 如需恢复原始值，请使用备份文件
- 修改注册表需要管理员权限
</details>

---

### 📚 推荐阅读

- [Cursor 问题合集与解决方案](https://mp.weixin.qq.com/s/pnJrH7Ifx4WZvseeP1fcEA)
- [AI 通用开发助手提示词指南](https://mp.weixin.qq.com/s/PRPz-qVkFJSgkuEKkTdzwg)

---

## 💬 反馈与建议

我们非常重视你对新增强脚本的反馈！如果你尝试过 `cursor_win_id_modifier.ps1` 脚本，欢迎分享你的体验：

- 🐛 **Bug 报告**：发现了任何问题？请告诉我们！
- 💡 **功能建议**：有改进想法吗？
- ⭐ **成功案例**：分享该工具如何帮助了你！
- 🔧 **技术反馈**：关于性能、兼容性或可用性的见解

你的反馈有助于我们持续改进工具。欢迎随时提交 Issue 或为项目贡献代码！

---

## 💰 支持

<div align="center">
<b>如果觉得有帮助，请考虑请我吃根辣条表示赞赏~ 💁☕️</b>
<table>
<tr>

<td align="center">
<b>微信赞赏</b><br>
<img src="img/wx_zsm2.png" width="500" alt="微信赞赏码"><br>
<small>要到饭咧？啊咧？啊咧？不给也没事~ 请随意打赏</small>
</td>
<td align="center">
<b>支付宝赞赏</b><br>
<img src="img/alipay.png" width="500" alt="支付宝赞赏码"><br>
<small>如果觉得有帮助,来包辣条犒劳一下吧~</small>
</td>
<td align="center">
<b>Alipay</b><br>
<img src="img/alipay_scan_pay.jpg" width="500" alt="Alipay"><br>
<em>1 根辣条 = 1 次 AI 思考周期</em>
</td>
<td align="center">
<b>WeChat</b><br>
<img src="img/qun-22.jpg" width="500" alt="WeChat"><br>
<em>二维码7天内(3月6日前)有效，过期请加微信或关注公众号「煎饼果子卷AI」</em>
</td>
<!-- <td align="center">
<b>ETC</b><br>
<img src="img/etc.png" width="100" alt="ETC Address"><br>
ETC: 0xa2745f4CD5d32310AC01694ABDB28bA32D125a6b
</td>
<td align="center"> -->
</td>
</tr>
</table>
</div>

### 💳 支付方式（捐赠 / 去广告）

- 🪙 **USDT (Tether)**
  - 🔴 TRC-20 (Tron): `TFbJnoY5Lep5ZrDwBbT8rV1i8xR4ZhX53k`
  - 🟡 Polygon / BSC / Arbitrum: `0x44f8925b9f93b3d6da8d5ad26a3516e3e652cc88`
- 🟦 **Litecoin (LTC)**: `LVrigKxtWfPymMRtRqL3z2eZxfncR3dPV7`

---

## ⭐ 项目统计

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=yuaotian/go-cursor-help&type=Date)](https://star-history.com/#yuaotian/go-cursor-help&Date)

![Repobeats analytics image](https://repobeats.axiom.co/api/embed/ddaa9df9a94b0029ec3fad399e1c1c4e75755477.svg "Repobeats analytics image")

</div>

## 📄 许可证

<details>
<summary><b>MIT 许可证</b></summary>

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

</details>