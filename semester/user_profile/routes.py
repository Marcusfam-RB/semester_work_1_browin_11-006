from flask import Flask, render_template, url_for, request, flash, get_flashed_messages, redirect, session

from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from auth.helpers import password_check
from semester import db
from user_profile import user_profile
from user_profile.forms import EditForm, PasswordForm

from semester.models import MainMenu, User


@user_profile.route('/user_profile', methods=['POST', 'GET'])
@login_required
def profile():
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == 'GET':
        return render_template(
            'user_profile/profile.html',
            menu_url=MainMenu.query.all(),
            user=user,
            p_amount=len(session['basket'])
        )
    elif request.method == 'POST':
        return redirect(url_for(
            'user_profile.edit.html',
            menu_url=MainMenu.query.all(),
            user=user
        ))


@user_profile.route('/edit', methods=['POST', 'GET'])
@login_required
def edit():
    form = EditForm()
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == 'GET':
        return render_template(
            'user_profile/edit.html',
            menu_url=MainMenu.query.all(),
            user=user,
            form=form
        )
    elif request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')
        if not name or not number or not address or not email:
            flash('Не все поля заполнены!', category='unfilled_error')
        elif '@' not in email or '.' not in email:
            flash('Некорректный email!', category='validation_error')
        elif email != user.email and  db.session.query(User).filter(User.email == user.email).first():
            flash('Пользователь с таким email уже существует!', category='validation_error')
        elif any(map(str.isdigit, name)) is True:
            flash('Некорректное имя!', category='validation_error')
        elif not number.isdigit():
            flash('Некорректный номер!', category='validation_error')
        else:
            user.name = name
            user.phone_number = number
            user.address = address
            user.email = email
            db.session.commit()
            flash("Изменения успешно применены!", category='success')
            return redirect(url_for(
                'user_profile.profile',
                menu_url=MainMenu.query.all(),
                user=user
            ))
        print(request)
        print(get_flashed_messages(True))
        return render_template(
            'user_profile/edit.html',
            menu_url=MainMenu.query.all(),
            user=user,
            form=form
        )
    else:
        raise Exception(f'Method {request.method} not allowed')


@user_profile.route('/edit_pass', methods=['POST', 'GET'])
@login_required
def edit_pass():
    form = PasswordForm()
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == 'GET':
        return render_template(
            'user_profile/edit_pass.html',
            menu_url=MainMenu.query.all(),
            user=user,
            form=form
        )
    elif request.method == 'POST':
        new_pass = request.form.get('new_pass')
        new_pass2 = request.form.get('new_pass2')
        old_pass = request.form.get('old_pass')
        if not new_pass or not new_pass2 or not old_pass:
            flash('Пароль не указан!', category='unfilled_error')
        else:
            print(user.password, old_pass)
            if check_password_hash(user.password, old_pass) is False:
                flash('Неверный пароль!', category='validation_error')
            else:
                if new_pass != new_pass2:
                    flash('Пароли не совпадают!', category='validation_error')
                else:
                    if password_check(new_pass)['password_ok'] is False:
                        flash('Пароль слишком слабый', category='password_error')
                    else:
                        hash = generate_password_hash(new_pass)
                        user.password = hash
                        db.session.commit()
                        flash("Пароль успешно изменён!", category='success')
                        return redirect(url_for(
                            'user_profile.profile',
                            menu_url=MainMenu.query.all(),
                            user=user,
                            form=form
                        ))
        print(request)
        print(get_flashed_messages(True))
        return render_template(
                'user_profile/edit_pass.html',
                menu_url=MainMenu.query.all(),
                user=user,
                form=form
        )
    else:
        raise Exception(f'Method {request.method} not allowed')
