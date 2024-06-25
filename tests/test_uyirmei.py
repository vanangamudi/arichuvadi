import unittest
from arichuvadi import uyirmei

class TestSplitUyirmei(unittest.TestCase):
    def test_split_uyirmei(self):
        self.assertEqual('உய்அர் த்அன்இச் ச்எம் ம்ஒழ்இ',
                        uyirmei.split_uyirmei(
                            'உயர் தனிச் செம் மொழி'))

    def test_split_uyirmei2(self):
        self.assertEqual('உய்அர் த்அன்இச் ச்எம் ம்ஒழி',
                        uyirmei.split_uyirmei2(
                            'உயர் தனிச் செம் மொழி'))

    def test_merge_uyirmei(self):
        #import pdb; pdb.set_trace()
        self.assertEqual('உயர் தனிச் செம் மொழி',
                         uyirmei.merge_uyirmei(
                             list(uyirmei.split_uyirmei(
                                 'உயர் தனிச் செம் மொழி',
                                 join_p=False))))

if __name__ == '__main__':
    unittest.main()
