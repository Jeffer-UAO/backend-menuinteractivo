from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from sauce.models import Sauce
from sauce.api.serializers import SauceSerializer


class SauceApiViewSet(ModelViewSet):
    Permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SauceSerializer
    queryset = Sauce.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']
