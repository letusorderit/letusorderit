from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/uid1000/letusorderit/db.sqlite3',
    }
}

STATIC_ROOT = '/home/uid1000/letusorderit/static/'
USE_X_FORWARDED_HOST = True
DEBUG = True
