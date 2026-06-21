# Releasing bardak

Users install by tracking `main` (the default branch); `claude plugin marketplace update`
re-pulls whatever is on it. So **`main` = published/stable**. Develop on `dev`, release by
merging `dev` → `main` and tagging.

## Branches

- **`main`** — stable, what installers get. Only release-ready commits land here.
- **`dev`** — integration. Do work here, or in feature branches → PR → `dev`.

Keep `main` as the GitHub default branch so the marketplace tracks stable.

## Cut a release

1. On `dev`, finish and verify changes (`scripts/bump-version.sh --check`; JSON valid; skills load).
2. Bump the version (kept in lockstep across both manifests):
   ```bash
   scripts/bump-version.sh 0.2.0
   scripts/bump-version.sh --check
   ```
3. Add a `## v0.2.0 (YYYY-MM-DD)` entry to `RELEASE-NOTES.md`.
4. Commit on `dev`, then merge to `main` (merge, not squash):
   ```bash
   git checkout main && git merge --no-ff dev
   ```
5. Tag and push:
   ```bash
   git tag -a v0.2.0 -m "v0.2.0" && git push origin main --tags
   ```
6. Publish the GitHub release:
   ```bash
   gh release create v0.2.0 --notes-from-tag
   ```
7. Tell users: `claude plugin marketplace update bardak`.

## Versioning (SemVer, 0.x while shaping)

- **minor** (`0.X.0`) — a new skill, or a notable behavior change.
- **patch** (`0.0.X`) — wording, fixes, small clarifications.

## Notes

- Push goes to the personal account: remote `git@personal:bahadirkisbet/bardak.git`.
- `gh` release commands need the `bahadirkisbet` account active
  (`gh auth switch -u bahadirkisbet`, then switch back).
