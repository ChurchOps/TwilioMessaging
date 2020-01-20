
from app import db

class Contact(db.Model):
    ContactId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Email = db.Column(db.String(120))
    Phone = db.Column(db.String(120))
    PasswordHash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)    

class ContactTag(db.Model):
    ContactTagId = db.Column(db.Integer, primary_key=True)
    TagId = db.Column(db.Integer)
    ContactId = db.Column(db.Integer)

class Tag(db.Model):
    TagId = db.Column(db.Integer, primary_key=True)
    Tag = db.Column(db.String())
