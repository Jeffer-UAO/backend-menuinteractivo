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
        'PASSWORD': 'Ptq6T8UtPTZwIRXOFDt8',
        'HOST': 'containers-us-west-16.railway.app',
        'PORT': '7314',
    }
}

STATIC_URL = '/static/'
