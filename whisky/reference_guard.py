import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .models import ResearchItem, ResearchPacket


def _is_url_reachable(url: str, timeout_seconds: int = 10) -> bool:
    try:
        request = Request(url, headers={"User-Agent": "whisky-bot/1.0"}, method="HEAD")
        with urlopen(request, timeout=timeout_seconds) as response:
            return 200 <= int(response.status) < 400
    except Exception:
        try:
            request = Request(url, headers={"User-Agent": "whisky-bot/1.0"}, method="GET")
            with urlopen(request, timeout=timeout_seconds) as response:
                return 200 <= int(response.status) < 400
        except (HTTPError, URLError, TimeoutError):
            return False


def filter_reachable_references(packet: ResearchPacket) -> ResearchPacket:
    reachable: list[ResearchItem] = []
    for item in packet.items:
        if not item.url.startswith(("http://", "https://")):
            continue
        if _is_url_reachable(item.url):
            reachable.append(item)
    if reachable:
        summary = packet.summary
    else:
        summary = f"{packet.summary} No reachable references were validated; manual sourcing required."
    return ResearchPacket(topic=packet.topic, summary=summary, items=reachable)


def normalize_references_section(markdown_text: str, packet: ResearchPacket) -> str:
    lines = markdown_text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip().lower() == "## references":
            start = index
            break
    if start is not None:
        end = len(lines)
        for index in range(start + 1, len(lines)):
            if lines[index].startswith("## "):
                end = index
                break
        lines = lines[:start] + lines[end:]
    rebuilt = "\n".join(lines).rstrip()
    if packet.items:
        refs = "\n".join(f"- [{item.title}]({item.url}) — {item.relevance}" for item in packet.items)
        return rebuilt + "\n\n## References\n\n" + refs + "\n"
    return rebuilt + "\n\n## References\n\n- Needs more sources\n"


def contains_external_link(markdown_text: str) -> bool:
    return bool(re.search(r"\[[^\]]+\]\(https?://[^)]+\)", markdown_text))
