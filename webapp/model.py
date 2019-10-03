from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, unique=True, nullable=False)
    id_major = db.Column(db.Integer, primary_key=False)
    id_prof = db.Column(db.Integer, primary_key=False)
    id_depart = db.Column(db.Integer, primary_key=False)

    def __repr__(self):
        return '<Users {} {}>'.format(self.full_name, self.role)
