<div align="center">

<a href="https://trendshift.io/repositories/10489" target="_blank"><img src="https://trendshift.io/api/badge/repositories/10489" alt="2noise%2FChatTTS | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

# ChatTTS
A generative speech model for daily dialogue.

[![Licence](https://img.shields.io/github/license/2noise/ChatTTS?style=for-the-badge)](https://github.com/2noise/ChatTTS/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/ChatTTS.svg?style=for-the-badge&color=green)](https://pypi.org/project/ChatTTS)

[![Huggingface](https://img.shields.io/badge/🤗%20-Models-yellow.svg?style=for-the-badge)](https://huggingface.co/2Noise/ChatTTS)
[![Open In Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/github/2noise/ChatTTS/blob/main/examples/ipynb/colab.ipynb)
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/Ud5Jxgx5yD)

**English** | [**简体中文**](docs/cn/README.md) | [**日本語**](docs/jp/README.md) | [**Русский**](docs/ru/README.md) | [**Español**](docs/es/README.md) | [**Français**](docs/fr/README.md) | [**한국어**](docs/kr/README.md)

</div>

## 简介
> [!Note]
> 本仓库包含算法基础设施和一些简单的示例。

> [!Tip]
> 关于扩展的终端用户产品，请参阅社区维护的索引仓库 [Awesome-ChatTTS](https://github.com/libukai/Awesome-ChatTTS/tree/en)。  
> 你可以在[这里](https://github.com/CodeBoarding/GeneratedOnBoardings/blob/main/ChatTTS/on_boarding.md)找到代码库的可视化图表。

ChatTTS 是一款专为对话场景（如大语言模型助手）设计的文本转语音（Text-to-Speech, TTS）生成模型。

### 支持的语言
- [x] 英语
- [x] 中文
- [ ] 即将推出...

### 亮点
> 详细功能介绍可参考 **[B站视频](https://www.bilibili.com/video/BV1zn4y1o7iV)**。

1. **对话式语音合成**：ChatTTS 针对对话任务进行了优化，能够生成自然且富有表现力的语音。它支持多说话人，便于实现交互式对话。
2. **细粒度控制**：该模型能够预测并控制精细的韵律特征，包括笑声、停顿和语气词等。 
3. **更优的韵律**：在韵律表现上，ChatTTS 优于大多数开源 TTS 模型。我们提供了预训练模型以支持进一步的研究与开发。

### 数据集与模型
> [!Important]
> 发布的模型仅限学术用途。

- 主模型使用超过 10 万小时的中文和英文音频数据进行训练。
- **[HuggingFace](https://huggingface.co/2Noise/ChatTTS)** 上的开源版本是一个未经 SFT（监督微调）的 4 万小时预训练模型。

### 路线图
- [x] 开源 4 万小时基础模型及 `spk_stats` 文件。
- [x] 流式音频生成。
- [x] 开源 DVAE 编码器与零样本推理代码。
- [ ] 多情感控制。
- [ ] ChatTTS.cpp（欢迎在 `2noise` 组织下创建新仓库）

### 许可协议

#### 代码

代码采用 `AGPLv3+` 许可证发布。

#### 模型

模型采用 `CC BY-NC 4.0` 许可证发布。本模型仅供教育与研究使用，不得用于任何商业或非法目的。作者不对信息的准确性、完整性或可靠性作出任何保证。仓库中使用的信息与数据仅用于学术与研究目的。数据来源于公开渠道，作者不主张对数据拥有任何所有权或版权。

### 免责声明

ChatTTS 是一款强大的文本转语音系统。然而，负责任且合乎道德地使用这项技术至关重要。为限制 ChatTTS 的滥用风险，我们在训练 40,000 小时模型时加入了少量高频噪声，并尽可能使用 MP3 格式压缩了音频质量，以防止恶意行为者将其用于犯罪目的。同时，我们已内部训练了一个检测模型，并计划在未来开源它。

### 联系方式
> 欢迎随时提交 GitHub Issues 或 PR。

#### 正式咨询
关于模型与路线图的相关事宜，请通过邮箱 **open-source@2noise.com** 联系我们。

#### 在线交流
##### 1. QQ 群（国内社交软件）
- **群 1**：808364215
- **群 2**：230696694
- **群 3**：933639842
- **群 4**：608667975

##### 2. Discord 服务器
点击[此处](https://discord.gg/Ud5Jxgx5yD)加入。

## 快速开始
### 克隆仓库
```bash
git clone https://github.com/2noise/ChatTTS
cd ChatTTS
```

### 安装依赖
#### 1. 直接安装
```bash
pip install --upgrade -r requirements.txt
```

#### 2. 通过 Conda 安装
```bash
conda create -n chattts python=3.11
conda activate chattts
pip install -r requirements.txt
```

#### 可选：安装 vLLM（仅限 Linux）
```bash
pip install safetensors vllm==0.2.7 torchaudio
```

#### 不推荐选项：使用 NVIDIA GPU 时安装 TransformerEngine（仅限 Linux）
> [!Warning]
> **请勿安装！** 
> TransformerEngine 的适配目前仍在开发中，暂时无法正常运行。仅建议在开发目的下安装。更多详情请参见 #672 #676

> [!Note]
> 安装过程可能非常缓慢。

```bash
pip install git+https://github.com/NVIDIA/TransformerEngine.git@stable
```

#### 不推荐选项：安装 FlashAttention-2（主要针对 NVIDIA GPU）
> [!Warning]
> **请勿安装！** 
> 根据[该 Issue](https://github.com/huggingface/transformers/issues/26990) 的反馈，目前 FlashAttention-2 会降低生成速度。仅建议在开发目的下安装。

> [!Note]
> 支持的硬件设备列表请参阅 [Hugging Face 文档](https://huggingface.co/docs/transformers/perf_infer_gpu_one#flashattention-2)。


```bash
pip install flash-attn --no-build-isolation
```

### 快速开始示例
> **执行以下命令前，请确保你位于项目根目录下。**

#### 1. 启动 WebUI
```bash
python examples/web/webui.py
```

#### 2. 通过命令行推理
> 音频将保存至 `./output_audio_n.mp3`

```bash
python examples/cmd/run.py "Your text 1." "Your text 2."
```

## 安装方式

1. 从 PyPI 安装稳定版
```bash
pip install ChatTTS
```

2. 从 GitHub 安装最新版
```bash
pip install git+https://github.com/2noise/ChatTTS
```

3. 以开发模式从本地目录安装
```bash
pip install -e .
```

### 基础用法

```python
import ChatTTS
import torch
import torchaudio

chat = ChatTTS.Chat()
chat.load(compile=False) # Set to True for better performance

texts = ["PUT YOUR 1st TEXT HERE", "PUT YOUR 2nd TEXT HERE"]

wavs = chat.infer(texts)

for i in range(len(wavs)):
    """
    In some versions of torchaudio, the first line works but in other versions, so does the second line.
    """
    try:
        torchaudio.save(f"basic_output{i}.wav", torch.from_numpy(wavs[i]).unsqueeze(0), 24000)
    except:
        torchaudio.save(f"basic_output{i}.wav", torch.from_numpy(wavs[i]), 24000)
```

### 高级用法

```python
###################################
# Sample a speaker from Gaussian.

rand_spk = chat.sample_random_speaker()
print(rand_spk) # save it for later timbre recovery

params_infer_code = ChatTTS.Chat.InferCodeParams(
    spk_emb = rand_spk, # add sampled speaker 
    temperature = .3,   # using custom temperature
    top_P = 0.7,        # top P decode
    top_K = 20,         # top K decode
)

###################################
# For sentence level manual control.

# use oral_(0-9), laugh_(0-2), break_(0-7) 
# to generate special token in text to synthesize.
params_refine_text = ChatTTS.Chat.RefineTextParams(
    prompt='[oral_2][laugh_0][break_6]',
)

wavs = chat.infer(
    texts,
    params_refine_text=params_refine_text,
    params_infer_code=params_infer_code,
)

###################################
# For word level manual control.

text = 'What is [uv_break]your favorite english food?[laugh][lbreak]'
wavs = chat.infer(text, skip_refine_text=True, params_refine_text=params_refine_text,  params_infer_code=params_infer_code)
"""
In some versions of torchaudio, the first line works but in other versions, so does the second line.
"""
try:
    torchaudio.save("word_level_output.wav", torch.from_numpy(wavs[0]).unsqueeze(0), 24000)
except:
    torchaudio.save("word_level_output.wav", torch.from_numpy(wavs[0]), 24000)
```

<details open>
  <summary><h4>示例：自我介绍</h4></summary>

```python
inputs_en = """
chat T T S is a text to speech model designed for dialogue applications. 
[uv_break]it supports mixed language input [uv_break]and offers multi speaker 
capabilities with precise control over prosodic elements like 
[uv_break]laughter[uv_break][laugh], [uv_break]pauses, [uv_break]and intonation. 
[uv_break]it delivers natural and expressive speech,[uv_break]so please
[uv_break] use the project responsibly at your own risk.[uv_break]
""".replace('\n', '') # English is still experimental.

params_refine_text = ChatTTS.Chat.RefineTextParams(
    prompt='[oral_2][laugh_0][break_4]',
)

audio_array_en = chat.infer(inputs_en, params_refine_text=params_refine_text)
torchaudio.save("self_introduction_output.wav", torch.from_numpy(audio_array_en[0]), 24000)
```

<table>
<tr>
<td align="center">

**男声说话人**

</td>
<td align="center">

**女声说话人**

</td>
</tr>
<tr>
<td align="center">

[male speaker](https://github.com/2noise/ChatTTS/assets/130631963/e0f51251-db7f-4d39-a0e9-3e095bb65de1)

</td>
<td align="center">

[female speaker](https://github.com/2noise/ChatTTS/assets/130631963/f5dcdd01-1091-47c5-8241-c4f6aaaa8bbd)

</td>
</tr>
</table>


</details>

## 常见问题 (FAQ)

#### 1. 需要多少显存（VRAM）？推理速度如何？
对于一段 30 秒的音频，至少需要 4GB GPU 显存。在 RTX 4090 GPU 上，每秒可生成约 7 个语义 token 对应的音频。实时因子（Real-Time Factor, RTF）约为 0.3。

#### 2. 模型稳定性不足，存在多说话人或音质较差等问题。
这是自回归模型（如 bark 和 valle）常见的问题，通常难以完全避免。建议尝试多次采样以找到合适的结果。

#### 3. 除了笑声，还能控制其他内容吗？能控制其他情绪吗？
在当前发布的模型中，唯一的词元级（token-level）控制单元是 `[laugh]`、`[uv_break]` 和 `[lbreak]`。在后续版本中，我们可能会开源具备更多情绪控制能力的模型。

## 致谢
- [bark](https://github.com/suno-ai/bark)、[XTTSv2](https://github.com/coqui-ai/TTS) 和 [valle](https://arxiv.org/abs/2301.02111) 展示了自回归风格系统在 TTS 任务上的卓越效果。
- [fish-speech](https://github.com/fishaudio/fish-speech) 揭示了 GVQ 作为大语言模型（LLM）音频词元化器（tokenizer）的能力。
- [vocos](https://github.com/gemelo-ai/vocos)，本项目将其用作预训练声码器（vocoder）。

## 特别鸣谢
- [wlu-audio lab](https://audio.westlake.edu.cn/)，为本项目早期的算法实验提供了支持。

## 感谢所有贡献者的付出
[![contributors](https://contrib.rocks/image?repo=2noise/ChatTTS)](https://github.com/2noise/ChatTTS/graphs/contributors)

<div align="center">

  ![counter](https://counter.seku.su/cmoe?name=chattts&theme=mbs)

</div>