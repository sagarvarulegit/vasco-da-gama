import pathlib
import subprocess
import unittest

class TestMasterVideoIntegrity(unittest.TestCase):
    def test_master_supercut_integrity(self):
        master_path = pathlib.Path("production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4")
        self.assertTrue(master_path.exists(), "Master video file must exist")
        self.assertGreater(master_path.stat().st_size, 300 * 1024 * 1024, "File size must be > 300 MB")

        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_name,channels,sample_rate", "-of", "json", str(master_path)]
        out = subprocess.check_output(cmd).decode()
        self.assertIn("aac", out)
        self.assertIn("48000", out)

if __name__ == "__main__":
    unittest.main()
