<p align="center">
  <img src="assets/banner.svg" alt="Claude Ads: Paid Advertising Audit Skill for Claude Code. Animated terminal-style banner with breathing gradient logo, scanning command palette, and pulsing status indicators" width="100%">
</p>

# Claude Ads: Paid Advertising Audit Skill for Claude Code

A manual audit of a single Google Ads account takes 4-6 hours of senior PPC time. **Claude Ads runs the same audit in 10-15 minutes**, scores it on a 0-100 weighted scale, and outputs a prioritized action plan across Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, and Amazon Ads. Built for **PPC agencies, in-house marketers, and freelance ad consultants**. Local, deterministic, MIT-licensed.

[![Agent Skill](https://img.shields.io/badge/Agent%20Skills-Compatible-blue)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/AgriciDaniel/claude-ads?label=public%20release)](https://github.com/AgriciDaniel/claude-ads/releases)
[![CI](https://img.shields.io/github/actions/workflow/status/AgriciDaniel/claude-ads/ci.yml?branch=main&label=public%20CI)](https://github.com/AgriciDaniel/claude-ads/actions)
[![Community](https://img.shields.io/badge/AI%20Marketing%20Hub-Pro%20community-purple)](https://www.skool.com/ai-marketing-hub-pro)
[![GitHub org](https://img.shields.io/badge/AI%20Marketing%20Hub-GitHub-181717?logo=github&logoColor=white)](https://github.com/AI-Marketing-Hub)

**Host support:**
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Verified-brightgreen)](https://claude.ai/claude-code)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-Experimental-yellow)](https://github.com/openai/codex)
[![Cursor](https://img.shields.io/badge/Cursor-Experimental-yellow)](https://cursor.sh)
[![Windsurf](https://img.shields.io/badge/Windsurf-Experimental-yellow)](https://codeium.com/windsurf)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Experimental-yellow)](https://github.com/google-gemini/gemini-cli)
[![Goose](https://img.shields.io/badge/Goose-Experimental-yellow)](https://block.github.io/goose/)

> **Last updated:** 2026-05-18 · **Version:** v1.7.1 · [CHANGELOG](CHANGELOG.md) · [Blog: full ad audit breakdown](https://agricidaniel.com/blog/claude-code-ad-agency)

> **Two versions of this skill.**
> - 🌐 **Public open-source** → [`AgriciDaniel/claude-ads`](https://github.com/AgriciDaniel/claude-ads): MIT, public releases, no membership. Best if you want stable + downloadable.
> - 🔒 **Community private mirror** → [`AI-Marketing-Hub/claude-ads`](https://github.com/AI-Marketing-Hub/claude-ads): early access to upcoming features and direct collaboration with the [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro) community. Requires membership.

## Who this is for

- **PPC agencies running 5+ accounts**: audit every account weekly instead of once a quarter. Same time budget.
- **In-house marketers owning paid across 4+ platforms**: second-pair-of-eyes before exec reviews. No human bias on which platform you favor.
- **Freelance PPC consultants**: anchor day-1 client scope with a 10-minute audit. Win the engagement before you spend an hour on diagnostic.

## What's new in v1.7.0 (Wave 2)

- **3 new sub-skills**: `/ads amazon` (Sponsored Products/Brands/Display, ACOS/TACOS), `/ads attribution` (AdAttributionKit + GA4 + Consent Mode V2), `/ads tracking` (sGTM + CAPI Gateway + dedup + hashing).
- **41-test pytest eval harness** in `tests/`: routing snapshots, bidirectional 209-check catalog coverage, scoring math determinism, SSRF regression. Runs in CI on every commit.
- **Cross-runtime install matrix**: `install.sh` / `install.ps1 --target=<host>` with whitelist validation for Claude Code, Codex CLI, Cursor, Windsurf, Gemini CLI, Goose.
- **Deep platform rewrites**: `/ads google` for the AI Max era (`ai_max_setting.enable_ai_max`, AI Brief, FUE, brand exclusions). `/ads meta` for the Andromeda + GEM + Lattice era with Entity-ID clustering detection.
- **10-Principle Thinking Framework**: every audit, plan, and creative output runs under a shared cognitive discipline. See [`ads/references/thinking-framework.md`](ads/references/thinking-framework.md).

Full release notes: [CHANGELOG.md](CHANGELOG.md).

## Demo

<p align="center">
  <img src="assets/demo.gif" alt="Claude Ads in action: /ads audit dispatching 6 parallel subagents, returning Ads Health Score with platform breakdown and prioritized action plan" width="100%">
</p>

### Sample output

What `/ads audit` actually returns (truncated for brevity):

```json
{
  "ads_health_score": 73,
  "grade": "C",
  "audit_date": "2026-05-18",
  "platforms": {
    "google_ads": { "score": 78, "grade": "B", "checks_run": 80, "critical": 2, "high": 5 },
    "meta_ads":   { "score": 64, "grade": "C", "checks_run": 50, "critical": 4, "high": 7 },
    "linkedin":   { "score": 81, "grade": "B", "checks_run": 27, "critical": 0, "high": 3 }
  },
  "top_findings": [
    {
      "id": "M-AND-01",
      "severity": "critical",
      "platform": "meta",
      "title": "Andromeda creative similarity > 60%: retrieval suppression risk",
      "impact": "Estimated 20-35% reach loss; 4 ad sets affected",
      "action": "Replace 7 near-duplicate creatives with concept-diverse variants",
      "owner": "creative",
      "eta_days": 7
    },
    {
      "id": "G-AIM-03",
      "severity": "high",
      "platform": "google",
      "title": "AI Max enabled without negative keyword discipline",
      "impact": "Wasted spend ~$1,400/mo on irrelevant queries",
      "action": "Build negative list from 30d search term report",
      "owner": "search",
      "eta_days": 2
    }
  ],
  "quick_wins": [
    "Enable Consent Mode V2 (Privacy Sandbox compatible, ~1 hr)",
    "Pause 3 ad groups failing 3x Kill Rule (saves ~$420/mo)"
  ]
}
```

Plus a PDF version (`/ads report`) with health score gauge, platform comparison charts, and zero-overlap layout for client delivery.

## Contents

- [Installation: 3 ways to add Claude Ads](#installation-3-ways-to-add-claude-ads)
- [Quick Start](#quick-start)
- [Commands](#commands)
- [Features: what 250+ audit checks cover](#features-what-250-audit-checks-cover)
- [Compared to manual / agency / commercial tools](#compared-to-manual--agency--commercial-tools)
- [Use cases](#use-cases)
- [Eval harness: verified rigor](#eval-harness-verified-rigor)
- [Architecture](#architecture)
- [How it analyzes your ads](#how-it-analyzes-your-ads)
- [FAQ](#faq)
- [Requirements](#requirements)
- [Uninstall](#uninstall)
- [Roadmap](#roadmap)
- [Project info](#project-info)
- [Related projects](#related-projects)
- [Maintainer](#maintainer)
- [License](#license)

## Installation: 3 ways to add Claude Ads

> ℹ️ **Two install paths — pick the one that matches your access.**
>
> The commands below default to the **community private mirror** at `AI-Marketing-Hub/claude-ads` (early access for Pro members). To use the **public release** at `AgriciDaniel/claude-ads` (MIT, no membership), swap `AI-Marketing-Hub/claude-ads` for `AgriciDaniel/claude-ads` and the plugin slug `claude-ads@ai-marketing-hub-claude-ads` for `claude-ads@agricidaniel-claude-ads` in every command.
>
> Pro members: requires `gh auth login` (or PAT) with access to the `AI-Marketing-Hub` org. If `/plugin marketplace add` 404s, DM in the [Skool community](https://www.skool.com/ai-marketing-hub-pro) to get added.

### 1. Plugin install (Claude Code, recommended)

```shell
/plugin marketplace add AI-Marketing-Hub/claude-ads
/plugin install claude-ads@ai-marketing-hub-claude-ads
```

Registers claude-ads as a native plugin with auto-updates, namespace isolation, and version tracking.

### 2. One-command install (Unix/macOS/Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/AI-Marketing-Hub/claude-ads/main/install.sh | bash
```

### 2. One-command install (Windows PowerShell)

```powershell
irm https://raw.githubusercontent.com/AI-Marketing-Hub/claude-ads/main/install.ps1 | iex
```

### 3. Cross-host install (Codex CLI / Cursor / Windsurf / Gemini CLI / Goose)

```bash
# Unix/macOS/Linux
bash install.sh --target=codex      # OpenAI Codex CLI       (experimental)
bash install.sh --target=cursor     # Cursor IDE              (experimental)
bash install.sh --target=windsurf   # Windsurf IDE            (experimental)
bash install.sh --target=gemini     # Gemini CLI              (experimental)
bash install.sh --target=goose      # Goose CLI               (experimental)
```

```powershell
# Windows PowerShell
.\install.ps1 -Target codex
.\install.ps1 -Target cursor
.\install.ps1 -Target windsurf
.\install.ps1 -Target gemini
.\install.ps1 -Target goose
```

**Per-host install path table:**

| Target     | Skills root                                     | Agents root                                | Python deps |
|------------|-------------------------------------------------|--------------------------------------------|-------------|
| `claude`   | `~/.claude/skills`                              | `~/.claude/agents`                         | ✓           |
| `codex`    | `~/.codex/skills`                               | `~/.codex/agents`                          | ✓           |
| `cursor`   | `~/.cursor/extensions/claude-ads/skills`        | `~/.cursor/extensions/claude-ads/agents`   | skipped     |
| `windsurf` | `~/.windsurf/skills`                            | `~/.windsurf/agents`                       | skipped     |
| `gemini`   | `~/.gemini/extensions/claude-ads/skills`        | `~/.gemini/extensions/claude-ads/agents`   | skipped     |
| `goose`    | `~/.config/goose/skills`                        | `~/.config/goose/agents`                   | skipped     |

**Path overrides:**

```bash
bash install.sh --target=claude --skill-dir=~/custom/skills --agent-dir=~/custom/agents
```

Targets and override paths are strictly whitelist-validated: no shell injection, no flag confusion, no `..` segments, no UNC paths.

> ⚠ **Experimental targets:** Only Claude Code is verified end-to-end. Other host install paths follow each host's documented convention; skill discovery and sub-skill routing may differ. Open an issue with reproduction details if a target needs adjustment.

### Manual install

```bash
git clone https://github.com/AI-Marketing-Hub/claude-ads.git
cd claude-ads
./install.sh                # Unix/macOS/Linux, default target=claude
./install.sh --target=codex # any cross-host target
```

```powershell
.\install.ps1                # Windows PowerShell, default Target=claude
.\install.ps1 -Target codex
```

<p align="center">
  <img src="assets/diagrams/20-install-methods.svg" alt="Installation Methods Comparison" width="100%">
</p>

## Quick Start

```bash
# Start Claude Code
claude

# Run a full multi-platform audit
/ads audit

# Deep analysis for a single platform
/ads google
/ads meta
/ads linkedin

# Strategic planning by business type
/ads plan saas
/ads plan ecommerce
/ads plan local-service

# Cross-platform creative audit
/ads creative

# Budget and bidding strategy review
/ads budget
```

<p align="center">
  <img src="assets/diagrams/06-how-it-works.svg" alt="How It Works: 5-Step Process" width="100%">
</p>

## Commands

| Command | Description |
|---------|-------------|
| `/ads audit` | Full multi-platform audit with parallel subagent delegation |
| `/ads google` | Google Ads deep analysis (Search, PMax, AI Max, Display, YouTube, Demand Gen) |
| `/ads meta` | Meta Ads deep analysis (FB, IG, Threads, Advantage+, Andromeda + GEM + Lattice) |
| `/ads youtube` | YouTube Ads specific analysis (Skippable, Shorts, Demand Gen, CTV) |
| `/ads linkedin` | LinkedIn Ads deep analysis (B2B, Lead Gen, TLA, ABM) |
| `/ads tiktok` | TikTok Ads deep analysis (Creative, Shop, Smart+, post-USDS) |
| `/ads microsoft` | Microsoft/Bing Ads deep analysis (Copilot, Import validation) |
| `/ads apple` | Apple Ads deep analysis (CPPs, Maximize Conversions, AdAttributionKit, TAP) |
| `/ads amazon` | Amazon Ads deep analysis (Sponsored Products / Brands / Display, ACOS / TACOS) · *Wave 2* |
| `/ads attribution` | Cross-platform attribution audit (AdAttributionKit, GA4, Consent Mode V2, MMP) · *Wave 2* |
| `/ads tracking` | Server-side tracking pipeline audit (sGTM, CAPI Gateway, dedup, hashing) · *Wave 2* |
| `/ads creative` | Cross-platform creative quality audit and fatigue detection |
| `/ads landing` | Landing page quality assessment for ad campaigns |
| `/ads budget` | Budget allocation and bidding strategy review |
| `/ads plan <type>` | Strategic ad plan with industry templates |
| `/ads competitor` | Competitor ad intelligence across all platforms |
| `/ads math` | PPC financial calculator (CPA, ROAS, break-even, budget forecasting, LTV:CAC) |
| `/ads test` | A/B test design (hypothesis framework, significance, sample size, duration) |
| `/ads report` | Generate PDF audit report for client deliverables |
| `/ads dna <url>` | Extract brand DNA from website → `brand-profile.json` |
| `/ads create` | Generate campaign concepts + copy briefs → `campaign-brief.md` |
| `/ads generate` | Generate AI ad images from brief → `ad-assets/` |
| `/ads photoshoot` | Product photography in 5 styles (Studio, Floating, Ingredient, In Use, Lifestyle) |

### `/ads audit`
**Full Multi-Platform Audit**

Spawns 6 parallel subagents:
- **audit-google**: 80 checks across Search, PMax, AI Max, Demand Gen, CTV, YouTube
- **audit-meta**: 50 checks across Pixel/CAPI, Andromeda creative diversity, Structure, Audience
- **audit-creative**: cross-platform creative quality with Andromeda Entity-ID and Symphony awareness
- **audit-tracking**: conversion tracking + privacy infrastructure (Consent Mode V2, CAPI, Events API, AdAttributionKit)
- **audit-budget**: budget and bidding across LinkedIn, TikTok, Microsoft
- **audit-compliance**: compliance, settings, performance benchmarks across all platforms

Generates a unified **Ads Health Score (0-100)** with prioritized action plan.

> **Wave 2 standalone sub-skills.** `/ads audit` parallel-delegates the 6 agents above. Amazon, attribution, and server-side tracking are standalone sub-skills (`/ads amazon`, `/ads attribution`, `/ads tracking`); invoke them directly. Wave 3 will add their paired audit agents.

<p align="center">
  <img src="assets/diagrams/02-pipeline-A.svg" alt="Audit pipeline: stage-by-stage execution from data intake through parallel sub-agent dispatch to scored report output" width="100%">
</p>

<p align="center">
  <img src="assets/diagrams/19-audit-lifecycle.svg" alt="Audit Lifecycle" width="100%">
</p>

### `/ads plan <business-type>`
**Strategic Ad Planning**

Industry templates with platform mix, campaign architecture, creative strategy, targeting, budget guidelines, and KPI targets.

**Supported business types:**
- `saas`: Trial/demo focus, Google + LinkedIn primary
- `ecommerce`: Shopping/PMax, ROAS-focused, seasonal
- `local-service`: Google Search + LSA, call tracking, geo radius
- `b2b-enterprise`: LinkedIn ABM, long sales cycle, pipeline metrics
- `info-products`: Meta + YouTube, webinar/VSL funnels
- `mobile-app`: Meta + Google UAC, MMP required, LTV:CPI
- `real-estate`: Special Ad Category (housing), buyer/seller campaigns
- `healthcare`: HIPAA compliance, LegitScript, restricted targeting
- `finance`: Special Ad Category (credit), required disclosures
- `agency`: Multi-client management, reporting framework
- `generic`: Universal template with platform selection questionnaire

<p align="center">
  <img src="assets/diagrams/08-industry-templates.svg" alt="Industry Templates" width="100%">
</p>

### `/ads math` and `/ads test`

<p align="center">
  <img src="assets/diagrams/18-ppc-calculators.svg" alt="PPC Calculators" width="48%">
  <img src="assets/diagrams/17-ab-testing.svg" alt="A/B Test Design" width="48%">
</p>

### `/ads report`

PDF audit reports for client deliverables: health score gauge, platform comparison charts, pass/fail distribution, formatted tables, zero-overlap layout.

<p align="center">
  <img src="assets/diagrams/16-pdf-pipeline.svg" alt="PDF Report Pipeline" width="100%">
</p>

## Features: what 250+ audit checks cover

What every check actually does: catches the platform-specific blind spots that cost you spend. Andromeda creative-similarity suppression on Meta. Negative-keyword discipline gaps on Google AI Max. Andromeda-aware creative diversity scoring. AdAttributionKit configurable-window gaps on Apple. ACOS/TACOS targets misaligned with margin on Amazon. Consent Mode V2 missing on the landing page (silent revenue leak). These are the items a manual audit misses because the analyst is mostly checking what *used* to matter, not what platforms changed in 2026.

### Coverage by platform

| Platform | Checks | Key areas |
|----------|--------|-----------|
| Google Ads | 80 | Search, PMax, AI Max (`ai_max_setting`, AI Brief, FUE), Demand Gen, CTV, YouTube |
| Meta Ads | 50 | Pixel/CAPI, Andromeda + GEM + Lattice, Entity-ID clustering, ASC/AAC, Structure, Audience |
| LinkedIn Ads | 27 | B2B targeting, TLA, Lead Gen, CRM integration |
| TikTok Ads | 28 | Creative-first, Smart+, GMV Max, Search Ads, Events API (post-USDS) |
| Microsoft Ads | 24 | Google import safety, Copilot, CTV, LinkedIn targeting, video |
| Apple Ads | 35+ | Campaign structure, CPPs, Maximize Conversions, AdAttributionKit |
| Amazon Ads | 30+\* | Sponsored Products / Brands / Display, ACOS / TACOS, search-term harvesting |
| Cross-platform | 3 | Privacy infrastructure, creative diversity, refresh cadence |
| Attribution + server-side | 25+\* | AdAttributionKit, GA4, Consent Mode V2, sGTM, CAPI Gateway, hash quality |

> \* **Verified vs estimated.** The 209 checks for Google (80), Meta (50), LinkedIn (27), TikTok (28), and Microsoft (24) are bidirectionally verified against `tests/fixtures/check-catalog.yaml`; they can't drift without failing CI. Apple, Amazon, Cross-platform, and Attribution + Server-side counts are inline thresholds in their respective SKILL.md files; corresponding audit reference files + catalog entries land in Wave 3.

<p align="center">
  <img src="assets/diagrams/15-platform-grid.svg" alt="Platform Coverage Grid" width="100%">
</p>

<p align="center">
  <img src="assets/diagrams/04-platform-checks.svg" alt="Platform Check Distribution" width="100%">
</p>

### Ads Health Score (0-100)

Weighted scoring algorithm with severity multipliers:

| Grade | Score | Action required |
|-------|-------|-----------------|
| A | 90-100 | Minor optimizations only |
| B | 75-89 | Some improvement opportunities |
| C | 60-74 | Notable issues need attention |
| D | 40-59 | Significant problems present |
| F | <40 | Urgent intervention required |

<p align="center">
  <img src="assets/diagrams/04-scoring-weights-B.svg" alt="Scoring weight breakdown: donut chart showing the 9 audit categories that compose the 100-point Ads Health Score, with per-platform legend" width="100%">
</p>

### Industry detection

Auto-detects business type from ad account signals (product feeds, conversion events, platform mix, targeting patterns) and loads industry-specific benchmarks and templates.

### Quality gates

Hard rules enforced during every audit:
- Never recommend Broad Match without Smart Bidding (Google)
- 3x Kill Rule: flag CPA >3x target for immediate pause
- Budget sufficiency: Meta ≥5x CPA/ad set, TikTok ≥50x CPA/ad group
- Learning phase protection: no edits during active learning
- Compliance: auto-check Special Ad Categories (housing/credit/finance)
- **Privacy infrastructure gate**: verify tracking stack (Consent Mode V2, CAPI, Events API, AdAttributionKit) before optimization recommendations
- **Andromeda creative diversity**: flag Meta accounts with <10 genuinely distinct creatives

<p align="center">
  <img src="assets/diagrams/05-quality-gates.svg" alt="Quality Gates" width="100%">
</p>

### Creative pipeline

AI-powered creative generation with 4 specialized agents (`/ads dna` → `/ads create` → `/ads generate` → `/ads photoshoot`).

<p align="center">
  <img src="assets/diagrams/14-creative-pipeline.svg" alt="Creative Pipeline" width="100%">
</p>

### Reference data

26 built-in reference files with 2026-current benchmarks, bidding decision trees, platform specifications, compliance requirements, conversion tracking guides, MCP integration guide, and platform coverage notes.

### 10-Principle Thinking Framework

Every audit, plan, and creative output runs under a shared cognitive discipline: **OBSERVE × 2 / LISTEN / THINK / CONNECT × 2 / FEEL / ACCEPT / CREATE / GROW**. Maps each principle to concrete ad-work behavior, the anti-pattern that signals you're skipping it, and the workflow stage where it dominates. It's the difference between a list of red flags and a strategic deliverable. Defined in [`ads/references/thinking-framework.md`](ads/references/thinking-framework.md).

### Data handling & privacy

Runs entirely on your local machine via Claude Code. No ad account data is sent to external servers. When using MCP servers for live API access, data flows directly between your machine and the platform APIs. All analysis happens locally.

<p align="center">
  <img src="assets/diagrams/12-privacy-flow.svg" alt="Privacy and Data Flow" width="100%">
</p>

## Compared to manual / agency / commercial tools

| | Manual audit | Agency engagement | Commercial PPC audit tool | **Claude Ads** |
|---|---|---|---|---|
| **Time per audit** | 4-6 hrs senior PPC time | 1-2 weeks turnaround | 5-30 min | **10-15 min** |
| **Cost** | High (billable hours) | $2k-$10k+ project | $99-$799/mo subscription | **Free skill + Claude Code subscription** |
| **Repeatable** | Inconsistent across analysts | Inconsistent across accounts | Yes | **Yes, deterministic + scriptable** |
| **Output format** | Wall-of-findings PDF | Branded slide deck | Web dashboard, exports | **JSON + PDF, local files** |
| **Custom benchmarks** | Manual | Manual | Vendor-fixed | **Edit local SKILL.md** |
| **Data leaves machine?** | No (your spreadsheet) | Yes (sent to agency) | Yes (uploaded to vendor) | **No, fully local** |
| **Lock-in** | None | High | High (data exit cost) | **None (MIT, your files)** |
| **Andromeda / AI Max / AdAttributionKit awareness** | Depends on analyst | Depends on agency seniority | Lagging (typically 6-12 mo behind) | **Andromeda (Oct 2025), AI Max (May 2025), AdAttributionKit + WWDC25 configurable windows, Consent Mode V2** |

> Cost benchmarks: manual audit assumes a senior PPC consultant at typical agency billable rates; agency engagement based on common discovery/audit deliverable scopes; commercial-tool subscriptions reflect published mid-tier pricing across the PPC audit category. Your numbers may differ.

## Use cases

**Agency lead running 12 client accounts.** Replaces the quarterly "deep audit" ritual with a weekly Monday morning `/ads audit` run per account. Time to deliver a client health-score email drops from 4 hours to 12 minutes; coverage goes from quarterly to weekly without billing more hours.

**In-house marketer at a 50-person SaaS company.** Runs `/ads audit` 24 hours before quarterly business reviews. Catches the items the platform UI buries (broken conversion goals, ASC budget starvation, missing Andromeda creative diversity) before the CMO asks "why is CAC up?" in front of the board.

**Freelance PPC consultant onboarding a new client.** Runs `/ads audit` on the discovery call. Anchors the engagement scope with a real 0-100 score and 3 prioritized critical findings instead of a vague "I'll take a look and get back to you." Closes more retainers because the proof of value happens before the proposal.

## Eval harness: verified rigor

**41 tests, 41 passing, CI on every commit.** Pytest suite in `tests/`:

- **Routing snapshots**: every documented trigger phrase routes to its expected sub-skill (catches description regressions)
- **Check-catalog coverage**: bidirectional check between `tests/fixtures/check-catalog.yaml` (209 IDs) and every audit reference file; no orphan IDs, no untracked rows
- **Scoring math**: re-implements the weighted-score algorithm; asserts determinism across 10 runs and correct severity weighting
- **SSRF regression suite**: 27 IPv4/IPv6 blocklist cases, non-HTTP scheme blocks, DNS fail-closed, credential redaction

Rare among Claude Code skills. Makes the project auditable end-to-end and prevents claim-vs-reality drift between releases.

## Architecture

<p align="center">
  <img src="assets/diagrams/01-architecture-B.svg" alt="System architecture: left-to-right pipeline from /ads audit invocation through orchestrator routing, sub-skill execution, and report synthesis" width="100%">
</p>

<p align="center">
  <img src="assets/diagrams/03-sub-skill-map-B.svg" alt="Sub-skill ecosystem: 22 modules organized as concentric rings, platform sub-skills inner, cross-cut and strategy and creative sub-skills outer" width="100%">
</p>

```
~/.claude/skills/ads/              # Main orchestrator
~/.claude/skills/ads/references/   # 26 RAG reference files
~/.claude/skills/ads-*/            # 22 sub-skills (incl. ads-math, ads-test, ads-amazon, ads-attribution, ads-server-side-tracking)
~/.claude/skills/ads-plan/assets/  # 12 industry templates
~/.claude/agents/                  # 10 agents (6 audit + 4 creative)
~/.claude/skills/ads/tests/        # 41-test pytest eval harness (Wave 2)
```

### How it works

1. **Orchestrator** (`/ads`) routes commands to specialized sub-skills
2. **Sub-skills** provide deep single-domain analysis with structured output
3. **Agents** run in parallel during full audits for maximum speed
4. **References** load on-demand (RAG pattern); only what's needed per analysis
5. **Templates** provide industry-specific strategy frameworks

## How it analyzes your ads

**Claude Ads works with data you provide**: exports, screenshots, or pasted metrics from your ad platform dashboards. It does not connect to any ad platform API automatically.

**To get accurate, account-specific recommendations:**
1. Export your account data (last 30 days recommended)
2. Run the relevant command: `/ads google`, `/ads audit`, etc.
3. Claude will ask for your industry and budget context first; provide these for relevant benchmarks
4. Paste or share your data when prompted

<p align="center">
  <img src="assets/diagrams/07-data-flow.svg" alt="Data Flow" width="100%">
</p>

### Live data integration (optional)

For direct API access without manual exports, pair Claude Ads with MCP servers. See [`ads/references/mcp-integration.md`](ads/references/mcp-integration.md) for setup:
- **Google Ads**: [mcp-google-ads](https://github.com/cohnen/mcp-google-ads), 29 GAQL tools for live API access
- **Meta Ads**: [Adspirer MCP](https://www.adspirer.com) (commercial); self-hosted option = wrap Meta Marketing API and feed JSON into the standard data-collection flow
- **LinkedIn Ads**: [GrowthSpree MCP](https://www.growthspreeofficial.com) or [Adzviser MCP](https://adzviser.com)

<p align="center">
  <img src="assets/diagrams/10-mcp-integration.svg" alt="MCP Integration" width="100%">
</p>

## FAQ

<details>
<summary><b>Can Claude Ads log into my ad manager automatically?</b></summary>

No. Claude Ads analyzes data you provide (exports, screenshots, or pasted metrics). It doesn't connect to ad platforms automatically. See the [Live data integration](#live-data-integration-optional) section for Google Ads API access via MCP.
</details>

<details>
<summary><b>Does it use real account data or generic benchmarks?</b></summary>

Both. Your account data drives the audit; industry benchmarks (from research covering thousands of campaigns) provide the comparison floor and ceiling. Benchmarks are averages; results vary by industry, budget level, and account maturity. Always provide your industry and monthly spend up front for the most relevant comparisons.
</details>

<details>
<summary><b>Is ad posting or campaign creation still manual?</b></summary>

Yes. Claude Ads is an audit and strategy tool. It finds issues, recommends fixes, and builds campaign plans, but creating, editing, or posting ads remains manual in your ad platform.
</details>

<details>
<summary><b>Why do some recommendations seem off for my account size?</b></summary>

Benchmarks and best practices differ significantly between a $500/month account and a $50k/month account. Tell Claude your budget upfront: *"I spend $2k/month on Google Ads for a local plumbing business"* gives much better results than running `/ads google` cold.
</details>

<details>
<summary><b>Does it support [platform] ads?</b></summary>

Currently supported: Google, Meta (Facebook/Instagram), YouTube, LinkedIn, TikTok, Microsoft/Bing, Apple, and Amazon. Additional platforms (Reddit, CTV/OTT, Pinterest, Snapchat) are covered in `ads/references/additional-platforms.md` for strategic planning.
</details>

<details>
<summary><b>How does it score financial KPIs like ROAS, CPA, ACOS, TACOS, LTV:CAC?</b></summary>

Use `/ads math` for the financial calculator (CPA, ROAS, CPL, break-even analysis, impression-share opportunity sizing, budget forecasting, LTV:CAC ratio, MER). The full audit (`/ads audit`) automatically benchmarks your reported ROAS / CPA / CPL against industry-specific targets loaded from `ads/references/benchmarks.md`. For Amazon, `/ads amazon` scores ACOS and TACOS against category benchmarks and flags products where TACOS exceeds your contribution margin.
</details>

<details>
<summary><b>What's the maintenance & support commitment?</b></summary>

Single maintainer (see [Maintainer](#maintainer)). Bug reports and issues filed via GitHub get a response within 48 hours on the public repo; faster for Pro community members via the [Skool community](https://www.skool.com/ai-marketing-hub-pro). No SLA on feature requests; those go through the public roadmap. CI runs the full eval harness on every commit, so regressions are caught before they ship.
</details>

<details>
<summary><b>Does my data leave my machine?</b></summary>

No. The skill runs locally in Claude Code. When you opt into a live MCP integration (e.g. mcp-google-ads), data flows directly from your machine to the platform API, never through claude-ads infrastructure (there is none).
</details>

<details>
<summary><b>How is this different from a commercial PPC audit tool?</b></summary>

Three things: (1) local-first, no data uploaded anywhere; (2) MIT-licensed and forkable: you can edit the audit checks; (3) it tracks 2026-current platform changes (Andromeda, AI Max, AdAttributionKit) that commercial tools often lag 6-12 months behind on.
</details>

<details>
<summary><b>Can I use this for client work as an agency?</b></summary>

Yes. MIT license. White-label the PDF reports via the `/ads report` template. The `/ads plan agency` template is built for multi-client management. The community private mirror at AI-Marketing-Hub ships ahead of public releases for Pro members.
</details>

## Requirements

- Claude Code CLI
- Python 3.10+ with Playwright (optional, for live landing page analysis)
- reportlab (optional, for PDF report generation via `/ads report`)

## Uninstall

### Unix/macOS/Linux

```bash
curl -fsSL https://raw.githubusercontent.com/AI-Marketing-Hub/claude-ads/main/uninstall.sh | bash
```

### Windows PowerShell

```powershell
irm https://raw.githubusercontent.com/AI-Marketing-Hub/claude-ads/main/uninstall.ps1 | iex
```

## Roadmap

<p align="center">
  <img src="assets/diagrams/05-roadmap-A.svg" alt="Wave roadmap: 12-month timeline from v1.5 stable through v1.7.x Wave 2 to v1.8.0 visual system and v2.0 multi-tenant" width="100%">
</p>

The 12-month delivery cadence from v1.5 stable through Wave 2 (v1.7.x, current) to Wave 3 (v1.8.0+, in active development on the private repo). Full per-release detail in [CHANGELOG.md](CHANGELOG.md).

## Project info

- [CHANGELOG](CHANGELOG.md): release history with full Wave 2 notes (v1.7.0 + v1.7.1)
- [CONTRIBUTING](CONTRIBUTING.md): bug reports, feature requests, sub-skill templates, testing discipline
- [CODE OF CONDUCT](CODE_OF_CONDUCT.md): Contributor Covenant
- [SECURITY](SECURITY.md): vulnerability disclosure, outbound network destinations table, error sanitization
- [SUPPORT](SUPPORT.md): where to ask for help

## Related projects

- [Claude SEO](https://github.com/AgriciDaniel/claude-seo): comprehensive SEO analysis skill for Claude Code

> Looking for the other version of this skill? See the [Two versions of this skill](#claude-ads-paid-advertising-audit-skill-for-claude-code) callout at the top of this README.

## Maintainer

Built by **[Agrici Daniel](https://agricidaniel.com/about)**: AI Workflow Architect. Single maintainer, open to community contributions via the [Pro Skool community](https://www.skool.com/ai-marketing-hub-pro).

- [Blog](https://agricidaniel.com/blog): deep dives on AI marketing automation
- [AI Marketing Hub (free)](https://www.skool.com/ai-marketing-hub): open community
- [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro): Pro community, early access to this skill
- [YouTube](https://www.youtube.com/@AgriciDaniel): tutorials and demos
- [All open-source tools](https://github.com/AgriciDaniel): public profile

## Star history

<a href="https://star-history.com/#AgriciDaniel/claude-ads&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=AgriciDaniel/claude-ads&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=AgriciDaniel/claude-ads&type=Date" />
    <img alt="Star history of AgriciDaniel/claude-ads on GitHub" src="https://api.star-history.com/svg?repos=AgriciDaniel/claude-ads&type=Date" />
  </picture>
</a>

If Claude Ads saves you time, a star on the [public repo](https://github.com/AgriciDaniel/claude-ads) is the easiest way to say thanks (and helps other PPC folks find it).

## License

MIT. See [LICENSE](LICENSE) for details.
