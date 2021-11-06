from flask import Flask, render_template, url_for, request, flash, get_flashed_messages, redirect

from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from auth.helpers import UserLogin, password_check, basket_clean, create_basket
from semester import db, app
from auth import auth

from semester.models import MainMenu, User
from auth.forms import LoginForm, RegisterForm

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return UserLogin().from_db(user_id, db)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template(
            'auth/login.html',
            menu_url=MainMenu.query.all(),
            user=db.session.query(User).filter(User.id == current_user.get_id()).first(),
            form=form
        )
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('rememberme')
        if remember:
            remember = True
        else:
            remember = False
        if not email:
            flash('Email не указан!', category='unfilled_error')
        else:
            if '@' not in email or '.' not in email:
                flash('Некорректный email!', category='validation_error')
            else:
                if not password:
                    flash('Пароль не указан!', category='unfilled_error')
                else:
                    user = db.session.query(User).filter(User.email == email).first()
                    if user and check_password_hash(user.password, password):
                        userlogin = UserLogin().create(user)
                        login_user(userlogin, remember=remember)
                        create_basket()
                        flash("Вы успешно авторизовались", category="success")
                        return redirect(url_for('user_profile.profile'))
                    flash("Неверный логин или пароль", category="validation_error")

        print(request)
        print(get_flashed_messages(True))
        return render_template(
            'auth/login.html',
            menu_url=MainMenu.query.all(),
            user=db.session.query(User).filter(User.id == current_user.get_id()).first(),
            form=form
        )
    else:
        raise Exception(f'Method {request.method} not allowed')


@auth.route('/logout')
@login_required
def logout():
    basket_clean()
    create_basket()
    logout_user()
    flash("Вы вышли из ккаунта", category="operation_success")
    return redirect(url_for('auth.login'))


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
        if not email or not name:
            flash('Email или имя не указан!', category='unfilled_error')
        elif '@' not in email or '.' not in email:
            flash('Некорректный email!', category='validation_error')
        elif db.session.query(User).filter(User.email == email).first():
            flash('Пользователь с такой почтой уже зарегестрирован', category='validation_error')
        elif not password or not password2:
            flash('Пароль не указан!', category='unfilled_error')
        elif password != password2:
            flash('Пароли не совпадают!', category='validation_error')
        elif password_check(password)['password_ok'] is False:
            flash('Пароль слишком слабый', category='password_error')
        else:
            hash = generate_password_hash(password)
            user = User(email=email, password=hash, name=name)
            db.session.add(user)
            db.session.commit()
            if user:
                flash("Регистрация прошла успешно", "success")
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
