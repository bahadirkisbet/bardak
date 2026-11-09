---
name: less-is-more
description: Compare realistic options for a significant architecture or design decision using the user's goal, existing system and business constraints. Not for routine local implementation choices or mechanical edits.
---

# Less Is More

Choose the smallest design that fully serves the requested outcome and known constraints. Reduction must preserve required validation, accessibility, security and data integrity.

## Understand the decision

State the intended outcome without replacing the user's chosen product or scope. Read the relevant existing implementation, accepted ADRs (including superseding records) and project context before proposing new machinery. Name any decision the proposed design would replace; resolve that conflict rather than silently ignoring it.

Use the project's designated knowledge source. Do not create a provider-specific business-context file when shared context already exists. Treat old notes as leads; revalidate facts that determine this decision.

Ask only for a missing fact that materially changes the choice. Continue independent work while waiting. For reversible details within authorized scope, use a stated reasonable assumption rather than requiring another approval.

## Compare viable paths

Present the genuine alternatives and their assumptions before the recommendation. Include reuse or doing nothing when either meets the need. Do not invent a fixed quota of alternatives when only one is viable.

Compare build effort, operational cost, reversibility and fit to known business constraints. Separate observed facts from estimates. Name the fact that would change the recommendation.

Prefer the existing component, platform feature or installed dependency when it fully works. A named future consumer can justify a small boundary now; speculative caching, registries and configuration cannot justify themselves. Use `more-is-less` only when that boundary decision is actually present.

## Preserve decisions without manufacturing memory

Before implementing a significant settled choice, identify its covering ADR or record it through `adr` when documentation is within scope. Include the rejected alternatives, consequences and observable acceptance criteria. Advice is not an accepted decision.

Persist new business knowledge only when supported by evidence and authorized by the user's request or established project policy. Use the canonical destination, keep company and personal scopes separate, and reread before a narrow edit. A pending inference is not a confirmed fact. No new durable knowledge means no write.

Do not turn each consultation into a new file, rule or approval cycle. Show tradeoffs and the recommendation; name any unresolved material assumption.
