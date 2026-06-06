[![Python Versions](https://img.shields.io/pypi/pyversions/pyqlib.svg?logo=python&logoColor=white)](https://pypi.org/project/pyqlib/#files)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey)](https://pypi.org/project/pyqlib/#files)
[![PypI Versions](https://img.shields.io/pypi/v/pyqlib)](https://pypi.org/project/pyqlib/#history)
[![Upload Python Package](https://github.com/microsoft/qlib/workflows/Upload%20Python%20Package/badge.svg)](https://pypi.org/project/pyqlib/)
[![Github Actions Test Status](https://github.com/microsoft/qlib/workflows/Test/badge.svg?branch=main)](https://github.com/microsoft/qlib/actions)
[![Documentation Status](https://readthedocs.org/projects/qlib/badge/?version=latest)](https://qlib.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/pypi/l/pyqlib)](LICENSE)
[![Join the chat at https://gitter.im/Microsoft/qlib](https://badges.gitter.im/Microsoft/qlib.svg)](https://gitter.im/Microsoft/qlib?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## :newspaper: **最新动态！** &nbsp;   :sparkling_heart: 

近期发布的功能

### 介绍 <a href="https://github.com/microsoft/RD-Agent"><img src="docs/_static/img/rdagent_logo.png" alt="RD_Agent" style="height: 2em"></a>：基于大语言模型的工业数据驱动研发自主演化智能体

我们很高兴宣布发布 **RD-Agent**📢，这是一款强大的工具，支持量化投资研发中的自动化因子挖掘和模型优化。

RD-Agent 现已在 [GitHub](https://github.com/microsoft/RD-Agent) 上开源，欢迎点亮你的 Star🌟！

欲了解更多详情，请访问 [RD-Agent 仓库](https://github.com/microsoft/RD-Agent)。我们为你准备了一些公开演示视频：

| 场景 | 演示视频（英文） | 演示视频（中文） |
| --                      | ------    | ------    |
| 量化因子挖掘 | [YouTube](https://www.youtube.com/watch?v=X4DK2QZKaKY&t=6s) | [YouTube](https://www.youtube.com/watch?v=X4DK2QZKaKY&t=6s) |
| 从研报中挖掘量化因子 | [YouTube](https://www.youtube.com/watch?v=ECLTXVcSx-c) | [YouTube](https://www.youtube.com/watch?v=ECLTXVcSx-c) |
| 量化模型优化 | [YouTube](https://www.youtube.com/watch?v=dm0dWL49Bc0&t=104s) | [YouTube](https://www.youtube.com/watch?v=dm0dWL49Bc0&t=104s) |

- 📃**论文**: [R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)
- 👾**代码**: https://github.com/microsoft/RD-Agent/
```BibTeX
@misc{li2025rdagentquant,
    title={R\&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization},
    author={Yuante Li and Xu Yang and Xiao Yang and Minrui Xu and Xisen Wang and Weiqing Liu and Jiang Bian},
    year={2025},
    eprint={2505.15155},
    archivePrefix={arXiv},
    primaryClass={cs.AI}
}
```
![image](https://github.com/user-attachments/assets/3198bc10-47ba-4ee0-8a8e-46d5ce44f45d)

***

| 功能 | 状态 |
| --                      | ------    |
| [R&D-Agent-Quant](https://arxiv.org/abs/2505.15155) 已发表 | 将 R&D-Agent 应用于 Qlib 进行量化交易 | 
| 端到端学习的 BPQP | 📈即将推出！（[审核中](https://github.com/microsoft/qlib/pull/1863)） |
| 🔥大语言模型驱动的自动量化工厂🔥 | 🚀已于 2024年8月8日在 [♾️RD-Agent](https://github.com/microsoft/RD-Agent) 发布 |
| KRNN 和 Sandwich 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/1414/) 于 2023年5月26日 |
| Qlib v0.9.0 发布 | :octocat: [已发布](https://github.com/microsoft/qlib/releases/tag/v0.9.0) 于 2022年12月9日 |
| RL 学习框架 | :hammer: :chart_with_upwards_trend: 已于 2022年11月10日发布。[#1332](https://github.com/microsoft/qlib/pull/1332), [#1322](https://github.com/microsoft/qlib/pull/1322), [#1316](https://github.com/microsoft/qlib/pull/1316),[#1299](https://github.com/microsoft/qlib/pull/1299),[#1263](https://github.com/microsoft/qlib/pull/1263), [#1244](https://github.com/microsoft/qlib/pull/1244), [#1169](https://github.com/microsoft/qlib/pull/1169), [#1125](https://github.com/microsoft/qlib/pull/1125), [#1076](https://github.com/microsoft/qlib/pull/1076)|
| HIST 和 IGMTF 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/1040) 于 2022年4月10日 |
| Qlib [notebook 教程](https://github.com/microsoft/qlib/tree/main/examples/tutorial) | 📖 [已发布](https://github.com/microsoft/qlib/pull/1037) 于 2022年4月7日 | 
| Ibovespa 指数数据 | :rice: [已发布](https://github.com/microsoft/qlib/pull/990) 于 2022年4月6日 |
| 实时数据库 (Point-in-Time database) | :hammer: [已发布](https://github.com/microsoft/qlib/pull/343) 于 2022年3月10日 |
| Arctic Provider Backend & Orderbook 数据示例 | :hammer: [已发布](https://github.com/microsoft/qlib/pull/744) 于 2022年1月17日 |
| 基于元学习的框架及 DDG-DA  | :chart_with_upwards_trend:  :hammer: [已发布](https://github.com/microsoft/qlib/pull/743) 于 2022年1月10日 | 
| 基于规划的组合优化 | :hammer: [已发布](https://github.com/microsoft/qlib/pull/754) 于 2021年12月28日 | 
| Qlib v0.8.0 发布 | :octocat: [已发布](https://github.com/microsoft/qlib/releases/tag/v0.8.0) 于 2021年12月8日 |
| ADD 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/704) 于 2021年11月22日 |
| ADARNN 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/689) 于 2021年11月14日 |
| TCN 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/668) 于 2021年11月4日 |
| 嵌套决策框架 (Nested Decision Framework) | :hammer: [已发布](https://github.com/microsoft/qlib/pull/438) 于 2021年10月1日。[示例](https://github.com/microsoft/qlib/blob/main/examples/nested_decision_execution/workflow.py) 和 [文档](https://qlib.readthedocs.io/en/latest/component/highfreq.html) |
| Temporal Routing Adaptor (TRA) | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/531) 于 2021年7月30日 |
| Transformer & Localformer | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/508) 于 2021年7月22日 |
| Qlib v0.7.0 发布 | :octocat: [已发布](https://github.com/microsoft/qlib/releases/tag/v0.7.0) 于 2021年7月12日 |
| TCTS 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/491) 于 2021年7月1日 |
| 在线服务与自动模型滚动更新 | :hammer:  [已发布](https://github.com/microsoft/qlib/pull/290) 于 2021年5月17日 | 
| DoubleEnsemble 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/286) 于 2021年3月2日 | 
| 高频数据处理示例 | :hammer: [已发布](https://github.com/microsoft/qlib/pull/257) 于 2021年2月5日  |
| 高频交易示例 | :chart_with_upwards_trend: [部分代码已发布](https://github.com/microsoft/qlib/pull/227) 于 2021年1月28日  | 
| 高频数据(1min) | :rice: [已发布](https://github.com/microsoft/qlib/pull/221) 于 2021年1月27日 |
| Tabnet 模型 | :chart_with_upwards_trend: [已发布](https://github.com/microsoft/qlib/pull/205) 于 2021年1月22日 |

2021年之前发布的功能未在此列出。

<p align="center">
  <img src="docs/_static/img/logo/1.png" />
</p>

Qlib 是一个开源的、面向人工智能的量化投资平台，旨在利用 AI 技术挖掘量化投资的潜力、赋能研究并创造价值，覆盖从想法探索到生产落地的全流程。Qlib 支持多样化的机器学习建模范式，包括监督学习、市场动态建模和强化学习。

越来越多的不同范式下的 SOTA 量化研究工作/论文正在 Qlib 中发布，以协同解决量化投资中的关键挑战。例如：1）使用监督学习从丰富且异构的金融数据中挖掘市场复杂的非线性模式；2）利用自适应概念漂移技术建模金融市场的动态特性；3）通过强化学习对连续投资决策进行建模，协助投资者优化交易策略。

它包含数据处理、模型训练、回测的完整机器学习流水线（ML pipeline）；并覆盖量化投资的全链条：Alpha 挖掘、风险建模、组合优化和订单执行。更多详情，请参阅我们的论文 [《Qlib: An AI-oriented Quantitative Investment Platform》](https://arxiv.org/abs/2009.11189)。


<table>
  <tbody>
    <tr>
      <th>框架、教程、数据与开发运维</th>
      <th>量化研究中的主要挑战与解决方案</th>
    </tr>
    <tr>
      <td>
        <li><a href="#plans"><strong>规划</strong></a></li>
        <li><a href="#framework-of-qlib">Qlib 框架</a></li>
        <li><a href="#quick-start">快速入门</a></li>
          <ul dir="auto">
            <li type="circle"><a href="#installation">安装</a> </li>
            <li type="circle"><a href="#data-preparation">数据准备</a></li>
            <li type="circle"><a href="#auto-quant-research-workflow">自动量化研究工作流</a></li>
            <li type="circle"><a href="#building-customized-quant-research-workflow-by-code">通过代码构建自定义量化研究工作流</a></li></ul>
        <li><a href="#quant-dataset-zoo"><strong>量化数据集库</strong></a></li>
        <li><a href="#learning-framework">学习框架</a></li>
        <li><a href="#more-about-qlib">关于 Qlib 的更多信息</a></li>
        <li><a href="#offline-mode-and-online-mode">离线模式与在线模式</a>
        <ul>
          <li type="circle"><a href="#performance-of-qlib-data-server">Qlib 数据服务器的性能</a></li></ul>
        <li><a href="#related-reports">相关报道</a></li>
        <li><a href="#contact-us">联系我们</a></li>
        <li><a href="#contributing">贡献代码</a></li>
      </td>
      <td valign="baseline">
        <li><a href="#main-challenges--solutions-in-quant-research">量化研究中的主要挑战与解决方案</a>
          <ul>
            <li type="circle"><a href="#forecasting-finding-valuable-signalspatterns">预测：寻找有价值的信号/模式</a>
              <ul>
                <li type="disc"><a href="#quant-model-paper-zoo"><strong>量化模型（论文）库</strong></a>
                  <ul>
                    <li type="circle"><a href="#run-a-single-model">运行单个模型</a></li>
                    <li type="circle"><a href="#run-multiple-models">运行多个模型</a></li>
                  </ul>
                </li>
              </ul>
            </li>
          <li type="circle"><a href="#adapting-to-market-dynamics">适应市场动态</a></li>
          <li type="circle"><a href="#reinforcement-learning-modeling-continuous-decisions">强化学习：对连续决策进行建模</a></li>
          </ul>
        </li>
      </td>
    </tr>
  </tbody>
</table>

# 规划
正在开发的新功能（按预计发布时间排序）。
你对这些功能的反馈非常重要。
<!-- | Feature                        | Status      | -->
<!-- | --                      | ------    | -->

# Qlib 框架

<div style="align: center">
<img src="docs/_static/img/framework-abstract.jpg" />
</div>

Qlib 的顶层框架如上所示（用户在深入细节时，可以查阅 Qlib 设计的[详细框架](https://qlib.readthedocs.io/en/latest/introduction/introduction.html#framework)）。各组件设计为松耦合模块，每个组件均可独立使用。

Qlib 提供了强大的基础设施以支持量化研究。[数据](https://qlib.readthedocs.io/en/latest/component/data.html) 始终是其中重要的一环。
我们设计了强大的学习框架，以支持多样化的学习范式（如 [强化学习](https://qlib.readthedocs.io/en/latest/component/rl.html)、[监督学习](https://qlib.readthedocs.io/en/latest/component/workflow.html#model-section)）以及不同层面的模式（例如 [市场动态建模](https://qlib.readthedocs.io/en/latest/component/meta.html)）。
通过对市场进行建模，[交易策略](https://qlib.readthedocs.io/en/latest/component/strategy.html) 将生成可执行的交易决策。不同层级或粒度的多个交易策略和执行器可以 [嵌套在一起进行联合优化与运行](https://qlib.readthedocs.io/en/latest/component/highfreq.html)。
最后，系统将提供全面的[分析](https://qlib.readthedocs.io/en/latest/component/report.html)，并且模型可以低成本地 [在线部署服务](https://qlib.readthedocs.io/en/latest/component/online.html)。


# 快速入门

本快速入门指南旨在展示：
1. 在 _Qlib_ 中构建完整的量化研究流程并尝试你的想法非常简单。
2. 即使使用*公开数据*和*简单模型*，机器学习技术在实战量化投资中也**表现优异**。

这里有一个快速 **[演示](https://terminalizer.com/view/3f24561a4470)** 展示了如何安装 ``Qlib`` 并使用 ``qrun`` 运行 LightGBM。**但是**，请确保你已按照[说明文档](#数据准备)准备好数据。


## 安装

下表展示了 `Qlib` 支持的 Python 版本：
|               | pip 安装      | 源码安装  |        绘图支持        |
| ------------- |:---------------------:|:--------------------:|:------------------:|
| Python 3.8    | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.9    | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.10   | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.11   | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.12   | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |

**注意**: 
1. 建议使用 **Conda** 管理你的 Python 环境。在某些情况下，在 `conda` 环境外使用 Python 可能会导致头文件缺失，从而引起某些包安装失败。
2. 请注意，如果在 Python 3.6 中安装 Cython，从源码安装 ``Qlib`` 时可能会报错。如果你的机器使用 Python 3.6，建议将 Python *升级*至 3.8 或更高版本，或使用 `conda` 的 Python 环境从源码安装 ``Qlib``。

### 通过 pip 安装
你可以通过以下命令轻松使用 pip 安装 ``Qlib``。

```bash
  pip install pyqlib
```

**注意**: pip 将安装最新稳定版 qlib。然而，qlib 的主分支（main branch）仍在积极开发中。如果你想测试主分支中的最新脚本或功能，请使用以下方法安装。

### 从源码安装
此外，你还可以通过以下步骤使用源码安装最新的 dev 版本 ``Qlib``：

* 在从源码安装 ``Qlib`` 之前，你需要先安装一些依赖项：

  ```bash
  pip install numpy
  pip install --upgrade cython
  ```

* 克隆仓库并按如下方式安装 ``Qlib``。
    ```bash
    git clone https://github.com/microsoft/qlib.git && cd qlib
    pip install .  # 开发时推荐使用 `pip install -e .[dev]`，详情请参阅 docs/developer/code_standard_and_dev_guide.rst
    ```

**提示**: 如果在你的环境中无法安装 `Qlib` 或运行示例，对比你的操作步骤与 [CI 工作流](.github/workflows/test_qlib_from_source.yml) 可能有助于你定位问题。

**Mac 用户提示**: 如果你使用的是 M1 芯片的 Mac，在构建 LightGBM 的 wheel 时可能会遇到问题，这是由于缺少 OpenMP 依赖项所致。要解决此问题，请先通过 ``brew install libomp`` 安装 openmp，然后运行 ``pip install .`` 以成功构建。 

## 数据准备
❗ 由于更严格的数据安全政策，官方数据集已暂时停用。你可以尝试社区贡献的[此数据源](https://github.com/chenditc/investment_data/releases)。以下是一个下载最新数据的示例。
```bash
wget https://github.com/chenditc/investment_data/releases/latest/download/qlib_bin.tar.gz
mkdir -p ~/.qlib/qlib_data/cn_data
tar -zxvf qlib_bin.tar.gz -C ~/.qlib/qlib_data/cn_data --strip-components=1
rm -f qlib_bin.tar.gz
```

下方的官方数据集将在不久的将来恢复提供。


----

通过运行以下代码加载和准备数据：

### 通过模块获取
  ```bash
  # 获取日频(1d)数据
  python -m qlib.cli.data qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn

  # 获取分钟频(1min)数据
  python -m qlib.cli.data qlib_data --target_dir ~/.qlib/qlib_data/cn_data_1min --region cn --interval 1min

  ```

### 从源码构建

  ```bash
  # 获取日频(1d)数据
  python scripts/get_data.py qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn

  # 获取分钟频(1min)数据
  python scripts/get_data.py qlib_data --target_dir ~/.qlib/qlib_data/cn_data_1min --region cn --interval 1min

  ```

该数据集由[爬虫脚本](scripts/data_collector/)收集的公开数据创建，这些脚本已发布在同一仓库中。
你可以使用它构建相同的数据集。[数据集说明](https://github.com/microsoft/qlib/tree/main/scripts/data_collector#description-of-dataset)

***请注意***，数据来源于[Yahoo Finance](https://finance.yahoo.com/lookup)，数据可能并不完美。
如果你拥有高质量的数据集，我们建议你自行准备数据。更多信息请参阅[相关文档](https://qlib.readthedocs.io/en/latest/component/data.html#converting-csv-format-into-qlib-format)*.

### 日频数据的自动更新（来自 Yahoo Finance）
  > 如果你仅希望在历史数据上测试你的模型和策略，此步骤为*可选*。
  > 
  > 建议用户先手动更新一次数据（例如 `--trading_date 2021-05-25`），然后设置为自动更新。
  >
  > **注意**: 你无法基于 Qlib 提供的离线数据进行增量更新（部分字段已被移除以减小数据体积）。你应该使用 [yahoo collector](https://github.com/microsoft/qlib/tree/main/scripts/data_collector/yahoo#automatic-update-of-daily-frequency-datafrom-yahoo-finance) 从头下载 Yahoo 数据，然后进行增量更新。
  > 
  > 更多信息请参阅：[yahoo collector](https://github.com/microsoft/qlib/tree/main/scripts/data_collector/yahoo#automatic-update-of-daily-frequency-datafrom-yahoo-finance)

  * 每个交易日自动将数据更新至 "qlib" 目录（Linux）
      * 使用 *crontab*: `crontab -e`
      * 设置定时任务：

        ```
        * * * * 1-5 python <script path> update_data_to_bin --qlib_data_1d_dir <user data dir>
        ```
        * **脚本路径**: *scripts/data_collector/yahoo/collector.py*

  * 手动更新数据
      ```
      python scripts/data_collector/yahoo/collector.py update_data_to_bin --qlib_data_1d_dir <用户数据目录> --trading_date <开始日期> --end_date <结束日期>
      ```
      * *trading_date*: 交易日开始时间
      * *end_date*: 交易日结束时间（不包含）

### 检查数据健康状况
  * 我们提供了一个脚本来检查数据的健康状况，你可以运行以下命令来检查数据是否健康。
    ```
    python scripts/check_data_health.py check_data --qlib_dir ~/.qlib/qlib_data/cn_data
    ```
  * 当然，你也可以添加一些参数来调整测试结果，例如：
    ```
    python scripts/check_data_health.py check_data --qlib_dir ~/.qlib/qlib_data/cn_data --missing_data_num 30055 --large_step_threshold_volume 94485 --large_step_threshold_price 20
    ```
  * 如果你想了解更多关于 `check_data_health` 的信息，请参阅[文档](https://qlib.readthedocs.io/en/latest/component/data.html#checking-the-health-of-the-data)。

<!-- 
- Run the initialization code and get stock data:

  ```python
  import qlib
  from qlib.data import D
  from qlib.constant import REG_CN

  # Initialization
  mount_path = "~/.qlib/qlib_data/cn_data"  # target_dir
  qlib.init(mount_path=mount_path, region=REG_CN)

  # Get stock data by Qlib
  # Load trading calendar with the given time range and frequency
  print(D.calendar(start_time='2010-01-01', end_time='2017-12-31', freq='day')[:2])

  # Parse a given market name into a stockpool config
  instruments = D.instruments('csi500')
  print(D.list_instruments(instruments=instruments, start_time='2010-01-01', end_time='2017-12-31', as_list=True)[:6])

  # Load features of certain instruments in given time range
  instruments = ['SH600000']
  fields = ['$close', '$volume', 'Ref($close, 1)', 'Mean($close, 3)', '$high-$low']
  print(D.features(instruments, fields, start_time='2010-01-01', end_time='2017-12-31', freq='day').head())
  ```
 -->

## Docker 镜像
1. 从 Docker Hub 仓库拉取镜像
    ```bash
    docker pull pyqlib/qlib_image_stable:stable
    ```
2. 启动新的 Docker 容器
    ```bash
    docker run -it --name <container name> -v <Mounted local directory>:/app pyqlib/qlib_image_stable:stable
    ```
3. 此时你已进入 Docker 环境，可以运行 qlib 脚本。示例：
    ```bash
    >>> python scripts/get_data.py qlib_data --name qlib_data_simple --target_dir ~/.qlib/qlib_data/cn_data --interval 1d --region cn
    >>> python qlib/cli/run.py examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml
    ```
4. 退出容器
    ```bash
    >>> exit
    ```
5. 重启容器
    ```bash
    docker start -i -a <container name>
    ```
6. 停止容器
    ```bash
    docker stop <container name>
    ```
7. 删除容器
    ```bash
    docker rm <container name>
    ```
8. 如果你想了解更多详情，请参阅[文档](https://qlib.readthedocs.io/en/latest/developer/how_to_build_image.html)。

## 自动量化研究工作流
Qlib 提供了一个名为 `qrun` 的工具来自动运行整个工作流（包括构建数据集、训练模型、回测和评估）。你可以按照以下步骤启动自动量化研究工作流并根据图形化报告进行分析： 

1. 量化研究工作流：使用 LightGBM 的工作流配置 ([workflow_config_lightgbm_Alpha158.yaml](examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml)) 运行 `qrun`，如下所示。
    ```bash
      cd examples  # 避免在包含 `qlib` 的目录下运行程序
      qrun benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml
    ```
    如果你希望在调试模式下使用 `qrun`，请使用以下命令：
    ```bash
    python -m pdb qlib/cli/run.py examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml
    ```
    `qrun` 的运行结果如下所示，关于结果的更多解释请参阅[文档](https://qlib.readthedocs.io/en/latest/component/strategy.html#result)。 

    ```bash

    'The following are analysis results of the excess return without cost.'
                           risk
    mean               0.000708
    std                0.005626
    annualized_return  0.178316
    information_ratio  1.996555
    max_drawdown      -0.081806
    'The following are analysis results of the excess return with cost.'
                           risk
    mean               0.000512
    std                0.005626
    annualized_return  0.128982
    information_ratio  1.444287
    max_drawdown      -0.091078
    ```
    以下是关于 `qrun` 和[工作流](https://qlib.readthedocs.io/en/latest/component/workflow.html)的详细文档。

2. 图形化报告分析：首先，运行 `python -m pip install .[analysis]` 安装所需依赖。然后使用 `jupyter notebook` 运行 `examples/workflow_by_code.ipynb` 以获取图形化报告。 
    - 预测信号（模型预测）分析
      - 分组累计收益率 (Cumulative Return of groups)
      ![Cumulative Return](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_cumulative_return.png)
      - 收益分布 (Return distribution)
      ![long_short](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_long_short.png)
      - 信息系数 (Information Coefficient, IC)
      ![Information Coefficient](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_IC.png)
      ![Monthly IC](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_monthly_IC.png)
      ![IC](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_NDQ.png)
      - 预测信号（模型预测）自相关性 (Auto Correlation of forecasting signal)
      ![Auto Correlation](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_auto_correlation.png)

    - 组合分析 (Portfolio analysis)
      - 回测收益 (Backtest return)
      ![Report](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/report.png)
      <!-- 
      - Score IC
      ![Score IC](docs/_static/img/score_ic.png)
      - Cumulative Return
      ![Cumulative Return](docs/_static/img/cumulative_return.png)
      - Risk Analysis
      ![Risk Analysis](docs/_static/img/risk_analysis.png)
      - Rank Label
      ![Rank Label](docs/_static/img/rank_label.png)
      -->
   - 上述结果的[解释](https://qlib.readthedocs.io/en/latest/component/report.html)

## 通过代码构建自定义量化研究工作流
自动工作流可能不适合所有量化研究员的研究流程。为了支持灵活的量化研究工作流，Qlib 还提供了模块化的接口，允许研究人员通过代码构建自己的工作流。[这里](examples/workflow_by_code.ipynb) 有一个通过代码构建自定义量化研究工作流的示例。

# 量化研究中的主要挑战与解决方案
量化投资是一个非常独特的场景，有许多关键挑战需要解决。
目前，Qlib 为其中部分问题提供了一些解决方案。

## 预测：寻找有价值的信号/模式
准确预测股价走势是构建盈利组合的重要环节。
然而，金融市场中各种格式的海量数据使得构建预测模型极具挑战性。

越来越多的 SOTA 量化研究工作/论文（专注于构建预测模型以从复杂金融数据中挖掘有价值信号/模式）正在 `Qlib` 中发布


### [量化模型（论文）库](examples/benchmarks)

以下是基于 `Qlib` 构建的模型列表：
- [基于 XGBoost 的 GBDT (Tianqi Chen, et al. KDD 2016)](examples/benchmarks/XGBoost/)
- [基于 LightGBM 的 GBDT (Guolin Ke, et al. NIPS 2017)](examples/benchmarks/LightGBM/)
- [基于 Catboost 的 GBDT (Liudmila Prokhorenkova, et al. NIPS 2018)](examples/benchmarks/CatBoost/)
- [基于 pytorch 的 MLP](examples/benchmarks/MLP/)
- [基于 pytorch 的 LSTM (Sepp Hochreiter, et al. Neural computation 1997)](examples/benchmarks/LSTM/)
- [基于 pytorch 的 GRU (Kyunghyun Cho, et al. 2014)](examples/benchmarks/GRU/)
- [基于 pytorch 的 ALSTM (Yao Qin, et al. IJCAI 2017)](examples/benchmarks/ALSTM)
- [基于 pytorch 的 GATs (Petar Velickovic, et al. 2017)](examples/benchmarks/GATs/)
- [基于 pytorch 的 SFM (Liheng Zhang, et al. KDD 2017)](examples/benchmarks/SFM/)
- [基于 tensorflow 的 TFT (Bryan Lim, et al. International Journal of Forecasting 2019)](examples/benchmarks/TFT/)
- [基于 pytorch 的 TabNet (Sercan O. Arik, et al. AAAI 2019)](examples/benchmarks/TabNet/)
- [基于 LightGBM 的 DoubleEnsemble (Chuheng Zhang, et al. ICDM 2020)](examples/benchmarks/DoubleEnsemble/)
- [基于 pytorch 的 TCTS (Xueqing Wu, et al. ICML 2021)](examples/benchmarks/TCTS/)
- [基于 pytorch 的 Transformer (Ashish Vaswani, et al. NeurIPS 2017)](examples/benchmarks/Transformer/)
- [基于 pytorch 的 Localformer (Juyong Jiang, et al.)](examples/benchmarks/Localformer/)
- [基于 pytorch 的 TRA (Hengxu, Dong, et al. KDD 2021)](examples/benchmarks/TRA/)
- [基于 pytorch 的 TCN (Shaojie Bai, et al. 2018)](examples/benchmarks/TCN/)
- [基于 pytorch 的 ADARNN (YunTao Du, et al. 2021)](examples/benchmarks/ADARNN/)
- [基于 pytorch 的 ADD (Hongshun Tang, et al.2020)](examples/benchmarks/ADD/)
- [基于 pytorch 的 IGMTF (Wentao Xu, et al.2021)](examples/benchmarks/IGMTF/)
- [基于 pytorch 的 HIST (Wentao Xu, et al.2021)](examples/benchmarks/HIST/)
- [基于 pytorch 的 KRNN](examples/benchmarks/KRNN/)
- [基于 pytorch 的 Sandwich](examples/benchmarks/Sandwich/)

非常欢迎提交包含新量化模型的 Pull Request。

每个模型在 `Alpha158` 和 `Alpha360` 数据集上的表现可在此处查看：[这里](examples/benchmarks/README.md)。

### 运行单个模型
上述所有模型均可通过 ``Qlib`` 运行。用户可以通过 [benchmarks](examples/benchmarks) 文件夹找到我们提供的配置文件以及模型的详细信息。更多信息可在上述模型文件中获取。

`Qlib` 提供了三种不同的方式来运行单个模型，用户可以选择最适合自己需求的方式：
- 用户可以利用上面提到的 `qrun` 工具，基于配置文件运行模型的整个工作流。
- 用户可以基于 `examples` 文件夹中列出的[示例](examples/workflow_by_code.py)创建 `workflow_by_code` Python 脚本。

- 用户可以使用 `examples` 文件夹中的 [`run_all_model.py`](examples/run_all_model.py) 脚本来运行模型。以下是具体的 shell 命令示例：`python run_all_model.py run --models=lightgbm`，其中 `--models` 参数可以接受上述列出的任意数量的模型（可用模型可在 [benchmarks](examples/benchmarks/) 中找到）。更多用法请参阅该文件的[文档字符串](examples/run_all_model.py)。
    - **注意**: 每个基线都有不同的环境依赖，请确保你的 Python 版本符合要求（例如：由于 `tensorflow==1.15.0` 的限制，TFT 仅支持 Python 3.6~3.7）

### 运行多个模型
`Qlib` 还提供了一个脚本 [`run_all_model.py`](examples/run_all_model.py)，可以多次迭代运行多个模型。**（注意）**：该脚本目前仅支持 *Linux*。未来将支持其他操作系统。此外，它暂不支持并行运行同一模型的多次实验，这将在未来的开发中修复。）

该脚本会为每个模型创建独立的虚拟环境，并在训练结束后删除这些环境。因此，只会生成并存储实验结果，如 `IC` 和回测结果。

以下是运行所有模型 10 次迭代的示例：
```python
python run_all_model.py run 10
```

它还提供了同时运行特定模型的 API。更多用法请参阅该文件的[文档字符串](examples/run_all_model.py)。 

### 破坏性变更（Break Change）
在 `pandas` 中，`group_key` 是 `groupby` 方法的一个参数。从 `pandas` 1.5 到 2.0，`group_key` 的默认值已从“无默认”变为 `True`，这会导致 qlib 在运行时报错。因此我们将其设置为 `group_key=False`，但这不能保证某些程序能正常运行，包括：
* qlib\examples\rl_order_execution\scripts\gen_training_orders.py
* qlib\examples\benchmarks\TRA\src\dataset.MTSDatasetH.py
* qlib\examples\benchmarks\TFT\tft.py



## [适应市场动态](examples/benchmarks_dynamic)

由于金融市场环境具有非平稳性，数据分布可能会在不同时期发生变化，这会导致在训练数据上构建的模型在未来测试数据上的性能下降。
因此，使预测模型/策略适应市场动态对于其性能至关重要。

以下是基于 `Qlib` 构建的解决方案列表：
- [滚动重训练 (Rolling Retraining)](examples/benchmarks_dynamic/baseline/)
- [基于 pytorch 的 DDG-DA (Wendi, et al. AAAI 2022)](examples/benchmarks_dynamic/DDG-DA/)

## 强化学习：对连续决策进行建模
Qlib 现在支持强化学习，这是一项旨在对连续投资决策进行建模的功能。该功能通过从与环境的交互中学习以最大化累积回报的概念，协助投资者优化交易策略。

以下是按场景分类的基于 `Qlib` 构建的解决方案列表：

### [订单执行中的强化学习 (RL for order execution)](examples/rl_order_execution)
[这里](https://qlib.readthedocs.io/en/latest/component/rl/overall.html#order-execution) 是该场景的介绍。以下所有方法均在[此处](examples/rl_order_execution)进行了对比。
- [TWAP](examples/rl_order_execution/exp_configs/backtest_twap.yml)
- [PPO: "An End-to-End Optimal Trade Execution Framework based on Proximal Policy Optimization", IJCAL 2020](examples/rl_order_execution/exp_configs/backtest_ppo.yml)
- [OPDS: "Universal Trading for Order Execution with Oracle Policy Distillation", AAAI 2021](examples/rl_order_execution/exp_configs/backtest_opds.yml)

# 量化数据集库 (Quant Dataset Zoo)
数据集在量化投资中扮演着非常重要的角色。以下是基于 `Qlib` 构建的数据集列表：

| 数据集                                    | 美股市场 | A股市场 |
| --                                         | --        | --           |
| [Alpha360](./qlib/contrib/data/handler.py) |  √        |  √           |
| [Alpha158](./qlib/contrib/data/handler.py) |  √        |  √           |

[这里](https://qlib.readthedocs.io/en/latest/advanced/alpha.html) 是使用 `Qlib` 构建数据集的教程。
非常欢迎提交包含新量化数据集的 Pull Request。


# 学习框架 (Learning Framework)
Qlib 具有高度可定制性，其许多组件都是可学习的。
可学习的组件是 `Forecast Model`（预测模型）和 `Trading Agent`（交易智能体）的实例。它们基于 `Learning Framework`（学习框架）层进行训练，然后应用于 `Workflow`（工作流）层的多个场景。
学习框架也利用了 `Workflow` 层（例如共享 `Information Extractor`、基于 `Execution Env` 创建环境）。

根据学习范式，它们可分为强化学习和监督学习：
- 对于监督学习，详细文档可在此处查看 [这里](https://qlib.readthedocs.io/en/latest/component/model.html)。
- 对于强化学习，详细文档可在此处查看 [这里](https://qlib.readthedocs.io/en/latest/component/rl.html)。Qlib 的 RL 学习框架利用 `Workflow` 层中的 `Execution Env` 来创建环境。值得注意的是，也支持 `NestedExecutor`。这赋予了你联合优化不同层级策略/模型/智能体的能力（例如：为特定的组合管理策略优化订单执行策略）。


# 关于 Qlib 的更多信息 (More About Qlib)
如果你想快速浏览 qlib 中最常用的组件，你可以尝试 [这里](examples/tutorial/) 的 notebooks。

详细文档组织在 [docs](docs/) 中。
构建 HTML 格式的文档需要 [Sphinx](http://www.sphinx-doc.org) 和 readthedocs 主题。 
```bash
cd docs/
conda install sphinx sphinx_rtd_theme -y
# 或者，你也可以使用 pip 安装它们
# pip install sphinx sphinx_rtd_theme
make html
```
你也可以直接在[在线文档](http://qlib.readthedocs.io/)中查看。

Qlib 正在积极且持续开发中。我们的规划路线图作为 [GitHub 项目](https://github.com/microsoft/qlib/projects/1) 进行管理。



# 离线模式与在线模式 (Offline Mode and Online Mode)
Qlib 的数据服务器可以部署为 `Offline`（离线）模式或 `Online`（在线）模式。默认模式为离线模式。

在 `Offline`（离线）模式下，数据将本地部署。 

在 `Online`（在线）模式下，数据将以共享数据服务的形式部署。数据和缓存将由所有客户端共享。由于缓存命中率更高，数据检索性能预计会提升。同时它也会占用更少的磁盘空间。在线模式的文档可在 [Qlib-Server](https://qlib-server.readthedocs.io/) 中查看。该模式可以通过[基于 Azure CLI 的脚本](https://qlib-server.readthedocs.io/en/latest/build.html#one-click-deployment-in-azure)自动部署。在线数据服务器的源代码可在 [Qlib-Server repository](https://github.com/microsoft/qlib-server) 中找到。

## Qlib 数据服务器的性能
数据处理性能对于像 AI 技术这样的数据驱动方法至关重要。作为一个面向人工智能的平台，Qlib 提供了数据存储和处理的解决方案。为了展示 Qlib 数据服务器的性能，我们将其与几种其他数据存储方案进行了对比。 

我们通过完成相同的任务来评估几种存储方案的性能：从股票市场的基本 OHLCV 日频数据（2007年至2020年每天800只股票）构建一个数据集（14个特征/因子）。该任务涉及数据查询和处理。

|                         | HDF5      | MySQL     | MongoDB   | InfluxDB  | Qlib -E -D  | Qlib +E -D   | Qlib +E +D  |
| --                      | ------    | ------    | --------  | --------- | ----------- | ------------ | ----------- |
| 总计 (1CPU) (秒)        | 184.4±3.7 | 365.3±7.5 | 253.6±6.7 | 368.2±3.6 | 147.0±8.8   | 47.6±1.0     | **7.4±0.3** |
| 总计 (64CPU) (秒)       |           |           |           |           | 8.8±0.6     | **4.2±0.2**  |             |
* `+(-)E` 表示是否启用（未启用）`ExpressionCache`
* `+(-)D` 表示是否启用（未启用）`DatasetCache`

大多数通用数据库加载数据耗时过长。深入底层实现后，我们发现通用数据库解决方案中的数据会经过过多的接口层和不必要的格式转换。这些开销严重拖慢了数据加载速度。Qlib 的数据以紧凑格式存储，便于高效组合成数组用于科学计算。

# 相关报道 (Related Reports)
- [Guide To Qlib: Microsoft’s AI Investment Platform](https://analyticsindiamag.com/qlib/)
- [微软也搞AI量化平台？还是开源的！](https://mp.weixin.qq.com/s/47bP5YwxfTp2uTHjUBzJQQ)
- [微矿Qlib：业内首个AI量化投资开源平台](https://mp.weixin.qq.com/s/vsJv7lsgjEi-ALYUz4CvtQ)

# 联系我们 (Contact Us)
- 如果你遇到任何问题，请在此处创建 Issue [here](https://github.com/microsoft/qlib/issues/new/choose) 或在 [gitter](https://gitter.im/Microsoft/qlib) 发送消息。
- 如果你想为 `Qlib` 做出贡献，请[创建 Pull Request](https://github.com/microsoft/qlib/compare)。 
- 其他事宜，欢迎通过电子邮件联系我们 ([qlib@microsoft.com](mailto:qlib@microsoft.com))。
  - 我们正在招募新成员（包括全职员工 FTEs 和实习生），欢迎投递简历！

加入即时通讯讨论组：
|[Gitter](https://gitter.im/Microsoft/qlib)|
|----|
|![image](https://github.com/microsoft/qlib/blob/main/docs/_static/img/qrcode/gitter_qr.png)|

# 贡献代码 (Contributing)
我们感谢所有的贡献，并致谢所有贡献者！
<a href="https://github.com/microsoft/qlib/graphs/contributors"><img src="https://contrib.rocks/image?repo=microsoft/qlib" /></a>

在 2020 年 9 月将 Qlib 作为开源项目发布到 GitHub 之前，它一直是我们团队的内部项目。遗憾的是，内部的提交历史并未保留。我们团队中的许多成员也为 Qlib 做出了大量贡献，包括 Ruihua Wang、Yinda Zhang、Haisu Yu、Shuyu Wang、Bochen Pang 以及 [Dong Zhou](https://github.com/evanzd/evanzd)。特别感谢 [Dong Zhou](https://github.com/evanzd/evanzd)，因为 Qlib 的初始版本是由他开发的。

## 指导说明 (Guidance)

本项目欢迎各类贡献和建议。  
**以下是提交 Pull Request 的一些[代码规范与开发指南](docs/developer/code_standard_and_dev_guide.rst)。**

做出贡献并不难。解决一个问题（可能只是回答一个在 [issues list](https://github.com/microsoft/qlib/issues) 或 [gitter](https://gitter.im/Microsoft/qlib) 中提出的问题）、修复/提出一个 Bug、改进文档甚至修正拼写错误，都是对 Qlib 的重要贡献。

例如，如果你想为 Qlib 的文档/代码做出贡献，你可以按照下图中的步骤操作。
<p align="center">
  <img src="https://github.com/demon143/qlib/blob/main/docs/_static/img/change%20doc.gif" />
</p>

如果你不知道如何开始贡献，可以参考以下示例：
| 类型 | 示例 |
| -- | -- |
| 解决 Issue | [回答问题](https://github.com/microsoft/qlib/issues/749); [提出](https://github.com/microsoft/qlib/issues/765) 或 [修复](https://github.com/microsoft/qlib/pull/792) Bug |
| 文档 (Docs) | [改进文档质量](https://github.com/microsoft/qlib/pull/797/files) ; [修正拼写错误](https://github.com/microsoft/qlib/pull/774) | 
| 功能 (Feature) | 实现[请求的功能](https://github.com/microsoft/qlib/projects)，如[此示例](https://github.com/microsoft/qlib/pull/754); [重构接口](https://github.com/microsoft/qlib/pull/539/files) |
| 数据集 (Dataset) | [添加数据集](https://github.com/microsoft/qlib/pull/733) | 
| 模型 (Models) | [实现新模型](https://github.com/microsoft/qlib/pull/689), [贡献模型的指导说明](https://github.com/microsoft/qlib/tree/main/examples/benchmarks#contributing) |

[Good first issues](https://github.com/microsoft/qlib/labels/good%20first%20issue) 标签用于标识易于上手的贡献任务。

你可以通过运行 `rg 'TODO|FIXME' qlib` 在 Qlib 中发现一些待改进的实现。
 
如果你想成为 Qlib 的维护者之一以参与更多工作（例如协助合并 PR、分类 Issue），请通过电子邮件联系我们 ([qlib@microsoft.com](mailto:qlib@microsoft.com))。我们将很乐意协助提升你的权限。

## 许可证 (License)
大多数贡献要求你同意一份贡献者许可协议（CLA），声明你有权且确实授予我们使用你贡献的权利。详情请访问 https://cla.opensource.microsoft.com。

当你提交 Pull Request 时，一个 CLA 机器人将自动判断你是否需要提供 CLA 并适当装饰 PR（例如状态检查、评论）。只需按照机器人提供的指示操作即可。你将只需要在我们所有使用 CLA 的仓库中执行一次此操作。

本项目已采用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
更多信息请参阅 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或联系 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提出任何额外的问题或意见。