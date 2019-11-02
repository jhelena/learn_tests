from webapp.db import db
from sqlalchemy.orm import relationship

class Major(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_code = db.Column(db.String(12), index=True, nullable=False)
    major_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Направление {} {}>'.format(self.major_code, self.major_name)

class Prof(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.Integer, db.ForeignKey('major.id'), nullable=False)
    prof_name = db.Column(db.String(255), index=True, nullable=False)
    major = relationship('Major')
    
    def __repr__(self):
        return '<Профиль {} {}>'.format(self.prof_name)

class Kurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.Integer, db.ForeignKey('major.id'), nullable=False)
    prof_id = db.Column(db.Integer, db.ForeignKey('prof.id'), nullable=False)
    depart_id = db.Column(db.Integer, nullable=False)
    kurs_name = db.Column(db.String(255), index=True, nullable=False)
    img_folder = db.Column(db.String(255), nullable=True)
    percent_result = db.Column(db.Integer, nullable=False)
    major = relationship('Major')
    prof = relationship('Prof')

    def __repr__(self):
        return '<Дисциплина {} {}>'.format(self.kurs_name)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.Integer, db.ForeignKey('major.id'), nullable=False)
    prof_id = db.Column(db.Integer, db.ForeignKey('prof.id'), nullable=False)
    kurs_id = db.Column(db.Integer, db.ForeignKey('kurs.id'), nullable=False)
    q_text = db.Column(db.Text, nullable=False)
    img_name = db.Column(db.SmallInteger, nullable=True)
    answ1 = db.Column(db.String(255), nullable=False)
    answ1_true = db.Column(db.SmallInteger, nullable=False)
    answ2 = db.Column(db.String(255), nullable=True)
    answ2_true = db.Column(db.SmallInteger, nullable=True)
    answ3 = db.Column(db.String(255), nullable=True)
    answ3_true = db.Column(db.SmallInteger, nullable=True)

    major = relationship('Major')
    prof = relationship('Prof')
    kurs = relationship('Kurs')


    def __repr__(self):
        return '<Вопрос {} {}>'.format(self.q_text)