#!/usr/bin/python3
"""Forms Module
Defines the forms used in the application
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WeatherForm(FlaskForm):
    """
    Form for submitting a city name to get weather information.

    Attributes:
        city (StringField): The input field for the city name
        submit (SubmitField): The submit button
    """
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Get Weather')
