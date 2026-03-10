# SKILL: ASG Brand Standard — Client-Facing Documents
**Authority Systems Group**
Version 1.0

---

## PURPOSE

This skill defines the visual and structural brand standard for all client-facing documents produced by Authority Systems Group. It is a reference skill — not executed independently. Any skill that produces a client-facing document must import and apply these standards.

**Documents governed by this skill:**
- Authority Blueprint™
- Authority Intelligence Brief™
- Proposal / Engagement Letter
- Campaign Report / Results Summary
- Email Sequence Deliverable
- Content Calendar Deliverable

---

## BRAND CONSTANTS

```
PRIMARY BLUE:     #25aae1   (hex) | RGB: 37, 170, 225
CHARCOAL GRAY:    #58585a   (hex) | RGB: 88, 88, 90
WHITE:            #FFFFFF
LIGHT BLUE TINT:  #EAF6FC   (used for table header fills, callout boxes)
LIGHT GRAY TINT:  #F5F5F5   (used for alternating table rows, sidebars)

PRIMARY FONT:     Arial
HEADING SIZES:    H1: 28pt | H2: 22pt | H3: 16pt | H4: 13pt
BODY SIZE:        11pt
SMALL/CAPTION:    9pt

LOGO:             brand-standards/assets/asgFull.png
                  Transparent background PNG | Original: 2167×1042 px | Aspect ratio: 2.08:1
                  Header use: width=160px (docx-js) / Inches(1.5) (python-docx) — height auto-scales
                  Cover page use: width=220px (docx-js) / Inches(2.0) (python-docx) — height auto-scales
TAGLINE:          "Positioning You As The Authority"
WEBSITE:          AuthoritySystemsGroup.com
```

---

## DOCX COLOR REFERENCE (docx-js format)

```javascript
// Always strip # from hex values for docx-js
const ASG_COLORS = {
  primaryBlue:    "25aae1",
  charcoalGray:   "58585a",
  white:          "FFFFFF",
  lightBlueTint:  "EAF6FC",
  lightGrayTint:  "F5F5F5",
  black:          "000000",
  borderGray:     "CCCCCC"
};
```

---

## PAGE SETUP (ALL DOCUMENTS)

```javascript
properties: {
  page: {
    size: {
      width: 12240,   // 8.5 inches — US Letter
      height: 15840   // 11 inches
    },
    margin: {
      top: 1440,      // 1 inch
      right: 1260,    // 0.875 inch
      bottom: 1440,   // 1 inch
      left: 1260      // 0.875 inch
    }
  }
}
// Content width = 12240 - 1260 - 1260 = 9720 DXA
```

---

## STYLE DEFINITIONS (APPLY TO ALL DOCUMENTS)

```javascript
styles: {
  default: {
    document: {
      run: { font: "Arial", size: 22, color: "58585a" } // 11pt default, charcoal body text
    }
  },
  paragraphStyles: [
    {
      id: "Heading1", name: "Heading 1",
      basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 56, bold: true, font: "Arial", color: "25aae1" }, // 28pt, primary blue
      paragraph: {
        spacing: { before: 360, after: 120 },
        outlineLevel: 0,
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "25aae1", space: 1 } }
      }
    },
    {
      id: "Heading2", name: "Heading 2",
      basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 44, bold: true, font: "Arial", color: "58585a" }, // 22pt, charcoal
      paragraph: { spacing: { before: 300, after: 100 }, outlineLevel: 1 }
    },
    {
      id: "Heading3", name: "Heading 3",
      basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 32, bold: true, font: "Arial", color: "25aae1" }, // 16pt, primary blue
      paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 2 }
    },
    {
      id: "Heading4", name: "Heading 4",
      basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 26, bold: true, font: "Arial", color: "58585a" }, // 13pt, charcoal
      paragraph: { spacing: { before: 180, after: 60 }, outlineLevel: 3 }
    },
    {
      id: "ASGCallout", name: "ASG Callout",
      basedOn: "Normal", next: "Normal",
      run: { size: 22, font: "Arial", color: "25aae1", bold: true },
      paragraph: {
        spacing: { before: 120, after: 120 },
        indent: { left: 720 },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: "25aae1", space: 6 } }
      }
    }
  ]
}
```

---

## HEADER (ALL DOCUMENTS)

```javascript
// docx-js implementation — logo is confirmed available at brand-standards/assets/asgFull.png
headers: {
  default: new Header({
    children: [
      new Paragraph({
        children: [
          new ImageRun({
            data: fs.readFileSync("brand-standards/assets/asgFull.png"),
            transformation: { width: 160, height: 77 }, // 2.08:1 ratio at 160px wide
            type: "png"
          }),
          new TextRun({
            text: "\t" + documentTitle, // right-aligned via tab stop
            font: "Arial", size: 18, color: "58585a"
          })
        ],
        tabStops: [{ type: TabStopType.RIGHT, position: 9720 }],
        border: {
          bottom: { style: BorderStyle.SINGLE, size: 6, color: "25aae1", space: 1 }
        }
      })
    ]
  })
}
```

### Python-docx header implementation (for .py build scripts)

```python
import os
from docx.shared import Inches

LOGO_PATH = os.path.join(os.path.dirname(__file__), '../../../../brand-standards/assets/asgFull.png')
# From client outputs/ folder: adjust relative path as needed
# Absolute path: /Users/Roger/Dropbox/code/authority-systems-group/brand-standards/assets/asgFull.png

def add_header(doc, document_title):
    section = doc.sections[0]
    header = section.header
    header.is_linked_to_previous = False
    para = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
    para.clear()
    # Logo left — add_picture auto-calculates height from width preserving 2.08:1 ratio
    run = para.add_run()
    run.add_picture(LOGO_PATH, width=Inches(1.5))
    # Document title right (tab stop)
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    pPr = para._p.get_or_add_pPr()
    tabs = OxmlElement('w:tabs')
    tab = OxmlElement('w:tab')
    tab.set(qn('w:val'), 'right')
    tab.set(qn('w:pos'), '9360')  # ~6.5" from left
    tabs.append(tab)
    pPr.append(tabs)
    title_run = para.add_run('\t' + document_title)
    title_run.font.name = 'Calibri'
    title_run.font.size = Pt(9)
    title_run.font.color.rgb = ASG_CHARCOAL
    add_bottom_border(para, color='25aae1', sz='6')
```

---

## FOOTER (ALL DOCUMENTS)

```javascript
footers: {
  default: new Footer({
    children: [
      new Paragraph({
        children: [
          new TextRun({
            text: "Authority Systems Group  |  AuthoritySystemsGroup.com  |  Confidential",
            font: "Arial", size: 16, color: "58585a"
          }),
          new TextRun({
            text: "\tPage ",
            font: "Arial", size: 16, color: "58585a"
          }),
          new SimpleField("PAGE")  // NOTE: PageNumber is an enum, not a constructor — use SimpleField("PAGE")
        ],
        tabStops: [{ type: TabStopType.RIGHT, position: 9720 }],
        border: {
          top: { style: BorderStyle.SINGLE, size: 4, color: "25aae1", space: 1 }
        }
      })
    ]
  })
}
```

---

## COVER PAGE PATTERN

Use for: Authority Blueprint™, Authority Intelligence Brief™, Proposal/Engagement Letter

```javascript
// Full-width dark header block with centered logo
new Table({
  width: { size: 9720, type: WidthType.DXA },
  columnWidths: [9720],
  rows: [
    new TableRow({
      children: [
        new TableCell({
          shading: { fill: "1a1a1a", type: ShadingType.CLEAR },
          margins: { top: 800, bottom: 800, left: 720, right: 720 },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
                     left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new ImageRun({
                  data: fs.readFileSync("brand-standards/assets/asgFull.png"),
                  transformation: { width: 220, height: 106 }, // 2.08:1 ratio at 220px wide
                  type: "png"
                })
              ]
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [new TextRun({
                text: "Positioning You As The Authority",
                font: "Arial", size: 18, color: "25aae1", italics: true
              })]
            })
          ]
        })
      ]
    })
  ]
}),

// Document title block
new Paragraph({ text: "", spacing: { before: 480 } }),
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({
    text: documentTitle,  // e.g. "Authority Blueprint™"
    font: "Arial", size: 56, bold: true, color: "25aae1"
  })]
}),
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({
    text: clientName + "  |  " + preparedDate,
    font: "Arial", size: 24, color: "58585a"
  })]
}),

// Charcoal divider line
new Paragraph({
  spacing: { before: 360 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "58585a", space: 1 } },
  children: [new TextRun({ text: "" })]
}),

// Prepared by block
new Paragraph({ spacing: { before: 360 } }),
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({
    text: "Prepared by Authority Systems Group",
    font: "Arial", size: 20, color: "58585a", italics: true
  })]
}),
new PageBreak()  // always wrap in a Paragraph
```

---

## TABLE STANDARD

```javascript
// Header row: PRIMARY BLUE fill, white text
// Body rows: alternate WHITE and LIGHT GRAY TINT
// All borders: borderGray (#CCCCCC), SINGLE, size 1

const tableHeaderCell = (text, width) => new TableCell({
  width: { size: width, type: WidthType.DXA },
  shading: { fill: "25aae1", type: ShadingType.CLEAR },
  margins: { top: 100, bottom: 100, left: 160, right: 160 },
  borders: { top: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
             bottom: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
             left: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
             right: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" } },
  children: [new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 20, bold: true, color: "FFFFFF" })]
  })]
});

const tableBodyCell = (text, width, isAltRow = false) => new TableCell({
  width: { size: width, type: WidthType.DXA },
  shading: { fill: isAltRow ? "F5F5F5" : "FFFFFF", type: ShadingType.CLEAR },
  margins: { top: 80, bottom: 80, left: 160, right: 160 },
  borders: { top: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
             bottom: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
             left: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
             right: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" } },
  children: [new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 20, color: "58585a" })]
  })]
});
```

---

## CALLOUT BOX (HIGHLIGHT / KEY INSIGHT)

```javascript
// Left blue border accent box — use for key takeaways, important notes, belief stage callouts
new Paragraph({
  style: "ASGCallout",
  children: [new TextRun({
    text: calloutText,
    font: "Arial", size: 22, color: "25aae1", bold: true
  })]
})
```

---

## SECTION DIVIDER

```javascript
// Blue rule between major sections — use sparingly
new Paragraph({
  spacing: { before: 240, after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "25aae1", space: 1 } },
  children: [new TextRun({ text: "" })]
})
```

---

## DOCUMENT-SPECIFIC COVER TITLES

```javascript
const ASG_DOCUMENT_TITLES = {
  authorityBlueprint:      "Authority Blueprint\u2122",
  authorityIntelligence:   "Authority Intelligence Brief\u2122",
  proposal:                "Proposal & Engagement Letter",
  campaignReport:          "Campaign Results Summary",
  emailSequence:           "Email Sequence Deliverable",
  contentCalendar:         "Content Calendar Deliverable"
};
```

---

## IMPLEMENTATION CHECKLIST

When producing any ASG client-facing document, verify:

- [ ] Page size set to US Letter (12240 x 15840 DXA)
- [ ] Margins set to 1" top/bottom, 0.875" left/right
- [ ] ASG_COLORS constants used throughout — no ad-hoc hex values
- [ ] Arial font applied to all text runs
- [ ] Logo loaded from `brand-standards/assets/asgFull.png` (transparent PNG, 2167×1042 native)
- [ ] Header includes ASG logo left + document title right-aligned
- [ ] Footer includes ASG attribution + page numbers + blue top border
- [ ] Cover page present (Blueprint, Intelligence Brief, Proposal)
- [ ] H1 headings in primary blue with bottom border
- [ ] H2 headings in charcoal gray
- [ ] H3 headings in primary blue
- [ ] Tables use blue header row + alternating gray body rows
- [ ] No unicode bullets — use LevelFormat.BULLET with numbering config
- [ ] ShadingType.CLEAR used (never SOLID)
- [ ] Document validated after generation: python scripts/office/validate.py output.docx

---

## NOTES

- Brand colors: #25aae1 (primary blue), #58585a (charcoal gray)
- This skill is referenced by all document-producing skills in the ASG system
- Referenced by: `DOCX_BUILDER.md`, `REPORT_FORMATTER.md`
- Built by Roger Bauer / Authority Systems Group
- AuthoritySystemsGroup.com
