import unittest
import collatz

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(2, collatz.collatz_length(2))

    def test_02(self):
        self.assertEqual(1, collatz.collatz_length(1))

    def test_03(self):
        self.assertEqual(4, collatz.collatz_length(8))

    def test_04(self):
        self.assertEqual(8, collatz.collatz_length(3))

    def test_05(self):
        self.assertEqual(3, collatz.collatz_length(4))

    def test_06(self):
        self.assertEqual(3, collatz.largest_collatz(5))

print(collatz.largest_collatz(1000000))

if __name__ == '__main__':
    unittest.main()