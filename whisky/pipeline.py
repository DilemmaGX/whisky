from pathlib import Path

from .agents import ContentReviewerAgent, FormatReviewerAgent, IssueClassifierAgent, WikiWriterAgent
from .config import AppConfig
from .deepseek_client import DeepSeekClient
from .editor_api import WikiEditorAPI
from .models import IssueContext, PipelineResult
from .obsidian import build_wiki_path, ensure_obsidian_frontmatter


def _select_template(topic: str, templates_root: Path) -> str:
    lowered = topic.lower()
    if any(key in lowered for key in ["person", "biography", "founder"]):
        path = templates_root / "biography.template.md"
    elif any(key in lowered for key in ["technology", "framework", "protocol", "api"]):
        path = templates_root / "technology.template.md"
    elif any(key in lowered for key in ["concept", "theory", "method"]):
        path = templates_root / "concept.template.md"
    else:
        path = templates_root / "entry.template.md"
    return path.read_text(encoding="utf-8")


def run_pipeline(issue: IssueContext, config: AppConfig) -> PipelineResult:
    if not config.api_key:
        raise RuntimeError("DeepSeek API key not found. Set DEEPSEEK_API_KEY or provide the API_KEY file in repository root.")
    client = DeepSeekClient(api_key=config.api_key, model=config.model, api_base=config.api_base)
    classifier = IssueClassifierAgent(client)
    writer = WikiWriterAgent(client)
    content_reviewer = ContentReviewerAgent(client)
    format_reviewer = FormatReviewerAgent(client)
    editor_api = WikiEditorAPI()

    classification = classifier.run(issue)
    if not classification.is_wiki_request:
        return PipelineResult(
            should_generate=False,
            issue_number=issue.number,
            topic=classification.topic,
            file_path="",
            content="",
            summary=classification.reason or "This issue is not a wiki entry request.",
        )

    template_text = _select_template(classification.topic, config.templates_root)
    draft = writer.run(issue=issue, topic=classification.topic, template_text=template_text)
    content_review = content_reviewer.run(topic=classification.topic, markdown_text=draft)
    format_review = format_reviewer.run(topic=classification.topic, markdown_text=draft)

    if not content_review.passed or not format_review.passed:
        feedback = "\n".join(
            [
                f"Content review: {content_review.feedback}",
                f"Format review: {format_review.feedback}",
            ]
        ).strip()
        draft = writer.run(issue=issue, topic=classification.topic, template_text=template_text, revision_feedback=feedback)

    normalized = ensure_obsidian_frontmatter(draft, classification.topic)
    invalid_links = editor_api.validate_internal_links(normalized)
    if invalid_links:
        normalized = normalized.rstrip() + "\n\n## Links to Fix\n\n" + "\n".join(f"- [[{ref}]]" for ref in invalid_links) + "\n"

    path = build_wiki_path(config.wiki_root, classification.topic)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8")

    summary = f"Generated wiki entry: {classification.topic}; output file: {path.as_posix()}"
    return PipelineResult(
        should_generate=True,
        issue_number=issue.number,
        topic=classification.topic,
        file_path=str(path),
        content=normalized,
        summary=summary,
    )
