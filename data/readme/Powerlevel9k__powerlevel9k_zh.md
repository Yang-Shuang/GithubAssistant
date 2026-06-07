## Powerlevel9k 已弃用且不再维护。请使用 [Powerlevel10k](https://github.com/romkatv/powerlevel10k)!
---
![](https://raw.githubusercontent.com/bhilburn/powerlevel9k-logo/master/logo-banner.png)
---
[![Build Status](https://travis-ci.org/bhilburn/powerlevel9k.svg?branch=master)](https://travis-ci.org/bhilburn/powerlevel9k)
[![Join the chat at https://gitter.im/bhilburn/powerlevel9k](https://badges.gitter.im/bhilburn/powerlevel9k.svg)](https://gitter.im/bhilburn/powerlevel9k?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Powerlevel9k 是一款基于 [Powerline Fonts](https://github.com/powerline/fonts) 的 ZSH 主题。它可与原生 ZSH 或各类 ZSH 框架（如 [Oh-My-Zsh](https://github.com/robbyrussell/oh-my-zsh)、[Prezto](https://github.com/sorin-ionescu/prezto)、[Antigen](https://github.com/zsh-users/antigen) 以及[众多其他框架](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions）配合使用。

让你的终端发挥更大价值。做个硬核玩家，在“截图你的桌面”帖子中惊艳所有人。使用 Powerlevel9k。

![](http://bhilburn.org/content/images/2015/01/pl9k-improved.png)

你可以在我们的 Wiki 中查看其他用户的配置：[展示你的配置](https://github.com/bhilburn/powerlevel9k/wiki/Show-Off-Your-Config)。

目前市面上已有不少 Powerline ZSH 主题。本主题的开发者专注于以下四个核心目标：

1. 为用户提供开箱即用的配置，无需任何额外设置即可直接使用。
2. 方便希望调整提示符(prompt)的用户进行自定义。
3. 提供实用的片段(segment)，你可以根据需要启用它们，让你的提示符更加高效有用。我们提供了从单元测试覆盖率到 AWS 实例等各种场景的提示符片段。
4. 尽可能优化代码的执行速度。流畅的终端才是快乐的终端。

Powerlevel9k 可用于打造既实用又美观的终端环境：

![](https://camo.githubusercontent.com/b5d7eb49a30bfe6bdb5706fa3c9be95fe8e5956e/687474703a2f2f67696679752e636f6d2f696d616765732f70396b6e65772e676966)

### 目录

1. [安装](#installation)
2. [自定义](#prompt-customization)
    1. [美化你的提示符](https://github.com/bhilburn/powerlevel9k/wiki/Stylizing-Your-Prompt)
    2. [自定义提示符片段](#customizing-prompt-segments)
    3. [可用的提示符片段](#available-prompt-segments)
3. [故障排除](https://github.com/bhilburn/powerlevel9k/wiki/Troubleshooting)

请务必也[查阅 Wiki](https://github.com/bhilburn/powerlevel9k/wiki)!

### 安装
从原生终端切换到 PL9k 终端需要两个步骤。完成后，你可以选择自定义你的提示符。

[安装说明](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions)

1. [安装 Powerlevel9k 主题](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#step-1-install-powerlevel9k)
2. [安装 Powerline 字体](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#step-2-install-a-powerline-font)

如果你喜欢默认设置，则无需进行任何额外配置。但如果你有兴趣，这里提供了丰富的片段自定义选项。

### 提示符自定义

请务必查看 Wiki 中关于其他自定义选项的页面，包括颜色和图标设置：[美化你的提示符](https://github.com/bhilburn/powerlevel9k/wiki/Stylizing-Your-Prompt)

#### 自定义提示符片段
自定义提示符非常简单！选择你想要显示的片段，然后通过以下变量将它们分配到左侧或右侧提示符中。将以下内容添加到你的 `~/.zshrc`：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_LEFT_PROMPT_ELEMENTS`|`(context dir vcs)`|左侧提示符的片段列表|
|`POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS`|`(status root_indicator background_jobs history time)`|右侧提示符的片段列表|

上表显示了默认值。因此，如果你想手动设置这些变量，只需将以下内容放入你的 `~/.zshrc`：
```zsh
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status root_indicator background_jobs history time)
```

#### 可用的提示符片段
当前可用的片段如下：

**系统状态片段：**
* [`background_jobs`](#background_jobs) - 后台任务指示器。
* [`battery`](#battery) - 当前电池状态。
* [`context`](#context) - 你的用户名和主机名，根据 `$USER` 和 SSH 状态进行条件显示。
* [`date`](#date) - 系统日期。
* [`dir`](#dir) - 当前工作目录。
* `dir_writable` - 如果你对当前文件夹没有写入权限，则显示锁图标。
* [`disk_usage`](#disk_usage) - 当前分区的磁盘使用情况。
* `history` - 当前行的命令编号。
* [`host`](#host) - 你的当前主机名。
* [`ip`](#ip) - 显示当前的 IP 地址。
* [`vpn_ip`](#vpn_ip) - 显示当前的 VPN IP 地址。
* [`public_ip`](#public_ip) - 显示你的公网 IP 地址。
* [`load`](#load) - 你机器的负载平均值。
* `os_icon` - 根据你的操作系统显示一个精美的小图标。
* `ram` - 显示可用内存(RAM)。
* `root_indicator` - 指示用户是否具有超级管理员权限。
* [`status`](#status) - 上一条命令的返回码。
* `swap` - 打印当前的交换空间大小。
* [`time`](#time) - 系统时间。
* [`user`](#user) - 你的当前用户名。
* [`vi_mode`](#vi_mode)- 提示符的 Vi 编辑模式 (NORMAL|INSERT)。
* `ssh` - 指示你是否处于 SSH 会话中。

**开发环境片段：**
* [`vcs`](#vcs) - 关于此 `git` 或 `hg` 仓库的信息（如果你当前位于某个仓库内）。

**语言片段：**
* **GoLang 片段：**
    * `go_version` - 显示当前的 GO 版本。
* **Javascript / Node.js 片段：**
    * `node_version` - 显示已安装的 Node.js 版本号。
    * [`nodeenv`](#nodeenv) - [nodeenv](https://github.com/ekalinin/nodeenv) 提示符，用于显示 node 版本和环境名称。
    * `nvm` - 如果当前激活的 Node 版本与 NVM 使用的版本不同，则显示该版本。
* **PHP 片段：**
    * `php_version` - 显示当前的 PHP 版本。
    * `laravel_version` - 显示当前的 Laravel 版本。
    * [`symfony2_tests`](#symfony2_tests) - 显示 Symfony2 的测试类与代码类的比例。
    * `symfony2_version` - 如果你位于 Symfony2 项目目录中，则显示当前 Symfony2 版本。
* **Python 片段：**
    * [`virtualenv`](#virtualenv) - 你的 Python [VirtualEnv](https://virtualenv.pypa.io/en/latest/)。
    * [`anaconda`](#anaconda) - 你当前的 [Anaconda](https://www.continuum.io/why-anaconda) 环境。
    * `pyenv` - 由 [`pyenv version`](https://github.com/yyuu/pyenv) 首单词报告的当前 Python 版本。注意：如果该单词为 _system_（即你正在使用系统自带的 Python），则该片段不会显示。
* **Ruby 片段：**
    * [`chruby`](#chruby) - 使用 `chruby` 的 Ruby 环境信息（如果有激活的环境）。
    * [`rbenv`](#rbenv) - 使用 `rbenv` 的 Ruby 环境信息（如果有激活的环境）。
    * [`rspec_stats`](#rspec_stats) - 显示 RSpec 的测试类与代码类的比例。
    * `rvm` - 使用 `$GEM_HOME` 和 `$MY_RUBY_HOME` 的 Ruby 环境信息（如果有激活的环境）。
* **Rust 片段：**
    * `rust_version` - 显示当前的 Rust 版本及[图标](https://www.rust-lang.org/logos/rust-logo-blk.svg)。
* **Swift 片段：**
    * `swift_version` - 显示已安装的 Swift 版本号。
* **Java 片段：**
    * `java_version` - 显示当前的 Java 版本。

**云服务片段：**
* **AWS 片段：**
    * [`aws`](#aws) - 当前激活的 AWS profile（如果存在）。
    * `aws_eb_env` - 当前的 Elastic Beanstalk Environment。
* `docker_machine` - 当前的 Docker Machine。
* `kubecontext` - 你 `kubectl` 配置的当前上下文。
* `dropbox` - 使用 `dropbox-cli` 指示 Dropbox 目录及同步状态。

**其他：**
* [`custom_command`](#custom_command) - 创建一个自定义片段，用于显示任意命令的输出结果。
* [`command_execution_time`](#command_execution_time) - 显示当前命令的执行耗时。
* [`todo`](http://todotxt.com/) - 显示你 todo.txt 任务文件中的任务数量。
* `detect_virt` - 使用 systemd 进行虚拟化检测。
* `newline` - 将提示符换行继续显示。
* `openfoam` - 显示当前已加载的 [OpenFOAM](https://openfoam.org/) 环境。

---------------------------------------------------------------------------------


##### anaconda

此片段显示你当前激活的 Anaconda 环境。它依赖于环境变量 `CONDA_ENV_PATH` 或 `CONDA_PREFIX`（取决于 `conda` 版本）的设置，这会在你正确执行 `source activate` 时自动完成。

特殊配置变量：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_ANACONDA_LEFT_DELIMITER`|"("|环境名称左侧的分隔符。|
|`POWERLEVEL9K_ANACONDA_RIGHT_DELIMITER`|")"|环境名称右侧的分隔符。|

此外，你还可以使用以下片段特定参数进行自定义：`POWERLEVEL9K_PYTHON_ICON`、`POWERLEVEL9K_ANACONDA_BACKGROUND` 和 `POWERLEVEL9K_ANACONDA_FOREGROUND`。

##### aws

如果你想显示[当前的 AWS profile](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)，请将 `aws` 片段添加到提示符中，并在你的 `~/.zshrc` 中定义 `AWS_DEFAULT_PROFILE`：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`AWS_DEFAULT_PROFILE`|None|你的 AWS profile 名称|

##### background_jobs

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_BACKGROUND_JOBS_VERBOSE`|`true`|如果存在多个后台任务，此片段将显示任务数量。将其设置为 `false` 可关闭此功能。|
|`POWERLEVEL9K_BACKGROUND_JOBS_VERBOSE_ALWAYS`|`false`|始终显示任务计数（即使为 0）。|

##### battery

该片段的默认设置会显示你当前的电池状态（在无电池的系统上会优雅降级）。它支持 OSX 和 Linux（注意：Linux 需要安装 `acpi`）。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_BATTERY_CHARGING`|`"yellow"`|指示充电中的颜色。|
|`POWERLEVEL9K_BATTERY_CHARGED`|`"green"`|指示已充满电的颜色。|
|`POWERLEVEL9K_BATTERY_DISCONNECTED`|$DEFAULT_COLOR|指示无电池的状态颜色。|
|`POWERLEVEL9K_BATTERY_LOW_THRESHOLD`|`10`|判定电池电量危急的阈值（百分比）。|
|`POWERLEVEL9K_BATTERY_LOW_COLOR`|`"red"`|指示极低电量的颜色。|
|`POWERLEVEL9K_BATTERY_VERBOSE`|`true`|在电池电量旁显示剩余时间。|
|`POWERLEVEL9K_BATTERY_HIDE_ABOVE_THRESHOLD`|`unset`|超过此阈值时不显示电池片段。|

注意：你可以[修改 `_FOREGROUND` 颜色](https://github.com/bhilburn/powerlevel9k/wiki/Stylizing-Your-Prompt#segment-color-customization)，而不会影响图标本身的颜色。

你还可以根据电量自动更改电池图标，这将覆盖默认电池图标。为此，你需要定义 `POWERLEVEL9K_BATTERY_STAGES` 变量。

| Variable                      | Default Value | Description                                                   |
|-------------------------------|---------------|---------------------------------------------------------------|
| `POWERLEVEL9K_BATTERY_STAGES` | Unset         | 字符串或数组，每个索引对应一个电量等级。                        |

Powerlevel9k 将使用字符串或数组的每个索引作为阶段来指示电池电量，从左到右递增。你可以提供任意数量的阶段。例如，下面的设置为 Powerlevel9k 提供了 8 个阶段：
```zsh
POWERLEVEL9K_BATTERY_STAGES="▁▂▃▄▅▆▇█"
```

如果你需要在图标后添加额外间距，则必须将其设置为数组，因为字符串中的空格会被视为一个阶段，导致缺少图标。为此，请按如下方式声明变量：
```zsh
POWERLEVEL9K_BATTERY_STAGES=($'\u2581 ' $'\u2582 ' $'\u2583 ' $'\u2584 ' $'\u2585 ' $'\u2586 ' $'\u2587 ' $'\u2588 ')
```

使用数组语法，你可以创建由多个字符组成的阶段。下面的设置提供了 40 个电池阶段。
```zsh
POWERLEVEL9K_BATTERY_STAGES=(
   $'▏    ▏' $'▎    ▏' $'▍    ▏' $'▌    ▏' $'▋    ▏' $'▊    ▏' $'▉    ▏' $'█    ▏'
   $'█▏   ▏' $'█▎   ▏' $'█▍   ▏' $'█▌   ▏' $'█▋   ▏' $'█▊   ▏' $'█▉   ▏' $'██   ▏'
   $'██   ▏' $'██▎  ▏' $'██▍  ▏' $'██▌  ▏' $'██▋  ▏' $'██▊  ▏' $'██▉  ▏' $'███  ▏'
   $'███  ▏' $'███▎ ▏' $'███▍ ▏' $'███▌ ▏' $'███▋ ▏' $'███▊ ▏' $'███▉ ▏' $'████ ▏'
   $'████ ▏' $'████▎▏' $'████▍▏' $'████▌▏' $'████▋▏' $'████▊▏' $'████▉▏' $'█████▏' )
```

你还可以根据电量自动更改片段的背景色。这将覆盖以下变量：`POWERLEVEL9K_BATTERY_CHARGING`、`POWERLEVEL9K_BATTERY_CHARGED`、`POWERLEVEL9K_BATTERY_DISCONNECTED` 和 `POWERLEVEL9K_BATTERY_LOW_COLOR`。为此，请定义一个从低到高的颜色数组，如下所示：
```zsh
POWERLEVEL9K_BATTERY_LEVEL_BACKGROUND=(red1 orangered1 darkorange orange1 gold1 yellow1 yellow2 greenyellow chartreuse1 chartreuse2 green1)
```

与电池阶段类似，你可以使用任意数量的颜色，Powerlevel9k 会自动按顺序应用它们。

一些示例设置：

| Brightness     | Possible Array                                                                                                |
|----------------|---------------------------------------------------------------------------------------------------------------|
| Bright Colors  | `(red1 orangered1 darkorange orange1 gold1 yellow1 yellow2 greenyellow chartreuse1 chartreuse2 green1)`       |
| Normal Colors  | `(red3 darkorange3 darkgoldenrod gold3 yellow3 chartreuse2 mediumspringgreen green3 green3 green4 darkgreen)` |
| Subdued Colors | `(darkred orange4 yellow4 yellow4 chartreuse3 green3 green4 darkgreen)`                                       |

##### chruby

此片段显示在使用 `chruby` 切换当前 Ruby 环境时所使用的 Ruby 版本。

它使用由 `chruby` 设置的 `$RUBY_ENGINE` 和 `$RUBY_VERSION`。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_CHRUBY_SHOW_ENGINE`|true|显示当前选定的 Ruby 引擎（例如 `ruby`、`jruby`、`rbx` 等）。|
|`POWERLEVEL9K_CHRUBY_SHOW_VERSION`|true|显示当前选定引擎的版本号（例如 `2.5.1`）|

##### command_execution_time

如果上一条命令的执行时间超过 `POWERLEVEL9K_COMMAND_EXECUTION_TIME_THRESHOLD`，则显示其耗时。时间格式为“人类可读”，会根据执行时长自动缩放单位。如果你需要更高精度，只需设置 `POWERLEVEL9K_COMMAND_EXECUTION_TIME_PRECISION` 字段即可。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_COMMAND_EXECUTION_TIME_THRESHOLD`|3|显示此片段的阈值（秒）。可设置为 `0` 以始终显示。|
|`POWERLEVEL9K_COMMAND_EXECUTION_TIME_PRECISION`|2|时间值小数部分使用的位数。|

##### custom_command

`custom_...` 片段允许你将自定义命令的输出转换为提示符片段。例如，如果你想创建一个显示 WiFi 信号强度的自定义片段，你可以定义一个名为 `custom_wifi_signal` 的片段，如下所示：
```zsh
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(context time battery dir vcs virtualenv custom_wifi_signal)
POWERLEVEL9K_CUSTOM_WIFI_SIGNAL="echo signal: \$(nmcli device wifi | grep yes | awk '{print \$8}')"
POWERLEVEL9K_CUSTOM_WIFI_SIGNAL_BACKGROUND="blue"
POWERLEVEL9K_CUSTOM_WIFI_SIGNAL_FOREGROUND="yellow"
```
如果你更喜欢，也可以在 `.zshrc` 中定义函数，而不是像上面那样直接写在变量导出中。只需别忘了在片段中调用你的函数即可！实现相同效果的示例代码：
```zsh
zsh_wifi_signal(){
    local signal=$(nmcli device wifi | grep yes | awk '{print $8}')
    local color='%F{yellow}'
    [[ $signal -gt 75 ]] && color='%F{green}'
    [[ $signal -lt 50 ]] && color='%F{red}'
    echo -n "%{$color%}\uf230  $signal%{%f%}" # \uf230 is 
}

POWERLEVEL9K_CUSTOM_WIFI_SIGNAL="zsh_wifi_signal"
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(context time battery dir vcs virtualenv custom_wifi_signal)
```
上面的命令会生成如下所示的无线信号片段：

![signal](http://i.imgur.com/hviMATC.png)

你可以定义任意数量的自定义片段。如果你认为你的片段对其他人也有用，请考虑将其贡献到主主题仓库中，以便大家都能使用！

##### context

`context` 片段（user@host 字符串）是条件显示的。默认情况下，仅当你不是“普通”用户（包括 root），或你通过 SSH 连接到远程主机时才会显示。`SUDO` 和 `REMOTE_SUDO` 状态也可用于指示当前用户或远程用户是否具有超级管理员权限。

要使用此功能，请确保提示符元素中已启用 `context` 片段（默认已启用），并在你的 `~/.zshrc` 中定义 `DEFAULT_USER`。

你可以自定义 `context` 片段。例如，你可以通过设置以下变量使其显示完整主机名：
```
POWERLEVEL9K_CONTEXT_TEMPLATE="%n@`hostname -f`"
```

你可以设置 `POWERLEVEL9K_CONTEXT_HOST_DEPTH` 变量来更改主机名的显示方式。详见 [ZSH Manual](http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html#Login-information)。默认设置为 `%m`，将显示第一个 `.` 之前的主机名部分。你可以将其设置为 `%{N}m`（其中 N 为整数），以显示系统主机名的前 N 个段。将 N 设置为负数将从主机名末尾开始显示指定数量的段。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`DEFAULT_USER`|None|视为“默认上下文”的用户名（你也可以设置 `$USER`）。|
|`POWERLEVEL9K_ALWAYS_SHOW_CONTEXT`|false|始终显示此片段，包括 $USER 和主机名。|
|`POWERLEVEL9K_ALWAYS_SHOW_USER`|false|始终显示用户名，但主机名仍按条件显示。|
|`POWERLEVEL9K_CONTEXT_TEMPLATE`|%n@%m|默认上下文提示符（username@machine）。有关所有可能的扩展（包括更深层的主机深度），请参阅 [ZSH Documentation](http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html)。|

此片段具有不同的状态，可能有助于你直观地查看你的不同权限。阅读更多关于使用状态进行样式设置的[说明](https://github.com/bhilburn/powerlevel9k/wiki/Stylizing-Your-Prompt#special-segment-colors)。

| State         | Meaning                                                  |
|---------------|----------------------------------------------------------|
| `DEFAULT`     | 你是普通用户                                             |
| `ROOT`        | 你是 root 用户                                           |
| `SUDO`        | 你正在使用提权（sudo）                                   |
| `REMOTE_SUDO` | 你通过 SSH 连接到机器并拥有提权权限                      |
| `REMOTE`      | 你通过 SSH 连接到机器                                    |

##### date

`date` 片段显示当前系统日期。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_DATE_FORMAT`|`%D{%d.%m.%y}`|[ZSH 时间格式](http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html#Date-and-time)，用于此片段。|

##### dir

`dir` 片段显示当前工作目录。当使用“Awesome Powerline”字体时，还会额外显示一些图标：

| `Compatible` | `Powerline` | `Awesome Powerline` | Situation
|------------|-----------|-------------------|----------------------------
| None       | None      | ![](https://cloud.githubusercontent.com/assets/1544760/12183451/40ec4016-b58f-11e5-9b9e-74e2b2f0b8b3.png) | 位于主目录根路径         |
| None       | None      | ![](https://cloud.githubusercontent.com/assets/1544760/12369315/8a5d762c-bbf5-11e5-8a20-ca1179f48d6c.png) | 位于主目录的子文件夹中     |
| None       | None      | ![](https://cloud.githubusercontent.com/assets/1544760/12183452/40f79286-b58f-11e5-9b8c-ed1343a07b08.png) | 位于主目录之外           |
| None       | None      | ⚙ | 位于 `/etc` 目录中         |

要关闭这些图标，你可以将这些变量设置为空字符串。
```zsh
POWERLEVEL9K_HOME_ICON=''
POWERLEVEL9K_HOME_SUB_ICON=''
POWERLEVEL9K_FOLDER_ICON=''
POWERLEVEL9K_ETC_ICON=''
```
你可以通过截断长路径来限制输出长度。可用的自定义项如下：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_DIR_PATH_ABSOLUTE`|None|如果设置为 `true`，将使用绝对路径而不是主目录缩写 `~`|
|`POWERLEVEL9K_SHORTEN_DIR_LENGTH`|`2`|如果你的缩短策略是整目录截断，此字段决定末尾保留多少级目录。如果是按字符数截断，则决定每个目录字符串允许的最大字符数。|
|`POWERLEVEL9K_SHORTEN_STRATEGY`|None|目录字符串的截断方式。详见下表。|
|`POWERLEVEL9K_SHORTEN_DELIMITER`|`..`|截断字符串中使用的分隔符。可以是任意字符串，如果希望没有分隔符可设为空字符串。|

| Strategy Name | Description |
|---------------|-------------|
|Default|从左侧截断整级目录。数量由 `POWERLEVEL9K_SHORTEN_DIR_LENGTH` 定义。|
|`truncate_absolute_chars`|从左侧截断固定数量的字符，使得路径显示的总字符数（含或不含 `POWERLEVEL9K_SHORTEN_DELIMITER`）不超过 `POWERLEVEL9K_SHORTEN_DIR_LENGTH` + `POWERLEVEL9K_SHORTEN_DELIMITER` 的长度。|
|`truncate_middle`|截断路径中间部分。例如你位于 `~/MySuperProjects/AwesomeFiles/BoringOffice`，如果设置了 `POWERLEVEL9K_SHORTEN_DIR_LENGTH=3`（控制保留的字符数），则会被截断为 `~/MyS..cts/Awe..les/BoringOffice`。|
|`truncate_from_right`|仅保留文件夹名称开头部分不变。例如你的路径将被截断为：`/ro../Pr../office`。保留多少字符由 `POWERLEVEL9K_SHORTEN_DIR_LENGTH` 控制。|
|`truncate_absolute`|除路径末尾的少数几个字符外，其余全部截断。例如你位于 `~/Projects/powerlevel9k` 且设置了 `POWERLEVEL9K_SHORTEN_DIR_LENGTH=3`，将显示为 `..l9k`。|
|`truncate_to_last`|截断路径中最后一个文件夹之前的所有内容。|
|`truncate_to_first_and_last`|从路径中截断中间的目录。保留多少级由 `POWERLEVEL9K_SHORTEN_DIR_LENGTH` 控制。例如你位于 `~/Projects/powerlevel9k` 且设置了 `POWERLEVEL9K_SHORTEN_DIR_LENGTH=1`，将显示为 `~/../powerlevel9k`。|
|`truncate_to_unique`|解析所有父路径组件并将其截断至最短的唯一长度。复制粘贴结果到 Shell 后按 `TAB`，应能无歧义地展开回原始路径。|
|`truncate_with_package_name`|搜索 `package.json` 或 `composer.json`，并打印其中的 `name` 字段以缩写目录路径。优先级和文件可通过 `POWERLEVEL9K_DIR_PACKAGE_FILES=(package.json composer.json)` 设置。如果你已安装 [jq](https://stedolan.github.io/jq/)，将显著提升此策略的速度。|
|`truncate_with_folder_marker`|搜索由 `POWERLEVEL9K_SHORTEN_FOLDER_MARKER` 指定的文件，并截断其之前的所有内容（如果找到则停止，否则在 $HOME 和 ROOT 处停止）。|

例如，如果你想要类似 `fish` shell 的截断行为（将 `/usr/share/plasma` 截断为 `/u/s/plasma`），请使用以下内容：
```zsh
POWERLEVEL9K_SHORTEN_DIR_LENGTH=1
POWERLEVEL9K_SHORTEN_DELIMITER=""
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_from_right"
```
每种情况下，你都必须指定希望将目录缩短到的长度。因此，在某些情况下 `POWERLEVEL9K_SHORTEN_DIR_LENGTH` 表示字符数，在其他情况下则表示整级目录数。

`truncate_with_package_name` 策略会显示相对于项目根目录的路径。例如，如果你在 `$HOME/projects/my-project` 下有一个包含如下内容 `package.json` 的项目：
```json
{
  "name": "my-cool-project"
}
```
显示的路径将是 `my-cool-project`。如果你导航到 `$HOME/projects/my-project/src`，则路径将显示为 `my-cool-project/src`。请注意，目前此功能会查找 `.git` 目录来确定项目根目录。

如果你想自定义目录分隔符，可以设置：
```zsh
# 注意这里的双引号很重要！
POWERLEVEL9K_DIR_PATH_SEPARATOR="%F{red} $(print_icon 'LEFT_SUBSEGMENT_SEPARATOR') %F{black}"
```
如果要省略第一个字符（通常是斜杠，当你设置 `POWERLEVEL9K_DIR_PATH_SEPARATOR` 时它会被替换），可以设置 `POWERLEVEL9K_DIR_OMIT_FIRST_CHARACTER=true`。

当你在 `$HOME` 下时，你也可以自定义开头的波浪号：
```zsh
# 注意这里的双引号很重要！
POWERLEVEL9K_HOME_FOLDER_ABBREVIATION="%F{red} $(print_icon 'HOME_ICON') %F{black}"
```

你还可以使用以下变量配置 `dir` 片段在你处于无写入权限的目录时显示：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_DIR_SHOW_WRITABLE`|`false`|如果设置为 `true`，且你位于没有写入权限的目录中，此片段将显示锁图标并进入 `NOT_WRITABLE` 状态（可按[我们的常规流程](https://github.com/bhilburn/powerlevel9k/wiki/Stylizing-Your-Prompt#segment-color-customization)自定义）。注意：此功能也可在单独的片段 `dir_writable` 中使用。|

如果你想自定义路径的最后一级目录，现在可以设置 `POWERLEVEL9K_DIR_PATH_HIGHLIGHT_FOREGROUND` 为自定义颜色，和/或设置 `POWERLEVEL9K_DIR_PATH_HIGHLIGHT_BOLD=true` 以加粗显示该部分。

你还可以通过 `POWERLEVEL9K_DIR_PATH_SEPARATOR_FOREGROUND` 单独设置分隔符的颜色。

##### disk_usage

`disk_usage` 片段将显示当前工作目录所在分区的磁盘使用率。可使用以下变量进行配置：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_DISK_USAGE_ONLY_WARNING`|false|仅在达到警告或严重级别时显示此片段，否则隐藏。|
|`POWERLEVEL9K_DISK_USAGE_WARNING_LEVEL`|90|触发警告状态的使用率阈值（百分比）。|
|`POWERLEVEL9K_DISK_USAGE_CRITICAL_LEVEL`|95|触发严重状态的使用率阈值（百分比）。|

##### host

`host` 片段将打印主机名。

你可以设置 `POWERLEVEL9K_HOST_TEMPLATE` 变量来更改主机名的显示方式。详见 (ZSH Manual)[http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html#Login-information]。默认设置为 `%m`，将显示第一个 `.` 之前的部分。你可以将其设置为 `%{N}m`（其中 N 为整数），以显示系统主机名的前 N 个段。将 `N` 设置为负数将从末尾开始显示指定数量的段。

```
POWERLEVEL9K_HOST_TEMPLATE="%2m"
```

默认情况下，本地主机会显示主机图标，远程主机会显示 SSH 图标。你可以通过设置以下变量覆盖它们：
```
POWERLEVEL9K_HOST_ICON="\uF109 "
POWERLEVEL9K_SSH_ICON="\uF489 "
```


##### ip

此片段尝试检查当前使用的所有网络接口，并打印找到的第一个地址。如果这不是正确的网卡(NIC)，你可以通过设置以下变量指定正确的网络接口：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_IP_INTERFACE`|None|希望显示 IP 地址的网卡。示例：`eth0`。|

##### vpn_ip

此片段尝试根据 NIC 类型从 nmcli 中提取与 VPN 相关的 IP 地址：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_VPN_IP_INTERFACE`|`tun`|VPN 接口名称。|

##### public_ip

此片段将显示你的公网 IP 地址。获取此信息有几种方法，默认情况下它会尝试所有方法（从最高效的开始）。你也可以指定希望使用的方法。可用的方法包括：通过 opendns 的 dig、curl 或 wget。wget 和 curl 使用的默认主机是 http://ident.me，但如果你愿意可以更改为其他主机。

如果你激活了 VPN，此片段的图标将变为定义的 VPN 图标。

public_ip 片段默认每 5 分钟尝试更新一次你的公网 IP（也可由用户配置）。如果连接断开，将显示缓存的 IP 地址，直到超时时间结束。之后每次生成提示符时都会重新尝试获取。在成功获取到新 IP 之前，此片段将显示 `$POWERLEVEL9K_PUBLIC_IP_NONE` 的值。如果该值为空（默认值）且 `$POWERLEVEL9K_PUBLIC_IP_FILE` 也为空，则不会显示此片段。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_PUBLIC_IP_FILE`|'/tmp/p9k_public_ip'|缓存你公网 IP 的文件路径。|
|`POWERLEVEL9K_PUBLIC_IP_HOST`|'http://ident.me'|获取你公网 IP 的默认主机地址。|
|`POWERLEVEL9K_PUBLIC_IP_TIMEOUT`|300|刷新缓存 IP 的时间间隔（秒）。|
|`POWERLEVEL9K_PUBLIC_IP_METHODS`|(dig curl wget)|按顺序使用的刷新 IP 的方法列表。|
|`POWERLEVEL9K_PUBLIC_IP_NONE`|None|未能获取到 IP 时显示的字符串|

##### load

显示你的一个负载平均值，并根据阈值进行状态着色：
- `0.7 * NUM_CORES <`: 严重 (critical)
- `0.5 * NUM_CORES <`: 警告 (warning)
- `less`: 正常 (normal)

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_LOAD_WHICH`|5|显示哪个时间段的平均值。可选值：1、5 或 15（分钟）|

##### newline

在提示符中插入换行，以便你可以在下一行继续使用片段。这允许你在两行上都使用片段，这与 `POWERLEVEL9K_PROMPT_ON_NEWLINE` 不同，后者仅将片段与提示符本身分隔开。

此功能仅在左侧有效。在右侧无效。

##### nodeenv

显示当前使用的 [nodeenv](https://github.com/ekalinin/nodeenv)。为避免 Nodeenv 的 activate 命令干扰 Powerlevel9k，请在你的 `~/.zshrc` 中设置 `NODE_VIRTUAL_ENV_DISABLE_PROMPT=1`。

##### rbenv

此片段显示在使用 `rbenv` 切换当前 Ruby 环境时所使用的 Ruby 版本。

它通过执行 `rbenv version-name` 命令的输出结果来确定正在使用的版本。

* 如果 `$PATH` 中未找到 `rbenv`，则不显示任何内容。
* 默认情况下，如果当前的本地 Ruby 版本与全局 Ruby 版本相同，则不显示任何内容。参见下方的配置变量以修改此行为。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_RBENV_PROMPT_ALWAYS_SHOW`|`false`|设置为 `true` 可在当前 Ruby 版本与全局版本相同时仍显示 rbenv 片段|

##### pyenv

此片段显示在使用 `pyenv` 切换当前 Python 环境时所使用的 Python 版本。

如果指定了环境变量 `PYENV_VERSION`，将直接使用它。否则，它会通过执行 `pyenv version-name` 命令的输出结果来确定正在使用的版本。

* 如果 `$PATH` 中未找到 `pyenv`，则不显示任何内容。
* 如果当前的 Python 版本与全局 Python 版本相同，则不显示任何内容。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_PYENV_PROMPT_ALWAYS_SHOW`|`false`|设置为 `true` 可在当前 Python 版本与全局版本相同时仍显示 pyenv 片段|

##### rspec_stats

参见下方的[单元测试比例](#unit-test-ratios)。

##### status

此片段显示上一条命令的返回码。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_STATUS_CROSS`|`false`|设置为 `true` 可在上一条命令报错时不显示错误代码，并可选择通过设置 `POWERLEVEL9K_STATUS_OK` 为 `false` 在上一条命令成功完成时隐藏此片段。|
|`POWERLEVEL9K_STATUS_OK`|`true`|设置为 `true` 可在上一条命令成功完成时显示此片段，设为 `false` 则隐藏。|
|`POWERLEVEL9K_STATUS_SHOW_PIPESTATUS`|`true`|设置为 `true` 可显示所有管道命令的退出状态。|
|`POWERLEVEL9K_STATUS_HIDE_SIGNAME`|`false`|设置为 `true` 返回原始退出码（1-255）。设为 `false` 时，大于 128 的值将显示为 `SIGNAME(-n)`（例如 `KILL(-9)`）|

##### ram

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_RAM_ELEMENTS`|Both|指定仅显示 `ram_free` 或 `swap_used`，而不是同时显示两者。|

##### symfony2_tests

参见下方的[单元测试比例](#unit-test-ratios)。

##### time

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_TIME_FORMAT`|`'H:M:S'`|此片段使用的 ZSH 时间格式。|

例如，如果你想要反转的时间格式，可以使用：
```zsh
# 反转时间格式
POWERLEVEL9K_TIME_FORMAT='%D{%S:%M:%H}'
```
如果你使用“Awesome Powerline Font”，还可以在此片段中添加一个时间符号：
```zsh
# 输出时间、日期以及来自“Awsome Powerline Font”集的符号
POWERLEVEL9K_TIME_FORMAT="%D{%H:%M:%S \uE868  %d.%m.%y}"
```

##### user

`user` 片段将打印用户名。

你还可以通过设置以下变量覆盖图标：

```
POWERLEVEL9K_USER_ICON="\uF415" # 
POWERLEVEL9K_ROOT_ICON="#"
POWERLEVEL9K_SUDO_ICON=$'\uF09C' # 
```

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`DEFAULT_USER`|None|视为“默认上下文”的用户名。|
|`POWERLEVEL9K_ALWAYS_SHOW_USER`|`false`|始终打印此片段。|
|`POWERLEVEL9K_USER_TEMPLATE`|`%n`|默认用户名提示符。有关所有可能的扩展，请参阅 [ZSH Documentation](http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html)。|

##### vcs

默认情况下，`vcs` 片段会提供相当多的信息。进一步的自定义通过以下变量实现：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_HIDE_BRANCH_ICON`|`false`|设置为 `true` 可在片段中隐藏分支图标。|
|`POWERLEVEL9K_SHOW_CHANGESET`|`false`|设置为 `true` 可在片段中显示哈希值/变更集。|
|`POWERLEVEL9K_CHANGESET_HASH_LENGTH`|`12`|在片段中显示的哈希值/变更集的字符数。|
|`POWERLEVEL9K_VCS_SHOW_SUBMODULE_DIRTY`|`true`|设置为 `false` 可在顶级仓库提示符中不反映子模块状态。|
|`POWERLEVEL9K_VCS_HIDE_TAGS`|`false`|设置为 `true` 停止在片段中显示标签。|
|`POWERLEVEL9K_VCS_GIT_HOOKS`|`(vcs-detect-changes git-untracked git-aheadbehind git-stash git-remotebranch git-tagname)`|Git 仓库的片段布局。|
|`POWERLEVEL9K_VCS_HG_HOOKS`|`(vcs-detect-changes)`|Mercurial 仓库的片段布局。|
|`POWERLEVEL9K_VCS_SVN_HOOKS`|`(vcs-detect-changes svn-detect-changes)`|SVN 仓库的片段布局。|
|`POWERLEVEL9K_VCS_ACTIONFORMAT_FOREGROUND`|`red`|执行操作期间（例如 `REBASE`）的前景色颜色。|


##### vcs symbols

`vcs` 片段使用各种符号来告诉你仓库的状态。这些符号取决于你安装的字体以及上方[安装](#installation)部分中选择的 `POWERLEVEL9K_MODE`。

| `Compatible` | `Powerline` | `Awesome Powerline` | Explanation
|--------------|---------------------|-------------------|--------------------------
| `↑4`         | `↑4`                | ![icon_outgoing](https://cloud.githubusercontent.com/assets/1544760/7976089/b5904d6e-0a76-11e5-8147-5e873ac52d79.gif)4  | 你的仓库比远程分支领先（ahead）的提交数
| `↓5`         | `↓5`                | ![icon_incoming](https://cloud.githubusercontent.com/assets/1544760/7976091/b5909c9c-0a76-11e5-9cad-9bf0a28a897c.gif)5  | 你的仓库比远程分支落后（behind）的提交数
| `⍟3`         | `⍟3`                | ![icon_stash](https://cloud.githubusercontent.com/assets/1544760/7976094/b5ae9346-0a76-11e5-8cc7-e98b81824118.gif)3 | 暂存区(stash)数量，此处为 3。
| `●`          | `●`                 | ![icon_unstaged](https://cloud.githubusercontent.com/assets/1544760/7976096/b5aefa98-0a76-11e5-9408-985440471215.gif) | 工作区中存在未暂存的更改
| `✚`          | `✚`                 | ![icon_staged](https://cloud.githubusercontent.com/assets/1544760/7976095/b5aecc8a-0a76-11e5-8988-221afc6e8982.gif) | 工作区中存在已暂存的更改
| `?`          | `?`                 | ![icon_untracked](https://cloud.githubusercontent.com/assets/1544760/7976098/b5c7a2e6-0a76-11e5-8c5b-315b595b2bc4.gif)  | 工作区中存在仓库未知的文件
| `→`          | `→`                 | ![icon_remote_tracking_branch](https://cloud.githubusercontent.com/assets/1544760/7976093/b5ad2c0e-0a76-11e5-9cd3-62a077b1b0c7.gif) | 你的分支名称与其跟踪分支不同。
| `☿`          | `☿`                 | ![icon_bookmark](https://cloud.githubusercontent.com/assets/1544760/7976197/546cfac6-0a78-11e5-88a6-ce3a1e0a174e.gif) | 一个 Mercurial bookmark 处于活动状态。
| `@`         | ![icon_branch_powerline](https://cloud.githubusercontent.com/assets/1544760/8000852/e7e8d8a0-0b5f-11e5-9834-de9b25c92284.gif) | ![](https://cloud.githubusercontent.com/assets/1544760/7976087/b58bbe3e-0a76-11e5-8d0d-7a5c1bc7f730.gif) | 分支图标
| None         |  None               | ![icon_commit](https://cloud.githubusercontent.com/assets/1544760/7976088/b58f4e50-0a76-11e5-9e70-86450d937030.gif)2c3705 | 当前提交的哈希值。此处为 "2c3705"
| None         |  None               | ![icon_git](https://cloud.githubusercontent.com/assets/1544760/7976092/b5909f80-0a76-11e5-9950-1438b9d72465.gif) | 仓库是 Git 仓库
| None         |  None               | ![icon_mercurial](https://cloud.githubusercontent.com/assets/1544760/7976090/b5908da6-0a76-11e5-8c91-452b6e73f631.gif) | 仓库是 Mercurial 仓库

##### vcs truncation

你可以通过截断长名称来限制分支名的长度。可用的自定义项如下：

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_VCS_SHORTEN_LENGTH`|None|此字段决定显示多少字符。|
|`POWERLEVEL9K_VCS_SHORTEN_MIN_LENGTH`|None|此字段决定分支名的最小长度。如果分支名长度大于此值，则进行截断。|
|`POWERLEVEL9K_VCS_SHORTEN_STRATEGY`|None|此字段决定如何截断分支名。详见下表。|
|`POWERLEVEL9K_SHORTEN_DELIMITER`|`...`|截断字符串中使用的分隔符。可以是任意字符串，如果希望没有分隔符可设为空字符串。|

| Strategy Name | Description |
|---------------|-------------|
|`truncate_middle`|截断路径中间部分。例如分支名为 `1234-super_super_long_branch_name`，如果同时设置了 `POWERLEVEL9K_VCS_SHORTEN_LENGTH=5`（控制保留的字符数），则会被截断为 `1234-..._name`。|
|`truncate_from_right`|仅保留分支名开头部分不变。例如分支名将如下截断：`1234-...`。保留多少字符由 `POWERLEVEL9K_VCS_SHORTEN_LENGTH` 控制。|

例如，如果你希望将 `1234-super_super_long_branch_name` 截断为 `1234-..` 且不涉及 `development`：
```zsh
POWERLEVEL9K_VCS_SHORTEN_LENGTH=4
POWERLEVEL9K_VCS_SHORTEN_MIN_LENGTH=11
POWERLEVEL9K_VCS_SHORTEN_STRATEGY="truncate_from_right"
POWERLEVEL9K_VCS_SHORTEN_DELIMITER=".."
```

##### vi_mode

此片段显示 ZSH 当前的输入模式。注意：仅当你使用 [ZSH Line Editor](http://zsh.sourceforge.net/Doc/Release/Zsh-Line-Editor.html)（VI 模式）时才有用。你可以通过 `.zshrc` 配置或插件（如 [Oh-My-Zsh 的 vi-mode 插件](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/vi-mode/vi-mode.plugin.zsh）启用此功能。

| Variable | Default Value | Description |
|----------|---------------|-------------|
|`POWERLEVEL9K_VI_INSERT_MODE_STRING`|"INSERT"|在“插入”模式下显示的字符串。|
|`POWERLEVEL9K_VI_COMMAND_MODE_STRING`|"NORMAL"|在“命令”模式下显示的字符串。|

要在 `INSERT` 模式下完全隐藏此片段，请设置 `POWERLEVEL9K_VI_INSERT_MODE_STRING=''`

##### virtualenv

此片段显示你的 Python [VirtualEnv](https://virtualenv.pypa.io/en/latest/)。为避免 VirtualEnvs activate 命令干扰 Powerlevel9k，请在你的 `~/.zshrc` 中设置 `VIRTUAL_ENV_DISABLE_PROMPT=1`。

#### 单元测试比例 (Unit Test Ratios)

`symfony2_tests` 和 `rspec_stats` 片段均显示源代码中“真实”类与测试类的比例。这只是一个非常简单的比例，不显示代码覆盖率或任何复杂的统计数据。它仅统计你的源文件和测试文件数量，并计算它们之间的比率。足以让你快速了解当前项目的测试情况。

### 禁用/启用 Powerlevel9k

你可以随时通过调用以下命令来禁用 P9k 并返回到非常基础的提示符：

```zsh
$ prompt_powerlevel9k_teardown
```

之后你可以通过调用以下命令重新启用它：

```zsh
$ prompt_powerlevel9k_setup
```

### tl; dr (太长不看版)

只想快速上手？查看 Wiki 的[展示你的配置](https://github.com/bhilburn/powerlevel9k/wiki/Show-Off-Your-Config)部分即可快速开始。

[Wiki 中还有大量其他有用信息！](https://github.com/bhilburn/powerlevel9k/wiki)

### License

项目：MIT

Logo：CC-BY-SA. 源码仓库：https://github.com/bhilburn/powerlevel9k-logo