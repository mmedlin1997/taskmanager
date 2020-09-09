from flask import Blueprint, render_template

home_api = Blueprint('home_api', __name__)

@home_api.route('/', methods=['GET','POST']) # HTML form methods must 1) contain GET 2) exclude PUT & DELETE
def message():
    return render_template('index.html')
