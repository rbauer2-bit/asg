#!/usr/bin/env python3
"""
generate_pdf_report.py
Authority Systems Group™ — Digital Intelligence Division

Generates a branded PDF marketing audit report from a JSON data file.

Usage:
    python3 scripts/generate_pdf_report.py <data.json> <output.pdf>
    python3 scripts/generate_pdf_report.py   # demo mode — creates MARKETING-REPORT-sample.pdf

Requires: pip3 install reportlab
"""

import sys
import json
import math
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, KeepTogether
    )
    from reportlab.platypus.flowables import HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.graphics.shapes import Drawing, Circle, Rect, String, Line
    from reportlab.graphics.charts.barcharts import HorizontalBarChart
    from reportlab.graphics import renderPDF
except ImportError:
    print("ERROR: reportlab is not installed.")
    print("Run: pip3 install reportlab")
    sys.exit(1)


# ─────────────────────────────────────────────
# ASG BRAND CONSTANTS
# ─────────────────────────────────────────────

ASG_BLUE        = HexColor("#25aae1")   # Primary — headers, titles, accents
ASG_CHARCOAL    = HexColor("#58585a")   # Body text, secondary headings
ASG_WHITE       = HexColor("#FFFFFF")
ASG_LIGHT_BLUE  = HexColor("#EAF6FC")   # Callout boxes, table tints
ASG_LIGHT_GRAY  = HexColor("#F5F5F5")   # Alternating table rows
ASG_BORDER      = HexColor("#CCCCCC")   # Table borders

# Score performance colors
COLOR_GREEN     = HexColor("#00C853")   # 80–100: Strong
COLOR_AMBER     = HexColor("#FFB300")   # 60–79: Solid
COLOR_ORANGE    = HexColor("#FF6B35")   # 40–59: Needs attention
COLOR_RED       = HexColor("#FF1744")   # 0–39: Critical

# Severity colors
SEV_CRITICAL    = HexColor("#FF1744")
SEV_HIGH        = HexColor("#FF6B35")
SEV_MEDIUM      = HexColor("#FFB300")
SEV_LOW         = ASG_BLUE


def score_color(score):
    if score >= 80:
        return COLOR_GREEN
    elif score >= 60:
        return COLOR_AMBER
    elif score >= 40:
        return COLOR_ORANGE
    else:
        return COLOR_RED


def score_label(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def severity_color(severity):
    s = severity.lower()
    if s == "critical":
        return SEV_CRITICAL
    elif s == "high":
        return SEV_HIGH
    elif s == "medium":
        return SEV_MEDIUM
    else:
        return SEV_LOW


# ─────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────

def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["cover_title"] = ParagraphStyle(
        "cover_title",
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=34,
        textColor=ASG_BLUE,
        spaceBefore=0,
        spaceAfter=22,
        alignment=TA_CENTER,
    )
    styles["cover_sub"] = ParagraphStyle(
        "cover_sub",
        fontName="Helvetica",
        fontSize=13,
        leading=18,
        textColor=ASG_CHARCOAL,
        spaceAfter=6,
        alignment=TA_CENTER,
    )
    styles["cover_tagline"] = ParagraphStyle(
        "cover_tagline",
        fontName="Helvetica-Oblique",
        fontSize=10,
        textColor=ASG_BLUE,
        spaceAfter=4,
        alignment=TA_CENTER,
    )
    styles["h1"] = ParagraphStyle(
        "h1",
        fontName="Helvetica-Bold",
        fontSize=18,
        textColor=ASG_BLUE,
        spaceBefore=16,
        spaceAfter=8,
    )
    styles["h2"] = ParagraphStyle(
        "h2",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=ASG_CHARCOAL,
        spaceBefore=12,
        spaceAfter=6,
    )
    styles["h3"] = ParagraphStyle(
        "h3",
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=ASG_BLUE,
        spaceBefore=8,
        spaceAfter=4,
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=10,
        textColor=ASG_CHARCOAL,
        spaceAfter=6,
        leading=14,
    )
    styles["body_sm"] = ParagraphStyle(
        "body_sm",
        fontName="Helvetica",
        fontSize=9,
        textColor=ASG_CHARCOAL,
        spaceAfter=4,
        leading=13,
    )
    styles["callout"] = ParagraphStyle(
        "callout",
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=ASG_BLUE,
        spaceBefore=8,
        spaceAfter=8,
        leftIndent=12,
        borderPad=8,
    )
    styles["table_header"] = ParagraphStyle(
        "table_header",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=ASG_WHITE,
    )
    styles["table_body"] = ParagraphStyle(
        "table_body",
        fontName="Helvetica",
        fontSize=9,
        textColor=ASG_CHARCOAL,
        leading=12,
    )
    styles["numbered"] = ParagraphStyle(
        "numbered",
        fontName="Helvetica",
        fontSize=10,
        textColor=ASG_CHARCOAL,
        spaceAfter=5,
        leftIndent=16,
        leading=14,
    )
    styles["footer"] = ParagraphStyle(
        "footer",
        fontName="Helvetica",
        fontSize=8,
        textColor=ASG_CHARCOAL,
        alignment=TA_CENTER,
    )

    return styles


# ─────────────────────────────────────────────
# SCORE GAUGE (circular dial)
# ─────────────────────────────────────────────

def build_score_gauge(score, size=160):
    """Draw a circular score gauge with ASG branding."""
    d = Drawing(size, size)

    cx, cy = size / 2, size / 2
    r_outer = size * 0.44
    r_inner = size * 0.30
    stroke_w = r_outer - r_inner

    color = score_color(score)
    angle_start = 225  # degrees — bottom left
    angle_range = 270  # degrees sweep
    angle_end = angle_start - (score / 100) * angle_range

    # Background arc (gray track)
    steps = 180
    for i in range(steps):
        a1 = math.radians(angle_start - (i / steps) * angle_range)
        a2 = math.radians(angle_start - ((i + 1) / steps) * angle_range)
        x1 = cx + r_outer * math.cos(a1)
        y1 = cy + r_outer * math.sin(a1)
        x2 = cx + r_outer * math.cos(a2)
        y2 = cy + r_outer * math.sin(a2)
        d.add(Line(x1, y1, x2, y2, strokeColor=ASG_BORDER, strokeWidth=stroke_w))

    # Score arc (colored)
    score_steps = max(1, int(steps * score / 100))
    for i in range(score_steps):
        a1 = math.radians(angle_start - (i / steps) * angle_range)
        a2 = math.radians(angle_start - ((i + 1) / steps) * angle_range)
        x1 = cx + r_outer * math.cos(a1)
        y1 = cy + r_outer * math.sin(a1)
        x2 = cx + r_outer * math.cos(a2)
        y2 = cy + r_outer * math.sin(a2)
        d.add(Line(x1, y1, x2, y2, strokeColor=color, strokeWidth=stroke_w))

    # Center circle (white fill)
    d.add(Circle(cx, cy, r_inner - 2, fillColor=ASG_WHITE, strokeColor=ASG_BORDER, strokeWidth=0.5))

    # Score number
    score_str = str(score)
    d.add(String(cx, cy + 6, score_str,
                 fontName="Helvetica-Bold", fontSize=size * 0.20,
                 fillColor=color, textAnchor="middle"))

    # Grade letter
    d.add(String(cx, cy - size * 0.14, score_label(score),
                 fontName="Helvetica-Bold", fontSize=size * 0.10,
                 fillColor=ASG_CHARCOAL, textAnchor="middle"))

    # "/100" label
    d.add(String(cx, cy - size * 0.22, "/ 100",
                 fontName="Helvetica", fontSize=size * 0.07,
                 fillColor=ASG_CHARCOAL, textAnchor="middle"))

    return d


# ─────────────────────────────────────────────
# HORIZONTAL BAR CHART
# ─────────────────────────────────────────────

def build_bar_chart(categories, width=440, height=180):
    """Horizontal bar chart for category scores."""
    names = list(categories.keys())
    scores = [categories[k]["score"] for k in names]

    d = Drawing(width, height)

    bar_h = 18
    gap = 8
    label_w = 140
    chart_w = width - label_w - 60
    y_start = height - 20

    for i, (name, score) in enumerate(zip(names, scores)):
        y = y_start - i * (bar_h + gap)
        color = score_color(score)

        # Background track
        d.add(Rect(label_w, y - bar_h, chart_w, bar_h,
                   fillColor=ASG_LIGHT_GRAY, strokeColor=ASG_BORDER, strokeWidth=0.5))

        # Score bar
        bar_len = (score / 100) * chart_w
        d.add(Rect(label_w, y - bar_h, bar_len, bar_h,
                   fillColor=color, strokeColor=None, strokeWidth=0))

        # Category label
        d.add(String(label_w - 6, y - bar_h + 4, name,
                     fontName="Helvetica", fontSize=8,
                     fillColor=ASG_CHARCOAL, textAnchor="end"))

        # Score value
        d.add(String(label_w + bar_len + 5, y - bar_h + 4, str(score),
                     fontName="Helvetica-Bold", fontSize=8,
                     fillColor=color, textAnchor="start"))

    return d


# ─────────────────────────────────────────────
# PAGE HEADER / FOOTER CANVAS
# ─────────────────────────────────────────────

class ASGCanvas:
    """Adds ASG header and footer to every page."""

    def __init__(self, business_name, report_date):
        self.business_name = business_name
        self.report_date = report_date

    def __call__(self, canvas, doc):
        canvas.saveState()
        w, h = letter

        # ── HEADER ──
        canvas.setFillColor(ASG_BLUE)
        canvas.setFont("Helvetica-Bold", 11)
        canvas.drawString(0.75 * inch, h - 0.55 * inch, "AUTHORITY SYSTEMS GROUP\u2122")

        canvas.setFillColor(ASG_CHARCOAL)
        canvas.setFont("Helvetica", 9)
        canvas.drawRightString(w - 0.75 * inch, h - 0.55 * inch,
                               f"Digital Authority Assessment  |  {self.business_name}")

        # Blue rule under header
        canvas.setStrokeColor(ASG_BLUE)
        canvas.setLineWidth(1.5)
        canvas.line(0.75 * inch, h - 0.65 * inch, w - 0.75 * inch, h - 0.65 * inch)

        # ── FOOTER ──
        canvas.setStrokeColor(ASG_BLUE)
        canvas.setLineWidth(0.75)
        canvas.line(0.75 * inch, 0.65 * inch, w - 0.75 * inch, 0.65 * inch)

        canvas.setFillColor(ASG_CHARCOAL)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(0.75 * inch, 0.45 * inch,
                          "Authority Systems Group\u2122  |  AuthoritySystemsGroup.com  |  Confidential")
        canvas.drawRightString(w - 0.75 * inch, 0.45 * inch,
                               f"Page {doc.page}  |  {self.report_date}")

        canvas.restoreState()


# ─────────────────────────────────────────────
# PAGE BUILDERS
# ─────────────────────────────────────────────

def build_cover_page(data, styles):
    """Page 1 — Cover with gauge and executive summary."""
    story = []

    story.append(Spacer(1, 0.3 * inch))

    # Report title
    story.append(Paragraph("Digital Authority Assessment", styles["cover_title"]))
    story.append(Paragraph(data.get("brand_name", ""), styles["cover_sub"]))
    story.append(Paragraph(data.get("url", ""), styles["cover_sub"]))
    story.append(Paragraph(data.get("date", ""), styles["cover_tagline"]))

    story.append(Spacer(1, 0.2 * inch))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ASG_BLUE))
    story.append(Spacer(1, 0.25 * inch))

    # Score gauge centered
    gauge = build_score_gauge(data.get("overall_score", 0), size=160)
    gauge_table = Table([[gauge]], colWidths=[6.5 * inch])
    gauge_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(gauge_table)

    story.append(Spacer(1, 0.2 * inch))

    # Executive summary box
    summary = data.get("executive_summary", "")
    if summary:
        summary_table = Table(
            [[Paragraph(summary, styles["body"])]],
            colWidths=[6.0 * inch]
        )
        summary_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), ASG_LIGHT_BLUE),
            ("LEFTPADDING", (0, 0), (-1, -1), 14),
            ("RIGHTPADDING", (0, 0), (-1, -1), 14),
            ("TOPPADDING", (0, 0), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ("BOX", (0, 0), (-1, -1), 1.5, ASG_BLUE),
        ]))
        story.append(summary_table)

    story.append(Spacer(1, 0.3 * inch))

    # Prepared by
    story.append(Paragraph(
        "Prepared by Authority Systems Group\u2122",
        styles["cover_tagline"]
    ))
    story.append(Paragraph(
        "Positioning You As The Authority",
        ParagraphStyle("italic_small", fontName="Helvetica-Oblique",
                       fontSize=9, textColor=ASG_CHARCOAL, alignment=TA_CENTER)
    ))

    story.append(PageBreak())
    return story


def build_score_page(data, styles):
    """Page 2 — Category score breakdown with bar chart."""
    story = []

    story.append(Paragraph("Score Breakdown", styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=1, color=ASG_BLUE))
    story.append(Spacer(1, 0.15 * inch))

    categories = data.get("categories", {})
    overall = data.get("overall_score", 0)

    # Bar chart
    if categories:
        chart = build_bar_chart(categories, width=480, height=len(categories) * 26 + 20)
        chart_table = Table([[chart]], colWidths=[6.5 * inch])
        chart_table.setStyle(TableStyle([
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ]))
        story.append(chart_table)
        story.append(Spacer(1, 0.2 * inch))

    # Score table
    table_data = [
        [
            Paragraph("Category", styles["table_header"]),
            Paragraph("Score", styles["table_header"]),
            Paragraph("Weight", styles["table_header"]),
            Paragraph("Status", styles["table_header"]),
        ]
    ]

    for i, (cat, vals) in enumerate(categories.items()):
        score = vals.get("score", 0)
        weight = vals.get("weight", "—")
        label = ("Strong" if score >= 80 else
                 "Solid" if score >= 60 else
                 "Needs Attention" if score >= 40 else
                 "Critical")
        bg = ASG_LIGHT_GRAY if i % 2 == 1 else ASG_WHITE
        table_data.append([
            Paragraph(cat, styles["table_body"]),
            Paragraph(str(score), styles["table_body"]),
            Paragraph(weight, styles["table_body"]),
            Paragraph(label, styles["table_body"]),
        ])

    # Overall row
    table_data.append([
        Paragraph("OVERALL SCORE", ParagraphStyle("bold_body", fontName="Helvetica-Bold",
                                                   fontSize=9, textColor=ASG_CHARCOAL)),
        Paragraph(str(overall), ParagraphStyle("bold_score", fontName="Helvetica-Bold",
                                                fontSize=9, textColor=score_color(overall))),
        Paragraph("", styles["table_body"]),
        Paragraph(score_label(overall), ParagraphStyle("bold_grade", fontName="Helvetica-Bold",
                                                        fontSize=9, textColor=score_color(overall))),
    ])

    col_widths = [3.2 * inch, 0.8 * inch, 0.8 * inch, 1.7 * inch]
    t = Table(table_data, colWidths=col_widths)

    row_count = len(table_data)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), ASG_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, row_count - 2), [ASG_WHITE, ASG_LIGHT_GRAY]),
        ("BACKGROUND", (0, row_count - 1), (-1, row_count - 1), ASG_LIGHT_BLUE),
        ("GRID", (0, 0), (-1, -1), 0.5, ASG_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]
    t.setStyle(TableStyle(style_cmds))
    story.append(t)

    story.append(PageBreak())
    return story


def build_findings_page(data, styles):
    """Page 3 — Key findings table."""
    story = []

    story.append(Paragraph("Key Findings", styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=1, color=ASG_BLUE))
    story.append(Spacer(1, 0.15 * inch))

    findings = data.get("findings", [])
    if not findings:
        story.append(Paragraph("No findings recorded.", styles["body"]))
        story.append(PageBreak())
        return story

    table_data = [
        [
            Paragraph("Severity", styles["table_header"]),
            Paragraph("Finding", styles["table_header"]),
        ]
    ]

    for i, f in enumerate(findings):
        sev = f.get("severity", "Low")
        finding_text = f.get("finding", "")
        sev_color = severity_color(sev)
        bg = ASG_LIGHT_GRAY if i % 2 == 1 else ASG_WHITE

        sev_style = ParagraphStyle(
            f"sev_{i}",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=sev_color,
        )
        table_data.append([
            Paragraph(sev, sev_style),
            Paragraph(finding_text, styles["table_body"]),
        ])

    t = Table(table_data, colWidths=[1.1 * inch, 5.4 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ASG_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ASG_WHITE, ASG_LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.5, ASG_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    story.append(PageBreak())
    return story


def build_action_plan_page(data, styles):
    """Page 4 — Prioritized action plan."""
    story = []

    story.append(Paragraph("Prioritized Action Plan", styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=1, color=ASG_BLUE))
    story.append(Spacer(1, 0.15 * inch))

    sections = [
        ("Quick Wins — This Week", data.get("quick_wins", []), COLOR_GREEN),
        ("Medium-Term — 1 to 3 Months", data.get("medium_term", []), COLOR_AMBER),
        ("Strategic — 3 to 6 Months", data.get("strategic", []), ASG_BLUE),
    ]

    for section_title, items, accent_color in sections:
        if not items:
            continue

        # Section header box
        header_table = Table(
            [[Paragraph(section_title, ParagraphStyle(
                "section_header",
                fontName="Helvetica-Bold",
                fontSize=11,
                textColor=ASG_WHITE,
            ))]],
            colWidths=[6.5 * inch]
        )
        header_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), accent_color),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]))
        story.append(header_table)

        for i, item in enumerate(items, 1):
            story.append(Paragraph(f"{i}.  {item}", styles["numbered"]))

        story.append(Spacer(1, 0.15 * inch))

    story.append(PageBreak())
    return story


def build_competitors_page(data, styles):
    """Page 5 — Competitive landscape (optional)."""
    competitors = data.get("competitors", [])
    if not competitors:
        return []

    story = []
    brand = data.get("brand_name", "Your Business")

    story.append(Paragraph("Competitive Landscape", styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=1, color=ASG_BLUE))
    story.append(Spacer(1, 0.15 * inch))

    # Build column headers: row label + brand + competitors
    comp_names = [c.get("name", f"Competitor {i+1}") for i, c in enumerate(competitors[:3])]
    headers = [""] + [brand] + comp_names
    n_cols = len(headers)
    col_w = 6.5 * inch / n_cols
    col_widths = [col_w] * n_cols

    header_row = [Paragraph(h, styles["table_header"]) for h in headers]

    rows_config = [
        ("Positioning", "positioning"),
        ("Pricing", "pricing"),
        ("Social Proof", "social_proof"),
        ("Content", "content"),
    ]

    table_data = [header_row]
    for i, (label, field) in enumerate(rows_config):
        bg = ASG_LIGHT_GRAY if i % 2 == 1 else ASG_WHITE
        # Brand column: blank (this is the client — they know their own info)
        row = [Paragraph(label, styles["table_body"]), Paragraph("—", styles["table_body"])]
        for comp in competitors[:3]:
            row.append(Paragraph(comp.get(field, "—"), styles["table_body"]))
        table_data.append(row)

    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ASG_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ASG_WHITE, ASG_LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.5, ASG_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 1), (0, -1), ASG_CHARCOAL),
    ]))
    story.append(t)

    story.append(PageBreak())
    return story


def build_methodology_page(styles):
    """Final page — Methodology and scoring guide."""
    story = []

    story.append(Paragraph("Methodology", styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=1, color=ASG_BLUE))
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph(
        "This Digital Authority Assessment evaluates six dimensions of digital marketing performance, "
        "each weighted by its relative impact on client acquisition and revenue growth for "
        "professional service businesses.",
        styles["body"]
    ))

    story.append(Spacer(1, 0.1 * inch))

    # Scoring table
    table_data = [
        [
            Paragraph("Category", styles["table_header"]),
            Paragraph("Weight", styles["table_header"]),
            Paragraph("What It Measures", styles["table_header"]),
        ],
        [Paragraph("Content & Messaging", styles["table_body"]),
         Paragraph("25%", styles["table_body"]),
         Paragraph("Copy quality, value proposition, headline clarity, brand voice", styles["table_body"])],
        [Paragraph("Conversion Optimization", styles["table_body"]),
         Paragraph("20%", styles["table_body"]),
         Paragraph("Social proof, form design, CTA placement, objection handling", styles["table_body"])],
        [Paragraph("SEO & Discoverability", styles["table_body"]),
         Paragraph("20%", styles["table_body"]),
         Paragraph("Title tags, meta descriptions, schema, internal linking, page speed", styles["table_body"])],
        [Paragraph("Competitive Positioning", styles["table_body"]),
         Paragraph("15%", styles["table_body"]),
         Paragraph("Differentiation, pricing clarity, comparison content", styles["table_body"])],
        [Paragraph("Brand & Trust", styles["table_body"]),
         Paragraph("10%", styles["table_body"]),
         Paragraph("Design quality, trust badges, security indicators, professionalism", styles["table_body"])],
        [Paragraph("Growth & Strategy", styles["table_body"]),
         Paragraph("10%", styles["table_body"]),
         Paragraph("Lead capture, email marketing, content strategy, acquisition channels", styles["table_body"])],
    ]

    t = Table(table_data, colWidths=[2.0 * inch, 0.8 * inch, 3.7 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ASG_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ASG_WHITE, ASG_LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.5, ASG_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.2 * inch))

    # Grade scale
    story.append(Paragraph("Grading Scale", styles["h2"]))

    grade_data = [
        [Paragraph("Score", styles["table_header"]),
         Paragraph("Grade", styles["table_header"]),
         Paragraph("Meaning", styles["table_header"])],
        [Paragraph("85–100", styles["table_body"]),
         Paragraph("A", styles["table_body"]),
         Paragraph("Excellent — minor optimizations only", styles["table_body"])],
        [Paragraph("70–84", styles["table_body"]),
         Paragraph("B", styles["table_body"]),
         Paragraph("Good — clear opportunities for improvement", styles["table_body"])],
        [Paragraph("55–69", styles["table_body"]),
         Paragraph("C", styles["table_body"]),
         Paragraph("Average — significant gaps to address", styles["table_body"])],
        [Paragraph("40–54", styles["table_body"]),
         Paragraph("D", styles["table_body"]),
         Paragraph("Below average — major overhaul needed", styles["table_body"])],
        [Paragraph("0–39", styles["table_body"]),
         Paragraph("F", styles["table_body"]),
         Paragraph("Critical — fundamental marketing issues", styles["table_body"])],
    ]

    g = Table(grade_data, colWidths=[1.2 * inch, 0.8 * inch, 4.5 * inch])
    g.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ASG_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ASG_WHITE, ASG_LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.5, ASG_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(g)

    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph(
        "Prepared by Authority Systems Group\u2122 | AuthoritySystemsGroup.com",
        ParagraphStyle("method_footer", fontName="Helvetica-Oblique",
                       fontSize=9, textColor=ASG_CHARCOAL, alignment=TA_CENTER)
    ))

    return story


# ─────────────────────────────────────────────
# MAIN GENERATOR
# ─────────────────────────────────────────────

def generate_pdf(data, output_path):
    styles = build_styles()
    business_name = data.get("brand_name", "Client")
    report_date = data.get("date", datetime.today().strftime("%B %d, %Y"))

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.75 * inch,
    )

    canvas_fn = ASGCanvas(business_name, report_date)

    story = []
    story += build_cover_page(data, styles)
    story += build_score_page(data, styles)
    story += build_findings_page(data, styles)
    story += build_action_plan_page(data, styles)
    story += build_competitors_page(data, styles)
    story += build_methodology_page(styles)

    doc.build(story, onFirstPage=canvas_fn, onLaterPages=canvas_fn)
    print(f"PDF created: {output_path}")


# ─────────────────────────────────────────────
# DEMO DATA
# ─────────────────────────────────────────────

DEMO_DATA = {
    "url": "https://example-lawfirm.com",
    "date": datetime.today().strftime("%B %d, %Y"),
    "brand_name": "Example Law Firm",
    "overall_score": 62,
    "executive_summary": (
        "Example Law Firm's digital presence shows solid SEO fundamentals but significant "
        "conversion and trust signal gaps that are likely costing 3–5 qualified leads per month. "
        "The homepage lacks a clear value proposition and social proof above the fold, "
        "and there is no structured lead capture mechanism beyond a generic contact form. "
        "Addressing the top three conversion issues alone could increase lead volume by 40–60% "
        "without additional ad spend."
    ),
    "categories": {
        "Content & Messaging":    {"score": 58, "weight": "25%"},
        "Conversion Optimization": {"score": 44, "weight": "20%"},
        "SEO & Discoverability":  {"score": 74, "weight": "20%"},
        "Competitive Positioning": {"score": 52, "weight": "15%"},
        "Brand & Trust":          {"score": 70, "weight": "10%"},
        "Growth & Strategy":      {"score": 48, "weight": "10%"},
    },
    "findings": [
        {"severity": "Critical",
         "finding": "Homepage headline reads 'Welcome to Our Firm' — no value proposition, no differentiation, no reason for a visitor to stay."},
        {"severity": "Critical",
         "finding": "No testimonials or case results visible on homepage or services pages. Social proof is buried in a separate 'Reviews' tab with 3 entries."},
        {"severity": "High",
         "finding": "Contact form is the only lead capture mechanism. No lead magnet, no free consultation CTA above the fold, no chat widget."},
        {"severity": "High",
         "finding": "Page load time is 4.8 seconds on mobile (benchmark: under 2.5s). This directly impacts both SEO ranking and bounce rate."},
        {"severity": "Medium",
         "finding": "No Google Business Profile posts in 6+ months. GBP activity is a local ranking signal and a direct client touchpoint."},
        {"severity": "Medium",
         "finding": "Services pages average 180 words each — not enough to rank or to overcome buyer objections. Competitors average 600–900 words."},
        {"severity": "Low",
         "finding": "About page has no attorney bio photos. Personal connection is a primary trust driver in legal services."},
    ],
    "quick_wins": [
        "Rewrite homepage headline to lead with client outcome: 'Dallas Family Law Attorney — Protecting Your Family's Future'",
        "Add 3–5 client testimonials (or anonymized case outcomes) directly to the homepage above the fold",
        "Create a free consultation CTA button in the navigation bar — present on every page",
    ],
    "medium_term": [
        "Expand all services pages to 600–900 words with FAQs, objection handling, and case result examples",
        "Implement a lead magnet (e.g. 'The 7 Mistakes People Make During Divorce') with email capture",
        "Set up Google Business Profile posting schedule — minimum 2 posts per week",
    ],
    "strategic": [
        "Build a content authority strategy: 2 SEO blog posts per month targeting local search intent keywords",
        "Launch a structured review acquisition system — post-engagement automated request via SMS/email",
        "Implement conversion tracking (Google Analytics 4 + call tracking) to establish baseline lead volume data",
    ],
    "competitors": [
        {
            "name": "Smith & Associates",
            "positioning": "High-volume family law, emphasizes experience",
            "pricing": "Transparent flat fees listed on website",
            "social_proof": "200+ Google reviews, 4.9 stars",
            "content": "Weekly blog, active YouTube channel",
        },
        {
            "name": "Dallas Family Legal",
            "positioning": "Boutique firm, emphasizes personal attention",
            "pricing": "Free consultation, no pricing listed",
            "social_proof": "85 Google reviews, 4.7 stars",
            "content": "Monthly newsletter, active GBP",
        },
    ],
}


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Demo mode
        print("Running in demo mode — generating sample report...")
        generate_pdf(DEMO_DATA, "MARKETING-REPORT-sample.pdf")

    elif len(sys.argv) == 3:
        json_path = sys.argv[1]
        output_path = sys.argv[2]

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"ERROR: JSON file not found: {json_path}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {json_path}: {e}")
            sys.exit(1)

        generate_pdf(data, output_path)

    else:
        print("Usage:")
        print("  python3 scripts/generate_pdf_report.py <data.json> <output.pdf>")
        print("  python3 scripts/generate_pdf_report.py   # demo mode")
        sys.exit(1)
