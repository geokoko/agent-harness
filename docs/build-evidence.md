# Integrated candidate build evidence

Prepared locally on 2026-10-05, branch `codex/integrated-harness`, based on PR #5
commit `1938949977101c403e002037ad73e7401f08203c`. The complete
[registry map](registry-map.md) identifies all four source snapshots and every
source skill. This record describes the integrated rebuild and its preparation
checks. Publication review evidence identifies the exact diff separately.

## What was combined

- PR #5 supplies the shared-source architecture, native client adapters,
  dry-run/no-clobber installers, and five original personal contracts.
- September supplies the full CPO/CTO mandates and references, plus diff-base,
  QA, course-source, benchmark and delegation evidence rules.
- PR #4 supplies the bounded decision-review concept and coding preferences.
- At the owner’s request, decision-review also preserves office-hours open-ended
  brainstorming and learning/hackathon/weekend-project exploration. The user can
  explore collaboratively without a forced verdict or commercial viability test.
- Main supplies useful planning, ticket, domain and testing formats as optional
  references rather than separate mandatory workflows.
- The owner explicitly requires Claude review of Codex-written changes before
  shipping and explicit authorization for the shipping action. Both rules are
  in the working agreements as well as the ship contract.

Each client registry exposes every shared contract. Shared bodies hold common
behavior; native metadata controls discovery. Four retain explicit invocation;
notes, CPO, CTO, decision-review, ui-design, docs-update, browser-qa,
skill-eval, ci-repair, consult, learn-by-building and project-catchup use normal
discovery. There is no global
router, fixed model table, custom graph launcher or new persistent state engine.
Hooks remain deferred; installed native permissions are not claimed equivalent.

## Authorship and reconciliation

Codex authored the shared/Codex contracts, integrated documentation and evaluation
repairs. Claude Code was separately asked to author the eight Claude skills from
immutable copies of all four sources, using `claude-fable-5-1` and `--effort xhigh`.
The CLI initialization confirms Claude Code 2.1.289 and that model identity.
The effort level is the requested CLI setting; it is not a measured quality claim.
Only file read/write tools were supplied for authoring, with no shell or connected
service tools. No alternative model was silently substituted.

Claude completed successfully: eight skills and references, root instructions
and an authoring report (21 Markdown files); no permission denials. Its authored
draft and a sanitized run record are retained in the local task's deliverables;
they are not files in this Git repository.
Codex then reconciled the two versions into one shared implementation:

| Material | Integration decision |
|---|---|
| Compact shared roots and Codex links | Keep the Codex structure; common behavior has one source |
| Claude opt-in entry descriptions | Use Claude's authored native frontmatter in the four thin adapters |
| CPO context/workflows and CTO lenses | Use Claude's refreshed September references, preserving attribution and canonical paths |
| Publication review | Incorporate actual-diff reading, authorship continuity, reported-versus-executed checks and valid delta review |
| Deployment verification | Incorporate evidence tying the running environment to the requested revision; pipeline success alone is insufficient |
| Handoff and security | Incorporate multi-agent authorship/review identity and privileged CI input tracing |
| Decision and planning formats | Preserve open-ended office-hours exploration and builder mode alongside bounded decisions; optional templates, no compulsory panels, labels, verdicts during exploration or invented scoring |
| Proposed aesthetic rules and numeric fallback thresholds | Do not adopt as defaults; Claude itself flagged them for confirmation. Use the project's actual standards and comparable evidence |
| Note template | Keep the existing source-faithful template; preserve September's content/extraction distinction |

Claude reported that PR #5 lacked `claude/CLAUDE.md`. Inspection resolved this:
it exists as a relative link to `shared/AGENTS.md`, in both the snapshot and
candidate. The link was preserved, and no duplicate instruction source was added.
Its original draft report is retained verbatim, including that corrected claim.

These runs were Claude **authoring**, not Claude review of the final integrated
Codex diff. The publication review is a separate pass over the actual diff;
its revision identity, findings and limits belong in the publication record.

## Frontend and documentation follow-up

The owner requested frontend coverage, a multiple-choice review-focus question
when intent is unclear, and a documentation shortcut that actually edits or
creates files. `ui-design` covers direction, implementation and polish;
`review` retains report-only audits. `docs-update` combines document-generate
and document-release while preserving accurate release state and local-only
authority. Both new skills are shared by both client registries.

Both additional Claude Code runs completed successfully with the reported model
`claude-fable-5-1`, requested `--effort xhigh`, and no permission denials. The
original eight-skill draft remains unchanged; the new drafts and sanitized run
record are retained separately in the local task's deliverables. Codex retained the compact shared roots and
incorporated Claude's task-scaled preparation, reference fidelity, interaction
evidence, explicit documentation paths and release-scope distinctions.

The integration does not copy universal focus rules across unlike controls or
require every image to be lazily loaded. Interaction guidance links to the
relevant WAI component patterns. Documentation follows the version of the release
being described rather than requiring every historical changelog entry to match
the current branch's version file.

A disposable docs-update trial edited README, created a CLI reference and added
an Unreleased changelog entry, preserving prior entries and leaving application
code unchanged. The examples and local links were checked. This is one scoped
execution, not a quality benchmark or verification of native automatic discovery.
The review-focus question uses a native choice interface when available and a
short numbered menu otherwise; a clearly scoped review proceeds directly.

## Approved browser QA, skill evaluation and CI repair additions

The owner approved `browser-qa`, `skill-eval` and `ci-repair` for both clients.
Codex authored compact shared contracts and direct discovery links. These
shortcuts execute concrete journeys, comparisons or repairs within the
request; they do not restore a mandatory phase engine or authorize shipping.
Independent Claude Code authoring completed successfully with reported model
`claude-fable-5-1`, requested `--effort xhigh`, and no permission denials. Its
three original drafts and authoring report are preserved in a separate local
archive with a sanitized run record, outside this repository. Codex retained the shared structure and incorporated
explicit smoke-versus-sweep scope, persistence checks where relevant, predeclared
grading rubrics, representative discovery neighbors, and PR-head-versus-merge
CI identity. Correlation with a change is not treated as proof of fault, and
an intermittent failure need not be hidden merely because it cannot be repeated.
This remains independent authoring, not Claude review of the final combined diff.

A disposable CI-repair trial matched source hashes to the simulated failed job,
reproduced a case-normalization failure, repaired its cause, and passed both
existing tests without changing them. Only application source changed; no hosted
run existed. A separate review found an optional coding-guide link missing from
copied evaluation snapshots. The skill now makes that checkout-only dependency
explicit and conditional rather than promising a bundled resource. No hidden
evaluation answers were added to snapshots. These are scoped checks, not a
cross-client behavior benchmark or fresh-client discovery validation.

## Consult addition

On 2026-10-05 the owner requested `consult`, recovering the graph's
cross-model consultation step. Claude Code (`claude-opus-5-5`) authored the
contract and links. A fresh read-only Claude session reported
`claude-fable-5-1` and reviewed it, with no permission denials; an owner-supplied
review also contributed findings. Both found that the launch lines relied on
compliance rather than enforcement. With Claude Code 2.1.289 and codex-cli
0.160.0, write probes were refused by the final lines: Claude had only Read,
Grep, Glob, WebSearch and WebFetch, no MCP tools and no plugin hook output, and
still found a file by repository search; Codex reported a read-only file
system. Plan mode with Bash also declined, but only by instruction. A
`--model haiku` request reported `claude-sonnet-5-5`, so the contract records
the reported model. Discovery, opinion quality and benefit over a fresh
same-model brief are not evaluated.

PR #6 review on 2026-10-06 found that these probes did not cover saved Codex
command allow rules, which can permit execution outside the read-only sandbox.
The launch now includes `--ignore-rules` and requires remaining write-capable
integrations, hooks and rules to be disabled for that invocation before launch.
If that boundary cannot be established, the consultation is unavailable. The
updated flags were checked against installed Codex CLI 0.160.0 help and its
release source; no new live consultation was run for this repair.

## Learn-by-building addition

On 2026-10-05 the owner requested `learn-by-building`, a new skill with no
source predecessor; it was drafted in a separate Claude Code session. An
owner-supplied review and a Claude Code (`claude-opus-5-5`) review found that
"implement and explain" could still pause for the user's position on every
decision; the decision loop now applies only to decisions the user owns or
shares. The second review also confirmed the native Learning output style it
is compared against exists in Claude Code 2.1.289. Local helper tests pass.
Discovery, teaching quality and benefit over a plain "guide me" request are not
evaluated.

## Project catch-up addition

The owner described returning to a project after time away: recover the
roadmap and WIP, catch up on collaborators' relevant changes, and optionally
learn an unfamiliar repository area. `project-catchup` reworks
engineering-weekly-review/retro for this purpose.

Codex prepared the addition locally against `da23eb4`, before the eval runner
was removed. Two independent, isolated Codex subagent trials used fictional
evidence snapshots: one reconciled a pilot roadmap with changed issues, PRs and
uncommitted work; the other recovered subsystem WIP, included relevant API/build
changes, explained an unfamiliar module and asked about an uncertain last-seen
baseline. These test responses under supplied instructions, not live repository
or tracker retrieval or native client discovery. Claude Code (`claude-opus-5-5`)
ported it onto the consult and learn-by-building commits as `bc672c7`; the
contract, its model-assumptions paragraph and the registry-map destination rows
are Codex's, while the port merged catalog lists and this record.

Claude Code's code-review skill reviewed `bc672c7`, and a read-only `consult`
session that reported `claude-fable-5-1` gave a second opinion; a consultation
is not the review `ship` requires. Both found that the contract did not forbid
pull, merge or rebase, its description matched plain code-explanation requests,
it had no untrusted-content rule, and this record was stale. The code-review also
found that resume requests were blocked, credentials could reach a saved
briefing, unselected transcripts were in scope, and the `learn-by-building`
frontmatter was invalid YAML.

Claude Code then edited the contract: it narrows the skill to returning users,
keeps the briefing read-only apart from a reported `git fetch --no-prune`,
continues an authorized resume after a short briefing, adds data and credential
rules, and reads prior conversations only when the user points to them. It also
rewords the `learn-by-building` description and adds a metadata check against
unquoted `: ` or ` #`. A second Fable consultation of those edits found the
read-only rule unscoped and this record imprecise. A final code-review of
`85d67e9..6fd78a9`, run as a fork of the editing session, found that resume
ignored blocked or conflicting tasks, the read-only and data rules were partial
lists, agent-authored WIP could be presented as the user's, and three limits had
been trimmed. Each was corrected; the read-only and data rules are now
principles. No independent review has covered the Claude edits. The Codex
trials ran against the original text, so the read-only, resume and
recover-then-ask rules have not been exercised; real discovery and briefing
quality are not evaluated. No new dependency, automatic state store, memory
update or scheduled task was introduced.

## Validation boundaries

At PR #6 head `d455b40`, `scripts/test-helpers` passed: Bash syntax for the three
scripts and 13 unit tests covering native discovery, opt-in metadata,
frontmatter keys, two plain-YAML description hazards, 16 isolated installer
scenarios, conflict guards and installed reference resolution after path
normalization. By inspection rather than test, every shared contract is linked
in both registries; the four opt-in contracts carry explicit-only metadata and
the rest are discoverable. ShellCheck is not installed and was skipped; runtime
discovery in a freshly installed personal client and live permission
enforcement are not established here.

The 2026-10-06 PR #6 repairs were prepared on `codex/pr6-review-fixes` from
`d455b40`. Both installers now use the canonical destination they preflight.
The evaluator selects each snapshot's workload layout and installer flags, and
rejects unrecognized legacy destination initializers before execution. The new
regressions failed before the repairs and passed afterward. `scripts/test-helpers`
passes all 18 tests, including CLI comparisons against `e65d080`, `1938949` and
`d455b40`; historical installer results remain 7/16 and modern results are 16/16.
Bash/Python syntax, skill metadata/references, all 39 tracked symlinks and
`git diff --check` pass. ShellCheck is unavailable. A separate Codex diff review
found no further issues; this is not the Claude review required before publication.

A separate Codex review reproduced two integration gaps (new skills omitted from
the evaluation catalog, and missing copied template references), then verified
the repairs and their six focused regression tests. It also checked all fifty
source-name memberships and reasoned through read-only CTO diagnosis, unsent CPO
campaign preparation, and changed-code shipping after stale Claude review.
Those scenario checks are reasoning about contracts, not measured model runs.

After restoring brainstorming, one isolated subagent trial read the updated skill
and answered an open-ended Saturday Python-project request. It offered concrete
playful directions, asked about interests and experience, and left the choice
open. This checks one response under supplied instructions; native discovery and
multi-turn behavior remain untested. No extra Claude authoring run was performed
for this follow-up edit to the shared contract.

The historical 198 trajectories compared old/native/PR #5 configurations; their
runner and records were later removed from this branch (summary in
[evals](../evals/README.md#historical-coding-comparison)). They do not measure
this integrated candidate and are not evidence that these contracts improve coding.

The independent pre-publication Claude review identified non-blocking fixes:
in-skill reference links for installed path normalization, clearer historical
evaluation labels, excluding ignored private files from trial snapshots, keeping
missing long-task workspaces ungraded, and assertions for actual opt-in metadata.
Those issues were repaired with focused regressions. The working agreement also
explicitly checks existing authority for destructive actions and external writes.
The publication record ties the original review and follow-up delta review to
their exact tree and patch identities; authoring runs do not substitute for either.

## Publication and installation scope

The owner requested Chrome MCP routing for browser QA, then authorized a commit,
push and a new PR on 2026-10-05. GPT/Codex uses its Chrome integration and Claude
Code uses Claude in Chrome; an unavailable connection must be reported without
silently substituting another browser or automation stack. Neither connection
was exercised while editing this instruction.

Preparation uses an isolated clone. Publishing this branch does not alter the
installed source checkout, personal skill links or the two earlier proposals.
Installation, merging and deployment remain separate actions. Before the
authorized publication, validation and Claude review must cover the actual diff;
the resulting PR records the commit and review evidence. This document itself
does not grant authority for any further action.
