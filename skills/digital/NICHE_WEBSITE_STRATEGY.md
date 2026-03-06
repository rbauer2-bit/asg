# NICHE_WEBSITE_STRATEGY.md
# Authority Systems Group™ — Skill: Niche Authority Website Strategy
# Produces Section 9 of the Authority Blueprint™ (when a domain asset is proposed)
# Voice: Iris Nolan, CTO
# Include this section when: ASG holds a relevant domain, or a niche site is recommended

---

## PURPOSE

A niche website is a purpose-built, fast-loading, single-service-focused web property that solves two problems simultaneously:

1. **Conversion leaks on a multi-practice main site** — general-practice websites with slow load times, diluted service messaging, or broad positioning lose conversion from high-intent visitors. A niche site eliminates all three issues for the target service.

2. **Local SEO competition** — keyword-specific domains with clean architecture rank faster and rank independently of a firm's main site. A niche site can capture search traffic while the main site remains optimized for its broader purpose.

This skill is invoked whenever:
- ASG holds a relevant domain asset that fits the client's primary service and geography
- The client's existing website has documented technical issues (slow load, multi-practice dilution)
- Local search competition for the target service is addressable with a clean, focused property

---

## INPUTS REQUIRED

- `client-context.yaml` — firm profile, location, primary service, awards, contact
- `niche-library/[niche-id].yaml` — competitive_landscape_patterns, compliance_flags, content_topics_bank
- Completed `MARKET_ANALYSIS.md` — especially Section 3D (Authority Statement) and 3A (competitive landscape)
- Completed `BELIEF_FILTER_MAP.md` — the avatar's trusted content channels and the positioning gap

---

## EXECUTION INSTRUCTIONS

### SECTION A — THE STRATEGIC CASE

Before specifying any technical details, establish why this niche site is the right investment for this client at this moment. Three things to address:

**1. The traffic problem** (specific): What is wrong with the client's current web presence that is costing them leads? Be specific — name the issue (slow load time confirmed, multi-practice dilution, no conversion-focused family law page, etc.). If the problem isn't documented, don't invent it.

**2. The opportunity** (specific): What search volume exists for the target service and geography? What are the top 3 keyword opportunities that a clean, focused site could compete for? Name them. Grade the competition: are competitors ranking on these terms with optimized content, or with thin profiles?

**3. The domain asset** (if applicable): Name the domain, explain why it's strategically valuable (keyword + geography alignment, potential DA from age, clean history), and state the deployment plan.

---

### SECTION B — TECHNICAL SPECIFICATIONS

Every niche site built by ASG follows these specifications. No exceptions — these represent the minimum viable foundation for a site that ranks and converts.

**Platform**:
- WordPress with Astra (or equivalent minimal theme — Kadence, GeneratePress)
- No page-builder bloat (no Elementor, no Divi — only lightweight builders if needed)
- Target load time: under 2 seconds (Google PageSpeed score 90+)

**Hosting**:
- Kinsta, WP Engine, or SiteGround (all meet the performance requirement)
- Region: US-based server for US-geography clients
- SSL: Mandatory from Day 1. HTTP auto-redirects to HTTPS.

**Indexing and tracking**:
- Google Search Console: submit sitemap within 24 hours of launch
- Google Analytics 4: installed before launch
- Google Tag Manager: for conversion tracking (form submissions, click-to-call)

**Mobile**:
- Mobile-first design standard. 55-65% of professional service searches occur on mobile.
- All CTAs (click-to-call, form, booking link) must be functional on mobile without zooming

**Lead capture**:
- Booking integration: Calendly, Acuity, or equivalent — for free consultation scheduling
- Contact form: Name, phone, email, brief description of situation
- Click-to-call: Phone number as a tappable link in header and footer, above the fold on all pages

---

### SECTION C — SITE ARCHITECTURE AT LAUNCH

Specify the full site map for the launch version. Every page listed must be built and live on launch day — no "coming soon" pages.

**Minimum required pages at launch:**

```
[Domain].com
├── Home (primary conversion page)
│   ├── Above the fold: H1 with primary keyword + client credentials + consultation CTA
│   ├── Awards/recognition display (with qualifying language per compliance flags)
│   ├── 3 primary service areas with brief descriptions and internal links
│   ├── Google reviews widget (auto-updates from GBP)
│   ├── "Why [Client Name]" differentiator section (pull from Authority Statement)
│   └── Free consultation CTA (form or booking link)
│
├── About [Attorney/Owner Name]
│   ├── [X]-year story — geography-specific, credential-anchored
│   ├── Awards and recognitions (with qualifying language)
│   ├── Differentiator section (pull from market positioning gap)
│   ├── Bar admissions / professional memberships
│   └── Personal element (appropriate to niche — builds trust without oversharing)
│
├── [Service 1] (e.g., Divorce)
│   ├── 600–900 words, primary keyword optimized
│   ├── What it is, what the process looks like, what the client needs to know
│   ├── CTA above and below the fold
│   └── FAQ section (3-5 questions, schema-marked for featured snippets)
│
├── [Service 2] (e.g., Child Custody)
│   └── Same structure as Service 1
│
├── [Service 3] (e.g., Divorce — uncontested variant, or next service)
│   └── Same structure
│
├── [Service 4] (optional at launch — add if content is ready)
│   └── Same structure
│
├── Blog / Resources
│   └── Initial 5 articles live at launch (from Content Strategy — Section 8)
│       Articles are real, fully written — not placeholder posts
│
├── FAQ (standalone page)
│   └── 10-15 questions with full answers — optimized for voice search and featured snippets
│       Schema markup applied
│
├── Free Consultation
│   ├── What to expect (removes friction — describes the process)
│   ├── Booking form / Calendly integration
│   └── Phone number prominent + click-to-call
│
└── Lead Magnet Landing Page
    └── [Guide title] opt-in — name, email → triggers Welcome Sequence
        See LEAD_MAGNET_AND_REFERRAL_PROGRAM.md
```

**Pages NOT included at launch** (add in Q2+):
- Testimonials page (build as review count grows)
- Case results / case studies (add when first anonymized case study is approved)
- Video library (add when video content is produced)

---

### SECTION D — LOCAL SEO STRATEGY

**Primary keywords** (typically 3-5):
Pull from `niche-library/[niche-id].yaml content_topics_bank` and from the client's geography. Structure as:
- "[Primary service] attorney [city]"
- "[City] [primary service] attorney"
- "[Primary service] lawyer [city]"
- "[Specific service variant] [city]" (e.g., "contested divorce attorney Louisville")

**Secondary / long-tail keywords** (typically 5-8):
Lower competition, higher buyer intent. Structure as:
- "[Specific case type] [city]" (e.g., "high asset divorce Louisville")
- "[Question format]" (e.g., "how much does divorce cost in Kentucky")
- "[Service + geography variant]" (e.g., "Jefferson County family law attorney")

**On-page SEO checklist** (apply to every page):
- [ ] Primary keyword in H1 (first heading on page)
- [ ] Primary keyword in first 100 words of body copy
- [ ] Secondary keywords distributed naturally in body copy
- [ ] Meta title: Primary keyword + location (under 60 characters)
- [ ] Meta description: CTA-oriented, includes keyword + location (under 155 characters)
- [ ] Image alt text: Descriptive with keyword where natural
- [ ] Internal links: Each service page links to 2+ other relevant pages
- [ ] Schema markup: LocalBusiness schema on home page; FAQ schema on FAQ page; Article schema on blog posts

**Google Business Profile integration**:
- [ ] GBP linked to niche site (or dual-linked — main site + niche site)
- [ ] All existing reviews acknowledged and responded to before launch
- [ ] Google Posts live within 7 days of launch (2/week cadence going forward)
- [ ] Service descriptions fully populated
- [ ] Photos: interior, exterior, headshot, at minimum

**Directory listings** (update to include niche site URL):
Specify the 5-8 most relevant directories for this niche. For legal:
- Avvo
- Martindale-Hubbell
- Lawyers.com
- Justia
- FindLaw
- State bar directory
- County bar association listing

---

### SECTION E — PERFORMANCE MILESTONES

Produce a milestone table. Every milestone has a date target and a measurable success metric — no vague milestones like "gaining traction."

| Milestone | Target Date | Success Metric |
|-----------|-------------|----------------|
| Site live | Day [X] | All core pages published, GSC + GA4 active |
| First organic impression | Day [X+15] | GSC showing impressions for ≥1 target keyword |
| First consultation from site | Day [X+20] | Form submission or click-to-call tracked in GA4 |
| [X] monthly organic sessions | Month [Y] | GA4 sessions report |
| Top-10 ranking for [keyword] | Month [Y+1] | GSC position report |
| [X] monthly sessions | Month [Y+2] | GA4 report |
| Google 3-Pack appearance | Month [Y+3] | Manual SERP check from Louisville IP |

Dates are filled in based on engagement start and the specific competitiveness of the target keywords. Conservative = 90-120 days to first meaningful ranking. Competitive markets = 120-180 days.

---

### SECTION F — COMPLIANCE REQUIREMENTS FOR THE SITE

Pull from `niche-library/[niche-id].yaml compliance_flags` and state bar advertising rules for the client's jurisdiction.

Apply to every page:
- Site-wide disclaimer in footer: "[Site name] is for informational purposes only and does not constitute legal / medical / financial advice."
- Award claims: "As recognized by [org] in [year]" — never standalone superlatives
- Outcome language: "may," "can," "in our experience," "results vary" — never guarantees
- Testimonials: Client-specific consent required. Anonymized case references do not require consent.

---

## OUTPUT FORMAT

Produce as Section 9 of the Authority Blueprint™:

**SECTION 9: [DOMAIN NAME] — NICHE WEBSITE STRATEGY**
*Prepared by Iris Nolan, CTO — Authority Systems Group™*

Open with:
> *"Your existing website serves multiple audiences across multiple practice areas. [Domain name] is something different — a single-purpose authority hub built specifically for [niche] clients in [geography], fast enough to rank and focused enough to convert. While your main site continues to serve your full practice, [domain] becomes the dedicated pipeline for [primary service] clients."*
> *— Iris Nolan, CTO | Authority Systems Group™*

Sections: A through F in the Blueprint. The technical specs (Section B) should be summarized — full spec lives in the CTO build brief, not the client document.

---

## QC CHECK BEFORE HANDOFF

- [ ] Strategic case names a specific, documented problem with current web presence
- [ ] Site architecture is complete — every launch page named, no "TBD" pages
- [ ] Keyword list is specific to client's geography and service (not generic niche keywords)
- [ ] Milestone table has actual target dates based on engagement start
- [ ] Compliance requirements are jurisdiction-specific (not generic)
- [ ] Platform and hosting recommendations are named (not "a fast host")
- [ ] Google Business Profile update plan is specified

---

*Authority Systems Group™ — Digital Skills Library*
*Owner: Iris Nolan, CTO | Strategy review: Daniel Frost, CSO*
