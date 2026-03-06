# BELIEF_TO_BUY_EMAIL_SEQUENCE.md
# Authority Systems Group™ — Skill: Belief-to-Buy Email Sequence Writer
# Voice: Rhett Callahan, Email Sequence Writer
# Managed by: Marcus Webb, Director of Content Marketing
# Status: ACTIVE — Prompt supplied by Roger 2026-03-04

---

## PURPOSE

Produces complete multi-email sequences mapped to the Belief-to-Buy Framework™ — every email labeled with its exact B/E stage pair, transition from the previous email, and the specific micro-belief it is designed to shift. Produces welcome sequences, nurture sequences, launch sequences, and reactivation sequences for professional service firms and coaching practices.

Distinct from `FIVE_PS_EMAIL_WRITER.md` (single email, complete arc) and `EMAIL_SEQUENCES.md` (Blueprint-level standard sequences). This skill builds custom sequences for specific campaign objectives.

---

## VOICE

**Rhett Callahan, Email Sequence Writer**
See: `/personas/content-team/callahan-rhett-b2b-email-sequence-writer.md`

---

## INPUTS REQUIRED

- `client-context.yaml` — client name, niche, avatar language, brand voice
- `BELIEF_FILTER_MAP.md` — full dual-track map; entry state (where the subscriber is when the sequence starts); exit state (where they should be when the sequence ends)
- Sequence type: welcome | nurture | launch | reactivation | referral capture
- Sequence length: number of emails and send cadence (days between sends)
- Any specific offer, content, or CTA the sequence is building toward

---

## FRAMEWORKS REFERENCED

- Belief-to-Buy Framework™ — every email mapped to a specific B/E stage pair
- Sequence arc architecture: starting stage → ending stage, with micro-shifts across each send
- Transition engineering: each email ends with an open question that the next email answers
- Subject line strategy: open rates are stage-dependent — B1/E1 subjects disrupt, B5/E5 subjects invite

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PROMPT
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**STATUS: ACTIVE** — Prompt supplied by Roger 2026-03-04

---

### THE AUTHORITY ENGINE — Belief-to-Buy Email Prompt Pack

This system qualifies identity, not interest. It delays selling until belief is locked. It reduces objections without handling them. It increases price tolerance without mentioning price. The offer becomes gravity, not persuasion.

---

### STEP 1: CLIENT INPUTS (FILLED ONCE)

Collect the following before writing any emails:

**Business Context**
- Industry / Niche: `{{INDUSTRY}}`
- Who you serve: `{{TARGET MARKET}}`
- Core decision prospects are making: `{{DECISION CONTEXT}}`

**Authority Position**
- Your role / perspective: `{{ROLE}}` (operator, consultant, clinician, strategist, etc.)
- Long-term outcome you optimize for: `{{LONG-TERM RESULT}}`

**Avatar A (DESIRED)**
- Name: `{{AVATAR A NAME}}`
- How they think: `{{AVATAR A BEHAVIORS}}`
- What they optimize for: `{{AVATAR A PRIORITIES}}`
- How they measure success: `{{AVATAR A METRICS}}`

**Avatar B (UNDESIRED)**
- Name: `{{AVATAR B NAME}}`
- How they think: `{{AVATAR B BEHAVIORS}}`
- What they optimize for: `{{AVATAR B PRIORITIES}}`
- How they measure success: `{{AVATAR B METRICS}}`

**Tradeoff Model**
- Neutral tradeoff that explains outcomes (e.g., responsibility transfer, short-term vs long-term, control vs leverage): `{{TRADEOFF MODEL}}`

---

### STEP 2: MASTER AUTHORITY RULE (APPLY TO EVERY EMAIL)

You are writing as a calm authority inside `{{INDUSTRY}}`.

You are not selling, persuading, encouraging, or pitching.

Your role is to describe reality, establish standards, and allow the reader to self-select.

If misaligned readers feel subtly uncomfortable and disengage, the output is correct.

---

### THE 6-EMAIL SEQUENCE

#### EMAIL 1 — META / ABOVE-THE-GAME
**Belief Stage:** Attention → Relevance

Write an authority email that reframes how most people in `{{INDUSTRY}}` think about `{{DECISION CONTEXT}}`. Explain why people obsess over `{{COMMON TACTIC OR TOOL}}` even though the real constraint is `{{STRUCTURAL CONSTRAINT}}`. Do not criticize individuals. Do not recommend solutions. The tone should feel observational and grounded, as if explaining a system from above. End without a CTA.

---

#### EMAIL 2 — BINARY WORLDVIEW / IDENTITY SPLITTER
**Belief Stage:** Relevance

Write an authority email introducing two types of people in `{{INDUSTRY}}` when it comes to `{{DECISION CONTEXT}}`. Type 1: `{{AVATAR A NAME}}`. Type 2: `{{AVATAR B NAME}}`. Describe each only by how they make decisions, what they optimize for, and how they define success. Show the downstream consequences each typically experiences over time. Do not judge. Do not label one as better. End without advice or CTA.

---

#### EMAIL 3 — RESPONSIBILITY TRANSFER / TRADEOFF
**Belief Stage:** Interpretation

Write an authority email explaining why `{{COMMON FRUSTRATION}}` persists in `{{INDUSTRY}}`. Use the tradeoff model `{{TRADEOFF MODEL}}` to explain how responsibility is often transferred away from the operator — and what that costs long-term. Do not blame. Do not rescue. Do not offer solutions. Let the tradeoff explain the outcome. End with calm finality and no CTA.

---

#### EMAIL 4 — "ENOUGH ROPE" EDUCATION
**Belief Stage:** Interpretation → Possibility (hinted)

Write an educational authority email explaining what `{{PROBLEM AREA}}` actually involves in `{{INDUSTRY}}`. Explain why it looks simple on the surface, where most people oversimplify, and what second-order consequences appear later. Do not explain how to implement anything. The reader should understand why partial understanding causes failure. End without offering help or CTA.

---

#### EMAIL 5 — COMPRESSED CASE SIGNAL / PROOF
**Belief Stage:** Possibility

Write a very short authority email (3–6 sentences). Mention someone in `{{INDUSTRY}}` who fits `{{AVATAR A NAME}}` and moved from `{{BEFORE STATE}}` to `{{AFTER STATE}}`. Do not explain how. Reference proof (video, interview, artifact) as optional context. The tone should feel factual, not promotional.

---

#### EMAIL 6 — STANDARD-SETTING / BOUNDARY
**Belief Stage:** Action (Internal Commitment)

Write an authority email that establishes standards for achieving `{{LONG-TERM RESULT}}` in `{{INDUSTRY}}`. Calmly describe who this approach does not work for using `{{AVATAR B BEHAVIORS}}`. Describe the standards required without persuasion or urgency. End with finality, not invitation.

---

### SEQUENCING RULE

Deliver emails in this exact order. Do not reorder. Do not add CTAs until Email 6 or later — and only if the client brief specifies it.

By the end of the sequence, prospects are either aligned and calm, or gone. Both outcomes are correct.

---

### CLIENT USAGE INSTRUCTIONS

- Fill in the variables once (Step 1)
- Run each prompt in order
- Do not add persuasion, hype, urgency, or CTAs unless specified
- These emails are designed to establish authority, force self-selection, protect the client's time, and make aligned prospects obvious

---

## OUTPUT FORMAT

```
SEQUENCE: [Sequence name / type]
Emails: [X] | Cadence: [Days between sends]
Entry stage: [B/E stage pair] | Exit stage: [B/E stage pair]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EMAIL 1 — [EMAIL NAME IN CAPS]
Day [X] | Stage: [B/E stage pair]
Transition from: [Entry state / Day 0 state]
Micro-belief shift: [What specifically changes in the reader's belief track after this email]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subject: [Subject line]
Subject B: [Alternate]

[Full email body]

[Compliance footer]

---

EMAIL 2 — [EMAIL NAME]
[Same format]

[Continue for all emails in sequence]
```

---

## QC CHECK

- [ ] Every email labeled with B/E stage pair and micro-belief shift
- [ ] Each email transitions from the previous — reader's state at start of Email N matches end of Email N-1
- [ ] No email attempts to close before the belief sequence has progressed sufficiently
- [ ] All emails fully written — no structural placeholders or "[insert copy here]"
- [ ] Compliance footers present on all emails
- [ ] Sequence arc is complete — final email reaches the intended exit stage

---

*Authority Systems Group™ — Content Skills Library*
*Owner: Rhett Callahan | Managed by: Marcus Webb | CMO Review: Vivienne Carr*
