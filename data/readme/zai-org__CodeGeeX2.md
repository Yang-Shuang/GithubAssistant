![](resources/codegeex_logo.png)

<p align="center">
    🏠 <a href="https://codegeex.cn" target="_blank">主页</a>｜🛠 插件 <a href="https://marketplace.visualstudio.com/items?itemName=aminer.codegeex" target="_blank">VS Code</a>, <a href="https://plugins.jetbrains.com/plugin/20587-codegeex" target="_blank">Jetbrains</a>｜🤗 <a href="https://huggingface.co/THUDM/codegeex2-6b" target="_blank">模型下载</a>｜📄 <a href="https://arxiv.org/abs/2303.17568" target="_blank">论文</a>｜👋 加入<a href="resources/wechat.md"target="_blank">微信开发者交流群</a>
</p>

Read this in [English](README_EN.md)<br>
[日本語](README_JA.md)で読む<br>
Lire en [Français](README_FR.md)

⭐️ 最新一代 [CodeGeeX4](https://github.com/THUDM/CodeGeeX4) 模型已经正式开源。
The newest [CodeGeeX4](https://github.com/THUDM/CodeGeeX4) has been released.

# CodeGeeX2: 更强大的多语言代码生成模型

CodeGeeX2 是多语言代码生成模型 [CodeGeeX](https://github.com/THUDM/CodeGeeX) ([KDD’23](https://arxiv.org/abs/2303.17568)) 的第二代模型。不同于一代 CodeGeeX（完全在国产华为昇腾芯片平台训练） ，CodeGeeX2 是基于 [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B) 架构加入代码预训练实现，得益于 ChatGLM2 的更优性能，CodeGeeX2 在多项指标上取得性能提升（+107% > CodeGeeX；仅60亿参数即超过150亿参数的 StarCoder-15B 近10%），更多特性包括：

* **更强大的代码能力**：基于 ChatGLM2-6B 基座语言模型，CodeGeeX2-6B 进一步经过了 600B 代码数据预训练，相比一代模型，在代码能力上全面提升，[HumanEval-X](https://huggingface.co/datasets/THUDM/humaneval-x) 评测集的六种编程语言均大幅提升 (Python +57%, C++ +71%, Java +54%, JavaScript +83%, Go +56%, Rust +321\%)，在Python上达到 35.9\% 的 Pass@1 一次通过率，超越规模更大的 StarCoder-15B。
* **更优秀的模型特性**：继承 ChatGLM2-6B 模型特性，CodeGeeX2-6B 更好支持中英文输入，支持最大 8192 序列长度，推理速度较一代 CodeGeeX-13B 大幅提升，量化后仅需6GB显存即可运行，支持轻量级本地化部署。
* **更全面的AI编程助手**：CodeGeeX插件（[VS Code](https://marketplace.visualstudio.com/items?itemName=aminer.codegeex), [Jetbrains](https://plugins.jetbrains.com/plugin/20587-codegeex)）后端升级，支持超过100种编程语言，新增上下文补全、跨文件补全等实用功能。结合 Ask CodeGeeX 交互式AI编程助手，支持中英文对话解决各种编程问题，包括且不限于代码解释、代码翻译、代码纠错、文档生成等，帮助程序员更高效开发。
* **更开放的协议**：CodeGeeX2-6B 权重对学术研究完全开放，填写[登记表](https://open.bigmodel.cn/mla/form?mcode=CodeGeeX2-6B)申请商业使用。

## 使用教程

* [快速开始](#快速开始)
* [推理教程（多卡推理，加速推理，多平台推理等）](docs/zh/inference_zh.md)

## AI编程助手

![](resources/codegeex_demo.png)

我们开发了支持 VS Code、 IntelliJ IDEA、PyCharm、GoLand、WebStorm、Android Studio 等IDE的 CodeGeeX 插件。在插件中，可以更直接地体验到 CodeGeeX2 模型在代码生成与补全、添加注释、代码翻译及技术问答方面的能力为开发效率带来的提升。欢迎在IDE中下载 CodeGeeX 插件获得更加全面的AI编程体验，详情见[CodeGeeX主页](https://codegeex.cn/)。


## 快速开始

### 使用`transformers`快速调用[CodeGeeX2-6B](https://huggingface.co/THUDM/codegeex2-6b)：

```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True, device='cuda')
model = model.eval()

# remember adding a language tag for better performance
prompt = "# language: Python\n# write a bubble sort function\n"
inputs = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(inputs, max_length=256, top_k=1)
response = tokenizer.decode(outputs[0])

>>> print(response)
# language: Python
# write a bubble sort function


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubble_sort([5, 2, 1, 8, 4]))
```

### 启动 Gradio DEMO：
```
python ./demo/run_demo.py

usage: run_demo.py [-h] [--model-path MODEL_PATH] [--example-path EXAMPLE_PATH] [--quantize QUANTIZE]
                   [--chatglm-cpp] [--fastllm] [--n-gpus N_GPUS] [--gpu GPU] [--cpu] [--auth] [--username yourname]
                   [--password yourpassword]
                   [--port PORT] [--listen ADDRESS]

# 若要启用身份验证，请先启用--auth，然后定义--username与--password，如：
python run_demo.py --auth --username user --password password  # 若要监听所有地址请指定 --listen 0.0.0.0
```
支持使用 [ChatGLM.cpp](https://github.com/li-plus/chatglm.cpp) 量化推理加速：
```sh
python ./demo/run_demo.py --quantize 4 --chatglm-cpp
```
### 启动FAST API:
```
python ./demo/fastapicpu.py
usage: fastapicpu.py [-h] [--model-path MODEL_PATH] [--listen ADDRESS] [--port PORT] [--workders NUM] [--cpu] [--half] [--quantize QUANTIZE] [--chatglm-cpp]
# --cpu启用cpu --half启用.half()
```
支持使用 [ChatGLM.cpp](https://github.com/li-plus/chatglm.cpp) 量化推理加速，同样添加 `--quantize 4 --chatglm-cpp` 参数即可。
### API使用示例
```
curl -X POST "http://127.0.0.1:7860" \
    -H 'Content-Type: application/json' \
    -d '{"lang": "Python", "prompt": "# Write a quick sort function"}'
```


❗️请注意：
* CodeGeeX2-6B 是一个基座代码生成模型，不具备聊天能力。请前往插件中体验更全面的 Ask CodeGeeX 聊天功能。
* 在使用 CodeGeeX2-6B 的补全功能时，输入prompt需要遵循特定的格式以获得最好的效果。比如需要在开头加入编程语言标签（`# language: Python`，请查看[完整语言列表](https://github.com/THUDM/CodeGeeX2/blob/main/evaluation/utils.py#L14)），以注释的形式写prompt等。参考`run_demo.py`中的处理。
* 如果显卡不支持`bfloat16`格式，将会输出错误的内容，需要将模型转换成`float16`格式：
    ```python
    model = AutoModel.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True).half().cuda()
    ```
* 如果需要使用多显卡加载模型,可以将以下代码：
    ```python
    tokenizer = AutoTokenizer.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True, device='cuda')
    model = model.eval()
    ```
    替换为

    ```python
    def get_model():
        tokenizer = AutoTokenizer.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True)
        from gpus import load_model_on_gpus
        # gpus文件在demo文件夹中
        model = load_model_on_gpus("THUDM/codegeex2-6b", num_gpus=2)
        model = model.eval()
        return tokenizer, model

    tokenizer, model = get_model()
    ```

## 代码能力评测

CodeGeeX2 作为一个多语言代码生成基座模型，代码能力较上一代大幅提升，以下是在 HumanEval，HumanEval-X, DS1000 基准上的评测结果（评价指标 Pass@k 定义与[论文](https://arxiv.org/abs/2303.17568)中一致）：

### HumanEval (Pass@1,10,100)

| **Model**           | **Pass@1** | **Pass@10** | **Pass@100** |
| :-----------------: | :--------: | :---------: | :----------: |
| CodeGen-16B-multi   | 19\.2      | 34\.6       | 55\.2        |
| CodeGeeX-13B        | 22\.9      | 39\.6       | 60\.9        |
| Codex-12B           | 28\.8      | 46\.8       | 72\.3        |
| CodeT5Plus-16B-mono | 30\.9      | 51\.6       | 76\.7        |
| Code-Cushman-001    | 33\.5      | 54\.3       | 77\.4        |
| LLaMA-65B           | 23\.7      | -           | 79\.3        |
| LLaMA2-70B          | 29\.9      | -           | -            |
| CodeGen2\.5-7B-mono | 33\.4      | 58\.4       | 82\.7        |
| StarCoder-15B       | 33\.2      | 61\.0       | 84\.7        |
| **CodeGeeX2-6B**    | **35\.9**  | **62\.6**   | **88\.3**    |
> **Pass@1** 使用 `n=20, t=0.2, top_p=0.95`；**Pass@10,Pass@100** 使用 `n=200, t=0.8, top_p=0.95`。

### HumanEval-X (Pass@1)

| **Model**                | **Python** | **C++**   | **Java**  | **JavaScript** | **Go**    | **Rust**  | **Overall** |
| :------------------: | :--------: | :-------: | :-------: | :------------: | :-------: | :-------: | :---------: |
| CodeGen-16B-multi    | 19\.2      | 18\.1     | 15\.0     | 18\.4          | 13\.0     | 1\.8      | 14\.2       |
| CodeGeeX-13B         | 22\.9      | 17\.1     | 20\.0     | 17\.6          | 14\.4     | 4\.3      | 16\.0       |
| Replit-code-v1-3B    | 22\.0      | 20\.1     | 20\.1     | 20\.1          | 12\.2     | 8\.6      | 17\.2       |
| CodeGen2\.5-7B-multi | 30\.6      | 24\.3     | 29\.0     | 27\.5          | 18\.9     | **20\.1** | 25\.1       |
| StarCoder-15B        | 35\.5      | 28\.2     | **31\.5** | **33\.2**      | 21\.3     | 17\.8     | 27\.9       |
| **CodeGeeX2-6B**         | **35\.9**  | **29\.3** | 30\.8     | 32\.2          | **22\.5** | 18\.1     | **28\.1**   |
> **Pass@1** 使用 `n=20, t=0.2, top_p=0.95`。

以上结果可使用脚本`scripts/run_humanevalx.sh`复现。环境配置和说明参见[评测环境](https://github.com/THUDM/CodeGeeX/blob/main/codegeex/benchmark/README_zh.md)。

### DS1000 (Pass@1)

| **Model**            | **Matplotlib** | **Numpy** | **Pandas** | **Pytorch** | **SciPy** | **Scikit-learn** | **TensorFlow** | **Overall** |
| :--------------: | :------------: | :-------: | :--------: | :---------: | :-------: | :--------------: | :------------: | :---------: |
| \# Samples       | 155            | 220       | 291        | 68          | 106       | 115              | 45             | 1000        |
| CodeGen-16B-Mono | 31\.7          | 10\.9     | 3\.4       | 7\.0        | 9\.0      | 10\.8            | 15\.2          | 11\.7       |
| code-cushman-001 | 40\.7          | 21\.8     | 7\.9       | 12\.4       | 11\.3     | 18\.0            | 12\.2          | 18\.1       |
| Codex-001        | 41\.8          | 26\.6     | 9\.4       | 9\.7        | 15\.0     | 18\.5            | 17\.2          | 20\.2       |
| **CodeGeeX2-6B** | 40\.5          | 25\.5     | 14\.5      | 17\.3       | 19\.3     | 24\.0            | 23\.0          | 23\.1       |
| StarCoder-15B    | 51\.7          | 29\.7     | 11\.4      | 21\.4       | 20\.2     | 29\.5            | 24\.5          | 26\.0       |
| Codex-002        | **57\.0**      | **43\.1** | **26\.5**  | **41\.8**   | **31\.8** | **44\.8**        | **39\.3**      | **39\.2**   |
> **Pass@1** 使用 `n=40, t=0.2, top_p=0.5`。

以上结果可使用[DS1000评测代码](https://github.com/HKUNLP/DS-1000.git)复现。

## 量化推理性能

CodeGeeX2 与上一代相比，对部署更加友好。得益于使用 Multi-Query Attention 和 Flash Attention，推理速度更快，且量化后仅需6GB显存即可运行：

### 量化

| **Model**        | FP16/BF16 | INT8    | INT4   |
| :--------------: | :-------: | :-----: | :----: |
| CodeGeeX-13B     | 26\.9 GB   | 14\.7 GB | -      |
| **CodeGeeX2-6B** | 13\.1 GB  | 8\.2 GB  | 5\.5 GB |
> 基于 PyTorch 2.0 测试，利用`torch.nn.functional.scaled_dot_product_attention`实现高效的 Attention 计算。

### 推理

| **Model**        | **推理速度 (字符/秒)** |
| :--------------: | :-------------: |
| CodeGeeX-13B     | 32              |
| **CodeGeeX2-6B** | 94              |
> `batch_size=1, max_length=2048`，均使用加速框架，测试硬件为`GeForce RTX-3090`。

## 协议

本仓库的代码依照 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) 协议开源，模型的权重的使用则需要遵循 [Model License](MODEL_LICENSE)。CodeGeeX2-6B 权重对学术研究完全开放，填写[登记表](https://open.bigmodel.cn/mla/form?mcode=CodeGeeX2-6B)申请商业使用。


## 引用

如果觉得我们的工作有帮助，欢迎引用以下论文：

```
@inproceedings{zheng2023codegeex,
  title={CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Benchmarking on HumanEval-X},
  author={Qinkai Zheng and Xiao Xia and Xu Zou and Yuxiao Dong and Shan Wang and Yufei Xue and Zihan Wang and Lei Shen and Andi Wang and Yang Li and Teng Su and Zhilin Yang and Jie Tang},
  booktitle={Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages={5673--5684},
  year={2023}
}
```
