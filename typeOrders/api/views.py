from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from typeOrders.models import Types
from typeOrders.api.serializers import TypesSerializer


class TypesApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TypesSerializer
    queryset = Types.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
