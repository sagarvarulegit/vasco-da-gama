import pathlib
import subprocess
import unittest

class TestMusicSuites(unittest.TestCase):
    def test_music_suites_exist_and_valid(self):
        suites = [
            "SUITE_1_LISBON_ATLANTIC.mp3",
            "SUITE_2_CAPE_STORMS.mp3",
            "SUITE_3_SWAHILI_COAST.mp3",
            "SUITE_4_MONSOON_CALICUT.mp3",
            "SUITE_5_CALICUT_AMBUSH.mp3",
            "MAP_BRIDGE.mp3",
        ]
        for s in suites:
            p = pathlib.Path(f"production/audio/music/{s}")
            self.assertTrue(p.exists(), f"Suite {s} must exist")
            self.assertGreater(p.stat().st_size, 15000, f"Suite {s} too small")

            cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=sample_rate", "-of", "json", str(p)]
            out = subprocess.check_output(cmd).decode()
            self.assertTrue("48000" in out or "44100" in out, f"Sample rate invalid in {s}")

if __name__ == "__main__":
    unittest.main()
