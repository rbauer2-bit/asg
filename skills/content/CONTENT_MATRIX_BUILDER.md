# CONTENT_MATRIX_BUILDER.md
# Authority Systems Group™ — Skill: Content Matrix Builder
# Owner: Vivienne Carr, CMO
# Managed by: Marcus Webb, Director of Content Marketing
# Status: ACTIVE — Version 1.0 | Built: 2026-03-09

---

## PURPOSE

Produces a populated content matrix for any ASG client — a structured, calendar-ready library of content ideas with all 8 system layers assigned to each idea. The matrix feeds directly into content specialist workflows. It is the engine behind ASG's ability to produce large volumes of strategically differentiated content at scale without repeating combinations or drifting from the client's conversion architecture.

This skill does not write content. It plans it. Content creation routes to the appropriate specialist skill after the matrix is built.

---

## THE 8-LAYER SYSTEM

Every content idea in the matrix is defined by exactly eight dimensions. Together they produce a combination that is:
- Strategically mapped to the Belief-to-Buy Framework™
- Format-specific (the Media Matrix determines packaging)
- Psychologically differentiated (the ACP Angle determines the belief entry point)
- Perspective-anchored (who is speaking and from what vantage point)
- Timely (the calendar hook creates cultural resonance)
- Production-ready (hook and headline layers brief the writing specialists)

| Layer | What It Defines | Source |
|---|---|---|
| 1. Topic | The specific subject matter | Client context + niche |
| 2. Content Category | The format container | Media Matrix (24 categories) |
| 3. ACP Angle | The belief entry point / psychological trigger | ACP Angle Library (below) |
| 4. Perspective | Who is speaking and from where | Fixed 4-option set (below) |
| 5. B2B Stage | The strategic job — which stage on which track | Belief-to-Buy Framework™ |
| 6. Calendar Hook | The timing tie-in | Marketing Calendar (Airtable) |
| 7. Opening Hook | The scroll-stopper | → Briefs to Declan Reyes |
| 8. Headline | The compressed promise | → Briefs to Cade Morrison |

Layers 1–6 are assigned in this skill. Layers 7–8 are produced by specialists working from the brief this skill generates.

---

## INPUTS REQUIRED

```
1. client-context.yaml         → niche, avatar, brand voice, B2B stage map, priority services
2. Number of ideas requested   → default: 112 (4 buckets × 7 categories × 4 perspectives)
3. Primary platform            → LinkedIn / blog / email / video / Facebook / mixed
4. Content goal                → build authority / generate demand / educate / attract clients
5. Calendar month(s)          → pull from Marketing Calendar Airtable for relevant celebrations
6. Priority B2B stage(s)      → optional; if Roger specifies a funnel gap, weight toward it
```

---

## STEP 1 — DEFINE 4 CONTENT BUCKETS

Content Buckets are the broad thematic pillars the creator will be known for. They are NOT topics. They are categories of expertise.

**Rules:**
- Buckets must be relevant to the niche, avatar, and content goal
- Each bucket must support at least one priority service from `client-context.yaml`
- Buckets must be distinct — no significant overlap
- Buckets must be broad enough to contain 28 ideas each (7 angles × 4 perspectives)

**Naming format:** Short, clear, audience-relevant label. Example: "The Divorce Process Decoded" not "Information About Divorce."

**Derivation method:** Pull from `priority_services` in client-context.yaml. Each priority service maps to one bucket. A fifth service, if present, either merges with a related bucket or becomes its own if volume supports it.

Output: 4 named content buckets with a one-sentence scope definition each.

---

## STEP 2 — SELECT 7 MEDIA MATRIX CATEGORIES

Select 7 content format categories from the Media Matrix for this niche and platform. With 24 available, selection should prioritize:

1. **Platform fit** — LinkedIn favors personal story, observations, rants, lessons, and how-to. Blog favors how-to guides, FAQs, data studies, checklists. Email favors personal story, rants, before/after.
2. **Funnel coverage** — Include at least one category from each phase: awareness (rants, observations, little-known facts), consideration (how-to, case studies, lessons learned), decision (FAQs, checklists, should-ask questions).
3. **Voice fit** — Categories must be executable in the client's brand voice without contradiction.

**The 24 Media Matrix categories (reference):**
Costly Mistakes | Story / Case Study | Data Study / Research | Rant / Contrarian Take |
Timeline / Step-by-Step | Before vs After | Prediction / Forecasting | Curated Post |
Latest News / Current Events | How to Guide | Personal Story Article | Cultural Tie-In |
Survey | Checklist / Cheat Sheet | Should Ask Questions | Listicle |
Frequently Asked Questions | Interview / Question & Answer | Little Known Facts / Trivia |
Review / Analysis | Observations | Lessons Learned | Wins / Failures | Principles / Rules

Output: 7 selected categories with a one-sentence rationale for each.

---

## STEP 3 — SELECT 7 ACP ANGLES

Angles are belief entry mechanisms — they determine how the brain first opens to an idea. Every piece of content uses one primary ACP angle. Supporting angles (3–5) are assigned across the full matrix to ensure psychological coverage.

**The rule:** Different buyers enter belief change through different cognitive triggers. Running angles from all four categories reaches almost every buyer type.

### THE ACP ANGLE LIBRARY

#### Category 1 — CURIOSITY ANGLES
*Purpose: Open attention. Disrupt assumptions. Trigger the need to know.*

| Angle Name | Mechanism | Best For |
|---|---|---|
| The Truth About | Exposes hidden reality | Pre-Frame (B2) |
| Exposed | Reveals what's being concealed | Pre-Frame (B2) |
| The Great [X] Hoax | Names a false belief as a fraud | Pre-Frame (B2) / Enemy Belief (B1) |
| Breaking News | Creates urgency around a new development | Dissatisfaction (E1) |

*Buyer type reached: Curious, analytical, skeptical*

#### Category 2 — EMOTIONAL ANGLES
*Purpose: Create internal resonance. Connect to identity. Move through feeling.*

| Angle Name | Mechanism | Best For |
|---|---|---|
| Emotional Story | Activates empathy and identification | Dissatisfaction (E1) / Contrast (E2) |
| Open Letter | Direct address creates intimacy and urgency | All stages |
| Mad as Hell | Channels frustration into action | Dissatisfaction (E1) |
| Man on a Mission | Identity-driven conviction | Internal Alignment (B4) |

*Buyer type reached: Emotional, identity-driven, motivated by feeling seen*

#### Category 3 — LOGICAL ANGLES
*Purpose: Reframe interpretation. Remove objections. Provide a path.*

| Angle Name | Mechanism | Best For |
|---|---|---|
| What To Do If | Provides a clear action path | New Worldview (B3) / Desire (E3) |
| Breakthrough | Introduces a reframe or paradigm shift | New Worldview (B3) |
| Yea Minus Boo | Acknowledges the valid concern before dismantling it | Pre-Frame (B2) |

*Buyer type reached: Analytical, skeptical, needs logic before emotion*

#### Category 4 — CONFLICT ANGLES
*Purpose: Intensify dissatisfaction. Create urgency. Name the enemy.*

| Angle Name | Mechanism | Best For |
|---|---|---|
| Us vs Them | Defines a clear in-group and an adversarial force | Enemy Belief (B1) / Dissatisfaction (E1) |
| Declaration of War | Signals a movement or change | Enemy Belief (B1) |
| The Industry Lie | Names a false narrative the industry perpetuates | Pre-Frame (B2) |

*Buyer type reached: Angry, frustrated, already dissatisfied, ready to switch*

**Selection rule for 7 angles:** Minimum 1 from each of the 4 categories. The remaining 3 slots go to whichever categories best fit the client's niche, avatar, and current funnel gap.

---

## STEP 4 — ASSIGN PERSPECTIVES

Every content idea is written from one of four perspectives. Rotating perspectives across the matrix prevents voice fatigue and creates variety even when the topic and angle are similar.

| # | Perspective | What It Sounds Like |
|---|---|---|
| 1 | **Personal Experience** | "Here's what I lived through / discovered / did" |
| 2 | **Audience Experience** | "Here's what you're experiencing / what's happening to people like you" |
| 3 | **Industry Observation** | "Here's what I've watched happen across hundreds of cases / clients / years" |
| 4 | **Teaching / Instructional** | "Here's what you need to know / understand / do" |

Assignment in the matrix: Rotate all four perspectives within each bucket × angle combination. No angle should use the same perspective twice in the same bucket.

---

## STEP 5 — MAP B2B STAGES

The Belief-to-Buy Framework™ runs on two parallel tracks that must reach alignment simultaneously before a buying decision occurs.

**BELIEF TRACK:**
- B1 Enemy Belief — The false assumption currently preventing the sale
- B2 Pre-Frame — Cracking the enemy belief; creating contrast
- B3 New Worldview — Introducing the replacement belief
- B4 Internal Alignment — The buyer adopts the new belief as their own
- B5 Certainty — The buyer is ready to act

**EMOTION TRACK:**
- E1 Dissatisfaction — Naming and amplifying the pain of the current state
- E2 Contrast — Showing what's possible vs. what exists
- E3 Desire — Creating a vivid picture of the desired outcome
- E4 Urgency — Introducing the cost of delay
- E5 Relief — Welcoming the buyer into the solution

**Assignment rules:**
1. A full 112-idea matrix must cover all 10 stage positions
2. No single stage should receive more than 20% of the total ideas (max ~22 of 112)
3. Stages B1/E1 and B2/E2 receive the most coverage in cold/awareness content
4. Stages B4/E4 and B5/E5 are reserved for warmer content (email sequences, retargeting, late-stage nurture)
5. Each bucket should produce ideas across at least 4 different stage positions

**Stage assignment by content category (guidelines, not rules):**
- Rant / Contrarian Take → typically B2/E2
- Costly Mistakes → typically B1/E1 or B2/E2
- Story / Case Study → typically E2/B3 or E3/B3
- How to Guide → typically B3/E3
- Before vs After → typically E2/B3
- Lessons Learned → typically B3 or B4
- Observations → typically B2/E1
- Principles / Rules → typically B3/B4
- FAQs / Should Ask Questions → typically B3/E3
- Wins / Failures → typically B3/E3 or B4/E4
- Checklist / Cheat Sheet → typically B3/E3

---

## STEP 6 — ASSIGN CALENDAR HOOKS

Calendar hooks are optional but powerful. They tie a content idea to a specific date, celebration, or cultural moment — creating resonance and timely relevance that makes the content feel spontaneous while being planned.

**Sources (Airtable — Marketing Calendar base):**
- Daily Celebrations (tblSXlLwzCJ07V1qV) — 2,000+ events
- Weekly Events (tblO9kp7AQdIdtw5L)
- Monthly Themes (tblpkJ2yCXun75GGE)
- Rotating Holidays (tblEuoLkShkSDRRXc)
- Marketing Events (tblCpJkaVhQy9RFWp)

**Assignment rules:**
- Not every idea needs a calendar hook. Target 20–30% of ideas in a given matrix
- Prioritize Quirky Celebrations and Cause Based categories — they create the most unexpected connections
- The hook must have a genuine conceptual connection to the topic + angle combination. Forced connections are worse than no hook.
- Competitor-resistant standard: the connection between the celebration and the content should be non-obvious to anyone who doesn't know the system. If a competitor can see the connection immediately, it's too on-the-nose.

**Assignment format in matrix:**
`Calendar: [Date] — [Celebration Name] — [One-sentence connection rationale]`

---

## STEP 7 — GENERATE THE MATRIX

Apply the formula:

```
Content Bucket × Media Matrix Category × ACP Angle × Perspective × B2B Stage [+ Calendar Hook]
= One content idea
```

For each of the 4 buckets:
- Apply all 7 selected Media Matrix categories
- For each category, apply all 4 perspectives
- Assign the most relevant ACP angle for that bucket × category combination
- Assign B2B stage based on the guidelines in Step 5
- Flag calendar hook opportunities where a strong conceptual match exists

**Total:** 4 buckets × 7 categories × 4 perspectives = 112 ideas minimum

---

## OUTPUT FORMAT

### Matrix Summary Header

```
CONTENT MATRIX — [Client Name]
Platform: [LinkedIn / Blog / Email / Mixed]
Built: [Date]
Ideas generated: [N]
B2B coverage: B1–B5 ✓ / E1–E5 ✓
Calendar hooks assigned: [N]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Bucket Definition Block (repeat for each bucket)

```
CONTENT BUCKET [#]: [Name]
Service anchor: [Priority service from client-context.yaml]
Scope: [One sentence]
B2B stages covered in this bucket: [list]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Idea Block (repeat for each idea)

```
IDEA [###]
Bucket: [Bucket Name]
Topic: [Specific subject — one sentence]
Category: [Media Matrix Category]
Angle: [ACP Category] — [Angle Name]
Perspective: [1 Personal / 2 Audience / 3 Industry / 4 Teaching]
Stage: [B# / E#]
Calendar: [Date — Celebration — Connection] OR [None]
Content Premise: [2–3 sentences — what this piece says, what belief it moves, what it leaves the reader thinking]
Production Route: [Content specialist skill + platform]
```

### Optional: Recommended Production Sequence

After the full matrix, produce a prioritized first-30 list:
- Sequence by B2B stage (B1/E1 before B2/E2, etc.)
- Flag any calendar-hooked ideas that must publish on a specific date
- Note which ideas share a bucket and should be spaced at least 5–7 days apart

---

## PRODUCTION ROUTING

After the matrix is approved by Roger / Vivienne, each idea routes as follows:

| Platform | Specialist | Skill File |
|---|---|---|
| LinkedIn post | Sienna Okafor | `LINKEDIN_CONTENT_WRITER.md` |
| Blog / SEO article | Naomi Patel | `BLOG_POST_WRITER.md` |
| Email (single) | Tomás Rivera | `FIVE_PS_EMAIL_WRITER.md` |
| Email (sequence) | Rhett Callahan | `BELIEF_TO_BUY_EMAIL_SEQUENCE.md` |
| Video script | Jade Calloway | `VIDEO_SCRIPT_WRITER.md` |
| Long-form body copy | Clara Ashworth | `BELIEF_TO_BUY_BODY_WRITER.md` |

**Before routing to any specialist:**
1. Run the idea through `CONTENT_BRIEF_WRITER.md` (when built) to generate the full production brief
2. Until `CONTENT_BRIEF_WRITER.md` exists: include Idea Block output as the brief and let the specialist work from it directly
3. For attorney clients: run `ABA_COMPLIANCE_CHECKER.md` after content is written, before DOCX

**Opening hooks and headlines:**
- Every brief includes a request to Declan Reyes (HOOK_WRITER.md) for 3–5 hook variants
- Every brief includes a request to Cade Morrison (MASTER_HEADLINE_CREATOR.md) for 5–8 headline variants
- These can be run in parallel with the body copy or before it — Declan's recommendation is preferred

---

## SAMPLE OUTPUT — 5 IDEAS (Family Law / Melissa Doss Law)

```
IDEA 001
Bucket: The Divorce Process Decoded
Topic: Why most women are surprised by how long the adversarial process actually takes
Category: Costly Mistakes
Angle: Curiosity — The Truth About
Perspective: 3 — Industry Observation
Stage: B2 / E1
Calendar: Mar 15 — Everything You Think Is Wrong Day — adversarial timeline myths
Content Premise: Melissa names the single most common misconception about divorce timelines
and traces it to the adversarial system's incentive structure. She's watched women budget
for 3 months and end up in month 14. The piece cracks the enemy belief ("this will be fast
if I just hire someone aggressive") without pitching collaborative divorce yet.
Production Route: Sienna Okafor → LINKEDIN_CONTENT_WRITER.md

IDEA 002
Bucket: Protecting What Matters Most
Topic: The one financial mistake women make in the first 30 days of separation
Category: Costly Mistakes
Angle: Conflict — The Industry Lie
Perspective: 3 — Industry Observation
Stage: B1 / E1
Calendar: Apr 15 — Tax Day — tax implications of financial decisions during separation
Content Premise: Melissa describes a specific financial move women make in good faith in
the first month of separation that consistently weakens their negotiating position. Named
as an industry failure — attorneys should be warning clients about this and most don't.
Production Route: Sienna Okafor → LINKEDIN_CONTENT_WRITER.md

IDEA 003
Bucket: Protecting Your Children Through the Process
Topic: What a co-parenting relationship looks like two years after an adversarial vs. collaborative divorce
Category: Before vs After
Angle: Emotional — Emotional Story
Perspective: 2 — Audience Experience
Stage: E2 / B3
Calendar: Apr 10 — National Siblings Day — sibling relationships and co-parenting stability
Content Premise: Written from the avatar's perspective — she imagines two versions of her
children's lives two years from now based on the process she chooses today. Not Melissa's
story. Rachel's story, in Rachel's voice. Creates vivid contrast. Plants the new worldview
without stating it directly.
Production Route: Clara Ashworth → BELIEF_TO_BUY_BODY_WRITER.md (long-form LinkedIn article)

IDEA 004
Bucket: Starting the Next Chapter
Topic: The question every woman should ask before hiring a divorce attorney
Category: Should Ask Questions
Angle: Logical — What To Do If
Perspective: 4 — Teaching / Instructional
Stage: B3 / E3
Calendar: None
Content Premise: Melissa teaches one specific question — "What is your default approach when
negotiations break down?" — and explains exactly what to listen for in the answer. This is
practical, actionable, and positions Melissa as the attorney who would give the right answer.
Does not say "hire me." Lets the implication do the work.
Production Route: Sienna Okafor → LINKEDIN_CONTENT_WRITER.md

IDEA 005
Bucket: The Divorce Process Decoded
Topic: Why Melissa started her practice with a collaborative-first philosophy after her first year
Category: Personal Story Article
Angle: Emotional — Man on a Mission
Perspective: 1 — Personal Experience
Stage: B4 / E3
Calendar: Mar 21 — Single Parents Day — mission to protect co-parenting relationships
Content Premise: Melissa's origin story for her collaborative-first approach. Not a resume.
A conviction. She watched something in her first year that she never wanted to be part of
again. This piece moves Rachel from considering collaborative divorce to believing Melissa
specifically is the right attorney — Internal Alignment stage. Vivienne to advise on voice.
Production Route: Clara Ashworth → BELIEF_TO_BUY_BODY_WRITER.md
```

---

## QUALITY GATES

Before delivering the matrix to Roger or Vivienne:

- [ ] All 10 B2B stages represented across the full matrix
- [ ] No single stage exceeds 20% of total ideas
- [ ] All 4 ACP angle categories represented (minimum 1 each)
- [ ] All 4 perspectives used across each bucket
- [ ] No two adjacent ideas (in production sequence) share the same bucket AND category
- [ ] Calendar hooks have genuine, non-obvious conceptual connections
- [ ] Every idea has a clear Content Premise (not a vague topic)
- [ ] Production routes assigned for all ideas
- [ ] Attorney clients: ABA compliance flag noted on every idea that will be produced

---

## CONTENT_BRIEF_WRITER.md (PLANNED — not yet built)

When built, `CONTENT_BRIEF_WRITER.md` will take a single Idea Block from this matrix and expand it into a full production brief including:
- Full topic framing
- Hook brief → Declan Reyes inputs pre-filled
- Headline brief → Cade Morrison inputs pre-filled
- Voice calibration block from client-context.yaml
- B2B stage behavioral objective ("this piece succeeds if the reader thinks/feels X")
- Content category prompt template from Media Matrix
- CTA constraint for stage

Until that skill exists, the Idea Block itself serves as the brief. Specialists have confirmed this is sufficient for standard productions.

---

*Authority Systems Group™ — Content Skills Library*
*Owner: Vivienne Carr, CMO | Managed by: Marcus Webb, Director of Content Marketing*
*Built: 2026-03-09 | Version 1.0*
