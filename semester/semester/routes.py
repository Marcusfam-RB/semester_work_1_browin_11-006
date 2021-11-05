from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_login import login_required, current_user
from semester import app, db
from semester.models import MainMenu, MenuPosition, User, OrdersPositions, Orders, Review
from semester.helpers import create_basket, basket_update, basket_clean
from semester.forms import ReviewForm, TownForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TownForm()
    create_basket()
    if request.method == "GET":
        return render_template(
            'index.html',
            menu_url=MainMenu.query.all(),
            user=db.session.query(User).filter(User.id == current_user.get_id()).first(),
            p_amount=len(session['basket']),
            form=form
        )
