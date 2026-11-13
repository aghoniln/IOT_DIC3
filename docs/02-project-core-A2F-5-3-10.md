# 02. DietSense 專案定錨：A–F 摘要 × 5 核心 × 3 取捨 × 10 細節

> 任務 2：make clear of your project — A to F (abstract), 5 cores, 3 trade-offs, 10 details
> 對應期末規範：Abstract（A–F）＋ Deep Research（Q1 五個核心思維 / Q2 三個專業爭論 / Q3 十個深度問題）

## 0. 一句話定位

**DietSense = 讓使用者用一句中文記錄飲食的 Domain AI Agent；LLM 只負責「聽懂、追問、調度」，
所有熱量數字由可稽核的資料庫與公式產生，並以「區間＋來源＋安全守門」輸出。**

> LLM orchestrates, deterministic domain tools compute.

四大產品亮點（2026-11-11 對話確認）：C1 自然語言輸入、C2 主動式智慧互動、C3 情境感知、C4 大數據驅動。

---

## 1. Abstract A–F（精簡定稿）

| 段 | 重點 | 證據 / 內容 |
|---|---|---|
| **A. Attention** | 肥胖是需長期管理的慢性病 | WHO fact sheet：全球 26 億成人（45%）過重，其中 9.4 億（16%）肥胖；臺灣成人過重及肥胖盛行率 50.3%（國健署 2017–2020 NAHSIT） |
| **B. But** | 三個瓶頸 | ① 手動記錄負擔高，自我監測遵循率隨時間非線性下降（SMARTER, Burke et al. 2025）② 自報攝取低報 18–54%（Poslusna 2009）③ 通用 LLM 估熱量 MAPE ≈ 35.8%、大份量系統性低估（Fridolfsson 2025） |
| **C. Cure** | 對話式、資料錨定、安全導向 Domain AI Agent | LLM 只協調；白名單 Function Calling 呼叫營養 DB、RAG、TDEE 引擎、不確定性模組、安全規則庫 |
| **D. Development** | 八模組 ①–⑧ | Whisper → 意圖分類 → Planner → USDA FDC / 臺灣食品成分 DB / 臺式料理向量庫 → E = g × kcal₁₀₀/100、Mifflin-St Jeor → 規則庫 → 建議 → 區間輸出；Clarification Loop |
| **E. Experiments** | 資料集 + Baseline + 指標 + User study | 500 筆臺式料理標註；對照 MyFitnessPal 與「純 LLM」；MAE、±10%/±20% 達標率、涵蓋率、記錄秒數、安全攔截率；20 人 × 7 天、SUS |
| **F. Findings** | **Expected Outcomes**（不得虛構） | ±20% 內 >85%、記錄時間 −60%、SUS >70、來源揭露率 100%、危險輸入攔截率 100% |

---

## 2. 五個核心（Q1：5 Core Mindsets）

| # | 核心思維 | 意義 | 證據 | → 系統設計落點 |
|---|---|---|---|---|
| 1 | **能量平衡** Energy Balance | 攝取 − 消耗 = 能量儲存變化；動態而非 3,500 kcal = 1 lb 靜態法則 | Hall et al., *Lancet* 2011 | ⑤ TDEE 引擎；⑦「今日剩餘 kcal」與趨勢，而非單餐評判 |
| 2 | **巨量營養素組成** Macronutrient Composition | 熱量相同、組成不同 → 飽足、體組成不同 | IOM AMDR：醣 45–65%、蛋白 10–35%、脂 20–35%；Atwater 4/4/9/7 | ⑤ 巨量營養素比例；⑧ 圓餅圖；⑥ AMDR 檢查 |
| 3 | **份量估算與不確定性** Portion & Uncertainty | 份量是最大誤差源；應誠實表達不確定 | 自報低報 18–54%（Poslusna 2009）；LLM 影像 MAPE ~36%（Fridolfsson 2025） | ⑤ 區間 [low, point, high]；③ 信心 < 0.8 觸發追問；⑥ 臺灣容器份量表 |
| 4 | **個體差異** Individual Variation | 同食物、不同人反應不同；公式有適用族群 | Zeevi et al., *Cell* 2015；Frankenfield 2005（Mifflin-St Jeor 約 70–80% 個體誤差在 ±10% 內） | ① 個人檔案；⑤ 公式選擇 + 標示限制；⑦ 以實際體重趨勢校正 TDEE |
| 5 | **行為情境** Behavioral Context | 飲食受時間、情緒、社交、外食環境影響 | 自我監測 + 回饋可減緩遵循率下降（SMARTER） | ③ 情境記憶（時間、餐別、場合）；⑦ 主動提醒；⑥ 暴食-節食模式偵測 |

---

## 3. 三個取捨（Q2：3 Controversies / Trade-offs）

### T1. 熱量「數量」 vs. 食物「品質」
- **A**：A calorie is a calorie — 等熱量控制飲食減重差異小（DIETFITS, Gardner et al., *JAMA* 2018：低脂 vs 低醣 12 個月無顯著差異）。
- **B**：品質更重要 — 超加工飲食使自由攝取量每日多約 500 kcal（Hall et al., *Cell Metab* 2019）。
- **共識**：熱量赤字是減重必要條件；品質決定可持續性與健康結果。
- **未解**：最佳巨量營養素比例的個體化；超加工食品的機制。
- **DietSense 取捨**：主指標仍為熱量（可量測、可驗證），輔以 AMDR 與「加工程度標記」作為次要提示，不做品質評分排名。

### T2. AI 純文字/影像估算 vs. 硬體輔助（秤、3D）
- **A**：LLM 已可用於日常 — NutriBench（Hua et al., ICLR 2025）顯示 GPT-4o + CoT 估醣接近營養師且更快。
- **B**：誤差不可接受 — 影像 MAPE ~36% 且大份量低估（Fridolfsson 2025）；臨床需秤重。
- **共識**：AI 適合「趨勢追蹤」，臨床精準需硬體或專業人員。
- **DietSense 取捨**：選擇**零硬體的日常可用性**，代價以「區間輸出 + 追問 + 來源揭露」補償；不宣稱臨床精準。

### T3. 通用指引 vs. 高度個人化
- **A**：DRI／國民飲食指南安全、可推廣、責任清楚。
- **B**：精準營養（Zeevi 2015）個人化建議優於通用。
- **共識**：通用指引為安全基線，個人化為優化層，兩者不互斥。
- **未解**：AI 個人化建議是否構成醫療行為、隱私。
- **DietSense 取捨**：**分層設計** — 預設通用指引；資料越完整才開啟個人化；任何建議不得低於安全底線（<1,200 kcal 警示）；高風險族群轉介。

> 第 4 個工程取捨（貫穿全系統）：**準確度 vs. 互動負擔** — 問越多越準但越煩 → 以「最多 2 輪追問 + 預設份量 + 區間」平衡，指標：每筆追問次數 vs. ±20% 達標率。

---

## 4. 十個細節（Q3：10 Deep Questions + 參考答案要點）

| # | 類型 | 問題 | 參考答案要點（口試用） |
|---|---|---|---|
| 1 | Why | 為什麼相同熱量攝取，一人瘦一人不瘦？ | BMR/NEAT 差異、自報誤差、水分波動；Agent 以 7–14 天體重趨勢反推實際 TDEE，而非只信公式 |
| 2 | What-if | 使用者只說「吃了一碗泡麵」？ | 先給預設品牌/份量區間（寬）；只追問影響最大的變數（是否加蛋、湯喝多少）；最多 2 輪 |
| 3 | Trade-off | 追問越多越準但越煩，平衡點？ | 以「資訊增益 / 預期 kcal 區間縮減」排序問題；KPI：追問次數、區間寬度、放棄率 |
| 4 | Failure Case | 資料庫沒有的「奶奶眷村炒年糕」？ | 優雅降級：拆解成食材（年糕、肉絲、油）→ 用相似菜 RAG → 寬區間 + 低信心標記 + 邀請使用者確認；絕不讓 LLM 編數字 |
| 5 | Evidence | AI 記錄比飲食日記有效的證據？如何設計 RCT？ | 自我監測與減重正相關（Burke 2011；Patel 2021）；RCT：DietSense vs MyFitnessPal，12 週，主要結果：遵循天數比例，次要：體重變化 |
| 6 | Comparison | RAG-LLM vs Fine-tuned LLM vs KG + 規則？ | RAG：資料可更新、可溯源；Fine-tune：數值仍會幻覺、更新成本高；KG/規則：精確但覆蓋低 → 本案採「RAG 查找 + 規則/公式計算」混合 |
| 7 | Design Decision | 為何對話式而非傳統 UI？何時對話反而較差？ | 複合菜、外食描述時對話勝；重複固定餐、精確秤重時「一鍵常用餐」較快 → 提供常用餐快捷 |
| 8 | Real-world | 夜市食物 USDA 不存在或失準？ | 臺灣食品成分資料庫優先；自建臺式料理卡（來源、日期、份量重量、驗證者）；每筆附 provenance；季度抽查 |
| 9 | Why | Harris-Benedict / Mifflin-St Jeor / Katch-McArdle 何時失準？ | Mifflin 對一般成人最準；肥胖/高齡/運動員偏差較大；Katch 需體脂率；孕婦不適用 → 顯示公式與限制，並轉介 |
| 10 | What-if | 建議助長飲食失調（長期 <1,200 kcal）？ | 規則層硬性攔截；偵測極端節食語句、暴食-節食循環；拒絕再給限制建議，改提供專業資源；不讓 LLM 自行判斷 |

---

## 5. 一頁追溯矩陣（核心 → 模組 → 可驗證指標）

| 核心 / 取捨 | 模組 | OpenSpec capability | 指標 |
|---|---|---|---|
| 能量平衡 | ⑤⑦ | `energy-analytics` | TDEE 計算單元測試 100% 通過 |
| 巨量營養素 | ⑤⑧ | `energy-analytics` | 巨量營養素 MAE |
| 份量 / 不確定性 | ③⑤ | `uncertainty-clarification` | ±20% 達標率、區間覆蓋率、追問次數 |
| 個體差異 | ①⑤ | `energy-analytics` | 公式限制揭露率 |
| 行為情境 | ③⑦ | `agent-orchestration` | 提醒接受率、7 天留存 |
| T1 數量 vs 品質 | ⑥⑦ | `recommendation-output` | AMDR 提示正確率 |
| T2 AI vs 硬體 | ⑤⑧ | `uncertainty-clarification` | 區間寬度 vs 誤差 |
| T3 通用 vs 個人化 | ⑥⑦ | `safety-guardrails` | 安全攔截率 100% |
