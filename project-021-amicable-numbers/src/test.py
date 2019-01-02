import unittest
import amicable

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(284, amicable.dfunc(220))

    def test_02(self):
        self.assertEqual(220, amicable.dfunc(284))



print amicable.amicable_sum(10000)

if __name__ == '__main__':
    unittest.main()