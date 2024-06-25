import unittest


import arichuvadi
from arichuvadi import uyirmei


class TestArichuvadi(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.saram = 'The Great உயர்தனிச்செம்மொழி தமிழ்!!!'
        self.expected_repr = "['T', 'h', 'e', ' ', 'G', 'r', 'e', 'a', 't', ' ', 'உ', 'ய', 'ர்', 'த', 'னி', 'ச்', 'செ', 'ம்', 'மொ', 'ழி', ' ', 'த', 'மி', 'ழ்', '!', '!', '!']"

    def test_get_letters_coding(self):
        #print(arichuvadi.get_letters_coding(self.saram))
        self.assertEqual(arichuvadi.get_letters_coding(self.saram),
                         ['T','h','e',' ','G','r','e','a','t',' ',\
                          'உ','ய','ர்','த','னி','ச்','செ','ம்','மொ','ழி',\
                          ' ','த','மி','ழ்','!','!','!'])

    def test_get_letters_glyph(self):
        #print(arichuvadi.get_letters_glyph(self.saram))
        self.assertEqual(arichuvadi.get_letters_glyph(self.saram),
                         ['T','h','e',' ','G','r','e','a','t',' ',\
                          'உ','ய','ர்','த','னி','ச்','செ','ம்','மொ','ழி',\
                          ' ','த','மி','ழ்','!','!','!'])

    def test_TamilStr_str(self):
        self.assertEqual(self.saram,
                        str(arichuvadi.TamilStr(self.saram)))

    def test_TamilStr_repr(self):
        repr_ = repr(arichuvadi.TamilStr(self.saram))
        assert len(repr_) == len(self.expected_repr), f'{len(repr_)} == {len(self.expected_repr)}'
        assert repr(arichuvadi.TamilStr(self.saram)) == self.expected_repr

if __name__ == '__main__':
    unittest.main()
