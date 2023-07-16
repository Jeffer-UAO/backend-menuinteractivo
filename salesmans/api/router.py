from rest_framework.routers import DefaultRouter

from salesmans.api.views import SalesmanApiViewSet

router_salesmans = DefaultRouter()

router_salesmans.register(
    prefix='salesman', basename='salesman', viewset=SalesmanApiViewSet
)
