# STRATEGIC_PLAN_1YR.md
# Authority Systems Group™ — Skill: Year 1 Strategic & Tactical Plan
# Produces Section 4 (Year 1 portion) of the Authority Blueprint™
# Voice: Daniel Frost, CSO

---

## PURPOSE

Produce the Year 1 strategic and tactical plan. This is the most operationally detailed section of the Blueprint — the client should be able to read it and know exactly what's happening to their business each quarter, what it's designed to accomplish, and how success is measured.

The Year 1 plan is organized around the Quarterly Authority Rotation™: each quarter focuses on one of the four highest-profit services. Full strategic depth on one service per quarter rather than shallow coverage across all four simultaneously.

**What makes this plan different from anything a Big 4 firm produces**:
- It's built around belief stages, not just activities
- Every initiative has a revenue mechanism — not just a marketing purpose
- It's sequenced for compounding effect — Q4 is stronger because of Q1, Q2, and Q3
- It's specific to THIS business in THIS market — not a template with the client's name inserted

---

## INPUTS REQUIRED

- `client-context.yaml` (fully populated)
- Completed `BELIEF_FILTER_MAP.md`
- Completed `MARKET_ANALYSIS.md` (especially Section 3D — Authority Statement)
- `niche-library/[niche-id].yaml` (seasonal patterns)

---

## YEAR 1 STRATEGIC ARCHITECTURE

### The Quarterly Authority Rotation™ Model

```
Q1: Foundation + Fast Cash
   Focus service: Priority Service #1 (highest value/margin)
   Strategic goal: Establish authority, capture existing demand, activate fast revenue
   Content focus: Priority Service #1
   Infrastructure: Core digital foundation, reputation system, referral program launch

Q2: Expansion + Optimization
   Focus service: Priority Service #2
   Strategic goal: Expand service authority, optimize what Q1 built, accelerate lead flow
   Content focus: Priority Service #2
   Infrastructure: Email system full deployment, paid media optimization

Q3: Depth + Diversification
   Focus service: Priority Service #3
   Strategic goal: Deepen market penetration, diversify acquisition channels
   Content focus: Priority Service #3
   Infrastructure: SEO compounding, referral network expansion

Q4: Dominance + Scale Prep
   Focus service: Priority Service #4
   Strategic goal: Solidify market position, prepare systems for Year 2 scale
   Content focus: Priority Service #4
   Infrastructure: Case study bank, testimonial system, Year 2 planning
```

---

## EXECUTION INSTRUCTIONS

### SECTION 4A — Year 1 Strategic Overview

**Voice**: Daniel Frost — structured, confident

Write a 3-paragraph executive framing of Year 1:

**Paragraph 1 — The Thesis**:
What is the single most important strategic objective of Year 1 for this specific client? Not "grow revenue" — something specific. Examples:
- "Establish [Client Name] as the definitive authority for [specific case type] in [City], making every competitor's positioning feel generic by comparison."
- "Convert [Client Name]'s strongest operational differentiator — [specific thing they do better] — into a marketing asset that attracts and pre-sells the ideal client before the first call."
- "Systematize the referral and reactivation revenue that [Client Name] is currently generating inconsistently, then layer in digital acquisition on top of a proven conversion foundation."

**Paragraph 2 — The Logic of Sequencing**:
Explain WHY the quarterly rotation order was chosen for this client. Reference the specific priority services and the belief barrier identified in the Belief Filter Map. The client should understand that Q1 was not arbitrary — it was selected because [specific reason].

**Paragraph 3 — What Success Looks Like at Month 12**:
Paint a specific picture. Not "increased revenue" but: "[Client Name] is generating [X] qualified consultations per month from [channels], converting at [Y%], averaging [Z per client]. The reactivation and referral systems are running without manual management. Q1 content is ranking for [specific terms]. The authority position is visible and differentiating."

---

### SECTION 4B — Quarter 1 Tactical Plan (Month 1-3)

**Focus Service**: `priority_services[0].name`
**Strategic Goal**: Foundation + Fast Cash

#### Month 1 — System Launch

**Week 1-2: Fast Cash Sprint™ Activation**
List the 3 fast cash campaigns from `fast_cash_priorities`. For each:
- Campaign name (make it specific to the client's niche and situation)
- Objective (one sentence)
- What's being deployed (sequence, campaign, program)
- What the client needs to do to activate it
- Success metric at 30 days

**Week 3-4: Digital Foundation**
- Google Business Profile audit and optimization
  - Specific items: service descriptions, photo upload, Q&A seeding, review response protocol
  - Success metric: complete profile with [X] initial review requests deployed
- Website conversion audit: identify the 3 highest-impact changes for the primary service landing page
- CRM setup / cleanup (based on `client-context.yaml crm_platform`)
  - What tags/pipelines/automations need to exist before content drives traffic

**Content Launch**:
- 4 social posts introducing the Q1 authority theme (from content calendar)
- 1 authority article published on website (SEO foundation)
- Video #1 script approved and scheduled for filming

#### Month 2 — Content Engine + Reputation System

**Content**:
- Authority content cadence running (social + blog)
- Video #1 published (if filmed in month 1)
- Email welcome sequence live for all new leads

**Reputation System**:
- Automated review request system active (from Iris Nolan / CTO spec)
- Review response protocol in place
- Target: [X] new Google reviews in month 2

**Referral Program Launch**:
- Referral program formally launched with top 10 existing clients personally notified
- Professional referral partner outreach initiated (specify the partner types for this niche)
- Target: [X] referral conversations initiated

#### Month 3 — Optimization + Q2 Prep

**Performance Review**:
- Review Q1 KPIs against targets
- Identify top-performing content pieces (double down)
- Identify conversion leaks (fix before Q2)

**Q2 Content Pre-Build**:
- Q2 content calendar finalized
- Q2 authority article briefs prepared
- Q2 video scripts in progress

**Success Metrics — Q1 Exit**:
- [ ] Fast Cash Sprint campaigns deployed and generating response
- [ ] [X] new Google reviews
- [ ] [X] qualified leads from organic/referral
- [ ] [X] consultations booked
- [ ] Email welcome sequence live and delivering
- [ ] Referral program active with first referrals logged

---

### SECTION 4C — Quarter 2 Tactical Plan (Month 4-6)

**Focus Service**: `priority_services[1].name`
**Strategic Goal**: Expansion + Optimization

**Write Q2 with the same Month 4 / Month 5 / Month 6 granularity as Q1.** Do not summarize Q2 as a single block — each month requires specific named actions, not category descriptions.

Q2 context and additions:
- Focus shifts to Priority Service #2 while Q1 service content continues compounding
- Q1 systems are running — Q2 builds ON them, not independently
- Paid media layer launches if not already running
- Email nurture sequences for Priority Service #2 go live
- Referral network expands to professional partner category #2
- Q1 content beginning to rank organically — document and amplify

**Month 4**: Launch Q2 content cadence for Priority Service #2. Q1 performance review — what exceeded targets, what needs adjustment. Deploy paid media if new this quarter.

**Month 5**: Video content for Priority Service #2 (if applicable). Professional referral second outreach or event. Review request cadence continues. Mid-point KPI check against 6-month targets.

**Month 6**: Mid-year strategy review with Roger Bauer. Case study production from Q1-Q2 closed clients. Q3 content pre-build initiated. Evaluate whether paid media budget should increase based on CPL data.

**Q2 Success Metrics — Exit Targets**: Use 6-month KPI targets from `client-context.yaml kpis.targets_90_days` extrapolated forward, or build explicitly for the engagement.

---

### SECTION 4D — Quarter 3 Tactical Plan (Month 7-9)

**Focus Service**: `priority_services[2].name`
**Strategic Goal**: Depth + Diversification

**Write Q3 with the same Month 7 / Month 8 / Month 9 granularity as Q1.** Three months with specific actions.

Q3 context:
- Q1 and Q2 content is ranking organically — reference the specific terms this client is targeting
- Referral network 6 months active — assess and optimize
- Paid media has data — optimize based on what's converting
- Introduce education/events strategy if applicable for this niche (check niche library)
- Cold outreach layer if pipeline targets aren't being hit

**Month 7**: Paid campaign optimization based on first 3 months of data. Case study #1 published. Seasonal trigger content deployed per niche library `seasonal_patterns` (e.g., January divorce surge prep for family law starts here).

**Month 8**: Seasonal peak content push (name the specific seasonal pattern from the niche library and what content addresses it). Partnership marketing activation — second professional referral category. Q3 case study production.

**Month 9**: Email upsell/cross-sell sequences to existing clients. Referral network health check — top referring sources identified and rewarded. Q3 performance review.

---

### SECTION 4E — Quarter 4 Tactical Plan (Month 10-12)

**Focus Service**: `priority_services[3].name`
**Strategic Goal**: Dominance + Year 2 Scale Prep

**Write Q4 with the same Month 10 / Month 11 / Month 12 granularity as Q1.** Q4 tone shifts from building to optimizing and preparing — but it still has monthly specificity.

**Month 10**: Q4 content launch for Priority Service #4. Pre-season campaign for the niche's highest-volume period (per niche library — e.g., December content for January divorce surge; Q4 planning content for financial advisors). Year 2 planning kickoff with Roger Bauer.

**Month 11**: Paid media seasonal push (if applicable). Second case study published. Email campaign to full list for seasonal trigger. Professional referral partner appreciation (relationship maintenance before year-end).

**Month 12**: Year-end full KPI review. Authority audit — what position has been established, what evidence exists. Referral system performance review (cost per referral, LTV of referred vs. non-referred). Pricing review — with established authority, is there a basis for a price increase in Year 2? Year 2 strategic plan brief.

**Year-End Success Criteria**:
Produce a specific table:

| KPI | Baseline (Month 0) | Target (Month 12) | Stretch (Month 12) |
|---|---|---|---|
| Monthly leads | [X] | [Y] | [Z] |
| Consultation booking rate | [X%] | [Y%] | [Z%] |
| Avg transaction value | $[X] | $[Y] | $[Z] |
| Monthly revenue | $[X] | $[Y] | $[Z] |
| Google review count | [X] | [X+Y] | [X+Z] |
| Review rating | [X.X] | 4.8+ | 4.9+ |
| Referral % of new clients | [X%] | [Y%] | [Z%] |

---

### SECTION 4F — Year 1 Investment & Resource Requirements

**Voice**: Preston Adler, COO

Be direct about what Year 1 requires from the client — not just their investment in ASG, but their operational commitments:

1. **Time**: What do they or their team need to do? (Review content, film videos, respond to inquiries, attend strategy calls)
2. **Content source material**: What do they need to provide? (Case details, photos, team bios, testimonials)
3. **Ad spend**: What paid media budget does the plan assume? (Separate from ASG fees)
4. **Decision-making speed**: Some recommendations require fast decisions — flag the time-sensitive ones
5. **Internal systems**: Any CRM, intake, or operational changes needed to support the marketing

---

## OUTPUT FORMAT

Produce as Section 4 of the Authority Blueprint™.

Open with:
> *"The Year 1 plan below was built from a clear-eyed analysis of [Client Name]'s market position, current assets, and the specific belief barriers standing between your ideal clients and your front door. It is not a general marketing plan with your name on it. Every initiative was selected because it's the right move for this business at this moment."*
> *— Daniel Frost, CSO | Authority Systems Group™*

Close with Daniel Frost sign-off and page break into Section 5.

---

## QC CHECK BEFORE HANDOFF

- [ ] Q1 plan is specific enough to execute without asking ASG for clarification
- [ ] Every initiative traces to a belief stage (from the Belief Filter Map)
- [ ] Every initiative has a success metric
- [ ] Quarterly sequence has a logical compounding logic (Q2 builds on Q1)
- [ ] Year-end KPI table uses actual baseline numbers from client-context.yaml
- [ ] Resource requirements are honest — nothing is understated

---

*Authority Systems Group™ — Strategy Skills Library*
*Owner: Daniel Frost, CSO | Reviewed by: Roger Bauer, Director*
