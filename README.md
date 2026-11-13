# DietSense: A Conversational Domain AI Agent for Daily Calorie Intake Analysis

> **NCHU DIC3 Final Project Proposal & Spec-Driven Development Refactor**
> Architecture: AI Agent + Nutrition Domain Knowledge + Food Data Analytics + Real-World Health Application

---

## 專案概述 (Project Overview)

**DietSense** 是一套結合自然語言互動、主動式智慧代理、多來源營養資料錨定與安全性守門的個人化飲食健康管理系統。
本專案嚴格遵循**規格驅動開發 (Spec-Driven Development, SDD)** 與課程評分規範，將傳統「使用者配合系統逐項填寫」的被動記錄工具，轉型為「AI Agent 理解日常語言並調度專業工具驗證」的主動式智慧代理人。

核心設計原則：**「LLM 負責理解與協調，確定性領域工具負責計算，專家規則負責安全守門」**。

---

## 五大交付成果索引 (Deliverables Index)

本專案已完成以下五大任務模組與文檔交付：

| 任務編號 | 核心項目 | 主要交付路徑 / 說明 |
|:---:|:---|:---|
| **1** | **OpenSpec SDD 規範與環境建置** | [`docs/01-openspec-sdd-guide.md`](docs/01-openspec-sdd-guide.md)<br>• OpenSpec 2.0.0 安裝與環境設定<br>• SDD 規格驅動開發方法論與 Antigravity 整合技能 |
| **2** | **專案定錨：A-F 摘要 × 5 核心 × 3 取捨 × 10 細節** | [`docs/02-project-core-A2F-5-3-10.md`](docs/02-project-core-A2F-5-3-10.md)<br>• A–F 研究故事定稿<br>• 5 大領域核心思維、3 大專業爭論、10 大深度口試問題解析 |
| **3** | **design.md 轉化為 OpenSpec 規格工作流** | [`DESIGN.md`](DESIGN.md) (根目錄系統架構規格書)<br>[`openspec/changes/build-dietsense-agent/`](openspec/changes/build-dietsense-agent/)<br>• `proposal.md`：變更提案動機與能力劃分<br>• `specs/`：八大模組之嚴謹 Delta Specs (SHALL/Scenario)<br>• `design.md`：架構決策、取捨與風險<br>• `tasks.md`：具備驗證依據的實作檢查清單 |
| **4** | **Introduction 緒論重構** | [`docs/04-introduction.md`](docs/04-introduction.md)<br>• 符合 IEEE Transactions 風格之 A–F 結構重構<br>• 導入最新客觀統計數據與研究問題 (RQ1–RQ3) |
| **5** | **Related Work 相關研究重構** | [`docs/05-related-work.md`](docs/05-related-work.md)<br>• 1/2 AI Technology + 1/2 Nutrition Domain 平衡論述<br>• 5 篇跨 2024–2025 年頂級文獻比較表 (Article Summary Table)<br>• SWOT 分析與 Research Gap 收斂路徑 |
| **附錄** | **可驗證文獻引文庫** | [`docs/references.md`](docs/references.md)<br>• 收錄 20 篇高可信度文獻、官方資料庫與臨床指引完整 DOI/URL |

---

## 系統架構簡覽 (Architecture Overview)

DietSense 由八大核心模組串接而成，所有估算過程透明、可解釋且受控：

```text
[① User Scenario] (文字或語音描述日常飲食)
       │
       ▼
[② Input Processing] (Whisper 轉寫 + 繁簡正規化 + 意圖分類 + Food NER 抽取)
       │
       ▼
[③ Planner & Reasoning Agent] (LLM Core + 白名單 Function Calling + 對話記憶)
       │
       ├─────────────────────────────────┬─────────────────────────────────┐
       ▼                                 ▼                                 ▼
[④ Data Retrieval]              [⑤ Analytics Engine]            [⑥ Domain Knowledge]
• 衛福部食品成分資料庫 (TFDA)      • 熱量密度計算 (portion × kcal)  • 臺灣容器份量表 (碗/份/杯)
• 臺式料理卡向量庫 (Chroma)       • 巨量營養素比例分析             • AMDR 營養比例標準
• 美國農業部 USDA FDC API         • Mifflin-St Jeor TDEE 引擎      • 安全熱量底線 (<1200 kcal)
• 使用者歷史飲食日誌             • 不確定性信賴區間 [lo, pt, hi]  • 飲食失調/高風險轉介規則
       │                                 │                                 │
       └─────────────────────────────────┼─────────────────────────────────┘
                                         ▼
                             [⑦ Decision & Recommendation]
                             • 每日攝取赤字/盈餘缺口分析
                             • 健康替代食材建議 (含熱量差與來源)
                             • 安全守門檢查 (OK / WARNING / DANGER)
                                         │
                                         ▼
                             [⑧ Output & Interaction]
                             • Markdown 結構化輸出 (含資料來源追溯)
                             • 熱量區間可視化展示 (拒絕單一假精確數字)
                             • 巨量營養素分佈圓餅圖與 7 日趨勢
```

---

## 規格驗證狀態 (OpenSpec Validation Status)

本專案之規格與工作流程已通過 OpenSpec 嚴格驗證模式：

```bash
$ openspec validate build-dietsense-agent --strict
Change 'build-dietsense-agent' is valid
Progress: 4/4 artifacts complete
[x] proposal
[x] specs (8 capabilities defined)
[x] design
[x] tasks (32 tracked implementation items)
```

---

## 如何開始開發 (Next Steps)

當進入程式碼實作階段時，請使用 Antigravity 內建的 OpenSpec 技能：
1. **查看待辦事項**：閱讀 [`openspec/changes/build-dietsense-agent/tasks.md`](openspec/changes/build-dietsense-agent/tasks.md)
2. **啟動實作任務**：在對話中呼叫 `/openspec-apply-change`
3. **完成驗證與封存**：完成全部 tasks 後執行 `/openspec-archive-change` 將規格沉澱至 `openspec/specs/`
