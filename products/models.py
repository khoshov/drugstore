from flask_admin import form

from extensions import db


class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    products = db.relationship('Product', backref='discount', lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.Unicode(128))
    price = db.Column(db.Integer, nullable=False, default=99)
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'), nullable=True)

    @property
    def thumbnail(self):
        return form.thumbgen_filename(self.image) if self.image else None
