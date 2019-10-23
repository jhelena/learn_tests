from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo
#from wtforms.validators import DataRequired, Email, EqualTo  # было бы с Email, если бы у нас был email в форме регистрации 

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})


class RegisrationForm(FlaskForm):
    user_name = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField("Пароль", validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    role = StringField("Роль пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    full_name = StringField("Полное имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    major = StringField("Направление", render_kw={"class": "form-control"}) #убрали валидатор, т.к. не всегда заполняем и далее тоже
    prof = StringField("Профиль", render_kw={"class": "form-control"})
    depart = StringField("Кафедра", render_kw={"class": "form-control"})

    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})