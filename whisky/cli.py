import argparse
import json
import os
from pathlib import Path
import sys

from .config import load_config
from .collab_protocol import build_structured_task_format
from .issue_parser import issue_from_event, issue_from_json
from .logging_utils import build_logger, sanitize_secret
from .pipeline import run_pipeline


def _write_outputs(data: dict) -> None:
    output_path = os.getenv("GITHUB_OUTPUT", "").strip()
    if not output_path:
        return
    lines = [f"{key}={value}" for key, value in data.items()]
    with open(output_path, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def cmd_issue_event(args: argparse.Namespace) -> int:
    logger = build_logger()
    issue = issue_from_event(Path(args.event_path))
    is_candidate = bool(issue.title.strip() or issue.body.strip())
    result = {
        "issue_number": issue.number,
        "issue_title": issue.title.replace("\n", " "),
        "should_process": str(is_candidate).lower(),
    }
    if args.github_output:
        _write_outputs(result)
    logger.info("issue_event parsed issue_number=%s should_process=%s", issue.number, is_candidate)
    print(json.dumps(result, ensure_ascii=False))
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    logger = build_logger()
    config = load_config(repo_root=repo_root)
    logger.info(
        "run start repo=%s model=%s api_base=%s api_key=%s",
        str(repo_root),
        config.model,
        config.api_base,
        sanitize_secret(config.api_key),
    )
    if args.issue_json:
        issue = issue_from_json(Path(args.issue_json).read_text(encoding="utf-8"))
    else:
        issue = issue_from_event(Path(args.event_path))
    result = run_pipeline(issue=issue, config=config)
    primary_topic = result.topics[0] if result.topics else ""
    primary_file = result.file_paths[0] if result.file_paths else ""
    output = {
        "should_generate": str(result.should_generate).lower(),
        "issue_number": result.issue_number,
        "topic": primary_topic,
        "file_path": primary_file,
        "topics": ",".join(result.topics),
        "file_paths": ",".join(result.file_paths),
        "summary": result.summary.replace("\n", " "),
    }
    if args.github_output:
        _write_outputs(output)
    print(json.dumps(output, ensure_ascii=False))
    return 0


def cmd_assist_outline(args: argparse.Namespace) -> int:
    from .editor_api import WikiEditorAPI

    api = WikiEditorAPI()
    print(api.build_outline_prompt(topic=args.topic, target_sections=args.sections))
    return 0


def cmd_assist_validate(args: argparse.Namespace) -> int:
    from .editor_api import WikiEditorAPI

    api = WikiEditorAPI()
    text = Path(args.file).read_text(encoding="utf-8")
    invalid = api.validate_internal_links(text)
    print(json.dumps({"invalid_links": invalid}, ensure_ascii=False))
    return 0


def cmd_assist_protocol(args: argparse.Namespace) -> int:
    print(build_structured_task_format())
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="whisky")
    sub = parser.add_subparsers(dest="command", required=True)

    issue_event = sub.add_parser("issue-event")
    issue_event.add_argument("--event-path", required=True)
    issue_event.add_argument("--github-output", action="store_true")
    issue_event.set_defaults(func=cmd_issue_event)

    run = sub.add_parser("run")
    run.add_argument("--repo-root", default=".")
    run.add_argument("--event-path")
    run.add_argument("--issue-json")
    run.add_argument("--github-output", action="store_true")
    run.set_defaults(func=cmd_run)

    assist = sub.add_parser("assist")
    assist_sub = assist.add_subparsers(dest="assist_command", required=True)

    outline = assist_sub.add_parser("outline")
    outline.add_argument("--topic", required=True)
    outline.add_argument("--sections", type=int, default=8)
    outline.set_defaults(func=cmd_assist_outline)

    validate = assist_sub.add_parser("validate")
    validate.add_argument("--file", required=True)
    validate.set_defaults(func=cmd_assist_validate)

    protocol = assist_sub.add_parser("protocol")
    protocol.set_defaults(func=cmd_assist_protocol)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
