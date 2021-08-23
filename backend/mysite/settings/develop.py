from django.core.exceptions import ImproperlyConfigured
from dotenv import dotenv_values

from .base import *


config = dotenv_values(BASE_DIR / "secrets.env")
SECRET_KEY = config.get("SECRET_KEY")
if SECRET_KEY is None:
    raise ImproperlyConfigured("SECRET_KEY ERROR")

DEBUG = True

ALLOWED_HOSTS = []  # "localhost", "127.0.0.1"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
