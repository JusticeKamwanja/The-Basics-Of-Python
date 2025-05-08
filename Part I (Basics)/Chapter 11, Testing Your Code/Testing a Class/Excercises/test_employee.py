# Write a test case for Employee.

# Write two test methods, test_give_default_raise() and test_give_custom_raise().

# Use the setUp() method so you don’t have to create a new employee instance in each test method.

# Run your test case, and make sure both tests pass.

# Import statements.
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for employee class."""

    def setUp(self):
        self.me = Employee('justice', 'kamwanja', 50000)

    def test_give_default_raise(self):
        """Test the default raise of $5000."""
        self.added_salary = self.me.give_raise()
        self.assertEqual(self.added_salary, 55000)

    def test_give_custom_raise(self):
        """Test for a custom raise of any amount."""
        self.added_salary = self.me.give_raise(4000)
        self.assertEqual(self.added_salary, 54000)

unittest.main()