---
name: bugfix-tdd
description: Reproduce a behavioral bug with a failing regression test before fixing it, then prove the fix and relevant surrounding behavior. Not for new features, documentation edits or behavior-preserving refactors.
---

# Bugfix TDD

For a behavioral bug, observe the failure before editing the implementation. A test failure is evidence only when it reaches the reported defect.

1. Confirm expected behavior and trace the actual entry point, callers and existing tests. Distinguish the reported symptom from an assumed cause.
2. Write the smallest regression test asserting the correct observable behavior. Run it against the buggy implementation and preserve the test process exit status; run the test directly, or enable pipefail if filtering its output. A trailing filter must not turn a failure into command success.
3. Inspect the failure. Missing imports, unavailable services, compilation errors and unrelated assertions do not prove the bug. Correct the harness or label the blocker before claiming red. Do not edit the implementation until this failure has been observed; an unavailable test runner permits investigation and a proposed test, not an unverified implementation fix.
4. Make the smallest in-scope fix at the responsible layer. Preserve validation and error handling; update affected callers and fixtures.
5. Observe the same regression test pass. Run relevant surrounding tests and repository-required checks. Verify the affected boundary when runtime behavior changed.

## When evidence is difficult

An unavailable environment or nondeterministic failure does not prove the diagnosis wrong. Gather a bounded reproduction, traces or a deterministic test of the responsible contract. State what remains unknown. Do not invent a red result, loosen an acceptance gate or repeatedly run a failing setup without new evidence.

If the fix already exists, run the new test against the pre-fix implementation in an isolated scratch copy/worktree, then against the fix. Preserve another writer's checkout. Report this as retrospective regression proof, not test-first development. A structural assertion that could stay green while behavior breaks needs a meaningful mutation or behavior check. Verify that the intended mutation actually changed the target, observe the expected failure, then restore and observe the baseline pass.

For a defect that cannot be automated, retain reproducible before/after steps and observations. Follow repository policy on required tests or exceptions; a skill does not waive those gates. A text/configuration correction needs relevant validation, not an artificial application regression test.

Report the buggy snapshot, failing command and failure reason, fixed snapshot and observed pass. Keep unavailable CI or live checks separate. Apply `no-silent-errors` only if failure handling changes and `pipeline-verification` at the boundary the fix reaches.
