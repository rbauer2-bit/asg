# DOCX_BUILDER.md
# Authority Systems Group™ — Skill: Word Document Generation
# Technical instructions for producing the final .docx file
# Owner: Preston Adler, COO / Iris Nolan, CTO (technical execution)
# Visual Brand Standard: /brand-standards/ASG_BRAND_DOCX.md — authoritative source for all colors, fonts, page setup, header/footer, cover page, and table patterns

---

## PURPOSE

Convert the assembled Authority Blueprint™ content into a properly formatted, brand-compliant Word document ready for print production or digital delivery.

This skill is purely technical — it does not make content decisions. All content and formatting specifications are defined in `REPORT_FORMATTER.md`. This skill executes those specifications in the document file.

---

## MANDATORY: MARKDOWN SYNTAX STRIPPING

**Every markdown formatting character must be stripped from rendered text after the corresponding formatting is applied.** Leaving syntax characters in the output creates a manual cleanup burden on every document. This is non-negotiable.

Rules by element type:

```
Headings (# / ## / ### / ####):
  Strip the # characters and leading space.
  The text itself should contain no # characters.

Bold (**text**):
  Strip both ** markers. Render the text as bold in the Word run.
  Output: "This Is Bold" (not "**This Is Bold**")

Italic (*text*):
  Strip both * markers. Render the text as italic in the Word run.
  Output: "This Is Italic" (not "*This Is Italic*")

Bullet markers (- / *):
  Strip the leading - or * and the following space using a regex prefix strip,
  NOT a character-level lstrip() (which corrupts **bold** bullets by eating
  the leading ** characters).
  Correct: re.sub(r"^[-*]\s+", "", text.strip())
  Wrong:   text.lstrip("- *").strip()

Checkboxes (- [ ] / - [x]):
  Strip the checkbox marker after stripping the bullet prefix.
  re.sub(r"^\[[ xX✓]\]\s*", "", clean)
  Render as a standard bullet. Do not use Word's checkbox style.

Blockquote (> text):
  Strip the > character and leading space.
  Apply the ASG_Callout style to the resulting paragraph.

Horizontal rule (---):
  Render as a paragraph with a blue bottom border. Do not output the dashes.

Inline code (`text`):
  Strip backtick markers. Render in Calibri (monospaced fallback).
```

When rendering programmatically, test each element type in isolation before assembling the full document. A spot-check on the QC section (which contains checkboxes) and any section with bold/italic labels will catch most stripping failures.

---

## DOCUMENT FRAMING STANDARD — COLD OUTREACH

**The Authority Blueprint™ is a cold outreach instrument until the client signs.**

This document is the first substantive contact Melissa (or any prospect) has with Authority Systems Group™. She does not know Roger Bauer. She has not signed anything. She has likely received "strategic proposals" before that were generic and forgettable.

The framing must reflect this reality:

**Prohibited language (assumes a relationship that does not yet exist):**
- "this engagement" → use "this analysis" or "this work" or nothing
- "as we discussed" / "when we spoke" → remove or replace with research framing
- "your delivery timeline" / "what we'll be sending you" → conditional: "what the first 60 days looks like if you move forward"
- Any language implying she has agreed, signed, or scheduled anything

**Required framing:**
- Roger Bauer's voice reads as: "I researched your market and built this specifically for you. I believe there's a significant opportunity here."
- The document demonstrates capability — it shows the depth of thinking ASG brings before a single dollar is exchanged.
- "What Happens Next" sections must read as: "Here is exactly what working with us looks like" — not as a confirmed delivery schedule.
- The goal is to generate one response: "I need to speak with Roger."

**Tone reference:** Think of a highly skilled consultant who has done the homework, believes in the opportunity, and is presenting findings to a busy executive who will dismiss generic pitches instantly. Direct. Evidence-based. No hedging. Confident without being presumptuous about the outcome.

---

## DOCUMENT SETUP

### Page Settings
```
Page size: Letter (8.5" × 11")
Margins:
  Top: 1.0"
  Bottom: 1.0"
  Left: 1.25"
  Right: 1.0"
  Header distance from edge: 0.5"
  Footer distance from edge: 0.5"
Gutter: 0" (single-sided printing)
```

### Style Definitions

Define these styles in the document's style library before adding content:

```
ASG_H1:
  Font: Calibri Bold (or Montserrat Bold if available)
  Size: 24pt
  Color: #25aae1
  Space before: 24pt
  Space after: 12pt
  Keep with next: Yes

ASG_H2:
  Font: Calibri Bold
  Size: 18pt
  Color: #58585a
  Space before: 18pt
  Space after: 8pt
  Keep with next: Yes

ASG_H3:
  Font: Calibri Bold
  Size: 14pt
  Color: #58585a
  Space before: 12pt
  Space after: 6pt

ASG_Body:
  Font: Georgia (or Cambria)
  Size: 11pt
  Color: #333333
  Line spacing: Multiple, 1.4
  Space after: 6pt

ASG_Callout:
  Font: Calibri Italic
  Size: 11pt
  Color: #58585a
  Left indent: 0.25"
  Left border: 4pt, #25aae1
  Background: #F5F5F5
  Space before: 12pt
  Space after: 12pt

ASG_SignOff:
  Font: Calibri Italic
  Size: 11pt
  Color: #58585a
  Space before: 18pt
  Left indent: 0.5"

ASG_TableHeader:
  Font: Calibri Bold
  Size: 11pt
  Color: #FFFFFF
  Background: #25aae1
  Alignment: Center

ASG_Footer:
  Font: Calibri
  Size: 9pt
  Color: #888888
```

---

## HEADER AND FOOTER SETUP

### Header (all interior pages except cover)
```
Left element: ASG logo inline image (approx 1.5" wide, 0.4" tall)
Right element: "Authority Blueprint™ — [Client Display Name]"
  Style: ASG_Footer
  Alignment: Right
Bottom border: 0.5pt line, #CCCCCC
```

### Footer (all interior pages except cover)
```
Left element: None
Center element: "Authority Systems Group™ — Confidential. Prepared exclusively for [Client Display Name]."
  Style: ASG_Footer
  Alignment: Center
Right element: Page number
  Style: ASG_Footer
  Format: Arabic numerals, starting at 1
  (Cover page excluded from count — start numbering at Table of Contents = page 1)
Top border: 0.5pt line, #CCCCCC
```

---

## SECTION DIVIDER FORMATTING

Between each major section:
```
Page break before new section
Full-width horizontal line: #25aae1, 2pt weight
  (Implemented as: bottom border on an empty paragraph using ASG_H1 style)
```

---

## COVER PAGE CONSTRUCTION

The cover page requires special handling — it uses a dark background that Word handles through a section break with different page color settings.

```
Insert section break (next page) after cover page
Cover page section settings:
  Page color: #1a1a1a
  No header/footer on cover page

Cover page elements (implemented as text boxes or positioned elements):
  1. Vertical accent stripe: Left margin, full height, 8pt wide, #25aae1
     → Implement as: thin colored table column or left border on page
  2. ASG Logo: Center positioned, approx 3" wide, white version
     → Insert as inline image, centered
  3. Title text: "YOUR AUTHORITY BLUEPRINT™"
     → Font: Calibri Bold, 34pt, White (#FFFFFF), centered
  4. Subtitle: "A Strategic Growth System Built Exclusively for:"
     → Font: Calibri, 14pt, #25aae1, centered
  5. Client name: "[Client Business Name]"
     → Font: Calibri Bold, 24pt, White, centered
  6. Attribution: "Directed by Roger | Authority Systems Group™"
     → Font: Calibri Italic, 12pt, #aaaaaa, centered
  7. Date: "[Month Year]"
     → Font: Calibri, 11pt, #888888, centered
  8. Confidential notice: "CONFIDENTIAL — Prepared Exclusively for [Client Name]"
     → Font: Calibri, 9pt, #666666, letter-spacing: expanded, centered, near bottom
  9. Bottom accent line: Full-width, #25aae1, 1pt
     → Positioned approximately 15% from bottom

Spacing between elements:
  Logo to title: 0.75"
  Title to subtitle: 0.25"
  Subtitle to client name: 0.15"
  Client name to attribution: 0.5"
  Attribution to date: 0.25"
```

---

## TABLE FORMATTING

For all data tables in the document:

```
Border: All cells, 0.5pt, #CCCCCC
Header row:
  Background: #25aae1
  Font: Calibri Bold, 11pt, White
  Alignment: Center
  Height: 0.35"
Odd data rows:
  Background: White (#FFFFFF)
Even data rows:
  Background: #F5F5F5
Data cell font: Calibri, 11pt, #333333
Cell padding: 0.08" all sides
Repeat header row: Yes (for tables spanning multiple pages)
```

---

## CALLOUT BOX IMPLEMENTATION

Callout boxes in Word:
```
Method: Paragraph with custom border styling
Left border: 4pt, #25aae1
Background fill: #F5F5F5
Left indent: 0.25" (both indent and hanging)
Space before: 12pt
Space after: 12pt
Apply style: ASG_Callout
```

---

## IMAGE AND PLACEHOLDER HANDLING

For persona headshots (current version uses placeholders):
```
Placeholder: Circle shape, 1" diameter
Fill: #E0E0E0 (light gray)
Border: 1pt, #25aae1
Center label: Person's initials, Calibri Bold, 14pt, #58585a
Caption below: [Name], [Title]
  Font: Calibri, 9pt, #666666
```

---

## DOCUMENT PROPERTIES

Set before finalizing:
```
Title: "Authority Blueprint™ — [Client Business Name]"
Subject: "Strategic Growth System"
Author: "Authority Systems Group™"
Company: "Authority Systems Group™"
Keywords: "authority blueprint, strategic plan, [client slug]"
Comments: "Prepared under the direction of Roger, Director — Authority Systems Group™"
```

---

## EXPORT SEQUENCE

```
Step 1: Save as .docx to /client-onboarding/clients/[slug]/outputs/
  Filename: [slug]_authority-blueprint_[YYYYMMDD].docx

Step 2: Export as PDF (File → Export → Create PDF/XPS)
  PDF settings:
    Quality: Standard (publishing online and printing)
    Include all document properties: Yes
    Optimize for: Print
  Filename: [slug]_authority-blueprint_[YYYYMMDD].pdf

Step 3: Verify PDF
  Open the PDF and confirm:
  — Cover page colors render correctly
  — All fonts embedded
  — Page numbers correct
  — No missing images or broken references

Step 4: Update deliverable log
```

---

## PYTHON/DOCX GENERATION (if building programmatically via Claude Code)

If using python-docx to generate the document:

```python
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Brand colors
ASG_BLUE = RGBColor(0x25, 0xAA, 0xE1)
ASG_CHARCOAL = RGBColor(0x58, 0x58, 0x5A)
ASG_DARK_BG = RGBColor(0x1A, 0x1A, 0x1A)
ASG_BODY_TEXT = RGBColor(0x33, 0x33, 0x33)
ASG_LIGHT_GRAY = RGBColor(0xF5, 0xF5, 0xF5)

# Document setup
doc = Document()
section = doc.sections[0]
section.page_width = Inches(8.5)
section.page_height = Inches(11)
section.left_margin = Inches(1.25)
section.right_margin = Inches(1.0)
section.top_margin = Inches(1.0)
section.bottom_margin = Inches(1.0)

# Apply heading style
def add_h1(doc, text):
    heading = doc.add_heading(text, level=1)
    heading.runs[0].font.color.rgb = ASG_BLUE
    heading.runs[0].font.size = Pt(24)
    heading.runs[0].font.bold = True
    return heading

# Apply body style
def add_body(doc, text):
    para = doc.add_paragraph(text)
    para.runs[0].font.size = Pt(11)
    para.runs[0].font.color.rgb = ASG_BODY_TEXT
    return para

# Save document
doc.save(f'/client-onboarding/clients/{client_slug}/outputs/{client_slug}_authority-blueprint_{date}.docx')
```

Full implementation should reference the python-docx documentation and the brand standards in `LGD_BRAND.md`.

---

*Authority Systems Group™ — Output Skills Library*
*Owner: Preston Adler, COO | Technical spec: Iris Nolan, CTO*
