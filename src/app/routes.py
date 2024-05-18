#!/usr/bin/python3
from flask import flash, redirect, url_for, request, Blueprint
from flask import render_template
from app.forms import WeatherForm
from app.utils import get_weather
from app import app_views


@app_views.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """"""
    form = WeatherForm()
    weather_data = None

    if form.validate_on_submit():
        city = form.city.data
        weather_data = get_weather(city)
    return render_template('index.html', form=form, weather_data=weather_data)


@app_views.route('/search', methods=['GET', 'POST'], strict_slashes=False)
def search():
    """"""
    form = WeatherForm()

    if form.validate_on_submit():
        city = form.city.data
        return redirect(url_for('main.index', city=city))
    return render_template('search.html', form=form)
