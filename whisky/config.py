from dataclasses import dataclass
from pathlib import Path
import os


@dataclass
class AppConfig:
    api_key: str
    model: str
    api_base: str
    wiki_root: Path
    roles_root: Path
    templates_root: Path


def _load_api_key_from_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def load_config(repo_root: Path) -> AppConfig:
    env_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    key_file = os.getenv("DEEPSEEK_API_KEY_FILE", "").strip()
    default_key_file = repo_root / "API_KEY"
    file_key = _load_api_key_from_file(Path(key_file)) if key_file else _load_api_key_from_file(default_key_file)
    api_key = env_key or file_key
    model = os.getenv("WHISKY_DEEPSEEK_MODEL", "deepseek-chat").strip()
    api_base = os.getenv("WHISKY_DEEPSEEK_API_BASE", "https://api.deepseek.com/v1").strip().rstrip("/")
    return AppConfig(
        api_key=api_key,
        model=model,
        api_base=api_base,
        wiki_root=repo_root / "wiki",
        roles_root=repo_root / "roles",
        templates_root=repo_root / "templates" / "wiki",
    )
