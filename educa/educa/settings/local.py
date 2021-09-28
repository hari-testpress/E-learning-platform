from .base import *
from .base import BASE_DIR
import os

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conduit.settings.development")
