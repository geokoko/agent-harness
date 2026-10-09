"""Baseline comparisons must measure the selected snapshot without home writes."""

import io
import json
from pathlib import Path
import runpy
import subprocess
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import harness_eval

ROOT = Path(__file__).resolve().parents[1]
EVALUATOR = runpy.run_path(str(ROOT / "scripts/evaluate-harness"))
# Pre-publication snapshots: the August harness (legacy layout) and the Codex
# native rebuild. They are not in the published history, so comparisons against
# them run only in a checkout that still has these commits.
LEGACY = "e65d080f2a69457942abaee69d613e1851e9314d"
CODEX_REBUILD = "1938949977101c403e002037ad73e7401f08203c"
UNPUBLISHED = "historical snapshot not in this checkout"


def available(revision):
    return subprocess.run(["git", "cat-file", "-e", f"{revision}^{{commit}}"],
                          cwd=ROOT, capture_output=True).returncode == 0


def extract(revision, destination):
    archive = subprocess.check_output(["git", "archive", revision], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
        stream.extractall(destination, filter="data")


class BaselineEvaluation(unittest.TestCase):
    def compare(self, revision):
        result = subprocess.run(
            [str(ROOT / "scripts/evaluate-harness"), "--baseline", revision],
            cwd=ROOT, text=True, capture_output=True, timeout=120,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["baseline_commit"], subprocess.check_output(
            ["git", "rev-parse", f"{revision}^{{commit}}"], cwd=ROOT, text=True).strip())
        self.assertEqual(report["new"]["installer_summary"], {"passed": 16, "total": 16})
        return report

    def test_modern_baselines_use_shared_workloads_and_target_flags(self):
        for revision in (CODEX_REBUILD, "HEAD"):
            with self.subTest(revision=revision):
                if not available(revision):
                    self.skipTest(UNPUBLISHED)
                report = self.compare(revision)
                self.assertEqual(report["old"]["installer_summary"], {"passed": 16, "total": 16})
                workloads = report["old"]["workloads"]
                self.assertEqual(workloads["code_review"]["paths"], ["shared-skills/review/SKILL.md"])
                self.assertEqual(workloads["task_recovery"]["paths"], ["shared-skills/handoff/SKILL.md"])
                self.assertEqual(workloads["implementation_plan"]["files"], 0)

    @unittest.skipUnless(available(LEGACY), UNPUBLISHED)
    def test_legacy_baseline_retains_historical_measurements(self):
        report = self.compare(LEGACY)
        self.assertEqual(report["old"]["installer_summary"], {"passed": 7, "total": 16})
        workloads = report["old"]["workloads"]
        self.assertEqual(workloads["code_review"]["paths"], ["codex-skills/code-check/SKILL.md"])
        self.assertEqual(workloads["implementation_plan"]["files"], 1)
        self.assertEqual(workloads["dual_agent_coordination"]["files"], 2)

    def test_missing_known_workload_source_is_an_error(self):
        for revision, missing in (
            (LEGACY, "shared-skills/dual-agent-software-engineering/references/phases.md"),
            (CODEX_REBUILD, "shared-skills/review/SKILL.md"),
        ):
            with self.subTest(revision=revision), tempfile.TemporaryDirectory() as directory:
                if not available(revision):
                    self.skipTest(UNPUBLISHED)
                source = Path(directory)
                extract(revision, source)
                (source / missing).unlink()
                with self.assertRaisesRegex(ValueError, "missing source files"):
                    EVALUATOR["workload_metrics"](source)

    @unittest.skipUnless(available(LEGACY), UNPUBLISHED)
    def test_unrecognized_legacy_destination_never_executes(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            extract(LEGACY, source)
            script = source / "scripts/install-codex"
            script.write_text(script.read_text().replace(
                'skills_dir="$HOME/.agents/skills"', 'skills_dir="$HOME/other-skills"'))
            with patch.object(harness_eval, "run") as execute:
                with self.assertRaisesRegex(ValueError, "legacy codex"):
                    harness_eval.installer_cases(source)
                execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()
