# OmniParser: 基于纯视觉的 GUI Agent 屏幕解析工具

<p align="center">
  <img src="imgs/logo.png" alt="Logo">
</p>
<!-- <a href="https://trendshift.io/repositories/12975" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12975" alt="microsoft%2FOmniParser | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a> -->

[![arXiv](https://img.shields.io/badge/Paper-green)](https://arxiv.org/abs/2408.00203)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

📢 [[Project Page](https://microsoft.github.io/OmniParser/)] [[V2 Blog Post](https://www.microsoft.com/en-us/research/articles/omniparser-v2-turning-any-llm-into-a-computer-use-agent/)] [[Models V2](https://huggingface.co/microsoft/OmniParser-v2.0)] [[Models V1.5](https://huggingface.co/microsoft/OmniParser)] [[HuggingFace Space Demo](https://huggingface.co/spaces/microsoft/OmniParser-v2)]

**OmniParser** 是一种全面的方法，用于将用户界面的截图解析为结构化且易于理解的元素，这显著增强了 GPT-4V 生成能够准确定位到界面相应区域的操作的能力。 

## News
- [2025/3] 我们支持轨迹（trajectory）的本地日志记录，以便你可以使用 OmniParser + OmniTool 构建适合你所在领域偏好的 Agent 的训练数据流水线。[文档编写中 WIP]
- [2025/3] 我们正在逐步添加多 Agent 编排功能，并改进 OmniTool 的用户界面以获得更好的体验。
- [2025/2] 我们发布了 OmniParser V2 [检查点（checkpoints）](https://huggingface.co/microsoft/OmniParser-v2.0)。[观看视频](https://1drv.ms/v/c/650b027c18d5a573/EWXbVESKWo9Buu6OYCwg06wBeoM97C6EOTG6RjvWLEN1Qg?e=alnHGC)
- [2025/2] 我们推出了 OmniTool：使用 OmniParser + 你选择的视觉模型来控制 Windows 11 VM。OmniTool 开箱即用支持以下大语言模型——OpenAI (4o/o1/o3-mini)、DeepSeek (R1)、Qwen (2.5VL) 或 Anthropic Computer Use。[观看视频](https://1drv.ms/v/c/650b027c18d5a573/EehZ7RzY69ZHn-MeQHrnnR4BCj3by-cLLpUVlxMjF4O65Q?e=8LxMgX)
- [2025/1] V2 即将发布。我们在新的定位（Grounding）基准测试 [Screen Spot Pro](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding/tree/main) 上取得了 39.5% 的新 SOTA（最先进）成绩！更多详情请点击[这里](https://github.com/microsoft/OmniParser/tree/master/docs/Evaluation.md)。
- [2024/11] 我们发布了更新版本 OmniParser V1.5，具备以下特性：1) 更细粒度/小图标检测；2) 预测每个屏幕元素是否可交互。示例见 demo.ipynb。 
- [2024/10] OmniParser 成为 Hugging Face Model Hub 上排名第一的热门模型（自 2024/10/29 起）。 
- [2024/10] 欢迎在 [HuggingFace Space](https://huggingface.co/spaces/microsoft/OmniParser) 体验我们的演示！（敬请期待 OmniParser + Claude Computer Use）
- [2024/10] 交互式区域检测模型与图标功能描述模型均已发布！[HuggingFace 模型链接](https://huggingface.co/microsoft/OmniParser)
- [2024/09] OmniParser 在 [Windows Agent Arena](https://microsoft.github.io/WindowsAgentArena/) 上取得了最佳性能！ 

## Install 
首先克隆仓库，然后安装环境：
```python
cd OmniParser
conda create -n "omni" python==3.12
conda activate omni
pip install -r requirements.txt
```

确保 `weights` 文件夹中已下载 V2 权重（请确认 caption 权重文件夹名为 `icon_caption_florence`）。如果尚未下载，请使用以下命令：
```
   # download the model checkpoints to local directory OmniParser/weights/
   for f in icon_detect/{train_args.yaml,model.pt,model.yaml} icon_caption/{config.json,generation_config.json,model.safetensors}; do huggingface-cli download microsoft/OmniParser-v2.0 "$f" --local-dir weights; done
   mv weights/icon_caption weights/icon_caption_florence
```

<!-- ## [deprecated]
Then download the model ckpts files in: https://huggingface.co/microsoft/OmniParser, and put them under weights/, default folder structure is: weights/icon_detect, weights/icon_caption_florence, weights/icon_caption_blip2. 

For v1: 
convert the safetensor to .pt file. 
```python
python weights/convert_safetensor_to_pt.py

For v1.5: 
download 'model_v1_5.pt' from https://huggingface.co/microsoft/OmniParser/tree/main/icon_detect_v1_5, make a new dir: weights/icon_detect_v1_5, and put it inside the folder. No weight conversion is needed. 
``` -->

## Examples:
我们在 `demo.ipynb` 中提供了一些简单的示例。 

## Gradio Demo
要运行 Gradio 演示，只需执行：
```python
python gradio_demo.py
```

## Model Weights License
关于 Hugging Face Model Hub 上的模型检查点，请注意 `icon_detect` 模型采用 AGPL 许可证（继承自原始 YOLO 模型的许可证）。而 `icon_caption_blip2` 与 `icon_caption_florence` 采用 MIT 许可证。请参阅每个模型文件夹中的 LICENSE 文件：https://huggingface.co/microsoft/OmniParser。

## 📚 Citation
我们的技术报告可在[这里](https://arxiv.org/abs/2408.00203)找到。
如果你觉得我们的工作有用，请考虑引用我们的研究：
```
@misc{lu2024omniparserpurevisionbased,
      title={OmniParser for Pure Vision Based GUI Agent}, 
      author={Yadong Lu and Jianwei Yang and Yelong Shen and Ahmed Awadallah},
      year={2024},
      eprint={2408.00203},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2408.00203}, 
}
```