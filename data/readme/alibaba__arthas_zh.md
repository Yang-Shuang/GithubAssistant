## Arthas

![arthas](site/docs/.vuepress/public/images/arthas.png)

[![Build Status](https://github.com/alibaba/arthas/workflows/JavaCI/badge.svg)](https://github.com/alibaba/arthas/actions)
[![download](https://img.shields.io/github/downloads/alibaba/arthas/total?label=Downloads)](https://github.com/alibaba/arthas/releases/latest)
[![maven](https://img.shields.io/maven-central/v/com.taobao.arthas/arthas-packaging.svg)](https://search.maven.org/search?q=g:com.taobao.arthas)
![license](https://img.shields.io/github/license/alibaba/arthas.svg)
[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/alibaba/arthas.svg)](https://isitmaintained.com/project/alibaba/arthas "Average time to resolve an issue")
[![Percentage of issues still open](https://isitmaintained.com/badge/open/alibaba/arthas.svg)](https://isitmaintained.com/project/alibaba/arthas "Percentage of issues still open")
[![Leaderboard](https://img.shields.io/badge/Arthas-Check%20Your%20Contribution-orange)](https://opensource.alibaba.com/contribution_leaderboard/details?projectValue=arthas)

`Arthas` 是阿里巴巴开源的一款 Java 诊断（Java Diagnostic）工具。

Arthas 允许开发者在不修改代码或重启服务器的情况下，排查 Java 应用的生产环境问题。

[中文说明/Chinese Documentation](README_CN.md)

### Background

通常，本地开发环境无法直接访问生产系统网络。如果在生产环境中遇到问题，就无法使用 IDE 远程调试应用。更重要的是，在生产环境中进行调试是不可接受的，因为它会挂起所有线程，导致业务服务中断。 

开发者可以尝试在测试或预发环境中复现相同的问题。但这很棘手，因为某些问题在不同环境中难以复现，或者一旦重启就会消失。

如果你想着通过添加日志来辅助排查问题，就必须经历完整的生命周期流程；测试、预发，然后才能到生产环境。时间就是金钱！这种方法效率低下！此外，正如前面所述，JVM 重启后问题可能无法复现。

Arthas 正是为了解决这些问题而诞生的。开发者可以实时排查生产环境问题，无需重启 JVM，也无需修改代码。Arthas 作为一个观察者运行，绝不会挂起你现有的线程。

### Key features

* 检查类是否已加载，或类的加载位置。（排查 jar 包冲突非常有用）
* 反编译类，确保代码按预期运行。
* 查看 ClassLoader 统计信息，例如 ClassLoader 数量、每个 ClassLoader 加载的类数量、ClassLoader 层级结构、潜在的 ClassLoader 内存泄漏等。
* 查看方法调用详情，例如方法参数、返回值、抛出的异常等。
* 检查指定方法调用的堆栈跟踪。当开发者想知道该方法的调用者时非常有用。
* 追踪方法调用，查找缓慢的子调用。
* 监控方法调用统计信息，例如 QPS（每秒查询率）、RT（响应时间）、成功率等。
* 监控系统指标、线程状态和 CPU 使用率、GC 统计信息等。
* 支持命令行交互模式，并启用自动补全功能。
* 支持 Telnet 和 WebSocket，可通过命令行和浏览器进行本地及远程诊断。
* 支持 Profiler / Flame Graph（火焰图）
* 支持获取堆内存中指定类的实例对象。 
* 版本 4.x 支持 JDK 8+，包括 JDK 17、JDK 21 和 JDK 25。
* 支持 Linux/Mac/Windows。


### Online Tutorials(Recommended)

* [查看在线教程](https://arthas.aliyun.com/doc/arthas-tutorials.html?language=en)

### Quick start

#### Use `arthas-boot`(Recommended)

下载`arthas-boot.jar`，通过 `java` 命令启动：

```bash
curl -O https://arthas.aliyun.com/arthas-boot.jar
java -jar arthas-boot.jar
```

打印帮助信息：

```bash
java -jar arthas-boot.jar -h
```

#### Use `as.sh`

你可以在 Linux、Unix 和 Mac 上通过单行命令安装 Arthas。复制以下命令并粘贴到命令行中，然后按 *Enter* 键运行：

```bash
curl -L https://arthas.aliyun.com/install.sh | sh
```

上述命令会将引导脚本 `as.sh` 下载到当前目录。你可以将其移动到任意位置，或将其路径添加到 `$PATH` 环境变量中。

执行 `as.sh` 即可进入交互界面，或执行 `as.sh -h` 获取更多帮助信息。


### Documentation

* [在线教程(推荐)](https://arthas.aliyun.com/doc/arthas-tutorials.html?language=en)
* [用户手册](https://arthas.aliyun.com/doc/en)
* [安装](https://arthas.aliyun.com/doc/en/install-detail.html)
* [下载](https://arthas.aliyun.com/doc/en/download.html)
* [快速入门](https://arthas.aliyun.com/doc/en/quick-start.html)
* [高级用法](https://arthas.aliyun.com/doc/en/advanced-use.html)
* [命令](https://arthas.aliyun.com/doc/en/commands.html)
* [Web控制台](https://arthas.aliyun.com/doc/en/web-console.html)
* [Docker](https://arthas.aliyun.com/doc/en/docker.html)
* [Arthas Spring Boot Starter](https://arthas.aliyun.com/doc/en/spring-boot-starter.html)
* [用户案例](https://github.com/alibaba/arthas/issues?q=label%3Auser-case)
* [常见问题](https://arthas.aliyun.com/doc/en/faq)
* [编译调试/如何贡献](https://github.com/alibaba/arthas/blob/master/CONTRIBUTING.md)
* [发布说明](https://github.com/alibaba/arthas/releases)


### Feature Showcase

#### Dashboard

* https://arthas.aliyun.com/doc/en/dashboard

![dashboard](site/docs/.vuepress/public/images/dashboard.png)

#### Thread

* https://arthas.aliyun.com/doc/en/thread

一眼看清哪些线程正在消耗大量 CPU（按 CPU 使用率排名），以及它们当前在做什么：

```bash
$ thread -n 3
"as-command-execute-daemon" Id=29 cpuUsage=75% RUNNABLE
    at sun.management.ThreadImpl.dumpThreads0(Native Method)
    at sun.management.ThreadImpl.getThreadInfo(ThreadImpl.java:440)
    at com.taobao.arthas.core.command.monitor200.ThreadCommand$1.action(ThreadCommand.java:58)
    at com.taobao.arthas.core.command.handler.AbstractCommandHandler.execute(AbstractCommandHandler.java:238)
    at com.taobao.arthas.core.command.handler.DefaultCommandHandler.handleCommand(DefaultCommandHandler.java:67)
    at com.taobao.arthas.core.server.ArthasServer$4.run(ArthasServer.java:276)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
    at java.lang.Thread.run(Thread.java:745)

    Number of locked synchronizers = 1
    - java.util.concurrent.ThreadPoolExecutor$Worker@6cd0b6f8

"as-session-expire-daemon" Id=25 cpuUsage=24% TIMED_WAITING
    at java.lang.Thread.sleep(Native Method)
    at com.taobao.arthas.core.server.DefaultSessionManager$2.run(DefaultSessionManager.java:85)

"Reference Handler" Id=2 cpuUsage=0% WAITING on java.lang.ref.Reference$Lock@69ba0f27
    at java.lang.Object.wait(Native Method)
    -  waiting on java.lang.ref.Reference$Lock@69ba0f27
    at java.lang.Object.wait(Object.java:503)
    at java.lang.ref.Reference$ReferenceHandler.run(Reference.java:133)
```

#### jad

* https://arthas.aliyun.com/doc/en/jad

一键反编译你的类：

```java
$ jad javax.servlet.Servlet

ClassLoader:
+-java.net.URLClassLoader@6108b2d7
  +-sun.misc.Launcher$AppClassLoader@18b4aac2
    +-sun.misc.Launcher$ExtClassLoader@1ddf84b8

Location:
/Users/xxx/work/test/lib/servlet-api.jar

/*
 * Decompiled with CFR 0_122.
 */
package javax.servlet;

import java.io.IOException;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public interface Servlet {
    public void init(ServletConfig var1) throws ServletException;

    public ServletConfig getServletConfig();

    public void service(ServletRequest var1, ServletResponse var2) throws ServletException, IOException;

    public String getServletInfo();

    public void destroy();
}
```

#### mc
* https://arthas.aliyun.com/doc/en/mc

内存编译器，在内存中将 `.java` 文件编译为 `.class` 文件。

```bash
$ mc /tmp/Test.java
```

#### retransform

* https://arthas.aliyun.com/doc/en/retransform

加载外部 `*.class` 文件，以重新转换/热替换 JVM 中已加载的类。

```bash
retransform /tmp/Test.class
retransform -c 327a647b /tmp/Test.class /tmp/Test\$Inner.class
```

#### sc

* https://arthas.aliyun.com/doc/en/sc

搜索任意已加载类的详细信息。

```bash
$ sc -d org.springframework.web.context.support.XmlWebApplicationContext
 class-info        org.springframework.web.context.support.XmlWebApplicationContext
 code-source       /Users/xxx/work/test/WEB-INF/lib/spring-web-3.2.11.RELEASE.jar
 name              org.springframework.web.context.support.XmlWebApplicationContext
 isInterface       false
 isAnnotation      false
 isEnum            false
 isAnonymousClass  false
 isArray           false
 isLocalClass      false
 isMemberClass     false
 isPrimitive       false
 isSynthetic       false
 simple-name       XmlWebApplicationContext
 modifier          public
 annotation
 interfaces
 super-class       +-org.springframework.web.context.support.AbstractRefreshableWebApplicationContext
                     +-org.springframework.context.support.AbstractRefreshableConfigApplicationContext
                       +-org.springframework.context.support.AbstractRefreshableApplicationContext
                         +-org.springframework.context.support.AbstractApplicationContext
                           +-org.springframework.core.io.DefaultResourceLoader
                             +-java.lang.Object
 class-loader      +-org.apache.catalina.loader.ParallelWebappClassLoader
                     +-java.net.URLClassLoader@6108b2d7
                       +-sun.misc.Launcher$AppClassLoader@18b4aac2
                         +-sun.misc.Launcher$ExtClassLoader@1ddf84b8
 classLoaderHash   25131501

```


#### vmtool

* https://arthas.aliyun.com/doc/en/vmtool

获取堆内存中指定类的实例对象。

```bash
$ vmtool --action getInstances --className java.lang.String --limit 10
@String[][
    @String[com/taobao/arthas/core/shell/session/Session],
    @String[com.taobao.arthas.core.shell.session.Session],
    @String[com/taobao/arthas/core/shell/session/Session],
    @String[com/taobao/arthas/core/shell/session/Session],
    @String[com/taobao/arthas/core/shell/session/Session.class],
    @String[com.taobao.arthas.core.shell.session.Session.class],
    @String[com/taobao/arthas.core/shell/session/Session.class],
    @String[com/],
    @String[java/util/concurrent/ConcurrentHashMap$ValueIterator],
    @String[java/util/concurrent/locks/LockSupport],
]
```

#### stack

* https://arthas.aliyun.com/doc/en/stack

查看 `test.arthas.TestStack#doGet` 的调用栈：

```bash
$ stack test.arthas.TestStack doGet
Press Ctrl+C to abort.
Affect(class-cnt:1 , method-cnt:1) cost in 286 ms.
ts=2018-09-18 10:11:45;thread_name=http-bio-8080-exec-10;id=d9;is_daemon=true;priority=5;TCCL=org.apache.catalina.loader.ParallelWebappClassLoader@25131501
    @test.arthas.TestStack.doGet()
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:624)
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:731)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:303)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:52)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:220)
        at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:110)
        ...
        at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:169)
        at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:103)
        at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:116)
        at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:451)
        at org.apache.coyote.http11.AbstractHttp11Processor.process(AbstractHttp11Processor.java:1121)
        at org.apache.coyote.AbstractProtocol$AbstractConnectionHandler.process(AbstractProtocol.java:637)
        at org.apache.tomcat.util.net.JIoEndpoint$SocketProcessor.run(JIoEndpoint.java:316)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
        at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
        at java.lang.Thread.run(Thread.java:745)
```

#### Trace

* https://arthas.aliyun.com/doc/en/trace

使用 trace 命令查看是什么拖慢了你的方法调用：

![trace](site/docs/.vuepress/public/images/trace.png)

#### Watch

* https://arthas.aliyun.com/doc/en/watch

仅当抛出异常时，监控 `test.arthas.TestWatch#doGet` 的第一个参数和抛出的异常。

```bash
$ watch test.arthas.TestWatch doGet {params[0], throwExp} -e
Press Ctrl+C to abort.
Affect(class-cnt:1 , method-cnt:1) cost in 65 ms.
ts=2018-09-18 10:26:28;result=@ArrayList[
    @RequestFacade[org.apache.catalina.connector.RequestFacade@79f922b2],
    @NullPointerException[java.lang.NullPointerException],
]
```

#### Monitor

* https://arthas.aliyun.com/doc/en/monitor

监控特定方法的调用统计信息，包括总调用次数、平均响应时间、成功率等，每 5 秒输出一次：

```bash
$ monitor -c 5 org.apache.dubbo.demo.provider.DemoServiceImpl sayHello
Press Ctrl+C to abort.
Affect(class-cnt:1 , method-cnt:1) cost in 109 ms.
 timestamp            class                                           method    total  success  fail  avg-rt(ms)  fail-rate
----------------------------------------------------------------------------------------------------------------------------
 2018-09-20 09:45:32  org.apache.dubbo.demo.provider.DemoServiceImpl  sayHello  5      5        0     0.67        0.00%

 timestamp            class                                           method    total  success  fail  avg-rt(ms)  fail-rate
----------------------------------------------------------------------------------------------------------------------------
 2018-09-20 09:45:37  org.apache.dubbo.demo.provider.DemoServiceImpl  sayHello  5      5        0     1.00        0.00%

 timestamp            class                                           method    total  success  fail  avg-rt(ms)  fail-rate
----------------------------------------------------------------------------------------------------------------------------
 2018-09-20 09:45:42  org.apache.dubbo.demo.provider.DemoServiceImpl  sayHello  5      5        0     0.43        0.00%
```

#### Time Tunnel(tt)

* https://arthas.aliyun.com/doc/en/tt

记录方法调用数据，以便稍后检查方法调用的参数、返回值和抛出的异常。它就像让你能够通过“时间隧道”回溯并重放过去的方法调用一样。

```bash
$ tt -t org.apache.dubbo.demo.provider.DemoServiceImpl sayHello
Press Ctrl+C to abort.
Affect(class-cnt:1 , method-cnt:1) cost in 75 ms.
 INDEX   TIMESTAMP            COST(ms)  IS-RET  IS-EXP   OBJECT         CLASS                          METHOD
-------------------------------------------------------------------------------------------------------------------------------------
 1000    2018-09-20 09:54:10  1.971195  true    false    0x55965cca     DemoServiceImpl                sayHello
 1001    2018-09-20 09:54:11  0.215685  true    false    0x55965cca     DemoServiceImpl                sayHello
 1002    2018-09-20 09:54:12  0.236303  true    false    0x55965cca     DemoServiceImpl                sayHello
 1003    2018-09-20 09:54:13  0.159598  true    false    0x55965cca     DemoServiceImpl                sayHello
 1004    2018-09-20 09:54:14  0.201982  true    false    0x55965cca     DemoServiceImpl                sayHello
 1005    2018-09-20 09:54:15  0.214205  true    false    0x55965cca     DemoServiceImpl                sayHello
 1006    2018-09-20 09:54:16  0.241863  true    false    0x55965cca     DemoServiceImpl                sayHello
 1007    2018-09-20 09:54:17  0.305747  true    false    0x55965cca     DemoServiceImpl                sayHello
 1008    2018-09-20 09:54:18  0.18468   true    false    0x55965cca     DemoServiceImpl                sayHello
```

#### Classloader

* https://arthas.aliyun.com/doc/en/classloader

```bash
$ classloader
 name                                                  numberOfInstances  loadedCountTotal
 BootstrapClassLoader                                  1                  3346
 com.taobao.arthas.agent.ArthasClassloader             1                  1262
 java.net.URLClassLoader                               2                  1033
 org.apache.catalina.loader.ParallelWebappClassLoader  1                  628
 sun.reflect.DelegatingClassLoader                     166                166
 sun.misc.Launcher$AppClassLoader                      1                  31
 com.alibaba.fastjson.util.ASMClassLoader              6                  15
 sun.misc.Launcher$ExtClassLoader                      1                  7
 org.jvnet.hk2.internal.DelegatingClassLoader          2                  2
 sun.reflect.misc.MethodUtil                           1                  1
```


#### Web Console

* https://arthas.aliyun.com/doc/en/web-console

![web console](site/docs/.vuepress/public/images/web-console-local.png)


#### Profiler/FlameGraph

* https://arthas.aliyun.com/doc/en/profiler

```bash
$ profiler start
Started [cpu] profiling
```

```
$ profiler stop
profiler output file: /tmp/demo/arthas-output/20211207-111550.html
OK
```

通过浏览器查看 arthas-output 目录下的 Profiler 结果：

![](site/docs/.vuepress/public/images/arthas-output-svg.jpg)

#### Arthas Spring Boot Starter

* [Arthas Spring Boot Starter](https://arthas.aliyun.com/doc/spring-boot-starter.html)

### Known Users

Arthas 已有超过 120 家注册用户，[查看全部](USERS.md)。

欢迎在此 Issue 中登记公司名称（按登记顺序排列）：https://github.com/alibaba/arthas/issues/111 

![Alibaba](static/alibaba.png)
![Alipay](static/alipay.png)
![Aliyun](static/aliyun.png)
![Taobao](static/taobao.png)
![ICBC](static/icbc.png)
![雪球财经](static/xueqiu.png)
![顺丰科技](static/sf.png)
![贝壳找房](static/ke.png)
![vipkid](static/vipkid.png)
![百度凤巢](static/baidufengchao.png)
![有赞](static/youzan.png)
![科大讯飞](static/iflytek.png)
![智联招聘](static/zhaopin.png)
![达美盛](static/dms.png)


### Derivative Projects

* [Bistoury: A project that integrates Arthas](https://github.com/qunarcorp/bistoury)
* [A fork of arthas using MVEL](https://github.com/XhinLiang/arthas)

### Credits

#### Contributors

本项目的存在离不开所有贡献者的付出。

<a href="https://github.com/alibaba/arthas/graphs/contributors"><img src="https://opencollective.com/arthas/contributors.svg?width=890&button=false" /></a>

#### Projects

* [bytekit](https://github.com/alibaba/bytekit) Java 字节码工具包。
* [greys-anatomy](https://github.com/oldmanpushcart/greys-anatomy): Arthas 的代码库源自 Greys，在此感谢 Greys 所做的出色工作。
* [termd](https://github.com/alibaba/termd): Arthas 的终端实现基于 termd（一个用于在 Java 中编写终端应用的开源库）。
* [crash](https://github.com/crashub/crash): Arthas 的文本用户界面渲染基于从[此处](https://github.com/crashub/crash/tree/1.3.2/shell)提取的代码。
* [cli](https://github.com/alibaba/cli): Arthas 的命令行接口实现基于 vert.x 开源的 cli 库。
* [compiler](https://github.com/skalogs/SkaETL/tree/master/compiler)：Arthas 的内存编译器。
* [Apache Commons Net](https://commons.apache.org/proper/commons-net/)：Arthas 使用的 Telnet 客户端库。
* [async-profiler](https://github.com/jvm-profiling-tools/async-profiler)：Arthas 的 Profiler 命令底层依赖。