# Instruction-file loading

Verified with codeword probes on 2026-10-05 against Claude Code 2.1.289 and
codex-cli 0.160.0, and consistent with each client's documentation. The Claude
Code entries were probed again on 2026-10-09 against 2.1.295. For another
client, or when behavior looks different, probe again: give the root file and a
nested file distinct codewords, open a file in the nested directory with the
Read tool, then ask a fresh session which codewords it was given. Use a capable
model; a small one can miss instructions attached to a tool result and report a
false negative.

## Claude Code

- At launch it loads `CLAUDE.md`, `.claude/CLAUDE.md` and `CLAUDE.local.md` from
  the working directory and every directory above it. `@path` imports expand at
  launch, relative to the importing file.
- `AGENTS.md` is read directly only when none of those three files exists in the
  working directory or above it (v2.1.277 and later). Otherwise it loads only
  through an `@AGENTS.md` import or a symlink. A built-in plugin provides this;
  its options can be changed in user or managed settings, not project settings.
- A subdirectory's file loads on demand, when the Read tool opens a file in that
  directory. Reading through the shell (`cat`, `grep`) loads nothing.
- With no `CLAUDE.md` at or above the working directory, a nested `AGENTS.md`
  loads on its own. With one, it does not: the subdirectory needs its own
  `CLAUDE.md` containing `@AGENTS.md`.

## Codex

- Once at start it loads the global file from the Codex home, then one file per
  directory from the project root (normally the Git root) down to the working
  directory: `AGENTS.override.md`, else `AGENTS.md`, else a configured fallback
  name.
- The client never loads a nested file off that path. Its built-in prompt only
  tells the model to look for applicable `AGENTS.md` files when working in a
  subdirectory, so a session started at the root may or may not read
  `packages/x/AGENTS.md`.
- `CLAUDE.md` is not read unless listed in `project_doc_fallback_filenames`. The
  combined instructions are capped, 32 KiB by default.

## Consequences

- A nested file scopes reliably only for sessions that start in that subtree
  (Codex) or open its files with the Read tool (Claude Code). Keep one pointer
  line in the root that names it.
- A rule that must hold in every session, such as a security, data-loss or
  compatibility boundary, stays in the root even when it concerns one subtree.
- Where the root has a `CLAUDE.md`, a nested `AGENTS.md` needs a sibling
  `CLAUDE.md` importing it. In an `AGENTS.md`-only repository it does not.
