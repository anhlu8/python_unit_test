import unittest
import calc
#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# Run `python -m unittest test_calc.py` without main function
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-2,-2), -4)
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-2,-2), 0)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-2,-2), 4)
    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-2,-2),1)
        self.assertEqual(calc.divide(5,2),2.5)
        
        self.assertRaises(ValueError, calc.divide, 10,0) #assertRaises() expects the exception, the function we want to test -- no (), and arguments

    
if __name__ == '__main__':
    unittest.main() # Run `python test_calc.py` 
    