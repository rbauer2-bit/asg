# AUTHORITY SYSTEMS GROUP™
## Reference File — CLAUDE_REFERENCE.md
### Internal Use Only. Load on demand — not required for every task.

This file holds detail that CLAUDE.md links to but does not need to carry. Read specific sections when the task requires them.

---

## VICTOR HALE — MARKET INTELLIGENCE DIVISION

**Victor Hale, Director of Market Intelligence** (reports to Iris Nolan, CTO + Daniel Frost, CSO)

Two modes — same underlying skill files, different output framing:

| Mode | Purpose | Orchestrator |
|---|---|---|
| `PROSPECTING` | Branded Digital Authority Assessment delivered to prospects as a value-first engagement tool. The audit IS the pitch. | `/skills/website-audit/WEBSITE_AUDIT_ORCHESTRATOR.md` |
| `ANALYSIS` | Internal marketing intelligence and client deliverables via the /market command suite. | `/skills/audit/MARKET_AUDIT_ORCHESTRATOR.md` |

**Victor's 5 Specialists:**

| Specialist | Domain | Skill File |
|---|---|---|
| Lena Park | Content & Messaging Analysis | `skills/audit/agents/content-analyst.md` |
| Marcus Cole | Conversion Rate Optimization | `skills/audit/agents/cro-specialist.md` |
| Reid Foster | Competitive Intelligence | `skills/audit/agents/competitive-intelligence.md` |
| Anika Suri | Technical SEO & Digital Infrastructure | `skills/audit/agents/technical-seo.md` |
| Clay Donovan | Brand & Growth Strategy | `skills/audit/agents/brand-growth.md` |

**PROSPECTING invocation:**
```
Requires: Target URL + business name + niche + geography
Output: Scored Digital Authority Assessment (13 sections + executive summary + priority action plan)
```

**ANALYSIS — /market command suite:**

| Command | What It Does | Output File |
|---|---|---|
| `/market audit <url>` | Full marketing audit — all 5 specialists, scored 0–100 | `MARKETING-AUDIT.md` |
| `/market quick <url>` | 60-second marketing snapshot | Terminal output |
| `/market copy <url>` | Copy analysis with before/after rewrites | `COPY-SUGGESTIONS.md` |
| `/market emails <topic>` | Complete email sequences | `EMAIL-SEQUENCES.md` |
| `/market social <topic>` | 30-day social content calendar | `SOCIAL-CALENDAR.md` |
| `/market ads <url>` | Ad creative and copy for all platforms | `AD-CAMPAIGNS.md` |
| `/market funnel <url>` | Sales funnel analysis and optimization | `FUNNEL-ANALYSIS.md` |
| `/market competitors <url>` | Competitive intelligence report | `COMPETITOR-REPORT.md` |
| `/market landing <url>` | Landing page CRO analysis | `LANDING-CRO.md` |
| `/market launch <product>` | Product/service launch playbook | `LAUNCH-PLAYBOOK.md` |
| `/market proposal <client>` | Client proposal generator | `CLIENT-PROPOSAL.md` |
| `/market report <url>` | Full marketing report (Markdown) | `MARKETING-REPORT.md` |
| `/market report-pdf <url>` | Full marketing report (PDF) | `MARKETING-REPORT.pdf` |
| `/market seo <url>` | SEO content audit | `SEO-AUDIT.md` |
| `/market brand <url>` | Brand voice analysis and guidelines | `BRAND-VOICE.md` |

**Cross-team integration after any audit:**
- Messaging findings → Vivienne Carr (CMO)
- Competitive findings → Daniel Frost (CSO)
- Technical findings → Iris Nolan (CTO)
- Conversion findings → Tanya Blackwood (CRO)

---

## AUTHORITY BLUEPRINT™ — SKILL-BY-SKILL ROUTING

The Authority Blueprint™ is assembled from these skills in order. Every skill must complete before the document assembles.

| Section | Skill File | Voice |
|---|---|---|
| 1: Executive Summary | `/skills/leadership/EXECUTIVE_SUMMARY.md` | Roger |
| 2: Director's Briefing | `/skills/leadership/EXECUTIVE_SUMMARY.md` | Roger |
| 3: Market Analysis | `/skills/strategy/MARKET_ANALYSIS.md` | Daniel Frost, CSO |
| 4: Belief-to-Buy Framework™ Map | `/skills/strategy/BELIEF_FILTER_MAP.md` | Dr. Cross + Vivienne Carr |
| 5: 1-Year Strategic Plan | `/skills/strategy/STRATEGIC_PLAN_1YR.md` | Daniel Frost, CSO |
| 6: Fast Cash Sprint™ | `/skills/revenue/FAST_CASH_STRATEGY.md` | Tanya Blackwood, CRO |
| 7: KPI Dashboard | `/skills/strategy/KPI_FRAMEWORK.md` | Preston Adler, COO |
| 8: Content Authority Strategy™ | `/skills/content/CONTENT_STRATEGY.md` | Vivienne Carr, CMO |
| 9: Niche Website Strategy | `/skills/digital/NICHE_WEBSITE_STRATEGY.md` | Iris Nolan, CTO |
| 10: Email Sequences (fully written) | `/skills/email/EMAIL_SEQUENCES.md` | Vivienne Carr, CMO |
| 11: Lead Magnet & Referral Program | `/skills/content/LEAD_MAGNET_AND_REFERRAL_PROGRAM.md` | Vivienne Carr + Tanya Blackwood |
| 12: Priority Services & Next Steps | `/skills/output/PRIORITY_SERVICES_AND_NEXT_STEPS.md` | Preston Adler, COO |
| 13: QC Gate Sign-Offs | `/brand-standards/QUALITY_CHECKLIST.md` | All four gate owners |

Assembly and formatting: `/skills/output/REPORT_FORMATTER.md`
DOCX generation: `build_docx.py` (run after markdown is complete)

Quality standard: The Blueprint floor is set by `anna-aleksander-law_authority-blueprint_20260302`. Every subsequent Blueprint must be at least as thorough.

---

## CALENDAR TEAM — SKILL ROUTING

Managed by Sloane Mercer, Calendar Director. Runs the Authority Engine™ content calendar system.

| Role | Skill File | Frequency |
|---|---|---|
| Calendar Team Orchestrator | `/skills/calendar/CALENDAR_TEAM_ORCHESTRATOR.md` | On demand — manages full team flow |
| Strategy Coordinator (Nadia Voss) | `/skills/calendar/STRATEGY_COORDINATOR.md` | Once per month per client |
| Content Coordinator (Caleb Navarro) | `/skills/calendar/CONTENT_COORDINATOR.md` | Once per week |
| Content Writer (Lena Ashby) | `/skills/calendar/CONTENT_WRITER.md` | Once per day / content piece |

Orchestrator modes: Full Monthly Cycle | Weekly Content Block | Single Day Content | Revision Cycle
Output flow: Monthly Theme Brief → Weekly Draft Packages → Approved content ready for publishing

---

## DIGITAL SYSTEMS DIVISION

**Marcus Chen, CRM Automation Builder** (reports to Iris Nolan, CTO)
Builds live automation systems — working configurations inside the client's actual CRM. Not strategies or blueprints — actual builds.

Skill file: `/skills/automation/CRM_AUTOMATION_BUILDER.md`
Persona: `/personas/digital-team/chen-marcus-crm-automation-builder.md`

Workflow: Email copy (Rhett or Tomás) + Iris Nolan automation blueprint → Marcus Chen builds. Chen builds; Nolan architects.

---

## REVENUE DIVISION — PAID MEDIA

**Jordan Merritt, Paid Media Specialist** (reports to Tanya Blackwood, CRO)
Google Ads, Meta Ads, LinkedIn Ads. Campaigns for clients who are ready for the amplification layer.

Skill file: `/skills/revenue/PAID_MEDIA_SPECIALIST.md`
Persona: `/personas/revenue-team/merritt-jordan-paid-media-specialist.md`

Workflow: Website copy conversion-ready (Audrey Voss) + tracking confirmed (Marcus Chen) + follow-up system active (Marcus Chen) → Jordan runs paid. Paid media does not precede the foundation.

---

## CONTENT TEAM ROSTER

Full team: `/personas/content-team/CONTENT_TEAM_ROSTER.md`
Audit team: `/personas/audit-team/AUDIT_TEAM_ROSTER.md`
Calendar team: `/personas/calendar-team/CALENDAR_TEAM_ROSTER.md`
Digital team: `/personas/digital-team/DIGITAL_TEAM_ROSTER.md`
Revenue team: `/personas/revenue-team/REVENUE_TEAM_ROSTER.md`

---

*Authority Systems Group™ — Internal Reference Document*
*Created: 2026-03-08 | Extracted from CLAUDE.md v3.0 for performance optimization*
