## ADDED Requirements

### Requirement: Deterministic energy computation
The system SHALL compute item energy as `portion_g × kcal_per_100g / 100` and composite energy as the sum of component energies, using deterministic code with no LLM involvement.

#### Scenario: Simple item
- **WHEN** portion is 200 g and density is 150 kcal/100 g
- **THEN** energy SHALL equal 300 kcal

### Requirement: Macronutrient analysis
The system SHALL compute protein, fat, and carbohydrate grams and their energy share, and SHALL compare daily shares against AMDR (carbohydrate 45–65%, protein 10–35%, fat 20–35%).

#### Scenario: Fat above AMDR
- **WHEN** fat contributes 42% of daily energy
- **THEN** the analysis SHALL flag fat as above the AMDR range

### Requirement: BMR and TDEE estimation
The system SHALL estimate BMR with the Mifflin-St Jeor equation and TDEE as BMR × activity factor (1.2–1.9), and SHALL display the formula used and its known limitations.

#### Scenario: Male profile
- **WHEN** profile is male, 70 kg, 175 cm, 30 years, activity 1.55
- **THEN** BMR SHALL be 1648.75 kcal and TDEE SHALL be 2555.6 kcal (±0.1)

#### Scenario: Formula not applicable
- **WHEN** the profile indicates pregnancy or age under 18
- **THEN** the system SHALL NOT present a TDEE target and SHALL refer to a professional

### Requirement: Daily energy balance
The system SHALL report daily intake interval, TDEE, goal target, and remaining or exceeded energy.

#### Scenario: Remaining budget
- **WHEN** intake point estimate is 1,400 kcal and goal target is 2,000 kcal
- **THEN** the system SHALL report 600 kcal remaining together with the intake interval

