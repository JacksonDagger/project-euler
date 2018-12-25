import unittest
import main

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual([2,3], main.prime_factorize(6))
    def test_02(self):
        self.assertEqual([2,2], main.prime_factorize(4))

    def test_03(self):
        self.assertEqual([3], main.prime_factorize(3))

    def test_04(self):
        self.assertEqual([2, 2, 7], main.prime_factorize(28))

    def test_05(self):
        self.assertEqual([], main.prime_factorize(1))

    def test_06(self):
        self.assertEqual(2520, main.smallest_multiple(10))



print(main.smallest_multiple(20))

if __name__ == '__main__':
    unittest.main()

