# Native client configuration

The clients supply the agent loop, model selection, tools, sessions, compaction,
worktrees and execution permissions. This repository supplies portable contracts
and native discovery metadata. No provider mapping file or API adapter is needed.
Keep the selected session model unless the task gives a reason to change it.
Model availability and effort behavior depend on the client and account; see the
[dated evidence](frontier-harness-audit.md#evidence-and-its-limits).

## Discovery and tools

Codex links every canonical source. Its four opt-in contracts use
`agents/openai.yaml` with `allow_implicit_invocation: false`. Claude instead uses
four small `disable-model-invocation: true` entrypoints, each linking a shared
contract and any references; `note-creation`, `decision-review`, `cpo`, `cto`,
`ui-design`, `docs-update`, `browser-qa`, `skill-eval`, `ci-repair`,
`consult`, `learn-by-building` and `project-catchup` link directly and support
native discovery. The review
adapter is `/evidence-review` in Claude to avoid its bundled `/review` alias,
and `$review` in Codex. These controls remove accidental activation without
imposing identical client behavior.
[Codex skills](https://learn.chatgpt.com/docs/build-skills),
[Claude skills](https://code.claude.com/docs/en/skills).

Use the available browser, shell, MCP and discovery tools according to their own
contracts. API support for programmatic calling, tool search or computer use
does not establish that a local client exposes it. Linking a skill neither
installs integrations nor grants accounts or tool access.

For `browser-qa`, the owner selects Chrome through each client's browser MCP:
the GPT/Codex Chrome integration in Codex, and Claude in Chrome in Claude Code.
Discover the current tools and select Chrome explicitly. Do not silently use the
in-app browser or install a separate browser driver when that connection is
missing; report the unavailable verification and obtain authorization for any
alternative. Existing project tests may supplement the requested Chrome run.
See the [GPT/Codex browser extension](https://learn.chatgpt.com/docs/chrome-extension)
and [Claude in Chrome](https://code.claude.com/docs/en/chrome). These are routing
instructions, not evidence that either extension is connected in a given session.

## Permission examples — UNAPPLIED

Checked against opened official documentation on **2026-09-29**. These examples
have not been installed or validated against the user's effective client
configuration. Review supported options and merge deliberately with local and
managed policy. Installing this harness does not apply them.

### Codex: workspace edits, restricted reads and reviewed escalation

Example `config.toml` for a client supporting permission profiles:

```toml
approval_policy = "on-request"
approvals_reviewer = "user"
default_permissions = "harness-workspace"

[permissions.harness-workspace]
extends = ":workspace"

[permissions.harness-workspace.filesystem]
":root" = "deny"
":minimal" = "read"

[permissions.harness-workspace.network]
enabled = false
```

The inherited profile permits workspace and temporary-file writes while retaining
protected metadata paths. Other reads are limited to the runtime baseline.
Grant read access to exact installed-skill source paths if needed. Permission
profiles are beta and do not compose with legacy `sandbox_mode` settings; remove
conflicts before relying on a profile. [Codex profiles](https://learn.chatgpt.com/docs/permissions).

The reviewer setting sends required approvals to the user. Ordinary actions
inside the boundary need no extra harness checkpoint.
[Approval configuration](https://learn.chatgpt.com/docs/agent-approvals-security).

For an additional command-specific prompt, a native `rules/*.rules` example is:

```python
prefix_rule(
    pattern = ["git", "push"],
    decision = "prompt",
    justification = "Review publication before executing it.",
    match = ["git push origin HEAD"],
)
```

Validate a rule using
`codex execpolicy check --rules PATH_TO_RULES -- git push origin HEAD`.
A prefix rule matches command invocations, not every equivalent API call or
script. [Codex rules](https://learn.chatgpt.com/docs/agent-configuration/rules).

### Claude Code: local edits with tool approvals and sandboxed commands

Example project `.claude/settings.json`:

```json
{
  "permissions": {
    "defaultMode": "acceptEdits",
    "blockReadsOutsideWorkingDirectories": true,
    "ask": ["Bash(git push *)", "Bash(gh *)", "mcp__*"]
  },
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "network": {"allowedDomains": []}
  }
}
```

This example permits local edits, adds a file-read fence, and prompts for the
listed command/tool forms. Replace broad MCP prompts with the actual tool-level
policy needed after inspecting installed schemas. Shell patterns are not a
complete semantic authorization boundary.
[Claude permissions](https://code.claude.com/docs/en/permissions).

The sandbox example fails startup when required support is unavailable and
disables model-requested unsandboxed retries. Empty `allowedDomains` supplies no
preapproved hosts itself; other settings and approved hosts can expand access.
Host approval does not distinguish reading from writing to that service.
The Bash sandbox's default read policy can still expose sensitive files or
environment variables; file-tool fences are not a universal credential vault.
Review native credential/read restrictions for the actual environment and use
narrow service credentials. Inspect `/permissions` and `/sandbox` before relying
on the resulting boundary.
[Claude sandbox](https://code.claude.com/docs/en/sandboxing).

## What these examples do not guarantee

Removing `careful`, `freeze`, `guard` and `unfreeze` removes their exact warning
and Edit/Write interception behavior. These examples do **not** provide an
equivalent selected-subdirectory freeze or universal destructive-command warning.
Workspace write permission still allows destructive edits inside the workspace.
Worktrees isolate file changes, not credentials, shared Git metadata or services.

A required narrower boundary belongs in native filesystem/tool policy or a
suitable sandbox, then needs harmless denied-read/write/network checks in the
target client. Tool hooks can provide additional checks, but coverage and trust
requirements differ. Codex currently excludes some paths from hooks and does not
support `PreToolUse` `ask` as a blocking approval result; do not copy Claude hook
schemas blindly. [Codex hooks](https://learn.chatgpt.com/docs/hooks),
[Claude hooks](https://code.claude.com/docs/en/hooks).

Native history remains with its client. Use `handoff` only for a requested
portable transfer, and preserve old state files. A saved instruction or
historical authorization cannot alter active host permissions.
