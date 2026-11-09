---
name: adr
description: Read and enforce relevant architecture decisions before structural implementation or review; record significant new decisions and explicit supersession. Use for data models, service boundaries, public contracts or dependency choices, not routine local edits.
---

# Architecture Decision Records

Preserve what was decided, by whom or under what authority, why, and at what cost. A recommendation is not an accepted decision.

## Read decisions before structural work

Use the project's existing ADR location, numbering and template; default to `docs/adr/` only when none exists. Search by the affected component, contract and decision topic, then read relevant accepted ADRs and their superseding records before designing, implementing or reviewing structural changes. Follow linked decisions only as needed; do not load every ADR. Check current constraints rather than treating a historical decision as permanently applicable.

State which decisions constrain the change and whether it conforms. If code differs from an accepted ADR, report the drift and establish whether the code or decision needs correction; neither silently wins. If the requested change conflicts with an accepted decision, surface the conflict before dependent implementation. Existing explicit authorization to replace that decision is sufficient; otherwise prepare the replacement proposal and continue independent work. Do not silently reverse a decision or ask again when the user has already settled it.

Create a record only within the authorized documentation scope. For a preview-only request, present a draft without changing the repository. Do not create a separate provider-specific decision store.

## Keep one decision per record

Use a short record with:
- Status: proposed, accepted, or superseded by a linked decision.
- Date and decision source/authority. Set accepted only when the decision is actually made within that authority.
- Context: the problem, constraints and material assumptions. Separate observed code/schema facts from assumptions and cite the evidence for consequential technical claims; do not fill missing facts from framework conventions.
- Decision: the chosen course, or the proposal awaiting a decision.
- Options considered: viable alternatives and reasons for choosing/rejecting them.
- Consequences: benefits, costs, compatibility/rollout implications and unresolved risks.
- Verification: observable criteria that would demonstrate the implementation follows the decision, plus links to implementation/tests when available. Mark future checks as planned, not passed.
- Revisit conditions when material: which changed constraint or new evidence would justify reconsideration, not an invented expiry date.

Use existing naming conventions. For sequential numbers, reread the directory immediately before creating a file and avoid overwriting a concurrently added record; renumber the new draft if necessary.

Before finishing an authorized significant structural change, check whether its settled decision is recorded. Reuse a covering ADR; create or update a draft when documentation is within scope, and flag an outstanding decision record otherwise. Do not create an ADR for ordinary local edits.

An accepted ADR's decision is not silently rewritten. To change course, create a new ADR that explicitly references its predecessor. A proposed replacement does not supersede the accepted decision yet. Once the replacement is accepted under the proper authority, narrowly update the old status/link. Verify both references. Keep proposed records open to revision and preserve unrelated edits.

Report whether the artifact is proposed, saved or accepted. Do not infer acceptance from file existence, a previous agent's summary or this skill's invocation.
