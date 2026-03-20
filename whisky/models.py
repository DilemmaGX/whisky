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
class ResearchTask:
    query: str
    purpose: str
    source_hints: List[str] = field(default_factory=list)


@dataclass
class EntryTask:
    topic: str
    operation: str
    entry_type: str
    scope: str
    source_hints: List[str] = field(default_factory=list)
    related_entries: List[str] = field(default_factory=list)
    research_tasks: List[ResearchTask] = field(default_factory=list)


@dataclass
class PlanResult:
    should_generate: bool
    global_summary: str
    tasks: List[EntryTask] = field(default_factory=list)


@dataclass
class ResearchItem:
    title: str
    url: str
    snippet: str
    relevance: str


@dataclass
class ResearchPacket:
    topic: str
    summary: str
    items: List[ResearchItem] = field(default_factory=list)


@dataclass
class EntryOutput:
    topic: str
    file_path: str
    operation: str


@dataclass
class PipelineResult:
    should_generate: bool
    issue_number: int
    summary: str
    topics: List[str] = field(default_factory=list)
    file_paths: List[str] = field(default_factory=list)
