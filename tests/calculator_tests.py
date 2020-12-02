import unittest

from modules.calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):
    #def setUp(self):



    def test_add(self):
        self.assertEqual(8, add(2, 6))


    def test_subtract(self):
        self.assertEqual(3, subtract(15, 12))

    def test_multiply(self):
        self.assertEqual(15, (multiply(5, 3)))

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))