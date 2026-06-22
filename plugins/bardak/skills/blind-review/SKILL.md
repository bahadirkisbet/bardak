---
name: blind-review
description: Use when a major implementation is complete and per-task reviews have passed, before merging a multi-file feature or a finished plan — the final quality gate. Reviewers read the code independently and never see the implementer's account of the work; you pick which intent artifact they judge against — none (cold audit), the spec (compliance), or the plan (drift). Not for single-file fixes, docs-only changes, or behavior-preserving refactors.
---

# Blind Review

Dispatch reviewers that read the code independently and judge it on its own merits. The one thing they NEVER see is the implementer's account of the work — no "what I did" summary, no file list, no self-review. That account tells a reviewer what to look at and, by omission, what to overlook. Strip it, and the reviewer finds the gap.

What you *do* hand them is one **intent artifact** — and which one sets the mode:

| Mode | Artifact given | Question it answers |
|---|---|---|
| **No context** (default) | nothing but the code | "Is this code sound?" — bugs, security, data safety, smells |
| **Spec** | the original requirements/ticket | "Did we build what was asked?" — compliance gap |
| **Plan-vs-code** | the intended implementation plan | "Did the build follow the design?" — drift between plan and code |

The artifact is always a statement of *intent* (what should be true), never a *narrative* of what the implementer claims they did. That distinction is what keeps every mode blind.

**Announce at start:** "Running blind review (`<mode>`) — independent reviewers, no implementer narrative."

## When to Use

Use after: multi-file features, plan execution completion, any change where the implementer also reviewed their own work.
Skip for: single-file bug fixes, documentation-only changes, behavior-preserving refactors.

Pick the mode by what you have and what you fear:
- No spec written, or you want the most independent read → **No context**.
- A spec/ticket exists and you fear missed or misread requirements → **Spec**.
- You just executed a written plan and want to catch where code silently diverged → **Plan-vs-code**.

When unsure, run **No context** first (it assumes the least), then escalate to Spec or Plan-vs-code if you need intent-level findings.

## Step 1: Gather the Intent Artifact

For the chosen mode, collect exactly one artifact — or none:

- **No context:** nothing. Skip to Step 2.
- **Spec:** the original requirements — spec, plan section, or ticket description.
- **Plan-vs-code:** the implementation/design plan as it was *intended* (the approved plan, the design doc), not a recap written after the fact.

**Never include**, in any mode: implementation summaries, file lists, "how it was built" notes, the implementer's self-review. Those bias the reviewer toward the author's mental model. (In Plan-vs-code, the plan is the *intended* design — a post-hoc "here's what I ended up doing" writeup is exactly the narrative to exclude.)

## Step 2: Dispatch Independent Reviewers (parallel)

Launch at least one, ideally two reviewers in parallel. The more independent the second reviewer's vantage — a different agent, or an external model via MCP if one is connected — the more it catches.

Reviewer prompt template (fill the bracketed parts per mode):

```
You are a blind reviewer — a hostile auditor. You read the codebase independently and have NO account of how it was implemented.

Read the code. Evaluate it against the intent artifact below (if any) and on its own merits.

[ INTENT ARTIFACT — one of: ]
[ No context:    "No spec or plan provided. Audit the code on its own merits." ]
[ Spec:          "SPEC:\n{paste spec}" ]
[ Plan-vs-code:  "INTENDED PLAN:\n{paste plan}\nReport every place the code diverges from this plan — additions, omissions, substitutions." ]

Check:
1. Intent match — [Spec: every requirement implemented, nothing extra, nothing misread] [Plan-vs-code: every plan step present and faithful; flag drift] [No context: skip — judge soundness only]
2. Security — empty defaults, missing auth, fail-open paths, race conditions, IDOR.
3. Data safety — backward compatibility, migration paths, malformed-input handling.
4. Missing error paths — token expiry, network failure, partial writes, retry/recovery.
5. Deployment — missing env vars, config, migrations, worker/queue requirements.

CRITICAL GUARD: If you cannot find the implementation, produce the report anyway. "Code not found" is a Critical finding, not a stop signal.

Report format:
### Critical (blocks merge)
### Important (fix before merge)
### Minor (fix or note)
### Intent Compliance (line by line — spec requirements or plan steps; omit in No-context mode)
### Risks
```

If a second independent model is available (e.g. via an MCP tool), give it the same prompt and artifact. If none is available, skip it silently and note "second reviewer skipped — none available."

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

- Leaking the implementer's narrative into the artifact — defeats the entire point, in every mode.
- Feeding a post-hoc "what I did" writeup in Plan-vs-code mode instead of the intended plan — that re-introduces the bias and turns drift detection into rubber-stamping.
- Trusting a "zero findings" report without checking the reviewer read real files.
- Running it on trivial changes — reserve it for the final gate on real features.
- Skipping the re-run after fixing Critical findings.

**Pairs with:** `bardak:verify-the-premise` (verify each finding against real behavior before acting) and `bardak:pipeline-verification` (confirm fixes end to end before merge).
