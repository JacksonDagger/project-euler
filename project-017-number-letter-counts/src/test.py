import unittest
import numberletter

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, numberletter.numletter(1))

    def test_02(self):
        self.assertEqual(6, numberletter.numletter(20))

    def test_03(self):
        self.assertEqual(10, numberletter.numletter(63))

    def test_04(self):
        self.assertEqual(10, numberletter.numletter(200))

    def test_05(self):
        self.assertEqual(18, numberletter.numletter(306))

    def test_06(self):
        self.assertEqual(25, numberletter.numletter(678))

    def test_07(self):
        self.assertEqual(20, numberletter.numletter(115))

    def test_08(self):
        self.assertEqual(23, numberletter.numletter(342))

    def test_09(self):
        self.assertEqual(11, numberletter.numletter(1000))

    def test_10(self):
        self.assertEqual(19, numberletter.nlsum(1, 5))


print(numberletter.nlsum(1, 1000))


if __name__ == '__main__':
    unittest.main()