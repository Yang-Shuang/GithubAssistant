<div align="center">
  <img alt="logo" width="120" src="https://github.com/user-attachments/assets/2e2f2a58-2b28-4d11-afd1-87b65612b2de" />
  <h1>avante.nvim</h1>
</div>

<p align="center">
  <a href="https://neovim.io/" target="_blank"><img src="https://img.shields.io/static/v1?style=flat-square&label=Neovim&message=v0.10%2b&logo=neovim&labelColor=282828&logoColor=8faa80&color=414b32" alt="Neovim: v0.10+" /></a>
  <a href="https://github.com/yetone/avante.nvim/actions/workflows/lua.yaml" target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/yetone/avante.nvim/lua.yaml?style=flat-square&logo=lua&logoColor=c7c7c7&label=Lua+CI&labelColor=1E40AF&color=347D39&event=push" alt="Lua CI status" /></a>
  <a href="https://github.com/yetone/avante.nvim/actions/workflows/rust.yaml" target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/yetone/avante.nvim/rust.yaml?style=flat-square&logo=rust&logoColor=ffffff&label=Rust+CI&labelColor=BC826A&color=347D39&event=push" alt="Rust CI status" /></a>
  <a href="https://github.com/yetone/avante.nvim/actions/workflows/pre-commit.yaml" target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/yetone/avante.nvim/pre-commit.yaml?style=flat-square&logo=pre-commit&logoColor=ffffff&label=pre-commit&labelColor=FAAF3F&color=347D39&event=push" alt="pre-commit status" /></a>
  <a href="https://discord.gg/QfnEFEdSjz" target="_blank"><img src="https://img.shields.io/discord/1302530866362323016?style=flat-square&logo=discord&label=Discord&logoColor=ffffff&labelColor=7376CF&color=268165" alt="Discord" /></a>
  <a href="https://dotfyle.com/plugins/yetone/avante.nvim"><img src="https://dotfyle.com/plugins/yetone/avante.nvim/shield?style=flat-square" /></a>
</p>

**avante.nvim** 是一款旨在模拟 [Cursor](https://www.cursor.com) AI IDE 行为的 Neovim 插件。它为用户提供由 AI 驱动的代码建议，并允许你以极少的操作直接将这些推荐应用到源文件中。

[查看中文版](README_zh.md)

> [!NOTE]
>
> 🥰 本项目正处于快速迭代阶段，许多令人兴奋的功能将陆续上线。敬请期待！

<https://github.com/user-attachments/assets/510e6270-b6cf-459d-9a2f-15b397d1fe53>

<https://github.com/user-attachments/assets/86140bfd-08b4-483d-a887-1b701d9e37dd>

## 赞助 ❤️

如果你喜欢这个项目，请考虑在 Patreon 上支持我，这将帮助我继续维护和改进它：

[赞助我](https://patreon.com/yetone)

## 功能特性

- **AI 驱动的代码辅助**：与 AI 交互以询问关于当前代码文件的问题，并获得智能的改进或修改建议。
- **一键应用**：通过单个命令快速将 AI 的建议更改应用到源代码中，简化编辑流程并节省时间。
- **项目专属指令文件**：通过在项目根目录添加 Markdown 文件（默认为 `avante.md`）来自定义 AI 行为。该文件会在工作区切换时自动引用。你也可以配置自定义文件名以定制项目指令。

## Avante Zen Mode

由于 `claude code` 的普及，很明显我们已进入 Coding Agent CLI 时代。因此出现了许多类似这样的争论：在 Vibe Coding 时代，编辑器已不再需要；你只需要在终端中使用 CLI。但人们是否意识到，半个多世纪以来，基于终端的编辑器已经解决并标准化了基于终端的应用程序最大的痛点——即尴尬的 TUI（文本用户界面）交互！无论这些 Coding Agent CLIs 如何优化其 UI/UX，它们的 UI/UX 始终只是基于终端的编辑器（Vim、Emacs）的子集。它们无法实现 Vim 优雅的动作+文本对象抽象（想象一下你通常如何在 Agent CLI 中编辑大型多行提示词），也无法利用成千上万个成熟的 Vim/Neovim 插件来优化 TUI UI/UX——例如 easymotions 等。此外，当它们想要查看或修改代码时，往往不得不跳转到其他应用程序，这会强行打断 UI/UX 体验。

因此，Avante 的 Zen（禅）模式应运而生！它看起来像一个 Vibe Coding Agent CLI，但底层完全是 Neovim。这样你就可以在上面使用你熟悉的 Vim 肌肉记忆操作以及那些丰富成熟的 Neovim 插件。同时，通过利用 [ACP](https://github.com/yetone/avante.nvim#acp-support)，它具备了 claude code / gemini-cli / codex 的所有功能！何乐而不为呢？

现在你需要做的只是将此命令别名设置为 avante；这样每次你只需输入 `avante`，就像使用 claude code 一样，即可进入 Avante 的 Zen 模式！

```bash
alias avante='nvim -c "lua vim.defer_fn(function()require(\"avante.api\").zen_mode()end, 100)"'
```

效果如下：

<img alt="Avante Zen Mode" src="https://github.com/user-attachments/assets/60880f65-af55-4e4c-a565-23bb63e19251" />

## 使用 avante.md 进行项目指令

<details>

<summary>
该文件允许你向 AI 提供项目特定的上下文和指令。此文件应放置在你的项目根目录中，并在所有与 avante 的交互过程中自动引用。
</summary>

### avante.md 最佳实践

为了充分利用项目指令文件，建议遵循以下结构：

#### 你的角色

定义 AI 在你项目中的身份和专业水平：

```markdown
### your role

you are an expert senior software engineer specializing in [technology stack]. you have deep knowledge of [specific frameworks/tools] and understand best practices for [domain/industry]. you write clean, maintainable, and well-documented code. you prioritize code quality, performance, and security in all your recommendations.
```

#### 你的任务

清晰描述 AI 应该关注什么以及它应如何提供帮助：

```markdown
### your mission

your primary goal is to help build and maintain [project description]. you should:

- provide code suggestions that follow our established patterns and conventions
- help debug issues by analyzing code and suggesting solutions
- assist with refactoring to improve code quality and maintainability
- suggest optimizations for performance and scalability
- ensure all code follows our security guidelines
- help write comprehensive tests for new features
```

#### 建议添加的其他部分

- **项目上下文**：项目的简要描述、目标及目标用户
- **技术栈**：使用的技术、框架和工具列表
- **编码规范**：需遵循的具体约定、风格指南和设计模式
- **架构指南**：组件应如何交互和组织
- **测试要求**：测试策略和覆盖率预期
- **安全考量**：特定的安全要求或限制

### avante.md 示例

```markdown
# project instructions for myapp

## your role

you are an expert full-stack developer specializing in react, node.js, and typescript. you understand modern web development practices and have experience with our tech stack.

## your mission

help build a scalable e-commerce platform by:

- writing type-safe typescript code
- following react best practices and hooks patterns
- implementing restful apis with proper error handling
- ensuring responsive design with tailwind css
- writing comprehensive unit and integration tests

## project context

myapp is a modern e-commerce platform targeting small businesses. we prioritize performance, accessibility, and user experience.

## technology stack

- frontend: react 18, typescript, tailwind css, vite
- backend: node.js, express, prisma, postgresql
- testing: jest, react testing library, playwright
- deployment: docker, aws

## coding standards

- use functional components with hooks
- prefer composition over inheritance
- write self-documenting code with clear variable names
- add jsdoc comments for complex functions
- follow the existing folder structure and naming conventions
```

</details>

## 安装

如果你希望从源码构建二进制文件，则需要安装 `cargo`。否则将使用 `curl` 和 `tar` 从 GitHub 获取预编译的二进制文件。

<details open>

  <summary><a href="https://github.com/folke/lazy.nvim">lazy.nvim</a> (推荐)</summary>

```lua
{
  "yetone/avante.nvim",
  -- if you want to build from source then do `make BUILD_FROM_SOURCE=true`
  -- ⚠️ must add this setting! ! !
  build = vim.fn.has("win32") ~= 0
      and "powershell -ExecutionPolicy Bypass -File Build.ps1 -BuildFromSource false"
      or "make",
  event = "VeryLazy",
  version = false, -- Never set this value to "*"! Never!
  ---@module 'avante'
  ---@type avante.Config
  opts = {
    -- add any opts here
    -- this file can contain specific instructions for your project
    instructions_file = "avante.md",
    -- for example
    provider = "claude",
    providers = {
      claude = {
        endpoint = "https://api.anthropic.com",
        model = "claude-sonnet-4-20250514",
        timeout = 30000, -- Timeout in milliseconds
          extra_request_body = {
            temperature = 0.75,
            max_tokens = 20480,
          },
      },
      moonshot = {
        endpoint = "https://api.moonshot.ai/v1",
        model = "kimi-k2-0711-preview",
        timeout = 30000, -- Timeout in milliseconds
        extra_request_body = {
          temperature = 0.75,
          max_tokens = 32768,
        },
      },
    },
  },
  dependencies = {
    "nvim-lua/plenary.nvim",
    "MunifTanjim/nui.nvim",
    --- The below dependencies are optional,
    "nvim-mini/mini.pick", -- for file_selector provider mini.pick
    "nvim-telescope/telescope.nvim", -- for file_selector provider telescope
    "hrsh7th/nvim-cmp", -- autocompletion for avante commands and mentions
    "ibhagwan/fzf-lua", -- for file_selector provider fzf
    "stevearc/dressing.nvim", -- for input provider dressing
    "folke/snacks.nvim", -- for input provider snacks
    "nvim-tree/nvim-web-devicons", -- or echasnovski/mini.icons
    "zbirenbaum/copilot.lua", -- for providers='copilot'
    {
      -- support for image pasting
      "HakonHarnes/img-clip.nvim",
      event = "VeryLazy",
      opts = {
        -- recommended settings
        default = {
          embed_image_as_base64 = false,
          prompt_for_file_name = false,
          drag_and_drop = {
            insert_mode = true,
          },
          -- required for Windows users
          use_absolute_path = true,
        },
      },
    },
    {
      -- Make sure to set this up properly if you have lazy=true
      'MeanderingProgrammer/render-markdown.nvim',
      opts = {
        file_types = { "markdown", "Avante" },
      },
      ft = { "markdown", "Avante" },
    },
  },
}
```

</details>

<details>

  <summary><a href="https://github.com/lumen-oss/rocks.nvim">rocks.nvim</a></summary>

运行 `:Rocks install avante.nvim`，然后在你的 init.lua 中添加：

```lua
require('avante').setup()
```

</details>

<details>

  <summary>vim-plug</summary>

```vim

call plug#begin()

" Deps
Plug 'nvim-lua/plenary.nvim'
Plug 'MunifTanjim/nui.nvim'
Plug 'MeanderingProgrammer/render-markdown.nvim'

" Optional deps
Plug 'hrsh7th/nvim-cmp'
Plug 'nvim-tree/nvim-web-devicons' "or Plug 'echasnovski/mini.icons'
Plug 'HakonHarnes/img-clip.nvim'
Plug 'zbirenbaum/copilot.lua'
Plug 'stevearc/dressing.nvim' " for enhanced input UI
Plug 'folke/snacks.nvim' " for modern input UI

" Yay, pass source=true if you want to build from source
Plug 'yetone/avante.nvim', { 'branch': 'main', 'do': 'make' }

call plug#end()

autocmd! User avante.nvim
lua << EOF
require('avante').setup({})
EOF
```

</details>

<details>

  <summary><a href="https://github.com/echasnovski/mini.deps">mini.deps</a></summary>

```lua
local add, later, now = MiniDeps.add, MiniDeps.later, MiniDeps.now

add({
  source = 'yetone/avante.nvim',
  monitor = 'main',
  depends = {
    'nvim-lua/plenary.nvim',
    'MunifTanjim/nui.nvim',
    'echasnovski/mini.icons'
  },
  hooks = { post_checkout = function() vim.cmd('make') end }
})
--- optional
add({ source = 'hrsh7th/nvim-cmp' })
add({ source = 'zbirenbaum/copilot.lua' })
add({ source = 'HakonHarnes/img-clip.nvim' })
add({ source = 'MeanderingProgrammer/render-markdown.nvim' })

later(function() require('render-markdown').setup({...}) end)
later(function()
  require('img-clip').setup({...}) -- config img-clip
  require("copilot").setup({...}) -- setup copilot to your liking
  require("avante").setup({...}) -- config for avante.nvim
end)
```

</details>

<details>

  <summary><a href="https://github.com/wbthomason/packer.nvim">Packer</a></summary>

```vim

  -- Required plugins
  use 'nvim-lua/plenary.nvim'
  use 'MunifTanjim/nui.nvim'
  use 'MeanderingProgrammer/render-markdown.nvim'

  -- Optional dependencies
  use 'hrsh7th/nvim-cmp'
  use 'nvim-tree/nvim-web-devicons' -- or use 'echasnovski/mini.icons'
  use 'HakonHarnes/img-clip.nvim'
  use 'zbirenbaum/copilot.lua'
  use 'stevearc/dressing.nvim' -- for enhanced input UI
  use 'folke/snacks.nvim' -- for modern input UI

  -- Avante.nvim with build process
  use {
    'yetone/avante.nvim',
    branch = 'main',
    run = 'make',
    config = function()
      require('avante').setup()
    end
  }
```

</details>

<details>

  <summary><a href="https://github.com/nix-community/home-manager">Home Manager</a></summary>

```nix
programs.neovim = {
  plugins = [
    {
      plugin = pkgs.vimPlugins.avante-nvim;
      type = "lua";
      config = ''
              require("avante").setup()
      '' # or builtins.readFile ./plugins/avante.lua;
    }
  ];
};
```

</details>

<details>

  <summary><a href="https://nix-community.github.io/nixvim/plugins/avante/index.html">Nixvim</a></summary>

```nix
  plugins.avante.enable = true;
  plugins.avante.settings = {
    # setup options here
  };
```

</details>

<details>

  <summary>Lua</summary>

```lua
-- deps:
require('cmp').setup ({
  -- use recommended settings from above
})
require('img-clip').setup ({
  -- use recommended settings from above
})
require('copilot').setup ({
  -- use recommended settings from above
})
require('render-markdown').setup ({
  -- use recommended settings from above
})
require('avante').setup({
  -- Example: Using snacks.nvim as input provider
  input = {
    provider = "snacks", -- "native" | "dressing" | "snacks"
    provider_opts = {
      -- Snacks input configuration
      title = "Avante Input",
      icon = " ",
      placeholder = "Enter your API key...",
    },
  },
  -- Your other config here!
})
```

</details>

> [!IMPORTANT]
>
> `avante.nvim` 目前仅兼容 Neovim 0.11.0 或更高版本。请在继续操作前确保你的 Neovim 版本满足此要求。

> [!NOTE]
>
> 在同步加载插件时，建议在你的 colorscheme 之后使用 `require` 加载它。

> [!NOTE]
>
> 推荐的 **Neovim** 选项：
>
> ```lua
> -- views can only be fully collapsed with the global statusline
> vim.opt.laststatus = 3
> ```

> [!TIP]
>
> 任何支持 Markdown 的渲染插件都应该能与 Avante 配合使用，只要你添加受支持的 filetype `Avante`。更多信息请参阅 <https://github.com/yetone/avante.nvim/issues/175> 和 [此评论](https://github.com/yetone/avante.nvim/issues/175#issuecomment-2313749363)。

### 默认配置说明

_完整配置请参阅 [config.lua#L9](./lua/avante/config.lua)_

你可以直接将选项传递给 `setup()`：

```lua
require("avante").setup({
  provider = "claude",
  behaviour = {
    auto_suggestions = false,
  },
})
```

或者，在调用 `setup()` 之前在 `vim.g.avante` 中定义相同的选项：

```lua
vim.g.avante = {
  provider = "claude",
  behaviour = {
    auto_suggestions = false,
  },
}

require("avante").setup()
```

如果两者同时使用，传递给 `setup()` 的选项将覆盖 `vim.g.avante` 中的值。

<details>
<summary>默认配置</summary>

```lua
{
  ---@alias Provider "claude" | "openai" | "azure" | "gemini" | "cohere" | "copilot" | string
  ---@type Provider
  provider = "claude", -- The provider used in Aider mode or in the planning phase of Cursor Planning Mode
  ---@alias Mode "agentic" | "legacy"
  ---@type Mode
  mode = "agentic", -- The default mode for interaction. "agentic" uses tools to automatically generate code, "legacy" uses the old planning method to generate code.
  -- WARNING: Since auto-suggestions are a high-frequency operation and therefore expensive,
  -- currently designating it as `copilot` provider is dangerous because: https://github.com/yetone/avante.nvim/issues/1048
  -- Of course, you can reduce the request frequency by increasing `suggestion.debounce`.
  auto_suggestions_provider = "claude",
  providers = {
    claude = {
      endpoint = "https://api.anthropic.com",
      auth_type = "api" -- Set to "max" to sign in with Claude Pro/Max subscription
      model = "claude-3-5-sonnet-20241022",
      extra_request_body = {
        temperature = 0.75,
        max_tokens = 4096,
      },
    },
  },
  ---Specify the special dual_boost mode
  ---1. enabled: Whether to enable dual_boost mode. Default to false.
  ---2. first_provider: The first provider to generate response. Default to "openai".
  ---3. second_provider: The second provider to generate response. Default to "claude".
  ---4. prompt: The prompt to generate response based on the two reference outputs.
  ---5. timeout: Timeout in milliseconds. Default to 60000.
  ---How it works:
  --- When dual_boost is enabled, avante will generate two responses from the first_provider and second_provider respectively. Then use the response from the first_provider as provider1_output and the response from the second_provider as provider2_output. Finally, avante will generate a response based on the prompt and the two reference outputs, with the default Provider as normal.
  ---Note: This is an experimental feature and may not work as expected.
  dual_boost = {
    enabled = false,
    first_provider = "openai",
    second_provider = "claude",
    prompt = "Based on the two reference outputs below, generate a response that incorporates elements from both but reflects your own judgment and unique perspective. Do not provide any explanation, just give the response directly. Reference Output 1: [{{provider1_output}}], Reference Output 2: [{{provider2_output}}]",
    timeout = 60000, -- Timeout in milliseconds
  },
  behaviour = {
    auto_suggestions = false, -- Experimental stage
    auto_set_highlight_group = true,
    auto_set_keymaps = true,
    auto_apply_diff_after_generation = false,
    support_paste_from_clipboard = false,
    minimize_diff = true, -- Whether to remove unchanged lines when applying a code block
    enable_token_counting = true, -- Whether to enable token counting. Default to true.
    auto_add_current_file = true, -- Whether to automatically add the current file when opening a new chat. Default to true.
    auto_approve_tool_permissions = true, -- Default: auto-approve all tools (no prompts)
    -- Examples:
    -- auto_approve_tool_permissions = false,                -- Show permission prompts for all tools
    -- auto_approve_tool_permissions = {"bash", "str_replace"}, -- Auto-approve specific tools only
    ---@type "popup" | "inline_buttons"
    confirmation_ui_style = "inline_buttons",
    --- Whether to automatically open files and navigate to lines when ACP agent makes edits
    ---@type boolean
    acp_follow_agent_locations = true,
  },
  prompt_logger = { -- logs prompts to disk (timestamped, for replay/debugging)
    enabled = true, -- toggle logging entirely
    log_dir = vim.fn.stdpath("cache") .. "/avante_prompts", -- directory where logs are saved
    fortune_cookie_on_success = false, -- shows a random fortune after each logged prompt (requires `fortune` installed)
    next_prompt = {
      normal = "<C-n>", -- load the next (newer) prompt log in normal mode
      insert = "<C-n>",
    },
    prev_prompt = {
      normal = "<C-p>", -- load the previous (older) prompt log in normal mode
      insert = "<C-p>",
    },
  },
  mappings = {
    --- @class AvanteConflictMappings
    diff = {
      ours = "co",
      theirs = "ct",
      all_theirs = "ca",
      both = "cb",
      cursor = "cc",
      next = "]x",
      prev = "[x",
    },
    suggestion = {
      accept = "<M-l>",
      next = "<M-]>",
      prev = "<M-[>",
      dismiss = "<C-]>",
    },
    jump = {
      next = "]]",
      prev = "[[",
    },
    submit = {
      normal = "<CR>",
      insert = "<C-s>",
    },
    cancel = {
      normal = { "<C-c>", "<Esc>", "q" },
      insert = { "<C-c>" },
    },
    sidebar = {
      apply_all = "A",
      apply_cursor = "a",
      retry_user_request = "r",
      edit_user_request = "e",
      switch_windows = "<Tab>",
      reverse_switch_windows = "<S-Tab>",
      remove_file = "d",
      add_file = "@",
      close = { "<Esc>", "q" },
      close_from_input = nil, -- e.g., { normal = "<Esc>", insert = "<C-d>" }
    },
  },
  selection = {
    enabled = true,
    hint_display = "delayed",
  },
  windows = {
    ---@type "right" | "left" | "top" | "bottom"
    position = "right", -- the position of the sidebar
    wrap = true, -- similar to vim.o.wrap
    width = 30, -- default % based on available width
    sidebar_header = {
      enabled = true, -- true, false to enable/disable the header
      align = "center", -- left, center, right for title
      rounded = true,
    },
    spinner = {
      editing = { "⡀", "⠄", "⠂", "⠁", "⠈", "⠐", "⠠", "⢀", "⣀", "⢄", "⢂", "⢁", "⢈", "⢐", "⢠", "⣠", "⢤", "⢢", "⢡", "⢨", "⢰", "⣰", "⢴", "⢲", "⢱", "⢸", "⣸", "⢼", "⢺", "⢹", "⣹", "⢽", "⢻", "⣻", "⢿", "⣿" },
      generating = { "·", "✢", "✳", "∗", "✻", "✽" }, -- Spinner characters for the 'generating' state
      thinking = { "🤯", "🙄" }, -- Spinner characters for the 'thinking' state
    },
    input = {
      prefix = "> ",
      height = 8, -- Height of the input window in vertical layout
    },
    edit = {
      border = "rounded",
      start_insert = true, -- Start insert mode when opening the edit window
    },
    ask = {
      floating = false, -- Open the 'AvanteAsk' prompt in a floating window
      start_insert = true, -- Start insert mode when opening the ask window
      border = "rounded",
      ---@type "ours" | "theirs"
      focus_on_apply = "ours", -- which diff to focus after applying
    },
  },
  highlights = {
    ---@type AvanteConflictHighlights
    diff = {
      current = "DiffText",
      incoming = "DiffAdd",
    },
  },
  --- @class AvanteConflictUserConfig
  diff = {
    autojump = true,
    ---@type string | fun(): any
    list_opener = "copen",
    --- Override the 'timeoutlen' setting while hovering over a diff (see :help timeoutlen).
    --- Helps to avoid entering operator-pending mode with diff mappings starting with `c`.
    --- Disable by setting to -1.
    override_timeoutlen = 500,
  },
  suggestion = {
    debounce = 600,
    throttle = 600,
  },
}
```

</details>

## Blink.cmp 用户配置

对于使用 Blink.cmp（nvim-cmp 替代品）的用户，请查看下方的配置说明。这是通过模拟 nvim-cmp 使用 blink.compat 实现的，或者你也可以直接使用 [Kaiser-Yang/blink-cmp-avante](https://github.com/Kaiser-Yang/blink-cmp-avante)。

<details>
  <summary>Lua</summary>

```lua
      selector = {
        --- @alias avante.SelectorProvider "native" | "fzf_lua" | "mini_pick" | "snacks" | "telescope" | fun(selector: avante.ui.Selector): nil
        --- @type avante.SelectorProvider
        provider = "fzf",
        -- Options override for custom providers
        provider_opts = {},
      }
```

要创建自定义的选择器提供者，你可以指定一个自定义函数来启动选择器并传递选中的项目到 `on_select` 回调中。

```lua
      selector = {
        ---@param selector avante.ui.Selector
        provider = function(selector)
          local items = selector.items ---@type avante.ui.SelectorItem[]
          local title = selector.title ---@type string
          local on_select = selector.on_select ---@type fun(selected_item_ids: string[]|nil): nil

          --- your customized picker logic here
        end,
      }
```

### 输入提供者配置

Avante.nvim 支持多种用户输入的输入提供者（如 API Key 输入）。你可以配置要使用的提供者：

<details>
  <summary>原生输入提供者 (默认)</summary>

```lua
{
  input = {
    provider = "native", -- Uses vim.ui.input
    provider_opts = {},
  }
}
```

</details>

<details>
  <summary>Dressing.nvim 输入提供者</summary>

使用增强型输入 UI，提供更好的样式和功能：

```lua
{
  input = {
    provider = "dressing",
    provider_opts = {},
  }
}
```

你需要安装 dressing.nvim：

```lua
-- With lazy.nvim
{ "stevearc/dressing.nvim" }
```

</details>

<details>
  <summary>Snacks.nvim 输入提供者 (推荐)</summary>

使用现代化、功能丰富的输入 UI：

```lua
{
  input = {
    provider = "snacks",
    provider_opts = {
      -- Additional snacks.input options
      title = "Avante Input",
      icon = " ",
    },
  }
}
```

你需要安装 snacks.nvim：

```lua
-- With lazy.nvim
{ "folke/snacks.nvim" }
```

</details>

<details>
  <summary>自定义输入提供者</summary>

要创建自定义的输入提供者，你可以指定一个函数：

```lua
{
  input = {
    ---@param input avante.ui.Input
    provider = function(input)
      local title = input.title ---@type string
      local default = input.default ---@type string
      local conceal = input.conceal ---@type boolean
      local on_submit = input.on_submit ---@type fun(result: string|nil): nil

      --- your customized input logic here
    end,
  }
}
```

</details>

选择除原生以外的其他选择器，因为目前原生的存在一些问题。对于 lazyvim 用户，请从官网复制完整的 blink.cmp 配置或扩展选项：

```lua
      compat = {
        "avante_commands",
        "avante_mentions",
        "avante_files",
      }
```

对于其他用户，只需添加自定义提供者即可。

### 可用的补全来源

Avante.nvim 提供了几个可以与 blink.cmp 集成的补全来源：

#### 提及 (`@` 触发)

提及功能允许你快速引用特定功能或将文件添加到聊天上下文中：

- `@codebase` - 启用项目上下文和仓库映射
- `@diagnostics` - 启用诊断信息
- `@file` - 打开文件选择器以将文件添加到聊天上下文
- `@quickfix` - 将 quickfix 列表中的文件添加到聊天上下文
- `@buffers` - 将打开的缓冲区添加到聊天上下文

#### 斜杠命令 (`/` 触发)

内置的常用操作斜杠命令：

- `/help` - 显示可用命令的帮助信息
- `/init` - 基于当前项目初始化 AGENTS.md
- `/clear` - 清除聊天记录
- `/new` - 开始新的聊天
- `/compact` - 压缩历史消息以节省 token
- `/lines <start>-<end> <question>` - 询问特定行的内容
- `/commit` - 为更改生成提交信息

#### 快捷方式 (`#` 触发)

快捷方式提供对预定义提示模板的快速访问。你可以在配置中自定义这些：

```lua
{
  shortcuts = {
    {
      name = "refactor",
      description = "Refactor code with best practices",
      details = "Automatically refactor code to improve readability, maintainability, and follow best practices while preserving functionality",
      prompt = "Please refactor this code following best practices, improving readability and maintainability while preserving functionality."
    },
    {
      name = "test",
      description = "Generate unit tests",
      details = "Create comprehensive unit tests covering edge cases, error scenarios, and various input conditions",
      prompt = "Please generate comprehensive unit tests for this code, covering edge cases and error scenarios."
    },
    -- Add more custom shortcuts...
  }
}
```

当你在输入中键入 `#refactor` 时，它会自动替换为相应的提示文本。

### 配置示例

以下是包含所有 Avante 来源的完整 blink.cmp 配置示例：

```lua
      default = {
        ...
        "avante_commands",
        "avante_mentions",
        "avante_shortcuts",
        "avante_files",
      }
```

```lua
      providers = {
        avante_commands = {
          name = "avante_commands",
          module = "blink.compat.source",
          score_offset = 90, -- show at a higher priority than lsp
          opts = {},
        },
        avante_files = {
          name = "avante_files",
          module = "blink.compat.source",
          score_offset = 100, -- show at a higher priority than lsp
          opts = {},
        },
        avante_mentions = {
          name = "avante_mentions",
          module = "blink.compat.source",
          score_offset = 1000, -- show at a higher priority than lsp
          opts = {},
        },
        avante_shortcuts = {
          name = "avante_shortcuts",
          module = "blink.compat.source",
          score_offset = 1000, -- show at a higher priority than lsp
          opts = {},
        }
        ...
    }
```

</details>

## 使用方法

### 使用 Claude Pro/Max 订阅
要使用你的 Claude 订阅登录，请将配置中 Claude 提供者的 **auth_type** 设置为 "max"，重新打开 Neovim，浏览器中将开始身份验证流程。登录并授权后，会出现一个代码需要复制到 Neovim 的提示框中，之后即可在 Avante 中使用你的订阅。

如果你之前选择了其他提供者，可能需要运行 `AvanteSwitchProvider claude` 来启动身份验证流程。

```lua
-- Providers = { ...

  claude = {
    -- ...
    auth_type = "max",
  },

```

### 基本功能

鉴于该项目仍处于早期阶段，`avante.nvim` 目前支持以下基本功能：

> [!IMPORTANT]
>
> 为了在不同 Neovim 会话之间保持一致性，建议在你的 shell 配置文件中设置环境变量。
> 默认情况下，`Avante` 会在启动时提示你输入所选提供者的 API Key。
>
> **作用域 API Key（推荐用于隔离）**
>
> Avante 现在支持作用域 API Key，允许你将 API Key 专门隔离给 Avante 使用，而不影响其他应用程序。只需在任何 API Key 前加上 `AVANTE_` 前缀即可：
>
> ```sh
> # Scoped keys (recommended)
> export AVANTE_ANTHROPIC_API_KEY=your-claude-api-key
> export AVANTE_OPENAI_API_KEY=your-openai-api-key
> export AVANTE_AZURE_OPENAI_API_KEY=your-azure-api-key
> export AVANTE_GEMINI_API_KEY=your-gemini-api-key
> export AVANTE_CO_API_KEY=your-cohere-api-key
> export AVANTE_AIHUBMIX_API_KEY=your-aihubmix-api-key
> export AVANTE_MOONSHOT_API_KEY=your-moonshot-api-key
> ```
>
> **全局 API Key（旧版）**
>
> 如果你仍偏好使用传统的全局 API Key，也可以继续使用：
>
> 对于 Claude：
>
> ```sh
> export ANTHROPIC_API_KEY=your-api-key
> ```
>
> 对于 OpenAI：
>
> ```sh
> export OPENAI_API_KEY=your-api-key
> ```
>
> 对于 Azure OpenAI：
>
> ```sh
> export AZURE_OPENAI_API_KEY=your-azure-api-key
> ```
>
> 对于 Amazon Bedrock：
>
> 你可以指定 `BEDROCK_KEYS` 环境变量来设置凭据。当未指定此变量时，bedrock 将使用默认的 AWS 凭证链（见下文）。
>
> ```sh
> export BEDROCK_KEYS=aws_access_key_id,aws_secret_access_key,aws_region[,aws_session_token]
> ```
>
> 注意：`aws_session_token` 是可选的，仅在使用临时 AWS 凭据时需要。
>
> 或者 Bedrock 会尝试使用 [默认凭证提供程序链](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-authentication.html) 解析 AWS 凭据。这意味着你可以配置例如通过 AWS CLI、存储在 ~/.aws/profile、使用 AWS SSO 等凭据。在这种情况下，`aws_region` 和可选的 `aws_profile` 应通过 bedrock 配置指定，例如：
>
> ```lua
> bedrock = {
>   model = "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
>   aws_profile = "bedrock",
>   aws_region = "us-east-1",
> },
> ```
>
> 注意：Bedrock 要求你的系统上已安装 [AWS CLI](https://aws.amazon.com/cli/)。

1. 在 Neovim 中打开一个代码文件。
2. 使用 `:AvanteAsk` 命令向 AI 询问关于该代码的问题。
3. 查看 AI 的建议。
4. 通过简单的命令或快捷键将推荐的更改直接应用到你的代码中。

**注意**：该插件仍在积极开发中，其功能和界面可能会发生重大变化。随着项目的演进，请预期会出现一些粗糙之处和不稳定性。

## 按键绑定

以下按键绑定可用于 `avante.nvim`：

| 按键绑定                                  | 描述                             |
| ----------------------------------------- | -------------------------------- |
| **侧边栏**                                |                                  |
| <kbd>]</kbd><kbd>p</kbd>                  | 下一个提示                         |
| <kbd>[</kbd><kbd>p</kbd>                  | 上一个提示                         |
| <kbd>A</kbd>                              | 应用全部                           |
| <kbd>a</kbd>                              | 应用光标处                         |
| <kbd>r</kbd>                              | 重试用户请求                       |
| <kbd>e</kbd>                              | 编辑用户请求                       |
| <kbd>&lt;Tab&gt;</kbd>                    | 切换窗口                           |
| <kbd>&lt;S-Tab&gt;</kbd>                  | 反向切换窗口                       |
| <kbd>d</kbd>                              | 移除文件                           |
| <kbd>@</kbd>                              | 添加文件                           |
| <kbd>q</kbd>                              | 关闭侧边栏                         |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>a</kbd> | 显示侧边栏                         |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>t</kbd> | 切换侧边栏可见性                   |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>r</kbd> | 刷新侧边栏                         |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>f</kbd> | 切换侧边栏焦点                     |
| **建议**                                  |                                  |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>?</kbd> | 选择模型                           |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>n</kbd> | 新建询问                           |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>e</kbd> | 编辑选中代码块                     |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>S</kbd> | 停止当前 AI 请求                   |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>h</kbd> | 在聊天历史之间选择                 |
| <kbd>&lt;M-l&gt;</kbd>                    | 接受建议                           |
| <kbd>&lt;M-]&gt;</kbd>                    | 下一个建议                         |
| <kbd>&lt;M-[&gt;</kbd>                    | 上一个建议                         |
| <kbd>&lt;C-]&gt;</kbd>                    | 取消建议                           |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>d</kbd> | 切换调试模式                       |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>s</kbd> | 切换建议显示                       |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>R</kbd> | 切换 repomap                       |
| **文件**                                  |                                  |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>c</kbd> | 将当前缓冲区添加到选中文件         |
| <kbd>Leader</kbd><kbd>a</kbd><kbd>B</kbd> | 将所有缓冲区文件添加到选中文件     |
| **Diff**                                  |                                  |
| <kbd>c</kbd><kbd>o</kbd>                  | 选择我们的                         |
| <kbd>c</kbd><kbd>t</kbd>                  | 选择他们的                         |
| <kbd>c</kbd><kbd>a</kbd>                  | 全选 theirs                        |
| <kbd>c</kbd><kbd>b</kbd>                  | 两者都选                           |
| <kbd>c</kbd><kbd>c</kbd>                  | 选择光标处                         |
| <kbd>]</kbd><kbd>x</kbd>                  | 移动到下一个冲突                   |
| <kbd>[</kbd><kbd>x</kbd>                  | 移动到上一个冲突                   |
| **确认**                                  |                                  |
| <kbd>Ctrl</kbd><kbd>w</kbd><kbd>f</kbd>   | 聚焦确认窗口                       |
| <kbd>c</kbd>                              | 确认代码                           |
| <kbd>r</kbd>                              | 确认响应                           |
| <kbd>i</kbd>                              | 确认输入                           |

> [!NOTE]
>
> 如果你使用的是 `lazy.nvim`，那么这里所有的按键映射都会安全设置，这意味着如果 `<leader>aa` 已经被绑定，avante.nvim 将不会覆盖该映射。在这种情况下，用户需要自行负责设置。更多详情请参阅 [关于按键绑定的说明](https://github.com/yetone/avante.nvim/wiki#keymaps-and-api-i-guess)。

### Neotree 快捷键

在 neotree 侧边栏中，你还可以添加一个新的键盘快捷键以快速将 `文件/文件夹` 添加到 `Avante Selected Files`。

<details>
<summary>Neotree 配置</summary>

```lua
return {
  {
    'nvim-neo-tree/neo-tree.nvim',
    config = function()
      require('neo-tree').setup({
        filesystem = {
          commands = {
            avante_add_files = function(state)
              local node = state.tree:get_node()
              local filepath = node:get_id()
              local relative_path = require('avante.utils').relative_path(filepath)

              local sidebar = require('avante').get()

              local open = sidebar:is_open()
              -- ensure avante sidebar is open
              if not open then
                require('avante.api').ask()
                sidebar = require('avante').get()
              end

              sidebar.file_selector:add_selected_file(relative_path)

              -- remove neo tree buffer
              if not open then
                sidebar.file_selector:remove_selected_file('neo-tree filesystem [1]')
              end
            end,
          },
          window = {
            mappings = {
              ['oa'] = 'avante_add_files',
            },
          },
        },
      })
    end,
  },
}
```

</details>

## 命令

| 命令                                   | 描述                                                                                                 | 示例                                            |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `:AvanteAsk [question] [position]`     | 向 AI 询问你的代码。可选的 `position` 设置窗口位置，`ask` 启用/禁用直接询问模式                       | `:AvanteAsk position=right Refactor this code here` |
| `:AvanteBuild`                         | 构建项目依赖                                                                                         |                                                 |
| `:AvanteChat`                          | 开始与 AI 关于你的代码库的聊天会话。默认为 `ask`=false                                               |                                                 |
| `:AvanteChatNew`                       | 开始新的聊天会话。当前聊天可以通过聊天选择器重新打开                                                 |                                                 |
| `:AvanteHistory`                       | 打开一个选择器以查看你之前的聊天会话                                                                 |                                                 |
| `:AvanteClear`                         | 清除当前聊天会话的聊天记录                                                                           |                                                 |
| `:AvanteEdit`                          | 编辑选中的代码块                                                                                     |                                                 |
| `:AvanteFocus`                         | 切换焦点到/从侧边栏                                                                                  |                                                 |
| `:AvanteRefresh`                       | 刷新所有 Avante 窗口                                                                                 |                                                 |
| `:AvanteStop`                          | 停止当前 AI 请求                                                                                     |                                                 |
| `:AvanteSwitchProvider`                | 切换 AI 提供者（例如 openai）                                                                        |                                                 |
| `:AvanteShowRepoMap`                   | 显示项目结构的仓库映射                                                                               |                                                 |
| `:AvanteToggle`                        | 切换 Avante 侧边栏                                                                                   |                                                 |
| `:AvanteModels`                        | 显示模型列表                                                                                         |                                                 |
| `:AvanteSwitchSelectorProvider`        | 切换 avante 选择器提供者（例如 native, telescope, fzf_lua, mini_pick, snacks）                       |                                                 |

## 高亮组

| 高亮组                    | 描述                     | 备注                                        |
| ------------------------- | ------------------------ | ------------------------------------------- |
| AvanteTitle               | 标题                     |                                             |
| AvanteReversedTitle       | 用于圆角边框             |                                             |
| AvanteSubtitle            | 选中代码标题             |                                             |
| AvanteReversedSubtitle    | 用于圆角边框             |                                             |
| AvanteThirdTitle          | 提示标题                 |                                             |
| AvanteReversedThirdTitle  | 用于圆角边框             |                                             |
| AvanteConflictCurrent     | 当前冲突高亮             | 默认为 `Config.highlights.diff.current`     |
| AvanteConflictIncoming    | 传入冲突高亮             | 默认为 `Config.highlights.diff.incoming`    |
| AvanteConflictCurrentLabel      | 当前冲突标签高亮         | 默认为 `AvanteConflictCurrent` 的色调       |
| AvanteConflictIncomingLabel   | 传入冲突标签高亮         | 默认为 `AvanteConflictIncoming` 的色调      |
| AvantePopupHint           | 弹出菜单中的使用提示     |                                             |
| AvanteInlineHint          | 可视模式下显示的行尾提示 |                                             |
| AvantePromptInput         | 提示输入的主体高亮       |                                             |
| AvantePromptInputBorder   | 提示输入的边框高亮       | 默认为 `NormalFloat`                        |

更多信息请参阅 [highlights.lua](./lua/avante/highlights.lua)

## Fast Apply（快速应用）

Fast Apply 是一项通过利用专用模型实现即时代码编辑且高精度的功能。它复制了 Cursor 的即时应用功能，允许无缝的代码修改，而不会带来传统代码生成通常关联的延迟。

### 目的与优势

Fast Apply 解决了 AI 辅助开发中代码应用缓慢的常见痛点。与其等待完整的语言模型处理并应用更改，Fast Apply 使用专用的“应用模型”可以快速且准确地合并代码编辑，准确率达到 96-98%，速度可达每秒 2500-4500+ token。

主要优势：

- **即时应用**：代码更改立即应用，无明显延迟
- **高精度**：专用模型在代码编辑方面达到 96-98% 的准确率
- **无缝工作流**：保持自然开发流程而不中断
- **大上下文支持**：支持高达 16k token 的输入和输出

### 配置

要启用 Fast Apply，你需要：

1. **在配置中启用 Fast Apply**：

   ```lua
     behaviour = {
       enable_fastapply = true,  -- Enable Fast Apply feature
     },
     -- ... other configuration
   ```

2. **获取你的 Morph API Key**：
   前往 [morphllm.com](https://morphllm.com/api-keys) 创建账户并获取 API Key。

3. **设置你的 Morph API Key**：

   ```bash
   export MORPH_API_KEY="your-api-key"
   ```

4. **更改 Morph 模型**：
   ```lua
   providers = {
     morph = {
       model = "morph-v3-large",
     },
   }
   ```

### 模型选项

Morph 提供了针对不同用例优化的不同模型：

| 模型               | 速度             | 准确率 | 上下文限制    |
| ------------------ | ---------------- | ------ | ------------- |
| `morph-v3-fast`    | 4500+ tok/sec    | 96%    | 16k tokens    |
| `morph-v3-large`   | 2500+ tok/sec    | 98%    | 16k tokens    |
| `auto`             | 2500-4500 tok/sec| 98%    | 16k tokens    |

### 工作原理

当启用 Fast Apply 并配置了 Morph 提供者时，avante.nvim 将：

1. 使用 `edit_file` 工具进行代码修改，而不是传统工具
2. 将原始代码、编辑指令和更新片段发送到 Morph API
3. 从专用应用模型接收完全合并的代码
4. 以高精度直接将更改应用到你的文件

该过程使用一种专用的提示格式，包括：

- `<instructions>`：清晰的更改说明
- `<code>`：原始代码内容
- `<update>`：使用截断标记（`// ... existing code ...`）的具体更改

这种方法确保应用模型可以快速准确地合并你的更改，而无需完整代码生成的开销。

## Ollama

Ollama 是 avante.nvim 的一等提供者。要开始使用它，你需要在配置中设置 `provider = "ollama"`，并在 `ollama` 中将 `model` 字段设置为你想要使用的模型。Ollama 默认禁用，你需要为其提供 `is_env_set` 方法的实现以正确启用它。例如：

```lua
provider = "ollama",
providers = {
  ollama = {
    model = "qwq:32b",
    is_env_set = require("avante.providers.ollama").check_endpoint_alive,
  },
}
```

## ACP 支持

Avante.nvim 现在支持 [Agent Client Protocol (ACP)](https://agentclientprotocol.com/overview/introduction)，能够与遵循此标准化通信协议的 AI 代理无缝集成。ACP 为 AI 代理与开发环境的交互提供了统一的方式，增强了代码编辑、文件操作和工具执行的能力。

### ACP 是什么？

Agent Client Protocol（ACP）是一种标准化的协议，使 AI 代理能够与开发工具和环境进行通信。它提供：

- **标准化通信**：基于 JSON-RPC 的统一协议用于代理-客户端交互
- **工具集成**：支持各种开发工具，如文件操作、代码执行和搜索
- **会话管理**：跨交互保持上下文的持久会话
- **权限系统**：对代理可访问和修改的内容进行细粒度控制

### 启用 ACP

要与 Avante.nvim 一起使用兼容 ACP 的代理，你需要配置一个 ACP 提供者。以下是当前支持的 ACP 代理：

#### Gemini CLI with ACP
```lua
{
  provider = "gemini-cli",
  -- other configuration options...
}
```

#### Claude Code with ACP
```lua
{
  provider = "claude-code",
  -- other configuration options...
}
```

#### Goose with ACP
```lua
{
  provider = "goose",
  -- other configuration options...
}
```

#### Codex with ACP
```lua
{
  provider = "codex",
  -- other configuration options...
}
```

#### Kimi CLI with ACP
```lua
{
  provider = "kimi-cli",
  -- other configuration options...
}
```

### ACP 配置

ACP 提供者在配置的 `acp_providers` 部分中进行配置：

```lua
{
  acp_providers = {
    ["gemini-cli"] = {
      command = "gemini",
      args = { "--experimental-acp" },
      env = {
        NODE_NO_WARNINGS = "1",
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY"),
      },
    },
    ["claude-code"] = {
      command = "claude-agent-acp",
      args = { },
      env = {
        NODE_NO_WARNINGS = "1",
        ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY"),
      },
    },
    ["goose"] = {
      command = "goose",
      args = { "acp" },
    },
    ["codex"] = {
      command = "codex-acp",
      args = {},
      env = {
        NODE_NO_WARNINGS = "1",
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY"),
      },
    },
  },
  -- other configuration options...
}
```

### 先决条件

在使用 ACP 代理之前，请确保已安装所需的工具：

- **对于 Gemini CLI**：安装 `gemini` CLI 工具并设置你的 `GEMINI_API_KEY`
- **对于 Claude Code**：通过 npm 安装 `acp-claude-code` 包并设置你的 `ANTHROPIC_API_KEY`

### ACP vs 传统提供者

ACP 提供器相比传统的基于 API 的提供器具有多项优势：

- **增强的工具访问**：代理可以直接与文件系统交互、运行命令和访问开发工具
- **持久上下文**：会话在多次交互中保持状态
- **细粒度权限**：精确控制代理可以访问和修改的内容
- **标准化协议**：兼容任何符合 ACP 的代理

## 自定义提供者

Avante 提供了一组默认提供者，但用户也可以创建自己的提供者。

更多信息请参阅 [Custom Providers](https://github.com/yetone/avante.nvim/wiki/Custom-providers)

## RAG 服务

Avante 提供了一个 RAG（检索增强生成）服务，这是一个用于获取 AI 生成代码所需上下文的工具。默认情况下未启用。你可以通过以下方式启用它：

```lua
  rag_service = { -- RAG Service configuration
    enabled = false, -- Enables the RAG service
    host_mount = os.getenv("HOME"), -- Host mount path for the rag service (Docker will mount this path)
    runner = "docker", -- Runner for the RAG service (can use docker or nix)
    llm = { -- Language Model (LLM) configuration for RAG service
      provider = "openai", -- LLM provider
      endpoint = "https://api.openai.com/v1", -- LLM API endpoint
      api_key = "OPENAI_API_KEY", -- Environment variable name for the LLM API key
      model = "gpt-4o-mini", -- LLM model name
      extra = nil, -- Additional configuration options for LLM
    },
    embed = { -- Embedding model configuration for RAG service
      provider = "openai", -- Embedding provider
      endpoint = "https://api.openai.com/v1", -- Embedding API endpoint
      api_key = "OPENAI_API_KEY", -- Environment variable name for the embedding API key
      model = "text-embedding-3-large", -- Embedding model name
      extra = nil, -- Additional configuration options for the embedding model
    },
    docker_extra_args = "", -- Extra arguments to pass to the docker command
  },
```

RAG Service 目前可以分别配置 LLM 和嵌入模型。在 `llm` 和 `embed` 配置块中，你可以设置以下字段：

- `provider`: 模型提供者（例如 "openai", "ollama", "dashscope", "openrouter"）
- `endpoint`: API 端点
- `api_key`: API Key 的环境变量名
- `model`: 模型名称
- `extra`: 附加配置选项

不同模型提供者的详细配置，你可以在此查看 [此处](./py/rag-service/README.md)。

此外，RAG Service 还依赖 Docker！（对于 macOS 用户，推荐使用 OrbStack 作为 Docker 的替代方案）。

`host_mount` 是将被挂载到容器的路径，默认为主目录。挂载是必需的，以便 RAG 服务可以访问主机上的文件。你可以决定是要挂载整个 `/` 目录、仅项目目录还是主目录。如果你计划对存储在主目录之外的项目使用 avante 和 RAG，则需要将 `host_mount` 设置为文件系统的根目录。

该挂载将是只读的。

更改 rag_service 配置后，你需要手动删除 rag_service 容器以确保使用新配置：`docker rm -fv avante-rag-service`

## 搜索引擎

Avante 的工具包含了一些网页搜索引擎，目前支持：

- [Tavily](https://tavily.com/)
- [SerpApi - Search API](https://serpapi.com/)
- Google 的 [Programmable Search Engine](https://developers.google.com/custom-search/v1/overview)
- [Kagi](https://help.kagi.com/kagi/api/search.html)
- [Brave Search](https://api-dashboard.search.brave.com/app/documentation/web-search/get-started)
- [SearXNG](https://searxng.github.io/searxng/)

默认使用 Tavily，可以通过配置 `Config.web_search_engine.provider` 更改：

```lua
web_search_engine = {
  provider = "tavily", -- tavily, serpapi, google, kagi, brave, or searxng
  proxy = nil, -- proxy support, e.g., http://127.0.0.1:7890
}
```

提供者所需的环境变量：

- Tavily: `TAVILY_API_KEY`
- SerpApi: `SERPAPI_API_KEY`
- Google:
  - `GOOGLE_SEARCH_API_KEY` 作为 [API Key](https://developers.google.com/custom-search/v1/overview)
  - `GOOGLE_SEARCH_ENGINE_ID` 作为 [搜索引擎](https://programmablesearchengine.google.com) ID
- Kagi: `KAGI_API_KEY` 作为 [API Token](https://kagi.com/settings?p=api)
- Brave Search: `BRAVE_API_KEY` 作为 [API Key](https://api-dashboard.search.brave.com/app/keys)
- SearXNG: `SEARXNG_API_URL` 作为 [API URL](https://docs.searxng.org/dev/search_api.html)

## 禁用工具

Avante 默认启用工具，但某些 LLM 模型不支持工具。你可以通过为提供者设置 `disable_tools = true` 来禁用工具。例如：

```lua
providers = {
  claude = {
    endpoint = "https://api.anthropic.com",
    model = "claude-sonnet-4-20250514",
    timeout = 30000, -- Timeout in milliseconds
    disable_tools = true, -- disable tools!
    extra_request_body = {
      temperature = 0,
      max_tokens = 4096,
    }
  }
}
```

如果你想禁止使用某些特定工具（例如避免 Claude 3.7 过度使用 python 工具），可以仅禁用特定工具：

```lua
{
  disabled_tools = { "python" },
}
```

工具列表

> rag_search, python, git_diff, git_commit, glob, search_keyword, read_file_toplevel_symbols,
> read_file, create_file, move_path, copy_path, delete_path, create_dir, bash, web_search, fetch

## 自定义工具

Avante 允许你定义自定义工具，供 AI 在代码生成和分析期间使用。这些工具可以执行 shell 命令、运行脚本或执行任何你需要的自定义逻辑。

### 示例：Go Test Runner

<details>
<summary>以下是一个运行 Go 单元测试的自定义工具示例：</summary>

```lua
{
  custom_tools = {
    {
      name = "run_go_tests",  -- Unique name for the tool
      description = "Run Go unit tests and return results",  -- Description shown to AI
      command = "go test -v ./...",  -- Shell command to execute
      param = {  -- Input parameters (optional)
        type = "table",
        fields = {
          {
            name = "target",
            description = "Package or directory to test (e.g. './pkg/...' or './internal/pkg')",
            type = "string",
            optional = true,
          },
        },
      },
      returns = {  -- Expected return values
        {
          name = "result",
          description = "Result of the fetch",
          type = "string",
        },
        {
          name = "error",
          description = "Error message if the fetch was not successful",
          type = "string",
          optional = true,
        },
      },
      func = function(params, on_log, on_complete)  -- Custom function to execute
        local target = params.target or "./..."
        return vim.system({ "go", "test", "-v", target }, { text = true }):wait().stdout
      end,
    },
  },
}
```

</details>

## MCP

你现在可以通过 `mcphub.nvim` 为 Avante 集成 MCP 功能。详细文档请参阅 [mcphub.nvim](https://ravitemer.github.io/mcphub.nvim/extensions/avante.html)

## 自定义提示词

默认情况下，`avante.nvim` 提供三种不同的交互模式：`planning`、`editing` 和 `suggesting`，每种模式对应三个不同的提示词。

- `planning`: 用于侧边栏的 `require("avante").toggle()`
- `editing`: 用于选中代码块的 `require("avante").edit()`
- `suggesting`: 用于 Tab 流程的 `require("avante").get_suggestion():suggest()`
- `cursor-planning`: 用于 Tab 流程的 `require("avante").toggle()`，但仅在启用 cursor planning mode 时。

用户可以通过 `Config.system_prompt` 或 `Config.override_prompt_dir` 自定义系统提示词。

`Config.system_prompt` 允许你设置全局系统提示词。建议根据你的需求在一个自定义 Autocmds 中调用：

```lua
vim.api.nvim_create_autocmd("User", {
  pattern = "ToggleMyPrompt",
  callback = function() require("avante.config").override({system_prompt = "MY CUSTOM SYSTEM PROMPT"}) end,
})

vim.keymap.set("n", "<leader>am", function() vim.api.nvim_exec_autocmds("User", { pattern = "ToggleMyPrompt" }) end, { desc = "avante: toggle my prompt" })
```

`Config.override_prompt_dir` 允许你指定包含自定义提示模板的目录，这将覆盖内置模板。如果你希望在 Neovim 配置之外维护一组自定义提示词，这非常有用。它可以是表示目录路径的字符串，也可以是返回目录路径的函数：

```lua
-- Example: Override with prompts from a specific directory
require("avante").setup({
  override_prompt_dir = vim.fn.expand("~/.config/nvim/avante_prompts"),
})

-- Example: Override with prompts from a function (dynamic directory)
require("avante").setup({
  override_prompt_dir = function()
    -- Your logic to determine the prompt directory
    return vim.fn.expand("~/.config/nvim/my_dynamic_prompts")
  end,
})
```

> [!WARNING]
>
> 如果你自定义了 `base.avanterules`，请确保 `{% block custom_prompt %}{% endblock %}` 和 `{% block extra_prompt %}{% endblock %}` 存在，否则整个插件可能无法使用。
> 如果你对具体原因或你在做什么不确定，请不要覆盖内置提示词。内置提示词运行效果非常好。

如果你希望为每种模式自定义提示词，`avante.nvim` 将基于给定缓冲区检查项目根目录是否包含以下模式：`*.{mode}.avanterules`。

根目录层级规则：

- lsp workspace folders
- lsp root_dir
- 当前文件名的根模式
- cwd 的根模式

你还可以通过 `rules` 选项为你的 `avanterules` 文件配置自定义目录：

```lua
require('avante').setup({
  rules = {
    project_dir = '.avante/rules', -- relative to project root, can also be an absolute path
    global_dir = '~/.config/avante/rules', -- absolute path
  },
})
```

加载优先级如下：

1.  `rules.project_dir`
2.  `rules.global_dir`
3.  项目根目录

<details>

  <summary>自定义提示词示例文件夹结构</summary>

如果你有以下结构：

```bash
.
├── .git/
├── typescript.planning.avanterules
├── snippets.editing.avanterules
├── suggesting.avanterules
└── src/

```

- `typescript.planning.avanterules` 将用于 `planning` 模式
- `snippets.editing.avanterules` 将用于 `editing` 模式
- `suggesting.avanterules` 将用于 `suggesting` 模式。

</details>

> [!important]
>
> `*.avanterules` 是一个 Jinja 模板文件，它将使用 [minijinja](https://github.com/mitsuhiko/minijinja) 进行渲染。有关如何扩展现有模板的示例，请参阅 [templates](https://github.com/yetone/avante.nvim/blob/main/lua/avante/templates)。

## 集成

Avante.nvim 可以通过其扩展模块与其他插件一起使用。以下是将 Avante 与 [`nvim-tree`](https://github.com/nvim-tree/nvim-tree.lua) 集成的示例，允许你直接从 NvimTree UI 选择或取消选择文件：

```lua
{
    "yetone/avante.nvim",
    event = "VeryLazy",
    keys = {
        {
            "<leader>a+",
            function()
                local tree_ext = require("avante.extensions.nvim_tree")
                tree_ext.add_file()
            end,
            desc = "Select file in NvimTree",
            ft = "NvimTree",
        },
        {
            "<leader>a-",
            function()
                local tree_ext = require("avante.extensions.nvim_tree")
                tree_ext.remove_file()
            end,
            desc = "Deselect file in NvimTree",
            ft = "NvimTree",
        },
    },
    opts = {
        --- other configurations
        selector = {
            exclude_auto_select = { "NvimTree" },
        },
    },
}
```

## 待办事项 (TODOs)

- [x] 与当前文件聊天
- [x] 应用 diff patch
- [x] 与选中代码块聊天
- [x] 斜杠命令
- [x] 编辑选中代码块
- [x] Smart Tab (Cursor Flow)
- [x] 与项目聊天（你可以使用 `@codebase` 与整个项目聊天）
- [x] 与选中的文件聊天
- [x] 工具调用
- [x] MCP
- [x] ACP
- [ ] 更好的代码库索引

## 路线图 (Roadmap)

- **增强的 AI 交互**：提高 AI 分析和推荐的深度，以应对更复杂的编码场景。
- **LSP + Tree-sitter + LLM 集成**：与 LSP、Tree-sitter 和 LLM 集成，提供更准确且强大的代码建议和数据分析。

## 常见问题 (FAQ)

### 如何禁用 agentic mode？

Avante.nvim 提供两种交互模式：

- **`agentic`（默认）**：使用 AI 工具自动生成和应用代码更改
- **`legacy`**：使用传统的规划方法，不自动执行工具

要禁用 agentic mode 并切换到 legacy mode，请更新你的配置：

```lua
{
  mode = "legacy", -- Switch from "agentic" to "legacy"
  -- ... your other configuration options
}
```

**有什么区别？**

- **Agentic mode**：AI 可以自动执行文件操作、bash 命令、网页搜索等工具来完成复杂任务
- **Legacy mode**：AI 提供建议和计划，但需要手动批准所有操作

**何时使用 legacy mode？**

- 如果你更喜欢控制 AI 采取的操作
- 如果你对自动工具执行的安全性感到担忧
- 如果你在应用更改前希望手动审查每一步
- 如果你在敏感环境中工作，不希望自动进行代码更改

你还可以通过配置 `disabled_tools` 在启用 agentic mode 的同时禁用特定工具：

```lua
{
  mode = "agentic",
  disabled_tools = { "bash", "python" }, -- Disable specific tools
  -- ... your other configuration options
}
```

## 贡献 (Contributing)

欢迎为 avante.nvim 做出贡献！如果你有兴趣帮助，请随时提交 pull requests 或打开 issues。

请参阅 [wiki](https://github.com/yetone/avante.nvim/wiki) 获取更多使用技巧和技巧。

## 致谢 (Acknowledgments)

我们衷心感谢以下开源项目的贡献者，他们的代码为 avante.nvim 的开发提供了宝贵的灵感和参考：

| Nvim 插件                                                           | 许可证             | 功能                     | 位置                                                                                                                               |
| --------------------------------------------------------------------- | ------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| [git-conflict.nvim](https://github.com/akinsho/git-conflict.nvim)     | No License         | Diff 比较功能            | [lua/avante/diff.lua](https://github.com/yetone/avante.nvim/blob/main/lua/avante/diff.lua)                                             |
| [ChatGPT.nvim](https://github.com/jackMort/ChatGPT.nvim)              | Apache 2.0 License | Token 计数计算           | [lua/avante/utils/tokens.lua](https://github.com/yetone/avante.nvim/blob/main/lua/avante/utils/tokens.lua)                             |
| [img-clip.nvim](https://github.com/HakonHarnes/img-clip.nvim)         | MIT License        | 剪贴板图片支持           | [lua/avante/clipboard.lua](https://github.com/yetone/avante.nvim/blob/main/lua/avante/clipboard.lua)                                   |
| [copilot.lua](https://github.com/zbirenbaum/copilot.lua)              | MIT License        | Copilot 支持             | [lua/avante/providers/copilot.lua](https://github.com/yetone/avante.nvim/blob/main/lua/avante/providers/copilot.lua)                   |
| [jinja.vim](https://github.com/HiPhish/jinja.vim)                     | MIT License        | 模板 filetype 支持       | [syntax/jinja.vim](https://github.com/yetone/avante.nvim/blob/main/syntax/jinja.vim)                                                   |
| [codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim) | MIT License        | Secrets 逻辑支持         | [lua/avante/providers/init.lua](https://github.com/yetone/avante.nvim/blob/main/lua/avante/providers/init.lua)                         |
| [aider](https://github.com/paul-gauthier/aider)                       | Apache 2.0 License | Planning mode 用户提示词 | [lua/avante/templates/planning.avanterules](https://github.com/yetone/avante.nvim/blob/main/lua/avante/templates/planning.avanterules) |

这些项目的高质量源代码和巧妙设计在整个开发过程中受益匪浅。我们向这些项目的作者和贡献者致以诚挚的感谢和敬意。正是开源社区的无私奉献推动了 avante.nvim 等项目的向前发展。

## 商业赞助 (Business Sponsors)

<table>
  <tr>
    <td align="center">
      <a href="https://s.kiiro.ai/r/ylVbT6" target="_blank">
        <img height="80" src="https://github.com/user-attachments/assets/1abd8ede-bd98-4e6e-8ee0-5a661b40344a" alt="Meshy AI" /><br/>
        <strong>Meshy AI</strong>
        <div>&nbsp;</div>
        <div>The #1 AI 3D Model Generator for Creators</div>
      </a>
    </td>
    <td align="center">
      <a href="https://s.kiiro.ai/r/mGPJOd" target="_blank">
        <img height="80" src="https://github.com/user-attachments/assets/7b7bd75e-1fd2-48cc-a71a-cff206e4fbd7" alt="BabelTower API" /><br/>
        <strong>BabelTower API</strong>
        <div>&nbsp;</div>
        <div>No account needed, use any model instantly</div>
      </a>
    </td>
  </tr>
</table>

## 许可证 (License)

avante.nvim 根据 Apache 2.0 License 许可。更多详情，请参阅 [LICENSE](./LICENSE) 文件。

# Star History

<p align="center">
  <a target="_blank" href="https://star-history.com/#yetone/avante.nvim&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=yetone/avante.nvim&type=Date&theme=dark">
      <img alt="NebulaGraph Data Intelligence Suite(ngdi)" src="https://api.star-history.com/svg?repos=yetone/avante.nvim&type=Date">
    </picture>
  </a>
</p>