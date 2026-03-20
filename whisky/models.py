from dataclasses import dataclass, field
from typing import List


@dataclass
class IssueContext:
    number: int
    title: str
    body: str
    labels: List[str] = field(default_factory=list)
    url: str = ""


@dataclass
class ClassificationResult:
    is_wiki_request: bool
    topic: str
    reason: str


@dataclass
class ReviewResult:
    passed: bool
    feedback: str


@dataclass
class PipelineResult:
    should_generate: bool
    issue_number: int
    topic: str
    file_path: str
    content: str
    summary: str
