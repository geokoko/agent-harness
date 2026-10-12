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

Inspect the actual diff and relevant surrounding code, including uncommitted
and new files. Record checks actually run and unavailable integration coverage.
Resolve blocking findings before publication. If a review was requested, record
the reviewed revision/diff and whether later edits affect its findings.

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
