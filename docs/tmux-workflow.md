# Optional visible agent sessions

Use tmux when the user wants independent CLI sessions that remain visible and
steerable. It is an optional presentation/operating choice, not a harness
runtime. Native delegation is sufficient when separate sessions add no value.
This guide neither launches sessions nor changes client permissions.

1. Inspect repository instructions, status and the requested outcome. Use the
   intended source revision; a branch name alone does not identify a dirty
   checkout. Preserve unrelated work.
2. Assign each worker a bounded task, acceptance evidence, exact absolute
   input/output paths, allowed writes and existing authority. Use the
   [handoff contract](../shared-skills/handoff/SKILL.md). Independent CLI
   sessions do not inherit each other’s conversation or decisions.
3. Give substantial concurrent editors separate worktrees and explicit write
   ownership. Readers can share the intended checkout. Separate worktrees do
   not isolate databases, ports, external accounts or generated shared state;
   coordinate those dependencies and serialize shared changes.
4. Open only the sessions needed, with ordinary `codex` or `claude` launch
   settings and the user’s requested model/effort. Do not add permission-bypass
   flags or a fixed role/model roster. A missing requested client or model is
   a limitation to resolve, not permission to silently substitute it.
5. Integrate completed changes in dependency order within the authorized
   editing scope. Check the combined diff and affected tests. Preserve the
   exact source and patch identity behind each report, and reuse valid evidence
   without repeating unrelated checks.
6. Use independent review appropriate to the task. **Claude must review
   Codex-written changes before shipping.** Review completion does not itself
   authorize commits, pushes, PR changes, merges, installation or deployment.
7. Report the retained worktree paths and session state. Inspect exact targets
   before cleanup. Do not force-remove dirty worktrees or broadly kill the
   user’s sessions. Preserve unfinished or unrelated work.

For a requested manual setup, these examples illustrate native tmux controls;
replace the session, name and absolute path with the inspected targets:

```bash
tmux list-sessions
tmux list-windows -t SESSION -F '#{window_index}:#{window_name} #{pane_current_path}'
tmux new-window -t SESSION -n TASK -c /absolute/path/to/task-worktree codex
tmux select-window -t SESSION:TASK
```

Start `claude` instead of `codex` for a Claude session. Pass the prepared task
handoff using the client’s supported interface. Consult the installed client’s
help for model/effort controls instead of assuming a saved flag remains valid.
No custom launcher, shared journal, automatic retry service or global state
directory is required.

Source: shortened from the September tuning line's guide to running agents in
tmux windows, with permanent roles, auto-publication assumptions and custom
helpers removed.
