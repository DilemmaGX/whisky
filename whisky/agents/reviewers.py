import json

from ..deepseek_client import DeepSeekClient
from ..models import ReviewResult


def _extract_json(raw: str) -> dict:
    text = raw.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise RuntimeError("Reviewer output is not valid JSON")
    return json.loads(text[start : end + 1])


class ContentReviewerAgent:
    def __init__(self, client: DeepSeekClient):
        self.client = client

    def run(self, topic: str, markdown_text: str) -> ReviewResult:
        system_prompt = (
            "You are a content reviewer. Check whether the wiki draft matches the topic, has complete structure, and keeps a neutral tone. "
            'Return JSON: {"passed": boolean, "feedback": string}'
        )
        user_prompt = f"Topic: {topic}\n\nDraft:\n{markdown_text}"
        data = _extract_json(self.client.chat(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0))
        return ReviewResult(passed=bool(data.get("passed", False)), feedback=str(data.get("feedback", "")))


class FormatReviewerAgent:
    def __init__(self, client: DeepSeekClient):
        self.client = client

    def run(self, topic: str, markdown_text: str) -> ReviewResult:
        system_prompt = (
            "You are a format reviewer. Check Obsidian Markdown format, heading hierarchy, internal links, and frontmatter conventions. "
            'Return JSON: {"passed": boolean, "feedback": string}'
        )
        user_prompt = f"Topic: {topic}\n\nDraft:\n{markdown_text}"
        data = _extract_json(self.client.chat(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0))
        return ReviewResult(passed=bool(data.get("passed", False)), feedback=str(data.get("feedback", "")))
