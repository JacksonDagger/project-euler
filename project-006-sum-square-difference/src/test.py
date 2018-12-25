import unittest
import sumsquare


class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(2640, sumsquare.sumsquareddiff(10))



print(sumsquare.sumsquareddiff(100))

if __name__ == '__main__':
    unittest.main()