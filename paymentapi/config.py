"""
config.py
- settings for the flask application object
"""
import os

class BaseConfig(object):
    DEBUG = True
    # used for encryption and session management
    SECRET_KEY = 'mysecretkey'
    stripe_keys = {
            'secret_key': os.environ['STRIPE_SECRET_KEY'],
            'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
    }
