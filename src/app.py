#!/usr/bin/python3
from flask import Flask, render_template, jsonify
from app import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    '''custom 404 error handler'''
    return jsonify(
        {"error": "Not found"}
    )
