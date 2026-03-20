# whisky

`whisky` is a multi-agent automation project that converts GitHub Issues into Obsidian-style wiki drafts, opens a Pull Request for human review, and then publishes approved content through GitHub Pages.

Repository: `github.com/DilemmaGX/whisky`

## What this project does

- Classifies whether an Issue is a wiki-entry request
- Generates a structured wiki draft with a writer agent
- Runs content and format review agents
- Revises once when review feedback fails
- Writes output to `wiki/*.md`
- Opens a review PR automatically from GitHub Actions

## Repository structure

- `.github/workflows/deploy-pages.yml`: deploy wiki site to GitHub Pages
- `.github/workflows/issue-to-wiki-pr.yml`: issue-triggered wiki generation + PR
- `.github/workflows/ci.yml`: compile and CLI smoke tests
- `.github/workflows/issue-triage.yml`: issue labeling and triage automation
- `.github/workflows/pr-labeler.yml`: PR labels based on changed files
- `whisky/`: CLI, agents, pipeline, DeepSeek integration
- `roles/`: detailed role specifications
- `templates/wiki/`: article templates
- `wiki/`: generated entries

## Security model

- API keys are loaded from:
  - `DEEPSEEK_API_KEY` environment variable, or
  - root `API_KEY` file (no extension)
- `API_KEY` is ignored by Git in `.gitignore`
- Logs sanitize credentials and never print full keys

## Quick start (local)

1. Create `API_KEY` in repository root with your DeepSeek key.
2. Run:

```bash
python -m whisky.cli assist outline --topic "Open Source" --sections 8
```

3. Create a local issue payload file (for example `issue.local.json`) and run:

```bash
python -m whisky.cli run --repo-root . --issue-json issue.local.json
```

4. Generated output appears in `wiki/`.

## GitHub setup

1. Add repository secret:
   - `DEEPSEEK_API_KEY`
2. Ensure GitHub Actions are enabled.
3. For site publishing, set **Settings -> Pages -> Build and deployment -> Source** to **GitHub Actions**.

## Issue interaction guide

This project is issue-driven. A well-structured issue gives better drafts and fewer review rounds.

### 1) Choose the right issue template

- **Wiki Entry Request**: use this for new or updated wiki pages.
- **Bug Report**: use this for pipeline/CLI/workflow problems.
- Blank issues are disabled to keep automation stable.

### 2) Recommended wiki request format

When opening **Wiki Entry Request**, provide:

- **Topic**: one clear title (for example: `Open Source`)
- **Entry type**: `concept`, `technology`, `biography`, or `general`
- **Scope and required sections**: must-have sections and exclusions
- **Source hints**: official docs, standards, reports, or trusted references

### 3) Label and triage behavior

- `issue-triage.yml` automatically applies `needs-triage`.
- Wiki-like issues are additionally labeled `wiki-entry`.
- `issue-to-wiki-pr.yml` runs on:
  - manual dispatch, or
  - `labeled` when the label is `wiki-entry`, or
  - `reopened` when `wiki-entry` already exists.
- This reduces duplicate runs from frequent issue edits.

### 3.1) Duplicate run prevention

- Both issue workflows use per-issue concurrency groups.
- Newer runs cancel older in-progress runs for the same issue.
- Editing issue text no longer triggers extra generation runs.

### 3.2) PR creation permissions

If `generate-wiki-pr` fails with:
`GitHub Actions is not permitted to create or approve pull requests`

Use one of these fixes:

1. Enable repository setting:
   - **Settings -> Actions -> General -> Workflow permissions**
   - Enable **Allow GitHub Actions to create and approve pull requests**
2. Or set a token secret named `WHISKY_PR_TOKEN` with repository write access.

The workflow automatically uses `WHISKY_PR_TOKEN` when present, otherwise falls back to `GITHUB_TOKEN`.

### 4) End-to-end issue lifecycle

1. You open a **Wiki Entry Request** issue.
2. Triage workflow adds labels.
3. Multi-agent pipeline classifies and drafts content.
4. A PR is created on an `auto/wiki-<issue_number>` branch.
5. Humans review factual quality and formatting.
6. After merge, `deploy-pages.yml` publishes to GitHub Pages.

### 5) How to improve draft quality

- Put hard constraints in the issue body (required sections, style limits, banned claims).
- Add links for high-risk factual areas.
- Explicitly list "out of scope" items to avoid over-generation.
- If the first draft is weak, update the same issue with concrete revision points.

### 6) Local issue simulation

You can test issue interaction locally before creating a real issue:

```bash
python -m whisky.cli run --repo-root . --issue-json issue.local.json
```

Minimal `issue.local.json` shape:

```json
{
  "number": 123,
  "title": "Wiki entry request: Open Source",
  "body": "Include definition, license families, governance, and limitations.",
  "labels": ["wiki-entry", "documentation"],
  "url": "https://github.com/DilemmaGX/whisky/issues/123"
}
```

## Agent roles

- Orchestrator: routing and workflow control
- Issue Classifier: request detection and topic extraction
- Wiki Writer: draft generation
- Content Reviewer: factual and structural checks
- Format Reviewer: Obsidian Markdown checks

See the `roles/` directory for full role behavior and review contracts.
