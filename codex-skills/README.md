# Codex skills

Relative directory links resolve to canonical sources in
[shared-skills/](../shared-skills/). See [the catalog](../README.md).
`note-creation`, `decision-review`, `cpo`, `cto`, `ui-design`, `docs-update`,
`browser-qa`, `skill-eval`, `ci-repair`, `consult`, `learn-by-building`,
`project-catchup` and `agents-md-modernizer` support native discovery.
The other four sources
carry `agents/openai.yaml` with `allow_implicit_invocation: false`: request
`$review`, `$handoff`, `$ship` or `$deploy-verify` explicitly.

Only `name` and `description` appear in shared skill frontmatter. Bodies and
relevant references load when selected; no root router or model mapping is
required. Invocation policy does not authorize external actions.

```bash
scripts/install-codex --dry-run
scripts/install-codex --apply
```

The installer requires Bash and GNU coreutils (`ln -T`, `realpath -m`); stock
macOS/BSD utilities are insufficient. Add `--global-agents` to include the optional personal instruction link after
reviewing its content. Existing files and foreign links are never replaced.
See [installation/update steps](../docs/skill-migration.md) and
[native permissions](../docs/providers.md). Model choice, tool access, MCP and
session continuation belong to the client.
