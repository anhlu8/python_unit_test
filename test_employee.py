import unittest
from pprint import pprint
from employee import Employee
from unittest.mock import patch #patch can be used as a decorator or a context manager

class TestEmployee(unittest.TestCase):
    
    def setUp(self): #this method comes with unittest
        # pprint('Inside setUP') # This returns 'Inside setUP'
        print('Inside setUp()') # This returns Inside setUP
        self.emp_1 = Employee('Bob', 'Smith', 5000)
        self.emp_2 = Employee('Sue', 'Smith', 6000)
    
    def tearDown(self): #this method comes with unittest
        print('Inside tearDown()\n')
        pass
    
    def test_email(self):
        print('Inside test_email()')
        self.assertEqual(self.emp_1.email, 'Bob.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email, 'John.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')


    def test_fullname(self):
        print('Inside test_fullname()')
        self.assertEqual(self.emp_1.fullname, 'Bob Smith')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.fullname, 'John Smith')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        
    def test_apply_raise(self):
        print('Inside test_apply_raise()')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 6300)
        
    
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, "Success")
            
            
if __name__ == '__main__':
    unittest.main()
    