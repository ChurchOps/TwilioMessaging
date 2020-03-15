from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

class FileForm(FlaskForm):
    file = FileField(validators=[FileRequired()])

class MessageForm(FlaskForm):
    message = StringField('Message', widget=TextArea())

class ContactForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    cell_phone = StringField('Cell Phone')
    email = StringField('Email')

class TagForm(FlaskForm):
    Tag_name = StringField('Tag')
    Default = BooleanField('Default Tag')

