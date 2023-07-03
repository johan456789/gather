import os
from dotenv import load_dotenv, find_dotenv

# this looks for a .env file in the directory and loads it up load_dotenv(find_dotenv())

#The .env file typically contains configuration variables like secret keys, API credentials, and database URLs.

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    EXAMPLE_PHOTO_URL = os.environ.get('EXAMPLE_PHOTO_URL')

#This configuration file provides a centralized place to store various settings used by the Flask application. By loading environment variables from the .env file, it ensures that sensitive information is not hardcoded in the source code and can be easily changed or kept secret.





