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


