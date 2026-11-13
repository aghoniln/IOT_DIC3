## ADDED Requirements

### Requirement: Confidence scoring
The system SHALL compute a confidence score in [0, 1] for each food item from match quality, portion specificity, and source quality, with weights and the threshold (default 0.80) stored as configuration.

#### Scenario: Vague description
- **WHEN** the user says「吃了一點炒飯」
- **THEN** the confidence SHALL be below the threshold because portion specificity is low

### Requirement: Clarification loop
When an item's confidence is below the threshold, the system SHALL ask the single question expected to reduce the energy interval the most, and SHALL ask at most 2 clarification rounds per item before logging with a wide interval.

#### Scenario: Highest-impact question first
- **WHEN** a noodle soup has unknown bowl size and unknown soup consumption
- **THEN** the first question SHALL target the variable with the larger expected kcal impact

#### Scenario: User declines to answer
- **WHEN** the user replies「不知道」twice
- **THEN** the system SHALL log the item using default portion, a widened interval, and a low-confidence label

### Requirement: Interval output
The system SHALL store and display each item and daily total as `[low, point, high]` kcal and SHALL NOT display a single number without its interval.

#### Scenario: Display format
- **WHEN** an item is logged
- **THEN** the response SHALL show a form such as「約 650 kcal（範圍 560–780）」

