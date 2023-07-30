from rest_framework.serializers import ModelSerializer
from typeOrders.models import Types


class TypesSerializer(ModelSerializer):
    class Meta:
        model = Types
        fields = ['id', 'code', 'name', 'active']
