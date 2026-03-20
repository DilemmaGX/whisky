import json
from dataclasses import dataclass
from http.client import IncompleteRead
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass
class DeepSeekClient:
    api_key: str
    model: str
    api_base: str

    def chat(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
        endpoint = f"{self.api_base}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": temperature,
        }
        data = json.dumps(payload).encode("utf-8")
        last_error: Exception | None = None
        for attempt in range(3):
            try:
                request = Request(
                    endpoint,
                    data=data,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self.api_key}",
                    },
                    method="POST",
                )
                with urlopen(request, timeout=90) as response:
                    body = response.read().decode("utf-8")
                parsed = json.loads(body)
                choices = parsed.get("choices", [])
                if not choices:
                    raise RuntimeError("DeepSeek returned no choices")
                message = choices[0].get("message", {})
                content = message.get("content", "")
                if not content:
                    raise RuntimeError("DeepSeek returned empty content")
                return content
            except HTTPError as error:
                detail = error.read().decode("utf-8", errors="ignore")
                last_error = RuntimeError(f"DeepSeek HTTP error {error.code}: {detail}")
            except (URLError, TimeoutError, json.JSONDecodeError, IncompleteRead, RuntimeError) as error:
                last_error = error
            if attempt < 2:
                time.sleep(2 ** attempt)
        raise RuntimeError(f"DeepSeek request failed after retries: {last_error}")
