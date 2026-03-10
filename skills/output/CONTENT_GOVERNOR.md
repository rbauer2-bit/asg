# CONTENT_GOVERNOR.md
# Authority Systems Group™ — Output Quality Governor
# Applies to: All client-facing deliverables produced by ASG skills
# Load order: After ACP_DOCTRINE.md and BELIEF_FILTER_MAP.md, before any content skill executes
# Version 1.0

---

## PURPOSE

This governor enforces two rules across all ASG output:

1. **No-Repeat Protocol** — Within any single deliverable, every insight, explanation, or framework definition is stated exactly once. Subsequent sections reference rather than restate. Clients are professionals. They read what was written. Do not treat them otherwise.

2. **Niche Content Library Protocol** — Niche-level insights are written once and reused across clients in the same niche. Only client-specific data (competitors, credentials, history, pricing, geography) is generated fresh per engagement. The wheel is not reinvented. The wheel is reused. The tire size is changed.

These rules apply to every Blueprint section, every email sequence, every content strategy, and every other client-facing document produced by any ASG skill.

---

## RULE 1 — NO-REPEAT PROTOCOL

### The Principle

Volume does not equal value. A 70-page Blueprint that says the same thing in four different sections is not four times as valuable as a 20-page Blueprint that says it once, precisely. It is less valuable — because it signals that the producer couldn't distinguish what mattered from what filled space.

Every statement in a client deliverable must earn its place. If a statement's only job is to repeat something already established, cut it.

### What "Restating" Looks Like (avoid all of these)

- Explaining the Belief-to-Buy Framework™ in Section 4 AND again in Section 8 (Content Strategy)
- Describing the client's practice area in Section 1 AND Section 3 AND the email sequences
- Introducing the same avatar frustration in Section 3 (Market Analysis), Section 4 (Belief Map), AND Section 8 (Content Strategy)
- Opening multiple sections with the same problem statement in different words
- Restating a persona's credentials every time they appear (after first introduction)
- Restating niche market size statistics that appeared earlier

### How to Handle It — Reference Protocol

Once something is established, reference it — don't restate it. Use these reference patterns:

| What Was Established | Reference Pattern (examples) |
|---------------------|------------------------------|
| Framework definition | "The Belief-to-Buy™ Framework (Section 4) maps this precisely..." |
| Client context | "[Client name]'s positioning advantage — established in Section 3 — means..." |
| Avatar insight | "The avatar profile's primary fear (Section 3C) drives the sequencing here..." |
| Market stat | "Against the [X]-size market noted in Section 3B..." |
| Enemy Belief | "The Enemy Belief identified in Section 4 — [brief restatement, one clause] — is what this content directly addresses." |
| Prior recommendation | "Building on the Fast Cash Sprint (Section 6)..." |

A brief one-clause callback is acceptable and useful for reader orientation. A full re-explanation of something already covered is not.

### Section-Level Rules

**Section 1 (Executive Summary):** Establishes the three core opportunities and the strategic frame. Nothing in Sections 2-13 should re-explain these opportunities from scratch — they reference them.

**Section 2 (Director's Briefing):** Adds Roger's direct read of the situation. Does NOT re-summarize the executive summary. Builds on it.

**Section 3 (Market Analysis):** Establishes all niche and competitive context — competitor profiles, avatar profile, market size, positioning gap, Authority Statement. These facts are established here and referenced elsewhere. They are NOT re-explained in Section 4, 5, or 8.

**Section 4 (Belief-to-Buy Map):** Establishes the full B1-B5 / E1-E5 map, Master Content Map, and Convergence Statement. Sections 5, 8, and 10 reference this map by stage pair — they do not re-explain what the stages mean.

**Section 8 (Content Strategy):** References the stage pairs from Section 4 by name. Does NOT re-explain what B1 or E3 mean. The reader has Section 4.

**Section 10 (Email Sequences):** Each email header cites its stage pair. The sequences do not re-introduce the framework. They execute it.

**Section 13 (QC Sign-Offs):** References the four gates. Does not summarize the document.

### Persona Introductions

Each team persona is introduced by full name and title at their **first appearance** in the deliverable. After that, first name or title only is sufficient. Do not restate credentials at every section they appear.

- First appearance: "Daniel Frost, Chief Strategy Officer" with one-sentence context
- Subsequent appearances: "Daniel" or "the strategic plan" — not "Daniel Frost, ASG's Chief Strategy Officer with 20 years of..."

---

## RULE 2 — NICHE CONTENT LIBRARY PROTOCOL

### The Principle

When a Blueprint is produced for a family law attorney in Phoenix, Arizona — every niche-level insight about family law buyer psychology, market dynamics, and enemy beliefs that was developed for a family law client in Louisville, Kentucky is still structurally true. The avatar fears losing their children in Phoenix the same way they fear it in Louisville. The enemy belief about what "lawyering up first" signals to a judge is the same in both markets.

Only the specifics change: the competitor names, the geography, the client's own story, the local review ecosystem, the fast cash assets available.

Reuse what is structurally transferable. Generate fresh what is genuinely client-specific. Never confuse the two.

### Content Classification Taxonomy

Every section and subsection of every deliverable maps to one of three categories:

**NICHE-CORE** — Structurally identical across all clients in the same niche. The specific language may be pulled from the niche library (`/niche-library/[niche-id].yaml`) with geographic and client-name variables substituted. Regenerating from scratch wastes time and risks producing an inferior version of something already established.

**CLIENT-SPECIFIC** — Unique to this client. Must be generated fresh. Cannot be reused from another client's deliverable — not even as a starting point without heavy customization.

**HYBRID** — The framework is niche-level (reusable); the data points inside it are client-specific (fresh). Pull the framework shell from the niche library, fill the data slots from `client-context.yaml`.

### Blueprint Section Classification

| Blueprint Section | Classification | Reuse Approach |
|------------------|---------------|----------------|
| Section 1: Executive Summary | CLIENT-SPECIFIC | Fresh — references client's specific situation, numbers, and opportunities |
| Section 2: Director's Briefing | CLIENT-SPECIFIC | Fresh — Roger's read of THIS client, not the niche |
| Section 3A: Competitive Landscape | CLIENT-SPECIFIC | Fresh — named local competitors; niche rating criteria are NICHE-CORE |
| Section 3B: Market Opportunity | HYBRID | Market size narrative = NICHE-CORE (adjust geography); revenue opportunity math = CLIENT-SPECIFIC |
| Section 3C: Avatar Profile | HYBRID | Avatar archetype = NICHE-CORE (from niche library); trigger events and fears language can be reused with name/city substitution |
| Section 3D: Positioning Gap + Authority Statement | CLIENT-SPECIFIC | Fresh — based on local competitor weaknesses |
| Section 4: Belief-to-Buy Map | HYBRID | Enemy Belief, B1-B5 monologues, E1-E5 states = NICHE-CORE (same niche, same psychology); specific "what [Client] says/shows" = CLIENT-SPECIFIC |
| Section 5: 1-Year Strategic Plan | HYBRID | Quarterly Authority Rotation™ structure = NICHE-CORE; specific named actions, timelines, and KPI targets = CLIENT-SPECIFIC |
| Section 6: Fast Cash Sprint™ | CLIENT-SPECIFIC | Fresh — based on client's actual assets, list size, CRM state |
| Section 7: KPI Dashboard | HYBRID | KPI categories and 5-metric structure = NICHE-CORE; baseline and target numbers = CLIENT-SPECIFIC |
| Section 8: Content Authority Strategy™ | HYBRID | Content pillar structure and % allocation = NICHE-CORE; named content piece titles and briefs = CLIENT-SPECIFIC |
| Section 9: Niche Website Strategy | HYBRID | Platform specs and architecture = NICHE-CORE; domain, keyword list, local SEO targets = CLIENT-SPECIFIC |
| Section 10: Email Sequences | HYBRID | Sequence architecture and stage-pair mapping = NICHE-CORE; all copy must be written in client's brand voice = CLIENT-SPECIFIC |
| Section 11: Lead Magnet & Referral Program | HYBRID | Lead magnet format and compliance structure = NICHE-CORE; title, TOC, and referral incentive design = CLIENT-SPECIFIC |
| Section 12: Priority Services & Next Steps | CLIENT-SPECIFIC | Fresh — owner-assigned actions tied to THIS client's situation |
| Section 13: QC Sign-Offs | CLIENT-SPECIFIC | Fresh — actual approval statements for THIS deliverable |

### How to Execute Niche Reuse

**Step 1 — Load the niche library file:**
`/niche-library/[niche-id].yaml`

Check whether a prior Blueprint has been produced for this niche. If yes, the following are available for reuse from that prior work:
- Avatar archetype narrative (substitute city, local court system references if applicable)
- Enemy Belief statement and B1 monologue (niche-level psychology does not change by geography)
- B2-B5 monologue frameworks (substitute client-specific proof points)
- E1-E5 emotional state descriptions (substitute specific contrast examples)
- Content pillar titles and angle descriptions
- Email sequence architecture and subject line frameworks (not the copy — the architecture)
- KPI category definitions and benchmark ranges

**Step 2 — Identify what is genuinely new:**
- Named local competitors (fresh every time)
- Client's own credentials, awards, story, testimonials
- Local market review ecosystem (Google review count, local directory presence)
- Fast Cash assets (current list, CRM, referral partner relationships)
- Revenue projections (based on THIS client's numbers)
- All email body copy (brand voice varies client to client)

**Step 3 — Variable substitution for reused blocks:**
When reusing niche-core content, replace the following variables before including in the deliverable:

```
[CLIENT_NAME]          → Client's full business name
[ATTORNEY_NAME]        → Client's name
[CITY]                 → Client's city
[STATE]                → Client's state
[PRACTICE_AREA]        → Client's primary Q1 focus service
[PRIOR_CLIENT_REF]     → Do NOT include — remove any reference to prior client
[COMPETITOR_NAMES]     → Replace with local competitors from client-context.yaml
```

**Critical:** Remove all references to prior clients when reusing content. The client should never see evidence that this language was adapted from another engagement. The Confidentiality Notice on every Blueprint is the standard — these are insights prepared exclusively for this client.

### What Reuse Is NOT

Reuse does not mean copy-paste of prior client documents. It means:
- The niche library YAML is the reuse source, not prior client files
- Structural frameworks, avatar psychology, and stage-pair architecture travel with the niche
- Client identity (name, story, credentials, market position) is always fresh
- The deliverable must read as though it was built for this client — because the client-specific layer was

---

## ENFORCEMENT

This governor is enforced at two points:

### During Content Production
Every content skill must check:
- "Have I already established this point in a prior section?" — If yes, reference it, don't restate it
- "Is this content niche-level or client-specific?" — Pull from niche library if niche-level; generate fresh if client-specific
- "Am I explaining a framework the reader was already given?" — If yes, use a one-clause callback, not a full re-explanation

### During QC (Gate 4 — Delivery Standard, Preston Adler)
The Final QC Checklist in REPORT_FORMATTER.md includes a Governor Compliance check. Before export, run:

- [ ] No framework (Belief-to-Buy, ACP, Cognitive Sequencing) is explained more than once in full
- [ ] No client context data is restated in multiple sections (established once, referenced after)
- [ ] No persona credentials are introduced more than once
- [ ] All niche-core sections have had client-variable substitution confirmed (no prior client names, prior city references, or prior competitor names remain)
- [ ] Each section adds something new — no section is a rewording of a prior section

---

## A NOTE ON DOCUMENT LENGTH

A longer document is not a more valuable document. A complete document is valuable. A redundant document is a liability — it signals that the producer couldn't distinguish signal from filler, and it wastes the client's time.

The Authority Blueprint™ floor (anna-aleksander-law, 2026-03-02) is the completeness standard — not the length standard. If a Blueprint exceeds that length through genuine additional content, that is correct. If it exceeds that length through repetition and restatement, that is a failure.

Every page must justify its presence. Every sentence must earn its place.

---

*Authority Systems Group™ — Output Quality Governor*
*Owner: Preston Adler, COO | Quality lens: Vivienne Carr, CMO*
*Version 1.0*
