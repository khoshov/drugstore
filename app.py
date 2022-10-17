import os
import os.path as op

from flask import Flask, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup
from sqlalchemy.event import listens_for
from flask_admin import Admin, form
from flask_admin.contrib import sqla

app = Flask(__name__, static_folder='media')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SECRET_KEY'] = '123456790'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app, name='drugstore', template_mode='bootstrap4')


image_path = op.join(op.dirname(__file__), 'files')
try:
    os.mkdir(image_path)
except OSError:
    pass


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.Unicode(128))

    @property
    def thumbnail(self):
        return form.thumbgen_filename(self.image) if self.image else None


class ImageView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        return Markup('<img src="%s">' % url_for('static', filename=model.thumbnail))

    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {
        'image': form.ImageUploadField('Image', base_path=image_path, thumbnail_size=(320, 240, True))
    }


admin.add_view(ImageView(Product, db.session))


@listens_for(Product, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(image_path, target.path))
        except OSError:
            pass

        try:
            os.remove(op.join(image_path,
                              form.thumbgen_filename(target.path)))
        except OSError:
            pass


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
    # products = [
    #     {
    #         'name': 'Аддералл',
    #         'image_path': 'img/aderall.jpg',
    #         'description': 'Полное название сульфат декстроамфетамина, сахарат декстроамфетамина, сульфат амфетамина и аспартат амфетамина - комбинированный препарат, сочетающий четыре соли амфетаминов.'
    #     },
    #     {
    #         'name': 'Кодеин',
    #         'image_path': 'img/codein.jpg',
    #         'description': '3-метилморфин, алкалоид опиума, используется как противокашлевое лекарственное средство центрального действия, обычно в сочетании с другими веществами. Обладает слабым наркотическим и болеутоляющим эффектом, в связи с чем используется также как компонент болеутоляющих лекарств.'
    #     },
    #     {
    #         'name': 'Фентанил',
    #         'image_path': 'img/fentanyl.jpg',
    #         'description': 'Опиоидный анальгетик, мощный агонист μ-опиоидных рецепторов. Выпускается в виде цитрата. Применяется главным образом как анальгетик в анестезиологии.'
    #     },
    #     {
    #         'name': 'Ксанакс',
    #         'image_path': 'img/xanax.jpg',
    #         'description': 'Лекарственное средство, анксиолитик, производное бензодиазепина средней продолжительности действия, которое используется для лечения панических расстройств, тревожных неврозов, таких как тревожное расстройство или социофобия.'
    #     },
    # ]

    products = db.session.execute(db.select(Product)).scalars()
    context = {
        'title': title,
        'description': description,
        'menu': menu,
        'products': products,
    }
    return render_template('main.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
