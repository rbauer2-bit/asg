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

LOGO:             [LOGO_PLACEHOLDER] — replace with ImageRun once logo file is available
                  Placeholder: Text "AUTHORITY SYSTEMS GROUP" in PRIMARY BLUE, 14pt, bold
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
// Logo placeholder — replace TextRun with ImageRun once logo is available
headers: {
  default: new Header({
    children: [
      new Paragraph({
        children: [
          new TextRun({
            text: "AUTHORITY SYSTEMS GROUP",
            font: "Arial", size: 28, bold: true, color: "25aae1"
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

// When logo is available, replace the first TextRun with:
// new ImageRun({
//   data: fs.readFileSync("asg-logo.png"),
//   transformation: { width: 150, height: 40 }, // adjust to actual logo dimensions
//   type: "png"
// })
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
// Full-width blue header block (simulated with shaded table)
new Table({
  width: { size: 9720, type: WidthType.DXA },
  columnWidths: [9720],
  rows: [
    new TableRow({
      children: [
        new TableCell({
          shading: { fill: "25aae1", type: ShadingType.CLEAR },
          margins: { top: 720, bottom: 720, left: 720, right: 720 },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
                     left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [new TextRun({
                text: "AUTHORITY SYSTEMS GROUP",
                font: "Arial", size: 36, bold: true, color: "FFFFFF"
              })]
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [new TextRun({
                text: "Positioning You As The Authority",
                font: "Arial", size: 20, color: "EAF6FC", italics: true
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
- [ ] Header includes "AUTHORITY SYSTEMS GROUP" in primary blue + document title right-aligned
- [ ] Footer includes ASG attribution + page numbers + blue top border
- [ ] Cover page present (Blueprint, Intelligence Brief, Proposal)
- [ ] H1 headings in primary blue with bottom border
- [ ] H2 headings in charcoal gray
- [ ] H3 headings in primary blue
- [ ] Tables use blue header row + alternating gray body rows
- [ ] No unicode bullets — use LevelFormat.BULLET with numbering config
- [ ] ShadingType.CLEAR used (never SOLID)
- [ ] Logo placeholder noted with comment: // TODO: replace with ImageRun(asg-logo.png)
- [ ] Document validated after generation: python scripts/office/validate.py output.docx

---

## LOGO UPGRADE PATH

When a logo file is available:
1. Save as `asg-logo.png` (recommended: 600px wide, transparent background)
2. In all document header code, replace the TextRun wordmark block with:

```javascript
new ImageRun({
  data: fs.readFileSync("asg-logo.png"),
  transformation: { width: 160, height: 45 }, // adjust to actual dimensions
  type: "png"
})
```

3. Update this skill file — remove the placeholder note

---

## NOTES

- Brand colors: #25aae1 (primary blue), #58585a (charcoal gray)
- This skill is referenced by all document-producing skills in the ASG system
- Referenced by: `DOCX_BUILDER.md`, `REPORT_FORMATTER.md`
- Built by Roger Bauer / Authority Systems Group
- AuthoritySystemsGroup.com
