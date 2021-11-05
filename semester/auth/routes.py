from flask import Flask, render_template, url_for, request, flash, get_flashed_messages, redirect

from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from auth.helpers import UserLogin, password_check, basket_clean, create_basket
from semester import db, app
from auth import auth

from semester.models import MainMenu, User
from auth.forms import LoginForm, RegisterForm

login_manager = LoginManager(app)


@auth.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template(
            'auth/register.html',
            menu_url=MainMenu.query.all(),
            user=db.session.query(User).filter(User.id == current_user.get_id()).first(),
            form=form
        )
    elif request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('repeat')
        if not email:
            flash('Email не указан!', category='unfilled_error')
        else:
            if '@' not in email or '.' not in email:
                flash('Некорректный email!', category='validation_error')
            else:
                if not password or not password2:
                    flash('Пароль не указан!', category='unfilled_error')
                else:
                    if password != password2:
                        flash('Пароли не совпадают!', category='validation_error')
                    else:
                        if password_check(password)['password_ok'] is False:
                            flash('Пароль слишком слабый', category='password_error')
                        else:
                            hash = generate_password_hash(password)
                            user = User(email=email, password=hash, name=name)
                            db.session.add(user)
                            db.session.commit()
                            if user:
                                flash("Регистрация прошла успешно", "operation_success")
                                return redirect(url_for('auth.login'))
                            else:
                                flash("пользователь с таким email уже существует", "error")

        print(request)
        print(get_flashed_messages(True))
        return render_template(
            'auth/register.html',
            menu_url=MainMenu.query.all(),
            user=db.session.query(User).filter(User.id == current_user.get_id()).first(),
            form=form
        )
    else:
        raise Exception(f'Method {request.method} not allowed')
