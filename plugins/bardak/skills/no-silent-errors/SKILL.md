---
name: no-silent-errors
description: Keep failure outcomes distinguishable from valid empty data when changing error handling, fallbacks or required-data contracts. Not a mandate to harden every value or turn expected absence into an exception.
---

# No Silent Errors

Unexpected failure must not masquerade as successful empty/default data. Preserve the domain's legitimate absence, recovery and partial-success behavior.

## Model the actual outcomes

Trace the caller and boundary before changing an error contract. When correcting an existing behavioral bug, load and follow `bugfix-tdd` to observe a failing regression before editing the implementation; error-handling work does not bypass that evidence. Distinguish required data, optional absence, expected domain rejection, partial result and unexpected failure.

Use the project's existing typed results, exceptions or discriminated unions. Validate untrusted external and persisted input at the responsible boundary; a static type alone does not validate runtime data. Do not use assertions for production trust-boundary checks. Avoid introducing a parallel Result framework or wrappers without a concrete need.

A missing required field differs from an explicit empty value. Inspect historical data and other writers before declaring a persisted field universally present. Preserve compatibility or plan an authorized migration.

## Keep failure visible at the right boundary

- Handle known recoverable failures explicitly. A fallback can be correct when its semantics are part of the contract and the degraded outcome remains visible where required.
- Raise or return a typed failure for broken contracts. Required configuration should fail validation rather than become a plausible empty setting.
- Log unexpected failures once where they become an outcome, with traceback and safe correlation context. Re-raise-only layers need not duplicate logs.
- Keep credentials and customer content out of logs and public errors. Sanitized tracebacks belong in restricted internal diagnostics, never public responses. Give callers the failure contract they expect.
- Catch broadly only at a responsible isolation boundary that preserves the failure state; do not swallow cancellation or continue after invalid partial writes.

A missing log entry does not establish that a path never ran. Verify the logger, sink and query scope before using absence as evidence. Recovery should preserve data integrity and make retry/partial effects explicit.

Check both failure behavior and legitimate empty/optional behavior. Error handling that turns a valid absence into an outage is also a regression.
