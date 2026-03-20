from dataclasses import dataclass
import re
from typing import List


@dataclass
class SectionChunk:
    heading: str
    body: str


class WikiEditorAPI:
    def build_outline_prompt(self, topic: str, target_sections: int = 8) -> str:
        return (
            f"Create a long-form article outline for topic '{topic}'. "
            f"Include {target_sections} top-level sections, each with 3 bullet points. "
            "Output as a Markdown list."
        )

    def split_by_h2(self, markdown_text: str) -> List[SectionChunk]:
        pattern = re.compile(r"^##\s+(.+)$", re.MULTILINE)
        matches = list(pattern.finditer(markdown_text))
        if not matches:
            return [SectionChunk(heading="Main", body=markdown_text.strip())]
        chunks: List[SectionChunk] = []
        for index, match in enumerate(matches):
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown_text)
            heading = match.group(1).strip()
            body = markdown_text[start:end].strip()
            chunks.append(SectionChunk(heading=heading, body=body))
        return chunks

    def merge_sections(self, topic: str, chunks: List[SectionChunk]) -> str:
        lines = [f"# {topic}", ""]
        for chunk in chunks:
            lines.append(f"## {chunk.heading}")
            lines.append("")
            lines.append(chunk.body.strip())
            lines.append("")
        return "\n".join(lines).strip() + "\n"

    def validate_internal_links(self, markdown_text: str) -> List[str]:
        refs = re.findall(r"\[\[([^\]]+)\]\]", markdown_text)
        invalid = [ref for ref in refs if "|" in ref and ref.count("|") > 1]
        return invalid
