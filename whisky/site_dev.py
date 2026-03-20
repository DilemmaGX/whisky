from pathlib import Path
import re
import shutil
import subprocess


def _replace_config_value(config_text: str, key: str, value: str) -> str:
    pattern = rf'{key}:\s*"[^"]*"'
    replacement = f'{key}: "{value}"'
    return re.sub(pattern, replacement, config_text)


def prepare_quartz_workspace(repo_root: Path, workspace_name: str = ".quartz-dev") -> Path:
    workspace = repo_root / workspace_name
    quartz = workspace / "quartz"
    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", "v4", "https://github.com/jackyzha0/quartz.git", str(quartz)],
        check=True,
        cwd=repo_root,
    )
    content_root = quartz / "content"
    if content_root.exists():
        shutil.rmtree(content_root)
    content_root.mkdir(parents=True, exist_ok=True)

    site_root = repo_root / "site"
    if site_root.exists():
        for item in site_root.iterdir():
            target = content_root / item.name
            if item.is_dir():
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)

    if not (content_root / "index.md").exists():
        welcome = repo_root / "Welcome.md"
        if welcome.exists():
            shutil.copy2(welcome, content_root / "index.md")
        else:
            (content_root / "index.md").write_text("# whisky\n\nWelcome to whisky.\n", encoding="utf-8")

    wiki_root = repo_root / "wiki"
    if wiki_root.exists():
        shutil.copytree(wiki_root, content_root / "wiki", dirs_exist_ok=True)

    config_path = quartz / "quartz.config.ts"
    config_text = config_path.read_text(encoding="utf-8")
    config_text = _replace_config_value(config_text, "baseUrl", "localhost:8080")
    config_text = _replace_config_value(config_text, "pageTitle", "whisky")
    config_path.write_text(config_text, encoding="utf-8")
    return quartz


def run_local_dev_server(repo_root: Path) -> int:
    quartz_root = prepare_quartz_workspace(repo_root)
    subprocess.run(["npm", "ci"], check=True, cwd=quartz_root)
    process = subprocess.run(["npx", "quartz", "build", "--serve"], cwd=quartz_root)
    return process.returncode
