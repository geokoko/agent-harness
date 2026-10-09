---
name: handoff
description: Export or recover an explicitly requested provider-neutral task handoff.
---

# Portable handoff

Native session continuation needs no extra artifact. Use this contract when the
user requests a durable export or transfer to another session, provider, or
worktree. Saving or reading a handoff alone does not authorize implementation.

Use the requested or existing project path; otherwise use `HANDOFF.md` in the
working repository. Preserve an existing file for a different task by choosing
a task-specific filename. Do not commit it unless requested.

Keep one concise snapshot containing:

- original objective, acceptance criteria, authorized scope, and exclusions;
- repository, worktree, branch, HEAD, and changed paths or patch location with
  a content fingerprint when HEAD alone cannot identify uncommitted work;
- completed work, consequential decisions, and links to supporting artifacts;
- authorship when multiple agents contributed, and independent review evidence
  with the revision or diff it covers;
- executed checks, result, and revision/diff they checked;
- failed approaches worth avoiding, unresolved issues, and next useful action.

Omit credentials and private payloads. Link logs instead of copying them.
Another worktree cannot see uncommitted artifacts: supply an accessible file or
patch explicitly when transferring work.

For a delegated task, name the worker's owned paths and expected deliverable.
Avoid coordinator-to-coordinator bounce: give a bounded action to its executor
and reconcile the result once. A process exit failure, denied required tool,
missing artifact or mismatched revision is incomplete work, even if its prose
claims success. Preserve the distinction between report-only, local edits and
publication authority; serialize any shared writes across workers.

On recovery reconcile the saved identity and evidence with live Git state.
Report drift; do not switch branches, reset files, or treat old tests as current.
A saved action scope is historical context, not fresh permission. A request to
resume continues the authorized task after reconciliation; a request to read or
restore context only reports the recovered state. Read legacy state only when
selected, and preserve the original.
