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

## Agent roles

- Orchestrator: routing and workflow control
- Issue Classifier: request detection and topic extraction
- Wiki Writer: draft generation
- Content Reviewer: factual and structural checks
- Format Reviewer: Obsidian Markdown checks

See the `roles/` directory for full role behavior and review contracts.
