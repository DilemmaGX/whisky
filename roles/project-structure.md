# Multi-file Management Plan

## Directory Layers
- `.github/workflows/`: automation triggers and deployment flows
- `whisky/`: core code (CLI, agents, pipeline, security config)
- `templates/wiki/`: reusable article templates
- `roles/`: detailed role responsibilities and review policies
- `wiki/`: generated wiki entry output directory

## Boundary Constraints
- The pipeline writes only to `wiki/`; it does not mutate role docs or templates.
- Templates provide structure only and never contain credentials.
- Agent logic and model integration stay encapsulated in `whisky/`.

## Security Constraints
- API keys can only come from environment variables or the root `API_KEY` file.
- `API_KEY` is ignored by Git through `.gitignore`.
- Logs must sanitize secrets and never print full keys in local or CI output.

## Review and Merge Flow
- Automated writing happens on PR branches only.
- The main branch updates only through human-reviewed merges.
- Failed generation does not create PRs, reducing noisy branches.
