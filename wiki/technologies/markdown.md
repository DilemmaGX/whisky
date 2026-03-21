---
title: Markdown
tags:
  - wiki
  - technology
  - documentation
  - markup-language
status: stable
---

# Markdown

## Technology Overview
Markdown is a lightweight markup language created in 2004 by John Gruber, with significant contributions from Aaron Swartz. It is designed to be easy to read and write in its source form and can be converted to structurally valid [[HTML]] and other formats. Its primary goal is to allow writers to focus on content without being distracted by complex tags, making it a foundational tool for technical documentation, note-taking, and web content creation.

## Design Goals
The language was conceived with several key principles:
- **Readability:** The source text should be publishable as-is, without looking like it has been marked up with tags or formatting instructions.
- **Simplicity:** The syntax should be intuitive and easy to remember, minimizing the barrier to entry for writing structured documents.
- **HTML Compatibility:** Markdown is intended as a format for writing for the web. Its syntax corresponds to a subset of HTML tags, and it can include raw HTML where needed for additional control.
- **Portability:** Documents should be renderable by a wide variety of software parsers into consistent, structured output.

## Architecture and Core Mechanisms
Markdown operates on plain text files. A parser reads the text, interprets specific punctuation characters as formatting instructions, and generates an abstract syntax tree, which is then typically rendered to HTML.

### Core Syntax
The original Markdown syntax, as defined by Gruber, includes:
- **Headings:** Created using hash symbols (e.g., `# H1`, `## H2`).
- **Emphasis:** `*italic*` or `_italic_`, `**bold**` or `__bold__`.
- **Lists:** Unordered lists using `-`, `+`, or `*`; ordered lists using numbers.
- **Links:** Inline links `[text](url)` and reference-style links.
- **Images:** Similar to links: `![alt text](image-url)`.
- **Code:** Inline code with backticks (`` `code` ``) and code blocks indented by four spaces or fenced with triple backticks (```).
- **Blockquotes:** Lines prefixed with the `>` character.
- **Horizontal Rules:** Three or more hyphens, asterisks, or underscores.

### Extended Syntax (Flavors)
Due to its popularity, many extensions have been created, leading to various "flavors." Two of the most significant are:
- **CommonMark:** A strongly specified, unambiguous syntax specification for Markdown. It aims to standardize Markdown across different parsers and resolve inconsistencies in the original spec.
- **GitHub Flavored Markdown (GFM):** An extension of CommonMark used on [[GitHub]]. It adds features like tables, task lists, strikethrough (`~~text~~`), autolink literals, and triple-backtick code blocks with syntax highlighting.

## Usage
Markdown has become ubiquitous in software and knowledge management due to its simplicity.
- **Documentation:** It is the *de facto* standard for project `README.md` files, API documentation, and wikis.
- **Static Site Generators:** Many [[Static Site Generator|Static Site Generators]] (e.g., Jekyll, Hugo, Eleventy) use Markdown as the primary content format.
- **Forums and Communication:** Platforms like Reddit, Discord, and many forum software packages use Markdown or a derivative for user posts.
- **Note-Taking and Knowledge Bases:** Tools like Obsidian, Logseq, and Notion use Markdown for storing and linking notes, leveraging its plain-text portability.

## Comparison with Alternatives
- **[[HTML]]:** Markdown is far less verbose and easier to write for common document structures. However, HTML is more expressive for complex layouts, interactive elements, and precise styling. Markdown and HTML are often used together, with Markdown covering the core content.
- **BBCode:** Used primarily in older forum software, BBCode uses tag-based syntax (e.g., `[b]bold[/b]`). Markdown is generally considered more readable and has broader adoption beyond forums.
- **Other [[Lightweight Markup Language|Lightweight Markup Languages]]:**
    - **reStructuredText (reST):** More feature-rich and explicit than Markdown, commonly used for Python documentation (e.g., with Sphinx). It has stricter syntax and more built-in constructs for large documentation projects.
    - **AsciiDoc:** Offers greater semantic depth and output format control than Markdown, suitable for complex books and technical documentation. Its syntax is more verbose but also more powerful.

## Common Questions
- **"Which flavor of Markdown should I use?"** For maximum portability, adhere to the CommonMark specification. For software development, especially on GitHub or GitLab, GitHub Flavored Markdown is the practical standard.
- **"Can I mix HTML with Markdown?"** Yes, most parsers allow raw HTML within a Markdown document, providing an escape hatch for unsupported features.
- **"Is Markdown standardized?"** The original specification was intentionally loose. The CommonMark project is the leading effort to create a formal, interoperable standard, though various implementations still have minor differences.

## Practical Guidance
- Use a consistent style guide and linter (like `markdownlint`) in collaborative projects to maintain uniformity.
- For documentation that may require cross-references, tables of contents, or complex conditional rendering, consider if a more powerful language like AsciiDoc or reStructuredText is more appropriate.
- When publishing on the web, ensure your chosen static site generator or platform supports the specific Markdown extensions you intend to use.

## Compatibility and Versioning
There is no single version number for Markdown itself. Compatibility is defined by the parser implementation. Key reference points are:
- **Original Markdown (2004):** John Gruber's syntax on Daring Fireball.
- **CommonMark:** A community-driven standard (specced at CommonMark.org) aiming for stability and interoperability.
- **GitHub Flavored Markdown (GFM):** A superset of CommonMark, versioned alongside GitHub's platform updates.

When sharing documents, it is best to note if they rely on a specific flavor's extensions.

## Related Entries
- [[HTML]]
- [[Lightweight Markup Language]]
- [[Documentation]]
- [[Static Site Generator]]
- [[GitHub]]

## References

- [Markdown](https://daringfireball.net/projects/markdown/) — Primary source for the history and original specification by the creator.
- [CommonMark Spec](https://spec.commonmark.org/) — Authoritative technical specification for the standardized Markdown variant.
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/) — Authoritative specification for the most widely used extended Markdown variant.
- [Writing on GitHub: Basic formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) — Authoritative, practical guide to the syntax of the most popular implementation.
- [Lightweight markup language - Wikipedia](https://en.wikipedia.org/wiki/Lightweight_markup_language) — Referenceable comparison of Markdown to related technologies in context.
- [AsciiDoc vs Markdown | AsciiDoc Documentation](https://docs.asciidoctor.org/asciidoc/latest/asciidoc-vs-markdown/) — Authoritative, technical comparison from a major alternative's perspective.
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) — Authoritative source for syntax and philosophy of a key comparable language.
- [Markdown Guide](https://www.markdownguide.org/) — Highly referenced, practical guide to standard and extended syntax elements.
- [BBCode - Wikipedia](https://en.wikipedia.org/wiki/BBCode) — Referenceable source for BBCode, a relevant comparative technology.
