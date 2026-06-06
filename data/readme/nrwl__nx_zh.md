<div align="center">

  <p>
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="images/nx-logo-light.svg">
      <img src="images/nx-logo.svg" alt="Nx Logo" width="140">
    </picture>
  </p>

  <h1 align="center">智能单体仓库 · 快速构建</h1>

  <p>
    <a href="https://www.npmjs.com/package/nx"><img src="https://img.shields.io/npm/v/nx.svg?style=for-the-badge" alt="NPM Version"></a>
    <a href="https://github.com/nrwl/nx"><img src="https://img.shields.io/github/stars/nrwl/nx?style=for-the-badge&logo=github" alt="GitHub Stars"></a>
    <a href=""><img src="https://img.shields.io/npm/l/nx.svg?style=for-the-badge" alt="License"></a>
    <a href="https://go.nx.dev/community"><img src="https://img.shields.io/discord/1143497901675401286?label=discord&style=for-the-badge" alt="Discord"></a>
    <a href="https://x.com/nxdevtools"><img src="https://img.shields.io/badge/@nxdevtools-555?style=for-the-badge&logo=x" alt="X (Twitter)"></a>
  </p>

 <br />

[**文档**](https://nx.dev/docs) &nbsp;&bull;&nbsp; [**更新日志**](https://nx.dev/changelog) &nbsp;&bull;&nbsp; [**博客**](https://nx.dev/blog) &nbsp;&bull;&nbsp; [**课程**](https://nx.dev/courses) &nbsp;&bull;&nbsp; [**YouTube**](https://youtube.com/@nxdevtools)

<br />

</div>

Nx 是一款面向 TypeScript 和多语言代码库的单体仓库（Monorepo）解决方案。基于 Rust 构建以保障性能，并通过 TypeScript 实现高度可扩展性。它会自动缓存未更改的内容，仅运行受影响的模块，并内置集成 CI 解决方案。从简单开始，随项目规模灵活扩展。

## 快速上手

访问 [Nx 快速入门文档](https://nx.dev/docs/quickstart) 即可开始使用。

## 为什么选择 Nx？

- **增量式设计** —— 在任何 npm/pnpm/yarn 工作区中运行 `npx nx init`。Nx 会自动识别你现有的 `package.json` 脚本，缓存其输出结果，并仅运行受影响的模块。无需更改现有配置即可无缝集成。
- **AI 原生工具链** —— Nx CLI 专为自主运行的 AI Agent（智能体）优化，使其能够获取所需上下文，并像人类一样高效操作。[了解更多 &raquo;](https://github.com/nrwl/nx-ai-agents-config)
- **多语言插件系统** —— 可选插件可自动发现任务、配置缓存输入/输出，并根据你实际使用的工具链生成代码。完美支持 Vite、Webpack、Jest、Vitest、ESLint、Gradle、Maven、.NET、Go 等 [更多技术](https://nx.dev/technologies)。
- **集成化 CI 解决方案** —— [将 Nx 连接到你的 CI 服务商](https://nx.dev/ci/intro/ci-with-nx)（如 GitHub Actions、GitLab、Azure 等），即可启用远程缓存、跨机器任务分发、仅运行受影响模块以及自动拆分 E2E 测试。[了解更多 &raquo;](https://nx.dev/ci/intro/ci-with-nx)
- **自愈型 CI** —— CI 流水线中的 AI Agent 可自动检测失败、分析根本原因、提出修复方案并验证。本地 Agent 通过 MCP 协议连接至 CI，自主发现并修复问题。[了解更多 &raquo;](https://nx.dev/ci/features/self-healing)

## 谁在使用 Nx？

从初创公司到财富 500 强企业都在使用。[查看我们的客户成功案例 &raquo;](https://nx.dev/customers)

## 如何参与贡献？

如果你打算提交 Bug 报告或 Pull Request（PR），请先阅读我们的 [贡献指南](https://github.com/nrwl/nx/blob/master/CONTRIBUTING.md)。

## 核心团队

| Victor Savkin                                                          | Jason Jean                                                            | Benjamin Cabanes                                                            | Jack Hsu                                                          |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| ![Victor Savkin](https://avatars1.githubusercontent.com/u/35996?s=160) | ![Jason Jean](https://avatars2.githubusercontent.com/u/8104246?s=160) | ![Benjamin Cabanes](https://avatars2.githubusercontent.com/u/3447705?s=160) | ![Jack Hsu](https://avatars0.githubusercontent.com/u/53559?s=160) |
| [vsavkin](https://github.com/vsavkin)                                  | [FrozenPandaz](https://github.com/FrozenPandaz)                       | [bcabanes](https://github.com/bcabanes)                                     | [jaysoo](https://github.com/jaysoo)                               |

| James Henry                                                              | Jon Cammisuli                                                            | Max Kless                                                            | Juri Strumpflohner                                                           |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| ![James Henry](https://avatars.githubusercontent.com/u/900523?s=160&v=4) | ![Jon Cammisuli](https://avatars2.githubusercontent.com/u/4332460?s=160) | ![Max Kless](https://avatars.githubusercontent.com/u/34165455?s=160) | ![Juri Strumpflohner](https://avatars1.githubusercontent.com/u/542458?s=160) |
| [JamesHenry](https://github.com/JamesHenry)                              | [cammisuli](https://github.com/cammisuli)                                | [MaxKless](https://github.com/MaxKless)                              | [juristr](https://github.com/juristr)                                        |

| Caleb Ukle                                                            | Steven Nance                                                           | Miroslav Jonaš                                                          | Leosvel Pérez Espinosa                                                            |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| ![Caleb Ukle](https://avatars.githubusercontent.com/u/23272162?s=160) | ![Steven Nance](https://avatars.githubusercontent.com/u/1036428?s=160) | ![Miroslav Jonaš](https://avatars.githubusercontent.com/u/881612?s=160) | ![Leosvel Pérez Espinosa](https://avatars.githubusercontent.com/u/12051310?s=160) |
| [barbados-clemens](https://github.com/barbados-clemens)               | [llwt](https://github.com/llwt)                                        | [meeroslav](https://github.com/meeroslav)                               | [leosvelperez](https://github.com/leosvelperez)                                   |

| Zachary DeRose                                                           | Craigory Coppola                                                           | Chau Tran                                                            | Nicole Oliver                                                           |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| ![Zachary DeRose](https://avatars.githubusercontent.com/u/3788405?s=160) | ![Craigory Coppola](https://avatars.githubusercontent.com/u/6933928?s=160) | ![Chau Tran](https://avatars.githubusercontent.com/u/25516557?s=160) | ![Nicole Oliver](https://avatars.githubusercontent.com/u/4440385?s=160) |
| [ZackDeRose](https://github.com/ZackDeRose)                              | [AgentEnder](https://github.com/AgentEnder)                                | [nartc](https://github.com/nartc)                                    | [nixallover](https://github.com/nixallover)                             |

| Rares Matei                                                           | Altan Stalker                                                           | Josh VanAllen                                                           | Louie Weng                                                            |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| ![Rares Matei](https://avatars.githubusercontent.com/u/5975076?s=160) | ![Altan Stalker](https://avatars.githubusercontent.com/u/6324206?s=160) | ![Josh VanAllen](https://avatars.githubusercontent.com/u/5290334?s=160) | ![Louie Weng](https://avatars.githubusercontent.com/u/56288712?s=160) |
| [rarmatei](https://github.com/rarmatei)                               | [StalkAltan](https://github.com/StalkAltan)                             | [joshvanallen](https://github.com/joshvanallen)                         | [lourw](https://github.com/lourw)                                     |