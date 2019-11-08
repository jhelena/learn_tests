#Должно быть свое про тесты
from flask_wtf import FlaskForm
from webapp.user.models import Users
from wtforms import BooleanField, FileField, HiddenField, PasswordField, SelectField, StringField, SubmitField 
from wtforms.validators import DataRequired, EqualTo, ValidationError
#from wtforms.validators import DataRequired, Email, EqualTo  # было бы с Email, если бы у нас был email в форме регистрации 

class KursForm(FlaskForm):
    major_id = SelectField(u'Направление', choices=[('1', 'Прикладная информатика'), ('2', 'Экономика')], validators=[DataRequired()], render_kw={"class": "form-control"})
    prof_id = SelectField(u'Профиль', choices=[('1', 'Прикладная информатика в дизайне'), ('2', 'Финансы и кредит'), 
        ('3', 'Прикладная информатика в экономике')], validators=[DataRequired()], render_kw={"class": "form-control"})
    kurs_name = StringField("Название курса", validators=[DataRequired()], render_kw={"class": "form-control"})
    percent_result = StringField("Процент прохождения", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})
    
class QuestionForm(FlaskForm):
    major_id = SelectField(u'Направление', choices=[('1', 'Прикладная информатика'), ('2', 'Экономика')], validators=[DataRequired()], render_kw={"class": "form-control"})
    prof_id = SelectField(u'Профиль', choices=[('1', 'Прикладная информатика в дизайне'), ('2', 'Финансы и кредит'), ('3', 'Прикладная информатика в экономике')], validators=[DataRequired()], render_kw={"class": "form-control"})
    kurs_id = SelectField(u'Дисциплина', choices=[('1', 'Информатика и программирование'), ('2', 'WEB-дизайн'), ('3', 'Прикладная семиотика')], validators=[DataRequired()], render_kw={"class": "form-control"})
    img_name = FileField(u'Загрузить фйал')    
    q_text = StringField("Текст вопроса", validators=[DataRequired()], render_kw={"class": "form-control"})
    answ1 = StringField("Вариант ответа 1", validators=[DataRequired()], render_kw={"class": "form-control"})
    answ1_true = BooleanField('Правильный', default=True, render_kw={"class": "form-check-input"})
    answ2 = StringField("Вариант ответа 2", render_kw={"class": "form-control"})
    answ2_true = BooleanField('Правильный', default=False, render_kw={"class": "form-check-input"})
    answ3 = StringField("Вариант ответа 3", render_kw={"class": "form-control"})
    answ3_true = BooleanField('Правильный', default=False, render_kw={"class": "form-check-input"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})

class TestForm(FlaskForm):
    #kurs_id = HiddenField('ID курса', validators=[DataRequired()])
    username = StringField("Введите ФИО", validators=[DataRequired()], render_kw={"class": "form-control"})
    answ = BooleanField('', render_kw={"class": "form-check-input"})
    submit = SubmitField("Отправить результат", render_kw={"class": "btn btn-primary"})

class ResultTest(FlaskForm):
    pass
