import pathlib
import subprocess
import unittest

class TestVoiceoverGeneration(unittest.TestCase):
    def test_proof_of_concept_voiceover(self):
        s01_vo = pathlib.Path("production/audio/voiceover/ACT_I_S01_vo.mp3")
        self.assertTrue(s01_vo.exists(), "Act I Scene 1 voiceover must exist")
        self.assertGreater(s01_vo.stat().st_size, 5000, "Audio file should have valid size")

        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(s01_vo)]
        dur = float(subprocess.check_output(cmd).decode().strip())
        self.assertTrue(2.0 <= dur <= 8.5, f"VO duration {dur}s outside expected 2-8.5s window")

if __name__ == "__main__":
    unittest.main()
