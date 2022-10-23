from flask_admin import form

from extensions import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.Unicode(128))

    @property
    def thumbnail(self):
        return form.thumbgen_filename(self.image) if self.image else None
