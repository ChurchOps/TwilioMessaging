from flask_wtf import FlaskForm
from wtforms import StringField

class MessageForm(FlaskForm):
    message = StringField('Message')
