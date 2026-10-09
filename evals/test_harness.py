"""Real local contracts: installation, discovery, references, recovery state."""

from pathlib import Path
import os
import re
import shutil
import tempfile
import unittest

from harness_eval import catalog, frontmatter, installer_cases, run

ROOT = Path(__file__).resolve().parents[1]


def markdown_files(root):
    """Markdown under root, following linked directories (rglob skips them before 3.13)."""
    seen = set()
    for directory, subdirectories, files in os.walk(root, followlinks=True):
        real = os.path.realpath(directory)
        if real in seen:
            # ponytail: realpath dedup breaks cycles; a second alias of a
            # directory is not walked again.
            subdirectories.clear()
            continue
        seen.add(real)
        yield from sorted(Path(directory) / name for name in files if name.endswith(".md"))


def broken_references(link):
    """Local Markdown links that are missing or escape the installed skill."""
    broken = []
    for source in markdown_files(link):
        for reference in re.findall(r"\[[^\]]*\]\(([^)]+)\)", source.read_text()):
            if reference.startswith(("https:", "http:", "#", "mailto:")):
                continue
            # Clients can normalize '..' before opening a path. Resolving it
            # through the source symlink first can hide escaping references.
            target = Path(os.path.normpath(source.parent / reference.split("#")[0]))
            if link not in target.parents or not target.is_file():
                broken.append(f"{source}: {reference}")
    return broken


class HarnessContracts(unittest.TestCase):
    def test_installers(self):
        for result in installer_cases(ROOT):
            with self.subTest(**result):
                self.assertTrue(result["passed"])

    def test_installers_normalize_cancelled_skill_path_components(self):
        for script, registry in (("scripts/install-codex", "codex-skills"),
                                 ("claude-skills/install.sh", "claude-skills")):
            with self.subTest(registry=registry), tempfile.TemporaryDirectory() as directory:
                skills = Path(directory) / "skills"
                # mkdir must not create a real ship directory that obstructs
                # its planned skill link.
                command = ["bash", str(ROOT / script), "--skills-dir"]
                original_path = str(skills / "ship/..")
                result = run([*command, original_path, "--dry-run"])
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertFalse(skills.exists())
                expected = {path.parent.name: path.parent for path in catalog(ROOT, registry)}
                for destination in (original_path, str(skills)):
                    result = run([*command, destination, "--apply"])
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual({path.name for path in skills.iterdir()}, set(expected))
                    for name, source in expected.items():
                        self.assertTrue((skills / name).is_symlink(), name)
                        self.assertEqual((skills / name).resolve(), source.resolve())
                # ship is now a symlink, so the original spelling resolves into
                # the source tree and must be rejected before writing there.
                result = run([*command, original_path, "--apply"])
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("inside source tree", result.stderr)

    def test_codex_instruction_conflict_is_preflighted(self):
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            target = temp / "config"
            target.mkdir()
            (target / "AGENTS.md").write_text("user rules")
            skills = temp / "skills"
            command = ["bash", str(ROOT / "scripts/install-codex"), "--apply",
                       "--skills-dir", str(skills), "--codex-home", str(target), "--global-agents"]
            result = run(command)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(skills.exists())
            self.assertEqual((target / "AGENTS.md").read_text(), "user rules")

    def test_obstructed_destination_aborts_before_skill_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            obstruction = temp / "config"
            obstruction.write_text("user file")
            skills = temp / "skills"
            result = run(["bash", str(ROOT / "scripts/install-codex"), "--apply",
                          "--skills-dir", str(skills), "--global-agents",
                          "--codex-home", str(obstruction / "nested")])
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(skills.exists())
            self.assertEqual(obstruction.read_text(), "user file")
            for script in ("scripts/install-codex", "claude-skills/install.sh"):
                result = run(["bash", str(ROOT / script), "--skills-dir", str(obstruction)])
                self.assertNotEqual(result.returncode, 0)
                result = run(["bash", str(ROOT / script), "--skills-dir", "--apply"])
                self.assertEqual(result.returncode, 2)

    def test_instruction_destination_cannot_follow_a_planned_skill_link(self):
        # Copy the installer into a minimal fixture: a regression must not
        # write into the real harness via one of its registry symlinks.
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            source = temp / "repo"
            (source / "scripts").mkdir(parents=True)
            shutil.copy2(ROOT / "scripts/install-codex", source / "scripts/install-codex")
            skill = source / "codex-skills/browse"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("fixture")
            (source / "codex").mkdir()
            (source / "codex/AGENTS.md").write_text("fixture instructions")
            alias = temp / "alias"
            alias.symlink_to(temp, target_is_directory=True)
            for home in (temp / "skills/browse", alias / "skills/browse"):
                result = run(["bash", str(source / "scripts/install-codex"), "--apply",
                              "--skills-dir", str(temp / "skills"), "--global-agents",
                              "--codex-home", str(home)])
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((temp / "skills").exists())
                self.assertFalse((skill / "AGENTS.md").exists())
            result = run(["bash", str(source / "scripts/install-codex"), "--apply",
                          "--skills-dir", str(temp / "skills"), "--global-agents",
                          "--codex-home", str(temp / "skills/browse/../config")])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((temp / "skills/config/AGENTS.md").is_symlink())
            self.assertFalse((source / "codex-skills/config").exists())

    def test_skill_directory_cannot_replace_planned_instruction_file(self):
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            alias = temp / "alias"
            alias.symlink_to(temp, target_is_directory=True)
            for skills in (temp / "config/AGENTS.md", temp / "config/AGENTS.md/skills",
                           alias / "config/AGENTS.md/skills"):
                result = run(["bash", str(ROOT / "scripts/install-codex"), "--apply",
                              "--skills-dir", str(skills), "--global-agents",
                              "--codex-home", str(temp / "config")])
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((temp / "config").exists())

    def test_codex_instruction_install_and_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            command = ["bash", str(ROOT / "scripts/install-codex"), "--apply",
                       "--skills-dir", str(temp / "skills"), "--codex-home", str(temp / "config"), "--global-agents"]
            for _ in range(2):
                self.assertEqual(run(command).returncode, 0)
            self.assertEqual((temp / "config/AGENTS.md").resolve(), (ROOT / "codex/AGENTS.md").resolve())

    def test_legacy_indirect_link_is_a_conflict(self):
        # A link reaching the source only through a retired umbrella (geo) must
        # not count as installed: unlinking geo would leave it dangling.
        for script, registry in (("claude-skills/install.sh", "claude-skills"),
                                 ("scripts/install-codex", "codex-skills")):
            with self.subTest(registry=registry), tempfile.TemporaryDirectory() as directory:
                skills = Path(directory) / "skills"
                skills.mkdir()
                (skills / "geo").symlink_to(ROOT / registry, target_is_directory=True)
                name = catalog(ROOT, registry)[0].parent.name
                (skills / name).symlink_to(f"geo/{name}")
                result = run(["bash", str(ROOT / script), "--apply", "--skills-dir", str(skills)])
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(f"only via geo/{name}", result.stderr)
                self.assertEqual(sorted(p.name for p in skills.iterdir()), sorted(["geo", name]))
                self.assertEqual(os.readlink(skills / name), f"geo/{name}")

    def test_skills_destination_cannot_be_inside_a_source_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            alias = Path(directory) / "alias"
            alias.symlink_to(ROOT, target_is_directory=True)
            for script, registry, skill in (("claude-skills/install.sh", "claude-skills", "evidence-review"),
                                            ("claude-skills/install.sh", "claude-skills", "cpo"),
                                            ("scripts/install-codex", "codex-skills", "review")):
                for skills in (ROOT / registry / skill / "nested", ROOT / registry / "nested",
                               ROOT / "shared-skills/review", alias / registry / skill):
                    with self.subTest(script=script, skills=str(skills)):
                        result = run(["bash", str(ROOT / script), "--skills-dir", str(skills)])
                        self.assertNotEqual(result.returncode, 0)
                        self.assertIn("inside source tree", result.stderr)
                result = run(["bash", str(ROOT / script), "--skills-dir", str(ROOT / "unrelated/skills")])
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_installer_invocation_guards(self):
        with tempfile.TemporaryDirectory() as directory:
            skills = Path(directory) / "skills"
            for script in ("claude-skills/install.sh", "scripts/install-codex"):
                result = run(["bash", str(ROOT / script), "--apply", "--skills-dir", str(skills)],
                             env=dict(os.environ, SUDO_USER="someone"))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("sudo", result.stderr)
                self.assertFalse(skills.exists())
            result = run(["bash", str(ROOT / "scripts/install-codex"), "--skills-dir", str(skills),
                          "--codex-home", str(Path(directory) / "config")])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("no effect without --global-agents", result.stderr)

    def test_discovery_and_installed_reference_paths(self):
        # No catalog parity requirement: validate what each client actually has.
        with tempfile.TemporaryDirectory() as directory:
            for registry in ("shared-skills", "codex-skills", "claude-skills"):
                installed = Path(directory) / registry
                installed.mkdir()
                self.assertTrue(catalog(ROOT, registry))
                for path in catalog(ROOT, registry):
                    link = installed / path.parent.name
                    link.symlink_to(path.parent, target_is_directory=True)
                    self.assertEqual(broken_references(link), [])
                for entry in (ROOT / registry).rglob("*"):
                    if entry.is_symlink(): self.assertTrue(entry.exists(), entry)

    def test_real_registries_preserve_opt_in_policies(self):
        expected = {
            "codex-skills": {"review", "handoff", "ship", "deploy-verify"},
            "claude-skills": {"evidence-review", "handoff", "ship", "deploy-verify"},
        }
        for registry, opt_in in expected.items():
            skills = catalog(ROOT, registry)
            self.assertTrue(opt_in <= {path.parent.name for path in skills}, registry)
            for skill in skills:
                with self.subTest(registry=registry, skill=skill.parent.name):
                    if registry == "claude-skills":
                        explicit_only = bool(re.search(
                            r"(?m)^disable-model-invocation: true[ \t]*$", frontmatter(skill)))
                    else:
                        policy = skill.parent / "agents/openai.yaml"
                        explicit_only = policy.is_file() and bool(re.search(
                            r"(?m)^policy:\s*\n(?:[ \t]+[^\n]*\n)*?"
                            r"  allow_implicit_invocation: false[ \t]*$", policy.read_text()))
                    self.assertEqual(explicit_only, skill.parent.name in opt_in)

    def test_reference_check_follows_linked_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            (temp / "shared").mkdir()
            (temp / "shared/guide.md").write_text("[gone](missing.md)\n")
            skill = temp / "skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text("[guide](references/guide.md)\n")
            (skill / "references").symlink_to(temp / "shared", target_is_directory=True)
            (skill / "loop").symlink_to(skill, target_is_directory=True)
            self.assertEqual(broken_references(skill),
                             [f"{skill}/references/guide.md: missing.md"])

    def test_skill_metadata(self):
        # Codex frontmatter is only name and description; Claude adapters may
        # add Claude keys. Every entry's name must match its directory.
        for registry in ("shared-skills", "codex-skills", "claude-skills"):
            for skill in catalog(ROOT, registry):
                with self.subTest(registry=registry, skill=skill.parent.name):
                    metadata = frontmatter(skill)
                    if registry != "claude-skills":
                        keys = re.findall(r"^([A-Za-z_-]+):", metadata, re.M)
                        self.assertEqual(sorted(keys), ["description", "name"])
                    self.assertRegex(metadata, rf"(?m)^name: {re.escape(skill.parent.name)}$")
                    self.assertRegex(metadata, r"(?m)^description: .+\S$")
                    # In an unquoted YAML value ": " is an error and " #" starts a comment.
                    self.assertNotRegex(metadata, r"(?m)^description: [^\"'].*(: | #)")

    def test_codex_discovery_budget_and_retired_names(self):
        # Codex loads every skill's frontmatter at startup; keep it bounded.
        metadata_bytes = sum(len(frontmatter(skill).encode()) for skill in catalog(ROOT, "codex-skills"))
        self.assertLessEqual(metadata_bytes, 7000)
        for retired in ("canary", "cso", "retro"):
            self.assertFalse(os.path.lexists(ROOT / "codex-skills" / retired), retired)


if __name__ == "__main__":
    unittest.main()
