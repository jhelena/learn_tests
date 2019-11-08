from flask import Blueprint, flash, Flask, current_app, request, render_template, redirect, send_from_directory, url_for
import os
from webapp.db import db
from flask_login import current_user, login_required
from webapp.user.models import Users, Depart
from webapp.user.forms import LoginForm
from webapp.test.models import Major, Prof, Kurs, Question, Result
from webapp.test.forms import QuestionForm, TestForm, KursForm

from werkzeug.utils import secure_filename

blueprint = Blueprint('test', __name__, url_prefix='/test')

@blueprint.route("/<int:depart_id>")
def test_index(depart_id):
    title = "Работа с тестами для кафедры"
    test_depart = Kurs.query.filter(Kurs.depart_id == depart_id).all()
    return render_template('test/depart.html', page_title=title, test_depart=test_depart, depart_id=depart_id)

@blueprint.route('/input_kurs/<int:depart_id>')
def input_kurs(depart_id):
    form = KursForm()
    title = "Ввод нового курса"
    return render_template('test/input_kurs.html', page_title=title, form=form, depart_id=depart_id)

@blueprint.route('/process-input_kurs/<int:depart_id>', methods=['POST'])
def process_input_kurs(depart_id):
    form = KursForm()
    if form.validate_on_submit():
        #вставка в БД
        new_kurs = Kurs(major_id=form.major_id.data, prof_id=form.prof_id.data, depart_id=depart_id,
            kurs_name=form.kurs_name.data, percent_result=form.percent_result.data)
        db.session.add(new_kurs)
        db.session.commit()
        flash('Курс успешно добавлен!')
        return redirect(url_for('test.test_index', depart_id=depart_id))
    else:
        for field, errors in form.errors.items():
            flash('Ошибка в поле "{}": - {}'.format(
                getattr(form, field).label.text,
                errors
            ))
        return redirect(url_for('test.input_kurs'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('test.input_kurs', depart_id=depart_id))

@blueprint.route('/input/<int:depart_id>')
def input(depart_id):
    form = QuestionForm()
    title = "Ввод вопросов теста"
    return render_template('test/input.html', page_title=title, form=form, depart_id=depart_id)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@blueprint.route('/process-input/<int:depart_id>', methods=['POST'])
def process_input(depart_id):
    form = QuestionForm()
    if form.validate_on_submit():
        #проверка файла
        file = request.files['img_name']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = ''
        
        global answ3_true
        answ3_true = 1 
        if int(form.answ2_true.data) == 1:
            answ3_true = 2
        if int(form.answ3_true.data) == 1:
            answ3_true = 3

        #вставка в БД
        new_question = Question(major_id=form.major_id.data, prof_id=form.prof_id.data, kurs_id=form.kurs_id.data,
            q_text=form.q_text.data, img_name=filename, answ1=form.answ1.data, answ1_true=0, 
            answ2=form.answ2.data, answ2_true=0, answ3=form.answ3.data, answ3_true=answ3_true)
        db.session.add(new_question)
        db.session.commit()
        flash('Вопрос успешно добавлен!')
        return redirect(url_for('test.input', depart_id=depart_id))
    else:
        for field, errors in form.errors.items():
            flash('Ошибка в поле "{}": - {}'.format(
                getattr(form, field).label.text,
                errors
            ))
        return redirect(url_for('test.input'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('test.input', depart_id=depart_id))

@blueprint.route("/student/<int:user_id>")
def test_student(user_id):
    title = "Тесты студента"
    user = Users.query.filter_by(id = user_id).first()
    major_id = user.id_major
    prof_id = user.id_prof

    test_student = Kurs.query.filter(Kurs.major_id == major_id, Kurs.prof_id == prof_id).all()
    return render_template('test/student.html', page_title=title, test_student=test_student, user_id=user_id)

@blueprint.route("/test_pass/<int:kurs_id>")
def test_pass(kurs_id):
    title = "Прохождение теста"
    test_form = TestForm()
    test_name = Kurs.query.filter_by(id=kurs_id).first()
    kurs_name=test_name.kurs_name
    user_id=current_user.id
    test_p = Question.query.filter_by(kurs_id=kurs_id).all()
    return render_template('test/test_pass.html', page_title=title, user_id=user_id, kurs_id=kurs_id, 
        test_p=test_p, kurs_name=kurs_name, form=test_form)

@blueprint.route("/test_view/<int:kurs_id>")
def test_view(kurs_id):
    title = "Просмотр теста"
    test_name = Kurs.query.filter_by(id=kurs_id).first()
    kurs_name=test_name.kurs_name
    user_id=current_user.id
    user_depart = Users.query.filter(Users.id == user_id).first()
    depart_id = user_depart.id_depart
    test_v = Question.query.filter_by(kurs_id=kurs_id).all()
    return render_template('test/test_view.html', page_title=title, user_id=user_id, kurs_id=kurs_id, 
        test_v=test_v, kurs_name=kurs_name, depart_id=depart_id,)

@blueprint.route("/result", methods=['POST'])
def result_test():
    form = TestForm()
    if form.validate_on_submit():
        user_id=current_user.id
        kurs_id = request.form['kurs_id']
        answ_test = Question.query.filter_by(kurs_id=kurs_id).all()
        count = Question.query.filter_by(kurs_id=kurs_id).count()
        i = 0
        res = 0
        for answ in answ_test:
            i=i+1
            a1= int(request.form['answ{}'.format(i)])
            if a1 == int(answ.answ3_true):
                res = int(res)+1
        percent_res = int(res) * 100 / i
        percent_res = '{:3.2f}'.format(percent_res)

        new_res = Result(kurs_id=kurs_id, user_id=user_id, user_name=form.username.data, percent_result=percent_res)
        db.session.add(new_res)
        db.session.commit()
        flash(f'Ваш результат: {percent_res}%. Данные успешно занесены в базу! ')
        return redirect(url_for('test.test_student', user_id=current_user.id, percent_res=percent_res))
    else:
        for field, errors in form.errors.items():
            flash('Ошибка в поле "{}": - {}'.format(
                getattr(form, field).label.text,
                errors
            ))
        return redirect(url_for('test.test_pass', kurs_id=kurs_id))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('test.test_student', user_id=current_user.id))
    
@blueprint.route("/view")
def view_res():
    title = "Результаты теста"
    user_id=current_user.id
    test_res = Result.query.filter_by(user_id=user_id).order_by(Result.kurs_id).all()
    return render_template('test/result.html', page_title=title, test_res=test_res)

@blueprint.route("/reskurs/<int:kurs_id>")
def view_reskurs(kurs_id):
    title = "Результаты теста по курсу"
    user_id=current_user.id
    user_depart = Users.query.filter(Users.id == user_id).first()
    depart_id = user_depart.id_depart
    labels=[]
    values=[]
    test_count = Result.query.filter_by(kurs_id=kurs_id).count()
    if test_count != 0:
        test_res = Result.query.filter_by(kurs_id=kurs_id).all()
        for kurs in test_res:
            kurs_name = kurs.kurs
            labels.append(kurs.user_name)
            values.append(kurs.percent_result)
        return render_template('test/result_kurs.html', page_title=title, test_res=test_res, depart_id=depart_id,
        kurs_name=kurs_name, values=values, labels=labels)
    else:
        flash('Результатов прохождения этого теста нет.')
        return redirect(url_for('test.test_index', depart_id=depart_id))
