# Using bardak skills with Codex

bardak ships as a Claude Code plugin, but the skills themselves are plain
`SKILL.md` files — Codex can use them too. Codex has no plugin marketplace;
it reads skills from a project-local `.codex/skills/` directory that you
reference from your `AGENTS.md`.

## Install (per project)

From the root of the repo where you want the skills:

```bash
# 1. clone bardak somewhere
git clone https://github.com/bahadirkisbet/bardak ~/.bardak

# 2. copy the skills into this project's .codex/skills/
mkdir -p .codex/skills
cp -R ~/.bardak/plugins/bardak/skills/* .codex/skills/
```

To update later: `git -C ~/.bardak pull` then re-run the copy.

## Wire them into AGENTS.md

Codex uses the skills you point it at. Add a section to your `AGENTS.md` so the
agent knows they exist and when to read them:

```markdown
## Skills

Read the relevant skill before the matching task:

- `.codex/skills/blind-review/SKILL.md` — final spec-only review gate
- `.codex/skills/retrospective/SKILL.md` — end-of-session lesson capture
- `.codex/skills/less-is-more/SKILL.md` — architecture paths + business-context memory
- `.codex/skills/no-silent-errors/SKILL.md` — strong types, no swallowed errors (apply always)
- `.codex/skills/verify-the-premise/SKILL.md` — never assume; act on data (apply always)
- `.codex/skills/pipeline-verification/SKILL.md` — verify end to end, map blast radius
- `.codex/skills/bugfix-tdd/SKILL.md` — failing test first, then fix
- `.codex/skills/adr/SKILL.md` — record significant decisions
```

## Notes

- The `SKILL.md` files are platform-neutral — no Claude-only tool names — so they
  read the same under Codex. The one Claude-specific touch is **blind-review**'s
  "second reviewer via MCP"; under Codex, run the second reviewer as a second
  Codex pass, or skip it and note so.
- `less-is-more` writes to `.claude/business-context.md` by default. Under Codex,
  either keep that path or point it at `.codex/business-context.md` — just be
  consistent so the memory accumulates in one place.
- Keep `.codex/skills/` in version control so your team shares the same skills.
```
