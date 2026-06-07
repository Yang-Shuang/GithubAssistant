# UI-TARS：以原生智能体引领自动化 GUI 交互的新篇章
![Local Image](figures/writer.png)
<div align="center">
<p>
        🌐 <a href="https://seed-tars.com/">Website</a>&nbsp&nbsp | 🤗 <a href="https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B">Hugging Face Models</a>&nbsp&nbsp 
        | &nbsp&nbsp 🔧 <a href="README_deploy.md">Deployment</a> &nbsp&nbsp  | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2501.12326">Paper</a> &nbsp&nbsp  |&nbsp&nbsp</a>
🖥️ <a href="https://github.com/bytedance/UI-TARS-desktop">UI-TARS-desktop</a>&nbsp&nbsp  <br>🏄 <a href="https://github.com/web-infra-dev/Midscene">Midscene (Browser Automation) </a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/pTXwYVjfcs">Discord</a>&nbsp&nbsp
</p>

[![](https://trendshift.io/api/badge/repositories/13561)](https://trendshift.io/repositories/13561)
</div>

我们还提供了 **UI-TARS-desktop** 版本，支持在您的**本地个人设备**上运行。如需使用，请访问 [https://github.com/bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)。若要在网页自动化中使用 UI-TARS，可参考开源项目 [Midscene.js](https://github.com/web-infra-dev/Midscene)。
**❗注意**：由于基于 Qwen 2.5VL 的模型使用绝对坐标进行目标定位，请务必参阅我们的 <a href="README_coordinates.md">指南</a> 中关于坐标处理的说明。

## Updates（更新记录）
- 🌟 2025.09.04：我们很高兴宣布发布 **UI-TARS-2**，这是 UI-TARS-1.5 的重大升级版本，在 GUI、游戏、代码和工具使用方面具备增强的能力。它是一个“全能型”智能体（Agent）模型，能够无缝整合多种能力以处理复杂任务。更多详情请查阅我们的最新 [技术报告](https://arxiv.org/abs/2509.02544)。欢迎在我们的 [官网展示页](https://seed-tars.com/showcase/ui-tars-2/) 查看更多精彩案例。
- 🌟 2025.04.16：我们在 [博客](https://seed-tars.com/1.5) 分享了 UI-TARS-1.5 模型的最新进展，该模型在游戏和 GUI 任务中表现优异，并已开源 [UI-TARS-1.5-7B](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B)。
- ✨ 2025.03.23：我们更新了来自官方 [OSWorld 仓库](https://github.com/xlang-ai/OSWorld/blob/main/run_uitars.py) 的 OSWorld 推理脚本。现在，你可以使用 OSWorld 官方的推理脚本来复现我们的结果。

## Introduction（简介）

UI-TARS-1.5 是一个基于强大视觉语言模型（VLM）构建的开源多模态智能体。它能够高效地在虚拟世界中执行多样化的任务。

依托 [我们最近的论文](https://arxiv.org/abs/2501.12326) 中引入的基础架构，UI-TARS-1.5 集成了由强化学习驱动的高级推理能力。这使得模型能够在采取行动前进行思维推演（Chain-of-Thought），显著提升了其性能与适应性，特别是在推理时间扩展方面表现突出。我们的新版 1.5 版本在多项标准基准测试中取得了最先进（SOTA）的结果，展现了强大的推理能力，并在各项指标上较先前模型有显著提升。
<!-- ![Local Image](figures/UI-TARS.png) -->
<p align="center">
    <video controls width="480">
      <source src="https://huggingface.co/datasets/JjjFangg/Demo_video/resolve/main/GUI_demo.mp4" type="video/mp4">
    </video>

<p>
<p align="center">
    <video controls width="480">
      <source src="https://huggingface.co/datasets/JjjFangg/Demo_video/resolve/main/Game_demo.mp4" type="video/mp4">
    </video>
<p>

## 🚀 快速开始指南：部署与使用我们的模型

为了帮助你快速上手我们的模型，我们建议按顺序执行以下步骤。这些步骤将指导你完成部署、预测后处理流程，使模型能在你的环境中采取行动。


### ✅ Step 1: Deployment & Inference（部署与推理）
👉 <a href="README_deploy.md">Deployment and Inference</a>.
This includes instructions for model deployment using huggingface endpoint, and running your first prediction. -> 本指南包含使用 Hugging Face Endpoint 进行模型部署的说明，以及运行首次预测的步骤。


### ✅ Step 2: Post Processing（后处理）

#### Installation（安装）
```bash
pip install ui-tars
# or
uv pip install ui-tars
```
#### Usage（使用方法）
```python
from ui_tars.action_parser import parse_action_to_structure_output, parsing_response_to_pyautogui_code

response = "Thought: Click the button\nAction: click(start_box='(100,200)')"
original_image_width, original_image_height = 1920, 1080
parsed_dict = parse_action_to_structure_output(
    response,
    factor=1000,
    origin_resized_height=original_image_height,
    origin_resized_width=original_image_width,
    model_type="qwen25vl"
)
print(parsed_dict)
parsed_pyautogui_code = parsing_response_to_pyautogui_code(
    responses=parsed_dict,
    image_height=original_image_height,
    image_width=original_image_width
)
print(parsed_pyautogui_code)
```
##### FYI: Coordinates visualization（参考信息：坐标可视化）
To help you better understand the coordinate processing, we also provide a <a href="README_coordinates.md">guide</a> for coordinates processing visualization. -> 为了帮助你更好地理解坐标处理过程，我们还提供了 <a href="README_coordinates.md">指南</a> 用于坐标处理的可视化说明。

## Prompt Usage Guide（Prompt 使用指南）

To accommodate different device environments and task complexities, the following three prompt templates in <a href="codes/ui_tars/prompt.py">codes/ui_tars/prompt.py</a>. are designed to guide GUI agents in generating appropriate actions. Choose the template that best fits your use case: -> 为了适配不同的设备环境和任务复杂度，我们在 <a href="codes/ui_tars/prompt.py">codes/ui_tars/prompt.py</a> 中设计了以下三种 Prompt（提示词）模板，用于引导 GUI 智能体生成合适的操作。请根据你的使用场景选择最合适的模板：

### 🖥️ `COMPUTER_USE`

**Recommended for**: GUI tasks on **desktop environments** such as Windows, Linux, or macOS. -> **适用场景**：**桌面环境**（如 Windows、Linux 或 macOS）上的 GUI 任务。

**Features**: -> **功能特点**：
- Supports common desktop operations: mouse clicks (single, double, right), drag actions, keyboard shortcuts, text input, scrolling, etc. -> - 支持常见的桌面操作：鼠标单击/双击/右键、拖拽、键盘快捷键、文本输入、滚动等。
- Ideal for browser navigation, office software interaction, file management, and other desktop-based tasks. -> - 非常适合浏览器导航、办公软件交互、文件管理等基于桌面的任务。


### 📱 `MOBILE_USE`

**Recommended for**: GUI tasks on **mobile devices or Android emulators**. -> **适用场景**：**移动设备或 Android 模拟器**上的 GUI 任务。

**Features**: -> **功能特点**：
- Includes mobile-specific actions: `long_press`, `open_app`, `press_home`, `press_back`. -> - 包含移动端专属操作：`long_press`（长按）、`open_app`（打开应用）、`press_home`（按主页键）、`press_back`（返回）。
- Suitable for launching apps, scrolling views, filling input fields, and navigating within mobile apps. -> - 适用于启动应用、滚动视图、填写输入框以及在移动应用内导航。


### 📌 `GROUNDING` 

**Recommended for**: Lightweight tasks focused solely on **action output**, or for use in model training and evaluation. -> **适用场景**：仅关注**动作输出**的轻量级任务，或用于模型训练与评估。

**Features**: -> **功能特点**：
- Only outputs the `Action` without any reasoning (`Thought`). -> - 仅输出 `Action`（动作），不包含任何推理过程（`Thought`）。
- Useful for evaluating grounding capability. -> - 适用于评估模型的定位/接地能力。

---

When developing or evaluating multimodal interaction systems, choose the appropriate prompt template based on your target platform (desktop vs. mobile) -> 在开发或评估多模态交互系统时，请根据你的目标平台（桌面端 vs 移动端）选择合适的 Prompt 模板。


## Performance（性能表现）
**Online Benchmark Evaluation（在线基准测试评估）**
| Benchmark type | Benchmark                                                                                                                                       | UI-TARS-1.5 | OpenAI CUA | Claude 3.7 | Previous SOTA       |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------|------------|----------------------|
| **Computer Use** | [OSworld](https://arxiv.org/abs/2404.07972) (100 steps)                                                                                        | **42.5**     | 36.4        | 28          | 38.1 (200 step)      |
|                | [Windows Agent Arena](https://arxiv.org/abs/2409.08264) (50 steps)                                                                              | **42.1**     | -           | -           | 29.8                 |
| **Browser Use**  | [WebVoyager](https://arxiv.org/abs/2401.13919)                                                                                                 | 84.8         | **87**      | 84.1        | 87                   |
|                | [Online-Mind2web](https://arxiv.org/abs/2504.01382)                                                                                              | **75.8**     | 71          | 62.9        | 71                   |
| **Phone Use**    | [Android World](https://arxiv.org/abs/2405.14573)                                                                                              | **64.2**     | -           | -           | 59.5                 |


**Grounding Capability Evaluation（定位能力评估）**
| Benchmark | UI-TARS-1.5 | OpenAI CUA | Claude 3.7 | Previous SOTA |
|-----------|-------------|------------|------------|----------------|
| [ScreenSpot-V2](https://arxiv.org/pdf/2410.23218) | **94.2** | 87.9 | 87.6 | 91.6 |
| [ScreenSpotPro](https://arxiv.org/pdf/2504.07981v1) | **61.6** | 23.4 | 27.7 | 43.6 |



**Poki Game（游戏测试）**

| Model       | [2048](https://poki.com/en/g/2048) | [cubinko](https://poki.com/en/g/cubinko) | [energy](https://poki.com/en/g/energy) | [free-the-key](https://poki.com/en/g/free-the-key) | [Gem-11](https://poki.com/en/g/gem-11) | [hex-frvr](https://poki.com/en/g/hex-frvr) | [Infinity-Loop](https://poki.com/en/g/infinity-loop) | [Maze:Path-of-Light](https://poki.com/en/g/maze-path-of-light) | [shapes](https://poki.com/en/g/shapes) | [snake-solver](https://poki.com/en/g/snake-solver) | [wood-blocks-3d](https://poki.com/en/g/wood-blocks-3d) | [yarn-untangle](https://poki.com/en/g/yarn-untangle) | [laser-maze-puzzle](https://poki.com/en/g/laser-maze-puzzle) | [tiles-master](https://poki.com/en/g/tiles-master) |
|-------------|-----------|--------------|-------------|-------------------|-------------|---------------|---------------------|--------------------------|-------------|--------------------|----------------------|---------------------|------------------------|---------------------|
| OpenAI CUA  | 31.04     | 0.00         | 32.80       | 0.00              | 46.27       | 92.25         | 23.08               | 35.00                    | 52.18       | 42.86              | 2.02                 | 44.56               | 80.00                  | 78.27               |
| Claude 3.7  | 43.05     | 0.00         | 41.60       | 0.00              | 0.00        | 30.76         | 2.31                | 82.00                    | 6.26        | 42.86              | 0.00                 | 13.77               | 28.00                  | 52.18               |
| UI-TARS-1.5 | 100.00    | 0.00         | 100.00      | 100.00            | 100.00      | 100.00        | 100.00              | 100.00                   | 100.00      | 100.00             | 100.00               | 100.00              | 100.00                 | 100.00              |


**Minecraft（我的世界）**

| Task Type   | Task Name           | [VPT](https://openai.com/index/vpt/) | [DreamerV3](https://www.nature.com/articles/s41586-025-08744-2) | Previous SOTA | UI-TARS-1.5 w/o Thought | UI-TARS-1.5 w/ Thought |
|-------------|---------------------|----------|----------------|--------------------|------------------|-----------------|
| Mine Blocks | (oak_log)               | 0.8      | 1.0            | 1.0                | 1.0              | 1.0             |
|             | (obsidian)          | 0.0      | 0.0            | 0.0                | 0.2              | 0.3             |
|             | (white_bed)               | 0.0      | 0.0            | 0.1                | 0.4              | 0.6             |
|             | **200 Tasks Avg.**  | 0.06     | 0.03           | 0.32               | 0.35             | 0.42            |
| Kill Mobs   | (mooshroom)            | 0.0      | 0.0            | 0.1                | 0.3              | 0.4             |
|             | (zombie)            | 0.4      | 0.1            | 0.6                | 0.7              | 0.9             |
|             | (chicken)          | 0.1      | 0.0            | 0.4                | 0.5              | 0.6             |
|             | **100 Tasks Avg.**  | 0.04     | 0.03           | 0.18               | 0.25             | 0.31            |

## Model Scale Comparison（模型规模对比）

Here we compare performance across different model scales of UI-TARS on the OSworld benchmark. -> 以下我们在 OSWorld 基准测试上对比了不同规模的 UI-TARS 模型性能。

| **Benchmark Type** | **Benchmark**                      | **UI-TARS-72B-DPO** | **UI-TARS-1.5-7B** | **UI-TARS-1.5** |
|--------------------|------------------------------------|---------------------|--------------------|-----------------|
| Computer Use       | [OSWorld](https://arxiv.org/abs/2404.07972)             | 24.6                | 27.5               | **42.5**        |
| GUI Grounding      | [ScreenSpotPro](https://arxiv.org/pdf/2504.07981v1) | 38.1                | 49.6               | **61.6**        |

### Limitations（局限性）

While UI-TARS-1.5 represents a significant advancement in multimodal agent capabilities, we acknowledge several important limitations: -> 尽管 UI-TARS-1.5 在多模态智能体能力方面取得了显著进展，但我们承认仍存在以下几项重要局限：

- **Misuse:** Given its enhanced performance in GUI tasks, including successfully navigating authentication challenges like CAPTCHA, UI-TARS-1.5 could potentially be misused for unauthorized access or automation of protected content. To mitigate this risk, extensive internal safety evaluations are underway. -> - **滥用风险**：鉴于其在 GUI 任务中表现优异（包括成功破解 CAPTCHA 等身份验证挑战），UI-TARS-1.5 可能被滥用于未经授权访问或自动化受保护内容。为降低此风险，我们正在进行广泛的内部安全评估。
- **Computation:** UI-TARS-1.5 still requires substantial computational resources, particularly for large-scale tasks or extended gameplay scenarios. -> - **计算资源**：UI-TARS-1.5 仍需消耗大量计算资源，尤其是在处理大规模任务或长时间游戏场景时。
- **Hallucination**: UI-TARS-1.5 may occasionally generate inaccurate descriptions, misidentify GUI elements, or take suboptimal actions based on incorrect inferences—especially in ambiguous or unfamiliar environments. -> - **幻觉问题**：UI-TARS-1.5 偶尔可能生成不准确的描述、错误识别 GUI 元素，或基于错误的推理采取次优操作——这在模糊或不熟悉的环境中尤为明显。
- **Model scale:** The released UI-TARS-1.5-7B focuses primarily on enhancing general computer use capabilities and is not specifically optimized for game-based scenarios, where the UI-TARS-1.5 still holds a significant advantage. -> - **模型规模限制**：开源的 UI-TARS-1.5-7B 主要侧重于增强通用电脑使用能力，并未针对游戏场景进行专门优化；而在游戏场景中，完整版 UI-TARS-1.5 仍具有显著优势。

## What's next（后续计划）

We are providing early research access to our top-performing UI-TARS-1.5 model to facilitate collaborative research. Interested researchers can contact us at TARS@bytedance.com. -> 我们正在向研究人员提供高性能 UI-TARS-1.5 模型的早期研究访问权限，以促进协作研究。感兴趣的学者可通过 TARS@bytedance.com 联系我们。

Looking ahead, we envision UI-TARS evolving into increasingly sophisticated agentic experiences capable of performing real-world actions, thereby empowering platforms such as [doubao](https://team.doubao.com/en/) to accomplish more complex tasks for you :) -> 展望未来，我们期望 UI-TARS 演变为更复杂的智能体体验，能够执行现实世界的操作，从而赋能 [doubao](https://team.doubao.com/en/) 等平台为你完成更复杂的任务 :)

## Star History（⭐ Star 历史）

[![Star History Chart](https://api.star-history.com/svg?repos=bytedance/UI-TARS&type=Date)](https://www.star-history.com/#bytedance/UI-TARS&Date)

## Citation（引用方式）
If you find our paper and model useful in your research, feel free to give us a cite. -> 如果你的研究使用了我们的论文和模型，欢迎引用我们。

```BibTeX
@article{qin2025ui,
  title={UI-TARS: Pioneering Automated GUI Interaction with Native Agents},
  author={Qin, Yujia and Ye, Yining and Fang, Junjie and Wang, Haoming and Liang, Shihao and Tian, Shizuo and Zhang, Junda and Li, Jiahao and Li, Yunxin and Huang, Shijue and others},
  journal={arXiv preprint arXiv:2501.12326},
  year={2025}
}
```