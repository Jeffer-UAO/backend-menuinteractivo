from rest_framework.routers import DefaultRouter

from typeOrders.api.views import TypesApiViewSet

router_types = DefaultRouter()

router_types.register(
    prefix='types', basename='types', viewset=TypesApiViewSet
)
