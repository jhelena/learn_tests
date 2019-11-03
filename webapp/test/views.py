from flask import Blueprint, flash, Flask,  current_app, request, render_template, redirect, send_from_directory, url_for
import os
from webapp.db import db
from flask_login import current_user, login_required
from webapp.user.models import Users, Depart
from webapp.user.forms import LoginForm
from webapp.test.models import Major, Prof, Kurs, Question
from webapp.test.forms import QuestionForm

from werkzeug.utils import secure_filename

blueprint = Blueprint('test', __name__, url_prefix='/test')
#UPLOAD_FOLDER = f"{basedir/upload/img}"
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


@blueprint.route("/")
def test_index():
    title = "Работа с тестами для кафедры"
    return render_template('test/depart.html', page_title=title)

@blueprint.route('/input')
def input():
    form = QuestionForm()
    title = "Ввод теста"
    return render_template('test/input.html', page_title=title, form=form)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@blueprint.route('/process-input', methods=['POST'])
def process_input():
    form = QuestionForm()
    if form.validate_on_submit():
        #проверка файла
        file = request.files['img_name']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        #вставка в БД
        new_question = Question(major_id=form.major_id.data, prof_id=form.prof_id.data, kurs_id=form.kurs_id.data,
            q_text=form.q_text.data, answ1=form.answ1.data, answ1_true=form.answ1_true.data, 
            answ2=form.answ2.data, answ2_true=form.answ2_true.data, 
            answ3=form.answ3.data, answ3_true=form.answ3_true.data, img_name=filename)
        db.session.add(new_question)
        db.session.commit()
        flash('Вопрос успешно добавлен!')
        return redirect(url_for('test.input'))
    else:
        for field, errors in form.errors.items():
            flash('Ошибка в поле "{}": - {}'.format(
                getattr(form, field).label.text,
                errors
            ))
        return redirect(url_for('test.input'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('test.input'))