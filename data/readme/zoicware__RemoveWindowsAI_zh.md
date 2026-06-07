# 移除 Windows AI

## 为什么？

Windows 11 当前的 25H2 版本及后续构建版本将包含越来越多的 AI 功能和组件。本脚本旨在移除所有这些功能，以提升用户体验、隐私和安全性。 

<img width="150" alt="AI-Explorer-icon" src="https://github.com/zoicware/RemoveWindowsAI/assets/118035521/33efb033-c935-416c-977d-777bb69a3737">

----------------------



### 脚本功能

 - **禁用注册表项** 

   - 禁用 Copilot
   - 禁用 Recall（回顾功能）
   - 禁用输入洞察（Input Insights）及打字数据收集 
   - 禁用 Edge 中的 Copilot
   - 禁用画图应用中的 AI 实验计划
   - 移除 AI Fabric 服务
   - 禁用 AI 操作
   - 禁用语音访问
   - 禁用 AI 语音效果
   - 禁用设置搜索中的 AI
   - 禁用游戏 Copilot
   - 禁用所有 Office 应用中的 Copilot
   - 禁用照片应用中的 AI 功能
   - 禁用截图工具中的“点击即可操作”（Click to Do）

 - **防止 AI 包重新安装**

   - 安装自定义的 Windows 更新包，以防止 CBS（基于组件的服务）存储库中重新安装 AI 包 

 - **禁用 Copilot 策略** 

   - 在 `IntegratedServicesRegionPolicySet.json` 中禁用与 Copilot 和 Recall 相关的策略

 - **移除 AI AppX 包**

   - 移除所有 AI AppX 包，包括标记为 `Nonremovable`（不可卸载）的包以及 WindowsWorkload 

 - **移除 Recall 可选功能**

 - **移除 CBS 中的 AI 包**

   - 这将移除 CBS（基于组件的服务）存储库中隐藏和锁定的 AI 包 

 - **清理 AI 文件**

   - 执行全面系统清理，删除所有剩余的 AI 安装程序、注册表项和包文件 

 - **隐藏 AI 组件设置页**

   - 将隐藏设置页面中的 `AI Components`（AI 组件）选项卡 

 - **禁用记事本中的重写 AI 功能**

- **移除 Recall 任务**

   - 强制删除 Recall 计划任务的所有实例

  - **更新后清理检查**

     - 创建计划任务，用于检查是否已进行 Windows 更新。若已更新，则自动移除新安装的 AI 功能



 - #### 安装经典应用

   - 此选项允许你用经典版本替换当前充斥现代 AI 的应用程序
   - **可选项目：** 替换记事本、画图、截图工具、照片查看器，以及安装旧版照片应用（Photos Legacy） 

 

#### 手动禁用 AI

- 很遗憾，并非所有功能和设置都能通过脚本完全禁用。本指南将展示如何手动禁用其他 AI 功能。
> **[Disable Other AI Features](https://github.com/zoicware/RemoveWindowsAI/blob/main/OtherAIFeatures.md)**

  

### 查看脚本文档

  > **[Documentation](https://github.com/zoicware/RemoveWindowsAI/blob/main/Documentation.md)**



  > [!WARNING]
  > 部分第三方杀毒软件可能会误报该脚本为恶意程序。这显然是误报，你需要暂时禁用杀毒软件或将该脚本添加至白名单（排除项）。
  > 
  > 由于本脚本会对系统进行高级修改，许多系统精简工具/脚本都可能被误报为恶意程序……如果你对该脚本存疑，我始终建议先在虚拟机中测试任何软件。



---

 

 ### 使用方法

 

 #### 以管理员身份在 PowerShell 控制台中运行

 ---



 > [!WARNING]
 > 已不再支持使用 PowerShell 7 运行此脚本，这会导致问题。为避免此情况，请确保你正在使用的是 Windows PowerShell (5.1)。
 >



 ### 启动图形界面 (UI)

 ```PowerShell
 & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/zoicware/RemoveWindowsAI/main/RemoveWindowsAi.ps1")))
 ```

 ### 精简命令：

 ##### 链接已使用开源短链服务缩短：https://kutt.to/

 ```PowerShell
 & ([scriptblock]::Create((irm 'https://kutt.to/RWAI')))
 ```







 <details>  
  <summary>点击查看界面</summary>
  <img width="586" height="693" alt="Capture2" src="https://github.com/user-attachments/assets/fa105ba5-c1dc-447c-ae2e-7ee373291042" />
  <img width="586" height="693" alt="Capture2" src="https://github.com/user-attachments/assets/8a446a23-7c47-468e-856b-1e783205c511" />
</details>  



&nbsp;



### 命令行选项



**以非交互模式运行所有选项**

 ```PowerShell
 & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/zoicware/RemoveWindowsAI/main/RemoveWindowsAi.ps1"))) -nonInteractive -AllOptions
 ```



--- 



**使用特定参数运行的示例**

 ```PowerShell
 & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/zoicware/RemoveWindowsAI/main/RemoveWindowsAi.ps1"))) -nonInteractive -Options DisableRegKeys,RemoveAppxPackages,DisableCopilotPolicies 
 ```



**所有可用参数：**
```
DisableRegKeys           
PreventAIPackageReinstall     
DisableCopilotPolicies        
RemoveAppxPackages         
RemoveRecallFeature 
RemoveCBSPackages          
RemoveAIFiles                
HideAIComponents            

DisableRewrite      
RemoveRecallTasks

UpdateCleanupCheck
```



**运行安装经典应用**

 ```PowerShell
 & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/zoicware/RemoveWindowsAI/main/RemoveWindowsAi.ps1"))) -nonInteractive -InstallClassicApps photoviewer,mspaint,snippingtool,notepad  
 ```



**所有可用参数：**
```
photoviewer           
mspaint     
snippingtool       
notepad        
photoslegacy 
```





**启用备份模式运行**



> [!NOTE]
> 必须启用备份模式才能完全还原更改。
> 
 ```PowerShell
 & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/zoicware/RemoveWindowsAI/main/RemoveWindowsAi.ps1"))) -nonInteractive -backupMode -AllOptions
 ```



---



**还原更改**



 ```PowerShell
 & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/zoicware/RemoveWindowsAI/main/RemoveWindowsAi.ps1"))) -nonInteractive -revertMode -AllOptions
 ```



---



### 更新说明



鉴于微软持续更新并添加新的 AI 功能，本脚本将尽力保持与最新稳定版构建同步。



你可以在这里查看脚本的最新更新记录：
https://github.com/zoicware/RemoveWindowsAI/commits/main/



 > [!NOTE]  
> 任何仅添加到 Insider（预览版）构建的功能，在微软将其加入最新稳定版之前，不会收录到本脚本中。


 

> [!TIP]
> **提交 AI 功能**
> 
> 如果你发现某个 AI 功能或注册表项当前未被此脚本移除或禁用，请提交 Issue（问题反馈），并提供尽可能多的详细信息，我将把它添加到脚本中。





### 捐赠支持 



如果你想支持我的工作，欢迎考虑捐赠 :)



[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/zoicware)





### 加入 Discord 社区



[![Discord](https://discordapp.com/api/guilds/1173717737017716777/widget.png?style=banner1)](https://discord.gg/VsC7XS5vgA)





### YouTube 视频教程

#### [如何移除所有 Windows AI 功能](https://youtu.be/j5_eEBWGHFw)