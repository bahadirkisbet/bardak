---
name: verify-the-premise
description: Use constantly — whenever you are about to act on, suggest, or decide something that rests on an assumption: a claim, a review finding, a doc, a remembered fact, a ticket, or your own belief about how the code behaves.
---

# Verify the Premise

Never assume. Decide, suggest, and act on **data** — observed behavior, real code, actual output — not on what you or anyone expects to be true.

This is a behavior, not a step you do once. Before you act on a belief, ask: **do I know this, or am I assuming it?** If assuming, verify first.

## Iron Law

**NEVER ACT ON AN ASSUMPTION — READ IT, RUN IT, OR TRACE IT FIRST.**

## The Rule

A premise and a conclusion can each be independently right or wrong. A correct conclusion drawn from a wrong premise is luck; a wrong conclusion from a correct premise is a missed fix. Check the premise *and* the conclusion against reality before acting on either.

## What "Verify" Means

- **Read the code**, don't recall it. The function you remember may have changed.
- **Run it / observe the output**, don't predict it. "This should return X" is a hypothesis until you see X.
- **Trace the actual path.** "The lower layer already retries" is only actionable if it actually does — confirm which layer retries before deleting the other.
- **Check what THIS source emits**, not what the class of thing usually emits. "This 429 branch is dead" requires confirming this endpoint emits 429 and not, say, 502.

## Apply To

- Review findings — yours and others'. Verify the claim before you fix or dismiss it.
- Docs, comments, memories, tickets — they drift from the code. Trust the code.
- Your own "I know this works" — the most expensive assumption. Confirm it.
- A user's stated cause — respectfully verify; they may be reporting a symptom, not the cause.

## When You Cannot Verify

Say so. State the assumption explicitly, what would confirm it, and the risk if it's wrong — then let the decision account for the uncertainty. An unverifiable premise that is flagged is safe; an unverified premise acted on silently is the failure.

## Red Flags — STOP

| Thought | Reality |
|---|---|
| "I'm pretty sure this function does X" | Pretty sure is a guess. Read it. |
| "The docs/comment say it works this way" | Docs drift from code. Trust the code. |
| "The lower layer already handles it" | Confirm which layer, on THIS path, before relying on it. |
| "This branch is obviously dead" | Confirm what this source actually emits before deleting it. |
| "It worked last time, so it works now" | Last time is not this time. Observe it. |

## Common Mistakes

- Acting on a remembered API/signature instead of reading the current one.
- Accepting a review finding's premise without tracing the real behavior.
- Predicting output instead of running and observing it.
- Generalizing ("X usually does Y") onto THIS specific case without checking it.
- Letting a confident claim substitute for evidence — confidence is not data.

**Pairs with:** `bardak:blind-review` and `bardak:pipeline-verification` (verify each finding and the real path before acting), and `bardak:no-silent-errors` (confirm a fault path is real, not assumed).
