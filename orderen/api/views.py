from rest_framework.viewsets import ModelViewSet


from orderen.models import Orderen
from orderen.api.serializers import OrderenSerializer


class OrderenApiViewSet(ModelViewSet):
    serializer_class = OrderenSerializer
    queryset = Orderen.objects.all()
    ordering_fields = '__all__'
