---
name: pipeline-verification
description: Use after any change, before calling it done — a change is not verified by unit tests alone. Trace what else it touches and verify end to end through the real user-visible pipeline.
---

# Pipeline Verification

A passing unit test means a unit works. It does not mean the change works, and it does not mean the change didn't break something else. Verify end to end, through the path a user actually exercises, and trace what else the change can reach.

**Announce at start:** "Verifying end to end, not just unit tests."

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

## Common Mistakes

- Treating green unit tests as proof the feature works.
- Verifying the function but never the user-visible pipeline.
- Ignoring blast radius — fixing A, silently breaking B that shared the path.
- "Container started" / "compiles" reported as "done."
- Claiming end-to-end coverage that was never actually run.
