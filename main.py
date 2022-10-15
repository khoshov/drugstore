from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

# create the extension
db = SQLAlchemy()


@app.route('/')
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
    products = [
        {
            'name': 'Аддералл',
            'image_path': 'img/aderall.jpg',
            'description': 'Полное название сульфат декстроамфетамина, сахарат декстроамфетамина, сульфат амфетамина и аспартат амфетамина - комбинированный препарат, сочетающий четыре соли амфетаминов.'
        },
        {
            'name': 'Кодеин',
            'image_path': 'img/codein.jpg',
            'description': '3-метилморфин, алкалоид опиума, используется как противокашлевое лекарственное средство центрального действия, обычно в сочетании с другими веществами. Обладает слабым наркотическим и болеутоляющим эффектом, в связи с чем используется также как компонент болеутоляющих лекарств.'
        },
        {
            'name': 'Фентанил',
            'image_path': 'img/fentanyl.jpg',
            'description': 'Опиоидный анальгетик, мощный агонист μ-опиоидных рецепторов. Выпускается в виде цитрата. Применяется главным образом как анальгетик в анестезиологии.'
        },
        {
            'name': 'Ксанакс',
            'image_path': 'img/xanax.jpg',
            'description': 'Лекарственное средство, анксиолитик, производное бензодиазепина средней продолжительности действия, которое используется для лечения панических расстройств, тревожных неврозов, таких как тревожное расстройство или социофобия.'
        },
    ]
    context = {
        'title': title,
        'description': description,
        'menu': menu,
        'products': products,
    }
    return render_template('main.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
