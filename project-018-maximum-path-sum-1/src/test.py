import unittest
import maxpath

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(23, maxpath.maxsum("test01.txt"))

    def test_02(self):
        self.assertEqual(10, maxpath.maxsum("test02.txt"))



if __name__ == '__main__':
    unittest.main()