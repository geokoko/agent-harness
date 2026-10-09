"""Dependency-free, local evaluation helpers. Never launch model sessions."""

import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import tempfile


def run(command, **kwargs):
    return subprocess.run(command, text=True, capture_output=True, timeout=30, **kwargs)


def catalog(root, registry):
    return sorted((root / registry).glob("*/SKILL.md"))


def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"Missing frontmatter: {path}")
    return text.split("---\n", 2)[1]


def size(paths):
    contents = [path.read_bytes() for path in paths if path.is_file()]
    texts = [data.decode() for data in contents]
    return {"files": len(contents), "bytes": sum(map(len, contents)),
            "words": sum(len(text.split()) for text in texts),
            "characters": sum(map(len, texts)),
            "estimated_tokens_at_4_characters": sum((len(text) + 3) // 4 for text in texts)}


def context_metrics(root):
    """Exact source size, not model tokens or actual client-injected context."""
    metrics = {"codex_global_instructions": size([root / "codex/AGENTS.md"]),
               "claude_router_on_invocation": size([root / "claude-skills/SKILL.md"])}
    all_sources = set()
    for registry in ("codex-skills", "claude-skills"):
        paths = catalog(root, registry)
        metadata = [frontmatter(path).encode() for path in paths]
        automatic = [path for path in paths if not (
            registry == "claude-skills" and "disable-model-invocation: true" in frontmatter(path)
            or registry == "codex-skills" and (path.parent / "agents/openai.yaml").is_file()
            and "allow_implicit_invocation: false" in (path.parent / "agents/openai.yaml").read_text())]
        metrics[registry] = {
            "automatic_discovery_skills": len(automatic),
            "automatic_discovery_bytes": sum(len(frontmatter(path).encode()) for path in automatic),
            "logical_skills": len(paths),
            "discovery_bytes": sum(map(len, metadata)),
            "discovery_words": sum(len(data.decode().split()) for data in metadata),
            # Claude adapters load their linked contract on invocation.
            "loaded_files": size([*paths, *(path.parent / "contract.md" for path in paths)]),
        }
        all_sources.update(path.resolve() for path in paths)
    metrics["unique_skill_sources"] = size(sorted(all_sources))
    return metrics


def redirect_legacy_installer(content, provider, base, destination, codex_target):
    """Redirect only recognized legacy initializers; reject unknown scripts."""
    if provider == "codex":
        replacements = {
            'skills_dir="$HOME/.agents/skills"': "skills_dir=" + shlex.quote(str(destination)),
            'codex_home="${CODEX_HOME:-$HOME/.codex}"': "codex_home=" + shlex.quote(str(codex_target)),
        }
        if any(content.count(marker) != 1 for marker in replacements):
            raise ValueError("Unsupported legacy codex installer destination initialization")
        for marker, replacement in replacements.items():
            content = content.replace(marker, replacement)
        return content
    markers = ("# Resolve the target user's home directory.",
               'SKILLS_DIR="$USER_HOME/.claude/skills"', 'STATE_DIR="$USER_HOME/.geo"')
    if any(content.count(marker) != 1 for marker in markers):
        raise ValueError("Unsupported legacy claude installer destination initialization")
    start, end = (content.index(marker) for marker in markers[:2])
    if start >= end:
        raise ValueError("Unsupported legacy claude installer destination initialization")
    return (content[:start] + "TARGET_USER=$(id -un)\nUSER_HOME="
            + shlex.quote(str(base / "fixture home")) + "\n\n" + content[end:])


def installer_cases(root):
    """Exercise actual scripts in fixtures; return pass/fail and exit evidence.

    Use native destination flags when available. Recognized legacy scripts
    are copied with only destination initialization redirected; unknown legacy
    initializers fail before execution. HOME and CODEX_HOME are not overridden.
    """
    results = []
    scenarios = ("dry_run", "fresh_apply", "idempotent", "file_conflict",
                 "foreign_symlink", "dangling_symlink", "invalid_option",
                 "legacy_directory")
    for provider, script_name, registry in (
        ("codex", "scripts/install-codex", "codex-skills"),
        ("claude", "claude-skills/install.sh", "claude-skills"),
    ):
        original = (root / script_name).read_text()
        target_flags = bool(re.search(r"(?m)^\s*--skills-dir(?:\|--codex-home)?\)\s*$", original))
        for scenario in scenarios:
            with tempfile.TemporaryDirectory(prefix="harness-install-eval-") as temp:
                base = Path(temp)
                source = root
                destination = base / "fixture home" / (".agents" if provider == "codex" else ".claude") / "skills"
                codex_target = base / "codex config"
                if not target_flags:
                    content = redirect_legacy_installer(original, provider, base, destination, codex_target)
                    source = base / "repo"
                    shutil.copytree(root, source, symlinks=True, ignore=shutil.ignore_patterns(".git", "__pycache__"))
                    script = source / script_name
                    script.write_text(content)
                script = source / script_name
                names = [path.parent.name for path in catalog(source, registry)]
                if not names:
                    raise ValueError(f"No skills in {registry}")
                target = destination / names[-1]
                sentinel = base / "foreign"
                sentinel.mkdir()
                (sentinel / "keep").write_text("user data")
                if scenario in {"file_conflict", "foreign_symlink", "dangling_symlink", "legacy_directory"}:
                    destination.mkdir(parents=True)
                    if scenario == "file_conflict":
                        target.write_text("user data")
                    elif scenario == "foreign_symlink":
                        target.symlink_to(sentinel)
                    elif scenario == "dangling_symlink":
                        target.symlink_to(base / "missing")
                    else:
                        (destination / "geo").mkdir()
                        (destination / "geo/keep").write_text("user data")
                args = ["--skills-dir", str(destination)] if target_flags else []
                if target_flags and provider == "codex":
                    args += ["--codex-home", str(codex_target)]
                if scenario == "invalid_option":
                    args += ["--not-a-real-option"]
                elif scenario != "dry_run":
                    args += ["--apply"]
                command = ["bash", str(script), *args]
                result = run(command, cwd=source)
                if scenario == "idempotent" and result.returncode == 0:
                    result = run(command, cwd=source)
                if scenario == "dry_run":
                    passed = result.returncode == 0 and not destination.exists()
                elif scenario in {"fresh_apply", "idempotent"}:
                    passed = result.returncode == 0 and all(
                        (destination / name).is_symlink()
                        and (destination / name).resolve() == (source / registry / name).resolve()
                        for name in names)
                elif scenario == "file_conflict":
                    passed = (result.returncode != 0 and target.is_file() and not target.is_symlink()
                              and target.read_text() == "user data" and len(list(destination.iterdir())) == 1)
                elif scenario in {"foreign_symlink", "dangling_symlink"}:
                    expected = sentinel if scenario == "foreign_symlink" else base / "missing"
                    passed = (result.returncode != 0 and target.is_symlink()
                              and Path(os.readlink(target)) == expected
                              and len(list(destination.iterdir())) == 1)
                elif scenario == "legacy_directory":
                    saved = destination / "geo/keep"
                    passed = saved.is_file() and saved.read_text() == "user data"
                else:
                    passed = result.returncode != 0 and not destination.exists()
                results.append({"provider": provider, "case": scenario, "passed": bool(passed),
                                "exit_code": result.returncode})
    return results
