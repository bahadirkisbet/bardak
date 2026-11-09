---
name: more-is-less
description: Decide whether a named consumer, variant or schema evolution justifies a small extension seam now. Use at data-model, integration or public-contract boundaries; not for speculative future flexibility or routine local refactors.
---

# More Is Less

Sometimes a little structure now avoids an expensive migration later. Justify it using a concrete need and the current code; preserve the minimal-design default of `less-is-more`.

## Earn the structure

Establish all of these:
1. A present or explicitly stated need crosses this boundary: a second provider, another consumer or a known schema evolution. A hypothetical future is insufficient.
2. The current cheap design imposes a concrete cost: repeated edits to generic orchestration, incompatible contracts, reparenting or a backfill. Name the affected paths and consequence.
3. An existing seam or a small addition removes that cost without building unused runtime behavior. Compare its present complexity with the avoided cost.

If the evidence is missing, keep the simpler design and state what would justify revisiting it. A migration is a tradeoff, not automatically a design failure.

## Choose the smallest fitting shape

- Reuse the project's port or registry when a genuine provider seam exists. A composition root may import and register concrete implementations; generic orchestration should use the boundary.
- A finite domain switch or a small dispatch table is not automatically broken. Build an interface when the named extension would otherwise force unrelated shared logic to change.
- Choose typed fields, an extension model or validated metadata according to query, integrity and evolution requirements. Do not replace constraints with an unvalidated JSON bag.
- Use named records or value types when they prevent a demonstrated ambiguity at the boundary. Do not impose wrappers on every local value or refactor unrelated code.

## Separate correctness from optional optimization

Security checks, input validation, transactional integrity and concurrency protection required by a known invariant belong in the initial design. Do not wait for an incident to add them.

Optional retries, caches, circuit breakers and performance machinery need an observed bottleneck, a documented provider/framework requirement or an explicit reliability requirement. Use established implementations and a single responsible layer; do not add machinery merely because it sounds safer.

Explain the named need, the chosen seam, present cost and the future edit it avoids. For a significant settled decision, record an ADR within the authorized documentation scope.
