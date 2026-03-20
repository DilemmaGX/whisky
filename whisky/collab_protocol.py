import json
from .models import EntryTask


def build_structured_task_format() -> str:
    payload = {
        "global_objective": "Create or update high-quality wiki entries",
        "tasks": [
            {
                "topic": "Open Source",
                "operation": "create",
                "entry_type": "auto",
                "scope": "Definition, history, licenses, governance, and limitations.",
                "source_hints": ["OSI", "FSF", "Linux Foundation"],
                "related_entries": ["Software Licensing", "Free Software"],
                "research_tasks": [
                    {
                        "query": "Open Source Definition primary source",
                        "purpose": "Anchor formal definition",
                        "source_hints": ["official standards body"],
                    }
                ],
            }
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def task_to_protocol_block(task: EntryTask) -> str:
    payload = {
        "topic": task.topic,
        "operation": task.operation,
        "entry_type": task.entry_type,
        "scope": task.scope,
        "source_hints": task.source_hints,
        "related_entries": task.related_entries,
        "research_tasks": [
            {"query": rt.query, "purpose": rt.purpose, "source_hints": rt.source_hints} for rt in task.research_tasks
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)
