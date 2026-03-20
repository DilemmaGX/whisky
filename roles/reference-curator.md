# Reference Curator Role Specification

## Mission
Guarantee that generated entries include explicit references suitable for review and future maintenance.

## Responsibilities
- Check that every major claim is anchored by at least one source category
- Ensure markdown links are valid and human-readable
- Remove low-quality or irrelevant sources from final reference list

## Output Contract
- Preserve a dedicated `## References` section
- Use markdown list format: `- [Title](URL) — relevance`
- Keep references focused and non-redundant

## Failure Conditions
- Missing references for factual sections
- Broken or malformed URLs
- References unrelated to page topic
