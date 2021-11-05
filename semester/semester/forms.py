from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea

from semester.helpers import TOWNLIST





class TownForm(FlaskForm):
    town = SelectField('Город', choices=TOWNLIST)
    submit = SubmitField('Выбрать город')
