import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    def setUp (self):
        self.calculator = SimpleCalculator()

    def add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def subtract(self):
        self.assertEqual(self.calculator.subtract(5,3),2)

    def multiply(self):
        self.assertEqual(self.calculator.multiply(4,2),8)
    
    def divide(self):
        self.assertEqual(self.calculator.divide(6,2),3)
        self.assertIsNone(self.calculator.divide(6, 0))
if __name__ == '__main__':
    unittest.main()

        
