---
name: adr
description: Use to record or document a significant, hard-to-reverse technical decision that has been made or is being finalized (framework, data model, service boundary, protocol, build-vs-buy) so the reasoning survives, or when the user says /adr. Also use before re-deciding something — to check existing ADRs first. This captures a decision; it does not deliberate one (weighing the options is less-is-more).
---

# ADR — Architecture Decision Records

A significant decision that isn't written down gets re-litigated, half-remembered, or silently reversed. An ADR is a short, immutable record of one decision: what was decided, why, what was rejected, and what it costs. Cheap to write; priceless six months later when someone asks "why is it like this?"

**Announce at start:** "Recording this as an ADR." / "Searching existing ADRs first."

## When to Use

- A decision that is expensive to reverse: a framework, a data model, a service boundary, a protocol, a build-vs-buy.
- A decision people will ask "why?" about later.
- Before re-deciding something — search existing ADRs first; the question may already be answered (and rejected for a reason).
- Not for: reversible, local, or obvious choices.
- Not for *deliberating* a decision still in flight — that is `bardak:less-is-more`. Reach for an ADR once the choice is settled and worth recording.

## Search First

Before writing a new ADR, look through the existing ones (default location: `docs/adr/`). If the decision was already made, read it — don't silently contradict or duplicate it. If you are reversing a past ADR, the new one supersedes it explicitly (reference its number).

## Write the ADR

One file per decision: `docs/adr/NNNN-short-title.md` (zero-padded sequential number). Keep it short — a screen, not an essay.

```
# NNNN. <short decision title>

- Status: proposed | accepted | superseded by ADR-XXXX
- Date: YYYY-MM-DD

## Context
What forces are at play — the problem, constraints, and assumptions that make this a real decision. Pull from project business context where relevant.

## Decision
What we are doing. State it as a fact: "We will …"

## Options Considered
- Option A — what it is, why chosen/rejected.
- Option B — …

## Consequences
What becomes easier, what becomes harder, what we now have to live with. The costs, not just the wins.
```

## Rules

- **Immutable.** An accepted ADR is not edited to change the decision. To change course, write a NEW ADR that supersedes it and flip the old one's status to "superseded by ADR-XXXX."
- **Numbered sequentially**, never reused.
- **Honest consequences** — record the costs and the things that got harder, not only the upside. A consequences section with only wins is a sales pitch, not a record.

## Common Mistakes

- Editing an old ADR to reverse it instead of superseding it — destroys the history of *why*.
- Writing ADRs for trivial or reversible choices — noise that buries the real ones.
- Skipping the search and re-deciding something already settled.
- A consequences section that lists only benefits.
- Novel-length ADRs nobody will read — keep it to one screen.

**Pairs with:** `bardak:less-is-more` — its path analysis and `.claude/business-context.md` feed this ADR's Context and Options sections.
