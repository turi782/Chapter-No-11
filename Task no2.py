# city_functions.py

def city_country(city, country, population):
    """Return a city, country and population formatted string."""
    return f"{city.title()}, {country.title()} – population {population}"
    # city_functions.py

def city_country(city, country, population=None):
    """Return a city and country, optionally with population."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
        # test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_population(self):
        result = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(result, 'Santiago, Chile – population 5000000')

if __name__ == '__main__':
    unittest.main()