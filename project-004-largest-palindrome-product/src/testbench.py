import unittest
import palindrome


class TestPalindrome(unittest.TestCase):
    def test_01(self):
        self.assertFalse(palindrome.is_palindrome(102))

    def test_02(self):
        self.assertFalse(palindrome.is_palindrome(223312))

    def test_03(self):
        self.assertFalse(palindrome.is_palindrome(91018))

    def test_04(self):
        self.assertFalse(palindrome.is_palindrome(45))

    def test_05(self):
        self.assertFalse(palindrome.is_palindrome(0660))

    def test_06(self):
        self.assertTrue(palindrome.is_palindrome(0))

    def test_07(self):
        self.assertTrue(palindrome.is_palindrome(1))

    def test_08(self):
        self.assertTrue(palindrome.is_palindrome(12321))

    def test_09(self):
        self.assertTrue(palindrome.is_palindrome(-4994))

    def test_10(self):
        self.assertEqual(9009, palindrome.palindrome_factor(2, 2))

    print(palindrome.palindrome_factor(3, 3))



if __name__ == '__main__':
    unittest.main()
