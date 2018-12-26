import unittest
import orderedPrime


class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(2, orderedPrime.getnthprime(1))

    def test_02(self):
        self.assertEqual(7, orderedPrime.getnthprime(4))

    def test_03(self):
        self.assertEqual(31, orderedPrime.getnthprime(11))

    def test_04(self):
        self.assertEqual(73, orderedPrime.getnthprime(21))



print(orderedPrime.getnthprime(10001))

if __name__ == '__main__':
    unittest.main()