---
name: bugfix-tdd
description: Use when fixing any bug — write a test that reproduces the bug and FAILS first, then fix it, then confirm the test goes green. No fix without a failing test that proves it.
---

# Bugfix TDD

A bug fix without a failing test that reproduces it is a guess. Reproduce first — a red test that captures the bug — then fix until it is green. The test is the proof the bug existed and the guard that it stays fixed.

**Announce at start:** "Reproducing the bug with a failing test before fixing."

## When to Use

- Any bug, regression, or "it does the wrong thing" report.
- Not for: net-new features (that's ordinary TDD), pure refactors with behavior unchanged.

## Step 1: Reproduce with a Failing Test

Write the smallest test that exercises the buggy path and asserts the *correct* behavior. Run it. It MUST fail.

If you can't write a test that fails, you don't yet understand the bug. Keep investigating; don't fix blind.

## Step 2: Confirm the Failure Is the Bug

Read the failure. Is it failing because of the actual bug, or because the test is wrong? A test that fails for the wrong reason proves nothing — fix the test until it fails for the bug's reason.

## Step 3: Fix

Make the minimal change that turns the test green. Don't expand scope; don't fix unrelated things in the same step.

## Step 4: Confirm Green + No Regressions

- The new test passes.
- The surrounding suite still passes — the fix didn't break a neighbor.
- Re-read the diff: did you fix the cause, or paper over the symptom just enough to make the test pass?

## Common Mistakes

- Fixing first, adding a test after (or never) — you lose the proof the test catches the bug.
- A test that passes even before the fix — it doesn't exercise the bug.
- A test that fails for the wrong reason — verify the failure mode first.
- Expanding the fix beyond what the test demands.
- Skipping the full-suite run — confirm the fix didn't regress a neighbor.
