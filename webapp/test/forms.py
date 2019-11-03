#Должно быть свое про тесты, пока копия из юзера
from flask_wtf import FlaskForm
from webapp.user.models import Users
from wtforms import BooleanField, FileField, PasswordField, SelectField, StringField, SubmitField 
from wtforms.validators import DataRequired, EqualTo, ValidationError
#from wtforms.validators import DataRequired, Email, EqualTo  # было бы с Email, если бы у нас был email в форме регистрации 

class QuestionForm(FlaskForm):
    #major_id = StringField("Направление", validators=[DataRequired()], render_kw={"class": "form-control"})
    #prof_id = StringField("Профиль", validators=[DataRequired()], render_kw={"class": "form-control"})
    #kurs_id = StringField("Дисциплина", validators=[DataRequired()], render_kw={"class": "form-control"})
    major_id = SelectField(u'Направление', choices=[('1', 'Прикладная информатика'), ('2', 'Экономика')], validators=[DataRequired()], render_kw={"class": "form-control"})
    prof_id = SelectField(u'Профиль', choices=[('1', 'Прикладная информатика в дизайне'), ('2', 'Финансы и кредит'), ('3', 'Прикладная информатика в экономике')], validators=[DataRequired()], render_kw={"class": "form-control"})
    kurs_id = SelectField(u'Дисциплина', choices=[('1', 'Информатика и программирование'), ('2', 'WEB-дизайн')], validators=[DataRequired()], render_kw={"class": "form-control"})
    img_name = FileField(u'Загрузить фйал', render_kw={"class": "form-control"})    
    q_text = StringField("Текст вопроса", validators=[DataRequired()], render_kw={"class": "form-control"})
    answ1 = StringField("Вариант ответа 1", validators=[DataRequired()], render_kw={"class": "form-control"})
    answ1_true = BooleanField('Правильный', default=True, render_kw={"class": "form-check-input"})
    answ2 = StringField("Вариант ответа 2", render_kw={"class": "form-control"})
    answ2_true = BooleanField('Правильный', default=False, render_kw={"class": "form-check-input"})
    answ3 = StringField("Вариант ответа 3", render_kw={"class": "form-control"})
    answ3_true = BooleanField('Правильный', default=False, render_kw={"class": "form-check-input"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})

'''    
    def validate_user_name(self, user_name):
        users_count = Users.query.filter_by(user_name=user_name.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким логином уже зарегистрирован')

    def validate_full_name(self, full_name):
        users_count = Users.query.filter_by(full_name=full_name.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')
'''
