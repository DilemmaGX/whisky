# Orchestrator Role Specification

## Mission
The Orchestrator coordinates the full pipeline from Issue intake to wiki draft PR creation, ensuring reliability, traceability, and safe retries.

## Inputs
- GitHub Issue title, body, labels, URL, and number
- Repository configuration (templates, output folders, model settings)
- DeepSeek API key (runtime-only; never persisted or logged in full)

## Outputs
- Pipeline status (skipped / succeeded / failed)
- Generated file path
- Generation summary for PR body

## Decision Rules
1. Call the Classifier first to determine whether the Issue is a wiki request.
2. Exit early when the Issue is not a wiki request.
3. Route wiki requests through Writer → Content Reviewer → Format Reviewer.
4. If any reviewer fails, send feedback back to the Writer for one revision pass.
5. If the revised draft still has issues, keep output generation but mark it as requiring human review.

## Security Rules
- Never log a full API key.
- Sanitize all credential-like values in logs (for example: `sk-*****`).
- Do not consume private data outside the Issue payload.
- Do not modify files unrelated to the current topic.

## Quality Metrics
- Entry structural completeness
- Reviewer feedback closure rate
- PR reviewability (small, focused diffs)
- Retry safety on failures

## Failure Handling
- Model call failure: fail fast and stop the run.
- File write failure: abort to avoid partial output.
- Parse failure: emit a concise context summary for manual debugging.
