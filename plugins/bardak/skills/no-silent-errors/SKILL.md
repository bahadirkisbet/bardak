---
name: no-silent-errors
description: Use whenever a failure or error path is in play — error handling, exceptions, swallowed failures, fallbacks, or empty/None/default values standing in for missing required data — and when modeling a type so a failure cannot be represented silently. The concern is failures that pass unnoticed; reach for it any time a value, call, or branch could fail without anyone seeing. Not triggered merely because code is involved, or because input is being parsed or formatted — triggered when how something fails, or is kept from failing, is at stake.
---

# No Silent Errors

Every error, failure, and fault path must be visible. No swallowed exceptions, no empty defaults standing in for missing required data, no fail-open. The strongest enforcement is not a runtime check — it is a type that makes the silent failure impossible to express.

This is a reflex, not an occasional pass. Apply it to almost every change.

## Iron Law

**IF IT CAN FAIL UNNOTICED, IT IS A BUG — EVERY ERROR PATH STAYS VISIBLE.**

## The Reflex

For every value, call, and branch, ask: **how does this fail, and would I see it?** If a failure can pass unnoticed, fix it — preferably with types.

## Strong Types First (primary mechanism)

Make illegal states unrepresentable; then the silent failure cannot compile.

- Model presence/absence in the type — `Optional` / `Maybe`, not a magic empty string or `-1`.
- Make failure a value: a typed result (`Result` / `Either`) or a typed exception — not `None` meaning both "error" and "empty".
- No `any` / `unknown` leaking across a boundary. Parse to a typed shape at the edge; downstream code reads typed values directly.
- Exhaustive handling — `match` / discriminated unions the compiler checks, so a new error variant forces a new branch instead of falling through.
- Distinct types for distinct things (a `UserId` is not a bare `str`), so a wrong value is a type error, not a runtime surprise.

## Then Runtime Visibility

Where types cannot reach:

- No bare `except:` / `catch {}` that drops the error. Catch the specific case, then re-raise, wrap, or log-and-fail.
- Validate required external/persisted data at the write/entry boundary and raise on violation — an explicit exception, not `assert` (asserts can be compiled out).
- Fail loud and fast on broken contracts. A missing required config aborts startup; it does not default to empty.
- Log the cause at the point of failure with enough context to act on.

## Required vs Genuinely Optional

The rule targets **required** data and **broken contracts** — not correct boundary modeling.

- Returning `None` / `[]` / `""` for a genuinely optional or boundary value (no next item at a list edge, an absent optional field) is correct domain modeling, not a silent failure.
- The defect is a *required* value silently becoming empty, or an error path quietly producing a plausible-but-wrong result.
- Do not convert correct optional-boundary handling into hard failures by reflex.

## Red Flags — STOP

| Thought | Reality |
|---|---|
| "I'll just catch it and log" | A log nobody reads is still silent. Re-raise, wrap, or fail. |
| "An empty default keeps it from crashing" | It crashes later, with less context. Fail at the boundary instead. |
| "It's probably never null here" | "Probably" is not a type. Make it `Optional` and handle it. |
| "Typing this is too much ceremony" | The type is cheaper than the 2am page when the value is wrong. |
| "Catch broad `Exception` so the flow survives" | The flow doesn't survive — it limps on corrupt state. |

## Common Mistakes

- `try/except: pass` (or `catch {}`) — the canonical silent failure.
- An empty default for required config/input instead of failing at startup/entry.
- One nullable return overloaded to mean both "no data" and "it failed."
- `assert` for validating external/persisted data (disabled under optimization).
- Stringly-typed boundaries (`any` / `dict` / `str`) where a parsed type would have caught the error.

**Pairs with:** `bardak:verify-the-premise` (confirm a fault path is real before trusting it), and applies during `bardak:bugfix-tdd` (don't let the fix introduce a silent failure).
