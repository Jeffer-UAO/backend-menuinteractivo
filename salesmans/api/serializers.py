from rest_framework.serializers import ModelSerializer

from salesmans.models import Salesman


class SalesmanSerializer(ModelSerializer):

    class Meta:
        model = Salesman
        fields = ['id', 'description', 'active']
