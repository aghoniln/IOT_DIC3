# 01. OpenSpec 安裝與規格驅動開發（Spec-Driven Development）

> 任務 1：install openspec and be familiar with spec-driven development

## 1.1 安裝紀錄（本機已完成）

| 項目 | 指令 / 結果 |
|---|---|
| Node.js | 可攜版安裝於 `%USERPROFILE%\tools\node`（已加入使用者 PATH），`node -v` → v26.x |
| OpenSpec CLI | `npm install -g @fission-ai/openspec@latest` → `openspec --version` = **2.0.0** |
| 專案初始化 | `openspec init --tools antigravity .` → 產生 `openspec/` 與 `.agents/skills/openspec-*` |
| 建立變更 | `openspec new change build-dietsense-agent` |
| 驗證 | `openspec validate build-dietsense-agent --strict` |

> [!NOTE]
> Windows PowerShell 預設禁止執行 `.ps1`，請改用 `openspec.cmd ...`，或執行
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`。
> 關閉匿名統計：`openspec config set telemetry.enabled false`。

## 1.2 什麼是 SDD？

傳統「Vibe coding」：想法 → 直接叫 AI 寫程式 → 結果與需求漂移、無法驗證。
**SDD**：先把「系統必須做什麼」寫成**可驗證的規格（spec）**，人與 AI 對規格達成共識後才實作；
規格是唯一真相來源（source of truth），程式碼只是規格的實現。

```
Idea ─▶ proposal.md (Why/What) ─▶ specs/*.md (SHALL + Scenario)
     ─▶ design.md (How / Trade-off) ─▶ tasks.md (checklist)
     ─▶ /openspec-apply (實作) ─▶ validate ─▶ /openspec-archive (合併回 openspec/specs)
```

## 1.3 OpenSpec 目錄結構（本 repo）

```
openspec/
├── config.yaml                 ← 專案共通約束（語言、核心原則、安全底線）
├── specs/                      ← 「目前系統」的正式規格（archive 後才會出現）
└── changes/
    └── build-dietsense-agent/  ← 一次「變更提案」
        ├── proposal.md         ← Why / What Changes / Capabilities / Impact
        ├── design.md           ← Context / Goals / Decisions / Risks
        ├── specs/<capability>/spec.md   ← Delta：ADDED/MODIFIED/REMOVED Requirements
        └── tasks.md            ← - [ ] 1.1 ... 可追蹤實作清單
```

## 1.4 規格寫法（Delta Spec）

```markdown
## ADDED Requirements

### Requirement: Deterministic energy computation
The system SHALL compute energy as portion_g × kcal_per_100g / 100 using a deterministic tool.

#### Scenario: LLM proposes a number
- **WHEN** the LLM draft contains a kcal value not returned by a tool
- **THEN** the response guard SHALL replace it with the tool value or reject the draft
```

規則：每條 Requirement 必須含 **SHALL/MUST**，且至少一個 `#### Scenario:`（WHEN/THEN）。
這正好對應期末規範「能用客觀證據驗證」——每個 Scenario 都可以變成一個測試案例。

## 1.5 Antigravity 中的工作流程（slash skills）

| 指令 | 用途 |
|---|---|
| `/openspec-explore` | 先討論、釐清需求（不寫檔） |
| `/openspec-propose "..."` | 一次產生 proposal / specs / design / tasks |
| `/openspec-update-change` | 修改既有變更 |
| `/openspec-apply-change` | 依 tasks.md 逐項實作並打勾 |
| `/openspec-sync-specs` | 把 delta 同步到 `openspec/specs/` |
| `/openspec-archive-change` | 完成後封存 |

## 1.6 為何 SDD 適合 DietSense

1. **安全需求可被強制**：「LLM 不得產生熱量數字」寫成 SHALL，測試即可驗證。
2. **對應評分**：proposal ↔ Introduction、design ↔ Proposed Scheme、tasks ↔ 實作計畫、Scenario ↔ Experiments。
3. **Final Handover**：規範要求「原開發者不在，下一位仍能理解並繼續」——`openspec/specs` 就是活的需求文件。

