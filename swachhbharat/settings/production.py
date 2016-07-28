import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['SB_DB_NAME'],
        'USER': os.environ['SB_DB_USER'],
        'PASSWORD': os.environ['SB_DB_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
