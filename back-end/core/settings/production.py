import os

from .common import *

DEBUG = False

BASE_URL = 'https://wordy-en.herokuapp.com'

SECRET_KEY = os.environ['SECRET_KEY']
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PORT': os.environ['DATABASE_PORT'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
    }
}


MIN_LENGTH_PASSWORD = 8
