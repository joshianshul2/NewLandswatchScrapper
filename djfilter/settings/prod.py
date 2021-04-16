'''Use this for production'''

from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]
WSGI_APPLICATION = 'djfilter.wsgi.prod.application'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djfilter.settings.prod")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'PropMaster',
        'USER': 'postgres',
        'PASSWORD':'anshul123',
        'HOST':'localhost',
        'PORT' :"5432",
        'listen_addresses':'*',
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'LandScrap',
#         'USER': 'LandScrap',
#         'PASSWORD':'w87zhetrhgxdvo21',
#         'HOST':'db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com',
#         'PORT' :'25060',
#         'listen_addresses':'*',
#         'DISABLE_SERVER_SIDE_CURSORS': True,
#     }
# }





# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'http://localhost:8000',
#     'http://localhost:8080',
# ]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
