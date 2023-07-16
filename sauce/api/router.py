from rest_framework.routers import DefaultRouter

from sauce.api.views import SauceApiViewSet

router_sauce = DefaultRouter()

router_sauce.register(
    prefix='sauce', basename='sauce', viewset=SauceApiViewSet
)
