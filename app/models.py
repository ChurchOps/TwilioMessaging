from app import db

class Contact(db.Model):
    ContactId = db.Column(db.Integer, index=True, unique=True, primary_key=True)
    FirstName = db.Column(db.String(64))
    LastName = db.Column(db.String(64))
    Email = db.Column(db.String(120))
    Phone = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.FirstName)

class ContactTag(db.Model):
    ContactTagId = db.Column(db.Integer, primary_key=True)
    TagId = db.Column(db.Integer, db.ForeignKey('tag.TagId'))
    ContactId = db.Column(db.Integer, db.ForeignKey('contact.ContactId')) 

class Tag(db.Model):
    TagId = db.Column(db.Integer, primary_key=True)
    TagName = db.Column(db.String())

    def __repre__(self):
        return '<Tag {}>'.format(self.TagName)
