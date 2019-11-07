from datetime import datetime
from sqlalchemy.orm import relationship
from webapp.db import db

class Major(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_code = db.Column(db.String(12), index=True, nullable=False)
    major_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Направление {} {}>'.format(self.major_code, self.major_name)

class Prof(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.Integer, db.ForeignKey('major.id', ondelete='CASCADE'), nullable=False)
    prof_name = db.Column(db.String(255), index=True, nullable=False)
    major = relationship('Major', backref='prof')
    
    def __repr__(self):
        return '<Профиль {} {}>'.format(self.prof_name)

class Kurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.Integer, db.ForeignKey('major.id', ondelete='CASCADE'), nullable=False)
    prof_id = db.Column(db.Integer, db.ForeignKey('prof.id', ondelete='CASCADE'), nullable=False)
    depart_id = db.Column(db.Integer, nullable=False)
    kurs_name = db.Column(db.String(255), index=True, nullable=False)
    img_folder = db.Column(db.String(255), nullable=True)
    percent_result = db.Column(db.Integer, nullable=False)
    major = relationship('Major')
    prof = relationship('Prof', backref='kurs')

    def __repr__(self):
        return ' {}'.format(self.kurs_name)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.Integer, db.ForeignKey('major.id', ondelete='CASCADE'), nullable=False)
    prof_id = db.Column(db.Integer, db.ForeignKey('prof.id', ondelete='CASCADE'), nullable=False)
    kurs_id = db.Column(db.Integer, db.ForeignKey('kurs.id', ondelete='CASCADE'), nullable=False)
    q_text = db.Column(db.Text, nullable=False)
    img_name = db.Column(db.String(255), nullable=True)
    answ1 = db.Column(db.String(255), nullable=False)
    answ1_true = db.Column(db.SmallInteger, nullable=False)
    answ2 = db.Column(db.String(255), nullable=True)
    answ2_true = db.Column(db.SmallInteger, nullable=True)
    answ3 = db.Column(db.String(255), nullable=True)
    answ3_true = db.Column(db.SmallInteger, nullable=True)

    major = relationship('Major')
    prof = relationship('Prof')
    kurs = relationship('Kurs', backref='questions')

    def __repr__(self):
        return '<Вопрос {} {}>'.format(self.q_text)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kurs_id = db.Column(db.Integer, db.ForeignKey('kurs.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user_name = db.Column(db.String(255), index=True, nullable=False)
    percent_result = db.Column(db.Float, nullable=False)
    data_test = db.Column(db.DateTime, nullable=False, default=datetime.now())
    kurs = relationship('Kurs')
    users = relationship('Users', backref='result')

    def __repr__(self):
        return '<Результат: {} {} {}>'.format(self.kurs_id, self.user_name, self.percent_result)