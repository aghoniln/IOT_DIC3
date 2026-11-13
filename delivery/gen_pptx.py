import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

COLOR_NAVY = RGBColor(26, 54, 93)     # #1A365D
COLOR_BLUE = RGBColor(49, 130, 206)   # #3182CE
COLOR_DARK = RGBColor(45, 55, 72)     # #2D3748
COLOR_GRAY = RGBColor(113, 128, 150)  # #718096
COLOR_BG = RGBColor(247, 250, 252)    # #F7FAFC
COLOR_WHITE = RGBColor(255, 255, 255)

def add_header(slide, title_text, category="DIETSENSE / PROPOSAL"):
    # Header tag
    tx_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.5), Inches(0.4))
    tf_c = tx_cat.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.size = Pt(11)
    p_c.font.bold = True
    p_c.font.color.rgb = COLOR_BLUE

    # Title
    tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.5), Inches(0.8))
    tf_t = tx_title.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(24)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_NAVY

# Slide 1: Title
s1 = prs.slides.add_slide(blank_layout)
tx_main = s1.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(3.0))
tf1 = tx_main.text_frame
p1 = tf1.paragraphs[0]
p1.text = "DietSense"
p1.font.size = Pt(44)
p1.font.bold = True
p1.font.color.rgb = COLOR_NAVY

p2 = tf1.add_paragraph()
p2.text = "A Data-Grounded & Safety-Aware Conversational AI Agent for Personalized Dietary Assessment"
p2.font.size = Pt(20)
p2.font.color.rgb = COLOR_BLUE
p2.space_before = Pt(10)

p3 = tf1.add_paragraph()
p3.text = "Core: AI Agent + Nutrition Domain Knowledge + Food Data Analytics + Real-World Health Application\nNCHU DIC3 Course Final Project Proposal | Spec-Driven Development"
p3.font.size = Pt(13)
p3.font.color.rgb = COLOR_GRAY
p3.space_before = Pt(20)

# Slide 2: Motivation & Background (A & B)
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "Motivation & Challenges: Why Dietary Tracking Fails", "01. PROBLEM & BACKGROUND")
tx2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf2 = tx2.text_frame
tf2.word_wrap = True

p = tf2.paragraphs[0]
p.text = "• Public Health Urgency:"
p.font.bold = True
p.font.size = Pt(16)
p.font.color.rgb = COLOR_NAVY
p_sub = tf2.add_paragraph()
p_sub.text = "  - Global: 2.6B adults overweight; 940M living with obesity (WHO 2024).\n  - Taiwan: 50.3% adult overweight/obesity prevalence (NAHSIT 2017-2020)."
p_sub.font.size = Pt(14)
p_sub.font.color.rgb = COLOR_DARK

p = tf2.add_paragraph()
p.text = "• The Self-Monitoring Bottleneck (SMARTER Trial, Burke et al. 2025):"
p.font.bold = True
p.font.size = Pt(16)
p.font.color.rgb = COLOR_NAVY
p.space_before = Pt(14)
p_sub = tf2.add_paragraph()
p_sub.text = "  - Self-monitoring adherence declines nonlinearly over 12 months; self-reported error spans 18%-54%.\n  - High cognitive friction in existing apps: manual search, weighing, and composite dish decomposition."
p_sub.font.size = Pt(14)
p_sub.font.color.rgb = COLOR_DARK

p = tf2.add_paragraph()
p.text = "• Standalone LLM Hallucinations (Fridolfsson et al. 2025):"
p.font.bold = True
p.font.size = Pt(16)
p.font.color.rgb = COLOR_NAVY
p.space_before = Pt(14)
p_sub = tf2.add_paragraph()
p_sub.text = "  - LLM image calorie estimation has ~35.8% MAPE with systematic underestimation of large portions.\n  - Cannot verify cooking oil, soup broths, or provide clinical guardrails without tool anchoring."
p_sub.font.size = Pt(14)
p_sub.font.color.rgb = COLOR_DARK

# Slide 3: Proposed Solution & Core Innovation (C)
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "Cure: 'LLM Orchestrates, Deterministic Tools Compute'", "02. CORE PARADIGM SHIFT")
tx3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf3 = tx3.text_frame
tf3.word_wrap = True

p = tf3.paragraphs[0]
p.text = "DietSense Core Paradigm:"
p.font.bold = True
p.font.size = Pt(18)
p.font.color.rgb = COLOR_NAVY

innovations = [
    ("1. Conversational Food NER & Clarification:", "Transforms colloquial Traditional Chinese into structured food entities with bounded multi-turn clarification (<= 2 rounds)."),
    ("2. Data-Grounded Multi-Source Retrieval:", "Prioritizes Taiwan Food Composition DB (TFDA) -> Curated Taiwanese Dish Cards (Vector RAG) -> USDA FoodData Central. Full provenance tracking."),
    ("3. Deterministic Analytics Engine:", "Zero LLM math: E = portion(g) * kcal_100g / 100 and Mifflin-St Jeor BMR/TDEE are computed strictly by deterministic code."),
    ("4. Uncertainty as a Calibrated Interval:", "Outputs [low, point, high] kcal intervals with confidence scores rather than false single numbers."),
    ("5. Deterministic Safety Guardrails:", "Hard rule interception on < 1,200 kcal/day floors, disordered-eating language, and pregnant/chronic health routing.")
]

for title, desc in innovations:
    p_t = tf3.add_paragraph()
    p_t.text = f"• {title}"
    p_t.font.bold = True
    p_t.font.size = Pt(15)
    p_t.font.color.rgb = COLOR_BLUE
    p_t.space_before = Pt(8)
    
    p_d = tf3.add_paragraph()
    p_d.text = f"   {desc}"
    p_d.font.size = Pt(13.5)
    p_d.font.color.rgb = COLOR_DARK

# Slide 4: 8-Module Architecture (D)
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "Eight-Module Agentic Architecture", "03. SYSTEM DESIGN")
tx4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf4 = tx4.text_frame
tf4.word_wrap = True

modules_summary = [
    ("(1) User / Scenario", "Daily colloquial Chinese meal input via Web/Mobile Chat interface."),
    ("(2) Input Processing", "Whisper ASR, OpenCC normalization, Intent Classification (5 types), and Food NER."),
    ("(3) Planner Agent", "LLM reasoning, whitelisted function calling, conversation memory, Response Guard."),
    ("(4) Data Retrieval", "TFDA Food Database, Local Dish Vector DB, USDA API, and local daily log storage."),
    ("(5) Analytics Engine", "Deterministic kcal, macronutrient breakdown (AMDR), Mifflin-St Jeor BMR/TDEE, interval logic."),
    ("(6) Domain Knowledge", "Taiwan household container portion table (P10-P90), dietary guidelines, safety rules YAML."),
    ("(7) Decision / Advice", "Daily calorie gap, healthy Taiwanese substitute recommendations, safety status (OK/WARN/DANGER)."),
    ("(8) Output Interaction", "Structured Markdown, macronutrient pie charts, 7-day trend intervals, auditable sources.")
]

for m_title, m_desc in modules_summary:
    p = tf4.add_paragraph()
    p.text = f"{m_title}: {m_desc}"
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_DARK
    p.space_before = Pt(4)

# Slide 5: Deep Research & Controversies
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Deep Research: Mindsets & Professional Controversies", "04. DOMAIN GROUNDING")
tx5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf5 = tx5.text_frame
tf5.word_wrap = True

p = tf5.paragraphs[0]
p.text = "5 Core Mental Models:"
p.font.bold = True
p.font.size = Pt(16)
p.font.color.rgb = COLOR_NAVY
p_sub = tf5.add_paragraph()
p_sub.text = "1. Energy Balance (Hall 2011) | 2. Macronutrient AMDR (IOM 2005) | 3. Portion Uncertainty (Poslusna 2009)\n4. Individual Variation (Zeevi 2015) | 5. Behavioral Context (Burke 2025 SMARTER trial)"
p_sub.font.size = Pt(13.5)
p_sub.font.color.rgb = COLOR_DARK

p = tf5.add_paragraph()
p.text = "3 Critical Domain Debates & System Trade-Offs:"
p.font.bold = True
p.font.size = Pt(16)
p.font.color.rgb = COLOR_NAVY
p.space_before = Pt(12)

debates = [
    ("T1. Quantity vs Quality:", "Calorie deficit drives weight loss (Gardner 2018), but food quality governs satiety and hormonal responses (Hall 2019). DietSense computes calories as primary while displaying AMDR balance & processing tags."),
    ("T2. AI vs Hardware Measurement:", "Pure AI image estimation yields ~36% MAPE (Fridolfsson 2025). DietSense chooses zero-hardware conversational convenience, compensating via bounded intervals & clarification."),
    ("T3. Universal vs Personalized:", "Dietary guidelines set safe baselines; metabolic precision optimizes adherence. DietSense layers personal TDEE over hard safety limits (<1,200 kcal floor).")
]
for d_title, d_desc in debates:
    p_d = tf5.add_paragraph()
    p_d.text = f"• {d_title} {d_desc}"
    p_d.font.size = Pt(13)
    p_d.font.color.rgb = COLOR_DARK
    p_d.space_before = Pt(4)

# Slide 6: Evaluation Plan & Expected Outcomes (E & F)
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Planned Evaluation & Expected Outcomes", "05. VERIFICATION & METRICS")
tx6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf6 = tx6.text_frame
tf6.word_wrap = True

p = tf6.paragraphs[0]
p.text = "Experimental Setup (Proposal Stage Targets -- No Fabricated Data):"
p.font.bold = True
p.font.size = Pt(16)
p.font.color.rgb = COLOR_NAVY

points = [
    ("Dataset:", "500 annotated Taiwanese meal descriptions (night-market snacks, bento, noodle soups, beverages)."),
    ("Baselines:", "(1) MyFitnessPal manual form entry, (2) Pure ungrounded LLM zero-shot prompt."),
    ("User Study:", "20 participants x 7 consecutive days measuring completion time, dropout rate, and SUS score."),
    ("Expected Target 1:", "Calorie estimation accuracy within +-20% error margin: > 85%"),
    ("Expected Target 2:", "Meal logging time reduction compared to manual search: ~60% faster"),
    ("Expected Target 3:", "System Usability Scale (SUS) score: > 70 (Good / High Acceptability)"),
    ("Expected Target 4:", "Safety interception on red-team eating disorder & extreme deficit queries: 100%")
]

for k, v in points:
    p_p = tf6.add_paragraph()
    p_p.text = f"• {k} {v}"
    p_p.font.size = Pt(13.5)
    p_p.font.color.rgb = COLOR_DARK
    p_p.space_before = Pt(4)

# Slide 7: Spec-Driven Development & Conclusion
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "OpenSpec Workflow & Handover Readiness", "06. SPEC-DRIVEN DEVELOPMENT")
tx7 = s7.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf7 = tx7.text_frame
tf7.word_wrap = True

p = tf7.paragraphs[0]
p.text = "Engineering Rigor via OpenSpec (SDD):"
p.font.bold = True
p.font.size = Pt(16)
p.font.color.rgb = COLOR_NAVY

sdd_points = [
    ("Strict Validation Passed:", "openspec validate build-dietsense-agent --strict (Proposal, 8 Specs, Design, Tasks)."),
    ("Auditable Delta Specs:", "8 durable capabilities defined with strict SHALL clauses and testable WHEN/THEN Scenarios."),
    ("Deterministic Guardrails:", "Response Guard asserts that all numbers in LLM responses are mathematical subsets of tool outputs."),
    ("Final Handover Compliance:", "Even if original developers leave, successors can execute, test, and expand via GitHub + README.md + DESIGN.md.")
]
for k, v in sdd_points:
    p_s = tf7.add_paragraph()
    p_s.text = f"• {k} {v}"
    p_s.font.size = Pt(14)
    p_s.font.color.rgb = COLOR_DARK
    p_s.space_before = Pt(6)

p_end = tf7.add_paragraph()
p_end.text = "\nGitHub Repository: https://github.com/aghoniln/IOT_DIC3"
p_end.font.bold = True
p_end.font.size = Pt(15)
p_end.font.color.rgb = COLOR_BLUE

pptx_out = r"C:\Users\譚人傑\.gemini\antigravity\scratch\2026-11-11-DIC3-ProjectRefactor\delivery\DietSense_Proposal_Presentation.pptx"
prs.save(pptx_out)
print("SUCCESS: PPTX generated at " + pptx_out)