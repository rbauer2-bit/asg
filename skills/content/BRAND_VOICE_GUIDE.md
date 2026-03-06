# BRAND_VOICE_GUIDE.md
# Authority Systems Group™ — Skill: Client Brand Voice Extraction & Codification
# Produces the client's Brand Voice Guide — used by all content skills
# Voice: Vivienne Carr, CMO
# Run AFTER: NICHE_INTAKE.md | Referenced by all content, email, and video skills

---

## PURPOSE

Extract the client's authentic brand voice from their intake data, existing copy, and review language — then codify it into a specific guide that every downstream skill references. Without this, content produced for the client sounds like ASG, not like the client.

The goal is not to manufacture a voice. It's to identify the voice that already exists — in how the owner speaks, how clients describe them, what language feels right and wrong — and make it replicable.

---

## EXECUTION INSTRUCTIONS

### Step 1 — Source Material Collection

Pull from:
1. `client-context.yaml brand_voice.approved_sample_copy` — best existing copy
2. `client-context.yaml brand_voice.client_testimonial_themes` — how clients describe the business in their own language
3. Client intake Q7 ("describe your best client") — reveals how they see relationships
4. Client intake Q12 ("what makes you different") — reveals their self-perception and values
5. Client intake Q13 ("who you don't want") — reveals implicit brand values by contrast
6. Any client website copy or social posts if provided

### Step 2 — Voice Extraction Analysis

Analyze the source material for:

**Vocabulary fingerprint**: What specific words and phrases appear repeatedly? What vocabulary is conspicuously absent?

**Sentence rhythm**: Short and punchy, or longer and explanatory? Does the natural voice use fragments? Rhetorical questions?

**Authority style**: Does the owner position themselves as the expert who knows best, the guide who walks alongside, the peer who's been through it, or the advocate who fights for the client?

**Emotional register**: What emotions does the voice naturally carry — confidence, empathy, urgency, warmth, directness? What emotions are absent or forced?

**Content defaults**: When the owner explains something, do they default to analogies, stories, data, step-by-step process, or principles?

### Step 3 — Produce the Brand Voice Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRAND VOICE GUIDE
[Client Name] | Prepared by Authority Systems Group™
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE VOICE IN ONE SENTENCE:
[Client Name]'s brand voice is [adjective], [adjective], and [adjective] —
the voice of [specific authority figure archetype] who [what they do for the client
in human terms].

WHAT THIS VOICE SOUNDS LIKE:
[2-3 sentences describing the voice as if you're describing a person.
Not "the tone is professional" but "this voice sounds like a trusted advisor
who tells you the truth your friends are too polite to say — and then
shows you exactly what to do about it."]

VOCABULARY THAT FITS:
[List 10-15 words/phrases that feel native to this brand voice]

VOCABULARY THAT DOESN'T FIT:
[List 10-12 words/phrases that break the voice — feel too corporate, too casual,
too clinical, or too generic]

SENTENCE STYLE:
Average length: [short / medium / long — and what "short" means for this voice]
Use of fragments: [Yes/No/Occasionally — and in what context]
Use of rhetorical questions: [Yes/No — and how they're used]
Use of direct address ("you"): [Frequency and style]

THE AUTHORITY POSITIONING:
How [Client Name] positions their expertise:
[Expert who teaches / Guide who walks alongside / Advocate who fights / Peer who understands]
Evidence of this in source material: [Quote or paraphrase]

THE EMOTIONAL FINGERPRINT:
Primary emotion the voice carries: [e.g., Calm confidence]
Secondary emotion: [e.g., Genuine concern for the client's situation]
Emotion that's absent (and should stay absent): [e.g., Desperation, self-promotion, fear-mongering]

CONTENT DEFAULT:
When [Client Name] explains something, they default to: [Story / Data / Analogy / Process / Principle]
Example from source material: [Quote or paraphrase that illustrates this]

THE VOICE IN THREE WRITING SAMPLES:
Show, don't just tell. Produce three example paragraphs written in the client's voice:

SAMPLE 1 — Explaining a complex topic simply:
[Write a paragraph explaining the core of the Q1 service in the client's voice]

SAMPLE 2 — Addressing a client fear or objection:
[Write a paragraph responding to the primary avatar's most common objection]

SAMPLE 3 — Making a recommendation with conviction:
[Write a paragraph giving a specific recommendation in the client's voice]

WHAT NOT TO DO — ANTI-EXAMPLES:
Three examples of copy that sounds wrong for this brand:
[Show what the voice is NOT — a competitor's generic copy, an overly formal version,
an overly casual version — with brief note on what's wrong about each]
```

### Step 4 — Save and Reference

Save the Brand Voice Guide to:
`/client-onboarding/clients/[slug]/brand-voice-guide.md`

Update `client-context.yaml brand_voice` section with any new fields extracted.

All downstream skills reference this guide before producing content.

---

## QC CHECK

- [ ] The "voice in one sentence" is specific enough that two different writers would produce similar output
- [ ] The three writing samples actually sound like a real person — not generic agency copy
- [ ] Vocabulary lists have at least 10 entries each
- [ ] Anti-examples clearly illustrate what breaks the voice

---

*Authority Systems Group™ — Content Skills Library*
*Owner: Vivienne Carr, CMO*
