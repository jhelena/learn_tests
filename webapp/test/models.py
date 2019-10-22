from webapp.db import db

class Depart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depart_name = db.Column(db.String, index=True, unique=True, nullable=False)
    full_name = db.Column(db.String, unique=True, nullable=False)

    
    def __repr__(self):
        return '<Кафедра {} {}>'.format(self.depart_name, self.full_name)