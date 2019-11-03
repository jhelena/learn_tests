from flask_wtf import FlaskForm
from webapp.user.models import Users
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
#from wtforms.validators import DataRequired, Email, EqualTo  # было бы с Email, если бы у нас был email в форме регистрации 

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})


