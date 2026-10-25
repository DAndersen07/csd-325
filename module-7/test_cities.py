"""Unit tests for city_functions.py."""
import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        """A city and country produce the expected formatted string."""
        self.assertEqual(city_country('Santiago', 'Chile'), 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
