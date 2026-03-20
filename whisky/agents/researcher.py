import json

from ..deepseek_client import DeepSeekClient
from ..models import EntryTask, ResearchItem, ResearchPacket


def _extract_json(raw: str) -> dict:
    text = raw.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise RuntimeError("Research collector output is not valid JSON")
    return json.loads(text[start : end + 1])


class ResearchCollectorAgent:
    def __init__(self, client: DeepSeekClient):
        self.client = client

    def run(self, task: EntryTask) -> ResearchPacket:
        system_prompt = (
            "You are a research collector for wiki writing. Return strict JSON only with this format: "
            '{"summary": string, "items": [{"title": string, "url": string, "snippet": string, "relevance": string}]}. '
            "Prefer authoritative and referenceable sources."
        )
        lines = [
            f"Topic: {task.topic}",
            f"Operation: {task.operation}",
            f"Entry type: {task.entry_type}",
            f"Scope: {task.scope}",
            f"Source hints: {', '.join(task.source_hints)}",
            "Research tasks:",
        ]
        if task.research_tasks:
            for rt in task.research_tasks:
                lines.append(f"- Query: {rt.query} | Purpose: {rt.purpose} | Hints: {', '.join(rt.source_hints)}")
        else:
            lines.append("- Query: authoritative definition and key references")
        user_prompt = "\n".join(lines)
        raw = self.client.chat(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.1)
        data = _extract_json(raw)
        items = []
        for item in data.get("items", []):
            title = str(item.get("title", "")).strip()
            url = str(item.get("url", "")).strip()
            if not title or not url:
                continue
            items.append(
                ResearchItem(
                    title=title,
                    url=url,
                    snippet=str(item.get("snippet", "")).strip(),
                    relevance=str(item.get("relevance", "")).strip(),
                )
            )
        summary = str(data.get("summary", "")).strip() or f"Collected research references for {task.topic}."
        return ResearchPacket(topic=task.topic, summary=summary, items=items)
