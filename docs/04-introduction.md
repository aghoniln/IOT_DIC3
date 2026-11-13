# 04. Introduction（Refactor）

> 任務 4：Introduction refactor｜依期末規範 Introduction A–F：Attention → Background → Problem → Existing Limitations → Innovation → Contributions
> 格式：IEEE Transactions 風格英文正文（與 IEEE Abstract 一致），引用編號見 [references.md](references.md)。

## 改寫重點（vs. 期中版）

| 期中版問題 | 本版處理 |
|---|---|
| 引用數據多處無法查證（如「WHO 2025 全球 10 億肥胖」、「85% 用戶 30 天放棄」、「MyFitnessPal 錯誤率 ~30%」、「市場 68 億美元」） | 全部改為可查證來源：WHO 26 億/9.4 億、NAHSIT 50.3%、SMARTER、Poslusna、Fridolfsson、Evenepoel |
| 只寫「做了什麼」，未說明「為何 LLM 不能直接用」 | 加入 LLM 幻覺與 MAPE 證據，導出「LLM 協調、工具計算」設計原則 |
| Innovation 與 Contributions 重疊 | Innovation = 與既有系統差異（3 點）；Contributions = 可交付產出（4 點） |
| 無研究問題 | 新增 RQ1–RQ3，直接對應 Experiments |
| 缺章節導覽 | 新增 Paper Organization |

---

## I. INTRODUCTION

**A. Attention Getter.** Overweight and obesity have become chronic, population-scale health problems. According to the World Health Organization, 2.6 billion adults—45% of the world's adult population—are overweight, and 940 million of them live with obesity [1]. Taiwan mirrors this trend: the 2017–2020 Nutrition and Health Survey in Taiwan reported that 50.3% of adults are overweight or obese [2]. Because obesity requires long-term management rather than one-off treatment, tools that help people sustainably monitor what they eat are of direct public-health value.

**B. Background.** Dietary self-monitoring is one of the most consistently supported behaviors in weight management; systematic reviews associate more frequent self-monitoring with greater weight loss [4], [5]. Smartphone applications have made logging ubiquitous, and recent advances in large language models (LLMs) now allow systems to understand free-form meal descriptions, conduct multi-turn dialogue, and invoke external tools [11]–[13]. These capabilities suggest that dietary logging could shift from form-filling to conversation—particularly valuable in Taiwan, where meals are frequently eaten out and consist of mixed dishes, soups, and night-market foods that are poorly represented in Western food databases.

**C. Problem.** The practical problem is that accurate dietary logging is cognitively expensive. A user who eats "a bowl of Taiwanese beef noodle soup with an egg, drinking half of the soup" must (i) search a database for the correct item, (ii) estimate portion weight without a scale, (iii) decompose the composite dish into components, and (iv) adjust for partial consumption. This burden contributes to declining adherence: in the 12-month SMARTER trial, adherence to dietary self-monitoring declined nonlinearly over time [3]. At the same time, self-reported intake is systematically biased, with energy under-reporting of 18%–54% [6], and portion size, hidden cooking oil, and soups amplify the uncertainty. This project therefore addresses the following question: *How can a system reduce the effort of dietary logging for Taiwanese meals while keeping its nutritional estimates traceable, honest about uncertainty, and safe?*

**D. Existing Limitations.** Current approaches each solve only part of this problem.
1. *Manual tracking applications* (e.g., MyFitnessPal) achieve reasonable energy correlation once data are cleaned [7], but rely on user-generated entries and full manual input, and offer limited coverage of local mixed dishes.
2. *Image-based food recognition* [17]–[19], [31] reduces typing but struggles with occluded ingredients, hidden fats, and volume estimation, and typically provides no reasoning or personalization.
3. *General-purpose LLMs* understand natural language but are not grounded in authoritative food composition data. Multimodal LLMs estimating nutrition from food images showed an energy MAPE of about 35.8% with systematic underestimation of larger portions [8], and LLMs in clinical nutrition raise concerns about hallucinated values and unverified advice [9], [10].
4. *Research dialogue systems* for nutrition [14] demonstrated spoken meal logging but predate tool-using LLM agents, and recent LLM nutrition work [15], [16] focuses on estimation benchmarks or recommendation rather than an end-to-end, safety-gated logging agent for local cuisine.

**E. Innovation.** To address these gaps, we propose **DietSense**, a data-grounded and safety-aware conversational Domain AI Agent. Its novelty lies in three design choices:
1. **"LLM orchestrates, tools compute."** The LLM is restricted to intent understanding, clarification, and tool coordination through whitelisted function calls; every energy and nutrient value must originate from deterministic modules querying the Taiwan Food Nutrient Database, curated Taiwanese dish cards, and USDA FoodData Central [28], [29], and a response guard rejects any number not produced by a tool.
2. **Uncertainty as a first-class output.** Instead of a falsely precise single number, DietSense propagates portion and source uncertainty into a calorie interval with a confidence score, and triggers a bounded clarification loop that asks the single question expected to narrow the interval most.
3. **Rule-based safety layered over personalization.** Personalized targets (Mifflin–St Jeor BMR and TDEE [23]) operate above a deterministic safety floor: energy targets below 1,200 kcal/day, disordered-eating signals, and high-risk populations are intercepted by versioned rules rather than left to LLM judgment.

To evaluate these choices, we pose three research questions:
- **RQ1 (Accuracy):** Does tool-grounded estimation reduce calorie error on Taiwanese meals compared with a pure-LLM baseline?
- **RQ2 (Burden):** Does conversational logging reduce logging time and perceived burden compared with manual entry?
- **RQ3 (Safety & transparency):** Can the system disclose sources for all values and intercept all unsafe requests in a red-team set?

**F. Contributions.** The expected contributions of this project are:
1. **A deployable Traditional-Chinese dietary AI agent** with an eight-module architecture that separates language understanding from nutritional computation and safety decisions.
2. **A 500-record annotated dataset** of Taiwanese meal descriptions (night-market snacks, lunchboxes, noodle soups, mixed dishes, beverages) with reference energy, macronutrients, and sources.
3. **A multi-source nutrition integration pipeline** with dish decomposition, portion reference tables, provenance tracking, and calibrated calorie intervals.
4. **A multi-dimensional evaluation framework** jointly measuring accuracy (MAE, ±10%/±20% hit rate, interval coverage), usability (logging time, SUS), and safety (source-disclosure and interception rates).

All performance figures in this proposal—e.g., more than 85% of estimates within ±20%, a ~60% reduction in logging time, and an SUS above 70—are *expected outcomes* to be verified experimentally, not reported results.

**Paper Organization.** Section II reviews related work in AI technology and nutrition domain knowledge. Section III presents the deep-research analysis of core mindsets, controversies, and design questions. Section IV describes the proposed DietSense architecture, flowchart, and algorithm. Section V details the evaluation plan, and Section VI concludes with limitations and future work.

---

## 中文對照摘要（口頭報告用）

- **A**：全球 26 億成人過重、9.4 億肥胖；臺灣成人過重及肥胖 50.3%。
- **B**：飲食自我監測有效，LLM 讓「用說的記錄」首次可行；臺灣外食與複合菜在西方資料庫覆蓋差。
- **C**：問題＝記錄負擔高（搜尋、秤重、拆解、部分攝取）→ 遵循率下降；自報低報 18–54%。
- **D**：手動 App 負擔高、拍照辨識看不到油與份量、通用 LLM 熱量 MAPE ~36% 會幻覺、舊對話系統無工具化 Agent。
- **E**：三項創新（LLM 協調 / 工具計算、不確定性區間 + 追問、規則安全層）＋ RQ1–RQ3。
- **F**：四項貢獻（Agent、500 筆資料集、整合管線、評估框架）；數字皆為預期成效。

