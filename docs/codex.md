# Using Bardak with Codex

Bardak's skills are Markdown workflows. Their instructions are portable; discovery,
invocation and installation depend on the host. Check the actual loaded path before
assuming an update took effect. Avoid maintaining both a copied and plugin-provided
version of the same skill unless that duplication is deliberate.

## Marketplace installation

On a Codex CLI exposing the `plugin marketplace` and `plugin add` commands:

```bash
codex plugin marketplace add bahadirkisbet/bardak
codex plugin add bardak@bardak
```

Check `codex plugin --help` and `codex plugin marketplace --help` for the installed
CLI's supported operations. The plugin selector is also available through `/plugins`.
Check the selected plugin's installation state, then start a fresh session and inspect
its skill paths. Command availability is not proof this package installed or activated.
Do not infer a minimum supported version from an untested older release.

## Project-local authoring or pinning

Current Codex documentation lists `.agents/skills/` for repository skills. Copy a
chosen revision's complete skill folders from `plugins/bardak/skills/` into that
location after checking for existing files. Preserve local changes and record the
source revision. Do not blindly copy over an existing installation on update.

Current Codex documentation also lists `~/.agents/skills/` for user skills. Older
installations may already expose copies elsewhere; inspect the current session's
skill catalog rather than deleting or migrating those copies automatically.

Codex can discover these skill directories without adding the full procedures to
`AGENTS.md`. Duplicating the procedure there creates a second version to maintain.
If a repository requires explicit routing, reference the installed skill path and
its actual purpose, not an obsolete checklist.

Invoke a locally discovered skill with its displayed name, for example
`$blind-review`. When plugin qualification differs, use the name shown by the host's
skill selector. Do not assume Claude's slash-command syntax is interchangeable.

## Shared behavior and knowledge

- Preserve higher-priority instructions, the user's scope and existing authorization.
- For independent review, use a fresh context with only the review task and required
  raw artifacts. In a Codex harness exposing `fork_turns`, use `"none"`; another harness
  may expose a different mechanism. A second pass with inherited history is not blind.
- Use the available tool capabilities. Missing delegation is a disclosed review
  limitation, not permission to call a self-review independent.
- Use the project's canonical knowledge source for both agents. Do not split business
  facts into `.claude/business-context.md` and `.codex/business-context.md`.
- Source edit, installed-copy update, skill discovery and behavior verification are
  separate states. Report which ones were checked.

## Verify a proposed update

Validate metadata and links, inspect the entire affected skills, and use
[the scenario matrix](skill-evaluation.md). Run a harmless representative task in a
fresh session before claiming runtime verification. Do not overwrite global skills,
install, publish or change hook configuration as a side effect of an audit.

References: [OpenAI skill discovery](https://learn.chatgpt.com/docs/build-skills),
[OpenAI skill design and testing](https://developers.openai.com/plugins/build/skills).
