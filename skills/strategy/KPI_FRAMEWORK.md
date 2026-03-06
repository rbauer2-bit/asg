# KPI_FRAMEWORK.md
# Authority Systems Group™ — Skill: KPI Dashboard & Measurement Framework
# Produces Section 7 of the Authority Blueprint™
# Voice: Preston Adler, COO

---

## PURPOSE

Define the 20 metrics [Client Name] tracks monthly, establish baselines from intake data, set 90-day and 12-month targets, and specify the dashboard structure that makes these metrics visible and actionable.

Measurement is what separates a marketing program from a marketing investment. If we can't measure it, we can't optimize it. If we can't optimize it, we're spending money on faith.

---

## EXECUTION INSTRUCTIONS

Load from `client-context.yaml`:
- All KPI baseline fields
- Revenue targets
- Priority services data
- Goals block

### The KPI Categories and Metrics

Organize into 5 categories. Present in the Blueprint as separate labeled tables, one per category:

**CATEGORY 1 — ACQUISITION & TOP-OF-FUNNEL** (Leading indicators)
1. Website sessions / month (all properties)
2. Niche website sessions / month (if separate site exists)
3. Monthly inbound inquiries — all sources
4. Monthly inbound inquiries — Q1 focus service specifically
5. Google review count (cumulative — this is a proxy for search rank)

**CATEGORY 2 — ENGAGEMENT & CONVERSION**
6. Consultation bookings / month
7. Consultation-to-client conversion rate (%)
8. Average days from first contact to signed agreement
9. Consultation show rate (booked → actually showed %)
10. Lead quality score (1–10, subjective — tracks whether the right clients are calling)

**CATEGORY 3 — REVENUE & VALUE**
11. New clients signed / month (Q1 focus service)
12. Average transaction value (Q1 focus service)
13. Monthly revenue — Q1 focus service
14. Reactivation revenue (one-time sprint result)
15. Referral-sourced new matters / month

**CATEGORY 4 — REPUTATION & REFERRAL**
16. New Google reviews / month (velocity)
17. Google review rating (rolling average)
18. Review requests sent / month
19. Referral asks sent / month
20. Active professional referral partners (cumulative)

**CATEGORY 5 — CONTENT & DIGITAL**
21. Niche website articles published (cumulative)
22. Email list size (opt-in subscribers)
23. Organic search clicks / month (Google Search Console)
24. Email open rate (primary sequences)
25. LinkedIn / social engagement rate (if applicable)

*Note: 25 metrics rather than 20 to accommodate the niche website and email list channels now standard in every Blueprint.*

---

### Baseline and Target Table

**4-COLUMN FORMAT — USE THIS EXACT STRUCTURE:**

For each category, produce a table:

| Metric | Baseline | 90-Day Target | 6-Month Target | 12-Month Target |
|--------|----------|---------------|----------------|-----------------|

The 6-month target column is **mandatory**. It represents the mid-year checkpoint — the point at which the Fast Cash Sprint results have fully materialized and the niche website/content engine is beginning to compound. Without a 6-month target, the client has no waypoint between the 90-day sprint and the 12-month vision.

**Example (Reputation & Referral category):**

| Metric | Baseline | 90-Day Target | 6-Month Target | 12-Month Target |
|--------|----------|---------------|----------------|-----------------|
| Google review count | 59 | 120 | 200 | 270 |
| Google review rating | 4.7 | 4.7+ | 4.7+ | 4.8 |
| New reviews / month | 0 (no system) | 10 | 15 | 15 |
| Referral asks sent / month | 0 | 20 | 30 | 40 |
| Active professional referral partners | 0 | 5 | 10 | 20 |

**Baseline instructions**:
- Pull from `client-context.yaml kpis` fields where populated
- For fields marked `# ESTIMATED` in client-context.yaml — note as estimated and flag for actual measurement in Month 1
- For fields with no data — write "To be established in Month 1" — do not invent numbers

**Target instructions**:
- 90-day targets should be achievable with Fast Cash Sprint execution alone
- 12-month targets should reflect the full Year 1 plan executing at target scenario
- Use these benchmark improvements as starting points, modified for client context:
  - Lead volume: +25-40% by Month 12 for most professional service businesses
  - Consultation booking rate: +10-15 percentage points if currently below 40%
  - Conversion rate: typically improves 5-10 pp with better authority positioning and pre-sell
  - Review count: minimum +3-5 new reviews/month once automation is live
  - Referral %: from current baseline to 30-40% within 12 months with formal program

---

### Dashboard Architecture

Specify the reporting structure:

**Weekly (internal team view)**:
- New leads this week vs. prior week
- Consultations booked this week
- Fast Cash Sprint response rates (during sprint period)
- New reviews this week

**Monthly (client-facing report)**:
All 20 KPIs vs. baseline and target
- Green: at or above target
- Yellow: within 15% of target
- Red: more than 15% below target

Monthly report delivery: First Friday of each month

**Quarterly (strategy review)**:
- Full 20-KPI review with trend analysis
- Revenue performance vs. 3-scenario model
- Channel efficiency analysis (cost/lead and cost/client by channel)
- Recommendation adjustments for upcoming quarter
- Forward outlook: next quarter targets and focus areas

**Recommended tools** (based on `client-context.yaml crm_platform`):
- GHL users: native GHL reporting + custom dashboard
- Other CRM: Simple Google Sheets template (ASG provides)
- Minimum viable: Monthly email report from ASG team

---

## OUTPUT FORMAT

Produce as Section 7 of the Authority Blueprint™:

**SECTION 7: KPI DASHBOARD**
*Prepared by Preston Adler, COO — Authority Systems Group™*

Open with:
> *"Marketing without measurement is guessing with better branding. Every recommendation in this plan has a corresponding metric. Every metric has a target. Every target has an owner. That's how we know if the system is working — and how we know what to change when it isn't."*
> *— Preston Adler, COO | Authority Systems Group™*

Include the full KPI table, dashboard architecture, and reporting schedule.

Close with:
> *"On the first Friday of every month, you'll receive a report showing all 20 of these metrics against your targets. Nothing buried. Nothing hidden. If something isn't working, we'll see it and we'll tell you."*
> *— Preston Adler, COO | Authority Systems Group™*

---

*Authority Systems Group™ — Operations Skills Library*
*Owner: Preston Adler, COO*
