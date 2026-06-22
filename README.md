# bardak

`bardak` is a [Claude Code](https://claude.com/claude-code) plugin: a small set of
skills for people who spend serious time in Claude Code. They encode the reflexes that
keep its output honest on real work — disciplined scrutiny, honest verification, and
structural restraint. Each skill is a short, opinionated procedure Claude follows when
the moment calls for it.

## The skills

| Skill | What it does |
|---|---|
| **blind-review** | Final quality gate. Dispatches independent reviewers who never see the implementer's account of the work — only the code and, at most, one intent artifact: nothing (cold audit), the spec (compliance), or the plan (drift). They find the gap between intent and what was built. |
| **retrospective** | At the end of a session, extracts the non-obvious lessons and persists them (project instructions / rules / skills / memory) so the same friction doesn't repeat. |
| **less-is-more** | For architecture decisions: extract the intent, lay out explicit paths *before* tradeoffs, weigh them against accumulated **business context** — and learn the business a little more on every use. |
| **more-is-less** | The disciplined counterweight to `less-is-more`: when a structural boundary — a schema, an integration/variant seam, a contract — has a *named* future need, invest in the seam now (a port, an extension point, a value type) so the next variant is additive, not a migration. Guards both failure modes: speculation is over-engineering; a hardcoded `if type == …` branch is under-engineering. |
| **no-silent-errors** | A reflex: every error, failure, and fault path stays visible. Strong types first (make illegal states unrepresentable), then loud runtime failures. No swallowed exceptions, no empty defaults for required data. |
| **verify-the-premise** | A behavior: never assume. Decide, suggest, and act on data — read the code, run it, trace the real path — not on what's expected to be true. |
| **pipeline-verification** | A change isn't verified by unit tests alone. Map the blast radius, verify end to end through the real user-visible pipeline, and report honestly what was and wasn't checked. |
| **bugfix-tdd** | No bug fix without a failing test that reproduces it first. Red, then fix, then green, then confirm no regressions. |
| **adr** | Capture a significant, hard-to-reverse decision as a short, immutable Architecture Decision Record — context, options, consequences — stored one-per-file in `docs/adr/`. Search existing ADRs before re-deciding. |

## Install

bardak is one marketplace, and the two big agentic CLIs read the same manifest — so the
install is the same two steps on each: add the marketplace, then install the plugin.

### Claude Code

```bash
claude plugin marketplace add bahadirkisbet/bardak
claude plugin install bardak
```

Or, from inside Claude Code:

```
/plugin marketplace add bahadirkisbet/bardak
/plugin install bardak@bardak
```

### Codex

Codex (CLI ≥ 0.139) reads the same marketplace:

```bash
codex plugin marketplace add bahadirkisbet/bardak
codex plugin add bardak@bardak
```

Or, from inside Codex: open `/plugins`, pick the **bardak** marketplace, install **bardak**,
then start a new thread. (This same install also covers the Codex desktop app — restart it
after installing and it picks up the plugin.)

Either way, skills activate on their own when the situation matches their description, or
you can invoke one directly (e.g. `/blind-review`, `/retrospective`, `/adr`).

For per-project pinning or wiring the skills into an `AGENTS.md` by hand, see
[docs/codex.md](docs/codex.md).

## A note on `less-is-more` and memory

`less-is-more` reads and appends to a project-local note at `.claude/business-context.md`.
Keep that file in your repo — it's how the skill compounds: every architecture decision
teaches it a little more about your domain, so its tradeoffs get more aligned with the
business over time. It's git-trackable on purpose, so a team shares the same context.

## License

MIT — see [LICENSE](LICENSE).
