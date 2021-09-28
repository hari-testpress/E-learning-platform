from .base import *

DEBUG = False

ADMINS = (("Antonio M", "email@mydomain.com"),)

ALLOWED_HOSTS = [".educaproject.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "educa",
        "USER": "hari",
        "PASSWORD": "1234",
    }
}
