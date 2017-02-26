import os

from .base import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['138.68.151.100']

CORS_ORIGIN_ALLOW_ALL = True

GOOGLE_PLACES_API_KEY = 'AIzaSyDO02iLFQF0pKitcUla-RUtCELpyF6OS2U'

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'studentcompanion',
#        'USER': 'studentcompanion',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR.parent.joinpath('db.sqlite3'))
    }
}
