import json
from pathlib import Path
from typing import Any

from .models import IssueContext


def issue_from_event(event_path: Path) -> IssueContext:
    payload = json.loads(event_path.read_text(encoding="utf-8"))
    issue = payload.get("issue", {})
    labels = [item.get("name", "") for item in issue.get("labels", [])]
    return IssueContext(
        number=int(issue.get("number", 0)),
        title=str(issue.get("title", "")),
        body=str(issue.get("body", "")),
        labels=[name for name in labels if name],
        url=str(issue.get("html_url", "")),
    )


def issue_from_json(raw: str) -> IssueContext:
    payload: Any = json.loads(raw)
    labels = payload.get("labels", [])
    normalized_labels = [str(item) for item in labels]
    return IssueContext(
        number=int(payload.get("number", 0)),
        title=str(payload.get("title", "")),
        body=str(payload.get("body", "")),
        labels=normalized_labels,
        url=str(payload.get("url", "")),
    )
