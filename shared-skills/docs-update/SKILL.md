---
name: docs-update
description: Create or update project documentation, release notes, and migration guidance from the implemented behavior or requested change.
---

# Documentation creation and updates

When asked to document a feature, update docs, or prepare release documentation,
produce the requested files and edits. A list of suggested changes is not the
deliverable when local edits are requested and permitted. A request only to
explain, brainstorm, or audit documentation remains an answer or report.

## Establish the target

Use the request and existing context to identify the audience, feature or change,
and intended documentation location. Ask only when unresolved scope or release
identity would materially change the result; batch those questions. A bare
invocation without a discernible target needs a short target question, not a
documentation audit of the whole repository.
Honor requested file paths before choosing a default location.

Read the relevant documentation, its navigation, and the implementation,
configuration, examples, and tests needed to establish the behavior being
documented. For a change-based update, identify the requested comparison and
include relevant uncommitted and untracked changes. Verify the comparison base;
being on the default branch or having an empty branch diff does not prevent
documenting an explicitly identified feature, release, or working-tree change.
For release notes, use the relevant release markers and target revision rather
than treating the current branch's version file as proof of every release's state.

## Write the documentation

Preserve the project's tone, structure, terminology, and documentation system.
Update existing material where it belongs; create missing pages when the
requested surface needs them. Choose tutorial, task guide, reference, or
explanation to fit the reader's need; do not manufacture a full set for each
change. Keep the work focused on the requested target and directly affected
documentation.

Cover relevant new surfaces as well as stale claims: behavior, commands, API
parameters and responses, configuration defaults, setup, compatibility, or
migration. Base concrete claims on observed implementation and evidence. If
implementation and stated intent disagree, expose the discrepancy rather than
silently promising behavior that does not exist or changing code to fit the
documentation.

Use exact, usable examples with explicit prerequisites and placeholders where
appropriate. Separate instructions users can run from steps actually verified.
For migrations, explain affected users, the required changes, and a practical
way to check the result; include recovery guidance when the change warrants it.

For release notes, describe user-visible changes, fixes, and breaking changes
from the verified change scope. Follow the existing changelog format and
preserve previous entries. Use a release version and date only when established;
keep pending changes clearly unreleased. A merged branch, passing test, or docs
request does not establish that a release has shipped or been deployed.

Connect new pages through existing indexes or navigation where needed. Reconcile
affected examples and overlapping docs without reorganizing unrelated content.

## Verify and finish

Check changed links, navigation, anchors, examples, and factual claims. Run the
repository's relevant documentation checks or build when available. Verify
commands safely in an appropriate local environment; describe checks that could
not run and why. Do not install a new documentation toolchain or execute live,
destructive, or external operations just to validate an example.

Inspect the final diff and report the files created or updated, the behavior or
release scope they describe, actual checks, and unresolved evidence gaps. Leave
source-code changes, commits, tags, release creation, publication, and deployment
to separately authorized work. Documentation edits alone do not authorize them.
