"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS

def create_app(app_name='PAYMENT_API'):
    app = Flask(app_name)
    CORS(app)
    app.config.from_object('paymentapi.config.BaseConfig')

    from paymentapi.api import payment_api
    app.register_blueprint(payment_api, url_prefix="/api/betterpark-payment")

    return app
