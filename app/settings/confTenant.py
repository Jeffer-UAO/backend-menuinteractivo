SHARED_APPS = (
    'django_tenants',
    'customers',
    'django.contrib.contenttypes',
    'django.contrib.sites',


)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'users',
    'simple_history',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
)


MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
]


DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

TENANT_MODEL = "customers.Client"
TENANT_DOMAIN_MODEL = "customers.Domain"


INSTALLED_APPS = list(SHARED_APPS) + \
    [app for app in TENANT_APPS if app not in SHARED_APPS]
