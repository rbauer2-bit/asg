# BELIEF_FILTER_MAP.md
# Authority Systems Group™ — Skill: Belief-to-Buy Framework™ Mapping
# Core mechanism: Authority Conversion Protocol™
# DUAL-TRACK SYSTEM — Both tracks must reach alignment before BUY
# Run BEFORE any content, messaging, sequence, ad, or video work.
# Version 2.0

---

## THE FRAMEWORK — READ THIS FIRST

The Belief-to-Buy Framework™ is a **dual-track parallel system**. It is NOT a linear funnel.

Two tracks run simultaneously. Both must reach their endpoint before a buying decision occurs. Move only one track and the prospect stalls — intellectually convinced but emotionally frozen, or emotionally hot but intellectually unresolved.

```
BELIEF TRACK (What they THINK is true)
Enemy Belief → Pre-Frame → New Worldview → Internal Alignment → Certainty
                                                                        ↘
                                                                        BUY
                                                                     (Belief + Emotion aligned)
                                                                        ↗
EMOTION TRACK (What they FEEL is true)
Dissatisfaction → Contrast → Desire → Urgency → Relief
```

**The Convergence Principle**:
*People don't buy when they're convinced. They buy when belief and emotion align at the same moment.*

This is why:
- Purely educational content builds belief but not urgency — prospects say "very interesting" and do nothing
- Purely emotional content creates excitement without certainty — prospects act impulsively and regret it
- Authority-based marketing addresses BOTH tracks simultaneously — prospects buy and stay bought

This framework is the operating system of the Authority Conversion Protocol™. Every content piece, email, ad, video, and consultation script produced by ASG maps to specific stages on BOTH tracks.

---

## THE TEN STAGES — DEFINED

### BELIEF TRACK (What They Think Is True)

**B1 — ENEMY BELIEF**
*The assumption keeping them stuck*

NOT ignorance. An active, specific wrong assumption the prospect holds as true — formed from past experience, conventional wisdom, or what they've been told by the wrong people. They're not missing information; they're operating on incorrect information they believe is correct.

You cannot move past the Enemy Belief by providing more information. You must first surface it, validate why it formed, then dismantle it with a better explanation. Marketing that skips this step lands on closed ears, no matter how good the rest of the message is.

**B2 — PRE-FRAME**
*How interpretation changes*

Doesn't argue with the Enemy Belief — changes the lens. Recontextualizes their situation so that evidence they already have starts pointing to a different conclusion. Not a rebuttal. A perspective shift. "Before I tell you X, let me show you why the way most people think about this is the problem."

**B3 — NEW WORLDVIEW**
*A coherent explanation replaces fragments*

The prospect has been operating with a fragmented understanding — pieces of information that never formed a complete picture. The New Worldview assembles those pieces into a coherent explanation. This is the aha moment — they don't just learn something new, they reorganize everything they already knew.

**B4 — INTERNAL ALIGNMENT**
*Past failures finally make sense*

With the New Worldview in place, the prospect can now explain why their past attempts didn't work. This is non-negotiable — if they can't explain past failures within the new framework, the framework feels incomplete and they revert to the Enemy Belief. "That explains why [past attempt] failed. It wasn't that this doesn't work — it was that I was trying to solve the wrong problem."

**B5 — CERTAINTY**
*The decision is no longer emotional or confused*

Intellectual clarity. The prospect knows what the problem actually is, why past attempts failed, and what the correct solution is. The decision feels logical, not like a gamble. NOTE: Certainty alone does not produce action. A prospect can reach B5 and still not buy because the Emotion Track hasn't kept pace.

---

### EMOTION TRACK (What They Feel Is True)

**E1 — DISSATISFACTION**
*Low-grade frustration they've normalized*

Living with a problem they've accepted as the cost of doing business or the reality of their situation. The pain is real but numbed by familiarity. They've stopped expecting things to be different. Most dangerous state for a provider — prospect isn't searching, isn't urgent, and may not respond to relevant marketing because they've mentally filed their problem under "just how it is."

**E2 — CONTRAST**
*Before vs. after becomes visible*

Something makes the gap between their current state and a better state visible and undeniable. A case study. A before/after story. A specific outcome. A peer who achieved what they want. Contrast breaks the normalization of E1. The prospect can now see their current state is not inevitable.

**E3 — DESIRE**
*They want the after-state*

No longer just aware of the gap — they want to close it. Desire is specific: not "things could be better" but "I want what that person has." Emotional investment in the outcome begins here.

**E4 — URGENCY**
*Staying the same starts to feel costly*

Delay has a price. Every day they don't act, something is being lost — money, time, competitive position, quality of life, opportunity. Staying the same is no longer neutral; it's an active cost. CRITICAL: Urgency must be real, not manufactured. Fake scarcity produces short-term action and long-term distrust. The ASG approach surfaces genuine cost of inaction — it doesn't fabricate external pressure.

**E5 — RELIEF**
*Action feels safe and obvious*

The final emotional state before the buy. The prospect has moved from anxious-about-acting to anxious-about-NOT-acting. The decision to buy feels like the resolution of tension, not the creation of it. When E5 is reached before the sale, buyer's remorse is rare and referrals are natural.

---

## EXECUTION INSTRUCTIONS

### STEP 1 — Load Context

Load from `client-context.yaml`:
- `avatars.primary` — full profile including belief_barriers, trigger_events, fears, desires
- `priority_services[0]` — Q1 focus service
- `competitive_landscape.market_positioning_gap`
- `brand_voice.client_testimonial_themes` — real client language reveals emotional track stages

Load from `niche-library/[niche-id].yaml`:
- `content_topics_bank` — especially objection_rebuttal_topics and educational_hooks
- `avatar_archetypes` matching the primary avatar
- `compliance_flags` — any restrictions on emotional or urgency-based messaging

---

### STEP 2 — Identify the Enemy Belief

**This is the most critical step in the entire system. Do not rush it.**

The Enemy Belief for this client's Q1 service must be:
- Specific (not "they don't trust attorneys" — but "they believe lawyering up first makes them look aggressive to the judge")
- Plausible (they formed this belief for understandable reasons — validate why)
- Active (they're currently operating on this assumption, not just theoretically holding it)
- Disqualifying (if left unchallenged, this belief prevents them from hiring regardless of how good the rest of the marketing is)

Sources for identifying it:
1. `avatars.primary.belief_barriers` — especially `provider_distrust` and `solution_skepticism` fields
2. Client's intake Q9 (top objections) — objections are usually the symptom; Enemy Belief is the root
3. Niche library `avatar_archetypes[x].belief_barriers` — cross-validated Enemy Beliefs for this vertical
4. Competitor review language — 1-star and 3-star reviews reveal what prospects feared before hiring

**Write as first-person avatar voice**. Test: would the avatar read this and say "yes, that's exactly what I thought"?

---

### STEP 3 — Map the Full Belief Track

For each of the 5 Belief stages, produce:

```
STAGE: [B1-B5 name]
Avatar's internal monologue at this stage:
"[First-person thought — specific, plausible, in their language]"

What produces the transition to the next stage:
[Content type / message / moment that shifts their interpretation]

What [Client Name] specifically says or shows:
[Concrete message or content piece that creates this shift]
```

Key transitions to nail:
- **Enemy Belief → Pre-Frame**: Does NOT attack the belief directly. Changes the lens first.
- **New Worldview → Internal Alignment**: Must explain past failures — or the New Worldview won't stick.
- **Internal Alignment → Certainty**: The final intellectual proof point. Often a case study or data point.

---

### STEP 4 — Map the Full Emotion Track

For each of the 5 Emotion stages, produce:

```
STAGE: [E1-E5 name]
Avatar's emotional state at this stage:
[Description of what they're feeling — specific, not clinical]

What produces the transition to the next stage:
[What specific content, story, or experience shifts this feeling]

The specific before/after contrast for THIS avatar and THIS service:
[Not generic — specific to the niche, the trigger event, and the outcome]

The real cost of inaction (for E4 — Urgency):
[What is actually being lost every month/quarter they wait? Specific and credible.]

What makes action feel safe (for E5 — Relief):
[The specific reassurance that removes the final emotional friction]
```

---

### STEP 5 — Build the Master Content Map

This table is the operating reference for every downstream content and email skill.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ BELIEF-TO-BUY™ MASTER CONTENT MAP                                                       │
│ [Client Name] — [Q1 Service] — Authority Conversion Protocol™                          │
├──────────┬──────────────────┬────────────────┬──────────────────┬──────────┬───────────┤
│ STAGE    │ BELIEF STAGE     │ EMOTION STAGE  │ CONTENT TYPE     │ CORE MSG │ CTA       │
├──────────┼──────────────────┼────────────────┼──────────────────┼──────────┼───────────┤
│ B1/E1    │ Enemy Belief     │ Dissatisfaction│ Pattern interrupt│          │           │
│ B2/E2    │ Pre-Frame        │ Contrast       │ Reframe content  │          │           │
│ B3/E3    │ New Worldview    │ Desire         │ Education/story  │          │           │
│ B4/E4    │ Int. Alignment   │ Urgency        │ Case study/proof │          │           │
│ B5/E5    │ Certainty        │ Relief         │ Consultation CTA │          │           │
└──────────┴──────────────────┴────────────────┴──────────────────┴──────────┴───────────┘
```

Fill the CORE MSG column with a single sentence that is the primary message for that stage pair — specific to THIS client, THIS service, THIS avatar.

Fill the CTA column with the specific next action appropriate to the avatar's readiness at that stage. (B1/E1 CTA is NOT "call us" — they're not ready. It might be "read this" or "watch this." B5/E5 CTA IS "book a consultation.")

---

### STEP 6 — Identify the Primary Stall Point

Where is the prospect pool LARGEST and MOST STUCK for this niche?

Review:
- Which `belief_barriers` fields in client-context.yaml have the most friction?
- Which intake Q9 objections appear most frequently?
- Which niche library `objection_rebuttal_topics` indicate the deepest resistance?

Determine whether the primary stall is on the **Belief Track** (intellectual — they don't believe the solution works), the **Emotion Track** (emotional — they believe it but fear acting), or **both** (dual stall — requires content that moves both simultaneously).

**This determines**:
- Which stage pair gets the most content volume and copy investment
- Which email in a sequence does the heaviest lifting
- What the consultation must accomplish in the first 10 minutes

---

### STEP 7 — Write the Convergence Statement

A single paragraph describing exactly what must happen simultaneously on both tracks for this specific avatar to reach the BUY.

Format:
> "[Avatar name] reaches the buying decision when [Belief Track endpoint — what they're now certain of] AT THE SAME MOMENT that [Emotion Track endpoint — what they now feel]. The content and consultation that gets them there must accomplish both. [Client Name] achieves this by [specific mechanism — what they do/say/show that produces both endpoints simultaneously]."

This paragraph becomes:
- The brief for the consultation close script
- The final email in every nurture sequence
- The CTA framework for all bottom-of-funnel content

---

## OUTPUT DOCUMENT FORMAT

```
BELIEF FILTER MAP™
[Client Name] | [Primary Service] | Prepared by Authority Systems Group™
Authority Conversion Protocol™

SECTION 1: THE ENEMY BELIEF
[Avatar first-person statement + why they formed it]

SECTION 2: BELIEF TRACK — FULL MAP
[5 stages with avatar monologue + transition trigger for each]

SECTION 3: EMOTION TRACK — FULL MAP
[5 stages with emotional state + transition trigger for each]

SECTION 4: MASTER CONTENT MAP TABLE
[Stage pair → content type → core message → CTA]

SECTION 5: PRIMARY STALL POINT ANALYSIS
[Which stage pair, which track, and the strategic implications]

SECTION 6: THE CONVERGENCE STATEMENT
[The single paragraph that briefs every bottom-of-funnel execution]
```

---

## HOW DOWNSTREAM SKILLS USE THIS DOCUMENT

| Skill | Reads | Uses |
|---|---|---|
| `CONTENT_STRATEGY.md` | Sections 2, 3, 4 | Maps each content piece to a stage pair |
| `QUARTERLY_CONTENT_CALENDAR.md` | Sections 4, 5 | Sequences stage pairs across 13 weeks |
| All email sequence skills | Section 4 | Each email targets a specific stage pair |
| `VIDEO_STRATEGY.md` | Sections 1, 2, 4 | Enemy Belief = Video #1 topic |
| `AD_STRATEGY.md` | Section 5 | Primary Stall Point determines targeting |
| Consultation scripts | Section 6 | Convergence Statement = close framework |
| `COLD_OUTREACH.md` | Sections 1, 2 | Opens at Enemy Belief or Pre-Frame stage |

---

## MANDATORY CONTENT QUALITY TEST

Before any content piece from any skill is considered complete, apply this test:

1. **Belief check**: Which stage on the Belief Track does this address? (Name it specifically.)
2. **Emotion check**: Which stage on the Emotion Track does this address? (Name it specifically.)
3. **Alignment check**: Are both answers from the same stage pair? (If not — the content is pulling in two directions and needs revision.)
4. **Convergence check** (bottom-of-funnel content only): Does this content simultaneously deliver Certainty AND Relief? If not — it will not close.

Content that fails this test does not pass Gate 2 (Messaging Integrity).

---

*Authority Systems Group™ — Core Framework Reference*
*Framework: Belief-to-Buy™ | Mechanism: Authority Conversion Protocol™*
*Version 2.0 — Dual-track architecture*
*Owner: Dr. Raymond Cross, Board | Application: Vivienne Carr, CMO*
