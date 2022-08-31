"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
import stripe


def create_app(app_name='PAYMENT_API'):
    app = Flask(app_name)
    app.config.from_object('paymentapi.config.BaseConfig')

    stripe.api_key = stripe_keys['secret_key']

    from paymentapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    return app
