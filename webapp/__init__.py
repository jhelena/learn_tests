from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from webapp.forms import LoginForm
from webapp.model import db, Users
#from webapp.users_db import users_list
#username='admin'

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route("/")
    def index():
        title = "On-line тестирование"
        #users_list = "Проверьте свои знания"
        return render_template('index.html', page_title=title)
    
    @app.route("/login")
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация на сайте"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)
 
    @app.route('/process_login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = Users.query.filter_by(user_name=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно зашли на сайт')
                return redirect(url_for('index'))
        
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы вышли из системы.')
        return redirect(url_for('index'))
    
    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return "Привет, админ!"
        else:
            return 'Ты не админ!'

    return app