import unittest
from city_functions import city_country

class FuncTest(unittest.TestCase):
    """Testing city_functions.py"""
    def test_city_country(self):
        """Output example: 'Eldoret, Kenya'."""
        
        output = city_country('eldoret', 'kenya')
        self.assertEqual(output, 'Eldoret, Kenya')

    def test_city_country_population(self):
        "Output example: 'Santiago, Chile -population 5000000"

        output = city_country('Santiago', 'Chile', 5000000)
        self.assertEqual(output, 'Santiago, Chile -population 5000000')

unittest.main()