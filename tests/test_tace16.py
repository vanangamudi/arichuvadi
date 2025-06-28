import unittest
from arichuvadi.tace16 import TACE16String, TACE16_MAP, REVERSE_MAP

class TestTACE16String(unittest.TestCase):

    def test_encode_decode_basic(self):
        s = TACE16String("கா")
        self.assertEqual(s.encode(), TACE16_MAP['கா'])
        self.assertEqual(s.decode(), "கா")

    def test_round_trip(self):
        original = "காகி"
        s = TACE16String(original)
        reconstructed = TACE16String.from_internal(s.encode())
        self.assertEqual(str(reconstructed), original)

    def test_indexing(self):
        s = TACE16String("காகி")
        self.assertEqual(s[0], "கா")
        self.assertEqual(s[1], "கி")

    def test_slicing(self):
        s = TACE16String("காகிகு")
        sliced = s[1:]
        self.assertEqual(str(sliced), "கிகு")

    def test_len(self):
        s = TACE16String("காகிகு")
        self.assertEqual(len(s), 3)

    def test_mixed_language(self):
        s = TACE16String("கா hello கி")
        self.assertEqual(str(s), "கா hello கி")
        self.assertEqual(len(s), 3 + 6)  # 3 graphemes (2 Tamil, 1 Tamil) + 6 English chars

    def test_regex_search(self):
        import re
        s = TACE16String("காகி")
        self.assertIsNotNone(s.search(r'[\uE000-\uF8FF]{2}'))  # Match two TACE16 characters

    def test_replace(self):
        s = TACE16String("காகி")
        replaced = s.replace("கா", "கி")
        self.assertEqual(str(replaced), "கிகி")

    def test_from_internal_unknowns(self):
        # Unknown PUA character should fallback to raw
        unknown_pua = '\uF0FF'
        s = TACE16String.from_internal("hello" + unknown_pua + "!")
        self.assertEqual(str(s), "hello\uF0FF!")

if __name__ == '__main__':
    unittest.main()
