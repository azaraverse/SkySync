#!/usr/bin/python3
"""Module to Get weather data from OpenWeatherMap API"""
import requests
from os import getenv
from dotenv import load_dotenv
import sys

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

    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def get_weather_coords(lat, lon):
    """A function that retrieves weather data from an API using
    coordinates.

    Args:
        lat (float): Latitude coordinate.
        lon (float): Longitude coordinate.
    Returns:
        JSON response of weather data.
    """
    api_key = getenv("WEATHER_API_KEY")
    if not api_key:
        print("API Key is missing...")
        sys.exit(1)

    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
