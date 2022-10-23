import os.path

from flask_admin import form

import settings


def del_image(mapper, connection, target):
    if target.path:
        try:
            os.remove(os.path.join(settings.MEDIA_DIR, target.path))
        except OSError:
            pass

        try:
            os.remove(os.path.join(settings.MEDIA_DIR, form.thumbgen_filename(target.path)))
        except OSError:
            pass
