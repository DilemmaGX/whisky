import json

from ..deepseek_client import DeepSeekClient
from ..models import ClassificationResult, IssueContext


class IssueClassifierAgent:
    def __init__(self, client: DeepSeekClient):
        self.client = client

    def run(self, issue: IssueContext) -> ClassificationResult:
        system_prompt = (
            "You are an issue classifier. Determine whether the issue requests creating or updating a wiki entry. "
            "Return strict JSON only in this format: "
            '{"is_wiki_request": boolean, "topic": string, "reason": string}'
        )
        user_prompt = f"Title:\n{issue.title}\n\nBody:\n{issue.body}\n\nLabels: {', '.join(issue.labels)}"
        raw = self.client.chat(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0)
        data = _extract_json(raw)
        return ClassificationResult(
            is_wiki_request=bool(data.get("is_wiki_request", False)),
            topic=str(data.get("topic", "")).strip() or issue.title.strip(),
            reason=str(data.get("reason", "")).strip(),
        )


def _extract_json(raw: str) -> dict:
    text = raw.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise RuntimeError("Classifier output is not valid JSON")
    return json.loads(text[start : end + 1])
