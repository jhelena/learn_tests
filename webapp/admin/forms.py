from flask_wtf import FlaskForm
from webapp.user.models import Users
from wtforms import PasswordField, StringField, SubmitField,SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError
#from wtforms.validators import Email  #если бы у нас был email в форме регистрации 

class RegisrationForm(FlaskForm):
    user_name = StringField("Логин пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField("Повторите пароль", validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    #role = StringField("Роль пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    role = SelectField(u'Роль пользователя', choices=[('student', 'Студент'), ('department', 'Кафедра')], 
        validators=[DataRequired()], render_kw={"class": "form-control"})
    full_name = StringField("Полное имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    #major = StringField("Направление", render_kw={"class": "form-control"}) #убрали валидатор, т.к. не всегда заполняем и далее тоже
    #prof = StringField("Профиль", render_kw={"class": "form-control"})
    major = SelectField(u'Направление', choices=[('', 'Выберите направление'),('1', 'Прикладная информатика'), 
        ('2', 'Экономика')], render_kw={"class": "form-control"})
    prof = SelectField(u'Профиль', choices=[('', 'Выберите профиль'),('1', 'Прикладная информатика в дизайне'), 
        ('2', 'Финансы и кредит'), ('3', 'Прикладная информатика в экономике')], render_kw={"class": "form-control"})
    depart = SelectField(u'Кафедра', choices=[('', 'Выберите кафедру'),('1', 'Информационных систем'), 
        ('2', 'Информационных технологий'), ('3', 'Прикладной математики')], render_kw={"class": "form-control"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})

    def validate_user_name(self, user_name):
        users_count = Users.query.filter_by(user_name=user_name.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким логином уже зарегистрирован')

    def validate_full_name(self, full_name):
        users_count = Users.query.filter_by(full_name=full_name.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')