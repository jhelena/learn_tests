from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_required
from webapp.db import db
from webapp.user.decorators import admin_required
from webapp.user.models import Users
from webapp.user.forms import LoginForm, RegisrationForm

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required
def admin_index():
    global users_list
    title = "Администрирование"
    users_list = Users.query.all()
    return render_template('admin/admin.html', page_title=title, users_list=users_list)
    #return render_template('login.html', page_title=title)

@blueprint.route('/register')
def register():
    #if current_user.is_authenticated:
        #return redirect(url_for('index'))
    form = RegisrationForm()
    title = "Регистрация"
    return render_template('admin/registration.html', page_title=title, form=form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegisrationForm()
    if form.validate_on_submit():
        new_user = Users(user_name=form.user_name.data, role=form.role.data, full_name=form.full_name.data, id_major=form.major.data, id_prof=form.prof.data, id_depart=form.depart.data,)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('admin.register'))