from rest_framework.viewsets import ModelViewSet

from group.models import Group
from group.api.serializers import GroupSerializer


class GroupApiViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

