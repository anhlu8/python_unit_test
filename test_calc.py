import unittest
import calc
#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# Run `python -m unittest test_calc.py`
class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
        
if __name__ == '__main__':
    unittest.main() # Run `python test_calc.py` 
    