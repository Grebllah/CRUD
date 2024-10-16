from flask_sqlalchemy import SQLAlchemy
from CRUD_backend import db

class User (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    email=db.Column(db.String)

def __repr__(self):
    return '<User> {}'.format(self.username)