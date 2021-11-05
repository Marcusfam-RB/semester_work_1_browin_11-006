from flask import Blueprint

user_profile = Blueprint('user_profile', __name__, template_folder='templates', static_folder='static')

from user_profile import routes
