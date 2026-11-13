## ADDED Requirements

### Requirement: Rule-based safety evaluation
Safety decisions SHALL be made by a deterministic rule engine (versioned YAML rules), not by the LLM, and SHALL return `OK`, `WARNING`, or `DANGER` with the triggering rule ID.

#### Scenario: Rule traceability
- **WHEN** a warning is produced
- **THEN** the response log SHALL contain the rule ID that triggered it

### Requirement: Minimum energy floor
The system SHALL issue a warning when completed-day intake or a requested target is below 1,200 kcal/day, and MUST NOT generate recommendations that lead below this floor. Partial-day totals SHALL NOT trigger the floor rule.

#### Scenario: User requests 900 kcal plan
- **WHEN** the user asks for a 900 kcal/day diet
- **THEN** the system SHALL refuse the plan, explain the risk, and suggest professional support

#### Scenario: After breakfast only
- **WHEN** only breakfast (400 kcal) has been logged at 09:00
- **THEN** the floor rule SHALL NOT fire

### Requirement: Disordered-eating signal detection
The system SHALL detect extreme-restriction language, compensatory behaviors, and binge–restrict cycles over the past 7 days, and on detection SHALL stop restrictive advice and provide support resources.

#### Scenario: Compensatory behavior mention
- **WHEN** the user says「吃太多了，我要催吐」
- **THEN** the result SHALL be `DANGER` and the response SHALL contain only supportive text and professional resources

### Requirement: High-risk population routing
For profiles indicating pregnancy, age under 18, chronic kidney disease, diabetes medication, or an eating-disorder history, the system SHALL NOT provide deficit targets and SHALL recommend consulting a professional.

#### Scenario: Pregnant user
- **WHEN** the profile indicates pregnancy
- **THEN** no calorie-deficit recommendation SHALL be shown

### Requirement: Non-medical disclaimer
Every recommendation response SHALL include a brief statement that DietSense does not provide medical diagnosis or treatment.

#### Scenario: Recommendation shown
- **WHEN** a recommendation is rendered
- **THEN** the disclaimer SHALL be present

