from flask import Flask
from sqlalchemy.event import listens_for

from core.admin import ImageView, del_image
from extensions import admin, db, migrate
from products.models import Product
from products.views import blueprint as product_pb


def create_app(config_object="settings"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    register_admin()
    register_signals()

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(product_pb)
    return None


def register_admin():
    admin.add_view(ImageView(Product, db.session))


def register_signals():
    listens_for(del_image, Product, 'after_delete')
