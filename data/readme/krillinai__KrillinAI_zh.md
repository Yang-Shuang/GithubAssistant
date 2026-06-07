<div align="center">
  <img src="/docs/images/logo.jpg" alt="KrillinAI" height="90">

# 面向人类与 Agent 的视频翻译与配音工具（内置 Skills）

<a href="https://trendshift.io/repositories/13360" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13360" alt="KrillinAI%2FKrillinAI | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

**[English](/README.md)｜[简体中文](/docs/zh/README.md)｜[日本語](/docs/jp/README.md)｜[한국어](/docs/kr/README.md)｜[Tiếng Việt](/docs/vi/README.md)｜[Français](/docs/fr/README.md)｜[Deutsch](/docs/de/README.md)｜[Español](/docs/es/README.md)｜[Português](/docs/pt/README.md)｜[Русский](/docs/rus/README.md)｜[اللغة العربية](/docs/ar/README.md)**

[![Twitter](https://img.shields.io/badge/Twitter-KrillinAI-orange?logo=twitter)](https://x.com/KrillinAI)
[![QQ 群](https://img.shields.io/badge/QQ%20群-754069680-green?logo=tencent-qq)](https://jq.qq.com/?_wv=1027&k=754069680)
[![Bilibili](https://img.shields.io/badge/dynamic/json?label=Bilibili&query=%24.data.follower&suffix=粉丝&url=https%3A%2F%2Fapi.bilibili.com%2Fx%2Frelation%2Fstat%3Fvmid%3D242124650&logo=bilibili&color=00A1D6&labelColor=FE7398&logoColor=FFFFFF)](https://space.bilibili.com/242124650)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/krillinai/KrillinAI)

</div>

## 项目简介（v2.0 已支持 Agent，现已发布）
[**快速开始**](#-快速-start)

KrillinAI 是由 Krillin AI 团队开发的一款多功能音视频本地化与增强方案，专为人类用户和 AI Agent（智能体）设计。该工具覆盖视频下载、语音识别、字幕翻译、TTS（文本转语音）配音、人像转换及封面生成等完整流程，支持横屏与竖屏格式，确保在各大主流平台（B站、小红书、抖音、微信视频号、快手、YouTube、TikTok 等）完美呈现。人类用户可通过客户端一键完成端到端的内容本地化；各模块也可通过 CLI 独立调用，AI Agent 则可按需编排单个或多个阶段，灵活组合自动化工作流。

## 新增功能

🤖 **支持 CLI**：提供分阶段的命令行接口，各阶段独立执行并输出结构化结果，支持跨阶段产物复用。

🧩 **Skills（技能）集合**：`skills/` 目录提供了面向 AI Agent 的各阶段 Skills，在稳定契约下直接调用，无需解析 CLI 文档。

🔗 **流水线编排**：一条命令串联多个阶段，实现从下载到渲染的全自动化。

🖼️ **封面生成**：根据原视频缩略图与提示词模板自动生成平台封面图片。

## 核心功能特性：

📥 **视频获取**：支持 yt-dlp 下载或本地文件上传

📜 **精准识别**：基于 Whisper 的高精度语音识别

🧠 **智能切分**：利用 LLM（大语言模型）进行字幕切分与对齐

🔄 **术语替换**：一键替换专业词汇

🌍 **专业翻译**：结合上下文的 LLM 翻译，保持语义自然流畅

🎙️ **声音克隆**：提供 CosyVoice 精选音色或自定义声音克隆

🎬 **视频合成**：自动处理横屏/竖屏视频与字幕排版

💻 **跨平台支持**：兼容 Windows、Linux、macOS，提供桌面端、服务端及 CLI 模式

## 效果演示

下图展示了导入一段 46 分钟本地视频并一键执行后生成的字幕文件效果。全程无需人工干预，无遗漏或重叠，切分自然，翻译质量极高。
![Alignment Effect](/docs/images/alignment.png)

<table>
<tr>
<td width="33%">

### 字幕翻译

---

https://github.com/user-attachments/assets/bba1ac0a-fe6b-4947-b58d-ba99306d0339

</td>
<td width="33%">

### 配音

---

https://github.com/user-attachments/assets/0b32fad3-c3ad-4b6a-abf0-0865f0dd2385

</td>

<td width="33%">

### 竖屏模式

---

https://github.com/user-attachments/assets/c2c7b528-0ef8-4ba9-b8ac-f9f92f6d4e71

</td>

</tr>
</table>

## 🔍 支持的语音识别服务

_**下表中的所有本地模型均支持可执行文件与模型文件的自动安装；你只需选择，KrillinAI 都会为你准备好一切。**_

| Service Source          | Supported Platforms | Model Options                             | Local/Cloud | Remarks                     |
|------------------------|---------------------|------------------------------------------|-------------|-----------------------------|
| **OpenAI Whisper**     | All Platforms        | -                                        | Cloud       | Fast speed and good effect  |
| **FasterWhisper**      | Windows/Linux       | `tiny`/`medium`/`large-v2` (recommended medium+) | Local       | Faster speed, no cloud service cost |
| **WhisperKit**         | macOS (M-series only) | `large-v2`                              | Local       | Native optimization for Apple chips |
| **WhisperCpp**         | All Platforms        | `large-v2`                              | Local       | Supports all platforms       |
| **Alibaba Cloud ASR**  | All Platforms        | -                                        | Cloud       | Avoids network issues in mainland China |

## 🚀 大语言模型支持

✅ 兼容所有符合 **OpenAI API 规范**的云端/本地大语言模型服务，包括但不限于：

- OpenAI
- Gemini
- DeepSeek
- Tongyi Qianwen（通义千问）
- Locally deployed open-source models（本地部署开源模型）
- Other API services compatible with OpenAI format（兼容 OpenAI 格式的 API 服务）

## 🎤 TTS（文本转语音）支持

- Alibaba Cloud Voice Service（阿里云语音服务）
- OpenAI TTS

## 语言支持

输入语言支持：中文、英文、日文、德文、土耳其语、韩文、俄文、马来语（持续增加中）

翻译输出语言支持：英文、中文、俄文、西班牙文、法文及 101 种其他语言

## 界面预览

![Interface Preview](/docs/images/ui_desktop_light.png)
![Interface Preview](/docs/images/ui_desktop_dark.png)

## 🚀 快速开始

你可以在 [KrillinAI DeepWiki](https://deepwiki.com/krillinai/KrillinAI) 上提问。它已索引仓库文件，助你快速找到答案。

### 基础步骤

首先，从 [Release](https://github.com/KrillinAI/KrillinAI/releases) 下载匹配你设备系统的可执行文件，然后根据下方教程选择桌面版或非桌面版。将软件解压到一个空文件夹中运行，因为运行时会自动生成一些目录，放在空文件夹中便于管理。

【如果是桌面版（即 release 文件名中包含 "desktop"），请看这里】
_桌面版为新发布版本，旨在解决新用户难以正确编辑配置文件的痛点，目前仍有部分 Bug 正在持续修复更新中。_

1. 双击文件即可开始使用（桌面版同样需要在软件内部进行配置）

【如果是非桌面版（即 release 文件名中不包含 "desktop"），请看这里】
_非桌面版为初始版本，配置相对复杂但功能稳定，适合服务端部署，因为它以 Web 形式提供 UI。_

1. 在文件夹内创建一个 `config` 文件夹，然后在 `config` 文件夹中创建 `config.toml` 文件。将源码 `config` 目录下的 `config-example.toml` 内容复制到 `config.toml` 中，并根据注释填写你的配置信息。
2. 双击或终端执行可执行文件以启动服务
3. 打开浏览器并访问 `http://127.0.0.1:8888` 开始使用（将 8888 替换为你在配置文件中指定的端口号）

### 致 macOS 用户

【如果是桌面版，即 release 文件名包含 "desktop"，请看这里】
由于签名限制，桌面版目前无法直接双击运行或通过 dmg 安装；你需要手动信任该应用。操作方法如下：

1. 打开终端并进入可执行文件所在目录（假设文件名为 `KrillinAI_1.0.0_desktop_macOS_arm64`）
2. 依次执行以下命令：

```
sudo xattr -cr ./KrillinAI_1.0.0_desktop_macOS_arm64
sudo chmod +x ./KrillinAI_1.0.0_desktop_macOS_arm64
./KrillinAI_1.0.0_desktop_macOS_arm64
```

【如果是非桌面版，即 release 文件名不包含 "desktop"，请看这里】
该软件未进行签名，因此在 macOS 上运行时，完成“基础步骤”中的文件配置后，仍需手动信任应用。操作方法如下：

1. 打开终端并进入可执行文件所在目录（假设文件名为 `KrillinAI_1.0.0_macOS_arm64`）
2. 依次执行以下命令：
   ```
   sudo xattr -rd com.apple.quarantine ./KrillinAI_1.0.0_macOS_arm64
    sudo chmod +x ./KrillinAI_1.0.0_macOS_arm64
    ./KrillinAI_1.0.0_macOS_arm64
   ```

   即可启动服务

### Docker 部署

本项目支持 Docker 部署；请参阅 [Docker 部署说明](./docker.md)

### CLI（命令行）使用

KrillinAI 提供分阶段的 CLI，适用于脚本编写、自动化流水线及 AI Agent 调用。CLI 默认同步执行，完成后向 stdout 输出单行 JSON，并将 `krillinai_manifest.json` 写入工作目录供后续阶段复用先前的产物。

从源码构建：

```bash
go build -o build/krillinai-cli ./cmd/cli
```

命令概览：

| Command | Purpose | Typical Outputs |
|---|---|---|
| `subtitle` | 根据 YouTube / Bilibili 链接或本地视频生成字幕；优先尝试平台自带字幕，失败则回退至 Whisper 识别 | `origin_language_srt.srt`, `target_language_srt.srt`, `bilingual_srt.srt`, `short_origin_mixed_srt.srt` |
| `tts` | 根据目标语言字幕生成配音 | `tts_final_audio.wav`, `video_with_tts.mp4` |
| `render-horizontal` | 输出横屏视频：原片+双语字幕，或配音版视频+目标语言字幕 | `horizontal_bilingual.mp4` |
| `render-vertical` | 输出竖屏视频：原片转竖屏+短字幕，或配音版视频+目标语言字幕 | `transferred_vertical_video.mp4`, `vertical_bilingual.mp4` |
| `pipeline` | 通过 `--outputs` 编排多个阶段 | 取决于所选阶段组合 |
| `cover` | 根据原封面与提示词模板生成封面图 | `generated_cover.png` |

典型工作流：

```bash
# 1. Generate subtitles: original, target, bilingual, and vertical short subtitles
./build/krillinai-cli subtitle "https://www.youtube.com/watch?v=dQw4w9WgXcQ" \
  --origin-lang en \
  --target-lang zh_cn \
  --workdir tasks/demo \
  --caption-source any

# 2. Generate dubbing from target-language subtitles
./build/krillinai-cli tts \
  --workdir tasks/demo \
  --input-srt tasks/demo/target_language_srt.srt \
  --line-mode target-only \
  --video tasks/demo/origin_video.mp4

# 3. Produce horizontal bilingual-subtitle video
./build/krillinai-cli render-horizontal \
  --workdir tasks/demo \
  --video tasks/demo/origin_video.mp4 \
  --subtitle tasks/demo/bilingual_srt.srt

# 4. Produce vertical short-subtitle video
./build/krillinai-cli render-vertical \
  --workdir tasks/demo \
  --video tasks/demo/origin_video.mp4 \
  --subtitle tasks/demo/short_origin_mixed_srt.srt \
  --major-title "今日话题" \
  --minor-title "AI Video"
```

Agent 集成规范：

- 解析 stdout 的最后一行 JSON 与 `krillinai_manifest.json` —— 请勿解析纯文本日志。
- `outputs` 字段记录了各阶段产物路径；后续命令只需传入 `--workdir` 即可复用清单文件。
- 支持 `--dry-run` 用于验证参数并生成清单，无需下载视频或调用外部 AI 服务。
- 错误处理依据 `error.kind`：`usage` → 修正参数，`retryable` → 重试，`dependency` → 安装 `ffmpeg` / `ffprobe` / `yt-dlp`。

完整参数参考请参阅 [CLI 能力汇总](./docs/zh/cli.md)。

### Agent Skills（技能）

仓库还内置了开箱即用的 Agent Skills（位于 `skills/`），供编程类 Agent 以稳定规范调用 CLI：

- [`krillinai-cli`](./skills/krillinai-cli/SKILL.md)：顶层路由 Skill，用于选择字幕、TTS、渲染、流水线或封面工作流。
- [`krillinai-subtitle`](./skills/krillinai-subtitle/SKILL.md)、[`krillinai-tts`](./skills/krillinai-tts/SKILL.md)、[`krillinai-render-horizontal`](./skills/krillinai-render-horizontal/SKILL.md) 与 [`krillinai-render-vertical`](./skills/krillinai-render-vertical/SKILL.md)：各阶段专属操作指南。
- [`krillinai-pipeline`](./skills/krillinai-pipeline/SKILL.md) 与 [`krillinai-cover`](./skills/krillinai-cover/SKILL.md)：流水线编排与封面生成的规划/预留指南，待执行路径完全打通后启用。
- [`cli-contract.md`](./skills/krillinai-cli/references/cli-contract.md)：共享的 JSON 结构、清单格式、outputs 字段及错误处理契约。

基于提供的配置文件，以下是为你更新的 README 中“配置帮助（必读）”章节的内容：

### 配置帮助（必读）

配置文件分为几个区块：`[app]`、`[server]`、`[llm]`、`[transcribe]` 与 `[tts]`。一个完整任务由语音识别（`transcribe`）+ 大模型翻译（`llm`）+ 可选配音服务（`tts`）组成。理解这一点将帮助你更好地掌握配置文件。

**最简单快捷的配置：**

**仅用于字幕翻译：**
   * 在 `[transcribe]` 区块中，将 `provider.name` 设置为 `openai`。
   * 随后你只需在 `[llm]` 块中填写 OpenAI API Key 即可开始进行字幕翻译。`app.proxy`、`model` 和 `openai.base_url` 可按需填写。

**兼顾成本、速度与质量（使用本地语音识别）：**

* 在 `[transcribe]` 区块中，将 `provider.name` 设置为 `fasterwhisper`。
* 设置 `transcribe.fasterwhisper.model` 为 `large-v2`。
* 在 `[llm]` 块中填写你的大语言模型配置。
* 所需的本地模型会自动下载并安装完毕。

**文本转语音（TTS）配置（可选）：**

* TTS 配置为可选项。
* 首先设置 `[tts]` 下的 `provider.name`（例如 `aliyun` 或 `openai`）。
* 然后填写所选服务商对应的配置区块。例如，若选择 `aliyun`，则必须填写 `[tts.aliyun]` 部分。
* 界面中的音色代码需根据所选服务商的文档进行选择。
* **注意：** 如果你计划使用声音克隆功能，必须将 TTS 提供商选为 `aliyun`。

**阿里云配置说明：**

* 关于获取阿里云服务所需的 `AccessKey`、`Bucket` 和 `AppKey` 的详细信息，请参阅 [阿里云配置说明](https://www.google.com/search?q=./aliyun.md)。其中重复出现的 AccessKey 等字段是为了保持清晰的配置结构而设计的。

**短字幕配置：**

* `short_subtitle_max_chars`: 英文短字幕每行最大字符数（默认值：20）
  - 专为竖屏/短视频设计
  - 中文文本保持完整，英文文本将按此长度进行拆分
  - 推荐取值范围：15-25

## 常见问题

请访问 [常见问题解答](./faq.md)

## 贡献指南

1. 请勿提交无用文件（如 `.vscode`、`.idea` 等）；请使用 `.gitignore` 将其过滤。
2. 请勿提交 `config.toml`；请提交 `config-example.toml`。

## 联系我们

1. 加入 QQ 群提问：754069680
2. 关注我们的社交媒体账号 [Bilibili](https://space.bilibili.com/242124650)，我们每天分享 AI 技术领域的优质内容。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=KrillinAI/KrillinAI&type=Date)](https://star-history.com/#KrillinAI/KrillinAI&Date)