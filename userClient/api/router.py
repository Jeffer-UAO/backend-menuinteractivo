from rest_framework.routers import DefaultRouter

from userClient.api.views import UserClientApiViewSet

router_userClient = DefaultRouter()

router_userClient.register(
    prefix='userClient', basename='userClient', viewset=UserClientApiViewSet
)
