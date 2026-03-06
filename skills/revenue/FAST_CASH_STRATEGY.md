# FAST_CASH_STRATEGY.md
# Authority Systems Group™ — Skill: Fast Cash Sprint™ Strategy Builder
# Produces Section 6 of the Authority Blueprint™
# Voice: Tanya Blackwood, CRO + Sofia Vega, Board

---

## PURPOSE

The Fast Cash Sprint™ is the section clients read first. It has to land hard.

Every professional service business owner who opens the Authority Blueprint™ is looking for proof that this isn't just a long-horizon marketing exercise — that there's something in here they can do THIS MONTH to move the needle. The Fast Cash Sprint™ is that proof.

This skill selects the 3 highest-return, most niche-appropriate strategies from the Hidden Revenue Playbook, customizes them completely to this specific client, and presents them as a ready-to-deploy 90-day revenue activation plan.

**The selection principle**: Fastest path to actual revenue, with the lowest implementation burden, for a business at this client's exact stage. Not theoretically applicable — specifically applicable.

---

## THE HIDDEN REVENUE PLAYBOOK — 22 STRATEGIES

Reference source: The Hidden Revenue Playbook (22 strategies for generating revenue from existing business assets).

Core thesis: The fastest, cheapest path to new revenue is almost always the assets the business already owns — past clients, existing relationships, underpriced services, untapped referral sources — not new lead generation.

Selling to an existing client is 5–7x cheaper than acquiring a new one. Existing clients spend more per transaction. This is not a marketing opinion — it's the foundational economics of professional services.

---

## EXECUTION INSTRUCTIONS

### Phase 1 — Strategy Selection

Load `client-context.yaml` fields:
- `fast_cash_priorities` (pre-selected strategies from NICHE_INTAKE.md)
- `business.client_count_past_12mo` and `business.client_count_active`
- `business.crm_platform`
- `business.primary_referral_sources`
- `business.avg_transaction_value`
- `niche.vertical`

Load `niche-library/[niche-id].yaml`:
- `fast_cash_strategy_fit` ratings
- `top_5_recommended` list
- `compliance_flags`

**Selection Filter — run every candidate strategy through this filter**:

1. **Niche fit**: Is this strategy rated "high" or "medium" for this niche? (Eliminate "low" and "not-applicable")
2. **Asset availability**: Does this client have the asset required? (Reactivation needs a list. Referral program needs existing clients. Prepaid packages need a defined service scope.)
3. **Implementation speed**: Can this be deployed within 30 days? (If it requires 6 months to build, it's not a fast cash strategy — it's infrastructure)
4. **Compliance clearance**: Does this strategy conflict with any compliance flags in the niche library?
5. **CRM dependency**: Does this strategy require automation that the client's current CRM can support?

Select the top 3 that pass all 5 filters. If a tie exists, choose the higher-estimated revenue impact.

---

### Phase 2 — Strategy Customization

For each of the 3 selected strategies, produce a complete campaign brief:

#### FORMAT FOR EACH STRATEGY:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FAST CASH STRATEGY #[1/2/3]
[Strategy Name — specific to this client, not generic]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE OPPORTUNITY [Sofia Vega voice — plain operator language]
[2-3 sentences describing exactly what revenue is sitting uncaptured and why.
No jargon. Reference specific numbers from client context.]

Example: "Right now, [Client Name] has approximately [X] past clients who haven't
been in contact in 12+ months. Based on your average transaction value of $[Y] and
a conservative 15% response rate, a properly structured reactivation campaign
should produce $[X × 0.15 × Y] in the first 30 days — from clients who already
know your work."

WHY THIS WORKS FOR [Client Name]
[2-3 sentences specific to this client's situation. Reference their specific
niche, avatar, and any relevant context from the intake questionnaire.
This cannot be generic niche library language — it must reference this client.]

THE APPROACH [Tanya Blackwood voice — revenue mechanics]
Step 1: [Specific action]
Step 2: [Specific action]
Step 3: [Specific action]
[No more than 5 steps. Each step is a real action, not a category.]

REVENUE IMPACT ESTIMATE
Conservative: $[X] (assumes [Y%] response rate, $[Z] avg transaction)
Target: $[X] (assumes [Y%] response rate, $[Z] avg transaction)
Math: [Show the calculation — list size × response rate × avg value]
Timeline: Revenue expected within [X] days of launch

IMPLEMENTATION REQUIREMENTS
What ASG provides: [List specific deliverables ASG produces for this strategy]
What [Client Name] provides: [Specific items needed from client]
CRM dependency: [None / GHL / [specific platform] — with specific setup notes]
Timeline to launch: [X days after client provides required items]

COMPLIANCE NOTES
[Any restrictions or required modifications for this niche — reference niche library flags]
[If none: "No compliance restrictions identified for this strategy in [niche]."]

SOFIA VEGA'S TAKE
[1-2 sentence quote in Sofia's voice — operator to operator, specific to this strategy for this niche]
Example: "I ran a version of this in my dental practice in year three and it pulled
$67k out of a list I'd been completely ignoring. The mechanics are simpler than it
looks — the hardest part is just deciding to send the first message."
```

---

### Phase 3 — The 90-Day Fast Cash Calendar

After presenting all 3 individual strategies, produce an integrated 90-day calendar showing how all three run simultaneously without conflicting or overwhelming the client's team.

**Calendar format standard**: Use □ checkbox items. Every item is specific enough to hand to an implementer without asking a single clarifying question. No generic directives like "continue campaign" or "monitor results" — name the specific action.

```
FAST CASH SPRINT™ — 90-DAY ACTIVATION CALENDAR

WEEK 1–2: LAUNCH PREPARATION
□ [Strategy 1]: [Specific setup action — name the exact thing being built/configured]
□ [Strategy 2]: [Specific setup action]
□ [Strategy 3]: [Specific setup action]
□ Client provides by Day 7: [Itemized list — past client list, photos, approvals, etc.]
□ ASG delivers by Day 7: [Itemized list — templates, copy drafts, etc.]

WEEK 3–4: CAMPAIGN LAUNCH
□ [Strategy 1]: [First touchpoint deploys — name what goes out, to whom, via what channel]
□ [Strategy 2]: [First touchpoint deploys]
□ [Monitor]: Review and respond to all initial responses within 24 hours
□ [Note any early performance signals for Roger Bauer review call]

WEEK 5–8: ACTIVE CAMPAIGN MANAGEMENT
□ [Strategy 1]: [Follow-up sequence step — name which email or touchpoint]
□ [Strategy 2]: [Ongoing activation — specific action]
□ [Strategy 3]: [Launch or major milestone — if this strategy has a later start]
□ Weekly: Track each strategy's response rate vs. target in KPI dashboard

WEEK 9–12: OPTIMIZATION + LOCK IN
□ Full performance review: all 3 strategies against conservative/target scenarios
□ Double down: [Name what to increase based on what's working]
□ [Strategy 1]: Determine if second deployment wave is warranted
□ Build case study / testimonial material from sprint results
□ Prepare 90-day results summary for Roger Bauer review call

TOTAL ESTIMATED 90-DAY REVENUE IMPACT:
Conservative: $[Combined conservative scenarios — show the addition]
Target: $[Combined target scenarios — show the addition]
```

---

### Phase 4 — The Tanya Blackwood Revenue Case

Close the Fast Cash Sprint™ section with Tanya Blackwood's overall revenue argument — a 1-page narrative that frames the entire sprint.

This is Tanya speaking to the client directly. It should read like a CRO briefing a business owner before a board meeting — clear, specific, no fluff.

Cover:
1. Why these 3 strategies were selected over the other options available
2. The total revenue opportunity and the math behind it
3. What the client needs to commit to in order for the sprint to work
4. What happens after the sprint — how it feeds the long-term strategy

Close with Tanya's sign-off.

---

## COMPLIANCE INTEGRATION

Before finalizing this section, run every strategy recommendation through `niche-library/[niche-id].yaml compliance_flags`.

For any compliance flag that affects a strategy:
- Add a "Compliance Note" to that strategy's section
- Modify the approach description to comply (don't just add a disclaimer — actually change the approach)
- If a strategy is significantly restricted, replace it with the next-best option that is fully compliant

**Legal niche example**: Strategy 5 (Referral Program) is high-fit for family law but requires modification — referral fee arrangements with non-attorneys are prohibited in most states. The approach must use non-financial incentives (thank you gifts, charitable donation in client's name) or structure referrals only within the attorney referral fee framework. The skill output must reflect this modification, not just note it.

---

## OUTPUT FORMAT

Produce as Section 6 of the Authority Blueprint™:

**SECTION 6: FAST CASH SPRINT™**
*Your First 90 Days of Revenue Activation*
*Prepared by Tanya Blackwood, CRO — Authority Systems Group™*

Open with:
> *"Before we build anything new, let's look at what's already there. Every professional [niche] business has revenue sitting in its existing relationships — in past clients who haven't heard from you, in referral sources who don't have a reason to call you, in services that have never been properly presented. The Fast Cash Sprint™ is how we go get it."*
> *— Tanya Blackwood, CRO | Authority Systems Group™*

---

## QC CHECK BEFORE HANDOFF

- [ ] All 3 strategies passed the 5-filter selection process
- [ ] Revenue estimates show their math (list size × rate × value)
- [ ] Every strategy references client-specific data (not generic niche language)
- [ ] 90-day calendar is specific enough to hand to an implementer
- [ ] All compliance flags are addressed in the output (not just noted)
- [ ] Sofia Vega's voice is present and sounds like an operator, not a consultant

---

*Authority Systems Group™ — Revenue Skills Library*
*Owner: Tanya Blackwood, CRO | Board review: Sofia Vega | Compliance: Iris Nolan, CTO*
