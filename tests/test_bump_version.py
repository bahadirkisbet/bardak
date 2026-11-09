import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


class BumpVersionTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory(prefix="bardak-version-test-")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.script = self.root / "scripts/bump-version.sh"
        self.plugin = self.root / "plugins/bardak/.claude-plugin/plugin.json"
        self.market = self.root / ".claude-plugin/marketplace.json"
        for path in [self.script, self.plugin, self.market]:
            path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO / "scripts/bump-version.sh", self.script)
        self.foreign = {"name": "other-plugin", "version": "0.1.2", "source": {"sha": "unchanged-pin"}}
        self.plugin.write_text(json.dumps({"name": "bardak", "version": "0.3.0"}, indent=2) + "\n")
        self.market.write_text(json.dumps({"metadata": {"version": "0.3.0"}, "plugins": [
            {"name": "bardak", "version": "0.3.0"}, self.foreign]}, indent=2) + "\n")

    def run_script(self, *args):
        return subprocess.run(["bash", str(self.script), *args], capture_output=True, text=True)

    def test_check_ignores_other_plugin_versions(self):
        result = self.run_script("--check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_bump_preserves_other_plugin_and_pin(self):
        result = self.run_script("0.4.0")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        plugin = json.loads(self.plugin.read_text())
        market = json.loads(self.market.read_text())
        self.assertEqual(plugin["version"], "0.4.0")
        self.assertEqual(market["metadata"]["version"], "0.4.0")
        self.assertEqual(market["plugins"][0]["version"], "0.4.0")
        self.assertEqual(market["plugins"][1], self.foreign)
        self.assertEqual(self.run_script("--check").returncode, 0)

    def test_check_detects_bardak_drift(self):
        self.plugin.write_text(json.dumps({"name": "bardak", "version": "0.2.0"}, indent=2))
        self.assertNotEqual(self.run_script("--check").returncode, 0)

    def test_invalid_version_does_not_modify_files(self):
        before = [self.plugin.read_bytes(), self.market.read_bytes()]
        self.assertNotEqual(self.run_script("not-a-version").returncode, 0)
        self.assertEqual([self.plugin.read_bytes(), self.market.read_bytes()], before)


if __name__ == "__main__":
    unittest.main()
