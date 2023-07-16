from rest_framework.viewsets import ModelViewSet

from userClientTemp.models import UserClientTemp
from userClientTemp.api.serializers import UserClientTempSerializer


class UserClientTempApiViewSet(ModelViewSet):
    serializer_class = UserClientTempSerializer
    queryset = UserClientTemp.objects.all()
