## ADDED Requirements

### Requirement: Whitelisted tool invocation
The Planner LLM SHALL obtain nutritional data, calculations, and safety decisions only by calling tools from a fixed whitelist (`lookup_food`, `portion_grams`, `compute_energy`, `compute_macros`, `bmr_tdee`, `summarize_day`, `safety_check`, `recommend`). Calls to any other tool name SHALL be rejected and logged.

#### Scenario: Non-whitelisted tool
- **WHEN** the LLM emits a call to a tool not in the whitelist
- **THEN** the orchestrator SHALL refuse the call, log it, and re-prompt the LLM

### Requirement: Response Guard against fabricated numbers
The system MUST NOT present any energy or nutrient value that was not produced by a tool in the current turn or retrieved from the user's log. Every numeric nutrition value in the final response SHALL be traceable to a tool output.

#### Scenario: LLM invents a calorie value
- **WHEN** the drafted response contains「約 550 kcal」but no tool returned 550
- **THEN** the guard SHALL replace the value with the tool output or block the draft and regenerate

### Requirement: Conversation memory and state
The system SHALL keep per-user conversation state, including pending clarification questions, today's log, and profile, so that follow-up answers update the correct food item.

#### Scenario: Answer to a clarification
- **WHEN** the agent asked「大碗還是小碗？」and the user replies「大碗」
- **THEN** the system SHALL update the pending noodle item's portion and SHALL NOT create a new entry

