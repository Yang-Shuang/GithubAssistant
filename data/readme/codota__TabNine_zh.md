# TabNine

这是 [TabNine](https://tabnine.com)（全语言自动补全工具）后端的代码仓库。此处不提供源代码文件，因为该后端属于闭源项目。

你可以通过提交 Issue 来提出功能建议。同时也欢迎就配置文件的修改提交 Pull Request。

`languages.yml` 用于确定哪些文件扩展名被视为属于同一语言。（例如，`.c` 文件中的标识符也会在 `.h` 文件中被推荐用于自动补全。）
`language_tokenization.json` 用于定义语言的**分词（tokenization）**规则。例如，Lisp 中的标识符可以包含连字符，而 Java 则不可以。

如果你的功能建议与特定编辑器的 TabNine 客户端相关，请在以下仓库中提交 Issue：

- [VS Code](https://github.com/zxqfl/tabnine-vscode)
- [Sublime Text](https://github.com/zxqfl/tabnine-sublime)
- [Vim](https://github.com/zxqfl/tabnine-vim)
- [Atom](https://github.com/zxqfl/tabnine-atom)

你可能还会对这些由**第三方**开发的 TabNine 客户端感兴趣：

> **_注意：_** Codota **不会**验证这些插件中的任何代码，也对此不承担任何责任。
- [Emacs](https://github.com/TommyX12/company-tabnine)
- [Vim (Deoplete)](https://github.com/tbodt/deoplete-tabnine)
- [Eclipse](https://github.com/GitPopcorn/tabnine-eclipse)
- 你的客户端 https://github.com/codota/TabNine/blob/master/HowToWriteAClient.md

# 支持的架构
- x86_64-unknown-linux-musl
- x86_64-apple-darwin
- aarch64-apple-darwin
- i686-pc-windows-gnu
- x86_64-pc-windows-gnu