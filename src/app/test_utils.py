#!/usr/bin/python3
from os import environ
from os import path
import sys

# ensure the src/app directory is in the sys.path to import utils
sys.path.append(path.join(path.dirname(__file__), 'src', 'app'))

from utils import get_weather


def test_get_weather():
    """test the get_weather method in utils"""
    environ["WEATHER_API_KEY"] = "051927028e4af256325429aca369c986"

    city = "Dodowa"
    weather_data = get_weather(city)

    if weather_data:
        print(f"Weather data for {city} retrieved successfully!")
        print(weather_data)
    else:
        print(f"Test failed for {city} weather data retrieval...")

    # test invalid city


if __name__ == "__main__":
    test_get_weather()
