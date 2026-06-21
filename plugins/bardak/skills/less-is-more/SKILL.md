---
name: less-is-more
description: Use before committing to any architecture, design, or non-trivial technical direction — when the user asks "how should we build X", proposes a system or feature, or faces a structural decision. Surfaces explicit paths and business-grounded tradeoffs, and learns the business each time so future calls align better.
---

# Less Is More

Architecture decisions are won or lost on understanding the *intent* and the *business* — not on cleverness. You are usually NOT fully aware of the business. This skill forces you to surface the real intent, lay out explicit paths, weigh tradeoffs against what you actually know of the business, and — every single time — record what you learn so the next decision is sharper.

This skill operates at the architecture / design altitude. Code-level minimalism (shorter functions, fewer lines, stdlib over custom) is a separate concern handled by a code-simplicity reviewer; do not duplicate it here.

**Announce at start:** "Using less-is-more to map paths and tradeoffs against business context."

## When to Use

- "How should we build / structure X?", a new service / module / feature, a schema or data-flow decision, build-vs-buy, a structural refactor.
- Any decision where picking wrong is expensive to reverse.
- Not for: localized code style, a single function's implementation, mechanical edits.

## Step 1: Extract the Intent

State the real goal in one or two sentences — the outcome the user wants, not the literal mechanism they named. Users often ask for a solution; find the problem underneath it.

If the intent is ambiguous, ask ONE clarifying question before going further. A wrong intent makes every path below wrong.

## Step 2: Load Business Context

Read the project's business-context note (default: `.claude/business-context.md`; create it if missing). It holds what you have learned about this project's domain, constraints, priorities, and past tradeoff decisions.

You are not the domain expert. This note is how you borrow the expertise you have accumulated across past sessions. Use it to ground everything below. Where the note is silent on something that matters, treat that as a known blind spot for Step 4.

## Step 3: Lay Out Explicit Paths — BEFORE Tradeoffs

Present 2–4 concrete, named paths. For each: what it is, what building it actually entails, what it assumes. Be specific — "Path A: extend the existing job runner with a new task type" not "we could reuse existing code."

Do NOT jump to a recommendation yet. The user needs to see the real option space before any verdict narrows it.

## Step 4: Tradeoffs, Grounded in the Business

Only now weigh the paths — against the business context, not abstract purity:

- Cost to build, cost to reverse, cost to operate.
- Fit to the known constraints and priorities from Step 2.
- The simplicity lens: fewer moving parts wins when nothing in the business argues otherwise.

**Flag your blind spots.** Wherever a tradeoff depends on business facts you do NOT have, say so plainly: "This hinges on X — I don't have that. If X, Path A; if not-X, Path B." Honesty about what you don't know is the point — it invites the user to fill the gap, which becomes Step 5's memory.

Then give a recommendation, conditioned on the open questions.

## Step 5: Learn the Business — EVERY Time

This is mandatory, not optional. The skill is worthless without it.

After the decision (or the user's correction of it), append to `.claude/business-context.md` what you learned:

```
## <YYYY-MM-DD> — <topic>
- Domain fact / constraint / priority learned:
- Decision made, and the *business* reason (not just the technical one):
- Tradeoff the user weighted differently than you expected:
```

Over many uses this note turns "I don't know the business" into "I know this business." Each invocation must leave the note richer than it found it.

## Common Mistakes

- Recommending before showing the explicit paths — the user can't see what you ruled out.
- Weighing tradeoffs on engineering aesthetics instead of business reality.
- Pretending to know the business — hiding blind spots instead of flagging them.
- Skipping Step 5 — a session that taught you nothing persistent wasted the skill.
- Reading "less" as "fewest lines." Here "less" means fewer moving parts and less you will regret, decided against the business.
