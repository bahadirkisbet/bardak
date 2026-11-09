---
name: pipeline-verification
description: Verify a completed change at the boundary it affects and report the limits of the evidence. Use for runtime, contract, UI or configuration changes; scale checks for documentation and mechanical edits.
---

# Pipeline Verification

Choose evidence that supports the actual completion claim. A passing unit test, healthy container, successful merge or installed plugin each proves a different thing.

## Identify the target and affected path

Record the changed checkout/snapshot and the acceptance behavior, including observable criteria from applicable accepted ADRs. An ADR being written or accepted does not prove its implementation was verified. Trace relevant callers, persistent readers/writers, downstream consumers and async work. For a contract change, inspect both sides; do not silently expand implementation into unrelated systems.

Before a live check, verify which build, checkout, configuration and account the running process serves. A healthy stale process does not verify the edited code. Preserve other writers' work and shared services.

## Run the smallest sufficient checks

- Runtime change: cross the changed boundary through the actual request, job or user interaction and observe its result. Check relevant failure and retry paths when changed.
- UI change: exercise the interaction at the relevant viewport, input method and accessibility setting. Browser evidence alone does not establish native-device behavior.
- Plugin/configuration change: distinguish valid files, installation/discovery and an actual triggered invocation. A doctor pass is not proof a hook ran.
- Documentation/mechanical change: validate affected links, examples, syntax or consistency. Do not start an application stack solely because a Markdown file changed.

Use existing fixtures and checks. Run repository-required checks, then expand only for a remaining risk, changed code or failure. A mock proves the mocked contract, not a live provider. Label synthetic evidence. For nondeterministic evaluations, preserve the baseline, repeat the comparison and report variability; one favorable run does not establish improvement.

Live checks stay within authorized environments and side effects. Prepare safely available local evidence before requesting any missing production or external-write authorization. Do not turn verification into deployment.

## Own temporary resources

Before starting a database, server or worker, register teardown for the exact resources you create, including failed startup and interruption. Preserve test failure status, use normal shutdown, verify cleanup, and never stop shared resources. Disclose intentionally retained resources and their owner. Cleanup cannot be guaranteed after a host crash or uncatchable termination.

## Report what the evidence establishes

State the target, command/action, observed result and unavailable stage. Distinguish local checks, integration, CI on a particular head, merge, deployment and user acceptance. Pending, unavailable and failed are different states; none means pass.

If blocked, report the exact missing prerequisite and the smallest next check. Do not claim completion of the blocked stage or rerun identical failures indefinitely. A handoff carries the target, completed evidence, blockers and remaining action; it does not create new authorization.
