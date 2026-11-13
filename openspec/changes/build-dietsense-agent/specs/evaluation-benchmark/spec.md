## ADDED Requirements

### Requirement: Annotated Taiwanese meal dataset
The project SHALL maintain a dataset of at least 500 natural-language Taiwanese meal descriptions covering night-market snacks, lunchboxes, noodle soups, mixed dishes, beverages, and home dishes, each with reference energy and macros, reference source, and annotator IDs.

#### Scenario: Dataset validation
- **WHEN** the dataset validation script runs
- **THEN** it SHALL report category counts and fail if any record lacks reference energy or source

### Requirement: Baselines
The evaluation SHALL compare DietSense against (a) a pure-LLM baseline that answers calories directly without tools and (b) a manual-entry baseline modeled on MyFitnessPal workflow.

#### Scenario: Pure-LLM baseline run
- **WHEN** the evaluation runs on the test split
- **THEN** results for DietSense and the pure-LLM baseline SHALL be produced on identical inputs

### Requirement: Evaluation metrics
The evaluation SHALL compute energy MAE and MAPE, percentage within ±10% and ±20%, macro MAE, interval coverage rate, database coverage rate, average clarification turns, source-disclosure rate, and safety interception rate on a red-team prompt set.

#### Scenario: Metric report
- **WHEN** `eval/run.py` completes
- **THEN** a report SHALL list every metric above, labeled as measured results with date and model version

### Requirement: User study protocol
The project SHALL define a 7-day within-subject study with 20 participants comparing logging time, dropout, perceived burden, and SUS between DietSense and manual entry, with informed consent.

#### Scenario: Protocol ready
- **WHEN** the user study begins
- **THEN** consent form, task script, and SUS questionnaire SHALL exist in the repository

