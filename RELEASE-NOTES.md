# Release Notes

## v0.2.0 (2026-06-22)

**New skill: `more-is-less`** — the disciplined counterweight to `less-is-more`. When a
structural boundary (a schema, an integration/variant seam, a contract) has a *named*
future need, it makes the case for investing in the seam now — a port, an extension
point, a value type — so the next variant is additive instead of a migration. It guards
both failure modes: speculative flexibility is over-engineering, but a hardcoded
`if type == …` branch is under-engineering. It refines, never overrides, `less-is-more`
(that one governs runtime complexity; this one governs structure at a boundary).

**Skill-triggering improvements** (wording only — no behavior change). A routing eval
(scoring each skill's description against the others and the real competing installed
skills) found the only systematic defect was over-firing:

- **adr** no longer fires while a decision is still being *deliberated* (that is
  `less-is-more`); it now anchors on *recording* a finalized decision.
- **no-silent-errors** drops its over-broad scope and no longer triggers on plain
  parsing/formatting (e.g. writing a regex).
- **verify-the-premise** spells out its distinction from `pipeline-verification`.

Recall held at 33/33 across the eval; description collisions dropped from 9 to 3. The new
`more-is-less` skill was validated the same way (5/6 recall, zero false fires after
tuning). Adds a reusable routing-eval harness under `plugins/bardak/.skill-evals/`.

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
