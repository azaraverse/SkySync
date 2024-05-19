#!/usr/bin/python3
from flask import flash, redirect, url_for, request, Blueprint
from flask import render_template
from app.forms import WeatherForm
from app.utils import get_weather
from app import app_views


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

    if form.validate_on_submit():
        city = form.city.data
        weather_data = get_weather(city)
    return render_template(
        "index.html", form=form, weather_data=weather_data
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
