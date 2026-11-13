## ADDED Requirements

### Requirement: Prioritized multi-source lookup
The system SHALL look up foods in priority order: Taiwan FDA Food Nutrient Database, then curated Taiwanese dish cards (vector retrieval), then USDA FoodData Central. Each candidate SHALL include `kcal_per_100g`, protein, fat, carbohydrate, `source`, `source_id`, and a match score.

#### Scenario: Local dish available
- **WHEN** the food is「蚵仔煎」and a curated dish card exists
- **THEN** the dish card SHALL be ranked above any USDA candidate

#### Scenario: No match in any source
- **WHEN** no candidate exceeds the minimum match score
- **THEN** the system SHALL decompose the dish into components via retrieval of similar dishes and flag the item as low confidence, and SHALL NOT let the LLM supply values

### Requirement: Composite dish decomposition
Dish cards SHALL describe composite dishes as components with gram weights per standard portion, so that energy is the sum of component energies and add-ons or partial consumption can be applied per component.

#### Scenario: Half soup consumed
- **WHEN** a beef noodle soup is logged with soup `consumed_fraction` 0.5
- **THEN** only the soup component SHALL be scaled by 0.5

### Requirement: Portion reference table
The system SHALL convert household portion terms (碗、大碗、小碗、便當、杯、份、片) to grams using a versioned Taiwan portion reference table.

#### Scenario: Container term
- **WHEN** the portion is「一碗白飯」
- **THEN** `portion_grams` SHALL return the table value and its plausible range

### Requirement: Provenance
Every logged item SHALL store its data source, source identifier, and database version so results are auditable.

#### Scenario: User asks for source
- **WHEN** the user asks「這數字哪來的？」
- **THEN** the system SHALL list the source name and identifier for each item

