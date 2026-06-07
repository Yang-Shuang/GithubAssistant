# GitHub Copilot for Vim 和 Neovim

GitHub Copilot 是一款 AI 结对编程工具，可帮助你更快、更智能地编写代码。它经过数十亿行公开代码的训练，能够将自然语言提示（包括注释和方法名）转化为涵盖几十种语言的编码建议。

Copilot.vim 是用于 GitHub Copilot 的 Vim/Neovim 插件。

欲了解更多详情，请访问 [GitHub Copilot 功能介绍](https://github.com/features/copilot)。

## 获取 GitHub Copilot 访问权限

要使用 GitHub Copilot，需要有效的订阅。你可以注册 [GitHub Copilot 免费版](https://github.com/settings/copilot)，或向企业管理员申请访问权限。

## 快速开始

1. 安装 [Neovim][] 或最新补丁版本的 [Vim][]（版本号为 9.0.0185 或更高）。

2. 安装 [Node.js][]。如果你使用包管理器，请确保同时安装了 NPM（例如在 Debian/Ubuntu 上运行 `apt install nodejs npm`）。

3. 使用 vim-plug、lazy.nvim 或其他任何插件管理器安装 `github/copilot.vim`。或者手动安装，请运行以下命令之一：

    * Vim (Linux/macOS)：

          git clone --depth=1 https://github.com/github/copilot.vim.git \
            ~/.vim/pack/github/start/copilot.vim

    * Neovim (Linux/macOS)：

          git clone --depth=1 https://github.com/github/copilot.vim.git \
            ~/.config/nvim/pack/github/start/copilot.vim

    * Vim, Windows (PowerShell 命令)：

          git clone --depth=1 https://github.com/github/copilot.vim.git `
            $HOME/vimfiles/pack/github/start/copilot.vim

    * Neovim, Windows (PowerShell 命令)：

          git clone --depth=1 https://github.com/github/copilot.vim.git `
            $HOME/AppData/Local/nvim/pack/github/start/copilot.vim

4. 启动 Vim/Neovim 并执行 `:Copilot setup`。

[Node.js]: https://nodejs.org/en/download/
[Neovim]: https://github.com/neovim/neovim/releases/latest
[Vim]: https://github.com/vim/vim

代码建议会以行内形式显示，按 Tab 键即可接受。有关更多信息，请参阅 `:help copilot`。

## 故障排除

我们非常欢迎你的帮助，共同改进 GitHub Copilot！如果你有反馈或遇到任何问题，请前往我们的[反馈论坛](https://github.com/github/copilot.vim/issues)留言。