from rest_framework.routers import DefaultRouter

from saucesorden.api.views import SauceordenApiViewSet

router_saucesorden = DefaultRouter()

router_saucesorden.register(
    prefix='sauceorder', basename='sauceorder', viewset=SauceordenApiViewSet
)
