from pathlib import Path


def _write_section_index(wiki_root: Path, section_folder: str, section_title: str) -> None:
    section_path = wiki_root / section_folder
    section_path.mkdir(parents=True, exist_ok=True)
    pages = sorted(path for path in section_path.glob("*.md") if path.name != "index.md")
    lines = [
        "---",
        f"title: {section_title}",
        "tags:",
        "  - wiki",
        f"  - {section_folder}",
        "status: stable",
        "---",
        "",
        f"# {section_title}",
        "",
    ]
    if pages:
        for page in pages:
            title = page.stem.replace("-", " ").title()
            rel = page.relative_to(wiki_root).as_posix()
            lines.append(f"- [[wiki/{rel[:-3]}|{title}]]")
    else:
        lines.append("- Needs more sources")
    lines.append("")
    (section_path / "index.md").write_text("\n".join(lines), encoding="utf-8")


def rebuild_all_indexes(wiki_root: Path) -> None:
    _write_section_index(wiki_root, "concepts", "Concepts")
    _write_section_index(wiki_root, "technologies", "Technologies")
    _write_section_index(wiki_root, "biographies", "Biographies")
    _write_section_index(wiki_root, "entries", "General Entries")

    lines = [
        "---",
        "title: Wiki Index",
        "tags:",
        "  - wiki",
        "  - index",
        "status: stable",
        "---",
        "",
        "# Wiki Index",
        "",
        "## Navigation",
        "- [[wiki/concepts/index|Concepts]]",
        "- [[wiki/technologies/index|Technologies]]",
        "- [[wiki/biographies/index|Biographies]]",
        "- [[wiki/entries/index|General Entries]]",
        "",
        "## Start Reading",
    ]

    starter_paths = [
        wiki_root / "concepts",
        wiki_root / "technologies",
        wiki_root / "biographies",
        wiki_root / "entries",
    ]
    for folder in starter_paths:
        for page in sorted(path for path in folder.glob("*.md") if path.name != "index.md")[:3]:
            title = page.stem.replace("-", " ").title()
            rel = page.relative_to(wiki_root).as_posix()
            lines.append(f"- [[wiki/{rel[:-3]}|{title}]]")
    lines.append("")
    (wiki_root / "index.md").write_text("\n".join(lines), encoding="utf-8")
