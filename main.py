from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


@app.route('/')
def main_page():
    title = 'Аптека'
    page_name = 'главная страница'
    description = 'Вязанные изделия любой сложности из наличия и на заказ'
    submenu = [
        {'title': 'Выбрать модель'},
        {'title': 'Заказать из наличия'},
        {'title': 'Помощь специалиста'},
    ]
    menu = [
        {'title': 'Доставка и оплата'},
        {'title': 'О нас'},
        {'title': 'Контакты'},
        {'title': 'Каталог', 'submenu': submenu},
    ]
    filters = [
        {'name': 'Цвет'},
        {'name': 'Шерсть'},
        {'name': 'Пошив'},
        {'name': 'Узоры'},
        {'name': 'Пол'},
        {'name': 'Размер'},
        {'name': 'Страна'},
        {'name': 'Забрать из наличия'},
    ]
    context = {
        'title': title,
        'page_name': page_name,
        'description': description,
        'menu': menu,
        'filters': filters,
    }
    return render_template('main.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
