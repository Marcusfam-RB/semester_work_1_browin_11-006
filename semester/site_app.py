# from flask import Flask, render_template, url_for, request, flash, get_flashed_messages, g, abort, \
#                   make_response, redirect, session
#
# from flask_login import login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

from semester import app

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Flask_user:roman2002@localhost:5432/semester1_db"
# app.config['SECRET_KEY'] = 'gheghgj3qhgt4q$#^#$he'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# class User(db.Model):
#     __tablename__ = 'User'
#
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String())
#     password = db.Column(db.String())
#     name = db.Column(db.String())
#     phone_number = db.Column(db.String())
#     address = db.Column(db.String())
#
#     def __init__(self, email, password, name, phone_number=None, address=None):
#         self.email = email
#         self.password = password
#         self.name = name
#         self.phone_number = phone_number
#         self.address = address
#
#     def __repr__(self):
#         return f""
#
#
# class MenuPosition(db.Model):
#     __tablename__ = 'MenuPosition'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     picture = db.Column(db.Integer())
#     price = db.Column(db.Integer())
#     composition = db.Column(db.String())
#
#     def __init__(self, name, picture, price, composition):
#         self.name = name
#         self.picture = picture
#         self.price = price
#         self.composition = composition
#
#     def __repr__(self):
#         return f""
#
#
# class Orders(db.Model):
#     __tablename__ = 'Orders'
#
#     id = db.Column(db.Integer, primary_key=True)
#     positions = db.Column(db.String())
#     cost = db.Column(db.Integer())
#     time = db.Column(db.String())
#     is_done = db.Column(db.Boolean())
#
#     def __init__(self, positions, cost, time, is_done=False):
#         self.positions = positions
#         self.cost = cost
#         self.time = time
#         self.is_done = is_done
#
#     def __repr__(self):
#         return f""
#
#
# class MainMenu(db.Model):
#     __tablename__ = 'MainMenu'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String())
#     url = db.Column(db.String())
#
#     def __init__(self, title, url):
#         self.title = title
#         self.url = url
#
#     def __repr__(self):
#         return f""

#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html', menu_url=MainMenu.query.all())
#     elif request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         if not email:
#             flash('Email не указан!', category='unfilled_error')
#         else:
#             if '@' not in email or '.' not in email:
#                 flash('Некорректный email!', category='validation_error')
#             else:
#                 if not password:
#                     flash('Пароль не указан!', category='unfilled_error')
#                 else:
#                     user = db.session.query(User).filter(User.email == email).first()
#                     if user and check_password_hash(user['password'], password):
#                         userlogin = UserLogin().create(user)
#                         login_user(userlogin)
#                         return redirect(url_for('user_profile'))
#                     flash("Неверный логин или пароль", "validation_error")
#
#         print(request)
#         print(get_flashed_messages(True))
#         return render_template('login.html', menu_url=MainMenu.query.all())
#     else:
#         raise Exception(f'Method {request.method} not allowed')
#
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("Вы вышли из ккаунта", category="operation_success")
#     return redirect(url_for('login'))
#
#
# @app.route("/register", methods=['POST', 'GET'])
# def register():
#     if request.method == 'GET':
#         return render_template('register.html', menu_url=MainMenu.query.all())
#     elif request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         password2 = request.form.get('repeat')
#         if not email:
#             flash('Email не указан!', category='unfilled_error')
#         else:
#             if '@' not in email or '.' not in email:
#                 flash('Некорректный email!', category='validation_error')
#             else:
#                 if not password or not password2:
#                     flash('Пароль не указан!', category='unfilled_error')
#                 else:
#                     if password != password2:
#                         flash('Пароли не совпадают!', category='validation_error')
#                     else:
#                         if password_check(password)['password_ok'] is False:
#                             flash('Пароль слишком слабый', category='password_error')
#                         else:
#                             hash = generate_password_hash(password)
#                             user = User(email=email, password=hash, name=name)
#                             db.session.add(user)
#                             db.session.commit()
#                             if user:
#                                 flash("Регистрация прошла успешно", "operation_success")
#                             else:
#                                 flash("пользователь с таким email уже существует", "error")
#
#         print(request)
#         print(get_flashed_messages(True))
#         return render_template('register.html', menu_url=MainMenu.query.all())
#     else:
#         raise Exception(f'Method {request.method} not allowed')



if __name__ == '__main__':
    app.run(debug=True)