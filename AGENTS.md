# Agent harness

This repository contains personal agent instructions, specialist skills, and
transparent installation/evaluation helpers. It is not an agent runtime. Do not
add a package manager, daemon, scheduler, state database, or generated-file pipeline.

`shared-skills/` holds portable contracts. `codex-skills/` and `claude-skills/`
contain native discovery entries; provider metadata may differ. Codex SKILL.md
frontmatter uses only name and description. Share content only when clients can
load it unchanged. Skill references are optional context, not permanent prompts.

External installation and changes to personal client configuration require an
explicit request. Preserve existing files, links, state and unrelated work.
Do not add automatic cleanup of retired names. Native clients own model selection,
permissions, sessions, tools, and delegation.

Validation: run `scripts/test-helpers` and `git diff --check`. Check shell
scripts with ShellCheck when available.
Inspect changed links/references and the full diff for scope and secrets.
Structural checks do not establish model behavior; label evaluation limits.
