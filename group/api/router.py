from rest_framework.routers import DefaultRouter
from group.api.views import GroupApiViewSet

router_group = DefaultRouter()

router_group.register(
    prefix='group', basename='group', viewset=GroupApiViewSet
)
