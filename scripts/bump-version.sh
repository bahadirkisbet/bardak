#!/usr/bin/env bash
# Bump/check Bardak's plugin, catalog entry and marketplace metadata together.
# Other plugins in the marketplace keep their own independent versions and pins.
set -euo pipefail

exec python3 - "$(cd "$(dirname "$0")/.." && pwd)" "$@" <<'PYTHON'
import json
from pathlib import Path
import re
import sys

if len(sys.argv) != 3 or (sys.argv[2] != "--check" and not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", sys.argv[2])):
    sys.exit("usage: bump-version.sh X.Y.Z | --check")

root, action = Path(sys.argv[1]), sys.argv[2]
plugin_path = root / "plugins/bardak/.claude-plugin/plugin.json"
market_path = root / ".claude-plugin/marketplace.json"
try:
    plugin = json.loads(plugin_path.read_text())
    market = json.loads(market_path.read_text())
    entries = [entry for entry in market["plugins"] if entry["name"] == "bardak"]
    if plugin["name"] != "bardak" or len(entries) != 1:
        raise ValueError("expected exactly one Bardak plugin and catalog entry")
    entry = entries[0]
    versions = {plugin["version"], market["metadata"]["version"], entry["version"]}
    if action == "--check":
        if len(versions) != 1:
            sys.exit("Bardak version drift: " + ", ".join(sorted(versions)))
        print("version OK: " + plugin["version"])
    else:
        plugin["version"] = market["metadata"]["version"] = entry["version"] = action
        plugin_path.write_text(json.dumps(plugin, indent=2) + "\n")
        market_path.write_text(json.dumps(market, indent=2) + "\n")
        print("bumped Bardak to " + action + "; other plugin versions unchanged")
        print("next: release notes, dev -> main merge, and tag v" + action + " (see RELEASE.md)")
except (OSError, ValueError, KeyError, TypeError) as error:
    sys.exit("version update failed: " + str(error))
PYTHON
