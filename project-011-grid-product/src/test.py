import NotAGridException
import grid
import unittest

class Test(unittest.TestCase):
    def test_01(self):
        tester = grid.grid("test01.txt")
        self.assertEqual(36, tester.get_product(2))

    def test_02(self):
        tester = grid.grid("test02.txt")
        self.assertEqual(405, tester.get_product(3))

    def test_03(self):
        tester = grid.grid("test03.txt")
        self.assertEqual(9, tester.get_product(1))

challenge = grid.grid("challenge.txt")
print(challenge.get_product(4))


if __name__ == '__main__':
    unittest.main()