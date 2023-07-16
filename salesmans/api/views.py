from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from salesmans.models import Salesman
from salesmans.api.serializers import SalesmanSerializer


class SalesmanApiViewSet(ModelViewSet):
    Permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SalesmanSerializer
    queryset = Salesman.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']
