#!/usr/bin/python3
"""Forms Module"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WeatherForm(FlaskForm):
    """"""
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Get Weather')
