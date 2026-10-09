# Model assumptions

Original provider evidence reviewed **2026-09-29**; candidate structure updated
**2026-10-05** without claiming a new provider capability audit. These are falsifiable reasons to retain the small
remaining contracts, not claims of measured superiority. Native permissions are
an execution requirement, not an assumption about model judgment. The broader
[capability evidence](frontier-harness-audit.md#evidence-and-its-limits) and
[task results](../evals/README.md) are separate.

| Assumption | Evidence | Mechanism depending on it | Retirement test |
|---|---|---|---|
| Personal standards add information native models cannot infer reliably. | Source-preservation, Greek exam patterns, report-only review and exact-commit publication are explicit user preferences. Vendor guidance favors specific knowledge over generic recipes: [Astra skills guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). | `note-creation`, `review`, `ship`, `deploy-verify`; minimal personal instructions. | Compare tasks with the request alone versus each contract. Remove or move any contract whose observable fidelity or authority handling does not improve enough to justify it. |
| Precise completion criteria can prevent premature stops without adding a workflow. | [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra) and [Sonnet 5.5 guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) describe incomplete check-ins; verification behavior differs with effort. | One completion/evidence paragraph, no fixed phases or review loops. | Compare completed, validated outcomes and unnecessary stops across selected models/efforts with and without the paragraph. Retain only the clauses addressing repeated failures. |
| Native session state does not by itself provide a provider-neutral handoff. | Native clients own their histories and compaction; [Claude session behavior](https://code.claude.com/docs/en/how-claude-code-works). A plain artifact carries revision-linked facts across clients. | Explicit-only `handoff`. | Transfer interrupted tasks between providers using ordinary artifacts versus the contract; compare recovery errors and time. Delete if normal artifacts are equally reliable and easier. |
| A different model given only a neutral brief can surface errors or alternatives the current model and conversation miss. | Owner request recovering the former graph's consultation step; no comparative measurement yet. | `consult`. | Compare consequential decisions with and without consultation, and against a fresh same-model brief; count real issues found after verification, false objections and cost. Delete if a fresh same-model brief is equally useful. |
| Narrow native discovery and opt-in controls are sufficient without a router. | [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude skills](https://code.claude.com/docs/en/skills) document progressive loading and explicit-only invocation. | Discoverable specialist skills; four opt-in contracts with thin native metadata. | Measure missed and accidental activation, loaded context and extra questions after client upgrades. Fix only demonstrated triggers; remove unused contracts rather than grow a router. |

The owner explicitly requires Claude review of Codex-written changes before
shipping, independently of comparative benchmark results. Preserve that rule
and explicit publication authority in always-loaded personal instructions.
Additional review panels or repeated rounds would need evidence that they find
enough real defects, after false positives and cost, to justify their use.

`cpo` and `cto` preserve September’s broader leadership and execution contracts;
`decision-review` supports open-ended brainstorming, learning/project exploration
and bounded decisions. Its exploration mode preserves the owner’s requested
office-hours behavior without forcing a verdict or commercial criteria. Their
distinct deliverables and authorization limits justify separate descriptions
provisionally. Test their
discovery and outputs on real tasks before claiming improvement or consolidation.

`ui-design` preserves visual direction through implementation and rendered
verification. `docs-update` is an explicit owner-requested shortcut for actual
documentation edits. Both should be evaluated by their concrete outputs and
correct scope, rather than generic process compliance.

The owner selected `browser-qa`, `skill-eval` and `ci-repair` as recurring
execution shortcuts. Evaluate complete browser journeys, meaningful skill
comparisons and revision-specific CI repairs; avoid duplicating generic
testing advice or adding automatic publication and infrastructure.

`learn-by-building` is unevaluated. On a real task, compare it with a plain
"guide me" request and, in Claude, the native Learning output style. Retain it
only if user-first decisions, unrewritten user code and explained-versus-
demonstrated notes improve observably.

`project-catchup` captures the owner's return-to-project briefing: reconcile
previous WIP and roadmap with relevant changes, with optional new-area orientation.
Only fictional trials of an earlier text exist. On a real return, compare it with
a plain "catch me up on X since Y" request; retain it only if relevance, source
coverage, baseline honesty and recovered WIP improve observably without unwanted
writes. No activity scoring
or automatic state store is required.

`agents-md-modernizer` matched native Claude Code and Codex at removing generic
or stale instructions, at audit-only requests and at consolidating duplicated
files. It differed in subtree scoping, in a checkable disposition and evidence
report, and, on `claude-fable-5-1` only, in keeping real constraints when asked
to shorten a legitimately long file. It cost roughly 10–55% more per Claude run
([evidence](build-evidence.md#agents-md-modernizer-addition)). Retire it when
native output keeps such constraints, scopes subtree rules and reports
dispositions unprompted. Probe its loader reference again after a client
upgrade.

For a weaker model, narrow the task and make its acceptance checks explicit; add
a targeted instruction only after reproducing the failure. Clients without native
opt-in skills can read one selected contract directly. Use the client's supported
sandbox and approval mechanism; unavailable enforcement is not replaced by prose.
