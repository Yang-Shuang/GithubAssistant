# AGENTS.md

![AGENTS.md logo](./public/og.png)

[AGENTS.md](https://agents.md) 是一种用于指导编程 Agent（coding agents）的简单、开放格式。

你可以将 AGENTS.md 视为面向 Agent 的 README：它是一个专用且可预测的位置，用于提供上下文和指令，帮助 AI 编码 Agent 在你的项目中工作。

以下是一个最小化的 AGENTS.md 文件示例：

```markdown
# Sample AGENTS.md file

## Dev environment tips
- Use `pnpm dlx turbo run where <project_name>` to jump to a package instead of scanning with `ls`.
- Run `pnpm install --filter <project_name>` to add the package to your workspace so Vite, ESLint, and TypeScript can see it.
- Use `pnpm create vite@latest <project_name> -- --template react-ts` to spin up a new React + Vite package with TypeScript checks ready.
- Check the name field inside each package's package.json to confirm the right name—skip the top-level one.

## Testing instructions
- Find the CI plan in the .github/workflows folder.
- Run `pnpm turbo run test --filter <project_name>` to run every check defined for that package.
- From the package root you can just call `pnpm test`. The commit should pass all tests before you merge.
- To focus on one step, add the Vitest pattern: `pnpm vitest run -t "<test name>"`.
- Fix any test or type errors until the whole suite is green.
- After moving files or changing imports, run `pnpm lint --filter <project_name>` to be sure ESLint and TypeScript rules still pass.
- Add or update tests for the code you change, even if nobody asked.

## PR instructions
- Title format: [<project_name>] <Title>
- Always run `pnpm lint` and `pnpm test` before committing.
```

## 网站

该仓库还包含一个托管在 https://agents.md/ 上的基础 Next.js 网站，以简洁的方式介绍了项目目标，并提供了一些示例。

### 本地运行应用
1. 安装依赖：
   ```bash
   pnpm install
   ```
2. 启动开发服务器：
   ```bash
   pnpm run dev
   ```
3. 打开浏览器并访问 http://localhost:3000