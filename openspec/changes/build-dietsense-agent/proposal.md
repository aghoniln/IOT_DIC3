## Why

飲食自我監測是體重管理的核心行為，但傳統 App 的手動搜尋、秤重與複合菜拆解讓遵循率隨時間下降；而直接詢問通用 LLM 又會產生無來源、可能錯誤的熱量數字。DietSense 要把「一句中文描述」轉成**有來源、有區間、有安全守門**的飲食紀錄與建議，並符合期末專題「Domain AI Agent，而非單純 Chatbot」的要求。

## What Changes

- 新增繁體中文自然語言（文字，選用語音）飲食輸入與結構化抽取（模組 ①②）。
- 新增 LLM Planner：只負責意圖理解、追問與工具調度；所有數值必須來自白名單工具（模組 ③）。
- 新增多來源營養檢索：臺灣食品成分資料庫 → 自建臺式料理卡 → USDA FoodData Central，並附資料來源（模組 ④⑥）。
- 新增確定性分析引擎：熱量、巨量營養素、Mifflin-St Jeor BMR/TDEE（模組 ⑤）。
- 新增不確定性量化與 Clarification Loop：信心 < 0.80 追問、最多 2 輪、以區間輸出（模組 ③⑤）。
- 新增規則式安全守門：< 1,200 kcal/日、極端節食、飲食失調與高風險族群轉介（模組 ⑥⑦）。
- 新增每日摘要、TDEE 缺口、替代建議、圖表與來源揭露輸出（模組 ⑦⑧）。
- 新增 500 筆臺式料理標註評估集與可重現評估流程。

## Capabilities

### New Capabilities

- `input-understanding`：自然語言/語音飲食輸入、正規化、意圖分類與食物實體抽取。〔核心 3 份量；核心 5 行為情境〕
- `agent-orchestration`：LLM Planner、工具白名單、對話記憶與 Response Guard（禁止 LLM 自創數值）。〔取捨 T2 AI vs 硬體〕
- `nutrition-retrieval`：多來源營養資料查詢、臺式料理卡、份量標準表與來源追溯。〔核心 2 巨量營養素；核心 3 份量〕
- `energy-analytics`：熱量、巨量營養素、BMR/TDEE 與每日能量平衡計算。〔核心 1 能量平衡；核心 4 個體差異〕
- `uncertainty-clarification`：信心分數、熱量區間與主動追問迴圈。〔核心 3 份量與不確定性；取捨 T2〕
- `safety-guardrails`：安全熱量底線、飲食失調訊號偵測、高風險族群轉介與免責聲明。〔取捨 T3 通用 vs 個人化〕
- `recommendation-output`：每日摘要、缺口分析、替代建議、視覺化與來源揭露。〔取捨 T1 數量 vs 品質；核心 5〕
- `evaluation-benchmark`：臺式料理標註資料集、Baseline 與評估指標計算。〔所有 Expected Outcomes〕

### Modified Capabilities

（無，本專案為新建系統）

## Out of Scope

- 食物影像辨識與 3D 份量估算（列為 Future Work）。
- 臨床診斷、處方飲食、醫療營養治療。
- 微量營養素完整評估、穿戴裝置自動同步。
- 原生行動 App（MVP 以 Web chat 呈現）。

## Impact

- 新程式碼：`app/`（FastAPI 服務、八模組）、`data/`（料理卡、份量表、規則 YAML）、`eval/`（資料集與評估腳本）、`tests/`。
- 外部依賴：LLM API（OpenAI 或 Gemini function calling）、USDA FDC API key、Whisper（選用）、向量資料庫（Chroma/pgvector）。
- 文件：`DESIGN.md`、`README.md` 需隨實作同步更新。
- 隱私：使用者身體資料與飲食日誌需本地儲存、可刪除、去識別化。

