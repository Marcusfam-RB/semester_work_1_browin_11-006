from flask import session, request


def create_basket():
    session['basket'] = []
    session['total'] = 0


def basket_update():
    if not session.get('basket'):
        create_basket()

        session['basket'] += [{
            'product_id': request.form.get('id'),
            'product_name': request.form.get('name'),
            'product_image': request.form.get('image'),
            'product_price': int(request.form.get('price')),
            'product_quantity': 1
        }]
        print("))")
    else:
        for s in session['basket']:
            print(s)
            if s['product_id'] == request.form.get('id'):
                s['product_quantity'] += 1
                s['product_price'] += int(request.form.get('price'))
                session['total'] += int(request.form.get('price'))
                return str(len(session['basket']))

        session['basket'] += [{
            'product_id': request.form.get('id'),
            'product_name': request.form.get('name'),
            'product_image': request.form.get('image'),
            'product_price': int(request.form.get('price')),
            'product_quantity': 1
            }]

    session['total'] += int(request.form.get('price'))
    return str(len(session['basket']))


def basket_clean():
    session.pop('basket', None)
    session.pop('total', None)
    return 'Visits deleted'


TOWNLIST = [
    'Казань',
    'Москва',
    'Санкт-Петербург',
    'Сочи',
    'Самара',
    'Новороссийск',
    'Нижний Новгород',
    'Омск',
    'Норильск',
    'Саратов',
    'Ульяновск',
    'Калининград'
]
