# city_functions.py

def city_country(city, country):
    """Return a city and country formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"
   # test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()