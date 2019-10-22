from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.models import Users
from webapp.users_db import users_list
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')
    def index():
        title = "On-line тестирование"
        return render_template('index.html', page_title=title)

    return app
