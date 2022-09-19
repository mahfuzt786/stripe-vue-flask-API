"""
config.py
- settings for the flask application object
"""
# import os
from os import environ

class BaseConfig(object):
    DEBUG = True
    # used for encryption and session management
    SECRET_KEY = environ.get('FLASK_SECRET_KEY'), #os.environ['FLASK_SECRET_KEY']
    STRIPE_SECRET_KEY = environ.get('STRIPE_SECRET_KEY')
    STRIPE_PUBLIC_KEY = environ.get('STRIPE_PUBLIC_KEY')

    # DEVELOPMENT = True
    # TESTING = True
    
