import unittest
from formatted_name_fucntion import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for formatted_name_fucntion.py"""
    def test_first_last_name(self):
        """Will a name like, 'Justice Kamwanja' work?"""
        formatted_name = get_formatted_name('justice', 'kamwanja')
        self.assertEqual(formatted_name, 'Justice Kamwanja')

    def test_first_middle_last_name(self):
        """Do names like, 'Justice Kamwanja Cheshari' work?"""
        formatted_name = get_formatted_name(first='justice', middle='kamwanja', last='cheshari')
        self.assertEqual(formatted_name, 'Justice Kamwanja Cheshari')

unittest.main()