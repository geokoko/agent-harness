# Working agreements

Preserve unrelated user work. Authorization persists within its stated scope;
a review or diagnosis alone does not authorize edits, publication, or deployment.
Use the client’s execution permissions for access and consequential actions.
Do not commit, push, create/change/close a PR, merge, deploy, install, or change
personal client configuration unless the user explicitly requests that action.
For destructive actions or external writes, verify that existing authorization
covers the action and target; ask only for missing authority, not approval again.

Before shipping Codex-written changes, obtain a Claude review of the actual
changes being published. Codex self-review is not a substitute. Record the
reviewed revision/diff and evidence; relevant later edits need renewed review.
If Claude is unavailable, complete safe preparation and report publication as
pending. Review does not itself authorize publication.

Explain a new dependency and its purpose before adding it. Prefer existing
project conventions and avoid unrequested abstractions or tooling. Handle
errors explicitly; fix the shared cause and inspect affected callers. Batch
material questions and use established context instead of asking again.

Complete the authorized outcome through relevant validation and repair of
regressions caused by the change. Report the checkout/branch, actual check results,
and remaining limits. Distinguish prepared, applied, committed, pushed, and deployed
states; when using another worktree, include its path and a reviewable diff.
