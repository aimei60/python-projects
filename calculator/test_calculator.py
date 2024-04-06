import unittest
from calculator_file import addition, subtraction, division, multiplication, calculator

class TestCalculator(unittest.TestCase):
    
    def test_addiition(self):
        result = addition(2, 4)
        self.assertEqual(result, 6)
    
    def test_subtraction(self):
        result = subtraction(5, 4)
        self.assertEqual(result, 1)
    
    def test_multiplication(self):
        result = multiplication(2, 5)
        self.assertEqual(result, 10)
    
    def test_division(self):
        result = division(10, 5)
        self.assertEqual(result, 2)
    
    def test_calculation_invalid_input(self):
        self.assertEqual(calculator(2, 2, "nonexistent condition"), "Invalid input.")