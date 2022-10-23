import os
import os.path as op

from flask import url_for
from flask_admin import form
from flask_admin.contrib import sqla
from markupsafe import Markup
from sqlalchemy.event import listens_for

import settings
from products.models import Product

try:
    os.mkdir(settings.MEDIA_DIR)
except OSError:
    pass


@listens_for(Product, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(settings.MEDIA_DIR, target.path))
        except OSError:
            pass

        try:
            os.remove(op.join(settings.MEDIA_DIR, form.thumbgen_filename(target.path)))
        except OSError:
            pass


class ImageView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        return Markup('<img src="%s">' % url_for('static', filename=model.thumbnail))

    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {
        'image': form.ImageUploadField('Image', base_path=settings.MEDIA_DIR, thumbnail_size=(320, 240, True))
    }
