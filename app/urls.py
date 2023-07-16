from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.db import router
from django.urls import path, include

from products.api.router import router_product
from users.api.router import router_user
from categories.api.router import router_category
from tables.api.router import router_table
from orders.api.router import router_orders
from orderen.api.router import router_orderen
from payments.api.router import router_payments
from sauce.api.router import router_sauce
from saucesproduct.api.router import router_saucesproduct
from saucesorden.api.router import router_saucesorden
from salesmans.api.router import router_salesmans
from group.api.router import router_group
from userClient.api.router import router_userClient
from userClientTemp.api.router import router_userClientTemp

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from rest_framework_simplejwt.views import (
#   TokenObtainPairView,
#   TokenRefreshView,
# )


schema_view = get_schema_view(
    openapi.Info(
        title="MarketPlaceRestaurant API",
        default_version='v2.0',
        description="Marketplace for to restaurants",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gerencia@ciberneto.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', include('jump.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_user.urls)),
    path('api/', include(router_category.urls)),
    path('api/', include(router_product.urls)),
    path('api/', include(router_table.urls)),
    path('api/', include(router_orders.urls)),
    path('api/', include(router_orderen.urls)),
    path('api/', include(router_salesmans.urls)),
    path('api/', include(router_payments.urls)),
    path('api/', include(router_sauce.urls)),
    path('api/', include(router_saucesproduct.urls)),
    path('api/', include(router_saucesorden.urls)),
    path('api/', include(router_group.urls)),
    path('api/', include(router_userClient.urls)),
    path('api/', include(router_userClientTemp.urls)),


    #path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # cache_timeout=0 -----> ???
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_ROOT)
