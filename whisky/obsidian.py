import re
from pathlib import Path


def slugify_title(value: str) -> str:
    cleaned = re.sub(r"[^\w\s\-]", "", value).strip().lower()
    cleaned = re.sub(r"\s+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned)
    return cleaned or "untitled-entry"


def build_wiki_path(wiki_root: Path, topic: str) -> Path:
    return wiki_root / f"{slugify_title(topic)}.md"


def ensure_obsidian_frontmatter(content: str, topic: str) -> str:
    if content.startswith("---"):
        return content
    header = "\n".join(
        [
            "---",
            f"title: {topic}",
            "tags:",
            "  - wiki",
            "  - auto-generated",
            "---",
            "",
        ]
    )
    return header + content.lstrip()
