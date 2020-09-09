from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)                   # initialize instance of WSGI application
app.config.from_object('config.Config') # configure Flask and DB

mysql = MySQL(app)                      # database object for controller imports  

# import blueprint API route controller(s)
from app.routes.task_api import task_api   
from app.routes.home_api import home_api

# register API controller(s) with Flask
app.register_blueprint(task_api)        
app.register_blueprint(home_api)
