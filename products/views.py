from flask import Blueprint, render_template
from flask import request

from extensions import db
from products.models import Product

blueprint = Blueprint('products', __name__, url_prefix='/', static_folder='../static')


@blueprint.route('/')
def main_page():
    title = 'Аптека'
    description = 'Надёжный поставщик качественных лекарственных средств'
    submenu = [
        {'title': 'Заказать из наличия'},
        {'title': 'Помощь специалиста'},
    ]
    menu = [
        {'title': 'Доставка и оплата'},
        {'title': 'О нас'},
        {'title': 'Контакты'},
        {'title': 'Каталог', 'submenu': submenu},
    ]

    discount = request.args.get('discount')

    if discount:
        products = db.session.execute(db.select(Product).filter(Product.discount_id != None)).scalars()
    else:
        products = db.session.execute(db.select(Product)).scalars()

    context = {
        'title': title,
        'description': description,
        'menu': menu,
        'products': products,
    }
    return render_template('main.html', **context)


@blueprint.route('/add')
def add_product():
    pass
