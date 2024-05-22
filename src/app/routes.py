#!/usr/bin/python3
from flask import flash, redirect, url_for, request, Blueprint, jsonify
from flask import session
from flask import render_template
from app.forms import WeatherForm
from app.utils import get_weather, get_weather_coords
from app.utils import get_weather_forecast
from app import app_views
# import logging

# logging.basicConfig(level=logging.DEBUG)


@app_views.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """
    Route for the landing page/root page to display weather data.

    Renders the main page with the weather form and displays the weather
    data.

    Returns:
        Rendered HTML template for the index/root page.
    """
    form = WeatherForm()
    weather_data = None
    forecast_data = None

    if form.validate_on_submit():
        city = form.city.data
        weather_data = get_weather(city)
        if weather_data:
            lat = weather_data["coord"]["lat"]
            lon = weather_data["coord"]["lon"]
            forecast_data = get_weather_forecast(lat, lon)
            session["weather_data"] = weather_data
            session["forecast_data"] = forecast_data
        return redirect(url_for("app_views.index"))

    # check if there is city-based weather data in the session
    if "weather_data" in session and "forecast_data" in session:
        weather_data = session.pop("weather_data", None)
        forecast_data = session.pop("forecast_data", None)

    return render_template(
        "index.html", form=form, weather_data=weather_data,
        forecast_data=forecast_data
        )


@app_views.route('/search', methods=['GET', 'POST'], strict_slashes=False)
def search():
    """
    Route for searching for weather data by city name.

    Renders the search bar with the weather form.

    Returns:
        Rendered HTML template for the search bar
    """
    form = WeatherForm()

    if form.validate_on_submit():
        city = form.city.data
        return redirect(url_for("app_views.index", city=city))
    return render_template("search.html", form=form)


@app_views.route(
    '/get_weather_by_coords', methods=['POST'], strict_slashes=False
    )
def get_weather_by_coords():
    """"""
    data = request.get_json()
    # logging.debug(f"Received data: {data}")

    if data is None:
        return jsonify(
            {"error": "No data received"}
            ), 400
    lat = data.get("lat")
    lon = data.get("lon")

    if not lat or not lon:
        return jsonify(
            {"error": "Missing coordinates"}
        ), 400

    weather_data = get_weather_coords(lat, lon)
    forecast_data = get_weather_forecast(lat, lon)
    if weather_data and forecast_data:
        return jsonify(
            {
                "weather": weather_data,
                "forecast": forecast_data
            }
            )
    else:
        return jsonify(
            {"error": "Unable to fetch weather data"}
        ), 500


@app_views.route('/forecast', methods=['POST'], strict_slashes=False)
def forecast():
    """"""
    data = request.get_json()

    if data is None:
        return jsonify(
            {"error": "no data retrieved"}
        ), 400
    lat = data.get("lat")
    lon = data.get("lon")

    if not lat or not lon:
        return jsonify(
            {"error": "missing coordinates"}
        ), 400

    forecast_data = get_weather_forecast(lat, lon)
    if forecast_data:
        return jsonify(forecast_data)
    else:
        return jsonify(
            {"error": "unable to retrieve forecast weather data."}
        ), 500
