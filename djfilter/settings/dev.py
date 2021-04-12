'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['64.227.16.16',]
DEBUG = True
# CORS_ORIGIN_WHITELIST = [
#     'https://localhost:3000'
# ]
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'http://localhost:8000',
#     'http://localhost:8080',
# ]

WSGI_APPLICATION = 'djfilter.wsgi.dev.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'PropMaster',
#         'USER': 'postgres',
#         'PASSWORD':'anshul123',
#         'HOST':'localhost',
#         # 'PORT' :5432
#         'listen_addresses':'*',
#         'DISABLE_SERVER_SIDE_CURSORS': True,
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'LandScrap',
        'USER': 'LandScrap',
        'PASSWORD':'w87zhetrhgxdvo21',
        'HOST':'db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com',
        'PORT' :'25060',
        'listen_addresses':'*'
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


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'rishu',
#         'USER': 'postgres',
#         'PASSWORD':'anshul123',
#         'HOST':'localhost',
#         # 'PORT' :5432
#         'listen_addresses':'*'
#     }
# }

# CORS_ORIGIN_WHITELIST = (
#     'localhost:3000',
# )
