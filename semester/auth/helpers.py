from flask import session
import re
from semester.models import User


class UserLogin:
    def from_db(self, user_id, db):
        self.__user = db.session.query(User).filter(User.id == user_id).first()
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anoymous(self):
        return False

    def get_id(self):
        return str(self.__user.id)


def password_check(password):
    """
    verify the strength of 'password'
    returns a dict indicating the wrong criteria
    a password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[a-z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }

def basket_clean():
    session.pop('basket', None)
    session.pop('total', None)
    return 'Visits deleted'


def create_basket():
    if not session.get('basket'):
        session['basket'] = []
        session['total'] = 0