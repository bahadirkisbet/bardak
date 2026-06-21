# Release Notes

## v0.1.1 (2026-06-22)

Maintenance — version bump only, no skill changes. First run of the `dev` → `main`
release flow, which also exercises the plugin upgrade path for installers
(`claude plugin marketplace update bardak`).

## v0.1.0 (2026-06-22)

Initial release. Eight skills, packaged as a Claude Code marketplace plugin.

**Skills**
- `blind-review` — final spec-only review gate; independent reviewers see only the spec.
- `retrospective` — extract non-obvious lessons at session end and persist them.
- `less-is-more` — architecture decisions: intent → explicit paths → business-grounded tradeoffs, with a `.claude/business-context.md` memory that compounds.
- `no-silent-errors` — every fault path visible; strong types first.
- `verify-the-premise` — never assume; act on observed data.
- `pipeline-verification` — verify end to end and map blast radius, not just unit tests.
- `bugfix-tdd` — a failing reproduction test before any fix.
- `adr` — short, immutable Architecture Decision Records.

**Conventions** (informed by a study of obra/Superpowers)
- Descriptions are trigger-only (when to use), so the skill body is read, not skipped.
- The four reflex skills carry an Iron Law and a Red Flags rationalization table.
- Skills cross-reference each other (`bardak:` namespace) into workflows.

**Other**
- `docs/codex.md` — install + `AGENTS.md` wiring for using the skills under Codex.
- MIT licensed.
