# bardak

Bardak is a small set of skills for Claude Code and Codex: independent review,
honest evidence, useful error handling and restrained architecture decisions.
Each skill handles a particular decision; ordinary tasks should not activate the
entire collection.

## Skills

| Skill | Use it for |
|---|---|
| **blind-review** | Independent review of a specific change and its requirements, with verified findings and explicit coverage. |
| **verify-the-premise** | Checking a material claim before it justifies an action; distinguishing observation, inference and missing evidence. |
| **bugfix-tdd** | Behavioral regression proof: observed failure on buggy code, minimal fix, observed pass and relevant surrounding checks. |
| **pipeline-verification** | Evidence at the changed boundary, with the actual running target, side effects, cleanup and unverified stages accounted for. |
| **no-silent-errors** | Keeping failure distinct from legitimate absence, with explicit recovery and safe error visibility. |
| **less-is-more** | Comparing viable designs against the user's goal, current system and business constraints. |
| **more-is-less** | A small seam justified by a named consumer or evolution cost, preserving required correctness protections. |
| **adr** | Reading relevant decisions before structural work, checking conformance and recording significant decisions or explicit supersession. |
| **retrospective** | Turning demonstrated friction into a concrete, scoped improvement proposal. |

## Scope and completion

Skills do not expand the user's authorization or replace repository policy. A review
can remain read-only; a preview stops before application; verification does not imply
deployment. Reuse evidence already gathered for the same unchanged target. Load a
related skill only when its workflow is needed, not merely because it is linked.

Use the project's designated knowledge source. A consultation with no new confirmed
knowledge requires no memory write. Keep company and personal context separate.

## Install and invoke

### Claude Code

```bash
claude plugin marketplace add bahadirkisbet/bardak
claude plugin install bardak@bardak
```

From Claude Code, the corresponding commands are `/plugin marketplace add
bahadirkisbet/bardak` and `/plugin install bardak@bardak`. Invoke plugin skills with
their namespace, for example `/bardak:blind-review` or `/bardak:retrospective`.
Unqualified commands may select a different local skill.

### Codex

On a CLI exposing these plugin commands:

```bash
codex plugin marketplace add bahadirkisbet/bardak
codex plugin add bardak@bardak
```

Use `/plugins` or the installed CLI's help to inspect support and installation.
For local discovery, pinning and invocation differences, see [Codex usage](docs/codex.md).

Both hosts can select skills from their descriptions. Inspect the active skill path
and start a fresh session when checking an update. A changed source checkout does not
prove copied skills or a versioned plugin cache were updated. Do not edit cache files
as the canonical source or remove another installation without examining its purpose.

## Validate changes

Keep the version manifests consistent with `scripts/bump-version.sh --check`.
Check frontmatter, links and representative behavior using
[the scenario matrix](docs/skill-evaluation.md). Metadata checks do not prove that
instructions activate or lead to the right actions in either host.

Publishing is a separate action: see [RELEASE.md](RELEASE.md).

References: [Claude Code skills](https://code.claude.com/docs/en/skills),
[OpenAI skill design](https://developers.openai.com/plugins/build/skills).

## License

MIT — see [LICENSE](LICENSE).
