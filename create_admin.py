from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db, Users

app = create_app()

with app.app_context():
    username = input('Введите логин пользователя: ')

    if Users.query.filter(Users.user_name == username).count():
        print('Такой пользователь уже существует!')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        print('Пароли не совпадают!')
        sys.exit(0)

    full_name = input('Введите полное имя пользователя: ')
    role = input('Выберите роль пользователя: ')   # здесь должен быть список из БД
    major = input('Введите направление обучения ')  # здесь должен быть список из БД
    prof = input('Введите профиль обучения ')  # здесь должен быть список из БД
    depart = input('Введите кафедру ')  # здесь должен быть список из БД

    new_user = Users(user_name=username, full_name=full_name, role=role, id_major=major, id_prof=prof, id_depart=depart)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Пользователь {}'.format(new_user.full_name) + ' добавлен.')