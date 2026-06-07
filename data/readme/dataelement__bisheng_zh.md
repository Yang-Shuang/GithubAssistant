**自豪地由中国团队打造，愿我们像 [Deepseek]、[黑神话：悟空] 的创作者一样，为世界带来更多奇迹与伟大。**

> 源自中国匠心，希望我们能像 [Deepseek]、[黑神话：悟空] 团队一样，给世界带来更多美好。

<img src="https://dataelem.com/bs/face.png" alt="Bisheng banner">

<p align="center">
    <a href="https://dataelem.feishu.cn/wiki/ZxW6wZAJicX4WkG0NqcWsbynde"><img src="https://img.shields.io/badge/docs-Wiki-brightgreen"></a>
    <img src="https://img.shields.io/github/license/dataelement/bisheng" alt="license"/>
    <a href=""><img src="https://img.shields.io/github/last-commit/dataelement/bisheng"></a>
    <a href="https://star-history.com/#dataelement/bisheng&Timeline"><img src="https://img.shields.io/github/stars/dataelement/bisheng?color=yellow"></a> 
</p>
<p align="center">
  <a href="./README_CN.md">简体中文</a> |
  <a href="./README.md">English</a> |
  <a href="./README_JPN.md">日本語</a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/717" target="_blank"><img src="https://trendshift.io/api/badge/repositories/717" alt="dataelement%2Fbisheng | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>
<div class="column" align="middle">
  <!-- <a href="https://bisheng.slack.com/join/shared_invite/"> -->
    <!-- <img src="https://img.shields.io/badge/Join-Slack-orange" alt="join-slack"/> -->
  </a>
  <!-- <img src="https://img.shields.io/github/license/bisheng-io/bisheng" alt="license"/> -->
  <!-- <img src="https://img.shields.io/docker/pulls/bisheng-io/bisheng" alt="docker-pull-count" /> -->
</div>


BISHENG 是一款面向企业场景的开源 LLM 应用 DevOps 平台。它已被众多行业领先机构和世界五百强企业广泛使用。

“毕昇”是活字印刷术的发明者，在推动人类知识传播方面发挥了至关重要的作用。我们希望 BISHENG 也能为智能应用的广泛落地提供强有力的支持。欢迎每一位开发者参与共建。


## Features 
1. **灵犀（Lingsight）：具备专家级水准的通用智能体**：通过 [AGL](https://github.com/dataelement/AgentGuidanceLanguage) 框架，我们将领域专家的偏好、经验和业务逻辑嵌入 AI 中，使智能体在处理任务时能够展现出“专家级的理解能力”。  
<p align="center"><img src="https://dataelem.com/bs/Linsight.png" alt="sence1"></p>   

2. **独特的 [BISHENG Workflow](https://dataelem.feishu.cn/wiki/R7HZwH5ZGiJUDrkHZXicA9pInif)**
   - 🧩 **独立且完整的应用编排框架**：支持在单一框架内执行各类任务（而同类产品通常依赖机器人调用，或为不同任务拆分 chatflow 和 workflow 模块）。
   - 🔄 **人在回路（Human in the loop）**：允许用户在流程执行过程中进行干预并提供反馈（包括多轮对话），而同类产品只能从头到尾自动运行，无法中途介入。
   - 💥 **功能强大**：支持循环、并行、批处理、条件逻辑以及所有逻辑组件的自由组合。能够轻松应对复杂场景，如多类型输入/输出、报告生成、内容审核等。
   - 🖐️ **直观易用**：在同类产品中需要专用组件才能实现的循环、并行和批处理操作，在 BISHENG 中可通过可视化“流程图”轻松完成（绘制闭环即形成循环，对齐元素即可实现并行，多选项目即可启用批处理）。
   <p align="center"><img src="https://dataelem.com/bs/bisheng_workflow.png" alt="sence0"></p>

3. <b>专为企业应用设计</b>：涵盖文档审阅、固定版式报告生成、多智能体协作、政策更新对比、工单辅助、客服辅助、会议纪要生成、简历筛选、通话记录分析、非结构化数据治理、知识挖掘、数据分析等。   
该平台支持构建<b>高度复杂的企业应用场景</b>，并提供数百个组件与数千项参数的<b>深度优化</b>。
<p align="center"><img src="https://dataelem.com/bs/chat.png" alt="sence1"></p>

4. <b>企业级特性</b>：这是应用落地的根本保障，包括安全审查、RBAC、用户组管理、按组分流量控制、SSO/LDAP 单点登录、漏洞扫描与补丁修复、高可用部署方案、监控统计等。
<p align="center"><img src="https://dataelem.com/bs/pro.png" alt="sence2"></p>

5. <b>高精度文档解析</b>：我们的高精度文档解析模型基于过去 5 年积累的海量高质量数据训练而成。内置高精度印刷文本、手写文本及生僻字识别模型，以及表格识别、版面分析与印章检测模型（原文存在重复表述，此处已优化）。支持免费私有化部署。
<p align="center"><img src="https://dataelem.com/bs/ocr.png" alt="sence3"></p>

6. **最佳实践共享社区**：开放的应用案例与最佳实践知识库，覆盖各类企业场景。

## Quick start 

安装 BISHENG 前，请确保满足以下条件：
- CPU ≥ 4 核虚拟核心
- RAM ≥ 16 GB
- Docker 19.03.9+
- Docker Compose 1.25.1+
> 推荐硬件配置：18 核虚拟核心，内存 48GB。除安装 BISHENG 外，默认还将自动部署以下第三方组件：ES、Milvus 和 OnlyOffice。

下载 BISHENG
```bash
git clone https://github.com/dataelement/bisheng.git
# Enter the installation directory
cd bisheng/docker

# If the system does not have the git command, you can download the BISHENG code as a zip file.
wget https://github.com/dataelement/bisheng/archive/refs/heads/main.zip
# Unzip and enter the installation directory
unzip main.zip && cd bisheng-main/docker
```
启动 BISHENG
```bash
docker compose -f docker-compose.yml -p bisheng up -d
```
服务启动完成后，在浏览器中访问 `http://IP:3001`。将显示登录页面，请进行用户注册。 

默认情况下，首位注册用户将成为系统管理员。 

更多安装与部署问题，请参阅：[自建部署指南](https://dataelem.feishu.cn/wiki/BSCcwKd4Yiot3IkOEC8cxGW7nPc)

## Acknowledgement 
本仓库的开发受益于以下优秀项目：[langchain](https://github.com/langchain-ai/langchain)、[langflow](https://github.com/logspace-ai/langflow)、[unstructured](https://github.com/Unstructured-IO/unstructured) 以及 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)。感谢它们的精彩贡献。

<b>感谢以下贡献者：</b>

<a href="https://github.com/dataelement/bisheng/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dataelement/bisheng" />
</a>



## Community & contact 
欢迎加入我们的讨论群

<img src="https://www.dataelem.com/nstatic/qrcode.png" alt="Wechat QR Code">


<!--
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=dataelement/bisheng&type=Date)](https://star-history.com/#dataelement/bisheng&Date)
-->