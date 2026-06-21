---
name: blind-review
description: Use when a major implementation is complete and per-task reviews have passed, before merging a multi-file feature or a finished plan — the final quality gate. Not for single-file fixes, docs-only changes, or behavior-preserving refactors.
---

# Blind Review

Dispatch reviewers that receive ONLY the original spec — no implementation summaries, no file lists, no notes on how the code was built. Each reviewer reads the code independently and judges it purely against what was requested.

**Announce at start:** "Running blind review — independent reviewers against the spec only."

## When to Use

Use after: multi-file features, plan execution completion, any change where the implementer also reviewed their own work.
Skip for: single-file bug fixes, documentation-only changes, behavior-preserving refactors.

Why blind: an implementer's summary tells the reviewer what to look at — and, by omission, what to overlook. Strip it. A reviewer who sees only the spec finds the gap between what was asked and what was built.

## Step 1: Gather the Spec

Extract the original requirements — the spec, plan section, or ticket description.
**Do NOT include:** implementation summaries, file lists, "how it was built" notes, the implementer's self-review. Those bias the reviewer toward the author's mental model.

## Step 2: Dispatch Independent Reviewers (parallel)

Launch at least one, ideally two reviewers in parallel. The more independent the second reviewer's vantage — a different agent, or an external model via MCP if one is connected — the more it catches.

Reviewer prompt template:

```
You are a blind spec reviewer — a hostile auditor. You received ONLY the spec below. You have NO context about how it was implemented.

Read the codebase independently. Evaluate ONLY against the spec.

SPEC:
{paste spec here}

Check:
1. Spec compliance — every requirement implemented? Anything extra? Anything misinterpreted?
2. Security — empty defaults, missing auth, fail-open paths, race conditions, IDOR.
3. Data safety — backward compatibility, migration paths, malformed-input handling.
4. Missing error paths — token expiry, network failure, partial writes, retry/recovery.
5. Deployment — missing env vars, config, migrations, worker/queue requirements.

CRITICAL GUARD: If you cannot find the implementation, produce the report anyway. "Code not found" is a Critical finding, not a stop signal.

Report format:
### Critical (blocks merge)
### Important (fix before merge)
### Minor (fix or note)
### Spec Compliance (line by line)
### Spec-Derived Risks
```

If a second independent model is available (e.g. via an MCP tool), give it the same spec-only prompt. If none is available, skip it silently and note "second reviewer skipped — none available."

## Step 3: Merge Findings

Combine the reports. Deduplicate. Prioritize:
- Critical from any reviewer → fix immediately.
- Important from any → fix before merge.
- Minor → fix or note.
- Zero issues from every reviewer → suspicious; verify the reviewers actually read the code.

## Step 4: Act

- Critical → fix, then re-run blind review on the fixed code.
- Important → fix before merge.
- Minor → fix or document as tech debt.

## Common Mistakes

- Leaking implementation context into the spec — defeats the entire point.
- Trusting a "zero findings" report without checking the reviewer read real files.
- Running it on trivial changes — reserve it for the final gate on real features.
- Skipping the re-run after fixing Critical findings.

**Pairs with:** `bardak:verify-the-premise` (verify each finding against real behavior before acting) and `bardak:pipeline-verification` (confirm fixes end to end before merge).
