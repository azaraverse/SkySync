#!/usr/bin/python3
"""
Unittest for testing the utils for the weather app
"""
from os import path
import sys
import unittest

# ensure the src/tests directory is in the sys.path to import utils
# sys.path.append(path.join(path.dirname(path.abspath(__file__)), '..', 'app'))

from app.utils import get_weather


class TestUtils(unittest.TestCase):
    """Testing the utils for the weather app"""
    def test_get_weather_valid_city(self):
        """Test the get_weather method in utils for valid city"""
        # environ["WEATHER_API_KEY"] = "051927028e4af256325429aca369c986"
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIsNotNone(
            weather_data, f"Failed to retrieve weather data for {city}"
        )

    def test_coord_utils(self):
        """Test the coord for the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("coord", weather_data)

    def test_weather(self):
        """Test the main weather info of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("weather", weather_data)

    def test_weather_description(self):
        """Test the weather description of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("description", weather_data['weather'][0])

    def test_weather_icon(self):
        """Test the weather description of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("icon", weather_data['weather'][0])

    def test_location_utils(self):
        """Test the location for the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("name", weather_data)
        self.assertEqual(city, weather_data['name'])

    def test_sys_utils(self):
        """Test sys of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("sys", weather_data)

    def test_sys_data(self):
        """Test the content of the sys dict of the weather info"""
        city = "Accra"
        country = "GH"
        weather_data = get_weather(city)

        self.assertIn("country", weather_data['sys'])
        self.assertIn("sunrise", weather_data['sys'])
        self.assertIn("sunset", weather_data['sys'])
        self.assertEqual(country, weather_data['sys']['country'])

    def test_main_utils(self):
        """Test the main dict for the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("main", weather_data)

    def test_temp(self):
        """Test the content of the main dict of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("temp", weather_data['main'])

    def test_feels_like(self):
        """Test the content of the main dict of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("feels_like", weather_data['main'])

    def test_temp_min(self):
        """Test the content of the main dict of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("temp_min", weather_data['main'])

    def test_temp_max(self):
        """Test the content of the main dict of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("temp_max", weather_data['main'])

    def test_humidity(self):
        """Test the content of the main dict of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("humidity", weather_data['main'])

    def test_datetime(self):
        """Test the current datetime of the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("dt", weather_data)

    def test_wind_utils(self):
        """Test the wind dict for the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

        self.assertIn("wind", weather_data)

    def test_weather_utils(self):
        """Test the weather dict for the weather data"""
        city = "Accra"
        weather_data = get_weather(city)

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
