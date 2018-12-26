import pythagoreanTriplet
import unittest

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(60, pythagoreanTriplet.pyTrip(12))

    def test_02(self):
        self.assertEqual(-1, pythagoreanTriplet.pyTrip(11))

    def test_03(self):
        self.assertEqual(65520, pythagoreanTriplet.pyTrip(144))

print(pythagoreanTriplet.pyTrip(1000))

if __name__ == '__main__':
    unittest.main()