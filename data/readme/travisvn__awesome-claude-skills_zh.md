<p align="center">
  <a href="https://github.com/travisvn/awesome-claude-skills">
    <img alt="Awesome Claude Skills" src="https://pc0o4oduww.ufs.sh/f/crfz5GypRfo0lI4924gMSJKLY6297aVP0zZpilXBvqTbDyrs"/>
  </a>
</p>

# Awesome Claude Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Last Updated](https://img.shields.io/badge/updated-Feb%202026-green.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> 一份精心整理的 Claude Skills（技能）精选列表，涵盖自定义 Claude AI 工作流的资源与工具

**Claude Skills（技能）** 教你如何让 Claude **以可重复的方式执行任务**

它们是包含指令、脚本和资源的专用文件夹，当相关任务出现时，Claude 会动态发现并加载它们。

### How Skills Work（Skills 工作原理）

Skills 采用**渐进式披露架构（Progressive Disclosure Architecture）**以提升效率：

1. **元数据加载**（~100 token）：Claude 扫描可用的 Skills 以识别相关匹配项
2. **完整指令**（<5k token）：当 Claude 判定该 Skill 适用时加载
3. **捆绑资源**：文件和可执行代码仅在需要时按需加载

这种设计使得多个 Skills 可以同时保持可用，而不会使 Claude 的上下文窗口过载。

## 🚀 Getting Started（快速入门）

### Claude.ai Web Interface（网页界面）

1. 前往 [Settings > Capabilities](https://claude.ai/settings/capabilities)
2. 启用 Skills 开关
3. 浏览可用技能或上传自定义技能
4. **对于团队/企业版**：管理员需首先在全组织范围内启用 Skills

### Claude Code CLI（命令行）

```bash
# Install skills from marketplace
/plugin marketplace add anthropics/skills

# Or install from local directory
/plugin add /path/to/skill-directory
```

### Claude API

Skills 可通过 `/v1/skills` API 端点访问。详见 [Skills API documentation](https://platform.claude.com/docs/en/api/beta/skills) 获取详细的集成示例。

```python
import anthropic

client = anthropic.Client(api_key="your-api-key")
# See API docs for full implementation details
```

## 🎯 Official Skills（官方技能）

### Document Skills（文档处理）

用于处理复杂文件格式的技能：

- **[docx](https://github.com/anthropics/skills/tree/main/skills/docx)** - 创建、编辑和分析 Word 文档，支持修订模式、批注、格式保留和文本提取
- **[pdf](https://github.com/anthropics/skills/tree/main/skills/pdf)** - 全面的 PDF 操作工具包，用于提取文本和表格、创建新 PDF、合并/拆分文档以及处理表单
- **[pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)** - 创建、编辑和分析 PowerPoint 演示文稿，支持布局、模板、图表和自动幻灯片生成
- **[xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx)** - 创建、编辑和分析 Excel 电子表格，支持公式、格式设置、数据分析和可视化

### Design & Creative（设计与创意）

- **[algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art)** - 使用 p5.js 创作生成艺术，支持种子随机数、流场和粒子系统
- **[canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design)** - 运用设计哲学在 .png 和 .pdf 格式中创作精美的视觉艺术作品
- **[slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator)** - 创建符合 Slack 尺寸限制的优化动画 GIF

### Development（开发工具）

- **[frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design)** - 指导 Claude 避免“AI 滥俗”或通用美学，并做出大胆的设计决策。与 React & Tailwind 配合效果极佳。
- **[web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder)** - 使用 React、Tailwind CSS 和 shadcn/ui 组件构建复杂的 claude.ai HTML artifacts（网页制品）
- **[mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder)** - 创建高质量 MCP 服务器的指南，用于集成外部 API 和服务
- **[webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing)** - 使用 Playwright 测试本地 Web 应用程序，进行 UI 验证和调试

### Communication（沟通协作）

- **[brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines)** - 将 Anthropic 的官方品牌颜色和排版应用于 artifacts（网页制品）
- **[internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms)** - 撰写内部通讯文件，如状态报告、新闻简报和常见问题解答（FAQ）

### Skill Creation（技能创建工具）

- **[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)** - 交互式技能创建工具，通过问答引导你构建新 Skills

## 🌟 Community Skills（社区技能）

> [!Warning]
> Skills 可在 Claude 的环境中执行任意代码。
> 
> 更多信息请参阅 [Security & Best Practices](#-security--best-practices)

### Collections & Libraries（集合与库）

- **[obra/superpowers](https://github.com/obra/superpowers)** - Claude Code 的核心技能库，包含 20+ 经过实战检验的技能（如 TDD、调试和协作模式）
  - 提供 `/brainstorm`、`/write-plan`、`/execute-plan` 命令及 `skills-search` 工具
  - [superpowers-skills](https://github.com/obra/superpowers-skills) - 社区维护的技能仓库
  - [Blog: Superpowers](https://blog.fsck.com/2025/10/09/superpowers/) - 作者 Jesse Vincent 的概述文章
  - 安装：`/plugin marketplace add obra/superpowers-marketplace`
 
- **[obra/superpowers-lab](https://github.com/obra/superpowers-lab)** - `Claude Code Superpowers` 的实验性技能（见上文）
  - 使用仍在完善和测试中的新技术（即其中的 Skills 可能会随时间变化）
  - [Blog post about its development](https://blog.fsck.com/2025/10/23/naming-claude-plugins/)
  - 从 `superpowers-marketplace` 插件安装


### Individual Skills（独立技能）

> These will be broken down into categories once there are enough community skills available to list
> [!Note] 当社区技能数量足够多时，此处将按类别进行细分。

| Skill | Description |
| --- | --- |
| **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** | iOS 应用构建、导航与自动化测试 |
| **[ffuf-web-fuzzing](https://github.com/jthack/ffuf_claude_skill)** | 渗透测试中 ffuf Web Fuzzing 的专业指导，包括使用原始请求进行身份验证模糊测试、自动校准和结果分析 |
| **[playwright-skill](https://github.com/lackeyjb/playwright-skill)** | 基于 Playwright 的通用浏览器自动化 |
| **[claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill)** | d3.js 数据可视化 |
| **[claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)** | 全面的即用型科学技能集合，包括使用专业科学库和数据库的工作流 |
| **[web-asset-generator](https://github.com/alonw0/web-asset-generator)** | 生成网站图标、应用图标和社交媒体图片等 Web 资源 |
| **[loki-mode](https://github.com/asklokesh/claudeskill-loki-mode)** | 多智能体自主启动系统——编排 37 个 AI 智能体跨越 6 个群组，从 PRD（产品需求文档）到营收实现完整初创公司的构建、部署与运营 |
| **[Trail of Bits Security Skills](https://github.com/trailofbits/skills)** | 用于 CodeQL/Semgrep 静态分析、变体分析、代码审计和漏洞检测的安全技能 |
| **[frontend-slides](https://github.com/zarazhangrui/frontend-slides)** | 从零创建或转换 PowerPoint 文件，生成富含动画的 HTML 演示文稿 |
| **[Expo Skills](https://github.com/expo/skills)** | Expo 团队官方提供的 Expo 应用开发技能 |
| **[shadcn/ui](https://ui.shadcn.com/docs/skills)** | 为 Claude Code 提供 shadcn 组件上下文及模式强制支持 |
| **[get-shit-done](https://github.com/gsd-build/get-shit-done)** | TÂCHES 推出的轻量级元提示（meta-prompting）、上下文工程和规范驱动开发系统，专为 Claude Code 打造 |

_More community skills coming soon! Submit a PR to add your skill._
_更多社区技能即将推出！提交 PR 以添加你的技能。_

### Tools（工具）

- **[yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - 将文档网站转换为 Claude Skills 的工具

## ✏️ Creating Your First Skill（创建你的第一个 Skill）

<details>
<summary><strong>Step-by-Step Guide</strong></summary>

### Method 1: Use skill-creator (Recommended)

The easiest way to create a skill is to use the built-in `skill-creator`:

1. Enable the skill-creator skill in Claude
2. Ask Claude: "Use the skill-creator to help me build a skill for [your task]"
3. Answer the interactive questions about your workflow
4. Claude generates the complete skill structure for you

### Method 2: Manual Creation

1. **Create folder structure**:

   ```
   my-skill/
   ├── SKILL.md          # Main skill file with frontmatter
   ├── scripts/          # Optional executable scripts
   │   └── helper.py
   └── resources/        # Optional supporting files
       └── template.json
   ```

2. **Create SKILL.md with frontmatter**:

   ```yaml
   ---
   name: my-skill
   description: Brief description for skill discovery (keep concise)
   ---

   # Detailed Instructions

   Claude will read these instructions when the skill is activated.

   ## Usage
   Explain how to use this skill...

   ## Examples
   Provide clear examples...
   ```

3. **Add executable scripts** (optional):

   - Python, JavaScript, or other scripts Claude can execute
   - Reference them in your SKILL.md instructions

4. **Test locally**:

   - Install the skill in Claude Code or Claude Desktop
   - Test with relevant tasks
   - Iterate and refine

5. **Share**:
   - Publish to GitHub
   - Submit to this awesome list via PR
   - Share with your team via git repos or internal distribution

### Best Practices

- **Keep descriptions concise** - The frontmatter description is used for skill discovery
- **Use clear, actionable instructions** - Write instructions as if for a human collaborator
- **Include examples** - Show specific examples in your SKILL.md
- **Version your skills** - Use git tags for version management
- **Document dependencies** - List any prerequisites or required packages
- **Test thoroughly** - Verify your skill works across different scenarios

</details>

## 📚 Official Documentation & Resources（官方文档与资源）

### Getting Started（快速入门）

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) - 解释 Claude Skills 的官方支持文章
- [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) - 如何启用和使用技能

### Documentation（文档资料）

- [Claude Skills Announcement](https://www.anthropic.com/news/skills) - Anthropic 的官方公告
- [Equipping Agents with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - 关于 Agent Skills 的工程深度解析
- [Claude Developer Platform](https://docs.claude.com/) - 官方文档
- [Skills API Endpoint](https://platform.claude.com/docs/en/api/beta/skills) - `/v1/skills` API 文档

### Repositories & Examples（代码库与示例）

- [anthropics/skills](https://github.com/anthropics/skills) - Skills 的官方公开仓库
- [Claude Cookbooks - Skills](https://github.com/anthropics/claude-cookbooks/tree/main/skills) - 示例笔记本和教程

## 📅 Recent Updates（最近更新）

### November 2025

- **Nov 13**: Anthropic publishes [Skills Explained](https://claude.com/blog/skills-explained) - Comprehensive guide covering progressive disclosure architecture, decision matrices for Skills vs Prompts/Subagents/Projects, and best practices
- **Nov 13**：Anthropic 发布 [Skills Explained](https://claude.com/blog/skills-explained) —— 涵盖渐进式披露架构、Skills vs Prompts/Subagents/Projects 的决策矩阵以及最佳实践的综合性指南

### October 2025

- **Oct 18**: Major community repositories emerge: [obra/superpowers](https://github.com/obra/superpowers) skills library
- **Oct 17**: Community publishes practical tutorials on DEV.to and Medium
- **Oct 16**: 🎉 **Claude Skills officially announced** - Available across Claude.ai, Code, and API
- **Oct 16**: Initial skills released including docx, pdf, pptx, xlsx, algorithmic-art, canvas-design, and more

## 💡 Skills vs Other Approaches（Skills 与其他方案的对比）

### Quick Reference: When to Use What（快速参考：何时使用何种方案）

| Tool | Best For |
|------|----------|
| **Skills** | Reusable procedural knowledge across conversations |
| **Prompts** | One-time instructions and immediate context |
| **Projects** | Persistent background knowledge within workspaces |
| **Subagents** | Independent task execution with specific permissions |
| **MCP** | Connecting Claude to external data sources |

**Use Skills when**: Capabilities should be accessible to any Claude instance. They're portable expertise.
**何时使用 Skills**：当能力应可供任何 Claude 实例调用时。它们是可移植的专业知识。

**Use Subagents when**: You need self-contained agents designed for specific purposes with independent workflows and restricted tool access.
**何时使用 Subagents（子智能体）**：当你需要为特定目的设计的自包含智能体，拥有独立工作流和受限的工具访问权限时。

**Combined approach**: Subagents can leverage Skills for specialized expertise, merging independence with portable knowledge.
**组合方案**：Subagents 可利用 Skills 获取专业知识，将独立性（自主工作流）与可移植知识相结合。

**Key insight**: *If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill.*
**核心洞察**：*如果你发现自己跨多个对话反复输入相同的提示词，就该创建一个 Skill 了。*

### Skills vs MCP (Model Context Protocol)（Skills 与 MCP）

| Feature              | Skills                                        | MCP                               |
| -------------------- | --------------------------------------------- | --------------------------------- |
| **Purpose**          | Task-specific expertise and workflows         | External data/API integration     |
| **Portability**      | Same format everywhere (Claude.ai, Code, API) | Requires server configuration     |
| **Code Execution**   | Can include executable scripts                | Provides tools/resources          |
| **Token Efficiency** | 30-50 tokens until loaded                     | Varies by implementation          |
| **Best For**         | Repeatable tasks, document workflows          | Database access, API integrations |

**Use Together**: Skills can create MCP servers! The `mcp-builder` skill helps build high-quality MCP integrations.
**配合使用**：Skills 可以创建 MCP 服务器！`mcp-builder` 技能有助于构建高质量的 MCP 集成。

#### Skills vs System Prompts（Skills 与系统提示词）

| Feature           | Skills                                              | System Prompts                    |
| ----------------- | --------------------------------------------------- | --------------------------------- |
| **Structure**     | Folder with YAML frontmatter, instructions, scripts | Plain text instructions           |
| **Reusability**   | Version-controlled, shareable, composable           | Copy-paste, conversation-specific |
| **Loading**       | On-demand (only when relevant)                      | Always in context                 |
| **Maintenance**   | Centralized updates                                 | Manual updates per conversation   |
| **Composability** | Multiple skills stack automatically                 | Manual combination                |

## 📖 Tutorials & Guides（教程与指南）

### Written Tutorials（图文教程）

- [How to Create Your First Claude Skill](https://skywork.ai/blog/ai-agent/how-to-create-claude-skill-step-by-step-guide/) - Step-by-step tutorial with examples
- [How to Use Skills in Claude Code](https://skywork.ai/blog/how-to-use-skills-in-claude-code-install-path-project-scoping-testing/) - Installation, project scoping, and testing guide

### Video Tutorials（视频教程）

_Video tutorials coming soon! Have a good video about Claude Skills? Submit a PR!_
_视频教程即将上线！如果你有关于 Claude Skills 的优质视频，欢迎提交 PR！_

<details>
<summary>Example topics we'd love to see</summary>

- Getting started with Claude Skills
- Building your first custom skill
- Skills vs MCP comparison
- Enterprise deployment strategies
</details>

## 📰 Articles & Blog Posts（文章与博客）

- [Skills Explained](https://claude.com/blog/skills-explained) - Official Anthropic blog post covering progressive disclosure, use cases, and when to use Skills vs other tools
- [Simon Willison: Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/) - Technical deep dive and analysis

## 🔒 Security & Best Practices（安全与最佳实践）

⚠️ **Important**: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.
⚠️ **重要提示**：Skills 可在 Claude 的环境中执行任意代码。仅安装来自可信来源的技能。

<details>
<summary><strong>Security Guidelines & Best Practices</strong></summary>

### Vetting Skills（技能审核）

- **Only install skills from trusted sources**
- **Review SKILL.md and all scripts** before enabling a skill
- **Be cautious of skills** that request sensitive data access
- **Audit carefully** before deploying to production or enterprise environments

### Security Concerns（安全顾虑）

- **Malicious skills** may introduce vulnerabilities or enable data exfiltration
- **Prompt injection attacks** could be amplified through compromised skills
- **Sandboxing limitations** - Understand the security model before enterprise deployment
- **Security research**: [Weaponizing Claude Code Skills](https://medium.com/@yossifqassim/weaponizing-claude-code-skills-from-5-5-to-remote-shell-a14af2d109c9) - Analysis of potential security risks

### Best Practices（最佳实践）

- **Version control** - Track all skills in git with proper version tags
- **Code review** - Peer review custom skills before team distribution
- **Least privilege** - Only grant necessary permissions and access
- **Regular audits** - Periodically review installed skills
- **Documentation** - Maintain clear documentation for custom skills
- **Testing** - Thoroughly test skills in non-production environments first

### Enterprise Considerations（企业注意事项）

- As of October 2025, Claude.ai does not support centralized admin management for custom skills
- Use version control and internal repositories for team skill distribution
- Establish clear policies for skill vetting and approval
- Monitor skill usage and performance

</details>

## 🛠️ Troubleshooting（故障排除）

<details>
<summary><strong>Known Issues & Common Problems</strong></summary>

### Known Issues（已知问题）

- **Linux path bug (Oct 18, 2025)**: Agent SDK uses hardcoded macOS paths instead of environment home directory

  - [Issue #268](https://github.com/anthropics/claude-agent-sdk-python/issues/268)
  - Workaround: Manually specify skill paths

- **Enterprise distribution**: No centralized admin management yet for custom skills on claude.ai
  - Use git repositories for team distribution
  - API integration provides more control

### Common Problems（常见问题）

**Skills not appearing in Claude**

- Check Settings > Capabilities to ensure Skills are enabled
- For Team/Enterprise: Verify admin has enabled Skills organization-wide
- Restart Claude after installing new skills

**Skills not loading/activating**

- Verify SKILL.md has proper YAML frontmatter format
- Check that `name` and `description` fields are present
- Ensure file structure matches expected format

**Permission errors**

- Review admin settings for Team/Enterprise accounts
- Check file permissions in skill directories
- Verify API key has appropriate permissions

**Skill execution failures**

- Check script dependencies are installed
- Review error logs for specific issues
- Test scripts independently outside of Claude

### Getting Help（获取帮助）

- [Official Skills Repository Issues](https://github.com/anthropics/skills/issues)
- [Claude Documentation](https://docs.claude.com/)
- [Community Discussions](https://github.com/anthropics/skills/discussions)

</details>

## ❓ FAQ（常见问题解答）

<details>
<summary><strong>Common Questions</strong></summary>

**Q: How much do skills impact token usage?**

A: Skills are highly efficient thanks to progressive disclosure. Each skill uses only ~100 tokens during metadata scanning to determine relevance. When activated, the full skill content loads at <5k tokens. Bundled resources only load as needed.

**Q: What's the difference between Claude Skills and Agent Skills?**

A: They are the same thing.

**Q: Can I share skills with my team?**

A: Yes! Skills can be shared via:

- Git repositories (recommended)
- Internal file sharing
- Claude API for programmatic distribution
- Enterprise-wide deployment features (coming soon)

**Q: Do skills work with all Claude models?**

A: Skills are available for Pro, Max, Team, and Enterprise users. Free tier users do not have access to Skills.

**Q: Can skills call external APIs?**

A: Yes, skills can include scripts that call external APIs. For complex API integrations, consider using MCP (Model Context Protocol) alongside skills.

**Q: How does Claude decide which skill to use?**

A: Claude scans all available skills' frontmatter (name and description), evaluates relevance to the current task, then loads the full content of relevant skills. Multiple skills can be loaded and composed together automatically.

**Q: Can I use Skills and MCP together?**

A: Absolutely! They complement each other. Use Skills for task-specific workflows and MCP for external data/API integration. The `mcp-builder` skill can even help you build MCP servers.

**Q: Are there any costs beyond my Claude subscription?**

A: No additional costs for using official skills. Community and custom skills are free to use, though some may require external services (APIs, databases, etc.) that have their own costs.

**Q: Can I monetize custom skills?**

A: Currently, there is no official marketplace for paid skills. Anthropic has mentioned plans for community contributions and a potential marketplace in the future.

**Q: How do I update a skill?**

A: For skills from git repositories, pull the latest changes. For manually installed skills, replace the skill folder with the updated version. Always test updates in a non-production environment first.

</details>

## 🤝 Contributing（贡献指南）

Contributions welcome! See [contribution guidelines](CONTRIBUTING.md) for details. To add a skill or resource: fork, add to appropriate section, submit PR.