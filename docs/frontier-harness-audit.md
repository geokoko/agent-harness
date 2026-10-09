# Frontier harness audit

> Historical evidence from the Codex native rebuild. These results do not evaluate
> the October integrated candidate or the September tuning line. See the [current registry map](registry-map.md)
> and [build evidence](build-evidence.md).

Audited against the August harness; official
documentation checked on **2026-09-29**. The baseline is versioned Markdown,
symlink registries and shell helpers, not an agent runtime. The rewrite keeps
that boundary. The audited implementations are described here; their sources are
not part of the published repository.

## Evidence and its limits

These sources identify assumptions to test. Vendor evaluations are not results
on this repository's tasks. API support does not establish a feature's presence
in an installed CLI, account or session.

| Current capability | Opened primary evidence | Old harness assumption affected | Architectural implication |
|---|---|---|---|
| Astra selects relevant repository reads and ordinarily checks its work | [OpenAI, Sep 11: Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Every edit needs full exploration, a planning recipe and repeated test reminders | Remove generic procedures and mandatory first-action routing; preserve non-obvious facts and completion criteria. |
| Strong instruction following can turn old caution into unnecessary stops | [GPT-6 guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra) | Additional approval stages always improve reliability | Express actual authority and stopping conditions; remove invented intermediate approvals. |
| Both clients discover skill metadata before loading bodies | [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude skills](https://code.claude.com/docs/en/skills) | A global router and matching taxonomies are necessary | Use native discovery and short distinct triggers. Large listings truncate descriptions; invoked bodies still consume context. |
| Native invocation policy can make a skill opt-in | [Codex policy](https://learn.chatgpt.com/docs/build-skills), [Claude invocation control](https://code.claude.com/docs/en/skills) | Every reusable instruction should be automatically activated | Use provider metadata when needed; Claude's user-only setting also removes its description from initial context. No parity requirement. |
| Native subagents isolate context and parallelize independent tasks | [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude subagents](https://code.claude.com/docs/en/sub-agents) | Roles, dispatch graphs and cross-vendor panels are prerequisites | Delegate bounded outcomes when useful; do not prescribe a topology. Codex's proactive delegation depends on mode and instructions. |
| Teams incur coordination and token costs | [Claude teams](https://code.claude.com/docs/en/agent-teams) | More agents always improve coverage | Prefer direct execution for sequential or coupled work. Evaluate optional independent review separately. |
| Opus 5.5 sustains longer coding work; effort calibration changes | [Opus 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | Stage-specific models and effort ladders remain calibrated | Inherit native session selection; compare effort settings on tasks rather than preserve model folklore. |
| Sonnet 5.5 can over-review at high effort and skip checks at low effort | [Sonnet 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) | One fixed review procedure suits every model | Keep concise observable completion criteria. Anthropic reports lower cost without quality loss from suppressing extra reviewer rounds in its max-effort coding tests; low-effort verification remains a limitation to test. |
| A formerly necessary context-reset mechanism became obsolete after a model upgrade | [Anthropic: Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) | Manual resets and recurring checkpoints are intrinsic requirements | Anthropic's Sonnet 4.5 context-anxiety workaround was unnecessary with Opus 4.5. Native continuation is the default; portable handoffs serve a different need. |
| Clients already own history, compaction and worktree isolation | [Claude operation](https://code.claude.com/docs/en/how-claude-code-works), [Claude workflows](https://code.claude.com/docs/en/common-workflows), [Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) | This repository needs a session framework or tmux coordination protocol | Remove competing state machinery and launcher workflows. Git worktrees isolate edits, not credentials or all side effects. |
| Native permission layers enforce execution boundaries | [Codex permissions](https://learn.chatgpt.com/docs/permissions), [Codex hooks](https://learn.chatgpt.com/docs/hooks), [Claude hooks](https://code.claude.com/docs/en/hooks) | Safety prose or shell-pattern hooks provide complete protection | Use effective sandbox, tool approvals and service credentials. Hook coverage is incomplete and provider schemas differ. |
| Hosts provide tool discovery, composition and caching | [OpenAI tool search](https://developers.openai.com/api/docs/guides/tools-tool-search), [programmatic calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling), [caching](https://developers.openai.com/api/docs/guides/prompt-caching), [Claude tool context](https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context) | Repository routing and cache choreography are necessary | Use exposed host capabilities. Caching reduces repeated-token cost, not context occupancy. Add no tool server or API loop. |

## Architecture before

The baseline exposed **35 common logical skills, six additional Claude skills,
and the `geo` root router: 42 entrypoints overall**. Eight shared sources had
relative registry links; 27 common names had separate client implementations.
Native loaders already disclosed skill bodies progressively. The router was
itself a skill, not proof that its entire body loaded on every turn.

When invoked, `geo` added environment preferences, forced matching skills as the
first action, and presented an idea-to-production chain. Separate planning,
executive and review families expanded that chain. Six Codex roles, a tmux
workflow, Claude-to-Codex implementation and a six-phase dual-agent protocol
coexisted with the graph workflow. The graph prescribed discovery fleets,
deduplication, refuters, voting, triage, per-file fixes, repair and acceptance,
gates, synthesis, routing scores, campaign state and publication.

Clients supplied the actual models, tools, MCP integrations, histories,
compaction, retrieval and permissions. The repository supplied no MCP server,
tool schema, vector store, compactor, cache service, scheduler or agent loop.
Its state formats accumulated beside those native systems: checkpoints,
benchmarks, health scores, deployment baselines, decision tickets, `.agent-team`
artifacts and graph histories. Validation primarily checked installation,
frontmatter, links, parity and hook examples; it did not establish model quality.

## Explicit skill deletion table

Costs below are **exact baseline `SKILL.md` source bytes, including frontmatter**,
read from Git, not estimated tokens or permanent-context costs. `C / X` means
Claude / Codex; `S` means one shared source, counted once; `C` alone means
Claude-only. Resources and scripts are accounted for separately below. The
table includes every baseline skill, including `geo`.

| Component | Why it exists | Still-needed failure mode? | Source bytes | Decision | Replacement |
|---|---|---|---:|---|---|
| `geo` root router | Stack context and intent routing | Native discovery already routes; stale environment facts and forced first action can interfere | C 4,439 | DELETE | Compact preferences plus native discovery; no main workflow. |
| `benchmark` | Repeatable performance comparison | Comparable samples and baseline promotion are precise reusable invariants | 4,574 / 2,279 | MERGE | Optional `review` reference for samples, provenance and baseline handling. |
| `browse` | Browser inspection and evidence | Real rendered evidence matters; tool contract already owns interaction semantics | 3,209 / 2,093 | REPLACE_WITH_NATIVE_FEATURE | Native browser or installed project tests; requested review lens. |
| `careful` | Warn on destructive shell patterns | Consequential operations still require enforcement; regex coverage is partial | C 1,955 | REPLACE_WITH_DETERMINISTIC_MECHANISM | Native permissions/sandbox/rules; not an equivalent installed replacement. |
| `ceo-review` | Investment and opportunity-cost lens | Explicit decision criteria useful; persona and ceremony unproven | S 2,762 | DELETE | Ask for cost, reversibility, risk and next experiment directly. |
| `checkpoint` | Recover context and task progress | Cross-provider handoff remains useful; ordinary compaction already native | 3,079 / 1,975 | USER_INVOKED_ONLY | Rename to `handoff`; concise portable evidence, no continuous journal. |
| `code-check` | Evidence-grounded, report-only review | User's read-only default and false-positive suppression are worth testing | 5,956 / 2,962 | KEEP_BUT_SHRINK | Rename to `review`; narrow finding contract and optional lenses. |
| `codebase-design` | Deep modules and interface design | Generic engineering knowledge; no repo-specific facts | S 4,290 | DELETE | Agent chooses design; project ADRs hold actual decisions. |
| `codex-implement` | Claude plans while Codex types | Fixed provider hierarchy and approval-bypass launcher are unjustified | C 5,662 | DELETE | Native agent or explicitly requested separate client session. |
| `codify` | Convert a verified flow into a script | Fixtures and output parity matter; ordinary scripting request already expresses outcome | 3,240 / 2,201 | DELETE | Ask for deterministic implementation with representative fixtures. |
| `cpo-review` | Product scope and adoption lens | Criteria useful; separate identity unnecessary | S 2,465 | DELETE | Supply product decision criteria in the task. |
| `cto-review` | Technical strategy and sequencing | Criteria useful; executive role adds no established value | S 2,872 | DELETE | Supply technical risk, cost and reversibility criteria. |
| `deploy-verify` | Verify a precise deployment without triggering one | Publication, live revision and healthy behavior are easily conflated | 4,842 / 2,781 | KEEP_BUT_SHRINK | Explicit verification request; exact revision/environment and evidence. |
| `design-consult` | Coherent design direction and DESIGN.md | No unusual design system or assets supplied by harness | 3,330 / 2,245 | DELETE | Native design capabilities and project-specific design context. |
| `design-review` | Rendered UI audit | Visual evidence is distinct from code review | 6,656 / 3,364 | MERGE | Common `review` evidence contract when selected; native browser supplies visual checks. |
| `devex-review` | Exercise developer onboarding | Fresh-environment execution is a distinct evaluation objective | 3,750 / 2,460 | MERGE | Optional onboarding criteria under `review`. |
| `document-generate` | Repository-grounded documentation | Generic documentation competence; no environment-specific procedure | 4,407 / 2,338 | DELETE | Direct request plus existing documentation conventions. |
| `document-release` | Update docs after behavior changes | Diff-grounded accuracy matters; separate workflow unnecessary | 3,096 / 2,219 | DELETE | Direct documentation task; remove default-branch abort and auto-commit behavior. |
| `domain-modeling` | Shared vocabulary, CONTEXT.md and ADRs | Project vocabulary matters; generic method should not create compulsory artifacts | S 3,392 | DELETE | Repository domain docs when the project actually needs them. |
| `dual-agent-software-engineering` | Owned phases and adversarial review | Independent evaluation sometimes helps; six phases and fixed stops unproven | S 8,752 | REPLACE_WITH_NATIVE_FEATURE | Native delegation; portable handoff for explicit independent work. |
| `engineering-weekly-review` | Git-grounded retrospective | Honest time windows matter; no special service or data source | S 2,793 | DELETE | Direct retrospective request with explicit date range and evidence. |
| `exec-review` | Combined executive panel | Fixed panel duplicates decision criteria and forces coordination | 2,713 / 2,467 | DELETE | One decision memo; request independent input only for a concrete need. |
| `freeze` | Limit Edit/Write to a directory | Write isolation remains necessary; Bash and other tools bypass this hook | C 2,308 | REPLACE_WITH_DETERMINISTIC_MECHANISM | Native filesystem boundaries; no claim of equivalent protection from prose. |
| `graph-workflow` | Autonomous campaign discovery, repair and shipping | Residual defects and coordination failures persist; this full topology lacks current matched evidence | C 39,771 | DELETE | Primary agent with optional bounded native delegation/review; compare through evals. |
| `guard` | Combine careful and freeze | Same genuine enforcement need, same partial coverage | C 2,166 | REPLACE_WITH_DETERMINISTIC_MECHANISM | Native permission policy; remove prompt-activated safety bundle. |
| `health` | Run native checks and produce scores | Actual failures matter; invented composite scores lack calibration | 4,444 / 2,592 | MERGE | Common `review` evidence contract when selected; native checks, no scoring database. |
| `investigate` | Reproduce, hypothesize, instrument and repair | Debugging still needs evidence; 3–5 hypotheses and fixed stop counts constrain judgment | 6,211 / 3,016 | REPLACE_WITH_NATIVE_FEATURE | Native investigation from objective and completion criteria. |
| `note-creation` | Faithful exam notes, scans, equations and worked examples | Concrete personal/domain standards are not inferable from generic coding behavior | 8,295 / 3,605 | MAKE_PROGRESSIVE | Shared specialist skill; source fidelity and optional topic reference. |
| `office-hours` | Challenge ideas and choose an experiment | Useful decision objective; fixed forcing questions and repeated approvals unnecessary | 4,118 / 2,474 | DELETE | Direct brainstorming/decision request. |
| `plan` | Lock architecture through prescribed sections | Model can plan; user may still request a reviewable artifact | 3,714 / 2,731 | REPLACE_WITH_NATIVE_FEATURE | Native plan mode or explicit plan request; no prerequisite to implementation. |
| `plan-review` | Scope, engineering, design and DX challenge | Independent critique can help; file-count gates and posture interrogation unproven | 4,505 / 2,791 | MERGE | Common `review` evidence contract when selected; no separate plan procedure. |
| `post-deploy-monitor` | Compare production with a baseline | Baseline identity and bounded observation remain useful | 3,867 / 2,109 | MERGE | Requested observation under `deploy-verify`; no monitoring daemon. |
| `qa` | Exercise behavior and failure paths | Execution evidence is distinct from static review | 4,256 / 2,369 | MERGE | Common `review` evidence contract when selected; native tests, no mandatory QA stage. |
| `resolving-merge-conflicts` | Preserve both changes' intent | Conflict resolution is native coding work; authorizations remain in core | 1,549 / 1,407 | REPLACE_WITH_NATIVE_FEATURE | Native Git tools and requested resolution; no automatic publication. |
| `scrape` | Public extraction to validated JSON | Source and output contract useful; wrapper adds no parser or integration | 2,630 / 2,221 | REPLACE_WITH_NATIVE_FEATURE | Native retrieval plus requested schema; site/tool permission contract. |
| `security-audit` | Threat model and verified findings | Specialized security objective remains; blanket exclusions can hide real issues | 8,884 / 3,000 | MERGE | JIT security criteria under `review`; evidence and reachability, no immunity lists. |
| `ship` | Commit/push/PR with authorization and scope control | Personal publication semantics, exact-commit intent and idempotence remain useful | 4,834 / 2,534 | KEEP_BUT_SHRINK | Explicit publication request; no implicit merge/rebase/deploy. |
| `spec` | Interrogate vague ideas into issues | Precise requirements matter; fixed five phases can re-ask settled questions | 4,962 / 2,986 | REPLACE_WITH_NATIVE_FEATURE | Explicit specification/issue request and observable acceptance criteria. |
| `test-first-development` | Red-green-refactor and test-boundary advice | Exact TDD mode can be requested; generic method is already model knowledge | S 3,521 | DELETE | Ask for TDD when desired; project tests enforce behavior. |
| `to-tickets` | Decompose into tracer-bullet tickets | External issue publication still needs authority; automatic decomposition not required | 4,284 / 4,107 | DELETE | Request tickets only when they are useful deliverables. |
| `unfreeze` | Remove freeze state | Exists solely for retired hook machinery | C 539 | DELETE | Native permission configuration; preserve existing user state untouched. |
| `wayfinder` | Durable decision map for uncertain work | Long work benefits from objectives; one ticket per session creates artificial stops | 7,201 / 6,914 | DELETE | Native long-running work and explicit handoff when needed. |

The resulting discovery catalog has **five specialist entrypoints**:
`note-creation`, `review`, `handoff`, `ship`, `deploy-verify`. Claude names the
review adapter `evidence-review` to avoid its bundled `/review` alias; Codex
retains `review`. Sharing their tool-neutral bodies is a consequence of
compatibility, not a parity goal.
Removed names do not survive as aliases that continue automatic activation.

## Major mechanisms and non-skill resources

Costs are baseline source bytes; overlapping rows must not be summed. A zero
means the repository did not implement that capability, not that native clients
provide it without runtime cost.

| Component | Why it exists | Still-needed failure mode? | Source cost | Decision | Replacement |
|---|---|---|---:|---|---|
| Repository `AGENTS.md` | Harness maintenance boundaries | Repository must remain auditable and avoid external writes | 2,199 | KEEP_BUT_SHRINK | Repository-specific constraints and native validation commands. |
| Global `codex/AGENTS.md` | User preferences and working procedure | Authority/preserve-user-work preferences remain | 1,352 | KEEP_BUT_SHRINK | Shared concise preferences; no generic competence checklist. |
| 35-name parity and registry documentation | Consistent catalogs | Link integrity matters; symmetry is not a requirement | Registry READMEs 13,403 | DELETE parity requirement | Validate each published registry and its actual sources. |
| Six Codex roles | Lead/implement/investigate/test/review/integrate division | Bounded tasks useful; role files do not enforce ownership | 6,327 | DELETE | Native agent receives objective, scope and acceptance criteria. |
| `tmux-agents.md` and `codex-window` | Start and coordinate external agents | Separate sessions sometimes useful; native clients handle them | 6,837 + 1,921 | REPLACE_WITH_NATIVE_FEATURE | Native worktrees/subagents; explicit cross-provider comparison when requested. |
| Codex completion, project, nested and handoff templates | Standard artifacts | Most sections duplicate normal engineering; portable handoff remains useful | 3,706 | DELETE | Short handoff contract in the relevant skill; project owns its instructions. |
| Dual-agent phase reference and metadata | Fixed role-to-phase transitions | No measured necessity for six phases or repeated stop gates | 7,999 + 292 | DELETE | No phase engine or review-round counter. |
| Graph design document | Explain routing, panels, metering and campaigns | Operational observations useful as history | 14,202 | DELETE active architecture | Historical evidence summarized below and recoverable from Git. |
| Graph model/effort menu and routing history | Assign difficulty and optimize cost | Task difficulty varies; model rankings drift | Embedded in 39,771-byte skill | DELETE | Native session selection, calibrated through evals; no replacement router. |
| Planning/design/TDD support resources | Deepening, alternative designs, ADRs and tests | Generic methods do not need permanent packaging | 14,018 | DELETE | Project artifacts and direct requests. |
| Note templates | Course-specific source and worked-example structure | Non-obvious personal output contract remains | 2,463 + 1,881 | MAKE_PROGRESSIVE | One optional specialist reference. |
| Careful/freeze hooks and tests | Pattern warnings and edit-path checks | Real safety remains necessary; these were incomplete guards | 3,739 + 2,497 + 2,111 | REPLACE_WITH_DETERMINISTIC_MECHANISM | Native enforcement documented separately; effective settings must be verified. |
| Claude and Codex installers | Create user registry links | Deterministic filesystem handling is still needed | 2,077 + 1,983 | KEEP_BUT_SHRINK | Dry-run-first, no-clobber installation with explicit targets. |
| `scripts/test-helpers` | Shell, metadata, link and parity checks | Installation and source integrity need executable checks | 4,391 | KEEP_BUT_SHRINK | Isolated fixture checks; retire taxonomy/parity assertions. |
| Checkpoints, health/benchmark/canary state, maps and graph journals | Continuation, trends and routing feedback | Durable evidence sometimes needed; parallel state systems conflict | Embedded in skill/workflow costs | DELETE competing protocols | Native history and ordinary task artifacts; opt-in portable handoff. |
| Fixed retries, hypotheses, review rounds and escalation | Recover from errors and suppress false findings | Failures persist; arbitrary counts do not diagnose causes | Embedded in skills/graph | DELETE | Native error recovery; explicit tool errors, evidence and task limits. |
| Tool definitions, MCP servers and retrieval | Client integrations | Must remain replaceable and discoverable | 0 custom implementation | REPLACE_WITH_NATIVE_FEATURE | Host tools and actual session capabilities. |
| Sessions, compaction, cache and logs | Native agent execution | Durable session evidence matters | 0 runtime implementation | REPLACE_WITH_NATIVE_FEATURE | Native history and caching; retain relevant artifacts, not another database. |
| Historical setup/migration narratives | Explain prior architecture | Useful provenance; harmful as current instructions | 8,569 + 12,343 | DELETE obsolete procedure | Current setup guidance and this bounded audit. |

The first reduced candidate still had 14 generic skill entrypoints, an unused
provider-tier mapping and another task-state contract. The second deletion pass
removed those abstractions as well. They were not requirements merely because
the initial rewrite introduced them.

## Historical assumptions invalidated by newer models

**Assumption: agents need explicit planning stages before editing.** Old response:
`spec → plan → plan-review → tickets`, with fixed sections and approval stops.
Current evidence: Astra guidance explicitly challenges prescriptive itineraries
and mandatory repository scans. New design: native planning; a plan is an
artifact when requested or useful, never a universal prerequisite. This does not
claim all complex work succeeds without an inspectable plan.

**Assumption: every failure needs several hypotheses and a fixed escalation
count.** Old response: mandatory 3–5 hypotheses, blast-radius gates and stop after
three attempts. Current evidence: newer models can select exploration strategies;
the existing counts had no repository evaluation establishing their benefit.
New design: let evidence determine the next step; preserve actual blockers and
failure output rather than enforcing a reasoning ritual.

**Assumption: a large assurance graph is necessary for reliable autonomous
engineering.** Old response: discovery/refutation/panel/repair/acceptance fleets
with stage models. Current evidence: native delegation exists, vendor guidance
documents coordination overhead, and the repository's own campaign comparison
questions the graph's cost. New design: primary agent and optional bounded
review, evaluated against the old graph rather than treated as proven superior.

**Assumption: model context requires recurring manual resets and phase summaries.**
Old response: checkpoint protocols, resume flags, journals and one-ticket sessions.
Current evidence: Anthropic documented a reset workaround becoming dead weight
after a model upgrade; both clients provide continuation. New design: native
sessions, Git/artifacts as evidence, explicit portable handoff only when needed.

**Assumption: particular providers must plan, implement or review.** Old response:
Claude plans/Codex types; named stage models and effort escalation menus. Current
evidence: both providers support substantial coding and delegation; effort names
are not calibrated equivalently across releases. New design: chosen session
model, no repository router. Compare providers when the task calls for it.

**Assumption: caution prompts and pattern hooks form a safety boundary.** Old
response: `careful`, `freeze`, `guard` and repeated approvals. This assumption was
never a valid security guarantee: `freeze` itself acknowledged Bash bypass.
New design: keep authorization semantics while relying on execution policy for
actual access restrictions. Better model judgment does not replace isolation.

## What history justifies preserving

- The July Codex harness established the Markdown/no-runtime boundary, dry-run installation,
  role prompts and handoff conventions. The boundary and deterministic installer
  protections survive; the roles and workflow do not.
- A July verification backport repaired lost evidence gates: false-positive checking, consumer
  inspection outside a diff, secret-history inspection, idempotent publication
  and retesting changed behavior. The useful finding/publication contracts
  survive. Broad security exclusions, automatic base merges and mandatory
  planning steps do not follow from those protections.
- The August graph-workflow skill introduced the graph; its design recorded duplicate findings,
  wrong-checkout writes and expensive review. Worktree identity and evidence
  remain meaningful even when the graph is removed.
- The August harness expanded shared sources and the 35-skill parity contract. Sharing
  reduced duplication, but did not evaluate whether each skill was necessary.
- The September tuning line kept changing provider roles and effort policy, four
  times in one day. That is historical evidence of routing maintenance, not part
  of the August size baseline or changes imported here.

### Graph counterfactual and historical measurements

An unpublished report from a separate branch compared
different boxes in one campaign. It reports graph runs with 27–110 agents and
1.29–5.61 million subagent output tokens; an attended manual run used six agents
and 1.20 million. Reported subagent tokens per shipped fix were 107–200k for
graph runs and 44k for the manual run. The report also records useful residual
defects caught by cross-vendor checks and an attention advantage for unattended
graph campaigns.

These are **historical observations**, not a matched current-model benchmark:
tasks differed, some counts were estimated, primary-agent spend was omitted and
false negatives were unknown. The report's causal and cost conclusions cannot
be adopted as measured facts here. It does justify challenging the assurance
stack instead of preserving it by default.

The coding ablation compares **old, native and candidate** instructions. A
separate protocol comparison uses **A: native primary**, **B: adapted legacy
graph** and **C: primary plus one independent reviewer**. B uses native delegation
and fixture-only effects; it does not reproduce the original cross-provider
CLI campaign. A missing historical tool is an execution limitation, not evidence
of inferior model quality. See
[evaluation protocol and recorded results](../evals/README.md) for actual runs,
sample counts, model/client identities and gaps. Source-byte reductions and
installer tests do not prove better coding performance.

In the completed nine-trial protocol groups, all three conditions detected the
same seeded defects with zero unsupported findings. Their strict success was
6/9 because review findings duplicated root causes. Adapted graph cost was
4.27× primary-only, using 18 subagents; primary-plus-review cost was 1.98×, using
nine. These bounded results justify removing the mandatory topology, not a claim
that independent review never helps. A summary is in the
[historical coding comparison](../evals/README.md#historical-coding-comparison).

## Safety and data continuity

Deleting hooks removes their exact warning/edit interception behavior. The
rewrite does **not** silently install or claim equivalent native configuration.
Its permission examples are unapplied guidance. Effective host sandboxing,
approval policy, hook trust and service credential scope must be checked before
claiming enforcement. Codex's current hook documentation explicitly excludes
some tool paths; its `PreToolUse` `ask` result is unsupported and must not be
treated as a portable approval gate.

No user checkpoint, baseline, map, transcript or external state directory is
deleted or automatically converted. Existing artifacts can be read for a
requested handoff; their saved tests and authorization are not proof of current
repository state or current permission. Repository installation must preserve
foreign files and links instead of replacing them to force the new layout.

## Remaining uncertainty

The five retained capabilities are candidates with narrow reasons to exist,
not permanent architecture. Review lenses may still duplicate native ability;
publication and deployment contracts may eventually fit entirely in personal
preferences; portable handoff may prove unnecessary for this user's actual
sessions. Their continuation depends on representative task results and useful
everyday behavior. The [assumption ledger](model-assumptions.md) records the
retirement tests; further deletion remains a valid outcome.
