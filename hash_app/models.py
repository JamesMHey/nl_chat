from app import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, Table, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
Base = declarative_base()

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
        self.last_seen = datetime.now()

    def __repr__(self):
        return '<uid:{},number:{}>'.format(self.uid, self.number)

    def seen(self):
        self.last_seen = datetime.now()

    def time_since_last_seen(self): # Return number of seconds since last seen
        return (datetime.now() - self.last_seen).total_seconds()

    def expired(self):
        if self.time_since_last_seen()>(7*24*60):
            return True
        return False

if __name__ == '__main__':
    engine = create_engine('sqlite:///hashpairs.db', echo=False)
    Base.metadata.create_all(engine)
