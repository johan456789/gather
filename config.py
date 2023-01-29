import os
from dotenv import load_dotenv, find_dotenv

# this looks for a .env file in the directory and loads it up load_dotenv(find_dotenv())

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False