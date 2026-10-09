---
name: review
description: Apply the personal evidence and report-only contract to an explicitly requested review.
---

# Review contract

Infer the intended review from the request, selected artifact and existing
context. If it remains unclear, ask what kind of review the user wants before
starting the substantive assessment. Use the client's multiple-choice question
interface when available; otherwise show a short numbered menu. Offer a few
relevant choices, such as code correctness, UI/UX, security, performance or a
broader review, and allow the user to describe another focus or combine choices.
Do not silently run every specialist review. A clear request such as "review
this diff for security" needs no repeated selection question.

Report findings without editing source unless fixes are also requested. Identify
the reviewed base, head or working-tree diff, including relevant untracked files.
Verify that the comparison base resolves and matches the requested scope; do
not assume a branch named main or master exists. Disclose stale or unavailable
evidence. For a dependency stack, check descendants and relevant open-PR overlap
before presenting an already-fixed defect as outstanding. Deduplicate by failure
claim and consequence, not by filename or matching title alone.

An actionable finding includes located evidence, a concrete failure scenario,
its consequence, and the smallest useful correction. Verify claimed missing
behavior through relevant callers, middleware, and generated constructs;
grep absence alone is insufficient. Distinguish introduced defects, pre-existing
problems, and unresolved suspicions. Do not report tool-enforced style choices.
For new enum/status/type values, trace sibling-value consumers outside the diff
when they may depend on an exhaustive list. Coverage claims identify actual
tests and assertions; plausible but unreproduced concerns stay separate.

Read a reference only for the requested specialist objective:

- [Security and repository-history exposure](references/security.md).
- [Measured developer onboarding](references/devex.md).
- [Browser performance comparisons](references/benchmark.md).
- [Rendered UI evidence](references/visual.md).
- [Behavioral verification](references/behavior.md).

Order confirmed findings by impact, then state the validation performed and
remaining scope limits. No findings means no actionable defect was established,
not that correctness was proved. Ordinary review needs no panel, fixed number
of rounds, or repair phase. The separate owner requirement remains: Claude
must review Codex-written changes before they are shipped. Record the reviewed
revision/diff; this requirement does not authorize publication.
