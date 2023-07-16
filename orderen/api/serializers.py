from rest_framework.serializers import ModelSerializer
from orderen.models import Orderen


class OrderenSerializer(ModelSerializer):
    class Meta:
        model = Orderen
        fields = ['id', 'tipo']
