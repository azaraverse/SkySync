#!/usr/bin/python3
""""""
from utils import get_weather_coords
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'app'))


def test_get_weather_coords():
    """"""
    # os.environ["WEATHER_API_KEY"] = "051927028e4af256325429aca369c986"
    lat = 5.884
    lon = -0.092
    weather_data_current = get_weather_coords(lat, lon)

    if weather_data_current:
        print(
            "Weather data for current using latitude "
            "longitude retrieved successfully"
            )
        print(weather_data_current)
    else:
        print("Failed to retrieve weather data for 3.0")
        sys.exit(1)


if __name__ == "__main__":
    test_get_weather_coords()
