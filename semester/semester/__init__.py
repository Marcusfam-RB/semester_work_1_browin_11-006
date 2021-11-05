from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Flask_user:roman2002@localhost:5432/semester1_db"
app.config['SECRET_KEY'] = 'gheghgj3qhgt4q$#^#$he'
app.config.from_object(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from auth import auth
app.register_blueprint(auth, url_prefix='/auth')

from user_profile import user_profile
app.register_blueprint(user_profile, url_prefix='/user_profile')

from semester import routes


