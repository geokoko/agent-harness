---
name: consult
description: Get an independent, read-only opinion from a different model in a fresh conversation when the user asks to consult another or a named model, or for a second opinion from one.
---

# Cross-model consultation

The consultant advises; the current agent remains responsible for the answer
and any action. Consulting grants no authority beyond the original request and
does not replace the Claude review that `ship` requires.

## Launch

Start a different actual model in a new conversation. Use the model the user
named; for an unnamed "another model", choose one other than the current model
and say which. A fork, resumed session or same-model agent is not this
consultation. Compare the model the client reports with your own; if they
match, label the result a same-model review or ask which model to use.
If the requested model, its client or a fresh-context launch is unavailable,
report that explicitly. Distinguish that from a launch blocked by your own
sandbox, approval or timeout.

Remove write-capable tools, including MCP servers, connectors and plugins;
a mode or instruction the consultant must obey is not enforcement. Keep the
brief and output in a new temporary directory outside the checkout. Check local
`--help` for current flags:

- Claude: `claude -p --restricted --strict-mcp-config --tools Read,Grep,Glob,WebSearch,WebFetch --no-session-persistence --model MODEL --output-format json <BRIEF >OUT`
- Codex: `codex exec --ignore-user-config --ignore-rules --sandbox read-only --ephemeral -C REPO -m MODEL - <BRIEF >OUT`
- A native subagent qualifies only when it runs a different model, inherits no
  conversation and has no write-capable tools.

For Codex, `--ignore-user-config` skips only user configuration;
`--ignore-rules` skips user/project command rules that could bypass the sandbox.
Inspect remaining project/system/managed configuration and disable write-capable
integrations, hooks and command rules for this invocation before launch. If an
enforced read-only setup cannot be established, report the consultation as unavailable.

## Brief

Write a self-contained brief: the question, requirements, constraints and
relevant source material, such as paths at an identified revision, excerpts,
logs or reproduction steps. Do not pass the transcript. For an independent
opinion, omit the current agent's preferred answer and leaning; present
candidate options neutrally. Omit credentials and data the question does not need.

Ask for an assessment with evidence, alternatives, uncertainties and the
strongest objections, including objections to its own recommendation. State
that the consultation is read-only: no edits, installs, commits or external writes.

## Bring it back

Record `git status` and a diff hash before launch, compare them afterward, and
do not edit the material under review while the consultant runs. This comparison
detects local changes; it does not enforce permissions or detect external writes.
A failed launch, empty output or nonzero exit is a failed
consultation, not an opinion.

Attribute the opinion to the consulted model and mechanism. Explain where it
agrees and disagrees with the current analysis, and why. Verify consequential
claims against code, documentation or checks before acting; keep unverified
claims labeled as the consultant's.
