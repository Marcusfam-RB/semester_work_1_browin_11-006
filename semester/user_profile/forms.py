from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class EditForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    address = StringField('Адрес', validators=[DataRequired()])
    number = StringField('Номер телефона', validators=[DataRequired()])
    submit = SubmitField('Изменить')


class PasswordForm(FlaskForm):
    old_pass = PasswordField('Старый пароль', validators=[DataRequired()])
    new_pass = PasswordField('Пароль', validators=[DataRequired()])
    new_pass2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Изменить')
