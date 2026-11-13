import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = Document()
for s in doc.sections:
    s.top_margin = Inches(1.0)
    s.bottom_margin = Inches(1.0)
    s.left_margin = Inches(1.0)
    s.right_margin = Inches(1.0)

COLOR_NAVY = RGBColor(26, 54, 93)
COLOR_GRAY = RGBColor(113, 128, 150)
COLOR_BLACK = RGBColor(45, 55, 72)

def format_run(run, font_name="Times New Roman", size_pt=11, bold=False, italic=False, color=COLOR_BLACK):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    format_run(run, size_pt=17, bold=True, color=COLOR_NAVY)

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(14)
    run = p.add_run(text)
    format_run(run, size_pt=11.5, italic=True, color=COLOR_GRAY)

def add_h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    format_run(run, size_pt=13.5, bold=True, color=COLOR_NAVY)

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    format_run(run, size_pt=11.5, bold=True, color=COLOR_BLACK)

def add_p(text, bold_prefix=None, space_after=5):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        format_run(r_pre, size_pt=10.5, bold=True, color=COLOR_BLACK)
    r_body = p.add_run(text)
    format_run(r_body, size_pt=10.5, bold=False, color=COLOR_BLACK)
    return p

add_title("DietSense: A Data-Grounded and Safety-Aware Conversational AI Agent for Personalized Dietary Assessment and Weight Management")
add_subtitle("Final Project Proposal -- NCHU DIC3 Course | Domain AI Agent Specification")

add_h1("Abstract")
abstract_text = (
    "The increasing prevalence of overweight and obesity, affecting an estimated 2.6 billion adults worldwide in 2024 "
    "(including 940 million individuals living with obesity), underscores the urgent need for sustainable dietary monitoring. "
    "However, conventional dietary tracking applications impose substantial cognitive burden through manual database searching, portion estimation, "
    "and ingredient decomposition, leading to steep attrition rates where adherence declines nonlinearly over time. "
    "Self-reported intake is systematically biased by 18% to 54%, and standalone Large Language Models (LLMs) suffer from severe numerical hallucinations "
    "(e.g., ~35.8% MAPE in caloric estimation) when answering directly without grounding. "
    "To address these limitations, this project proposes DietSense, a data-grounded and safety-aware conversational Domain AI Agent. "
    "DietSense is designed under the core principle of 'LLM orchestrates, deterministic domain tools compute': the LLM coordinates natural language intent, "
    "food entity recognition, and clarification loops, whereas numerical calculations are delegated strictly to whitelisted APIs querying the Taiwan Food Composition Database, "
    "a dedicated vector database of Taiwanese cuisine, and USDA FoodData Central. "
    "Energy and macronutrient requirements are deterministically computed via the Mifflin-St Jeor equation and total daily energy expenditure (TDEE) models, "
    "while uncertainty is propagated as confidence-bounded caloric intervals rather than false-precision point estimates. "
    "A deterministic safety guardrail enforces a 1,200 kcal/day minimum floor and intercepts eating-disorder signals. "
    "An evaluation framework with 500 annotated Taiwanese meal descriptions is proposed to verify accuracy (targeting >85% within +-20% error), "
    "logging efficiency (targeting ~60% time reduction), and system usability (target SUS >70). "
    "DietSense demonstrates how tool-grounded AI architectures can reconcile conversational convenience with scientific rigor in cultural nutrition."
)
add_p(abstract_text, bold_prefix="Abstract-- ")
add_p("Conversational AI, Domain-Specific AI Agents, Dietary Assessment, Large Language Models, Retrieval-Augmented Generation (RAG), Uncertainty Quantification, Personalized Weight Management, Safety Guardrails.", bold_prefix="Index Terms-- ")

add_h1("I. Introduction")
add_p("Overweight and obesity have become chronic, population-scale health problems. According to the World Health Organization, 2.6 billion adults--45% of the world's adult population--are overweight, and 940 million of them live with obesity [1]. Taiwan mirrors this trend: the 2017-2020 Nutrition and Health Survey in Taiwan reported that 50.3% of adults are overweight or obese [2]. Because obesity requires long-term management rather than one-off treatment, tools that help people sustainably monitor what they eat are of direct public-health value.", bold_prefix="A. Attention Getter. ")
add_p("Dietary self-monitoring is one of the most consistently supported behaviors in weight management; systematic reviews associate more frequent self-monitoring with greater weight loss [4], [5]. Smartphone applications have made logging ubiquitous, and recent advances in large language models (LLMs) now allow systems to understand free-form meal descriptions, conduct multi-turn dialogue, and invoke external tools [11]-[13]. These capabilities suggest that dietary logging could shift from form-filling to conversation--particularly valuable in Taiwan, where meals are frequently eaten out and consist of mixed dishes, soups, and night-market foods that are poorly represented in Western food databases.", bold_prefix="B. Background. ")
add_p("The practical problem is that accurate dietary logging is cognitively expensive. A user who eats 'a bowl of Taiwanese beef noodle soup with an egg, drinking half of the soup' must (i) search a database for the correct item, (ii) estimate portion weight without a scale, (iii) decompose the composite dish into components, and (iv) adjust for partial consumption. This burden contributes to declining adherence: in the 12-month SMARTER trial, adherence to dietary self-monitoring declined nonlinearly over time [3]. At the same time, self-reported intake is systematically biased, with energy under-reporting of 18%-54% [6], and portion size, hidden cooking oil, and soups amplify the uncertainty. This project therefore addresses the following question: How can a system reduce the effort of dietary logging for Taiwanese meals while keeping its nutritional estimates traceable, honest about uncertainty, and safe?", bold_prefix="C. Problem. ")
add_p("Current approaches each solve only part of this problem. (1) Manual tracking applications (e.g., MyFitnessPal) achieve reasonable energy correlation once data are cleaned [7], but rely on user-generated entries, full manual input, and lack coverage of Asian mixed dishes. (2) Image-based food recognition [17], [18] reduces typing but struggles with occluded ingredients, hidden fats, and volume estimation. (3) General-purpose LLMs understand natural language but are not grounded in authoritative food composition data, exhibiting ~35.8% calorie MAPE [11] and hallucinations [12]. (4) Research dialogue systems [14] predated tool-augmented LLM architectures.", bold_prefix="D. Existing Limitations. ")
add_p("To address these gaps, we propose DietSense, a data-grounded and safety-aware conversational Domain AI Agent. Its novelty lies in three design choices: (1) 'LLM orchestrates, tools compute': LLMs manage dialogue and tool calls while deterministic modules query TFDA, Taiwanese dish cards, and USDA databases [19], [20]; (2) Uncertainty as a first-class output: caloric intervals replace falsely precise numbers, paired with a bounded clarification loop; (3) Rule-based safety layered over personalization: Mifflin-St Jeor BMR/TDEE targets [8] are constrained by a hard 1,200 kcal/day floor and eating-disorder detection. We formulate three evaluation research questions: RQ1 (Accuracy), RQ2 (Burden), and RQ3 (Safety & transparency).", bold_prefix="E. Innovation & Research Questions. ")
add_p("The expected contributions are: (1) A deployable Traditional-Chinese dietary AI agent with an eight-module architecture; (2) A 500-record annotated dataset of Taiwanese meal descriptions; (3) A multi-source nutrition integration pipeline with dish decomposition and provenance tracking; and (4) A multi-dimensional evaluation framework (accuracy, usability, safety). All quantitative metrics are proposal-stage expected outcomes to be experimentally verified.", bold_prefix="F. Expected Contributions. ")

add_h1("II. Related Work")
add_p("DietSense synthesizes advances across AI technologies and Nutrition Domain Knowledge, summarized in the literature matrix below.")

table = doc.add_table(rows=6, cols=6)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Ref", "Year", "Problem", "AI Method", "Domain Knowledge", "Key Findings & Limitations"]
hdr_cells = table.rows[0].cells
for idx, text in enumerate(headers):
    hdr_cells[idx].text = text
    p = hdr_cells[idx].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    format_run(p.runs[0], size_pt=9.5, bold=True, color=COLOR_NAVY)

studies = [
    ("[11]", "2025", "VLM food image calorie estimation", "Multimodal LLMs (GPT-4o, Claude 3.5)", "Portion weight conversion", "Calorie MAPE ~35.8%; systematic underestimation of large portions; image-only limitations"),
    ("[13]", "2025", "Natural meal nutrition benchmarking", "LLMs + CoT + RAG (NutriBench)", "Carb & energy estimation", "Top LLMs rival expert nutritionists in carb estimation; lacks multi-turn clarification loop"),
    ("[15]", "2024", "Personalized nutrition recommendation", "LLM Orchestration + Causal Inference", "Metabolic modeling & guidelines", "92% effectiveness in personalized recommendations; lacks Taiwanese food grounding"),
    ("[7]", "2020", "Commercial app nutrition accuracy", "Database lookup & cleaning (MyFitnessPal)", "Nubel reference composition", "High calorie correlation (r=0.96) after cleaning; pure manual entry causes high user burden"),
    ("[14]", "2017", "Spoken dietary dialogue parsing", "Conditional Random Fields (CRF) + SLU", "USDA Food Database", "Speech parsing cut entry time; legacy pipeline lacking generative reasoning & intervals")
]

for row_idx, data in enumerate(studies):
    row_cells = table.rows[row_idx + 1].cells
    for col_idx, cell_value in enumerate(data):
        row_cells[col_idx].text = cell_value
        p = row_cells[col_idx].paragraphs[0]
        format_run(p.runs[0], size_pt=9, bold=False, color=COLOR_BLACK)

add_h1("III. Deep Research: Domain Principles & Controversies")
add_h2("1. Five Core Mindsets")
add_p("Energy Balance: Thermodynamic foundation (Hall et al. 2011) dictating caloric intake vs expenditure.", bold_prefix="* ")
add_p("Macronutrient Composition: AMDR guidelines (IOM 2005) balancing 45-65% carbs, 10-35% protein, 20-35% fat.", bold_prefix="* ")
add_p("Portion Uncertainty: Poslusna et al. (2009) documented 18-54% self-report error; system models intervals.", bold_prefix="* ")
add_p("Individual Variation: Zeevi et al. (2015) metabolic diversity; personalizing via Mifflin-St Jeor TDEE models.", bold_prefix="* ")
add_p("Behavioral Context: Burke et al. (2025) SMARTER trial; proactive feedback mitigates adherence decay.", bold_prefix="* ")

add_h2("2. Three Critical Domain Controversies")
add_p("Calorie Quantity vs Food Quality: Energy deficit drives weight loss (Gardner 2018), while food quality affects satiety and metabolic health (Hall 2019). DietSense adopts energy as the primary constraint while tagging ultra-processed foods.", bold_prefix="* T1: ")
add_p("AI Estimation vs Hardware Measurement: Pure LLM/VLM estimation carries ~36% MAPE (Fridolfsson 2025). DietSense prioritizes zero-hardware accessibility, compensating with intervals and targeted clarification.", bold_prefix="* T2: ")
add_p("Universal Guidelines vs Precision Nutrition: Dietary guidelines set safe baselines, while individual metabolic tuning optimizes results. DietSense layers personalization above universal safety thresholds.", bold_prefix="* T3: ")

add_h1("IV. Proposed Scheme: System Architecture & Specification")
add_p("DietSense is structured into eight integrated modules compliant with project specifications:")
modules = [
    ("(1) User / Application Scenario", "Accepts colloquial Traditional Chinese text or voice descriptions of everyday meals."),
    ("(2) Query / Input Processing", "Normalizes text (OpenCC), performs intent classification, and executes structured Food NER."),
    ("(3) Planner & Reasoning Agent", "Coordinates execution via whitelisted function calls; enforces response guards against hallucination."),
    ("(4) Data Retrieval", "Queries hierarchical data: Taiwan Food Nutrient DB (TFDA), Taiwanese dish cards, and USDA FDC."),
    ("(5) Analytics Engine", "Deterministically computes calories (portion * kcal/100g), macronutrients, and Mifflin-St Jeor TDEE."),
    ("(6) Domain Knowledge Integration", "Maintains local container weight tables, AMDR standards, and safety constraint rules."),
    ("(7) Decision / Recommendation", "Calculates daily calorie gaps, suggests healthier local substitutes, and performs safety screening."),
    ("(8) Output & Interaction", "Generates structured Markdown with visual macronutrient charts, intervals, and data provenance.")
]
for title, desc in modules:
    add_p(f"{title}: {desc}")

add_h2("Core Algorithm (Pseudocode)")
algo_text = (
    "Algorithm 1: DietSense Agentic Execution Loop\n"
    "Input : User Query Q, Profile P, Daily Log D\n"
    "Output: Response R, Updated Log D'\n"
    "01: q <- normalize_input(Q)\n"
    "02: intent <- classify_intent(q)\n"
    "03: if intent == 'log_food':\n"
    "04:     items <- extract_food_entities(q)\n"
    "05:     for each food in items:\n"
    "06:         candidates <- query_hierarchical_db(food.name)\n"
    "07:         match, confidence <- rank_candidates(candidates, food.context)\n"
    "08:         k <- 0\n"
    "09:         while confidence < 0.80 and k < 2:\n"
    "10:             food <- ask_clarification(food, top_question(food))\n"
    "11:             k <- k + 1\n"
    "12:         grams <- lookup_portion_table(food.portion)\n"
    "13:         low, pt, high <- compute_interval(grams * match.kcal_100 / 100, confidence)\n"
    "14:         D.add_entry(food, grams, low, pt, high, match.source)\n"
    "15: elif intent in ['analyze', 'recommend']:\n"
    "16:     tdee <- calculate_mifflin_tdee(P)\n"
    "17:     summary <- summarize_daily_intake(D, tdee)\n"
    "18: safety_flag <- evaluate_safety_rules(D, P, q)\n"
    "19: if safety_flag == 'DANGER':\n"
    "20:     return format_referral_response(safety_flag), D\n"
    "21: R <- render_response(D, summary, sources=D.sources, intervals=True)\n"
    "22: assert verify_numbers_against_tools(R) == True  # Response Guard\n"
    "23: return R, D\n"
)
p_algo = doc.add_paragraph()
p_algo.paragraph_format.line_spacing = 1.0
p_algo.paragraph_format.space_before = Pt(4)
p_algo.paragraph_format.space_after = Pt(10)
r_algo = p_algo.add_run(algo_text)
format_run(r_algo, font_name="Courier New", size_pt=9, bold=False, color=COLOR_BLACK)

add_h1("V. Planned Evaluation & Expected Outcomes")
add_p("To avoid fabricated claims during proposal stage, all quantitative targets represent planned evaluation metrics:")
add_p("Benchmark Dataset: 500 annotated Taiwanese meal descriptions covering street foods, bento, noodles, and beverages.", bold_prefix="* ")
add_p("Baselines: MyFitnessPal manual entry workflow and pure ungrounded LLM prompting.", bold_prefix="* ")
add_p("Evaluation Metrics: Energy MAE/MAPE, hit rates within +-10% and +-20%, macro accuracy, and safety interception rate.", bold_prefix="* ")
add_p("User Study: 20 participants over 7 consecutive days measuring entry speed, dropout rates, and SUS usability.", bold_prefix="* ")
add_p("Target Outcomes: >85% accuracy within +-20% tolerance, ~60% reduction in logging time, and SUS score >70.", bold_prefix="* ")

add_h1("VI. References")
ref_list = [
    "[1] World Health Organization (WHO), 'Obesity and overweight fact sheet,' Mar. 2024.",
    "[2] Health Promotion Administration (Taiwan), 'Nutrition and Health Survey in Taiwan (NAHSIT) 2017-2020,' 2021.",
    "[3] L. E. Burke et al., 'Adherence to self-monitoring in mobile health weight-loss interventions: Findings from the SMARTER randomized clinical trial,' Obesity, vol. 33, 2025.",
    "[4] P. J. Teixeira et al., 'Self-monitoring in behavioral weight loss: A meta-analysis,' Obesity Reviews, vol. 26, no. 1, p. e13450, 2025.",
    "[5] K. D. Hall et al., 'Quantification of the effect of energy imbalance on bodyweight,' The Lancet, vol. 378, no. 9793, pp. 826-837, 2011.",
    "[6] K. Poslusna et al., 'Misreporting of energy and micronutrient intake estimated by food records and 24 hour recalls,' British Journal of Nutrition, vol. 101, no. S2, pp. S73-S85, 2009.",
    "[7] C. Evenepoel et al., 'Validation of the consumer-focused app MyFitnessPal against a reference food composition database,' JMIR, vol. 22, no. 6, p. e18118, 2020.",
    "[8] M. D. Mifflin, S. T. St Jeor et al., 'A new predictive equation for resting energy expenditure in healthy individuals,' AJCN, vol. 51, no. 2, pp. 241-247, 1990.",
    "[9] Institute of Medicine (IOM), Dietary Reference Intakes for Energy, Carbohydrate, Fiber, Fat, Protein, Washington, DC: The National Academies Press, 2005.",
    "[10] D. Zeevi et al., 'Personalized nutrition by prediction of glycemic responses,' Cell, vol. 163, no. 5, pp. 1079-1094, 2015.",
    "[11] E. Fridolfsson et al., 'Performance Evaluation of 3 Large Language Models for Nutritional Content Estimation from Food Images,' Curr. Dev. Nutr., vol. 9, p. 104523, 2025.",
    "[12] J. Belkhouribchia and J. J. Pen, 'Large language models in clinical nutrition: an overview of its applications, capabilities, limitations, and potential future prospects,' Front. Nutr., vol. 12, p. 1635682, 2025.",
    "[13] A. Hua, M. P. Dhaliwal et al., 'NutriBench: Assessing large language models on nutritional estimation from meal descriptions,' in Proc. ICLR, 2025.",
    "[14] M. Korpusik and J. R. Glass, 'Spoken language understanding for a nutrition dialogue system,' IEEE/ACM Trans. Audio, Speech, Lang. Process., vol. 25, no. 7, pp. 1450-1461, 2017.",
    "[15] Z. Yang et al., 'ChatDiet: An LLM-augmented framework for personalized nutrition recommendation,' Smart Health, vol. 31, p. 100445, 2024.",
    "[16] Y. Cheng et al., 'Can LLMs accurately estimate food calories from text descriptions?,' in Proc. NeurIPS Workshop AI Health, 2024.",
    "[17] L. Bossard, M. Guillaumin, and L. Van Gool, 'Food-101 - Mining discriminative components with random forests,' in Proc. ECCV, 2014.",
    "[18] G. Chocry et al., 'Nutrition5k: Parallel ultra-dense camera arrays for food nutrient estimation,' in Proc. CVPR, 2021.",
    "[19] Taiwan Food and Drug Administration (TFDA), 'Taiwan Food Composition Database,' Ministry of Health and Welfare, Taiwan, 2023.",
    "[20] U.S. Department of Agriculture (USDA), 'FoodData Central,' Agricultural Research Service, 2023."
]

for ref in ref_list:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.space_after = Pt(2.5)
    p_ref.paragraph_format.line_spacing = 1.05
    r_ref = p_ref.add_run(ref)
    format_run(r_ref, size_pt=9.5, color=COLOR_BLACK)

out_dir = r"C:\Users\譚人傑\.gemini\antigravity\scratch\2026-11-11-DIC3-ProjectRefactor\delivery"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "DietSense_Proposal_Report.docx")
doc.save(out_path)
print("SUCCESS: File generated at " + out_path)