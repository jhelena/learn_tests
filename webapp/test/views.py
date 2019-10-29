from flask import Blueprint, flash, render_template, redirect, url_for
from webapp.db import db
from flask_login import current_user, login_required
from webapp.user.models import Users, Depart
from webapp.user.forms import LoginForm
from webapp.test.models import Major, Prof
from webapp.test.forms import QuestionForm

blueprint = Blueprint('test', __name__, url_prefix='/test')

@blueprint.route("/")
def test_index():
    title = "Работа с тестами для кафедры"
    #if current_user.is_authenticated:
    #return "Меню работы с тестами для кафедры!"
    return render_template('test/depart.html', page_title=title)

@blueprint.route('/input')
def register():
    #if current_user.is_authenticated:
        #return redirect(url_for('index'))
    form = QuestionForm()
    title = "Ввод теста"
    return render_template('test/input.html', page_title=title, form=form)


@blueprint.route('/process-input', methods=['POST'])
def process_reg():
    form = QuestionFormForm()
    if form.validate_on_submit():
        new_question = Question(major_id=form.major_id.data, prof_id=form.prof_id.data, kurs_id=form.kurs_id.data,
            q_text=form.q_text.data, answ1=form.answ1.data, answ1_true=form.answ1_true.data, 
            answ2=form.answ1.data, answ2_true=form.answ1_true.data, 
            answ3=form.answ1.data, answ3_true=form.answ1_true.data)
        db.session.add(new_question)
        db.session.commit()
        flash('Вопрос успешно добавлен!')
        return redirect(url_for('test'))
    else:
        for field, errors in form.errors.items():
            flash('Ошибка в поле "{}": - {}'.format(
                getattr(form, field).label.text,
                errors
            ))
        return redirect(url_for('test.input'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('test.input'))