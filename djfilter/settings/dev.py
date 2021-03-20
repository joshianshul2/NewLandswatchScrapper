'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['*']
DEBUG = True
CORS_ORIGIN_WHITELIST = [
    'https://localhost:3000'
]
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
]

WSGI_APPLICATION = 'djfilter.wsgi.dev.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Rishu',
        'USER': 'postgres',
        'PASSWORD':'anshul123',
        'HOST':'localhost',
        # 'PORT' :5432
        'listen_addresses':'*'
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)
