from flask import Blueprint, render_template

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

    products = db.session.execute(db.select(Product)).scalars()
    context = {
        'title': title,
        'description': description,
        'menu': menu,
        'products': products,
    }
    return render_template('main.html', **context)
