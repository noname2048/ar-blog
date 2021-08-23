from django.core.exceptions import ImproperlyConfigured
from dotenv import dotenv_values

from .base import *


config = dotenv_values(BASE_DIR / "secrets.env")
SECRET_KEY = config.get("SECRET_KEY")
if SECRET_KEY is None:
    raise ImproperlyConfigured("SECRET_KEY ERROR")

DEBUG = False

ALLOWED_HOSTS = [".elasticbeanstalk.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config.get("DATABASE_NAME"),
        "USER": config.get("DATABASE_USER"),
        "PASSWORD": config.get("DATABASE_PASSWORD"),
        "HOST": config.get("DATABASE_HOST"),
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
