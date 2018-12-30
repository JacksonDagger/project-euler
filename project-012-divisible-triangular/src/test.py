import triangular
import unittest

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(28, triangular.triangle_number(7))

    def test_02(self):
        self.assertEqual(21, triangular.triangle_number(6))

    def test_03(self):
        self.assertEqual(36, triangular.triangle_number(8))

    def test_04(self):
        self.assertEqual(0, triangular.triangle_number(0))

    def test_05(self):
        self.assertEqual(1, triangular.triangle_number(1))

    def test_06(self):
        self.assertEqual(28, triangular.triangle_divisors(5))

print(triangular.triangle_divisors(500))

if __name__ == '__main__':
    unittest.main()