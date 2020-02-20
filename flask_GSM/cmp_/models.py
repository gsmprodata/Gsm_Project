from cmp_ import app
from cmp_.db import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True,nullable = False)
    email = db.Column(db.String(100),unique = True,nullable = False)
    password = db.Column(db.String(100),unique = True,nullable = False)