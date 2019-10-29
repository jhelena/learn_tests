from flask_wtf import FlaskForm
from webapp.user.models import Users
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
#from wtforms.validators import DataRequired, Email, EqualTo  # было бы с Email, если бы у нас был email в форме регистрации 

class RegisrationForm(FlaskForm):
    user_name = StringField("Логин пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField("Пароль", validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    role = StringField("Роль пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    full_name = StringField("Полное имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    major = StringField("Направление", render_kw={"class": "form-control"}) #убрали валидатор, т.к. не всегда заполняем и далее тоже
    prof = StringField("Профиль", render_kw={"class": "form-control"})
    depart = StringField("Кафедра", render_kw={"class": "form-control"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})

    def validate_user_name(self, user_name):
        users_count = Users.query.filter_by(user_name=user_name.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким логином уже зарегистрирован')

    def validate_full_name(self, full_name):
        users_count = Users.query.filter_by(full_name=full_name.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')