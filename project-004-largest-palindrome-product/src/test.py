import unittest
import palindrome


class TestPalindrome(unittest.TestCase):
    def test_01(self):
        self.assertFalse(is_palindrome(102))



if __name__ == '__main__':
    unittest.main()
