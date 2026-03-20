import json

from ..deepseek_client import DeepSeekClient
from ..models import EntryTask, IssueContext, PlanResult, ResearchTask


def _extract_json(raw: str) -> dict:
    text = raw.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise RuntimeError("Planner output is not valid JSON")
    return json.loads(text[start : end + 1])


class TaskPlannerAgent:
    def __init__(self, client: DeepSeekClient):
        self.client = client

    def run(self, issue: IssueContext) -> PlanResult:
        system_prompt = (
            "You are a wiki task planner. Build a flexible execution plan for one or many wiki entries. "
            "Support operation values: create, update, remake. "
            "Use only strict JSON in this format: "
            '{"should_generate": boolean, "global_summary": string, "tasks": ['
            '{"topic": string, "operation": "create|update|remake", "entry_type": "concept|technology|biography|general", '
            '"scope": string, "source_hints": [string], "related_entries": [string], '
            '"research_tasks": [{"query": string, "purpose": string, "source_hints": [string]}]}]}'
        )
        user_prompt = (
            f"Issue title:\n{issue.title}\n\n"
            f"Issue body:\n{issue.body}\n\n"
            f"Issue labels: {', '.join(issue.labels)}\n\n"
            "If a structured task block exists in issue text, preserve it and normalize missing fields."
        )
        raw = self.client.chat(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.1)
        data = _extract_json(raw)
        tasks = []
        for item in data.get("tasks", []):
            research_tasks = []
            for rt in item.get("research_tasks", []):
                query = str(rt.get("query", "")).strip()
                purpose = str(rt.get("purpose", "")).strip()
                if not query:
                    continue
                research_tasks.append(
                    ResearchTask(
                        query=query,
                        purpose=purpose or "Collect evidence for factual writing",
                        source_hints=[str(x).strip() for x in rt.get("source_hints", []) if str(x).strip()],
                    )
                )
            topic = str(item.get("topic", "")).strip()
            if not topic:
                continue
            operation = str(item.get("operation", "create")).strip().lower()
            if operation not in {"create", "update", "remake"}:
                operation = "create"
            entry_type = str(item.get("entry_type", "general")).strip().lower()
            if entry_type not in {"concept", "technology", "biography", "general"}:
                entry_type = "general"
            tasks.append(
                EntryTask(
                    topic=topic,
                    operation=operation,
                    entry_type=entry_type,
                    scope=str(item.get("scope", "")).strip(),
                    source_hints=[str(x).strip() for x in item.get("source_hints", []) if str(x).strip()],
                    related_entries=[str(x).strip() for x in item.get("related_entries", []) if str(x).strip()],
                    research_tasks=research_tasks,
                )
            )
        should_generate = bool(data.get("should_generate", bool(tasks)))
        summary = str(data.get("global_summary", "")).strip() or "Planned wiki generation tasks."
        return PlanResult(should_generate=should_generate and bool(tasks), global_summary=summary, tasks=tasks)
