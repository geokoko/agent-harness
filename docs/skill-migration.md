# Install or update the harness

Use a stable checkout selected for everyday use. A comparison worktree is a
review artifact; do not install it merely because its local checks pass.
The [catalog](../README.md) describes the capabilities, and the
[registry map](registry-map.md) classifies every entrypoint across all four sources.
The integrated branch and its PR are review artifacts, not an installation.

## New installation

The installers require Bash and GNU coreutils: `ln` with `-T`, plus `realpath`
with `-m` for Codex. Stock macOS/BSD utilities do not support these options; use
GNU tools on `PATH` before installing there.

Run as the intended user, without `sudo`:

```bash
scripts/install-codex --dry-run
claude-skills/install.sh --dry-run
```

Codex defaults to `~/.agents/skills`; Claude defaults to `~/.claude/skills`.
Use `--skills-dir DIRECTORY` to preview another target. Codex also accepts
`--global-agents` and `--codex-home DIRECTORY`; the optional instruction link
otherwise uses `${CODEX_HOME:-$HOME/.codex}/AGENTS.md`.

Review every destination, then rerun the chosen command with `--apply`.
Installers reject conflicts before creating links and accept existing links
that resolve to the intended source. They never replace a real file, foreign
link or conflicting dangling link. Claude personal instructions are a separate
manual review/merge from [claude/CLAUDE.md](../claude/CLAUDE.md).

Start a fresh client session and inspect its discovered skills. Invoke the
four opt-in contracts explicitly; the others support native discovery.
Normal tasks need no skill invocation.
The review contract is `/evidence-review` in Claude and `$review` in Codex; the
Claude adapter intentionally avoids the bundled `/review` alias.
Installation does not configure hooks, MCP servers, model selection or safety
permissions. [Provider guidance](providers.md) contains unapplied examples.

## Updating an older installation

1. Inspect installed links and effective hook configuration before removing
   source paths. End sessions that have loaded retired careful/freeze hooks;
   remove only their reviewed configuration entries. A missing script is not
   a replacement safety mechanism.
2. Review the actual permission boundary needed. Workspace write permission
   does not reproduce a selected-subdirectory freeze or destructive-command
   warnings. Configure and test native restrictions separately if required.
3. Preview installation from the chosen checkout. Inspect existing symlink
   chains, including `~/.claude/skills/geo`, with `readlink`; names alone do not
   establish ownership. Preserve unrelated skills and all real directories.
4. Remove only individually reviewed obsolete links with `unlink EXACT_PATH`.
   The installer deliberately performs no cleanup. Do not recursively delete
   a registry or personal state directory to resolve a conflict.
5. Apply the reviewed links and inspect discovery in a fresh session. Retired
   names, the `geo` umbrella and six-phase parameters have no active aliases.

## Existing task data

Keep checkpoints, health reports, benchmark/canary baselines, decision maps,
graph records and dual-agent artifacts where they already live. No automatic
conversion or new state directory is required. A requested `handoff` can read
selected legacy artifacts, reconcile their repository/revision with live state,
and export only the useful facts while preserving originals.

Old snapshots do not confer new authorization or prove current checks pass.
Native session resume remains the default; this repository neither migrates
native transcripts nor modifies client memory.
