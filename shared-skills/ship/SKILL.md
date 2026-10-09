---
name: ship
description: Apply the personal publication contract to explicitly authorized commit, push, or PR work.
---

# Publication contract

Match actions to existing authorization. Readiness requests are read-only;
pushing an existing commit means that exact commit. Creating a PR does not
authorize merging or deployment. This skill grants no execution permissions.
The user's explicit no-ship boundary remains in force until they request the
particular commit, push, PR change, merge, deployment, or installation.

Before publishing Codex-written changes, require Claude review of the actual
diff being shipped, including relevant uncommitted/new files. Record the base,
head or working-tree identity, findings, checked evidence and limitations.
The reviewer reads the diff and relevant surrounding code, not only the author's
summary. Record actual checks separately from reported checks and unavailable
integration coverage. Preserve authorship across delegation and handoffs; mixed
changes containing Codex work still need Claude review. A general request to
ship does not waive this rule.
Codex self-review cannot satisfy this owner requirement. Resolve blocking
findings; relevant edits after review need another Claude pass. If Claude is
unavailable, finish safe preparation and leave publication pending. Existing
review evidence may be reused only when it still covers the exact changes.
Reviewing the changed portion is enough when the earlier reviewed state is
identifiable; otherwise review the full diff.

Use the requested branch, remote, and protocol. Do not silently rebase, merge
the base, force-push, or publish from the default branch. Preserve unrelated
changes; stage only the intended paths or hunks and inspect the staged diff.
Exposed secrets, unclear publication scope, or relevant failing required checks
block publication. Report reproduced baseline failures separately.

Check remote state after an ambiguous network result before retrying a push or
PR creation. Reuse the existing PR when appropriate. Its title and description
must describe the final change, actual validation, and material limits.

Report exact branch/commit and the resulting publication state. A prepared
patch, local commit, successful push, open PR, passing hosted CI, and deployed
revision are different outcomes; claim only those actually verified.
