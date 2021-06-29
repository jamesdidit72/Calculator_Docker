#import pytest
import unittest

import calc_functions as calc_functions

class Calc_test(unittest.TestCase):  # helps us test

    #calc_test = Function_Calc()

    def test_add(self):
        # this naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter can recognise it so it can run
        self.assertEqual(calc_functions.add(10, 5), 15)  # 10 + 5 = 15

    def test_subtract(self):
        self.assertEqual(calc_functions.subtract(5, 2), 3)  # 5 - 2 = 3

    def test_multiply(self):
        self.assertEqual(calc_functions.multiply(10, 10), 100)  # 10 * 10 = 100

    def test_divide(self):
        self.assertEqual(calc_functions.divide(15, 3), 5)  # 15 / 3 = 5

if __name__ == '__main__':
    unittest.main()
