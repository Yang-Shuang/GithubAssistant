<p align="center">
  <a href="https://github.com/trimstray/test-your-sysadmin-skills">
    <img src="https://github.com/trimstray/test-your-sysadmin-skills/blob/master/static/img/sysadmin_preview.png" alt="Master">
  </a>
</p>

<br>

<p align="center">:star:</p>

<p align="center">"<i>优秀的管理员不需要无所不知，但必须能针对不可能完成的项目想出绝妙的解决方案。</i>" - cwheeler33 (ServerFault)</p>

<p align="center">:star:</p>

<p align="center">"<i>我的技能在于让事情运转起来，而不是背诵海量的事实。[...] 如果我要修复一个系统，我会识别问题、检查日志并查找错误信息。如果需要实施解决方案，我会研究合适的方案、实施并记录它，之后除非经常交互，否则我对它是如何工作的只有大致的了解……这就是为什么要做文档的原因。</i>" - Sparcrypt (Reddit)</p>

<br>

<p align="center">
  <a href="https://github.com/trimstray/test-your-sysadmin-skills/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?longCache=true" alt="Pull Requests">
  </a>
  <a href="LICENSE.md">
    <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg?longCache=true" alt="MIT License">
  </a>
</p>

<br>

****

<br>

:information_source: &nbsp;该项目包含 **284** 道测试题及答案，可用于自我知识测试或用于系统管理员（Linux (\*nix)）职位的面试/考试。

:heavy_check_mark: &nbsp;答案仅为**示例**，并未涵盖整个主题的大部分细节。其中大多数包含了有助于深入理解的**有用资源**。

:warning: &nbsp;标记为 **`***`** 的题目目前还没有答案或答案不完整——请提交 Pull Request 来补充它们！

:traffic_light: &nbsp;如果你发现某些内容不合理或不正确，**请提交 Pull Request**，并添加关于你更改内容的有效且合理的解释或评论。

:books: &nbsp;为了提升你的知识/技能，请参阅 [devops-interview-questions](https://github.com/bregman-arie/devops-interview-questions)。这看起来非常有趣。

<br>

<p align="center">
  » <b><code><a href="https://github.com/trimstray/test-your-sysadmin-skills/issues">欢迎提出所有建议</a></code></b> «
</p>

<br>

## Table of Contents (目录)

| <b><u>章节类型</u></b> | <b><u>题目数量</u></b> | <b><u>简短描述</u></b> |
| :---         | :---         | :---         |
| <b>[简介](#introduction)</b> |||
| :small_orange_diamond: [简单问题](#simple-questions) | 14 questions | 轻松、有趣且简单——非常适合入门。 |
| <b>[通用知识](#general-knowledge)</b> |||
| :small_orange_diamond: [初级系统管理员](#junior-sysadmin) | 65 questions | 相对简单直接，基于基础知识。 |
| :small_orange_diamond: [中级系统管理员](#regular-sysadmin) | 94 questions | 如果你具备扎实的知识，这是中等难度的题目。 |
| :small_orange_diamond: [高级系统管理员](#senior-sysadmin) | 99 questions | 难题和谜题。如果你想变得优秀，请查看这些内容。 |
| <b>[秘密知识](#secret-knowledge)</b> ||
| :small_orange_diamond: [专家级系统管理员](#guru-sysadmin) | 12 questions | 非常深入的问题，旨在了解专家级系统管理员的知识水平。 |

<br>

## <a name="introduction">简介</a>

### :diamond_shape_with_a_dot_inside: <a name="simple-questions">简单问题</a>

- <b>这周你学到了什么？</b>
- <b>系统管理领域有什么让你感到兴奋或感兴趣的地方？</b>
- <b>你最近遇到的技术挑战是什么，你是如何解决的？</b>
- <b>谈谈你完成的最后一个主要项目。</b>
- <b>你有参与任何开源项目吗？</b>
- <b>描述一下你的家庭实验室（homelab）设置。</b>
- <b>你最引以为豪的个人成就是什么？</b>
- <b>谈谈你犯过的最大的错误。如果今天重来，你会怎么做？</b>
- <b>在第一天到新公司上班时，你会安装哪些软件工具？</b>
- <b>你是如何管理你的知识库的（例如 wiki、文件、门户）。</b>
- <b>你每天查看哪些新闻来源？（系统管理员、安全相关或其他）</b>
- <b>你的 NOC 团队有一笔用于系统管理员认证的新预算。你想要哪个证书，为什么？</b>
- <b>你是如何与开发人员互动的：*我们 vs 他们* 还是 *所有人以不同的方式共同努力*？</b>
- <b>如果你要面试我，你会问什么系统管理问题来了解我在非标准情况下的处理能力？</b>

## <a name="general-knowledge">通用知识</a>

### :diamond_shape_with_a_dot_inside: <a name="junior-sysadmin">初级系统管理员</a>

###### 系统问题 (37)

<details>
<summary><b>举一些 Linux 发行版的例子。你最喜欢的发行版是什么，为什么？</b></summary><br>
- Red Hat Enterprise Linux
- Fedora
- CentOS
- Debian
- Ubuntu
- Mint
- SUSE Linux Enterprise Server (SLES)
- SUSE Linux Enterprise Desktop (SLED)
- Slackware
- Arch
- Kali
- Backbox

我最喜欢的 Linux 发行版：

- **Arch Linux**，它提供了一个不错的极简主义基础系统，你可以在其上构建自定义操作系统。它的优点在于拥有 Arch 用户仓库（AUR），结合其官方二进制仓库，使其可能拥有所有发行版中最大的软件库。它的打包过程也非常简单，这意味着如果某个包不在其官方仓库或 AUR 中，自己制作起来应该很容易。
- **Linux Mint**，它也基于 Ubuntu LTS 版本构建，但提供了一些具有不同桌面环境的版本，包括 Cinnamon、MATE 和 Xfce。Mint 相当精致，美学设计也很吸引人，我特别喜欢它的新图标主题，尽管我非常不喜欢它的 GTK+ 主题（对我来说太单调了）。我也发现它在最新版本 Mint 19 中存在一个 bug，这让我很恼火，因为我在两周前就在他们的论坛上报告了这个 bug，但至今没有收到回复，而且这个 bug 让我的使用体验变得更加困难。
- **Kali Linux**，这是一个基于 Debian 的 Linux 发行版，旨在用于高级渗透测试和安全审计。Kali 包含数百种工具，针对各种信息安全任务进行了优化，如渗透测试、安全研究、计算机取证和逆向工程。

有用资源：

- [Linux 发行版列表](https://en.wikipedia.org/wiki/List_of_Linux_distributions)
- [你最喜欢的 Linux 发行版是什么，为什么？](https://www.quora.com/What-is-your-favorite-Linux-distro-and-why)

</details>

<details>
<summary><b>Unix、Linux、BSD 和 GNU 之间有什么区别？</b></summary><br>

**GNU** 实际上并不是一个操作系统。它更像是一套规则或哲学，指导着自由软件的发展，同时也在试图创建操作系统的过程中诞生了一堆工具。因此，**GNU** 工具基本上已经是存在的工具的开源版本，但为了符合开放软件的原理而重新实现了。**GNU/Linux** 是这些工具和 **Linux 内核**的混合体，形成了一个完整的操作系统，但也有其他的 GNU，例如 **GNU/Hurd**。

**Unix** 和 **BSD** 是“更老”的 POSIX 实现，处于不同程度的“闭源”状态。**Unix** 通常是完全闭源的，但 **Unix** 的种类就像 **Linux**（甚至更多）一样多。**BSD** 通常不被认为是“开源”的，但在发布时被认为是非常开放的。它的许可证允许商业使用，限制比当时更“开放”的许可证要少得多。

**Linux** 是这四者中最新的。严格来说，它只是“一个内核”；然而，一般来说，当与 GNU 工具和几个其他核心组件结合使用时，它被视为一个完整的操作系统。

这些之间主要的管理区别在于它们的理念。**Unix**、**Linux** 和 **BSD** 有不同的理念并加以实施。它们都是 POSIX 标准的，基本上是可以互换的。它们以不同的方式解决一些相同的问题。因此，除了理念和如何选择实现 POSIX 标准之外，差异很小。

更多信息建议阅读一篇关于 **GNU**、**OSS**、**Linux**、**BSD** 和 **UNIX** 创建过程的简短文章。这些文章可能会有偏向于各自的理念，但这些文章应该能让你更好地了解它们之间的区别。

有用资源：

- [Unix、Linux、BSD 和 GNU 之间有什么区别？（原版）](https://unix.stackexchange.com/questions/104714/what-is-the-difference-between-unix-linux-bsd-and-gnu)
- [大辩论：是 Linux 还是 GNU/Linux？](https://www.howtogeek.com/139287/the-great-debate-is-it-linux-or-gnulinux/)

</details>

<details>
<summary><b>什么是 CLI？谈谈你最喜欢的 CLI 工具、技巧和黑客技术。</b></summary><br>

**CLI** 是命令行界面（Command Line Interface）或命令语言解释器的缩写。命令行是控制系统/计算机的最强大方式之一。

在类 Unix 系统中，**CLI** 是用户可以输入命令供系统执行的接口。**CLI** 非常强大，但容错性不高。

**CLI** 允许你以更精细的方式操作系统的内部结构和代码。无论使用什么操作系统，它都提供了比 GUI（图形用户界面）更大的灵活性和控制力。许多你可能想要使用的软件程序（托管在 Github 上）也需要在 **CLI** 中运行一些命令才能启动它们。

**我最喜欢的工具**

- `screen` - 免费的终端多路复用器，我可以启动一个会话，即使连接丢失我的终端也会保存下来，这样你可以稍后或从家里恢复
- `ssh` - 最有价值的整体命令之一，我可以用它做一些很棒的事情：
  * 使用 `sshfs` 挂载互联网上的文件系统
  * 转发命令：通过 ssh 启动 rsync 守护进程，从而在没有 rsync 守护进程的服务器上运行 `rsync`
  * 在批处理文件中运行：我可以重定向远程命令的输出并在本地批处理文件中使用它
- `vi/vim` - 最流行和最强大的文本编辑器，它是通用的，即使在大文件上也能工作得非常快
- `bash-completion` - 包含许多预定义的 shell 补全规则

**技巧与黑客技术**

- 使用 `CTRL + R` 搜索命令历史
- `popd/pushd` 和其他允许你操作目录栈的 shell 内置命令
- 编辑键盘快捷键，如 `CTRL + U`、`CTRL + E`
- 组合键会自动展开：
  * `!*` - 上一个命令的所有参数
  * `!!` - 整个上一个命令
  * `!ssh` - 以 ssh 开头的最后一个命令

有用资源：

- [命令行界面定义](http://www.linfo.org/command_line_interface.html)
- [你最喜欢的 Bash 单行命令行技巧是什么？](https://stackoverflow.com/questions/68372/what-is-your-single-most-favorite-command-line-trick-using-bash/69716)
- [你最喜欢哪些命令行功能或技巧？](https://unix.stackexchange.com/questions/6/what-are-your-favorite-command-line-features-or-tricks)

</details>

<details>
<summary><b>你最喜欢的 shell 是什么，为什么？</b></summary><br>

**BASH** 是我最喜欢的。这真的是一种偏好类型的事情，我喜欢它的语法，它对我来说很“合拍”。输入/输出重定向语法（`>>`, `<< 2>&1`, `2>`, `1>` 等）类似于 C++，这使得我更容易识别。

我也喜欢 **ZSH** shell，因为它比 **BASH** 更可定制。它具有 Oh-My-Zsh 框架、强大的基于上下文的标签补全、增强版的模式匹配/通配符、可加载模块等。

有用资源：

- [命令壳层比较](https://en.wikipedia.org/wiki/Comparison_of_command_shells)

</details>

<details>
<summary><b>如何在命令行上获取帮助？***</b></summary><br>

- `man` [commandname] 可用于查看命令的描述（例如：`man less`, `man cat`）

- `-h` 或 `--help` 某些程序在传递此参数时会实现打印说明（例如：`python -h` 和 `python --help`）

</details>

<details>
<summary><b>登录到 *nix 服务器后的前 5 个命令。</b></summary><br>

- `w` - 其中包含大量关于系统运行时间的有用信息
- `top` - 你可以看到所有正在运行的进程，然后按 CPU、内存利用率等排序
- `netstat` - 了解你的服务器在哪个端口和 IP 上监听，以及哪些进程在使用它们
- `df` - 报告文件系统使用的可用磁盘空间量
- `history` - 告诉你当前连接的用户之前运行过什么

有用资源：

- [当我连接到 Linux 服务器时的前 5 个命令（原版）](https://www.linux.com/blog/first-5-commands-when-i-connect-linux-server)

</details>

<details>
<summary><b><code>ls -al</code> 输出中的字段是什么意思？</b></summary><br>

按输出顺序：

```bash
-rwxrw-r--    1    root   root 2048    Jan 13 07:11 db.dump
```

- 文件权限，
- 链接数，
- 所有者名称，
- 所有者组，
- 文件大小，
- 最后修改时间，
- 文件/目录名称

文件权限显示如下：

- 第一个字符是 `-` 或 `l` 或 `d`，`d` 表示目录，`-` 代表文件，`l` 是符号链接（或软链接）——一种特殊类型的文件
- 三组字符，三次出现，分别表示所有者、组和其他人的权限：
  - `r` = 可读 (readable)
  - `w` = 可写 (writable)
  - `x` = 可执行 (executable)

在你的示例 `-rwxrw-r--` 中，这意味着显示的这一行是：

- 普通文件（显示为 `-`）
- 所有者可读、可写和可执行 (`rwx`)
- 组可读、可写，但不可执行 (`rw-`)
- 其他人只读，不可写或不可执行 (`r--`)

有用资源：

- [ls -al 输出中的字段是什么意思？（原版）](https://unix.stackexchange.com/questions/103114/what-do-the-fields-in-ls-al-output-mean)

</details>

<details>
<summary><b>如何获取已登录用户的列表？</b></summary><br>

对于已登录用户的摘要，包括每个用户名、用户附加的终端、他们登录的日期/时间以及可能进行连接的计算机，请输入：

```bash
# 它使用 /var/run/utmp 和 /var/log/wtmp 文件来获取详细信息。
who
```

对于广泛的信息，包括用户名、终端、源计算机的 IP 地址、登录开始的时间、任何空闲时间、进程 CPU 周期、作业 CPU 周期以及当前运行的命令，请输入：

```bash
# 它使用 /var/run/utmp 及其进程的 /proc。
w
```

另外，显示最后登录用户列表也很重要，请输入：

```bash
# 它使用 /var/log/wtmp。
last
```

有用资源：

- [识别 Linux 系统上谁已登录的 4 种方法](https://www.thegeekstuff.com/2009/03/4-ways-to-identify-who-is-logged-in-on-your-linux-system/)

</details>

<details>
<summary><b>在后台运行进程有什么优势？你如何做到这一点？</b></summary><br>

在后台运行进程的最显著优势是，当其他进程在后台运行时，你可以同时执行任何其他任务。因此，当你处理不同进程时，可以在后台完成更多进程。这可以通过在命令末尾添加特殊字符 `&` 来实现。

通常，那些执行时间过长且不需要用户交互的应用程序会被发送到后台，以便我们继续在终端中工作。

例如，如果你想下载东西到后台，你可以：

```bash
wget https://url-to-download.com/download.tar.gz &
```

当你运行上述命令时，你会得到以下输出：

```bash
[1] 2203
```

这里 1 是作业序列号，2203 是作业的 PID。

你可以使用以下命令查看后台运行的作业：

```bash
jobs
```

当你在后台执行作业时，它会给你一个作业的 PID，你可以使用以下命令杀死在后台运行的作业：

```bash
kill PID
```

用作业的 PID 替换 PID。如果你只有一个作业在运行，你可以将其带到前台：

```bash
fg
```

如果你有多个作业在后台运行，你可以将任何作业带到前台：

```bash
fg %#
```

将 `#` 替换为作业的序列号。

有用资源：

- [我如何在 Unix 中在后台运行进程？](https://kb.iu.edu/d/afnz)
- [作业控制命令](http://tldp.org/LDP/abs/html/x9644.html)
- [在后台运行应用程序有什么优势？](https://unix.stackexchange.com/questions/162186/what-is-are-the-advantages-of-running-applications-in-backgound)

</details>

<details>
<summary><b>在你能够管理进程之前，你必须能够识别它们。你会使用哪些工具？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>以 root 用户身份运行命令。这是好还是坏的做法？</b></summary><br>

（一切）都以 root 身份运行是糟糕的，因为：

- **愚蠢**：没有什么能阻止你犯粗心的错误。如果你试图以任何潜在有害的方式更改系统，你需要使用 sudo，这会确保有一个暂停（当你输入密码时），以确保你没有犯错。
- **安全**：如果不知道管理员用户的登录账户，就更难被黑客攻击。root 意味着你已经拥有了工作管理凭证的一半。
- **你真的不需要它**：如果你需要以 root 身份运行几个命令，并且对 `sudo` 过期后必须多次输入密码感到烦恼，你只需要做 `sudo -i`，现在你就是 root 了。想要使用管道运行一些命令？那么使用 `sudo sh -c "command1 | command2"`。
- **你总是可以在恢复控制台中使用它**：恢复控制台允许你从重大错误中恢复，或修复由应用程序引起的问题（你必须以 `sudo` 身份运行该问题）。Ubuntu 在这种情况下没有 root 账户的密码，但你可以在线搜索更改它的方法——这将使任何能够物理接触你的机器的人更难造成损害。

有用资源：

- [为什么以 root 登录是糟糕的？（原版）](https://askubuntu.com/questions/16178/why-is-it-bad-to-log-in-as-root)
- [一直做 root 有什么问题？](https://serverfault.com/questions/57962/whats-wrong-with-always-being-root)
- [为什么你应该避免以 root 身份运行应用程序](https://bencane.com/2012/02/20/why-you-should-avoid-running-applications-as-root/)

</details>

<details>
<summary><b>如何检查内存统计信息和 CPU 统计信息？</b></summary><br>

你会使用 `top/htop`。使用 `free` 和 `vmstat` 命令我们可以分别显示物理和虚拟内存统计信息。在 `sar` 命令的帮助下，我们可以看到 CPU 利用率和其他统计信息（但大多数系统中甚至没有安装 `sar`）。

有用资源：

- [我如何找出 Linux CPU 利用率？](https://www.cyberciti.biz/tips/how-do-i-find-out-linux-cpu-utilization.html)
- [你必须知道的 16 个 Linux 服务器监控命令](https://www.hpe.com/us/en/insights/articles/16-linux-server-monitoring-commands-you-really-need-to-know-1703.html)

</details>

<details>
<summary><b>什么是负载平均值（Load Average）？</b></summary><br>

Linux **负载平均值** 是“系统负载平均值”，显示运行线程（任务）对系统的平均需求，即正在运行的加上等待的线程的平均数量。这测量的是需求，可能大于系统当前处理的能力。大多数工具显示三个平均值，分别为 1、5 和 15 分钟。

这三个数字不是不同 CPU 的数字。这些数字是给定时间段内负载数字的平均值（过去 1、5 和 15 分钟）。

**负载平均值**通常被描述为“运行队列的平均长度”。因此，少数消耗 CPU 的进程或线程可以将 **负载平均值** 提高到 1 以上。如果 **负载平均值** 小于 CPU 核心总数，则没有问题。但如果它高于 CPU 数量，这意味着一些线程/进程将保持在队列中，准备运行但等待空闲 CPU。

它是为了给你一个系统状态的概念，经过几个时间段平均。由于它是平均值，当系统在重负荷下后，恢复到 0 需要时间。

一些解释：

- 如果平均值是 0.0，那么你的系统是空闲的
- 如果 1 分钟平均值高于 5 或 15 分钟平均值，则负载正在增加
- 如果 1 分钟平均值低于 5 或 15 分钟平均值，则负载正在减少
- 如果它们高于 CPU 数量，那么你可能有性能问题（这取决于具体情况）

有用资源：

- [Linux 负载平均值：解开谜团（原版）](http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)
- [Linux 负载平均值 - 权威总结](http://blog.angulosolido.pt/2015/04/linux-load-average-definitive-summary.html)
- [CPU 负载平均值是如何工作的（以及如何使用它们对 Web 服务器性能进行分类！）](https://jvns.ca/blog/2016/02/07/cpu-load-averages/)

</details>

<details>
<summary><b>我的密码存储在 Linux/Unix 的哪里？</b></summary><br>

密码根本没有存储在系统中的任何地方。存储在 `/etc/shadow` 中的是所谓的密码哈希值（hashes）。

通过对其文本（密码）执行一种称为单向函数的操作来创建文本的哈希，从而创建一个要检查的字符串。设计上，“不可能”（计算上不可行）逆转该过程。

较旧的 Unix 变体将加密后的密码与其他每个账户的信息一起存储在 `/etc/passwd` 中。

更新的版本只是在 `/etc/passwd` 的相关字段中具有 `*`，并使用 `/etc/shadow` 来存储密码，部分是为了确保没有人能在只需要其他东西时获得对密码的读取访问权限（`shadow` 通常比 `passwd` 受到更强的保护）。

更多信息请参阅 `man crypt`, `man shadow`, `man passwd`。

有用资源：

- [我的密码存储在 Linux 上的哪里？](https://security.stackexchange.com/questions/37050/where-is-my-password-stored-on-linux)
- [Linux 中用户的密码位于何处？](https://www.cyberciti.biz/faq/where-are-the-passwords-of-the-users-located-in-linux/)
- [Linux 密码和 Shadow 文件格式](https://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html)

</details>

<details>
<summary><b>如何递归更改所有目录的权限（除了文件）以及所有文件的权限（除了目录）？</b></summary><br>

要将所有目录更改为例如 **755** (`drwxr-xr-x`)：

```bash
find /opt/data -type d -exec chmod 755 {} \;
```

要将所有文件更改为例如 **644** (`-rw-r--r--`)：

```bash
find /opt/data -type f -exec chmod 644 {} \;
```

有用资源：

- [如何设置文件夹及其所有子文件夹和文件的 chmod？（原版）](https://stackoverflow.com/questions/3740152/how-do-i-set-chmod-for-a-folder-and-all-of-its-subfolders-and-files?rq=1)

</details>

<details>
<summary><b>每个命令都失败并显示 <code>command not found</code>。如何追踪错误来源并解决它？</b></summary><br>

看起来在某个时候或另一个时候，默认 `PATH` 环境变量被覆盖了。你拥有的这种类型的错误表明 `PATH` 不包含例如 `/bin`，而命令（包括 bash）就驻留在其中。

开始调试你的 bash 脚本或命令的一种方法是使用 `-x` 选项启动子 shell：

```bash
bash --login -x
```

这将向你显示启动该 shell 时执行的每个命令及其参数。

同样非常有帮助的是显示 `PATH` 变量值：

```bash
echo $PATH
```

如果你运行这个：

```bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin
```

大多数命令应该开始工作——然后你可以编辑 `~/.bash_profile` 而不是 `~/.bashrc`，并修复任何重置那里 `PATH` 的东西。**root** 和其他用户的默认 `PATH` 变量值在 `/etc/profile` 文件中。

有用资源：

- [如何正确地将路径添加到 PATH？](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path)

</details>

<details>
<summary><b>你输入了 <code>CTRL + C</code> 但你的脚本仍在运行。如何停止它？ </b></summary><br>

在大多数情况下，你可以使用 `CTRL + C` 键盘组合来停止正在运行的脚本。这会向脚本发送一个中断信号（SIGINT），从而终止其执行。如果这不起作用且脚本仍在运行，你可以尝试使用 `CTRL + \` 组合，它会向脚本发送一个退出信号（SIGQUIT），这可能会立即终止它。

或者，如果你使用的是终端或命令行界面，可以尝试使用 `kill` 命令向脚本进程发送信号。你可以使用 `ps` 或 `top` 命令找到脚本的进程 ID (PID)，然后使用带有 PID 的 `kill` 来停止脚本。

在某些情况下，你可能需要使用 `kill -9` 命令强制停止脚本，因为常规 kill 命令在脚本卡住或未响应时可能不起作用。`-9` 选项发送一个 SIGKILL 信号，这会强制进程立即停止。
</details>

<details>
<summary><b>什么是 <code>grep</code> 命令？如何在同一行中匹配多个字符串？</b></summary><br>

`grep` 实用程序是一类 Unix 工具，包括 `egrep` 和 `fgrep`。

`grep` 搜索文件模式。如果你正在另一个命令的输出中寻找特定模式，`grep` 会突出显示相关行。使用此 grep 命令来搜索日志文件、特定进程等。

要匹配多个字符串：

```bash
grep -E "string1|string2" filename
```

或者

```bash
grep -e "string1" -e "string2" filename
```

有用资源：

- [什么是 grep，我如何使用它？（原版）](https://kb.iu.edu/d/afiy)

</details>

<details>
<summary><b>解释文件内容命令及其描述。</b></summary><br>

- `head`：用于检查文件的开头。
- `tail`：用于检查文件的结尾。它是 head 命令的反向操作。
- `cat`：用于查看、创建、连接文件。
- `more`：以分页形式在终端窗口中显示文本。
- `less`：用于向后查看文本，并提供单行移动功能。

有用资源：

- [从 shell 提示符查看文本文件](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/4/html/Step_by_Step_Guide/s1-viewingtext-terminal.html)

</details>

<details>
<summary><b>SIGHUP, SIGINT, SIGKILL 和 SIGTERM POSIX 信号。解释。</b></summary><br>

- **SIGHUP** - 当控制终端关闭时发送给进程。它最初设计用于通知进程串行线路断开（挂起）。许多守护进程在收到此信号时会重新加载其配置文件并重新打开日志文件，而不是退出。
- **SIGINT** - 当其控制终端希望中断进程时发送给用户进程。这通常是通过按 `Ctrl+C` 发起的，但在某些系统上，“删除”字符或“中断”键也可以使用。
- **SIGKILL** - 发送给进程以使其立即终止（杀死）。与 **SIGTERM** 和 **SIGINT** 不同，此信号不能被捕获或忽略，接收进程在收到此信号时不能执行任何清理工作。
- **SIGTERM** - 发送给进程以请求其终止。与 **SIGKILL** 信号不同，它可以被进程捕获、解释或忽略。这允许进程执行优雅的终止，释放资源并在适当的情况下保存状态。**SIGINT** 几乎与 **SIGTERM** 相同。

有用资源：

- [POSIX 信号](https://dsa.cs.tsinghua.edu.cn/oj/static/unix_signal.html)
- [Unix 信号编程简介](http://titania.ctie.monash.edu.au/signals/)

</details>

<details>
<summary><b><code>kill</code> 命令做什么？</b></summary><br>

在 Unix 和类 Unix 操作系统中，`kill` 是一个用于向进程发送信号命令。默认情况下，发送的消息是终止信号，请求该进程退出。但 `kill` 有点名不副实；发送的信号可能与杀死进程无关。

有用资源：

- [掌握 Linux 中的“Kill”命令](https://www.maketecheasier.com/kill-command-in-linux/)

</details>

<details>
<summary><b><code>rm</code> 和 <code>rm -rf</code> 有什么区别？</b></summary><br>

`rm` 仅删除命名文件（而不是目录）。正如你所说，带有 `-rf`：

- `-r`, `-R`, `--recursive` 递归删除目录的内容，包括隐藏文件和子目录
- `-f`, `--force` 忽略不存在的文件，从不提示

有用资源：

- [`rm -r` 和 `rm -f` 之间有什么区别？](https://superuser.com/questions/1126206/what-is-the-difference-between-rm-r-and-rm-f)

</details>

<details>
<summary><b>我如何递归地 <code>grep</code>？举几个例子解释。***</b></summary>

待补充。

</details>

<details>
<summary><b><code>archive.tgz</code> 有 ~30 GB。你如何列出其内容并只提取一个文件？</b></summary><br>

```bash
# 列出内容
tar tf archive.tgz

# 提取文件
tar xf archive.tgz filename
```

有用资源：

- [列出 tar 或 tar.gz 文件的内容](https://www.cyberciti.biz/faq/list-the-contents-of-a-tar-or-targz-file/)
- [如何从 tar.gz 中提取特定文件？](https://unix.stackexchange.com/questions/61461/how-to-extract-specific-files-from-tar-gz)

</details>

<details>
<summary><b>在一行中执行组合多个 shell 命令。</b></summary><br>

如果你只想在前一个成功后才执行每个命令，那么使用 `&&` 运算符将它们组合起来：

```bash
cd /my_folder && rm *.jar && svn co path to repo && mvn compile package install
```

如果其中一个命令失败，则不会执行其后的所有其他命令。

如果你想不管前一个是否失败都执行所有命令，请用分号分隔它们：

```bash
cd /my_folder; rm *.jar; svn co path to repo; mvn compile package install
```

在你的情况下，我认为你想要第一种情况，即下一个命令的执行取决于前一个的成功。

你也可以将所有命令放在脚本中并执行该脚本：

```bash
#! /bin/sh
cd /my_folder \
&& rm *.jar \
&& svn co path to repo \
&& mvn compile package install
```

有用资源：

- [在一行中执行组合多个 Linux 命令（原版）](https://stackoverflow.com/questions/13077241/execute-combine-multiple-linux-commands-in-one-line)

</details>

<details>
<summary><b>你可以向 <code>chmod</code> 传递什么符号表示，以在不影响其他权限的情况下给所有用户执行访问权限？</b></summary><br>

```bash
chmod a+x /path/to/file
```

- `a` - 用于所有用户
- `x` - 用于执行权限
- `r` - 用于读取权限
- `w` - 用于写入权限

有用资源：
- [如何使用 chmod 设置文件权限](https://www.washington.edu/computing/unix/permissions.html)
- [`chmod +x your_file_name` 做什么，我如何使用它？](https://askubuntu.com/questions/443789/what-does-chmod-x-filename-do-and-how-do-i-use-it)

</details>

<details>
<summary><b>我如何同步两个本地目录？</b></summary><br>

要将 **dir1** 的内容同步到同一系统上的 **dir2**，请输入：

```bash
rsync -av --progress --delete dir1/ dir2
```

- `-a`, `--archive` - 归档模式
- `--delete` - 删除目标目录中多余的文件
- `-v`, `--verbose` - 详细模式（增加详细程度）
- `--progress` - 显示传输进度

有用资源：

- [我如何同步两个本地目录？（原版](https://unix.stackexchange.com/questions/392536/how-can-i-sync-two-local-directories)
- [使用 rsync 同步文件夹](https://www.jveweb.net/en/archives/2010/11/synchronizing-folders-with-rsync.html)

</details>

<details>
<summary><b>许多基本维护任务要求你编辑配置文件。解释撤销你所做更改的方法。</b></summary><br>

- 在编辑之前手动备份文件（使用大括号扩展，如：`cp filename{,.orig}`）
- 手动复制存储文件的目录结构（例如 `cp`, `rsync` 或 `tar`）
- 在你的编辑器中制作原始文件的备份（例如，在你的编辑器配置文件中设置规则）
- 最好的解决方案是使用 `git`（或其他任何版本控制工具）来跟踪配置文件（例如 `/etc` 目录的 `etckeeper`）

有用资源：

- [在文件名扩展之前用 .bak 备份文件](https://unix.stackexchange.com/questions/66376/backup-file-with-bak-before-filename-extension)
- [使用 git 进行配置文件版本控制是个好主意吗？](https://superuser.com/questions/1037211/is-it-a-good-idea-to-use-git-for-configuration-file-version-controlling)

</details>

<details>
<summary><b>你必须找到所有大于 20MB 的文件。你如何做到这一点？</b></summary><br>

```bash
find / -type f -size +20M
```

有用资源：

- [我如何查找比 x 字节大/小的文件？](https://superuser.com/questions/204564/how-can-i-find-files-that-are-bigger-smaller-than-x-bytes)

</details>

<details>
<summary><b>为什么我们使用 <code>sudo su -</code> 而不是仅仅 <code>sudo su</code>？</b></summary><br>

`sudo` 在大多数现代 Linux 发行版中，（但并非总是）root 用户被禁用且没有设置密码。因此，你不能通过 `su` 切换到 root 用户（你可以试试）。你必须以 root 特权调用 `sudo`：`sudo su`。

`su` 只是切换用户，提供一个与旧用户几乎相同环境的普通 shell。

`su -` 在切换用户后调用登录 shell。登录 shell 会重置大多数环境变量，提供一个干净的基线。

有用资源：

- [su vs sudo -s vs sudo -i vs sudo bash](https://unix.stackexchange.com/questions/35338/su-vs-sudo-s-vs-sudo-i-vs-sudo-bash)
- [为什么我们使用 su - 而不是仅仅 su？（原版）](https://unix.stackexchange.com/questions/7013/why-do-we-use-su-and-not-just-su)

</details>

<details>
<summary><b>如何查找在过去 60 分钟内修改过的系统上的文件？</b></summary><br>

```bash
find / -mmin -60 -type f
```

有用资源：

- [获取目录中最后 30 天修改的所有文件（原版）](https://stackoverflow.com/questions/23070245/get-all-files-modified-in-last-30-days-in-a-directory)

</details>

<details>
<summary><b>保留旧日志文件的主要原因是什么？</b></summary><br>

它们是调查系统问题所必需的。**日志管理**对于 IT 安全至关重要。

服务器、防火墙和其他 IT 设备会保留记录重要事件和事务的日志文件。这些信息可以提供有关影响你网络的内部和外部的敌对活动的重要线索。日志数据还可以提供用于识别和排除设备问题的信息，包括配置问题和硬件故障。

这是你的服务器的记录，记录了谁访问了你的站点，何时访问，以及他们确切查看了哪些内容。它非常详细，显示了：

- 人们来自哪里
- 他们使用的浏览器
- 他们查看的确切文件
- 加载每个文件花了多长时间
- 以及一大堆其他极客的东西

需要考虑的因素：

- 保留或销毁的法律要求
- 公司关于保留和销毁的政策
- 日志有用的时间长度
- 你希望从日志中回答的问题
- 它们占用了多少空间

通过收集和记录日志，你可以了解网络内发生的情况。每个日志文件包含许多有价值的信息片段，特别是如果你知道如何阅读和分析它们的话。

有用资源：

- [你保留日志文件多久？](https://serverfault.com/questions/135365/how-long-do-you-keep-log-files)

</details>

<details>
<summary><b>什么是增量备份（Incremental Backup）？</b></summary><br>

增量备份是一种只复制自上次备份以来更改过的文件的备份类型。

有用资源：

- [什么是增量备份？](https://www.nakivo.com/blog/what-is-incremental-backup/)

</details>

<details>
<summary><b>什么是 RAID？RAID0, RAID1, RAID5, RAID6, RAID10 是什么？ </b></summary><br>

**RAID**（廉价磁盘冗余阵列）是一种用于提高数据存储性能和/或可靠性的技术。

- **RAID0**: 也称为磁盘**条带化**，是一种将文件拆分并将数据分散到 RAID 组中所有驱动器上的技术。没有针对故障的保护措施
- **RAID1**: 一种流行的磁盘子系统，通过在两个驱动器上写入相同的数据来提高安全性。称为“**镜像**”，RAID 1 不会提高写入性能，但读取性能可能等于每个磁盘性能的总和。然而，如果一个驱动器发生故障，将使用第二个驱动器，并手动更换故障驱动器。更换后，RAID 控制器会将工作驱动器的内容复制到新驱动器上
- **RAID5**: 这是一种通过计算奇偶校验数据并通过在三个或更多驱动器之间交错数据来提高速度的磁盘子系统（**条带化**）。在一个驱动器发生故障时，后续读取可以从分布的奇偶校验中计算出来，这样就不会丢失任何数据
- **RAID6**: RAID 6 通过在另一个奇偶校验块上扩展 RAID 5。它需要至少四个磁盘，并且可以继续执行并发磁盘故障的任何两个读写操作。RAID 6 对读操作没有性能损失，但由于与奇偶校验计算相关的开销，它对写操作有性能损失
- **RAID10**: 也称为 **RAID 1+0**，是一种结合磁盘镜像和磁盘条带化以保护数据的 RAID 配置。它需要至少四个磁盘，并在镜像对之间条带化数据。只要每个镜像对中有一个驱动器功能正常，就可以检索数据。如果同一镜像对中的两个驱动器发生故障，所有数据都将丢失，因为条带集没有奇偶校验

有用资源：

- [RAID](https://www.prepressure.com/library/technology/raid)

</details>

<details>
<summary><b>如何确定用户的默认组？你会如何更改它？ </b></summary><br>

```bash
useradd -m -g initial_group username
```

`-g/--gid`: 定义用户初始登录组的组名或编号。如果指定，则必须存在该组名；如果提供了组号，则必须引用已存在的组。

如果未指定，`useradd` 的行为将取决于 `/etc/login.defs` 中包含的 `USERGROUPS_ENAB` 变量。默认行为（`USERGROUPS_ENAB yes`）是创建一个与用户名同名的组，**GID** 等于 **UID**。

有用资源：

- [我如何在 Linux 中更改用户的默认组？](https://unix.stackexchange.com/questions/26675/how-can-i-change-a-users-default-group-in-linux)

</details>

<details>
<summary><b>你最喜欢的用于日常工作和脚本编写的命令行文本编辑器是什么？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>为什么要在机架中安装服务器？</b></summary><br>

- 保护硬件
- 适当的冷却
- 有序的工作空间
- 更好的电源管理
- 更清洁的环境

有用资源：

- [将 PC 机架安装的 5 个理由](https://www.racksolutions.com/news/custom-projects/5-reasons-to-rackmount-pc/)

</details>

###### 网络问题 (23)

<details>
<summary><b>给我画一个简单的网络图：你有 20 台系统，1 个路由器，4 个交换机，5 台服务器和一个小型 IP 块。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>关于 OSI（或任何其他）模型，最重要的事情是什么？</b></summary><br>

关于 **OSI**（或其他任何）模型最重要的事情是：

- 我们可以将协议划分为层
- 层提供封装
- 层提供抽象
- 层将功能与其他功能解耦

有用资源：

- [OSI 模型与网络协议的关系](https://networkengineering.stackexchange.com/questions/6380/osi-model-and-networking-protocols-relationship)

</details>

<details>
<summary><b>VLAN 和子网有什么区别？你需要 VLAN 来设置子网吗？</b></summary><br>

**VLANs** 和 **子网**解决不同的问题。**VLANs** 在 Layer 2（数据链路层）工作，从而改变广播域（例如）。而 **子网**在当前上下文中是 Layer 3（网络层）。

**子网** - 是由地址的一部分（通常称为网络地址）和子网掩码（netmask）确定的 IP 地址范围。例如，如果 netmask 是 `255.255.255.0`（或简写为 `/24`），并且网络地址是 `192.168.10.0`，那么这就定义了一个 IP 地址范围 `192.168.10.0` 到 `192.168.10.255`。简写为 `192.168.10.0/24`。

**VLAN** - 思考这一点的好方法是“交换机分区”。假设你有一个 8 端口的可 VLAN 化交换机。你可以将 4 个端口分配给一个 **VLAN**（例如 `VLAN 1`），将 4 个端口分配给另一个 **VLAN**（例如 `VLAN 2`）。`VLAN 1` 不会看到任何来自 `VLAN 2` 的流量，反之亦然。从逻辑上讲，你现在有两个单独的交换机。通常在交换机上，如果交换机没有看到 MAC 地址，它会将流量“泛洪”到所有其他端口。**VLANs** 防止了这种情况。

子网不过是帮助主机在 Layer 2 和 Layer 3 上进行通信的 IP 地址范围。每个子网不需要自己的 **VLAN**。**VLANs** 用于隔离（是 Layer 2 通信的沙箱，不同 **VLAN** 的两个系统不能通信，但可以通过 **VLAN 间路由**完成），便于管理和安全。

有用资源：

- [VLAN 和子网有什么区别？（原版）](https://superuser.com/questions/353664/what-is-the-difference-between-a-vlan-and-a-subnet)
- [用于网络安全和分段的 VLANS vs. 子网](https://networkengineering.stackexchange.com/questions/46899/vlans-vs-subnets-for-network-security-and-segmentation)

</details>

<details>
<summary><b>列出你应该知道的 5 个常见网络端口。</b></summary><br>

<table style="width:100%">
  <tr>
    <th>服务</th>
    <th>端口</th>
  </tr>
  <tr>
    <td>SMTP</td>
    <td>25</td>
  </tr>
  <tr>
    <td>FTP</td>
    <td>数据传输使用 20，连接建立使用 21</td>
  </tr>
  <tr>
    <td>DNS</td>
    <td>53</td>
  </tr>
  <tr>
    <td>DHCP</td>
    <td>DHCP 服务器使用 67/UDP，DHCP 客户端使用 68/UDP</td>
  </tr>
  <tr>
    <td>SSH</td>
    <td>22</td>
  </tr>
</table>

有用资源：

- [Red Hat Enterprise Linux 4: 安全指南 - 常见端口](https://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-ports.html)

</details>

<details>
<summary><b>POP 和 IMAP 是什么，以及如何选择你应该实施哪一个？</b></summary><br>

POP 和 IMAP 都是用于从邮件服务器检索消息到邮件客户端的协议。

**POP**（邮局协议）使用从邮件服务器到客户端的单向推送。默认情况下，这会将消息发送到 POP 邮件客户端并从邮件服务器上删除它们，尽管可以配置邮件服务器以保留所有消息。你在邮件客户端中对消息采取的任何操作（标记、删除、移动到文件夹）都不会反映在邮件服务器上，因此无法被其他从邮件服务器拉取消息的邮件客户端访问。POP 在邮件服务器上占用很少的存储空间，并且由于消息只存在于一个邮件客户端而不是邮件服务器和多个客户端上，因此可以被视为更安全。

**IMAP**（互联网消息访问协议）使用邮件服务器和客户端之间的双向通信。在你配置为 IMAP 的邮件客户端中删除或标记一条消息也将删除或标记邮件服务器上的该消息。当跨不同客户端或设备访问邮件时，IMAP 允许提供类似的体验，因为消息可以存在于多个设备上并保持相同的状态。IMAP 还可以通过选择性同步消息来节省邮件客户端上的磁盘空间，从邮件客户端删除旧消息，因为它可以在需要时稍后从邮件服务器同步它们。

如果你需要在多个设备上访问消息并希望节省客户端设备上的磁盘空间，请选择 IMAP。如果你想节省邮件服务器上的磁盘空间，仅从一个客户端设备访问消息并确保消息不存在于多个系统上，请选择 POP。

</details>

<details>
<summary><b>如何检查默认路由和路由表？</b></summary><br>

使用命令 `netstat -nr`, `route -n` 或 `ip route show` 我们可以查看默认路由和路由表。

有用资源：

- [如何在 linux 中检查路由（路由表）](https://howto.lintel.in/how-to-check-routes-routing-table-in-linux/)
- [FreeBSD 设置默认路由/网关](https://www.cyberciti.biz/faq/freebsd-setup-default-routing-with-route-command/)

</details>

<details>
<summary><b>127.0.0.1 和 localhost 之间有什么区别？</b></summary><br>

嗯，最可能的区别是你仍然必须在某处实际查找 localhost。

如果你使用 `127.0.0.1`，那么（智能）软件会直接将其转换为 IP 地址并使用它。某些 `gethostbyname` 的实现将检测点分格式（以及等效的 IPv6 格式），根本不进行查找。

否则，必须解析该名称。而且不能保证你的 hosts 文件实际上会被用于该解析（首先或无论如何），所以 localhost 可能变成一个完全不同的 IP 地址。

我的意思是，在某些系统上，可以绕过本地 hosts 文件。`host.conf` 文件在 Linux（以及许多其他 Unix）上控制这一点。

如果你使用 Unix 域套接字，它比使用 TCP/IP 稍快一些（因为你拥有的开销较少）。Windows 默认使用 TCP/IP，而 Linux 在你选择 localhost 时尝试使用 Unix 域套接字，而在你选择 `127.0.0.1` 时使用 TCP/IP。

有用资源：

- [127.0.0.1 和 localhost 之间有什么区别？](https://stackoverflow.com/questions/7382602/what-is-the-difference-between-127-0-0-1-and-localhost)
- [localhost vs. 127.0.0.1](https://stackoverflow.com/questions/3715925/localhost-vs-127-0-0-1)

</details>

<details>
<summary><b><code>ping</code> 命令使用哪个端口？</b></summary><br>

`ping` 使用 **ICMP**，特别是 **ICMP echo request**（回显请求）和 **ICMP echo reply**（回显应答）数据包。没有与 **ICMP** 关联的“端口”。端口与两个 IP 传输层协议 TCP 和 UDP 相关联。**ICMP**, TCP, 和 UDP 是“兄弟”；它们不是基于彼此的，而是三个独立的协议，运行在 IP 之上。

**ICMP** 数据包由 IP 数据报头中的“协议”字段标识。**ICMP** 不使用 UDP 或 TCP 通信服务，它使用原始 IP 通信服务。这意味着 **ICMP** 消息直接承载在 IP 数据报数据字段中。`raw` 来自软件实现的方式，要创建和发送 **ICMP** 消息，人们打开一个 `raw` 套接字，构建包含 **ICMP** 消息的缓冲区，然后将包含该消息的缓冲区写入原始套接字。

**ICMP** 的 IP 协议值为 1。协议字段是 IP 头的一部分，用于标识 IP 数据报数据部分中的内容。

然而，你可以使用 `nmap` 来查看端口是否打开：

```bash
nmap -p 80 example.com
```

有用资源：

- [Ping 端口号](https://networkengineering.stackexchange.com/questions/42463/ping-port-number)
- [是否可以 ping 地址:端口？](https://superuser.com/questions/769541/is-it-possible-to-ping-an-addressport)

</details>

<details>
<summary><b>服务器 A 无法与服务器 B 通信。用几步描述可能的原因。</b></summary><br>

要排查服务器之间的通信问题，最好理想地遵循 TCP/IP 栈：

1. **应用层**：两个服务器上的服务是否正在运行？它们是否正确配置（例如绑定正确的 IP 和端口）？应用程序和系统日志是否显示有意义的错误？
2. **传输层**：应用程序使用的端口是否打开（试试 telnet！）？可以 ping 通该服务器吗？
3. **网络层**：网络上或操作系统上是否有正确配置的防火墙？IP 栈是否正确配置（IP、路由、dns 等）？交换机和路由器工作正常吗（检查 ARP 表！）？
4. **物理层**：服务器是否连接到网络？数据包是否在丢失？

</details>

<details>
<summary><b>为什么你的服务器上的主机名无法解析？修复此问题。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>如何使用 CLI 使用外部 dns 解析域名？IP 可以解析为域名吗？</b></summary><br>

将 IP 地址解析为域名的示例：

```bash
# 使用 host 命令:
host domain.com 8.8.8.8

# 使用 dig 命令:
dig @9.9.9.9 google.com

# 使用 nslookup 命令:
nslookup domain.com 8.8.8.8
```

你可以（有时）将 IP 地址解析回主机名。IP 地址可以存储在 **PTR** 记录中。然后你可以执行：

```bash
dig A <hostname>
```

查找主机的 IPv4 地址，或者：

```bash
dig AAAA <hostname>
```

查找主机的 IPv6 地址，或者：

```bash
dig PTR ZZZ.YYY.XXX.WWW.in-addr.arpa.
```

查找 IPv4 地址 `WWW.XXX.YYY.ZZZ` 的主机名（注意八位字节是反向的），或者：

```bash
dig PTR b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa.
```

有用资源：

- [我如何在 Bash 脚本中将主机名解析为 IP 地址？](https://unix.stackexchange.com/questions/20784/how-can-i-resolve-a-hostname-to-an-ip-address-in-a-bash-script)
- [如何将 IP 地址解析为域名？](https://superuser.com/questions/315687/how-to-resolve-ip-addresses-to-domain-names)

</details>

<details>
<summary><b>如何使用 <code>telnet</code> 或 <code>nc</code> 测试端口连通性？</b></summary><br>

```bash
# 使用 telnet 命令:
telnet code42.example.com 5432

# 使用 nc (netcat) 命令:
nc -vz code42.example.com 5432
```

</details>

<details>
<summary><b>为什么你应该避免使用 <code>telnet</code> 远程管理系统？</b></summary><br>

现代操作系统默认关闭了所有潜在不安全的服务。另一方面，一些网络设备供应商仍然允许使用 telnet 协议建立通信。

**Telnet** 使用最不安全的通信方法。它以纯文本格式通过网络发送数据，任何人都可以使用网络工具轻松找出密码。

在 **Telnet** 的情况下，这包括以明文形式传递登录凭据，这意味着任何在你的网络上运行嗅探器的人都可以只需几秒钟就能通过窃听 **Telnet** 登录会话找到他需要控制设备的信息。

有用资源：

- [Telnet 和 SSH 作为安全替代方案](https://www.ssh.com/ssh/telnet)
- [如何 telnet 到特定端口的 IP 地址？](https://superuser.com/questions/339107/how-to-telnet-to-an-ip-address-on-a-specific-port)

</details>

<details>
<summary><b><code>wget</code> 和 <code>curl</code> 有什么区别？</b></summary><br>

主要区别是：与 `curl` 相比，`wget` 的主要强项是其递归下载能力。`wget` 仅命令行使用。`curl` 支持 FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, POP3, IMAP, SMTP, RTMP 和 RTSP。

有用资源：

- [curl 和 wget 之间有什么区别？（原版）](https://unix.stackexchange.com/questions/47434/what-is-the-difference-between-curl-and-wget)

</details>

<details>
<summary><b>什么是 SSH，它是如何工作的？</b></summary><br>

**SSH** 代表 **Secure Shell**。它是一种协议，允许你从服务器“A”进入到一个服务器“B”的 shell 会话。它允许你与你的服务器“B”进行交互。

要建立 **SSH** 连接，远程机器（服务器 A）必须运行一个称为 **SSH** 守护进程的软件，而用户的计算机（服务器 B）必须有 **SSH** 客户端。

**SSH** 守护程序和 **SSH** 客户端在特定网络端口（默认 22）上监听连接请求，验证连接请求，并在用户提供正确的凭据时生成适当的环境。

有用资源：

- [了解 SSH 加密和连接过程](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)

</details>

<details>
<summary><b>大多数教程建议使用 SSH 密钥认证而不是密码认证。为什么这被认为更安全？</b></summary><br>

**SSH 密钥**是 SSH 协议中的访问凭证。它的功能类似于用户名和密码，但密钥主要用于自动化流程以及由系统管理员和高级用户实施的单点登录（SSO）。

与其要求用户的密码，也可以使用非对称加密算法来确认客户端的身份，使用公钥和私钥。

如果你的 SSH 服务仅允许公钥认证，攻击者需要拥有存储在服务器上的公钥对应的私钥副本。

如果你的 SSH 服务允许基于密码的认证，那么你的互联网连接的 SSH 服务器将被试图猜测用户名和密码的僵尸网络日夜轰炸。僵尸网不需要任何信息，它只是尝试流行的名称和流行的密码。除此之外，这还会堵塞你的日志。

有用资源：

- [基于密钥的认证（公钥认证）](http://www.crypto-it.net/eng/tools/key-based-authentication.html)
- [SSH 密码与密钥认证](https://security.stackexchange.com/questions/33381/ssh-password-vs-key-authentication)

</details>

<details>
<summary><b>什么是包过滤器，它是如何工作的？</b></summary><br>

**包过滤**是一种防火墙技术，用于通过监控传出和传入的数据包并根据源和目标互联网协议（IP）地址、协议和端口允许它们通过或阻止来控制网络访问。

当安全要求适中时，包过滤是合适的。许多组织的内部（私有）网络并没有高度分段。将组织的一部分与另一部分隔离开来并不需要非常复杂的防火墙。

然而，为生产网络提供某种保护免受实验室或实验网络的侵害是明智的。包过滤设备是为提供一个子网与另一个子网的隔离而提供的非常适当的措施。

在网络层和 TCP/IP 协议栈的传输层运行，每个数据包在进入协议栈时都会被检查。网络和传输头被仔细检查以下信息：

- **协议（IP 头，网络层）** - 在 IP 头中，第 9 个字节（记住字节计数从零开始）标识数据包的协议。大多数过滤设备能够区分 TCP、UDP 和 ICMP。
- **源地址（IP 头，网络层）** - 源地址是创建该数据包的主机的 32 位 IP 地址。
- **目的地址（IP 头，网络层）** - 目的地址是该数据包 destined for 的主机的 32 位 IP 地址。
- **源端口（TCP 或 UDP 头，传输层）** - TCP 或 UDP 网络连接的两端都绑定到一个端口。TCP 端口与 UDP 端口分开且不同。编号低于 1024 的端口保留——它们有特定定义的用途。编号高于 1024（含）的端口被称为临时端口。供应商可以选择如何使用它们。有关“知名”端口的列表，请参阅 RFP1700。源端口是一个伪随机分配的临时端口号。因此，在源端口上进行过滤通常不是很有用。
- **目的端口（TCP 或 UDP 头，传输层）** - 目的端口号指示数据包发送到的端口。目标主机上的每个服务都在监听一个端口。一些可能被过滤的知名端口是 20/TCP 和 21/TCP - ftp 连接/数据，23/TCP - telnet，80/TCP - http，以及 53/TCP - DNS 区域传输。
- **连接状态（TCP 头，传输层）** - 连接状态告诉数据包是否是网络会话的第一个数据包。如果这是会话中的第一个数据包，则 TCP 头中的 ACK 位设置为“false”或 0。通过拒绝或删除任何具有将 ACK 位设置为“false”或 0 的数据包来禁止主机建立连接很简单。

有用资源：

- [构建互联网防火墙 - 包过滤](http://web.deu.edu.tr/static/oreily/networking/firewall/ch06_01.htm)

</details>

<details>
<summary><b>使用反向代理服务器的优势是什么？</b></summary><br>

**隐藏你的后端服务器的拓扑和特征**

**反向代理服务器**可以隐藏源服务器的存在和特征。它充当互联网云和 Web 服务器之间的中间人。出于安全原因，这很好，特别是当你使用 Web 托管服务时。

**允许对后端服务器进行透明维护**

你对运行在反向代理后面的服务器所做的更改对你的最终用户来说将是完全透明的。

**负载均衡**

然后，反向代理将强制执行一种负载均衡算法，如轮询、加权轮询、最少连接数、加权最少连接数或随机，以分发集群中服务器的负载。

当一台服务器宕机时，系统将自动故障转移到下一台服务器，用户可以继续他们的安全文件传输活动。

**SSL 卸载/终止**

处理传入的 HTTPS 连接，解密请求并将未加密的请求传递给 Web 服务器。

**IP 掩码**

使用单个 IP 但不同的 URL 路由到不同的后端服务器。

有用资源：

- [反向代理的好处](https://dzone.com/articles/benefits-reverse-proxy)

</details>

<details>
<summary><b>路由器（Router）和网关（Gateway）有什么区别？默认网关是什么？</b></summary><br>

**路由器**描述了通用技术功能（Layer-3 转发）或旨在用于该目的的硬件设备，而网关描述本地段的函数（提供与其他地方的连接）。你也可以说“_你设置一个路由器作为网关_”。另一个术语是跳（hop），它描述了子网之间的转发。

术语 **默认网关**是指你的 LAN 上的路由器，负责成为与 LAN 外部的计算机通信的流量接触的第一个点。

这只是视角的问题，设备是一样的。

有用资源：

- [路由器和网关的区别（原版）](https://networkengineering.stackexchange.com/questions/51426/difference-between-router-and-gateway)

</details>

<details>
<summary><b>解释以下每个 DNS 记录的功能：SOA, PTR, A, MX, 和 CNAME。</b></summary><br>

**DNS 记录**基本上是映射文件，告诉 DNS 服务器每个域关联哪个 IP 地址，以及如何处理发送到每个域的请求。几乎所有 DNS 记录配置中常用的 **DNS 记录**语法是 `A`, `AAAA`, `CNAME`, `MX`, `PTR`, `NS`, `SOA`, `SRV`, `TXT` 和 `NAPTR`。

- **SOA** - 权威起始记录 (Start Of Authority)
- **A** - 地址映射记录
- **AAAA** - IP 版本 6 地址记录
- **CNAME** - 规范名称记录
- **MX** - 邮件交换记录
- **NS** - 域名服务器记录
- **PTR** - 反向查找指针记录

有用资源：

- [DNS 记录类型列表](https://en.wikipedia.org/wiki/List_of_DNS_record_types)

</details>

<details>
<summary><b>为什么不能使用 MAC 地址而不是 IPv4/6 进行网络通信？</b></summary><br>

**OSI** 模型解释了为什么基于物理的 **Layer 2** 机制做出路由（一个 **Layer 3** 概念）决定没有意义。

现代 networking 被分解为许多不同的层，以完成你的端到端通信。你的网卡（mac 地址寻址的东西 - 物理地址）只需要负责与其物理网络上的对等方进行通信。

你允许使用 **MAC** 地址完成的通信将仅限于与你机器物理接触内的其他设备。例如，在互联网上，你没有与每台机器物理连接。这就是为什么我们需要在需要与我们没有物理连接的机器进行通信时使用 **TCP/IP**（一个 **Layer 3**，逻辑地址）机制的原因。

**IP** 是一种以分层方式强加在一组计算机上的任意编号方案，以便将它们逻辑地区分为一组（那就是子网的作用）。在这些组之间发送消息是通过路由表完成的，它们本身被划分为多个级别，这样我们就不必跟踪每个单个子网。

这也很容易与另一对系统联系起来。你有一个州颁发的身份证号码，为什么如果该 ID 号码对你来说是唯一的，还需要一个邮寄地址？你需要邮寄地址，因为它是描述你应该将通信的唯一目的地发送到的任意系统。

另一方面，**MAC** 地址在网络上的分布是随机的，与拓扑完全无关。路由分组是不可能的，每个路由器都需要跟踪通过它转发流量的每个单个设备的路由。这就是 **Layer 2** 交换机所做的，并且这在超过一定数量的主机时扩展性不好。

有用资源：

- [为什么不能使用 MAC 地址而不是 IPv4|6 进行网络通信？（原版）](https://serverfault.com/questions/410626/why-couldnt-mac-addresses-be-used-instead-of-ipv46-for-networking)

</details>

<details>
<summary><b>可以应用于包含多达 30 台设备的网络的最小 IPv4 子网掩码是什么？</b></summary><br>

无论你是为终端用户拥有标准的 `/24` VLAN，还是点对点链路的 `/30`，或者介于两者之间并且必须包含多达 30 台设备的子网算出来是 `/27`——或者是 `255.255.255.224` 的子网掩码。

有用资源：

- [你如何计算前缀、网络、子网和主机号？](https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the-prefix-network-subnet-and-host-numbers)
- [IP 地址后的斜杠 - CIDR 表示法](https://networkengineering.stackexchange.com/questions/3697/the-slash-after-an-ip-address-cidr-notation)
- [为什么有 3 个私有 IPv4 地址范围？](https://networkengineering.stackexchange.com/questions/32119/why-are-there-3-ranges-of-private-ipv4-addresses)
- [IP 计算器](http://jodies.de/ipcalc)

</details>

<details>
<summary><b>一些常见的 HTTP 状态码是什么？</b></summary><br>

- **1xx** - 信息性响应 - 通信传输协议级别的信息
- **2xx** - 成功 - 表明客户端的请求被成功接受
- **3xx** - 重定向 - 表明客户必须采取一些额外行动才能完成他们的请求
- **4xx** - 客户端错误 - 这一类错误状态码指向客户端
- **5xx** - 服务器端错误 - 服务器承担这些错误状态码的责任

有用资源：

- [HTTP 状态码](https://httpstatuses.com/)

</details>

###### Devops 问题 (5)

<details>
<summary><b>什么是 DevOps？对于任何 DevOps 社区的成功来说，人们如何沟通还是你选择部署的工具更重要？***</b></summary><br>

**DevOps** 是一个参与开发和运维任务的 cohesive team（协作团队），或者是紧密合作的个体运维和开发团队。这更像是一种与其他部门合作以实现共同目标的“方式”。

</details>

<details>
<summary><b>什么是版本控制？你的提交消息好看吗？</b></summary><br>

它是一个系统，记录文件或一组文件随时间的变化，以便你以后可以回忆特定版本。版本控制系统由一个中央共享存储库组成，团队成员可以在其中提交对文件或一组文件的更改。然后你可以提到版本控制的用途。

版本控制允许你：

- 将文件恢复到以前的状态
- 将整个项目恢复到以前的状态
- 比较随时间的变化
- 查看最后修改了可能导致问题的内容的谁
- 谁引入了问题以及何时引入

伟大提交消息的七条规则：

- 用空行分隔主题和正文
- 将主题限制为 50 个字符
- 大写主题行
- 不要在主题行末尾加句号
- 在主题行中使用祈使语气
- 在 72 个字符处换行正文
- 使用正文解释“什么”和“为什么”，而不是“如何”

有用资源：

- [入门 - 关于版本控制（原版）](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

</details>

<details>
<summary><b>解释一些基本的 <code>git</code> 命令。</b></summary><br>

- `git init` - 创建一个新的本地存储库
- `git commit -m "message"` - 将更改提交到 head
- `git status` - 列出你已添加的文件与 `git add`，以及自那时以来已更改的任何文件
- `git push origin master` - 将更改发送到远程存储库的主分支

</details>

<details>
<summary><b>解释一个简单的持续集成（CI）流水线。</b></summary><br>

- 克隆存储库
- 部署阶段 (QA)
- 测试环境 (QA)
- 部署阶段 (PROD)

</details>

<details>
<summary><b>解释一些基本的 <code>docker</code> 命令。</b></summary><br>

- `docker ps` - 显示正在运行的容器
- `docker ps -a` - 显示所有容器
- `docker images` - 显示 docker 镜像
- `docker logs <container-id|container-name>` - 从容器中获取日志
- `docker network ls` - 显示所有 docker 网络
- `docker volumes ls` - 显示所有 docker 卷
- `docker exec -it <container-id|container-name> bash` - 在具有交互式 shell 的容器中执行 bash

</details>

###### 网络安全问题 (1)

<details>
<summary><b>什么是安全配置错误（Security Misconfiguration）？</b></summary><br>

**安全配置错误**是一种漏洞，当设备/应用程序/网络以可以被攻击者利用的方式来配置时。这可以简单到保持默认用户名/密码不变或对于设备账户等过于简单。

</details>

### :diamond_shape_with_a_dot_inside: <a name="regular-sysadmin">中级系统管理员</a>

###### 系统问题 (60)

<details>
<summary><b>谈谈你在生产环境中的经验？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>你会选择哪个发行版来运行大型 Web 服务器？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>用几点解释 Linux 系统的启动过程。</b></summary><br>

**BIOS**: BIOS 的全称是基本输入输出系统，它执行完整性检查并将搜索和加载引导加载程序然后执行。

**Bootloader (引导加载程序)**: 由于早期阶段与操作系统无关，基于 BIOS 的 x86 和 x86-64 架构的启动过程被认为是在真实模式下执行主引导记录（MBR）代码并加载第一阶段引导加载程序时开始的。在 UEFI 系统中，可以执行有效负载，例如 Linux 内核。因此不需要引导加载程序。一些流行的引导加载程序：**GRUB**, **Syslinux/Isolinux** 或 **Lilo**。

**Kernel (内核)**: Linux 中的内核处理所有操作系统进程，如内存管理、任务调度、I/O、进程间通信和整体系统控制。这是分两个阶段加载的——在第一阶段，内核（作为压缩映像文件）被加载到内存中并解压缩，并且设置了一些基本功能，如基本内存管理。

**Init**: 它是系统中所有进程的父进程，由内核执行并负责启动所有其他进程。

- `SysV init` - init 的工作是“一旦内核完全运行，让一切按应有的方式运行”。本质上它建立和操作用户空间的全部范围。这包括检查和挂载文件系统、启动必要的用户服务，并最终在系统启动完成时切换到用户环境。
- `systemd` - systemd 的开发人员旨在取代从 Unix System V 继承的 Linux init 系统。像 init 一样，systemd 是一个管理其他守护进程的守护进程。所有守护程序，包括 systemd，都是后台进程。Systemd 是第一个启动的守护进程（在引导期间）和最后一个终止的守护进程（在关机时）。
- `runinit` - runinit 是一种用于类 Unix 操作系统的 init 方案，它在整个操作系统中初始化、监督和结束进程。它是 daemontools 进程监督工具包的重新实现，运行在 Linux, Mac OS X, \*BSD 和 Solaris 操作系统上。

有用资源：

- [分析 Linux 启动过程](https://opensource.com/article/18/1/analyzing-linux-boot-process)
- [Systemd 引导过程在 Linux 中的近距离观察](https://linoxide.com/linux-how-to/systemd-boot-process/)

</details>

<details>
<summary><b>Linux 守护进程如何以及为什么降低权限？为什么一些守护进程需要 root 权限才能启动？解释。***</b></summary>

待补充。

</details>

<details>
<summary><b>为什么在单核机器上负载为 1.00 并不理想？</b></summary><br>

负载为 1.00 的问题是，你没有余量。在实践中，许多系统管理员会在 0.70 处画一条线。

“需要调查”的经验法则：0.70 如果你的负载平均值保持在 > 0.70，那么在情况变得更糟之前进行调查是时候了。

“立即修复”的经验法则：1.00。如果你的负载平均值保持在 1.00 以上，找出问题并立即解决它。否则，你将在半夜被叫醒，而且那将不会很有趣。

经验法则：5.0。如果你的负载平均值高于 5.00，你可能会遇到严重的问题，你的机器要么挂起要么速度大幅下降，而这会在最糟糕的时间发生（例如在半夜或当你正在会议上演示时）。不要让事情发展到那个地步。

有用资源：

- [正确解释 4 核 8 线程处理器上的系统负载](https://serverfault.com/questions/618130/proper-way-of-interpreting-system-load-on-a-4-core-8-thread-processor)
- [理解 Linux CPU 负载 - 什么时候你应该担心？](http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages)

</details>

<details>
<summary><b>当有效用户是 root，但真实用户 ID 仍然是你的名字时，这意味着什么？</b></summary><br>

**真实用户 ID (RUID)** 是你真正是谁（拥有该进程的用户），而 **有效用户 ID (EUID)** 是操作系统用来决定你是否被允许做某事的东西（大多数时候有一些例外）。

当你登录时，登录 shell 将 **真实和有效用户 ID** 都设置为密码文件提供的相同值（你的 **真实用户 ID**）。

例如，如果你执行 setuid，并且除了以另一个用户（例如 **root**）身份运行之外，setuid 程序还应该代表你做某事。

在执行 setuid 之后，它将拥有你的 **真实 ID**（因为你是进程所有者）和文件所有者的有效用户 id（例如 **root**），因为它被设置为 setuid。

让我们使用 `passwd` 的情况：

```bash
-rwsr-xr-x 1 root root 45396 may 25  2012 /usr/bin/passwd
```

当 user2 想要更改他们的密码时，他们执行 `/usr/bin/passwd`。

**RUID** 将是 user2，但该进程的 **EUID** 将是 root。

user2 只能使用 passwd 来更改自己的密码，因为内部 passwd 检查 **RUID**，如果不是 root，其操作将限于真实用户的密码。

在 `passwd` 的情况下，**EUID** 必须变为 root，因为该进程需要写入 `/etc/passwd` 和/或 `/etc/shadow`。

有用资源：

- [真实用户 ID、有效用户 ID 和保存用户 ID 之间的区别？（原版）](https://stackoverflow.com/questions/30493424/what-is-the-difference-between-a-process-pid-ppid-uid-euid-gid-and-egid)
- [pid, ppid, uid, euid, gid 和 egid 之间有什么区别？](https://stackoverflow.com/questions/30493424/what-is-the-difference-between-a-pid-ppid-uid-euid-gid-and-egid)

</details>

<details>
<summary><b>开发人员添加了一个生成大量日志文件的 cron 作业。你如何防止它们变得如此之大？</b></summary><br>

使用 `logrotate` 是处理日志文件的常用方法。但是，你应该将你自己的任务添加到 `/etc/logrotate.d/` 而不是向 `/etc/logrotate.conf` 添加内容，否则在发布升级期间你将不得不查看更多的配置文件差异。

如果它正在被积极写入，你确实没有太多可以通过截断来做的事情。你唯一的选择是截断文件：

```bash
: >/var/log/massive-logfile
```

这非常有帮助，因为它会在不中断进程的情况下截断该文件。

有用资源：

- [如何使用 logrotate 管理日志文件](https://www.linode.com/docs/uptime/logs/use-logrotate-to-manage-log-files/)
- [系统日志记录](https://www.ibm.com/developerworks/library/l-lpic1-108-2/index.html)

</details>

<details>
<summary><b>Linux 内核如何在系统中创建、管理和删除进程？***</b></summary><br>

待补充。

有用资源：

- [Linux 进程](https://www.tldp.org/LDP/tlk/kernel/processes.html)

</details>

<details>
<summary><b>解释你可以在 <code>top</code> 和 <code>htop</code> 中看到的选定信息。如何使用这些工具诊断负载、高用户时间和内存不足问题？***</b></summary><br>

待补充。

有用资源：

- [以可视化方式解释 top](https://www.svennd.be/top-explained-visually/)
- [以可视化方式解释 htop](https://codeahoy.com/2017/01/20/hhtop-explained-visually/)
- [你可以从 Linux 上的 htop/top 看到的一切的解释](https://peteris.rocks/blog/htop/)

</details>

<details>
<summary><b>你如何识别一个正在占用资源的进程？ </b></summary><br>

`top` 工作得相当好，只要你查看正确的数字。
- **M** 按当前驻留内存使用量排序
- **T** 按总（或累积）CPU 使用量排序
- **P** 按当前 CPU 使用量排序（这是默认的刷新）
- **?** 显示所有 top 命令的使用摘要

这对于解决问题时获取计算机进程运行缓慢的有用信息以及决定杀死哪些进程/卸载什么软件非常重要。

有用资源：

- [如何找到占用机器资源的进程](https://superuser.com/questions/326300/how-to-find-the-processes-which-are-hogging-the-machine)

</details>

<details>
<summary><b>你需要在 200 台服务器上升级 <code>ntpd</code> 服务。最好的方法是什么，以便将所有这些升级到最新版本？</b></summary><br>

通过使用 **基础设施即代码 (Infrastructure as a Code)** 的方法，有多种好方法：

1. **配置同步变更管理模式**：

有配置管理工具（Ansible, Chef, Puppet, Saltstack...），可用于自动更新所有服务器上的 `ntpd` 服务。为了保持系统稳定，服务器上的系统包通常只使用安全更新进行自动更新。软件包的主要或次要版本通常在配置定义中锁定版本，以防止服务的错误配置。然后通过更改配置定义中的 `ntpd` 版本来部署变更。

采用这种方法时，大规模向基础设施部署变更时要小心很重要。部署流水线应包括单元测试、集成测试和系统测试，并最终首先部署到 Staging（预发布）环境以证明配置正确性。如果测试证明了配置的正确性，则应通过增量 rollout（滚动更新）进行部署，并能够在出错或失败时回滚。

2. **不可变服务器模型**：

在不可变服务器模型中，整个单元（服务器、容器）被新的更新镜像替换，而不是对正在运行的服务器进行更改（这消除了配置漂移）。采用这种方法，你通常使用 Packer 或带有 Dockerfile 的 Docker 等工具构建服务器镜像。然后测试该镜像并类似于上面的选项 (1.) 部署，但现在使用诸如金丝雀发布等技术，这也具有增量 rollout 和回滚的能力。

有用资源：

- [基础设施即代码 - 第 8 章：更新和更改服务器的模式](http://shop.oreilly.com/product/0636920039297.do)

</details>

<details>
<summary><b>如何在 Linux/Unix 上永久设置 <code>$PATH</code>？为什么这个变量如此重要？***</b></summary>

待补充。

</details>

<details>
<summary><b>当你的服务器启动时，控制台上出现一些错误。如何检查引导消息以及它们存储在哪里？</b></summary><br>

你的控制台有两种类型的消息：

- **由内核生成**（通过 printk）
- **由用户空间生成**（通常是你的 init 系统）

内核消息始终存储在 **kmsg** 缓冲区中，可通过 `dmesg` 命令查看。它们也经常被复制到你的 **syslog**。这也适用于写入 `/dev/kmsg` 的用户空间消息，但这些相当罕见。

同时，当用户空间将其漂亮的启动状态文本写入 `/dev/console` 或 `/dev/tty1` 时，它根本不会存储在任何地方。它只是去屏幕然后就这样了。

`dmesg` 用于查看内核环形缓冲区中包含的引导消息。环形缓冲区是固定大小的缓冲区，任何添加到其中的新数据都会覆盖其中最旧的数据。

它显示引导过程完成后的操作，例如传递给内核的命令选项；检测到的硬件组件、添加新 USB 设备时的事件或错误，如 NIC（网络接口卡）故障和驱动程序报告未检测到网络上的链路活动以及更多内容。

如果系统日志记录是通过 journal 组件完成的，你应该使用 `journalctl`。它显示的消息包括内核和引导消息；来自 syslog 或各种服务的消息。

启动问题/错误要求系统管理员查看某些重要文件以及特定命令（由不同版本的 Linux 以不同方式处理）：

- `/var/log/boot.log` - 系统启动日志，包含系统启动期间发生的所有事情
- `/var/log/messages` - 存储全局系统消息，包括在系统启动期间记录的消息
- `/var/log/dmesg` - 包含内核环形缓冲区信息

有用资源：

- [如何在 Linux 引导后查看所有引导消息？（原版）](https://superuser.com/questions/1188407/how-to-view-all-boot-messages-in-linux-after-booting)
- [/var/log/{syslog,dmesg,messages} 日志文件之间的差异](https://superuser.com/questions/565927/differences-in-var-log-syslog-dmesg-messages-log-files)
- [如何在引导 Debian 系统时回顾滚动的消息？](https://serverfault.com/questions/516411/all-debian-boot-messages)

</details>

<details>
<summary><b>Swap（交换空间）使用率过高。造成这种情况的原因是什么，如何解决交换问题？</b></summary><br>

**Swap 空间**是操作系统在可用内存已完全利用时分配用于使用的物理内存的受限量。这是一种涉及将内存部分从物理存储交换到交换空间的内存管理。

如果系统需要更多内存资源且 RAM 已满，则内存中的非活动页面会被移动到 swap 空间。虽然 swap 空间可以帮助拥有少量 RAM 的机器，但它不应被视为更多 RAM 的替代品。**Swap** 空间位于硬盘驱动器上，其访问时间比物理内存慢。

工作负载增加了你的 RAM 需求。你正在运行需要更多内存的工作负载。整个 swap 的使用表明了这一点。此外，将 `swappiness` 更改为 **1** 可能不是一个明智的决定。将 `swappiness` 设置为 **1** 并不意味着不会进行交换。它只表示内核在交换方面有多积极，它并不能消除交换。如果需要，交换将会发生。

- **增加 swap 空间的大小** - 首先，你会增加磁盘使用量。如果你的磁盘不够快以跟上速度，那么你的系统最终可能会颠簸（thrashing），并且你会经历数据进出内存时的减速。这将导致瓶颈。
- **添加更多 RAM** - 真正的解决方案是添加更多内存。RAM 没有替代品，如果你有足够的内存，你将较少交换。

用于监控 swap 空间使用率：

- `cat /proc/swaps` - 查看总 swap 大小和使用量
- `grep SwapTotal /proc/meminfo` - 显示总 swap 空间
- `free` - 显示系统内存（包括 swap）的可用和已用数量
- `vmstat` - 检查交换统计信息
- `top`, `htop`- 检查 swap 空间使用情况
- `atop` - 显示你的系统是否过度承诺了内存
- 或使用单行 shell 命令列出所有应用程序及其使用的 swap 空间量（以千字节为单位）：
```bash
for _fd in /proc/*/status ; do
  awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $_fd
done | sort -k 2 -n -r | less
```

有用资源：

- [Linux 吃掉了我的 ram！](https://www.linuxatemyram.com/)
- [如何在 Linux 中找出哪些进程正在使用 swap 空间？](https://stackoverflow.com/questions/479953/how-to-find-out-which-processes-are-using-swap-space-in-linux)
- [8 个用于监控 Linux 上 Swap 空间使用的有用命令](https://www.tecmint.com/commands-to-monitor-swap-space-usage-in-linux/)
- [在 Ubuntu 服务器上拥有完全使用的 SWAP 有什么危险？](https://serverfault.com/questions/499301/what-is-the-danger-in-having-a-full-used-swap-in-an-ubuntu-server)
- [如果还有空闲 RAM，如何清空 swap？](https://askubuntu.com/questions/1357/how-to-empty-swap-if-there-is-free-ram)

</details>

<details>
<summary><b>什么是 umask？如何为用户永久设置它？</b></summary><br>

在 Linux 和其他类 Unix 操作系统上，新文件是使用默认权限集创建的。具体来说，可以通过应用称为 `umask` 的权限“掩码”以特定方式限制新文件的权限。`umask` 命令用于设置此掩码或显示其当前值。

永久更改（例如设置 `umask 02`）：

- `~/.profile`
- `~/.bashrc`
- `~/.zshrc`
- `~/.cshrc`

有用资源：

- [什么是 Umask 以及如何在 Linux 下设置默认 umask？](https://www.cyberciti.biz/tips/understanding-linux-unix-umask-value-usage.html)

</details>

<details>
<summary><b>解释以下 umask 值之间的差异：000, 002, 022, 027, 077, 和 277。</b></summary><br>

<table style="width:100%">
  <tr>
    <th>Umask</th>
    <th>文件结果</th>
    <th>目录结果</th>
  </tr>
  <tr>
    <td>000</td>
    <td>666 rw- rw- rw-</td>
    <td>777 rwx rwx rwx</td>
  </tr>
 <tr>
    <td>002</td>
    <td>664 rw- rw- r--</td>
    <td>775 rwx rwx r-x</td>
  </tr>
  <tr>
    <td>022</td>
    <td>644 rw- r-- r--</td>
    <td>755 rwx r-x r-x</td>
  </tr>
<tr>
    <td>027</td>
    <td>640 rw- r-- ---</td>
    <td>750 rwx r-x ---</td>
  </tr>
<tr>
    <td>077</td>
    <td>600 rw---- ---</td>
    <td>700 rwx --- ---</td>
  </tr>
<tr>
    <td>277</td>
    <td>400 r-- --- ---</td>
    <td>500 r-x --- ---</td>
  </tr>
</table>

有用资源：

- [什么是 Umask 以及如何在 Linux 下设置默认 umask？](https://www.cyberciti.biz/tips/understanding-linux-unix-umask-value-usage.html)

</details>

<details>
<summary><b>符号链接（symbolic link）和硬链接（hard link）有什么区别？</b></summary><br>

在文件系统下，文件由 inode 表示（或者是多个 inode，不确定）。

- 文件系统中的文件基本上是对 inode 的链接
- 然后硬链接只是创建另一个指向相同底层 inode 的文件

当你删除一个文件时，它会移除对底层 inode 的一个链接。只有当所有到该 inode 的链接都被删除时，inode 才会被删除（或可删除/覆盖）。

- 符号链接是文件系统中另一个名称的链接

一旦创建了硬链接，链接就是指向 inode 的。删除、重命名或移动原始文件不会影响硬链接，因为它链接到底层 inode。对 inode 上数据的任何更改都会反映在所有引用该 inode 的文件中。

注意：硬链接仅在同一个文件系统内有效。符号链接可以跨越文件系统，因为它们只是另一个文件的名称。

区别：

- **Hardlink（硬链接）**不能为目录创建。只能为文件创建硬链接
- **Softlink（软链接/符号链接）**也可以链接到目录

有用资源：

- [硬链接和符号链接之间有什么区别？](https://medium.com/@wendymayorgasegura/what-is-the-difference-between-a-hard-link-and-a-symbolic-link-8c0493041b62)

</details>

<details>
<summary><b>粘滞位（sticky bit）是如何工作的？**SUID/GUID** 是一样的吗？</b></summary><br>

这可能是我最令人烦恼的事情之一，人们总是搞砸。 **SUID/GUID** 位和 **粘滞位**是两件完全不同的事情。

如果你做 `man chmod`，你可以阅读关于 **SUID** 和 **粘滞位**的信息。

**SUID/GUID**

上面手册页试图说的是，在 rwxrwxrwx 的用户八进制（第一组 rwx）和组八进制（第二组 rwx）中 x 位所在的位置可以处于额外状态，其中 x 变为 s。当这种情况发生时，该文件在执行时（如果它是一个程序而不是 shell 脚本）将以文件或组的权限运行。

因此，如果文件由 root 拥有且 **SUID** 位打开，则该程序将以 root 身份运行。即使你作为普通用户执行它也是如此。**GUID** 位也适用同样的情况。

示例：

**无 suid/guid** - 仅设置 `rwxr-xr-x` 位。

```bash
ls -lt b.pl
-rwxr-xr-x 1 root root 179 Jan  9 01:01 b.pl
```

**suid & 用户的可执行位启用（小写 s）** - 设置 `rwsr-x-r-x` 位。

```bash
chmod u+s b.pl
ls -lt b.pl
-rwsr-xr-x 1 root root 179 Jan  9 01:01 b.pl
```

**suid 启用 & 可执行位禁用（大写 S）** - 设置 `rwSr-xr-x` 位。

```bash
chmod u-x b.pl
ls -lt b.pl
-rwSr-xr-x 1 root root 179 Jan  9 01:01 b.pl
```

**guid & 组的可执行位启用（小写 s）** - 设置 `rwxr-sr-x` 位。

```bash
chmod g+s b.pl
ls -lt b.pl
-rwxr-sr-x 1 root root 179 Jan  9 01:01 b.pl
```

**guid 启用 & 可执行位禁用（大写 S）** - 设置 `rwxr-Sr-x` 位。

```bash
chmod g-x b.pl
ls -lt b.pl
-rwxr-Sr-x 1 root root 179 Jan  9 01:01 b.pl
```

**粘滞位**

另一方面，粘滞位表示为 `t`，例如 `/tmp` 目录：

```bash
ls -l /|grep tmp
drwxrwxrwt. 168 root root 28672 Jun 14 08:36 tmp
```

这个位应该始终被称为 _受限删除位_，因为它真正表示的就是那个。当启用此模式位时，它使目录成为用户只能删除其中拥有的文件和目录。

有用资源：

- [粘滞位是如何工作的？（原版）](https://unix.stackexchange.com/questions/79395/how-does-the-sticky-bit-work)

</details>

<details>
<summary><b>命令前的 <code>LC_ALL=C</code> 做什么？在什么情况下它会很有用？</b></summary><br>

`LC_ALL` 是覆盖所有其他本地化设置的环境变量。这将所有 `LC_` 类型的变量一次性设置为指定的区域设置。

在命令前设置 `LC_ALL=C` 的主要原因是简单地获取英文输出（一般更改命令使用的区域设置）。

另一方面，使用 `LC_ALL=C` 增加命令执行速度也很重要，例如 `grep` 或 `fgrep`。使用 `LC_ALL=C` 区域设置提高了我们的性能并缩短了命令执行时间。

例如，如果你设置 `LC_ALL=en_US.utf8`，你的系统打开了 `/usr/lib/locale` 目录中的多个文件。对于 `LC_ALL=C`，只执行最少量的打开和读取操作。

如果你想恢复会话的所有正常（原始）区域设置：

```bash
LC_ALL=
```

如果 `LC_ALL` 不起作用，请尝试使用 `LANG`（如果那仍然不起作用，请尝试 `LANGUAGE`）：

```bash
LANG=C date +%A
Monday
```

有用资源：

- [LC_ALL=C 做什么？（原版）](https://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do)
- [使用 LC_ALL=C 加速 grep 搜索](https://www.inmotionhosting.com/support/website/ssh/speed-up-grep-searches-with-lc-all)

</details>

<details>
<summary><b>如何使 Web 应用程序具有高可用性？***</b></summary>

待补充。

</details>

<details>
<summary><b>你正在配置一台新服务器。其中一个步骤是为应用目录设置权限。你会采取哪些步骤，要避免什么错误？</b></summary><br>

**1) 主要要求 - 记住这一点**

- 哪些用户可以访问应用程序文件系统
- Web 服务器的权限，例如 Apache 和应用程序服务器（如 uwsgi）的权限
- 特定目录的权限，如 **uploads**, **cache** 和主应用目录如 `/var/www/app01/html`
- 用户正确的 `umask` 值以及 **suid**/**sgid**（仅用于特定情况）
- 所有未来文件和目录的权限
- cron 作业和脚本的权限

**2) 应用程序目录**

`/var/www` 包含每个网站的目录（应用的隔离），例如 `/var/www/app01`, `/var/www/app02`

```bash
mkdir /var/www/{app01,app02}
```

**3) 应用所有者和组**

每个应用程序都有一个指定的 **所有者**（如 **u01-prod**, **u02-prod**）和 **组**（如 **g01-prod**, **g02-prod**），它们被设置为网站目录中所有文件和目录的所有者：

```bash
chown -R u01-prod:g01-prod /var/www/app01
chown -R u02-prod:g02-prod /var/www/app02
```

**4) 开发人员所有者和组**

维护网站的所有用户都有自己的组，并附加到应用程序组：

```bash
id alice
uid=2000(alice) gid=4000(alice) groups=8000(g01-prod)
id bob
uid=2001(bob) gid=4001(bob) groups=8000(g01-prod),8001(g02-prod)
```

因此，**alice** 用户拥有 `/var/www/app01` 的标准权限，而 **bob** 用户拥有 `/var/www/app01` 和 `/var/www/app02` 的标准权限。

**5) Web 服务器所有者和组**

任何需要由 webserver 写入的文件或目录都有它们的所有者。如果 web 服务器是 Apache，默认所有者/组是 **apache:apache** 或 **www-data:www-data**，对于 Nginx 将是 **nginx:nginx**。不要更改这些设置。

如果应用程序与像 **uwsgi** 或 **php-fpm** 这样的应用服务器一起工作，应该在特定配置文件中设置适当的用户和组（例如对于 **app01** 将是 **u01-prod:g01-prod**）。

**6) 权限**

使用 **访问控制列表 (ACLs)** 正确设置权限：

```bash
# For web server
setfacl -Rdm "g:apache:rwx" /var/www/app01
setfacl -Rm "g:apache:rwx" /var/www/app01

# For developers
setfacl -Rdm "g:g01-prod:rwx" /var/www/app01
setfacl -Rm "g:g01-prod:rwx" /var/www/app01
```

如果你使用 **SELinux**，请记住安全上下文：

```bash
chcon -R system_u:object_r:httpd_sys_content_t /var/www/app01
```

**7) 安全错误**

- 文件和目录的 **root** 所有者
- **root** 从不执行网站目录中的任何文件，也不应该在那里创建文件
- 权限太宽，如 **777**，因此某些关键文件可能对所有用户可写和可读
- 避免使用 suid root 创建维护脚本或其他关键文件

如果你允许你的站点修改构成你运行站点的代码的文件，你就让某人接管你的服务器变得容易得多。

文件上传工具允许用户上传任何名称和任何内容的文件。这允许用户上传邮件中继 PHP 脚本来到你的站点，他们可以在任何地方放置它，将你的服务器变成转发未经请求的商业电子邮件的机器。此脚本也可用于读取你数据库中的每个电子邮件地址或其他个人信息。

如果恶意用户可以上传具有任何名称的文件但不能控制内容，那么他们可以轻松上传覆盖你的 `index.php`（或其他关键文件）并破坏你的站点的文件。

有用资源：

- [如何为 WWW 文件夹设置 linux 权限？](https://serverfault.com/questions/124800/how-to-setup-linux-permissions-for-the-www-folder)
- [我的网站文件或文件夹在 Linux Web 服务器上应该有什么权限？](https://serverfault.com/questions/357108/what-permissions-should-my-website-files-folders-have-on-a-linux-webserver)
- [setgid 程序的安全陷阱](https://www.agwa.name/blog/post/security_pitfalls_of_setgid_programs)

</details>

<details>
<summary><b>当你在运行级别 3 时运行 <code>telinit 1</code>，init 将采取哪些步骤？最终结果是什么？如果你使用 <code>telinit 6</code> 而不是 <code>reboot</code> 命令，你的服务器会重启吗？***</b></summary><br>

待补充。

有用资源：

- [如果我使用“telinit 6”代替“reboot”命令来重启我的电脑会有什么不同？](https://unix.stackexchange.com/questions/434560/what-differences-it-will-make-if-i-use-telinit-6-instead-of-reboot-command)

</details>

<details>
<summary><b>我忘记了 root 密码！我在 BSD 中该怎么办？进入单用户模式启动的目的是什么？</b></summary><br>

重启系统，在 `Boot:` 提示符下输入 `boot -s` 以进入 **单用户模式**。

关于要使用的 shell 的问题时，按 `Enter`，这将显示一个 `#` 提示符。

输入 `mount -urw /` 以重新挂载根文件系统为读写，然后运行 `mount -a` 以重新挂载所有文件系统。

运行 `passwd root` 更改 root 密码，然后运行 `exit` 继续引导。

**单用户模式**基本上应该让你能够使用 root 访问权限登录并更改几乎任何事情。例如，你可能会在恢复损坏的主数据库或系统数据库时使用单用户模式，或者当你正在更改服务器配置选项（如密码恢复）时。

有用资源：

- [FreeBSD 重置或恢复 Root 密码](https://www.cyberciti.biz/tips/howto-freebsd-reset-recover-root-password.html)
- [单用户模式定义](http://www.linfo.org/single_user_mode.html)

</details>

<details>
<summary><b>你如何在不调用文本编辑器的情况下修改文本文件？</b></summary><br>

例如：<br>

```bash
# cat >filename ... - 覆盖文件
# cat >>filename ... - 追加到文件
cat > filename << __EOF__
data
__EOF__
```

</details>

<details>
<summary><b>如何更改内核参数？你可能需要调整哪些内核选项？***</b></summary><br>

要在类 Unix 系统中设置内核参数，首先编辑 `/etc/sysctl.conf` 文件，进行更改后保存文件并运行命令 `sysctl -p`，此命令将使更改永久生效而无需重启机器。

有用资源：

- [如何以持久和非持久方式更改内核运行时参数](https://www.tecmint.com/change-modify-linux-kernel-runtime-parameters/)

</details>

<details>
<summary><b>解释 <code>/proc</code> 文件系统。</b></summary><br>

`/proc` 是一个虚拟文件系统，提供有关内核、硬件和正在运行的进程的详细信息。

由于 `/proc` 包含虚拟文件，因此称为虚拟文件系统。这些虚拟文件具有独特的品质。其中大多数列为零字节大小。

诸如 `/proc/interrupts`, `/proc/meminfo`, `/proc/mounts` 和 `/proc/partitions` 之类的虚拟文件提供了系统硬件的即时一瞥。其他：`/proc/filesystems` 文件和 `/proc/sys/` 目录提供系统配置信息和接口。

有用资源：

- [Linux 文件系统层次结构 - /proc](https://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html)

</details>

<details>
<summary><b>描述你的数据备份过程。你应该多久测试一次备份？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>解释 ext3/ext4 中的三种日志记录类型。</b></summary><br>

**ext3/ext4** 文件系统中提供三种类型的日志记录：

- **Journal (日志)** - 元数据和内容都保存在日志中
- **Ordered (有序)** - 只有元数据保存在日志中。只有在将内容写入磁盘后才对元数据进行日志记录。这是默认设置
- **Writeback (回写)** - 只有元数据保存在日志中。元数据可能在将内容写入磁盘之前或之后进行日志记录

</details>

<details>
<summary><b>什么是 inode？如何找到文件的 inode 号以及如何使用它？</b></summary><br>

**inode** 是 Linux 和其他类 Unix 操作系统上文件系统中的数据结构，存储有关文件的所有信息，除了其名称和实际数据。数据结构是一种以高效方式使用数据的存储方式。

Unix 文件存储在磁盘的两个不同部分——数据块和 inode。我不会深入超级块和其他异国情调的信息。数据块包含文件的“内容”。关于文件的信息存储在其他地方——在 inode 中。

使用 `ls` 命令可以轻松找到文件的 inode 号，该命令默认列出当前目录（即用户当前所在的目录）中的对象（即文件、链接和目录），带有其 `-i` 选项。因此，例如，以下将显示当前目录中每个对象的名称及其 inode 号：

```bash
ls -i
```

`df` 的 `-i` 选项指示它提供有关每个文件系统上的 inode 的信息，而不是关于可用空间的信息。具体来说，它告诉 df 为每个挂载的文件系统返回 inode 总数、空闲 inode 数、已用 inode 数和 inode 使用百分比。此选项可以与 `-h` 选项一起使用如下，以使输出更易于阅读：

```bash
df -hi
```

**通过 inode 查找文件**

如果你知道 inode，你可以使用 find 命令找到它：

```bash
find . -inum 435304 -print
```

**删除具有奇怪名称的文件**

有时文件是使用文件名中的特殊字符创建的。Unix 文件系统允许任何字符作为文件名的一部分，除了空值（ASCII 000）或 "/"。每个其他字符都是允许的。

用户可以创建使目录或文件难以看到的字符的文件。他们可以创建一个末尾带有空格目录 ".. "，或者使用以下命令创建一个名称中包含退格符的文件：

```bash
touch `printf "aa\bb"`
```

现在当你使用 `ls` 命令时会发生什么：

```bash
ls
aa?b
ls | grep 'a'
ab
```

注意，当 `ls` 将结果发送到终端时，它在文件名中放置一个 "**?**" 以显示不可打印的字符。

你可以使用 `rm -i *` 摆脱这个文件，它会在删除每个文件之前提示你。但你也可以使用 `find` 来删除该文件，一旦你知道 inode 号。

```bash
ls -i
435304 aa?b
find . -inum 435304 -delete
```

有用资源：

- [理解 UNIX/Linux Inodes 基础与示例](https://www.thegeekstuff.com/2012/01/linux-inodes/)
- [POSIX 定义的 inode 是什么？](https://unix.stackexchange.com/questions/387087/what-is-an-inode-as-defined-by-posix/387093)

</details>

<details>
<summary><b><code>ls -l</code> 显示文件属性为问号。这意味着什么，你将采取哪些步骤来删除未使用的“僵尸”文件？</b></summary><br>

这个问题可能更难解决，因为可能需要几个步骤——有时你会得到 `test/file: Permission denied`, `test/file: No such file or directory` 或 `test/file: Input/output error`。

当用户无法对文件执行 `stat()`（这需要执行权限），但可以读取目录条目时（这需要目录上的读访问权限）就会发生这种情况。因此，你得到了目录中的文件列表，但由于它们不可读而无法获取任何关于文件的信息。如果你有一个具有读权限但没有执行权限的目录，你会看到这一点。

一些进程如 `rsync` 生成临时文件，这些文件创建和丢弃很快，这会导致如果你尝试调用其他简单的文件管理命令如 `rm`, `mv` 等时出错。

输出示例：

```bash
?????????? ? ?        ?               ?            ? sess_kee6fu9ag7tiph2jae
```

1) 更改权限：`chmod 0777 sess_kee6fu9ag7tiph2jae` 并尝试删除
2) 更改所有者：`chown root:root sess_kee6fu9ag7tiph2jae` 并尝试删除
3) 为目录更改权限和所有者：`chmod -R 0777 dir/ && chown -R root:root dir/` 并尝试删除
4) 重新创建文件：`touch sess_kee6fu9ag7tiph2jae` 并尝试删除
5) 注意服务器上运行的其他进程，例如 `rsync`，有时你可以将其视为 NFS 服务器过载时的暂时性错误
6) 查找文件 inode：`ls -i`，并尝试删除：`find . -inum <inode_num> -delete`
7) 重新挂载（如果可能）你的文件系统
8) 将系统引导到单用户模式并使用 `fsck` 修复文件系统

有用资源：

- [目录的 ls 中出现问号。也有 IO 错误。](https://serverfault.com/questions/65616/question-marks-showing-in-ls-of-directory-io-errors-too)

</details>

<details>
<summary><b>LVM 还是不使用 LVM。它提供了什么好处？</b></summary><br>

- LVM 使移动文件系统变得相当容易
- 你可以将卷组扩展到新的物理卷上
- 从旧的物理卷中移动任意数量的逻辑卷
- 在不卸载任何分区的情况下将该卷从卷组中移除
- 你还可以为制作备份而创建逻辑卷的快照
- LVM 内置镜像支持，因此你可以在多个物理卷之间镜像逻辑卷
- LVM 甚至支持 TRIM

有用资源：

- [什么是 LVM 以及它用于什么？](https://askubuntu.com/questions/3567/what-is-lvm-and-what-is-it-used-for)

</details>

<details>
<summary><b>如何增加 LVM 分区的大小？</b></summary><br>

使用 `lvextend` 命令调整 LVM 分区大小。

- 扩展大小为 500MB：

```bash
lvextend -L +500M /dev/vgroup/lvolume
```

- 扩展所有可用空闲空间：

```bash
lvextend -l +100%FREE /dev/vgroup/lvolume
```

以及 `resize2fs` 或 `xfs_growfs` 来调整文件系统大小：

- 对于 ext 文件系统：

```bash
resize2fs /dev/vgroup/lvolume
```

- 对于 xfs 文件系统：

```bash
xfs_growfs mountpoint_for_/dev/vgroup/lvolume
```

有用资源：

- [扩展逻辑卷](https://www.tldp.org/HOWTO/LVM-HOWTO/extendlv.html)

</details>

<details>
<summary><b>什么是僵尸/已终止进程？</b></summary><br>

是通过 `exit` 系统调用完成执行但仍具有进程表项的进程：它是处于“**终止状态**”的进程。

标记为 **defunct（已终止）** 的是死进程（所谓的“僵尸”），它们仍然存在是因为它们的父级没有正确销毁它们。如果父进程退出，这些进程将被 init 销毁。

有用资源：

- [什么是 <defunct> 进程，为什么它没有被杀死？](https://askubuntu.com/questions/201303/what-is-a-defunct-process-and-why-doesnt-it-get-killed)

</details>

<details>
<summary><b>在生产环境中升级/更新系统的正确方法是什么？你自动化这些过程吗？你为它们设置停机时间吗？写建议。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>你的朋友在配置 MySQL 服务器时问你：<i>我在安装 mysql 后应该运行 <code>sudo mysql_secure_installation</code> 吗？</i>你怎么看？ </b></summary><br>

最好以它提供的许多安全选项来运行命令，例如：

- 你可以为 root 账户设置密码
- 你可以删除可以从本地主机外部访问的 root 账户
- 你可以删除匿名用户账户
- 你可以删除默认情况下可以由匿名用户访问的测试数据库

有用资源：

- [使用 mysql_secure_installation 的目的是什么？](https://stackoverflow.com/questions/20760908/what-is-purpose-of-using-mysql_secure_installation)

</details>

<details>
<summary><b>展示并解释使用 <code>kill</code> 命令的好方法。</b></summary><br>

谈到杀死进程，除非绝对必要，否则从不使用 `kill -9/SIGKILL`。这种杀戮可能会由于其蛮力而导致问题。

始终尝试使用以下简单程序：

- 首先，发送 **SIGTERM** (`kill -15`) 信号，它告诉进程关闭并通常被视为干净关闭时使用的信号（但请记住此信号可以被忽略）。
- 接下来尝试发送 **SIGHUP** (`kill -1`) 信号，这通常用于告诉进程关闭和重启，该信号也可以被进程捕获和忽略。

在绝大多数情况下，这就是你所需要的——而且更干净得多。

有用资源：

- [什么时候不应该 kill -9 一个进程？](https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process)
- [SIGTERM vs. SIGKILL](https://major.io/2010/03/18/sigterm-vs-sigkill/)

</details>

<details>
<summary><b>什么是 <code>strace</code> 命令，应该如何使用的？解释连接到已经运行的进程的示例。</b></summary><br>

`strace` 是一个强大的命令行工具，用于调试和故障排除类 Unix 操作系统（如 Linux）中的程序。它捕获并记录进程所做的所有系统调用以及进程接收到的信号。

**Strace 概述**

`strace` 可以被视为一个轻量级调试器。它允许程序员/用户快速了解程序如何与 OS 交互。它是通过监控系统调用和信号来完成的。

**用途**

当你没有源代码或不想费心去真正查看时很好用。此外，如果你对自己的代码感兴趣但不想打开 **GDB**，只是想了解外部交互，它也很有用。

**连接到进程的示例**

`strace -p <PID>` - 将进程附加到 strace。

`strace -e trace=read,write -p <PID>` - 通过这种方式，你还可以为事件（如读取和写入）跟踪一个进程/程序（在此示例中）。因此，这里它将打印该进程包含的所有此类事件，包括读取和写入系统调用。

其他这样的例子

- `-e trace=network` - 跟踪所有与网络相关的系统调用。
- `-e trace=signal` - 跟踪所有与信号相关的系统调用。
- `-e trace=ipc` - 跟踪所有 IPC 相关的系统调用。
- `-e trace=desc` - 跟踪所有文件描述符相关的系统调用。
- `-e trace=memory` - 跟踪所有内存映射相关的系统调用。

有用资源：

- [应该如何使用的 strace？（原版）](https://stackoverflow.com/questions/174942/how-should-strace-be-used)
- [strace 如何连接到已经运行的进程？（原版）](https://stackoverflow.com/questions/7482076/how-does-strace-connect-to-an-already-running-process)
- [strace：为了乐趣、利润和调试](http://timetobleed.com/hello-world/)

</details>

<details>
<summary><b>什么时候你会使用访问控制列表而不是或结合 <code>chmod</code> 命令？***</b></summary><br>

待补充。

</details>

<details>
<summary><b><code>/etc/shadow</code> 文件中支持哪些算法？</b></summary><br>

典型的当前算法是：

- MD5
- SHA-1（也称为 SHA）

两者都不再应用于加密/安全目的！！

- SHA-256
- SHA-512
- SHA-3 (KECCAK 在 2012 年 10 月宣布为新的联邦批准哈希算法竞赛的获胜者)

有用资源：

- [用于加密 Linux 密码使用的算法是什么？](https://crypto.stackexchange.com/questions/40841/what-is-the-algorithm-used-to-encrypt-linux-passwords)
- [如何找到用于混淆密码的哈希算法？](https://unix.stackexchange.com/questions/430141/how-to-find-the-hashing-algorithm-used-to-obfuscate-passwords)

</details>

<details>
<summary><b>在类 Unix 系统中 ulimit 的用途是什么？</b></summary><br>

大多数类 Unix 操作系统，包括 Linux 和 BSD，提供限制和控制系统资源使用的方法，如每个进程和每个用户基础的线程、文件和网络连接。这些“**ulimits**”防止单个用户使用过多的系统资源。

</details>

<details>
<summary><b>什么是软限制（soft limits）和硬限制（hard limits）？</b></summary><br>

**硬限制**是允许用户的最大值，由超级用户或 root 设置。此值设置在 `/etc/security/limits.conf` 文件中。用户可以自行增加 **软限制**以需要更多资源时，但不能将 **软限制**设置为高于 **硬限制**。

</details>

<details>
<summary><b>在配置 HAProxy 与 Redis 一起工作时，你从日志中收到 <code>General socket error (Permission denied)</code>。SELinux 已启用。解释 CLI 中的基本 SELinux 故障排除。***</b></summary><br>

有用资源：

- [CLI 中的基本 SELinux 故障排除](https://access.redhat.com/articles/2191331)

</details>

<details>
<summary><b>你配置了 RSA 密钥登录，但你的服务器显示 <code>Server refused our key</code>。你会在哪里寻找问题的原因？</b></summary><br>

**服务器端**

在文件 `/etc/ssh/sshd_config` 中设置 `LogLevel VERBOSE` 可能是你需要的，尽管还有更高级别：

SSH 身份验证失败记录在 `/var/log/auth.log`, `/var/log/secure` 或 `/var/log/audit/audit.log` 中。

以下内容将只给你与 ssh 相关的日志行（例如）：

```bash
grep 'sshd' /var/log/auth.log
```

接下来，列出所有失败的 SSH 登录的最简单命令是下面显示的：

```bash
grep "Failed password" /var/log/auth.log
```

也有用的是：

```bash
grep "Failed\|Failure" /var/log/auth.log
```

在较新的 Linux 发行版上，你可以通过 `journalctl` 命令查询由 Systemd 守护进程维护的运行时日志文件（`ssh.service` 或 `sshd.service`）。例如：

```bash
journalctl _SYSTEMD_UNIT=ssh.service | egrep "Failed|Failure"
```

**客户端**

此外，你还应该以 `-v|--verbose` 运行 SSH 客户端——这是第一级详细程度。接下来，你可以启用额外的（第 2 和第 3 级）详细程度以获得更多调试消息，如下所示，例如使用 `-vv`。

有用资源：

- [在 SSH 中启用调试模式以解决连接问题](https://www.tecmint.com/enable-debugging-mode-in-ssh/)

</details>

<details>
<summary><b>为什么大多数发行版使用 ext4，而不是 XFS 或其他文件系统？为什么有这么多？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>项目经理需要一个新的 SQL Server。你会问她/他什么？***</b></summary><br>

我希望 DBA 问这样的问题：

- 数据库会有多大？（我们是否可以将数据库添加到现有服务器）
- 数据库有多关键？（关于集群、灾难恢复、高可用性）

</details>

<details>
<summary><b>创建一个包含 100 行随机值的文件。</b></summary><br>

例如：

```bash
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 100 > /path/to/file
```

</details>

<details>
<summary><b>如何在不输入密码的情况下以另一个用户身份运行脚本？</b></summary><br>

例如（使用 `visudo` 命令）：

```bash
user1 ALL=(user2) NOPASSWD: /opt/scripts/bin/generate.sh
```

命令路径必须是绝对的！然后从 user1 shell 调用 `sudo -u user2 /opt/scripts/bin/generate.sh`。

</details>

<details>
<summary><b>如何在 bash 脚本中检查是否以 root 身份运行？你应该注意什么？</b></summary><br>

在 bash 脚本中，你有几种方法可以检查正在运行的用户是否是 root。

作为警告，不要使用 root 用户名来检查用户是否是 root。没有任何东西保证 ID 为 0 的用户被称为 root。这是一种被广泛遵循的非常强烈的约定，但任何人都可以将超级用户重命名为另一个名称。

我认为在使用 bash 时最好的方法是使用 `$EUID`，因为 `$UID` 可能会被更改并且不反映运行脚本的真实用户。

```bash
if (( $EUID != 0 )); then
  echo "Please run as root"
  exit
fi
```
</details>

<details>
<summary><b>你能给出一个特定示例，何时指示使用 <code>nobody</code> 账户？告诉我以 <code>nobody</code> 和 <code>www-data</code> 账户运行 httpd 服务的区别。</b></summary><br>

在许多 Unix 变体中，`nobody` 是一个没有拥有任何文件、不在任何特权组中且除了每个其他用户拥有的能力之外没有任何能力的用户账户的惯例名称。

通常以 `nobody` 身份运行守护进程，尤其是服务器，以限制恶意用户在获得控制权后可能造成的损害。

然而，如果像这样运行多个守护进程，这种技术的有用性会降低，因为控制一个守护进程将提供对它们全部的控制。原因是由 `nobody` 拥有的进程能够相互发送信号甚至调试彼此，允许它们读取甚至修改彼此的内存。

**我应该什么时候使用 `nobody` 账户？**

当程序的操作不需要权限时。这在永远不会有任何磁盘活动时最为显著。

这种情况的一个现实例子是 **memcached**（一个键值内存缓存/数据库/东西），它坐在我的计算机和我的服务器上以 `nobody` 账户运行。为什么？因为它根本不需要任何权限，给它一个具有对文件写访问权的账户将只是一个不必要的风险。

Web 服务器也是一个很好的例子。想象一下如果 Apache 以 root 身份运行，有人找到了一种通过 Apache 向控制台发送自定义命令的方法，他们将能够访问你的整个系统。

`nobody` 账户还用作受限 shell，用于给用户文件系统访问权限而没有实际的 shell（如 bash）。这应该防止他们执行任何操作。

**对于 httpd (Apache) 使用 `nobody` 还是 `www-data`？**

在启动 Apache 时需要 root 访问权限，但它很快放弃此权限并假设非特权用户的身份。这个用户可以是 `nobody` 或 `apache`，或者 `www-data`。

几个应用程序将用户 `nobody` 用作默认值。例如，你可能永远不想要像 Apache 服务这样的东西覆盖属于 bind 的文件。拥有每个服务的账户往往是一个非常好的主意。

让 Apache 以 `nobody:nobody` 运行相当容易，只需更新用户和组设置即可。但正如我上面提到的，我真的不建议那个特定的用户/组。你将来可能会倾向于将某个服务添加到也作为 `nobody` 运行的系统中，并且你会忘记你已经给予了用户 `nobody` 对文件系统的写访问权限。

如果 somehow（不知何故），`nobody` 被攻破，它们可能比像 `www-data` 这样的应用程序隔离用户产生更大的影响。当然，这将在很大程度上取决于文件和组权限。`nobody` 使用其他人的权限，而特定于应用程序的用户可以配置为允许文件读取访问，但其他人仍然可能被拒绝。

有用资源：

- [什么是 nobody 用户和组？](https://unix.stackexchange.com/questions/186568/what-is-nobody-user-and-group)
- [Linux 和 Unix Nobody 用户](http://linuxg.net/the-linux-and-unix-nobody-user/)
- [`nobody` 用户的目的是什么？](https://askubuntu.com/questions/329714/what-is-the-purpose-of-the-nobody-user)

</details>

<details>
<summary><b>有一种方法可以将输出重定向到文件并在 stdout 上显示它吗？</b></summary><br>

你想要的命令名为 tee：

`foo | tee output.file`

例如，如果你只关心 stdout：

`ls -a | tee output.file`

如果你想包含 stderr，请执行以下操作：

`program [arguments...] 2>&1 | tee outfile`

`2>&1` 将通道 2（stderr/标准错误）重定向到通道 1（stdout/标准输出），以便两者都作为 stdout 写入。它也被重定向到 tee 命令给定的输出文件。

此外，如果你想追加到日志文件，请使用 `tee -a` 如下：

`program [arguments...] 2>&1 | tee -a outfile`

</details>

<details>
<summary><b>首选的 bash shebang 是什么，为什么？使用 <code>./script</code> 或 <code>bash script</code> 执行文件有什么区别？</b></summary><br>

你应该使用 `#!/usr/bin/env bash` 以实现可移植性：不同的 \*nixes 将 bash 放在不同的位置，而使用 `/usr/bin/env` 是运行在 `PATH` 上找到的第一个 bash 的解决方法。

运行 `./script` 正是这样做的，并且需要文件上的执行权限，但它对程序类型保持中立。它可能是 **bash 脚本**、**sh 脚本**或 **Perl**, **Python**, **awk** 或 **expect 脚本**，或者是实际的 **二进制可执行文件**。运行 `bash script` 将强制它在 `sh` 下运行，而不是任何其他内容。

有用资源：

- [首选的 Bash shebang？（原版）](https://stackoverflow.com/questions/10376206/what-is-the-preferred-bash-shebang)

</details>

<details>
<summary><b>你必须运行一个将执行非常长时间的命令。你如何防止在 ssh 会话断开后杀死这个进程？</b></summary><br>

使用 `nohup` 使你的进程忽略挂断信号：

```bash
nohup long-running-process &
exit
```

或者你想要使用 **GNU Screen**：

```bash
screen -d -m long-running-process
exit
```

有用资源：

- [断开连接后保持远程 SSH 会话和进程运行的 5 种方法](https://www.tecmint.com/keep-remote-ssh-sessions-running-after-disconnection/)

</details>

<details>
<summary><b>中间证书颁发机构的主要目的是什么？</b></summary><br>

要了解中间 CA 的主要目的，你应该首先了解 **根 CA**、**中间 CA** 和 **SSL 证书链信任**。

**根 CA** 是主要 CA，通常不直接签署最终实体/服务器证书。它们颁发 Root 证书，这些证书通常预先安装在所有浏览器、移动设备和应用程序中。这些证书的私钥用于签名其他后续证书，称为中间证书。根 CA 通常保持“离线”状态并处于高度安全的环境中，访问受到严格限制。

**中间 CA** 是隶属于一个或多个级别的根 CA 的 CA，由它们信任代表他们签署证书。创建和使用中间 CA 的主要目的是出于安全原因，因为如果中间私钥被泄露，那么根 CA 可以吊销中间证书并使用新的加密密钥对创建一个新证书。

**SSL 证书链信任**是从根证书到最终实体/服务器证书的 SSL 证书列表。为了使 SSL 证书受到信任，它必须由受信任的 CA 颁发，该 CA 包含在连接设备（浏览器、移动设备和应用程序）的信任 CA 列表中。因此，连接设备将测试信任链中每个 SSL 证书的可靠性，直到它与由受信任 CA 颁发的证书匹配为止。

**根-中间 CA**结构是由每个主要 CA 创建的，以防止根密钥泄露的灾难性影响。如果根密钥被泄露，它将使根和所有从属证书变得不可信。因此，创建中间 CA 是确保对主根密钥进行严格保护的最佳实践。

有用资源：

- [证书链如何工作](https://knowledge.digicert.com/solution/SO16297.html)

</details>

<details>
<summary><b>配置更改后如何重新加载 PostgreSQL？</b></summary><br>

解决方案 1：

```bash
systemctl reload postgresql
```

解决方案 2：

```
su - postgres
/usr/bin/pg_ctl reload
```

解决方案 3：

```
SELECT pg_reload_conf();
```

</details>

<details>
<summary><b>你在 <code>.profile</code> 中添加了一些别名。如何在不退出的情况下重新加载 shell？</b></summary><br>

最好的方法是 `exec $SHELL -l`，因为 `exec` 用新进程替换当前进程。也很好（但其他）的解决方案是 `. ~/.profile`。

有用资源：

- [如何从命令行重新加载 .bash_profile？](https://stackoverflow.com/questions/4608187/how-to-reload-bash-profile-from-the-command-line)

</details>

<details>
<summary><b>如何在不保存 shell 历史的情况下退出？</b></summary><br>

```bash
kill -9 $$
```

或者

```bash
unset HISTFILE && exit
```

有用资源：

- [我如何在关闭终端时不保存历史记录？](https://unix.stackexchange.com/questions/25049/how-do-i-close-a-terminal-without-saving-the-history)

</details>

<details>
<summary><b>这个 UID 0 toor 账户是什么？我被入侵了吗？</b></summary><br>

**toor** 是替代超级用户账户，其中 toor 是 root 的反向拼写。它旨在与非标准 shell 一起使用，因此 root 的默认 shell 不需要更改。

这很重要，因为不属于基本发行版而是从端口或包安装的 shell，安装在 `/usr/local/bin` 中，默认情况下驻留在不同的文件系统上。如果 root 的 shell 位于 `/usr/local/bin` 并且包含 `/usr/local/bin`) 的文件系统未挂载，root 将无法登录以解决问题并必须重新引导到单用户模式才能输入 shell 的路径。

有些人使用 toor 进行日常 root 任务与非标准 shell，留下 root（带有标准 shell）用于单用户模式或紧急情况。默认情况下，用户使用 toor 无法登录，因为它没有密码，因此请以 root 身份登录并为 toor 设置密码后再使用它来登录。

有用资源：

- [root 账户（和 toor）](https://administratosphere.wordpress.com/2007/10/04/the-root-account-and-toor/)

</details>

<details>
<summary><b>有一种简单的方法可以在复杂的目录结构中搜索数千个文件以查找包含特定字符串的文件吗？</b></summary><br>

例如使用 `fgrep`：

```bash
fgrep * -R "string"
```

或者：

```bash
grep -insr "pattern" *
```

- `-i` 忽略 **PATTERN** 和输入文件中的大小写差异
- `-n` 在输出中每行前缀加上其在输入文件中的基于 1 的行号
- `-s` 抑制关于不存在或不可读文件的错误消息。
- `-r` 递归读取每个目录下的所有文件。

有用资源：

- [如何在 LINUX 中的目录及其子目录文件中 grep 字符串？](https://stackoverflow.com/questions/15622328/how-to-grep-a-string-in-a-directory-and-all-its-subdirectories-files-in-linux)

</details>

<details>
<summary><b>如何找出可执行文件在运行时加载的动态库？</b></summary><br>

你可以使用 `ldd` 命令做到这一点：

```bash
ldd /bin/ls
```

</details>

<details>
<summary><b>你有同步测试和生产环境的任务。你会采取哪些步骤？</b></summary><br>

很容易陷入关于克隆环境的 bikeshedding（无关紧要的细节争论）并错过真正的重点：

- 只有生产环境才是生产环境

每次你在那里部署时，你都在测试独特的部署代码 + 软件 + 环境的组合。

每隔一段时间，定期克隆生产服务器以创建测试服务器是一个好的解决方案。你可以使用快照在 dev/test 下创建具有与你的生产环境完全复制的实例，例如：

- 生成生产的快照
- 将快照复制到 staging（或其他）
- 使用此快照创建新磁盘

当然，你可以启动各种系统组件或整个系统的克隆，并捕获真实流量以离线重放（系统测试的黄金标准）。但许多系统太大、太复杂且成本过高而无法克隆。

在环境同步之前，一个好的方法是跟踪你对测试环境所做的每一个更改并提供一种将其传播到生产环境的方法，这样你就不会跳过任何步骤并以尽可能平滑的方式完成它。

结构比较工具或部署脚本从生产环境更新测试环境也是一个好的解决方案。

**预同步任务**

首先是通知开发人员和客户不要在测试环境中进行更改（如果可能，禁用针对此环境的测试域或设置有关同步信息的静态页面）。

备份/快照两个环境也很重要。

**数据库服务器**

- 同步/更新系统版本（例如包）
- 从生产 db 服务器上创建数据库的转储文件
- 在测试 db 服务器上导入转储文件
- 如有必要，同步登录权限、角色、数据库权限、打开连接到数据库和其他内容

**Web/App 服务器**

- 同步/更新系统版本（例如包）
- 如有必要，更新内核参数、防火墙规则等
- 同步/更新所有正在运行的重要服务的配置文件
- 同步/更新用户账户（例如权限）及其主目录
- 从 git/svn 存储库部署项目
- 同步/更新项目中存在的重要目录，如 **static**, **asset** 和其他
- 同步/更新项目目录的权限
- 删除/更新所有 webhooks
- 更新 cron 作业

**其他任务**

- 更新测试域和特定 URL 的负载均衡器配置
- 更新队列、会话和存储实例的配置

有用资源：

- [保持测试和生产服务器环境干净、同步和一致](https://stackoverflow.com/questions/639668/keeping-testing-and-production-server-environments-clean-in-sync-and-consisten)

</details>

###### 网络问题 (24)

<details>
<summary><b>在你的工作站上配置虚拟接口。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>根据 HTTP 监视器，一个网站已关闭。你可以 telnet 到端口，那么如何解决它？</b></summary><br>

如果你可以 telnet 到该端口，这意味着在该端口上运行的服务正在运行并且你可以连接到它（这不是网络问题）。检查域名解析到的 IP 地址并使用相同的域来测试连接是一个好方法。

首先从其他位置检查你的网站是否在线。然后让你知道网站是否 everywhere（到处）关闭，或者只有你的网络无法查看它。检查 web 浏览器返回的内容也是一个好主意。

**如果只有 IP 连接工作**

- 你可以使用 whois 查看哪些 DNS 服务器为站点提供主机名：`whois www.example.com`
- 你可以使用 `dig` 或 `host` 等工具来测试 DNS，看看主机名是否正在解析：`host www.example.org dns.example.org`
- 你还可以检查全局公共 dns 服务器：`host www.example.com 9.9.9.9`

如果域名未解析，可能是 DNS 服务器的问题。

**如果域名正确解析**

- 调查日志文件并根据日志解决问题，这是显示出了什么问题的最佳方法
- 检查 http 状态码，通常将是带有 5xx 的响应，也许服务器过载是因为客户端对网站或特定 url 进行了大量连接？也许是你的缓存规则没有正常工作？
- 检查 web/proxy 服务器配置（例如 `nginx -t -c </path/to/nginx.conf>`），也许是另一个系统管理员对域名配置进行了一些更改？
- 也许是服务器上的一些东西崩溃了？也许空间不足或内存不足？
- 也许是网站上的编程错误？

</details>

<details>
<summary><b>负载均衡可以极大地影响服务器性能。讨论几种负载均衡机制。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>列出 DNS 问题期间可能会退化的网络故障排除工具的示例。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>解释 HTTP 1.1 和 HTTP 2.0 之间的区别。</b></summary><br>

<b>HTTP/2</b> 支持查询多路复用、头部压缩、优先级以及更智能的数据包流管理。这导致延迟减少并加速现代网页上的内容下载。

与 **HTTP/1.1** 的关键区别：

- 它是二进制的，而不是文本的
- 完全多路复用的，而不是有序和阻塞的
- 因此可以使用一个连接进行并行处理
- 使用头部压缩来减少开销
- 允许服务器将响应“推送”到客户端缓存中

有用资源：

- [什么是 HTTP/2 - 终极指南](https://kinsta.com/learn/what-is-http2/)

</details>

<details>
<summary><b>开发团队报告了一个错误：<code>POST http://ws.int/api/v1/Submit/ resulted in a 413 Request Entity Too Large</code>。怎么了？</b></summary><br>

**修改域名的 NGINX 配置文件**

设置正确的 `client_max_body_size` 变量值：

```bash
client_max_body_size 20M;
```

重启 Nginx 以应用更改。

**修改 php.ini 文件以进行上传限制**

并非所有配置都需要，但你可能还必须修改 PHP 上传设置以确保没有任何内容超出 php 配置的限制。

现在逐一查找以下指令：

```bash
upload_max_filesize
post_max_size
```

并将其限制增加到 20M，默认它们是 8M 和 2M：

```bash
upload_max_filesize = 20M
post_max_size = 20M
```

最后保存它并重启 PHP。

有用资源：

- [Nginx 中的 413 Request Entity Too Large 以及设置的 client_max_body_size](https://serverfault.com/questions/814767/413-request-entity-too-large-in-nginx-with-client-max-body-size-set)

</details>

<details>
<summary><b>什么是握手机制，为什么我们需要三次握手？</b></summary><br>

**握手**开始于一个设备向另一个设备发送消息表明它想要建立通信通道。然后两个设备来回发送几条消息以使他们同意通信协议。

**三次握手**是一种用于在 TCP/IP 网络中创建本地主机/客户端和服务器之间连接的方法。它是一种需要客户端和服务器在 actual（实际）数据通信开始之前交换 `SYN` 和 `ACK` (`SYN`, `SYN-ACK`, `ACK`) 数据包的三步方法。

有用资源：

- [为什么我们需要三次握手？为什么不只要两次？](https://networkengineering.stackexchange.com/questions/24068/why-do-we-need-a-3-way-handshake-why-not-just-2-way)

</details>

<details>
<summary><b>为什么 UDP 比 TCP 快？</b></summary><br>

**UDP** 比 **TCP** 快，简单的原因是它的现有确认数据包（`ACK`）允许连续的数据包流，而不是 TCP 使用 TCP 窗口大小和往返时间（`RTT`）计算的一组数据包的确认。

有用资源：

- [UDP vs TCP，它有多快？](https://stackoverflow.com/questions/47903/udp-vs-tcp-how-much-faster-is-it)

</details>

<details>
<summary><b>在你看来，提高安全性的 5 个最重要的 OpenSSH 参数是什么？***</b></summary><br>

待补充。

有用资源：

- [OpenSSH 安全和加固](https://linux-audit.com/audit-and-harden-your-ssh-configuration/)

</details>

<details>
<summary><b>什么是 NAT？它是用来做什么的？</b></summary><br>

它使使用未注册 IP 地址的私有 IP 网络能够连接到互联网。**NAT** 在路由器上运行，通常连接两个网络，并在数据包转发到另一个网络之前将内部网络中的私有（非全球唯一）地址转换为合法地址。

可以使用 **NAT** 为需要特殊外部访问的工作站或其他计算机分配特定的外部 IP，允许它们与需要唯一公共 IP 地址的计算机和应用程序进行通信。**NAT** 也是防火墙安全的一个重要方面。

有用资源：

- [网络地址转换 (NAT) 概念](http://www.firewall.cx/networking-topics/network-address-translation-nat/227-nat-concepts.html)

</details>

<details>
<summary><b>生成树（Spanning Tree）的目的是什么？</b></summary><br>

该协议在 OSI 模型的 Layer 2 上运行，目的是防止网络上的环路。没有 **STP**，冗余交换机部署将产生广播风暴，甚至使最强大的网络瘫痪。有几个基于原始 IEEE 802.1D 标准的迭代版本；每个都与其他略有不同，但基本上实现了相同的无环目标。

</details>

<details>
<summary><b>如何检查我的 Linux 服务器上正在监听的端口？</b></summary><br>

使用：

- `lsof -i`
- `ss -l`
- `netstat -atn` - 用于 tcp
- `netstat -aun` - 用于 udp
- `netstat -tulapn`

</details>

<details>
<summary><b>当你连接到远程主机时 <code>Host key verification failed</code> 是什么意思？你会自动接受它吗？</b></summary><br>

`Host key verification failed` 意味着远程主机的主机密钥已更改。当连接到其 `/etc/ssh` 中的主机密钥已更改的计算机（如果该计算机在升级时未复制其旧的主机密钥）时，这很容易发生。这里的主机密钥是当你通过 ssh 重新连接到远程计算机时的证明，你正在与你第一次访问它时连接的同一台计算机交谈。

每当您通过 SSH 连接服务器时，该服务器的公钥都会存储在家目录中（或者如果使用 Mac 或 Windows 桌面可能存储在本地账户设置中）名为 **known_hosts** 的文件中。当您重新连接到同一台服务器时，SSH 连接将验证当前公钥是否与您在 **known_hosts** 文件中保存的公钥匹配。如果自上次连接到它以来服务器的密钥已更改，您将收到上述错误。

不要删除整个 **known_hosts** 文件，正如一些人建议的那样，这完全使警告的意义无效。这是一种安全功能，用于警告你可能发生了中间人攻击。

在接受新主机密钥之前，请与你的/其他系统管理员进行验证。

有用资源：

- [Git 错误：“连接远程存储库时 Host Key Verification Failed”](https://stackoverflow.com/questions/13363553/git-error-host-key-verification-failed-when-connecting-to-remote-repository)

</details>

<details>
<summary><b>如何使用 <code>telnet</code> 发送 HTTP 请求？</b></summary><br>

例如：

```bash
telnet example.com 80
Trying 192.168.252.10...
Connected to example.com.
Escape character is '^]'.
GET /questions HTTP/1.0
Host: example.com

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
...
```

</details>

<details>
<summary><b>你如何在 Linux 中杀死使用例如 80 端口的程序？</b></summary><br>

列出监听端口 80 的任何进程：

```bash
# with lsof
lsof -i:80

# with fuser
fuser 80/tcp
```

要杀死监听端口 80 的任何进程：

```bash
kill $(lsof -t -i:80)
```

或者更激烈地：

```bash
kill -9 $(lsof -t -i:80)
```

或使用 `fuser` 命令：

```bash
fuser -k 80/tcp
```

有用资源：

- [如何在 Linux 中杀死运行在特定端口上的进程？](https://stackoverflow.com/questions/11583562/how-to-kill-a-process-running-on-particular-port-in-linux/32592965)
- [查找使用特定端口的进程的 PID？](https://unix.stackexchange.com/questions/106561/finding-the-pid-of-the-process-using-a-specific-port)

</details>

<details>
<summary><b>你得到 <code>curl: (56) TCP connection reset by peer</code>。你将采取哪些步骤来解决这个问题？</b></summary><br>

- 检查 URL 是否正确，也许你应该添加 `www` 或正确设置 `Host:` header？还要检查 scheme（http 或 https）
- 检查域名是否解析为正确的 IP 地址
- 使用 `--trace-ascii curl.dump` 启用调试跟踪。`Recv failure` 是一个非常通用的错误，因此很难获取更多信息
- 使用外部代理进行调试连接从外部 ip：`--proxy`
- 使用网络嗅探器（例如 `tcpdump`）在较低的 TCP/IP 层调试连接
- 检查生产环境中的防火墙规则以及网络的出口点，还要检查你的 NAT 规则
- 检查通过网络传输的数据包的 MTU 大小
- 如果你连接到 https 协议，请使用 ssl/tls `curl` 参数检查 SSL 版本
- 这可能是客户端侧的问题，例如 netfilter drop 或限制从你的 IP 地址到域的连接

有用资源：

- [CURL ERROR: Recv failure: Connection reset by peer - PHP Curl](https://stackoverflow.com/questions/10285700/curl-error-recv-failure-connection-reset-by-peer-php-curl)

</details>

<details>
<summary><b>如何使用 iptables 允许来自/到特定 IP 的流量？</b></summary><br>

例如：

```bash
/sbin/iptables -A INPUT -p tcp -s XXX.XXX.XXX.XXX -j ACCEPT
/sbin/iptables -A OUTPUT -p tcp -d  XXX.XXX.XXX.XXX -j ACCEPT
```

</details>

<details>
<summary><b>如何在 OpenBSD 中使用 <code>pf</code> 阻止滥用 IP 地址？</b></summary><br>

做到这一点的最佳方法是定义一个表并创建一个规则来阻止主机，在 `pf.conf` 中：

```bash
table <badhosts> persist
block on fxp0 from <badhosts> to any
```

然后动态从中添加/删除 IP 地址：

```bash
pfctl -t badhosts -T add 1.2.3.4
pfctl -t badhosts -T delete 1.2.3.4
```

</details>

<details>
<summary><b>像 Apache 或 Nginx 这样的 Web 服务器在什么时候将信息写入日志文件？在服务请求之前还是之后？</b></summary><br>

两个服务器都提供了非常全面和灵活的日志记录功能——用于记录服务器上发生的所有事情，从初始请求、通过 URL 映射过程到连接的最终解决，包括过程中可能发生的任何错误。

**Apache**

Apache 服务器访问日志记录由服务器处理的所有请求（在请求完成后）。

**Nginx**

NGINX 在处理完客户端请求后立即在访问日志中写入有关客户端请求的信息。

有用资源：

- [Apache 何时将日志记录到 access.log - 在服务请求之前还是之后？](https://webmasters.stackexchange.com/questions/65566/when-does-apache-log-to-access-log-before-or-after-serving-the-request)
- [nginx 在处理请求之前记录请求](https://serverfault.com/questions/693049/nginx-log-request-before-processing)

</details>

<details>
<summary><b>分析 Web 服务器日志并仅显示 <code>5xx</code> http 代码。你使用哪些外部工具？</b></summary><br>

```bash
tail -n 100 -f /path/to/logfile | grep "HTTP/[1-2].[0-1]\" [5]"
```

http/https 日志管理工具的示例：

- **goaccess** - 是一个开源的实时 Web 日志分析器和交互式查看器，它在 *nix 系统中的终端或通过你的浏览器运行
- **graylog** - 是一个免费和开源的日志管理平台，支持深入的日志收集和分析

有用资源：

- [最佳日志管理工具：51 个用于日志管理、监控、分析和更多的有用工具](https://stackify.com/best-log-management-tools/)

</details>

<details>
<summary><b>开发人员使用服务器上的私钥通过 ssh 部署应用程序。为什么这是不正确的行为，在这种情况下更好的（但不理想）的解决方案是什么？</b></summary><br>

你有个人账户的私钥。服务器需要你的公钥以便它可以验证你试图使用的账户的私钥是否已授权。

私钥的全部意义在于它们是私有的，意味着只有你拥有你的私钥。如果有人接管了你的私钥，它可以在任何时候冒充你。

更好的解决方案是使用 ssh 密钥转发。本质上，你需要创建一个 `~/.ssh/config` 文件（如果不存在）。然后，在文件中添加主机（域名或 IP 地址）并设置 `ForwardAgent yes`。例如：

```bash
Host git.example.com
    User john
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa.git.example.com
    ForwardAgent yes
```

你的远程服务器必须允许入站连接上的 SSH 代理转发，并且你的本地 `ssh-agent` 必须正在运行。

转发 ssh 代理会带来自己的安全风险。如果远程机器上的人可以访问你转发的 ssh 代理连接，他们仍然可以使用你的密钥。然而，这比在远程机器上存储密钥更好：攻击者只能使用 ssh 代理连接，而不是密钥本身。因此，只有当你登录到远程机器时他们才能做任何事情。如果你将密钥存储在远程机器上，他们可以复制它并随时使用它。

如果使用 ssh 密钥请记住关于密码短语，强烈建议减少密钥意外泄露的风险。

有用资源：

- [如何在 SSH 会话中转发本地密钥对？](https://stackoverflow.com/questions/12257968/how-to-forward-local-keypair-in-a-ssh-session)
- [使用 SSH 代理转发](https://developer.github.com/v3/guides/using-ssh-agent-forwarding/)
- [SSH 代理转发被认为有害](https://heipei.github.io/2015/02/26/SSH-Agent-Forwarding-considered-harmful/)
- [使用 ssh-agent 时的安全注意事项](https://www.commandprompt.com/blog/security_considerations_while_using_ssh-agent/)

</details>

<details>
<summary><b>CORS 和 CSPs 之间有什么区别？</b></summary><br>

**CORS** 允许放宽 **同源策略 (Same Origin Policy)**。

例如，通常如果用户同时登录到 `example.com` 和 `example.org`，同源策略防止 `example.com` 向 `example.org/current_user/full_user_details` 发出 AJAX 请求并获取响应访问权限。

这是 Web 的默认策略，防止用户在同时登录多个站点时泄露数据。

现在有了 **CORS**，`example.org` 可以设置一个策略来说明它将允许来源 `https://example.com` 读取由 AJAX 做出的响应。如果 `example.com` 和 `example.org` 都由同一家公司运行并且要在用户浏览器中允许跨来源的数据共享，则会这样做。它只影响客户端方面的事物，而不是服务器端。

**CSPs (内容安全策略)** 另一方面设置当前站点上可以运行什么内容的策略。例如，是否可以执行内联 JavaScript，或者可以从哪些域加载 `.js` 文件。这可以作为对抗 **XSS** 攻击的又一道防线，其中攻击者将尝试注入脚本到 HTML 页面中。通常输出会被编码，但假设开发人员忘记在一个输出字段上。由于政策防止内联脚本的执行，攻击被挫败了。

有用资源：

- [CORS 和 CSPs 之间有什么区别？（原版）](https://stackoverflow.com/questions/39488241/what-is-the-difference-between-cors-and-csps)
- [CSP, SRI 和 CORS](https://colorblindprogramming.com/csp-sri-and-cors)

</details>

<details>
<summary><b>解释使用 <code>nmap</code> 扫描时防火墙的四种响应类型。</b></summary><br>

可能有四种类型的响应：

- **开放端口** - 在防火墙的情况下少数端口
- **关闭端口** - 大多数端口由于防火墙而关闭
- **过滤** - `nmap` 不确定端口是否打开
- **未过滤** - `nmap` 可以访问该端口，但仍然对端口的打开状态感到困惑

有用资源：

- [NMAP - 关闭与过滤](https://security.stackexchange.com/questions/182504/nmap-closed-vs-filtered)

</details>

<details>
<summary><b><code>tcpdump</code> 做什么？如何只捕获到你接口的传入流量？</b></summary><br>

`tcpdump` 是最强大和最广泛使用的命令行数据包嗅探器或包分析工具，用于捕获或过滤在特定接口上接收或传输的 TCP/IP 数据包。

`tcpdump` 将你的网卡置于混杂模式，这基本上告诉它接受它收到的每个数据包。它允许用户查看通过网络传递的所有流量。Wireshark 使用 pcap 来捕获数据包。

如果你想只查看到达你接口的数据包你应该：

- `-Q in` - 用于 Linux `tcpdump` 版本
- `-D in` - 用于 BSD `tcpdump` 版本

两个参数设置发送/接收方向，即应该捕获数据包的方向。

```bash
tcpdump -nei eth0 -Q in host 192.168.252.125 and port 8080
```

</details>

###### Devops 问题 (7)

<details>
<summary><b>什么是顶级 DevOps 工具？你使用过哪些工具？</b></summary><br>

下面提到了最受欢迎的 DevOps 工具：

- **Git** : 版本控制系统工具
- **Jenkins** : 持续集成工具
- **Selenium** : 持续测试工具
- **Puppet**, **Chef**, **Ansible** : 配置管理和部署工具
- **Nagios** : 持续监控工具
- **Docker** : 容器化工具

</details>

<details>
<summary><b>所有这些工具如何一起工作？</b></summary><br>

下面提到了最受欢迎的 DevOps 工具：

- 开发人员开发代码，此源代码由版本控制系统工具（如 Git 等）管理
- 开发人员将此代码发送到 Git 存储库，对代码所做的任何更改都提交到此存储库
- Jenkins 使用 Git 插件从存储库中提取此代码并使用 Ant 或 Maven 等工具构建它
- 配置管理工具（如 puppet）部署并准备测试环境，然后 Jenkins 在此测试环境中发布此代码，在该环境中使用 selenium 等工具进行测试
- 一旦代码经过测试，Jenkins 将其发送到生产服务器进行部署（甚至生产服务器也由 puppet 等工具提供和维持）
- 部署后，它由 Nagios 等工具持续监控
- Docker 容器为测试构建功能提供测试环境

</details>

<details>
<summary><b>什么是 Ansible 中的 playbooks？</b></summary><br>

Playbooks 是 Ansible 的配置、编排和部署语言。

它们可以描述你想要你的远程系统强制执行的政策，或者一组一般 IT 流程的步骤。Playbooks 旨在易于阅读，并使用基本文本语言开发。

在基本层面上，playbooks 可用于管理配置以及部署到远程机器。

</details>

<details>
<summary><b>Nagios 中的 NRPE（Nagios Remote Plugin Executor）是什么？</b></summary><br>

**NRPE** 插件旨在允许你在远程 Linux/Unix 机器上执行 Nagios 插件。这样做的主要原因是允许 Nagios 监视“本地”资源（如 CPU 负载、内存使用等）在远程机器上。

由于这些公共资源通常不暴露给外部机器，因此必须在远程 Linux/Unix 机器上安装像 **NRPE** 这样的代理。

</details>

<details>
<summary><b>Nagios 中的主动检查和被动检查有什么区别？</b></summary><br>

主动检查和被动检查之间的主要区别是主动检查由 Nagios 发起和执行，而被动检查由外部应用程序执行。

被动检查对于监视以下服务非常有用：

- 本质上是非同步的并且不能通过定期轮询其状态来有效监控的服务。
- 位于防火墙后面且无法从监控主机进行主动检查的服务。

主动检查的主要功能如下：

- 主动检查由 Nagios 进程发起。
- 主动检查在定期安排的基础上运行。

</details>

<details>
<summary><b>如何 <code>git clone</code> 包括子模块？</b></summary><br>

例如：

```bash
# With -j8 - performance optimization
git clone --recurse-submodules -j8 git://github.com/foo/bar.git

# For already cloned repos or older Git versions
git clone git://github.com/foo/bar.git
cd bar
git submodule update --init --recursive
```

</details>

<details>
<summary><b>提到使用 Redis 的优势是什么？什么是 <code>redis-cli</code>？ </b></summary><br>

- 它提供高速（比其他快得多）
- 它支持服务器端锁定
- 它有很多客户端库
- 它具有命令级原子操作（tx 操作）
- 支持丰富的数据类型，如哈希、集合、位图

`redis-cli` 是 **Redis** 命令行界面，一个简单的程序，允许从终端直接向 **Redis** 发送命令并读取服务器发送的回复。

有用资源：

- [Redis 的 10 个优势](https://dzone.com/articles/10-traits-of-redis)

</details>

###### 网络安全问题 (4)

<details>
<summary><b>什么是 XSS，你将如何缓解它？</b></summary><br>

**跨站脚本 (Cross Site Scripting)** 是 Web 应用程序中的 JavaScript 漏洞。解释这一点的最简单方法是一个用户进入客户端输入字段的脚本并且该输入在未经验证的情况下被处理的情况。这导致不受信任的数据保存并在客户端执行。

XSS 的对策是输入验证、实施 CSP（内容安全策略）等。

</details>

<details>
<summary><b>HIDS vs NIDS，哪一个更好以及为什么？</b></summary><br>

**HIDS** 是主机入侵检测系统，**NIDS** 是网络入侵检测系统。这两个系统在相似线上工作。只是放置位置不同。**HIDS** 放置在每个主机上，而 **NIDS** 放置在网络上。对于企业来说，首选 **NIDS** 因为 **HIDS** 难以管理，此外它还消耗主机的处理能力。

</details>

<details>
<summary><b>什么是合规性（Compliance）？</b></summary><br>

遵守由政府/独立方/组织设定的一套标准，例如存储、处理或传输支付相关信息的行业需要符合 PCI DSS（支付卡行业数据安全标准）。其他合规性示例可以是组织符合其自身政策的情况。

</details>

<details>
<summary><b>什么是 WAF 以及它的类型是什么？</b></summary><br>

**WAF** 代表 Web 应用防火墙。它用于通过过滤恶意流量来保护应用程序。**WAF** 可以是盒式或基于云端的。

</details>

### :diamond_shape_with_a_dot_inside: <a name="senior-sysadmin">高级系统管理员</a>

###### 系统问题 (61)

<details>
<summary><b>解释你负责的当前架构并指出它在哪里是可扩展或容错的。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>告诉我代码如何在你当前的生产中部署。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>有哪些不同类型的内核？解释。</b></summary><br>

**单体内核 (Monolithic Kernels)**

在这种类型的内核架构的早期，所有基本系统服务（如进程和内存管理、中断处理等）都被打包到内核空间中的单个模块中。这种架构导致了一些严重的缺点：

- 内核的大小，这非常大
- 可维护性差，这意味着修复错误或添加新功能会导致重新编译整个内核，这可能消耗数小时

在现代单体架构方法中，内核由可以动态加载和卸载的不同模块组成。这种模块化方法允许轻松扩展操作系统的功能。采用这种方法后，内核的可维护性变得非常容易，因为每次特定模块有更改或错误修复时只需加载和卸载受影响的模块即可。

Linux 遵循单体模块化方法。

**微内核 (Microkernels)**

这种架构主要解决了我们在单体方法中无法控制的不断增长的代码大小的问题。此架构允许一些基本服务（如设备驱动程序管理、协议栈、文件系统等）在用户空间中运行。

在这种架构中，所有被制成用户空间一部分的基本操作系统服务都被制作成作为服务器运行的程序，这些程序通过进程间通信 (IPC) 由系统中的其他程序使用。

例如：我们有用于设备驱动程序、网络协议栈、文件系统、图形等的服务器。微内核服务器本质上与其他守护进程程序一样，除了内核授予其中一些特权以与通常对大多数程序关闭限制的物理内存部分进行交互。

**混合内核（模块化内核）(Hybrid Kernels (Modular Kernels))**

这是上述两者的结合，关键思想是操作系统服务在 Kernel Space 中，没有消息传递，没有性能开销以及将服务放在用户空间中的可靠性好处。

这由 Microsoft 的 NT 内核使用，一直到最新的 Windows 版本。

有用资源：

- [内核简介。计算设备的核心。（原版）](https://keetmalin.wixsite.com/keetmalin/single-post/2017/08/24/An-Introduction-to-Kernels-The-Heart-of-Computing-Devices)

</details>

<details>
<summary><b>程序返回缺少库的错误。如何提供动态链接库？</b></summary><br>

环境变量 `LD_LIBRARY_PATH` 是一个冒号分隔的目录列表，应该在标准目录集之前首先搜索这些目录中的库；这在调试新库或使用非标准库进行特殊用途时很有用。

使用 `LD_LIBRARY_PATH` 的最佳方法是在执行该程序之前在命令行或脚本上设置它。这样新的 `LD_LIBRARY_PATH` 与系统的其余部分隔离开来。

使用示例：

```bash
export LD_LIBRARY_PATH="/list/of/library/paths:/another/path" ./program
```

有用资源：

- [如何正确使用 LD_LIBRARY_PATH](http://wiredrevolution.com/system-administration/how-to-correctly-use-ld_library_path)

</details>

<details>
<summary><b>为新手管理员写出安全使用 root 特权的最重要规则。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>在多个系统上同步 UID/GID 的优势是什么？</b></summary><br>

有几个原则原因，为什么你想要在网络中协调 **用户/UID** 和 **组/GID** 管理。

第一个相对明显——它与用户和管理便利性有关。

如果你的每个用户都期望在整个网络中的系统上有相对统一的访问权限，那么他们期望他们的相同用户名和密码在他们应该使用的每个系统上都能正常工作。如果他们更改了密码，他们将希望该更改是全局的。

它也与 Unix 和 Linux 中的名称和组名有关系。它们被映射为数字形式（分别是 **UID** 和 **GID**）。所有文件所有权（inode）和进程在整个内核和驱动程序中用于所有访问和身份确定使用这些数字值。这些数值通过显示或处理该信息的实用程序反向映射回其相应的原理符号表示（名称）。

还建议你采用 **UID** 不被重用的政策。当用户离开你的组织时，你“退休”他们的 **UID**（通过将他们的 passwd 设置为 * 来禁用访问权限，从组映射中删除它们，将他们的“shell”设置为某个 `/bin/denied` 二进制文件以及将他们的家目录设置为安全的 _墓地_——我在我的系统上使用 `/home/.graveyard`）。

原因可能不明显。但是，如果你维护几年的归档备份（或无限期），你将避免由于恢复一个（早已消失）用户的文件并发现它们由你的一个新用户拥有而导致的任何歧义和混淆。

有用资源：

- [UID/GID 同步和管理（原版）](https://linuxgazette.net/issue31/tag_uidgid.html)
- [在 Linux 机器上同步 UID/GID 的优势是什么？](https://serverfault.com/questions/603987/whats-the-advantage-of-synchronizing-uid-gid-across-linux-machines)
- [我如何在多台机器上保持用户账户一致？](https://unix.stackexchange.com/questions/141023/how-can-i-keep-user-acccounts-consistent-accross-multiple-machines)

</details>

<details>
<summary><b>成功进行系统性能调整应遵循哪些原则？***</b></summary><br>

待补充。

有用资源：

- [性能调整简介](https://www.oreilly.com/library/view/system-performance-tuning/059600284X/ch01.html)

</details>

<details>
<summary><b>描述 BSD 系统中的启动配置文件和目录。</b></summary><br>

在 BSD 中，主要的启动配置文件是 `/etc/defaults/rc.conf`。系统启动脚本如 `/etc/rc` 和 `/etc/rc.d` 只是包含此文件。

如果你想将其他程序添加到系统启动，你需要更改 `/etc/rc.conf` 文件而不是 `/etc/defaults/rc.conf`。

</details>

<details>
<summary><b>CPU 花了大部分时间来完成 IO 操作。你使用哪些工具来诊断什么进程确切地等待了 IO？如何最小化 IO 等待时间？***</b></summary><br>

待补充。

有用资源：

- [谁能精确解释什么是 IOWait？](https://serverfault.com/questions/12679/can-anyone-explain-precisely-what-iowait-is)

</details>

<details>
<summary><b>初级开发人员意外破坏了生产数据库。你如何防止这种情况发生？</b></summary><br>

**创建灾难恢复计划**

灾难恢复和业务连续性规划是组织整体风险管理不可或缺的一部分。它是记录的过程或一套程序，用于恢复和保护业务 IT 基础设施。

如果你没有恢复解决方案，那么你的恢复工作将成为从头开始重建的努力以重新创建任何丢失的内容。

你应该使用现实生活中常见的数据灾难场景来模拟在危机期间备份将和不会做什么。

**创建灾难恢复中心**

因此，在主位置运行出现计划外中断的情况下，服务和所有运营活动切换到备用中心，因此服务的不可用性限制为绝对最小值。

该设施是否有足够的带宽选项和电力来扩展和处理重大灾害期间的增加负载？是否有资源定期测试故障转移？

**创建定期备份并测试它！**

备份是保护数据投资的一种方式。通过拥有多个数据副本，如果其中一个被销毁也没关系（成本只是从备份中恢复丢失数据的成本）。

当你失去数据时，有一点是确定的：停机时间。

为了确保任何备份的有效性和完整性，必须定期进行还原测试。理想情况下，应在每次备份完成后进行测试以确保数据可以成功保存和恢复。然而，这通常由于缺乏可用资源或时间限制而不切实际。

制作整个虚拟机和其中重要组件的中间备份。

**创建快照：vm, 磁盘或 lvm**

如果你想从之前的状态恢复服务器，快照非常完美但它只是一个“快速方法”，它不能在太多项目更改后恢复系统。

始终在生产环境（不仅限于此）进行更改之前创建它们。

磁盘快照用于生成整个磁盘的快照。这些快照并不容易恢复单个数据块（例如丢失的用户账户），尽管这是可能的。主要目的是在磁盘故障的情况下恢复整个磁盘。

LVM 快照主要用于轻松地将生产环境中的数据复制到 staging 环境。

记住：快照不是备份！

**开发和测试环境**

生产环境是公司或客户使用的真实应用程序及其数据库实例。生产数据库拥有所有真实数据。

基于直接的生产数据库设置开发环境，而不是为此使用备份（消除了上述需求）。你的工程师可以访问的开发和测试环境以及只有少数人可以推送更新的 prod 环境遵循批准的更改。

所有环境如 prod、dev 和 test 应该有一个主要区别：服务授权数据。例如，测试环境上的 postgres 数据库实例应与生产数据库保持一致（如果可能），然而，为了消除数据库名称和登录密码的授权错误，应该是不同的。

**单点故障 (Single point of failure)**

避免单点故障的一般方法是提供每个必要资源的冗余组件，以便如果一个组件发生故障服务可以继续运行。

**数据库的同步和复制过程**

复制过程非常脆弱且容易出错。

一个好主意也是稍微延迟数据复制（例如对于 DRC）。由于在副本中，数据更改通常会在几分钟内复制，因此一旦这种情况发生，丢失的数据也不会出现在副本数据库中。

**创建具有用户、角色和权限的数据库模型，使用不同的保护方法**

只有非常高级的开发人员才拥有 db 管理员访问权限。其他人真的不需要写访问权限来克隆数据库。另一方面，只是不要给开发人员对 prod 的写访问权限。

生产数据库应该拒绝来自任何服务器和 pc 的连接，除非是运行生产应用程序的那个，即使它提供有效的用户名/密码。

开发机器怎么可能像那样直接访问生产数据库？关于一个简单的防火墙规则只让需要 DB 数据访问的服务器访问数据库怎么样？

**在故障后创建总结/事后文档 (Postmortem documents)**

事后会议的受众包括客户、直属下属、同事、公司执行团队和通常投资者。

按时间线解释导致停机的原因。每个事件都以特定时间的特定触发器开始，这通常会导致一些意外行为。例如，我们的服务器重启了，我们期望它们完好无损地回来，但这并没有发生。

此外，每个事件都有一个根本原因：重启本身是触发器，然而驱动程序中的错误导致了实际的停机。最后，每个事件都有后果，最明显的是站点宕机。

事后会议回答了关于什么可以防止停机的最重要问题。

尽管停机可能很痛苦，但你能做的最糟糕的事情就是掩盖它并且从不以清晰透明的方式关闭该事件。

**如果你也犯了一个大错误...**

  > "*人类只是拥有更大计算机的猿类。*" - african_cheetah (Reddit)
  >
  > "*我开始欣赏无法访问我绝对不需要的东西。*" - warm_vanilla_sugar (Reddit)
  >
  > 将发生的事情记录在某处。编写设置指南。失败是有教育意义的。

有用资源：

- [在第一天上班时意外破坏了生产数据库...](https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/)
- [1月31日数据库停机的事后报告](https://about.gitlab.com/2017/02/10/postmortem-of-database-outage-of-january-31/)
- [如何编写事件报告/事后文档](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem)

</details>

<details>
<summary><b>如何在不停机的情况下在 Linux 服务器上添加新磁盘？如何在 LVM 中重新扫描并添加它？</b></summary><br>

待补充。

有用资源：

- [如何在不重启的情况下在 Linux CentOS 7 中添加新磁盘](https://linoxide.com/linux-how-to/add-new-disk-centos-7-without-rebooting/)

</details>

<details>
<summary><b>解释用于 Linux 中进程管理的每个系统调用。</b></summary><br>

有一些用于进程管理的系统调用。如下：

- `fork()`：它用于创建新进程
- `exec()`：它用于执行新进程
- `wait()`：它用于使进程等待
- `exit()`：它用于退出或终止进程
- `getpid()`：它用于查找唯一的进程 ID
- `getppid()`：它用于检查父进程 ID
- `nice()`：它用于偏置当前运行的进程属性

有用资源：

- [系统调用](http://faculty.salina.k-state.edu/tim/ossg/Introduction/sys_calls.html)

</details>

<details>
<summary><b>无法挂载根文件系统。为什么？***</b></summary><br>

待补充。

有用资源：

- ["挂载根文件系统"的确切含义是什么？](https://superuser.com/questions/193918/what-does-mounting-a-root-file-system-mean-exactly)
- [内核如何挂载根分区？](https://unix.stackexchange.com/questions/9944/how-does-a-kernel-mount-the-root-partition)

</details>

<details>
<summary><b>你必须删除 100GB 的文件。哪种方法是最优的？***</b></summary><br>

待补充。

有用资源：

- [有没有办法在不颠簸 IO/负载的情况下在 Linux 上删除 100GB 文件？](https://serverfault.com/questions/336917/is-there-a-way-to-delete-100gb-file-on-linux-without-thrashing-io-load)
- [rm 在有数百万文件的目录上](https://serverfault.com/questions/183821/rm-on-a-directory-with-millions-of-files)

</details>

<details>
<summary><b>解释 Linux 中的中断和中断处理程序。</b></summary><br>

这是低级处理的概览。我正在描述一个简单的典型架构，真实架构可能更复杂或以不影响此详细级别的方式不同。

当 **中断**发生时，处理器查看中断是否被屏蔽。如果是，则什么都不发生直到它们取消屏蔽。当中断变为未屏蔽时，如果有挂起的中断，处理器选择一个。

然后处理器通过分支到内存中的特定地址来执行中断。该地址处的代码称为 **中断处理程序**。当处理器分支到那里时，它屏蔽中断（以便中断处理程序拥有独占控制权）并将某些寄存器的内容保存到某个地方（通常是其他寄存器）。

中断处理程序做它必须做的事情，通常通过与触发中断的外围设备通信以发送或接收数据。如果中断是由计时器引发的，则处理程序可能会触发 OS 调度器切换到不同的线程。当处理程序执行完毕后，它执行特殊的返回-from-interrupt 指令来恢复保存的寄存器和取消屏蔽中断。

中断处理程序必须快速运行，因为它防止任何其他中断运行。在 Linux 内核中，中断处理分为两部分：

- “上半部分”是中断处理程序。它做最少必要的事情，通常与硬件通信并在内核内存中的某个地方设置标志。
- “下半部分”做任何其他必要的处理，例如将数据复制到进程内存、更新内核数据结构等。它可以花时间甚至阻塞等待系统的另一部分运行，因为它以启用中断的方式运行。

有用资源：

- [Linux 中如何处理中断？（原版）](https://unix.stackexchange.com/questions/5788/how-is-an-interrupt-handled-in-linux)
- [中断和中断处理程序](https://notes.shichao.io/lkd/ch7/)

</details>

<details>
<summary><b>在设计高可用性应用程序时，在架构级别和应用级别需要考虑哪些因素？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>Inode 中存储了哪些字段？</b></summary><br>

在 POSIX 系统中，文件具有以下可以通过 stat 系统调用检索的属性：

- **设备 ID**（这标识包含文件的设备；也就是说，序列号的唯一性范围）。
文件序列号
- **文件模式**，它确定文件类型以及文件的拥有者、其组和其他人可以如何访问该文件
- **链接计数**，告诉有多少硬链接指向 inode
- 文件的 **用户 ID**
- 文件的 **组 ID**
- 如果它是设备文件，则是设备的 **设备 ID**。
- 文件的 **大小（字节）**
- **时间戳**，告诉 inode 本身上次何时修改 (ctime, inode change time)，文件内容最后何时修改 (mtime, modification time) 以及最后访问 (atime, access time)
- 首选的 **I/O 块大小**
- 分配给此文件的 **块数**

有用资源：

- [Inodes - 简介](http://www.grymoire.com/Unix/Inodes.html)

</details>

<details>
<summary><b>普通用户能够读取 <code>/etc/passwd</code>。这是一个安全漏洞吗？你知道其他密码阴影方案吗？</b></summary><br>

通常在大多数 Linux 系统上，_哈希密码_ 存储在 `/etc/shadow` 中：

```bash
-rw-r----- 1 root shadow 1349 2016-07-03 03:54 /etc/shadow
```

它们在 BSD 系统中存储在 `/etc/master.passwd` 中。

需要执行身份验证的程序仍然需要以 `root` 特权运行：

```bash
-rwsr-xr-x 1 root root 42792 2016-02-14 14:13 /usr/bin/passwd
```

如果你不喜欢 `setuid root` 程序和包含系统上所有哈希密码的单个文件，你可以用 **Openwall TCB PAM module** 替换它。这为每个用户提供了存储其哈希密码的自己的文件——因此系统中的 `setuid root` 程序数量可以大幅减少。

有用资源：

- [普通用户能够读取 /etc/passwd，这是一个安全漏洞吗？（原版）](https://serverfault.com/questions/286654/ordinary-users-are-able-to-read-etc-passwd-is-this-a-security-hole/286657#286657)
- [tcb - /etc/shadow 的替代品](https://www.openwall.com/tcb/)
- [为什么要阴影你的 passwd 文件？](https://www.tldp.org/HOWTO/Shadow-Password-HOWTO-2.html)

</details>

<details>
<summary><b>与 SysV init 相比，使用 systemd 的一些优势是什么？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>你如何在每次修改文件时运行命令？</b></summary><br>

例如：

```bash
while inotifywait -e close_write filename ; do

  echo "changed" >> /var/log/changed

done
```

</details>

<details>
<summary><b>你需要复制大量数据。解释最有效的方法。***</b></summary><br>

待补充。

有用资源：

- [在本地复制大型目录树？cp 还是 rsync？](https://serverfault.com/questions/43014/copying-a-large-directory-tree-locally-cp-or-rsync)

</details>

<details>
<summary><b>告诉我关于 LVM 的危险和注意事项。</b></summary><br>

**使用 LVM 的风险**

- 易受 SSD 或 VM 管理器的写缓存问题影响
- 由于更复杂的磁盘结构，数据恢复更难
- 正确调整文件系统大小更难
- 快照很难用、慢且有 bug
- 鉴于这些问题，需要一些技能才能正确配置

有用资源：

- [LVM 的危险和注意事项（原版）](https://serverfault.com/questions/279571/lvm-dangers-and-caveats)

</details>

<details>
<summary><b>你公司的 Python 开发团队面临着一个困境，要在 uwsgi 或 gunicorn 之间做出选择。从管理员的角度来看，每个解决方案的优缺点是什么？***</b></summary><br>

待补充。

有用资源：

- [uWSGI vs. Gunicorn，或者如何让 Python 比 Node 更快](https://blog.kgriffs.com/2012/12/18/uwsgi-vs-gunicorn-vs-node-benchmarks.html)

</details>

<details>
<summary><b>如果 <code>kill -9</code> 不起作用怎么办？描述使用 SIGKILL 不足的例外情况。</b></summary><br>

`kill -9` (`SIGKILL`) 总是有效的，只要你有权力杀死该进程。基本上要么进程必须由你启动且不是 setuid 或 setgid，或者你必须是 root。有一个例外：即使是 root 也不能向 PID 1（init 进程）发送致命信号。

然而 `kill -9` 并不保证立即生效。所有信号，包括 `SIGKILL`，都是异步传递的：内核可能需要时间来传递它们。通常，传递信号最多只需几微秒，只是目标获得时间片所需的时间。但是，如果目标阻塞了该信号，则该信号将被排队直到目标取消阻塞它。

正常情况下，进程不能阻止 `SIGKILL`。但内核代码可以，并且当进程调用系统调用时执行内核代码。

在系统调用中阻塞的进程处于不可中断睡眠状态。`ps` 或 `top` 命令将在（大多数 Unix）上以 **D** 状态显示它。

要移除 **D** 状态的进程，由于它是不可中断的，只有机器重启才能解决问题，除非它由系统自动处理。

通常进程长时间保持在 **D** 状态的机会非常少。如果确实如此，那么系统中有些东西没有被正确处理。这也可能是一个潜在的 bug。

长不可中断睡眠的经典案例是当服务器不响应时访问 NFS 上的文件的进程；现代实现往往不强加不可中断睡眠（例如在 Linux 下，intr 挂载选项允许信号中断 NFS 文件访问）。

你有时可能会在 `ps` 或 `top` 输出中看到标记为 **Z**（或在 Linux 下为 **H**）的条目。这些技术上不是进程，它们是僵尸进程，它们不过是进程表中的条目，保留以便父进程可以收到其子代死亡的通知。当父进程注意时（或死亡），它们将消失。

总结例外情况：

- 僵尸进程不能被杀死因为它们已经死了并等待它们的父进程来收割它们
- 处于阻塞状态的进程在再次唤醒之前不会死
- init 进程是特殊的：它不处理它不想处理的信号，因此它可以忽略 **SIGKILL**。此例外的一个例外是在 Linux 上 init 被 ptraced 时
- 不可中断睡眠的进程可能无法终止（并释放其资源），即使发送了 **SIGKILL**。这是 Unix 系统可能需要重启以解决临时软件问题的少数情况之一

有用资源：

- [如果 kill -9 不起作用怎么办？（原版）](https://unix.stackexchange.com/questions/5642/what-if-kill-9-does-not-work)
- [如果在 Linux 中 kill -9 没有效果，如何杀死进程](https://serverfault.com/questions/458261/how-to-kill-a-process-in-linux-if-kill-9-has-no-effect)
- [什么时候不应该 kill -9 一个进程？](https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process)
- [SIGTERM vs. SIGKILL](https://major.io/2010/03/18/sigterm-vs-sigkill/)

</details>

<details>
<summary><b><code>nohup</code>, <code>disown</code> 和 <code>&</code> 之间的区别。当一起使用时会发生什么？</b></summary><br>

- `&` 将作业放在后台，也就是说，使其尝试读取输入时阻塞，并使 shell 不等待其完成
- `disown` 从 shell 的作业控制中删除进程，但它仍然连接到终端。结果之一是 shell 不会向它发送 **SIGHUP**。显然，它只能应用于后台作业，因为你不能在运行前台作业时输入它
- `nohup` 将进程与终端断开连接，将其输出重定向到 `nohup.out` 并使其免受 **SIGHUP** 的影响。一个效果（命名方面）是进程不会收到任何发送的 **SIGHUP**。它与作业控制完全独立，原则上也可以用于前台作业（尽管这不是很实用）

如果你一起使用这三者，该进程在后台运行，从 shell 的作业控制中删除并有效地与终端断开连接。

有用资源：

- [nohup, disown 和 & 之间的区别（原版）](https://unix.stackexchange.com/questions/3886/difference-between-nohup-disown-and)

</details>

<details>
<summary><b>使用 <code>chroot</code> 的主要优势是什么？什么时候以及为什么我们使用它？在 chroot 环境中挂载 dev, proc, sys 的目的是什么？</b></summary><br>

拥有 chroot 环境的一个优势是文件系统与物理主机完全隔离。`chroot` 在文件系统中有一个单独的文件系统，区别在于它使用新创建的根(/)作为其根目录。

Chroot jail 是一种将进程及其子代与系统的其余部分隔离的方法。它应该只用于不以 root 身份运行的进程，因为 root 用户可以非常轻松地打破监狱。

想法是你创建一个目录树，在其中复制或链接所有系统文件以供进程运行。然后你使用 `chroot()` 系统调用将根目录更改为此新树的底部并开始在该 chroot'd 环境中运行的进程。由于它实际上不能引用修改后的根之外的路径，因此它不能在那些位置恶意地执行操作（读取/写入等）。

在 Linux 上，使用绑定挂载是填充 chroot 树的好方法。使用该功能，你可以拉入像 `/lib` 和 `/usr/lib` 这样的文件夹而不拉入 `/usr`，例如。只需将你想绑定的目录树绑定到你创建的监狱目录中的目录即可。

Chroot 环境用于：

- 重新安装引导加载程序
- 重置遗忘的密码
- 执行内核升级（或降级）
- 重建你的 initramdisk
- 修复你的 **/etc/fstab**
- 使用包管理器重新安装包
- 无论什么

在 chrooted 环境中工作时，有几个特殊的文件系统需要挂载以便所有程序正常运行。

限制是 `/dev`, `/sys` 和 `/proc` 默认不挂载但用于许多任务。

有用资源：

- [关于 Chroot 的一切](https://medium.com/@itseranga/chroot-316dc3c89584)
- [UNIX chroot() 操作的最佳实践](http://www.unixwiz.net/techtips/chroot-practices.html)
- [有没有比绑定挂载更容易的 chroot 方法？](https://askubuntu.com/questions/32418/is-there-an-easier-way-to-chroot-than-bind-mounting)
- [准备 chroot 以修复损坏的 Linux 安装的正确方法是什么？](https://superuser.com/questions/111152/whats-the-proper-way-to-prepare-chroot-to-recover-a-broken-linux-installation)

</details>

<details>
<summary><b>什么是段错误（segfaults），以及如何识别导致它们的原因？</b></summary><br>

**段错误**（又名 _segfault_）是导致程序崩溃的常见条件。段错误是由程序尝试读取或写入非法内存位置引起的。

程序内存被划分为不同的段：

- 用于程序指令的文本段
- 在编译时定义的变量和数组的数据段
- 子程序和函数中定义的临时（或自动）变量的栈段
- 由函数在运行时分配的变量的堆段，如 `malloc` (C)

在实践中，段错误几乎总是由于尝试读取或写入不存在的数组元素、在使用前未正确定义指针或在 C 程序中意外使用变量值作为地址。因此，当进程 A 读取内存位置 0x877 时，它读取的信息与进程 B 读取其自己的 0x877 时在 RAM 中的不同物理位置驻留的信息不同。

所有现代操作系统都支持和使用分段，因此都可以产生段错误。

在以下情况下也可能发生段错误：

- 有 bug 的程序/命令，只能通过应用补丁来修复
- 当你尝试访问 C 编程下数组末尾的数组时也会出现
- 在 chrooted jail 中，当缺少关键共享库、配置文件或 `/dev/` 条目时会发生这种情况
- 有时硬件或有故障的内存或驱动程序也会造成问题
- 维护建议的环境用于所有计算机设备（过热也可能产生这个问题）

要调试此类错误请尝试以下一种或全部技术：

- 启用核心文件：`$ ulimit -c unlimited`
- 重现崩溃：`$ ./<program>`
- 使用 gdb 调试崩溃：`$ gdb <program> [core file]`
- 或者运行 `LD_PRELOAD=...path-to.../libSegFault.so <program>` 以获取带有回溯、加载库等的报告

此外：

- 确保正确安装和配置硬件
- 始终应用所有补丁并使用更新的系统
- 确保监狱中安装了所有依赖项
- 为支持的服务（如 Apache）打开核心转储
- 使用 `strace`，这是一个有用的诊断、指令和调试工具

有时段错误不是由程序中的 bug 引起的，而是由于系统内存限制设置得太低。通常导致这种问题的原因是栈大小限制（栈溢出）。要检查内存限制，请在 bash 中使用 `ulimit` 命令。

有用资源：

- [什么是段错误（segfaults），我如何识别导致它们的原因？（原版）](https://kb.iu.edu/d/aqsj)
- [Linux 上的段错误是什么？](https://stackoverflow.com/questions/3200526/what-is-a-segmentation-fault-on-linux)
- [调用递归 bash 函数时发生段错误](https://unix.stackexchange.com/questions/296641/segmentation-fault-when-calling-a-recursive-bash-function)
- [故障排除分段违规/错误](http://web.mit.edu/10.001/Web/Tips/tips_on_segmentation.html)
- [可以使用 libSegFault.so 获取 SIGABRT 的回溯吗？](https://stackoverflow.com/questions/18706496/can-one-use-libsegfault-so-to-get-backtraces-for-sigabrt)

</details>

<details>
<summary><b>其中一个进程运行缓慢。你如何检查它已经运行了多长时间，你将使用哪些工具？</b></summary><br>

待补充。

有用资源：

- [我如何检查一个进程已经运行了多久？](https://unix.stackexchange.com/questions/7870/how-to-check-how-long-a-process-has-been-running)
- [Linux 中进程已经运行了多久？](https://www.cyberciti.biz/faq/how-to-check-how-long-a-process-has-been-running/)
- [我如何看到当前时间由进程执行的系统调用？](https://stackoverflow.com/questions/42677724/how-to-see-system-call-that-executed-in-current-time-by-process)

</details>

<details>
<summary><b>Linux 中的文件描述符（file descriptor）是什么？</b></summary><br>

在 Unix 和相关计算机操作系统中，文件描述符（FD，较少使用 fildes）是用于访问文件或任何其他输入/输出资源（如管道或网络套接字）的抽象指示器（句柄）。文件描述符构成 POSIX 应用程序编程接口的一部分。

</details>

<details>
<summary><b>你会建议哪种方式额外提供随机熵池以产生随机密码？如何改进它？</b></summary><br>

你应该使用 `/dev/urandom`，而不是 `/dev/random`。`/dev/random` 和 `/dev/urandom` 之间的两个区别是：

 - `/dev/random` 理论上在 _信息论安全算法的上下文中_ 可能更好。这是那种对当今技术、明天的技术以及外星人的技术和上帝自己的 iPad 都安全的算法。
 
 - `/dev/urandom` 不会阻塞，而 `/dev/random` 可能会这样做。`/dev/random` 维护一个“它还有多少熵”的计数器，假设它产生的任何位都是丢失的熵位。阻塞会引起非常现实的问题，例如服务器在自动安装后未能启动因为它在其 SSH 服务器密钥创建上停滞不前。

所以你想要使用 `/dev/urandom` 并停止担心这种熵业务。

诀窍是 `/dev/urandom` 从不阻塞，即使它应该：只要它在上次引导以来接收了足够的“初始熵”字节（32 个随机字节就足够了），`/dev/urandom` 就是安全的。正常的 Linux 安装将在安装时创建一个随机种子（来自 `/dev/random`）并将其保存在磁盘上。每次重启时，种子将被读取，馈送到 `/dev/urandom`，并立即生成一个新的种子（来自 `/dev/urandom`）以替换它。因此，这保证了 `/dev/urandom` 始终有足够的初始熵来产生密码学强的 alea，完全足以满足任何普通的加密工作，包括密码生成。

如果这些守护进程中的任何一个在耗尽所有可用熵时需要随机性，它们可能会暂停等待更多，这可能会导致你的应用程序中出现过度的延迟。更糟糕的是，由于大多数现代应用程序将要么 resort 到使用其在程序初始化时创建的自己的随机种子，要么使用 `/dev/urandom` 来避免阻塞，你的应用程序将从较低质量的随机数据中受到影响。这会影响你的安全通信的完整性，并增加对你的私人数据进行密码分析的机会。

要检查当前可用的熵字节量，请使用：

```bash
cat /proc/sys/kernel/random/entropy_avail
```

**rng-tools**

Fedora/Rh/Centos 类型：`sudo yum install rng-tools`。

在 deb 类型上：`sudo apt-get install rng-tools` 以设置它。

然后在生成密钥之前运行 `sudo rngd -r /dev/urandom`。

**haveged**

Fedora/Rh/Centos 类型：`sudo yum install haveged` 并将 `/usr/local/sbin/haveged -w 1024` 添加到 `/etc/rc.local`。

在 deb 类型上：`sudo apt-get install haveged` 并将 `DAEMON_ARGS="-w 1024"` 添加到 `/etc/default/haveged` 以设置它。

然后在生成密钥之前运行 `sudo rngd -r /dev/urandom`。

有用资源：

- [喂养 /dev/random 熵池？（原版）](https://security.stackexchange.com/questions/89/feeding-dev-random-entropy-pool)
- [GPG 没有足够的熵](https://serverfault.com/questions/214605/gpg-does-not-have-enough-entropy)

</details>

<details>
<summary><b><code>/sbin/nologin</code>, <code>/bin/false</code> 和 <code>/bin/true</code> 之间有什么区别？</b></summary><br>

当 `/sbin/nologin` 设置为 shell 时，如果使用该 shell 的用户登录，他们会收到一条礼貌的消息说“此账户当前不可用”。

`/bin/false` 只是一个二进制文件，当被调用时立即退出并返回 false，所以当有人以 false 作为 shell 登录时，他们在 false 退出时被立即注销。将 shell 设置为 `/bin/true` 具有不允许某人登录的相同效果，但 false 可能比 true 更好地传达这个人没有 shell 的概念。

`/bin/nologin` 是更用户友好的选项，给予尝试登录的用户一个可自定义的消息，所以理论上你想要使用那个；但是 nologin 和 false 都会有相同的最终结果，即某人没有 shell 并且无法 ssh 进来。

有用资源：

- [/sbin/nologin 和 /bin/false 之间有什么区别](https://unix.stackexchange.com/questions/10852/whats-the-difference-between-sbin-nologin-and-bin-false)
- [为什么一些系统用户有 /usr/bin/false 作为他们的 shell？](https://superuser.com/questions/1183311/why-do-some-system-users-have-usr-bin/false-as-the-shell)

</details>

<details>
<summary><b>磁盘瓶颈可能遭受哪些症状？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>FreeBSD 中错误 <code>maxproc limit exceeded by uid %i ...</code> 的含义是什么？</b></summary><br>

FreeBSD 内核只允许同时存在一定数量的进程。这个数字基于 **kern.maxusers** 变量。

**kern.maxusers** 还影响各种其他内核限制，如网络缓冲区。如果机器负载很重，增加 **kern.maxusers**。这将除了最大进程数之外增加这些其他系统限制。

要调整 **kern.maxusers** 值，请参阅手册中的文件/进程限制部分。虽然该部分指的是打开的文件，但相同的限制适用于进程。

如果机器负载很轻但运行着大量进程，请通过在 `/boot/loader.conf` 中定义它来调整 **kern.maxproc** 可调参数。

</details>

<details>
<summary><b>如何逐行读取文件并将值分配给变量？</b></summary><br>

例如：

```bash
while IFS='' read -r line || [[ -n "$line" ]] ; do
  echo "Text read from file: $line"
done < "/path/to/filename"
```

解释：

- `IFS=''`（或 `IFS=`）防止修剪前导/尾随空格。
- `-r` 防止反斜杠转义被解释。
- `|| [[ -n $line ]]` 防止最后一行被忽略，如果它不以 `\n` 结尾（因为当遇到 EOF 时 read 返回非零退出代码）。

有用资源：

- [逐行读取文件并将值分配给变量](https://stackoverflow.com/questions/10929453/read-a-file-line-by-line-assigning-the-value-to-a-variable)

</details>

<details>
<summary><b>客户报告他的站点在 ssllabs 扫描器中获得 B 级。准备 SSL 配置的最佳实践清单。***</b></summary><br>

有用资源：

- [获得完美的 SSL Labs 分数](https://michael.lustfield.net/nginx/getting-a-perfect-ssl-labs-score)
- [17 个小建议如何改进 ssllabs.com/ssltest/](https://community.qualys.com/thread/14023)
- [如何使用 Let's Encrypt 和 Nginx 在 SSL Labs 测试中以所有类别获得 A+ 和 100？](https://stackoverflow.com/questions/41930060/how-do-you-score-a-with-100-on-all-categories-on-ssl-labs-test-with-lets-encry)

</details>

<details>
<summary><b>CPU jumps 是什么意思？</b></summary><br>

操作系统是一个非常忙碌的东西，特别是当你让它做一些事情时（即使你没有）。而且当我们查看活跃的企业环境时，总有一些事情在发生。

大部分活动是“突发”的，意味着进程通常是静止的，但有短暂的强烈活动期。这肯定适用于任何类型的基于网络的活动（例如处理 PHP 请求），但也适用于 OS 维护（例如文件系统维护、页面回收、磁盘 I/O 请求）。

如果你有一个有很多这种突发进程的情况，你会得到一个非常不规则和尖刺的 CPU 使用率图。

正如 `500 - Internal Server Error` 所说，大量的上下文切换将使情况变得更糟。

有用资源：

- [“CPU jumps”是什么意思？（原版）](https://stackoverflow.com/questions/32185607/what-does-cpu-jumps-mean)

</details>

<details>
<summary><b>你如何在 Linux 中跟踪系统调用？解释可能的方法。</b></summary><br>

**SystemTap**

这是最强大的方法。它甚至可以显示调用参数：

用法：

```bash
sudo apt-get install systemtap
sudo stap -e 'probe syscall.mkdir { printf("%s[%d] -> %s(%s)\n", execname(), pid(), name, argstr) }'
```

然后在另一个终端上：

```bash
sudo rm -rf /tmp/a /tmp/b
mkdir /tmp/a
mkdir /tmp/b
```

示例输出：

```bash
mkdir[4590] -> mkdir("/tmp/a", 0777)
mkdir[4593] -> mkdir("/tmp/b", 0777)
```

**`strace` with `-f|-ff` params**

你可以使用 `-f` 和 `-ff` 选项。像这样：

```bash
strace -f -e trace=process bash -c 'ls; :'
```

- `-f` : 跟踪由当前正在跟踪的进程通过 fork(2) 系统调用创建子进程的结果。

- `-ff` : 如果 `-o filename` 选项生效，每个进程的跟踪写入 filename.pid，其中 pid 是每个进程的数值进程 ID。这与 `-c` 不兼容，因为没有每个进程的计数被保留。

**`ltrace -S` 显示系统调用和库调用**

这个很棒的工具因此提供了对可执行文件正在做什么的进一步可见性。

**`ftrace` 最小可运行示例**

这里有一个最小的可运行示例。以 `sudo` 运行：

```bash
#!/bin/sh
set -eux

d=debug/tracing

mkdir -p debug
if ! mountpoint -q debug; then
  mount -t debugfs nodev debug
fi

# Stop tracing.
echo 0 > "${d}/tracing_on"

# Clear previous traces.
echo > "${d}/trace"

# Find the tracer name.
cat "${d}/available_tracers"

# Disable tracing functions, show only system call events.
echo nop > "${d}/current_tracer"

# Find the event name with.
grep mkdir "${d}/available_events"

# Enable tracing mkdir.
# Both statements below seem to do the exact same thing,
# just with different interfaces.
# https://www.kernel.org/static/html/v4.18/trace/events.html
echo sys_enter_mkdir > "${d}/set_event"
# echo 1 > "${d}/events/syscalls/sys_enter_mkdir/enable"

# Start tracing.
echo 1 > "${d}/tracing_on"

# Generate two mkdir calls by two different processes.
rm -rf /tmp/a /tmp/b
mkdir /tmp/a
mkdir /tmp/b

# View the trace.
cat "${d}/trace"

# Stop tracing.
echo 0 > "${d}/tracing_on"

umount debug
```

示例输出：

```bash
# tracer: nop
#
#                              _-----=> irqs-off https://sourceware.org/systemtap/documentation.html
#                             / _----=> need-resched
#                            | / _---=> hardirq/softirq
#                            || / _--=> preempt-depth
#                            ||| /     delay
#           TASK-PID   CPU#  ||||    TIMESTAMP  FUNCTION
#              | |       |   ||||       |         |
            mkdir-5619  [005] .... 10249.262531: sys_mkdir(pathname: 7fff93cbfcb0, mode: 1ff)
            mkdir-5620  [003] .... 10249.264613: sys_mkdir(pathname: 7ffcdc91ecb0, mode: 1ff)
```

这种方法的一个很酷之处在于它同时显示系统上所有进程的功能调用，尽管你也可以使用 `set_ftrace_pid` 过滤感兴趣的 PID。

有用资源：

- [我如何在 Linux 中跟踪系统调用？（原版）](https://stackoverflow.com/questions/29840213/how-do-i-trace-a-system-call-in-linux)
- [ftrace 是否允许捕获对 Linux 内核的系统调用参数，还是只捕获函数名？](https://stackoverflow.com/questions/27608752/does-ftrace-allow-capture-of-system-call-arguments-to-the-linux-kernel-or-only)
- [如何仅使用 ftrace 跟踪系统调用事件而不显示 Linux 内核中的任何其他功能？](https://stackoverflow.com/questions/52764544/how-to-trace-just-system-call-events-with-ftrace-without-showing-any-other-funct)
- [在 Linux 中用于加载库的系统调用是什么？](https://unix.stackexchange.com/questions/226524/what-system-call-is-used-to-load-libraries-in-linux)

</details>

<details>
<summary><b>如何删除目录中的所有文件除了某些文件？</b></summary><br>

解决方案 1 - 使用 `extglob`：

```bash
shopt -s extglob
rm !(textfile.txt|backup.tar.gz|script.php|database.sql|info.txt)
```

解决方案 2 - 使用 `find`：

```bash
find . -type f -not -name '*txt' -print0 | xargs -0 rm --
```

</details>

<details>
<summary><b>如何在 Bash 中检查字符串是否包含子串？</b></summary><br>

你也可以在 case 语句之外使用 `*`（通配符），如果你使用双括号：

```bash
string='some text'
if [[ $string = *"My long"* ]] ; then
  true
fi
```

</details>

<details>
<summary><b>解释 <code>2>&-</code>, <code>2>/dev/null</code>, <code>|&</code>, <code>&>/dev/null</code> 和 <code>>/dev/null 2>&1</code> 之间的区别。</b></summary><br>

- **数字 1** = 标准输出（即 `STDOUT`）
- **数字 2** = 标准错误（即 `STDERR`）
- 如果没有明确给出数字，则 shell (bash) 假定 **数字 1**

首先让我们解决这些功能。

`2>&-`

这个的一般形式是 `M>&-`，其中 **"M"** 是一个文件描述符编号。这将关闭引用哪个文件描述符的输出，即 **"M"**。

`2>/dev/null`

这个的一般形式是 `M>/dev/null`，其中 **"M"** 是一个文件描述符编号。这会将文件描述符 **"M"** 重定向到 `/dev/null`。

`2>&1`

这个的一般形式是 `M>&N`，其中 **"M"** & **"N"** 是文件描述符编号。它将文件描述符 **"M"** 和 **"N"** 的输出组合成单个流。

`|&`

这仅仅是 `2>&1 |` 的缩写。它是在 Bash 4 中添加的。

`&>/dev/null`

这仅仅是 `>/dev/null 2>&1` 的缩写。它将文件描述符 2 (`STDERR`) 和描述符 1 (`STDOUT`) 重定向到 `/dev/null`。

`>/dev/null`

这仅仅是 `1>/dev/null` 的缩写。它将文件描述符 1 (`STDOUT`) 重定向到 `/dev/null`。

有用资源：

- [2>&-, 2>/dev/null, |&, &>/dev/null 和 >/dev/null 2>&1 之间的区别](https://unix.stackexchange.com/questions/70963/difference-between-2-2-dev-null-dev-null-and-dev-null-21)
- [第 20 章。I/O 重定向](http://www.tldp.org/LDP/abs/html/io-redirection.html)

</details>

<details>
<summary><b>如何在同一行中将 stderr 和 stdout 重定向到不同的文件？</b></summary><br>

只需将它们添加在一行 `command 2>> error 1>> output`。

然而，请注意 `>>` 用于追加如果文件已经有数据。而 `>` 将覆盖文件中任何现有数据。

所以，`command 2> error 1> output` 如果你不想追加。

只是为了完整性起见，你可以写 `1>` 为只是 `>` 因为默认文件描述符是输出。所以 `1>` 和 `>` 是一样的。

所以，`command 2> error 1> output` 变成，`command 2> error > output`。

</details>

<details>
<summary><b>具有 24 个核心的服务器上负载平均值超过 30 但 CPU 显示大约 70% 空闲。造成这种情况的常见原因之一是什么？如何调试和修复？</b></summary><br>

涉及磁盘 I/O 的请求可能会大大减慢，如果 cpu(s) 需要等待磁盘读取或写入数据。I/O Wait（I/O 等待）是 CPU 必须等待磁盘的时间百分比。

让我们看看如何使用一些终端命令行工具 (`top`, `atop` 和 `iotop`) 确认磁盘 I/O 是否正在减缓应用程序性能。

调试示例：

- 回答 I/O 是否导致系统变慢
- 找出哪个磁盘被写入
- 找出导致高 I/O 的进程
- 进程列表 **状态**
- 找出哪些文件被大量写入
- 你是否看到你的复制过程放入 **D** 状态等待由 pdflush 完成的 I/O 工作？
- 你是否在磁盘上看到沉重的同步写活动？

此外：

- 使用 `top` 命令 - 负载平均值和 wa (wait time)
- 使用 `atop` 命令监控 DSK (disk) I/O 统计信息
- 使用 `iotop` 命令获取磁盘读写的实时见解

为了提高性能：

- 检查驱动器阵列配置
- 检查磁盘排队算法并调整它们
- 调整一般块 I/O 参数
- 调整虚拟内存管理以提高 I/O 性能
- 检查和调整挂载选项和文件系统参数（也负责缓存）

有用资源：

- [Linux 服务器性能：是磁盘 I/O 减缓了你的应用程序吗？（原版）](https://haydenjames.io/linux-server-performance-disk-io-slowing-application/)
- [故障排除 Linux 中的高 I/O Wait](https://bencane.com/2012/08/06/troubleshooting-high-io-wait-in-linux/)
- [调试 Linux I/O 延迟](https://superuser.com/questions/396696/debugging-linux-i-o-latency)
- [pdflush, kjournald, swapd 等如何相互作用？](https://unix.stackexchange.com/questions/76970/how-do-pdflush-kjournald-swapd-etc-interoperate)
- [5 种提高 Linux 上 HDD 速度的方法](https://thecodeartist.blogspot.com/2012/06/improving-hdd-performance-linux.html)

</details>

<details>
<summary><b>如何在 SSH 中强制执行授权方法？在什么情况下它会很有用？</b></summary><br>

强制使用密码登录：

```bash
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no user@remote_host
```

强制使用密钥登录：

```bash
ssh -o PreferredAuthentications=publickey -o PubkeyAuthentication=yes -i id_rsa user@remote_host
```

有用资源：

- [如何强制 ssh 客户端仅使用密码认证？](https://unix.stackexchange.com/questions/15138/how-to-force-ssh-client-to-use-only-password-auth)

</details>

<details>
<summary><b>Postgres 出现 <code>Too many Open files</code> 错误。如何解决它？</b></summary><br>

通过将 `max_files_per_process` 减少到例如从默认值 1000 减少到 200 解决了该问题。此参数在 `postgresql.conf` 文件中，这设置了允许每个服务器子进程同时打开的最大文件数。

通常人们开始编辑 `/etc/security/limits.conf` 文件，但忘记了这个文件只适用于通过 PAM 系统积极登录的用户。

</details>

<details>
<summary><b>在什么情况下 <code>df</code> 和 <code>du</code> 会对可用磁盘空间产生分歧？你如何解决它？</b></summary><br>

`du` 检查目录的使用情况，但 `df` 检查已释放的 inode，并且在删除文件后文件可以保持打开并占用空间。

**解决方案 1**

检查位于挂载点下的文件。通常如果你将一个目录（例如 sambafs）挂载到已经有文件或目录的文件系统上，你就失去了看到这些文件的能力，但它们仍然消耗底层磁盘上的空间。

我在单用户模式下进行文件复制时将文件转储到我无法看到的目录中（由于其他目录系统在它们上面挂载）。

**解决方案 2**

另一方面 `df -h` 和 `du -sh` 可能不匹配约 50% 的硬盘大小。这是由例如 Apache (httpd) 在内存中保留大型日志文件引起的，这些文件已从磁盘删除。

这通过运行 `lsof | grep "/var" | grep deleted` 被追踪到，其中 `/var` 是我需要清理的分区。

输出显示这样的行：

```
httpd     32617    nobody  106w      REG        9,4 1835222944     688166 /var/log/apache/awstats_log (deleted)
```

然后通过重启 Apache (`service httpd restart`) 解决了这种情况并清除了磁盘空间，通过允许删除文件上的锁被清除。

有用资源：

- [为什么 du 和 df 在 Linux 和 Unix 中显示不同的值](https://linuxshellaccount.blogspot.com/2008/12/why-du-and-df-display-different-values.html)

</details>

<details>
<summary><b>加密和解密有什么区别？</b></summary><br>

**哈希 (Hashing)**：最后，哈希是一种形式的密码学安全，它与 **加密 (Encryption)** 不同，而 **加密** 是用于首先加密然后解密消息的两步过程，**哈希**将消息压缩成不可逆的固定长度值或哈希。

</details>

<details>
<summary><b>根证书应该放在服务器上吗？</b></summary><br>

**自签名根证书 (Self-signed root certificates)** 不需要/不应该包含在 Web 服务器配置中。它们没有任何用途（客户端将始终忽略它们）并且由于它们增加了 SSL 握手的大小而带来轻微的性能（延迟）损失。

如果客户端在他们的信任存储中没有根，那么它将不信任网站，而且没有办法解决这个问题。让 Web 服务器发送根证书无济于事——根证书必须来自受信任的第三方（大多数情况下是浏览器供应商）。

有用资源：

- [SSL 根证书可选？](https://security.stackexchange.com/questions/65332/ssl-root-certificate-optional)

</details>

<details>
<summary><b>如何记录在生产服务器上由 root 运行的所有命令？</b></summary><br>

`auditd` 是这里正确工作的工具：

1. 将这些 2 行添加到 `/etc/audit/audit.rules`：

```bash
-a exit,always -F arch=b64 -F euid=0 -S execve
-a exit,always -F arch=b32 -F euid=0 -S execve
```

这将跟踪由 root (euid=0) 运行的所有命令。为什么有两个规则？execve 系统调用必须在 32 位和 64 位代码中都被跟踪。

2. 为了摆脱日志中的 `auid=4294967295` 消息，在内核的 cmdline（通过编辑 `/etc/default/grub`）中添加 `audit=1`

3. 在登录相关的所有 PAM 配置文件（`/etc/pam.d/{login,kdm,sshd}`）中放置行，但在与 su 或 sudo 相关的文件中不放置。这将允许 auditd 正确获取调用用户的 uid 当调用 sudo 或 su 时。

现在重启你的系统。

让我们登录并运行一些命令：

```bash
$ id -u
1000
$ sudo ls /
bin  boot  data  dev  etc  home  initrd.img  initrd.img.old  lib  lib32  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  scratch  seLinux  srv  sys  tmp  usr  var  vmlinuz  vmlinuz.old
$ sudo su -
# ls /etc
[...]
```

现在读取 `/var/log/audit/auditd.log` 以显示已记录的内容。

有用资源：

- [记录在生产服务器上由管理员运行的所有命令](https://serverfault.com/questions/470755/log-all-commands-run-by-admins-on-production-servers)

</details>

<details>
<summary><b>如何防止 <code>dd</code> 冻结你的系统？</b></summary><br>

尝试使用 ionice：

```bash
ionice -c3 dd if=/dev/zero of=file
```

这以“空闲”IO 优先级启动 `dd` 进程：它只在其他进程不使用磁盘 IO 一段时间后获得磁盘时间。

当然，这仍然可以淹没缓冲区缓存并导致系统在将缓存刷新到磁盘时冻结。在 `/proc/sys/vm/` 下有可调参数来影响这一点，特别是 `dirty_*` 条目。

</details>

<details>
<summary><b>如何限制进程不超过 X% 的 CPU 使用率？</b></summary><br>

**nice/renice**

nice 是一个用于系统“一次性”调整的好工具：

```bash
nice COMMAND
```

**cpulimit**

如果你需要运行 CPU 密集型任务并且拥有空闲 CPU 时间对系统的响应能力至关重要，请使用 cpulimit：

```bash
cpulimit -l 50 COMMAND
```

**cgroups**

cgroups 将限制应用于一组进程，而不仅仅是其中一个：

```bash
cgcreate -g cpu:/cpulimited
cgset -r cpu.shares=512 cpulimited
cgexec -g cpu:cpulimited COMMAND_1
cgexec -g cpu:cpulimited COMMAND_2
cgexec -g cpu:cpulimited COMMAND_3
```

</details>

<details>
<summary><b>如何挂载临时 ram 分区？</b></summary><br>

```bash
# -t - 文件系统类型
# -o - 挂载选项
mount -t tmpfs tmpfs /mnt -o size=64M
```

</details>

<details>
<summary><b>如何杀死锁定文件的进程？</b></summary><br>

```bash
fuser -k filename
```

</details>

<details>
<summary><b>其他管理员试图调试服务器时意外输入了：<code>chmod -x /bin/chmod</code>。如何将权限重置回默认值？</b></summary><br>

```bash
# 1:
cp /bin/ls chmod.01
cp /bin/chmod chmod.01
./chmod.01 700 file

# 2:
/bin/busybox chmod 0700 /bin/chmod

# 3:
setfacl --set u::rwx,g::---,o::--- /bin/chmod

# 4:
/usr/lib/ld*.so /bin/chmod 0700 /bin/chmod
```

有用资源：

- [当你无法 chmod chmod 时你能做什么？](https://www.networkworld.com/article/3002286/operating-systems/what-can-you-do-when-you-cant-chmod-chmod.html)

</details>

<details>
<summary><b><code>grub></code> vs <code>grub-rescue></code>。解释。</b></summary><br>

- `grub>` - 这是它传递到的模式，如果你在配置文件之外找到运行系统所需的一切。使用此模式，我们可以访问大多数（如果不是全部）模块和命令。这可以通过按 'c' 键从菜单调用
- `grub-rescue` - 这是它传递到的模式，如果不可能找到自己的目录（特别是带有模块和附加命令的目录，例如 `/boot/grub/i386-pc`），如果其内容损坏或如果没有找到正常模块，则只包含基本命令

</details>

<details>
<summary><b>如何检查私钥和证书是否匹配？</b></summary><br>

```bash
(openssl rsa -noout -modulus -in private.key | openssl md5 ; openssl x509 -noout -modulus -in certificate.crt | openssl md5) | uniq
```

</details>

<details>
<summary><b>如何在不使用 <code>useradd</code>/<code>adduser</code> 命令的情况下添加新用户？</b></summary><br>

1. 在 <code>/etc/passwd</code> 中使用 `vipw` 添加用户详细信息条目：

```bash
# username:password:UID:GID:Comments:Home_Directory:Login Shell
user:x:501:501:test user:/home/user:/bin/bash
```

  > 注意语法。不要直接用编辑器编辑。`vipw` 锁定文件，因此其他命令不会尝试同时更新它。

2. 你将不得不在 <code>/etc/group</code> 中使用 `vigr`（与 `vipw` 类似的工具）创建同名的组：

```bash
user:x:501:
```

3. 为用户分配密码：

```bash
passwd user
```

4. 使用 mkdir 创建用户的主目录：

```bash
mkdir -m 0700 /home/user
```

5. 从 `/etc/skel` 复制文件到新主目录：

```bash
rsync -av --delete /etc/skel/ /home/user
```

6. 使用 `chown` 和 `chmod` 修复所有权和权限：

```bash
chown -R user:user /home/user
chmod -R go-rwx /home/user
```

有用资源：

- [在不使用 useradd/adduser 的情况下将用户添加到系统的步骤是什么？](https://unix.stackexchange.com/questions/153225/what-steps-to-add-a-user-to-a-system-without-using-useradd-adduser)

</details>

<details>
<summary><b>为什么我们需要 <code>mktemp</code> 命令？给出使用示例。</b></summary><br>

<code>mktemp</code> 随机化名称。从安全角度来看这非常重要。

想象一下，你在以 root 运行的脚本中做这样的事情：

```bash
echo "random_string" > /tmp/temp-file
```

而某人（读过你的脚本的人）做了

```bash
ln -s /etc/passwd /tmp/temp-file
```

<code>mktemp</code> 命令可以帮助你在以下情况：

```bash
TEMP=$(mktemp /tmp/temp-file.XXXXXXXX)
echo "random_string" > ${TEMP}
```

现在这个 <code>ln /etc/passwd</code> 攻击将不起作用。

</details>

<details>
<summary><b>在生产中将 <code>strace</code> 附加到正在运行的进程安全吗？后果是什么？</b></summary><br>

`strace` 是 Linux 的系统调用跟踪器。它目前使用神秘的 `ptrace()`（进程跟踪）调试接口，它以暴力的方式运行：**暂停目标进程**以便调试器读取状态进行每个系统调用。并且这样做两次：当系统调用开始时和结束时。

这意味着 `strace` 为每次系统调用暂停你的应用程序两次，并在应用程序和 `strace` 之间切换上下文。这就像在你的应用程序上放置交通计量灯。

缺点：

- 可能导致显著且有时巨大的性能开销，在最坏的情况下，使目标应用慢 100 倍以上。这不仅可能使其不适合生产使用，而且任何时序信息也可能被扭曲到具有误导性
- 不能同时跟踪多个进程（除了跟随的子进程）
- 可见性仅限于系统调用接口

有用资源：

- [strace Wow Much Syscall（原版）](http://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html)

</details>

<details>
<summary><b>删除 <code>-rf</code> 目录条目的最简单、最安全和最便携的方法是什么？</b></summary><br>

它们有效但不是最佳可移植性：

- <code>rm -- -fr</code>
- <code>perl -le 'unlink("-fr");'</code>

那些谈论 shell 命令行引用和字符转义的人几乎与那些甚至不认识到像那样的文件名会造成任何问题的人一样危险。

最便携的解决方案：

```bash
rm ./-fr
```

</details>

<details>
<summary><b>编写一个简单的 bash 脚本（或一对脚本）来备份和恢复你的系统。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>什么是加盐哈希？为 <code>/etc/shadow</code> 文件生成带有盐的密码。</b></summary><br>

**Salt (盐)** 在最基本的层面上是随机数据。当受保护的密码系统接收新密码时，它将创建该密码的哈希值，创建一个新的随机盐值，然后将该组合值存储在其数据库中。这有助于防御字典攻击和已知哈希攻击。

例如，如果用户在两个不同的系统上使用相同的密码，如果他们使用相同的哈希算法，他们可能最终得到相同的哈希值。然而，如果一个系统使用其哈希值的盐，这些值将不同。

`/etc/shadow` 文件中的加密密码以以下格式存储：

```bash
$ID$SALT$ENCRYPTED
```

`$ID` 表示加密类型，`$SALT` 是随机（最多 16 个字符）字符串和 `$ENCRYPTED` 是密码的哈希。

<table style="width:100%">
  <tr>
    <th>哈希类型</th>
    <th>ID</th>
    <th>哈希长度</th>
  </tr>
  <tr>
    <td>MD5</td>
    <td>$1</td>
    <td>22 个字符</td>
  </tr>
  <tr>
    <td>SHA-256</td>
    <td>$5</td>
    <td>43 个字符</td>
  </tr>
  <tr>
    <td>SHA-512</td>
    <td>$6</td>
    <td>86 个字符</td>
  </tr>
</table>

使用以下命令从 Linux shell 为 `/etc/shadow` 生成带有随机盐的哈希密码：

- 生成 **MD5** 密码哈希

```bash
python -c "import random,string,crypt; randomsalt = ''.join(random.sample(string.ascii_letters,8)); print crypt.crypt('MySecretPassword', '\$1\$%s\$' % randomsalt)"
```

- 生成 **SHA-256** 密码哈希

```bash
python -c "import random,string,crypt; randomsalt = ''.join(random.sample(string.ascii_letters,8)); print crypt.crypt('MySecretPassword', '\$5\$%s\$' % randomsalt)"
```

- 生成 **SHA-512** 密码哈希

```bash
python -c "import random,string,crypt; randomsalt = ''.join(random.sample(string.ascii_letters,8)); print crypt.crypt('MySecretPassword', '\$6\$%s\$' % randomsalt)"
```

</details>

###### 网络问题 (27)

<details>
<summary><b>为你的站点创建 SPF 记录以帮助控制垃圾邮件。</b></summary><br>

* 从 SPF 版本开始，这部分定义记录为 SPF。SPF 记录应始终以版本号 v=spf1（版本 1）开头，此标签将记录定义为 SPF。曾经有过第二个版本的 SPF（称为：SenderID），但已停止使用。

* 在包含 v=spf1 SPF 版本标签之后，你应该跟随所有授权代表你发送电子邮件的 IP 地址。例如：<code>v=spf1 ip4:34.243.61.237 ip6:2a05:d018:e3:8c00:bb71:dea8:8b83:851e</code>

* 接下来，你可以为每个代表你发送电子邮件的第三方组织包含一个 include 标签，例如 <code>include:thirdpartydomain.com.</code> 此标签表示该特定第三方被授权代表你的域发送电子邮件。你需要咨询第三方以了解哪个域名用作 'include' 语句的值。

* 一旦你实施了所有 IP 地址和 include 标签，你应该用 <code>~all</code> 或 <code>-all</code> 标签结束记录。all 标签是 SPF 记录的重要组成部分，因为它指示当 ISP 检测到未列在你的 SPF 记录中的服务器时应应用什么策略。如果未经授权的代表你的域发送电子邮件，将根据已发布的策略采取行动（例如拒绝邮件或将其标记为垃圾邮件）。这些标签之间有什么区别？你需要指示服务器需要多严格地对待邮件。<code>~all</code> 标签表示软失败，<code>-all</code> 表示硬失败。all 标签具有以下基本标记：<br><br>
`-all` – 未列在 SPF 记录中的服务器无权发送电子邮件（不符合的邮件将被拒绝）<br>
`~all` – 如果邮件来自未列出的服务器，则邮件将标记为软失败（邮件将被接受但标记）<br>
`+all` - 我们强烈建议不使用此选项，此标签允许任何服务器从你的域发送电子邮件<br>

* 在定义你的 SPF 记录之后，你的记录可能看起来像这样：
<code>v=spf1 ip4:34.243.61.237 ip6:2a05:d018:e3:8c00:bb71:dea8:8b83:851e include:thirdpartydomain.com -all</code>

有用资源：

- [SPF 记录检查器](https://www.dmarcanalyzer.com/spf/checker/)
- [SPF 语法](https://www.spf-record.com/syntax)


</details>

<details>
<summary><b>权威答案和非权威 DNS 查询答案之间有什么区别？***</b></summary><br>

权威 DNS 查询答案来自包含所查询域的 zone files（区域文件）的服务器。这是域管理员设置 DNS 记录的名服务器。非权威答案来自不托管域 zone files 的名服务器（例如，常用名服务器已缓存答案，如 Google 的 8.8.8.8 或 OpenDNS 208.67.222.222）。

</details>

<details>
<summary><b>如果你尝试解析主机名，你从 <code>host</code> 命令得到 <code>NXDOMAIN</code>。你的 <code>resolv.conf</code> 存储了两个名称服务器但只有第二个存储此域名。为什么本地解析器没有检查第二个名称服务器？</b></summary><br>

**NXDOMAIN** 不过是现存的互联网或内联网域名。如果无法使用 DNS 解析域名，则发生称为 **NXDOMAIN** 的条件。

`resolv.conf` 和 `resolver` 的默认行为是按列出的顺序尝试服务器。解析器将只在下一个名称服务器超时时尝试下一个名称服务器。

使用的算法是尝试名称服务器，如果查询超时，则尝试下一个，直到没有名称服务器，然后重复尝试所有名称服务器直到达到最大重试次数。

如果名称服务器响应 **SERVFAIL** 或引用（nofail）或终止查询（fail），也只使用第一个 dns 服务器。

示例：

```
nameserver 192.168.250.20   # it's not a dns
nameserver 8.8.8.8          # not store gate.test.int
nameserver 127.0.0.1        # store gate.test.int
```

所以如果你检查：

```
host -v -t a gate.test.int
Trying "gate.test.int"                        # trying first dns (192.168.250.20) but response is time out, so try the next nameserver
Host gate.test.int not found: 3(NXDOMAIN)     # ok but response is NXDOMAIN (not found this domain name)
Received 88 bytes from 8.8.8.8#53 in 43 ms
Received 88 bytes from 8.8.8.8#53 in 43 ms
                                              # so the last server in the list was not asked
```

为了避免这种情况，你可以使用例如 `nslookup` 命令，如果它从第一个名称服务器收到 **SERVFAIL**，它将使用第二个名称服务器。

有用资源：

- [第二名称服务器在 /etc/resolv.conf 中未被 wget 拾取](https://serverfault.com/questions/398837/second-nameserver-in-etc-resolv-conf-not-picked-up-by-wget)

</details>

<details>
<summary><b>探索你站点的当前 MTA 配置。MTA 中正在使用的一些特殊功能是什么？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>如何根据 IP 地址查找域名？你可以使用哪些技术/工具？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>是否可以为 IP 地址而不是域名拥有 SSL 证书？</b></summary><br>

只要它是公共 IP 地址，这是可能的（但很少使用）。

SSL 证书通常颁发给完全限定域名 (FQDN)，例如 `https://www.domain.com`。然而，一些组织需要颁发给公共 IP 地址的 SSL 证书。此选项允许你在证书签名请求 (CSR) 中将公共 IP 地址指定为通用名称。颁发的证书然后可用于直接保护与公共 IP 地址的连接（例如 `https://1.1.1.1`）。

根据 CA Browser 论坛，除非 IP 地址在 commonName 和 subjectAltName 字段中，否则用于地址的证书可能存在兼容性问题。这是由于未与 RFC 5280 对齐的传统 SSL 实现，特别是 Windows OS 早于 Windows 10。

有用资源：

- [SSL 证书是否绑定到服务器的 IP 地址？](https://stackoverflow.com/questions/1095780/are-ssl-certificates-bound-to-the-servers-ip-address)
- [公共 IP 地址的 SSL 证书？](https://serverfault.com/questions/193775/ssl-certificate-for-a-public-ip-address)

</details>

<details>
<summary><b>你如何为网站进行负载测试和容量规划？***</b></summary><br>

待补充。

有用资源：

- [你如何为网站进行负载测试和容量规划？（原版）](https://serverfault.com/questions/350454/how-do-you-do-load-testing-and-capacity-planning-for-web-sites)
- [你能帮我做我的容量规划吗？](https://serverfault.com/questions/384686/can-you-help-me-with-my-capacity-planning)
- [你如何为数据库进行负载测试和容量规划？](https://serverfault.com/questions/350458/how-do-you-do-load-testing-and-capacity-planning-for-databases)

</details>

<details>
<summary><b>开发人员报告与远程服务连接的问题。使用 <code>/dev</code> 进行故障排除。</b></summary><br>

```bash
# <host> - 设置远程主机
# <port> - 设置目标端口

# 1
timeout 1 bash -c "</dev/tcp/<host>/<port>" >/dev/null 2>&1 ; echo $?

# 2
timeout 1 bash -c 'cat < /dev/null > </dev/tcp/<host>/<port>' ; echo $?

# 2
&> echo > "</dev/tcp/<host>/<port>"
```

有用资源：

- [高级 Bash-Scripting Guide - /dev](http://www.tldp.org/LDP/abs/html/devref1.html#DEVTCP)
- [/dev/tcp as a weapon](https://securityreliks.wordpress.com/2010/08/20/devtcp-as-a-weapon/)
- [从 shell 脚本测试远程 TCP 端口是否打开](https://stackoverflow.com/questions/4922943/test-from-shell-script-if-remote-tcp-port-is-open)

</details>

<details>
<summary><b>我如何使用 <code>curl</code> 同时测量请求和响应时间？</b></summary><br>

`curl` 支持格式化输出以获取请求的详细信息（有关详细信息，请参阅 `curl` manpage，在 `-w| -write-out 'format'` 下）。就我们的目的而言，我们将只关注提供的时间细节。

1. 创建一个新文件 `curl-format.txt` 并粘贴以下内容：

```bash
    time_namelookup:  %{time_namelookup}\n
       time_connect:  %{time_connect}\n
    time_appconnect:  %{time_appconnect}\n
   time_pretransfer:  %{time_pretransfer}\n
      time_redirect:  %{time_redirect}\n
 time_starttransfer:  %{time_starttransfer}\n
                    ----------\n
         time_total:  %{time_total}\n
```

2. 发出请求：

```bash
curl -w "@curl-format.txt" -o /dev/null -s "http://example.com/"
```

这做了什么：

- `-w "@curl-format.txt"` - 告诉 cURL 使用我们的格式文件
- `-o /dev/null` - 将请求的输出重定向到 /dev/null
- `-s` - 告诉 cURL 不显示进度计
`http://example.com/` 是我们正在请求的 URL。如果 URL 有 "&" 查询字符串参数，请使用引号

</details>

<details>
<summary><b>你需要将 ext4 日志移动到另一个磁盘/分区。这样做的理由是什么？***</b></summary><br>

待补充。

有用资源：

- [ext4: 使用外部日志优化性能](https://raid6.com.au/posts/fs_ext4_external_journal/)
- [如何移动 ext4 日志](https://unix.stackexchange.com/questions/278998/how-to-move-an-ext4-journal)

</details>

<details>
<summary><b>在您的网站/应用程序前面有 Varnish 是否意味着您不需要关心负载均衡或冗余？</b></summary><br>

这取决于。Varnish 是缓存服务器，所以它的目的是缓存内容并充当反向代理，以加快数据检索速度并减轻 Web 服务器的负载。
Varnish 也可以配置为多个 Web 服务器的负载均衡器，但如果我们只使用一个 Varnish 服务器，这将成为我们基础设施中的单点故障。

确保负载均衡或冗余的更好解决方案将是至少两个 Varnish 实例的集群，以 active-active 模式或 active-passive 模式运行。

</details>

<details>
<summary><b>Varnish Cache 中的 hits, misses, 和 hit-for-pass 是什么？</b></summary><br>

**Hit (命中)** 是成功从缓存中提供请求的请求，**Miss (未命中)** 是通过缓存但发现空缓存并因此必须从源获取的请求，**hit-for-pass** 出现在 Varnish Cache 意识到它请求的一个对象是不可缓存的并且将导致传递时。

有用资源：

- [VCL 命中规则](https://book.varnish-software.com/4.0/chapters/VCL_Subroutines.html#vcl-vcl-hit)
- [VCL hit-for-pass 规则](https://book.varnish-software.com/4.0/chapters/VCL_Subroutines.html#hit-for-pass)
- [使用示例](https://book.varnish-software.com/4.0/chapters/VCL_Basics.html#vcl-backend-response)

</details>

<details>
<summary><b>给定以下参数，缓存内容的合理 TTL 是什么？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>开发人员说：<i><code>htaccess</code> 充满了魔法，应该使用它</i>。你对使用 <code>htaccess</code> 文件的看法如何？这对 Web 应用程序有什么影响</b></summary><br>

`.htaccess` 文件诞生于共享主机普遍存在的时代：

- sysadmins 需要一种方法来允许多个客户端在不同的账户下访问他们的服务器，并为他们的网站提供不同的配置。

`.htaccess` 文件允许他们修改 Apache 的工作方式而无需访问整个服务器。这些文件可以驻留在网站目录树中的任何和每个目录中，并为该目录及其内部的文件和文件夹提供功能。

**它对性能很糟糕**

为了让 `.htaccess` 工作，Apache 需要检查请求路径中的 EVERY（所有）目录以查找 `.htaccess` 文件的存在，如果存在则读取它们的每一个并解析它。这发生在每次请求时。记住你改变那个文件的那一刻它就生效了。这是因为 Apache 每次都读取它。

Web 服务器处理的每个单个请求——即使是最低级的 `.png` 或 `.css` 文件——导致 Apache：

- 查找当前请求目录中的 `.htaccess` 文件
- 然后从那里向上到服务器根目录查找每个目录中的 `.htaccess` 文件
- 合并所有这些 `.htaccess` 文件
- 使用新设置重新配置 Web 服务器
- 最后，交付文件

每个网页可以生成几十个请求。这是你不需要且完全不必要的开销。

**安全和权限损失**

允许个人用户使用 `.htaccess` 修改服务器的配置可能会引起安全问题，如果不妥善处理的话。如果你在 `.htaccess` 文件中添加任何指令，它将被视为添加到 Apache 配置文件。

这意味着非管理员可能编写这些文件从而“撤销”你的所有安全设置。如果你需要做临时性的事情，`.htaccess` 是一个好地方去做，如果你需要做更永久性的事情，只需将其放在 `/etc/apache/sites-available/site.conf`（或 `httpd.conf` 或其他服务器调用）中即可。

**总结**

如果你有访问 httpd 主服务器配置文件的权限，你应该完全避免使用 `.htaccess` 文件。如果它在 `.htaccess` 中工作，它也会在你的虚拟主机 `.conf` 文件中工作。

如果你无法避免使用 `.htaccess` 文件，你应该遵循这些规则。

- 只使用一个 `.htaccess` 文件或尽可能少
- 将 `.htaccess` 文件放在站点根目录中
- 保持你的 `.htaccess` 文件简短简单

有用资源：

- [喜欢 Apache: .htaccess](https://www.nginx.com/resources/wiki/start/topics/examples/likeapache-htaccess/)
- [除非必须否则不要使用 .htaccess](https://www.danielmorell.com/guides/htaccess-seo/basics/dont-use-htaccess-unless-you-must)

</details>

<details>
<summary><b>在生产中使用 SNI SSL 安全吗？如何测试带有和不带它的连接？在什么情况下它很有用？</b></summary><br>

使用 <b>OpenSSL</b>：

```bash
# Testing connection to remote host (with SNI support)
echo | openssl s_client -showcerts -servername google.com -connect google.com:443
# Testing connection to remote host (without SNI support)
echo | openssl s_client -connect google.com:443 -showcerts
```

使用 <b>GnuTLS</b>：

```bash
# Testing connection to remote host (with SNI support)
gnutls-cli -p 443 google.com
# Testing connection to remote host (without SNI support)
gnutls-cli --disable-sni -p 443 google.com
```

</details>

<details>
<summary><b>Cookies 如何在 HTTP 协议中传递？</b></summary><br>

服务器在其响应头中发送以下内容以设置 cookie 字段：

`Set-Cookie:name=value`

如果设置了 cookie，则浏览器在其请求头中发送以下内容：

`Cookie:name=value`

</details>

<details>
<summary><b>你如何防止处理具有未定义服务器名称的请求？没有定义的默认服务器规则会是安全问题吗？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>你应该将带有有效负载的 POST 重写为外部 API，但 POST 请求丢失了 URL 上传递的参数。如何解决这个问题（例如在 Nginx 中）以及这种行为的原因是什么？</b></summary><br>

问题是外部重定向永远不会重新发送 **POST** 数据。这是写入 HTTP 规范（检查 `3xx` 部分）。任何这样做客户端都违反了规范。

**POST** 数据是在请求的主体中传递的，如果你做标准重定向则会被丢弃。

看这个：

```
   +-------------------------------------------+-----------+-----------+
   |                                           | Permanent | Temporary |
   +-------------------------------------------+-----------+-----------+
   | Allows changing the request method from   | 301       | 302       |
   | POST to GET                               |           |           |
   | Does not allow changing the request       | 308       | 307       |
   | method from POST to GET                   |           |           |
   +-------------------------------------------+-----------+-----------+
```

你可以尝试使用 HTTP 状态代码 **307**，符合 RFC 的浏览器应该重复 post 请求。你只需要用 HTTP 状态代码 **307** 或 **308** 编写 Nginx rewrite 规则：

```bash
location / {
    proxy_pass              http://localhost:80;
    client_max_body_size    10m;
}

location /api {
    # HTTP 307 only for POST method.
    if ($request_method = POST) {
        return 307 https://api.example.com?request_uri;
    }

    # You can keep this for non-POST requests.
    rewrite ^ https://api.example.com?request_uri permanent;

    client_max_body_size    10m;
}
```

HTTP 状态代码 **307** 或 **308** 应该代替 **301** 使用，因为它将请求方法从 **POST** 更改为 **GET**。

有用资源：

- [Apache 上的重定向（保持 POST 参数）](https://stackoverflow.com/questions/17295085/redirection-on-apache-maintain-post-params)
- [为什么 HTTP 没有 POST 重定向？](https://softwareengineering.stackexchange.com/questions/99894/why-doesnt-http-have-post-redirect)

</details>

<details>
<summary><b>测试 NFS 性能的正确方法是什么？准备简短清单。
</b></summary><br>

最好的基准总是“你正常使用的应用程序(s)”。当你有 20 个人同时编译 Linux 内核时，NFS 系统上的负载与一群人同时登录或账户用作“本地 Web 服务器的 home directories”完全不同。

但我们有测试这个的一些好工具。

- <b>boonie</b> - 一个经典的性能评估工具测试。主程序测试对单个文件（或一组文件，如果你希望测试超过 1G 的存储）的数据库类型访问，并测试小文件的创建、读取和删除，这可以模拟 Squid, INN 或 Maildir 格式邮件等程序的使用。
- <b>DBench</b> - 旨在允许独立开发人员调试和测试 SAMBA。它深受原始 SAMBA 工具的启发。
- <b>IOZone</b> - 性能测试套件。POSIX 和 64 位兼容。这是 L.S.E. 的文件系统测试。主要功能：POSIX async I/O, Mmap() file I/O, Normal file I/O Single stream measurement, Multiple stream measurement, Distributed file server measurements (Cluster) POSIX pthreads, Multi-process measurement selectable measurements with fsync, O_SYNC Latency plots.

</details>

<details>
<summary><b>你需要阻止来自同一子网的几个 IP。系统遍历 iptables 规则集或黑洞路由的最有效方法是什么？</b></summary><br>

如果你的系统在路由表中定义了数千条路由并且在 iptables 规则中没有内容，那么输入 iptables 规则实际上可能更有效。

然而，在大多数系统中，路由表相当小，在这种情况下使用 null routes（空路由）实际上更有效。如果你已经广泛放置了 iptables 规则，这尤其如此。

假设你是基于源地址而不是目的地阻止，那么在 **raw/PREROUTING** 中做 **DROP** 将工作得很好，因为你基本上可以在做出任何路由决策之前丢弃数据包。

然而请记住，iptables 规则本质上是一个链表，为了在阻止多个地址时获得最佳性能，你应该使用 `ipset`。

另一方面，如果按目的地阻止，则在路由表与 iptables 之间可能几乎没有区别，**除非**源 IP 被欺骗在这种情况下黑洞条目可能会消耗路由缓存资源；在这种情况下，**raw/PREROUTING** 仍然是首选。

你的出站路线在你尝试向攻击者发送数据包之前不会重要。到那时你已经付出了大部分套接字设置的代价，甚至可能有线程阻塞等待内核得出你没有主机的路由，加上你的服务器进程在得出结论有网络问题时所做的任何错误处理。

iptables 或其他防火墙将允许你阻止传入流量并在它到达服务器上的守护进程进程之前丢弃它。在这个用例中显然优越得多。

```bash
iptables -A INPUT -s 192.168.200.0/24 -j DROP
```

当你在 Linux/Unix 系统上定义路由时，它告诉系统在为了与指定 IP 地址通信你将需要将你的网络通信路由到这个特定地方。

当你定义空路由时，它只是告诉系统将指定给指定 IP 地址的网络通信丢弃。这意味着任何基于 TCP 的网络通信将无法建立，因为你的服务器将不再能够发送 SYN/ACK 回复。然而，任何基于 UDP 的网络通信仍然会收到；但是你的系统将不再向源 IP 发送任何响应。

虽然 iptables 可以接受链中的成千上万条规则，但链是顺序走直到在每个数据包上找到匹配项。所以，大量规则可能导致系统花费惊人的 CPU 时间穿过规则。

路由规则比 iptables 简单得多。在 iptables 中，匹配可以基于许多不同的变量，包括协议、源和目标数据包，甚至是在当前数据包之前发送的其他数据包。

在路由中，唯一重要的是远程 IP 地址，所以它很容易优化。此外，许多系统有很多路由规则。典型系统可能只有 5 或 10 个，但充当 BGP 路由器的东西可能有成千上万条。因此，长期以来一直有关于为特定数据包选择正确路线的大量优化。

用不太技术性的术语来说，这意味着你的系统将接收来自攻击者的数据但不再响应它。

```bash
ip route add blackhole 192.168.200.0/24
```

或者

```bash
ip route add 192.168.200.0/24 via 127.0.0.1
```

有用资源：

- [iptables DROP 和空路由之间的区别。](https://www.tummy.com/blogs/2006/07/27/the-difference-between-iptables-drop-and-null-routing/)

</details>

<details>
<summary><b>如何使用第二个远程主机运行 <code>scp</code>？</b></summary><br>

使用 `ssh`：

```bash
ssh user1@remote1 'ssh user2@remote2 "cat file"' > file
```

使用 `tar`（带压缩）：

```bash
ssh user1@remote1 'ssh user2@remote2 "cd path2; tar cj file"' | tar xj
```

使用 `ssh` 和端口转发隧道：

```bash
# First, open the tunnel
ssh -L 1234:remote2:22 -p 45678 user1@remote1

# Then, use the tunnel to copy the file directly from remote2
scp -P 1234 user2@localhost:file .
```

</details>

<details>
<summary><b>你如何减少动态网站的加载时间？</b></summary><br>

- 网页优化
- 缓存的 Web 页面
- 优质的 Web 托管
- 压缩文本文件
- apache/nginx 调整

</details>

<details>
<summary><b>当你在浏览器中输入 api.example.com 并按回车时，有哪些类型的 dns 缓存在工作？</b></summary><br>

浏览器检查其缓存中是否有域名（要查看 DNS Cache，转到 `chrome://net-internals/#dns`）。当此缓存失败时，它只是询问 OS 来解析域名。

OS 解析器有自己的缓存，它将检查。如果这失败了，它就 resort 到询问 OS 配置的 DNS 服务器。

OS 配置的 DNS 服务器通常由 DHCP 从路由器配置，其中 DNS 服务器可能是 ISP 的 DNS 服务器，通过互联网网关到路由器的 DHCP 配置。

在路由器有它自己的 DNS 服务器的情况下，它可能有它自己的缓存否则你应该被直接引导到你的 ISP 的 DNS 服务器通常在 OS 缓存被发现为空时。

有用资源：

- [当...发生时](https://github.com/alex/what-happens-when)
- [DNS 解释 - 你的浏览器如何找到网站](https://scotch.io/tutorials/dns-explained-how-your-browser-finds-websites)
- [Firefox 使 dns 缓存无效](https://stackoverflow.com/questions/13063496/firefox-invalidate-dns-cache)

</details>

<details>
<summary><b><code>Cache-Control: max-age=0</code> 和 <code>Cache-Control: no-cache</code> 之间有什么区别？</b></summary><br>

**当由源服务器发送时**

`max-age=0` 只是告诉缓存（和用户代理）响应从一开始就是过期的，所以他们应该重新验证响应（例如使用 If-Not-Modified header）然后再使用缓存副本，而 `no-cache` 告诉他们在使用缓存副本之前必须重新验证。

换句话说，缓存有时可能选择使用过期响应（尽管我相信他们必须然后添加 Warning header），但 `no-cache` 说无论什么都不能使用过期响应。也许当你生成页面中的棒球统计数据时你想要 SHOULD-revalidate 行为，但你想要电子商务购买的 MUST-revalidate 行为。

**当由用户代理发送时**

如果用户代理发送带有 `Cache-Control: max-age=0`（即“端到端重新验证”）的请求，那么沿途的每个缓存将重新验证其缓存条目（例如使用 If-Not-Modified header）一直到源服务器。如果回复然后是 304 (未修改)，则可以使用缓存实体。

另一方面，发送带有 `Cache-Control: no-cache`（即“端到端重载”）的请求不会重新验证并且服务器不得在响应时使用缓存副本。

</details>

<details>
<summary><b>设置 <code>Access-Control-Allow-Origin</code> 的安全风险是什么？</b></summary><br>

通过响应 <code>Access-Control-Allow-Origin: *</code>，请求的资源允许与每个来源共享。这基本上意味着任何站点都可以向你的站点发送 XHR 请求并访问服务器的响应，如果你没有实现这个 CORS 响应就不会发生这种情况。

所以任何站点都可以在他们的访客代表下向你的站点发出请求并处理其响应。如果你有类似基于浏览器自动提供的东西（cookie、基于 cookie 的会话等）实现的认证或授权方案，由第三方站点触发的请求也将使用它们。

</details>

<details>
<summary><b>使用 <code>netcat</code> 创建一次性 TCP 或 UDP 代理。</b></summary><br>

```bash
### TCP -> TCP
nc -l -p 2000 -c "nc [ip|hostname] 3000"

### TCP -> UDP
nc -l -p 2000 -c "nc -u [ip|hostname] 3000"

### UDP -> UDP
nc -l -u -p 2000 -c "nc -u [ip|hostname] 3000"

### UDP -> TCP
nc -l -u -p 2000 -c "nc [ip|hostname] 3000"
```

</details>

<details>
<summary><b>解释使用 <code>nmap</code> 避免防火墙的 3 种技术。</b></summary><br>

**使用欺骗地址 (Decoy addresses)**

```bash
# Generates a random number of decoys.
nmap -D RND:10 [target]

# Manually specify the IP addresses of the decoys.
nmap -D decoy1,decoy2,decoy3
```

在这种类型的扫描中，你可以指示 Nmap 从其他主机欺骗数据包。在防火墙日志中，不仅会有我们的 IP 地址，还会有欺骗者的 IP 地址，因此很难确定扫描是从哪个系统开始的。

**源端口号指定 (Source port number specification)**

```bash
nmap --source-port 53 [target]
```

许多管理员在配置防火墙时犯的一个常见错误是设置规则以允许来自特定端口号的所有传入流量。<code>--source-port</code> 选项的 Nmap 可用于利用此错误配置。你可以用于这种类型扫描的常用端口是：20, 53 和 67。

**附加随机数据 (Append Random Data)**

```bash
nmap --data-length 25 [target]
```

许多防火墙通过查看其大小来检查数据包以识别潜在端口扫描。这是因为许多扫描仪发送具有特定大小的数据包。为了避免这种类型的检测，你可以使用命令 <code>--data-length</code> 添加额外数据并发送与默认值不同大小的数据包。

**TCP ACK Scan (TCP ACK 扫描)**

```bash
nmap -sA [target]
```

总是最好发送 ACK 数据包而不是 SYN 数据包，因为如果远程计算机上有任何活动防火墙工作，由于 ACK 数据包，防火墙无法创建日志，因为防火墙将 ACK 数据包视为 SYN 数据包的响应。

有用资源：

- [Nmap - 避免防火墙的技术](https://pentestlab.blog/2012/04/02/nmap-techniques-for-avoiding-firewalls/)

</details>

###### Devops 问题 (5)

<details>
<summary><b>解释 Nagios 中的 Flap Detection（抖动检测）是如何工作的？</b></summary><br>

**Flapping (抖动)** 发生在服务或主机状态变化太频繁时，这会导致大量问题和恢复通知。

一旦你定义了 **Flapping**，解释 Nagios 如何检测到 **Flapping**。每当 Nagios 检查主机或服务状态时，它将检查它是否开始或停止 flapping。

Nagios 遵循以下给定程序来做到这一点：

- 存储过去 21 次主机或服务检查结果分析历史检查结果并确定在哪里发生状态变化/转换
- 使用状态转换来确定百分比状态改变值（变化的衡量）对于主机或服务
- 将百分比状态改变值与低和高 flapping 阈值进行比较

</details>

<details>
<summary><b>容器化相比虚拟化提供了哪些优势？</b></summary><br>

以下是容器化相对于虚拟化的优势：

- 容器提供实时配置和扩展，但 VM 提供缓慢的配置
- 与 VM 相比，容器是轻量级的
- 与容器相比，VM 的性能有限
- 容器具有比 VM 更好的资源利用率

</details>

<details>
<summary><b>从 Docker Hub 分发 Docker 应用程序（例如 Apache, MySQL）的方式对于生产环境来说好吗？描述安全问题及可能的解决方案。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>LXC 和 LXD 的一些常见用例来自以下要求...解释。</b></summary><br>

- 需要隔离的开发环境而不污染你的主机机器
- 生产服务器内的隔离以及在其自己的容器中运行多个服务的可能性
- 需要使用同一软件或多个不同操作系统的不同版本进行测试的需求
- 在没有物理主机上安装的情况下尝试不同的和新的 GNU/Linux 发行版发布
- 尝试使用或可能不使用一些玩耍后的软件开发栈的软件
- 在你的主要开发机器或生产服务器上安装许多类型的软件并长期维护它们
- 在实际在生产机器上执行任何安装或维护任务之前进行试运行
- 更好地利用和配置为不同用户或客户运行多个服务的服务器资源
- 高密度虚拟专用服务器 (VPS) 托管，其中需要隔离而无需全虚拟化成本
- 从容器中访问主机硬件比从虚拟机中访问复杂的方法更容易
- 具有不同自定义的多个构建环境

</details>

<details>
<summary><b>你必须准备一个 Redis 集群。你将如何确保安全性？</b></summary><br>

- 通过防火墙保护给定的 Redis 实例免受外部访问
- 如果只有本地客户端正在访问它，则将其绑定到 127.0.0.1
- 沙盒环境
- 启用 **AUTH**
- 启用 **Protected Mode (受保护模式)**
- 数据加密支持（例如 `spiped`）
- 禁用特定命令
- 用户 **ACLs (访问控制列表)**

有用资源：

- [Redis 安全](https://redis.io/topics/security)
- [关于 Redis 安全性的一些事情](http://antirez.com/news/96)

</details>

###### 网络安全问题 (5)

<details>
<summary><b>什么是 OWASP 应用安全验证标准？用几点解释。***</b></summary><br>

待补充。

</details>

<details>
<summary><b>什么是 CSRF？</b></summary><br>

**跨站请求伪造 (Cross Site Request Forgery)** 是 Web 应用程序漏洞，其中服务器不检查请求是否来自受信任的客户端。请求只是直接处理。它可以进一步通过检测此方法、示例和对策来遵循。

</details>

<details>
<summary><b>policies, processes 和 guidelines 之间有什么区别？</b></summary><br>

作为 **安全策略 (security policy)** 定义了组织的安全目标和安全框架。**流程 (Process)** 是详细的逐步如何文档，指定实施重要安全机制所必需的精确操作。**指南 (Guidelines)** 是可以定制并用于创建程序的推荐。

</details>

<details>
<summary><b>在 IDS 的情况下什么是误报和漏报？</b></summary><br>

当设备为实际上未发生的入侵生成警报时：这是 **误报 (false positive)**，如果设备没有生成任何警报而入侵确实发生了，这就是 **漏报 (false negative)** 的情况。

</details>

<details>
<summary><b>Web 服务器加固的 10 个快速要点。</b></summary><br>

示例：

- 如果机器是新安装，在操作系统安装和加固之前保护它免受恶意网络流量
- 为 `/tmp` 创建一个带有 `nodev`, `nosuid` 和 `noexec` 选项设置的单独分区
- 为 `/var`, `/var/log`, `/var/log/audit` 和 `/home` 创建单独的分区
- 启用随机虚拟内存区域放置
- 删除遗留服务（例如 `telnet-server`, `rsh`, `rlogin`, `rcp`, `ypserv`, `ypbind`, `tftp`, `tftp-server`, `talk`, `talk-server`）。
- 通过防火墙和其他访问控制技术限制对主机上运行的服务的连接到授权用户的服务
- 禁用源路由数据包接受
- 启用 **TCP/SYN** cookies
- 禁用 SSH root 登录
- 安装和配置 **AIDE**
- 安装和配置 **OSsec HIDS**
- 配置 **SELinux**
- 所有管理员或 root 访问必须记录
- 系统账户、组成员资格及其关联特权的完整性检查应该启用并测试
- 设置密码创建要求（例如使用 PAM）

有用资源：

- [安全加固 CentOS 7](https://highon.coffee/blog/security-harden-centos-7/)
- [CentOS 7 服务器加固指南](https://www.lisenet.com/2017/centos-7-server-hardening-guide/)

</details>

## <a name="secret-knowledge">秘密知识</a>

### :diamond_shape_with_a_dot_inside: <a name="guru-sysadmin">专家级系统管理员</a>

<details>
<summary><b>解释什么是事件驱动架构 (Event-Driven architecture) 以及它如何提高性能？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>应用程序遇到一些性能问题。你应该找到我们要优化的代码。如何在 Linux 环境中对应用进行性能分析（profile）？</b></summary><br>

> 理想情况下，我需要一个将附加到进程并记录定期快照的应用程序：内存使用量、线程数 CPU 使用率。

1. 你可以在批处理模式中使用 `top`。它以批处理模式运行直到它被杀死或 N 次迭代完成：

```bash
top -b -p `pidof a.out`
```

或者

```bash
top -b -p `pidof a.out` -n 100
```

2. 你可以在 shell 脚本中使用 ps（例如）：

```bash
ps --format pid,pcpu,cputime,etime,size,vsz,cmd -p `pidof a.out`
```

> 我需要一些在 Linux 机器上记录应用程序性能的手段。

1. 记录性能数据：

```bash
perf record -p `pidof a.out`
```

或者记录 10 秒：

```bash
perf record -p `pidof a.out` sleep 10
```

或者使用调用图（call graph）记录：

```bash
perf record -g -p `pidof a.out`
```

2) 分析记录的数据

```bash
perf report --stdio
perf report --stdio --sort=dso -g none
perf report --stdio -g none
perf report --stdio -g
```

**这是一个测试程序的性能分析示例**

1. 我运行我的测试程序（c++）：

```bash
./my_test 100000000
```

2. 然后我记录正在运行的进程的性能数据：

```bash
perf record -g  -p `pidof my_test` -o ./my_test.perf.data sleep 30
```

3. 然后我分析每个模块的负载：

```bash
perf report --stdio -g none --sort comm,dso -i ./my_test.perf.data

# Overhead  Command                 Shared Object
# ........  .......  ............................
#
    70.06%  my_test  my_test
    28.33%  my_test  libtcmalloc_minimal.so.0.1.0
     1.61%  my_test  [kernel.kallsyms]
```

4. 然后分析每个函数的负载：

```bash
perf report --stdio -g none -i ./my_test.perf.data | c++filt

# Overhead  Command                 Shared Object                       Symbol
# ........  .......  ............................  ...........................
#
    29.30%  my_test  my_test                       [.] f2(long)
    29.14%  my_test  my_test                       [.] f1(long)
    15.17%  my_test  libtcmalloc_minimal.so.0.1.0  [.] operator new(unsigned long)
    13.16%  my_test  libtcmalloc_minimal.so.0.1.0  [.] operator delete(void*)
     9.44%  my_test  my_test                       [.] process_request(long)
     1.01%  my_test  my_test                       [.] operator delete(void*)@plt
     0.97%  my_test  my_test                       [.] operator new(unsigned long)@plt
     0.20%  my_test  my_test                       [.] main
     0.19%  my_test  [kernel.kallsyms]             [k] apic_timer_interrupt
     0.16%  my_test  [kernel.kallsyms]             [k] _spin_lock
     0.13%  my_test  [kernel.kallsyms]             [k] native_write_msr_safe

  ...
```

5. 然后分析调用链：

```bash
perf report --stdio -g graph -i ./my_test.perf.data | c++filt

# Overhead  Command                 Shared Object                       Symbol
# ........  .......  ............................  ...........................
#
    29.30%  my_test  my_test                       [.] f2(long)
            |
            --- f2(long)
               |
                --29.01%-- process_request(long)
                          main
                          __libc_start_main

    29.14%  my_test  my_test                       [.] f1(long)
            |
            --- f1(long)
               |
               |--15.05%-- process_request(long)
               |          main
               |          __libc_start_main
               |
                --13.79%-- f2(long)
                          process_request(long)
                          main
                          __libc_start_main

  ...
```

所以在这一点上你知道你的程序在哪里花费时间。

做应用程序性能分析（profile）的简单方法是使用 `pstack` 实用程序或 `lsstack`。

另一个工具是 Valgrind。所以我推荐这个。首先运行程序：

```bash
valgrind --tool=callgrind --dump-instr=yes -v --instr-atstart=no ./binary > tmp
```

现在当它工作时，我们应该在其他窗口中开始性能分析（profile）我们运行：

```bash
callgrind_control -i on
```

这开启性能分析。要关闭并停止整个任务我们可以使用：

```bash
callgrind_control -k
```

现在我们有一些名为 callgrind.out.* 的文件在当前目录中。要查看性能分析结果请使用：

```bash
kcachegrind callgrind.out.*
```

我建议在下一个窗口点击 **Self** 列标题，否则它显示 `main()` 是最耗时的任务。

有用资源：

- [为了乐趣和利润而跟踪进程](http://techblog.rosedu.org/tracing-processes-for-fun-and-profit.html)

</details>

<details>
<summary><b>使用安装的包数量有限且 telnet 不可用的 Linux 系统。使用 sysfs 虚拟文件系统测试所有接口（除了 loopback）上的连接。</b></summary><br>

例如：

```bash
#!/usr/bin/bash

for iface in $(ls /sys/class/net/ | grep -v lo) ; do

  if [[ $(cat /sys/class/net/$iface/carrier) = 1 ]] ; then state=1 ; fi

done

if [[ $state -ne 0 ]] ; then echo "not connection" > /dev/stderr ; exit ; fi
```

</details>

<details>
<summary><b>写出两条减少被入侵系统影响的黄金法则。</b></summary><br>

1) **最小特权原则 (The principle of least privilege)**

你应该配置服务以使用完成服务的任务所需的最少权限的用户运行。这可以在他们进入机器后限制黑客。

例如，使用 Apache Web 服务器服务的零日漏洞破解系统的黑客很可能仅限于该进程可以访问的系统内存和文件资源。黑客将能够下载你的 html 和 php 源代码文件，并可能查看你的 mysql 数据库，但他们不应该能够获得 root 或扩展他们的入侵超出 apache-accessible 文件。

许多默认 Apache Web 服务器安装创建 'apache' 用户和组作为默认值，你可以轻松配置主 Apache 配置文件 (`httpd.conf`) 以使用那些组运行 apache。

2) **特权分离原则 (The principle of separation of privileges)**

如果你的网站只需要对数据库的只读访问权限，那么创建一个只有只读权限且仅对该数据库的账户。

**SElinux** 是创建安全上下文的不错的选择，`app-armor` 是另一个工具。**Bastille** 曾经是加固的选择。

通过将被攻破的服务的力量分离到它自己的“盒子”中来减少任何攻击的后果。

3) **白名单，而不是黑名单 (Whitelist, don't blacklist)**

你描述的是黑名单方法。白名单方法将更安全得多。

一个专属俱乐部永远不会试图列出每个人不能进来；他们将列出每个人可以进来并排除不在列表上的人。

同样，尝试列出所有不应该访问机器的东西注定要失败。限制对短程序/IP 地址/用户的访问将更加有效。

当然，像任何其他事情一样，这涉及一些权衡。具体来说，白名单非常不方便并且需要持续维护。

为了进一步在权衡中，你可以通过断开机器与网络的连接来获得很好的安全性。

**也很有趣的是：**

使用可用的工具。你不太可能做得比安全专家更好，所以利用他们的才能来保护自己。

- 公钥加密提供 excellent security
- 强制执行密码复杂性
- 理解你为什么做出上述规则的例外——定期审查你的例外情况
- 对失败负责，它让你保持警惕

有用资源：

- [如何防止零日攻击（原版）](https://serverfault.com/questions/391370/how-to-prevent-zero-day-attacks)

</details>

<details>
<summary><b>你在一个安全会议上。成员们争论在核心网络上建立 OpenBSD 防火墙。走到讲台上表达你对这个解决方案的看法。优缺点是什么以及为什么？***</b></summary><br>

待补充。

</details>

<details>
<summary><b>有没有一种方法可以在 Nginx 中使用 Access-Control-Allow-Origin header 允许多个跨域？</b></summary><br>

要匹配域名和子域名列表，这个正则表达式使它与字体一起工作变得容易：

```bash
location ~* \.(?:ttf|ttc|otf|eot|woff|woff2)$ {
   if ( $http_origin ~* (https?://(.+\.)?(domain1|domain2|domain3)\.(?:me|co|com)$) ) {
      add_header "Access-Control-Allow-Origin" "$http_origin";
   }
}
```

稍微更配置：

```bash
location / {

    if ($http_origin ~* (^https?://([^/]+\.)*(domainone|domaintwo)\.com$)) {
        set $cors "true";
    }

    # Nginx doesn't support nested If statements. This is where things get slightly nasty.
    # Determine the HTTP request method used
    if ($request_method = 'GET') {
        set $cors "${cors}get";
    }
    if ($request_method = 'POST') {
        set $cors "${cors}post";
    }

    if ($cors = "true") {
        # Catch all in case there's a request method we're not dealing with properly
        add_header 'Access-Control-Allow-Origin' "$http_origin";
    }

    if ($cors = "trueget") {
        add_header 'Access-Control-Allow-Origin' "$http_origin";
        add_header 'Access-Control-Allow-Credentials' 'true';
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
        add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';
    }

    if ($cors = "truepost") {
        add_header 'Access-Control-Allow-Origin' "$http_origin";
        add_header 'Access-Control-Allow-Credentials' 'true';
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
        add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';
    }

}
```

</details>

<details>
<summary><b>解释 <code>:(){ :|:& };:</code> 以及如果你已经登录到系统如何停止此代码？</b></summary><br>

这是一个 **Fork Bomb (分支炸弹)**。

- `:()` - 这定义了函数。`:` 是函数名，空括号表示它将不接受任何参数
- `{ }` - 这些字符显示函数定义的开头和结尾
- `:|:` - 它加载一个副本到内存中的函数 `:` 并将其输出管道传输到另一个必须加载到内存中的 `:` 函数的副本
- `&` - 这将使进程成为后台进程，因此即使父级自动杀死子进程也不会被杀死
- `:` - 最终 `:` 将再次执行该功能，从而引发连锁反应

保护多用户系统的最佳方法是使用 **PAM** 来限制用户可以使用的进程数量。我们知道分支炸弹的最大问题是它占用这么多进程的事实。

所以我们有两种尝试修复的方法，如果你已经登录到系统：
- 执行 **SIGSTOP** 命令停止进程：`killall -STOP -u user1`
- 如果你不能在命令行运行你必须使用 `exec` 强制它运行（由于所有进程都被使用）：`exec killall -STOP -u user1`

对于分支炸弹，你最好的方法是防止从一开始就变成太大的问题。

</details>

<details>
<summary><b>如何恢复被例如 Apache 打开的已删除文件？</b></summary><br>

如果文件已被删除但仍处于打开状态，这意味着该文件在文件系统中仍然存在（它具有 inode）但具有硬链接计数为 0。由于没有到文件的链接，你无法按名称打开它。也没有通过 inode 打开文件的设施。

Linux 通过 `/proc` 下的特殊符号链接公开打开的文件。这些链接称为 `/proc/12345/fd/42`，其中 12345 是进程的 **PID**，42 是该进程中的文件描述符编号。以与该进程相同的用户运行的程序可以访问该文件（读写执行权限与你删除文件时具有的权限相同）。

打开文件的名称仍然可见于符号链接的目标中：如果文件是 `/var/log/apache/foo.log`，则链接的目标是 `/var/log/apache/foo.log (deleted)`。

因此，你可以像这样恢复给定具有它打开的进程 **PID** 和描述符的打开删除文件的内容：

```bash
recover_open_deleted_file () {
  old_name=$(readlink "$1")
  case "$old_name" in
    *' (deleted)')
      old_name=${old_name%' (deleted)'}
      if [ -e "$old_name" ]; then
        new_name=$(TMPDIR=${old_name%/*} mktemp)
        echo "$oldname has been replaced, recovering content to $new_name"
      else
        new_name="$old_name"
      fi
      cat <"$1" >"$new_name";;
    *) echo "File is not deleted, doing nothing";;
  esac
}
recover_open_deleted_file "/proc/$pid/fd/$fd"
```

如果你只知道进程 **ID** 但不知道描述符，你可以恢复所有文件：

```bash
for x in /proc/$pid/fd/* ; do
  recover_open_deleted_file "$x"
done
```

如果你也不知道进程 **ID**，你可以在所有进程中搜索：

```bash
for x in /proc/[1-9]*/fd/* ; do
  case $(readlink "$x") in
    /var/log/apache/*) recover_open_deleted_file "$x";;
  esac
done
```

你还可以通过解析 `lsof` 的输出获得此列表，但它不简单也不更可靠或不更可移植（这无论如何是 Linux 特定的）。

</details>

<details>
<summary><b>管理员团队需要你的支持。你必须远程重新安装一台主要服务器上的系统。没有访问管理控制台（例如 iDRAC）的权限。如何从另一个运行中的 Linux 在磁盘上安装 Linux？</b></summary><br>

问题可能是：“_系统和位置已经运行的其他系统级别安装_”。

以 Debian GNU/Linux 发行版为例。

1. 创建工作目录并使用 debootstrap 工具下载系统。

```bash
_working_directory="/mnt/system"
mkdir $_working_directory
debootstrap --verbose --arch amd64 {wheezy|jessie} . http://ftp.en.debian.org/debian
```

2. 挂载子系统：`proc`, `sys`, `dev` 和 `dev/pts`。

```bash
for i in proc sys dev dev/pts ; do mount -o bind $i $_working_directory/$i ; done
```

3. 复制系统备份以恢复。

```bash
cp system_backup_22012015.tgz $_working_directory/mnt
```

然而，最好不浪费空间并以不同方式执行（假设副本在 `/mnt/backup`）：

```bash
_backup_directory="${_working_directory}/mnt/backup"
mkdir $_backup_directory && mount --bind /mnt/backup $_backup_directory
```

4. Chroot 到“新”系统。

```bash
chroot $_working_directory /bin/bash
```

5. 更新已挂载设备的信息。

```bash
grep -v rootfs /proc/mounts > /etc/mtab
```

6. 在“新”系统中，接下来要做的是挂载包含“旧”系统的磁盘（例如 `/dev/sda1`）。

```bash
_working_directory="/mnt/old_system"
_backup_directory="/mnt/backup"
mkdir $_working_directory && mount /dev/sda1 $_working_directory
```

7. 删除旧系统的所有文件。

```bash
for i in $(ls | awk '!(/proc/ || /dev/ || /sys/ || /mnt/)') ; do rm -fr $i ; done
```

8. 下一步是从备份恢复系统。

```bash
tar xzvfp $_backup_directory/system_backup_22012015.tgz -C $_working_directory
```

9. 并在新的工作目录中挂载 `proc`, `sys`, `dev` 和 `dev/pts`。

```bash
for i in proc sys dev dev/pts ; do mount -o bind $i $_working_directory/$i ; done
```

10. 安装并更新 grub 配置。

```bash
chroot $_working_directory /bin/bash -c "grub-install --no-floppy --root-directory=/ /dev/sda"
chroot $_working_directory /bin/bash -c "update-grub"
```

11. 卸载 `proc`, `sys`, `dev` 和 `dev/pts` 文件系统。

```bash
cd
grep $_working_directory /proc/mounts | cut -f2 -d " " | sort -r | xargs umount -n
```

没有可用的命令，即 `halt`, `shutdown` 或 `reboot` 将工作。你需要重新加载系统配置——为此使用 **kernel debugger**（不带 '**b**' 选项）：

```bash
echo 1 > /proc/sys/kernel/sysrq
echo reisu > /proc/sysrq-trigger
```

当然，建议完全重启机器以完全加载当前系统。为此：

```bash
sync ; reboot -f
```

</details>

<details>
<summary><b>Rsync 触发了单个 50 GB 文件上的 Linux OOM killer。OOM killer 如何决定首先杀死哪个进程？你如何控制这个？</b></summary><br>

主要发行版内核将 `/proc/sys/vm/overcommit_memory` 的默认值设置为零，这意味着进程可以请求比系统中当前空闲更多的内存。

如果进程耗尽性地使用内存，达到可能威胁系统稳定性的程度，那么 **OOM killer** 就会出现。

注意：**OOM Killer** 的任务是继续杀死进程直到释放足够的内存以便内核试图运行的其余过程的顺利运行。

**OOM Killer** 必须选择要杀死的最佳进程（es）。这里的最佳是指该过程在杀死时将释放最大内存并且对系统最不重要的过程。

主要目标是杀死最少数量的进程以最小化造成的损害，同时最大化释放的内存量。

为了促进这一点，内核为每个进程维护一个 `oom_score`。你可以在 `/proc` 文件系统下的 pid 目录中看到每个进程的 oom_score。

  > 分析 OOM killer 日志时，重要的是查看触发它的因素。

```bash
cat /proc/10292/oom_score
```

任何进程的 `oom_score` 值越高，它在内存不足情况下被 **OOM Killer** 杀死的几率就越大。

如果你想创建一个包含应该首先接收 **OOM killer's** 注意的进程列表的特殊控制组，请在 `/mnt/oom-killer` 下创建一个目录来表示它：

```bash
mkdir lambs
```

将 `oom.priority` 设置为足够高的值：

```bash
echo 256 > /mnt/oom-killer/lambs/oom.priority
```

`oom.priority` 是 64 位无符号整数，可以具有无符号 64 位数所能持有的最大值。在扫描要杀死的进程时，**OOM-killer** 从具有最高 `oom.priority` 值的任务列表中选择一个进程。

将进程的 PID 添加到要添加到任务列表的进程中：

```bash
echo <pid> > /mnt/oom-killer/lambs/tasks
```

要创建一个不会被 **OOM-killer** 杀死的进程列表，请创建一个包含进程的目录：

```bash
mkdir invincibles
```

将 `oom.priority` 设置为零将使此 cgroup 中的所有进程被排除在目标进程列表之外。

```bash
echo 0 > /mnt/oom-killer/invincibles/oom.priority
```

要将更多进程添加到此组，将任务的 pid 添加到 invincible 组中的任务列表中：

```bash
echo <pid> > /mnt/oom-killer/invincibles/tasks
```

有用资源：

- [Rsync 触发了单个 50 GB 文件上的 Linux OOM killer](https://serverfault.com/questions/724469/rsync-triggered-linux-oom-killer-on-a-single-50-gb-file)
- [驯服 OOM killer](https://lwn.net/Articles/317814/)

</details>

<details>
<summary><b>你有很多套接字，挂在 <code>TIME_WAIT</code> 中。你的 http 服务后面代理服务器提供大量的小 http 请求。如何检查和减少 <code>TIME_WAIT</code> 套接字？***</b></summary><br>

待补充。

有用资源：

- [如何减少 TIME_WAIT 中的套接字数量？](https://serverfault.com/questions/212093/how-to-reduce-number-of-sockets-in-time-wait)

</details>

<details>
<summary><b><code>SO_REUSEADDR</code> 和 <code>SO_REUSEPORT</code> 有什么区别？解释所有套接字实现。***</b></summary><br>

待补充。

</details>