---
title: Home
tags:
  - home
  - whisky
status: stable
---

# Home

whisky is built to turn issue-driven knowledge requests into maintainable, reviewable, and reference-safe wiki pages for Obsidian and GitHub Pages.

## Why this project exists

- Documentation requests often arrive in fragmented issue threads.
- Teams need a consistent way to transform those requests into structured wiki pages.
- Generated content must stay review-friendly, link-rich, and reference-valid over time.

## What whisky automates

1. Accepts one issue with one or many entry tasks
2. Plans a task graph with operation mode (`create`, `update`, `remake`)
3. Collects and validates references
4. Generates and reviews pages
5. Updates wiki indexes and cross-page navigation
6. Opens a pull request for human approval

## Contributing

1. Open a `Wiki Entry Request` or `Bug Report` issue.
2. For multi-page work, include a structured task JSON block.
3. Add reference policy constraints if your domain requires stricter sources.
4. Review generated pull requests for factual correctness and style consistency.
5. Improve templates and role specs when recurring quality gaps are identified.

## Start exploring

- [[wiki/index|Wiki Index]]
- [[wiki/concepts/index|Concepts]]
- [[wiki/technologies/index|Technologies]]

## Local development

Run a local test server:

```bash
python -m whisky.cli dev serve --repo-root .
```
