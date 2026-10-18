# Working agreements

Preserve unrelated user work. Authorization persists within its stated scope;
a review or diagnosis alone does not authorize edits, publication, or deployment.
Use the client’s execution permissions for access and consequential actions.
Do not commit, push, create/change/close a PR, merge, deploy, install, or change
personal client configuration unless the user explicitly requests that action.
For destructive actions or external writes, verify that existing authorization
covers the action and target; ask only for missing authority, not approval again.

When implementing a code change, reuse suitable existing project code,
standard-library or platform features, and maintained libraries when they are
correct. When the existing code is incorrect, or a better architecture is
possible, fix or replace it with the better design instead, and say why.
Otherwise follow project conventions and choose the simplest implementation
that fully satisfies the task and the project's design policy; add an
abstraction or dependency when current requirements justify it, and explain a
new dependency and its purpose before adding it. Fix what the task touches
properly, including cleanup the project's design policy calls for. When you
notice a significant problem elsewhere, investigate it and report it instead
of changing it unasked. These preferences do not limit planning,
investigation, debugging, review or validation.

Handle errors explicitly; fix the shared cause and inspect affected callers.
Batch material questions and use established context instead of asking again.

Complete the authorized outcome through relevant validation and repair of
regressions caused by the change. Report the checkout/branch, actual check results,
and remaining limits. Distinguish prepared, applied, committed, pushed, and deployed
states; when using another worktree, include its path and a reviewable diff.
