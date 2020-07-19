
from .common import *

DEBUG = True

BASE_URL = 'http://127.0.0.1:8000'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!lhzji^^an!8b9^kzt=0q0!op=ton7hg#iwzndp+fb@br)*iy$'
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
# SECURITY WARNING: don't run with debug turned on in production!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIN_LENGTH_PASSWORD = 4