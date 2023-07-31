from .base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_restaurant',
        'USER': 'dev_restaurant',
        'PASSWORD': 'D3s4rr0ll0',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
