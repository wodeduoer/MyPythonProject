import unittest
from solver import Solver


class MyTestCase(unittest.TestCase):
    def test_negative_disc(self):
        s = Solver
        self.assertRaises(Exception)

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
