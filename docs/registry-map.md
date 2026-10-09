# Complete registry reconciliation

This is the migration map for the integrated rebuild. It
reconciles both development lines and both rebuild proposals. It is not an
installation record or a claim that these changes are merged, published, or
active in either client. Existing installed links and legacy artifacts remain
outside this candidate’s changes.

## Source snapshots

All comparisons use these immutable commits, not moving branch names:

| Snapshot | Exact revision | Claude entries | Codex entries |
|---|---|---:|---:|
| `main` | [`e65d080f2a69457942abaee69d613e1851e9314d`](https://github.com/geokoko/agent-harness/tree/e65d080f2a69457942abaee69d613e1851e9314d) | 41 + root `geo` | 35 |
| `skills/shared-graph-model-tuning` | [`128efe0edf1418958e473f384694ea9358b6c435`](https://github.com/geokoko/agent-harness/tree/128efe0edf1418958e473f384694ea9358b6c435) | 33 + root `geo` | 28 |
| Claude PR #4 | [`ba9da80de697b922ae4f94a098ecb8ee8a794869`](https://github.com/geokoko/agent-harness/tree/ba9da80de697b922ae4f94a098ecb8ee8a794869) | 18 + root `geo` | 14 |
| Codex PR #5 | [`1938949977101c403e002037ad73e7401f08203c`](https://github.com/geokoko/agent-harness/tree/1938949977101c403e002037ad73e7401f08203c) | 5 | 5 |

`main` and the September branch diverged from
`4f3d3e14bd527a98b424ce65764276fce9ada2cf`: `main` has 7 commits unique
to its line and September has 43. Commit counts describe ancestry, not the
amount of unique functionality. Both rebuild PRs use the `main` line;
September is not their ancestor. Its full `cpo` and `cto` work therefore
requires explicit incorporation. Its `canary`, `cso`, and `retro` names are
accounted for alongside `main`’s corresponding longer names below.

## Resulting registry

Every canonical contract below is exposed to both clients. Codex uses `$name`;
Claude uses `/name`, except the review entry is `/evidence-review`.

| Canonical skill | Scope | Discovery intent |
|---|---|---|
| `note-creation` | Source-faithful engineering study material and checked PDF output | Relevant study-material request |
| `review` | Evidence-backed assessment; clarify ambiguous focus with multiple choice | Explicit selection; Claude `evidence-review` |
| `decision-review` | Open-ended brainstorming and builder exploration; bounded decisions use relevant product/viability/technical lenses | Brainstorming, project-idea exploration or a bounded decision request |
| `learn-by-building` | Guided learning inside authorized work: user-first on decisions the user owns, reviewed user code, explained-versus-demonstrated notes | A request to learn from, or be guided through, a task |
| `cpo` | Product leadership, marketing/growth and authorized concrete execution | Narrow product-lead mandate |
| `cto` | Technical leadership, priorities/readiness and authorized concrete execution | Narrow technical-lead mandate |
| `ui-design` | Visual direction, responsive pages/components and authorized polish | Design, build, redesign or polish a web interface |
| `docs-update` | Create/update requested docs, release notes and migration guidance | Document a feature, update docs or prepare release documentation |
| `browser-qa` | Execute Chrome journeys through GPT/Codex's or Claude's browser MCP; reproduce failures and create tests or fixes within scope | Test a web app or a specific browser journey |
| `skill-eval` | Compare behavior, activation, scope and resulting artifacts with exact input provenance | Evaluate a skill or harness change |
| `ci-repair` | Diagnose and repair a concrete failed CI run; distinguish local and hosted results | Fix failing CI checks or pipeline jobs |
| `consult` | Read-only, fresh-context opinion from a different actual model, reconciled and verified by the current agent | Consult another or a named model; second opinion from one |
| `project-catchup` | Read-only return briefing: roadmap/WIP, relevant collaborator changes since a baseline, orientation to named areas | Return to a project after time away; not retrospectives or plain explanations |
| `handoff` | Portable task state tied to actual revision, evidence and authority | Explicit selection |
| `ship` | Precisely authorized publication and mandatory Claude review of Codex changes | Explicit selection |
| `deploy-verify` | Verify an already-triggered deployment and requested bounded monitoring | Explicit selection |

CPO/CTO are broader mandates than decision-review. They can produce finished
work and execute when that action is authorized; their titles alone grant no
permission to edit, publish, contact customers, provision resources, or spend.
A review/decision memo stays within its requested scope. Decision-review also
retains office-hours brainstorming: explore ideas collaboratively, adapt to
business versus learning/fun goals, and narrow only when the user wants to.
An exploratory conversation need not produce a go/no-go verdict.

The owner approved the three additional shortcuts (`browser-qa`, `skill-eval`,
`ci-repair`) after the initial ten-skill reconciliation. They are additions
to the final catalog, not extra names in the immutable source snapshots.
The owner later added `consult`: it recovers `graph-workflow`’s fresh-context
consultation of a different model for material decisions as one read-only
step, without the graph, fixed model table or panels.
The owner also requested `learn-by-building`, a new skill with no source
predecessor.
`project-catchup` subsequently reworks the old weekly-review/retro use case into
a return-to-project briefing with an explicit baseline and personal scope.

The four inherited opt-in contracts remain opt-in. Selection and publication
are separate: invoking `ship` does not create authority beyond the request.
Mandatory Claude review before shipping Codex-written changes also belongs in
the shared agreements so ordinary publication paths cannot bypass it.

## Every source entry and its destination

There are **50 distinct entry names across the four snapshots**, including the
Claude alias `evidence-review`; the `main`/September union is 46. The root `geo`
is listed separately. “Both” means present in each client’s registry, including
shared-directory links. A dash means absent. Name links point to the exact
source file, preferring September when present; presence columns preserve the
other source memberships. Destination names are semantic migrations, not
installed compatibility aliases. “Direct” means an ordinary authorized task,
without a separate harness skill.

| Source entry | Main | September | #4 | #5 | Integrated destination |
|---|---|---|---|---|---|
| [benchmark](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/benchmark/SKILL.md) | Both | Both | — | — | `review` → [performance reference](../shared-skills/review/references/benchmark.md); comparable baselines and complete samples. |
| [browse](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/browse/SKILL.md) | Both | Both | Both | — | Direct browser tasks; rendered evidence and unavailable signals in `review`. |
| [canary](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/canary/SKILL.md) | — | Both | — | — | `deploy-verify` → [monitoring reference](../shared-skills/deploy-verify/references/monitor.md); retain explicit baselines and bounded observation. |
| [careful](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/careful/SKILL.md) | Claude | Claude | Claude | — | Deferred optional hook; repair and test actual client enforcement before adoption. |
| [ceo-review](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/ceo-review/SKILL.md) | Both | — | — | — | `decision-review` → viability, opportunity cost, reversibility, stop criteria. |
| [checkpoint](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/checkpoint/SKILL.md) | Both | Both | — | — | `handoff`; export/recovery on request, without continuous checkpoint ceremony. |
| [code-check](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/code-check/SKILL.md) | Both | Both | Both | — | `review`; actual diff, untracked additions, relevant consumers and evidence. |
| [codebase-design](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/codebase-design/SKILL.md) | Both | — | Both | — | `cto` for a technical mandate; optional module/interface guidance in [templates](templates.md). |
| [codex-implement](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/codex-implement/SKILL.md) | Claude | Claude | Claude | — | Direct cross-client delegation when requested; precise scope and independent Claude review before shipping Codex changes. |
| [codify](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/codify/SKILL.md) | Both | Both | Both | — | Direct scripting task; stage and check behavior/fixtures before authorized installation. |
| [cpo](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/cpo/SKILL.md) | — | Both | — | — | **Keep `cpo`**: product strategy, positioning/pricing, adoption, marketing/growth and authorized execution. |
| [cpo-review](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/cpo-review/SKILL.md) | Both | — | — | — | `decision-review` for one initiative; `cpo` for the broader product mandate. |
| [cso](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/cso/SKILL.md) | — | Both | — | — | `review` → [security reference](../shared-skills/review/references/security.md); complete exploit conditions and concrete evidence. |
| [cto](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/cto/SKILL.md) | — | Both | — | — | **Keep `cto`**: technical direction, architecture, operations, cost, debt, priorities and authorized execution. |
| [cto-review](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/cto-review/SKILL.md) | Both | — | — | — | `decision-review` for one initiative; `cto` for broader technical leadership. |
| [decision-review](https://github.com/geokoko/agent-harness/blob/ba9da80de697b922ae4f94a098ecb8ee8a794869/shared-skills/decision-review/SKILL.md) | — | — | Both | — | **Keep `decision-review`** from #4, with office-hours exploration; use a decision memo when a verdict is requested. |
| [deploy-verify](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/deploy-verify/SKILL.md) | Both | Both | — | Both | **Keep `deploy-verify`**: exact environment and deployed revision; verification does not authorize deployment. |
| [design-consult](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/design-consult/SKILL.md) | Both | Both | — | — | `ui-design`: coherent direction, concrete tokens, existing brand/components and reusable design documentation when useful. |
| [design-review](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/design-review/SKILL.md) | Both | Both | Both | — | `review` → [visual reference](../shared-skills/review/references/visual.md) for audits; `ui-design` for authorized polish. Render relevant states and separate observations from taste. |
| [devex-review](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/devex-review/SKILL.md) | Both | Both | — | — | `review` → [onboarding reference](../shared-skills/review/references/devex.md); exercise the setup path and report measured friction. |
| [document-generate](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/document-generate/SKILL.md) | Both | Both | — | — | `docs-update`: actually create or update requested docs; choose the needed form, ground claims in behavior and connect navigation. |
| [document-release](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/document-release/SKILL.md) | Both | Both | — | — | `docs-update`: update changed/new surfaces and release notes; accurate unreleased/released/deployed state, no automatic commits or publication. |
| [domain-modeling](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/domain-modeling/SKILL.md) | Both | — | Both | — | Project glossary and selective ADRs; optional [templates](templates.md), no new standing skill. |
| [dual-agent-software-engineering](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/dual-agent-software-engineering/SKILL.md) | Both | Both | — | — | Native delegation plus `handoff`/`review`/`ship`; retain revision-specific evidence, not six compulsory phases. |
| [engineering-weekly-review](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/engineering-weekly-review/SKILL.md) | Both | — | — | — | `project-catchup` for recovered roadmap/WIP, relevant changes and requested new-area orientation; period retrospectives remain direct requests with an explicit period, verified totals and committed versus shipped distinction. |
| [evidence-review](https://github.com/geokoko/agent-harness/blob/1938949977101c403e002037ad73e7401f08203c/claude-skills/evidence-review/SKILL.md) | — | — | — | Claude | **Claude discovery name for `review`**; avoids colliding with the client command. |
| [exec-review](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/claude-skills/exec-review/SKILL.md) | Both | — | — | — | `decision-review`; selected lenses and explicit disagreements, no standing executive panel. |
| [freeze](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/freeze/SKILL.md) | Claude | Claude | Claude | — | Deferred optional hook; repair symlink/path handling and test enforcement before adoption. |
| [graph-workflow](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/graph-workflow/SKILL.md) | Claude | Both | Claude | — | Retire the fixed graph/runtime; preserve useful delegation and evidence contracts below. |
| [guard](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/guard/SKILL.md) | Claude | Claude | — | — | Retire wrapper; hooks are not adopted or silently replaced by native permissions. |
| [handoff](https://github.com/geokoko/agent-harness/blob/1938949977101c403e002037ad73e7401f08203c/claude-skills/handoff/SKILL.md) | — | — | — | Both | **Keep `handoff`** from #5: portable, revision-specific task state and authority. |
| [health](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/health/SKILL.md) | Both | Both | — | — | Requested `review` or `cto` assessment with actual checks; no invented aggregate scores or state protocol. |
| [investigate](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/investigate/SKILL.md) | Both | Both | — | — | Direct debugging task; reproduce and fix the cause within scope, no fixed hypothesis count. |
| [note-creation](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/note-creation/SKILL.md) | Both | Both | — | Both | **Keep `note-creation`**: source fidelity, complete requested coverage, worked notes and rendered PDF checks. |
| [office-hours](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/office-hours/SKILL.md) | Both | Both | Both | — | `decision-review` preserves open-ended brainstorming, idea pressure-testing and learning/hackathon/weekend builder mode; adaptive questions and no compulsory verdict. `cpo` handles broader product delivery. |
| [plan](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/plan/SKILL.md) | Both | Both | Both | — | Direct planning task plus optional [template](templates.md); planning alone does not authorize edits. |
| [plan-review](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/plan-review/SKILL.md) | Both | Both | — | — | `decision-review` for scope/feasibility; `review` for code-grounded findings where relevant. |
| [post-deploy-monitor](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/claude-skills/post-deploy-monitor/SKILL.md) | Both | — | — | — | `deploy-verify` → [monitoring reference](../shared-skills/deploy-verify/references/monitor.md); same destination as September’s `canary`. |
| [qa](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/qa/SKILL.md) | Both | Both | — | — | `browser-qa` for actual browser journeys and requested regression tests/fixes; `review` → [behavioral reference](../shared-skills/review/references/behavior.md) for assessments. Distinguish executed and untested coverage. |
| [resolving-merge-conflicts](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/claude-skills/resolving-merge-conflicts/SKILL.md) | Both | — | Both | — | Direct resolution request; preserve both intents and unrelated work, no automatic publication. |
| [retro](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/retro/SKILL.md) | — | Both | — | — | `project-catchup` for returning to work; same destination as `engineering-weekly-review`. Period retrospectives remain direct requests. |
| [review](https://github.com/geokoko/agent-harness/blob/1938949977101c403e002037ad73e7401f08203c/shared-skills/review/SKILL.md) | — | — | — | Codex | **Keep `review`** from #5, strengthened by selected #4/September evidence requirements. |
| [scrape](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/scrape/SKILL.md) | Both | Both | Both | — | Direct extraction task; requested schema, one validated JSON document when requested, honest incomplete results. |
| [security-audit](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/claude-skills/security-audit/SKILL.md) | Both | — | Both | — | `review` → [security reference](../shared-skills/review/references/security.md); same destination as September’s `cso`. |
| [ship](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/ship/SKILL.md) | Both | Both | Both | Both | **Keep `ship`** with mandatory Claude review before shipping Codex changes and explicit publication authority. |
| [spec](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/spec/SKILL.md) | Both | Both | — | — | Direct specification task plus optional [template](templates.md); observable acceptance criteria. |
| [test-first-development](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/test-first-development/SKILL.md) | Both | — | Both | — | Requested TDD mode plus optional [testing guidance](templates.md); no universal test-seam approval gate. |
| [to-tickets](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/claude-skills/to-tickets/SKILL.md) | Both | — | — | — | Direct ticket drafting plus optional [template](templates.md); vertical slices and dependencies, separate publication authority. |
| [unfreeze](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/unfreeze/SKILL.md) | Claude | Claude | — | — | Retire active command; any existing hook configuration/state requires deliberate migration. |
| [wayfinder](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/claude-skills/wayfinder/SKILL.md) | Both | — | — | — | Normal continuation and requested `handoff`; no second task-state or decision-map protocol. |
| [root `geo`](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/SKILL.md) | Claude | Claude | Claude | — | Shared working agreements plus native discovery; remove router and fixed model table. |

## September contracts beyond skill names

The September branch added real correctness and scope work. Removing its graph
entry must not erase these lessons. The following are retained as instructions
or optional references; removed runtime formats are not claimed to be supported.

| September material | Retained in the integrated design | Retired or limited |
|---|---|---|
| [CPO skill and references](https://github.com/geokoko/agent-harness/tree/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/cpo) | Product evidence, pricing/positioning, activation, finished campaign work, denominators/cohorts, authority and observed delivery states | Fixed model recommendations and automatic graph handoff |
| [CTO skill and lenses](https://github.com/geokoko/agent-harness/tree/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/cto) | Architecture/readiness, measured capacity/cost, recovery proof, delivery capacity, debt and build-versus-buy | Model ladder and dependencies on retired specialist commands |
| [Shared engineering graph](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/graph-workflow/references/engineering.md) and [phase contract](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/dual-agent-software-engineering/references/phases.md) | `handoff`/`review`/`ship`: exact revision including uncommitted patch identity, existing authority, owned paths, independent review, affected-check reuse and explicit incomplete evidence | Mandatory phases, fixed node count, model/effort ladder, compulsory panel and vote counts |
| [Sweep contract](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/shared-skills/graph-workflow/references/sweep.md) | `review`: verify claims and counterexamples, deduplicate by claim, account for fixes already in flight; ordinary implementation: serialize shared writes and preserve source checkout | Campaign grouping thresholds, automatic draft-PR terminal, routing journals, profile census, history-shaping node, `preVerified`/`alreadyFixed`/`repairNotes`/`ship:false` protocol |
| [Official-CLI launcher](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/scripts/claude-graph), [Codex adapter](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/codex/workflows/graph-workflow.md), [Claude runtime](https://github.com/geokoko/agent-harness/tree/128efe0edf1418958e473f384694ea9358b6c435/claude-skills/graph-workflow-runtime) | Delegation/handoff: no recursive coordinator bounce; exit failures, permission denials, missing artifacts and stale revision evidence remain failures; local/report/publication scope stays explicit | Executable graph adapters, persistent runtime schemas and helper launchers are not ported or installed |
| [Tuning and defect ledger](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/docs/skill-tuning.md) | `review`: verified diff base, untracked additions, required-versus-executed QA, explicit unavailable browser signals, complete security preconditions; performance: bounded samples, missing values stay missing | Historical fixture passes are source evidence, not a passing test result for this candidate |
| Course-source classification in the same ledger | `note-creation`: lecture/exam/mixed is determined by content; extraction quality selects the reading method; missing exam weighting stays unknown | Do not infer importance from scan quality or invent past-exam frequency |
| Non-review output contracts in the same ledger | Direct work: validate requested extraction schema; aggregate the requested retrospective period; preserve failure status; carry authority without repeat approval | No automatic global stores for extraction, health, retrospective, or benchmark state |
| Hook fixes and tests in the same branch | Preserve the source history and recognize hooks as a distinct optional feature | Hooks remain deferred; source tests alone do not establish reliable path/command parsing or live client enforcement |
| [tmux guide](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/codex/workflows/tmux-agents.md) | Short optional [operational guide](tmux-workflow.md): visible independent sessions, explicit handoffs, isolated concurrent editors | Permanent role roster, custom window helper and automatic launches |

Preserve existing `.agent-team`, `~/.geo`, checkpoint, graph, benchmark and
monitoring records in their existing locations. A requested handoff may inspect
selected legacy evidence and reconcile it with current state. It must not infer
new authority from those records, replay obsolete runtime state, or silently
delete or convert them. The installers do not prune retired links.

## What the evaluations establish

PR #5’s historical runs evaluate the old/native/#5 configurations, including
Claude running #5. They do not compare #4 against #5, do not evaluate the
September branch as a complete candidate, and do not evaluate this integrated
catalog. Keep that distinction when interpreting success rates and costs.
Structural/installer checks establish their tested contracts only. New model
behavior, live hook enforcement and production readiness require their own
relevant evidence. Record exact input snapshots and regrade when graded inputs
change; a stored grade is not evidence for modified output.

The integrated branch is reviewed before its authorized publication as a new PR.
Follow [migration guidance](skill-migration.md) only when the user
requests installation; do not switch the installed source checkout as a shortcut.
