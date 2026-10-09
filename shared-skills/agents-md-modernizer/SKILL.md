---
name: agents-md-modernizer
description: Audit, simplify, or modernize AGENTS.md, CLAUDE.md and related repository agent-instruction files that are bloated, stale, duplicated or generic. Not for ordinary project documentation.
---

# Agent instruction modernization

Produce the smallest instruction set that materially changes agent behavior in
this repository. An audit or review request remains a report: classify and
recommend, edit nothing.

## The test

Keep an instruction only when a capable current coding agent would be materially
more likely to make a mistake without it. That normally requires all four: it is
specific to this project, non-obvious or expensive to infer, relevant often
enough for its loading scope, and able to change implementation or execution.
Advice that merely sounds prudent fails; delete it rather than rephrase it. For
a personal or global file, read "this project" as "this user's work across
projects".

Classify each substantive instruction:

- **KEEP** — repository context an agent cannot derive: commands, generated-file
  sources, invariants, contracts and boundaries.
- **REMOVE** — generic conduct, whatever is cheap to discover, duplicated
  elsewhere or mechanically enforced, and anything stale.
- **MOVE** — valid, but loaded too broadly. Instructions for one subtree belong
  in that directory's instruction file or a document the root points to. Leave
  one pointer line in the root instead of a summary: a nested file loads only
  in some sessions (see [loader behavior](references/loaders.md)). A rule that
  must hold in every session, such as a security, data-loss or compatibility
  boundary, stays in the root even when it concerns one subtree.
- **REWRITE** — a real constraint expressed as coaching. State the invariant,
  and its reason when the original or the repository gives one: "be very
  careful with migrations" becomes "migrations must stay backwards compatible
  with the previous release; blue-green deployment runs both versions
  simultaneously."

Prefer pointing to an authoritative file or example over paraphrasing it.

Modernizing removes, corrects and relocates; it does not add. Replace a stale
command or path with what the repository actually provides. Anything else the
original lacked, however true, is proposed in the report and written only when
the request asks for fuller instructions.

## Rare but critical rules

Rarely triggered does not mean removable. Preserve the underlying constraint in
any project-specific rule touching security, credentials, production, releases,
migrations, backwards compatibility, generated artifacts, irreversible actions
or external systems, even while removing obsolete wording around it and even
when asked to shorten the file. When the reason for such a rule cannot be
established, keep it and report the uncertainty. Generic security advice, such
as not committing secrets or validating input, is still generic.

## Multiple instruction files

Determine each file's actual scope and whether its content is unique before
consolidating. Prefer one shared source when the clients in use can load it;
keep client-specific content only when it is truly client-specific.
Compatibility files and symlinks are not deleted or duplicated on assumption.
[Loader behavior](references/loaders.md) records what Claude Code and Codex
were verified to load; probe any other client before relying on a file it may
not read.

## Verify

Every command and path that remains must be supported by repository evidence:
manifests, scripts, CI configuration or the files themselves. Never invent one.
A constraint the repository cannot confirm, such as deployment topology or an
external system's behavior, stays on the original's authority, neither dropped
nor presented as checked. List it as unverified in the report; the instruction
file itself carries no such caveat.

After editing, reread the result against the original. Each project-specific
instruction must be present, moved to a location that exists and that the
client loads, or removed for a stated reason. No contradiction or dangling
pointer may remain. Optimize information density, not a line count: a simple
repository may need under twenty lines, and seventy lines of real hardware or
safety constraints should stay seventy.

## Report

Give the reader enough to check the result without repeating the work, in the
reply itself and not in a new file:

- **Disposition** — every project-specific instruction from the original with
  its class and where it now lives, or why it was removed. Group generic
  removals by kind rather than listing each one.
- **Evidence** — for each retained or corrected command and path, the file that
  supports it, and whether a command was executed or only confirmed to exist.
- **Proposed additions** — constraints found by inspection that the original
  lacked, each with its evidence, for the user to accept or decline.
- **Unverified** — constraints kept on the original's authority, loader behavior
  assumed rather than tested, and conflicting repository evidence.
- **Size** — lines before and after for each instruction file, with the
  original measured before the first edit.

An audit reports the same disposition and evidence as recommendations. No
scoring rubric unless requested.
