#!/usr/bin/env python3
"""Routing eval: does each bardak skill description fire when it should, stay
silent when it shouldn't, and not lose to a competing installed skill?

One `claude -p` classification call per query. The model sees the SAME name+description
table the real router sees (bardak skills read live from SKILL.md + real competitors),
and returns which skills should be consulted. We score bardak triggering only.

Usage: python route.py [--model M] [--workers N] [--out results.json]
"""
import json, re, subprocess, sys, os, argparse, concurrent.futures
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS_DIR = HERE.parent.parent / "skills"  # plugins/bardak/skills

# Real competing skills installed in this environment (trimmed descriptions).
COMPETITORS = {
    "superpowers:systematic-debugging": "Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes.",
    "superpowers:test-driven-development": "Use when implementing any feature or bugfix, before writing implementation code.",
    "superpowers:verification-before-completion": "Use when about to claim work is complete, fixed, or passing, before committing or creating PRs; requires running verification commands and confirming output.",
    "superpowers:requesting-code-review": "Use when completing tasks, implementing major features, or before merging to verify work meets requirements.",
    "superpowers:brainstorming": "Use before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.",
    "superpowers:writing-plans": "Use when you have a spec or requirements for a multi-step task, before touching code.",
    "superpowers:finishing-a-development-branch": "Use when implementation is complete, all tests pass, and you need to decide how to integrate the work (merge, PR, cleanup).",
    "ponytail:ponytail-review": "Code review focused exclusively on over-engineering: what to delete, reinvented stdlib, unneeded dependencies, speculative abstractions.",
    "ponytail:ponytail": "Forces the laziest solution that actually works: YAGNI, stdlib before custom, native before dependency, simplest minimal solution.",
}

def load_bardak():
    """Read name+description live from each SKILL.md frontmatter."""
    out = {}
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_md.read_text()
        m = re.search(r"^---\s*\n(.*?)\n---", text, re.S)
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M).group(1).strip()
        desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1).strip()
        out[f"bardak:{name}"] = desc
    return out

def build_table(bardak):
    rows = []
    for n, d in list(bardak.items()) + list(COMPETITORS.items()):
        rows.append(f"- {n}: {d}")
    return "\n".join(rows)

PROMPT = """You are the skill router for an AI coding assistant. Below is the list of available skills with the description that says when each should be used. Given the user's message, decide which skill(s) the assistant should consult.

Rules:
- Select a skill ONLY if its description genuinely matches the user's intent.
- Multiple skills may apply; select every one that genuinely fits.
- If none fit, return an empty array.
- Judge purely on the descriptions below, as the real router does.

AVAILABLE SKILLS:
{table}

USER MESSAGE:
{query}

Respond with ONLY a JSON array of the selected skill names, e.g. ["bardak:bugfix-tdd"] or []. No prose, no explanation."""

def run_one(model, table, item, runs=1):
    """Run a query `runs` times; a skill counts as selected if it appears in a
    majority of runs. Smooths out the model's run-to-run stochasticity."""
    q = item["query"]
    prompt = PROMPT.format(table=table, query=q)
    env = dict(os.environ); env.pop("CLAUDECODE", None)
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", model]
    def extract_result_text(raw):
        outer = json.loads(raw)
        if isinstance(outer, dict):
            return outer.get("result", "")
        # stream array: find the terminal result event
        txt = ""
        for ev in outer:
            if isinstance(ev, dict) and ev.get("type") == "result":
                txt = ev.get("result", "")
        return txt
    from collections import Counter
    votes = Counter(); errs = []
    for _ in range(runs):
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=180)
            txt = extract_result_text(p.stdout)
            m = re.search(r"\[[^\[\]]*\]", txt, re.S)   # the model's answer array
            sel = json.loads(m.group(0)) if m else []
            for s in sel:
                if isinstance(s, str): votes[s.strip()] += 1
        except Exception as e:
            errs.append(str(e)[:120])
    selected = [s for s, c in votes.items() if c > runs / 2]   # majority
    out = {**item, "selected": selected}
    if runs > 1: out["votes"] = dict(votes)
    if errs: out["error"] = errs
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--runs", type=int, default=1, help="runs per query, majority-voted")
    ap.add_argument("--out", default=str(HERE / "results.json"))
    ap.add_argument("--queries", default=str(HERE / "queries.json"))
    a = ap.parse_args()

    bardak = load_bardak()
    bardak_names = set(bardak)
    table = build_table(bardak)
    queries = json.loads(Path(a.queries).read_text())

    results = [None] * len(queries)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(run_one, a.model, table, q, a.runs): i for i, q in enumerate(queries)}
        done = 0
        for fut in concurrent.futures.as_completed(futs):
            i = futs[fut]; results[i] = fut.result(); done += 1
            print(f"  [{done}/{len(queries)}] done", file=sys.stderr)

    # Score
    per_skill = {}  # skill -> {recall_hit, recall_total, falsefire}
    for s in bardak_names:
        per_skill[s] = {"recall_hit": 0, "recall_total": 0, "false_fire": 0}
    none_falsefire = 0; none_total = 0
    steals = []  # expected bardak skill missed, what fired instead
    for r in results:
        exp = r["expected"]; sel = set(r["selected"])
        sel_bardak = sel & bardak_names
        if exp == "none":
            none_total += 1
            if sel_bardak:
                none_falsefire += 1
        else:
            per_skill[exp]["recall_total"] += 1
            if exp in sel:
                per_skill[exp]["recall_hit"] += 1
            else:
                steals.append({"query": r["query"][:70], "expected": exp,
                               "fired_instead": sorted(sel)})
        # false fire: any bardak skill selected that is NOT the expected one
        for s in sel_bardak:
            if s != exp:
                per_skill[s]["false_fire"] += 1

    summary = {"model": a.model, "n_queries": len(queries), "per_skill": per_skill,
               "none_total": none_total, "none_falsefire": none_falsefire,
               "steals": steals}
    Path(a.out).write_text(json.dumps({"summary": summary, "results": results}, indent=2))

    # Print human summary
    print("\n=== ROUTING EVAL SUMMARY ===")
    print(f"model={a.model}  queries={len(queries)}")
    print(f"{'skill':<32} recall   false-fire")
    for s in sorted(per_skill):
        d = per_skill[s]
        rec = f"{d['recall_hit']}/{d['recall_total']}"
        print(f"{s:<32} {rec:<8} {d['false_fire']}")
    print(f"{'(none-expected false fire)':<32} {none_falsefire}/{none_total}")
    if steals:
        print("\n--- MISSES (expected bardak skill did NOT fire) ---")
        for st in steals:
            print(f"  [{st['expected']}] {st['query']}")
            print(f"       fired instead: {st['fired_instead']}")

if __name__ == "__main__":
    main()
