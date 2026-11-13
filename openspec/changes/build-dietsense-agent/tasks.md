# Tasks

## 1. 專案骨架與資料基礎（①④⑥）

- [ ] 1.1 [①–⑧] 建立 `app/`（八模組子套件 m1_scenario … m8_output）、`data/`、`eval/`、`tests/`，`pytest` 可執行空測試並通過
- [ ] 1.2 [④] 下載 TFDA 食品營養成分資料庫並轉成 SQLite，記錄版本；驗證：`python data/build_tfda.py` 後查詢「白飯」回傳 kcal/100g
- [ ] 1.3 [④] 申請 USDA FDC API key，實作 `usda_client.search()`；驗證：整合測試查詢 "egg" 回傳 FDC ID
- [ ] 1.4 [⑥] 建立臺灣份量參照表 `data/portion_table.yaml`（碗/大碗/便當/杯/片，含 P10–P90 範圍）；驗證：schema 測試通過
- [ ] 1.5 [④⑥] 建立前 100 張臺式料理卡（成分 g、來源、驗證者）；驗證：`python data/validate_cards.py` 無缺欄位

## 2. 分析引擎（⑤）

- [ ] 2.1 [⑤] 實作 `compute_energy`、複合菜加總與 `consumed_fraction`；驗證：單元測試含 200 g × 150 kcal = 300 kcal 與「湯喝一半」案例
- [ ] 2.2 [⑤] 實作 `compute_macros` 與 AMDR 檢查；驗證：脂肪 42% 案例被標記
- [ ] 2.3 [⑤] 實作 `bmr_mifflin` 與 `tdee`，含不適用族群判斷；驗證：70 kg/175 cm/30 歲男、1.55 → 1648.75 / 2555.6
- [ ] 2.4 [⑤] 實作區間傳遞 `interval()` 與日總和；驗證：單元測試 lo ≤ pt ≤ hi 且總和逐項相加

## 3. 檢索（④）

- [ ] 3.1 [④] 實作料理卡向量索引（Chroma）+ 別名表雙路召回；驗證：「蚵煎」能召回「蚵仔煎」卡
- [ ] 3.2 [④] 實作 `lookup_food` 優先序與排序、`source`/`source_id` 回傳；驗證：蚵仔煎時料理卡排序高於 USDA
- [ ] 3.3 [④] 實作無匹配時的成分拆解降級並標記低信心；驗證：「眷村炒年糕」測試回傳 components 與 low-confidence 旗標

## 4. 輸入理解（②）

- [ ] 4.1 [②] OpenCC 繁簡正規化與（選用）Whisper 轉寫；驗證：簡體輸入轉繁體的單元測試
- [ ] 4.2 [②] 意圖分類（LLM + few-shot），5 類；驗證：50 則標註語句準確率報告
- [ ] 4.3 [②] 食物實體抽取（JSON schema：name/portion/cooking/add_ons/consumed_fraction/meal_type）；驗證：「牛肉麵加蛋湯喝一半」案例通過，缺值標 `unknown`

## 5. Planner 與追問（③⑤）

- [ ] 5.1 [③] 實作工具白名單 function calling 與對話狀態；驗證：非白名單工具呼叫被拒絕並記錄的測試
- [ ] 5.2 [③] 實作 Response Guard（營養數字 ⊆ 工具輸出）；驗證：注入「550 kcal」幻覺的測試被攔截
- [ ] 5.3 [③⑤] 實作信心分數（權重與門檻可設定）；驗證：「一點炒飯」信心 < 0.80
- [ ] 5.4 [③] 實作 Clarification Loop（最大縮減問題優先、≤ 2 輪、拒答降級）；驗證：兩次「不知道」後以寬區間記錄的測試

## 6. 安全守門（⑥⑦）

- [ ] 6.1 [⑥] 建立 `data/safety_rules.yaml`（rule ID、版本）與規則引擎；驗證：每條規則至少一個單元測試
- [ ] 6.2 [⑥] 實作 1,200 kcal 底線（僅全日/目標判定）；驗證：900 kcal 計畫被拒、早餐後不誤報
- [ ] 6.3 [⑥] 實作飲食失調訊號（關鍵詞 + 分類器 + 7 日暴食-節食模式）；驗證：「我要催吐」→ DANGER
- [ ] 6.4 [⑥⑦] 高風險族群轉介與免責聲明；驗證：孕婦檔案不顯示赤字建議
- [ ] 6.5 [⑥] 建立 ≥ 50 則紅隊測試集；驗證：攔截率與誤報率報告

## 7. 建議與輸出（⑦⑧）

- [ ] 7.1 [⑦] 每日摘要與缺口分析；驗證：1,400/2,000 kcal → 剩 600 kcal 並附區間
- [ ] 7.2 [⑦] 替代建議（取自知識庫、經安全規則過濾）；驗證：雞排替代建議皆附 kcal 差與來源
- [ ] 7.3 [⑧] 區間格式、來源清單、圓餅圖與 7 日趨勢（含上下帶）；驗證：快照測試
- [ ] 7.4 [①⑧] Streamlit 對話 UI 串接 FastAPI；驗證：README 的 Demo 步驟可完整操作一次

## 8. 評估（Expected Outcomes 驗證）

- [ ] 8.1 [④] 建立 500 筆臺式料理評估集（雙人標註、來源）；驗證：`eval/validate_dataset.py` 報告各類別數量
- [ ] 8.2 [③] 實作純 LLM baseline 與手動輸入 baseline 腳本；驗證：同一輸入產生兩組結果
- [ ] 8.3 [⑤] 評估熱量準確度：MAE、MAPE、±10%/±20% 達標率（目標 ±20% > 85%）；驗證：`eval/run.py` 報告
- [ ] 8.4 [⑤] 評估巨量營養素 MAE 與區間覆蓋率；驗證：報告含兩指標
- [ ] 8.5 [④] 評估資料庫涵蓋率與來源揭露率（目標 100%）；驗證：報告含兩指標
- [ ] 8.6 [③] 評估平均追問輪數；驗證：報告含指標
- [ ] 8.7 [⑥] 評估安全攔截率（目標 100%）與誤報率；驗證：紅隊報告
- [ ] 8.8 [①⑧] 20 人 × 7 天使用者研究：記錄時間（目標 −60%）、中斷率、主觀負擔、SUS（目標 > 70）；驗證：同意書、腳本、SUS 問卷入庫並產出統計

## 9. 整合與交接

- [ ] 9.1 端到端整合測試：牛肉麵案例從輸入到含來源區間的回應；驗證：E2E 測試通過
- [ ] 9.2 同步 `DESIGN.md` Results/Limitations 與 `README.md`（Installation/How to Run/Demo）；驗證：新成員依 README 可在乾淨環境跑起來

## Workflow follow-up

- `openspec validate build-dietsense-agent --strict` 通過後提交審閱。
- 實作完成後執行 `/openspec-archive-change`，將 specs 合併至 `openspec/specs/`。

