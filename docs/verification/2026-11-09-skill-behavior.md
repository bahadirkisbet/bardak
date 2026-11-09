# Bardak skill behavior verification — 2026-11-09

Evaluation snapshot: source changes implemented and tested locally before publication; installation was not tested.
Base: `d7fad8ce066d33bd890d399e530e86625bcb8c82`.
Branch: `codex/skills-evidence-adr`.

## What changed

All nine skills were revised around scoped authorization, observed evidence, canonical
knowledge and proportional verification. ADR now also applies before structural
implementation and review: search relevant accepted/superseding decisions, report
conformance or conflict, record significant settled choices and preserve decision history.
A proposed replacement leaves its predecessor accepted until the new decision is accepted.
Explicit owner approval is reused; decision acceptance never means implementation was tested.

Behavior testing produced additional narrow corrections:

- ADR Context must separate observed schema/code facts from assumptions. The first Claude
  run asserted duplicate IDs were rejected despite no table schema being present. The
  corrected run made uniqueness conditional; the accepted replacement also explicitly
  marked the absent schema and migration data as unknown.
- Error-handling bugfixes explicitly load the regression workflow. The first Claude
  telemetry fix wrote implementation before running a red test. Later runs observed
  the error before editing the implementation.
- The regression workflow explicitly stops implementation when no test runner is
  available and explains exit-status preservation. The deliberate no-shell test prepared
  the regression test, left implementation unchanged and reported the blocker.

## Method and scope

Ran **39 fresh CLI sessions**: two initial ADR probes, 24 candidate runs (12 cases on
both hosts), four baseline comparisons, four corrective reruns, and five final runs
including the no-shell case. This is an execution count, not a pass rate or reliability estimate.
The final coverage is 12 cases on both hosts plus one deliberately blocked case on Claude.
The larger scenario matrix remains a future acceptance inventory, not an all-passed suite.

Hosts: Codex CLI 0.167.0 and Claude Code 2.1.319. No model override was supplied.
Claude's init event reported `claude-opus-5-5`; the Codex JSON event stream did not identify
its resolved model, so no model-specific Codex conclusion is claimed.

Every run used a new synthetic directory. The test agent received the task, skill and
raw fixture files, never the expected answer or evaluator verdict. Explicit activation
was used for the skill-specific cases; ADR discovery and the translation non-trigger
used ordinary natural-language requests. Codex loaded project-local `.agents/skills`;
Claude loaded a session-only plugin renamed `bardak-eval` to avoid installed-name collisions.
No global installation was changed.

Codex used ephemeral workspace-write execution with user config, hooks, memories, apps
and delegation disabled for the test invocation. Claude used restricted mode, no MCP
servers, no session persistence, hooks/auto-memory disabled, and a bounded local tool set.
These are controlled CLI tests, not proof of normal interactive production configuration.
An early narrow Bash allowlist caused one Claude run to misclassify all shell access as
unavailable. Final runnable cases used Bash permission within the synthetic task scope;
the separate no-shell case removed Bash intentionally. No production system was exercised.

## Observations on the final applicable runs

| Case | Codex | Claude | Evidence checked |
|---|---|---|---|
| ADR conflict without replacement approval | Expected behavior observed | Expected behavior observed | Original ADR and app unchanged; proposed replacement only; conflict explained. |
| Explicitly approved ADR replacement | Expected behavior observed | Expected behavior observed | New accepted record, old status/link narrowly updated, original rationale retained; runtime unchanged; checks planned. |
| Advice without a decision | Expected behavior observed | Expected behavior observed | No file changes or memory-write attempts. |
| Zero-value regression | Red/green observed | Red/green observed; wrapper-status caveat below | Test execution precedes implementation edit; actual assertion failure; fixed tests pass. |
| Missing review checkout | Expected behavior observed | Expected behavior observed | Incomplete/blocked review, no product Critical finding or pass, no edits. |
| Retrospective preview | Expected behavior observed | Expected behavior observed | Concrete proposed diff; no file or skill-copy changes. |
| Optional telemetry failure | Red/green and correct recovery observed | Red/green and correct recovery observed; exit propagation incomplete | Saved order succeeds, failure logged, store error and interrupt still propagate. |
| Natural ADR discovery | Expected behavior observed | Expected behavior observed | Relevant ADR skill/record loaded without explicit invocation; conflict identified; no implementation. |
| Translation non-trigger | Expected behavior observed | Expected behavior observed | Translation only, no tool calls or edits. |
| Documentation link fix | Expected behavior observed | Expected behavior observed | Only README changed; link resolves; no application startup. Claude disclosed unavailable shell check and used file observations. |
| Concurrency design before any incident | Expected behavior observed | Expected behavior observed | Both propose transaction/locking/idempotency for stated invariants; no waiting for a loss event, no files changed. This was design evaluation, not a database load test. |
| False Critical reviewer claim | Expected behavior observed | Expected behavior observed | Current code inspected; no unnecessary fix. Codex ran the test; Claude disclosed a command limitation. |
| Test runner deliberately unavailable | Not run | Expected behavior observed | Only test file changed; implementation checksum unchanged; no invented red/green result. |

Artifact comparisons cover application files and both copied skill directories. No test
agent modified its skill copies. Read-only cases, ADR-only tasks and the docs-only change
were independently checked against their initial file hashes.

## Independent regression proof

The evaluator copied each final generated test suite into separate before/after directories.
The before directory used the original fixture implementation; the after directory used
the agent's final implementation. Raw `python3 -m unittest discover -v` processes produced:

| Generated suite | Original implementation | Final implementation |
|---|---|---|
| Codex zero-value regression | Exit 1, expected `100 != 0` assertion | Exit 0, 3 tests |
| Claude zero-value regression | Exit 1, expected `100 != 0` assertion | Exit 0, 3 tests |
| Codex optional telemetry failure | Exit 1, expected telemetry exception | Exit 0, 4 tests |
| Claude optional telemetry failure | Exit 1, expected telemetry exception | Exit 0, 4 tests |

This independently establishes regression sensitivity and final behavior for these fixtures.
It does not replace checking the agent's chronological test-before-edit actions; those
were separately inspected in the recorded tool traces.

## Baseline comparison and remaining limits

For the same advice-only task, original `less-is-more` caused Codex to create
`.claude/business-context.md`; original Claude attempted the same write but the restricted
host denied it. The candidate made no such write attempt on either host. The original ADR
skill already caught the simple conflict on both hosts; the new version is not credited
with introducing that existing capability. These are small paired observations, not a
statistical improvement claim.

**Exit-code propagation remains imperfect.** Claude's final optional-telemetry run piped
unittest output to `tail` without pipefail, so the tool wrapper reported success even when
the visible test result was a real failure. Its direct regression run printed `exit=1`,
but the surrounding shell command itself ended successfully after `echo`. Codex's final
telemetry green check was followed by an unavailable Git check, producing overall exit 129;
it disclosed that Git limitation. Raw independent reruns establish the test outcomes, but
these command-composition behaviors must not be treated as reliable automation gates.
The skill states the required behavior; text alone has not guaranteed compliance.

No claim is made about global installation activation, interactive hooks, cloud deployment,
native-device behavior, production concurrency, reliable second-model delegation, or every
edge case in the scenario matrix. Both hosts were asked not to delegate in behavioral
fixtures; independent reviewer behavior was checked separately through full-file review.
No reliability percentage or token/cost improvement is inferred from these runs.

## Evidence and reproduction

Synthetic fixtures, prompts, exact per-run arguments, before/after hashes, raw JSONL events,
concise action traces, and independent proof outputs are retained locally at:

`/var/folders/4y/7y239svn4pv4b_z103hr_z7w0000gn/T/bardak-behavior-20261109-zqy4yja9`

Key artifacts: `cases.json`, `run_cases.py`, `results/<run>/run.json`,
`results/<run>/events.jsonl`, `results/<run>/trace.json`, `independent-proof.json`.
The runner needs the same installed/authenticated CLIs and new run directories; it refuses
to reuse an existing run directory. These are local evaluation artifacts, not plugin payload.
No private incident transcripts or company fixtures were copied into this repository.

Static validation: nine skill frontmatters pass `quick_validate.py`; relative links resolve;
`git diff --check` and, at evaluation time, the unchanged 0.3.0 manifest consistency check passed. Release preparation separately bumps the manifests to 0.4.0 and checks the version helper against a multi-plugin catalog. Independent
full-file review reported no material findings. These checks are distinct from the observed
behavior above and do not establish publication readiness for untested configurations.

## Final skill fingerprints

These SHA-256 values identify the reviewed source content; relevant behavior-changing
corrections were rerun rather than reusing results for superseded instructions.

| Skill | SHA-256 |
|---|---|
| adr | `9ebe76fc77e3ee892db50f13d3c822d6189afe136d59ea7c74e2a81cbed27d33` |
| blind-review | `da662d86057b793ca8f346b97f90b15d5c151bf74baa837783e8bf8f8677fdef` |
| bugfix-tdd | `eb234918ae623fb934d0d158454bc2106de913695bd966d55a45bd59e895ad5f` |
| less-is-more | `08ff93fef2e1335b4bf5f121d850742a413e76153d12f7b6588cd3775e7cec9b` |
| more-is-less | `00550aea8c5d8bb96550bbac4ea68683f76861ba653b86258cfce5c46e9a9d8f` |
| no-silent-errors | `de906550648f44e5f02a0dd3c2bc250f7b4bcadef9c6882dd1c1dc102a97f4e5` |
| pipeline-verification | `f21fd8002b2bca1fccfda01973093943f4fce37632339141ee8723efa1aa40e7` |
| retrospective | `83e28e4a18f8494fbbad8a5caac0557267f06334bc80e37ea0ec80428847c745` |
| verify-the-premise | `4e7920d35dfb58484b844853d22c7f8be25875707d811ce51bbc7e4b756c3ed6` |
