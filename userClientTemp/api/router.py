from rest_framework.routers import DefaultRouter

from userClientTemp.api.views import UserClientTempApiViewSet

router_userClientTemp = DefaultRouter()

router_userClientTemp.register(
    prefix='userClientTemp', basename='userClientTemp', viewset=UserClientTempApiViewSet
)