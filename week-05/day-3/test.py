import unittest
from divide_ten import divide_ten
from number_of_lines import number_of_lines

class TestDivideTen(unittest.TestCase):

    def test_divide_by_one(self):
        self.assertEqual(divide_ten(1), 10)

    def test_divide_by_five(self):
        self.assertEqual(divide_ten(5), 2)

    def test_divide_by_minus_one(self):
        self.assertEqual(divide_ten(-1), -10)

    def test_divide_by_zero(self):
        self.assertEqual(divide_ten(0), 'fail')

    def test_read_number_of_lines(self):
        self.assertEqual(number_of_lines('test.txt'), 3)

    def test_read_file_not_exist(self):
        self.assertEqual(number_of_lines('not_test.txt'), 0)

if __name__ == '__main__':
    unittest.main()
