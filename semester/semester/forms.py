from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

from semester.helpers import TOWNLIST


class ReviewForm(FlaskForm):
    review = StringField('Отзыв', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Отправить отзыв')


class TownForm(FlaskForm):
    town = SelectField('Город', choices=TOWNLIST)
    submit = SubmitField('Выбрать город')
