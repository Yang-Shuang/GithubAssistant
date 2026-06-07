<p align="center">
  <img src="assets/banner.png" alt="Anthropic Cybersecurity Skills" width="100%">
</p>

<div align="center">

# Anthropic Cybersecurity Skills

### 面向 AI Agent 的最大开源网络安全技能库

[![GARS-2026 Survey](https://img.shields.io/badge/GARS--2026-Take%20the%20Survey-E8B84B?style=for-the-badge&logo=googleforms&logoColor=black)](https://mahipal.engineer/survey?utm_source=github_badge&utm_medium=readme&utm_campaign=gars2026)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-754-brightgreen?style=flat-square)](#whats-inside--26-security-domains)
[![Frameworks](https://img.shields.io/badge/frameworks-5-orange?style=flat-square)](#five-frameworks-one-skill-library)
[![Domains](https://img.shields.io/badge/domains-26-9cf?style=flat-square)](#whats-inside--26-security-domains)
[![Platforms](https://img.shields.io/badge/platforms-26%2B-blueviolet?style=flat-square)](#compatible-platforms)
[![GitHub stars](https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/commits/main)
[![agentskills.io](https://img.shields.io/badge/standard-agentskills.io-ff6600?style=flat-square)](https://agentskills.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Playground](https://img.shields.io/badge/Playground-Casky.ai-blue)](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-compatible-blueviolet?style=flat)](https://github.com/NousResearch/hermes-agent)


**754 个生产级网络安全技能 · 26 个安全领域 · 5 种框架映射 · 支持 26+ 款 AI 平台**

[快速开始](#quick-start) · [内容概览](#whats-inside--26-security-domains) · [五大框架](#five-frameworks-one-skill-library) · [兼容平台](#compatible-platforms) · [参与贡献](#contributing)

</div>

---

> ⚠️ **社区项目** —— 本项目为独立社区创建，与 Anthropic PBC 无隶属关系。 

## 赋予任意 AI Agent 资深分析师的安全技能

初级分析师知道对可疑内存转储应运行哪个 Volatility3 插件、哪些 Sigma 规则能捕获 Kerberoasting 攻击，以及如何跨三个云厂商界定云入侵范围。**你的 AI Agent 目前还不具备这些能力——除非你赋予它这些技能。**

本仓库包含 **754 个结构化网络安全技能**，覆盖 **26 个安全领域**，每个技能均遵循 [agentskills.io](https://agentskills.io) 开源标准。每项技能均已映射至 **五大行业标准框架** —— MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、MITRE D3FEND 和 NIST AI RMF，使其成为唯一具备统一跨框架覆盖能力的开源技能库。克隆本仓库并指向你的 Agent，即可在数秒内获得专家级的安全调查指导。

## 五大框架，一个技能库

没有其他开源技能库能将每项技能同时映射到全部五个框架。一项技能，五项合规检查项。 

| Framework | Version | Scope in this repo | What it maps |
|---|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org) | v19.1 | 15 tactics · 286 techniques | Adversary behaviors and TTPs |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | 2.0 | 6 functions · 22 categories | Organizational security posture |
| [MITRE ATLAS](https://atlas.mitre.org) | v5.4 | 16 tactics · 84 techniques | AI/ML adversarial threats |
| [MITRE D3FEND](https://d3fend.mitre.org) | v1.3 | 7 categories · 267 techniques | Defensive countermeasures |
| [NIST AI RMF](https://airc.nist.gov/AI_RMF) | 1.0 | 4 functions · 72 subcategories | AI risk management |

**示例 —— 单个技能在五个框架中的映射：**

| Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF |
|---|---|---|---|---|---|
| `analyzing-network-traffic-of-malware` | T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6 |

### MITRE ATT&CK v19.1 —— 754/754 项技能已映射

每项技能均包含一个 `mitre_attack` frontmatter（前置元数据）列表，使用官方 `mitreattack-python` 库针对 **MITRE ATT&CK v19.1**（最新版本）进行验证 —— 涵盖全部 15 个企业级战术中的 286 种独立技术，并在相关场景下包含 ICS 和 Mobile 技术。零撤销或废弃 ID。v19.1 重构的防御规避（现拆分为 **Stealth/隐蔽** 和 **Defense Impairment/防御削弱**）已反映在下表中。

| Tactic | ID | Skills |
|--------|----|--------|
| Reconnaissance | TA0043 | 103 |
| Resource Development | TA0042 | 22 |
| Initial Access | TA0001 | 467 |
| Execution | TA0002 | 350 |
| Persistence | TA0003 | 444 |
| Privilege Escalation | TA0004 | 464 |
| Stealth | TA0005 | 442 |
| Defense Impairment | TA0112 | 92 |
| Credential Access | TA0006 | 202 |
| Discovery | TA0007 | 237 |
| Lateral Movement | TA0008 | 68 |
| Collection | TA0009 | 172 |
| Command and Control | TA0011 | 123 |
| Exfiltration | TA0010 | 82 |
| Impact | TA0040 | 50 |

## Quick start

```bash
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

可立即与 Claude Code、GitHub Copilot、OpenAI Codex CLI、Cursor、Gemini CLI 以及任何 [agentskills.io](https://agentskills.io)-compatible platform 配合使用。 

## 🌍 GARS-2026 —— 全球 Agent AI 就绪度调查

我正在开展一项全球学术研究，旨在评估安全专业人员、开发人员和团队对 Agentic AI（自主智能体 AI）的实际准备程度 —— 涵盖 MCP 服务器、工具调用、治理机制及人机协同工作流。

**如果你正在使用本仓库，你的反馈将是一个极具价值的数据点。**

📋 **参与调查（约 10 分钟）：**
[Survey Link](https://mahipal.engineer/survey?utm_source=github_repo&utm_medium=readme&utm_campaign=gars2026)

- 60 道题目 · 匿名提交 · 由 SRH Berlin 监督
- 完成后可获得 **50 Casky Tokens**，用于提前体验 [casky.ai](https://casky.ai)
- 调查结果将以 CC-BY 4.0 协议开源发布

## 🚀 在体验区试用

亲身体验 Casky.ai —— 无需本地配置。

**[→ Launch Playground on Casky.ai](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)**

体验区支持以下功能：
- 针对真实目标运行实时网络安全技能演练
- 观察 AI Agent 如何逐步执行结构化技能
- 交互式探索 MITRE ATT&CK 映射工作流
- 测试威胁狩猎、DFIR（数字取证与应急响应）及渗透测试场景

无需安装。无需配置。打开即用。
## Why this exists

2024 年全球网络安全人才缺口达 **480 万个未填补岗位**（ISC2）。AI Agent 可帮助弥补这一缺口 —— 但前提是它们必须具备结构化的领域知识。当前的 Agent 能够编写代码和搜索网络，却缺乏能将通用 LLM 转化为合格安全分析师的从业者操作手册。

现有的安全工具仓库通常提供词表、Payload 或漏洞利用代码。但它们均未为 AI Agent 提供资深分析师所遵循的结构化决策工作流：何时使用何种技术、需检查哪些前置条件、如何逐步执行以及如何验证结果。这正是本项目旨在填补的空缺。

**Anthropic Cybersecurity Skills** 并非脚本或检查单的集合。它是一个面向 [agentskills.io](https://agentskills.io) 标准从头构建的 **AI 原生知识库** —— 采用 YAML frontmatter 实现秒级检索，使用结构化 Markdown 指导逐步执行，并配备参考文件提供深度技术上下文。每项技能均编码了真实从业者的工作流，而非 AI 生成的摘要。 

## What's inside — 26 security domains

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 60 | AWS, Azure, GCP hardening · CSPM · cloud forensics |
| Threat Hunting | 55 | Hypothesis-driven hunts · LOTL detection · behavioral analytics |
| Threat Intelligence | 50 | STIX/TAXII · MISP · feed integration · actor profiling |
| Web Application Security | 42 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |
| Network Security | 40 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |
| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |
| Digital Forensics | 37 | Disk imaging · memory forensics · timeline reconstruction |
| Security Operations | 36 | SIEM correlation · log analysis · alert triage |
| Identity & Access Management | 35 | IAM policies · PAM · zero trust identity · Okta · SailPoint |
| SOC Operations | 33 | Playbooks · escalation workflows · metrics · tabletop exercises |
| Container Security | 30 | K8s RBAC · image scanning · Falco · container forensics |
| OT/ICS Security | 28 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |
| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |
| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |
| Incident Response | 25 | Breach containment · ransomware response · IR playbooks |
| Red Teaming | 24 | Full-scope engagements · AD attacks · phishing simulation |
| Penetration Testing | 23 | Network · web · cloud · mobile · wireless pentesting |
| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |
| DevSecOps | 17 | CI/CD security · code signing · Terraform auditing |
| Phishing Defense | 16 | Email authentication · BEC detection · phishing IR |
| Cryptography | 14 | TLS · Ed25519 · certificate transparency · key management |
| Zero Trust Architecture | 13 | BeyondCorp · CISA maturity model · microsegmentation |
| Mobile Security | 12 | Android/iOS analysis · mobile pentesting · MDM forensics |
| Ransomware Defense | 7 | Precursor detection · response · recovery · encryption analysis |
| Compliance & Governance | 5 | CIS benchmarks · SOC 2 · regulatory frameworks |
| Deception Technology | 2 | Honeytokens · breach detection canaries |

## How AI agents use these skills

每项技能仅需 **约 30 tokens**（仅扫描 frontmatter）即可检索，完整加载工作流需 **500–2,000 tokens**。这种渐进式披露架构使 Agent 能在单次请求中遍历全部 754 项技能，而不会耗尽上下文窗口。 

```
User prompt: "Analyze this memory dump for signs of credential theft"

Agent's internal process:

  1. Scans 754 skill frontmatters (~30 tokens each)
     → identifies 12 relevant skills by matching tags, description, domain

  2. Loads top 3 matches:
     • performing-memory-forensics-with-volatility3
     • hunting-for-credential-dumping-lsass
     • analyzing-windows-event-logs-for-credential-access

  3. Executes the structured Workflow section step-by-step
     → runs Volatility3 plugins, checks LSASS access patterns,
        correlates with event log evidence

  4. Validates results using the Verification section
     → confirms IOCs, maps findings to ATT&CK T1003 (Credential Dumping)
```

**缺乏这些技能时**，Agent 只能盲目猜测工具命令并遗漏关键步骤。**配备这些技能后**，它将遵循资深 DFIR 分析师的标准操作手册。 

## Skill anatomy

每项技能均遵循一致的结构规范：

```
skills/performing-memory-forensics-with-volatility3/
├── SKILL.md              ← Skill definition (YAML frontmatter + Markdown body)
├── references/
│   ├── standards.md      ← MITRE ATT&CK, ATLAS, D3FEND, NIST mappings
│   └── workflows.md      ← Deep technical procedure reference
├── scripts/
│   └── process.py        ← Working helper scripts
└── assets/
    └── template.md       ← Filled-in checklists and report templates
```


### YAML frontmatter (real example)

```yaml
---
name: performing-memory-forensics-with-volatility3
description: >-
  Analyze memory dumps to extract running processes, network connections,
  injected code, and malware artifacts using the Volatility3 framework.
domain: cybersecurity
subdomain: digital-forensics
tags: [forensics, memory-analysis, volatility3, incident-response, dfir]
atlas_techniques: [AML.T0047]
d3fend_techniques: [D3-MA, D3-PSMD]
nist_ai_rmf: [MEASURE-2.6]
nist_csf: [DE.CM-01, RS.AN-03]
version: "1.2"
author: mukul975
license: Apache-2.0
---
```


### Markdown body sections

```markdown
## When to Use
Trigger conditions — when should an AI agent activate this skill?

## Prerequisites
Required tools, access levels, and environment setup.

## Workflow
Step-by-step execution guide with specific commands and decision points.

## Verification
How to confirm the skill was executed successfully.
```

Frontmatter 字段说明：`name`（kebab-case，1–64 字符）、`description`（富含关键词以便 Agent 检索）、`domain`、`subdomain`、`tags`、 `atlas_techniques`（MITRE ATLAS ID）、`d3fend_techniques`（MITRE D3FEND ID）、`nist_ai_rmf`（NIST AI RMF 引用）、`nist_csf`（NIST CSF 2.0 分类）。MITRE ATT&CK 技术映射记录在每个技能的 `references/standards.md` 文件中，并在发布版附带的 ATT&CK Navigator 层中提供。 

<details>
<summary><strong>📊 MITRE ATT&CK Enterprise coverage — all 14 tactics</strong></summary>

&nbsp;

| Tactic | ID | Coverage | Key skills |
|---|---|---|---|
| Reconnaissance | TA0043 | Strong | OSINT, subdomain enumeration, DNS recon |
| Resource Development | TA0042 | Moderate | Phishing infrastructure, C2 setup detection |
| Initial Access | TA0001 | Strong | Phishing simulation, exploit detection, forced browsing |
| Execution | TA0002 | Strong | PowerShell analysis, fileless malware, script block logging |
| Persistence | TA0003 | Strong | Scheduled tasks, registry, service accounts, LOTL |
| Privilege Escalation | TA0004 | Strong | Kerberoasting, AD attacks, cloud privilege escalation |
| Defense Evasion | TA0005 | Strong | Obfuscation, rootkit analysis, evasion detection |
| Credential Access | TA0006 | Strong | Mimikatz detection, pass-the-hash, credential dumping |
| Discovery | TA0007 | Moderate | BloodHound, AD enumeration, network scanning |
| Lateral Movement | TA0008 | Strong | SMB exploits, lateral movement detection with Splunk |
| Collection | TA0009 | Moderate | Email forensics, data staging detection |
| Command and Control | TA0011 | Strong | C2 beaconing, DNS tunneling, Cobalt Strike analysis |
| Exfiltration | TA0010 | Strong | DNS exfiltration, DLP controls, data loss detection |
| Impact | TA0040 | Strong | Ransomware defense, encryption analysis, recovery |

An **ATT&CK Navigator layer file** is included in the [v1.0.0 release assets](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) for visual coverage mapping. 

> **Note:** ATT&CK v19 lands April 28, 2026 — splitting Defense Evasion (TA0005) into two new tactics: *Stealth* and *Impair Defenses*.  Skill mappings will be updated in a forthcoming release.

</details>

<details>
<summary><strong>📊 NIST CSF 2.0 alignment — all 6 functions</strong></summary>

&nbsp;

| Function | Skills | Examples |
|---|---|---|
| **Govern (GV)** | 30+ | Risk strategy, policy frameworks, roles & responsibilities |
| **Identify (ID)** | 120+ | Asset discovery, threat landscape assessment, risk analysis |
| **Protect (PR)** | 150+ | IAM hardening, WAF rules, zero trust, encryption |
| **Detect (DE)** | 200+ | Threat hunting, SIEM correlation, anomaly detection |
| **Respond (RS)** | 160+ | Incident response, forensics, breach containment |
| **Recover (RC)** | 40+ | Ransomware recovery, BCP, disaster recovery |

NIST CSF 2.0 (February 2024) added the **Govern** function  and expanded scope from critical infrastructure to all organizations.  Skill mappings align to all 22 categories and reference 106 subcategories. 

</details>

<details>
<summary><strong>📊 Framework deep dive — ATLAS, D3FEND, AI RMF</strong></summary>

&nbsp;

### MITRE ATLAS v5.4 — AI/ML adversarial threats
ATLAS maps adversarial tactics, techniques, and case studies specific to AI and machine learning systems. Version 5.4 covers **16 tactics and 84 techniques** including agentic AI attack vectors added in late 2025: AI agent context poisoning, tool invocation abuse, MCP server compromises, and malicious agent deployment.  Skills mapped to ATLAS help agents identify and defend against threats to ML pipelines, model weights, inference APIs, and autonomous workflows. 

### MITRE D3FEND v1.3 — Defensive countermeasures
D3FEND is an NSA-funded knowledge graph of **267 defensive techniques** organized across 7 tactical categories: Model, Harden, Detect, Isolate, Deceive, Evict, and Restore.  Built on OWL 2 ontology, it uses a shared Digital Artifact layer to bidirectionally map defensive countermeasures to ATT&CK offensive techniques.  Skills tagged with D3FEND identifiers let agents recommend specific countermeasures for detected threats.

### NIST AI RMF 1.0 + GenAI Profile (AI 600-1)
The AI Risk Management Framework defines 4 core functions — Govern, Map, Measure, Manage — with **72 subcategories** for trustworthy AI development.  The GenAI Profile (AI 600-1, July 2024) adds **12 risk categories** specific to generative AI, from confabulation and data privacy to prompt injection and supply chain risks.  Colorado's AI Act (effective February 2026) provides a **legal safe harbor** for organizations complying with NIST AI RMF, making these mappings directly relevant to regulatory compliance.

</details>

## Compatible platforms

**AI code assistants**
Claude Code (Anthropic) · GitHub Copilot (Microsoft) · Cursor · Windsurf · Cline · Aider · Continue · Roo Code · Amazon Q Developer · Tabnine · Sourcegraph Cody · JetBrains AI 

**CLI agents**
OpenAI Codex CLI · Gemini CLI (Google) 

**Autonomous agents**
Devin · Replit Agent · SWE-agent · OpenHands 

**Agent frameworks & SDKs**
LangChain · CrewAI · AutoGen · Semantic Kernel · Haystack · Vercel AI SDK · Any MCP-compatible agent 

所有支持 [agentskills.io](https://agentskills.io) 标准的平台均可零配置加载这些技能。 

## What people are saying

> *"A database of real, organized security skills that any AI agent can plug into and use. Not tutorials. Not blog posts."* 
> — **[Hasan Toor (@hasantoxr)](https://x.com/hasantoxr/status/2033193922349179249)**, AI/tech creator

> *"This is not a random collection of security scripts. It's a structured operational knowledge base designed for AI-driven security workflows."* 
> — **[fazal-sec](https://fazal-sec.medium.com/claude-skills-ai-powered-cybersecurity-the-complete-guide-to-building-intelligent-security-7bb7e9d14c8e)**,  Medium

## Featured in

| Where | Type | Link |
|---|---|---|
| **awesome-agent-skills** | Awesome List (1,000+ skills index) | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) |
| **awesome-ai-security** | Awesome List (AI security tools) | [ottosulin/awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) |
| **awesome-codex-cli** | Awesome List (Codex CLI resources) | [RoggeOhta/awesome-codex-cli](https://github.com/RoggeOhta/awesome-codex-cli) |
| **SkillsLLM** | Skills directory & marketplace | [skillsllm.com/skill/anthropic-cybersecurity-skills](https://skillsllm.com/skill/anthropic-cybersecurity-skills) |
| **Openflows** | Signal analysis & tracking | [openflows.org](https://openflows.org/currency/currents/anthropic-cybersecurity-skills/) |
| **NeverSight skills_feed** | Automated skills index | [NeverSight/skills_feed](https://github.com/NeverSight/skills_feed) |

## Star history

<a href="https://star-history.com/#mukul975/Anthropic-Cybersecurity-Skills&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date" width="100%" />
 </picture>
</a>

## Releases

| Version | Date | Highlights |
|---|---|---|
| [v1.0.0](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) | March 11, 2026 | 734 skills · 26 domains · MITRE ATT&CK + NIST CSF 2.0 mapping · ATT&CK Navigator layer |

v1.0.0 发布后，`main` 分支持续更新技能库 —— 现已包含 **754 项技能**并实现 **五框架映射**（MITRE ATLAS、D3FEND 和 NIST AI RMF 为发行后新增）。请查看 [Releases](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases) 获取最新标签版本。

## Contributing

本项目通过社区贡献持续成长。参与方式如下：

**添加新技能** —— Deception Technology（2 项）和 Compliance & Governance（5 项）等领域最需补充。请遵循 [CONTRIBUTING.md](CONTRIBUTING.md) 中的模板，并提交标题为 `Add skill: your-skill-name` 的 PR。

**优化现有技能** —— 补充框架映射、修复工作流、更新工具引用，或贡献脚本与模板。

**报告问题** —— 发现流程不准确或脚本失效？[提交 Issue](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues)。

所有 PR 将在 48 小时内完成技术准确性审核及 agentskills.io 标准合规性检查。可查看 [good first issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) 作为入门起点。

本项目遵循 [Contributor Covenant](https://www.contributor-covenant.org/) 行为准则。参与即表示你同意遵守该规范。 

## Community

💬 [Discussions](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) —— 提问、想法与路线图讨论
🐛 [Issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues) —— Bug 报告与功能请求
🔒 [Security Policy](SECURITY.md) —— 负责任披露流程（48 小时内确认） 

## Citation

如果你在研究或出版物中使用了本项目：

```bibtex
@software{anthropic_cybersecurity_skills,
  author       = {Jangra, Mahipal},
  title        = {Anthropic Cybersecurity Skills},
  year         = {2026},
  url          = {https://github.com/mukul975/Anthropic-Cybersecurity-Skills},
  license      = {Apache-2.0},
  note         = {754 structured cybersecurity skills for AI agents,
                  mapped to MITRE ATT\&CK, NIST CSF 2.0, MITRE ATLAS,
                  MITRE D3FEND, and NIST AI RMF}
}
```

## License

本项目采用 [Apache License 2.0](LICENSE) 许可协议。你可自由在个人及商业项目中免费使用、修改和分发这些技能。 

---

<div align="center">

**如果本项目对你的安全工作有所帮助，欢迎点亮 ⭐**

[⭐ Star](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers) · [🍴 Fork](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/fork) · [💬 Discuss](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) · [📝 Contribute](CONTRIBUTING.md)

Community project by [@mukul975](https://github.com/mukul975). Not affiliated with Anthropic PBC.

</div>