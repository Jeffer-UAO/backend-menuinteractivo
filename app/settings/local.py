from .base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django_tenants.postgresql_backend',
#         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'menudigital',
#         'USER': 'SYSDBA',
#         'PASSWORD': 'D3s4rr0ll0',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'q3XXoUn9t6oEKlvxbeue',
        'HOST': 'containers-us-west-61.railway.app',
        'PORT': '6995',
    }
}

STATIC_URL = '/static/'
