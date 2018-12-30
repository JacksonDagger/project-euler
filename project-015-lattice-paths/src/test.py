import unittest
import lattice

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(1, lattice.lattice(0))

    def test_02(self):
        self.assertEqual(6, lattice.lattice(2))

    def test_03(self):
        self.assertEqual(20, lattice.lattice(3))

    def test_04(self):
        self.assertEqual(70, lattice.lattice(4))




print(lattice.lattice(20))


if __name__ == '__main__':
    unittest.main()