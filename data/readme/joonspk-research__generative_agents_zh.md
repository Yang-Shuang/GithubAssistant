# 生成式智能体：人类行为的交互式模拟 

<p align="center" width="100%">
<img src="cover.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>

本仓库配合我们的研究论文《[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)》。其中包含我们用于生成式智能体的核心仿真模块——即能够模拟逼真人类行为的计算代理，以及其游戏环境。下文将记录在本地机器上配置仿真环境的步骤，以及如何以演示动画形式回放仿真过程。

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Isabella_Rodriguez.png" alt="Generative Isabella">   环境配置 
要配置你的运行环境，需要生成一个包含你 OpenAI API Key（API密钥）的 `utils.py` 文件，并下载必要的依赖包。

### 步骤 1：生成 Utils 文件
在 `reverie/backend_server` 文件夹中（即 `reverie.py` 所在目录），创建一个名为 `utils.py` 的新文件，并将以下内容复制粘贴到该文件中：
```
# Copy and paste your OpenAI API Key
openai_api_key = "<Your OpenAI API>"
# Put your name
key_owner = "<Name>"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True
```
将 `<Your OpenAI API>` 替换为你的 OpenAI API Key，并将 `<Name>` 替换为你的姓名。
 
### 步骤 2：安装依赖包
安装 `requirements.txt` 文件中列出的所有依赖（强烈建议先按惯例配置虚拟环境 virtualenv）。关于 Python 版本的说明：我们在 Python 3.9.12 环境下测试过本系统。 

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Klaus_Mueller.png" alt="Generative Klaus">   运行仿真 
要启动新的仿真，你需要同时启动两个服务：环境服务器和智能体仿真服务器。

### 步骤 1：启动环境服务器
同样，该环境是基于 Django 项目实现的，因此你需要启动 Django 服务。首先在你的命令行中导航到 `environment/frontend_server`（即 `manage.py` 所在目录）。然后运行以下命令：

    python manage.py runserver

接着，在你常用的浏览器中访问 [http://localhost:8000/]。如果看到提示“Your environment server is up and running”，说明服务已正常运行。在仿真过程中请确保该服务器持续运行，因此请保持此命令行窗口打开！（注：建议使用 Chrome 或 Safari 浏览器。Firefox 可能会在前端显示一些渲染异常，但通常不会影响实际仿真。）

### 步骤 2：启动仿真服务器
打开另一个命令行窗口（第一步中的窗口应保持运行环境服务，无需关闭）。导航至 `reverie/backend_server` 并运行 `reverie.py`。

    python reverie.py
这将启动仿真服务器。命令行会出现提示：“Enter the name of the forked simulation: ”。若要启动包含 Isabella Rodriguez、Maria Lopez 和 Klaus Mueller 的 3 个智能体的仿真，请输入：
    
    base_the_ville_isabella_maria_klaus
随后会提示“Enter the name of the new simulation: ”。输入任意名称以标识当前仿真（例如暂且输入 "test-simulation"）。

    test-simulation
请保持仿真服务器运行。此时它将显示以下提示：“Enter option: ”

### 步骤 3：运行与保存仿真
在浏览器中访问 [http://localhost:8000/simulator_home]。你将看到 Smallville（小镇）的地图以及地图上活跃的智能体列表。你可以使用键盘方向键移动视角。请保持此标签页打开。要开始运行仿真，请在仿真服务器的命令行提示“Enter option”后输入以下命令：

    run <step-count>
注意，请将 `<step-count>` 替换为表示你想要模拟的游戏步数的整数。例如，若要模拟 100 个游戏步骤，请输入 `run 100`。游戏中的一个步骤代表现实中的 10 秒。


你的仿真应该已经开始运行，并在浏览器地图中看到智能体移动。仿真完成后，“Enter option”提示将再次出现。此时，你可以通过输入带有所需步数的 `run` 命令继续模拟更多步骤，或输入 `exit` 不保存直接退出，也可输入 `fin` 保存并退出。

下次运行仿真服务器时，可通过将你之前的仿真名称作为分支仿真（forked simulation）提供来访问已保存的仿真数据。这将允许你从断点处继续运行仿真。

### 步骤 4：回放仿真
只需保持环境服务器运行，并在浏览器中访问以下地址即可回放已运行的仿真：`http://localhost:8000/replay/<simulation-name>/<starting-time-step>`。请确保将 `<simulation-name>` 替换为你想回放的仿真名称，并将 `<starting-time-step>` 替换为开始回放的整数时间步。

例如，访问以下链接将启动一个预置的示例回放，从第 1 个时间步开始：  
[http://localhost:8000/replay/July1_the_ville_isabella_maria_klaus-step-3-20/1/]

### 步骤 5：演示仿真
你可能已经注意到，回放中的所有角色图像看起来都是一样的。需要说明的是，回放功能主要用于调试目的，并未优先优化仿真文件夹大小或视觉效果。若要使用合适的角色图像进行正式演示，你需要先对仿真数据进行压缩。为此，请使用文本编辑器打开 `reverie` 目录下的 `compress_sim_storage.py` 文件。然后执行其中的 `compress` 函数，并将目标仿真的名称作为输入参数传入。这样即可压缩仿真文件，使其准备好用于演示。

要开始演示，请在浏览器中访问以下地址：`http://localhost:8000/demo/<simulation-name>/<starting-time-step>/<simulation-speed>`。注意，其中的 `<simulation-name>` 和 `<starting-time-step>` 含义同上。`<simulation-speed>` 可用于控制演示速度，1 为最慢，5 为最快。例如，访问以下链接将以中等速度（3）从第 1 个时间步开始播放预置示例：  
[http://localhost:8000/demo/July1_the_ville_isabella_maria_klaus-step-3-20/1/3/]

### 提示
我们注意到，当达到 OpenAI API 的每小时调用限额时，API 可能会出现挂起（hang）情况。此时你可能需要重启仿真。目前建议你在运行过程中频繁保存仿真数据，以便在需要停止并重新运行时尽可能减少进度丢失。截至 2023 年初，运行这些仿真的成本可能相对较高，尤其是在环境中包含大量智能体时。

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Maria_Lopez.png" alt="Generative Maria">   仿真存储位置
你保存的所有仿真数据将位于 `environment/frontend_server/storage`，所有压缩后的演示文件将位于 `environment/frontend_server/compressed_storage`。 

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Sam_Moore.png" alt="Generative Sam">   自定义配置

有两种可选方式来定制你的仿真。 

### 编写与加载智能体历史数据
第一种是在仿真开始时用独特的历史数据初始化智能体。为此，你需要：1) 使用某个基础仿真启动项目；2) 编写并加载智能体历史数据。具体步骤如下：

#### 步骤 1：启动基础仿真 
仓库中提供了两个基础仿真：包含 25 个智能体的 `base_the_ville_n25`，以及包含 3 个智能体的 `base_the_ville_isabella_maria_klaus`。按照上述步骤操作至第二步即可加载其中一个基础仿真。 

#### 步骤 2：加载历史文件 
当提示“Enter option: ”时，你应通过以下命令加载智能体历史数据：

    call -- load history the_ville/<history_file_name>.csv
注意，请将 `<history_file_name>` 替换为现有历史文件的名称。仓库中提供了两个示例历史文件：`agent_history_init_n25.csv`（对应 `base_the_ville_n25`）和 `agent_history_init_n3.csv`（对应 `base_the_ville_isabella_maria_klaus`）。这些文件包含以分号分隔的每个智能体的记忆记录——加载它们会将记忆记录插入到智能体的记忆流中。

#### 步骤 3：进一步自定义配置 
若要编写自己的历史文件来自定义初始化，请将你的文件放置于以下文件夹：`environment/frontend_server/static_dirs/assets/the_ville`。自定义历史文件的列格式必须与包含的示例文件保持一致。因此，建议先复制仓库中已有的文件作为起点进行修改。

### 创建新的基础仿真
若需更深入的自定义，你需要编写自己的基础仿真文件。最直接的方法是复制现有的基础仿真文件夹，并根据需求重命名和编辑。如果你决定保持智能体名称不变，此过程会更简单。但如果你想更改名称或增加 Smallville 地图可容纳的智能体数量，可能需要直接使用 [Tiled](https://www.mapeditor.org/) 地图编辑器来修改地图文件。


## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Eddy_Lin.png" alt="Generative Eddy">   作者与引用 

**作者：** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein

如果你使用了本仓库中的代码或数据，请引用我们的论文。 
```
@inproceedings{Park2023GenerativeAgents,  
author = {Park, Joon Sung and O'Brien, Joseph C. and Cai, Carrie J. and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S.},  
title = {Generative Agents: Interactive Simulacra of Human Behavior},  
year = {2023},  
publisher = {Association for Computing Machinery},  
address = {New York, NY, USA},  
booktitle = {In the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)},  
keywords = {Human-AI interaction, agents, generative AI, large language models},  
location = {San Francisco, CA, USA},  
series = {UIST '23}
}
```

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Wolfgang_Schulz.png" alt="Generative Wolfgang">   致谢

我们鼓励大家支持为本项目设计游戏资产的三位杰出艺术家，尤其是如果你计划将此处包含的资产用于你自己的项目： 
* 背景美术：[PixyMoon (@_PixyMoon\_)](https://twitter.com/_PixyMoon_)
* 家具/室内设计：[LimeZu (@lime_px)](https://twitter.com/lime_px)
* 角色设计：[ぴぽ (@pipohi)](https://twitter.com/pipohi)

此外，感谢 Lindsay Popowski、Philip Guo、Michael Terry 以及高级行为科学研究中心（CASBS）社区的见解、讨论与支持。最后，Smallville 中出现的所有地点均灵感来源于 Joon 在本科和研究生时期常去的真实地点——他在此感谢多年来一直照顾和支持他的所有人。