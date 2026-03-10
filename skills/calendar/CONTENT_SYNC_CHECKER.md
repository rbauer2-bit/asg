# CONTENT_SYNC_CHECKER.md
# Authority Systems Group™ — Skill: Content Sync Checker
# Voice: Sloane Mercer, Calendar Team Director
# Managed by: Sloane Mercer, Calendar Team Director
# Status: ACTIVE — Prompt supplied by Roger 2026-03-08

---

# SKILL: Content Sync Checker
**Calendar & Marketing Team — Authority Systems Group**
Version 1.0

---

## PURPOSE

This is a mandatory pre-flight check. It runs before any content production begins for a client. Its job is to surface all existing content for the target month(s), extract the campaign context already established across platforms, and package that context into a **Sync Context Block** so that every new content piece is part of a cohesive campaign — not an isolated deliverable.

If existing content is found, the Sync Context Block becomes a required input for the downstream content skill. The content writer does not proceed without it.

---

## WHEN THIS SKILL IS ACTIVATED

Activate at the start of every content production request, before invoking:
- Cleo Strand (Dopamine Ladder / LinkedIn Pack)
- Milo Vance (YouTube Long-Form Script Writer)
- Naomi Patel (Blog Post Writer)
- Sienna Okafor (LinkedIn Content Writer)
- Lena Ashby (Calendar Content Writer)
- Any other content specialist when a specific month is in scope

**Exception:** If Roger explicitly states "standalone piece — no sync needed," skip this check and proceed directly to the requested content skill.

---

## REQUIRED INPUTS

1. **[Client Slug]** — folder name under `client-onboarding/clients/` (e.g., `legal-growth-dynamics`)
2. **[Target Month(s)]** — the month(s) the requested content will cover (e.g., April 2026, or April–May 2026 for a pack that spans months)
3. **[Content Type Requested]** — what is being produced (LinkedIn, YouTube, Blog, Email, Calendar, etc.)

---

## EXECUTION STEPS

### STEP 1 — Locate the Client Output Folders

```
Markdown files:  /client-onboarding/clients/[client-slug]/outputs/md/
DOCX files:      /client-onboarding/clients/[client-slug]/outputs/docx/
PDF files:       /client-onboarding/clients/[client-slug]/outputs/pdf/
```

Use the Glob tool to list files in each typed subfolder. For content sync purposes, `.md` files in `outputs/md/` are the primary source. Reference `.docx` and `.pdf` listings only to confirm delivery status.

If any subfolder is missing, note it in the Sync Context Block but do not halt. Proceed with whatever exists.

---

### STEP 2 — Filter Files by Target Month(s)

Scan file names in `outputs/md/` for month references matching the target month(s). Look for:

| Content Type | Subfolder | File Name Pattern |
|---|---|---|
| Marketing Calendar | `outputs/md/` | `*[month]*marketing-calendar*` |
| LinkedIn Pack | `outputs/md/` | `*linkedin*` (check date/month in front matter) |
| YouTube Scripts | `outputs/md/` | `*youtube*[month]*` or `*[month]*youtube*` |
| Blog / Articles | `outputs/md/` | `*blog*[month]*` or `*articles*[month]*` |
| Theme Selection | `outputs/md/` | `*[month]*theme-selection*` |
| Authority Blueprint | `outputs/md/` | `*authority-blueprint*` (always relevant — contains annual/quarterly direction) |

Month matching is case-insensitive. Match full month name (e.g., "april", "may") or 4-digit year if included.

If target content spans two months (e.g., a 30-day LinkedIn pack starting April 1 runs into May), check both months.

---

### STEP 3 — Read and Extract Context from Found Files

For each matching file found, read the file and extract the following:

**From Marketing Calendar:**
- Primary monthly theme
- Belief stage(s) in focus
- Weekly events and key daily celebrations selected
- CTA in use for the month

**From LinkedIn Pack:**
- Monthly strategy overview (avatar, psychological drivers, enemy belief)
- 30-day topic arc and belief stage progression
- CTA used
- Calendar hooks already woven in (to avoid duplication)
- Approval status (if known)

**From YouTube Scripts:**
- Which LinkedIn post days they mirror (if applicable)
- Topics covered
- Any supplemental angles or platform-specific frames used

**From Blog / Articles:**
- Topics covered and which belief stages they map to
- Any SEO keywords or search-intent angles in use
- Whether they reference or extend LinkedIn or YouTube content

**From Theme Selection:**
- Primary theme and supporting themes selected for the month
- Quarterly campaign angle
- Belief stage focus

**From Authority Blueprint:**
- Annual campaign direction
- Quarterly campaign angle (for current quarter)
- Primary belief stage for current quarter

---

### STEP 4 — Check for Cross-Platform Conflicts or Gaps

Once context is extracted, assess:

1. **Topic overlap** — Is the requested content covering a topic already addressed on another platform this month? If so, flag it. The new content should extend or deepen that topic, not repeat it.

2. **Belief stage alignment** — What stage is the existing content working at? The new content should operate at the same stage or take the next logical step.

3. **CTA consistency** — Is there a CTA already established for this month? The new content should use the same CTA unless there is a deliberate reason to introduce a new one.

4. **Hook / celebration reuse** — Have specific daily celebrations or weekly events already been assigned to other pieces this month? Flag any overlap so the content writer can use a different hook or reference the same event from a different angle.

5. **Campaign gaps** — What content types are missing for this month? If LinkedIn exists but YouTube doesn't, flag the gap. Don't wait to be asked.

---

### STEP 5 — Output the Sync Context Block

```
SYNC CONTEXT BLOCK
==================
Client: [Client Slug]
Target Month(s): [Month(s)]
Requested Content Type: [Type]
Check Run: [Date]

EXISTING CONTENT FOUND:
  ✓ Marketing Calendar: [filename or NONE]
  ✓ LinkedIn Pack: [filename or NONE]
  ✓ YouTube Scripts: [filename or NONE]
  ✓ Blog / Articles: [filename or NONE]
  ✓ Theme Selection: [filename or NONE]
  ✓ Authority Blueprint: [filename or NONE]

CAMPAIGN CONTEXT (extracted from existing files):
  Annual Direction: [from Authority Blueprint or NONE]
  Quarterly Angle: [from most recent theme/calendar doc or NONE]
  Primary Monthly Theme: [value or NONE]
  Supporting Themes: [list or NONE]
  Belief Stage Focus: [current month's stage(s) or NONE]
  Active CTA: [the CTA in use this month or NONE]

EXISTING CONTENT SUMMARY:
  LinkedIn: [brief summary of arc/topics/stages covered — or NONE]
  YouTube: [brief summary — or NONE]
  Blog: [brief summary — or NONE]
  Calendar: [key hooks/celebrations already selected — or NONE]

CROSS-PLATFORM FLAGS:
  Topic Overlap: [list any overlapping topics or NONE]
  Hook Reuse Risk: [celebrations already used — new content should vary or reframe]
  CTA Conflict: [flag if requested content uses a different CTA — or NONE]
  Campaign Gaps: [content types not yet produced for this month]

SYNC DIRECTIVE FOR CONTENT WRITER:
  [2–4 sentences: What the new content must do to integrate with the existing campaign.
   What stage to operate at. What angle to take. What to avoid.
   If no existing content found: "No existing content for [Month]. Proceed with inputs from
   Authority Engine and client-context.yaml. Establish the campaign foundation."]

SYNC STATUS: [CLEAR TO PROCEED | REVIEW REQUIRED]
```

---

## SYNC DIRECTIVE RULES

The Sync Directive is the most important output of this skill. Write it in plain language that a content writer can act on immediately.

**If existing LinkedIn content is found and YouTube is being requested:**
The YouTube scripts must mirror the LinkedIn arc — same topics, same stages, same CTA. The Sync Directive should confirm this and flag any LinkedIn posts that already have corresponding YouTube scripts so Milo Vance starts from the right day.

**If existing YouTube and LinkedIn exist and Blog is being requested:**
Blog articles should extend the belief arc — going deeper than a LinkedIn post or YouTube script can, adding supporting evidence, SEO substance, and long-form proof. The Sync Directive should identify which belief stages need blog reinforcement.

**If a marketing calendar exists:**
All content must use the weekly events and daily celebrations selected in the calendar. The content writer does not select new hooks independently. The calendar is the source of truth.

**If no content exists for the target month:**
The Sync Directive states this clearly and directs the content writer to establish the campaign foundation using the Authority Blueprint and client-context.yaml.

---

## ERROR HANDLING

- If the client outputs folder does not exist: "No output folder found at `client-onboarding/clients/[client-slug]/outputs/`. Confirm client slug or run onboarding first."
- If a file is found but cannot be read: Flag it. Do not silently skip.
- If front matter dates are ambiguous: Check the filename date AND the document body for month references.
- If multiple LinkedIn packs exist for the same month: Flag both. Ask Roger which is the active version before proceeding.

---

## OUTPUT FORMAT

Output the Sync Context Block only. No prose around it. Pass directly to the requested content skill as a required input addendum.

The requesting skill (Cleo, Milo, Naomi, etc.) receives:
1. Their standard required inputs
2. The Sync Context Block appended

If SYNC STATUS is `REVIEW REQUIRED`, pause and present the flags to Roger before invoking the content skill. Do not proceed through a conflict silently.

---

## NOTES

- This skill is part of the ASG Calendar & Marketing Team
- Managed by: Sloane Mercer, Calendar Team Director
- Runs: Before every content production request (unless explicitly waived by Roger)
- Feeds into: All content skills
- Purpose: Campaign coherence, not just content production
