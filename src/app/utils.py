#!/usr/bin/python3
"""Module to Get weather data from OpenWeatherMap API"""
import requests
from os import getenv
from dotenv import load_dotenv
import sys
from datetime import datetime

load_dotenv()  # load environment variables in .env


# define a function for the search feature that gets weather information
# a given city
def get_weather(city):
    """A function that retrieves weather data from an API

    Args:
        city (str): City name to get weather data for
    Return:
        Returns the json format of response
    """
    # get and ensure OpenWeatherMap API Key is available in the
    # environment variables
    api_key = getenv("WEATHER_API_KEY")
    if not api_key:
        print("API Key is missing...")
        sys.exit(1)

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


# Define a function that retrieves current weather data based on
# passed coordinates. This would be incorporated in a feature that
# displays the weather data on document loadup.
def get_weather_by_coords(lat, lon):
    """A function that retrieves weather data from an API using
    coordinates.

    Args:
        lat (float): Latitude coordinate.
        lon (float): Longitude coordinate.
    Returns:
        JSON response of weather data.
    """

    # get and ensure OpenWeatherMap API Key is available in the
    # environment variables
    api_key = getenv("WEATHER_API_KEY")
    if not api_key:
        print("API Key is missing...")
        sys.exit(1)

    # check if coordinates are of float type by handling float conversion
    try:
        lat = float(lat)
    except ValueError:
        print("Given coordinate for latitude is not of type float!")
        sys.exit(1)

    try:
        lon = float(lon)
    except ValueError:
        print("Given coordinate for longitude is not of type float!")
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


# Define a function that retrieves forecast weather data based on
# passed coordinates. This would be incorporated in a feature that
# displays the weather data on document loadup.
def get_weather_forecast(lat, lon):
    """A function that retrieves a 5-day weather forecast data from an
    API using coordinates.

    Args:
        lat (float): Latitude coordinate.
        lon (float): Longitude coordinate.
    Returns:
        JSON response of weather data.
    """

    # get and ensure OpenWeatherMap API Key is available in the
    # environment variables
    api_key = getenv("WEATHER_API_KEY")
    if not api_key:
        print("API Key is missing...")
        sys.exit(1)

    # check if coordinates are of float type by handling float conversion
    try:
        lat = float(lat)
    except ValueError:
        print("Given coordinate for latitude is not of type float!")
        sys.exit(1)

    try:
        lon = float(lon)
    except ValueError:
        print("Given coordinate for longitude is not of type float!")
        sys.exit(1)

    api_url = "https://api.openweathermap.org/data/2.5/forecast"
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
        print(f"Error: Received status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def capitalise_words(s):
    """
    Capitalises the first alphabet of each word from the description of
    the weather data.

    Args:
        s: strings to capitalise (first char of each words only)
    Returns:
        A capitalised first word for each word given in the weather
        description API.
    """
    return ' '.join(word.capitalize() for word in s.split())


def datetime_filter(timestamp):
    """
    Converts a Unix timestamp to a formatted datetime string.

    Args:
        timestamp (int): The unix timestamp to be converted. This is a
        number representing the number of seconds since the epoch (
        January 1, 1970, 00:00:00 UTC.
        )

    Returns:
        str: A formatted datetime string in the format 'Day, Month, Date,
        Hour:Minute'.
    """
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime('%a, %b, %d, %H:%M')


def datetimeformat(value, format='%H'):
    """
    Converts a datetime string to a specified format.

    Args:
        value (str): The datetime string to be formatted. This should be
        in the format 'YYYY-MM-DD HH:MM:SS'.
        format (str, optional): The format to convert the datetime string
        to. Defaults to '%H', which represents the hour in a 24-hour clock

    Returns:
        str: The formatted datetime string according to the specified
        format.
    """
    date = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return date.strftime(format)
