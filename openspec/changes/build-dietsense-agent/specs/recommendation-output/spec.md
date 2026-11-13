## ADDED Requirements

### Requirement: Daily summary and gap analysis
On `analyze` intent the system SHALL return today's intake interval, macro distribution, TDEE, goal target, and remaining/exceeded energy.

#### Scenario: Evening check
- **WHEN** the user asks「今天吃得怎樣？」
- **THEN** the response SHALL include intake interval, remaining budget, and AMDR flags

### Requirement: Substitution recommendations
On `recommend` intent the system SHALL propose substitutions drawn from the food knowledge base (not invented by the LLM), each with its energy difference and source, and SHALL pass all suggestions through the safety rule engine.

#### Scenario: Lower-energy alternative
- **WHEN** the user asks for a lighter alternative to「炸雞排」
- **THEN** each suggestion SHALL show its kcal interval, the difference versus the original, and its data source

### Requirement: Visualization
The system SHALL provide a macronutrient pie chart for the day and a 7-day energy trend chart with interval bands.

#### Scenario: Trend request
- **WHEN** the user has at least 3 logged days and asks for a trend
- **THEN** a line chart with low/high bands SHALL be returned

### Requirement: Source disclosure
Every response containing nutrition numbers SHALL include a compact source list for the items involved.

#### Scenario: Logged meal response
- **WHEN** a meal is logged
- **THEN** the response SHALL list the sources (e.g., TFDA DB, dish card ID, USDA FDC ID)

