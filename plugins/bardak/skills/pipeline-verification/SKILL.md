---
name: pipeline-verification
description: Use after any change, before calling it done or claiming it works — especially a change that touches shared code, a contract, or a user-visible path. Triggers whenever you are tempted to rely on unit tests alone.
---

# Pipeline Verification

A passing unit test means a unit works. It does not mean the change works, and it does not mean the change didn't break something else. Verify end to end, through the path a user actually exercises, and trace what else the change can reach.

**Announce at start:** "Verifying end to end, not just unit tests."

## Iron Law

**"TESTS PASS" / "IT COMPILED" / "CONTAINER STARTED" IS NOT "IT WORKS".**

## The Two Questions

1. **Does the real pipeline still work?** Exercise the change through the actual user-visible boundary — the request, the job, the screen — not an isolated function.
2. **What else does this touch?** A change rarely stays local. Trace its blast radius and check the neighbors.

## Step 1: Map the Blast Radius

Before declaring done, list what the change can affect:

- Callers of every function/endpoint you changed.
- Shared state, schemas, or contracts you touched (their other readers and writers).
- Downstream consumers — other services, the frontend, background jobs, caches.
- Anything that depends on the old behavior you just changed.

If you changed a contract, the other side of that contract is in scope.

## Step 2: Verify End to End

- Run the change through the **real path** — the smallest live exercise that crosses the changed boundary: an actual request/response, a job from enqueue to effect, a user action to its visible result.
- "The container started" / "it compiled" / "the unit test passed" is **not** verification. Verify the user-visible effect.
- Check the neighbors from Step 1 still behave — at least the ones the change can plausibly reach.

## Step 3: Report Honestly

State exactly what you verified and how, and what you did NOT.

- "Verified: X end to end via Y, observed Z."
- "Not verified: W — couldn't run it because …; residual risk is …"
- If a required check can't run, give the exact command and the blocker. Never imply coverage you don't have.

## Red Flags — STOP

| Thought | Reality |
|---|---|
| "Unit tests are green, so it works" | Units work. The feature and its neighbors are unverified. |
| "It compiled / the container started" | That's a precondition, not verification. Exercise the real path. |
| "The change is local — nothing else is affected" | Trace the blast radius before believing that. |
| "The frontend/consumer probably still works" | You changed a contract; assume nothing across it — check it. |

## Common Mistakes

- Treating green unit tests as proof the feature works.
- Verifying the function but never the user-visible pipeline.
- Ignoring blast radius — fixing A, silently breaking B that shared the path.
- "Container started" / "compiles" reported as "done."
- Claiming end-to-end coverage that was never actually run.

**Pairs with:** `bardak:verify-the-premise` (report observed data, not assumed coverage); invoked by `bardak:bugfix-tdd` and `bardak:blind-review` before calling work done.
