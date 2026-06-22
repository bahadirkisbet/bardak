# Using bardak with Codex

bardak ships as a marketplace plugin, and Codex (CLI ≥ 0.139) reads the same
`marketplace.json` manifest that Claude Code does — so the recommended install
is the marketplace, identical to Claude Code. The older per-project copy is kept
below as a fallback for pinning, offline use, or older Codex.

## Install (marketplace — recommended)

```bash
codex plugin marketplace add bahadirkisbet/bardak
codex plugin add bardak@bardak
```

Or, from inside Codex: open `/plugins`, pick the **bardak** marketplace, install
**bardak**, then start a new thread. The Codex desktop app uses the same install —
restart it afterward and it picks up the plugin.

Skills then activate on their own when the situation matches, or you invoke one
directly (`/blind-review`, `/adr`, …) — no `AGENTS.md` wiring needed.

To update later: `codex plugin marketplace upgrade` then `codex plugin add bardak@bardak`.

## Install (per-project vendoring — fallback)

Use this when you want the skills pinned in the repo (offline, air-gapped, or a
Codex too old for the marketplace). The `SKILL.md` files are plain Markdown, so a
copy works:

```bash
# 1. clone bardak somewhere
git clone https://github.com/bahadirkisbet/bardak ~/.bardak

# 2. copy the skills into this project's .codex/skills/
mkdir -p .codex/skills
cp -R ~/.bardak/plugins/bardak/skills/* .codex/skills/
```

To update later: `git -C ~/.bardak pull` then re-run the copy.

### Wire them into AGENTS.md

A vendored copy isn't auto-discovered — point Codex at it from your `AGENTS.md`:

```markdown
## Skills

Read the relevant skill before the matching task:

- `.codex/skills/blind-review/SKILL.md` — final spec-only review gate
- `.codex/skills/retrospective/SKILL.md` — end-of-session lesson capture
- `.codex/skills/less-is-more/SKILL.md` — architecture paths + business-context memory
- `.codex/skills/more-is-less/SKILL.md` — invest in a boundary now when a future need is named
- `.codex/skills/no-silent-errors/SKILL.md` — strong types, no swallowed errors (apply always)
- `.codex/skills/verify-the-premise/SKILL.md` — never assume; act on data (apply always)
- `.codex/skills/pipeline-verification/SKILL.md` — verify end to end, map blast radius
- `.codex/skills/bugfix-tdd/SKILL.md` — failing test first, then fix
- `.codex/skills/adr/SKILL.md` — record significant decisions
```

Keep `.codex/skills/` in version control so your team shares the same skills.

## Notes

- The `SKILL.md` files are platform-neutral — no Claude-only tool names — so they
  read the same under Codex. The one Claude-specific touch is **blind-review**'s
  "second reviewer via MCP"; under Codex, run the second reviewer as a second
  Codex pass, or skip it and note so.
- `less-is-more` writes to `.claude/business-context.md` by default. Under Codex,
  either keep that path or point it at `.codex/business-context.md` — just be
  consistent so the memory accumulates in one place.
