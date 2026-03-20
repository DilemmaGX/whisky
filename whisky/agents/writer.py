from ..deepseek_client import DeepSeekClient
from ..models import IssueContext


class WikiWriterAgent:
    def __init__(self, client: DeepSeekClient):
        self.client = client

    def run(self, issue: IssueContext, topic: str, template_text: str, revision_feedback: str = "") -> str:
        system_prompt = (
            "You are an Obsidian wiki writer. Produce high-quality Markdown following the template structure. "
            "Keep the tone neutral, clear, and maintainable. Avoid fabricated numerical claims. "
            "If information is missing, explicitly write 'Needs more sources' and suggest source categories."
        )
        user_prompt = (
            f"Topic: {topic}\n\n"
            f"Issue title: {issue.title}\n\n"
            f"Issue body:\n{issue.body}\n\n"
            f"Template:\n{template_text}\n\n"
            f"Revision feedback:\n{revision_feedback or 'None'}\n\n"
            "Output Markdown only."
        )
        return self.client.chat(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.3).strip()
