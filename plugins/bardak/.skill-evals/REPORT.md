# Bardak skills — triggering improvement report

**Goal:** improve all 8 plugin skills (triggering accuracy + body quality), evals first, business-agnostic.
**Method:** routing eval — score every bardak description against each other *and* the real competing installed skills (superpowers, ponytail), measuring recall (fires when it should), collision (fires when another should), and steal (loses to a competitor). One `claude -p` classification call per query.

## Why not the skill-creator `run_loop`

`run_loop` registers each skill in isolation and counts a trigger at the first Skill-tool call within 30s. In this environment that produced **all-zeros** — Opus's time-to-first-tool-call exceeds 30s, and a direct probe showed a plain "fix this bug" prompt fires `superpowers:systematic-debugging` (co-firing), proving these skills compete with ~40 installed skills that an isolated loop can't see. Optimizing in isolation would push bardak descriptions *broader* to "win" — the opposite of the fix needed. So the eval was rebuilt to score the descriptions against the real competitive field. Harness kept at `router/route.py` (+ `router/queries.json`, 39 labeled queries) as a reusable triggering regression test.

## Headline result

| metric | before (1×) | after (majority-of-3) |
|---|---|---|
| recall (fires when expected) | **33/33** | **33/33** |
| generic "none" queries leaking a skill | 0/6 | **0/6** |
| total wrong-fires (collisions) | **9** | **3** |
| `adr` firing during design deliberation | **5/5** | **1** (borderline) |

Recall never moved — no skill lost its trigger. Wrong-fires cut from 9 to 3.

## Diagnosis

The skills were **not** under-triggering and did **not** lose to competitors. The one systematic defect was **over-firing**: `adr` fired on every "how should we build/structure X?" design question — because its description triggered on "making a hard-to-reverse decision," which is the *deliberation* phase that belongs to `less-is-more`. ADR's real job is *recording* a decision, not deliberating it.

## Changes (3 descriptions + 1 body line; other 5 skills untouched)

- **adr** — re-anchored on *recording/documenting a finalized decision*; added "this captures a decision, it does not deliberate one (that is less-is-more)" to description, plus a matching "Not for deliberating a decision still in flight" line in the body. → eliminated 4 of 5 false fires.
- **no-silent-errors** — replaced the over-broad "triggers on almost any implementation or review" with a failure/error-path anchor, and explicitly excluded parsing/formatting. → killed a regression where "write a phone-number regex" triggered it via "validating data."
- **verify-the-premise** — kept the constant-reflex intent but added the distinction "distinct from verifying a finished change works end to end (pipeline-verification)."

## Remaining 3 wrong-fires are legitimate dual-relevance, not defects

- bug-with-empty-response → also `no-silent-errors` (a wrong/empty response *is* a failure-visibility concern)
- "build vs buy for feature flags" → also `adr` (its description lists build-vs-buy; lone residue, 2/3 votes)
- "delete the dead 429 branch?" → also `no-silent-errors` (deleting an error branch is NSE-adjacent)

In each, both skills genuinely apply. Chasing them risks recall for no real gain.

## Bodies

Assessed as already mature (tight, good "why", Red Flags, cross-refs, generic). Only the adr deliberation-boundary line was added — the rest needed no change.

## Notes / caveats

- The router eval is a *proxy* for real triggering (classification turn, not mid-task invocation), but it directly tests description-vs-description routing, which is what we tuned. Run-to-run variance is real at 1×; majority-of-3 smooths it (recall was stable at 33/33 across all runs regardless).
- Cost ≈ $0.13/call (~$5/pass at 1×, ~$15 at 3×). Re-run anytime: `python router/route.py --runs 3`.
- `.skill-evals/results/` and `eval-sets/` are gitignored; `router/` (harness + queries) is kept.
