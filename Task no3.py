# employee.py

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add raise to the annual salary."""
        self.annual_salary += amount
       # test_employee.py

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Create an employee instance once for all tests."""
        self.emp = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.annual_salary, 55000)

    def test_give_custom_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()