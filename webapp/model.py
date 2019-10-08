from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(52), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String(12), index=True, nullable=False)
    id_major = db.Column(db.Integer, primary_key=False)
    id_prof = db.Column(db.Integer, primary_key=False)
    id_depart = db.Column(db.Integer, primary_key=False)

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
