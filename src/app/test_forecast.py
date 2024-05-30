#!/usr/bin/python3
"""Test forecast for 5 days"""
from utils import get_weather_forecast
from os import path
import sys
from utils import capitalise_words

# ensure the src/app directory is in the sys.path to import utils
sys.path.append(path.join(path.dirname(__file__), 'src', 'app'))


def test_get_weather_forecast():
    """Test weather forecast function"""
    lat = 5.88
    lon = -0.09

    weather_data = get_weather_forecast(lat, lon)

    if weather_data:
        print("Forecast data retrieved successfully")
        # day 1
        temp = int(weather_data['list'][0]['main']['temp'])
        weather = weather_data['list'][0]['weather'][0]['description']
        feels_like = int(weather_data['list'][0]['main']['feels_like'])
        humidity = int(weather_data['list'][0]['main']['humidity'])
        temp_max = int(weather_data['list'][0]['main']['temp_max'])
        temp_min = int(weather_data['list'][0]['main']['temp_min'])
        wind = int(weather_data['list'][0]['wind']['speed'])
        print(f"1st day forecast:")
        print(f"\t\t Temperature: {temp}°")
        print(f"\t\t Feels like: {feels_like}°")
        print(f"\t\t Conditions: {capitalise_words(weather)}")
        print(f"\t\t Humidity: {humidity}%")
        print(f"\t\t High: {temp_max}°")
        print(f"\t\t Low: {temp_min}°")
        print(f"\t\t Wind Speed: {wind} km/s")

        # day 2
        temp2 = int(weather_data['list'][1]['main']['temp'])
        weather2 = weather_data['list'][1]['weather'][0]['description']
        feels_like2 = int(weather_data['list'][1]['main']['feels_like'])
        humidity2 = int(weather_data['list'][1]['main']['humidity'])
        temp_max2 = int(weather_data['list'][1]['main']['temp_max'])
        temp_min2 = int(weather_data['list'][1]['main']['temp_min'])
        wind2 = int(weather_data['list'][1]['wind']['speed'])
        print(f"2nd day forecast:")
        print(f"\t\t Temperature: {temp2}°")
        print(f"\t\t Feels like: {feels_like2}°")
        print(f"\t\t Conditions: {capitalise_words(weather2)}")
        print(f"\t\t Humidity: {humidity2}%")
        print(f"\t\t High: {temp_max2}°")
        print(f"\t\t Low: {temp_min2}°")
        print(f"\t\t Wind Speed: {wind2} km/s")

        # day 3
        temp3 = int(weather_data['list'][2]['main']['temp'])
        weather3 = weather_data['list'][2]['weather'][0]['description']
        feels_like3 = int(weather_data['list'][2]['main']['feels_like'])
        humidity3 = int(weather_data['list'][2]['main']['humidity'])
        temp_max3 = int(weather_data['list'][2]['main']['temp_max'])
        temp_min3 = int(weather_data['list'][2]['main']['temp_min'])
        wind3 = int(weather_data['list'][2]['wind']['speed'])
        print(f"3rd day forecast:")
        print(f"\t\t Temperature: {temp3}°")
        print(f"\t\t Feels like: {feels_like3}°")
        print(f"\t\t Conditions: {capitalise_words(weather3)}")
        print(f"\t\t Humidity: {humidity3}%")
        print(f"\t\t High: {temp_max3}°")
        print(f"\t\t Low: {temp_min3}°")
        print(f"\t\t Wind Speed: {wind3} km/s")

        # day 4
        temp4 = int(weather_data['list'][3]['main']['temp'])
        weather4 = weather_data['list'][3]['weather'][0]['description']
        feels_like4 = int(weather_data['list'][3]['main']['feels_like'])
        humidity4 = int(weather_data['list'][3]['main']['humidity'])
        temp_max4 = int(weather_data['list'][3]['main']['temp_max'])
        temp_min4 = int(weather_data['list'][3]['main']['temp_min'])
        wind4 = int(weather_data['list'][3]['wind']['speed'])
        print(f"4th day forecast:")
        print(f"\t\t Temperature: {temp4}°")
        print(f"\t\t Feels like: {feels_like4}°")
        print(f"\t\t Conditions: {capitalise_words(weather4)}")
        print(f"\t\t Humidity: {humidity4}%")
        print(f"\t\t High: {temp_max4}°")
        print(f"\t\t Low: {temp_min4}°")
        print(f"\t\t Wind Speed: {wind4} km/s")

        # day 5
        temp5 = int(weather_data['list'][4]['main']['temp'])
        weather5 = weather_data['list'][4]['weather'][0]['description']
        feels_like5 = int(weather_data['list'][4]['main']['feels_like'])
        humidity5 = int(weather_data['list'][4]['main']['humidity'])
        temp_max5 = int(weather_data['list'][4]['main']['temp_max'])
        temp_min5 = int(weather_data['list'][4]['main']['temp_min'])
        wind5 = int(weather_data['list'][4]['wind']['speed'])
        print(f"5th day forecast:")
        print(f"\t\t Temperature: {temp5}°")
        print(f"\t\t Feels like: {feels_like5}°")
        print(f"\t\t Conditions: {capitalise_words(weather5)}")
        print(f"\t\t Humidity: {humidity5}%")
        print(f"\t\t High: {temp_max5}°")
        print(f"\t\t Low: {temp_min5}°")
        print(f"\t\t Wind Speed: {wind5} km/s")
    else:
        print("Failed to retrieve weather data")
        sys.exit(1)


if __name__ == "__main__":
    test_get_weather_forecast()
