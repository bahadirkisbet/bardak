---
name: retrospective
description: Use when ending a long session, when the user says /retro or /retrospective, or after a session with multiple corrections, friction, or workarounds. Not for short sessions with no friction.
---

# Retrospective

Extract the non-obvious lessons from this session and persist them where they will prevent the same friction next time — with user approval.

**Announce at start:** "Running retrospective to review this session for improvements."

## When to Use

- User says /retro, /retrospective, or "let's wrap up."
- End of a long session with corrections, friction, or workarounds.
- Not needed for short sessions with no friction.

## Step 1: Scan the Conversation for Signals

- **Corrections** (strongest signal) — "no, not that", "don't do X", "stop doing Y".
- **Friction** — repeated attempts, workarounds, confusion.
- **New patterns** — approaches that worked and the user validated.
- **Outdated docs** — instructions contradicted by what actually happened.
- **Missing context** — information you needed but didn't have.

## Step 2: Categorize and Filter

| Destination | When | Where |
|---|---|---|
| Project instructions | Project-wide convention | `CLAUDE.md` (or your agent's project-instructions file) |
| Rule | Domain-specific pattern for this repo | project rules dir (e.g. `.claude/rules/`) |
| Skill | Reusable technique across ANY project | your skills dir (e.g. `.claude/skills/`) |
| Personal memory | Cross-project personal preference | your global memory store |

**Categorization test:** "Would this help someone on a completely different project?" → Yes = Skill, not memory/rule.

**STOP guard:** before writing a memory/rule for a reusable technique, check whether it belongs as a Skill instead.

**Two-pass rule** — only persist if: an explicit correction, it appeared in 2+ sessions, the user asked to remember it, or it fills a clear documentation gap. One-off corrections rarely warrant persistence.

## Step 3: Verify Before Presenting

**Anti-hallucination guard — the #1 failure mode.** Agents fabricate "already saved" claims.

- If you claim a file was created/updated, verify it exists (read it / list it) before claiming so.
- If you cannot verify, do NOT claim it was persisted.
- "I wrote X to Y" with no tool verification = hallucination.

## Step 4: Present Summary and Get Approval

```
### Project-Instruction Updates
- [file] — what changed and why

### New Rules
- [rule name] — what it enforces

### Suggested Skills
- [skill name] — what it teaches (cross-project patterns only)

### Pruning
- [file] — what's outdated and should be removed
```

Wait for user approval before applying.

## Step 5: Apply Changes

- Surgical edits to project instructions (append sections; don't rewrite).
- Write new rule files to the rules dir.
- For new skills, follow your skill-authoring process.
- Update memory files with structured content.

## Common Mistakes

- Persisting everything — keep only non-obvious lessons that prevent future friction.
- Rewriting instead of appending — changes to project instructions should be surgical.
- Filing cross-project patterns as memories instead of Skills.
- Claiming findings are saved without tool verification.
- Dropping the structured format under time pressure.
- Ignoring the two-pass rule — one-off corrections rarely warrant persistence.

**Pairs with:** business facts you learn belong in `bardak:less-is-more`'s `.claude/business-context.md`; durable decisions belong in a `bardak:adr`.
