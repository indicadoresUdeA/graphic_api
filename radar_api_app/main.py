# main.py
import os
from flask import current_app, send_from_directory, abort


def get_image(filename):
    """Return an image file from the images directory."""
    images_dir = os.path.join(current_app.root_path, 'images')
    try:
        return send_from_directory(
            images_dir,
            filename,
            as_attachment=False,
            cache_timeout=31536000
        )
    except FileNotFoundError:
        abort(404)

def service(module):
    """Return a URL where the generated image can be accessed."""
    filename = "descarga.png"
    url = f"http://46.202.177.37/service/radar/{filename}"
    return url
