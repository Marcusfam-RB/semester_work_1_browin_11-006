from semester import db
import datetime


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    password = db.Column(db.String())
    name = db.Column(db.String())
    phone_number = db.Column(db.String())
    address = db.Column(db.String())

    def __init__(self, email, password, name, phone_number="Не указан", address="Не указан"):
        self.email = email
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f""


class MenuPosition(db.Model):
    __tablename__ = 'MenuPosition'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    images = db.Column(db.String())
    price = db.Column(db.Integer())
    composition = db.Column(db.String())
    type = db.Column(db.String())

    def __init__(self, name, images, price, composition, type):
        self.name = name
        self.images = images
        self.price = price
        self.composition = composition
        self.type = type

    def __repr__(self):
        return f""


class Orders(db.Model):
    __tablename__ = 'Orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('User.id'))
    address = db.Column(db.String())
    phone_number = db.Column(db.String())
    cost = db.Column(db.Integer())
    time = db.Column(db.DateTime())
    is_done = db.Column(db.Boolean())

    def __init__(self, user_id, address, phone_number, cost, time=datetime.datetime.now(), is_done=False):
        self.user_id = user_id
        self.address = address
        self.phone_number = phone_number
        self.cost = cost
        self.time = time
        self.is_done = is_done

    def __repr__(self):
        return f""


class OrdersPositions(db.Model):
    __tablename__ = 'OrdersPositions'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.ForeignKey('Orders.id'))
    position_id = db.Column(db.ForeignKey('MenuPosition.id'))
    quantity = db.Column(db.Integer())

    def __init__(self, order_id, position_id, quantity):
        self.order_id = order_id
        self.position_id = position_id
        self.quantity = quantity

    def __repr__(self):
        return f""


class MainMenu(db.Model):
    __tablename__ = 'MainMenu'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    url = db.Column(db.String())

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return f""


class Review(db.Model):
    __tablename__ = 'Review'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('User.id'))
    text = db.Column(db.String())
    time = db.Column(db.DateTime())

    def __init__(self, text, user_id, time=datetime.datetime.now()):
        self.user_id = user_id
        self.text = text
        self.time = time

    def __repr__(self):
        return f""
