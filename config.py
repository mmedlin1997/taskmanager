"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

# Load secrets into environment variables
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    # Set Flask Variables
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True

    # Set DB Variables
    MYSQL_USER = environ.get('MYSQL_USER')
    MYSQL_PASSWORD = environ.get('MYSQL_PASSWORD')
    MYSQL_CURSORCLASS = 'DictCursor'
    