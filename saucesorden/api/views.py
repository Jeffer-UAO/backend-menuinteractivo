from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


from saucesorden.models import Sauceorden
from saucesorden.api.serializers import SauceordenSerializer


class SauceordenApiViewSet(ModelViewSet):
    Permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SauceordenSerializer
    queryset = Sauceorden.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']
