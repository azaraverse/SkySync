#!/usr/bin/python3
"""
Unittest to test the accuracy of the weather forecast
retrival module and method
"""
from app.utils import get_weather_forecast
import unittest


class TestForecast(unittest.TestCase):
    """Testing the Weather Forecast method"""
    def test_weather_forecast(self):
        """Testing the module"""
        latitude = 5.88
        longitude = -0.09
        weather_data = get_weather_forecast(latitude, longitude)

        self.assertIsNotNone(
            weather_data, "Failed to retrieve weather data for given "
            "coordinates."
        )

    def test_list(self):
        """Test the availablity of list in weather data"""
        latitude = 5.88
        longitude = -0.09
        weather_data = get_weather_forecast(latitude, longitude)

        self.assertIn("list", weather_data)

    def test_main(self):
        """Test the availablity of main in weather data"""
        longitude = -0.09
        latitude = 5.88
        weather_data = get_weather_forecast(latitude, longitude)

        self.assertIn("main", weather_data['list'][0])

    def test_temp(self):
        """Test the temperature for the forecast"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("temp", weather_data['list'][0]['main'])

    def test_feels_like(self):
        """Test the feels_like param of the forecast"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("feels_like", weather_data['list'][0]['main'])

    def test_temp_min(self):
        """Test the minimum temperature param of the forecast"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("temp_min", weather_data['list'][0]['main'])

    def test_temp_max(self):
        """Test the maximum temperature param of teh forecast"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("temp_max", weather_data['list'][0]['main'])

    def test_humidity(self):
        """Test the humidity parameter of the forecast data"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("humidity", weather_data['list'][0]['main'])

    def test_weather(self):
        """Test the availability of weather for extracting description"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("weather", weather_data['list'][0])

    def test_weather_description(self):
        """Test the availability of description in weather data"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn(
            "description", weather_data['list'][0]['weather'][0]
        )

    def test_weather_icon(self):
        """Test the availability of icon in weather description"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("icon", weather_data['list'][0]['weather'][0])

    def test_weather_windspeed(self):
        """Test the availability of wind speed in weather data"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("speed", weather_data['list'][0]['wind'])

    def test_current_datetime(self):
        """Test the availablity of current datetime"""
        lat = 5.88
        lon = -0.09
        weather_data = get_weather_forecast(lat, lon)

        self.assertIn("dt_txt", weather_data['list'][0])


if __name__ == "__main__":
    unittest.main()
