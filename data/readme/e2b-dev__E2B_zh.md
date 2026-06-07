<!-- <p align="center">
  <img width="100" src="/readme-assets/logo-circle.png" alt="e2b logo">
</p> -->

![E2B SDK Preview](/readme-assets/e2b-sdk-light.png#gh-light-mode-only)
![E2B SDK Preview](/readme-assets/e2b-sdk-dark.png#gh-dark-mode-only)

<h4 align="center">
  <a href="https://pypi.org/project/e2b/">
    <img alt="Last 1 month downloads for the Python SDK" loading="lazy" decoding="async" style="color:transparent;width:170px;height:18px" src="https://static.pepy.tech/personalized-badge/e2b?period=monthly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=PyPi%20Monthly%20Downloads">
  </a>
  <a href="https://www.npmjs.com/package/e2b">
    <img alt="Last 1 month downloads for the JavaScript SDK" loading="lazy" width="200" height="30" decoding="async" data-nimg="1"
    style="color:transparent;width:170px;height:18px" src="https://img.shields.io/npm/dm/e2b?label=NPM%20Monthly%20Downloads">
  </a>
</h4>

<!---
<img width="100%" src="/readme-assets/preview.png" alt="Cover image">
--->
## 什么是 E2B？
[E2B](https://www.e2b.dev/) 是一个开源基础设施，允许你在云端的安全隔离沙箱（sandbox）中运行 AI 生成的代码。要启动和控制沙箱，请使用我们的 [JavaScript SDK](https://www.npmjs.com/package/e2b) 或 [Python SDK](https://pypi.org/project/e2b)。

## 运行你的第一个沙箱

### 1. 安装 SDK

JavaScript / TypeScript
```
npm i e2b
```

Python
```
pip install e2b
```

### 2. 获取你的 E2B API 密钥
1. 在此处注册 E2B [here](https://e2b.dev)。
2. 在此处获取你的 API 密钥 [here](https://e2b.dev/dashboard?tab=keys)。
3. 设置包含你 API 密钥的环境变量
```
E2B_API_KEY=e2b_***
```

### 3. 启动沙箱并运行命令

JavaScript / TypeScript
```ts
import Sandbox from 'e2b'

const sandbox = await Sandbox.create()
const result = await sandbox.commands.run('echo "Hello from E2B!"')
console.log(result.stdout) // Hello from E2B!
```

Python
```py
from e2b import Sandbox

with Sandbox.create() as sandbox:
    result = sandbox.commands.run('echo "Hello from E2B!"')
    print(result.stdout)  # Hello from E2B!
```

### 4. 使用代码解释器执行代码

如需使用 [`runCode()`](https://e2b.dev/docs/code-interpreting)/[`run_code()`](https://e2b.dev/docs/code-interpreting) 执行代码，请安装 [Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter)：

```
npm i @e2b/code-interpreter  # JavaScript/TypeScript
pip install e2b-code-interpreter  # Python
```

```ts
import { Sandbox } from '@e2b/code-interpreter'

const sandbox = await Sandbox.create()
const execution = await sandbox.runCode('x = 1; x += 1; x')
console.log(execution.text)  // outputs 2
```

### 5. 查看文档
访问 [E2B 官方文档](https://e2b.dev/docs)。

### 6. E2B 示例库 (Cookbook)
访问我们的 [Cookbook](https://github.com/e2b-dev/e2b-cookbook/tree/main)，参考其中针对不同大语言模型（LLM）和 AI 框架的示例，获取更多开发灵感。

## 自托管部署

阅读 [自托管指南](https://github.com/e2b-dev/infra/blob/main/self-host.md) 了解如何自行部署 [E2B 基础设施](https://github.com/e2b-dev/infra)。该基础设施基于 Terraform 进行部署。 

支持的云服务商：
- 🟢 AWS
- 🟢 Google Cloud (GCP)
- [ ] Azure
- [ ] 通用 Linux 机器