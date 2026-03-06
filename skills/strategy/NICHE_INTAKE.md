# NICHE_INTAKE.md
# Authority Systems Group™ — Skill: Client Context Builder
# Merges niche library YAML + intake questionnaire into client-context.yaml
# Run this first. Everything else depends on it.

---

## PURPOSE

Transform raw intake questionnaire responses and niche library data into a fully populated `client-context.yaml` that every downstream skill can read without ambiguity.

This skill produces the data spine. Do not proceed to any other skill until this file is complete and all required fields are populated.

---

## INPUTS REQUIRED

1. **Niche library file**: `/niche-library/[niche-id].yaml`
2. **Intake questionnaire responses**: Raw client answers (text, form output, or notes from discovery call)
3. **Engagement metadata**: Client name, slug, onboard date, assigned account lead

---

## EXECUTION INSTRUCTIONS

### Phase 1 — Load and Cross-Reference

Load the niche library YAML for this client's vertical. Identify:
- The closest matching `priority_services_archetypes` to the client's actual top services
- The avatar archetype(s) that best match the client's described ideal client
- The top 5 recommended fast cash strategies pre-rated for this niche

Cross-reference niche library defaults against the client's specific answers. Client-specific data always overrides niche library defaults. Flag any contradictions for review.

### Phase 2 — Populate Engagement Metadata

Fill all fields in the `engagement:` block:
- Generate `client_slug` as: lowercase, hyphenated, no special characters
  - Example: "Riverside Family Law Group" → `riverside-family-law`
- Set `engagement_phase` to `onboarding`
- Set `assigned_account_lead` to `Roger Bauer`

### Phase 3 — Populate Business Profile

Map intake questionnaire answers to `business:` fields. For any field not directly answered:
- Use niche library `typical_business_profile` as a reasonable default
- Mark with `# ESTIMATED` comment so it can be confirmed later
- Never leave a field blank — use `"unknown"` only as last resort

**Critical fields that must be confirmed (not estimated)**:
- `crm_platform` — automation skill output depends on this
- `avg_transaction_value` — revenue projections depend on this
- `client_count_past_12mo` — reactivation strategy sizing depends on this

### Phase 4 — Priority Services Ranking

Map the client's 4 highest-revenue services to `priority_services:` blocks ranked 1-4.

For each service:
- Pull `avg_value` and `margin_estimate` from client answers or niche library archetypes
- Assign quarterly content focus: rank 1 = Q1, rank 2 = Q2, rank 3 = Q3, rank 4 = Q4
- Write a 1-sentence `ideal_avatar_summary` pulling from the matching niche library avatar

If client lists fewer than 4 services, note this and flag for discussion. Do not fabricate services.

### Phase 5 — Avatar Construction

Build the primary avatar profile under `avatars.primary`:

1. Select the closest matching archetype from niche library `avatar_archetypes`
2. Override with specific language from the client's intake answers (Q7: "describe your best client")
3. Map client-provided objections (Q9) to the appropriate `belief_barriers` fields
4. Pull trigger events from both niche library and client's Q8 answer
5. Assign avatar name: follow niche library convention (alliterative, memorable, e.g., "Asset-Anxious Alan")

If client's described avatar diverges significantly from niche library archetypes, build from client data and note the divergence.

### Phase 6 — Competitive Landscape

Map Q11 (competitors) and Q12 (differentiators) to `competitive_landscape:` block.

For `market_positioning_gap`:
- Cross-reference client's differentiators against niche library `typical_positioning_gaps`
- Identify the most specific unclaimed positioning statement available
- Write as: "[Client Name] can own the position of [specific claim] because [competitor weakness]"

### Phase 7 — Fast Cash Priorities

Select top 3 strategies from the niche library `top_5_recommended` list, filtered against:
- Client's current assets (do they have a past client list? → reactivation applicable)
- Client's CRM capability (does their system support automation? → which strategies require it)
- Client's team capacity (solo vs. team affects implementation timeline)
- Any niche compliance flags that restrict certain strategies

For each selected strategy, write:
- `rationale`: 2-3 sentences specific to THIS client, not the niche generally
- `estimated_revenue_impact`: Use the formula: (list size or transaction volume × estimated response rate × avg transaction value). Show the math.
- `implementation_timeline`: Days 1-7 / Days 8-21 / Days 22-30 format
- `required_assets`: Specific list of what the client must provide

### Phase 8 — Brand Voice

Pull from:
- Q10 (what clients say in reviews) → `client_testimonial_themes`
- Q12 (differentiators) → `personality_words`
- Any sample copy from client website or materials → `approved_sample_copy`
- Q13 (who they don't want) → reveals implicit brand values, add to `communication_style_notes`

### Phase 9 — Goals and KPIs

Map Q19-22 to `goals:` block. For KPI baseline fields:
- Use client-provided numbers where available
- Estimate from niche library `typical_business_profile` where not
- Mark all estimates with `# ESTIMATED`

For target fields (yr1 targets):
- Apply conservative growth assumptions: 25-40% revenue growth year 1 for businesses under $1M; 15-25% for $1M-$3M
- Base lead volume targets on conversion rate improvement, not just volume increase

### Phase 10 — Validate and Flag

Before saving, run this check:

**Required fields — must not be blank or "unknown"**:
- `client_slug`
- `business.city` and `business.state`
- `niche.vertical`
- `priority_services[0].name` and `.avg_value`
- `avatars.primary.avatar_name`
- `avatars.primary.trigger_events` (at least 2)
- `avatars.primary.belief_barriers.provider_distrust`
- `competitive_landscape.market_positioning_gap`
- `fast_cash_priorities[0].strategy_name` and `.rationale`
- `goals.ninety_day` and `goals.year_one`

**Flag for human review (add `# NEEDS CONFIRMATION` comment)**:
- Any field estimated from niche library rather than client data
- Any compliance flag that may restrict a recommended strategy
- Any contradiction between client answers and niche library norms
- Any field where client's answer was vague or ambiguous

---

## OUTPUT

Save completed file to:
`/client-onboarding/clients/[slug]/client-context.yaml`

Also generate a brief **Intake Summary Memo** (internal, not client-facing):
- Client name and slug
- Niche match and any divergences from library
- Top 3 fast cash strategies selected and one-line rationale for each
- List of fields flagged for confirmation
- Any compliance flags activated
- Estimated time to first deliverable

---

## QUALITY CHECK BEFORE PROCEEDING

- [ ] Zero blank required fields
- [ ] All revenue estimates show their math
- [ ] Avatar profile is specific enough that a copywriter could write to this person without asking any questions
- [ ] Positioning gap is specific and defensible — not generic ("be better than competitors")
- [ ] Fast cash rationale references client-specific data, not just niche library copy

---

*Authority Systems Group™ — Strategy Skills Library*
*Owner: Daniel Frost, CSO | Reviewed by: Roger Bauer, Director*
