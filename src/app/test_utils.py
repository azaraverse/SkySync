#!/usr/bin/python3
from utils import get_weather
from os import environ
from os import path
import sys

# ensure the src/app directory is in the sys.path to import utils
sys.path.append(path.join(path.dirname(__file__), 'src', 'app'))


def test_get_weather():
    """test the get_weather method in utils"""
    # environ["WEATHER_API_KEY"] = "051927028e4af256325429aca369c986"

    city = "Dodowa"
    weather_data = get_weather(city)

    if weather_data:
        print(f"Weather data for {city} retrieved successfully!")
        print(weather_data)
        # test retrieving paramenters to use in html
        name = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = int(weather_data["main"]["temp"])
        feels = int(weather_data["main"]["feels_like"])
        humidity = int(weather_data["main"]["humidity"])
        wind = weather_data["wind"]["speed"]
        conditions = weather_data["weather"][0]["description"]
        print(f'Weather for: {name}, {country}')
        print(f'Temperature: {temperature}°C')  # alt + 0176 for degree sym
        print(f'Feels like: {feels}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind}m/s')
        print(f'Conditions: {conditions}')
    else:
        print(f"Test failed for {city} weather data retrieval...")
        sys.exit(1)

    # test invalid city
    invalid_city = "No City is called this!"
    weather_data = get_weather(invalid_city)

    if weather_data is None:
        print(f"Test failed for '{invalid_city}'...")
        # sys.exit(1)
    else:
        print(f"Test passed for an invalid city. Check your code logic!")


if __name__ == "__main__":
    test_get_weather()
