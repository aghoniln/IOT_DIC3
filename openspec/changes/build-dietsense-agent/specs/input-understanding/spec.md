## ADDED Requirements

### Requirement: Natural-language meal input
The system SHALL accept free-form Traditional Chinese or English text describing meals, and MAY accept audio that is transcribed to text before processing. Simplified Chinese input SHALL be normalized to Traditional Chinese.

#### Scenario: Text meal description
- **WHEN** the user sends「我剛吃了一碗加蛋台式牛肉麵，湯喝一半」
- **THEN** the system SHALL pass the normalized text to intent classification without requiring any form fields

#### Scenario: Audio input
- **WHEN** the user uploads a voice message
- **THEN** the system SHALL transcribe it and show the transcript to the user before logging

### Requirement: Intent classification
The system SHALL classify each message into exactly one of `log_food`, `query_nutrition`, `analyze`, `recommend`, or `other`.

#### Scenario: Analysis request
- **WHEN** the user asks「我今天還能吃多少？」
- **THEN** the intent SHALL be `analyze`

#### Scenario: Out-of-domain message
- **WHEN** the message is unrelated to diet or weight management
- **THEN** the intent SHALL be `other` and no food entry SHALL be created

### Requirement: Structured food entity extraction
For `log_food` messages the system SHALL extract a list of food items, each with `name`, `portion_desc`, `cooking_method`, `add_ons`, `consumed_fraction`, and `meal_type`, validated against a JSON schema. Missing fields SHALL be marked `unknown` rather than guessed.

#### Scenario: Partial consumption and add-ons
- **WHEN** the user says「牛肉麵加蛋，湯喝一半」
- **THEN** the extraction SHALL contain the noodle dish with add-on「滷蛋」and soup `consumed_fraction` 0.5

#### Scenario: Unspecified portion
- **WHEN** the user says「吃了雞排」without a size
- **THEN** `portion_desc` SHALL be `unknown`

