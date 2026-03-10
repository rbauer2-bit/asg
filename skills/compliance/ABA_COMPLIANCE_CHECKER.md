# ABA_COMPLIANCE_CHECKER.md
## Skill: Attorney Advertising Compliance Review
### Specialist: Diana Voss, Legal Compliance Analyst (reports to Preston Adler, COO)

---

## PURPOSE

This skill runs an ABA advertising compliance audit on any attorney-facing copy before it is delivered or published. It applies to website service pages, about pages, landing pages, email sequences, social media content, direct mail, and any other marketing material produced for attorney clients.

**This check is mandatory for all attorney client deliverables.** It runs AFTER content is written and BEFORE the DOCX is built. No attorney client deliverable ships without this gate.

Governing rules: ABA Model Rules of Professional Conduct 7.1 and 7.2 (post-2018 amendments). Supplemented by state-specific rules where client jurisdiction is known.

---

## WHEN TO RUN

- After any content specialist (Vivienne Carr, Clara Ashworth, Audrey Voss, Rhett Callahan, Sienna Okafor, Solomon Grey, Ingrid Holt, Tomás Rivera, or any other content team member) produces a deliverable for an attorney client
- Before the DOCX builder is invoked
- Before any content is marked COMPLETE in the deliverable log
- Whenever Roger flags a review request explicitly

---

## INPUT REQUIRED

1. The markdown content to be reviewed (full text)
2. Client's primary practice state(s) — pulls from `client-context.yaml`
3. Content type (service page, email, social post, direct mail, landing page, etc.)

---

## THE AUDIT — 8 CHECKS

Run each check sequentially. Flag every violation. Do not skip any check because the content "looks clean."

---

### CHECK 1 — FORBIDDEN LANGUAGE (ABA Rule 7.1)

Scan for any of the following. Flag every instance found.

**Prohibited superlatives and self-praise (unverifiable):**
- "best," "top," "leading," "premier," "finest," "most successful," "greatest," "number one," "#1"
- "cheapest," "lowest fees," "most affordable"
- Any comparative language without verifiable data ("better than other attorneys," "more experience than")

**Prohibited specialization claims (ABA Rule 7.2(c)):**
- "specialist," "specializes in," "specialized practice," "specialized knowledge"
- "expert," "expertise in" (when used as a credential claim rather than a description of depth)
- "board certified" or "certified specialist" — unless the client is certified by a state bar program or ABA-accredited organization; if used, the certifying body MUST be named

**Prohibited outcome guarantees:**
- "guarantee," "guaranteed result," "guaranteed outcome," "you will win," "we will win"
- "promise," "assured," "certain to"
- Any language that implies a specific result is likely or expected for the reader

**Note — Credential citations are NOT the same as specialization claims.** Citing a fellowship, rating, recognition, or certification by name is factual. "He holds AAML Fellowship" is compliant. "He is a specialist in family law by virtue of his AAML Fellowship" is not — AAML is not an ABA-accredited board certification.

---

### CHECK 2 — CREDENTIAL ACCURACY (ABA Rule 7.1)

For each credential cited:

1. Confirm the credential is accurately described (not overstated)
2. Confirm the credential name is correct
3. Flag any derived statistics not published by the credentialing body itself (e.g., "top X%" calculations based on total attorney population estimates)
4. Confirm "Board Certified" language is only used if the client is certified by a state bar board certification program or ABA-accredited organization

**Safe framing for non-board-certification credentials:**
- AAML Fellowship → "Fellow of the American Academy of Matrimonial Lawyers"
- Super Lawyers → "Named to Super Lawyers [Year/Years]"
- AV Preeminent → "Martindale-Hubbell AV Preeminent Rated"
- Do NOT describe these as "certifications" or "board certifications"

---

### CHECK 3 — RESULTS AND OUTCOMES LANGUAGE (ABA Rule 7.1, 7.2(d))

Flag any of the following:
- Description of past case results without a "results may vary" qualifier
- Language implying that what happened for a prior client will happen for the reader
- Testimonials (if present) that do not include a disclaimer
- Statements like "clients regularly achieve X" or "most of our clients get Y" without disclaimer

**Required disclaimer when any results, outcomes, or case descriptions appear:**
> Past results do not guarantee or predict a similar outcome in future cases. Results depend on the specific facts and legal circumstances of each matter.

This disclaimer does not need to appear in every paragraph — it must appear on the page or in the document. For website pages, it belongs in the sitewide footer. For standalone documents (lead magnets, email sequences), it belongs at the end of the document.

---

### CHECK 4 — ATTORNEY-CLIENT RELATIONSHIP CLARITY (ABA Rule 7.1, 7.2(e))

**For website pages and contact-facing content:**
Flag if the document does not include or specify:
- "No attorney-client relationship" disclaimer on or near contact forms
- Disclaimer that submitting a form / sending an email does not create representation

**For email sequences:**
Flag if initial outreach emails imply a relationship before one is formed.

**For general content (blog, social, video scripts):**
Flag if the content presents legal information in a way that could be mistaken for legal advice to the reader.

**Required language (contact forms):**
> Submitting this form does not create an attorney-client relationship. No attorney-client relationship is formed until a written engagement agreement has been executed by both parties.

---

### CHECK 5 — STATE-SPECIFIC RULES

Apply the relevant state rules based on `client-context.yaml → primary_state` and `secondary_state`.

#### KENTUCKY (SCR 3.130)
- [ ] All advertisements must include at least one attorney's name and Kentucky office address
- [ ] All claims must be substantiated — vague or unverifiable statements are prohibited
- [ ] Kentucky Attorneys' Advertising Commission (AAC) pre-approval is optional but creates a safe harbor; flag for Roger's consideration on any significant campaign launch
- [ ] No false, deceptive, or misleading statements (same as ABA 7.1, actively enforced by AAC)

#### INDIANA (Rules of Professional Conduct Rules 7.1–7.3)
- [ ] All advertising must include the name and office address of at least one responsible lawyer or the firm
- [ ] All advertising records must be retained for **6 years** after dissemination — flag this requirement in the deliverable notes so the client knows to archive
- [ ] For direct solicitation materials (direct mail, email outreach to specific prospects): "ADVERTISING MATERIAL" must appear conspicuously at the beginning and end
- [ ] For personal injury or wrongful death matters: **30-day waiting period** before direct solicitation of a prospective client (this is practice-area specific — flag if applicable)

#### ALL OTHER STATES
If the client practices in a state other than KY or IN, flag: "State-specific rules for [STATE] have not been audited. Recommend client verify compliance with [STATE] bar advertising rules before publication."

---

### CHECK 6 — THIRD-PARTY RATING ATTRIBUTION

Flag any reference to the following rating services and confirm the required attribution language is present (either on the page, in a footer, or specified in implementation notes):

**Super Lawyers:**
> Super Lawyers is a rating service of outstanding lawyers from more than 70 practice areas who have attained a high degree of peer recognition and professional achievement. The selection process includes independent research, peer nominations, and peer evaluations.

**Martindale-Hubbell AV Preeminent:**
> AV Preeminent is a trademark of Internet Brands, Inc. The AV Preeminent rating reflects a combination of achieving a Very High General Ethical Standards rating and a Legal Ability score of 4.5–5.0, as assessed by peers in the legal community.

**Best Lawyers / Best Law Firms:**
> Best Lawyers is a trademark of Woodward/White, Inc. Recognition by Best Lawyers is based on peer nominations and evaluations and does not constitute a guarantee of legal ability.

**Avvo:**
> Avvo ratings are calculated using a mathematical model and are intended as a starting point for selecting an attorney. They do not constitute a guarantee of legal ability.

For any other third-party rating or recognition cited: Flag for verification of the rating service's own usage guidelines and required attribution language.

---

### CHECK 7 — FIRM STRUCTURE ACCURACY (ABA Rule 7.1 — post-consolidation of old Rule 7.5)

- [ ] Firm name in content matches the actual registered legal entity name
- [ ] No implication of partnerships, associates, or organizational size that does not exist
- [ ] If "Law Offices of [Name]" or "[Name] & Associates" is used, confirm the structure is accurate
- [ ] No implication that the firm has offices in locations where it does not practice

---

### CHECK 8 — CONTENT TYPE SPECIFIC FLAGS

**Website service pages:**
- [ ] "Attorney Advertising" notation required in footer for Indiana sites
- [ ] "Past results" disclaimer required in footer
- [ ] "No attorney-client relationship" disclaimer required on contact page / form
- [ ] Attorney name and office address visible on site

**Email sequences (outreach / nurture):**
- [ ] If direct solicitation to a specific person who may need specific services → check Rule 7.3; verify contact was not "opt-out" prior to contact
- [ ] Indiana: "ADVERTISING MATERIAL" at beginning and end if solicitation
- [ ] No guaranteed outcome language in subject lines or body

**Direct mail:**
- [ ] Indiana: "ADVERTISING MATERIAL" on outer envelope
- [ ] KY/IN: Attorney name and address required
- [ ] "Past results" disclaimer required if results referenced
- [ ] No solicitation of personal injury / wrongful death prospects in Indiana within 30 days of incident

**Social media posts (LinkedIn, Facebook, etc.):**
- [ ] No guaranteed results
- [ ] No "specialist" or "expert" claims without certification
- [ ] Factual credential references are fine
- [ ] If post includes a direct CTA to contact about a specific legal matter → may trigger Rule 7.3 direct solicitation rules in some states; use general CTAs ("schedule a consultation") rather than matter-specific ones

**Video scripts:**
- [ ] All checks above apply to spoken content
- [ ] Disclaimers must appear on-screen long enough to be read (minimum 3 seconds for short disclaimers)
- [ ] Super Lawyers / AV Preeminent attribution required in video description or on-screen if cited

---

## OUTPUT FORMAT

Produce a structured Compliance Report:

```
ABA COMPLIANCE REVIEW
=====================
Client: [client-name]
Content: [deliverable name]
Reviewed: [date]
State(s): [KY / IN / other]
Reviewer: Diana Voss, Legal Compliance Analyst | Authority Systems Group™

VIOLATIONS FOUND: [N]
WARNINGS: [N]
STATUS: [PASS / PASS WITH NOTES / REQUIRES REVISION]

──────────────────────────────────────────────────────────────
VIOLATIONS (must fix before delivery)
──────────────────────────────────────────────────────────────
[List each violation with: Check # | Location in document | Issue | Required fix]

──────────────────────────────────────────────────────────────
WARNINGS (flag to Roger; client action may be required)
──────────────────────────────────────────────────────────────
[List each warning with: Check # | Location | Issue | Recommended action]

──────────────────────────────────────────────────────────────
REQUIRED IMPLEMENTATION ITEMS (client must add before publishing)
──────────────────────────────────────────────────────────────
[List each required site-level or document-level addition not in the body copy itself]

──────────────────────────────────────────────────────────────
SIGN-OFF
──────────────────────────────────────────────────────────────
[ ] All violations resolved
[ ] All warnings reviewed by Roger
[ ] Implementation items documented in deliverable notes
[ ] Preston Adler notified for QC gate sign-off

Diana Voss
Legal Compliance Analyst
Authority Systems Group™
```

---

## STATUS DEFINITIONS

**PASS** — No violations found. Warnings documented. Ready for DOCX build and delivery.

**PASS WITH NOTES** — No violations in the copy itself. Required implementation items exist (disclaimers, attribution, footer language) that the client must add at the website/publication level. Document these clearly. Ready for delivery.

**REQUIRES REVISION** — One or more violations found in the copy. Do not build DOCX or deliver until violations are resolved. Return to content specialist with specific corrections.

---

## ESCALATION

If Diana Voss identifies a violation that is ambiguous — where the rule could reasonably be interpreted either way — escalate to Preston Adler (COO) before making a judgment call. Preston reviews with Daniel Frost (CSO) if the issue affects strategic positioning. Roger has final authority on any borderline call.

---

## STATE EXPANSION NOTE

This skill currently covers ABA Model Rules (all states), Kentucky (SCR 3.130), and Indiana (Rules of Professional Conduct Rules 7.1–7.3) in full detail. For clients in other states, Check 5 flags the gap. To expand full coverage to a new state, add the state's specific provisions to Check 5 and document any deviations from ABA Model Rules in a `state-addendum/[STATE].md` file in this directory.

---

*Authority Systems Group™ — Internal Skill File*
*Compliance Division | Diana Voss, Legal Compliance Analyst*
*Created: 2026-03-08 | Version 1.0*
