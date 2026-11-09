---
name: blind-review
description: Independently review a completed change against its requirements and connected code before commit or merge. Scale depth to behavioral risk; also use for an explicitly requested cold audit. A review request alone does not authorize fixes or publication.
---

# Blind Review

Use an independent reviewer without the implementer's narrative. Independence means a fresh context, not merely a different agent name or a second pass in the same conversation.

## Fix the scope before dispatch

Give the reviewer the repository/worktree path, exact base/head or working-tree snapshot, applicable repository rules, and original requirements. Include untracked files that belong to the change. A factual changed-file list or diff is useful scope; it is not an implementation narrative. Let the reviewer follow callers, other readers/writers and tests beyond that list.

Choose the intent:
- Requirements/spec for a change: did it solve the requested problem and preserve existing behavior?
- Approved plan when design drift is the question. Distinguish justified deviations from defects.
- No intent artifact only for an explicit cold audit. Do not infer missing product requirements.

Do not include the author's self-review, claimed test outcomes, suspected findings or proposed fixes. If fresh context is unavailable, disclose the limitation; do not call a self-review independent.

## Dispatch one reviewer per round

Use an available independent agent when delegation is allowed. A second reviewer is useful only for a distinct unresolved risk or an explicit requirement; model count is not evidence. External review tools require authorization to send their inputs.

Give a bounded, read-only task:

> Review the specified snapshot and original requirements. Read applicable instructions and connected code. Do not edit files, implement the parent task, post messages, resolve threads or delegate. Report each actionable finding with location, trigger, observed evidence and consequence. Label inference and unavailable evidence. Report coverage and remaining risks even if no defects are found.

Read relevant accepted ADRs and superseding records for structural changes. Report whether the change conforms; distinguish an explicitly authorized replacement from unexplained drift. Review security, data safety, compatibility, failure/recovery behavior and deployment ordering where the change reaches them. A small auth change can need deeper review than a large mechanical edit. For documentation changes, read the complete affected document and its references.

A wrong checkout, inaccessible implementation, tool failure or missing report is **blocked/incomplete review**, not a product defect or a pass. Check the target before retrying. A zero-finding review is valid when its scope and evidence are credible; do not manufacture findings.

## Validate findings before acting

For each finding, trace or reproduce its premise against the reviewed snapshot. Record accepted, rejected with evidence, or unresolved. A severity label is not proof. Resolve disagreement against code, requirements and observed behavior, not reviewer votes.

An audit-only request ends with the report. Under existing fix authority, fix confirmed in-scope defects and run the relevant checks. Re-review material changes, especially changed contracts, auth or data handling; do not repeat unchanged checks without a reason.

Report reviewed snapshot, coverage, confirmed findings, unresolved blockers and residual risk. A changed head invalidates affected review conclusions. Commit, merge, deployment and external messages remain subject to the user's authorization and repository policy.

Related: `verify-the-premise` for claim validation; `pipeline-verification` for observing the changed runtime path. Load them only when needed, using the installed skill path/name rather than assuming a particular harness namespace.
