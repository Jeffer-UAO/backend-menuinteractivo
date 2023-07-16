from rest_framework.viewsets import ModelViewSet

from userClient.models import UserClient
from userClient.api.serializers import UserClientSerializer


class UserClientApiViewSet(ModelViewSet):
    serializer_class = UserClientSerializer
    queryset = UserClient.objects.all()
