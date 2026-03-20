from pathlib import Path
from dataclasses import dataclass
import re


@dataclass
class WikiPage:
    title: str
    path: Path
    entry_type: str


def _entry_type_from_path(path: Path, wiki_root: Path) -> str:
    try:
        relative = path.relative_to(wiki_root)
    except ValueError:
        return "general"
    if len(relative.parts) < 2:
        return "general"
    folder = relative.parts[0]
    mapping = {
        "concepts": "concept",
        "technologies": "technology",
        "biographies": "biography",
        "entries": "general",
    }
    return mapping.get(folder, "general")


def _extract_title(markdown_text: str, fallback: str) -> str:
    match = re.search(r"^title:\s*(.+)$", markdown_text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip().strip("\"'")
    match = re.search(r"^#\s+(.+)$", markdown_text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback


def load_wiki_pages(wiki_root: Path) -> list[WikiPage]:
    pages: list[WikiPage] = []
    if not wiki_root.exists():
        return pages
    for md_path in sorted(wiki_root.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        title = _extract_title(text, md_path.stem.replace("-", " ").title())
        entry_type = _entry_type_from_path(md_path, wiki_root)
        pages.append(WikiPage(title=title, path=md_path, entry_type=entry_type))
    return pages


def build_catalog_snapshot(wiki_root: Path, max_items: int = 120) -> str:
    pages = load_wiki_pages(wiki_root)
    if not pages:
        return "No wiki pages exist yet."
    lines = ["Current wiki pages:"]
    for page in pages[:max_items]:
        rel = page.path.relative_to(wiki_root).as_posix()
        lines.append(f"- [{page.entry_type}] {page.title} ({rel})")
    if len(pages) > max_items:
        lines.append(f"- ... {len(pages) - max_items} more pages")
    return "\n".join(lines)


def infer_entry_type_auto(topic: str, snapshot_text: str) -> str:
    lowered = topic.lower()
    if any(key in lowered for key in ["person", "founder", "biography", "author", "ceo"]):
        return "biography"
    if any(key in lowered for key in ["protocol", "framework", "technology", "tool", "platform", "api"]):
        return "technology"
    if any(key in lowered for key in ["concept", "model", "theory", "principle", "license"]):
        return "concept"
    snapshot_lower = snapshot_text.lower()
    if "technologies/" in snapshot_lower and any(key in lowered for key in ["github", "markdown", "spdx"]):
        return "technology"
    if "concepts/" in snapshot_lower and any(key in lowered for key in ["open source", "licensing", "governance"]):
        return "concept"
    return "general"
