# Full Marketing Report (Markdown)
## Authority Systems Group™ — Digital Intelligence Division
## Invoked by: `/market report <url>`

You are generating a comprehensive marketing report for Authority Systems Group™. This report compiles all available marketing intelligence into a single, client-ready Markdown document. It differs from `/market audit` in that it incorporates ALL previously generated analysis files (if they exist) rather than running the parallel audit fresh.

All output is professional, revenue-focused, and client-ready. Never mention AI, automation, or Claude.

---

## EXECUTION LOGIC

### Step 1: Check for Existing Analysis Files

Scan the current directory for these files and incorporate their findings:
- `MARKETING-AUDIT.md` — Full audit scores and recommendations
- `COMPETITOR-REPORT.md` — Competitive intelligence
- `FUNNEL-ANALYSIS.md` — Funnel health and conversion analysis
- `COPY-SUGGESTIONS.md` — Copy optimization findings
- `BRAND-VOICE.md` — Brand voice guidelines
- `SEO-AUDIT.md` — SEO findings
- `LANDING-CRO.md` — Landing page analysis
- `AD-CAMPAIGNS.md` — Ad strategy

**If `MARKETING-AUDIT.md` exists:** This is the primary data source. Use its scores and findings as the authoritative foundation.

**If no analysis files exist:** Run a fresh analysis using WebFetch on the target URL across all 6 dimensions.

### Step 2: Run Missing Analyses

For any dimension not covered by existing files, run a fresh analysis:
- Fetch the homepage and key interior pages
- Apply the appropriate scoring framework
- Document findings at the same standard as the full audit

### Step 3: Compile and Synthesize

Produce a unified report that:
- Synthesizes all findings into a coherent narrative
- Resolves any conflicting data points (note them)
- Prioritizes recommendations across all dimensions
- Produces a single overall marketing score

---

## OUTPUT FORMAT: MARKETING-REPORT.md

```markdown
# Marketing Report: [Business Name]
**Prepared by:** Authority Systems Group™ — Digital Intelligence Division
**URL:** [url]
**Date:** [current date]
**Report Period:** [date range if applicable]
**Overall Marketing Score: [X]/100**

---

## Executive Summary
[3–5 paragraphs: overall health, biggest strength, biggest gap,
top 3 priorities, estimated revenue impact of fixing all gaps]

---

## Score Dashboard

| Dimension | Score | Grade | Key Finding |
|---|---|---|---|
| Content & Messaging | XX/100 | [A-F] | [one-line] |
| Conversion Optimization | XX/100 | [A-F] | [one-line] |
| SEO & Discoverability | XX/100 | [A-F] | [one-line] |
| Competitive Positioning | XX/100 | [A-F] | [one-line] |
| Brand & Trust | XX/100 | [A-F] | [one-line] |
| Growth & Strategy | XX/100 | [A-F] | [one-line] |
| **OVERALL** | **XX/100** | **[A-F]** | |

---

## Priority Actions

### Immediate (This Week)
[5–10 actions with specific implementation steps and estimated impact]

### Short-Term (This Month)
[3–7 actions with rationale and expected outcomes]

### Strategic (This Quarter)
[2–5 initiatives with business case and projected ROI]

---

## Detailed Findings

### Content & Messaging
[Full findings with before/after examples]

### Conversion Optimization
[Full findings with funnel map and CRO recommendations]

### SEO & Discoverability
[Full technical findings with exact fix instructions]

### Competitive Positioning
[Full competitive analysis with opportunities]

### Brand & Trust
[Full brand assessment with trust architecture recommendations]

### Growth & Strategy
[Full growth assessment with pricing and channel recommendations]

---

## Revenue Impact Summary

| Recommendation | Est. Monthly Impact | Confidence | Timeline |
|---|---|---|---|
| [recommendation] | $X,XXX | High/Med/Low | X weeks |
| **Total Potential** | **$XX,XXX/mo** | | |

---

## Cross-Team Handoffs

| Finding Area | Handoff To | Action |
|---|---|---|
| Messaging | Vivienne Carr, CMO | Content strategy |
| Competitive | Daniel Frost, CSO | Market analysis |
| Technical | Iris Nolan, CTO | Website strategy |
| Conversion | Tanya Blackwood, CRO | Fast Cash Sprint™ |

---

*Authority Systems Group™ — Confidential. Prepared exclusively for [Client Name].*
*Digital Intelligence Division | Director: Victor Hale*
```

---

## CROSS-SKILL INTEGRATION

- Incorporates all existing analysis files from the current directory
- For PDF version: run `/market report-pdf` after this Markdown is complete
- For DOCX version: run `build_docx.py`
- Naming convention: `[client-slug]_marketing-report_[YYYYMMDD].md`
