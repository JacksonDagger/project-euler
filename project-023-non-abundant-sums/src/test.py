import unittest
import abundant

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual([12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56], abundant.generate_abundant_numbers(60))




if __name__ == '__main__':
    unittest.main()