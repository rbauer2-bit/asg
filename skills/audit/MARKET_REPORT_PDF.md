# MARKET_REPORT_PDF.md
# Authority Systems Group™ — Digital Intelligence Division
# Skill: PDF Marketing Report Generator
# Invoked by: Cait Brennan (Analytics & Tracking) | Victor Hale (Digital Intelligence Director)
# Status: ACTIVE — Updated 2026-03-06

---

## PURPOSE

Generate a professional, visually polished PDF marketing report branded to Authority Systems Group™ standards. This skill collects all available audit and analysis data, structures it into the expected JSON format, invokes `scripts/generate_pdf_report.py`, and produces a client-ready PDF with score gauges, bar charts, comparison tables, findings, and a prioritized action plan.

---

## VOICE

Victor Hale, Director of Digital Intelligence
See: `/personas/audit-team/hale-victor-audit-director.md`

---

## WHEN TO USE

- User wants a PDF version of the marketing report (not just Markdown)
- User is preparing a deliverable for a client presentation
- User asks for a "polished report", "client-ready report", or "PDF report"
- User wants a visual report with charts and scores
- Triggered by `/market report-pdf` or `/market report-pdf <domain>`

## PDF vs Markdown Decision Guide

| Format | Best For | Pros | Cons |
|---|---|---|---|
| **PDF** | Client presentations, email attachments, prospecting outreach | Professional appearance, consistent formatting, visual charts, ASG branding | Harder to edit, requires Python script |
| **Markdown** | Internal use, quick reference, iterative editing, version control | Easy to edit, readable in any editor | Less visually polished, no charts |

**Rule of thumb:** If the report is going to a client or prospect, use PDF. If it is for internal use or further editing, use Markdown.

---

## INPUTS REQUIRED

- Target URL
- Business name (for cover page and competitor table)
- Any previously generated audit files in the project directory

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PROMPT
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**STATUS: ACTIVE** — Updated 2026-03-06

---

### STEP 1: COLLECT ALL AVAILABLE DATA

Gather data from all previous skill runs. Check for these files in the project directory:

**Primary data sources:**
- `MARKETING-AUDIT.md` — Overall audit results
- `LANDING-CRO.md` — Landing page conversion analysis
- `SEO-AUDIT.md` — SEO findings
- `BRAND-VOICE.md` — Brand voice analysis
- `COMPETITOR-ANALYSIS.md` — Competitor comparison data
- `FUNNEL-ANALYSIS.md` — Funnel analysis
- `SOCIAL-AUDIT.md` — Social media audit
- `EMAIL-AUDIT.md` — Email marketing audit
- `AD-AUDIT.md` — Advertising audit

**If no previous data exists:**
1. Recommend the user run `/market audit <url>` first for best results
2. If the user insists on generating without prior audits, analyze the provided URL directly and build the data structure from scratch
3. Use `python scripts/analyze_page.py <url>` to gather automated data

---

### STEP 2: BUILD THE JSON DATA STRUCTURE

The `scripts/generate_pdf_report.py` script expects a JSON file with this exact structure:

```json
{
  "url": "https://example.com",
  "date": "March 6, 2026",
  "brand_name": "Example Co",
  "overall_score": 62,
  "executive_summary": "A 2-4 sentence summary of the overall marketing health, key opportunities, and estimated revenue impact of implementing recommendations.",
  "categories": {
    "Content & Messaging": {
      "score": 68,
      "weight": "25%"
    },
    "Conversion Optimization": {
      "score": 52,
      "weight": "20%"
    },
    "SEO & Discoverability": {
      "score": 74,
      "weight": "20%"
    },
    "Competitive Positioning": {
      "score": 48,
      "weight": "15%"
    },
    "Brand & Trust": {
      "score": 70,
      "weight": "10%"
    },
    "Growth & Strategy": {
      "score": 55,
      "weight": "10%"
    }
  },
  "findings": [
    {
      "severity": "Critical",
      "finding": "Description of the most important finding — specific, evidence-based, quantified"
    },
    {
      "severity": "High",
      "finding": "Description of a high-priority finding"
    },
    {
      "severity": "Medium",
      "finding": "Description of a medium-priority finding"
    },
    {
      "severity": "Low",
      "finding": "Description of a lower-priority finding"
    }
  ],
  "quick_wins": [
    "First quick win action item — specific and actionable",
    "Second quick win action item",
    "Third quick win action item"
  ],
  "medium_term": [
    "First medium-term action item",
    "Second medium-term action item",
    "Third medium-term action item"
  ],
  "strategic": [
    "First strategic action item",
    "Second strategic action item",
    "Third strategic action item"
  ],
  "competitors": [
    {
      "name": "Competitor A",
      "positioning": "Their market position",
      "pricing": "Their pricing model",
      "social_proof": "Their trust signals",
      "content": "Their content approach"
    },
    {
      "name": "Competitor B",
      "positioning": "Their market position",
      "pricing": "Their pricing model",
      "social_proof": "Their trust signals",
      "content": "Their content approach"
    }
  ]
}
```

---

### STEP 3: FIELD-BY-FIELD DATA ASSEMBLY GUIDE

#### `url` (string, required)
The target website URL. Use the full URL including protocol.

#### `date` (string, required)
The report generation date. Format: "Month DD, YYYY" (e.g., "March 6, 2026").

#### `brand_name` (string, required)
The company or brand name. Used in the cover header and competitor comparison table.

#### `overall_score` (integer, 0–100, required)
The weighted average of all category scores. Calculate as:
```
overall_score = (content * 0.25) + (conversion * 0.20) + (seo * 0.20) + (competitive * 0.15) + (brand * 0.10) + (growth * 0.10)
```
Round to the nearest whole number. Decimals imply false precision.

#### `executive_summary` (string, required)
2–4 sentences covering:
- Current marketing health assessment
- Top 1–2 most impactful findings
- Estimated revenue impact of implementing recommendations
- Recommended first step

Keep it tight. This appears on the cover page directly below the score gauge. Clients skim cover pages.

#### `categories` (object, required)
Exactly 6 categories with their scores. Scoring guidance:

| Category | What It Measures | Scoring |
|---|---|---|
| Content & Messaging | Copy quality, value proposition, headline clarity, CTA text, brand voice | 80+: Clear, benefit-driven, specific. 60–79: Adequate but generic. <60: Vague, feature-focused |
| Conversion Optimization | Social proof, form design, CTA placement, objection handling, urgency | 80+: Multiple proof types, optimized forms. 60–79: Some elements. <60: Missing critical elements |
| SEO & Discoverability | Title tags, meta descriptions, headers, schema, internal linking, page speed | 80+: Fully optimized. 60–79: Mostly present. <60: Major gaps |
| Competitive Positioning | Differentiation, pricing clarity, comparison content, market awareness | 80+: Clear positioning, comparison pages. 60–79: Some differentiation. <60: No clear positioning |
| Brand & Trust | Design quality, trust badges, security indicators, professional appearance | 80+: Modern design, trust signals throughout. 60–79: Adequate. <60: Outdated or unprofessional |
| Growth & Strategy | Lead capture, email marketing, content strategy, acquisition channels | 80+: Multi-channel strategy in place. 60–79: Some channels active. <60: No clear growth strategy |

#### `findings` (array, required)
5–10 findings ordered from most to least severe. Each has `severity` and `finding` fields.

**Severity levels:**
- `Critical` — Directly losing revenue or customers. Fix immediately.
- `High` — Significant impact on growth. Fix within 1–2 weeks.
- `Medium` — Meaningful improvement opportunity. Fix within 1 month.
- `Low` — Nice-to-have. Fix when time allows.

**Writing effective findings:**
- Be specific: "Homepage headline says 'Welcome to Our Firm'" not "Headline needs improvement"
- Quantify impact: "Missing meta descriptions on 8 of 12 service pages"
- Reference benchmarks: "Page load time is 4.2s (benchmark: under 2s)"
- Include evidence: "No testimonials found on homepage, services page, or contact page"

#### `quick_wins` (array, required)
3–5 action items implementable within one week with minimal effort. Each must be specific and actionable.

**Good:** "Rewrite the homepage headline from 'Welcome to Our Firm' to 'Dallas Family Law Attorney — Protecting What Matters Most'"
**Bad:** "Improve the headline" (too vague)

#### `medium_term` (array, required)
3–5 action items requiring 1–3 months. More involved but high impact.

#### `strategic` (array, required)
3–5 action items requiring 3–6 months. Foundational changes requiring planning and sustained effort.

#### `competitors` (array, optional)
Up to 3 competitor objects for the comparison table. If no competitor data is available, omit this field — the script will skip the competitor section.

---

### STEP 4: WRITE THE JSON FILE

```bash
cat > /tmp/report_data.json << 'JSONEOF'
{
  ... assembled JSON data ...
}
JSONEOF
```

---

### STEP 5: INVOKE THE PDF GENERATOR

**Prerequisites check:**
```bash
python3 -c "import reportlab" 2>/dev/null || pip3 install reportlab
```

**Generate the report:**
```bash
python3 scripts/generate_pdf_report.py /tmp/report_data.json "MARKETING-REPORT-<domain>.pdf"
```

Replace `<domain>` with the target domain, hyphens instead of dots:
- `example.com` → `MARKETING-REPORT-example-com.pdf`
- `dallaslaw.com` → `MARKETING-REPORT-dallaslaw-com.pdf`

**Demo mode (no arguments):**
```bash
python3 scripts/generate_pdf_report.py
# Creates: MARKETING-REPORT-sample.pdf
```

---

### STEP 6: VERIFY OUTPUT AND CLEAN UP

```bash
ls -la "MARKETING-REPORT-<domain>.pdf"
rm /tmp/report_data.json
```

Report the file path and size to the user.

---

## PDF REPORT STRUCTURE

### Page 1: Cover Page
- ASG wordmark ("AUTHORITY SYSTEMS GROUP") in ASG Blue (#25aae1), top-left
- Report title: "Digital Authority Assessment" or "Marketing Audit Report"
- Business name + target URL
- Generation date
- Overall score gauge (circular visualization, color-coded)
- Grade letter (A+ through F)
- Executive summary (2–4 sentences)
- Footer: "Authority Systems Group™ | AuthoritySystemsGroup.com | Confidential"

### Page 2: Score Breakdown
- Horizontal bar chart — all 6 category scores, color-coded
- Score table: category name, score, weight, status label
- Color coding per score-to-color mapping below

### Page 3: Key Findings
- Findings table with severity labels and descriptions
- Color-coded severity indicators
- Ordered most to least severe

### Page 4: Prioritized Action Plan
- Quick Wins (This Week)
- Medium-Term (1–3 Months)
- Strategic (3–6 Months)
- Numbered action items in each tier

### Page 5: Competitive Landscape (if competitor data provided)
- Comparison table: client vs. up to 3 competitors
- Rows: Positioning, Pricing, Social Proof, Content

### Final Page: Methodology
- Scoring methodology explanation
- Category weights and measurement criteria
- Footer: "Prepared by Authority Systems Group™ | AuthoritySystemsGroup.com"

---

## ASG BRAND COLOR SCHEME

The PDF uses Authority Systems Group™ brand standards throughout:

| Element | Color | Hex Code |
|---|---|---|
| Primary (headers, titles, wordmark) | ASG Blue | #25aae1 |
| Body text, secondary headings | ASG Charcoal | #58585a |
| Light backgrounds, table tints | ASG Light Blue Tint | #EAF6FC |
| Alternating table rows | ASG Light Gray | #F5F5F5 |
| White backgrounds | White | #FFFFFF |
| Success (high scores, 80+) | Green | #00C853 |
| Warning (medium scores, 60–79) | Amber | #FFB300 |
| Caution (low scores, 40–59) | Orange | #FF6B35 |
| Danger (critical scores, 0–39) | Red | #FF1744 |
| Borders | Light Border | #CCCCCC |

**Score-to-color mapping:**
- 80–100: Green (#00C853) — Strong performance
- 60–79: Amber (#FFB300) — Solid with room to improve
- 40–59: Orange (#FF6B35) — Needs attention
- 0–39: Red (#FF1744) — Critical issues

**Applied branding in the PDF:**
- Cover page header block: ASG Blue (#25aae1) fill, white text
- All section headings: ASG Blue (#25aae1)
- Table header rows: ASG Blue (#25aae1) fill, white text
- Table body rows: alternate White / ASG Light Gray (#F5F5F5)
- Body copy: ASG Charcoal (#58585a)
- Callout boxes: left border in ASG Blue, light blue tint background (#EAF6FC)
- Footer: ASG Charcoal text, ASG Blue top rule
- Score gauge: color-coded by performance tier (green/amber/orange/red)

See full brand constants: `/brand-standards/ASG_BRAND_DOCX.md`

---

## TROUBLESHOOTING

| Issue | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'reportlab'` | Run `pip3 install reportlab` |
| Script produces empty PDF | Check that JSON has all required fields |
| Score gauge not rendering | Ensure `overall_score` is an integer 0–100 |
| Competitor table missing | Ensure `competitors` array has objects with `name`, `positioning`, `pricing`, `social_proof`, `content` |
| PDF is only 1 page | Check for JSON parsing errors: `python3 -c "import json; json.load(open('/tmp/report_data.json'))"` |
| Colors don't match ASG brand | Verify `generate_pdf_report.py` uses updated ASG hex constants (not the original navy/blue defaults) |
| Script not found | `scripts/generate_pdf_report.py` must exist — see NOTE below |

**NOTE:** `scripts/generate_pdf_report.py` must be built. The script does not yet exist in the project. Reference this skill file as the specification. The script must accept two arguments: (1) path to JSON data file, (2) output PDF filename. It must use `reportlab` and apply ASG brand colors as defined above.

---

## INTEGRATION WITH OTHER SKILLS

Recommended workflow — run these first, then generate PDF:

```
1. /market audit <url>        → MARKETING-AUDIT.md
2. /market competitors <url>  → COMPETITOR-ANALYSIS.md
3. /market seo <url>          → SEO-AUDIT.md
4. /market landing <url>      → LANDING-CRO.md
5. /market report-pdf <url>   → MARKETING-REPORT-<domain>.pdf
```

The PDF skill automatically checks for output files from each preceding skill and incorporates their data into the report JSON. The more prior audits available, the richer the findings.

**For DOCX (ASG branded Word document) instead of PDF:**
```bash
python build_docx.py MARKETING-REPORT.md
```
Produces a fully ASG-branded DOCX per `/brand-standards/ASG_BRAND_DOCX.md`.

---

## OUTPUT FORMAT

```
File:     MARKETING-REPORT-<domain>.pdf
Location: Project root directory
Size:     Typically 200KB–500KB depending on content volume
Pages:    5–7 pages depending on competitor data and section count
Naming:   [client-slug]_marketing-report_[YYYYMMDD].pdf (client delivery version)
```

---

## QC CHECK

- [ ] JSON data complete — all required fields present before invoking script
- [ ] `overall_score` is a whole number calculated from the correct weighted formula
- [ ] Findings are specific and evidence-based — no generic language
- [ ] Quick wins are genuinely actionable within one week
- [ ] Cover page shows correct business name, URL, and date
- [ ] ASG Blue (#25aae1) used for all headers, title, and table headers
- [ ] ASG Charcoal (#58585a) used for body text
- [ ] Footer reads "Authority Systems Group™ | AuthoritySystemsGroup.com | Confidential"
- [ ] Score gauge color matches performance tier
- [ ] Competitor section present only if competitor data was collected
- [ ] PDF verified with `ls -la` after generation

---

*Authority Systems Group™ — Digital Intelligence Division*
*Skill Owner: Victor Hale | Technical Oversight: Iris Nolan, CTO*
*Updated: 2026-03-06 — Full ASG branding, comprehensive field guide*
