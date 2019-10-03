import requests
from flask import Flask, render_template, request

from webapp.model import db, Users
from webapp.users_db import users_list
username='admin'

def index():
    title = "On-line тестирование"
    users_list = Users.query.all()
    return render_template('index.html', page_title=title, users_list =users_list)
def sign_up():
    return render_template('sign_up.html')
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/", methods=['post', 'get'])
    def check():
        if username=='admin':
            title = "On-line тестирование"
            result=index()
        else: 
            result=sign_up()
        return result
   
    return app