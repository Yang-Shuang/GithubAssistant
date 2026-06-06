![hero illustration](https://github.com/vercel/ai/blob/HEAD/assets/hero.gif)

# AI SDK

[AI SDK](https://ai-sdk.dev/docs) 是一个与服务商无关的 TypeScript 工具包，旨在帮助你使用 Next.js、React、Svelte、Vue、Angular 等主流 UI 框架以及 Node.js 等运行时环境来构建 AI 驱动的应用程序和 Agent（智能体）。

如需了解更多关于如何使用 AI SDK 的信息，请参阅我们的 [API 参考文档](https://ai-sdk.dev/docs/reference) 和[完整文档](https://ai-sdk.dev/docs)。

## Installation

你需要在本地开发机器上安装 Node.js 22+ 和 npm（或其他包管理器）。

```shell
npm install ai
```

## Skill for Coding Agents

如果你使用 Claude Code 或 Cursor 等编程代理，我们强烈建议将 AI SDK 技能添加到你的代码库中：

```shell
npx skills add vercel/ai
```

## Unified Provider Architecture

AI SDK 提供了一个[统一的 API](https://ai-sdk.dev/docs/foundations/providers-and-models)，用于与 [OpenAI](https://ai-sdk.dev/providers/ai-sdk-providers/openai)、[Anthropic](https://ai-sdk.dev/providers/ai-sdk-providers/anthropic)、[Google](https://ai-sdk.dev/providers/ai-sdk-providers/google) 等模型服务商进行交互，以及[更多服务商](https://ai-sdk.dev/providers/ai-sdk-providers)。

默认情况下，AI SDK 会使用 [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) 让你开箱即用地访问所有主流服务商。只需传入任意支持模型的模型字符串即可：

```ts
const result = await generateText({
  model: 'anthropic/claude-opus-4.6', // or 'openai/gpt-5.4', 'google/gemini-3-flash', etc.
  prompt: 'Hello!',
});
```

你也可以直接使用各服务商的 SDK 包进行连接：

```shell
npm install @ai-sdk/openai @ai-sdk/anthropic @ai-sdk/google
```

```ts
import { anthropic } from '@ai-sdk/anthropic';

const result = await generateText({
  model: anthropic('claude-opus-4-6'), // or openai('gpt-5.4'), google('gemini-3-flash'), etc.
  prompt: 'Hello!',
});
```

## Usage

### Generating Text

```ts
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'openai/gpt-5.4', // use Vercel AI Gateway
  prompt: 'What is an agent?',
});
```

### Generating Structured Data

```ts
import { generateText, Output } from 'ai';
import { z } from 'zod';

const { output } = await generateText({
  model: 'openai/gpt-5.4',
  output: Output.object({
    schema: z.object({
      recipe: z.object({
        name: z.string(),
        ingredients: z.array(
          z.object({ name: z.string(), amount: z.string() }),
        ),
        steps: z.array(z.string()),
      }),
    }),
  }),
  prompt: 'Generate a lasagna recipe.',
});
```

### Agents

```ts
import { ToolLoopAgent } from 'ai';

const sandboxAgent = new ToolLoopAgent({
  model: 'openai/gpt-5.4',
  system: 'You are an agent with access to a shell environment.',
  tools: {
    shell: openai.tools.localShell({
      execute: async ({ action }) => {
        const [cmd, ...args] = action.command;
        const sandbox = await getSandbox(); // Vercel Sandbox
        const command = await sandbox.runCommand({ cmd, args });
        return { output: await command.stdout() };
      },
    }),
  },
});
```

### UI Integration

[AI SDK UI](https://ai-sdk.dev/docs/ai-sdk-ui/overview) 模块提供了一组钩子（hooks），帮助你构建聊天机器人和生成式用户界面。这些钩子与框架无关，因此可在 Next.js、React、Svelte 和 Vue 中使用。

你需要安装对应框架的包，例如：

```shell
npm install @ai-sdk/react
```

#### Agent @/agent/image-generation-agent.ts

```ts
import { openai } from '@ai-sdk/openai';
import { ToolLoopAgent, InferAgentUIMessage } from 'ai';

export const imageGenerationAgent = new ToolLoopAgent({
  model: 'openai/gpt-5.4',
  tools: {
    generateImage: openai.tools.imageGeneration({
      partialImages: 3,
    }),
  },
});

export type ImageGenerationAgentMessage = InferAgentUIMessage<
  typeof imageGenerationAgent
>;
```

#### Route (Next.js App Router) @/app/api/chat/route.ts

```tsx
import { imageGenerationAgent } from '@/agent/image-generation-agent';
import { createAgentUIStreamResponse } from 'ai';

export async function POST(req: Request) {
  const { messages } = await req.json();

  return createAgentUIStreamResponse({
    agent: imageGenerationAgent,
    messages,
  });
}
```

#### UI Component for Tool @/component/image-generation-view.tsx

```tsx
import { openai } from '@ai-sdk/openai';
import { UIToolInvocation } from 'ai';

export default function ImageGenerationView({
  invocation,
}: {
  invocation: UIToolInvocation<ReturnType<typeof openai.tools.imageGeneration>>;
}) {
  switch (invocation.state) {
    case 'input-available':
      return <div>Generating image...</div>;
    case 'output-available':
      return <img src={`data:image/png;base64,${invocation.output.result}`} />;
  }
}
```

#### Page @/app/page.tsx

```tsx
'use client';

import { ImageGenerationAgentMessage } from '@/agent/image-generation-agent';
import ImageGenerationView from '@/component/image-generation-view';
import { useChat } from '@ai-sdk/react';

export default function Page() {
  const { messages, status, sendMessage } =
    useChat<ImageGenerationAgentMessage>();

  const [input, setInput] = useState('');
  const handleSubmit = e => {
    e.preventDefault();
    sendMessage({ text: input });
    setInput('');
  };

  return (
    <div>
      {messages.map(message => (
        <div key={message.id}>
          <strong>{`${message.role}: `}</strong>
          {message.parts.map((part, index) => {
            switch (part.type) {
              case 'text':
                return <div key={index}>{part.text}</div>;
              case 'tool-generateImage':
                return <ImageGenerationView key={index} invocation={part} />;
            }
          })}
        </div>
      ))}

      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          disabled={status !== 'ready'}
        />
      </form>
    </div>
  );
}
```

## Templates

我们已构建了一系列[模板](https://ai-sdk.dev/docs/introduction#templates)，其中包含了针对不同用例、服务商和框架的 AI SDK 集成。你可以使用这些模板快速启动你的 AI 驱动应用。

## Community

AI SDK 的社区位于 [Vercel 社区](https://community.vercel.com/c/ai-sdk/62)，你可以在这里提问、分享想法，并向其他人展示你的项目。

## Contributing

我们欢迎并非常感谢对 AI SDK 的贡献。不过，在开始之前，请查阅我们的[贡献指南](https://github.com/vercel/ai/blob/main/CONTRIBUTING.md)，以确保你为 AI SDK 做出贡献的过程顺畅顺利。

## Authors

本库由 [Vercel](https://vercel.com) 和 [Next.js](https://nextjs.org) 团队创建，并得到了[开源社区](https://github.com/vercel/ai/graphs/contributors)的贡献。