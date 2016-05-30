import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_add_5_and_6_is_5(self):
        self.assertEqual(extend.add(5, 6), 11)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)

    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(3, 5, 4), 5)

    def test_max_of_three_second_another_sort(self):
        self.assertEqual(extend.max_of_three(4, 5, 3), 5)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)

    def test_median_ten(self):
        self.assertEqual(extend.median([1,4,2,4,2,3,5,3,1,1]), 2.5)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_is_vovel_á(self):
        self.assertTrue(extend.is_vovel('á'))

    def test_is_vovel_1(self):
        self.assertFalse(extend.is_vovel('1'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_1234(self):
        self.assertEqual(extend.translate(1234), '1234')

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('alma'), 'avalmava')

if __name__ == '__main__':
    unittest.main()
