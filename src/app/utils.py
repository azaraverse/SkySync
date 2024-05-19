#!/usr/bin/python3
"""Module to Get weather data from OpenWeatherMap API"""
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def get_weather(city):
    """A function that retrieves weather data from an API

    Args:
        city (str): City name to get weather data for
    Return:
        Returns the json format of response
    """
    api_key = getenv("WEATHER_API_KEY")
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    return None
