# Release Notes

## v0.3.0 (2026-06-22)

**`blind-review` gains review modes.** It was spec-only; it now runs in one of three
modes, chosen by which *intent artifact* the reviewer is handed:

- **No context** (default) — nothing but the code: a cold soundness audit (bugs,
  security, data safety).
- **Spec** — the original requirements: the compliance gap (was the right thing built?).
- **Plan-vs-code** — the intended implementation plan: drift detection (did the build
  follow the design?).

The invariant that makes it "blind" is unchanged and now explicit: the reviewer **never**
sees the implementer's account of the work. Modes differ only in which statement-of-intent
(none / spec / plan) they judge against — never a post-hoc "what I did" narrative. A focused
routing eval confirmed the broader description doesn't regress: blind-review held 5/5 recall
(including the new plan-vs-code and cold-audit phrasings) with zero false fires, and no
adjacent skill (pipeline-verification, less-is-more, adr) was stolen.

**Codex is now a first-class install.** Codex CLI (≥ 0.139) reads the same
`marketplace.json` as Claude Code, so the install is the same two steps on each
(`codex plugin marketplace add … && codex plugin add bardak@bardak`). README documents
both; `docs/codex.md` promotes the marketplace path and keeps manual `.codex/skills/`
vendoring as a fallback. README also now states ADRs live in `docs/adr/`.

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
`more-is-less` skill was validated the same way (5/6 recall, zero false fires after tuning).

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

**Conventions**
- Descriptions are trigger-only (when to use), so the skill body is read, not skipped.
- The four reflex skills carry an Iron Law and a Red Flags rationalization table.
- Skills cross-reference each other (`bardak:` namespace) into workflows.

**Other**
- `docs/codex.md` — install + `AGENTS.md` wiring for using the skills under Codex.
- MIT licensed.
