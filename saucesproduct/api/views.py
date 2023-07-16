from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


from saucesproduct.models import Sauceproduct
from saucesproduct.api.serializers import SauceproductSerializer


class SauceproductApiViewSet(ModelViewSet):
    Permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SauceproductSerializer
    queryset = Sauceproduct.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'sauces']