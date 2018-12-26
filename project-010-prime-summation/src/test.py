import summation
import unittest

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(17, summation.getprimesumbelow(10))

    def test_02(self):
        self.assertEqual(28, summation.getprimesumbelow(12))

    def test_03(self):
        self.assertEqual(41, summation.getprimesumbelow(14))


print(summation.getprimesumbelow(2000000))


if __name__ == '__main__':
    #unittest.main()