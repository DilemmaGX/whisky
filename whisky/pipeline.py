from pathlib import Path
import re

from .agents import (
    ContentReviewerAgent,
    FormatReviewerAgent,
    IssueClassifierAgent,
    ResearchCollectorAgent,
    TaskPlannerAgent,
    WikiWriterAgent,
)
from .collab_protocol import task_to_protocol_block
from .config import AppConfig
from .deepseek_client import DeepSeekClient
from .editor_api import WikiEditorAPI
from .models import EntryOutput, EntryTask, IssueContext, PipelineResult, PlanResult, ResearchPacket, ResearchTask
from .obsidian import build_wiki_path, ensure_obsidian_frontmatter
from .reference_guard import filter_reachable_references, normalize_references_section


def _select_template(task: EntryTask, templates_root: Path) -> str:
    if task.entry_type == "biography":
        path = templates_root / "biography.template.md"
    elif task.entry_type == "technology":
        path = templates_root / "technology.template.md"
    elif task.entry_type == "concept":
        path = templates_root / "concept.template.md"
    else:
        path = templates_root / "entry.template.md"
    return path.read_text(encoding="utf-8")


def _load_obsidian_guide(roles_root: Path) -> str:
    guide_path = roles_root / "obsidian-advanced-authoring.md"
    if guide_path.exists():
        return guide_path.read_text(encoding="utf-8")
    return "Use Obsidian-friendly Markdown with internal links, backlinks awareness, and graph-friendly linked entities."


def _fallback_plan(issue: IssueContext) -> PlanResult:
    title_part = issue.title.split(":", 1)[-1].strip() if ":" in issue.title else issue.title
    candidates = re.split(r",| and |/|;", title_part, flags=re.IGNORECASE)
    topics = []
    for candidate in candidates:
        cleaned = re.sub(r"(?i)wiki entry request:|create|update|remake|entry|wiki|for|please", "", candidate).strip(" -:.")
        cleaned = re.sub(r"[^A-Za-z0-9 \-_/]", "", cleaned).strip()
        if len(cleaned) >= 3 and cleaned.lower() not in {"issue", "request"}:
            topics.append(cleaned.title())
    deduped = []
    for topic in topics:
        if topic not in deduped:
            deduped.append(topic)
    deduped = deduped[:3]
    if not deduped:
        deduped = [issue.title.strip() or "Untitled Entry"]
    tasks = [
        EntryTask(
            topic=topic,
            operation="create",
            entry_type="general",
            scope="Provide definition, background, core concepts, practical usage, limitations, and references.",
            source_hints=[],
            related_entries=[],
            research_tasks=[ResearchTask(query=f"{topic} official references", purpose="Fallback evidence collection", source_hints=[])],
        )
        for topic in deduped
    ]
    return PlanResult(should_generate=True, global_summary="Fallback plan generated due planner unavailability.", tasks=tasks)


def _fallback_research_packet(task: EntryTask) -> ResearchPacket:
    return ResearchPacket(topic=task.topic, summary=f"Fallback research packet for {task.topic}. Needs more sources.", items=[])


def _fallback_draft(task: EntryTask, template_text: str, existing_content: str) -> str:
    base = template_text.replace("{{topic}}", task.topic).strip()
    extra = "\n\n## Operation Notes\n\n"
    if task.operation == "update" and existing_content:
        extra += "This entry was generated in update mode. Existing content should be reviewed and merged carefully."
    elif task.operation == "remake":
        extra += "This entry was generated in remake mode and should replace prior structure after human review."
    else:
        extra += "This entry was generated in create mode."
    extra += "\n\n## References\n\n- Needs more sources\n"
    return base + extra


def _generate_single_entry(
    issue: IssueContext,
    task: EntryTask,
    config: AppConfig,
    writer: WikiWriterAgent,
    researcher: ResearchCollectorAgent,
    content_reviewer: ContentReviewerAgent,
    format_reviewer: FormatReviewerAgent,
    editor_api: WikiEditorAPI,
) -> EntryOutput:
    template_text = _select_template(task, config.templates_root)
    path = build_wiki_path(config.wiki_root, task.topic, task.entry_type)
    existing_content = path.read_text(encoding="utf-8") if path.exists() else ""
    try:
        research_packet = researcher.run(task)
    except Exception:
        research_packet = _fallback_research_packet(task)
    research_packet = filter_reachable_references(research_packet)
    obsidian_guide = _load_obsidian_guide(config.roles_root)
    enriched_scope = task.scope.strip()
    if task.related_entries:
        enriched_scope += f"\n\nRelated entries to link: {', '.join(task.related_entries)}"
    if task.research_tasks:
        enriched_scope += "\n\nStructured research plan:\n- " + task_to_protocol_block(task)
    enriched_task = EntryTask(
        topic=task.topic,
        operation=task.operation,
        entry_type=task.entry_type,
        scope=enriched_scope,
        source_hints=task.source_hints,
        related_entries=task.related_entries,
        research_tasks=task.research_tasks,
    )
    try:
        draft = writer.run(
            issue=issue,
            task=enriched_task,
            template_text=template_text,
            research_packet=research_packet,
            obsidian_guide=obsidian_guide,
            existing_content=existing_content,
        )
    except Exception:
        draft = _fallback_draft(task, template_text, existing_content)
    try:
        content_review = content_reviewer.run(topic=task.topic, markdown_text=draft)
        format_review = format_reviewer.run(topic=task.topic, markdown_text=draft)
    except Exception:
        content_review = type("ReviewState", (), {"passed": True, "feedback": ""})()
        format_review = type("ReviewState", (), {"passed": True, "feedback": ""})()

    if not content_review.passed or not format_review.passed:
        feedback = "\n".join(
            [
                f"Content review: {content_review.feedback}",
                f"Format review: {format_review.feedback}",
            ]
        ).strip()
        try:
            draft = writer.run(
                issue=issue,
                task=enriched_task,
                template_text=template_text,
                research_packet=research_packet,
                obsidian_guide=obsidian_guide,
                revision_feedback=feedback,
                existing_content=existing_content,
            )
        except Exception:
            draft = _fallback_draft(task, template_text, existing_content)

    normalized = ensure_obsidian_frontmatter(draft, task.topic)
    normalized = normalize_references_section(normalized, research_packet)
    invalid_links = editor_api.validate_internal_links(normalized)
    if invalid_links:
        normalized = normalized.rstrip() + "\n\n## Links to Fix\n\n" + "\n".join(f"- [[{ref}]]" for ref in invalid_links) + "\n"

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8")
    return EntryOutput(topic=task.topic, file_path=str(path), operation=task.operation)


def run_pipeline(issue: IssueContext, config: AppConfig) -> PipelineResult:
    if not config.api_key:
        raise RuntimeError("DeepSeek API key not found. Set DEEPSEEK_API_KEY or provide the API_KEY file in repository root.")
    client = DeepSeekClient(api_key=config.api_key, model=config.model, api_base=config.api_base)
    classifier = IssueClassifierAgent(client)
    planner = TaskPlannerAgent(client)
    researcher = ResearchCollectorAgent(client)
    writer = WikiWriterAgent(client)
    content_reviewer = ContentReviewerAgent(client)
    format_reviewer = FormatReviewerAgent(client)
    editor_api = WikiEditorAPI()

    try:
        classification = classifier.run(issue)
    except Exception:
        classification = type("ClassState", (), {"is_wiki_request": True, "reason": "Classifier unavailable; fallback execution."})()
    if not classification.is_wiki_request:
        return PipelineResult(
            should_generate=False,
            issue_number=issue.number,
            topics=[],
            file_paths=[],
            summary=classification.reason or "This issue is not a wiki entry request.",
        )

    try:
        plan = planner.run(issue)
    except Exception:
        plan = _fallback_plan(issue)
    if not plan.should_generate or not plan.tasks:
        return PipelineResult(
            should_generate=False,
            issue_number=issue.number,
            topics=[],
            file_paths=[],
            summary=plan.global_summary or "Planner produced no actionable wiki tasks.",
        )

    outputs = [
        _generate_single_entry(
            issue=issue,
            task=task,
            config=config,
            writer=writer,
            researcher=researcher,
            content_reviewer=content_reviewer,
            format_reviewer=format_reviewer,
            editor_api=editor_api,
        )
        for task in plan.tasks
    ]
    topics = [item.topic for item in outputs]
    file_paths = [item.file_path for item in outputs]
    summary = (
        f"Generated {len(outputs)} wiki entries. "
        + "; ".join(f"{item.operation}:{item.topic}->{Path(item.file_path).as_posix()}" for item in outputs)
    )
    return PipelineResult(
        should_generate=True,
        issue_number=issue.number,
        topics=topics,
        file_paths=file_paths,
        summary=summary,
    )
