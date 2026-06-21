#!/usr/bin/env bash
# Bump (or check) the bardak version, kept in lockstep across both manifests.
#   bump-version.sh X.Y.Z   -> set version in plugin.json + marketplace.json
#   bump-version.sh --check -> verify all version strings match (exit 1 on drift)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN="$ROOT/plugins/bardak/.claude-plugin/plugin.json"
MARKET="$ROOT/.claude-plugin/marketplace.json"
SEMVER='[0-9]+\.[0-9]+\.[0-9]+'

versions() {
  grep -hoE "\"version\": \"$SEMVER\"" "$PLUGIN" "$MARKET" | grep -oE "$SEMVER" | sort -u
}

if [[ "${1:-}" == "--check" ]]; then
  n=$(versions | wc -l | tr -d ' ')
  if [[ "$n" != "1" ]]; then
    echo "version drift across manifests:"; versions; exit 1
  fi
  echo "version OK: $(versions)"; exit 0
fi

NEW="${1:-}"
if [[ ! "$NEW" =~ ^$SEMVER$ ]]; then
  echo "usage: bump-version.sh X.Y.Z | --check" >&2; exit 1
fi
OLD=$(versions | head -1)
perl -0pi -e "s/\"version\":\s*\"$SEMVER\"/\"version\": \"$NEW\"/g" "$PLUGIN" "$MARKET"
echo "bumped ${OLD:-?} -> $NEW in plugin.json + marketplace.json"
echo "next: add a RELEASE-NOTES.md entry, merge dev -> main, tag v$NEW (see RELEASE.md)"
