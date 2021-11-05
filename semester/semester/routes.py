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


@app.route('/burgers', methods=['POST', 'GET'])
def burgers():
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == "GET":
        return render_template(
            'burgers.html',
            menu_url=MainMenu.query.all(),
            positions=db.session.query(MenuPosition).filter(MenuPosition.type == 'burgers').all(),
            user=user,
            url='burgers',
            p_amount=len(session['basket'])
        )


@app.route('/pizza', methods=['POST', 'GET'])
def pizza():
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == "GET":
        return render_template(
            'pizza.html',
            menu_url=MainMenu.query.all(),
            positions=db.session.query(MenuPosition).filter(MenuPosition.type == 'pizza').all(),
            user=user,
            url='pizza',
            p_amount=len(session['basket'])
        )


@app.route('/snacks', methods=['POST', 'GET'])
def snacks():
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == "GET":
        return render_template(
            'snacks.html',
            menu_url=MainMenu.query.all(),
            positions=db.session.query(MenuPosition).filter(MenuPosition.type == 'snack').all(),
            user=user,
            url='snacks',
            p_amount=len(session['basket'])
        )


@app.route('/sauces', methods=['POST', 'GET'])
def sauces():
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == "GET":
        return render_template(
            'sauces.html',
            menu_url=MainMenu.query.all(),
            positions=db.session.query(MenuPosition).filter(MenuPosition.type == 'sauce').all(),
            user=user,
            url='sauces',
            p_amount=len(session['basket'])
        )


@app.route('/drinks', methods=['POST', 'GET'])
def drinks():
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == 'GET':
        return render_template(
            'drinks.html',
            menu_url=MainMenu.query.all(),
            positions=db.session.query(MenuPosition).filter(MenuPosition.type == 'drink').all(),
            user=user,
            url='drinks',
            p_amount=len(session['basket'])
        )


@app.route('/about', methods=['GET'])
def about():
    if request.method == "GET":
        return render_template(
            'about.html',
            menu_url=MainMenu.query.all(),
            user=db.session.query(User).filter(User.id == current_user.get_id()).first(),
            p_amount=len(session['basket'])
        )


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ReviewForm()
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == "GET":
        return render_template(
            'contacts.html',
            menu_url=MainMenu.query.all(),
            user=user,
            p_amount=len(session['basket']),
            form=form
        )
    elif request.method == 'POST':
        text = request.form['review']
        review = Review(text, user.id)
        db.session.add(review)
        db.session.commit()
        flash('Спасибо за ваш отзыв!', category='success')
        return render_template(
            'contacts.html',
            menu_url=MainMenu.query.all(),
            user=user,
            p_amount=len(session['basket']),
            form=form
        )


@app.route('/basket', methods=['POST', 'GET'])
@login_required
def basket():
    user = db.session.query(User).filter(User.id == current_user.get_id()).first()
    if request.method == 'GET':
        return render_template(
            'basket.html',
            menu_url=MainMenu.query.all(),
            user=user,
            basket=session['basket'],
            total=session['total'],
            p_amount=len(session['basket'])
        )
    elif request.method == 'POST':
        if session['total'] == 0:
            flash("Ваша корзина пуста", category="validation_error")
            return render_template(
                'basket.html',
                menu_url=MainMenu.query.all(),
                user=user,
                basket=session['basket'],
                total=session['total'],
                p_amount=len(session['basket'])
            )
        address = request.form['address']
        phone_number = request.form['number']
        order = Orders(user.id, address, phone_number, session['total'])
        db.session.add(order)
        db.session.commit()
        for p in session['basket']:
            position = OrdersPositions(order.id, p['product_id'], p['product_quantity'])
            db.session.add(position)
            db.session.commit()
        db.session.commit()
        basket_clean()
        return redirect(url_for('index'))
