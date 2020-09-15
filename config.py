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
    SERVER_NAME = '0.0.0.0:5000'

    # Set DB Variables
    MYSQL_USER = environ.get('MYSQL_USER')
    MYSQL_PASSWORD = environ.get('MYSQL_PASSWORD')
    MYSQL_CURSORCLASS = 'DictCursor'
    MYSQL_DB = 'taskdb'
    MYSQL_HOST = 'task-mysql'
    MYSQL_PORT = 3306
    #MYSQL_ROOT_HOST = 127.0.0.1
    #MYSQL_ROOT_PASSWORD = 'NAt1ss4m1gl4m'
    
