# main.py
import os
from flask import current_app, send_from_directory, abort

def service(module):
    """
    Devuelve siempre descarga.png que está en <tu_app>/images.
    El parámetro 'module' lo ignoras por ahora.
    """
    images_dir = os.path.join(current_app.root_path, 'images')

    try:
        return send_from_directory(
            images_dir,
            "descarga.png",
            as_attachment=False,        # True = fuerza descarga; False = la muestra inline
            cache_timeout=31536000      # 1 año de caché si lo necesitas
        )
    except FileNotFoundError:
        abort(404)
