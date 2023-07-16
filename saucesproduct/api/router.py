from rest_framework.routers import DefaultRouter

from saucesproduct.api.views import SauceproductApiViewSet

router_saucesproduct = DefaultRouter()

router_saucesproduct.register(
    prefix='saucesproduct', basename='saucesproduct', viewset=SauceproductApiViewSet
)
