---
name: more-is-less
description: Use when a structural decision at a boundary — a schema, data model, integration or variant seam, or public contract — has a named, already-present-or-stated future need, and the cheap version now would cost a painful migration or shotgun surgery later. The disciplined case for spending more structure up front: build the seam, extension point, or value type now so the next variant is additive, not surgery. Reach for it on smells like `if type == ...` dispatch, a generic layer importing a concrete one, stringly-typed or positional-tuple boundaries, or a change that forces a backfill/migration. NOT for speculative flexibility added "in case" or "someday" — the future need must be named and concrete, not hypothetical. And only for structure at a boundary; runtime machinery (caches, locks, retries, guards) stays deferred until a measured failure, which is less-is-more.
---

# More Is Less

Some code is cheaper written long now than cheap today. At a structural boundary — a schema, a data model, an integration or variant seam, a contract — the lazy shape *looks* smaller but bills you later as a migration, a backfill, or shotgun surgery across the generic layer. This skill is the disciplined case for paying that cost up front: build the seam, the extension point, the value type now, so the next variant is *additive* instead of surgery.

It is the deliberate counterweight to lazy minimalism — and it **refines, never overrides**, `bardak:less-is-more`. The split is sharp: **structure at a boundary is built right; runtime machinery is deferred.**

**Announce at start:** "Using more-is-less — investing structure now at this boundary so the next change is additive."

## Governing Rule

**Invest in structure now exactly when the cheap version would cost a future migration — and the future need is named, not imagined. Defer runtime machinery (caches, locks, retries, guards) until a real failure demands it.**

Under-abstraction and over-abstraction are equally defects. This skill targets only the first, and only at a boundary.

## When to Use

- A schema / data-model / persistence decision — the highest-stakes boundary; the wrong shape forces a painful reparenting later.
- An integration or provider/variant seam where a second (third, Nth) variant is foreseeable.
- A public contract or boundary type others will depend on.
- A smell saying the seam is already wrong: `if type == "x"` dispatch, a handler table keyed by variant, the generic/shared layer importing a concrete one, stringly-typed or positional-tuple boundaries.
- Not for: runtime machinery without a measured failure, one-off scripts, a localized function body, or "we might need it someday" with no named need — that is speculation; stay lazy.

## The Earn Test — all four, or stay lazy

1. **It is structure, not machinery.** A boundary, schema, seam, or type — not a cache, lock, retry, or guard. Machinery waits for a measured failure.
2. **The future need is named.** A stated next variant, a known second consumer, persistence that must evolve. "Might someday" is not named — that is speculation, and `bardak:ponytail` wins.
3. **The cheap version fails the N+1 test.** Ask: *what happens at variant N+1?* If adding the second case means editing the generic/shared layer, the seam is in the wrong place — build the port now.
4. **The cheap version forces future ceremony.** If shipping it small now means a later backfill, migration, new index, or reparenting, the cheap design is the expensive one.

If any fails, you are over-engineering — stop, and let `bardak:less-is-more` / `bardak:ponytail` govern.

## The Mentality — recognize the shape, apply the solidified form

When a recurring shape appears, name it and reach for the form that is already battle-tested: it states intent and is cheaper to maintain than a clever bespoke version. The shapes worth knowing:

- **Behavior keyed by a type/variant** (`if provider == …`, switch on kind) → one **port**: an interface/`Protocol` the generic layer talks to, with concrete implementations registering themselves behind a registry/factory. Adding a variant becomes additive — no edit to the generic layer.
- **A generic model sprouting special-case columns/branches** → a generic **extension point** (a metadata/JSON field, or a dedicated model), not another special case.
- **An entity that may later need merge/dedup** → a **canonical entity + alias/identity** shape, so the future operation repoints instead of reparents.
- **Primitive obsession / stringly-typed** → an **enum** over string literals, a **value type** over a bare `str` (a `UserId` is not a `str`).
- **Positional/tuple returns** → a **named/frozen record** — an order-swap in a tuple is a silent failure.
- **A long procedural blob** → **extract** small, intent-revealing methods or a class.

For machinery you *have* justified, reach for a well-tested library over a hand-rolled version (a retry/backoff/circuit-breaker lib beats a bespoke loop).

## Boundaries Are One-Directional

The generic core stays generic: shared/core models, services, and hot paths carry no variant-specific fields or logic — those live behind the port. The tell that a boundary leaked is not only a column; it is an **import or an equality check**. If the generic layer imports a concrete variant or compares against its name, the seam is already broken.

## Red Flags — STOP, you are *over*-applying

| Thought | Reality |
|---|---|
| "Make it generic in case we need it" | No named need = speculation. Build it when the need is named; `ponytail` wins now. |
| "Add a lock/retry/guard to be safe" | Runtime machinery. Defer until a failure is measured. |
| "This abstraction is elegant" | Elegance isn't a justification. Name the future cost it buys down, or drop it. |
| "Fold these three refactors into this PR" | Investment isn't scope creep. Split orthogonal refactors out. |
| "It needs a migration and a backfill, but it works" | Ceremony is a design smell. A different shape likely removes the need — reconsider the design first. |

## Red Flags — STOP, you are *under*-applying

| Thought | Reality |
|---|---|
| "Just one more `if type == …` branch" | That branch is the smell. If N+1 edits the generic layer, build the port now. Don't cite YAGNI to dodge a real seam. |
| "Ship the small schema now, migrate later" | "Later" is a backfill and a reparent. If the future shape is named, build the additive shape now. |
| "Return a tuple, it's fewer lines" | An order-swap is a silent bug. A named record is the cheaper one. |

## Common Mistakes

- Treating every repetition as a reason to abstract — the gate is a *named future need crossing a boundary*, not a repetition count.
- Adding runtime machinery with no measured failure — that is the counterweight skill's job to refuse.
- Building the port but leaving a concrete import or name-equality in the generic layer — the boundary still leaks.
- Scaling machinery beyond the scale that actually exists.

**Pairs with:** `bardak:less-is-more` (the counterweight it refines — that one governs runtime complexity and reduction, this one governs structure at a boundary), `bardak:no-silent-errors` (the typed seams and named records here exist so a failure cannot be expressed silently), and `bardak:adr` (record the structural choice and the named future need that justified it).
