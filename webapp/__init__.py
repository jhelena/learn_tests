from flask import Flask, render_template, request

from webapp.model import db, Users
#from webapp.python_org_news import get_python_news
#from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = "On-line тестирование"
        #weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        users_list = Users.query.all()
        return render_template('index.html', page_title=title, users_list =users_list)

    return app

