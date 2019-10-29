from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(52), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String(12), index=True, nullable=False)
    id_major = db.Column(db.Integer, nullable=True)
    id_prof = db.Column(db.Integer, nullable=True)
    id_depart = db.Column(db.Integer, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role =='admin'

    def __repr__(self):
        return '<Пользователь {} {}>'.format(self.full_name, self.role)
        #return format(self.full_name)


class Depart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depart_name = db.Column(db.String(120), index=True, unique=True, nullable=False)
    full_name = db.Column(db.String(255), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Кафедра {} {}>'.format(self.depart_name, self.full_name)