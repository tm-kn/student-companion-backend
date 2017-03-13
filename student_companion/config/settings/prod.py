import os

from .base import *

SECRET_KEY = 'testprodkey'

DEBUG = False

ALLOWED_HOSTS = ['django.sc.tmkn.uk']

CORS_ORIGIN_ALLOW_ALL = True

GOOGLE_PLACES_API_KEY = 'AIzaSyCL9oi9bAt0LKDNDoIlacveotaMzt80fus'

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

CORS_ORIGIN_ALLOW_ALL = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MEDIA_URL = 'https://django.sc.tmkn.uk/media/'

STATIC_URL = 'https://django.sc.tmkn.uk/static/'
