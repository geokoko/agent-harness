# agent-harness

Personal extensions for Claude Code and Codex: a few durable preferences,
specialist contracts, optional references, and safe installation helpers.
The native client supplies the model, tools, permissions, sessions, compaction,
worktrees and subagents. This repository adds no agent runtime or routing layer.

## What it adds

| Capability | Useful addition beyond native behavior | Invocation |
|---|---|---|
| [note-creation](shared-skills/note-creation/SKILL.md) | Personal Greek engineering exam-note standards, complete requested coverage, worked examples and PDF evidence | Native discovery or explicit selection |
| [review](shared-skills/review/SKILL.md) | Multiple-choice focus selection when unclear; report-only evidence contract with specialist references | Explicit skill selection |
| [decision-review](shared-skills/decision-review/SKILL.md) | Open-ended brainstorming, learning/weekend-project exploration and evidence-based initiative decisions | Native discovery or explicit selection |
| [learn-by-building](shared-skills/learn-by-building/SKILL.md) | Learn through an already chosen task: on decisions the user owns, they commit before seeing yours; their code is reviewed rather than rewritten; notes separate explained from demonstrated understanding | Native discovery or explicit selection |
| [cpo](shared-skills/cpo/SKILL.md) | Product strategy, discovery, positioning, pricing and growth deliverables within granted authority | Native discovery or explicit selection |
| [cto](shared-skills/cto/SKILL.md) | Technical direction, architecture, operational readiness and engineering priorities | Native discovery or explicit selection |
| [ui-design](shared-skills/ui-design/SKILL.md) | Design direction, responsive UI implementation and verified visual polish | Native discovery or explicit selection |
| [docs-update](shared-skills/docs-update/SKILL.md) | Actually create or update documentation, release notes and migration guidance | Native discovery or explicit selection |
| [browser-qa](shared-skills/browser-qa/SKILL.md) | Execute Chrome journeys through the client's browser MCP; reproduce defects and create tests or fixes when requested | Native discovery or explicit selection |
| [skill-eval](shared-skills/skill-eval/SKILL.md) | Compare skill behavior, discovery and artifacts with reproducible evidence | Native discovery or explicit selection |
| [ci-repair](shared-skills/ci-repair/SKILL.md) | Diagnose a specific failed CI revision and repair its cause with truthful validation | Native discovery or explicit selection |
| [consult](shared-skills/consult/SKILL.md) | Read-only opinion from a different model in fresh context, reconciled and verified before acting; unavailability reported, not substituted | Native discovery or explicit selection |
| [project-catchup](shared-skills/project-catchup/SKILL.md) | Read-only return briefing: recover roadmap and WIP, explain relevant collaborator changes since a baseline and orient to areas the user names | Native discovery or explicit selection |
| [agents-md-modernizer](shared-skills/agents-md-modernizer/SKILL.md) | Reduce AGENTS.md/CLAUDE.md to what an agent cannot infer: keep/remove/move/rewrite classification, protected rare-but-critical rules, verified commands and paths, and a disposition report with evidence | Native discovery or explicit selection |
| [handoff](shared-skills/handoff/SKILL.md) | Provider-neutral export with revision identity and reconciliation of stale evidence | Explicit skill selection |
| [ship](shared-skills/ship/SKILL.md) | Exact-change Claude review before shipping Codex work, scoped publication intent and precise status | Explicit skill selection |
| [deploy-verify](shared-skills/deploy-verify/SKILL.md) | Existing-deployment verification, exact revision and bounded baseline comparison | Explicit skill selection |

Use `/evidence-review` in Claude Code or `$review` in Codex. The Claude name
avoids its bundled `/review` alias; the other opt-in contracts share their names.
A normal coding, debugging, planning or review request can
proceed with native behavior; no skill chain precedes implementation.
[Working agreements](shared/AGENTS.md) are optional personal instructions,
linked from `claude/CLAUDE.md` and `codex/AGENTS.md`. They preserve the owner’s
standing requirements: explicit permission for shipping and Claude review before
shipping Codex-written changes. Review itself grants no publication authority.

This integrated rebuild reconciles four earlier versions of the harness: the
August cross-client harness, a September line that tuned model roles and added
CPO/CTO skills, a Claude proposal that cut the catalog to 18 skills, and a Codex
rebuild around native client capabilities. The
[full registry map](docs/registry-map.md) records every old name and its destination;
[build evidence](docs/build-evidence.md) distinguishes how the rebuild was
assembled, local checks and model review. Publishing does not install it in
either client.

## What earns a skill

A skill belongs here when it carries a recurring personal standard, non-obvious
domain knowledge, a precise authorization/output contract, or useful bundled
resources. Keep its description narrow and its root body short. Load references
only for the relevant task.

Generic advice to plan, navigate a repository, debug, test or act like a senior
engineer does not justify another skill. A recurring user-requested shortcut can
earn a skill when it reliably delivers a concrete artifact: `docs-update` edits
the requested documentation, and `ui-design` carries design intent through
to the requested interface. The owner also selected `browser-qa`, `skill-eval`
and `ci-repair` for repeatable journey tests, skill comparisons and CI repairs,
and `learn-by-building` for learning engineering through real project work.
`project-catchup` restores context after time away, with a scoped change briefing
and optional orientation to an unfamiliar area. `agents-md-modernizer` reduces a
repository's agent instructions to what a current agent cannot infer.
Mandatory phase sequences do not earn a skill, nor do role personas, repeated
review loops or fixed model assignments. Project facts
belong in that project's instructions and documentation.

Share a body when both clients can consume it unchanged. Add a thin client
adapter only for an actual native difference. Four Claude adapters enforce
manual invocation and link to shared contracts; Codex uses native invocation
metadata. Notes, product/technical leadership, decision review, frontend design,
documentation updates, browser QA, skill evaluation, CI repair, cross-model
consultation, guided learning and project catch-up link directly in both
registries.
Catalog parity is not a requirement.

## Permissions and state

The client's sandbox, tool approvals and service credentials enforce access.
Skill instructions describe intent; installing skills changes no permissions.
The [provider examples](docs/providers.md) are **unapplied** and do not recreate
the removed careful/freeze hooks. A workspace sandbox does not enforce a chosen
subdirectory or warn about every destructive operation inside it.

Native session continuation is the default. Use a handoff only for an explicit
export or transfer; there is no required task-state directory, journal or memory
service. Existing personal state is preserved.

## Install and validate

The installers require Bash and GNU coreutils (`ln -T`, `realpath -m`). Stock
macOS/BSD utilities do not satisfy this requirement.
Use the chosen stable checkout, not a temporary comparison worktree:

```bash
scripts/install-codex --dry-run
claude-skills/install.sh --dry-run
```

Both installers default to dry-run and reject conflicting destinations before
creating links. `--apply` creates the reviewed links. Codex's optional
`--global-agents` also links personal instructions; review and merge Claude's
personal instruction source manually. See [installation and updates](docs/skill-migration.md)
for destination overrides and handling an older installation.

```bash
scripts/test-helpers
scripts/evaluate-harness --help
git diff --check
```

Local tests check source and installation contracts. Model-task results,
context measurements and their limitations are separate in
[the evaluation record](evals/README.md).

## Keep the harness small

Before adding a mechanism, identify the observed failure and compare native
behavior with the candidate on representative tasks. Measure correctness and
interventions alongside context, calls, latency and cost where available.
Revisit retained instructions after client/model upgrades; remove machinery
whose improvement no longer justifies its cost.

- [Architecture](HARNESS_ARCHITECTURE.md)
- [Full four-source registry map](docs/registry-map.md)
- [Optional planning templates](docs/templates.md) and [tmux workflow](docs/tmux-workflow.md)
- [Historical audit of the August harness](docs/frontier-harness-audit.md)
- [Model assumptions and retirement tests](docs/model-assumptions.md)
- [Third-party attribution](THIRD_PARTY_NOTICES.md)
