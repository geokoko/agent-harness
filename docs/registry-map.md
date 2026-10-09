# Complete registry reconciliation

This is the migration map for the integrated rebuild. It
reconciles both development lines and both rebuild proposals. It is not an
installation record or a claim that these changes are merged, published, or
active in either client. Existing installed links and legacy artifacts remain
outside this candidate’s changes.

## Source versions

The integrated catalog reconciles four earlier versions of this harness. Their
sources predate the published history; the counts below were taken from fixed
snapshots of each.

| Source version | What it was | Claude entries | Codex entries |
|---|---|---:|---:|
| August harness (2026-08-23) | The cross-client harness both rebuilds started from: a broad specialist catalog behind a root `geo` router, with shared sources and a 35-skill parity contract | 41 + root `geo` | 35 |
| September tuning line (2026-09-12) | A parallel line that tuned model roles and effort, coordinated Claude and Codex through graph workflows, and added full CPO and CTO skills | 33 + root `geo` | 28 |
| Claude modernization proposal (2026-09-29) | Cut about 35 skills to 18 and deleted the router and role prompts | 18 + root `geo` | 14 |
| Codex native rebuild (2026-09-30) | Rebuilt the harness around native client capabilities: shared contracts, thin client adapters and dry-run installers | 5 | 5 |

The August and September lines split from the same June starting point; the
August line then gained 7 changes of its own and the September line 43. Change
counts describe ancestry, not the amount of unique functionality. Both rebuild
proposals started from the August line; the September line is not their
ancestor. Its full `cpo` and `cto` work therefore required explicit
incorporation. Its `canary`, `cso`, and `retro` names are accounted for
alongside the August line's corresponding longer names below.

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
| `agents-md-modernizer` | Reduce repository agent-instruction files to non-inferable project constraints, with verified commands/paths and a disposition report | Audit, simplify or modernize AGENTS.md, CLAUDE.md or related instruction files |
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
to the final catalog, not extra names in the source versions.
The owner later added `consult`: it recovers `graph-workflow`’s fresh-context
consultation of a different model for material decisions as one read-only
step, without the graph, fixed model table or panels.
The owner also requested `learn-by-building`, a new skill with no source
predecessor.
`project-catchup` subsequently reworks the old weekly-review/retro use case into
a return-to-project briefing with an explicit baseline and personal scope.
`agents-md-modernizer` is likewise new, with no source predecessor.

The four inherited opt-in contracts remain opt-in. Selection and publication
are separate: invoking `ship` does not create authority beyond the request.
Mandatory Claude review before shipping Codex-written changes also belongs in
the shared agreements so ordinary publication paths cannot bypass it.

## Every source entry and its destination

There are **50 distinct entry names across the four versions**, including the
Claude alias `evidence-review`; the August/September union is 46. The root `geo`
is listed separately. “Both” means present in each client’s registry, including
shared-directory links. A dash means absent. “What it did” summarizes the
entry's own description, taken from the September line where it existed there.
Destination names are semantic migrations, not installed compatibility aliases.
“Direct” means an ordinary authorized task, without a separate harness skill.

| Source entry | What it did | August | September | Claude proposal | Codex rebuild | Integrated destination |
|---|---|---|---|---|---|---|
| `benchmark` | Browser load-time and bundle-size regression checks against a stored baseline | Both | Both | — | — | `review` → [performance reference](../shared-skills/review/references/benchmark.md); comparable baselines and complete samples. |
| `browse` | Drive a web app in a real browser (connected Chrome, else headless Playwright) | Both | Both | Both | — | Direct browser tasks; rendered evidence and unavailable signals in `review`. |
| `canary` | Watch a live app after a deploy against a pre-deploy baseline | — | Both | — | — | `deploy-verify` → [monitoring reference](../shared-skills/deploy-verify/references/monitor.md); retain explicit baselines and bounded observation. |
| `careful` | Hook warning before destructive commands such as `rm -rf` or force-push | Claude | Claude | Claude | — | Deferred optional hook; repair and test actual client enforcement before adoption. |
| `ceo-review` | Fund, test, defer or kill a company initiative | Both | — | — | — | `decision-review` → viability, opportunity cost, reversibility, stop criteria. |
| `checkpoint` | Save and restore working context across sessions and machines | Both | Both | — | — | `handoff`; export/recovery on request, without continuous checkpoint ceremony. |
| `code-check` | Code review of committed and uncommitted changes | Both | Both | Both | — | `review`; actual diff, untracked additions, relevant consumers and evidence. |
| `codebase-design` | Deep modules, small interfaces and testable seams | Both | — | Both | — | `cto` for a technical mandate; optional module/interface guidance in [templates](templates.md). |
| `codex-implement` | Delegate specified implementation to Codex, with layered Claude review | Claude | Claude | Claude | — | Direct cross-client delegation when requested; precise scope and independent Claude review before shipping Codex changes. |
| `codify` | Freeze a flow that just worked into a script, fixture and test | Both | Both | Both | — | Direct scripting task; stage and check behavior/fixtures before authorized installation. |
| `cpo` | Product-lead mandate for strategy and marketing/growth | — | Both | — | — | **Keep `cpo`**: product strategy, positioning/pricing, adoption, marketing/growth and authorized execution. |
| `cpo-review` | Product review of one initiative: problem, scope, adoption, outcome | Both | — | — | — | `decision-review` for one initiative; `cpo` for the broader product mandate. |
| `cso` | OWASP Top 10 and STRIDE security audit | — | Both | — | — | `review` → [security reference](../shared-skills/review/references/security.md); complete exploit conditions and concrete evidence. |
| `cto` | Technical-lead mandate for engineering strategy or a bounded CTO review | — | Both | — | — | **Keep `cto`**: technical direction, architecture, operations, cost, debt, priorities and authorized execution. |
| `cto-review` | Technical strategy, sequencing and build-versus-buy review of one initiative | Both | — | — | — | `decision-review` for one initiative; `cto` for broader technical leadership. |
| `decision-review` | One decision memo from selectable viability, product and technical lenses | — | — | Both | — | **Keep `decision-review`** from the Claude proposal, with office-hours exploration; use a decision memo when a verdict is requested. |
| `deploy-verify` | Detect the deploy platform, wait for a deploy and verify the live site | Both | Both | — | Both | **Keep `deploy-verify`**: exact environment and deployed revision; verification does not authorize deployment. |
| `design-consult` | Interview, then propose a design system recorded in `DESIGN.md` | Both | Both | — | — | `ui-design`: coherent direction, concrete tokens, existing brand/components and reusable design documentation when useful. |
| `design-review` | Screenshot-based design audit with an optional fix pass | Both | Both | Both | — | `review` → [visual reference](../shared-skills/review/references/visual.md) for audits; `ui-design` for authorized polish. Render relevant states and separate observations from taste. |
| `devex-review` | Live developer-experience audit of an API, CLI, SDK or docs | Both | Both | — | — | `review` → [onboarding reference](../shared-skills/review/references/devex.md); exercise the setup path and report measured friction. |
| `document-generate` | Generate Diataxis documentation for a feature or module | Both | Both | — | — | `docs-update`: actually create or update requested docs; choose the needed form, ground claims in behavior and connect navigation. |
| `document-release` | Update docs to match a completed feature or diff | Both | Both | — | — | `docs-update`: update changed/new surfaces and release notes; accurate unreleased/released/deployed state, no automatic commits or publication. |
| `domain-modeling` | Project terminology, domain scenarios, `CONTEXT.md` and ADRs | Both | — | Both | — | Project glossary and selective ADRs; optional [templates](templates.md), no new standing skill. |
| `dual-agent-software-engineering` | Claude Code and Codex as independent agents through fixed phases | Both | Both | — | — | Native delegation plus `handoff`/`review`/`ship`; retain revision-specific evidence, not six compulsory phases. |
| `engineering-weekly-review` | Weekly engineering summary from Git evidence | Both | — | — | — | `project-catchup` for recovered roadmap/WIP, relevant changes and requested new-area orientation; period retrospectives remain direct requests with an explicit period, verified totals and committed versus shipped distinction. |
| `evidence-review` | Claude entry name for the evidence and report-only review contract | — | — | — | Claude | **Claude discovery name for `review`**; avoids colliding with the client command. |
| `exec-review` | Combined CEO, CPO and CTO panel producing one decision memo | Both | — | — | — | `decision-review`; selected lenses and explicit disagreements, no standing executive panel. |
| `freeze` | Hook restricting edits to one directory for the session | Claude | Claude | Claude | — | Deferred optional hook; repair symlink/path handling and test enforcement before adoption. |
| `graph-workflow` | Claude and Codex engineering through a dependency graph, or a bounded defect sweep | Claude | Both | Claude | — | Retire the fixed graph/runtime; preserve useful delegation and evidence contracts below. |
| `guard` | `careful` and `freeze` together | Claude | Claude | — | — | Retire wrapper; hooks are not adopted or silently replaced by native permissions. |
| `handoff` | Export or recover a provider-neutral task handoff | — | — | — | Both | **Keep `handoff`** from the Codex rebuild: portable, revision-specific task state and authority. |
| `health` | Scored code-quality dashboard with local trend history | Both | Both | — | — | Requested `review` or `cto` assessment with actual checks; no invented aggregate scores or state protocol. |
| `investigate` | Root-cause debugging before any fix | Both | Both | — | — | Direct debugging task; reproduce and fix the cause within scope, no fixed hypothesis count. |
| `note-creation` | Exam-focused study notes from course materials and past papers | Both | Both | — | Both | **Keep `note-creation`**: source fidelity, complete requested coverage, worked notes and rendered PDF checks. |
| `office-hours` | Product brainstorming and idea pressure-testing before code | Both | Both | Both | — | `decision-review` preserves open-ended brainstorming, idea pressure-testing and learning/hackathon/weekend builder mode; adaptive questions and no compulsory verdict. `cpo` handles broader product delivery. |
| `plan` | Architecture and implementation plan before code | Both | Both | Both | — | Direct planning task plus optional [template](templates.md); planning alone does not authorize edits. |
| `plan-review` | Review a plan through scope, engineering, design and DX lenses | Both | Both | — | — | `decision-review` for scope/feasibility; `review` for code-grounded findings where relevant. |
| `post-deploy-monitor` | Compare production with a pre-deploy baseline after a deploy | Both | — | — | — | `deploy-verify` → [monitoring reference](../shared-skills/deploy-verify/references/monitor.md); same destination as September’s `canary`. |
| `qa` | Report-only tester pass over current changes | Both | Both | — | — | `browser-qa` for actual browser journeys and requested regression tests/fixes; `review` → [behavioral reference](../shared-skills/review/references/behavior.md) for assessments. Distinguish executed and untested coverage. |
| `resolving-merge-conflicts` | Resolve an in-progress merge or rebase by both sides' intent | Both | — | Both | — | Direct resolution request; preserve both intents and unrelated work, no automatic publication. |
| `retro` | Weekly retrospective from commit history | — | Both | — | — | `project-catchup` for returning to work; same destination as `engineering-weekly-review`. Period retrospectives remain direct requests. |
| `review` | Evidence and report-only review contract | — | — | — | Codex | **Keep `review`** from the Codex rebuild, strengthened by selected evidence requirements from the Claude proposal and the September line. |
| `scrape` | Read-only page-data extraction into one JSON document | Both | Both | Both | — | Direct extraction task; requested schema, one validated JSON document when requested, honest incomplete results. |
| `security-audit` | OWASP Top 10 and STRIDE audit with quote-verified findings | Both | — | Both | — | `review` → [security reference](../shared-skills/review/references/security.md); same destination as September’s `cso`. |
| `ship` | Pre-push checklist, then push and PR creation | Both | Both | Both | Both | **Keep `ship`** with mandatory Claude review before shipping Codex changes and explicit publication authority. |
| `spec` | Turn vague intent into a backlog-ready issue specification | Both | Both | — | — | Direct specification task plus optional [template](templates.md); observable acceptance criteria. |
| `test-first-development` | One vertical slice at a time, red-green-refactor | Both | — | Both | — | Requested TDD mode plus optional [testing guidance](templates.md); no universal test-seam approval gate. |
| `to-tickets` | Split a plan into small vertical tickets with dependencies | Both | — | — | — | Direct ticket drafting plus optional [template](templates.md); vertical slices and dependencies, separate publication authority. |
| `unfreeze` | Remove the `freeze` boundary | Claude | Claude | — | — | Retire active command; any existing hook configuration/state requires deliberate migration. |
| `wayfinder` | Map large, uncertain work as decision tickets on the issue tracker | Both | — | — | — | Normal continuation and requested `handoff`; no second task-state or decision-map protocol. |
| root `geo` | Personal preferences and the router to the other `geo` skills | Claude | Claude | Claude | — | Shared working agreements plus native discovery; remove router and fixed model table. |

## September contracts beyond skill names

The September tuning line added real correctness and scope work. Removing its graph
entry must not erase these lessons. The following are retained as instructions
or optional references; removed runtime formats are not claimed to be supported.

| September material | Retained in the integrated design | Retired or limited |
|---|---|---|
| CPO skill and references | Product evidence, pricing/positioning, activation, finished campaign work, denominators/cohorts, authority and observed delivery states | Fixed model recommendations and automatic graph handoff |
| CTO skill and lenses | Architecture/readiness, measured capacity/cost, recovery proof, delivery capacity, debt and build-versus-buy | Model ladder and dependencies on retired specialist commands |
| Shared engineering graph and the dual-agent phase contract | `handoff`/`review`/`ship`: exact revision including uncommitted patch identity, existing authority, owned paths, independent review, affected-check reuse and explicit incomplete evidence | Mandatory phases, fixed node count, model/effort ladder, compulsory panel and vote counts |
| Graph-workflow defect-sweep contract | `review`: verify claims and counterexamples, deduplicate by claim, account for fixes already in flight; ordinary implementation: serialize shared writes and preserve source checkout | Campaign grouping thresholds, automatic draft-PR terminal, routing journals, profile census, history-shaping node, `preVerified`/`alreadyFixed`/`repairNotes`/`ship:false` protocol |
| Graph launcher for the official Claude CLI, the Codex graph adapter and the Claude graph runtime | Delegation/handoff: no recursive coordinator bounce; exit failures, permission denials, missing artifacts and stale revision evidence remain failures; local/report/publication scope stays explicit | Executable graph adapters, persistent runtime schemas and helper launchers are not ported or installed |
| Skill-tuning and defect ledger | `review`: verified diff base, untracked additions, required-versus-executed QA, explicit unavailable browser signals, complete security preconditions; performance: bounded samples, missing values stay missing | Historical fixture passes are source evidence, not a passing test result for this candidate |
| Course-source classification in the same ledger | `note-creation`: lecture/exam/mixed is determined by content; extraction quality selects the reading method; missing exam weighting stays unknown | Do not infer importance from scan quality or invent past-exam frequency |
| Non-review output contracts in the same ledger | Direct work: validate requested extraction schema; aggregate the requested retrospective period; preserve failure status; carry authority without repeat approval | No automatic global stores for extraction, health, retrospective, or benchmark state |
| Hook fixes and tests from the same line | Recognize hooks as a distinct optional feature; the fixes and tests themselves were not carried over | Hooks remain deferred; source tests alone do not establish reliable path/command parsing or live client enforcement |
| Guide to running agents in tmux windows | Short optional [operational guide](tmux-workflow.md): visible independent sessions, explicit handoffs, isolated concurrent editors | Permanent role roster, custom window helper and automatic launches |

Preserve existing `.agent-team`, `~/.geo`, checkpoint, graph, benchmark and
monitoring records in their existing locations. A requested handoff may inspect
selected legacy evidence and reconcile it with current state. It must not infer
new authority from those records, replay obsolete runtime state, or silently
delete or convert them. The installers do not prune retired links.

## What the evaluations establish

The historical runs evaluated the August harness, native behavior and the Codex
rebuild, including Claude running the rebuild. They do not compare the Claude
proposal against the Codex rebuild, do not evaluate the September line as a
complete candidate, and do not evaluate this integrated catalog. Keep that distinction when interpreting success rates and costs.
Structural/installer checks establish their tested contracts only. New model
behavior, live hook enforcement and production readiness require their own
relevant evidence. Record exact input snapshots and regrade when graded inputs
change; a stored grade is not evidence for modified output.

The integrated catalog was reviewed before publication.
Follow [migration guidance](skill-migration.md) only when the user
requests installation; do not switch the installed source checkout as a shortcut.
