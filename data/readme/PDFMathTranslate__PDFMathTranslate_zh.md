<div align="center">
	<a href="https://go.warp.dev/PDFMathTranslate" target="_blank">
		<sup>特别感谢：</sup>
		<br>
		<img alt="Warp sponsorship" width="400" src="https://github.com/warpdotdev/brand-assets/blob/main/Github/Sponsor/Warp-Github-LG-02.png">
		<br>
		<h>Warp，专为多 AI 代理编码打造</b>
		<br>
		<sup>支持 macOS、Linux 和 Windows</sup>
	</a>
</div>

<br>

<div align="center">

English | [简体中文](docs/README_zh-CN.md) | [繁體中文](docs/README_zh-TW.md) | [日本語](docs/README_ja-JP.md) | [한국어](docs/README_ko-KR.md)

<img src="./docs/images/banner.png" width="320px"  alt="PDFMathTranslate"/>

<h2 id="title">PDFMathTranslate</h2>

<p>
  <!-- PyPI -->
  <a href="https://pypi.org/project/pdf2zh/">
    <img src="https://img.shields.io/pypi/v/pdf2zh"></a>
  <a href="https://pepy.tech/projects/pdf2zh">
    <img src="https://static.pepy.tech/badge/pdf2zh"></a>
  <a href="https://hub.docker.com/r/byaidu/pdf2zh">
    <img src="https://img.shields.io/docker/pulls/byaidu/pdf2zh"></a>
  <a href="https://hellogithub.com/repository/8ec2cfd3ef744762bf531232fa32bc47" target="_blank"><img src="https://api.hellogithub.com/v1/widgets/recommend.svg?rid=8ec2cfd3ef744762bf531232fa32bc47&claim_uid=JQ0yfeBNjaTuqDU&theme=small" alt="Featured｜HelloGitHub" /></a>
  <a href="https://gitcode.com/Byaidu/PDFMathTranslate/overview">
    <img src="https://gitcode.com/Byaidu/PDFMathTranslate/star/badge.svg"></a>
  <a href="https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97-Online%20Demo-FF9E0D"></a>
  <a href="https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate">
    <img src="https://img.shields.io/badge/ModelScope-Demo-blue"></a>
  <a href="https://github.com/Byaidu/PDFMathTranslate/pulls">
    <img src="https://img.shields.io/badge/contributions-welcome-green"></a>
  <a href="https://t.me/+Z9_SgnxmsmA5NzBl">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white"></a>
  <!-- License -->
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Byaidu/PDFMathTranslate"></a>
</p>

<a href="https://trendshift.io/repositories/19816" target="_blank"><img src="https://trendshift.io/api/badge/repositories/19816" alt="PDFMathTranslate%2FPDFMathTranslate | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

<h2 id="updates">1. 它能做什么？</h2>

保留排版的科学 PDF 文档翻译工具。

- 📊 保留公式、图表、目录和注释。
- 🌐 支持[多种语言](#usage)，以及丰富的[翻译服务](#usage)。
- 🤖 提供[命令行工具](#usage)、[交互式图形界面（GUI）](#install)和[Docker](#install)部署方案

<div align="center">
<img src="./docs/images/preview.gif" width="80%"/>
</div>

<h2 id="updates">2. 最近更新</h2>

- [2026年3月23日] 实验性支持使用隔离环境的 v2.0 翻译内核（`--mode precise`）。（由 [@reycn](https://github.com/reycn) 贡献）
- [2026年3月22日] 新增对 MiniMax 的支持（PR by [@octo-patch](https://github.com/octo-patch)）
- [2026年3月22日] 修复与 OpenAI 相关的问题（PR by [@samqin123](https://github.com/samqin123)）
- [2026年3月22日] 修复 HTTP 相关问题（PR by [@soukouki](https://github.com/soukouki)）
- [2026年3月22日] 在 Mac 和 OONX 平台上加快模型加载速度，优化 GUI 启动、版本打印及持续集成流程。（由 [@reycn](https://github.com/reycn) 贡献）
- [2025年5月9日] pdf2zh 2.0 预览版 [#586](https://github.com/Byaidu/PDFMathTranslate/issues/586)：Windows ZIP 文件和 Docker 镜像现已可用。

  > [!NOTE]
  >
  > v2.0 版本已迁移至组织下的新仓库：[PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next)
  > 
  > v2.0 正式版已发布。

<h2 id="use-section">3. 使用指南 🌟</h2>
<h3 id="demo">3.1 在线服务 🌟</h3>

你可以通过以下演示体验我们的应用：

- [公共免费服务](https://pdf2zh.com/)，无需安装即可在线使用（推荐）。
- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) 提供免费使用额度；详情请参阅页面中的常见问题解答部分。（推荐）
- [HuggingFace 托管的演示](https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker)
- [ModelScope 托管的演示](https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate)，无需安装。

⚠️ 请注意，演示环境的计算资源有限，请避免滥用。

<h3 id="install">3.2 本地安装</h3>

针对不同使用场景，我们提供了多种运行方式：

<details open>
  <summary>3.2.1 Python：通过 uv 安装</summary>

1. 已安装 Python（版本要求 3.11 <= version <= 3.12）

2. 安装我们的包：

   ```bash
   pip install uv
   uv tool install --python 3.12 pdf2zh
   ```

3. 执行翻译，文件将生成在[当前工作目录](https://chatgpt.com/share/6745ed36-9acc-800e-8a90-59204bd13444)中：

   ```bash
   pdf2zh document.pdf
   ```

</details>
<details>
  <summary>3.2.2 Python：通过 pip 安装</summary>

1. 已安装 Python（版本要求 3.11 <= version <= 3.12）
2. 安装我们的包：

   ```bash
   pip install pdf2zh
   ```

3. 执行翻译，文件将生成在[当前工作目录](https://chatgpt.com/share/6745ed36-9acc-800e-8a90-59204bd13444)中：

   ```bash
   pdf2zh document.pdf
   ```

</details>
<details>
  <summary>3.3.3 Python：图形用户界面（GUI）</summary>

1. 已安装 Python（版本要求 3.11 <= version <= 3.12）

2. 安装我们的包：

  ```bash
  pip install pdf2zh
  ```

3. 在浏览器中启动使用：

   ```bash
   pdf2zh -i
   ```

4. 如果浏览器未自动打开，请手动访问

   ```bash
   http://localhost:7860/
   ```

   <img src="./docs/images/gui.gif" width="500"/>

更多详情请参阅 [GUI 文档](./docs/README_GUI.md)。

</details>

<details>
  <summary>3.2.4 应用程序：Windows 版</summary>

1. 从[发布页面](https://github.com/Byaidu/PDFMathTranslate/releases)下载 pdf2zh-version-win64.zip

2. 解压后双击 `pdf2zh.exe` 运行。


  > [!TIP]
  >
  > - 如果你使用的是 Windows 系统且下载后无法打开文件，请安装 [vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe) 并重试。
  > 
</details>


<details>

<summary>3.2.5 文献管理：Zotero 插件</summary>


更多详情请参阅 [Zotero PDF2zh](https://github.com/guaguastandup/zotero-pdf2zh)。

</details>


<details>
  <summary>3.2.6 Docker：容器化部署</summary>

1. 拉取并运行：

   ```bash
   docker pull byaidu/pdf2zh
   docker run -d -p 7860:7860 byaidu/pdf2zh
   ```

2. 在浏览器中打开：

   ```
   http://localhost:7860/
   ```

如需在云服务上进行 Docker 部署：

<div>
<a href="https://www.heroku.com/deploy?template=https://github.com/Byaidu/PDFMathTranslate">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" height="26"></a>
<a href="https://render.com/deploy">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Koyeb" height="26"></a>
<a href="https://zeabur.com/templates/5FQIGX?referralCode=reycn">
  <img src="https://zeabur.com/button.svg" alt="Deploy on Zeabur" height="26"></a>
<a href="https://template.sealos.io/deploy?templateName=pdf2zh">
  <img src="https://sealos.io/Deploy-on-Sealos.svg" alt="Deploy on Sealos" height="26"></a>
<a href="https://app.koyeb.com/deploy?type=git&builder=buildpack&repository=github.com/Byaidu/PDFMathTranslate&branch=main&name=pdf-math-translate">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb" height="26"></a>
</div>

> [!TIP]
>
> - 如果你无法访问 Docker Hub，请尝试使用 [GitHub Container Registry](https://github.com/Byaidu/PDFMathTranslate/pkgs/container/pdfmathtranslate) 上的镜像。
> ```bash
> docker pull ghcr.io/byaidu/pdfmathtranslate
> docker run -d -p 7860:7860 ghcr.io/byaidu/pdfmathtranslate
> ```
</details>

<details>
  <summary>3.2.* 安装过程中的网络问题解决方案</summary>

特定地区的用户在加载 AI 模型时可能会遇到网络困难。当前程序依赖 AI 模型（`wybxc/DocLayout-YOLO-DocStructBench-onnx`），部分用户因网络原因无法下载该模型。

为解决此模型的下载问题，可使用以下环境变量作为替代方案：

  ```shell
  set HF_ENDPOINT=https://hf-mirror.com
  ```

  PowerShell 用户使用：

  ```shell
  $env:HF_ENDPOINT = https://hf-mirror.com
  ```

  如果该解决方案对你无效或遇到其他问题，请参阅[常见问题解答](https://github.com/Byaidu/PDFMathTranslate/wiki#-faq--%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)。
</details>


<h2 id="usage">4. 技术细节</h2>

### 4.1 高级选项

在命令行中执行翻译命令，将在当前工作目录生成翻译后的文档 `example-mono.pdf` 和双语对照文档 `example-dual.pdf`。默认使用 Google 作为翻译服务。更多支持的翻译服务请查看[此处](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#services)。

<img src="./docs/images/cmd.explained.png" width="580px"  alt="cmd"/>

在下表中，我们列出了所有高级选项供参考：

| Option                | Function                                                                                                      | Example                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| files                 | 本地文件路径                                                                                                   | `pdf2zh ~/local.pdf`                           |
| links                 | 在线文件链接                                                                                                  | `pdf2zh http://arxiv.org/paper.pdf`            |
| `-i`                  | [进入图形界面（GUI）](#gui)                                                                                             | `pdf2zh -i`                                    |
| `-p`                  | [部分文档翻译](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#partial) | `pdf2zh example.pdf -p 1`                      |
| `-li`                 | [源语言](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#languages)            | `pdf2zh example.pdf -li en`                    |
| `-lo`                 | [目标语言](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#languages)            | `pdf2zh example.pdf -lo zh`                    |
| `-s`                  | [翻译服务](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#services)         | `pdf2zh example.pdf -s deepl`                  |
| `-t`                  | [多线程处理](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#threads)                | `pdf2zh example.pdf -t 1`                      |
| `-o`                  | 输出目录                                                                                                    | `pdf2zh example.pdf -o output`                 |
| `-f`, `-c`            | [异常处理](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#exceptions)                | `pdf2zh example.pdf -f "(MS.*)"`               |
| `-cp`                 | 兼容模式                                                                                                    | `pdf2zh example.pdf --compatible`              |
| `--skip-subset-fonts` | [跳过字体子集](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#font-subset)         | `pdf2zh example.pdf --skip-subset-fonts`       |
| `--ignore-cache`      | [忽略翻译缓存](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#cache)         | `pdf2zh example.pdf --ignore-cache`            |
| `--share`             | 生成公开链接                                                                                                   | `pdf2zh -i --share`                            |
| `--authorized`        | [授权访问](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#auth)                   | `pdf2zh -i --authorized users.txt [auth.html]` |
| `--prompt`            | [自定义提示词（Prompt）](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#prompt)                 | `pdf2zh --prompt [prompt.txt]`                 |
| `--onnx`              | [使用自定义 DocLayout-YOLO ONNX 模型]                                                                        | `pdf2zh --onnx [onnx/model/path]`              |
| `--serverport`        | [自定义 WebUI 端口]                                                                                       | `pdf2zh --serverport 7860`                     |
| `--dir`               | [批量翻译]                                                                                             | `pdf2zh --dir /path/to/translate/`             |
| `--config`            | [配置文件](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#cofig)             | `pdf2zh --config /path/to/config/config.json`  |
| `--serverport`        | [自定义 Gradio 服务器端口]                                                                                   | `pdf2zh --serverport 7860`                     |
| `--mode`              | 翻译模式：`fast`（默认，v1）或 `precise`（v2，实验性，需 pdf2zh_next 子模块）         | `pdf2zh --mode precise example.pdf`            |
| `--babeldoc`          | 使用实验性后端 [BabelDOC](https://funstory-ai.github.io/BabelDOC/) 进行翻译                     | `pdf2zh --babeldoc` -s openai example.pdf      |
| `--mcp`               | 启用 MCP STDIO 模式                                                                                         | `pdf2zh --mcp`                                 |
| `--sse`               | 启用 MCP SSE 模式                                                                                           | `pdf2zh --mcp --sse`                           |

有关详细解释及所有选项的完整列表，请参阅我们的[高级用法文档](./docs/ADVANCED.md)。

<h3 id="downstream">4.2 下游开发</h3>
对于下游应用开发者，请参阅我们的 [API 详情文档](./docs/APIS.md)，了解以下信息：

- **[Python API](./docs/APIS.md#api-python)**：如何在其他 Python 程序中调用本工具
- **[HTTP API](./docs/APIS.md#api-http)**：如何与已安装该程序的服务器进行通信

<h3 id="downstream">4.3 两大分支的区别</h3>

- [Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)：当前主仓库，专注于稳定版发布。

- [PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next)：包含 Web UI 及附加功能的分支。该分支处理了大量边缘情况，提升了 PDF 兼容性，并优化了跨列/跨页语义一致性、动态缩放及缩放一致性等多项翻译质量指标。请注意，此分支仅用于开发测试，未解决兼容性问题，且不面向社区贡献开放。

<h2 id="information">5. 项目信息</h2>
<h3 id="citation">5.1 引用文献</h3>

本工作已被 [*Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*](https://aclanthology.org/2025.emnlp-demos.71/) (EMNLP 2025) 接收。 

引用格式：

```
@inproceedings{ouyang-etal-2025-pdfmathtranslate,
	    title = "{PDFM}ath{T}ranslate: Scientific Document Translation Preserving Layouts",
	    author = "Ouyang, Rongxin  and
	      Chu, Chang  and
	      Xin, Zhikuang  and
	      Ma, Xiangyao",
	    editor = {Habernal, Ivan  and
	      Schulam, Peter  and
	      Tiedemann, J{\"o}rg},
	    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
	    month = nov,
	    year = "2025",
	    address = "Suzhou, China",
	    publisher = "Association for Computational Linguistics",
	    url = "https://aclanthology.org/2025.emnlp-demos.71/",
	    pages = "918--924",
	    ISBN = "979-8-89176-334-0",
	    abstract = "Language barriers in scientific documents hinder the diffusion and development of science and technologies. However, prior efforts in translating such documents largely overlooked the information in layouts. To bridge the gap, we introduce PDFMathTranslate, the world{'}s first open-source software for translating scientific documents while preserving layouts. Leveraging the most recent advances in large language models and precise layout detection, we contribute to the community with key improvements in precision, flexibility, and efficiency. The work is open-sourced at https://github.com/byaidu/pdfmathtranslate with more than 222k downloads."
	}
```
<h3 id="acknowledgement">5.2 鸣谢</h3>

- [Immersive Translation](https://immersivetranslate.com) 为活跃贡献者提供每月 Pro 会员兑换码，详情见：[CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- 新后端引擎：[BabelDOC](https://github.com/funstory-ai/BabelDOC)

- 文档合并：[PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- 文档解析：[Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- 文档提取：[MinerU](https://github.com/opendatalab/MinerU)

- 文档预览：[Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- 多线程翻译：[MathTranslate](https://github.com/SUSYUSTC/MathTranslate)

- 版面解析：[DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- 文档标准参考：[PDF Explained](https://zxyle.github.io/PDF-Explained/)，[PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- 多语言字体支持：[Go Noto Universal](https://github.com/satbyy/go-noto-universal)

<h3 id="contrib">5.3 贡献者</h3>

<a href="https://github.com/Byaidu/PDFMathTranslate/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a>

![Alt](https://repobeats.axiom.co/api/embed/dfa7583da5332a11468d686fbd29b92320a6a869.svg "Repobeats analytics image")

有关如何参与贡献的详细信息，请参阅[贡献指南](https://github.com/Byaidu/PDFMathTranslate/wiki/Contribution-Guide---%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97)。


<h3 id="star_hist">5.4 Star 历史</h3>

<a href="https://star-history.com/#Byaidu/PDFMathTranslate&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Byaidu/PDFMathTranslate&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Byaidu/PDFMathTranslate&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Byaidu/PDFMathTranslate&type=Date"/>
 </picture>
</a>