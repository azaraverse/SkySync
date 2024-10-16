#!/usr/bin/python3
""" Flask Routes
"""
from flask import redirect, url_for, request, jsonify
from flask import session
from flask import render_template
from ..app.forms import WeatherForm
from ..app.utils import get_weather, get_weather_by_coords
from ..app.utils import get_weather_forecast
from ..app import app_views
# import logging

# logging.basicConfig(level=logging.DEBUG)


@app_views.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """
    Route for the index page to display weather data.

    Renders the main page with the weather form and displays the weather
    data.

    Returns:
        Rendered HTML template for the index/root page.
    """
    form = WeatherForm()
    weather_data = None
    forecast_data = None

    if request.method == "POST":
        city = request.form.get('city')
        if city:
            weather_data = get_weather(city)
            if weather_data:
                lat = weather_data["coord"]["lat"]
                lon = weather_data["coord"]["lon"]
                forecast_data = get_weather_forecast(lat, lon)
                session["weather_data"] = weather_data
                session["forecast_data"] = forecast_data
            else:
                return jsonify(
                    {"Error": "Could not retrieve weather data."}
                )
        else:
            return jsonify({"Error": "City name required."})
        return redirect(url_for("app_views.index"))

    # check if there is city-based weather data in the session
    # pop available weather-data from session to prevent stale data
    if "weather_data" in session and "forecast_data" in session:
        weather_data = session.pop("weather_data", None)
        forecast_data = session.pop("forecast_data", None)

    return render_template("index.html", form=form)


@app_views.route('/search', methods=['GET', 'POST'], strict_slashes=False)
def search():
    """
    Route for searching for weather data by city name.

    Renders the search bar with the weather form.

    Returns:
        Rendered HTML template for the search bar
    """
    form = WeatherForm()
    weather_data = None
    forecast_data = None

    if request.method == "POST":
        city = request.form.get('city')
        if city:
            # fetch weather data using the utility function
            weather_data = get_weather(city)
            if weather_data:
                lat = weather_data["coord"]["lat"]
                lon = weather_data["coord"]["lon"]
                forecast_data = get_weather_forecast(lat, lon)
                return jsonify(weather_data)
            else:
                return render_template(
                    "search.html", form=form,
                    error="Could not retrieve weather data"
                ), 400
        else:
            return render_template(
                "search.html", form=form, error="City name is required."
            ), 400
    return render_template(
        "search.html", form=form, weather_data=weather_data,
        forecast_data=forecast_data
    )


@app_views.route(
    '/get_weather_by_coords', methods=['POST'], strict_slashes=False
    )
def get_weather_using_coords():
    """
    Route for getting weather data using coordinates from the JavaScript
    geolocation retrieved from browser.

    Returns:
        Weather data retrieved successfully.
    """
    data = request.get_json()
    # logging.debug(f"Received data: {data}")

    if data is None:
        return jsonify(
            {"Error": "No data received."}
            ), 400
    lat = data.get('latitude')
    lon = data.get('longitude')

    if not lat or not lon:
        return jsonify(
            {"Error": "Missing coordinates."}
        ), 400

    weather_data = get_weather_by_coords(lat, lon)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify(
            {"Error": "Unable to fetch weather data."}
        ), 500


@app_views.route('/forecast', methods=['POST'], strict_slashes=False)
def forecast():
    """
    Route for getting forecast weather data using the coordinates from
    the JavaScript file retrieved from the browser's geolocation.

    Returns:
        Weather data retrieved successfully.
    """
    data = request.get_json()

    if data is None:
        return jsonify(
            {"Error": "No data retrieved."}
        ), 400
    lat = data.get("lat")
    lon = data.get("lon")

    if not lat or not lon:
        return jsonify(
            {"Error": "Missing coordinates."}
        ), 400

    forecast_data = get_weather_forecast(lat, lon)
    if forecast_data:
        return jsonify(forecast_data)
    else:
        return jsonify(
            {"Error": "Unable to retrieve forecast weather data."}
        ), 500


@app_views.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """
    Route for displaying the about html page of the weather app.

    Returns:
        A rendered html template that contains the about section of the
        weather app.
    """
    return render_template('about.html')
