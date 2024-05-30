#!/usr/bin/python3
from os import path
import sys
import unittest

# ensure the src/tests directory is in the sys.path to import utils
# sys.path.append(path.join(path.dirname(path.abspath(__file__)), '..', 'app'))

from app.utils import get_weather


class TestUtils(unittest.TestCase):
    def test_get_weather_valid_city(self):
        """Test the get_weather method in utils for valid city"""
        # environ["WEATHER_API_KEY"] = "051927028e4af256325429aca369c986"
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIsNotNone(
            weather_data, f"Failed to retrieve weather data for {city}"
        )
        self.assertIn("name", weather_data)
        self.assertIn("sys", weather_data)
        self.assertIn("main", weather_data)
        self.assertIn("wind", weather_data)
        self.assertIn("weather", weather_data)

    def test_get_weather_invalid_city(self):
        """Test get_weather util for invalid city"""
        invalid_city = "No city is called this!"
        weather_data = get_weather(invalid_city)
        self.assertIsNone(
            weather_data, f"Unexpected data for {invalid_city}"
        )


if __name__ == "__main__":
    unittest.main()
