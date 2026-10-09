# Claude Code skills

This registry exposes the capabilities in [the catalog](../README.md).
`note-creation`, `decision-review`, `cpo`, `cto`, `ui-design`, `docs-update`,
`browser-qa`, `skill-eval`, `ci-repair`, `consult`, `learn-by-building` and
`project-catchup` link directly to shared sources and can be discovered from
their descriptions.

`evidence-review`, `handoff`, `ship` and `deploy-verify` have short Claude
entrypoints with `disable-model-invocation: true`. Invoke them with
`/evidence-review`, `/handoff`, `/ship` or `/deploy-verify`.
Each entrypoint links `contract.md` and any references to
the shared source. This adapter supplies native invocation policy; it does not
duplicate the contract or grant tool permissions. `/evidence-review` avoids
Claude's bundled `/review` alias and uses the canonical `review` contract.

```bash
claude-skills/install.sh --dry-run
claude-skills/install.sh --apply
```

Requires Bash and GNU coreutils (`ln -T`, `realpath -m`), including GNU tools on macOS.
Run from the stable checkout after reviewing the dry-run. Conflicting files or
links are preserved and abort installation. The installer creates top-level
skill links, not a `geo` umbrella, hooks or personal state. Review
[installation/update steps](../docs/skill-migration.md) for an older setup.

Optional personal instructions are [claude/CLAUDE.md](../claude/CLAUDE.md);
review and merge them into the intended instruction layer manually. The
[permission examples](../docs/providers.md) are unapplied and do not recreate
the former careful/freeze behavior. Start a fresh session after changing loaded
skills or hooks.
