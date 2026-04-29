"""
PDF Report Generator — Creates downloadable analysis reports using ReportLab.
"""

import io
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY


def generate_analysis_report(analysis):
    """
    Generate a professional PDF report for a resume analysis.
    
    Args:
        analysis: AnalysisResult model instance
        
    Returns:
        io.BytesIO: PDF file buffer
    """
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
    )
    
    # Custom styles
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        name='ReportTitle',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=6,
        textColor=colors.HexColor('#E63946'),
        alignment=TA_CENTER,
    ))
    
    styles.add(ParagraphStyle(
        name='ReportSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=20,
        textColor=colors.HexColor('#6b7280'),
        alignment=TA_CENTER,
    ))
    
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=10,
        textColor=colors.HexColor('#1e293b'),
        borderPadding=(0, 0, 4, 0),
    ))
    
    styles.add(ParagraphStyle(
        name='BodyText2',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        leading=14,
        alignment=TA_JUSTIFY,
    ))
    
    styles.add(ParagraphStyle(
        name='SkillMatched',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#059669'),
    ))
    
    styles.add(ParagraphStyle(
        name='SkillMissing',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#dc2626'),
    ))
    
    # Build content
    content = []
    
    # === HEADER ===
    content.append(Paragraph("SkillSync AI", styles['ReportTitle']))
    content.append(Paragraph("Resume Analysis Report", styles['ReportSubtitle']))
    content.append(HRFlowable(
        width="100%", thickness=2,
        color=colors.HexColor('#E63946'),
        spaceAfter=20
    ))
    
    # === OVERVIEW TABLE ===
    content.append(Paragraph("📋 Overview", styles['SectionHeader']))
    
    overview_data = [
        ['Resume', analysis.resume.original_filename],
        ['Job Title', analysis.job_title or 'Not specified'],
        ['Category', analysis.get_category_display()],
        ['Overall Score', f"{analysis.overall_score:.0f} / 100"],
        ['Analysis Date', analysis.analyzed_at.strftime('%B %d, %Y at %I:%M %p')],
    ]
    
    overview_table = Table(overview_data, colWidths=[120, 380])
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f1f5f9')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#475569')),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    content.append(overview_table)
    content.append(Spacer(1, 15))
    
    # === SCORE INTERPRETATION ===
    score = analysis.overall_score
    if score >= 80:
        score_text = "Excellent Match — Strong candidate for this role."
        score_color = '#059669'
    elif score >= 60:
        score_text = "Good Match — Meets most requirements with some gaps."
        score_color = '#d97706'
    elif score >= 40:
        score_text = "Partial Match — Significant skill gaps identified."
        score_color = '#ea580c'
    else:
        score_text = "Weak Match — Major upskilling needed for this role."
        score_color = '#dc2626'
    
    content.append(Paragraph(
        f'<font color="{score_color}"><b>Score Assessment:</b> {score_text}</font>',
        styles['BodyText2']
    ))
    content.append(Spacer(1, 10))
    
    # === MATCHED SKILLS ===
    matched = analysis.matched_skills
    if matched:
        content.append(Paragraph("✅ Matched Skills", styles['SectionHeader']))
        skills_text = " • ".join(matched)
        content.append(Paragraph(
            f'<font color="#059669">{skills_text}</font>',
            styles['BodyText2']
        ))
        content.append(Spacer(1, 10))
    
    # === MISSING SKILLS ===
    missing = analysis.missing_skills
    if missing:
        content.append(Paragraph("❌ Missing Skills (Skill Gaps)", styles['SectionHeader']))
        skills_text = " • ".join(missing)
        content.append(Paragraph(
            f'<font color="#dc2626">{skills_text}</font>',
            styles['BodyText2']
        ))
        content.append(Spacer(1, 10))
    
    # === STRENGTHS ===
    strengths = analysis.strengths
    if strengths:
        content.append(Paragraph("💪 Key Strengths", styles['SectionHeader']))
        for s in strengths:
            content.append(Paragraph(f"• {s}", styles['BodyText2']))
        content.append(Spacer(1, 10))
    
    # === DETAILED FEEDBACK ===
    if analysis.detailed_feedback:
        content.append(Paragraph("📝 Detailed Analysis", styles['SectionHeader']))
        # Split by newlines and add as paragraphs
        for para in analysis.detailed_feedback.split('\n'):
            if para.strip():
                content.append(Paragraph(para.strip(), styles['BodyText2']))
        content.append(Spacer(1, 10))
    
    # === SKILL COMPARISON TABLE ===
    skill_scores = analysis.skill_scores
    required_scores = analysis.required_scores
    
    if skill_scores and required_scores:
        content.append(Paragraph("📊 Skill Proficiency Comparison", styles['SectionHeader']))
        
        table_data = [['Skill', 'Your Level', 'Required Level', 'Gap']]
        for skill in skill_scores:
            current = skill_scores.get(skill, 0)
            required = required_scores.get(skill, 0)
            gap = required - current
            gap_str = f"+{abs(gap)}" if gap <= 0 else f"-{gap}"
            table_data.append([skill, f"{current}%", f"{required}%", gap_str])
        
        skill_table = Table(table_data, colWidths=[150, 100, 100, 80])
        skill_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0F0F0F')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('PADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ]))
        content.append(skill_table)
        content.append(Spacer(1, 15))
    
    # === RECOMMENDATIONS ===
    recommendations = analysis.recommendations
    if recommendations:
        content.append(Paragraph("🚀 Recommended Actions", styles['SectionHeader']))
        for i, rec in enumerate(recommendations, 1):
            if isinstance(rec, dict):
                title = rec.get('title', 'Recommendation')
                desc = rec.get('description', '')
                skill = rec.get('skill_target', '')
                content.append(Paragraph(
                    f"<b>{i}. {title}</b> <font color='#6b7280'>(Target: {skill})</font>",
                    styles['BodyText2']
                ))
                if desc:
                    content.append(Paragraph(f"   {desc}", styles['BodyText2']))
            else:
                content.append(Paragraph(f"{i}. {rec}", styles['BodyText2']))
        content.append(Spacer(1, 10))
    
    # === FOOTER ===
    content.append(HRFlowable(
        width="100%", thickness=1,
        color=colors.HexColor('#e2e8f0'),
        spaceBefore=20, spaceAfter=10
    ))
    content.append(Paragraph(
        f"<font size='8' color='#9ca3af'>Generated by SkillSync AI on "
        f"{datetime.now().strftime('%B %d, %Y at %I:%M %p')} • "
        f"This is an AI-generated analysis and should be used as guidance only.</font>",
        styles['Normal']
    ))
    
    # Build PDF
    doc.build(content)
    buffer.seek(0)
    
    return buffer
