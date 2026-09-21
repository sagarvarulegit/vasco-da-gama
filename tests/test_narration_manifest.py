import json
import pathlib
import unittest

class TestNarrationManifest(unittest.TestCase):
    def test_manifest_structure_and_completeness(self):
        manifest_path = pathlib.Path("production/audio/narration_manifest.json")
        self.assertTrue(manifest_path.exists(), "Manifest file must exist")
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data), 64, f"Expected 64 scenes, found {len(data)}")
        for item in data:
            self.assertIn("scene_id", item)
            self.assertIn("text", item)
            self.assertTrue(len(item["text"]) > 10, f"Text too short in {item.get('scene_id')}")
            self.assertGreaterEqual(item["word_count"], 3, f"Line too short in {item['scene_id']}")
            self.assertLessEqual(item["word_count"], 45, f"Line too long for 10s window in {item['scene_id']}")

if __name__ == "__main__":
    unittest.main()
