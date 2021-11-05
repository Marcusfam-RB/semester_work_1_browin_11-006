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
        elif any(map(str.isdigit, name)) is True:
            flash('Некорректное имя!', category='validation_error')
        elif any(map(str.isdigit, number)) is False:
            flash('Некорректный номер!', category='validation_error')
        else:
            user.name = name
            user.phone_number = number
            user.address = address
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
