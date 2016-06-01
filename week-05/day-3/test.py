import unittest
from divide_ten import divide_ten

class TestDivideTen(unittest.TestCase):

    def test_divide_by_one(self):
        self.assertEqual(divide_ten(1), 10)

    def test_divide_by_five(self):
        self.assertEqual(divide_ten(5), 2)

    def test_divide_by_minus_one(self):
        self.assertEqual(divide_ten(-1), -10)

    def test_divide_by_zero(self):
        self.assertEqual(divide_ten(0), 'fail')

if __name__ == '__main__':
    unittest.main()
