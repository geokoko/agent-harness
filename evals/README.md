# Evidence, not prompt aesthetics

> Historical PR #5 evidence. These results do not evaluate the October integrated
> candidate or the September branch. See the [current registry map](../docs/registry-map.md)
> and [build evidence](../docs/build-evidence.md).

Historical baseline: `e65d080f2a69457942abaee69d613e1851e9314d`.
The candidate in the checked-in results is **PR #5 at
`1938949977101c403e002037ad73e7401f08203c`**, not this integrated checkout or an
installed home configuration. Two evidence layers remain: filesystem contracts
and native discovery. The coding runner and its model results were removed; see
[historical coding comparison](#historical-coding-comparison).

## Local contracts and historical source measurements

These commands check the current checkout. Write fresh measurements to a separate
file; do not overwrite the historical structural record:

```bash
scripts/test-helpers
scripts/evaluate-harness --output /tmp/harness-current-structural.json
# A newer baseline uses its own shared-contract layout and installer flags.
scripts/evaluate-harness --baseline HEAD
```

These commands make no model calls. Use Bash, Git, GNU coreutils and Python 3.12+;
ShellCheck runs when available. Every shell script receives its own `bash -n`.
Installers run only against temporary destinations. Each snapshot uses its own
legacy or shared-contract workload layout and installer destination flags.
Legacy scripts without target flags are copied only after their expected
destination initializers are checked, then those initializers are redirected;
linking/conflict logic remains unchanged. Unknown legacy initializers and missing
required workload sources fail the evaluation. HOME and CODEX_HOME are not overridden.

The following table records the historical comparison against PR #5. No integrated
candidate source-size measurements are recorded in this table or the checked-in
JSON; see [build evidence](../docs/build-evidence.md) for current validation limits.

| Contract or source measurement | Old baseline | PR #5 |
|---|---:|---:|
| Installer scenario contracts | 7/16 | 16/16 |
| Codex skill entries | 35 | 5 |
| Claude child entries, excluding root router | 41 | 5 |
| Codex automatic metadata bytes | 6,082 | 154 |
| Claude automatic metadata bytes | 14,642 | 154 |
| Optional global instruction bytes | 1,352 | 582 |
| Code-review entrypoint bytes | 2,962 | 1,415 |
| Study notes + topic reference bytes | 5,486 | 2,468 |
| Portable recovery/handoff entrypoint bytes | 1,975 | 1,619 |
| Dual-agent entrypoint + phase manual bytes | 16,751 | 0 |
| Graph entrypoint + guide bytes | 53,973 | 0 |

The [historical structural record](deterministic-results.json) contains per-case
outcomes and exact source paths for that comparison. The current helper tests
also cover both directions of
instruction/skill path overlap, skills destinations inside source trees, symlink
aliases, obstructed ancestors, indirect legacy links, sudo refusal, installed
reference resolution through linked directories, per-registry metadata, and
preservation of existing files. No test enforces
provider parity, a role count, or a prompt-heading ritual.

These are historical source sizes, not actual model context or billing. At a rough
four characters per token, PR #5's optional common prefix fell from about **338 to 145**
tokens, ordinary planning from **683 to zero custom tokens**, review from
**741 to 354**, and graph skill/guide from **13,382 to zero custom tokens**.
These estimates do not describe the integrated candidate. Native instructions and
tools still consume context. Paths, formatting and client
boilerplate are excluded; not all old skill bodies were loaded on every turn.
Cached tokens still occupy context. The native opt-in policy was checked rather
than assuming that invisible commands have zero description cost.

## Historical native mechanism checks

[Sanitized discovery evidence](native-discovery.json) records two bounded checks:

- Codex CLI 0.155.1: toggling only `allow_implicit_invocation` changed the synthetic
  catalog from one entry to two; bodies stayed unloaded. No inference was used.
- Claude Code 2.1.284 / Opus 5.5: the synthetic `/evidence-review` command loaded
  its contract through the same symlink layout with exactly one Read. Only Read
  was available. This tests dispatch, not review quality or a home installation.

Claude restricted mode suppressed project-skill discovery in that tested build. The
successful dispatch probe used project settings, a native file-read fence and
Read-only tools instead. A separate probe using the real repository contract was
rejected by automatic approval review over export authorization; it did not run.
The accepted replacement sent only synthetic marker text. Actual repository
links and references were validated locally.

## Historical coding comparison

A ten-workload coding corpus compared the old prompt/catalog, native behavior and
PR #5 across 198 Codex and Claude Code trajectories (September 29). All arms
passed 26–28 of 30 strict tasks, so the fixtures could not separate them; only
cost differed. Candidate Claude input was 35.5% lower than old, but native-only
was cheaper still. In a separate review comparison, an adapted graph workflow
cost 4.27× and primary-plus-reviewer 1.98× primary-only, detecting no additional
seeded defects. That result justified removing mandatory review topology.

The runner, corpus and raw records were removed because near-saturated tasks
measured cost rather than skill behavior. They remain in commit
`da23eb49cb2ed1649a44b4b3b835027c2c88db6c` (PR #6 branch) under `evals/coding/`.

## Limits and retirement

Small deterministic fixtures expose regressions and common steering costs; they
cannot establish multi-hour autonomy, uncommon failures, production safety,
browser quality, or universal superiority across models. Three repetitions do
not prove equivalence. Native permission examples remain unapplied to the user's
host. A fresh-process handoff does not exercise actual context-window compaction.

No historical coding result established that every optional personal contract beats a fully
specified request. Review/publication/deployment contracts remain explicit-only
shortcuts, with retirement tests in the [assumption ledger](../docs/model-assumptions.md).
When a real failure occurs, retain its smallest representative task, compare the
same objective and permissions, and add machinery only when repeated evidence
justifies its cost.
