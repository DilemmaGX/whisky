# Task Planner Role Specification

## Mission
Transform a single issue into an executable task graph that can include one or many wiki entries.

## Inputs
- Issue title, body, labels
- Optional structured task JSON block
- Existing repository constraints and output conventions

## Outputs
- A normalized plan with one or many entry tasks
- Operation per task: `create`, `update`, or `remake`
- Entry type per task: `auto`, `concept`, `technology`, `biography`, or `general`
- Research subtasks for evidence collection

## Decision Strategy
- Prefer structured JSON tasks if provided
- Fill missing fields with safe defaults
- Use `auto` entry type when the issue does not clearly enforce a category
- Split broad requests into independent entry tasks
- Preserve dependency order for related entries

## Validation Rules
- Every task must include a non-empty topic
- Operation must be one of `create`, `update`, `remake`
- Entry type must be one of `auto`, `concept`, `technology`, `biography`, `general`
- Research tasks must include at least a query if present
