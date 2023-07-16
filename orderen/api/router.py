from rest_framework.routers import DefaultRouter

from orderen.api.views import OrderenApiViewSet

router_orderen = DefaultRouter()


router_orderen.register(
    prefix='orderen', basename='orderen', viewset=OrderenApiViewSet
)
