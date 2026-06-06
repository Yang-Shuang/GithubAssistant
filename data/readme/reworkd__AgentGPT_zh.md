<p align="center">
  <img src="https://raw.githubusercontent.com/reworkd/AgentGPT/main/next/public/banner.png" height="300" alt="AgentGPT Logo"/>
</p>
<p align="center">
  <em>🤖 在浏览器中组装、配置并部署自主 AI 代理。🤖   </em>
</p>
<p align="center">
    <img alt="Node version" src="https://img.shields.io/static/v1?label=node&message=%20%3E=18&logo=node.js&color=2334D058" />
      <a href="https://github.com/reworkd/AgentGPT/blob/master/README.md"><img src="https://img.shields.io/badge/lang-English-blue.svg" alt="English"></a>
  <a href="https://github.com/reworkd/AgentGPT/blob/master/docs/README.zh-HANS.md"><img src="https://img.shields.io/badge/lang-简体中文-red.svg" alt="简体中文"></a>
  <a href="https://github.com/reworkd/AgentGPT/blob/master/docs/README.hu-Cs4K1Sr4C.md"><img src="https://img.shields.io/badge/lang-Hungarian-red.svg" alt="Hungarian"></a>
</p>

<p align="center">
<a href="https://agentgpt.reworkd.ai">🔗 短链接</a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="https://reworkd.ai/docs">📚 文档</a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="https://twitter.com/reworkdai">🐦 Twitter</a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="https://discord.gg/gcmNyAAFfV">📢 Discord</a>
</p>

AgentGPT 允许你配置并部署自主 AI 代理。
为你的自定义 AI 命名，让它去实现任何你能想到的目标。
它将尝试通过构思任务、执行任务并从结果中学习来达成目标 🚀。

---

## ✨ Demo
为了获得最佳的演示体验，请直接访问[我们的网站](https://agentgpt.reworkd.ai) :)

[Demo Video](https://github.com/reworkd/AgentGPT/assets/50181239/5348e44a-29a5-4280-a06b-fe1429a8d99e)


## 👨‍🚀 快速开始

使用项目自带的自动安装 CLI 是上手 AgentGPT 最简单的方式。
该 CLI 将为 AgentGPT 配置以下内容：
- 🔐 [环境变量](https://github.com/reworkd/AgentGPT/blob/main/.env.example)（及 API 密钥）
- 🗂️ [数据库](https://github.com/reworkd/AgentGPT/tree/main/db)（MySQL）
- 🤖 [后端](https://github.com/reworkd/AgentGPT/tree/main/platform)（FastAPI）
- 🎨 [前端](https://github.com/reworkd/AgentGPT/tree/main/next)（Next.js）

## 前置条件 :point_up:

在开始之前，请确保已安装以下内容：

- 你喜欢的编辑器。例如，[Visual Studio Code (VS Code)](https://code.visualstudio.com/download)
- [Node.js](https://nodejs.org/en/download)
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop)。安装后，请创建账户、打开 Docker 应用程序并登录。
- 一个 [OpenAI API 密钥](https://platform.openai.com/signup)
- 一个 [Serper API Key]（可选）
- 一个 [Replicate API Token]（可选）

## 开始使用 :rocket:
1. **打开你的编辑器**

2. **打开终端** - 通常，你可以通过“终端”选项卡或使用快捷键（例如在 VS Code 中，Windows 为 `Ctrl + ~`，Mac 为 `Control + ~`）来打开。

3. **克隆仓库并进入目录** - 终端打开后，运行以下命令克隆仓库并切换至该目录。

   **Mac/Linux 用户** :apple: :penguin:
   ```bash
   git clone https://github.com/reworkd/AgentGPT.git
   cd AgentGPT
   ./setup.sh
   ```
   **Windows 用户** :windows:
   ```bash
   git clone https://github.com/reworkd/AgentGPT.git
   cd AgentGPT
   ./setup.bat
   ```
4. **按照脚本提示完成设置** - 添加相应的 API 密钥，待所有服务运行后，在浏览器中访问 [http://localhost:3000](http://localhost:3000)。

祝你玩得开心！:tada:


## 🚀 技术栈

- ✅ **项目初始化**：[create-t3-app](https://create.t3.gg) + [FastAPI-template](https://github.com/s3rius/FastAPI-template)。
- ✅ **框架**：[Next.js 13 + TypeScript](https://nextjs.org/) + [FastAPI](https://fastapi.tiangolo.com/)
- ✅ **认证**：[Next-Auth.js](https://next-auth.js.org)
- ✅ **ORM（对象关系映射）**：[Prisma](https://prisma.io) 与 [SQLModel](https://sqlmodel.tiangolo.com/)。
- ✅ **数据库**：[Planetscale](https://planetscale.com/)。
- ✅ **样式**：[TailwindCSS + HeadlessUI](https://tailwindcss.com)。
- ✅ **数据校验**：[Zod](https://github.com/colinhacks/zod) 与 [Pydantic](https://docs.pydantic.dev/)。
- ✅ **大模型工具链**：[LangChain](https://github.com/hwchase17/langchain)。


<h2 align="center">
💝 Our GitHub sponsors 💝
</h2>

<p align="center">
加入我们，共同助力开源项目 AgentGPT 的开发，该项目正在不断拓展 AI 代理的边界！你的赞助将帮助我们扩大资源、增强功能与特性，并持续迭代这一令人兴奋的项目！ 🚀
</p>

<p align="center">
<!-- sponsors --><a href="https://github.com/arthurbnhm"><img src="https://github.com/arthurbnhm.png" width="60px" alt="Arthur" /></a><a href="https://github.com/mrayonnaise"><img src="https://github.com/mrayonnaise.png" width="60px" alt="Matt Ray" /></a><a href="https://github.com/jd3655"><img src="https://github.com/jd3655.png" width="60px" alt="Vector Ventures" /></a><a href="https://github.com/durairajasivam"><img src="https://github.com/durairajasivam.png" width="60px" alt="" /></a><a href="https://github.com/floriank"><img src="https://github.com/floriank.png" width="60px" alt="Florian Kraft" /></a><a href="https://github.com/localecho"><img src="https://github.com/localecho.png" width="60px" alt="" /></a><a href="https://github.com/fireheat135"><img src="https://github.com/fireheat135.png" width="60px" alt="" /></a><a href="https://github.com/zoelidity"><img src="https://github.com/zoelidity.png" width="60px" alt="Zoe" /></a><a href="https://github.com/busseyl"><img src="https://github.com/busseyl.png" width="60px" alt="Lucas Bussey" /></a><a href="https://github.com/DuanChaori"><img src="https://github.com/DuanChaori.png" width="60px" alt="" /></a><a href="https://github.com/jukwaphil1"><img src="https://github.com/jukwaphil1.png" width="60px" alt="" /></a><a href="https://github.com/lisa-ee"><img src="https://github.com/lisa-ee.png" width="60px" alt="Lisa" /></a><a href="https://github.com/VulcanT"><img src="https://github.com/VulcanT.png" width="60px" alt="" /></a><a href="https://github.com/kman62"><img src="https://github.com/kman62.png" width="60px" alt="kmotte" /></a><a href="https://github.com/Haithamhaj"><img src="https://github.com/Haithamhaj.png" width="60px" alt="" /></a><a href="https://github.com/SwftCoins"><img src="https://github.com/SwftCoins.png" width="60px" alt="SWFT Blockchain" /></a><a href="https://github.com/ChevalierzA"><img src="https://github.com/ChevalierzA.png" width="60px" alt="" /></a><a href="https://github.com/research-developer"><img src="https://github.com/research-developer.png" width="60px" alt="" /></a><a href="https://github.com/Mitchell-Coder-New"><img src="https://github.com/Mitchell-Coder-New.png" width="60px" alt="" /></a><a href="https://github.com/Trecares"><img src="https://github.com/Trecares.png" width="60px" alt="" /></a><a href="https://github.com/nnkostov"><img src="https://github.com/nnkostov.png" width="60px" alt="Nikolay Kostov" /></a><a href="https://github.com/oryanmoshe"><img src="https://github.com/oryanmoshe.png" width="60px" alt="Oryan Moshe" /></a><a href="https://github.com/ClayNelson"><img src="https://github.com/ClayNelson.png" width="60px" alt="Clay Nelson" /></a><a href="https://github.com/0xmatchmaker"><img src="https://github.com/0xmatchmaker.png" width="60px" alt="0xmatchmaker" /></a><a href="https://github.com/carlosbartolomeu"><img src="https://github.com/carlosbartolomeu.png" width="60px" alt="" /></a><a href="https://github.com/Agronobeetles"><img src="https://github.com/Agronobeetles.png" width="60px" alt="" /></a><a href="https://github.com/CloudyGuyThompson"><img src="https://github.com/CloudyGuyThompson.png" width="60px" alt="Guy Thompson" /></a><a href="https://github.com/Jhonvolt17"><img src="https://github.com/Jhonvolt17.png" width="60px" alt="" /></a><a href="https://github.com/sirswali"><img src="https://github.com/sirswali.png" width="60px" alt="Vusi Dube" /></a><a href="https://github.com/Tweezamiza"><img src="https://github.com/Tweezamiza.png" width="60px" alt="" /></a><a href="https://github.com/DixonFyre"><img src="https://github.com/DixonFyre.png" width="60px" alt="" /></a><a href="https://github.com/jenius-eagle"><img src="https://github.com/jenius-eagle.png" width="60px" alt="" /></a><a href="https://github.com/CubanCongaMan"><img src="https://github.com/CubanCongaMan.png" width="60px" alt="Roberto Luis Sanchez, P.E., P.G.; D,GE; F.ASCE" /></a><a href="https://github.com/cskrobec"><img src="https://github.com/cskrobec.png" width="60px" alt="" /></a><a href="https://github.com/Jahmazon"><img src="https://github.com/Jahmazon.png" width="60px" alt="" /></a><a href="https://github.com/ISDAworld"><img src="https://github.com/ISDAworld.png" width="60px" alt="David Gammond" /></a><a href="https://github.com/lazzacapital"><img src="https://github.com/lazzacapital.png" width="60px" alt="Lazza Capital" /></a><a href="https://github.com/OptionalJoystick"><img src="https://github.com/OptionalJoystick.png" width="60px" alt="" /></a><a href="https://github.com/rodolfoguzzi"><img src="https://github.com/rodolfoguzzi.png" width="60px" alt="" /></a><a href="https://github.com/bluecat2210"><img src="https://github.com/bluecat2210.png" width="60px" alt="" /></a><a href="https://github.com/dactylogram9"><img src="https://github.com/dactylogram9.png" width="60px" alt="" /></a><a href="https://github.com/RUFreeJAC63"><img src="https://github.com/RUFreeJAC63.png" width="60px" alt="" /></a><a href="https://github.com/cecilmiles"><img src="https://github.com/cecilmiles.png" width="60px" alt="" /></a><a href="https://github.com/Djarielm007"><img src="https://github.com/Djarielm007.png" width="60px" alt="" /></a><a href="https://github.com/mikenj07"><img src="https://github.com/mikenj07.png" width="60px" alt="" /></a><a href="https://github.com/SvetaMolusk"><img src="https://github.com/SvetaMolusk.png" width="60px" alt="" /></a><a href="https://github.com/wuminkung"><img src="https://github.com/wuminkung.png" width="60px" alt="" /></a><a href="https://github.com/zhoumo1221"><img src="https://github.com/zhoumo1221.png" width="60px" alt="" /></a><a href="https://github.com/Stefan6666XXX"><img src="https://github.com/Stefan6666XXX.png" width="60px" alt="Stephane DeGuire" /></a><a href="https://github.com/lyska"><img src="https://github.com/lyska.png" width="60px" alt="Lyska" /></a><a href="https://github.com/KurganKolde"><img src="https://github.com/KurganKolde.png" width="60px" alt="" /></a><a href="https://github.com/sclappccsu"><img src="https://github.com/sclappccsu.png" width="60px" alt="Sharon Clapp at CCSU" /></a><a href="https://github.com/Rooba-Finance"><img src="https://github.com/Rooba-Finance.png" width="60px" alt="Rooba.Finance" /></a><a href="https://github.com/ferienhausmiete"><img src="https://github.com/ferienhausmiete.png" width="60px" alt="" /></a><a href="https://github.com/benjaminbales"><img src="https://github.com/benjaminbales.png" width="60px" alt="Benjamin Bales" /></a><a href="https://github.com/pimentel233"><img src="https://github.com/pimentel233.png" width="60px" alt="" /></a><a href="https://github.com/PinkyWobbles"><img src="https://github.com/PinkyWobbles.png" width="60px" alt="" /></a><a href="https://github.com/jconroy11"><img src="https://github.com/jconroy11.png" width="60px" alt="" /></a><a href="https://github.com/DavidJamesRotenberg"><img src="https://github.com/DavidJamesRotenberg.png" width="60px" alt="" /></a><a href="https://github.com/antecochat"><img src="https://github.com/antecochat.png" width="60px" alt="" /></a><a href="https://github.com/RealBonOfaSitch"><img src="https://github.com/RealBonOfaSitch.png" width="60px" alt="" /></a><!-- sponsors -->
</p>

<h2 align="center">
💪 Contributors 💝
</h2>

<p align="center">
我们的贡献者让这个项目成为可能。感谢大家！🙏
</p>

<a href="https://github.com/reworkd/agentgpt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=reworkd/agentgpt" />
</a>

<div align="center">
<sub>Made with <a href="https://contrib.rocks">contrib.rocks</a>.</sub>
</div>