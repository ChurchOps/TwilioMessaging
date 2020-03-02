from flask_wtf import FlaskForm
from wtforms import StringField

class MessageForm(FlaskForm):
    message = StringField('Message')

class ContactForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    cell_phone = StringField('Cell Phone')
    email = StringField('Email')
