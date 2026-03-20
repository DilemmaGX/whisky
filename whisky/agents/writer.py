from ..deepseek_client import DeepSeekClient
from ..models import EntryTask, IssueContext, ResearchPacket


class WikiWriterAgent:
    def __init__(self, client: DeepSeekClient):
        self.client = client

    def run(
        self,
        issue: IssueContext,
        task: EntryTask,
        template_text: str,
        research_packet: ResearchPacket,
        obsidian_guide: str,
        revision_feedback: str = "",
        existing_content: str = "",
    ) -> str:
        system_prompt = (
            "You are an Obsidian wiki writer. Produce high-quality Markdown following the template structure. "
            "Keep the tone neutral, clear, and maintainable. Avoid fabricated numerical claims. "
            "If information is missing, explicitly write 'Needs more sources' and suggest source categories. "
            "Always include a 'References' section with markdown links using provided sources."
        )
        user_prompt = (
            f"Topic: {task.topic}\n\n"
            f"Operation: {task.operation}\n\n"
            f"Entry type: {task.entry_type}\n\n"
            f"Scope: {task.scope}\n\n"
            f"Issue title: {issue.title}\n\n"
            f"Issue body:\n{issue.body}\n\n"
            f"Structured research summary:\n{research_packet.summary}\n\n"
            "Structured research sources:\n"
            + "\n".join(
                f"- {item.title} | {item.url} | {item.relevance} | {item.snippet}" for item in research_packet.items
            )
            + "\n\n"
            + f"Obsidian authoring guide:\n{obsidian_guide}\n\n"
            + f"Existing content (for update/remake):\n{existing_content or 'None'}\n\n"
            f"Template:\n{template_text}\n\n"
            f"Revision feedback:\n{revision_feedback or 'None'}\n\n"
            "Output Markdown only."
        )
        return self.client.chat(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.3).strip()
