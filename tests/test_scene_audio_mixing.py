import pathlib
import subprocess
import unittest

class TestSceneAudioMixing(unittest.TestCase):
    def test_ducked_scene_audio(self):
        clip_path = pathlib.Path("production/exports/supercut_cache/001_ACT_I_S01.mp4")
        self.assertTrue(clip_path.exists(), "Target clip must exist in cache")

        cmd = ["ffprobe", "-v", "error", "-show_entries", "stream=channels,sample_rate,codec_name", "-of", "csv=p=0", str(clip_path)]
        out = subprocess.check_output(cmd).decode().strip()
        self.assertIn("aac", out)
        self.assertIn("48000", out)

if __name__ == "__main__":
    unittest.main()
