"""Start the API"""
from flask import Flask, jsonify, render_template
from ..app import app_views
from flask_cors import CORS
import os
# from os import getenv
# from dotenv import load_dotenv
# import re
from ..app.utils import capitalise_words, datetime_filter, datetimeformat
import logging

# load_dotenv()
secret_key = os.urandom(24)

# ensure flask can locate the templates and static folder
# template_folder = os.path.join(
#    os.path.dirname(__file__), 'app', 'templates'
#    )
#static_folder = os.path.join(os.path.dirname(__file__), 'app', 'static')

app = Flask(
    __name__, template_folder="../app/templates",
    static_folder="../app/static"
    )

logging.debug("Flask app initialised")

app.config["SECRET_KEY"] = secret_key
app.register_blueprint(app_views, url_prefix='/')
app.jinja_env.filters['capitalise_words'] = capitalise_words
app.jinja_env.filters['datetime'] = datetime_filter
app.jinja_env.filters['datetimeformat'] = datetimeformat
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# return a custom 404 message on page not found.
@app.errorhandler(404)
def not_found(error):
    """
    custom 404 error handler
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    pass
