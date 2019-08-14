import unittest
import calc
#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# Run `python -m unittest test_calc.py`
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-2,-2), -4)

    
if __name__ == '__main__':
    unittest.main() # Run `python test_calc.py` 
    