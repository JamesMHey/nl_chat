from app import db
from twilio_interface import twilio_interface

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)

class HashPair(db.Model):
    __tablename__ = 'hashpairs'

    uid = db.Column(db.String(), primary_key = True)
    number = db.Column(db.String())

    def __init__(self, uid, number):
        self.uid = uid
        self.number = number

    def 
