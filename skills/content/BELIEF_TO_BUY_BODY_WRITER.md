# BELIEF_TO_BUY_BODY_WRITER.md

Authority Systems Group™ — Skill: Belief-to-Buy Body Content Writer
Voice: Clara Ashworth, Body Content Writer
Managed by: Marcus Webb, Director of Content Marketing
Status: ACTIVE

---

## PURPOSE

Produces the body of any long-form content piece — the paragraphs between the hook and the CTA that must advance the argument, provide evidence, create contrast, and bring the reader to the moment of decision. Operates in conjunction with `HOOK_WRITER.md` (produces the hook) and `OUTLINE_BUILDER.md` (produces the structure).

Called for: LinkedIn articles, blog posts, lead magnet sections, landing page body copy, email body paragraphs, and any content piece where the body must do genuine persuasive work mapped to a specific Belief-to-Buy stage.

---

## VOICE

**Clara Ashworth, Belief-to-Buy Body Content Writer**
See: `/personas/content-team/ashworth-clara-b2b-body-writer.md`

---

## INPUTS REQUIRED

- `client-context.yaml` — client niche, avatar profile, brand voice
- `BELIEF_FILTER_MAP.md` — specific stage pair being served, enemy belief, avatar language at current stage
- `OUTLINE_BUILDER.md` output — the structural map for the piece (do not write body without an outline)
- Hook (from `HOOK_WRITER.md` or supplied separately)
- Target stage pair and content pillar designation

---

## FRAMEWORKS REFERENCED

- Belief-to-Buy Framework™ — every paragraph labeled internally with its function (advance logic / provide evidence / create contrast / bring to decision)
- Four paragraph functions: Logic Advance | Evidence | Contrast | Decision Proximity
- Argument sequencing: never deploy evidence before the argument is established; never create contrast before the current state is viscerally felt

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PROMPT
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATUS: ACTIVE

---

### AI Skill: Belief-to-Buy Content Architect™

#### Purpose

This skill generates body content engineered to move a prospect through the Belief-to-Buy™ cycle.

Instead of writing generic persuasive content, it creates messaging designed to install the specific belief required for the next stage of decision readiness.

The skill adapts to:

- The prospect's current belief stage
- The target belief stage
- The industry or niche
- The desired content format
- The tone of voice

---

#### Core Principle

Prospects do not buy when persuaded.

They buy when the next belief required to justify buying becomes true in their mind.

This skill produces content designed to install that belief.

---

#### Belief-to-Buy Cycle

The skill operates across five cognitive stages.

**Stage 1 — Attention**
Prospect realizes something important may apply to them.
Internal question: *"Should I pay attention to this?"*
Goal: Pattern interrupt and create relevance.

**Stage 2 — Relevance**
Prospect recognizes their situation inside the message.
Internal question: *"Is this really about me?"*
Goal: Identity recognition.

**Stage 3 — Interpretation**
Prospect understands their problem differently.
Internal question: *"Have I misunderstood the real issue?"*
Goal: Reframe the root cause.

**Stage 4 — Possibility**
Prospect believes improvement might be achievable.
Internal question: *"Could this actually work for me?"*
Goal: Reduce perceived risk.

**Stage 5 — Action**
Prospect feels safe moving forward.
Internal question: *"What should I do next?"*
Goal: Make action feel logical and inevitable.

---

#### Skill Inputs

**Required:**

- Industry / niche
- Target prospect description
- Primary problem the prospect experiences
- Desired outcome the prospect wants

**Optional:**

- Prospect belief stage (Attention / Relevance / Interpretation / Possibility / Action)
- Target belief stage
- Content format (article / email / LinkedIn post / video script / webinar section / landing page)
- Tone of voice (authoritative / conversational / analytical / storytelling)
- Length (short / medium / long)

---

#### Stage-Specific Content Architecture

**Stage 1 — Attention**
Objective: Disrupt assumptions and create curiosity.
Techniques: surprising statistics, pattern interruption, myth breaking, provocative questions, industry contradictions.
Structure: Hook → Unexpected insight → Implication → Open loop

Template:
> Most people in {{industry}} believe {{common assumption}}.
> But after working with {{type of clients}}, we've discovered something surprising.
> The real issue isn't {{surface problem}}. It's actually {{hidden factor}}.
> And until that changes, {{negative outcome}} keeps repeating.

---

**Stage 2 — Relevance**
Objective: Create personal identification. Prospect should feel: *"This describes me exactly."*
Techniques: scenario storytelling, identity mirroring, pain articulation, daily frustration descriptions.
Structure: Avatar description → Daily reality → Internal conflict → Emotional resonance

---

**Stage 3 — Interpretation**
Objective: Install a new explanation for the problem. This is the authority stage.
Techniques: root cause analysis, industry misconception exposure, system explanation, causal chains.
Structure: Old explanation → Why it fails → Hidden cause → New interpretation

Template:
> Most people assume {{problem}} happens because {{common belief}}.
> But when you examine what's really happening, a different pattern appears.
> The real driver is {{hidden mechanism}}.
> Which means the solution isn't {{traditional solution}}. It's {{new understanding}}.

---

**Stage 4 — Possibility**
Objective: Reduce perceived risk. Prospect must believe: *"This might actually work."*
Techniques: case studies, examples, simplification, step demonstrations, belief bridge stories.
Structure: Before state → Intervention → Outcome → Transferable insight

---

**Stage 5 — Action**
Objective: Make the next step feel obvious.
Techniques: decision framing, risk reversal, clarity, future pacing.
Structure: Summary of new reality → Decision moment → Safe next step

Template:
> At this point the question usually isn't whether {{solution}} works.
> The real question becomes whether you want to continue dealing with {{old reality}}.
> If not, the next step is simple.

---

#### Emotional Synchronization Layer

| Stage | Emotional State |
| --- | --- |
| Attention | Curiosity |
| Relevance | Recognition |
| Interpretation | Clarity |
| Possibility | Hope |
| Action | Confidence |

---

#### Adaptive Stage Selection

If stage is not specified, analyze the context and estimate the most likely stage:

- Cold traffic → Attention
- Audience aware of problem → Interpretation
- Warm leads → Possibility
- Hot prospects → Action

---

#### Output Structure

Produce:

1. Stage identification
2. Belief being installed
3. Full body content
4. Suggested next stage

Format:

```
Stage Targeted: [stage name]
Belief Installed: [one sentence — the exact belief this content installs]

Body Content:
[full structured content]

Next Stage: [stage name]
```

---

#### Advanced Capability

May generate multi-stage sequences:

- 5-email belief sequence
- LinkedIn content ladder
- Video series
- Webinar flow

Each piece must move one stage forward.

---

#### Governing Rule

Every piece of content must answer: **"Which belief is this installing?"**

If the belief is unclear, the content will not move the prospect forward.

---

#### Invocation

```
Use the Belief-to-Buy Content Architect skill.

Industry: {industry}
Audience: {target avatar}
Problem: {core problem}
Desired Outcome: {goal}
Current Belief Stage: {optional}
Content Format: {format}
Tone: {tone}
Length: {length}
```

---

## OUTPUT FORMAT

Body copy delivered inline with outline section markers:

```
[SECTION: Name from outline]
[Stage: B/E stage pair]
[Function: Logic Advance | Evidence | Contrast | Decision Proximity]

[Body copy for this section]

---
[Next section...]
```

Full piece assembled at end with sections stitched together, ready for final formatting.

---

## QC CHECK

- [ ] Every section maps to the stage pair designated in the outline
- [ ] No section could have been written for a different client in a different niche
- [ ] Evidence is deployed after the argument is established — never before
- [ ] Contrast is visceral, not academic — reader should feel the gap, not just understand it
- [ ] Final section leaves the reader at decision proximity — not pushed, but positioned
- [ ] Client voice consistent throughout — not Clara's voice, the client's

---

*Authority Systems Group™ — Content Skills Library*
*Owner: Clara Ashworth | Managed by: Marcus Webb | CMO Review: Vivienne Carr*
