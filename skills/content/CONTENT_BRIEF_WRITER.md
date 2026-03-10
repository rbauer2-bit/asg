# CONTENT_BRIEF_WRITER.md
# Authority Systems Group™ — Skill: Content Brief Writer
# Owner: Marcus Webb, Director of Content Marketing
# CMO Review: Vivienne Carr
# Status: ACTIVE — Version 1.0 | Built: 2026-03-09

---

## PURPOSE

Takes a single Idea Block from the `CONTENT_MATRIX_BUILDER.md` output and expands it into a fully populated, specialist-ready production brief. The brief is self-contained — a content specialist can execute from it without reading any other file, accessing the client context, or making any framework decisions.

This skill is the connective tissue between strategy and execution. All 8 system layers are locked before the brief is issued. The specialist's only job is to write.

**This skill does not write content.** It produces the brief. Content creation routes to the appropriate specialist after the brief is approved.

---

## INPUTS REQUIRED

```
1. Idea Block (from CONTENT_MATRIX_BUILDER.md) — all 8 layers assigned
2. client-context.yaml — voice, avatar, brand parameters, compliance flags
3. Media Matrix category definition — Long Form Description + promptTemplate
   (pulled from Airtable: appAn7JSKrI6ZfS9A / tblmIPH5XVMVOlFUP)
4. Platform — determines format constraints, word count, CTA style
```

---

## WHAT THE BRIEF CONTAINS

Every brief produced by this skill includes all of the following sections. None are optional.

```
1.  Brief Header          — client, topic, date, production route
2.  Strategic Objective   — what this piece accomplishes in the conversion sequence
3.  B2B Stage Target      — behavioral success test
4.  ACP Angle Execution   — how to apply the assigned angle
5.  Perspective Direction — how to write from the assigned POV
6.  Calendar Hook         — how to integrate it (if assigned)
7.  Content Category      — format instructions + prompt template from Media Matrix
8.  Topic Framing         — what this piece covers and what it explicitly does NOT cover
9.  Voice Calibration     — client brand voice parameters
10. Hook Brief            — Declan Reyes inputs pre-filled
11. Headline Brief        — Cade Morrison inputs pre-filled
12. Format & Length       — platform-specific constraints
13. CTA Constraint        — stage-appropriate options only
14. Compliance Flags      — attorney clients: ABA gate; all clients: standard
15. Sign-Off Line         — Marcus Webb approval
```

---

## THE BRIEF TEMPLATE

Run every section in sequence. Do not skip or compress any section. The brief fails its purpose if any layer is underspecified.

---

### SECTION 1 — BRIEF HEADER

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTENT BRIEF — [Client Display Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brief ID:       [Client slug]-[###] (sequential per client)
Issued:         [Date]
Platform:       [LinkedIn / Blog / Email / Video / etc.]
Production:     [Specialist Name] → [SKILL_FILE.md]
Approver:       Marcus Webb / Vivienne Carr

SYSTEM LAYERS
─────────────────────────────────────────
Topic:          [From Idea Block]
Category:       [Media Matrix Category]
Angle:          [ACP Category] — [Angle Name]
Perspective:    [#] — [Name]
Stage:          [B#] / [E#]
Calendar Hook:  [Date — Celebration] OR [None]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### SECTION 2 — STRATEGIC OBJECTIVE

State in 2–4 sentences what this piece accomplishes within the client's conversion sequence.

**Include:**
- Where the avatar is right now (belief state, emotional state)
- What this piece is designed to shift
- Where the avatar should be after consuming this piece
- What this piece is NOT trying to do (scope constraint)

**Format:**
```
STRATEGIC OBJECTIVE
─────────────────────────────────────────
[2–4 sentences]

This piece succeeds if the reader [specific belief shift or emotional shift].
This piece does NOT attempt to [scope constraint — usually the job of the next stage].
```

---

### SECTION 3 — B2B STAGE TARGET

Specify the exact stage pair and the behavioral test for success.

```
B2B STAGE TARGET
─────────────────────────────────────────
Belief Track:   [B#] — [Stage Name]
Emotion Track:  [E#] — [Stage Name]

Belief objective:  [What belief should be introduced, reinforced, or cracked?]
Emotion objective: [What feeling should this piece activate, deepen, or resolve?]

Behavioral test:   After reading this, the avatar thinks: "[Specific thought]"
                   After reading this, the avatar feels: "[Specific feeling]"

CTA ceiling: [What is the most the CTA can ask for at this stage — see Section 13]
```

**Stage reference (internal — do not reproduce in brief):**

| Stage | Belief Track | Emotion Track |
|---|---|---|
| 1 | Enemy Belief | Dissatisfaction |
| 2 | Pre-Frame | Contrast |
| 3 | New Worldview | Desire |
| 4 | Internal Alignment | Urgency |
| 5 | Certainty | Relief |

---

### SECTION 4 — ACP ANGLE EXECUTION

Translate the assigned ACP angle into specific writing instructions for this piece.

```
ACP ANGLE
─────────────────────────────────────────
Category:  [Curiosity / Emotional / Logical / Conflict]
Angle:     [Angle Name]
Purpose:   [What cognitive trigger this angle activates]

Execution instructions:
[3–5 specific directions for applying this angle to this topic]

What this angle must NOT do:
[1–2 constraints — common failure modes for this angle in this niche]
```

**Angle execution reference (Marcus Webb's standing notes):**

**CURIOSITY — The Truth About / Exposed / The Great X Hoax / Breaking News**
- Open with the hidden reality, not the context for it
- Name the false assumption directly; give it credit before dismantling it
- The payoff must be specific — vague reveals destroy curiosity faster than they satisfy it
- Do not reveal the full answer in the hook

**CURIOSITY — Breaking News**
- Anchor to a real, current development — not a manufactured urgency claim
- Explain why this matters to THIS avatar specifically, not the industry generally

**EMOTIONAL — Emotional Story**
- The story must be true to the avatar's experience, even if it is Melissa's observation
- Show the internal moment, not just the external event
- The reader must see themselves in the before state before the piece pivots

**EMOTIONAL — Open Letter**
- Direct second-person address ("You have been told...") from the first line
- Tone must be warm and advocative — not preachy or accusatory
- The letter is FOR the avatar, not about them

**EMOTIONAL — Mad as Hell**
- The anger must be on behalf of the avatar, not directed at them
- Name the specific injustice — vague frustration is not anger, it's complaint
- Channel toward a productive reframe, not a dead end

**EMOTIONAL — Man on a Mission**
- This is identity-driven conviction — the practitioner's "why"
- State the mission before the evidence, not after
- Must feel earned, not performed

**LOGICAL — What To Do If**
- Lead with the specific situation, not general advice
- Action steps must be sequenced — not a list of independent tips
- Acknowledge the objection before providing the path

**LOGICAL — Breakthrough**
- The reframe must be genuinely non-obvious — if the reader could have figured it out themselves, it is not a breakthrough
- State the new frame explicitly, then prove it

**LOGICAL — Yea Minus Boo**
- Validate the conventional wisdom before dismantling it
- The "yea" must be generous — if it sounds dismissive, the reader stops trusting the "boo"

**CONFLICT — Us vs Them**
- Define the in-group with precision — the avatar must immediately recognize themselves
- Name the adversarial force without personal attack — systemic critique, not individual accusation
- The "us" must be aspirational, not just sympathetic

**CONFLICT — Declaration of War**
- The declaration must be on a principle, not a person
- State what will no longer be tolerated and why

**CONFLICT — The Industry Lie**
- Name the lie precisely — vague systemic critique reads as opinion, not exposure
- Trace the lie to an incentive structure, not malice
- The practitioner must be positioned as an exception, not a savior

---

### SECTION 5 — PERSPECTIVE DIRECTION

Translate the assigned perspective into specific writing instructions.

```
PERSPECTIVE
─────────────────────────────────────────
Assigned:  [#] — [Name]

Voice instruction: [How the writer should position themselves / the narrator]
What this sounds like: [1–2 example sentence starters or characteristic phrases]
What to avoid: [The failure mode for this perspective in this niche]
```

**Perspective reference:**

**1 — Personal Experience**
- First person, past tense for the experience, present tense for the reflection
- Must cite a specific event, decision, or period — not a general trend
- The lesson must feel discovered, not predetermined
- Avoid: "I always knew that..." (undermines authenticity)

**2 — Audience Experience**
- Second person ("you") or third person composite ("women navigating divorce often...")
- Describes what the avatar is experiencing from the outside with insider precision
- The avatar should feel seen, not studied
- Avoid: Clinical or demographic framing ("clients aged 34–50 typically...")

**3 — Industry Observation**
- First person, present or past tense
- "I've watched," "I've seen," "Over [N] years" — standing and tenure signal authority
- Describes patterns, not individual anecdotes (unless anonymized and clearly composite)
- Avoid: Making claims about what "the industry" does without specificity

**4 — Teaching / Instructional**
- Authoritative but not condescending — explains, does not lecture
- Uses "here's what matters," "the key distinction is," "what most people miss"
- Structures information so the reader can act on it, not just absorb it
- Avoid: Starting with "In order to understand X, you must first understand Y" (too academic)

---

### SECTION 6 — CALENDAR HOOK INTEGRATION

If a calendar hook is assigned, provide specific guidance for how to weave it into the piece.

```
CALENDAR HOOK
─────────────────────────────────────────
[If assigned:]
Date:          [Date]
Celebration:   [Celebration Name]
Connection:    [Why this celebration connects to this topic + angle]

Integration method: [One of the following]
  OPENER    — Use the celebration as the first line; let the irony or connection
              do the pattern interrupt work. Then pivot immediately to the topic.
  METAPHOR  — Weave the celebration in as a recurring reference point. Return to
              it at the midpoint and again at the close.
  BOOKEND   — Open with the celebration, close by returning to it as resolution.

Integration instruction:
[2–3 sentences on specifically how to use this celebration for this piece]

What to avoid:
[1–2 sentences on how this connection could go wrong or feel forced]

[If not assigned:]
Calendar Hook: None assigned. Do not introduce one.
```

---

### SECTION 7 — CONTENT CATEGORY INSTRUCTIONS

Pull directly from the Media Matrix record for the assigned category.

```
CONTENT CATEGORY
─────────────────────────────────────────
Category:    [Name]
Definition:  [Long Form Description from Media Matrix — verbatim]

Prompt template (follow this structure):
[promptTemplate from Media Matrix — verbatim]
```

---

### SECTION 8 — TOPIC FRAMING

Define precisely what this piece covers and what it explicitly does not cover. This prevents scope creep and stage confusion.

```
TOPIC FRAMING
─────────────────────────────────────────
Topic:          [From Idea Block — specific subject]
Content premise: [From Idea Block — 2–3 sentences]

THIS PIECE COVERS:
- [Specific point 1]
- [Specific point 2]
- [Specific point 3 if applicable]

THIS PIECE DOES NOT COVER:
- [Out-of-scope item 1 — usually the job of a later B2B stage]
- [Out-of-scope item 2]

The piece ends when: [Specific endpoint — what is the last thought the reader should have?]
```

---

### SECTION 9 — VOICE CALIBRATION

Pull directly from `client-context.yaml → brand_voice`. Reproduce the parameters exactly. The specialist should not need to read the client file.

```
VOICE CALIBRATION — [Client Name]
─────────────────────────────────────────
Overall tone:     [From brand_voice.overall_tone]
Personality:      [From brand_voice.personality_words — comma-separated]

PREFERRED FRAMING (use these constructions):
[List from brand_voice.preferred_framing]

AVOID (never use these words or constructions):
[List from brand_voice.avoid_words]

Communication style notes:
[From brand_voice.communication_style_notes]

Avatar language to use naturally:
[2–3 specific phrases or terms the avatar uses — from avatar psychographics]
```

---

### SECTION 10 — HOOK BRIEF

Pre-fill all inputs for Declan Reyes. The brief goes to Declan alongside the full brief. He produces 3–5 hook variants; his recommendation is the default unless overridden by Vivienne.

```
HOOK BRIEF → Declan Reyes / HOOK_WRITER.md
─────────────────────────────────────────
Niche:            [Client niche]
Avatar:           [Avatar name + 1-sentence description]
Offer/Service:    [Relevant service from client-context.yaml]
Pain Point:       [Primary fear or frustration from avatar profile]
Desired Outcome:  [Primary desire from avatar profile]
Big Promise:      [The core claim or insight this piece delivers]
Platform:         [Platform]
Stage:            [B#/E#]
Calendar Hook:    [If assigned: "Tie the hook to [Celebration] using [Method]"]

Preferred hook mechanism for this stage:
[B1/E1: Contrast or Fear | B2/E2: Contrast or Curiosity Gap | B3/E3: Transformation or Benefit | B4/E4: Authority or Fear of Loss | B5/E5: Utopia Vision or Command]

Produce: 3–5 variants using different mechanisms. Label each. Include recommendation with rationale.
```

---

### SECTION 11 — HEADLINE BRIEF

Pre-fill all inputs for Cade Morrison. Runs in parallel with the hook brief.

```
HEADLINE BRIEF → Cade Morrison / MASTER_HEADLINE_CREATOR.md
─────────────────────────────────────────
Niche:              [Client niche]
Target Audience:    [Avatar role + situation + experience level]
Primary Topic:      [What the piece is about — one sentence]
Core Problem:       [What the reader is struggling with or wants]
Primary Outcome:    [What changes for the reader after consuming this]
Tone:               [From brand voice — e.g., "warm, direct, empowering"]
Platform:           [Platform — determines character limit]
Stage:              [B#/E#]

Preferred mechanism for this stage:
[B1/E1: Fear or Contradiction | B2/E2: Contradiction or Knowledge Gap | B3/E3: Benefit or Outcome | B4/E4: Knowledge Gap or Authority | B5/E5: Benefit or Command]

Produce: 8–10 variants across at least 3 mechanisms. Label each. Include top recommendation and runner-up with rationale.
```

---

### SECTION 12 — FORMAT AND LENGTH

```
FORMAT & LENGTH
─────────────────────────────────────────
Platform:     [Platform]
Format:       [Post / Article / Email / Script / etc.]
Target length: [Word count or character count — see platform standards below]
Structure:    Hook → [Body structure based on category] → CTA
White space:  [LinkedIn: single sentences, generous line breaks | Blog: paragraphs of 3–5 lines max | Email: short paragraphs]

Platform length standards:
  LinkedIn post (standard):      300–600 words
  LinkedIn article (long-form):  700–1,200 words
  Blog post (SEO):                800–1,500 words
  Email (single):                 250–450 words
  Email (sequence piece):         200–350 words
  Video script (2–3 min):        300–450 words
  Video script (5–7 min):        700–900 words
```

---

### SECTION 13 — CTA CONSTRAINT

The CTA must be appropriate for the assigned B2B stage. A premature CTA destroys the conversion sequence. This section is non-negotiable.

```
CTA CONSTRAINT
─────────────────────────────────────────
Stage:    [B#/E#]
Ceiling:  [Maximum ask for this stage — see table below]
Assigned CTA: [Specific CTA text or instruction]

B2B STAGE CTA CEILINGS:
  B1/E1 — Awareness:     Follow, save, share. Never ask for contact.
  B2/E2 — Pre-Frame:     Follow, save, comment. Soft engagement only.
  B3/E3 — New World:     Download, read more, reply with a question. No pitch.
  B4/E4 — Alignment:     Book a call, get the guide, reply "yes." Soft CTA only.
  B5/E5 — Certainty:     Schedule consultation, apply, contact us. Full CTA allowed.

Violation check: If the content is B1/E1 or B2/E2, no mention of services by name,
no pricing, no "schedule a consultation." If the specialist adds one, Vivienne flags it
in QC and it is removed before delivery.
```

---

### SECTION 14 — COMPLIANCE FLAGS

```
COMPLIANCE
─────────────────────────────────────────
[ATTORNEY CLIENT — run all of the following:]
  [ ] No outcome guarantees or implied results
  [ ] No "specialist," "expert," "certified" without verification
  [ ] No superlatives (best, top, leading, #1)
  [ ] "May," "can," "in our experience" framing for all outcome language
  [ ] Informational disclaimer required at close:
      "This content is for informational purposes only and does not constitute
      legal advice. Every situation is different — consult a licensed attorney
      in your state before making legal decisions."
  [ ] If case descriptions appear: results disclaimer required
  [ ] CTA must not directly solicit a person currently represented by another attorney
  [ ] KY clients: attorney name and office address required in LinkedIn profile (not per-post)
  [ ] ABA Compliance Checker (ABA_COMPLIANCE_CHECKER.md) required before DOCX build

[ALL CLIENTS:]
  [ ] No fabricated testimonials or composite case results presented as specific outcomes
  [ ] No claims that cannot be operationalized or verified
  [ ] No AI/Claude/automation references in client-facing content
```

---

### SECTION 15 — SIGN-OFF

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF APPROVED FOR PRODUCTION

Marcus Webb
Director of Content Marketing — Authority Systems Group™

Vivienne Carr review: [ ] Required  [ ] Routed  [ ] Approved

Production notes:
[Any additional context, timing constraints, or sequencing notes]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## EXAMPLE — FULLY POPULATED BRIEF

**Source:** Idea 001 from Melissa Doss Law matrix (Get Over It Day post)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTENT BRIEF — Melissa Doss Law
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brief ID:       melissa-doss-001
Issued:         2026-03-09
Platform:       LinkedIn
Production:     Sienna Okafor → LINKEDIN_CONTENT_WRITER.md
Approver:       Marcus Webb / Vivienne Carr

SYSTEM LAYERS
─────────────────────────────────────────
Topic:        Why the adversarial divorce approach prevents women from moving forward
Category:     Rant / Contrarian Take
Angle:        Conflict — The Industry Lie
Perspective:  3 — Industry Observation
Stage:        B2 / E2
Calendar:     March 9 — Get Over It Day
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRATEGIC OBJECTIVE
─────────────────────────────────────────
Rachel is currently operating under the enemy belief that hiring a divorce attorney
means entering a war — that conflict is the default mode of the process. She may be
actively receiving advice from friends and family to "fight for everything." This
piece is designed to crack that belief by naming the adversarial system's incentive
structure and creating contrast. She should finish this post thinking: "I didn't know
there was another way to handle this."

This piece succeeds if the reader thinks: "The adversarial approach might be working
against me, not for me."
This piece does NOT attempt to name or pitch collaborative divorce — that is the B3
job. This piece only creates the crack.

B2B STAGE TARGET
─────────────────────────────────────────
Belief Track:  B2 — Pre-Frame
Emotion Track: E2 — Contrast

Belief objective:  Crack the enemy belief: "hiring an attorney turns it into a war."
                   Introduce doubt about the adversarial approach.
Emotion objective: Create contrast between how the adversarial process feels vs. what
                   is possible. Activate a quiet dissatisfaction with conventional wisdom.

Behavioral test:   After reading, the avatar thinks: "Maybe the strategy I've been
                   given isn't actually protecting me."
                   After reading, the avatar feels: Unsettled about the conventional
                   path. Curious about what else might be true.

CTA ceiling: Engagement only. Follow, save, comment. No service mention.

ACP ANGLE
─────────────────────────────────────────
Category:  Conflict
Angle:     The Industry Lie
Purpose:   Exposes a false narrative the industry perpetuates to activate urgency and
           dissatisfaction with the status quo.

Execution instructions:
1. Name the "lie" precisely — not "the legal industry is broken" but "the adversarial
   strategy is designed to extend proceedings, not resolve them."
2. Trace the lie to an incentive structure (billing), not malice.
3. Melissa is positioned as an exception — someone inside the industry who sees it
   clearly — not as a savior.
4. The tone must be observational, not angry. She is reporting, not ranting.
5. Do not name competitors or individual attorneys.

What this angle must NOT do:
- Sound self-righteous or preachy — Melissa is sharing what she has seen, not passing
  judgment on women who chose the adversarial path.
- Overstate the claim — "the entire legal system is corrupt" is not the Industry Lie
  angle. The specific, traceable claim is.

PERSPECTIVE
─────────────────────────────────────────
Assigned:  3 — Industry Observation

Voice instruction: Melissa speaks as a 11-year practitioner who has watched a specific
pattern repeat. She is not speaking from personal moral authority — she is speaking
from professional proximity to hundreds of cases.

What this sounds like:
  "I've watched women enter this process..."
  "Over 11 years in family law, one pattern has stayed with me..."
  "The cases that end well have one thing in common..."

What to avoid: Personal testimony ("this happened to me") or clinical framing ("studies
show that adversarial proceedings..."). It must be her observation, not data.

CALENDAR HOOK
─────────────────────────────────────────
Date:          March 9, 2026
Celebration:   Get Over It Day
Connection:    Get Over It Day is premised on the idea that holding on costs more than
               letting go — which is the exact indictment of the adversarial divorce
               strategy. The adversarial system is designed to make sure you never get
               over it. The irony of the celebration creates the pattern interrupt.

Integration method: OPENER
Integration instruction: Open with the celebration name and one line of irony. Pivot
immediately to the topic. Return to "Get Over It Day" at the close as a call-back
that ties the piece together.

What to avoid: Spending more than two lines on the celebration itself. The hook is
the irony, not an explanation of the holiday.

CONTENT CATEGORY
─────────────────────────────────────────
Category:    Rant / Contrarian Take
Definition:  Challenge a widely accepted belief, industry norm, or conventional wisdom
             that your audience has been told is true. The goal is not to be provocative
             for its own sake — it is to expose a flawed assumption that is costing your
             audience results. Name the belief, dismantle it with evidence or reasoning,
             and replace it with a better framework.

Prompt template:
1. Identify a widely held belief your audience accepts as true but that is wrong,
   outdated, or harmful.
2. State the conventional wisdom clearly and without straw-manning it.
3. Explain specifically why this belief is flawed, with at least one concrete example.
4. Present your contrarian position as the better framework.
5. Anticipate and briefly address the most obvious objection.
6. Close with a clear, direct statement of what the audience should do or believe
   differently as a result.
7. Do not use hedging language. Take a clear position.

TOPIC FRAMING
─────────────────────────────────────────
Topic:    The adversarial divorce approach prevents women from moving forward

THIS PIECE COVERS:
- The incentive structure of adversarial proceedings (billing → extended conflict)
- What Melissa has watched happen to women who followed adversarial advice
- The contrast between adversarial and resolution-focused processes (without naming
  collaborative divorce specifically)

THIS PIECE DOES NOT COVER:
- What collaborative divorce is or how it works (B3 job)
- Melissa's specific services or pricing
- Any critique of specific attorneys, firms, or competitors

The piece ends when: Rachel has a new question — "Is there another way?" — that she
did not have before she started reading.

VOICE CALIBRATION — Melissa Doss Law
─────────────────────────────────────────
Overall tone:  Warm, clear, confident, empowering — never adversarial
Personality:   collaborative, trustworthy, clear, protective, grounded

PREFERRED FRAMING:
- "Guide you through" (not "fight for you")
- "Protect what matters most" (not "win your case")
- "Your next chapter" (not "getting through the divorce")
- "Your children's stability" (not "custody victory")

AVOID: fight, battle, war, win, destroy, attack

Communication style: Melissa explains things clearly. She does not weaponize fear.
Content should feel like advice from a smart, experienced friend who happens to know
family law exceptionally well.

Avatar language: "get through this," "co-parenting relationship," "my kids," "start over"

HOOK BRIEF → Declan Reyes
─────────────────────────────────────────
Niche:           Family Law — Collaborative Divorce, Northern Kentucky
Avatar:          Ready-to-Restart Rachel — woman 34–50, contemplating/beginning divorce,
                 wants out without a war, primary fear is losing time with children or
                 financial security
Offer/Service:   Collaborative divorce representation
Pain Point:      Being told to fight for everything while secretly wanting to avoid
                 prolonged conflict
Desired Outcome: Get through the divorce with dignity, financial stability, and
                 co-parenting relationship intact
Big Promise:     The adversarial strategy may be costing you more than it's protecting
Platform:        LinkedIn
Stage:           B2/E2
Calendar Hook:   Open with Get Over It Day + irony in 2 lines

Preferred mechanism: Contrast or Curiosity Gap for B2/E2
Produce: 3–5 variants, labeled, with recommendation.

HEADLINE BRIEF → Cade Morrison
─────────────────────────────────────────
Niche:           Family Law — Northern Kentucky
Target Audience: Women 34–50 navigating or contemplating divorce, being advised
                 by friends and attorneys to fight for everything
Primary Topic:   The adversarial divorce strategy prevents women from moving forward
Core Problem:    The conventional advice ("get everything you can") may be working
                 against Rachel's actual interests
Primary Outcome: Rachel questions the adversarial path and becomes curious about
                 whether another option exists
Tone:            Warm, direct, observational — not accusatory
Platform:        LinkedIn post
Stage:           B2/E2

Preferred mechanism: Contradiction or Knowledge Gap for B2/E2
Produce: 8–10 variants, labeled. Top recommendation + runner-up with rationale.

FORMAT & LENGTH
─────────────────────────────────────────
Platform:      LinkedIn
Format:        Standard post (not article)
Target length: 350–500 words
Structure:     Hook (2 lines) → Pivot → Observation → Industry Lie → Contrast → Close
White space:   Single sentences or short pairs. Generous line breaks throughout.

CTA CONSTRAINT
─────────────────────────────────────────
Stage:         B2/E2
Ceiling:       Engagement only
Assigned CTA:  "Save this for someone who needs to hear it. Or follow along — I share
               what I've learned over 11 years of family law every week."
Violation check: No service mention, no pricing, no "schedule a consultation."

COMPLIANCE
─────────────────────────────────────────
[ATTORNEY CLIENT]
  [ ] No outcome guarantees
  [ ] No "specialist/expert" claims
  [ ] "May/can/in our experience" framing for outcome language
  [ ] Informational disclaimer at close (required)
  [ ] ABA_COMPLIANCE_CHECKER.md before DOCX build

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF APPROVED FOR PRODUCTION

Marcus Webb
Director of Content Marketing — Authority Systems Group™

Vivienne Carr review: [✓] Required  [✓] Routed  [ ] Approved

Production notes: Calendar-sensitive — publish on March 9 only (Get Over It Day).
If delayed, hold for next relevant calendar hook or remove the opener and reframe
as a standalone industry observation piece.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## QUALITY GATES — BEFORE ISSUING THE BRIEF

- [ ] All 15 sections populated — no section skipped or left at placeholder
- [ ] B2B stage behavioral test is specific enough to evaluate ("the reader thinks X" not "the reader learns about Y")
- [ ] ACP angle execution instructions are actionable — the specialist can follow them without asking clarifying questions
- [ ] Calendar hook integration method specified (OPENER / METAPHOR / BOOKEND)
- [ ] Voice calibration pulled verbatim from client-context.yaml — not paraphrased
- [ ] Hook brief and Headline brief have all inputs filled — no blanks
- [ ] CTA ceiling enforced — stage-appropriate only
- [ ] Attorney clients: all compliance flags present
- [ ] Topic Framing includes explicit "THIS PIECE DOES NOT COVER" section

---

## HANDOFF SEQUENCE

```
1. Brief issued → Declan Reyes (hook variants) in parallel with → Cade Morrison (headlines)
2. Hook and headline sets returned to Marcus Webb
3. Marcus selects recommended variant from each (or routes to Vivienne for judgment call)
4. Full brief + selected hook + selected headline → content specialist
5. Content written → returned to Marcus for QC
6. QC pass → attorney clients: ABA_COMPLIANCE_CHECKER.md → Diana Voss
7. Compliance pass → DOCX build → delivery
```

---

## RELATIONSHIP TO OTHER SKILLS

```
UPSTREAM:   CONTENT_MATRIX_BUILDER.md → produces Idea Block → feeds this skill
PARALLEL:   HOOK_WRITER.md (Declan) + MASTER_HEADLINE_CREATOR.md (Cade) run from this brief
DOWNSTREAM: All content specialist skills receive this brief as their primary input
GATE:       ABA_COMPLIANCE_CHECKER.md runs after specialist output, before DOCX
OUTPUT:     DOCX_BUILDER.md produces the final deliverable from compliant content
```

---

*Authority Systems Group™ — Content Skills Library*
*Owner: Marcus Webb, Director of Content Marketing*
*CMO Review: Vivienne Carr | COO Gate: Preston Adler*
*Built: 2026-03-09 | Version 1.0*
